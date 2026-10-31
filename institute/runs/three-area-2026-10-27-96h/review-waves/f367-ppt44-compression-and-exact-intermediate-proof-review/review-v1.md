# f367 — Complete written review with additive clock qualification

**Scoped verdict: SUPPORTED. Candidate findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

The supplied S1 §§3–4 arguments correctly establish:

1. \(R/25\) is an actual \(4\times4\) PPT state with Schmidt number exactly \(2\).
2. Every PSD completion of its specified separable codimension-one compression has Schmidt number at most \(2\), including singular and zero cores and arbitrary complex coherent completion blocks consistent with positivity.
3. The broader specified retained-block PPT family also has Schmidt number at most \(2\).

The general local-extension lemma and intermediate-state SN-\(2\) conclusion are already present in the supplied primary source. **No novelty, unrestricted \(4\times4\) no-go, original-target acceptance, or verdict on the separately assigned public Eq. (6) claim is granted.**

## 1. Additive clock and process qualification

The fresh observation **`2026-10-30T09:39:07-0700 PDT` was supplied by Main**. It was received after my first complete written review return. It is recorded additively, not backdated as my start, private derivation, completion time, or child-native execution. It does not change any scientific finding below.

Before mathematical packet reads, I read the complete manifest, freeze receipt, all seven named status/permission controls and their endings, and the complete parent metadata supply, then sent the required direct pre-body ACK.

I subsequently read the entire ordered packet, physical lines **1–630**, in raw windows of at most 20 LF, including S1’s final source record 502 and every S2–S5 ending. One mistyped-path request failed; its intended window was immediately recovered from the correct path. The dispatch receipt was also read.

All hashes, byte counts and native clocks are **parent-supplied observations**, not independently executed reviewer metadata:

- Manifest: `84899e86cd94dd197e42b1e1e96cd63de2ff3a16f14829a358f17e9bd33e2e7d`
- Freeze receipt: `e0bf8de5758b52df0c6f408798eb15bef512a097254eefbe169953924e94b692`
- Packet: `38fcbbf71bea16297dedfa06f26df0606f8005aa2bf9c4cce964666f52a8d151`
- Earlier parent metadata observation: `2026-10-30T09:31:55-0700 PDT`
- Fresh parent observation: `2026-10-30T09:39:07-0700 PDT`

No scientific executable, CAS, interpreter, solver, scan, replay, or additional selected mathematical instance was used. No sibling output, held f337 payload, held parent mathematical payload, author checker, or linked prior review body was opened.

The assignment disclosed the proposed claims before the packet read; this is not blind review. The manifest discloses the parent’s pre-freeze candidate preview. S1’s own earlier-author chronology at LF18–30 remains an author disclosure, not independently certified here.

Working-tree writes were unavailable under this reviewer’s tool restrictions. This is the complete fallback body for parent materialization; no write bypass was attempted. Preserve the earlier return and record this new clock qualification additively.

### Frozen source identities

| Source | Parent-supplied SHA-256 |
|---|---|
| S1, complete f362 candidate | `1fbc6f48356fc00fc73024a0e06a3dd0f8133e75529275f64a458bd746d533bc` |
| S2, local-extension Theorem 2 excerpt | `b9c5800122e15f79a449c5628a30d3aee01bc5c73244bbb446327cbf218d0d3b` |
| S3, Supplementary Material E excerpt | `8da6500820e18f3b13328327c38cd16887a770513e4d09b599c439dacbb6a996` |
| S4, Horodecki theorem excerpt | `2a42bcb8941e8fe76c3646702dcaaaf2b8af1b6a278a8a24a3b546008971e9fb` |
| S5, existing \(4\times5\) disposition | `a560d2fc54be58695362a1c0cf338df026f28fec084325772e90e481e44479ad` |

S2–S4 were read completely as **bounded frozen excerpts**, not represented as complete-paper reads.

## 2. Per-claim findings

| Claim | Disposition | Source anchors |
|---|---|---|
| \(R\ge0\), rank \(8\), trace \(25\) | **SUPPORTED** | S1 LF65–87 |
| Exact complex partial transpose is PSD, rank \(9\) | **SUPPORTED** | S1 LF91–121 |
| Fourth-root averaging gives the exact Schmidt-rank-\(\le2\) decomposition | **SUPPORTED** | S1 LF125–157 |
| Complex range minors establish entanglement and true SN \(=2\) | **SUPPORTED** | S1 LF164–189 |
| No universally complex-rank-\(\le2\) nonnegative detector pairs negatively with this state | **SUPPORTED** | S1 LF150–155, 193 |
| Codimension-one separable compression implies SN \(\le2\), including singular/zero cores and complex coherent completions | **SUPPORTED** | S1 LF203–246; S2 LF16, 21–23, 34–45 |
| Exact \(C_0\) separability and every PSD completion of \(tC_0\), \(t\ge0\) | **SUPPORTED** | S1 LF250–278 |
| Broader \(\mathcal E,\mathcal F,\mathcal G\) retained-block PPT family | **SUPPORTED** | S1 LF282–309; S4 LF19–26 |
| Existing-source attribution of the lemma and intermediate SN-\(2\) conclusion | **SUPPORTED** | S1 LF78, 246; S2 LF21–45; S3 LF15–23 |
| Unrestricted \(4\times4\) PPT/SN-\(\le2\) theorem or target SN-\(\ge3\) state | **INCONCLUSIVE / NOT ESTABLISHED** | S1 LF56, 309, 493–496 |
| Separate public-paper Eq. (6) characterization | **OUT OF SCOPE; no verdict** | S1 §5 |

No assigned mathematical claim is refuted.

## 3. Actual \(R\): positivity, normalization, partial transpose

Use \([v]=|v\rangle\langle v|\) and Bob partial transpose
\[
(|ij\rangle\langle k\ell|)^\Gamma=|i\ell\rangle\langle kj|.
\]

The supplied vectors are
\[
A=|00\rangle+|11\rangle+|22\rangle,\quad
B=|01\rangle+|12\rangle,\quad
D=|10\rangle-|21\rangle,\quad
E=|20\rangle+|33\rangle,
\]
with
\[
R=[A]+[B]+[D]+3\bigl([02]+[E]+[23]+[30]+[32]\bigr).
\]

### PSD, rank and trace — SUPPORTED

The eight nonzero vectors have pairwise disjoint supports:
\[
\{00,11,22\},\{01,12\},\{10,21\},\{02\},
\{20,33\},\{23\},\{30\},\{32\}.
\]
They are independent, so the positive projector sum has rank \(8\). Its trace is
\[
3+2+2+3(1+2+1+1+1)=25.
\]
Therefore \(R/25\) is a normalized positive state.  
**Anchors:** S1 LF65–87.

### Exact complex partial transpose — SUPPORTED

Direct expansion yields
\[
\begin{aligned}
R^\Gamma={}&[\,|01\rangle+|10\rangle\,]
+[\,|12\rangle+|21\rangle\,]\\
&+[\,|02\rangle+|11\rangle-|20\rangle\,]
+2[\,|02\rangle+|20\rangle\,]\\
&+3[\,|23\rangle+|30\rangle\,]
+[00]+[22]+3[33]+3[32].
\end{aligned}
\]

The cross terms of \([A]\) give the \(01\leftrightarrow10\), \(02\leftrightarrow20\), and \(12\leftrightarrow21\) couplings. Those of \([B]\), \([D]\), and \(3[E]\) give respectively \(02\leftrightarrow11\), \(-11\leftrightarrow20\), and \(3(23\leftrightarrow30)\), confirming the displayed signs and locations.

The \((02,11,20)\) block is exactly
\[
\begin{pmatrix}3&1&1\\1&1&-1\\1&-1&3\end{pmatrix}
=
\begin{pmatrix}1\\1\\-1\end{pmatrix}
\begin{pmatrix}1&1&-1\end{pmatrix}
+
2\begin{pmatrix}1\\0\\1\end{pmatrix}
\begin{pmatrix}1&0&1\end{pmatrix}.
\]
It has rank \(2\). The disjoint block ranks total
\[
1+1+2+1+1+1+1+1=9.
\]
Thus \(R^\Gamma\ge0\) and \(\operatorname{rank}R^\Gamma=9\).

These are outer-product identities on the complex Hilbert space, not real-only tests or numerical eigenvalue evidence.  
**Anchors:** S1 LF91–121.

## 4. Exact Schmidt number

### Root-of-unity decomposition — SUPPORTED

For \(z\in\{1,i,-1,-i\}\),
\[
v_z=B+zA-z^2D+z^{-1}|02\rangle
\]
has the exact factorization
\[
\begin{aligned}
v_z={}&
(|0\rangle+z|1\rangle+z^2|2\rangle)
\otimes(|1\rangle+z^{-1}|2\rangle)\\
&+(z|0\rangle-z^2|1\rangle)\otimes|0\rangle.
\end{aligned}
\]
It is a sum of two product vectors over \(\mathbb C\). Its rows-\(0,1\), columns-\(0,1\) minor is
\[
\det\begin{pmatrix}z&1\\-z^2&z\end{pmatrix}=2z^2\ne0,
\]
so each supplied \(v_z\) actually has Schmidt rank \(2\).

The exponents \(-1,0,1,2\) are distinct modulo \(4\). Because \(\bar z=z^{-1}\), fourth-root averaging cancels every cross term:
\[
\frac14\sum_z[v_z]=[A]+[B]+[D]+[02].
\]
Consequently,
\[
R=\frac14\sum_z[v_z]+2[02]+3[E]+3[23]+3[30]+3[32].
\]
All summands have Schmidt rank at most \(2\), proving
\[
\operatorname{SN}(R/25)\le2.
\]
**Anchors:** S1 LF125–157.

### Range-minor lower bound — SUPPORTED

Local projection of both parties onto \(0,1,2\) gives
\[
R_3=[A]+[B]+[D]+3[02]+3[20],
\]
whose range consists of matrices
\[
X=\begin{pmatrix}
a&b&c\\d&a&b\\e&-d&a
\end{pmatrix}.
\]
Complex rank at most \(1\) forces
\[
a^2-bd=0,\qquad a^2+bd=0.
\]
Hence \(a=0\). Every product vector in this range has zero \(00\) coefficient.

Every constituent of a positive decomposition of \(R_3\) lies in its range: testing a kernel vector gives a sum of nonnegative squared overlaps, all of which must vanish. A separable decomposition would therefore imply
\[
\langle00|R_3|00\rangle=0,
\]
contradicting its value \(1\).

Thus \(R_3\), and therefore \(R\), is entangled. Together with the upper decomposition,
\[
\boxed{\operatorname{SN}(R/25)=2.}
\]
**Anchors:** S1 LF164–189.

Applying a universally complex-Schmidt-rank-\(\le2\) nonnegative detector to each positive term of the decomposition gives \(\operatorname{Tr}(WR)\ge0\). This excludes negative detection of **this** state, not all \(4\times4\) PPT states.  
**Anchor:** S1 LF193.

## 5. General codimension-one completion lemma

Let
\[
\mathcal H_B=\mathcal H_{B,r}\oplus\operatorname{span}\{|\perp\rangle\},
\qquad
\rho=\begin{pmatrix}C&Z\\Z^\dagger&D\end{pmatrix}\ge0.
\]

For \(x\in\ker C\), the vector \((x,0)\) has zero \(\rho\)-quadratic form. Positivity forces \(\rho(x,0)=0\), hence \(Z^\dagger x=0\). Therefore
\[
\operatorname{range}Z\subseteq\operatorname{range}C,\qquad CC^+Z=Z.
\]
Evaluating the quadratic form at \((-C^+Zy,y)\) gives
\[
K:=D-Z^\dagger C^+Z\ge0.
\]

For separable \(C\), choose a finite conic decomposition
\[
C=\sum_j[u_j],\qquad u_j=a_j\otimes b_j.
\]
Define
\[
\widetilde u_j=
\begin{pmatrix}u_j\\ Z^\dagger C^+u_j\end{pmatrix}.
\]
The Moore–Penrose identities give
\[
\sum_j[\widetilde u_j]
=
\begin{pmatrix}
C&CC^+Z\\
Z^\dagger C^+C&Z^\dagger C^+CC^+Z
\end{pmatrix}
=
\begin{pmatrix}
C&Z\\Z^\dagger&Z^\dagger C^+Z
\end{pmatrix}.
\]

Writing \(w_j=Z^\dagger C^+u_j\in\mathcal H_A\),
\[
\widetilde u_j=a_j\otimes b_j+w_j\otimes|\perp\rangle
\]
has Schmidt rank at most \(2\), including arbitrary complex phases. The remainder
\[
K\otimes[|\perp\rangle]
\]
is separable. Therefore
\[
\boxed{\operatorname{SN}(\rho)\le2.}
\]

If \(C=0\), range inclusion forces \(Z=0\); every nonzero completion is separable after normalization. The zero operator causes no difficulty in the conic formulation.

This proof handles singular \(C\), zero \(C\), singular \(D\), and arbitrary complex \(Z,D\) subject to positivity. It requires **no PPT assumption**.  
**Anchors:** S1 LF203–244.

### Attribution

This is the separable-core specialization of the published local-extension theorem, with parties exchanged:

- S2 LF21–23 states the one-local-dimension Schmidt-number bound.
- S2 LF34–45 gives the same lifted-vector/Schur-remainder mechanism.
- S2 LF43 explicitly specifies the pseudoinverse.

S1 LF246 correctly describes its proof as a reconstruction, not a new general theorem.

Primary source: [Krebs–Gachechiladze, arXiv:2509.07086v1, Theorem 2](https://arxiv.org/html/2509.07086v1#Thmobservation2).

## 6. Exact \(C_0\) and arbitrary coherent completions

Deleting Bob coordinate \(0\) gives
\[
\begin{aligned}
C_0={}&[\,|11\rangle+|22\rangle\,]+[B]+[21]+3[02]\\
&+3[23]+3[33]+3[32].
\end{aligned}
\]
The supplied product vector
\[
p_z=(|0\rangle+z|1\rangle+z^2|2\rangle)
\otimes(|1\rangle+z^{-1}|2\rangle)
\]
expands as
\[
p_z=B+z(|11\rangle+|22\rangle)+z^2|21\rangle+z^{-1}|02\rangle.
\]
Fourth-root averaging therefore proves exactly
\[
\boxed{
C_0=\frac14\sum_z[p_z]+2[02]+3[23]+3[33]+3[32].
}
\]
Thus \(C_0\) is separable. Its disjoint-support form also shows rank \(7\) in the retained 12-dimensional space: the singular-core treatment is relevant to the actual example.

Every \(tC_0\), \(t\ge0\), is separable. The proved lemma yields
\[
Q\rho Q=tC_0,\quad \rho\ge0
\quad\Longrightarrow\quad
\operatorname{SN}(\rho)\le2.
\]
All complex coherent completion blocks consistent with positivity are included; they need not equal the completion blocks of \(R\). The \(t=0\) boundary is covered by the zero-core argument.  
**Anchors:** S1 LF250–278.

## 7. Broader retained-block PPT family

The supplied spaces \(\mathcal E,\mathcal F,\mathcal G\) are orthogonal, have dimensions \(6,3,3\), and exhaust the retained space.

For a PPT \(\rho\) whose retained compression is block diagonal across them:

- The \(\mathcal E\) block is a local \(3\times2\) compression. It is positive and PPT. Normalize if nonzero, exchange parties, and apply Horodecki Theorem 3: the block is separable. PPT on either party is equivalent because the two partial transposes differ by full transpose.
- The \(\mathcal F\) block has a one-dimensional Bob factor and is separable.
- The \(\mathcal G\) block has a one-dimensional Alice factor and is separable.
- Zero blocks contribute nothing.

Block diagonality makes the retained compression a sum of these separable blocks. The codimension-one lemma proves SN \(\le2\) for the full state, including its coherent completion blocks.

The named import is specifically PPT iff separable on \(2\times2\) and \(2\times3\), not on \(3\times3\) or \(4\times4\).  
**Anchors:** S1 LF282–309; S4 LF19–26.

Primary source: [Horodecki–Horodecki–Horodecki, quant-ph/9605038v2, Theorem 3](https://arxiv.org/html/quant-ph/9605038v2#Thmtheorem3).

## 8. Intermediate-state attribution and source caveat

S3 LF15–23 already identifies the single-extension intermediate \(4\times4\) state as SN \(2\), using a separable projection and Theorem 2. The candidate’s exact certificates reconstruct that conclusion; they do not establish novelty.

Primary source: [Krebs–Gachechiladze, Supplementary Material E](https://arxiv.org/html/2509.07086v1#A5).

**Documentary caveat, not a candidate defect:** S3 LF23 lists \(|30\rangle\) among terms remaining after deleting Bob coordinate \(0\), although
\[
(I_A\otimes Q_B)|30\rangle=0.
\]
S1’s explicit \(C_0\) formula correctly omits it. The reviewed result rests on the exact decomposition, not that inconsistent source list.

S5 retains its \(4\times5\) boundary. Its state/detector result does not transfer an SN-\(\ge3\) conclusion to \(4\times4\). No prior fixed-pair pairing or review summary was used to establish the present bounds.

## 9. Final disposition

**Overall correctness: correct within the frozen §§3–4 written-review scope.**

The exact state, complex partial transpose, root-of-unity decomposition, rank-one range-minor obstruction, singular/zero-core completion proof, explicit \(C_0\), and broader retained-block family all withstand written reconstruction. The relevant general lemma and intermediate-state conclusion have existing primary-source attribution.

The unrestricted \(4\times4\) target remains **not proved or refuted**. The separate public Eq. (6) claim remains **unadjudicated** here.

**Confidence: 0.98** for these scoped written mathematical conclusions. This is same-harness written support, not human, independent-model-family, formal/kernel, novelty, or original-target acceptance.