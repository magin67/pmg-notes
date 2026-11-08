"""Check the displayed first square step by exhaustive forests and a determinant."""
from collections import Counter
import sympy as sp
from verify_weaving_exponential import forest_data, projections, laplacian, t

def main():
    # a=0, b=1, c=2, d=3; the initial edge is ab, output is (c,d).
    edges=[(0,1),(0,2),(2,3),(3,1)]
    types,states=forest_data(4,edges,(2,3))
    expected=Counter({
        ((1,1),()):1, ((1,1),(2,)):1,
        ((2,),()):1, ((2,),(2,)):1,
        ((2,1),()):1, ((1,2),()):1,
        ((2,2),()):1, ((3,1),()):1, ((1,3),()):1,
        ((3,),()):2, ((4,),()):4,
    })
    assert states==expected
    z2,z3,z4=sp.symbols('z2 z3 z4');z={1:1,2:z2,3:z3,4:z4}
    top=sum(count*t**sum(typ)*sp.prod(z[k+1] for k in typ) for typ,count in types.items())
    assert sp.expand(top-(1+4*t*z2+t**2*(4*z3+2*z2**2)+4*t**3*z4))==0
    fc=fd=0
    for (active,closed),count in states.items():
        term=count*t**sum(s-1 for s in active+closed)
        if len(active)==1:fc+=term
        else:fd+=term
    assert sp.expand(fc-(t+3*t**2+4*t**3))==0
    assert sp.expand(fd-(1+3*t+3*t**2))==0
    f,p=projections(types)
    assert sp.expand(f-(1+4*t+6*t**2+4*t**3))==0
    assert sp.expand(p-(1+8*t+20*t**2+16*t**3))==0
    assert sp.expand((sp.eye(4)+t*laplacian(4,edges)).det()-p)==0
    print('PASS: all 16 edge subsets; 15 forests; full first state; two boundary states; both evaluations; independent determinant.')

if __name__=='__main__':main()
