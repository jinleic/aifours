# Erratum E1 to v8 (marginal IS forced) and a new exact exclusion of dihedral H-pair planes

Owner PhysicsRQLS10-2. Actual `/bin/date` observed immediately before this file: `Sun Oct 25 20:53:02 PDT 2026`. Additive to the pinned `global-neb-orbit-dihedral-v8.md` (SHA256 `94ee295f8171ff6faeb5098af814cb8f025e066a7395c82ab95cb25a9548917d`), which is NOT edited. WRITTEN only; no interpreter, program, CAS, enumeration, solver, replay, CLI, nested agent or GO. V9/v10/v11/HOLD unchanged.

## 1. Erratum (MAJOR author error in v8, corrected here)

v8 Section 0 (second bullet of "Unlike the Weyl family"), Section 3 (closing paragraph) and Section 6, together with `checkpoint-dihedral-neb-family-v1.json` item (N4), state that the dihedral family's qubit marginal is NOT forced to be maximally mixed. **WITHDRAWN: that is false.** The marginal is forced to be `I/2`, exactly as in the Weyl family. Corrected proof:

Write `u_e = (conj<e|v0>, conj<e|v1>)` and `alpha_L = <f_L|v0>`, `gamma_L = <f_L|v1>`. Expanding (C2) in the F-basis (`D5(mu) = sum_L chi_L(mu)|f_L><f_L|`, `Pi5 f_L = f_{-L}`) gives, for every `L`,

    conj(alpha_L) gamma_{-L} + alpha_{-L} conj(gamma_L) = 0.      (E1.1)

Together with (C1), `|alpha_L|^2 + |gamma_L|^2 = 1/5` for all `L`, this says the Bloch vector of `u_{-L}` is the `x`-reflection `R_x` of that of `u_L`:

- If the `alpha`'s are nonzero, the ratio `r = gamma/alpha` obeys `r_{-L} = -conj(r_L)`, and the norms are equal.
- If `alpha_L = 0`, then (E1.1) forces `alpha_{-L} = 0`.
- At `L = 0`: `Re(conj(alpha_0) gamma_0) = 0`.

Then `conj(alpha_L) gamma_L + conj(alpha_{-L}) gamma_{-L} = 2i Im(...)`. By Parseval, `Re<v0,v1> = Re sum_L conj(alpha_L) gamma_L = 0`. In the G-basis (`Pi5 g_M = g_{-M}`), (T2) gives `conj(C_M) D_{-M} = C_{-M} conj(D_M)`, i.e. the reflection `R_y`, and hence `Im<v0,v1> = 0`. (R) gives `|v0| = |v1|`. **So `<v0,v1> = 0` and `rho_A = I/2`.**

Corrected Bloch form of the dihedral family, with `psi = (|0>(x)b0 + |1>(x)b1)/sqrt2`, `b0` and `b1` orthonormal, and `|u_e|^2 = 2/5` for `e` in `E ∪ F ∪ G`:

    (E) r_K _|_ z;      (F) r_{-L} = R_x r_L;      (G) r_{-M} = R_y r_M.      (E1.2)

Compare the Weyl family: `r_L _|_ x` and `r_M _|_ y`. v8's other statements are unaffected: system (5.1), Theorems 4.1-4.3, Proposition 1 and Theorem 7. The unforced-marginal claim was never used in any proof there. Theorem 4.1 already worked with `<v0, Pi5 v1> = 0` and even vectors. This is recorded as an author process/mathematics MAJOR in the v8 headline. The frozen file remains as written, and this erratum must accompany any citation of v8.

## 2. New theorem: every dihedral H-pair plane fails (both classes)

**Setting.** Take an H-line of slope `s` (one of the three slopes outside `{E, F, G}`). Its stabilizer basis is `h_beta(K) = omega5^{(s/2)K^2 + beta K}/sqrt5`. Use symmetric Weyl operators `D(p,q) = tau^{pq} X^p Z^q` (`tau^2 = omega5`) and phase points `A_u = D(2u) Pi5`, so that `(A_u w)(K) = omega5^{2u2(K - u1)} w(2u1 - K)`.

**Lemma 2.1 (exact cross-Wigner value).**

    <h_beta, A_u h_beta'> = omega5^{u1(beta' - beta)}  if  u2 = s u1 + (beta + beta')/2,   and 0 otherwise.

Proof: the `K^2` terms cancel, and the remaining character sum is `5` exactly on the stated affine midline. Substituting the midline into the constant exponent `-2u1u2 + 2s u1^2 + 2 beta' u1` gives `u1(beta' - beta)`.

**Theorem 2.2.** Every dihedral solution satisfies `span(b0, b1) != span(h_beta, h_beta')`. This holds for every H-basis, every `beta != beta'`, and both classes.

Proof:

1. Inside that plane, E-flatness forces `{b0, b1} = {h_beta, e^{i chi} h_beta'}`. The values `5 conj(h_beta(K)) h_beta'(K)` are five unit complex numbers summing to `0`, and the odd-sum argument (v7 E1) shows they are not collinear, so the only E-flat rays are the two basis vectors.
2. Lemma 2.1 meets F (`u = (u1, 0)`) at the single point `u1 = -(beta + beta')/(2s)`, and meets G (`u = (u1, c u1)`, `c` the slope of G) at `u1 = (beta + beta')/(2(c - s))`.
3. (C2) and (T2) reduce to `e^{i chi} z_F` in `iR` and `e^{i chi} z_G` in `R`. Therefore `z_F/z_G = +-i`.
4. But Lemma 2.1 gives `z_F/z_G = omega5^{-(beta'^2 - beta^2) c/(2s(c - s))}`, a 5th root of unity, which is never `+-i`. Contradiction.

(For `beta' = -beta` both points are the origin and the ratio is 1.) QED.

The Weyl analogue was already excluded by v7 Lemma E2. Mixed planes `span(h in H_i, h' in H_j)` are excluded for BOTH families by v7 Lemma E3: (R) forces the flat E-diagonal `1/5` of `P/2`, and that lemma shows such planes cannot have it.

## 3. Status

Theorem 2.2 removes the most natural structured candidates of the dihedral family. The exact open systems are unchanged: Weyl-A (v7 (9.1)), dihedral-A and dihedral-B (v8 (5.1)). The Bloch form (E1.2) is the corrected interface. No witness, no unrestricted no-go and no acceptance is claimed.
