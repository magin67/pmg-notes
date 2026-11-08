"""Reproduce English SVGs without changing the graph geometry.

Run the Russian drawing programs first if the source figures have changed.
Every Russian text node must have an explicit translation in the adjacent JSON.
"""
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET


def fit_text(element, old, new):
    """Keep longer translated labels within the source label's width."""
    if not element.tag.endswith('}text') or not element.get('font-size'):
        return
    from PIL import ImageFont
    from matplotlib import font_manager
    weight = 'bold' if element.get('font-weight') == 'bold' else 'normal'
    font = ImageFont.truetype(font_manager.findfont(
        font_manager.FontProperties(family='DejaVu Sans', weight=weight)), 100)
    ratio = font.getlength(old) / max(1, font.getlength(new))
    if ratio < 1:
        element.set('font-size', f"{float(element.get('font-size')) * ratio:.3f}")

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'pmg-library/ru/Преобразования и сочленения графов/Цепи из ядер/images'
TARGET = ROOT / 'pmg-library/en/Graph Transformations and Gluing/Chains of cores/images'
DATA = json.loads(Path(__file__).with_name('figure-translations-en.json').read_text(encoding='utf-8'))
CYRILLIC = re.compile('[А-Яа-яЁё]')
ET.register_namespace('', 'http://www.w3.org/2000/svg')


def main():
    TARGET.mkdir(parents=True, exist_ok=True)
    count = 0
    for filename, entry in DATA.items():
        tree = ET.parse(SOURCE / filename)
        used = set()
        for element in tree.iter():
            if element.text and CYRILLIC.search(element.text):
                source_text = element.text
                element.text = entry['text'][source_text]
                if entry.get('fit_text'):
                    fit_text(element, source_text, element.text)
                used.add(source_text)
            for key, value in element.attrib.items():
                if CYRILLIC.search(value):
                    element.set(key, entry['text']['@' + key + '=' + value])
                    used.add('@' + key + '=' + value)
        assert used == set(entry['text']), (filename, 'Unused or missing translations')
        text = ET.tostring(tree.getroot(), encoding='unicode')
        assert not CYRILLIC.search(text), (filename, 'Untranslated Cyrillic')
        (TARGET / entry['file']).write_text(text + '\n', encoding='utf-8')
        count += 1
    print(f'Translated {count} SVGs, including titles and descriptions.')


if __name__ == '__main__':
    main()
