"""Reproducible bounded-CPU exact spot-checks of the quintic/sextic SPR claims.

Numerical generation/optimization proposes boxes and numerators.  Rational
Routh and Sturm checks alone accept cases.  All proposals, rejected attempts,
and diagnostic failures are retained under evidence/spotcheck.  Sampling is
not a proof, and no Lean build or proof audit is performed here.
"""
from __future__ import annotations

# Set these before importing numpy/scipy; HiGHS also gets its own threads=1.
import os
for _key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "HIGHS_THREADS"):
    os.environ[_key] = "1"

import argparse
from datetime import datetime
from fractions import Fraction
from functools import partial
import hashlib
import json
import math
from pathlib import Path
import platform
import resource
import sys
import time
from zoneinfo import ZoneInfo

import mpmath
import numpy as np
import scipy
from scipy.optimize import linprog
import sympy as sp

import sprlib
from exact_verify import (T, box_stable_exact, endpoints_exact, is_hurwitz_exact,
                          pairing_polys, to_fraction_box, verify_numerator)
from sextic_construction import construct_sextic

# scipy explicitly forwards unrecognized options to HiGHS; its one warning is
# retained in the execution log.  This changes no file or numerical algorithm.
sprlib.linprog = partial(linprog, options={"threads": 1})
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "evidence" / "spotcheck"


def serializable(value):
    if isinstance(value, dict):
        return {str(k): serializable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, np.ndarray)):
        return [serializable(x) for x in value]
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, np.generic):
        return value.item()
    return value


def save_json(path, value):
    with path.open("x", encoding="utf-8") as stream:
        json.dump(serializable(value), stream, indent=2, allow_nan=False)
        stream.write("\n")


def sample_center(rng, n, mode, adversarial=False):
    """Known stable factors, covering real, oscillatory, clustered, and wide roots."""
    poly = np.array([1.0])
    factors = []
    if mode == 0 and not adversarial:
        for _ in range(n):
            pole = float(np.exp(rng.uniform(-1.5, 1.5)))
            factors.append([pole, 1.0])
    else:
        for j in range(n // 2):
            if adversarial:
                frequency = (0.2, 1.0, 5.0)[j]
                damping = float(10**rng.uniform(-4.0, -2.0))
            elif mode == 2:
                frequency = float(np.exp(rng.uniform(-0.08, 0.08)))
                damping = float(np.exp(rng.uniform(-3.5, -0.5)))
            elif mode == 3:
                frequency = float(np.exp(rng.uniform(-2.3, 2.3)))
                damping = float(np.exp(rng.uniform(-3.5, 0.7)))
            else:
                frequency = float(np.exp(rng.uniform(-1.3, 1.3)))
                damping = float(np.exp(rng.uniform(-2.5, 0.5)))
            factors.append([frequency**2, 2*damping*frequency, 1.0])
        if n % 2:
            factors.append([float(np.exp(rng.uniform(-1.0, 1.0))), 1.0])
    for factor in factors:
        poly = np.polynomial.polynomial.polymul(poly, factor)
    poly, _, frequency_scale = sprlib.normalize_frequency(poly, poly)
    poly[-1] = 1.0
    return poly, {"factors_before_normalizing": factors,
                  "center_frequency_scale": float(frequency_scale)}


def generate_box(rng, n, group, index):
    mode = index % 4
    center, metadata = sample_center(rng, n, mode, group == "adversarial")
    wlo = abs(center) * np.exp(rng.uniform(-3.0, 1.0, n + 1))
    whi = abs(center) * np.exp(rng.uniform(-3.0, 1.0, n + 1))
    wlo[-1] = whi[-1] = 0
    pattern = "all coefficients variable"
    if group == "degenerate":
        if index < 8:
            wlo[::2] = whi[::2] = 0
            pattern = "fixed even part"
        elif index < 12:
            wlo[1::2] = whi[1::2] = 0
            pattern = "fixed odd part"
        elif index < 18:
            keep = (index - 12) % n
            for k in range(n):
                if k != keep:
                    wlo[k] = whi[k] = 0
            pattern = f"only coefficient {keep} varies"
        elif index < 20:
            wlo[:] = whi[:] = 0
            pattern = "singleton"
        else:
            mask = rng.random(n) < 0.6
            mask[0] = True
            for k in range(n):
                if mask[k]:
                    wlo[k] = whi[k] = 0
            pattern = "random fixed-coordinate mask"
    epsilon = float(np.exp(rng.uniform(math.log(1e-4), math.log(0.3))))
    if np.any(wlo) or np.any(whi):
        radius = float(sprlib.stability_radius(center, wlo, whi, iters=60))
        if not math.isfinite(radius) or radius <= 0:
            raise ArithmeticError("Invalid numerical stability radius for known stable center")
        lo_float, hi_float = sprlib.scaled_box(center, wlo, whi, (1-epsilon)*radius)
    else:
        radius = None
        lo_float, hi_float = center.copy(), center.copy()
    rejected_roundings = []
    for max_den in (10**6, 10**9, 10**12, 10**18):
        lo, hi = to_fraction_box(lo_float, hi_float, max_den=max_den)
        if box_stable_exact(lo, hi):
            break
        rejected_roundings.append({"max_den": max_den, "lo": lo, "hi": hi,
                                   "box_stable_exact": False})
    else:
        raise ArithmeticError("Rationalized box not exactly stable even at denominator 10^18")
    # Verify the reused numerical convention against the independent exact one.
    for numerical, exact in zip(sprlib.endpoints(list(map(float, lo)), list(map(float, hi))),
                                endpoints_exact(lo, hi)):
        if not np.array_equal(numerical, np.array(list(map(float, exact)))):
            raise AssertionError("sprlib endpoint convention mismatch")
    metadata.update(group=group, index=index, mode=mode, pattern=pattern,
                    center=center, width_lower=wlo, width_upper=whi,
                    epsilon=epsilon, stability_radius=radius,
                    float_lo=lo_float, float_hi=hi_float, rational_max_den=max_den,
                    rejected_box_roundings=rejected_roundings,
                    degenerate_indices=[k for k in range(n) if lo[k] == hi[k]])
    return lo, hi, metadata


def _negative_pocket_points(lo, hi, beta):
    """Exact root isolation proposes extra numerical LP rows, not acceptance."""
    extra, witnesses = [], []
    for ci, p in enumerate(pairing_polys(lo, hi, beta)):
        roots = p.diff().intervals(eps=sp.Rational(1, 10**24))
        for (left, right), multiplicity in roots:
            if right <= 0:
                continue
            point = max(sp.Rational(0), (left + right)/2)
            value = p.eval(point)
            extra.append(float(point))
            if value <= 0:
                witnesses.append({"corner": ci, "t": str(point), "pairing": str(value),
                                  "critical_root_interval": [str(left), str(right)],
                                  "multiplicity": multiplicity})
    return extra, witnesses


def find_lp_numerator(lo, hi):
    original_lo, original_hi = np.array(list(map(float, lo))), np.array(list(map(float, hi)))
    normalized_lo, normalized_hi, w0 = sprlib.normalize_frequency(original_lo, original_hi)
    attempts, extra, last_beta = [], [], None
    n = len(lo) - 1
    for attempt in range(4):
        # The last two retries vary the frequency normalization, not the box.
        scale = float(w0 if attempt < 2 else (1.0 if attempt == 2 else w0*0.5))
        frequency_factors = scale ** (np.arange(n + 1) - n)
        scaled_lo, scaled_hi = original_lo*frequency_factors, original_hi*frequency_factors
        if attempt == 0:
            grid = None
        else:
            grid = np.unique(np.concatenate(([0.0], np.logspace(-12, 12, 1601*attempt),
                                              np.array(extra) / scale**2,
                                              sprlib.special_points(scaled_lo, scaled_hi))))
        started = time.monotonic()
        tau_grid, tau_numeric, numeric_beta, info = sprlib.synthesis_margin(
            scaled_lo, scaled_hi, max_iter=40 if attempt == 0 else 80,
            tol=1e-10 if attempt == 0 else 1e-12, grid0=grid)
        entry = {"attempt": attempt, "frequency_scale": scale,
                 "tau_grid": tau_grid, "tau_numeric": tau_numeric,
                 "exchange_history": info.get("hist"), "seconds": time.monotonic()-started,
                 "error": info.get("error"), "roundings": []}
        attempts.append(entry)
        if numeric_beta is None:
            continue
        original_beta = numeric_beta / frequency_factors
        original_beta[-1] = 1.0
        entry["numeric_beta_original_coordinates"] = original_beta
        for max_den in (10**6, 10**12, 10**18):
            beta = [Fraction(str(x)).limit_denominator(max_den) for x in original_beta]
            beta[-1] = Fraction(1)
            certificate = verify_numerator(lo, hi, beta)
            entry["roundings"].append({"max_den": max_den, "beta": beta,
                                        "certificate": certificate})
            last_beta = beta
            if certificate["ok"]:
                classification = "first LP and rounding certified" if attempt == 0 and max_den == 10**6 else (
                    "coarse numerator rounding recovered" if attempt == 0 else
                    "numerical LP/grid candidate recovered by exact-guided refinement")
                return {"ok": True, "beta": beta, "verification": certificate,
                        "attempts": attempts, "classification": classification}
        points, witnesses = _negative_pocket_points(lo, hi, last_beta)
        extra.extend(points)
        entry["exact_nonpositive_witnesses"] = witnesses
    return {"ok": False, "beta": last_beta, "attempts": attempts,
            "classification": "unresolved numerical search; not an infeasibility certificate"}


def independent_hurwitz_crosscheck(seed):
    """Compare Routh with exact Hurwitz determinants on 100 seeded polynomials."""
    rng = np.random.default_rng(seed)
    for j in range(100):
        n = 2 + j % 5
        c = [Fraction(int(x), 3) for x in rng.integers(-4, 25, n)] + [Fraction(1)]
        if j % 3 == 0:
            c = [Fraction(math.comb(n, k)) for k in range(n+1)]
        desc = c[::-1]
        matrix = sp.Matrix(n, n, lambda r, col:
            sp.Rational(desc[2*col-r+1]) if 0 <= 2*col-r+1 <= n else 0)
        determinants = all(matrix[:k, :k].det(method="domain-ge") > 0 for k in range(1, n+1))
        if is_hurwitz_exact(c) != determinants:
            raise AssertionError(f"Routh/Hurwitz disagreement: {c}")
    return {"count": 100, "all_agree": True}


def run(args):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(args.seed)
    start = time.monotonic()
    summary = {"seed": args.seed, "started_pt": datetime.now(ZoneInfo("America/Los_Angeles")).isoformat(),
               "versions": {"python": platform.python_version(), "numpy": np.__version__,
                            "scipy": scipy.__version__, "sympy": sp.__version__, "mpmath": mpmath.__version__},
               "command": [sys.executable, *sys.argv],
               "resource_settings": {"blas_threads": 1, "highs_threads": 1, "sequential": True},
               "source_sha256": {name: hashlib.sha256((ROOT/"work"/name).read_bytes()).hexdigest()
                                  for name in ("exact_verify.py", "sextic_construction.py", "spotcheck.py", "sprlib.py")},
               "independent_hurwitz_crosscheck": independent_hurwitz_crosscheck(args.seed + 1),
               "degrees": {}, "formula_discrepancies": [], "failure_files": [],
               "scope": "Exact certificates for rational boxes; randomized spot-checks, not a theorem or Lean audit."}
    for n in args.degrees:
        nstart = time.monotonic()
        counts = {"requested_random": args.random_count, "requested_degenerate": args.degenerate_count if n == 6 else 0,
                  "requested_adversarial": args.adversarial_count,
                  "total": 0, "stable_exact": 0, "verified_numerators": 0,
                  "failed_numerators": 0, "formula_audits_pass": 0, "formula_audits_fail": 0,
                  "fixed_even_cases": 0, "box_rounding_recoveries": 0,
                  "numerator_rounding_recoveries": 0, "lp_refinement_recoveries": 0,
                  "construction_failures": 0, "groups": {}, "epsilon_min": 1.0, "epsilon_max": 0.0}
        case_path = OUTPUT / f"{args.prefix}-n{n}-cases.jsonl"
        with case_path.open("x", encoding="utf-8") as stream:
            groups = [("random", args.random_count), ("adversarial", args.adversarial_count)]
            if n == 6:
                groups.append(("degenerate", args.degenerate_count))
            for group, count in groups:
                counts["groups"][group] = {"total": 0, "pass": 0, "fail": 0}
                for index in range(count):
                    case_start = time.monotonic()
                    lo, hi, metadata = generate_box(rng, n, group, index)
                    case_id = f"n{n}-{group}-{index:03d}"
                    record = {"id": case_id, "lo": lo, "hi": hi, "sampling": metadata,
                              "box_stable_exact": True}
                    counts["total"] += 1
                    counts["stable_exact"] += 1
                    counts["epsilon_min"] = min(counts["epsilon_min"], metadata["epsilon"])
                    counts["epsilon_max"] = max(counts["epsilon_max"], metadata["epsilon"])
                    counts["groups"][group]["total"] += 1
                    if metadata["rejected_box_roundings"]:
                        counts["box_rounding_recoveries"] += 1
                    needs_failure_record = bool(metadata["rejected_box_roundings"])
                    if n == 6:
                        try:
                            construction = construct_sextic(lo, hi, dps=50)
                        except ArithmeticError as exc:
                            construction = {"error": str(exc), "audit_ok": False,
                                            "verification": {"ok": False}}
                        record["construction"] = construction
                        ok = construction["verification"]["ok"]
                        if construction.get("method") == "Lemma 2.3 fixed even part":
                            counts["fixed_even_cases"] += 1
                        if construction["audit_ok"]:
                            counts["formula_audits_pass"] += 1
                        else:
                            counts["formula_audits_fail"] += 1
                            needs_failure_record = True
                            summary["formula_discrepancies"].append(case_id)
                        roundings = construction.get("details", {}).get("rounding_attempts", [])
                        if len(roundings) > 1:
                            counts["numerator_rounding_recoveries"] += int(ok)
                            needs_failure_record = True
                        if not ok or not construction["audit_ok"]:
                            needs_failure_record = True
                            counts["construction_failures"] += int(not ok)
                            record["reexamination_100dps"] = construct_sextic(lo, hi, dps=100)
                            if record["reexamination_100dps"]["verification"]["ok"] and not ok:
                                record["classification"] = "working-precision construction recovered at 100 digits"
                                ok = True
                            record["independent_lp"] = find_lp_numerator(lo, hi)
                            if not ok and record["independent_lp"]["ok"]:
                                ok = True
                                record["classification"] = "construction failure but exact LP numerator exists"
                            elif not ok:
                                record["classification"] = "unresolved construction and LP; counterexample candidate only"
                    else:
                        synthesis = find_lp_numerator(lo, hi)
                        record["synthesis"] = synthesis
                        ok = synthesis["ok"]
                        if len(synthesis["attempts"]) > 1:
                            counts["lp_refinement_recoveries"] += int(ok)
                            needs_failure_record = True
                        if any(len(x["roundings"]) > 1 for x in synthesis["attempts"]):
                            counts["numerator_rounding_recoveries"] += int(ok)
                            needs_failure_record = True
                    record["ok"] = ok
                    record["seconds"] = time.monotonic()-case_start
                    counts["verified_numerators" if ok else "failed_numerators"] += 1
                    counts["groups"][group]["pass" if ok else "fail"] += 1
                    if needs_failure_record or not ok:
                        path = OUTPUT/f"{args.prefix}-{case_id}-investigation.json"
                        save_json(path, record)
                        summary["failure_files"].append(path.name)
                    stream.write(json.dumps(serializable(record), allow_nan=False) + "\n")
                    stream.flush()
                    if (counts["total"] % 25 == 0) or not ok:
                        print(json.dumps({"degree": n, "completed": counts["total"],
                                          "passed": counts["verified_numerators"],
                                          "failed": counts["failed_numerators"],
                                          "seconds": time.monotonic()-nstart}), flush=True)
        counts["seconds"] = time.monotonic()-nstart
        counts["cases_file"] = case_path.name
        summary["degrees"][str(n)] = counts
    summary["seconds"] = time.monotonic()-start
    usage = resource.getrusage(resource.RUSAGE_SELF)
    summary["peak_rss_bytes"] = usage.ru_maxrss if sys.platform == "darwin" else usage.ru_maxrss*1024
    summary["cpu_seconds"] = usage.ru_utime + usage.ru_stime
    summary["ok"] = all(row["failed_numerators"] == 0 and row["formula_audits_fail"] == 0
                        for row in summary["degrees"].values())
    summary_path = OUTPUT/f"{args.prefix}-summary.json"
    save_json(summary_path, summary)
    print(json.dumps(serializable(summary), indent=2, allow_nan=False), flush=True)
    return 0 if summary["ok"] else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--random-count", type=int, default=200)
    parser.add_argument("--degenerate-count", type=int, default=24)
    parser.add_argument("--adversarial-count", type=int, default=12)
    parser.add_argument("--seed", type=int, default=20261014)
    parser.add_argument("--prefix", default="spotcheck")
    parser.add_argument("--degrees", type=int, nargs="+", default=[6, 5], choices=[5, 6])
    arguments = parser.parse_args()
    if min(arguments.random_count, arguments.degenerate_count, arguments.adversarial_count) < 0:
        parser.error("counts must be nonnegative")
    if not arguments.prefix or "/" in arguments.prefix or "\\" in arguments.prefix:
        parser.error("prefix must be a nonempty filename component")
    raise SystemExit(run(arguments))
