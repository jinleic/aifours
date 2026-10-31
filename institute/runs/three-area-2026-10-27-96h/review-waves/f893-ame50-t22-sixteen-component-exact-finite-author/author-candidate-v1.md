# f893 author candidate v1 — exact local finite classification of connected 16-word t22 E components (UNRUN source + written results)

**Status.** NONBLIND, same-harness GENERAL AUTHOR candidate (owner addendum 2). Author `VerifyF893AME22Finite`. Clock observed (`date -u`) before this exclusive write: 2026-10-31T04:02:13Z (an observation before the write, not a creation certificate). Deliverables: this narrative and ONE prepared, **UNRUN** standard-library source

`finite-sixteen-component-v1.py` — SHA-256 `7e280a4e24aa5556d4993627166937603ee4d31c79ef6591afccd618d6915a2e`, 27388 bytes, 716 LF.

No scientific execution, compilation, test, solver, CAS, eval, child process, network or external model was used. Every computational statement below about the source is an intended behaviour, not an observed result. A parent full read and a separate one-shot GO (external bound <=55 s) are required before any run; timeout/partial output is INCOMPLETE, never PASS. Written results in §4 are author claims with written proofs, not adopted results. Nothing here is a P22 completion, AME or support-50 witness, global classification, family/human/formal acceptance, novelty or priority claim.

## 1. Actual object, imports and exact quantifiers

Fix ONE normalized complex AME(4,6) tensor psi, ONE local orthonormal product basis, U=6psi, N=50, t=22; P = the 22 modulus-one words, E = the other 28 (S2|13, S3|3, S6|7–9, S7|7–13, S8|7–9). Imported, parent-adopted or packet-reconstructed facts (named conditional imports; not re-proved here beyond the short derivations given):

- **I1 (pair/cut interface; S3|3, S6|9, S7|9–13, S8|7–9).** In every physical pair, every E value has exactly two E extensions, is disjoint from the 22 distinct P values, and each balanced cut restricted to E is exactly seven K2,2 blocks; one set of words, one coefficient per word, in all six pair systems and all three cuts.
- **I2 (components; S4|5 adopted, S6|59–65, S8|35–41).** Agreement components (distinct E words sharing >=2 coordinates, i.e. sharing a pair value) are closed under all six pair-mate involutions, have size divisible by 4, and E is either one 28-word component or components of sizes 12 and 16. A 16-word component has necessary sorted local profile in {2444, 3333, 3334, 3344, 3444, 4444} (S4|5, S6|65, S8|64).
- **I3 (binary box; S4|5 adopted, S6|47–49, S8|21–23).** Every two-symbol-per-party box contains at most 7 E words.
- **I4 (phase iff; S3 adopted, S6|31–41, S7|37–53).** For the actual support, common unit phases exist iff every integral y with A^T y=0 has even coordinate sum, A the signed cut-indexed square matrix.
- **I5 (12-word component; S5 adopted).** Every 12-word component is the canonical 2333 gadget; 3333 is impossible. Used ONLY as the expectation of engine controls E1/E2.

**Target finite problem (exact).** Let C ⊂ [6]^4 with |C|=16. Call C a *candidate component with sorted profile q* if
(N1) in each of the six pair systems every pair value used by C has exactly two words of C (this is agreement-closure plus the two-extension law of I1 restricted to C);
(N2) for each cut ij|kl, the bipartite graph with rows = ij-values, columns = kl-values and one edge per word of C is a disjoint union of K2,2;
(N3) the agreement graph of C is connected;
(N4) the sorted vector of used alphabet sizes is q, q in the six-profile list.
For each such C the source computes **B(C)** = maximum number of words of C in a two-symbol-per-party box, and **Phi(C)** = [every integral left-kernel vector of A_C has even sum], with A_C the 12x16 signed matrix (one row per cut-indexed block [[a,b],[c,d]]: +1 at a,d and -1 at b,c). It enumerates ALL such C up to party permutations and per-party symbol permutations, and reports each class with B(C), Phi(C) and an exact certificate.

**Why exactly these are the local necessary conditions of an actual 16-word component.** If C is the 16-word component of an actual split E: (N1) is I1 plus I2 closure; (N2) holds because each of the seven K2,2 blocks of a cut has its four words pairwise linked through shared pair values, hence inside one agreement component, so the cut restricted to C is a union of whole blocks; (N3) is the definition of component; (N4) is I2; B(C)<=7 is I3 restricted to C. For Phi: the 21 cut-indexed squares split by component (each block lies in one component), so the global 21x28 matrix A is block diagonal, A=diag(A_C12, A_C16), up to row/column order. Then ker_Z(A^T)=ker_Z(A_C12^T) ⊕ ker_Z(A_C16^T) and the coordinate sum is additive, so

  **(D1)** global even-sum condition of I4  <=>  Phi(C12) and Phi(C16).

With I5, C12 is the canonical gadget, whose phases are paid (S9 Theorem 1), so in the split branch I4 is equivalent to Phi(C16) **together with** the remaining common-P/pair-disjointness conditions, which this local classification does NOT examine. Each 16-word component has 8 values per pair system, so 8 rows/8 columns per cut, 4 blocks per cut and **12 cut-indexed squares**: A_C is 12x16 with two +1 and two -1 per row.

## 2. Decisive written identities used by the source

- **(D2) K2,2 test.** Rows and columns all of degree two; the component of row r with columns c1,c2 is K2,2 iff the other row at c1 equals the other row at c2. Equivalently the ij- and kl-mate involutions commute and w, M_ij w, M_kl w, M_ij M_kl w is a 4-cycle. A word is determined by its (ij-value, kl-value), so the cell (r2,c2) is a unique word.
- **(D3) Degrees.** For x used at party i, its occurrence count is 2 d(x) with d(x) the (common) number of partner symbols at any other party; 2 <= d(x) <= min_{j != i} q_j and sum_x d(x) = 8. Consequently: q_i=2 gives (4,4); q_i=4 gives (2,2,2,2); q_i=3 gives (2,3,3) or (2,2,4), the latter only if no other party has three symbols (S8|64, S10|40). The source reports these multisets per class; they are NOT filters.
- **(D4) Integral kernel and certificates.** Unimodular integer row reduction gives V A = H in echelon form. Rows of V at zero rows of H are a Z-basis of ker_Z(A^T) (V unimodular, nonzero echelon rows independent; S7|53). Parity is additive, so some integral dependency is odd iff some basis row has odd sum. Odd: the basis row y is re-verified (y^T A = 0 exactly, sum(y) odd); by multiplying the phase system A theta = (1/2)1 (mod 1) by y^T it is a complete obstruction. Even: back substitution on the pivot rows gives rational theta with H theta = V(1/2)1 exactly on pivot rows; zero rows have integral right side; hence A theta - (1/2)1 = V^{-1}(H theta - V(1/2)1) ∈ Z^12, and the source re-verifies A theta - 1/2 ∈ Z^12 directly with `Fraction`. Then z_w = exp(2 pi i theta_w) satisfies z_a z_d + z_b z_c = 0 on all 12 squares. Both verdicts are therefore self-certifying, independently of the sufficiency half of I4. Rational theta means roots of unity; with flat moduli 1/sqrt(2) each square is a complex Hadamard block (local partial unitary only).
- **(D5) Sign-only is different.** The mutant evaluator solves A x = 1 over F2 (sign phases). On the S7 formal rows (S7|61–67) the rows sum to zero mod 2 while the right sides sum to 1, so it reports infeasible; the integral kernel of those rows is zero (S7|67), so the integral evaluator must return EVEN with a re-verified rational theta (S7's written torus vector (1/4,1/4,0,0,1/2,0) is one solution; the source's back-substituted theta may differ). The source requires this disagreement.

## 3. Algorithm and written completeness proof

Parties are ordered so that q is ascending; relabelings allowed: per-party symbol permutations and party permutations preserving q (any isomorphism preserves alphabet sizes, so no other party permutation can identify two normalized sets).

**Search state.** A set T of words (LIFO stack), counts of every pair value in T, per-party symbol counts. Root T={0000}. *Pending* = pair values of T used by exactly one word.

**Lemma 1 (root and labels).** Every candidate S has a relabeling S' with 0000 ∈ S' and labels {0..q_i-1} at party i.

**Lemma 2 (invariant T ⊆ S').** Suppose T ⊆ S', S' a candidate, and the labels used by T at each party are a prefix {0..u_i-1}. (a) If T has no pending value, T is a union of mate-closed sets inside S'; since S' is connected, T=S'; so |T|<16 with no pending value is correctly pruned. (b) For any pending value chosen by the (label-dependent) rule, S' contains exactly one further word v with that value (its mate). v ∉ T and every pair value of v is used at most once in T (S' uses it exactly twice). If v has a symbol x unused by T at party k, x ≥ u_k and x < q_k; swapping labels x and u_k in S' fixes T, keeps a candidate, and makes v[k]=u_k. Hence v is among the generated candidates `coordinate < min(u_k+1, q_k)` with counts <=1. (c) Forced closure: if in T a word w has its ij-mate w1 and kl-mate u both present, then by (D2) applied to S' the word v=(ij-value of u, kl-value of w1) lies in S'; mates found inside T are the mates in S' because each value has exactly two words in S'. So adding v keeps T ⊆ S', and if v cannot be added (size 16 reached or a value already used twice) no candidate extends T. (d) Prunes are valid: each new word settles <= 6 pending values (`pending <= 6*rem`); each pair system has exactly 8 values in S' (`<= 8`); by (D3) a used symbol needs final even count >= max(4, 2*partners_in_T, count rounded up to even) and <= 2*min_{j != i} q_j, and each still-unused label needs >= 4 occurrences, while each new word contributes exactly one occurrence per party (`need <= rem`).

By induction every candidate class is reached by at least one leaf; at that leaf no value is pending, |T|=16, forced closure has closed every cut 4-cycle (so (N2) holds), connectivity holds by construction, and the leaf is recorded only if every party uses exactly q_i labels. **Every recorded set is re-validated by an independent from-scratch validator** (`structural_reason`), which shares no code with the search; any failure sets INTERNAL_INCONSISTENCY.

**Class identification.** `relabel_run(S, sigma, b)`: reorder parties by sigma, map b to 0000, repeatedly add the mate completing the lexicographically least pending *relabeled* pair value, labelling new symbols by first appearance per party. Its output depends only on the isomorphism type of S and the choice (sigma, b): relabeling S by g and choosing (sigma∘g_party^{-1}, g(b)) gives an identical output. Hence the set Out(S) of all outputs is an isomorphism invariant, each output is a relabeled copy of S, and S ≅ S' iff one output of S' lies in Out(S). The class canonical form is min Out(S); |Aut(S)| = |Sigma_q|·16/|Out(S)| is reported as a consistency value (must be integral). A fixed nontrivial relabeling (last q-preserving party permutation, reversed alphabets) is applied to every representative and must reproduce the canonical form.

## 4. Written results (author claims; fresh examples, no execution)

**Theorem A (a phase-feasible 16-word 2444 local component exists).** Let parties be (A,B,C,D), i ∈ Z/4, L_i=(i,i,i), R_i=(i,i+1,i+2), and BIP16 = {L_i, R_i} × {0,1} (D binary). Then BIP16 satisfies (N1)–(N4) with profile 2444, B=4 <= 7, and Phi holds.
*Proof.* L and R triples are distinct (R has three distinct coordinates). AB values (i,i),(i,i+1); AC values (i,i),(i,i+2); BC values (i,i),(i+1,i+2): eight distinct each, each with the two D values. The triples with A=a are L_a,R_a; with B=b are L_b,R_{b-1}; with C=c are L_c,R_{c-2}: each XD value has exactly two words. Every cut pairs D with one ternary-like party X: the row of a triple's other two coordinates (or the (x,d) row) meets the two columns of the other triple with the same X symbol, giving K2,2 by (D2). The triple graph (share one coordinate) joins R_i to L_i, L_{i+1}, L_{i+2} and never two triples twice (L_j vs R_i share A iff j=i, B iff j=i+1, C iff j=i+2); it is cubic bipartite and connected; D-flips connect the two copies. A box takes two A, B and C symbols; two L's force X=Y=Z={a,b} which contains no R_i (i, i+1, i+2 distinct); a box with R_i,R_j has X∩Y∩Z = ∅ for j=i±1, ±2; hence at most two triples, B=4. Phases: every square is [[U_{t0},U_{t1}],[U_{t'0},U_{t'1}]] for an edge t–t', with equation r_t = -r_{t'}, r = z_0/z_1; theta(L_i,d)=0, theta(R_i,0)=1/2, theta(R_i,1)=0 gives r_L=1, r_R=-1 on every L–R edge. ∎
*Consequence (scope-limited).* For profile 2444 the local conditions (N1)–(N4), B<=7 and Phi alone do **not** exclude a 12+16 split; any exclusion must use the common P22 / pair-disjointness with C12 or global profile data. This is NOT a completion: BIP16 is a 16-word partial unitary with 28 zero rows/columns per 36x36 cut and no P.

**Proposition B (incidence-only survivor failing Phi).** TRI16 = {000,011,110,122,203,231,323,332} × {0,1} satisfies (N1)–(N4) with profile 2444 and B=6, but has an odd integral dependency.
*Proof.* Each symbol occurs exactly twice per coordinate (A:00112233, B: 0 in 000/203, 1 in 011/110, 2 in 122/323, 3 in 231/332; C: 0 in 000/110, 1 in 011/231, 2 in 122/332, 3 in 203/323); the twelve mate pairs 000–011(A), 000–203(B), 000–110(C), 011–110(B), 011–231(C), 110–122(A), 122–323(B), 122–332(C), 203–231(A), 203–323(C), 231–332(B), 323–332(A) are distinct, so no two triples share two coordinates; (N1),(N2) follow as in Theorem A. Boxes: for each pair of A symbols the four triples carry at least three distinct B symbols, so at most three triples fit, B=6 ({0,1}^3 attains it). The triangle 000–011–110 gives r_000=-r_011=r_110=-r_000, i.e. the three square rows with signs sum to zero while their right sides sum to 3/2: an odd integral dependency. ∎

These two examples are encoded as engine controls E3/E4: the 2444 search must find both classes.

## 5. Controls and intended-reason mutants (all expectations written before any run)

| id | input | intended reason / expectation |
|---|---|---|
| M1 | CYCLE8 = (k%2,k//2,k%2,k//2),(k%2,k//2,(k+1)%4%2,(k+1)%4//2), k<4 | AB|CD rows/columns all degree 2 but one 8-cycle: `cut_is_k22_union` False |
| M1+ | EVEN8 (eight even binary words) | all three cuts K2,2 unions: [True,True,True] |
| M2 | EVEN8 minus 0000 | value AB=00 has one word: pair test False |
| M3 | EVEN8 | passes (N1)–(N3) structurally (None) but box maximum 8 > 7 (I3 reason) |
| M4 | EVEN8 | ODD integral dependency (contains r1+r2-r3=0 of S6|53–57, coefficient sum odd) |
| M5 | S7 three formal rows | integral: EVEN with theta; sign-only MUTANT: infeasible (rows sum to 0 mod 2, right side 1) |
| M6 | canonical gadget (S9 (4)) | structural None, box<=7, EVEN |
| M7 | S9 triangular prism | structural None, box 6<=7, ODD |
| M8 | gadget ∪ shifted disjoint copy (24 words) | reason DISCONNECTED |
| M9 | gadget against profile 3333 | reason PROFILE |
| E1 | search N=12, profile 3333 | 0 classes (I5) |
| E2 | search N=12, profile 2333 | finds gadget and prism; the EVEN classes are exactly [gadget] (I5); all raw sets pass the independent validator |
| E3/E4 | search N=16, profile 2444 | BIP16 class found, box<=7, EVEN; TRI16 class found, box<=7, ODD |

E1/E2 expectations rest on the adopted import I5; a failure would be reported as CONTROL_FAIL (it would contradict the engine or I5, and could not be silently absorbed). E3/E4 rest on §4.

## 6. Run contract (for the separate parent GO)

Command: `python3 finite-sixteen-component-v1.py` in this wave directory, no arguments, stdin unused; stdout is one JSON report; no file is written. `LIMIT_S=38.0` cooperative internal limit from module import (<=40 s). Exit 0 = `COMPLETE_LOCAL` only if every control passes, all six profiles finish, every class re-validates, relabeling invariance holds and every phase certificate verifies; 2 = `INCOMPLETE` (timeout; `in_progress_profile` names the unfinished profile, completed profiles are still printed but carry no PASS); 3 = `CONTROL_FAIL`; 4 = `INTERNAL_INCONSISTENCY`. Per profile the report gives search nodes, raw labeled solutions, classes (canonical words, automorphism count, degree multisets, box maximum and argmax, phase verdict with rank, kernel rank, basis parities and certificate y or theta, the 12 squares) and the counts `n_classes_box_le_7` and `n_classes_box_le_7_and_even`. Runtime is not estimated or promised; a timeout is an admissible INCOMPLETE outcome.

## 7. Boundary cases and limits

- Only symbols actually used by C are relabeled; an embedding into the six physical symbols per party is any injective relabeling, so "up to relabeling" covers it. Profiles are of C, not of global E.
- Components with box > 7 are reported (not silently dropped) but are excluded for an actual E by I3. A class with Phi false is excluded as a C16 of an actual tensor by D1+I4. A class surviving B<=7 and Phi is only a **local** survivor: pair-disjointness from C12, the common P22 coverage/injectivity, and the global profile constraints (S4|7, S6|77–93) are not examined.
- The connected 28-word case, the ten split profiles' global P conditions and every other t are outside this source. No claim that the 3566/3666/4456 connectivity results or any profile decision follows from it.
- The source is unrun; no count of classes, no runtime and no verdict for the target is asserted here beyond the written §4 statements.

## 8. Reading, sequence and process declarations

1. Before any body: read manifest (294 LF), freeze receipt (271 LF), final binding (223 LF), live metadata (284 LF), actual dispatch receipt (62 LF). Initial structural displays elided nested lines; each was then re-read completely in RAW (manifest 1–142,142–294; receipt 1–140,136–271; binding 16–120,120–223 after full lines 1–15; metadata 22–160,156–284 after full lines 1–21; dispatch receipt line 60, first shown truncated at 768 chars, re-read whole). Parent's IRC confirmation of the dispatch receipt arrived after I had already read the existing receipt; I then read all 22 controls completely in RAW (live SHA-256 = pins). Controls: status/permissions only.
2. Wrote `prebody-ack-v1.md` (3361 B) and sent Main the direct PREBODY ACK before any packet body or mathematics.
3. Measured per-window bytes (`LC_ALL=C awk`, metadata only): every 20-LF window <= 5804 bytes, longest line 1528 bytes. Read part 01 RAW in windows 1–20, 21–40, …, 381–400, 401–418 and part 02 RAW in windows 1–20, …, 381–400, 401–416, through both endings (S7|119, S10|139), at most two consecutive windows per tool batch, consumed in ascending order. No clipping observed; no recovery needed. Bodies covered: S1 1–40, S2 1–15, S3 1–21, S4 1–16, S5 1–34, S6 1–143, S7 1–119, S8 1–141, S9 1–122, S10 1–139.
4. No linked or unlisted file, held episode, held consumer, sibling output, old code (including f806/f815 sources) or control-named path was opened. All genuine held episodes and all their consumers remain NONINPUT.
5. Process notes: one earlier assistant response hit an output-length limit and was discarded by the harness before any of its tool calls ran (system notice; nothing was written or executed by it). The write tool automatically set the executable bit on the source (permission metadata only; never executed). The source was revised once in place before its hash was pinned (adding the written E3/E4 controls and the `in_progress_profile` marker); the pinned hash above is the only delivered version. Commands used: `date`, `ls`, `shasum`, `wc`, the awk byte measurement; no scientific execution.
6. This narrative was revised once in place before delivery to replace an unfinished `theta=(…)` phrase in (D5) by the explicit statement now shown; no other content changed.
