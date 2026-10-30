"""Reproduce the English SVGs from the reviewed Russian figures (stdlib only)."""
from pathlib import Path
import argparse
import html
import json
import re
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
LIBRARY = HERE.parents[1] / 'pmg-library'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=LIBRARY)
    parser.add_argument('--destination', type=Path, default=LIBRARY)
    args = parser.parse_args()
    data = json.loads((HERE / 'figure_translations_en.json').read_text(encoding='utf-8'))
    source = args.source / 'ru/Граничные полиномы и сочленение графов'
    destination = args.destination / 'en/Boundary polynomials and graph gluing'
    destination.mkdir(parents=True, exist_ok=True)
    used = set()
    for ru, en in data['files'].items():
        original = (source / ru).read_text(encoding='utf-8')

        def translate(match):
            text = html.unescape(match[1])
            if not re.search('[А-Яа-яЁё]', text):
                return match[0]
            assert text in data['labels'], (ru, text)
            used.add(text)
            return '>' + html.escape(data['labels'][text], quote=False) + '<'

        translated = re.sub(r'>([^<>]+)<', translate, original)
        assert not re.search('[А-Яа-яЁё]', translated), ru
        # Geometry, edge weights, partition labels, and all nontext nodes are retained.
        a, b = ET.fromstring(original), ET.fromstring(translated)
        assert len(list(a.iter())) == len(list(b.iter()))
        for x, y in zip(a.iter(), b.iter()):
            assert x.tag == y.tag and x.attrib == y.attrib
        (destination / en).write_text(translated, encoding='utf-8')
    assert used == set(data['labels']), 'Unused translations: ' + str(set(data['labels']) - used)
    print(f'Reproduced {len(data["files"])} English SVGs; {len(used)} distinct texts translated.')


if __name__ == '__main__':
    main()
