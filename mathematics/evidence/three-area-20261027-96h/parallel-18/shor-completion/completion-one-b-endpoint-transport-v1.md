# Actual one-b endpoint transport: integer path conservation and a raw multi-b exclusion

Owner **MathShor-2 / math-5**. Actual `/bin/date` before writing: **Tue Oct 27 15:07:45 PDT 2026**.
This resumes only the admitted definition-first S1 line **after ACTUAL return of w8** (return preceded by the actual 15:04:57 clock). The Tuscan packet/review is NOT a Shor input. Current inputs are the supplied literal code/UD/factor-completeness definitions and elementary word equality, finite integer matrix counting and geometric growth. No old FACT/source/held guide is used or reopened. Extensive old exposure and all process/input limitations remain; no clean-cognition or independent-priority claim.
**WRITTEN, unreviewed candidate.** This conditional necessary theorem is about the SAME actual hypothetical completion and its actual one-b codewords. It neither constructs a code from cyclic data nor decides the original problem.

## 1. Actual completion and the compulsory pure-a word

Let D be ANY finite UD factor-complete extension of the full supplied Shor code S over {a,b}. Let L be its maximum word length. UD excludes the empty word. If D had no all-a word, an all-a factor of D* could cross at most one codeword boundary, so would have length at most 2L, contradicting completeness of `a^(2L+1)`. Two distinct all-a codewords commute and give distinct parses. Hence D has exactly one all-a codeword `a^n`, n>=1.
Define its actual one-b part

    B={a^i b a^j in D : i,j>=0}.

B is finite and nonempty (b belongs to the mandatory S). It contains every one-b word of S, with literal, not residue-only, exponents. Let k=|B|.
No b-containing D-word outside B is being erased from D; the statements below extract a necessary layer from that same D, and later put the multi-b words back into the UD caller.

## 2. UD makes every endpoint path count zero or one

Take a list of m>=1 actual B-words

    (a^i1 b a^j1, ..., a^im b a^jm).

Its residue data are

    (i1 mod n;
     j1+i2 mod n, ..., j_(m-1)+im mod n;
     jm mod n).                                          (DATA)

**Lemma 1.** No two distinct B-word lists of the same length m have the same (DATA).

**Proof.** Between consecutive B-words there is a genuine codeword boundary in EACH parse. If the two bases of a corresponding interior a-run have the same residue modulo n, enlarge both by nonnegative multiples of n to their common larger value. Do the same at the two ends. This is legal insertion of copies of the actual codeword `a^n` at codeword boundaries only. The two distinct actual B-lists now give distinct D-parses of the same raw word, contradicting UD. This is the all-boundary special case of the direct run-equality construction, not an imported cyclic factorization theorem.

In particular different B-words have different endpoint residue pairs. Form the n-by-n **integer** zero-one matrix

    W_ij=1 iff B contains an actual word a^u b a^v
                  with u==i mod n and v==j mod n.

There is at most one such actual B-word for any pair. Matrix entries and path counts are ordinary nonnegative INTEGERS, not arithmetic modulo n.
For gamma in Z_n, define the permutation matrix

    (J_gamma)_(j,i)=1 iff j+i=gamma in Z_n.

For any internal residue word gamma_1,...,gamma_(m-1), the product

    A_gamma=W J_gamma1 W ... J_gamma_(m-1) W               (PATH)

counts the actual B-lists with those internal residues and each endpoint pair. Lemma 1 makes EVERY entry at most one. Thus all products (PATH) are zero-one integer matrices.

## 3. A finite maximum forces every such product to have at most n entries

Let P be the set of all nonempty products (PATH), of all lengths. It is a finite set of zero-one n-by-n matrices, whether or not some different paths give the same matrix. It contains W. If A,C belong to P, so does `A J_gamma C` for every gamma: concatenate their actual B-lists with that seam residue.
Write |A| for the integer sum of A's entries. Choose a member of maximum size K. K>0 because B is nonempty. All n products `A J_gamma A` have size at most K. Since

    sum_gamma J_gamma = the all-one matrix,

ordinary matrix counting gives

    sum_gamma |A J_gamma A|=|A|^2=K^2.

Therefore `K^2<=nK`, and K<=n. Consequently

    |A_gamma|<=n for EVERY internal residue word,
    k=|W|<=n.                                            (UB)

The finiteness/maximal-member argument is an existence proof, not an enumeration or a search through matrices. It works for all n>=1 and zero entries/reducible path structures; no prime or square-free hypothesis is needed.

## 4. Completeness forces all long-gap internal residue patterns to occur

**Lemma 2.** For every m>=1 and every internal residue word gamma_1,...,gamma_(m-1), some actual B-list realizes those internal residues.

**Proof.** Choose integer gap lengths g_t congruent gamma_t modulo n and all greater than 2L; this is possible for arbitrary positive n. Consider the raw word

    a^L b a^g1 b ... b a^g_(m-1) b a^L.

For m=1 it has no internal gaps. Factor-completeness puts this word inside a concatenation of actual D-codewords. A D-codeword containing one of its displayed b's cannot contain another b:
- another displayed b is farther away than L;
- a b outside the displayed factor is separated from its first/last displayed b by an a-guard of length L.
Both alternatives exceed the word length L. The D-codeword containing each displayed b is therefore an actual ONE-b word in B. The guards also ensure that its whole word lies inside the displayed factor.
Between consecutive such one-b codewords, only all-a D-codewords can occur, and the unique one is `a^n`. Hence

    g_t=j_t+i_(t+1)+n q_t, q_t>=0.

Their residues are exactly gamma_t. Every chosen gap here is part of a universally quantified proof lift for arbitrary D and arbitrary label word, not a selected numerical instance or magnitude probe.

Since B^m maps onto all n^(m-1) internal residue words,

    k^m>=n^(m-1) for EVERY m>=1.                          (LB)

If k<n, the positive geometric powers `(n/k)^(m-1)` would be bounded above by k for all m, impossible. Together with (UB), this proves

    |B|=n.                                               (COUNT)

This conclusion alone is a necessary-layer fact, not original completion progress or a stronger inherited divisibility claim.

## 5. Exact all-order integer conservation at each internal residue word

**Theorem 3.** For every m>=1 and every internal residue word, (PATH) has exactly n entries equal to one. Equivalently there are exactly n actual B-lists with those internal residues, with at most one list for each endpoint residue pair.

**Proof.** The m=1 matrix W has n entries by (COUNT). Suppose a prefix product A has n entries. Each possible next product `A J_gamma W` has at most n entries by (UB). But

    sum_gamma |A J_gamma W|=|A||W|=n^2.

There are n summands, each at most n, so each equals n. Induction pays EVERY residue word and every length, not just an aggregate average or a finite prefix. The endpoint uniqueness comes from Lemma 1.

Neither W nor these products can be independently supplied as a completion: they must come from the actual B inside the same hypothetical D. No FACT statement from an old body is an input, and no identification of this formulation with an old unreconstructed gate is asserted.

## 6. A raw multi-b codeword must escape these actual endpoint paths

Let

    H_B=max{j+i' : a^i b a^j and a^i' b a^j' belong to B}.

This is a finite nonnegative threshold of the SAME actual one-b words, not a chosen rate/control or a claimed universal size bound. Let c be any actual D-codeword with m>=2 copies of b and run vector `(r0,...,rm)`. Set gamma_t=r_t modulo n for its internal runs, and use the actual matrix A_gamma in (PATH).

**Theorem 4 (uniform raw lifting obstruction).** It is impossible that BOTH

    r_t>=H_B for every 1<=t<m,
    (A_gamma)_(r0 mod n, rm mod n)=1.                      (FORBID)

**Proof.** The matrix entry supplies the SAME sequence of actual B-words with endpoint residues matching c and with every internal base `j_t+i_(t+1)` congruent r_t. The threshold gives `j_t+i_(t+1)<=H_B<=r_t`; hence every difference is a nonnegative n-multiple. Prefix/suffix congruences can be balanced by nonnegative pure-a pads. Thus

    a^(n l) c a^(n h)
      =a^(n q0) b_1 a^(n q1) ... b_m a^(n qm)

for actual b_t in B. The left parse uses the single codeword c with m>=2 b's, while the right uses only ONE-b codewords and `a^n`. They are distinct D-parses of one raw word, contradicting UD.

Consequently, each multi-b atom of ANY original finite completion must either have an internal run below this actual threshold, or occupy an endpoint pair absent from its own internal-label path matrix. The same n and same B govern ALL its atoms. The n occupied endpoint pairs in Theorem 3 cannot be assigned independently to different candidate words or gap positions.

This is an actual new coupling obligation, beyond merely giving an integer path encoding: it constructs an exact ambiguity for every violation (FORBID) and rules out that atom in every extension containing those words. It does not say the complementary endpoint pairs are realizable codewords or supply a converse existence criterion.

## 7. Exact remaining bridge and claim limits

The uniform coupling question is now explicit: can a finite complete D containing the mandatory S place **all** its multi-b words in the short-run or absent-endpoint escapes of Theorem 4 while retaining the full all-list no-compatible-pair condition? No contradiction or actual witness has been proved. The count/path laws do not force a violating atom by themselves.

**NR-ESCAPE-VERSUS-COVERAGE:** a proof that raw factor-completeness forces some actual multi-b atom to satisfy both parts of (FORBID), or a construction of a finite full UD complete code escaping all ambiguities, is still missing. Even an abstract family of zero-one products satisfying the conservation law would not answer it. No purely modular condition is upgraded to a raw-code completion.

All statements here are necessary at the full original finite-extension quantifiers. They may reproduce general code-theory facts; no novelty or difference-from-every-old-result is claimed, and no old source body was accessed to establish such a comparison. The material caller is the raw threshold-plus-endpoint ambiguity, not the scalar count on its own. No numerical source test, scientific interpreter, finite enumeration, solver, build, external model or nested agent occurred. All original STOP/HOLD/ZERO/history limits outside S1, N4 UNKNOWN/historical exit unestablished and aux214 STOP persist.

**END OF RESUMED UNIVERSAL COUPLING CANDIDATE.**
