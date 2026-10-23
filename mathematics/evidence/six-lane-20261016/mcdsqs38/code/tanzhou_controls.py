#!/usr/bin/env python3
"""Positive controls: transcribe the cyclic mcDSQS(26) and mcDSQS(32) of Tan–Zhou
arXiv:2503.11934v1, Appendix B (lemma 3.4), from the lane-read text extraction, into MCDSQS
certificates (standard library only).

Source rows (1-based line numbers of the text file, sha256 checked):
  v=26: base blocks lines 1282-1286; colouring at 0 lines 1294-1319
  v=32: base blocks lines 1326-1332; colouring at 0 lines 1341-1372
Blocks = all Z_v translates of the base blocks (duplicates from short orbits merged).
Classes: the PDF prints each PPC ("part") as two consecutive rows; we group consecutive row
pairs.  The colouring at x is the translate by x of the printed colouring at 0 (the SQS is
cyclic), which is how the paper's statement "the above cyclic SQS is an mcDSQS" is read.
Usage: tanzhou_controls.py SOURCE_TXT OUTDIR
"""
import hashlib
import os
import re
import sys

SRC_SHA = "df52a8f11a46974eef129fa115bb3305831f7c8edc3e2102e4fd22c64c3c8164"
SPEC = {26: ((1282, 1286), (1294, 1319), 13), 32: ((1326, 1332), (1341, 1372), 16)}
SET = re.compile(r"\{\s*(\d+(?:\s*,\s*\d+)*)\s*\}")


def sets(line):
    return [tuple(int(x) for x in m.group(1).split(",")) for m in SET.finditer(line)]


def main(src, outdir):
    data = open(src, "rb").read()
    assert hashlib.sha256(data).hexdigest() == SRC_SHA, "source text hash mismatch"
    lines = data.decode().split("\n")   # newline-only numbering (the text contains form feeds)
    os.makedirs(outdir, exist_ok=True)
    for v, ((b0, b1), (c0, c1), ncol) in SPEC.items():
        base = [s for ln in range(b0, b1 + 1) for s in sets(lines[ln - 1])]
        assert all(len(b) == 4 for b in base)
        blocks = sorted({tuple(sorted((p + s) % v for p in b)) for b in base for s in range(v)})
        rows = [sets(lines[ln - 1]) for ln in range(c0, c1 + 1)]
        assert all(rows) and all(len(t) == 3 for r in rows for t in r)
        classes0 = [sorted(rows[2 * i] + rows[2 * i + 1]) for i in range(len(rows) // 2)]
        assert len(classes0) == ncol and len(rows) == 2 * ncol
        out = [f"# control: Tan-Zhou arXiv:2503.11934v1 Appendix B cyclic mcDSQS({v}); base blocks lines "
               f"{b0}-{b1}, colouring at 0 lines {c0}-{c1} (row pairs), translated to every point",
               f"MCDSQS {v}", f"COLOURS {ncol}", "BLOCKS"]
        out += [" ".join(map(str, b)) for b in blocks]
        for x in range(v):
            out.append(f"POINT {x}")
            for j, C in enumerate(classes0):
                out.append(f"CLASS {j}")
                out += [" ".join(map(str, t)) for t in sorted(
                    tuple(sorted((p + x) % v for p in t)) for t in C)]
        text = ("\n".join(out) + "\n").encode()
        path = os.path.join(outdir, f"tanzhou_mcdsqs{v}.txt")
        open(path, "wb").write(text)
        print(v, "base", len(base), "blocks", len(blocks), "class sizes", [len(C) for C in classes0],
              "sha256", hashlib.sha256(text).hexdigest())


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
