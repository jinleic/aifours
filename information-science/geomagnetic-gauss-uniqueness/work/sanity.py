"""Empirical checks only; the all-degree proofs do not depend on this program.

Reconstruct degree-1..5 internal/external coefficients on an ellipsoid from B:
line-integrate B to obtain the potential trace, then apply Green moment formulas.
Also evaluate the explicit patch-instability sequence, and exact finite Backus
recurrence cancellations with fractions.Fraction.
"""
import argparse
import datetime
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import sys
import time

for variable in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                 "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[variable] = "1"

import numpy as np
import scipy
from scipy.special import lpmv

AXES = np.array([1.1, 0.9, 1.0])
DEGREE = 5
SEED = 20261014
MODES = [(n, m, trig) for n in range(1, DEGREE + 1)
         for m in range(n + 1) for trig in (("cos", "sin") if m else ("cos",))]


def solid_harmonics(points):
    """Real orthonormal harmonics and Cartesian gradients, with no polar nodes."""
    radius = np.linalg.norm(points, axis=1)
    er = points / radius[:, None]
    mu = er[:, 2]
    sintheta = np.sqrt(1.0 - mu * mu)
    phi = np.arctan2(points[:, 1], points[:, 0])
    etheta = np.column_stack((mu * np.cos(phi), mu * np.sin(phi), -sintheta))
    ephi = np.column_stack((-np.sin(phi), np.cos(phi), np.zeros_like(phi)))
    regular, irregular, grad_regular, grad_irregular = [], [], [], []
    for n, m, trig in MODES:
        norm = math.sqrt((2*n+1)/(4*math.pi) * math.factorial(n-m)/math.factorial(n+m))
        if m:
            norm *= math.sqrt(2.0)
        legendre = lpmv(m, n, mu)
        previous = lpmv(m, n-1, mu) if m < n else np.zeros_like(mu)
        dtheta = -( (n+m)*previous - n*mu*legendre ) / sintheta
        if trig == "cos":
            angular = np.cos(m*phi)
            dphi = -m*np.sin(m*phi)
        else:
            angular = np.sin(m*phi)
            dphi = m*np.cos(m*phi)
        y = norm * legendre * angular
        gy = norm * (dtheta[:, None]*angular[:, None]*etheta
                     + (legendre*dphi/sintheta)[:, None]*ephi)
        regular.append(radius**n * y)
        irregular.append(radius**(-n-1) * y)
        grad_regular.append(radius[:, None]**(n-1) * (n*y[:, None]*er + gy))
        grad_irregular.append(radius[:, None]**(-n-2) * (-(n+1)*y[:, None]*er + gy))
    return (np.stack(regular, axis=1), np.stack(irregular, axis=1),
            np.stack(grad_regular, axis=1), np.stack(grad_irregular, axis=1))


def synthetic_field(points, internal, external):
    h, k, dh, dk = solid_harmonics(points)
    potential = k @ internal + h @ external
    field = -np.einsum("mjc,j->mc", dk, internal) - np.einsum("mjc,j->mc", dh, external)
    return potential, field


def parametrization(theta, phi):
    theta, phi = np.broadcast_arrays(theta, phi)
    omega = np.stack((np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi),
                      np.cos(theta)), axis=-1)
    dtheta = np.stack((np.cos(theta)*np.cos(phi), np.cos(theta)*np.sin(phi),
                       -np.sin(theta)), axis=-1)
    dphi = np.stack((-np.sin(theta)*np.sin(phi), np.sin(theta)*np.cos(phi),
                     np.zeros_like(theta)), axis=-1)
    return omega*AXES, dtheta*AXES, dphi*AXES


def recover_trace(theta, phi, path_order, field_only):
    """Use B only: base (theta=pi/2,phi=0), meridian then latitude paths."""
    nodes, weights = np.polynomial.legendre.leggauss(path_order)
    meridian_angle = math.pi/2 + (theta[:, None]-math.pi/2)*(nodes[None, :]+1)/2
    p, dtheta, _ = parametrization(meridian_angle, np.zeros_like(meridian_angle))
    b = field_only(p.reshape(-1, 3)).reshape(p.shape)
    meridian = np.sum(-np.sum(b*dtheta, axis=2)*weights[None, :], axis=1)
    meridian *= (theta-math.pi/2)/2
    phi_path = phi[:, None]*(nodes[None, :]+1)/2
    trace = np.empty((len(theta), len(phi)))
    for row, angle in enumerate(theta):
        p, _, dphi = parametrization(np.full_like(phi_path, angle), phi_path)
        b = field_only(p.reshape(-1, 3)).reshape(p.shape)
        latitude = np.sum(-np.sum(b*dphi, axis=2)*weights[None, :], axis=1)*phi/2
        trace[row] = meridian[row] + latitude
    return trace.reshape(-1)


def ellipsoid_run(nmu, nphi, path_order, internal, external):
    mu, wmu = np.polynomial.legendre.leggauss(nmu)
    theta = np.arccos(mu)
    phi = np.arange(nphi)*2*math.pi/nphi
    theta_grid, phi_grid = np.meshgrid(theta, phi, indexing="ij")
    points, _, _ = parametrization(theta_grid, phi_grid)
    points = points.reshape(-1, 3)
    omega = points / AXES
    normal_unnormalized = omega / AXES
    normal_length = np.linalg.norm(normal_unnormalized, axis=1)
    normal = normal_unnormalized / normal_length[:, None]
    weights = np.repeat(wmu, nphi) * (2*math.pi/nphi) * np.prod(AXES) * normal_length
    truth_potential, data = synthetic_field(points, internal, external)
    f = recover_trace(theta, phi, path_order,
                      lambda p: synthetic_field(p, internal, external)[1])
    f -= np.dot(weights, f)/np.sum(weights)
    truth_potential -= np.dot(weights, truth_potential)/np.sum(weights)
    g = -np.sum(data*normal, axis=1)
    h, k, dh, dk = solid_harmonics(points)
    dhn = np.einsum("mjc,mc->mj", dh, normal)
    dkn = np.einsum("mjc,mc->mj", dk, normal)
    divisors = np.array([2*n+1 for n, _, _ in MODES])
    recovered_i = np.sum(weights[:, None]*(f[:, None]*dhn-g[:, None]*h), axis=0)/divisors
    recovered_e = np.sum(weights[:, None]*(g[:, None]*k-f[:, None]*dkn), axis=0)/divisors
    recovered = np.concatenate((recovered_i, recovered_e))
    truth = np.concatenate((internal, external))
    return {
        "label": "Empirical evidence", "quadrature": [nmu, nphi], "path_order": path_order,
        "vector_observations": len(points), "unknown_coefficients": len(truth),
        "trace_recovery_max_absolute_error_modulo_constant": float(np.max(np.abs(f-truth_potential))),
        "coefficient_max_absolute_error": float(np.max(np.abs(recovered-truth))),
        "coefficient_relative_l2_error": float(np.linalg.norm(recovered-truth)/np.linalg.norm(truth)),
        "internal_relative_l2_error": float(np.linalg.norm(recovered_i-internal)/np.linalg.norm(internal)),
        "external_relative_l2_error": float(np.linalg.norm(recovered_e-external)/np.linalg.norm(external)),
        "minimum_radial_normal_dot": float(np.min(np.sum(normal*points/np.linalg.norm(points, axis=1)[:, None], axis=1))),
        "recovered_internal": recovered_i.tolist(), "recovered_external": recovered_e.tolist(),
    }


def patch_run():
    # Area quadrature for the cap z in [-1,-1/4]. No data outside it enter the norm.
    nodes, w = np.polynomial.legendre.leggauss(80)
    z = -1 + (nodes+1)*0.375
    w *= 0.375
    phi = np.arange(160)*2*math.pi/160
    zz, pp = np.meshgrid(z, phi, indexing="ij")
    rr = np.sqrt(1-zz*zz)
    points = np.stack((rr*np.cos(pp), rr*np.sin(pp), zz), axis=-1).reshape(-1, 3)
    weights = np.repeat(w, len(phi))*2*math.pi/len(phi)
    a = np.array([1j, 0j, 1+0j])
    complex_w = points[:, 2] + 1j*points[:, 0]
    t = (1+complex_w)/2
    dt = a[None, :]/2 - complex_w[:, None]*points
    q = math.sqrt(3/8)
    rows = []
    for degree in (2, 4, 8, 16, 32, 64, 128):
        gradient = -points*(np.real(t**degree)-2.0**(-degree))[:, None]/degree
        gradient += np.real(t[:, None]**(degree-1)*dt)
        intensity = np.linalg.norm(gradient, axis=1)
        rows.append({
            "degree": degree,
            "patch_sample_max": float(np.max(intensity)),
            "patch_l2_quadrature": float(math.sqrt(np.dot(weights, intensity**2))),
            "rigorous_formula_upper_bound_evaluated_in_float":
                (q**degree+2.0**(-degree))/degree + (1+1/math.sqrt(2))*q**(degree-1),
            "whole_sphere_north_value": 0.5+(1-2.0**(-degree))/degree,
        })
    return {"label": "Empirical evidence", "patch": "z <= -1/4", "quadrature": [80, 160],
            "sequence": "proof.md Eq.13", "rows": rows}


def exact_recurrence_check():
    coefficient = Fraction(1)
    rows = []
    for ell in range(1, 64, 2):
        next_coefficient = -Fraction((ell+2)*ell*(2*ell+5), 3*(ell+3)**2*(2*ell+1))*coefficient
        up = Fraction((ell+2)*ell, 2*ell+1)
        down_next = Fraction(3*(ell+3)**2, 2*ell+5)
        residual = up*coefficient + down_next*next_coefficient
        rows.append({"l": ell, "a_l": str(coefficient), "residual": str(residual)})
        coefficient = next_coefficient
    return {"label": "COMPUTED+VERIFIED finite rational identities only",
            "arithmetic": "fractions.Fraction", "zero_residual_count": sum(r["residual"] == "0" for r in rows),
            "count": len(rows), "rows": rows}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    start = time.monotonic()
    rng = np.random.default_rng(SEED)
    degrees = np.array([n for n, _, _ in MODES])
    internal = rng.normal(size=len(MODES))/(degrees+1)**2
    external = 0.25*rng.normal(size=len(MODES))/(degrees+1)**2
    result = {
        "scope": "Empirical sanity, not proof of any uniqueness statement",
        "seed": SEED, "maximum_degree": DEGREE, "ellipsoid_semiaxes": AXES.tolist(),
        "modes": MODES, "true_internal": internal.tolist(), "true_external": external.tolist(),
        "ellipsoid": [ellipsoid_run(*grid, internal, external) for grid in ((32, 64, 40), (48, 96, 64))],
        "patch_instability": patch_run(), "exact_backus_recurrence": exact_recurrence_check(),
    }
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    script = Path(__file__).resolve()
    receipt = {
        "command": [sys.executable, *sys.argv], "cwd": str(Path.cwd()),
        "completed_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "elapsed_seconds": time.monotonic()-start, "exit_code": 0,
        "python": sys.version, "platform": platform.platform(),
        "numpy": np.__version__, "scipy": scipy.__version__,
        "threads": {k: os.environ[k] for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")},
        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "requirements_sha256": hashlib.sha256(script.with_name("requirements.txt").read_bytes()).hexdigest(),
        "output": str(args.output.resolve()), "output_sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
    }
    args.receipt.write_text(json.dumps(receipt, indent=2)+"\n")
    summary = {
        "ellipsoid": [{k: v for k, v in r.items() if not k.startswith("recovered_")} for r in result["ellipsoid"]],
        "patch": result["patch_instability"]["rows"],
        "exact_zero_residuals": result["exact_backus_recurrence"]["zero_residual_count"],
        "elapsed_seconds": receipt["elapsed_seconds"],
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
