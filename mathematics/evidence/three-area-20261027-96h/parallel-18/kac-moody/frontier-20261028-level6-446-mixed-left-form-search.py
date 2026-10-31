#!/usr/bin/env python3
"""Search rational X=L+gamma*A left tests on the full 446 target.

Exact blocked integer Gram products and Sylvester checks. A failed bounded
search says nothing about arbitrary left tests or a D3 kernel.
"""
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('checked',ROOT/'frontier-20261028-level6-446-selected-accretivity-attempt.py')
checked=importlib.util.module_from_spec(spec);spec.loader.exec_module(checked)


def main():
    raw=(ROOT/'frontier-20261028-level6-446-full-target-pencil-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='f4289288531b1b8aa169121c5709968924a075b4b7e749874c75ae7ab53331f3'
    P=json.loads(raw);m=P['target_row_count'];n=P['whole_lowest_dim'];D=10368;assert (m,n)==(1780,162)
    L=np.zeros((m,n),dtype=np.int64);E=np.zeros((m,n),dtype=np.int64)
    for i,row in enumerate(P['rows']):
        for e in row['entries']:
            j=e['column'];l,q=Q(e['L'])*D,Q(e['E'])*D
            assert l.denominator==q.denominator==1 and abs(l)<2**62 and abs(q)<2**62
            L[i,j]=int(l);E[i,j]=int(q)
    ml=int(np.max(np.abs(L)));me=int(np.max(np.abs(E)));assert 6*ml+me<2**63
    A=6*L+E;ma=int(np.max(np.abs(A)))
    denominator=2*max(ml*ml,ml*ma,ma*ma)
    block=max(1,min(m,(2**63-1)//denominator));assert block*denominator<2**63
    H0=np.zeros((n,n),dtype=object);HL=np.zeros((n,n),dtype=object);HA=np.zeros((n,n),dtype=object)
    for start in range(0,m,block):
        l=L[start:start+block,:];a=A[start:start+block,:]
        H0+=(l.T@a+a.T@l).astype(object);HL+=(2*(l.T@l)).astype(object);HA+=(2*(a.T@a)).astype(object)
    assert np.array_equal(H0,H0.T) and np.array_equal(HL,HL.T) and np.array_equal(HA,HA.T)
    attempts=[];found=None
    for gamma in (Q(1,10),Q(1,2),Q(1),Q(2),Q(5),Q(10)):
        p,q=gamma.numerator,gamma.denominator
        left0=checked.sylvester(q*H0+p*HA)
        entry={'gamma':str(gamma),'H0_positive':left0['positive_definite'],
               'H0_positive_prefix':left0['verified_positive_prefix']}
        if not left0['positive_definite']:entry['H0_first_nonpositive_pivot']=left0['pivot']
        if left0['positive_definite']:
            leftL=checked.sylvester(q*HL+p*H0)
            entry.update({'HL_positive':leftL['positive_definite'],'HL_positive_prefix':leftL['verified_positive_prefix']})
            if not leftL['positive_definite']:entry['HL_first_nonpositive_pivot']=leftL['pivot']
            else:
                found={'gamma':str(gamma),'H0_leading_determinants':left0['leading_principal_determinants'],
                       'HL_leading_determinants':leftL['leading_principal_determinants']}
        attempts.append(entry);print('gamma',gamma,'H0',entry['H0_positive'],'HL',entry.get('HL_positive','not tested'),flush=True)
        if found:break
    result={'degree':[4,4,6],'full_target_sha256':digest,'target_rows':m,'source_columns':n,
            'common_denominator':D,'int64_block_size':block,'int64_per_block_bound':block*denominator,
            'tested_gammas':[str(q) for q in (Q(1,10),Q(1,2),Q(1),Q(2),Q(5),Q(10))],
            'attempts':attempts,'found':found,
            'status':'BOTH_FULL_TARGET_MIXED_LEFT_FORMS_PD' if found else 'NO_BOTH_PD_IN_BOUNDED_LIST',
            'scope':'particular X=L+gamma A and selected finite rational list; no map-kernel/no-other-left-test/optimality claim'}
    out=ROOT/'frontier-20261028-level6-446-mixed-left-form-search-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('DONE',result['status'],out.name,flush=True)

if __name__=='__main__':main()
