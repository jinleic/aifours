#!/usr/bin/env python3
"""nets.py: nets of order 7 for lane moqls7-maximum (stdlib only).

A k-net of order 7 is given by its point coordinates: net[q] = (l_0(q), ..., l_{k-1}(q)), where l_c(q) in 0..6 is the
label of the line of parallel class c through point q. lines(net) returns, for every (class, label), the list of its
points in increasing order.
"""
import itertools
import json

P = 7


def desarguesian_net(dirs):
    """Points (x, y) of AG(2,7), index q = 7x + y. Direction 'inf': the line label is x. Direction m (int): the line
    label is y - m x mod 7."""
    net = []
    for x in range(P):
        for y in range(P):
            net.append(tuple(x if d == "inf" else (y - d * x) % P for d in dirs))
    return net


def net_from_mols(*squares):
    """Rows, columns and the given Latin squares; point q = 7r + c."""
    return [tuple([r, c] + [L[r][c] for L in squares]) for r in range(P) for c in range(P)]


def lines(net):
    k = len(net[0])
    out = []
    for cl in range(k):
        for b in range(P):
            out.append([q for q in range(len(net)) if net[q][cl] == b])
    return out


def is_net(net):
    """Every class partitions the 49 points into 7 lines of 7; two points share at most one line."""
    k = len(net[0])
    if len(net) != P * P:
        return False
    for cl in range(k):
        if sorted(sum(1 for q in net if q[cl] == b) for b in range(P)) != [P] * P:
            return False
    for q1, q2 in itertools.combinations(range(len(net)), 2):
        if sum(1 for c in range(k) if net[q1][c] == net[q2][c]) > 1:
            return False
    return True


def cross_ratio_class(dirs):
    """Cross-ratio of 4 points of PG(1,7) in F_7 (inf allowed), returned as the orbit set under S_4."""
    def cr(a, b, c, d):
        def diff(u, v):
            return None if u == "inf" or v == "inf" else (u - v) % P

        def inv(x):
            return pow(x, P - 2, P)
        terms = [(c, a), (d, b), (c, b), (d, a)]
        num, den = 1, 1
        for k, (u, v) in enumerate(terms):
            dv = diff(u, v)
            if dv is None:
                continue
            if k < 2:
                num = num * dv % P
            else:
                den = den * dv % P
        return num * inv(den) % P
    vals = {cr(*perm) for perm in itertools.permutations(dirs)}
    return sorted(vals)


def load_classes(path):
    """Read the classification output of code/mols7_classify (JSON lines)."""
    out = []
    for line in open(path):
        d = json.loads(line)
        if "class" in d:
            out.append(d)
    return out


if __name__ == "__main__":
    for dirs in (["inf", 0, 1, 2], ["inf", 0, 1, 3]):
        n = desarguesian_net(dirs)
        print(dirs, "net:", is_net(n), "cross-ratio orbit:", cross_ratio_class(dirs))
