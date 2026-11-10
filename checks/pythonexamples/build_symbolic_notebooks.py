from pathlib import Path
import re,json,nbformat,shutil
R=Path(__file__).resolve().parents[2];READY=R
INSTALL='https://github.com/magin67/polyform_algebra/archive/refs/tags/v0.9.0.zip'
SETUP=f'''from importlib.metadata import version, PackageNotFoundError
import subprocess
import sys

try:
    installed = version("polyform_algebra")
except PackageNotFoundError:
    installed = None
if installed != "0.9.0":
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "{INSTALL}"])
import polyform_algebra
assert polyform_algebra.get_version() == "0.9.0"
print("polyform_algebra", polyform_algebra.get_version())'''
VERTICES='''from fractions import Fraction
from math import factorial
from polyform_algebra import Point, Polyform, quForm

a, b, c, d, e = Point.create_list("abcde")
f_ab = quForm([(a, b)])
f_bc = quForm([(b, c)])
f_cd = quForm([(c, d)])
f_de = quForm([(d, e)])
f_ad = quForm([(a, d)])
unit = Polyform.one()
print("vertices:", a, b, c, d, e)
print("f_ab =", f_ab)'''
FORMAT=r'''from IPython.display import display, Math

def form_tex(form):
    # This display adapter only formats the computed boundary forms.
    if form.is_zero():
        return "0"
    if form.is_one():
        return r"\mathrm{e}"
    components = []
    for component in form.components:
        if not isinstance(component, tuple):
            raise TypeError("This tutorial formats boundary forms only")
        labels = [str(vertex) for vertex in component]
        if not all(label in "abcde" and len(label) == 1 for label in labels):
            raise ValueError("Expected the named tutorial vertices")
        components.append("(" + "".join(labels) + ")")
    return "[" + "".join(components) + "]^2"

def show(name, value):
    terms = value.terms if isinstance(value, Polyform) else {value: 1}
    pieces = []
    for form, coefficient in sorted(terms.items(), key=lambda item: str(item[0])):
        if coefficient == 0 or form.is_zero():
            continue
        magnitude = Fraction(abs(coefficient))
        scalar = (str(magnitude.numerator) if magnitude.denominator == 1 else
                  rf"\frac{{{magnitude.numerator}}}{{{magnitude.denominator}}}")
        body = form_tex(form)
        if magnitude != 1:
            body = scalar + r"\," + body
        sign = "-" if coefficient < 0 else ("+" if pieces else "")
        pieces.append(sign + body)
    if not pieces:
        pieces = ["0"]
    rows = [" ".join(pieces[i:i+3]) for i in range(0, len(pieces), 3)]
    display(Math(r"\begin{aligned}& " + name + " = " +
                 r"\\ &\quad ".join(rows) + r"\end{aligned}"))'''
PRODUCTS='''merged = f_ab * f_bc
separate = f_ab * f_cd
print("f_ab * f_bc =", merged)
print("f_ab * f_cd =", separate)
print("f_ab * f_ab =", f_ab * f_ab)
print("f_ab * f_bc * f_ad * f_cd =", f_ab * f_bc * f_ad * f_cd)
assert merged.as_polyform().is_equivalent(quForm([(a, b, c)]).as_polyform())
assert separate.as_polyform().is_equivalent(quForm([(a, b), (c, d)]).as_polyform())
assert (f_ab * f_ab).is_zero()
assert (f_ab * f_bc * f_cd * f_ad).is_zero()'''
PATH='''L_path = f_ab + f_bc + f_cd + f_de
M_path = L_path.exp()
print("L_path =", L_path)
print("exp(L_path):")
print(M_path)'''
CYCLE='''L_cycle = f_ab + f_bc + f_cd + f_ad
M_cycle = L_cycle.exp()
print("L_cycle =", L_cycle)
print("exp(L_cycle):")
print(M_cycle)'''
EXPAND='''partial = unit
for edge in (f_ab, f_bc, f_cd, f_de):
    partial = partial * (unit + edge)
    print("Factor:", unit + edge)
    print(partial)
    print()
assert partial.is_equivalent(M_path)'''
TREES='''cycle_edges = (f_ab, f_bc, f_cd, f_ad)
tree_sum = Polyform.zero()
for omitted in range(len(cycle_edges)):
    tree = unit
    for position, edge in enumerate(cycle_edges):
        if position != omitted:
            tree = tree * edge
    print("Without", cycle_edges[omitted], "->", tree)
    tree_sum = tree_sum + tree
show(r"(M_{C_4})_3", tree_sum)
assert tree_sum.is_equivalent(4 * quForm([(a, b, c, d)]))
assert M_cycle.extract_grade(3).is_equivalent(tree_sum)
assert M_cycle.extract_grade(4).is_zero()'''
CHECKS='''for L, M, edges, weights in [
    (L_path, M_path, (f_ab, f_bc, f_cd, f_de), (1, 4, 6, 4, 1)),
    (L_cycle, M_cycle, cycle_edges, (1, 4, 6, 4, 0)),
]:
    product = unit
    for edge in edges:
        product = product * (unit + edge)
    assert product.is_equivalent(M)
    for grade in range(5):
        part = M.extract_grade(grade)
        assert part.is_equivalent(Fraction(1, factorial(grade)) * (L ** grade))
        # Valid for this forest expansion, not arbitrary equivalent rewrites.
        assert sum(part.terms.values()) == weights[grade]
assert M_path.extract_grade(4).is_equivalent(quForm([(a, b, c, d, e)]).as_polyform())
print("All algebraic checks passed.")'''
WEIGHTED=r'''L_weighted = Fraction(3, 2) * f_ab + f_bc + f_cd + f_ad
M_weighted = L_weighted.exp()
print(M_weighted)
show(r"(M_{\mathrm{weighted}})_3", M_weighted.extract_grade(3))
assert M_weighted.extract_grade(3).is_equivalent(Fraction(11, 2) * quForm([(a, b, c, d)]))'''
for lang in ('ru','en'):
 ru=lang=='ru'
 title='Пример: экспоненты пути P5 и цикла C4' if ru else 'Example: path P5 and cycle C4 exponentials'
 filename='Экспоненты пути P5 и цикла C4 на Python' if ru else 'Path P5 and Cycle C4 Exponentials in Python'
 cells=[]
 def md(s):cells.append(nbformat.v4.new_markdown_cell(s))
 def code(s):cells.append(nbformat.v4.new_code_cell(s))
 md('# '+title+'\n\n'+('Здесь результат вычисления — **символьная полиформа**: видны её формы, коэффициенты и грейды. Сначала создаются элементы `a, b, c, d, e`, затем формы, лапласианы и экспоненты. Числа обозначают коэффициенты и номера грейдов, а не вершины.' if ru else 'The result here is a **symbolic polyform**: its forms, coefficients, and grades remain visible. First create the elements `a, b, c, d, e`, then forms, Laplacians, and exponentials. Numbers denote coefficients and grades, not vertices.'))
 md('## '+('Подготовка' if ru else 'Setup')+'\n\n'+('Выполните ячейки сверху вниз. Используется `polyform_algebra 0.9.0`.' if ru else 'Run the cells from top to bottom. This notebook uses `polyform_algebra 0.9.0`.'))
 code(SETUP)
 md('## '+('Элементы и формы' if ru else 'Elements and forms')+'\n\n'+(r'Переменная `e` ниже обозначает вершину; `unit` — единицу алгебры $\mathrm{e}$. Форма `f_ab` — это $[(ab)]^2$, где $(ab)=b-a$. В штатном выводе пакета `f[(a, b)]` означает эту же квадратичную форму, а `f[1]` — единицу алгебры.' if ru else r'The variable `e` below is a vertex; `unit` is the algebra unit $\mathrm{e}$. The form `f_ab` is $[(ab)]^2$, where $(ab)=b-a$. The package prints this quadratic form as `f[(a, b)]` and the algebra unit as `f[1]`.'))
 code(VERTICES)
 md('## '+('Умножение: слияние, раздельные компоненты, обнуление' if ru else 'Multiplication: merging, separate components, and vanishing')+'\n\n'+r'$$[(ab)]^2[(bc)]^2=[(abc)]^2,\qquad [(ab)]^2[(cd)]^2=[(ab)(cd)]^2.$$'+'\n\n'+('Общая вершина сливает две границы. При отсутствии общей вершины остаются две компоненты. Повторное ребро или замкнутый цикл даёт нулевое произведение.' if ru else 'A shared vertex merges the boundaries. Disjoint edges retain two components. A repeated edge or a closed cycle gives a zero product.'))
 code(PRODUCTS)
 md('### '+('Вывод в обозначениях заметок' if ru else 'Displaying the notation used in the notes')+'\n\n'+('Следующая вспомогательная функция только оформляет уже вычисленные формы. Умножение и экспоненту выполняет пакет. Формулы ниже строятся из результата, а не подставляются готовыми строками.' if ru else 'The following helper only formats computed forms. Multiplication and exponentiation are performed by the package. Displayed formulas are generated from the result rather than supplied as prewritten answers.'))
 code(FORMAT)
 code('show(r"[(ab)]^2[(bc)]^2", merged)\nshow(r"[(ab)]^2[(cd)]^2", separate)')
 md('## '+('Путь P5: полный символьный вывод' if ru else 'Path P5: the full symbolic output')+'\n\n'+r'$a-b-c-d-e$. '+('Все проводимости равны единице. `print(M_path)` сам группирует экспоненту по грейдам: `g0` — единица, `g1` — рёберные формы, `g2` — произведения двух рёбер и так далее.' if ru else 'All conductances equal one. `print(M_path)` groups the exponential by grade: `g0` is the unit, `g1` contains edge forms, `g2` contains two-edge products, and so on.'))
 code(PATH)
 code('show(r"L_{P_5}", L_path)\nfor grade in range(5):\n    show(rf"(M_{{P_5}})_{{{grade}}}", M_path.extract_grade(grade))')
 md('### '+('Как появляются грейды' if ru else 'How the grades arise')+'\n\n'+r'$$\exp L=\prod_{xy\in E}(\mathrm{e}+f_{xy}),\qquad M_k=\frac{L^k}{k!}.$$'+'\n\n'+('Каждый следующий множитель добавляет варианты с очередным ребром. Ниже видны все промежуточные полиформы, а не только старший коэффициент.' if ru else 'Each factor adds the alternatives containing the next edge. The following output shows every intermediate polyform, not just its top coefficient.'))
 code(EXPAND)
 md('## '+('Цикл C4: четыре дерева, одна форма' if ru else 'Cycle C4: four trees, one form')+'\n\n'+r'$a-b-c-d-a$. '+('Любые три ребра дают форму $[(abcd)]^2$. Все четыре ребра образуют цикл и дают ноль. Поэтому старший ненулевой грейд равен $4[(abcd)]^2$.' if ru else 'Any three edges give the form $[(abcd)]^2$. All four edges form a cycle and give zero. Thus the highest nonzero grade is $4[(abcd)]^2$.'))
 code(CYCLE)
 code('show(r"L_{C_4}", L_cycle)\nfor grade in range(5):\n    show(rf"(M_{{C_4}})_{{{grade}}}", M_cycle.extract_grade(grade))')
 code(TREES)
 md('## '+('Коэффициенты при формах' if ru else 'Coefficients of forms')+'\n\n'+(r'Изменим только проводимость $ab$ на $3/2$. Три дерева содержат это ребро, одно не содержит; их суммарный вес равен $3\cdot3/2+1=11/2$. Сама форма остаётся $[(abcd)]^2$. Здесь используются точные рациональные коэффициенты; символы вершин не заменяются числовыми метками.' if ru else r'Change only conductance $ab$ to $3/2$. Three trees contain this edge and one does not, so their total weight is $3\cdot3/2+1=11/2$. The form remains $[(abcd)]^2$. These coefficients are exact rationals; vertex symbols are not replaced with numeric labels.'))
 code(WEIGHTED)
 md('## '+('Проверки алгебраических равенств' if ru else 'Checking the algebraic identities')+'\n\n'+('Сравниваются сами полиформы, а не только их нормы или суммы коэффициентов. Сумма коэффициентов дополнительно проверяется именно для полученного лесного разложения; при произвольной эквивалентной перезаписи этот смысл не гарантирован.' if ru else 'The checks compare the polyforms themselves, not merely their norms or coefficient sums. Coefficient sums are additionally checked for this particular forest expansion; arbitrary equivalent rewrites need not retain that interpretation.'))
 code(CHECKS)
 md('## '+('От формы к числу' if ru else 'From a form to a number')+'\n\n'+('Это отдельный, необязательный шаг: `potential` и `norm` оценивают построенные формы. Они не заменяют символьного разложения.' if ru else 'This is a separate, optional step: `potential` and `norm` evaluate the constructed forms. They do not replace the symbolic expansion.'))
 code('print("tau(P5) =", M_path.potential(quForm.one()))\nprint("tau(C4) =", M_cycle.potential(quForm.one()))\nprint("R_ae(P5) =", M_path.norm(quForm([(a, e)])))\nassert M_path.potential(quForm.one()) == 1\nassert M_cycle.potential(quForm.one()) == 4\nassert M_path.norm(quForm([(a, e)])) == 4')
 md('## '+('Попробуйте изменить' if ru else 'Try changing the input')+'\n\n'+('Замените проводимость $ab$ на 2 и просмотрите все грейды: старшая форма цикла получит коэффициент 7. Затем удалите $ad$ из лапласиана цикла: останется путь на четырёх вершинах, и старшая форма будет иметь коэффициент 1.' if ru else 'Set conductance $ab$ to 2 and inspect every grade: the top cycle form receives coefficient 7. Then remove $ad$ from the cycle Laplacian: the remaining four-vertex path has top coefficient 1.'))
 nb=nbformat.v4.new_notebook(cells=cells,metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python'},'colab':{'name':'symbolic-polyforms.ipynb','provenance':[]},'pmg':{'package_version':'0.9.0'}})
 out=READY/'pmg-library'/lang/'PythonExamples/notebooks/symbolic-polyforms.ipynb';out.parent.mkdir(parents=True,exist_ok=True);nbformat.validate(nb);nbformat.write(nb,out)
