#!/usr/bin/env python3
"""Exact CRT and rational-area density of two certified parameter regions.

The result is conditional on the separately pinned map certificates, not a
verification of them, a finite-box guarantee, or a full-quadrant claim.
"""
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent


def main():
    raw=(ROOT/'frontier-20261028-level6-226-modular-row-certificate-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='738977afb213e2ddec6426c852e27bdab0edbaa8611d127f6048ee84db40a217'
    P=json.loads(raw);rows=P['root_free_rows'];assert len(rows)==10
    primes=[r['prime'] for r in rows];assert len(set(primes))==len(primes)
    assert all(p>=2 and all(p%d for d in range(2,math.isqrt(p)+1)) for p in primes)
    assert all(len(set(r['good_x_residues']))==len(r['good_x_residues']) and
               all(0<=x<r['prime'] for x in r['good_x_residues']) for r in rows)
    period=math.prod(primes);bad_count=math.prod(r['prime']-len(r['good_x_residues']) for r in rows)
    delta=Q(bad_count,period);modular_coverage=1-delta*delta
    lam=Q(217,50);outside_ratio=(lam-1)/(lam+1)
    combined=1-delta*delta*outside_ratio
    assert delta==Q(30599331840,312792071761)
    assert modular_coverage>Q(99,100) and combined>Q(497,500)
    out=ROOT/'frontier-20261028-level6-226-certified-density-v1.json'
    if out.exists():raise FileExistsError(out)
    result={'modular_certificate_sha256':digest,'prime_period':str(period),'bad_one_coordinate_count_per_period':str(bad_count),
            'bad_one_coordinate_density':str(delta),'row_or_column_coverage_density':str(modular_coverage),
            'ratio_lambda':str(lam),'outside_ratio_geometric_area':str(outside_ratio),
            'combined_modular_or_ratio_coverage_density':str(combined),'combined_strictly_above_497_over_500':True,
            'status':'EXACT_CRT_AND_RATIONAL_SQUARE_DENSITY',
            'scope':'natural density in expanding square of certified parameter subset; conditional on named map proofs; not a finite-box bound, full quadrant or actual map maximality'}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact CRT density and rational cone area: certified subset density >497/500;',out.name)

if __name__=='__main__':main()
