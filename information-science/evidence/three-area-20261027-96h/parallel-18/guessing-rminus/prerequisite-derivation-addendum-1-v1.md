# Addendum 1 — an unrestricted seven-marginal obstruction in the original graph

InfoGuessingRminus-2, original info-5. Actual preceding clock: **Tue Oct 27 14:57:05 PDT 2026**. New author-written UNREVIEWED material under the definition-first release; no change to frozen v1. No numerical instance, diagnostic substitution, program or source fetch.

Main classified the prior source over-display as a **source-scope deviation MINOR**, not a quarantine, and directed that its fragments not be used or recovered. That source line remains closed. Inputs here are only the admitted game definition, the already displayed Fig. 1 edges stated below, and elementary finite probability/counting. No held or ZERO guidance is an input. Prior exposure is not certified away.

## 1. Exact original-object statement

Let U={1,2,3} and T={4,5,6,7,8,9,10}. In the visual transcription of the original R-minus figure, U is a triangle, and every vertex of T observes a member of U. Only the following edges are used:

- 1–2, 2–3, 3–1;
- 1–4, 1–5, 1–6, 1–7;
- 3–8;
- 2–9, 2–10.

These edges are directly visible in the admitted Fig. 1 and survive deletion of 9–10. Additional original neighbours are retained; the decoders below may ignore their values, which the full-domain game definition permits. No graph is replaced by a selected subgraph.

**Theorem A (arbitrary-law extension).** EVERY finite joint law Y=(Y_t)_{t in T} extends to a finite original-R-minus FD law X whose T-marginal is exactly Y. For every subset A of vertices its entropy is

- H(X_A)=H(Y_A) if A is contained in T;
- H(X_A)=H(Y_T) if A intersects U.

Thus the projection of the UNNORMALIZED finite original-FD entropy region to the seven T-variables is the entire finite seven-variable entropic region. This is an original-class obstruction to treating the neighbour FDs as extra constraints on those seven marginal entropies alone.

**Theorem B (actual winning-law extension).** EVERY rational finite law P on the T-tuples is exactly the T-marginal of the UNIFORM law on the complete winning set of some genuine finite common-alphabet original-R-minus strategy. This preserves the source's independent uniform pre-game sampling and its full-domain decoders. No merely compatible subset is substituted for the actual winning set.

## 2. Proof of Theorem A, including all degeneracies

Let S be the nonempty finite support of Y. Choose q>=max(2,|S|) and an injection e:S->[q]. Embed each component alphabet of Y into [q]; it has at most |S| used symbols. Put

`X_1=X_2=X_3=e(Y_T)`,
`X_t=the embedded Y_t` for t in T.

Every U-coordinate is read from another U-coordinate along its triangle edge. Every t in T can recover its coordinate as a function of its designated observing U-coordinate, whose label determines the entire Y-tuple. Hence all original FDs hold simultaneously. Constant variables, point-mass Y, unequal component alphabet sizes and unused symbols are included.

If A intersects U, X_A contains an injective encoding of the full Y-tuple and consists only of functions of that tuple, so its entropy is exactly H(Y_T). If A lies inside T, its joint law is Y_A up to injective component relabelling. This proves the entropy formula. The other direction of the projected-region equality is immediate: projecting any original finite FD law gives an ordinary finite seven-variable law. No FD preservation under an unproved closure or marginalization operation is asserted.

## 3. Exact full-domain construction for Theorem B

Let P(y)=n_y/D for y in its finite nonempty support, with n_y positive integers and sum_y n_y=D. Let q>=max(2,D), and let C be any D-element subset of [q]. Choose a map pi:C->supp(P) whose fibre over y has n_y labels. Such a finite map exists by the integer-count hypothesis; it is not an executed enumeration.

Take c0 in C and define the complete alphabet function

`r(c)=c` for c in C, and `r(c)=c0` otherwise.

For the three triangle vertices use these legal full-domain rules:

- vertex 1 outputs the value seen at vertex 2;
- vertex 2 outputs the value seen at vertex 3;
- vertex 3 outputs r(value seen at vertex 1).

At t in T, read its designated U-neighbour: vertex 1 for t in {4,5,6,7}; vertex 3 for t=8; vertex 2 for t in {9,10}. If the observed label c belongs to C, output the embedded t-component of pi(c). Otherwise output a fixed alphabet symbol. These functions are defined for EVERY original neighbour tuple and ignore only permitted extra observations.

In an actual winning word the three triangle equations force
`x_1=x_2=x_3=c=r(c)`.
This holds iff c belongs to C: an invalid c is mapped to c0, which is different from it. For each c in C, all seven other coordinates are uniquely forced to pi(c)'s components. Conversely that full word wins at every vertex.

Therefore the actual winning set has EXACTLY D words, one for every c in C; no unseen-input completion can introduce a further fixed word. Under the source's independent uniform sampling, conditional on winning each of these D words has probability 1/D. Its T-marginal is exactly P, since pi's fibres have cardinalities n_y.

The construction includes D=1 and all deterministic marginal laws. The common alphabet remains at least two, and all decoder values outside the prescribed support are explicitly defined.

## 4. Consequence for candidate entropy inequalities

Suppose a homogeneous linear inequality involving only the entropies H(X_A), A subset T, is claimed to follow from the original ten FDs for EVERY finite original-FD law. By Theorem A it must hold for EVERY ordinary finite seven-variable law, with no FD restrictions at all. Conversely any universally valid seven-variable entropy inequality clearly holds on those marginals. Thus there are no additional R-minus-specific homogeneous entropy inequalities on that projection alone.

Even if a proposed argument is stated only for uniform laws on ACTUAL winning sets, Theorem B tests it against every rational finite seven-variable law. Approximating the probabilities of any fixed finite seven-law by rationals and using entropy continuity gives the same necessary universal-inequality condition.

This does NOT say Shannon inequalities are all possible: universal non-Shannon inequalities may still matter. It says that deleting the information-carrying triangle from the entropy model deletes every graph-specific constraint on the remaining seven marginal entropies. An inequality involving the joint ten-variable entropy, an entropy containing U, an explicit alphabet term or a normalized max-marginal budget is NOT covered by this projection-only obstruction.

## 5. Cost accounting and original-target caller

Theorem B spends a full U-label to name each of D winning words. Its winning count is D on a common alphabet q>=D. Thus it is not a strict-gain construction for the original lower target. For nondegenerate Theorem A, the full joint entropy and maximum one-coordinate entropy are both H(Y_T). This family therefore does not violate the homogeneous all-law bound needed for a guessing-number improvement.

The useful conclusion is the exact FAILED IMPLICATION: unrestricted seven-variable entropy data cannot be treated as graph-restricted merely because it arose as a projection of an original FD law, or even as a projection of an actual uniform winning law. The required coupling to the other three coordinates and their alphabet/entropy cost must be retained. This is stronger than a barrier for a selected architecture: it explicitly realizes ALL finite laws on the entire seven-variable marginal, and supplies the converse actual-word construction.

No original strict-gain FD law, unrestricted improved upper inequality, guessed numerical witness or new bound is supplied. The inherited interval remains unchanged. The remaining scientific prerequisite is still an all-ten-variable entropy gain/certificate that pays this coupling cost rather than eliminating it.

Ordinary imports: finite set maps, independent uniform sampling, injective relabelling invariance of finite entropy and entropy continuity. All graph-specific extensions and decoder equations were proved above. Exact source equivalence of the Fig. 1 transcription remains a written-source gate, not machine verification.

Same original slot, new exclusive root, scientific HOLD and deadline 2026-10-31T21:23:27.000Z. No stronger acceptance or novelty claim.
