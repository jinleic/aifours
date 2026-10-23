"""DESK EVIDENCE, NOT PROOF. Independent stdlib enumeration for property-form T16 (overlay section 1).

Model: U[k,i] = <Q1(0,k), Q1(i,0)>, k,i = 0..7, is unitary with U[:,0] = e_0, so only the 7x7 block on
coordinates k = 1..7 (pattern rows) and column-0 cells i = 1..7 (pattern columns) matters. From the T16
hypotheses ONLY, the support pattern of that block satisfies these necessary conditions:
  H1  column i=1 has support exactly A = {1,2,3} (SB2 hypothesis for Q1 at (1,0));
      every column i has 1..3 nonzeros (unit vector; column-degree bound from the row-0 frame);
  H2  every coordinate row k has 1..3 nonzeros (unitary rows are nonzero; row-degree bound, column-0 frame);
  H3  two distinct columns never share exactly one coordinate, and two distinct rows never share exactly one
      column (a single nonzero summand cannot vanish: orthogonality of distinct columns / rows of U);
  H4  every connected component of the bipartite support graph has as many rows as columns (rank balance).
Residual moves acting on the pattern: sigma in Sym(A) x Sym(B) on coordinates (B = {4,5,6,7}) and a common
permutation of rows 2..7 of the squares (= permutation of pattern columns 2..7); square relabelling does not
touch U. ROWLEX key of a column-0 cell: (c in supp for c = 0..7), coordinate 0 most significant, False < True,
ascending non-strict (gram_a.py 248-270 as quoted in the pinned imports).
The script enumerates every multiset of six columns for i = 2..7 satisfying H1-H4 (patterns are compared
after the ROWLEX sort, so multisets suffice), then checks whether some sigma maps the sorted list onto one of
the 16 lists parsed from the pinned template-cover snapshot, and compares those 16 lists with the pinned
weakened-manifest supports. Inputs are SHA-checked snapshot copies; the result JSON is created exclusively.
"""
import hashlib
import itertools
import json
import math
import resource
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TPL = HERE / 'snapshot/TPL__K5_COLUMN0_TEMPLATE_COVER.r1.md'
TPL_SHA = '1ae1c81d5c2982ecf23b7a3f881e79786576bbed21efc456ba5b427b53907d9a'
WMAN = HERE / 'snapshot/WMAN__MANIFEST.json'
WMAN_SHA = '355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74'
OUT = HERE / 'desk/t16_enum.result.json'

A = frozenset({1, 2, 3})
B = frozenset({4, 5, 6, 7})
COORDS = tuple(range(1, 8))


def sha(b):
    return hashlib.sha256(b).hexdigest()


def key(S):
    return tuple(c in S for c in range(8))


def fmt(S):
    return ''.join(str(c) for c in sorted(S))


def parse_tpl(text):
    lines = text.split('\n')                      # 1-based line n is lines[n-1]
    bnames = ['B1=I4', 'B2=K22+I2', 'B3=K22+K22', 'B4=K33+I1', 'B5=(K33-e)+I1', 'B6=K44-matching']
    cnames = ['C1=I3', 'C2=K22+I1', 'C3=K33-e', 'C4=K33']
    blists, clists = [], []
    for n, name in zip(range(88, 94), bnames):
        f = [x.strip() for x in lines[n - 1].split('|')]
        assert f[1] == name, (n, f)
        blists.append([frozenset(int(ch) for ch in tok) for tok in f[2].split(';')])
    assert '123;123 for P0' in lines[95 - 1] and '23;123 for P1' in lines[95 - 1], lines[94]
    for n, name in zip(range(101, 105), cnames):
        f = [x.strip() for x in lines[n - 1].split('|')]
        assert f[1] == name, (n, f)
        clists.append([frozenset(int(ch) for ch in tok) for tok in f[2].split(';')])
    tails = {'P0': [A, A], 'P1': [frozenset({2, 3}), A]}
    out = {}
    for p in ('P0', 'P1'):
        for b, bl in enumerate(blists, start=1):
            out[f'{p}-B{b}'] = bl + tails[p]
    for c, cl in enumerate(clists, start=1):
        out[f'P2-C{c}'] = cl
    return out


def passes(cols):
    """cols: list of 7 frozensets (i = 1..7). Check H1-H4 fully (independent of the pruning below)."""
    if cols[0] != A or any(not (1 <= len(S) <= 3) or not S <= set(COORDS) for S in cols):
        return False
    for S, T in itertools.combinations(cols, 2):
        if len(S & T) == 1:
            return False
    rows = {k: frozenset(i for i, S in enumerate(cols) if k in S) for k in COORDS}
    if any(not (1 <= len(r) <= 3) for r in rows.values()):
        return False
    for r1, r2 in itertools.combinations(rows.values(), 2):
        if len(r1 & r2) == 1:
            return False
    return all(nr == nc for nr, nc, _e, _d in components(cols))


def components(cols):
    parent = {}

    def find(x):
        while parent.setdefault(x, x) != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i, S in enumerate(cols):
        for k in S:
            parent[find(('c', i))] = find(('r', k))
    groups = {}
    for i in range(len(cols)):
        groups.setdefault(find(('c', i)), set()).add(('c', i))
    for k in COORDS:
        groups.setdefault(find(('r', k)), set()).add(('r', k))
    out = []
    for g in groups.values():
        cs = [x[1] for x in g if x[0] == 'c']
        rs = [x[1] for x in g if x[0] == 'r']
        e = sum(len(cols[i]) for i in cs)
        degs = tuple(sorted([len(cols[i]) for i in cs] + [sum(1 for i in cs if k in cols[i]) for k in rs]))
        out.append((len(rs), len(cs), e, degs))
    return out


def ctype(nr, nc, e, degs):
    table = {(1, 1, 1): 'K11', (2, 2, 4): 'K22', (3, 3, 8): 'K33-e', (3, 3, 9): 'K33', (4, 4, 12): 'K44-PM'}
    t = table.get((nr, nc, e))
    if t == 'K44-PM' and set(degs) != {3}:
        return 'OTHER'
    return t or 'OTHER'


def main():
    t0 = time.time()
    tpl_raw, wman_raw = TPL.read_bytes(), WMAN.read_bytes()
    assert sha(tpl_raw) == TPL_SHA and sha(wman_raw) == WMAN_SHA, 'snapshot pin'
    tpl = parse_tpl(tpl_raw.decode())
    tpl_sorted_ok = {cid: all(key(x) <= key(y) for x, y in zip(L, L[1:])) for cid, L in tpl.items()}
    tpl_pass = {cid: passes([A] + L) for cid, L in tpl.items()}
    wman = {x['id']: [frozenset(S) for S in x['supports_row2to7']] for x in json.loads(wman_raw)['cases']}
    tpl_vs_wman = {cid: (cid in wman and wman[cid] == L) for cid, L in tpl.items()}
    tpl_index = {tuple(key(S) for S in L): cid for cid, L in tpl.items()}

    # candidate columns i = 2..7: H1 size bound and H3 against column 1 (= A) only, then sorted by ROWLEX key
    opts = [frozenset(c) for r in (1, 2, 3) for c in itertools.combinations(COORDS, r)]
    opts = sorted((S for S in opts if len(S & A) != 1), key=key)

    sigmas = []
    for pa in itertools.permutations(sorted(A)):
        for pb in itertools.permutations(sorted(B)):
            m = dict(zip(sorted(A), pa)); m.update(zip(sorted(B), pb))
            sigmas.append(m)
    assert len(sigmas) == 144

    passing, labelled, unmatched = [], 0, []
    hits, orbit_rep, orbit_hit = Counter(), {}, {}
    type_hist = Counter()
    pruned_nodes = 0

    def rec(start, chosen, deg):
        nonlocal pruned_nodes, labelled
        pruned_nodes += 1
        if len(chosen) == 6:
            cols = [A] + chosen
            if not passes(cols):
                return
            passing.append(chosen[:])
            mult = Counter(chosen)
            labelled += math.factorial(6) // math.prod(math.factorial(v) for v in mult.values())
            for nr, nc, e, d in components(cols):
                type_hist[ctype(nr, nc, e, d)] += 1
            images = []
            for m in sigmas:
                img = tuple(sorted((key(frozenset(m[c] for c in S)) for S in chosen)))
                images.append(img)
            rep = min(images)
            matched = sorted({tpl_index[im] for im in images if im in tpl_index})
            orbit_rep.setdefault(rep, matched)
            if matched:
                hits.update(matched)
            else:
                unmatched.append([fmt(S) for S in chosen])
            return
        for j in range(start, len(opts)):
            S = opts[j]
            if any(len(S & T) == 1 for T in chosen):
                continue
            nd = dict(deg)
            ok = True
            for k in S:
                nd[k] = nd.get(k, 0) + 1
                if nd[k] > 3:
                    ok = False
            if not ok:
                continue
            chosen.append(S)
            rec(j, chosen, nd)
            chosen.pop()

    rec(0, [], {k: 1 for k in A})
    orbit_lists = {fmt_rep: v for fmt_rep, v in ((str(k), v) for k, v in orbit_rep.items())}
    one_to_one = (len(orbit_rep) == 16 and all(len(v) == 1 for v in orbit_rep.values())
                  and sorted(v[0] for v in orbit_rep.values()) == sorted(tpl))
    # negative control: dropping any single list must leave some passing pattern unmatched
    drop_detects = {}
    for cid in tpl:
        drop_detects[cid] = any(v == [cid] for v in orbit_rep.values())
    ru = resource.getrusage(resource.RUSAGE_SELF)
    result = {
        'kind': 'desk evidence, not proof: T16 support-pattern enumeration from stated hypotheses H1-H4',
        'script_sha256': sha(Path(__file__).read_bytes()),
        'inputs': {'TPL_snapshot_sha256': TPL_SHA, 'WMAN_snapshot_sha256': WMAN_SHA},
        'tpl_lists': {cid: ';'.join(fmt(S) for S in L) for cid, L in tpl.items()},
        'tpl_lists_rowlex_sorted': all(tpl_sorted_ok.values()),
        'tpl_lists_satisfy_H1_H4': all(tpl_pass.values()),
        'tpl_lists_equal_weakened_manifest_supports': all(tpl_vs_wman.values()) and len(wman) == 16,
        'candidate_column_supports_after_H1_and_H3_vs_A': len(opts),
        'search_nodes': pruned_nodes,
        'passing_sorted_multisets': len(passing),
        'passing_labelled_patterns_columns_2_to_7': labelled,
        'sigma_group_size': len(sigmas),
        'orbits_under_SymA_x_SymB': len(orbit_rep),
        'all_passing_patterns_map_into_16_lists': not unmatched,
        'unmatched_patterns_first_20': unmatched[:20],
        'unmatched_count': len(unmatched),
        'tpl_lists_hit_by_some_pattern': sorted(hits),
        'orbit_to_list_bijection': one_to_one,
        'negative_control_each_list_needed': drop_detects,
        'component_type_histogram_over_passing_multisets': dict(type_hist),
        'orbit_matches': orbit_lists,
        'runtime_seconds': round(time.time() - t0, 3),
        'maxrss_bytes_darwin': ru.ru_maxrss,
    }
    with OUT.open('x') as fh:
        json.dump(result, fh, indent=1)
        fh.write('\n')
    print(json.dumps({k: result[k] for k in ('passing_sorted_multisets', 'passing_labelled_patterns_columns_2_to_7',
                                            'orbits_under_SymA_x_SymB', 'all_passing_patterns_map_into_16_lists',
                                            'orbit_to_list_bijection', 'tpl_lists_equal_weakened_manifest_supports',
                                            'tpl_lists_satisfy_H1_H4', 'tpl_lists_rowlex_sorted',
                                            'component_type_histogram_over_passing_multisets', 'runtime_seconds')}))


if __name__ == '__main__':
    main()
