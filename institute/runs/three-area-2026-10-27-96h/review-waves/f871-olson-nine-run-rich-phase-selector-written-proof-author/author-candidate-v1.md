# F871 author candidate: the actual nine-run phase selector

**Status.** Independent written reconstruction of the specified f849 `H=0` impossibility and same-phase rich-center selector, including the actual original-order consumer. This is an author candidate, not a parent disposition or family/human/formal acceptance. It does not settle the remaining one-nine-run cases or the full deficit-eight band.

## 1. Exact statement and quantifiers

Let `p >= 7` be a prime, and write

`D_(2p) = F_p ⋊ {0,1}`, `(x,e)(y,f) = (x + (-1)^e y, e+f mod 2)`.

Write `s_x=(x,1)` for a reflection occurrence and `r_y=(y,0)` for a rotation occurrence. For **every actual linear word** `W` with exactly `F=3p-2` reflections and `R >= p+1` rotations, suppose each physical cyclic gap between consecutive reflection occurrences contains at most one rotation occurrence. Rotation exponents can be zero or repeated. Suppose the cyclic reflection projection consists of exactly one maximal constant run of nine occurrences and otherwise singleton runs. Two nonadjacent occurrences may have the same exponent, including the nine-run exponent. A cyclic reflection triple `(a,b,c)` is rich if its **set** `{a-b,a-c,b-c}` has cardinality three; `H` counts rich windows as occurrences.

Index the run in cyclic order as `A_1,...,A_9`, all with exponent `a`, and then index the remaining `m=3p-11` reflections as `b_1,...,b_m`. Their subscripts name occurrences and their symbols also denote their exponents. Set `x_0=a`, `x_i=b_i` for `1<=i<=m`, `x_(m+1)=a`, and `d_i=x_i-x_(i-1)` for `1<=i<=m+1`.

The following claims hold without assuming `H<=3`:

1. `H>=1`.
2. If there are distinct rich centers `b_i,b_k` with `i≡k (mod 3)`, then `W` has an identity subsequence in its **original linear order**, with exactly `2p-2` reflections and exactly two actual rotations. Equivalently, the condition is that at least one of the three partitions below has two rich blocks. In particular it holds whenever `H>=4`.

For the f849 `H<=3` domain, the only cases not decided by this particular same-phase criterion have `H=1`, or `H=2` or `3` with all rich-center indices in different residue classes modulo three. This is merely an explicit residual domain: it is not a claim that its words avoid identity or that all formally described cases are realizable.

## 2. Closure and rich centers

The single-run hypothesis is exactly `d_i != 0` for every `i=1,...,m+1`. Telescoping around the outside chain gives

`sum_(i=1)^(m+1) d_i = 0`.                                           (1)

Conversely, any nonzero increments satisfying (1), with any starting `a`, reconstruct this run type: consecutive outside exponents, and each outside exponent next to the nine-run, differ. Equality at nonadjacent places creates no additional adjacent equality and is allowed.

Every triple centered in the nine-run contains adjacent equal exponents, so cannot be rich. At outside center `b_i`, its adjacent increments are `d_i,d_(i+1)` and its three differences are

`{-d_i, -(d_i+d_(i+1)), -d_(i+1)}`.                                  (2)

The first and middle elements differ because `d_(i+1) != 0`, and the middle and last differ because `d_i != 0`; consequently (2) has size three exactly when `d_i != d_(i+1)`. In particular, if `d_(i+1)=-d_i`, the first and third reflection exponents coincide but the window is nevertheless rich, since `p` is odd. Thus

`H = #{i : 1<=i<=m, d_i != d_(i+1)}`.                               (3)

Were `H=0`, all `n=m+1=3p-10` increments would equal one nonzero `d`. Equation (1) would give `(3p-10)d=-10d=0` in `F_p`, impossible because a prime `p>=7` divides neither `10` nor `d`. This proves claim 1, not just a bound on formal slope patterns.

## 3. The three actual omission phases

Let `q=p-4`, so `m=3q+1` and `q>=3`. For `j=1,2,3`, omit the actual occurrence `A_j`, cut the cyclic occurrence list immediately after it, and partition the other `3p-3` reflections into `p-1` chronological triples. The following list gives every block in every phase; the first two blocks in each row are constant:

* **Phase 1:** `(A_2,A_3,A_4)`, `(A_5,A_6,A_7)`, `(A_8,A_9,b_1)`, then `(b_(3t-1),b_(3t),b_(3t+1))` for `1<=t<=q`.
* **Phase 2:** `(A_3,A_4,A_5)`, `(A_6,A_7,A_8)`, `(A_9,b_1,b_2)`, then `(b_(3t),b_(3t+1),b_(3t+2))` for `1<=t<=q-1`, and finally `(b_(3q),b_(3q+1),A_1)`.
* **Phase 3:** `(A_4,A_5,A_6)`, `(A_7,A_8,A_9)`, then `(b_(3t-2),b_(3t-1),b_(3t))` for `1<=t<=q`, and finally `(b_(3q+1),A_1,A_2)`.

The first and last outside transitions are nonzero by the run hypothesis. Hence there are exactly two constant blocks in every phase. Phase 1 has exactly one nonconstant block with adjacent equal exponents, `(a,a,b_1)`; phase 3 has exactly one, `(b_m,a,a)`; and phase 2 has none. Every other nonconstant block has both adjacent differences nonzero, though its first and third exponents may agree.

The rich centers in phase 1 are exactly `b_3,b_6,...,b_(3q)`; in phase 2 they are `b_1,b_4,...,b_(3q+1)`; and in phase 3 they are `b_2,b_5,...,b_(3q-1)`, subject in each case to the richness test (3). Thus an outside rich center `b_i` occurs as a block in exactly phase

`j≡i+1 (mod 3)`, with `j` represented by `1,2,3`.                  (4)

This proves the claimed equivalence between two centers in one index residue and two distinct rich **blocks** in one phase. Both boundary centers `b_1,b_m` are included in phase 2. At `p=7`, `q=3`, the three lists are respectively indices `{3,6,9}`, `{1,4,7,10}`, and `{2,5,8}`.

The gap before omitted `A_j` and the gap after omitted `A_j` are two distinct physical cyclic gaps. They become adjacent only after the omission; they must not be merged in the accounting. Each may contain its own actual rotation, and each is a boundary/end gap of the cut list.

## 4. Local signs, unsafe gaps, and actual rotations

Consider a chronological triple with reflection exponents `(a,b,c)` and physical interior gaps `g_1=(a,b)`, `g_2=(b,c)`. Exactly two reflections will be retained from every triple. A selected interior rotation contributes with the sign determined by the number of retained reflections before it, not by the number of original reflections. More explicitly, if selected rotations of exponents `u,v` lie in `g_1,g_2`, respectively, and an absent rotation is represented algebraically by exponent zero **while selection is tracked separately**, the contributions of retaining `(b,c)`, `(a,c)`, `(a,b)` are

`b-c+u-v`,  `a-c-u-v`,  `a-b-u+v`.                                  (5)

A selected zero-exponent rotation and an absent rotation therefore agree in (5) but are different occurrence selections.

With only one selected interior rotation of exponent `u` in `g_1`, the choices `(a,c)` and `(a,b)` give `a-c-u` and `a-b-u`. They are distinct exactly when `b!=c`. With only one selected rotation of exponent `v` in `g_2`, the choices `(b,c)` and `(a,c)` give `b-c-v` and `a-c-v`, distinct exactly when `a!=b`. Thus the only potentially unsafe interior gap of a nonconstant block is `g_1` when `b=c`, or `g_2` when `a=b`. If neither interior gap contains a selected rotation, a nonconstant triple has at least two different values in `{b-c,a-c,a-b}`. A rich block has three values when neither interior gap is selected. A constant block always has at least one actual local value; if it has a single selected internal rotation `r_y`, its possible values include `y` and `-y`, possibly coincident when `y=0`.

In phase 1 the only unsafe nonconstant physical gap is `(A_9,b_1)`; in phase 3 it is `(b_m,A_1)`; in phase 2 there is no unsafe nonconstant physical gap. All other nonconstant gaps are safe even when nonadjacent block exponents agree.

Suppose a phase has at least two rich blocks. Protect two of them by forbidding their four physical interior gaps, and also forbid the phase's at most one unsafe nonconstant gap. This forbids at most five distinct gaps, and at most four in phase 2. Since each physical gap contains at most one rotation, at least

`R-5 >= p-4 >= 3`                                                     (6)

actual rotations remain eligible; the phase-2 lower bound is `R-4 >= p-3`. A triple has only two interior gaps. Therefore among at least three eligible rotations, two can be chosen so that no triple has more than one selected interior rotation: if one is in a boundary or inter-block gap, choose it and any other; otherwise three rotations cannot all occupy one triple. Both physical end gaps are eligible, and both can be chosen simultaneously. There is no assumption that their exponents, or any selected rotation exponents, are nonzero or distinct.

Fix such a pair `Q`. Retain two reflections from each triple. Each preceding triple contributes an even number of selected reflections, so each block starts with positive reflection parity, regardless of how many rotations precede it. A selected boundary or inter-block rotation therefore contributes its actual exponent with plus sign; the two separate cut-end gaps have plus signs as well. Within each block use (5). The protected rich blocks have their full three-element local sets, every other nonconstant block has at least two distinct local values by the safe-gap argument, and each constant block has at least one. Local choices in disjoint triples are choices of actual occurrences and are mutually independent.

## 5. Finite-field sumset proof and selector

For nonempty `A,B⊆F_p`,

`|A+B| >= min(p, |A|+|B|-1)`.                                      (7)

For completeness, here is the argument used. Choose nonempty `A'⊆A`, `B'⊆B` such that `alpha=|A'|-1`, `beta=|B'|-1`, and `alpha+beta=N=min(p-1,|A|+|B|-2)`. If `|A+B|<=N`, choose a set `C⊆F_p` of size `N` containing `A'+B'`. The polynomial `f(X,Y)=prod_(c in C)(X+Y-c)` vanishes on `A'×B'`. Its coefficient of `X^alpha Y^beta` is `binom(N,alpha)`, nonzero in `F_p` since `N<p`. On the other hand the Lagrange grid coefficient formula expresses that coefficient, for a polynomial of total degree at most `alpha+beta`, as

`sum_(x in A', y in B') f(x,y) / (prod_(x'!=x)(x-x') prod_(y'!=y)(y-y'))`,

which is zero. The denominators are nonzero. This contradiction proves (7); iteration gives `|T_1+...+T_k| >= min(p,1+sum_i(|T_i|-1))` for nonempty sets.

There are `p-1` triples in the protected phase. Exactly two are constant, two protected rich triples have local sets of size three, and the other `p-5` nonconstant triples have local sets of size at least two. Hence their actual independent local-sum set has cardinality at least

`min(p, 1 + 2 + 2 + (p-5)) = p`.                                   (8)

This calculation includes `p=7`, where there are six triples and two remaining nonconstant triples. Thus the local-sum set is all `F_p`. In particular it contains the negative of the **actual** sum of the selected boundary/inter-block rotation exponents. Choose one realized local pair of reflections in each triple to obtain total exponent zero. The resulting cut-order subsequence has `2(p-1)+2=2p` actual occurrences, of which exactly two are rotations; it is the group identity. This proves claim 2 in the cut order.

For the original order, write a cyclically shifted selected occurrence list as two consecutive products `P,Q`. Its product in one cut is `PQ`, and in the other it is `QP=P^(-1)(PQ)P`. Thus cyclically changing the physical starting point conjugates the selected product and preserves identity. Reinsert no omitted reflection: simply view the same selected occurrences in the original linear order. This is a cyclic shift, not an arbitrary permutation. It proves the claimed original-order consumer, including when the original word starts inside a physical reflection gap.

## 6. Boundary examples and what zero rotations mean

At `p=7`, a concrete collision example has run exponent `a=0` and increments

`(d_1,...,d_11)=(4,1,1,1,2,2,2,2,2,2,2)`.

Their sum is `21=0`; the outside exponents are `(4,5,6,0,2,4,6,1,3,5)`. The only changes occur at `i=1,4`, so the rich centers share phase 2; the outside sequence also repeats nonadjacent labels and contains another zero. Put eight actual identity rotations in the eight distinct gaps after `A_1,...,A_8`, and start the actual linear word at `A_1`. Select the rotations after `A_3,A_6` and the six reflection pairs

`(A_3,A_4)`, `(A_6,A_7)`, `(A_9,b_2)`, `(b_3,b_5)`, `(b_6,b_8)`, `(b_9,b_10)`.

These are in original occurrence order; their pair contributions are `0,0,2,4,3,5`, with sum `14=0` in `F_7`. Hence they exhibit the exact-two-rotation identity, even though both selected rotation exponents are zero.

Conversely, `H=1` is not ruled out by the `H=0` proof. For `p=7`, take increments `(1,2,2,2,2,2,2,2,2,2,2)`, whose sum is `21=0`. There is exactly one change, at `i=1`, and the outside exponents from `a=0` are `(1,3,5,0,2,4,6,1,3,5)`. Adding identity rotations in the eight gaps after `A_1,...,A_8` gives a valid actual word outside the collision hypothesis. This is **not** asserted to be an avoiding word.

The input hypothesis `R>=p+1` excludes a word with no rotation occurrences. It does **not** exclude an identity subsequence selecting zero rotations. The proof above constructs exactly two rotation occurrences and makes no nonexistence assertion about zero-rotation or higher-even-rotation selections. If an exact all-selection bookkeeping expression is desired, in `Z[X]/(X^p-1)` put

`S_x=[[0,X^x],[X^(-x),0]]`, `R_y=[[X^y,0],[0,X^(-y)]]`,

and form, in the original linear occurrence order, the product of `I+t S_x` over reflection occurrences and `I+t z R_y` over rotation occurrences. Matrix multiplication implements the displayed group law. In its `(1,1)` entry, `[t^(2p) z^0 X^0]` counts length-`2p` identity subsequences with zero rotations, while summing `[t^(2p) z^r X^0]` over even `r` counts all length-`2p` identity subsequences. Coefficients are nonnegative integer counts. This identity is bookkeeping, not a proof that the residual domain is empty.

## 7. Imports, scope, and read declaration

The proof above derives the needed finite-field sumset bound and actual-word consumer explicitly. It uses no unproved mathematical import from S1 or S2. Their linked f603 author, f638/f639 reviews, and f640 narrative/source/run receipt were **not** opened: any separate claim depending on those missing bodies or their historical review/execution details is a named conditional import and is not used here. All genuinely held episodes, including f602, and all their proof/method/selection/planning/verification/reporting/confidence/downstream consumers remain NONINPUT. No original-source correspondence, novelty, global theorem, or independent-family/human/formal review is claimed.

Before mathematical body access or assigned mathematical reasoning, I read the complete manifest, freeze receipt, final pre-dispatch binding, parent live metadata supply, actual-dispatch receipt, and all 22 listed controls as status/permissions only. I wrote `prebody-ack-v1.md` and directly sent the prebody acknowledgment to Main before opening the packet. The owned directory listing showed both new output names absent. The available write tool has no atomic exclusive-create flag; absence plus exclusive wave ownership was used, not a claim of atomic `O_EXCL`.

Afterward I read the complete sole literal packet part in order, in raw windows LF `1-15`, `16-30`, `31-45`, `46-60`, `61-75`, `76-90`, `91-105`, `106-120`, `121-135`, `136-150`, `151-165`, `166-180`, `181-195`, `196-210`, `211-225`, and `226-234`, including the ending. Every display was below 30,000 bytes and every window at most 20 LF. No packet clipping was observed or recovery needed. These windows cover S1 source lines 1–186 and S2 source lines 1–38 in full. Initial compact administrative displays elided portions; I recovered all five complete administrative records with raw reads before the acknowledgment. Parent-reported hashes and byte counts are administrative metadata, not independently executed hash checks.

The general memory summary and written-math acceptance-protocol skill were read as procedure, not mathematical premises. No other mathematical body or link target, peer scientific content, network, external model, code execution, scientific evaluation, test, compilation, solver, or child subprocess was used. The examples are written hand calculations. No verifier code was prepared, so there is no prepared-code hash. I do not claim to certify prior private cognition or historical nonexposure.
