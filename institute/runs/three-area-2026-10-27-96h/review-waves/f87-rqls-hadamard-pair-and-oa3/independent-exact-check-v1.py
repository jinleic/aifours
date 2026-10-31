#!/usr/bin/env python3
"""Independent exact f87 review: no author code execution or third-party libraries."""
import ast
import hashlib
import json
import math
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path

EVIDENCE = Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/rqls10')

def require(ok, what):
    if not ok:
        raise AssertionError(what)

def pinned(name, digest):
    b = (EVIDENCE / name).read_bytes()
    require(hashlib.sha256(b).hexdigest() == digest, 'hash mismatch: ' + name)
    return b

def literal_binding(data, name):
    tree = ast.parse(data)
    hits = [node.value for node in tree.body if isinstance(node, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == name for t in node.targets)]
    require(len(hits) == 1, 'literal assignment count: ' + name)
    return ast.literal_eval(hits[0])

# The only use of the author's Python files is extracting literal data by AST.
E = literal_binding(pinned('frontier-20261028-near-hadamard-pair-exact-v1.py',
    'be0a9fe04893282e8491e2804a7e40bfc354ed324fe5e33530216095c68dcdd3'), 'E')
require(len(E)==10 and all(len(row)==10 and all(type(x)==int and 0<=x<20 for x in row) for row in E), 'E dimensions/range')
require(all(E[0][j] == E[j][0] == 0 for j in range(10)), 'dephasing')

# Compute powers of a root by multiplication in Z[x]/(Phi), not by importing the supplied remainder code.
def powers(phi, count):
    degree = len(phi)-1
    v = [1]+[0]*(degree-1)
    out=[]
    for _ in range(count+1):
        out.append(tuple(v))
        w=[0]+v
        high=w.pop()
        v=[w[j]-high*phi[j] for j in range(degree)]
    require(out[-1] == out[0], 'root period')
    return out[:-1]
r10=powers([1,-1,1,-1,1],10)
r20=powers([1,0,-1,0,1,0,-1,0,1],20)
require(len(set(r10))==10 and len(set(r20))==20, 'primitive roots')

def scale(a,m): return tuple(m*x for x in a)
def plus(a,b): return tuple(x+y for x,y in zip(a,b))
zero4=(0,)*4
families=[]
expected_edges=[{(0,2),(1,5),(3,4),(6,9),(7,8)},
                {(0,1),(2,4),(3,9),(5,8),(6,7)}]
pattern_counts=[]
for shift in range(2):
    defect=set();patterns=Counter()
    for c,d in combinations(range(10),2):
        coeff={p:zero4 for p in (-1,0,1)}
        for t in range(10):
            power=E[t][d]%2-E[t][c]%2
            k=(E[t][d]//2-E[t][c]//2+shift*t*(d-c))%10
            coeff[power]=plus(coeff[power],r10[k])
        actual=tuple(coeff[p] for p in (-1,0,1))
        if actual==(zero4,zero4,zero4):
            continue
        defect.add((c,d))
        # Two algebraically different Laurent forms have the same modulus on |z|=1.
        if shift==0:
            first=(zero4,scale(r10[0],5),scale(r10[9],-5))
            second=(scale(r10[1],-5),scale(r10[0],5),zero4)
        else:
            first=(zero4,scale(r10[0],5),scale(r10[0],-5))
            second=(scale(r10[0],-5),scale(r10[0],5),zero4)
        require(actual in (first,second), 'unexpected Laurent coefficient: '+str((shift,c,d,actual)))
        patterns['z' if actual==first else 'z^-1']+=1
    require(defect==expected_edges[shift], 'defect edge set')
    families.append(defect);pattern_counts.append(dict(patterns))
all_edges=families[0] | families[1]
adj={i:set() for i in range(10)}
for a,b in all_edges: adj[a].add(b);adj[b].add(a)
require(len(all_edges)==10 and all(len(v)==2 for v in adj.values()),'cycle degrees')
seen=set();todo=[0]
while todo:
    i=todo.pop()
    if i not in seen: seen.add(i);todo.extend(adj[i]-seen)
require(len(seen)==10,'cycle connectedness')
char_hits=[]
for c,d in combinations(range(10),2):
    for k in range(10):
        if len({(E[t][c]-E[t][d]-2*k*t)%20 for t in range(10)})==1:
            char_hits.append((c,d,k))
require(not char_hits,'midpoint ray collision')
print('FAMILY: 90/90 Laurent Gram sums; defect edges',*[sorted(x) for x in families])
print('FAMILY: Laurent patterns',pattern_counts,'cycle connected, degree=2')
print('FAMILY: 450/450 midpoint character tests clear')

# Parker transcription and constructed witness; re-check the actual 100 vectors,
# the labels and the classical OA, not the author's validation script.
tables=pinned('frontier-20261028-coordinate-switch-v1.py',
    '13e4960da018e260373b06ec6c1de33a542dac4f3bfc35b986fdfd9d776d8011')
A=literal_binding(tables,'PARKER_A');B=literal_binding(tables,'PARKER_B')
points=[(r,c,int(A[r][c]),int(B[r][c])) for r in range(10) for c in range(10)]
universe=set(product(range(10),repeat=2))
require(len(set(points))==100,'Parker tuple distinctness')
for i,j in combinations(range(4),2):
    require({(q[i],q[j]) for q in points}==universe,'Parker OA projection '+str((i,j)))
pocket=[q for q in points if all(x in (7,8,9) for x in q)]
require(len(pocket)==9,'Parker pocket size')
for i,j in combinations(range(4),2):
    require({(q[i],q[j]) for q in pocket}==set(product((7,8,9),repeat=2)), 'Parker pocket projection')
pocketset=set(pocket)
raw=pinned('frontier-20261028-parker-13ray-result-v1.json',
    '0108335bbbe2d35214761904172490bbbed6976d59dd19748aaa7843276dc9e5')
w=json.loads(raw)['partial_witness']; V=w['array']; labels=w['labels']
require(w['denominator']==3 and len(V)==len(labels)==10,'witness dimensions')
for q in points:
    color,r,c,label=q
    v=[0]*10
    if q in pocketset:
        for z in (7,8,9): v[z]=(3 if z==color else 0)-2
    else: v[color]=3
    require(V[r][c]==v and labels[r][c]==label,'Parker rotated vector/label mismatch')
def dot(a,b):return sum(x*y for x,y in zip(a,b))
require(all(dot(V[r][c],V[r][c])==9 for r in range(10) for c in range(10)),'norms')
for axis in range(3):
    for symbol in range(10):
        if axis==0: block=[V[symbol][c] for c in range(10)]
        elif axis==1: block=[V[r][symbol] for r in range(10)]
        else: block=[V[r][c] for r in range(10) for c in range(10) if labels[r][c]==symbol]
        require(len(block)==10 and all(dot(a,b)==0 for a,b in combinations(block,2)), 'basis '+str((axis,symbol)))
def ray(v):
    g=math.gcd(*v); z=tuple(x//g for x in v)
    return tuple(-x for x in z) if next(x for x in z if x)!=abs(next(x for x in z if x)) else z
counts=Counter(ray(V[r][c]) for r in range(10) for c in range(10))
parallel=sum(n*(n-1)//2 for n in counts.values())
require(len(counts)==13 and parallel==387,'Parker ray count')
print('PARKER: actual transcribed OA 6/6 projections, pocket 6/6; 100 norms, 30 bases, rays',len(counts),'parallel pairs',parallel)

# OA double counts: the sets being counted are not assumed realizable.
# Disjoint Q: one axis has t shared symbols. A outside is all S-memberships
# minus those on Q; D is cross membership in distinct axes; J is same-axis.
for t in range(4):
    outside=100-9-9
    Acount=4*3*(10-3)-3*t
    Dcross=4*3*3*3-2*(3*3*t)
    Jsame=(10-3-3)*t
    I=Dcross+Jsame
    aonly=Acount-I
    neither=outside-(2*Acount-I)
    require(aonly<0 or neither<0,'no disjoint contradiction at t='+str(t))
    print('OA_DISJOINT:', 't',t,'X',outside,'A',Acount,'cross',Dcross,'same',Jsame,'intersection',I,'Aonly',aonly,'neither',neither)
# For a one-cell intersection, Q removes two occurrences of each of four shared symbols.
outside=100-(9+9-1)
Acount=4*3*(10-3)-4*(3-1)
Dcross=4*3*3*3-(2*(4*3*3)-12)
Jsame=4*(10-(3+3-1))
I=Dcross+Jsame
union=2*Acount-I
require((outside,Acount,Dcross,Jsame,I,union)==(83,76,48,20,68,84),'overlap count')
print('OA_OVERLAP: X,A,B,cross,same,intersection,union,neither',outside,Acount,Acount,Dcross,Jsame,I,union,outside-union)
# Exhaust the normalized two-by-two Latin squares; none are orthogonal.
cells=list(product(range(2),repeat=2)); squares=[]
for vals in product(range(2),repeat=4):
    f=dict(zip(cells,vals))
    if all(len({f[r,c] for c in range(2)})==2 for r in range(2)) and all(len({f[r,c] for r in range(2)})==2 for c in range(2)):
        squares.append(vals)
orthogonal=[(u,v) for u in squares for v in squares if len(set(zip(u,v)))==4]
require(len(squares)==2 and not orthogonal,'OA2 impossibility')
print('OA2: normalized Latin squares',len(squares),'orthogonal pairs',len(orthogonal))

# Cosine enclosures from exact pentagon/half-angle radical identities, NOT the
# author's Machin+Taylor series. Every bound and rounding decision is rational.
prec=10**30
s5lo=Q(math.isqrt(5*prec*prec),prec);s5hi=s5lo+Q(1,prec)
require(s5lo*s5lo<5<s5hi*s5hi,'sqrt5 bracket')
def sqrt_floor(q):
    return Q(math.isqrt((q.numerator*prec*prec)//q.denominator),prec)
def sqrt_enclose(lo,hi):
    a=sqrt_floor(lo);b=sqrt_floor(hi)+Q(1,prec)
    require(a*a<=lo and b*b>hi,'sqrt rational enclosure')
    return a,b
c1=sqrt_enclose((5+s5lo)/8,(5+s5hi)/8)
c3=sqrt_enclose((5-s5hi)/8,(5-s5lo)/8)
base=[(Q(1),Q(1)),c1,((1+s5lo)/4,(1+s5hi)/4),c3,
      ((s5lo-1)/4,(s5hi-1)/4),(Q(0),Q(0))]
for j in range(6,11):
    lo,hi=base[10-j];base.append((-hi,-lo))
for j in range(11,20): base.append(base[20-j])
S=10**12
def nearest(x): return (x*S+Q(1,2)).numerator//(x*S+Q(1,2)).denominator
cosints=[]
for j,(lo,hi) in enumerate(base):
    a,b=nearest(lo),nearest(hi)
    require(a==b,'cosine rounding bin '+str(j));cosints.append(a)
print('COS: radical rational brackets; all 20 unique nearest 1e-12 bins',cosints)

# Reconstruct all derivatives from C = (2/100) sum_{c<d,a}(10+2 sum_{t<s} cos(alpha)).
# Gradient tracks the exact vectors for zeta20^k-zeta20^-k; Hessian is integer numerator.
N=81;grad=[[0]*8 for _ in range(N)];M=[[0]*N for _ in range(N)];terms=0
for c,d in combinations(range(10),2):
    for t,s in combinations(range(10),2):
        v={}
        for r,col,sign in ((t,d,1),(t,c,-1),(s,d,-1),(s,c,1)):
            if r and col: v[(r-1)*9+col-1]=sign
        for a in (0,1):
            k=(E[t][d]-E[t][c]-E[s][d]+E[s][c]+2*a*(t-s)*(d-c))%20
            terms+=1
            diff=[x-y for x,y in zip(r20[k],r20[-k%20])]
            for i,vi in v.items():
                for b in range(8): grad[i][b]+=vi*diff[b]
                for j,vj in v.items(): M[i][j]-=4*cosints[k]*vi*vj
require(terms==4050 and all(all(x==0 for x in row) for row in grad),'gradient not zero')
require(all(M[i][j]==M[j][i] for i in range(N) for j in range(N)),'Hessian symmetry')
print('GRADIENT: 81/81 exact zero in Q(zeta20); independent cyclic-basis arithmetic; terms',terms)
D=100*S
for i in range(N): M[i][i]-=D//200
# Exact symmetric fraction-free elimination: pivots are leading principal minors.
piv=[];previous=1;divisions=0
for k in range(N):
    p=M[k][k]
    require(p>0,'nonpositive leading principal minor '+str(k+1))
    piv.append(p)
    if k==N-1: break
    for i in range(k+1,N):
        for j in range(i,N):
            num=p*M[i][j]-M[i][k]*M[k][j]
            q,r=divmod(num,previous)
            require(r==0,'inexact fraction-free division')
            M[i][j]=M[j][i]=q;divisions+=1
    for i in range(k+1,N): M[i][k]=M[k][i]=0
    previous=p
pivhash=hashlib.sha256(('\n'.join(map(str,piv))+'\n').encode()).hexdigest()
require(Q(81*81,S)<Q(1,200),'rounding safety margin')
print('PIVOTS: 81/81 positive leading principal minors; exact divisions',divisions,'SHA256(decimal pivots + LF)',pivhash)
print('PIVOTS: first',piv[0],'last decimal digits',len(str(piv[-1])))
print('BOUND: <=4050 terms * 4/(100*2*1e12) = 81/1e12 per entry; operator <=6561/1e12 < 1/200')
print('ALL EXACT REVIEW CHECKS PASSED')
