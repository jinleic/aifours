# SPR7 reciprocal source admission — exact contact-SQUARE factorization of the full Hurwitz/Bezout determinant

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 06:56:54 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN CONDITIONAL THEOREM CANDIDATE.** This identifies the algebraic source-admission walls of the ACTUAL nonpalindromic corner, not just a generic matrix criterion. No point, physical feasibility, word-set emptiness, universal SPR7 result or scientific GO is claimed.

All-variable exact symbolic proof only, including privately. No numeric/control instance, decimal gloss, calculator, scientific interpreter/eval/program/CAS, enumeration, solver, replay, CLI or nested agent. The withdrawn fifth-instance check and every consuming inference remain ZERO credit/no rerun/backconversion; all FIVE findings and prior histories permanent. The qualified future-only ACK SHA256 `80ea3c102fea58d9549d470039bdca85b4066eace6afb5163b51bc88b838cdad` preceded the new proofs. Frozen sources/reviews/gates unchanged.

## 0. Exact imports and an essential polynomial-type distinction

Use the COMPLETE v21 generic/source Bezout theorem (`reciprocal-three-by-three-Bezout-whole-box-admission-v21.md`,167LF, SHA256 `873160daacab5d87ee9e7bb3a3fb374fee286ecf28843a4bed48eef3f63983fd`) and COMPLETE v22 weak-positive/PSD/single-determinant theorem (`reciprocal-weak-positivity-PSD-and-single-determinant-admission-v22.md`). The actual global corner/target/zero setup is the COMPLETE v11 packet, SHA256 `6ce35ce58f8636a95aeddb3b3bbdcbda33a29facb18cdeb28d9b98f236c405b8`, with all its original v5/v9/v10+erratum interfaces retained.

**Important:** S(t) below is the original PHYSICAL corner pairing in t=omega^2, not the compact determinant R(v) of v11–v14. Their residual cubics are DIFFERENT polynomials and are not equated. The resultants use the actual EVEN/ODD source components, not the real target-pairing cubics. All type and coordinate distinctions are explicit.

Let a be the ACTUAL C2 monic septic corner, with constant1 and all six coefficients positive. Let B be the fixed strict Hurwitz palindromic target of the original weak-positive box. Write

`a(iomega)=E(t)+iomega O(t)`, `B(iomega)=E_B(t)+iomega O_B(t)`,

`S(t)=E(t)E_B(t)+t O(t)O_B(t)>=0 for EVERY t>=0`.

The degree7 polynomial S is monic and S(0)=1. Let alpha=A1>0, so E has leading coefficient -alpha and O leading coefficient -1. Let H be v21's ACTUAL C2 Bezout matrix.

Retain v11's strict target-component margins: S(y)>0 at EVERY positive zero y of O_B. These hold automatically in its full pal-contact construction and are NOT optional in the generic theorem below.

## 1. Three source-even roots and the fixed positive denominator resultant

By v22, a_epsilon=(a+epsilon B)/(1+epsilon) is strictly Hurwitz for EVERY symbolic epsilon>0. Its three source-even component roots are positive, simple and interlaced. As epsilon decreases to0, coefficient/root continuity gives THREE positive real roots e1,e2,e3 of E, counted with multiplicity. No root can escape to infinity because E's leading coefficient tends to -alpha!=0, and no root can reach0 because E(0)=1. Repetitions are retained, not excluded by a genericity shortcut.

Thus

`E(t)=-alpha product_(i=1)^3(t-e_i)`, `product e_i=1/alpha`.

Let y1<y2<y3 be the three positive odd-component roots of the STRICT target B. Its even component has signs (-,+,-) at those three points by the exact target HB order. Since S(y_j)=E(y_j)E_B(y_j)>0, E has the SAME respective signs there. In the standard resultant convention

`Res(F,G)=leading(F)^(degree G) product_(F-roots) G(root)`,

one therefore has

`D_B:=Res(E,O_B)=product_(j=1)^3 E(y_j)>0`. (DEN)

The identity follows because O_B is degree3 with leading -1 and the odd-degree swap sign cancels that leading sign. Its strict positivity follows from the TWO negative and ONE positive factors. Thus no source-even/target-odd collision is hidden in a denominator division.

## 2. Exact identity before factoring the contact polynomial

First,

`det H=Res(E,O)`. (RES)

For completeness, with P=-O monic and Q=-E, the v21 Vandermonde diagonal formula gives det H=-Res(P,Q) on the distinct-P-root locus; degree3 swap and scalar signs give -Res(P,Q)=Res(E,O). Both sides are polynomial in the original coefficients, so this identity holds identically, including repeated/common-root cases. No numeric test is used to establish the polynomial identity.

At EVERY source-even root e_i, counted with multiplicity,

`S(e_i)=e_i O(e_i)O_B(e_i)`.

The resultant product formulas and product e_i=1/alpha give

`product_i S(e_i)=det H * D_B / alpha^7`.

Hence the exact identity

`det H * D_B=alpha^7 product_i S(e_i)`. (MASTER)

This is an algebraic identity of the actual source/target components. It remains valid when det H=0 or E has repeated roots. The positive source-even roots are used only to infer signs, not to derive the identity by numerical factorization.

## 3. TWO physical nonpalindromic contacts — selected amplitudes are SQUARED factors

Suppose p,q>0 are two DISTINCT physical C2 pairing contacts, so S has at least their double factors. In W_II these are its two below-one C2 contacts. In W_III one is the below-one C2 contact and the other is the reciprocal above-one C2 image of the below-one C4 contact.

Write the EXACT physical factorization

`S(t)=(t-p)^2(t-q)^2 Q_phys(t)`,

where Q_phys is monic cubic with Q_phys(0)=1/(p^2q^2)>0 and Q_phys>=0 on[0,infinity). This follows from S>=0 and continuity after division; it is NOT the v-variable cubic from v12.

Substitute into(MASTER). Since E(p)^2=alpha^2 product_i(e_i-p)^2, and likewise at q,

`det H * D_B`

`=alpha^3 E(p)^2 E(q)^2 product_i Q_phys(e_i)`

`=-E(p)^2 E(q)^2 Res(E,Q_phys)`. (TWO)

The scalar denominator D_B is STRICTLY positive, and -Res(E,Q_phys)=alpha^3 product_i Q_phys(e_i)>=0 because every e_i>0. Thus the selected physical source-even values enter the FULL admission determinant as exact SQUARE factors. They are not merely local approximate wall indicators.

At a selected weak contact with BOTH target components nonzero, a/B=i*y implies

`E(p)=-y_p sqrt(p) O_B(p)`.

Therefore E(p)=0 IFF its actual contact amplitude y_p (equivalently the appropriately defined compact kappa) is0; the same holds at q. A physical contact at t=1 is absent in the strict reciprocal construction, so no u=0 amplitude division occurs.

Consequently the complete actual nonpalindromic strict-Hurwitz admission is EXACTLY

`E(p)!=0`, `E(q)!=0`, `Res(E,Q_phys)<0`. (ADM2)

This uses v22's equivalence det H>0, not an assumed source-stability conclusion. The selected lead/lag signs still strengthen these two nonvanishing checks and remain mandatory for the positive dual.

### 3a. The residual source wall, exhaustively

If Q_phys is STRICTLY positive on the positive half-line, then its resultant factor is automatically strictly negative. In that case selected nonzero amplitudes alone imply the complete nonpalindromic source admission; there is NO additional hidden imaginary-zero test.

If Q_phys has a positive zero h, it is its ONLY positive zero and is double (or is coincident with a selected root, increasing that root's multiplicity). Then Res(E,Q_phys)=0 IFF E(h)=0. Since S(h)=0 and the target-component margins exclude O_B(h)=0, the latter implies O(h)=0 as well. Thus the residual resultant wall is EXACTLY the extra source amplitude-zero wall, not every extra contact.

An extra contact with E(h)!=0 is admissible and may have a nonzero lead/lag sense; no boundary is discarded. This matches the exhaustive zero accounting of v12/v14 after the exact t↔v/reversal correspondence, while keeping the DIFFERENT cubic polynomials distinct.

## 4. THREE physical C2 contacts — W_I's entire nonpal admission is a positive multiplier times THREE squares

For W_I, its two selected below-one C2 contacts and the reciprocal of its selected C4 contact are THREE DISTINCT physical C2 pairing roots p,q,w. Degree7 and nonnegativity force

`S(t)=(t-p)^2(t-q)^2(t-w)^2(t+beta)`,

`beta=1/(p^2 q^2 w^2)>0`.

No additional positive physical C2 root is possible. Substituting into(MASTER) gives

`det H * D_B=E(-beta) E(p)^2 E(q)^2 E(w)^2`. (THREE)

Indeed E(-beta)=alpha product_i(e_i+beta)>0; the six squared factors contribute alpha^-6 and(MASTER) alpha^7. Because ALL actual source coefficients are positive, E(-beta)>0 also follows directly from its alternating-sign form at a negative argument.

Thus W_I's NONPAL source-Hurwitz determinant is positive IFF the three selected physical source amplitudes are nonzero. There is no unselected nonpal pairing root to be checked. This does NOT waive a possible unselected palindromic C1 contact: its separate pal source strictness/nonzero-amplitude conditions remain part of the actual original-box admission. The theorem is about the actual C2/C4 part, not every corner by fiat.

## 5. Exact physical meaning and remaining task

The scalar determinants in v21/v22 are now factored into:

- a fixed STRICT positive target/source-component resultant denominator;
- SQUARES of each selected actual physical corner amplitude, via E at its contact;
- a residual resultant that vanishes precisely at the only possible extra source-zero contact, or a strictly positive multiplier when the physical residual has no positive zero.

This is an exact global algebraic identification of the actual source-admission faces, including multiplicities, not a numerical stability observation. It also explains why a generic strict determinant or positive diagonal cannot replace an explicit contact/amplitude proof without the global weak-positive hypotheses.

What remains is to solve or exclude the FULL original width/height/contact/factor/selected-orientation equations. The new square identity does NOT show any square factor must vanish, nor furnish a point where they are all nonzero. W_I, W_II_strict and W_III physical feasibility and original universal SPR7 remain OPEN. No genericity, approximate source stability, rational tuple or executed finite certificate is claimed.

This later v21-v23 chain is outside the pre-event v11-v20 intake manifest unless a parent freezes a NEW complete union prospectively. It requires full source/application reconstruction at its stated ordinary algebra/HB/minimum-principle interfaces. No formal/kernel/human/configured-family/cross-vendor/executable/triple-finite/novelty or parent acceptance, new GO, source cutover, nineteenth owner, deadline reset or round closeout. Same original18/HOLD/science cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 and actual-clock substantive cadence; research remains active.
