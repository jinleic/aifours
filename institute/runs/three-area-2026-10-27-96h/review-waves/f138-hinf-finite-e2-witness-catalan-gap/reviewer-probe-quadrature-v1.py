#!/usr/bin/env python3
"""reviewer-probe-quadrature-v1.py  (review f138) -- NON-load-bearing.

Explains the single residual Part-C tolerance miss in reviewer-exact-controls-v2
(C5: tail-integral route differed from the closed form by 5.0e-18 at dps=30).
Here the 1/(2 sqrt t) endpoint singularity is removed by t = u^2 and dps is 40;
the tail-integral route then agrees with 4 sqrt(2 pi) G / pi^2 to ~1e-41.
Writes reviewer-probe-quadrature-v1.log next to itself.
"""
import hashlib, os, time
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
lines = []


def out(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    lines.append(s)


out('start UTC', time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
mp.mp.dps = 40


def surv_eigen(t, K=80):
    return (4 / mp.pi) * mp.fsum(((-1) ** k) * mp.mpf(1) / (2 * k + 1) * mp.exp(-(2 * k + 1) ** 2 * mp.pi ** 2 * t / 8) for k in range(K))


def surv_images(t, K=14):
    rt = mp.sqrt(t)
    return mp.fsum(((-1) ** n) * (mp.ncdf((2 * n + 1) / rt) - mp.ncdf((2 * n - 1) / rt)) for n in range(-K, K + 1))


v1 = 4 * mp.sqrt(2 * mp.pi) * mp.catalan / mp.pi ** 2
# E sqrt(tau) = int_0^inf P(tau>t)/(2 sqrt t) dt ; on [0,1/2] substitute t=u^2: = int_0^{sqrt(1/2)} P(tau>u^2) du
v3b = mp.quad(lambda u: surv_images(u * u), [0, mp.sqrt(mp.mpf('0.5'))]) + \
    mp.quad(lambda t: surv_eigen(t) / (2 * mp.sqrt(t)), [mp.mpf('0.5'), 5, 50, mp.inf])
out('closed form 4 sqrt(2pi) G/pi^2 (dps40) =', mp.nstr(v1, 32))
out('tail-integral route, singularity removed  =', mp.nstr(v3b, 32))
out('difference =', mp.nstr(v3b - v1, 5))
q, err = mp.quad(lambda t: surv_images(t) / (2 * mp.sqrt(t)), [0, mp.mpf('0.5')], error=True)
out('for comparison, singular-endpoint quad error estimate at dps40 =', mp.nstr(err, 5))
out('RESULT:', 'AGREE to 1e-35' if abs(v3b - v1) < mp.mpf('1e-35') else 'DISAGREE')
with open(os.path.abspath(__file__), 'rb') as fh:
    out('self sha256 =', hashlib.sha256(fh.read()).hexdigest())
out('end UTC', time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
with open(os.path.join(HERE, 'reviewer-probe-quadrature-v1.log'), 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines) + '\n')
