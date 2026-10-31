# General sharp scale-free mixing criterion for a middle even-root spread

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:16:18 PDT 2026**. **WRITTEN universal necessary theorem candidate**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. It generalizes the numerical sharp threshold and genuine seven-width example in `frontier-20261029-shared-odd-root-sharp-width-v1.md`, SHA-256 `3cc332f1bd711be0a4d153ebdf42bbea44930e082795823b9366a74fe14c87d4`.

## 1. Statement

Let \(K\) be any bounded closed independent monic septic coefficient box, all of whose members are strictly Hurwitz. Suppose its even-component projection contains
\[
E_b(t)=-L(t-a)(t-b)(t-c),\quad E_d(t)=-H(t-a)(t-d)(t-c),\qquad 0<a<b<d<c,\quad L,H>0. \tag{1}
\]
The two even parts may come from different actual members. Let \(T\in(d,c)\) be the second odd root of **any** actual member; its odd part need not be the odd part of either source member. Define
\[
S_d=ac+(a+c)d,\quad Q_d=a+c+d,\quad C=a^2+ac+c^2,\quad
E=(T-a)(T-b)(c-T)>0. \tag{2}
\]
Then necessarily
\[
E>(d-b)C\min\left\{\frac{T^2}{S_d},\frac{T}{Q_d}\right\}. \tag{3}
\]
Equivalently, at least one of the following two **linear inequalities in \(d\)** must hold:
\[
E S_d>(d-b)CT^2,\qquad E Q_d>(d-b)CT. \tag{4}
\]
If both fail, **no** choice of positive scales \(L,H\) can occur in any all-Hurwitz independent coefficient box with this odd-root condition. Conversely, when (3) holds there are positive scales for which all 16 independently mixed even parts are strictly positive at this one odd-root frequency. This converse is only a single-frequency coefficient-mixing statement, **not** a full stability or common-numerator theorem.

The independence of coefficient coordinates is used twice: all mixed even coefficients lie in the box, and they can be paired with the actual odd component that has root \(T\). The necessary condition is not available for general convex or parity-product families with correlated even coefficients.

## 2. Exact maximization

Put \(r=H/L\), \(P_x=axc\), \(S_x=ac+(a+c)x\), and \(Q_x=a+c+x\). The coefficientwise minimal even evaluation at \(T\), divided by \(L\), is
\[
G(r)=\min(P_b,rP_d)-T\max(S_b,rS_d)
+T^2\min(Q_b,rQ_d)-T^3\max(1,r). \tag{5}
\]
The first, second, third and fourth switches occur at
\[
0<\frac bd<\frac{S_b}{S_d}<\frac{Q_b}{Q_d}<1. \tag{6}
\]
Both strict comparisons follow by cross multiplication: \(ac>0\), and \((a+c)^2-ac=C>0\). All operations are exact and the formula applies to arbitrary real parameters satisfying the stated strict inequalities.

Before \(S_b/S_d\), the slopes of \(G\) are strictly positive; after \(Q_b/Q_d\), they are strictly negative. Between them the slope is
\(T(TQ_d-S_d)\). Consequently
\[
\max_{r>0}G(r)=\max\left\{G(S_b/S_d),\ G(Q_b/Q_d)\right\}. \tag{7}
\]
The two candidates satisfy, using \(Q_bS_d-Q_dS_b=(d-b)C\),
\[
G(S_b/S_d)=E-\frac{(d-b)CT^2}{S_d},\qquad
G(Q_b/Q_d)=E-\frac{(d-b)CT}{Q_d}. \tag{8}
\]
Equations (7)–(8) give
\[
\max_{r>0}G(r)=E-(d-b)C\min\left\{\frac{T^2}{S_d},\frac{T}{Q_d}\right\}. \tag{9}
\]
If the middle slope vanishes there is a flat maximizer interval; otherwise the indicated switch is the unique maximum. This exact formula proves both directions of the **local** condition in §1.

## 3. Why it is necessary for an eligible box

At \(T\), the second odd root of an actual member, every actual even part obtained by independent coefficient mixing has positive value: combine it with that member's odd coefficients, then apply odd-degree Hermite–Biehler to the resulting actual Hurwitz polynomial. The minimal mixed value is \(LG(r)\), so \(G(r)>0\); in particular its maximum in (9) is positive. The strict inequality is necessary even when coefficient intervals are degenerate. No assumption that root values from one component are independent of scale is made beyond the literal box mixing.

The condition is genuinely nonvacuous: the predecessor constructs an explicit seven-positive-width all-Hurwitz box containing the pairs \(a=1/2,b=2,d=201/100,c=5\), and an actual member whose second odd root is \(9/2\). For \(a=1/2,b=2,c=5,T=9/2\), (9) reduces to the predecessor's sharp single-frequency threshold \(d<2218/959\). Its exact marker computations are a **named author-written import**, not independent verification of this general derivation.

## 4. Limits and provenance

This is a local necessary box-geometry inequality and exact single-frequency scale feasibility, not a proof that the whole box has a common numerator and not an eligible-box negative certificate. It uses no numerical search or execution. The only named classical import is Hermite–Biehler interlacing; the min/max and interpolation algebra are written deductions. No independent review, formal proof, parent adoption or novelty clearance is claimed. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
