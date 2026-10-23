"""Exact verification of the FULL sparse AMH table, with independently built Gram decompositions.

Claim checked: AMH arXiv:2603.19901v1 Eqs (31)-(35) with weights (38). alpha and beta
follow Appendix A; gamma is re-derived as the ordered-pair orbit count (the printed Eq. 41
has a typo). Optional `--gst-second-family` also checks two classical Gijswijt–Schrijver–
Tanaka necessary conditions absent from AMH Eq. 31. This is a moment-feasible point, NOT a
quantum code. No worker code, search matrices or numerical eigensolvers are imported.
Standard library only. Version 1.1: hashes exactly the parsed bytes and rejects duplicate
JSON keys; version 1 is preserved as check_matrix_weights_independent_v1.py.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
from math import comb
from pathlib import Path
import json
import time
from zoneinfo import ZoneInfo

N = 24
EXPECTED = {0:1, 10:18216, 12:156492, 14:1147608, 16:3736557,
            18:6248088, 20:4399164, 22:1038312, 24:32778}


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def orbits(n: int):
    # Enumerate five coordinate-type multiplicities, not the worker's i,j,t,p loops.
    for single_u in range(n + 1):
        for single_v in range(n - single_u + 1):
            for equal_nonzero in range(n - single_u - single_v + 1):
                for unequal_nonzero in range(n - single_u - single_v - equal_nonzero + 1):
                    t = equal_nonzero + unequal_nonzero
                    yield (single_u + t, single_v + t, t, equal_nonzero)


def orbit_size(o: tuple[int,int,int,int], n: int) -> int:
    i, j, t, p = o
    sizes = [i-t, j-t, p, t-p, n-i-j+t]
    ways = 1
    remaining = n
    for count in sizes:
        ways *= choose(remaining, count)
        remaining -= count
    return ways * 3 ** (i+j-t) * 2 ** (t-p)


@lru_cache(None)
def color_polynomial(a: int, t: int) -> tuple[int,...]:
    # Coefficients of (z-1)^a (z+2)^(t-a), by integer convolution.
    if t < a:
        return ()
    poly = [1]
    for c in [-1] * a + [2] * (t-a):
        out = [0] * (len(poly)+1)
        for r, val in enumerate(poly):
            out[r] += c * val
            out[r+1] += val
        poly = out
    return tuple(poly)


@lru_cache(None)
def binary_factor(m: int, t: int, i: int, j: int, k: int) -> int:
    if min(m,t,i,j,k) < 0:
        return 0
    total = 0
    for u in range(t, min(i,j,m-k)+1):
        factor = (choose(u,t) * choose(m-2*k,m-k-u) *
                  choose(m-k-u,i-u) * choose(m-k-u,j-u))
        total += factor if (t-u) % 2 == 0 else -factor
    return total


def block_coefficient(o: tuple[int,int,int,int], a: int, k: int, n: int) -> int:
    i,j,t,p = o
    poly = color_polynomial(a,t)
    if not poly or poly[p] == 0:
        return 0
    if (i+j) % 2:
        raise ValueError('Nonzero odd weight: rational Type-II block reduction not applicable')
    return (binary_factor(n-a,t-a,i-a,j-a,k-a) *
            3 ** ((i+j)//2-t) * poly[p])


def gram_decomposition(matrix: list[list[Q]]) -> tuple[list[dict], str]:
    size = len(matrix)
    if any(matrix[r][c] != matrix[c][r] for r in range(size) for c in range(size)):
        raise ValueError('Nonsymmetric block')
    residual = [row[:] for row in matrix]
    terms = []
    for _ in range(size):
        if any(residual[r][r] < 0 for r in range(size)):
            raise ValueError('Negative Schur-complement diagonal')
        pivots = [r for r in range(size) if residual[r][r] > 0]
        if not pivots:
            if any(v for row in residual for v in row):
                raise ValueError('Zero diagonal with a nonzero off-diagonal')
            break
        p = pivots[0]
        d = residual[p][p]
        vector = [residual[r][p] / d for r in range(size)]
        terms.append((d,vector))
        for r in range(size):
            for c in range(size):
                residual[r][c] -= d * vector[r] * vector[c]
    if any(v for row in residual for v in row):
        raise ValueError('Nonzero residual after Gram factorization')
    # Separate reconstruction, not merely acceptance of positive pivots.
    for r in range(size):
        for c in range(size):
            if sum((d*v[r]*v[c] for d,v in terms),Q(0)) != matrix[r][c]:
                raise ValueError('Gram reconstruction mismatch')
    packed = [{'weight':str(d),'vector':[str(v) for v in vector]} for d,vector in terms]
    digest = hashlib.sha256(json.dumps(packed,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return packed,digest


def reject_duplicate_keys(pairs: list) -> dict:
    keys = [k for k,_ in pairs]
    if len(keys) != len(set(keys)):
        raise ValueError('Duplicate JSON object key')
    return dict(pairs)


def load_table(data: bytes) -> dict:
    raw = json.loads(data.decode('utf-8'), object_pairs_hook=reject_duplicate_keys)
    if not isinstance(raw,dict) or not isinstance(raw.get('entries'),list):
        raise ValueError('Expected full sparse entries array')
    table = {}
    for row in raw['entries']:
        if not isinstance(row,list) or len(row)!=5 or any(type(v) is not int for v in row):
            raise ValueError('Every row must contain five genuine integers')
        i,j,t,p,value = row
        key = (i,j,t,p)
        if not (0<=i<=N and 0<=j<=N and 0<=p<=t<=min(i,j) and i+j<=t+N):
            raise ValueError('Invalid orbit index')
        if key in table:
            raise ValueError('Duplicate full-table row')
        if value <= 0:
            raise ValueError('Sparse nonzero values must be positive')
        table[key] = value
    return table


def scaled_block(xvals: dict, by_ij: dict, a: int, k: int, n: int) -> list[list[Q]]:
    # D^-1 M D^-1 with D=diag(3^(i/2)); handles odd i+j exactly without square roots.
    indices = list(range(k,n+a-k+1))
    matrix = [[Q(0)]*len(indices) for _ in indices]
    for r,i in enumerate(indices):
        for c,j in enumerate(indices):
            for o in by_ij.get((i,j),()):
                i0,j0,t,p = o
                poly = color_polynomial(a,t)
                if not poly or not poly[p]:
                    continue
                beta = binary_factor(n-a,t-a,i0-a,j0-a,k-a)
                if beta:
                    matrix[r][c] += Q(beta*poly[p],3**t)*xvals[o]
    return matrix


def verify(path: Path, include_gram: bool = False, gst_second_family: bool = False) -> dict:
    started = time.monotonic()
    data = path.read_bytes()
    input_sha = hashlib.sha256(data).hexdigest()
    table = load_table(data)
    indexset = list(orbits(N))
    if len(indexset)!=choose(N+4,4) or len(set(indexset))!=len(indexset):
        raise RuntimeError('Independent orbit enumeration incomplete')
    lam = defaultdict(int,table)
    x = {o:Q(lam[o],orbit_size(o,N)) for o in indexset}
    gates = {}
    gates['normalization'] = x[(0,0,0,0)]==1
    gates['commuting_pairs'] = all(lam[o]==0 for o in indexset if (o[2]-o[3])%2)
    symmetry = {}
    for i,j,t,p in indexset:
        if (t-p)%2:
            continue
        key = (tuple(sorted((i,j,i+j-t-p))),t-p)
        value = x[i,j,t,p]
        if key in symmetry and symmetry[key]!=value:
            gates['triple_symmetry'] = False
            break
        symmetry[key] = value
    else:
        gates['triple_symmetry'] = True
    totals = [0]*(N+1)
    for (i,j,t,p),value in table.items():
        totals[i+j-t-p] += value
    gates['all_projector_row_sums'] = all(totals[k]==2**N*lam[k,0,0,0] for k in range(N+1))
    gates['specified_weight_distribution'] = all(lam[j,0,0,0]==EXPECTED.get(j,0) for j in range(N+1))
    gates['pure_support'] = all(not ({i,j,i+j-t-p} & set(range(1,10))) for i,j,t,p in table)
    diag = [lam[j,j,j,j] for j in range(N+1)]
    def kw(j,i):
        return sum((-1)**u*3**(j-u)*choose(i,u)*choose(N-i,j-u) for u in range(j+1))
    gates['knill_laflamme'] = all(sum(kw(j,i)*lam[i,0,0,0] for i in range(N+1))==2**N*lam[j,0,0,0]
                                  for j in range(1,10))
    gates['self_dual_macwilliams'] = all(sum(kw(j,i)*diag[i] for i in range(N+1))==2**N*diag[j]
                                         for j in range(N+1))
    gates['self_dual_shadow_odd'] = all(sum((-1)**i*kw(j,i)*diag[i] for i in range(N+1))==0
                                        for j in range(N+1) if (N-j)%2)
    gates['type_II'] = sum(diag[::2])==2**N
    gates['integer_nonnegative_full_table'] = all(type(v) is int and v>=0 for v in table.values())
    gates['total_ordered_pairs'] = sum(table.values())==2**(2*N)
    if not all(gates.values()):
        raise ValueError({'failed_linear_gates':[k for k,v in gates.items() if not v]})
    block_records = []
    by_ij = defaultdict(list)
    for o in table:
        by_ij[o[:2]].append(o)
    for a in range(N+1):
        for k in range(a,(N+a)//2+1):
            indices = list(range(k,N+a-k+1))
            matrix = [[sum((block_coefficient(o,a,k,N)*x[o] for o in by_ij[i,j]),Q(0))
                       for j in indices] for i in indices]
            gram,digest = gram_decomposition(matrix)
            record = {'a':a,'k':k,'dimension':len(indices),'rank':len(gram),'gram_sha256':digest}
            if include_gram:
                record['gram'] = gram
            block_records.append(record)
    if len(block_records)!=169:
        raise RuntimeError('Wrong PSD block count')
    # PSD routine must reject both types of indefinite two-by-two control.
    rejected = 0
    for bad in ([[Q(1),Q(2)],[Q(2),Q(1)]],[[Q(0),Q(1)],[Q(1),Q(0)]]):
        try:
            gram_decomposition(bad)
        except ValueError:
            rejected += 1
    if rejected!=2:
        raise RuntimeError('Indefinite matrix controls were not rejected')
    extra = None
    if gst_second_family:
        second = {o:x[(o[0]+o[1]-o[2]-o[3],0,0,0)]-x[o] for o in indexset}
        upper_violations = sum(x[o] > x[(o[0],0,0,0)] or x[o] > x[(o[1],0,0,0)] for o in indexset)
        by_second = defaultdict(list)
        for o,v in second.items():
            if v:
                by_second[o[:2]].append(o)
        second_ranks = []
        for a in range(N+1):
            for k in range(a,(N+a)//2+1):
                gram,_ = gram_decomposition(scaled_block(second,by_second,a,k,N))
                second_ranks.append(len(gram))
        if upper_violations or len(second_ranks)!=169:
            raise ValueError('Classical second-family check failed')
        extra = {'upper_bound_violations':0,'second_family_blocks_PSD':len(second_ranks),
                 'nonzero_second_family_entries':sum(1 for v in second.values() if v),
                 'scope':'Classical GST q-ary necessary constraints for the stabilizer as an additive F4 code; standard-form transcription, not part of AMH OP1.'}
    return {'status':'AMH_EQ31_35_38_FEASIBLE_POINT_VERIFIED','input_sha256':input_sha,
            'checked_at_pt':datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
            'source':'AMH v1 Eqs31-35,38; alpha,beta per App. A; gamma re-derived (printed Eq41 typo) = multinomial(24;24-i-j+t,j-t,i-t,p,t-p)*3^(i+j-t)*2^(t-p)',
            'version':'1.1',
            'nonzero_full_table_entries':len(table),'all_admissible_orbits':len(indexset),
            'total_pairs':sum(table.values()),'linear_gates':gates,'PSD_blocks':block_records,
            'indefinite_controls_rejected':rejected,'classical_gst_extra':extra,
            'duration_seconds':time.monotonic()-started,
            'limits':'Exact rational moment feasibility only. Does not construct a code, certify novelty, certify higher hierarchy levels, or establish extra genus-two/dimension claims.'}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument('table',type=Path)
    p.add_argument('--output',type=Path)
    p.add_argument('--include-gram',action='store_true')
    p.add_argument('--gst-second-family',action='store_true')
    args = p.parse_args()
    if args.output and args.output.exists():
        raise SystemExit('Refusing to overwrite evidence output')
    report = verify(args.table,args.include_gram,args.gst_second_family)
    text = json.dumps(report,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    print(json.dumps({k:v for k,v in report.items() if k!='PSD_blocks'},indent=2))
    print('PSD blocks:',len(report['PSD_blocks']),'ranks:',[b['rank'] for b in report['PSD_blocks']])


if __name__=='__main__':
    main()
