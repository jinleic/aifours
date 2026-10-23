"""Exact (combinatorial) bound for enphased dual permutations.

For every permutation matrix P of order 9 that is dual (P^R a permutation matrix) and every enphasing
P_theta = sum_k e^{i theta_k} |p(k)><k|, the matrix P_theta^Gamma has the same support as P^Gamma (Gamma only moves
entries), so rank P_theta^Gamma <= term rank of supp(P^Gamma) (maximum matching).  If the term rank is <= 5, then
e_p(P_theta) <= 1 - (81/5 - 9)/72 = 9/10 by Cauchy-Schwarz (Theorem A argument).  Enphasing preserves duality
(P_theta^R has the same support pattern as P^R, a permutation, with unimodular entries).
Writes ../evidence/enphased_perms_exact.json
"""
import itertools
import json
import os
from collections import Counter


def realign_support(ones):
    """ones: set of (row, col) of a 9x9 0/1 matrix -> support of its realignment (source R)."""
    out = set()
    for (r, c) in ones:
        i, a = divmod(r, 3)
        j, b = divmod(c, 3)
        out.add((3 * i + j, 3 * a + b))
    return out


def ptrans_support(ones):
    out = set()
    for (r, c) in ones:
        i, a = divmod(r, 3)
        j, b = divmod(c, 3)
        out.add((3 * i + b, 3 * j + a))
    return out


def is_perm(ones):
    rows = Counter(r for r, _ in ones)
    cols = Counter(c for _, c in ones)
    return len(ones) == 9 and all(rows[k] == 1 for k in range(9)) and all(cols[k] == 1 for k in range(9))


def term_rank(ones):
    """maximum bipartite matching (Kuhn)."""
    adj = {r: [c for (rr, c) in ones if rr == r] for r in range(9)}
    match = {}

    def try_(r, seen):
        for c in adj[r]:
            if c in seen:
                continue
            seen.add(c)
            if c not in match or try_(match[c], seen):
                match[c] = r
                return True
        return False

    return sum(1 for r in range(9) if try_(r, set()))


def main():
    hist = Counter()
    n_dual = n_2u = 0
    max_tr_non2u = 0
    for p in itertools.permutations(range(9)):
        ones = {(p[k], k) for k in range(9)}
        if not is_perm(realign_support(ones)):
            continue
        n_dual += 1
        G = ptrans_support(ones)
        tdual = is_perm(G)
        tr = term_rank(G)
        hist[(tr, tdual)] += 1
        if tdual:
            n_2u += 1
        else:
            max_tr_non2u = max(max_tr_non2u, tr)
    out = {"dual_permutations": n_dual, "two_unitary_permutations": n_2u,
           "histogram (term rank of supp P^Gamma, T-dual)": {f"{k[0]},{k[1]}": v for k, v in sorted(hist.items())},
           "max term rank over non-2-unitary dual permutations": max_tr_non2u,
           "consequence": "every enphased non-2-unitary dual permutation (and its LU orbit) has rank U^Gamma <= "
                          f"{max_tr_non2u}, hence e_p <= 1 - (81/{max_tr_non2u} - 9)/72"}
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "enphased_perms_exact.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
