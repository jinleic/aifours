# v131-B — review of RQLS10 v35–v38 (449 LF): mathematics, and dependency, application and trust

- **Reviewer:** InfoRecursiveMDS18-2.
- **Author:** PhysicsRQLS10-2.
- **Clock:** actual `/bin/date` before this body: **Mon Oct 26 10:04:45 PDT 2026**.
- **What this is:** a same-harness written reconstruction from the supplied source.
- **What this is not:** blind, configured-family, human, formal, kernel, executable, finite-witness, novelty, priority or current-openness acceptance.
- **Method:** exact symbolic written reasoning only. No interpreter, calculator, eval, CAS, program, enumeration, solver, replay, CLI or nested agent. No decimal, magnitude or chosen-instance probe.

## 0. Separate verdicts (process findings are not mathematical counts)

**MATHEMATICS — whole union, claim classes I–V below:** 0 FATAL, 0 MAJOR, 1 MINOR.
- Every new claim is WRITTEN RECONSTRUCTED at the named elementary interfaces (§7).
- The MINOR is precision only and is repaired in this review (§4, III-1). The v37 §1 normalization H = I+iC tacitly uses a global complex conjugation of the ray array for the case H = I−iC. It says only "harmless common phases/permutations". The step is valid, by the same symmetry v35 §5 uses explicitly, and no conclusion changes.

**DEPENDENCY / APPLICATION / TRUST — whole union:** 0 FATAL, 0 MAJOR, 0 new MINOR.
- This holds at the registered modern 1-RQLS10 definition boundary of S72, with the trust qualifications of §7.
- One boundary is NAMED_NOT_RECONSTRUCTED: I did not independently re-authenticate the Zhang–Cao source, which was not supplied. The application uses only the definitions S72 states explicitly.

**Theorem actually supported (V).** Take any 10x10 ray array q_(a,b) = K_a∘conj(H_b)/sqrt10 where:
- K and H are each independently monomially equivalent to one of the four central Petersen Hadamards;
- this includes arbitrary independent row/column phases and permutations, signs, both category orders and any relative column pairing;
- followed by any common unitary, complex conjugation or transposition of the array.

Then the array admits NO full quantum-transversal resolution. So it is not a 1-RQLS10 at all, and in particular not a maximal one. The quantifier distinctions are retained:
- in the mixed and conference/conference cases, ten specific cells lie on no transversal;
- in the golden/golden case, no transversal exists at all.

**What is not claimed.** This is not a statement about arbitrary complex Hadamards, the full Type-IV biunitary master, A5-WLOG, arbitrary arrays, or the original maximal 1-RQLS10. That remains UNKNOWN, and every intrinsic 10 / 4+6 / 5+5 / noncovariant branch remains open. The positive 100-ray QLS10 of v35 is NOT a 1-RQLS witness. The executable finite-witness independent-checker, control, vendor and priority gates were NOT PERFORMED under HOLD.

## 1. Exact coverage and chronology (bounded documentary record)

**Before my ACK.** After receiving the dispatch I:
1. saved the whole primary state: checkpoint-128, SHA256 `30b6b98e…95fd`;
2. read v9, v10, v11, HOLD and the opaque envelope, each completely, in that order;
3. wrote the opaque ACK `peer-review-v131-B-opaque-ack-v1.json`, SHA256 `9b64fd3ec2517e7bf88b82925231f159fc4a1916cf314c15d4a88d73f748f96c`, 112 LF;
4. sent it to Main and waited.

**After Main's explicit release** (release record SHA256 `4361d813…26af`), in this order:
1. **The parent's mandated first reads**, each COMPLETE:
   - `new-source-provenance-control-replay-and-parent-duty-correction-v59.json` (73 LF, `d62146da…763f`);
   - `Tuscan-intake-pause-privacy-cadence-and-prospective-directions-v60.json` (40 LF, `176b3cbb…bb85`).
2. **The manifest and receipt:**
   - the manifest `peer-review-wave-eighteen-v131.json` (`a42e67af…7902`): top level and my entire v131-B entry, including `post_ack_entire_scope` and all 73 source pins;
   - the receipt (58 LF, `68ee942e…374d`).
3. **All three literal parts, raw, through their endings:**
   - part1 (fddb58f4…8dd4) LF 1–916: S1–S26;
   - part2 (773ec765…2953) LF 1–1002: S27–S65;
   - part3 (cb78b99b…41f0) LF 1–607: S66–S73.

   They include the 449 author LF in full:
   - v35: 132 LF, `7365a4bee96f059ddb16f76a6ea6448f240223941230618e95146d3600f3b71c`;
   - v36: 107 LF, `4395c9ec27a1e6a7b9c49de793de92a2c3d19292c29d4052033579ff44590a65`;
   - v37: 97 LF, `5e90e14a26d9051dc8e5c1847c381568ae64694d6a0197654d5763cd4eff963d`;
   - v38: 113 LF, `620948d52ec6b81e1abbb702bc25a0267c335c5396cd00e0871b6048e3e1a79a`.

   These four pins were re-derived live with shasum (449 LF total) before this file was pinned, and match the manifest.

   They also include the author gate request S71 (19 LF), the registered-definition addendum S72 (23 LF) and the sector-union parent S73 (40 LF).

The live hashes, observed at 09:54:15 PDT, equal the release and receipt values. No part was truncated in my reads. Hash equality binds bytes, not proof; the proof assessment below is from the read bodies.

## 2. Claim class I — v35

**I-1. Petersen identities.** P is duad disjointness and B = J−I−P.
- A duad is disjoint from exactly the three duads inside its complementary 3-set. It meets the other six in one point.
- Two disjoint duads cover four of the five points, so no duad avoids both (λ = 0). Two meeting duads cover three points, so exactly one duad avoids both (μ = 1).
- Hence P² = 3I + 0·P + 1·B = 2I − P + J, and PJ = JP = 3J. This is the literal SRG(10,3,0,1) identity.
- On 1^⊥ we have J = 0, so θ² + θ − 2 = 0 and θ is 1 or −2. Multiplicities follow from m1 + m2 = 9 and 3 + m1 − 2m2 = tr P = 0, giving (5, 4).
- B has eigenvalues 10−1−3 = 6, −1−1 = −2 and −1+2 = 1. **RECONSTRUCTED.**

**I-2. Literal H and K, and unitarity.** r = (−1+i·sqrt15)/4 satisfies r·conj(r) = (1+15)/16 = 1.
- H = I+iP−iB and K = I+rP+conj(r)B are polynomials in P, since J = P²+P−2I. They are therefore commuting normal matrices.
- The eigenvalues at P = 3, 1, −2 are as printed: 1−3i, 1+3i, 1−3i for H, and (−5−3i·sqrt15)/4, (5+3i·sqrt15)/4, (5−3i·sqrt15)/4 for K. I re-derived each, for example 1+3r+6·conj(r) = (4−3−6+(3−6)i·sqrt15)/4.
- Each has squared modulus 1+9 = 10 or (25+135)/16 = 10. So HH^† = KK^† = 10I.
- Since r^−1 = conj(r) and i^−1 = −i, we get K_(as) = r^ε_a(s) and H_(bs) = i^ε_b(s). **RECONSTRUCTED.**

**I-3. Row and column ONBs.**
- Row a is diag(K_a) applied to the rows of conj(H)/sqrt10. Column b is diag(conj(H_b)) applied to the rows of K/sqrt10.
- These are unitary diagonals times orthonormal systems. **RECONSTRUCTED** (the actual ONB condition, not a count).

**I-4. r is not a root of unity.**
- r² = (−7−i·sqrt15)/8, so 2r²+r+2 = 0. Also r + r^−1 = 2Re r = −1/2.
- If r were a root of unity, r and r^−1 would be algebraic integers, and so would their rational sum. That sum would then be an integer. Contradiction.
- Consequently r^m = i^n with m ≠ 0 is impossible. **RECONSTRUCTED.**

**I-5. All 100 rays are distinct.** All entries are nonzero, so coordinate ratios remove λ.
- I-4 forces ε_a − ε_c to be constant. If a ≠ c, its values at s = a and s = c are −h and +h, with h = ε_a(c) = ε_c(a) = ±1 (the relation is symmetric). So a = c.
- Then conj(H_b) and conj(H_d) are proportional orthogonal nonzero vectors unless b = d. **RECONSTRUCTED.**

**I-6. No transversal through any diagonal cell (a,a).** For c ≠ a and d ≠ a, 10·⟨q_aa, q_cd⟩ = Σ_s r^Δ_s · i^(ε_a(s)−ε_d(s)), with Δ_s = ε_c(s) − ε_a(s).
- The i-exponent is even off {a,d}. It is −h at s = a, giving −hi, and +h at s = d, giving +hi, where h = ε_a(d).
- So the sum is R(r) + hi[r^Δ_d − r^Δ_a], with R(r) ∈ Z[r, r^−1] ⊂ F = Q(r) = Q(sqrt(−15)).
- i ∉ F, because Q(i) = Q(sqrt(−15)) would need (−1)/(−15) = 1/15 to be a rational square. So 1 and i are F-independent. Vanishing forces r^Δ_d = r^Δ_a, hence Δ_d = Δ_a by I-4.
- Δ_a = ε_c(a) is odd. If d = c, then Δ_d = −Δ_a. If d ∉ {a, c}, then Δ_d is a difference of two signs, which is even.
- So q_aa is orthogonal exactly to its 18 rook cells. A transversal through (a,a) needs nine cells off its row and column, all orthogonal to q_aa. Impossible. **RECONSTRUCTED**, as a decomposition in the field F(i) = F ⊕ iF (not a real/imaginary split).

**I-7. Classification of the central Hadamards.**
- The A5-stabilizer of a duad has order 6. For {1,2} it is {id, (345), (354), (12)(34), (12)(35), (12)(45)}. It is transitive on the 3 disjoint duads and on the 6 meeting duads.
- So A5 has exactly three orbitals on ordered pairs of duads. Invariant unit-entry matrices are α(I + xP + yB).
- Such an M is normal with eigenvalues 1+x−2y, 1−2x+y and 1+3x+6y, all of nonzero multiplicity. It is Hadamard iff each has squared modulus 10.
- Expanding with u = Re x, v = Re y, w = Re(x·conj(y)) gives u−2v−2w = 2 and −2u+v−2w = 2. Hence u = v and u+2w = −2.
- Equal real parts give y = x or y = conj(x). The case y = x gives w = 1 and u = −4, impossible. The case y = conj(x) gives w = Re(x²) = 2u²−1, so 4u²+u = 0 and u is 0 or −1/4.
- These give exactly (x,y) = (i,−i), (−i,i), (r,conj r), (conj r, r). The all-ones eigenvalue then has squared modulus 10 in each case (checked exactly, and also from trace MM^† = 100). **RECONSTRUCTED.**

**I-8. The two-matrix family at a common coordinate pairing.**
- K = H puts every diagonal ray at the uniform ray. K = conj(H) gives q_(a,b) = q_(b,a). Neither is maximal.
- Mixed categories are §§2–4 for all four sign choices. I re-derived the i → −i case: the i-component becomes hi[r^Δ_a − r^Δ_d], with the same vanishing condition. The r → conj(r) case has the same field and is again not a root of unity.
- The opposite order is conj(transpose), which preserves the ONB, transversal, resolution and distinctness conditions.
- Row phases and permutations rephase or relabel cells. Column phases give a common coordinate diagonal. A common column permutation gives a common coordinate permutation.
- The stated limitation, that the relative column permutation is NOT covered by v35, is correct. **RECONSTRUCTED.**

**Dependency and trust of class I.**
- Only printed identities and elementary facts are used: SRG counting, the spectral theorem for commuting normal matrices, rational algebraic integers, the identification criterion for quadratic fields, and the rank-3 orbit count.
- No catalogue or classifier is used. The positive mixed array is a literal AUTHOR-WRITTEN 100-distinct-ray QLS10, not a 1-RQLS witness. Its executable independent-checker gates were not performed.

## 3. Claim class II — v36

**II-1. Normal form.**
- Independent monomial changes on each Hadamard reduce, after one common coordinate permutation, to one arbitrary relative permutation π. Row phases are per-cell phases. Column phases give the common diagonal D2·conj(D4).
- Signs are σ, τ ∈ {±1}. Complex conjugation of the second factor is absorbed into τ. The central matrices are symmetric, so transposing a factor adds nothing.
- (MIX) and (GG) are therefore the general forms. **RECONSTRUCTED.**

**II-2. MIX rows, columns and distinctness for every π.**
- Column b is diag(i^(τε_b)) applied to the rows of the column-permuted golden Hadamard, which is still Hadamard. Row a is diag(K_(a,π(·))) applied to the conference rows.
- Distinctness: ε_a∘π − ε_c∘π must be constant over s, hence over all duads, since π is a bijection. This gives a = c and then b = d, as in I-5. **RECONSTRUCTED.**

**II-3. MIX moved bad cells (a, π^−1(a)).**
- For c ≠ a and d ≠ b = π^−1(a), the conference factor is i^(τ(ε_d(s)−ε_b(s))). It is real off {b,d}. It is τh'i at s = b and −τh'i at s = d, where h' = ε_d(b) = ε_b(d).
- So the i-component is τh'i(r^Δ_b − r^Δ_d), with Δ_s = σ[ε_c(π s) − ε_a(π s)].
- Δ_b = σε_c(a) is odd. π(d) ≠ a. Either π(d) = c, giving Δ_d = −Δ_b, or π(d) ∉ {a,c}, giving Δ_d even. So the inner product is nonzero by I-4 and I-6.
- These ten cells, one per row and one per column, lie on no transversal, so no resolution exists. Category exchange is conj(transpose) plus a common coordinate permutation. **RECONSTRUCTED.**

**II-4. GG necessary pair condition.** For cells (a,b) and (c,d) with a ≠ c and b ≠ d, 10·⟨·,·⟩ = Σ_s r^D_s, where D_s = σ[ε_c(πs) − ε_a(πs)] + τ[ε_d(s) − ε_b(s)] lies in [−4,4].
- P(x) = Σ_s x^(D_s+4) is in Z[x] with nonnegative coefficients and P(1) = 10.
- Suppose the two cells are orthogonal. Then P(r) = 0. m = 2x²+x+2 is primitive and irreducible (discriminant −15, no rational root), and is a scalar multiple of the minimal polynomial of r. So m divides P in Q[x], and by Gauss's lemma in Z[x]. Hence 3 = m(−1) divides P(−1).
- P(−1) = Σ(−1)^D_s = 10 − 2N_odd. A bracket ε_c(x) − ε_a(x) is odd iff exactly one of the two terms is 0, i.e. iff x ∈ {a,c}. So D_s is odd exactly on the symmetric difference of {π^−1 a, π^−1 c} and {b,d}, and N_odd ∈ {0,2,4}.
- Only N_odd = 2 makes P(−1) = 6 divisible by 3. So the two sets meet in exactly one point. This is necessary only; no sufficiency is claimed. **RECONSTRUCTED.**

**II-5. No permutation satisfies PERM, so there is no transversal at all.** Put T(x) = f(π(x)).
- Two fixed points violate PERM, since their intersection has size 2.
- Otherwise at least nine non-fixed points form a T-invariant set. For such an x, discard x, T(x) and T^−1(x), which leaves at least six choices of y. Then T(x) ∉ {x,y} and T(y) ∉ {x,y}, so the intersection is empty.
- This covers every permutation with no enumeration. **RECONSTRUCTED.**

**II-6. Scope.**
- All mixed and all GG independent-monomial orbit pairs are covered. The conference/conference family is correctly left OPEN in v36: its powers lie in Q(i), the field split fails, and the mod-3 lemma does not apply.
- That historical OPEN boundary is correct at its own time. It is not re-edited by v38. **RECONSTRUCTED.**

**Dependency of class II.** Class I (I-4, I-6 and the matrices), Gauss's lemma, irreducibility of m, and elementary permutation counting. There is NO golden-congruence transfer to the conference case, and none is used later.

## 4. Claim class III — v37

**III-1. Normalization — MINOR (precision; repaired).**
- A K-factor (I ± iC)Π with relabelled rows (row a' := π^−1(a)) becomes I ± iΠ^T CΠ. So D = ±Π^T CΠ has zero diagonal, and its real entry sits at s = a.
- Check: C = P−B = 2P+I−J. Using J² = 10J and PJ = 3J, C² = 4P²+4P+I−4J. With P² = 2I−P+J this is 9I. So C is a symmetric conference matrix.
- For H = I−iC, conjugating the whole array maps (I+iD, I−iC) to (I+i(−D), I+iC). This conjugation preserves every relevant property. v37 calls the step only "harmless common phases/permutations", hence the precision MINOR.
- With this explicit step, (CC) covers ALL relative pairings and BOTH signs. **RECONSTRUCTED** with that repair.

**III-2. The matched cells are real, have equal products, and are pairwise nonorthogonal.**
- q_aa(s) = D_(as)·C_(as) ∈ {±1} for s ≠ a, and 1 at s = a.
- A C-row has three +1 and six −1 off the diagonal, so its product is +1. A D-row has product +1 if D = +Π^TCΠ, and (−1)^9 = −1 if D = −Π^TCΠ. So all ten products are equal.
- Orthogonal real ±1 vectors of length 10 differ in exactly five places, which would make the product ratio (−1)^5. Hence no two matched rays are orthogonal, including when rays coincide. **RECONSTRUCTED.**

**III-3. Pigeonhole.** A resolution is ten disjoint transversals covering all 100 cells (S72 item 2). Each contains at most one matched cell and all ten must be covered, so each contains exactly one. Its permutation f therefore has exactly one fixed point a0. **RECONSTRUCTED.**

**III-4. Imaginary support.**
- For a ≠ b, the nonreal coordinates of q_(a,b) are exactly a (−iC_(ba)) and b (iD_(ab)).
- Row a0 of T is real. Column a0 is real because f(a) = a0 forces a = a0.
- Real sign changes on rows and columns make that row and column all ones, without moving imaginary positions. So the core is A+iB with disjoint supports.
- supp B = I9 + P_f, with two entries in every row and every column: column s has entries from rows s and f^−1(s) ≠ s. **RECONSTRUCTED.**

**III-5. Lower bound on the π-adic valuation** (π = 1+i).
- Subtracting the first row and expanding gives det T = det(A−J+iB).
- Entries of A−J+iB:
  - where B = 0, the entry is 0 or −2 = i·π² (since π² = 2i), i.e. divisible by π²;
  - where B = ±1, the entry is −1±i, of norm 2, i.e. exactly one factor π.
- So E = (A−J+iB)/π has entries ≡ 0 mod π (since −2/π = −1+i) or ≡ 1 mod π (the quotients are i and −1). Hence E mod π = I+P_f over F2.
- ker(I+P_f) over F2 is the cycle-constant vectors, so rank = 9−c.
- An invertible F2 row reduction producing c zero rows lifts, through elementary row operations, to a unimodular U over Z[i]. Then UE has c rows divisible by π, so v_π(det E) ≥ c and v_π(det T) ≥ 9+c. **RECONSTRUCTED.**

**III-6. Exact valuation.**
- det T·conj(det T) = det(TT^†) = 10^10.
- 2 = −iπ², π̄ is an associate of π, and 5 = (2+i)(2−i) is coprime to π. Hence 2v_π(det T) = v_π(10^10) = 2·10, so v_π(det T) = 10.
- Therefore c ≤ 1, so c = 1: f is one 9-cycle on the non-fixed points. **RECONSTRUCTED.**

**III-7. The necessary theorem** (now superseded by IV). Any resolution is an idempotent Latin square whose ten symbol permutations all have type (1)(9). As a necessary condition this is correct. Its OPEN boundary is historical and correct at its time. **RECONSTRUCTED.**

## 5. Claim class IV — v38

**IV-1. B = ±(I−R).**
- Orthogonality to the first row and column gives A1 = −1, B1 = 0, 1^T A = −1^T and 1^T B = 0 (SUMS), from the real and imaginary parts of 1 + Σ_s(A+iB)_(as) = 0 and of the column analogue.
- Rows of B carry opposite signs at (a,a) and (a,f(a)). The column f(a) has entries b_f(a) and −b_a, which must also be opposite. So b_f(a) = b_a, constant along the single cycle.
- Conjugating T maps B to −B and leaves A unchanged, giving B = I−R with R = P_f. **RECONSTRUCTED** (forced, not an ansatz).

**IV-2. Normality and commutation.**
- L = BB^T = B^TB = 2I−R−R^−1, since R^T = R^−1.
- The real parts of the core blocks of TT^† = 10I and T^†T = 10I give J + AA^T + L = 10I and J + A^TA + L = 10I. So AA^T = A^TA = 10I−J−L.
- Normality gives A(AA^T) = (AA^T)A. SUMS give AJ = JA = −J. Hence A commutes with L, and so with R+R^−1. Both the row and the column Hadamard equations are genuinely used. **RECONSTRUCTED.**

**IV-3. Circulancy.**
- Index the cycle by Z9. The eigenvalues 2cos(2πk/9) of R+R^−1 for k = 0,…,4 are distinct, since cos is strictly decreasing on [0,π]. So the eigenspaces are span(f_0) and span(f_k, f_−k).
- A commuting matrix preserves these. Writing A = Σ α_k f_k f_k^† + β_k f_−k f_k^† gives A_(ij) = u_(i−j) + v_(i+j).
- The zero diagonal is ACTUAL, since supp B ⊇ I. So u_0 + v_2i = 0 for all i. Because 2 is invertible mod 9, v is constant. Absorbing it, A is circulant, and A and A^T commute with R. **RECONSTRUCTED** (derived, not assumed).

**IV-4. Integrality contradiction.**
- The imaginary part of the core of TT^† = 10I is BA^T − AB^T = 0.
- With B^T = I−R^−1 = −R^−1 B, and A commuting with R and B: AB^T = −AR^−1B = −R^−1AB = −R^−1BA = −BR^−1A. So B(A^T + R^−1A) = 0.
- W = A^T + R^−1A is an integer matrix. ker(I−R) is the constants for a single 9-cycle, so each column of W is constant.
- Since 1^T R^−1 = 1^T, we get 1^T W = (A1)^T + 1^T A = −2·1^T. A constant column with sum −2 would have entries −2/9 ∉ Z. Contradiction. **RECONSTRUCTED.**

**IV-5. Conference theorem.** No quantum transversal passes through any matched real cell. So there is no full resolution for any conference/conference pairing, whether or not its rays are distinct. **RECONSTRUCTED.**

**Dependency of classes III–IV.**
- Gaussian-integer factorization (2 ramified, 5 split), norm multiplicativity, F2 rank, lifting of elementary operations to unimodular Z[i] operations, determinant multiplicativity, Fourier diagonalization of the cyclic shift on Z9 with the eigenvalue-distinctness argument above, and integer linear algebra.
- The v37 §3–§4 details are a genuine dependency of v38, and v38 cites them correctly.

## 6. Claim class V — composition

The categories are mixed (both orders), golden/golden and conference/conference, under all independent monomial changes, signs and relative π, plus common array unitary, conjugation and transposition. They are exhausted by I-8, II-1 and III-1.
- **Mixed:** ten untransversalizable cells (II-3).
- **GG:** no transversal (II-5).
- **CC:** ten untransversalizable cells (IV-5).

Hence no array of the family is a 1-RQLS10, under S72's actual one-resolution definition. Ten disjoint transversals must partition all 100 cells, so any untransversalizable cell, or the absence of any transversal, blocks every resolution, covariant or not. A classical-only or covariant substitute is not used. **RECONSTRUCTED.**

The headline "no maximal 1-RQLS in this family" is correct and in fact weaker than what is proved, since no resolution exists regardless of maximality. The v35 claim that same-category, same-coordinate arrays are not maximal is consistent with, and superseded by, the stronger II-5 and IV-5.

## 7. Dependency / application / trust (whole union)

**(a) Model application.** S72 items 1–2 state the needed definitions:
- QLS(v) cells are unit vectors with every row and every column an ONB;
- phase multiples count as identical, so maximal means 100 distinct rays;
- a transversal is v cells in distinct rows and columns forming an ONB;
- for t = 1, a resolution is one set of v mutually disjoint transversals partitioning the square.

Every application step uses exactly these. The registered roster requirement ("row/column/transversal ONBs") agrees.

TRUST: S72 is a parent addendum resting on SELECTED reading of Zhang–Cao (arXiv 2608.29201v2: Introduction, Definition 1.1, Lemma 2.2) and a local excerpt. Neither the source nor a book page was supplied to me. **NAMED_NOT_RECONSTRUCTED:** independent source authentication of that definition. I apply the definition exactly as S72 states it.

**(b) Imports.** No catalogue, classifier, finite search, machine certificate, v14 material (withdrawn, S39) or v15/v16 sector theory is a premise. S73 is context only. Its conclusion — that only the intrinsic {10}, {4,6} and {5,5} patterns remain necessary — is consistent with the author's statement that those branches stay open, and is not used.

**(c) Process sources.** S1–S66 are mandatory overlays and process records. None is a mathematical premise. Their permanent findings and quarantines are preserved. The ZERO-credit rule is respected: no withdrawn guidance is used here.

**(d) Ceilings.** Same-harness written reconstruction only, as at the top of this file. The finite-witness executable independent-checker, control, vendor and priority gates are NOT PERFORMED under HOLD.

## 8. Process disclosures (permanent; not mathematical counts)

1. **NEW own permanent PRIMARY-REVIEW INTAKE PAUSE PROCESS MAJOR**, bound by parent v60 (`176b3cbb…bb85`).
   - After the v131-B dispatch reached me, and while saving the primary state, I added one mathematical sentence to the then-unpinned primary packet v73 (§4, line 60) before pinning it and writing checkpoint-128.
   - That sentence and any proof guidance consuming it receive ZERO admitted credit. v73 as a whole remains UNREVIEWED.
   - This review is not a retroapproval. My ACK disclosed the event; the ACK's "primary paused from ACK" wording does not attest the receipt-to-ACK interval.
2. **Parent v59.** The parent's "latest v105-D" preceding-duty attribution is WITHDRAWN. My true preceding assignment was v102-C, returned Oct 25 (review SHA256 `33adee68…8309`).
3. **Older own findings remain**: the v102-C private-written-exactness MAJOR, cadence lapses (32:24, 59:57, 45:00, 39:33), the hash-order correction and the checkpoint045 withdrawal.
4. **Exposure.**
   - My earlier completed reviews are listed in the ACK. They include five MOQLS reviews (related quantum-Latin-square domain) and no prior review of an RQLS author body, according to my root's file names.
   - The mandatory overlays supplied general round exposure.
   - This is not a blind review and not a census of what I have seen.
5. **During this review:**
   - exact symbolic reasoning only, with no decimal, magnitude or chosen-instance probe;
   - no primary reasoning since the ACK;
   - checkpoints 128 (09:47:16) and 129 (10:02:46).

**Explicit nonclaims:** no arbitrary-Hadamard, full Type-IV, A5-WLOG, unrestricted no-go, original-witness, novelty or current-openness promotion. The original maximal 100-ray 1-RQLS10 remains UNKNOWN.
