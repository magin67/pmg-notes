"""Exact checks of the new KVP geometric illustrations; standard library only."""
from fractions import Fraction as F
import verify as v

def graph(n,edges):
    C=v.zero(n)
    for i,j,c in edges:C[i][j]=C[j][i]=F(c)
    return C

def green(C):
    n=len(C);J0=v.mat(n,lambda i,j:F(1,n))
    return v.sub(v.inv(v.add(v.lap(C),J0)),J0)

def squared_distances(points):
    return v.mat(len(points),lambda i,j:sum((a-b)**2 for a,b in zip(points[i],points[j])))

def check_geometry():
    # The network is specified independently of the proposed Euclidean coordinates.
    C=graph(3,[(0,1,F(1,4)),(0,2,1)])
    Gr=green(C);R=v.dist(Gr);points=[(F(0),F(0)),(F(2),F(0)),(F(0),F(1))]
    assert R==squared_distances(points)
    h=[sum(p[k] for p in points)/3 for k in range(2)];p=[F(1),F(1,2)]
    assert h==[F(2,3),F(1,3)]
    rho0=v.trace(Gr)/3;offset=sum((a-b)**2 for a,b in zip(p,h))
    radii=[sum((a-b)**2 for a,b in zip(x,p)) for x in points]
    assert radii==[F(5,4)]*3 and rho0==F(10,9) and offset==F(5,36)
    assert rho0+offset==radii[0]

    for n,points,expected in [
        (3,[(0,0),(1,0),(1,1)],1),
        (4,[(0,0,0),(1,0,0),(1,1,0),(1,1,1)],6)]:
        R=v.dist(green(graph(n,[(i,i+1,1) for i in range(n-1)])))
        assert R==squared_distances(points) and v.H(R)==expected
    print('PASS network resistances, triangle area, tetrahedron, and circumcenter')

    C=graph(5,[(i,i+1,1) for i in range(4)]);Gr=green(C);R=v.dist(Gr)
    _,w,_=v.dec(R)
    components,_,_=v.dec(C)
    a=[v.scale(v.mul(v.lap(X),[[t] for t in w]),F(1,10)) for X in components[:3]]
    metric=[[v.mul(v.mul(v.trans(x),Gr),y)[0][0] for y in a] for x in a]
    planar=[(30,0),(-4,2),(-5,-5)]
    projected=[[F(10,150**2)*sum(u*t for u,t in zip(x,y)) for y in planar] for x in planar]
    assert metric==projected
    assert v.rank(metric)==2 and v.trace(metric)==F(97,225) and sum(v.rows(metric))==F(1,5)
    print('PASS exact planar realization of mixed KVP vectors for P5')

if __name__=='__main__':
    if not __debug__:raise SystemExit('Run without -O: assertions are required.')
    check_geometry()
