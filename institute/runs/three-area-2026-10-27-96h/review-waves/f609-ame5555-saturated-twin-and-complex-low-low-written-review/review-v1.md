# f609 WRITTEN review: saturated twins and the complex low–low obstruction

**Role:** WRITTEN  
**Disposition:** SUPPORTED at the exact fixed-profile scope below.  
**Candidate findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Scientific execution:** **NOT RUN.**  
**Adoption:** This review is one same-harness written gate, not parent adoption or completion of the other required gates.

## 1. Read coverage and process boundary

Before reading the mathematical packet, I read through the endings of:

- `manifest-v1.json`, LF1–125;
- `freeze-receipt-v1.json`, LF1–47;
- all thirteen declared status-only controls;
- `parent-live-metadata-supply-v1.json`;
- `parent-dispatch-receipt-v1.json`.

I then sent the required direct administrative pre-body ACK to `agent://Main`. Only afterward did I read `literal-packet-v1.md`, in ordered raw windows LF1–20, 21–40, continuing in windows of at most twenty lines through LF561–580 and finally LF581–582. The complete packet was read through its ending before derivation.

This covers:

- **S1:** the entire f597 author candidate, logical lines 1–531;
- **S2:** the entire earlier \(4455\) disposition, lines 1–49.

The distinction between S1’s 530 LF characters and 531 logical source lines is retained; I did not treat the receipt’s LF count as permission to omit its final logical line.

**Pins used, as parent-supplied observations rather than child-recomputed hashes:**

- Manifest: `96c42d0d0d7fe836717a7d59678cbbd0d2e4790866801c7ba25b15f410a32af8`
- Receipt: `cf989abb526f41d5bb872473ced4309e6479113c4d664e59c9497376aaf7d1a5`
- Packet: `d36a91f1ee298f0733532f5f48eebcc5606b84538909123b26c302ce1ac6509f`
- S1: `9cd3311e6ae8eb98b9437f0ae6652f5ce9552a26e94213af47e01500a8fa25af`
- S2: `faadf4777ac1b3f0e57d484624080a08835c9d71de980b87ad823866531f3bb4`

**Administrative correction to my ACK:** its dispatch-receipt endpoint wording was not an independently measured file-length observation. The actual operation was a raw LF1–20 request, read through the closing brace. I withdraw the unsupported endpoint count, not the complete-read or pre-body ordering statement.

No linked scientific source, author code, sibling review, held scientific payload, or held consumer was opened. S2 was read as supplied architectural context; its \(4455\)-specific conclusions and reported finite results were not substituted for a \(5555\) derivation. No scientific executable, enumeration, CAS, solver, external model, or additional selected state, word configuration, phase assignment, gauge, or parameter instance was used.

These are statements about this review’s access and work, not a clean-cognition certificate.

## 2. Exact theorem reviewed

The supported conditional contradiction is:

> There is no complex tensor \(U=6\psi\) whose three balanced \(36\times36\) flattenings are unitary, whose support has exactly \(48\) entries, whose modulus-one support has exactly \(24\) entries, and whose remaining \(24\) entries use exactly five symbols at each of the four physical parties.

The proof retains the same actual tensor, maximal support \(P\), and residual support \(E\) throughout. Its final contradiction uses their actual complementary pair projections, not independently realizable shadow graphs or separately chosen completions.

The following is my written reconstruction of every load-bearing step.

## 3. Same-tensor interface and \(5555\) degree profiles

**Status: SUPPORTED — S1 lines 47–103.**

Every entry has modulus at most one because it belongs to a unit-norm row of a balanced unitary flattening. Thus the support partitions into the declared sets \(P\) and \(E\), each of size \(24\).

A modulus-one entry exhausts its row and column norms. Applying this to all three balanced cuts shows, at every one of the six physical pairs:

1. the projection of \(P\) is injective;
2. no residual word shares a projected pair with \(P\);
3. exactly twelve pair values remain outside the projection of \(P\).

For any balanced cut, all twelve remaining rows must have nonzero residual support. None can have a singleton residual entry, since its row norm would make that entry modulus one. The total residual support is \(24\), so each remaining row has exactly two entries. The same holds for columns.

Consequently each residual physical pair has exactly two extensions in the same \(E\), and every residual pair shadow has size twelve.

Two residual rows sharing a column must share their second column: otherwise their inner product consists of precisely one nonzero term. The actual residual flattening therefore decomposes into six full nonzero \(2\times2\) blocks. This conclusion uses the actual complex unitary matrix; it is not merely a degree-two graph assertion.

For a residual symbol \(a\) at party \(i\), its occurrence count is twice its number of neighbors at any other party. Hence that neighbor number \(r_i(a)\) is independent of the other party, and its sum over the five residual symbols is twelve.

Degree one is impossible: the two occurrences of such a symbol would have the same unique neighbor at each of the other three coordinates and would therefore be the same word. The five degrees are thus at least two, giving exactly the profiles

\[
(3,3,2,2,2),\qquad (4,2,2,2,2).
\]

In particular every slice has four, six, or eight words. Pair complementarity also gives

\[
p_i(a)=6-r_i(a),\qquad p_i(o_i)=6.
\]

No \(4455\)-specific degree restriction is needed here.

## 4. Maximal-word moments and outside occupancy

**Status: SUPPORTED — S1 lines 107–191.**

Each party contributes eighteen internal-coordinate occurrences to \(P\), so the first maximal-word moment is \(72\). Each physical pair has thirteen internal maximal pairs, giving the second moment \(78\).

Together with \(|P|=24\), these imply the displayed identities

\[
3n_0+n_1+n_4=6,\qquad
n_4=3n_0+2n_1+n_2.
\]

Each of the six outside pairs occurs in exactly one maximal word, so

\[
6n_0+3n_1+n_2=6.
\]

There is at most one all-outside word. There is also at most one word with exactly three outside coordinates: two such words would agree on an outside physical pair. These facts yield exactly the three listed necessary histograms:

\[
(1,0,0,20,3),\quad
(0,0,6,12,6),\quad
(0,1,3,15,5).
\]

For an internal symbol \(a\), the three pairs \((a,o_j)\) each occur once in \(P\). Therefore its maximal occurrences satisfy

\[
\sum_h m_h(a)=6-r_i(a),\qquad
\sum_h h\,m_h(a)=3,
\]

and hence

\[
r_i(a)=3-m_0(a)+m_2(a)+2m_3(a).
\]

A degree-four symbol has two maximal occurrences, whose outside occupancies must be \(\{0,3\}\) or \(\{1,2\}\). The consequence for regime A follows.

These are necessary-count statements, not assertions that any histogram is realizable. The final contradiction does not rely on a histogram being realized or on a \(4455\) exceptional-party restriction.

## 5. Saturation of every distance-one pair

**Status: SUPPORTED — S1 lines 195–258.**

Suppose two actual residual words differ only at coordinate \(i\), with symbols \(a,a'\), and let \(T\) be their common three-coordinate slice.

For each other coordinate \(j\), the rows \((a,t_j)\) and \((a',t_j)\) share a column in the corresponding balanced cut. Actual \(2\times2\) closure gives the same second column in both rows. Thus equality at coordinate \(j\) defines a fixed-point-free matching on \(T\).

The three matching edges at a vertex are distinct. If two coordinate matchings paired the same two triples, the triples would agree at those two coordinates; their copies at both \(a\) and \(a'\) would produce four extensions of that physical pair. This contradicts multiplicity two.

The matching graph is therefore simple and cubic. Its actual nonzero complex quantities

\[
z_t=U_{a,t}\overline{U_{a',t}}
\]

satisfy \(z_t+z_{t'}=0\) along every matching edge, by the corresponding actual row orthogonality. An odd cycle would force a nonzero \(z_t\) to equal its negative. The graph is bipartite.

Each side of a nonempty simple cubic bipartite component has at least three vertices. Since a symbol slice has at most eight words, the common slice has size six or eight.

- **Six triples:** each remaining coordinate uses exactly three values, twice each. If either complete symbol slice had eight words, its last two triples could use none of those saturated values. Both would have to use its single fourth neighbor at each coordinate and would coincide. Thus both complete slices have size six.
- **Eight triples:** both symbols would have degree four, impossible in either \(5555\) degree profile.

Every distance-one pair therefore consists of the two degree-three symbols of an ordinary party, with identical complete six-triple slices. Its saturated component has twelve words. In particular, no distance-one pair can vary through a low symbol.

Different-coordinate twin components are word-disjoint. A word in both would allow both twin replacements, giving four distinct words with the same complementary physical pair. Since there are only twenty-four residual words, at most two twin coordinates can exist. The ordinary profile permits at most one twin pair at a given party.

## 6. Low–low routing and the actual complex obstruction

**Status: SUPPORTED — S1 lines 262–357.**

Consider an arbitrary actual low–low residual pair \((a,b)\). Its two extensions cannot be identical. If they differ at one complementary coordinate, the preceding lemma gives a twin at that coordinate.

For the remaining case, use the candidate’s literal notation:

\[
(a,b,c,d),\qquad(a,b,c',d'),
\]

with both complementary coordinates different.

The low \(a\)-slice has four words, with two values occurring twice at every other coordinate. Its three equality partitions are perfect matchings. The \(j\)-matching differs from both other matchings because the displayed extensions differ at \(k,\ell\).

The \(k\)- and \(\ell\)-matchings cannot coincide: their common partner through a word with \(j=b\) would form a distance-one pair varying through the low symbol \(b\). All three matchings are therefore distinct, forcing the four words displayed in S1 lines 285–286.

Applying the same argument to the low \(b\)-slice forces the additional two words in lines 292–293. Actual block closure then forces the final two words:

- In the \(ik\mid j\ell\) cut, the rows containing \((a,b,c,d)\) and \((a',b,c',d)\) share column \((b,d)\).
- Their other columns must coincide, forcing \((a',b',c',d')\).
- The corresponding closure for the other existing pair forces \((a',b',c,d)\).

These are precisely the eight literal even-parity words in the packet. Their binary labels describe the actual forced symbols; no additional tensor instance or phase choice is introduced.

Each physical pair used by these eight words already has its two extensions inside the eight-word set. Therefore no other residual word can add a term to the relevant rows. In each balanced cut, the eight words form two closed full \(2\times2\) blocks: equal row/column parity gives the even block and the odd block. This checks closure in all three cuts, rather than only the cut used to force the last two words.

### Complex orthogonality

The three displayed row equations have the stated actual indices:

1. In \(ij\mid k\ell\), rows \(00,11\) share columns \(00,11\).
2. In \(ik\mid j\ell\), rows \(00,11\) share columns \(00,11\).
3. In \(i\ell\mid jk\), rows \(01,10\) share columns \(01,10\).

They give exactly

\[
u_{0000}\overline{u_{1100}}
+u_{0011}\overline{u_{1111}}=0,
\]

\[
u_{0000}\overline{u_{1010}}
+u_{0101}\overline{u_{1111}}=0,
\]

\[
u_{0011}\overline{u_{1010}}
+u_{0101}\overline{u_{1100}}=0.
\]

Every summand is nonzero. Each equation therefore equates the two summand magnitudes and makes their normalized phases negatives. With precisely the packet’s \(X,Y,Z\), this yields

\[
X=-Y,\qquad X=-Z,\qquad Y=-Z.
\]

The latter two give \(X=Y\), contradicting the first because these products are nonzero complex numbers.

No equal-modulus premise was inserted: equality of the relevant product magnitudes follows separately from each two-term orthogonality equation. Nor is the argument restricted to real signs or an \(\mathbb F_2\) phase fixture.

The two-coordinate-difference case is impossible. Thus every low–low edge must route to a twin at one of its two complementary coordinates. The downstream use of this conclusion in the twin-count cases is valid.

## 7. Zero and one twin coordinates are impossible

**Status: SUPPORTED — S1 lines 361–405.**

### Zero twins

The routing lemma forbids low–low edges at every physical pair. Every low symbol needs two distinct neighbors at each opposite party, so each party must have at least two high symbols. Thus all parties are ordinary.

Between any two ordinary parties, the three lows each meet both opposite highs. Those six edges exhaust the opposite highs’ total degree. Applying the same statement in the opposite direction gives exactly

\[
R_{ij}=(L_i\times H_j)\ \dot\cup\ (H_i\times L_j).
\]

An actual residual word has four low/high statuses. Two statuses must agree, producing a prohibited low–low or high–high pair. Hence zero twins is impossible.

### One twin

Let \(i\) be the sole twin coordinate. For any \(j\ne i\), a low–low edge at \(ij\) would need a twin at a complementary coordinate, where none exists.

The three lows at \(i\) therefore force every other party to be ordinary, and the same degree saturation gives the displayed cross-only shadow at every \(ij\).

There are twelve residual words with coordinate \(i\) low. All their other coordinates are high. At any two other parties, these twelve words project into only four high–high pair values. Actual pair multiplicity two permits at most eight such words, a contradiction.

Together with the at-most-two result, this proves that there are exactly two twin coordinates.

## 8. Two twins and the final same-\(P\) collision

**Status: SUPPORTED — S1 lines 409–491.**

Let the twin coordinates be \(i,j\). Their disjoint twelve-word components exhaust the same \(E\). Every word using an \(H_i\) symbol belongs to \(C_i\), and every word using an \(H_j\) symbol belongs to \(C_j\), because the corresponding symbol slices are complete twin slices. Hence no residual word contains both:

\[
R_{ij}\cap(H_i\times H_j)=\varnothing.
\]

At either remaining coordinate \(k\), each component uses three symbols, each four times. Since the components exhaust \(E\), their alphabets have union \(A_k\), of size five. They intersect in one symbol. That symbol has eight occurrences and degree four; the other four have four occurrences and degree two. The same reasoning applies at \(\ell\).

This establishes the stated ordinary/ordinary/exceptional/exceptional arrangement without assuming it beforehand.

For any \(a\in H_i\), \(b\in H_j\), the missing residual pair \((a,b)\) has a unique maximal completion in the same \(P\).

Its \(k\)-coordinate cannot lie in \(B_k^i\), since every pair \((a,c)\) with \(c\in B_k^i\) is residual. It cannot lie in \(B_k^j\), since every pair \((b,c)\) with \(c\in B_k^j\) is residual. Their union is all of \(A_k\), so the maximal word must use \(o_k\). Likewise it must use \(o_\ell\).

Thus all four distinct pairs in \(H_i\times H_j\) require distinct maximal words with the same complementary pair \((o_k,o_\ell)\), contradicting injectivity of the \(k\ell\) projection of \(P\).

The physical-pair consumers are complete:

- \(ij\): the four high–high pairs are absent from \(E\) and therefore supplied by \(P\);
- \(ik,jk\): residual neighborhoods force the maximal \(k\)-coordinate outside;
- \(i\ell,j\ell\): residual neighborhoods force the maximal \(\ell\)-coordinate outside;
- \(k\ell\): the resulting maximal-pair collision contradicts injectivity.

No independent complement, local gauge, or replacement maximal support enters this dispatch.

## 9. Boundary cases, imports, and findings

**Boundary coverage:** SUPPORTED.

- Residual amplitudes are nonzero by definition; every phase normalization and sign-propagation step therefore has a nonzero operand.
- Degree-one symbols are excluded explicitly, rather than silently omitted.
- Both possible common-slice sizes, six and eight, are handled.
- Low–low extensions differing at one or two complementary coordinates are both handled.
- Zero, one, and two twin coordinates are all disposed of after proving the upper bound.
- Ordinary and exceptional placements are not preselected.
- All maximal-word histograms are covered; the final argument does not depend on choosing one.
- All six physical pair projections and all three balanced cuts are used with their actual common-tensor meaning.

**Imports:** The proof reconstructs its operative \(P/E\), degree, twin, low–low, and completion statements within S1. S2 provides historical architecture only. No \(4455\)-specific exceptional-party bound, rounding theorem, Euler–Tarry/no-OLS theorem, reported finite result, linked review, or held material is a load-bearing premise of this reconstruction.

**Findings:** None. No FATAL, MAJOR, or MINOR mathematical defect was found within the exact theorem reviewed.

## 10. Verdict and acceptance boundary

**Overall correctness:** correct.

**Explanation:** The complete written reconstruction supports the contradiction for the entire actual complex residual-alphabet profile \(5555\) under the stated support-\(48\), exactly-\(24\)-modulus-one, three-unitary hypotheses. The saturated-twin reduction, arbitrary-complex low–low obstruction, zero-/one-twin exclusions, and final same-\(P\) collision all close without an unpaid import. This is one scoped same-harness WRITTEN return; the candidate remains UNADOPTED pending the remaining required gates and parent disposition.

**Confidence:** 0.97.

This review does **not** exclude \(4555\), establish an unconditional complete residual-profile list, exclude every \(t=24\) tensor or every support-\(48\) tensor, prove \(N\ge49\), or determine the global minimum. It supplies no finite-execution, independent-family, human, formal/kernel, novelty, priority, or printed-source-equivalence assurance.