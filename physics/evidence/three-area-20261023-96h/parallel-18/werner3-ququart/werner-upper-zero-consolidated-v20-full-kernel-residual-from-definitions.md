# Werner upper zero — the exact universal residual for E_full itself (Lemma N_full), derived directly from the v1 definitions

PhysicsResearch96h-2 / physics-1. **WRITTEN OWNER-CANDIDATE; not parent-read, reviewed, adopted or checked in any kernel.** `/bin/date` immediately before creation: **Mon Oct 26 06:27:20 PDT 2026**.

Provenance. This packet was written under Main's v33 release, after the cp047 whole-state ACK (`2ccf78605d76cf14429cd76141c98d76f356680025c17eb468ad1b81251bc622`), and after v19 (`6467e82697ceedf6d03e9a6b9b0bab0cce00a96ae9a1295eee7a49a69b0f9d29`). v19 was authored after the cp047 ACK/SEND but before v33 was received. Mandatory provenance for v19, v20 and everything they build on:

- v24/v29/v33;
- cp047 B1–B3;
- F1–F5 are owner-reported pre-trial and UNREVIEWED.

Method:

- Universal statements only (every positive spectrum).
- Symbolic variables and rational coefficients only.
- No region, threshold, parameter instance, numerical example or zero-credit guidance.
- Held leads B1–B3 are not used.
- No interpreter, calculator, Eval, CAS, program, solver, enumeration, replay, CLI, nested agent or GO.

All process findings and the HOLD remain.

## 0. Result and limits

1. Every identity that v19 imported from the owner-candidate v18 is re-derived here directly from the operator definitions in v1 §2 (ρ', j, K_c, K_full, E_full).
2. **Theorem (universal equivalence).** At every positive spectrum, E_full,c(Z)≥0 for all Z with Zc=0 iff Lemma N_full holds (§4). Lemma N_full is v19's Lemma N with one extra explicit Hermitian term Δ_K(σ) added on the larger side. Δ_K is the full raw q correction K_full−K_c written in edge coordinates.

**Lemma N_full is NOT proved here.** Consequently E_full≥0, Z_up≥0, P11, the other three canonical signs and W4 remain NOT proved. Nothing here is a completion claim. G13 and the bare dual lift remain FALSE and are not used.

## 1. Definitions used (verbatim content of v1 §2 / v4 §3)

`werner-upper-zero-consolidated-v1.md` (`b006646d85afb5b6f4428880d733a413f22f6a92c4320654e4d8dabbcafd553b`) §2 gives the definitions below.

Basic quantities:

- c_i>0 with Σc_i^2=1; x_i=c_i^2, d_i=1-x_i, D=diag(d_i), d_ij=(d_i+d_j)/2;
- Q=I-cc^T, r=1/Σ_i(1/d_i), W=e3(d).

Operators on H={Zc=0}, Hermitian Hilbert–Schmidt pairing <A,B>=tr(A^†B):

- `B'Z=D^2 Z-D diag(Z_ii) Q`;
- `rho'Z=B'Z+r Q Z^T Q`;
- `j_ij(Z)=[d_i(1+d_i)Z_ij+d_j(1+d_j)Z_ji+c_i c_j(d_i Z_ii+d_j Z_jj)]/(d_i+d_j)`.

Kernels:

- K_c: `(K_c)_(ij,ij)=1+d_i d_j/d_ij^2`, `(K_c)_(ij,it)=-d_i c_j c_t/(2 d_ij d_it)`, 0 on disjoint edges.
- K_full: `(K_full)_(ij,ij)=3-2 d_ij d_kl/W`, where {k,l} is the complement of {i,j}; `(K_full)_(ij,it)=-c_j c_t/(2 d_jt)`; 0 on disjoint edges.

Comparisons:

- `E_full,c(Z)=<Z,rho'Z>-j^dagger K_full^-1 j`.
- G7 (the R0 comparison) is `<Z,rho'Z>>=j^dagger K_c^-1 j`.

Joint forms. Completing the square in F (K_full, K_c > 0) gives

`min_F [<Z,rho'Z>-sqrt(2)Re(j^dagger F)+(1/2)F^dagger K F] = <Z,rho'Z>-j^dagger K^-1 j`  for K in {K_c, K_full}.

Imported and not re-proved: K_full≥K_c (addendum-2 `ef401cddef2d596c1b3bbd53bbfac3f05a48f53c3d43cf3f61c6b242b78cda64`, v7 `31f993aa031d4affc156f08bfe58ec289eb10d287f2351da0be4938eccb49d08`). It is used ONLY for the remark Δ_K⪰0 in §3. The equivalence in §4 does not use it.

## 2. Direct derivation of the v19 inputs (I1)–(I4)

Coordinates as in v19: T_ij=Z_ij/(c_i c_j) for i≠j, `Tbar_i=Σ_j x_j T_ij/d_i`, Z_ii=-d_i Tbar_i, and var_i(w) as in v19 (weighted variance identity (WV)). Edge coordinates: F_ij=sqrt(2) w_ij σ_ij with w_ij=c_i c_j d_ij.

**(I2) p energy.**

1. `<Z,B'Z>=Σ_i d_i^2 Σ_j|Z_ij|^2-Σ_i d_i Z_ii conj(Σ_j Z_ij Q_ij)`. Here `Σ_j conj(Z_ij)Q_ij=conj(Z_ii)-c_i conj((Zc)_i)=conj(Z_ii)`. So `<Z,B'Z>=Σ_i d_i^2Σ_j|Z_ij|^2-Σ_i d_i|Z_ii|^2`.
2. In T coordinates this is `Σ_i d_i^2 x_i Σ_j x_j|T_ij|^2+Σ_i(d_i^4-d_i^3)|Tbar_i|^2=Σ_i d_i x_i[d_iΣ_j x_j|T_ij|^2-d_i^2|Tbar_i|^2]=Σ_i d_i x_i var_i(T)`.
3. Next, `<Z,QZ^TQ>=tr(QZ^dagger Q Z^T)=<QZQ,Z^T>`. With M=QZQ=Z-cu^T and u=Z^Tc, `<M,uc^T>=Σ_i u_i conj((Mc)_i)=0`, so `<M,Z^T>=<M,M^T>`. This equals <Z,Z^T> by v19 Lemma 1.
4. Hence `P(Z)=<Z,rho'Z>=Σ_i d_i x_i var_i(T)+r<Z,Z^T>`.

**(I4) forcing.** Substitute Z_ij=c_i c_j T_ij and Z_ii=-d_i Tbar_i. Then `j_ij=c_i c_j[ψ_ij+ψ_ji]/(d_i+d_j)` with `ψ_ij=d_i(1+d_i)T_ij-d_i^2 Tbar_i`.

**(I3) base q energy.**

1. Write `(1/2)F^dagger K_c F=Σ_e w_e^2 (K_c)_ee|σ_e|^2+Σ_{e~f} 2w_e w_f (K_c)_ef Re(conj(σ_e)σ_f)`, the second sum over unordered pairs sharing a vertex.
2. For e=ij and f=it, `w_e w_f|(K_c)_ef|=d_i x_i x_j x_t/2=:γ_(i;jt)`. Use `-2Re(conj a b)=|a-b|^2-|a|^2-|b|^2`.
3. The diagonal becomes `x_i x_j(d_ij^2+d_i d_j)-Σ_t[γ_(i;jt)+γ_(j;it)]=x_i x_j[d_ij^2+d_i d_j-d_ij(1-x_i-x_j)]`.
4. Since `1-x_i-x_j=2d_ij-1`, this equals `x_i x_j[d_ij(1-d_ij)+d_i d_j]=x_i x_j g_ij=m_ij`.
5. Therefore `Q_K(σ)=Σ_e m_e|σ_e|^2+Σ_i(d_i x_i/2)var_i(σ)`.

**(I1) joint form.**

1. `conj(j_e)w_e=x_i x_j conj(φ_e)/2`, because `d_ij/(d_i+d_j)=1/2`. Hence `sqrt(2)Re(j^dagger F)=Re Σ_e x_i x_j conj(φ_e)σ_e`.
2. So the K_c joint form equals v19's `Phi(Z,σ)=P-Re Σ_e x_i x_j conj(φ_e)σ_e+Q_K(σ)`.
3. G7 holds iff Phi≥0 on H×C^6.

## 3. The full raw correction in edge coordinates

Define `Δ_K(σ)=(1/2)F^dagger(K_full-K_c)F` with F=sqrt(2)w∘σ. From the definitions:

- diagonal: `w_e^2[(K_full)_ee-(K_c)_ee]=x_i x_j(2d_ij^2-2d_ij^3 d_kl/W-d_i d_j)`;
- shared pair e=ij, f=it: `2w_e w_f[(K_full)_ef-(K_c)_ef]=x_i x_j x_t(d_i-d_ij d_it/d_jt)`.

Therefore

`Δ_K(σ)=Σ_e x_i x_j(2d_ij^2-2d_ij^3 d_kl/W-d_i d_j)|σ_e|^2 + Σ_i Σ_(j<t) x_i x_j x_t(d_i-d_ij d_it/d_jt) Re(conj(σ_ij)σ_it)`.

The K_full joint form is `Phi_full=Phi+Δ_K(σ)`. By the import K_full≥K_c, Δ_K⪰0 (remark only).

## 4. Theorem — exact universal residual for E_full

At every positive spectrum, the following are equivalent:

- (a) E_full,c(Z)≥0 for every complex Z with Zc=0;
- (b) **Lemma N_full**: for all T in C^12 and σ in C^6,

`Σ_e Etilde_e(T_ij,T_ji,σ_e) + Σ_i (d_i x_i/2) var_i(σ-T) + Δ_K(σ)  >=  Σ_i (r-d_i x_i/2) var_i(T)`,

where Etilde_e is v19's edge form; every Etilde_e is PSD at every positive spectrum (v19 Lemma 4).

*Proof.*

1. (a) holds iff `min_F J_full≥0` for all Z, by §1. Since Z↦T is bijective, this holds iff Phi_full≥0 on C^12×C^6.
2. By §3 and v19 identity (J), `Phi_full=Σ_e Etilde_e+Σ_i(d_i x_i/2)var_i(σ-T)-Σ_i(r-d_i x_i/2)var_i(T)+Δ_K(σ)`. ∎

Lemma N (v19) implies Lemma N_full whenever Δ_K⪰0. Lemma N_full is the residual of the ORIGINAL E_full leaf. It keeps the entire raw q correction and makes no symmetry, reality or sector assumption on Z.

## 5. Exact remaining gap (universal)

- Prove Lemma N_full (or the stronger Lemma N) for EVERY positive spectrum and all (T,σ), or exhibit an exact violating spectrum together with its W4 eligibility boundary.
- The negative side consists only of `(r-d_i x_i/2)var_i(T)` at vertices with `r>d_i x_i/2`. The available nonnegative terms are:
  - the PSD edge forms Etilde_e, whose Schur margins are at least `x_i x_j d_i d_j/2` in σ_e;
  - the σ-T row variances;
  - Δ_K.
- The other three canonical signs (F_up, F_low, Z_low) and unrestricted rank≤2 W4.

No falsifying spectrum, physical witness, region or instance is supplied or claimed.

## 6. Assurance

Same-harness owner-written exact symbolic algebra only. Not reviewed, formal, kernel, executable, configured-family, cross-vendor, human or novelty accepted. Original cutoff 2026-10-27T11:05:38-07:00 and deadline 12:35:38 unchanged. No park and no round closeout.
