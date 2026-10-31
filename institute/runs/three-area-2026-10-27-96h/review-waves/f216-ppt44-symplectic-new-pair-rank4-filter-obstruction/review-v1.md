# f216 independent same-harness written review

**Disposition: 0 FATAL / 0 MAJOR / 0 MINOR for the reconstructed mathematical claims; 3 INCONCLUSIVE categories:** Park attribution/map-normalization equivalence; prior-art/novelty/priority; and the author's reported execution history and chronology. None of these inconclusive categories is used as a premise for the mathematical conclusions. The concrete 6×6 pair and the stated general `k,d` compression/filter obstruction are supported by the written reconstruction below. The obstruction is for this witness family only. The original unrestricted 4×4 PPT/Schmidt-number-3 target remains open as the pinned parent disposition states; this review is not a global no-go theorem.

Native clock observed immediately before writing this report: `2026-10-29T13:30:33-0700 PDT`. This is a clock observation, not an assertion of file creation time.

## Frozen inputs, measurements, and sequence actually followed

1. First research artifact opened was the assigned `manifest-v1.json`. Its measured SHA-256 was `a4ffc39dea6c49369166016756d2bda31bf154aed74fdd3307b38d7e2f6591ad`, matching the assigned `a4ffc39dea6c` prefix. A truncated manifest line 29 was then read in full at `:raw:29-29`. No mandatory errata were listed as inputs.
2. Before opening either input body, measured SHA-256, byte count, and LF count for both input files. Both matched every manifest value:

   | Manifest order and role | Full SHA-256 | Bytes | LF |
   |---|---|---:|---:|
   | `institute/runs/three-area-2026-10-27-96h/dispositions/physics-3-ppt44-z-correlated-decomposability-parent-v1.md` — adopted context | `a0912ca962a91a7cfead6467dee59e87df9e947576a9e1eb8756f2e1d9a2a4f5` | 6886 | 23 |
   | `physics/evidence/three-area-20261027-96h/parallel-18/ppt-schmidt44/frontier-20261029-symplectic-new-pair-rank4-filter-v1.json` — target | `2e0cd19c588b20644f371b1362f3dc6be19dd65a27610495bd9b51c2cde5fdf9` | 6999 | 13 |

3. Read the entire first input, including its end, as short raw windows `1-8`, `9-16`, `17-23`. Then read the entire target, including its end, as short raw requests `1-7`, `8-14` (the latter reaches EOF). A first attempt at the target had a mistyped home-directory component and returned path-not-found without displaying a body; it was immediately corrected. The two declared input bodies were thus displayed in manifest order before any mathematical reconstruction or control. An administrative memory summary was consulted after the manifest and fingerprint measurements, and was not used as scientific evidence.
4. Reconstructed the claims below and wrote and ran only the reviewer-owned bounded control described in the receipt. No linked input bodies, author script, author PASS or solver status, external search/API, other model, sibling review, author contact, held material, or Git was used. Parent disposition claims A/B/C were not needed for the algebra here; only its expressly stated original-target status is carried forward at its stated scope.

## Per-claim verdicts

`0F/0M/0m` means no fatal, major, or minor defect found in the written argument, not a proof-assistant or novelty certification.

| Claim | Verdict | Scope and reason |
|---|---|---|
| Concrete `d=6,k=2` pair, real `J=[[0,I_3],[-I_3,0]]`: `R=I+F+[vec J]` is PPT; `W=2I-2F-[vec J]` is 2-block positive and `Tr(WR)=-12` | 0F/0M/0m | Reconstructed exactly, including the Bob partial transpose. `R` is unnormalized; `Tr R=48`, so normalized pairing is `-1/4`. |
| General even `d`, integer `1≤k<d/2`, skew-unitary `J`: `R_d` is PPT, `W_(k,d)` is k-block positive, and their pairing is `d(2k-d)<0` | 0F/0M/0m | Direct skew-part/nuclear-norm proof, plus explicit PSD expressions for `R_d` and `R_d^Γ`. The negative pairing also proves this `W` indecomposable. |
| Skew-Takagi normal form and canonical input compression for an arbitrary `2k`-plane, including paired singular values, complement capacity, zero and unit singular-value endpoints | 0F/0M/0m | Reconstructed constructively using a skew anti-linear operator; the complement coordinates exist because the nonzero rows of `N` are orthogonal. |
| All-variable identity `C_U=P+Q^{Γ_A}` with the stated PSD sums | 0F/0M/0m | Proved by the four-dimensional outside-block identity and a vector-valued Lagrange identity, without author scripts or a search. |
| Any Alice filter of rank at most `2k`, arbitrary Bob filter, any PPT source: pairing is nonnegative; likewise with Alice and Bob interchanged | 0F/0M/0m | Factorization through a `2k`-plane and the explicit conjugated-filter formula preserve decomposability. The second orientation follows from swap symmetry. This does **not** say arbitrary-rank filters on both sides cannot detect: identities already give the negative pairing above. |
| Park arXiv:2602.09860v1 attribution, identification of the map family, and the claimed fixed-Bob-unitary/positive-normalization relation | INCONCLUSIVE 1 | Named external import/prior-art claim in the packet; external expansion was forbidden, and these source-specific statements were not reconstructed from the declared inputs. They are not used in any proof here. |
| Whether this pair or compression obstruction is novel, previously known, or has priority | INCONCLUSIVE 2 | No prior-art or novelty determination was attempted. `new` is a packet label, not a novelty finding. |
| Author-reported polynomial checks, file execution, and post-contact chronology | INCONCLUSIVE 3 | Not independently audited and not evidence for this review; no author code was opened, run, imported, or compiled. |
| Claimed limitation to this family and inherited open status of the original unrestricted 4×4 target | 0F/0M/0m at this stated scope | The proof gives only the stated witness-family obstruction. The parent expressly records the target as open; no wider nonexistence or present-day literature survey is asserted. |

## Definitions and the PPT source

Fix `vec(Y)=Σ_ij Y_ij |i⟩|j⟩`, `F|i,j⟩=|j,i⟩`, `[v]=|v⟩⟨v|`, and take `Γ_B` in the displayed computational output basis. Let `J^T=-J`, `JJ†=I`, `j=vec(J)`, and `Ω=Σ_i |i,i⟩`. Then `Fj=-j` and `⟨j,j⟩=Tr(J†J)=d`. Consequently

`R=I+F+[j]=2 P_sym+[j] ≥ 0`.

The partial-transpose orientation is important. In components,

`([j]^{Γ_B})_{ij,ℓm} = J_{im} conjugate(J_{ℓj})`.

The same entry of `(I⊗conjugate(J)) F (I⊗conjugate(J)†)` is `conjugate(J_{jℓ}) J_{mi}`, equal to the preceding expression by skew-symmetry twice. Thus, with `V=I⊗conjugate(J)`,

`R^{Γ_B}=I+[Ω]+V F V†=V(I+F)V†+[Ω] ≥ 0`.

Here `V` is unitary, so the last equality is an explicit sum of PSD operators. Equivalently the middle term is a Hermitian involution. This also explains why replacing `conjugate(J)` by `J` is not legitimate for a general complex `J`. For the concrete real `J`, `conjugate(J)=J` and `conjugate(J)†=J^T`. Positive partial transpose on Alice follows from `R^{Γ_A}=(R^{Γ_B})^T`.

The traces follow without normalizing:

* `Tr R=d²+d+d=d(d+2)`;
* `Tr(FR)=d+d²-d=d²`;
* `⟨j|R|j⟩=d²`, because `(I+F)j=0` and `[j]j=dj`;
* `Tr(W_(k,d) R)=k d(d+2)-k d²-d²=d(2k-d)<0`.

In particular `d=6,k=2` gives `Tr R=48`, `Tr(WR)=-12`, and the normalized PPT state `R/48` pairs to `-1/4`.

## Independent k-block-positivity argument

For a coefficient matrix `Y` of rank at most `k`, let `S=(Y-Y^T)/2`. Because `F vec(Y)=vec(Y^T)`,

`⟨vec Y|W_(k,d)|vec Y⟩ = 2k ||S||_F² - |Tr(J†S)|²`.

The symmetric part of `Y` does not contribute to `Tr(J†Y)` because `J†` is also skew-symmetric. Moreover `rank(S)≤rank(Y)+rank(Y^T)≤2k`. Writing an SVD of `S`, unitarity of `J` bounds each singular-vector overlap by one; hence `|Tr(J†S)|≤||S||_*≤sqrt(rank(S)) ||S||_F≤sqrt(2k)||S||_F`. The displayed expectation is therefore nonnegative for every rank-≤k `Y`.

The negative PPT pairing proves `W_(k,d)` cannot be decomposable: a PSD operator and a partial transpose of a PSD operator each pair nonnegatively with a PPT operator. It also implies the normalized `R_d` is not a convex combination of rank-≤k coefficient-vector projectors. These are conclusions about the displayed `d×d` pair, not a 4×4 counterexample.

## Reconstructing the skew-Takagi compression

Put `m=2k` and let `U:C^m→C^d` be any isometry. Extend its columns by an orthonormal complement `U_perp`. In the input basis and the corresponding output basis `U` followed by `U_perp`, define

`K=U† J conjugate(U)`, `N=U† J conjugate(U_perp)`.

`K^T=-K` and `KK†+NN†=I_m`, since `[U,U_perp]` is unitary and `J` is unitary. Thus `K` is a contraction. The following supplies the canonical form rather than importing it.

For any complex skew matrix `K`, define the antilinear map `T x=K conjugate(x)`. With `⟨x,y⟩=x†y`, skew-symmetry gives `⟨x,Ty⟩=-⟨y,Tx⟩`, and `T²=K conjugate(K)=-KK†`. Let `H=KK†=-T²`. The antilinear `T` commutes with `H`, so it preserves each real-eigenvalue eigenspace of `H`. Choose a unit eigenvector `e` with eigenvalue `λ²>0`, and set `f=-Te/λ`. The skew identity implies `⟨e,Te⟩=0` and `||Te||²=λ²`; hence `e,f` are orthonormal. Also `Te=-λf` and `Tf=λe`. Their span and its orthogonal complement are `T`-invariant: for `x` orthogonal to both, `⟨e,Tx⟩=-⟨x,Te⟩=0` and similarly for `f`. Repeating on the orthogonal complement pairs every positive singular value. On the zero eigenspace `T²x=0` and the same skew identity gives `Tx=0`; its dimension is even here and its basis vectors can be paired arbitrarily. Therefore some unitary change of the common input/output-`E` basis gives

`K = ⊕_(i=1)^k λ_i [[0,1],[-1,0]]`, with `0≤λ_i≤1`.

Write `s_i=sqrt(1-λ_i²)`. In this basis `NN†=⊕_i s_i² I_2`: its nonzero rows are mutually orthogonal and each row of pair `i` has norm `s_i`. If `r` pairs have `s_i>0`, then `rank(N)=2r≤d-m`, so the complement has the needed `2r` coordinates. A unitary change of complement coordinates sends these orthogonal rows to `s_i` times distinct coordinate rows, with signs chosen as below. This includes `s_i=1` and `s_i=0` without a limiting argument.

Writing the paired input/output-`E` coordinates as `x_i=2i-1`, `y_i=2i`, and the two selected output-complement coordinates for a defective pair as `p_i,q_i`, define

`a_i=|x_i,y_i⟩-|y_i,x_i⟩`, `c_i=|x_i,p_i⟩-|y_i,q_i⟩`.

Then the compressed vector is

`j_U=(U†⊗I)j = Σ_i λ_i a_i + Σ_(i:s_i>0) s_i c_i`.

The displayed vectors are mutually orthogonal with squared norm two. The compressed swap `F_E=(U†⊗I)F(U⊗I)` swaps the input with the output on `E` and is zero when the output is in `E_perp`. Thus

`C_U=(U†⊗I)W_(k,d)(U⊗I)=k I-k F_E-[j_U]`.

All these statements use bases, not a restriction to a special `U`; the original `U` may be rotated internally, and the decomposition transports back by local unitaries with the conjugation rule in the filter section.

## PSD/co-PSD identity for every compression

Let the list `u_α` consist of all `a_i` and all `c_i` for `s_i>0`, with corresponding real weights `w_α=λ_i` and `s_i`. By construction

`j_U=Σ_α w_α u_α`, `Σ_α w_α²=Σ_i(λ_i²+s_i²)=k`,

where a zero `s_i` contributes nothing. Let `A_other` contain each unnormalized `|p,q⟩-|q,p⟩`, `p<q≤m`, except the `a_i`. Let `B_other` contain each standard vector `|p,o⟩` with input `p≤m` and output `o∈E_perp`, except the four-coordinate block belonging to each defective pair. For a defective `i`, let

`h_i=|x_i,q_i⟩+|y_i,p_i⟩`.

The identity to prove is

`C_U=P+Q^{Γ_A}`,

`P=Σ_(α<β) [w_α u_β-w_β u_α] + k Σ_(v∈A_other)[v] + k Σ_(v∈B_other)[v]`,

`Q=k Σ_(i:s_i>0)[h_i]`.

Every term of `P` and `Q` is PSD. To verify equality, use the **input** partial transpose `Γ_A`. On the four outside basis vectors `|x_i,p_i⟩, |x_i,q_i⟩, |y_i,p_i⟩, |y_i,q_i⟩`, direct expansion gives

`I_4=[c_i]+[h_i]^{Γ_A}`.

Indeed `[h_i]^{Γ_A}` has diagonal projectors on `|x_i,q_i⟩,|y_i,p_i⟩` and positive cross terms between `|x_i,p_i⟩,|y_i,q_i⟩`; `[c_i]` supplies the two missing diagonal projectors and cancels those cross terms. On `E⊗E`, `I-F_E` is the sum of the unnormalized antisymmetric projectors, while outside `E` it is the identity. Consequently

`C_U-Q^{Γ_A}=k Σ_α[u_α]-[Σ_α w_α u_α]+k Σ_(v∈A_other)[v]+k Σ_(v∈B_other)[v]`.

Expanding the outer products gives the exact vector-valued Lagrange identity

`Σ_(α<β)[w_α u_β-w_β u_α]=(Σ_α w_α²)Σ_α[u_α]-[Σ_α w_α u_α]`.

Since `Σ_α w_α²=k`, this proves the claimed `P`. It does not divide by a singular value or require any general-position assumption; zero weights and a missing `c_i` when `s_i=0` are harmless. The use of unnormalized vectors is consistent throughout: the antisymmetric projector sum is exactly `I-F_E`, not half of it.

## Arbitrary filters and transpose orientation

For any filter `A:C^d→C^d` with `rank A≤m`, choose a `d×m` isometry `U` whose range contains `ran A`, and write `A=UC` with `C=U†A` of size `m×d`. For any Bob filter `B`,

`(A⊗B)† W (A⊗B)=(C⊗B)† C_U (C⊗B)=P'+(Q')^{Γ_A}`,

where

`P'=(C⊗B)†P(C⊗B) ≥ 0`,

`Q'=(conjugate(C)⊗B)† Q (conjugate(C)⊗B) ≥ 0`.

The conjugate on `C` is required: it is obtained by expanding the input partial transpose, not by moving `B` across the transpose. For a PPT `σ`, `σ^{Γ_A}=(σ^{Γ_B})^T≥0`, and self-adjointness of partial transpose under the trace yields

`Tr[W(A⊗B)σ(A⊗B)†]=Tr(P'σ)+Tr(Q'σ^{Γ_A})≥0`.

The identity also handles rectangular intermediate `C`, rank zero, smaller ranks, and arbitrary complex local filters. `F W F=W` because `Fj=-j`. Swapping the subsystems exchanges the PPT orientations, so the same conclusion holds if instead `rank B≤2k` and `A` is arbitrary. In the specific `d=6,k=2` pair this excludes negative pairing from either local filter of rank at most four against **any** PPT source, including `R/48`. If both local ranks are unrestricted, it is false to claim a general obstruction: `A=B=I` with `σ=R/48` gives `-1/4`.

## Reviewer-owned exact controls and receipts

The controls are finite sanity checks of the independent algebra, not universal proofs. The only script used was `reviewer-f216-controls-v1.py` in this wave directory, written independently with Python standard-library sparse matrices and exact Gaussian rationals. Measured SHA-256:

`13aea9b4ba63bd3b6c3e5d83ed84f2c1e0df8dcd09fe1b840d1e47a54c095f32`.

Native clock observed before writing the script: `2026-10-29T13:27:16-0700 PDT`. First bounded invocation, `python3 reviewer-f216-controls-v1.py`, was bracketed by `/bin/date` observations `2026-10-29T13:29:05-0700 PDT` and `2026-10-29T13:29:09-0700 PDT` and returned normally. A second receipt-bearing invocation of the unchanged script used a 120-second subprocess timeout: `/bin/date` start and end both `2026-10-29T13:29:53-0700 PDT`; explicit **exit code 0**, stderr empty, no timeout. All hashes and clocks are observations, not asserted filesystem creation times.

For each row below, exact entrywise calculations checked skew-unitarity; the PSD sums for `R` and `R^{Γ_B}` and both transpose orientations; `Tr R`, `Tr(WR)`; the actual compressed swap/vector; and `P+Q^{Γ_A}=C_U`. The same checks were repeated after a non-real diagonal unitary congruence of `J`, with the conjugated input phase applied to `Q`.

| `d,k` | `(λ_i,s_i)` | Defective pairs | Result |
|---|---|---:|---|
| 4,1 | `(0,1)` | 1 | Exact equalities passed |
| 6,2 | `(3/5,4/5)`, `(1,0)` | 1 | Exact equalities passed |
| 6,2 | `(1,0)`, `(1,0)` | 0 | Exact equalities passed |
| 8,2 | `(3/5,4/5)`, `(5/13,12/13)` | 2 | Exact equalities passed |
| 8,3 | `(1,0)`, `(0,1)`, `(1,0)` | 1 | Exact equalities passed |
| 10,3 | `(3/5,4/5)`, `(5/13,12/13)`, `(1,0)` | 2 | Exact equalities passed |
| 12,3 | `(3/5,4/5)`, `(5/13,12/13)`, `(8/17,15/17)` | 3 | Exact equalities passed |

The literal requested real `J_0=[[0,I_3],[-I_3,0]]` was checked separately. With zero-based standard basis labels, the exact orthogonal basis with columns

`e_0, (3e_3+4e_1)/5, e_2, e_5, (4e_3-3e_1)/5, -e_4`

transformed `J_0` to the one-defect `d=6,k=2` canonical instance in the table. For this actual pair, the controls obtained `Tr R=48`, `Tr WR=-12`; a rank-two vector `|0,3⟩+|1,4⟩` saturates at zero. Forty seeded, explicitly rank-at-most-two real matrices `Y=Σ_(t=1)^2 u_t v_t^T` had nonnegative expectations, smallest `129`; these samples do not establish the universal inequality.

Intended-reason negative controls, all exact:

1. Dropping one nonzero Lagrange outer-product term from the one-defect `d=6` decomposition produces 16 incorrect matrix entries; the first zero-based difference is `(1,1)=-1`.
2. In its complex-congruence version, incorrectly applying `Γ_B` to the transformed `Q` instead of the required `Γ_A` produces two incorrect entries; first difference `(4,11)=4i`.
3. In the complex source formula, replacing the required `conjugate(J)` twist by `J` produces 48 incorrect entries; first difference `(0,10)=-(24/25)i`.
4. PPT is necessary: `y=|0,3⟩+|1,4⟩+|2,5⟩` has `⟨y|W|y⟩=-3`, remains unchanged by the rank-four Alice projection onto `e_0,…,e_3`, and its PSD source `[y]` is not PPT: `|0,4⟩-|1,3⟩` has expectation `-2` under `[y]^{Γ_B}`. This does not contradict the PPT-source theorem.

## Imports, remaining gap, and deviations

The only cited external mathematical attribution in the target, Sang-Jun Park, arXiv:2602.09860v1, including any statement about a normalized generalized Breuer–Hall map and a local-unitary equivalence, remains a **named, unverified external import**, not reconstructed truth or a necessary hypothesis for the proof above. The adopted parent disposition contains a named Yang–Leung–Tang import for its separate 4×4 phase-covariant claim A; this review does not use that theorem. No author's checks or linked prior results were accepted as evidence. No external source was opened and no novelty or priority search was performed.

The remaining substantive gap is the unrestricted original 4×4 PPT/SN3 question: this family-specific compression obstruction neither solves nor excludes other sources, witnesses, or maps. Park equivalence and prior art remain unresolved under the review's source restrictions. The reported source execution and chronology likewise remain unaudited.

Deviations: no substantive deviation from the frozen contract. The single mistyped, unsuccessful input path attempt and the administrative memory read are disclosed in the sequence above; neither displayed an undeclared scientific input or changed the input read order. The reviewer control was run twice, each time within its 120-second bound, to obtain an explicit exit-code receipt. No author file was edited; no files were deleted or published, and no Git, infrastructure mutation, project build, lint, test suite, or formatter was run.

**This is same-harness review, not human review, independent-model-family review, formal/kernel verification, or novelty verification.**
