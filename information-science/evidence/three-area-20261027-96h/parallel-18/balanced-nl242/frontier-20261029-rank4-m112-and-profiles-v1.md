# info-6 frontier: rank four — m=112 is impossible, two profiles fall to an odd mod-3 identity, and E≥2 is forced

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-29T06:16:43-0700**. **UNREVIEWED AUTHOR CANDIDATE.** The proofs are written. They use the pinned finite facts below; no SAT or SMT verdict is used. This is a partial rank-four reduction, not an exclusion of rank four, not a witness, and not reviewed, formal or novelty-cleared.

## Setting and inputs

The notation follows `frontier-20261029-rank4-E0-structure-v1.md` (S₄): f is balanced with T≠0, max|W_f|≤28 and rank(B)=4. The inputs are:

* the author-only collective candidate C, which gives z=96 and `m=116+S+D/2`;
* the author-only rank-four profile list P1, which gives `(D,m)` in {(8,104), (8,110), (10,108), (12,106), (12,112), (14,110), (16,108), (18,112), (20,110), (24,112)};
* the parent-adopted caller congruence and the f131 disposition;
* S₄ Lemmas 2–5 and Corollaries 1 and 6.

The quantity S is `Σ_{y∈Y}σ(y)v′(y)`, where Y is the 16-point Walsh support of the odd quadratic character `g=(−1)^Q`. Since Q has polar B, Y is one block, say λ. The odd inverse v′ takes values in {−1,0,1} and vanishes exactly on the even support.

Without P2: Z is a positive multiple of 4 (S₄ §1), and Z=4 forces rank six (f131), so **Z≥8 at rank four**.

## A. m=112 is impossible

By S₄ Corollary 1, m=112 gives E=0 and Z=8. By S₄ Corollary 6 the configuration `(β,N₆,N₈)` is (6,0,0), (0,2,0) or (2,0,1). For a quadric fibre t, let `o_t`, `w_t` and `f_t` count the entries |y_t|=1, 2 and 4 (S₄ Lemma 5). The checker confirms the needed row geometry over all 3¹⁶ ternary preimages:

* (G1) four ±1 entries always lie on an affine 2-flat;
* (G2) in shape (8,2,0) the ±1 entries form an affine 3-flat;
* (G3) a ±4 entry is the only nonzero entry of its row.

* **(6,0,0).** The four type-10 blocks share one edge set, so they share one Z₀ 4-set F. Then `o_t=4` on F and `o_t=0` off F. The allowed shapes give `w_t≤2` on F and `w_t≤4` off F, so `Σw_t≤16`. But the six type-12 blocks give `Σw_t=18`.
* **(2,0,1).** By (G3), both rows of the type-8 pair {t,t′} contain nothing else. So every type-10 block has pair {t,t′}, and all eight share one edge set. Its four edges would then be covered 8 times, not 4.
* **(0,2,0).** Every row has exactly the two ±2 entries of the type-6 blocks, so `o_t∈{0,4,8}`. Take two rows with `o_t=8`. By (G2) both ±1 sets are affine 3-flats inside the ten type-10 positions, so they share at least 6 points. Distinct affine 3-flats of F₂⁴ share at most 4, so the two sets are equal. Hence each type-10 pair contains both t and t′ or neither. Three such rows would force every pair to avoid all three, giving `o_t=10`. So at most two rows have `o_t=8`, and `Σo_t≤2·8+4·4=32<40=4α`.

**Theorem A.** Rank four with m=112 is impossible. With P1 this removes the profiles (12,112), (18,112) and (24,112). ∎

## B. E=0 at m=110 and m=108

By S₄ (2), E=0 gives `Z=56−8(β+3N₆+4N₈)`.

* **m=110 (Z=16).** The sum is 5, so the configuration is (5,0,0), (2,1,0) or (1,0,1). There is no β=5 covering. For (1,0,1), the argument of A gives nine copies of one edge set. For (2,1,0), none of the 180 covering and triple choices gives six rows of allowed shape (checker).
* **m=108 (Z=24).** The sum is 4, so the configuration is (4,0,0), (1,1,0) or (0,0,1). Configuration (1,1,0) is shape-infeasible in all 20 cases. For (0,0,1), the A argument gives ten copies of one edge set. Configuration (4,0,0) passes the row-shape test in 30 of 240 cases.

**Theorem B.** At rank four, E=0 excludes m=110. At m=108 it leaves only configuration (4,0,0): six type-10, four type-12 and six zero blocks. ∎

## C. The odd half modulo three

Use C's notation: `k=k₀−8δ`, `k₀=g(12h−7)`, with δ∈{−1,0,1} supported exactly on the D odd frequencies with |k|∈{1,3}. Then `k≡−g+δ (mod 3)`. Fourier inversion gives `v′=Walsh(k)/128`. At rank four, `Walsh(g)=64σ·1_Y`. Since 128≡2 and 64≡1 (mod 3),

    v′ ≡ σ·1_Y − Walsh(δ)   (mod 3).                                (C)

Outside Y, v′ is therefore the mod-3 lift of a sum of D signed characters. For each local frequency s put `δ_s=δ(·,s)` and `b_s(c)=Σ_rδ(r,s)(−1)^{r·c}`. Then the odd local transform satisfies `V_s(c)≡−b_s(c)` for every block c≠λ.

**C1 (block Y).** Put `ψ=σv′` on Y. Then (C) gives `Σ_s b_s(λ)χ_s ≡ σ(1−ψ)` on Y, and `σ|_Y=±(−1)^{Q₄(z+μ)}` is bent. Let N be the number of s with `b_s(λ)≢0`. Each such s needs `δ_s≠0`, so D≥N. Write p and z₀ for the numbers of points with ψ=1 and ψ=0; then `S=p−(16−p−z₀)`.

* If S=−16, then ψ≡−1 and `σ(1−ψ)≡−σ`. A bent function has all 16 Walsh values ±4≢0, so N=16 and **D≥16**.
* If S=−13, then (p,z₀) is (0,3) or (1,1). Exhaustion gives N≥10 and N≥12 respectively, so **D≥10**.

P1 has S=−16 at (8,104) and (12,106), with D=8 and 12. **Both profiles are impossible.**

**C2 (one atom per fibre).** If every nonzero δ_s has exactly one atom, then `b_s(c)=±(−1)^{r_s·c}≠0` for every block. Mod 3, Parseval for the odd part of block c≠λ gives

    #{s: V_s(c)≢0} ≡ 16(16−n_c) ≡ 1−n_c   (mod 3).

This applies to (16,108), where S=−16 and D=16 force one atom in every fibre, and to (10,108), where S=−13, D=10, (p,z₀)=(0,3) force one atom in each of exactly ten fibres. The left side is 16 or 10 respectively, both ≡1. So **n_c≡0 (mod 3) for every block c≠λ**.

**C3 (E=0 dies).**

* At (16,108), E=0 requires configuration (4,0,0) with six type-10 blocks, and 10≢0 (mod 3).
* At (10,108), Y has `n_Y=z₀=3`, which is not a C₀ weight.
* m=110 has no E=0 case by Theorem B.

## Status after A–C

Of the ten rank-four profiles, five survive, and each needs E≥2:

| profile (D,m) | S | E range | forced structure |
|---|---:|---|---|
| (16,108) | −16 | 2,4,6,8 (Z=24−2E) | one δ-atom per fibre; n_Y=0; n_c≡0 (mod 3) |
| (10,108) | −13 | 2,4,6,8 | one atom in each of ten fibres; n_Y=3; n_c≡0 (mod 3) |
| (20,110) | −16 | 2,4 (Z=16−2E) | every fibre has an atom; n_Y=0 |
| (14,110) | −13 | 2,4 | N∈{10,12,13} |
| (8,110) | −10 | 2,4 | — |

Remark (not used). At (16,108), (C) determines v′ completely from the atom positions r: F₂⁴→F₂⁴. For c≠λ the odd block is `−lift(θ·Walsh((−1)^{Q₄+r·(c+λ)})(·+μ) mod 3)`, and on Y it is −σ. The even support outside Y is the zero set of these Walsh values mod 3. A search over r is a possible next step; none has been run.

Rank four is still open in these five profiles. Ranks six and eight, the original witness-or-unrestricted-exclusion question and the (24,24,2) gap all remain open. Every step depends on the unreviewed C, P1 and S₄ and needs disjoint review.

| File | SHA-256 | LF | role |
|---|---|---:|---|
| `frontier-20261029-rank4-m112-check.py` | `afb8d355000f326f6fe17589e434753c7cb1cf41136c3fc578aee04df5a2b300` | 141 | G1–G3, configuration row feasibility, C1 table |
| `frontier-20261029-rank4-m112-check-result.json` | `9877df2b0f5fe062d0752a0269045a7638e05ff0b6dee6e7b93e101f37cb47b3` | 230 | receipt |
| `frontier-20261029-rank4-E0-structure-v1.md` | `25b054cdf6eae80fc02771d65206b8c4ea0d89d3ad7442d7af6c4ad4be139797` | 81 | S₄, unreviewed |
| `frontier-20261028-collective-polar-exclusion-v1.md` | `e562e6074dec7beb4a713eed24c3044d6115965de0c60b5c9faf7827da86426d` | 108 | C, unreviewed |
| `frontier-20261028-lowrank-valid-profile-v1.md` | `910d3b68e5e25d13b10b7843b5716edffbdbe82203c01f70b2351bb4faa8ceac` | 63 | P1, unreviewed |

**END.**
