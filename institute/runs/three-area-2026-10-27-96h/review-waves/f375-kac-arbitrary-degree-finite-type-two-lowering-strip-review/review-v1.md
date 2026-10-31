# f375 — Written audit of Theorem A

**Result: SUPPORTED at the named displayed-presentation and actual-quotient import boundary.**  
**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

This review concerns **Theorem A only**: the arbitrary-horizontal-degree, finite-type two-lowering strip. It does not adopt Theorem B, its horizontal-\((1,1)\) basis or matrix arguments, or any whole-target conclusion. Parent disposition remains required.

### 1. Frozen scope and evidence

The reviewed wave is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f375-kac-arbitrary-degree-finite-type-two-lowering-strip-review/`

Bindings, **as observed and supplied by the parent**, are:

- Manifest: `f84269190f528fd29e814f86bebb17dfe9e5d42019b1e6c6f228ca475906d5de`.
- Freeze receipt: `4fc503d8df9035f0314af25b3baeefae6ffb77d11c83a6ae628aab976d9ddb67`.
- Literal packet: `05e8783fec6cbb1e9a2eb52fccf52c81493ee57c48b38328397a39e48f9cd3da`, 53,530 bytes, 959 packet LF.

The complete ordered packet, including every ending, was read before derivation. Citations below use its **source labels**, such as `S1|250–265`, rather than the packet’s physical LF.

Exact imported boundaries:

| Input | Permitted mathematical use |
|---|---|
| **S1**, candidate, logical LF1–790 | The claims and proof under review; not an accepted premise merely because the author states them. |
| **S2**, LF1–39 | The prior upper-gap result and its named actual-source, Gram, and generalized-primary interfaces, at their stated scopes. Its finite calculation is not a substitute for the present universal proof. |
| **S3**, LF1–27 | Actual simple-adjoint local nilpotence; reflection/rootwise saturation for nonnegative horizontal degrees and level at least two; positive-simple-weight lowering injectivity; fixed-component finiteness at the named source boundary. |
| **S4**, LF1–27 | The displayed full-Cartan/f276 actual-source and whole-ideal interface: \(S_n=L_n(V)/I_n\), with **both complete seed modules**, all outer brackets and mixed contributions imposed. No preliminary-\(G_{\mathcal C}\) positive-freeness or whole-algebra PBW import. |
| **S5**, LF1–74 | The displayed row-Cartan convention, full Cartan realization, all positive and negative Serres, and precise family/target definitions. No independent authentication of the original book or transcription. |

The f306 contraction and f314 generalized-primary interfaces remain **named imports at their stated boundaries**; this review does not claim a fresh complete reconstruction of their underlying manuscripts.

### 2. Claim-by-claim disposition

| Claim | Source LF | Disposition |
|---|---|---|
| The stated hypotheses imply \(n\ge3\), so every lowering target has level at least two. | S1\|39–56, 250–258 | **SUPPORTED.** |
| All lowering contributions other than those attached to \(u_0,u_1\) vanish in the displayed orientation. | S1\|183–219, 250–265 | **SUPPORTED**, with strict inequalities and negative-coordinate cases reconstructed below. |
| The remaining expression has coefficients \(+1,+1\) and the order \([F_3,F_1]\). | S1\|198–219, 260–265 | **SUPPORTED** at the declared coevaluation normalization. |
| Nodes \(1,3\) give a finite-type \(A_2/B_2/G_2\) representation on the actual quotient. | S1\|169–179, 270–275 | **SUPPORTED.** No faithfulness assumption is needed. |
| Every vector lies in a finite-dimensional module for that rank-two algebra. | S1\|277–283; S3\|17–19 | **SUPPORTED**, using Weyl conjugacy and finite-type PBW only. |
| A compatible compact-averaged Hermitian form gives \(E_i^*=F_i\) and \(E_\gamma^*=F_\gamma\), without an adverse root-length factor. | S1\|285–294 | **SUPPORTED**, including unequal root lengths. |
| Positive \(h_3\)-weight makes \(F_3\) injective. | S1\|297–301; S3\|19 | **SUPPORTED.** |
| The operator is invertible on the **entire** actual root component and has no generalized-zero chains there. | S1\|303–305, 734–747 | **SUPPORTED.** |
| The mirrored statement and the claimed first-boundary inclusion hold with their exact restrictions. | S1\|56–66, 305 | **SUPPORTED.** |
| The projected-seed equality follows through the stated f314 identification. | S1\|118–124, 156–165, 747 | **SUPPORTED as a conditional corollary of that named identification**, not a fresh verification of f314. |
| Theorem B, its basis, matrices, spectra and finite illustration. | S1\|68–102, 307–730 | **Outside this assignment; no disposition granted.** They were read but are not premises for any conclusion below. |

### 3. Exact strip, levels and target elimination

Use the displayed row convention and write
\[
\alpha=a\alpha_1+b\alpha_2+n\alpha_3,\qquad
t=ra+sb,\qquad d=t-n.
\]
Consequently,
\[
\alpha(h_3)=2n-ra-sb=t-2d.
\]

First take the orientation
\[
r<s,\qquad 1\le r\le3,\qquad a,b\ge1,\qquad
0\le d\le s-2,\qquad 2d<t.
\]
All degrees and parameters here are integral, as in the root-lattice source.

Since \(t\ge r+s\),
\[
n=t-d\ge r+s-(s-2)=r+2\ge3.
\]
Thus every lowering target has level \(n-1\ge2\). In particular, the exceptional level-one target responsible for the separate \(n=2\) mixed Gram block cannot occur in Theorem A.

For a letter of horizontal charge \((c,e)\), its actual lowering target is
\[
S_{(a-c,b-e,n-1)}.
\]
If either horizontal coordinate is negative, the third coordinate remains positive, so this is a mixed-sign degree and vanishes by triangular support.

Otherwise, the excess of its level over the third-string saturation bound is
\[
\Delta(c,e)
=(n-1)-\bigl[r(a-c)+s(b-e)\bigr]
=rc+se-d-1.
\]
The complete roster is:

| Letter | Charge \((c,e)\) | Excess \(\Delta(c,e)\) | Conclusion |
|---|---:|---:|---|
| \(u_0\) | \((0,0)\) | \(-d-1\) | Not eliminated by this saturation argument. |
| \(u_1\) | \((1,0)\) | \(r-d-1\) | Retained unless the stronger sub-band inequality eliminates it. |
| \(u_2\) | \((0,1)\) | \(s-d-1\ge1\) | Zero target. |
| \(u_3,u_4\) | \((1,1)\) | \(r+s-d-1\ge r+1>0\) | Both zero targets. |
| \(u_5\) | \((2,1)\) | \(2r+s-d-1\ge2r+1>0\) | Zero target. |
| \(u_6\) | \((1,2)\) | \(r+2s-d-1\ge r+s+1>0\) | Zero target. |
| \(u_7\) | \((2,2)\) | \(2r+2s-d-1\ge2r+s+1>0\) | Zero target. |

Every application of saturation therefore has the required **strict** inequality and level at least two. This includes targets with both horizontal coordinates zero: higher pure-simple degree is not left as a loophole.

“Retained” does not mean that \(u_1\)'s target, or its contribution, is nonzero for every \(a,b,d\). If \(d\le r-2\), then
\[
r-d-1\ge1,
\]
and that target vanishes too, recovering the prior \(E_3F_3\) sub-band. At \(d=r-1\), the excess becomes zero, so it must not be discarded by the strict saturation theorem.

These eliminations take place in the **actual whole-two-seed quotient**. They do not discard one seed, assume the two seed images are disjoint, or replace their mixed ideal by a rank subtraction.

### 4. Gram normalization, signs and consuming map

The consuming expression is the stated inverse-Gram bracket sum
\[
\overline A_nx
=\sum_{i,j}(G^{-1})_{ij}[u_i,W_jx].
\]
This is the point at which the surviving lowerings must actually be traced into the operator.

The fixed Levi \(A_2\) module supplies a direct normalization check. With \(u_0=e_3\) of norm one, its Levi weights are \((-1,-1)\), and
\[
F_1u_0=F_2u_0=0,\qquad
F_1u_1=u_0,\qquad F_2u_2=u_0.
\]
Thus \(G_{00}=G_{11}=G_{22}=1\).

For the duplicate charge,
\[
u_3=E_1u_2,\qquad u_4=E_2u_1,
\]
and the Chevalley relations give
\[
F_1u_3=2u_2,\qquad F_1u_4=u_2,\qquad
F_2u_4=2u_1.
\]
Hence
\[
G_{\{3,4\}}=
\begin{pmatrix}2&1\\1&2\end{pmatrix},
\qquad
G_{\{3,4\}}^{-1}
=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
\]
The off-diagonal sign is therefore positive in \(G\), negative in its inverse, as claimed.

The factors \(-\tfrac12\) and \(+\tfrac12\) in \(u_5,u_6\) give singleton norms one: for example, \(F_1E_1u_3=2u_3\) and \(\|u_3\|^2=2\), so
\[
\left\|-\tfrac12E_1u_3\right\|^2=1.
\]
The exchanged calculation gives \(\|u_6\|^2=1\). Also \(F_1u_6=0\) and \(H_1u_6=-u_6\), giving \(\|E_1u_6\|^2=1\). Distinct charges have distinct Levi weights and are orthogonal. Thus there is no omitted inverse-Gram coupling of \(u_0\) or \(u_1\) to a different charge.

The actual transpose anti-involution sends \(e_i\) to \(f_i\) and reverses bracket order. In particular,
\[
w_0=f_3,\qquad
w_1=[f_3,f_1],
\]
so
\[
W_0=F_3,\qquad W_1=[F_3,F_1].
\]
The order is essential: replacing \(W_1\) by \([F_1,F_3]\) would reverse the sign of the second contribution.

All columns belonging to \(W_2,\ldots,W_7\) now vanish. In particular, **both** columns of the mixed Gram block vanish, so no off-diagonal remnant survives. The consuming bracket sum is exactly
\[
\overline A_n
=E_3F_3+\operatorname{ad}(u_1)[F_3,F_1]
=E_3F_3+[E_1,E_3][F_3,F_1].
\]

This argument uses the declared finite-Levi Gram normalization. It does **not** identify that Gram form with a global invariant form on the nonsymmetrizable algebra, or with the auxiliary Hermitian form constructed next.

### 5. Finite-type representation and local finiteness

The actual quotient satisfies the Chevalley and both-sign Serre relations for nodes \(1,3\), whose matrix is
\[
\begin{pmatrix}2&-1\\-r&2\end{pmatrix}.
\]
For \(r=1,2,3\), the finite-dimensional Chevalley–Serre theorem therefore supplies the corresponding \(A_2,B_2,G_2\) algebra and a representation on \(S\) by the actual adjoints.

An additional injectivity or faithfulness assertion about this representation is unnecessary. Further relations in \(S\) do not invalidate a representation of the finite-type algebra.

For completeness, with \(\eta=\alpha_1\) and \(\beta=\alpha_3\), the positive-root lists involved are:

| Type | Positive roots |
|---|---|
| \(A_2\) | \(\eta,\beta,\eta+\beta\) |
| \(B_2\) | \(\eta,\beta,\eta+\beta,\eta+2\beta\) |
| \(G_2\) | \(\eta,\beta,\eta+\beta,\eta+2\beta,\eta+3\beta,2\eta+3\beta\) |

These are the three required finite-type cases, not selected diagnostic instances.

Simple adjoint local nilpotence is available directly on the actual quotient: the Serres give it on the other simple generators, the Chevalley relations give it on opposite generators and Cartan directions, and the derivation binomial identity extends it to every finite Lie word.

The finite exponentials
\[
T_i=\exp(E_i)\exp(-F_i)\exp(E_i)
\]
are therefore well-defined invertible linear maps. They implement the rank-two Weyl action on root operators. Every root of each listed finite root system is Weyl-conjugate to a simple root **of the same length**; in the unequal-length systems, both required lengths are represented among the two simple roots. Accordingly, every root operator is a nonzero scalar multiple of a conjugate of a locally nilpotent simple operator, and is locally nilpotent. Negative roots are covered as well.

Now use PBW for this **finite-dimensional rank-two algebra**, with finitely many root factors and the Cartan factors ordered to the right. On a fixed weight vector, the Cartan powers are scalar. For each successive root factor, only finitely many powers act nontrivially on each of the finitely many vectors obtained at the preceding stage. Induction over the finite list of factors gives a finite spanning set for its cyclic module.

A general vector is a finite sum of weight vectors, so it also lies in a finite-dimensional submodule. This proves the needed local finiteness without invoking PBW or positive freeness for the whole preliminary nonsymmetrizable algebra.

### 6. Compact Hermitian form and root-length normalization

Let \(M\) be one such finite-dimensional module. Choose the standard compact real form compatible with the given Chevalley generators, and integrate the representation to its simply connected compact group. Averaging any positive Hermitian form over that group produces a positive Hermitian form on \(M\).

In this compact form,
\[
e_i-f_i,\qquad \mathrm i(e_i+f_i),\qquad \mathrm i h_i
\]
act skew-adjointly for \(i=1,3\). The first two identities imply
\[
E_1^*=F_1,\qquad E_3^*=F_3.
\]
This normalization is available for the unequal-length \(B_2,G_2\) systems as well. Root-length factors belong to the symmetrized invariant bilinear form; they do not force an extra factor in these Chevalley adjoint identities.

The finite-type symmetrizer can be taken as
\[
D=\operatorname{diag}(r,1),\qquad
DA_{13}=
\begin{pmatrix}2r&-r\\-r&2\end{pmatrix}.
\]
Its determinant is \(r(4-r)>0\) throughout the stipulated range. Thus the compact choice used here is the finite-type one, not a claimed compact structure on the full nonsymmetrizable algebra.

Set
\[
E_\gamma=[E_1,E_3],\qquad F_\gamma=[F_3,F_1].
\]
Taking adjoints reverses operator order, and consequently
\[
E_\gamma^*=[F_3,F_1]=F_\gamma.
\]
There is neither a minus sign nor a root-length multiplier here.

A further normalization check, directly from the displayed Cartan relations, is
\[
[[e_1,e_3],[f_3,f_1]]=r h_1+h_3,
\qquad
(\alpha_1+\alpha_3)(r h_1+h_3)=2.
\]
Thus these very bracket vectors already have the compatible opposite-root normalization; no replacement by differently scaled root vectors is being silently made.

Even a convention yielding \(E_i^*=c_iF_i\) with positive real \(c_i\) would give
\[
\langle x,\overline A_nx\rangle
=c_3\|F_3x\|^2+c_1c_3\|F_\gamma x\|^2.
\]
Such positive rescalings would not undermine the positivity argument. For the compatible compact Chevalley choice above, \(c_1=c_3=1\), giving exactly the author’s displayed identity.

### 7. Positive weight, whole-component invertibility and generalized chains

For \(x\in S_\alpha\), choose a finite-dimensional rank-two submodule containing \(x\). The established operator identity gives
\[
\langle x,\overline A_nx\rangle
=\|F_3x\|^2+\|F_\gamma x\|^2.
\]

Here \(x\) has third simple weight
\[
m=t-2d>0.
\]
To reconstruct injectivity without a complete-reducibility assumption, suppose \(F_3x=0\) and \(x\ne0\). Local nilpotence of \(E_3\) supplies a least \(k\ge1\) with \(E_3^kx=0\). The simple-string identity gives
\[
F_3E_3^kx
=-k(m+k-1)E_3^{k-1}x.
\]
The left side is zero; the right side is nonzero because \(m>0\) and the preceding power is nonzero. This contradiction proves \(F_3\)-injectivity.

It follows that
\[
x\ne0\quad\Longrightarrow\quad
\langle x,\overline A_nx\rangle>0,
\]
and hence \(\ker(\overline A_n|S_\alpha)=0\).

This is an argument for **every** vector of the actual component, not merely a chosen string or a collection of exhibited vectors. Moreover, \(S_\alpha\) is finite-dimensional because it is a root component of the finite free level \(L_n(V)\) modulo the actual ideal. If desired, take a finite basis of \(S_\alpha\) and sum the finite cyclic rank-two modules containing its basis vectors; that gives one finite module and one averaged form covering the entire component simultaneously.

Each retained product has total root degree zero, so it preserves \(S_\alpha\). Injectivity of this endomorphism on the finite-dimensional component therefore proves its invertibility.

The generalized-zero conclusion follows directly:
\[
\ker \overline A_n^{\,k}=0\qquad(k\ge1).
\]
No prior zero-semisimplicity or diagonalizability assumption is being used.

Likewise, from \(\overline A_n=\overline\mu_n\overline{\mathcal C}_n\),
\[
\ker\overline{\mathcal C}_n=0,\qquad
\operatorname{im}\overline{\mathcal C}_n
\cap\ker\overline\mu_n=0.
\]
For the second statement, write a tensor in the intersection as \(\overline{\mathcal C}_nx\); its bracket is \(\overline A_nx=0\), so \(x=0\).

At the **named f314 identification**
\[
E_0(\overline A_n|S_\alpha)
\cong
E_{n,\alpha}/\operatorname{im}(e_n\Phi_n)_\alpha,
\]
vanishing of the entire generalized-zero space gives the stated projected-seed equality. This last step retains precisely that import; it does not independently authenticate or enlarge it.

### 8. Mirror, boundaries and empty cases

For \(s<r\), \(1\le s\le3\), exchange nodes \(1,2\). The exact conditions become
\[
a,b\ge1,\qquad
0\le d\le r-2,\qquad
2d<ra+sb,
\]
and
\[
\overline A_n
=E_3F_3+[E_2,E_3][F_3,F_2].
\]
The auxiliary algebra is now the finite-type algebra on nodes \(2,3\). The same proof gives \(n\ge s+2\), target elimination, compatible adjoints, injectivity and whole-component invertibility.

The boundary checks are:

- **Exact integral strip.** In the first orientation, the allowed values are
  \[
  0\le d\le
  \min\!\left(s-2,\left\lfloor\frac{t-1}{2}\right\rfloor\right).
  \]
  The strict positive-weight restriction has not been replaced by a weak inequality.
- **Nonempty parameter strip.** Since \(r<s\), one has \(s\ge2\), and \(d=0\) is admissible. This is a statement about allowed parameters, not an assertion that every corresponding root component exists.
- **New part.** Since \(s\ge r+1\), the interval
  \[
  r-1\le d\le s-2
  \]
  contains its first endpoint. At that endpoint,
  \[
  t-2(r-1)\ge r+s-2r+2=s-r+2>0.
  \]
  Thus the claimed first-boundary inclusion holds for arbitrary \(a,b\ge1\).
- **Empty old band.** When the minimum parameter is one, the earlier band \(0\le d\le\min(r,s)-2\) is empty. The present argument does not rely on that band being nonempty.
- **Upper endpoint.** At \(d=s-2\), the \(u_2\) target still has excess one and is eliminated. At the excluded value \(d=s-1\), its excess is zero; the elimination cannot be extended by assertion.
- **Weight boundary.** At \(2d=t\), positive-weight lowering injectivity is unavailable. No conclusion at that boundary is imported from this argument.
- **Zero root component.** If \(S_\alpha=0\), its unique endomorphism is bijective and all the claimed kernels and intersections vanish. No nonzero-root existence claim is needed.
- **Equal parameters and larger minimum.** Equal parameters are outside this two-term proof. A minimum of at least four is outside the finite-type compact argument. Neither is covered by the present verdict.
- **Small horizontal coefficients.** Negative-coordinate targets are eliminated before applying saturation, so no hidden assumption \(a,b\ge2\) enters the proof.

### 9. Findings and unpaid gates

There is no patch-anchored mathematical defect to report within Theorem A’s assigned scope. In particular, the compact-form argument survives the unequal root lengths, the lowering commutator has the correct order, and the proof reaches the entire actual component.

The following remain unpaid by this review:

1. Independent verification or original-source authentication of the f276 actual-source/full-ideal bridge and the f306/f314 interfaces beyond their named scopes.
2. Theorem B, its full quotient basis, row-cancellation argument, exceptional Gram matrix, spectra and supplied finite illustration.
3. Any general claim for equal parameters, minimum parameter at least four, the second-arm boundary, or other regions outside Theorem A.
4. Whole-level \(B_8=0\), whole-level contraction or primary saturation, all-level \(J=\tau\), or the full original conjecture.
5. Executable finite certification, independent-model-family review, human review, formal/kernel verification, novelty or priority certification.

The author’s candidate status is not self-adoption, and this reviewer’s scoped written support is not a substitute for parent disposition.

**overall_correctness:** correct

**explanation:** Theorem A’s reduction and finite-type positivity argument are valid on the entire actual root component at the named import boundary. The mirrored case and strict boundary conditions also hold; this verdict does not extend to Theorem B or the unresolved global target.

**confidence:** 0.98

---

## Materializable body: `reviewer-process-v1.md`

# f375 — Reviewer process and coverage record

### Role and delivery

- Assignment: **WRITTEN review of Theorem A only** in `f375-kac-arbitrary-degree-finite-type-two-lowering-strip-review`.
- Actual runtime model supplied by this session’s runtime context: `anthropic/claude-fable-5-1`.
- No independent-family, human, kernel or novelty assurance is claimed.
- Working-tree file writing is unavailable under this reviewer’s read-only role and tool contract. **No working-tree write was attempted, and no refusal is fabricated.** The complete review and this process body are returned directly for parent materialization; no alternate-filesystem bypass was used.

### Metadata attribution

The parent supplied the following live bindings:

| Artifact | SHA256 | Parent-reported bytes / LF |
|---|---|---|
| `manifest-v1.json` | `f84269190f528fd29e814f86bebb17dfe9e5d42019b1e6c6f228ca475906d5de` | 6,906 / 128 |
| `freeze-receipt-v1.json` | `4fc503d8df9035f0314af25b3baeefae6ffb77d11c83a6ae628aab976d9ddb67` | 3,315 / 86 |
| `literal-packet-v1.md` | `05e8783fec6cbb1e9a2eb52fccf52c81493ee57c48b38328397a39e48f9cd3da` | 53,530 / 959 |
| S1 candidate | `af51a0025d41ddd0a62fd42b1be8b7f65d69601d253455ff0f8717fd26fa9d01` | 26,149 / 789 |
| S2 upper-gap disposition | `7f95403e09074983f4d8326214c6ed1a3f6ea0c91ff91bc120b291bba639d3be` | 5,838 / 39 |
| S3 rootwise-saturation disposition | `6bd5cebd05e8627b07d15095dc351ed8b7a2f30d7e96083598e728c0315cece4` | 4,553 / 27 |
| S4 actual-source/full-ideal disposition | `09d94aacd14c652568da68facca73f79121fb8b2f0a7b30a4cdd703204230c0e` | 5,403 / 27 |
| S5 source definitions | `b415be711bf075210e2154db9812b024cb2282dfd38c3ae2fd9fb97315234030` | 5,166 / 74 |

The S1 coverage statement in this review refers to the packet’s complete **logical source labels LF1–790**, including its final request for disposition. The table above preserves the parent’s reported LF metadata without presenting it as a child-run count.

No child-native hash or clock command was executed.

### Controls read before the mathematical body

The complete manifest, complete freeze receipt and the following seven controls were read before packet access:

1. `contract-addendum-2-frontier-first-owner-direction-v1.json`  
   SHA `5e18c2d4b94656fc12b5cfce4122889fa6073e24a21f1e0062c79d846b6037ce`.
2. `parent-L1-selected-diagnostic-release-quarantine-v1.json`  
   SHA `ba6b4bb953e9ee20c57c4ae84b85dadbc66e26f8e800089f5176b2582a13555f`.
3. `parent-written-duty-execution-and-reporting-deviations-20261030-v1.json`  
   SHA `12e118d84b8fd065d9c02bd29e2d030e6b1b4d4b26c84f1748eb2d72acd8416b`.
4. `prospective-author-method-scope-restoration-20261030-v1.json`  
   SHA `6ab69778c11dbfc4ac895f97b381cc70d0059a5723d6b02f62b9957c7e8dcd95`.
5. `parent-ame-held-compression-claim-consumer-quarantine-v1.json`  
   SHA `c307e902eee5f3736aab0e2437738898382b3d3083f6c307118219b9a4c875b0`.
6. `parent-core-gram-auxiliary-operator-diagnostic-quarantine-v1.json`  
   SHA `23fa29449cef8e02d981efc021934e4cec16960ca6bfe8f6f2178bbd048c85b4`.
7. `parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1.json`  
   SHA `e4d6f1e49cb18aced7735cf025dee54830400554c9adc08138250ae9f0523efc`.

These were used as **status and permission controls only**. No excluded scientific payload was followed. All genuine held outputs and their proof, method, selection, planning and confidence consumers remained NONINPUT.

The general-author permission for fresh examples was not misclassified as a violation. Conversely, it did not override this assignment’s explicit WRITTEN_ONLY contract.

The parent’s complete `parent-live-metadata-supply-v1.json` was also read before packet access.

### Pre-body acknowledgment

After those reads, an administrative ACK was delivered directly to Main, before any mathematical packet read or derivation. It accepted:

- Theorem A only;
- WRITTEN_ONLY and no privately selected diagnostic instances;
- complete ordered raw packet reads in windows of at most 20 LF;
- exact-scope imports;
- held-consumer exclusions;
- no sibling-outcome access;
- parent attribution of supplied metadata;
- direct full-body fallback if role tools did not permit down-wave file writing.

No mathematical conclusion was included in that ACK.

### Complete packet-read coverage

The packet was read raw and sequentially in these windows:

1–20; 21–40; 41–60; 61–80; 81–100; 101–120; 121–140; 141–160; 161–180; 181–200; 201–220; 221–240; 241–260; 261–280; 281–300; 301–320; 321–340; 341–360; 361–380; 381–400; 401–420; 421–440; 441–460; 461–480; 481–500; 501–520; 521–540; 541–560; 561–580; 581–600; 601–620; 621–640; 641–660; 661–680; 681–700; 701–720; 721–740; 741–760; 761–780; 781–800; 801–820; 821–840; 841–860; 861–880; 881–900; 901–920; 921–940; 941–959.

This covered:

- S1 logical LF1–790, including its ending;
- S2 LF1–39;
- S3 LF1–27;
- S4 LF1–27;
- S5 LF1–74, including the final provenance limitation.

No packet elision remained unrecovered. Derivation began only after that final window.

The decisive target and finite-form passages were subsequently reread in raw windows of at most 20 LF. No additional scientific source or prior reviewer body was opened.

### Methods and checkpoint chronology

All mathematical checking was written reconstruction of the supplied universal proof. It included:

- the complete lowering-charge roster and every strict saturation inequality;
- the remaining Gram entries and commutator order;
- finite-type root actions and PBW local finiteness;
- compact Hermitian adjoints, including root-length normalization;
- positive-weight lowering injectivity;
- whole-component finiteness, invertibility and generalized-zero consequences;
- the mirror, parameter endpoints and zero-component cases.

No new selected mathematical instance was introduced privately or publicly. The author-supplied finite illustration was read as part of the mandatory complete packet, not treated as independently observed output or used as a premise for Theorem A.

A substantive checkpoint was delivered directly to Main after complete packet reading and reconstruction of the target and finite-form steps. It explicitly disclaimed child-native timing and scientific execution.

The parent supplied two actual parent clock observations:

- `2026-10-30T09:54:48-0700 PDT`, with the live metadata supply;
- `2026-10-30T10:02:52-0700 PDT`, following the substantive checkpoint and the reviewer’s request for a fresh clock.

These are **parent observations**, not reviewer-native execution, start, derivation or completion times. No backdated checkpoint time, unobserved activity interval or continuous-runtime certificate is asserted.

### Non-actions and assurance ceiling

No scientific code, CAS, interpreter calculation, solver, enumeration, replay or finite executable check was run. No build, test, lint or formatter was triggered.

No external-model CLI, paid or remote job, installation, deletion, provider or credential change, commit, push, publication or infrastructure mutation occurred. No current sibling outcome or excluded held payload was read.

The completed deliverable is a same-harness, exact-scope written review supporting Theorem A conditionally on the named imports. It is not whole-target acceptance, and it grants no independent-family, human, formal/kernel, source-authenticity or novelty certification.