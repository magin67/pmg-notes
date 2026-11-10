from pathlib import Path
import re,sys,json,math,contextlib,io
ROOT=Path(__file__).resolve().parents[2]

import polyform_algebra
assert polyform_algebra.get_version()=='0.9.0'
results=[]
for p in sorted((ROOT/'pmg-library').glob('*/PythonExamples/*.md')):
 blocks=re.findall(r'```python\n(.*?)```',p.read_text(encoding='utf-8'),re.S)
 ns={};stream=io.StringIO();count=0
 with contextlib.redirect_stdout(stream):
  for code in blocks:
   if code.lstrip().startswith('%'):continue
   exec(compile(code,str(p),'exec'),ns);count+=1
 title=p.stem
 if 'triangle' in title.lower() or 'треугольника' in title:
  if 'area_squared' in ns:assert math.isclose(float(ns['area_squared']),1/12)
  if 'tau_one' in ns:assert ns['tau_one']==5 and ns['tau_two']==8
 if 'updated' in ns:
  assert ns['updated'].potential(ns['quForm'].one())==0
  assert ns['updated'].potential(ns['f_ac'])==1
 if 'part' in ns:
  assert ns['metric'].potential(ns['quForm'].one())==4
  assert math.isclose(float(ns['metric'].norm(ns['form'])),3/4)
 results.append({'note':title,'blocks':count,'output':stream.getvalue()})
 print(title,count,'OK')
(ROOT/'checks/pythonexamples/execution.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
