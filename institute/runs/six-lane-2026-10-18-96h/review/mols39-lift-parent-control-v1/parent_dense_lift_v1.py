#!/usr/bin/env python3
"""Parent independent dense-GF(3) lift enumeration, exact anchor only; no worker imports."""
import hashlib,itertools,json,subprocess,sys,time
from pathlib import Path
START=time.monotonic()
DEADLINE=START+120

def guard():
    if time.monotonic()>DEADLINE: raise RuntimeError('SELF_BUDGET_EXCEEDED')

def date():
    return subprocess.run(['/bin/date','+%Y-%m-%dT%H:%M:%S%z'],check=True,capture_output=True,text=True).stdout.strip()

def fingerprint(A):
    return hashlib.sha256('\n'.join(' '.join(map(str,row)) for row in A).encode('ascii')).hexdigest()

def dm_check(D,n):
    if len(D)<2 or any(len(row)!=n or any(not 0<=v<n for v in row) for row in D): raise ValueError('BAD_MATRIX')
    universe=set(range(n))
    for a,b in itertools.combinations(range(len(D)),2):
        if {(x-y)%n for x,y in zip(D[a],D[b])}!=universe: raise ValueError('NOT_DM')

def structures(D,n):
    dm_check(D,n)
    if n%3 or (n//3)%3==0: raise ValueError('BAD_ORDER')
    q=n//3; k=len(D)
    E=[[(D[a][c]-D[0][c])%n for c in range(n)] for a in range(k)]
    fibres=[]
    for a,b in itertools.combinations(range(k),2):
        for t in range(q):
            cells=[c for c in range(n) if (E[a][c]-E[b][c])%q==t]
            if len(cells)!=3: raise ValueError('BAD_FIBRE_SIZE')
            fibres.append((a,b,cells))
    return E,fibres

def rainbow(A,fibres):
    return all({(A[a][c]-A[b][c])%3 for c in cells}=={0,1,2} for a,b,cells in fibres)

def count(D,n):
    guard(); E,fibres=structures(D,n); k=len(D)
    cells=[(a,c) for a in range(1,k) for c in range(1,n)]
    indexes={ac:j for j,ac in enumerate(cells)}; nv=len(cells)
    equations=[]
    for a,b,cols in fibres:
        row=[0]*nv
        for c in cols:
            if a and c: row[indexes[(a,c)]]=(row[indexes[(a,c)]]+1)%3
            if b and c: row[indexes[(b,c)]]=(row[indexes[(b,c)]]-1)%3
        equations.append(row)
    # Full dense reduced row echelon form; independent of the workers' sparse propagator.
    rank=0; pivots=[]
    for col in range(nv):
        guard()
        candidates=[j for j in range(rank,len(equations)) if equations[j][col]]
        if not candidates: continue
        chosen=candidates[0]; equations[rank],equations[chosen]=equations[chosen],equations[rank]
        inv=1 if equations[rank][col]==1 else 2
        equations[rank]=[(x*inv)%3 for x in equations[rank]]
        pivot=equations[rank]
        for j in range(len(equations)):
            if j!=rank and equations[j][col]:
                scale=equations[j][col]
                equations[j]=[(x-scale*y)%3 for x,y in zip(equations[j],pivot)]
        pivots.append(col); rank+=1
    free=[c for c in range(nv) if c not in set(pivots)]
    if len(free)>6: raise ValueError('ENUMERATION_SCOPE_EXCEEDED')
    accepted=[]; visits=0
    for coeff in itertools.product(range(3),repeat=len(free)):
        guard(); visits+=1; vec=[0]*nv
        for c,v in zip(free,coeff): vec[c]=v
        for j,p in enumerate(pivots): vec[p]=(-sum(equations[j][c]*v for c,v in zip(free,coeff)))%3
        A=[[0]*n for _ in range(k)]
        for (a,c),v in zip(cells,vec): A[a][c]=v
        if rainbow(A,fibres): accepted.append(A)
    T=[[(row[c]-row[0])%3 for c in range(n)] for row in E]
    neg=[[(-v)%3 for v in row] for row in T]
    expected={fingerprint(T),fingerprint(neg)}
    actual={fingerprint(A) for A in accepted}
    if len(actual)!=len(accepted): raise ValueError('DUPLICATE_NORMALIZED_SOLUTION')
    return {'n':n,'k':k,'gauged_variables':nv,'rank':rank,'dimension':len(free),'enumerated_vectors':visits,'N_classes':len(accepted),'N_total':len(accepted)*3**(k-1),'rep_sha256':sorted(actual),'exactly_signed_anchor':actual==expected,'representatives':accepted},T,fibres

def main():
    inp=Path(sys.argv[1]); expected=sys.argv[2]; out=Path(sys.argv[3]); data=inp.read_bytes()
    if hashlib.sha256(data).hexdigest()!=expected: raise ValueError('INPUT_PIN_MISMATCH')
    D=[[int(v) for v in ln.split()] for ln in data.decode('ascii').splitlines() if ln.strip()]
    if len(D)!=6 or any(len(r)!=39 for r in D): raise ValueError('WRONG_ANCHOR_DIMENSIONS')
    positive,_,_=count([[0,0,0],[0,1,2]],3)
    if positive['N_classes']!=2 or positive['N_total']!=6 or not positive['exactly_signed_anchor']: raise ValueError('POSITIVE_CONTROL_FAILED')
    bad=[row[:] for row in D]; bad[1][1]=(bad[1][1]+1)%39
    try: structures(bad,39)
    except ValueError as ex:
        if str(ex)!='NOT_DM': raise
        mutation_dm='NOT_DM'
    else: raise ValueError('DM_MUTATION_ACCEPTED')
    result,T,fibres=count(D,39)
    corrupt=[row[:] for row in T]; corrupt[1][1]=(corrupt[1][1]+1)%3
    if rainbow(corrupt,fibres): raise ValueError('RAINBOW_MUTATION_ACCEPTED')
    if result['N_classes']!=2 or result['N_total']!=486 or result['dimension']!=5 or not result['exactly_signed_anchor']: raise ValueError('ANCHOR_COUNT_DISAGREES')
    record={'at':date(),'status':'PASS_EXACT_ANCHOR_CONTROL','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':expected,'positive_DM3':positive,'mutation_DM':mutation_dm,'mutation_lift':'REJECTED_RAINBOW','anchor':result,'elapsed_seconds':time.monotonic()-START,'scope':'One fixed mod13 skeleton, gauge-normalized mod3 lifts only. No seven-row DM or six MOLS39 result.'}
    with out.open('x') as f: json.dump(record,f,indent=2); f.write('\n')
    print(json.dumps({'status':record['status'],'rank':result['rank'],'classes':result['N_classes'],'vectors':result['enumerated_vectors'],'elapsed_seconds':record['elapsed_seconds']}))

if __name__=='__main__': main()
