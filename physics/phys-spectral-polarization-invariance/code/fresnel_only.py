#!/usr/bin/env python3
"""Known azimuthal-degeneracy mechanism: Fresnel invariance is not all-probe invariance."""
from __future__ import annotations

import json
import os
from pathlib import Path

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")

import numpy as np
from scipy.integrate import quad
from scipy.special import jv
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def polarization(jxx: np.ndarray, jyy: np.ndarray) -> np.ndarray:
    return np.abs(jxx - jyy) / (jxx + jyy)


def main() -> None:
    t = sp.symbols("t", positive=True)
    # Angular integral kills opposite azimuthal orders. Radial Gram for l=0,1.
    radial = [sp.Integer(1), (2 - t) / sp.sqrt(2)]
    gram = sp.Matrix([[sp.integrate(t * sp.exp(-t) * a * b, (t, 0, sp.oo))
                       for b in radial] for a in radial])
    assert gram == sp.eye(2)
    # Scalar modes ordered (0+,0-,1+,1-), each feeding only its named polarization.
    # Radial incoherent weights 1,1/2 and polarization powers 3/4,1/4.
    trace_matrix = sp.diag(sp.Rational(3, 4), sp.Rational(1, 4),
                           sp.Rational(3, 8), sp.Rational(1, 8))
    assert trace_matrix.rank() == 4 and all(v > 0 for v in trace_matrix.diagonal())
    gamma = sp.diag(sp.Rational(3, 4), 0, 0, sp.Rational(1, 4),
                    sp.Rational(3, 8), 0, 0, sp.Rational(1, 8))
    assert gamma.is_positive_semidefinite
    projected = gamma[:2, :2]
    projector_degree = sp.sqrt(1 - 4 * projected.det() / sp.trace(projected)**2)
    h = sp.symbols("h", positive=True)
    local = h * sp.diag(sp.Rational(3, 4), sp.Rational(1, 4))
    local_degree = sp.simplify(sp.sqrt(1 - 4 * local.det() / sp.trace(local)**2))
    assert projector_degree == 1 and local_degree == sp.Rational(1, 2)
    exact = {"orthonormal_radial_gram": str(gram), "trace_support_rank": 4,
             "trace_eigenvalues": [str(v) for v in trace_matrix.diagonal()],
             "free_space_degree": str(local_degree),
             "isolating_scalar_probe_degree": str(projector_degree),
             "projected_coherency_matrix": str(projected)}

    n, length, k = 256, 20.0, 7.0
    axis = (np.arange(n) - n // 2) * length / n
    xx, yy = np.meshgrid(axis, axis, indexing="ij")
    r2 = xx**2 + yy**2
    gaussian = np.exp(-r2 / 2)
    fields = np.stack([(xx + 1j*yy) * gaussian / np.sqrt(np.pi),
                       (xx - 1j*yy) * gaussian / np.sqrt(np.pi),
                       (xx + 1j*yy) * (2-r2) * gaussian / np.sqrt(2*np.pi),
                       (xx - 1j*yy) * (2-r2) * gaussian / np.sqrt(2*np.pi)],axis=-1)
    dx = length / n
    numerical_gram = np.einsum("xya,xyb->ab", fields.conj(), fields) * dx**2
    assert np.max(np.abs(numerical_gram - np.eye(4))) < 2e-13
    q = 2 * np.pi * np.fft.fftfreq(n, dx)
    q2 = q[:, None]**2 + q[None, :]**2
    source_fft = np.fft.fft2(fields, axes=(0, 1))
    sample_offsets = [(8, 0), (8, 6), (-12, 7), (0, 16), (19, -9)]
    samples = [(n//2+a, n//2+b) for a,b in sample_offsets]
    records = []
    for z in (1.5, 3.0, 6.0):
        propagated = np.fft.ifft2(source_fft * np.exp(-1j*z*q2/(2*k))[:, :, None], axes=(0, 1))
        plus = np.abs(propagated[..., 0])**2 + 0.5*np.abs(propagated[..., 2])**2
        minus = np.abs(propagated[..., 1])**2 + 0.5*np.abs(propagated[..., 3])**2
        intensity = 0.75*plus + 0.25*minus
        reliable = intensity > 1e-6*intensity.max()
        error_p = float(np.max(np.abs(polarization(0.75*plus[reliable],0.25*minus[reliable])-0.5)))
        assert error_p < 2e-11
        # Independent radial Hankel-Fresnel integral, not a 2D FFT encoding.
        max_error = 0.0
        for ix, iy in samples:
            radius = float(np.hypot(axis[ix],axis[iy]))
            theta = float(np.arctan2(axis[iy],axis[ix]))
            for ell in (0, 1):
                def integrand(r: float) -> complex:
                    envelope = r*np.exp(-r*r/2)/np.sqrt(np.pi)
                    if ell:
                        envelope *= (2-r*r)/np.sqrt(2)
                    return r*envelope*np.exp(1j*k*r*r/(2*z))*jv(1,k*radius*r/z)
                real, real_err = quad(lambda r: integrand(r).real, 0, 12,
                                      epsabs=2e-11, epsrel=2e-11,limit=300)
                imag, imag_err = quad(lambda r: integrand(r).imag, 0, 12,
                                      epsabs=2e-11, epsrel=2e-11,limit=300)
                radial_out = k/(1j*z)*(-1j)*np.exp(1j*k*radius**2/(2*z))*(real+1j*imag)
                for j, sign in ((2*ell, 1),(2*ell+1, -1)):
                    expected = radial_out*np.exp(1j*sign*theta)
                    max_error = max(max_error,float(abs(propagated[ix,iy,j]-expected)))
        assert max_error < 2e-9
        records.append({"z": z,"degree_max_error":error_p,
                        "FFT2_vs_Hankel_Fresnel_max_error":max_error,
                        "degree_relative_intensity_floor":1e-6,
                        "degree_sample_count":int(reliable.sum())})
    # A scalar astigmatic phase breaks the +/-m symmetry; not all ABCD systems preserve it.
    z = 3.0
    astigmatic = fields*np.exp(-1j*k*(xx**2/4.0+yy**2/7.0)/2)[:, :, None]
    perturbed = np.fft.ifft2(np.fft.fft2(astigmatic,axes=(0,1))
                           *np.exp(-1j*z*q2/(2*k))[:, :, None],axes=(0,1))
    plus = np.abs(perturbed[...,0])**2+0.5*np.abs(perturbed[...,2])**2
    minus = np.abs(perturbed[...,1])**2+0.5*np.abs(perturbed[...,3])**2
    intensity = 0.75*plus+0.25*minus
    reliable = intensity > 1e-6*intensity.max()
    observed = polarization(0.75*plus[reliable],0.25*minus[reliable])
    max_deviation = float(np.max(np.abs(observed-0.5)))
    assert max_deviation > 0.1
    result = {"status":"PASS","exact":exact,
              "grid":{"n":n,"length":length,"k":k,"sample_offsets":sample_offsets},
              "numerical_gram_error":float(np.max(np.abs(numerical_gram-np.eye(4)))),
              "Fresnel":records,
              "astigmatic_lens_negative_control":{"f_x":4.0,"f_y":7.0,"z":z,
                  "degree_range":[float(observed.min()),float(observed.max())],
                  "max_deviation_from_half":max_deviation},
              "evidence":"Exact orthogonality/rank identities; propagation comparisons are empirical.",
              "scope":"Refutes transfer of all-probe necessity to Fresnel-only invariance, not Wolf's sufficiency."}
    (ROOT/'results/fresnel-only.json').write_text(json.dumps(result,indent=2)+'\n')
    print("PASS: rank-four positive source, Fresnel P=1/2, scalar projector P=1")
    print("PASS: independent FFT2 versus Hankel-Fresnel integrals")
    print("PASS: astigmatic scalar lens breaks invariance (negative control)")
    print("WROTE results/fresnel-only.json")


if __name__ == '__main__':
    main()
