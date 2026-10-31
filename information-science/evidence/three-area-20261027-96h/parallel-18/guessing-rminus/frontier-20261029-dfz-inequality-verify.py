#!/usr/bin/env python3
"""Independently re-derive published DFZ inequalities from their copy steps.

Usage: python3 script.py OUT.json "a b c d e f g h i|copy steps" [...]
For each inequality
  a I(A;B) <= b I(A;B|C)+c I(A;C|B)+d I(B;C|A)+e I(A;B|D)+f I(A;D|B)+g I(B;D|A)+h I(C;D)+i I(C;D|A)
and its listed copy steps (DFZ notation 'xy uv pq.' = (X,Y) is a copy of (U,V)
over (P,Q), conditionally independent of every previously existing variable
given (P,Q); a parenthesized item such as (cr) is one joint item), the script
builds every elemental Shannon inequality on the enlarged variable set, every
copy marginal equality H(U,new_Q)=H(U,old_Q) for U a subset of the over-set and
Q a nonempty subset of the copied items, and the conditional independence
equality. A floating basic dual is found by simplex; multipliers are then
solved EXACTLY over Q (Fraction Gaussian elimination on the basic support),
signs are checked (elemental multipliers >= 0), and the coefficient identity
  RHS-LHS = sum(lambda_i * elemental_i) + sum(mu_j * copy_equality_j)
is verified on every joint-entropy coordinate. Only exact identities count.
"""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy

def parse_steps(text):
    steps=[]
    for part in [p.strip() for p in text.split('.') if p.strip()]:
        new,old,over=part.split()
        items=[];i=0
        while i<len(old):
            if old[i]=='(':
                j=old.index(')',i);items.append(old[i+1:j]);i=j+1
            else:items.append(old[i]);i+=1
        if len(items)!=len(new):raise ValueError('STEP_ARITY')
        steps.append((list(new),items,over))
    return steps

def target(coef,idx):
    a,b,c,d,e,f,g,h,i=coef;A,B,C,D=(1<<idx[x] for x in 'abcd')
    def I(x,y,z=0):return [(x|z,1),(y|z,1),(x|y|z,-1),(z,-1)]
    out={}
    for w,t in [(-a,I(A,B)),(b,I(A,B,C)),(c,I(A,C,B)),(d,I(B,C,A)),(e,I(A,B,D)),(f,I(A,D,B)),(g,I(B,D,A)),(h,I(C,D)),(i,I(C,D,A))]:
        for m,x in t:
            if m:out[m]=out.get(m,0)+w*x
    return {m:Fraction(x) for m,x in out.items() if x}

def build(coef,steps):
    idx={x:k for k,x in enumerate('abcd')}
    for new,items,over in steps:
        for x in new:
            if x in idx:raise ValueError('NAME_REUSE')
            idx[x]=len(idx)
    n=len(idx);full=(1<<n)-1;rows=[];eqs=[]
    def mask(s):return sum(1<<idx[x] for x in s)
    for i in range(n):rows.append(({full:1,full^(1<<i):-1},['mono',i]))
    for i,j in combinations(range(n),2):
        rest=full^(1<<i)^(1<<j);z=rest
        while True:
            t={z|1<<i:1,z|1<<j:1,z|1<<i|1<<j:-1}
            if z:t[z]=-1
            rows.append((t,['cmi',i,j,z]))
            if not z:break
            z=(z-1)&rest
    existing=set('abcd')
    for new,items,over in steps:
        if not set(over)<=existing or not all(set(it)<=existing for it in items):raise ValueError('UNDEFINED_VARIABLE')
        Y=mask(over)
        for qbits in range(1,1<<len(new)):
            nm=sum(1<<idx[new[q]] for q in range(len(new)) if qbits>>q&1)
            om=0
            for q in range(len(new)):
                if qbits>>q&1:om|=mask(items[q])
            U=Y
            while True:
                t={}
                for m,x in ((U|nm,1),(U|om,-1)):t[m]=t.get(m,0)+x
                t={m:x for m,x in t.items() if m and x}
                if t:eqs.append((t,['copy',''.join(new),qbits,U]))
                if not U:break
                U=(U-1)&Y
        E=mask(existing);N=mask(new);t={}
        for m,x in ((E|N,1),(Y,1),(E,-1),(Y|N,-1)):
            if m:t[m]=t.get(m,0)+x
        eqs.append(({m:x for m,x in t.items() if x},['independence',''.join(new),over]))
        existing|=set(new)
    return n,idx,target(coef,idx),rows,eqs

def exact_solve(cols,F,ncoord):
    # Solve sum_k w_k cols[k] = F exactly; cols are dicts mask->int. Returns list of Fractions or None.
    k=len(cols);M=[[Fraction(cols[j].get(m,0)) for j in range(k)]+[F.get(m,Fraction(0))] for m in range(1,ncoord+1)]
    piv=[];r=0
    for c in range(k):
        p=next((i for i in range(r,len(M)) if M[i][c]!=0),None)
        if p is None:continue
        M[r],M[p]=M[p],M[r];inv=1/M[r][c];M[r]=[x*inv for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                f=M[i][c];M[i]=[a-f*b for a,b in zip(M[i],M[r])]
        piv.append(c);r+=1
    if any(M[i][k]!=0 for i in range(r,len(M))):return None
    w=[Fraction(0)]*k
    for i,c in enumerate(piv):w[c]=M[i][k]
    return w

def certify(coef,stepstext):
    steps=parse_steps(stepstext);n,idx,F,rows,eqs=build(coef,steps);ncoord=(1<<n)-1
    allrows=rows+eqs;nin=len(rows)
    starts=[];index=[];value=[]
    for t,meta in allrows:
        starts.append(len(index))
        for m,x in sorted(t.items()):index.append(m-1);value.append(float(x))
    lp=highspy.HighsLp();lp.num_col_=len(allrows);lp.num_row_=ncoord
    lp.col_cost_=np.array([1.0]*nin+[0.0]*len(eqs));lp.col_lower_=np.array([0.0]*nin+[-highspy.kHighsInf]*len(eqs))
    lp.col_upper_=np.full(len(allrows),highspy.kHighsInf)
    rhs=np.zeros(ncoord)
    for m,x in F.items():rhs[m-1]=float(x)
    lp.row_lower_=rhs;lp.row_upper_=rhs.copy();lp.a_matrix_.format_=highspy.MatrixFormat.kColwise
    lp.a_matrix_.start_=np.array(starts+[len(index)],dtype=np.int32);lp.a_matrix_.index_=np.array(index,dtype=np.int32)
    lp.a_matrix_.value_=np.array(value,dtype=float)
    h=highspy.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('solver','simplex')
    h.passModel(lp);h.run();status=h.modelStatusToString(h.getModelStatus())
    if status!='Optimal':return {'status':status,'valid_exact':False}
    sol=np.array(h.getSolution().col_value);support=[k for k in range(len(allrows)) if abs(sol[k])>1e-9]
    w=exact_solve([allrows[k][0] for k in support],F,ncoord)
    if w is None:return {'status':status,'valid_exact':False,'reason':'EXACT_INCONSISTENT'}
    acc={}
    for kk,k in enumerate(support):
        if k<nin and w[kk]<0:return {'status':status,'valid_exact':False,'reason':'NEGATIVE_ELEMENTAL'}
        for m,x in allrows[k][0].items():acc[m]=acc.get(m,Fraction(0))+w[kk]*x
    acc={m:x for m,x in acc.items() if x}
    ok=acc==F
    return {'status':status,'valid_exact':ok,'variables':n,'elemental_rows':nin,'copy_equalities':len(eqs),
            'support':len(support),'elemental_used':sum(1 for kk,k in enumerate(support) if k<nin and w[kk]!=0),
            'multipliers':[{'row':allrows[k][1],'kind':'elemental' if k<nin else 'copy','value':str(w[kk])} for kk,k in enumerate(support) if w[kk]!=0]}

def main():
    out=ROOT/sys.argv[1];res=[]
    for spec in sys.argv[2:]:
        nums,steps=spec.split('|');coef=tuple(int(x) for x in nums.split())
        r=certify(coef,steps);r.update({'coefficients':list(coef),'copy_steps':steps});res.append(r)
        print(coef,steps,r['status'],r['valid_exact'],r.get('support'),flush=True)
    # negative control: strengthen the first inequality's LHS by one unit; must fail
    nums,steps=sys.argv[2].split('|');coef=list(int(x) for x in nums.split());coef[0]+=1
    ctl=certify(tuple(coef),steps);ctl_ok=not ctl['valid_exact']
    with open(out,'x',encoding='utf-8') as f:
        json.dump({'results':res,'all_valid':all(r['valid_exact'] for r in res),'negative_control_strengthened_lhs_rejected':ctl_ok,
                   'limits':'Exact Shannon-plus-copy-lemma certificate for each listed inequality; the copy lemma itself (DFZ Lemma, proved there) is the only imported fact.'},f,indent=1);f.write('\n')
    print('all_valid',all(r['valid_exact'] for r in res),'control_rejected',ctl_ok)

if __name__=='__main__':main()
