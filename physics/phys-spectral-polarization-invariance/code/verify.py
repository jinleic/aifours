#!/usr/bin/env python3
"""Replay exact identities and independent propagation controls for RESULTS.md.

Exact identities use SymPy. Floating-point comparisons are empirical controls,
not continuum error bounds or proofs. No network or mutable external inputs.
"""
from __future__ import annotations

import json
import os
import platform
from pathlib import Path

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")

import numpy as np
import scipy
import scipy.integrate
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SEED = 20261014


def degree(j: np.ndarray) -> np.ndarray:
    """Bloch norm avoids artificial clipping of a determinant cancellation."""
    tr = np.trace(j, axis1=-2, axis2=-1).real
    if np.any(tr <= 0):
        raise ValueError("Polarization is undefined at nonpositive intensity")
    s = np.stack(
        (2 * j[..., 0, 1].real, -2 * j[..., 0, 1].imag,
         (j[..., 0, 0] - j[..., 1, 1]).real), axis=-1,
    )
    return np.linalg.norm(s, axis=-1) / tr


def choi(p: float, transpose: bool = False) -> np.ndarray:
    if transpose:
        part = np.zeros((4, 4), complex)
        for a in range(2):
            for b in range(2):
                part[2 * a + b, 2 * b + a] = 1
    else:
        omega = np.array([1, 0, 0, 1], complex)
        part = np.outer(omega, omega.conj())
    return (1 - p) * np.eye(4) / 2 + p * part


def apply_choi(gamma: np.ndarray, f: np.ndarray) -> np.ndarray:
    n = gamma.shape[0] // 2
    return np.einsum("...a,...b,aibj->...ij", f, f.conj(),
                     gamma.reshape(n, 2, n, 2))


def exact_controls() -> dict:
    p = sp.symbols("p", real=True)
    omega = sp.Matrix([1, 0, 0, 1])
    swap = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0],
                      [0, 1, 0, 0], [0, 0, 0, 1]])
    b = (1 - p) * sp.eye(4) / 2 + p * omega * omega.T
    c = (1 - p) * sp.eye(4) / 2 + p * swap
    expected_b = {(1 + 3 * p) / 2: 1, (1 - p) / 2: 3}
    expected_c = {(1 + p) / 2: 3, (1 - 3 * p) / 2: 1}
    eigenvalue = sp.symbols("eigenvalue")
    for matrix, expected in ((b, expected_b), (c, expected_c)):
        factored = sp.prod((eigenvalue - e)**m for e, m in expected.items())
        assert sp.expand(matrix.charpoly(eigenvalue).as_expr() - factored) == 0
    # A negative Choi eigenvalue is a physical-realizability negative control.
    assert min(c.subs(p, sp.Rational(1, 2)).eigenvals()) == -sp.Rational(1, 4)

    ar, ai, br, bi = sp.symbols("ar ai br bi", real=True)
    f = sp.Matrix([ar + sp.I * ai, br + sp.I * bi])
    norm2 = (f.conjugate().T * f)[0]
    for transpose in (False, True):
        rho = f * f.conjugate().T
        pure = rho.T if transpose else rho
        j = p * pure + (1 - p) * norm2 * sp.eye(2) / 2
        assert sp.expand(j.det() - (1 - p**2) * norm2**2 / 4) == 0
    u, v, zr, zi = sp.symbols("u v zr zi", real=True)
    rho = sp.Matrix([[u, zr + sp.I * zi], [zr - sp.I * zi, v]])
    mixed = p * rho + (1 - p) * sp.trace(rho) * sp.eye(2) / 2
    assert sp.expand(sp.trace(mixed)**2 - 4 * mixed.det()
                     - p**2 * (sp.trace(rho)**2 - 4 * rho.det())) == 0

    weights = [sp.Rational(1, 2), sp.Rational(4, 5)]
    normalized = [w / sum(weights) for w in weights]
    assert normalized == [sp.Rational(5, 13), sp.Rational(8, 13)]
    ratio = sp.exp(3 * sp.log(2) / 3)
    assert sp.simplify((ratio - 1) / (ratio + 1)) == sp.Rational(1, 3)
    # Mixture witness only: opposite outputs average to an unpolarized matrix.
    # The dimension >=3 pure-input exclusion is proved in RESULTS.md, not here.
    j0 = sp.diag(sp.Rational(3, 4), sp.Rational(1, 4))
    j1 = sp.diag(sp.Rational(1, 4), sp.Rational(3, 4))
    assert (j0 + j1) / 2 == sp.eye(2) / 2
    return {
        "status": "PASS",
        "B_choi_eigenvalues": {str(k): v for k, v in expected_b.items()},
        "C_choi_eigenvalues": {str(k): v for k, v in expected_c.items()},
        "transpose_p_half_negative_eigenvalue": "-1/4",
        "pure_input_determinant_identities": "zero for arbitrary complex input",
        "mixed_input_bloch_identity": "zero polynomial",
        "spectral_line_weights": [str(x) for x in normalized],
        "far_zone_polarization_counterexample": ["0", "1/3"],
        "opposite_output_mixture": "I_2/2; P=0",
    }


def channel_controls() -> dict:
    rng = np.random.default_rng(SEED)
    f = rng.normal(size=(513, 2)) + 1j * rng.normal(size=(513, 2))
    f /= np.linalg.norm(f, axis=1, keepdims=True)
    answer = {}
    for name, p, transpose in (("B", 0.5, False), ("C", 0.25, True)):
        gamma = choi(p, transpose)
        matrix = apply_choi(gamma, f)
        vectors = f.conj() if transpose else f
        formula = p * np.einsum("...i,...j->...ij", vectors, vectors.conj())
        formula += (1 - p) * np.eye(2)[None] / 2
        error = float(np.max(np.abs(matrix - formula)))
        degree_error = float(np.max(np.abs(degree(matrix) - p)))
        assert error < 2e-14 and degree_error < 2e-14
        answer[name] = {"choi_vs_closed_form_max_error": error,
                        "degree_max_error": degree_error,
                        "min_choi_eigenvalue": float(np.linalg.eigvalsh(gamma).min())}
    # Nontrivial trace whitening: Phi(X)=Psi(A X A*) with positive A.
    a = np.array([[2, 0.2j], [-0.2j, 1]], complex)
    intensity = np.einsum("...a,...a->...", (f @ a.T).conj(), f @ a.T).real
    j = apply_choi(choi(0.5), f @ a.T)
    assert np.max(np.abs(np.trace(j, axis1=1, axis2=2).real - intensity)) < 3e-14
    assert np.max(np.abs(degree(j) - 0.5)) < 2e-14
    answer["whitening_nonidentity_trace_matrix"] = "PASS"
    # Verify replacement for 4 spatial modes and arbitrary PSD response mixtures.
    q = np.array([[0.6, 0.2j], [-0.2j, 0.4]], complex)
    expected = float(degree(q))
    f4 = rng.normal(size=(37, 4)) + 1j * rng.normal(size=(37, 4))
    gamma4 = np.kron(np.eye(4), q)
    j4 = apply_choi(gamma4, f4)
    assert np.max(np.abs(degree(j4) - expected)) < 2e-14
    assert abs(float(degree(j4.mean(axis=0))) - expected) < 2e-14
    answer["four_mode_replacement_and_mixture"] = "PASS"
    # C5: matched achromatic probes, different polarization families/frequencies.
    spectral_j = [2 * apply_choi(choi(0.5), f),
                  3 * apply_choi(choi(0.25, True), f)]
    spectral_i = np.stack([np.trace(m, axis1=1, axis2=2).real
                           for m in spectral_j], axis=1)
    normalized = spectral_i / spectral_i.sum(axis=1, keepdims=True)
    spectral_error = float(np.max(np.abs(normalized - np.array([0.4, 0.6]))))
    assert spectral_error < 2e-14
    assert np.max(np.abs(degree(spectral_j[0]) - 0.5)) < 2e-14
    assert np.max(np.abs(degree(spectral_j[1]) - 0.25)) < 2e-14
    # Nonproportional trace matrices give different normalized spectra for e0,e1.
    bad_intensities = np.array([[1., 2.], [1., 1.]])
    bad_spectra = bad_intensities / bad_intensities.sum(axis=1, keepdims=True)
    assert np.max(np.abs(bad_spectra[0] - bad_spectra[1])) > 0.16
    answer["joint_achromatic_invariance"] = {
        "spectrum_max_error": spectral_error,
        "frequency_degrees": [0.5, 0.25],
        "nonproportional_trace_negative_control": bad_spectra.tolist(),
    }
    return answer


def fft_propagate(fields: np.ndarray, dx: float, z: float, k: float) -> np.ndarray:
    q = 2 * np.pi * np.fft.fftfreq(fields.shape[0], dx)
    multiplier = np.exp(-1j * z * q**2 / (2 * k))
    multiplier = multiplier.reshape((-1,) + (1,) * (fields.ndim - 1))
    return np.fft.ifft(np.fft.fft(fields, axis=0) * multiplier, axis=0)


def fresnel_kernel(xout: np.ndarray, x: np.ndarray, k: float, z: float,
                   lens_f: float | None = None) -> np.ndarray:
    dx = x[1] - x[0]
    kernel = np.sqrt(k / (2j * np.pi * z)) * np.exp(
        1j * k * (xout[:, None] - x[None, :])**2 / (2 * z)) * dx
    if lens_f is not None:
        kernel *= np.exp(-1j * k * x[None, :]**2 / (2 * lens_f))
    return kernel


def csd_from_modes(modes: np.ndarray, gamma: np.ndarray) -> np.ndarray:
    n = modes.shape[1]
    return np.einsum("xa,yb,aibj->ijxy", modes, modes.conj(),
                     gamma.reshape(n, 2, n, 2))


def propagate_csd(kernel: np.ndarray, w: np.ndarray) -> np.ndarray:
    # Source-CSD contraction, independent of Kraus/modal propagation below.
    result = np.empty((kernel.shape[0], 2, 2), complex)
    for i in range(2):
        for j in range(2):
            result[:, i, j] = np.sum((kernel @ w[i, j]) * kernel.conj(), axis=1)
    return result


def propagation_controls() -> dict:
    n, length, k = 512, 24.0, 7.0
    x = (np.arange(n) - n // 2) * length / n
    dx = length / n
    modes = np.stack((np.exp(-x**2 / 2), np.sqrt(2) * x * np.exp(-x**2 / 2)), axis=1)
    modes /= np.sqrt(np.sum(np.abs(modes)**2, axis=0) * dx)
    selected = np.where(np.abs(x) <= 3)[0][::4]
    answer = {"grid": {"n": n, "length": length, "k": k,
                       "sample_count": len(selected), "z": [1.5, 3.0, 6.0]}}
    for name, p, transpose in (("B", 0.5, False), ("C", 0.25, True)):
        gamma = choi(p, transpose)
        w = csd_from_modes(modes, gamma)
        eigval, eigvec = np.linalg.eigh(gamma)
        # Independent realization: coherent random Jones modes from the full covariance.
        amplitudes = (eigvec * np.sqrt(eigval)[None, :]).reshape(2, 2, 4)
        source_fields = np.einsum("xa,ail->xil", modes, amplitudes)
        records = []
        for z, lens_f in ((1.5, None), (3.0, None), (6.0, None), (3.0, 4.0)):
            fields = source_fields.copy()
            if lens_f is not None:
                fields *= np.exp(-1j * k * x**2 / (2 * lens_f))[:, None, None]
            propagated = fft_propagate(fields, dx, z, k)[selected]
            j_fft = np.einsum("xil,xjl->xij", propagated, propagated.conj())
            kernel = fresnel_kernel(x[selected], x, k, z, lens_f)
            j_csd = propagate_csd(kernel, w)
            error = float(np.max(np.abs(j_fft - j_csd)))
            intensity = np.trace(j_fft, axis1=1, axis2=2).real
            # Direct double-integral cancellation makes normalized ratios at
            # effectively dark samples ill-conditioned. Keep their matrix check.
            reliable = intensity > 1e-6 * intensity.max()
            perr = float(max(np.max(np.abs(degree(j_csd[reliable]) - p)),
                             np.max(np.abs(degree(j_fft[reliable]) - p))))
            assert error < 2e-10 and perr < 2e-9, (name, z, lens_f, error, perr)
            records.append({"z": z, "lens_f": lens_f,
                            "CSD_integral_vs_coherent_mode_FFT_max_error": error,
                            "degree_max_error": perr,
                            "degree_relative_intensity_floor": 1e-6,
                            "degree_sample_count": int(reliable.sum()),
                            "matrix_sample_count": len(selected)})
        answer[name] = records
    # Binary random scalar phase-screen response: average coherency, not degrees.
    z, p = 3.0, 0.5
    gamma = choi(p)
    f_plus = fft_propagate(modes * np.exp(0.8j * x)[:, None], dx, z, k)[selected]
    f_minus = fft_propagate(modes * np.exp(-0.8j * x)[:, None], dx, z, k)[selected]
    j_average = (apply_choi(gamma, f_plus) + apply_choi(gamma, f_minus)) / 2
    r = (np.einsum("xa,xb->xab", f_plus, f_plus.conj())
         + np.einsum("xa,xb->xab", f_minus, f_minus.conj())) / 2
    predicted = p * degree(r)
    residual = float(np.max(np.abs(degree(j_average) - predicted)))
    assert residual < 2e-14
    assert degree(j_average).min() < p - 0.05
    answer["binary_random_phase_screen"] = {
        "tilt_radians_per_unit": [-0.8, 0.8],
        "mixture_formula_max_error": residual,
        "ensemble_degree_range": [float(degree(j_average).min()), float(degree(j_average).max())],
        "each_deterministic_degree": p,
        "not_a_Kolmogorov_atmosphere_simulation": True,
    }
    return answer


def gaussian_schell_controls() -> dict:
    n, length, k, z, sigma = 256, 20.0, 5.0, 2.0, 1.2
    x = (np.arange(n) - n // 2) * length / n
    dx = length / n
    selected = np.where(np.abs(x) <= 3)[0][::4]
    kernel = fresnel_kernel(x[selected], x, k, z)
    q = np.array([[0.65, 0.12 + 0.09j], [0.12 - 0.09j, 0.35]])
    delta = 0.8
    spatial = np.exp(-(x[:, None]**2 + x[None, :]**2) / (4 * sigma**2)
                     - (x[:, None] - x[None, :])**2 / (2 * delta**2))
    w = q[:, :, None, None] * spatial[None, None]
    j = propagate_csd(kernel, w)
    # Independent closed form from Gaussian Wigner shear / Gaussian integration.
    width2 = sigma**2 + (z / k)**2 * (1 / (4 * sigma**2) + 1 / delta**2)
    analytic = sigma / np.sqrt(width2) * np.exp(-x[selected]**2 / (2 * width2))
    error = float(np.max(np.abs(j - analytic[:, None, None] * q[None])))
    perr = float(np.max(np.abs(degree(j) - degree(q))))
    assert error < 2e-11 and perr < 2e-12
    # Unequal correlation widths: source degree zero, propagated degree nonzero.
    intensities, quadratures = [], []
    for d in (0.5, 1.3):
        spatial_d = np.exp(-(x[:, None]**2 + x[None, :]**2) / (4 * sigma**2)
                           - (x[:, None] - x[None, :])**2 / (2 * d**2))
        numerical = np.sum((kernel @ spatial_d) * kernel.conj(), axis=1).real
        v = sigma**2 + (z / k)**2 * (1 / (4 * sigma**2) + 1 / d**2)
        intensities.append(sigma / np.sqrt(v) * np.exp(-x[selected]**2 / (2 * v)))
        quadratures.append(numerical)
    predicted_p = np.abs(intensities[0] - intensities[1]) / (intensities[0] + intensities[1])
    numeric_p = np.abs(quadratures[0] - quadratures[1]) / (quadratures[0] + quadratures[1])
    assert np.max(np.abs(predicted_p - numeric_p)) < 2e-11
    assert numeric_p.max() > 0.05
    return {"grid": {"n": n, "length": length, "k": k, "z": z, "sigma": sigma},
            "factorized_delta": delta,
            "factorized_integral_vs_analytic_max_error": error,
            "factorized_degree_max_error": perr,
            "negative_control_deltas": [0.5, 1.3],
            "negative_control_initial_degree": 0,
            "negative_control_propagated_degree_max": float(numeric_p.max()),
            "negative_control_vs_analytic_max_error": float(np.max(np.abs(predicted_p - numeric_p)))}


def spectrum_controls() -> dict:
    # Fresnel on-axis 2D response from two separable 1D FFT propagations.
    n, length, z, waist = 1024, 48.0, 1.0, 1.0
    x = (np.arange(n) - n // 2) * length / n
    dx = length / n
    source = np.exp(-x**2 / (2 * waist**2))
    measured = []
    for k in (1.0, 2.0):
        amplitude_1d = fft_propagate(source, dx, z, k)[n // 2]
        measured.append(float(abs(amplitude_1d)**4))
    expected = np.array([0.5, 0.8])
    assert np.max(np.abs(np.array(measured) - expected)) < 2e-12
    # Direct continuous Fourier quadrature, separate from closed-form Gaussian FT.
    records = []
    ss = [0.0, np.sqrt(np.log(2) / 3), 0.9]
    for k in (1.0, 1.7, 2.0):
        intensities = []
        for s in ss:
            pol = []
            for width in (1.0, 2.0):
                fx, errx = scipy.integrate.quad(
                    lambda t: np.exp(-k**2 * t*t / (2 * width**2)) * np.cos(k * s * t),
                    -np.inf, np.inf, epsabs=2e-11, epsrel=2e-11)
                fy, erry = scipy.integrate.quad(
                    lambda t: np.exp(-k**2 * t*t / (2 * width**2)),
                    -np.inf, np.inf, epsabs=2e-11, epsrel=2e-11)
                # Divide out common (2pi)^2; keep k^2 Fraunhofer prefactor.
                pol.append(float(k**2 * abs(k / width**2 * fx * fy)**2 / (2*np.pi)**2))
            intensities.append(pol)
        intensities = np.array(intensities)
        expected_far = np.exp(-np.array(ss)[:, None]**2 * np.array([1., 4.])[None, :])
        residual = float(np.max(np.abs(intensities - expected_far)))
        assert residual < 2e-10
        records.append({"k": k, "normalized_far_intensities": intensities.tolist(),
                        "quadrature_vs_analytic_max_error": residual})
    return {"on_axis_2d_fft_intensities": measured,
            "on_axis_normalized_spectrum": (np.array(measured)/sum(measured)).tolist(),
            "far_zone_s_samples": ss, "scaled_gaussian_quadratures": records,
            "quadrature_error_estimates_not_rigorous_bounds": True}


def main() -> None:
    result = {
        "status": "PASS", "seed": SEED,
        "versions": {"python": platform.python_version(), "numpy": np.__version__,
                     "scipy": scipy.__version__, "sympy": sp.__version__},
        "effective_thread_environment": {k: os.environ.get(k) for k in
                                         ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS")},
        "exact": exact_controls(),
        "channels": channel_controls(),
        "non_schell_propagation": propagation_controls(),
        "gaussian_schell": gaussian_schell_controls(),
        "spectra": spectrum_controls(),
        "scope": "Symbolic identities certified; numerical propagation is empirical, not a universal proof.",
    }
    (ROOT / "results" / "verification.json").write_text(json.dumps(result, indent=2) + "\n")
    print("PASS: exact Choi/determinant/mixing/spectral identities")
    print("PASS: deterministic all-probe family controls and nonidentity trace whitening")
    print("PASS: non-Schell Fresnel/ABCD CSD integrals vs independent coherent-mode FFT")
    print("PASS: random scalar-screen mixture formula and depolarization negative control")
    print("PASS: Gaussian Schell-model analytic integrals and unequal-width negative control")
    print("PASS: spectral nonimplications, rational witness and independent Fourier quadrature")
    print("WROTE results/verification.json")


if __name__ == "__main__":
    main()
