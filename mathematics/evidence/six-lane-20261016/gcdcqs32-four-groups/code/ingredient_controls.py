#!/usr/bin/env python3
"""README E10: intended-reason mutation controls for code/check_ingredients.py (stdlib).
Every mutated file is written (exclusive create) and RETAINED in OUTDIR; each must be rejected with
the intended failure category.  Usage: ingredient_controls.py FG.json FDH.txt OUTDIR"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lane_guard  # noqa: F401,E402
from lane_guard import fresh_dir, xopen  # noqa: E402


def run(kind, path):
    r = subprocess.run([sys.executable, os.path.join(HERE, "check_ingredients.py"), kind, path],
                       capture_output=True, text=True)
    return r.returncode, r.stdout.strip()


def main():
    fgp, fdhp, out = sys.argv[1:4]
    fresh_dir(out)
    res = {}
    fg = json.load(open(fgp))

    def fgmut(name, f, pat):
        d = json.loads(json.dumps(fg))
        f(d)
        p = os.path.join(out, f"fg_{name}.json")
        with xopen(p) as fh:
            json.dump(d, fh)
        rc, msg = run("fg", p)
        res[f"fg_{name}"] = {"rc": rc, "msg": msg, "as_intended": rc == 1 and re.search(pat, msg) is not None}

    def swap_point(d):
        t = d["T"][0]
        q = next(p for p in range(16) if p not in t)
        d["T"][0] = sorted(t[:-1] + [q])

    fgmut("T_point_swapped", swap_point, r"STEINER3")
    fgmut("T_block_dropped", lambda d: d["T"].pop(5), r"STEINER3")
    fgmut("B_line_replaced", lambda d: d["B"].__setitem__(0, sorted(d["T"][0][:4])), r"STEINER2|STEINER3")
    fgmut("T_block_size4", lambda d: d["T"].__setitem__(1, d["T"][1][:4]), r"T: a block of size")
    fgmut("group_size3", lambda d: d["groups"].__setitem__(0, d["groups"][0][:3]), r"GROUPS")
    L = open(fdhp).read().split("\n")

    def fdhmut(name, f, pat):
        M = list(L)
        f(M)
        p = os.path.join(out, f"fdh_{name}.txt")
        with xopen(p) as fh:
            fh.write("\n".join(M))
        rc, msg = run("fdh", p)
        res[f"fdh_{name}"] = {"rc": rc, "msg": msg, "as_intended": rc == 1 and re.search(pat, msg) is not None}

    bstart = L.index("BLOCKS") + 1
    pstart = next(i for i, l in enumerate(L) if l.startswith("POINT"))

    def drop_block(M):
        del M[bstart + 3]

    def dup_block(M):
        M.insert(bstart + 1, M[bstart])

    def same_group(M):
        b = [int(z) for z in M[bstart].split()]
        b[1] = b[0] + 1 if b[0] % 8 != 7 else b[0] - 1
        M[bstart] = " ".join(map(str, sorted(b)))

    def move_triple(M):
        # move the first triple of CLASS 0 at POINT 0 into CLASS 1 at POINT 0
        c0 = pstart + 1
        c1 = next(i for i in range(c0 + 1, len(M)) if M[i].startswith("CLASS 1"))
        t = M.pop(c0 + 1)
        M.insert(c1, t)

    def drop_point(M):
        last = max(i for i, l in enumerate(M) if l.startswith("POINT"))
        del M[last:]
        M.append("")

    fdhmut("block_dropped", drop_block, r"COVERAGE")
    fdhmut("block_duplicated", dup_block, r"repeated block|COVERAGE")
    fdhmut("block_meets_group_twice", same_group, r"meets a group twice")
    fdhmut("triple_moved_between_classes", move_triple, r"FRAME")
    fdhmut("point_section_dropped", drop_point, r"COMPLETENESS")
    base = {"fg": run("fg", fgp), "fdh": run("fdh", fdhp)}
    rec = {"unmutated": base, "results": res, "as_intended": sum(r["as_intended"] for r in res.values()),
           "total": len(res)}
    with xopen(os.path.join(out, "control-results.json")) as fh:
        json.dump(rec, fh, indent=1)
    print(f"{rec['as_intended']}/{rec['total']} as intended; unmutated: {base}")
    for n, r in res.items():
        print(n, r["as_intended"], "|", r["msg"][:90])
    return 0 if rec["as_intended"] == rec["total"] else 1


if __name__ == "__main__":
    sys.exit(main())
