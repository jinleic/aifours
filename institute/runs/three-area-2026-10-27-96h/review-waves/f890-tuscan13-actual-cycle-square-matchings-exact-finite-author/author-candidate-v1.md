# f890 author candidate v1: exact local actual-cycle grammar, square matchings and chord tables (T13 four-full branch)

**Status:** prospective GENERAL AUTHOR candidate (owner addendum 2) by `VerifyF890TuscanExact`. Written derivations plus a
NEW standalone stdlib verifier prepared **UNRUN**. No scientific execution of any kind occurred. Parent full source read and
a separate one-shot GO are required before any run. Parent disposition is separate; nothing here is adopted.

## 1. Exact scope and quantifiers

Fix four labeled three-vertex cells `A,B,C,D`, opposite pairs `{A,B}` and `{C,D}`, twelve vertices `(X,k)`, `k∈{0,1,2}`.
A **local actual cycle** is one directed Hamilton cycle on exactly these twelve vertices (each vertex once, hence connected).
Its **directed squares** are the arcs `x→z` for consecutive `x→y→z`, cyclically; `S_{PQ}` is the set of squares with tail in
`P`, head in `Q`. A **run** is a maximal cyclically consecutive same-cell segment; a **join** of a pair is an arc between its
two cells. The four-full row is `F=(A0 A1 A2 B0 B1 B2 C0 C1 C2 D0 D1 D2)`, so `F` joins `A→B`, `C→D` and cell labels are the
positions on `F`'s full runs, matching S1 (12) (`α=1→0, β=2→1, γ=0→2, δ=2→0`).

All results below quantify over **every** local actual cycle with one double and one singleton run in each cell, exactly one
join per opposite pair, both join endpoints in doubles, and singleton transport (each singleton's two neighbours lie one in
each cell of the other pair), and over every labeling of the four cells. They are **local**: one cycle at a time (Sections
2–3), or abstract `3×3` zero-one matrix identities (Section 4), or the literal pair `(U,W)` subcase of S1 §5 (Section 6).
Nothing here asserts a five-cycle residual decomposition, a `T13`/`T14` branch exhaustion, a T2(11) array, `M=C`, or
existence of any global configuration.

### Conditional imports (named, not reproved)

* **J1 = S1 I1 / S2:13–15 / S3:17** — under `M=C` and two tripled supports, the five residual cycles' squares between each
  ordered opposite pair are exactly the nine entries once each; this is the premise behind S1 (6) and (9).
* **J2 = S1 I2–I3 / S2:5,17 / S3:19–30** — `T13` regularity, the `(4,0,0,0,0)` pattern, layouts `2+1` in zero-full rows,
  join endpoints nontrivial, singleton transport. Used only as the *definition* of the local cycles enumerated here.
* **J3 = S1 hypothesis** — `2:3`/`3:2` joins (`n_+∈{1,2}`); S2:7 `4:1` exclusion is NOT used and not reproved.
* **J4** — directed-arc uniqueness inside a cell across `F,U,W` (S1 §4 and §5 "distinct"), a consequence of J1's arc
  partition (S2:13). Used only in Section 6, as a stated hypothesis.

## 2. Exact zero-full grammar (written proof; verifier rechecks by full enumeration)

Let `X=x0x1` and `Y=y0y1` be the two join blocks (doubles, in cycle order). All four singletons lie in the two gaps
`G` (after `X`) and `H` (after `Y`).

* A gap of size 1 is impossible: its singleton would neighbour `x1` and `y0`, cells of different pairs.
* Size 3 is impossible: its first entry neighbours `x1`, so it lies in pair `Y` and forces the second to be `x0`; the third
  then neighbours `x0` and `y0`, again cells of different pairs.
* Size 4 (`G`): the first neighbours `x1` so lies in `Y`, the second must be `x0`; the last precedes `y0` so lies in `X`, the
  third must be `y1`; then `x0`'s neighbours force the first to be `y0` and `y1`'s force the last to be `x1`:
  `G=y0⁰ x0⁰ y1⁰ x1⁰`, `H=∅` (symmetrically `H=x0⁰ y0⁰ x1⁰ y1⁰`, `G=∅`).
* Size 2+2: `G=y1⁰ x0⁰`, `H=x1⁰ y0⁰` by the same two-step forcing.

These are exactly S1's table rows (lines 36–40), with an empty gap allowed. With rotation fixed at `A`'s double and the two
join directions free, the words are **4 grouped-after-`AB`, 4 grouped-after-`CD`, 4 split** (12 total); each has `6^4=1296`
labelings. Maximality holds automatically (no two consecutive runs share a cell).

## 3. Actual square matchings of one cycle (written two-step readings)

For pair `(p,q)` with roles `p⁻→p⁺` (double), `p⁰` (singleton), reading the strings above gives, for **every** labeling:

| row | join | `S_{pq}` | `S_{qp}` |
|---|---|---|---|
| grouped, gap after this pair's block | `p→q` | `P={(p⁻,q⁻),(p⁺,q⁺),(p⁰,q⁰)}` | `C={(q⁺,p⁰)}` |
| grouped, gap after the other block | `p→q` | `P` as above | `C={(q⁰,p⁻)}` |
| grouped, gap after this block | `q→p` | `C={(p⁺,q⁰)}` | `P={(q⁻,p⁻),(q⁺,p⁺),(q⁰,p⁰)}` |
| grouped, gap after the other block | `q→p` | `C={(p⁰,q⁻)}` | `P` as above |
| split | `p→q` | `L={(p⁻,q⁻),(p⁺,q⁺)}`, omits `(p⁰,q⁰)` | `R={(q⁺,p⁰),(q⁰,p⁻)}`, omits `(q⁻,p⁺)` |
| split | `q→p` | `L={(p⁺,q⁰),(p⁰,q⁻)}`, omits `(p⁻,q⁺)` | `R={(q⁻,p⁻),(q⁺,p⁺)}`, omits `(q⁰,p⁰)` |

Example derivation (grouped after `X=AB`, joins `A→B`, `C→D`): `A⁻A⁺B⁻B⁺ C⁰A⁰D⁰B⁰ C⁻C⁺D⁻D⁺`; the `A→B` squares are
`A⁻A⁺B⁻`, `A⁺B⁻B⁺`, `A⁰D⁰B⁰`; the only `B→A` square is `B⁺C⁰A⁰`; the only `D→C` square is `D⁰B⁰C⁻`. The wrap
`D⁺→A⁻→A⁺` gives no opposite-pair square. Hence one physical gap fixes **both** reverse squares: `(B⁺,A⁰)` and `(D⁰,C⁻)`,
which is S1's coupling after (3). This agrees with S1 (2)–(4) and its omitted-pair table. `F` gives
`F_{AB}={(A1,B0),(A2,B1)}`, `F_{BA}=∅` (same for `C,D`). Counts: grouped `3` forward / `1` reverse, split `2/2`.

**Count (5).** With `g` grouped rows, `n` of them signed like `F`: `#A→B = 2+3n+(g−n)+2(4−g)=10+2n−g`; it equals 9 iff
`g=2n+1`, so `g∈{1,3}`. (Total squares per pair are always 18, so `B→A=9` is equivalent.) Of the `2^4·2^4` kind/sign
assignments exactly `4·8+4·2·3=56` satisfy it.

## 4. Abstract `3×3` identities (written proofs; verifier rechecks exhaustively)

* **(7) involution, all six `π`.** For each of the 6 permutation matchings `π`, the six other entries form a bipartite
  6-cycle; it has exactly **4** partitions into two-edge matchings: the all-reciprocal one (relative permutation
  `π^{-1}τ=id`) and three with one reciprocal pair (`π^{-1}τ` a transposition). Each vertex of the 6-cycle has degree 2 and
  its two edges lie in different pairs, so omitted tails (heads) are distinct. Example `π=id`:
  `{01,10}{02,21}{12,20}` omits `(2,2),(1,0),(0,1)`, i.e. the transposition `(0 1)`.
* **(10) third matching.** For disjoint `π_R,π_S`, `δ=π_R^{-1}π_S` is fixed-point-free on three points, hence a 3-cycle, and
  `ρ=π_Rδ²` is the complementary perfect matching (`π_Rδ^0, π_Rδ, π_Rδ²` are the three values). If
  `π_R+π_S+R_W+C=J`, then `R_W∪C=ρ`, so `C=(u,ρ(u))` with `(u,v)` the omitted pair of `R_W`. Exactly `12·3=36` solutions.
* **(8)** tail degree: `3=[a∈{1,2}]+[a=x]+3−#{i:t_i=a}` gives `{t_i}={1,2,x}`; heads `{h_i}={0,1,y}`.
* **(11)** after removing `P_U`: `[a∈{1,2}]+1−[a=t]+[a=x_R]+[a=x_S]=2` gives `{x_R,x_S}={0,t}`; heads `{y_R,y_S}={2,h}`.

## 5. Per-cell chord tables (new compact rule + full written recomputation)

**Omitted-vertex rule** (from the split rows of §3, pair oriented by `F`): if a split row's double in that cell is `e=v⁻→v⁺`,
the omitted **head** of `R^{BA}` in source cell `A` is `v⁺` for sign `+` and the singleton `v⁰` for sign `−`; the omitted
**tail** in target cell `B` is `v⁻` for `+` and `v⁰` for `−`. This reproduces S1's table (lines 180–185) entry by entry:
source `α 0/2, β 1/0, γ 2/1, δ 0/1`; target `α 1/2, β 2/0, γ 0/1, δ 2/1`.

Checking all `4` choices of `e_X` × `3` positions of the minority sign, for both `n_+=1` and `n_+=2` and both cell roles
(48 cases, each written out), distinct omitted vertices survive exactly in:

| cell / `n_+` | surviving `(e_X, e_minority)` | one decisive witness / failure |
|---|---|---|
| source, 1 | `(α,γ)`, `(β,δ)` | `e_X=α`: `γ+,β−,δ−` → `2,0,1`; `β+,γ−,δ−` → `1,1,1` |
| target, 1 | `(α,δ)`, `(β,γ)` | `e_X=γ`: all three placements collide (`1,0,1`; `2,2,1`; `2,2,0`) |
| source, 2 | `(β,δ)`, `(γ,α)` | `e_X=γ`: `α−,β+,δ+` → `2,1,0` |
| target, 2 | `(α,δ)`, `(γ,β)` | `e_X=δ`: `2,2,0`; `0,1,0`; `1,1,2` all collide |

This **confirms** S1 lines 165–170 and claims 1–3 at the per-cell necessary level (in particular `e_X≠δ` in every cell).

## 6. Actual `g=3` coupled shared gap (S1 §5), both gap cases

Hypotheses: `U` grouped with joins `A→B`, `C→D` (matching `F` in both pairs), `W` split with `B→A`, `D→C`; (10) for both pairs
(i.e. `C_U^{BA}` = omitted pair of `R_W^{BA}`, `C_U^{DC}` = omitted pair of `R_W^{DC}`), and J4 in every cell.

* Gap after `U`'s `AB` block: `C_U=(B_U⁺,A_U⁰),(D_U⁰,C_U⁻)`; `W` omits `(B_W⁰,A_W⁰),(D_W⁰,C_W⁰)`. So `A_U⁰=A_W⁰`,
  `D_U⁰=D_W⁰`; the two doubles in `A` (and `D`) lie on the same two vertices and are distinct, hence reversed; the only
  reversed pair avoiding `F`'s `0→1,1→2` is `{γ,δ}`.
* Gap after `U`'s `CD` block: `C_U=(B_U⁰,A_U⁻),(D_U⁺,C_U⁰)`, giving `B_U⁰=B_W⁰`, `C_U⁰=C_W⁰` and `{γ,δ}` in cells `B,C`.

Thus (13) holds; the conclusion is a necessary condition only. **Literal positive control** (verifier `PC_GROUPED`,
`PC_W3`): `U=A2 A0 B1 B0 C2 A1 D1 B2 C1 C0 D0 D2`, `W=B2 B1 A0 A2 C1 B0 D2 D0 C2 C0 A1 D1`. Then
`C_U^{BA}=(B0,A1)`, `C_U^{DC}=(D1,C1)` equal `W`'s omitted pairs; arcs per cell `A: U δ, W γ`; `B: U α, W β`;
`C: U α, W δ`; `D: U γ, W δ`, all distinct from `F` and each other; `{γ,δ}` in `A` and `D` as predicted. Both gap cases are
nonvacuous locally (written construction: after `CD`, take `B⁰=C⁰=1` common, `U_A=α`, `W_A∈{γ,δ}`, `U_D=α`, `W_D=β`).

## 7. Prepared UNRUN verifier

`exact-local-cycle-square-matchings-v1.py` — sha256 `ac3af2e1441ccff1954454e52d99c0f87ab3c1245bb01da3e6288ba579477434`,
23440 bytes, 586 LF; new code, stdlib only (`hashlib, itertools, json, sys, time`); no subprocess, network or file write.
Intended command after GO: `python3 exact-local-cycle-square-matchings-v1.py`, outer timeout ≤55 s; internal deadline 40 s
(`internal_deadline`, exit 2). Every stage prints one flushed JSON line; final line `COMPLETE_LOCAL_ONLY` (exit 0) or
`FAIL`/`ERROR` with reason (exit 1).

Stages: (1) actual-cycle positive controls (literal `F`, grouped, split, `(U,W)` pair; hard-coded squares); (2) all 5040
words with `A`'s double first, filtering only by layout/join/endpoint/transport reasons, any other survivor is a hard
`grammar_extra` failure, and forms must equal `4/4/4`; (3) all `12·1296=15552` labeled cycles: §3 table, omitted pairs,
square counts, chord map (must be single-valued), `U(++)`, `W(−−)` lists; (4) count (5); (5) (7) over all six `π`; (10);
(8); (11); (6) chord tables vs §5, claim `e_X≠δ`; (7) `g=3` shared gap over all actual `U,W` with key equality and J4,
requiring survivors in both gap cases; (8) nine intended-reason mutants: repeated-vertex relaxed fixture
(`guard_not_hamilton`), 11-vertex relaxed path (`guard_not_12`), literal transport violator
`A0 A1 B0 B1 C2 A2 C0 C1 D0 D1 B2 D2` (`transport`), swapped gap (`C_formula`), non-matching pair (`pair_not_matching`),
wrong third entry (`J_mismatch`), flipped chord entry (`chord_table`), dropped four-row entry (`four_row_table`), `g=3`
without arc uniqueness (`g3_conclusion`).

Written predictions only (not results): forms `4/4/4`; 15552 cycles; `U_pp=2592`, `W_mm=1296`; 56 count solutions; each
involution shape `[1,1,1,3]`; 36 third-matching solutions. Other counts are not predicted.

Known design limits of v1 (not edited): the role-level `g3_endpoint` re-assertion is active only for the gap-after-`AB`
case (for gap-after-`CD` the endpoint identities are enforced by the actual-square key equality, not re-asserted); the
source file handle in `main` is not explicitly closed. The write tool reported setting the executable bit on the `.py`; it
was never executed.

## 8. Result limits

Local necessary identities only. Not shown: that any `g=1`/`g=3` system is nonempty globally, sufficiency, extension to the
other six actual cycles, cross-cell/cross-pair agreement of chord choices, J1 itself, `M=C`, `(2,2,0,0,0)`, `T14`, a T2(11)
array or a no-go. The verifier does **not** enumerate five-cycle residual decompositions or arrays and uses no relaxed or
selected-interface fixture. No family/human/formal acceptance, novelty or priority claim.

## 9. Read, process and execution declaration

* Before any mathematical body I read completely (raw) the manifest, freeze receipt, final binding, metadata, the actual
  dispatch receipt (naming `VerifyF890TuscanExact`) and all 22 controls, as status only; recomputed `shasum -a 256` for the
  five administrative files and the packet (all pins matched); wrote `prebody-ack-v1.md`; sent a direct ACK to Main.
* Then read the sole literal part completely in order in raw windows 1–20, 21–40, …, 281–300, 301–322: 16 windows, fifteen
  of 20 LF and a final window of **22 LF** (301–322). That final window exceeded the manifest `raw_window_max_lf=20` by two
  lines: a disclosed PROCESS deviation, not clipping (max line 1870 chars, every display far below 30000 bytes; terminal
  line S3|36 and the part ending were read). This declaration was corrected in place before delivery; it first said
  "17 windows, ≤20 LF", which was wrong.
* Inputs used: S1, S2, S3 complete bodies only. Linked/unlisted files (f641, f656, f657, f658, f461, f474–f476 etc.) were
  not opened; held episodes and consumers were not inspected. No skill or old code was read.
* Process facts: one earlier response of mine (after the packet read) exceeded the harness output limit and was discarded
  unseen with its planned tool calls; no file or message came from it. Shell use was administrative only (`wc`, `shasum`,
  `date`, `ls`). No code, test, solver, eval, network, external model or child scientific process ran. Writes:
  `prebody-ack-v1.md`, `exact-local-cycle-square-matchings-v1.py`, this file, all new, inside this wave directory.
