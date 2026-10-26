# SPR7 reciprocal class — exact reduction to three explicit five-dimensional word sets

Actual returned `/bin/date` BEFORE creation: **Sun Oct 25 21:42:13 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN CONDITIONAL REDUCTION**, requiring a fresh complete gate. Only symbolic variables and exact polynomial/sign reasoning were used. No numeric parameter trial, approximate gloss, calculator, interpreter, eval, program, CAS, LP, enumeration, root checker, optimizer, solver, replay, CLI or nested agent was used.

All three of my own written-exactness majors remain permanent, together with the earlier eval/pre-return finding and every parent, author and reviewer history. Approximate or colliding scouts receive ZERO credit and are not used. The bounded generic-integer illustration disclosed in checkpoint-v59 and v9 is not used here. Checkpoint-v66 additively withdrew a misleading v65 state label; no exclusion of any strict-cubic word is claimed. HOLD, v9/v10/v11, later overlays and the original October 27 cutoff/deadline remain.

## 0. Result and exact scope

The INPUT class is the ORIGINAL independent monic septic box with `A7=1`. The pairs (A1,A6), (A2,A5) and (A3,A4) range independently over the SAME intervals `[α_i,β_i]` with `α_i<β_i`. Every member is assumed strictly Hurwitz. Members are NOT individually palindromic. This is an explicit input subclass, not the general problem.

**Theorem (sufficiency, unconditional at its stated hypotheses).** §4 defines three explicit semialgebraic sets `W_I, W_II, W_III` of pairs (palindromic strict-cubic target B, reciprocal box). Any point of their union yields a robustly Hurwitz reciprocal box that has NO unrestricted real exact-degree-7 common SPR numerator. It can then be enlarged to an original box with rational endpoints and all SEVEN widths positive that is still a counterexample.

**Theorem (conditional necessity).** Assume the NEW 341LF first-critical interface `reciprocal-critical-cone-entire-inverse-and-positive-kernel-v5.md`, SHA256 `7a358b729dfff820eb18d8af9bd474e83592979f4a045ea212a09237bda7f70a`, and the NEW 255LF weak-quadratic transfer theorem `reciprocal-weak-quadratic-strict-transfer-entire-v9.md`, SHA256 `34d12a551f4255f9c647d1c643af3baae5fff805417896124b511e87723cc435`. Under those two named, still-unaccepted imports, every negative reciprocal box yields a point of the union.

Hence, conditional on those imports, **reciprocal-class SPR7 synthesis holds iff `W_I ∪ W_II ∪ W_III` is empty.** Each `W_k` is cut out in five-dimensional contact-shape coordinates. `W_I` has an equation-free chart. **Neither emptiness nor a point is supplied here.** This is the exact final finite-dimensional form of the reciprocal question; it is not an answer to it.

Two contributions are NEW in this source:

- a complete band-orientation proof that strict-cubic critical support has EXACTLY three words, independent of the earlier width argument;
- the box-from-C2 parametrization, which shows that the whole configuration is determined by (B, P2), with an automatic consistency lemma.

All operative proofs are given below. No earlier hash, checkpoint or headline is used as proof.

## 1. The whole box is determined by its C2 corner

Write `E_a(t)=-A1t³+A3t²-A5t+1` and `O_a(t)=-t³+A2t²-A4t+A6`, with t=ω². For t>0 the attained actual extremes are

`Eplus=-α1t³+β3t²-α2t+1`, `Eminus=-β1t³+α3t²-β2t+1`,

`Oplus=-t³+β2t²-α3t+β1`, `Ominus=-t³+α2t²-β3t+α1`.

These follow by choosing each independent coefficient at the relevant endpoint. The four ACTUAL corners, written as coefficient lists (A1..A6), are

`C1=(Eplus,Ominus)=(α1,α2,β3,β3,α2,α1)`,

`C2=(Eplus,Oplus)=(α1,β2,β3,α3,α2,β1)`,

`C3=(Eminus,Oplus)=(β1,β2,α3,α3,β2,β1)`,

`C4=(Eminus,Ominus)=(β1,α2,α3,β3,β2,α1)`.

Thus C1 and C3 are palindromic, and C4 is the reversal R(C2) with `Ra=s^7a(1/s)`. In the other direction, the C2 coefficient list (A1,...,A6) recovers every interval: `[α1,β1]=[A1,A6]`, `[α2,β2]=[A5,A2]`, `[α3,β3]=[A4,A3]`. Positive widths are `A6>A1`, `A2>A5`, `A3>A4`.

Reciprocity holds exactly:

`Eplus(t)=-t³Ominus(1/t)`, `Eminus(t)=-t³Oplus(1/t)`.

Direct substitution checks both. Let the actual root bands be `I_Ej=[eL_j,eU_j]` and `I_Oj=[oL_j,oU_j]`, strictly alternating. Since Eplus≥E_a≥Eminus for t>0, the root lists are

- Eplus: (eU1, eL2, eU3);
- Eminus: (eL1, eU2, eL3);
- Oplus: (oU1, oL2, oU3);
- Ominus: (oL1, oU2, oL3).

Each comes from comparing an extreme with members on its positive and negative stretches. Reciprocity then gives `I_Ej=1/I_O(4-j)`. In particular `eU2=1/oL2<oL2`, so oL2>1. Therefore **I_E1, I_O1 and I_E2 lie in (0,1), while I_O2, I_E3 and I_O3 lie in (1,∞).**

## 2. Palindromic strict-cubic target: cells and pairing calculus

Let `B=(s+1)s³T(s+1/s)` with `T=z³+dz²+ez+f` strictly Hurwitz (d,e,f>0, de>f). Then B is monic of degree 7, B(0)=1, and B is strictly Hurwitz by the root map `Re z=Re s(1+|s|^-2)`. Its components obey

`E_B(t)=-t³O_B(1/t)`.

Hermite–Biehler gives E_B roots x1<x2<x3 and O_B roots y_i=1/x_(4-i) with

`x1<y1<x2<1<y2<x3<y3`, i.e. `x1x3<1`, `x2<1<x2x3`.

On (0,1) the signs give four cells, each with its UNIQUE minimizing corner:

- `(0,x1)`: E_B>0, O_B>0, corner C4;
- `(x1,y1)`: E_B<0, O_B>0, corner C1;
- `(y1,x2)`: E_B<0, O_B<0, corner C2;
- `(x2,1)`: E_B>0, O_B<0, corner C3.

The cells above 1 are the reciprocals: C3 on (1,y2), C4 on (y2,x3), C1 on (x3,y3), C2 on (y3,∞).

Let `P_j=E_(a_j)E_B+tO_(a_j)O_B` be the four pairings. Each is monic of degree 7 with `P_j(0)=1`. With `ΔE=Eplus-Eminus=2t(w1t²+w3t+w2)` and `ΔO=Oplus-Ominus=2(w2t²+w3t+w1)`, where `w_i=(β_i-α_i)/2>0`:

`P2-P3=ΔE·E_B`, `P3-P4=tΔO·O_B`, `P2-P1=tΔO·O_B`,

`P1+P3=P2+P4`, `P4(t)=t^7P2(1/t)`.

P1 and P3 are palindromic, since C1, C3 and B are reversal-invariant and `P_(Ra,B)(t)=t^7P_(a,RB)(1/t)`. The three difference identities show that **each P_j≥0 needs checking only on its own cells.** For example, P3 exceeds P2 where E_B<0 and exceeds P4 where O_B>0. The union of those sets is the complement of C3's cells [x2,y2]. The same argument applies to the other corners.

**Determination lemma.** Given B, the map from the six free coefficients of a to the six free coefficients of P_(a,B) is bijective because E_B and O_B are coprime. So (B,P2) determines C2 and therefore, by §1, the whole box. Conversely, let P2 and P3 be pairings in which P3 is palindromic and `P2-P3=G·E_B` with G of degree at most 3 and G(0)=0. Then G is the actual ΔE of the box built from P2. Proof: any palindromic polynomial of the form `G'E_B` with G'(0)=0 satisfies `-t⁴G'(1/t)O_B=G'E_B`. Coprimality forces E_B to divide `t⁴G'(1/t)`, which has degree at most 3 and zero constant term, so G'=0. Hence no hidden consistency equation remains.

## 3. Orientation calculus and the EXACTLY-three-word theorem

At a positive weak contact of corner a, write `a(iω)/B(iω)=iy` with y real and nonzero. Then

`y=ωO_a/E_B=-E_a/(ωO_B)`.

So y>0 means a LEADS B by π/2. For each contact, the signs of E_a and O_a are fixed by the cell and by sign(y).

**Positive kernel iff alternation.** Take four distinct finite contacts in compact coordinates. Write `D=A+iC` with `a=(s+1)s³D` and `Bval=uC`, u=ω-1/ω. Contact means `(f-dV)A+(e-V)Bval=0`, V=u². Any annihilation of the four vectors `δ³(-V Bval,-V A,Bval,A)` has weighted `A_j=η_j(αV_j+β')` and weighted `Bval_j=η_j(γV_j+ε)`, where `η_j=1/∏_(k≠j)(V_j-V_k)`. The contact equations make a polynomial of degree at most 2 vanish at four points. Coefficient comparison together with de-f>0 then gives a ONE-dimensional kernel. Since `(A_j,Bval_j)=κ_j(V_j-e,f-dV_j)` with `κ_j=y_ju_j`, the unique weights are `λ_j=α'η_j/(δ_j³κ_j)`. The η_j alternate, so **positive weights exist iff sign(y_j) alternates in frequency order.**

**Phase rule.** For actual Hurwitz members, the unwrapped arg(a/B) is continuous on [0,∞), starts at 0 and stays in [-π/2,π/2] by weak positivity. At a contact it equals exactly ±π/2. In the C4 cell the target phase lies in (0,π/2). A lag there would make the member's phase negative, so **every C4 contact below 1 leads.**

**Band locations by orientation.** These follow from §1's root lists, restricted to (0,1):

- C2 lag requires Eplus<0 and Oplus>0, which places it in `(eU1,oU1)`.
- C2 lead requires Eplus>0 and Oplus<0, which places it in `(eL2,1)`.
- C4 lead places it in `(eL1,oL1)`.
- C1 lead places it in `(oL1,eL2)`; C1 lag places it in `(0,eU1)`.
- C3 lag requires Eminus<0 and Oplus<0, which places it in `(oU1,eU2)`. C3 lead would require Eminus>0 and Oplus>0, i.e. `(0,eL1)` below 1. In every surviving word, C3 is the LAST selected contact and alternation forces it to lag, so the lead case is never used.

**Counting.** Every orbit is represented in (0,1); there are no ω=1 contacts, by the 341LF interface. C2 contacts above 1 reflect to C4 contacts below 1. Distinct contacts in one cell are consecutive in the full selected sequence.

- All C4 contacts lead, so alternation allows at most ONE.
- C2 lags lie strictly below C2 leads (oU1<eL2), so at most ONE lag followed by ONE lead.
- C1 and C3 have at most one contact each, by the nonnegative monic cubic real form.

Four orbits are required: at most three is impossible, as shown in 341LF §4; the endpoint is never a contact because B·(64,0,0,0)=64>0. The multiplicities (C4,C1,C2,C3) summing to 4 are (1,0,2,1), (0,1,2,1), (1,1,1,1) and (1,1,2,0). The last forces the pattern C4 lead, C1 lag, then C2 lead before C2 lag, which contradicts C2 lag-before-lead. Hence EXACTLY:

- **Word I:** C4@d0 lead, C2@r lag, C2@s lead, C3@c lag. Order: `eL1<d0<min(x1,oL1)`, `max(eU1,y1)<r<oU1<eL2<s<x2<c<eU2<1`.
- **Word II:** C1@g lead, C2@r lag, C2@s lead, C3@c lag. Order: `max(x1,oL1)<g<y1<r<oU1<eL2<s<x2<c<eU2`, with eU1<r.
- **Word III:** C4@d0 lead, C1@g lag, C2@r lead, C3@c lag. Order: `eL1<d0<x1<g<min(y1,eU1)`, `max(y1,eL2)<r<x2<c<eU2`.

This proves the three-word classification by band orientation alone. It is consistent with, but independent of, the earlier width/unwrapped-index argument.

## 4. The three word sets and their charts

`W_k` is the set of pairs (B, reciprocal box with positive widths) such that:

1. B is a strict-cubic palindromic target as in §2.
2. Every corner pairing is ≥0 on its own cells.
3. Word k's four contacts are double roots in the stated cells, with the stated orientations.
4. Every corner is nonzero at every positive zero of its own pairing.
5. The minimum pairing is >0 at each of x_i and y_i.

**Equation-free chart for W_I.** Choose `0<r<s<1<w` and `0<c<1`, together with h>0. Put

`P2=(t-r)²(t-s)²(t-w)²(t+β)`, `β=(rsw)^-2`,

`P3=(1+t)H_c(t)²((t-1)²+ht)`, `H_c=t²-(c+1/c)t+1`.

These are exactly the forced forms: P2 is monic of degree 7 with constant 1 and three double roots (d0=1/w), and P3 is palindromic with real form `(V-V_c)²(V+h)`. Let `F=(P2-P3)/t` (degree at most 5).

Require that F factor as E_B·Δrev, where:

- E_B has positive roots x1<x2<x3 satisfying the §2 interlacing;
- E_B(0)=1;
- Δrev is a quadratic with positive coefficients.

B is then determined by E_B. The box is determined by (B,P2) through the determination lemma, and its widths are exactly Δrev/2. Consistency is automatic. The remaining conditions are the cell/orientation chain of §3, P1≥0 on (x1,y1), and conditions 4–5.

Several sign facts are automatic and are recorded as consistency, not filters. F>0 at d0 and at c, F<0 at r, s and w, and F(1/c)≥0. Hence `x1∈(d0,r)`, `x2∈(s,c)` and `x3∈[1/c,w)` are forced. The coefficient conditions are F(0)=2w2>0 and a negative leading coefficient -2Aw1, where A=1/(x1x2x3).

**Charts for W_II and W_III.**

- W_II: take `P1=(1+t)H_g²((t-1)²+h1t)`, `P3=(1+t)H_c²((t-1)²+h3t)` and B. Widths are fixed by the three palindromic coefficients of `P1-P3=t(ΔrevE_B-ΔO O_B)`. P2 is then fixed, and TWO equations remain: double roots at r and s.
- W_III: the same, with double roots at r and w=1/d0.

Each set is five-dimensional in these coordinates. No point of any W_k is exhibited.

## 5. Sufficiency: any point is a genuine counterexample

At a point of W_k, the four contacts give a positive annihilation of the compact target vectors by §3. Each finite functional applied to the palindromic projection `(B'+RB')/2` of an ARBITRARY real degree-7 target B' splits into two ACTUAL atoms: (a_j,t_j) and (Ra_j,1/t_j). This uses `P_(a,RB')(t)=t^7P_(Ra,B')(1/t)`, and the box is reversal-invariant. A strict common B' would give positive values on all eight atoms, which contradicts the annihilation. So no common numerator exists.

**Admission.** For any member a, a(0)=1. The function a/B is analytic on the closed right half-plane, tends to 1 at ∞, and has boundary real part `P_(a,B)/|B|²≥min_jP_j≥0`. The minimum principle gives Re(a/B)>0 inside, so there are no right-half-plane roots.

Suppose a(iω0)=0 with t0=ω0². Then the minimum pairing vanishes at t0, and by condition 5, t0 lies inside a cell. There the functional `(E,O)↦E·E_B+tO·O_B` has two nonzero coefficients, so it attains its minimum at the UNIQUE corner. The member's values therefore equal that corner's, and the corner vanishes, which contradicts condition 4. Hence the whole box is strictly Hurwitz. This is proved without samples or an opaque Routh test.

**Rational all-width enlargement.** The box is compact inside the open Hurwitz set. Enlarge every endpoint slightly to rational values and give A7 a small interval around 1, keeping all members Hurwitz. Containment preserves the obstruction. This is a conditional transfer; no epsilon is evaluated.

## 6. Conditional necessity

Let K be a negative reciprocal box. Contract widths about the same palindromic center (the class is preserved). The 341LF interface yields a first-critical box K* with:

- a weak palindromic B;
- strict cubic or quadratic T;
- exactly four positive-weight orbits;
- all members Hurwitz.

v9 shows that a weak quadratic B forces a strict common numerator on K*, contradicting first failure, so T is strict cubic. The contacts lie in open cells, since at a weak contact both B components are nonzero (341LF). Section 3 then places the configuration in exactly one W_k. Robust Hurwitz stability gives conditions 4 and 5. **This necessity is only as strong as the unreconstructed 341LF and v9.**

## 7. Exact residual and assurance

What remains open:

- Emptiness, or a point, of `W_I ∪ W_II ∪ W_III`. No uniform contradiction and no admissible point is known here.
- General nonreciprocal boxes, arbitrary bad-infimum attainment and the universal SPR7 problem.
- A future emptiness certificate would have to cover all five-dimensional strict inequalities. A future point would give a genuine counterexample by §5.

The adopted independent double-endpoint v3/v4 results, older profile packets and the 175/188/225/143/306LF reciprocal candidates keep their own scopes. None is a premise here; bytes are unchanged. Named ordinary imports are:

- degree-specific Hermite–Biehler and the root map;
- monotone unwrapped phase of Hurwitz polynomials and the weak positive-real minimum principle;
- coprimality, Lagrange and Vandermonde algebra;
- finite-dimensional compact separation;
- actual independent coefficient rectangles.

Every model-specific identity, classification step and lemma is written out above.

This is NOT formal, kernel, human, configured-family, cross-vendor, executable, triple-finite, novelty, SOTA or publication acceptance. It is not a universal SPR7 or reciprocal-class verdict, and it is not a new GO. There was no source/shared/Git/deletion/config edit, no deadline reset and no round closeout. Every process finding and ZERO-probe credit remains.
