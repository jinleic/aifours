import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[name] = '1'
import itertools, json, time
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from pathlib import Path

CASES = [
    [[1,2],[1,3],[2,3],[1,4],[2,4],[3,4,5]],
    [[1,2],[1,3],[1,4],[2,3,5],[2,4,5],[3,4,5]],
    [[1,2],[1,3],[2,4],[3,4],[2,3,5],[1,4,5]],
    [[1,2],[1,3],[2,4],[2,3,5],[1,4,5],[3,4,5]],
    [[1,2,3],[1,2,4],[1,3,4],[1,2,5],[1,3,5],[1,4,5]],
]

def access(minsets):
    minimal = [sum(1 << (i-1) for i in q) for q in minsets]
    qualified = [q for q in range(32) if any(q & a == a for a in minimal)]
    forbidden = [q for q in range(32) if q not in qualified]
    maximal = [f for f in forbidden if not any(f != g and f & g == f for g in forbidden)]
    return minimal, qualified, forbidden, maximal


def find_basis(case, m):
    _, qs, fs, maxfs = access(CASES[case-1])
    rows, lows, highs = [], [], []
    for f in maxfs:
        for p in range(32):
            if p & f == p:
                a = np.array([int(c & f == p) for c in range(32)])
                rows.append(np.r_[a, -a]); lows.append(0); highs.append(0)
    for q in qs:
        a = np.array([int(bool(c & q)) for c in range(32)])
        rows.append(np.r_[-a, a]); lows.append(1); highs.append(np.inf)
    rows.extend([np.r_[np.ones(32), np.zeros(32)], np.r_[np.zeros(32), np.ones(32)]])
    lows.extend([m,m]); highs.extend([m,m])
    t = time.monotonic()
    res = milp(np.zeros(64), integrality=np.ones(64), bounds=Bounds(0, m), constraints=LinearConstraint(np.array(rows), lows, highs), options={'time_limit':120,'threads':1})
    out = {'case':case, 'm':m, 'status':int(res.status), 'message':res.message, 'seconds':time.monotonic()-t}
    if res.x is not None:
        a = np.rint(res.x).astype(int)
        w = [c for c in range(32) for _ in range(int(a[c]))]
        b = [c for c in range(32) for _ in range(int(a[32+c]))]
        assert len(w) == len(b) == m
        assert all(sorted(c&f for c in w) == sorted(c&f for c in b) for f in fs)
        assert all(sum(bool(c&q) for c in b) >= sum(bool(c&q) for c in w)+1 for q in qs)
        out.update(white=w, black=b, verification='exact integer all forbidden and all qualified')
    return out

if __name__ == '__main__':
    out = []
    for case,m in [(1,6),(5,8)]:
        r = find_basis(case,m); out.append(r); print(json.dumps(r), flush=True)
    Path(__file__).with_name('basis_controls.json').write_text(json.dumps(out,indent=2)+'\n')
