# Actual nonreversible Tuscan core — reverse-pair normal form and the first surviving turn stratum

Observed `/bin/date` before creation: **Sun Oct 25 10:32:25 PDT 2026**. Owner `InfoRecursiveMDS18-2`, slot info-4. Consolidated immutable successor for the102319 primary continuation.

**NEW WRITTEN CANDIDATE / PARTIAL FOR UNRESTRICTED TUSCAN-2(11).** No scientific interpreter/eval, arithmetic or symbolic program, enumeration, solver, replay, compile, external CLI or nested agent. Written proofs and source/metadata reads only. V9/v10/v11 and HOLD remain binding. The full table-or-unrestricted-obstruction criterion is NOT met.

This paper retains ALL arbitrary/asymmetric arrays. It does not impose row-reversal symmetry: it counts which reverse partners actually occur. It derives restrictions on genuine center permutations and their full Hamilton row realization, not on an invented regular source. The global asymmetry/canonicalization candidate is NOT a premise.

## 1. Exact retained primary and qualified baseline

There are eleven arbitrary row permutations of X, |X|=11. All110 ordered distinct LINEAR adjacent pairs must occur exactly once; all99 LINEAR distance-two events must be distinct. There is no Latin middle-column, circular-distance, cyclic-development, independent-reversal, regular-deficit or finite-cap normalization.

The current boundary-turn interface is `unrestricted-boundary-turn-coupling-v1.md`, SHA256 `e54953336e35bd7a535d147ca6a564f9db30ddca966f1ad31dc58485167d8275`,191LF. Its complete source was reread for this push. The complete151LF mathematics reconstruction was read, SHA256 `acaa6029b30eee6c51f64ff6ff99a900c7b6aaf41d865f51ed4771634ddf7ee5`; the complete25LF current parent boundary was read, SHA256 `57f88518207f60db578f2fc2892969c133527304aba00d76a711a7a62fdebc0e`.

That boundary's10:04 claimed clock is WITHDRAWN by v11. No timing/cadence credit or backdating is inferred from it. Its mathematical support is the scoped same-harness written interface, not full Tuscan-2 existence, formal or novelty acceptance. The NEW core lemmas below need their own reconstruction; the old no-defect review does not cover them.

The v76-B review was fully returned and checkpoint008 written before this separate primaryACK/body. Earlier informal core reasoning recorded under the0853 continuation is disclosed, not relabeled preregistered. No old UNKNOWN or unadmitted scientific output is a premise.

## 2. Actual notation and the full coupled interface

For general n, adjacency coverage gives exactly one row starting and one ending at every symbol. Index rows by their start and write tau(s) for the end; tau is a fixed-point-free bijection.

Let f(v) be the second symbol of the row STARTING v and p(v) the penultimate symbol of the row ENDING v. F has arc v->f(v), G arc p(v)->v. Neither function is required to be bijective. Complete the actual internal-triple matching through v to a permutation K_v by the one added turn p(v)->f(v) and fixed point v->v. The only possible extra fixed point is p(v)=f(v).

On ordered distinct arcs define `T(a,v)=(v,K_v(a))`. It follows an actual row and then splices to the row starting at its endpoint. Thus a tau-cycle of length ell is exactly one T-cycle of length(n-1)ell. For a T-cycle C let I_C be its row-start set and r_C=|I_C|. Then

`length(C)=(n-1)r_C`.

The raw cyclic T-word lists the TAIL of each arc. Its number of occurrences of an original symbol a is

`nu_C(a)=r_C-1_(a in I_C)`.                               (V)

Proof: each Hamilton row contributes every symbol once except its END to that tail list, and its row ends run bijectively through I_C. This simple count is essential to the new argument; no Latin column is used.

For Tuscan-2 the full identity remains

`sum_v K_v=J+GF-M`,                                      (D)

where M is the ACTUAL simple zero-diagonal eleven-arc distance-two deficit. The disjoint ten-step first-arc layers and the Hamilton11 segment condition remain part of the exact iff. D alone, the endpoint polynomial or marginal degrees is not a replacement for actual rows. In particular GF=M is false as a general necessity, as the explicit genuine n4 control in v1 shows.

## 3. The split turn graph with arbitrary local cycles

For every original symbol v, make one split vertex for EACH cycle of K_v on X\{v}. Attach its neighbors as incident half-edges in that cycle order. The original unordered edge{a,b} joins the copy of a containing b to the copy of b containing a.

This is an undirected graph with exactly n(n-1)/2 edges. It has no loops or parallel edges: endpoints have different original labels, and a given original unordered pair occurs once. A split vertex has degree equal to its local cycle length. Degree1 is an off-v fixed point and is possible ONLY at the actual boundary backtrack p(v)=f(v). Degree2 is a local two-cycle. Degree>=3 is a noninvolutive turn cycle.

T runs on oriented edges by the local cyclic orders. Every T-cycle stays inside one split-graph component. Every actual row stays there too, since its successive arcs are a contiguous T-segment. Each component therefore has a closed subset of rows/endpoints, not merely a set of degree-feasible abstract edges.

## 4. No isolated degree-two cycle component can occur

**Lemma1. A component consisting entirely of degree2 split vertices is impossible in ANY actual Tuscan-1 square.**

Such a component is a cycle with m edges, giving two opposite T-cycles of length m. Their row counts are equal, r=m/(n-1), a positive integer. Reversing the undirected cycle preserves its multiset of ORIGINAL vertex labels, even if different split vertices share a label. Therefore the two T-cycles have equal nu_C(a) for every a.

Formula(V), with the same r, then implies their endpoint/start sets are IDENTICAL. But these are different T-cycles, hence disjoint tau-cycles, whose nonempty start sets must be disjoint. Contradiction.

This does not appeal to a global reversal automorphism. It is a count inside one actual split component and explicitly uses the Hamilton row property and unique endpoints.

## 5. Path components are EXACTLY actual reverse-row pairs

**Lemma2. Every path component has exactly n-1 edges and consists of one row and its exact reverse. Conversely every actual reverse-row pair forms such an isolated path component.**

For a path of m edges, T has one boundary walk of length2m, reflecting at the leaves. Each leaf is an off-v fixed point and hence an ACTUAL row boundary. The leaf-to-leaf distance m is therefore a positive multiple of n-1; in particular m>=n-1.

The row ending at one leaf and the row starting there traverse the same first n-1 path edges in opposite directions, because no branch is encountered. They are exact reverse Hamilton rows. Their endpoints swap, so their tau-cycle has length2 and their T-cycle has length2(n-1). But this path component has only its length2m T-cycle. Thus m=n-1, proving the first direction.

Conversely, if a row and its exact reverse both occur, at each internal symbol their opposite turns form one K_v two-cycle; at their endpoints p(v)=f(v) supplies the fixed boundary turn. These particular split copies have no additional incident edges. Their n-1 undirected edges consequently form an isolated path. Adjacency uniqueness prevents a third row from taking any of those directed arcs.

A useful variant follows: **in a branched component the distance from any leaf to the first degree>=3 split vertex is STRICTLY less than n-1.** Otherwise the two adjacent rows at that leaf would be exact reverses by the same argument, and hence would already form an isolated path rather than reach a branch.

These statements rule out a long-tail shortcut and make removing reverse pairs an ACTUAL normal form, not an assumed symmetry class.

## 6. At order11 at least FIVE rows have no reverse partner

Let R be the number of actual rows without an exact reverse partner. Remove all reverse pairs. By Lemmas1–2, the remaining split components all contain a degree>=3 vertex, and they contain precisely those R rows.

The remaining adjacency union is symmetric: the complete directed graph is symmetric, and each removed row/reverse pair removes both orientations of the same undirected Hamilton path. R has the same parity as n. A single remaining Hamilton path cannot have a nonempty symmetric arc set, so at odd order R>=3.

The next theorem excludes exactly three remaining rows when n=3 mod4.

**Theorem3. Three n-symbol Hamilton rows with distinct starts/ends and no repeated directed edge cannot have a symmetric adjacent-arc union if n=3 mod4 and their start/end sets coincide.**

For such three rows let U be their common three-element endpoint set. The endpoint map restricted to U has no fixed point, hence is a3-cycle. The underlying undirected graph has degree2 at U and degree3 at the other n-3 symbols: each row supplies one outgoing/incoming arc except at its unique end/start.

At a nonendpoint symbol all three occurrences are internal. The local predecessor-to-successor map is a fixed-point-free permutation of its three graph neighbors, hence a3-cycle with sign+. At an endpoint symbol the one internal turn maps two distinct neighbors; its endpoint splice completes their transposition, sign-. The product of local turn signs is therefore(-1)^3=-.

Arc reversal has sign `(-1)^(3(n-1)/2)`. For n=3 mod4 that exponent is odd, so its sign is also-. Their product, the actual arc-successor permutation, has sign+.

But the endpoint3-cycle splices the three whole rows into ONE cycle of length3(n-1), an even length, whose sign is-. Contradiction. This is a written permutation-parity proof, not a small-n search or a topology assumption.

After removal of reverse pairs, exactly three remaining rows have precisely these hypotheses: the removed pairs had equal start/end sets, so the residual endpoint set coincides; their directed adjacency union is symmetric. Thus for n11,

`R is one of{5,7,9,11}`.                                 (R)

This applies to ALL unrestricted Tuscan-1 arrays, hence every hypothetical Tuscan-2 target. It does not assume or use the unreviewed global-asymmetry theorem.

## 7. Exact branched-component frontier at n11

Each split component has a symmetric directed adjacency union and a closed row-start/end set. It cannot contain just one row, and two rows with such a union must use the same n-1 undirected path edges in opposite directions, making the component a path by Lemma2. Three rows are prohibited by Theorem3 at n11. Thus every BRANCHED component contains at least FOUR rows.

Consequently the complete possible row-count partitions of the branched part are:

|unpaired rows R|reverse pairs removed|branched-component row counts|
|---|---:|---|
|5|3|(5)|
|7|2|(7)|
|9|1|(9) or(4,5)|
|11|0|(11) or(4,7) or(5,6)|

This is only a partition of ACTUAL split components; it is not a catalogue of arrays, phases, nets or sources. Every component's face rows still visit ALL eleven original symbols. Its edges number5 times its row count, since both orientations of every undirected edge are covered by ten-edge rows.

There is a further lower bound with real structural content. If a branched component has an ODD number k of rows and endpoint set C, then at every original symbol v outside C its graph degree is k. It has NO boundary turn there, because the unique row starting/ending v belongs to another component. All its local cycles through v are therefore actual, fixed-point-free turns. An odd number of neighbors without fixed points cannot be partitioned into two-cycles: there is an odd cycle of length>=3.

Thus at least n-k distinct original centers have long cycles IN THAT component, and the total number of long-cycle arrows is at least3(n-k). At n11 this yields, for example:

- branched5 => at least6 noninvolutive centers and at least18 long-cycle arrows;
- branched7 => at least4 centers and12 arrows;
- branched9 => at least2 centers and6 arrows.

The bound applies to the odd component even when accompanied by an even4/6 component. One may not add center-count bounds from different components without checking overlaps; the long arrows themselves are disjoint cycle copies.

## 8. Boundary loops, reverse rows and an exact bad-turn budget

Let

- h=#centers with a local cycle of length>=3;
- m=TOTAL number of arrows in all such local cycles;
- beta=#centers with p(v)=f(v), equivalently `tr(GF)`;
- delta=#centers whose added boundary arrow lies in a local cycle of length>=3.

At odd n, an involution on the even-sized X\{v} cannot have EXACTLY one fixed point. Since there is at most one extra fixed point, every boundary loop p(v)=f(v) forces a noninvolutive K_v. Hence beta<=h and m>=3beta.

Each actual reverse-row pair contributes TWO distinct endpoint symbols with p=f. Therefore

`beta>=n-R`, `h>=beta`, `m>=3(n-R)`.                    (B)

In particular the R5 branch at n11 forces beta>=6,h>=6,m>=18; R7 forces m>=12; R9 forces m>=6. Reverse pairs are not a harmless way of evading the center-cycle constraints.

Call an actual internal turn BAD when its reverse at the SAME center is not an actual internal turn. At center v, all arrows in long cycles are bad except its possible added boundary arrow; if the boundary arrow lies in a2-cycle, its remaining reverse arrow is one additional bad actual turn; if it is fixed, it contributes no actual backtrack. Counting the three mutually exclusive boundary types gives the EXACT identity

`B_bad=m+n-beta-2delta`.                                (C)

A row with an exact reverse has no bad turns. Conversely if all of its n-2 reverse turns are actual, adjacency uniqueness traces its entire n-1-edge reverse contiguously inside one actual row; it must be that whole row. Thus every unpaired row has a bad turn and

`R<=B_bad`.

At n11, (R) yields the coupled necessary inequality `m+11-beta-2delta>=5`. This counts actual row/center/boundary objects, not just degrees of an arbitrary missing graph. It is still a necessary condition, not a complete contradiction.

## 9. The first long-cycle support m=3 is impossible at EVERY odd order

The known interface already gives m>=3 at odd order. A genuine new strengthening is

**Theorem4. At odd order, m>=4.**

Suppose m=3. There is one3-cycle at a single center v and all other off-v cycles are two-cycles, except possible boundary fixed points. Since |X\{v}| is even, the three-cycle leaves an odd number of other neighbors. Thus at this center there must be EXACTLY one extra fixed point; it is the boundary p(v)=f(v). All other centers are involutions and therefore have no extra fixed point at odd n.

The split graph has exactly ONE degree3 vertex and ONE leaf, both labelled by the SAME original symbol v; every other split vertex has degree2. By Lemma1 it has no disjoint degree2 cycle component. Its odd-degree vertices belong to the same component, so the entire graph is one connected lollipop: a cycle of length a and a leaf-tail of length b attached to its degree3 vertex. Its total edges are `a+b=n(n-1)/2`.

The two T-faces have lengths a and a+2b. Both are multiples of n-1. Lemma2's tail variant gives0<b<n-1. Since n is odd, the total edge number has residue(n-1)/2 modulo n-1, so

`b=(n-1)/2`, `a=(n-1)^2/2`.

The short and long faces therefore contain k=(n-1)/2 and k+1 rows. The boundary at the leaf v is in the LONG face, so v is in its endpoint/start set and not the short face's. Formula(V) says their raw v-counts are respectively k and(k+1)-1=k: EQUAL.

But the long face traverses the same cycle in reverse, preserving its original-label counts, AND makes the out-and-back tail excursion. Its branch and leaf are BOTH labelled v. That excursion adds at least two occurrences of original v (and possibly more from internal split copies). The long count must therefore be strictly larger, contradiction.

No symmetric-center, Latin completion or row automorphism was assumed. This closes the entire three-long-arrow regime of actual arbitrary rows, rather than a selected regular source.

## 10. Exact geometry if the minimum m=4 occurs

If m=4 at odd order, there is exactly one4-cycle at one center v; all other off-v local cycles are two-cycles. There are NO boundary fixed points: at the special center the remaining even neighbors are paired, and every other center is involutive on an even neighbor set.

Thus the split graph has one degree4 vertex, every other vertex degree2 and no leaves. Lemma1 excludes all separate cycle components, so it is connected. It consists of TWO edge-disjoint cycles meeting at the one degree4 vertex, a figure-eight, with lengths a,b and `a+b=n(n-1)/2`.

At that degree4 cyclic order, the four loop half-edges have two possible face types. Pair the two ends of each loop. If the4-cycle interlaces the two pairs, the successor on the four visits is a4-cycle and there is one T-face of length2(a+b). If not interlaced, there are three faces of lengths a,b,a+b. This is checked directly on the two loop pairs(12),(34): composing their return involution with a cyclic order(1234) gives two fixed visits and one2-cycle, whereas(1324) gives one4-cycle. Reversing/renaming the loop ends gives the same two alternatives.

The three-face case is impossible: a+b=n(n-1)/2 is NOT divisible by n-1 for odd n, contrary to the required T-period of that outer face. Therefore m4 forces the ONE-face interlaced case.

At n11 this means:

- T is one110-cycle and tau is one11-cycle;
- beta=tr(GF)=0, but f/p are STILL not assumed bijective;
- there are no reverse-row pairs, so R=11;
- all ten-step cuts must yield actual Hamilton11 rows and the SAME simple zero-diagonal M through(D).

These are necessary properties of the first surviving noninvolutive stratum, not a constructed tuple. The boundary placements, all eleven K_v and the T2 inequality remain coupled. No choice of figure-eight graph alone realizes the primary.

## 11. Full remaining frontier and first unproved step

The base exact iff remains unchanged: all eleven K_v, f/p with their actual boundary arrow, disjoint ten-step arc layers, Hamilton11 segments and entrywise0<=Gamma<=J-I must coexist. New results above derive an actual reverse-pair/core normal form, R>=5, the boundary/bad-turn counts, m>=4, and the forced one-face geometry at m4.

**No actual11x11 table and no obstruction for ALL noninvolutive systems is delivered.** The first unproved cases are:

1. m4's interlaced figure-eight/one110-cycle regime with all Hamilton cuts and simpleM enforced — still neither constructed nor excluded;
2. ALL m>=5 regimes, including every actual branched row partition in section7, still subject to the FULL boundary/turn/T2 constraints.

The new lower bounds do not assert that one of these systems is realizable, and do not permit deleting them. In particular GF=M, regular M, Latin middle columns, cyclic developments, independently reversed rows or a finite cap are still false/unlicensed shortcuts. No accepted asymmetry theorem is used.

These are NEW WRITTEN candidate proofs requiring actual separate reconstruction and parent disposition. The older accepted interface does not automatically validate the new core lemmas. Novelty, formal/kernel, human, configured-family and executable acceptance remain unperformed. The unrestricted original Tuscan-2(11) target, cutoff/deadline and HOLD are unchanged; research continues at the exact residual just stated.
