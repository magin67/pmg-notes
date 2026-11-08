"""Check the added worked examples directly from graph Laplacians.

This is a small example check, not a rerun of the 16-million-class catalog.
"""
from pathlib import Path
import json
import numpy as np
import sympy as sp
from verify_three_hexagons import graph as pair_graph, laplacian
from verify_slr_code import graph
from draw_slr_code import geometry

HERE=Path(__file__).resolve().parent

def rooted(u):
    g,cores,boundary,edges=graph(u)
    return int((sp.eye(len(g))+laplacian(edges,len(g))).det(method='domain-ge'))

def run():
    xi=sp.Symbol('xi');polys={};spectra={}
    for label in ['A','B']:
        _,edges=pair_graph(label);L=laplacian(edges,14)
        polys[label]=L.charpoly(xi).as_poly()
        eig,vec=np.linalg.eigh(np.array(L,dtype=float))
        assert abs(eig[0])<1e-12 and eig[1]>0
        assert np.max(np.abs(np.array(L,dtype=float)@vec-vec*eig))<1e-12
        assert abs(eig.sum()-32)<1e-12
        eig[0]=0.0;spectra[label]=eig.tolist()
    assert sp.gcd(polys['A'],polys['B']).as_expr()==xi
    assert 55*320+34*144+34*144-2*56+21*55==rooted('')==28435
    square={('S'+u):rooted(u) for u in ['SS','SL','LS','LL']}
    assert square['SSS']-square['SSL']-square['SLS']+square['SLL']==-102487
    straight=91*2518737-216*28435+91*320-3
    turn=96*2504096-706*28435+96*320-3-32
    assert straight==rooted('SS')==223092224
    assert turn==rooted('LL')==220348791
    period=7759*13250645128864264-51561*1709242570740+7759*220480560-28435+19602
    assert period==rooted('LR'*4)==102723627009376555443
    for u in ['SS','SL','LS','LL','L']:
        p,c,e,b=geometry(u);g,cores,boundary,edges=graph(u)
        assert e==set(edges) and c==cores and b==boundary
    result={'spectra_for_plot':spectra,'square_values':square,'square_difference':-102487,
            'two_core_rooted_count':28435,'constant_family_step':{'S':straight,'L':turn},
            'LR_m4':period,'plot_note':'Eigenvalues are approximate drawing coordinates; the common-root claim is checked exactly by polynomial gcd.'}
    (HERE/'editorial-examples-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('PASS: exact example determinants, transfer arithmetic, mixed difference, recurrence steps, figure graphs, and spectral plot residuals.')

if __name__=='__main__':run()
