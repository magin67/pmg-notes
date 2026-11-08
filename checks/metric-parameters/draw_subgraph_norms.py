"""Draw the three types of vertex triples in the two-triangle example."""
from pathlib import Path
from html import escape
import sys

FONT = "Arial, sans-serif"
positions = {"h": (145, 117), "a": (55, 54), "b": (55, 180),
             "c": (235, 54), "d": (235, 180)}
edges = [("h", "a"), ("h", "b"), ("a", "b"),
         ("h", "c"), ("h", "d"), ("c", "d")]
panels = [({"h", "a", "b"}, "{h, a, b}", "2"),
          ({"h", "a", "c"}, "{h, a, c}", "4/3"),
          ({"a", "b", "c"}, "{a, b, c}", "2/3")]


def make_svg():
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="960" height="330" viewBox="0 0 960 330" role="img" aria-labelledby="title desc">',
             '<title id="title">Нормы троек в двух треугольниках с общей вершиной</title>',
             '<desc id="desc">Выделенные тройки hab, hac, abc имеют нормы 2, 4/3 и 2/3. Веса всех шести рёбер равны единице.</desc>',
             '<rect width="960" height="330" rx="12" fill="#ffffff"/>',
             f'<g font-family="{FONT}" fill="#183247">']
    for number, (selected, label, value) in enumerate(panels):
        xoff = 20 + number * 320
        parts.append(f'<g transform="translate({xoff}, 40)">')
        parts.append(f'<text x="145" y="-15" text-anchor="middle" font-size="18" font-weight="bold">S = {escape(label)}</text>')
        for a, b in edges:
            x1, y1 = positions[a]
            x2, y2 = positions[b]
            chosen = a in selected and b in selected
            color = "#1c6da8" if chosen else "#b5bdc6"
            width = 4 if chosen else 2
            parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"/>')
        for vertex, (x, y) in positions.items():
            chosen = vertex in selected
            fill = "#dceefb" if chosen else "#ffffff"
            color = "#1c6da8" if chosen else "#7b8794"
            width = 3 if chosen else 2
            parts.append(f'<circle cx="{x}" cy="{y}" r="17" fill="{fill}" stroke="{color}" stroke-width="{width}"/>')
            parts.append(f'<text x="{x}" y="{y + 6}" text-anchor="middle" font-size="18">{vertex}</text>')
        parts.append(f'<text x="145" y="232" text-anchor="middle" font-size="20" font-weight="bold">Норма = {value}</text>')
        parts.append('</g>')
    parts.extend(['<text x="480" y="310" text-anchor="middle" font-size="15">Все проводимости равны 1; метрика во всех трёх случаях одна и та же.</text>',
                  '</g></svg>'])
    return "\n".join(parts) + "\n"


if __name__ == "__main__":
    repo = Path(__file__).resolve().parents[2]
    default = repo / "pmg-library/ru/Резистивная геометрия и дуальность/Метрические параметры/images/Нормы лапласианов - тройки двух треугольников.svg"
    destination = Path(sys.argv[1]) if len(sys.argv) > 1 else default
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(make_svg(), encoding="utf-8")
    print(destination)

