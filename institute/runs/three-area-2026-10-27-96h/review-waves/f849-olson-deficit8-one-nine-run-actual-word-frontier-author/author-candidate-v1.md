# F849 author candidate: one nine-run, at most three rich windows

**Disposition requested:** independent checking and parent disposition of the written results below. This is an AUTHOR CANDIDATE, not an acceptance. It proves a strictly larger actual-word region and gives an exact algebraic description of the surviving problem; it does **not** prove that the surviving region is empty, produce an avoiding word, or establish an unrestricted ordered-Olson theorem. The complete-original-source correspondence and novelty remain unassessed.

## 1. Quantified object and result

Let `p >= 7` be an odd prime, let `D_(2p) = F_p ⋊ {0,1}` with

`(x,e)(y,f) = (x + (-1)^e y, e+f mod 2)`, `r_y=(y,0)`, `s_x=(x,1)`,

and let `W` be an **actual linear ordered word** with exactly `F=3p-2` reflection occurrences and `R >= p+1` rotation occurrences. Assume at most one rotation in each original cyclic gap between consecutive reflection occurrences. The group identity rotation is allowed and still counts as a rotation occurrence. Assume that the cyclic reflection projection has exactly one constant run of length nine and that all other runs are singletons; thus `o_pi=3p-10`. Let `H <= 3` be the number of rich cyclic triple windows, with richness exactly as defined in S1: the three differences `{a-b,a-c,b-c}` are pairwise distinct. Occurrences, not labels, are counted.

The results proved here are:

1. `H=0` is impossible. If two rich windows have centers in the same residue class modulo three in the natural outside-run indexing defined below, there is an original-order identity subsequence with exactly `2p` occurrences: `2p-2` reflections and two actual rotations. This includes valid `H=2` and `H=3` inputs not covered by S1's stated `H>=4` type-nine criterion.
2. Even when each phase has at most one rich block, the explicit direction tests in §5 give an exact-two-rotation selector for every word that passes them, for **every** assignment of actual rotation gaps and exponents satisfying the hypotheses. The tests include `p=7` without an asymptotic or division-by-`p-7` assumption.
3. Failure of all those tests is still not a counterexample. §6 adds necessary finite-field offset restrictions involving every actual eligible rotation pair. §7 gives a nonnegative-coefficient transfer expression whose vanishing is **equivalent** to failure of *all* original-order length-`2p` identity selections, including selections with zero, four, or more rotations and the two-rotation selections not represented by our triple cuts. Together these supply the exact surviving structural/algebraic frontier. Its nonemptiness and its universal resolution are not claimed.

All following arguments are written and self-contained. The packet S1 gives the set-up and prior disposition; I do not import its linked author/review/checker bodies or use its stated selector as an unproved premise. In particular, if one wishes to invoke their separate results or historical proof details, the missing bodies and their respective dispositions are **named conditional imports**: f603 author, f638/f639 written reviews, f640 narrative, source and run receipt, all as identified in S1. None was opened here. Cauchy--Davenport is proved in the form used in §4, so no missing sumset-proof body is needed for this candidate.

## 2. Exact one-nine-run parametrization

Cyclically index the nine equal reflection occurrences as `A_1,...,A_9`, each with exponent `a`, followed by the `m=3p-11` outside singletons `b_1,...,b_m`, whose exponents are also denoted `b_i`. Put

`x_0=a`, `x_i=b_i` for `1<=i<=m`, `x_(m+1)=a`, and `d_i=x_i-x_(i-1)` for `1<=i<=n=m+1=3p-10`.

The nine-run and all-other-singletons condition is **equivalent** to

`d_i in F_p^×` for all `i`, and `sum_(i=1)^n d_i=0`.

In particular, nonadjacent outside labels may equal one another or `a`; they are not assumed distinct. Conversely every such nonzero closed increment sequence reconstructs a cyclic reflection projection of exactly the required run type, including when an outside label happens to equal `a`. The actual rotation position and exponent in every one of the `F` cyclic gaps are retained separately. An original linear word can start anywhere in this cycle.

The only possibly rich triples have centers `b_i`, `1<=i<=m`, and their difference sets are

`{-d_i, -(d_i+d_(i+1)), -d_(i+1)}`.

Because the adjacent increments are nonzero, this set has three distinct elements exactly when `d_i != d_(i+1)`. Every triple meeting the interior of the nine-run has a repeated adjacent label and is not rich. Hence

`H = #{1<=i<=m : d_i != d_(i+1)}`.                                      (2.1)

If `H=0`, all `d_i=d != 0` and closure gives `(3p-10)d=-10d=0`, impossible for a prime `p>=7`. Thus `1<=H<=3` on all actual inputs under discussion.

Equivalently, choose `h=H`, change indices `1<=k_1<...<k_h<=n-1`, positive lengths `ell_0=k_1`, `ell_j=k_(j+1)-k_j` for `1<=j<h`, `ell_h=n-k_h`, and nonzero slopes `v_0,...,v_h` with `v_(j-1)!=v_j`. The complete closure condition is

`sum_(j=0)^h ell_j v_j = 0 in F_p`.                                    (2.2)

This is an exact parametrization, not a claim that every choice of lengths is realizable: (2.2), nonzero slopes, and adjacent inequality must all hold.

## 3. The three actual cuts and their gap accounting

For `j=1,2,3`, omit the actual occurrence `A_j`, cut immediately after it in the cyclic word, and partition the other `3p-3` reflection occurrences chronologically into `p-1` triples. The physical gap before the omitted occurrence and the physical gap after it remain **distinct**, even though they become adjacent in the surviving cyclic reflection projection. All rotations in inter-block gaps and in those two end gaps remain in their actual chronological positions.

Each of the three partitions has exactly two constant triples, all lying inside the nine-run. The only nonconstant triple with an equal adjacent pair is `(a,a,b_1)` in phase `j=1`, respectively `(b_m,a,a)` in phase `j=3`; phase `j=2` has none. These statements follow by counting the run pieces after the cut: their initial lengths are `8,7,6`, their final lengths are `0,1,2`, and `m ≡ 1 (mod 3)`. No outside adjacent increment is zero.

A rich window centered at `b_i` is a block in exactly one of these partitions, namely

`j ≡ i+1 (mod 3)`, where `j` is chosen from `{1,2,3}`.               (3.1)

Write `r_j` for the number of rich blocks in phase `j`; then `sum_j r_j=H`. Thus a same-residue collision of rich centers is exactly the existence of a phase `r_j>=2`.

For a block `(a,b,c)`, call its two interior physical gaps `g_1` (between `a,b`) and `g_2` (between `b,c`). If a single selected rotation of exponent `u` is in `g_1`, the two choices omitting respectively `b,c` have pair contributions

`a-c-u`, `a-b-u`;                                                     (3.2a)

if a single selected rotation of exponent `v` is in `g_2`, the two choices omitting respectively `a,b` have pair contributions

`b-c-v`, `a-c-v`.                                                     (3.2b)

Thus `g_1` is unsafe only when `b=c`, and `g_2` only when `a=b`. A constant block need not be forbidden: with at most one selected interior rotation it contributes at least one valid value, and its actual value is retained. Among nonconstant blocks in the chosen partition, at most one physical gap is unsafe.

Protect any `min(r_j,2)` rich blocks by forbidding their two interior physical gaps, and forbid the at-most-one unsafe nonconstant gap. At most five actual gaps are forbidden. As `R>=p+1>=8`, at least three actual rotations remain. Since any one triple has only two interior gaps, two remaining rotations can be selected with at most one in each triple; rotations in inter-block/end gaps are unrestricted by this last condition. This counts the two physical end gaps separately and does not assume that selected rotation exponents are nonzero or distinct.

For such a rotation pair, choose exactly two reflections in each triple. Every block begins after an even number of selected reflections, so a selected boundary-gap rotation contributes its actual exponent with plus sign. Each protected rich triple contributes its full three-element difference set; every other nonconstant triple contributes at least two distinct values, by (3.2) if it contains a rotation and by its difference set otherwise; each constant triple contributes at least one value. All local choices correspond to actual original occurrences and may be combined independently.

## 4. Sumset proof and the same-residue selector

For finite nonempty `A,B ⊆ F_p`, the bound

`|A+B| >= min(p, |A|+|B|-1)`                                           (4.1)

is needed. Here is a self-contained proof. Choose nonempty subsets `A',B'` with `(abs(A')-1)+(abs(B')-1) = N := min(p-1,abs(A)+abs(B)-2)`. If `abs(A+B)<=N`, choose `C` of size `N` containing `A'+B'`. The polynomial `f(X,Y)=product_(c in C)(X+Y-c)` vanishes on `A'×B'`, has total degree `N`, and the coefficient of `X^(abs(A')-1)Y^(abs(B')-1)` is `binom(N,abs(A')-1)`, nonzero in `F_p` since `N<p`. Lagrange interpolation on the finite grid expresses this top coefficient as a sum of the values of `f` on that grid divided by nonzero Vandermonde denominators, giving zero, a contradiction. This proves (4.1), and iteration proves the corresponding multi-set bound.

If `r_j>=2`, protect two rich blocks as in §3. Of the `p-1` blocks, two are constant, two protected blocks contribute three values each, and the remaining `p-5` nonconstant blocks contribute at least two each. By (4.1), the local sumset has size at least

`min(p, 1 + 2 + 2 + (p-5)) = p`.

It therefore contains the negative of the **actual** boundary-gap contribution. The corresponding `2p-2` actual reflections and two actual rotations have product identity in the cut order. Returning to the original linear occurrence order cyclically rotates the selected subsequence and hence conjugates its product; identity remains identity. This proves item 1 of §1 for all `p>=7`, including `p=7`.

## 5. Additional complete direction tests for phases with `r_j<=1`

Fix a phase with `r=r_j` equal to 0 or 1. Protect its rich block if present and choose any eligible two rotations as in §3. For each nonconstant, nonrich triple, choose its two-value local set: the whole difference set if it has no internal selected rotation, or the corresponding safe pair in (3.2) otherwise. Its nonzero direction, up to sign, is independent of the chosen eligible rotations: it is the common nonzero adjacent difference of the triple, including the single nonzero difference in `(a,a,b_1)` or `(b_m,a,a)`. Let the resulting multiset of direction classes modulo sign be `D_j`. Its cardinality is

`n_j=p-3-r`: `p-3` when `r=0`, and `p-4` when `r=1`.                (5.1)

For `r=1`, let `T_j` be the rich triple's exact three-element difference set.

**The direction selector.** Under the hypotheses of §1, an original-order exact-two-rotation selector exists if any phase satisfies one of the following:

* `r=0`: `D_j` has at least two entries outside every single sign-class `{+d,-d}`; or it has exactly one entry outside some such class and that exceptional entry is not in `{+2d,-2d}`.
* `r=1`: `D_j` contains two different sign-classes; or all its entries lie in `{+d,-d}` but `T_j` is not a three-term consecutive `d`-progression `{t,t+d,t+2d}` in `F_p`.

These tests depend on the actual chronological blocks and their actual field values, not merely on `H` or on run-length multiplicities. They never demand a particular rotation exponent. Proof:

For `r=0`, there are `n_j=p-3` two-point sets. Two direction classes not equal up to sign give a four-point sum of the two corresponding sets. If there are two disjoint unequal-class pairs, (4.1) gives at least `min(p,4+4-1+(n_j-4))=p` values. Since `n_j>=4`, such pairs exist exactly when no class has at least `n_j-1` members. If all but one have direction `±d`, translate and orient them as `{0,d}`. Their sum is an interval of `p-3` consecutive `d`-points, whose complement consists of three consecutive `d`-points. Adding the exceptional `{0,e}` fills the field whenever `e` is not `0,±d,±2d`; here `e!=0,±d`, so precisely the stated `e!=±2d` test guarantees coverage. The two possible constant-block values and the actual boundary contribution are merely extra translates, never an obstruction to field coverage.

For `r=1`, there are `n_j=p-4` two-point sets and one protected three-point set. If two directions differ modulo sign, their sum has four elements; adding the remaining pairs and the triple gives at least `min(p,4+(n_j-2)+2)=p`. Otherwise orient all pairs as `{0,d}`. If `T_j` is not three consecutive vertices in the cyclic `d`-ordering of `F_p`, then `|T_j+{0,d}|>=5`: each component of `T_j` in that cycle contributes a new endpoint, and a nonconsecutive three-set has at least two components. Adding the remaining pairs again gives at least `min(p,5+(n_j-1))=p`. The cardinalities are valid already at `p=7`.

For interpreting the remaining `r=1` case without a hidden finite-field degeneracy, write its neighboring nonzero increments as `u!=v`. Its rich set is `T={-u,-v,-u-v}`. It is a three-term progression of step `±d` precisely in one of these three cases:

`u=2v` and `d=±v`; or `v=2u` and `d=±u`; or `v=-u` and `d=±u`.  (5.2)

This follows by testing which of the three distinct values is the midpoint. The conditions use field arithmetic; no assumption of distinct nonadjacent reflection labels is made.

## 6. Exact phase-offset restrictions that any surviving word must satisfy

These restrictions retain each eligible actual rotation pair and both physical cut-end gaps. They strengthen the direction-only frontier but are **necessary**, not asserted sufficient for a word to avoid all selectors.

For a bad phase in §5, choose a representative `d` of its common sign-class. For each eligible two-rotation pair `Q`, orient each selected two-point nonrich local set as `{b_i,b_i+d}`; in the one-outlier case orient the exceptional set as `{b_e,b_e+2d}`. If `r=1`, write the protected rich set uniquely as `{b_T,b_T+d,b_T+2d}`. These are actual field elements, including all selected interior-rotation offsets in the `b_i`.

Let `B_j(Q)` be the set of all sums of: the actual exponents of the selected rotations in inter-block and both physical end gaps; all bases `b_i` and, if present, `b_T`; and one arbitrary *actual* local value from each of the two constant blocks. A constant block with no selected internal rotation contributes `{0}`; one with a selected internal rotation of exponent `y` contributes `{y,-y}` (possibly a singleton when `y=0`). A selected rotation cannot be in a protected rich block. The sets `B_j(Q)` therefore include all actual constant-block choices and all boundary offsets; there is no free cancellation by an invented field element.

For each `Q`, the following deliberately restricted choices are all actual subsequences:

* `r=0`, every direction `±d`: `B_j(Q) + {0,1,...,p-3}d`; zero is absent exactly when `B_j(Q) ⊆ {d,2d}`.
* `r=0`, exactly one direction `±2d` and all others `±d`: `B_j(Q) + {0,1,...,p-2}d`; zero is absent exactly when `B_j(Q) ⊆ {d}`.
* `r=1`, all nonrich directions `±d` and `T_j` consecutive of step `d`: the same set `B_j(Q)+{0,1,...,p-2}d`; zero is absent exactly when `B_j(Q) ⊆ {d}`.

For example, the second interval is obtained from `{0,...,p-4}d + {0,2d}`; it is an interval because `p>=7`. Consequently, if **any** eligible actual `Q` violates the corresponding containment, it explicitly yields an exact-two-rotation identity selector. If all selectors fail, these containments hold for **every** eligible `Q` in **every** phase. In the singleton-containment cases, an eligible `Q` containing a nonzero rotation inside a constant block already forces a selector, because its two constant-block values differ by `2y != 0`. In the first case a surviving such pair must instead have `2y in {0,±d}`.

The phase restrictions deliberately select only two choices from some triples. A safe internal rotation can in fact make a nonrich block's *full* local set three-valued; two selected rotations can even occupy the same block in an unrestricted selection. Neither possibility is discarded from the exact frontier below. For any block `(a,b,c)`, if its selected rotations in `g_1,g_2` have exponents `u,v` respectively, with an absent rotation represented by the value zero **but its selection count tracked separately**, the full exact local set obtained by omitting one of the three reflections is

`T(a,b,c;u,v) = { b-c+u-v, a-c-u-v, a-b-u+v }`.                    (6.1)

For any phase `j` and **any** two distinct actual rotations `Q`, including two in one block, the chronological one-omission/two-per-triple family has an identity exactly when zero belongs to the sum of these full `T` sets and the actual plus-signed inter-block/end-gap exponents. This is an exact test for that family, not a claim that the family contains every possible selection.

## 7. Exact surviving all-selection frontier

The following expression includes all physical rotation gaps, their exponents, chronological order, and arbitrary numbers of rotations. It is a written finite-field transfer identity, not an executed verifier.

Work over `Z[X]/(X^p-1)`. Define

`S_x = [[0, X^x], [X^(-x), 0]]`, `R_y = [[X^y, 0], [0, X^(-y)]]`.

Cyclically start at `A_1` and list the `F` actual reflection exponents `x_1,...,x_F` in order. Let `rho_i` be 1 if the original cyclic gap after reflection `i` contains an actual rotation, and 0 otherwise; for `rho_i=1` let `y_i` be its actual exponent. There is at most one such occurrence by hypothesis. Form the ordered product

`P(t,z) = product_(i=1)^F (I+t S_(x_i)) (I+rho_i t z R_(y_i))`.       (7.1)

The product is ordered by occurrence, not commuted. In the top-left entry put

`N(W) = sum_(r even, 0<=r<=min(R,2p)) [t^(2p) z^r X^0] P(t,z)_(1,1)`, (7.2)

where `X` exponents are reduced modulo `p` before taking `[X^0]`. Each factor independently omits or selects its actual occurrence. Matrix multiplication implements precisely the semidirect-product exponent signs. Thus every coefficient is a nonnegative integer and `N(W)` is **exactly the number** of identity subsequences of length `2p`. An identity has an even number of selected reflections; since its total length is even, it has an even number of selected rotations, as enumerated. The case of zero rotations, all higher even rotation counts, and zero-exponent rotation occurrences are included. Cyclically moving the physical cut from the original linear start to `A_1` cyclically rotates every selected occurrence list, conjugating its product, so it neither creates nor destroys identity selections and preserves their count.

Consequently the exact counterexample frontier to the assigned original-word existence statement consists of all data satisfying simultaneously:

1. the full input hypotheses and (2.2), with `1<=h=H<=3`;
2. each of the three counts `r_j` from (3.1) is at most one;
3. every phase has one of the bad direction patterns listed in §6, and its stated `B_j(Q)` containment holds for **every** eligible actual rotation pair `Q`;
4. `N(W)=0` in (7.2).

Necessity of 1--3 was proved above, and condition 4 is necessary and sufficient for actual avoidance; hence this is an exact, not merely necessary, description of the surviving set. Condition 4 is explicitly the **first unresolved all-selection obligation**, not a proved automatic consequence of 1--3 or an assertion that such words exist. Its exact logical complement is: for every prime and every original word in 1--3, the nonnegative coefficient in (7.2) is positive. Showing that statement, or providing a fully valid word with coefficient zero, would settle the rest of this assigned frontier. A necessary-only declaration that the `B` conditions imply avoidance would be false reasoning. The equivalent special-family equation (6.1) can strengthen a future proof, but cannot replace (7.2) without separately proving completeness of that family.

## 8. Explicit `p=7` boundary and a nonvacuous newly covered word

At `p=7`, `F=19`, `m=10`, `n=11`, `R>=8`, and there are six chronological triples per cut, exactly two of them constant. The rich center classes of phases `1,2,3` are respectively `{3,6,9}`, `{1,4,7,10}`, and `{2,5,8}`. If `r=0`, four nonrich blocks contribute pairs: the uniform-direction restricted set is `B+{0,1,2,3,4}d`, with missing offsets `d,2d`; the single `±2d` outlier gives `B+{0,1,2,3,4,5}d`, with missing offset `d`. If `r=1`, three nonrich blocks plus the rich triple give the latter six-point set in the bad case. The gap proof still has at least three eligible rotations even when five physical gaps are forbidden.

If `H=1`, the lone change index is `k in {1,...,10}`. With slopes `u` before and `v` after it, the exact closure is `k u + (11-k)v=0` in `F_7`. Nonzero slopes rule out `k=4,7`; for the remaining `k`, the exact ratios are

`k:       1  2  3  5  6  8  9 10`
`v/u:     2  6  4  5  3  2  6  4`.

No inference about selection follows merely from this table. For `H=2,3`, all positive segment lengths and all neighboring-distinct nonzero slopes satisfying (2.2) remain included; in particular, no small-field boundary offset is discarded.

A hand-derived nonvacuous example in the newly proved same-phase region is as follows. Set the run label to `0` and take outside increments `(4,1,1,1,2,2,2,2,2,2,2)` in `F_7`. Their sum is `21=0`; the outside labels are `(4,5,6,0,2,4,6,1,3,5)`. The two rich centers are `i=1,4`, both in phase 2. Put eight actual identity rotations `r_0` in the eight distinct gaps after `A_1,...,A_8`. Omitting `A_2`, the six triples are

`(0,0,0), (0,0,0), (0,4,5), (6,0,2), (4,6,1), (3,5,0)`.

Choose rotations after `A_3` and `A_6`; choose reflection pairs `(A_3,A_4)`, `(A_6,A_7)`, `(A_9,b_2)`, `(b_3,b_5)`, `(b_6,b_8)`, `(b_9,b_10)`. They occur in that original order, and their alternating reflection exponent is `0+0+2+4+3+5=14=0` in `F_7`. Thus these actual 14 occurrences multiply to identity. This example is illustrative only and is not a substitute for the general proof.

## 9. Read, provenance, and limits

Before any mathematical packet read or reasoning I read the full manifest, freeze receipt, final pre-dispatch binding, parent live metadata supply, actual-dispatch receipt, and every one of the 22 listed controls as status/permission only. I created `prebody-ack-v1.md` and directly sent the prebody acknowledgement to Main before opening the packet. The owner-only directory listing showed that both new output names were absent; the available write tool has no atomic exclusive-create flag, a process qualification rather than an assertion of atomic `O_EXCL`.

After the acknowledgement I read the sole literal part completely and in order in raw windows LF `1-15`, `16-30`, and `31-44`, including its ending. The whole part is parent-reported 9,142 bytes, so every display was below 30,000 bytes and every window at most 20 LF. No packet clipping was observed and no recovery was needed. These windows render all S1 source lines 1--38 and its ending. Initial compact administrative displays elided portions; I recovered each of the five administrative records by complete `:raw` reads before the acknowledgement. Parent-provided source/part SHA256 values are metadata, not an independently executed hash check.

No other mathematical body, link target, held f602 episode, other held episode, or held proof/method/selection/planning/verification/reporting/confidence/downstream consumer was read. The general memory summary and written-math procedure were read before the mathematical packet and provide no mathematical premise here. No peer scientific content, network, external model, code execution, scientific evaluation, test, compilation, solver, child subprocess, or prepared verifier was used. The `p=7` example is a fresh written hand calculation, not an execution. No code was prepared and no prepared-code hash exists. I make no claim to independently certify private cognition or historical nonexposure. The sole permitted scope is this author candidate; no formal, human, independent-family, publication, global-theorem, or parent-acceptance status is implied.
