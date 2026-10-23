DISPOSITION: K5NF-r2=ACCEPT; HALL3-r1=ACCEPT

**K5NF-r2 — FATAL: none; MAJOR: none; MINOR: none.**

- **Projection lemma is sound.** SB2 forces support exactly \(A\), with all three coordinates nonzero; this is justified by the accepted lossless normalization, not an additional assumption (`code/gram_a.py:271–281`; `review/K4K5_ENCODING_SOUNDNESS.r3.md:107–111`). Column-0 orthonormality removes coordinate 0. Under the contradiction assumption, Lemma 2 forces at least two A-coordinates, leaving at most one B-coordinate. Completeness supplies four distinct B-bearing vectors, whose nonzero A-projections are pairwise orthogonal in the two-dimensional \(v^\perp\cap\mathbb C^A\). Complex phases do not alter this argument. A vector using three A-coordinates simply cannot be selected as B-bearing; multiple vectors using the same B-coordinate cause no problem (`review/K5_RESIDUAL_NORMAL_FORM.r2.md:16–39`).

- **Residual symmetry is legitimate.** Precisely, before sorting rows,
  \[
  Q'_{\rho(s)}(i,\sigma(j))=P_\sigma Q_s(i,j),
  \quad \rho(1)=1,\quad \rho(s)=\sigma(s+2)-2\ (s\ge2).
  \]
  Thus columns and coordinates 4–7 are permuted, columns and coordinates 0–3 fixed, and squares 2–5 relabelled. Every square remains a QLS; tensor-product orthogonality survives the common cell permutation and unitaries. Square relabelling is independently legitimate because the conditions quantify symmetrically over squares, despite its omission from r3’s enumerated moves. Row 0, P4, reduced-K5 membership and SB2 survive. A common permutation of rows 2–7 then restores ROWLEX while fixing rows 0 and 1, allowing the accepted bridge to apply (`review/K5_RESIDUAL_NORMAL_FORM.r2.md:48–67`).

- **Ordering and root indices agree.** ROWLEX compares coordinates 0,1,…,7, most significant first (`code/gram_a.py:248–270`). Every A-meeting support exceeds \(C_k\); any different B-subset of cardinality at least \(k\) must use an earlier coordinate than \(C_k\). Hence \(C_k\) is the unique minimum support, although several vectors may share it. Cube indexing instead assigns coordinate \(j\) weight \(2^{j-1}\): \(\{7\}\mapsto64\), \(\{6,7\}\mapsto96\), \(\{5,6,7\}\mapsto112\). The note correctly distinguishes these orders (`review/K5_RESIDUAL_NORMAL_FORM.r2.md:57–66`; `README.md:186–189`).

- **Conclusion has the correct scope.** Only c112’s accepted refutation is used. Complete independently accepted c064/c096 subtree refutations, this lemma and the necessity bridge would exclude reduced K5; those obligations remain unfinished. This does not establish \(F\) UNSAT or transfer arbitrary Boolean models. No K4 result is needed or obtained (`review/K5_RESIDUAL_NORMAL_FORM.r2.md:69–88`; `parent/moqls8-k5-root-parent-verdict.md:5`; `review/K4K5_ENCODING_SOUNDNESS.r3.md:112–114`).

**HALL3-r1 — FATAL: none; MAJOR: none; MINOR: none.**

- **Necessity holds in both orientations.** Three orthonormal rows cannot occupy two columns; apply the same argument to \(U^*\) for columns. Parallel lines present no exception. Intersecting lines give, after reindexing, \(1\oplus U'\): the shared-cell overlap is 1 and its other row/column entries vanish. The encoder’s self/common-line constants and unordered-pair variables represent exactly these support bits (`review/HALL3_PATTERN_NECESSITY.r1.md:8–19`; `code/gram_a.py:127–138`).

- **The counterpattern works.** In \(J_{3\times2}\oplus J_{2\times3}\oplus I_3\), distinct rows intersect in 0, 2 or 3 positions, as do columns; every row and column is nonempty. It therefore passes the actual G3 tests, but its first three rows occupy only two columns and violate H3. This establishes a gap in G3 alone, without claiming a full-\(F\) countermodel (`review/HALL3_PATTERN_NECESSITY.r1.md:23–30`; `code/gram_a.py:179–190`).

- **Count, restriction and folding are sound.** There are \(5\cdot15\cdot56\cdot28\cdot2=235{,}200\) candidates, each with \(3\cdot6=18\) positions. Restricting to row 0 against the other 15 lines selects valid necessary clauses. Folding True drops a tautology; deleting False preserves equivalence. No candidate becomes empty: for parallel lines only diagonal positions are constant zero; for intersecting lines the selected rectangle retains nonshared row/column pairs unless already tautological (`review/HALL3_PATTERN_NECESSITY.r1.md:34–47`; `code/h3_pilot.py:53–66,157–176`).

- **Certificate accounting must preserve formula identity.** A checked \(F\land c\) refutation implies \(F_{H3}\land c\) UNSAT. Conversely, refuting \(F_{H3}\land c\) need not refute \(F\land c\). DRAT bytes have no automatic transfer in either direction: RAT steps need not survive added clauses; acceptance against another CNF requires checking that exact target. Both kinds of accepted refutation may contribute to a genuine-configuration cover, with their respective formula bindings and the H3 necessity bridge. H3 certificates cannot mark old-\(F\) leaves CERTIFIED, nor can old receipts silently acquire new formula identities (`review/HALL3_PATTERN_NECESSITY.r1.md:46–47,61–63`).

**Novelty:** Neither note establishes external originality. H3 is a Hall/rank support condition; its strict strengthening of full \(F\) remains unproved.

**Significance:** Accepting r2 makes c016.L2.040.L3.104 unnecessary for the semantic K5 route. The other 121 accepted root proofs and UNKNOWN c016/c032/c048/c080 remain in the Boolean ledger. H3’s possible search benefit is separate. Neither K4 nor K5 is excluded.

Static generator inspection matches the stipulated family, pinned-map lookup, constants, orientations, count and absence of new variables. Its controls cover the bad pattern, identity, permutation, Fourier and block-Hadamard supports, plus the relaxed classical positive control (`code/h3_pilot.py:147–205,214–278`). No controls or solvers were executed; no desk census was used as a premise.

K5NF-r2 FATAL=0 MAJOR=0 MINOR=0  
HALL3-r1 FATAL=0 MAJOR=0 MINOR=0  
GENERATOR: CONSISTENT