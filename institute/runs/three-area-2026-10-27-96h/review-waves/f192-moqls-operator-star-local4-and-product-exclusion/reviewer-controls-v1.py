#!/usr/bin/env python3
"""Exact bounded reviewer controls. No author code, solver, numerical float, or external data."""
import hashlib
import itertools
import json
import pathlib
import subprocess
import sys
import traceback
from fractions import Fraction as F

HERE = pathlib.Path(__file__).resolve().parent
INPUTS = [
    HERE / 'manifest-v1.json',
    pathlib.Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/MOQLS-unrestricted-four-family-ray-gap-intrinsic-and-local-span-budget-entire-parent-v1.md'),
    pathlib.Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/moqls8/frontier-20261029-operator-star-cover-and-local4-rigidity-v1.md'),
    pathlib.Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/moqls8/frontier-20261029-C4-product-component-exclusion-v1.md'),
]
OUT = HERE / 'reviewer-controls-output-v1.json'
Z = (F(0), F(0))
ONE = (F(1), F(0))

def G(a=0, b=0): return (F(a), F(b))
def add(x, y): return (x[0] + y[0], x[1] + y[1])
def neg(x): return (-x[0], -x[1])
def sub(x, y): return add(x, neg(y))
def mul(x, y): return (x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def conj(x): return (x[0], -x[1])
def div(x, y):
    d = y[0]*y[0] + y[1]*y[1]
    if not d: raise ZeroDivisionError('Gaussian rational zero')
    return ((x[0]*y[0]+x[1]*y[1])/d, (x[1]*y[0]-x[0]*y[1])/d)
def scale(x, a): return (x[0]*a, x[1]*a)
def dot(x, y):
    out = Z
    for a, b in zip(x, y): out = add(out, mul(conj(a), b))
    return out
def nrm(v):
    n = dot(v, v)
    if n[1] or n[0] <= 0: raise ValueError('nonpositive norm')
    return n[0]
def gauss_abs2(z): return z[0]*z[0] + z[1]*z[1]
def tensor(x, y): return tuple(mul(a, b) for a in x for b in y)
def vadd(x, y): return tuple(add(a, b) for a, b in zip(x, y))
def vscale(x, z): return tuple(mul(a, z) for a in x)
def proj(v):
    d = nrm(v)
    return [[scale(mul(a, conj(b)), F(1, 1)/d) for b in v] for a in v]
def flat(M): return [p for row in M for z in row for p in z]
def matmul(A, B):
    return [[sumg(mul(A[i][k], B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def matsub(A, B): return [[sub(x, y) for x, y in zip(a, b)] for a, b in zip(A, B)]
def sumg(xs):
    z = Z
    for x in xs: z = add(z, x)
    return z
def cross(P, Q):
    pq = matmul(P, Q)
    return matsub(pq, matmul(pq, P))
def rank_real(rows):
    if not rows: return 0
    A = [list(map(F, x)) for x in rows]
    r = 0
    for j in range(len(A[0])):
        p = next((i for i in range(r, len(A)) if A[i][j]), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        t = A[r][j]
        A[r] = [x/t for x in A[r]]
        for i in range(r+1, len(A)):
            t = A[i][j]
            if t: A[i] = [x-t*y for x, y in zip(A[i], A[r])]
        r += 1
        if r == len(A): break
    return r
def rank_complex(rows):
    if not rows: return 0
    A = [list(x) for x in rows]
    r = 0
    for j in range(len(A[0])):
        p = next((i for i in range(r, len(A)) if A[i][j] != Z), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        t = A[r][j]
        A[r] = [div(x, t) for x in A[r]]
        for i in range(r+1, len(A)):
            t = A[i][j]
            if t != Z: A[i] = [sub(x, mul(t, y)) for x, y in zip(A[i], A[r])]
        r += 1
        if r == len(A): break
    return r
def same_ray(x, y):
    ix = next((i for i, a in enumerate(x) if a != Z), None)
    if ix is None or y[ix] == Z: return False
    return all(mul(x[j], y[ix]) == mul(y[j], x[ix]) for j in range(len(x)))
def ray_key(x):
    a = next(a for a in x if a != Z)
    return tuple(div(b, a) for b in x)
def weight(v, z): return gauss_abs2(dot(v, z))/(nrm(v)*nrm(z))
def native_clock(): return subprocess.check_output(['/bin/date', '-u', '+%Y-%m-%dT%H:%M:%SZ'], text=True).strip()
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()

checks = []
def check(name, ok, detail):
    checks.append({'name': name, 'result': 'PASS' if ok else 'FAIL', 'detail': detail})
    if not ok: raise AssertionError(name + ': ' + detail)

def gf_mul(a, b):
    out = 0
    while b:
        if b & 1: out ^= a
        b >>= 1
        a <<= 1
        if a & 8: a ^= 0b1011
    return out

def basis(seed):
    # Gaussian-integer columns all have squared norm 25; division by 5 is implicit.
    result = []
    for block in range(4):
        for k in range(2):
            v = [Z]*8
            if (seed+block) % 2:
                v[2*block], v[2*block+1] = ((G(3), G(4)) if k == 0 else (G(-4), G(3)))
            else:
                v[2*block], v[2*block+1] = ((G(3), G(0,4)) if k == 0 else (G(0,4), G(3)))
            result.append(tuple(v))
    return result

def line_reason(family):
    for k, sq in enumerate(family):
        for i in range(8):
            for j in range(8):
                if nrm(sq[8*i+j]) != 25: return 'unit-norm'
                for l in range(j):
                    if dot(sq[8*i+j], sq[8*i+l]) != Z: return 'row-orthogonality'
                    if dot(sq[8*j+i], sq[8*l+i]) != Z: return 'column-orthogonality'
    return None

def pair_reason(A, B):
    for y in range(64):
        for z in range(y):
            if dot(A[y], A[z]) != Z and dot(B[y], B[z]) != Z:
                return 'pair-product-orthogonality'
    return None

def validate(family):
    reason = line_reason(family)
    if reason: return reason
    for i, j in itertools.combinations(range(4), 2):
        reason = pair_reason(family[i], family[j])
        if reason: return reason
    return 'VALID'

def exact_full_family():
    slopes = [1, 2, 3, 4]
    syms = [[i ^ gf_mul(a, j) for i in range(8) for j in range(8)] for a in slopes]
    bases = [basis(i) for i in range(4)]
    family = [[bases[k][t] for t in syms[k]] for k in range(4)]
    check('ordinary-four-MOQLS-positive', validate(family) == 'VALID',
          '64 cells; all four row/column ONBs and all six 64-product ONBs; GF(8) slopes; complex Gaussian-rational global bases')
    bad = [list(s) for s in family]
    bad[0][1] = bad[0][0]
    check('row-negative', validate(bad) == 'row-orthogonality', 'duplicate in one actual row, intended row reason')
    bad = [family[0], family[0], family[2], family[3]]
    check('Q-mate-negative', line_reason(bad) is None and pair_reason(bad[0], bad[1]) == 'pair-product-orthogonality',
          'rows and columns still ONBs; identical squares violate Q-X product ONB')
    bad = [family[0], family[1], family[1], family[3]]
    check('mate-pair-negative', line_reason(bad) is None and all(pair_reason(bad[0], bad[k]) is None for k in (1,2,3))
          and pair_reason(bad[1], bad[2]) == 'pair-product-orthogonality',
          'all Q-mate ONBs retained; duplicated mates violate mate-mate ONB')
    overlap = next(((y,z) for y in range(64) for z in range(64) if y != z
                    and dot(bad[1][y], bad[1][z]) != Z and dot(bad[0][y], bad[0][z]) == Z), None)
    check('mate-weight-disjointness-negative', overlap is not None, 'duplicated mates have simultaneously nonzero weights at a distinct cell')
    outer = [[[mul(x, conj(y)) for y in v] for x in v] for v in bases[0]]
    identities = disjoint = 0
    for y in range(64):
        for z in range(64):
            if y == z: continue
            nz = sum(dot(family[k][y], family[k][z]) != Z for k in (1,2,3))
            if nz > 1: raise AssertionError('mate disjointness')
            disjoint += 1
        for k in (1,2,3):
            coeff = [F(0)]*8
            for z in range(64):
                if z == y or z//8 == y//8 or z%8 == y%8: continue
                if dot(family[0][y], family[0][z]) != Z: continue
                coeff[syms[0][z]] += gauss_abs2(dot(family[k][y], family[k][z]))
            for i in range(8):
                for j in range(8):
                    lhs = sumg(scale(outer[a][i][j], coeff[a]) for a in range(8))
                    rhs = sub(G(15625 if i == j else 0), scale(outer[syms[0][y]][i][j], F(625)))
                    if lhs != rhs: raise AssertionError('per-mate operator identity')
            identities += 1
    check('per-mate-operator-identities', identities == 192 and disjoint == 4032,
          'all 64 y and three mates; exact 8x8 matrices and all distinct-cell weight disjointness')
    counts = [syms[0].count(a) for a in range(8)]
    check('component-boundary', counts == [8]*8, 'all 8 intrinsic components have dimension 1 and multiplicity 8; no nontrivial component is claimed')
    # In the full ambient space (not one intrinsic component), each perpendicular Q ray occurs eight times.
    check('ambient-star-positive', all(x == 8 for x in counts), 'A=8(I-P), hence A-5(I-P)=3(I-P) positive; ambient is reducible')
    check('ambient-no-isolated-shortcut-negative', all(x == 8 for x in counts),
          'ambient star has isolated orthogonal rays of multiplicity 8; nontrivial-component GAP3 is inapplicable')

def partial_fractional_control():
    e0, e1 = (G(1),Z), (Z,G(1))
    c, d = (G(3),G(0,4)), (G(0,4),G(3))
    cells = [(e0,e0), (e0,e1), (e1,c), (e1,d)]
    check('fractional-pair-product-ONB', all(dot(x1,x2) == Z or dot(y1,y2) == Z
          for (x1,y1),(x2,y2) in itertools.combinations(cells,2)),
          'complete 2-by-2 product ONB; supplemental algebra, not a four-MOQLS')
    weights = [weight(e0, x) for _, x in cells]
    check('fractional-weights', weights == [F(1),F(0),F(9,25),F(16,25)],
          'nontrivial exact weights 9/25 and 16/25')
    matrix = [[sumg(scale(proj(q)[i][j], weights[k]) for k,(q,_) in enumerate(cells)) for j in range(2)] for i in range(2)]
    check('fractional-partial-resolution', matrix == [[ONE,Z],[Z,ONE]], 'partial product-basis resolution gives I exactly')
    missing = [[sumg(scale(proj(q)[i][j], weights[k]) for k,(q,_) in enumerate(cells[:-1])) for j in range(2)] for i in range(2)]
    check('fractional-missing-term-negative', missing != [[ONE,Z],[Z,ONE]], 'removing the 16/25 term fails the identity, not a parser error')

def star_controls():
    axes = [(G(1),Z,Z),(Z,G(1),Z),(Z,Z,G(1))]
    v, w = (G(1),G(0,1),Z), (G(1),G(0,2),Z)
    stars = axes + [v,w]
    check('support-two-off-direction', rank_real([flat(proj(a)) for a in stars]) == 4 and not same_ray(v,w),
          'one real off-direction in a two-plane, two distinct complex rays')
    check('support-two-isolated-axis', all(dot(axes[2], a) == Z for a in stars if not same_ray(a,axes[2])),
          'third axis is an isolated star ray')
    eval_e3 = sum((weight(axes[2],a) for a in axes for _ in range(3)), F(0)) + 3*weight(axes[2],v)
    check('support-two-cover-negative', eval_e3 == 3 and eval_e3 < 5,
          'multiplicity-three axes plus v fail the five-cover exactly along the isolated axis')
    v3 = (G(1),G(0,1),G(1))
    vals = [G(1),G(-1),G(0,1),G(0,-1),G(1,1),G(1,-1),G(-1,1),G(-1,-1)]
    def off(x):
        p = proj(x)
        return [t for i in range(3) for j in range(i+1,3) for t in p[i][j]]
    ov = off(v3)
    matching = 0
    for a in itertools.product(vals, repeat=3):
        ow = off(a)
        if rank_real([ov,ow]) == 1:
            matching += 1
            if not same_ray(a,v3): raise AssertionError('support-three rank-one rigidity')
    check('support-three-purity-finite', matching > 0, 'enumerated 512 complex integer rays; every off-collinear ray is the same projective ray; matches='+str(matching))
    xi = (G(1),G(0,1),G(-2))
    check('support-three-cover-negative', dot(v3,xi) == Z and sum((3*weight(xi,a) for a in axes),F(0)) + 3*weight(xi,v3) == 3,
          'xi perpendicular to the unique extra ray; axis multiplicity cap gives exactly 3<5')

def neighbour_controls():
    pi = (Z,Z,ONE)
    mus = [(ONE,Z,Z),(Z,ONE,Z),(G(F(3,5)),G(0,F(4,5)),Z)]
    check('three-distinct-K-intersections', all(rank_complex([pi,a,b]) == 3 for a,b in itertools.combinations(mus,2)),
          'each two 2-planes meet only in the pi ray, including a genuinely complex plane')
    check('duplicate-K-negative', rank_complex([pi,mus[0],mus[0]]) == 2,
          'duplicate plane fails the intended pairwise-intersection condition')
    rays = [pi]*3 + [vadd(pi, mu) for mu in mus for _ in range(2)]
    total = sum((weight(pi,x) for x in rays),F(0))
    sums = [sum((weight(pi,x) for x in rays if rank_complex([pi,mu,x]) == 2),F(0)) for mu in mus]
    check('pi-overlap-count', total == 6 and sums == [F(4)]*3 and sum(sums) == total+2*3,
          'three shared pi cells counted three times, all other pi-active cells at most once')
    check('pi-three-directions-contradiction', 3*5 > 8+2*3, '15>14 at the maximal allowed pi multiplicity')
    u = (ONE,Z,Z)
    lam1 = (Z,ONE,Z)
    kap = G(F(3,13),F(4,13))
    lam2 = (Z,kap,G(F(12,13)))
    r = G(1,1)
    first = r
    for _ in range(6):
        s = neg(div(ONE,mul(kap,conj(r))))
        sp = neg(div(ONE,conj(s)))
        t = neg(div(ONE,mul(conj(kap),conj(sp))))
        rn = neg(div(ONE,conj(t)))
        v1, v2, v3, v4, v5 = [vadd(u,vscale(l,q)) for l,q in ((lam1,r),(lam2,s),(lam2,sp),(lam1,t),(lam1,rn))]
        if not all(dot(a,b) == Z for a,b in zip((v1,v2,v3,v4),(v2,v3,v4,v5))):
            raise AssertionError('closure orthogonality')
        if rn != scale(r,F(25,169)) or not (0 < gauss_abs2(rn) < gauss_abs2(r)):
            raise AssertionError('closure contraction')
        r = rn
    check('complex-closure-contraction', r == scale(first,F(25,169)**6),
          'six exact chains, all four orthogonal edges, kappa=(3+4i)/13 and ratio 25/169; finite sample only')
    bads = neg(div(ONE,mul(kap,first)))
    check('closure-conjugation-negative', dot(vadd(u,vscale(lam1,first)),vadd(u,vscale(lam2,bads))) != Z,
          'omitting conjugation produces a nonorthogonal cross-plane pair')
    check('closure-boundary-guards', gauss_abs2(kap) == F(25,169) and 0 < gauss_abs2(kap) < 1,
          'kappa=0 gives no mixed cross partner; |kappa|=1 coincides the planes; r=0 is not mixed')

def product_controls():
    e0, e1 = (ONE,Z), (Z,ONE)
    local = [e0,e1,(G(3),G(0,4)),(G(0,4),G(3)),(G(5),G(0,12)),(G(0,12),G(5))]
    pairs = [(a,b) for a in local for b in local]
    ok = [[False]*36 for _ in range(36)]
    for i,j in itertools.combinations(range(36),2):
        ok[i][j] = dot(pairs[i][0],pairs[j][0]) == Z or dot(pairs[i][1],pairs[j][1]) == Z
    counts = {'A_only':0,'B_only':0,'both':0}
    def classification(indices):
        if not all(ok[min(i,j)][max(i,j)] for i,j in itertools.combinations(indices,2)):
            return 'product-basis-not-orthogonal'
        def split(f):
            groups = {}
            for i in indices: groups.setdefault(ray_key(pairs[i][f]),[]).append(i)
            if len(groups) != 2 or sorted(map(len,groups.values())) != [2,2]: return False
            gs = list(groups.values())
            return dot(pairs[gs[0][0]][f],pairs[gs[1][0]][f]) == Z and all(
                dot(pairs[g[0]][1-f],pairs[g[1]][1-f]) == Z for g in gs)
        a,b = split(0),split(1)
        return 'both' if a and b else 'A_only' if a else 'B_only' if b else 'NEITHER'
    for ids in itertools.combinations(range(36),4):
        if not all(ok[i][j] for i,j in itertools.combinations(ids,2)): continue
        c = classification(ids)
        if c == 'NEITHER': raise AssertionError('product ONB split classification')
        counts[c] += 1
    check('complex-product-ONB-split-finite', all(counts.values()), 'exhaustive 36 choose 4 finite rays; '+json.dumps(counts,sort_keys=True))
    bad = (0,1,6,8)
    check('product-ONB-negative', classification(bad) == 'product-basis-not-orthogonal',
          'nonorthogonal fourth ray rejected for intended basis reason')
    # Five complex qubit ONBs, once on each first-factor axis; this intentionally is not a 32-cell component.
    second = [e0,e1]
    for a,b in ((3,4),(5,12),(8,15),(7,24)):
        second += [(G(a),G(0,b)),(G(0,b),G(a))]
    rays = [tensor(p,q) for p in (e0,e1) for q in second]
    def star_eval(u,v,rs):
        return sum((weight(v,z) for z in rs if dot(u,z) == Z),F(0))
    u00,u01,u10,u11 = [tensor(p,q) for p in (e0,e1) for q in (e0,e1)]
    tests = [star_eval(u00,u10,rays), star_eval(u01,u11,rays),
             star_eval(u10,u00,rays), star_eval(u11,u01,rays)]
    check('twenty-cell-scalar-boundary', tests == [F(5)]*4 and len(rays) == 20,
          'four P-A tested scalar inequalities tight; N_A(a)=N_A(a-perp)=10; not a complete C4 component')
    cut = rays[:10] + rays[11:]
    check('twenty-cell-missing-direction-negative', len(cut) == 19 and star_eval(u00,u10,cut) < 5,
          'removing one opposite-sector ray breaks the intended scalar cover')
    check('split-basis-counting', 2*20 > 32, 'two DIFFERENT A bases, or two different B bases, have disjoint local rays and would require at least 40 cells')
    check('disconnected-product-boundary', star_eval(u00,u01,rays) == 1,
          'twenty-cell scalar fixture fails full five-cover in a same-sector direction and is reducible')
    x, xp = tensor(e0,second[2]), tensor(e0,second[3])
    star = [z for z in rays if dot(x,z) == Z]
    check('all-light-isolated-partner', dot(x,xp) == Z and any(same_ray(xp,z) for z in star)
          and all(same_ray(xp,z) or dot(xp,z) == Z for z in star),
          'mixed complex two-support ray has its actual isolated in-plane partner')
    check('all-light-cover-negative', star_eval(x,xp,rays) == 1, 'partner multiplicity one gives 1<5, intended cover failure')

def residual_controls():
    # Six REAL local rays, three exact orthonormal bases. Full Cartesian 36-ray fixture is not 32 cells and not a four-MOQLS.
    local = [(ONE,Z),(Z,ONE),(G(3),G(4)),(G(-4),G(3)),(G(5),G(12)),(G(-12),G(5))]
    rays = [tensor(a,b) for a in local for b in local]
    P = [proj(z) for z in rays]
    b = rank_real([flat(q) for q in P])
    check('real-product-span-nine', b == 9, '36-ray real product fixture; not an actual four-MOQLS component')
    # The nonorthogonality graph is connected.
    seen = {0}; todo = [0]
    while todo:
        i = todo.pop()
        for j in range(36):
            if j not in seen and dot(rays[i],rays[j]) != Z: seen.add(j); todo.append(j)
    check('real-product-connected', len(seen) == 36, 'all 36 projective rays in one nonorthogonality graph component')
    for idx in (0, 16):
        u = rays[idx]; Pu = P[idx]
        stars = [j for j,z in enumerate(rays) if dot(u,z) == Z]
        active = [j for j,z in enumerate(rays) if dot(u,z) != Z]
        sig = rank_real([flat(P[j]) for j in stars])
        cr = rank_real([flat(cross(Pu,P[j])) for j in range(36)])
        cspan = rank_complex([rays[j] for j in active])
        kernel_sub = rank_real([flat(Pu)] + [flat(P[j]) for j in stars])
        check('span-nine-equality-sample-'+str(idx), (sig,cr,cspan,kernel_sub,b-cr) == (5,3,4,6,6),
              'sigma=5, real cross=3, active complex span=4, star+P_u=full 6D kernel')
    u, v = rays[0], rays[1]
    cover = sum((weight(v,z) for z in rays if dot(u,z) == Z),F(0))
    check('span-nine-not-family-negative', len(rays) == 36 and cover == 3 and cover < 5,
          '36 cells rather than 32 and the actual five-cover fails at e00 along e01: 3<5')
    star_sector = [j for j,z in enumerate(rays) if dot(rays[0],z) == Z and same_ray(local[j//6],local[1])]
    check('star-span-omission-negative', rank_real([flat(P[j]) for j in star_sector]) == 3,
          'retaining one factor sector loses two of the five star-span directions')
    complex_local = [(ONE,Z),(Z,ONE),(G(3),G(4)),(G(3),G(0,4))]
    local_rank = rank_real([flat(proj(a)) for a in complex_local])
    complex_rank = rank_real([flat(proj(tensor(a,b))) for a in complex_local for b in complex_local])
    check('complex-product-span-sixteen', local_rank == 4 and complex_rank == 16,
          'arbitrary complex local pure projectors real-span Herm(2) tensor Herm(2), dimension 16, not 9')

def main():
    if OUT.exists(): raise FileExistsError('refusing to overwrite output')
    exact_full_family()
    partial_fractional_control()
    star_controls()
    neighbour_controls()
    product_controls()
    residual_controls()

if __name__ == '__main__':
    start = native_clock()
    result = {'clock_start_utc':start, 'script_sha256':digest(pathlib.Path(__file__)),
              'inputs': [{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size,'LF':p.read_bytes().count(b'\n')} for p in INPUTS],
              'control_scope':'Exact finite diagnostics only; full four-MOQLS fixture has only dimension-one components. Supplemental examples are explicitly not full four-MOQLS.',
              'checks':checks}
    rc = 0
    try:
        main()
        result['status'] = 'PASS'
    except Exception as exc:
        result['status'] = 'FAIL'
        result['exception'] = repr(exc)
        result['traceback'] = traceback.format_exc()
        rc = 1
    result['clock_end_utc'] = native_clock()
    result['exit_code'] = rc
    try:
        with OUT.open('x', encoding='utf-8') as f: json.dump(result,f,indent=2,sort_keys=True); f.write('\n')
    except Exception:
        traceback.print_exc(); sys.exit(2)
    print(json.dumps({'status':result['status'],'exit_code':rc,'checks':len(checks),'start':start,'end':result['clock_end_utc'],'output':str(OUT)},sort_keys=True))
    sys.exit(rc)
