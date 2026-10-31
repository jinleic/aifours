# f117 independent same-harness scientific review — |P| = 24 branch (`size24`)

Review wave `f117-shor-1320-final-cardinality-cases`, manifest `manifest-v1.json`
SHA256 `5ba7dfc08c681e28bb9e9d1f2ae6134bbf62f634061eb17c0e131b6d71258346` (3824 B, verified).
Native `/bin/date` immediately before this file was written: **Wed Oct 28 19:54:05 PDT 2026**.
Reviewer: f117 size24 subagent (same harness as the author; NOT a human, independent-model-family,
kernel/formal or novelty review). Authority: contract-addendum-2 frontier-first owner direction.

## 0. Verdict (scientifically scoped)

**Scope reviewed:** only §6 of `frontier-20261028-1320-border-no-go-candidate-v1.md` — the `|P| = 24`
cardinality branch of the conditional order-1320 border no-go candidate — together with the two author
size24 programs read as text. Nothing about `|P| = 44`, the f114 two-size reduction, the combined
candidate theorem, or any all-order statement is accepted or asserted here.

**Premises assumed, not established here:**
- **(T)** actual border tiling: `P ⊕ Q = Z_1320` is a direct tiling with `A = {0,3,8,11} ⊆ P`,
  `Y = {0,1,7,13,14} ⊆ Q`, and `|P| = 24` is one of the two remaining cardinalities. This is the
  f114 chain (border theorem reconstruction, divisor packing, four/three/two-size reductions), which is
  **separately under review and NOT accepted**.
- **(S)** Sands' divisor-class theorem, necessary direction: no nonzero difference of `P` and nonzero
  difference of `Q` share a gcd with 1320. Used by the author as "independently derived" in the f114
  divisor-class predecessor, which I did not review. I ran only a finite small-`n` sanity control (§4.7);
  that is **not** a proof of (S).

**Conditional result.** Given (T) and (S), the `|P| = 24` branch is **CORRECT**: there is no direct
tiling `P ⊕ Q = Z_1320` with `A ⊆ P`, `Y ⊆ Q`, `|P| = 24`. I rederived every step of §6 independently
(§3) and recomputed the finite exclusion with two reviewer-written search algorithms, an independent
witness verifier, a positive gcd-220 control, per-class sensitivity, rejection mutations and randomized
brute-force completeness tests (§4). No author code was executed or imported.

**Defects:** FATAL none; MAJOR none; MINOR items in §5 (an omitted-but-valid strengthening that makes the
branch a pure counting contradiction, unconfirmed author node counts, wording). **Counterexamples:** none
to the branch; the relaxed instance becomes satisfiable only when one of the classes `3,5,8,11,220,440,660`
is dropped (§4.4), which shows the relaxation is tight at those classes, not that a tiling exists.

If (S) is false in the form used, the head screen, the transfer of `H`, and the `Q` screen all collapse and
nothing in this branch survives. If (T) is false (no direct border tiling, or wrong anchors/cardinalities),
the branch is vacuous. Everything below is conditional on both.

## 1. Inputs read in manifest order (all SHA256 / bytes / LF verified exactly)

| # | role | path (basename) | sha256 prefix | bytes | LF |
|---|---|---|---|---|---|
| 1 | f114 prerequisite manifest (not accepted) | `f114-shor-1320-two-border-sizes/manifest-v1.json` | `ad3f0ad3…` | 5366 | 95 |
| 2 | two-size reduction candidate | `frontier-20261028-1320-two-border-sizes-v1.md` | `0e2474a0…` | 5512 | 54 |
| 3 | order-1320 exclusion candidate | `frontier-20261028-1320-border-no-go-candidate-v1.md` | `52aeaff1…` | 11391 | 116 |
| 4 | size24 author quota search | `frontier-20261028-1320-p24-quota-check.py` | `4b1cb58d…` | 3073 | 58 |
| 5 | size24 author replay | `frontier-20261028-1320-p24-quota-replay.py` | `5aaee98e…` | 2086 | 42 |
| 6 | size44 author seed search | `frontier-20261028-1320-p44-seed-check.py` | `419611ff…` | 3158 | 56 |
| 7 | size44 author replay | `frontier-20261028-1320-p44-seed-replay.py` | `8aa5e270…` | 1837 | 34 |

Inputs 4–7 were read as text only (never executed, never imported). Inputs 6–7 are outside my branch and
are listed only because the manifest requires reading every input in order. I did not open any f114 input
beyond its manifest, any held payload, the web, or an external model.

## 2. What the author claims in §6 (restated for checking)

1. `|Q| = 55` is odd, so `Φ_2, Φ_4, Φ_8` divide the `P`-mask; `P` is uniform mod 8 with 3 per class.
2. The old-anchor head screen has exactly 3 candidates in each of the mod-8 classes 1, 2, 5, 6, forcing
   the twelve residues `33,198,253,418,473,638,693,858,913,1078,1133,1298 ∈ P`.
3. Differences of `198,253,418,473,693` from `33` have gcds `165,220,55,440,660`, so `Q − Q` must avoid
   `H = {55,165,220,440,660}` in addition to `{3,5,8,11}`.
4. `Q` has exactly 11 elements in each class mod 5 and 5 in each class mod 11.
5. Relaxation: keep only `Q`-elements in mod-5 classes `{0,4}` or mod-11 classes `{0,3}`; require anchors
   `0,14`, old-anchor compatibility, pairwise compatibility under the nine classes, and the four exact
   quotas `(11,11,5,5)`; 144 candidates; exhaustive search UNSAT; positive control SAT when only gcd 220
   is removed. Hence `Q` must use a `P` class — contradiction.

## 3. Independent rederivation (reviewer's own, from n = 1320, A, Y)

**3.1 Cardinality.** (T) gives `|P|·|Q| = 1320`, so `|Q| = 55`.

**3.2 Cyclotomic prime balance.** From (T), `P(x)Q(x) = (x^1320 − 1)/(x − 1) + (x^1320 − 1)R(x)` in
`Z[x]`, so for every `d | 1320`, `d > 1`, the irreducible `Φ_d` divides `P(x)` or `Q(x)`. For prime
`p ∈ {3,5,11}` (each dividing 1320 once) `Φ_p | P(x)` iff `P` is uniform mod `p`, which forces `p | |P|`;
hence the side whose cardinality `p` divides is uniform mod `p`: `5 ∤ 24, 11 ∤ 24` ⇒ `Q` uniform mod 5
(11 per class) and mod 11 (5 per class); `3 ∤ 55` ⇒ `P` uniform mod 3 (unused). For the 2-part: if
`Φ_8 | Q(x)` then the mod-8 counts satisfy `c_r = c_{r+4}` (since `1,ζ_8,ζ_8²,ζ_8³` are linearly
independent over `Q`), so `|Q|` is even; likewise `Φ_4 | Q(x)` gives `c_r = c_{r+2}` mod 4 and
`Φ_2 | Q(x)` gives `#even = #odd`. `|Q| = 55` is odd, so all three divide `P(x)`;
`Φ_2Φ_4Φ_8 = 1 + x + … + x^7` (checked by integer polynomial multiplication in the checker), which
divides `P(x) mod (x^8 − 1)`, so the eight mod-8 counts of `P` are equal: **3 per class**. Author claim 1 ✓.

**3.3 Head screen and forced twelve.** By (S), every `x ∈ P \ A` satisfies `gcd(x − a, 1320) ∉ GY` for
all `a ∈ A`, where `GY = gcd-classes(Y − Y) = {1,2,6,12}` (recomputed; `GA = {3,5,8,11}` likewise; the two
sets are disjoint, as (S) requires of the anchors themselves). This necessary screen has 112 residues with
mod-8 counts `(32,3,3,32,18,3,3,18)` for classes `0..7`. `A` occupies mod-8 classes 0 and 3 only, so classes
1, 2, 5, 6 need 3 new heads each and have exactly 3 candidates each: all twelve are forced. Author claim 2 ✓.
Closed form (hand derivation, machine-confirmed): `gcd(x − a, 1320) ∉ {1,2,6,12}` ⇔ `4 | x−a` or `5 | x−a`
or `11 | x−a`. For `x mod 8 ∈ {1,2,5,6}` no `x − a` (`a ∈ {0,3,8,11}`) is divisible by 4, so each `a` needs
`5 | x−a` or `11 | x−a`; the only consistent assignment is `11 | x, 11 | x−11, 5 | x−3, 5 | x−8`, i.e.
`x ≡ 33 (mod 55)`; the 24 residues of that class with `x mod 8 ∈ {1,2,5,6}` are exactly the twelve.

**3.4 Forced classes.** gcd classes of all `C(12,2) = 66` forced–forced differences are **exactly**
`H = {55,165,220,440,660}` (differences are `55k`, `k ≡ 0,3,4,7 (mod 8)`, so `gcd(k,24) ∈ {1,3,4,8,12}`;
classes 110 and 330 never occur). Author claim 3 ✓ (the author only needed `⊇`). The forced–old-head
differences additionally give the classes **`{10,15,22,30,33,66}`**, also forbidden to `Q − Q` by (S); the
author omits them. Omitting forbidden classes only enlarges the candidate set, so the author's `G = {3,5,8,11}
∪ H` is a valid relaxation (see §5 M1 for what the full set does).

**3.5 Sufficiency of the relaxation.** Any `Q` satisfying (T),(S) yields `Q' = Q ∩ ({x ≡ 0,4 (mod 5)} ∪
{x ≡ 0,3 (mod 11)})` with: `0,14 ∈ Q'` (the only old tails in these classes; `1,7,13` lie outside them);
every `x ∈ Q' \ Y` has `gcd(x − y) ∉ G` for all `y ∈ Y`; `Q'` is pairwise `G`-compatible; and `Q'` has
**exactly** `11, 11, 5, 5` elements in the four classes (3.2; the classes are fully contained in the relaxed
universe, and an element in both a mod-5 and a mod-11 class counts toward both quotas). So UNSAT of the
relaxed instance implies no `Q`, hence no tiling with `|P| = 24`. Author claims 4–5 ✓ in structure.

**3.6 Instance.** Candidates `{x : x in the classes, x = y or gcd(x−y,1320) ∉ G ∀ y ∈ Y}`: **144** (recomputed);
group sizes `mod5=0: 66, mod5=4: 66, mod11=0: 18, mod11=3: 18`; 24 candidates lie in two groups; after
forcing anchors the needs are `(10,10,4,4)` with `(65,65,17,17)` available — no counting contradiction at the
root, each mod-5 group alone admits 21 pairwise-compatible elements, so a genuine search is needed.

## 4. Independent computation (`size24-check-v1.py`, `size24-aux-v1.py`)

**4.1 Design (no author code).** The checker derives everything in §3 from `n, A, Y` with assertions, then:
- **GB** (group-branching): at each node remove groups whose remaining quota is 0; prune if some group has
  fewer available members than its remaining quota; pick the positive-quota group with minimum slack; let
  `e` range in ascending order over its available members, include `e` (removing `e`, its conflicts, and all
  smaller members of that group), recurse. *Completeness:* a solution `S'` of the subproblem has a smallest
  element `e` in that group; the branch for `e` keeps `S' \ {e}` available with exact updated quotas; by
  induction it is found. *Soundness:* every returned set is re-checked by `verify`.
- **LAY** (layered, differently ordered): enumerate by `itertools.combinations` all exact pairwise-compatible
  fills of the two mod-11 groups (225 × 225), keep the 12,418 cross-compatible pairs, then fill the two mod-5
  groups with GB restricted to those groups (mod-11 universe removed since its quotas are full).
- **`verify(W, forb, quotas)`** is independent of the search data structures: it checks residues, no
  duplicates, anchors, class membership, old-anchor compatibility, pairwise compatibility and exact counts.
- Quota pruning is the only non-trivial pruning; its validity is the exactness of 3.2 (over-fill is
  impossible, under-fill is infeasible). Both searches are also cross-checked against brute force (4.6).

**4.2 Main result (author's nine classes `G`).**
GB: **UNSAT**, 6,599 nodes, 5,198 quota prunes. LAY: **UNSAT**, 12,418 compatible mod-11 fills; 12,427 GB
nodes with 12,426 quota prunes, i.e. every mod-11 fill but one is already counting-infeasible in the mod-5
groups and the single survivor dies after 9 branches. Wall time of the whole checker: 0.9 s.
Monotone sanity: under the full known set `G_full = G ∪ {10,15,22,30,33,66}` only 56 candidates remain and GB
is UNSAT at the root (1 node).

**4.3 Positive control (only gcd 220 removed).** GB finds a 22-residue witness in 21 nodes:
`0,14,44,110,120,164,204,230,234,240,264,284,324,330,350,360,384,404,410,450,564,630`, verified by `verify`
under `G ∖ {220}` (exact `(11,11,5,5)`, anchors, all compatibilities); under `G` it fails at the old-anchor
pair `(234,14)` (gcd 220) and has six gcd-220 collisions. The author's literal 22-residue list `W` (quoted as
data from input 4) was checked by my verifier: **passes** under `G ∖ {220}` and **fails** under `G` with
collisions `(14,234),(680,900),(704,924)` — the author's nonvacuity statement is confirmed.

**4.4 Per-class sensitivity (drop one class, GB).** Dropping `3` (226 cand.), `5` (260), `8` (218),
`11` (212), `220` (146), `440` (146) or `660` (146) each yields **SAT** (verified witnesses recorded in
`size24-run-v1.json`); dropping `55` (152 cand., 8,900 nodes) or `165` (146 cand., 5,468 nodes) stays
**UNSAT**. Dropping all of `H` (160 cand.) is SAT. So the load-bearing classes of the relaxed instance are the
four old-head classes plus `220, 440, 660`; `55` and `165` are individually redundant.

**4.5 Rejection mutations (verifier must reject; 8/8 rejected with the expected reason).** author `W`
under full `G` (gcd-220 old-anchor conflict); anchor 14 dropped; `60→61` (outside classes); `60→55`
(conflict with 0, gcd 55); duplicate entry; `60` dropped (quota `[10,11,5,5]`); reviewer witness under full
`G`; wrong quota vector `(11,11,4,4)`.

**4.6 Randomized brute-force completeness/soundness.** 400 seeded sub-instances (anchors + 12 random
candidates; 214 with planted compatible sets fixing the quotas, 186 with random quotas; 117 with one
forbidden class removed): brute-force enumeration over all subsets agreed with both GB and LAY in every
trial (263 SAT / 137 UNSAT); all three witnesses per SAT trial passed `verify`. Finite controls do not prove
completeness; the proof is the argument in 4.1.

**4.7 Auxiliary controls (`size24-aux-v1.py`).**
- Root counting under `G_full`: non-anchor mod-11 survivors are only `{110,330,770}` (class 0) and
  `{564,1004,1224}` (class 3), i.e. 3 available vs 4 needed in each — the branch is a pure counting
  contradiction once the six omitted classes are used (see M1).
- Sands small-`n` sanity control: all direct tilings `A ⊕ B = Z_n`, `0 ∈ A ∩ B`, `|A|² ≤ n`, `n ≤ 36`
  (684,772 tilings, all complements found by DFS) have disjoint gcd-class sets. Zero violations. This supports
  the *statement* of (S) used by the author; it is not a proof and does not substitute for the f114 review.

**4.8 Execution receipts.** `size24-run-v1.json` (`receipt` block): checker self-hash
`1c312d630213c6bbdb70f416412d4d3c2fb0dda3f8874056f33406d0e1a2bcbf`, Python 3.14.3,
macOS-27.0.1-arm64, `/bin/date` before `Wed Oct 28 19:46:55 PDT 2026`, after `19:46:56`, 0.9 s, exit 0.
`size24-aux-v1.json`: script self-hash `fe34107740c93b6dddf614c274f95f9dd098682665d7ebe91d842ef0ae78df58`,
before `19:50:27`, after `19:50:42`, 15.4 s, exit 0. Reproduce with `python3 size24-check-v1.py` and
`python3 size24-aux-v1.py` in this directory (each rewrites only its own `size24-*.json`).

## 5. Findings

- **FATAL:** none found in the `|P| = 24` branch.
- **MAJOR:** none found.
- **MINOR M1 (omitted valid strengthening).** The author forbids only `{3,5,8,11} ∪ H` for `Q − Q`, omitting
  the six forced-head–old-head classes `{10,15,22,30,33,66}` that (S) equally forbids. The omission is a
  valid relaxation, so the UNSAT stands; but with the full set the mod-11 quotas fail by counting at the root
  (3 available vs 4 needed per class), so the exhaustive search and the 144-candidate relaxation are more than
  is needed. Worth stating in a revision; not a defect of correctness.
- **MINOR M2 (unconfirmed author counts).** The author's search statistics (831/356/60 and 991/496) were not
  independently confirmed because author code was not executed; they are not load-bearing. My independently
  designed searches return UNSAT with different, algorithm-specific counts (6,599 and 12,427 nodes).
- **MINOR M3 (wording).** §6 calls the two author programs "independent implementations"; both are the same
  author in the same harness, as the header of the same document correctly states. The text says "Hence Q must
  avoid all five gcd classes H" where `H` is in fact exactly the forced–forced class set (3.4) — correct, and
  slightly understated.
- **Dependency, not a defect (D1).** (S) is load-bearing three times in this branch (head screen, transfer of
  `H`, `Q` screen). Its reconstruction lives in the f114 chain and is not reviewed here.
- **Dependency, not a defect (D2).** Everything is conditional on (T): the border theorem reconstruction, the
  anchors, direct tiling, and the cardinality partition leaving `{24,44}`, all in the unaccepted f114 chain.

## 6. Dependencies and what this review does and does not establish

- Establishes (conditional on (S)): the finite statement "no direct tiling `P ⊕ Q = Z_1320` with
  `{0,3,8,11} ⊆ P`, `{0,1,7,13,14} ⊆ Q`, `|P| = 24`". The connection of that statement to codes (that any
  order-1320 completion yields such a tiling) is (T), owned by f114.
- Does **not** establish: (S); (T); the `|P| = 44` branch (separate reviewer); the combined candidate theorem
  of input 3; any all-order noncompletion; novelty or priority; anything about the historical held outcomes
  (none was used as a premise).
- Acceptance of the candidate theorem still requires: the f114 disposition, the size44 review, and the
  owner-mandated separation from this same-harness review (human / independent-family / formal as the
  contract requires).

## 7. Limitations

Same harness and language as the author (Python, `math.gcd`); shared blind spots are possible in principle,
mitigated by: different search algorithms, a search-independent verifier, author-free derivation of every
list, hand closed forms for the forced heads and `H`, brute-force agreement on sub-instances, and a positive
control. The brute-force trials cover only 14-element sub-instances. The Sands control covers `n ≤ 36` only.
No formal/kernel verification was performed.

## 8. Reviewer artifacts (all under this directory, prefix `size24-`)

| file | sha256 | bytes | LF |
|---|---|---|---|
| `size24-check-v1.py` | `1c312d630213c6bbdb70f416412d4d3c2fb0dda3f8874056f33406d0e1a2bcbf` | 20429 | 470 |
| `size24-run-v1.json` | `e81e40f035543328e4db9f3d695e48a6939af56c3b9938d48431ee55723bf794` | 7076 | 532 |
| `size24-aux-v1.py` | `fe34107740c93b6dddf614c274f95f9dd098682665d7ebe91d842ef0ae78df58` | 5419 | 125 |
| `size24-aux-v1.json` | `4fb344716bc59369b802faf29ecbf40490bdcf1ca6027ec880709a04df51f5a1` | 1802 | 119 |
| `size24-review-v1.md` | (this file; hash reported by the parent) | | |

Not mine and left untouched: `size44-*` files and `__pycache__/size44-independent-search-v1.cpython-314.pyc`
(created by the size44 reviewer's import). No file outside this directory was written; no deletion, Git,
web, external model, author contact or infrastructure action was performed.

**END OF size24 REVIEW.**
