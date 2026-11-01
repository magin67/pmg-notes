"""Exact catalog of P_G(1), modulo the four proved SLR symmetries."""
from pathlib import Path
import argparse
import json

OUT=Path(__file__).resolve().parent

def decode(code, length):
    digits=[]
    for _ in range(length):
        code,r=divmod(code,3);digits.append('SLR'[r])
    return ''.join(reversed(digits))

def value(u):
    a,b,c,d,e=320,144,144,56,55
    for letter in u:
        aa=55*a+34*b+34*c-2*d+21*e
        if letter=='S':
            bb=24*a+16*b+15*c+10*e;cc=24*a+15*b+16*c+10*e
            ee=9*a+6*b+6*c+4*e
        elif letter=='L':
            bb=21*a+21*b+13*c+13*e;cc=24*a+16*b+15*c+10*e
            ee=8*a+8*b+5*c+5*e
        else:
            bb=24*a+15*b+16*c+10*e;cc=21*a+13*b+21*c+13*e
            ee=8*a+5*b+8*c+5*e
        a,b,c,d,e=aa,bb,cc,ee+d,ee
    return 55*a+34*b+34*c-2*d+21*e

def catalog(m):
    seen={};collisions={};count=0
    powers=[3**i for i in range(m+1)]
    def walk(level,w,bar,rev,rbar,a,b,c,d,e):
        nonlocal count
        if w>bar:return
        if level==m:
            if w>rev or w>rbar:return
            count+=1
            v=55*a+34*b+34*c-2*d+21*e
            old=seen.get(v)
            if old is None:seen[v]=w
            else:collisions.setdefault(v,[old]).append(w)
            return
        aa=55*a+34*b+34*c-2*d+21*e
        bs=24*a+16*b+15*c+10*e;cs=24*a+15*b+16*c+10*e
        es=9*a+6*b+6*c+4*e
        el=8*a+8*b+5*c+5*e;er=8*a+5*b+8*c+5*e
        p=powers[level];w*=3;bar*=3
        walk(level+1,w,bar,rev,rbar,aa,bs,cs,es+d,es)
        walk(level+1,w+1,bar+2,rev+p,rbar+2*p,aa,21*a+21*b+13*c+13*e,bs,el+d,el)
        walk(level+1,w+2,bar+1,rev+2*p,rbar+p,aa,cs,21*a+13*b+21*c+13*e,er+d,er)
    walk(0,0,0,0,0,320,144,144,56,55)
    assert count==(3**m+1+3**((m+1)//2)+3**(m//2))//4
    row={'N':m+2,'words':3**m,'graph_classes':count,'distinct_P1':len(seen),
         'collision_groups':len(collisions),'colliding_classes':sum(map(len,collisions.values())),
         'min_P1':min(seen),'max_P1':max(seen),
         'minimum_word':'S'+decode(seen[min(seen)],m),'maximum_word':'S'+decode(seen[max(seen)],m),
         'canonical_order':'S<L<R'}
    pairs=[{'P1':v,'codes':['S'+decode(w,m) for w in ws]} for v,ws in collisions.items()]
    return row,pairs

def summary(rows,pairs):
    return {'max_N':rows[-1]['N'],
            'total_classes':sum(r['graph_classes'] for r in rows),
            'represented_words':sum(r['words'] for r in rows),
            'adjacent_size_intervals_disjoint':all(a['max_P1']<b['min_P1'] for a,b in zip(rows,rows[1:])),
            'rows':rows,'collisions':pairs}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--max-n',type=int,default=18);args=parser.parse_args()
    if args.max_n < 2:
        parser.error('--max-n must be at least 2')
    rows=[];pairs=[]
    for m in range(args.max_n-1):
        row,cl=catalog(m);rows.append(row);pairs.extend(cl)
        print(json.dumps(row),flush=True)
        (OUT/'slr-distinguishability-catalog.json').write_text(json.dumps(summary(rows,pairs),ensure_ascii=False,indent=2),encoding='utf-8')
