# Definition-first necessary coupling: a synchronized old-word shadow obstructs every completion

Owner **MathShor-2**, same math-5. Actual `/bin/date` before writing: **Tue Oct 27 14:50:38 PDT 2026**.
Authority: the prospective S1 release, read completely before the supplied definitions. Required pre-body exposure ACK: `release-v1-pre-body-exposure-ack-v1.json`, SHA256 **705679da88b6111366168495c11f24f74143b05c541f943bb88ceb9805b2834c**. All 66 LF of the pinned packet were then read through the ending.
**WRITTEN author candidate, not adopted/formal/kernel/executed/novelty-cleared.** This is a necessary obstruction for actual finite codewords with an explicit word-equality certificate, not a cyclic factorization asserted to be a completion.

## 1. Inputs, provenance and full original target

Only the current S1 controls, S2 literal problem definitions, S0/current contract/own safe intake, and elementary facts stated below are inputs. No old proof/review/park/checkpoint/map/dossier/Bayonet paper or held133/108/119 body was opened. No old FACT/STAB/source lemma is used in this proof. Prior authorship and control/provenance exposures remain disclosed; this proof-input statement is not a clean-cognition or independent-reconstruction guarantee.

S2 supplies the book-transcription literal

    S=b{1,a,a^7,a^13,a^14}
      union {a^3,a^8}b{1,a^2,a^4,a^6}
      union a^11b{1,a,a^2}.

Here 1 is the empty word in these products, not an additional codeword. Equivalently, write

    S={a^i b a^j : (i,j) in T},
    T=({0} x {0,1,7,13,14})
      union ({3,8} x {0,2,4,6})
      union ({11} x {0,1,2}).

These entries are exactly the supplied original object, not a chosen/tested control. The source claims 16 words; no independent page-pixel or publication authentication is made here. The book's printed year/editorial correction is preserved by the packet and is not a theorem premise.

Let X={a,b}. A candidate completion is a **finite set D of words over X containing S**, uniquely decipherable in the following raw sense: equality of two concatenations of D-words forces equality of their ordered lists of codewords (including list length). Factor-completeness means exactly the supplied definition

    for every w in X*, there exist u,v in X* with uwv in D*.

The target is existence of such D or universal nonexistence for every finite D, not one order/family. Empty words cannot be in a uniquely decipherable D: the empty list and the one-term list containing the empty word would have equal concatenation. No completeness/maximality or factorization theorem is imported.

### Elementary background used

- Equality of words in the free monoid is equality letter by letter; a word containing m copies of b has a unique run decomposition `a^r0 b a^r1 ... b a^rm`, with all r_t nonnegative integers.
- Elementary nonnegative integer divisibility and the finite maximum of a finite set of word lengths.
- The raw unique-decipherability and factor-completeness definitions just stated.

There is no classical code-theory theorem import or unsupplied multiplier assertion in the derivation.

## 2. Every finite completion has exactly one actual pure-a codeword

**Lemma 1.** Every finite factor-complete uniquely decipherable D containing S contains exactly one word `a^n`, for an integer n>=1.

**Existence.** Suppose every word of D contains b. Let L be the largest D-word length; L is finite and positive because S is nonempty. A factor containing only a's in a concatenation of D-words can meet at most two consecutive codewords: meeting three would include a complete intervening codeword and hence b. Its length is therefore at most 2L. This also bounds factors contained in one codeword and the empty concatenation. But completeness requires `a^(2L+1)` to be a factor of some word of D*, a contradiction. This is a quantified witness determined by arbitrary D, not evaluation of a selected code/order.

**Uniqueness.** If two distinct pure-a codewords `a^m` and `a^n` were present, the two different lists `(a^m,a^n)` and `(a^n,a^m)` would have the same concatenation, contradicting UD. The empty-word exclusion gives n>=1.

Because b is already in S, no other pure-b word can be in D either: `b^k` for k>1 would have the one-word parse and its k-term b parse. Thus every added codeword other than the unique `a^n` contains b; the result below applies to all of them, without any bound on their b-count.

This lemma is a definition-level prerequisite, not a new size/divisibility result or a completion. The useful next step is the actual-word obstruction below, which preserves the interior run inequalities that mere residues would drop.

## 3. Exact synchronized-shadow criterion at all orders

Fix **any** n>=1 and any word containing m>=1 copies of b,

    c=a^r0 b a^r1 ... b a^rm,  r_t>=0.

Say c has an **old-word shadow at n** if there are m actual pairs `(i_t,j_t) in T`, t=1,...,m, satisfying

    r0 == i_1 mod n,
    rm == j_m mod n,
    r_t = j_t+i_(t+1)+n q_t for t=1,...,m-1,
    q_t nonnegative integers.                              (SH)

Equivalently every interior difference `r_t-j_t-i_(t+1)` must be both nonnegative and divisible by n. Interior residues alone are NOT (SH). There are no interior equations when m=1. Repetitions of old words/pairs are permitted; these are actual words, not independently assigned polynomial weights.

**Lemma 2 (exact word-equality equivalence).** (SH) holds if and only if there exist nonnegative integers `l,h,q_0,...,q_m` and old words `s_t=a^i_t b a^j_t in S` with

    a^(n l) c a^(n h)
      =a^(n q_0) s_1 a^(n q_1) s_2 ... s_m a^(n q_m).      (EQ)

The words s_t on the right are the same ones that witness (SH); there are exactly m because they each contain one b.

**Proof, (SH) to (EQ).** For each interior gap use the supplied q_t. Write `r0-i_1=n d0` with integer d0. If d0>=0, set l=0,q_0=d0; if d0<0, set l=-d0,q_0=0. Then `n l+r0=n q_0+i_1` in either case. Similarly, write `rm-j_m=n dm` and take h=0,q_m=dm if dm>=0, and h=-dm,q_m=0 otherwise. Both endpoints can thus be balanced by nonnegative powers of the **same actual** codeword `a^n`.
The interior runs of the right concatenation have lengths `j_t+nq_t+i_(t+1)=r_t`; the endpoint equalities match the other runs. Both sides have m b's in the same order, so equality follows letter by letter. This proves (EQ) without inserting a codeword inside c.

**Proof, (EQ) to (SH).** Compare the unique a-run decompositions of both words. Endpoint differences are multiples of n. The t-th interior run of the right side is exactly `j_t+nq_t+i_(t+1)` with q_t>=0, which gives every equality and nonnegativity in (SH). Thus no assumption about independent endpoints, scalar factorization or an invertible symbolic map is involved.

## 4. A necessary obstruction for EVERY finite completion

**Theorem 3.** Let D be any finite UD factor-complete extension of the full supplied S. Let `a^n` be its actual unique pure-a word from Lemma 1. Then **no codeword c in D outside `S union {a^n}` has an old-word shadow at that same n**.

**Proof.** Every such c contains b. If it satisfied (SH), Lemma 2 would give (EQ). Its left side has a D-codeword parse using c, preceded/followed by copies of the actual codeword `a^n`. Its right side has a D-codeword parse using only S and `a^n`. Since c is neither an S-word nor `a^n`, the two ordered lists cannot be equal. They nevertheless concatenate to the same actual word by (EQ), contradicting UD.

The argument works for every finite completion D, its induced n, every m>=1 and every choice of zero/nonzero run lengths. There is no restriction to one-b extensions, to a chosen n, or to particular new codeword lengths. Finiteness/completeness enter solely to force the actual `a^n`; once it is present the word-level UD obstruction applies even to an infinite UD supercode.

### Actual-object forward caller and exact converse limit

- **Forward caller:** given an actual proposed extension containing S and `a^n`, finding (SH) for just one genuinely new c proves the extension **not UD**, by the two explicit codeword lists in (EQ). Any further supercode containing these words remains non-UD. No factor-completeness check can repair that ambiguity.
- **Converse paid by Lemma 2:** an equality of the restricted form (EQ), with only old one-b words and `a^n` on its right and just the one new c between pure-a pads on its left, is detected exactly by (SH).
- **Converse NOT paid:** absence of (SH) for all new atoms does not establish UD of the entire extension; there could be competing parses involving several new atoms or other boundary arrangements. This proof supplies no equivalence with ALL ambiguities. Likewise it proves no factor-completeness from an arithmetic factorization or from avoidance of this forbidden language.

This is more than an encoding of the original question: a syntactically specified all-order run pattern now yields an explicit actual-word ambiguity and excludes that codeword from **every** completion. It preserves one simultaneous sequence of actual old pairs across adjacent runs and the one-sided nonnegativity of every interior padding. No independent per-gap choice or modular-only relaxation is promoted to the certificate.

## 5. Useful immediate corollary and boundary accounting

For m=1, Lemma 2 has only the two endpoint congruences. Therefore two distinct one-b codewords in any UD set containing `a^n` cannot have the same ordered pair of endpoint residues modulo n: pure-a padding would give two different parses. This applies also to the mandatory old S itself; it is not a sufficient UD or completeness criterion.

Zero endpoint differences require zero padding. Negative endpoint differences are balanced on the left as proved, never by a negative codeword power. Interior differences cannot be balanced that way because c is one indivisible codeword there: a negative interior difference fails (SH), even if divisible by n. The m=1 case has no unmentioned interior denominator or constraint. The proof does not require n prime, square-free, large, or divisible by any inherited arithmetic constant.

## 6. Exact remaining step, assurance and continuation

**Changed:** a completely source-local word-equality obstruction couples the compulsory pure-a generator of an arbitrary finite completion to every possible added b-containing atom and all its actual interior runs. The original code spelling is retained throughout. No old necessary restriction was used as a converse and no scientific arithmetic was executed.

**Unchanged:** neither a finite completion nor a universal obstruction has been supplied. The missing positive direction is an actual finite added set with **full** UD and factor-completeness proofs. The missing negative direction is a proof that every hypothetical finite factor-complete extension must violate UD, not merely the existence of this forbidden language. In particular a bridge forcing a (SH)-word among its new atoms has NOT been proved here; the extension may avoid this particular single-atom ambiguity mechanism. These are named gaps, not invented counterexamples to a converse.

Next genuinely admitted step: examine, from these same raw definitions only, what factor-completeness forces on long-gap b-patterns of a finite completion and whether it couples to the exact interior-padding obstruction. Any result will retain the same D and n, not independently chosen factorization/word data. No admissible full completion implication is preclaimed. If the next step would require a held source or an excluded guide, stop that branch and report its exact missing premise rather than reconstruct it.

All prior STOP/HOLD/ZERO/findings, N4 UNKNOWN/historical exit unestablished and aux214 STOP persist. The book transcription/source equivalence is used only at the supplied literal provenance, not newly authenticated. No code-theory import, machine/kernel/formal/human/configured-family/cross-vendor/novelty acceptance or original-solution claim follows. New-root-only immutable writing; no old evidence changed.

**END OF FIRST SUBSTANTIVE DEFINITION-FIRST CANDIDATE.**
