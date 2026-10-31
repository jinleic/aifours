#!/usr/bin/env python3
"""Propose rational fractional reconstruction-cover certificates on 41 planes."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
SRC=('frontier-20261028-three-syndrome-fourfactor-color-screen-result.json','218c42798aa317236225f99e5b03f2cd6bd87c21cbaeb606ebdb54b53d1ac7a8')
OUT=ROOT/'frontier-20261028-fourfactor-plane-fractional-certificates-v1.json'
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy


def main():
    raw=(ROOT/SRC[0]).read_bytes()
    if sha256(raw).hexdigest()!=SRC[1]:raise ValueError('HASH')
    source=json.loads(raw);result=[]
    for row in source['cases']:
        if row['color'] is not None:continue
        allowed=row['allowed_masks'];safe=[I for I in range(1,1024) if not any(D&I==D for D in allowed)]
        starts=[];index=[];value=[]
        for I in safe:
            starts.append(len(index))
            for v in range(10):
                if I>>v&1:index.append(v);value.append(1.)
        lp=highspy.HighsLp();lp.num_col_=len(safe);lp.num_row_=10;lp.col_cost_=np.ones(len(safe))
        lp.col_lower_=np.zeros(len(safe));lp.col_upper_=np.full(len(safe),highspy.kHighsInf)
        lp.row_lower_=np.ones(10);lp.row_upper_=np.full(10,highspy.kHighsInf);lp.sense_=highspy.ObjSense.kMinimize
        lp.a_matrix_.format_=highspy.MatrixFormat.kColwise;lp.a_matrix_.start_=np.array(starts+[len(index)],dtype=np.int32)
        lp.a_matrix_.index_=np.array(index,dtype=np.int32);lp.a_matrix_.value_=np.array(value)
        h=highspy.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',2.);h.passModel(lp);h.run()
        if h.modelStatusToString(h.getModelStatus())!='Optimal':raise ValueError('SOLVER')
        sol=h.getSolution();primal=[(I,Fraction(x).limit_denominator(10000)) for I,x in zip(safe,sol.col_value) if x>1e-9];dual=[Fraction(x).limit_denominator(10000) for x in sol.row_dual]
        p=sum(w for _,w in primal);d=sum(dual)
        if p!=d or any(x<0 for x in dual) or any(sum(w for I,w in primal if I>>v&1)<1 for v in range(10)) or any(sum(dual[v] for v in range(10) if I>>v&1)>1 for I in safe):raise ValueError('RATIONAL_CHECK')
        result.append({'factors':row['factors'],'syndrome_plane':row['syndrome_plane'],'objective':str(d),'primal':[[I,str(w)] for I,w in primal],'dual':[str(x) for x in dual]})
    if len(result)!=41:raise ValueError('COUNT')
    with OUT.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'cases':len(result),'objectives':{str(q):sum(c['objective']==str(q) for c in result) for q in sorted({Fraction(c['objective']) for c in result})}},indent=2))


if __name__=='__main__':main()
