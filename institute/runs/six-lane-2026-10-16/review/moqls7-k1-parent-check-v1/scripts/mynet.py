"""mynet.py (parent moqls7-k1-parent-check-v1): independent helpers for 4-nets of order 7 given as 49 points with
4 line labels each (class c line of point q has label net[q][c]). Written from the definitions; imports no lane code."""
import json

N = 7


def load_nets(classfile):
    with open(classfile) as f:
        data = json.load(f)
    return [[tuple(int(v) for v in q) for q in c["net"]] for c in data["classes"]], data


def check_net(net):
    """True iff net is a 4-net of order 7: 4 parallel classes, each a partition of the 49 points into 7 lines of size
    7 (labels 0..6), and two lines of different classes meet in exactly one point."""
    if len(net) != 49 or any(len(q) != 4 for q in net):
        return False, "shape"
    for c in range(4):
        for b in range(N):
            if sum(1 for q in net if q[c] == b) != 7:
                return False, "class %d label %d size" % (c, b)
        if any(not (0 <= q[c] < N) for q in net):
            return False, "label range"
    for c in range(4):
        for d in range(c + 1, 4):
            pairs = {(q[c], q[d]) for q in net}
            if len(pairs) != 49:
                return False, "classes %d,%d not orthogonal" % (c, d)
    if len(set(net)) != 49:
        return False, "repeated point"
    return True, "ok"


def lines(net):
    return [(c, b, [p for p in range(49) if net[p][c] == b]) for c in range(4) for b in range(N)]


def frame_allowed(net):
    """Frame: line l0 = class-0 line with label 0; its point with class-1 label j carries e_j. For p off l0, the class-1,2,3
    lines through p meet l0 at 3 points r (distinct); p is collinear with each, so coordinate label(r) is excluded."""
    frame = [p for p in range(49) if net[p][0] == 0]
    label = {p: net[p][1] for p in frame}
    allowed = {}
    for p in range(49):
        if p in label:
            allowed[p] = frozenset([label[p]])
            continue
        excl = set()
        for c in (1, 2, 3):
            hits = [r for r in frame if net[r][c] == net[p][c]]
            assert len(hits) == 1
            excl.add(label[hits[0]])
        assert len(excl) == 3
        allowed[p] = frozenset(range(N)) - excl
    return frame, label, allowed


def pattern_violations(net, supp, label=None, allowed=None):
    """Evaluate F1-F4 (and frame/allowed if given) directly on a support pattern supp: point -> set of coordinates."""
    bad = []
    if label is not None:
        for p, k in label.items():
            if set(supp[p]) != {k}:
                bad.append(("frame", p))
    for p in range(49):
        if not supp[p]:
            bad.append(("F1", p))
        if allowed is not None and not set(supp[p]) <= set(allowed[p]):
            bad.append(("allowed", p))
    for c, b, pts in lines(net):
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                if len(set(supp[pts[i]]) & set(supp[pts[j]])) == 1:
                    bad.append(("F2", c, b, pts[i], pts[j]))
        for k in range(N):
            cov = [p for p in pts if k in supp[p]]
            if not cov:
                bad.append(("F3", c, b, k))
            elif len(cov) == 1 and len(supp[cov[0]]) != 1:
                bad.append(("F4", c, b, k, cov[0]))
    return bad
