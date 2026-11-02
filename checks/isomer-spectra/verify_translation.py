"""Check mathematical and structural parity of the RU/EN isomer series.

Run from any directory. Uses only the standard library. The sole TeX changes
allowed are translated words, graph label Б -> B, and equation tags 12а/12б.
This checks parity, not the mathematical truth of the shared statements; use
the independent verification programs documented in README.md for that.
"""
from collections import Counter
from pathlib import Path
from urllib.parse import unquote
import json
import re
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
LIB = HERE.parents[1] / 'pmg-library'
RU = LIB / 'ru/Преобразования и сочленения графов/Спектры изомеров'
EN = LIB / 'en/Graph Transformations and Gluing/Spectra of Isomers'
TEXT = {
    r'\text{Б}':r'\text{B}', r'\tag{12а}':r'\tag{12a}', r'\tag{12б}':r'\tag{12b}',
    r'\text{иначе}':r'\text{otherwise}', r'\text{ - лес}':r'\text{ is a forest}',
    r'\text{компонента }':r'\text{the component of }',
    r'\text{ имеет корень }':r'\text{ is rooted at }',
    r'\text{ оба являются корнями}':r'\text{ are both roots}',
    r'\text{ является корнем}':r'\text{ is a root}',
}


def field(raw, name):
    match = re.search(r'^'+name+r': (.+)$', raw.split('---',2)[1], re.M)
    assert match, name
    return match[1].strip('"\'')


def formulas(raw):
    raw = re.sub(r'^> ?', '', raw, flags=re.M)
    return re.findall(r'\$\$[\s\S]*?\$\$|\$[^$\n]+\$', raw)


def table_numbers(raw):
    return [re.findall(r'\d+',re.sub(r'\[\[[^\]]+\]\]','',line))
            for line in raw.splitlines() if re.match(r'^(?:> )?\|',line)]


def main():
    pairs = {field(p.read_text(encoding='utf-8'),'translation_key'):p for p in RU.glob('*.md')}
    count = dict(pages=0, display_formulas=0, inline_formulas=0, callouts=0,
                 figures=0, image_uses=0, wikilinks=0, anchors=0)
    for p in EN.glob('*.md'):
        en = p.read_text(encoding='utf-8')
        source = pairs.pop(field(en,'translation_key'))
        ru = source.read_text(encoding='utf-8')
        assert field(en,'translated_revision') == field(ru,'revision'), p.name
        assert field(en,'order') == field(ru,'order'), p.name
        assert source.relative_to(LIB).with_suffix('').as_posix() in en
        assert p.relative_to(LIB).with_suffix('').as_posix() in ru
        for a,b in TEXT.items():
            ru = ru.replace(a,b)
        a,b = formulas(ru),formulas(en)
        assert Counter(a) == Counter(b), (p.name,'formulas')
        assert [x for x in a if x.startswith('$$')] == [x for x in b if x.startswith('$$')]
        calls = lambda s: re.findall(r'^> \[!([^\]]+)\](-?)',s,re.M)
        assert calls(ru) == calls(en), (p.name,'callouts')
        assert table_numbers(ru) == table_numbers(en), (p.name,'table numbers')
        assert not re.search('[А-Яа-яЁё]',re.sub(r'\[\[[^\]]+\]\]','',en)), p.name
        for src in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',en):
            assert (EN/unquote(src)).is_file(), (p.name,src)
            count['image_uses'] += 1
        for link in re.findall(r'\[\[([^\]]+)\]\]',en):
            name,_,anchor = link.replace('\\|','|').split('|')[0].partition('#')
            dest = LIB/(name+'.md')
            assert dest.is_file(), (p.name,name)
            count['wikilinks'] += 1
            if anchor:
                assert anchor in re.findall(r'^#{2,6} (.+)$',dest.read_text(encoding='utf-8'),re.M)
                count['anchors'] += 1
        count['pages'] += 1
        count['display_formulas'] += sum(x.startswith('$$') for x in b)
        count['inline_formulas'] += sum(not x.startswith('$$') for x in b)
        count['callouts'] += len(calls(en))
    assert not pairs and count['pages'] == 10
    entries = json.loads((HERE/'figure-labels-en.json').read_text(encoding='utf-8'))
    for entry in entries:
        raw = (EN/entry['target']).read_text(encoding='utf-8')
        assert not re.search('[А-Яа-яЁё]',raw), entry['target']
        if entry['target'] != 'Rooted Forest Growth in Periodic Chains.svg':
            a = list(ET.fromstring((RU/entry['source']).read_text(encoding='utf-8')).iter())
            b = list(ET.fromstring(raw).iter())
            assert len(a) == len(b)
            for x,y in zip(a,b):
                assert x.tag == y.tag
                attrs = lambda e: {k:v for k,v in e.attrib.items() if k!='font-size'}
                assert attrs(x) == attrs(y), (entry['target'],'geometry')
        count['figures'] += 1
    assert count['figures'] == 35 == len(list(EN.glob('*.svg')))
    print('PASS: '+json.dumps(count,sort_keys=True))


if __name__ == '__main__':
    main()
