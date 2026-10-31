# f359 — Frozen written proof review

**Disposition: SUPPORTED at the displayed full-Cartan/f276 whole-ideal boundary.**

**Findings against the candidate: 0 FATAL / 0 MAJOR / 0 MINOR.**

The general upper-Serre-gap no-cancellation theorem is supported. The separate actual-quotient nonvacuity, dimension and spectrum claims are also supported: the free-Lie elimination can be matched to the actual positive source, and both complete Levi seed modules and their whole ideal are accounted for. Neither conclusion requires an independent finite computation.

The own-wave process-file write was refused by the available transport. No review/process file was persisted, and no shell or alternate-path bypass was attempted. This is the complete review for parent materialization.

## 1. Reviewed scope and binding

All source labels below are **f359 packet labels**, not the internal labels used in f348 §2.

| Label | Frozen source | Complete coverage read |
|---|---|---|
| S1 | f348 author candidate | Logical lines 1–479; 478 LF |
| S2 | Rootwise saturation/cancellation-corridor disposition | Lines 1–27 |
| S3 | Quotient contraction/zero-primary disposition | Lines 1–44 |
| S4 | Actual free-source/full-Cartan/whole-ideal disposition | Lines 1–27 |
| S5 | Displayed defining presentation and family | Lines 1–74 |
| S6 | Complete f343 rootwise review and process ending | Logical lines 1–680; 679 LF |

The entire ordered packet, **LF1–1333**, was read raw in consecutive windows of at most 20 LF, including both unterminated source endings, before mathematical reconstruction. No displayed window was elided or clipped.

The binding metadata is **parent-observed**, not a child-executed hash check:

- Manifest: `12e9081097f2bbb24dc0615f1bc6cf359635223cae40f32235f06aee18f49912`
- Freeze receipt: `04c6fc56fa4d81cb655edbff25913ed7e11e2885d8d26b8ccf8c7f5e3f80033e`
- Literal packet: `31a5bf4ea14b03b750be116f49c022165db4e2574c17a7f518f426ff51bc3320`
- Author candidate S1: `3c1cf8cc14cace36229e88d0974409e31ede04434c812f2ca0af46e63e1188ff`

The freeze receipt asserts selected-line byte equality and stable source hashes. I did not independently re-render or hash the packet.

### Exact retained imports

1. **S4 lines 3–10, 15–19:** full-Cartan injection; actual positive source \(T_n=L_n(V)\); ordinary characteristic-zero free-Lie tensor embedding; actual Chevalley action; complete lowest Levi seed modules; whole positive ideal; and
   \[
   J/K=P_+\oplus P_-
   \]
   with disjoint positive/negative support.
2. **S2 lines 5–21; S6 lines 74–259:** actual simple-adjoint local nilpotence, triangular support, full-root-character separation, and whole-root vanishing for
   \[
   A,B\ge0,\quad N\ge2,\quad N>rA+sB.
   \]
3. **S3 lines 7–22, 32–36; S6 lines 274–335, 379–416:** whole-seed generation, actual lowering/coevaluation/bracket descent, equal-charge Gram blocks, finite-dimensionality and generalized-zero-primary quotient identification.
4. **S5 lines 16–38, 66–70:** the displayed row-Cartan convention, full realization and Serre quotient.

The underlying f276 manuscripts are not independently reconstructed here. These remain named conditional imports, not original-source authentication.

## 2. General theorem — SUPPORTED

**Candidate references: S1 lines 9–57, 92–244.**

Let
\[
t=ra+sb,\qquad d=t-n,\qquad h=\min(r,s),
\]
with \(a,b\ge1\) and \(0\le d\le h-2\).

A nonempty band requires \(h\ge2\). Consequently,
\[
n=t-d\ge r+s-h+2=\max(r,s)+2\ge4,
\]
and the displayed **third row** gives
\[
m=\alpha(h_3)=2n-t=t-2d
  \ge r+s-2h+4=|r-s|+4>0.
\]
Thus all lowering targets used below have third coefficient \(n-1\ge3\). The saturation theorem is never applied outside its \(N\ge2\) domain. If \(r=1\) or \(s=1\), the claimed band is empty, not an exceptional unproved case.

### 2.1 Every nonzero-charge lowering target vanishes

**Candidate references: S1 lines 105–122, 147–191.**

The complete charge roster is:

| Letter | Horizontal charge \((c,e)\) | \(rc+se\) |
|---|---:|---:|
| \(u_0\) | \((0,0)\) | \(0\) |
| \(u_1\) | \((1,0)\) | \(r\) |
| \(u_2\) | \((0,1)\) | \(s\) |
| \(u_3,u_4\) | \((1,1)\) | \(r+s\) |
| \(u_5\) | \((2,1)\) | \(2r+s\) |
| \(u_6\) | \((1,2)\) | \(r+2s\) |
| \(u_7\) | \((2,2)\) | \(2r+2s\) |

For every \(j\ne0\), \(rc_j+se_j\ge h\), and the actual negative letter has target
\[
\beta_j=(a-c_j)\alpha_1+(b-e_j)\alpha_2+(n-1)\alpha_3.
\]

There are exactly two relevant cases:

- If either horizontal coefficient is negative, \(\beta_j\) is mixed-sign because \(n-1>0\). Triangular support and full-root-character separation give \(S_{\beta_j}=0\).
- Otherwise both are nonnegative, and
  \[
  \begin{aligned}
  (n-1)-\bigl(r(a-c_j)+s(b-e_j)\bigr)
  &=rc_j+se_j-d-1\\
  &\ge h-(h-2)-1\\
  &=1.
  \end{aligned}
  \]
  Hence the required saturation inequality is **strict**, including at \(d=h-2\), and \(S_{\beta_j}=0\).

Therefore
\[
W_j|S_\alpha=0\qquad(j\ne0).
\]

This argument concerns zero components of the **actual whole-ideal quotient**. It neither splits the two seed images nor assumes away mixed contributions.

### 2.2 The normalization gives exactly \(E_3F_3\)

**Candidate references: S1 lines 124–145, 193–200. Imported interface: S6 lines 290–303, 379–390.**

The supplied Levi matrix labels agree with the stated normalizations of the eight letters. Their entrywise trace pairing has six root-letter diagonal entries equal to one and the charge-\((1,1)\) block
\[
\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]
All remaining cross-block entries vanish. In particular, charge \((0,0)\) is a singleton and
\[
G_{00}=1,\qquad (G^{-1})_{00}=1.
\]

The actual negative letter is \(w_0=f_3\), so \(W_0=F_3\). Substituting the vanished nonzero-charge lowerings into the actual descended coevaluation gives
\[
\overline{\mathcal C}_n x=u_0\otimes F_3x.
\]
The consuming bracket map therefore gives
\[
\overline A_nx
=\overline\mu_n\overline{\mathcal C}_nx
=[e_3,F_3x]
=E_3F_3x.
\]

There is no omitted scalar or unprocessed Gram-block contribution. The matrix labels are used only for the Levi pairing, not as replacements for free-Lie brackets.

### 2.3 The \(EF\)-injectivity lemma is valid

**Candidate references: S1 lines 204–231.**

From
\[
[E,F]=H,\qquad [H,E]=2E,\qquad Hx=mx
\]
one obtains
\[
FE^Nx=E^NFx-N(m+N-1)E^{N-1}x.
\]
If \(EFx=0\), then for every \(N\ge1\),
\[
E^NFx=E^{N-1}(EFx)=0.
\]

For nonzero \(x\), local nilpotence supplies a least \(N\ge1\) with \(E^Nx=0\). The identity then forces
\[
N(m+N-1)E^{N-1}x=0.
\]
Because \(m>0\), its scalar is nonzero in characteristic zero, contradicting minimality.

Thus \(EF\) is injective on the entire positive-weight space. This proof does not require semisimplicity, irreducibility, a positive form, or even local nilpotence of \(F\).

Applied to the actual node-3 adjoints, it establishes injectivity of \(\overline A_n\) on all of \(S_\alpha\). Fixed-root finite-dimensionality then makes it an automorphism. Individual root components need not be Levi submodules; none is treated as one.

### 2.4 No cancellation and full zero-primary absence follow

**Candidate references: S1 lines 233–244. Imports: S3 lines 9–22; S6 lines 305–335.**

If
\[
y=\overline{\mathcal C}_nx,\qquad \overline\mu_ny=0,
\]
then \(\overline A_nx=0\), whence \(x=0\) and \(y=0\). Therefore
\[
\operatorname{im}(\overline{\mathcal C}_n|S_\alpha)
\cap\ker\overline\mu_n=0.
\]

Invertibility also gives
\[
\ker(\overline A_n^k|S_\alpha)=0
\qquad(k\ge1).
\]
Using the imported identification
\[
E_0(\overline A_n|S_\alpha)
\cong
E_{n,\alpha}/\operatorname{im}(e_n\Phi_n)_\alpha
\]
therefore yields
\[
\operatorname{im}(e_n\Phi_n)_\alpha=E_{n,\alpha}.
\]

This uses the **entire generalized zero-primary space**, not a substitution of the ordinary free-source kernel. Zero-dimensional quotient components cause no exception.

## 3. Actual-quotient nonvacuity — separately SUPPORTED

**Candidate references: S1 lines 246–342.**

This conclusion requires more than the general theorem. The necessary source/ideal comparison is valid at the named imports.

### 3.1 Ordinary free-Lie elimination

The semidirect algebra
\[
\mathbb Ct_0\ltimes
\operatorname{Lie}\langle X_i,Y_j:i,j\ge0\rangle,
\qquad
[t_0,X_i]=X_{i+1},\quad[t_0,Y_j]=Y_{j+1},
\]
is the free Lie algebra on \(t_0,X_0,Y_0\). The two maps specified in S1 lines 268–273 are well defined and inverse on every generator.

Horizontal bidegree \((1,1)\) consequently contains exactly one \(X\)-letter and one \(Y\)-letter. At third coefficient \(n\), its basis is
\[
Z_{i,j}=[X_i,Y_j],\qquad i+j=n.
\]
Distinct pairs have distinct tensor words on the eliminated alphabet, giving independence and dimension \(n+1\).

This is an ordinary free-Lie construction, not an assumption of preliminary-\(G_{\mathcal C}\) positive freeness.

### 3.2 Comparison with the actual \(L(V)\) source

**Candidate references: S1 lines 283–303.**

Eliminating \(u_0\) in the imported ordinary \(L(V)\), the complete charge-\((1,1)\), level-\(n\) roster is:

- \((\operatorname{ad}u_0)^{n-1}u_3\);
- \((\operatorname{ad}u_0)^{n-1}u_4\);
- the \(n-1\) brackets
  \[
  [(\operatorname{ad}u_0)^pu_1,
    (\operatorname{ad}u_0)^qu_2],
  \qquad p+q=n-2.
  \]

Higher-charge letters cannot enter this sector. The elimination presentation gives independence. Thus the actual source dimension is \(n+1\) for \(n\ge1\); at \(n=1\), only the two first-listed generators occur. At \(n=0\), both presentations have the one-dimensional Levi component \([e_1,e_2]\).

The natural free-positive-word surjection onto the actual positive source is therefore an isomorphism **on each of these components**. It is not asserted to be an isomorphism globally.

### 3.3 Both complete seed modules and the whole ideal

**Candidate references: S1 lines 305–333. Import: S4 lines 9–10, 19.**

The raw remaining positive Serres are \(X_{r+1}\) and \(Y_{s+1}\), up to nonzero signs. At the imported boundary they are actual lowest vectors for the finite Levi action.

Finite-Levi commutator reordering moves lowering operators to the right, where they annihilate these lowest seeds; Cartan operators act by weights. Consequently the complete cyclic modules are spanned by positive Levi raising words applied to the raw seeds.

It follows in both directions that:

- the ideal under the entire positive algebra generated by the two raw seeds contains both complete Levi seed modules;
- the \(L(V)\)-ideal generated by those complete modules is positive-Levi stable and contains both raw seeds.

These are the same ideal \(I\).

For clarity, the precise quotient comparison can be written as follows. Let
\[
\pi:F\longrightarrow n_+(T)
\]
be the positive-source surjection, and let \(H\) be the ideal of \(F\) generated by \(X_{r+1},Y_{s+1}\). Then
\[
\pi(H)=I,\qquad \pi^{-1}(I)=H+\ker\pi.
\]
The preceding component isomorphism gives
\[
(\ker\pi)_{(1,1,n)}=0.
\]
Hence
\[
S_{(1,1,n)}
\cong
F_{(1,1,n)}/H_{(1,1,n)}.
\]

The other positive Serres have first or second horizontal coefficient at least two and cannot contribute through positive brackets to this sector. **That positive-cone observation alone would not exclude negative-Serre consequences.** Their exclusion uses the separately named f276 result: \(P_+\) is already a full ideal and \(J/K=P_+\oplus P_-\) has disjoint positive/negative support. No extra positive relation is inferred away without that import.

### 3.4 Truncation introduces no relation among surviving letters

In the elimination presentation, the ideal generated by all
\[
X_i\ (i>r),\qquad Y_j\ (j>s)
\]
is stable under the shift derivation and is exactly \(H\):

- repeated brackets with \(t_0\) produce every higher invalid letter from the two raw seeds;
- conversely, the ideal of invalid letters is derivation-stable and contains both raw seeds.

The quotient is therefore free on the surviving alphabet, with
\[
DX_r=DY_s=0.
\]
An actual quotient basis is
\[
Z_{i,j},\qquad
0\le i\le r,\quad0\le j\le s,\quad i+j=n.
\]

Both seed ideals are imposed simultaneously. Words involving both invalid types lie in their union; their overlap does not create a relation among surviving words. No rank subtraction or directness assertion is used.

For \(n=r+s-d\) in the stated band, the allowed indices are exactly
\[
i=r-d,\ldots,r,
\]
so
\[
\dim S_{(1,1,r+s-d)}=d+1.
\]

This proves actual nonvacuity and permits unbounded multiplicity as the allowed parameters grow.

## 4. Explicit quotient spectrum — SUPPORTED

**Candidate references: S1 lines 344–412.**

The actual Chevalley action gives
\[
\begin{aligned}
E_3X_i&=X_{i+1},
&
F_3X_i&=i(r-i+1)X_{i-1},\\
E_3Y_j&=Y_{j+1},
&
F_3Y_j&=j(s-j+1)Y_{j-1}.
\end{aligned}
\]
These follow from \(F_3e_1=F_3e_2=0\), their respective weights \(-r,-s\), and the same universal commutator identity. The endpoint conventions agree with the Serre truncations.

Applying the actual derivations to \([X_i,Y_j]\) gives exactly S1 lines 357–364. These are identities in the **full actual quotient**, including its level-zero Levi part—not an extension of a positive free-algebra lowering into an undefined level-zero codomain.

For the proposed coefficients,
\[
\frac{c_{k,i+1}}{c_{k,i}}
=
-\frac{(k-i)(s-k+i+1)}{(i+1)(r-i)}.
\]
Thus every coefficient in \(F_3v_k\) cancels by the stated recurrence. All factorials and denominators are defined because
\[
0\le i\le k\le d\le\min(r,s)-2.
\]
The coefficient \(c_{k,0}=1\), together with the actual quotient basis, ensures \(v_k\ne0\).

Write \(\ell_k=r+s-2k\). Then
\[
F_3v_k=0,\qquad H_3v_k=-\ell_kv_k,
\]
and
\[
F_3E_3^qv_k
=q(\ell_k-q+1)E_3^{q-1}v_k.
\]
At the first nilpotent index \(N\), this forces \(N=\ell_k+1\). Therefore every claimed string vector is nonzero through exponent \(\ell_k\).

For
\[
w_k=E_3^{n-k}v_k,
\]
the exponent is nonnegative and does not exceed \(\ell_k\), since
\[
\ell_k-(n-k)=d-k\ge0.
\]
Hence
\[
\overline A_nw_k
=E_3F_3w_k
=(n-k)(d+1-k)w_k.
\]

Both factors are positive. For successive indices,
\[
\lambda_k-\lambda_{k+1}=n+d-2k=r+s-2k>0.
\]
There are therefore \(d+1\) nonzero eigenvectors with distinct eigenvalues in the actual \(d+1\)-dimensional component. They form a basis. Diagonalizability is proved **here**, not assumed in the general theorem.

### Supplied level-eight illustration

**Candidate references: S1 lines 414–429.**

For the author-supplied \(r=5,s=6,a=b=1,n=8\), the stated \(d=3\), four basis pairs and eigenvalues
\[
32,\quad21,\quad12,\quad5
\]
agree by written substitution with the proved basis and spectrum formula.

This is review of the supplied claim only. It is not an independently selected instance, executed finite check, certificate replay or whole-level-eight result.

## 5. Boundary and residual claims — SUPPORTED as limitations

**Candidate references: S1 lines 431–461.**

At the author’s next boundary \(d=h-1\), with \(a=b=1\) and \(r\le s\), one has \(n=s+1\). The \(W_1\) target is
\[
(0,1,s),
\]
and the attempted strict inequality becomes equality:
\[
n-1=s=r\cdot0+s\cdot1.
\]
The target is the nonzero top of the actual \(e_2\) node-3 string. Its survival follows from \(F_3e_2=0\), weight \(-s\), local nilpotence, and the nonzero Levi generator.

This establishes failure of the **target-vanishing argument**, not a nonzero cancellation term or a defect witness. The candidate correctly makes neither stronger inference.

Additional edges are handled correctly:

- At \(d=0\), the quotient sector has one basis vector; the general proof and explicit string proof remain valid.
- At \(d=h-2\), the lowering-target inequality still has margin at least one.
- If \(h=1\), the theorem’s band is empty.
- Zero quotient components satisfy all stated automorphism/kernel conclusions with their usual zero-space meanings.
- No argument extends the theorem to zero/nonpositive \(h_3\)-weight or to the rest of the positive-weight corridor.

## 6. Per-claim verdict

| Claim | Verdict | Source lines / basis |
|---|---|---|
| Full-Cartan row convention and \(m=2n-ra-sb\) | **SUPPORTED**, conditional on displayed presentation | S1 9–18, 92–99; S5 16–38 |
| Band implies \(n\ge4\), \(m\ge|r-s|+4\) | **SUPPORTED** | S1 149–157; §2 above |
| All seven positive-charge lowerings vanish on the entire component | **SUPPORTED** | S1 160–191; complete charge audit above |
| \(G_{00}=1\), \(W_0=F_3\), and exact \(\overline A_n=E_3F_3\) | **SUPPORTED** | S1 124–145, 193–200 |
| \(EF\) injective at positive weight under \(E\)-local nilpotence | **SUPPORTED** | S1 204–231 |
| Entire-component invertibility and no cancellation | **SUPPORTED** | S1 231–237 |
| Every zero-primary chain absent; full projected seed-span equality | **SUPPORTED** | S1 239–244; S3 9–22; S6 305–335 |
| Ordinary free-Lie elimination and \(n+1\) source basis | **SUPPORTED** | S1 257–281 |
| Matching to actual \(L(V)\), including \(n=0,1\) | **SUPPORTED**, at f276 source boundary | S1 283–303; S4 7, 19 |
| Both whole Levi seed modules and mixed ideal contributions included | **SUPPORTED** | S1 305–333; S4 9–10 |
| No hidden positive relation from negative Serres | **SUPPORTED**, specifically conditional on f276 full-ideal/direct-sum import | S1 316–320; S4 9, 19 |
| Actual quotient basis and dimension \(d+1\) | **SUPPORTED** | S1 322–342 |
| \(F/E\) coefficients, lowest vectors and string lengths | **SUPPORTED** | S1 346–393 |
| Eigenvalues, positivity, distinctness and basis | **SUPPORTED** | S1 395–412 |
| Supplied four-dimensional level-eight illustration | **SUPPORTED as a written consequence**, not independently computed | S1 414–429 |
| Next-boundary target survival and failure of strict saturation | **SUPPORTED as a limitation** | S1 439–450 |
| Rest-of-corridor no-cancellation, global \(B_8=0\), whole-level-eight saturation/lowering vanishing | **INCONCLUSIVE / NOT ESTABLISHED** | Explicitly excluded at S1 452–461 |
| All-level \(J=\tau\), source authentication, novelty | **INCONCLUSIVE / OUTSIDE REVIEW** | S1 458–459; S4 27 |

No candidate mathematical claim was refuted. The expressly excluded stronger claims are not findings against it.

## 7. Process chronology and exclusions

1. Before scientific packet access, I read the complete manifest, freeze receipt, dispatch receipt, parent metadata supply and all **seven** named status-only controls.
2. I delivered an administrative pre-body ACK to Main; the tool reported delivery.
3. I then read the complete ordered packet in raw windows of at most 20 LF, including every ending. Mathematical reconstruction began only afterward.
4. Hashes, counts and native clock observations are attributed to the parent metadata. The parent message reports its observation at **2026-10-30T09:08:45-0700 PDT**. This is not a reviewer start, derivation or completion timestamp. No child-native clock/hash or continuous-supervision certificate is claimed.
5. The author’s initial ordinary packet preview before its controls remains the **disclosed chronology deviation** at S1 lines 465–466. The subsequent complete reread and pre-derivation control sequence are the author’s report, not independently observed cognition. I do not replace that disclosure with a clean initial pre-body claim or automatically classify it as mathematical contamination.
6. The author’s fresh supplied example was permitted by its restored general-author scope. That authorization did not widen this reviewer’s written-only method.
7. No scientific executable, interpreter, CAS, solver, enumeration, certificate replay, build, lint, test, formatter, new selected instance, outside-model CLI, scientific web source or author code was used. No sibling output, held payload or excluded linked consumer was opened. The explicitly supplied S6 review was read as an authorized frozen input.
8. The own-wave process-file write was refused. No alternate-path or shell writer was used; frozen sources and historical records were not edited or deleted.

## 8. Overall verdict

**overall_correctness: correct**

**explanation:** At the named displayed full-Cartan and f276/f314 whole-ideal boundaries, the candidate proves the universal upper-Serre-gap reduction to \(E_3F_3\), entire-rootspace invertibility, full zero-primary absence and no cancellation. Its separate actual-quotient nonvacuity and explicit spectrum proof also reconstructs successfully, without implying global \(B_8=0\), whole-level-eight vanishing or all-level \(J=\tau\).

**confidence: 0.98**

**Assurance ceiling:** disjoint same-harness **written support for the conditional claims above**. No human, independent-model-family, formal/kernel, numerical, original-source-authentication, priority or novelty certification.