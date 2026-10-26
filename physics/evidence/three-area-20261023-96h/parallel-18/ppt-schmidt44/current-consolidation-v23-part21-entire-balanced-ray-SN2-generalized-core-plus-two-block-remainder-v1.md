# CURRENT P44 CONSOLIDATION v23 — PART21/21: the ENTIRE balanced ray R_(s,s,s,s), s>0, has Schmidt number two; the Part20 gap (2/√5,1)∪(1,3/2) is closed by an s-dependent Part13 core plus the two-block remainder

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Mon Oct 26 01:05:44 PDT 2026**. Exact WRITTEN mathematics; every identity and inequality is displayed and checked by hand. No scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO. Same original cutoff and deadline.

## R0. Scope and union

The NEW claims C42 and C43 sit on the ORIGINAL chart. The complete current union is the twenty parts plus Part15 ADDENDUM-1 bound in `checkpoint-103-complete-current-v22-twenty-part-manifest-v1.json` (SHA256 7e0e045d723d47607735bcb7c82fd533f71e2bb853079e46b256b85de2579603), THIS part, and all mandatory overlays. Parts 9–21 are LATER UNREVIEWED.

Imports:
- Part10 H1.1/H1.2 chart and coefficient matrix;
- Part13 X2 core design, generalised below and fully re-derived here;
- Part20 (B1.1) coefficient calculus, B3 mixed family and principle (B-P);
- Part20 C41;
- Part15 Q6.

Throughout, x=(s,s,s,s) with s>0, so u=v=w=z=s.

## R1. The s-dependent core family (eight vectors)

Fix κ>0 with sκ^2<1, and put

`ρ := (1 - sκ^2) / (κ(s+1)) > 0,   γ := √ρ · e^{-iπ/4},   so γ^2 = -iρ.`

The eight members, with equal weight 1/8, are:
- δ=iκ with β,χ each independently in {+γ,-γ};
- δ=-iκ with β,χ each independently in {+γ̄,-γ̄}.

For each member set

`ψ = a + β b + χ c + δ d - sδ e + sδ(χ-1) f + sδ(β-1) g.                    (R1.1)`

**Rank.** By H1.2, with α=1, γ_c=χ, ε=-sδ, φ=sδ(χ-1), η=sδ(β-1), κ_j=λ=0:
- row0 = [1, β, δ, 0];
- row1 = [χ, 1, β, 0];
- row2 = [-sδ, -χ, 1, 0];
- row3 = [sδ+sδ(χ-1), sδ, sδ+sδ(β-1), sδ-sδ] = [sδχ, sδ, sδβ, 0] = sδ·row1.

Column 3 is zero. Expanding along row 0,

`det[[1,β,δ],[χ,1,β],[-sδ,-χ,1]] = (1+βχ) - β(χ+sβδ) + δ(-χ^2+sδ) = 1 - δ(sβ^2+χ^2) + sδ^2.`

- First branch: β^2=χ^2=-iρ, so δ(s+1)(-iρ) = iκ(s+1)(-iρ) = κ(s+1)ρ = 1-sκ^2, and sδ^2=-sκ^2. The determinant is 1-(1-sκ^2)-sκ^2 = 0.
- Second branch: β^2=χ^2=iρ and δ=-iκ give the same two numbers.

Hence SR(ψ)<=2. At s=1, κ=2/3 we get ρ=5/12, which recovers Part13 X2 exactly.

**Moments.** Within each branch the signs of β and χ are independent, and E[δ]=0 across branches. So every mean, and every cross-moment that is odd in β or χ, vanishes. The remaining moments are:
- E|β|^2 = E|χ|^2 = ρ, and E[βχ̄]=0;
- |δ|^2 = κ^2;
- E[δ conj(-sδ)] = -sκ^2;
- E[δ conj(sδ(χ-1))] = sκ^2 E[χ̄-1] = -sκ^2, and the same for g;
- E[-sδ conj(sδ(χ-1))] = s^2κ^2, and the same for g;
- E|sδ(χ-1)|^2 = s^2κ^2(ρ+1), and the same for g;
- E[sδ(χ-1) conj(sδ(β-1))] = s^2κ^2(E[χβ̄]-E[χ]-E[β̄]+1) = s^2κ^2.

Every moment pairing b or c with d, e, f or g vanishes. For example b–g gives sE[δ̄(|β|^2-β)] = s(ρE[δ̄]-E[δ̄β]) = 0. Therefore

`E P(ψ) = P(a) + ρ[P(b)+P(c)] + κ^2 P(d - s e - s f - s g) + s^2κ^2ρ [P(f)+P(g)].   (R1.2)`

At s=1, κ=2/3 this is Part13 (X2.2).

## R2. The remainder

By (B1.1), R_x - E P(ψ) = (1-ρ)[P(b)+P(c)] + F M F^†, where F has columns (d,e,f,g,h,j) and

`M = 3I - κ^2 ω ω^T - s^2κ^2ρ (E_ff + E_gg),   ω = (1,-s,-s,-s,0,0).`

Its entries are:
- d: 3-κ^2; e: 3-s^2κ^2; f = g: 3-s^2κ^2(1+ρ); h = j: 3;
- (d,e)=(d,f)=(d,g)=sκ^2;
- (e,f)=(e,g)=(f,g)=-s^2κ^2;
- every entry involving h or j off the diagonal is 0.

We need ρ<=1, since b and c are SR2 vectors.

## R3. Removing the d–e entry with the Part20 B3 family

Apply the Part20 B3 family (27 members, rank<=2 for every x) with a0 c0 = sκ^2. Its average contributes:
- (d,e) entry a0c0 = sκ^2, and no other off-diagonal entry;
- diagonals a0^2 (d), c0^2 (e), ν0^2c0^2 (f), a0^4/b0^2 (g), b0^2 (h), c0^2/ν0^2 (j).

Choose ν0^2c0^2 = a0^4/b0^2, so f and g lose the same amount. The remainder M' has:
- D := 3-κ^2-a0^2 (d);
- Ee := 3-s^2κ^2-c0^2 (e);
- G := 3-s^2κ^2(1+ρ)-a0^4/b0^2 (f and g);
- 3-b0^2 (h) and 3-c0^2/ν0^2 (j);
- (d,e)=0, (d,f)=(d,g)=m:=sκ^2, and (e,f)=(e,g)=(f,g)=-n with n:=s^2κ^2.

## R4. Two-block split with symmetric f,g

Write M' = Φ2 + Φ1 + (nonnegative h, j diagonals):
- Φ2 on (d,f,g) is [[D,m,m],[m,F1,X1],[m,X1,F1]];
- Φ1 on (e,f,g) is [[Ee,-n,-n],[-n,F2,X2],[-n,X2,F2]];
- F1+F2=G and X1+X2=-n.

In the basis (f±g)/√2 the (f,g) sub-block has eigenvalues F±X, and the d- (or e-) coupling meets only the + mode, with strength √2 m (or √2 n). Hence:
- Φ2>=0 iff F1-X1>=0 and D(F1+X1) >= 2m^2;
- Φ1>=0 iff F2-X2>=0 and Ee(F2+X2) >= 2n^2.

Choose P1=F1+X1 and P2=F2+X2 with P1>=2m^2/D, P2>=2n^2/Ee and P1+P2=G-n, and Q1=Q2=(G+n)/2 for the minus modes. This is possible iff

`2m^2/D + 2n^2/Ee <= G - n,   with D, Ee > 0 and G >= 0.                     (R4.1)`

F Φ2 F^† is supported on Alice{0,3}⊗C^4 and F Φ1 F^† on Alice{2,3}⊗C^4, so both are SN<=2 by (B-P).

## R5. Theorem C42 (the middle of the ray)

**C42.** For every s in [2/3, 3/2], SN(R_(s,s,s,s)) = 2.

*Proof.* Take κ=1/2, a0=c0=√s/2 (so a0c0=s/4=sκ^2), b0^2=3 and ν0^2=s/12. Then:
- ν0^2c0^2 = s^2/48 = a0^4/b0^2.
- The h entry is 0, and the j entry is 3-(s/4)/(s/12) = 0.
- sκ^2=s/4<1.
- ρ = (1-s/4)/((s+1)/2) = (4-s)/(2(s+1)), and ρ<=1 iff 4-s<=2s+2 iff s>=2/3.
- D = (11-s)/4 > 0.
- Ee = (12-s-s^2)/4 >= (12-3/2-9/4)/4 = 33/16 > 0 on the interval.
- G - n = 3-(s^2/4)(2+ρ)-s^2/48.
- 2m^2/D = s^2/(2(11-s)) and 2n^2/Ee = s^4/(2(12-s-s^2)).

**Left side of (R4.1).** Both terms increase on (0,3/2], because their numerators increase and their positive denominators decrease. So the left side is at most its value at s=3/2:

`(9/4)/19 + (81/16)/(33/2) = 9/76 + 27/88 = 198/1672 + 513/1672 = 711/1672 < 1/2.`

**Right side.** Since ρ<=1 on the interval, G-n >= 3-(3/4)s^2-s^2/48 = 3-(37/48)s^2 >= 3-(37/48)(9/4) = 243/192 = 81/64 > 1. Also G >= G-n > 0.

So (R4.1) holds on [2/3,3/2]. Then

R = E P(ψ) + (1-ρ)[P(b)+P(c)] + E P(B3 family) + F(Φ2+Φ1)F^†

is a positive combination of projectors onto SR<=2 vectors. So SN<=2, and Q6 gives SN>=2. ∎

**Spot check at s=1** (the Part13 point, with these new parameters):
- ρ=3/4, D=5/2, Ee=5/2, n=m=1/4;
- G = 3-(1/4)(7/4)-1/48 = 144/48-21/48-1/48 = 122/48 = 61/24;
- left side = 2(1/16)/(5/2) + 2(1/16)/(5/2) = 1/20+1/20 = 1/10;
- right side = G-n = 61/24-6/24 = 55/24. This agrees with the closed form 3-(1/4)(2+3/4)-1/48 = 3-11/16-1/48 = 110/48 = 55/24.

So 1/10 <= 55/24 holds.

## R6. Corollary C43 (entire balanced ray)

**C43.** R_(s,s,s,s) has Schmidt number exactly two for EVERY s>0.

Coverage:
- Part20 C41(b) covers s^2<=4/5, i.e. s<=2/√5≈0.894, and 2/3<2/√5;
- C42 covers [2/3,3/2];
- Part20 C41(a) covers s>=3/2.

The union is (0,∞). Through the Part6 involution, R_(1,1,-1,ζ) is also SN2 for every real ζ>0. Part20 C41(a) already gave all complex ζ with |ζ|<=2/3.

**Consequences.**
1. The far balanced ray, the chart's main SN3 candidate direction (Part14 C33.3, Part16), contains no SN3 state. Combined with Part15 Theorem E0 at the limit point x0, the whole closure of the ray in the involution chart is SN2.
2. The coordinate-peel barriers (C34.4, C35, C38) are method barriers only, as they were always labelled.
3. **Status of P44.** The chart family R_x was the round's principal explicit 4x4 PPT candidate family. Its balanced ray is now completely SN2, and large further regions are SN2 by Parts 6, 10, 13–15 and 18–20. No member of the chart is known to have SN3. P44 itself (an explicit 4x4 PPT SN>=3 state, or an unrestricted no-go) remains UNMET. The general-x version of R1 holds with ε=-zδ, φ=δ(vχ-u), η=δ(vβ-w) and det 1-δ(zβ^2+χ^2)+zδ^2; it is recorded as a tool, without a region claim.

**Original physics-3/P44 remains UNMET.** These are author-WRITTEN candidates pending fresh reconstruction. They are not formal/kernel/executable/triple/configured-family/human/cross-vendor/novelty acceptance, not a park and not a closeout.

**END OF COMPLETE CURRENT v23 PART21/21.**
