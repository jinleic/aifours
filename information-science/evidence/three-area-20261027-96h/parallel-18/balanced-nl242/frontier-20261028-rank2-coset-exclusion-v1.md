# info-6 frontier: rank two is impossible (conditional coset proof)

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-29T04:17:31-0700**. **UNREVIEWED AUTHOR CANDIDATE.** The proof below is written and elementary. It uses the parent-adopted Walsh caller/mod-4 disposition and three **author-only** inputs, named below. A pinned finite checker confirms the small tables and runs Z3 cross-checks. Those cross-checks are not the proof. This is a branch exclusion only: there is no witness, no unrestricted no-go, no novelty claim, no disjoint review and no formal verification.

## Statement

Let f:F₂⁹→F₂ be balanced. Assume `T=⊕{x:f(x)=1}≠0` and `max|W_f|≤28`. Let q be the even-half quadratic `k/2 mod 2` on T⊥, where `k=W_f/4`. Let B be the polar of q. Assume:

* **(P1)** The author-only low-rank profile `frontier-20261028-lowrank-valid-profile-v1.md`, which uses the collective and sparse-sign predecessors. If rank(B)=2, it gives two facts. First, q has exactly 64 zeros. Second, `(D,m)` is one of `(12,118),(16,120),(20,122)`. Here `D=n₁+n₃` counts odd-half `|k|∈{1,3}`, and m counts agreeing unordered T-pairs.
* **(P2)** The author-only singular-cubic minimum-support bound. It gives Z≥8, where Z is the number of Walsh zeros.

Then **rank(B)≠2**.

The author-only collective-polar candidate already excludes rank 0. Hence, conditionally, the even polar rank is 4, 6 or 8. Ranks 4, 6 and 8 and the unrestricted question remain open.

## 1. The even half as 64 four-point blocks

Put T last and set `u(y)=((-1)^{f(y,0)}+(-1)^{f(y,1)})/2`. Then u is ternary on F₂⁸ with support m, Σu=0, and `Ŵ:=Walsh(u)=2k` on T⊥.

Rank two with 64 zeros forces the following. q vanishes on its 6-dimensional polar radical R; otherwise q would be balanced. q is anisotropic on the quotient. So q=0 exactly on R.

Choose dual coordinates: frequencies `a=(r,s)` and points `y=(c,z)`, with r,c∈F₂⁶, s,z∈F₂², and `R={s=0}`. For each block c, define the four-point transform

    U_s(c)=Σ_z u(c,z)(−1)^{s·z}.

Then `Ŵ(r,s)=Σ_c U_s(c)(−1)^{r·c}`. The peak bound gives the allowed values:

* `Ŵ(r,0)∈{0,±8}`, with exactly Z zeros.
* For s≠0, `Ŵ(r,s)∈{±4,±12}`. Exactly `e_s` of the 64 values in block s have magnitude 4.

Write `E₂=e₁+e₂+e₃`. Parseval gives `256m=64(64−Z)+16E₂+144(192−E₂)`, so

    E₂=248−Z/2−2m.                                               (1)

The parent-adopted congruence `E₂+2n₃≡0 (mod4)` makes E₂ even. By (1), Z≡0 (mod 4).

Define

    v_s=Ŵ(·,s)/4∈{±1,±3},   σ_s=sign v_s,   τ_s=σ_s·1_{|v_s|=1}.

Then `v_s=3σ_s−2τ_s` and `U_s=Walsh₆(v_s)/16`. Hence

    16U_s(c)=3W(σ_s)(c)−2t_s(c),    t_s:=W(τ_s),                   (2)

so `t_s≡U_s (mod 3)`. Parseval also gives:

* `Σ_cU₀²=64−Z`, `Σ_cU_s²=144−2e_s` and `Σ_cU₀=0`.
* `Σ_cW(σ_s)²=4096`, `Σ_ct_s²=64e_s` and `Σ_cW(σ_s)t_s=64e_s`.            (3)

Each block is one of 81 ternary 4-vectors. Let n_c be the number of nonzero entries in block c. The transform satisfies `Σ_sU_s(c)²=4n_c`. The classes are as follows, with j∈{1,2,3}:

| class | n | absolute values of `U₀,U_j,(the other two)` |
|---|---:|---|
| A_j | 3 | 1, 3, (1,1) |
| B | 3 | 3, all 1 |
| C_j | 2 | 2, 2, (0,0) |
| D_j | 2 | 0, 0, (2,2) |
| E | 4 | all 2 |
| F | 1 | all 1 |
| G_j | 4 | 0, 4, (0,0) |
| H | 4 | 4, all 0 |
| O | 0 | all 0 |

Every n=3 vector has exactly one |U|=3 entry.

## 2. Lemmas

**L1 (parity).** Odd squares are 1 mod 4 and even squares are 0 mod 4. Also U_s(c)≡n_c (mod 2) for every s. So each sum in (3) is congruent mod 4 to `#{c:n_c odd}`. Therefore `2e_s≡Z (mod4)` for every s. Since Z≡0 (mod 4), every e_s is even.

**L2 (e_s=0).** If e_s=0 then t_s=0. Then U_s∈{0,±3}, and exactly 16 blocks have |U_s|=3. These are A_s blocks, in which every other |U| equals 1.

**L3 (two zeros).** If `e_s=e_{s'}=0` with s≠s′, then L2 for s puts 16 blocks with `|U_{s'}|=1`. That contradicts `U_{s'}∈{0,±3}`.

**L4 (e_s=2).** In this case `t_s∈{0,±2}`. Congruence with U_s forces t=0 at |U|∈{0,3}, t=∓2 at U=±1 or ±4, and t=±2 at U=±2. The corresponding W(σ) values are 0,16,4,20,12. Let `N_k=#{|U_s|=k}`. Then (3) has exactly the integer solutions

    (N₀,N₁,N₂,N₃,N₄)=(24+2κ,20−2κ,12+κ,8−2κ,κ),    κ=0,…,4.

Moreover τ_s has two signed atoms. So `{t_s=0}={c:U_s(c)∈{0,±3}}` is an **affine hyperplane** `Hyp_s`.

**L5 (zero and two).** If e_s=0 and e_{s'}=2, then L2 gives `N₁^{(s')}≥16`. No block has `|U_{s'}|=3`, so κ=4 and `N₁^{(s')}=12`. Contradiction.

**L6 (e_s=4).** The |t_s| histogram over the values (0,2,4) is one of three patterns:

* (0,64,0).
* (48,0,16).
* (24,32,8). Here τ_s has four affinely independent atoms. Then `{|t|=2}` is the complement of an affine hyperplane Hyp_s, `{t=0}` is `Hyp_s∖F_s`, and F_s⊂Hyp_s is an affine 3-flat.

For |U|=0 and |U|=3, t=0. For |U|=1 or 4, t is −2 or 4; for |U|=2, t is 2 or −4 (signs taken relative to U).

**Flat fact.** Two affine 3-flats in a 5-dimensional affine space meet in 0, 2, 4 or 8 points. This follows by dimension count; the checker also enumerates it.

## 3. Case analysis

By (1), E₂≡Z/2 (mod 2), and L1 makes every e_s even.

* If E₂≤2, some two e_s vanish, so L3 applies. This covers `(D,m,Z)=(20,122,8),(16,120,12),(16,120,16),(12,118,20),(12,118,24)`.
* Profile (16,120,8) has E₂=4. Its patterns (0,0,4) and (0,2,2) fail by L3 and L5.
* Profile (12,118,16) has E₂=4 and fails the same way.
* Profile (12,118,12) has E₂=6. Patterns (0,0,6) and (0,2,4) fail by L3 and L5.
* Profile (12,118,8) has E₂=8. Patterns (0,0,8) and (0,2,6) fail by L3 and L5.

(D,m) fixes Z≤(7936−64m)/16 with Z≥8, so no other cases remain. Three patterns survive the counting lemmas. The pinned Z3 runs confirm that their counting systems alone are satisfiable, so the geometric arguments below carry real content.

**(12,118,12) with (2,2,2).** By L4, all three κ_s are equal to some κ. Then `A_s=8−2κ`, `G_s=κ` and `B+F=4+2κ`. Each class has a fixed pattern of membership in the three hyperplanes Hyp₁, Hyp₂, Hyp₃:

| pattern | classes |
|---|---|
| (1,0,0) | A₁, D₁ |
| (0,1,1) | C₁, G₁ |
| (0,0,0) | B, E, F |
| (1,1,1) | H, O |

The other patterns follow by permuting indices. Now split by the linear normals of the hyperplanes:

* **Independent normals.** Each pattern holds 8 blocks. Then E=4−2κ, C_s=8−κ, D_s=2κ. The U₀ energy equation reduces to `2B+4H=6κ−22<0`. Impossible.
* **Some hyperplanes coincide or are complementary.** Either A_s=0 with G_s≠0 forced into an empty pattern, or `B+F=0` with `B+F=4+2κ`. Impossible.
* **Normals dependent, with ρ₃=ρ₁+ρ₂.** Only the even-weight or only the odd-weight patterns occur, 16 blocks each. The even case forces κ=4 and then 2B+…<0. The odd case forces B+E+F=0. Impossible.

**(12,118,8) with (0,4,4).** By L2 with e₁=0, only the classes {A₁, C₂, C₃, D₁, G₂, G₃, H, O} occur, and A₁=16.

For s=2, the histograms (0,64,0) and (48,0,16) violate `ΣW(σ)²=4096`. In (24,32,8), (3) gives G₂=2 and C₂+D₁=22, and s=3 is symmetric. Energy then gives `C₂=C₃=5−2H`, `D₁=17+2H` and `O=17+H`.

The zero sets of U₂ and U₃ are `Hyp₂∖F₂` and `Hyp₃∖F₃`. Their intersection is exactly H∪O, which has ≥17 blocks. So Hyp₂=Hyp₃. Then `|F₂∩F₃|=16−(32−17−2H)=1+2H`, which is odd. The flat fact makes it even. Contradiction.

**(12,118,8) with (2,2,4).** By L4, κ₁=κ₂=κ. Then `A₁=A₂=8−2κ`, `G₁=G₂=κ` and `A₃+B+F=12`.

If Hyp₁ and Hyp₂ coincide or are complementary, a forced-nonzero class falls in an empty pattern. So they are transversal and cut F₂⁶ into four quadrants of 16 blocks each.

For s=3, the histograms (0,64,0) and (48,0,16) fail the U₃ energy or `ΣWt=256`. In (24,32,8), (3) gives `A₃+G₃+κ=5` together with the other linear counts.

* **ρ₃ in span(ρ₁,ρ₂).** Hyp₃ is a union of two quadrants. Each of the four placements contradicts either nonnegativity or the outside-Hyp₃ count `y−w=24−4G₃−2A₃`. Here y and w count |U₃|=2 and |U₃|=4 blocks with |t₃|=2.
* **ρ₃ not in that span.** Each quadrant meets Hyp₃ in 8 blocks. Counting forces `A₃+B+E+G₃+2H+f₁₁=1`, where f₁₁ counts Q₁₁ blocks in F₃. Hence κ=4 and A₃+G₃=1.
  * (A₃,G₃)=(1,0) needs an F₃ quadrant intersection of size 3. That is impossible.
  * (A₃,G₃)=(0,1) forces y−w=22. The required value is 20.

The z3 cross-check also enumerates all 29 geometric region vectors of this configuration and finds each UNSAT. ∎

## 4. Checks, limits and pins

The checker does the following:

* enumerates the 81 local types and their class table, and checks the n=3 sign identity `U₀U₁U₂U₃=−3`;
* finds every integer solution of the L4 system, which gives exactly the κ=0…4 family;
* recomputes the exact e=2 and e=4 |t| histograms by even-relation-code enumeration;
* enumerates all 620 affine 3-flats of F₂⁵, whose pairwise intersections are 0, 2, 4 or 8;
* tests 400 random general-position four-atom τ's against the L6 geometry;
* records 36 Z3 class-count cross-checks. Every case excluded above is UNSAT. The three geometric cases are SAT without geometry, and all 29 region systems for (2,2,4) are UNSAT.

The proof depends on the unreviewed P1 and P2. If P2 failed, the Z=4 sub-cases (E₂=6 or 10) would need separate treatment; Z3 finds their counting systems satisfiable. Ranks 4, 6 and 8, actual construction and the original witness-or-exclusion gap remain open. Every step needs disjoint review.

| File | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-rank2-coset-exclusion-check.py` | `c8b9b51da0be3a36091f20300094d253cdb99e9932c3d763f98773ef193e60af` | 206 | finite inputs + Z3 cross-checks |
| `frontier-20261028-rank2-coset-exclusion-check-result.json` | `32b5b2b2167379f0cda05ab512fb719d75c7e39e5f5aa078a0c746067c42cec2` | 136 | receipt |
| `frontier-20261028-lowrank-valid-profile-v1.md` | `910d3b68e5e25d13b10b7843b5716edffbdbe82203c01f70b2351bb4faa8ceac` | 63 | P1, unreviewed |
| `frontier-20261028-collective-polar-exclusion-v1.md` | `e562e6074dec7beb4a713eed24c3044d6115965de0c60b5c9faf7827da86426d` | 108 | P1 input, unreviewed |
| `frontier-20261028-rank2-sparse-sign-exclusion-v1.md` | `b16317ae852eb710c7f473b4e2ffcc0d519a9d62af20b37e2a76dc89c6a2143a` | 63 | P1 input, unreviewed |
| `frontier-20261028-singular-cubic-zero-v1.md` | `6fba1086e8beefa0101f28c5c4c4c3243be2fc583d18328f6271ac6695e961fe` | 70 | P2, unreviewed |
| `institute/runs/three-area-2026-10-27-96h/dispositions/info-6-walsh-caller-and-mod4-coupling-parent-v1.md` | `721222262af91bc768227ce8bfae563cabf5a102437ac55e6583de38ec2d3c9d` | 23 | parent-adopted caller |

**END.**
