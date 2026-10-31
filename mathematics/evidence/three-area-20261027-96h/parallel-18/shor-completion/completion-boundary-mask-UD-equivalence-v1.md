# Exact boundary-mask criterion for all ambiguities, with a finite-completeness padding bridge

Owner **MathShor-2 / math-5**. Actual `/bin/date` before writing: **Tue Oct 27 14:56:01 PDT 2026**.
Prospective authority: current definition-first S1 only. Inputs: its supplied literal code and raw definitions, ordinary equality of words/nonnegative integer arithmetic, and the proof of the unique pure-a atom in `prerequisite-derivation-v1.md` (a5c76def11edc0393d82a2a185adcf37a4d43c872ea1ac7bb51d87ee596aea3b), an unreviewed candidate whose needed elementary argument is restated below. No old source/proof/held guide or code-theory theorem is used.
**Exact WRITTEN author candidate.** No execution, formal/kernel/human/configured-family/novelty acceptance. Prior exposure and all ZERO/HOLD/STOP findings persist; printed input separation is not a clean-cognition claim.

## 1. Scope and why the boundary masks matter

The first candidate paid a single-new-codeword versus old-one-b-word ambiguity mechanism. The present statement pays **all** competing codeword lists, not just that mechanism, for a word set with one pure-a atom. Both proposed parses retain the same actual b-positions and actual codeword interiors. An internal run with no codeword boundary in a parse cannot receive extra `a^n` there.
The result gives an explicit local congruence/inequality test, for each pair of actual b-containing codeword lists, that is equivalent to existence of a shared raw word after legal insertions. Thus any compatible pair rules out **every** supercode containing those actual codewords and `a^n`. It is not a test of selected numerical data or a cyclic-factorization-to-completion converse.

## 2. General raw setting and normalized parses

Let n>=1. Let E be any set of finite words over {a,b}, each containing at least one b. Put

    D={a^n} union E.

No UD assumption is made. No word of E is empty or equal to `a^n`. E need not yet be finite for the ambiguity theorem.
Any D-codeword list containing b has a unique normalized description: its ordered E-word list

    U=(u_1,...,u_k), k>=1,

and the nonnegative counts of consecutive `a^n` codewords before, between and after these E-words. This merely groups repetitions of the unique pure-a codeword; it changes no actual codeword order or count. A list without b consists entirely of copies of `a^n` and is already uniquely determined by its raw length.

For an E-list U, let m_j be the number of b's in u_j and M=sum m_j. The raw concatenation `u_1...u_k` has a unique run vector

    A_U=(A_U,0,...,A_U,M),
    u_1...u_k=a^(A_U,0) b a^(A_U,1) ... b a^(A_U,M).

Define its legal insertion mask

    B_U={0,M} union {m_1, m_1+m_2, ..., m_1+...+m_(k-1)}.

These are the gaps between E-codewords, plus the two ends. All interior mask indices are distinct because every m_j>=1. At a gap i in B_U, inserted pure-a codewords may add n times a nonnegative integer. At a gap outside B_U the run lies inside one indivisible E-codeword and cannot be increased by such a codeword insertion.

**Run realization lemma.** A raw word with M b's and run vector G is represented by U with legal insertions if and only if

    G_i=A_U,i                 for i outside B_U,
    G_i=A_U,i+n q_i, q_i>=0    for i in B_U.                (R)

Proof: concatenate the actual words and the pure-a insertions. Conversely each q_i in a masked gap specifies exactly the indicated number of `a^n` codewords at that boundary. Equality of the resulting run vector proves raw equality, with no insertion inside an E-word.

## 3. Complete compatibility test for TWO actual parses

Take two E-lists U,V with the SAME total b-count M>=1. Write A_i=A_U,i, C_i=A_V,i, and B=B_U, F=B_V. They are **compatible** if every gap i=0,...,M meets its appropriate condition:

| Boundary status at i | Exact required condition |
|---|---|
| i outside B union F | A_i=C_i |
| i in B intersect F | A_i congruent C_i modulo n |
| i in B but not F | C_i-A_i is a nonnegative multiple of n |
| i in F but not B | A_i-C_i is a nonnegative multiple of n |

The ends always lie in both masks, so their condition is the two-sided congruence, not a one-sided bound. All actual interior zero runs are retained. No independent interior residue choice replaces a fixed run equality.

**Theorem 1 (exact shared-word iff).** U and V are compatible if and only if there is a raw word with legal pure-a insertions into BOTH U and V.

**Necessity.** Let G be the shared run vector from (R). If neither parse has a boundary, both runs are fixed and equal. If both have boundaries, their fixed bases differ by a multiple of n. If only U has a boundary, V's run C_i is fixed and must be A_i plus a nonnegative n-multiple. The other one-sided case is symmetric.

**Sufficiency with explicit common word.** Construct each G_i as follows, using the SAME U,V and n throughout:
- outside both masks, take the common A_i=C_i;
- inside both masks, take `max(A_i,C_i)`, which is in both n-congruence classes and is at least both bases;
- in B only, take C_i;
- in F only, take A_i.

Every constructed entry is nonnegative. The assumed conditions make its difference from each masked base a nonnegative multiple of n, and it equals every unmasked base. Hence (R) supplies two actual parses of the word with run vector G. This is a universal integer construction, not an evaluated codeword/control or parameter probe.

## 4. An exact ALL-list unique-decipherability criterion

**Theorem 2.** `D={a^n} union E` is UD if and only if **no two distinct ordered E-lists U,V of the same total b-count are compatible**.

**Forward direction.** By Theorem 1, a compatible pair gives two D-codeword parses of the same word. If U and V are distinct as lists of actual E-words, the full D-word lists are distinct even after their pure-a insertions, so UD fails.

**Reverse direction.** Suppose D is not UD. Choose two different finite D-codeword lists with the same raw word. They have the same number of b's. If it is zero, both lists contain only `a^n`, and raw length forces the same number of copies, so they cannot be different. Thus M>=1.
Extract their normalized E-lists U,V. If U=V, the masks and fixed run vectors coincide; in each masked gap the common raw run gives exactly `(G_i-A_i)/n` pure-a copies. Both normalized lists and every insertion count are therefore equal, hence the original full lists are equal, again a contradiction. Thus U and V are distinct. The common word makes them compatible by Theorem 1.

This proves the full converse, not merely the restricted converse in the first candidate. It still quantifies over ALL finite actual E-lists, not a chosen maximum b-count, finitely sampled pair, commutative shadow or root-of-unity condition. Unequal list lengths are allowed; only total b-count must agree, a necessary raw-word condition.

### Concrete actual-object caller

For any hypothetical completion, E is its actual set of b-containing codewords and n is its actual pure-a exponent. Producing just one compatible distinct pair proves non-UD, and the explicit G construction gives the exact common raw word and both original-order codeword parses. No completeness theorem can repair that pair. Conversely absence of ALL such pairs proves UD for D, by Theorem 2, but says nothing by itself about factor-completeness.

## 5. Finite factor-completeness has a uniform actual padding bound

Now let D be finite and nonempty, with maximum word length L>=1 and with no empty word. Then

    D is factor-complete
      iff for every raw word w there are raw words x,y with
          |x|<L, |y|<L, and xwy in D*.                    (P)

**Proof.** The reverse implication is precisely the factor definition. For the forward implication, take an occurrence of nonempty w inside a concatenation of D-words. Retain only the first codeword containing its first letter, the last codeword containing its last letter, and those between. The retained product is xwy; x is a proper prefix of the first word and y a proper suffix of the last. Their lengths are strictly below L, even if the two endpoints lie in the same codeword. For empty w take x=y empty, using the empty concatenation in D*.

The bound is uniform for the SAME finite D. It is not a supplied a priori bound on L, a finite code search, a compactness theorem or an algorithmic completion decision.

For completeness of the original actual-object application: any finite UD complete extension containing the supplied S has exactly one pure-a word. Existence follows because, if every D-word contained b, any all-a factor could span at most two codewords and have length at most 2L, contradicting the required factor `a^(2L+1)`. Uniqueness follows from the two commuting lists of distinct pure-a words. Empty words are excluded by UD itself. Thus the hypotheses of Theorem 2 and (P) apply to **every** original finite completion, not a chosen subfamily.

## 6. What is paid and the exact unproved all-order coupling

For any actual finite proposed `D={a^n} union E` containing the whole original S:
- **UD is equivalent** to absence of compatible distinct E-lists (Theorem 2).
- **Factor-completeness is equivalent** to the SAME D's bounded-padding statement (P).
- A compatible pair is an explicit universal obstruction to any UD extension containing its words and `a^n`.

These are exact actual-object forward/converse callers and a constructive ambiguity lemma. They do not assert that arbitrary masks/run vectors are independently realizable as actual codeword lists. In every invocation U,V must be formed from the SAME actual E; no formal matrix solution is promoted to a completion or an avoiding code.

**NR-UNIFORM-MASK-COUPLING:** no proof yet shows that all finite E containing the required original S and satisfying (P) must contain a compatible distinct pair; no actual finite E is supplied satisfying both (P) and the full no-pair condition. This is the original constructive-versus-universal-obstruction gap in these coordinates. The coordinate equivalence itself is not an original solution.

**Exact forbidden shortcut:** reducing all gaps merely modulo n drops the equality at unmasked/unmasked gaps and drops the oriented nonnegativity at one-sided masked gaps. Such data do not pay the raw lifting conditions in Theorem 1. No FACT or cyclic-group statement is used as that missing implication, and no sampled counterexample or old withdrawn control is proposed.

No further source theorem, classical factorization input or held guide is needed for the proofs above. No new source/proof permission outside current S1, stronger verification, novelty or all-order result is conferred. All old findings and input quarantines remain. Continued original progress needs a genuine source-clean lemma at NR-UNIFORM-MASK-COUPLING, not more renaming of this encoding or a selected small-code test.

**END OF ALL-LIST COUPLING CANDIDATE.**
