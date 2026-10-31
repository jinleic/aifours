# f128 review: all-order divisibility, order-660 exclusion, universal 55-tail branch

**Wave:** `f128-shor-660-exclusion-and-divisibility`, manifest `manifest-v1.json` SHA-256 `2dac20119db1afef26f655256fafed9688a845caf55518636e0d5e34b28fea80` (3427 bytes). Native `/bin/date` observed before composing this file: **2026-10-28T20:47:50-0700 PDT** (first copied into the review directory at 2026-10-28T20:50:01-0700 PDT, SHA-256 `a997d3bccd04c1a8a34006a190ed4b956ab6f754f203e38f9d48b310706edbb7`; re-written at **2026-10-28T20:50:26-0700 PDT** solely to backslash-escape `|` characters inside backtick spans of markdown table rows so the verdict table renders; no wording or verdict changed).
**Kind:** independent same-harness scientific review. Not a human, independent-model-family, formal/kernel or novelty certification. No web search, external model, author contact, Git, deletion or infrastructure change was used. The author checker was read, never executed or imported.

## Verdicts (exact scope)

| Scope | Verdict | Findings |
|---|---|---|
| (a) All-order necessary condition `660 \| n OR 2310 \| n` for the actual pure-a order n, from the old anchors under the adopted border/Sands framework | **ACCEPT — 0 FATAL / 0 MAJOR / 0 MINOR** | Rederived in writing for every n ≥ 2; finite control shows the anchor-only Sands screen passes exactly the multiples of 660 or 2310 up to n = 30000 (so the statement is also tight for anchors alone). |
| (b) No direct border tiling `P ⊕ Q = Z_660` with `{0,3,8,11} ⊆ P`, `{0,1,7,13,14} ⊆ Q`; hence no finite UD factor-complete extension of the literal Shor code has actual pure-a order 660 | **ACCEPT — 0 FATAL / 0 MAJOR / 2 MINOR (presentational)** | Every residue, capacity, slot, matching and shortage fact reproduced by independently written exact integer code; additionally every divisor size 4–42 is excluded by an independent pure-directness exact-cover search, so the exclusion does not even need the author's residue arguments or the seven-head predecessor. |
| (c) Universal 55-tail obstruction: no direct tiling with the anchors, `\|P\| = 3·2^k`, `\|Q\| = 55` at `n = 165·2^k`, k ≥ 2 | **ACCEPT — 0 FATAL / 0 MAJOR / 1 MINOR (presentational)** | The CRT rectangle, three forced classes, projection injectivity and the four-versus-five class-7 shortage are rederived in writing for all k ≥ 2 and controlled exactly for k = 2..9. |

**Not claimed, in any scope:** no all-order completion or no-go; no order floor of any kind (order 1980 is unreviewed and nothing here touches it); no exclusion of any order other than 660 (the (c) branch excludes one border-cardinality family only); no novelty/priority statement.

## Stated premises (every load-bearing input is listed here)

All taken from the adopted disposition `dispositions/math-5-shor-order1320-border-exclusion-parent-v1.md` (SHA `7157…ef9d`), not from any historical held outcome:

1. **Border tiling.** Any finite UD factor-complete D ⊇ literal Shor code has a unique pure-a atom `a^n`, n ≥ 26, and with `P = {i mod n : a^i b^k ∈ D, k ≥ 1}`, `Q = {j mod n : b^l a^j ∈ D, l ≥ 1}` a direct tiling `P ⊕ Q = Z_n`, `|P||Q| = n`, with `A = {0,3,8,11} ⊆ P` and `Y = {0,1,7,13,14} ⊆ Q` (the 16 literal words `b·a^{0,1,7,13,14}`, `a^{3,8,11}·b…` supply exactly these).
2. **Cyclotomic/prime balance.** `P ⊕ Q = Z_n` iff `|P||Q| = n` and for every `d | n, d > 1`, `Φ_d | P(x)` or `Φ_d | Q(x)`; `Φ_p | P(x)` (p prime, p | n) iff P is uniform modulo p; `Φ_{2}Φ_{4}…Φ_{2^k} | P(x)` iff P is uniform modulo `2^k`; `Φ_d | S(x)` forces `Φ_d(1) | S(1) = |S|`, so a prime power `Φ_{p^j}` cannot divide the mask of a set whose size is not divisible by p.
3. **Sands (necessary direction).** If `P ⊕ Q = Z_n` then no nonzero P-difference and nonzero Q-difference have the same gcd with n.

Everything below is derived from 1–3 and exact integer facts; the seven-head predecessor (`|P| ≥ 7`) is used by the author for (b) and was hand-checked, but my control shows (b) also holds without it.

## Inputs read completely, in declared order (all SHA-256/bytes/LF verified before reading)

| # | Input | SHA-256 | bytes/LF |
|---|---|---|---|
| 1 | `dispositions/math-5-shor-order1320-border-exclusion-parent-v1.md` | `715755734f720c37027d178d17cd2df9b6c69ea48af732b75daebaba25ef9d90` | 9593/68 |
| 2 | `frontier-20261028-seven-head-border-obstruction-v1.md` | `713afb914e2781c8367e31726c298bc158c2c5b61176277c2d219762dfd96e24` | 7566/91 |
| 3 | `frontier-20261028-660-and-order-floor-candidate-v1.md` | `cce97442e94386f80e9d63f782c5be83c7c4c0e3a7eddb5eb38e0c999494ab79` | 6677/80 |
| 4 | `frontier-20261028-660-border-exclusion-check.py` (read only) | `3d93de9d4968b8ab36606d4128d7d5f424ac79376390ced8213351aff98ddde4` | 2253/41 |
| 5 | `frontier-20261028-universal-55-tail-obstruction-v1.md` | `d6c9929c1a6a2a69f79f4951e76443b752764f035f1d80af9760876aba1c6673` | 5575/62 |

## (a) All-order divisibility — independent rederivation

Nonzero Q-differences include `1 − 0 = 1`, gcd 1 with every n. By premise 3 every nonzero P-difference must have gcd ≠ 1 with n. The P-differences `3 = 3−0`, `5 = 8−3`, `8 = 8−0`, `11 = 11−0` are nonzero for n ≥ 26, so `3 | n`, `5 | n`, `2 | n` (from gcd(8,n) ≠ 1), `11 | n`; hence **`330 | n`**. (Even without n ≥ 26 the same conclusion holds for every n ≥ 2 by cases, which the control confirms.)

With `2 | n`: if `v_2(n) = 1` and `7 ∤ n` then `gcd(8, n) = 2` (P-difference) and `gcd(14 − 0, n) = 2` (Q-difference) coincide, contradicting premise 3. So `4 | n` or `7 | n`, i.e. **`660 | n` or `2310 | n`**. The candidate's equation (1) is exactly this and it correctly refrains from asserting `660 | n` unconditionally.

Tightness: my control (`A_divisibility`) evaluates the full anchor-only Sands screen for every `2 ≤ n ≤ 30000`; the pass-set equals exactly the 51 multiples of 660 or 2310 in that range (negatives 330, 990, 1650, 2970 fail; 1980, 2310, 4620 pass; below 1980 only 660 and 1320 pass). So no further divisibility follows from the anchors alone; anything stronger needs other inputs.

## (b) Order 660 — independent rederivation of every step

`n = 660 = 4·3·5·11`. Old classes: `G_A = {3,4,5,11}` (from 3,8,11,5,8,3) and `G_Y = {1,2,6,12}` (from 1,7,13,14,6,12,13,6,7,1 → gcds 1,1,1,2,6,12,1,6,1,1). ✓

**Head screen.** `P ⊆ PC := {x : x ∈ A or ∀a ∈ A, gcd(x − a, 660) ∉ G_Y}` (premise 3 applied to each new head against each anchor). Independently recomputed: `|PC| = 42`, `PC = {0,3,8,11,33,63,68,88,123,128,132,143,183,188,198,243,248,253,256,264,275,303,308,363,368,396,407,415,418,423,428,473,483,488,528,539,543,548,583,603,608,638}`; class counts mod 3 `[18,6,18]`, mod 5 `[3,3,2,32,2]`, mod 4 `[18,3,3,18]`, mod 11 `[20,2,2,3,2,2,2,2,3,2,2]`. So `|P| ≤ 42`; with `|P| ≥ 7` (seven-head predecessor, whose four/five/six-head collision identities I re-verified by hand: e.g. target `U+4` candidates `U+4, U+1, U−4, U−7, 4` collide via `7+U, 1+U, 7+U, 1+U, 1+3`; target `U+9` leaves only `U+9 ∈ Q`, and `(U+9)+V = (V+9)+U` kills six heads) the divisor sizes are exactly **`{10,11,12,15,20,22,30,33}`**. ✓

**Capacities.** For `p ∈ {3,5,11}` (each `p ∥ 660`) exactly one of `|P|, |Q|` is divisible by p, and premise 2 makes that side uniform mod p. Size 33 → P uniform mod 3, 11 per class, but class 1 has 6 candidates. Sizes 15/20/30 → 3/4/6 per mod-5 class, but class 2 has 2. Size 11 → 1 per mod-11 class, but `0 ≡ 11`. ✓

**Size 10 (18-slot).** P uniform mod 5, two per class; classes 2 and 4 of PC are exactly `{132,407}` and `{264,539}`, all forced. `gcd(132−407,660) = 55`, `gcd(132−0,660) = 132`, so Q-differences avoid `G_10 = G_A ∪ {55,132}`. Screen `Q_10` (100 residues) has no residue `4 mod 6` (in fact none survives even `G_A` alone: `x−1, x−7, x−13` would each need a factor 5 or 11 while pairwise differing by 6 or 12). `|Q| = 66`, `3 ∤ 10` → Q uniform mod 3 → 22 elements `≡ 1 mod 3`, all odd. Two of them in one `(mod 11, mod 4)` slot differ by a nonzero multiple of 132, and `gcd(132t, 660) = 132` for `t = 1..4`, a P-class; so at most one per slot. `Q_10` offers exactly **18** slots `< 22`. ✓

**Size 12 (six-pair matching).** `|Q| = 55` odd, so `Φ_2, Φ_4 ∤ Q` (each equals 2 at 1), hence both divide P and P is uniform mod 4, three per class. PC classes 1 and 2 mod 4 are exactly `{33,253,473}`, `{198,418,638}`; their differences realise gcds 55, 165, 220 (indeed the full forced class set is `{3,4,5,10,11,15,22,30,33,55,66,165,220}`; the author's relaxation `G_12 = G_A ∪ {55,165,220}` is valid and weaker). Under `G_12`: class 0 mod 11 of the Q-screen is `{0} ∪ L`, `L = {44,110,264,374,594,627}`; class 3 is `{14} ∪ R`, `R = {47,80,300,410,564,630}`; anchors 0 and 14 are the only anchors in these classes. `11 | 55`, `11 ∤ 12` → Q uniform mod 11, five per class → four from L and four from R. Exhaustively, **all 225 choices of (4 of L) × (4 of R) contain a cross pair with gcd in `G_12`**; the unique perfect forbidden matching is the author's `(44,300),(110,47),(264,80),(374,630),(594,410),(627,564)` (gcds 4,3,4,4,4,3). Pigeonhole over six disjoint pairs with eight endpoints is correct. ✓ (Under the full forced class set the classes collapse to `{0,110}` and `{14,564}`, so the contradiction is immediate; without class 55 the 4×4 check still finds zero admissible selections.)

**Size 22 (outside-class shortage).** P uniform mod 11, two per class; PC class 1 is exactly `{188,243}`, forced, `gcd(55)`. `|Q| = 30` → uniform mod 5 (6 per class) and mod 3 (10 per class, so 20 tails `≢ 1 mod 3`). Under `G_22 = G_A ∪ {55}` (108 residues) **no** tail `≡ 1 mod 3` lies in mod-5 classes 0 or 4, so those classes contribute 12 tails all `≢ 1 mod 3`; outside them the only tails `≢ 1 mod 3` are `{47, 627}`; `12 + 2 = 14 < 20`. ✓ (Sensitivity: without class 55 the outside list grows to eight and the count would reach exactly 20, so the forced pair {188,243} is load-bearing and is correctly forced.)

**Independent exhaustive confirmation (pure directness).** My control enumerates every `P` with `A ⊆ P ⊆ PC` meeting only the prime-balance caps (no pairwise gcd filter) and runs an MRV exact-cover search for `Q ⊇ Y` with `P ⊕ Q = Z_660`: sizes 4 (1 set), 5 (38), 6 (703) with **no caps at all**, 10 (4), 12 (4), 22 (4): **zero tilings**, no node cap hit, at most 44 search nodes per instance. Sizes 11/15/20/30/33 admit no cap-compatible P (capacity). Thus the complete cardinality partition `{4,5,6} ∪ {10,12,22} ∪ {11} ∪ {15,20,30} ∪ {33}` is exhausted and **order 660 is excluded** by a route that uses only premises 1–3 and directness, independently of the author's residue arguments and of the seven-head predecessor.

**MINOR (b)-1, presentational.** §4 writes that Q "must avoid classes 55 and 132 as well as G_A" before the "no residue 4 mod 6" claim; that claim already holds under `G_A` alone (control `sensitivity_4mod6_without_132 = 0`). Class 132 is genuinely needed only for the slot-exclusivity step. Harmless.
**MINOR (b)-2, presentational.** §1–§2 of the candidate present a conditional floor `n ≥ 1980`; it is explicitly conditional there, out of this wave's scope, and not adopted here.

Author checker (input 4): read only; every assertion in it corresponds to a fact my code reproduced independently (42; 6; 2; `[188,243]`; `[132,407]`, `[264,539]`; 55/132; no `4 mod 6`; 18 slots; `f1/f2`; `{55,165,220}`; `L/R`; the six matching gcds; 188/243 → 55; empty 1-mod-3 in classes 0/4; `[47,627]`). Its execution output is not used as evidence.

## (c) Universal 55-tail branch — independent rederivation for all k ≥ 2

`n = 165m`, `m = 2^k`, `|Q| = 55`, `|P| = 3m`.

1. **Uniform 2-power fibres.** For `1 ≤ j ≤ k`, `Φ_{2^j}(1) = 2 ∤ 55`, so `Φ_{2^j} | P(x)` for all j; the product is `1 + x + … + x^{m−1}`, so P has exactly `3m/m = 3` elements in every class mod m. ✓
2. **Rectangle.** `G_Y = {1,2,6,12}` for every k ≥ 2 (gcd(14,n)=2, gcd(6,n)=6, gcd(12,n)=12 need only `4 | n`). For `x ≡ 1 mod 4`: `v_2(x−3) = v_2(x−11) = 1`, so `gcd(x−3,n) = 2·gcd(x−3,165) ∉ {2,6}` forces `5 | x−3` or `11 | x−3`, likewise for `x−11`; since `(x−3)−(x−11) = 8` is prime to 5 and 11, `(x mod 5, x mod 11) ∈ {(3,0),(1,3)}`. In case (1,3), `x` and `x−8` are odd and prime to 5 and 11, so avoiding gcd 1 forces `3 | x` and `3 | x−8`, impossible; case (3,0) passes all four anchors (gcds in {11,33},{10,30},{5,15},{22,66}) with `x mod 3` free. For `x ≡ 2 mod 4` the same with `v_2(x) = v_2(x−8) = 1` gives `{(0,8),(3,0)}`; (0,8) forces `3 | x−3` and `3 | x−11`, impossible; (3,0) passes. Hence in every class `r ≡ 1, 2 mod 4` the only admissible residues are the CRT lifts of `x mod 165 ∈ {33, 88, 143}` — exactly three — and all are forced. Since `v_2(x−a) ∈ {0,1}` is determined by `x mod 4` whenever `x ≢ a mod 4`, this is a finite statement over `{1,2} × Z_165`, which my control enumerates exhaustively (both survivor lists are `[33,88,143]`; both excluded CRT cases fail as stated). ✓
3. **Forced classes.** `x ≡ (1, 143)`: `x−8` odd, `≡ 135 mod 165` → gcd 15. `x ≡ (1, 33)`: `x−3 ≡ −2 mod m` (v_2 = 1 as m ≥ 4), `≡ 30 mod 165` → gcd 30. `x ≡ (1,33)`, `y ≡ (2,88)`: `x−y` odd, `≡ −55 mod 165` → gcd 55. So `H = {3,5,11,15,30,55}` are P-classes for every k ≥ 2. ✓
4. **Lifting.** If `gcd(d,660) ∈ H` then `v_2(d) ≤ 1`, so `gcd(d,n) = gcd(d,165)·2^{v_2(d)} = gcd(d,660)`. Hence the projected Q must pass the H-screen against Y inside `Z_660`. ✓
5. **Injectivity.** For `2 ≤ a ≤ k−1`, heads `(1,33)` and `(1+2^a, 33)` (note `1+2^a ≡ 1 mod 4`) differ by a multiple of 165 with 2-adic valuation exactly a, gcd `165·2^a`. Two distinct Q-elements congruent mod 660 differ by `660t`, `0 < |t| < 2^{k−2}`, gcd `165·2^{2+v_2(t)}` with `2 ≤ 2+v_2(t) ≤ k−1` — a P-class. So `Q → Z_660` is injective (`k = 2` trivially), image a 55-set containing Y. ✓
6. **Shortage.** `11 | 55`, `11 ∤ 3m` → Q uniform mod 11, five per class, preserved by projection. Independently recomputed H-screen at 660, class 7 mod 11: exactly `{7, 73, 337, 601}` — one anchor plus three non-anchors — for the required five. ✓ (Classes 1 and 2 are also short at four; `H` without any one of 15, 30, 55 would leave class 7 with 8, 6, 8 candidates, so all three forced classes are load-bearing and each was proved above for all k.)

Finite controls for k = 2..9 (n up to 84480) confirm the forced rectangle in every `r ≡ 1,2 mod 4` class, the 15/30/55 witnesses, every injectivity gcd `165·2^a`, the lifting identity, and the class-7 list. At k = 2 the forced heads are the size-12 heads of (b), and at k = 3 the twelve forced heads in classes 1,2,5,6 mod 8 agree with the adopted order-1320 disposition's "four classes each have exactly three screened candidates". The (12,55) case at 660 is therefore excluded by three mutually independent routes (matching, 55-tail, exact cover).

**MINOR (c)-1, presentational.** §3's lifting sentence ("if a difference has gcd in H modulo 660, it has the same gcd with n") is correct but the needed direction (660-class in H ⇒ n-class in H) deserves to be stated explicitly since the screen is applied to projected residues. No mathematical change.

## Controls: what actually ran (clock/hash receipts)

All files below live only in this review directory; nothing imports author or prior reviewer code. Exact Python integers (`math.gcd`, bit masks); Python 3.14.3.

| Artifact | SHA-256 | bytes/LF | Status |
|---|---|---|---|
| `reviewer-f128-exact-control-v1.py` | `9b1a2958e416f5e5ff70a66fad009b6d2d22937bf67de89f5f131c17da98dcb8` | 16215/358 | ran 20:37:36→20:38:56 PDT, exit 0, but **its exact-cover section was vacuous**: my `enumerate_P` compared non-anchor picks against the full `\|P\|`, so 0 P-sets were enumerated (self-detected from `admissible_P = 0` at sizes 10/12/22). All other sections (screens, residue facts, divisibility, rectangle, family k = 2..9) are unaffected and agree with v4. Kept as a record. |
| `reviewer-f128-exact-control-result-v1.json` | `236b81f5b2e49b3a5257be2fb62ee18c453d7ba54e3091f071b94e1432473500` | 7334/606 | output of v1 (vacuous exact-cover section). |
| `reviewer-f128-exact-control-v2.py` | `a456845790421901cb819859208d19aafab743b4a76283c88d2e16a35b2598de` | 17483/380 | enumeration fixed; run 20:42:05→20:42:29 PDT aborted by its own assertion: the lowest-element exact cover hit the 20M-node cap at sizes 10 and 12 (no tiling found); result file empty (`e3b0c442…`). |
| `reviewer-f128-mrv-probe-v1.py` | `9836dc275f28a76f002c510faa876af2415a5eebc48d02deb0f3349fe4a80bd6` | 2769/79 | probe at 20:43:43 PDT: MRV pure-directness cover excludes the three pairwise-admissible P-sets in 16/22/12 nodes; interval positive and {0,1,3} negative pass. (A Sands-pruned variant in v2 also excluded them in 32/1 nodes.) |
| `reviewer-f128-exact-control-v3.py` | `bcf6083368dc5e23d46baa8970390ca7686cf8a2ded18d293ae21fea2b5ddf2d` | 17057/369 | MRV cover integrated; run 20:45:31→20:45:32 PDT aborted by an over-strict reviewer assertion (it demanded a positive admissible count at size 4 under the mod-4 cap, which is rightly zero because anchors 0, 8 share a class while `\|Q\| = 165` is odd); result file empty. |
| **`reviewer-f128-exact-control-v4.py`** | **`ec5b1afc4d2bdeab1fd68a0f63c03bb51d897281b58b8682aa2527960d71c3f6`** | 17353/372 | **authoritative run** 20:45:54→20:45:55 PDT, exit 0, `ALL ASSERTIONS PASSED`, 1.3 s; sizes 4–6 run with no caps. Self-reported script hash matches. |
| **`reviewer-f128-exact-control-result-v4.json`** | **`06853d48f6ed5fa686696333f85617bffa1257e442b137247b6cf4c583cc8d61`** | 8800/669 | full machine record of every count quoted above. |

Positive/negative cases exercised in v4 (`D_primitive_controls`): direct-tiling checker accepts `{0..9} ⊕ 10·Z_66` and rejects a one-element corruption; Sands checker accepts that tiling and `{0,3} ⊕ {0,1,2} = Z_6`, rejects `({0,1},{0,1})` in `Z_4`; MRV cover finds `Q` for the interval tile (66 nodes) and for `{0..4}+{0,10}` with forced `{0,5,20}` (64 nodes), returns none for overlapping forced translates, for `{0,1,3}` in `Z_12, Z_30, Z_60`, and agrees with brute-force enumeration on seven small `(n,P)` cases; `enumerate_P` returns the four expected size-10 sets (including `A ∪ {132,264,275,396,407,539}`) and nothing at size 11.

## Dependencies and limits

* (a) depends only on premises 1 and 3 and the four anchor differences; (b) depends on premises 1–3 (the author's written route additionally on the seven-head `|P| ≥ 7`, hand-verified; my exhaustive route does not); (c) depends on premises 1–3 only.
* The premises themselves (same-code border tiling, prime balance, Sands necessary direction) are taken from the adopted order-1320 disposition and were not re-proved here beyond the sketch in that disposition.
* Nothing here is a human, independent-model-family, formal/kernel or novelty clearance; the classical Sands/border literature was not searched (web search prohibited). The original all-order finite UD factor-completion problem remains open; no floor, no order other than 660, and no border branch other than `(3·2^k, 55)` at `165·2^k` is excluded by this review.

**END OF f128 REVIEW v1.**
