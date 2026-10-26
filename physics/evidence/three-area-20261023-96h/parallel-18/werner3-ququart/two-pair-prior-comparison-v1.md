# Two-pair reference theorem: matched primary-source comparison v1

Before-creation clock observed: **2026-10-23T15:16:20-07:00**. Owner: PhysicsResearch96h. This is source/status work while new candidate generation is paused for the actual independent reconstruction. No scientific execution or external model was used.

## 1. Verdict and exact candidate pin

Candidate compared:

`proof-two-pair-reference-asymmetric-domination-v1.md`, SHA256 **`c882c5678969a80d0b7c9800dc9086070cf3f70f7b9143c0f08e77db41292478`**.

Its complete dependency manifest is `two-pair-candidate-manifest-v1.json`, SHA256 **`6b16b61e9f2cae541c2f1e4df79f0b5a55e6f8cc0013c255ffbc60a63271370b`**.

The exact candidate is full256-dimensional **-3C_B<=S_eta<=C_B** for eta with Schmidt coefficients(a,a,b,b), and the resulting q3 nonnegativity for rank<=2 coefficient operators whose range or co-range contains `first-site ray tensor eta`, with arbitrary other ray and covectors. It is not unrestricted W4.

**Bounded source outcome:** the actual theorem statements read below do not contain this entire reference class. Section3 supplies an explicit operator outside the literal hypotheses of all the named closed three-copy sectors, and outside the old local reference classes. This is a strict **hypothesis noncontainment** result, conditional on the new candidate's mathematical validity; it is **not** a certification of scientific priority, a claim that this one example was previously hard, or proof that no combination of known techniques can already yield the new class.

**Novelty remains UNCLEARED.** No exact matched public theorem for this full class was found in the bounded sources actually read. Several additional papers were screened only at abstract level, the literature was not exhausted, and the complete candidate itself is still undergoing reconstruction. A negative search cannot turn either gate into PASS.

## 2. Actual primary sources and read scopes

All accesses below were read-only on23October2026. Dates are the source's version/publication labels, not invented access timestamps or proof-verification dates.

| Source | Actual read scope | Exact scope comparison |
|---|---|---|
| Wu-Zou, *Sharp Plucker Geometry for Three-Copy Werner Distillation*, arXiv2608.02647v1,31July2026: <https://arxiv.org/html/2608.02647v1> | Retained full primary text; for this comparison re-read Cor6.1/6.2, Prop7.1, Theorems7.2/7.3, full Lemma7.4 proof and AppendixC statements/proofs relevant to their hypotheses. Current unversioned abstract and Atom query were freshly read; the latter returned the v1 link. | Normal rank-two; common initial-final two-plane; one local output/input support overlap<=2; **fully product** ray in range or co-range; local-traceless; crossed locally orthogonal product codes. None states arbitrary biseparable entangled reference rays with the other ray/covectors unrestricted. |
| Ulam, *Structured Multicopy Werner Bounds*, archive label29July2026: <https://www.ulam.ai/archive/structured_multicopy_werner_bounds.pdf> | All six extracted pages, especially Definition of admissibly block-product pairs, Thm1.2, Prop3.2, Cor3.4, Prop4.1/Cor4.2 and final limitations. | It treats **coherent sums**, not just tensor-factorized operators. Both rank-one terms must factor over a common admissible block partition. For three sites this imposes a common2+1 product structure, unless one large padding block has common range/co-range. The candidate imposes no such condition on the second ray or covectors. |
| Ulam, *Obstructions to Werner Distillation*,31July2026: <https://www.ulam.ai/archive/obstructions_to_werner_distillation.pdf> | All six extracted pages, exact Thm1.1 and its code-envelope/local-support definitions and proofs, Prop4.1/4.2. | At three copies the spectator criterion needs at least one local row/column support overlap<=2; the code criterion needs range or co-range inside tensor products of one-/two-copy code spaces of dimension<=2. A single biseparable ray does not imply either whole-plane envelope. |
| Bharti-Gajjala-Haug, arXiv2607.24479v1,27July2026: <https://arxiv.org/html/2607.24479v1> | Retained full primary source; exact Prop8.2, Thm8.3, Cor8.4 and finite-copy/outlook boundary re-read here. | Its finite-copy endpoint theorem assumes an actual operator tensor factorization with any rank-two core confined to a block of at most two copies. Its general finite-copy parameter bound is not unrestricted alpha=-1/2 three-copy positivity. |
| Fraser-Huber-Pozsgay-Vona, arXiv2607.24309v1: <https://arxiv.org/html/2607.24309> | Current primary abstract, contribution TheoremA and CorB/C, two-copy-only application scope; full returned text searched for higher-copy/reference terms. Not a full independent proof audit. The arXiv header says27July2026 and the typeset page says24August2026; no chronology is inferred from that discrepancy. | Its rank-r bipartite partial-trace inequality and unrestricted **two-copy** classification are prior results, not a new task or an automatic three-copy induction. No matched paired-reference three-copy theorem was located in the read scope. |
| Song-Chen2607.23416,26July2026: <https://arxiv.org/abs/2607.23416>; Fu-Gao-Park2607.21367,23July2026: <https://arxiv.org/abs/2607.21367> | Current abstracts only. | Two-copy results, including the former's two-parameter/two-state activation extension. No whole-proof absence claim is made for unread corollaries. |
| Costa Rico2310.05726: <https://arxiv.org/abs/2310.05726>, first posted9October2023, later LMP115(2025)47 | Current abstract and the precise older opposite-sign Hermitian scope as quoted/used in the Wu-Zou primary. This is not a fresh full-body audit of every proposition. | Prior partial-trace/distillability methods are credited. Their known Hermitian/normal sector is not replaced by the new arbitrary-complex nonnormal reference claim. |
| Anonymous qutrit candidate, version1.1.0-candidate,4October2026: <https://raw.githubusercontent.com/ipitchford/three-copy-werner-undistillability/main/README.md> and <https://raw.githubusercontent.com/ipitchford/three-copy-werner-undistillability/main/CLAIMS.json> | Current actual README and exact claims/exclusions. Earlier retained manuscript access is in the lane's original source gate; no certificate replay occurred here. | Claims unrestricted **27x27, three qutrits** and expressly excludes unrestricted higher local dimensions. It is an unrefereed computer-assisted candidate, not an accepted theorem imported into this proof. The new class allows full four-dimensional local supports. |

Current arXiv version route actually read: <https://export.arxiv.org/api/query?id_list=2608.02647>. The returned feed linked <https://arxiv.org/abs/2608.02647v1>. The retained Wu-Zou primary text pin from the original source capture is `14c6b3a89eceab623fa7af079b930e4045695f7a0c73bd43380d5a87e099db99`.

### The imported architecture is not itself new

Wu-Zou Lemma7.4 explicitly gives the switched Schur order `D-L A^-1 L†`, the reversed co-Choi convention, the three one-site reducing blocks, and the sufficient tensor-contraction argument for fully product references. Its printed one-site matrices already determine the generalized eigenvalues1,-1/3 by elementary diagonalization. The asymmetric interval[-3,1] is a direct sharpened use of those existing matrices, not a claim to have invented the switched-complement framework.

The candidate's possible mathematical contribution is the **full physical256-dimensional domination for a nonproduct paired-Schmidt reference**, with all angles and arbitrary other ray/covectors, not the already-known low-copy theorem, product-reference mechanism, or a search framework.

## 3. Explicit strict noncontainment test

This is a written **scope witness**, not a numerical q3 test or a negative Werner witness. It is included only to prevent a new class from being declared distinct by vague wording.

Use all indices modulo4 where indicated and set

`u=(4|000>+4|011>+|022>+|033>)/sqrt(34)`,

`x=(|001>+|112>+|223>+|330>)/2`,

`y=(|002>+|113>+|220>+|331>)/2`,

`C=|u><u|+|x><y|`.

The three vectors u,x,y are exactly orthonormal: their displayed computational supports are disjoint, and their squared coefficient sums are1. Therefore

`rank C=2`, `ran C=span{u,x}=E`, `ran C†=span{u,y}=F`,

`CC†=P_u+P_x`, `C†C=P_u+P_y`, `Tr C=1`.

It is genuinely nonnormal and `dim(E+F)=3`.

The ray u is first-site-biseparable with the nonuniform two-pair spectrum `(4,4,1,1)/sqrt(34)`, so the **candidate** covers C. No value of q3(C) is computed here and its nonnegativity is not used to prove noncontainment.

### 3.1 Full local support and nonzero partial traces

Both x and y have one-site density matrices I4/4 at all three sites. Hence every minimal one-site support of E and F is C4. For Wu-Zou Thm7.2 and the Ulam spectator criterion all three overlaps are therefore

`Tr(P_i Q_i)=4`,

not<=2. Also `Tr(Tr_i C)=Tr C=1`, so none of the three local partial traces vanishes. The local-traceless theorem does not apply.

### 3.2 No fully product ray in either plane, even after choosing another basis

For any nonzero coefficient beta, a vector `alpha u+beta x` has single-site Schmidt rank at least3 across **every** one-versus-two cut. Project onto the three first-site labels1,2,3 of the x branch: these supply distinct, nonzero computational coordinates in distinct rows across each cut, whereas u has first-site label0 and cannot cancel them. The same argument applies to `alpha u+beta y`.

When beta=0, u has Schmidt rank1 across the first cut but rank4 across each of the other cuts. Thus neither E nor F contains a fully product ray. In fact their only biseparable ray is u, across the first cut.

Consequently Wu-Zou Thm7.3 does not apply. Cor6.1 fails by the explicit nonnormality, and Cor6.2 fails because the joint initial-final plane dimension is3.

### 3.3 No common block-product decomposition or two-dimensional code envelope

Across the first cut, E has only one product ray u, so it cannot be spanned by two independent product vectors. Across the second and third cuts, u already has Schmidt rank4; a span of two product vectors across either cut would make every vector in that span have Schmidt rank at most2, a contradiction. The same holds for F.

Hence no choice of a degenerate singular basis can supply the two independent product left vectors required by the Ulam common2+1 block theorem. This argument excludes an admissible rank-one decomposition, not merely the particular two branches written above. A one-block three-copy padding case would require coincident rank-one ranges or co-ranges and make C rank<=1, also impossible. The actual operator-tensor-factorized subclass of Bharti-Gajjala-Haug is correspondingly excluded.

For Ulam's two-dimensional code envelope, every possible singleton block already has local range/co-range support dimension4. A three-site partition into blocks of at most two must include such a singleton. Neither E nor F can lie in the required envelope.

For Wu-Zou AppendixC.2, a vector in a locally orthogonal product-code span has first-site Schmidt rank equal to the number of nonzero codeword coefficients. If that rank is1 it must be a single fully product codeword. The entangled two-site reference u is therefore not in any such code span, so no range code containing E can meet that theorem's hypothesis.

### 3.4 The two-copy theorem is not a rank-preserving induction

For this same C,

`Tr_1 C=|eta_hat><eta_hat|+(1/4)sum_i |i,i+1><i,i+2|`,

where `eta_hat=(4|00>+4|11>+|22>+|33>)/sqrt(34)`.

The second summand has rank4, with both range and co-range orthogonal to the diagonal support of eta_hat. Thus `rank(Tr_1 C)=5`. This explicitly blocks simply applying a rank-two two-copy theorem to the traced operator. It does not rule out every possible use of known all-rank inequalities, and is not offered as a claim that q3 of this particular example is difficult.

### 3.5 Strict delta from the old local reference results

The only biseparable ray in E or F is u. Its two-site Schmidt coefficients are nonuniform rank4, neither the earlier uniform Omega4 nor embedded uniform Omega3 class, under any site permutation. In standard Schmidt coordinates its normalized reference has inner product `5/sqrt(34)` with Phi4, so its distance from Phi4 is greater than1/2 (`1600<1666` after squaring the equivalent inequality). It is far outside the earlier conservative radius1/207424 ball. Maximizing overlap with a maximally entangled ray gives the same Schmidt-coefficient sum, so a local-unitary rotation cannot turn that small-ball condition into coverage.

Moreover the earlier exact C_B+S_eta obstruction at unnormalized eta=(1,1,1/4,1/4) excludes the old **symmetric** GS premise for this reference. The new asymmetric candidate is therefore a real enlargement relative to that local sufficient route, not a re-labeling of its already-positive angles. This does not make the full W4 target solved.

## 4. Equivalent reference description included in the screen

Apply on the second ququart the unitary J with

`J|0>=|1>`, `J|1>=-|0>`, `J|2>=|3>`, `J|3>=-|2>`.

It sends eta_t to

`|01>-|10>+t(|23>-|32>)`.

Thus paired-Schmidt, two orthogonal singlet blocks, and an antisymmetric/skew-symmetric representative are relevant descriptions of this same reference family. They were included in the matched searches. This elementary explicit unitary does not itself establish a new theorem or certify that antisymmetric-reference corollaries are absent from the broader literature.

## 5. Public claim inventory screens and limitations

- `openai/math` current CONTENTS: <https://raw.githubusercontent.com/openai/math/main/CONTENTS.md>, freshly read earlier in this bounded source wave, header719 manuscripts/372 result families. The full returned inventory was searched for Werner, NPT, distillability, qutrit, Schmidt, partial-trace and entanglement terms. No direct W4/paired-reference family was found; unrelated ground-state-area-law, photon-number and secret-key/PPT-channel entries are not the same claim. This is an inventory/abstract screen, not an audit of every paper or Lean artifact.
- Ulam archive <https://www.ulam.ai/archive>: the actual returned title/abstract data led to the two full primary papers read above, plus the known two-copy spectral-gap paper. Their limitations are treated by exact hypotheses, not merely by their titles.
- EulerSolve's first negotiated home response was insufficient. The actual public HTML supplied its Papers route, and <https://eulersolve.org/papers/> was then read. Its complete returned407-item title/abstract-snippet index was searched for Werner, distillability, NPT, co-Choi, biseparability, ququart and partial-trace terms, with no match. This does not audit407 proof bodies or certify absence of an indirectly stated corollary. All the site's items are explicitly unrefereed.
- Initial broad web queries sometimes returned irrelevant persons named Werner Schmidt or commercial pages. They provide **no** negative scientific evidence. Narrower three-copy/antisymmetric searches returned the matched Wu-Zou primary and the qutrit candidate, which were checked directly. Other search misses are not novelty certificates.

The unresolved prior-art task is not an invitation to run extra scientific controls: it is whether an existing result, including a corollary under another representation, already gives this full paired-reference class. That gate remains open. The actual distinct reviewer and parent must separately decide the candidate's mathematical status; no source screen substitutes for reconstruction.

## 6. Completion boundary

This audit establishes an explicit scope distinction from the named primary theorem statements read, with a checkable rank-two hypothesis witness. It does not establish first priority or publishability. It does not accept the external qutrit certificate or use a quota/access condition as mathematical evidence.

The complete candidate and its six leaves remain frozen for MathSemigroup's actual reconstruction under the parent's review wave. No new theorem/corollary packet is generated here. Full W4 and the broader book questions remain NOT PROVED, and no further scientific execution has been admitted.
