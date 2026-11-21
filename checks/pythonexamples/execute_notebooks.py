"""Execute every public PythonExamples notebook in a fresh kernel."""
from pathlib import Path
import os
import re
import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter

ROOT = Path(__file__).resolve().parents[2]
output = ROOT / 'checks/pythonexamples/previews'
output.mkdir(parents=True, exist_ok=True)
for path in (ROOT / 'pmg-library').glob('*/PythonExamples/notebooks/*.ipynb'):
    language = path.relative_to(ROOT).parts[1]
    notebook = nbformat.read(path, as_version=4)
    NotebookClient(notebook, timeout=120, kernel_name='python3',
                   resources={'metadata': {'path': str(ROOT)}}).execute(env=os.environ.copy())
    nbformat.validate(notebook)
    outputs = [item for cell in notebook.cells for item in cell.get('outputs', [])]
    assert all(item.output_type != 'error' for item in outputs)
    if path.stem == 'digraph-polyforms':
        note = (ROOT / notebook.metadata.pmg.source_note).read_text(encoding='utf-8')
        fragments = re.findall(r'```python\n(.*?)```', note, re.S)
        assert [c.source for c in notebook.cells[4:] if c.cell_type == 'code'] == [s.strip() for s in fragments]
        assert sum(bool(c.get('attachments')) for c in notebook.cells) == 2
    elif path.stem == 'symbolic-polyforms':
        assert sum('text/latex' in item.get('data', {}) for item in outputs) == 16
    elif path.stem == 'weighted-chain':
        assert sum('image/png' in item.get('data', {}) for item in outputs) == 1
    nbformat.write(notebook, path)
    html, _ = HTMLExporter().from_notebook_node(notebook)
    (output / f'{path.stem}-{language}.html').write_text(html, encoding='utf-8')
    print(language, path.stem, 'executed successfully')
