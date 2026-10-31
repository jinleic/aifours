#!/usr/bin/env python3
"""Independent exact reconstruction of F85; imports no author checker/solver."""
from itertools import product, permutations
from pathlib import Path
import hashlib, json, re

ROOT=Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f85-semigroup-all-cs-globally-regular-band')
manifest=json.loads((ROOT/'manifest-v2.json').read_text())
texts=[]; hashes=[]
for item in manifest['inputs_in_read_order']:
    data=Path(item['path']).read_bytes()
    digest=hashlib.sha256(data).hexdigest()
    if digest!=item['sha256'] or len(data)!=item['bytes'] or data.count(b'\n')!=item['LF']:
        raise RuntimeError('manifest pin mismatch: '+item['path'])
    texts.append(data.decode('utf-8')); hashes.append(digest)
neg,boundary,host=texts[0],texts[2],texts[5]

def text_table(text):
    x=re.search(r'```text\n(.*?)\n```',text,re.S)
    if not x: raise RuntimeError('missing table')
    rows=[tuple(int(v) for v in row.split()) for row in x.group(1).splitlines()]
    if len(rows)!=5 or any(len(row)!=5 or set(row)-set(range(5)) for row in rows):
        raise RuntimeError('bad 5x5 table')
    return tuple(rows)

def amul(x,y):
    if x==4: return y
    if y==4: return x
    # x=(r,g), y=(s,h) encoded as 2r+g, (r,g)(s,h)=(s xor g,g xor h)
    r,g=divmod(x,2); s,h=divmod(y,2)
    return 2*(s^g)+(g^h)
A=tuple(tuple(amul(x,y) for y in range(5)) for x in range(5))
if A!=text_table(neg): raise RuntimeError('source table is not the given semidirect product')
P=((4,4,4),(4,1,3),(4,4,1))
if 'P=((4,4,4),(4,1,3),(4,4,1))' not in neg or 'θ=(0,1,0,1,0)' not in neg:
    raise RuntimeError('unexpected source P/theta')
th=lambda a: 0 if a==4 else a%2
qmat=tuple(tuple(th(x) for x in row) for row in P)
S=tuple(product(range(3),range(5),range(3))); n=len(S)
index={s:i for i,s in enumerate(S)}
def sp(x,y):
    i,a,l=x; j,b,m=y
    return (i,amul(amul(a,P[l][j]),b),m)
mult=tuple(tuple(index[sp(x,y)] for y in S) for x in S)
def q(x): return (x[0],th(x[1]),x[2])
def qp(x,y): return (x[0],x[1]^qmat[x[2]][y[0]]^y[1],y[2])
assert n==45
assert all(amul(amul(x,y),z)==amul(x,amul(y,z)) for x,y,z in product(range(5),repeat=3))
assert all(mult[mult[i][j]][k]==mult[i][mult[j][k]] for i,j,k in product(range(n),repeat=3))
assert all(any(mult[mult[i][j]][i]==i and mult[mult[j][i]][j]==j for j in range(n)) for i in range(n))
E={i for i in range(n) if mult[i][i]==i}
assert len(E)==24
weak_e_obstructions=[]
for i in range(n):
    both={mult[e][i] for e in E}&{mult[i][e] for e in E}&E
    if both and i not in E: weak_e_obstructions.append((S[i],S[min(both)]))
assert not weak_e_obstructions
local_sizes=[]; inverse_failure=None
for e in E:
    corner={mult[mult[e][i]][e] for i in range(n)}
    assert all(mult[i][j] in corner for i,j in product(corner,repeat=2))
    ie=corner&E
    assert all(mult[i][j] in E for i,j in product(ie,repeat=2))
    for i,j,k in product(ie,repeat=3):
        assert mult[mult[mult[mult[i][j]][i]][k]][i]==mult[mult[mult[i][j]][k]][i]
    local_sizes.append(len(corner))
    noncomm=[(i,j) for i,j in product(ie,repeat=2) if mult[i][j]!=mult[j][i]]
    if noncomm and inverse_failure is None:
        i,j=noncomm[0]; inverse_failure=(S[e],S[i],S[j])
assert inverse_failure is not None
nonorth=next((S[i],S[j],S[mult[i][j]]) for i,j in product(E,repeat=2) if mult[i][j] not in E)
assert all(q(S[mult[i][j]])==qp(q(S[i]),q(S[j])) for i,j in product(range(n),repeat=2))
assert all((i in E)==(qp(q(S[i]),q(S[i]))==q(S[i])) for i in range(n))
# All source contexts, including both absent slots. Bit vectors use distinct context positions.
contexts=[None]+list(range(n)); signatures=[]
for i in range(n):
    bits=0; pos=0
    for left in contexts:
        a=i if left is None else mult[left][i]
        for right in contexts:
            b=a if right is None else mult[a][right]
            if b in E: bits |= 1<<pos
            pos+=1
    signatures.append(bits)
assert all((signatures[i]==signatures[j])==(q(S[i])==q(S[j])) for i,j in product(range(n),repeat=2))
assert len(set(signatures))==18

def st(x,y): return S[mult[index[x]][index[y]]]
e=(1,1,1); f=(1,3,1); a=(1,4,0); b=(2,4,0); z=(0,4,1); s=(1,4,1)
assert e!=f and index[e] in E and index[f] in E and q(e)==q(f)
assert (st(e,f),st(f,e),st(a,b),st(b,a),st(s,st(a,z)),st(s,st(b,z)))==(f,e,a,b,e,f)
assert th(s[1])^qmat[s[2]][a[0]]==th(s[1])^qmat[s[2]][b[0]]==1

B=text_table(boundary)
assert B==text_table(host)
def bp(x,y): return B[x][y]
def word(*xs):
    r=xs[0]
    for x in xs[1:]: r=bp(r,x)
    return r
assert all(bp(i,i)==i for i in range(5))
assert all(bp(bp(i,j),k)==bp(i,bp(j,k)) for i,j,k in product(range(5),repeat=3))
corners=[]
for h in range(5):
    c={bp(bp(h,x),h) for x in range(5)}
    assert c=={x for x in range(5) if bp(h,x)==x==bp(x,h)}
    assert all(bp(x,y) in c for x,y in product(c,repeat=2))
    assert all(word(x,y,x,z,x)==word(x,y,z,x) for x,y,z in product(c,repeat=3))
    corners.append(sorted(c))
assert corners==[[0],[1,2,4],[2],[2,3,4],[4]]
assert word(1,0,1,3,1)==2 and word(1,0,3,1)==4
x,u,v,y=0,1,3,1; ee=word(x,u,y); ff=word(x,v,y)
assert (bp(u,v),bp(v,u),ee,ff,bp(ee,ff),bp(ff,ee))==(u,v,2,4,4,2)
upper=lambda seq: [h for h in range(5) if all(bp(h,w)==w==bp(w,h) for w in seq)]
assert upper((x,u,v,y))==[] and upper((ee,ff))==[1,3]
auto=(0,3,4,1,2)
assert all(auto[auto[x]]==x for x in range(5))
assert all(auto[bp(x,y)]==bp(auto[x],auto[y]) for x,y in product(range(5),repeat=2))
assert (bp(3,1),bp(1,3),word(0,auto[3],auto[3]),word(0,auto[1],auto[3]))==(3,1,2,4)
mut=[list(row) for row in B]; mut[0][1]=1
assoc_failure=next(((i,j,k) for i,j,k in product(range(5),repeat=3) if mut[mut[i][j]][k]!=mut[i][mut[j][k]]),None)
assert assoc_failure is not None

coefficient=[]
for i in range(4):
    line=next(line for line in host.splitlines() if line.startswith('a='+str(i)+' '))
    row=tuple((int(a),int(b)) for a,b in re.findall(r'\((\d),(\d)\)',line))
    if len(row)!=3: raise RuntimeError('bad coefficient row')
    coefficient.append(row)
assert 'u_0=u_2=1' in host and 'u_1=3' in host and 'v_0=v_2=4' in host and 'v_1=0' in host
uvals=(1,3,1); vvals=(4,0,4)
def coef(t):
    i,a,l=t
    return coefficient[a][l] if a<4 else (uvals[i],vvals[l])
BB=tuple(product(range(5),repeat=2))
def mul2(x,y): return (bp(x[0],y[0]),bp(x[1],y[1]))
def swap(x): return (x[1],x[0])
def twist(w,x): return swap(x) if w else x
def bw(*xs):
    r=xs[0]
    for x in xs[1:]: r=mul2(r,x)
    return r
assert all(mul2(x,x)==x for x in BB)
assert all(mul2(mul2(x,y),z)==mul2(x,mul2(y,z)) for x,y,z in product(BB,repeat=3))
assert all(swap(swap(x))==x for x in BB)
assert all(swap(mul2(x,y))==mul2(swap(x),swap(y)) for x,y in product(BB,repeat=2))
corner25=[]
for h in BB:
    loc={mul2(mul2(h,x),h) for x in BB}
    assert all(bw(x,y,x,z,x)==bw(x,y,z,x) for x,y,z in product(loc,repeat=3))
    corner25.append(len(loc))
assert bw((1,1),(0,1),(1,1),(3,1),(1,1))==(2,1)
assert bw((1,1),(0,1),(3,1),(1,1))==(4,1)
assert len({(coef(x),q(x)) for x in S})==45
bad_identity=0
for i,j in product(range(n),repeat=2):
    x,y=S[i],S[j]; w=th(x[1])^qmat[x[2]][y[0]]
    assert coef(S[mult[i][j]])==mul2(coef(x),twist(w,coef(y)))
    if coef(S[mult[i][j]])!=mul2(coef(x),coef(y)): bad_identity+=1
assert (coef(e),coef(f))==((0,4),(0,2))
assert bad_identity==651
# Dual source actor and B^op, independently reverse the original table.
def dop(x): return (x[2],th(x[1]),x[0])
def dualcoef(x): return twist(th(x[1]),coef(x))
def dopmul(x,y): return (x[0],x[1]^qmat[y[0]][x[2]]^y[1],y[2])
assert len({(dualcoef(x),dop(x)) for x in S})==45
for i,j in product(range(n),repeat=2):
    x,y=S[i],S[j]; xy=S[mult[j][i]]; w=th(x[1])^qmat[y[2]][x[0]]
    assert dop(xy)==dopmul(dop(x),dop(y))
    assert dualcoef(xy)==mul2(twist(w,dualcoef(y)),dualcoef(x))
assert (dualcoef(e),dualcoef(f))==((4,0),(2,0))
assert st(f,e)==e and st(e,f)==f

# Nonabelian S3 gauge/transport checks, constructed independently of author programs.
G=tuple(permutations(range(3))); one=(0,1,2)
def gmul(x,y): return tuple(x[y[i]] for i in range(3))
def inv(x): return tuple(x.index(i) for i in range(3))
rot=(1,2,0); H=(one,rot,gmul(rot,rot))
swap01=(1,0,2); swap12=(0,2,1)
U=(one,swap01); V=(one,swap12)
Q=((one,one),(one,rot))
Pamb=tuple(tuple(gmul(gmul(inv(V[l]),Q[l][j]),inv(U[j])) for j in range(2)) for l in range(2))
T=tuple(product(range(2),H,range(2)))
def tprod(a,b): return (a[0],gmul(gmul(a[1],Q[a[2]][b[0]]),b[1]),b[2])
def incl(a): return (a[0],gmul(gmul(U[a[0]],a[1]),V[a[2]]),a[2])
def ambprod(a,b): return (a[0],gmul(gmul(a[1],Pamb[a[2]][b[0]]),b[1]),b[2])
images={incl(t) for t in T}
assert len(images)==12 and all(incl(tprod(a,b))==ambprod(incl(a),incl(b)) for a,b in product(T,repeat=2))
for i,l in product(range(2),repeat=2):
    cell={x for x in images if x[0]==i and x[2]==l}; p=Pamb[l][i]
    assert len(cell)==3 and (i,inv(p),l) in cell
    assert all(ambprod(a,b) in cell for a,b in product(cell,repeat=2))
    assert all((i,gmul(gmul(inv(p),inv(a[1])),inv(p)),l) in cell for a in cell)
GB=tuple(product(G,repeat=2))
def gmub(a,b): return (a[0],b[1])
def gact(g,c): return (gmul(g,c[0]),gmul(g,c[1]))
restriction_checks=0; no_restriction_gauge_fail=0
for x,y in product(T,repeat=2):
    ax,ay=incl(x),incl(y); weight=gmul(ax[1],Pamb[x[2]][y[0]])
    tw=gmul(x[1],Q[x[2]][y[0]])
    for c,d in product(GB,repeat=2):
        lhs=gact(inv(U[x[0]]),gmub(c,gact(weight,d)))
        rhs=gmub(gact(inv(U[x[0]]),c),gact(tw,gact(inv(U[y[0]]),d)))
        assert lhs==rhs
        no_restriction_gauge_fail+=gmub(c,gact(weight,d))!=gmub(c,gact(tw,d))
        restriction_checks+=1
assert no_restriction_gauge_fail>0

# Onto pure nonabelian actor: M[S3;2,2;v_l u_i] -> S3.
U2=(swap01,swap12); V2=(rot,swap01)
Q2=tuple(tuple(gmul(V2[l],U2[i]) for i in range(2)) for l in range(2))
D=tuple(product(range(2),G,range(2)))
def dprod(x,y): return (x[0],gmul(gmul(x[1],Q2[x[2]][y[0]]),y[1]),y[2])
def fm(x): return gmul(gmul(U2[x[0]],x[1]),V2[x[2]])
assert set(map(fm,D))==set(G)
assert all(fm(dprod(x,y))==gmul(fm(x),fm(y)) for x,y in product(D,repeat=2))
assert all((dprod(x,x)==x)==(fm(x)==one) for x in D)
assert all(len({fm(x) for x in D if x[0]==i and x[2]==l})==6 for i,l in product(range(2),repeat=2))
def push(c,x): return ((x[0],x[2]),gact(U2[x[0]],c),fm(x))
assert len({push(c,x) for c,x in product(GB,D)})==len(GB)*len(D)
push_checks=0; no_push_gauge_fail=0
for x,y in product(D,repeat=2):
    xy=dprod(x,y); sw=gmul(x[1],Q2[x[2]][y[0]])
    for c,d in product(GB,repeat=2):
        expect=push(gmub(c,gact(sw,d)),xy)
        px,py=push(c,x),push(d,y)
        got=((px[0][0],py[0][1]),gmub(px[1],gact(px[2],py[1])),gmul(px[2],py[2]))
        assert got==expect
        no_push_gauge_fail+=gmub(c,gact(fm(x),d))!=gmub(c,gact(sw,d))
        push_checks+=1
assert no_push_gauge_fail>0

out={
 'manifest_sha256':hashlib.sha256((ROOT/'manifest-v2.json').read_bytes()).hexdigest(),
 'input_sha256':hashes,
 'source':{'A_triples':125,'S_order':n,'S_associativity_triples':n**3,'S_idempotents':len(E),
   'source_regular':True,'weak_E_obstructions':weak_e_obstructions,'local_r_orthodox_corners':len(E),
   'local_corner_sizes':sorted(set(local_sizes)),'nonorthodox_witness':nonorth,'noninverse_local_witness':inverse_failure,
   'contexts_per_element':len(contexts)**2,'tau_classes':len(set(signatures)),
   'actor_q_classes':len(set(map(q,S))),'explicit_source_relations':True},
 'band5':{'associativity_triples':125,'local_corners':corners,'regular_global_failure':[2,4],
   'four_term':[u,v,ee,ff,bp(u,v),bp(v,u),bp(ee,ff),bp(ff,ee)],
   'upper_four':upper((x,u,v,y)),'upper_outputs':upper((ee,ff)),'automorphism':auto,
   'mutation_associativity_failure':assoc_failure},
 'host':{'band_order':len(BB),'band_associativity_triples':len(BB)**3,'regular_local_corners':len(corner25),
   'local_corner_sizes':sorted(set(corner25)),'actor_and_host_products':n*n,'host_image_size':len({(coef(x),q(x)) for x in S}),
   'e_f_coefficients':[coef(e),coef(f)],'identity_action_failed_products':bad_identity,
   'opposite_products':n*n,'opposite_image_size':len({(dualcoef(x),dop(x)) for x in S}),
   'opposite_e_f_coefficients':[dualcoef(e),dualcoef(f)]},
 'nonabelian_gauges':{'ambient_group':'S3','subgroup':'C3','finite_image_size':len(images),
   'occupied_cells':4,'cell_group_size':3,'restriction_product_checks':restriction_checks,
   'without_restriction_gauge_failures':no_restriction_gauge_fail,
   'push_actor_size':len(D),'push_band_size':len(GB),'push_source_host_size':len(D)*len(GB),
   'push_product_checks':push_checks,'without_push_gauge_failures':no_push_gauge_fail},
 'limit':'Finite computations do not replace universal proofs or independent-family review.'}
print(json.dumps(out,indent=2,sort_keys=True))
