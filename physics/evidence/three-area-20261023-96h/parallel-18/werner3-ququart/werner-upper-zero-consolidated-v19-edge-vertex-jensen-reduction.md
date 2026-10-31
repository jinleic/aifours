# Werner upper zero — exact edge/vertex-mean decomposition of the joint form, all-spectra edge positivity, and reduction of G7 to one vertex-variance lemma

PhysicsResearch96h-2 / physics-1. **WRITTEN OWNER-CANDIDATE; not parent-read, reviewed, adopted or checked in any kernel.** `/bin/date` immediately before creation: **Mon Oct 26 06:16:55 PDT 2026**.

Provenance. The statements F1–F5 below were first recorded, without proofs, in checkpoint-046 (`23a4ece9cd320fd676601fec697a09c3c6ab1d2be4afb55584291338304c6122`, 05:57:45). That was before the derived-condition trials disclosed in `61bedebaa37af9b663f4f93c7c1e065fe62cf0883bc8df91d6b5ebb959a234bb`. Main's v29 classifies them as owner-reported pre-trial, UNREVIEWED and not adopted.

This packet only supplies complete written proofs. It was written after the v29 whole-state ACK (`2ccf78605d76cf14429cd76141c98d76f356680025c17eb468ad1b81251bc622`, sent before any further work), in symbolic variables with rational coefficients only.

It contains:

- no region, threshold or parameter-instance statement;
- no numerical example;
- none of the held leads B1–B3 of that ACK.

No interpreter, calculator, Eval, CAS, program, solver, enumeration, replay, CLI, nested agent or GO was used. All process findings and the HOLD remain.

## 0. Result and limits

For EVERY positive normalized four-Schmidt spectrum, the following hold.

1. On the whole p space H={Zc=0}, the joint form of (G6) splits exactly into edge forms in (T_ij, T_ji, σ_ij) and vertex forms in the weighted row means (Lemma 2).
2. A Jensen identity moves the vertex forms onto the edges. Every resulting edge form is positive semidefinite for every spectrum, with an explicit Schur margin (Lemmas 3 and 4).
3. Consequently the strong comparison G7 is EQUIVALENT to Lemma N (Theorem 5). In Lemma N, two families of nonnegative terms must dominate `Σ_i (r - d_i x_i/2) var_i(T)`. Only vertices with `r > d_i x_i/2` contribute positively to that right side.

**Lemma N is NOT proved here.** Consequently G7, E_full≥0, Z_up≥0, P11, the other three canonical signs and W4 are all NOT proved. G13 and the bare dual lift remain FALSE and are not used.

## 1. Imports (named, not re-proved)

- v18 `984348f49ab7c1bc31dae759d66f143f3f5b21fcb44bbaeba3a41d343fc20489` (owner-candidate, unreviewed), which itself imports G1–G8 of `249c1becd5e89ff08a3badebaab8234f3e89d7cb7879430e8e9152eabff18a7e`, the FALSE-G13 correction `1b0e9a523810b5fb29cfa3c53ad287112d19803dc8110913d1b1f975817e6eb5`, and `K_full>=K_c` from addendum-2 `ef401cddef2d596c1b3bbd53bbfac3f05a48f53c3d43cf3f61c6b242b78cda64` and v7 `31f993aa031d4affc156f08bfe58ec289eb10d287f2351da0be4938eccb49d08`. Used exactly:
  - (I1) the joint form `Phi(Z,σ)=P(Z)-Re Σ_e x_i x_j conj(φ_e)σ_e+Q_K(σ)` (v18 Lemma B). Since `F_c(Z)=sup_σ[Re Σ_e x_i x_j conj(φ_e)σ_e-Q_K(σ)]` (v18 Theorem C, step 1), G7 holds iff Phi≥0 on H×C^6.
  - (I2) `P(Z)=Σ_i d_i x_i var_i(T)+r<M,M^T>`, M=QZQ (v18 §4; generic G9 plus the N term).
  - (I3) `Q_K(σ)=Σ_e m_e|σ_e|^2+Σ_i (d_i x_i/2) var_i(σ)` (v18 Lemma A proof; G8 with gamma_(i;jt)=d_i x_i x_j x_t/2).
  - (I4) `φ_e=ψ_ij+ψ_ji`, `ψ_ij=d_i(1+d_i)T_ij-d_i^2 Tbar_i` (v18 §2; G5).
  - (I5) G7 ⇒ E_full≥0, because K_full≥K_c.

## 2. Notation

- c_i>0 with Σc_i^2=1; x_i=c_i^2, d_i=1-x_i, r=1/Σ_k(1/d_k).
- For an edge e={i,j}: d_e=(d_i+d_j)/2, δ_e=d_i-d_j, g_e=d_e-δ_e^2/4, m_e=x_i x_j g_e, p_e=x_i+x_j. {k,l} denotes the complementary edge.
- For Z in H: T_ij=Z_ij/(c_i c_j) for i≠j, `Tbar_i=Σ_(j≠i) x_j T_ij/d_i` and Δ_ij=T_ij-Tbar_i. Since `(Zc)_i=c_i(Z_ii+Σ_j x_j T_ij)`, we have Z_ii=-d_i Tbar_i. So Z↦T is a linear bijection H→C^12.
- σ in C^6 with σ_ij=σ_ji; S_i=Σ_(j≠i) x_j σ_ij, `σbar_i=S_i/d_i`, ρ_ij=σ_ij-σbar_i.
- For any array (w_ij)_(j≠i): `var_i(w)=Σ_(j<t; j,t≠i) x_j x_t |w_ij-w_it|^2`.
- (WV) Weighted variance identity. The weights x_j, j≠i, sum to d_i, so `var_i(w)=d_i Σ_j x_j|w_ij|^2-|Σ_j x_j w_ij|^2=d_i Σ_j x_j|w_ij-wbar_i|^2`, where wbar_i=Σ_j x_j w_ij/d_i.

Two scalar identities are used repeatedly:

- (S1) `(d_i^2+d_j^2)/2=d_e^2+δ_e^2/4`, hence `g_e+(d_i^2+d_j^2)/2=d_e(1+d_e)`.
- (S2) `g_e=d_e(1-d_e)+d_i d_j` and `1-d_e=p_e/2`, hence `4g_e=p_e(d_i+d_j)+4d_i d_j`.

## 3. Lemma 1 — the transpose pairing (F1)

For Z in H, `<M,M^T>=<Z,Z^T>=Σ_i d_i^2|Tbar_i|^2+Σ_(i≠j) x_i x_j Re(conj(T_ij)T_ji)`.

*Proof.*

1. Zc=0 gives ZQ=Z, so M=QZ=Z-cu^T with u=Z^T c.
2. Expanding gives `<M,M^T>=<Z,Z^T>-<Z,uc^T>-<cu^T,Z^T>+<cu^T,uc^T>`.
3. `<Z,uc^T>=Σ_i u_i conj((Zc)_i)=0` and `<cu^T,Z^T>=Σ_j conj(u_j)(Zc)_j=0`.
4. `<cu^T,uc^T>=|c^T u|^2=|(Zc)^T c|^2=0`.
5. Finally conj(Z_ij)Z_ji=x_i x_j conj(T_ij)T_ji for i≠j, and |Z_ii|^2=d_i^2|Tbar_i|^2. The sum is real. ∎

## 4. Lemma 2 — edge/vertex-mean decomposition (F2)

For all Z in H and σ in C^6,

`Phi(Z,σ)=Σ_e x_i x_j e_e(T_ij,T_ji,σ_e)+Σ_i x_i d_i v_i(Tbar_i,σbar_i)`,

where

- `e_e(a,b,s)=d_i^2|a|^2+d_j^2|b|^2+2r Re(conj(a)b)-Re[(d_i(1+d_i)conj(a)+d_j(1+d_j)conj(b))s]+d_e(1+d_e)|s|^2`,
- `v_i(a,s)=(d_i(r-d_i x_i)/x_i)|a|^2+d_i^2 Re(conj(a)s)-(d_i^2/2)|s|^2`.

*Proof.*

1. By (I2), (WV) and Lemma 1,
   `P=Σ_(i≠j) x_i x_j d_i^2|T_ij|^2+r Σ_(i≠j) x_i x_j Re(conj(T_ij)T_ji)+Σ_i d_i^2(r-d_i x_i)|Tbar_i|^2`.
2. By (I4) and σ_ij=σ_ji,
   `Σ_e x_i x_j conj(φ_e)σ_e=Σ_(i≠j) x_i x_j conj(ψ_ij)σ_ij=Σ_(i≠j) x_i x_j d_i(1+d_i)conj(T_ij)σ_ij-Σ_i x_i d_i^2 conj(Tbar_i)S_i`.
3. By (I3), (WV) and (S1),
   `Q_K=Σ_e x_i x_j d_e(1+d_e)|σ_e|^2-Σ_i (d_i x_i/2)|S_i|^2`.
4. Group the terms with both indices of an edge into e_e. Group the terms in (Tbar_i, S_i) into the vertex form. Substitute S_i=d_i σbar_i; then `x_i d_i v_i(Tbar_i,σbar_i)=d_i^2(r-d_i x_i)|Tbar_i|^2+x_i d_i^2 Re(conj(Tbar_i)S_i)-(d_i x_i/2)|S_i|^2`. ∎

## 5. Lemma 3 — Jensen split (F3)

**General identity.** Let ℓ_i (i=1..4) be ANY Hermitian forms on C^2. Then

`Phi=Σ_e x_i x_j[e_e-ℓ_i(T_ij,σ_e)-ℓ_j(T_ji,σ_e)]+Σ_i x_i d_i[v_i+ℓ_i](Tbar_i,σbar_i)+Σ_i x_i Σ_(j≠i) x_j ℓ_i(Δ_ij,ρ_ij)`.

*Proof.* Take a Hermitian form ℓ and weights ω_j=x_j/d_i, which sum to 1. Put u_j=(T_ij,σ_ij); its mean is ubar=(Tbar_i,σbar_i). Then `Σ_j ω_j ℓ(u_j)=ℓ(ubar)+Σ_j ω_j ℓ(u_j-ubar)`, because `Σ_j ω_j(u_j-ubar)=0` kills the cross terms. Multiply by x_i d_i, then add and subtract in Lemma 2. ∎

**Certificate principle (immediate).** Suppose Hermitian ℓ_i satisfy (i) ℓ_i⪰0, (ii) v_i+ℓ_i⪰0 and (iii) for every edge, the 3×3 form `e_e(a,b,s)-ℓ_i(a,s)-ℓ_j(b,s)⪰0`. Then Phi≥0, i.e. G7 holds at that spectrum. This is stated for any fixed spectrum; no choice of ℓ_i is made here.

**The choice ℓ_i=-v_i.** Here the mean term vanishes and Phi is given by (J) below.

- Edge part. `e_e+v_i(a,s)+v_j(b,s)` has |a|^2-coefficient `d_i^2+d_i(r-d_i x_i)/x_i=r d_i/x_i`. Its s-coupling is `-d_i(1+d_i)+d_i^2=-d_i`, and its |s|^2-coefficient is g_e by (S1).
- Deviation part. `-v_i(Δ,ρ)=(d_i^2/2)|ρ-Δ|^2+(d_i/x_i)(d_i x_i/2-r)|Δ|^2`. Since ρ_ij-Δ_ij is the deviation of (σ-T)_ij from its row mean, (WV) gives (J):

`Phi = Σ_e Etilde_e + Σ_i (d_i x_i/2) var_i(σ-T) - Σ_i (r-d_i x_i/2) var_i(T)`,       (J)

`Etilde_e(a,b,s)=r[x_j d_i|a|^2+x_i d_j|b|^2+2x_i x_j Re(conj(a)b)]-x_i x_j Re[(d_i conj(a)+d_j conj(b))s]+m_e|s|^2`.

Here (σ-T)_ij=σ_ij-T_ij is read along row i.

## 6. Lemma 4 — every edge form is PSD, for every spectrum (F4)

For every positive spectrum and every edge e={i,j}, with complementary edge {k,l}:

- (a) The (a,b) block `B_e=r[[x_j d_i, x_i x_j],[x_i x_j, x_i d_j]]` is positive definite, with `det B_e=r^2 x_i x_j(1-p_e)>0`.
- (b) The Schur complement of B_e in Etilde_e equals `x_i x_j (d_i d_j/4)[4-p_e(1/d_k+1/d_l)]`.
- (c) `p_e(1/d_k+1/d_l)=2-x_l/d_k-x_k/d_l<2`. Hence that Schur complement exceeds `x_i x_j d_i d_j/2>0`, and Etilde_e⪰0.

*Proof.* Divide by x_i x_j.

1. The block becomes `r[[d_i/x_i,1],[1,d_j/x_j]]`. Its determinant is `r^2(d_i d_j-x_i x_j)/(x_i x_j)=r^2(1-p_e)/(x_i x_j)`, which is positive because x_k, x_l>0.
2. With v=(d_i,d_j):
   `v^T B^-1 v = x_i x_j[d_i^2 d_j/x_j-2d_i d_j+d_j^2 d_i/x_i]/(r(1-p_e)) = d_i d_j[d_i x_i+d_j x_j-2x_i x_j]/(r(1-p_e)) = d_i d_j p_e/r`,
   because `d_i x_i+d_j x_j-2x_i x_j=p_e-p_e^2`.
3. So the Schur complement is `g_e-d_i d_j p_e/(4r)`.
4. With `1/r=1/d_i+1/d_j+1/d_k+1/d_l` we get `d_i d_j p_e/r=p_e(d_i+d_j)+p_e d_i d_j(1/d_k+1/d_l)`. By (S2), 4 times the Schur complement is `d_i d_j[4-p_e(1/d_k+1/d_l)]`.
5. Finally p_e=1-x_k-x_l=d_k-x_l=d_l-x_k, which gives (c). ∎

## 7. Theorem 5 — exact reduction (F5)

At any positive spectrum, G7 holds iff **Lemma N** holds: for all T in C^12 and σ in C^6,

`Σ_e Etilde_e(T_ij,T_ji,σ_e) + Σ_i (d_i x_i/2) var_i(σ-T)  >=  Σ_i (r-d_i x_i/2) var_i(T)`.      (N)

*Proof.* This is (I1), (J) and the bijection H→C^12. ∎

On the left of (N), every term is nonnegative: by Lemma 4, and because var_i≥0 with d_i x_i/2>0. On the right, vertex i contributes a nonpositive amount whenever `r<=d_i x_i/2`. By (I5), Lemma N for all spectra would give E_full≥0 (Z_up≥0, P11) for all spectra.

## 8. Exact remaining gap

- Lemma N for every positive spectrum and all (T,σ). Equivalently: the nonnegative variance terms `(r-d_i x_i/2)var_i(T)` at the vertices with `r>d_i x_i/2` must be absorbed by the PSD edge forms (Lemma 4, with their explicit Schur margins) together with the σ-T row variances. Each var_i(T) couples the three edges at vertex i. No region, threshold or instance claim is made in either direction.
- The other three canonical signs (F_up, F_low, Z_low) and unrestricted rank≤2 W4.
- Review of v18 and of this packet.

No falsifying spectrum or physical witness is supplied.

## 9. Assurance

Same-harness owner-written exact symbolic algebra only. Not reviewed, formal, kernel, executable, configured-family, cross-vendor, human or novelty accepted. Original cutoff 2026-10-27T11:05:38-07:00 and deadline 12:35:38 unchanged. No park and no round closeout.
