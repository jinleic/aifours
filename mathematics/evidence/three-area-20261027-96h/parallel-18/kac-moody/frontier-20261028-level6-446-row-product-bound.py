#!/usr/bin/env python3
"""Exact row-product/cofactor strengthening for the pinned level-six matrix.

This reads ONLY the new current-round 162x162 source certificate.  It does
not establish matrix correctness, independently verify its determinant, or
import an older cone guide. All computations are rational.
"""
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent


def main():
    inp=ROOT/'frontier-20261028-level6-446-leading-map-cone-v1.json'
    dest=ROOT/'frontier-20261028-level6-446-row-product-bound-v1.json'
    if dest.exists():raise FileExistsError(dest)
    raw=inp.read_bytes();assert hashlib.sha256(raw).hexdigest()=='606b1cfe1fdadf3d741b0d5aa649ac59a7fc7ca094ff68cf242096cc76adf3ed'
    P=json.loads(raw);assert P['status']=='LEADING_INJECTIVE_COFAC_CONE'
    data=[[[Q(x) for x in triple] for triple in row] for row in P['matrix_entries']]
    n=len(data);assert n==162 and all(len(row)==n for row in data)
    sums=[[sum((abs(e[j]) for e in row),Q(0)) for row in data] for j in range(3)]
    assert all(x>0 for x in sums[0])
    product=math.prod(sums[0]);delta=abs(Q(P['leading_determinant']))
    H=Q(n)*max(product/q for q in sums[0])/delta
    B=max(sums[1]);G=max(sums[2]);old=Q(P['cofactor_bound_C'])
    oldB=old*Q(P['difference_entry_abs_max']);oldG=old*Q(P['constant_entry_abs_max'])
    assert H*B*10**10<oldB and H*G*10**10<oldG
    result={'leading_data_sha256':hashlib.sha256(raw).hexdigest(),'matrix_size':n,
            'L_row_absolute_sums':[str(q) for q in sums[0]],
            'min_L_row_absolute_sum':str(min(sums[0])),'max_L_row_absolute_sum':str(max(sums[0])),
            'L_row_sum_product':str(product),'leading_determinant':str(delta),
            'cofactor_inverse_bound_H':str(H),'K_max_row_absolute_sum_B':str(B),'E_max_row_absolute_sum_G':str(G),
            'both_new_coefficients_over_10^10_strictly_smaller_than_old':True,
            'criterion':'t > H*(B*abs(d)+G), t=(r+s)/2, d=(r-s)/2',
            'status':'EXACT_ROW_PRODUCT_CONE_STRENGTHENING',
            'limits':'conditional on the full unreviewed leading source/determinant and the written cofactor argument; not a separate leading-map correctness proof'}
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact 162 row sums; B',B,'G',G,'both coefficients >10^10 improved;',dest.name,flush=True)

if __name__=='__main__':main()
