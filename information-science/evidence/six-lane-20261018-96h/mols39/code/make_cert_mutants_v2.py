#!/usr/bin/env python3
"""make_cert_mutants_v2.py (ContinueCFR21, mols39 lane; written 2026-10-19; NOT executed when frozen; stdlib only).
v2 supersedes v1 (sha256 12d89e5c388f191d2c7544ec95cf821b8ae41ae8cce4fea9b39448dff32a212d, never executed). Only change: --outdir must be an EXISTING directory (the
supervisor's output root, which may already hold supervisor files); the ten mutants and manifest.json are
written into it as flat regular files (exclusive create), and no directory is created. Mutations, intended checks
and serialisation are unchanged.
Preregistered negative controls for the independent Lemma U certificate checker (review/cert_checker/). Reads a
VALID certificate (format evidence/lemmaU-certificate-format-v1.md, sha256 1b6537a4...) produced for the exact anchor
and writes deterministic mutants into an EXISTING directory (exclusive creates), plus manifest.json. It imports neither the
producer nor the checker. Each mutant is serialised exactly like the producer (json.dumps(sort_keys=True,
separators=(",", ":")) + "\\n").
Mutants and the intended first failing check of the format file (section 4):
  nc0_identity           unchanged copy                                            -> VALID (bytes identical to input)
  nc1_basis_flip         basis[0][pivot of witness record 0] += 1 (mod 3)           -> check 2
  nc2_pivot_swap         swap the "pivot" values of witness records 0 and 1         -> check 4
  nc3_rainbow_swap       smallest rainbow idx <-> smallest failure idx (fibre 0)    -> check 5
  nc4_failure_delete     delete the first failure entry                            -> check 6
  nc5_wrong_anchor_hash  anchor_sha256 := --other-sha256 (DM21 raw)                 -> check 1
  nc6_failure_wrong_fibre first failure whose point has a passing fibre: its j := smallest passing fibre -> check 6
  nc7_witness_coef       witness record 0, first combination coefficient 1 <-> 2    -> check 4
  nc8_witness_drop       delete the last witness record                            -> check 0
  nc9_anchor_mutation    anchor_sha256 := --mut-anchor-sha256 (frozen mutated anchor raw, run with that raw) -> check 1
CLI: --cert CERT --cert-sha256 HEX --anchor RAW --anchor-sha256 HEX --other-sha256 HEX --mut-anchor-sha256 HEX
     --outdir EXISTING_DIR
Exit 0 on success (one JSON summary line); 2 on any input problem (one JSON line, nothing or a partial set written)."""
import sys, os, json, copy, hashlib, argparse


def dump(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n"


def main(argv):
    ap = argparse.ArgumentParser(add_help=False)
    for name in ("--cert", "--cert-sha256", "--anchor", "--anchor-sha256", "--other-sha256", "--mut-anchor-sha256", "--outdir"):
        ap.add_argument(name, required=True)
    try:
        a = ap.parse_args(argv)
    except SystemExit:
        print(json.dumps({"status": "BAD_INPUT", "reason": "bad command line"}))
        return 2
    if not os.path.isdir(a.outdir):
        print(json.dumps({"status": "BAD_INPUT", "reason": "--outdir is not an existing directory"}))
        return 2
    cb = open(a.cert, "rb").read()
    if hashlib.sha256(cb).hexdigest() != a.cert_sha256:
        print(json.dumps({"status": "INPUT_PIN_MISMATCH", "reason": "certificate sha256"}))
        return 2
    rb = open(a.anchor, "rb").read()
    if hashlib.sha256(rb).hexdigest() != a.anchor_sha256:
        print(json.dumps({"status": "INPUT_PIN_MISMATCH", "reason": "anchor sha256"}))
        return 2
    cert = json.loads(cb)
    if cert.get("anchor_sha256") != a.anchor_sha256 or dump(cert).encode("utf-8") != cb:
        print(json.dumps({"status": "BAD_INPUT", "reason": "certificate not canonical or not for this anchor"}))
        return 2
    n, q, k, U, dim = cert["n"], cert["q"], cert["k"], cert["U"], cert["dim"]
    rows = [[int(t) % n for t in ln.split()] for ln in rb.decode("ascii").splitlines() if ln.strip()]
    E = [[(rows[x][c] - rows[0][c]) % n for c in range(n)] for x in range(k)]
    fibres = []
    for x in range(k):
        for y in range(x + 1, k):
            buckets = [[] for _ in range(q)]
            for c in range(n):
                buckets[((E[x][c] % q) - (E[y][c] % q)) % q].append(c)
            for t in range(q):
                fibres.append((x, y, buckets[t]))

    def var(x, c):
        return None if (x == 0 or c == 0) else (x - 1) * (n - 1) + (c - 1)

    def point(idx):
        z = []
        rem = idx
        for _ in range(dim):
            z.append(rem % 3)
            rem //= 3
        z.reverse()
        A = [0] * U
        for zr, b in zip(z, cert["basis"]):
            if zr:
                A = [(av + zr * bv) % 3 for av, bv in zip(A, b)]
        return A

    def fibre_ok(A, j):
        x, y, cols = fibres[j]
        vals = set()
        for c in cols:
            vx, vy = var(x, c), var(y, c)
            vals.add(((0 if vx is None else A[vx]) - (0 if vy is None else A[vy])) % 3)
        return len(vals) == 3

    muts = []
    m = copy.deepcopy(cert)
    muts.append(("nc0_identity", m, None, "unchanged copy"))
    m = copy.deepcopy(cert)
    p0 = m["rank_witness"][0]["pivot"]
    m["basis"][0][p0] = (m["basis"][0][p0] + 1) % 3
    muts.append(("nc1_basis_flip", m, 2, "basis[0][%d] += 1" % p0))
    m = copy.deepcopy(cert)
    m["rank_witness"][0]["pivot"], m["rank_witness"][1]["pivot"] = m["rank_witness"][1]["pivot"], m["rank_witness"][0]["pivot"]
    muts.append(("nc2_pivot_swap", m, 4, "pivots of witness records 0 and 1 swapped"))
    m = copy.deepcopy(cert)
    r0 = m["rainbow"][0]
    f0 = m["failures"][0][0]
    m["rainbow"] = sorted([i for i in m["rainbow"] if i != r0] + [f0])
    m["failures"] = sorted([e for e in m["failures"] if e[0] != f0] + [[r0, 0]], key=lambda e: e[0])
    muts.append(("nc3_rainbow_swap", m, 5, "rainbow idx %d listed as failure, failure idx %d listed as rainbow" % (r0, f0)))
    m = copy.deepcopy(cert)
    dropped = m["failures"].pop(0)
    muts.append(("nc4_failure_delete", m, 6, "failure entry %r deleted" % (dropped,)))
    m = copy.deepcopy(cert)
    m["anchor_sha256"] = a.other_sha256
    muts.append(("nc5_wrong_anchor_hash", m, 1, "anchor_sha256 replaced by the DM21 raw sha256"))
    m = copy.deepcopy(cert)
    target = None
    for pos, (idx, j) in enumerate(m["failures"]):
        A = point(idx)
        if fibre_ok(A, j):
            print(json.dumps({"status": "BAD_INPUT", "reason": "input certificate failure entry %d is wrong" % pos}))
            return 2
        for jj in range(len(fibres)):
            if fibre_ok(A, jj):
                target = (pos, idx, j, jj)
                break
        if target:
            break
    if target is None:
        print(json.dumps({"status": "BAD_INPUT", "reason": "no failure entry with a passing fibre"}))
        return 2
    m["failures"][target[0]] = [target[1], target[3]]
    muts.append(("nc6_failure_wrong_fibre", m, 6, "failure idx %d: fibre %d replaced by passing fibre %d" % (target[1], target[2], target[3])))
    m = copy.deepcopy(cert)
    c0 = m["rank_witness"][0]["combination"][0]
    c0[1] = 3 - c0[1]
    muts.append(("nc7_witness_coef", m, 4, "witness record 0, combination entry for equation %d: coefficient flipped" % c0[0]))
    m = copy.deepcopy(cert)
    m["rank_witness"].pop()
    muts.append(("nc8_witness_drop", m, 0, "last witness record deleted"))
    m = copy.deepcopy(cert)
    m["anchor_sha256"] = a.mut_anchor_sha256
    muts.append(("nc9_anchor_mutation", m, 1, "anchor_sha256 = mutated anchor raw (run with --anchor = that raw)"))
    manifest = {"source_cert": os.path.abspath(a.cert), "source_cert_sha256": a.cert_sha256, "anchor_sha256": a.anchor_sha256,
                "generator_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(), "mutants": []}
    for name, obj, check, desc in muts:
        text = dump(obj)
        path = os.path.join(a.outdir, name + ".cert.json")
        with open(path, "x") as fh:
            fh.write(text)
        manifest["mutants"].append({"item": name, "path": path, "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                                    "intended_first_failed_check": check,
                                    "intended_verdict": "VALID" if check is None else "INVALID", "description": desc})
    mp = os.path.join(a.outdir, "manifest.json")
    with open(mp, "x") as fh:
        fh.write(json.dumps(manifest, indent=1, sort_keys=True) + "\n")
    print(json.dumps({"status": "OK", "manifest": mp, "manifest_sha256": hashlib.sha256(open(mp, "rb").read()).hexdigest(),
                      "mutants": len(muts)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
