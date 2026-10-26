# Checkpoint 001 — a strictly stronger angular obstruction from the complete two-dimensional principal form

Before-creation clock observed: **2026-10-23T13:58:37-07:00**. Retained slot: physics-1. Status: **CANDIDATE written derivation**, pending distinct reconstruction. No scientific execution occurred after the ownership cutover, and no pending open-region result is used as an accepted premise.

## 1. Actual delta and exact scope

For the two-equal-pairs family `eta_t=|00>+|11>+t|22>+t|33>`, put s=t^2>=0. The legacy fixed co-Choi test vector w=p2+2q2 supplied a necessary cubic inequality. Here the **whole quadratic form on span{p2,q2}** gives the stronger necessary condition

**`Q(s)=112s^4+316s^3+331s^2+96s-9>=0`.**

The condition is necessary for symmetric domination `-C_B<=S_eta<=C_B`, not sufficient for the full256-dimensional matrices. Its positive zero is strictly larger than the positive zero of the old fixed-vector cubic. Thus this is not merely a rewording of the already written-checked obstruction.

At the exact rational value **s=147/2000**, the old fixed-vector form is positive while this principal form is indefinite. This proves that checking only the old cubic can miss a genuine co-Choi failure. The resulting negative vector still has coefficient rank four and is **not** a rank-two Werner witness. Unrestricted W4 and the full angular classification remain open.

## 2. Definitions and inherited physical contractions

Use the same co-Choi convention and reference map as the new slot's selection. References may be unnormalized because M_eta is scale invariant. The legacy angle packet `proof-reference-angle-obstructions-v1.md`, SHA `ccb579da080fcfba43c44dafbb7aa8511f989d33696c36193736ec5105abde84`, has been independently written-checked at its complete raw inverse. Its p2,q2 contractions are the starting identities, not finite sample values:

`p2=|0000>+|0011>+|1100>+|1111>`,

`q2=|0000>+|0110>+|1001>+|1111>`.

For t=u and s=t^2 set

`a=1+2s`, `b=2+s`, `z=2/a+2s/b`,

`F(s)=12a(1+s)^2>0`.

The retained full inverse gives

`<p2,S p2>=[z+(16+2z)/a-4/a^2]/(4+z)`,

`<p2,S q2>=[z/2-(4+2z)/a-2/a^2]/(4+z)`,

`<q2,S q2>=[z-(8+z)/a-4/a^2]/(4+z)`.

The C_B form on the same basis is `[[3,-3/2],[-3/2,3]]`. These are **quadratic-form matrices** in a linearly independent, nonorthogonal basis; positive semidefiniteness/indefiniteness under this congruence is the intended test. No ordinary eigenvalue of a nonorthogonal action matrix is being used.

The four-dimensional reference inverse is retained even though p2,q2 use only labels0,1. In particular z contains both outside Schmidt coefficients; this is not a two-level truncation.

## 3. Explicit complete principal matrix

Because

`z=4(1+s+s^2)/(ab)`, `4+z=12(1+s)^2/(ab)`,

the three S form entries have common denominator F(s), with numerators

`N_pp=8s^3+52s^2+96s+36`,

`N_pq=4s^3-10s^2-24s-18`,

`N_qq=8s^3-8s^2-36s-24`.

For example the pp numerator before dividing out the common inverse denominator is

`4(1+s+s^2)(a+2)+16ab-4b`,

which expands to the stated N_pp. The cross numerator is `2(1+s+s^2)(a-4)-4ab-2b`; the qq numerator is `4(1+s+s^2)(a-1)-8ab-4b`. Expanding them gives N_pq,N_qq exactly.

Adding the C_B form yields

**`Form(C_B+S_eta)|_(p2,q2)=(4/F(s)) [[2A(s),-B(s)],[-B(s),D(s)]]`,**

where

`A(s)=9+30s+29s^2+10s^3`,

`B(s)=9+24s+25s^2+8s^3`,

`D(s)=3+27s+43s^2+20s^3`.

All A,B,D are positive for s>=0. Hence this principal form is PSD if and only if `2A(s)D(s)-B(s)^2>=0`.

## 4. Exact quartic factorization

A coefficientwise multiplication gives

`A D=27+333s+1284s^2+2283s^3+2117s^4+1010s^5+200s^6`,

`B^2=81+432s+1026s^2+1344s^3+1009s^4+400s^5+64s^6`.

Therefore

`2AD-B^2=-27+234s+1542s^2+3222s^3+3225s^4+1620s^5+336s^6`

`         =3(1+s)^2[112s^4+316s^3+331s^2+96s-9]`.

Since the positive prefactor cannot change sign, the principal PSD condition is exactly Q(s)>=0. The polynomial Q is strictly increasing for s>=0 because

`Q'(s)=448s^3+948s^2+662s+96>0`.

Its value at zero is negative and it tends to infinity, so it has exactly one positive zero. This is an exact principal-block threshold, not a numerical estimate and not a full GS theorem.

## 5. Strict improvement over the old fixed-vector cubic

The old test w=p2+2q2 evaluates to

`(2/3)P(s)/[(1+2s)(1+s)^2]`,

`P(s)=34s^3+65s^2+36s-3`.

P is strictly increasing for s>=0 and has one positive zero s_w. At s=s_w, w has quadratic value zero. However the first coordinate of the principal matrix applied to (1,2) is proportional to

`2A(s)-2B(s)=4s(s^2+2s+3)>0` for s>0.

Thus this zero vector is **not in the principal matrix kernel**. A PSD Hermitian matrix cannot have a zero quadratic vector outside its kernel. Consequently the principal matrix is indefinite at s_w, Q(s_w)<0, and the positive zero of Q lies strictly beyond s_w. This proves the strict necessary-condition improvement without approximating either zero.

A fully exact separating value is s=147/2000. Written integer arithmetic gives

`P(147/2000)=85171782/8000000000>0`,

`Q(147/2000)=-433823189328/16000000000000<0`.

For transparency, `147^2=21609`, `147^3=3176523`, `147^4=466948881`; substituting these powers gives both numerators directly. No parameter loop, symbolic engine or executable arithmetic was used.

## 6. Exact negative co-Choi vector at the separating value

For any s with Q(s)<0, choose

`v_s=[B(s)/(2A(s))]p2+q2`.

The coefficient of p2 in the first row cancels exactly. Its quadratic value is

`<v_s,(C_B+S_eta)v_s>=(4/F(s))[D(s)-B(s)^2/(2A(s))]`

`                       =2[2A(s)D(s)-B(s)^2]/[A(s)F(s)]<0`.

At s=147/2000, t=sqrt(147/2000) is a specified positive algebraic number. A,B,D and the vector coefficient are rational functions at a rational input, so this is an exact algebraic reference and exact rational co-Choi negative value, given without floating recognition.

Across the input:output partition, v_s has coefficient matrix

`[B(s)/(2A(s))]|Omega2><Omega2|+F_2`.

Its eigenvalues are `1+B(s)/A(s)` on Omega2,1 on the two-dimensional symmetric-orthogonal subspace and-1 on the antisymmetric line. All are nonzero for s>=0. Its rank is four. This rules out an erroneous promotion to a rank-two Werner witness.

## 7. Exact blocker and next bounded action

The current remaining obstruction is precise: the principal two-dimensional form does not determine positivity on its coupling to the other invariant Bell-pair directions, nor on the nontrivial representation sectors. The correlated U(2)×U(2) action leaves an eight-dimensional invariant subspace spanned by the two p/q pairings within each equal-Schmidt group and the four mixed-group pairings. The next bounded written action is to derive its **full** matrix with the correct Gram metric and then account for the complementary sectors; one cannot simply assert the new quartic is sufficient.

This checkpoint gives a genuine strengthened necessary angular boundary and a separating exact counterexample to the weaker fixed-vector test. It does not finish the global reference criterion, does not accept the still-pending open-region packet, and does not solve unrestricted W4. No new scientific GO exists; legacy sources and sibling slots remain unchanged.
