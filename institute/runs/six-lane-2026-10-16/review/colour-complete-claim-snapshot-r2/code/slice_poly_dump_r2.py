"""Standalone r2 of code/slice_poly.py + code/slice_poly_dump.py (Codex review item 3): no lane imports.

Builds the 12 Sylvester minors (dropped index 0..3; P1, P2, P3 = leading principal minors of the
remaining 3x3 block) of
    Mpoly = 5 Phi (2 diag(m) - S2) + 3 m m^T,
    d_s = w_s mu^s,  Phi = sum_s d_s,  m = sum_s d_s s,  S2 = sum_s d_s s s^T  (homogeneous degree 10),
over the 36 spectra s = (s_{-1,-1}, s_{-1,1}, s_{1,-1}, s_{1,1}) (entry sum 5, both row sums and both
column sums >= 1), w_s = 5!/prod s_k!.  Serialises exactly like evidence/slice_minors_rainbow.json.
Writes NO files.  Modes:
    --stdout          print the canonical JSON to stdout
    --compare PATH    byte-compare the canonical JSON with PATH (exit 1 on mismatch)
Per-minor statistics and the sha256 of the canonical JSON go to stderr.  python-flint 0.9.0 used.
"""
import sys, json, hashlib, itertools, math
import flint


def spectra():
    out = []
    for a, b, c in itertools.product(range(6), repeat=3):
        d = 5 - a - b - c
        if d < 0:
            continue
        if min(a + b, c + d) >= 1 and min(a + c, b + d) >= 1:
            out.append((a, b, c, d))
    return out


S = spectra()
if len(S) != 36:
    raise SystemExit('spectrum count != 36')
W = [math.factorial(5) // math.prod(math.factorial(x) for x in s) for s in S]
if sum(W) != 900:
    raise SystemExit('sum of weights != 900')
ctx = flint.fmpz_mpoly_ctx.get(('x', 'y', 'z', 'w'), 'degrevlex')
zero = ctx.from_dict({})
mono = lambda s: ctx.from_dict({tuple(s): 1})
Phi = sum((w * mono(s) for s, w in zip(S, W)), zero)
m = [sum((w * s[k] * mono(s) for s, w in zip(S, W)), zero) for k in range(4)]
S2 = [[sum((w * s[k] * s[l] * mono(s) for s, w in zip(S, W)), zero) for l in range(4)] for k in range(4)]
M = [[5 * Phi * ((2 * m[k] if k == l else 0) - S2[k][l]) + 3 * m[k] * m[l] for l in range(4)] for k in range(4)]
for k in range(4):
    if sum(M[k], zero) != 0:
        raise SystemExit('Mpoly 1 != 0')
out = {'variables': ['mu_{-1,-1}', 'mu_{-1,1}', 'mu_{1,-1}', 'mu_{1,1}'],
       'matrix': '5 Phi (2 diag m - S2) + 3 m m^T', 'minors': {}}
allpos = True
for drop in range(4):
    keep = [k for k in range(4) if k != drop]
    A = [[M[i][j] for j in keep] for i in keep]
    P1 = A[0][0]
    P2 = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    P3 = (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
          + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))
    for name, P in (('P1', P1), ('P2', P2), ('P3', P3)):
        terms = sorted(([list(map(int, e)), int(c)] for e, c in zip(P.monoms(), P.coeffs())))
        pos = all(c > 0 for _, c in terms)
        allpos &= pos
        out['minors'][f'drop{drop}_{name}'] = {'n_terms': len(terms), 'all_coefficients_positive': pos, 'terms': terms}
        print(f'drop{drop}_{name}: terms={len(terms)} min_coeff={min(c for _, c in terms)} '
              f'max_coeff={max(c for _, c in terms)} all_positive={pos}', file=sys.stderr)
out['all_minors_all_coefficients_positive'] = bool(allpos)
s = json.dumps(out, sort_keys=True)
print('canonical sha256', hashlib.sha256(s.encode()).hexdigest(), 'bytes', len(s), 'all_positive', allpos, file=sys.stderr)
if '--stdout' in sys.argv:
    sys.stdout.write(s)
if '--compare' in sys.argv:
    path = sys.argv[sys.argv.index('--compare') + 1]
    same = open(path, 'rb').read() == s.encode()
    print('compare with', path, ':', 'IDENTICAL' if same else 'DIFFERENT', file=sys.stderr)
    if not same:
        raise SystemExit(1)
if not allpos:
    raise SystemExit(1)
