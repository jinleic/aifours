# Proof review (f142): every odd-root Fourier-product QLS10 has no transversal

Native `/bin/date` observed immediately before creating this file: **2026-10-28T21:15:01-0700 PDT**. Reviewer: same-harness proof lane (physics-5 manifest `f142-rqls10-all-odd-fourier-product-obstruction`, manifest SHA-256 `18c99ee567c62fce537563f4fde06bebb1308b4549e5417191bfcecf7d331d02`, 3897 bytes, verified before reading).

## 1. Disposition

**FATAL 0; MAJOR 0; MINOR 3 (presentational, §7). Verdict: the written reduction is CORRECT at the exact stated scope, conditional on the two named imports below, one of which (the BH(10,5) finite base) this review independently discharged at same-harness level.**

Statement reviewed: for every odd positive integer q and every K in BH(10,q), the array `psi_(r,c)(t) = zeta10^(rt) K_(t,c)/sqrt(10)` has no orthogonal transversal (ten cells, one per physical row and column, pairwise orthogonal), including arrays with repeated rays and after arbitrary unit row/column gauges of K; hence no 1-resolution of that family in the base source's sense (every symbol class an orthogonal transversal).

Dependencies and their status:

| Dependency | Status in this review |
|---|---|
| Lam–Leung, *On vanishing sums of roots of unity*, arXiv math/9511209v1, Corollary 3.4 and Lower Bound Theorem 4.8 | **IMPORT.** Statements read directly from the arXiv v1 PDF (§3). The candidate's deductions from the statements are verified (§4). The theorems' proofs were read but not re-derived; exhaustive exact small-q controls corroborate the used consequences (§6.B–D) but do not replace the theorem for general q. |
| Irreducibility of cyclotomic polynomials (Φ_n is the minimal polynomial of ζ_n) | IMPORT (standard); used by all exact root-sum tests here. |
| BH(10,5) Fourier-product no-transversal base (`frontier-20261028-all-bh10-5-product-obstruction-v1.md`, SHA `44776a4d…`, certificate SHA `67bc6f39…`) | **Independently discharged at same-harness level** (§5): the finite certificate was regenerated and verified from scratch by this reviewer's own code, and the written normalization/physical caller was checked mathematically and on 65,520 exact instances. Not a human, kernel or independent-family discharge. |
| Prior f72 review and receipt | Read and assessed; consistent with my independent counts; **not** used as a premise. |

Nonclaims: nothing here bears on general or unrestricted QLS10, on even q (q=18 and q=10 included), on non-Fourier products, arbitrary complex Hadamard K, or BH classification; no novelty, priority, human, formal-kernel or independent-model-family verification is asserted. Same-harness review only.

## 2. Inputs read, in manifest order, with full verification before interpretation

| Input | Bytes | LF | SHA-256 (verified) |
|---|---:|---:|---|
| odd-q candidate `frontier-20261028-all-odd-fourier-product-no-transversal-v1.md` | 6254 | 54 | `d9422ffac608ddd9b128e979dc105b20c6ca94ad06f4a63af4e086a42e6e9490` |
| BH5 base `frontier-20261028-all-bh10-5-product-obstruction-v1.md` | 11149 | 105 | `44776a4da92b9b50cc9b8710bdd7b7dc7b2119dbb7c3beebf4aa909969885678` |
| certificate `frontier-20261028-bh10-structural-cert-v1.json` | 612365 | 1 | `67bc6f39a6d2bbd6a3c181dc4a7e5baaa7e5406b4ad8a50eb997b44e41197eb2` |
| f72 `review-v1.md` | 11197 | 75 | `1fb094152763cf0785f08b80affa5c9ad24fa1ffb2c3e3940b8f6250477757e3` |
| f72 `receipt-v1.json` | 5612 | 222 | `e131fa267ed4edf0992064dc8d493923a1e8a1d217f82a29a37d38175123a011` |

All five text inputs were read completely (`:raw` full-range reads). The certificate (one 612,365-byte line) was fully UTF-8 decoded and strictly parsed with duplicate-key rejection; all 16,064 records were examined (§5). No author code was read, imported or executed; the two `.py`/`.cpp` producers and checkers named in the base source were not opened. The manifest names no PDF input; the only PDF is the primary source fetched below. During this review a parallel finite lane created `finite-*` files in the same directory; they are not declared inputs of this manifest and were **not** read.

## 3. Primary source: direct read of Lam–Leung arXiv math/9511209v1

Fetched `https://arxiv.org/pdf/math/9511209v1` to `proof-lam-leung-math9511209v1.pdf` (201,910 bytes, 18 pages, SHA-256 `b010546db8230a39741997807a1110402c4f24fb7e897441e66fc355284ce1ab`). Page 1 was rasterized (`proof-lam-leung-page1-01.png`, SHA `7c084694…`) and inspected visually: title "ON VANISHING SUMS OF ROOTS OF UNITY", T. Y. Lam and K. H. Leung, stamp "arXiv:math/9511209v1 [math.NT] 13 Nov 1995", abstract "…(with repetitions allowed) adding up to zero…". Text extracted with `pdftotext -layout` to `proof-lam-leung-math9511209v1.txt` (SHA `108179193e…`); line numbers below refer to that file.

Verbatim statements (modulo extraction typography):

* **Corollary 3.4** (p. 8, lines 326–328): "Let m = p^a q^b, where p, q are primes. Then, up to a rotation, the only minimal vanishing sums of m th roots of unity are: 1 + ζ_p + ··· + ζ_p^{p−1} = 0, and 1 + ζ_q + ··· + ζ_q^{q−1} = 0." It is stated as "a direct consequence of (3.3)(2)".
* **Lower Bound Theorem 4.8** (p. 11, lines 458–461): "Let G be a cyclic group of order m = p_1^{a_1} ··· p_r^{a_r}, where p_1 < ··· < p_r are primes, and let ZG → Z[ζ] be the usual map, where ζ = ζ_m. For any minimal element x ∈ NG ∩ ker(φ), we have either (A) x is symmetric, or (B) r ≥ 3 and ε(x) ≥ ε_0(x) ≥ p_1(p_2 − 1) + p_3 − p_2 > p_3."
* Definitions used (Intro lines 72–82, 138–142; §4 lines 331–340): elements of NG ∩ ker φ are exactly vanishing sums of m-th roots **with repetitions allowed**; ε(x) is the weight (number of terms with multiplicity), ε_0(x) the support size; x is minimal iff it is not a sum of two nonzero elements of NG ∩ ker φ (equivalently no proper subsum vanishes, line 112); the symmetric minimal elements are exactly g·σ(P_i), i.e. a rotated full set of p_i-th roots, of weight exactly p_i (lines 335–338); "In the case r ≤ 2, (3.3) implies that all minimal elements … are symmetric" (line 342), restated at the start of the proof of 4.8 (lines 464–465).

The candidate cites exactly these two results and uses them only through the consequences checked in §4.1. Theorem numbering in the candidate matches the arXiv v1 numbering. The proofs of 3.3, 4.1 and 4.8 were read; they are coherent but are **not** independently re-derived here and remain an import.

## 4. Step-by-step verdicts on the written reduction

### 4.1 §2 root-sum facts — CORRECT (given the import)

1. *Decomposition.* Any nonzero x ∈ NG ∩ ker φ is a finite sum of minimal elements (descent on ε(x); the source uses this itself, line 529). A vanishing sum of at most 10 odd-q roots therefore splits into minimal vanishing sums of weight ≤ 10.
2. *Minimal pieces are regular odd-prime polygons.* For odd q every prime factor is odd, so in Theorem 4.8 p_1 ≥ 3, p_2 ≥ 5, p_3 ≥ 7 and the (B) bound p_1(p_2−1)+p_3−p_2 = p_1p_2 − p_1 − p_2 + p_3 is increasing in each p_i; its minimum over odd triples is 3·4+7−5 = **14** > 10. Hence every minimal piece of weight ≤ 10 is symmetric: a rotated regular p-gon (p an odd prime dividing q, all p roots distinct), of weight exactly p. For r ≤ 2 the same follows from Cor. 3.4 / Thm 4.8(A). The candidate's "asymmetric minimal weight is at least 14 when q has at least three odd prime factors, and with at most two factors all minimal sums are symmetric" is exactly this.
3. *Five terms.* 5 as a sum of odd primes dividing q is only 5 = 5; so a five-term zero sum is one regular pentagon (five **distinct** roots, a coset of μ_5), and exists only if 5 | q. Multiplicities cannot occur. CORRECT.
4. *Ten terms.* 10 as a sum of odd primes is only 5+5 or 3+7 (3+3+… and 2+… are impossible). CORRECT, including repetitions (5+5 may be the same coset twice).
5. *LOW/HIGH in G = μ_q/μ_5.* A pentagon maps to a single G-value, so 5+5 gives one value ×10 or two values ×5 (same coset ⇔ same G-value). For 3+7: μ_3 and μ_7 inject into G (orders coprime to 5), the images of the two cosets are cosets of subgroups of coprime orders 3 and 7 and meet in at most one point, giving ≥ 3+7−1 = 9 distinct G-values. CORRECT; the control §6.D finds exactly 9 in all 525 cases at q = 105.

### 4.2 §3 opposite-row pairing and the two uniform halves — CORRECT

* *Pairing.* A transversal {(r, c(r))} with c a permutation contains both r and r+5 for r = 0..4; the five pairs {c(r), c(r+5)} partition the ten K-columns. With ζ_10^{5t} = (−1)^t, `10⟨ψ_(r,c), ψ_(r+5,d)⟩ = S_E(c,d) − S_O(c,d)` and column orthogonality gives S_E + S_O = 0, hence S_E = S_O = 0 with E = even coordinates, O = odd. Verified by hand and exactly in Z[ζ_30] on 500 instances (§6.H).
* *Same G-value on matched pairs.* S_E(c,d) = Σ_{t∈E} K_(t,d)/K_(t,c) is a five-term zero sum of q-th roots, hence a pentagon by 4.1(3), so all five ratios share one G-value g_E(c,d); likewise on O. Then for s, t ∈ E: [K_(s,c)/K_(t,c)] = [K_(s,d)/K_(t,d)] because [K_(s,d)/K_(s,c)] = [K_(t,d)/K_(t,c)] (G abelian). CORRECT.
* *Row quotient parity.* The ten G-values of the row quotient (s over t), s,t ∈ E, are constant on each of the five matched pairs, so each value has even multiplicity and at most five values occur. Rows s, t of K are orthogonal, so Σ_c K_(s,c)/K_(t,c) = 0 is a ten-term zero sum, hence LOW or HIGH by 4.1(5). HIGH needs ≥ 9 values; nonconstant LOW has multiplicities 5, 5 (odd). Therefore the G-row quotient is constant. Same for O. CORRECT. Control §6.F: the orthogonal pair of μ_15 rows with profile (5,5) admits **0 of 945** column pairings with equal G-values in every pair; the profile-(10) pair admits all 945.
* *Dephasing.* Multiplying row s ∈ E by a q-th-root representative of γ_{s,t_0}^{-1} makes all E rows equal in G; similarly for O; column phases by representatives of [K_(t_0,c)]^{-1} make E identically 1 in G, leaving one pattern (δ_c) on O. Row/column phases are diagonal unitaries D_1, D_2 with q-th-root entries: K' = D_1 K D_2 ∈ BH(10,q), ψ' = (D_2)_c · D_1 ψ, so transversal orthogonality and the transversal cells are preserved. CORRECT. Control §6.G runs this procedure exactly (q = 15) and recovers an exact BH(10,5).

### 4.3 §4 tight-frame parity and collapse to BH(10,5) — CORRECT

* *Cross-group half-sums vanish.* For columns c, d with δ_c ≠ δ_d the ten quotient terms have G-value 1 on E and δ_dδ_c^{-1} ≠ 1 on O, five each; two distinct values exclude HIGH, so the zero column sum is 5+5 with the two pentagons in distinct G-cosets, which forces one pentagon to be exactly the E-terms and the other the O-terms. Hence Σ_{t∈E} conj(K_(t,c))K_(t,d) = 0: the column spaces col(A_i) ⊂ C^5 of the E-row blocks are pairwise orthogonal. CORRECT.
* *Tight frame.* K_E K_E^† = Σ_i A_iA_i^† = 10 I_5 by full-row orthogonality (each A_iA_i^† has range in col(A_i) and kills its orthogonal complement; applying the sum to v ∈ col(A_j) gives A_jA_j^† v = 10v). So A_iA_i^† = 10 P_i and taking traces 5m_i = 10 rank(A_i): every group size m_i is even and ≥ 2, so at most five groups. CORRECT. Controls §6: the doubled Fourier-5 frame (tight) has component sizes [2,2,2,2,2]; the non-tight (3,2,2,2,1) column arrangement shows odd groups once tightness is dropped; all 3,276 E-halves of 13 exact BH(10,5) matrices had only even (in fact single, size-10) components.
* *E row versus O row.* Its G-profile consists of the values δ_i with even multiplicities m_i and ≤ 5 values; not HIGH, not the (5,5) LOW profile, hence constant: all δ_c equal. One more O-row phase puts every entry in μ_5. CORRECT. (The LOW/HIGH dichotomy is again 4.1(5); control §6.E shows a q = 30 ten-term zero sum with the all-even nonconstant profile {4,2,2,2}, so this step genuinely needs odd q.)

### 4.4 Physical caller — CORRECT

The transversal T of the K-array is a transversal of the K'-array for the gauge-equivalent K' ∈ BH(10,5) (cell set unchanged; inner products scale by unit phases — verified exactly on all 4,950 cell pairs at q = 15, §6.H, and the orthogonality graph is gauge-invariant). The base theorem is universal over all K' ∈ BH(10,5) with E the actual even coordinates, so K row/column permutations need no separate treatment. Arbitrary (non-root) unit gauges of K, a common unitary, cell phases and physical row/column relabelings preserve transversal orthogonality. Contradiction; hence no transversal and no 1-resolution. For 5 ∤ q the contradiction already occurs at 4.2 (no five-term zero sum exists). The quantifier "even if rays repeat" is harmless: a cell cannot be orthogonal to a repeated copy of itself, so repeats only shrink the set of possible transversals.

## 5. BH(10,5) base: independent same-harness discharge

`proof-replay-bh5-v1.py` (SHA `fed5e945dc0c28f90b45f037a2cfbdd2c49bf5ec4dc85e77cc9938219fab05a4`, standard library only, written from the theorem text and this reviewer's own mathematics) ran under Python 3.14.3 from **2026-10-28T21:07:13-0700** to the receipt clock **2026-10-28T21:07:19-0700**, producing `proof-replay-bh5-receipt-v1.json` (SHA `378194f41b28cc673aa33ec538af6c609129d8debec6d1cfa3943ae0fc8c0fe2`, exclusive creation). It established exactly:

* Exact fifth-root criterion by Φ_5 division over all 126 five-multisets and 1001 ten-multisets of Z_5: zero iff each residue once/twice.
* Regeneration: 22,680 balanced tails; **1,075** candidates (lexicographic); **26,715** compatibility edges; **53,065** triangles; **16,064** with ≥ 5 common neighbours — the certificate's triple set equals this set exactly, each triple once, no duplicate JSON keys, record keys only {triple, isolated} or {triple, odd_component}.
* Every witness checked against a freshly built Γ_E: 16,000 isolated columns (histogram 12,800 one-isolate, 3,200 two-isolate, 64 none) and 64 odd cuts, all of size 5, none with a crossing edge; in addition an independent perfect-matching search rejected all 16,064 graphs. Matching routine controls: 10-cycle accepted, star and odd component rejected.
* Index binding: my candidate list at the f72 sample indices [57,208,429,512,621,723,882,1074] reproduces that receipt's exponent rows (used as data only); my own 8-clique search returned the same clique first and 12 cliques in total, all verified exact BH(10,5) (45 row and 45 column pairs).
* Normalization/caller: for 13 matrices × 252 halves × 20 ordered (p,q) × pivot 0 = **65,520** normalizations, the normalized triple is eligible and the relabeled Γ_E equals the certified graph; none of the 3,276 halves has a perfect matching.
* Exact Z[ζ_10] physical control on four arrays: 3,600 basis orthogonality checks, 1,800 opposite-row identity checks (⟨ψ_(r,c),ψ_(r+5,d)⟩ = 0 ⇔ S_E = 0 ⇔ S_O = 0), and a brute-force transversal search over all row-by-row column choices found **none**, while a planted-transversal control array was found (diagonal).

Mathematically, the reduction in the base's §2–3 (pairing ⇒ perfect matching of Γ_E; WLOG dephasing of a first row and pivot column with the second row in canonical form; Γ_E invariant under row phases, column phases and column relabeling; the five outside rows are five distinct common neighbours, so the ≥ 5-neighbour filter yields a superset) was re-derived by me and holds. Base status: **independently discharged at same-harness level**; it remains computer-assisted, not kernel-checked or human-reviewed.

## 6. Exact controls for the odd-q steps (receipt `proof-oddq-controls-receipt-v3.json`, SHA `0be8e5d3a8aa83832b05ba353fa30e4829a57697ccbb976bf28974b6a28d00df`)

Script `proof-oddq-controls-v3.py` (SHA `356933c8b689947411e2ff313d6c68caccc14920fe01e98effd3b02b948cbc5f`; numpy 2.4.3 + standard library), run **2026-10-28T21:10:45-0700 → 21:10:49-0700**, exclusive-creation receipt. Two earlier attempts stopped on reviewer-side errors and wrote no receipt: `v1` (SHA `f7ba3d9a…`) expected a non-pentagon five-term zero sum at q = 10, which does not exist (5 = 2+3 needs 3 | q — the correct expectation is itself consistent with Cor. 3.4); `v2` (SHA `edd5872e…`) cancelled a G-value g ∈ Z_3 with exponent 5g instead of a residue-g representative (10g). Both files are retained; v3 differs only in those two expectations/representatives and the receipt name.

* **B. Five-term, complete.** For q ∈ {3,5,7,9,15,21,25,35,45,63,75,105}, every multiset of five q-th roots containing 1 (WLOG by rotation; 5,359,095 multisets at q = 105) was tested numerically then every hit confirmed exactly by Φ_q division: exactly one zero sum (the regular pentagon) when 5 | q, none otherwise; smallest nonzero |sum| ≥ 1.76·10^{-3} ≫ the 10^{-7} prefilter. Even-q countercontrol: q = 30 has 25 such zero sums, not all pentagons (e.g. 1 + (−1) + 1 + ω + ω² with four distinct G-values); q = 10 has only the pentagon, as Cor. 3.4 predicts.
* **C. Ten-term, complete and exact (meet-in-the-middle on exact Z[ζ_q] coordinates).** q = 15: 6 zero ten-multisets, all 5+5, profiles (10)×3, (5,5)×3; q = 21: 21, all 3+7; q = 35: 28, all 5+5, (10)×7, (5,5)×21; q = 45 (1,906,884 five-multisets): 45, all 5+5, (10)×9, (5,5)×36. No unclassified zero sums, no profile outside LOW, matching the theoretical coset counts C(q/5+1, 2) and 7·3.
* **D. q = 105 constructive.** All 231 5+5 sums are exact zeros with profile (10) or (5,5); all 525 3+7 sums are exact zeros with exactly 9 distinct G-values (profile (2,1^8)). The exhaustive ten-term enumeration at q = 105 was **not** performed (≈1.2·10^8 five-multisets); that there are no other ten-term zero sums at q = 105 rests on the import.
* **E. Even-q countercontrols (exact).** q = 30: {0,15,0,10,20} vanishes and is not a pentagon; {0,10,20,6,16,26,0,15,6,21} vanishes with G-profile {4,2,2,2} — all even, four values, nonconstant — so the "even multiplicities ⇒ constant" steps of §3/§4 fail at even q; q = 10: five antipodal pairs vanish and are neither 5+5 nor 3+7.
* **F. Pairing lemma at q = 15.** Orthogonal rows 0^{10} and (0,3,6,9,12,1,4,7,10,13) (profile (5,5)): 0 of 945 pairings have equal G-values in every pair; with (0,3,6,9,12)×2 (profile (10)): 945 of 945.
* **G. Dephasing.** A verified BH(10,5) sample with pseudo-random 15th-root row and column gauges (seed 20261028) is Hadamard in Z[ζ_15]; the §3/§4 procedure (row phases, column phases, final O-row phase) yields a matrix with all entries in μ_5 that is an exact BH(10,5).
* **H. Physical caller in Z[ζ_30].** For that gauged q = 15 matrix: 900 basis orthogonality checks; **500** exact opposite-row identities `10⟨ψ_(r,c),ψ_(r+5,d)⟩ = S_E − S_O`; **4,950** exact gauge-covariance identities N' = ζ_15^{κ_d−κ_c} N (row phases cancel); the orthogonality graph (1,110 orthogonal cell pairs) is identical to the ungauged array's; exact transversal search: none.

## 7. MINOR items (no effect on correctness)

1. §2 should state the two elementary facts it silently uses: that any vanishing sum decomposes into minimal ones, and that a symmetric minimal element has weight exactly p_i; Cor. 3.4 is subsumed by Thm 4.8(A) for r ≤ 2, so citing both is redundant but harmless.
2. §1's "arbitrary K row/column … permutations" covers K row permutations only through universality over BH(10,q) (a K row permutation is a different array, not a symmetry of one array); §4 says this correctly, §1 could say it explicitly.
3. "1-resolution" is used without definition; it is inherited from the base source (each symbol class an orthogonal transversal).

## 8. Exact scope of this verdict

Proven, conditional on the imports in §1: no orthogonal transversal, hence no 1-resolution, for every Fourier10 × BH(10,q) array with q odd, under all unit gauges/permutations of K and physical symmetries. Not proven and not claimed: that odd-q BH(10,q) matrices are BH(10,5)-equivalent in general; anything for even q (q = 18 and q = 10 remain open as wholes); non-Fourier products; arbitrary complex Hadamard K; unrestricted QLS10. The Lam–Leung theorems are published results read here only in their arXiv v1 statements; the small-q exhaustive controls corroborate but do not replace them. The BH(10,5) base is discharged only as an exact same-harness computation plus written argument. This review is same-harness and is not human, independent-model-family, formal-kernel or novelty verification.

Artifacts written (all `proof-*`, this directory): `proof-lam-leung-math9511209v1.pdf` (`b010546d…`), `proof-lam-leung-math9511209v1.txt` (`10817919…`), `proof-lam-leung-page1-01.png` (`7c084694…`), `proof-replay-bh5-v1.py`, `proof-replay-bh5-receipt-v1.json`, `proof-oddq-controls-v1.py`, `proof-oddq-controls-v2.py`, `proof-oddq-controls-v3.py`, `proof-oddq-controls-receipt-v3.json`, and this file. No shared input, the manifest, or any `finite-*` file was modified.
