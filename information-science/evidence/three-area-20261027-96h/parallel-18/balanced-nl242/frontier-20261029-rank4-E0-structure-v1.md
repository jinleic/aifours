# info-6 frontier: rank-four even half — the E=0 block code and an even-half control

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-29T05:34:10-0700**. **UNREVIEWED AUTHOR CANDIDATE.** Written lemmas plus a pinned finite checker and one decoded solver model that was re-verified by a separate direct 256×256 Walsh computation. This is a structure theorem and a control, **not** an exclusion of rank four, not a Boolean witness, and not reviewed, formal or novelty-cleared.

## Setting

Let f:F₂⁹→F₂ be balanced with `T=⊕{x:f(x)=1}≠0` and `max|W_f|≤28`; let q be the even-half quadratic `k/2 mod 2` on T⊥ (`k=W_f/4`) and B its polar. Assume rank(B)=4. The author-only collective candidate (`frontier-20261028-collective-polar-exclusion-v1.md`) gives z=96, i.e. q vanishes on R=rad(B) and is elliptic on T⊥/R. Choose coordinates a=(r,s), r,s∈F₂⁴, with R={s=0} and

    q(r,s)=Q₄(s)=s₁s₂+s₃s₄+s₃+s₄,   Z₀={s:Q₄(s)=0}={0,1,2,7,11,15},   NZ = the other 10.

(Bits: s=s₁+2s₂+4s₃+8s₄.) Points are y=(c,z); the 16 blocks c are the cosets of R⊥. With u the agreeing-pair ternary function (as in the rank-two paper), `Ŵ=Walsh(u)=2k` on T⊥, the local transforms are `U_s(c)=Σ_z u(c,z)(−1)^{s·z}` and `Ŵ(r,s)=Σ_c U_s(c)(−1)^{r·c}`. The peak bound and q give

* `Ŵ(r,s)∈{0,±8}` for s∈Z₀ (Z zeros in total, `Ŵ(0,0)=0`);
* `Ŵ(r,s)∈{±4,±12}` for s∈NZ; `e_s` counts magnitude 4 in fibre s, `E=Σe_s`.

## 1. Energy

Parseval over T⊥ gives `256m=64(96−Z)+Σ_{s∈NZ}(2304−128e_s)`, so

    E=228−Z/2−2m.                                                   (1)

The parent-adopted congruence `E+2n₃≡0 (mod 4)` (E is the even-half count E₂ there) makes E even, so Z≡0 (mod 4).

**Corollary 1.** If m=112 then E=4−Z/2 and Z∈{4,8}. Exactly four zeros force rank six by the parent-adopted f131 disposition. Hence **m=112 ⇒ Z=8 and E=0**. In the author-only rank-four profile list (P1, `frontier-20261028-lowrank-valid-profile-v1.md`) this covers `(D,m)=(12,112),(18,112),(24,112)`.

## 2. The block code when E=0

**Lemma 2 (C₀ reduction).** If e_s=0 for every s∈NZ, then every block `u(c,·)` is the ternary lift of a word of the [16,6]₃ code C₀ spanned by the characters χ_t, t∈Z₀.

*Proof.* For s∈NZ, `Ŵ(·,s)=12σ_s`, so `U_s=(3/4)Walsh(σ_s)`; integrality forces `4|Walsh(σ_s)`, so `U_s≡0 (mod 3)`. Since 16≡1 (mod 3), `u(c,·)≡Σ_s U_s(c)χ_s≡Σ_{t∈Z₀}U_t(c)χ_t (mod 3)`, and a {−1,0,1}-vector is determined by its residues. ∎

The 729 lifted words have exactly eight |U|-profiles (checker):

| type n | count | \|U\| on Z₀ | \|U\| on NZ |
|---:|---:|---|---|
| 0 | 1 | 0 | 0 |
| 6 | 32 | 4 at all six | 0 |
| 8 | 60 | 8 at a pair | 0 |
| 10 | 240 | 2 at a 4-set F | 6 at four points |
| 11 | 192 | 1 at five, 9 at one | 3 at all ten |
| 12 | 160 | 4 at a triple A | 12 at the single point ΣA |
| 15 | 32 | 5 at all six | 3 at all ten |
| 16 | 12 | 16 at one | 0 |

**Lemma 3 (counting).** With E=0, no block has type 11, 15 or 16; exactly ten blocks have type 10 or 12; and, writing β for the type-12 count,

    Z=56−8β−24N₆−32N₈,      m=100+2β+6N₆+8N₈.                    (2)

*Proof.* Each Z₀ fibre has `Σ_cU_t²=4(16−z_t)≤64<256`, excluding type 16. The NZ fibres give `144(N₁₀+N₁₂)+90(N₁₁+N₁₅)=1440`, so `(N₁₀+N₁₂,N₁₁+N₁₅)∈{(10,0),(5,8),(0,16)}`. The Z₀ energy `96N₆+128N₈+16N₁₀+86N₁₁+48N₁₂+150N₁₅=4(96−Z)≤384` kills the last two. Then (2) is the Z₀ energy and the weight count. ∎

**Lemma 4 (NZ dichotomy).** For s∈NZ the column `(U_s(c))_c` either has a single entry ±12 (a type-12 block with ΣA=s) or four entries ±6 (type-10 blocks) located on an **affine 2-flat of block space with sign product −1**.

*Proof.* Energy 144 with entries in {0,±6,±12} leaves only these supports. For four entries put `x(r)=Ŵ(r,s)/6=Σ_{c∈P}ε_cχ_r(c)`; flatness `x=±2` is equivalent to `Σ_r x⁴=256` given `Σ_r x²=64`. The fourth moment is 16 times the signed number of ordered quadruples in P with zero sum: 40 trivial ones, plus 24π when P is an affine 2-flat with sign product π. So P is a flat and π=−1. ∎

In the K₅ model (Z₀∖0 = five vertices, NZ = the ten edges p_i+p_j), a type-10 word's four NZ points are a star at one vertex or one edge plus the opposite triangle (15 edge sets), and a type-12 word with triple A covers the single edge ΣA. By Lemma 4 every edge is covered either once by a type-12 block or exactly four times by type-10 edge sets. The checker finds such coverings only for β∈{0,1,2,4,6,10}, with 27, 10, 45, 15, 15 and 1 solutions; β=10 contradicts Z≥0 in (2).

**Lemma 5 (Z₀ rows).** For t∈Z₀ put `y_t=U_t/2`; then `Walsh(y_t)∈{0,±4}`. Among all such 16-vectors with entries in {0,±1,±2,±4} (enumerated from all 3¹⁶ ternary preimages) the shapes `(#|y|=1,#|y|=2,#|y|=4)` are exactly (0,0,0), (0,0,1), (0,2,0), (0,4,0), (4,0,0), (4,1,0), (4,2,0), (6,0,0), (6,1,0), (8,0,0), (8,1,0), (8,2,0), (10,0,0), (12,0,0), (16,0,0). In particular a type-8 entry ±4 is always alone in its Z₀ fibre.

**Corollary 6 (m=112).** By Corollary 1 and (2), `β+3N₆+4N₈=6`. Since β=3 admits no covering, `(β,N₆,N₈)` is one of `(6,0,0)`, `(0,2,0)` or `(2,0,1)`.

## 3. An even-half control

The pinned file `frontier-20261029-rank4-even-E0-control.json` is a ternary u on F₂⁸ built from ten type-10 blocks and six zero blocks. A separate checker recomputes all 256 Walsh values directly: Σu=0, `Ŵ∈{0,±8}` on every q-zero frequency, `Ŵ=±12` on every q-one frequency, m=100, Z=56, E=0, no violations. So **the rank-four even-half conditions alone are satisfiable**. Any exclusion of rank four must use the odd half, for instance P1's `m≥104`, which this control violates. It is not a Boolean function and says nothing about the odd half.

A first bounded annealing of odd-half signings on this control's 156-point odd support reached only max|Walsh|=22 (allowed 14). That is search output, not an exclusion.

## 4. Status, dependencies and pins

Rank four remains open. The m=112 branch is reduced to E=0 with three block configurations. Searches on those are running and are not reported here. The proof depends on the author-only collective (z=96) and, for Corollaries 1 and 6, on P1's profile list and on the parent-adopted f131 and caller congruence. The original witness-or-unrestricted-exclusion gap and ranks six and eight remain open.

| File | SHA-256 | LF | role |
|---|---|---:|---|
| `frontier-20261029-rank4-E0-structure-check.py` | `640266e6047650f683685e0de27e05ba5958718642d583bd947ef5ea8a7f72fc` | 152 | C₀ table, NZ rows, Z₀ shapes, coverings |
| `frontier-20261029-rank4-E0-structure-check-result.json` | `303e9420aef2631d03b6251cc6e484e02edad7ecf06e47afda646c10ba274320` | 416 | receipt |
| `frontier-20261029-rank4-even-E0-control.json` | `cb716808561da4b543563edb56293c9be9b3e249153a753ce51b6266053ccc26` | — | even-half control (decoded kissat model) |
| `frontier-20261029-rank4-even-check.py` | `7289f528c2ce5e31d552e1ef6e9d368358f535e829d47ddff4feb1412f8d0105` | 29 | direct Walsh checker |
| `frontier-20261029-rank4-even-E0-control-check.json` | `e57218f388b5972a8bb6720d1e416e07695ca1df2b77884ec01e6376a500ce45` | 16 | control receipt |
| `scratch-20261029/rank4E0b.cnf` | `f93efb85660a1345aa906e64acddd7e9f5a29835d077a887d28116d6791f1515` | — | SAT encoding that produced the control |
| `frontier-20261029-odd-sign-anneal.cpp` | `9b805688ee45a3ed07df3a190fe3bf73938539503bf3f37fd0597069fc5c164d` | 57 | bounded odd-half annealer |

**END.**
