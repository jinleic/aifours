#!/usr/bin/env python3
"""Independent f82 review: parse literal written collision certificates, then
check exact finite controls. No author checker is imported or executed.
"""
import ast
import hashlib
import itertools
import re
from functools import lru_cache
from pathlib import Path

ROOT = Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion')
FILES = {
    'escape': ('frontier-20261028-zero-column-multib-escape-v1.md','ae6ffc9c29f74b1ea4951a50c2c9b79e82ebd2362883896122c93ef55eeb49b5'),
    'seven': ('frontier-20261028-seven-head-border-obstruction-v1.md','713afb914e2781c8367e31726c298bc158c2c5b61176277c2d219762dfd96e24'),
    'seven_checker': ('frontier-20261028-seven-head-symbolic-check.py','5a99d1a528228ddbb6165dca04e80a4d41ef9f4b7faf1359409d51adcc45027d'),
    'eight': ('frontier-20261028-eight-head-border-obstruction-v1.md','803c69db29d403a1a2fec137dcd9f50e132356802b00b7d64ac2e9138de4b412'),
    'eight_checker': ('frontier-20261028-eight-head-certificate.py','6e629ecf8906ad4dc7b3d3e4b87dd44a8ffaa12c59b7ce3e908f15ec36a9eeb6'),
}
texts = {}
for key,(name,expected) in FILES.items():
    data = (ROOT/name).read_bytes()
    assert hashlib.sha256(data).hexdigest() == expected, (key, 'hash mismatch')
    texts[key] = data.decode('utf-8').splitlines()

# Integer affine vectors in (1,U,V,W), interpreted over every cyclic group.
def plus(a,b): return tuple(x+y for x,y in zip(a,b))
def minus(a,b): return tuple(x-y for x,y in zip(a,b))
def const(k): return (k,0,0,0)
def scale(k,a): return tuple(k*x for x in a)
ZERO=const(0)
U,V,W=(0,1,0,0),(0,0,1,0),(0,0,0,1)
P=(ZERO,const(3),const(8),const(11),U,V,W)

def ev_ast(x,env):
    if isinstance(x,ast.Constant) and isinstance(x.value,int): return const(x.value)
    if isinstance(x,ast.Name): return env[x.id]
    if isinstance(x,ast.UnaryOp) and isinstance(x.op,ast.USub): return scale(-1,ev_ast(x.operand,env))
    if isinstance(x,ast.BinOp):
        if isinstance(x.op,ast.Add): return plus(ev_ast(x.left,env),ev_ast(x.right,env))
        if isinstance(x.op,ast.Sub): return minus(ev_ast(x.left,env),ev_ast(x.right,env))
        if isinstance(x.op,ast.Mult) and isinstance(x.left,ast.Constant) and isinstance(x.left.value,int):
            return scale(x.left.value,ev_ast(x.right,env))
    raise ValueError(ast.dump(x))
def ev(s,env): return ev_ast(ast.parse(s.strip(),mode='eval').body,env)
def term_parts(s,env):
    node=ast.parse(s.strip(),mode='eval').body
    assert isinstance(node,ast.BinOp) and isinstance(node.op,ast.Add), s
    return ev_ast(node.left,env),ev_ast(node.right,env)
base={'U':U,'V':V,'W':W}
oldq={const(i) for i in (0,1,7,13,14)}

def check_seven():
    lines=texts['seven']
    # Read the actual inline candidate identities, preserving their source line.
    entries=[]
    for literal in lines[28].strip().rstrip('.').split(','):
        lhs,rhs=literal.split('=')
        q,p=term_parts(lhs,base); anchor,p2=term_parts(rhs,base)
        assert p in P[:4] and p2 in P[:4] and p != p2 and anchor in oldq
        assert plus(q,p)==plus(anchor,p2)
        entries.append(q)
    assert set(entries)=={minus(const(6),p) for p in P[:4]}
    def table(first,last,target,heads,anchors):
        qs=[]
        for ln in range(first,last+1):
            line=lines[ln-1].strip()
            hit=re.fullmatch(r'(\S+)\s+(.+?)\s*=\s*(.+?)(?:\s+\[.*\])?',line)
            assert hit, (ln,line)
            q=ev(hit.group(1),base)
            q_l,p=term_parts(hit.group(2),base)
            k,p2=term_parts(hit.group(3),base)
            assert q==q_l and p in heads and p2 in heads and p!=p2 and k in anchors, (ln,line)
            assert plus(q,p)==plus(k,p2), (ln,line)
            qs.append(q)
        assert len(set(qs))==len(qs)
        return set(qs)
    q4=table(34,38,plus(U,const(4)),P[:5],oldq)
    assert q4=={minus(plus(U,const(4)),p) for p in P[:5]}
    edge=ev('U-V+4',base)
    assert q4|{edge}=={minus(plus(U,const(4)),p) for p in P[:6]}
    q9=table(51,55,plus(U,const(9)),P[:6],oldq|{edge})
    assert q9|{plus(U,const(9))}=={minus(plus(U,const(9)),p) for p in P[:6]}
    # Literal endpoint identity and V<->U symmetry, as integer coefficients.
    end=lines[58].strip().rstrip(',')
    lhs,rhs=end.split('=')
    lq,lp=term_parts(lhs,base); rq,rp=term_parts(rhs,base)
    assert lp in P[:6] and rp in P[:6] and lp!=rp and plus(lq,lp)==plus(rq,rp)
    swap=lambda x:(x[0],x[2],x[1],x[3])
    assert swap(edge)==ev('V-U+4',base) and swap(lq)==rq
    # Independent Q=Y lower bound: target 2, five head candidates.
    qtab=[('2','1','3','0'),('1','0','0','1'),('-5','13','8','0'),('-11','14','3','0'),('-12','13','0','1')]
    assert {ev(q,base) for q,_,_,_ in qtab}=={minus(const(2),y) for y in oldq}
    for cand,y,known,y2 in qtab:
        c,y,k,y2=(ev(z,base) for z in (cand,y,known,y2))
        assert y in oldq and y2 in oldq and y!=y2 and k in P[:4] and plus(c,y)==plus(k,y2)
    print('seven: 4 bare-head, 5 five-head, 5 six-head equations, final collision, symmetry, coverage PASS')
    print('tail lower bound: five bare-Q collision equations PASS')

def check_eight():
    lines=texts['eight']; count=0
    env=dict(base); env['E']=ev('U-V+4',env); env['F']=ev('W-U+4',env)
    known=set(oldq)
    def row(n,target,survivors,known):
        nonlocal count
        parts=[x.strip() for x in lines[n-1].strip().strip('|').split('|')]
        assert len(parts)==8 and ev(parts[0],env)==ev(target,env), (n,parts)
        got=[]
        for source,cell in zip(P,parts[1:]):
            if cell=='*': got.append(source); continue
            m=re.fullmatch(r'([A-Z]|\d+)/\(([^,]+),([^,]+)\)',cell)
            assert m, (n,cell)
            k=ev(m.group(1),env); p=ev(m.group(2),env); p2=ev(m.group(3),env)
            assert k in known and p in P and p2 in P and p!=p2, (n,cell,'prerequisites')
            assert plus(minus(ev(target,env),source),p)==plus(k,p2), (n,cell,'identity')
            count+=1
        assert got==[ev(s,env) for s in survivors],(n,got,survivors)
        return [minus(ev(target,env),s) for s in got]
    first=row(31,'U+4',['V','W'],known)
    assert first==[env['E'],ev('U-W+4',env)]
    # Symmetry permutes the two remaining source columns; add E WLOG.
    assert minus(first[0],first[1])==minus(W,V)
    known.add(env['E'])
    assert row(32,'W+4',['U'],known)==[env['F']]; known.add(env['F'])
    branch=row(33,'W+9',['0','V'],known)
    assert branch==[ev('W+9',env),ev('W-V+9',env)]
    branch_base=set(known)
    # First case: add each Q element only after checking its forcing row.
    known=set(branch_base); env['B']=branch[0]; known.add(env['B'])
    env['C']=ev('U-W+9',env)
    assert row(43,'U+9',['W'],known)==[env['C']]; known.add(env['C'])
    env['D']=ev('U+12',env)
    assert row(44,'U+12',['0'],known)==[env['D']]; known.add(env['D'])
    env['H']=ev('W-2*V+12',env)
    assert row(45,'W-V+12',['V'],known)==[env['H']]; known.add(env['H'])
    assert row(46,'U-V+W+12',[],known)==[]
    # Second case has its own meanings for B,D,H; no first-case import.
    known=set(branch_base); env['B']=branch[1]; known.add(env['B'])
    env['D']=ev('W+12',env)
    assert row(54,'W+12',['0'],known)==[env['D']]; known.add(env['D'])
    env['H']=ev('U-2*V+W+12',env)
    assert row(55,'U-V+W+12',['V'],known)==[env['H']]; known.add(env['H'])
    env['I']=ev('W-2*V+15',env)
    assert row(56,'W-V+15',['V'],known)==[env['I']]; known.add(env['I'])
    assert plus(env['H'],const(3))==plus(env['I'],U) and const(3)!=U
    assert count==59
    print('eight: 10 literal rows, 59 collision cells, survivor coverage, branch-local Q dependencies and final collision PASS')

def sardinas_patterson(code):
    # Strict suffix sets of finite words; equality creates the empty suffix.
    r={x[len(y):] for x in code for y in code if len(x)>len(y) and x.startswith(y)}
    seen=set()
    while r:
        s=frozenset(r)
        if s in seen: return True
        seen.add(s)
        nxt=set()
        for suffix in r:
            for word in code:
                if suffix.startswith(word): nxt.add(suffix[len(word):])
                if word.startswith(suffix): nxt.add(word[len(suffix):])
        if '' in nxt: return False
        r=nxt
    return True

def layer_controls():
    for n in (4,5):
        cells=[(i,j) for i in range(n) for j in range(n) if (i,j)!=(0,0)]
        total=ud=anchors=0
        for extras in itertools.combinations(cells,n-1):
            total+=1; B=((0,0),)+extras
            code=['a'*n]+['a'*i+'b'+'a'*j for i,j in B]
            if not sardinas_patterson(code): continue
            ud+=1
            I={i for i,j in B if j==0}
            for h in range(n):
                J={j for i,j in B if i==h}
                assert len({(j+i)%n for j in J for i in I})==len(J)*len(I)
            for k in range(1,len(I)+1):
                for a in itertools.combinations(sorted(I),k):
                    anchors+=1
                    outside=sum(i not in a for i,j in B)
                    assert outside>=n-len(a)*(n//len(I)),(n,B,a)
        print('layer n=%d total=%d UD=%d anchor_checks=%d PASS'%(n,total,ud,anchors))
    B=((0,0),(0,1),(0,2),(1,0)); I={i for i,j in B if j==0}
    assert not sardinas_patterson(['aaaa']+['a'*i+'b'+'a'*j for i,j in B])
    assert sum(i!=0 for i,j in B)<4-(4//len(I))
    print('non-UD packing-violation negative control PASS')

def finite_border_controls():
    A=(0,3,8,11); Y=(0,1,7,13,14)
    assert all(len({(p+q)%n for p in A for q in Y})<20 for n in range(1,26))
    assert len({(p+q)%26 for p in A for q in Y})==20
    counts={k:0 for k in range(4,8)}; searches=0; nodes=0
    for n in range(26,57):
        base={(p+q)%n for p in A for q in Y}
        if len(base)<20: continue
        possible=[p for p in range(n) if p not in A and not ({(p+q)%n for q in Y}&base)]
        for k in range(4,8):
            if n%k or n//k<5: continue
            for extra in itertools.combinations(possible,k-4):
                Pset=A+extra
                occupied={(p+q)%n for p in Pset for q in Y}
                if len(occupied)!=len(Pset)*len(Y): continue
                counts[k]+=1; searches+=1
                masks=[sum(1<<((p+q)%n) for p in Pset) for q in range(n)]
                start=sum(1<<x for x in occupied); full=(1<<n)-1
                @lru_cache(None)
                def can_complete(mask):
                    nonlocal nodes
                    nodes+=1
                    if mask==full: return True
                    available=[v for v in masks if not v&mask]
                    missing=[i for i in range(n) if not (mask>>i)&1]
                    choices=min(([v for v in available if (v>>i)&1] for i in missing),key=len)
                    return any(can_complete(mask|v) for v in choices)
                assert not can_complete(start),(n,Pset)
    print('border n=26..56 all sizes 4..7, Q>=5: compatible P counts %s, searches=%d, nodes=%d, no tiling PASS'%(counts,searches,nodes))
    for n in (60,1320):
        p=(0,3,8,11,1,4); q=range(0,n,6)
        assert len({(x+y)%n for x in p for y in q})==n
        assert not set(Y)<=set(q)
    print('positive direct tilings with old Q anchors dropped at n=60,1320 PASS')

def arithmetic():
    n=1320
    sizes=[p for p in range(1,n+1) if n%p==0 and p>=7 and n//p>=6 and p not in (8,11,220)]
    expected=[10,12,15,20,22,24,30,33,40,44,55,60,66,88,110,120,132,165]
    assert sizes==expected and n-4*(n//5)==264 and n%9!=0
    print('n=1320: 18 necessary-filter divisors and threshold 264 PASS')

if __name__=='__main__':
    check_seven(); check_eight(); layer_controls(); finite_border_controls(); arithmetic()
    print('All checks are bounded controls and formal integer identities; they do not establish a completion.')
