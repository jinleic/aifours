# review-v1 — ReviewF900TuscanT13 — wave `f900-tuscan13-four-full-pattern-class-exclusion-critical-review`

Critical disjoint reconstruction of the f889 (packet S1) Part B claim that the actual T13 full-count pattern `(4,0,0,0,0)` is empty under its stated hypotheses, plus a FATAL/MAJOR check of Part A.
Reviewer: ReviewF900TuscanT13 (not the author). Science cutoff 2026-10-31T21:23:27Z.
Clocks (bash `date -u`, metadata only): 2026-10-31T11:35:58Z before the PREBODY ACK; 11:56:09Z after the complete packet read and hand work; 12:01:48Z immediately before this file's write.

**Citation convention.** `S1|N` = logical line N of S1 (the f889 candidate) exactly as printed in the packet prefix `S1|N|`; `S2|N` … `S5|N` likewise. In THIS packet: S2 = f853 candidate, S3 = singleton-transport disposition, S4 = overlap-budget / joint-cut disposition, S5 = synchronized-third-cut disposition. "LF" always means this logical line unless "packet LF" is written.

---

## 1. Verdict

**FATAL 0 / MAJOR 0 / MINOR 6.**

* **Part B (S1|286–410): accepted at its stated boundary** as a conditional exclusion: under H1–H4 and named imports I1–I2 (S1|30–47) the actual `(4,0,0,0,0)` T13 branch is empty. I reconstructed from scratch the cell numbering by the full run of `F` (S1|61–75), Lemma 1 (S1|288–296), the Lemma 2 class table (S1|300–329), Lemmas 3–4 (S1|333–340), Theorem 1 (S1|342–360), Theorem 2 (S1|362–392) and the Corollary (S1|394–400), and I found no step that fails.
* **Part B depends on Part A.** The grammar, the twelve-square tables and the count (5) (A1–A3, S1|79–163) are load-bearing for Part B (see MINOR M3). I reconstructed them too and accept them. A4–A7 (S1|165–272) are not used by Part B; I also reconstructed them: no FATAL/MAJOR (one MINOR, M5). A8 (S1|274–284) is a verdict statement; consistent.
* **Requested omission checks (§5):** no square matching, sign pattern, G/H choice or row assignment is omitted; the class table rests on no unproved orientation convention.
* **Boundary:** I1/I2 are imports whose own proofs are not in the packet. I checked that S1's wording of I1/I2 is consistent with S3|13, S4|17–30 and S5|7–31 at statement level only (§2, §8).
* No family, human, formal or kernel acceptance, no novelty or priority claim. Parent disposition is separate.

The six MINOR findings (§3) are documentation/wording defects. None changes a conclusion.

---

## 2. Exact accepted statement and import boundary

**Accepted statement (S1|396–400 restated).** Let `𝒯` be an actual T2(11) on an 11-set `X` (eleven rows, each a permutation of `X`; each ordered pair at most once at row-distance 1 and at most once at row-distance 2). Let `Σ₁≠Σ₂` be odd-position six-supports, each the odd-position support of three rows. Assume
* H1: the missing linear distance-two set `M` equals the last-to-first closing set `C`;
* H3: the synchronized value of `(Σ₁,Σ₂)` is `T=13`;
* H4: the five residual cycles have full-cell-count pattern `(4,0,0,0,0)`;
* and the conditional imports I1, I2 exactly as worded in S1|40–45.

Then a contradiction follows, i.e. no such `𝒯, Σ₁, Σ₂` exists. H5 and I4 are not used by Part B. H2 is used only through the existence of the six alternating cycles and five residual cycles.

**Import boundary (named, not re-proved).** Used only in the following form:
* **I1** (S1|40): the eleven `∞`-augmented rows are directed Hamilton 12-cycles on `X∪{∞}`; their adjacency arcs partition all 132 directed arcs; under H1 their directed squares (`i→i+2` along the cycle) partition all 132 ordered pairs. Supporting text: S3|13, S5|7–9.
* **I2** (S1|41–45): cells `I,J,K,L` of size 3 with opposite pairs `{I,L},{J,K}`; six cycles alternate across `Σ₁` or `Σ₂`, five residual cycles remain; under `T=13` each cell has, over the five residual cycles, exactly one full (length-3) run and four "double + singleton" layouts, no three-singleton layout; every residual cycle is regular (exactly one join per opposite pair, both endpoints in nontrivial runs). Supporting text: S4|17–30 (table `T=13: 1,4,0`), S3|13 ("In T13 all five are regular … full-cell counts are 0,2,4"), S5|11–13, S5|19–21 (T=13: every residual cycle has exactly one I–L join and one J–K join), S5|28 (T=13 patterns `(4,0,0,0,0)` or `(2,2,0,0,0)`).

Everything else used is derived inside S1 and was reconstructed by me (§4): the two cut facts and the partitions (P1), (P2), the singleton law T, the cell-word grammar, the square tables, the count `g∈{1,3}`, Lemmas 1–4, Theorems 1–2.

**Not asserted:** anything about H5, I4, `(2,2,0,0,0)`, `T=14`, `M≠C`, fewer than two tripled supports, existence of arrays, or the truth of the imports' own proofs.

---

## 3. Findings (all MINOR; presentation/documentation; no failing mathematical step)

**M1 — private source IDs in citations (S1|40, 41, 46, 284, 402; also every "S1 (n)" / "S1 §n" in Part A).**
Quoted: S1|40 "**I1** (S2:13; S1 §1 I1)."; S1|41 "**I2** (S2:13; S3:17–30; S1 §1 I2)."; S1|46 "…counting route of S2:15."; S1|284 "S1 never asserted nonemptiness (S1:212)"; S1|402 "By S2:13 (full counts `0,2,4`) and S3:30 (`G=4T−48=4` full runs)".
Failing step: the candidate never defines S1/S2/S3. They are the author's own three-source packet IDs: S1 = f853 candidate (221 LF), S2 = singleton-transport disposition (51 LF), S3 = overlap-budget disposition (36 LF) (confirmed by S1|485 "S1 complete 221 lines, S2 complete 51 lines, S3 complete 36 lines"). In the f900 packet these are S2, S3, S4 and `S1` is f889 itself, so the citations resolve literally to the wrong lines (S2|13 here is f853's I3 import line, not the I1 source). Correct resolution: S3|13 (I1, "all five regular", "full-cell counts 0,2,4"), S4|17–30 (I2), S3|15 (counting route), S2|212 ("do not prove that either alternative is nonempty"), S3|13 and S4|30 (`G=4T−48`). I checked all resolved targets; they support what S1 uses them for. The third-cut disposition S5 was not in the author's packet (S1|459); I compared I2 against S5|11–31 and found it consistent. No effect on validity.

**M2 — S1|374 wording.**
Quoted: "If both are pure, they fill two classes, and `R_W ∪ {C_U}` must be the third class. So `R_W` lies in one class and `W` is pure. Then at most `U` is mixed, contradicting Lemma 3's "0 or 2"."
Failing step: read literally this says the branch "R and S pure" is contradictory, which would undercut S1|376 "Hence all four rows are pure". The step actually valid and used: `R,S,W` pure ⇒ at most one mixed row ⇒ (Lemma 3: 0 or 2) ⇒ zero ⇒ `U` pure. Wording only.

**M3 — scope sentences understate Part B's dependence on Part A and on both pairs (S1|22, S1|344, S1|368, S1|396).**
Quoted: S1|22 "**What Part B does not use:** … or the second opposite pair."; S1|344 "No sign pattern, gap choice, H5 or other pair is used."; S1|396 "By A3, every configuration has `g∈{1,3}`, and Theorems 1–2 refute both alternatives for any one pair."
Failing step: Part B's square tables are those of A2 (S1|126–128), which come from the grammar of A1. That grammar rests on the singleton law T for all four cells (both opposite pairs) and on regularity for both pairs; e.g. the square `p0⁰→p1⁰` is centred at the other pair's singleton (`q1⁰` in `W_G`, S1|134). What is unused is the second pair's square equations and class bookkeeping, not the second pair's structure. The Corollary cites only A3. Part B's validity therefore requires A1–A2 as well; I verified them (§4.4–4.6).

**M4 — two compressed justifications for Lemma 3's premise (S1|51–54, S1|225, S1|333).**
Quoted: S1|333 "In each of `A` and `B`, `δ` is the double of exactly one zero-full row, and `α,β,γ` are the doubles of the other three (§0)."; S1|54 "Hence (a) no alternating cycle has an internal-cell adjacency arc, and (b) …" after the "two cut facts" S1|51–52.
Failing steps: (i) (a) needs "each of `I,J,K,L` lies on one side of each cut" (true by definition of the cells), which is not among the two listed cut facts (they list only "opposite cells lie on different sides" and "arcs cross, squares do not"). (ii) The bijection between the four zero-full rows and `{α,β,γ,δ}` needs: a zero-full row has exactly one internal arc of `V` (its double); distinct rows have distinct such arcs and none is `0→1` or `1→2` (F's run) by I1 arc uniqueness; four distinct elements of a 4-set. §0/A6 only say "By §0 and `F`'s run". Both points are immediate; reconstructed in §4.2–4.3.

**M5 — incomplete case split in A4 (S1|182; same gap in S2|115). Not load-bearing for Part B.**
Quoted: "No other partition exists, because a 3-cycle cannot be split into within-cycle pairs alone."
Failing step: this excludes only zero reciprocal pairs. Exactly two reciprocal pairs is not addressed (it forces the remaining two arcs, one from each 3-cycle, to be the third reciprocal pair, i.e. case (a)). I enumerated: reciprocal count `r∈{1,3}`, four partitions. Conclusion (7) and the omitted-pair maps (S1|184–185) are correct.

**M6 — "all 16 completions" vs an 8-row table (S1|414–425). Not load-bearing.**
Quoted: "**(i) `g=1` via S1's own tables (A6), `n_+∈{1,2}`, all 16 completions.**"
Failing step: the table lists 8 rows (the 8 admissible `(e_X^A,e_X^B,n_+)`), each row's reason being claimed to dispose of both bijections of the other two rows (16 = 8×2); this is not stated. I recomputed every row: each collision lies in the row(s) pinned by the tables (rows 1, 4, 8: independent of the completion; rows 2, 3, 6, 7: the unique-sign row; row 5: both sub-completions displayed). All correct.

---

## 4. Reconstruction of every load-bearing step I accept

Notation as S1: `ℓ`, `α=1→0, β=2→1, γ=0→2, δ=2→0` with (tail, head, third): `α(1,0,2) β(2,1,0) γ(0,2,1) δ(2,0,1)`; `F` the four-full row; `A→B` the join direction of `F` for the fixed opposite pair; roles `v⁻→v⁺` (double, in cycle order) and `v⁰` (singleton).

### 4.1 Imports as used — see §2.

### 4.2 Cut facts and partitions (S1|49–59)
For `Σ∈{Σ₁,Σ₂}`, a row with odd-position support `Σ` becomes the 12-cycle `x₁…x₁₁∞`. Positions 1,3,…,11 hold `Σ`; positions 2,…,10 hold `X∖Σ`; position 12 holds `∞∉Σ`. So its adjacency arcs cross the cut `(Σ, Σᶜ)` and its squares (`i→i+2`, including `x₁₀→∞`, `x₁₁→x₁`, `∞→x₂`) stay on one side. Cells: `I,J⊂Σ₁`, `K,L⊂Σ₁ᶜ`, `I,K⊂Σ₂`, `J,L⊂Σ₂ᶜ`. Hence every cell is on one side of both cuts, so internal-cell arcs never cross: (a) no alternating cycle has an internal-cell arc; and opposite cells (`I,L`) and (`J,K`) are separated by both cuts, so (b) no alternating cycle has a square between opposite cells. (`∞∈L` is an ordinary vertex: it lies on the `Σᶜ` side in every alternating cycle and takes part in the I1 partitions, S1|59.) With I1 and I2 (the five other cycles are the residual ones):
* **(P1)** each of the 18 directed pairs between opposite cells `A,B` (9 in each direction) is a square of exactly one residual cycle;
* **(P2)** each directed internal arc of a cell is an arc of exactly one residual cycle. (Only "at most one" is needed below.)

### 4.3 `F`, labels, and the premise of Lemma 3 (S1|61–75, S1|225)
`T=13` gives exactly one full run per cell over the five residual cycles; `(4,0,0,0,0)` puts all four in one cycle `F` and none in the other four ("zero-full rows"), so each cell of a zero-full row is one double + one singleton. `F` has four runs of three; its four inter-run arcs lie in cyclic run order; regularity gives exactly one join per opposite pair, which forces the cyclic order `A,B,Y,Z` (arcs `A→B` join, `B→Y`, `Y→Z` join, `Z→A`; if an opposite pair were non-adjacent in the run order, `F` would have no join for it). `F = a₀a₁a₂ b₀b₁b₂ y₀y₁y₂ z₀z₁z₂` with `ℓ(v_i)=i`; its only A–B squares are `a₁→b₀`, `a₂→b₁` (positions 2→4, 3→5), and it has none `B→A` (S1|130).
Each cell has six directed internal arcs: `0→1, 1→2` (F's run) and `α,β,γ,δ`. A zero-full row has exactly one internal arc of `V` (its double). Distinct rows have distinct arcs and none uses `0→1` or `1→2` (P2). Four rows, four available arcs ⇒ **bijection** between the four zero-full rows and `{α,β,γ,δ}` in each cell. The bijections in `A` and `B` are independent (rows are the same physical cycles in both cells).

### 4.4 Singleton law T (A1, S1|79–89)
Fix `{A,B}`, other pair `{Y,Z}`.
1. By (P1) the 18 directed A–B pairs are squares `u→m→w` of residual cycles, once each.
2. A residual cycle has a unique A–B join `x→y` (I2) with nontrivial runs `x′→x` (in A), `y→y′` (in B). A square between A and B with middle `m∈A∪B` contains an A–B adjacency arc, i.e. the join; so it is `(x′,y)` or `(x,y′)`: exactly 2 per cycle, 10 in total.
3. The other 8 squares have `m∈Y∪Z` with neighbours `u∈A`, `w∈B` (or reverse), so `m` is a singleton run.
4. By I2, `Y` and `Z` have 4+4=8 singleton runs, each the middle of exactly one square. `18 ≤ 10+8`, equality, so every singleton run of `Y∪Z` has one neighbour in A and one in B. By symmetry every singleton run of any cell has one neighbour in each cell of the other pair. ∎ (uses only P1 and I2)

### 4.5 Grammar (A1, S1|91–118)
Zero-full row, joins `p0→p1`, `q0→q1` (names per row). Join endpoints are doubles, so the cycle is `p0⁻p0⁺p1⁻p1⁺`, gap `G`, `q0⁻q0⁺q1⁻q1⁺`, gap `H`, with the four singletons filling `G∪H` (8+4=12). Law T: a `p`-singleton has neighbours in `q0` and `q1`; a `q`-singleton in `p0` and `p1`.
* `|G|=1` (or `|H|=1`): the singleton's neighbours are `p1⁺,q0⁻` (or `q1⁺,p0⁻`): cells of different pairs ✗. So `|G|∈{0,2,4}`.
* `|G|=4`: first singleton follows `p1⁺` ⇒ a `q`-singleton ⇒ next is `p0⁰`; `p0⁰`'s next is a `q`-singleton, whose next is `p1⁰`; `p1⁰` precedes `q0⁻` ⇒ third is `q1⁰`, first `q0⁰`. `G=q0⁰p0⁰q1⁰p1⁰`, `H=∅`.
* `|G|=0`: mirror: `H=p0⁰q0⁰p1⁰q1⁰`, `G=∅`.
* `|G|=2`: first follows `p1⁺` ⇒ `q`-singleton ⇒ next is `p0⁰`; `p0⁰` precedes `q0⁻` ⇒ first is `q1⁰`: `G=q1⁰p0⁰`. `H` starts after `q1⁺` with the remaining `p`-singleton `p1⁰`, then `q0⁰` (precedes `p0⁻`): `H=p1⁰q0⁰`.
The three words (S1|112–114) are `W_G, W_H, W_S` ("grouped at G / grouped at H / split"). Grouped/split is a property of the physical row (exchanging the pairs exchanges G and H). The only opposite-cell adjacency arcs are the two joins; the empty-gap arc joins non-opposite cells (S1|116).

### 4.6 Square tables (A2, S1|120–148)
Positions 1–12; squares `i→i+2` cyclically; I recomputed all 36:
* `W_G`: 1 p0⁻,2 p0⁺,3 p1⁻,4 p1⁺,5 q0⁰,6 p0⁰,7 q1⁰,8 p1⁰,9 q0⁻,10 q0⁺,11 q1⁻,12 q1⁺. Squares: p0⁻→p1⁻, p0⁺→p1⁺, p1⁻→q0⁰, p1⁺→p0⁰, q0⁰→q1⁰, p0⁰→p1⁰, q1⁰→q0⁻, p1⁰→q0⁺, q0⁻→q1⁻, q0⁺→q1⁺, q1⁻→p0⁻, q1⁺→p0⁺.
* `W_H`: 1 p0⁻,2 p0⁺,3 p1⁻,4 p1⁺,5 q0⁻,6 q0⁺,7 q1⁻,8 q1⁺,9 p0⁰,10 q0⁰,11 p1⁰,12 q1⁰. Squares: p0⁻→p1⁻, p0⁺→p1⁺, p1⁻→q0⁻, p1⁺→q0⁺, q0⁻→q1⁻, q0⁺→q1⁺, q1⁻→p0⁰, q1⁺→q0⁰, p0⁰→p1⁰, q0⁰→q1⁰, p1⁰→p0⁻, q1⁰→p0⁺.
* `W_S`: 1 p0⁻,2 p0⁺,3 p1⁻,4 p1⁺,5 q1⁰,6 p0⁰,7 q0⁻,8 q0⁺,9 q1⁻,10 q1⁺,11 p1⁰,12 q0⁰. Squares: p0⁻→p1⁻, p0⁺→p1⁺, p1⁻→q1⁰, p1⁺→p0⁰, q1⁰→q0⁻, p0⁰→q0⁺, q0⁻→q1⁻, q0⁺→q1⁺, q1⁻→p1⁰, q1⁺→q0⁰, p1⁰→p0⁻, q0⁰→p0⁺.
These equal the table S1|126–128. Hence, for the pair of interest `p={A,B}`:
* grouped row, join `p0→p1`: `P={(p0⁻,p1⁻),(p0⁺,p1⁺),(p0⁰,p1⁰)}` forward and one reverse square `C=(p1⁺,p0⁰)` at G / `(p1⁰,p0⁻)` at H;
* split row sign `+` (join `A→B`): `L^AB={(a⁻,b⁻),(a⁺,b⁺)}`, `R^BA={(b⁺,a⁰),(b⁰,a⁻)}`; sign `−` (join `B→A`): `L^AB={(a⁺,b⁰),(a⁰,b⁻)}`, `R^BA={(b⁻,a⁻),(b⁺,a⁺)}`.
The same description holds when `{A,B}` plays the role `q` (with G, H exchanged). Each row has exactly 4 A–B squares; `2+4·4=18` ✓. The role pairs `(−,+)` and `(+,−)` never occur as squares (they are exactly the omitted pairs `L(−)` omits `(a⁻,b⁺)` and `R(+)` omits `(b⁻,a⁺)`).

### 4.7 Count (A3, S1|150–163)
`g` = number of grouped zero-full rows, `n` those with `F`'s join direction. A→B squares: `F` gives 2; a grouped row with `F`'s direction gives 3 (`P`), the other grouped rows 1 (`C`), split rows 2: `9 = 2+3n+(g−n)+2(4−g) = 10+2n−g`, so `g=2n+1`, `0≤n≤g≤4` ⇒ `(g,n)∈{(1,0),(3,1)}`. `g` is a property of the physical rows (common to both pairs). ✓

### 4.8 Lemma 1 (S1|288–296)
For a double `e` with tail `t`: `α,β,γ` have head `t−1`, third `t+1`; `δ` has head `t+1`, third `t−1`. Check: `α(1;0,2)`, `β(2;1,0)`, `γ(0;2,1)` ((head,third)=(t−1,t+1) mod 3 ✓), `δ(2;0,1)` ((t+1,t−1)=(0,1) ✓). With `ε=+1` for `α,β,γ`, `ε=−1` for `δ`: `ℓ(v⁻)=t`, `ℓ(v⁺)=t−ε`, `ℓ(v⁰)=t+ε`. The arcs `0→1`, `1→2` belong to `F` (4.3). ✓

### 4.9 Lemma 2 (class table, S1|300–329)
Class of a directed A–B pair = `ℓ(A-endpoint)−ℓ(B-endpoint)` in both directions (a fixed definition; each class has 3 pairs forming a perfect matching in each direction). `κ=t_A−t_B`. For role pair `(x,y)` (A-role, B-role): `cl=ℓ(a^x)−ℓ(b^y)`:

| role pair | occurs in | class | pure `ε_A=ε_B=ε` | mixed `ε_B=−ε_A`, `ε:=ε_A` |
|---|---|---|---|---|
| (−,−) | P, R(−), L(+) | κ | κ | κ |
| (+,+) | P, R(−), L(+) | κ−ε_A+ε_B | κ | κ+ε |
| (0,0) | P | κ+ε_A−ε_B | κ | κ−ε |
| (0,+) | R(+) [b⁺→a⁰]; C^BA at G | κ+ε_A+ε_B | κ−ε | κ |
| (−,0) | R(+) [b⁰→a⁻]; C^BA at H | κ−ε_B | κ−ε | κ+ε |
| (+,0) | L(−) [a⁺→b⁰]; C^AB at G | κ−ε_A−ε_B | κ+ε | κ |
| (0,−) | L(−) [a⁰→b⁻]; C^AB at H | κ+ε_A | κ+ε | κ+ε |

(uses `2ε≡−ε`.) I recomputed every entry symbolically and numerically (§7 HC-A). Consequences (all verified from the table and 4.6):
* **pure row:** `P` = one full class `κ`; `R(−), L(+)` ⊂ class `κ`; `R(+)` ⊂ class `κ−ε`; `L(−)` ⊂ class `κ+ε`; `C^BA` ⊂ `κ−ε`, `C^AB` ⊂ `κ+ε` for **both** gaps;
* **mixed row:** `P` meets each class once; each of `R(±), L(±)` meets two distinct classes once each (`R(−),L(+)`: `κ`, `κ+ε`; `R(+)`, `L(−)`: `κ`, `κ+ε`). (`C` classes in a mixed row depend on the gap, κ at G and κ+ε at H; they are never used, see §5.3.)
* `F_AB={[1,0],[2,1]}_{AB}` ⊂ class 1; third pair of class 1 is `[0,2]_{AB}`.

### 4.10 Lemmas 3–4 (S1|333–340)
**Lemma 3.** By 4.3 each of `α,β,γ,δ` is the double of exactly one zero-full row in each of `A`, `B`. Let `r_A`, `r_B` be the rows with `δ` in `A`, `B`. If `r_A=r_B` that row is pure with `ε=−1`, `κ=2−2=0` (the "δ-row") and the other three are pure with `ε=+1`. If `r_A≠r_B`, exactly those two rows are mixed and the other two are pure with `ε=+1`. So exactly one of: (one δ-row, 0 mixed) or (exactly 2 mixed). ✓
**Lemma 4.** Three pure `ε=+1` rows have `A`-arcs `α,β,γ` (tails `1,2,0`) and `B`-arcs `α,β,γ` in some order, so `t_B=σ(t_A)` for a permutation `σ` of `ℤ/3`; the six permutations are `x↦x+c`, `x↦−x+c`; `κ=t_A−σ(t_A)` is constant `−c` or `2x−c` (a bijection). ✓

### 4.11 Theorem 1, `g=1` (S1|342–360)
`J_BA=P_X+R_{W₁}+R_{W₂}+R_{W₃}` (all 9 `B→A` pairs once; `X` opposes `F`). Per class: pure `P` contributes 3 to one class; mixed `P` 1 to each; pure `R` 2 to one class; mixed `R` 1 to each of two classes; each class must total 3. Mixed rows: 0 or 2 (Lemma 3).
* 0 mixed: classes `≠c_X` receive only 2's: `3=even` ✗.
* 2 mixed, `X` mixed (+ one mixed `W`): `3=1+m_c+2k_c`, `m_c∈{0,1}` ⇒ `m_c=0` for all `c`, but the mixed `W` meets two classes ✗.
* 2 mixed, `X` pure: `c_X` is full, so both mixed `R`'s avoid it and each meets exactly the other two classes once; `c≠c_X` gets `1+1+(0\text{ or }2)≠3` ✗. ∎
Valid for every sign pattern, both gap choices (no `C` is involved), no H5.

### 4.12 Theorem 2, `g=3` (S1|362–392)
`J_BA=P_R+P_S+R_W+C_U^{BA}`, `J_AB=F_AB+P_U+L_W+C_R^{AB}+C_S^{AB}` (A5; counts 9 and 9).
* **Step 1 (all rows pure; `B→A` only).** `R` pure, `S` mixed (or conversely): `P_R` fills a class, `P_S` meets it ⇒ repeated pair. Both mixed: `U,W` pure (Lemma 3); `P_R,P_S` leave exactly one pair per class, but pure `R_W` puts two in one class ✗. Both pure: `κ_R≠κ_S`, `R_W∪{C_U}` is the third class; so `R_W` is in one class ⇒ `W` pure; then `R,S,W` pure ⇒ at most `U` mixed ⇒ (0 or 2) none (cf. M2). So all four pure, one δ-row `D∈{U,R,S,W}` (`ε_D=−1`, `κ_D=0`), the other three `ε=+1`.
* **Step 2.** `B→A`: third class `κ*=R_W∪{C_U}`, `cl(C_U)=κ_U−ε_U=κ*`. `A→B`: `F_AB⊂` class 1, so `κ_U≠1`; `c′:=` the class `∉{1,κ_U}`; the four pairs `L_W∪{C_R,C_S}` are `[0,2]_{AB}` and class `c′`; `L_W` (pure `W`) is in one class ⇒ `L_W⊂c′`; hence `{cl(C_R),cl(C_S)}={κ_R+ε_R, κ_S+ε_S}={1,c′}`.
* **Step 3.** `D=W`: `U,R,S` have `ε=+1`, `κ_R≠κ_S` ⇒ (Lemma 4) pairwise distinct ⇒ `κ*=κ_U` but `cl(C_U)=κ_U−1≠κ_U` ✗. `D=U`: `cl(C_U)=0+1=1=κ*`; `R,S,W` distinct ⇒ `κ*=κ_W=1`, `{κ_R,κ_S}={0,2}`; `c′=2`; `{κ_R+1,κ_S+1}={1,0}≠{1,2}` ✗. `D=R` (and `S` symmetric): `cl(C_R)=0−1=2≠1` ⇒ `c′=2`, `cl(C_S)=κ_S+1=1` ⇒ `κ_S=0=κ_R`, contradicting `κ_R≠κ_S` ✗. ∎
Valid for either sign of `W` and either gap (after Step 1 all `C` are in pure rows), no H5.

### 4.13 Corollary (S1|394–400)
`g∈{1,3}` (4.7); for one chosen opposite pair Theorem 1 kills `g=1` and Theorem 2 kills `g=3`. Hence the stated branch is empty at the I1–I2 boundary. ✓ The "Reduction within the same imports" (S1|402): with I2's full counts `0,2,4` and `G=4T−48=4`, the only multisets are `(4,0,0,0,0)` and `(2,2,0,0,0)`; S5|28 agrees. Accepted as an import-level remark.

---

## 5. The requested omission checks

**5.1 Square matchings.** Every A–B square of every zero-full row has role pair among the seven listed (4.6, 4.9); `(−,+)` and `(+,−)` never occur. `F` contributes only `F_AB`. Per pair `2+4·4=18`. For `g=1`: `9=3+2·3` B→A; `9=2+1+6` A→B. For `g=3`: `9=3+3+2+1` and `9=2+3+2+1+1`. No further matching exists.
**5.2 Sign patterns.** Signs of split rows enter only through which of `R(±)`, `L(±)` occurs; for pure rows each of these lies in one class, for mixed rows each meets two distinct classes (4.9). The proofs of Theorems 1–2 hold for every sign pattern; Theorem 1's parity count was additionally enumerated at pair level over all patterns (§7 HC-C).
**5.3 G/H choices.** `C^BA`, `C^AB` of a pure row lie in a single class independent of the gap (`κ−ε`, `κ+ε`). In a mixed row `C` depends on the gap, but Theorem 2 uses `C` classes only after Step 1 has shown all rows pure, and Step 1 uses no `C` class. Theorem 1 uses no `C`. The coupling of gap choices between the two pairs is not needed.
**5.4 Row assignments.** Lemma 3 covers all pairings of `A`-arcs and `B`-arcs across rows (δ-row case and two-mixed case); Lemma 4 covers all pairings among the pure rows with `ε=+1`; Step 3 covers every position of the δ-row.
**5.5 Orientation conventions.** The labels `ℓ` come from `F`'s actual directed full run; the four arcs are defined from `ℓ`; `ε`, head and third are the explicit arithmetic of 4.8; `A→B` is `F`'s join direction; the class is a fixed definition; roles `⁻,⁺` are positions inside the double in cycle order; sign `±` of a split row is its join direction relative to `F`. The same rule applies to the second pair (`Y→Z`) if it is chosen. No unproved orientation convention enters.

---

## 6. Part A (S1|77–284): FATAL/MAJOR check

A1 (law T, grammar): reconstructed, 4.4–4.5, matches S1|79–118. A2 (tables): reconstructed, 4.6. A3: 4.7. A4 (S1|165–201): equations (6) are (J_BA, J_AB) as in 4.11/4.6; the six arcs of `K₃,₃` minus a matching, after relabelling `A` by `π_X^{-1}`, are two directed 3-cycles; two arcs form a matching iff in the same 3-cycle or reciprocal; partitions `r∈{1,3}` reciprocal pairs (4 partitions); omitted maps identity or transposition `(x z)` (S1|184–185 examples recomputed); multisets (8) from degree counts (`3=[a∈{a₁,a₂}]+[a=x]+3−#{i:t_i=a}`). A5 (S1|203–221): `δ_RS=π_R^{-1}π_S` fixed-point-free ⇒ 3-cycle; the third matching `π_Rδ²`; `C_U=(u,v)`, `v=π_R(δ²(u))`; multisets (11) by degree 2 after removing `P_U`. A6 (S1|223–259): the omitted-vertex table (S1|232–235) recomputed; all 4×2×8=64 distinctness checks recomputed: the surviving patterns equal S1|241–242 and, with `n_+∈{1,2}`, S1|248–251 (= S2|167–170); consequences 1–3 (S1|253–257) follow. A7 (S1|261–272): `C_U^{BA}=(B_U⁺,A_U⁰)`, `C_U^{DC}=(D_U⁰,C_U⁻)` (gap B-block→C-block), `W`'s omitted reverse pairs `(B_W⁰,A_W⁰),(D_W⁰,C_W⁰)`; (10) gives `A_U⁰=A_W⁰`, `D_U⁰=D_W⁰` (also `B_U⁺=B_W⁰`, `C_U⁻=C_W⁰`); the two doubles in `A` (and `D`) are distinct arcs on the same two vertices, hence reverses, and `{γ,δ}` is the only reversed pair among `α,β,γ,δ` (`α↔0→1`, `β↔1→2` are `F`'s); run-middle refinement (`a₁,d₁`, resp. `b₁,c₁`) ✓. A8: consistent with Part B (S1|284). **No FATAL, no MAJOR; MINOR M5 only (non-load-bearing).**

---

## 7. Hand cross-checks (fresh, reviewer-performed, by hand, NOTHING EXECUTED; labelled under owner addendum 2 / manifest methods line)

Data: `α(1,0,2) β(2,1,0) γ(0,2,1) δ(2,0,1)`; pairs `[ℓ(b),ℓ(a)]`; `P_X(e_A,e_B)={[t_B,t_A],[h_B,h_A],[z_B,z_A]}`, `R(+)(e_A,e_B)={[h_B,z_A],[z_B,t_A]}`, `R(−)(e_A,e_B)={[t_B,t_A],[h_B,h_A]}` (`t,h,z` = tail, head, third of the double in the indicated cell).

**HC-A (Lemma 2 numeric).** Pure sample: `A`-arc `α` (`a⁻,a⁺,a⁰=1,0,2`), `B`-arc `β` (`b⁻,b⁺,b⁰=2,1,0`), `κ=2`: classes `(−,−)=2, (+,+)=2, (0,0)=2, (0,+)=1, (−,0)=1, (+,0)=0, (0,−)=0` = `κ,κ,κ,κ−ε,κ−ε,κ+ε,κ+ε` ✓. A `δ,δ` pure row (`κ=0`, `ε=−1`): `(0,+)=1, (−,0)=1, (+,0)=2, (0,−)=2` ✓. Mixed sample: `A`-arc `α`, `B`-arc `δ` (`b⁻,b⁺,b⁰=2,0,1`), `κ=2`, `ε=+1`: `(−,−)=2, (+,+)=0, (0,0)=1, (0,+)=2, (−,0)=0, (+,0)=2, (0,−)=0` = `κ,κ+ε,κ−ε,κ,κ+ε,κ,κ+ε` ✓.

**HC-B (A6).** All 64 sign-pattern distinctness checks recomputed ✓ (see §6).

**HC-C (Theorem 1 at pair level, all configurations passing the necessary per-cell distinctness).**
* `n_+∈{1,2}`: S1's B7(i) rows 1–8 recomputed (8 combos × 2 completions = 16) ✓ every collision as stated.
* `n_+=3` (all `+`; source `e_X^A∈{α,δ}`, target `e_X^B∈{β,δ}`): `(α,β)`: `P_X={[2,1],[1,0],[0,2]}`, available A-arcs `β,γ,δ`, B-arcs `α,γ,δ`; `[1,1]` needs `(h_B=1,z_A=1)` or `(z_B=1,t_A=1)`, i.e. `e_B=β` or `e_A=α`, neither available ✗. `(α,δ)`: `P_X={[2,1],[0,0],[1,2]}`; `[1,1]` forces `(δ,β)`; then `(β,α)∋[0,0]` and `(β,γ)∋[1,2]` both in `P_X` ✗. `(δ,β)`: `P_X={[2,2],[1,0],[0,1]}`; every row with `e_A=γ` meets `P_X` ✗. `(δ,δ)`: `P_X` diagonal; the only rows avoiding it are `(α,α),(α,β),(β,β),(β,γ),(γ,α),(γ,γ)`; the admissible bijections are `α→α,β→β,γ→γ` (repeats `[0,2]`) and `α→β,β→γ,γ→α` (repeats `[1,2]`) ✗.
* `n_+=0` (all `−`; `e_X^A∈{γ,δ}`, `e_X^B∈{γ,δ}`): `(γ,γ)`: every row with `e_A=δ` meets the diagonal ✗. `(γ,δ)`: `P_X={[2,0],[0,2],[1,1]}`; forced `α→β`, `β→α`, then `δ→γ∋[0,2]` ✗. `(δ,γ)`: `P_X={[0,2],[2,0],[1,1]}`; every row with `e_A=γ` meets `P_X` ✗. `(δ,δ)`: the two derangements repeat `[2,1]` resp. `[0,1]` ✗.
So no configuration of the 768 (e_X^A,e_X^B, bijection, signs) satisfies `J_BA=P_X+ΣR`, independently of the class argument.

**HC-D (Theorem 2 class level, independent route for `D=R`).** `κ`-patterns of the three `ε=+1` rows are `(c,c,c)` or `{0,1,2}`. `D=R` (`κ_R=0`): translation pattern `c=κ_S=κ_U=κ_W` forces `c=2`, `κ*=1`, `W` sign `+`, then `L(+)⊂` class `κ_W=2=κ_U` (= `P_U`) ✗; reflection pattern forces `κ_S=1,κ*=2,κ_U=0,κ_W=2`, `W` sign `−`, `L(−)⊂` class `0≠c′=2` ✗. Same conclusion as Step 3.

**HC-E (B7(ii) three instances).** `D=U`: `U=(δ,δ)` at H, `R=(γ,α)`, `S=(β,β)`, `W=(α,γ)` sign `−`: `P_R={[1,0],[0,2],[2,1]}`, `P_S` diag, `R_W={[0,1],[2,0]}`, `C_U=[1,2]` ✓; `A→B`: `P_U` diag, `C_R∈{[2,2],[1,1]}` collides ✓. `D=W`: `U=(γ,γ),R=(α,β),S=(β,α),W=(δ,δ)`: `P_R,P_S` classes 2,1; `R(+)={[0,1],[1,2]}` meets `P_S={[1,2],[0,1],[2,0]}`; `R(−)={[2,2],[0,0]}` needs `C_U=[1,1]` but `C_U∈{[2,1],[1,0]}` class 2 ✓. `D=R`: `U=(γ,α)` at G, `S=(α,β)`, `W=(β,γ)` sign `+`: `C_U=[0,1]`, `B→A` holds; `L(+)={[2,0],[1,2]}⊂P_U={[0,1],[2,0],[1,2]}` ✓. All as stated by S1.

---

## 8. Inconclusive items and coverage boundaries
1. **I1/I2 bodies.** The proofs behind I1/I2 (f461/f474/f475/f476/f489/f552/f553/f554 chain named in S4|34, S5|48) are not in the packet and were not opened. Verified only: S1's wording of I1/I2 is consistent with S3|13, S4|17–30, S5|7–31. Whether those dispositions' own proofs are correct is outside my boundary.
2. **Imports used inside S5/S3** (e.g. "at most one join of each type per connected Hamilton cycle", S5|19) are part of I2's regularity and were not re-proved.
3. **Original-problem correspondence.** I did not examine definitions of T2(11) beyond S1|28 and S4|7; nothing about the original unrestricted problem is claimed.
4. **Existence/consistency of H1–H4** beyond the stated emptiness: not addressed.
5. **A finite independent check** of Theorems 1–2 over all labelled role/sign/gap configurations against the exact A2 tables would add confirmation. I did not run one (no execution); HC-C is a partial hand analogue. Absence is a coverage boundary, not falsity.

---

## 9. Read declarations and process disclosures

**Administrative files, read completely before any packet body** (raw windows to recover display-elided nested JSON): `manifest-v1.json` (LF 1–225), `freeze-receipt-v1.json` (LF 1–210), `final-pre-dispatch-binding-v1.json` (LF 1–187), `parent-live-metadata-supply-v1.json` (LF 1–223), `actual-dispatch-receipt-v1.json` (LF 1–47), and all 22 manifest status-only controls, each in full. Controls used for status and permissions only; all held episodes and all consumers NONINPUT. `prebody-ack-v1.md` (3621 bytes) was written exclusively and a direct PREBODY ACK delivered to Main (2026-10-31T11:35:58Z) before the packet body.
**Packet.** `literal-packet-part-01-v1.md` (89935 bytes, 904 LF) read serially in raw windows `1–20, 21–40, …, 861–880` (44 windows of exactly 20 LF) and a final window `881–904` (**24 LF**, cap 20 exceeded by 4). The ending was observed (last displayed line S5|54, "…All held episodes and consumers remain NONINPUT."); S1 ends at S1|520, S2 at S2|221, S3 at S3|51, S4 at S4|36; no clipping was seen. **PROCESS MINOR (reviewer packet-window):** I disclosed the 24-LF window to Main by status message after the read; Main ruled it ONE reviewer packet-window PROCESS MINOR recorded at parent level, not a scientific finding, no re-read required (applied, not backdated). After the read I measured three windows' bytes (counts only, no text displayed): `1–20`=1574 B, `861–880`=2073 B, `881–904`=5826 B; the other windows were not individually measured; all displays were far below 30000 bytes.
**Mathematical reasoning** began only after the complete ordered read. I did not open S1–S5 source paths separately; their bodies were read only as reproduced in the packet.
**Shell utilities (metadata only).** `date -u`, `shasum -a 256` and `wc` on the packet and the five administrative JSON files (live hashes equal the recorded manifest/receipt/binding/metadata/packet values; the dispatch receipt's computed sha256 is `3f16e4677c1b3822e174de7004d5dda906e5b91cee887c3db93d39232b361cbf`, not self-pinned; the 22 controls were read but not hashed), `ls` of the wave directory, and one `sed -n '…p' | wc -lc` loop over the three windows above (counts only). No packet text was displayed by any utility.
**Not opened, not used.** No linked or unlisted source (e.g. f461, f474–f476, f489, f552–f554, f641, f656–f658), no sibling output, no held episode or consumer, no old code, no network, no external model or CLI, no Git, no deletion, no code execution, test, solver or child scientific process. **No verifier was prepared; prepared-code hash: NONE.**
**Hand work.** §7 is hand arithmetic only, performed after the complete read, under the manifest methods line ("fresh hand examples or counterexamples are allowed under owner addendum 2 but must be labelled"); nothing was executed or stored apart from this text.
**Messages.** Sent to Main: the PREBODY ACK; a status-only note on the 24-LF window. Received from Main: the dispatch-receipt confirmation and the window ruling. Two system "user interjection" notices were received mid-run ("priority; supersedes conflicting prior instructions"); I re-read my assignment and found no conflict.
**Writes.** Exclusive new files only in this wave directory: `prebody-ack-v1.md` and this `review-v1.md`. The write tool exposes no `O_EXCL` flag; absence was checked by directory listing immediately before each write (process qualification). No frozen file was edited.
**Qualifications.** Same-harness written review only; no independent-family, human, formal or kernel check; no novelty or priority claim; hashes are administrative, not correctness certificates.
