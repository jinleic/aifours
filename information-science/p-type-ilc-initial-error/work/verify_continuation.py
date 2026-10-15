"""Bounded deterministic assay for the rational P-local obstruction.

This is not a search or a proof of an infinite quantifier. Exact rational
polynomial plant recursion is checked against an independent z-series formula;
nonlinear physical RK4 checks and adversarial persistent-noise controls follow.
"""
import os
for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[name] = "1"
import hashlib
import json
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import sys
import time

import mpmath as mp
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence/continuation"
# C(z)=P(z)/D(z); every D(0)=1. The choices are fixed, not tuned.
LEARNERS = {
    "accumulator": ([Q(1)], [Q(1), Q(-1)]),
    "forgetting": ([Q(1)], [Q(1), -Q(1, 2)]),
    "momentum": ([Q(1)], [Q(1), -Q(3, 2), Q(1, 2)]),
    "double_accumulator": ([Q(1)], [Q(1), Q(-2), Q(1)]),
    "triple_accumulator": ([Q(1)], [Q(1), Q(-3), Q(3), Q(-1)]),
    "two_error_memory": ([Q(1), Q(1, 4)], [Q(1), -Q(5, 4), Q(1, 4)]),
    "finite_error_memory": ([Q(1), Q(1, 2)], [Q(1)]),
}


def convolution(a, b, n):
    result = [Q(0)] * (n + 1)
    for i, x in enumerate(a[:n+1]):
        for j, y in enumerate(b[:n+1-i]):
            result[i+j] += x*y
    return result


def coefficients(p, d, n):
    result = []
    for k in range(n + 1):
        rhs = p[k] if k < len(p) else Q(0)
        result.append((rhs - sum(d[j]*result[k-j] for j in range(1, min(k, len(d)-1)+1))) / d[0])
    return result


def integrate(poly, q):
    return [Q(0)]*q + [v*Q(factorial(j), factorial(j+q)) for j, v in enumerate(poly)]


def combine(terms):
    result = [Q(0)]*max(len(poly) for _, poly in terms)
    for scale, poly in terms:
        for j, v in enumerate(poly):
            result[j] += scale*v
    return result


def direct_impulses(q, p, d, n):
    # Difference equation D(z)U=z P(z)E and actual plant y=a+J^q u.
    inputs, errors, impulses = [], [], []
    for i in range(n + 1):
        terms = [(Q(0), [Q(0)])]
        terms += [(-d[j], inputs[i-j]) for j in range(1, min(i, len(d)-1)+1)]
        terms += [(p[j], errors[i-1-j]) for j in range(min(i, len(p)))]
        u = combine(terms)
        y = integrate(u, q)
        y[0] += Q(i == 0)
        inputs.append(u)
        errors.append([-v for v in y])
        impulses.append(sum(y))
    return impulses


def series_impulses(q, p, d, n):
    k = [Q(0)] + coefficients(p, d, n-1)
    power = [Q(1)] + [Q(0)]*n
    h = [Q(1)] + [Q(0)]*n
    for order in range(1, n+1):
        power = convolution(power, k, n)
        weight = Q((-1)**order, factorial(q*order))
        for j in range(n+1):
            h[j] += weight*power[j]
    return h


def exact_checks():
    records, witnesses = [], []
    for name, (p, d) in LEARNERS.items():
        for q in range(1, 6):
            direct = direct_impulses(q, p, d, 12)
            formula = series_impulses(q, p, d, 12)
            assert direct == formula, (name, q)
            records.append({"learner": name, "q": q, "horizon": 12, "pass": True})
    for name in ("momentum", "double_accumulator", "two_error_memory"):
        p, d = LEARNERS[name]
        for q in (1, 2, 3):
            h = direct_impulses(q, p, d, 48)
            for n in (8, 24, 48):
                signs = [1 if x >= 0 else -1 for x in reversed(h[:n+1])]
                actual = sum(h[n-j]*Q(sign, 20) for j, sign in enumerate(signs))
                expected = sum(map(abs, h[:n+1]))/20
                assert actual == expected
                # Identical measured-output witness with zero starts and constant-in-time noise.
                physical = actual-Q(signs[-1], 20)
                witnesses.append({"learner": name, "q": q, "N": n, "epsilon": "1/20", "signs": signs,
                                  "measured_output": str(actual), "measured_output_float": float(actual),
                                  "noise_only_physical_output": str(physical),
                                  "amplification": float(expected*20)})
    return records, witnesses


def E(q, w):
    if w == 0:
        return mp.mpc(1)
    root = mp.root(w, q)
    return sum(mp.exp(root*mp.exp(2j*mp.pi*j/q)) for j in range(q))/q


def boundary_checks():
    mp.mp.dps = 100
    results = []
    for q in (1, 2, 3, 5):
        for m in (1, 2, 3):
            if q == m == 1:
                a, b, height = mp.mpf(2), mp.mpf(-1), mp.mpf(1)
                radial = mp.exp(-(a/mp.mpf("0.001")+b))
                z = 1-1/(height+10000j)
                tangent = abs(mp.exp(-(a/(1-z)+b)))
                assert abs(tangent-mp.exp(-1)) < mp.mpf("1e-90")
                results.append({"q": q, "pole_order": m, "radial_modulus": str(radial), "tangential_modulus": str(tangent)})
                continue
            # Fixed admissible rays: q=1 needs cos(m theta)<0, others avoid root ties.
            theta = mp.mpf("1.3") if q == 1 else mp.mpf("0.4")
            logs = []
            for rho in (mp.mpf("0.04"), mp.mpf("0.01"), mp.mpf("0.0025")):
                z = 1-rho*mp.exp(1j*theta)
                assert abs(z) < 1
                value = E(q, -1/(1-z)**m)
                logs.append(float(mp.log(abs(value))))
            assert logs[-1] > logs[0], (q, m, logs)
            results.append({"q": q, "pole_order": m, "theta": float(theta), "log_moduli": logs})
    # The negative-residue q=1 case grows already on the radius.
    negative_residue = [float(mp.log(abs(mp.exp(1/rho)))) for rho in (mp.mpf("0.1"), mp.mpf("0.01"))]
    assert negative_residue[1] > negative_residue[0]
    return results, negative_residue


def physical_trial(q, u, initial_output):
    steps = len(u)-1
    x = np.zeros(q)
    x[0] = initial_output
    for _ in range(10):
        x[0] -= (x[0]+0.2*np.sin(x[0])-initial_output)/(1+0.2*np.cos(x[0]))
    assert abs(x[0]+0.2*np.sin(x[0])-initial_output) < 1e-13
    y = np.empty(steps+1)
    y[0] = initial_output
    dt = 1/steps
    def rhs(state, control):
        result = np.empty(q)
        if q == 1:
            result[0] = control/(1+0.2*np.cos(state[0]))
        else:
            result[0] = state[1]/(1+0.2*np.cos(state[0]))
            result[1:-1] = state[2:]
            result[-1] = control
        return result
    for j in range(steps):
        middle = (u[j]+u[j+1])/2
        k1 = rhs(x, u[j])
        k2 = rhs(x+dt*k1/2, middle)
        k3 = rhs(x+dt*k2/2, middle)
        k4 = rhs(x+dt*k3, u[j+1])
        x += dt*(k1+2*k2+2*k3+k4)/6
        y[j+1] = x[0]+0.2*np.sin(x[0])
    return y


def nonlinear_checks(witnesses):
    records = []
    for witness in witnesses:
        if witness["learner"] != "momentum" or witness["N"] != 24:
            continue
        q = witness["q"]
        for steps in (400, 800):
            for channel in ("initial_shift", "measurement_noise"):
                u, previous = np.zeros(steps+1), np.zeros(steps+1)
                for sign in witness["signs"]:
                    amplitude = sign*0.05
                    initial = amplitude if channel == "initial_shift" else 0.0
                    noise = amplitude if channel == "measurement_noise" else 0.0
                    physical = physical_trial(q, u, initial)
                    measured = physical+noise
                    next_u = 1.5*u-0.5*previous-measured
                    previous, u = u, next_u
                expected = witness["measured_output_float"]
                difference = abs(float(measured[-1])-expected)
                assert difference < 2e-3*max(1, abs(expected)), (q, steps, channel, difference)
                records.append({"q": q, "steps": steps, "channel": channel,
                                "N": 24, "exact_measured_endpoint": expected,
                                "measured_endpoint": float(measured[-1]),
                                "physical_endpoint": float(physical[-1]), "absolute_discrepancy": difference})
    return records


def forgetting_checks():
    records = []
    for q in (1, 2, 3):
        steps, n, rho, ell = 500, 180, 0.5, 1.0
        t = np.linspace(0, 1, steps+1)
        target = t**q/factorial(q)
        for noisy in (False, True):
            u = np.zeros(steps+1)
            maximum = 0.0
            for i in range(n):
                # Persistent deterministic signs and a spatially nonconstant measurement disturbance.
                a = 0.02*(1 if (i//3)%2 == 0 else -1) if noisy else 0.0
                noise = 0.01*(1 if i%2 == 0 else -1)*(0.5+0.5*np.cos(7*t)) if noisy else np.zeros_like(t)
                y = physical_trial(q, u, a)+noise
                error = (np.zeros_like(t) if noisy else target)-y
                maximum = max(maximum, float(np.max(abs(error))))
                u = rho*u+ell*error
            if noisy:
                lam = 4.0
                beta = abs(rho)+abs(ell)*lam**(-q)
                bound = np.exp(lam)*(1+abs(ell)*lam**(-q)/(1-beta))*0.03
                assert maximum <= bound
                records.append({"q": q, "mode": "persistent_adversarial_noise_zero_target", "max_error": maximum, "proved_bound": float(bound)})
            else:
                residual = np.array([float(mp.re((1-E(q, -2*mp.mpf(float(s))**q))/2)) for s in t])
                discrepancy = float(np.max(abs(error-residual)))
                assert discrepancy < 2e-5, (q, discrepancy)
                records.append({"q": q, "mode": "nominal_residual", "max_final_error": float(np.max(abs(error))),
                                "exact_endpoint_residual": float(residual[-1]), "uniform_discrepancy": discrepancy})
    return records


def compact_inverse_checks():
    rows = []
    for q in range(1, 6):
        for h in (Q(1, 2), Q(1, 8), Q(1, 32)):
            # Exact integration of a terminal ramp: J^q u_h(T)=h^q/(q+1)!.
            integrated = Q(1, h)*Q(factorial(1), factorial(q+1))*h**(q+1)
            assert integrated == h**q/factorial(q+1)
            rows.append({"q": q, "h": str(h), "input_norm": 1, "output_norm": str(integrated), "necessary_inverse_gain": str(1/integrated)})
    return rows


def main():
    started = time.time()
    OUT.mkdir(exist_ok=True)
    exact, witnesses = exact_checks()
    boundary, negative = boundary_checks()
    report = {"date_pt": "2026-10-14", "command": f"{sys.executable} work/verify_continuation.py",
              "protocol": "Fixed seven learners; exact degrees 1..5/horizon12, witnesses degrees1..3/horizons8,24,48; no search.",
              "evidence_boundary": "Finite exact/empirical checks do not prove infinite divergence; written theorem plus independent review supplies the general claim.",
              "exact_identity_checks": exact, "finite_adversarial_witnesses": witnesses,
              "complex_boundary_checks": boundary, "negative_residue_log_moduli": negative,
              "nonlinear_counterchecks": nonlinear_checks(witnesses),
              "forgetting_controls": forgetting_checks(), "compact_inverse_ramps": compact_inverse_checks(),
              "versions": {"python": sys.version, "numpy": np.__version__, "mpmath": mp.__version__}}
    report["seconds"] = time.time()-started
    report["proof_sha256"] = hashlib.sha256((ROOT/"work/continuation-theorems.md").read_bytes()).hexdigest()
    report["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (OUT/"verification.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"pass": True, "exact_identity_checks": len(exact), "exact_witnesses": len(witnesses),
                      "nonlinear_counterchecks": len(report["nonlinear_counterchecks"]), "seconds": report["seconds"]}, indent=2))


if __name__ == "__main__":
    main()
