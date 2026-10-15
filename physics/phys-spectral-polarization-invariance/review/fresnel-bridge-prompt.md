# Hostile referee: physical counterexample to the all-probe/Fresnel bridge

Read-only, no delegation, no file writes, no network necessary. Read only files inside `/Users/jinleic/jinleic-workspace/ai4s/phys-spectral-polarization-invariance/`. You may read `code/fresnel_only.py`, `results/fresnel-only.json`, and the C2 theorem in `RESULTS.md` for context. Do not run the script (it writes output). Standalone write-free calculations are allowed. The current local date is 2026-10-14.

This is an independent new, narrowly scoped proof audit; another referee is auditing C1-C5. Do not duplicate that audit. We need to establish an exact obstruction to treating C2's necessary all-scalar-probe condition as necessary for physical Fresnel propagation. The mechanism is standard azimuthal-order degeneracy, not claimed new. Full primary 2022 structured-polarization source paper, if needed for context only: Martínez-Herrero et al., Optics & Laser Technology 152, 108079, DOI 10.1016/j.optlastec.2022.108079; https://oa.upm.es/87042/1/9906481.pdf, Eq. 33 retains the angular matrix under Fresnel propagation.

## Proposed exact statement and full argument

On the two-dimensional source plane, define four square-integrable orthonormal scalar modes, with r²=x²+y²:

`psi_0,+ = (x+iy) exp(-r²/2)/sqrt(pi)`;
`psi_0,- = (x-iy) exp(-r²/2)/sqrt(pi)`;
`psi_1,+ = (x+iy)(2-r²) exp(-r²/2)/sqrt(2*pi)`;
`psi_1,- = (x-iy)(2-r²) exp(-r²/2)/sqrt(2*pi)`.

Orthogonality of +/- azimuthal orders follows from the angular integral; that of radial indices 0/1 follows from `integral_0^infinity t exp(-t) (2-t) dt=0`; their stated normalizations use integrals 1 and 2. Set weights w0=1, w1=1/2. Define a statistically stationary source at each fixed frequency by four independent zero-mean complex random coefficients and covariance

`W_xx(r1,r2) = (3/4) sum_l w_l psi_l,+(r1) psi_l,+*(r2)`;
`W_yy(r1,r2) = (1/4) sum_l w_l psi_l,-(r1) psi_l,-*(r2)`;
`W_xy = W_yx = 0`.

This is a finite-energy PSD matrix kernel by construction. In scalar-mode basis `(0+,0-,1+,1-)`, its trace response T is diagonal `(3/4,1/4,3/8,1/8)`, so rank T is four. Its full spatial-polarization covariance is diagonal with four positive entries and remaining entries zero. It is NOT factorized `g C`: equal-radius source-pair correlations in W_xx and W_yy have opposite phases `exp(+-i(theta1-theta2))`, so they are not proportional as kernels. Alternatively, C2 would forbid a nonreplacement invariant map of trace support rank four under every probe.

Let U_z be the common scalar paraxial free-space Fresnel propagator in the full transverse plane, at any fixed k>0 and every z>=0. In polar variables, the Laplacian on `h(r) exp(im theta)` has radial part `h''+h'/r-m²h/r²`. Thus the propagated radial envelopes are identical for m=+1 and m=-1. Equivalently, the angular Fresnel integral is `2*pi*(-i)^m J_m(k Rr/z) exp(im Theta)`; the identities `J_-1=-J_1` and `(-i)^-1 J_-1=(-i) J_1` give the same radial transfer. Therefore

`|U_z psi_l,+(r)|² = |U_z psi_l,-(r)|²`

for every r,z. If `H(r,z)=sum_l w_l |U_z psi_l,+(r)|²`, the local output matrix is exactly `H diag(3/4,1/4)`. At all illuminated points its degree is P=1/2, identical to the source, even its normalized polarization matrix is invariant. At dark points, notably the axis, P is undefined and excluded.

However, the scalar mode-selective functional `L(E)=integral psi_0,+*(r) E(r) dr` yields `diag(3/4,0)` because the four scalar modes are orthonormal. Its degree is P=1. This is an allowed scalar probe of C2, though not free-space point evaluation. Hence transfer of C2's universal-probe necessity to Fresnel-only invariance is FALSE, not merely unproved. The full restricted Fresnel-only classification is still unresolved by this example. This does NOT contradict Wolf's sufficient conditions.

A rotationally symmetric scalar ABCD kernel preserves the same +/-m degeneracy, but an astigmatic lens need not; no claim is made for all ABCD systems. The script numerically compares 2D FFT propagation to independent 1D Hankel-Fresnel quadrature at fixed points, and includes an astigmatic lens negative control. All these comparisons are empirical; the analytic symmetry and orthogonality carry the universal quantifiers.

## Requested report

Return correct / correct-with-fixes / incorrect, then numbered findings with severity, precise issue, checkable correction, and whether the proposed source is a valid counterexample. Check covariance positivity, conjugation conventions, rank T, normalization, kernel factorization, full-plane Fresnel symmetry, zero intensity, and exact projector response. Also check that the numeric implementation actually represents the stated source and independent integral. Do not claim novelty. State the strongest defensible summary in one sentence.
