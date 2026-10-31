# f405 — Written source-alignment review

## Verdict

**SUPPORTED:** The explicitly defined actual residual adopted in f263 entails f384’s complete second-fibre magnitude hypothesis **(M)**, in the same shared coordinates. This is a **direct named import from f263**, followed by the displayed normalization identity. It does not require identifying an unspecified historical meaning of “rank two” with the separate parity-rank definition in f384 §7.

The required actual ternary \(u\), sixteen-block \(U_1\) support, and local \(U_2\) value restrictions transfer at that same scope. **Affineness of the sixteen-block support is not an inherited fact:** it is the additional family condition that f384 proposes to exclude.

**Findings at the reconstructed source-alignment scope: 0 FATAL / 0 MAJOR / 0 MINOR.** This is not a review or adoption of f384’s obstruction proof.

## 1. Process, bindings, and coverage

I read the complete manifest, freeze receipt, dispatch receipt, parent metadata supply, and all seven listed status-only controls before opening the mathematical packet. An administrative pre-body ACK was delivered to Main before the first packet read.

I then read the entire literal packet in consecutive raw windows of at most twenty lines: packet lines 1–1160 in twenty-line windows, followed by 1161–1164. This included all endings: S1 through source line 24, S2 through 31, S3 through 477, and S4 through 630. Targeted rereads of the already permitted S2 followed the complete read.

The supplied bindings are:

- Manifest: `4619b79751d3ad3ef0634857c09c1467f6f7b0e9eeddd8c98a3834a632f98780`
- Freeze receipt: `86766f4cff8928888dcbaf57ea01caa1682815e9fa36723665e7bd7ea6f002c5`
- Literal packet: `c70ec8d9ad399a90fd84d9bde890ed3a1c5c7803b79237a7b38c3d8b54b0e9ee`

The clock **2026-10-30T10:39:50-0700 PDT**, and the live hash/byte/LF matches, are **parent-supplied observations** from `parent-live-metadata-supply-v1.json`, not checks or a native start time executed by this reviewer. No independent reviewer-native clock or cadence certificate is claimed.

No scientific executable, CAS, interpreter, enumeration, selected mathematical probe, external-model CLI, or public-source search was run. No excluded historical body, held payload, sibling outcome, f239/CR7 source, or linked control payload was opened. Historical execution descriptions appearing inside the permitted dispositions were not replayed or treated as this reviewer’s verification.

Repository writes are prohibited by this reviewer role. This is the complete review body for parent materialization as the wave’s `review-v1.md`; no repository write or bypass was attempted.

## 2. Exact sources and inherited scope

All paths below are relative to:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`

| Source | Pinned path | SHA-256 |
|---|---|---|
| S1 | `dispositions/info-6-nl242-rank2-eightzero-116-fibre-048-obstruction-parent-v1.md` | `18403a17269311682255e3bb9823a89a0a69cd7344a66ad02bdd841bcc52f912` |
| S2 | `dispositions/info-6-nl242-rank2-eightzero-116-fibre-048-residual-10-cross-fibre-parent-v1.md` | `e09be9069bf8027bdb53e60a73c804f525b1c5c1953d517e417b5749b555ba09` |
| S3 | `review-waves/f365-balanced-original-u-v-after-coset-exclusion/review-v1.md` | `2355e1c4acfeccba991c2ddd2dd5e6d61aa44625920f1564364a6c12db6b8b9f` |
| S4 | `review-waves/f384-balanced-actual-global-caller-completion-frontier/review-v1.md` | `3c18f0df77421c82e9c75962381d50f9202df6c69ad53b8c57f071b8062e70e5` |

Let \(\mathcal D_{263}^{\mathrm{explicit}}\) denote the **actual original Boolean callers at S2’s adopted scope**, not a relaxation consisting only of spectral arrays or support placements. Its hypotheses are:

- \(f:\mathbb F_2^9\to\mathbb F_2\) is balanced and \(\max|W_f|\le28\);
- the named even polar \(B\) has rank two;
- there are exactly eight Walsh zeros;
- \(m=116\);
- the ordered nonzero-fibre pattern is \((e_1,e_2,e_3)=(0,4,8)\);
- \(T\ne0\) and \(q^{-1}(0)=R\), as explicitly imported in S2;
- \(G_3=1\);
- \(H=0\), **where \(H\) means the number of \(U_1=0\) blocks whose local transform is a single \(|U_0|=4\) peak**.

This is S2:3’s scope. In particular, I do **not** replace its explicit \(H\) definition with an undisplayed historical class convention. S2:17 and 23 expressly withhold that historical equivalence.

S1:3–9 supplies the preceding f244 caller/count frontier; it does not by itself eliminate the explicit-definition qualification in S2.

## 3. Direct derivation of (M)

### 3.1 The required complete magnitude information is explicit

S2:3 defines:

- \(A_2\): the four atoms forming the \(|k|=2\) support in the second nonzero fibre;
- \(A_3\): the corresponding eight atoms in the third fibre;
- both in **one shared \(R\)-coordinate system**.

S2:13 states, without requiring reconstruction of a historical rank convention:

\[
k(r,s)\in\{\pm2,\pm6\}
\quad\text{on every nonzero fibre},
\]

and

\[
2k(r,s)=\sum_{c\in R^*}U_s(c)(-1)^{r\cdot c}.
\]

Consequently, for the labelled second fibre,

\[
A_2=\{r\in R:|k_2(r)|=2\},
\qquad |A_2|=4,
\]

and, because the only remaining allowed magnitude is six,

\[
|k_2(r)|=
\begin{cases}
2,&r\in A_2,\\
6,&r\notin A_2.
\end{cases}
\]

This specifies **all sixty-four frequencies**, not merely the four exceptional positions.

### 3.2 The factor of two is the same normalization

S2:13 uses the shared dual decomposition

\[
K=R\oplus P,\qquad V\simeq R^*\oplus P^*.
\]

Identify \(Q\) in S3/S4 with this same \(P\), retaining the ordered nonzero labels. The local transform is then

\[
U_s(c)=\sum_{w\in Q^*}u(c,w)\chi_s(w),
\]

exactly as displayed in S3:70–80 and S4:68–80. Its unnormalized sixty-four-point transform is

\[
\widehat U_s(r)=2k_s(r).
\]

There is no normalized-versus-unnormalized conversion left unpaid.

Taking absolute values gives

\[
\boxed{
|\widehat U_2(r)|=
\begin{cases}
4,&r\in A_2,\quad |A_2|=4,\\
12,&r\notin A_2.
\end{cases}}
\]

This is precisely S4:12–25’s **(M)**.

The exact transcribed implication is therefore

\[
\boxed{
f\in\mathcal D_{263}^{\mathrm{explicit}}
\ \Longrightarrow\
\left[
\begin{aligned}
&A_2=\{r:|k_2(r)|=2\},\quad |A_2|=4,\\
&k_2(r)\in\{\pm2,\pm6\}\quad(\forall r\in R),\\
&\widehat U_2(r)=2k_2(r)\quad(\forall r\in R)
\end{aligned}
\right]
\ \Longrightarrow\ (M).
}
\]

This is an implication about necessary data of every actual caller in the named residual. It asserts neither existence of such a caller nor exclusion of the residual.

## 4. Actual \(u\), flat fibre, and block restrictions

### 4.1 Actualness and the two different support sizes

S2:13 supplies the original-object ternary pair function

\[
u(y)=\frac{\varepsilon(y)+\varepsilon(y+T)}2,
\qquad \varepsilon(y)=(-1)^{f(y)},
\]

on the inherited \(V=a_0^\perp\), with

\[
\sum u=0,\qquad |\operatorname{supp}u|=116.
\]

It also supplies

\[
U_1(c)\in\{0,\pm3\},\qquad
S:=\{c:U_1(c)\ne0\},\qquad |S|=16.
\]

Thus **116 counts nonzero entries of \(u\)**, whereas **16 counts blocks supporting \(U_1\)**. Neither is a constructed or relaxed realization. These are the facts used in S3:86–103 and S4:82–101.

### 4.2 Flatness of \(k_1\) transfers

The same normalization and the sixteen \(\pm3\) values give

\[
\frac1{64}\sum_r k_1(r)^2
=\frac14\sum_c U_1(c)^2
=\frac14(16\cdot9)
=36.
\]

Every \(k_1(r)^2\) is at most \(36\), by S2:13’s complete nonzero-fibre magnitude statement. Therefore every term equals \(36\):

\[
k_1=6\sigma,\qquad \sigma:R\to\{\pm1\}.
\]

With \(a=U_1/3\),

\[
\widehat a=4\sigma,\qquad \widehat\sigma=16a.
\]

These are exactly S3:88–103’s flat-fibre conventions and the support data used in S4:487–490. They concern flat **spectral magnitude**; they do not say that \(S\) is an affine flat.

### 4.3 The local values needed by f384 follow from actual blocks

For \(c\in S\), the four ternary summands in

\[
U_1(c)=\sum_wu(c,w)\chi_1(w)=3a(c)
\]

must have exactly three nonzero entries, aligned after multiplication by \(\chi_1\). There is a unique missing point \(w_0(c)\), and

\[
u(c,w)=a(c)\chi_1(w)\quad(w\ne w_0(c)).
\]

For \(s\ne1\), character orthogonality gives

\[
U_s(c)=-a(c)\chi_{s+1}(w_0(c)).
\]

In particular,

\[
U_2(c)\in\{\pm1\}\qquad(c\in S).
\]

For \(c\notin S\), \(U_1(c)=0\). Modulo two, this equals the parity of the number of nonzero entries of the actual block. That number is therefore even, so \(U_2(c)\) is an even integer of magnitude at most four:

\[
U_2(c)\in\{0,\pm2,\pm4\}\qquad(c\notin S).
\]

These are S4:89–101’s required restrictions, also consistent with S3:106–118. No hole-map condition, sign-template condition, relaxed inverse array, or completion of the other forty-eight blocks was substituted for actual \(u\).

For completeness, S2:5 also explicitly supplies \(X(A_2)\ne0\), the additional source fact cited in S4:416–420. This observation does not review S4’s supplementary accounting proof.

## 5. Coordinate and permutation orientation

### Nonzero-fibre labels

S1:3 allows the \((0,4,8)\) pattern up to permutation. S2:3 fixes the orientation:

\[
e_1=0,\qquad e_2=4,\qquad e_3=8.
\]

S3:59 retains \(1=2+3\). A simultaneous relabelling of the three nonzero elements of \(\mathbb F_2^2\) is compatible with this relation. The zero fibre remains fixed.

The import must use this **single consistent labelling**. It would not be justified to exchange \(A_2\) and \(A_3\) while retaining their old cardinalities or leave the \(U_s\) labels unchanged.

### Shared \(R\)-coordinates and complement changes

S2:15 explicitly describes the change of complement determined by a linear map \(L:P\to R\):

\[
U'_s(c)=(-1)^{L(s)\cdot c}U_s(c).
\]

Its consuming-side Fourier identity is

\[
\widehat U'_s(r)
=\widehat U_s(r+L(s))
=2k_s(r+L(s)).
\]

Accordingly,

\[
k'_s(r)=k_s(r+L(s)),\qquad
A'_s=A_s+L(s).
\]

Thus the signs, frequency positions, and local transforms move together. For the displayed shear \(L(2)=t,\ L(3)=0\), \(A_2\) becomes \(A_2+t\) and \(A_3\) stays fixed, exactly as S2:15 states. Absolute block shapes and the support \(S\) are unchanged.

An invertible change of primal \(R^*\)-coordinates induces the corresponding dual frequency permutation; a primal translation multiplies the Fourier transform by a character. These preserve (M), the cardinality of \(S\), and whether \(S\) is affine. Therefore f384’s coordinate choice placing an **assumed affine** \(S\) at a standard four-flat does not create a source-alignment mismatch.

No independent sorting or reorientation of the fibres is needed or licensed.

## 6. Direct import versus f384 §7

There are two different statements.

**Direct named import — SUPPORTED.**  
For \(\mathcal D_{263}^{\mathrm{explicit}}\), S2:3 and 13 already state the complete magnitude alternatives, exceptional-set size, and transform normalization needed for (M).

**Historical parity-rank identification — INCONCLUSIVE and unnecessary here.**  
S4:530–577 introduces a separate lemma using

\[
\kappa=\widehat u/4,\qquad q_{\mathrm{par}}=\kappa\bmod2,
\]

and the quadratic polar rank of that explicitly defined parity function. S4:579–588 correctly distinguishes this definition from an unspecified historical convention.

The present source alignment does not establish that the historical \(q\) and \(B\) are precisely \(q_{\mathrm{par}}\) and its polar form. Establishing that identity would require the missing original definitions and their identification with the same common fibres—not merely the word “rank two.” This task neither reconstructs nor adopts that separate lemma.

Accordingly, the proposition that **(M) remains unpaid for the exact f263 caller now frozen in f405** is **REFUTED by S2’s explicit statements**. This does not establish that f384’s caution was erroneous relative to its own earlier packet. The newly available direct source route is enough for the present named application.

Likewise, equality of the explicit local \(H\) with every undisplayed historical \(H\)-class convention remains **INCONCLUSIVE**. Matching count equations in S2:17 does not, by itself, supply that missing definition.

## 7. Claim ledger

| Claim | Status | Source anchors |
|---|---|---|
| The named f263 actual residual has four second-fibre \(|k_2|=2\) atoms and \(|k_2|=6\) everywhere else | **SUPPORTED as an explicit import** | S2:3, 13 |
| \(\widehat U_2=2k_2\) uses the same shared coordinates and unnormalized transform as f365/f384 | **SUPPORTED** | S2:13; S3:53–80; S4:68–80 |
| The named caller entails complete (M) | **SUPPORTED; implication reconstructed above** | S2:3, 13; S4:12–25 |
| Actual ternary \(u\), sixteen \(U_1=\pm3\) blocks, and the required \(U_2\) value restrictions transfer | **SUPPORTED** | S2:13; S3:86–118; S4:82–101 |
| The inherited support \(S\) is already affine | **NOT SUPPORTED**; it is an extra family hypothesis | S4:103–118 |
| Historical \(H\) and parity-rank conventions are fully identified | **INCONCLUSIVE** | S2:17, 23; S4:579–588 |
| f384’s core obstruction is proved or adopted by this review | **NOT REVIEWED** | Outside the frozen audit scope |
| The whole residual or balanced NL242 target is excluded | **NOT ESTABLISHED** | S2:21; S4:607, 619–630 |

## 8. Exact conditional composition and unpaid steps

The permissible composition is

\[
\boxed{
\begin{gathered}
\text{For every }f\in\mathcal D_{263}^{\mathrm{explicit}},
\text{ its actual }u\text{ satisfies f384's block hypotheses and (M)};\\
\text{if f384's core obstruction is independently reviewed and adopted,}\\
\text{then every such caller has non-affine }S.
\end{gathered}}
\]

The latter conclusion would give \(\dim\operatorname{aff}(S)\ge5\), since \(|S|=16\); it would not exclude callers with affine-span dimension five or six.

Still unpaid:

1. Independent mathematical review and separate parent adoption of f384’s obstruction proof and any structural corollary being promoted.
2. Construction or exclusion of the remaining non-affine actual-\(U\) cases.
3. Any required global actual-\(V\) complement and odd-cap analysis for surviving \(U\).
4. Other f244 count pairs, other fibre patterns, \(m=114\), rank two generally, and the full balanced nine-variable NL242 target.
5. Historical class/parity-definition equivalences, if separately desired.
6. Novelty or priority verification.

**Overall correctness: correct at the source-alignment-only scope.** The exact f263 source supplies (M) and the required actual-block data without an unspecified historical-convention import. Composition with f384 remains conditional on its separate proof review and adoption.

**Confidence: 0.99** for this bounded source-alignment conclusion. Same-harness written review only; not independent-model-family, human, formal/kernel, executable, or novelty verification.