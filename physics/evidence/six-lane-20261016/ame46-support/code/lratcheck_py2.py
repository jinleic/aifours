#!/usr/bin/env python3
"""lratcheck_py2.py: lratcheck_py.py with the hint-terminator assert replaced by an explicit error, so that
PYTHONOPTIMIZE cannot remove it (Codex v5 delta review m4). Otherwise byte-for-byte the same logic. Same author as
lratcheck.c, so not independent of it.

Usage: lratcheck_py.py formula.cnf proof.lrat
Semantics: for each added lemma, assign the negation of its literals; process the hints in order. A hint must be
falsified (success), or unit (its remaining literal is assigned). A hint that is already satisfied is reported as an
error unless --allow-satisfied is given, in which case it is skipped.
"""
import sys


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    allow_sat = "--allow-satisfied" in sys.argv
    cnf, proof = args
    clauses = {}
    with open(cnf) as fh:
        toks = []
        for line in fh:
            if line.startswith("c") or line.startswith("p"):
                continue
            toks.extend(int(t) for t in line.split())
    cid, cur = 1, []
    for t in toks:
        if t == 0:
            clauses[cid] = cur
            cid += 1
            cur = []
        else:
            cur.append(t)
    nsat = 0
    added = 0
    empty = False
    with open(proof) as fh:
        for line in fh:
            t = line.split()
            if not t:
                continue
            if t[1] == "d":
                for x in t[2:]:
                    x = int(x)
                    if x == 0:
                        break
                    if x not in clauses:
                        raise SystemExit("ERROR deleting unknown clause %d" % x)
                    del clauses[x]
                continue
            lid = int(t[0])
            z = t.index("0", 1)
            lits = [int(x) for x in t[1:z]]
            hints = [int(x) for x in t[z + 1:]]
            if not hints or hints[-1] != 0:
                raise SystemExit("ERROR missing hint terminator 0 in lemma %d" % lid)
            hints = hints[:-1]
            val = {}
            taut = False
            for l in lits:
                v = abs(l)
                want = -1 if l > 0 else 1          # make l false
                if v in val and val[v] != want:
                    taut = True
                val[v] = want
            ok = taut
            if not ok:
                for h in hints:
                    if h < 0:
                        raise SystemExit("ERROR RAT hint in lemma %d" % lid)
                    if h not in clauses:
                        raise SystemExit("ERROR unknown hint %d in lemma %d" % (h, lid))
                    unassigned = []
                    sat = False
                    for l in clauses[h]:
                        v = abs(l)
                        if v in val:
                            if (val[v] == 1) == (l > 0):
                                sat = True
                                break
                        else:
                            unassigned.append(l)
                    if sat:
                        if allow_sat:
                            nsat += 1
                            continue
                        raise SystemExit("ERROR hint %d satisfied in lemma %d" % (h, lid))
                    if not unassigned:
                        ok = True
                        break
                    if len(set(unassigned)) > 1:
                        raise SystemExit("ERROR hint %d not unit in lemma %d" % (h, lid))
                    l = unassigned[0]
                    val[abs(l)] = 1 if l > 0 else -1
            if not ok:
                raise SystemExit("ERROR lemma %d not implied" % lid)
            clauses[lid] = lits
            added += 1
            if not lits:
                empty = True
                break
    print("c lemmas %d, satisfied hints skipped %d" % (added, nsat))
    print("s VERIFIED" if empty else "s NOT VERIFIED (no empty clause)")


if __name__ == "__main__":
    main()
