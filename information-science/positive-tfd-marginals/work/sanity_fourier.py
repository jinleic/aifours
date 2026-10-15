#!/usr/bin/env python3
"""Floating-point sanity checks from an independent representation.

Not a certificate. It rebuilds the signal from normalized Hermite functions
(scipy), transforms it numerically, and compares with the closed forms used by
verify_fourier_obstruction.py.
"""
import argparse
import json
import math
from pathlib import Path
import numpy as np
from scipy.special import eval_hermite

A4 = math.sqrt(6) / 7


def hermite_function(n, x):
    return (np.pi ** -0.25 * np.exp(-x * x / 2) * eval_hermite(n, x)
            / math.sqrt(2.0 ** n * math.factorial(n)))


def signal(x):
    return hermite_function(0, x) + 1j * A4 * hermite_function(4, x)


def unitary_ft(values, x, omega):
    """S(w)=(2pi)^(-1/2) int s(t)e^{-iwt}dt by direct trapezoid sums."""
    dx = x[1] - x[0]
    return np.array([np.sum(values * np.exp(-1j * w * x)) * dx for w in omega]) / math.sqrt(2 * math.pi)


def closed_rho(t):
    p = 4 * t**4 - 12 * t**2 + 3
    return (196 + p * p) * np.exp(-t * t) / (220 * math.sqrt(math.pi))


def closed_if(t):
    p = 4 * t**4 - 12 * t**2 + 3
    return 14 * (16 * t**3 - 24 * t) / (196 + p * p)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    x = np.linspace(-30, 30, 120001)
    s = signal(x)
    energy = np.sum(abs(s) ** 2) * (x[1] - x[0])
    omega = np.linspace(-6, 6, 241)
    spectrum = unitary_ft(s, x, omega)
    derivative_spectrum = unitary_ft(-1j * x * s, x, omega)  # dS/dw
    s_at = signal(omega)
    h = 1e-5
    ds = (signal(omega + h) - signal(omega - h)) / (2 * h)
    if_numeric = np.imag(np.conj(s_at) * ds) / abs(s_at) ** 2
    gd_numeric = -np.imag(np.conj(spectrum) * derivative_spectrum) / abs(spectrum) ** 2
    result = {
        'status': 'FLOAT_SANITY_ONLY',
        'energy_numeric': float(energy), 'energy_exact': 55 / 49,
        'max_abs_S_minus_s_on_[-6,6]': float(np.max(abs(spectrum - s_at))),
        'max_abs_rho_numeric_minus_closed': float(np.max(abs(abs(s_at) ** 2 / energy - closed_rho(omega)))),
        'max_abs_IF_numeric_minus_closed': float(np.max(abs(if_numeric - closed_if(omega)))),
        'max_abs_GD_numeric_plus_closed_IF': float(np.max(abs(gd_numeric + closed_if(omega)))),
        'sup_abs_IF_on_fine_grid': float(np.max(abs(closed_if(np.linspace(0, 6, 600001))))),
    }
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
