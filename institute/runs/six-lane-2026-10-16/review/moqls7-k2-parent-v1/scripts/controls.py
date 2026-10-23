#!/usr/bin/env python3
"""Controls for the parent K2 replay desk (review/moqls7-k2-parent-v1).

Usage: controls.py TAG SECTION [SECTION ...]   with SECTION in: transport checker noheavy mutate
Each control writes controls/TAG-NAME.json (exclusive). Outcomes are recorded as observed; the
expectations listed in each receipt are the task's, and 'matches_expectation' compares against them.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import k2lib as K  # noqa: E402

UNSAT4 = b"p cnf 2 4\n1 2 0\n1 -2 0\n-1 2 0\n-1 -2 0\n"
SAT3 = b"p cnf 2 3\n1 2 0\n1 -2 0\n-1 2 0\n"
UNIT = b"p cnf 1 1\n1 0\n"
EMPTY_CLAUSE = b"a\x00"            # binary DRAT: add the empty clause
VALID4 = b"a\x02\x00a\x00"         # binary DRAT: add unit clause (1), then the empty clause
NPAIR = 735                        # non-collinear cell pairs of a 3-net of order 7 (1176 - 21*21)


def log(msg):
    print("[%s] %s" % (K.now(), msg), flush=True)


def save(tag, name, rec):
    path = os.path.join(K.DESK, "controls", "%s-%s.json" % (tag, name))
    K.write_json_x(path, rec)
    log("%s: %s" % (name, json.dumps({k: rec.get(k) for k in ("outcome", "matches_expectation")})))


def run(tag, name, cnf, mine=2, **kw):
    cap = K.wait_for_capacity(log, mine=mine)
    if cap is None:
        return {"label": "%s-%s" % (tag, name), "capacity": None, "outcome": "UNKNOWN: capacity wait exceeded"}
    rec = K.pipeline("%s-%s" % (tag, name), cnf, **kw)
    rec["capacity"] = cap
    return rec


def summarize(rec):
    s = rec.get("children", {}).get("solver", {}).get("rc")
    return "solver_rc=%s checker_rc=%s status=%s verified=%s" % (
        s, rec.get("children", {}).get("checker", {}).get("rc"), rec.get("checker_status_lines"),
        rec.get("checker_verified"))


# ---------------------------------------------------------------- parent-side CNF utilities
def clause_lines(cnf):
    body = cnf[cnf.index(b"\n") + 1:]
    return [ln for ln in body.split(b"\n") if ln.strip() and not ln.startswith(b"c")]


def with_clauses(nv, lines):
    return b"p cnf %d %d\n" % (nv, len(lines)) + b"".join(ln + b"\n" for ln in lines)


def model_from_log(log_bytes):
    lits = []
    for ln in log_bytes.decode().split("\n"):
        if ln.startswith("v "):
            lits.extend(int(x) for x in ln[2:].split())
    if not lits or lits[-1] != 0:
        raise ValueError("no terminated model")
    return [x for x in lits[:-1]]


def evaluate(cnf, model):
    nv, ncl = K.cnf_header(cnf)
    val = {}
    for x in model:
        val[abs(x)] = x > 0
    missing = [v for v in range(1, nv + 1) if v not in val]
    unsat, count = 0, 0
    for ln in clause_lines(cnf):
        lits = [int(x) for x in ln.split()]
        if lits[-1] != 0:
            raise ValueError("unterminated clause")
        count += 1
        if not any(val.get(abs(x), False) == (x > 0) for x in lits[:-1]):
            unsat += 1
    return {"vars": nv, "clauses_header": ncl, "clauses_read": count, "unassigned_vars": len(missing),
            "falsified_clauses": unsat}


def net_lines(L):
    cells = [(i, j) for i in range(7) for j in range(7)]
    lines = [[(i, j) for j in range(7)] for i in range(7)] + [[(i, j) for i in range(7)] for j in range(7)]
    lines += [[c for c in cells if L[c[0]][c[1]] == s] for s in range(7)]
    return cells, lines


def g_index(L):
    """Parent's own numbering hypothesis: square a, pair p<q (row-major), non-collinear -> (a-1)*735+k+1."""
    cells, lines = net_lines(L)
    col = set()
    for l in lines:
        for p in l:
            for q in l:
                if p != q:
                    col.add((p, q))
    pairs = [(p, q) for i, p in enumerate(cells) for q in cells[i + 1:] if (p, q) not in col]
    assert len(pairs) == NPAIR, len(pairs)
    return pairs


VMAP_WRAPPER = r'''
import json, sys
sys.path.insert(0, sys.argv[1])
import gram_enc
L = json.loads(sys.stdin.read())
F, vmap = gram_enc.build(2, L, True, False, None)
sys.stdout.write(json.dumps(vmap))
'''


def encoder_a_vmap(L):
    import subprocess
    p = subprocess.run([K.PY, "-B", "-c", VMAP_WRAPPER, K.CODE], input=json.dumps(L).encode(),
                       capture_output=True, cwd=K.TMP, env=K.ENV)
    if p.returncode:
        raise RuntimeError(p.stderr.decode()[-1000:])
    return json.loads(p.stdout)


def semantic(L, model):
    """Evaluate the decoded g-model (parent numbering) against G1-free facts: per-square edge counts,
    G5 overlap and, per square and line, whether some off-line point has >= 3 neighbours on it (G4)."""
    cells, lines = net_lines(L)
    pairs = g_index(L)
    val = {abs(x): x > 0 for x in model}
    out = {}
    for a in (1, 2):
        adj = {c: set() for c in cells}
        for k, (p, q) in enumerate(pairs):
            if val.get((a - 1) * NPAIR + k + 1):
                adj[p].add(q)
                adj[q].add(p)
        heavy_fail = []
        for li, l in enumerate(lines):
            ls = set(l)
            if not any(len(adj[p] & ls) >= 3 for p in cells if p not in ls):
                heavy_fail.append(li)
        out["square%d" % a] = {"true_g_pairs": sum(len(v) for v in adj.values()) // 2,
                               "lines_without_heavy_point": heavy_fail,
                               "edges": sorted([list(p), list(q)] for p in cells for q in adj[p] if p < q)}
    both = sum(1 for k in range(NPAIR) if val.get(k + 1) and val.get(NPAIR + k + 1))
    out["g5_overlaps"] = both
    return out


def class0():
    rows = K.read_classes()
    key = rows[0][0]
    return key, K.decode_key(key)


def gen(enc, L, heavy):
    f = K.encode_A if enc == "A" else K.encode_B
    cnf, info = f(L, heavy)
    if cnf is None:
        raise RuntimeError("encoder failed: %s" % json.dumps(info))
    return cnf, info


def receipt_cnf(enc, c):
    with open(os.path.join(K.CERT, "k2%s_%d.json" % (enc, c))) as f:
        return json.load(f)["cnf_sha256"]


# ---------------------------------------------------------------- sections
def transport(tag):
    cases = [("T1-cadical-UNSAT4", UNSAT4, "cadical", True, 20), ("T2-kissat-UNSAT4", UNSAT4, "kissat", True, 20),
             ("T3-cadical-SAT3", SAT3, "cadical", False, 10), ("T4-kissat-SAT3", SAT3, "kissat", False, 10)]
    for name, cnf, solver, exp_ver, exp_rc in cases:
        rec = run(tag, name, cnf, solver=K.solver_argv(solver, 30), checker_seconds=60)
        rec["cnf_text"] = cnf.decode()
        rec["expectation"] = {"solver_rc": exp_rc, "checker_verified": exp_ver}
        got = rec.get("children", {}).get("solver", {}).get("rc")
        rec["matches_expectation"] = (got == exp_rc and rec.get("checker_verified") == exp_ver)
        rec["outcome"] = summarize(rec)
        save(tag, name, rec)
    rec = run(tag, "T5-parentproof-UNSAT4-valid", UNSAT4, mine=1, proof=VALID4, checker_seconds=60)
    rec["cnf_text"] = UNSAT4.decode()
    rec["proof_hex"] = VALID4.hex()
    rec["expectation"] = {"checker_verified": True}
    rec["matches_expectation"] = rec.get("checker_verified") is True
    rec["outcome"] = summarize(rec)
    save(tag, "T5-parentproof-UNSAT4-valid", rec)


def checker(tag):
    cases = [("Cb1-SATunit-emptyclause", UNIT, EMPTY_CLAUSE), ("Cb2-SAT3-emptyclause", SAT3, EMPTY_CLAUSE),
             ("Cc-UNSAT4-emptyproof", UNSAT4, b"")]
    for name, cnf, proof in cases:
        rec = run(tag, name, cnf, mine=1, proof=proof, checker_seconds=60)
        rec["cnf_text"] = cnf.decode()
        rec["proof_hex"] = proof.hex()
        rec["expectation"] = {"checker_status": "s NOT VERIFIED", "checker_verified": False}
        rec["matches_expectation"] = (rec.get("checker_verified") is False
                                      and "s NOT VERIFIED" in rec.get("checker_status_lines", [])
                                      and "s VERIFIED" not in rec.get("checker_status_lines", []))
        rec["outcome"] = summarize(rec)
        save(tag, name, rec)


def noheavy(tag):
    key, L = class0()
    vmap = encoder_a_vmap(L)
    pairs = g_index(L)
    mine = {"%d|%d,%d|%d,%d" % (a, p[0], p[1], q[0], q[1]): (a - 1) * NPAIR + k + 1
            for a in (1, 2) for k, (p, q) in enumerate(pairs)}
    numbering = {"parent_numbering_equals_encoderA_vmap": mine == vmap, "vmap_entries": len(vmap)}
    log("numbering check: %s" % numbering)
    for enc, solver in (("A", "cadical"), ("B", "kissat")):
        H, hinfo = gen(enc, L, True)
        N, ninfo = gen(enc, L, False)
        hl, nl = clause_lines(H), clause_lines(N)
        struct = {"heavy_cnf_sha256": K.sha_bytes(H), "heavy_matches_receipt": K.sha_bytes(H) == receipt_cnf(enc, 0),
                  "noheavy_cnf_sha256": K.sha_bytes(N), "heavy_header": K.cnf_header(H),
                  "noheavy_header": K.cnf_header(N), "noheavy_is_clause_prefix_of_heavy": hl[:len(nl)] == nl,
                  "heavy_family_clauses": len(hl) - len(nl),
                  "heavy_family_new_vars": K.cnf_header(H)[0] - K.cnf_header(N)[0]}
        log("%s structure: %s" % (enc, struct))
        name = "Ca-class0-%s-noheavy" % enc
        rec = run(tag, name, N, solver=K.solver_argv(solver, 900))
        rec["class"], rec["key"], rec["L"] = 0, key, L
        rec["encoder_runs"] = {"heavy": hinfo, "noheavy": ninfo}
        rec["structure"] = struct
        rec["numbering"] = numbering
        rec["expectation"] = {"solver_rc": 10, "checker_verified": False}
        srec = rec.get("children", {}).get("solver", {})
        if srec.get("rc") == 10:
            with open(os.path.join(K.DESK, rec["solver_log"]), "rb") as f:
                model = model_from_log(f.read())
            ev = evaluate(N, model)
            nv = K.cnf_header(N)[0]
            bits = bytearray((nv + 7) // 8)
            for x in model:
                if x > 0:
                    bits[(x - 1) // 8] |= 1 << ((x - 1) % 8)
            rec["model"] = {"literals": len(model), "true_vars": sum(1 for x in model if x > 0),
                            "bitmask_hex_var1_lsb": bits.hex(), "bitmask_sha256": K.sha_bytes(bytes(bits)),
                            "parent_clause_evaluation": ev, "semantic_parent_numbering": semantic(L, model)}
        rec["matches_expectation"] = (srec.get("rc") == 10 and rec.get("checker_verified") is False
                                      and rec.get("model", {}).get("parent_clause_evaluation", {}).get(
                                          "falsified_clauses") == 0)
        rec["outcome"] = summarize(rec)
        save(tag, name, rec)


def mutate(tag):
    key, L = class0()
    for enc, solver in (("A", "cadical"), ("B", "kissat")):
        H, hinfo = gen(enc, L, True)
        nv, ncl = K.cnf_header(H)
        hl = clause_lines(H)
        g5 = [i for i, ln in enumerate(hl) if len(ln.split()) == 3 and ln.split()[2] == b"0"
              and int(ln.split()[0]) < 0 and int(ln.split()[1]) == int(ln.split()[0]) - NPAIR
              and 1 <= -int(ln.split()[0]) <= NPAIR]
        target = b"-1 -%d 0" % (NPAIR + 1)
        hits = [i for i in g5 if hl[i] == target]
        if len(g5) != NPAIR or len(hits) != 1:
            raise RuntimeError("unexpected G5 family layout: %d members, %d target hits" % (len(g5), len(hits)))
        M = with_clauses(nv, hl[:hits[0]] + hl[hits[0] + 1:])
        pairs = g_index(L)
        info = {"heavy_cnf_sha256": K.sha_bytes(H), "heavy_matches_receipt": K.sha_bytes(H) == receipt_cnf(enc, 0),
                "g5_family_members_found": len(g5), "g5_block_first_last_index": [g5[0], g5[-1]],
                "dropped_clause": target.decode(), "dropped_clause_index": hits[0],
                "dropped_pair_parent_numbering": [list(pairs[0][0]), list(pairs[0][1])],
                "mutated_cnf_sha256": K.sha_bytes(M), "mutated_header": K.cnf_header(M)}
        log("%s mutation: %s" % (enc, info))
        name = "Cd-class0-%s-dropG5" % enc
        rec = run(tag, name, M, solver=K.solver_argv(solver, 900))
        rec.update({"class": 0, "key": key, "mutation": info, "encoder_run": hinfo,
                    "expectation": "none (record as observed)"})
        rec["outcome"] = summarize(rec)
        rec["matches_expectation"] = None
        save(tag, name, rec)
        name = "Cd2-class0-%s-origproof-vs-mutatedcnf" % enc
        rec = run(tag, name, H, solver=K.solver_argv(solver, 900), checker_cnf=M)
        rec.update({"class": 0, "key": key, "mutation": info,
                    "note": "solver reads the unmutated heavy CNF; drat-trim checks that proof against the mutated CNF",
                    "expectation": "none (record as observed)"})
        rec["outcome"] = summarize(rec)
        rec["matches_expectation"] = None
        save(tag, name, rec)


if __name__ == "__main__":
    tag = sys.argv[1]
    bad = K.check_runtime_pins()
    if bad:
        raise SystemExit("runtime pin mismatch: %s" % bad)
    for section in sys.argv[2:]:
        {"transport": transport, "checker": checker, "noheavy": noheavy, "mutate": mutate}[section](tag)
