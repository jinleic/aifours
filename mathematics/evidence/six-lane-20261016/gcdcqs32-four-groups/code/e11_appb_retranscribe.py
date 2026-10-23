#!/usr/bin/env python3
"""README E11a: independent re-transcription of the Tan-Zhou Appendix B mcDSQS(32) (stdlib only).

No code is shared with tz_appb_mcdsqs32.py.  Two routes, each compared with the pinned E0 JSON:
  G  Ghostscript txtwrite text of PDF pages 23-24: base blocks = every 4-set between the anchor
     sentences "Now, we construct a cyclic SQS(32)" and "The above cyclic SQS(32) is an mcDSQS(32)";
     part rows = the 3-set lines after "each part form a PPC" up to the Appendix C heading, taken
     two printed rows per part (the two-row groups seen on the rendered page).
  L  arXiv v1 LaTeX source: the tabular after "\\mathrm{SQS}(32)$ on point set" (base blocks, with the
     \\underline / double \\underline marks), and the tabular after "mcDSQS}(32)$. We list below",
     split into parts at the blank source lines (an independent grouping signal).
Checks: equal ordered base-block lists and equal ordered part lists (each part a set of triples);
underline marks equal the blocks whose Z32-orbit has length 16 (single) / 8 (double).
Usage: e11_appb_retranscribe.py GS_TEXT TEX_FILE E0_JSON OUT.json"""
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import xopen  # noqa: E402

GS_SET = re.compile(r"\{\s*(\d+(?:\s*,\s*\d+)*)\s*\}")
TEX_SET = re.compile(r"\\\{([^\\{}]*)\\\}")


def nums(s):
    return tuple(sorted(int(z.strip()) for z in s.split(",")))


def route_g(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    a = next(i for i, s in enumerate(lines) if "Now, we construct a cyclic SQS(32)" in s)
    b = next(i for i, s in enumerate(lines) if "The above cyclic SQS(32) is an mcDSQS(32)" in s)
    c = next(i for i, s in enumerate(lines) if "each part form a PPC" in s)
    d = next(i for i, s in enumerate(lines) if re.match(r"\s*C\s+The", s))
    assert a < b < c < d
    base = [nums(m) for s in lines[a:b] for m in GS_SET.findall(s)]
    rows = [[nums(m) for m in GS_SET.findall(s)] for s in lines[c + 1:d]]
    rows = [r for r in rows if r]
    assert all(len(t) == 3 for r in rows for t in r), "non-triple in part rows"
    assert len(rows) % 2 == 0, f"{len(rows)} part rows (odd)"
    parts = [rows[k] + rows[k + 1] for k in range(0, len(rows), 2)]
    return base, parts, {"anchor_lines": [a + 1, b + 1, c + 1, d + 1], "part_rows": len(rows)}


def route_l(path):
    lines = open(path, encoding="latin-1").read().split("\n")
    a = next(i for i, s in enumerate(lines) if "cyclic $\\mathrm{SQS}(32)$ on point set" in s)
    b = next(i for i in range(a, len(lines)) if "\\end{tabular}" in lines[i])
    c = next(i for i, s in enumerate(lines) if "$\\mathrm{SQS}(32)$ is an $\\mathrm{mcDSQS}(32)$" in s)
    d = next(i for i in range(c, len(lines)) if "\\end{tabular}" in lines[i])
    assert a < b < c < d
    base, single, double = [], [], []
    for s in lines[a + 1:b]:
        s = s.split("%")[0]
        for m in re.finditer(r"(\\underline\{\\underline\{)?(\\underline\{)?" + TEX_SET.pattern, s):
            blk = nums(m.group(3))
            base.append(blk)
            if m.group(1):
                double.append(blk)
            elif m.group(2):
                single.append(blk)
    parts, cur = [], []
    for s in lines[c + 1:d]:
        s = s.split("%")[0]
        if not s.strip():
            if cur:
                parts.append(cur)
                cur = []
            continue
        cur += [nums(m) for m in TEX_SET.findall(s)]
    if cur:
        parts.append(cur)
    assert all(len(t) == 3 for P in parts for t in P), "non-triple in parts"
    return base, parts, {"source_lines": [a + 1, b + 1, c + 1, d + 1], "single_underlined": single,
                         "double_underlined": double}


def orbit_len(blk, v=32):
    return len({tuple(sorted((p + i) % v for p in blk)) for i in range(v)})


def canon(base, parts):
    return [list(b) for b in base], [sorted(list(t) for t in P) for P in parts]


def main():
    gs_p, tex_p, e0_p, out = sys.argv[1:5]
    sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()  # noqa: E731
    e0 = json.load(open(e0_p))
    e0_base = [tuple(sorted(b)) for b in e0["base_blocks"]]
    e0_parts = [[tuple(sorted(t)) for t in P] for P in e0["parts"]]
    gb, gp, ginfo = route_g(gs_p)
    lb, lp, linfo = route_l(tex_p)
    ref = canon(e0_base, e0_parts)
    res = {
        "inputs": {"gs_text": [gs_p, sha(gs_p)], "tex": [tex_p, sha(tex_p)], "e0_json": [e0_p, sha(e0_p)]},
        "route_G": {"base_blocks": len(gb), "parts": len(gp), "part_sizes": [len(P) for P in gp], **ginfo,
                    "base_equal_E0": canon(gb, gp)[0] == ref[0], "parts_equal_E0": canon(gb, gp)[1] == ref[1]},
        "route_L": {"base_blocks": len(lb), "parts": len(lp), "part_sizes": [len(P) for P in lp],
                    "source_lines": linfo["source_lines"],
                    "base_equal_E0": canon(lb, lp)[0] == ref[0], "parts_equal_E0": canon(lb, lp)[1] == ref[1],
                    "single_underlined": [list(b) for b in linfo["single_underlined"]],
                    "double_underlined": [list(b) for b in linfo["double_underlined"]]},
        "orbit_lengths": {" ".join(map(str, b)): orbit_len(b) for b in e0_base if orbit_len(b) != 32},
    }
    short16 = sorted(b for b in e0_base if orbit_len(b) == 16)
    short8 = sorted(b for b in e0_base if orbit_len(b) == 8)
    res["underlines_match_orbits"] = (sorted(linfo["single_underlined"]) == short16
                                      and sorted(linfo["double_underlined"]) == short8)
    ok = all([res["route_G"]["base_equal_E0"], res["route_G"]["parts_equal_E0"], res["route_L"]["base_equal_E0"],
              res["route_L"]["parts_equal_E0"], res["underlines_match_orbits"], len(gp) == 16, len(lp) == 16,
              len(gb) == 40, len(lb) == 40])
    res["result"] = "MATCH" if ok else "MISMATCH"
    with xopen(out) as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({k: res[k] for k in ("result", "underlines_match_orbits", "orbit_lengths")}))
    print("G:", {k: res["route_G"][k] for k in ("base_blocks", "parts", "base_equal_E0", "parts_equal_E0")})
    print("L:", {k: res["route_L"][k] for k in ("base_blocks", "parts", "base_equal_E0", "parts_equal_E0",
                                                 "single_underlined", "double_underlined")})
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
