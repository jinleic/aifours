# Definition-first actual-row prerequisite: triangle holonomy is necessary for common realization, and pairwise collision-free compatibility does not imply it

Owner **InfoRecursiveMDS18-2**, slot **info-4**. Actual native prewrite clock: **Tue Oct 27 14:40:52 PDT 2026**.

**Status: new author-WRITTEN prerequisite result, unreviewed.** This is not a Tuscan-2(11) witness, universal nonexistence proof, support restriction, book-equivalence certification or novelty claim. It supplies a specific failure of a tempting pairwise-gluing implication, together with a full actual-row converse showing exactly what the missing common-realization condition is. The equivalence by itself is a representation, not progress; the substantive negative result is §4, which invalidates gluing from reciprocal pairwise collision-free relations alone, even when every individual relation is realized by genuine Hamilton rows.

## 0. Authority, sources and separation

This work is limited to the new prospective actual-rows release:
- S1 controls: SHA256 `0d81c1ac11d7a44de9d5c6a9e7720b2e2637a46da396e117c63fabdfa15f4e78`, complete LF1-19.
- Release JSON: SHA256 `a5a7e4b80e1ad3699f831215de55eb60f89827e2547030eac643c88102b99b05`, complete LF1-37.
- Exact literal packet: `institute/runs/three-area-2026-10-27-96h/written-releases/info-4-actual-rows-packet-v1.md`, SHA256 `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c`, complete LF1-37, 5650 bytes. Its S2 LF1-11 is the supplied original problem definition.
- Equality receipt: SHA256 `6dd395e5bdeaf4fd0248946b020a0dbc9d8d942f5b3a9048753521d1ea8d3007`, complete LF1-11.
- `actual-rows-prebody-exposure-ack-v1.json` was written at actual14:37:43 before this derivation.

S2 is Main's observed CPro1 PROB_DEF literal from its pinned first-party static source. It specifies the modern target; it is not represented as a verbatim-book quotation, HTTP-byte certificate or independent current-openness audit.

**Mathematical imports:** elementary bijections/permutation composition and inverses; finite counting/pigeonhole principle; elementary directed event indexing. All operative arguments are below. No old completed-turn, graph-splitting, lower-support, endpoint/converse, W44DB, type8, author-response, reviewer-bridge or v199-v216 result is an input. No old source, review, checkpoint or park was reopened. Prior authorship/exposure survives: this is not a claim of clean cognition or independent reconstruction.

No interpreter, calculator, arithmetic Eval, CAS, program, enumeration, solver, selected numeric/control/boundary probe, replay, modelCLI or new GO was used. The counterfamily below is an exact formula for every size and every pair of row identities, not a tested instance or a finite case scan. It refutes a relaxation, not a restriction of the original target.

## 1. All-variable original actual-row object

Let X be a set of n symbols and let R be a set of n row identities; the original problem has n=11. A row r is a bijection a_r:[n]→X. Write p_r=a_r^{-1}:X→[n]. Positions are linear: for d∈{1,2}, a distance-d event in r is

`(a_r(i),a_r(i+d)),  1≤i≤n-d`.

An event never has equal symbols. There is no wraparound, no restriction on columns, no symmetry assumption and no support premise.

For n=11 the requirements are:
- each distinct ordered pair of symbols occurs exactly once at distance1 across the eleven rows;
- each distinct ordered pair occurs at most once at distance2 across the rows.

Within one row, at a fixed distance an ordered pair cannot repeat, since its first symbol determines its unique position. Thus only collisions between distinct rows need checking. The two distances are checked separately: the same pair appearing once at each distance is NOT ruled out by the definition.

For distinct rows r,s, their **relative position bijection** is

`F_rs := p_s ∘ a_r : [n]→[n]`.

It maps a position in r to the position of the SAME symbol in s. This is about actual common labels, not separate relabellings for each pair.

Call a bijection q on [n] **short-jump admissible** if, for each d∈{1,2} and each i with 1≤i≤n-d,

`q(i+d) ≠ q(i)+d`.                                                  (A)

No inequality between q(i) and q(i+d) of any other kind is imposed. Fixed points, equal columns across rows, and cross-distance coincidences are allowed.

### Lemma 1 — pairwise event collision test

For fixed r≠s and d, an ordered distance-d event is repeated in r and s if and only if `F_rs(i+d)=F_rs(i)+d` for some legal i.

**Proof.** Put x=a_r(i), y=a_r(i+d). In s these labels have positions F_rs(i), F_rs(i+d). They form the same directed linear distance-d event exactly when the second position equals the first plus d. Conversely, such an equality automatically gives a legal starting position in s, since both images lie in [n]. No missing endpoint condition is assumed. ∎

Consequently an actual family of n rows is an original Tuscan-2 array iff every relative F_rs is short-jump admissible. For distance1, absence of repetitions is enough: n rows supply exactly n(n−1) events and there are n(n−1) distinct ordered pairs, so injectivity is also exact coverage. At distance2 this argument yields only the required noncollision, not coverage of all ordered pairs.

## 2. Mandatory common-realization coupling

### Lemma 2 — triangle holonomy

Every family of actual rows satisfies

- `F_rr = id`;
- `F_sr = F_rs^{-1}`;
- `F_st ∘ F_rs = F_rt` for all r,s,t.                              (H)

In particular, a closed triangle has trivial ordered product:

`F_tr ∘ F_st ∘ F_rs = id`.

**Proof.** The first two identities follow by inversion. For the third,

`(p_t ∘ a_s) ∘ (p_s ∘ a_r) = p_t ∘ (a_s ∘ p_s) ∘ a_r = p_t ∘ a_r`.

The cancellation is valid because the occurrence of a symbol in row s is unique and the SAME p_s/a_s pair is used in both relations. ∎

This is a common-label/common-row coupling, not a consequence of event counts or of assigning two Hamilton rows independently to each pair of row identities.

### Lemma 3 — exact converse, including actual row realization

Suppose bijections F_rs on [n] are supplied for all ordered pairs of row identities, with identities, reciprocity and (H). Then they are realized by a single common labelled family of actual Hamilton rows. Moreover that family is unique up to one common symbol relabelling.

**Proof.** Choose an anchor o∈R and an arbitrary bijection λ:[n]→X. Define

`a_r := λ ∘ F_or^{-1}`, and `p_r := F_or ∘ λ^{-1}`.

Each a_r is a bijection, so it is an actual linear row containing every symbol exactly once. The triangle identity for o,r,s is `F_rs ∘ F_or = F_os`, hence

`p_s ∘ a_r = F_os ∘ F_or^{-1} = F_rs`.

Thus EVERY supplied relation is realized at once by the same rows, with common endpoints and all event layers; no separate pair/triple-margin gluing is presumed. Another realization chooses a different anchor labelling λ′ and differs by the single common relabelling λ′∘λ^{-1}. Conversely, Lemma2 proves the necessity of all these identities. ∎

**Original-object caller.** If in addition (A) holds for each r≠s, the realized n rows satisfy both original event conditions by Lemma1 and the distance1 count. Conversely, every original array gives such a system. This is a full all-array equivalence at n=11, not an assertion that a system satisfying it exists.

**Degenerate cases and quantifiers:**
- r=s is excluded from (A), since a row must not be compared to itself. Repeated row identities in (H) are handled by identity/reciprocity; no special triangle exception is needed.
- Actual rows with identical orders would give F_rs=id for r≠s, which violates (A) when n≥2; they are not silently quotiented out.
- Both d=1 and d=2 range only over legal linear positions. In general n<3 the d=2 range is empty; the proofs still hold. Our target remains n=11.
- No old turn-system or row-realization theorem is used: the explicit a_r construction supplies the converse itself.

## 3. Exact failed implication

A tempting relaxation is:

> For each ordered pair of row identities independently, supply an admissible bijection F_rs; require reciprocal relations F_sr=F_rs^{-1}; conclude they can be glued into one n-row array.

The inference **from independent reciprocal pairwise admissibility to common realization** is false. Its missing hypothesis is (H), not another count on the numbers of distance1/distance2 events.

The next section proves this uniformly, rather than merely naming an unproved step or displaying a sampled numerical instance.

## 4. Uniform counterfamily: every individual pair is genuine, no triangle glues

### Theorem 4

For every integer n≥3, the relaxation of §3 has a reciprocal family of short-jump-admissible maps on n row identities that admits NO common family of actual rows.

**Proof.** Define the index reflection `J(i)=n+1-i` on [n]. Set

`F_rr=id`, and `F_rs=J` for every r≠s.

Then J is a bijection and J^{-1}=J, so reciprocity holds. For any legal i and d∈{1,2},

`J(i+d)-J(i)=-d`, which is not d.

Thus every non-diagonal relation is admissible. Each individual relation is in fact realizable by two genuine Hamilton rows: choose any one labelled order and take the other order whose position map is J composed with the first. The two rows share no directed event at the same distance1 or2, by the displayed calculation. This is a statement about each pair separately, not an n-row witness.

Take any three DISTINCT row identities r,s,t. Their supplied maps satisfy

`F_st ∘ F_rs = J ∘ J = id`, but `F_rt=J≠id`.

So (H) fails on every such triangle, contradicting the mandatory identity for actual rows. There is no simultaneous realization. ∎

**What this rules out.** Even exact local Hamilton realizations and reciprocal pairwise disjointness at both event distances do not pay the common-row gluing obligation. A collection of locally successful pairwise margins cannot be promoted to an original array without a consistency condition that couples at least three row identities. This failure already occurs with arbitrary size left symbolic and with every possible row-pair in the family included; no selected control was tested.

**What it does NOT rule out.** A coherent short-jump-admissible n-row family could still exist. The theorem does not exclude any original array: every original array already satisfies (H). It is a falsification of the relaxation, not of Tuscan-2(11).

## 5. Exact progress, gap and next admitted step

**WRITTEN result:** the local-to-global gluing inference of §3 is false, witnessed by the uniform family in Theorem4; its exact missing coupling is (H). Lemmas1-3 supply a complete original-object caller, including explicit actual rows in the converse and all linear endpoints, without relying on any old completed-turn or candidate result.

**Not claimed as progress:** merely introducing F_rs, stating (A), or recognizing an equivalent feasibility problem. Those are coordinate restatements. The new input-clean prerequisite finding is the precise falsification of the pairwise-only relaxation and the proof that its discarded triangle condition cannot be inferred even from genuine local Hamilton data.

**Remaining original gap:** find a coherent short-jump-admissible system on eleven row identities, with actual rows extracted as above, or derive a contradiction for EVERY such coherent system. No scientific bound, support exclusion, witness or original no-go is delivered. Every original support value remains in scope, and no earlier support theorem is imported.

**Next genuine admitted step:** examine whether an apparently cheaper substitute for full permutation-valued (H), such as sign-valued consistency, still permits nonrealizable locally admissible families. If it does, give an all-variable proof of the failure and identify the stronger missing coupling; do not select and test a finite numerical state. This stays within S1's definition-first actual-row/common-realization scope. No new external source or computation is needed or authorized.

**Ceilings:** author-written, unreviewed, same harness; no parent adoption, independent-family, formal/kernel, executable, human, priority or novelty clearance. Every old STOP/HOLD/ZERO finding, N4 UNKNOWN with historical exit unestablished, auxiliary214 STOP and the prior exposure record remains. Immutable successors only; original target remains OPEN.
