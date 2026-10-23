"""Exact parent check of ROW-U weights and nonabelian LFC/INV mechanics; not a full Sun7 proof."""
import hashlib, itertools, json, math, os, resource, subprocess, sys, time
from fractions import Fraction as F
from pathlib import Path
OUT=Path(sys.argv[1]); begin=time.monotonic()
def guard():
    fs=os.statvfs(OUT.parent)
    if fs.f_bavail*fs.f_frsize<12000000000: raise RuntimeError('disk floor')
    if time.monotonic()-begin>60: raise RuntimeError('self-budget')
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>256*2**20: raise RuntimeError('RSS')
def subsets(n):
    for mask in range(1,1<<n): yield tuple(i for i in range(n) if mask>>i&1)
def allowed(a,T):
    for s in range(2,len(T)+1):
        for U in itertools.combinations(T,s):
            if max(math.gcd(a[i],a[j]) for i,j in itertools.combinations(U,2))<s: return False
    return True
def weights(a):
    k3=a.count(3); k5=a.count(5); b=a.count(4)
    y=[]
    for x in a:
        if x==1: z=F(1)
        elif x==3: z=F(1,min(3,k3))
        elif x==5: z=F(1,min(5,k5))
        elif b<=2: z=F(1,2) if x==2 else F(1,4)
        elif b==3: z=F(0) if x==2 else F(1,3)
        else: z=F(1,4)
        y.append(z)
    return y
rows={}
for n in (5,6):
    seen=violating=0; minimum=None
    for a in itertools.combinations_with_replacement(range(1,6),n):
        guard(); y=weights(a)
        for T in subsets(n):
            if allowed(a,T) and sum(y[i] for i in T)>1: raise RuntimeError(('infeasible',a,T,y))
        value=sum(F(x)*z for x,z in zip(a,y)); minimum=value if minimum is None else min(minimum,value)
        bad=any(x in a for x in (3,5)) or a.count(1)>1 or a.count(4)<3
        if n==6 and bad:
            violating+=1
            if value<6: raise RuntimeError(('row counterexample',a,value))
        if n==5 and value<4: raise RuntimeError(('five-neighbour counterexample',a,value))
        seen+=1
    rows[str(n)]={'multisets':seen,'all_weights_feasible':True,'global_minimum_value':str(minimum),'violating_ROW_U_conditions':violating}
a=(2,4,4,1,1,1); bady=[F(1,2),F(1,3),F(1,3),F(1),F(1),F(1)]; T=(0,1,2)
if not allowed(a,T) or sum(bady[i] for i in T)<=1: raise RuntimeError('Weight mutation did not fail as intended')
# S3 exact permutation group. Non-normal order-two subgroups are included.
G=tuple(itertools.permutations(range(3))); index={p:i for i,p in enumerate(G)}
mul=[[index[tuple(a[b[i]] for i in range(3))] for b in G] for a in G]
e=index[(0,1,2)]; inv=[next(j for j in range(6) if mul[i][j]==e and mul[j][i]==e) for i in range(6)]
subs=[]
for mask in range(1,64):
    U=frozenset(i for i in range(6) if mask>>i&1)
    if e in U and all(mul[x][y] in U for x in U for y in U): subs.append(U)
cosets=[]
for U in subs:
    seen=set()
    for g in range(6):
        C=frozenset(mul[g][u] for u in U)
        if C not in seen: seen.add(C); cosets.append((g,U,C))
checks=0; configurations=0; wrong_inverse_counterexample=None
for k in range(2,7):
    for family in itertools.combinations(cosets,k):
        guard()
        if any(A[2]&B[2] for A,B in itertools.combinations(family,2)): continue
        configurations+=1
        for g,U,C in family:
            n=6//len(U); fibres={frozenset(mul[x][u] for u in U) for x in range(6)}
            for h,V,D in family:
                if C==D: continue
                nj=6//len(V); gcd=math.gcd(n,nj); I=6//len(U&V); alpha=F(I,math.lcm(n,nj))
                meets=[Fibre for Fibre in fibres if Fibre&D]
                if len(meets)!=len(V)//len(U&V) or any(Fibre==C for Fibre in meets): raise RuntimeError('left-fibre incidence')
                for Fibre in meets:
                    if len(Fibre&D)!=len(U&V): raise RuntimeError('fibre intersection size')
                Ustar={mul[mul[g][u]][inv[g]] for u in U}; Vstar={mul[mul[h][v]][inv[h]] for v in V}
                astar=F(6//len(Ustar&Vstar),math.lcm(n,nj))
                relative=mul[inv[g]][h]
                dbl={mul[mul[u][relative]][v] for u in U for v in V}
                product={mul[u][v] for u in U for v in V}
                q=F(len(dbl)*gcd,6)
                if q!=astar or dbl&product or alpha+astar>gcd: raise RuntimeError('INV/nonabelian double-coset check')
                if wrong_inverse_counterexample is None and alpha!=astar:
                    wrong_inverse_counterexample={'g':G[g],'h':G[h],'U':[G[u] for u in sorted(U)],'V':[G[v] for v in sorted(V)],'alpha':str(alpha),'alpha_star':str(astar),'gcd':gcd,'wrong_rule':'Replacing conjugated inverse subgroup by original subgroup incorrectly identifies alpha_star with alpha'}
                checks+=1
if wrong_inverse_counterexample is None: raise RuntimeError('No intended conjugation mutation counterexample')
result={'at':subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z'],text=True).strip(),'status':'PASS','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'row_multisets':rows,'weight_mutation':{'allowed_subset':T,'sum':str(sum(bady[i] for i in T)),'rejected':'feasibility exceeds1'},'S3':{'subgroups':len(subs),'cosets':len(cosets),'disjoint_configurations':configurations,'directed_pair_checks':checks,'conjugation_mutation_counterexample':wrong_inverse_counterexample},'seconds':time.monotonic()-begin,'scope':'Finite exact arithmetic and S3 mechanics controls, not a proof over arbitrary groups or the fullSun7 target'}
with OUT.open('x') as f: json.dump(result,f,indent=2); f.write('\n')
print(json.dumps(result,indent=2))
