# CURRENT P44 CONSOLIDATION v22 — PART20/20: a two-block remainder theorem gives SN2 on large regions of the original chart, including the far balanced ray for s>=3/2 and s<=2/√5, where every coordinate peel dies

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Mon Oct 26 00:59:26 PDT 2026**. Exact WRITTEN mathematics; every identity and inequality is displayed and checked by hand. No scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or GO. Same original cutoff and deadline.

## B0. Scope and union

The NEW claims C39–C41 sit on the ORIGINAL chart (Part10 H1.1/H1.2). The complete current union is the nineteen parts plus Part15 ADDENDUM-1 bound in `checkpoint-102-complete-current-v21-nineteen-part-manifest-v1.json` (SHA256 2b60176617cb71cb3041c6802029be6d4c0290e8e8ca4dd6963add467be4ce5f), THIS part, and all mandatory overlays. Parts 9–20 are LATER UNREVIEWED.

Imports:
- Part10 H1.1 chart, H1.2 coefficient matrix and H5 involution;
- Part15 Q6 (every R_x is entangled);
- Part13 (x=(1,1,1,1) is SN2), used only for the statement in B6.

No PPT⇒separable import is needed here.

**Principle (B-P).** Every vector of C^2⊗C^4 has Schmidt rank <=2. So every PSD operator supported on (a 2-dim Alice subspace)⊗C^4 lies in the SN<=2 cone, and sums of such operators stay in the cone. Part10's residual rule already used this for span{j,h}. Here it is used for two blocks with NONZERO cross-moments:
- Alice{0,3}: generators d, f, g, h;
- Alice{2,3}: generators e, f, g, j.

## B1. Coefficient calculus

Write Ψ=[a,b,c,d,e,f,g,h,j] for the generator list (with d=d_x, h=h_x) and D=diag(1,1,1,3,3,3,3,3,3), so R_x=Ψ D Ψ^†. For any finite family of coefficient vectors c with weights summing to one, writing E for the weighted average,

`R_x - E[P(Ψc)] = Ψ (D - E[c c^†]) Ψ^†.                                          (B1.1)`

This is an exact linear-algebra identity. For a coefficient vector (α,β,γ,δ,ε,φ,η,κ,λ) the matrix of Ψc (rows Alice, columns Bob) is H1.2:

```
[α+λu, β+λv, δ+λw, λz]
[γ,    α,    β,    0 ]
[ε,   -γ,    α,    κ ]
[δu+φ, δv,   δw+η, δz+ε]
```

## B2. The rigid product-plus-one family (fifth roots)

For r^5=1 take α=1, β=r, γ=-r̄, δ=r^2, ε=-z r^2, φ=0, η=v r^3-w r^2, κ=λ=0. The matrix is:

```
[ 1,       r,     r^2,   0 ]
[ -r̄,      1,     r,     0 ]
[ -z r^2,  r̄,     1,     0 ]
[ u r^2,   v r^2, v r^3, 0 ]
```

Columns 1 and 2 equal (r,1,r̄,v r^2)⊗(1,r) and column 3 is zero. So Ψc(r) = (r|0>+|1>+r̄|2>+v r^2|3>)⊗(|1>+r|2>) + (|0>-r̄|1>-z r^2|2>+u r^2|3>)⊗|0>, which has SR<=2.

The coefficient charges are 0, 1, -1, 2, 2 and {2,3}, so every needed difference k has 1<=|k|<=4 and E over fifth roots kills it. The nonzero moments are:
- E|α|^2 = E|β|^2 = E|γ|^2 = E|δ|^2 = 1;
- E|ε|^2 = |z|^2, E|η|^2 = |v|^2+|w|^2;
- E[δε̄] = -z̄, E[δη̄] = E[r^2(v̄ r̄^3 - w̄ r̄^2)] = -w̄, E[εη̄] = E[-z r^2(v̄ r̄^3 - w̄ r̄^2)] = z w̄.

All other cross-moments vanish; for example E[βγ̄]=-E[r^2]=0 and E[α η̄]=0. Hence K' := D - E[cc^†] has zero a, b, c rows and columns, and on the indices (d,e,f,g,h,j):
- K'_dd = 2, K'_ee = 3-|z|^2, K'_ff = 3, K'_gg = 3-|v|^2-|w|^2, K'_hh = 3, K'_jj = 3;
- K'_de = z̄, K'_dg = w̄, K'_eg = -z w̄.

All other entries are 0.

## B3. The mixed family (third roots) that carries the d–e coupling

Fix t>0, b0>0 and ν0>0. For θ,φ,ψ independent and uniform on the cube roots of unity (27 vectors), put A=t e^{iθ}, C=(z/t)e^{iθ}, B=b0 e^{iφ}, ν=ν0 e^{iψ}, and

`κ = A d + C e + νC f + (A^2/B) g + B h + (C/ν) j.`

By H1.2 its rows are:
- row0 = (Bu, Bv, A+Bw, Bz);
- row1 = 0;
- row2 = (C, 0, 0, C/ν);
- row3 = (Au+νC, Av, Aw+A^2/B, Az+C).

Since row3 = (A/B)row0 + ν·row2, the vector κ has SR<=2.

**Moments.**
- A C̄ = z̄ exactly, so the (d,e) moment is z̄.
- Every other off-diagonal moment carries a nontrivial factor e^{±i(θ-φ)}, e^{±iψ}, e^{2i(θ-φ)} or e^{2iψ}, and averages to 0. For example (g,h): A^2 B̄/B = t^2 e^{2iθ}e^{-2iφ}; (f,j): |C|^2 ν/ν̄ = |C|^2 e^{2iψ}.
- Diagonals: t^2 (d), |z|^2/t^2 (e), ν0^2|z|^2/t^2 (f), t^4/b0^2 (g), b0^2 (h), |z|^2/(t^2ν0^2) (j).

## B4. Theorem C39 (two-block remainder)

**C39.** Let x=(u,v,w,z) with u arbitrary. Suppose there are t, b0, ν0 >0 and g1, g2 >=0 with:
- (i) t^2<2, b0^2<=3, ν0^2|z|^2<=3t^2 and |z|^2<=3t^2ν0^2;
- (ii) E := 3-|z|^2-|z|^2/t^2 >= 0;
- (iii) (2-t^2)g1 >= |w|^2 and E g2 >= |z|^2|w|^2;
- (iv) g1+g2 <= 3-|v|^2-|w|^2-t^4/b0^2.

Then SN(R_x)=2. If z=0 the mixed family is omitted, (i)–(ii) drop, and the condition becomes 2g1>=|w|^2, g1<=3-|v|^2-|w|^2.

*Proof.* By (B1.1), R_x = E_r P(Ψc(r)) + E_{θφψ} P(κ) + Ψ K'' Ψ^†, where K''=K'-E[κκ^†] (κ read as a coefficient vector). By B2–B3, K'' has these entries:
- d: 2-t^2; e: E; f: 3-ν0^2|z|^2/t^2; g: 3-|v|^2-|w|^2-t^4/b0^2; h: 3-b0^2; j: 3-|z|^2/(t^2ν0^2);
- (d,g)=w̄, (e,g)=-z w̄, (d,e)=z̄-z̄=0, and all other off-diagonals 0.

Split K'' as:
- K_03 = [[2-t^2, w̄],[w, g1]] on (d,g), which is PSD by (iii);
- K_23 = [[E, -z w̄],[-z̄ w, g2]] on (e,g), which is PSD by (ii)–(iii);
- a nonnegative diagonal remainder on f, g, h, j: the g entry is (iv)'s slack, the others are (i).

Ψ K_03 Ψ^† is supported on Alice{0,3}⊗C^4 and Ψ K_23 Ψ^† on Alice{2,3}⊗C^4, so both are SN<=2 by (B-P). The diagonal remainder is a sum of P(f), P(g), P(h), P(j), which are products. Every term is therefore in the SN<=2 cone, so SN<=2, and Q6 gives SN>=2. ∎

## B5. Corollaries

**C40 (z=0 slice).** If z=0 and |v|^2+(3/2)|w|^2 <= 3, then SN(R_x)=2 for every u.

Take g1=|w|^2/2. This subsumes Part18 C36 (|v|^2+2|w|^2<=5/3) and Part15 Theorem E (|v|=|w|=t, t^2<=9/8): on the diagonal C40 gives t^2<=6/5. It also contains x0=(u,1,-1,0) (2.5<=3) and (u,v,0,0) with |v|^2<=3. Part19 C37 (the v=0 PPT-residual slab, e.g. (u,0,1,1)) is NOT subsumed, since its mechanism is different.

**C41 (far balanced ray).** R_(s,s,s,s) has SN=2 for 0<s^2<=4/5 and for s>=3/2.

*(a) s>=3/2.* By the involution R_(s,s,s,s) ~ R_(1,1,-1,ζ) with ζ=1/s, |ζ|^2<=4/9. Take t^2=2/5, b0^2=3, ν0=1:
- (i) 4/9<=6/5.
- (ii) E=3-(7/2)|ζ|^2 >= 3-14/9 = 13/9.
- (iii) g1=1/(8/5)=5/8 and g2=|ζ|^2/(3-(7/2)|ζ|^2) <= (4/9)/(13/9) = 4/13. The map Z↦Z/(3-3.5Z) is increasing on [0,6/7).
- (iv) 5/8+4/13 = 97/104 <= 3-1-1-(4/25)/3 = 71/75, because 97·75=7275 < 71·104=7384.

The f and j entries are 3-(5/2)|ζ|^2 >= 17/9 and the h entry is 0.

*(b) s^2=σ<=4/5, directly at x=(s,s,s,s).* Take t^2=7/10, b0^2=3, ν0=1:
- (i) σ<=21/10.
- (ii) E=3-(17/7)σ >= 3-68/35 = 37/35.
- (iii) g1=10σ/13 <= 8/13 and g2=σ^2/(3-17σ/7) <= (16/25)/(37/35) = 112/185.
- (iv) the g entry is 3-2σ-49/300 >= 7/5-49/300 = 371/300. We need 8/13+112/185 = 2936/2405 <= 371/300, and 2936·300=880800 < 371·2405=892255.

Both sides are monotone in σ (the left increases, the right decreases), so σ=4/5 is the worst case. The f and j entries are 3-10σ/7>=13/7. ∎

**Consequences for earlier method barriers.** For 0<|ζ|<1/(6√2), every coordinate peel of R_(1,1,-1,ζ) is entangled (Part15 C34.4, Part19 C38), and the same holds for R_(s,s,s,s) with s>6(1+√2) (Part16 C35). C41 shows that these points ARE SN2. Those barriers were method barriers only, as recorded, and Part16's "far ray resists" is now resolved in the SN2 direction for s>=3/2. Part14's s=2,3,5 are subsumed. cp097's first-order budget feasibility is confirmed by an exact construction.

## B6. Exact remaining gap, and status

- Far balanced ray: SN2 is now proved for s^2<=4/5 (C41b), s=1 (Part13) and s>=3/2 (C41a). The part of the ray NOT covered is exactly s in (2/√5,1)∪(1,3/2), a bounded gap with compact closure in (0,∞). The Part6 ball (s<=1/√2) lies inside C41b.
- Literal x=(1,1,1,1): SN2 by Part13. C39 does not reach it directly. At v=w=z=1, (i)–(ii) force t^2>=1/2, and then 1/(2-t^2) >= 2/3 and t^2/(2t^2-1) >= 2/3 on [1/2,2). So the left side of (iv) is at least 4/3, while its right side is at most 1.
- Not covered by C39–C41, for every u: (u,2,0,0), since |v|^2=4>3; (u,0,2,1), since the g entry is 3-4-t^4/b0^2<0; and (u,1,1,1), as just shown. Some of these points are covered by earlier parts, for instance by Part10 Theorem C for large |u|; no claim is made either way here.
- If R_x has SN3 anywhere on the chart, it must lie outside the union of Part6, Part10, Parts 13–15, 18–20. On the balanced ray that means inside the bounded gap.

**Original physics-3/P44 remains UNMET.** These are author-WRITTEN candidates pending fresh reconstruction. They are not formal/kernel/executable/triple/configured-family/human/cross-vendor/novelty acceptance, not a park and not a closeout.

**END OF COMPLETE CURRENT v22 PART20/20.**
