# f41 disjoint scientific review — a character square against arbitrary mates

Reviewer **InfoBalancedNL242-2-2**, separate info-6 owner; author PhysicsMOQLS8-2. Actual native review-start observation **2026-10-28T17:36:26-0700 PDT**; native `/bin/date` observed before this write **17:39:14 PDT**. Assignment was read first, the previous local scientific step was completed/pinned, and then the complete candidate was reconstructed. No author contact, nested agent, external-model CLI or paid API was used.

## Verdict and original-object boundary

**NO_SUBSTANTIVE_DEFECT AT THE STATED SCOPE: 0 FATAL / 0 MAJOR / 0 MINOR.** The zero-plane calculation, all three classical-mate exclusions, arbitrary-complex-mate support argument, rank-one two-mate dimension obstruction, and finite corroborations are reconstructed below. Thus in every actual ordinary four-MOQLS(8) family a member of the stated binary-character form is classical; the other three members remain arbitrary complex QLS. More strongly, a nonclassical member of that form has no classical mate, and a rank-one member has no two mutually orthogonal mates.

The theorem is **not** a reduction of an arbitrary QLS to character form; it does not resolve the unrestricted mixed four-family, supply a nonclassical family, establish M(8), novelty or priority, or constitute Lean/kernel, human or independent-model acceptance. Parent adoption remains a separate decision.

## 1. Inputs and exact physical setup

- Assignment `review-waves/f41-moqls-character-square-all-mates/assignment-v1.json`, SHA-256 `c0a657c741f4e842a6f32e1531638d3ff54eb859d6c23713dc4acf0fc3a98500e`, 22 LF, read before the candidate.
- Candidate `frontier-20261028-character-square-all-mates-v1.md`, SHA-256 `facbb32afca0f9715efa5fbc415c8f0af4e5cc3e0f8c7a5dd6918f75ae22344b`, 159 LF, read completely in raw windows 1–53, 54–106 and 107–159.
- Registered `physics-4-four-family-definitions-v1.md`, SHA-256 `ebfd79fe2fba3aab2d4b61b29688e66199718ff789a3a922c8bc2e38277bdfee`, 9 LF, and the physical [Ball–Simoens source](https://arxiv.org/html/2607.12933v2) §§2.2–2.3 were checked during my immediately preceding f24 review. That review, `frontier-review-f24-moqls-binary-character-classicality-v1.md`, SHA-256 `023eccbfb8cf9d70f3b4b5d82360831a55ab8893a7f98faffde1eaccf2ea4eb9`, 84 LF, independently reconstructs the predecessor character caller; the necessary part is re-established here.

Ordinary QLS have an ONB in each row and column, and two squares are orthogonal iff their 64 SAME-cell product vectors form an ONB. Each member may independently change output basis and phases; pair-product orthogonality is unchanged. A classical member uses rays from one global ONB, hence each such ray occurs once in each row and column.

For f,g permutations of V=F₂³, output relabelling y=g(x) and row phases reduce the specified member to

    ψ^F_{i,j}=8^(−1/2)Σ_y(−1)^{i·F(y)+j·y}|y>,    F=f∘g⁻¹, F(0)=0.

Fixed-row character sums show that g must be a permutation and columns similarly require f; the converse is immediate by character orthogonality. Additive F yields only Fourier-basis rays. Conversely, the first row is a Fourier ONB; if all cells are classical, comparing each `(i,0)` with a first-row ray and evaluating at y=0 fixes its phase and shows every `i·F(y)` is linear. Nondegeneracy makes F additive. These transformations are memberwise physical unitaries/phases, not an arbitrary-family WLOG assumption.

## 2. Walsh-zero planes and the three classical-mate cases

Each coordinate of a permutation F has even truth-table weight, so its cubic multilinear coefficient vanishes; with F(0)=0, F has degree ≤2. Its B_F(x,y)=F(x+y)+F(x)+F(y) is alternating bilinear, represented by β_F:Λ²F₂³→F₂³. Let r=rank β_F. F is additive iff r=0.

For u≠0, q_u(x)=u·F(x) is balanced. Its alternating scalar polar form has rank 0 or 2. In a fixed basis define J(u) from the three polar coefficients `(b_u(e₂,e₃),b_u(e₃,e₁),b_u(e₁,e₂))`; this is linear, has rank r, and its nonzero value is the unique radical vector t_u. Directly expanding the square of W(u,v)=Σ_x(−1)^{q_u(x)+v·x} gives

    W(u,v)²=8 Σ_{h∈rad b_u}(−1)^{q_u(h)+v·h}.

For J(u)≠0, balance W(u,0)=0 forces q_u(Ju)=1; hence W(u,v)=0 iff v·J(u)=0 and its other four values have magnitude 4. For nonzero u∈ker J, q_u is a nonzero linear character, so exactly one nonzero column has W=8. These statements cover all u,v, including the kernel and zero row.

If a classical mate exists, follow any one of its basis rays: its eight cells form a row/column transversal `(a,π(a))` for a permutation π. Pair-product orthogonality makes the selected character-square entries at those cells orthogonal, hence

    W(a+b,π(a)+π(b))=0  for all a≠b.                             (1)

Subtracting π(0) changes no differences, so normalize π(0)=0. This is a necessary condition for every physical classical mate, not a claimed extension of each formal transversal.

- **r=1:** ker J has two cosets and the image is {0,t}. Across different cosets (1) forces `π(a)·t=π(b)·t`; the common relation makes this scalar constant on all eight a, impossible for a permutation.
- **r=2:** ker J={0,k}; let B be the nonzero annihilator of im J. Applying (1) to `(a,a+h)` and `(a+k,a+h)` for all h outside the kernel forces `π(a)+π(a+k)=B` for every a. The linear component q_k has character label b_k; because q_u(Ju)=q_{u+k}(J(u+k))=1, b_k annihilates im J and equals B. Thus W(k,B)=8, contradicting (1).
- **r=3:** J is invertible. Equation (1) with b=0 gives π(a)·J(a)=0; expansion for a,b gives π(a)·J(b)=π(b)·J(a). Applying this twice and using surjectivity of J makes π additive, hence invertible linear. The pairing `(a,b)↦π(a)·J(b)` is then a nondegenerate alternating form on an odd-dimensional space, impossible. A three-dimensional alternating form has a nonzero radical by choosing a paired u,v and adjusting a third basis vector to be perpendicular to both.

Thus no nonadditive character square has a classical ordinary QLS mate; no assumption is made that the arbitrary mate has character form.

## 3. Actual arbitrary mates at polar rank 2 or 3

Assume a four-family contains the selected character square. Independently map each member's first row to the same **labelled coordinate basis** using its own output unitary. In a cell (i,j) with i≠0, every member's j-coordinate is zero by its column ONB. For any remaining coordinate k, pair-product orthogonality between `(i,j)` and `(0,k)` makes the four members' supports pairwise disjoint.

The selected member has 8−2^{3−r} nonlinear rows: six for r=2 and seven for r=3. Its entry in each such row has support exactly four in the first-row basis by §2. Only three of the seven allowed coordinates remain for the three other nonzero mate vectors, so each mate has support exactly one in every such cell. Including the first row, each mate has at least seven entire coordinate-ray rows. If one row remains, each column already contains seven distinct orthogonal coordinate rays and its last unit vector must be the missing ray. All three mates are therefore classical. This contradicts §2's no-classical-mate conclusion for a nonlinear selected member.

## 4. Rank-one arbitrary-mate K₄,₄ argument

At r=1, write F(x)=Lx+kq(x), where L is additive, k≠0 and q has nonzero scalar alternating polar. Four selected-square rows use the same Fourier basis E; the other four use the basis F′=diag((−1)^q)E. Each of their 16 rays occurs four times. The direct zero-plane computation for q, without assuming q balanced, says each E/F′ cross overlap is 0 or has magnitude 1/2; its nonzero graph is exactly two disjoint K₄,₄ blocks. E and F′ share no ray.

Let B be an **actual** orthogonal mate. The four B vectors at the occurrences of one selected ray are orthonormal; their span has dimension four. Within a K₄,₄ block every selected E-ray overlaps every selected F′-ray, so the corresponding four-dimensional B-spans are orthogonal. In C⁸ all four E-spans of a block therefore coincide and the four F′-spans are their common orthogonal complement. In any E-type row the B entries form an ONB with four vectors from each of the two E-blocks, so those block subspaces are complements. The same conclusion holds independently for another actual mate C.

Every selected-square row has four cells in each block; exactly 32 cells have the same row-type/block parity. At all those cells, the B⊗C product lies in one fixed 4×4=16-dimensional tensor subspace. Thirty-two nonzero pairwise-orthogonal product vectors cannot fit there, contradicting B–C ordinary orthogonality. Thus rank 1 excludes two mutually orthogonal mates already; ranks 2/3 exclude the three mates in an actual four-family. All mixed cases are covered.

## 5. Two independent exact local corroborations

A new reviewer C++ program, importing no author code, evaluated all 5,040 normalized F and all 5,040 normalized π per F using direct Walsh-zero masks. Exact observed counts by polar rank 0/1/2/3 were

    F:       [168,1176,2352,1344]
    tested:  [846720,5927040,11854080,6773760]
    passing: [8064,0,0,0].

The per-F passing minimum and maximum are both `[48,0,0,0]`. For every one of the 1,176 rank-one F, it also checked the exact 16 rays/multiplicity four/two K₄,₄ cross graph and **1,024** actual row/column Gram entries, totaling **1,204,224**. Rank-zero and nonpermutation controls were rejected.

A separately written reviewer Python program computed Walsh sums directly for every F, verified every nonlinear zero plane and linear row, and counted all normalized transversals by recursive permutation search rather than the C++ flat loop. It reproduced every rank, tested/pass and per-F count; it also reconstructed every rank-one ray graph and all 1,204,224 row/column Gram entries. Its rank-zero and nonpermutation controls failed for the intended reasons. These checks exhaust the finite **character/transversal** class only; they do not enumerate arbitrary complex mates or replace §§3–4.

| Reviewer artifact (OWN root) | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-review-f41-transversal.cpp` | `93f2353bdde11ce5bd85f2630975759985d8187a012088aea463b6fa0161d860` | 217 |
| Compiled `frontier-20261028-review-f41-transversal` | `42ae07e6afa1195f77bd640717cb21c37f954caeb9616c7d33894791d1a75f96` | — |
| `frontier-20261028-review-f41-transversal-result.json` | `eab5d6a41202a569e2626a22a3e4a43c5e3c621a5c240f65e980d5c332fe1cf1` | 13 |
| `frontier-20261028-review-f41-walsh-planes.py` | `50e8e0f9b6dcca2c5646edb6ecd1eb3435adb53142112b28ba5c957d655d4605` | 179 |
| `frontier-20261028-review-f41-walsh-planes-result.json` | `1465f26198f3d84613566edbf62cbe8c9c5d88912e83d9e22b12ed858843177d` | 41 |

C++ compiled/run with `/usr/bin/clang++ -std=c++17 -O3 -Wall -Wextra` and reported 0.0303177 s; Python ran with `/opt/homebrew/bin/python3 -B` and completed in 1.57 s. The first C++ compile encountered a missing closing parenthesis; it was corrected, then the successful compile/run above produced the pinned result. Both implementations were written locally without importing author code. The candidate's author-source/binary/receipt hashes were checked, and its two receipt summaries compared after the independent work; those receipts are not the independent evidence.

## 6. Assurance and provenance

The registered original problem covers all ordinary complex four-families, including mixtures of classical and nonclassical members; this review pays only the stated character-member obstruction. It does not assert a universal ordinary-four-family result or any numerical M(8) value. The reviewer previously performed a status-only MOQLS-related documentary audit and reported uncertainty about historical held-target exposure. The latest owner direction authorizes this scientific reconstruction, but no blind/clean-cognition or prior-process-success claim follows. No historical quarantined mathematical result was assumed. No current literature-wide novelty, formal/kernel, independent-model or human verification was performed. **END.**
