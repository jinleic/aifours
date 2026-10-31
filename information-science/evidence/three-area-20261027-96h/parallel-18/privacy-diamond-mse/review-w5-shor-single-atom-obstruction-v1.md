# w5 Shor single-atom obstruction — complete frozen-scope written review

Reviewer **InfoResearch96h-2**, info-1. Author **MathShor-2**, math-5. Actual native prewrite clock: **Tue Oct 27 14:56:11 PDT 2026**; first duty observation **14:55:10 PDT**.

**Verdict:** the three substantive scoped claims are SUPPORTED in writing, with **0 FATAL / 0 MAJOR / 1 MINOR** precision finding below. The minor concerns an unnecessary-padding necessity phrase, not the obstruction, converse or completion quantifiers. The original existence/nonexistence alternative remains OPEN.

## 1. Complete supplied reads, pins and exposure

Read the frozen manifest completely before the part: `manifest-v1.json`, SHA256 `bd3c6f1ead052e2a7200803d2f4421bc2e598d8c79faf70d39af791a39d706eb`, 28LF/2466B, raw1–28.

The SINGLE part was pin-matched and read raw **LF1–185 completely through S2|111 END**: `packet-part-1-v1.md`, SHA256 `6c336405b8194d9585efbe6a44d5057e5513f12a1b875cc3ca7656c7554749d7`, 185LF/20687B. It includes ALL of:

- **S1 CONTEXT:** 66LF packet, SHA256 `127337371c3af60de7473dce93574fbbb453df296cd5c25ccd5def1fa0dfdde9`, including controls and the literal book excerpt/definition packet through ending.
- **S2 AUTHOR:** entire111LF `prerequisite-derivation-v1.md`, SHA256 `a5c76def11edc0393d82a2a185adcf37a4d43c872ea1ac7bb51d87ee596aea3b`.

Line references below use the OUTER S1/S2 labels supplied in the part. No linked source, book page, old code-theory paper, old proof/review/park/checkpoint, extra dossier or author contact was opened. The packet's historical transcription/page-check claim is its provenance boundary, not a fresh source-image or bibliographic authentication by this reviewer. The author's ACK/process assertions were not independently audited by opening their linked files.

**Prior contact:** this is not a fresh blind or configured-family review. The inherited round context records MathShor-2's prior review contact with my privacy work and previously qualified reciprocal contact; I do not claim that contact is absent. A complete old incoming/outgoing contact census was not performed, and no old review/body was recovered to make one. Old held/control/provenance sources and their consumers remain NONINPUT. All proofs below use only the frozen literal words, definitions and elementary free-monoid/integer reasoning; no old arithmetic restriction, FACT theorem or prior verdict is imported. My own privacy line remains deferred under Main's current direction.

No scientific execution, calculator/CAS/interpreter/Eval, enumeration, selected order/state probe, replay, model CLI, nested agent or outside mathematical source was used. Only this requested review output is written. This is same-harness supplied-proof written review, not stronger assurance, novelty or a clean-cognition/process certificate.

## 2. Definitions checked against the supplied book excerpt

S1's excerpt states completeness as `for every w in X*, X*wX* intersects C* nontrivially`. This is exactly the candidate's statement that some `u w v` belongs to `D*`, with `u,v` allowed empty. It is FACTOR-completeness, not the generally stronger demand that w itself be a concatenation of codewords.

The finite completion target is a finite complete CODE containing the supplied Shor code. The candidate explicitly uses ordinary raw unique decipherability: equality of concatenations forces equality of ordered codeword lists, including list length. This is the code property needed by the source question, not a prefix/suffix restriction. Finite maximality equivalence is mentioned in the book but not used to replace or prove factor-completeness here; no external theorem about maximal/factorizing codes is required for the new implication.

The three displayed unions defining the original object agree literally with S1's book excerpt. Treating `1` in those products as the empty word yields the stated ordered exponent-pair set T and DOES NOT put the empty word into the code. Every old word has exactly one b. No assertion about the old code's UD proof, an arithmetic order restriction or a completion is needed to establish the conditional necessary result for an arbitrary UD D containing these literal words.

The candidate correctly excludes an empty codeword: its one-term list and the empty list concatenate to the same word. Even if one formulated UD only for nonempty lists, the one-term and two-term empty-word lists would yield the same contradiction. Thus every actual D-codeword used later is nonempty.

## 3. Claim (a): compulsory actual pure-a word, including uniqueness

**Scope:** S2 LF40–50. **Decision: SUPPORTED.**

Let D be ANY finite UD factor-complete extension. It is nonempty because it contains the prescribed old words. Let L be its finite maximum word length, positive because codewords are nonempty.

Suppose there is no pure-a word. Then every D-word contains b. A contiguous factor consisting solely of a's cannot intersect three consecutive codewords nontrivially: it would contain the intervening complete nonempty codeword and hence a b. Consequently such a factor lies within one codeword or crosses one boundary, and has length at most `2L`. The empty concatenation contributes no positive-length factor. Factor-completeness applied to `a^(2L+1)` contradicts this bound. L is a universally quantified function of the hypothetical D, not an order selected for a numerical probe.

There is therefore some `a^n in D`, with n positive. If distinct pure-a words `a^m,a^n` occurred, the ordered two-word lists `(a^m,a^n)` and `(a^n,a^m)` would differ but have the same concatenation. UD excludes this, proving uniqueness. This proof does not assume a length bound on hypothetical completions shared across all D.

The further pure-b observation is also correct: b is in the prescribed code, so an additional `b^k` of length greater than one would have the one-atom parse and the list of k copies of b. Every added atom other than the unique pure-a word must therefore contain b, as used in the main theorem. There is no omitted epsilon-codeword case.

## 4. Claim (b): every index and padding sign in the explicit word equality

**Scope:** S2 LF52–85. **Decision: SUPPORTED.**

Fix arbitrary `n>=1`, `m>=1`, and

`c=a^r0 b a^r1 ... b a^rm`, all `r_t>=0`.

Choose ONE simultaneous ordered sequence of m actual old pairs `(i_t,j_t) in T`. The source spelling of a concatenation of their old words, separated by repetitions of the same actual `a^n`, has run lengths

- initial: `n q_0+i_1`;
- interior `t=1,...,m-1`: `j_t+n q_t+i_(t+1)`;
- final: `j_m+n q_m`.

The left word with l,h pure-a pads has runs `nl+r0`, then the unchanged interiors `r_t`, then `rm+nh`. Thus the candidate's conditions retain exactly the adjacent pair coupling and every interior nonnegativity requirement; it does not replace them with independent residue choices.

### Forward construction

Endpoint congruence gives integers `d0=(r0-i_1)/n` and `dm=(rm-j_m)/n`, not necessarily nonnegative. The equation at the first endpoint is `q_0-l=d0`. The author's construction chooses `(l,q_0)=(0,d0)` when `d0>=0`, and `(-d0,0)` otherwise. Both entries are nonnegative and solve the required equation. The final construction `q_m-h=dm` is identical and independent. There is no negative power of a word in either parse.

For each interior gap the supplied `q_t>=0` solves its EXACT length equation. No padding is inserted within the new atom c on the left. Unique run decomposition therefore proves the displayed free-monoid equality letter by letter:

`(a^n)^l c (a^n)^h = (a^n)^(q_0) s_1 (a^n)^(q_1) ... s_m (a^n)^(q_m)`.

Zero powers denote omitted codewords. All zero/nonzero endpoint and interior lengths are included. When `m=1` there is one old word on the right and no interior condition; the notation `q_0,q_m` then means the two distinct endpoint indices, with no accidental shared interior variable. When `n=1` the congruences still make sense; no primality, square-freeness, largeness or inherited divisibility premise was inserted.

### Actual UD contradiction for a genuinely new atom

Now take the n forced by the SAME actual completion D, not a separately chosen order. If `c in D` but outside the old code and `{a^n}`, the left side is a D-parse containing c exactly once, while the right side uses only old atoms and `a^n`. Both lists are legal; they are DIFFERENT because the literal D-element c is absent from the second list. Equality of lengths of lists is irrelevant: the ordered lists cannot be identical even if their counts happen to agree. Therefore UD fails.

Any further supercode retains both lists and the same ambiguous word, so completeness or more atoms cannot cure it. Finiteness/factor-completeness were needed only to force `a^n`; conditional on its presence, this obstruction applies to arbitrary UD supercodes, even infinite ones. The candidate says precisely that, rather than assuming finiteness throughout the word-equality argument.

## 5. Claim (c): exact converse scope and the one-b corollary

**Scope:** S2 LF67–77 and87–99. **Decision: SUPPORTED, subject only to the wording MINOR in §6.**

Conversely, ANY equality of the displayed restricted form has m old right-side atoms because every one contributes exactly one b and pure-a pads contribute none. Comparing initial/final runs gives the two endpoint congruences. Comparing each unchanged interior run gives

`r_t-j_t-i_(t+1)=n q_t`, with `q_t>=0`.

Thus SH detects exactly these equalities using a single new c between endpoint pads and a right parse of old one-b atoms plus pure-a words. It does NOT detect every possible D-ambiguity. The candidate explicitly leaves open competing parses involving multiple new atoms or other boundary arrangements. Likewise SH-avoidance supplies no factor-completeness or general UD proof, so it is not a completion criterion.

The one-b corollary can also be reconstructed without importing a code theorem. For ANY two distinct one-b D-words `x=a^i b a^j` and `y=a^k b a^ell`, equal ordered endpoint residues modulo n allow nonnegative pads on both sides solving

`n p+i=n q+k`, `j+n r=ell+n s`.

The same sign-balancing argument constructs an equality of two parses with x on one side and y on the other. Since the b-containing codewords differ and all other atoms are `a^n`, the parses differ. This validates the corollary for arbitrary one-b atoms, not just pairs in the old T. The simultaneous old-pair sequence remains essential for the multi-b criterion; this corollary does not free those interior choices.

## 6. One precision finding

### MINOR — S2 LF99: zero endpoint differences do not REQUIRE zero padding

The phrase **“Zero endpoint differences require zero padding”** overstates necessity. If `d0=0`, the endpoint equation is `q_0=l`, and ANY common nonnegative value satisfies it; similarly `dm=0` permits `q_m=h`. The proof's chosen minimal sign-balancing solution sets both entries to zero, but that is a valid CHOICE, not a requirement on every equality. This is an all-variable algebraic observation, not a selected finite example or arithmetic test.

**Effect:** no impact on Lemma2's existential equivalence or Theorem3's UD obstruction. The actual construction at LF74 is correct, and the converse allows arbitrary nonnegative pads as it should.

**Exact prospective wording correction:** “For zero endpoint differences, the construction may choose zero padding on both sides.” No original frozen byte was edited by this reviewer.

## 7. Imports, unchanged target and final scoped decision

Only ordinary free-monoid equality/run decomposition, elementary integer divisibility/nonnegativity and a finite maximum are required for the substantive claims. The supplied book excerpt governs the finite complete-code target; its provenance is not freshly authenticated here. No Schützenberger/factorization theorem, old FACT/STAB or 660/1320 arithmetic statement, prefix-code WLOG or residue-only sufficiency claim is consumed.

The result is a universal NECESSARY condition tied to an actual compulsory pure-a atom and an explicit ambiguous word. It is stronger than mere encoding in that it excludes each matching new atom from every hypothetical completion with that n. It is NOT universal nonexistence: a proof forcing at least one such atom in every hypothetical finite complete extension is not supplied. The missing positive direction is an actual finite added set with full UD and factor-completeness proofs; the missing negative direction remains a universal UD violation for every hypothetical extension. S2 LF103–107 states these limitations correctly. The proposed next research step is not an established theorem or permission to use held inputs.

**Final counts: 0 FATAL / 0 MAJOR / 1 MINOR.** Claims (a), (b), and the restricted converse in (c) are SUPPORTED in writing; LF99 needs the indicated non-load-bearing precision correction. No original Shor completion/noncompletion, decision procedure for the broader book question, novelty/SOTA, process cure or stronger-family/human/formal/kernel/executable acceptance follows. All prior STOP/HOLD/ZERO/findings, N4 UNKNOWN and auxiliary214 STOP remain.

**END COMPLETE w5 REVIEW — the sole part and both supplied source endings read; no author contact or other mathematical source.**
