# SPR7 general boxes — zone words for Hurwitz weak numerators of degree six (J alternatives A and B)

Actual returned `/bin/date` BEFORE creation: **Sun Oct 25 22:23:31 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN STRUCTURAL CANDIDATE**, an additive companion to `general-n7-contact-zone-table-v1.md` (SHA256 `a05d332de4fac12f2416a4758c34f4e2fb380163e76fa7f17eb6313fadf4fce1`; not edited). A fresh gate is required.

Only symbolic sign/order reasoning and hand-counted compositions are used. There is no numeric instance, interpreter, calculator, eval, program, CAS, enumeration program, solver, replay or GO. All four owner written-exactness majors (erratum v1–v4) and all parent findings remain permanent, and probes receive zero credit.

## 0. Statement

Let K be as in the companion: an ORIGINAL independent monic degree-7 box, every member strictly Hurwitz, with varying intervals in both blocks. Let b be a weak common numerator that is Hurwitz of EXACT degree 6 with b(0)>0. Then:

1. **Cells.** b has six cells, with target quadrant q=0..5. They are `(0,x1)` C4, `(x1,y1)` C1, `(y1,x2)` C2, `(x2,y2)` C3, `(y2,x3)` C4 and `(x3,∞)` C1.
2. **Zones.** The companion's corner zones apply unchanged, with q=k−1 for a lead and q=k+1 for a lag. The C2 lag zone `(eU3,oU3)` now needs q=6, so it is IMPOSSIBLE. Eleven positions remain, forming the string `+ − + − + − + − + − +`:
   - position 1: C4 lead in cell 1;
   - positions 2/3: C1 lag/lead in cell 2;
   - positions 4/5: C2 lag/lead in cell 3;
   - positions 6/7: C3 lag/lead in cell 4;
   - positions 8/9: C4 lag/lead in cell 5;
   - positions 10/11: C1 lag `(oU2,eU3)` and C1 lead `(oL3,∞)` in cell 6.
3. **Alternative (A)** (eight positive nodes, no infinity mass) has exactly **13** admissible words: 18 alternating 8-subsets, minus the 5 that contain all of C1's positions {2,3,10,11}.
4. **Alternative (B)** (seven positive nodes and infinity mass μ∞>0) forces κ>0, so the FIRST and LAST nodes LAG. It has exactly **8** words: {2..8}, {4..10}, and the six sets from 2 to 10 with exactly one gap of 3.

No word is shown empty or realized. Weak b with b(0)=0 or imaginary-axis roots, and zero nodes, are not covered.

## 1. Cells

For Hurwitz b of degree 6 with b(0)>0: E_b(t) has degree 3 with E_b(0)>0 and negative leading coefficient, while O_b(t) has degree 2 with O_b(0)>0 and positive leading coefficient. Hermite–Biehler gives `x1<y1<x2<y2<x3`. The signs of (E_b,O_b) on the six intervals are (+,+), (−,+), (−,−), (+,−), (+,+) and (−,+), so the unique minimizers are C4, C1, C2, C3, C4 and C1. The quadrant index increases by one at each component root, giving q=0..5.

At a positive weak contact both components of b are nonzero, by the companion's §1 parity-variation argument; that argument uses only simple component roots. As ω→∞, φ_a−φ_b→7π/2−3π=π/2, and weak positivity keeps the continuous difference in [−π/2,π/2]. So the contact relation k=q±1 holds exactly as in the companion §2.

## 2. Zone assignment

Each companion zone keeps its interval and its corner index k: these depend only on the corners, not on b. Its forced cell index q=k∓1 is unchanged except that q must now lie in 0..5. Hence:

- (eU3,oU3), C2 lag, k=5, would need q=6: IMPOSSIBLE.
- (oL3,∞), C1 lead, k=6, gives q=5: cell 6, whose minimizer is C1, which is consistent.
- (oU2,eU3), C1 lag, k=4, gives q=5: cell 6, consistent.
- (0,eL1), C3 lead, and (oU3,∞), C3 lag, remain impossible.

Every other row lands in the same-numbered cell as in degree 7. In each middle cell, and also in cell 6, the lag zone lies below the lead zone, because oU2<oL3.

## 3. Alternation and the sign of κ

Let the nodes be t_1<…<t_m with weights μ_i>0 and minimizing members a_i. Write eta_i=1/∏_{j≠i}(t_i−t_j). Then sign(eta_i)=(−1)^{m−i}.

**(A), m=8.** This is exactly the companion's §3 argument. E_b has degree 3 and O_b degree 2, and they are coprime. The identity E_b g+O_b h≡0 holds because its degree is at most 5 and it vanishes at 8 nodes. It gives g=κO_b and h=−κE_b, so y_i=−κ eta_i/(μ_i ω_i): orientation alternates, and κ may have either sign.

**(B), m=7.** For every real c of degree ≤7, the annihilation is

Σ μ_i P_{a_i,c}(t_i)+μ∞·[s⁷]c=0.

Since [s⁷]c=−[t³]O_c, the odd part gives Σ v_i p(t_i)=μ∞[t³]p for every p of degree ≤3, where v_i=μ_i t_i O_{a_i}(t_i).

Write v_i=eta_i h(t_i) with deg h≤6. This is a bijection by Lagrange interpolation. The divided-difference identity Σ eta_i r(t_i)=[t⁶]r for deg r≤6 then gives:

- [t⁶]h=[t⁵]h=[t⁴]h=0, from p=1, t and t² taken IN THAT ORDER, so that each product hp has degree ≤6 when it is used;
- [t³]h=μ∞>0, from p=t³.

The even part gives μ_i E_{a_i}(t_i)=eta_i g(t_i) with deg g≤2. The contacts make E_b g+O_b h vanish at 7 nodes, and its degree is at most 5, so it vanishes identically. Coprimality then gives h=−κE_b and g=κO_b. Comparing leading coefficients, −κ·(lead E_b)=μ∞>0; since lead E_b<0, this gives **κ>0**.

Then y_i=−κ eta_i/(μ_i ω_i) has sign −(−1)^{7−i}. So node 1 lags, nodes alternate, and node 7 lags.

## 4. Counts

**(A).** Choose 8 of the 11 positions with odd consecutive gaps. Put a=p_1−1 and s=11−p_8, and write the gaps as 2h_i+1. Then a+s+2Σh_i=3. The case Σh=0 with a+s=3 gives 4 sets; the case Σh=1 with a+s=1 gives 7·2=14. Total: **18**.

**Corner bound.** A corner pairing with this b has degree ≤6, is ≥0 and has positive constant term b(0)a(0). So it has at most THREE positive double roots. C4 sits at {1,8,9}, C2 at {4,5} and C3 at {6,7}, so none of these can exceed the bound. C1 sits at {2,3,10,11}.

A set containing all four C1 positions has 11 last and 2,3 chosen. The chain from 3 to 10 must have an even number j of interior points, and 4+j+[1 chosen]=8. That forces j=4 with position 1 omitted: 5 compositions of 7 into five odd parts. **13 words remain.**

**(B).** We need 7 positions with odd gaps, p_1 and p_7 EVEN (both lag) and p_7≤10, so p_7−p_1∈{6,8}:

- p_7−p_1=6: {2..8} and {4..10}, 2 words;
- p_7−p_1=8, from 2 to 10 with exactly one gap of 3 among the six gaps: 6 words.

Total: **8**. None contains position 11, so none uses four C1 contacts; the bound of 3 allows all 8.

## 5. Scope and assurance

These are necessary zone/order conditions only. No word is excluded beyond the stated counts, decided or realized. Combined with the companion, every Hurwitz weak b with b(0)>0 and degree 6 or 7 in Theorem J's alternatives now has an explicit finite word list: 43 for degree 7, 13 for degree 6 under (A), and 8 under (B). Weak b with b(0)=0 or imaginary-axis roots, and zero nodes, are NOT covered.

The named ordinary inputs are Hermite–Biehler, the Kharitonov extremes and their band-endpoint roots, monotone Hurwitz phase, the weak-positive-real phase interval, Lagrange/divided-difference identities, coprimality and composition counting. Old theory.md Theorem J is historical ancestry; the alternation and sign of κ used here are derived above.

This is not formal, kernel, human, configured-family, cross-vendor, executable, novelty or publication acceptance. It is not a universal SPR7 verdict, a new GO, an edit of any frozen or shared source, a deadline reset or a round closeout.
