# RQLS10 v9 - the Weyl E+F+marginal core: prior-art alignment, exact compact form, and three written exclusions

Owner PhysicsRQLS10-2. Actual `/bin/date` observed immediately before this file: `Sun Oct 25 21:02:20 PDT 2026`.

**WRITTEN CANDIDATE**, additive successor to the pinned v7 (`8636f523...997d`) and v8 (`94ee295f...917d`) with v8-erratum E1 (`81efc30c...543d`). It is not reviewed, accepted, formal, executable or novelty-cleared. All arithmetic below is hand-written, including the decimal bounds in Theorem 3.2. No interpreter, eval, program, CAS, enumeration, solver, replay, CLI, nested agent or GO. V9/v10/v11/HOLD and the original cutoff/deadline are unchanged.

## 1. Prior-art alignment (correction of emphasis, no mathematical change)

- **v7 Theorem B Step 1 is known.** McNulty-Pammer-Weigert, *Mutually unbiased product bases for multiple qudits* (arXiv:1510.08085, 2016), Corollary 6: for `d = d1 d2` with `d1 = 2` (or 3) and `d2` prime with `d2 >= d1`, any vector mutually unbiased to `d1 + 1` MU product bases is maximally entangled. v7 re-derived it; it is not a new contribution. The `d = 6` case of the full non-extension is McNulty-Weigert (arXiv:1203.6887).
- **The open class-A question is an instance of an expectation stated there.** The same paper says: "We expect similar results to hold for larger product dimensions", meaning non-existence of vectors unbiased to three MU product bases. For `C^2 (x) C^5`, every direct product triple pairs the three qubit bases with three of the six Weyl MUBs of `C^5`, because all complex Hadamard matrices of order 5 are Fourier type (Haagerup). The triples therefore fall exactly into v7's classes A and B.
  - Class B was verified by computer (I1, Grassl-McNulty-Mista-Paterek).
  - Class A is the remaining direct case of that expectation.
  - Indirect product triples (as `T1` in `d = 6`) are NOT treated here and are not needed for RQLS10.

## 2. The core and why it matters

The **Weyl core** is the problem obtained from v7 (7.1) by deleting the G-condition: orthonormal E-flat `b0, b1` in `C^5` with `(b0 +/- b1)/sqrt2` both F-flat.

- In `C^10` it is equivalent to a biunimodular `psi` (unbiased to the `Z10` and `X10` eigenbases) with `A(5,5) = 0`.
- Equivalently, `E := sum_{t even} conj(psi_t) psi_{t+5} = 0`. Here `Re E = 0` already follows from biunimodularity, because the odd-`t` sum equals `conj(E)` and their total is `R(5) = 0`. So the extra condition is `Im E = 0`.
- **Both Weyl classes contain the core.** Emptiness of the core would close the whole Weyl family in writing, without I1. The `d = 6` analogue is empty, by McNulty-Weigert's Steps 2-3, which use only `z, x` and the marginal.

**Compact form.** Write `b0 = a/sqrt5`, `b1 = b/sqrt5`, `a_K = e^{-i theta_K} w_K` and `b_K = e^{i theta_K} w_K`, with `w` in `T^5` and `theta` in `(R/piZ)^5`. Then `a + b = 2 cos(theta) w` and `a - b = -2i sin(theta) w`. Put `rho_K(m) = conj(w_K) w_{K+m}`. The core is exactly:

    (i)   sum_K e^{2 i theta_K} = 0
    (ii)  sum_K cos(theta_K - theta_{K+m}) rho_K(m) = 0      (m = 1, 2)
    (iii) sum_K cos(theta_K + theta_{K+m}) rho_K(m) = 0      (m = 1, 2)                      (2.1)

Here (ii) and (iii) are the sum and difference of the perfectness conditions for `cos(theta) w` and `sin(theta) w`; `m = 3, 4` are their conjugates. This is 10 real equations in 9 real unknowns, and no continuous symmetry remains. **The core is overdetermined by one**, and generically empty. This is not proved.

## 3. Written exclusions inside the core

**Theorem 3.1 (Gaussian pairs).** No core solution has both `a` and `b` Gaussian.

- Different quadratic parts: then `<a,b>` is a nondegenerate Gauss sum of modulus `sqrt5 != 0`.
- Same quadratic part `q`: write `a = omega5^{qK^2 + j1 K}`, `b = omega5^{qK^2 + j2 K}` with `j1 != j2`. Then `R_a = R_b = 0` off zero. At `m = (j1 - j2)/(2q)`, the cross term `C_ab(m) = 5 omega5^{q m^2 + j2 m}` is nonzero while `C_ba(m) = 0`, because `2(j1 - j2) != 0`. So `R_{a +/- b}(m) != 0`. QED.

**Corollary 3.1'.** Every Gaussian (chirp) or CRT-product biunimodular vector on `Z10` has a pure qubit marginal. Chirps are eigenvectors of some `XZ^k`, whose CRT tensor product has simple spectrum, so they are product states. Any core solution is therefore a non-Gaussian, non-product biunimodular 10-vector.

**Theorem 3.2 (Fourier-invariant planes).** No core solution has `P = span(b0,b1)` invariant under the unitary DFT `F5`.

Proof. Invariance makes `F5|_P` map the E-flat pair to an F-flat pair, so `n_F = R(F5|_P) n_E`. Orthogonality forces a quarter turn: the eigenvalue ratio is `+-i` and `n_E` is perpendicular to the eigen-axis.

`F5` has multiplicities `1:2, -1:1, i:1, -i:1`. The `+-1` eigenvectors are even and the `+-i` eigenvectors are odd. In the even basis `(delta0, (delta1+delta4)/sqrt2, (delta2+delta3)/sqrt2)`, the 1-eigenspace is spanned by `(0,1,-1)` and `(1, g', g')` with `g' = (sqrt5 - 1)/(2 sqrt2)`. The -1-eigenvector is `(1, -(sqrt5+1)/(2sqrt2), -(sqrt5+1)/(2sqrt2))`.

Write `b0, b1 = (phi1 +- e^{i kappa} phi2)/sqrt2`. E-flatness then needs `|phi1(K)|^2 + |phi2(K)|^2 = 2/5` and `Re(e^{i kappa} conj(phi1(K)) phi2(K)) = 0`. Since `phi2` is odd, this gives `|phi1(0)|^2 = 2/5`.

- `(-1, +-i)`: `|phi1(0)|^2 = (5 - sqrt5)/10 != 2/5`.
- `(1, +-i)`: the Re-conditions force `phi1` to be `i` times a real vector in the 1-eigenspace. A nonzero real part would have to be supported at `K = 0`, and `delta0` is not an eigenvector. Then `t^2 = 2/5` and `s^2 = sqrt5/10`, so `|phi2(2)|^2/|phi2(1)|^2 = (5 +- 2R)/(5 -+ 2R)` with `R = sqrt(3 sqrt5 - 5)`. Since `sqrt5 < 2.2361`, `R^2 < 1.7083` and `R < 1.3071`, so the ratio lies in `(2.3858/7.6142, 7.6142/2.3858)`, which is inside `(0.31, 3.2)`.

But the odd eigenvectors have ratio `(lambda - s1)/(lambda + s1) < 0.081`, or its inverse `> 12.3`, where `lambda = sqrt5/2` and `s1 = sin 72°`. These use only `s1^2 + s2^2 = 5/4` and `(y/x)^2 = (lambda - s1)/(lambda + s1)`. The ranges are disjoint, a contradiction. QED.

Scope: `F5` itself only. Its compositions with dilations or Weyl translations are not treated.

**Theorem 3.3 (H-pairs, recalled).** v7 Lemma E2 already excludes `P` spanned by two vectors of one further MUB, and Lemma E3 excludes mixed pairs. Both hold inside the core: E2 uses only E and F, and E3 only E.

## 4. Status

Open: the Weyl core (2.1), Weyl-A (v7 (9.1)), and dihedral-A/B (v8 (5.1) with E1). Unrestricted maximal 1-RQLS(10) is UNKNOWN. Written evidence does not settle either way whether the NEB-orbit route is dead. Every structured candidate tested has failed, and both Weyl classes are inside an overdetermined core. A decisive step would be an analytic emptiness proof of the core (2.1) for `p = 5`, which would extend McNulty-Weigert from `d = 6` to `d = 10`, or an admitted exact elimination. Novelty: UNCLEAR. Same-harness written candidate only.
