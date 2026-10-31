# d=4 certificate global-aggregation source walkthrough

This is a written source-code and mathematical reconstruction of the pinned Tomar v3 `ep3core.py`, SHA256 `0f0d84a9ce257edbf9b0b6cbbff2690041fbd6aad18d139c8845e8edf547d450`, in archive SHA256 `2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3`. It is **not a separately executed exact global-identity checker**, nor a Lean/human/configured-family proof or theorem adoption. Initial actual finite map checks and their hashes are in `frontier-20261028-d4-source-data-audit-v1.md`, SHA256 `1240320c5357e34d75c1206056aa072b3758e461c948398fe4e6264b1b1aa566`. The separate exact correction/replay was still running when this note was authored; no result from it is assumed here.

## 1. Original caller and coefficient convention

For arbitrary complex `U,V:C²→(C⁴)^tensor3`, put C=UV†. For each physical subset S, exact index contraction gives

`||Tr_S C||HS² = <vec U ⊗ vec V, F_Q F_S(vec U ⊗ vec V)>`.

Here Q is the shared two-dimensional column index, F_S swaps exactly the physical sites in S, and all traces in the left side are UNNORMALIZED. This holds for arbitrary U,V, not only orthonormal columns. The independent integer coefficient checker `frontier-20261028-d4-original-swap-coefficients-check.py`, SHA256 `fc70405ca23ebb76ca08d4539ff0251db4760a4614b0a3367995cb7c0086b5f6`, compared both formulas on every formal monomial of all eight subsets; result SHA256 `ea9eff59833ccdd487a1ca4ace3b56f05c54a2b7711e1d09b7e8b5bfa130bf99` reports131072 direct term occurrences, zero mismatches. The combination weights after multiplying q3 by8 are exactly 8,−4,+2,−1 by subset size. This is an exact machine check of a finite symbolic identity, not positivity evidence.

For nonzero C normalize ||C||HS²=1/2. A range isometry A and B=2C†A produce normalized physical vectors a,b with C_xy=Σ_r a_xr conjugate(b_yr) and ancilla marginal of a equal I/2; conversely every such pair gives an original normalized rank<=2 C. The source's objective is the swap expectation and its twirled moment normalization `L=(2*4³)^4`; the objective denominator `2³L=2^31` includes all three 1/2 factors. The all-331776-word independent objective check reported zero mismatches against this normalization. Rank0 is treated separately and rank1 has an isometric completion.

## 2. Exact block-contribution index reconstruction

For one source family and one common row-pair pattern `(r,s)`, write the 4 local compressed maps as `A_l[p_l,(i_l,j_l)]`, with l=1,2,3,Q. Here p_l ranges over S4, and local pairs index an actual fixed compression J_l. The previously run site/auxiliary checkers computed these maps by explicit basis-index contraction for **every** module/row-pair/permutation actually used by the d4 data.

For each type t sharing the pattern and module tuple, let W_t be its integral congruence/compression, partitioned by Gram row into matrices `W_(t,r)` and `W_(t,s)` with a common product-space index i=(i1,i2,i3,iQ). Let Z_t be its rational multiplier and choose a common positive denominator D. Define

`B_(i,j)=Σ_t Σ_(a,b) W_(t,r)[i,a]*(D Z_t)[a,b]*W_(t,s)[j,b]`.

Then the integer contribution of this grouped row pair to one word `(p1,p2,p3,pQ)` is exactly

`Σ_(i,j) B_(i,j) ∏_l A_l[p_l,(i_l,j_l)]`,

and dividing by D gives its certificate contribution. This is the entrywise expansion of `Tr(Z_t K_t† M_t K_t)`; symmetry of Z handles the equivalent transposition of scalar Gram indices.

In `Relaxation.contributions`, source `ep3core.py:438–496`, the code obtains `Bsum=Wr*Zint*Ws.transpose()` in exact FLINT integer arithmetic, reshapes its row/column product indices as `dims+dims`, and transposes them into `(i1,j1,i2,j2,i3,j3,iQ,jQ)`. Offsets insert the terms for different fixed modules into the appropriate disjoint per-axis concatenated coordinate blocks. Each `mode_product` applies the corresponding local map A_l on that axis. Thus, as an index identity, its output tensor is exactly the displayed word-contribution formula. No assumption that site modules are orthogonal, complete, linearly independent or invertible enters; each is an actual compression.

This is a source-level derivation, with runtime semantics of exact FLINT matrices and numpy reshape/transposes as imports. It has not been independently reimplemented as a second full 4675-row exact global aggregator.

## 3. Equality and objective terms

In `Relaxation.residual` (`ep3core.py:545–579`), each equality group provides a sparse tensor `Lt` of rational lambda coefficients, cleared by a group denominator. Every signed part supplies four local matrices `E_l` and the code applies them one axis at a time. Its resulting coefficient for a word is

`Σ_o lambda[o] ∏_l E_l[o_l,p_l]`

with the prescribed part sign. The actual d4 five canonical group names, a-replica slots, family signs, common-marginal reordering and all used local equality compressed maps were independently compared with explicit partial traces. No equality is justified merely by the name attached to a data field.

The objective tensor is added only to family31. Its literal numerator and exact denominator were checked on every word by the independent objective script. Thus the computed residual is the objective minus every block contribution and equality term, provided the code's tensor operations and exact arithmetic implement the source as inspected.

## 4. Orbit sums, exact arithmetic and correction role

The source space consists of real orbit sums of permutation words under simultaneous left/right family stabilizers, site permutations and inversion. `add_orbit_sums` groups every word coefficient by its computed orbit label and adds them as exact integers or `Fraction`s. Independent union-find rebuilt **the entire partition**, not just its count, and checked both directions against the author labels: 1142,2391,1142 components.

Therefore a **correctly computed exact zero** residual on all4675 source-orbit sums makes the functional zero on their real span. The source's Schur–Weyl/physical twirl lemma puts all actual moments in that span; it need not make orbit-sums linearly independent. In combination with PSD multipliers and valid equalities, the conditional certificate implication then follows.

In the author per-d program, the first 2634-row/column rational solve constructs a correction; the final `rx.residual` computation and every corrected PSD test are decisive, not the correction algorithm by itself. The modular CRT column computation uses primes below 2^26; `mode_product_mod` asserts each summed axis has length<=16 and the code bounds integer products/sums within int64. The terminal exact residual calculation uses object/FLINT integer and rational arithmetic rather than relying on the CRT result's claimed correctness. No actual terminal result is stated in this note.

## 5. Precisely what remains

The block/equality/objective assembly above has been reconstructed from source, and its local inputs and source partition have been independently exercised exhaustively for this fixed d4 package. This is significantly stronger than a bare source-file hash, but the inspection still trusts Python/numpy/FLINT arithmetic and does not itself compute the corrected rational identity. The separate bounded author-code replay may independently establish a run of that identity; its final PSD capture uses a different rational Schur algorithm. Until actual outputs arrive, corrected PSD and exact residual remain pending. Even a successful replay is not automatically a second independently implemented global aggregator, formal Lean verification, external-human review or accepted original theorem.

No source method is counted as new discovery, and no previously quarantined output is accepted as a premise. The original unrestricted d4 rank<=2 q3 inequality remains the target throughout.
