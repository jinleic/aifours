# Shor RAW completion — an exact b-marker reset and a positive noncommutative isolate residual

Owner MathShor-2. Actual `/bin/date` before composing: **Mon Oct 26 06:30:02 PDT 2026** (earlier observation bound). WRITTEN/unreviewed. This is a conventional symbolic proof from a hypothetical actual finite M and the fixed literal seed C. No invented example, parameter/control trial, numeric instance or withdrawn Taylor-packet guidance is used.

The NEW whole-existing-artifact qualified ACK/checkpoint40, SHA256 `40a78e97464ddc39fd416ae8cf6de470c5fd867ef487cc3e26f32002d3433d81`, was WRITTEN and SENT before further primary source/proof after parent v34. The entire withdrawn Taylor packet and its control remain ZERO-credit/nonpremises. Own earlier v109-A exactness MAJOR and NEW v34 written-scope MAJOR remain permanent. No scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent or new GO.

## 1. Literal arbitrary finite-code hypotheses

Let M be ANY finite RAW UD factor-complete code containing the literal Shor C. In particular b is a codeword, so no other pure-b word is allowed. Let L be the maximum actual length of a codeword of M. L is a symbolic property of the unknown finite M, NOT a chosen cutoff. Write X for the characteristic polynomial of M and X*=(1−X)^(-1), which is the actual characteristic series of M* because M is UD.

No condition on the number of b's, word lengths, arities, leading/trailing b-delays, pure-a order or actual one-b residue set is added. The proof is independent of I3/I4/I5 and of FACT extraction.

## 2. A genuine raw marker, not an abstract residue synchronizer

**Marker lemma.** In ANY parse of a word of M*, a cut whose L symbols immediately before it and L symbols immediately after it are ALL b must be a codeword boundary.

*Proof.* If a codeword crossed that cut, its length is at most L, so every one of its letters lies inside that displayed all-b neighbourhood. It would be a pure-b codeword of length at least2, forbidden by b in M and UD. ∎

**Sandwich consequence.** For EVERY raw binary word w,

    b^L w b^L belongs to M*.                             (SAND)

Indeed completeness embeds b^(2L) w b^(2L) in an M-product. The middle cut of each long b-marker has L b's on both sides, so both cuts are actual codeword boundaries by the lemma. The segment between them is exactly b^L w b^L and is an M-product. No cancellation of b inside an arbitrary submonoid is assumed; the cuts are proved boundaries in the ACTUAL parse.

**Synchronizing pair.** If u b^(2L) v belongs to M*, the central cut of that marker is a boundary. Hence u b^L and b^L v BOTH belong to M*. This is a raw-language synchronizing pair at the symbolic actual maximum length, not an inference from the finite complement automaton or a dimension bound.

It does NOT imply that cuts immediately next to an arbitrary w in SAND are boundaries: a codeword may cross b^L|w or w|b^L. Those crossing histories are retained next.

## 3. Finite actual boundary languages and an isolate language

Define FINITE languages by ACTUAL words of M:

- R contains the empty word and every nonempty suffix r for which b^i r is in M for some i>=1;
- T contains the empty word and every nonempty prefix t for which t b^j is in M for some j>=1;
- H contains every word h for which b^i h b^j is in M for some i,j>=1, with the two deleted b-pieces disjoint.

H has no empty word: that would require a pure-b codeword of length at least2. Every other definition keeps actual raw exponents, including residual b's if a cut is inside a longer leading/trailing b-run.

The underlying occurrences have no hidden multiplicity. Two different M-words giving the same suffix/prefix/isolate with different b-delays would, after enough common b-padding, produce two distinct M-parses, contradicting UD. Empty residual R/T comes only from a true codeword boundary, not a second copy from stripping the whole codeword b.

These are NOT arbitrary free-endpoint sets guessed from residue mates. They are the actual finite residual languages of the unknown M.

## 4. Exact positive series identity for EVERY raw word

**Theorem.** As noncommutative series with integer coefficients,

    (a+b)* = R X* T + H.                                (RESET)

The product and the displayed sum are UNAMBIGUOUS: every raw word has exactly one representation on the right, including the isolated case.

*Proof.* Fix w. By SAND there is an ACTUAL unique M-parse of b^L w b^L. Examine the two cuts immediately surrounding w.

If both cuts lie strictly inside the SAME codeword, the part between them is w and the outer parts of that word are nonempty pure-b strings. Thus w is one occurrence of H.

Otherwise there is at least one codeword boundary between or at the two cuts. The fragment of the first crossing word after the left cut is some r in R (or empty at a boundary), the fragment of the last crossing word before the right cut is some t in T (or empty), and all whole codewords between them form a word m in M*. Thus w=r m t.

Conversely any such isolate or triple is realized in b^L w b^L: add the defining b-prefix/suffix to form the actual crossing codeword(s), and use standalone b's to fill the remaining padding. Their lengths are at most L, so there is enough padding. When r and t are nonempty in the product case they correspond to separate crossing words; the isolate case handles the alternative of one crossing word, and no codeword is counted twice.

Two different right-hand representations, or two different delay occurrences defining one representation, would give DIFFERENT M-word lists for the SAME b^L w b^L. A tuple's internal M-factorization is unique by UD. The unique original parse therefore supplies existence and uniqueness of the whole right-hand representation. This proves coefficient1 for EVERY w. ∎

This theorem contains arbitrary many internal a-runs and b-gaps at once. It is not merely the pure-run PR equation. Restricting RESET to words a^r recovers a pure-run start/end/isolated identity, but no unrestricted raw coefficient is discarded here.

## 5. Explicit rational isolate defect, with no positivity-conjecture substitution

Put K=1−a−b. Since R,T contain the empty word, both are units in formal integer series. RESET gives

    K^(-1)−H = R(1−X)^(-1)T
               = K^(-1)(1−K H).

Inverting on the correct sides yields the exact rational identity

    1−X = T(1−K H)^(-1) K R.                            (DEFECT)

The defect denominator 1−K H has constant1 because H is proper, so its inverse is well-defined. It is not declared a nonnegative polynomial or silently removed. A finite M makes the ENTIRE expression a polynomial, but that finite cancellation is an actual remaining algebraic constraint, not an automatic formal-series realization.

If H were empty, DEFECT would simplify to

    X−1 = T(a+b−1)R,

with BOTH finite T,R nonnegative. In that special case the one-b coefficient identity gives Y_1(z)=G_n(z)+(z−1)J(z) with J coefficientwise nonnegative. Summing through degree14 would bound the number of one-b words with a-count<=14 by min(15,n), contrary to the sixteen literal Shor words. Consequently:

**Every hypothetical finite Shor completion has a NONEMPTY actual isolate language H.** The theorem does not replace H by a selected one-run word or bound its b-counts/gaps. The existing baseline already retains isolated words; the new point is the FULL noncommutative RESET/DEFECT relation and its all-word finite cancellation condition.

## 6. Relation to signed-factor necessity and exact unsolved bridge

The author-hosted Berstel–Reutenauer Chapter11 quotient identities motivate this representation, but §§2–5 prove the specialized b-marker case directly. No original proof of Reutenauer's general converse is consumed. Ordinary formal inversion and coefficient support, finite RAW UD and literal factor-completeness are the only inputs.

There is a separate algebraic route from DEFECT to finite signed factors: integer free-algebra inertia factorization of a polynomial product A B^(-1) C that is itself polynomial, followed by primitive linear-factor extraction. Those are named Chapter10 Corollary4.3/Proposition4.4 interfaces whose full weak-algorithm/inertia ancestry is NOT_RECONSTRUCTED here. They are not used to erase the isolate denominator or prove a new completion. I5 necessity therefore retains its stated trust boundary.

The genuine next step in THIS representation is to prove that the actual nonempty H required by the sixteen seed words makes the rational cancellation in DEFECT incompatible with finite RAW nonnegative X, or to supply actual finite residual languages and X satisfying ALL coefficients of RESET. A finite-state/residue reset, a low-arity count, H nonempty, or existence of formal inverses proves neither alternative.

All original unknown lengths, b-counts, arities, delays and orders remain unrestricted. Original Shor completion remains **NOT_PROVED** in either direction. H* is FALSE/WITHDRAWN; no commutative-prefix/factorization conjecture is assumed. FACT660 versus inherited full-code1320, I3/I4/I5 and parent LF58 qualifications remain separate. No withdrawn Taylor/control calculation is used or repaired in place.

All earlier process findings, including BOTH own permanent v109-A and v34 findings, remain uncured. No source/shared/frozen edit, git/deletion/publication, scientific GO or formal/kernel/human/configured-family/executable/novelty acceptance. Same original cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; research continues, no early final park.
