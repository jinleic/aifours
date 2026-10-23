#!/usr/bin/env python3
"""Retained intended-reason SW controls, plus independent Z5 expansion/action audit."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECKER = HERE / "check_sw_independent.py"
WITNESS = HERE / "sw25-parent-inputs-v1/sw25-16-witness-v1.sw"
EXPECTED = "bfadf44596bc5138106432690bf507a8ff9c36cd3c40eb8eeb08195a9b2d4ab0"


def encode(M, w):
    return (f"SW {len(M)} {w}\n" + "".join(" ".join(map(str, r)) + "\n" for r in M)).encode()


def paley(q):
    squares = {a * a % q for a in range(1, q)}
    M = [[0] * (q + 1) for _ in range(q + 1)]
    for a in range(q):
        M[0][a + 1] = M[a + 1][0] = 1
        for b in range(q):
            M[a + 1][b + 1] = 0 if a == b else (1 if (a - b) % q in squares else -1)
    return M


def main():
    out = HERE / "sw25-parent-controls-v1"
    out.mkdir(exist_ok=False)
    data = WITNESS.read_bytes()
    if hashlib.sha256(data).hexdigest() != EXPECTED:
        raise ValueError("pinned witness changed")
    W = [[int(x) for x in r.split()] for r in data.decode().splitlines()[1:]]
    H = [[1]]
    for _ in range(4):
        H = [r + r for r in H] + [r + [-x for x in r] for r in H]
    fixtures = []

    def add(name, raw, n, w, expected, sha=None):
        f = out / (name + ".sw")
        with f.open("xb") as h:
            h.write(raw)
        fixtures.append({"name": name, "file": f.name, "n": n, "w": w,
                         "sha256": sha or hashlib.sha256(raw).hexdigest(),
                         "actual_sha256": hashlib.sha256(raw).hexdigest(), "expected": expected})

    add("target", data, 25, 16, "VALID")
    add("paley6", encode(paley(5), 5), 6, 5, "VALID")
    add("paley14", encode(paley(13), 13), 14, 13, "VALID")
    add("sylvester16", encode(H, 16), 16, 16, "VALID")
    perm = list(range(25))
    perm[0], perm[1] = perm[1], perm[0]
    add("simultaneous-permutation", encode([[W[perm[i]][perm[j]] for j in range(25)] for i in range(25)], 16), 25, 16, "VALID")
    signs = [-1] + [1] * 24
    add("signed-conjugation", encode([[signs[i] * W[i][j] * signs[j] for j in range(25)] for i in range(25)], 16), 25, 16, "VALID")
    add("global-negation", encode([[-x for x in r] for r in W], 16), 25, 16, "VALID")
    add("row-only-permutation", encode([W[i] for i in perm], 16), 25, 16, "SYMMETRY")
    M = [r[:] for r in W]
    M[0][0] = 0
    add("wrong-weight", encode(M, 16), 25, 16, "WEIGHT")
    M = [r[:] for r in W]
    M[0][0] *= -1
    add("symmetric-sign-flip", encode(M, 16), 25, 16, "ORTHO")
    M = [r[:] for r in W]
    M[0][0] = 2
    add("nonternary", encode(M, 16), 25, 16, "ENTRIES")
    lines = data.splitlines(keepends=True)
    add("missing-row", b"".join(lines[:-1]), 25, 16, "FORMAT")
    add("extra-row", data + lines[1], 25, 16, "FORMAT")
    add("extra-token", b"".join([lines[0], lines[1].rstrip(b"\n") + b" 0\n"] + lines[2:]), 25, 16, "FORMAT")
    add("double-space", data.replace(b"1 0", b"1  0", 1), 25, 16, "FORMAT")
    add("crlf", data.replace(b"\n", b"\r\n"), 25, 16, "FORMAT")
    add("missing-final-lf", data[:-1], 25, 16, "FORMAT")
    add("wrong-header", data.replace(b"SW 25 16", b"SW 25 15", 1), 25, 16, "HEADER")
    add("wrong-expected-n", data, 24, 16, "HEADER")
    add("wrong-digest", data, 25, 16, "DIGEST", "0" * 64)
    add("trailing-text", data + b"unexpected\n", 25, 16, "FORMAT")
    add("noncanonical-numeric-token", data.replace(b"\n1 ", b"\n01 ", 1), 25, 16, "ENTRIES")
    runs = []
    for f in fixtures:
        for optimize in (False, True):
            cmd = [sys.executable] + (["-O"] if optimize else []) + ["-B", str(CHECKER),
                   str(f["n"]), str(f["w"]), str(out / f["file"]), f["sha256"]]
            r = subprocess.run(cmd, capture_output=True, text=True)
            ok = (r.returncode == 0 and json.loads(r.stdout)["verdict"] == "VALID") if f["expected"] == "VALID" else (
                r.returncode == 1 and r.stderr.startswith("INVALID " + f["expected"] + ":"))
            runs.append({"fixture": f["name"], "optimized": optimize, "rc": r.returncode,
                         "expected": f["expected"], "ok": ok, "stdout": r.stdout, "stderr": r.stderr})
    seeds = [[W[5 * i][5 * j:5 * j + 5] for j in range(5)] for i in range(5)]
    expanded = [[seeds[i // 5][j // 5][(j % 5 - i % 5) % 5] for j in range(25)] for i in range(25)]
    expanded_bytes = encode(expanded, 16)
    with (out / "cyclic-seed.json").open("x") as f:
        json.dump({"circulant_convention": "block(i,j)[r,c]=seed[i][j][(c-r) mod5]", "seed": seeds}, f, indent=1)
        f.write("\n")
    with (out / "expanded.sw").open("xb") as f:
        f.write(expanded_bytes)
    pi = [5 * (i // 5) + (i % 5 + 1) % 5 for i in range(25)]
    action_bad = [(i, j) for i in range(25) for j in range(25) if W[pi[i]][pi[j]] != W[i][j]]
    nonaction_bad = [(i, j) for i in range(25) for j in range(25) if W[perm[i]][perm[j]] != W[i][j]]
    quotient = [[sum(b) for b in row] for row in seeds]
    quotient_square = [[sum(quotient[i][k] * quotient[k][j] for k in range(5)) for j in range(5)] for i in range(5)]
    structure = {"seed_expansion_byte_equal": expanded_bytes == data,
                 "expanded_sha256": hashlib.sha256(expanded_bytes).hexdigest(),
                 "generator": pi, "generator_order": 5, "entry_tests": 625,
                 "action_failures": action_bad, "nonautomorphism_transposition_failures": len(nonaction_bad),
                 "quotient": quotient, "quotient_square": quotient_square}
    passed = all(r["ok"] for r in runs) and structure["seed_expansion_byte_equal"] and not action_bad and bool(nonaction_bad)
    record = {"recorded_at_pt": subprocess.check_output(["date", "+%Y-%m-%d %H:%M:%S %Z"], text=True).strip(),
              "driver_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "checker_sha256": hashlib.sha256(CHECKER.read_bytes()).hexdigest(),
              "fixtures": fixtures, "runs": runs, "structure": structure,
              "verdict": "PASS" if passed else "FAIL"}
    with (out / "result.json").open("x") as f:
        json.dump(record, f, indent=1)
        f.write("\n")
    print(json.dumps({"verdict": record["verdict"], "fixtures": len(fixtures), "runs": len(runs),
                      "structure": structure}))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
