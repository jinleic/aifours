# f144 — Independent same-harness review of local regularity ⇔ abcda = abcacda

## Verdict and exact scope

**Corrected composite: VERIFIED at the band-identity scope, using the explicitly declared classical Green–Rees import. FATAL 0 / MAJOR 0 / MINOR 1 historical, repaired by the frozen additive erratum.** Both implications, both actual local substitutions, all four contexts, all 23 literal transitions (21 square contractions and two content absorptions), and their composition have been independently reconstructed. There is no remaining mathematical blocker at this scope.

**Original LF26, considered without its erratum: MINOR — an invalid one-premise inference, not a counterexample to the theorem.** The original sentence cannot stand as its stated justification. The original file remains unchanged; the later erratum supplies valid additional reasoning. This review does not retroactively treat the erratum as read before the original.

The statement reviewed is precisely: for every nonempty associative idempotent semigroup B, all eBe satisfy xyxzx = xyzx if and only if B satisfies abcda = abcacda, with all variables universally quantified. No embedding, canonical SEP/R/L, printed Q1/Q2, Billhardt–Szendrei assertion, priority, novelty, independent-family, human, formal/kernel, or whole-run acceptance is established here. The historical naming “seminormal in Billhardt's 1998 convention” is not independently source-verified here; the displayed identity is the definition used throughout.

## 1. Frozen inputs, complete coverage, and chronology

All input files were read completely, not inferred from their hashes. The same-author Python replay was read as text only; no author module, search program, executable or generated certificate was imported or executed as evidence.

| Input | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| manifest-v1.json | 24d290eac38f25d87fdaee0276f8ecae04609da0b20c810e852efc5e121f42d1 | 2488 | 30 |
| manifest-v2.json | 843b051c235415a7e5faed2cd9a36e59737770a1c6b05acafc4c2c5b11a46344 | 3566 | 43 |
| frontier-20261028-local-regular-seminormal-equivalence-v1.md | bf7af7afe0440fda2774231c99577fa1d36ebf4b12f70628eddc380a162663ee | 6295 | 118 |
| frontier-20261028-local-seminormal-proof-replay-v1.py | 29a4157f635a6576dee7ee3ea1f422704981bd25b6463eb13c192f29dc600bc4 | 2609 | 57 |
| frontier-20261028-local-seminormal-band-content-rationale-erratum-v1.md | dfedbf04821a2e60259e2d34631f336178ed73f867e79373d888926f4cb1262a | 1196 | 7 |

The evidence root for the last three files is `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding/`. Complete paths and renewed full SHA/bytes/LF checks are retained in `reviewer-f144-assurance-v1.json`. Its native-clock interval is 2026-10-29T05:07:41Z–05:07:41Z. Every input still matched both frozen manifests. The script's unused manifest-tuple LF field is not an asserted expected LF; the actual manifest-v1 LF count is 30, as independently recorded in the receipt above. Input-file LF values are explicitly enforced against the manifests.

Observed chronology, without invented exact read times:

1. Native clocks before the original manifest/input checks were 2026-10-29T04:09:18Z and 04:09:31Z. Under v1, I read the complete main proof, then the complete author replay, in that order.
2. Before the parent's erratum notification, my written analysis identified that X(XY)X = X does not itself establish equal R-coordinates, and supplied X(XY) = (XX)Y = XY as the needed separate reason. The public Cirpons slide source was read during this original analysis, following the observed 04:21:58Z toolchain clock. No exact PDF-read completion time is claimed.
3. The parent then notified me of the frozen v2/erratum. I verified v2 at the observed 04:26:57Z clock, read it fully, verified the erratum's SHA/bytes/LF at 04:27:07Z, and read all seven lines before reassessing the affected argument. The original files were rehashed unchanged. The pointer to original LF26 was confirmed; a subsequent clock was 04:27:31Z.
4. I later also completed the v2 declared text order erratum → full original proof → full author replay, before the 05:07:41Z final input recheck. These later full reads do not erase or backdate the original-source finding.

The owner authority was read at its named path, `contract-addendum-2-frontier-first-owner-direction-v1.json`. This is a new mathematical reconstruction; no earlier held output is adopted merely because local computation is now permitted.

## 2. Local monoids and implication SN ⇒ local regularity

Fix e ∈ B. Since B is a band, e² = e. Each eBe consists exactly of the values ebe with b ∈ B. Its multiplication is closed because (ebe)(ece) = e(bec)e; e is its two-sided identity, and it is a band as a subsemigroup of B. In particular e itself belongs to eBe, since eee = e.

Assume SN: abcda = abcacda. For arbitrary x,y,z ∈ eBe, substitute a=x, b=y, c=e, d=z. The two sides are xy ezx and xy exezx. Because e is an identity on these actual local elements, they become xyzx and xyxzx. Thus xyzx = xyxzx on eBe, exactly the specified regular-band identity with the sides reversed. This uses no hypothesis about global regularity.

The reviewer control also expanded x=exe, y=eye, z=eze and verified the two substitutions by literal ee → e deletions alone. **Disposition: VERIFIED, 0F/0M/0m.**

## 3. Content absorption: historical finding, corrected proof, and source assurance

### Historical finding — use the separate idempotence equation to establish equal R-coordinates

At original LF26, the implication “X(XY)X = X, so X and XY have the same R-coordinate” is not justified by that displayed equality alone: in a rectangular band every p,u satisfy pup = p, irrespective of their R-rows. In the explicitly checked 2×2 rectangular band with (i,j)(k,l) = (i,l), X=(0,0), U=(1,1) give XUX=X but different rows. This isolates the invalid inference; it is not a counterexample with U=XY, since that additional product structure supplies the missing reason. The separate identity X(XY) = (XX)Y = XY is essential to the intended coordinate argument. **MINOR; confidence 1.0; original LF26.** The frozen seven-line erratum now supplies exactly that reasoning. No further author edit is requested beyond retaining the erratum as part of the composite whenever this proof is consumed.

### Correct derivation of (C)

Let X,Y,Z be nonempty words, K=cont(X)=cont(Z), and cont(Y) ⊆ K. Work first in the free band on their letters. By the content/D-class characterization, X, XY and Z are in one D-class. With the standard band fact that such a D-class is a rectangular band, its multiplication satisfies pqr = pr. Apply this with p=X, q=XY, r=Z:

- X(XY) = (XX)Y = XY, by associativity and idempotence; hence X(XY)Z = XYZ.
- Rectangularity gives X(XY)Z = XZ.
- Therefore XYZ = XZ.

Equivalently, writing the rectangular product as (i,λ)(j,μ)=(i,μ), X(XY)=XY forces XY to have X's row; then (XY)Z and XZ have the same row and Z's column. This is the erratum's valid argument. I independently checked its elementary rectangular-band assertions and the historical counterexample in `reviewer-f144-assurance-v1.py`.

There is also a direct reconstruction from the exact Green–Rees R/L statement in the cited slides, without relying on the slides to spell out the rectangular-D-class fact. When |K|≥2, the longest prefix missing one K-letter and its next letter in each of XYZ and XZ occur entirely in the initial X; they are identical literal words/letters. Dually, the longest suffix missing one K-letter and its preceding letter occur entirely in the terminal Z and are identical. Green–Rees therefore gives both R- and L-equivalence of XYZ and XZ. H is trivial in a band: for idempotents p,q, p R q implies pq=q, whereas p L q implies pq=p, so p=q. The |K|=1 case is just equality of positive powers of one idempotent. Thus XYZ=XZ. The free universal property transfers this identity to every band under every assignment of the letters.

For the two actual uncontextualized (C) steps, my separate boundary calculation gives the identical data pref=`abcacbc`, ltof=`d`, ftol=`a`, suff=`bcd` before and after. Their right context `a` is then restored by associativity/congruence. This corroborates the general proof; it does not replace it by a selected finite instance.

### What was sourced, and what was not replayed

The directly read named source was [Reinis Cirpons, Computing in Free Bands](https://www-users.york.ac.uk/~varg1/2023_11_08_York_Semigroups_Computing_in_Free_Bands-corrected.pdf). Pages/slides 9–11 give the free-band quotient/universal setting, prefix/suffix operations and the Green–Rees (1952) D/R/L characterization; slide 17 states its recursive word-problem test. Slide 18 also explicitly states the Siekmann–Szabó (1982) rewrite rule XYZ → XZ under precisely cont(Y) ⊆ cont(X)=cont(Z), as part of a complete rewriting system. Slide 14 supplies the cardinality controls 1, 6, 159, 332380 used for the independent implementation.

This slide deck is an exposition of the classical results, not an independent replay of the original 1952 or 1982 papers. I did not read those original papers or prove Green–Rees or the general band D-class structure theorem from the band axioms. They remain explicitly named, unreplayed classical imports; no foundational/kernel verification is claimed. The Green–Rees theorem and all-band transfer suffice for the corrected proof above; completeness of the Siekmann–Szabó rewriting system is not needed for this candidate. The statement-matching source premise has **0F/0M/0m**; axiom-level replay of the imported structure theorem is **INCONCLUSIVE / not performed**, not silently promoted to verification. The original LF26 inference is the historical MINOR finding; the corrected composite (C) derivation is VERIFIED relative to the stated classical import.

## 4. Actual local substitutions and contexts for local regularity ⇒ SN

For arbitrary a,b,c,d ∈ B define L=XYXZX, R=XYZX. Under local regularity L=R for the following actual local elements:

| Instance | e | X=eAe | Y=eBe | Z=eCe | Left context | Right context |
|---|---|---|---|---|---|---|
| I | c | cac | cbc | cdac = c(da)c | ab | da |
| II | bc | bcabc = (bc)a(bc) | bcacbc = (bc)(ac)(bc) | bcdbc = (bc)d(bc) | a | da |

The letter `B` in the substitution-table slot is an arbitrary middle factor, not a new ambient band. Both c and bc are idempotent because every element of B is idempotent. The displayed six elements are literally e(ambient element)e, so lie in the correct cBc or (bc)B(bc); their membership is not guessed from word content. The independent control also verifies eXe=X for each literal word. Multiplication by the common external contexts preserves each local equality; no cancellation or identity outside eBe is used.

My own concatenation reconstruction produces exactly the four source words in the original text:

| Chain | Independently reconstructed start | Claimed and checked endpoint |
|---|---|---|
| I-left: ab L(c,a,b,da) da | abcaccbccaccdaccacda | abcacda |
| I-right: ab R(c,a,b,da) da | abcaccbccdaccacda | abcacbcda |
| II-left: a L(bc,a,ac,d) da | abcabcbcacbcbcabcbcdbcbcabcda | abcda |
| II-right: a R(bc,a,ac,d) da | abcabcbcacbcbcdbcbcabcda | abcacbcda |

Every equality is literal, including the contexts; arbitrary coincidences among a,b,c,d do not affect its validity. **Both substitutions, all actual membership premises, and both context pairs: VERIFIED, 0F/0M/0m.**

## 5. Every literal transition

`reviewer-f144-exact-controls-v1.py` extracts the actual four trace blocks from the pinned markdown, rather than manually rewriting them, and checks its independently reconstructed starts. Its own exact transition parser verifies the 23 arrows as follows. For a square witness (i,W), i is the zero-based start of WW in the source, and the target is exactly source[:i] + W + source[i+2|W|:]. Multiple possible witnesses do not weaken a valid step; one is listed below. The log retains the full before/after strings and all witnesses found.

| Chain | Step | Verified literal certificate |
|---|---:|---|
| I-left | 1 | square i=4, W=c |
| I-left | 2 | square i=9, W=c |
| I-left | 3 | square i=6, W=ccacda |
| I-left | 4 | square i=6, W=c |
| I-left | 5 | square i=1, W=bcac |
| I-right | 1 | square i=4, W=c |
| I-right | 2 | square i=6, W=c |
| I-right | 3 | square i=9, W=c |
| I-right | 4 | square i=8, W=ac |
| I-right | 5 | square i=6, W=cda |
| II-left | 1 | square i=9, W=cb (also i=10, W=bc works) |
| II-left | 2 | square i=5, W=cbca |
| II-left | 3 | square i=9, W=bc |
| II-left | 4 | square i=4, W=bcbcabcd |
| II-left | 5 | square i=1, W=bcabc |
| II-left | 6 | square i=0, W=abc |
| II-right | 1 | square i=0, W=abc |
| II-right | 2 | square i=1, W=bc |
| II-right | 3 | square i=4, W=cb (also i=5, W=bc works) |
| II-right | 4 | square i=8, W=bc |
| II-right | 5 | (C): P=empty, X=abcacbcd, Y=b, Z=cabcd, Q=a |
| II-right | 6 | (C): P=empty, X=abcacbcd, Y=c, Z=abcd, Q=a |
| II-right | 7 | square i=5, W=bcda |

For II-right step 5 the source is exactly X·b·cabcd·a and target X·cabcd·a; for step 6 it is exactly X·c·abcd·a and target X·abcd·a. In both, cont(X)=cont(Z)={a,b,c,d} and the single letter in Y is contained. Both steps are separately confirmed not to be single square contractions; (C) is genuinely load-bearing at these arrows. Every square contraction is an all-band equality because its W evaluates to an idempotent, regardless of whether W is itself a letter. The independently implemented Green–Rees invariant is also unchanged across every arrow.

**I-left, I-right, II-left and the five square steps of II-right: VERIFIED, 0F/0M/0m, without a free-band structural import. Both (C) factorizations/content premises: VERIFIED, 0F/0M/0m; their equality rule is supported as in §3. No literal rewrite counterexample was found.**

The first local equality therefore yields abcacda = abcacbcda, and the second yields abcda = abcacbcda. Symmetry/transitivity give abcda = abcacda for arbitrary a,b,c,d. **Implication local regularity ⇒ SN, for the corrected composite: VERIFIED, 0F/0M/0m with the stated classical import.** The independent invariant also distinguishes abcda from abcacda in the unrestricted free band; no erroneous global use of regularity or unconditional SN is hidden in this argument.

## 6. Independently constructed finite bands and exact controls actually run

All executable controls are reviewer-authored. The Green–Rees implementation was written after reading the author's text and code, not under a clean-room or provenance-isolated condition; its method shares the named theorem, so it is not evidence of methodological/family independence. The literal parser, direct finite-table checks and typed mutations supply distinct checks but remain same-reviewer/same-harness work.

### A finite band in the variety but not globally regular

The reviewer-authored exhaustive small-band search produced the following band on {0,1,2,3,4}, subsequently rechecked by two Python evaluators, including an independently parsed parenthesized-term interpreter. Rows multiply columns.

| · | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 3 | 4 |
| 2 | 2 | 2 | 2 | 2 | 2 |
| 3 | 0 | 1 | 4 | 3 | 4 |
| 4 | 4 | 4 | 4 | 4 | 4 |

The last evaluator verified all five idempotence cases and all 125 associativity cases. The actual local sets for e=0,1,2,3,4 are respectively {0}, {0,1,4}, {2}, {0,3,4}, {4}, with e acting as the identity on its set. All 625 local-identity assignments and all 625 SN assignments pass. Global regularity fails at x=1,y=3,z=2: xyxzx=0 whereas xyzx=4. Thus the control does not mistakenly conflate global regularity with local regularity. This finite-band witness needs no Green–Rees interpretation at all; its entire multiplication table is checked directly.

The search also produced an order-6 band outside both identity classes; its full table is retained in `reviewer-f144-assurance-v1.json`. It is associative/idempotent, has identity element 3, and fails local regularity at e=3,x=1,y=4,z=2 (left 0, right 5). SN fails at a=1,b=4,c=3,d=2 (left 5, right 0). This is an intended negative control, not a counterexample to the equivalence.

### Runs and receipts

| Reviewer control | Observed native-clock interval (UTC) | Actual result and limitation |
|---|---|---|
| exact-controls-v1.py, Python 3.14.3, -B | 04:27:49–04:27:59 | All substitution, trace, count, endpoint, invariant and direction checks pass; |FB(1..4)|=1,6,159,332380. Process exit 1 because one reviewer-designed negative control was actually a valid (C) move; see the preserved error below. |
| fb3-exhaustive-v1.cpp, clang++ -O2 -std=c++17 | 04:31:22–04:31:23 (compile/hash clock 04:31:20) | 159-element generated table: idempotent; 4,019,679 associativity assignments pass; 639,128,961 local and 639,128,961 SN assignments each have zero violations. Global regularity has 5670 violating triples. Actual exit 0. These finite-table facts do not require accepting the table as the free band. |
| small-bands-v2.cpp, clang++ -O2 -std=c++17 | 04:33:36–04:33:48 | All 698,603 labeled bands of orders 1–6 checked; LOC⇔SN and REG⇔the control identity abcda=abacda hold for every table. Actual exit 0. Counts by order: 1,4,35,604,16727,681232. This is bounded support, not the universal proof. |
| exact-controls-v2-mutations.py, Python -B | 04:34:38–04:34:38 | Repaired negative control; 1454 factor deletions checked: 440 accepted steps all Green–Rees equal, zero accepted/unequal; 1014 rejected, including 769 unequal and 245 equal but not one-step moves. Order-5 and order-6 example tables independently rechecked. Actual exit 0. |
| assurance-v1.py, Python -B | 05:07:41–05:07:41 | Fresh full input hashes/bytes/LF; original-inference rectangular counterexample; corrected algebra; exact two (C) certificates; reason-specific negative controls; third term-interpreter verification of both finite tables. Complete exclusive JSON receipt produced; the shell pipeline did not separately persist a waited Python return code. |

The table above abbreviates only the common `reviewer-f144-` filename prefix. The logs and `reviewer-f144-inventory-v1.json` bind complete filenames, SHA-256, bytes and LF. The FB(3) table SHA is `e90608af8514515e38682b0fac0fb70ed5749302772329f7ad2a26f3d6b4c0bc`. The assurance receipt SHA is `e9c2091901908b3d7bb1e9dcd8df47341f7002736bbb4b4c2664fcfb69c07b8a`. All scripts are retained for reproduction; no author script is needed.

The exhaustive enumeration has 120 order-5 and 9360 order-6 locally-regular-but-not-regular labeled bands, and 720 order-6 bands failing both local regularity and SN. These are labeled tables, not counts of isomorphism classes. Completeness here comes from assigning every off-diagonal cell every possible value with fixed idempotent diagonal; associativity pruning only rejects fully assigned contradictions. The universal theorem still rests on the written derivation, not a small-order cutoff.

### Intended-reason positive/negative controls

- Genuine square and content certificates are accepted. Breaking the square's second factor is rejected with `NOT_THE_STATED_CONSECUTIVE_SQUARE`.
- Changing Z so its content no longer equals X's is rejected specifically with `END_CONTENT_MISMATCH`.
- Adding a letter to Y outside cont(X) is rejected specifically with `MIDDLE_CONTENT_NOT_CONTAINED`.
- Removing the real right context `a` while leaving the source/target fixed is rejected specifically with `LITERAL_FACTORIZATION_MISMATCH`.
- The typed checker accepts only the expected rejection reason; arbitrary exceptions do not count as successful negative controls.
- Separate mutations of the actual rewrite remove a necessary first `d` or an unmatched letter: the literal parser rejects them and the independent Green–Rees invariant distinguishes the words. Mutating instance I's C from da to d or instance II's e from bc to b also fails to reproduce the required endpoints.
- The unrestricted free-band target words abcda and abcacda are distinct, and the local identity fails there at e=a,x=b,y=c,z=d. These checks are conditional on Green–Rees; the order-6 table is a separate import-free negative control.

## 7. Reviewer errors, optional searches, and process disclosures

These are not findings against the author and are not silently converted into successful checks.

1. **Mis-designed reviewer negative control, preserved:** exact-controls-v1 expected deletion `abcacbcdbcabcda → abcacbcdbabcda` to fail. In fact it is a valid (C) move with X=abcacbcdb, Y=c, Z=abcd, right context a. Its failure flag and exit 1 remain in the v1 log. The v2 control positively verifies this case and separately rejects deletion of the first d for the correct reason. All 23 original proof-transition checks had already passed in v1; the failed control does not refute any of them.
2. **Reviewer enumeration tally bug, preserved:** small-bands-v1 declared tally[8][8] but indexed masks up to 15, invalidating reliance on that run's tallies and generating false REG/CTL failures. The v2 artifact changes the second dimension to 16 and reruns the complete order≤6 enumeration. Only v2 counts are used above. Both original source and log remain retained.
3. **No import-free square-only reconstruction claimed:** optional reviewer bidirectional searches for the two (C) pairs, without the trailing a, returned NOT FOUND with insertion-factor bound 6 and word-length bound 20 (04:31:43–04:31:44 for C1; 04:31:44–04:31:48 for C2; actual exit 3). Broader length-24 searches were cancelled before the observed 05:08:03Z clock. Their last fully reported visited totals were 7,530,469 and 11,201,970; they have no completed success/failure verdict. The search's node cap is only checked at layer boundaries, not a hard resource admission bound. The two broader logs are partial and are not certificates of nonexistence. At the scope of an explicit square-only derivation of these two equalities, the result is **INCONCLUSIVE**. This optional gap does not weaken the reconstructed classical-import proof of (C).
4. **Output-directory deviation:** early control preparation wrote reviewer-prefixed session scratch files, and compiled four executables under `/tmp/f144-build/` (`fb3`, `bands`, `bands2`, `sqsearch`), outside the assigned review directory. This did not comply literally with the directory-only artifact restriction. No frozen manifest, author source, unrelated repository file or infrastructure configuration was edited. The deviation is disclosed, not retroactively authorized; those scratch outputs were not deleted. Subsequent durable evidence is in this review directory. No author contact, external-model call, paid API, Git command, publication, secret access, deletion or unrelated build/test/formatter suite was performed. The two optional jobs were explicitly cancelled through their own job handles.

## 8. Per-scope dispositions and final assurance boundary

| Exact scope | Disposition |
|---|---|
| eBe closure, identity and actual local-element membership | VERIFIED; 0 FATAL / 0 MAJOR / 0 MINOR |
| SN ⇒ every eBe regular | VERIFIED; 0F/0M/0m |
| Both local substitutions and contexts | VERIFIED; 0F/0M/0m |
| Each of the 21 literal square contractions | VERIFIED individually; 0F/0M/0m |
| Both literal content-rule factorizations and content conditions | VERIFIED individually; 0F/0M/0m |
| Original LF26 “X(XY)X=X, so same R-coordinate” rationale alone | MINOR, invalid inference; preserved historical finding |
| Erratum plus original as a composite rationale for (C) | VERIFIED using the stated classical import; the historical MINOR is repaired |
| Named Green–Rees source statement/applicability | VERIFIED matching statement in named slide source; 0F/0M/0m; foundational proof itself unreplayed |
| Local regularity ⇒ SN with corrected (C) premise | VERIFIED at full universal band-identity scope; 0F/0M/0m |
| Original author's claimed Python/C++ execution receipts | INCONCLUSIVE / not independently replayed; not accepted as evidence; own controls substitute for them |
| Explicit square-only derivations of the two (C) pairs | INCONCLUSIVE; optional searches do not discharge or contradict this stronger assurance scope |
| Historical terminology, embedding/SEP/Q1/Q2, novelty, family/kernel acceptance | NOT REVIEWED and not claimed |

**Overall correctness: correct for the prospectively corrected composite at the exact displayed band-identity scope. Confidence: 0.98.** The only source finding is the historical MINOR at LF26, explicitly repaired by the frozen erratum. The finite controls provide nontrivial positive/negative assurance, not a replacement for the quantified written proof or an independent-family/kernel certificate. The parent should consume original + erratum + this review together and separately record its own disposition.
