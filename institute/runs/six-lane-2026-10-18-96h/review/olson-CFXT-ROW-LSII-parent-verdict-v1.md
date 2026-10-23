# Olson STAB prerequisites: CF, XT, RS/DGM-p/U, ROW, SH, AP and conditional LS-II accepted at exact scopes

Recorded at 2026-10-19T06:03:56-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL** for the prerequisite package, read through [erratum 1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/erratum-1-CF-XT-ROW-range.md) (`767fe8f8…`) and the mandatory consolidated [erratum 2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/erratum-2-prereq-consolidated.md) (`fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5`). **LS, LS+, STAB, TR and ordered Olson remain OPEN.** No novelty or priority claim.

## Frozen texts
- [proof-CF-XT-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/proof-CF-XT-v1.md) `aa602d45…191f`; [proof-ROW-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/proof-ROW-v1.md) `a7b73415…5b21`; [note-STAB-range-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/note-STAB-range-v1.md) `5b8faa3a…0115`; [proof-LS-caseII-v2.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/proof-LS-caseII-v2.md) `3df159ff…a73`. None was edited.

## Reviews
- [Codex](olson-CFXT-ROW-LSII-codex-v1.prompt.stdout.txt) `d049d5316f73b9f7ba2beb46e40f7f81daf1856262a97b99fd66902c21f9b3e9`: observed gpt-6.1-sol, max, read-only. FATAL 0; two MAJOR scope hazards (the E3 half of the XT corollary; the unscoped length-(3κ+2) dichotomy); one false intermediate inequality in AP; several MINOR.
- [Claude](olson-CFXT-ROW-LSII-claude-v1.prompt.note.md) `8decff2928613d01d646faa519b40d209dd1e43e6bf2025d2215aecc01ac3239`: observed claude-opus-5-5, max, no tools. FATAL 0; one MAJOR (the same dichotomy scope); MINORs per item.

Erratum 2 disposes every finding of both reviews (R1–R13). The parent checked the mapping item by item. Every repair is either a restriction or a proof rewrite, except R9, which relabels E5 as the new strengthened endpoint claim it is.

## Accepted statements (exact scopes)
1. **CF(a)–(c):** p≥5 prime, integer 0≤κ≤p−1, any odd generator g. (L) characterises a zero-sum of length ≥2p+2; this equals "long" only under (ZP_κ).
2. **XT(i):** p≥7, κ0+1≤κ≤p−2. **XT(ii):** κ0+2≤κ≤p−2. The corollary's E3 half holds **only** for κ≥κ0+2. At κ=κ0+1 with p≡1 mod 3, Codex's counterexample shows (−3h)³ is an admissible extension of E3(κ0).
3. **TR Proposition:** for κ0+2≤κ≤p−2, STAB(p,κ−1) and TR(p,κ) imply STAB(p,κ), with the STAB wording pinned by R3. TR is OPEN and the base cell κ0+1 is not covered.
4. **RS(a), RS(b):** RS(b) needs an integer K≥0 and nonzero terms.
5. **DGM-p and sharp Theorem U:** integer (p−3)/2≤κ≤p−1; DGM-p is vacuous at κ=p−1. The sharp example has no zero-sum longer than 2κ. U's κ=0 remark is withdrawn.
6. **Lemma ROW** under its two stated inequalities. The **LS-threshold dichotomy** holds for κ0+1≤κ≤p−2 and every (ZP_κ) odd Y of threshold length (the long zero-sum is not used). The **length-(3κ+2) dichotomy** is restricted to κ0+1≤κ≤p−2 **and** to the hypothesis that some generator has v_g≥p−e; it is not an LS+ reduction step.
7. **Endpoint results.** Y_(a,b) satisfies (ZP_(p−1)) for every prime p≥5 and distinct a,b. The p=11 example 1^21 5^10 is accepted. E5, a new strengthened statement: extending STAB to κ=p−1 fails for every prime p≥7; p=5 is undecided.
8. **SH(a,b),** conditional on H′(κ), with the parity and occurrence repairs. **Lemma AP** with the corrected proof of R6.
9. **LS-II,** conditional on H′(κ): a threshold LS counterexample is not in case (II). Codex's shorter completion after Step 2 is recorded as a valid alternative.

## Limits and accounting
The imports are Cauchy–Davenport, the accepted S1-sharp in its lower range, and RED. No finite computation is a premise. Lane-internal parameter calibrations are not literature priority. A [bounded priority screen](olson-new-cells-priority-scout-v3.json) found the newer lane cells LS(p,p−2) and BASE1 likely corollary-level given classical inverse theorems and Zeng–Yuan 2011 [INFERENCE]; that screen concerns the separate delta package. The delta package (unconditional LS-II′, LS-small, BASE1, LS+2, LS-lin) is NOT covered by this verdict.
