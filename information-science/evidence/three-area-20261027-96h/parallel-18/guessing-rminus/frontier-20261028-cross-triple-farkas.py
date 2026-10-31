#!/usr/bin/env python3
"""Attempt one exact 13-variable multi-auxiliary cross-copy amalgam.

Fixes all pairwise marginals of (d'1,g'2,f'3) from the separately checked
star/pair systems; adds every 13-variable Shannon row and I(d'1,g'2;f'3|X)=0.
A fixed-marginal failure does not exclude alternative source-copy assignments.
"""
from array import array
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from math import lcm
from pathlib import Path
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
C12=('frontier-20261028-crossbranch12-exact-candidate.json','1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739')
C13=('frontier-20261028-crossbranch13-threefamilies-exact-candidate.json','e31643a10db9556bf8394d7b7d2a9cf1b20fa9380bf3da98b57bd2c655ca8474')
P1=('frontier-20261028-crossbranch23-round4-pair-1-1-candidate.json','c60246f6499aa7ff83ddd4b2c5dbd4aae35ae80137954efd96a21eed113d1b9b')
P2=('frontier-20261028-crossbranch23-round4-pair-3-1-candidate.json','59ed2e3479e7dafbbe42d54aaad7e58d1fcd489f0ea0fd37a88ce0d23fd716bb')
OUT=ROOT/'frontier-20261028-cross-triple-farkas-result.json'
CAND=ROOT/'frontier-20261028-cross-triple-farkas-candidate.json'
ORIGINAL=tuple('abcdefghij');AUX=("d'1","g'2","f'3");VARS=ORIGINAL+AUX
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
spec=spec_from_file_location('projection',ROOT/'frontier-20261028-exact-affine-reconstruction.py');projection=module_from_spec(spec);spec.loader.exec_module(projection)


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def main():
    base,c12,c13,p1,p2=map(pin,(BASE,C12,C13,P1,P2));index={v:i for i,v in enumerate(VARS)}
    def mask(labels):return sum(1<<index[v] for v in labels)
    known={0:Fraction(0)}
    for e in base['primal_values']:
        labs=e['entropy_variables']
        if set(labs)<=set(ORIGINAL):known[mask(labs)]=Fraction(e['value'])
    if len(known)!=1024:raise ValueError('BASE')
    # Singletons and the within-V pair are fixed by the star systems.
    for doc,allowed in ((c12,set(ORIGINAL)|set(AUX[:2])),(c13,set(ORIGINAL)|{AUX[2]})):
        for e in doc['auxiliary_values']:
            labs=e['entropy_variables']
            if set(labs)<=allowed and set(labs)&set(AUX):
                m=mask(labs)
                if m in known:raise ValueError('DUPLICATE_STAR')
                known[m]=Fraction(e['value'])
    # Cross-pair entropies come from separately verified 12-variable systems.
    for doc,required in ((p1,{AUX[0],AUX[2]}),(p2,{AUX[1],AUX[2]})):
        if set(doc['pair'])!=required:raise ValueError('PAIR')
        for e in doc['cross_values']:
            labs=e['entropy_variables']
            if not required<=set(labs) or not set(labs)<=set(ORIGINAL)|required:raise ValueError('PAIR_LABEL')
            m=mask(labs)
            if m in known:raise ValueError('DUPLICATE_PAIR')
            known[m]=Fraction(e['value'])
    if len(known)!=7168:raise ValueError(('KNOWN_SIZE',len(known)))
    scale=lcm(*(v.denominator for v in known.values()));fixed={m:int(v*scale) for m,v in known.items()}
    unknown=[m for m in range(1,8192) if m not in known];cols={m:i for i,m in enumerate(unknown)}
    if len(unknown)!=1024:raise ValueError('UNKNOWN_SIZE')
    starts=array('i');indices=array('i');coeff=array('d');lo=array('d');hi=array('d');lower=[];upper=[];rowmeta=[];known_only=0
    def add(terms,equality=False):
        nonlocal known_only
        constant=0;un={}
        for m,c in terms:
            if m in fixed:constant+=c*fixed[m]
            else:un[cols[m]]=un.get(cols[m],0)+c
        un={i:c for i,c in un.items() if c}
        if not un:
            known_only+=1
            if (equality and constant) or (not equality and constant<0):raise ValueError(('KNOWN_CONTRADICTION',terms,constant))
            return
        starts.append(len(indices))
        for i,c in un.items():indices.append(i);coeff.append(float(c))
        lower.append(-constant);upper.append(-constant if equality else None)
        rowmeta.append({'terms':terms,'equality':equality})
        lo.append(-constant/scale);hi.append(-constant/scale if equality else highspy.kHighsInf)
    full=8191
    for i in range(13):add(((full,1),(full^(1<<i),-1)))
    for i,j in combinations(range(13),2):
        a,b=1<<i,1<<j;z=full^a^b
        while True:
            add(((z|a,1),(z|b,1),(z|a|b,-1),(z,-1)))
            if not z:break
            z=(z-1)&(full^a^b)
    X=1023;A=(1<<10)|(1<<11);B=1<<12
    add(((X|A,1),(X|B,1),(X|A|B,-1),(X,-1)),equality=True)
    lp=highspy.HighsLp();lp.num_col_,lp.num_row_=len(unknown),len(starts)
    lp.col_cost_,lp.col_lower_,lp.col_upper_=np.zeros(len(unknown)),np.zeros(len(unknown)),np.full(len(unknown),13.)
    lp.row_lower_,lp.row_upper_=np.frombuffer(lo,dtype=np.float64),np.frombuffer(hi,dtype=np.float64)
    lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.append(np.frombuffer(starts,dtype=np.int32),np.int32(len(indices)))
    lp.a_matrix_.index_=np.frombuffer(indices,dtype=np.int32);lp.a_matrix_.value_=np.frombuffer(coeff,dtype=np.float64);lp.sense_=highspy.ObjSense.kMinimize
    solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('solver','simplex');solver.setOptionValue('time_limit',20.);solver.passModel(lp);solver.run()
    status=solver.modelStatusToString(solver.getModelStatus());result={'variables':VARS,'fixed_coordinates':7167,'unknown_coordinates':1024,
        'known_only_exact_checks':known_only,'status_float_unverified':status}
    if status=='Infeasible':
        ray_status,exists,ray=solver.getDualRay();result['ray_status']=str(ray_status);result['ray_exists']=bool(exists)
        if exists:
            trials=[]
            for den in (10,100,1000,10000,1000000):
                y=[Fraction(float(v)).limit_denominator(den) for v in ray];res=[Fraction(0)]*len(unknown);bound=Fraction(0);bad=[];selected=[]
                for i,w in enumerate(y):
                    if not w:continue
                    if upper[i] is None and w<0:bad.append(('wrong_row_sign',i,str(w)))
                    bound+=w*Fraction(lower[i],scale)
                    end=starts[i+1] if i+1<len(starts) else len(indices)
                    for j in range(starts[i],end):res[indices[j]]+=w*int(coeff[j])
                    selected.append({'row':i,'metadata':rowmeta[i],'ray_weight':str(w)})
                upperbox=sum((13*z for z in res if z>0),Fraction(0));gap=bound-upperbox
                trials.append({'max_denominator':den,'selected_rows':len(selected),'wrong_signs':bad,'strict_gap':str(gap),'exact_candidate':not bad and gap>0})
                if not bad and gap>0:
                    result['exact_farkas_candidate']={'weights':selected,'row_lower_bound':str(bound),'box_upper_bound':str(upperbox),'strict_gap':str(gap),
                        'positive_column_residuals':[[unknown[i],str(z)] for i,z in enumerate(res) if z>0],
                        'negative_column_residuals':[[unknown[i],str(z)] for i,z in enumerate(res) if z<0]}
                    break
            result['rationalization_attempts']=trials
    with CAND.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    result['base_sha256']=BASE[1];result['cross12_sha256']=C12[1];result['cross13_sha256']=C13[1];result['pair_hashes']=[P1[1],P2[1]]
    result['candidate_file']=CAND.name;result['candidate_sha256']=sha256(CAND.read_bytes()).hexdigest()
    result['limits']='Only one 13-variable system with fixed chosen pairwise auxiliary marginals; any exact ray needs independent verification, and no original-base or all-17-variable conclusion follows.'
    with OUT.open('x',encoding='utf-8') as stream:json.dump({k:v for k,v in result.items() if k!='cross_values'},stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cross_values'},indent=2))


if __name__=='__main__':main()
