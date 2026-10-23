#!/usr/bin/env python3
"""README §3 controls: intended-reason mutations of a Format S or Format D certificate (stdlib).  Every mutated
file is retained in OUTDIR (new); each must make BOTH routes fail, each for the intended reason (regex on the
route-1 failure message and on the route-2 output line).  Usage: mutations_fmt.py CERT OUTDIR"""
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lane_guard  # noqa: F401,E402
from lane_guard import fresh_dir, xopen  # noqa: E402


def toks(s):
    return s.split("#", 1)[0].split()


def index(L):
    """block line indices, sections: list of (header idx, kind, label, [(class idx, [triple idx])])"""
    blocks, secs, state = [], [], "head"
    for i, s in enumerate(L):
        t = toks(s)
        if not t:
            continue
        if t[0] == "BLOCKS":
            state = "blocks"
        elif t[0] in ("POINT", "STEMPOINT"):
            state = "sec"
            secs.append((i, t[0], int(t[1]), []))
        elif t[0] in ("CLASS", "FRAME", "PC"):
            secs[-1][3].append((i, []))
        elif state == "blocks" and len(t) == 4:
            blocks.append(i)
        elif state == "sec" and len(t) == 3:
            secs[-1][3][-1][1].append(i)
    return blocks, secs


def ints(L, i):
    return [int(z) for z in toks(L[i])]


def mutations(L, fmt):
    blocks, secs = index(L)
    out = {}

    def mut(name, py, c, f):
        M = list(L)
        f(M)
        out[name] = ("\n".join(M), py, c)

    mut("drop_block", r"^COVERAGE", r"COVERAGE|BLOCK", lambda M: M.__setitem__(blocks[5], ""))
    mut("duplicate_block", r"^BLOCK: .*repeated", r"BLOCK", lambda M: M.__setitem__(blocks[7], M[blocks[3]]))
    gsec = [s for s in secs if s[1] == "POINT"]
    x, cls = gsec[1][2], gsec[1][3]

    def move_conflict(M):
        c1 = {p for i in cls[1][1] for p in ints(L, i)}
        i = next(i for i in cls[0][1] if set(ints(L, i)) & c1)
        M[i] = ""
        M[cls[1][0]] = M[cls[1][0]] + "\n" + L[i]
    # v2 (after the 16:48 T0 run): in Format D the class that LOST the triple is reported first by route 1
    reason = r"COLOURING: .*not disjoint" if fmt == "S" else r"CLASS: .*(not disjoint|not a parallel class)"
    mut("move_triple_into_clashing_class", reason, r"COLOURING|CLASS", move_conflict)

    def delete_triple(M):
        M[cls[2][1][0]] = ""
    reason = r"COLOURING: .*not the derived design" if fmt == "S" else r"CLASS: .*(not a parallel class|do not cover)"
    # v2: route 2 reports a missing derived triple under COMPLETENESS ("lists k-1 derived triples, but k blocks")
    mut("delete_triple", reason, r"COLOURING|CLASS|COMPLETENESS: .*derived triples", delete_triple)

    def nonblock(M):
        i = cls[3][1][0]
        t = ints(L, i)
        used = {p for j in cls[3][1] for p in ints(L, j)}
        others = [p for j in cls[3][1] if j != i for p in ints(L, j)]
        # replace one point by an unused point of the same group class region: keep disjointness, break blockness
        for q in sorted(set(range(10 ** 4)) - used - {x}):
            cand = sorted([t[0], t[1], q])
            if q not in others and cand != sorted(t):
                M[i] = " ".join(map(str, cand))
                return
    reason = r"is not a block" if fmt == "S" else r"(is not a block|not a parallel class)"
    mut("non_derived_triple", reason, r"COLOURING|CLASS", nonblock)
    mut("drop_last_section", r"^COMPLETENESS", r"COMPLETENESS",
        lambda M: [M.__setitem__(i, "") for i in range(secs[-1][0], len(M))])
    if fmt == "S":
        ssec = [s for s in secs if s[1] == "STEMPOINT"]
        head = next(i for i, s in enumerate(L) if toks(s)[:1] == ["COLOURS"])
        mut("colours_header_plus_one", r"^PARAM", r"PARAM",
            lambda M: M.__setitem__(head, "COLOURS " + str(int(toks(L[head])[1]) + 1)))
        hf = next(i for i, s in enumerate(L) if toks(s)[:1] == ["HOLEFREE"])
        mut("holefree_header_plus_one", r"^PARAM", r"PARAM",
            lambda M: M.__setitem__(hf, "HOLEFREE " + str(int(toks(L[hf])[1]) + 1)))
        hdr = next(toks(s) for s in L if toks(s)[:1] == ["GCDCQS"])
        n, g = int(hdr[2]), int(hdr[3])
        gl = next(i for i, s in enumerate(L) if toks(s) == ["GROUPS"])
        groups = [[int(z) for z in toks(L[gl + 1 + k])] for k in range(n)]
        sl = next(i for i, s in enumerate(L) if toks(s) == ["STEM"])
        stem = [int(z) for z in toks(L[sl + 1])] if toks(L[sl + 1]) and toks(L[sl + 1])[0] != "BLOCKS" else []
        gid = {p: k for k, G in enumerate(groups) for p in G}
        if ssec:
            fcls = ssec[0][3]

            def frame_move(M):
                i = fcls[0][1][0]
                M[i] = ""
                M[fcls[1][0]] = M[fcls[1][0]] + "\n" + L[i]
            mut("frame_triple_moved", r"^FRAME", r"FRAME", frame_move)

            def frame_relabel(M):
                k = int(toks(L[fcls[0][0]])[1])
                M[fcls[0][0]] = f"FRAME {(k + 1) % n}"
            mut("frame_label_wrong", r"^FRAME: .*not a parallel class", r"FRAME", frame_relabel)

            def two_stems(M):
                b = ints(L, blocks[-1])
                keep = [p for p in b if p not in stem][:2]
                M[blocks[-1]] = " ".join(map(str, sorted(keep + stem)))
            mut("block_with_both_stems", r"^COVERAGE", r"COVERAGE|BLOCK", two_stems)

        def kempe(M):
            # Kempe swap between a hole-avoiding class A and a non-avoiding class B at x: both stay partial
            # parallel classes and the listed triples are unchanged, but A gains hole triples while B keeps
            # some -> only the number of hole-avoiding classes (t - 1) is wrong.
            hole = (set(groups[gid[x]]) | set(stem)) - {x}
            T = {i: set(ints(L, i)) for _, tl in cls for i in tl}
            avoid = [c for c in cls if not any(T[i] & hole for i in c[1])]
            nonav = [c for c in cls if any(T[i] & hole for i in c[1])]
            for A in avoid:
                for B in nonav:
                    items = A[1] + B[1]
                    comp_of, cid = {}, 0
                    for i0 in items:
                        if i0 in comp_of:
                            continue
                        stack, comp_of[i0] = [i0], cid
                        while stack:
                            u = stack.pop()
                            for w in items:
                                if w not in comp_of and T[w] & T[u]:
                                    comp_of[w] = cid
                                    stack.append(w)
                        cid += 1
                    hb = [i for i in B[1] if T[i] & hole]
                    for c in sorted({comp_of[i] for i in hb}):
                        moved_hole = [i for i in hb if comp_of[i] == c]
                        if len(moved_hole) < len(hb):
                            for i in items:
                                if comp_of[i] == c:
                                    M[i] = ""
                            inA = [L[i] for i in items if comp_of[i] == c and i in B[1]]
                            inB = [L[i] for i in items if comp_of[i] == c and i in A[1]]
                            M[A[0]] = "\n".join([M[A[0]]] + inA)
                            M[B[0]] = "\n".join([M[B[0]]] + inB)
                            return
            raise RuntimeError("no Kempe swap available")
        mut("kempe_swap_fewer_avoiding_classes", r"^HOLEFREE", r"HOLEFREE", kempe)
    else:
        def relabel_frame_or_pc(M):
            t = toks(L[cls[0][0]])
            if t[0] == "FRAME":
                gx = None
                M[cls[0][0]] = f"FRAME {(int(t[1]) + 1) % 5}"
            else:
                M[cls[0][0]] = "PC 9999"
        mut("class_label_wrong", r"^(CLASS|FORMAT)", r"CLASS|FORMAT", relabel_frame_or_pc)

        def meets_group_twice(M):
            b = ints(L, blocks[11])
            gl = next(i for i, s in enumerate(L) if toks(s) == ["GROUPS"])
            groups = []
            j = gl + 1
            while toks(L[j]) != ["BLOCKS"]:
                groups.append([int(z) for z in toks(L[j])])
                j += 1
            gid = {p: k for k, G in enumerate(groups) for p in G}
            q = next(p for p in groups[gid[b[0]]] if p != b[0])
            M[blocks[11]] = " ".join(map(str, sorted([q, b[1], b[2], b[0]])))
        mut("block_meets_group_twice", r"^BLOCK: .*meets a group twice", r"BLOCK", meets_group_twice)
    return out


def main():
    cert, outdir = sys.argv[1], sys.argv[2]
    L = open(cert).read().split("\n")
    fmt = "S" if toks(next(s for s in L if toks(s)))[0] == "GCDCQS" else "D"
    r1 = os.path.join(HERE, "check_gcdcqs_s.py" if fmt == "S" else "check_gdd34.py")
    r2 = os.path.join(HERE, "bin", "check_gcdcqs_s_c" if fmt == "S" else "check_gdd34_c")
    fresh_dir(outdir)
    res, ok = {}, True
    for name, (text, pre, cre) in mutations(L, fmt).items():
        p = os.path.join(outdir, name + ".txt")
        with xopen(p) as fh:
            fh.write(text)
        a = subprocess.run([sys.executable, r1, p], capture_output=True, text=True)
        ar = json.loads(a.stdout)
        b = subprocess.run([r2, p], capture_output=True, text=True)
        a_ok = a.returncode == 1 and ar["result"] == "FAIL" and re.search(pre, ar.get("failure", "")) is not None
        b_ok = b.returncode == 1 and b.stdout.startswith("FAIL") and re.search(cre, b.stdout) is not None
        res[name] = {"file": p, "sha256": hashlib.sha256(text.encode()).hexdigest(), "route1": ar.get("failure", ar["result"]),
                     "route1_as_intended": a_ok, "route2": b.stdout.strip(), "route2_as_intended": b_ok}
        ok &= a_ok and b_ok
    base1 = json.loads(subprocess.run([sys.executable, r1, cert], capture_output=True, text=True).stdout)["result"]
    base2 = subprocess.run([r2, cert], capture_output=True, text=True).stdout.strip()
    summ = {"certificate": cert, "certificate_sha256": hashlib.sha256(open(cert, "rb").read()).hexdigest(),
            "format": fmt, "unmutated_route1": base1, "unmutated_route2": base2, "mutations": len(res),
            "as_intended": sum(v["route1_as_intended"] and v["route2_as_intended"] for v in res.values()), "results": res}
    with xopen(os.path.join(outdir, "mutation-results.json")) as fh:
        json.dump(summ, fh, indent=1)
    print(f"{summ['as_intended']}/{summ['mutations']} as intended; unmutated {base1} / {base2}")
    for k, v in res.items():
        if not (v["route1_as_intended"] and v["route2_as_intended"]):
            print("NOT AS INTENDED", k, v["route1"], "|", v["route2"])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
