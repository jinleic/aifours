# f395 WRITTEN review — conditional Boolean parity-rank-two bridge

**Disposition:** SUPPORTED at the explicitly conditional scope of S1 §7.  
**Findings:** 0 FATAL / 0 MAJOR / 0 MINOR within that scope.  
**Historical caller identification:** INCONCLUSIVE; not established by the supplied literal definitions.  
**Candidate adoption:** Not performed; remains a separate parent decision.

This is the complete review body for parent materialization. It does not adopt or independently certify the affine-support obstruction in S1 §§3–6.

## 1. Assignment, provenance, and complete-read audit

The reviewed wave is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f395-boolean-parity-rank2-four-small-fibre-bridge-written-review/`

Bindings supplied in the assignment and corroborated by the **parent’s** live metadata:

| Record | SHA-256 | Bytes | LF delimiters |
|---|---|---:|---:|
| `manifest-v1.json` | `cde1a8b0a146237b7fdb6c2568c0d3a2b5b67e021e7d312e5643bdd1f9766e4d` | 6090 | 102 |
| `freeze-receipt-v1.json` | `a58c0b64e04a068b89d4018d4223910449f5f6b8361fc06a5e36f325e378aa6a` | 2375 | 60 |
| `literal-packet-v1.md` | `263b287e6c0b9d6da7e494ebc24cc17279787e5a0d9a2ffe7c2da7ff7afebc63` | 38203 | 682 |

The parent metadata records `2026-10-30T10:35:40-0700 PDT`. This is **not** my native clock observation, research start, completion time, or independently executed hash check. I performed no native hashing, clock command, or byte-equality computation. The receipt’s equality/stability flags and the live matching-pin observation remain attributed to the parent.

### Read order

Before mathematical packet reads, I read:

1. The required memory summary and applicable review-protocol skills.
2. The complete manifest, LF 1–102.
3. The complete freeze receipt, LF 1–60.
4. All seven required status-only controls, including their endings:
   - `contract-addendum-2-frontier-first-owner-direction-v1.json`, LF 1–14.
   - `parent-L1-selected-diagnostic-release-quarantine-v1.json`, LF 1–23.
   - `parent-written-duty-execution-and-reporting-deviations-20261030-v1.json`, LF 1–28.
   - `parent-held-ph-registration-report-consumer-quarantine-v1.json`, LF 1–49.
   - `parent-ame-held-compression-claim-consumer-quarantine-v1.json`, LF 1–8.
   - `parent-core-gram-auxiliary-operator-diagnostic-quarantine-v1.json`, LF 1–9.
   - `parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1.json`, LF 1–11.
5. The dispatch receipt and complete parent live-metadata supply.
6. A direct administrative **pre-body ACK to Main**, before reading the mathematical packet.

I then read the complete packet consecutively in raw windows of at most 20 LF: 1–20, 21–40, continuing without gaps through 661–680, followed by 681–682. This included every source ending:

- **S1:** author candidate, source lines 1–630; SHA `3c18f0df77421c82e9c75962381d50f9202df6c69ad53b8c57f071b8062e70e5`, 21418 bytes, 629 LF delimiters.
- **S2:** caller-interface disposition, source lines 1–19; SHA `b1834337754499fbfdc5f0c1165dff8a1f44bcc5ff0420c1264f4624082afede`, 3824 bytes, 19 LF.
- **S3:** named-residual disposition, source lines 1–31; SHA `e09be9069bf8027bdb53e60a73c804f525b1c5c1953d517e417b5749b555ba09`, 8344 bytes, 31 LF.

The 630 numbered content lines of S1 are compatible with its recorded 629 LF delimiters; these are distinct counts. No packet elision was observed. After completing the packet, I made targeted raw rereads of §7 and the S3 caller statements.

No linked historical mathematical body, author code, sibling review/outcome, or held payload was opened. All quarantined episodes and their proof, selection, confidence, and planning consumers remained NONINPUT. No selected mathematical instance, scientific executable, CAS, interpreter, enumeration, replay, external-model CLI, or finite test was used.

## 2. Exact theorem reconstructed

Let \(E=\mathbb F_2^8\), and let an **actual** function

\[
u:E\longrightarrow\{0,\pm1\}
\]

satisfy

\[
|\operatorname{supp}u|=116,\qquad
\widehat u(r)\in4\mathbb Z,\qquad
|\widehat u(r)|\le12
\quad(r\in E).
\]

Here

\[
\widehat u(r)=\sum_{y\in E}u(y)(-1)^{r\cdot y}.
\]

Define

\[
\kappa(r)=\frac{\widehat u(r)}4,
\qquad q(r)=\kappa(r)\pmod2.
\]

Then:

1. \(q\) has Boolean algebraic degree at most two.
2. If the quadratic polar form of \(q\) has rank two, then
   \[
   \operatorname{wt}(q)=192.
   \]
3. Its zero set is one affine six-flat, whose direction is the radical of that polar form.
4. If additionally \(\sum_yu(y)=0\), this zero set contains zero and is the radical itself, a linear six-space.
5. **If the caller’s common fibre decomposition is identified with these radical cosets**, its three nonzero fibres have
   \[
   \kappa\in\{\pm1,\pm3\}.
   \]
   With the supplied normalization and the exact definition of the four-atom set \(A_2\), this gives the complete magnitude condition (M).

No affine-support obstruction is a premise of this theorem.

## 3. Reconstruction of the Boolean polynomial, including integrality

For each index set \(I\subseteq\{1,\ldots,8\}\), put

\[
m_I=\sum_{y\in E}u(y)\prod_{i\in I}y_i.
\]

Each \(m_I\) is an integer because \(u\) is an actual integer-valued function. On Boolean inputs,

\[
(-1)^{r_i y_i}=1-2r_i y_i.
\]

Consequently the following is an exact integer multilinear expansion:

\[
\widehat u(r)
=
\sum_{I\subseteq[8]}(-2)^{|I|}m_I\prod_{i\in I}r_i.
\]

After division by four:

- The constant coefficient is \(m_\varnothing/4\), integral because
  \(m_\varnothing=\widehat u(0)\in4\mathbb Z\).
- The coefficient of \(r_i\) is \(-m_{\{i\}}/2\). It is integral because
  \[
  \widehat u(e_i)-\widehat u(0)=-2m_{\{i\}}\in4\mathbb Z.
  \]
- The coefficient of \(r_i r_j\) is \(m_{\{i,j\}}\), automatically integral. Equivalently, it is the second finite difference
  \[
  \frac{\widehat u(e_i+e_j)-\widehat u(e_i)
  -\widehat u(e_j)+\widehat u(0)}4.
  \]
- For \(|I|\ge3\), the coefficient is
  \[
  (-1)^{|I|}2^{|I|-2}m_I,
  \]
  an even integer.

Thus the divided polynomial has integral coefficients before reduction modulo two, and every term of degree at least three vanishes after that reduction. Explicitly,

\[
q(r)\equiv
\frac{m_\varnothing}{4}
-\sum_i\frac{m_{\{i\}}}{2}r_i
+\sum_{i<j}m_{\{i,j\}}r_i r_j
\pmod2.
\]

This establishes the degree bound without treating division by four as an operation in \(\mathbb F_2\).

**Status:** SUPPORTED.  
**Source:** S1 lines 532–553, particularly the expansion and divisibility argument at 547–553.

## 4. Rank-two normal form, including a radical linear part

Define the polar form

\[
B_q(x,y)=q(x+y)+q(x)+q(y)+q(0).
\]

Because \(q\) has degree at most two, \(B_q\) is alternating and bilinear. Assume its rank is two.

Choose \(e,f\) with \(B_q(e,f)=1\), and write

\[
Z=\operatorname{rad}(B_q).
\]

The span of \(e,f\) is nondegenerate. Its orthogonal complement has dimension six and, since the entire form has rank two, equals \(Z\). Hence every vector has a unique expression

\[
x=ae+bf+z,\qquad a,b\in\mathbb F_2,\ z\in Z.
\]

For some \(\alpha,\beta,c\in\mathbb F_2\) and a linear functional
\(\ell:Z\to\mathbb F_2\),

\[
q(a,b,z)=ab+\alpha a+\beta b+\ell(z)+c.
\]

This form retains the possible linear component on the radical.

If \(\ell\ne0\), choose \(z_0\in Z\) with \(\ell(z_0)=1\). Translation by \(z_0\) exchanges zeros and ones, so \(q\) has weight \(128\).

If \(\ell=0\), then

\[
q(a,b,z)=(a+\beta)(b+\alpha)+\delta,
\qquad \delta=c+\alpha\beta.
\]

The product is one at exactly one of the four quotient points \((a,b)\). Therefore:

- \(\delta=0\) gives weight \(64\);
- \(\delta=1\) gives weight \(192\).

In the latter case, the zero set is the unique quotient point where that product is one, extended over \(Z\). It is one affine coset of the six-dimensional radical.

Thus the complete rank-two weight list is

\[
\boxed{\operatorname{wt}(q)\in\{64,128,192\}.}
\]

**Status:** SUPPORTED, including the radical-linear case.  
**Source:** S1 lines 543–555 and 569.

## 5. Parseval forces weight 192

Actual ternarity gives

\[
\sum_yu(y)^2=116.
\]

Unnormalized Walsh Parseval therefore yields

\[
16\sum_r\kappa(r)^2
=
256\cdot116,
\qquad
\boxed{\sum_r\kappa(r)^2=1856.}
\]

The cap and divisibility hypotheses imply

\[
\kappa(r)\in\{0,\pm1,\pm2,\pm3\}.
\]

At a point where \(q=1\), its square is at most \(9\). Where \(q=0\), its square is at most \(4\). Writing \(w=\operatorname{wt}(q)\),

\[
1856
\le9w+4(256-w)
=1024+5w.
\]

Hence \(5w\ge832\). Since \(5\cdot166=830<832\), integer \(w\) satisfies \(w\ge167\). Of the three rank-two possibilities, only \(192\) remains.

It follows that

\[
\boxed{\operatorname{wt}(q)=192,\qquad q^{-1}(0)=z_*+Z.}
\]

This is a necessary conclusion for every actual \(u\) under the hypotheses. It is not a construction or existence certificate for such a \(u\).

**Status:** SUPPORTED.  
**Source:** S1 lines 557–569.

## 6. Balance identifies a linear parity-zero space

If the actual caller is balanced in the stated sense,

\[
\sum_yu(y)=\widehat u(0)=0.
\]

Thus \(\kappa(0)=0\) and \(q(0)=0\). Since \(q^{-1}(0)\) is one coset of \(Z\) and contains zero,

\[
\boxed{q^{-1}(0)=Z.}
\]

The three other cosets of \(Z\) consist entirely of odd values of \(\kappa\).

The phrase **zero coset** here means the zero set of the parity function \(q\), not the Walsh-zero set. It has 64 points, which may have \(\kappa=0\) or \(\kappa=\pm2\). This conclusion neither asserts nor contradicts the separate eight-Walsh-zero hypothesis of the named residual.

**Status:** SUPPORTED.  
**Source:** S1 line 571; named eight-zero scope in S3 line 3.

## 7. Complete magnitude condition and the consuming-side boundary

This step requires an identification with the caller’s **same** common coordinates, not merely the existence of some quotient coordinates.

Suppose the spectral decomposition is

\[
E=R\oplus Q,\qquad \dim R=6,\quad\dim Q=2,
\]

with \(R=Z=q^{-1}(0)\). Use the dual decomposition of the actual input space and define

\[
U_s(c)=\sum_{w\in Q^*}u(c,w)(-1)^{s\cdot w}.
\]

Then the full transform and the fibre transform agree exactly:

\[
\widehat U_s(r)
=
\sum_cU_s(c)(-1)^{r\cdot c}
=
\widehat u(r,s)
=
4\kappa(r,s).
\]

The supplied caller normalization is

\[
\widehat U_s(r)=2k(r,s),
\]

so

\[
k(r,s)=2\kappa(r,s).
\]

For every nonzero fibre label \(s\), the parity result now gives, at **every** \(r\in R\),

\[
\kappa(r,s)\in\{\pm1,\pm3\},
\qquad
k(r,s)\in\{\pm2,\pm6\}.
\]

In particular, define the small-coefficient support on fibre 2 exactly as

\[
A_2=\{r\in R:|k(r,2)|=2\}.
\]

The supplied source defines \(A_2\) as this support and gives \(|A_2|=4\) (S3 line 3). Therefore

\[
|\widehat U_2(r)|
=
\begin{cases}
4,&r\in A_2,\\
12,&r\notin A_2.
\end{cases}
\]

This proves **complete** (M), not merely four small coefficients with an unspecified remainder.

Cardinality alone would not identify an arbitrary four-point set with the small-coefficient support. The support definition and normalization are essential imports.

**Status:** SUPPORTED under the explicit coordinate identification.  
**Sources:** S1 lines 73–80, 573–577; S3 lines 3 and 13.

### What the literal packet does and does not establish

S3 line 3 names an “even polar \(B\)” of rank two and states \(q^{-1}(0)=R\); however, the supplied body does not define that historical \(q\) as

\[
(\widehat u/4)\bmod2
\]

or define its \(B\) as the polar form reconstructed above. Equality of the names is insufficient to prove equality of these mathematical objects. Thus the §7 bridge does **not** independently establish that every historical named-rank-two caller satisfies its parity-rank and coordinate-identification hypotheses.

There is a separate documentary observation: **S3 line 13 explicitly supplies**
\(k\in\{\pm2,\pm6\}\) on the nonzero fibres. Together with S3 line 3’s definition and size of \(A_2\), that statement already supplies (M) **as an import at S3’s stated residual scope**. Using that scoped disposition statement is not a derivation identifying the historical polar with \(B_q\). This review does not reconstruct the historical derivation behind it.

Changing to a newly chosen radical-adapted decomposition does not, by itself, pay the identification gate for the original application: the four-point blocks, the fields \(U_s\), and their primal support geometry are defined by the chosen decomposition. They cannot silently be replaced while claiming a conclusion about the original common-coordinate caller.

**Historical rank/coordinate identification status:** INCONCLUSIVE, not REFUTED.  
**Source boundary:** S1 lines 579–588 and 619; S3 lines 3, 13, and 31.

## 8. Per-claim disposition

| Claim | Disposition | Source |
|---|---|---|
| \(q=(\widehat u/4)\bmod2\) has degree at most two | SUPPORTED | S1 532–553 |
| The divided polynomial has integral quadratic coefficients | SUPPORTED; explicit reconstruction above | S1 547–553 |
| Rank-two polar form permits weights \(64,128,192\), including a nonzero radical linear part | SUPPORTED | S1 555 |
| Parseval and the cap force weight \(192\) | SUPPORTED | S1 557–567 |
| The parity-zero set is one affine six-flat | SUPPORTED | S1 569 |
| Balance makes that six-flat linear and equal to the radical | SUPPORTED | S1 571 |
| Identified nonzero parity fibres have \(k\in\{\pm2,\pm6\}\) everywhere | SUPPORTED conditionally | S1 573–575; S3 13 |
| Exact small-support definition and \(|A_2|=4\) give complete (M) | SUPPORTED conditionally | S1 577; S3 3 |
| Historical “rank2” and common fibres are the reconstructed parity rank and cosets | INCONCLUSIVE; definitions not supplied | S1 581–588; S3 3, 31 |
| S3 directly supplies the complete nonzero-fibre magnitude set at its own scope | SUPPORTED as a scoped source import, not independently re-proved history | S3 3, 13 |
| All named actual rank-two callers are thereby excluded | NOT ESTABLISHED; not claimed by the reviewed bridge | S1 585–588, 619–622 |

No assigned mathematical claim was refuted. The explicit unresolved historical import is a correctly retained boundary, not a defect requiring a finding.

## 9. Exact acceptance ceiling

The reconstructed result concerns **actual ternary \(u\)**. Its energy identity uses actual support size 116, and its polynomial derivation uses the integer moments of that actual function. It does not turn a spectral shadow, projected sign assignment, or formal placement into an actual \(u\).

This review establishes neither:

- the affine-support obstruction in S1 §§3–6;
- a full actual \(U/V\) witness;
- feasibility or exclusion of the entire \(m=116\) residual;
- historical equivalence of the rank conventions;
- a global complement satisfying all remaining conditions;
- the \(m=114\) cases, other class-count pairs, rank two generally, or balanced NL242;
- novelty, human verification, independent-model-family verification, or formal/kernel verification.

The non-affine-support and global-complement gates remain outside this assignment. No held output has been rehabilitated.

## 10. Execution, artifacts, and final verdict

No finite code was assigned to this WRITTEN role. No scientific code was authored or run, and there is no stdout, finite-check result, or machine certificate to report. No build, test, lint, formatter, installation, deletion, commit, push, or publication occurred.

The role’s read-only restrictions provide no permitted route to write `review-v1.md` in the repository. This complete returned body is supplied for parent materialization; no write bypass was attempted.

**overall_correctness:** correct — at the explicit conditional §7 scope.

**explanation:** The parity-polynomial construction, full rank-two normal-form classification, Parseval weight bound, balanced zero-coset conclusion, and conditional derivation of complete (M) all reconstruct correctly. The historical rank/common-coordinate identification remains unestablished, as the candidate expressly acknowledges; no whole-candidate or residual acceptance follows from this review.

**confidence:** 0.98.