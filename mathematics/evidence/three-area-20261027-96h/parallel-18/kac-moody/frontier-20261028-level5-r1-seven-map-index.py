#!/usr/bin/env python3
"""Pin every actual r1 seven-map uniform and fixed-pair certificate.

This is an index and consistency check, not a mathematical proof or substitute
for reviewing or independently executing each complete source/certificate.
"""
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent


def get(name):
    b=(ROOT/name).read_bytes();return json.loads(b),{'path':name,'sha256':hashlib.sha256(b).hexdigest(),'LF':b.count(b'\n')}


def main():
    out=ROOT/'frontier-20261028-level5-r1-seven-map-index-v1.json'
    if out.exists():raise FileExistsError(out)
    results=[]
    for ab in ('22','32','23','33','43','34','44'):
        P,pp=get(f'frontier-20261028-level5-r1-{ab}-smallrow-pencil-v1.json')
        D,dp=get(f'frontier-20261028-level5-r1-{ab}-smallrow-determinant-v1.json')
        R,rp=get(f'frontier-20261028-level5-r1-{ab}-smallrow-independent-replay-v1.json')
        assert D['status']=='ONE_SIGN_ALL_S_GE_4' and R['status']=='PASS_ENTIRE_SMALLROW_QUOTIENT_POLYNOMIAL'
        assert P['joint_horizontal_kernel_dim']==R['joint_horizontal_kernel_dimension']==D['matrix_size']
        assert D['constant_coefficient']==R['constant_coefficient'] and D['nonzero_coefficient_count']==R['nonzero_coefficient_count']
        uni={'F':P['free_source_dim'],'I':P['source_ideal_dim'],'Q':P['quotient_source_dim'],
             'k':P['joint_horizontal_kernel_dim'],'sign':D['signs'][0],'terms':D['nonzero_coefficient_count'],
             'constant':D['constant_coefficient'],'artifacts':[pp,dp,rp]}
        fixed=[]
        for s in (2,3):
            C,cp=get(f'frontier-20261028-level5-fixed-{ab}-r1-s{s}-v1.json')
            V,vp=get(f'frontier-20261028-level5-fixed-{ab}-r1-s{s}-independent-replay-v1.json')
            c=C['case'];assert c['status']=='CERTIFIED_ONE_SIGN' and V['status']=='PASS_FULL_SPAN_TREE_JACOBI_GRID_SIGN'
            assert c['horizontal_kernel_dim']==V['horizontal_kernel_dim'] and c['source_dim']==V['source_dim']
            fixed.append({'s':s,'F':c['free_source_dim'],'I':c['ideal_source_dim'],'Q':c['source_dim'],
                          'k':c['horizontal_kernel_dim'],'determinant':c['determinant_coefficients'][0]['coefficient'],
                          'artifacts':[cp,vp]})
        results.append({'degree':[int(ab[0]),int(ab[1]),5],'uniform_s_ge_4':uni,'fixed_s2_s3':fixed})
    out.write_text(json.dumps({'types':results,'uniform_count':7,'fixed_count':14,
                               'note':'one uniform polynomial and two complete fixed quotient cases per type; source/C/PBW reviews remain pending',
                               'metadata_index_not_independent_review':True},indent=2)+'\n')
    print('PINNED seven entire uniform maps and fourteen entire fixed maps;',out.name,flush=True)

if __name__=='__main__':main()
