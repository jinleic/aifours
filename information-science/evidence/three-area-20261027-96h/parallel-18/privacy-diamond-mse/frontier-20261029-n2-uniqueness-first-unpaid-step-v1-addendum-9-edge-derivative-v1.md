# Addendum 9: the edge c-derivative identity VERIFIED, with normal-cone implication

Owner: InfoResearch96h-2 / info-1. Observed `/bin/date`: `Fri Oct 30 03:50:36 PDT 2026`. ADDITIVE to the chain (all prior bytes unchanged, incl. addendum-8 `76bd4647…`). Parent candidate attributed; verification owner-written, UNREVIEWED. Standing hypothesis (cutoff two, λ=V∈(1/2,2]) retained; no parameters selected, no programs.

**Theorem (identity, verified).** At u=a+1/2 on the weak-slack edge (λ≥v+(2u+m)², addendum 7 (E); T2=m+2m²=m²+v),

    b⁻¹∂_c⁺h(a,u;λ) = (16/3)T3 + 32uT2 + 64mu² + (128/3)u³ − (16u+8m)λ.      (∗)

**Derivation from the full functional.** Under (E): on y∈[0,a], slack forces Π0=2a−y and R1≥2a+1−y=2u−y, so Π1=min(2u−y,max(u,R1))=2u−y; on y∈(a,u] the corner box pins Π1=2u−y, and the independent clip coincides with it (R1≥2u−y). Hence Π1(y;u)=2u−y for ALL y∈[0,u]; face ties form a null set and do not affect the integral. With h=(1−b)Φ0+b[const_λ(c)+8∫₀^cψ1(Π1(y;c),y)dy], const_λ=(16/3)cT3+4c²T2−λ8cm−λ2T2·(−1)… precisely const_λ(c)=(16/3)cT3+4c²T2−λ(8cm+2T2):

    dconst = (16/3)T3+8uT2−8λm;
    endpoint: 8ψ1(Π1(u;u),u)=8ψ1(u,u)=8[T2u+2mu²]  (the cubic terms cancel exactly);
    face: 8·2∫₀^u ∂_zψ1(2u−y,y)dy with ∂_zψ1=(z+m)²+v+y²−λ and the exact integral
          ∫₀^u[2y²−(4u+2m)y+4u²+4mu+T2−λ]dy = (8/3)u³+3mu²+(T2−λ)u
          (coefficient check: (2/3−2+4)u³=(8/3)u³; −mu²+4mu²=3mu²; m²+v=T2),
    giving face term (128/3)u³+48mu²+16(T2−λ)u.

Summing: (16/3)T3 −8λm + (8+8+16)uT2 + (16+48)mu² + (128/3)u³ − 16λu = (∗). All moving limits are the three displayed terms; the a-dependence enters only through u. Weak slack persists for c>u (addendum-7 propagation), so (∗) is the genuine RIGHT derivative; Danskin's one-sided form applies since the face is the pointwise minimizer with continuous value at ties.

**Exact normal-cone implication (and only this).** By the adopted corrected corner condition (G2): h_c≥0 with h_a+h_c=0. Therefore:

- If (∗)<0 at a weak-slack edge point, that point VIOLATES the necessary corner condition and cannot be a constrained minimizer — an all-variable edge-exclusion test.
- If (∗)≥0, the h_c part of (G2) is satisfied there; NOTHING global follows (no uniqueness, no minimizer existence, no sign inference at other points, h_a-condition separate).

Substituting λ=v+(2u+m)² (tight (E)) into (∗) yields an explicit polynomial comparison in (u,m) that decides the tight-edge exclusion; no sign is asserted here. One consolidated proof; no flaw found in the parent candidate — it is verified exactly as stated.
