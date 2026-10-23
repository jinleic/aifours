#!/usr/bin/env python3
"""moqls7-k1-delta-v1 bridge check (delegated parent delta check; stdlib only, in memory, one process).

Checks, against the pinned lane file evidence/nets7_classes.json (read-only):
  B1  the pandiagonal 4-net of order 7 (rows x=c, columns y=c, broken diagonals y-x=b, broken anti-diagonals
      y+x=b; point index 7x+y) satisfies the net axioms and has direction set {inf,0,1,-1};
  B2  the shear (x,y)->(x,y+x) is an affine collineation of AG(2,7) and maps the pandiagonal net line-for-line
      onto the lane's class 5 (labels (x,y,y-x,y-2x)), not onto class 6;
  B3  class-5/class-6 label formulas and harmonic/equianharmonic cross-ratio types;
  B4  the two diagonal resolutions are orthogonal (every pair of lines meets in exactly one cell).
Aid only (computed [F] consistency check, never a premise):
  F1  strong complete mappings mu of Z_7 (mu, mu+id, mu-id all bijective) and the exact ray count of the
      Fourier-type square |phi_ij> ~ (w^(t*j + i*mu(t)))_t used by Huang-Li Thm 2.6 / Cor 2.7.
Writes nothing; the caller stores stdout.
"""
import hashlib, itertools, json, sys

NETS = '/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/evidence/nets7_classes.json'
EXPECT = '78d1728f9096afff9d23650f88808f9d7888b4cc380141f68b31578a26ec0d67'
Q = 7
INV = {a: pow(a, Q - 2, Q) for a in range(1, Q)}


def classes_from_labels(labels):
    out = []
    for c in range(4):
        d = {}
        for p, lab in enumerate(labels):
            d.setdefault(lab[c], set()).add(p)
        out.append(frozenset(frozenset(s) for s in d.values()))
    return out


def net_axioms(classes):
    pts = set(range(Q * Q))
    ok = len(classes) == 4
    for cl in classes:
        ok = ok and len(cl) == Q and all(len(l) == Q for l in cl) and set().union(*cl) == pts
    for a, b in itertools.combinations(range(len(classes)), 2):
        for l in classes[a]:
            for m in classes[b]:
                ok = ok and len(l & m) == 1
    return ok


def xy(p):
    return divmod(p, Q)


def pair_slope(p, r):
    (x1, y1), (x2, y2) = xy(p), xy(r)
    if x1 == x2:
        return 'inf'
    return ((y2 - y1) * INV[(x2 - x1) % Q]) % Q


def class_direction(cl):
    """Return the unique direction of a parallel class of affine lines, or None if not affine-parallel."""
    dirs = set()
    for l in cl:
        for p, r in itertools.combinations(sorted(l), 2):
            dirs.add(pair_slope(p, r))
    return dirs.pop() if len(dirs) == 1 else None


def proj(m):
    return (0, 1) if m == 'inf' else (1, m)


def det(u, v):
    return (u[0] * v[1] - u[1] * v[0]) % Q


def cross_ratios(dirs):
    vals = set()
    for a, b, c, d in itertools.permutations([proj(m) for m in dirs]):
        num, den = det(a, c) * det(b, d) % Q, det(b, c) * det(a, d) % Q
        vals.add(num * INV[den] % Q)
    return sorted(vals)


def all_lines():
    lines = set()
    for m in list(range(Q)) + ['inf']:
        for b in range(Q):
            if m == 'inf':
                lines.add(frozenset(Q * b + y for y in range(Q)))
            else:
                lines.add(frozenset(Q * x + (m * x + b) % Q for x in range(Q)))
    return lines


def main():
    raw = open(NETS, 'rb').read()
    sha = hashlib.sha256(raw).hexdigest()
    res = {'nets7_classes_path': NETS, 'nets7_classes_sha256': sha, 'sha_matches_expected': sha == EXPECT}
    data = json.loads(raw)
    cls = data['classes']
    res['class5_origin'] = cls[5]['origin']
    res['class6_origin'] = cls[6]['origin']
    nets = {i: classes_from_labels([tuple(v) for v in c['net']]) for i, c in enumerate(cls)}

    # B3: label formulas and direction / cross-ratio types of the two Desarguesian classes
    f5 = all(tuple(cls[5]['net'][Q * x + y]) == (x, y, (y - x) % Q, (y - 2 * x) % Q) for x in range(Q) for y in range(Q))
    f6 = all(tuple(cls[6]['net'][Q * x + y]) == (x, y, (y - x) % Q, (y - 3 * x) % Q) for x in range(Q) for y in range(Q))
    res['B3_class5_labels_are_(x,y,y-x,y-2x)'] = f5
    res['B3_class6_labels_are_(x,y,y-x,y-3x)'] = f6
    d5 = [class_direction(c) for c in nets[5]]
    d6 = [class_direction(c) for c in nets[6]]
    res['B3_class5_directions'] = sorted(map(str, d5))
    res['B3_class6_directions'] = sorted(map(str, d6))
    res['B3_class5_cross_ratio_values'] = cross_ratios(d5)
    res['B3_class6_cross_ratio_values'] = cross_ratios(d6)
    res['B3_class5_harmonic'] = cross_ratios(d5) == sorted({(-1) % Q, 2, INV[2]})
    res['B3_class6_equianharmonic'] = all((l * l - l + 1) % Q == 0 for l in cross_ratios(d6))

    # B1: pandiagonal net
    pand_labels = [(x, y, (y - x) % Q, (y + x) % Q) for x in range(Q) for y in range(Q)]
    pand = classes_from_labels(pand_labels)
    dp = [class_direction(c) for c in pand]
    res['B1_pandiagonal_net_axioms'] = net_axioms(pand)
    res['B1_pandiagonal_directions'] = sorted(map(str, dp))
    res['B1_pandiagonal_directions_equal_{inf,0,1,-1}'] = sorted(map(str, dp)) == sorted(map(str, ['inf', 0, 1, (-1) % Q]))
    res['B1_pandiagonal_cross_ratio_values'] = cross_ratios(dp)
    res['B1_pandiagonal_harmonic'] = cross_ratios(dp) == sorted({(-1) % Q, 2, INV[2]})
    # each diagonal / anti-diagonal line has one cell per row and per column (transversal shape)
    rows = {frozenset(Q * x + y for y in range(Q)) for x in range(Q)}
    cols = {frozenset(Q * x + y for x in range(Q)) for y in range(Q)}
    diag_lines = set(pand[2]) | set(pand[3])
    res['B4_each_diagonal_line_meets_each_row_and_column_once'] = all(
        len(l & r) == 1 for l in diag_lines for r in rows | cols)
    res['B4_diagonal_resolutions_orthogonal'] = all(len(l & m) == 1 for l in pand[2] for m in pand[3])
    res['B4_main_diagonal_and_antidiagonal_are_lines'] = (
        frozenset(Q * i + i for i in range(Q)) in pand[2] and frozenset(Q * i + (Q - 1 - i) for i in range(Q)) in pand[3])

    # B2: shear
    def S(p):
        x, y = xy(p)
        return Q * x + (y + x) % Q
    res['B2_shear_bijective'] = sorted(S(p) for p in range(Q * Q)) == list(range(Q * Q))
    L = all_lines()
    res['B2_AG27_has_56_lines'] = len(L) == 56
    res['B2_shear_is_affine_collineation'] = all(frozenset(S(p) for p in l) in L for l in L)
    img = [frozenset(frozenset(S(p) for p in l) for l in c) for c in pand]
    di = [class_direction(c) for c in img]
    res['B2_image_directions'] = sorted(map(str, di))
    res['B2_image_directions_equal_{inf,0,1,2}'] = sorted(map(str, di)) == sorted(map(str, ['inf', 0, 1, 2]))
    flat = lambda classes: set().union(*[set(c) for c in classes])
    res['B2_image_lines_equal_class5_lines'] = flat(img) == flat(nets[5])
    res['B2_image_parallel_classes_equal_class5_classes'] = set(img) == set(nets[5])
    res['B2_image_class_map_pandiagonal_to_class5_coordinate'] = [
        [j for j in range(4) if img[i] == nets[5][j]] for i in range(4)]
    res['B2_image_lines_equal_class6_lines'] = flat(img) == flat(nets[6])
    res['B2_unsheared_pandiagonal_equals_class5_literally'] = flat(pand) == flat(nets[5])
    res['B2_image_equals_any_maximal_class_0_4'] = any(flat(img) == flat(nets[i]) for i in range(5))

    # F1: aid only
    strong, affine_strong, rays_hist = 0, 0, {}
    nonaffine_examples = []
    for mu in itertools.permutations(range(Q)):
        if len({(mu[t] + t) % Q for t in range(Q)}) != Q or len({(mu[t] - t) % Q for t in range(Q)}) != Q:
            continue
        strong += 1
        a = (mu[1] - mu[0]) % Q
        is_aff = all(mu[t] == (mu[0] + a * t) % Q for t in range(Q))
        affine_strong += is_aff
        if not is_aff and len(nonaffine_examples) < 3:
            nonaffine_examples.append(mu)
        # exact ray count: phi_ij ~ phi_i'j' iff t -> t*j + i*mu(t) - (t*j' + i'*mu(t)) is constant mod 7
        keys = set()
        for i in range(Q):
            for j in range(Q):
                f = [(t * j + i * mu[t]) % Q for t in range(Q)]
                keys.add(tuple((v - f[0]) % Q for v in f))
        rays_hist[len(keys)] = rays_hist.get(len(keys), 0) + 1
        # exact ONB checks (sum of 7 seventh roots vanishes iff exponents form a bijection)
        def exps(i, j, i2, j2):
            return {(t * (j2 - j) + (i2 - i) * mu[t]) % Q for t in range(Q)}
        cells_lines = [[(x, y) for y in range(Q)] for x in range(Q)] + [[(x, y) for x in range(Q)] for y in range(Q)]
        cells_lines += [[(x, (x + b) % Q) for x in range(Q)] for b in range(Q)]
        cells_lines += [[(x, (b - x) % Q) for x in range(Q)] for b in range(Q)]
        assert all(len(exps(i, j, i2, j2)) == Q for line in cells_lines
                   for (i, j), (i2, j2) in itertools.combinations(line, 2)), mu
    res['F1_aid_strong_complete_mappings_Z7'] = strong
    res['F1_aid_affine_strong_complete_mappings_Z7'] = affine_strong
    res['F1_aid_expected_affine_count_a_in_{2,3,4,5}_times_7'] = 4 * Q
    res['F1_aid_nonaffine_examples'] = nonaffine_examples
    res['F1_aid_fourier_PQLS7_ray_count_histogram'] = {str(k): v for k, v in sorted(rays_hist.items())}
    res['F1_aid_all_line_ONB_checks_exact'] = True
    res['F1_aid_note'] = ('Computed consistency aid, not a premise: every Huang-Li-type Fourier PQLS(7) from a strong '
                          'complete mapping of Z_7 has the ray count shown; any non-affine strong complete mapping '
                          'would have produced a 49-ray PQLS(7) contradicting Corollary 2.')
    required = [k for k in res if k.startswith(('B1_', 'B2_', 'B3_', 'B4_')) and isinstance(res[k], bool)]
    expected_false = {'B2_image_lines_equal_class6_lines', 'B2_unsheared_pandiagonal_equals_class5_literally',
                      'B2_image_equals_any_maximal_class_0_4'}
    res['all_bridge_checks_pass'] = res['sha_matches_expected'] and all(
        (not res[k]) if k in expected_false else res[k] for k in required)
    json.dump(res, sys.stdout, indent=1, sort_keys=False)
    sys.stdout.write('\n')
    return 0 if res['all_bridge_checks_pass'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
