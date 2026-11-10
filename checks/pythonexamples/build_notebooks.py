from pathlib import Path
import re,nbformat,urllib.parse
ROOT=Path(__file__).resolve().parents[2]
READY=ROOT
INSTALL='https://github.com/magin67/polyform_algebra/archive/refs/tags/v0.9.0.zip'
PLOT='''import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 2.8))
ax.plot([0, 1, 2], [0, 0, 0], color="#176b9b", linewidth=3)
for x, label, voltage in [(0, "a", 3), (1, "b", 1), (2, "c", 0)]:
    ax.plot(x, 0, "o", markersize=22, color="white", markeredgecolor="#44536a", markeredgewidth=2)
    ax.text(x, 0, label, ha="center", va="center")
    ax.text(x, -.3, f"φ = {voltage} V", ha="center")
for x, conductance in [(0, 1), (1, 2)]:
    ax.text(x + .5, .12, f"c = {conductance} S", ha="center")
    ax.annotate("", (x + .8, .5), (x + .2, .5),
                arrowprops={"arrowstyle": "-|>", "mutation_scale": 22, "color": "#b65422", "lw": 2})
    ax.text(x + .5, .65, "I = 2 A", ha="center")
ax.set(xlim=(-.3, 2.3), ylim=(-.55, .9))
ax.axis("off")
plt.tight_layout()
plt.show()
'''
def page_link(lang,target):
 # Resolve a wiki target against the complete library, including its language.
 target,_,label=target.partition('|');stem,_,anchor=target.partition('#')
 candidates=list((ROOT/'pmg-library'/lang).rglob('*.md'))
 found=[p for p in candidates if p.stem==stem or p.as_posix().endswith(stem+'.md')]
 if not found:return label or stem
 path=found[0].relative_to(ROOT/'pmg-library').as_posix()
 parts=re.sub(r'\s','-',path.removesuffix('.md')).lower().split('/')
 slug='/'.join(parts[:-1])+'/' if parts[-1]==parts[-2] else '/'.join(parts)
 url='https://magin67.github.io/pmg-notes/'+urllib.parse.quote(slug,safe='/,')
 if anchor:url+='#'+urllib.parse.quote(re.sub(r'[^\w\s-]','',anchor.lower()).replace(' ','-'))
 return '['+(label or stem)+']('+url+')'
PINNED_COMMITS = {
    'metric-parameters': '14f137c0b4bf965392f47f877165f2f3b8168073',
    'structural-identities': '73ac82d5c16afbfd47285436e1b6f37d5a68f8af',
    'polynomial-toponomes': '3ae0e82e30c547e7980f1890bf1f62f5308b4a75',
    'partition-toponomes': '4d2ef44d35a57c73fb5e6ecf6feccf88c237bbbc',
    'combinatorial-potentials': '990f4462b17a1afaad25666220ffc1fbc2cd4d26',
    'symmetric-polyforms': '73ac82d5c16afbfd47285436e1b6f37d5a68f8af',
}

COMPANIONS = (
    ('ru', 'Пример - Взвешенная цепочка', 'weighted-chain'),
    ('en', 'Example - Weighted Chain', 'weighted-chain'),
    ('ru', 'Пример - Подпространства и преобразования графов', 'spaces'),
    ('en', 'Example - Subspaces and Graph Transformations', 'spaces'),
    ('ru', 'Пример - Метрические параметры графов', 'metric-parameters'),
    ('en', 'Example - Metric Parameters of Graphs', 'metric-parameters'),
    ('ru', 'Пример - Проверка структурных тождеств', 'structural-identities'),
    ('en', 'Example - Checking Structural Identities', 'structural-identities'),
    ('ru', 'Пример - Проверка тождеств симметрических полиформ', 'symmetric-polyforms'),
    ('en', 'Example - Checking Symmetric Polyform Identities', 'symmetric-polyforms'),
    ('ru', 'Пример - Комбинаторные потенциалы', 'combinatorial-potentials'),
    ('en', 'Example - Combinatorial Potentials', 'combinatorial-potentials'),
    ('ru', 'Пример - Топономы разбиений', 'partition-toponomes'),
    ('en', 'Example - Partition Toponomes', 'partition-toponomes'),
    ('ru', 'Пример - Полиномиальные топономы', 'polynomial-toponomes'),
    ('en', 'Example - Polynomial Toponomes', 'polynomial-toponomes'),
)

def revision_setup(commit):
    return f'''from importlib.metadata import PackageNotFoundError, distribution
import json
import subprocess
import sys

source = "https://github.com/magin67/polyform_algebra/archive/{commit}.zip"
try:
    installed = distribution("polyform_algebra")
    installed_url = json.loads(installed.read_text("direct_url.json") or "{{}}").get("url")
except PackageNotFoundError:
    installed = None
    installed_url = None

# A tag and a development revision can report the same version string.
if installed_url != source:
    if "polyform_algebra" in sys.modules:
        raise RuntimeError("Restart the kernel before installing the pinned package revision.")
    command = [sys.executable, "-m", "pip", "install", "-q"]
    if installed is not None and installed.version == "0.9.0":
        command += ["--force-reinstall", "--no-deps"]
    subprocess.check_call(command + [source])
'''


for lang, title, slug in COMPANIONS:
 has_plot = slug == 'weighted-chain'
 revision = PINNED_COMMITS.get(slug)
 note=(READY/'pmg-library'/lang/'PythonExamples'/(title+'.md')).read_text(encoding='utf-8').split('---',2)[2].strip()
 note=re.sub(r'^\[\[(?:ru|en)/PythonExamples/.*?\n','',note,flags=re.M)
 note=re.sub(r'^\[(?:Открыть в Colab|Open in Colab).*?\n','',note,flags=re.M)
 note=re.sub(r'\[\[([^]]+)\]\]',lambda m:page_link(lang,m[1]),note)
 # The source note and notebook share all calculation cells and explanatory text.
 note=re.sub(r'!\[images/[^\n]+\n','\n<!-- figure -->\n',note)
 # Wiki replacement strips the image target; replace its remaining text reliably.
 note=re.sub(r'^!images/[^\n]+\n','\n<!-- figure -->\n',note,flags=re.M)
 cells=[nbformat.v4.new_markdown_cell('# '+title),nbformat.v4.new_markdown_cell('## Подготовка\n\nВыполните все ячейки сверху вниз. Проверенная версия пакета: **0.9.0**.' if lang=='ru' else '## Setup\n\nRun all cells from top to bottom. Tested package version: **0.9.0**.'),nbformat.v4.new_code_cell(f'%pip install -q "{INSTALL}" matplotlib'),nbformat.v4.new_code_cell('import polyform_algebra\nassert polyform_algebra.get_version() == "0.9.0"\nprint("polyform_algebra", polyform_algebra.get_version())')]
 for part in re.split(r'(```python\n.*?```|<!-- figure -->)',note,flags=re.S):
  if part.startswith('```python'):cells.append(nbformat.v4.new_code_cell(part[len('```python\n'):-3].strip()))
  elif part=='<!-- figure -->':cells.append(nbformat.v4.new_code_cell(PLOT))
  elif part.strip():cells.append(nbformat.v4.new_markdown_cell(part.strip()))
 assert any('plt.show()' in c.source for c in cells) == has_plot, note
 setup = '''from importlib.metadata import version, PackageNotFoundError
import subprocess
import sys

# Install only when the required package version is missing.
try:
    installed = version("polyform_algebra")
except PackageNotFoundError:
    installed = None
if installed != "0.9.0":
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q",
                          "'''+INSTALL+'''"])
'''
 if has_plot:
  setup += '''import importlib.util

if importlib.util.find_spec("matplotlib") is None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "matplotlib"])
'''
 if revision is not None:
  setup = revision_setup(revision)
  preparation = ('Выполните все ячейки сверху вниз. Ревизия пакета: ' if lang == 'ru'
                 else 'Run all cells from top to bottom. Package revision: ')
  heading = '## Подготовка' if lang == 'ru' else '## Setup'
  cells[1].source = f'{heading}\n\n{preparation}**{revision[:7]}**.'
 cells[2] = nbformat.v4.new_code_cell(setup)
 nb=nbformat.v4.new_notebook(cells=cells,metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python','version':'3.12'},'colab':{'name':title+'.ipynb','provenance':[]},'pmg':{'package_version':'0.9.0','source_note':f'pmg-library/{lang}/PythonExamples/{title}.md'}})
 if revision is not None:
  nb.metadata.pmg.package_commit = revision
 out=READY/'pmg-library'/lang/'PythonExamples/notebooks'/f'{slug}.ipynb';out.parent.mkdir(exist_ok=True);nbformat.validate(nb);nbformat.write(nb,out)
 print(lang,len(cells),'cells')
