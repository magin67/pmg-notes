---
title: "Example: Spectra of Isomers"
date: 2026-11-11
updated: 2026-11-11
revision: 1
translated_revision: 1
status: draft
text_prepared_by: ChatGPT
translation_key: python-isomer-spectra
lang: en
description: "Nine exact calculations for hexagonal chains. Compare the characteristic polynomials of two three-hexagon chains, transfer five coordinates to a new boundary, recover an SLR code, and check recurrences for periodic chains."
order: 19
---

Nine exact calculations for hexagonal chains. Compare the characteristic polynomials of two three-hexagon chains, transfer five coordinates to a new boundary, recover an SLR code, and check recurrences for periodic chains.

[[ru/PythonExamples/Пример - Спектры изомеров|Русский]]

Run the fragments from top to bottom. The notebook installs the pinned package revision. [polyform-algebra 5adcacd](https://github.com/magin67/polyform_algebra/commit/5adcacdf23303333a8b03ffc0835da52df4bdb3c).

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/isomer-spectra.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/isomer-spectra.ipynb)

## Two three-hexagon isomers

The two chains have the same ordinary forest polynomial, spanning-tree count, and resistance radius. Their characteristic difference is the square of the characteristic polynomial of $C_5$, and their first differing rooted coefficient is at grade 4.

[[en/Graph Transformations and Gluing/Spectra of Isomers/Two Isomers of Three Hexagons#Exact characteristic polynomials|Related section of the note]].

```python
from fractions import Fraction
from functools import reduce
from math import gcd, lcm
from string import ascii_lowercase

from sympy import Matrix, Poly, Symbol, diag, expand, eye, factor

from polyform_algebra.boundary_data import spectral_pair_passport, spectral_pair_transfer
from polyform_algebra.core import circumsphere, laplacian, network, spanning_tree_weight
from polyform_algebra.matroid import forest_coefficients
from polyform_algebra.toponomes import laplacian_polynomial


def cycle_edges(vertices):
    return tuple(zip(vertices, vertices[1:] + vertices[:1]))


def unit_graph(vertices, edges):
    return network(tuple(vertices), [(a, b, 1) for a, b in edges])


exits = {"L": 2, "S": 3, "R": 4}


def chain(operations):
    """Attach one hexagon per letter, returning the graph and ordered exit."""
    vertices = tuple("abcdef")
    edges = {tuple(sorted(pair)) for pair in cycle_edges(vertices)}
    active = tuple("ab")
    for letter in operations:
        fresh = tuple(ascii_lowercase[len(vertices):len(vertices)+4])
        assert len(fresh) == 4
        core = (*active[::-1], *fresh)
        vertices += fresh
        edges.update(tuple(sorted(pair)) for pair in cycle_edges(core))
        position = exits[letter]
        active = core[position:position+2]
    return unit_graph(vertices, sorted(edges)), active


def characteristic(graph):
    return Matrix(laplacian(graph).value.values).charpoly(x).as_expr()


x = Symbol("xi")
straight, bent = (chain(letter + "S")[0] for letter in "SL")
chi_straight, chi_bent = map(characteristic, (straight, bent))
pentagon_polynomial = x * (x**2 - 5*x + 5)**2
assert expand(chi_straight - chi_bent - pentagon_polynomial**2) == 0
assert forest_coefficients(straight) == forest_coefficients(bent)
assert laplacian_polynomial(straight)[4] - laplacian_polynomial(bent)[4] == 1
assert all(spanning_tree_weight(graph).value == 204 for graph in (straight, bent))
assert all(circumsphere(graph).value.resistance_radius == Fraction(43595, 41616)
           for graph in (straight, bent))
print("Three-hexagon difference:", factor(chi_straight - chi_bent))
```

## Transfer to a new boundary

Compare all five transferred coordinates with direct minors for the three exits. A separate example tests the polynomial formula at $\xi=2$, where the old interior minor vanishes.

[[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Transfer to a New Boundary#Three outputs of a unit hexagon|Related section of the note]].

```python
kernel = unit_graph("abcdef", cycle_edges(tuple("abcdef")))
entry = tuple("ab")
swap = eye(5)
swap.row_swap(1, 2)
transfers = {
    letter: spectral_pair_transfer(kernel, entry, tuple("abcdef"[i:i+2]), x, shared_conductance=1)
    for letter, i in exits.items()
}
operators = {letter: matrix * swap for letter, matrix in transfers.items()}
seed = Matrix(spectral_pair_passport(kernel, entry, x))


def spectral_state(operations):
    result = seed
    for letter in operations:
        result = (operators[letter] * result).applyfunc(expand)
    return result


for operations in ("L", "S", "R", "LS", "RS"):
    graph, active = chain(operations)
    direct_state = Matrix(spectral_pair_passport(graph, active, x))
    assert spectral_state(operations) == direct_state

# A separate attachment at a zero of the old interior minor.
old = unit_graph("acb", (("a", "c"), ("c", "b")))
runner = unit_graph("adeb", (("a", "d"), ("d", "e"), ("e", "b")))
glued = network(tuple("acbde"), old.edges + runner.edges)
old_state = Matrix(spectral_pair_passport(old, entry, x))
exit_pair = tuple("de")
transfer = spectral_pair_transfer(runner, entry, exit_pair, x)
assert old_state[4].subs(x, 2) == 0
assert (transfer * old_state).applyfunc(expand) == Matrix(spectral_pair_passport(glued, exit_pair, x))
print("Five-coordinate transfer checked, including xi = 2")
```

## Symmetries of an SLR code

Build the orbit of one code under reflection and reversal. Check the symmetry of the transfer matrices and the equality of the spectral polynomials in this orbit.

[[en/Graph Transformations and Gluing/Spectra of Isomers/SLR Codes of Hexagonal Chains#Reflection and reversal of the chain|Related section of the note]].

```python
mirror_table = str.maketrans("LR", "RL")


def orbit(word):
    reflected = word.translate(mirror_table)
    return {word, reflected, word[::-1], reflected[::-1]}


assert transfers["R"] == swap * transfers["L"] * swap
assert transfers["S"] == swap * transfers["S"] * swap
turn_word = "LS"
equivalent_codes = sorted("S" + word for word in orbit(turn_word))
assert equivalent_codes == ["SLS", "SRS", "SSL", "SSR"]
assert len({spectral_state(code[1:] + "S")[0] for code in equivalent_codes}) == 1
print("Equivalent SLR codes:", ", ".join(equivalent_codes))
```

## Two exact spectral differences

Compare the polynomials for $S,L$ and $LL,LR$. Here and below the words in the code give the internal turns. The full chain code has an initial $S$.

[[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Differences of SLR Chains#Two concrete differences first|Related section of the note]].

```python
for first, second, expected in (
    ("S", "L", pentagon_polynomial**2),
    ("LL", "LR", -(x-2)**2 * pentagon_polynomial**2),
):
    difference = spectral_state(first + "S")[0] - spectral_state(second + "S")[0]
    assert expand(difference - expected) == 0
    print("Spectral difference", first, second, "=", factor(difference))
delta = operators["S"] - operators["L"]
assert delta.subs(x, -1).rank() == 2
```

## Decoding a rooted state

Specialize the spectral passport at $\xi=-1$. Compare with direct minors and undo the transfer steps using the signs of two linear forms.

[[en/Graph Transformations and Gluing/Spectra of Isomers/Rooted Forests and Decoding the Boundary State#The inverse algorithm and the decoding theorem|Related section of the note]].

```python
sign = diag(1, -1, -1, -1, 1)
integer_operators = {letter: sign * matrix.subs(x, -1) * sign
                     for letter, matrix in operators.items()}
integer_seed = sign * seed.subs(x, -1)
assert tuple(integer_seed) == (320, 144, 144, 56, 55)


def rooted_state(operations):
    result = integer_seed
    for letter in operations:
        result = integer_operators[letter] * result
    return result


def decode_operations(value):
    inverse = {letter: matrix.inv() for letter, matrix in integer_operators.items()}
    decoded = []
    while value != integer_seed:
        a, b, c, d, e = value
        assert a*e - b*c + d*d == 0
        sectors = {(True, True): "S", (False, True): "L", (True, False): "R"}
        assert 9*b != 4*a and 9*c != 4*a
        letter = sectors[(9*b > 4*a, 9*c > 4*a)]
        predecessor = inverse[letter] * value
        assert 0 < predecessor[0] < a
        decoded.append(letter)
        value = predecessor
    return "".join(reversed(decoded))


for operations in ("S", "LS", "RLS", "SLRS"):
    value = rooted_state(operations)
    graph, active = chain(operations)
    assert value == sign * Matrix(spectral_pair_passport(graph, active, -1))
    assert value[0] == sum(laplacian_polynomial(graph))
    assert decode_operations(value) == operations
print("Rooted-state decoding:", decode_operations(rooted_state("SLRS")))
```

## Recovery from the boundary response

Recover the primitive integer state from the boundary block of $(I+L)^{-1}$ and check the recovered code. The calculation uses exact rational entries.

[[en/Graph Transformations and Gluing/Spectra of Isomers/Reconstructing a Chain from Its Boundary Response#Why normalization retains the chain|Related section of the note]].

```python
operations = "LRSS"
graph, active = chain(operations)
matrix = eye(len(graph.context.labels)) + Matrix(laplacian(graph).value.values)
positions = [graph.context.labels.index(label) for label in active]
boundary_inverse = matrix.inv().extract(positions, positions)
r, s, h = map(Fraction, (boundary_inverse[0, 0], boundary_inverse[1, 1], boundary_inverse[0, 1]))
projective = (Fraction(1), r, s, h, r*s-h*h)
scale = lcm(*(part.denominator for part in projective))
recovered = Matrix([int(scale * part) for part in projective])
assert reduce(gcd, recovered) == 1 and recovered == rooted_state(operations)
assert decode_operations(recovered) == operations
print("Code recovered from exact boundary response:", "S" + operations[:-1])
```

## Constant straight turns

Check the characteristic polynomial of the straight-step matrix and the spanning-tree recurrence for the first five chains.

[[en/Graph Transformations and Gluing/Spectra of Isomers/Weaving SLR Chains and Constant Turns#Five coordinates and a power of one matrix|Related section of the note]].

```python
q = Symbol("q")
straight_operator = operators["S"]
alpha = (x**2-6*x+6) * (x**2-4*x+2)
beta = 2*(x-1)*(x**3-9*x**2+25*x-19)
quartic = q**4 - alpha*q**3 + beta*q**2 - alpha*q + 1
assert expand(straight_operator.charpoly(q).as_expr() - (q-1)*quartic) == 0
tree_counts = [spanning_tree_weight(chain("S"*n)[0]).value for n in range(5)]
assert tree_counts == [6, 35, 204, 1189, 6930]
assert all(c == 6*b - a for a, b, c in zip(tree_counts, tree_counts[1:], tree_counts[2:]))
print("Constant straight turns, spanning trees:", tuple(map(str, tree_counts)))
```

## First differing grades

Compute characteristic polynomials directly to locate the first differing grades. Check the fourth and sixth moments in terms of bends and adjacent turns in the same direction.

[[en/Graph Transformations and Gluing/Spectra of Isomers/Spectral Distinguishability of SLR Chains#Coinciding leading coefficients|Related section of the note]].

```python
for first, second, expected_grade in (("LL", "LR", 6), ("LSL", "LRL", 4), ("SL", "LS", None)):
    first_graph = chain(first + "S")[0]
    second_graph = chain(second + "S")[0]
    difference = Poly(characteristic(first_graph) - characteristic(second_graph), x)
    grade = None if difference.is_zero else len(first_graph.context.labels) - difference.degree()
    assert grade == expected_grade
    print("First different grade", first, second, "=", grade)
for word in ("LL", "LR", "LSL", "LRL"):
    graph = chain(word + "S")[0]
    matrix = Matrix(laplacian(graph).value.values)
    n = len(word) + 2
    bends = sum(letter != "S" for letter in word)
    repeated_turns = sum(a == b and a != "S" for a, b in zip(word, word[1:]))
    assert (matrix**4).trace() == 648*n - 228 + 4*bends
    assert (matrix**6).trace() == 13656*n - 8112 + 576*bends + 6*repeated_turns
```

## Transfer for a periodic word

At $\xi=-1$, check cyclic phase similarity, the reciprocal quartic factor, and the scalar recurrence with constant right-hand side for $LR$, $SL$, and $LLS$. Compare the first values with direct rooted polynomials.

[[en/Graph Transformations and Gluing/Spectra of Isomers/Periodic SLR Chains - Recurrences and Spectra#A worked recurrence for period LR|Related section of the note]].

```python
def period_matrix(word):
    matrix = eye(5)
    for letter in word:
        matrix = integer_operators[letter] * matrix
    return matrix


for word in ("LR", "SL", "LLS"):
    matrix = period_matrix(word)
    rotated = period_matrix(word[1:] + word[0])
    first = integer_operators[word[0]]
    assert rotated * first == first * matrix
    characteristic_period = matrix.charpoly(q).as_expr()
    quotient, remainder = Poly(characteristic_period, q).div(Poly(q-1, q))
    coefficients = quotient.all_coeffs()
    assert remainder.is_zero and coefficients == coefficients[::-1]
    row = integer_operators["S"][0, :]
    sequence = [(row * matrix**k * integer_seed)[0] for k in range(9)]
    residuals = [sum(a*b for a, b in zip(coefficients, reversed(sequence[k:k+5]), strict=True))
                 for k in range(5)]
    assert len(set(residuals)) == 1
    assert Matrix(5, 5, lambda i, j: sequence[i+j]).det() != 0
    for repeats in range(2):
        graph = chain(word*repeats + "S")[0]
        assert sequence[repeats] == sum(laplacian_polynomial(graph))
    print("Period", word, "first rooted totals:", sequence[:3])
```
