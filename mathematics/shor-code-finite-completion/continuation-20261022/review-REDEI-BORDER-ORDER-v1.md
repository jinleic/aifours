# Bounded written review: Rédei border/order candidate

Before-creation clock observed with `/bin/date '+%Y-%m-%dT%H:%M:%S%z %Z'`: **2026-10-22T23:07:54-0700 PDT**.

## Verdict

**No mathematical defect found in the candidate's applied factorization/order argument, relative to its explicit R2 and inherited B/U8 inputs. Two wording clarifications below; no acceptance/promotion verdict.**

The replacement establishes the claimed consequence at a precisely identified theorem-import boundary. It does not authenticate the original monograph proof or Szabó 2006 Theorem 7. The condition on m is not a new mathematical restriction relative to the old conditional source statement: the delta is source support/presentation. It therefore does not by itself discharge the frozen target-B demand for an additional new condition.

This is one bounded in-harness written check, not an independent-model CLI review, a formal replay, a literature novelty clearance, or the blocked historical second-family gate.

## Pinned target and checked boundaries

- Whole target read: `proof-REDEI-BORDER-ORDER-v1.md`, lines 1–101. Observed SHA256: `7ac304f71a384d9acdf4529856f618a10e6859cb526d6ae51b83a90ba981f2a4` (matches the assigned snapshot).
- `../proof.md`: read whole during STEP0; this review reread the load-bearing §§3–7, requested lines 48–98 and 99–181, with reader boundary context. Observed unchanged whole SHA256: `fe22a69786a237e144c6e4f06c08bee9f8dcd3ac6cbd365b4fab054debf312e6`.
- `../sources/cordero2023.txt`: read whole during STEP0; this review reread lines 805–860 with context, including literal Lemma 5.2 at 815–817. Observed whole SHA256: `c2cc3649b9b9ad36a3b563b2a9c88fca7bc07406e43263cb44f43afa75e57f86`.
- Primary HTML opened: [Cordero arXiv:2301.13566v1, Lemma 5.2](https://arxiv.org/html/2301.13566v1#S5.Thmtheorem2). The first response exposed its opening through displayed lines 1–245 and was truncated; I did not treat that as a whole article read. A targeted grep located the lemma in the returned source artifact, and I read `artifact://25993:1195-1203:raw` untruncated. This includes attribution to SS09 Theorem 5.5, the hypotheses, and the complete lemma conclusion. No whole monograph/2006 proof authentication is claimed.
- Old conditional predicate checked against `../proof.md` §7 and `../evidence/hmz/actor-final/sources__szabo-2006-theorem7-excerpt.txt`, lines 26–34 (whole excerpt read at STEP0). Observed excerpt SHA256: `6a92a15c0ddfdd52c00519232b30a32810c94f4c02c04230c89aeff74d528131`.
- Procedural skill `research-contribution-sota-audit` was read for the distinction between correctness, priority and source status. Its broad delegation/search workflow was not run: this assignment expressly prohibits nested agents/CLI review and requests only the bounded comparison.
- Other continuation artifacts, including the newly listed `PRIMARY-SOURCE-CHECK-v1.md`, were not opened for this review. The author-hosted PDF was not fetched. No transitive proof search was performed.

## Findings

### F1 — Medium, target-B/status wording; not a defect in the numerical argument

**Locations:** candidate lines 9–13, 81–85, 93–99, particularly “New source-relative order restrictions” at line 99.

The candidate appropriately disclaims priority at lines 3 and 13. Nevertheless, its delivery should explicitly say that the m restriction re-expresses the old conditional condition, rather than merely disclaiming originality or describing it as new.

With the inherited `n=1320m`, the old predicate “there exist three pairwise distinct primes with `330*p1*p2*p3 | n`” is exactly “`4m` has at least three distinct prime divisors”, hence “m has at least two distinct odd prime divisors”. Conversely, two such odd primes together with 2 supply the old three-prime predicate. This comparison does not require disjointness from the prime divisors of 330.

**Required disposition:** replace/qualify the line-99 “New” wording and add an explicit sentence: the structural restriction was already implicit in the old conditional transcription; this manuscript supplies a better-sourced derivation, not an additional new target-B condition or a novelty result. Mark target B unmet by this manuscript alone. The source-status improvement can still be reported accurately under target A at the declared theorem-import boundary.

### F2 — Low, multiplier notation collision

**Locations:** candidate lines 44–50, especially line 48.

`B^(d)` is defined as pushforward, while the same plaintext shape `B^(ℓ−1)` is used where the calculation requires the ordinary convolution power. The adjacent `B^ℓ` indicates the intended argument, which is correct, but the notation makes two different operations look the same.

**Suggested clarification:** write pushforward as `T_d B` and the ordinary convolution power separately; for example, `F*(T_ℓ B)=F*B^{*ℓ}=W*B^{*(ℓ−1)}=|B|^{ℓ−1}W` in the characteristic-ℓ group ring. This is a notation correction, not a request for a different proof or a new lemma.

## Written checks of the applied chain

1. **Conventions and actual data — checked.** Candidate lines 33–35 agree with the inherited `proof.md` B2–B4: R is the right-exponent set from `b^s a^r`, L the left-exponent set from `a^l b^t`. Thus the inclusions, the map `(r,l) -> r+l`, and `|R||L|=n` use consistent factor orientation. The candidate does not confuse these names with the older actor's R/S convention.
2. **Normalizedness and generation — checked.** Both sets contain 0; R contains 1. The integer relation `3*3-8=1`, interpreted in the additive cyclic group, proves generation by L without requiring an individual member to be a unit. Normalization therefore requires no translation that could lose the forced residues. The actual application has `n>=20`; no trivial-group edge case is being used.
3. **Literal R2 statement — checked as an import.** The HTML says normalized factorization and `|P|=p^alpha q^beta`, with primes p,q and nonnegative exponents; its first proper-subgroup conclusion is written in words and the second includes explicit MathML `\langle Q\rangle\neq\mathbb Z_n`. This agrees with the retained text and the candidate's mathematical paraphrase. Exchanging factors is legitimate here. The lemma is stated/attributed there, not proved there as a self-contained monograph proof.
4. **M0, including multiplicity — checked.** The finite abelian group ring is commutative. In characteristic ℓ, Frobenius turns the ordinary ℓth power into the coefficient-counting pushforward. `W*B=|B|W` and Fermat give the displayed congruence. Nonnegative integer coefficients are then at least 1; their unchanged total is `|G|`, so every coefficient is exactly 1. Iteration over prime factors preserves total mass and composes pushforwards. No invertibility modulo the group order is assumed. F2 concerns notation only.
5. **`330 | |R|` — checked.** All four rows use the stated original pairs with distinct R preimages 0 and 1. Even if a nonunit multiplier collapses image points, the pushforward retains their multiplicities, so the two original contributions still force a coefficient at least 2. The first row excludes odd `|R|` using multiplier 8; the other rows force the primes 3, 5 and 11. Their pairwise coprimality gives the product divisor. No injectivity of multiplication on all of R was illicitly assumed.
6. **Three prime divisors on L — checked relative to R2.** Both generated subgroups are the whole cyclic group, so R2 with P=L and Q=R excludes zero-, one- and two-prime cardinalities for `|L|`. This is a restriction on the actual factor cardinality, not a claim inferred merely from the size of n. M1 already supplies four distinct primes on the other factor.
7. **Quotient and odd-prime condition — checked.** Writing `|R|=330a` gives the genuine integer quotient `q=ab` with `b=|L|`; positivity follows from a nonempty finite factorization. Thus three distinct prime divisors of b remain divisors of q even if they also divide 330. From `8 | 330q`, the cancellation of the factor 2 and coprimality with the odd factor 165 justify `4 | q`. This does not cancel all of 330 or remove overlapping prime multiplicities.
8. **Bound — checked.** With `q=4m`, at least two distinct prime divisors of q are odd; coprimality with 4 puts them in m. Their product divides the positive integer m and is at least 15. Consequently the stated `n>=19800` follows. The candidate explicitly avoids claiming a factorization/completion at that value.
9. **Inherited U8 interface — checked at its written boundary.** The candidate does not substitute the finite sanity tests or arithmetic-only Lean roots for the code-theoretic proof. The inherited §§3–6 give the all-t map, the unit lemma and the `8 | n` argument. The latter uses the prior `4 | n`, a unit with `8u=4 mod n`, the specified forced Y-pairs and their collision; the application has nonzero residue 4. No new failure was found in that imported written chain during this bounded scrutiny.
10. **Scope/source status — checked with F1.** The candidate continues to label itself a written consequence of R2, does not claim to authenticate Szabó 2006 or the monograph proof, and does not infer realizability, completion existence or all-order noncompletion. Its improvement is a more explicit source-supported route to a known-form restriction; F1 prevents that from being misreported as a new target-B theorem.

## Command/create ledger and limits

Only source/metadata shell commands were run in this review slice:

1. `/bin/date '+%Y-%m-%dT%H:%M:%S%z %Z'` — initial observed clock `2026-10-22T23:04:18-0700 PDT`.
2. `/usr/bin/shasum -a 256 proof-REDEI-BORDER-ORDER-v1.md ../proof.md ../sources/cordero2023.txt ../evidence/hmz/actor-final/sources__szabo-2006-theorem7-excerpt.txt` — four observed hashes recorded above.
3. `/bin/date '+%Y-%m-%dT%H:%M:%S%z %Z'` — pre-create clock recorded at the top.
4. Post-create metadata only: `/usr/bin/shasum -a 256 review-REDEI-BORDER-ORDER-v1.md` — result returned separately, without rewriting this file.

One exclusive new file: `review-REDEI-BORDER-ORDER-v1.md`; its absence was checked by directory read. No candidate, old audit, source, receipt or other artifact was changed. No code, solver, Lean, test, build, lint, model CLI or nested agent was run. This is not proof of the imported literature theorem, a novelty/SOTA certification, or either required historical model-family acceptance gate.
