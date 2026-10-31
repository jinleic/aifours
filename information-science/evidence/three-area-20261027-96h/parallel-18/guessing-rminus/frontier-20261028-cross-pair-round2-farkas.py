#!/usr/bin/env python3
"""Propose an exact Farkas obstruction for one fixed cross-branch pair.

The pair marginals are fixed from separately checked star primals. A negative
result excludes only these marginals, not other copies of the original law.
HiGHS proposes a dual ray; every reported positive gap is checked as Fraction.
"""
from array import array
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import lcm
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
C12=('frontier-20261028-crossbranch12-exact-candidate.json','1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739')
C13=('frontier-20261028-crossbranch13-all-cuts-exact-candidate.json','1d7263364c8c543bdd07a4b140c7a7ab2d65753c38506f26c02072fc9bd29703')
OUTPUT=ROOT/'frontier-20261028-cross-pair-round2-farkas-result.json'
ORIGINAL=tuple('abcdefghij');PAIR=("d'1","g'3")
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def main():
    start=monotonic();base,c12,c13=map(pin,(BASE,C12,C13));variables=ORIGINAL+PAIR;idx={v:i for i,v in enumerate(variables)}
    def mask(labels):return sum(1<<idx[v] for v in labels)
    known={0:Fraction(0)}
    for e in base['primal_values']:
        labs=e['entropy_variables']
        if set(labs)<=set(ORIGINAL):known[mask(labs)]=Fraction(e['value'])
    for doc,sym in ((c12,PAIR[0]),(c13,PAIR[1])):
        for e in doc['auxiliary_values']:
            labs=e['entropy_variables']
            if sym in labs and set(labs)<=set(ORIGINAL)|{sym}:known[mask(labs)]=Fraction(e['value'])
    if len(known)!=3072:raise ValueError('MARGINAL_SIZE')
    scale=lcm(*(v.denominator for v in known.values()));fixed={m:int(v*scale) for m,v in known.items()}
    unknown=[m for m in range(1,4096) if m not in known];cols={m:i for i,m in enumerate(unknown)}
    starts=array('i');indices=array('i');coeff=array('d');lo=array('d');hi=array('d');meta=[];low_int=[];upper_int=[]
    def add(terms,kind,equality=False):
        constant=0;un={}
        for m,c in terms:
            if m in fixed:constant+=c*fixed[m]
            else:un[cols[m]]=un.get(cols[m],0)+c
        un={i:c for i,c in un.items() if c}
        if not un:
            if (equality and constant) or (not equality and constant<0):raise ValueError(('KNOWN_INFEASIBLE',kind,constant))
            return
        starts.append(len(indices))
        for i,c in un.items():indices.append(i);coeff.append(float(c))
        lo.append(-constant/scale);hi.append(-constant/scale if equality else highspy.kHighsInf)
        low_int.append(-constant);upper_int.append(-constant if equality else None)
        meta.append({'kind':kind,'terms':terms,'equality':equality})
    full=4095
    for i in range(12):add(((full,1),(full^(1<<i),-1)),{'kind':'Hconditional','i':i})
    for i,j in combinations(range(12),2):
        a,b=1<<i,1<<j;z=full^a^b
        while True:
            add(((z|a,1),(z|b,1),(z|a|b,-1),(z,-1)),{'kind':'CMI','i':i,'j':j,'z':z})
            if not z:break
            z=(z-1)&(full^a^b)
    X=1023;a,b=1024,2048
    add(((X|a,1),(X|b,1),(X|a|b,-1),(X,-1)),{'kind':'conditional_independence'},True)
    lp=highspy.HighsLp();lp.num_col_,lp.num_row_=len(unknown),len(starts)
    lp.col_cost_,lp.col_lower_,lp.col_upper_=np.zeros(len(unknown)),np.zeros(len(unknown)),np.full(len(unknown),12.)
    lp.row_lower_,lp.row_upper_=np.frombuffer(lo,dtype=np.float64),np.frombuffer(hi,dtype=np.float64)
    lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.append(np.frombuffer(starts,dtype=np.int32),np.int32(len(indices)))
    lp.a_matrix_.index_=np.frombuffer(indices,dtype=np.int32);lp.a_matrix_.value_=np.frombuffer(coeff,dtype=np.float64)
    lp.sense_=highspy.ObjSense.kMinimize
    solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('solver','simplex');solver.setOptionValue('time_limit',20.)
    solver.passModel(lp);solver.run();status=solver.modelStatusToString(solver.getModelStatus())
    result={'pair':PAIR,'base_sha256':BASE[1],'cross12_sha256':C12[1],'cross13_sha256':C13[1],
            'status_float_unverified':status,'solver_rows':len(starts),'scale':str(scale)}
    if status=='Infeasible':
        ray_status,exists,ray=solver.getDualRay();result['ray_status']=str(ray_status);result['ray_exists']=bool(exists)
        if exists:
            candidates=[]
            for den in (10,100,1000,10000,1000000):
                y=[Fraction(float(v)).limit_denominator(den) for v in ray];res=[Fraction(0)]*len(unknown);bound=Fraction(0);bad=[];selected=[]
                for i,w in enumerate(y):
                    if not w:continue
                    if upper_int[i] is None and w<0:bad.append(('wrong_row_sign',i,str(w)))
                    bound+=w*Fraction(low_int[i],scale)
                    end=starts[i+1] if i+1<len(starts) else len(indices)
                    for j in range(starts[i],end):res[indices[j]]+=w*int(coeff[j])
                    selected.append({'row':i,'metadata':meta[i],'ray_weight':str(w)})
                # x is a joint entropy and 0 <= x <= 12 for every unknown coordinate.
                variable_max=sum((12*z for z in res if z>0),Fraction(0));gap=bound-variable_max
                entry={'max_denominator':den,'selected_rows':len(selected),'wrong_signs':bad,
                       'row_lower_bound':str(bound),'box_upper_bound':str(variable_max),'strict_gap':str(gap),
                       'exact_farkas_candidate':not bad and gap>0}
                candidates.append(entry)
                if not bad and gap>0:
                    result['exact_farkas_candidate']={'weights':selected,'row_lower_bound':str(bound),
                        'box_upper_bound':str(variable_max),'strict_gap':str(gap),
                        'positive_column_residuals':[[unknown[i],str(z)] for i,z in enumerate(res) if z>0],
                        'negative_column_residuals':[[unknown[i],str(z)] for i,z in enumerate(res) if z<0]}
                    break
            result['rationalization_attempts']=candidates
    result['elapsed_seconds']=monotonic()-start
    result['limits']='Any exact ray needs an independent row/graph/sign/box-bound check and excludes only these fixed auxiliary marginals, not the original profile with alternative copies.'
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='exact_farkas_candidate'},indent=2))
    if 'exact_farkas_candidate' in result:print('EXACT FARKAS CANDIDATE: independent verification required')


if __name__=='__main__':main()
