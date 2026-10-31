# Independent author reconstruction: eligibility, exact septic SDP, and actual-root consumers

**Status: AUTHOR-WRITTEN, UNADOPTED; not blind, not a completed global theorem.** For the frozen f695 candidate I reconstruct the per-box statements below, subject to the explicitly named classical theorems and the stated S2–S4 imports. I found no mathematical counterargument to those per-box statements. Section 4 records a precise normalization clarification. In Section 9 I also independently derive the finite strict-negative normal form from the imported buffered bridge; this is conditional and supplies no counterexample. The original universal both-parity synthesis/ROOT/DUAL question remains **OPEN**. Parent full reading, disposition, and any additional verification are separate.

## 1. Exact object, order of choices, and physical pairing

Let
\[
K=\{a(s)=s^7+\textstyle\sum_{j=0}^6a_js^j:\ell_j\le a_j\le u_j\}
\]
be a nonempty compact **independent** box, with real endpoints and possibly degenerate intervals. Eligibility means **every actual member** is strictly Hurwitz. The synthesis target is
\[
\forall\,\hbox{eligible }K\quad\exists\,Q\ \hbox{monic, strictly Hurwitz}\quad
\forall a\in K\quad\forall\omega\in\mathbb R:
\operatorname{Re}\frac{Q(i\omega)}{a(i\omega)}>0.
\]
Here the same Q precedes the choices of member and frequency. A uniform shift formulation of strict positive realness follows for these rational functions: the stable denominator has a nonzero pole margin and the boundary ratio has a positive uniform margin, including its limit 1 at infinity. Conversely a strict positive-real ratio supplies these boundary inequalities. I use this standard rational strict-PR convention; no frequency-wise or slice-wise choice of Q is permitted.

For \(t=\omega^2\), set
\[
E_a=a_0-a_2t+a_4t^2-a_6t^3,\quad O_a=a_1-a_3t+a_5t^2-t^3,
\]
\[
F_Q=q_0-q_2t+q_4t^2-q_6t^3,\quad G_Q=q_1-q_3t+q_5t^2-t^3,
\]
where \(q_7=1\). Then
\[
a(i\omega)=E_a+i\omega O_a,\qquad
P_{Q,a}=F_QE_a+tG_QO_a=\operatorname{Re}(Q(i\omega)\overline{a(i\omega)}).
\]
The actual ascending-coefficient row is
\[
r_a(t)=(E_a,tO_a,-tE_a,-t^2O_a,t^2E_a,t^3O_a,-t^3E_a,-t^4O_a),
\quad q\cdot r_a=P_{Q,a}.
\]
Writing \(\widehat r=r/(1+t)^7\), the endpoint rows are \(\widehat r_a(0)=a_0e_0\) and \(\widehat r_a(\infty)=e_7\). These are limits of actual rows, not extra freely chosen finite-frequency polynomials.

For eligible K, the fixed-Q target is equivalent to one \(\eta>0\) satisfying
\[
P_{Q,a}(t)\ge\eta(1+t)^7\quad(a\in K,\ t\ge0). \tag{1}
\]
Indeed the normalized pairing is jointly continuous on compact \(K\times[0,\infty]\); at infinity it is 1, and strict boundary positivity makes its minimum positive. Conversely, for any fixed \(a_*\in K\), (1) gives positive boundary real part of \(Q/a_*\), analytic on the closed right half-plane with limit 1 at infinity. The harmonic minimum principle on large right half-disks gives positive real part in the open right half-plane. Thus Q cannot vanish there; (1) also excludes imaginary-axis zeros, so Q is strictly Hurwitz. Applying the same pairing to every a gives the common strict ratio. This pays stability of Q; it is not an extra hidden feasibility constraint.

## 2. Actual four-corner reduction, not a stability shortcut

Define
\[
\begin{aligned}
E_-&=\ell_0-u_2t+\ell_4t^2-u_6t^3,& E_+&=u_0-\ell_2t+u_4t^2-\ell_6t^3,\\
O_-&=\ell_1-u_3t+\ell_5t^2-t^3,& O_+&=u_1-\ell_3t+u_5t^2-t^3.
\end{aligned}
\]
Each pair \((E_\sigma,O_\tau)\), \(\sigma,\tau\in\{-,+\}\), comes from one fixed actual corner \(C_{\sigma\tau}\). For each fixed \(t\ge0\), the actual parity-value set is exactly \([E_-,E_+]\times[O_-,O_+]\): the even and odd coefficient coordinates are independent and the image of each coefficient rectangle under its linear evaluation map is its full interval. The physical row is affine in these two values, so it is a convex combination of the four **same-frequency** corner rows. This remains true when intervals or parity-value ranges collapse. Consequently the same Q and eta satisfy (1) for all members iff they satisfy it for all four corners and all t. This does not say that K is the convex hull of four polynomials and does not infer all-member Hurwitz stability from corner stability.

## 3. Exact all-member eligibility, including equality and degeneracy

Write \(b_j=(\ell_j+u_j)/2\), \(h_j=(u_j-\ell_j)/2\ge0\), and \(B=s^7+\sum b_js^j\). Put
\[
H_E=h_0+h_2t+h_4t^2+h_6t^3,\quad H_O=h_1+h_3t+h_5t^2,
\]
with \(E_b,O_b\) defined as above. I reconstruct the following iff:

1. B is strictly Hurwitz;
2. \(\ell_0>0\);
3. there is **no** \(t>0\) with both \(E_b(t)^2\le H_E(t)^2\) and \(O_b(t)^2\le H_O(t)^2\).

For \(t>0\), both halfwidths are nonnegative and the actual pair is the full rectangle \([E_b-H_E,E_b+H_E]\times[O_b-H_O,O_b+H_O]\). Thus the two weak inequalities, including equality and tangency, hold iff an actual member has \(a(i\sqrt t)=0\). At t=0, all members avoid zero iff the constant interval excludes zero. Necessity of \(\ell_0>0\) uses that every real monic Hurwitz polynomial has positive constant coefficient, and B is itself a member.

For sufficiency, fix an arbitrary actual a and use \(B_\theta=(1-\theta)B+\theta a\), \(0\le\theta\le1\), which remains in K. The three conditions exclude imaginary-axis zeros on the entire segment. Its coefficients are uniformly bounded and monicity gives a uniform Cauchy root bound, so no root can escape through infinity. Continuity of the multiset of roots, or of the spectral abscissa, then prevents a root from leaving the open left half-plane without an imaginary-axis crossing. Hence every actual a is Hurwitz. No positive-width assumption is used.

For the real-algebraic formulation, I import the classical Routh–Hurwitz criterion: let \(d_0=1,d_1=b_6,\ldots,d_7=b_0\), \(d_k=0\) outside \(0\le k\le7\), and \(H_{ij}=d_{2j-i}\). B is strictly Hurwitz iff all seven leading principal determinants of H are positive. The eligibility predicate is therefore a first-order polynomial predicate, with the exact no-zero clause
\[
\forall t\;[t>0\Rightarrow(E_b^2>H_E^2\ \lor\ O_b^2>H_O^2)]. \tag{2}
\]
Weak inequalities in the excluded joint condition must not be silently replaced by strict ones.

## 4. Per-box compact separation and the finite zero dual

Let \(S_K\) be the four compactified actual-corner curves for \(0\le t\le\infty\), and let \(H_K=\operatorname{conv}S_K\subset\mathbb R^8\). For each eligible K, strict common synthesis is equivalent to \(0\notin H_K\). The forward direction is (1). Conversely, if zero is outside this compact convex hull, let z be its minimum-norm point. The projection inequality gives \(z\cdot v\ge\|z\|^2>0\) for every \(v\in H_K\). Because \(e_7\in S_K\), \(z_7>0\); dividing z by \(z_7\) gives a single monic Q and a uniform positive margin, and Section 1 proves its stability.

If \(0\in H_K\), Carathéodory in \(\mathbb R^8\) gives at most nine compactified points. Combining endpoint contributions yields the exact alternative
\[
\sum_{i=1}^{m}w_i r_{C_i}(t_i)+\lambda e_0+\mu e_7=0,\qquad
m+\mathbf 1_{\lambda>0}+\mathbf 1_{\mu>0}\le9, \tag{3}
\]
where \(m\ge1\), each \(t_i,w_i>0\), \(\lambda,\mu\ge0\), and every \(C_i\) is one of the four actual corners; repetitions are permitted. At least one finite atom is needed, since a nontrivial positive combination of \(e_0,e_7\) cannot be zero.

**Normalization clarification.** If a normalized atom has coefficient \(\alpha_i>0\), its raw-row coefficient is \(w_i=\alpha_i/(1+t_i)^7\). Conversely, a raw coefficient \(w_i\) becomes \(\alpha_i=w_i(1+t_i)^7\), not \(w_i/(1+t_i)^7\). For a positive \(\lambda\), use any actual corner C with \(a_0(C)>0\), contributing coefficient \(\lambda/a_0(C)\) on its zero-frequency compactified row; infinity contributes coefficient \(\mu\). Dividing all these positive coefficients by their sum gives the convex representation. This makes the inverse scaling and the constant-endpoint factor explicit; it is not a counterexample to (3).

This is an exact **zero** dual for the same K, not an all-eight-strict-negative certificate. In (3) the six middle aggregate coordinates vanish, while the endpoint coordinates are \(-\lambda,-\mu\). In particular, neither (3) nor weak separation proves that this same K has an all-negative finite aggregate. No actual K satisfying (3) is furnished here.

## 5. Eight PSD blocks and rational certificates

Set \(v=(1,t,t^2,t^3)^T\) and \(p_{\sigma\tau}=P_{Q,C_{\sigma\tau}}-\eta(1+t)^7\). The exact fixed-K strict-synthesis feasibility system is
\[
\eta>0,\quad M_{\sigma\tau},N_{\sigma\tau}\succeq0,\quad
p_{\sigma\tau}=v^TM_{\sigma\tau}v+t\,v^TN_{\sigma\tau}v
\quad(\sigma,\tau\in\{-,+\}). \tag{4}
\]
There are seven free nonleading q coefficients, one eta, and eight symmetric 4-by-4 matrices with ten independent entries each: **88 real existential scalars**. Matching powers \(t^0,\ldots,t^7\) for each corner gives **32 equalities**, plus **eight PSD constraints**. They share one q and one eta. To specify the equalities literally, for \(k=0,\ldots,7\), \(q_7=a_7=1\), and empty sums zero,
\[
\begin{aligned}
&\sum_{i+j=k}(-1)^{i+j}q_{2i}a_{2j}
+\sum_{i+j=k-1}(-1)^{i+j}q_{2i+1}a_{2j+1}-\eta\binom7k\\
&\hspace{1cm}=\sum_{i+j=k}M_{ij}+\sum_{i+j=k-1}N_{ij},\qquad 0\le i,j\le3,
\end{aligned} \tag{5}
\]
with the appropriate actual corner coefficients a in each equation.

The half-line SOS implication is exact. For a real polynomial p of degree at most 7, \(p\ge0\) on \([0,\infty)\) iff (4)'s one-corner representation exists. The reverse implication is immediate. For the forward implication, \(p(x^2)\) is globally nonnegative of degree at most 14. Factoring into real roots of even multiplicity and conjugate pairs gives \(p(x^2)=A(x)^2+B(x)^2\), with real A,B of degree at most 7; zero is trivial. Split A and B into even and odd parts and average at \(x\) and \(-x\). This gives two squares in t plus t times two squares in t, all of degree at most 3, and their coefficient outer products give the PSD matrices. Together with Section 2 this proves (4), not merely a sampled-frequency test.

If the endpoints are rational and the strict target holds, all 88 quantities can be chosen rational with all eight matrices positive definite. First approximate the seven q entries by rationals closely enough to preserve a positive compactified margin, then choose a smaller positive rational eta. Let
\(T(t)=(1+t)\sum_{j=0}^3t^{2j}\). Its compactified ratio to \((1+t)^7\) is bounded, so subtract a sufficiently small rational \(\delta T\) from each residual while preserving nonnegativity. Apply the half-line representation and add \(\delta I\) to each of the two Gram matrices, obtaining positive-definite real matrices. With rational residual coefficients fixed, approximate all off-diagonal entries rationally. In the coefficient equation of degree \(2j\), the diagonal \(M_{jj}\) occurs with coefficient 1 and no other M or N diagonal does; in degree \(2j+1\), the corresponding independent diagonal is \(N_{jj}\). Solve these eight diagonal entries exactly. The corrections can be made arbitrarily small, so positive definiteness persists. Rational coefficient equalities and exact principal-minor signs would check such a certificate; none is supplied or run here.

Similarly, for rational endpoints, any existing zero dual (3) has a witness with real-algebraic \(t_i,w_i,\lambda,\mu\). For each finite choice of m, corner labels, and endpoint-support pattern permitted by (3), the defining equations and strict/non-strict inequalities form an existential polynomial formula over \(\mathbb Q\). Transfer between real closed fields gives a real-algebraic witness if a real witness exists. This is an existence theorem, not a rational-frequency assertion and not an observed obstruction.

## 6. One Q for the actual bands, every R4, and both R5 orientations

Assume K is eligible with at least one nondegenerate odd interval and (4) holds. A real monic strictly Hurwitz polynomial has strictly positive coefficients: factor it into \(s+\alpha\), \(\alpha>0\), and real irreducible quadratics \(s^2+2\alpha s+\alpha^2+\beta^2\), \(\alpha>0\). Hence \(q_0,\ldots,q_7>0\).

For any nonempty finite family of actual rows with \(w_i>0\), \(t_i>0\), and
\[
M_{\rm odd}=\sum_iw_i(t_iO_i,-t_i^2O_i,t_i^3O_i,-t_i^4O_i)\le0
\quad\text{componentwise},
\]
the very same Q and eta give
\[
\sum_iw_iF_Q(t_i)E_i(t_i)
=\sum_iw_iP_{Q,a_i}(t_i)-(q_1,q_3,q_5,1)\cdot M_{\rm odd}
\ge\eta\sum_iw_i(1+t_i)^7>0. \tag{6}
\]
No odd value is divided by in this inequality.

I explicitly import S3's actual-box band theorem, not arbitrary ordered markers: \(O_-\) has roots \(a,d,e\), \(O_+\) has roots \(b,c,f\), with \(0<a<b<c<d<e<f\); on the three actual bands \([a,b],[c,d],[e,f]\), every actual even value has respective strict sign \(-,+,-\), and \(O_-\le0\le O_+\). At an interior band point choose two actual corners with the **same** even endpoint, weights \(O_+,-O_-\), and the opposite odd endpoints. Their four odd moments cancel. At a boundary use the actual zero-odd singleton; do not divide by its zero. Equation (6) forces F to have the band sign, including at each boundary. Since \(F(0)=q_0>0\), the intermediate value theorem gives roots
\[
x\in(0,a),\qquad y\in(b,c),\qquad z\in(d,e).
\]
The degree is exactly three with leading coefficient \(-q_6<0\); these distinct roots exhaust it, and
\[
F_Q(t)=q_6(x-t)(y-t)(z-t). \tag{7}
\]
Thus the triple is one strict-interior triple determined by the same global Q, not a new triple selected per ray.

For an actual endpoint ray select its actual minimizing even endpoint \(E_F=E_-\) when F is nonnegative and \(E_F=E_+\) when F is negative; independence makes the chosen even and odd endpoints one actual corner at each node. From (6)–(7), every nonzero actual R4 and either actual R5 orientation satisfies, simultaneously,
\[
\sum_iw_iE_F(t_i)(x-t_i)(y-t_i)(z-t_i)
\ge\frac{\eta}{q_6}\sum_iw_i(1+t_i)^7>0. \tag{8}
\]
The same statement covers zero-odd singletons, same-frequency opposite-odd cancellations, and positive combinations. This verifies the direction from a feasible strict SDP to the full actual ROOT caller, not the reverse weak-to-strict implication on an unbuffered box.

For the named ray formulas, write \(0<u_1<\cdots<u_n\), \(H_n(t)=\prod_i(t-u_i)\), and let \(e_j(\widehat u_i)\) be the elementary symmetric polynomial in the other nodes. An actual R4 has odd signs \((- ,+,-,+)\) and for each omitted active moment \(k\in\{0,1,2,3\}\)
\[
w_i=\frac{e_{3-k}(\widehat u_i)}{u_iO_iH'_4(u_i)}>0.
\]
Lagrange interpolation of \(t^r\), \(0\le r\le3\), gives
\(\sum_i e_{3-k}(\widehat u_i)u_i^r/H'_4(u_i)=(-1)^{3-k}\delta_{rk}\). Thus its signed odd-moment vector is \(-e_k\). For R5 use
\(w_i=\varepsilon/[u_iO_iH'_5(u_i)]>0\), where \(\varepsilon=+1\) for signs \((+,-,+,-,+)\) and \(-1\) for the opposite orientation. Interpolation gives \(\sum_i u_i^r/H'_5(u_i)=0\) for \(r=0,1,2,3\), so all four signed moments vanish in **both** orientations. These computations independently establish applicability of (6) to every named ray. The completeness of the ray classification and the actual-band theorem themselves are imports at exactly S3's scope.

## 7. Exact quantified sentence; no global verdict

Let Elig be the ordered-endpoints condition, the seven positive Hurwitz determinants of the center, \(\ell_0>0\), and (2). The original strict universal problem is exactly
\[
\forall (\ell_0,u_0,\ldots,\ell_6,u_6)\in\mathbb R^{14}:\quad
\mathrm{Elig}(\ell,u)\Longrightarrow
\exists(q_0,\ldots,q_6,\eta,M_{\sigma\tau},N_{\sigma\tau})\;[(4)]. \tag{9}
\]
The inner existence block is the 88 scalars and 32 identities above. Each 4-by-4 PSD condition is equivalently the nonnegativity of **all 15 principal minors**, giving 120 such inequalities across the eight blocks. The eligibility frequency variable in (2) retains its own universal quantifier inside the antecedent. This is a first-order sentence over a real closed field. Classical quantifier elimination decides its truth in principle, but I have not performed QE, supplied a solver or its running time, proved (9), or produced an eligible counterexample. Merely displaying (9) is not a proof of its consequent.

## 8. Fresh both-parity positive example and exact comparison

For completeness I reconstruct S1's local example. Let \(Q=(s+1)^7\) and independently perturb all seven lower coefficients by \(|d_0|\le9/10\), \(|d_j|\le1/100\) for \(1\le j\le6\). Thus both parities genuinely vary. For \(t=\omega^2\), \(|Q(i\omega)|=(1+t)^{7/2}\), and, since \(j\le6\),
\[
\left|Q(i\omega)\overline{\sum_{j=0}^6d_j(i\omega)^j}\right|
\le(1+t)^{7/2}\sum_jh_jt^{j/2}
\le\tfrac{24}{25}(1+t)^7.
\]
Consequently \(P_{Q,a}(t)\ge\frac1{25}(1+t)^7\). The same bound applies on every segment \(Q+\theta(a-Q)\), so no segment polynomial has an imaginary-axis zero. Monicity, bounded roots, and the stable start Q prove all-member eligibility. This is a full-width positive example, not evidence for every box.

Its constant interval is \([1/10,19/10]\), ratio 19. In S4's displayed scaled-binomial sufficient family, the constant interval ratio is \((1+\epsilon)/(1-\epsilon)<11\), for every \(\beta>0\) and \(0<\epsilon<5/6\). A positive interval containing \([1/10,19/10]\) would have ratio at least 19, so no box from that **particular** family contains this example. This does not compare it against every other positive neighborhood or establish the global target.

## 9. Buffered versus same-box dual; conditional finite normal form

Define \(\mathcal B(K)\) to mean that there exists a nonzero coefficientwise nonnegative vector q of degree at most 7 with \(q\cdot r_a(t)\ge0\) for **every** actual member and frequency. S2 imports the bridge: for each eligible K there is an eligible enlargement L obtained by independent positive constant and linear buffers, and \(\mathcal B(L)\Rightarrow\) one strict common-SPR Q on K. It does **not** say \(\mathcal B(K)\Rightarrow\) strict synthesis on that same K. S2 also states the universal SPR/DUAL/ROOT equivalence; S3 supplies the actual ROOT interface. I do not substitute a same-box weak-to-strict theorem for these imports.

Here is a direct reconstruction of the conditional strict-negative normal form, with its dependence on the buffered bridge explicit.

* For any eligible L, \(\mathcal B(L)\) is equivalent to \(H_L\) being disjoint from the open negative orthant \(D=\{x:x_j<0\ \forall j\}\). If a nonzero nonnegative q is weakly nonnegative on H, then no point of H lies in D. Conversely, compact convex H and open convex D can be weakly separated. Because D is an open cone, a separating normal can be chosen nonzero and coefficientwise nonnegative, with \(q\cdot H\ge0\). This is a weak separator, not the strict separator of Section 4.
* If some eligible K lacks a strict common numerator, the imported implication gives \(\neg\mathcal B(L)\) for its eligible buffer L. Hence \(H_L\cap D\ne\varnothing\). Represent a point in this intersection by finitely many compactified corner atoms. If an atom is at 0 or infinity, replace it by a sufficiently nearby positive finite frequency on the same corner curve. Since D is open, all eight signs remain strictly negative. Convert the normalized coefficients into positive raw-row weights using Section 4.
* Conic Carathéodory now reduces this **same strictly negative vector** to at most eight positive actual-corner atoms. Indeed, for more than eight vectors a nonzero linear dependence exists; choose its sign with at least one positive coefficient and subtract the largest permitted nonnegative multiple from the current positive coefficients. At least one coefficient becomes zero, none becomes negative, and the sum remains unchanged. Repeat.
* Strict Hurwitz stability is open in the coefficient vector. Since L is compact and all its actual members are stable, some uniform coefficient neighborhood of L is stable. Perturb/expand its fourteen endpoints to nearby rational endpoints with all seven widths positive; every member of the new box remains in that stable neighborhood. Perturb the finitely many positive squared frequencies and weights to positive rationals. The selected corner rows and their aggregate depend continuously on these quantities, so all eight strict negative inequalities persist. The resulting rational full-width eligible box and at-most-eight actual-corner atoms need not equal the original K or its original L.

Conversely, a supplied eligible strict-negative aggregate rules out a strict common numerator on that same box, because a stable monic numerator has strictly positive coefficients while (1) makes its pairing with each positive atom strictly positive. Therefore the conditional global counterexample normal form is sound, but **no such aggregate or box is asserted or supplied**. The zero dual (3) alone does not supply it. Fixed-parity scoped results, the strict-negative normal form, and the ROOT equivalence are not automatic clearance of any older gate.

## 10. Imports, coverage, chronology, and assurance

* Source packet: one ordered part, SHA-256 `7c776fa3df1aa8075ea6cf786f38ea518f7f159d1192b1278eb5913bd52662b9`; I directly read raw LF 1–325 in consecutive serial windows of at most 20 LF, through the ending. It renders complete S1 f695 lines 1–182, S2 lines 1–40, S3 lines 1–46, and S4 lines 1–39. The parent freeze receipt reports complete-body roundtrip and persisted-byte equality; I did not independently re-render or authenticate original source bytes.
* Before the direct pre-body ACK to Main I read the manifest, freeze receipt, final binding, prepared live metadata, actual dispatch, all 21 manifest-listed permission/status-only controls through their endings, and the referenced multipart policy. Directly observed manifest SHA-256 `3c0a4819a197c2e4eceb8467e9a3cea38486b043506ea9b0f4146fd0364b86c8`, freeze `69aae5ebc09a39dbd2987815a3aa99a58e030b0f168fcb40ee433eef29359482`, and final binding `29603673799dfdd1a22b6767f3742061614941bff5e2285d17094f0d9ad6bb99` match the assignment. Controls were read in parallel batches; no serial completion order is claimed. I made no mathematical derivation before the ACK or before the complete ordered packet read.
* This is nonblind: the manifest's task description and the f695 candidate itself were visible. Mathematical imports are the classical root-continuity/Cauchy bound, harmonic minimum principle, Routh–Hurwitz criterion, compact convex separation, Carathéodory, Lagrange interpolation, real closed fields/quantifier elimination, and the explicitly scoped S2 buffered bridge/S3 actual-band and cone statements/S4 comparison family. No independent authentication of those source identities, source-wide correspondence, worldwide status, or novelty is claimed.
* I followed no packet outgoing scientific links, held episode, held history or consumer, sibling proof, or old code. No child scientific executable, code, test, build, lint, formatter, solver, public-source fetch, external-model CLI, install, Git or paid/heavy action was run. The clock observed before composing this output was `2026-10-30T16:43:28-0700 PDT`; it is not backdated. All held episodes **and all their consumers remain NONINPUT**. No private-cognition certificate is asserted.
* This author's reconstruction, including the conditional normal form, is not a family review, parent disposition, independent-model-family/human/formal-kernel verification, a finite-run receipt, an actual strict-negative witness, or universal theorem closure. Any prospective executable requires the parent's full static read and separate GO under the assigned time bound.
