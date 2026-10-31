#!/usr/bin/env python3
"""Independent, standard-library exact checks for f84; no author replay."""
import collections
import hashlib
import itertools
import json
import math
import operator
import pathlib
import subprocess
from functools import reduce

HERE = pathlib.Path(__file__).resolve().parent
OWNER = pathlib.Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242')
PINS = {
    'frontier-20261028-four-zero-spatial-placement-result.json': '9e7c777f5478a124c122323c875de94f6d7a3ee5fbdc9fb4077840c031bf3f39',
    'frontier-20261028-four-zero-coupled-placement-result.json': 'ba99cc035f8cc8bbbcb9edfc99d9068263e93bdb93dfa9e368b2219f1e223c0f',
    'frontier-20261028-four-zero-coupled-rank-result.json': '0a4ebd458300628a6962b6038b91172ddf5aa27dbc2c2075a9702b165bc07406',
}

def pinned_json(name):
    data = (OWNER / name).read_bytes()
    assert hashlib.sha256(data).hexdigest() == PINS[name], name
    return json.loads(data)

def monomial_mask(n, variables):
    return sum(1 << x for x in range(1 << n) if all(x & (1 << i) for i in variables))

def mask_combinations(basis):
    masks = [0]
    for b in basis:
        masks += [m ^ b for m in masks]
    return masks

def rank_binary(rows, n):
    rows = list(rows)
    r = 0
    for c in range(n):
        pivot = next((j for j in range(r, n) if rows[j] & (1 << c)), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        for j in range(n):
            if j != r and rows[j] & (1 << c):
                rows[j] ^= rows[r]
        r += 1
    return r

def enumerate_small_quadratics(n):
    pairs = list(itertools.combinations(range(n), 2))
    linears = [monomial_mask(n, (i,)) for i in range(n)]
    pair_masks = [monomial_mask(n, ij) for ij in pairs]
    linear_masks = mask_combinations(linears)
    quadratic_masks = mask_combinations(pair_masks)
    size = 1 << n
    whole = (1 << size) - 1
    affines = linear_masks + [m ^ whole for m in linear_masks]
    supports = collections.Counter()
    rank_counts = collections.Counter()
    pairs_by_z = collections.defaultdict(set)
    checked_pairs = 0
    for code, quad in enumerate(quadratic_masks):
        rows = [0] * n
        for bit, (i, j) in enumerate(pairs):
            if code & (1 << bit):
                rows[i] ^= 1 << j
                rows[j] ^= 1 << i
        rank = rank_binary(rows, n)
        assert rank % 2 == 0
        for lin in linear_masks:
            q = quad ^ lin
            assert not q & 1  # q(0)=0
            wt = q.bit_count()
            charsum = size - 2 * wt
            assert (charsum == 0 and rank < n) or abs(charsum) == 1 << (n - rank // 2)
            supports[size - wt] += 1
            rank_counts[rank] += 1
            for affine in affines:
                Q = q ^ affine
                w = Q.bit_count()
                s = size - 2 * w
                assert (s == 0 and rank < n) or abs(s) == 1 << (n - rank // 2)
                pairs_by_z[size - wt].add(w)
                checked_pairs += 1
    assert sum(supports.values()) == 1 << (n * (n + 1) // 2)
    assert checked_pairs == (1 << (n * (n + 1) // 2)) * (1 << (n + 1))
    return {'dimension': n, 'zero_constant_quadratics': sum(supports.values()),
            'quadratic_affine_pairs': checked_pairs,
            'zero_support_distribution': dict(sorted(supports.items())),
            'polar_rank_distribution': dict(sorted(rank_counts.items())),
            'attained_z_w_pairs': {str(z): sorted(ws) for z, ws in sorted(pairs_by_z.items())}}

def derive_eight_table():
    n = 8
    size = 1 << n
    linear = mask_combinations([monomial_mask(n, (i,)) for i in range(n)])
    full = (1 << size) - 1
    affine = linear + [x ^ full for x in linear]
    table = collections.defaultdict(set)
    count = 0
    for pairs in range(5):
        quad = 0
        for i in range(pairs):
            quad ^= monomial_mask(n, (2*i, 2*i+1))
        for l in linear:
            q = quad ^ l
            z = size - q.bit_count()
            assert z > 0
            for a in affine:
                table[z].add((q ^ a).bit_count())
                count += 1
    expected = {64:{64,128,192},192:{64,128,192},96:{96,128,160},160:{96,128,160},
                112:{112,128,144},144:{112,128,144},120:{120,136},136:{120,136},
                128:{0,64,96,112,128,144,160,192,256},256:{0,128,256}}
    assert dict(table) == expected
    return {'canonical_polar_rank_affine_pairs':count,
            'table':{str(z):sorted(ws) for z,ws in sorted(table.items())},
            'allowed_F_given_Z4':sorted(z-4 for z in table)}

def fwht(values):
    a = list(values)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def anf_degree(truth):
    a = list(truth)
    n = (len(a)-1).bit_length()
    for i in range(n):
        for x in range(len(a)):
            if x & (1 << i):
                a[x] ^= a[x ^ (1 << i)]
    return max((x.bit_count() for x,v in enumerate(a) if v), default=-1)

def xor_all(xs):
    return reduce(operator.xor, xs, 0)

def spectrum_stats(k):
    assert len(k) == 512 and all(isinstance(v, int) for v in k)
    u = fwht(k)
    direct_r = [sum(k[a]*k[a ^ b] for a in range(512)) for b in range(512)]
    via = fwht([v*v for v in u])
    assert all(x % 512 == 0 for x in via)
    assert direct_r == [x//512 for x in via]
    return {'sum':sum(k), 'sum_squares':sum(v*v for v in k),
            'peak_count':sum(abs(v)==7 for v in k),
            'inverse_nonsign_count':sum(abs(v)!=128 for v in u),
            'nonzero_shift_autocorrelation_count':sum(r != 0 for r in direct_r[1:]),
            'histogram_full':dict(sorted(collections.Counter(k).items()))}

def krawtchouk_direct(n, weight):
    aa = [math.comb(weight, i) for i in range(weight+1)]
    bb = [math.comb(n-weight, i) for i in range(n-weight+1)]
    return [sum((-1 if i & 1 else 1)*aa[i]*bb[j-i]
                for i in range(max(0, j-(n-weight)), min(weight,j)+1))
            for j in range(n+1)]

def dual_certificate(k):
    assert k[0] == 0
    counts = collections.Counter(k[1:])
    assert sum(counts.values()) == 511
    assert sum(t*count for t,count in counts.items()) == 128
    assert sum(t*t*count for t,count in counts.items()) == 16384
    assert sum(count for t,count in counts.items() if t % 2) == 256
    polys = {t:krawtchouk_direct(256, 128+t) for t in counts}
    numer = [math.comb(256,j) + sum(c*polys[t][j] for t,c in counts.items()) for j in range(257)]
    assert all(x % 512 == 0 and x >= 0 for x in numer)
    dual = [x//512 for x in numer]
    assert dual[:3] == [1,0,0] and dual[256] == 0 and dual[255] in (0,1)
    assert sum(dual) == 1 << 247
    inverse = [0]*257
    for j, d in enumerate(dual):
        previous = 1
        inverse[0] += d
        current = 256 - 2*j
        inverse[1] += d*current
        for i in range(1,256):
            top = (256-2*j)*current - (257-i)*previous
            assert top % (i+1) == 0
            following = top // (i+1)
            inverse[i+1] += d*following
            previous, current = current, following
    assert all(v % (1 << 247) == 0 for v in inverse)
    primal = [v//(1 << 247) for v in inverse]
    expected = [0]*257
    expected[0] = 1
    for t,c in counts.items():
        expected[128+t] += c
    assert primal == expected
    return dual, {'nonnegative_integral':len(dual), 'D0_D1_D2':[dual[0],dual[1],dual[2]],
                  'D254_D255_D256':[dual[254],dual[255],dual[256]],
                  'sum_equals_2_pow_247':True, 'inverse_recovers_257_primal_coefficients':True}

def even_five_flat_parities(indicators):
    n, dim = 8, 5
    directions = flats = 0
    for pivots in itertools.combinations(range(n), dim):
        nonpivots = [j for j in range(n) if j not in pivots]
        variable_cells = [(i,j) for i,pivot in enumerate(pivots) for j in nonpivots if j > pivot]
        cosets = mask_combinations([1 << j for j in nonpivots])
        for code in range(1 << len(variable_cells)):
            rows = [1 << j for j in pivots]
            for t,(i,j) in enumerate(variable_cells):
                if code & (1 << t):
                    rows[i] ^= 1 << j
            subspace = mask_combinations(rows)
            assert len(subspace) == 32 and len(set(subspace)) == 32
            directions += 1
            for rep in cosets:
                for indicator in indicators:
                    assert sum(indicator[rep ^ x] for x in subspace) % 2 == 0
                flats += 1
    assert directions == 97155 and flats == 777240
    return {'linear_directions':directions,'affine_5_flats':flats,'indicators_checked':len(indicators)}

def sample_balanced_table():
    M = (set(range(256,512)) - {257}) | {1}
    assert len(M) == 256 and 0 not in M
    T = xor_all(M)
    assert T == 256
    w = fwht([-1 if x in M else 1 for x in range(512)])
    assert all(v % 4 == 0 for v in w)
    k = [v//4 for v in w]
    assert k[0] == 0 and sum(v*v for v in k) == 16384
    assert all((v & 1) == ((a & T).bit_count() & 1) for a,v in enumerate(k))
    q = [(k[x]//2) & 1 for x in range(256)]
    Q = [((k[256+x]-1)//2) & 1 for x in range(256)]
    m = [sum((x >> i) & 1 for x in M) for i in range(8)]
    assert all(v % 2 == 0 for v in m)
    pairs = {(i,j):sum(((x >> i)&1)*((x >> j)&1) for x in M) % 2
             for i,j in itertools.combinations(range(8),2)}
    def predicted(y):
        result = sum(((m[i]//2)&1)*((y>>i)&1) for i in range(8))
        result += sum(v*((y>>i)&1)*((y>>j)&1) for (i,j),v in pairs.items())
        return result % 2
    assert all(q[x] == predicted(x) for x in range(256))
    assert all((q[u^v]^q[u]^q[v]^q[0]) == (Q[u^v]^Q[u]^Q[v]^Q[0])
               for u in range(256) for v in range(256))
    return {'support_definition':'{256,...,511} remove 257, add 1', 'support_size':len(M),
            'T':T, 'balanced':w[0] == 0, 'maximum_abs_W':max(map(abs,w)),
            'satisfies_28_cap':max(map(abs,w)) <= 28,
            'sum_k_squared':sum(v*v for v in k), 'q_zero_count':q.count(0),
            'Q_one_count':sum(Q), 'q_anf_degree':anf_degree(q), 'Q_anf_degree':anf_degree(Q),
            'all_65536_polar_pairs_match':True,'support_parity_expansion_reconstructed':True}

def main():
    spatial = pinned_json('frontier-20261028-four-zero-spatial-placement-result.json')['spectrum_k']
    coupled = pinned_json('frontier-20261028-four-zero-coupled-placement-result.json')['spectrum_k']
    model = pinned_json('frontier-20261028-four-zero-coupled-rank-result.json')
    sstat = spectrum_stats(spatial)
    cstat = spectrum_stats(coupled)
    assert sstat['inverse_nonsign_count'] == 493 and sstat['nonzero_shift_autocorrelation_count'] == 511
    assert cstat['inverse_nonsign_count'] == 507 and cstat['nonzero_shift_autocorrelation_count'] == 508
    assert sstat['peak_count'] == 129 and cstat['peak_count'] == 200
    spatial_zeros = [i for i,v in enumerate(spatial) if v==0]
    spatial_fours = [i for i,v in enumerate(spatial) if abs(v)==4]
    coupled_zeros = [i for i,v in enumerate(coupled) if v==0]
    coupled_fours = [i for i,v in enumerate(coupled) if abs(v)==4]
    assert spatial_zeros == [0,1,2,3] and spatial_fours == [4,5,6,7]
    assert coupled_zeros == [0,64,128,192] and len(coupled_fours) == 140
    assert xor_all(spatial_zeros) == xor_all(spatial_fours) == 0
    assert xor_all(coupled_zeros) == xor_all(coupled_fours) == 0
    assert all(v % 2 == a//256 for a,v in enumerate(spatial))
    assert all(v % 2 == a//256 for a,v in enumerate(coupled))
    p1 = [int(abs(spatial[256+x]) in (1,7)) for x in range(256)]
    p2 = [int(abs(coupled[256+x]) in (1,7)) for x in range(256)]
    Q1 = [sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(4)) % 2 for x in range(256)]
    assert all((spatial[256+x] - (1+2*Q1[x])) % 4 == 0 for x in range(256))
    assert (sum(p1),sum(Q1),sum(a*b for a,b in zip(p1,Q1)),anf_degree(p1)) == (150,120,80,4)
    q2 = [sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3)) % 2 for x in range(256)]
    Q2 = [v ^ 1 for v in q2]
    assert (q2.count(0),sum(Q2),anf_degree(p2)) == (144,144,3)
    assert all((coupled[a] - (2*q2[a%256] + 3*(a//256))) % 4 == 0 for a in range(512))
    zero_p2 = [x for x,v in enumerate(p2) if not v]
    assert len(zero_p2) == 32
    base = zero_p2[0]
    differences = {x ^ base for x in zero_p2}
    assert 0 in differences and all(a^b in differences for a in differences for b in differences)
    assert sum(p2[x] for x in range(32)) % 2 == 0
    mutated = p2.copy(); mutated[0] ^= 1
    assert sum(mutated[x] for x in range(32)) % 2 == 1
    cube = [spatial[x] for x in (0,8,16,24,32,40,48,56)]
    assert cube == [0,-6,-6,-6,-6,-6,-6,-6]
    delta = sum((-1 if (3-mask.bit_count()) % 2 else 1)*cube[mask] for mask in range(8))
    assert delta == -6 and delta % 4 == 2
    sdual, sd = dual_certificate(spatial)
    cdual, cd = dual_certificate(coupled)
    assert [int(x) for x in model['dual_coefficients_decimal']] == cdual
    assert {int(t):c for t,c in model['histogram'].items()} == {t:collections.Counter(coupled[1:])[t] for t in range(-7,8)}
    assert sd['D254_D255_D256'] == [69,0,0] and cd['D254_D255_D256'] == [47,1,0]
    sharp = [int(((x&1)!=0) or ((x&2)!=0)) for x in range(256)]
    assert sharp.count(0) == 64 and sharp[0] == 0 and anf_degree(sharp)==2
    receipt = {'pinned_import_sha256':PINS, 'dimension4':enumerate_small_quadratics(4),
               'dimension5':enumerate_small_quadratics(5), 'eight_dimensional_table':derive_eight_table(),
               'balanced_truth_table':sample_balanced_table(), 'spatial_spectrum':sstat,
               'spatial_dual':sd, 'spatial_zero_indices':spatial_zeros, 'spatial_abs4_indices':spatial_fours,
               'spatial_P_Q':[sum(p1),sum(Q1),sum(a*b for a,b in zip(p1,Q1))], 'spatial_P_degree':anf_degree(p1),
               'spatial_cube':cube, 'spatial_cube_delta':delta,
               'coupled_spectrum':cstat, 'coupled_dual':cd, 'coupled_zero_indices':coupled_zeros,
               'coupled_abs4_count':len(coupled_fours), 'coupled_q_zero_Q_one':[q2.count(0),sum(Q2)],
               'coupled_P_degree':anf_degree(p2), 'coupled_P_complement_affine_5_flat':True,
               'single_bit_flat_parity_mutation_detected':True,
               'all_flat_check':even_five_flat_parities([p1,p2]), 'sharp_quadratic_zero_count':sharp.count(0)}
    receipt['native_clock_before_receipt'] = subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()
    output = HERE / 'independent-check-result-v1.json'
    with output.open('x') as f:
        json.dump(receipt,f,indent=2,sort_keys=True)
        f.write('\n')
    print(json.dumps({'receipt':str(output),'dimension4_supports':receipt['dimension4']['zero_support_distribution'],
                      'dimension5_supports':receipt['dimension5']['zero_support_distribution'],
                      'eight_table':receipt['eight_dimensional_table'],
                      'balanced_truth_table':receipt['balanced_truth_table'],
                      'flat_check':receipt['all_flat_check'],
                      'spatial_inverse_autocor':[sstat['inverse_nonsign_count'],sstat['nonzero_shift_autocorrelation_count']],
                      'coupled_inverse_autocor':[cstat['inverse_nonsign_count'],cstat['nonzero_shift_autocorrelation_count']],
                      'dual_endpoints':[sd['D254_D255_D256'],cd['D254_D255_D256']]},indent=2))

if __name__ == '__main__':
    main()
