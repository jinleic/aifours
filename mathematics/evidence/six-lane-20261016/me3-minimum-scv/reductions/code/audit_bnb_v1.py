"""Audit of the optional lower-bound program ctl_f_d1bnb_v1.py (fix (4) of review me3-reductions-codex-v1, a6d34ecb).

A. Binding: sha256 of reductions/code/ctl_f_d1bnb_v1.py must equal the pinned 508b1488...41b7 (the hash in the
   pre-receipts of runs ctl-f-main-v1, ctl-f-mut-*-v1 and the file checked by ctl-f-gradsym-v1).
B. Static acceptance logic (AST of the pinned file):
   B1 the only success flag is `certified = bool(middle_certified and tails_ok)` with
      `middle_certified = (not aborted) and (refuted is None) and not stack`  (completion = EMPTY stack);
   B2 inside `while stack:` every `continue` sits in an `if` whose test is a certain ball comparison `... > La`
      (natural extension or mean-value form) -> a box is dropped only when certified;
   B3 every `break` sits in an `if` body that first sets `aborted = True` or `refuted = ...` (cap, depth, refutation);
   B4 the fall-through (neither certified nor break) pushes both bisection halves (2 x stack.append per branch);
   B5 tails_ok is an exact sympy conjunction; exit code is 0 iff outcome == EXPECT.
C. Library semantics actually relied on (python-flint 0.9.0, EXPLORATORY demonstrations): undecided comparisons are
   False; NaN / infinite balls never compare True; nonnegative_part keeps every true value; dyadic box balls contain
   their endpoints; F_ball(box) contains the point values (inclusion); the gradient on a ball touching u = 0 is not
   finite, so the mean-value test cannot certify such a box (and the code only tries it when 0 < u_lo, u_hi < 2).
D. Run evidence: ctl-f-main-v1 output flags (certify, not aborted, no refutation, empty stack, tails OK) and the
   binary-tree bookkeeping identity processed = 2 * certified_leaves - 1; receipts (exit 0, hashes) of main and
   gradsym runs; the two existing mutation runs report reject.
"""
import os
import sys
import ast
import json
import hashlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: E402,F401
from flint import arb, fmpq, ctx  # noqa: E402

RUN = sys.argv[1]
LANE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RED = os.path.join(LANE, "reductions")
SRC = os.path.join(RED, "code", "ctl_f_d1bnb_v1.py")
PIN = "508b148870fc18e3cb32de6ada1c5245aca4271db92867b959597b4ba29341b7"
ctx.prec = 128
checks = {}


def record(name, ok, detail=None):
    checks[name] = {"pass": bool(ok), "detail": detail}
    if not ok:
        print("FAIL", name, detail)


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


# ---------------- A. binding
raw = open(SRC, "rb").read()
record("A_source_sha256_is_pinned", hashlib.sha256(raw).hexdigest() == PIN, hashlib.sha256(raw).hexdigest())
src = raw.decode()
lines = src.splitlines()
tree = ast.parse(src)

# ---------------- B. static acceptance logic
assigns = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
        assigns.setdefault(node.targets[0].id, []).append((node.lineno, ast.unparse(node.value)))
record("B1_middle_certified_expr", assigns.get("middle_certified") ==
       [(165, "not aborted and refuted is None and (not stack)")], assigns.get("middle_certified"))
record("B1_certified_expr", assigns.get("certified") == [(166, "bool(middle_certified and tails_ok)")],
       assigns.get("certified"))
record("B1_outcome_expr", assigns.get("outcome") == [(167, "'certify' if certified else 'reject'")],
       assigns.get("outcome"))
record("B5_tails_ok_expr", assigns.get("tails_ok") ==
       [(57, "d3_ok and rho_ok and (small_tail > Lq) and (big_tail > Lq)")], assigns.get("tails_ok"))
names_assigned_true = [n.lineno for n in ast.walk(tree) if isinstance(n, ast.Assign)
                       and any(isinstance(tg, ast.Name) and tg.id in ("certified", "middle_certified")
                               for tg in n.targets)]
record("B1_success_flags_assigned_only_once", names_assigned_true == [165, 166], names_assigned_true)
loops = [n for n in tree.body if isinstance(n, ast.While)]
record("B_single_top_level_while_stack", len(loops) == 1 and ast.unparse(loops[0].test) == "stack",
       [ast.unparse(x.test) for x in loops])
loop = loops[0]
parent = {}
for node in ast.walk(loop):
    for ch in ast.iter_child_nodes(node):
        parent[ch] = node
conts, brks = [], []
for node in ast.walk(loop):
    if isinstance(node, ast.Continue):
        conts.append(node)
    if isinstance(node, ast.Break):
        brks.append(node)
cont_info = []
cont_ok = True
for c in conts:
    p = parent[c]
    test = ast.unparse(p.test) if isinstance(p, ast.If) else None
    good = isinstance(p, ast.If) and isinstance(p.test, ast.Compare) and len(p.test.ops) == 1 and \
        isinstance(p.test.ops[0], ast.Gt) and ast.unparse(p.test.comparators[0]) == "La"
    cont_ok = cont_ok and good
    cont_info.append({"line": c.lineno, "guard": test})
record("B2_every_continue_guarded_by_certain_gt_La", cont_ok and len(conts) == 2, cont_info)
brk_info = []
brk_ok = True
for b in brks:
    p = parent[b]
    body = p.body if isinstance(p, ast.If) else []
    tg = [ast.unparse(s.targets[0]) for s in body if isinstance(s, ast.Assign)]
    good = isinstance(p, ast.If) and ("aborted" in tg or "refuted" in tg)
    brk_ok = brk_ok and good
    brk_info.append({"line": b.lineno, "guard": ast.unparse(p.test) if isinstance(p, ast.If) else None,
                     "assigns_before_break": tg})
record("B3_every_break_sets_aborted_or_refuted", brk_ok and len(brks) == 3, brk_info)
last = loop.body[-1]
split_ok = isinstance(last, ast.If) and \
    sum(1 for s in last.body if "stack.append" in ast.unparse(s)) == 2 and \
    sum(1 for s in last.orelse if "stack.append" in ast.unparse(s)) == 2
halves = [ast.unparse(s) for s in last.body + last.orelse if "stack.append" in ast.unparse(s)]
record("B4_fallthrough_pushes_both_halves", split_ok, halves)
record("B4_halves_are_[lo,mid]_and_[mid,hi]", halves == [
    "stack.append((wl, wm, ul, uh, dep + 1))", "stack.append((wm, wh, ul, uh, dep + 1))",
    "stack.append((wl, wh, ul, um, dep + 1))", "stack.append((wl, wh, um, uh, dep + 1))"], halves)
mvf_if = [n for n in ast.walk(loop) if isinstance(n, ast.If) and ast.unparse(n.test) == "ul > 0 and uh < 2"]
record("B2_mean_value_form_only_when_0<u_lo_and_u_hi<2", len(mvf_if) == 1)
exits = [ast.unparse(n) for n in ast.walk(tree) if isinstance(n, ast.Call) and ast.unparse(n.func) == "sys.exit"]
record("B5_exit_code_iff_outcome_eq_EXPECT", exits == ["sys.exit(0 if outcome == EXPECT else 1)"], exits)
out_lines = {k: lines[k - 1] for k in (29, 57, 68, 80, 113, 114, 118, 126, 129, 130, 135, 143, 146, 149, 152, 153,
                                        156, 158, 159, 162, 163, 165, 166, 167, 183)}

# ---------------- C. library semantics (EXPLORATORY demonstrations on the installed python-flint)
ns = {"arb": arb}
fn = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in ("F_ball", "grad_ball", "iv")]
exec(compile(ast.Module(body=fn, type_ignores=[]), SRC, "exec"), ns)
F_ball, grad_ball, iv = ns["F_ball"], ns["grad_ball"], ns["iv"]
La = arb(fmpq(20090156350055, 10 ** 14))
ovl = arb(fmpq(1)).union(arb(fmpq(3)))
nan = arb("nan")
sem = {"overlap_gt": ovl > 2, "overlap_lt": ovl < 2, "nan_gt": nan > 0, "nan_lt": nan < 0,
       "nan_minus_gt": (nan - 1) > 0, "nan_abs_upper_times_gt": (arb(1) - nan.abs_upper() * arb(1)) > 0}
try:
    infball = arb(1) / arb(fmpq(0)).union(arb(fmpq(1)))
    sem["div_by_ball_with_0_is_finite"] = infball.is_finite()
    sem["div_by_ball_with_0_gt"] = infball > 0
    sem["minus_its_abs_upper_gt"] = (arb(1) - infball.abs_upper()) > 0
except ZeroDivisionError as exc:
    sem["div_by_ball_with_0"] = "ZeroDivisionError: " + str(exc)
record("C1_undecided_and_nan_comparisons_are_False",
       not any(v for k, v in sem.items() if k.endswith("_gt") or k.endswith("_lt")), sem)
x = arb(fmpq(-1, 8)).union(arb(fmpq(3, 8)))
nn = x.nonnegative_part()
record("C2_nonnegative_part_contains_[0,3/8]_and_is_nonneg", nn.contains(arb(0)) and nn.contains(arb(fmpq(3, 8)))
       and not (nn < 0) and nn.lower() >= 0, nn.str(10))
dy = [(fmpq(0), fmpq(2)), (fmpq(1, 2 ** 50), fmpq(2, 2 ** 50)), (fmpq(7, 4), fmpq(2)),
      (fmpq(1, 4), fmpq(4)), (fmpq(1112324551, 2 ** 30), fmpq(1112324552, 2 ** 30))]
iv_ok = all(iv(a, b).contains(arb(a)) and iv(a, b).contains(arb(b)) and iv(a, b).contains(arb((a + b) / 2))
            for a, b in dy)
iv_pos = iv(fmpq(1, 2 ** 50), fmpq(2, 2 ** 50)).lower() > 0
record("C3_dyadic_box_balls_contain_endpoints_and_stay_positive", iv_ok and iv_pos)
Wb, Ub = iv(fmpq(1, 4), fmpq(4)), iv(fmpq(0), fmpq(2))
Fb = F_ball(Wb, Ub)
record("C4_F_ball_on_full_middle_domain_finite_and_not_certified", Fb.is_finite() and not (Fb > La), Fb.str(8))
box = (fmpq(33, 32), fmpq(17, 16), fmpq(11, 16), fmpq(3, 4))
Fbox = F_ball(iv(box[0], box[1]), iv(box[2], box[3]))
incl = True
for i in range(9):
    for j in range(9):
        wv = box[0] + (box[1] - box[0]) * i / 8
        uv = box[2] + (box[3] - box[2]) * j / 8
        incl = incl and Fbox.contains(F_ball(arb(wv), arb(uv)))
record("C5_inclusion_point_values_in_box_enclosure_81pts", incl, Fbox.str(12))
gw, gu = grad_ball(iv(fmpq(1), fmpq(9, 8)), iv(fmpq(0), fmpq(1, 8)))
Fc = F_ball(arb(fmpq(17, 16)), arb(fmpq(1, 16)))
try:
    err = gw.abs_upper() * arb(fmpq(1, 16)) + gu.abs_upper() * arb(fmpq(1, 16))
    mvf_cert = (Fc - err) > La
    err_s = err.str(5)
except (ZeroDivisionError, ValueError) as exc:
    mvf_cert = False
    err_s = "exception: " + str(exc)
record("C6_gradient_ball_touching_u=0_not_finite_and_MVF_cannot_certify",
       (not gu.is_finite() or not gw.is_finite()) and not mvf_cert,
       {"grad_u": gu.str(5), "grad_w": gw.str(5), "err": err_s})

# ---------------- D. run evidence
main = json.load(open(os.path.join(RED, "runs", "ctl-f-main-v1", "ctl_f.json")))
bnb, res_, tails = main["bnb"], main["result"], main["tails"]
leaves = bnb["certified_by_natural_extension"] + bnb["certified_by_centered_form"]
record("D1_main_outcome_certify", res_["outcome"] == "certify" and res_["certified_v_cos_ge_L"] is True, res_)
record("D1_main_not_aborted_no_refutation_empty_stack",
       bnb["aborted_box_limit_or_depth"] is False and bnb["refutation"] is None and bnb["remaining_stack"] == 0,
       {k: bnb[k] for k in ("aborted_box_limit_or_depth", "refutation", "remaining_stack")})
record("D1_main_tails_ok", tails["both_tails_exceed_L"] is True and tails["rho_bar_ok"] is True and
       tails["Delta3_gt_2765/10000_Sturm"] is True, tails)
record("D1_binary_tree_identity_processed=2*leaves-1", bnb["boxes_processed"] == 2 * leaves - 1,
       {"processed": bnb["boxes_processed"], "certified_leaves": leaves})
rec = {}
for run in ("ctl-f-main-v1", "ctl-f-gradsym-v1", "ctl-f-mut-L-above-v1", "ctl-f-mut-tail-v1"):
    pre = json.load(open(os.path.join(RED, "receipts", run + "-pre.json")))
    post = json.load(open(os.path.join(RED, "receipts", run + "-post.json")))
    outs = {os.path.basename(k): v["sha256"] for k, v in post["outputs_sha256"].items()}
    now = {b: sha(os.path.join(RED, "runs", run, b)) for b in outs}
    rec[run] = {"pre_code_sha_ctl_f": pre["code_sha256"].get("reductions/code/ctl_f_d1bnb_v1.py"),
                "exit_code": post["exit_code"], "argv": pre["argv"],
                "post_pins_pre": post["pre_receipt_sha256"] == sha(os.path.join(RED, "receipts", run + "-pre.json")),
                "outputs_unchanged": outs == now, "outputs_sha256": outs}
record("D2_receipts_pin_source_exit0_outputs_unchanged",
       all(v["pre_code_sha_ctl_f"] == PIN and v["exit_code"] == 0 and v["post_pins_pre"] and v["outputs_unchanged"]
           for v in rec.values()), rec)
gs = json.load(open(os.path.join(RED, "runs", "ctl-f-gradsym-v1", "ctl_f_gradsym.json")))
record("D3_gradsym_verified_pinned_source_all_pass", gs["verified_source_sha256"] == PIN and gs["all_pass"] is True
       and gs["residuals_final"] == {"d_w": "0", "d_u": "0", "d_F": "0"}, gs["residuals_final"])
muts = {r: json.load(open(os.path.join(RED, "runs", r, "ctl_f.json")))["result"]["outcome"]
        for r in ("ctl-f-mut-L-above-v1", "ctl-f-mut-tail-v1")}
record("D4_existing_mutations_report_reject", all(v == "reject" for v in muts.values()), muts)

res = {"script": "audit_bnb_v1.py", "audited_source": "reductions/code/ctl_f_d1bnb_v1.py", "pinned_sha256": PIN,
       "evidence_lines": out_lines, "library_semantics": {k: str(v) for k, v in sem.items()},
       "checks": checks, "all_pass": all(v["pass"] for v in checks.values())}
with lane_guard.xopen(os.path.join(RUN, "audit_bnb.json")) as fh:
    json.dump(res, fh, indent=1, default=str)
print(json.dumps({"all_pass": res["all_pass"], "n_checks": len(checks),
                  "failed": [k for k, v in checks.items() if not v["pass"]]}))
sys.exit(0 if res["all_pass"] else 1)
