#!/usr/bin/env python3
"""Project a floating LP point onto an exact rational equality manifold.

Caller supplies all integer-scaled rows. This is a proposal generator, not an
independent checker: only an exactly checked complete point may be admitted.
"""
from fractions import Fraction
from time import monotonic


def reconstruct(solution,starts,indices,coeff,exact_lower,exact_upper,scale,n,seconds=20):
    started=monotonic();R=len(starts);C=len(solution)
    rows=[];slacks=[];equal=[]
    for i in range(R):
        end=starts[i+1] if i+1<R else len(indices)
        row=tuple((indices[j],int(coeff[j])) for j in range(starts[i],end))
        rows.append(row);equal.append(exact_upper[i] is not None)
        slacks.append(sum(solution[k]*c for k,c in row)-exact_lower[i]/scale)
    summaries=[]
    for tol in (0.0,1e-10,1e-8):
        if monotonic()-started>seconds:break
        picked=[i for i in range(R) if equal[i] or (tol and abs(slacks[i])<=tol)]
        piv={};order={};inconsistent=None
        for step,i in enumerate(picked):
            if step%100==0 and monotonic()-started>seconds:
                inconsistent='time_budget';break
            row={j:Fraction(c) for j,c in rows[i]};b=Fraction(exact_lower[i],scale)
            while True:
                shared=[j for j in row if j in piv]
                if not shared:break
                k=min(shared,key=lambda x:order[x]);factor=row.pop(k);pr,pb=piv[k];b-=factor*pb
                for j,c in pr.items():
                    if j==k:continue
                    z=row.get(j,Fraction(0))-factor*c
                    if z:row[j]=z
                    else:row.pop(j,None)
            if not row:
                if b:inconsistent=f'nonzero equality residual at row {i}: {b}';break
                continue
            k=min(row);factor=row[k];row={j:c/factor for j,c in row.items()};b/=factor
            order[k]=len(order);piv[k]=(row,b)
        item={'active_tolerance':tol,'equations':len(picked),'independent_pivots':len(piv),
              'equality_system_inconsistent_or_stopped':inconsistent,'grid_attempts':[]}
        summaries.append(item)
        if inconsistent:continue
        free=[i for i in range(C) if i not in piv]
        ordered=sorted(piv,key=lambda x:order[x],reverse=True)
        for grid in (1000,10000,100000,1000000,100000000):
            if monotonic()-started>seconds:break
            x=[Fraction(round(float(v)*grid),grid) for v in solution]
            for k in ordered:
                row,b=piv[k];x[k]=b-sum(c*x[j] for j,c in row.items() if j!=k)
            bad_bounds=sum(1 for v in x if v<0 or v>n);bad_eq=bad_ineq=0
            for i,row in enumerate(rows):
                val=sum((x[j]*c for j,c in row),Fraction(0))*scale
                if equal[i]:bad_eq+=int(val!=exact_lower[i])
                else:bad_ineq+=int(val<exact_lower[i])
            item['grid_attempts'].append({'denominator':grid,'bound_violations':bad_bounds,
                                          'equality_violations':bad_eq,'inequality_violations':bad_ineq})
            if not (bad_bounds or bad_eq or bad_ineq):
                return {'found':True,'attempts':summaries,'free_count':len(free),
                        'elapsed_seconds':monotonic()-started},x
    return {'found':False,'attempts':summaries,'elapsed_seconds':monotonic()-started},None
