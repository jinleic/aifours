# Synchronized cuts and both parity obstructions for the actual 4444 tensor

**Prospective GENERAL AUTHOR candidate; conditional, nonblind, same harness.** This is not a parent disposition or a family, human, formal, kernel, priority, or novelty claim. The exact conditional result proved below is:

> Let `ψ` be one normalized complex four-party AME(4,6) tensor in one fixed product basis, `U=6ψ`, with exactly 50 nonzero entries, exactly 26 of modulus one, and residual E alphabet size four at each party. Suppose, for **every one of the six physical pair systems**, no E pair value has multiplicity four; and at **every** party the two surplus-two E symbols have degree three while the other two E symbols have surplus zero and degree two. Then such a tensor does not exist.

The assumptions are simultaneous properties of that one tensor, not independent cut choices. In particular, this document does **not** prove the earlier f860 claims that every 4444 tensor satisfies the full no-F and surplus/degree assumptions. Those are named conditional imports if one tries to deduce an unconditional 4444 exclusion. The derivation below independently supplies the T line counts, the complete relevant X/Y cut classification, synchronization, both binary parity obstructions, and their actual shared-symbol incidence. No source-linked unlisted proof body or computation is imported.

## 1. Actual words, lines, surplus and all six T systems

Let the parties be `A,B,C,D`. The three balanced flattenings of `U` are 36-by-36 unitaries. Let `P` be the same 26 modulus-one words in all cuts, and `E` the other 24 nonzero words. A modulus-one unitary entry exhausts its whole row and column. Thus, for every physical pair `ij`, the 26 P pair values are distinct and E uses precisely the remaining ten pair values. Every used E pair value has at least two extensions: a lone nonzero in a residual unitary row would itself have modulus one. A word is determined by its two complementary pair values, so each residual matrix entry is one actual E word, not a multiplicity or an abstract mask.

At party `i`, let `Q_i` be its four E-used symbols and, for `x∈Q_i`, let `d_i(x)` count its E-neighbors at any other party; this degree is independent of the other party because its number of P occurrences is `6-d_i(x)`. Let `s_i(x)` be the number of E words containing x and `h_i(x)=s_i(x)-2d_i(x)`. Denote the two surplus-two, degree-three symbols by `H_i` and the other two, surplus-zero, degree-two symbols by `L_i`. Thus

```
s_i(x)=8  (x∈H_i),             s_i(x)=4  (x∈L_i).                 (1)
```

Let `m_ij(x,y)` be the number of E extensions of an E-used pair value `(x,y)`. For each symbol,

```
Σ_{y:(x,y) used} (m_ij(x,y)-2) = h_i(x).                         (2)
```

All terms are nonnegative. Consequently every pair line incident with a low symbol has multiplicity exactly two, and every line has multiplicity at most four. The no-F hypothesis excludes four; hence the only possibilities are two and three. A multiplicity-three line has high symbols at both endpoints. Each high symbol has surplus two and thus meets both opposite high symbols in multiplicity-three lines. Therefore in **each** of AB, AC, AD, BC, BD, CD the four high-high values `H_i×H_j` occur three times each, and all six other used pair values occur twice. In particular every high symbol has both high symbols and exactly one low symbol as its neighbors at each other party; every low symbol has exactly two neighbors. We call these the six T systems.

## 2. Reconstructing the complete T/T cut masks from actual unitarity

Fix any of the three complementary cuts. Delete the isolated P rows and columns. The remaining square unitary has ten rows and ten columns, four degree-three and six degree-two lines on each side. The four degree-three rows are exactly `H_i×H_j`, and the four degree-three columns exactly `H_k×H_l`. Row and column inner products prohibit two distinct lines from having exactly one common nonzero.

For a degree-two row r with neighboring columns p,q, every other row meets either both p,q or neither; otherwise it overlaps r in exactly one position. Hence p,q have identical row neighborhoods and the same degree. If that degree is two, the two columns form a 2-by-2 unitary supported on their two common rows. Orthogonality to both columns forces every other column to vanish on those rows, so this is an isolated full 2-by-2 component. If p,q have degree three they form a high-column twin pair. Two distinct degree-two rows cannot share such a pair: their two orthonormal rows would span the two columns, forcing their column degrees down to two. Distinct twin pairs are disjoint, since any common column has the same neighborhood as its partner.

Let k be the number of degree-two rows meeting high columns. There are only four high columns, so `k≤2`; all other degree-two rows belong to disjoint isolated 2-by-2 components, so `6-k` is even. Therefore `k=0` or `k=2`.

* **k=0 (Y).** The six low rows and six low columns form three isolated 2-by-2 blocks. The remaining four high rows and columns each have degree three, so their 4-by-4 block has exactly one zero in every row and column: the missing positions form a permutation. This is a 12-entry Y core.
* **k=2 (X).** The two low rows use disjoint high-column twin pairs, together exhausting all four high columns. Each pair has one low and two high row neighbors. The two two-element high-row neighbor sets are disjoint, because a degree-three row cannot meet both complete twin pairs; together they exhaust all four high rows. Four other low rows and four low columns make two isolated 2-by-2 blocks. Each of the four high rows has one remaining edge, necessarily to one of the two remaining low columns: it cannot meet just one column in the other twin pair. A low column meeting one row of a high-row twin pair must meet both, or it would overlap one of their high columns once. Hence each high-row pair shares one low column. The result is two 3-by-3-minus-one components, with two high rows, two high columns and one low row and low column each, plus two isolated 2-by-2 blocks. Each 3-by-3 block has its sole zero at the low-row/low-column intersection; its high-high 2-by-2 subblock is full.

These arguments classify the actual supports under the stated assumptions, including the equality cases, without assuming a graph-only mask is realizable. They also explain where complex phases enter: only the unitary consequences just proved are used.

### Local phase and equality alternatives

No equal-modulus or real-phase hypothesis is made. For completeness, an arbitrary full-support unitary 3-by-3-minus-one component, after permitted **local row and column phase choices for that one component**, can be written as

```
[ e^(iχ) sinφ sinθ   -e^(iχ) sinφ cosθ    cosφ ]
[-e^(iχ) cosφ sinθ    e^(iχ) cosφ cosθ    sinφ ]      (3)
[          cosθ                 sinθ          0  ]
```

with `0<θ,φ<π/2` and arbitrary real χ. To see this, make the two low-row entries and two low-column entries positive. Write them respectively as `(cosθ,sinθ)` and `(cosφ,sinφ)`. Each high row's first two entries is a scalar multiple of `(sinθ,-cosθ)`; the two high-row norms and their inner product give exactly (3). The strict inequalities are necessary for the stipulated full eight-entry support; endpoint angles belong to different, sparser components. In particular the high-high 2-by-2 determinant is zero, but its nonzero magnitudes are not assumed equal. A full 2-by-2 unitary has the analogous nonzero-angle freedom and arbitrary row/column phases. These per-component gauges need not be compatible across cuts, and are not treated as independent phases of a tensor.

Y cannot be discarded merely as an impossible single-cut unitary: for example, after row/column permutations its core can be the following real conference matrix divided by `√3`, with three full 2-by-2 unitary blocks beside it:

```
 0  1  1  1
-1  0  1 -1
-1 -1  0  1
-1  1 -1  0
```

The following Y contradiction uses the three cuts of the **same** word set and excludes every possible phase realization, not only this example.

## 3. The same Ω synchronizes all cuts; Y is impossible

Set

```
Ω = E ∩ (H_A × H_B × H_C × H_D).                                  (4)
```

For any cut `ij|kl`, its four high rows and four high columns are precisely the corresponding high pair values. Each entry in their intersection is the same actual all-high E word, and conversely. In an X cut the intersection is the union of the two full 2-by-2 high subblocks, so `|Ω|=8`. In a Y cut it is the 4-by-4 block with four permutation zeros, so `|Ω|=12`. Since (4) does not depend on the cut, mixed X/Y choices are impossible: all three cuts are X or all three are Y. This is a count of one set, not three independently completed matrices.

Suppose all three are Y. The four absent high words project bijectively onto every one of the six high coordinate-pair alphabets: each pair appears exactly once among the missing cells of its actual cut. Label the four missing words by their first two high bits `(a,b)`. Bijectivity of the AC and BC projections says that the third bit, as a 2-by-2 binary table, differs along every row and column; hence it is `a⊕b⊕e`. Likewise the fourth bit is `a⊕b⊕f`, for constants `e,f∈{0,1}`. The CD projection of the four words then has only two distinct values, not four. This contradiction holds for all pair labelings and all possible permutations of zeros. Therefore all three cuts are X and

```
|Ω|=8,     |{w∈Ω : w_i=x,w_j=y}|=2
```

for every physical pair `ij` and every `(x,y)∈H_i×H_j`.

## 4. Complete binary-eight classification

Relabel each `H_i` by a sign `x_i∈{−1,+1}` and put `F(x)=2·1_Ω(x)-1`. Its constant, singleton and pair Fourier coefficients vanish by the preceding equal two-coordinate projections. The four remaining degree-three characters and the degree-four character give the unique expansion

```
F(x)=x_A x_B x_C x_D (c_0+c_A x_A+c_B x_B+c_C x_C+c_D x_D),   (5)
```

with real coefficients. Because `F²=1`, coefficients of `x_i` and `x_i x_j` in the square of the parenthesis give `2c_0c_i=0` and `2c_ic_j=0` for `i≠j`; its constant term is `c_0²+Σc_i²=1`. Thus exactly one of the five coefficients is nonzero, and it is `+1` or `−1`. There are no other equality or mixture cases. Up to party permutation and independent high-bit flips, the two exhaustive supports are

```
three-coordinate parity cylinder:  Ω={a⊕b⊕c=0},  d free;
four-coordinate parity class:        Ω={a⊕b⊕c⊕d=0}.               (6)
```

The flips also cover both parity constants. Both cases are now contradicted using actual E pair lines, not an abstract orthogonal array alone.

## 5. Three-coordinate parity: low-D/BC-neighbor contradiction

Assume the first support in (6), with bit labels for high symbols. In the actual AD|BC cut, for each fixed high a, the two high rows `(a,0)` and `(a,1)` have the same two high BC columns, namely `b⊕c=a`; they must be the two high rows in one X component. The components for `a=0` and `a=1` are distinct. Let their actual low BC columns be

```
s_a=(β_a,γ_a).                                                     (7)
```

If `β_a` were high, then the two entries at `s_a` would add two words to the high AB line `(a,β_a)`, already containing two Ω words, contradicting its exact multiplicity three. The same argument at AC shows `γ_a` is low. Thus the four distinct non-Ω words on these columns are

```
L_a(d)=(a,β_a,γ_a,d),        a,d∈{0,1}.                          (8)
```

For each high a, its four Ω words and two L words exhaust the two high-D pair lines. Since `s_A(a)=8`, there are two more words. The high a has exactly one low D neighbor `δ_a`, and the low B and C neighbors `β_a,γ_a` already have their `(a,β_a)` and `(a,γ_a)` multiplicity-two lines exhausted by the two L words. Hence both remaining words have D=`δ_a` and high B,C. Their actual pair row `(a,δ_a)` has multiplicity two and must be the low row of one of the two AD|BC X components. Its high BC columns are the two values of one fixed parity, differing in both coordinates. The two such rows for a=0,1 are distinct and occupy the two components. Thus there is a permutation `r` of `{0,1}` such that these four words are exactly

```
M_a(b)=(a,b,r(a)⊕b,δ_a),    a,b∈{0,1}.                           (9)
```

This includes both possible component assignments. Since the low symbol `δ_0` has degree two at B and C and its row in (9) already meets both high B symbols and both high C symbols, **all four** E words containing `δ_0` have high B,C. Each high BC value has two Ω words and exactly one other word; those four other words are exactly the two low AD rows in (9). Therefore all four have D=`δ_0`, so `δ_1=δ_0=:δ`. Let `δ'` be the other low D symbol.

For every high B symbol b, Ω supplies neighbors both high D symbols, and (9) supplies neighbor δ. Its degree three therefore excludes `(b,δ')`. The degree-two symbol `δ'` must have two B neighbors, and with neither high B available they must be **both** low B symbols. In particular it must meet `β_0`. But (8) shows `β_0` already meets both high D symbols; because `β_0` has degree two, it cannot meet δ'. Contradiction. This does not assume `β_0≠β_1`, `γ_0≠γ_1`, any phase relation, or a preferred permutation r.

### The actual six-pair incidence behind the contradiction

For clarity, after the forced equality `δ_0=δ_1=δ`, put `M_a(b)=(a,b,r(a)⊕b,δ)`. Let `Z^{BD}_{b,d}` and `Z^{CD}_{c,d}` denote actual words, with unconstrained low symbols where indicated. The following table records all six physical pair systems; each displayed high line has multiplicity exactly three and each displayed low line multiplicity exactly two.

| Physical pair | Actual high and relevant low pair lines |
|---|---|
| AB | `(a,b)` contains the two Ω words with `c=a⊕b`, d=0,1, and `M_a(b)`; `(a,β_a)` contains `L_a(0),L_a(1)`. |
| AC | `(a,c)` contains the two Ω words with `b=a⊕c`, d=0,1, and `M_a(r(a)⊕c)`; `(a,γ_a)` contains `L_a(0),L_a(1)`. |
| AD | `(a,d)` contains its two Ω words and `L_a(d)`; `(a,δ)` contains `M_a(0),M_a(1)`. |
| BC | `(b,c)` contains its two Ω words, with a=`b⊕c` and d=0,1, and `M_{r^{-1}(b⊕c)}(b)`; `(β_a,γ_a)` contains `L_a(0),L_a(1)`. |
| BD | `(b,d)` contains two Ω words and a unique `Z^{BD}_{b,d}=(low_A,b,low_C,d)`; `(b,δ)` contains `M_0(b),M_1(b)`; `(β_a,d)` contains `L_a(d)` and one further word. |
| CD | `(c,d)` contains two Ω words and a unique `Z^{CD}_{c,d}=(low_A,low_B,c,d)`; `(c,δ)` contains `M_0(r(0)⊕c),M_1(r(1)⊕c)`; `(γ_a,d)` contains `L_a(d)` and one further word. |

The low A coordinate of each Z is forced because every high AD line is already exhausted by its two Ω entries and L; the indicated low C or low B coordinate is forced because every high BC line is already exhausted by its two Ω entries and M. The four Z words of each kind are distinct and the two kinds are disjoint. Together with the eight Ω, four L and four M words, these eight Z words account for all 24 E words. This counting is not a separate completion or a claim that their remaining low coordinates are independently choosable.

There is also a shorter independent contradiction before the low-D step: for either high d, Ω gives both high B neighbors, while `L_0(d),L_1(d)` give the low B neighbors `β_0,β_1`. Degree three forces `β_0=β_1`. The same argument gives `γ_0=γ_1`; then `s_0=s_1`, impossible because those are columns in different X components. The low-D/BC argument above is nevertheless given in full and does not rely on this shortcut.

## 6. Four-coordinate parity: propagation through all six actual pair systems

Assume the second support in (6). Fix any cut `ij|kl`. In either X component, its two high `kl` columns have equal `k⊕l` parity and therefore differ in **both** coordinates. Write `R_ij` for the two actual low ij rows of the two high X components. Each such row has two E words at its component's two high kl columns.

Suppose one row has low i symbol `α`. Its two words already use both high k and both high l symbols. Since α has degree two and `s_i(α)=4`, every α word has high k and l. Each of the four high kl pair values has exactly two Ω words and one non-Ω word, and those four non-Ω positions are exactly the words in the two rows `R_ij`. Therefore all four positions must have i-coordinate α: **both** rows in `R_ij` have i-coordinate α. If either also had low j-coordinate β, applying the same argument to β would force both rows to be the identical pair `(α,β)`, impossible. Consequently their j coordinates are the two distinct high symbols. The symmetric argument applies if a row has low j instead. Thus, for every one of the six pair systems, there is exactly one of the actual star forms

```
R_ij = {α}×H_j       (α∈L_i),
or
R_ij = H_i×{β}       (β∈L_j).                                    (10)
```

A low/low row, two different low symbols on the selected endpoint, or any non-star arrangement is impossible. There is no assumption about how the rows are assigned to the two components: they must occupy different components because each has exactly one low row.

If `R_ij={α}×H_j`, the four actual α words all have j,k,l high and visit every high kl pair exactly once. As the two α rows occupy different X components, their high kl column parities are opposite. Thus for some bit ε their **entire** α slice is

```
{(α,x_j,x_k,x_l): x_j⊕x_k⊕x_l=ε}.                               (11)
```

In particular each `(α,x_k)` and each `(α,x_l)` is an actual multiplicity-two E pair line whose two words have high complementary symbols. In the ik and il cuts each such row lies in a high X component, and the two rows exhaust its two low rows. Hence the same physical symbol α propagates:

```
R_ij={α}×H_j  ⇒  R_ik={α}×H_k  and  R_il={α}×H_l.               (12)
```

This is propagation of **the same four E words and the same α**, not merely an orientation of independently selected masks. The permutation of high rows/components and the parity constant ε are arbitrary.

The contradiction uses the stars in all six real pair systems. By relabeling parties, suppose AB chooses its low endpoint at A, with actual symbol α. Then (12) forces the following table. `β,γ,η` below denote arbitrary low symbols at B,C,D; each alternative is separately forbidden by propagation back to a displayed A-star.

| Pair and complementary cut | Its actual two low rows | Consequence |
|---|---|---|
| AB `|` CD | `{α}×H_B` | Chosen without loss of generality. |
| AC `|` BD | `{α}×H_C` | Forced by the same four α words. |
| AD `|` BC | `{α}×H_D` | Forced by the same four α words. |
| BC `|` AD | `{β}×H_C` or `H_B×{γ}` | First forces AB=`H_A×{β}`; second forces AC=`H_A×{γ}`. Both conflict with the actual rows above. |
| BD `|` AC | `{β}×H_D` or `H_B×{η}` | First conflicts with AB; second forces AD=`H_A×{η}` and conflicts with AD. |
| CD `|` AB | `{γ}×H_D` or `H_C×{η}` | First conflicts with AC; second conflicts with AD. |

Already the BC row has neither permitted alternative, so the four-coordinate parity support is impossible. The remaining two rows of the table make explicit that the same argument covers all six systems, including the complementary low columns; no unexamined phase, common-symbol, parity-constant, or component-matching alternative remains.

## 7. Exact result limits and outstanding imports

Sections 1–6 establish the displayed conditional theorem for one actual complex tensor with arbitrary nonzero amplitudes and phases. All needed multiplicity-three/two lines, X/Y supports, three-cut synchronization, four-word Y obstruction, binary Fourier alternatives, and both actual parity contradictions were reconstructed here. The nonzero-angle phase discussion is local only and is not a claimed simultaneous phase parameterization.

The precise remaining load-bearing import for an unconditional 4444 exclusion is: **every** such tensor has, simultaneously at all four parties, two surplus-two degree-three high symbols and two surplus-zero degree-two low symbols, and **none** of its six pair systems contains a multiplicity-four line. The f860 §§2–4 argument for that premise is present as a prior candidate in packet S2, but has not been established by this document; the no-F/degree premise is not a consequence of the parity proof. No absent source is silently promoted. In particular, no all-t=26, all-N=50, q≠4444, global minimum, construction, publication-priority or novelty statement is made. The parent must separately disposition this author candidate and every required import.

## 8. Complete reads and process declaration

Before any mathematical packet body or task-specific mathematical reasoning, I read the complete frozen manifest, freeze receipt, final pre-dispatch binding, parent live metadata supply, actual-dispatch receipt, and all 22 manifest-listed status-only controls. Initial non-raw administrative displays elided blocks; complete raw displays recovered those blocks before both the local `prebody-ack-v1.md` and the direct prebody acknowledgement to Main. The controls were permissions/status only, not mathematical inputs. The output names were absent in the initial owned-directory listing; the write interface does not expose an OS-level exclusive-create flag, so no stronger atomic-creation guarantee is asserted.

Only after both acknowledgements, I read the one literal packet part serially in raw windows `1–20, 21–40, …, 401–420, 421–434`, including the ending. Every displayed window was below 30,000 bytes and at most 20 LF; no packet clipping was observed and no clipping recovery was needed. The packet completely renders S1 original LF 1–3, S2 LF 1–182, S3 LF 1–172, S4 LF 1–22 and S5 LF 1–33. The parent-supplied packet SHA-256 is `7628f3d1d1bb7ee9a8c0d8d30c79c817701c10be2f32fcc8d3fbfc9c34e85dc1`; source paths and supplied whole-source pins are in the frozen manifest. These are parent-supplied administrative bindings, not independently recomputed hashes, source-identity certification, or correctness verification.

S2 is the nonblind prior author candidate being reconstructed; S1 is S3's notation erratum, S3 is a separate author candidate, and S4/S5 are scoped parent dispositions. No linked source or historical code was opened. All genuine held episodes and their proof, method, planning, selection, verification, confidence, reporting and downstream consumers remained NONINPUT; no sibling scientific output was read. No network, external model, scientific eval, code execution, subprocess, test, solver, compilation, build, lint, formatter, Git, deletion or executable preparation was used. Hence there is no prepared code hash or computational verification. No process deviation beyond the recovered initial administrative display elisions is known. Any correction must be a new additive file, not an edit of this candidate.
