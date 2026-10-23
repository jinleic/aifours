# Olson LS+ partials: scoped lemmas accepted; LS+ and STAB stay open

Recorded at 2026-10-19T04:54:54-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIAL.** Lemma TV, Lemma RED+, Lemma SHIFT, Corollary SHIFT-C (with its LS version) and Lemma MAX hold as stated, read through the consolidated erratum. RED+(b) and SHIFT-C are conditional on H(kappa); the LS version is conditional on H'(kappa); SHIFT is conditional on LS+(p,kappa') for the stated kappa'. "STAB implies LS+" is accepted only as a conditional reduction. Candidate SO is HOLD (unreviewed, not granted). **LS+, STAB, LS, INV* and ordered Olson remain OPEN.** No novelty, significance or Lean claim.

## Texts
- [Partials](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-LSplus-partials-v2.md) `eedfa0f1…b6b2` and [MAX addendum](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-LSplus-partials-v2-addendum-MAX-v2.md) `4b0be3e3…51c7`, both unedited.
- [Consolidated erratum 1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-LSplus-partials-v2-erratum-1.md) `9438cd898c4ea294f8875952054337481a701488852cc1a32da0d8a56eba8630`, mandatory. The parent read it in full.

## Reviews
- [Codex](olson-LSplus-partials-codex-v1.prompt.stdout.txt) `89ba12944b2edd1ab585bcd3968afc8008fe0e4889b8c41badae9ec487bfceb1`: observed gpt-6.1-sol, effort max, read-only. Result: FATAL 0, MAJOR 0, MINOR 3. M1 asks for a shortest T in SHIFT-C; M2 asks for an integer witness in MAX; M3 asks that the side observation become a separate candidate.
- [Claude](olson-LSplus-partials-claude-v1.prompt.note.md) `f4a4557649936daa81fff270aa6fff7f2ca036c8ea236cee47432579b02d7ac3`: observed claude-opus-5-5, effort max, no tools. Result: FATAL 0, MAJOR 0, MINOR 9, with minimal repairs 1–8.

## Parent check of the erratum
The parent checked each repair against both reviews.
- **Item 1 (MAX).** The E2 interval width is a/3 with a = 2p−3e+2 ≥ p+3, using e = p−kappa and 3kappa ≥ 2p+1. The E3 width is (3kappa−2p+2)/3 ≥ 1. Both give ceil(x) ≤ floor(x'). The bounds 0 ≤ j2 and w2 ≥ p+e > 0 are added. The witness j* = max(j1,w1) ≤ min(j2,w2) follows from the four integer inequalities. c = 1 is delegated to Lemma TV.
- **Item 2 (SHIFT-C).** Odd kappa is handled by parity. Otherwise the erratum takes a shortest long T, so SLZ3 makes the complement X nonempty and sigma(X) = 0 gives the contradiction.
- **Item 3.** It states Fact S with the range 0 ≤ kappa' ≤ kappa0. It adds that z is even, kappa' ≥ delta = 2kappa−p ≥ 3 (delta is odd and ≥ (p+2)/3), and that all set notions are by occurrence.
- **Item 4 (RED+(a)).** The cut-down Y' = T plus 3kappa+2−|T| further occurrences uses only SLZ3 and heredity of (ZP). It does not use H(kappa).
- **Item 6.** It quotes LS from `80ae8041…`. The complement bound is |X| ≤ delta−1, which is even.
- **Items 5, 7 and 8** are citations, the status label for SO, and TV wording.

No lemma statement changes, and nothing new becomes load-bearing.

## Limits
The accepted [SLZ3 verdict](olson-SLZ3-parent-verdict-v1.md) and [S1-sharp verdict](olson-s1sharp-parent-verdict-v1.md) are imports. These partials are written mathematics with two CLI model reviews and a parent check; there is no Lean or human review. The [priority note v2](olson-priority-parent-note-v2.md) calibrates these partials as routine scaffolding toward LS+. STAB probe support is three cells with kappa ≤ kappa0+2 and is an aid, not a premise.
