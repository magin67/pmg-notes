"""Check RU/EN parity of the two weaving notes; standard library only.

Checks preserve formulas, numerical data, callout states, links, and native
figure geometry. Mathematical truth is checked independently by verify_weaving
and verify_weaving_exponential, not established by translation parity.
"""
from collections import Counter
from pathlib import Path
from urllib.parse import unquote
import json
import re
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
LIB = HERE.parents[1] / 'pmg-library'
RU = LIB / 'ru/Преобразования и сочленения графов/Цепи из ядер'
EN = LIB / 'en/Graph Transformations and Gluing/Chains of cores'
PAIRS = [
    ('Плетение графов - вилка, розетка и рекурсия', 'Weaving Graphs - Plug Socket and Recurrence'),
    ('Экспонента лапласиана при плетении графов', 'The Laplacian Exponential in Graph Weaving'),
]
TEX = {r'\text{Б}': r'\text{B}', r'\text{квадраты}': r'\text{squares}',
       r'\text{ - лес}': r'\text{ is a forest}', r'\text{ закрыта}': r'\text{ closed}'}


def field(text, name):
    return re.search(r'^'+name+r': (.+)$', text.split('---', 2)[1], re.M)[1].strip('\"\'')


def formulas(text):
    return re.findall(r'\$\$[\s\S]*?\$\$|\$[^$\n]+\$', re.sub(r'^> ?', '', text, flags=re.M))


def tables(text):
    width = None
    for i, line in enumerate(text.splitlines(), 1):
        line = re.sub(r'^> ?', '', line).strip()
        if not line.startswith('|'):
            width = None
            continue
        for link in re.findall(r'\[\[[^\]]+\]\]', line):
            assert not re.search(r'(?<!\\)\|', link), (i, 'unescaped alias')
        size = len(re.findall(r'(?<!\\)\|', line)) - 1
        if width is None:
            width = size
        assert size == width, (i, 'table width')


def main():
    counts = dict(pages=0, display_formulas=0, inline_formulas=0, callouts=0,
                  proofs=0, links=0, anchors=0, figures=0, translated_labels=0)
    figures = set()
    for ru, en in PAIRS:
        rp, ep = RU/(ru+'.md'), EN/(en+'.md')
        r, e = rp.read_text(encoding='utf-8'), ep.read_text(encoding='utf-8')
        assert field(e, 'translated_revision') == field(r, 'revision')
        assert field(e, 'translation_key') == field(r, 'translation_key')
        assert field(e, 'order') == field(r, 'order')
        assert ep.relative_to(LIB).with_suffix('').as_posix() in r
        assert rp.relative_to(LIB).with_suffix('').as_posix() in e
        for a, b in TEX.items():
            r = r.replace(a, b)
        rf, ef = formulas(r), formulas(e)
        assert Counter(rf) == Counter(ef), (en, 'formulas')
        assert [s for s in rf if s.startswith('$$')] == [s for s in ef if s.startswith('$$')]
        calls = lambda s: re.findall(r'^> \[!([^\]]+)\](-?)', s, re.M)
        assert calls(r) == calls(e), (en, 'callout sequence and folding')
        def numeric(s):
            body = re.sub(r'\[\[[^\]]+\]\]', '', s.split('---', 2)[2])
            body = re.sub(r'(?<=\]\()[^)]+', '', body)
            return Counter(re.findall(r'\d+', body))
        assert numeric(r) == numeric(e), (en, 'all body numerical data')
        assert not re.search('[А-Яа-яЁё]', re.sub(r'\[\[[^\]]+\]\]', '', e)), en
        assert len(re.findall(r'^#{2,6} ', r, re.M)) == len(re.findall(r'^#{2,6} ', e, re.M))
        tables(r); tables(e)
        for item in re.findall(r'\[\[([^\]]+)\]\]', e):
            target = item.replace('\\|', '|').split('|')[0]
            path, _, anchor = target.partition('#')
            dest = LIB/(path+'.md')
            assert dest.is_file(), (en, target)
            if anchor:
                assert anchor in re.findall(r'^#{2,6} (.+)$', dest.read_text(encoding='utf-8'), re.M), target
                counts['anchors'] += 1
            counts['links'] += 1
        for item in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', e):
            name = unquote(item)
            assert (EN/name).is_file(), name
            figures.add(name)
        counts['pages'] += 1
        counts['display_formulas'] += sum(s.startswith('$$') for s in ef)
        counts['inline_formulas'] += sum(not s.startswith('$$') for s in ef)
        counts['callouts'] += len(calls(e))
        counts['proofs'] += sum(fold == '-' for _, fold in calls(e))
    labels = json.loads((HERE/'figure-translations-en.json').read_text(encoding='utf-8'))
    for source, entry in labels.items():
        if 'images/' + entry['file'] not in figures:
            continue
        r = list(ET.parse(RU/'images'/source).iter())
        raw = (EN/'images'/entry['file']).read_text(encoding='utf-8')
        e = list(ET.fromstring(raw).iter())
        assert not re.search('[А-Яа-яЁё]', raw), entry['file']
        assert len(r) == len(e)
        for a, b in zip(r, e):
            assert a.tag == b.tag
            attrs = lambda x: {k:v for k,v in x.attrib.items() if k != 'font-size'}
            assert attrs(a) == attrs(b), (source, 'geometry')
            if a.text and re.search('[А-Яа-яЁё]', a.text):
                assert b.text == entry['text'][a.text]
            else:
                assert a.text == b.text, (source, 'unchanged mathematical label')
        counts['figures'] += 1
        counts['translated_labels'] += len(entry['text'])
    assert counts['figures'] == 8
    orders = [int(field(p.read_text(encoding='utf-8'), 'order')) for p in EN.glob('*.md')]
    assert sorted(orders) == list(range(8)), ('series order', orders)
    print('PASS: '+json.dumps(counts, sort_keys=True))


if __name__ == '__main__':
    main()
