"""Localize verified spectral figures before Matplotlib lays out the text."""
import json
from pathlib import Path
import re
from matplotlib.text import Text
from matplotlib.table import Table
from matplotlib.ticker import FuncFormatter

_ROOT = Path(__file__).resolve().parents[2]
_ENGLISH = json.loads(
    Path(__file__).with_name("figure_labels_en.json").read_text(encoding="utf-8")
)

def output_directory(lang):
    """Return the publication folder for the selected language."""
    folder = (
        "en/Spectra and diagonalization in polyform algebra"
        if lang == "en" else "ru/Спектры и диагонализация в алгебре полиформ"
    )
    path = _ROOT / "pmg-library" / folder
    path.mkdir(parents=True, exist_ok=True)
    return path

def _translate(text):
    if re.search("[А-Яа-яЁё]", text):
        return _ENGLISH["labels"][text]
    return text

def prepare_figure(fig, name, description, lang):
    """Translate whole labels, including math text, without changing data."""
    if lang == "en":
        # Tick formatters can recreate their labels during drawing.
        for ax in fig.axes:
            for axis in (ax.xaxis, ax.yaxis):
                for kind in ("major", "minor"):
                    tick_labels = getattr(axis, f"get_{kind}ticklabels")()
                    if any(re.search("[А-Яа-яЁё]", t.get_text()) for t in tick_labels):
                        formatter = getattr(axis, f"get_{kind}_formatter")()
                        getattr(axis, f"set_{kind}_formatter")(FuncFormatter(
                            lambda value, pos, source=formatter: _translate(source(value, pos))
                        ))
        # Table cells do not expose their Text objects through findobj.
        for table in fig.findobj(Table):
            for cell in table.get_celld().values():
                text = cell.get_text()
                text.set_text(_translate(text.get_text()))
        for item in fig.findobj(Text):
            item.set_text(_translate(item.get_text()))
        metadata = _ENGLISH["figures"][name]
        return metadata["name"], metadata["description"]
    return name, description
