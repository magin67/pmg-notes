---
title: "Example: Checking Symmetric Polyform Identities"
date: 2026-11-10
updated: 2026-11-10
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-symmetric-polyforms
lang: en
description: "Exact comparisons of partition forms, products, exponentials, and Abel polynomials."
order: 10
---

Start with the identity on five vertices. Then check type normalization, products of forms, graph exponentials, and the transition to Abel polynomials. The calculations cover the stated sizes and grades. See the series notes for the general proofs.

[[ru/PythonExamples/Пример - Проверка тождеств симметрических полиформ|Русский]] · [[en/PythonExamples/PythonExamples|Programming Examples]]

Run the fragments from top to bottom. The notebook installs the pinned package revision. [polyform-algebra 73ac82d](https://github.com/magin67/polyform_algebra/commit/73ac82d5c16afbfd47285436e1b6f37d5a68f8af).

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/symmetric-polyforms.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/symmetric-polyforms.ipynb)

## The identity on five vertices

On vertices $a,b,c,d,e$, build the left-hand side from the ten partitions into a triple and its complementary pair. On the right, sum the five quadruple forms and multiply by $3$. In each partition on the right the remaining vertex is a singleton.

$$
E_5[2,1]=3E_5[3,0]
$$

The function `q` builds a partition form from its blocks. With no blocks it returns the unit $e$. The function `check` compares the coefficients of the two forms in one context. On a mismatch, it shows the pair of basis blades and the coefficient of the difference. As a control, also compare the left-hand side with $E_5[3,0]$ without the factor $3$.

[[en/Polyform Algebra and Combinatorics/Symmetric polyforms/Fundamental Theorem of Symmetric Polyforms#An example before the general formula|Related section of the note]].

```python
from itertools import combinations

from polyform_algebra.core import (
    Context, equivalent, form_coefficients, partition_form,
)


def q(context, *blocks):
    return partition_form(context, blocks).value


def principal(context, grade):
    return sum((q(context, block)
                for block in combinations(context.labels, grade + 1)),
               start=0 * q(context))


def check(identity, left, right):
    matches = equivalent(left, right).value
    if not matches:
        pair, difference = form_coefficients(left - right).value[0]
        blades = tuple(" ∧ ".join(left.context.labels[i] for i in blade)
                       for blade in pair)
        raise AssertionError((identity, blades, difference))
    print(identity, "→", matches)


five = Context(tuple("abcde"))
triple_pair_terms = [
    q(five, triple, tuple(vertex for vertex in five.labels if vertex not in triple))
    for triple in combinations(five.labels, 3)
]
assert len(triple_pair_terms) == 10
assert len(list(combinations(five.labels, 4))) == 5
E5_21 = sum(triple_pair_terms, start=0 * q(five))
E5_30 = principal(five, 3)
check("E₅[2,1] = 3 E₅[3,0]", E5_21, 3 * E5_30)
assert not equivalent(E5_21, E5_30).value
```

## Types and normalizations

Enumerate partitions by adding the first vertex either as a singleton or to a block of a partition of the remaining vertices. This gives each partition once. A block's grade is its size minus one. Sum the forms by type and check the number of summands against the representation-size formula.

On four vertices the three pair partitions give the same form as the four partitions with a triple. For each of the $23$ positive-grade types with $2\leqslant n\leqslant6$, compare the sum of partition forms with a multiple of its principal polyform. The fundamental theorem gives the multiplier from factorials and multiplicities of equal positive grades. Display three identities on six vertices, including a type with a singleton.

[[en/Polyform Algebra and Combinatorics/Symmetric polyforms/Symmetric Polyforms - Types and Normalizations#Type, coefficients, and metric evaluation|Related section of the note]].

```python
from collections import Counter
from fractions import Fraction
from math import factorial, prod


def set_partitions(labels):
    if not labels:
        yield ()
        return
    first, *rest = labels
    for blocks in set_partitions(rest):
        yield ((first,),) + blocks
        for index, block in enumerate(blocks):
            yield blocks[:index] + ((first,) + block,) + blocks[index + 1:]


def block_type(blocks):
    return tuple(sorted((len(block) - 1 for block in blocks), reverse=True))


def group_forms(context):
    sums = {}
    counts = Counter()
    zero = 0 * q(context)
    for blocks in set_partitions(context.labels):
        grades = block_type(blocks)
        sums[grades] = sums.get(grades, zero) + q(context, *blocks)
        counts[grades] += 1
    return sums, counts


def type_count(n, grades):
    divisor = prod(factorial(grade + 1) for grade in grades)
    repeats = prod(factorial(count) for count in Counter(grades).values())
    return Fraction(factorial(n), divisor * repeats)


def principal_factor(grades):
    positive = tuple(grade for grade in grades if grade)
    repeats = prod(factorial(count) for count in Counter(positive).values())
    divisor = factorial(grades.count(0)) * prod(map(factorial, positive)) * repeats
    return Fraction(factorial(len(grades) - 1) * factorial(sum(grades)), divisor)


four = Context(tuple("abcd"))
six = Context(tuple("abcdef"))
four_types, four_counts = group_forms(four)
E4_2 = principal(four, 2)
E4_11 = four_types[(1, 1)]
assert four_counts[(1, 1)] == 3 and four_counts[(2, 0)] == 4
check("E₄[1,1] = E₄[2,0]", E4_11, E4_2)

checked = 0
for n in range(2, 7):
    context = Context(tuple("abcdef"[:n]))
    type_sums, type_counts = group_forms(context)
    for grades, form in type_sums.items():
        grade = sum(grades)
        assert type_counts[grades] == type_count(n, grades), grades
        if grade:
            right = principal_factor(grades) * principal(context, grade)
            assert equivalent(form, right).value, (n, grades)
            checked += 1

six_types, six_counts = group_forms(six)
for grades, coefficient in (((1, 1, 1), 2), ((2, 1, 0), 6), ((2, 2), 3)):
    assert principal_factor(grades) == coefficient
    check(f"E₆{list(grades)} = {coefficient} E₆[{sum(grades)}]",
          six_types[grades], coefficient * principal(six, sum(grades)))
assert checked == 23
print("Positive-grade types (2 ≤ n ≤ 6):", checked)
```

## Products and powers

Build the left-hand sides by multiplying forms in the package. For the square of $E_4[1]$ and the products on five and six vertices, use the expansion by block type on the right, then express the sum through the principal polyform. Also check the cube of $E_4[1]$ and the vanishing of powers whose grade exceeds $n-1$.

[[en/Polyform Algebra and Combinatorics/Symmetric polyforms/Products and Powers of Symmetric Polyforms#Examples on four, five, and six vertices|Related section of the note]].

```python
from polyform_algebra.core import form_product


def multiply(left, right):
    return form_product(left, right).value


E4_1 = principal(four, 1)
E4_3 = principal(four, 3)
square4 = multiply(E4_1, E4_1)
cube4 = multiply(square4, E4_1)
check("E₄[1]² = 6 E₄[2] + 2 E₄[1,1]", square4, 6 * E4_2 + 2 * E4_11)
check("E₄[1]² = 8 E₄[2]", square4, 8 * E4_2)
check("E₄[1]³ = 96 E₄[3]", cube4, 96 * E4_3)
check("E₄[1]⁴ = 0", multiply(cube4, E4_1), 0 * E4_1)

product5 = multiply(principal(five, 1), principal(five, 2))
check("E₅[1] E₅[2] = 12 E₅[3] + E₅[2,1]", product5, 12 * E5_30 + E5_21)
check("E₅[1] E₅[2] = 15 E₅[3]", product5, 15 * E5_30)

E6_2 = principal(six, 2)
E6_4 = principal(six, 4)
square6 = multiply(E6_2, E6_2)
check("E₆[2]² = 30 E₆[4] + 2 E₆[2,2]", square6, 30 * E6_4 + 2 * six_types[(2, 2)])
check("E₆[2]² = 36 E₆[4]", square6, 36 * E6_4)
check("E₆[2]³ = 0", multiply(square6, E6_2), 0 * E6_2)
```

## Two expansions of the complete-graph exponential

Take the complete graph $K_5$ with unit conductances. On the left, compute the polyform exponential of its Laplacian. On the right, build two sums. The first groups the forms by forest type and weights them by the number of ways to choose trees on fixed blocks. The second uses the principal form of grade $k$ with coefficient $5^{k-1}$ and adds the unit $e$ separately.

Compare both full sums with the exponential, then check the formulas for grades two and three separately. The top grade gives the spanning-tree coefficient $\tau(K_5)=125$.

[[en/Polyform Algebra and Combinatorics/Symmetric polyforms/Symmetric Polyforms of the Complete Graph#The complete graph on five vertices|Related section of the note]].

```python
from polyform_algebra.core import (
    Network, form_exp, grade_part, laplacian_form, spanning_coefficient,
)


def complete_graph(context):
    return Network(context, tuple((a, b, 1) for a, b in combinations(context.labels, 2)))


def tree_factor(grades):
    return prod((grade + 1) ** (grade - 1) for grade in grades if grade)


def principal_exp(context):
    n = len(context.labels)
    return sum((n ** (k - 1) * principal(context, k) for k in range(1, n)),
               start=q(context))


K5 = complete_graph(five)
M_K5 = form_exp(laplacian_form(K5).value).value
five_types, _ = group_forms(five)
assert (tree_factor((2, 0, 0)), tree_factor((2, 1))) == (3, 3)
forest_exp = sum((tree_factor(grades) * form for grades, form in five_types.items()),
                 start=0 * q(five))
check("M(K₅) = forest expansion", M_K5, forest_exp)
check("M(K₅) = principal expansion", M_K5, principal_exp(five))
check("M₂(K₅) = 3 E₅[2] + E₅[1,1]", grade_part(M_K5, 2).value,
      3 * principal(five, 2) + five_types[(1, 1, 0)])
check("M₃(K₅) = 16 E₅[3] + 3 E₅[2,1]", grade_part(M_K5, 3).value,
      16 * E5_30 + 3 * E5_21)
tau_K5 = spanning_coefficient(M_K5).value
assert tau_K5 == 125
print("τ(K₅) =", tau_K5)
```

## Deleting the diagonals

Build $M_{C_4}$ from the four edge factors $e+[(uv)]^2$ of the cycle $a-b-c-d-a$ with unit conductances. Denote the forms of diagonals $ac$ and $bd$ by $p$ and $q$. On the right, start with the principal expansion of $M_{K_4}$ and delete the diagonals by multiplying by $(e-p)(e-q)$. Check both the resulting polyform and its simplified expression in the note. Extract $\tau(C_4)=4$ from the top grade.

[[en/Polyform Algebra and Combinatorics/Symmetric polyforms/Symmetric Polyforms of the Complete Graph#Example: deleting the diagonals of a four-cycle|Related section of the note]].

```python
cycle_edges = (("a", "b"), ("b", "c"), ("c", "d"), ("d", "a"))
cycle_product = q(four)
for edge in cycle_edges:
    cycle_product = multiply(cycle_product, q(four) + q(four, edge))

p = q(four, ("a", "c"))
diagonal_q = q(four, ("b", "d"))
diagonals = multiply(p, diagonal_q)
deleted = multiply(principal_exp(four), q(four) - p - diagonal_q + diagonals)
cycle_formula = q(four) + (E4_1 - p - diagonal_q) + 2 * E4_2 - diagonals + 4 * E4_3
check("M(C₄) = M(K₄) (e − p) (e − q)", cycle_product, deleted)
check("M(C₄) = simplified expansion", cycle_product, cycle_formula)
tau_C4 = spanning_coefficient(cycle_product).value
assert tau_C4 == 4
print("τ(C₄) =", tau_C4)
```

## Forest coefficients and Abel polynomials

Enumerate partitions of an auxiliary set of $k$ letter-named vertices into $m$ blocks. Add one root to each block. Cayley's factor counts the trees on the augmented block. Summing over partitions gives $\operatorname{St}(k,m)$.

Build $A_k(x)=x(x+k)^{k-1}$ on the left and $\sum_m\operatorname{St}(k,m)x_{\underline m}$ on the right. Compare the integer coefficients of every power of $x$ for $1\leqslant k\leqslant6$. For $A_3(2)$, also compute the determinant of the Laplacian minor of $K_5$ obtained by removing the rows and columns of the prescribed roots $d,e$. Both expressions give $50$.

[[en/Polyform Algebra and Combinatorics/Symmetric polyforms/Forest Coefficients and Abel Polynomials#The expansion of Abel polynomials|Related section of the note]].

```python
from sympy import Matrix, Poly, Symbol
from polyform_algebra.core import laplacian

x = Symbol("x")
for k in range(1, 7):
    St = Counter()
    for blocks in set_partitions(tuple("abcdef"[:k])):
        # Adding a root to each block makes its size a boundary grade.
        grades = tuple(len(block) for block in blocks)
        St[len(blocks)] += tree_factor(grades)
    abel = Poly(x * (x + k) ** (k - 1), x)
    falling = Poly(sum(St[m] * prod(x - j for j in range(m))
                       for m in range(1, k + 1)), x)
    assert abel == falling, (k, abel - falling)
    print(f"A{k}(x) =", falling.as_expr())
    if k == 3:
        assert tuple(St[m] for m in range(1, 4)) == (16, 9, 1)
        assert abel.eval(2) == 50
    if k == 4:
        assert tuple(St[m] for m in range(1, 5)) == (125, 91, 18, 1)

# The principal minor keeps ordinary vertices a, b, c and deletes roots d, e.
ordinary = [K5.context.labels.index(vertex) for vertex in "abc"]
minor = Matrix(laplacian(K5).value.values).extract(ordinary, ordinary)
assert minor.det() == 2 * (3 + 2) ** (3 - 1) == 50
print("A3(2) = det(L[abc, abc]) =", minor.det())
```
