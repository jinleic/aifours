# Werner upper zero — universal consequences of the Jensen split: an explicit deficit bound, a positivity subspace containing K_B, and the exact closed form on all symmetric Z

PhysicsResearch96h-2 / physics-1. **WRITTEN OWNER-CANDIDATE; not parent-read, reviewed, adopted or checked in any kernel.** `/bin/date` immediately before creation: **Mon Oct 26 06:30:45 PDT 2026**.

Provenance. Written under Main's v33 release (universal conventional proof scope). It builds on:

- v19 `6467e82697ceedf6d03e9a6b9b0bab0cce00a96ae9a1295eee7a49a69b0f9d29`;
- v20 `b5c3d36c1b8594388b28c74a12e46de5adf4feb3d85a6d81d96d494a5a2c86ea`.

Mandatory provenance for those packets: v24/v29/v33, cp047 B1–B3, and F1–F5 being owner-reported pre-trial and UNREVIEWED.

Method:

- Every statement holds for EVERY positive spectrum.
- Symbolic variables and rational coefficients only.
- No region, threshold, parameter instance, numerical example or zero-credit guidance.
- B1–B3 are not used.
- No interpreter, calculator, Eval, CAS, program, solver, enumeration, replay, CLI, nested agent or GO.

## 0. Results and limits

For every positive spectrum c, with ν_i:=r-d_i x_i/2 and var_i, Etilde_e, Q_K, K_σ as in v18/v19:

1. **Universal deficit bound.** For every Z in H, `E_full,c(Z) >= E_c(Z) >= -Σ_i max(ν_i,0) var_i(T)`.
2. **Universal positivity subspace.** E_c≥0, hence E_full≥0, on the linear subspace `V_+(c)={Z in H: var_i(T)=0 for every i with ν_i>0}`. This subspace always contains the four-dimensional row-constant sector `K_B={Z=-diag(z)Q}` (T_ij=z_i). No claim is made about the size of V_+(c) at any spectrum.
3. **Exact closed form on ALL symmetric Z** (a six-dimensional subspace of H, with T_ij=T_ji=τ_e):
   `E_c(Z)=Σ_e x_i x_j(2r-d_e(1-d_e))|τ_e|^2+Σ_i d_i^2 ν_i|τbar_i|^2-(1/4)g^dagger K_σ^-1 g`, where `g_e=x_i x_j δ_e^2 τ_e/2`.
   Hence `E_c(Z)>=Σ_e x_i x_j μ_e|τ_e|^2+Σ_i d_i^2 ν_i|τbar_i|^2` with `μ_e=2r-d_e(1-d_e)-δ_e^4/(16 g_e)`.

Items 2 and 3 are SUBSPACE statements. They are necessary for the original sign but are not the original full-H statement. Item 1 is a quantitative bound, not a sign. **E_full≥0 on all of H for all spectra, the other three canonical signs and W4 remain NOT proved.**

## 1. Imports

- v19 identity (J): `Phi=Σ_e Etilde_e+Σ_i(d_i x_i/2)var_i(σ-T)-Σ_i ν_i var_i(T)`, together with Lemma 4 (each Etilde_e⪰0 for every positive spectrum).
- v20: (I1)–(I4) derived from the v1 definitions, and E_c(Z)=inf_σ Phi(Z,σ).
- `K_full>=K_c` (addendum-2 `ef401cddef2d596c1b3bbd53bbfac3f05a48f53c3d43cf3f61c6b242b78cda64`, v7 `31f993aa031d4affc156f08bfe58ec289eb10d287f2351da0be4938eccb49d08`). It gives `E_full>=E_c`.
- v18 Lemma A: `Q_K(ζ)=ζ^dagger K_σ ζ` with `K_σ=D_K-R^dagger Λ R⪰D_m=diag(m_e)`. Here `K_σ-D_m` is the γ-Laplacian (v20 (I3)), which is ⪰0.

## 2. Proofs of items 1 and 2

In (J), the first two sums are nonnegative for every σ: Lemma 4 gives the first, and var≥0 with d_i x_i/2>0 gives the second. Hence `Phi(Z,σ)>=-Σ_i ν_i var_i(T)>=-Σ_i max(ν_i,0)var_i(T)` for every σ. Taking the infimum over σ gives item 1, and K_full≥K_c gives the E_full part.

On V_+(c), every term with ν_i>0 vanishes, so item 1 gives E_c≥0.

If T_ij=z_i for all j, then each var_i(T)=0. Moreover Z_ij=c_i c_j z_i and Z_ii=-d_i z_i, i.e. Z=-diag(z)Q. ∎

## 3. Proof of item 3

Let T be symmetric and write σ=τ+ζ.

1. Since `x_j d_i+x_i d_j+2x_i x_j=x_i+x_j=p_e`, we get `Etilde_e=r p_e|τ_e|^2-2x_i x_j d_e Re(conj(τ_e)σ_e)+m_e|σ_e|^2`.
2. Substitute σ_e=τ_e+ζ_e and use `m_e-x_i x_j d_e=-x_i x_j δ_e^2/4`. This gives `Etilde_e=[r p_e-x_i x_j(d_e+δ_e^2/4)]|τ_e|^2-(x_i x_j δ_e^2/2)Re(conj(τ_e)ζ_e)+m_e|ζ_e|^2`.
3. var_i(σ-T)=var_i(ζ), and `Σ_e m_e|ζ_e|^2+Σ_i(d_i x_i/2)var_i(ζ)=Q_K(ζ)`.
4. By (WV), `Σ_i ν_i var_i(τ)=Σ_i ν_i d_i Σ_j x_j|τ_ij|^2-Σ_i ν_i d_i^2|τbar_i|^2`, and `Σ_e r p_e|τ_e|^2=r Σ_i Σ_j x_j|τ_ij|^2`.
5. The ordered-pair coefficient is therefore `r-ν_i d_i=r x_i+d_i^2 x_i/2`. Summed over both orientations of an edge, this gives `x_i x_j[2r+(d_i^2+d_j^2)/2]`.
6. Using `(d_i^2+d_j^2)/2=d_e^2+δ_e^2/4`, the total edge coefficient is `x_i x_j[2r+d_e^2-d_e]=x_i x_j(2r-d_e(1-d_e))`. Hence
   `Phi=Σ_e x_i x_j(2r-d_e(1-d_e))|τ_e|^2+Σ_i d_i^2 ν_i|τbar_i|^2-Re<g,ζ>+Q_K(ζ)`.
7. The infimum over ζ in C^6 of `Q_K(ζ)-Re<g,ζ>` is `-(1/4)g^dagger K_σ^-1 g`. This proves the closed form.
8. Finally, K_σ⪰D_m gives `(1/4)g^dagger K_σ^-1 g<=Σ_e|g_e|^2/(4m_e)=Σ_e x_i x_j δ_e^4|τ_e|^2/(16 g_e)`. ∎

**Consistency.** On the kernel of R (τbar=0), item 3 reduces to v18 §7's T2^0 formula. Indeed `K_σ^-1=D_K^-1+D_K^-1R^dagger W^-1 R D_K^-1` (v18 Theorem C) turns `(1/4)g^dagger K_σ^-1 g` into `Σ_e x_i x_j δ_e^4 θ_e|τ_e|^2/16+(1/4)h^dagger W^-1 h`, with `h_i=(1/2)Σ_j x_j θ_ij δ_ij^2 τ_ij`.

## 4. Exact remaining gap (universal)

- Lemma N_full (v20) for every positive spectrum on ALL of H. Equivalently, the deficit bound of item 1 must be beaten by the nonnegative terms of (J) plus Δ_K at every spectrum.
- On symmetric Z alone: positivity of the explicit six-dimensional form in item 3 for every spectrum. This is a necessary condition. It is not proved here in general, because this derivation does not give nonnegativity of the coefficients 2r-d_e(1-d_e) or ν_i.
- The other three canonical signs and unrestricted W4.

No falsifying spectrum, physical witness, region or instance is supplied or claimed.

## 5. Assurance

Same-harness owner-written exact symbolic algebra only. Not reviewed, formal, kernel, executable, configured-family, cross-vendor, human or novelty accepted. Original cutoff 2026-10-27T11:05:38-07:00 and deadline 12:35:38 unchanged. No park and no round closeout.
