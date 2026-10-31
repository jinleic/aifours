# f414 — Whole-class \(4445\) written review

**Role:** WRITTEN  
**Result:** SUPPORTED at the exact quantified scope below.  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Acceptance status:** This is a written-review return, not parent adoption. The candidate remains UNREVIEWED until parent disposition.  
**Code/execution:** No scientific code was authored or executed. Finite verification is **NOTRUN in this review** and is not replaced by the written argument.

## 1. Bindings, access and delivery

The assigned frozen wave is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f414-ame48-t24-4445-whole-class-written-review/`

Bindings supplied by the parent:

- Manifest SHA256: `8fa3cf29aa02133d5f39d3f457dcc0c6a358c871c4868e4bdfa01c3311418df6`
- Freeze-receipt SHA256: `d8981290c6cf8c9721b1a36c2cd141ef1daa4bce464c7318d779f804612e06d6`
- Literal-packet SHA256: `dd248e9b73936ce3424eb07974ee5d6648d4f34cce7d8e696b34f2b0e5b6aaee`

These are **parent-supplied bindings**, not child-executed hash checks.

Before reading the mathematical packet, I read the complete manifest, freeze receipt, dispatch receipt, parent metadata supply and all eight listed status-only controls. I sent a direct administrative pre-body ACK to Main. The ACK misstated the metadata supply’s length as 92 lines; I subsequently corrected that count to its observed ending at logical line 93. This was a metadata-count correction, not a missing mathematical read.

I then read the entire 534-line literal packet, in order, using raw windows of at most 20 lines, through all three source endings, before deriving the review:

- **S1:** complete author candidate, logical lines 1–481; source has 480 LF characters.
- **S2:** complete earlier alphabet-shadow/external-partner disposition, lines 1–28.
- **S3:** complete earlier \(4444\) disposition, lines 1–23.

No excluded links, held mathematical payload, author checker, current sibling result or external mathematical source was opened. The status controls were not mathematical inputs. No selected examples, scientific interpreter, solver, CAS, enumeration, replay, build, test, lint or formatter was used.

The permitted `git diff` command for the three assigned source paths returned no output. Accordingly, this return audits the supplied frozen mathematical body; it does not invent a Git hunk or a patch finding.

No working-tree review file was written under this read-only assignment. This is the complete body for parent materialization. No child-native clock or independently calculated hash is claimed.

## 2. Exact caller and quantifiers

**Status: SUPPORTED.**

The theorem being reviewed is S1:16–32, not a broader AME or support-minimum claim.

Let \(\psi\in(\mathbb C^6)^{\otimes4}\) be normalized and let \(U=6\psi\). Assume:

1. All three balanced \(36\times36\) flattenings of this **same tensor** are unitary.
2. \(U\) has exactly 48 nonzero entries.
3. Exactly 24 entries have modulus one.
4. The residual nonzero entries have coordinate-alphabet sizes \(4,4,4,5\), in some party order.

The claimed conclusion is that these hypotheses are inconsistent, for **every** support and **every** assignment of nonzero complex amplitudes satisfying them.

Party permutation permits naming the four-symbol parties \(1,2,3\) and the five-symbol party \(4\). This is a symmetry of the stated hypotheses, not a support normal form.

Write \(P\) for the 24 unit-modulus tensor words and \(E\) for the remaining 24 nonzero tensor words. The proof excludes a necessary combinatorial interface of these actual objects. It neither asserts that a relaxed support object is a physical tensor nor uses a finite failure of construction as a universal proof.

## 3. Reconstructing the actual common-\(P\) interface

**Status: SUPPORTED.**  
**Anchors:** S1:63–111.

Every entry of a unitary matrix has modulus at most one. A modulus-one entry exhausts both its row norm and its column norm. Therefore the entries of \(P\) occupy 24 distinct rows and 24 distinct columns in each balanced flattening, and every other entry in those rows or columns vanishes.

Deleting those rows and columns leaves a \(12\times12\) unitary with exactly the 24 entries of \(E\). Each remaining row and column is nonempty. A singleton remaining row would have an entry of modulus one, contrary to the definition of \(E\); the same applies to a singleton column. Since there are 24 residual entries and 12 remaining rows and columns, every remaining row and every remaining column has exactly two nonzeros.

The three flattenings collectively supply all six physical coordinate-pair projections. Thus, for every \(ij\),

\[
R_{ij}=\pi_{ij}(E)
\]

has 12 elements, each with exactly two extensions in \(E\). Moreover, \(\pi_{ij}\) is injective on \(P\), and

\[
\pi_{ij}(P)=[6]^2\setminus R_{ij}.
\]

These complements come from the **same \(P\)** in every pair system. No independently chosen pair packing has been substituted.

For \(a\in A_i=\pi_i(E)\), put

\[
p_i(a)=|\{w\in P:w_i=a\}|.
\]

Counting the six pair values with first coordinate \(a\) gives

\[
r_i(a)=6-p_i(a).
\]

Consequently \(r_i(a)\) is independent of the partner party. Exact two-extension counting also gives

\[
|\{w\in E:w_i=a\}|=2r_i(a),
\qquad
\sum_{a\in A_i}r_i(a)=12.
\]

Finally, \(r_i(a)=1\) is impossible: there would be precisely two residual words containing \(a\), and at every other coordinate both would have to use the unique neighbor of \(a\). They would therefore be the same tensor word, contradicting distinctness of support entries.

Hence \(r_i(a)\ge2\). This argument uses neither no-distance-one nor no-OLS(6).

## 4. Maximal-word moments and forced degrees

**Status: SUPPORTED.**  
**Anchors:** S1:115–194.

For \(w\in P\), let \(k(w)\) count its coordinates belonging to the corresponding residual alphabets. Since the alphabet sizes sum to 17,

\[
\sum_{w\in P}k(w)
=\sum_i\sum_{a\in A_i}(6-r_i(a))
=6\cdot17-4\cdot12
=54.
\]

For each physical pair \(ij\), precisely \(|A_i||A_j|-12\) maximal words have both coordinates internal. Therefore

\[
\sum_{w\in P}\binom{k(w)}2
=3(16-12)+3(20-12)
=36.
\]

The function

\[
\binom{k}{2}-2k+3
\]

is nonnegative for \(k=0,1,2,3,4\), with respective values \(3,1,0,0,1\). Its sum over the 24 maximal words is zero. Thus no maximal word has 0, 1 or 4 internal coordinates. Solving the two remaining count equations gives

\[
n_2=18,\qquad n_3=6.
\]

For an internal symbol \(a\in A_i\), let \(\tau_i(a)\) count maximal words containing \(a\) with three internal coordinates. Counting the other internal coordinates in maximal words containing \(a\) gives

\[
p_i(a)+\tau_i(a)
=\sum_{j\ne i}(|A_j|-r_i(a)).
\]

Substituting \(p_i(a)=6-r_i(a)\) yields

\[
\tau_i(a)=17-|A_i|-6-2r_i(a).
\]

For a four-symbol party, nonnegativity gives \(r_i(a)\le3\); four such degrees sum to 12, so every degree is exactly three. Consequently

\[
r_i(a)=3,\quad p_i(a)=3,\quad \tau_i(a)=1.
\]

Every one of the twelve symbols at parties \(1,2,3\) occurs in exactly one maximal triple.

At party \(4\), the degrees are integers between two and three and sum to 12 across five symbols. Their multiset is therefore

\[
(3,3,2,2,2).
\]

The two degree-three symbols occur in no maximal triple; each of the three degree-two symbols occurs in exactly two. These six occurrences account for all six maximal triples. Thus every maximal triple contains party \(4\), using a degree-two symbol, and exactly two of parties \(1,2,3\).

No inherited alphabet classification or external-partner theorem enters this derivation.

## 5. Simultaneous \(T/F\) matchings

**Status: SUPPORTED.**  
**Anchors:** S1:198–259.

For \(i,j\in\{1,2,3\}\), define

\[
M_{ij}=(A_i\times A_j)\setminus R_{ij}.
\]

Each vertex has one missing internal neighbor, so \(M_{ij}\) is a perfect matching between the two four-symbol sets. Its four edges are actual pair projections of unique words in the common \(P\).

Every such maximal word either has internal positions \(ij4\), producing a \(T_{ij}\) edge, or has internal positions exactly \(ij\), producing an \(F_{ij}\) edge. These alternatives exhaust the possibilities already established for \(P\).

Let \(x_{ij}=|T_{ij}|\). Each four-symbol party contributes its four symbols exactly once to maximal triples, giving

\[
x_{12}+x_{13}
=x_{12}+x_{23}
=x_{13}+x_{23}
=4.
\]

Thus each \(T_{ij}\) has two edges, and each \(F_{ij}\) also has two edges.

On the **party-tagged disjoint union** \(A_1\sqcup A_2\sqcup A_3\), the union \(T\) is a perfect matching because each symbol occurs in exactly one maximal triple. Each vertex has two incident missing edges overall, one toward each other party. Precisely one belongs to \(T\), so the other belongs to \(F\); therefore \(F\) is also a perfect matching.

This establishes the required simultaneous structure without separate pair gauges or implicit equalities of symbols at different physical parties.

The additional cycle classification is also correct. Every vertex of the union has one neighbor in each of the other two parties, forcing the party colors to repeat cyclically along a component. Component lengths are divisible by three. Alternation between \(T\) and \(F\) makes them even. The union is simple and has twelve vertices, leaving only a 12-cycle or two 6-cycles. The final contradiction does not depend on choosing either case.

The stated maximal-word type counts also follow: each four-party symbol lies in one triple, one \(F\)-word and one remaining \(i4\)-word. This accounts for all 24 maximal words.

## 6. Four-word slice lemma, including distance-one words

**Status: SUPPORTED.**  
**Anchors:** S1:263–294.

Fix an arbitrary degree-two symbol \(\ell\) at party \(4\), and define

\[
N_i=\{a:(a,\ell)\in R_{i4}\},
\qquad S_i=A_i\setminus N_i.
\]

For every \(i\in\{1,2,3\}\), both \(N_i\) and \(S_i\) have size two. The slice \(E_\ell\) has four distinct words, with each of the two symbols at each remaining coordinate occurring twice.

Each coordinate therefore defines an unordered \(2+2\) partition of the four-word index set. There are three such partitions. Any two distinct partitions have all four intersections of size one, so their coordinate-pair projection is the entire corresponding product \(N_i\times N_j\).

If all three partitions were equal, each partition class would contain two identical coordinate triples. With party \(4\) fixed to \(\ell\), these would be duplicate tensor words, which is impossible.

Hence either all three partitions differ, or precisely two coincide. At most one coordinate-pair projection is non-full.

Importantly, the second alternative is retained. It contains the relevant distance-one possibility; it is not discarded by an unproved inherited restriction.

## 7. Matching balance and concentration of the two triples

**Status: SUPPORTED.**  
**Anchors:** S1:298–335.

For any perfect matching \(M_{ij}\) between the two \(2+2\) partitions,

\[
|M_{ij}\cap(N_i\times N_j)|
=
|M_{ij}\cap(S_i\times S_j)|.
\]

To see this directly, if the first count is \(x\), then \(2-x\) matching edges run from \(N_i\) to \(S_j\), and \(2-x\) run from \(S_i\) to \(N_j\). The remaining \(x\) edges join \(S_i\) to \(S_j\).

If the slice projection onto \(ij\) is full, every \(N_i\times N_j\) pair lies in \(R_{ij}\), so the first count is zero and hence the second is zero. The slice lemma consequently permits \(S\)-to-\(S\) missing edges in at most one party pair.

The two maximal triples containing \(\ell\) each supply a \(T\)-edge whose endpoints lie in the corresponding \(S\)-sets: their pairs with \(\ell\) belong to \(P\), not \(E\). These two edges must therefore lie in the same exceptional party pair \(ij\).

They are disjoint because \(T\) is a perfect matching. Since \(|S_i|=|S_j|=2\) and \(|T_{ij}|=2\), they constitute all of \(T_{ij}\) and exhaust \(S_i,S_j\).

For the remaining party \(k\), the two edges in \(T_{ik}\) must consequently exhaust \(N_i\), and the two edges in \(T_{jk}\) must exhaust \(N_j\). This is a forced consequence of the global matching, not a new independent choice.

## 8. Final contradiction

**Status: SUPPORTED.**  
**Anchors:** S1:339–355.

Take any \(a\in S_k\). Its unique \(T\)-edge ends at party \(i\) or party \(j\).

If it ends at party \(i\), its edge in \(M_{kj}\) belongs to \(F_{kj}\). The two \(T_{kj}\) edges exhaust \(N_j\), so the other two edges of the perfect matching \(M_{kj}\), namely \(F_{kj}\), end in \(S_j\). Thus an \(M_{kj}\) edge joins \(S_k\) to \(S_j\).

But \(kj\) is not the exceptional pair \(ij\), so such an edge is forbidden by the slice/matching argument.

If the \(T\)-edge of \(a\) instead ends at party \(j\), the same reasoning with \(i,j\) interchanged gives a forbidden \(S_k\)-to-\(S_i\) edge. Both possibilities are covered; the symmetry does not relabel individual pair matchings independently.

Every degree-two symbol would therefore give a contradiction, and three such symbols were forced. This excludes the entire stated \(4445\) interface and hence the entire actual tensor class.

## 9. Coverage and dependency audit

### Triple-color cases

**Status: SUPPORTED.**  
**Anchors:** S1:359–377.

The color-versus-party-pair incidence matrix has row and column sums two. If an entry is two, its row and column separate, leaving either two further concentrated rows or two split rows. If there is no entry two, the matrix is binary with exactly one zero in each row and column, hence is equivalent to \(J_3-I_3\).

Thus the three listed families are exhaustive. A split row is excluded by the concentration argument in §7 above; the all-concentrated family is excluded by §8. This ancillary classification does not introduce an uncovered family.

### Exact imports

**Status: SUPPORTED.**  
**Anchors:** S1:383–440; S2:7–16, 28; S3:7–15, 23.

The new contradiction is self-contained from the stated same-tensor hypotheses. It does **not** import:

- no-distance-one;
- no-OLS(6);
- the earlier restriction of possible alphabets to \(\{3,4,5\}\);
- the external-partner obstruction;
- the \(4444\) simultaneous normal form;
- independent pair gauges;
- equal moduli or real phases.

S2 is contextual alignment, not a necessary premise for the new theorem. S3 concerns a distinct \(4444\) class and is not transferred to \(4445\).

The older surviving-profile list retains its inherited no-OLS-dependent interface. An eventual combination of separately supported results must preserve that dependency; this review does not make the whole list no-OLS-independent.

### Complex amplitudes

**Status: SUPPORTED.**

The actual-to-combinatorial implication uses unitary row and column norms, support distinctness and exact extension counts. The contradiction occurs before any phase assignment. It therefore covers arbitrary complex phases and arbitrary nonzero residual moduli compatible with the original hypotheses.

## 10. Unpaid claims and verification boundary

The following remain distinct from the supported theorem:

| Claim or gate | Status in this return |
|---|---|
| Exact whole-\(4445\) actual tensor exclusion | **SUPPORTED by written reconstruction** |
| Necessary common-\(P\), exact-two-extension \(4445\) interface is impossible | **SUPPORTED by written reconstruction** |
| Finite canonical or exhaustive computational verification | **NOTRUN** |
| Exclusion of every other residual profile | **NOT ESTABLISHED here** |
| Universal \(t=24\) exclusion | **NOT ESTABLISHED here** |
| Universal support-\(48\) exclusion or \(N\ge49\) | **NOT ESTABLISHED here** |
| Physical AME witness | **NOT SUPPLIED** |
| Worldwide novelty or priority | **INCONCLUSIVE; not investigated** |
| Printed original-target equivalence or whole original-target resolution | **NOT ESTABLISHED here** |
| Human, independent-family or formal/kernel verification | **NOT PERFORMED here** |
| Parent adoption | **PENDING parent disposition** |
| Rehabilitation of held outputs or their consumers | **NONE** |

No mathematical defect requiring a source-line finding was found. The administrative metadata-count correction is disclosed above and does not alter the reconstructed theorem.

**Overall correctness:** correct

**Explanation:** The complete frozen proof establishes the exact whole-\(4445\) exclusion through a necessary shared-support interface, including the distance-one slice alternative and the simultaneous common-\(P\) matching constraints. It does not establish the broader support-minimum problem, novelty, finite verification or adoption.

**Confidence:** 0.98