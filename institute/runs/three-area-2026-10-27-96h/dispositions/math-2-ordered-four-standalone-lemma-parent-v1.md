# Standalone ordered-four lemma over F_p (no application)

**Disposition: ACCEPT the finite-field sequence lemma under its fresh, application-free scope.** Native clock observed before composing: **2026-10-28T20:22:09-0700 PDT**. This record does **not** rehabilitate, salvage or transfer any part of the withdrawn f111 adoption; it is a new review of a new packet containing only the lemma. No actual-block, odd-run, raw-graph, floor, reflection-selector or L_RES statement is adopted here, and the original ordered-Olson problem remains open.

## Adopted statement

For every odd prime p and every sequence `z₁,…,z_(p+2)` over F_p with `z_i≠z_(i+1)` for all consecutive pairs, there exist indices `i<j<k<l` with `z_i−z_j+z_k−z_l=0`. No full-support or distinctness hypothesis is needed; length p+1 is sharp (e.g. `0,1,…,p−1,0`).

## Reconstructed proof

If the sequence has full support and no zero quadruple, the value `z_i−z_(i+1)+z_(i+2)` of each consecutive triple must occur inside that triple, hence in its middle by adjacency; so all steps equal a nonzero d and positions `1,2,3,p+2` give `−pd=0`. If some value occurs four times, or one value three times and another twice, a zero quadruple is immediate (disjoint/nested pairs or the `a,b,a,b,a` pattern); a triple with all other values single forces full support. Otherwise multiplicities are ≤2 with `s≥2` doubled values and exactly `s−2` absent values; doubled intervals must pairwise cross, and for every ordered pair of doubled values `(a,b)` the value `2a−b` (distinct from a,b because p is odd) must be absent, since any occurrence in any of the six positions relative to the crossing intervals yields a zero quadruple in increasing index order. Fixing a gives `s−1` distinct absent values, contradicting `s−2`.

## Evidence

- [Standalone candidate, 53 LF](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/ordered-olson/frontier-20261028-olson-ordered-four-standalone-v1.md): `18dbdfaf149d7ae31563d4cb87a78f61d455fd51db57a12d5bcc95be790261a5`; parent read completely; it discloses that the same statement appeared in the held source and claims no prior review credit.
- [Frozen manifest](../review-waves/f124-olson-standalone-ordered-four-new-scope/manifest-v1.json): `81efb7408a2e72633c62211e643be44a764dbc199f001b928c17895cf0264a64`, with the fatal correction `e11fd873…` as mandatory first input.
- [Fresh review, 127 LF](../review-waves/f124-olson-standalone-ordered-four-new-scope/review-v1.md): PASS, 0 FATAL / 0 MAJOR / 4 presentational MINORs; the reviewer did not open the old f111 body, review or controls. Its receipted control ran exhaustive pruned searches for `p∈{3,5,7,11,13,17}` with zero Q-free adjacent-distinct sequences and zero violations of the internal claims, confirmed sharpness at length p+1, checked all 31,960 named quadruple cases over odd primes ≤31, and showed adjacency is load-bearing (counterexamples exist without it). Its observation that the argument only uses oddness (so it also holds for Z/n with odd n) is a proof-dependency note, not adopted scope.
- The parent's own earlier finite controls (16 and 4,096 translation-normalized sequences for p=3,5) are consistent but are not credited from the withdrawn disposition.

## Boundaries

Any use of this lemma for reflection words requires a separately stated, literally defined actual-block correspondence and its own review; the author's new repaired-scope candidate and projection-only characterization are unreviewed. No novelty, human, independent-model-family or formal/kernel claim.
