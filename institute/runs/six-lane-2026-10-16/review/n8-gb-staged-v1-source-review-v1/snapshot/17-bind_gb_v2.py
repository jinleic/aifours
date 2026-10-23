#!/usr/bin/env python3
"""Parent-owned independent GB (second-encoder) binding of the MOQLS(8) one-P4 leaf formulas, v2.

v2 supersedes the never-run-for-generation draft scripts/bind_gb_v1.py (7818a04f...33f0): its pre-flight
receipts/SELFTEST.v1.json (157d7f5c...68b4e) FAILED because gate (a) wrongly required that no single-unit flip
of one template equal ANY genuine formula, although several templates differ from another in exactly one unit
(e.g. P0-B1 vs P1-B1 at row 6, coordinate 1). v2 requires instead: each flip differs from its own formula,
the 42 flips are distinct, and a flip equals another genuine formula exactly when its composed pieces are equal
(same header/tail and identical unit list). Everything else is unchanged apart from the v2 file/dir names.

Desk: institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-binding-v1 (parent-owned).
Scope: exact-formula identities (bytes, counts, SHA256) of the 16 GB template formulas and the six GB
strengthened formulas of normal form r2 section 5. No SAT/UNSAT, transfer, n=8 or Problem-16 claim.
No worker code (code/gb_one_p4_r1.py) and no worker output is imported, copied, read or run.
No CNF or proof bytes are written to disk; no native tool or child process is started; stdlib only; one thread.

GB base. The hash-pinned bytes of code/gram_b_r2.py (4b593e55...beae0) are compiled and executed into fresh
module objects (importlib.util.module_from_spec; nothing is added to sys.path or sys.modules; main() is not run).
The exact flag list  --order 8 --quantum 12345 --ngeneric 0 --p4 1 --sb2 --g5  is turned into the encode()
arguments by evaluating main()'s own argparse/assignment statements (extracted from the pinned source AST), giving
encode(8, [1,2,3,4,5], 0, [1], True, None, True, False, False) == the brief's
encode(8,[1,2,3,4,5],0,[1],True,fixg=None,g5=True,allrows=False,allcols=False).
ONLY the clause storage is replaced: in the generation module object the global name F (which encode
instantiates as "F_ = F()") is rebound to a subclass of that module's own F whose c(*lits) appends the ASCII
bytes of (" ".join(map(str, lits)) + " 0\\n") -- the line main() writes for each stored clause -- to an
in-memory bytearray segment (a full 16 MiB segment is frozen as bytes and a new one started; boundaries fall
on clause boundaries) instead of appending list(lits) to F.cl (set to None so that any list use would fail).
F.new, F.n, F.tab and encode are inherited unchanged. Base header = "p cnf %d %d\\n" % (F.n, clause count),
as main() writes it. Why this cannot change the encoding: see gb_ast_facts() and the n=5 storage control.

Composition (GA parent conventions: review/moqls8-one-p4-parent-binding-v1/parent_binding_v1.py and
review/moqls8-strengthened-parent-replay-v1/scripts/bind_v1.py; exact lines are checked below):
  template T      "p cnf V C+42\\n" + base body + 42 unit lines "%d 0\\n": for i = 2..7 (ascending) and
                  c = 1..7 (ascending) the literal +v if c is in the WMAN support of row i of T, else -v,
                  with v = GB F.tab[('g', 1, (0, c), (i, 0))];
  strengthened    "p cnf V C+42+126\\n" + base body + the same 42 unit lines + 126 lines
                  "%d %d 0\\n" % tuple(sorted((-a, -b))) for i = 2..7 (ascending), (c, d) in
                  itertools.combinations(1..7, 2), a = F.tab[('g', s, (0, c), (i, 0))],
                  b = F.tab[('g', s, (0, d), (i, 0))].

Usage (environment: exactly TMPDIR=<desk>/tmp/<run>/):
  python3.14 -I -B scripts/bind_gb_v2.py --selftest   pre-flight (TMPDIR <desk>/tmp/selftest-v2/): pins, source
      checks, n=5 storage control, synthetic composition/controls incl. negative checks; NO n=8 encode;
      writes only receipts/SELFTEST.v2.json.
  python3.14 -I -B scripts/bind_gb_v2.py SHA256       the single generation run (TMPDIR <desk>/tmp/gen-v2/),
      started only by scripts/launch_gb_v2.py, which passes this file's pinned sha256; writes
      GB-PRIMARY-MAP.v2.txt and GBBINDING.json (or receipts/CHILD-ABORT.v2.json on a stop).
Exit codes: 0 PASS, 2 manifest written with failed gates, 3 cooperative abort (UNKNOWN), 4 stopped
(precondition/error), 5 refused before any work (free-space gate).
"""
import argparse
import ast
import datetime
import hashlib
import importlib.util
import io
import itertools
import json
import os
import re
import resource
import signal
import sys
import time
import traceback

T0 = time.monotonic()

ROOT = "/Users/jinleic/repos/aifours"
RUN = ROOT + "/institute/runs/six-lane-2026-10-16"
REVIEW = RUN + "/review"
LANE = ROOT + "/physics/evidence/six-lane-20261016/moqls8-problem16"
DESK = REVIEW + "/moqls8-gb-parent-binding-v1"
SCRIPT_REL = "scripts/bind_gb_v2.py"
SCRIPT = DESK + "/" + SCRIPT_REL
TMP_GEN = DESK + "/tmp/gen-v2"
TMP_SELFTEST = DESK + "/tmp/selftest-v2"
OUT_MAP = DESK + "/GB-PRIMARY-MAP.v2.txt"
OUT_MANIFEST = DESK + "/GBBINDING.json"
OUT_ABORT = DESK + "/receipts/CHILD-ABORT.v2.json"
OUT_SELFTEST = DESK + "/receipts/SELFTEST.v2.json"
SUPERSEDES = {"script": "scripts/bind_gb_v1.py",
              "sha256": "7818a04f2475cad69529e836b8572d5d775af95b7b09c4d3d05528a2c5c333f0",
              "selftest_receipt": "receipts/SELFTEST.v1.json",
              "selftest_receipt_sha256": "157d7f5cf094f944513232fea2bade20ccfc737332512172c1c9c52b1c868b4e",
              "reason": "gate (a) design error: required that no single-unit flip equal any genuine formula, but "
                        "templates that differ in exactly one unit (e.g. P0-B1/P1-B1) make such equalities "
                        "correct; v2 predicts every equality from the composed pieces instead",
              "v1_generation_runs": 0}

GB = LANE + "/code/gram_b_r2.py"
WMAN = LANE + "/evidence/n8_one_p4_templates_v1/MANIFEST.json"
NF_R2 = LANE + "/review/P1_COLUMN0_BOOLEAN_NORMAL_FORM.r2.md"
GA_LEAF_RESULT = REVIEW + "/moqls8-one-p4-parent-binding-v1/RESULT.json"
GA_LEAF_SCRIPT = REVIEW + "/moqls8-one-p4-parent-binding-v1/parent_binding_v1.py"
GA_STRONG_SCRIPT = REVIEW + "/moqls8-strengthened-parent-replay-v1/scripts/bind_v1.py"
GA_STRONG_BINDING = REVIEW + "/moqls8-strengthened-parent-replay-v1/BINDING.json"
PINS = {
    GB: "4b593e557fe5b26053537e7107ca5e7a11b3df8ce011bdf78981bc7e068beae0",
    WMAN: "355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74",
    NF_R2: "8ae0ac01de7ea5883111e8dcc4f84246813d8599b1e8af782e0498104a449e8f",
    GA_LEAF_RESULT: "65311ab0b3109412383b47113b36c6a4b3d74f8132fc334cb2f5194b480928b0",
    # sha recorded as script_sha256 in review/moqls8-one-p4-parent-binding-v1/PRE-EXEC.json (GA leaf unit convention)
    GA_LEAF_SCRIPT: "6b085b9050893171a2135baa22fc14e1ce8d0664cc8cf718d9dee3823ea75a51",
    GA_STRONG_SCRIPT: "b010baa4dd5c7620f7c6215beeb052af80846bfd6c3ee0a80e8d8a235144786c",
    GA_STRONG_BINDING: "5e1116e8311bfe4b2e06554edd0c77fc564574b06c1320334373648171f5f98c",
}
WORKER_PACKAGE_NOT_READ = {  # comparison targets only; this script never opens these files
    LANE + "/code/gb_one_p4_r1.py": "952c761c3543299e8f2f5c13db7e5d21cbb1f4e0156012b44d27665af15bd88c",
    LANE + "/review/GB_ONE_P4_NECESSITY.r1.md": "e4dd33f4bcd2b680bbdd1ebec4cabcf8583b60b17930682ff5c666d3327703ed",
}

FLAGS = ["--order", "8", "--quantum", "12345", "--ngeneric", "0", "--p4", "1", "--sb2", "--g5"]
BRIEF_CALL_JSON = json.dumps([8, [1, 2, 3, 4, 5], 0, [1], True, None, True, False, False])
CONTROL_CALL = {"n": 5, "Q": [1, 2], "ngen": 0, "p4": [1], "sb2": True, "fixg": None, "g5": True,
                "allrows": False, "allcols": False}
EXPECTED_IDS = ["P0-B1", "P0-B2", "P0-B3", "P0-B4", "P0-B5", "P0-B6", "P1-B1", "P1-B2", "P1-B3", "P1-B4",
                "P1-B5", "P1-B6", "P2-C1", "P2-C2", "P2-C3", "P2-C4"]
FORMULAS = (("P1-B1.M2", "P1-B1", 2), ("P1-B2.M2", "P1-B2", 2), ("P1-B2.M4", "P1-B2", 4),
            ("P1-B3.M2", "P1-B3", 2), ("P1-B5.M2", "P1-B5", 2), ("P1-B5.M3", "P1-B5", 3))
NF_SOURCES = ("P1-B1", "P1-B2", "P1-B3", "P1-B5")
DIRECT12 = [t for t in EXPECTED_IDS if t not in NF_SOURCES]
UNITS, TAIL = 42, 126
ROWS, COORDS = tuple(range(2, 8)), tuple(range(1, 8))

RSS_LIMIT = 1 << 30            # 1 GiB peak RSS of this process (ru_maxrss is in bytes on macOS)
WALL_LIMIT = 2700.0            # seconds since interpreter start of this script
FREE_FLOOR = 11_500_000_000    # in-flight cooperative stop (parent clarification for this in-memory job)
FREE_GATE = 12_000_000_000     # fresh reading required before any work (parent 07:17 rule + clarification)
FREE_PERIOD = 10.0             # seconds between in-flight free-space readings (low-frequency watcher rule)
GUARD_MASK = (1 << 17) - 1     # guard every 131072 stored clauses
SEGMENT = 1 << 24              # 16 MiB sink segments for the generation run
CONTROL_SEGMENT = 1 << 16      # 64 KiB segments in the storage control (many segment boundaries)
UNIT_RE = re.compile(rb"(-?[1-9][0-9]*) 0")
TAIL_RE = re.compile(rb"(-[1-9][0-9]*) (-[1-9][0-9]*) 0")

GB_LINES = (  # exact lines of the pinned GB source this binding relies on
    "class F:",
    "    def __init__(self):",
    "        self.n = 0",
    "        self.cl = []",
    "        self.tab = {}",
    "    def new(self, key=None):",
    "        self.n += 1",
    "        if key is not None:",
    "            self.tab[key] = self.n",
    "        return self.n",
    "    def c(self, *lits):",
    "        self.cl.append(list(lits))",
    "def encode(n, Q, ngen, p4, sb2, fixg=None, g5=False, allrows=False, allcols=False):",
    "    F_ = F()",
    "    T = F_.new(\"TRUE\")",
    "        key = (s,) + tuple(sorted((p, q)))",
    "            G[key] = F_.new((\"g\",) + key)",
    "    return F_",
    "    Q = [int(ch) for ch in a.quantum]",
    "    p4 = [] if a.p4 == \"none\" else [int(ch) for ch in a.p4]",
    "    F_ = encode(a.order, Q, a.ngeneric, p4, a.sb2, fixg, a.g5, a.p4_all_rows, a.p4_all_cols)",
    "    with open(a.cnf, \"x\") as fh:",
    "        fh.write(\"p cnf %d %d\\n\" % (F_.n, len(F_.cl)))",
    "        for cl in F_.cl:",
    "            fh.write(\" \".join(map(str, cl)) + \" 0\\n\")",
    "        json.dump({json.dumps(k): v for k, v in F_.tab.items()}, fh)",
)
NF_FRAGMENTS = (
    "M_s can be imposed by126 negative binary clauses for i=2..7 and1≤c<d≤7:",
    "NOT g_s((0,c),(i,0)) OR NOT g_s((0,d),(i,0)).",
    "- P1-B1: F_one AND C AND M2;",
    "- P1-B2: F_one AND C AND M2, or F_one AND C AND M4;",
    "- P1-B3: F_one AND C AND M2;",
    "- P1-B5: F_one AND C AND M2, or F_one AND C AND M3.",
)
GA_LEAF_LINES = (  # GA parent leaf composition: unit order/sign/serialization and header (+42)
    "    weak_header=b'p cnf 509915 5740226\\n';leaf_header=b'p cnf 509915 5740268\\n'",
    "        for i,S in enumerate(supports,2):",
    "            for c in range(1,8):",
    "                units.append(v if c in S else -v)",
    "        hh=leaf.copy();hh.update(b''.join(('%d 0\\n'%u).encode('ascii') for u in units))",
)
GA_STRONG_LINES = (  # GA parent strengthened composition: tail order/sign/serialization and header (+126)
    "        for i in range(2, 8):",
    "            for c, d in itertools.combinations(range(1, 8), 2):",
    "                cl = tuple(sorted((-a, -b)))",
    "        tb = \"\".join(\"%d %d 0\\n\" % cl for cl in clauses).encode(\"ascii\")",
    "    derived_header = b\"p cnf %d %d\\n\" % (int(m.group(1)), int(m.group(2)) + TAIL_CLAUSES)",
    "        h = hashlib.sha256(STRONG_HEADER)",
    "        h.update(body)",
    "        h.update(ub)",
    "        h.update(tb)",
)
GA_SERIALIZATION = ("literals ascending within each clause (so -b before -a, since b > a), single spaces, "
                    "terminating ' 0', LF; clauses in i, then (c,d) lexicographic order")
SCOPE = ("Exact-formula binding (bytes, counts, SHA256) of 16 GB-r2 template formulas and six GB-r2 strengthened "
         "formulas, regenerated in memory by the parent independently of the worker adapter. PLANNED input "
         "identities only: no solver or checker was run, no SAT/UNSAT, transfer, n=8 or Problem-16 claim.")

STATE = {"term": False, "phase": "start", "last_free": None, "last_free_t": None, "min_free": None,
         "free_readings": 0, "guards": 0, "clauses_seen": 0}


class Abort(Exception):
    """Cooperative stop (SIGTERM, wall, RSS or free-space limit): the run is UNKNOWN."""


class Stop(Exception):
    """Precondition failure (pin, source, input structure, refused gate): no hashes are produced."""


def on_sigterm(signum, frame):
    STATE["term"] = True


def now_iso():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()


def free_bytes():
    st = os.statvfs(DESK)
    return st.f_bavail * st.f_frsize


def peak_rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss


def read_free(now):
    fb = free_bytes()
    STATE["last_free"], STATE["last_free_t"] = fb, now
    STATE["min_free"] = fb if STATE["min_free"] is None else min(STATE["min_free"], fb)
    STATE["free_readings"] += 1
    return fb


def guard():
    STATE["guards"] += 1
    if STATE["term"]:
        raise Abort("SIGTERM received (phase %s)" % STATE["phase"])
    now = time.monotonic()
    if now - T0 > WALL_LIMIT:
        raise Abort("wall limit: %.1f s > %.0f s (phase %s)" % (now - T0, WALL_LIMIT, STATE["phase"]))
    rss = peak_rss()
    if rss > RSS_LIMIT:
        raise Abort("peak RSS %d B > %d B (phase %s)" % (rss, RSS_LIMIT, STATE["phase"]))
    if STATE["last_free_t"] is None or now - STATE["last_free_t"] >= FREE_PERIOD:
        fb = read_free(now)
        if fb < FREE_FLOOR:
            raise Abort("free space %d B < in-flight floor %d B (phase %s)" % (fb, FREE_FLOOR, STATE["phase"]))


def require_lines(text, lines, what):
    have = set(text.split("\n"))
    missing = [x for x in lines if x not in have]
    if missing:
        raise Stop("%s: exact lines missing: %r" % (what, missing))
    return list(lines)


# ----------------------------------------------------------------------------------------------- GB source facts
def top_level(tree):
    top = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            if node.name in top:
                raise Stop("GB: duplicate top-level definition " + node.name)
            top[node.name] = node
        elif isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for t in targets:
                if isinstance(t, ast.Name) and t.id in ("F", "encode", "main"):
                    raise Stop("GB: module-level rebinding of " + t.id)
    return top


def gb_ast_facts(tree):
    """encode() touches its F instance only through F_.new(...) calls and F_.c(...) expression statements
    (return values discarded), never reads F_.cl/F_.n/F_.tab, never aliases F_, and creates it by a bare F().
    Hence replacing only F.c's storage cannot change which clauses are emitted, their order or the numbering."""
    top = top_level(tree)
    cls, enc = top.get("F"), top.get("encode")
    if not isinstance(cls, ast.ClassDef) or not isinstance(enc, ast.FunctionDef):
        raise Stop("GB: class F / def encode not found")
    methods = [n.name for n in cls.body if isinstance(n, ast.FunctionDef)]
    if sorted(methods) != ["__init__", "c", "new"] or len(cls.body) != 3 or cls.bases or cls.decorator_list:
        raise Stop("GB: class F shape %r" % methods)
    parents = {}
    for node in ast.walk(enc):
        for ch in ast.iter_child_nodes(node):
            parents[ch] = node
    attr_uses, assigns, returns, other, f_refs = {}, 0, 0, [], []
    c_calls = c_stmt = 0
    for node in ast.walk(enc):
        if isinstance(node, ast.Name) and node.id == "F_":
            par = parents.get(node)
            if isinstance(par, ast.Attribute) and par.value is node:
                attr_uses[par.attr] = attr_uses.get(par.attr, 0) + 1
                call = parents.get(par)
                if not (isinstance(call, ast.Call) and call.func is par):
                    other.append("F_.%s not called (line %d)" % (par.attr, node.lineno))
                elif par.attr == "c":
                    c_calls += 1
                    if isinstance(parents.get(call), ast.Expr):
                        c_stmt += 1
            elif isinstance(par, ast.Assign) and any(t is node for t in par.targets):
                assigns += 1
            elif isinstance(par, ast.Return) and par.value is node:
                returns += 1
            else:
                other.append("F_ used in %s (line %d)" % (type(par).__name__, node.lineno))
        elif isinstance(node, ast.Name) and node.id == "F":
            par = parents.get(node)
            f_refs.append(isinstance(par, ast.Call) and par.func is node and not par.args and not par.keywords)
        elif isinstance(node, (ast.Global, ast.Nonlocal)) and ({"F_", "F"} & set(node.names)):
            other.append("global/nonlocal F_/F (line %d)" % node.lineno)
    facts = {"class_F_methods": methods, "F_instance_attribute_uses_in_encode": attr_uses,
             "F_instance_assignments_in_encode": assigns, "F_instance_returns_in_encode": returns,
             "F_instance_other_uses_in_encode": other, "F_c_calls": c_calls,
             "F_c_calls_that_are_expression_statements": c_stmt,
             "class_F_references_in_encode": len(f_refs), "class_F_reference_is_bare_call": all(f_refs)}
    ok = (set(attr_uses) == {"new", "c"} and assigns == 1 and returns == 1 and not other
          and c_calls == c_stmt == attr_uses.get("c") and f_refs == [True])
    if not ok:
        raise Stop("GB encode storage-interface facts violated: %r" % facts)
    return facts


def refuse_open(*args, **kwargs):
    raise Stop("main() statement tried to open a file: %r" % (args,))


def flags_to_call(tree):
    """Evaluate main()'s own parser construction and its Q/p4/fixg/encode-argument statements on FLAGS."""
    main_def = top_level(tree).get("main")
    if not isinstance(main_def, ast.FunctionDef):
        raise Stop("GB: def main not found")
    adds, assigns = [], {}
    for st in main_def.body:
        if (isinstance(st, ast.Expr) and isinstance(st.value, ast.Call) and isinstance(st.value.func, ast.Attribute)
                and st.value.func.attr == "add_argument" and isinstance(st.value.func.value, ast.Name)
                and st.value.func.value.id == "ap"):
            adds.append(st)
        elif isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Name):
            assigns.setdefault(st.targets[0].id, []).append(st)
    for name in ("ap", "a", "Q", "p4", "fixg", "F_"):
        if len(assigns.get(name, [])) != 1:
            raise Stop("GB main(): expected exactly one assignment to " + name)
    call = assigns["F_"][0].value
    if not (isinstance(call, ast.Call) and isinstance(call.func, ast.Name) and call.func.id == "encode"
            and not call.keywords and len(call.args) == 9):
        raise Stop("GB main(): encode call shape")
    ns = {"argparse": argparse, "json": json, "open": refuse_open}

    def run(st):
        exec(compile(ast.Module(body=[st], type_ignores=[]), GB, "exec", dont_inherit=True), ns)

    run(assigns["ap"][0])
    for st in adds:
        run(st)
    ns["a"] = ns["ap"].parse_args(FLAGS + ["--cnf", "NOT-WRITTEN.cnf"])
    for name in ("Q", "p4", "fixg"):
        run(assigns[name][0])
    args = [eval(compile(ast.Expression(body=x), GB, "eval", dont_inherit=True), ns) for x in call.args]
    parsed = {k: v for k, v in sorted(vars(ns["a"]).items()) if k != "cnf"}
    return args, parsed, len(adds)


def load_gb(src, name):
    """Fresh module object from the verified bytes (no sys.path / sys.modules change; __name__ != '__main__')."""
    spec = importlib.util.spec_from_loader(name, loader=None, origin=GB)
    mod = importlib.util.module_from_spec(spec)
    mod.__file__ = GB
    exec(compile(src, GB, "exec", dont_inherit=True), mod.__dict__)
    return mod


def make_sink_class(base, segment):
    class GBSinkF(base):
        """Clause storage replaced by an in-memory byte sink; F.new / F.n / F.tab inherited unchanged."""
        SEGMENT_BYTES = segment

        def __init__(self):
            base.__init__(self)
            self.cl = None              # the list storage is switched off; any use of F.cl raises
            self.ncl = 0
            self.segments = []          # frozen full segments (bytes), in emission order
            self.cur = bytearray()      # current segment

        def c(self, *lits):
            # exactly main()'s line for the stored clause list(lits): " ".join(map(str, cl)) + " 0\n"
            self.cur += (" ".join(map(str, lits)) + " 0\n").encode("ascii")
            self.ncl += 1
            if len(self.cur) >= self.SEGMENT_BYTES:
                self.segments.append(bytes(self.cur))
                self.cur = bytearray()
            if not self.ncl & GUARD_MASK:
                STATE["clauses_seen"] = self.ncl
                guard()

        def finish(self):
            if self.cur:
                self.segments.append(bytes(self.cur))
            self.cur = None             # no clause can be stored after the header is fixed
            return self.segments
    return GBSinkF


def make_sorted_mutant_class(base, segment):
    """Negative storage control only: a plausible wrong sink that sorts literals inside each clause."""
    sink = make_sink_class(base, segment)

    class SortedMutantF(sink):
        def c(self, *lits):
            sink.c(self, *sorted(lits))
    return SortedMutantF


def cli_reference_bytes(F_):
    """main()'s serialization of the module's own list storage, written through a text layer as open(...,'x')."""
    raw = io.BytesIO()
    fh = io.TextIOWrapper(raw, encoding="utf-8", newline=None, write_through=True)
    fh.write("p cnf %d %d\n" % (F_.n, len(F_.cl)))
    for cl in F_.cl:
        fh.write(" ".join(map(str, cl)) + " 0\n")
    fh.flush()
    out = raw.getvalue()
    fh.detach()
    return out


def storage_control(src):
    STATE["phase"] = "storage-control-n5"
    ref_mod = load_gb(src, "gram_b_r2_pinned_control_reference")
    fa = ref_mod.encode(**CONTROL_CALL)
    ref = cli_reference_bytes(fa)
    ref_tab, ref_n, ref_ncl = list(fa.tab.items()), fa.n, len(fa.cl)
    del fa, ref_mod
    guard()
    res = {"instance": "encode(5,[1,2],0,[1],True,fixg=None,g5=True,allrows=False,allcols=False) -- same flag "
                       "pattern as n=8 (sb2 needs len(Q)=n-3); the CLI's --order choices (7,8) are bypassed by "
                       "calling encode() directly, the same in-memory path used at n=8",
           "reference": "pinned module object with its own list storage (F.cl), serialized by main()'s lines through "
                        "io.TextIOWrapper(newline=None) like open(a.cnf,'x')",
           "reference_vars": ref_n, "reference_clauses": ref_ncl, "reference_bytes": len(ref),
           "reference_sha256": sha(ref), "reference_ascii": all(b < 128 for b in ref), "sinks": []}
    ok = res["reference_ascii"]
    for seg in (CONTROL_SEGMENT, SEGMENT):
        mod = load_gb(src, "gram_b_r2_pinned_control_sink_%d" % seg)
        mod.F = make_sink_class(mod.F, seg)
        fb = mod.encode(**CONTROL_CALL)
        segs = fb.finish()
        got = b"p cnf %d %d\n" % (fb.n, fb.ncl) + b"".join(segs)
        row = {"segment_bytes": seg, "segments": len(segs), "bytes": len(got), "sha256": sha(got),
               "byte_identical_to_reference": got == ref, "vars_equal": fb.n == ref_n,
               "clauses_equal": fb.ncl == ref_ncl, "name_table_identical_incl_order": list(fb.tab.items()) == ref_tab,
               "segments_end_on_clause_boundary": all(x.endswith(b" 0\n") for x in segs),
               "list_storage_disabled": fb.cl is None}
        ok = ok and all(v for k, v in row.items() if k not in ("segment_bytes", "segments", "bytes", "sha256"))
        ok = ok and (row["segments"] > 1) == (seg == CONTROL_SEGMENT)
        res["sinks"].append(row)
        del fb, segs, got, mod
        guard()
    mod = load_gb(src, "gram_b_r2_pinned_control_mutant")
    mod.F = make_sorted_mutant_class(mod.F, SEGMENT)
    fm = mod.encode(**CONTROL_CALL)
    got = b"p cnf %d %d\n" % (fm.n, fm.ncl) + b"".join(fm.finish())
    res["negative_sorted_literal_sink"] = {"sha256": sha(got), "byte_identical_to_reference": got == ref,
                                           "detected": got != ref}
    ok = ok and got != ref
    del fm, got, mod
    res["pass"] = ok
    guard()
    return res


# ------------------------------------------------------------------------------------------------- inputs
def check_inputs():
    STATE["phase"] = "pins-and-sources"
    raw, rows = {}, []
    for path, exp in PINS.items():
        b = read_bytes(path)
        got = sha(b)
        rows.append({"path": path, "expected_sha256": exp, "sha256": got, "bytes": len(b), "ok": got == exp})
        if got != exp:
            raise Stop("pin mismatch %s: %s != %s" % (path, got, exp))
        raw[path] = b
    src = raw[GB]
    src_text = src.decode("utf-8")
    tree = ast.parse(src_text, GB)
    checks = {"gb_exact_lines": require_lines(src_text, GB_LINES, "gram_b_r2.py"),
              "gb_ast_facts": gb_ast_facts(tree)}
    args, parsed, nadds = flags_to_call(tree)
    if json.dumps(args) != BRIEF_CALL_JSON:
        raise Stop("flags map to %s, brief says %s" % (json.dumps(args), BRIEF_CALL_JSON))
    checks["flags"] = " ".join(FLAGS)
    checks["flags_parsed_by_main_parser"] = parsed
    checks["main_add_argument_statements_evaluated"] = nadds
    checks["encode_args_from_main_statements"] = json.loads(json.dumps(args))
    checks["encode_args_equal_brief_call"] = True
    nf_text = raw[NF_R2].decode("utf-8")
    missing = [f for f in NF_FRAGMENTS if f not in nf_text]
    if missing:
        raise Stop("normal form r2 fragments missing: %r" % missing)
    checks["normal_form_r2_fragments"] = list(NF_FRAGMENTS)
    checks["ga_leaf_script_lines"] = require_lines(raw[GA_LEAF_SCRIPT].decode("utf-8"), GA_LEAF_LINES,
                                                   "parent_binding_v1.py")
    checks["ga_strong_script_lines"] = require_lines(raw[GA_STRONG_SCRIPT].decode("utf-8"), GA_STRONG_LINES,
                                                     "bind_v1.py")
    ga_binding = json.loads(raw[GA_STRONG_BINDING])
    if not (ga_binding.get("status") == "MATCH"
            and ga_binding.get("tail_derivation", {}).get("serialization") == GA_SERIALIZATION
            and "clause count + 126, variable count unchanged" in ga_binding.get("composition_rule", "")
            and "the M_s tail appended after the last unit line" in ga_binding.get("composition_rule", "")):
        raise Stop("GA BINDING.json convention fields")
    checks["ga_binding_status"] = ga_binding["status"]
    checks["ga_binding_composition_rule"] = ga_binding["composition_rule"]
    checks["ga_binding_tail_serialization"] = ga_binding["tail_derivation"]["serialization"]
    ga_leaf = json.loads(raw[GA_LEAF_RESULT])
    wman = json.loads(raw[WMAN])
    if wman.get("schema") != "n8-one-p4-template-manifest/1":
        raise Stop("WMAN schema")
    cases = wman.get("cases") or []
    if [c.get("id") for c in cases] != EXPECTED_IDS or wman.get("run_cases") != EXPECTED_IDS:
        raise Stop("WMAN case ids")
    sup = {}
    for c in cases:
        S = c.get("supports_row2to7")
        good = (isinstance(S, list) and len(S) == 6 and all(
            isinstance(r, list) and r and r == sorted(set(r)) and all(type(x) is int and 1 <= x <= 7 for x in r)
            for r in S))
        U = c.get("units")
        if not good or not (isinstance(U, list) and len(U) == UNITS and all(type(u) is int and u != 0 for u in U)):
            raise Stop("WMAN case structure " + str(c.get("id")))
        sup[c["id"]] = [list(r) for r in S]
    return {"raw": raw, "rows": rows, "src": src, "args": args, "checks": checks, "ga_binding": ga_binding,
            "ga_leaf": ga_leaf, "wman": wman, "sup": sup}


# ------------------------------------------------------------------------------------- composition and controls
def primary_of(key):
    """(s, c, i) if key is a GB primary name ('g', s, (0, c), (i, 0)) with c, i in 1..7, else None."""
    if (isinstance(key, tuple) and len(key) == 4 and key[0] == "g" and type(key[1]) is int
            and isinstance(key[2], tuple) and isinstance(key[3], tuple) and len(key[2]) == 2 and len(key[3]) == 2
            and key[2][0] == 0 and key[3][1] == 0 and key[2][1] in COORDS and key[3][0] in range(1, 8)):
        return key[1], key[2][1], key[3][0]
    return None


def unit_section(lits):
    return "".join("%d 0\n" % u for u in lits).encode("ascii")


def compose(tab, V, C, segs, sup, wman, ga_binding, ga_leaf):
    failures = []

    def gate(name, ok):
        if not ok:
            failures.append(name)
        return bool(ok)

    STATE["phase"] = "name-table"
    inv = {}
    for k, v in tab.items():
        if v in inv:
            raise Stop("GB name table is not injective (id %d)" % v)
        inv[v] = k
    prim = {}
    for s in range(1, 6):
        for c in COORDS:
            for i in range(1, 8):
                key = ("g", s, (0, c), (i, 0))
                if key not in tab:
                    raise Stop("GB primary name missing: %r" % (key,))
                prim[(s, c, i)] = tab[key]
    name_checks = {
        "true_id": tab.get("TRUE"),
        "true_id_is_1": gate("TRUE id is 1", tab.get("TRUE") == 1),
        "primary_entries_s1to5_c1to7_i1to7": len(prim),
        "primary_ids_distinct": gate("245 primary ids distinct", len(set(prim.values())) == 245),
        "primary_ids_in_2_to_V": gate("primary ids in 2..V", all(2 <= v <= V for v in prim.values())),
        "name_table_entries": len(tab), "name_table_injective": True,
        "observation_g_entries": sum(1 for k in tab if isinstance(k, tuple) and k and k[0] == "g"),
        "observation_L_entries": sum(1 for k in tab if isinstance(k, tuple) and k and k[0] == "L"),
        "observation_ids_equal_1568(s-1)+49c+7i-5": all(
            v == 1568 * (s - 1) + 49 * c + 7 * i - 5 for (s, c, i), v in prim.items()),
    }
    map_lines = ["# GB-r2 F.tab primary ids g_s((0,c),(i,0)) = F.tab[('g', s, (0, c), (i, 0))], s=1..5, c=1..7, "
                 "i=1..7 (245 rows, sorted by s, c, i); constant F.tab['TRUE'] = %d; columns: s c i gb_id"
                 % tab.get("TRUE")]
    map_lines += ["%d %d %d %d" % (s, c, i, prim[(s, c, i)]) for (s, c, i) in sorted(prim)]
    map_bytes = ("\n".join(map_lines) + "\n").encode("ascii")
    cli_map = json.dumps({json.dumps(k): v for k, v in tab.items()}).encode("ascii")

    STATE["phase"] = "body-hashing"
    body_bytes = body_lines = body_terms = 0
    aligned = True
    hb = hashlib.sha256()
    for x in segs:
        body_bytes += len(x)
        body_lines += x.count(b"\n")
        body_terms += x.count(b" 0\n")
        aligned = aligned and x.endswith(b" 0\n")
        hb.update(x)
        guard()
    gate("(e) body LF count == stored clause count", body_lines == C)
    gate("(e) body ' 0\\n' terminator count == stored clause count", body_terms == C)
    gate("body segments end on clause boundaries", aligned)
    header_base = b"p cnf %d %d\n" % (V, C)
    header_tpl = b"p cnf %d %d\n" % (V, C + UNITS)
    header_str = b"p cnf %d %d\n" % (V, C + UNITS + TAIL)

    def prefixed(prefix):
        h = hashlib.sha256(prefix)
        for x in segs:
            h.update(x)
            guard()
        return h

    h_base, h_tpl, h_str = prefixed(header_base), prefixed(header_tpl), prefixed(header_str)
    base = {"vars": V, "clauses": C, "header": header_base.decode("ascii"), "body_bytes": body_bytes,
            "body_sha256": hb.hexdigest(), "body_LF_count": body_lines, "body_clause_terminators": body_terms,
            "body_segments": len(segs), "base_cnf_sha256_cli_equivalent": h_base.hexdigest(),
            "base_cnf_bytes_cli_equivalent": len(header_base) + body_bytes,
            "cli_map_json_sha256_equivalent": sha(cli_map), "cli_map_json_bytes_equivalent": len(cli_map)}

    STATE["phase"] = "composition"
    units, ubytes = {}, {}
    for t in EXPECTED_IDS:
        lits = []
        for i, S in zip(ROWS, sup[t]):
            for c in COORDS:
                v = tab[("g", 1, (0, c), (i, 0))]
                lits.append(v if c in S else -v)
        units[t], ubytes[t] = lits, unit_section(lits)
    tails, tbytes = {}, {}
    for s in (2, 3, 4, 5):
        cls = []
        for i in ROWS:
            for c, d in itertools.combinations(COORDS, 2):
                a = tab[("g", s, (0, c), (i, 0))]
                b = tab[("g", s, (0, d), (i, 0))]
                cls.append(tuple(sorted((-a, -b))))
        tails[s], tbytes[s] = cls, "".join("%d %d 0\n" % cl for cl in cls).encode("ascii")
    tail_info = {str(s): {"sha256": sha(tbytes[s]), "bytes": len(tbytes[s]), "clauses": len(tails[s]),
                          "distinct": len(set(tails[s])) == TAIL, "first_line": tbytes[s].split(b"\n")[0].decode(),
                          "used_by": [f for f, _t, s2 in FORMULAS if s2 == s]} for s in (2, 3, 4, 5)}
    formulas, genuine = [], {}
    for t in EXPECTED_IDS:
        h = h_tpl.copy()
        h.update(ubytes[t])
        rec = {"id": t, "kind": "template", "direct": t in DIRECT12, "source_template": t, "monomial_square": None,
               "header": header_tpl.decode("ascii"), "variables": V, "clauses": C + UNITS,
               "bytes": len(header_tpl) + body_bytes + len(ubytes[t]), "sha256": h.hexdigest(),
               "pieces": {"header_bytes": len(header_tpl), "body_sha256": base["body_sha256"],
                          "body_bytes": body_bytes, "body_clauses": C, "units_sha256": sha(ubytes[t]),
                          "units_bytes": len(ubytes[t]), "units_lines": ubytes[t].count(b"\n")},
               "supports_row2to7": sup[t]}
        formulas.append(rec)
        genuine[t] = rec["sha256"]
    for fid, t, s in FORMULAS:
        h = h_str.copy()
        h.update(ubytes[t])
        h.update(tbytes[s])
        rec = {"id": fid, "kind": "strengthened", "direct": False, "source_template": t, "monomial_square": s,
               "header": header_str.decode("ascii"), "variables": V, "clauses": C + UNITS + TAIL,
               "bytes": len(header_str) + body_bytes + len(ubytes[t]) + len(tbytes[s]), "sha256": h.hexdigest(),
               "pieces": {"header_bytes": len(header_str), "body_sha256": base["body_sha256"],
                          "body_bytes": body_bytes, "body_clauses": C, "units_sha256": sha(ubytes[t]),
                          "units_bytes": len(ubytes[t]), "units_lines": ubytes[t].count(b"\n"),
                          "tail_sha256": sha(tbytes[s]), "tail_bytes": len(tbytes[s]),
                          "tail_lines": tbytes[s].count(b"\n")},
               "supports_row2to7": sup[t]}
        formulas.append(rec)
        genuine[fid] = rec["sha256"]
    gate("22 formula hashes distinct", len(set(genuine.values())) == 22)
    all_genuine = set(genuine.values())
    guard()

    STATE["phase"] = "controls"
    ctl = {}
    # (a) every single unit sign flip changes the formula hash; a flip may equal another genuine formula only
    #     when the composed pieces coincide (same header and tail, identical unit list)
    by_pieces = {}
    for rec in formulas:
        by_pieces.setdefault((rec["monomial_square"], tuple(units[rec["source_template"]])), []).append(rec["id"])
    a_rows = {}
    for rec in formulas:
        t, s = rec["source_template"], rec["monomial_square"]
        mhs, cross, predicted = [], [], True
        for k in range(UNITS):
            m = list(units[t])
            m[k] = -m[k]
            h = (h_tpl if s is None else h_str).copy()
            h.update(unit_section(m))
            if s is not None:
                h.update(tbytes[s])
            x = h.hexdigest()
            mhs.append(x)
            observed = sorted(f for f, v in genuine.items() if v == x)
            if observed != sorted(by_pieces.get((s, tuple(m)), [])):
                predicted = False
            if observed:
                cross.append({"k": k, "i": 2 + k // 7, "c": 1 + k % 7, "equals_genuine": observed})
        row = {"mutants": len(mhs), "all_differ_from_own_genuine": all(x != rec["sha256"] for x in mhs),
               "mutants_distinct": len(set(mhs)) == UNITS,
               "equalities_with_other_genuine_exactly_as_predicted_from_pieces": predicted,
               "equal_to_other_genuine": cross, "first_unit_flip_sha256": mhs[0]}
        a_rows[rec["id"]] = row
        gate("(a) unit sign flips " + rec["id"], row["all_differ_from_own_genuine"] and row["mutants_distinct"]
             and predicted)
    ctl["a_unit_sign_flips"] = {"rule": "each of the 42 unit literals negated in turn (42 mutants per formula, header "
                                        "and clause count unchanged); every mutant must differ from its own formula, "
                                        "the 42 must be distinct, and a mutant may equal another genuine formula only "
                                        "where the composed pieces are identical (one-unit template neighbours)",
                                "per_formula": a_rows}

    def decode_units(ub):
        out, errs = [], []
        lines = ub.split(b"\n")
        if lines[-1] != b"":
            errs.append("no final LF")
        for line in lines[:-1]:
            mt = UNIT_RE.fullmatch(line)
            pk = primary_of(inv.get(abs(int(mt.group(1))))) if mt else None
            if pk is None:
                errs.append(line.decode("ascii", "replace"))
                continue
            out.append((pk[0], pk[1], pk[2], 1 if int(mt.group(1)) > 0 else -1))
        return out, errs

    def decode_tail(tb):
        out, errs = [], []
        lines = tb.split(b"\n")
        if lines[-1] != b"":
            errs.append("no final LF")
        for line in lines[:-1]:
            mt = TAIL_RE.fullmatch(line)
            if not mt:
                errs.append(line.decode("ascii", "replace"))
                continue
            l1, l2 = int(mt.group(1)), int(mt.group(2))
            p1, p2 = primary_of(inv.get(-l1)), primary_of(inv.get(-l2))
            if p1 is None or p2 is None:
                errs.append(line.decode("ascii", "replace"))
                continue
            out.append((p1[0], p2[0], p1[2], p2[2], tuple(sorted((p1[1], p2[1]))), l1 < l2))
        return out, errs

    def supports_from(decoded):
        S, seen, ok = {i: [] for i in ROWS}, set(), True
        for s, c, i, sg in decoded:
            if s != 1 or i not in S or (c, i) in seen:
                ok = False
                continue
            seen.add((c, i))
            if sg > 0:
                S[i].append(c)
        return ok and len(seen) == UNITS, [sorted(S[i]) for i in ROWS]

    # (b) swapped-square tail: square-3 ids in each s=2 formula
    b_rows = {}
    dec3, err3 = decode_tail(tbytes[3])
    for fid, t, s in FORMULAS:
        if s != 2:
            continue
        h = h_str.copy()
        h.update(ubytes[t])
        h.update(tbytes[3])
        x = h.hexdigest()
        equals = sorted(k for k, v in genuine.items() if v == x)
        expected = ["P1-B5.M3"] if t == "P1-B5" else []
        row = {"mutant": "M_3 tail (square-3 GB ids) in place of the M_2 tail; header unchanged",
               "mutant_sha256": x, "differs_from_genuine": x != genuine[fid], "equals_genuine": equals,
               "expected_equal_genuine": expected,
               "mutant_tail_decodes_to_squares": sorted({r[0] for r in dec3} | {r[1] for r in dec3})}
        b_rows[fid] = row
        gate("(b) swapped-square tail " + fid, row["differs_from_genuine"] and equals == expected and not err3
             and row["mutant_tail_decodes_to_squares"] == [3])
    ctl["b_swapped_square_tail"] = b_rows
    bb = {}
    for fid, t, s in FORMULAS:
        first, rest = tbytes[s].split(b"\n", 1)
        l1, l2, z = first.split(b" ")
        mut = b"%d %s %s\n" % (-int(l1), l2, z) + rest
        h = h_str.copy()
        h.update(ubytes[t])
        h.update(mut)
        x = h.hexdigest()
        bb[fid] = {"mutant": "first tail literal sign-flipped", "mutant_sha256": x, "differs": x not in all_genuine}
        gate("(b2) tail first-literal flip " + fid, x not in all_genuine)
    ctl["b2_tail_first_literal_flip"] = bb

    # (c) decode every appended literal through the inverse GB name table
    c_rows = {}
    for rec in formulas:
        t, s = rec["source_template"], rec["monomial_square"]
        du, eu = decode_units(ubytes[t])
        exp_u = [(1, c, i, 1 if c in S else -1) for i, S in zip(ROWS, sup[t]) for c in COORDS]
        row = {"unit_lines": len(du) + len(eu), "unit_decode_errors": eu,
               "units_decode_to_intended_(s=1,c,i,sign)_in_order": du == exp_u}
        ok = not eu and du == exp_u
        if s is not None:
            dt, et = decode_tail(tbytes[s])
            exp_t = [(s, s, i, i, (c, d), True) for i in ROWS for c, d in itertools.combinations(COORDS, 2)]
            row.update({"tail_lines": len(dt) + len(et), "tail_decode_errors": et,
                        "tail_decodes_to_intended_(s,i,c<d)_in_order_negative_ascending": dt == exp_t})
            ok = ok and not et and dt == exp_t
        row["max_appended_var"] = max([abs(u) for u in units[t]] + ([-x for cl in tails[s] for x in cl] if s else []))
        row["max_appended_var_le_V"] = row["max_appended_var"] <= V
        ok = ok and row["max_appended_var_le_V"]
        c_rows[rec["id"]] = row
        gate("(c) decode " + rec["id"], ok)
    ctl["c_decode_inverse_name_table"] = c_rows

    # (d) support semantics decoded from the unit lines (position-free) equal the WMAN supports
    d_rows = {}
    for rec in formulas:
        t = rec["source_template"]
        okd, got = supports_from(decode_units(ubytes[t])[0])
        m = list(units[t])
        m[0] = -m[0]
        okn, gotn = supports_from(decode_units(unit_section(m))[0])
        row = {"decoded_supports_row2to7": got, "equal_wman": okd and got == sup[t],
               "negative_first_unit_flip_detected": gotn != sup[t]}
        d_rows[rec["id"]] = row
        gate("(d) supports " + rec["id"], row["equal_wman"] and row["negative_first_unit_flip_detected"])
    ctl["d_support_semantics"] = {"direct12": DIRECT12, "normal_form_sources": list(NF_SOURCES),
                                  "direct12_all_equal": all(d_rows[t]["equal_wman"] for t in DIRECT12),
                                  "all16_templates_equal": all(d_rows[t]["equal_wman"] for t in EXPECTED_IDS),
                                  "six_strengthened_unit_sections_equal": all(d_rows[f]["equal_wman"]
                                                                             for f, _t, _s in FORMULAS),
                                  "per_formula": d_rows}

    # (e) clause-count identity C_formula = C_base + 42 (+126), V unchanged, byte length identity
    e_rows = {}
    for rec in formulas:
        t, s = rec["source_template"], rec["monomial_square"]
        mt = re.fullmatch(r"p cnf (\d+) (\d+)\n", rec["header"])
        nu = ubytes[t].count(b"\n")
        nt = tbytes[s].count(b"\n") if s is not None else 0
        want = C + UNITS + (TAIL if s is not None else 0)
        row = {"header_vars": int(mt.group(1)), "header_clauses": int(mt.group(2)), "C_base": C,
               "unit_lines": nu, "tail_lines": nt, "identity": "C_base + 42" + (" + 126" if s is not None else ""),
               "holds": (int(mt.group(1)) == V and int(mt.group(2)) == want == body_lines + nu + nt and nu == UNITS
                         and nt == (TAIL if s is not None else 0)
                         and rec["bytes"] == len(rec["header"]) + body_bytes + len(ubytes[t])
                         + (len(tbytes[s]) if s is not None else 0))}
        e_rows[rec["id"]] = row
        gate("(e) clause-count identity " + rec["id"], row["holds"])
    ctl["e_clause_count_identity"] = e_rows

    # (f) GA reference cross-check of the conventions (GA ids are never used in any GB formula)
    ga_units = {c["id"]: c["units"] for c in wman["cases"]}
    f_rows = {}
    for t in EXPECTED_IDS:
        gu = ga_units[t]
        row = {"sign_pattern_equal_ga_units": [1 if u > 0 else -1 for u in gu] == [1 if u > 0 else -1 for u in units[t]],
               "ga_unit_positions_follow_i_major_c_minor_49c+7i-6": all(
                   abs(gu[k]) == 49 * (1 + k % 7) + 7 * (2 + k // 7) - 6 for k in range(UNITS))}
        f_rows[t] = row
        gate("(f) GA unit-convention cross-check " + t, all(row.values()))
    gb_rows = [(i, c, d) for i in ROWS for c, d in itertools.combinations(COORDS, 2)]
    tails_ga = ga_binding["tail_derivation"]["tails"]
    rows_eq = {str(s): [tuple(r[:3]) for r in tails_ga[str(s)]["derivation_rows_i_c_d_a_b_line"]] == gb_rows
               for s in (2, 3, 4, 5)}
    ga_f = [(f["id"], f["source_template"], f["monomial_square"]) for f in ga_binding["formulas"]]
    leaves = ga_leaf.get("leaves") or []
    f_misc = {"ga_tail_row_order_i_c_d_equal": rows_eq, "ga_formula_list_equal": ga_f == list(FORMULAS),
              "ga_leaf_result_status": ga_leaf.get("status"),
              "ga_leaf_ids_equal_wman": [x.get("id") for x in leaves] == EXPECTED_IDS,
              "ga_leaf_template_table_and_units_equal_all16": all(x.get("template_table_equal") is True
                                                                 and x.get("units_equal") is True for x in leaves)}
    gate("(f) GA tail row order", all(rows_eq.values()))
    gate("(f) GA formula list", f_misc["ga_formula_list_equal"])
    gate("(f) GA leaf provenance", f_misc["ga_leaf_result_status"] == "PASS" and f_misc["ga_leaf_ids_equal_wman"]
         and f_misc["ga_leaf_template_table_and_units_equal_all16"])
    ctl["f_ga_reference_crosscheck"] = {"per_template": f_rows, **f_misc}
    guard()
    return {"failures": failures, "name_checks": name_checks, "map_bytes": map_bytes, "base": base,
            "tails": tail_info, "formulas": formulas, "controls": ctl}


# ---------------------------------------------------------------------------------------------------- modes
def synthetic():
    tab = {"TRUE": 1}
    nid = 100
    for s in range(1, 6):
        for c in COORDS:
            for i in range(1, 8):
                nid += 3
                tab[("g", s, (0, c), (i, 0))] = nid
    return tab, nid + 7, 2, [b"1 0\n", b"-2 3 0\n"]


def selftest(ctx):
    res = {"storage_control_n5": storage_control(ctx["src"])}
    STATE["phase"] = "selftest-synthetic"
    tab, V, C, segs = synthetic()
    pos = compose(tab, V, C, segs, ctx["sup"], ctx["wman"], ctx["ga_binding"], ctx["ga_leaf"])
    manifest_text = json.dumps({k: v for k, v in pos.items() if k != "map_bytes"}, indent=1)
    res["synthetic_positive"] = {"failures": pos["failures"], "pass": not pos["failures"],
                                 "manifest_json_bytes": len(manifest_text), "map_bytes": len(pos["map_bytes"]),
                                 "a_equalities_with_other_genuine": {
                                     f: r["equal_to_other_genuine"]
                                     for f, r in pos["controls"]["a_unit_sign_flips"]["per_formula"].items()
                                     if r["equal_to_other_genuine"]}}
    neg1 = compose(tab, V, C + 1, segs, ctx["sup"], ctx["wman"], ctx["ga_binding"], ctx["ga_leaf"])
    bad_sup = {k: [list(r) for r in v] for k, v in ctx["sup"].items()}
    bad_sup["P0-B1"][0] = [6]
    neg2 = compose(tab, V, C, segs, bad_sup, ctx["wman"], ctx["ga_binding"], ctx["ga_leaf"])
    res["synthetic_negative_wrong_clause_count"] = {"failures": neg1["failures"],
                                                    "detected": "(e) body LF count == stored clause count" in neg1["failures"]}
    res["synthetic_negative_altered_support"] = {"failures": neg2["failures"],
                                                 "detected": "(f) GA unit-convention cross-check P0-B1" in neg2["failures"]}
    res["pass"] = (res["storage_control_n5"]["pass"] and res["synthetic_positive"]["pass"]
                   and res["synthetic_negative_wrong_clause_count"]["detected"]
                   and res["synthetic_negative_altered_support"]["detected"])
    return res


def generate(ctx, script_sha, expected_sha, started, timing):
    t = time.monotonic()
    ctl5 = storage_control(ctx["src"])
    timing["storage_control_n5_s"] = round(time.monotonic() - t, 2)
    if not ctl5["pass"]:
        raise Stop("storage control failed: %s" % json.dumps(ctl5))
    rss_before = peak_rss()
    STATE["phase"] = "encode-n8"
    t = time.monotonic()
    mod = load_gb(ctx["src"], "gram_b_r2_pinned_generation")
    pristine_F = mod.F
    mod.F = make_sink_class(pristine_F, SEGMENT)
    F8 = mod.encode(*ctx["args"])
    segs = F8.finish()
    V, C = F8.n, F8.ncl
    timing["encode_n8_s"] = round(time.monotonic() - t, 2)
    print("encode n=8 done: vars %d clauses %d segments %d peak_rss %d" % (V, C, len(segs), peak_rss()), flush=True)
    guard()
    t = time.monotonic()
    out = compose(F8.tab, V, C, segs, ctx["sup"], ctx["wman"], ctx["ga_binding"], ctx["ga_leaf"])
    timing["compose_and_controls_s"] = round(time.monotonic() - t, 2)
    STATE["phase"] = "write"
    map_sha = sha(out["map_bytes"])
    with open(OUT_MAP, "xb") as f:
        f.write(out["map_bytes"])
    ru = resource.getrusage(resource.RUSAGE_SELF)
    failures = out["failures"]
    manifest = {
        "schema": "moqls8-gb-parent-binding/1", "status": "PASS" if not failures else "FAIL", "failures": failures,
        "scope": SCOPE, "desk": DESK, "started_at": started,
        "script": {"path": SCRIPT_REL, "sha256": script_sha, "expected_sha256_from_launcher": expected_sha,
                   "supersedes": SUPERSEDES},
        "python": {"executable": sys.executable, "realpath": os.path.realpath(sys.executable),
                   "version": sys.version, "isolated_flag": sys.flags.isolated,
                   "dont_write_bytecode": sys.dont_write_bytecode, "utf8_mode": sys.flags.utf8_mode,
                   "os_linesep": os.linesep, "pid": os.getpid(), "argv": sys.argv},
        "inputs_pinned": ctx["rows"],
        "worker_package_not_read": WORKER_PACKAGE_NOT_READ,
        "gb_source_checks": ctx["checks"],
        "storage_replacement": {
            "replaced": "module global F of the generation module object -> subclass of the pinned F overriding "
                        "__init__ (adds the sink, sets F.cl = None) and c(*lits) (appends the ASCII bytes of "
                        "' '.join(map(str, lits)) + ' 0\\n' to a bytearray segment; 16 MiB segments frozen as bytes)",
            "unchanged": "F.new, F.n, F.tab, encode() and every nested GB function (pinned bytes executed as-is)",
            "why_encoding_cannot_change": "gb_source_checks.gb_ast_facts: encode uses its F instance only via "
                                          "F_.new(...) calls and F_.c(...) expression statements, never reads "
                                          "F_.cl/F_.n/F_.tab, never aliases F_, creates it by a bare F(); the per-"
                                          "clause bytes equal main()'s line for list(lits); header from F.n and "
                                          "the count of c() calls as in main()",
            "segment_bytes": SEGMENT, "storage_control_n5": ctl5},
        "gb_base": out["base"],
        "name_table": out["name_checks"],
        "primary_map_file": {"path": os.path.basename(OUT_MAP), "sha256": map_sha, "bytes": len(out["map_bytes"]),
                             "rows": 245},
        "conventions": {
            "units": "42 lines '%d 0\\n' (ASCII, LF): for i = 2..7 ascending, c = 1..7 ascending: +v if c in WMAN "
                     "supports_row2to7[i-2] of the template, else -v; v = GB F.tab[('g',1,(0,c),(i,0))] (square 1)",
            "tail": "126 lines '%d %d 0\\n' % tuple(sorted((-a,-b))): i = 2..7 ascending, (c,d) in "
                    "itertools.combinations(1..7, 2); a = F.tab[('g',s,(0,c),(i,0))], b = F.tab[('g',s,(0,d),(i,0))]",
            "template_formula": "'p cnf V C+42\\n' + GB base body (unchanged) + 42 unit lines",
            "strengthened_formula": "'p cnf V C+42+126\\n' + GB base body + the source template's 42 unit lines + "
                                    "the M_s tail",
            "V": "GB F.n (unchanged by units/tails: every appended id is an existing GB primary id)",
            "source": "GA parent bindings parent_binding_v1.py (units) and bind_v1.py/BINDING.json (tail, headers); "
                      "exact lines checked in gb_source_checks"},
        "ambiguities_and_choices": [
            "'12 direct templates' read as the 16 WMAN templates minus the four normal-form sources P1-B1/B2/B3/B5; "
            "controls (c)/(d) are run on all 16 templates and on the six strengthened formulas' unit sections.",
            "Square-1 ids are used for the 42 units (Q1 column-0 templates), as in the GA leaves and the brief.",
            "No 'c' comment lines, LF only, single spaces, as main() writes; the strengthened tail follows the "
            "last unit line (GA bind_v1 composition).",
            "M_5 tail is derived and hashed for reference only; none of the six formulas uses it.",
            "In-flight free-space stop 11.5e9 B and launch gate 12.0e9 B per parent clarification for this "
            "in-memory job (frozen defaults were 12e9 / 12.2e9 B)."],
        "tails": out["tails"],
        "formulas": out["formulas"],
        "controls": out["controls"],
        "resources": {"peak_rss_bytes_self": ru.ru_maxrss, "peak_rss_bytes_before_n8_encode": rss_before,
                      "rss_limit_bytes": RSS_LIMIT, "wall_limit_s": WALL_LIMIT,
                      "wall_s_at_write": round(time.monotonic() - T0, 2), "cpu_user_s": round(ru.ru_utime, 2),
                      "cpu_sys_s": round(ru.ru_stime, 2), "phase_seconds": timing,
                      "min_free_bytes_observed": STATE["min_free"], "free_readings": STATE["free_readings"],
                      "free_floor_in_flight": FREE_FLOOR, "free_gate_at_start": FREE_GATE,
                      "guard_calls": STATE["guards"], "threads": 1},
        "cnf_or_proof_bytes_written_to_disk": False, "native_tools_started": 0, "child_processes_started": 0,
        "written_at": now_iso()}
    text = json.dumps(manifest, indent=1) + "\n"
    with open(OUT_MANIFEST, "x") as f:
        f.write(text)
    print("GBBINDING %s status %s sha256 %s" % (OUT_MANIFEST, manifest["status"], sha(text.encode("utf-8"))),
          flush=True)
    for rec in out["formulas"]:
        print("%-9s %s vars %d clauses %d bytes %d" % (rec["id"], rec["sha256"], rec["variables"], rec["clauses"],
                                                      rec["bytes"]), flush=True)
    for x in failures:
        print("FAILED GATE " + x, flush=True)
    return 0 if not failures else 2


def main(argv):
    signal.signal(signal.SIGTERM, on_sigterm)
    started = now_iso()
    selftest_mode = argv[1:] == ["--selftest"]
    record_path = OUT_SELFTEST if selftest_mode else OUT_ABORT
    timing = {}
    script_sha = expected = None
    try:
        if not selftest_mode and not (len(argv) == 2 and re.fullmatch(r"[0-9a-f]{64}", argv[1])):
            raise Stop(__doc__)
        tmp = TMP_SELFTEST if selftest_mode else TMP_GEN
        if os.environ.get("TMPDIR") != tmp + "/" or not os.path.isdir(tmp):
            raise Stop("TMPDIR must be %s/ (existing)" % tmp)
        os.chdir(tmp)
        script_sha = sha(read_bytes(SCRIPT))
        if os.path.realpath(__file__) != SCRIPT:
            raise Stop("script path %s != %s" % (os.path.realpath(__file__), SCRIPT))
        if not selftest_mode:
            expected = argv[1]
            if script_sha != expected:
                raise Stop("script sha256 %s != pinned %s" % (script_sha, expected))
        if os.linesep != "\n":
            raise Stop("os.linesep is not LF")
        fb = read_free(time.monotonic())
        if fb < FREE_GATE:
            print("REFUSED: fresh free %d B < gate %d B; nothing done" % (fb, FREE_GATE), flush=True)
            return 5
        t = time.monotonic()
        ctx = check_inputs()
        timing["pins_and_sources_s"] = round(time.monotonic() - t, 2)
        guard()
        if selftest_mode:
            res = selftest(ctx)
            rec = {"schema": "moqls8-gb-parent-binding-selftest/1", "status": "PASS" if res["pass"] else "FAIL",
                   "started_at": started, "script": {"path": SCRIPT_REL, "sha256": script_sha, "supersedes": SUPERSEDES},
                   "python": {"realpath": os.path.realpath(sys.executable), "version": sys.version},
                   "inputs_pinned": ctx["rows"], "gb_source_checks": ctx["checks"], "results": res,
                   "note": "pre-flight only: no n=8 encode, no formula hashes; synthetic name table in the composition "
                           "exercise", "peak_rss_bytes_self": peak_rss(),
                   "seconds": round(time.monotonic() - T0, 2), "min_free_bytes_observed": STATE["min_free"],
                   "written_at": now_iso()}
            with open(OUT_SELFTEST, "x") as f:
                f.write(json.dumps(rec, indent=1) + "\n")
            print("SELFTEST %s sha256 %s" % (rec["status"], sha(read_bytes(OUT_SELFTEST))), flush=True)
            return 0 if res["pass"] else 2
        return generate(ctx, script_sha, expected, started, timing)
    except (Abort, Stop, Exception) as e:
        kind = "ABORT-UNKNOWN" if isinstance(e, Abort) else ("STOP" if isinstance(e, Stop) else "ERROR")
        rec = {"schema": "moqls8-gb-parent-binding-stop/1", "status": kind, "reason": str(e),
               "traceback": traceback.format_exc() if kind == "ERROR" else None, "phase": STATE["phase"],
               "clauses_seen_at_last_guard": STATE["clauses_seen"], "started_at": started,
               "script_sha256": script_sha, "expected_sha256": expected, "peak_rss_bytes_self": peak_rss(),
               "seconds": round(time.monotonic() - T0, 2), "min_free_bytes_observed": STATE["min_free"],
               "last_free_bytes": STATE["last_free"], "written_at": now_iso()}
        try:
            with open(record_path, "x") as f:
                f.write(json.dumps(rec, indent=1) + "\n")
        except OSError as w:
            print("could not write stop record: %r" % (w,), file=sys.stderr, flush=True)
        print("%s: %s" % (kind, e), file=sys.stderr, flush=True)
        return 3 if kind == "ABORT-UNKNOWN" else 4


if __name__ == "__main__":
    sys.exit(main(sys.argv))
