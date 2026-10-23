#!/usr/bin/env python3
"""Write the two altered LKTS(57) certificates used as rejection controls.

Both start from the frozen raw file (SHA-256 checked) and change it by exact line edits:

* swap: in KTS 0, CLASS 0 the rows "0 19 38" and "1 7 11" become "0 11 19" and "1 7 38".
  CLASS 0 is still a partition of the 57 points, but KTS 0 now covers the pair {0, 11} twice
  (also by "0 11 14" in CLASS 1) and misses {0, 38}, {19, 38}, {1, 11}, {7, 11}.  Because an
  LKTS uses every triple exactly once, the two new triples necessarily also occur in other
  systems (KTS 43 and KTS 48), so cross-system distinctness fails as well.
* dupsys: the CLASS blocks of KTS 54 are replaced by a verbatim copy of those of KTS 0.  Every
  system is still a genuine KTS(57), but KTS 0 and KTS 54 share all their blocks.

Usage: python3 make_controls.py FROZEN_RAW OUTDIR
"""
import hashlib
import pathlib
import sys

FROZEN = "09a9d8ca0602ed28541e170ada7f096871311c29fd4515b6fea3e25f72b05f09"


def sections(lines):
    """Map system index -> (start, end) line range of its CLASS blocks (after the KTS line)."""
    out, cur = {}, None
    for k, ln in enumerate(lines):
        tok = ln.split()
        if tok[:1] == ["KTS"]:
            if cur is not None:
                out[cur] = (out[cur][0], k)
            cur = int(tok[1])
            out[cur] = (k + 1, None)
    out[cur] = (out[cur][0], len(lines) if lines[-1] else len(lines) - 1)
    return out


def main():
    raw_path, outdir = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    raw = raw_path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != FROZEN:
        raise SystemExit("frozen SHA-256 mismatch")
    lines = raw.decode("ascii").split("\n")
    sec = sections(lines)
    outdir.mkdir(parents=True, exist_ok=True)

    # swap control
    s0, e0 = sec[0]
    swap = list(lines)
    edits = {"0 19 38": "0 11 19", "1 7 11": "1 7 38"}
    # KTS 0 starts with CLASS 0 and its first two rows are exactly the two rows to change
    assert swap[s0] == "CLASS 0", swap[s0]
    for k in (s0 + 1, s0 + 2):
        assert swap[k] in edits, swap[k]
        swap[k] = edits[swap[k]]
    swap[0] = "# CONTROL (altered, invalid on purpose): swap 38<->11 in KTS 0 CLASS 0 rows 0,1"
    (outdir / "lkts57_control_swap.txt").write_text("\n".join(swap))

    # duplicated-system control
    s54, e54 = sec[54]
    dup = lines[:s54] + lines[s0:e0] + lines[e54:]
    dup[0] = "# CONTROL (altered, invalid on purpose): KTS 54 classes replaced by a copy of KTS 0"
    (outdir / "lkts57_control_dupsys.txt").write_text("\n".join(dup))

    for name in ("lkts57_control_swap.txt", "lkts57_control_dupsys.txt"):
        data = (outdir / name).read_bytes()
        print(name, hashlib.sha256(data).hexdigest(), len(data))


if __name__ == "__main__":
    main()
