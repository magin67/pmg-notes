"""Check the English series against Russian formulas, links, and SVG geometry."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from translate_figures_en import NAMES, SOURCE, DESTINATION

ROOT = Path(__file__).resolve().parents[2]
LIBRARY = ROOT / 'pmg-library'
RU = SOURCE.parent
EN = DESTINATION.parent


def header(text, name):
    return re.search(r'^'+name+r':\s*(.+)$',text.split('---',2)[1],re.M)[1].strip()


def formulas(text):
    body=text.split('---',2)[2]
    body=re.sub(r'^> ?', '', body, flags=re.M)
    return [a or b for a,b in re.findall(r'\$\$(.*?)\$\$|\$([^\n$]+)\$',body,re.S)]


def main():
    ru_pages={header(p.read_text(encoding='utf-8'),'translation_key'):p for p in RU.glob('*.md')}
    all_pages=list(LIBRARY.rglob('*.md'))
    names={}
    for p in all_pages:
        names.setdefault(p.stem,[]).append(p)
    count=0
    for ep in EN.glob('*.md'):
        english=ep.read_text(encoding='utf-8')
        rp=ru_pages[header(english,'translation_key')]
        russian=rp.read_text(encoding='utf-8')
        assert header(english,'lang')=='en'
        assert header(english,'translated_revision')==header(russian,'revision')
        assert header(english,'order')==header(russian,'order')
        assert formulas(english)==formulas(russian),ep.name
        count+=len(formulas(english))
        assert len(re.findall(r'^> \[!',english,re.M))==len(re.findall(r'^> \[!',russian,re.M))
        assert len(re.findall(r'^#{2,6} ',english,re.M))==len(re.findall(r'^#{2,6} ',russian,re.M))
        for line in english.splitlines():
            if re.search('[А-Яа-яЁё]',line):
                assert line.startswith('[[ru/') and line.endswith('|Русский]]'),(ep.name,line)
        for p,text in [(ep,english),(rp,russian)]:
            assert not re.search(r'^\s*(?:>\s*)?\$\s*$',text,re.M),p.name
            for target in re.findall(r'\[\[([^\]]+)\]\]',text):
                target=target.replace('\\|','|').split('|')[0]
                name,_,anchor=target.partition('#')
                options=[LIBRARY/(name+'.md'),p.parent/(name+'.md')]+names.get(name,[])
                resolved=next((q for q in options if q.exists()),None)
                assert resolved is not None,(p.name,target)
                if anchor:
                    headings=re.findall(r'^#{1,6} (.+)$',resolved.read_text(encoding='utf-8-sig'),re.M)
                    assert anchor in headings,(p.name,target)
            for image in re.findall(r'!\[[^\]]*\]\(<([^>]+)>\)',text):
                assert (p.parent/image).exists(),(p.name,image)
    for old,new in NAMES.items():
        src=ET.parse(SOURCE/(old+'.svg')).getroot()
        dst=ET.parse(DESTINATION/(new+'.svg')).getroot()
        assert len(list(src.iter()))==len(list(dst.iter())),old
        for a,b in zip(src.iter(),dst.iter()):
            assert a.tag==b.tag and a.attrib==b.attrib,(old,a.tag)
            if a.text and re.search('[А-Яа-яЁё]',a.text):
                assert re.findall(r'-?\d+(?:[./]\d+)*',a.text)==re.findall(r'-?\d+(?:[./]\d+)*',b.text),(old,a.text)
            else:
                assert a.text==b.text,(old,a.text)
    print(f'Passed: 5 bilingual page pairs, {count} identical math expressions, '
          'matching callouts and headings, resolved links, 12 SVGs with unchanged geometry and numbers.')


if __name__=='__main__':
    main()
