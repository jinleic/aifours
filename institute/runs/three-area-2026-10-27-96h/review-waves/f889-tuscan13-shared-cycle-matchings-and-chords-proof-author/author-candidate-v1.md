# Author candidate v1 (f889): actual T13 four-full-row matchings and chords — independent reconstruction and an exact mod-3 class obstruction

**Author:** AuthorF889TuscanMatch (prospective GENERAL AUTHOR under owner addendum 2). **Status:** author candidate only. Disjoint checking and parent disposition are separate. No family, human, formal or kernel acceptance is claimed, and no novelty, publication priority or global theorem.

**Summary.**

* **Part A** independently re-derives every displayed f853 (S1) item in scope, on the same actual cycles and vertices:
  * the actual zero-full cycle grammar (grouped at `G`, grouped at `H`, split), including the shared-gap coupling;
  * the exact square matchings (1)–(4) and the omitted-pair table, for both opposite pairs;
  * the exhaustive count (5), `g=2n+1∈{1,3}`;
  * the `g=1` equations (6), the relative-permutation involution (7) and the forward-degree multisets (8);
  * the `g=3` equations (9), the forced third matching (10) and the multisets (11);
  * the split-edge omitted-vertex table and all four source/target × minority-sign chord rows, with consequences 1–3;
  * the shared-gap subcase (13).

  No mathematical discrepancy was found. Two refinements are added: A4 identifies which transposition occurs, and A7 shows the common singleton is the run middle.
* **Part B (new).** Label every cell by its position in the actual full run of `F`. The four non-`F` internal arcs then have a rigid mod-3 form, and every actual square matching of every zero-full row lies in prescribed difference classes. For **either single opposite pair**:
  * a parity count makes the `g=1` equation impossible;
  * a short class case split makes the two `g=3` equations jointly impossible.

  Hence, under the explicit hypotheses H1–H4 and imports I1–I2 of §0, the actual `(4,0,0,0,0)` T13 branch is **empty**.
* **What Part B does not use:** the `2:3/3:2` split (H5), the optional import I4, either gap choice, any split-row sign, or the second opposite pair.
* **What Part B is:** a written proof over all configurations of exact necessary equations.
* **What Part B is not:** an inference from finite or relaxed fixtures, a construction, or a T2(11) no-go.

## 0. Exact quantifiers, hypotheses and conditional imports

**Quantifiers.** The statements quantify over every actual T2(11) array 𝒯 on an 11-symbol set X: eleven rows, each a permutation of X, in which each ordered pair occurs at most once at row-distance 1 and at most once at row-distance 2. They also quantify over every ordered choice of two distinct odd-position six-supports Σ₁ ≠ Σ₂, each the odd-position support of three rows of 𝒯.

**Hypotheses.** Assume simultaneously:

* **H1 (`M=C`):** the actual missing linear distance-two set `M` of 𝒯 equals its actual last-to-first closing set `C`.
* **H2 (two tripled supports):** Σ₁, Σ₂ as above. Other tripled supports, if any, are neither excluded nor used.
* **H3 (`T=13`):** the synchronized interface value of (Σ₁, Σ₂) is `T=13`, in S3's notation.
* **H4 (full count):** the five residual cycles have full-cell-count pattern `(4,0,0,0,0)`.
* **H5 (f853's split; optional):** each opposite pair has join split `2:3` or `3:2`. It is used only where Part A reconstructs S1 statements that assume it. Part B never uses H5.

**Named conditional imports.** These are load-bearing. They come from the literal adopted dispositions S2 and S3. Their complete proofs are not in the packet and are not re-proved here.

* **I1** (S2:13; S1 §1 I1). Adjoining one common `∞` to every row gives eleven connected directed Hamilton 12-cycles on X∪{∞}. These partition all 132 directed adjacency arcs. Under H1, their directed squares (each vertex to the vertex two steps later, in cycle orientation) also partition all 132 ordered pairs.
* **I2** (S2:13; S3:17–30; S1 §1 I2). Under H1–H2:
  * the cells I=Σ₁∩Σ₂, J=Σ₁∖Σ₂, K=Σ₂∖Σ₁ and L=(X∪{∞})∖(Σ₁∪Σ₂) each have size three, with opposite pairs {I,L} and {J,K};
  * six cycles alternate across Σ₁ or Σ₂, and five residual cycles remain.

  Under `T=13`, on the five residual cycles each cell has exactly one full (length-3) run and four layouts "one double + one singleton". Every residual cycle is regular: for each opposite pair it has exactly one join (an adjacency arc between the two opposite cells), with both endpoints in nontrivial runs.
* **Transport (S1 I3) is not imported.** A1 re-derives the singleton-transport law from I1+I2 by the counting route of S2:15.
* **I4 is not used anywhere.** This is S1's optional exclusion of `4:1`/`1:4`, which rests on the unlisted f641 four-case proof.

**Two cut facts**, immediate from the definitions in I2:

* Opposite cells lie on different sides of both Σ₁ and Σ₂.
* An alternating cycle's adjacency arcs all cross its cut, and its squares never do.

Hence (a) no alternating cycle has an internal-cell adjacency arc, and (b) no alternating cycle has a square between opposite cells. Combined with I1:

* every directed pair between opposite cells is a square of exactly one of the five residual cycles;
* every internal-cell directed arc is an adjacency arc of exactly one residual cycle.

The cell `L` contains `∞`. That changes nothing: `∞` is an ordinary vertex of its cell, and its arcs and squares belong to the I1 partitions.

## 1. Notation (one array, one set of actual cycles)

**Rows.** `F` is the unique four-full residual cycle. The other four residual cycles are the zero-full rows.

**Pair orientation.** For an opposite pair, orient the names so that `F`'s join is `A→B`: `A` is the source cell and `B` the target cell. By I2 regularity, `F` (four runs of three) has exactly one join per pair. Name the other pair `Y→Z` by `F`'s join; then the cyclic run order of `F` is `A,B,Y,Z`. (S1 §5 uses `A,B,C,D` for this order; there `C` is a cell, not the closing set.)

**Labels.** Label each cell by `F`. The actual full run of `F` in cell `V` is `v_0→v_1→v_2`; write `ℓ(v_i)=i∈ℤ/3`.

**Roles.** In a zero-full row `r`, cell `V` has one double `v_r⁻→v_r⁺` (in cycle orientation) and one singleton `v_r⁰`. These are actual labeled vertices, shared by both pairs.

**Arcs.** The four internal arcs of `V` not used by `F` are (S1 (12)):

`α=1→0`, `β=2→1`, `γ=0→2`, `δ=2→0`.

**Pairs and classes.** For a directed pair between `A` and `B`, write `[i,j]_{BA}` for `b_i→a_j` and `[i,j]_{AB}` for `a_i→b_j`, tail label first. Its **class** is `cl = ℓ(A-endpoint) − ℓ(B-endpoint) ∈ ℤ/3` in both directions. In each direction each class consists of exactly three pairs, and those three pairs form a perfect matching.

## Part A. Independent reconstruction of S1

### A1. Singleton transport and the actual cycle grammar

**Transport (re-derived).**

1. Fix an opposite pair {A,B}, and let {Y,Z} be the other pair. The 18 directed A–B pairs are squares of the five residual cycles, once each (§0).
2. Each residual cycle has a unique A–B join `x→y`, with nontrivial runs `x′→x` and `y→y′`. It gives exactly the two squares `x′→y` and `x→y′`.
3. Every other A–B square `u→m→w` has `m∉A∪B`. If `m` were in `A∪B`, one of `u→m`, `m→w` would be an A–B adjacency arc, i.e. the cycle's unique join, and the square would be one of its two join squares.
4. So `m∈Y∪Z`. Neither neighbor of `m` is in `m`'s cell, so `m` is a singleton run.
5. By I2, each of `Y` and `Z` has exactly four singleton runs on the five residual cycles, and each is the middle of at most one square.

Hence `18 ≤ 2·5 + 8`, with equality. This gives **law T: every singleton run of a cell of one pair has one neighbor in each cell of the other pair.** By symmetry the law holds for all four cells.

**Grammar.** In a zero-full row each cell has one double and one singleton. Name the row's joins `p0→p1` and `q0→q1` (cell names are per row).

* Join endpoints lie in doubles, so the join is the arc from the end of the `p0` double to the start of the `p1` double. This gives the block `p0⁻ p0⁺ p1⁻ p1⁺`, and likewise the block `q0⁻ q0⁺ q1⁻ q1⁺`.
* The four singletons fill two gaps: `G`, after the `p`-block and before the `q`-block; and `H`, after the `q`-block and before the `p`-block. Let `k=|G|`.

The cases are:

* **`k∈{1,3}` is impossible.** A gap of length one holds a singleton whose neighbors are `p1` and `q0` (in `G`) or `q1` and `p0` (in `H`). These are cells of different pairs, contrary to T.
* **`k=4`.**
  * The first `G` singleton follows `p1`, so it is a `q`-singleton, and it is followed by `p0⁰`.
  * `p0⁰` is followed by the other `q`-singleton, which is followed by `p1⁰`.
  * `p1⁰` precedes `q0⁻`, so the third singleton is `q1⁰` and the first is `q0⁰`.

  Result: `G = q0⁰ p0⁰ q1⁰ p1⁰`, and `H` is empty.
* **`k=0`.** Symmetrically, `H = p0⁰ q0⁰ p1⁰ q1⁰`, and `G` is empty.
* **`k=2`.**
  * `G`'s first singleton follows `p1`, so it is a `q`-singleton followed by `p0⁰`. Since `p0⁰` precedes `q0⁻`, `G = q1⁰ p0⁰`.
  * `H` starts after `q1⁺` with the remaining `p`-singleton `p1⁰`, followed by `q0⁰`, which precedes `p0⁻`. So `H = p1⁰ q0⁰`.

This reproduces S1's table (S1 §2) exactly, including all cyclic endpoints and the empty gap. The complete words, positions 1–12 read cyclically, are:

* `W_G` (grouped at `G`): `p0⁻ p0⁺ p1⁻ p1⁺ q0⁰ p0⁰ q1⁰ p1⁰ q0⁻ q0⁺ q1⁻ q1⁺`
* `W_H` (grouped at `H`): `p0⁻ p0⁺ p1⁻ p1⁺ q0⁻ q0⁺ q1⁻ q1⁺ p0⁰ q0⁰ p1⁰ q1⁰`
* `W_S` (split): `p0⁻ p0⁺ p1⁻ p1⁺ q1⁰ p0⁰ q0⁻ q0⁺ q1⁻ q1⁺ p1⁰ q0⁰`

In each word every singleton satisfies T, and the only opposite-cell adjacency arcs are the two joins. The empty-gap arcs, `q1⁺→p0⁻` in `W_G` and `p1⁺→q0⁻` in `W_H`, join non-opposite cells.

"Grouped" versus "split" is a property of the physical row, not of a pair. Exchanging the roles of the two pairs exchanges `G` and `H`: grouped at `G` for `(p,q)` is grouped at `H` for `(q,p)`.

### A2. Exact square matchings of every actual row kind (both pairs)

All twelve squares `i→i+2` of each word:

| word | pair `p` forward (`p0→p1`) | pair `p` reverse | pair `q` forward (`q0→q1`) | pair `q` reverse | non-opposite squares |
|---|---|---|---|---|---|
| `W_G` | `p0⁻→p1⁻, p0⁺→p1⁺, p0⁰→p1⁰` | `p1⁺→p0⁰` | `q0⁰→q1⁰, q0⁻→q1⁻, q0⁺→q1⁺` | `q1⁰→q0⁻` | `p1⁻→q0⁰, p1⁰→q0⁺, q1⁻→p0⁻, q1⁺→p0⁺` |
| `W_H` | `p0⁻→p1⁻, p0⁺→p1⁺, p0⁰→p1⁰` | `p1⁰→p0⁻` | `q0⁻→q1⁻, q0⁺→q1⁺, q0⁰→q1⁰` | `q1⁺→q0⁰` | `p1⁻→q0⁻, p1⁺→q0⁺, q1⁻→p0⁰, q1⁰→p0⁺` |
| `W_S` | `p0⁻→p1⁻, p0⁺→p1⁺` | `p1⁺→p0⁰, p1⁰→p0⁻` | `q0⁻→q1⁻, q0⁺→q1⁺` | `q1⁰→q0⁻, q1⁺→q0⁰` | `p1⁻→q1⁰, p0⁰→q0⁺, q1⁻→p1⁰, q0⁰→p0⁺` |

The row `F` = `a_0 a_1 a_2 b_0 b_1 b_2 y_0 y_1 y_2 z_0 z_1 z_2` has only the A–B squares `a_1→b_0` and `a_2→b_1`. This is S1 (1), `F_AB={(a_1,b_0),(a_2,b_1)}`, and `F` has no `B→A` square.

Consequences, all matching S1 verbatim:

* **(2)** A grouped row with join `p0→p1` has the full permutation matching `P={(p0⁻,p1⁻),(p0⁺,p1⁺),(p0⁰,p1⁰)}`. The first two squares are centered at the join; the third is centered at a singleton of the other pair (`q1⁰` in `W_G`, `q0⁰` in `W_H`).
* **(3)** Its unique reverse square is `(p1⁺,p0⁰)` at `G` and `(p1⁰,p0⁻)` at `H`. In the same physical row, the other pair's reverse square is `(q1⁰,q0⁻)` at `G` and `(q1⁺,q0⁰)` at `H`.
  * Coupling in invariant form: in a grouped row, the pair whose join block **immediately precedes** the four singletons has reverse square `target⁺→source⁰`; the pair whose block **immediately follows** them has `target⁰→source⁻`.
  * So the two choices of (3) are never independent.
* **(4)** Split rows:
  * sign `+` (join `A→B`): `L^AB={(a⁻,b⁻),(a⁺,b⁺)}` and `R^BA={(b⁺,a⁰),(b⁰,a⁻)}`;
  * sign `−` (join `B→A`, i.e. `p0=B`): `L^AB={(a⁺,b⁰),(a⁰,b⁻)}` and `R^BA={(b⁻,a⁻),(b⁺,a⁺)}`.

  Omitted (tail, head) pairs:
  * sign `+`: `L` omits `(a⁰,b⁰)` and `R` omits `(b⁻,a⁺)`;
  * sign `−`: `L` omits `(a⁻,b⁺)` and `R` omits `(b⁰,a⁰)`.

  Each two-edge set has distinct tails and distinct heads.

Every row contributes exactly four A–B squares, so per pair the total is `2+4·4=18` ✓.

### A3. Exhaustive count

Let `g` be the number of grouped zero-full rows, and `n` the number of them whose join for the given pair has `F`'s direction.

* Counting `A→B` squares gives `9 = 2 + 3n + (g−n) + 2(4−g) = 10+2n−g`, so `g=2n+1` (S1 (5)).
* The `B→A` count, `9 = 3(g−n) + n + 2(4−g)`, gives the same.
* Since `0≤n≤g≤4`, `(g,n)∈{(1,0),(3,1)}`.

`g` is a property of the physical rows, so it is common to both pairs; then `n=(g−1)/2` is common too. This uses neither H5 nor I4.

Join counts, with `n_+` = the number of split rows with `F`'s direction:

* For `g=1`, the `F`-direction count is `1+n_+`, so H5 holds exactly when `n_+∈{1,2}`.
* For `g=3`, the count is `2+n_+(W)∈{2,3}`, so H5 holds automatically.

### A4. `g=1`: equations (6), involution (7), multisets (8)

`X` is the unique grouped row; by (5) its join opposes `F` in **both** pairs. `W_1,W_2,W_3` are split.

**Equations (6).** Collecting the squares of A2, per pair:

`J_BA = P_X^BA + Σ R_{W_i}^BA`, `J_AB = F_AB + C_X^AB + Σ L_{W_i}^AB` (S1 (6)),

as 0/1 matrix identities. Taking `p0=B`, `p1=A` for `X`: `C_X^AB=(a_X⁺,b_X⁰)` at `G` and `(a_X⁰,b_X⁻)` at `H`, with G/H taken relative to this pair first. It is coupled with the other pair as in A2 ✓.

**Involution (7).** Relabel `A` by `π_X^{-1}`, so that `P_X` becomes the diagonal of `B×B`. Its complement is the arc set of the complete digraph on the three vertices of `B`, i.e. two directed 3-cycles. Two arcs form a matching (distinct tails and distinct heads) exactly when they lie in the same directed 3-cycle or are reciprocal.

The partitions of the six arcs into three such pairs are:

* **(a)** the three reciprocal pairs;
* **(b)** one reciprocal pair `{x→z,z→x}`, with the remaining two arcs of each 3-cycle paired within it. There are three choices.

No other partition exists, because a 3-cycle cannot be split into within-cycle pairs alone. The omitted (tail, head) maps are:

* in (a), the identity;
* in (b), the transposition `(x z)` of the reciprocal pair's vertices, fixing the third vertex `y`. For example, `{x→y,y→z}` omits `(z,x)`, `{y→x,z→y}` omits `(x,z)`, and `{x→z,z→x}` omits `(y,y)`.

Each complement vertex has degree two, and each pair covers it at most once, so every vertex is omitted exactly once. Omitted tails are therefore distinct, and so are omitted heads. Hence:

* `τ:B→A` is a bijection;
* `π_X^{-1}∘τ` is the identity or a transposition, so `(π_X^{-1}∘τ)²=id_B` ✓ (S1 (7));
* at least one omitted pair is an edge of `P_X` ✓.

The four partitions follow the same pattern as the "four admissible pair partitions" of S2:23, which concerns a different setting. Nothing from that T14 argument is imported.

**Multisets (8).** Every tail has degree 3 in `J_AB`. The contributions at tail `a` are:

* `Σ L_{W_i}` gives degree `3−#{i:t_i=a}`;
* `F_AB` gives degree one at `a_1` and at `a_2`;
* `C_X^AB=(x,y)` gives degree one at `x`.

So `{t_1,t_2,t_3}={a_1,a_2,x}` as multisets. The heads give likewise `{h_1,h_2,h_3}={b_0,b_1,y}` ✓.

### A5. `g=3`: equations (9), third matching (10), multisets (11)

Per pair, `U` is the unique grouped row with `F`'s direction, `R` and `S` are the other grouped rows, and `W` is the split row. The identity of `U` may differ between pairs; all rows are the same physical cycles.

**Equations (9).** Collecting A2:

`J_BA = P_R + P_S + R_W + C_U^BA`, `J_AB = F_AB + P_U + L_W + C_R^AB + C_S^AB` (S1 (9)).

The counts are `3+3+2+1=9` and `2+3+2+1+1=9` ✓.

**Third matching (10).**

* `P_R` and `P_S` are disjoint permutation matchings, so `δ_RS:=π_R^{-1}π_S` is fixed-point-free, hence a 3-cycle.
* Their complement has one entry per row and per column: the matching `ρ=π_R δ_RS²`, taking the third value at each `b` ✓.
* `R_W` covers all tails except `u` and all heads except `v`, so the remaining entry of `ρ` is `(u,v)`.

Hence `C_U^BA=(u,v)` with `v=π_R(δ_RS²(u))` ✓ (S1 (10)).

**Multisets (11).** Removing `P_U` from `J_AB` leaves degree two everywhere. `F_AB` covers tails `a_1,a_2` and heads `b_0,b_1`; `L_W` covers all tails but `t` and all heads but `h`. Hence `{x_R,x_S}={a_0,t}` and `{y_R,y_S}={b_2,h}` ✓ (S1 (11)).

### A6. Chord tables (all four source/target × minority rows)

By §0 and `F`'s run, in each cell each of `α,β,γ,δ` is the double of exactly one zero-full row. This is S1 §4's premise ✓.

**Omitted vertices of a split row.**

* For double `e` in the source `A`, the omitted head in `A` of `R^BA` is `a⁺=head(e)` (sign `+`) or `a⁰=third(e)` (sign `−`).
* For double `e′` in the target `B`, the omitted tail in `B` is `b⁻=tail(e′)` (sign `+`) or `b⁰=third(e′)` (sign `−`).

With `(tail,head,third)` = `α:(1,0,2)`, `β:(2,1,0)`, `γ:(0,2,1)`, `δ:(2,0,1)`, this is exactly S1's split-edge table:

* source: `α 0/2, β 1/0, γ 2/1, δ 0/1`;
* target: `α 1/2, β 2/0, γ 0/1, δ 2/1` ✓.

**Distinctness per cell (A4).** All eight sign patterns of the three non-`X` arcs were checked. The surviving patterns, with signs listed in the order of the arcs shown, are:

| cell | `e_X=α` (`β,γ,δ`) | `e_X=β` (`α,γ,δ`) | `e_X=γ` (`α,β,δ`) | `e_X=δ` (`α,β,γ`) |
|---|---|---|---|---|
| source `A` | `+++`, `−+−` | `−−+`, `++−` | `−++`, `−−−` | `+++`, `−−−` |
| target `B` | `−−+`, `++−` | `+++`, `−+−` | `+−+`, `−−−` | `+++`, `−−−` |

Restricting to `n_+∈{1,2}` (H5) gives exactly S1's four rows ✓:

| cell, `n_+` | `(e_X, e_{unique split})` | unique split sign |
|---|---|---|
| source, `n_+=1` | `(α,γ)` or `(β,δ)` | `+` |
| target, `n_+=1` | `(α,δ)` or `(β,γ)` | `+` |
| source, `n_+=2` | `(β,δ)` or `(γ,α)` | `−` |
| target, `n_+=2` | `(α,δ)` or `(γ,β)` | `−` |

S1 §4's consequences 1–3 follow ✓:

* `X` never uses `δ`.
* Minority case: `X∈{α,β}`, and the unique `+` split row uses `γ`/`δ` in both cells.
* Majority case: in the source `X∈{β,γ}`, in the target `X∈{α,γ}`, and the unique `−` split row is pinned in both cells with one row identity.

As S1 states, these are per-cell necessary conditions only.

### A7. Shared-gap `g=3` subcase (13)

Use S1 §5's letters `A,B,C,D` for the cells of `F`'s runs, with joins `A→B` and `C→D`. The same `U` agrees with `F`, and the same split `W` opposes `F`, in both pairs.

* **`U` grouped in the gap from its `B` block to its `C` block.**
  * A2 gives `C_U^BA=(B_U⁺,A_U⁰)` and `C_U^DC=(D_U⁰,C_U⁻)`.
  * `W`'s omitted reverse pairs are `(B_W⁰,A_W⁰)` and `(D_W⁰,C_W⁰)`.
  * (10) forces `B_U⁺=B_W⁰`, `A_U⁰=A_W⁰`, `D_U⁰=D_W⁰` and `C_U⁻=C_W⁰`.
  * In cell `A`, the two doubles are distinct arcs on the same two vertices, hence reverse to each other. The only reverse pair among `α,β,γ,δ` is `{γ,δ}` ✓. Cell `D` is identical.
* **`U` grouped in the other gap.** `C_U^BA=(B_U⁰,A_U⁻)` and `C_U^DC=(D_U⁺,C_U⁰)`, which give opposite long chords in cells `B,C` ✓ (S1 (13)).

**Refinement:** the common singleton is the run middle. In the first case `A_U⁰=A_W⁰=a_1` and `D_U⁰=D_W⁰=d_1`; in the second, `B_U⁰=B_W⁰=b_1` and `C_U⁰=C_W⁰=c_1`.

### A8. Verdict on S1

Reconstructed at S1's exact stated scope:

* all displayed S1 identities (1)–(13);
* the grammar table, the omitted-pair table and the split-edge table;
* the four chord rows.

I found no mathematical discrepancy, no missing case, and no unjustified step outside the imports that S1 itself names.

Part B shows that the hypotheses of S1 §§3–5 are never simultaneously satisfied, so these necessary conditions hold vacuously. S1 never asserted nonemptiness (S1:212), so this does not contradict S1.

## Part B. New: one pair's actual square equations are unsatisfiable in both alternatives

### B1. Lemma 1 (mod-3 form of the actual doubles)

Let `r` be a zero-full row and `V∈{A,B}`. Put `t=ℓ(v_r⁻)`, and `ε=+1` if the double is `α`, `β` or `γ`, `ε=−1` if it is `δ`. Then `ℓ(v_r⁺)=t−ε` and `ℓ(v_r⁰)=t+ε`.

*Proof.*

* `α=1→0`, `β=2→1` and `γ=0→2` are the arcs of the directed 3-cycle `0→2→1→0`, so head `=t−1` and third `=t+1`.
* `δ=2→0` has head `0=t+1` and third `1=t−1`.
* The arcs `0→1` and `1→2` belong to `F`'s run and are not doubles of zero-full rows (§0). ∎

**Pure and mixed rows.** Call row `r` **pure** for the pair if `ε_r^A=ε_r^B`, and **mixed** otherwise. Put `κ_r=t_r^A−t_r^B`.

### B2. Lemma 2 (class table)

For an A-role `x` and a B-role `y`, `cl(a_r^x,b_r^y)=ℓ(a_r^x)−ℓ(b_r^y)`. Lemma 1 gives `ℓ(a⁻)=t_A`, `ℓ(a⁺)=t_A−ε_A` and `ℓ(a⁰)=t_A+ε_A`, and likewise for `B`. Using `2ε≡−ε` mod 3:

| role pair (A-role, B-role) | occurs in | class | pure (`ε_A=ε_B=ε`) | mixed (`ε_B=−ε_A=−ε`) |
|---|---|---|---|---|
| `(−,−)` | `P`, `R(−)`, `L(+)` | `κ` | `κ` | `κ` |
| `(+,+)` | `P`, `R(−)`, `L(+)` | `κ−ε_A+ε_B` | `κ` | `κ+ε` |
| `(0,0)` | `P` | `κ+ε_A−ε_B` | `κ` | `κ−ε` |
| `(0,+)` | `R(+)` [`b⁺→a⁰`], `C^BA` at `G` | `κ+ε_A+ε_B` | `κ−ε` | `κ` |
| `(−,0)` | `R(+)` [`b⁰→a⁻`], `C^BA` at `H` | `κ−ε_B` | `κ−ε` | `κ+ε` |
| `(+,0)` | `L(−)` [`a⁺→b⁰`], `C^AB` at `G` | `κ−ε_A−ε_B` | `κ+ε` | `κ` |
| `(0,−)` | `L(−)` [`a⁰→b⁻`], `C^AB` at `H` | `κ+ε_A` | `κ+ε` | `κ+ε` |

Here:

* `P` is the role-preserving permutation matching of a grouped row in its join direction (A2 (2));
* `R(±)` and `L(±)` are the split matchings of A2 (4);
* `C^BA` is the reverse square of a grouped row with join `A→B`, and `C^AB` that of a grouped row with join `B→A` (A2 (3)).

Consequences:

* **Pure row:**
  * `P` is **exactly one full class, `κ`**;
  * `R(−)` and `L(+)` lie in class `κ`;
  * `R(+)` lies in class `κ−ε`;
  * `L(−)` lies in class `κ+ε`;
  * `C^BA` lies in class `κ−ε` and `C^AB` in class `κ+ε`, **for both gap choices**.
* **Mixed row:** `P` meets each class exactly once, and each of `R(±)`, `L(±)` meets two distinct classes once each.
* **`F`:** `F_AB={[1,0],[2,1]}_AB` lies in class `1`, whose third pair is `[0,2]_AB`.

### B3. Lemmas 3–4

**Lemma 3.** In each of `A` and `B`, `δ` is the double of exactly one zero-full row, and `α,β,γ` are the doubles of the other three (§0). Hence exactly one of the following holds:

* one row has `δ` in both cells — it is pure, with `ε=−1` and `κ=2−2=0`; call it the **δ-row** — and the other three rows are pure with `ε=+1`;
* exactly two rows are mixed.

**Lemma 4.** If three rows are pure with `ε=+1`, their `κ` values are either all equal or pairwise distinct.

*Proof.* `α,β,γ` have tails `1,2,0`, so these rows' `t_A` values and their `t_B` values each run over ℤ/3. Thus `t_B=σ(t_A)` for a permutation `σ` of ℤ/3. Every permutation of ℤ/3 is `x↦x+c` or `x↦−x+c`. The first gives `κ=−c`, constant; the second gives `κ=2x−c`, taking all three values. ∎

### B4. Theorem 1 (`g=1` is empty)

**Statement.** Fix either opposite pair. If `g=1`, the 0/1 identity `J_BA = P_X + R_{W_1} + R_{W_2} + R_{W_3}` (A4) has no solution. No sign pattern, gap choice, H5 or other pair is used.

*Proof.* Each class has three `B→A` pairs. By Lemma 3 there are 0 or 2 mixed rows.

* **0 mixed.** `P_X` is one full class, and each `R_{W_i}` lies in one class. Each of the other two classes (3 pairs) would then be a disjoint union of 2-sets, which is impossible.
* **2 mixed, `X` mixed.**
  * `P_X` gives one pair to each class.
  * Exactly one `W` is mixed; it gives one pair to each of two classes.
  * The pure `W`s give 0 or 2 pairs to a class.

  Each class needs `3=1+m_c+even` with `m_c∈{0,1}`. This forces `m_c=0` for every class, contradicting the mixed `W`.
* **2 mixed, `X` pure.**
  * `P_X` fills class `c_X`.
  * Both mixed `W`s avoid `c_X`, so each gives exactly one pair to each of the other two classes.
  * The pure `W` gives 0 or 2 pairs to a class.

  A class `≠c_X` then has `1+1+(0 or 2)≠3` pairs. ∎

### B5. Theorem 2 (`g=3` is empty)

**Statement.** Fix either opposite pair. If `g=3`, the two identities

`J_BA = P_R + P_S + R_W + C_U^BA` and `J_AB = F_AB + P_U + L_W + C_R^AB + C_S^AB` (A5)

have no simultaneous solution. No gap choice, sign of `W`, H5 or other pair is used.

**Step 1 (no mixed rows; uses `B→A` only).**

* If `R` is pure and `S` mixed, or conversely, the pure one fills a class and the mixed one meets that class: a repeated pair.
* If both are mixed, then `U` and `W` are pure by Lemma 3. Each class has one remaining pair, but the pure `R_W` puts two pairs in one class.
* If both are pure, they fill two classes, and `R_W ∪ {C_U}` must be the third class. So `R_W` lies in one class and `W` is pure. Then at most `U` is mixed, contradicting Lemma 3's "0 or 2".

Hence all four rows are pure, and there is a δ-row `D∈{U,R,S,W}` with `ε_D=−1` and `κ_D=0`. The other three rows have `ε=+1`.

**Step 2 (class bookkeeping).**

* `B→A`: `P_R` and `P_S` are full classes `κ_R≠κ_S`. The third class `κ*` equals `R_W∪{C_U}`, so `cl(C_U)=κ_U−ε_U=κ*`.
* `A→B`: class 1 contains `F_AB`, so the full class `P_U` is not class 1, i.e. `κ_U≠1`. Let `c′` be the class `∉{1,κ_U}`.
  * The four pairs `L_W∪{C_R,C_S}` must be `[0,2]_AB` together with class `c′`.
  * `L_W` is two pairs of one class, so it lies in `c′`.
  * Therefore `{cl(C_R),cl(C_S)}={κ_R+ε_R, κ_S+ε_S}={1,c′}`.

**Step 3 (cases).**

* **`D=W`.** `U,R,S` have `ε=+1` and `κ_R≠κ_S`, so by Lemma 4 `κ_U,κ_R,κ_S` are distinct and `κ*=κ_U`. But `cl(C_U)=κ_U−1≠κ_U`.
* **`D=U`.** `cl(C_U)=0+1=1=κ*`. `R,S,W` have `ε=+1` and `κ_R≠κ_S`, so their `κ` values are distinct; hence `κ*=κ_W=1` and `{κ_R,κ_S}={0,2}`. Since `κ_U=0`, `c′=2`, and `{κ_R+1,κ_S+1}={1,0}≠{1,2}`.
* **`D=R`** (and symmetrically `D=S`). `cl(C_R)=0−1=2≠1`, so `c′=2` and `cl(C_S)=κ_S+1=1`, i.e. `κ_S=0=κ_R`. This contradicts `κ_R≠κ_S`.

All cases fail. ∎

### B6. Corollary and scope

**Corollary.** Assume H1–H4 and imports I1–I2, quantified as in §0. By A3, every configuration has `g∈{1,3}`, and Theorems 1–2 refute both alternatives for any one pair. Hence:

> **No actual T2(11) exists with two distinct tripled odd supports, `M=C`, synchronized `T=13` and full-count pattern `(4,0,0,0,0)`.**

The actual four-full T13 branch is empty. H5 and I4 are not needed.

**Reduction within the same imports.** By S2:13 (full counts `0,2,4`) and S3:30 (`G=4T−48=4` full runs), the only T13 full-count pattern left open is `(2,2,0,0,0)`. That reduction relies on those imports and is not re-proved here.

**What this does not say.**

* It constructs nothing.
* It is not a no-go for unrestricted T2(11).
* It does not touch `(2,2,0,0,0)`, `T=14`, `M≠C`, fewer than two tripled supports, or the imports' own proofs.
* It is not an inference from local fixture counts. It is a written proof that the exact equations, which hold on the same actual cycles, have no solution.
* It needs disjoint checking before adoption.

### B7. Disjoint cross-checks and illustrations (not load-bearing)

**(i) `g=1` via S1's own tables (A6), `n_+∈{1,2}`, all 16 completions.** `B→A` pairs are written `[ℓ(b),ℓ(a)]`.

| # | `(e_X^A,e_X^B)` | `n_+` | collision |
|---|---|---|---|
| 1 | `(α,α)` | 1 | `P_X` is the diagonal. The `−` row holding target `β` (`b⁻=2`) holds source `β` or `δ` (`a⁻=2`), so `[2,2]` repeats. |
| 2 | `(α,β)` | 1 | The `+` row is `(γ,γ)`, with `R(+)={[2,1],[1,0]}⊂P_X={[2,1],[1,0],[0,2]}`. |
| 3 | `(β,α)` | 1 | The `+` row is `(δ,δ)`, with `R(+)={[0,1],[1,2]}⊂P_X={[1,2],[0,1],[2,0]}`. |
| 4 | `(β,β)` | 1 | `P_X` is the diagonal. The `−` row holding source `α` (`a⁺=0`) holds target `α` or `δ` (`b⁺=0`), so `[0,0]` repeats. |
| 5 | `(β,α)` | 2 | The `−` row `(δ,δ)` gives `{[2,2],[0,0]}`. The `+` rows (`α,γ` × `β,γ`) give `{[1,2],[0,1]}⊂P_X` or `[2,2]` again. |
| 6 | `(β,γ)` | 2 | The `−` row `(δ,β)` gives `[1,0]∈P_X={[0,2],[2,1],[1,0]}`. |
| 7 | `(γ,α)` | 2 | The `−` row `(α,δ)` gives `[2,1]∈P_X={[1,0],[0,2],[2,1]}`. |
| 8 | `(γ,γ)` | 2 | `P_X` is the diagonal. The `+` row holding source `β` (`a⁰=0`) holds target `α` or `δ` (`b⁺=0`), so `[0,0]` repeats. |

The excluded `n_+∈{0,3}` completions of the same tables also each fail. For example:

* `n_+=3, (α,β)`: `[1,1]` is covered by nothing;
* `n_+=0, (γ,γ)`: target vertex `0` cannot receive both `[0,1]` and `[0,2]`;
* the `(δ,δ)` cases fail by the parity argument of Theorem 1.

All of this agrees with Theorem 1.

**(ii) `g=3` written illustrations.** These are fresh instances chosen to test Lemma 2; arcs are listed as `(source cell, target cell)`.

* **`D=U`:** `U=(δ,δ)` at `H`, `R=(γ,α)`, `S=(β,β)`, `W=(α,γ)` with sign `−`.
  * The `B→A` identity holds exactly: `P_R={[1,0],[0,2],[2,1]}`, `P_S` is the diagonal, `R_W={[0,1],[2,0]}`, and `C_U=[1,2]`.
  * The `A→B` identity fails: `P_U` is the diagonal, and `C_R∈{[2,2],[1,1]}_AB⊂P_U` for either gap.
* **`D=W`:** `U=(γ,γ)`, `R=(α,β)`, `S=(β,α)`, `W=(δ,δ)`.
  * `P_R` and `P_S` fill classes 2 and 1.
  * `R_W(+)={[0,1],[1,2]}` meets `P_S`, and `R_W(−)={[2,2],[0,0]}` omits `[1,1]`.
  * But `C_U∈{[2,1],[1,0]}`, which lies in class 2.
* **`D=R`:** `U=(γ,α)` at `G`, `S=(α,β)`, `W=(β,γ)` with sign `+` (all `κ=2`).
  * The `B→A` identity holds exactly, with `C_U=[0,1]`.
  * The `A→B` identity fails: `L_W(+)={[2,0],[1,2]}_AB⊂P_U={[0,1],[2,0],[1,2]}_AB`.

These are consistent with B5. They are illustrations, not proof, and no code was run.

## C. Result limits

* **Part A.** Every identity is a necessary condition at S1's scope. By Part B those hypotheses are inconsistent, so the systems are vacuous. Part A reports no S1 error.
* **Part B.** This is a conditional branch exclusion under H1–H4 and I1–I2. It is not:
  * an array;
  * an unrestricted no-go;
  * a proof of `M=C`;
  * a statement about `(2,2,0,0,0)`, `T=14`, `M≠C` or fewer tripled supports.

  The bodies behind I1 and I2 (the f461/f474/f475/f476 chain and the synchronized third-cut disposition) were not opened and remain named imports.
* **Status.** This is an author candidate only:
  * no independent-family, human, formal or kernel review;
  * no novelty or publication-priority claim;
  * parent disposition is separate.

## D. Read, process and execution declaration

**Clock.** Native clock `2026-10-31T03:01:41Z` before the prebody ACK, and `2026-10-31T03:22:56Z` immediately before this file's first write.

**Administrative reads, all before any mathematical body.** I completely read:

| item | how it was read |
|---|---|
| manifest | non-raw display, then raw lines 8–201 to recover elided nested blocks |
| freeze receipt | raw lines 10–186, after a non-raw display |
| final binding | raw lines 16–173, after a non-raw display |
| parent-live metadata | raw lines 22–198, after a non-raw display |
| actual-dispatch receipt | complete in one display, 47 LF |
| all 22 status-only controls | each in full, raw |

* The elisions were display folding of nested JSON, recovered before the ACK. They were not packet clipping.
* Live `shasum -a 256` values of the manifest, receipt, binding, metadata, packet and all 22 controls equal their pins. The dispatch receipt is `32a3dee0d6ac9bfaf300766fa3c3c56a4f54a19d24c592aafd5a3906cb1d5737`.
* Controls were used for status and permissions only; all held episodes and all their consumers stayed NONINPUT.
* `prebody-ack-v1.md` (3316 bytes) was written and a direct PREBODY ACK was delivered to Main before the packet body was opened.

**Packet part 01** (`ed1de2c5c950d77d9ca438546879b7891d28fb141c7899623fcef421ffd5d627`, 40586 bytes, 322 LF; S1 complete 221 lines, S2 complete 51 lines, S3 complete 36 lines). It was read serially in these raw windows:

| window (LF) | bytes | | window (LF) | bytes |
|---|---|---|---|---|
| 1–20 | 3600 | | 161–180 | 2060 |
| 21–40 | 1517 | | 181–200 | 2156 |
| 41–60 | 1018 | | 201–220 | 2382 |
| 61–80 | 847 | | 221–240 | 4251 |
| 81–100 | 1285 | | 241–260 | 3800 |
| 101–120 | 2256 | | 261–280 | 5803 |
| 121–140 | 1607 | | 281–300 | 2187 |
| 141–160 | 1267 | | 301–322 | 4550 (22 LF) |

* Every display was below 30000 bytes. The ending and terminal LF were observed, and no clipping occurred.
* Mathematical derivation began after the complete ordered read.
* I did not open the S1–S3 source paths separately; their bodies were read only as reproduced in the packet.

**PROCESS MINOR (parent ruling, Main IRC, applied without backdating).** The final raw window, packet lines 301–322, was 22 LF. That exceeds the 20-LF raw-window cap by two lines. It is one author packet-window process minor, not a mathematical finding.

**Shell utilities (metadata only).** I used `date`, `ls`, `shasum`, `wc`, and one byte-count loop that piped `sed -n` for each of the sixteen window ranges into `wc -lc`. That loop displayed only counts, never packet text. A terminal-byte check, `tail -c 1 … | od -c | head -1`, displayed exactly one packet byte: offset 40585 (0-based), value LF, the terminal newline after packet line 322 (S3:36). No other packet byte was displayed outside the ordered raw pass. A status-only disclosure of the window and the utilities was sent to Main after the packet read, and Main's ruling was received and applied.

**Not opened, not used.**

* No linked or unlisted bodies. Every file named in S2/S3 stays unopened, including f641, f656, f657, f658, f461, f474, f475, f476 and the synchronized third-cut disposition.
* No held episode or consumer, no sibling output, no network, no external model.

**No execution.**

* No code execution, test, compilation, solver, scientific eval or child scientific process.
* No verifier was prepared, because the scope did not request one. **Prepared-code hash: NONE.**
* The written instances in B7(ii) and the explicit sign enumerations are author-chosen written cases under the prospective general-author method scope. None was executed.

**Writes.** Exclusive writes, only in this wave directory: `prebody-ack-v1.md` and this `author-candidate-v1.md`.

* Each path was checked absent by directory listing immediately before its first write. The write tool exposes no `O_EXCL` flag; this is a process qualification.
* No frozen file was edited. No delete, Git, cleanup, build, lint, test or formatter was run.
