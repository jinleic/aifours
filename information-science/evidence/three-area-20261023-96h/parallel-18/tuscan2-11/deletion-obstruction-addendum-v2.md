# Deletion obstruction addendum v2 — Dic3 closed by a written case split

Clock actually observed before creation: **2026-10-23T14:44:05-0700**. Read with immutable `deletion-obstruction-candidate-v1.md` (SHA-256 `a7ce2e0dd4bb7ddd6b3a0c573496e0340f58a44c3cc4f654b4863ad7edb041b7`) and `deletion-obstruction-addendum-v1.md` (`7f327786262f18967784fefb1d647c3a32d41af75eb7565e8751bad9bb9bbb50`). Status **CANDIDATE / WRITTEN ONLY / PARTIAL FOR UNRESTRICTED T2(11) / NOVELTY_UNCLEAR**.

**Claim:** no group-developed Tuscan-2 square of order12 can yield even a Tuscan-1 square of order11 by deleting one row and one symbol and closing the gaps. This closes only that deletion-construction family. It does **not** exclude non-group-developed sources, other order12 arrays, multi-point deletions, trades before deletion, or arbitrary Tuscan-2 squares of order11. The unrestricted target remains active.

No code, solver, scientific arithmetic program or enumeration was executed. The finite tables below are explicit written modular derivations. Both scientific assay requests and both uncompiled sources are superseded and remain **permanently HOLD / NEVER RUN**. A written route closure makes their proposed execution unnecessary.

## 1. Exact Dic3 arithmetic and inherited conditions

Write

`Dic3=<a,x | a^6=1, x²=a³, xax^(−1)=a^(−1)>`.

Put `R_r=a^r`, `X_r=a^r x`, with indices modulo6. Rotations R form a subgroup; the six X elements form its other coset. Directly from the presentation:

- `X_r^(−1)=X_(r+3)` and `X_r²=R_3`;
- right quotient `R_r^(−1)R_s=R_(s−r)`;
- right quotient `X_r^(−1)X_s=R_(r−s)`;
- right quotient `R_r^(−1)X_s=X_(s−r)`;
- right quotient `X_r^(−1)R_s=X_(r+3−s)`.

These identities fix all signs used in the case tables. In particular the +3 in the last formula is essential; using the dihedral formula there would analyze the wrong group.

The earlier proofs reduce any successful deletion to a starter

`A=(A_0,...,A_11)`

with

`A_0=R_0`, `A_10=v²`, `A_11=v`, `v∈{a,a⁵}`,

and `A_1` one of the six X elements. Its11 adjacent right quotients enumerate all nonidentity elements. Its10 distance2 quotients are distinct and omit exactly `A_1` from the11 nonidentity elements. The necessary actual edge matching is

`{(d_i^(−1),d_(i+1)):0≤i≤9}`

`= {(A_j,A_(j+1)):1≤j≤10}`.  (E)

We may take `v=a`, so `A_10=a²`, `A_11=a`. The map `a↦a^(−1), x↦x` is an automorphism of the displayed presentation and interchanges the two endpoint cases. We may also shift every X subscript by a fixed value, using the automorphism `a↦a, x↦a^k x`. Thus the first X element can be normalized to X_0 whenever convenient. These are actual group automorphisms, not unproved independent row/column normalizations.

## 2. A forbidden predecessor and exact R/X run counts

**Lemma 1.** In a starter satisfying(E), no nonidentity nonterminal element y can be preceded by y².

*Proof.* Suppose `A_i=y`, `A_(i−1)=y²`, `1≤i≤10`. Then `d_(i−1)^(−1)=y`. By(E) the bridge beginning at y must end at the actual successor `A_(i+1)`. Its endpoint is also `d_i=y^(−1)A_(i+1)`, forcing y=1. ∎

Every X element has square `t=a³`. Therefore **t cannot be immediately followed by an X element**. It is not the initial identity, not the endpoint a, and not the penultimate a².

Now record only whether each A_i is R or X. There are six of each. The type begins R,X and ends R,R. An adjacent right quotient is X exactly when the type changes; the adjacent quotient list contains six X elements. Hence there are exactly six type changes, giving four R runs and three X runs.

Let `c_i` be the0/1 indicator of a type change between positions i and i+1. Then c has length11, six1s, first entry1 and last entry0. A distance2 quotient is X exactly when `c_i≠c_(i+1)`. Since the distance2 list omits the X element A_1, it has exactly five X elements. Thus c has exactly five transitions. If h is the number of adjacent11 pairs in c, counting the two incidences of each1 gives

`2·6 −1−0 = 2h+5`, hence **h=3**.

An adjacent11 pair in c is exactly a singleton internal run of the original R/X word. Thus among its two internal R runs and three X runs there are exactly three singleton runs.

The first R run has length1; let the last R-run length be ℓ≥2. The two internal R lengths p,q satisfy `ℓ+p+q=5`. Thus either:

- ℓ=2 and `{p,q}={1,2}`; or
- ℓ=3 and p=q=1.

In the second case t cannot occupy either internal singleton R run, because it would be followed by X. It must therefore be the first entry of the final R run, making its last three entries `(a³,a²,a)`. But the last two adjacent quotients would both be a⁵. Contradiction.

Consequently the final R run is exactly `(a²,a)`. One internal R run is a singleton, and the other has length2 and begins with t=a³ (again t cannot precede X). Its second element z is a⁴ or a⁵; the other is the singleton. Exactly one internal R run is a singleton, so exactly two X runs are singletons. Their lengths are therefore **1,1,4**.

This forcing is exhaustive for the normalized Dic3 deletion model. It has not assumed column-Latin properties of the target.

## 3. Case I: the internal R double run is (a³,a⁴)

The R singleton is then a⁵. The adjacent rotation quotients contributed by the R runs are a (inside a³,a⁴) and a⁵ (at the end a²,a). The three adjacent rotation quotients inside the unique long X run must therefore have exponents `{2,3,4}`.

No two consecutive such exponents may sum to0 modulo6, because the corresponding distance2 quotient would be1. In particular2and4 cannot be consecutive. Thus the three exponents are `(2,3,4)` or `(4,3,2)`.

A long X run with first subscript b consequently has subscripts

- `(b,b+4,b+1,b+3)`, or
- `(b,b+2,b+5,b+3)`.

Each set is closed under the inverse pairing `r↦r+3`. The two missing X elements, which occupy the singleton runs, are also an inverse pair.

If the first X run were a singleton w, then w^(−1) would be the other singleton and would have an R successor. However(E), applied to d_0=w, forces its successor to be d_1, which is X because the first singleton w is followed by R. Contradiction of types.

Thus the long X run is first. Normalize its first element to X_0. Its inverse X_3 is the last element of that long run. Equation(E) forces the following R element to equal d_1, which is a² or a⁴. But the first following internal R element is either a³ (if the double run comes first) or the singleton a⁵. Contradiction. **CaseI is excluded.**

## 4. Case II: the internal R double run is (a³,a⁵)

The R singleton is now a⁴. The adjacent R quotients contributed by R runs are a² and a⁵, so the long X run's three adjacent quotient exponents are a permutation of **(1,3,4)**.

### 4.1 If the long X run is first

Normalize its first subscript to0. The six possibilities are:

| Long-run quotient exponents | Long X subscripts | Location of X_3=X_0^(−1) | Consequence of(E) |
|---|---|---|---|
|1,3,4|0,5,2,4|singleton later|d_1=a cannot be an R successor after any X run; those are a³,a⁴,a²|
|1,4,3|0,5,1,4|singleton later|same a contradiction|
|3,1,4|0,3,2,4|internal long-run position|actual successor of X_3 is X, but d_1=a³ is R|
|3,4,1|0,3,5,4|internal long-run position|same type contradiction|
|4,1,3|0,2,1,4|singleton later|R double run must precede the a⁴ singleton; see explicit cross list below|
|4,3,1|0,2,5,4|singleton later|same forced R order; see explicit cross list below|

For either last case(E) forces the successor of the singleton X_3 to be a⁴. Hence the R double run `(a³,a⁵)` follows the long X run, X_3 is the second X run, a⁴ follows it, and the other singleton X_h is third. The normalized starter has the shape

`1, [long X run ending X_4], a³,a⁵, X_3, a⁴, X_h, a²,a`.

Its six adjacent X-quotient subscripts, in occurrence order, are

`(0,4,4,2,h−4,h+1)`.

For the two actual h values they are:

| Long X subscripts | h | Six cross-quotient subscripts |
|---|---:|---|
|0,2,1,4|5|**0,4,4,2,1,0**|
|0,2,5,4|1|**0,4,4,2,3,2**|

Both repeat a quotient, contradicting the source Tuscan-1 condition. Therefore the long X run cannot be first in CaseII.

### 4.2 If the first X run is a singleton

Normalize it to X_0. The R run immediately after it starts either at a³ (the double run) or at a⁴ (the singleton). Equation(E) for d_0=X_0 forces the successor of X_3 to be

`d_1 = X_3^(? no additional inverse) R_r = X_(3−r)`,

where r is3or4; this displayed expression simply means `X_0^(−1)R_r`, using the fixed quotient formula.

If r=3, that successor would be X_0, which already has the identity as its predecessor in the starter. Thus r=3 is impossible. Hence the first internal R run is the singleton a⁴, the second is `(a³,a⁵)`, and

**X_3 must be immediately followed by X_5 inside the long X run.**

If the third X run were a singleton X_h, its entering and exiting quotients would be

`(a⁵)^(−1)X_h=X_(h+1)` and `X_h^(−1)a²=X_(h+1)`,

a repetition. Therefore the second X run is the other singleton X_h and the third X run is long. The full shape is

`1, X_0, a⁴, X_h, a³,a⁵, [long X run], a²,a`.

The long run has quotient exponents a permutation of(1,3,4), includes the edge X_3→X_5 (quotient a⁴), and cannot include the already used X_0. The six quotient orders give this explicit exhaustive table:

| Quotient order | Long X subscripts forced by X_3→X_5 | Other singleton h | Disposition |
|---|---|---:|---|
|1,3,4|1,0,3,5|—|repeats the initial X_0, not an ordering|
|1,4,3|4,3,5,2|1|cross list below|
|3,1,4|1,4,3,5|2|cross list below|
|3,4,1|0,3,5,4|—|repeats the initial X_0, not an ordering|
|4,1,3|3,5,4,1|2|cross list below|
|4,3,1|3,5,2,1|4|cross list below|

If b and c are the first and last long-run subscripts, the six adjacent X-quotient subscripts are exactly

`(0,5,h−4,h,b−5,c+1)`.

The four surviving ordering cases give:

| Long X subscripts | h | Six cross-quotient subscripts |
|---|---:|---|
|4,3,5,2|1|**0,5,3,1,5,3**|
|1,4,3,5|2|**0,5,4,2,2,0**|
|3,5,4,1|2|**0,5,4,2,4,2**|
|3,5,2,1|4|**0,5,0,4,4,2**|

All repeat an adjacent quotient. This excludes the remaining CaseII possibilities. Together with the two lists in §4.1, these are the **six explicit residual cross-quotient lists**; the other cases were excluded by symbol repetition or a direct type contradiction, not silently omitted.

**Theorem.** Dic3-developed Tuscan-2 sources of order12 cannot yield a Tuscan-1 square of order11 by one-row/one-symbol deletion. ∎

## 5. Why these groups cover the order12 group-source route

For completeness, only elementary Sylow theory is needed to classify the source groups; no inaccessible design-spectrum theorem is imported.

Let |G|=12. The number of Sylow3 subgroups is1or4.

- If the Sylow3 subgroup N is normal, choose a Sylow2 subgroup P of order4. Then `G=NP`, `N∩P=1`, so G is a semidirect product C3⋊P. Here P is C4 or C2×C2, and its action on C3 is trivial or has image C2. The trivial actions give C12 and C6×C2, both excluded by the abelian obstruction. The nontrivial C4 action gives Dic3: if n has order3 and c has order4 acting by inversion, take `a=nc², x=c`, obtaining the presentation above. The nontrivial C2×C2 action gives D12: with central involution h in the action kernel and an inverting involution s, take r=nh. These are the two nonabelian semidirect cases already treated.
- If there are four Sylow3 subgroups, the conjugation action gives a transitive homomorphism `G→S4`. Its image has order divisible4 and dividing12, so the kernel has order1or3. A kernel of order3 would be a normal Sylow3 subgroup, impossible; the action is faithful. Its image has index2 in S4 and hence is A4: every3-cycle maps trivially to the quotient C2, and3-cycles generate A4. The original A4 abelianization obstruction applies.

Therefore the abelian groups, A4, D12 and Dic3 exhaust the order12 group-developed source family. With the preceding manuscript/addendum, **that entire one-point deletion route is excluded in writing**.

## 6. Exact remaining target and review/execution boundary

This is a route-closure packet, not an answer to unrestricted Tuscan11 existence. A Tuscan-2 square of order11 need not arise by any deletion, nor from a group-developed source, nor from a Latin-column source. The unrestricted missing-distance2 digraph from Lemma1 of the original packet still has11 arcs with penultimate/second-position degree sequences; those degrees are not assumed1. That is the lane's next unrestricted written line.

The three-document candidate awaits actual separate in-harness and parent reconstruction at pinned bytes. Written case arithmetic is not a proof-assistant kernel or executable certificate replay. Correctness, scope, classical imports, finite/formal verification and novelty remain separate. No assay ran, no compiler produced a binary, and no checker/control result is claimed. Both `admission-request-group-deletion-v1.json` and `admission-request-dic3-deletion-v2.json` remain preserved, superseded, and permanently HOLD; their source files are historical unexecuted proposals, not evidence.
