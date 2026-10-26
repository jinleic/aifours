# math-5: exact Shor finite-completion target and attack freeze

Observed before this freeze: **2026-10-23T13:59:45-0700 PDT**. Owner: MathShor. This immutable selection does not reset the common deadline 2026-10-27T12:35:38-07:00.

## Literal target and source relationship

Let A={a,b}, with a and b distinct, and let

C = b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8}b{1,a^2,a^4,a^6} ∪ a^11b{1,a,a^2}.

Equivalently the exact pairs (i,j) for a^i b a^j are

- i=0: j=0,1,7,13,14;
- i=3: j=0,2,4,6;
- i=8: j=0,2,4,6;
- i=11: j=0,1,2.

Decide whether there exists a **finite** M⊆A^+ with C⊆M, such that concatenation from every finite list of words of M is injective (unique decipherability), and

    for every w∈A*, there exist u,v∈A* with uwv∈M*.

There is no bound or ansatz on |M|, word lengths, number of b's per word, algebraic symmetry, or pure-a order. This is exactly book pp.64–65 Question 1, transcribed in `mathematics/shor-code-finite-completion/source/problem.zh.txt` and bound to the literal instance `evidence/raw-instance.json`. Question 2 (decidability) is not the target. The modern bayonet/cyclic-factorization language supplies necessary conditions, not an established converse.

## Strongest matched baseline and trust

The current dossier and October 22 operative erratum were read. Existing results are not this round's discoveries:

1. Any finite completion contains a unique pure-a word a^n. Its actual borders R,L and one-b residue set Y satisfy |R||L|=|Y|=n and the all-t bijections

       R×Y^t×L → Z_n^(t+1),
       (r,(i1,j1),…,(it,jt),l) ↦ (r+i1,j1+i2,…,jt+l).

   R contains {0,1,7,13,14}, L contains {0,3,8,11}, and Y contains the exact sixteen pairs.
2. The current written multiplier/bridge proof gives 330 divides |R|, 2 divides |L|, and 1320 divides n. These are baseline interfaces, not a new bound.
3. October 22 imports Cordero 2023 Lemma 5.2 (Rédei cardinality restriction) to restate the earlier conditional result as n=1320m with m having at least two distinct odd prime divisors, hence n≥19800. The operative erratum explicitly says this is **not an additional new condition**. It will not be repackaged here.
4. Szabó 2006 Theorem 7 and its original proof remain unauthenticated. Cordero's authenticated statement is an external theorem import; the 2009 monograph proof has not been read. No hidden use of that proof or of the unauthenticated transcription is permitted.

Current primary statements actually read: Cordero 2019, introduction, exact code (2), lines 61–74 of the retained text, explicitly says inclusion in a finite maximal code was unknown; Cordero 2023, definitions 1.2/1.5, Theorem 1.4, Proposition 2.6, Theorem 7.2 and conclusion. The 2023 text explicitly leaves general n-cbc realization unresolved. Author publication page currently lists the 2023 paper as its latest item. Live searches for the precise completion/triangle/bayonet terms located no inspected later resolution. **Status: UNCERTIFIED-OPEN as of this bounded screen**, not proof of continued openness.

Primary links:

- https://www.normalesup.org/~cordero/Publications/A_Note_with_Computer_Exploration_on_the_Triangle_Conjecture.pdf
- https://arxiv.org/html/2301.13566v1
- https://www.normalesup.org/~cordero/

Local openai/math CONTENTS/overview/Lean docs and TeX corpus were screened for exact Shor/bayonet/triangle-completion terminology; the returned Shor hits in quantum algorithms/capacity are unrelated. The live remote CONTENTS was also searched with no target match. Remote CONTENTS latest commit metadata returned 301488868beec11bfd897168433b0a64f5258559 (2026-10-08). This is a bounded claim screen, not a correctness audit of that corpus.

## Missing ingredient and consequential delta

The missing ingredient is not lower-bound arithmetic: one must either exclude **every** admissible all-order tiling/finite realization, or construct an actual finite UD complete M containing C. A cyclic border or n-cbc alone cannot be promoted to a completion. A consequential partial result would be an additional proved structural restriction not implied by the existing predicate, or an explicit realization/certificate protocol with a genuinely new mathematical bridge.

## First bounded attack

Written attack only: strengthen the completion-to-border interface by using the full factor-coprime multiplier closure (Cordero 2023 Theorem 7.2), rather than repeating the known unit-only arithmetic. Derive exact orbit/valuation obstructions for *unknown* added words and borders, then test symbolically whether these force a new cardinality/periodicity/realization restriction. If the literal known sixteen-word orbit cannot yield further contradictions, prove and delimit that saturation instead of reporting finite failed searches. A second written route is the finite realization interface: identify a certificate carrying actual raw words, UD, and Bernoulli/Kraft completeness, not merely residue data.

## Verification and redirect condition

Any complete candidate is frozen on pinned bytes before a parent and a separate in-harness reconstruction. Correctness, imported-source trust, scope, novelty, significance and formal status remain separate. No Lean/kernel claim from arithmetic or graph prose. Scientific execution requires an exact named parent GO; none has been requested or used at this freeze. No finite failed search can imply noncompletion.

Redirect if a primary matched source already decides the target, or if all currently justified routes are proved saturated: report the exact result and propose a distinct replacement outside all eighteen roster entries for parent collision checking. No silent narrowing or reviewer-only slot.
