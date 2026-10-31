"""Exact finite checks for frontier-20261029-rightSN-nonlocal-regularity-v1.md.
(1) In the non-RIGHTSN band RB22^1 (2x2 rectangular band with identity adjoined), find elements
    e,x,y with exeyex != eyex.  Then check that the image semigroupoid of the graph e:c->c', x,y:c'->c
    has right-seminormal local semigroups <ex,ey> and <xe,ye>.
(2) Check the identity xyxzxy = xzxy on every triple of two explicit RIGHTSN bands: the 306-element
    S45 canonical band (from its pinned JSON) and a host band rebuilt from the group-top checker.
(3) Check condition (C) on regular, pure, RRL sources from S45 (full Rees source) and from sampled
    subsemigroups of P(B5,D8): for all e,x,y with ex, ey idempotent and q(ex)=q(ey),
    (ex)(ey)(ex)=(ey)(ex).  As a negative control, find a regular pure NON-RRL source violating (C).
Integer table arithmetic only."""
import json,random
from itertools import product
from pathlib import Path
R=Path(__file__).resolve().parent
def adjoin1(T):
    n=len(T);return [[y if x==n else (x if y==n else T[x][y]) for y in range(n+1)] for x in range(n+1)]
def gen_sub(T,gens):
    S=set(gens);todo=list(gens)
    while todo:
        a=todo.pop()
        for b in list(S):
            for c in (T[a][b],T[b][a]):
                if c not in S:S.add(c);todo.append(c)
    return sorted(S)
def rightSN_on(T,S):
    return all(T[T[T[T[T[x][y]][x]][z]][x]][y]==T[T[T[x][z]][x]][y] for x in S for y in S for z in S)
# (1)
RB22=[[2*(x//2)+(y%2) for y in range(4)] for x in range(4)];B=adjoin1(RB22);n=len(B)
assert all(B[x][x]==x for x in range(n)) and all(B[B[x][y]][z]==B[x][B[y][z]] for x in range(n) for y in range(n) for z in range(n))
assert not rightSN_on(B,range(n))
wit=None
for e,x,y in product(range(n),repeat=3):
    lhs=B[B[B[B[B[e][x]][e]][y]][e]][x];rhs=B[B[B[e][y]][e]][x]
    if lhs!=rhs:
        Lc=gen_sub(B,[B[e][x],B[e][y]]);Lc2=gen_sub(B,[B[x][e],B[y][e]])
        if rightSN_on(B,Lc) and rightSN_on(B,Lc2):wit=(e,x,y,lhs,rhs,Lc,Lc2);break
assert wit is not None
print('PASS (1) RB22^1 not RIGHTSN; witness e,x,y =',wit[:3],'exeyex =',wit[3],'eyex =',wit[4],
      'local semigroups',wit[5],wit[6],'both RIGHTSN')
# (2)
J=json.loads((R/'frontier-20261029-source45-rightSN-canonical-host-data-v1.json').read_text())
T306=J['band_table'];m=len(T306)
ok=True
for x in range(m):
    for y in range(m):
        xy=T306[x][y];xyx=T306[xy][x]
        for z in range(m):
            if T306[T306[T306[xyx][z]][x]][y]!=T306[T306[T306[x][z]][x]][y]:ok=False;break
        if not ok:break
    if not ok:break
assert ok
print('PASS (2a) xyxzxy=xzxy on all',m**3,'triples of the 306-element S45 canonical band')
import importlib.util
spec=importlib.util.spec_from_file_location('gt',R/'frontier-20261029-group-top-two-level-host-checker-v1.py');gt=importlib.util.module_from_spec(spec);spec.loader.exec_module(gt)
random.seed(1);hb=None
while hb is None:
    g=random.sample(range(40),2);S=gt.closure(g)
    pos={s:k for k,s in enumerate(S)};M=[[pos[gt.PT[a][b]] for b in S] for a in S];act=[gt.PACT[s] for s in S]
    if len(set(act))<8:continue
    r=gt.analyse(M,act)
    if r is None:continue
    K,H,h=r
    if not any(e<f and act[e]==act[f] and M[e][f]==f and M[f][e]==e for e in range(len(M)) for f in range(len(M)) if M[e][e]==e and M[f][f]==f):continue
    hb=gt.build(M,act,K,H,h)[0]
assert rightSN_on(hb,range(len(hb)))
print('PASS (2b) xyxzxy=xzxy on all triples of a',len(hb),'element group-top host band')
# (3)
P8=((0,0),(0,1))
def condC(M,act):
    N=len(M);bad=0
    for e in range(N):
        for x in range(N):
            a=M[e][x]
            if M[a][a]!=a:continue
            for y in range(N):
                b=M[e][y]
                if M[b][b]!=b or act[a]!=act[b]:continue
                if M[M[a][b]][a]!=M[b][a]:bad+=1
    return bad
def rrl(M):
    N=len(M);E=[x for x in range(N) if M[x][x]==x]
    return all(M[M[f][g]][f]==M[g][f] for e in E for f in E if M[e][f]==f==M[f][e] for g in E if M[e][g]==g==M[g][e])
A=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4));P=((4,4,4),(4,1,3),(4,4,1));th=(0,1,0,1,0)
S45=list(product(range(3),range(5),range(3)));ix={s:k for k,s in enumerate(S45)}
M45=[[ix[(x[0],A[A[x[1]][P[x[2]][y[0]]]][y[1]],y[2])] for y in S45] for x in S45]
assert rrl(M45)
c45=condC(M45,[(x[0],th[x[1]],x[2]) for x in S45])
assert c45==0
print('PASS (3a) S45 (natural actor) is RRL and satisfies (C): violations',c45)
B5=[[0,2,2,4,4],[0,1,2,1,4],[0,2,2,2,4],[0,3,2,3,4],[0,4,2,4,4]];SW=(0,3,4,1,2)
B51=adjoin1(B5);SW1=SW+(5,)
PB=[(b,(i,g,l)) for b in range(6) for i in range(2) for g in range(2) for l in range(2)];PIX={x:k for k,x in enumerate(PB)}
def pm(x,y):
    b,(i,g,l)=x;c,(j,h,mm)=y;w=g^P8[l][j];return PIX[(B51[b][SW1[c] if w else c],(i,w^h,mm))]
PT=[[pm(x,y) for y in PB] for x in PB]
random.seed(5);good=0;non=0;nonviol=0;seen=set();tries=0
while tries<6000:
    tries+=1;g=random.sample(range(len(PB)),random.choice((2,3)));S=gen_sub(PT,g)
    if tuple(S) in seen or len(S)>120:continue
    seen.add(tuple(S));pos={s:k for k,s in enumerate(S)};M=[[pos[PT[a][b]] for b in S] for a in S];act=[PB[s][1] for s in S];N=len(M)
    if not all(any(M[M[x][y]][x]==x for y in range(N)) for x in range(N)):continue
    if not all((M[x][x]==x)==(act[x][1]==P8[act[x][2]][act[x][0]]) for x in range(N)):continue
    c=condC(M,act)
    if rrl(M):
        assert c==0;good+=1
    else:
        non+=1;nonviol+=(c>0)
assert good>=200 and non>0 and nonviol==non
print('PASS (3b) P(B5^1,D8), 2-3 generators, 6000 draws:',good,'distinct regular pure RRL sources all satisfy (C);',non,'regular pure NON-RRL sources all violate (C) (consistent with (C) => RRL)')
print('LIMIT finite checks only; the universal statements are the written proofs in the note')
