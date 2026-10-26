# Tuscan-2(11): rainbow insertion barrier and exact projective-family obstruction

Observed `/bin/date` before creation: **Sun Oct 25 04:01:46 PDT 2026**. Owner `InfoRecursiveMDS18`, slot info-4. New successor; no pinned/reviewed file is changed.

**Status: WRITTEN; the explicit projective coloring certificate is WRITTEN-checked-in-kernel. PARTIAL FOR THE UNRESTRICTED TARGET.** No 11x11 witness and no all-permutation impossibility proof is delivered. No formal proof, independent-agent review, cross-vendor acceptance, or novelty clearance is claimed. All arithmetic below is over integers or the exact field F11, never floating point. `time.monotonic` is used only for bounded-search lifecycle metadata.

## 1. Unchanged target and imports

Every row is an arbitrary permutation of 0,...,10. Linear distance 1 must cover all 110 ordered distinct pairs once; the 99 linear distance-2 events must be distinct. No wraparound, column-Latin constraint, or identification of the two distances is imposed. The missing eleven distance-2 pairs are not assumed to form a permutation.

The primary formulation/status qualification remains [selection-v1.md](selection-v1.md). Earlier endpoint/root results retain the operative [endpoint addendum](unrestricted-defect-endpoint-addendum-v1.md) and their actual review boundaries. The square-root/phase packet is neither edited nor upgraded. The source's Example 2 is an old Tuscan-1 array, not a Tuscan-2 witness.

The only mathematical input needed below is the elementary definition of a directed Hamilton-cycle decomposition and the field arithmetic of F11. PGL(2,11) is defined explicitly in section 3; no classification or design-existence theorem is imported. The rainbow construction is a generalization of the literal insertion mechanism already reconstructed from Etzion in the older packet, not a new claim that the classical mechanism itself was discovered here.

## 2. A general obstruction to one-rainbow-path insertion

Let n>=4. Let C_1,...,C_(n-1) be directed Hamilton cycles on a common n-symbol set X, whose arcs partition every ordered distinct pair. Choose exactly one arc e_j from each C_j. Suppose these n-1 removed arcs, in some order, form one directed Hamilton path

`P=(p_0,p_1,...,p_(n-1))`.

Cut C_j at e_j, leaving a linear n-symbol row R_j. Adding P to the n-1 rows R_j always gives a Tuscan-1 square: each removed arc reappears once in P. Call this a **one-rainbow-path insertion**. The path is rainbow because its consecutive arcs have distinct source cycles.

Let M_0 be the directed graph of ordered pairs that do not occur at cyclic distance 2 in any source cycle C_j. This is the source's circular missing-pair graph, not the final square's linear defect graph.

### Theorem 1 — the inserted path must lie in the source's missing graph

If this insertion gives a Tuscan-2 square, then

`{(p_i,p_(i+2)):0<=i<=n-3} subset M_0`.

**Proof.** Fix an inserted pair (a,b)=(p_i,p_(i+2)), with middle vertex c=p_(i+1). Suppose a source cycle has a consecutive cyclic triple (a,m,b). Its occurrence is removed on cutting that source cycle only if its selected cut arc is a->m or m->b.

In the first case the cut arc is also an arc of P. Since a has the unique successor c in P, m=c. Both a->c and c->b then belong to that same source cycle. Their source-cycle colors would coincide, contradicting the rainbow condition. In the second case P's unique predecessor of b similarly gives m=c and the same contradiction. Thus **every** source occurrence of (a,b) survives in an old row. The inserted row adds another occurrence. Tuscan-2 noncollision is therefore possible only if there was no source occurrence at all. This proves the inclusion. No assumption on the source's distance-2 multiplicities was used. QED.

### Corollary 1 — spanning two-path-forest requirement

M_0 must contain two vertex-disjoint directed paths, on respectively ceil(n/2) and floor(n/2) vertices, that together span X. They are

`p_0 -> p_2 -> p_4 -> ...` and `p_1 -> p_3 -> p_5 -> ...`.

In particular M_0 has at least n-2 arcs and has no isolated vertex, because n>=4 makes both paths nontrivial. These are necessary conditions only; they do not ensure that the old rows are distance-2-compatible.

### Corollary 2 — every one-fixed-point regular development is excluded

Suppose the source cycles are one orbit under a group G acting regularly on X\{z} and fixing z, with |G|=n-1. This includes the usual multiplicative development on F11 with z=0, but is not limited to an abelian group.

Choose one source cycle written `(z,s_1,...,s_(n-1))`. Its cyclic distance-2 event from z is z->s_2, and the event into z is s_(n-2)->z. On development, regularity makes their other endpoints enumerate X\{z} exactly once. Consequently **every** ordered pair to or from z already occurs at source cyclic distance 2. The missing graph M_0 has isolated vertex z. Corollary 1 gives a contradiction.

Thus **no one-rainbow-path insertion into any such source can produce Tuscan-2(n), for any n>=4**. For n=11 this excludes every multiplicative starter, not merely Etzion's displayed starter, its add-zero orbit, or a bounded local trade neighborhood. No condition on Latin columns has entered the proof. This is a source-family obstruction, not a reason that every unrestricted Tuscan square has that source representation.

A construction must escape this route by changing the source symmetry, or by using a genuinely different multi-cut/multi-row mechanism. Repeating another regular starter or another rainbow path cannot evade the theorem.

## 3. A distinct direct row family: projective Hamilton successors

Put Omega=F11 union {infinity}. A nonsingular matrix `(a,b,c,d)`, taken up to nonzero scalar, acts by

`T(x)=(a*x+b)/(c*x+d)`.

A zero denominator gives infinity; T(infinity)=a/c when c!=0. A transformation that is one 12-cycle supplies the linear eleven-symbol row

`T(infinity), T^2(infinity), ..., T^11(infinity)`.

These rows are *not* assumed to be translates, to be a Latin array, or to have circular distance-2 noncollision. Every Hamilton successor has c!=0, since an affine map fixes infinity. Normalize c=1. Enumerating the integers a,b,d in 0,...,10 with ad-b!=0, and retaining only a single orbit of length 12, gives **220 distinct rows**. This is a finite family of allowable unrestricted rows, not a complete parameterization of all 11! row permutations.

### Safe affine normalization inside this family

Take any selected family row `(r_0,r_1,...)`. Conjugation by the affine map

`F(x)=(x-r_0)/(r_1-r_0)`

fixes infinity and simultaneously relabels every row. It preserves both linear pair conditions and this projective family. The chosen row now begins (0,1). Its c=1 matrix must have a=0 and b=d, so it is `(0,d,1,d)` with 1<=d<=10.

The exact orbit lengths of infinity for d=1,...,10 are

|d|1|2|3|4|5|6|7|8|9|10|
|---|---|---|---|---|---|---|---|---|---|---|
|length|10|5|12|12|10|5|11|6|4|3|

Hence there are exactly two representatives:

- `S3=(0,3,1,3)`, row `(0,1,9,3,6,4,2,5,10,7,8)`;
- `S4=(0,4,1,4)`, row `(0,1,3,10,5,9,2,8,4,6,7)`.

This is output-symbol relabeling, not a forbidden column rotation.

## 4. Compact obstruction certificate for the entire projective family

In any full square every symbol starts and ends exactly one row: the total available outgoing arcs from a symbol is ten, while its eleven appearances contribute eleven minus its number of terminal appearances; the incoming count is analogous.

Call two family rows compatible if they have distinct starting and ending symbols and their pair sets are disjoint **separately** at linear distances 1 and 2. Every pair of rows in a valid square must be compatible. Endpoint uniqueness here is a proved necessary global condition, not an extra Latin-column assumption.

The complete compatible neighborhoods of S3 and S4 have 32 and 34 rows. The delivered [literal coloring certificate](projective-coloring-certificate-v1.json) partitions them into respectively four and five classes. Every two distinct rows within one class are incompatible. All classes are supplied as actual matrices, not as search-dependent internal indices.

Therefore any pairwise-compatible set that contains S3 has size at most 1+4=5, and one that contains S4 has size at most 1+5=6. By safe normalization every hypothetical family square falls into one of these cases.

**Theorem 2. There is no Tuscan-2 square of order 11 all of whose rows arise by cutting infinity from Hamilton elements of PGL(2,11). Indeed the explicit coloring certificate bounds any compatible such set by six rows.**

This proof does not depend on a reported UNSAT result. Its finite certificate is an explicit graph coloring whose properness and completeness can be checked directly. A separate exact clique exhaustion found the sharper maximum five in the same family (361 search nodes); the written obstruction needs only the weaker six-row coloring bound.

### Literal verification method actually exercised

[verify-projective-coloring-v1.py](verify-projective-coloring-v1.py) reconstructs every matrix row from the formula, verifies the 220-row census, checks that exactly S3/S4 normalize to (0,1), reconstructs each complete compatible neighborhood, checks exact neighbor coverage with no omission or duplication, and checks every same-color pair. It uses Python integer modular inverses and finite sets only.

The delivered source bytes were executed **inside the existing owner eval kernel**, with `__name__` non-main. No Python CLI, native solver, subprocess, background job, or external model was launched. The verifier returned `VALID_RESTRICTED_FAMILY_OBSTRUCTION`, neighborhoods 32/34, colors 4/5, row bound 6, and explicitly `unrestricted_T2_11_verdict=UNRESOLVED`.

Four controlled corruptions were rejected for their intended reasons: non-Hamilton seed (`seed set`), omitted neighbor (`neighbor cover`), duplicated neighbor (`neighbor cover`), and an actual compatible pair moved into one color (`color class contains compatible rows`). This is one author's executable certificate check, not three independent implementations or a proof-assistant kernel.

## 5. Other finite exact checks and honest cutoffs

All actual check details, candidate definitions, bounds, per-case counts and output pins are frozen in [kernel-checks-v1.json](kernel-checks-v1.json). They are auxiliary evidence, not unrestricted impossibility proofs.

1. **Multiplicative starters.** Fix first nonzero symbol 1 and require all nine consecutive nonzero ratios to differ. Exhaustive depth-first propagation visits 19,250 nodes and gives 288 starters. Eight have all nine cyclic distance-2 ratios distinct. Theorem 1 excludes the entire rainbow insertion route even for these positive circular controls; finding another starter cannot help.
2. **Powers.** Rows `a*x^k+b`, k in {1,3,7,9}, a!=0, give 440 rows. Exact row-cover search exhausts all four affine-normalized seeds in 12 nodes, with no family square. Allowing every input shift `a*(x+c)^k+b` gives 3,740 rows; all 44 tested seeds exhaust in 2,584 nodes, no family square. Eleven linear seeds are redundant affine copies; retaining them does not invalidate exhaustion.
3. **Quadratic-residue union.** Five-element residue/nonresidue cycles were independently phased and oriented, concatenated or interleaved, with zero inserted at every position. Together with shifted powers, projective rows, and affine images of the literal Etzion rows, their affine closure has 484 orbits and 53,240 rows. The declared 200,000-node/20-second exact-cover bound reached node 200,001 after about 12.75 seconds. Only three seed cases exhausted; the fourth stopped. **The union is UNKNOWN, not obstructed.** No scope is inferred for the 480 unstarted seeds.
4. **Unrestricted search.** Safe standard form fixes row0 to 0,...,10 and orders remaining rows by starting symbol. Cell backtracking enforces both pair masks, row permutations, and distinct ends, with no other column constraint. Order3 exhausted as negative control; order4 reconstructed the known valid table. The order11 call reached its declared 500,000-node cap (node500001), with eight compatible complete rows on one branch. **UNKNOWN; no eleven-row certificate or nonexistence.**
5. **New residual-path exact cover.** Rather than merely extend that cap, all possible remaining row permutations compatible with one fixed five-row prefix were generated: 17,303 nodes, 625 rows. Exact cover of the remaining 60 adjacency arcs, with distance-2/end conflicts, exhausts 18 nodes and proves this prefix inextendible. The prefix is **not** assumed without loss of generality. This demonstrates an exact stronger propagation interface; it does not close other prefixes.

The exact-cover recurrence is definition-level: choose an uncovered distance-1 pair with the fewest currently compatible provider rows; branch over *all* its providers; intersect the candidate set with the selected row's compatibility set. A valid remaining completion must contain one of those providers. If any uncovered pair has no provider, the branch is impossible. Eleven pairwise-disjoint ten-arc rows cover all 110 pairs automatically. Time/node cutoffs interrupt this recurrence and do not certify its unvisited branches.

The 625-row suffix census is similarly exact at its fixed prefix: choose each unused starting symbol, append each unused symbol whose new distance-1 and distance-2 pairs avoid the prefix, and accept only unused terminal symbols. Every compatible row permutation appears once. Pairwise compatibility and complete adjacency cover then exactly encode that prefix's remaining completion problem.

## 6. Parked boundary

New substantive results are the general rainbow insertion barrier (including every one-fixed-point regular source) and the complete PGL row-family obstruction with a compact checked coloring certificate. The older source/phase results remain immutable and separately scoped.

**The requested unrestricted certificate-or-all-family-obstruction acceptance criterion remains unmet.** A positive still needs eleven actual arbitrary row permutations with all 110/99 pair events checked from the literal table. A negative still needs an argument covering every row permutation, not these finite/algebraic families. The quadratic-residue union and unrestricted capped search remain UNKNOWN. No scientific GO is requested or inferred; all historical held sources remain unrun. The new packets require separate reconstruction and parent disposition before any upgraded assurance.
