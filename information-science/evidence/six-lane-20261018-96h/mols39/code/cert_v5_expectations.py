# PACKAGE v5 I/O repair: every artifact/audit open is nonblocking/no-follow; descriptor regular/nlink1
# and <=cap+1 actual consumption; all prior schema/audit/nc6 barriers retained. Late stdout => exit5.
#!/usr/bin/env python3
"""CERTIFICATE PACKAGE v4: nc6 reconstructed from actual pinned raw/fibres/points, complete runtime-pin
inventory, and fresh final-publication budget checks; parent review7b07cf45 findings1/3/5. Source-only.
cert_v5_expectations.py (ContinueCFR21, mols39 lane; written 2026-10-19; NOT executed when frozen; stdlib only).

Expectation gate for the Lemma U certificate wave of evidence/lemmaU-cert-run-plan-v5.json.
Successor of check_cert_runs_v2.py (sha256 d7be83ffa375818f45efe6513a77990e36e5af504d6483a167ce679f1d3a5959, never
executed). It answers review ea5f29a7... F1, F2, M1 and M4 (see the per-finding map). Run only through
code/cert_v5_entry_expectations.py, which verifies the job root and makes it the working directory.

What it does for --self ITEM (an "expectations" job of the plan):
  * prefix = all plan items strictly before ITEM, in plan order, earlier EXP items included. Every prefix item must
    carry a parent audit record (<audit_dir>/<item>.audit.json, format v2 section 8) with verdict AUDITED_PASS and
    the expected exit code; the record's declared-output hashes must equal the hashes this program computes from the
    actual files.
  * Every artifact is read from <base_dir>/<item>/<declared name>, where base_dir is fixed by the plan. Each read
    walks the path component by component with O_NOFOLLOW and requires a regular file with one link and a size within
    its cap. No path supplied by a manifest or report is followed.
  * Each result file is parsed strictly (duplicate keys, NaN, Infinity and non-finite floats are rejected) and must
    be one line in its producer's exact serialisation, with the exact key set. Comparisons use typed equality, so
    1 != True and 7 != 7.0.
  * Producer: report fields as preregistered; cert_sha256 equals the sha256 of the actual cert.json; the certificate
    is canonical and its header is consistent with the report.
  * Checker: report fields as preregistered, including the anchor hash; the reason must match exactly, by full-match
    regex or by a template filled from the verified mutant details; cert_sha256 equals the sha256 of the actual
    certificate artifact named by the plan; the plan's argv for the job is rebuilt and compared.
  * Generator: report and manifest as preregistered; every mutant file is canonical, and its content equals the
    intended mutation of the actual producer certificate. The mutation is re-applied independently here, and the
    manifest details are checked against the source.
  * Earlier EXP items: report as preregistered (same plan, same prefix, all_as_expected, claim "UNEVALUATED").
  * Pins: every program and input file named by the plan must still hash to its pin.
  * Claim: "UNEVALUATED" while the claim item is outside the prefix; otherwise true or false by the exact predicate
    (format v2 section 6). qualified is true only for the plan's final item, with everything as expected and the
    claim true.
Exit: 0 iff the evaluation completed and is as expected (for the final item: qualified); 1 on any deviation;
2 on a plan or input error; 5 on budget. One JSON line is printed and written to result.json (canonical)."""
import sys, os, re, json, math, stat, time, copy, hashlib

PLAN_CAP = 4 << 20
ART_CAP = 8 << 20
AUDIT_CAP = 1 << 20
PIN_CAP = 8 << 20
MAX_BUDGET_S = 280.0
DEFAULT_BUDGET_S = 240.0
HEX = frozenset("0123456789abcdef")
NAME_RE = re.compile(r"[A-Za-z0-9_.-]+")
FLAGS = ("--plan", "--plan-sha256", "--self", "--budget-s")
RESULT_KEYS = ("status", "reason", "self", "plan_sha256", "evaluated_prefix", "all_as_expected", "claim",
               "qualified", "pin_mismatches", "items", "wall_s")
PRODUCER_KEYS = ("status", "reason", "n", "q", "k", "U", "J", "rank", "dim", "rainbow_count", "alpha_hat_idx",
                 "minus_alpha_hat_idx", "cert_sha256", "anchor_sha256", "producer_sha256", "wall_s")
CHECKER_KEYS = ("verdict", "first_failed_check", "reason", "cert_sha256", "anchor_sha256", "n", "q", "k", "U", "J",
                "dim", "rank", "rainbow_count", "alpha_hat_listed", "minus_alpha_hat_listed",
                "rainbow_is_pm_alpha_hat", "wall_s")
GENERATOR_KEYS = ("status", "reason", "mutants", "manifest_sha256", "source_cert_sha256", "generator_sha256",
                  "wall_s")
CERT_KEYS = ("format", "anchor_sha256", "n", "q", "k", "U", "J", "dim", "basis", "free_columns", "rank_witness",
             "rainbow", "failures", "producer")
MANIFEST_KEYS = ("format", "source_cert_sha256", "anchor_sha256", "generator_sha256", "mutants")
MUTANT_KEYS = ("item", "file", "sha256", "intended_verdict", "intended_first_failed_check", "detail")
AUDIT_KEYS = ("format", "item", "plan_sha256", "verdict", "settled", "exit_code", "declared_output_sha256",
              "receipt_sha256", "auditor", "at", "notes")
DETAIL_KEYS = {"nc0_identity": (), "nc1_basis_flip": ("vector", "position", "old", "new"),
               "nc2_pivot_swap": ("record_a", "record_b", "pivot_a", "pivot_b"),
               "nc3_rainbow_swap": ("rainbow_idx_moved", "failure_idx_moved", "failure_fibre_of_moved",
                                    "new_failure_fibre"),
               "nc4_failure_delete": ("deleted_idx", "deleted_fibre"), "nc5_wrong_anchor_hash": (),
               "nc6_failure_wrong_fibre": ("position", "idx", "old_fibre", "new_fibre"),
               "nc7_witness_coef": ("record", "term", "equation", "old_coef", "new_coef"),
               "nc8_witness_drop": ("deleted_record", "deleted_pivot"), "nc9_anchor_mutation": (),
               "nc10_basis_scale": ("vector", "factor")}


class Fatal(Exception):
    """Plan, argument or own-environment error: status ERROR (or BUDGET_EXCEEDED)."""

    def __init__(self, status, reason):
        super().__init__(reason)
        self.status, self.reason = status, reason


class Problem(Exception):
    """A deviation of one item."""


class Budget:
    def __init__(self, t0, seconds):
        self.deadline = t0 + seconds

    def tick(self):
        if time.monotonic() > self.deadline:
            raise Fatal("BUDGET_EXCEEDED", "self budget exceeded")


def same(a, b):
    """Typed structural equality: bool, int, float, str, None, list and dict never compare across types."""
    if type(a) is not type(b):
        return False
    if type(a) is dict:
        return list(a.keys()) == list(b.keys()) and all(same(a[k], b[k]) for k in a) \
            if list(a.keys()) == list(b.keys()) else (set(a) == set(b) and all(same(a[k], b[k]) for k in a))
    if type(a) is list:
        return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
    return a == b


def strict_loads(data):
    def pairs(items):
        out = {}
        for key, value in items:
            if key in out:
                raise ValueError("duplicate key")
            out[key] = value
        return out

    def bad_constant(name):
        raise ValueError("non-finite constant")

    def finite_float(text):
        value = float(text)
        if not math.isfinite(value):
            raise ValueError("non-finite float")
        return value

    return json.loads(data.decode("utf-8"), object_pairs_hook=pairs, parse_constant=bad_constant,
                      parse_float=finite_float)


def parse_report(data, keys, sorted_keys):
    """One-line report in its producer's exact serialisation with exactly `keys`."""
    if not data.endswith(b"\n") or data.count(b"\n") != 1:
        raise Problem("report is not exactly one newline-terminated line")
    try:
        obj = strict_loads(data)
    except (UnicodeDecodeError, ValueError, RecursionError):
        raise Problem("report is not strict JSON") from None
    if type(obj) is not dict:
        raise Problem("report is not an object")
    if sorted_keys:
        if set(obj) != set(keys):
            raise Problem("report key set differs")
        canon = json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n"
    else:
        if list(obj.keys()) != list(keys):
            raise Problem("report keys differ from the fixed order")
        canon = json.dumps(obj, separators=(",", ":")) + "\n"
    if canon.encode("ascii") != data:
        raise Problem("report bytes are not in the exact serialisation")
    return obj


def parse_canonical(data, keys, what):
    try:
        obj = strict_loads(data)
    except (UnicodeDecodeError, ValueError, RecursionError):
        raise Problem(what + " is not strict JSON") from None
    if type(obj) is not dict or set(obj) != set(keys):
        raise Problem(what + " key set differs")
    if (json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii") != data:
        raise Problem(what + " is not in canonical bytes")
    return obj


def is_hex64(v):
    return type(v) is str and len(v) == 64 and set(v) <= HEX


def finite_nonneg_float(v):
    return type(v) is float and math.isfinite(v) and v >= 0.0


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def open_dir(path):
    if type(path) is not str or not path.startswith("/") or "\x00" in path:
        raise OSError("not an absolute path")
    parts = path.split("/")[1:]
    if any(p in ("", ".", "..") for p in parts):
        raise OSError("path is not normalised")
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for p in parts:
            nfd = os.open(p, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = nfd
    except OSError:
        os.close(fd)
        raise
    return fd


def read_entry(dir_fd, name, cap):
    if not NAME_RE.fullmatch(name) or name in (".", ".."):
        raise Problem("bad file name")
    try:
        fd = os.open(name, os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW, dir_fd=dir_fd)
    except OSError as exc:
        raise Problem("cannot open %s: %s" % (name, type(exc).__name__)) from None
    try:
        st = os.fstat(fd)
        if not stat.S_ISREG(st.st_mode):
            raise Problem(name + " is not a regular file")
        if st.st_nlink != 1:
            raise Problem(name + " does not have exactly one link")
        if st.st_size > cap:
            raise Problem(name + " exceeds its size cap")
        chunks, total = [], 0
        while True:
            block = os.read(fd, min(65536, cap + 1 - total))
            if not block:
                break
            total += len(block)
            if total > cap:
                raise Problem(name + " exceeds its size cap")
            chunks.append(block)
        return b"".join(chunks)
    finally:
        os.close(fd)


def read_pinned(path, cap):
    fd = os.open(path, os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_size > cap:
            raise OSError("pinned input kind or cap")
        chunks, total = [], 0
        while True:
            b = os.read(fd, min(65536, cap + 1 - total))
            if not b:
                break
            total += len(b)
            if total > cap:
                raise OSError("pinned input grew past cap")
            chunks.append(b)
        return b"".join(chunks)
    finally:
        os.close(fd)


def parse_args(argv):
    got = {}
    if len(argv) % 2:
        raise Fatal("ERROR", "arguments must be --flag value pairs")
    for i in range(0, len(argv), 2):
        flag, value = argv[i], argv[i + 1]
        if flag not in FLAGS or flag in got:
            raise Fatal("ERROR", "unknown or repeated flag")
        got[flag] = value
    for flag in FLAGS[:-1]:
        if flag not in got:
            raise Fatal("ERROR", "missing " + flag)
    budget_s = DEFAULT_BUDGET_S
    if "--budget-s" in got:
        try:
            budget_s = float(got["--budget-s"])
        except ValueError:
            raise Fatal("ERROR", "--budget-s is not a number") from None
    if not (math.isfinite(budget_s) and 0.0 < budget_s <= MAX_BUDGET_S):
        raise Fatal("ERROR", "--budget-s must be finite with 0 < S <= 280")
    return got["--plan"], got["--plan-sha256"], got["--self"], budget_s


def load_plan(path, pin):
    try:
        data = read_pinned(path, PLAN_CAP)
    except OSError as exc:
        raise Fatal("ERROR", "cannot read plan: " + type(exc).__name__) from None
    if sha256(data) != pin:
        raise Fatal("ERROR", "plan sha256 differs from --plan-sha256")
    try:
        plan = strict_loads(data)
    except (UnicodeDecodeError, ValueError, RecursionError):
        raise Fatal("ERROR", "plan is not strict JSON") from None
    for key in ("base_dir", "audit_dir", "order", "jobs", "programs", "inputs", "claim", "final_item",
                "audit_record_format"):
        if key not in plan:
            raise Fatal("ERROR", "plan lacks " + key)
    order = plan["order"]
    jobs = {}
    for job in plan["jobs"]:
        item = job.get("item")
        if type(item) is not str or not NAME_RE.fullmatch(item) or item in jobs:
            raise Fatal("ERROR", "plan job item names")
        jobs[item] = job
    if type(order) is not list or list(order) != [j["item"] for j in plan["jobs"]]:
        raise Fatal("ERROR", "plan order differs from its job list")
    if plan["final_item"] != order[-1] or jobs[order[-1]].get("kind") != "expectations":
        raise Fatal("ERROR", "plan final item")
    return plan, jobs


def expected_argv(plan, job):
    """Rebuild the argv tail that the plan must contain for this job."""
    base, inp, kind = plan["base_dir"], plan["inputs"], job["kind"]
    tail = ["--job-root", base + "/" + job["item"]]
    if kind == "producer":
        a = inp[job["anchor_input"]]
        tail += ["--anchor", a["path"], "--anchor-sha256", a["sha256"], "--budget-s", "240"]
    elif kind == "checker":
        a = inp[job["anchor_input"]]
        ca = job["cert_artifact"]
        tail += ["--anchor", a["path"], "--anchor-sha256", a["sha256"],
                 "--cert", base + "/" + ca["item"] + "/" + ca["file"], "--out", "result.json", "--budget-s", "240"]
    elif kind == "generator":
        sa = job["source_artifact"]
        tail += ["--cert", base + "/" + sa["item"] + "/" + sa["file"], "--cert-sha256", "@PROD_ANCHOR_CERT_SHA256@",
                 "--anchor", inp[job["anchor_input"]]["path"], "--anchor-sha256", inp[job["anchor_input"]]["sha256"],
                 "--other-sha256", inp[job["other_input"]]["sha256"],
                 "--mut-anchor-sha256", inp[job["mut_anchor_input"]]["sha256"], "--budget-s", "240"]
    elif kind == "expectations":
        tail += ["--plan", plan["plan_path"], "--plan-sha256", "@PLAN_SHA256@", "--self", job["item"],
                 "--budget-s", "240"]
    else:
        raise Problem("unknown job kind")
    return tail


def derive_nc6(src, anchor_raw, budget):
    """Independent from producer/generator/checker code: derive ALL candidate fibres from pinned raw,
    reconstruct each source point, and select first eligible failure + smallest passing fibre.
    No manifest position or new_fibre is used to guide the selection.
    """
    n, q, k, U, dim = (src[key] for key in ("n", "q", "k", "U", "dim"))
    if not all(type(v) is int for v in (n, q, k, U, dim)) or not (2 <= k <= 12 and n <= 120
            and n == 3*q and q >= 1 and q % 3 != 0 and 0 <= dim <= 8 and U == (k-1)*(n-1)):
        raise Problem("nc6 source header/work limits")
    lines = anchor_raw.split(b"\n")
    if lines[-1] == b"":
        lines.pop()
    D = []
    for line in lines:
        budget.tick()
        tokens = line.split()
        if not tokens:
            raise Problem("nc6 raw G1 blank row")
        vals = []
        for t in tokens:
            z = t[1:] if t[:1] in (b"+", b"-") else t
            if not z.isdigit():
                raise Problem("nc6 raw G1 token")
            vals.append(int(t) % n)
        D.append(vals)
    if len(D) != k or any(len(r) != n for r in D):
        raise Problem("nc6 raw/source shape")
    fibres = []
    for x in range(k):
        for y in range(x+1, k):
            budget.tick()
            buckets = [[] for _ in range(q)]
            for c in range(n):
                buckets[(D[x][c]-D[y][c]) % q].append(c)
            for t in range(q):
                if len(buckets[t]) != 3:
                    raise Problem("nc6 raw fibre size")
                fibres.append((x, y, buckets[t]))
    if len(fibres) != src["J"]:
        raise Problem("nc6 fibre count")
    basis = src["basis"]
    if type(basis) is not list or len(basis) != dim or any(type(b) is not list or len(b) != U
            or any(type(v) is not int or not 0 <= v <= 2 for v in b) for b in basis):
        raise Problem("nc6 source basis schema")
    def good(A, j):
        x, y, cols = fibres[j]
        values = []
        for c in cols:
            ax = A[(x-1)*(n-1)+(c-1)] if x and c else 0
            ay = A[(y-1)*(n-1)+(c-1)] if y and c else 0
            values.append((ax-ay) % 3)
        return len(set(values)) == 3
    last = -1
    for pos, entry in enumerate(src["failures"]):
        budget.tick()
        if type(entry) is not list or len(entry) != 2:
            raise Problem("nc6 source failure schema")
        idx, old_j = entry
        if type(idx) is not int or not last < idx < 3**dim or type(old_j) is not int or not 0 <= old_j < len(fibres):
            raise Problem("nc6 source failure index")
        last = idx
        digits = [0]*dim
        rem = idx
        for r in range(dim-1, -1, -1):
            digits[r] = rem % 3
            rem //= 3
        A = [sum(digits[r]*basis[r][v] for r in range(dim)) % 3 for v in range(U)]
        if good(A, old_j):
            raise Problem("nc6 claimed source failure actually passes")
        for j in range(len(fibres)):
            budget.tick()
            if good(A, j):
                return {"position": pos, "idx": idx, "old_fibre": old_j, "new_fibre": j}
    raise Problem("nc6 no eligible source failure")


def apply_mutation(src, name, detail, inputs, job, anchor_raw, budget):
    """Independent re-derivation of the intended mutant from the actual source certificate."""
    if type(detail) is not dict or list(sorted(detail)) != sorted(DETAIL_KEYS[name]) \
            or not all(type(v) is int for v in detail.values()):
        raise Problem(name + ": detail keys or types differ")
    m = copy.deepcopy(src)
    rw, fl = src["rank_witness"], src["failures"]
    if name == "nc0_identity":
        pass
    elif name == "nc1_basis_flip":
        p = rw[0]["pivot"]
        old = src["basis"][0][p]
        if not same(detail, {"vector": 0, "position": p, "old": old, "new": (old + 1) % 3}):
            raise Problem(name + ": detail differs from the source")
        m["basis"][0][p] = (old + 1) % 3
    elif name == "nc2_pivot_swap":
        pa, pb = rw[0]["pivot"], rw[1]["pivot"]
        if not same(detail, {"record_a": 0, "record_b": 1, "pivot_a": pa, "pivot_b": pb}):
            raise Problem(name + ": detail differs from the source")
        m["rank_witness"][0]["pivot"], m["rank_witness"][1]["pivot"] = pb, pa
    elif name == "nc3_rainbow_swap":
        r0, f0, jf0 = src["rainbow"][0], fl[0][0], fl[0][1]
        if not same(detail, {"rainbow_idx_moved": r0, "failure_idx_moved": f0, "failure_fibre_of_moved": jf0,
                             "new_failure_fibre": 0}):
            raise Problem(name + ": detail differs from the source")
        m["rainbow"] = sorted([i for i in src["rainbow"] if i != r0] + [f0])
        m["failures"] = sorted([list(e) for e in fl if e[0] != f0] + [[r0, 0]], key=lambda e: e[0])
    elif name == "nc4_failure_delete":
        if not same(detail, {"deleted_idx": fl[0][0], "deleted_fibre": fl[0][1]}):
            raise Problem(name + ": detail differs from the source")
        m["failures"] = [list(e) for e in fl[1:]]
    elif name == "nc5_wrong_anchor_hash":
        m["anchor_sha256"] = inputs[job["other_input"]]["sha256"]
    elif name == "nc6_failure_wrong_fibre":
        derived = derive_nc6(src, anchor_raw, budget)
        if not same(detail, derived):
            raise Problem(name + ": independently derived first eligible failure/smallest passing fibre differs")
        m["failures"][derived["position"]] = [derived["idx"], derived["new_fibre"]]
    elif name == "nc7_witness_coef":
        eq, oc = rw[0]["combination"][0]
        if not same(detail, {"record": 0, "term": 0, "equation": eq, "old_coef": oc, "new_coef": 3 - oc}):
            raise Problem(name + ": detail differs from the source")
        m["rank_witness"][0]["combination"][0] = [eq, 3 - oc]
    elif name == "nc8_witness_drop":
        if not same(detail, {"deleted_record": len(rw) - 1, "deleted_pivot": rw[-1]["pivot"]}):
            raise Problem(name + ": detail differs from the source")
        m["rank_witness"] = copy.deepcopy(rw[:-1])
    elif name == "nc9_anchor_mutation":
        m["anchor_sha256"] = inputs[job["mut_anchor_input"]]["sha256"]
    elif name == "nc10_basis_scale":
        if not same(detail, {"vector": 0, "factor": 2}):
            raise Problem(name + ": detail differs from the source")
        m["basis"][0] = [(2 * v) % 3 for v in src["basis"][0]]
    else:
        raise Problem("unknown mutant " + name)
    return m


class Evaluator:
    def __init__(self, plan, jobs, plan_sha, budget):
        self.plan, self.jobs, self.plan_sha, self.budget = plan, jobs, plan_sha, budget
        self.state = {}          # item -> parsed objects for later items
        self.ok = {}             # item -> bool

    def check_audit(self, audit_fd, item, job, actual):
        data = read_entry(audit_fd, item + ".audit.json", AUDIT_CAP)
        try:
            rec = strict_loads(data)
        except (UnicodeDecodeError, ValueError, RecursionError):
            raise Problem("audit record is not strict JSON") from None
        if type(rec) is not dict or set(rec) != set(AUDIT_KEYS):
            raise Problem("audit record key set differs")
        want = {"format": self.plan["audit_record_format"], "item": item, "plan_sha256": self.plan_sha,
                "verdict": "AUDITED_PASS", "settled": True, "exit_code": job["expected_exit"]}
        for key, value in want.items():
            if not same(rec[key], value):
                raise Problem("audit %s = %r, expected %r" % (key, rec[key], value))
        outs = rec["declared_output_sha256"]
        if type(outs) is not dict or set(outs) != set(job["declared_outputs"]):
            raise Problem("audit declared outputs differ from the plan")
        for name, digest in outs.items():
            if not is_hex64(digest) or digest != actual[name]:
                raise Problem("audit hash of %s differs from the actual file" % name)
        for key in ("receipt_sha256", "auditor", "at", "notes"):
            if type(rec[key]) is not str:
                raise Problem("audit %s is not a string" % key)

    def artifact(self, item, name):
        st = self.state.get(item)
        if st is None or name not in st["bytes"]:
            raise Problem("dependency %s/%s unavailable" % (item, name))
        if not self.ok.get(item):
            raise Problem("dependency %s is not as expected" % item)
        return st["bytes"][name]

    def check_producer(self, job, files):
        exp = job["expect_fields"]
        rep = parse_report(files["result.json"], PRODUCER_KEYS, True)
        for key, value in exp.items():
            if not same(rep[key], value):
                raise Problem("result %s = %r, expected %r" % (key, rep[key], value))
        anchor = self.plan["inputs"][job["anchor_input"]]["sha256"]
        if not same(rep["anchor_sha256"], anchor):
            raise Problem("result anchor_sha256 differs from the pinned input")
        if not same(rep["cert_sha256"], sha256(files["cert.json"])):
            raise Problem("result cert_sha256 differs from the actual cert.json")
        if not finite_nonneg_float(rep["wall_s"]):
            raise Problem("result wall_s is not a finite non-negative float")
        dim, rc = rep["dim"], rep["rainbow_count"]
        ia, ima = rep["alpha_hat_idx"], rep["minus_alpha_hat_idx"]
        if type(ia) is not int or type(ima) is not int or ia == ima or not (0 <= ia < 3 ** dim) \
                or not (0 <= ima < 3 ** dim):
            raise Problem("result alpha_hat indices invalid")
        cert = parse_canonical(files["cert.json"], CERT_KEYS, "cert.json")
        if cert["format"] != "lemmaU-cert-v1" or not same(cert["anchor_sha256"], anchor):
            raise Problem("cert.json format or anchor hash")
        for key in ("n", "q", "k", "U", "J", "dim"):
            if not same(cert[key], rep[key]):
                raise Problem("cert.json %s differs from the result" % key)
        if type(cert["basis"]) is not list or len(cert["basis"]) != dim \
                or type(cert["rank_witness"]) is not list or len(cert["rank_witness"]) != cert["U"] - dim \
                or type(cert["rainbow"]) is not list or len(cert["rainbow"]) != rc \
                or type(cert["failures"]) is not list or len(cert["failures"]) != 3 ** dim - rc \
                or ia not in cert["rainbow"] or ima not in cert["rainbow"]:
            raise Problem("cert.json sizes or rainbow list inconsistent with the result")
        return {"result": rep, "cert": cert}

    def check_checker(self, job, files):
        exp = job["expect_fields"]
        rep = parse_report(files["result.json"], CHECKER_KEYS, False)
        for key, value in exp.items():
            if not same(rep[key], value):
                raise Problem("result %s = %r, expected %r" % (key, rep[key], value))
        if not same(rep["anchor_sha256"], self.plan["inputs"][job["anchor_input"]]["sha256"]):
            raise Problem("result anchor_sha256 differs from the pinned input")
        ca = job["cert_artifact"]
        if not same(rep["cert_sha256"], sha256(self.artifact(ca["item"], ca["file"]))):
            raise Problem("result cert_sha256 differs from the actual certificate artifact")
        if not finite_nonneg_float(rep["wall_s"]):
            raise Problem("result wall_s is not a finite non-negative float")
        reason = rep["reason"]
        if type(reason) is not str:
            raise Problem("result reason is not a string")
        if "reason" in exp:
            pass
        elif job.get("reason_regex") is not None:
            if not re.fullmatch(job["reason_regex"], reason):
                raise Problem("reason %r does not match %r" % (reason, job["reason_regex"]))
        elif job.get("reason_template") is not None:
            mut = job["template_mutant"]
            detail = self.state["MUT"]["details"].get(mut) if "MUT" in self.state else None
            if detail is None or not self.ok.get("MUT"):
                raise Problem("template details unavailable")
            try:
                want = job["reason_template"].format(**detail)
            except (KeyError, IndexError, ValueError):
                raise Problem("reason template cannot be filled") from None
            if reason != want:
                raise Problem("reason %r, expected %r" % (reason, want))
        else:
            raise Problem("plan gives no reason expectation")
        return {"result": rep}

    def check_generator(self, job, files):
        rep = parse_report(files["result.json"], GENERATOR_KEYS, True)
        for key, value in job["expect_fields"].items():
            if not same(rep[key], value):
                raise Problem("result %s = %r, expected %r" % (key, rep[key], value))
        sa = job["source_artifact"]
        src_bytes = self.artifact(sa["item"], sa["file"])
        src_sha = sha256(src_bytes)
        if not same(rep["source_cert_sha256"], src_sha):
            raise Problem("result source_cert_sha256 differs from the actual producer certificate")
        if not same(rep["manifest_sha256"], sha256(files["manifest.json"])):
            raise Problem("result manifest_sha256 differs from the actual manifest")
        if not finite_nonneg_float(rep["wall_s"]):
            raise Problem("result wall_s is not a finite non-negative float")
        man = parse_canonical(files["manifest.json"], MANIFEST_KEYS, "manifest.json")
        inputs = self.plan["inputs"]
        if man["format"] != "lemmaU-cert-mutants-v2" or not same(man["source_cert_sha256"], src_sha) \
                or not same(man["anchor_sha256"], inputs[job["anchor_input"]]["sha256"]) \
                or type(man["generator_sha256"]) is not str:
            raise Problem("manifest header differs")
        plan_m = job["mutants"]
        if type(man["mutants"]) is not list or len(man["mutants"]) != len(plan_m):
            raise Problem("manifest mutant count differs")
        src = parse_canonical(src_bytes, CERT_KEYS, "source certificate")
        anchor_input = inputs[job["anchor_input"]]
        anchor_raw = read_pinned(anchor_input["path"], 1 << 20)
        if sha256(anchor_raw) != anchor_input["sha256"]:
            raise Problem("nc6 independent anchor pin mismatch")
        details = {}
        for entry, want in zip(man["mutants"], plan_m):
            self.budget.tick()
            if type(entry) is not dict or set(entry) != set(MUTANT_KEYS):
                raise Problem("manifest entry keys differ")
            name = want["item"]
            if not same(entry["item"], name) or not same(entry["file"], name + ".cert.json") \
                    or not same(entry["intended_verdict"], want["intended_verdict"]) \
                    or not same(entry["intended_first_failed_check"], want["intended_first_failed_check"]):
                raise Problem("manifest entry %s differs from the plan" % name)
            data = files[name + ".cert.json"]
            if not same(entry["sha256"], sha256(data)):
                raise Problem("manifest hash of %s differs from the actual file" % name)
            mut = parse_canonical(data, CERT_KEYS, name)
            expected = apply_mutation(src, name, entry["detail"], inputs, job, anchor_raw, self.budget)
            if not same(mut, expected) and not (set(mut) == set(expected) and
                                                all(same(mut[k], expected[k]) for k in expected)):
                raise Problem("%s is not exactly the intended mutation of the source" % name)
            details[name] = entry["detail"]
        if files["nc0_identity.cert.json"] != src_bytes:
            raise Problem("nc0_identity bytes differ from the source certificate")
        return {"result": rep, "manifest": man, "details": details}

    def check_expectations(self, item, job, files):
        rep = parse_report(files["result.json"], RESULT_KEYS, True)
        order = self.plan["order"]
        prefix = order[:order.index(item)]
        want_claim = "UNEVALUATED" if self.plan["claim"]["item"] not in prefix else True
        want = {"status": "OK", "reason": None, "self": item, "plan_sha256": self.plan_sha,
                "evaluated_prefix": prefix, "all_as_expected": True, "claim": want_claim,
                "qualified": item == self.plan["final_item"], "pin_mismatches": []}
        for key, value in want.items():
            if not same(rep[key], value):
                raise Problem("result %s = %r, expected %r" % (key, rep[key], value))
        if not finite_nonneg_float(rep["wall_s"]) or type(rep["items"]) is not list:
            raise Problem("result wall_s or items")
        return {"result": rep}

    def evaluate_item(self, base_fd, audit_fd, item):
        job = self.jobs[item]
        record = {"item": item, "kind": job.get("kind"), "problems": [], "artifacts": {}}
        try:
            argv = job.get("argv_tail")
            if not same(argv, expected_argv(self.plan, job)):
                raise Problem("plan argv_tail differs from the rebuilt argv")
            names = job["declared_outputs"]
            if type(names) is not list or not names or len(set(names)) != len(names):
                raise Problem("plan declared_outputs")
            if base_fd is None:
                raise Problem("base_dir cannot be opened safely")
            try:
                item_fd = os.open(item, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=base_fd)
            except OSError as exc:
                raise Problem("job root cannot be opened safely: " + type(exc).__name__) from None
            try:
                files = {}
                for name in names:
                    self.budget.tick()
                    files[name] = read_entry(item_fd, name, ART_CAP)
            finally:
                os.close(item_fd)
            record["artifacts"] = {name: sha256(data) for name, data in files.items()}
            if audit_fd is None:
                raise Problem("audit_dir cannot be opened safely")
            self.check_audit(audit_fd, item, job, record["artifacts"])
            kind = job["kind"]
            if kind == "producer":
                parsed = self.check_producer(job, files)
            elif kind == "checker":
                parsed = self.check_checker(job, files)
            elif kind == "generator":
                parsed = self.check_generator(job, files)
            elif kind == "expectations":
                parsed = self.check_expectations(item, job, files)
            else:
                raise Problem("unknown job kind")
            parsed["bytes"] = files
            self.state[item] = parsed
        except Problem as exc:
            record["problems"].append(str(exc))
        except (KeyError, TypeError, IndexError, ValueError, AttributeError) as exc:
            record["problems"].append("plan or data shape error: " + type(exc).__name__)
        self.ok[item] = not record["problems"]
        if item not in self.state:
            self.state[item] = None
        return record


def main(argv):
    t0 = time.monotonic()
    out = {key: None for key in RESULT_KEYS}
    out.update({"evaluated_prefix": [], "all_as_expected": False, "claim": "UNEVALUATED", "qualified": False,
                "pin_mismatches": [], "items": []})
    code = 2
    budget = None
    try:
        plan_path, plan_sha, self_item, budget_s = parse_args(argv)
        budget = Budget(t0, budget_s)
        if not is_hex64(plan_sha):
            raise Fatal("ERROR", "--plan-sha256 is not 64 lowercase hex digits")
        plan, jobs = load_plan(plan_path, plan_sha)
        plan["plan_path"] = plan_path
        out["self"], out["plan_sha256"] = self_item, plan_sha
        order = plan["order"]
        if self_item not in jobs or jobs[self_item].get("kind") != "expectations":
            raise Fatal("ERROR", "--self is not an expectations item of the plan")
        try:
            own = os.stat(".")
            root_fd = open_dir(plan["base_dir"] + "/" + self_item)
            try:
                mine = os.fstat(root_fd)
            finally:
                os.close(root_fd)
        except OSError:
            raise Fatal("ERROR", "own job root cannot be verified") from None
        if (own.st_dev, own.st_ino) != (mine.st_dev, mine.st_ino):
            raise Fatal("ERROR", "working directory is not <base_dir>/<self>")
        prefix = order[:order.index(self_item)]
        out["evaluated_prefix"] = prefix
        pins = []
        for prog in plan["programs"].values():
            pins += [(prog["entrypoint"], prog["entrypoint_sha256"]), (prog["algorithm"], prog["algorithm_sha256"])]
        for inp in plan["inputs"].values():
            pins.append((inp["path"], inp["sha256"]))
            provenance = inp.get("provenance")
            if type(provenance) is dict and "path" in provenance and "sha256" in provenance:
                pins.append((provenance["path"], provenance["sha256"]))
        for key in ("format", "format_overlay"):
            documentary = plan[key]
            pins.append((documentary["path"], documentary["sha256"]))
        provenance = plan["nc9"]["provenance"]
        pins.append((provenance["path"], provenance["sha256"]))
        inventory = plan["runtime_pin_inventory"]
        if type(inventory) is not list:
            raise Fatal("ERROR", "runtime pin inventory missing")
        recorded = {}
        for rec in inventory:
            if type(rec) is not dict or set(rec) != {"path", "sha256"} or type(rec["path"]) is not str or not is_hex64(rec["sha256"]):
                raise Fatal("ERROR", "runtime pin inventory schema")
            if rec["path"] in recorded:
                raise Fatal("ERROR", "runtime pin inventory duplicate path")
            recorded[rec["path"]] = rec["sha256"]
        if any(recorded.get(path) != digest for path, digest in pins):
            raise Fatal("ERROR", "runtime inventory omits a required source/format/provenance pin")
        pins = list(recorded.items())
        for path, digest in pins:
            budget.tick()
            try:
                if sha256(read_pinned(path, PIN_CAP)) != digest:
                    out["pin_mismatches"].append(path)
            except OSError:
                out["pin_mismatches"].append(path)
        try:
            base_fd = open_dir(plan["base_dir"])
        except OSError:
            base_fd = None
        try:
            audit_fd = open_dir(plan["audit_dir"])
        except OSError:
            audit_fd = None
        ev = Evaluator(plan, jobs, plan_sha, budget)
        try:
            for item in prefix:
                budget.tick()
                out["items"].append(ev.evaluate_item(base_fd, audit_fd, item))
        finally:
            for fd in (base_fd, audit_fd):
                if fd is not None:
                    os.close(fd)
        all_ok = all(not r["problems"] for r in out["items"]) and not out["pin_mismatches"]
        out["all_as_expected"] = all_ok
        claim = plan["claim"]
        if claim["item"] in prefix:
            st = ev.state.get(claim["item"])
            ca = claim["cert_artifact"]
            holds = False
            if st is not None and ev.ok.get(claim["item"]) and ev.state.get(ca["item"]) is not None:
                rep = st["result"]
                holds = all(same(rep[k], v) for k, v in claim["fields"].items()) \
                    and same(rep["cert_sha256"], sha256(ev.state[ca["item"]]["bytes"][ca["file"]])) \
                    and finite_nonneg_float(rep["wall_s"])
            out["claim"] = holds
        out["qualified"] = bool(self_item == plan["final_item"] and all_ok and out["claim"] is True)
        budget.tick()
        out["status"], out["reason"] = "OK", None
        if self_item == plan["final_item"]:
            code = 0 if out["qualified"] else 1
        else:
            code = 0 if (all_ok and out["claim"] == "UNEVALUATED") else 1
    except Fatal as exc:
        out["status"], out["reason"] = exc.status, exc.reason
        out["all_as_expected"], out["qualified"] = False, False
        code = 5 if exc.status == "BUDGET_EXCEEDED" else 2
    except Exception as exc:
        out["status"], out["reason"] = "ERROR", "internal: " + type(exc).__name__
        out["all_as_expected"], out["qualified"] = False, False
        code = 2
    if out["status"] == "OK" and budget is not None:
        try:
            budget.tick()
        except Fatal:
            out.update(status="BUDGET_EXCEEDED", reason="budget before result publication", all_as_expected=False, qualified=False)
            code = 5
    out["wall_s"] = round(time.monotonic() - t0, 3)
    line = json.dumps(out, sort_keys=True, separators=(",", ":"))
    try:
        fd = os.open("result.json", os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
        try:
            data = memoryview((line + "\n").encode("ascii"))
            while data:
                data = data[os.write(fd, data):]
        finally:
            os.close(fd)
    except OSError:
        out["status"], out["reason"] = "ERROR", "cannot write result.json"
        out["all_as_expected"], out["qualified"] = False, False
        line = json.dumps(out, sort_keys=True, separators=(",", ":"))
        code = 2
    if out["status"] == "OK" and budget is not None:
        try:
            budget.tick()
        except Fatal:
            out.update(status="BUDGET_EXCEEDED", reason="budget after result publication", all_as_expected=False, qualified=False)
            out["wall_s"] = round(time.monotonic() - t0, 3)
            line = json.dumps(out, sort_keys=True, separators=(",", ":"))
            code = 5
    try:
        print(line, flush=True)
    except OSError:
        return 2
    # Flush completion is inside the cooperative deadline; already emitted evidence is never rewritten.
    if budget is not None:
        try:
            budget.tick()
        except Fatal:
            return 5
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
