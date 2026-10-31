# f117 size-44 branch: independent same-harness review (size44-review-v1)

Review wave `f117-shor-1320-final-cardinality-cases`, manifest `manifest-v1.json`
SHA256 `5ba7dfc08c681e28bb9e9d1f2ae6134bbf62f634061eb17c0e131b6d71258346` (3824 bytes), hash
re-computed before reading. `/bin/date -u` before this file was written: see §9 receipt.
Reviewer: same-harness agent. **Not** a human, independent-model-family, kernel/formal or
novelty review. No author contact, no web_search, no external model or paid API, no Git,
no deletion, no publication, no live-infrastructure change, no repo build/lint/format/test
suites. Author code was read in full but **never executed or imported**.

## 1. Exact scope and boundary

Reviewed claim (no-go candidate §7 only): *conditional* on the actual-border premises and
the unadopted f114 two-size reduction, the border cardinality `|P| = 44, |Q| = 30` is
impossible at `n = 1320`.

Premises taken as given and **not adopted here** (they are f114's / predecessors' scope):

* (T) `Z_1320 = P (+) Q` is a direct tiling with `A = {0,3,8,11} ⊂ P`, `Y = {0,1,7,13,14} ⊂ Q`.
* (S) Sands divisor-class disjointness: nonzero differences of `P` and of `Q` never share
  a gcd with 1320.
* (U) Prime uniformity for `r ∈ {3,5,11}`: the factor whose cardinality `r` divides is
  equidistributed mod `r`.
* The reduction of the cardinality list to `{24, 44}` (f114, under separate review).

Expressly **excluded**: any all-order statement; any unconditional order-1320 exclusion
(the result is conditional on (T)); the `|P| = 24` branch (separate reviewer); the correctness
of (T),(S),(U) themselves; any historical held mathematical outcome; the Z3 observation
(not used). Finite controls prove the finite statements only; they do not prove the
completeness of the written reduction beyond what §3 derives.

Reviewer side-check, **not** an adoption of f114: (U) and (S) follow from (T) by the
cyclotomic criterion (`Z_n = P (+) Q` iff `|P||Q| = n` and every `Φ_t`, `t | n`, `t > 1`,
divides `P(x)` or `Q(x)`): `Q(ζ_r) = 0` forces equidistribution mod `r` hence `r | |Q|`,
giving (U); and `Φ_t | P(x^k) ⇔ Φ_t | P(x)` for `gcd(k,n) = 1` gives `kP (+) Q = Z_n`, so a
common subgroup `⟨p−p'⟩ = ⟨q−q'⟩` would yield `k p + q' = k p' + q` with `kp ≠ kp'`,
contradicting directness, giving (S). This is recorded for transparency only.

## 2. Inputs verified (declared order; SHA256 / bytes / LF all matched)

| # | role | SHA256 (prefix) | bytes | LF |
|---|---|---|---|---|
| 1 | f114 manifest | ad3f0ad3…30eaf | 5366 | 95 |
| 2 | two-border-sizes-v1.md | 0e2474a0…fae946 | 5512 | 54 |
| 3 | border-no-go-candidate-v1.md | 52aeaff1…385869e | 11391 | 116 |
| 4 | p24-quota-check.py | 4b1cb58d…252d76bf | 3073 | 58 |
| 5 | p24-quota-replay.py | 5aaee98e…038f9fc6 | 2086 | 42 |
| 6 | p44-seed-check.py | 419611ff…b354727f7f | 3158 | 56 |
| 7 | p44-seed-replay.py | 8aa5e270…422edff80 | 1837 | 34 |

Full hashes equal the manifest entries character for character (checked with
`shasum -a 256`, `wc -c`, `tr -cd '\n' | wc -c`). Inputs 4–5 (size 24) were read for
context only and are outside this review.

## 3. Independent written rederivation of the branch

Notation: `n = 1320 = 2^3·3·5·11`; `gc(d) = gcd(d mod n, n)`;
`GA = gc(A−A)\{n} = {3,5,8,11}`, `GY = gc(Y−Y)\{n} = {1,2,6,12}` (recomputed).

**3.1 Mod-11 uniformity of P.** `|P| = 44`, `|Q| = 30`. `11 ∤ 30`, so `Q(ζ_11) ≠ 0`
(a vanishing sum of 11th roots with nonnegative integer coefficients forces all eleven
residue counts equal, impossible for 30). The tiling criterion needs `Φ_11 | P(x)Q(x)`, hence
`Φ_11 | P(x)` and `P` has exactly four residues in every class mod 11. The anchors
`0,3,8,11` lie in classes `0,3,8,0`; classes `1` and `2` contain no anchor.

**3.2 Head screen and forced gcd 55.** Every `p ∈ P` satisfies `gc(p − a) ∉ GY` for all
`a ∈ A` (by (S) with `Y ⊂ Q`). The screened head set has 112 residues; its mod-11 class
sizes are `{0:40, 1:6, 2:6, 3:12, 4:6, 5:6, 6:6, 7:6, 8:12, 9:6, 10:6}`. Classes 1, 2:

    C1 = {155,188,243,848,903,936},   C2 = {35,68,123,728,783,816}      (recomputed)

gcd-55 edges: `C1`: 188–243, 188–903, 243–848, 848–903 (a 4-cycle); `C2`: 68–123, 68–783,
123–728, 728–783 (a 4-cycle). If `P` avoided class 55, at most two of each 4-cycle could be
chosen, so the four picks would be `{155,936} ∪` an antipodal pair, i.e. exactly
`{155,188,848,936}` or `{155,243,903,936}`, and likewise `{35,68,728,816}` or
`{35,123,783,816}`. Forced elements: `155,936 ∈ P` and `35,816 ∈ P`. But
`gc(155−816) = gcd(661,1320) = 1 ∈ GY` (661 is prime) — and independently
`gc(936−35) = 1 ∈ GY` — contradicting (S) with `Y ⊂ Q`. Stronger exhaustive form
(reviewer): among all `(4 ⊂ C1, 4 ⊂ C2)` choices that are GY-free inside and across, there
are exactly **61** admissible pairs and **0** of them avoid class 55. Hence `P` contains a
difference of class 55, and by (S) **Q must avoid class 55**. The author's text is correct;
its "sole remaining candidate" step is a special case of the exhaustive statement.

**3.3 Q balances.** `3 ∤ 44` and `5 ∤ 44`, so `Φ_3 | Q(x)` and `Φ_5 | Q(x)`: `Q` has exactly
10 residues in each class mod 3 and 6 in each class mod 5. Anchors: mod 3 → `{0}`,
`{1,7,13}`, `{14}`; mod 5 → one per class.

**3.4 Elementary screen facts under `G = GA ∪ {55} = {3,5,8,11,55}`.**
(i) Parity lemma: a screened `x ≡ 1 (mod 3)` is odd. If `x` were even, `x−1, x−7, x−13` are
odd multiples of 3 occupying three distinct residues mod 5 and mod 11, so at least one of
them is coprime to 2, 5, 11 and has gcd exactly 3 — forbidden. (Verified: all 116 class-1
residues screened under `GA` alone are odd.)
(ii) No screened class-1 residue in mod-5 class 0 or 4: for `x ≡ 0 (5)`, `x ≡ 1 (3)`, `x`
odd, `gc(x − 0) = 5·11^c ∈ {5,55}`; for `x ≡ 4 (5)`, `gc(x − 14) = 5·11^c ∈ {5,55}` (`x−14`
odd, `≡ 2 (3)`). Both forbidden under `G`. (Verified: the list is empty; under `GA` alone
the eight such residues `55,289,385,619,715,949,1045,1279` all have gcd 55 against 0 or 14.)

**3.5 Twelve candidates and why eight must be selected.** By 3.3 the six `Q`-residues in
mod-5 class 0 and the six in class 4 are all in mod-3 classes `{0,2}` (by 3.4(ii)); they
contain the anchors 0 and 14. `Q` has exactly `10+10 = 20` residues in mod-3 classes
`{0,2}`; twelve of them are those, so exactly **8** more lie in mod-5 classes `{1,2,3}` with
residue `≢ 1 (mod 3)`, and each must pass the `Y`-screen under `G`. The screen admits
exactly **12** such residues (recomputed, with `(mod 5, mod 3)` of each):

    47(2,2) 363(3,0) 443(3,2) 561(1,0) 627(2,0) 641(1,2) 693(3,0) 707(2,2)
    773(3,2) 891(1,0) 971(1,2) 1287(2,0)

The anchors `1,7,13` are in mod-3 class 1 and are not among them. So the non-class-1 part
of any actual `Q` restricted to mod-5 classes `{1,2,3}` is an 8-subset ("seed") of this
list: `C(12,8) = 495` seeds. (These are tail/`Q` candidates; the assignment's word "heads"
for them is a terminology slip, not an author error.)

**3.6 Relaxed instance `R(G)` and its soundness.** Find a seed `S` (8 of the 12), a 6-set
`L ⊂ {screened, ≡0 (5)}` with `0 ∈ L`, a 6-set `R ⊂ {screened, ≡4 (5)}` with `14 ∈ R`,
such that `T = S ∪ L ∪ R` (20 residues) is pairwise `G`-free and has exactly 10 residues
`≡ 0 (3)` and 10 residues `≡ 2 (3)`. If an actual `Q` existed, its non-class-1 part is such
a `T` (3.3–3.5 and (S)). The instance drops the ten class-1 residues of `Q` and every
other constraint, so it is a pure relaxation: **UNSAT of `R(G)` excludes the branch.**
Screened base sizes: 70 residues in class 0, 70 in class 4 (none in mod-3 class 1).

## 4. Independent finite execution (reviewer code only)

Program `size44-independent-search-v1.py` (written from scratch; bitmask clique
enumeration; exclusive-create output). Two different exhaustive structures:

* **Structure 1** (seed enumeration): all 495 seeds → seed-internal `G` check → seed-filtered
  availability → all anchored 6-cliques per class → every `(L,R)` pair tested for balance
  and cross `G`-freeness (both always computed and counted).
* **Structure 2** (quota DFS): one ordered include-enumeration over the merged universe
  `X12 ∪ B0 ∪ B4` with group quotas `(8,5,5)` after preselecting anchors, pruning on
  quotas and on reachable mod-3 counts; no reuse of structure 1's masks.

Main run (clock `/bin/date -u` before/after: `2026-10-29T02:46:13Z` / `02:46:14Z`; program
`utc_start = utc_end = 2026-10-29T02:46:14Z`; 0.296 s; Python 3.14.3, macOS 27.0.1 arm64):

| count | reviewer | author §7 / code |
|---|---|---|
| seeds | **495** | 495 |
| seed conflicts | **474** | 474 |
| compatible seeds | **21** | 21 |
| anchored 6-sets, class 0 (sum over seeds) | **8739** | n/a |
| anchored 6-sets, class 4 (sum over seeds) | **8739** | n/a |
| `(L,R)` pairs examined | **104 112** | n/a |
| balanced pairs (10/10) | **156** | 156 |
| cross-compatible pairs (balance ignored) | **0** | n/a |
| balanced and cross-compatible | **0** | 0 |
| structure-2 solutions / nodes | **0 / 505** | n/a |

Per-seed `(|L|,|R|)` histogram: `(6,6)×3, (798,6)×6, (1293,6)×3, (6,1293)×3, (6,798)×6`.
Head side: 61 admissible choice pairs, 0 avoiding 55 (§3.2).

Supplement `size44-supplement-v1.py` (02:49:10Z–02:49:11Z, 0.495 s): balance-free
exhaustive structure-2 search over all 21 splits `zeros+twos = 20` → **0** solutions
(6222 nodes); minimum number of cross-conflicting element pairs over all 104 112 `(L,R)`
pairs is **4** (no pair is within one conflict of admissibility); inside each class the rule
"conflict ⇔ different mod-3 class and different parity" has 0 violations in both 70-sets;
every admissible `L` is either all-even or entirely `≡ 0 (3)` (dually for `R`), which is the
structural reason the cross test never passes.

## 5. Mutation controls (same instance, one check disabled at a time)

| mutation | effect | reading |
|---|---|---|
| skip cross test | accepted = **156** (= balanced pairs) | cross test is what rejects every balanced pair |
| skip balance test | accepted = **0**, cross-ok = 0 | balance is **not** load-bearing in the final step |
| skip seed-conflict test | compatible = **495**, balanced = **6420**, accepted = **0** | seed test is exercised; cross conflicts still exclude everything |
| drop anchor 14 from the Y-screen | screen 381, extras 72, class-1 in classes 0/4: 40 | instance is anchor-sensitive; the 12-list depends on 14 |

## 6. gcd-55 relaxation positive controls

* **Full GA-relaxed instance** (forbidden `{3,5,8,11}`, extras recomputed → 30, bases 74→70
  after removing class-1): structure-2 DFS, first witness only, **SAT** after 12 133 nodes:
  `{0,14,20,44,62,68,110,114,120,140,230,234,264,282,288,384,398,618,716,936}`; checked by
  the reviewer's direct checker (distinct, anchors, Y-screen, pairwise-free, counts
  `[6,6,10,10,0]`) and it contains a gcd-55 difference (so it is genuinely excluded by `G`).
* **Author's 20-residue witness** `W` from `p44-seed-check.py`, checked by reviewer code
  only: passes all GA-constraints and quotas, contains gcd 55 vs `Y` (e.g. `936−1 = 935`),
  and **fails** under `G` (Y-screen). Consistent with the author's description.
* **Restricted control** (55 dropped but seeds still from the same 12 and bases still
  non-class-1): all counts identical (495/474/21/156/0, cross-ok 0). Supplement 2
  explains this: no gcd-55 pair survives inside any seed-filtered availability for any of
  the 21 compatible seeds, and the 56 gcd-55 pairs of the universe lie between residues of
  different parity *and* different mod-3 class, which never co-occur in an admissible
  6-set. **Mechanism:** the 55-ban is load-bearing through the `Y`-anchor screen — it removes
  the 18 extras `62,68,276,282,288,386,398,612,618,716,722,936,948,1046,1052,1058,1266,1272`
  (each has gcd 55 against some `Y` anchor) and the 8 class-1 residues of classes 0/4 — not
  through pairwise 55-conflicts inside the universe. The GA witnesses above use only
  extras from the removed 18.

## 7. Findings

**FATAL: none. MAJOR: none** in the size-44 branch as written, conditional on §1.

MINOR (documentation/precision; none affects the conclusion):

1. No-go §7 states "Exactly 156 candidate pairs meet the balance quotas"; both author
   programs only *print* this figure (their asserts cover 495/474/21 and 0). Reviewer
   independently reproduces 156, so the statement is true, but it is not program-pinned.
2. §7 presents the mod-3 balance as part of the exclusion test; in fact every one of the
   104 112 `(L,R)` pairs already fails the cross-gcd test (minimum 4 conflicts), so the
   exclusion is stronger than stated and does not depend on the balance step. Suggest
   noting this margin.
3. §7's relaxation description could say explicitly that the 55-ban acts via the anchor
   screen (18 extras and 8 class-1 residues removed), since the stated positive control `W`
   uses extras that are *not* in the 12-list; a reader may otherwise expect `W` to be a
   solution of the identical 495-seed instance with 55 lifted (it is not; see §6).
4. The forced-head argument can be stated exhaustively (61 admissible GY-free choice
   pairs, none 55-free) and has a second gcd-1 collision (`936−35`); harmless redundancy.

Counterexamples found: none. Author-code review (read only): the seed program and the
complement replay implement exactly the instance of §3.6; their `okay`/`conflict`
predicates, anchor retention, quota tests and cross tests agree with the reviewer's
reconstruction; the `break`-on-witness logic cannot truncate the balanced-pair count when
no witness exists.

## 8. Dependencies the verdict rests on

(T) actual border tiling with anchors `A ⊂ P`, `Y ⊂ Q` (predecessor border factorization;
f114 chain); (S) Sands disjointness and (U) prime uniformity (predecessor divisor-class
packet; reviewer side-derivation in §1 is not a substitute for their review); `|P||Q| =
1320`; the f114 two-size reduction that makes 44 one of the two remaining sizes (not
accepted). Nothing is imported from held outcomes, Z3, or the size-24 branch.

## 9. Receipt

Environment: `/opt/homebrew/opt/python@3.14/bin/python3.14` 3.14.3, macOS 27.0.1, arm64.
All programs exact-integer, deterministic, exhaustive unless marked "first witness only".

| artifact | SHA256 | bytes | LF |
|---|---|---|---|
| size44-independent-search-v1.py | 5ded821552ec68ac80bb2f45340aaf09a9866139d047b90c33f0fefa4f953ec0 | 20874 | 438 |
| size44-independent-search-output-v1.json | 172a74909377886971b9eac7283fbaaa5b69fe46acd1ca6a234c871ba7126204 | 7716 | 568 |
| size44-supplement-v1.py | 0a4cc7b1edbd372d15b3885d0b65c5330f01a3a60066f287da878dee6b5e89a3 | 6861 | 156 |
| size44-supplement-output-v1.json | 95cc7ad25dcc375bb3798611c5a5c8a0be57e2c8b6308b09f75eecff4aac1a5b | 20010 | 1747 |
| size44-supplement2-v1.py | 1d76b9cdf6f71aa4965364e82b91fe5a37013d199de63c5ec2f78b193775b052 | 4098 | 81 |
| size44-supplement2-output-v1.json | 34160ec8f59cbc89b5dbeab38e6a68b13b7768bd3c07e740d797a023fe7f13eb | 10729 | 1080 |

Clocks (`/bin/date -u`): manifest hash check 02:35:49Z; main run 02:46:13Z–02:46:14Z;
supplement 02:49:10Z–02:49:11Z; supplement 2 02:51:08Z; hashing 02:51:18Z (all 2026-10-29
UTC = 2026-10-28 PDT evening). The hash of this review file is reported in the handoff
message, not inside it.

Side effect disclosed: `__pycache__/size44-independent-search-v1.cpython-314.pyc`
(37354 bytes, SHA256 f68aa65aec08ac146d861d89036df1e0d4396ebccf8c8bcaf46f6581227b75c9) was
created at 19:49 PDT by the supplements importing the reviewer's own module. It is not
evidence; not removed (no deletion authority). Sibling `size24-*` files in this directory
belong to the size-24 reviewer and were neither read nor touched.

## 10. Verdict (scoped)

**Size-44 branch: EXCLUDED, conditional.** Under (T), (S), (U) and the f114 cardinality
reduction, the reviewer independently rederived mod-11 uniformity of `P`, the forced gcd-55
class in `P` (61 admissible head choices, none 55-free; forced `155/936` vs `816/35`
collide in class 1 ∈ GY), the `Q` balances, the empty class-1 set in mod-5 classes 0/4, the
exact 12-candidate list and the necessity of an 8-seed, and executed two independently
structured exhaustive searches of the relaxed instance with counts
**495 / 474 / 21 / 156 balanced / 0 cross-compatible / 0 solutions** (plus balance-free
0 solutions and a minimum cross-conflict margin of 4). Mutation controls show each enabled
check is exercised; the gcd-55 relaxation is SAT (reviewer witness and author witness both
verified), so the 55-ban — acting through the anchor screen — is the operative constraint.
No FATAL or MAJOR defect; four MINOR documentation notes. This is **not** an all-order
result, **not** an unconditional order-1320 exclusion, **not** an acceptance of f114 or of
any source premise, and **not** a human, independent-family, formal/kernel or novelty review.

END OF SIZE-44 REVIEW.
