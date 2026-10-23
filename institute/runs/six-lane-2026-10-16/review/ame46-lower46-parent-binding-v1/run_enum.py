#!/usr/bin/env python3
"""run_enum.py -- item 5 driver: runs the parent-written enumerator enum_nsets (independent exhaustive search for all
N-sets satisfying the N-only predicate) on the 14 profiles of the five computer cases, plus enumerator controls:
  final      : the 14 profiles in JSON coordinate order (the outputs compared by binding_check.py);
  orderings  : every distinct coordinate ordering of each profile, mapped back -> must equal the final set;
  reversed   : every coordinate's parts in reversed value order, mapped back -> must equal the final set;
  ablations  : one interior pruning rule disabled at a time (node budget) -> if complete, must equal the final set,
               otherwise recorded as UNKNOWN;
  bruteforce : (2,2)^4 (t = 32 normal form, 16 points) for e = 0..8: all subsets of size 8 + e tested with
               binding_check.failures() -> must equal the enumerator output;
  no_orth    : C4 dropped in three profiles where it matters: final sets must be a subset and every extra set must
               fail failures() with exactly ["orth"] (natural intended-reason negatives for the predicate).
Native limits per enumerator process: RLIMIT_CPU soft limit and RLIMIT_FSIZE (no kill/timeout); peak RSS from
/usr/bin/time -l. Writes enum-runs.json (mode "x"); enumerator outputs are created exclusively by enum_nsets.
"""
import sys

sys.dont_write_bytecode = True

import itertools  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import platform  # noqa: E402
import re  # noqa: E402
import resource  # noqa: E402
import subprocess  # noqa: E402

import binding_check as bc  # noqa: E402

HERE = bc.HERE
BIN = HERE / "enum_nsets"
CPU_LIMIT_S = 1800
FSIZE_LIMIT_BYTES = 256 * 2 ** 20
ABLATION_NODE_BUDGET = 200_000_000
CONTROL_NODE_BUDGET = 2_000_000_000
ABLATION_FLAGS = ("--no-orth-prune", "--no-close-prune", "--no-dist-prune")
NO_ORTH_CASES = [(28, 0, ((3, 3, 2),) * 4), (29, 2, ((3, 2, 2),) * 4), (30, 2, ((3, 3), (2, 2, 2), (2, 2, 2), (2, 2, 2)))]


def native_limits():
    _, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (CPU_LIMIT_S, hard))
    resource.setrlimit(resource.RLIMIT_FSIZE, (FSIZE_LIMIT_BYTES, FSIZE_LIMIT_BYTES))


def run_enum(parts, e, out_rel, flags=()):
    out = HERE / out_rel
    pstr = ["-".join(map(str, p)) for p in parts]
    cmd = ["/usr/bin/time", "-l", str(BIN)] + pstr + [str(e), str(out)] + list(flags)
    r = subprocess.run(cmd, capture_output=True, text=True, preexec_fn=native_limits)
    if r.returncode != 0:
        raise RuntimeError("enum_nsets failed (%d): %s" % (r.returncode, r.stderr[-500:]))
    stats = json.loads(r.stdout.strip().splitlines()[-1])
    m = re.search(r"(\d+)\s+maximum resident set size", r.stderr)
    stats["peak_rss_bytes"] = int(m.group(1)) if m else None
    stats["output"] = out_rel
    stats["output_sha256"] = bc.sha256_file(out)
    stats["cmd"] = ["enum_nsets"] + pstr + [str(e), out_rel] + list(flags)
    return stats


def read_sets(rel):
    sets = []
    with open(HERE / rel) as fh:
        for line in fh:
            sets.append(frozenset(bc.parse_point(s) for s in line.split()))
    if len(set(sets)) != len(sets):
        raise RuntimeError("duplicate solution lines in " + rel)
    return set(sets)


def tag_of(t, e, prof):
    return "t%d_e%d_" % (t, e) + "_".join("-".join(map(str, p)) for p in prof)


def main():
    started = bc.now()
    res = {"started": started, "python": platform.python_version(), "binary_sha256": bc.sha256_file(BIN),
           "source_sha256": bc.sha256_file(HERE / "enum_nsets.c"),
           "limits": {"rlimit_cpu_soft_s": CPU_LIMIT_S, "rlimit_fsize_bytes": FSIZE_LIMIT_BYTES,
                      "ablation_node_budget": ABLATION_NODE_BUDGET},
           "final": {}, "orderings": [], "reversed": [], "ablations": [], "bruteforce": [], "no_orth": []}
    fails = []
    profiles = []
    for t, e in bc.CASES:
        report = json.loads((bc.SNAP / "evidence" / ("large_t_gen_t%d_e%d.json" % (t, e))).read_text())
        for entry in report["profiles"]:
            profiles.append((t, e, tuple(tuple(p) for p in entry["profile"]),
                             sum(r["orbit_size"] for r in entry["reps"])))
    finals = {}
    for t, e, prof, expected in profiles:
        tag = tag_of(t, e, prof)
        st = run_enum(prof, e, "enum/final/%s.txt" % tag)
        st["expected_sum_of_orbit_sizes"] = expected
        res["final"][tag] = st
        if not st["complete"] or st["leaf_cheap_reject_full_accept"]:
            fails.append("final_run_unclean:" + tag)
        if st["solutions"] != expected:
            fails.append("final_count_differs_from_orbit_sum:" + tag)
        finals[tag] = read_sets(st["output"])
    for t, e, prof, _ in profiles:
        tag = tag_of(t, e, prof)
        ref = finals[tag]
        seen = {prof}
        for sigma in itertools.permutations(range(4)):
            order = tuple(prof[s] for s in sigma)
            if order in seen:
                continue
            seen.add(order)
            st = run_enum(order, e, "enum/orderings/%s__ord%s.txt" % (tag, "".join(map(str, sigma))),
                          ("--max-nodes=%d" % CONTROL_NODE_BUDGET,))
            mapped = set()
            for S in read_sets(st["output"]):
                img = set()
                for y in S:
                    x = [0] * 4
                    for kk in range(4):
                        x[sigma[kk]] = y[kk]
                    img.add(tuple(x))
                mapped.add(frozenset(img))
            st["sigma"] = list(sigma)
            st["equal_to_final_after_mapping"] = mapped == ref
            res["orderings"].append(st)
            if not st["complete"] or st["leaf_cheap_reject_full_accept"] or mapped != ref:
                fails.append("ordering_mismatch:%s:%s" % (tag, sigma))
        rev = tuple(tuple(reversed(p)) for p in prof)
        st = run_enum(rev, e, "enum/reversed/%s__rev.txt" % tag, ("--max-nodes=%d" % CONTROL_NODE_BUDGET,))
        lo = [6 - len(p) for p in prof]
        mapped = {frozenset(tuple(2 * lo[i] + len(prof[i]) - 1 - y[i] for i in range(4)) for y in S)
                  for S in read_sets(st["output"])}
        st["equal_to_final_after_mapping"] = mapped == ref
        res["reversed"].append(st)
        if not st["complete"] or st["leaf_cheap_reject_full_accept"] or mapped != ref:
            fails.append("reversed_mismatch:" + tag)
        for flag in ABLATION_FLAGS:
            st = run_enum(prof, e, "enum/ablations/%s__%s.txt" % (tag, flag.strip("-")),
                          (flag, "--max-nodes=%d" % ABLATION_NODE_BUDGET))
            if st["complete"]:
                st["equal_to_final"] = read_sets(st["output"]) == ref
                if not st["equal_to_final"] or st["leaf_cheap_reject_full_accept"]:
                    fails.append("ablation_mismatch:%s:%s" % (tag, flag))
            else:
                st["equal_to_final"] = "UNKNOWN (node budget reached)"
            res["ablations"].append(st)
    pts16 = list(itertools.product((4, 5), repeat=4))
    prof32 = ((2, 2),) * 4
    V, d = bc.normal_form(prof32)
    for e in range(9):
        brute = {frozenset(c) for c in itertools.combinations(pts16, 8 + e) if not bc.failures(c, V, d, e)}
        st = run_enum(prof32, e, "enum/bruteforce/t32_2-2x4_e%d.txt" % e)
        got = read_sets(st["output"])
        st["bruteforce_count"] = len(brute)
        st["subsets_tested"] = math.comb(16, 8 + e)
        st["equal_to_bruteforce"] = got == brute
        res["bruteforce"].append(st)
        if got != brute or not st["complete"]:
            fails.append("bruteforce_mismatch:e%d" % e)
    for t, e, prof in NO_ORTH_CASES:
        tag = tag_of(t, e, prof)
        st = run_enum(prof, e, "enum/no_orth/%s__no-orth.txt" % tag,
                      ("--no-orth", "--max-nodes=%d" % CONTROL_NODE_BUDGET))
        got = read_sets(st["output"])
        V, d = bc.normal_form(prof)
        extra = got - finals[tag]
        reasons = {}
        for S in extra:
            key = ",".join(bc.failures(S, V, d, e))
            reasons[key] = reasons.get(key, 0) + 1
        st["final_subset"] = finals[tag] <= got
        st["extra_sets"] = len(extra)
        st["extra_failure_reasons"] = reasons
        st["pass"] = st["complete"] and st["final_subset"] and len(extra) > 0 and set(reasons) == {"orth"}
        res["no_orth"].append(st)
        if not st["pass"]:
            fails.append("no_orth_control_failed:" + tag)
    res["fails"] = fails
    res["verdict"] = "FAIL" if fails else "PASS"
    res["ended"] = bc.now()
    with open(HERE / "enum-runs.json", "x") as fh:
        json.dump(res, fh, indent=1)
        fh.write("\n")
    print(json.dumps({"verdict": res["verdict"], "fails": fails, "final": {k: v["solutions"] for k, v in
                                                                          res["final"].items()}}))


if __name__ == "__main__":
    main()
