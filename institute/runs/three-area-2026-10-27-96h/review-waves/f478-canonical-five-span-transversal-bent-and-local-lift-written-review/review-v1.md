# F478 WRITTEN review: canonical five-span transversals, bent equivalences and local ternary lifts

## Result and scope

**0 FATAL / 0 MAJOR / 0 MINOR mathematical findings in the reconstructed written claims.**

- **SUPPORTED:** conditional normalized five-span graph necessity; both exact Fourier equivalences; the parametric 116-nonzero ternary local lift with the explicitly defined local \(H=0\).
- **INCONCLUSIVE / NOT_RECONSTRUCTED independently:** the finite census, execution assertions, ANF-degree census, and availability of a compatible phase for every one of the reported 896 graphs.
- No mathematical refutation was found.

This is not blanket acceptance of S1, an original-caller existence result, or a solution of the balanced NL242 problem.

Repository materialization of `review-v1.md` was attempted and refused by the tool’s path restriction. No repository file was written. This complete body is returned for parent materialization and disposition, without bypass or automatic adoption.

## Administrative record and coverage

**Role:** WRITTEN.

The complete manifest, freeze receipt, ten status-only controls, parent dispatch receipt, and parent live metadata supply were read before the administrative pre-body ACK. That ACK preceded the first mathematical packet read.

The packet was then read raw and sequentially, without mathematical derivation between windows, at LF:

- 1–20
- 21–40
- 41–60
- 61–80
- 81–100
- 101–120
- 121–140
- 141–152

Coverage is **S1:1–76, S2:1–37, and S3:1–37**, including every ending. No elision was present.

**Frozen metadata:**

- Manifest SHA: `7f5a91266bf8b7ee310476d39f4d602b3633c553dfd6d3107fa5ea39ff740369`
- Receipt SHA: `5205d87a8d685cb2ac53a0c64e94563034aa4f71fc4652cd2d7e37e6e106aed8`
- Packet SHA: `b67727027816329e16d8e090eaeac06e8f7b078fd1ccd7ea61d2d632160f4d80`
- Packet: 23,086 bytes, 152 LF.

These hashes, sizes, and clocks are **parent-supplied observations**, not child-native hash/date measurements. The supplied parent clock is `2026-10-30T12:13:16-0700 PDT`; it is not a completion timestamp for this review. No child-native completion clock is claimed.

**Source pins supplied by the frozen records:**

- S1: `642e16f3042fcfed6efd97ec84bd13b6aaa41cd2c0a470756d5a21ec611e56b1`
- S2: `2aa39512cf0ef6d1194cc8257dfe722cf9a58b62f637baf9056e08355b4423f0`
- S3: `43b0033914ef23e050ceb3628a61ccf75605d5a5c97f13da286dec4cabce29d6`

Source coverage means the complete literal bodies displayed in the frozen packet, not an independent live-source hash check.

No selected mathematical instance, scientific execution, code/CAS/interpreter/solver/enumeration/replay, new mathematical source, sibling review, author code, held payload, external-model CLI, build, test, lint, or formatter was used. The formulas below use the supplied formal parameters and explicitly assigned coordinates only. Quarantines were read only for status; no excluded links were followed. No cognition/provenance-isolation certificate is asserted.

## Imports retained at their exact scope

**S2:7–15,23,27,31** supplies the actual-object two-fibre necessities, normalized small-frequency signs, five-coset saturation, and five-span occupancy. In particular:

- \(U_1=3a\);
- \(a\) has 16 signs on \(S\);
- \(|\widehat a|=4\) everywhere;
- \(|\widehat g|=4\) at the four named \(A\) frequencies and 12 elsewhere;
- actual blocks give \(g=\pm1\) on \(S\) and \(g\in\{0,\pm2,\pm4\}\) off \(S\);
- five-span occupancy is \((0;4,4,4,4)\), with both full blocks in \(E\).

The earlier nonzero-XOR/dichotomy theorem is imported, not reproved from linked author, reviewer, or code files.

**S3:7–17,21–23** fixes the actual-block and explicit local-\(H\) interface. Its affine-support exclusion remains an earlier scoped import, not a new result of this review. Its historical rank/\(H\) equivalence caveats remain intact.

No previous reviewer rating, finite-check output, or exclusion outside these named import scopes is used as fresh proof evidence.

## Claim 1 — Normalization and fixed signs

**Status: SUPPORTED conditionally.**

**References:** S1:7–15; S2:7–15,23,31.

The inherited common operations act on the same actual \(u\), rather than separately on \(a\) and \(g\). The additional affine change on \(h\) sends the two distinct full blocks of \(E\) to \(0\) and \(1\). Since the exceptional four frequencies have zero \(h\)-frequency, an \(h\)-only translation/linear change preserves their positions and positive signs. This does not restore an original balance condition that inherited modulation may have changed.

The displayed \(g\)-signs also follow directly. For every normalized \(c=(h,d)\), inverse Fourier inversion reduced modulo three gives

\[
g(h,d)\equiv
\sum_{r\in\{0,1,2,4\}}(-1)^{r\cdot d}\pmod 3,
\]

because \(64\equiv1\) and \(4\equiv1\pmod3\), while every other full coefficient is divisible by three.

- On \(E\), the residue is \(1\). The two full values are therefore \(+4\), and the other six values are \(-2\).
- On \(d=1,2,4\), the residue is \(-1\). The support values are therefore \(-1\), and the nonfull off-support values are \(+2\).
- On \(d=7\), these signs reverse.
- On the remaining \(d\)-cosets, the residue is zero, and the allowed even off-support values force \(g=0\).

This reproduces \(\rho=(-1,-1,-1,+1)\) and

\[
g(h,d_b)=\rho_b\bigl(-2+3\mathbf1_S(h,d_b)\bigr).
\]

There is no independently selectable \(B\)-sign. The count four in every \(B\)-slice is inherited for every actual five-span object.

## Claim 2 — Every support slice is a transversal

**Status: SUPPORTED.**

**References:** S1:19–26.

For all \(h\)-frequencies \(y\), the \(E\)-contribution is

\[
G_0(y)=-16\mathbf1_{\{y=0\}}+
6\bigl(1+(-1)^{y\cdot1}\bigr).
\]

Thus every nonzero \(y\in1^\perp\) has \(G_0(y)=12\). Such \(y\) cannot be an exceptional small-frequency row. Every one of its eight full coefficients therefore belongs to \(\{-12,+12\}\); their average is \(G_0(y)=12\), forcing all eight to equal \(+12\). Inverting the \(d\)-transform gives \(G_d(y)=0\) for \(d\ne0\).

For each fixed \(B\)-slice, define

\[
n_b(j)=\mathbf1_S(2j,d_b)+\mathbf1_S(2j+1,d_b).
\]

Its three nontrivial quotient Walsh coefficients vanish by the preceding identity, while its trivial coefficient is four by inherited occupancy. Fourier inversion gives \(n_b(j)=1\) for every \(j\).

Hence the complete support is uniquely parametrized by

\[
S=\{(2j+f(j,b),d_b):j,b\in\mathbb F_2^2\}.
\]

The argument uses **all three nonzero elements of \(1^\perp\)** and applies to every normalized actual five-span caller, not merely to a selected collection of slices.

## Claim 3 — Complete \(g\)-spectrum iff \(f+q\) is bent

**Status: SUPPORTED.**

**References:** S1:30–36.

Use exactly the supplied coordinates

\[
d_b=1+3b_0+5b_1,\qquad
q(b)=1+b_0b_1,\qquad
y=1+2v,\qquad
w(z)=(z\cdot3,z\cdot5),
\]

with binary-vector addition. Then

\[
\rho_b=(-1)^{q(b)},\quad
y\cdot(2j+f)=v\cdot j+f,\quad
z\cdot d_b=z\cdot1+w(z)\cdot b.
\]

For every odd \(y\), the \(E\)-contribution vanishes, and the constant part of each \(B\)-slice has zero \(h\)-transform. Consequently,

\[
\widehat g(1+2v,z)
=3(-1)^{z\cdot1}W_{f+q}(v,w(z)).
\]

The vectors \(3\) and \(5\) are linearly independent, so \(w\) is onto \(\mathbb F_2^2\). Every one of the sixteen Walsh frequencies of \(f+q\) is tested, not merely a projection. The required magnitude 12 on these rows is equivalent to all these Walsh magnitudes being four.

The other rows are completely accounted for:

- Nonzero even \(y\) has every coefficient \(+12\), by Claim 2.
- At \(y=0\), \(G_0=-4\) and \(G_{d_b}=-4\rho_b\), so

\[
\widehat g(0,z)
=-4+4\!\left[
(-1)^{z\cdot1}+(-1)^{z\cdot2}+(-1)^{z\cdot4}
\right]-4(-1)^{z\cdot7}.
\]

This is \(+4\) precisely for \(z\in\{0,1,2,4\}\), and \(-12\) at the remaining four \(z\).

No additional small-frequency or sign condition is omitted. Conversely, any graph \(f\) with \(f+q\) bent, inserted into the fixed \(g\)-table, satisfies the entire 64-position magnitude condition.

## Claim 4 — Complete flat \(a\)-spectrum iff \(r\) and \(r+f\) are bent

**Status: SUPPORTED.**

**References:** S1:38–43.

For the same graph and its one common support sign function \(r\), the complete transforms are

\[
\widehat a(2v,z)
=(-1)^{z\cdot1}W_r(v,w(z)),
\]

\[
\widehat a(1+2v,z)
=(-1)^{z\cdot1}W_{r+f}(v,w(z)).
\]

The even and odd \(h\)-rows exhaust all \(h\)-frequencies; surjectivity of \(w\) exhausts all four-variable frequencies in each half. Thus

\[
|\widehat a|\equiv4
\quad\Longleftrightarrow\quad
r\text{ and }r+f\text{ are both bent}.
\]

The same \(r\) appears in both conditions. This is genuinely a common-phase compatibility condition, not independently assigned spectra.

## Claim 5 — Finite census and non-affine classification

**Status: INCONCLUSIVE independently.**

**References:** S1:45–62,74; manifest audit.

The \(896/512/384/384\) census, 344,064 pair total, quadratic-degree assertion, complete phase availability for every surviving graph, execution timing, control outcomes, and program-input assertions are parent-reported finite evidence.

This WRITTEN review neither opened the linked program/receipt nor enumerated or replayed anything. Those assertions receive **no independent numerical, execution-safety, or finite-certificate validation here**. S1 expressly distinguishes parent authorship/execution from independent checking, so this limitation is not a mathematical finding against the manuscript.

The geometric implication at S1:62 is supported conditionally: projection from a graph onto \((j,b)\) is bijective onto \(\mathbb F_2^4\); an affine four-flat graph would make its output coordinate \(f\) affine. Thus a non-affine graph contained in this affine five-flat has affine span exactly five.

For actual callers, the earlier S2:23 exact-five-span import already supplies the actual branch’s dimension. This does not independently establish the stated ANF census or its all-graph consequence.

## Claim 6 — Actual ternary support blocks

**Status: SUPPORTED parametrically.**

**References:** S1:64–68.

**Quantifiers:** for any \(f,r\) satisfying the three bent conditions above, construct the same \(a,g\), then a ternary \(u\) block by block. This is a conditional construction for every such pair; a count of all such pairs is unnecessary for its proof.

On each support block, let

\[
\alpha=a(c)\in\{-1,+1\},\qquad
\gamma=g(c)\in\{-1,+1\},\qquad
t(w)=\chi_1(w)\chi_2(w).
\]

The nontrivial character \(t\) has two points of each sign. Choose any \(w_0\) with \(t(w_0)=-\gamma/\alpha\), set \(u(w)=\alpha\chi_1(w)\) except at \(w_0\), and set that entry to zero. Exactly two omissions are admissible. Orthogonality gives

\[
U_1=3\alpha,\qquad
U_2=\alpha\sum_{w\ne w_0}t(w)
=-\alpha t(w_0)=\gamma.
\]

Thus this block has exactly three actual ternary nonzeros with the desired simultaneous two-fibre values.

For each full block, \(\gamma/4\) is a sign, and \(u=(\gamma/4)\chi_2\) gives \(U_1=0,U_2=\gamma\), with four nonzeros.

For each remaining nonzero \(g\)-block, \(\gamma=\pm2\). Choosing one point of each \(t\)-sign class and setting \(u=(\gamma/2)\chi_2\) on those two points gives

\[
U_1=(\gamma/2)(1-1)=0,\qquad U_2=\gamma.
\]

Every entry belongs to \(\{-1,0,+1\}\). These are physical local blocks, not merely a list of putative transforms.

## Claim 7 — 116 nonzeros and explicit local \(H=0\)

**Status: SUPPORTED.**

**References:** S1:68–70; S3:7.

There are 16 support blocks. The eight \(E\)-blocks consist of two full blocks and six nonfull blocks; the 32 \(B\)-blocks consist of 16 support blocks and 16 nonfull blocks. Thus exactly 22 nonzero \(g\)-blocks remain off \(S\). These give

\[
16\cdot3+2\cdot4+22\cdot2=100
\]

nonzeros.

The other 24 blocks have \(a=g=0\). On any eight distinct such blocks, the pair \(w,w+(1,1)\) with equal nonzero entries cancels both \(\chi_1\) and \(\chi_2\). It therefore changes neither \(U_1\) nor \(U_2\) and adds exactly two nonzeros. The total is 116. The remaining 16 inactive blocks stay empty.

Every \(U_1=0\) block has support at most two, and therefore \(|U_0|\le2\), except the two full blocks. Those full blocks are multiples of the nontrivial character \(\chi_2\) and have \(U_0=0\).

Hence no \(U_1=0\) block has \(|U_0|=4\), and the **specifically defined local \(H\) is zero**. This does not identify local \(H\) with an undisplayed historical convention.

## Consumer boundary and remaining obligations

The graph \(f\) and its shared phase \(r\) are consumed explicitly by both Fourier calculations and by the physical-block construction. The local lift preserves the complete \(U_1,U_2\) values, rather than only one projected spectrum.

The construction does not forward a claim of global acceptance. S1:70,74,76 expressly stops at local lifts and retains the unpaid original-caller obligations.

In particular, neither the proof nor its local-\(H\) result establishes:

- the \(U_0,U_3\) Walsh conditions;
- original balance;
- the full rank/eight-zero/\(T\) interface;
- simultaneous four-fibre constraints;
- a shared complementary 140-support \(V\);
- the global odd-fibre caps.

The two six-span branches, other m116/m114 callers, and balanced NL242 remain open at the stated scope.

No physical support/phase consequence is imported from an AME weak graph; no incompatible four-qubit marginals are asserted; no Song–Chen/H2 novelty claim is made. No independent-family, human, formal-kernel, source-wide authenticity, novelty, or global exclusion credit is given.

## Findings and verdict

**FATAL: 0. MAJOR: 0. MINOR: 0.**

**Overall correctness:** correct.

**Explanation:** The normalized five-span graph necessity, exact bent equivalences, and parametric 116-support ternary local lift reconstruct with consistent coordinates, signs, and quantifiers. This verdict is limited to those conditional written claims: the parent finite census and existence for every reported graph remain independently unverified, and no original balanced caller or complement is accepted.

**Confidence:** 0.96 for the written reconstruction at precisely that scope. No confidence rating is assigned to unreviewed program or execution claims.