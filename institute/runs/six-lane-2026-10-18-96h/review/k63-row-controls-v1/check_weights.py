"""Exact controls for K63-RES's explicit row weights; not a group theorem."""
import hashlib, itertools, json, math, os, subprocess, sys, time
from fractions import Fraction as F
from pathlib import Path
START=time.monotonic()
def allowed_sets(types):
    allowed=[False]*64; allowed[0]=True
    gcds={(a,b):math.gcd(types[a],types[b]) for a in range(6) for b in range(a+1,6)}
    for mask in range(1,64):
        inds=[i for i in range(6) if mask>>i&1]
        allowed[mask]=(len(inds)==1 or (max(gcds[a,b] for a in inds for b in inds if a<b)>=len(inds) and all(allowed[mask^(1<<i)] for i in inds)))
    return [mask for mask in range(1,64) if allowed[mask]]
def standard(y,indices,x):
    fours=[i for i in indices if x[i]==4]
    for i in indices:
        y[i]=F(1) if x[i]==1 else (F(1,2) if x[i]==2 else F(1,4))
    if len(fours)>=3:
        for i in indices:
            if x[i]==4: y[i]=F(1,len(fours))
            elif x[i]==2: y[i]=F(0)
def certificate(x,xs,E,marker):
    ty=[x[i]*(5 if marker==i else 1) for i in range(4)]+[2**E*xs*(5 if marker==4 else 1),3*(5 if marker==5 else 1)]
    masks=allowed_sets(ty); y=[F(0)]*6
    ts=[i for i in range(4) if x[i]==3]; fs=[i for i in range(4) if x[i]==5]
    if fs:
        if marker!=5:
            for i in fs:y[i]=F(1,len(fs))
            y[5]=F(1); case='1a'
        elif len(fs)<4:
            for i in fs:y[i]=F(1,len(fs))
            y[next(i for i in range(4) if i not in fs)]=F(1); case='1b'
        else:
            for i in range(4):y[i]=F(1,5)
            y[5]=F(1,5); y[4]=F(1,5) if xs==5 else F(4,5); case='1c'
    elif len(ts)==4:
        for i in ts+[5]:y[i]=F(1,3)
        if xs==3:y[4]=F(1,3)
        else:y[4]=F(2,3) if any(math.gcd(ty[4],ty[i])>=2 for i in ts+[5]) else F(1)
        case='2'
    elif len(ts)==3:
        z=next(i for i in range(4) if i not in ts)
        for i in ts+[5]:y[i]=F(1,3)
        if xs==3:
            y[4]=F(1,3);y[z]=F(1) if x[z]==1 else F(2,3);case='3a'
        elif any(math.gcd(ty[4],ty[i])>=2 for i in ts+[5]):
            y[4]=F(2,3);case='3b-q'
        else:
            y[4]=y[z]=F(1,2) if math.gcd(ty[4],ty[z])>=2 else F(1);case='3b-noq'
    elif len(ts)==2:
        zs=[i for i in range(4) if i not in ts]; a,b=zs
        for i in ts:y[i]=F(1,2)
        if sorted([x[a],x[b]]) not in ([1,1],[2,2]):
            if x[a]%2==0 and x[b]%2==0:y[max(zs,key=lambda i:x[i])]=F(1)
            else:y[a]=y[b]=F(1)
            case='4-basic'
        elif x[a]==1:
            y[a]=y[b]=F(1)
            if xs==3:
                for i in ts+[4,5]:y[i]=F(1,3)
            elif xs!=5:y[4]=F(1)
            elif marker in ts:y[4]=F(1,2)
            elif marker in zs:y[marker]=F(0);y[4]=F(1)
            else:y[4]=F(1)
            case='4a'
        else:
            for i in ts+[5]:y[i]=F(1,3)
            y[a]=y[b]=F(1,2)
            if xs==3:y[4]=F(1,3)
            elif ((1<<a)|(1<<b)|(1<<4)) not in masks:y[4]=F(1,2)
            else:y[a]=y[b]=F(0);y[4]=F(1)
            case='4b'
    elif len(ts)==1:
        y[ts[0]]=F(1);standard(y,[i for i in range(4) if i not in ts],x);case='5'
    else:
        y[5]=F(1);standard(y,list(range(4)),x);case='6'
    return ty,masks,y,case

def violations(masks,y):
    return [mask for mask in masks if sum((y[i] for i in range(6) if mask>>i&1),F(0))>1]

def main():
    out=Path(sys.argv[1]); counts={}; minima={}; rows=0
    # Explicit positive and intended-reason corruption controls.
    ty,masks,y,_=certificate((3,3,3,3),3,1,-1)
    val=sum((y[i]*3 for i in range(5)),F(0))+2*y[5]
    if violations(masks,y) or val!=F(17,3):raise ValueError('positive all-three certificate')
    bad=list(y);bad[0]=F(1)
    if not violations(masks,bad):raise ValueError('infeasible-weight control not rejected')
    if not (val>5 and val<6):raise ValueError('strengthened-bound control')
    for x,xs,E,marker in itertools.product(itertools.product(range(1,6),repeat=4),range(1,6),(1,2),range(-1,6)):
        if rows%128==0 and time.monotonic()-START>250:
            status='INCOMPLETE_BUDGET';break
        ty,masks,y,case=certificate(x,xs,E,marker)
        val=sum((y[i]*x[i] for i in range(4)),F(0))+y[4]*xs+2*y[5]
        bad=violations(masks,y)
        if min(y)<0 or val<=5 or bad:raise ValueError(repr({'row':x,'xs':xs,'E':E,'marker':marker,'types':ty,'weights':list(map(str,y)),'value':str(val),'violating_masks':bad,'case':case}))
        counts[case]=counts.get(case,0)+1;minima[case]=min(minima.get(case,val),val);rows+=1
    else:status='COMPLETE_ALL_EXPLICIT_CERTIFICATES_VALID'
    record={'at':subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z'],text=True).strip(),'status':status,'rows':rows,'counts':counts,'minima':{k:str(v) for k,v in minima.items()},'controls':{'all_three_value':str(F(17,3)),'infeasible_weight_rejected':True,'old_bound_does_not_exclude_control':True},'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'wall_s':time.monotonic()-START,'scope':'Explicit row-weight arithmetic on capped gcd types only. Not a group proof, independent proof assistant, or novelty evidence.'}
    data=json.dumps(record,indent=2)+'\n'
    if len(data.encode())>1048576:raise ValueError('output cap')
    with out.open('x') as f:f.write(data)
    print(json.dumps(record),flush=True)
    return 0 if rows==43750 and status.startswith('COMPLETE') else 2
if __name__=='__main__':raise SystemExit(main())
