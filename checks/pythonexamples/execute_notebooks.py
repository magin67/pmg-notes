from pathlib import Path
import os,nbformat,json
from nbclient import NotebookClient
from nbconvert import HTMLExporter
ROOT=Path(__file__).resolve().parents[2]
env=os.environ.copy();env['IPYTHONDIR']=str(ROOT/'ipython');env['MPLCONFIGDIR']=str(ROOT/'matplotlib');env['PYTHONUTF8']='1'
out=ROOT/'checks/pythonexamples/previews';out.mkdir(exist_ok=True)
for lang in ('ru','en'):
 p=ROOT/'pmg-library'/lang/'PythonExamples/notebooks/weighted-chain.ipynb'
 nb=nbformat.read(p,as_version=4)
 NotebookClient(nb,timeout=120,kernel_name='python3',resources={'metadata':{'path':str(ROOT)}}).execute(env=env)
 nbformat.validate(nb);nbformat.write(nb,p)
 html,_=HTMLExporter().from_notebook_node(nb);(out/f'notebook-{lang}.html').write_text(html,encoding='utf-8')
 count=0
 for c in nb.cells:
  for o in c.get('outputs',[]):
   assert o.output_type!='error'
   if 'image/png' in o.get('data',{}):
    import base64
    (out/f'notebook-plot-{lang}.png').write_bytes(base64.b64decode(o.data['image/png']));count+=1
 assert count==1
 print(lang,'executed',len(nb.cells),'cells,',count,'figure',flush=True)
