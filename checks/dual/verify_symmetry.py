"""Exact zero-sum and tetrahedron identities on 2..8 elements.

Run: python checks/dual/verify_symmetry.py
Uses only the standard library; writes JSON to stdout and creates no files.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json
import verify_vector as v

square = lambda a: v.tensor(a, a)
def main():
    cases = 0
    for n in range(2, 9):
        vertices = [v.coform([i], n) for i in range(n)]
        total = {}
        for a in vertices: total = v.add(total, square(a))
        for r in range(1, n):
            left = {}
            for S in combinations(range(n), r):
                s = {}
                for i in S: s = v.add(s, vertices[i])
                left = v.add(left, square(s))
            assert left == v.add({}, total, F(comb(n-2, r-1)))
            cases += 1
        for ids in combinations(range(n), 4):
            a, b, c, d = [vertices[i] for i in ids]
            diff = lambda x, y: v.add(y, x, F(-1))
            lhs = {}
            for p, q, r, s in [(a,b,c,d), (a,c,b,d), (a,d,b,c)]:
                lhs = v.add(lhs, square(v.wedge(diff(p,q), diff(r,s))))
            rhs = {}
            for p, q, r in combinations([a,b,c,d], 3):
                rhs = v.add(rhs, square(v.wedge(diff(p,q), diff(p,r))))
            assert lhs == rhs
            cases += 1
    result = {'status': 'passed', 'n': '2..8', 'tensor_identities': cases,
              'checks': ['zero-sum subset-square identities', 'tetrahedron identities in the quotient']}
    print(json.dumps(result))


if __name__ == "__main__":
    main()
