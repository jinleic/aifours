# f52 — independent review of the all-pairs two-level AME barrier

Reviewer **MathSemigroup-2**, math-4; author **PhysicsAME46-2**, physics-6. Assignment SHA `e2dd01f7f8dce2fd65fcec1c564890d750010fa7ddee5006855fe75e60107740`. Native prewrite observation: **Wed Oct 28 17:46:03 PDT 2026**.

## 1. Exact verdict and limits

**NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE — 0 FATAL / 0 MAJOR / 0 MINOR.**

For the **specific** published 60-term Pandya AME(4,6) tensor, each of the four parties may independently choose ANY of its15 coordinate pairs, apply ANY complex invertible 2×2 block on that pair, and apply ANY invertible monomial map on the other four levels. The resulting support is at least60. Identity attains60. The conclusion also applies to physical unitary instances and to added input/output local monomials as proved below.

This is an exact **one-two-level-block-per-party restricted orbit** theorem, not a bound for every AME tensor, arbitrary U(6)^4, multiple noncommuting blocks on a party, or the global minimum. It uses an independently executed finite 50,625-choice/block census plus the universal written CP-rank arguments in §§3–5. It is same-harness computer-assisted written support, not formal/kernel, human/independent-model or novelty acceptance.

## 2. Actual source and independent complete census

In the prescribed order I read the entire79LF candidate `frontier-20261028-four-party-arbitrary-two-level-barrier-v1.md`, SHA `2b32df2e5c4a33fd9e966bcdd3d280eae84a3820e077bbba27c8ece6b4a604e8`, and the entire38LF source table `frontier-20261028-pandya-table-v1.txt`, SHA `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38`. Both hashes matched. The table is [Pandya arXiv:2610.16673v1, Table 1](https://arxiv.org/html/2610.16673v1#S2.T1), previously read and independently transcribed/compared in my f21 review `frontier-review-f21-ame-three-party-support-v1.md`, SHA `33597eeaf6c291955cf8a07a1c28871cf666227fa7651f7d0693664140a6cfd7`. That earlier review also directly checked the **same tensor's six** exact two-party marginals; its source/table facts are known prior familiarity, not a blind re-discovery. The earlier three-party bound is not a premise of the present block argument.

The new standalone program `frontier-review-f52-independent-block-census-v1.py`, SHA `9cee2194ee83c6a784dad75da550a8e854374de76c96a8c654fa0d7e3469d8d7`, imports only my own pinned strict source parser `frontier-review-f35-independent-sector-check-v1.py` SHA `aa7105b8e868ba9a53507ba77f4fa93853423f1454634960db9ce8061fda6066`. It does **not** import any author code, census, engine or receipt. It builds every block from the original60 indexed coefficients, independently checks the Hamming condition, classifies supports, and computes its own modular flattening ranks. The shared source table and same reviewer parser mean this is separately implemented same-harness evidence, not a third-family/blind or formal verifier.

Actual bounded command, **Wed Oct 28 17:45:38 PDT 2026**, timeout180s, exit0 in4.65s:

```text
/opt/homebrew/bin/python3 -B mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding/frontier-review-f52-independent-block-census-v1.py physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-pandya-table-v1.txt

pair_choices=50625 nonempty_blocks=2993046 certified_support_sum_each=60
block (0, 1, 'singleton') count= 600000
block (1, 1, 'singleton') count= 1200000
block (2, 1, 'singleton') count= 871200
block (2, 2, 'two_separated') count= 14400
block (3, 1, 'singleton') count= 255840
block (3, 2, 'two_separated') count= 21600
block (3, 3, 'W') count= 320
block (4, 1, 'singleton') count= 22488
block (4, 2, 'two_separated') count= 6642
block (4, 3, 'W_constant_leg') count= 160
block (4, 3, 'modular3') count= 336
block (4, 4, 'modular4') count= 60
PASS every block rank lower certificate equals exact source term count
CONTROL added Hamming-one source coefficient rejected at collision predicate
```

The input support itself was checked for every unordered pair; the targeted mutation adds a new coordinate at Hamming distance one and is rejected by that exact collision predicate. This is not a full mutation suite. The 320 three-active and160 constant-leg W cases use the written rank lemma below, not a claim that the code computed CP rank directly. All other indicated nontrivial4-leg lower certificates are exact modular matrix-rank checks. No floating-point threshold, angle grid or author-generated certificate is used.

Prior contacts include w20/w58/f21/f35 AME reviews and QOA source-only work, disclosed as same-harness familiarity, not a clean-cognition or independent-family certificate. Current prospective owner direction permits bounded scientific verification; historical quarantined outcomes are not accepted as premises. No author contact, external model, publication, deletion, Git push or infrastructure mutation occurred.

## 3. Invariant blocks and the same transformation

Fix any one of the15^4 choices of local coordinate pairs. At party i decompose its six-dimensional space into the chosen 2-dimensional coordinate subspace and the four remaining **one-dimensional** coordinate subspaces. Tensor products of these summands give a disjoint coordinate-block decomposition. A local matrix with an arbitrary invertible block on its chosen pair and a monomial complement maps each such block invertibly onto another block. The complement permutations are bijections, so different blocks remain disjoint; diagonal phases never create zeros. Equivalently strip a harmless output monomial to fix the labels. No selected block is treated as if its local maps were independently chosen in the actual transformed tensor.

Let t(B) be the number of the ORIGINAL source coefficients in block B and r(B) its ordinary complex CP/tensor rank. The t(B) source coordinates express B as t(B) elementary product tensors, so `r(B)<=t(B)`. Invertible local maps preserve tensor rank. Any transformed block with u nonzero coefficients is a sum of u elementary product tensors in the fixed product basis, so `u>=r(B)`.

The finite census independently establishes `r(B)>=t(B)` for EVERY nonempty block and EVERY choice by the case-specific certificates reconstructed next. Hence r(B)=t(B), and the actual SAME four-party transformation has

`support(after) = Σ_blocks support(after block) >= Σ_blocks t(B)=60`.

Zero blocks stay zero under invertible maps within their summands. Shared transformations cannot weaken a lower bound valid for every local invertible map on each block. Identity attains the bound because the source itself has exactly60 nonzeros.

Output monomials always preserve support. An input monomial M may be moved to the output side as `V M = M(M^{-1} V M)`: its conjugation relabels the active pair and preserves the class of an arbitrary 2×2 block plus monomial complement. Thus independently selected input/output local monomials do not escape the theorem. No conclusion follows for a composition that genuinely has multiple noncommuting 2×2 blocks on a party.

## 4. Exact rank certificates for 1, 2 and 3 terms

The independent program verifies that no two of the60 source coordinates differ in exactly one party. This property passes to every block. One nonzero product-basis coefficient gives rank1.

For two terms, Hamming distance is at least2, and all their differing coordinates lie among that block's active axes (singleton axes are fixed). Flatten by separating one differing axis from the remaining axes; the two nonzero coefficients lie in different matrix rows and different columns. The resulting 2×2 diagonal submatrix has nonzero determinant, so flattening rank and CP rank are at least2. The two source terms give rank at most2. This is exact over C and works for all phases/nonzero coefficients.

For a three-term 2×2×2 block with no Hamming-one pair, the three occupied binary vertices all have the same parity. Indeed opposite-parity nonadjacent vertices must be antipodal; every third cube vertex is distance1 from one of the two. Translate bit labels and permute axes to place the three nonzero coefficients at `000,011,101`, with nonzero complex coefficients a,b,c. Slicing the first axis gives

`M_0=[[a,0],[0,b]]`, `M_1=[[0,c],[0,0]]`,
`det(x M_0+y M_1)=ab x²`.

Every one-axis flattening has rank2: both local values occur, and their nonzero complementary supports are disjoint. If the tensor were a sum of two product tensors, the two local vectors in EACH mode would therefore be independent. Its matrix pencil would factor as `V diag(ℓ_1(x,y),ℓ_2(x,y)) W^T` with invertible V,W and **independent** linear forms ℓ_1,ℓ_2. Its determinant would be a nonzero scalar times two distinct linear factors, contradicting the repeated factor `ab x²` over C. Hence rank>=3; the three source terms give rank<=3.

If a block has four nominal active axes but one axis is constant on all three terms, it is a nonzero single vector on that leg tensored with the above three-way tensor. Tensor rank is unchanged: extending any three-way decomposition gives one inequality, and applying a linear functional taking that nonzero fourth vector to1 gives the other. This pays all160 constant-leg cases. The proof is about **exact** tensor rank, not the border rank of the W tensor or an approximation threshold.

## 5. Exact modular lower bounds on the remaining blocks

The unnormalized source coefficients lie in Z[√2]. The map `a+b√2↦a+6b mod17` is a ring homomorphism because 6²=36≡2 mod17. Therefore a determinant nonzero in F_17 cannot have been zero as an exact Z[√2] expression, and the corresponding complex matrix minor is nonzero. A matrix flattening rank is always a lower bound for complex CP rank.

For every four-active 3-term block with no constant leg, the independent census forms all three distinct2|2 flattenings and finds at least one with modular rank3. For every four-active 4-term block it finds a modular rank4 flattening. Since the source is already an exact three- or four-product-term decomposition, those lower bounds are equal to the true complex tensor ranks. This uses the same tensor coefficients in each block, including signs and √2 values; no choice of independent marginals or real-coefficient restriction is introduced.

The complete independent census yields exactly336 modular3 and60 modular4 blocks over **all** pair selections, matching the candidate. It also explicitly verifies that there is no unhandled block with more than4 terms, that every classified block's lower certificate equals its term count, and that the60 term counts are recovered in every one of the50,625 choices. The W and two-term cases are paid by §4, not by a modular rank that might be only2.

## 6. Scope and remaining gates

The original source is an actual normalized AME(4,6) tensor: all six marginals were checked independently in f21 on the same signed/sqrt2 table. Applying local **unitaries** gives another actual AME state; using invertible but nonunitary maps in the proof only strengthens a mathematical support statement for this fixed tensor.

No new FATAL/MAJOR/MINOR defect was found in the invariant-block argument, W-rank lemma including constant legs, modular specialization, full pair/block coverage or finite/computational-to-universal inference. The published 38 lower-bound input and global latest status were not reviewed. No result for arbitrary U(6)^4, an arbitrary AME state, a sub-60 witness or the full minimum follows.

This is same-harness scientific review with one independently implemented exact census and prior disclosed familiarity; it is not a formal/kernel/human/independent-model or novelty/priority clearance. Main must read the complete author candidate, actual return and evidence before any adoption.
