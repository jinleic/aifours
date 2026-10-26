# v30-F — written review of rainbow insertion and the projective-family boundary

**Reviewer:** PhysicsRQLS10-2, physics-5. **Author:** InfoRecursiveMDS18. Actual pre-write `/bin/date`: **Sun Oct 25 04:27:50 PDT 2026**. Strictly written reconstruction/source reading; no scientific eval, arithmetic interpreter, enumeration, certificate replay, solver, nested agent or external CLI was used. Metadata hashes/clocks only.

## 1. Verdict and exact scope

**PARTIAL WRITTEN RECONSTRUCTION; NOT a PASS for the projective obstruction.**

- **General rainbow insertion theorem, spanning two-path requirement and ALL one-fixed-point regular-source obstruction:** reconstructed, **0 FATAL / 0 MAJOR / 0 MINOR** at their stated hypotheses.
- **Projective parametrization, safe affine normalization, necessary endpoint uniqueness and the conditional coloring-to-clique implication:** reconstructed, **0F/0M/0m**.
- I additionally give a direct written eigenvalue-ratio argument below for the two Hamilton normalized seeds and the220-row family cardinality. This replaces reliance on the printed ten-entry period table for those particular conclusions; it does not check any neighborhood/coloring data.
- **Theorem2's bound at most six, and hence the whole projective-family exclusion:** **NOT_RECONSTRUCTED**, with **one MAJOR load-bearing acceptance gap M1**, not an established mathematical counterexample. Exact compatible-neighborhood completeness and all same-color incompatibilities are neither proved by the literal packet nor hand-reconstructed here. Certificate data/replay are expressly outside this assignment. No finite coloring or clique bound is accepted.
- **Overall:** 0 FATAL findings, 1 MAJOR unmet finite-reconstruction obligation, 0 MINOR findings. This is not a claim of an erroneous analytic theorem; it is an explicit barrier to an end-to-end acceptance of the projective claim at the assigned source boundary.

Unrestricted T2(11) remains **OPEN**. The capped200000/500000-node calls remain **UNKNOWN**. Fixed-prefix exact-cover statements retain ONLY their literal fixed-prefix scope; their actual finite verdicts are not independently verified here.

## 2. Pinned exposure and complete reading

The exact v30-F entry is manifest LF181–209, SHA256 `99da25ec26aa7b7f35050105d206016ccd68dd6eb14b2cabb0b2f1b54d671154`.

The full literal source packet was read at **all LF1–175**, including both complete declared source ranges:

1. **R:** `information-science/evidence/three-area-20261023-96h/parallel-18/tuscan2-11/rainbow-split-and-projective-family-v1.md`, LF1–126, SHA256 `553831a49b73388c5bf72b5440b9a3f39124550920a277150944857e95728014`.
2. **A:** `information-science/evidence/three-area-20261023-96h/parallel-18/tuscan2-11/kernel-admission-correction-addendum-v1.md`, LF1–35, SHA256 `b3ca05c7e7710af1f987c2b100b7873602424ffd62b50f288a91f333b9e8d68b`.

Packet SHA256 is `10c9d773cdb5f932f610c774cba873ec8b9d3981c188e6fc08e8b3218d94691a`. The packet provenance receipt, all LF1–55, has SHA256 `c8c1bade3e6f074cd25e1df4d9af8666f0e7266babadccaa35be2cb926198871`; its v30-F record declares both source pins verified and literal bytes equal to the packet render. Fresh metadata hashes of the packet and both original source paths match the frozen pins.

The mandatory parent erratum v7, all LF1–39, was read; SHA256 `d5e1911bba6549684c93b2e910fac66eb44c353ae5dea2a8d1555516946e8d05`.

Long packet lines were additionally read explicitly with `:raw`: LF13,41,71,100,110,112,118,120–124,126,128,132–134,146–150,154–166,170–174. No omitted/truncated source body is treated as read by inference. Source line citations below use R/A numbering, not packet prefixes; packet R lines are source LF+8, and packet A lines are source LF+139.

**Not exposed/reviewed:** the linked coloring JSON, verifier bytes, kernel-checks JSON, earlier Etzion/endpoint packets or literal fixed prefixes. They are not in this assignment's two-source packet and are not silently imported as verified inputs.

## 3. General rainbow-path insertion: full written reconstruction

### 3.1 Required hypothesis — Hamilton decomposition, not an arbitrary orbit

R:17–23 assumes n−1 directed Hamilton cycles whose arcs partition the complete directed graph without loops. Exactly one arc is removed per source cycle, and the collection of removed arcs forms ONE directed Hamilton path P. These assumptions are retained throughout. In particular, a later group orbit is still required to be such a source decomposition; arbitrary developed cycles are not automatically declared arc-disjoint.

After cutting at its selected arc, each source cycle becomes a linear permutation row containing every other source arc. The inserted row P restores each selected arc once. Thus the distance1 events partition all ordered distinct pairs, proving the claimed Tuscan1 property in R:21. This does not assert distance2 compatibility.

### 3.2 Survival of every source occurrence

Fix the inserted distance2 event `(a,b)=(p_i,p_(i+2))` with c=p_(i+1). If a source cycle contains the cyclic triple `(a,m,b)`, cutting removes its distance2 occurrence only when the selected cut is one of its two constituent arcs `a->m` or `m->b`. Cutting at any other arc keeps the entire triple consecutive in the old linear row.

If `a->m` is the selected cut, that arc is an arc of P. A Hamilton path has a unique successor of a, namely c here, so m=c. Both arcs `a->c` and `c->b` then belong to that SAME source cycle. Since the source arcs form a decomposition, both have its same source color. But P contains exactly one selected arc of each color. This contradicts the rainbow condition. If `m->b` is selected, the unique predecessor of b gives the identical contradiction.

Therefore no cut can remove ANY source occurrence of `(a,b)`. If it occurred even once in the source, it survives in an old row and the inserted row creates a duplicate at linear distance2. Every inserted distance2 pair must consequently lie in M0. This proves R:27–33 without assuming cyclic distance2 uniqueness or any multiplicity bound in the source.

**Boundary verdict:** 0F/0M/0m. M0 is the auxiliary circular source missing graph; it is not identified with the final eleven linear defects.

### 3.3 Two directed paths spanning every vertex

The inserted distance2 pairs are precisely the consecutive arcs of the two index-parity subsequences

    p0 -> p2 -> p4 -> ...,
    p1 -> p3 -> p5 -> ....

Because P is a permutation, these are vertex-disjoint directed paths, of ceil(n/2) and floor(n/2) vertices, together spanning X. They have n−2 arcs altogether. For n>=4 both paths contain at least two vertices, so every vertex is incident with a selected missing arc. Hence M0 contains the required spanning two-path forest, has at least n−2 arcs, and has no isolated vertex. These are necessary conditions only, exactly as R:37–41 says. The conclusion would not justify the no-isolated-vertex assertion for n=3, which is correctly excluded.

**Boundary verdict:** 0F/0M/0m.

### 3.4 Every one-fixed-point regular source

Assume G fixes z, is regular on X without z, and its developed cycles are the source cycles from Section3.1. In a base cyclic word `(z,s1,...,s_(n−1))`, the cyclic distance2 events incident with z include `z->s2` and `s_(n−2)->z`.

For any fixed non-z symbol s, the map `g -> g(s)` is a bijection from G to X without z by regularity. Developing the first displayed event therefore supplies every outgoing ordered pair from z; developing the second supplies every incoming ordered pair to z. Thus M0 has z isolated, contradicting Section3.3. Nothing in this reasoning uses commutativity of G, a particular starter, or Latin columns.

For completeness, the developed cycles themselves have no nonidentity stabilizer: a group element fixing z and the directed base cycle must fix its successor s1, so regularity makes it the identity. This is consistent with the n−1 source cycles, but does not replace the original arc-decomposition assumption.

This reconstructs R:45–49 for ALL one-fixed-point regular sources satisfying the stated decomposition hypothesis. It excludes the specified one-cut-per-cycle, one-inserted-path mechanism, not every unrestricted Tuscan array or every multi-cut construction.

**Boundary verdict:** 0F/0M/0m.

## 4. Analytic part of the projective argument

### 4.1 Parametrization and uniqueness

A nonsingular two-by-two F11 matrix acts bijectively on the projective line Omega=F11 union infinity, modulo scalar. If its permutation is one12-cycle, deleting infinity from the cyclic orbit yields a linear row containing each finite symbol exactly once. Its successor map is determined by that row, including the final return to infinity. Thus two such projective maps cannot supply the same row.

A Hamilton successor cannot have c=0, since then infinity is fixed. Scaling to c=1 is therefore legitimate. This reconstructs the structural part of R:55–63; it does not assume an exhaustive list of row permutations.

### 4.2 Safe normalization and a written replacement for the Hamilton-seed census

For a chosen row, the unique affine symbol relabeling sending its first two distinct entries to0,1 fixes infinity. Conjugating its projective successor by that relabeling preserves the family, and simultaneously applying the relabeling to every row preserves each linear distance pair condition. No column rotation or wraparound is used.

For the normalized successor, c=1 and `T(infinity)=0` force a=0. Then `T(0)=1` forces b=d and d nonzero. Thus the normalized matrix has the form

    A_d=[0 d; 1 d], d in F11 without0.

Here is a purely written way to isolate the Hamilton values, independent of the source's full period table R:73–77. A12-cycle has projective order12. Since11 does not divide12, A_d is diagonalizable over a splitting field, and the ratio r of its two eigenvalues has order12. Trace d and determinant −d give

    r+r^(-1) = trace(A_d)^2/det(A_d)-2 = -d-2.

A primitive twelfth root satisfies `r^4-r^2+1=0`, hence `(r+r^(-1))^2=3`. Therefore `(d+2)^2=3` in F11. The two roots are d=3,4:5 and −5 are the two square roots of3, and a degree-two polynomial over a field has no other roots.

Conversely, for d=3 or4 the characteristic discriminant d²+4d is −1. This is nonsquare in F11: a putative x²=−1 would give x^10=−1, contradicting the nonzero-field-element identity x^10=1. Thus the two eigenlines are not F11-rational. The ratio r satisfies `r^4-r^2+1=0`, so r^6=−1 and r^12=1. Its order cannot divide6; the only remaining proper divisor of12 would be4, but r²=−1 would make `r^4-r^2+1=3`, not0 in characteristic11. Its order is12.

Every nonidentity projective power then has the same two nonrational eigenlines and no fixed point on Omega. Each point has orbit length12, so the action is one12-cycle. Consequently precisely S3 and S4 are the Hamilton normalized successors.

Finally each normalized seed has exactly one affine image for each ordered pair of distinct first symbols: the affine map is uniquely determined by those two images. The two orbits are disjoint, because an affine map fixing0 and1 is the identity. Hence the family cardinality is `2*11*10=220`. This is a written derivation of that cardinality, not execution credit from R:102–106. I have not reconstructed every other period in the ten-entry table, nor every entry of the printed S3/S4 eleven-symbol rows; neither is needed for this matrix-based count. The finite compatibility/coloring claim still needs its own data.

**Boundary verdict for the analytic normalization and220-row count:** 0F/0M/0m, at the explicit field/matrix argument above. No unrestricted row parameterization follows.

### 4.3 Endpoint uniqueness and conditional coloring implication

In eleven permutation rows, each symbol occurs eleven times. If it ends e rows, it contributes11−e outgoing distance1 events. A full Tuscan1 square has exactly ten outgoing distinct ordered pairs from that symbol, so e=1. The analogous incoming count proves exactly one starting row. This reconstructs R:88 without imposing Latin columns.

Every valid family square is therefore a clique in the graph whose edges require distinct starts/ends and disjoint distance1 sets and disjoint distance2 sets, SEPARATELY. After the legitimate simultaneous affine relabeling, choose its normalized seed S3 or S4. All other rows lie in that seed's complete compatible neighborhood.

IF that neighborhood is partitioned into four, respectively five, classes in which no two distinct rows are compatible, a clique contains at most one row from each class. Including the seed gives bounds five and six. This reconstructs the logical implication in R:90–96, conditional on the finite proper-coloring/completeness premises.

**Boundary verdict for this implication:** 0F/0M/0m. Its finite premises are NOT established here.

## 5. M1 — load-bearing finite identities NOT_RECONSTRUCTED

**Severity:** MAJOR acceptance gap, not an established false identity. **Sources:** R:92–106, especially R:92 and96; mandatory qualification A:27–33.

The following are load-bearing for the claimed six-row bound but absent from the assigned literal mathematical evidence:

1. **NOT_RECONSTRUCTED:** the S3 neighborhood contains exactly the declared32 compatible rows, with no omitted family row.
2. **NOT_RECONSTRUCTED:** the S4 neighborhood contains exactly the declared34 compatible rows, again with exact completeness.
3. **NOT_RECONSTRUCTED:** the supplied color classes cover each entire neighborhood exactly once and have respectively four and five classes.
4. **NOT_RECONSTRUCTED:** EVERY distinct same-color pair is incompatible under the correct separate linear distance1/distance2/end conditions.

The packet points to a JSON coloring object and executable verifier, but those bytes and their replay are explicitly outside this assignment. The verifier's printed VALID result and its four mutation outcomes are disclosed unadmitted computations, not premises establishing the four written identities. The two-source packet's assertion that these can be checked directly is not the checks themselves.

Thus **Theorem2, its six-row bound and its whole-family nonexistence conclusion are not accepted by this review**. This remains so even though the source family size220 has an independent written derivation above. The sharper five-row maximum/361-node exhaustion at R:98 is also NOT_RECONSTRUCTED and is unnecessary to the conditional six-row argument.

Closing M1 requires a permissible complete written reconstruction of the frozen literal neighborhood/color data at these exact scopes, or a new analytic argument covering them. This review neither requests nor authorizes a replay, and does not turn intentional certificate exclusion into evidence that the data are wrong.

## 6. Auxiliary finite claims, searches and process boundaries

R:112–116 reports several other computed family counts, exhausted restricted searches and capped runs. A:17–25 discloses their actual in-kernel computation. I do not independently reconstruct those finite outputs or promote their verification status.

- The200000-node union and500000-node unrestricted calls remain UNKNOWN, exactly as R:114–115 and A:21–22 state. No unstarted seed or unvisited branch is called exhausted.
- The literal five-/six-row-prefix searches concern those fixed prefixes only. Neither prefix is WLOG. The actual suffix census and exhausted finite verdict are NOT_RECONSTRUCTED here.
- The exact-cover recurrence in R:118 is logically sound IF all compatible provider rows are supplied: any completion must choose a provider for a selected uncovered distance1 arc, and all providers are branched. A zero-provider arc excludes that branch. The suffix-generation description R:120 gives a plausible definition-level completeness interface, but does not independently establish its reported625-row output or18-node exhaustion.
- No wrapping or cross-distance identification is introduced. Circular distance2 in the source is auxiliary to Theorem1; final square conditions remain linear and separate. Missing final distance2 pairs are not assumed to form a permutation.
- R:104's no-native-child statement is only that narrower statement. It is NOT a no-scientific-execution blanket: A explicitly discloses the scientific kernel work, no named GO, and no retroactive admission. Parent v7 assigns the incorrect blanket permission to the parent.

The admission addendum correctly prevents using unadmitted output as verification, while leaving the general written rainbow argument separately reconstructible. No fresh process-major finding against the author is invented here.

## 7. Final disposition

The written general insertion obstruction and its one-fixed-point regular-source consequence are reconstructed at their exact assumptions. The projective structural and normalization argument is reconstructed, including a written220-row count, but the finite neighborhood/coloring implication's premises are **NOT_RECONSTRUCTED** and block acceptance of the six-row/PGL-family exclusion. No supplied-proof review label is allowed to bypass that boundary.

This is a same-harness cross-domain written review, not blind, cross-vendor, human, formal, finite-certificate or novelty acceptance. It supplies no new T2(11) witness, no all-permutation impossibility and no upgrade of capped or fixed-prefix searches. No scientific computation was performed in this review. Sources and author root remain unchanged.
