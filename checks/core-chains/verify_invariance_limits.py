"""Exact, explicitly labelled constructions for the limits-of-invariance note."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations
from pathlib import Path
from random import Random
import json

from verify_admissible_chains import cycle, determinant, edge, laplacian
from verify_matroid_invariance import direct_metrics


def cyclic(m):
    return {'name':f'C{m}', 'size':m, 'edges':cycle(list(range(m)))}


def complete(m):
    return {'name':f'K{m}', 'size':m, 'edges':set(combinations(range(m),2))}


def prism(m):
    es=cycle(list(range(m))) | cycle(list(range(m,2*m))) | {(i,i+m) for i in range(m)}
    return {'name':f'C{m} x K2', 'size':2*m, 'edges':es}


def rank(vertices, edges):
    parent={v:v for v in vertices}
    def find(v):
        while parent[v]!=v:
            parent[v]=parent[parent[v]];v=parent[v]
        return v
    result=0
    for a,b in edges:
        a,b=find(a),find(b)
        if a!=b:
            parent[b]=a;result+=1
    return result


def induced(es,vs):
    return {e for e in es if set(e)<=set(vs)}


def assemble(name, templates, attachments, extra_contacts=None):
    """New core k is glued to a previous core by ordered local vertex lists."""
    extra_contacts=extra_contacts or {}
    maps=[list(range(templates[0]['size']))]
    fresh=templates[0]['size']
    seams=[]
    for k,(parent,left,right) in enumerate(attachments,1):
        assert parent<k and len(left)==len(right)==len(set(left))==len(set(right))
        mp=dict(zip(right,[maps[parent][v] for v in left]))
        assert len(set(mp.values()))==len(mp)
        for v in range(templates[k]['size']):
            if v not in mp:mp[v]=fresh;fresh+=1
        maps.append([mp[v] for v in range(templates[k]['size'])])
        common=[maps[parent][v] for v in left]
        seams.append({'parent':parent,'child':k,'parent_local':left,'child_local':right,
                      'common_vertices_in_order':common})
    assert len(maps)==len(templates)
    core_edges=[{edge(mp[a],mp[b]) for a,b in t['edges']} for mp,t in zip(maps,templates)]
    declared={(s['parent'],s['child']):set(s['common_vertices_in_order']) for s in seams}
    intersections=[]
    for i,j in combinations(range(len(maps)),2):
        shared=set(maps[i]) & set(maps[j])
        assert shared==declared.get((i,j),set(extra_contacts.get((i,j),[]))), (name,i,j,shared)
        common_edges=core_edges[i] & core_edges[j]
        assert induced(core_edges[i],shared)==induced(core_edges[j],shared)==common_edges
        if shared:
            intersections.append({'cores':[i,j],'vertices':sorted(shared),'edges':sorted(common_edges),
                                  'components':len(shared)-rank(shared,common_edges)})
    vertices=set().union(*map(set,maps));es=set().union(*core_edges)
    assert vertices==set(range(fresh)) and rank(vertices,es)==len(vertices)-1
    for mp,t in zip(maps,templates):
        assert len(mp)==len(set(mp))==t['size']
    for seam in seams:
        vs=seam['common_vertices_in_order']
        seam['common_edges']=sorted(induced(es,vs))
    L,R,tau,rho,d,alpha=direct_metrics(vertices,sorted(es))
    rec={'name':name,'N':len(templates),'n':len(vertices),'E':len(es),
         'templates':[dict(t,edges=sorted(t['edges'])) for t in templates],
         'core_vertex_maps':maps,'core_edges':[sorted(e) for e in core_edges],
         'attachments':seams,'actual_intersections':intersections,
         'vertices':sorted(vertices),'edges':sorted(es),'tau':tau,'rho':str(rho),'rho_decimal':float(rho),
         'degree_sequence':sorted(Counter(v for e in es for v in e).values(),reverse=True),
         'resistances_to_vertex_zero':list(map(str,d)), 'circumcenter_weights':list(map(str,alpha))}
    return rec,L,R


def triple(name,template,source,left,right,rotation=0,extra_contacts=None):
    target=right[rotation:]+right[:rotation]
    return assemble(name,[template]*3,[(0,left,source),(0,target,source)],extra_contacts)


def tree_check(rec):
    cores=[set(c) for c in rec['core_vertex_maps']]
    for i in range(len(cores)):
        incident=[set(s['common_vertices_in_order']) for s in rec['attachments'] if i in (s['parent'],s['child'])]
        assert all(not(a & b) for a,b in combinations(incident,2))
    N=rec['N'];M=[[0]*N for _ in range(N)]
    for i,t in enumerate(rec['templates']):M[i][i]=t['size']
    for seam in rec['attachments']:
        vs=seam['common_vertices_in_order'];es=seam['common_edges']
        assert len(es)==len(vs)-1 and rank(vs,es)==len(vs)-1
        i,j=seam['parent'],seam['child'];M[i][j]=M[j][i]=-len(es)
    members=defaultdict(list)
    for i,es in enumerate(rec['core_edges'],1):
        for e in es:members[tuple(e)].append(i)
    dual={e:tuple(fs) if len(fs)==2 else (0,fs[0]) for e,fs in members.items()}
    assert all(1<=len(fs)<=2 for fs in members.values())
    dual_edges=list(dual.values());DL=laplacian(set(range(N+1)),dual_edges)
    assert [row[1:] for row in DL[1:]]==M and determinant(M)==rec['tau']
    assert rec['E']-rec['n']+1==N
    es=sorted(dual,key=lambda e:(dual[e],e));m=len(es);full=(1<<m)-1
    masks={0,full}
    for k in (1,2):
        for chosen in combinations(range(m),k):
            mask=sum(1<<j for j in chosen);masks.update((mask,full^mask))
    rng=Random(517)
    masks.update(rng.getrandbits(m) for _ in range(256))
    for mask in masks:
        A=[es[i] for i in range(m) if mask>>i&1]
        comp=[dual[es[i]] for i in range(m) if not(mask>>i&1)]
        assert rank(rec['vertices'],A)==len(A)+rank(range(N+1),comp)-N
    rec.update(dual_cofactor=M,dual_vertex_zero_is_exterior=True,
               edge_dual_correspondence=[{'edge':e,'dual_endpoints':dual[e]} for e in es],
               dual_rank_checks=len(masks))


def small_forest_check(rec,R):
    es=rec['edges'];f=[0]*rec['n']
    for mask in range(1<<len(es)):
        chosen=[e for i,e in enumerate(es) if mask>>i&1]
        if rank(rec['vertices'],chosen)==len(chosen):f[len(chosen)]+=1
    H2=sum(R[a][b]**2 for a,b in es)
    assert f[-1]==rec['tau'] and Q(f[-2],3*f[-1])-H2/12==Q(rec['rho'])
    rec.update(ordinary_forest_coefficients=f,H2=str(H2))


def cycle4_counts(t):
    counts=Counter()
    for vertices in combinations(range(t['size']),4):
        for rest in permutations(vertices[1:]):
            vs=(vertices[0],)+rest
            if vs[1]>vs[-1]:continue
            es=cycle(list(vs))
            if es<=t['edges']:counts.update(es)
    return counts


def main():
    records=[]
    def add(result,tree=False,small=False):
        rec,L,R=result
        if tree:tree_check(rec)
        if small:small_forest_check(rec,R)
        records.append(rec)
        print(rec['name'],rec['n'],rec['E'],rec['tau'],rec['rho'],flush=True)
        return rec,L
    add(assemble('hex4_path',[cyclic(6)]*4,[(i,[3,4],[0,1]) for i in range(3)]),tree=True)
    add(assemble('hex4_star',[cyclic(6)]*4,[(0,[i,i+1],[0,1]) for i in (0,2,4)]),tree=True)
    for variant,slots in enumerate([[[0],[2,3],[5,6,7]],[[0],[1,2],[4,5,6]]]):
        add(assemble('fixed_tree_variant_'+str(variant),[cyclic(m) for m in [9,3,5,6]],
                     [(0,vs,list(range(len(vs)))) for vs in slots]),tree=True)
    add(assemble('fixed_tree_reversed',[cyclic(m) for m in [9,3,5,6]],
                 [(0,vs,list(reversed(range(len(vs))))) for vs in [[0],[2,3],[5,6,7]]]),tree=True)
    variants=[r for r in records if r['name'].startswith('fixed_tree')]
    assert all((r['tau'],r['rho'],r['dual_cofactor'])==(variants[0]['tau'],variants[0]['rho'],variants[0]['dual_cofactor']) for r in variants)
    for label,right in [('A',[2,3,6,7]),('B',[6,7,10,11])]:
        rec,_=add(triple('disconnected_'+label,cyclic(12),[0,1,4,5],[0,1,4,5],right))
        assert all(x['components']==2 for x in rec['actual_intersections'])
        assert rec['E']-rec['n']+1==5
    add(triple('tetra_disjoint',complete(4),[0,1],[0,1],[2,3]))
    add(triple('tetra_adjacent',complete(4),[0,1],[0,1],[0,2],extra_contacts={(1,2):[0]}))
    cube=prism(4)
    for label,right in [('same_face',[2,3]),('opposite',[6,7]),('skew',[2,6])]:
        rec,_=add(triple('cube_'+label,cube,[0,1],[0,1],right))
        rec['middle_boundary_induced_edges']=sorted(induced(cube['edges'],[0,1]+right))
    autos=[p for p in permutations(range(8)) if {edge(p[a],p[b]) for a,b in cube['edges']}==cube['edges']
           and {p[0],p[1]}=={0,1}]
    assert len(autos)==4
    orbits=[sorted({edge(p[a],p[b]) for p in autos}) for a,b in [(2,3),(6,7),(2,6)]]
    assert list(map(len,orbits))==[2,1,4]
    assert set().union(*map(set,orbits))=={e for e in cube['edges'] if not(set(e)&{0,1})}
    t=prism(6);source=[0,1,7,6]
    prism_proofs=[]
    for j in (2,3):
        for rotation in (0,1):
            rec,L=add(triple(f'prism_j{j}_r{rotation}',t,source,source,[j,j+1,j+7,j+6],rotation))
            if rotation==0:
                hrec,HL=add(triple(f'base_hexagons_j{j}',cyclic(6),[0,1],[0,1],[j,j+1]),tree=True)
                h=hrec['n']
                shifted=[[HL[a][b]+(2 if a==b else 0) for b in range(h)] for a in range(h)]
                factor=determinant(shifted)
                assert Q(hrec['tau'],2)*factor==rec['tau']
                # Explicit isomorphism to the Cartesian product, via local core maps.
                phi={}
                for hp,pp in zip(hrec['core_vertex_maps'],rec['core_vertex_maps']):
                    for v in range(6):
                        for layer in range(2):
                            target=pp[v+6*layer];key=(hp[v],layer)
                            assert key not in phi or phi[key]==target
                            phi[key]=target
                pes={edge(phi[a,k],phi[b,k]) for a,b in hrec['edges'] for k in range(2)}
                pes|={edge(phi[a,0],phi[a,1]) for a in hrec['vertices']}
                assert pes==set(map(tuple,rec['edges']))
                prism_proofs.append({'j':j,'base_tau':hrec['tau'],'det_shifted_laplacian':int(factor),'prism_tau':rec['tau']})
    counts=cycle4_counts(t)
    assert counts[(0,1)]==1 and counts[(0,6)]==2
    A,_=add(assemble('equal_tau_A',[cyclic(4),cyclic(3)],[(0,[0],[0])]),small=True)
    bipartite={'name':'K2,3','size':5,'edges':{edge(a,b) for a in [0,1] for b in [2,3,4]}}
    B,_=add(assemble('equal_tau_B',[bipartite,complete(2)],[(0,[0],[0])]),small=True)
    assert A['tau']==B['tau']==12 and A['rho']=='77/144' and B['rho']=='7/12'
    assert A['ordinary_forest_coefficients'][-2]==30 and B['ordinary_forest_coefficients'][-2]==32
    expected={
        'hex4_path':(1189,'7514229/5654884'),'hex4_star':(1188,'1931/1452'),
        'disconnected_A':(28160,'39255199/24780800'),'disconnected_B':(26460,'100697/58800'),
        'tetra_disjoint':(2304,'91/288'),'tetra_adjacent':(2240,'1831/5600'),
        'cube_same_face':(38395904,'925251899/1405950016'),
        'cube_opposite':(38600704,'29149547/44405888'),
        'cube_skew':(38651904,'14934827209/22796168256'),
        'prism_j2_r0':(25708969440,'1577840090603782727/2294969130787687200'),
        'prism_j2_r1':(25999447104,'6440697234937240577/9388489579356860928'),
        'prism_j3_r0':(25762140408,'227948734512412671515/331843939200753203232'),
        'prism_j3_r1':(26037789636,'464711264225412294751/677966489128589012496')}
    assert all((r['tau'],r['rho'])==expected[r['name']] for r in records if r['name'] in expected)
    result={'graphs':records,'graph_count':len(records),
            'cube_pair_orbits_with_edge_01_fixed':orbits,
            'prism_cartesian_product_checks':prism_proofs,
            'prism_edge_four_cycle_counts':{f'{a}-{b}':v for (a,b),v in sorted(counts.items())},
            'scope':'Exact finite examples; general statements are proved in the note. No closure models.'}
    Path(__file__).with_name('invariance-limits-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Verified',len(records),'explicit graphs; all radii checked by two separate inversions.')


if __name__=='__main__':
    main()
