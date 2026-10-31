# f707: exact both-parity four-corner certificate and bounded finite-source proposal

**Status: AUTHOR-WRITTEN CANDIDATE; SOURCE AND ALL ITS OUTPUTS NOT RUN.** This is a single explicit full-width box and a synthetic logical guard, not an arbitrary-box theorem or a counterexample. No parent disposition, independent reviewer, family, human, kernel, original printed-source identity, or novelty clearance is implied. The global ROOT/SPR/DUAL caller and a genuine eligible at-most-nine-atom zero obstruction remain **NOT ISSUED**. All held episodes and every consumer remain NONINPUT; no prior gate is cleared or historical record backdated.

Native clock observed before composing this narrative: `2026-10-30T16:44:18-0700 PDT`. The prospective executable is [`exact-finite-source-v1.py`](exact-finite-source-v1.py), SHA-256 `b95f71640d0a693e3d823ed14fc85b79942cc632e7043f1aada483fe2008b14c`. It was created once exclusively from final bytes and has **not** been imported, compiled, run, linted, tested, or formatted. Parent must read the complete source and independently decide whether to grant one bounded execution, with an external limit at most 55 seconds; a proposed command is `python3 -B exact-finite-source-v1.py` under the parent's admission and output/settlement controls. No execution is authorized by this document. Results described as checked by the program are conditional expectations, not observed outputs. A subsequent correction requires a new complete file or addendum, never modifying these bytes.

## 1. Exact object and all-member Hurwitz proof

Write coefficients ascending. Let

\[
Q(s)=(s+1)^7,\quad q=(1,7,21,35,35,21,7,1),\qquad
K_{\rm small}: a_j\in[q_j-1/1000,q_j+1/1000]\ (0\le j\le6),\ a_7=1.
\]

All seven independent widths are positive, including both parities. For **every** actual member write \(a=Q+\delta\), where \(|d_j|\le h_j=1/1000\). For \(t=\omega^2\ge0\), since \(|\omega|^j\le(1+t)^{7/2}\) for \(j\le6\),

\[
 |\delta(i\omega)|\le\sum_{j=0}^6h_j|\omega|^j
 \le {7\over1000}(1+t)^{7/2},\quad |Q(i\omega)|=(1+t)^{7/2}.
\]

For the entire segment \(a_\theta=Q+\theta\delta\), \(0\le\theta\le1\), the triangle inequality and real-part bound give

\[
\operatorname{Re}[Q(i\omega)\overline{a_\theta(i\omega)}]
\ge(1-7/1000)(1+t)^7={993\over1000}(1+t)^7>0.
\]

Thus no segment polynomial has an imaginary-axis root. Roots of this bounded monic degree-seven segment vary continuously and cannot escape to infinity; since \(Q\) has seven roots at \(-1\), **every member** of \(K_{\rm small}\) is Hurwitz. This is an all-member homotopy, not a corner-stability shortcut, and it is independent of sampling. Its stronger analytic margin also confirms that the small SDP margin below is conservative.

## 2. Four exact actual-corner diagonal Gram certificates

Put \(\sigma,\tau\in\{-1,+1\}\). For the even coefficients \((a_0,a_2,a_4,a_6)\), label \(\sigma=-1\) as \((\ell_0,u_2,\ell_4,u_6)\) and \(\sigma=+1\) as \((u_0,\ell_2,u_4,\ell_6)\). For \((a_1,a_3,a_5)\), \(\tau=-1\) is \((\ell_1,u_3,\ell_5)\), and \(\tau=+1\) is \((u_1,\ell_3,u_5)\). These four are **actual** box members; at each \(t\ge0\) their even/odd values give the four corners of the actual parity rectangle. The convex weights needed for an arbitrary member can depend on \(a,t\); this does not say the seven-dimensional coefficient box is the convex hull of four polynomials.

Set \(F=1-21t+35t^2-7t^3\), \(G=7-35t+21t^2-t^3\). For these actual corners

\[
 E_{\sigma}=F+{\sigma\over1000}(1+t+t^2+t^3),\qquad
 O_{\tau}=G+{\tau\over1000}(1+t+t^2).
\]

With the **same** \(Q\) and \(\eta=1/2>0\) for all four, set \(P_{\sigma\tau}=F E_{\sigma}+tG O_{\tau}\) and \(p_{\sigma\tau}=P_{\sigma\tau}-\eta(1+t)^7\). Exact polynomial expansion yields, for \(0\le k\le7\),

\[
 [t^k]p_{\sigma\tau}={1\over2}{7\choose k}+{\sigma A_k+\tau B_k\over1000},\quad
 A=(1,-20,15,8,7,28,-7,0),\quad B=(0,7,-28,-7,-15,20,-1,0).
\]

Let \(v=(1,t,t^2,t^3)^T\). The following explicit rational **diagonal** matrices supply all eight Gram blocks:

\[
M_{\sigma\tau}={1\over1000}\operatorname{diag}
 (500+\sigma,\ 10500+15\sigma-28\tau,\ 17500+7\sigma-15\tau,\ 3500-7\sigma-\tau),
\]
\[
N_{\sigma\tau}={1\over1000}\operatorname{diag}
 (3500-20\sigma+7\tau,\ 17500+8\sigma-7\tau,\ 10500+28\sigma+20\tau,\ 500).
\]

For each label, \(p_{\sigma\tau}=v^TM_{\sigma\tau}v+t\,v^TN_{\sigma\tau}v\) coefficient by coefficient. The componentwise lower numerators across all labels are respectively
`M: (499, 10457, 17478, 3492)` and `N: (3473, 17485, 10452, 500)`, all divided by 1000; hence the matrices are in fact positive definite. Thus the four nonnegative polynomials give the margin for **every nonnegative real** \(t\), not just tested frequencies. Because each \(P\) is affine in the actual even/odd rectangle values at fixed \(t\), the same \(Q,\eta\) work for every actual box member. At infinity, the leading coefficient of every \(P\) is \(q_7a_7=1\) and \(p\)'s leading coefficient is \(1-\eta=1/2\); this is the compactified \(t=\infty\) boundary, not an inference from finite-frequency samples. Together with the preceding all-member stability proof this gives one strict common positive-real numerator **for this one box**.

The source computes actual coefficients independently from parity convolution; computes the displayed \(A,B\) formula; builds both explicit diagonal Gram matrices; and compares the eight coefficients of each Gram expression against the physical residual, for 32 exact rational identities in all. Its rational sample checks at \(\omega=0,1/2,1,2,3\), and \(t=\omega^2\), compare polynomial convolution with rational-pair complex Horner evaluation, the direct parity expression and the raw physical-row dot product. These samples are cross-checks only and do not establish the all-frequency claim. The exact symbolic coefficient identities and PSD calculation are the intended all-frequency finite certificate; no program check or output has been observed.

For this box's actual positive-weight row collections, the same positive-coefficient \(Q\) and the margin imply that a nonpositive aggregate of the four signed odd coordinates leaves a strictly positive even contribution. This applies uniformly to every actual R4 omitted moment and **both** actual R5 orientations, as well as zero-odd and opposite-odd cancellations, whenever their stated cone hypotheses hold. The source does not enumerate the continuum of such rays: its missing-orientation test is a scope guard, not a proof by enumeration or a counterexample.

## 3. Original wide 9/10 diagnostic: analytic bound, not an emitted Gram certificate

For the separate box centered on the same \(Q\), take \(h_0=9/10\), \(h_j=1/100\) for \(1\le j\le6\). Every width is positive and \(\sum h_j=24/25<1\). The same triangle and homotopy proof, now with the full \(24/25\) bound, gives for every member and every frequency

\[
 P_{Q,a}(t)\ge {1\over25}(1+t)^7,
\]

and proves that every actual member is strictly Hurwitz. This is not corner-only inference. The constant interval is \([1/10,19/10]\), ratio 19. In the assigned displayed scaled-binomial family, for \(\beta>0\) and \(0<\epsilon<5/6\), the constant-endpoint ratio is \((1+\epsilon)/(1-\epsilon)<11\), independent of \(\beta\); hence no such interval can contain this wide interval. This excludes containment only in that displayed family, not every other previously proved family.

**WIDE SDP: NOT TESTED.** This source does not materialize or verify a wide-box Gram certificate, does not invoke an approximate solver, and does not pretend that the small-box diagonal matrices certify the wide diagnostic. The written analytic margin and homotopy are separate claims subject to parent review. The code is designed to check the exact width sum, margin, interval ratio, and algebraic threshold; no such check has actually been run.

## 4. Explicit zero-hull guard, intentionally noneligible

This is a bounded **synthetic logical control**, not an eligible-box obstruction and not an all-eight-negative witness. For four positive nodes use these rational monic septics (all unlisted coefficients are zero):

| \(t_i\) | \(E_i\) | \(O_i\) | \(a_i(s)=s^7+a_{1i}s+a_{0i}\) |
|---:|---:|---:|---|
| 1 | −4 | −1/6 | \(s^7+(5/6)s-4\) |
| 2 | 6 | 1/4 | \(s^7+(33/4)s+6\) |
| 3 | −4 | −1/6 | \(s^7+(161/6)s-4\) |
| 4 | 1 | 1/24 | \(s^7+(1537/24)s+1\) |

At each listed node the table really has \(E_i=a_{0i}\) and \(O_i=a_{1i}-t_i^3\). Their raw physical rows are
\(r_i=(E_i,t_iO_i,-t_iE_i,-t_i^2O_i,t_i^2E_i,t_i^3O_i,-t_i^3E_i,-t_i^4O_i)\). The exact signed moment identities are

\[
\sum_i E_i=-1,\quad \sum_i t_i^k E_i=0\ (k=1,2,3),\quad
\sum_i t_i^kO_i=0\ (k=1,2,3),\quad \sum_i t_i^4O_i=1.
\]

Consequently \(\sum_i r_i+e_0+e_7=0\). The fourth listed polynomial has the genuine zero-frequency raw endpoint \(e_0\); monicity gives the normalized infinity endpoint \(e_7\). Let \(R_i=r_i/(1+t_i)^7\), \(D=\sum_i(1+t_i)^7+2=96826\), and use the strictly positive convex weights \((1+t_i)^7/D\) for the four finite rows and \(1/D\) for each endpoint. They sum to one and their weighted row sum is exactly zero.

If \(m(q)=\min_{R\in\{R_i,e_0,e_7\}}q\cdot R\), the zero hull forces \(m(q)\le0\) for every \(q\); the zero vector attains zero. Thus the **unconstrained synthetic phase maximum is exactly zero**, not a strictly positive separation. With the additional monic constraint \(q_7=1\), the same weighted identity even gives \(m(q)\le-1/96825\), because the infinity row has positive weight and pairing one. This is a small algebraic phase guard, not an optimizer or a proof about the original eligible boxes.

The first polynomial has negative value at \(s=0\) and positive value at \(s=2\), so it has a positive real root by the intermediate value theorem. Hence the displayed polynomials cannot all belong to any all-Hurwitz box, and they are not asserted to be the four envelope corners of an eligible box. The intended program emits these rational rows and weights, checks their aggregate and the zero-phase condition, and checks that calling the zero maximum strictly positive is rejected. **Eligible zero-hull materialization: NOT TESTED.** No finite zero obstruction in an eligible box and no strict-negative actual-corner certificate is supplied.

## 5. Source scope and intended mutation discrimination

The stdlib source uses `Fraction` for scientific arithmetic, fixed explicit data and finite loops; it reads no files or input, creates/deletes nothing, uses no network or child process, and emits its one JSON result to stdout. It has no random choices, external dependencies, solver calls, arbitrary-input decision procedure, or unbounded search. The 100,000-byte number in the assigned metadata is a **packet-part transport limit only**, not a scientific output limit.

Each control is designed to require its particular named rejection, not merely an arbitrary exception; however all are **NOT RUN** until parent GO and the observed result:

| Mutation | Intended rejection | What it does / does not establish |
|---|---|---|
| wrong even endpoint selected | `ENDPOINT_PARITY` | Violates the actual endpoint pattern. |
| wrong even sign; wrong odd sign | `PARITY_COMPLEX_MISMATCH` | Each contradicts exact direct complex evaluation at an explicit rational point; sampling is not proof of the sign formula. |
| omit one R5 orientation | `R5_ORIENTATION_SCOPE` | Missing-scope guard only, not a counterexample or ray enumeration. |
| one corner gets a different q | `NONUNIFORM_Q` | Enforces one numerator before all four corners. |
| all q have q7 different from one | `Q7_NOT_MONIC` | Enforces the normalized infinity boundary. |
| eta set to zero | `ETA_NOT_POSITIVE` | Weak is not strict. |
| claim all-member stability from corners only | `CORNER_STABILITY_NOT_BOX_PROOF` | Scope rejection only; no invented unstable box. |
| perturbation halfwidth sum at least one | `HOMOTOPY_BOUND_NOT_STRICT` | Rejects the specified sufficient proof condition, not necessarily stability. |
| change a Gram diagonal without changing the residual | `GRAM_COEFFICIENT_IDENTITY` | Detects a coefficient mismatch. |
| give a Gram diagonal a negative entry | `GRAM_NOT_PSD` | Detects non-PSD in this diagonal representation. |
| interchange distinct synthetic convex weights | `ZERO_HULL_AGGREGATE` | Tests the exact synthetic zero identity, not eligibility. |
| call the synthetic zero phase strictly positive | `ZERO_OR_NEGATIVE_PHASE_NOT_STRICT` | Distinguishes max zero from strict separation. |

## 6. Input coverage and exposure disclosure

Before reading scientific body I read, through their endings, manifest `05132f85bed61e406a919ecab687ebbe8ec66402a3c24c88e45608a2466bc1d8`, freeze `c0862c8c2c99dbd9b49a22ce945b9ee4bb2697c74005447fab2808d503ef543a`, final pre-dispatch binding `f1c7ef14634141ef3cdfbd855b3af42ac59f29adeccd57a35ba80b5252919f61`, prepared live metadata, actual dispatch, and all 21 listed permission/status controls. I independently observed the three assigned metadata hashes. I sent a direct PREBODY ACK to Main before packet access. I then read the sole ordered part in consecutive serial RAW windows of at most 20 LF through its ending, LF 1–325; its observed SHA-256 was `7c776fa3df1aa8075ea6cf786f38ea518f7f159d1192b1278eb5913bd52662b9`, size reported 45,669 bytes, within the frozen transport limit. This covers all rendered source bodies S1 LF 1–182, S2 LF 1–40, S3 LF 1–46, S4 LF 1–39. Parent binding reports complete source/packet roundtrip; I did not re-render source files or independently authenticate the original source identity.

I did not follow outgoing links or read sibling proofs, old checker code, held mathematical payloads, their methods, histories, or consumers. The assigned S1 is itself an unadopted author candidate; its prior exposure disclosure is not upgraded into independent verification. The adopted statuses of S2–S4 are as reported in the packet and remain at their exact written scopes. Only after the complete packet did I derive the explicit example, the finite logical control, and this prospective source. No child scientific executable, solver, test, build, lint, formatter, external-model CLI, Git, installation, deletion, network or heavy/paid work was used. No cognition-isolation certificate is asserted.

The program and these written calculations remain for full parent static read and separate disposition. Nothing here establishes the original universal both-parity ROOT triple, a universal strict common numerator, an eligible zero-hull/strict-negative witness, exact arbitrary-box computation, source equivalence, priority, novelty, or independent-family/human/kernel verification.
