# Author candidate: simultaneous square-complement and chord restrictions in the actual T13 four-full branch

**Status:** prospective written GENERAL AUTHOR candidate, not an adopted disposition. This gives explicit necessary invariants for **both** grouped subbranches of the whole surviving `(4,0,0,0,0)` T13 branch, not a no-go or a construction. All objects in each assertion below belong to the same eleven-row array and the same five labeled connected residual twelve-cycles. The independent review and parent disposition are separate.

## 1. Exact scope and conditional imports

Quantify over any actual T2(11), any two distinct odd-position six-supports each appearing in three of its rows, and the same array's actual missing linear distance-two set `M` and closing set `C`. Assume **`M=C`**, the synchronized `T=13` interface, and that the five actual residual cycles have full-cell-count pattern `(4,0,0,0,0)`. Assume also that each opposite-cell pair has surviving join split `2:3` or `3:2`. The two distinguished supports need not be claimed to be the only tripled supports. The conclusion is simultaneous for both opposite pairs.

The load-bearing **conditional imports** from the two complete literal source bodies are:

* **I1 — actual augmentation and square partition** (S1:11–15): adjoining the same infinity gives eleven connected directed Hamilton twelve-cycles that partition all directed adjacency arcs; under the explicit `M=C` assumption, their directed squares also partition all directed arcs. Opposite cells lie on different sides of both distinguished cuts, so no square of one of the six cut-alternating cycles joins opposite cells. Consequently the five *same* residual cycles use each of the nine directed squares between each oriented opposite pair exactly once.
* **I2 — synchronized residual structure** (S1:13,17; S2:17–30): the two supports give four three-vertex cells, opposite in pairs. In T13 every residual cycle is regular, with exactly one join per opposite pair, whose endpoints are in nontrivial cell runs; over the five residual cycles each cell has one length-three run and four length-two-plus-singleton layouts. In the specified branch the unique four-full row is denoted `F`; the other four rows have no full cell.
* **I3 — physical singleton transport** (S1:15–17): every zero-full row has its four singleton runs either all in one gap or two in each gap between its two opposite-pair join blocks, and a singleton's neighbors lie in the two opposite cells of the other pair. This is a statement about consecutive vertices in the actual connected cycle, not independent schedules. The packet gives the counting rationale; its linked, unlisted source bodies are not opened here.
* **I4 — optional whole-branch reduction** (S1:29–35): the stated exclusion of `4:1` and `1:4` joins in this full-count pattern invokes the packet's four-case endpoint exhaustion whose complete author proof is not in the literal packet. If one wishes to drop the explicitly stated `2:3`/`3:2` hypothesis, that exclusion is a **named conditional import**, not independently reproved here. None of the results below needs it when the displayed split is assumed.

The source packet itself is not a proof of `M=C`, existence of an array, or the original unrestricted no-go. In particular `(2,2,0,0,0)`, `T=14`, `M≠C`, and fewer than two tripled supports are not decided here.

## 2. One-cycle grammar and actual square pairs

For one ordered opposite pair write its cells `A,B`, and orient the names so that the join in `F` is `A→B`. Write the full runs of the **actual** `F` as

\[
 a_0\to a_1\to a_2,\qquad b_0\to b_1\to b_2.
\]

Thus the `A→B` join of `F` contributes the two squares

\[
 F_{AB}=\{(a_1,b_0),(a_2,b_1)\}. \tag{1}
\]

There is no `B→A` square of `F`: it has neither a reverse join nor singleton centers. For each zero-full row `r`, write its unique internal double in a cell `V` as `v_r^-→v_r^+`, and its other vertex as `v_r^0`. These refer to actual labeled vertices, not copies chosen independently per pair. Let `+` mean the `A→B` join and `−` the `B→A` join in that row.

To derive the subsequent formulas, let a zero-full cycle's two actual join blocks be `p0 p1` and `q0 q1`, where the letters designate cells and each block consists of two double runs; both arrows are read in cycle orientation. Let `G` be the gap from the end of the `p1` double to the start of the `q0` double, and `H` the other gap from `q1` to `p0`. Superscript `0` below denotes the singleton of a cell. I3 forces exactly these singleton strings:

| row kind | `G` | `H` |
|---|---|---|
| grouped at `G` | `q0⁰ p0⁰ q1⁰ p1⁰` | empty |
| grouped at `H` | empty | `p0⁰ q0⁰ p1⁰ q1⁰` |
| split | `q1⁰ p0⁰` | `p1⁰ q0⁰` |

Indeed, the two neighbors of each singleton must be opposite cells of the other pair, successively forcing every displayed letter; the remaining singletons must each be used once. This also verifies all cyclic endpoints, including an empty gap.

A grouped row with join `p0→p1` therefore contributes the following **full permutation matching** in that direction:

\[
 P_r^{p0,p1}=\{(p0_r^-,p1_r^-),\ (p0_r^+,p1_r^+),\ (p0_r^0,p1_r^0)\}. \tag{2}
\]

The first two are the join-centered squares, the third is centered at a singleton of the other pair. Its one square in the reverse direction is

\[
 C_r^{p1,p0}=\begin{cases}
 (p1_r^+,p0_r^0),&\text{grouped at }G,\\
 (p1_r^0,p0_r^-),&\text{grouped at }H.
 \end{cases} \tag{3}
\]

For the other join `q0→q1`, **the same physical gap choice** gives the reverse square `(q1⁰,q0⁻)` at `G` and `(q1⁺,q0⁰)` at `H`. Thus the two pairwise choices of (3) cannot be made independently.

A split row `r` contributes the following two-edge matchings in the two directions:

\[
 L_r^{AB}=\begin{cases}
 \{(a_r^-,b_r^-),(a_r^+,b_r^+)\},&r\text{ has }+,\\
 \{(a_r^+,b_r^0),(a_r^0,b_r^-)\},&r\text{ has }-,
 \end{cases}\qquad
 R_r^{BA}=\begin{cases}
 \{(b_r^+,a_r^0),(b_r^0,a_r^-)\},&r\text{ has }+,\\
 \{(b_r^-,a_r^-),(b_r^+,a_r^+)\},&r\text{ has }-.
 \end{cases} \tag{4}
\]

Each displayed two-edge set has distinct tails and distinct heads. Its omitted tail/head pair is respectively

| row sign | omitted by `L_r^{AB}` | omitted by `R_r^{BA}` |
|---|---|---|
| `+` | `(a_r⁰,b_r⁰)` | `(b_r⁻,a_r⁺)` |
| `−` | `(a_r⁻,b_r⁺)` | `(b_r⁰,a_r⁰)` |

These identities are direct two-step readings of the cyclic vertex strings, including the cases in which the singleton is adjacent to a double run. No global array is constructed by writing them.

## 3. Both grouped cases and exact same-cycle complement equations

Let `g` be the number of grouped zero-full rows. For either opposite pair orient `F` as `A→B` and let `n` be the number of grouped rows with the same orientation. Counting `A→B` squares via (1)–(4) gives

\[
 9=2+3n+(g-n)+2(4-g)=10+2n-g,
 \quad\text{hence}\quad g=2n+1. \tag{5}
\]

Thus **exactly one or exactly three** of the four zero-full cycles are grouped. This `g` is the same for both pairs because it describes the same physical singleton gaps.

Regard each pair set below as its `3×3` zero-one matrix and `J` as the all-one matrix. Equalities are integer matrix equalities, so in particular no entry is repeated. They hold simultaneously for both pairs, with common row identities and common actual vertices.

### `g=1`: three split cycles

Let `X` be the unique grouped row and `W1,W2,W3` the same three split rows. Equation (5) forces `X` to join against `F` **in both opposite pairs**. For each pair,

\[
 J_{BA}=P_X^{BA}+\sum_{i=1}^3 R_{W_i}^{BA},\qquad
 J_{AB}=F_{AB}+C_X^{AB}+\sum_{i=1}^3 L_{W_i}^{AB}. \tag{6}
\]

Here `P_X` is the matching (2) for the actual `B→A` join of `X`, and `C_X` is its actual reverse singleton square from (3). In the `G/H` convention of Section 2 with this pair first, `C_X` is respectively `(a_X⁺,b_X⁰)` or `(a_X⁰,b_X⁻)`; the corresponding choice for the second pair is coupled as stated after (3).

**Involution invariant.** Let `π_X:B→A` be the bijection represented by `P_X`. For each split row let `(u_i,v_i)` be the omitted tail and head of its actual `R_{W_i}^{BA}`, as in the table after (4). The three `u_i` are all distinct and the three `v_i` are all distinct. Consequently `τ(u_i)=v_i` defines a bijection `τ:B→A`, and necessarily

\[
 \boxed{\ (\pi_X^{-1}\circ\tau)^2=\mathrm{id}_B.\ } \tag{7}
\]

Equivalently, the relative permutation is the identity or a transposition, never a three-cycle. In particular at least one split row's omitted pair is itself an edge of `P_X`. This must hold for each of the **two** opposite pairs using the same `X` and `W1,W2,W3`, not separate freely chosen rows.

Proof: remove the permutation matching `P_X` from `K_{3,3}`. The six remaining entries form a bipartite six-cycle, partitioned by (6) into the three actual two-edge matchings `R_{W_i}`. Relabel the head side by `π_X^{-1}`. The six off-diagonal entries are the two directed three-cycles. Within one three-cycle any two edges form a matching; a cross-cycle pair is a matching only when its edges are reciprocal. A partition into pairs therefore has either three reciprocal pairs, whose omitted matching is the identity, or one reciprocal pair and one pair from each directed three-cycle, whose omitted matching is a transposition. Each remaining graph vertex has degree two, proving the distinct omitted tails and heads. This proves (7), not merely a parity heuristic.

There is also a **coupled forward-degree identity**. If `C_X^{AB}=(x,y)` and `(t_i,h_i)` is the omitted tail/head of `L_{W_i}^{AB}`, then

\[
 \{t_1,t_2,t_3\}_{\rm multi}=\{a_1,a_2,x\}_{\rm multi},\qquad
 \{h_1,h_2,h_3\}_{\rm multi}=\{b_0,b_1,y\}_{\rm multi}. \tag{8}
\]

Indeed, in (6) each split matching uses every tail except its omitted tail, and the full matrix has degree three at every tail; the contributions of `F` and `C_X` are precisely the right-hand multiset. The head identity is identical. Equations (7) and (8) must both use the same row-by-row `+`/`−` choices and actual vertices, with (3)'s shared-gap coupling across the two pairs.

### `g=3`: one split cycle

Let `W` be the unique split row. For a given opposite pair, (5) gives a **unique** grouped row `U` that joins in the same direction as `F`; the other grouped rows `R,S` join in the reverse direction. The identity of `U` may differ between the two opposite pairs, but all three grouped rows and `W` are the same actual cycles. The exact equations are

\[
 J_{BA}=P_R^{BA}+P_S^{BA}+R_W^{BA}+C_U^{BA},\qquad
 J_{AB}=F_{AB}+P_U^{AB}+L_W^{AB}+C_R^{AB}+C_S^{AB}. \tag{9}
\]

Let `π_R,π_S:B→A` be the two reverse grouped matchings. Since they are disjoint, `δ=π_R^{-1}π_S` is a fixed-point-free permutation of three vertices and hence a three-cycle. Their complement is the third perfect matching `ρ=π_Rδ²`. If `(u,v)` is the omitted tail and head of the actual `R_W^{BA}`, then

\[
 \boxed{\quad C_U^{BA}=(u,v),\qquad v=\pi_R\bigl(\delta^2(u)\bigr).\quad} \tag{10}
\]

The proof is simply that two disjoint permutation matrices leave exactly one entry in each row and column; the two entries of `R_W` and the one actual square `C_U` must form that third matching. This is stronger than a count of three squares: it pins both endpoints of `C_U` to omitted vertices of the **same** split cycle.

There is a corresponding forward-degree identity. Let `(t,h)` be the omitted pair of `L_W^{AB}`, and write `C_R^{AB}=(x_R,y_R)`, `C_S^{AB}=(x_S,y_S)`. Removing the perfect matching `P_U` from the second equality in (9) leaves degree two at every tail and head. Therefore

\[
 \{x_R,x_S\}_{\rm multi}=\{a_0,t\}_{\rm multi},\qquad
 \{y_R,y_S\}_{\rm multi}=\{b_2,h\}_{\rm multi}. \tag{11}
\]

These equations too are simultaneous for both opposite pairs; `(10)` cannot be satisfied by relabeling a separate copy of `W` for the second pair.

## 4. New directed-arc chord restrictions

The following are consequences of (6), the physical `2:3`/`3:2` split, and directed adjacency uniqueness, not extra assumptions.

For any cell of `F`, label its full run `0→1→2`, and abbreviate the four directed arcs not used by this full run as

\[
 \alpha=1\to0,\qquad\beta=2\to1,\qquad
 \gamma=0\to2,\qquad\delta=2\to0. \tag{12}
\]

Each of these four arcs occurs **once** as a double run among `X,W1,W2,W3`: the six alternating cycles have no internal cell arc, the full run uses two distinct internal arcs, and I1 partitions all six directed internal-cell arcs. Let `n_+` be the number of split rows whose join has the same `A→B` direction as `F`. Because the joins have split `2:3`/`3:2` and `X` is negative, `n_+` is 1 or 2. The following table gives every possibility not already ruled out by the distinct omitted vertices in (7). `e_X` is the actual double edge in that cell; the second column of each set gives the double edge of the unique split row with the indicated minority sign.

| cell / `n_+` | necessary `(e_X, e_{unique split})` choices |
|---|---|
| source `A`, `n_+=1` | `(α,γ)` or `(β,δ)`; unique split sign `+` |
| target `B`, `n_+=1` | `(α,δ)` or `(β,γ)`; unique split sign `+` |
| source `A`, `n_+=2` | `(β,δ)` or `(γ,α)`; unique split sign `−` |
| target `B`, `n_+=2` | `(α,δ)` or `(γ,β)`; unique split sign `−` |

In particular:

1. **The unique grouped row `X` never uses `δ=2→0` in any of the four cells.** The reverse long chord of each actual full run is used by one of the three same split cycles.
2. If `F` is on the minority side of a pair's `2:3` join split (`n_+=1`), then in **both** cells of that pair `X` uses the reverse of a consecutive edge of the full run, `α` or `β`. The one split row joining in `F`'s direction uses a long chord `γ` or `δ` in **both** cells. If `F` is the minority on both opposite pairs, these restrictions apply to all four cells; the unique positive split row for one pair may be the same physical row as, or different from, that for the other pair.
3. If `F` is on the majority side (`n_+=2`), the source-cell edge of `X` is in `{β,γ}` and the target-cell edge is in `{α,γ}`. The table additionally pins the double edge of the unique negative split row, with the **same row identity at both endpoints**.

Proof of the table: by (7), the three omitted heads in `A` of `R_W` are distinct and the three omitted tails in `B` are distinct. In the notation (12), for an edge in a split row the possible omitted vertex is

| split edge | omitted head in source `A`, sign `+` / `−` | omitted tail in target `B`, sign `+` / `−` |
|---|---|---|
| `α` | `0 / 2` | `1 / 2` |
| `β` | `1 / 0` | `2 / 0` |
| `γ` | `2 / 1` | `0 / 1` |
| `δ` | `0 / 1` | `2 / 1` |

For each proposed `e_X`, the three remaining edges are assigned to the three split rows. Reading the table with one or two `+` signs and demanding three distinct omitted vertices gives precisely the four rows of the preceding table. For example, if `e_X=δ`, the remaining edges are `α,β,γ`; their all-`+` and all-`−` omissions separately permute the three vertices, but mixing signs makes a collision. Both uniform signs are excluded by `n_+∈{1,2}`. The other entries follow by the same explicit three-edge check. This proof checks each cell separately only to obtain necessary restrictions; their row/sign assignments must subsequently agree between the two cells and between both opposite pairs.

## 5. A shared-gap chord constraint in the `g=3` branch

There is an additional genuinely joint special case, derived from (10), not from a relaxed row fixture. Orient and cyclically name the four full runs of `F` as `A,B,C,D`, with the two joins `A→B` and `C→D`. Suppose the **same** grouped row `U` is the unique grouped row matching `F` in both pairs, and the unique split row `W` opposes `F` in both pairs. This is a subcase of, not an assertion about, all `g=3` configurations.

If `U` is grouped in the gap from its `B` block to its `C` block, (3) gives its reverse singleton squares

\[
 B_U^+\to A_U^0,\qquad D_U^0\to C_U^-.
\]

Since `W` has reverse joins in both pairs, its omitted reverse-square pairs in (10) are `(B_W⁰,A_W⁰)` and `(D_W⁰,C_W⁰)`. Equality forces `A_U⁰=A_W⁰` and `D_U⁰=D_W⁰`. The actual double arcs of `U` and `W` in each of cells `A,D` use the other two vertices and are distinct; hence they are reversals. The only pair of mutually reversed arcs not used by `F` is `{γ,δ}` from (12). Thus `U` and `W` use the two opposite long chords in each of `A,D`.

If instead `U` is grouped in the other gap, its reverse singleton squares are `B_U⁰→A_U⁻` and `D_U⁺→C_U⁰`; the same reasoning forces the opposite-long-chord conclusion in cells `B,C`. Hence

\[
 \boxed{\text{under these stated simultaneous signs, }U,W\text{ use opposite long chords in }\{A,D\}\text{ or }\{B,C\},}
 \tag{13}
\]

with the choice determined by their **one physical grouped gap**. The remaining endpoint equalities in (10) also remain necessary. This uses connected cyclic words and both pairs together; it does not assert that either choice extends to an actual array.

## 6. What has and has not been established

Equations (6)–(11) and the arc tables apply to **all** actual `(4,0,0,0,0)` survivors with the stated `2:3`/`3:2` joins, split into the exhaustive `g=1` and `g=3` alternatives. They provide simultaneous actual-vertex invariants, including a relative-permutation involution, a forced third matching, physical shared-gap endpoint identifications, and full-path chord restrictions. They do not prove that either alternative is nonempty, that the displayed necessary systems are sufficient, or that any candidate satisfying them extends to the other six actual cycles. Full directed adjacency uniqueness between different cells and all other square classes remain necessary even if the displayed opposite-pair equations happen to hold.

There is no inference from the packet's one-lift zero count, relaxed fixtures, or local positive controls to a physical obstruction. No global no-go, original-source equivalence, publication priority, family/human/formal/kernel acceptance, or novelty claim is made. The full-count pattern `(2,2,0,0,0)` and all outside-scope branches remain unresolved here.

## 7. Read, process, and execution declaration

* Before mathematical-body access or reasoning I read the complete manifest, freeze receipt, final binding, parent-live metadata, actual-dispatch receipt, and all 22 controls listed in the manifest, using the controls **only** for administrative status/permissions. I wrote `prebody-ack-v1.md` and sent a direct prebody acknowledgment to Main before reading the packet. The actual-dispatch receipt identifies `AuthorF853TuscanT13` and the ordered part.
* I read the complete sole literal packet part serially in raw windows `1–15`, `16–30`, `31–45`, `46–60`, `61–75`, `76–90`, `91–97`, including its ending and complete S1/S2 bodies. The entire part is parent-pinned as 18,447 bytes, so each display was below 30,000 bytes; each window was at most 15 LF. No packet clipping was observed. S1 is parent-pinned SHA256 `5b54fedca445f0af3148176de04ee87574f47938d932d973544e2f8321493f6a`; S2 is `c82b00df7bb8fc2d3a8eb9cc3e2b841f4464314d6b471586c4a833e846c30c60`; the part is `be2a1135ad1839fb9874b75a22a95fdc1eeb7a3ce9bee08ac338828e1ab64c01`. These are supplied metadata, not independently recomputed hashes or a provenance certificate.
* Initial non-raw administrative displays elided nested fields and truncated the dispatch-summary line; I recovered the complete administrative documents with raw windows before acknowledgment. This was not packet clipping. The write tool available here does not expose an atomic exclusive-create flag: I checked each new acknowledgment/candidate path absent immediately before its first write, and no sibling has ownership of this wave directory. This is a process qualification, not a claim of atomic `O_EXCL`.
* I did not open linked or unlisted mathematical source bodies, held episodes or their consumers, use network or an external model, run child processes, execute code, tests, solvers, builds, scientific evaluations, or prepare a verifier. Thus there is no prepared-code hash and no executed scientific check. The reasoning above is a written author derivation conditioned on the identified imports; it awaits disjoint checking.
