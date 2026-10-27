"""Rebuild the exact SVG for the Greenian potentials note (standard library)."""
from html import escape
from pathlib import Path


def main():
    target = (Path(__file__).resolve().parents[2] / 'pmg-library' / 'ru'
              / 'Гриниан и дуальность полиформ'
              / 'Заданные значения и энергия в метрике гриниана.svg')
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="850" viewBox="0 0 1040 850" role="img" aria-labelledby="title desc">',
             '<title id="title">Потенциалы и энергия на единичном пути</title>',
             '<desc id="desc">Для пути a-b-c-d показаны заданные значения минус один, один, ноль, ноль с энергией пять; один, один, ноль, ноль с энергией один; и гармонические значения минус один, один, один, один с энергией четыре. Под каждым ребром указана его энергия. Пунктиром обозначены свободные вершины.</desc>',
             '<rect width="1040" height="850" fill="#ffffff"/>',
             '<g font-family="DejaVu Sans, sans-serif" fill="#172b40">']

    def text(x, y, value, size=20, color='#172b40', anchor='start', weight='normal'):
        parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{escape(value)}</text>')

    text(36, 47, 'Один путь, три задания значений', 30, weight='bold')
    text(36, 82, 'Проводимость каждого ребра равна 1. Числа под рёбрами - их вклады в энергию.', 18, '#52667b')
    rows = [
        ('Разность b − a', [-1, 1, 0, 0], [4, 1, 0], 'E = 4 + 1 = 5',
         'Все значения закреплены. На ребре ab перепад равен 2, его вклад равен 4.', False),
        ('Сумма центрированных вершин', [1, 1, 0, 0], [0, 1, 0], 'E = 1',
         'Общий сдвиг значений не меняет энергию. Работает только разрез ab | cd.', False),
        ('Только a = −1 и b = 1 закреплены', [-1, 1, 1, 1], [4, 0, 0], 'min E = 4',
         'Свободные c и d получают значение 1. На рёбрах bc и cd перепада нет.', True)]
    for row, (title, values, energies, total, caption, free) in enumerate(rows):
        top = 109 + 231*row
        parts.append(f'<rect x="24" y="{top}" width="992" height="216" rx="14" fill="#f5f8fb" stroke="#dce5ed"/>')
        text(46, top+35, title, 23, weight='bold')
        y, xs = top+105, [130, 310, 490, 670]
        for i, energy in enumerate(energies):
            color = '#247aab' if energy else '#aebbc6'
            width = 5 if energy else 3
            parts.append(f'<line x1="{xs[i]+27}" y1="{y}" x2="{xs[i+1]-27}" y2="{y}" stroke="{color}" stroke-width="{width}"/>')
            text((xs[i]+xs[i+1])/2, y+36, str(energy), 23, color, 'middle', 'bold')
        for i, (x, value) in enumerate(zip(xs, values)):
            dash = ' stroke-dasharray="6 4"' if free and i >= 2 else ''
            parts.append(f'<circle cx="{x}" cy="{y}" r="26" fill="#ffffff" stroke="#244760" stroke-width="2.5"{dash}/>')
            text(x, y-39, 'abcd'[i], 22, anchor='middle', weight='bold')
            text(x, y+8, str(value).replace('-', '−'), 22, anchor='middle')
        parts.append(f'<rect x="748" y="{y-25}" width="244" height="67" rx="10" fill="#e3eff8"/>')
        text(870, y+15, total, 21, '#185d84', 'middle', 'bold')
        text(46, top+190, caption, 18, '#52667b')
    text(36, 829, 'Кружок: значение на вершине. Пунктирный кружок: значение найдено минимизацией энергии.', 16, '#52667b')
    parts.extend(['</g>', '</svg>'])
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text('\n'.join(parts)+'\n', encoding='utf-8')
    print(target)


if __name__ == '__main__':
    main()
