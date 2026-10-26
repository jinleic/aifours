# Unrestricted Tuscan-2: boundary-turn permutations, exact defect coupling and an odd-order local-cycle obstruction

Observed `/bin/date` before creation: **Sun Oct 25 09:46:12 PDT 2026**. Owner `InfoRecursiveMDS18-2`, slot info-4. ONE new immutable consolidated successor for the frozen0853 primary push.

**WRITTEN CANDIDATE / PARTIAL FOR UNRESTRICTED TUSCAN-2(11) / NOVELTY_UNCLEAR.** No scientific interpreter/eval, arithmetic or symbolic program, enumeration, solver, replay, compile, external CLI or nested agent. All derivations below are written. Metadata clocks/hashes and source reading only. Parentv9/v10, scientific HOLD and the original deadline remain binding.

The prior asymmetry/canonicalization paper is an UNREVIEWED candidate and is NOT a premise. No finite-family exclusion, old UNKNOWN cutoff or unadmitted arithmetic output is used. This successor starts directly from arbitrary row permutations and actual endpoint bijections. It does not impose a group, Latin middle columns or row-reversal assumption.

## 1. Full target and notation

Let X have n symbols, n>=3. A Tuscan-1 array here has n rows, each a permutation of X, covering every ordered distinct adjacent pair exactly once. Tuscan-2 additionally makes all n(n-2) LINEAR distance-two events distinct. No wraparound condition is included in that definition.

Every symbol starts and ends exactly one row: its n appearances have n-1 outgoing and n-1 incoming adjacent arcs. Index a row by its start s, and let tau(s) be its end. Thus tau is a permutation with no fixed point.

For each v define

- f(v): second symbol of the row STARTING v;
- p(v): penultimate symbol of the row ENDING v.

Neither f nor p is assumed bijective. Both differ from v at v. Define zero-one boundary matrices, with row-tail/column-head convention,

`F_(v,b)=1 iff f(v)=b`,
`G_(a,v)=1 iff p(v)=a`.

F has one entry per row, G one per column. Their product GF is an integer matrix, possibly with diagonal or repeated entries. The actual missing-distance-two matrix is denoted M; under Tuscan-2 it is zero-one, diagonal zero, with exactly n entries.

## 2. Complete each ACTUAL center matching — no Latin-column assumption

Fix a center v. In every row where v is internal, write its actual consecutive triple a,v,b. The predecessor a is different in all these rows, by adjacent-pair coverage. The successor b is likewise different.

The unique row starting v has no predecessor; its successor is f(v). The unique row ending v has predecessor p(v) and no successor. Consequently the n-2 internal triples define a matching from

`X minus{v,p(v)}` to `X minus{v,f(v)}`.

Complete it by

`K_v(p(v))=f(v)`, `K_v(v)=v`.

**Lemma1. K_v is a genuine permutation of X.** Its only possible extra fixed point, apart from v, is p(v)=f(v): an internal triple a,v,a is forbidden by the row permutation property. No Tuscan-2 uniqueness was needed for this lemma; adjacency and actual rows suffice.

The added arrow p(v)->f(v) is a BOUNDARY TURN, not an actual distance-two event. It combines the end of one row with the start of the row beginning at its endpoint. It must not be mistaken for a closing arc of one row.

## 3. The coupled exact matrix identity

Let Gamma count the actual internal distance-two pairs, with multiplicity if Tuscan-2 has not yet been imposed. Summing the center permutations counts:

- all actual internal triples: Gamma;
- one artificial diagonal arrow v->v per center: I;
- the n boundary turns: GF.

Therefore, for every unrestricted Tuscan-1 array,

`sum_(v in X) K_v = I+Gamma+GF`.                           (1)

Under Tuscan-2, Gamma=J-I-M, so

`sum_v K_v=J+GF-M`,

or equivalently

`M=J+GF-sum_v K_v`.                                      (2)

This is stronger data than choosing a graph with the correct missing degrees: GF is tied to the ACTUAL first/last-two boundary functions, while each K_v must come from all actual turns through v.

Taking row/column sums recovers, rather than assumes, the usual deficit identities:

`outdeg_M(a)=#{v:p(v)=a}`,
`indeg_M(b)=#{v:f(v)=b}`.

Both total n. The FULL matrix identity(2), not merely these marginals, is retained below. It neither proves nor assumes GF=M.

## 4. A small WRITTEN calibration that forbids a tempting false restriction

The following n4 array is checked directly from the definition:

```
0 1 2 3
1 3 0 2
2 0 3 1
3 2 1 0.
```

Its adjacent pairs are

`01,12,23;13,30,02;20,03,31;32,21,10`,

all twelve. Its distance-two pairs are

`02,13;10,32;23,01;31,20`,

eight distinct pairs. Thus its missing M consists of03,30,12,21.

Here f=(1,3,0,2), and p(0)=1,p(1)=3,p(2)=0,p(3)=2. Hence GF=I, NOT M. The completed center permutations are

`K0=(2 3)`, `K1=(0 2)`, `K2=(1 3)`, `K3=(0 1)`,

with all unspecified symbols fixed. Their sum is exactly J+I-M, agreeing with(2). This is a hand list of the actual turns, not a program replay.

Thus requiring GF=M would discard even a genuine Tuscan-2 array. In particular the center table need not complete to an idempotent Latin square in the boundary cells: some added turns land on an already occupied diagonal. No such convenience restriction is licensed at order11.

## 5. The actual arc-turn permutation and its endpoint polynomial

Let A be the n(n-1) ordered distinct arcs(a,v). Define

`T(a,v)=(v,K_v(a))`.

This is a permutation of A: K_v fixes v and permutes the other symbols, so the output is still a distinct arc and the inverse incoming neighbor is unique.

At an actual internal vertex of a row, T simply follows the next edge of that row. At its terminal arc(p(v),v), T moves to(v,f(v)), the first arc of the row STARTING v. Therefore it splices every n-1-edge Hamilton row into the row beginning at its endpoint.

**Theorem2 — exact period coupling.** Every tau-cycle of length ell corresponds to ONE T-cycle of length(n-1)ell, containing its rows in order. There are no other T-cycles. In particular

`det(zI_(n(n-1))-T)=det(z^(n-1)I_n-tau)`.                 (3)

Proof: all adjacent arcs are covered once and each row contains exactly n-1 arcs; the stated splice is bijective on row starts. A cycle cannot close inside one row or before all rows of that endpoint cycle have been traversed. The characteristic polynomial of a permutation cycle of length m is z^m-1, giving(3) factor by factor. This is a written structural determinant identity, not numerical determinant evaluation.

For n11 all T-cycle lengths are multiples of10 and at least20, since tau has no fixed point. In particular tr(T^k)=0 for1<=k<=19, and generally

`tr(T^(10k))=10 tr(tau^k)`.

Neither these period constraints nor the endpoint matrix alone guarantees Hamilton row segments; that condition remains essential.

### Exact sign coupling

Let alpha(a,v)=(v,a) be arc reversal and let sigma(v,a)=(v,K_v(a)). Then T=sigma alpha. The reversal alpha has sign(-1)^(n(n-1)/2); sigma has sign product_v sign(K_v). If c(tau) is the endpoint-cycle count, T has c(tau) cycles. Thus

`product_v sign(K_v)=(-1)^(n(n-3)/2) sign(tau)`.           (4)

At n11 the exponent is44, so the product equals sign(tau). This couples local actual turn cycles to the actual endpoint permutation without assuming a symbol automorphism or a regular source.

## 6. New odd-order obstruction: the completed turns cannot all be involutions

**Theorem3. In ANY odd-order Tuscan-1 array, at least one K_v has a cycle of length>=3.** This applies to every asymmetric array as well. It is a local-turn statement, not a repetition of the earlier global-automorphism obstruction.

Suppose instead all K_v are involutions. For each original symbol v split it into vertices indexed by cycles of K_v on X\{v}. For each unordered edge{a,b} put one undirected edge between the copy of a containing neighbor b and the copy of b containing neighbor a.

A two-cycle of K_v gives degree2 at its copy; an off-v fixed point gives degree1. There are no other degrees. The resulting finite graph is therefore a disjoint union of paths and cycles. Original unordered edges are unique and have different original endpoints, so this graph has no loops or multiple edges that would create an unaccounted case.

The T walks are precisely the directed boundary walks of these path/cycle components:

- A cycle with m edges gives TWO oppositely oriented T-cycles of length m.
- A path with m edges gives ONE T-cycle of length2m, reversing at its two leaves.

For a cycle component, Theorem2 makes m divisible by n-1. The two orientations together contain `2m/(n-1)` rows, an even number.

For a path component, each leaf is an off-v fixed point K_v(a)=a, and by Lemma1 this can occur ONLY at the designated boundary turn p(v)=f(v)=a. A reversal a->v->a cannot lie inside a Hamilton row. BOTH end reversals are therefore row boundaries. Their distance along the T-cycle is m arcs. Consecutive row boundaries are n-1 arcs apart, so m is divisible by n-1. The path consequently also contributes `2m/(n-1)` rows, an even number.

Every T-cycle is accounted for by these components, and Theorem2 accounts for all rows. Their total n would be even, contrary to the odd order. QED.

An immediate concrete consequence is that some actual center v has distinct outer symbols a,b,c with actual triples

`a,v,b` and `b,v,c`

in different rows. Indeed choose a cycle of K_v of length>=3; at most ONE of its arrows is the added boundary arrow. Removing that one arrow still leaves two consecutive ACTUAL arrows. This produces a genuine four-symbol nonreversible-turn pattern that every hypothetical order11 target must contain. It does not yet exclude that pattern.

The n4 calibration has all K_v involutions and an even number of rows, so this obstruction has the correct parity boundary. No arithmetic interpreter was used to check it.

## 7. An exact UNRESTRICTED construction/obstruction interface

The new representation is not a degree-feasible graph substituted for rows. The following data are equivalent to an actual Tuscan-2 square:

1. Permutations K_v of X fixing v; functions f(v),p(v)!=v with `K_v(p(v))=f(v)`.
2. The turn permutation T above and the distinguished first-arc set `B={(v,f(v)):v in X}` have DISJOINT layers `T^k B`, k=0,...,n-2, covering ALL ordered distinct arcs.
3. For each start s, the n vertices obtained along its distinguished n-1-edge segment are all distinct. Thus every segment is a Hamilton row, not merely an arc trail.
4. The integer matrix

   `Gamma=sum_v K_v-I-GF`

   satisfies `0<=Gamma<=J-I` ENTRYWISE.

Necessity was proved above. For sufficiency, condition2 gives each adjacent arc exactly once among the distinguished segments. It also implies T^(n-1)B=B: applying the bijection T to the layer partition leaves the already occupied layers1,...,n-2, so the last image must be precisely the missing layer0. Hence endpoints permute the starts, and the predecessor boundary arcs are exactly T^-1B={(p(v),v)}. Condition3 gives n actual row permutations and excludes equal starts/ends within a row.

Every nonboundary turn is then inside exactly one of those rows. Its ordered outer pair is exactly an entry counted by Gamma; the v->v terms were the artificial diagonals and GF the n boundary turns. Thus condition4 is precisely linear distance-two noncollision. Its total entry count is automatically n(n-2), leaving exactly n missing ordered pairs. This proves the FULL converse, retaining arbitrary asymmetric arrays and all original quantifiers.

No regularity of M, bijectivity of f/p, Latin columns, common phase, cyclic row development, independent row reversal or finite cap appears in this interface. A constructive tuple satisfying1–4 would give the literal11x11 certificate immediately. A universal contradiction to1–4 would be an unrestricted obstruction.

## 8. What has and has not been achieved

The new coupled identity(2), endpoint characteristic identity(3), sign relation(4), and odd-order noninvolutive-turn necessity are written results for ACTUAL arbitrary rows. The exact converse above keeps the missing Hamilton-segment realization step visible. They go beyond forbidding global symmetry, and the involutive regime is closed without imposing a regular source.

**The full order11 target is STILL UNRESOLVED.** No tuple satisfying1–4 and no literal11x11 table is delivered. No argument excludes all tuples with a noninvolutive K_v. The FIRST UNPROVED step is exactly the simultaneous realization/exclusion at n11 of:

- the boundary coupling `M=J+GF-sum K_v` with M simple and diagonal-free;
- the endpoint-period/first-arc layer condition, with a complete Hamilton11 segment at every cut;
- at least one noninvolutive center, as Theorem3 requires.

The nonlinear cycle condition alone and a graph with correct deficit degrees are not enough. In particular GF=M is false as a general necessity, and cannot be used to turn this into a convenient Latin-source problem. The earlier asymmetry candidate is neither needed nor promoted.

A short source check found no new literal11 solution in the bounded material consulted; no present-openness or novelty clearance follows. Anderson's1991 primary abstract at https://combinatorialpress.com/ars-articles/volume-032-ars-articles/a-family-of-n-x-n-tuscan-2-squares-with-n-1-composite/ constructs even sides2p under its prime congruences, not11. That classical source is not a premise of any proof here.

All frozen predecessors, scientific-admission qualifications and original acceptance requirements remain unchanged. This successor is a parkable WRITTEN partial representation/obstruction theorem, not a full-target verdict, formal certificate, independent reconstruction, parent acceptance or scientific GO.
