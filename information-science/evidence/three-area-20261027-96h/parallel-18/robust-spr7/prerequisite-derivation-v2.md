# Actual septic-box coupling II — shared root bands rule out every four-frequency dual and five-frequency endpoint-free dual

Owner **InfoSPR7-2**, same info-2. Actual `/bin/date` immediately before this write: **Tue Oct 27 14:58:24 PDT 2026**.
**WRITTEN author candidate, unreviewed.** This is a substantive continuation of the current S1 definition-first task, not a new input release, old-method revival, universal synthesis theorem or actual counterexample.

## 1. Inputs, scope and relation to the first packet

The mathematical starting inputs remain ONLY the supplied definitions in packet SHA256 `9df2b558c03b2aac8cefb786be5a2a0802de822724bcd6ee60b47d0205fc61f6` and named elementary facts. The current first derivation `prerequisite-derivation-v1.md`, **117LF/16223B**, SHA256 `2c50f876efc528ec5f276ea52694fa7175516da830d176b842e535ecc1bef677`, supplies the FULL exact-degree/strict-zero/infinity/vertex/actual-member finite-dual alternative. It is a NEW current unreviewed manuscript, not an adopted old research import. A full gate must read BOTH packets and every boundary.

No old SPR/contact/reciprocal/phase-table proof, dossier suffix, work/ file, lower-degree announcement, checkpoint/park/identity-map body or held/withdrawn/ZERO guide is read or used as a theorem. The elementary phase/root-band necessity and Vandermonde identities needed below are proved inline; this is NOT a transfer of an older named contact theorem or an independent-provenance claim. Historical exposure and all six findings remain.

K is the SAME actual independent closed monic coefficient box of degree7, with EVERY member strictly Hurwitz. Its target is ONE unrestricted real numerator of EXACT degree7 with strict positive real ratio against EVERY member at EVERY finite real frequency including0. Degenerate coefficient intervals remain allowed.

From v1, failure of this original target is equivalent to an actual positive annihilator on at most9 compactified-frequency atoms. Atoms at the same frequency can be merged by averaging ACTUAL members inside the SAME K. We use that exact caller, including at0 and infinity, not an invented abstract tuple.

**New conclusion:** every such genuine obstruction has at least5 DISTINCT positive finite frequencies, regardless of endpoints. If neither endpoint occurs, it has at least6. This strengthens v1's interpolation budget by using the independent actual-box/Hurwitz coupling, not just the dimension of polynomial evaluation.

## 2. Elementary root-interlacing necessity for one actual member

For an actual a write
`a(i sqrt(t))=E_a(t)+i sqrt(t) O_a(t)` for t>=0,
where
`E_a(t)=a_0-a_2 t+a_4 t^2-a_6 t^3`,
`O_a(t)=a_1-a_3 t+a_5 t^2-t^3`.
This is a direct evaluation identity, not a numerator profile restriction. It is used to analyze the FULL unrestricted-numerator annihilator.

**Lemma 1.** Each E_a and O_a has three distinct positive roots, respectively e_1<e_2<e_3 and o_1<o_2<o_3, with
`0<e_1<o_1<e_2<o_2<e_3<o_3`.
Their signs start positive at0 and alternate at these roots.

**Proof from roots of a.** Factor a(s)=product_(r=1..7)(s+alpha_r-i beta_r), alpha_r>0, with conjugate roots paired. The continuous argument theta(w) of a(iw), starting at theta(0)=0, satisfies
`theta'(w)=sum_r alpha_r/(alpha_r^2+(w-beta_r)^2)>0`.
The formula is the elementary derivative of the argument of each nonzero factor. Conjugate pairing makes the initial argument0; each factor's argument tends to pi/2 as w increases, so theta increases strictly from0 toward7pi/2, never reaching that endpoint at finite w.

The real part vanishes exactly at theta=pi/2,3pi/2,5pi/2. The imaginary part, apart from w=0, vanishes exactly at theta=pi,2pi,3pi. Each crossing is simple because |a(iw)|>0 and theta'>0. Passing to t=w^2 preserves the strict order and simplicity. The displayed E/O polynomials are cubics (a_6=sum alpha_r>0), so these are all their roots. Their positive constants follow from the positive coefficients of real linear/quadratic Hurwitz factors. This proves the signs and order without importing a Hermite–Biehler/edge theorem.

## 3. Independent coefficient intervals force COMMON disjoint root bands

Let E-box be the compact family of E polynomials obtained from the EVEN coefficients of K and O-box the compact family obtained from its ODD coefficients, with the monic leading odd coefficient fixed. Independence of ALL original coefficient intervals means EVERY pair (E,O) in this product comes from an ACTUAL member of K. Every pair therefore satisfies Lemma1.

For each E define its ordered roots e_i(E), and similarly o_i(O). These root functions are continuous on their respective compact coefficient boxes. To see the needed elementary fact, isolate the three simple positive roots of one polynomial in disjoint small intervals with opposite endpoint signs. Nearby coefficients preserve these signs, hence have one root in each interval by the intermediate-value theorem; cubic degree leaves no additional roots. This gives local continuity of each ordered root. The leading coefficients never vanish on the compact boxes. Thus each root has a finite attained minimum and maximum, including when its range is a point.

For EVERY E and EVERY O, Lemma1 gives e_i(E)<o_i(O) and, for i<3, o_i(O)<e_(i+1)(E). Choose independent maximizers/minimizers: the extrema still form actual members because the parity boxes are independent. Consequently
`max e_1 < min o_1 <= max o_1 < min e_2 <= max e_2 < min o_2`
`<= max o_2 < min e_3 <= max e_3 < min o_3`.
All strict gaps are genuine; they are not inferred from separate extrema that cannot coexist. This is where the original independent BOX hypothesis is used. The statement is not asserted for a merely correlated collection of stable polynomials.

Two sign-order consequences will be used. They hold even if different ACTUAL members are used at every sampled t.

- **Same-sign locations:** possible (++),(--),(++),(--) regions occur only in this global order: before an even first root; between an odd first and even second root; between an odd second and even third root; after an odd third root. Every location in each listed class precedes every location in the next. For example the first -- location is below max e_2, while every later ++ location exceeds min o_2>max e_2. Initial ++ locations precede min o_1; final -- locations exceed max e_3.
- **Opposite-sign locations:** possible (-,+),(+,-),(-,+) regions occur only in that global order, between e_1/o_1, e_2/o_2 and e_3/o_3 respectively. Every first class is below max o_1<min e_2, and every second class is below max o_2<min e_3.
- At an E-root, O has signs (+,-,+) on the globally ordered three E-root bands. At an O-root, E has signs (-,+,-) on the globally ordered three O-root bands.

These assertions concern the order of the indicated sign CLASSES, not a false assertion that any one sign is monotone throughout a root band. No contact orientation, unwrapped word list or legacy chart is assumed.

## 4. Exact moment equations of an ACTUAL merged annihilator

Suppose an obstruction certificate from v1 has m distinct positive finite nodes t_1<...<t_m. Let a^(j) be the ACTUAL averaged member at t_j, with values E_j and O_j. Its positive merged weight is Lambda_j and put `mu_j=Lambda_j/(1+t_j)^7>0`.

If0 is present put `eta_0=Lambda_0 a_bar_0(0)>0`; otherwise eta_0=0. If infinity is present put eta_inf=Lambda_inf>0; otherwise eta_inf=0. These strict signs use actual Hurwitz constant coefficients and the exact monic leading coefficient, not an arbitrary endpoint functional.

Test the claimed annihilator against the eight monomials b(s)=s^k. Equivalently expand `P_(a,b)=E_b E_a+t O_b O_a`. The resulting equations are EXACTLY, for k=0,1,2,3,
`sum_j mu_j t_j^k E_j = -eta_0 * 1_(k=0)`,
`sum_j mu_j t_j^(k+1) O_j = eta_inf * 1_(k=3)`.
The sign of the infinity term in the second equation is important: the coefficient of t^3 in O_b is -b_7, while the infinity functional is +b_7. No scalar numeric instance or arithmetic interpreter is used.

For distinct nodes t_j define H(t)=product_j(t-t_j). The elementary Lagrange identity gives
`sum_j t_j^k/H'(t_j)=0` for0<=k<=m-2,
`sum_j t_j^(m-1)/H'(t_j)=1`.
Indeed interpolate t^k at the m nodes and compare the coefficient of t^(m-1) in its degree-at-most(m-1) interpolant. Also
`sum_j 1/(t_j H'(t_j))=-1/H(0)`
when all nodes are positive, by the partial-fraction identity for1/H evaluated at0; multiplying that identity by H gives a polynomial identity verified at every distinct node, so no rational-function theorem beyond interpolation is needed.

## 5. Theorem C — NO genuine obstruction on four positive frequencies, with ANY endpoints

Cases m<=3 and m=4 with no endpoint were excluded by v1's interpolation budget. It remains to treat m=4 with at least one endpoint. Then H is quartic and H(0)>0. In ascending-node order H'(t_j) has signs (-,+,-,+).

The four-by-four Vandermonde matrix is invertible: a polynomial of degree at most3 vanishing at four distinct nodes is zero, so its transpose has trivial kernel. The moment equations and the identities above therefore determine their solutions uniquely.

**Case 1: zero only.** eta_0>0 and eta_inf=0. The odd equations force O_j=0 for all four nodes. The even equations give
`mu_j E_j=eta_0 H(0)/(t_j H'(t_j))`.
Thus the E_j signs are (-,+,-,+). But at any actual O-root the E sign is (-,+,-) on the three globally ordered O-root bands. Four ordered nodes with strictly alternating E signs cannot fit: every sign change must move to a different later band, and there are only three bands. Contradiction.

**Case 2: infinity only.** eta_0=0 and eta_inf>0. The even equations force E_j=0 for all four nodes. The odd equations give
`mu_j t_j O_j=eta_inf/H'(t_j)`.
Thus O_j has signs (-,+,-,+). At actual E-roots O has only (+,-,+) on its three globally ordered bands, so again four strictly alternating signs are impossible. Contradiction.

**Case 3: both endpoints.** The same unique solutions give
`mu_j E_j=eta_0 H(0)/(t_j H'(t_j))`,
`mu_j t_j O_j=eta_inf/H'(t_j)`.
Both constants are positive. Hence the sign pairs are (--),(++),(--),(++). The same-sign classes in §3 are ordered (++),(--),(++),(--). Starting with -- leaves at most the later ++ and final --, with no later ++. The required four-node pattern is impossible. Contradiction.

These cases cover every endpoint pattern and retain strict endpoint signs. Therefore EVERY actual original-box obstruction requires m>=5 distinct positive finite frequencies, regardless of how many actual member atoms were originally merged there. This is a uniform actual-box coupling exclusion, not a sampled calculation or a lower-degree numerator ansatz.

## 6. Theorem D — five positive frequencies with NO endpoints also cannot obstruct

Now m=5 and eta_0=eta_inf=0. The four-row Vandermonde moment matrix has rank4: a degree-at-most3 polynomial with five distinct roots is zero. Its nullspace is one-dimensional. The vector with entries1/H'(t_j) lies in that nullspace by §4 and is nonzero. Therefore, for some real constants c,d,
`mu_j E_j=c/H'(t_j)`,
`mu_j t_j O_j=d/H'(t_j)`.
For five increasing nodes H'(t_j) has signs (+,-,+,-,+).

- If c and d are both nonzero with the SAME sign, the pairs alternate between ++ and -- at all five nodes. The entire actual box has only the four globally ordered same-sign classes in §3. Five alternating pairs are impossible.
- If c and d have OPPOSITE signs, the pairs alternate between -+ and +-. There are only the three globally ordered opposite-sign classes. Five alternating pairs are impossible.
- If c=0 but d!=0, every E_j=0 while the O_j signs alternate at five nodes. At E-roots the actual O signs lie in the three ordered bands (+,-,+); impossible. If d=0 but c!=0, the analogous O-root sign bands (-,+,-) give the same contradiction.
- If c=d=0, each actual a^(j) vanishes at i sqrt(t_j), contrary to strict Hurwitz stability.

Thus no five-frequency endpoint-free certificate exists. Endpoint strictness is not smuggled into this case: eta_0=eta_inf=0 is precisely the absence of those atoms.

## 7. Full original-object consequence and exact remaining gap

Combine the new theorems with v1's complete necessary-and-sufficient actual-member alternative. If the ORIGINAL septic problem has a negative box, it has an obstruction certificate with at most9 merged atoms, and:

- with no endpoint it needs at least6 DISTINCT positive finite frequencies;
- with exactly one endpoint it needs at least5;
- with both endpoints it needs at least5.

These are necessary restrictions on an ACTUAL original-class certificate, not a claim that any freely selected data above those thresholds are realizable. No obstruction is supplied and no universal common numerator is constructed. Degenerate coefficient intervals are covered by the same compact parity-box argument; if either parity family is a singleton its root bands may be points but all required cross-band gaps remain strict.

The forward original caller is unchanged: an actual positive annihilator excludes ALL unrestricted exact-degree7 common numerators. The converse original caller is unchanged: original failure produces such actual data by v1, and the new actual-box bands/moment equations force the restrictions above. No correlated-family, reciprocal-only, strict-width, general-chart-attainment or finite-sample replacement occurs.

**First remaining step:** control the higher-frequency moment nullspaces while keeping ALL averaged members in the SAME independent Hurwitz coefficient box. The simple one-dimensional alternating-vector argument no longer covers the endpoint cases at five nodes or the endpoint-free case from six nodes. An admissible all-variable contradiction there, or an actual eligible annihilator and actual box, would change the original conclusion. The present theorems do not assert that merely counting nodes or choosing a phase pattern supplies either result.

The sign/root-band facts themselves are necessary actual-box couplings, not claimed sufficient to solve synthesis. A new polynomial realization or a moment tuple cannot be declared actual merely because it passes these sign restrictions. No legacy critical-chart or old consumer is imported to close this gap.

## 8. Verification and process ceiling

All math here is conventional WRITTEN algebra/analysis. Named ordinary facts: elementary factorization and argument derivative of a nonzero complex linear factor, intermediate value/root counting, continuity on compact finite-dimensional coefficient sets, real linear algebra and polynomial interpolation. Every specialized phase/interlacing/band/moment application is supplied, not borrowed from an unprovided theorem or old review. No numeric parameter, polynomial box, boundary sample, decimal, scientific program or CAS was selected/executed. Metadata clocks/hashes/counts only.

The combined v1/v2 candidate requires an exact frozen full-scope review and complete parent reads before any adoption. No formal/kernel/human/configured-family/executable/novelty or book-image-equivalence claim. Same existing owner/new exclusive root; old round CLOSED/FROZEN; all SPR78 limits outside S1, HOLDv2, N4 UNKNOWN/historical exit unestablished, auxiliary214 STOP and all findings/ZERO consumers persist. Research deadline remains2026-10-31T21:23:27.000Z; no early cutoff or one-file-completion inference.
