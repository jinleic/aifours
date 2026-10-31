#!/usr/bin/env python3
"""Directly replay ALL 1780 exact rows of the common-left obstruction."""
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent


def main():
    raw=(ROOT/'frontier-20261028-level6-446-full-target-pencil-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='f4289288531b1b8aa169121c5709968924a075b4b7e749874c75ae7ab53331f3'
    P=json.loads(raw);W=json.loads((ROOT/'frontier-20261028-level6-446-common-left-relation-search-v1.json').read_text())
    assert W['status']=='EXACT_RELATION_OBSTRUCTS_EQUAL_LEFT';u=W['result']['source_u'];v=W['result']['source_v']
    n=P['whole_lowest_dim'];assert len(u)==len(v)==n==162
    first=next(i for i,(a,b) in enumerate(zip(u,v)) if a+b)
    m=P['target_row_count'];assert m==len(P['rows'])==1780
    for row in P['rows']:
        total=Q(0)
        for e in row['entries']:
            j=e['column'];l,ee=Q(e['L']),Q(e['E'])
            total+=(6*l+ee)*u[j]+l*v[j]
        assert total==0,('nonzero full target row',row['word'],total)
    # If v=c*u then this would be a different, possible pencil-kernel question.
    idx=next(i for i,a in enumerate(u) if a);ratio=Q(v[idx],u[idx])
    assert any(Q(b)!=ratio*a for a,b in zip(u,v))
    result={'degree':[4,4,6],'target_sha256':digest,'source_dimension':n,'target_rows':m,
            'all_exact_Au_plus_Lv_rows_zero':True,'first_nonzero_u_plus_v_index':first,
            'first_nonzero_u_plus_v_value':str(u[first]+v[first]),'u_and_v_not_proportional':True,
            'status':'PASS_EXACT_RELATION_OBSTRUCTS_IDENTICAL_INVERTIBLE_LEFT_IMAGES',
            'scope':'rules out X^T A=X^T L=G with G invertible; not a D3 kernel or arbitrary-positive-left impossibility'}
    out=ROOT/'frontier-20261028-level6-446-common-left-relation-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact relation on all1780 rows, u+v nonzero, u/v not proportional;',out.name,flush=True)

if __name__=='__main__':main()
