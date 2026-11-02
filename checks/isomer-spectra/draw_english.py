"""Reproduce the 35 English SVGs without changing graph or numerical data.

Native SVG text is translated from the reviewed Russian figures. Font sizes
may be reduced to keep translated labels within the original text width.
The periodic-growth plot is redrawn from the same exact-results JSON because
the Russian source encodes its labels as glyph paths rather than SVG text.
Requires Matplotlib and Pillow; no mathematical verification file is rewritten.
"""
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

from PIL import ImageFont
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import FormatStrFormatter

HERE = Path(__file__).resolve().parent
LIB = HERE.parents[1] / 'pmg-library'
RU = LIB / 'ru/Преобразования и сочленения графов/Спектры изомеров'
EN = LIB / 'en/Graph Transformations and Gluing/Spectra of Isomers'
LABELS = json.loads((HERE / 'figure-labels-en.json').read_text(encoding='utf-8'))
SVG = 'http://www.w3.org/2000/svg'
ET.register_namespace('', SVG)
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
FONT = ImageFont.truetype(font_manager.findfont('DejaVu Sans'), 100)
CYRILLIC = re.compile('[А-Яа-яЁё]')


def translate_svg(entry):
    root = ET.fromstring((RU / entry['source']).read_text(encoding='utf-8'))
    used = set()
    for element in root.iter():
        for attr in ('text', 'tail'):
            old = getattr(element, attr)
            if old is None or not CYRILLIC.search(old):
                continue
            new = entry['labels'][old]
            used.add(old)
            setattr(element, attr, new)
            if attr == 'text' and element.tag == '{'+SVG+'}text' and element.get('font-size'):
                ratio = FONT.getlength(old) / max(1, FONT.getlength(new))
                if ratio < 1:
                    element.set('font-size', f"{float(element.get('font-size')) * ratio:.3f}")
    assert used == set(entry['labels']), entry['source']
    result = ET.tostring(root, encoding='unicode') + '\n'
    assert not CYRILLIC.search(result), entry['source']
    (EN / entry['target']).write_text(result, encoding='utf-8')


def growth_plot(entry):
    data = json.loads((HERE / 'periodic-slr-results.json').read_text(encoding='utf-8'))
    words = ['LR', 'LLS', 'SL']
    values = [float(data['periods'][w]['at_minus_one']['growth_per_core']) for w in words]
    with plt.rc_context({'font.family':'DejaVu Sans', 'font.size':15,
                         'svg.fonttype':'path', 'svg.hashsalt':'periodic-slr-en'}):
        fig, ax = plt.subplots(figsize=(11.8, 4.7))
        fig.patch.set_facecolor('white')
        ax.set_facecolor('#f7f9fc')
        for i, (word, value, color) in enumerate(zip(words, values, ['#196bb9','#15815b','#bc294b'])):
            ax.plot(value, 2-i, 'o', color=color, markersize=11)
            ax.annotate(f'{value:.6f}', (value, 2-i), xytext=(0,15),
                        textcoords='offset points', ha='center', color=color, fontsize=16)
        ax.set_yticks([2,1,0], words)
        ax.set_ylim(-.5, 2.6)
        ax.set_xlim(88.0, 88.35)
        ax.set_xticks([88.0,88.05,88.1,88.15,88.2,88.25,88.3,88.35])
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
        ax.grid(axis='x', color='#dce4ed')
        ax.set_axisbelow(True)
        for side in ['top','right','left']:
            ax.spines[side].set_visible(False)
        ax.spines['bottom'].set_color('#aab7c6')
        ax.tick_params(axis='y', length=0, pad=12)
        ax.set_xlabel('Limiting rooted forest growth per core', labelpad=17)
        ax.set_title('The period affects the growth rate', fontsize=20, loc='left', pad=24)
        fig.text(.5, .035, 'The comparison uses three cores per LLS period and two per LR or SL period.',
                 ha='center', fontsize=13, color='#52657a')
        fig.subplots_adjust(left=.10, right=.97, top=.80, bottom=.25)
        texts = list(entry['labels'].values())
        fig.savefig(EN / entry['target'], metadata={'Date':None,'Title':texts[0],'Description':texts[1]})
        plt.close(fig)
    p = EN / entry['target']
    p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')


def main():
    EN.mkdir(parents=True, exist_ok=True)
    for entry in LABELS:
        if entry['target'] == 'Rooted Forest Growth in Periodic Chains.svg':
            growth_plot(entry)
        else:
            translate_svg(entry)
    assert len(LABELS) == 35
    print('PASS: 35 English SVGs; translated labels and accessible descriptions; shared exact data.')


if __name__ == '__main__':
    main()
