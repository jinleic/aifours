# Review v1 — f168-werner-stratified-source-independent-v2

- Reviewer: ReviewF168WernerV2 (same-harness task agent).
- Manifest: `manifest-v1.json`, SHA-256 `9edf4483e76b21c59c24e796ffef67b4e43a629c733b4e3b11250dddb2a71e7b` (verified before reading anything else).
- Written after native clock `Thu Oct 29 07:43:37 PDT 2026` (`/bin/date` run immediately before this write).
- Candidate: `frontier-20261029-d4-q3-stratified-source-independent-frontier-v2.md` (PhysicsResearch96h-2 / physics-1).

**Nature of this review.** This is a same-harness written review backed by exact and high-precision controls that I wrote. It is **not** a human review. It is **not** an independent-model-family review. It is **not** a formal or kernel (Lean) check. It is **not** a novelty or literature check. I did not use the author's "PASS" statements as evidence. This review makes no claim about the truth of T_2, Z_2, Z_3 or T_3.

**Bottom line.** Counts are FATAL 0 / MAJOR 0 / MINOR 5, plus one coverage bullet marked INCONCLUSIVE because it depends on a packet outside the frozen inputs. Every reformulation in scope reconstructs independently and passes exact controls:

- the Ky-Fan dual and identity (1);
- the support ladder;
- the range-wise dual;
- the spread bound;
- the contraction identities (5) and (6);
- the strictly positive open families.

The five MINOR items are precision and wording fixes. The most important is in the §6 coverage wording.

---

## 1. Inputs, read order and integrity

| # | file | role | SHA-256 | bytes | LF | status |
|---|---|---|---|---|---|---|
| 0 | `manifest-v1.json` | manifest | `9edf4483…71e7b` | 2787 | – | verified; read first |
| 1 | `…/werner3-ququart/frontier-20261029-d4-q3-stratified-source-independent-frontier-v2.md` | v2 candidate | `bf50bfbf3d0f4d24ec6a9e5fc55b19ced5cd2acdb223bbb1518fe6ebf4177329` | 13054 | 153 | verified; read completely in a single exact raw read |
| 2 | `…/werner3-ququart/frontier-20261029-d4-stratified-v2-exact-check-addendum-1.json` | author exact-check addendum (read/hash only) | `3627abce4a79020b33138e78393d179167045341e2a8e59cddaffe841417a591` | 1564 | 15 | verified; read completely; parsed in full by my own code |

On input 2: my parser found 13 keys, all string-valued, and its `packet_sha256` equals the hash of input 1.

- **Errata and overlays.** The manifest declares no errata, overlays or withdrawals, and I read none.
- **Hash-only checks.** The addendum declares an author script `frontier-20261029-d4-one-leg-contraction-identity-exact-check-v1.py` (`5582c79d…7488`) and a result file `…-results-v1.json` (`0ceef09e…1b88`). Both hashes match the addendum. I did not open either file and did not execute the script.
- **Not read (outside the frozen inputs).** The candidate cites four earlier packets by SHA:
  - the v1 packet it supersedes (`319e0316…`);
  - the positive-map addendum (`8cd42f79…`);
  - the consolidated local-support packet (`0ccc096a…`);
  - the dense-boundary lemma (`4e6fe204…`).

  I did not review any claim that rests only on those packets (see S21e).

## 2. Definitions as reconstructed

Throughout, d ≥ 2, the sites are 1..n, and the target is d = 4, n = 3.

**Operators and the functional.**
- H_n = (C^d)^{⊗n}, and C is any complex operator on H_n.
- Tr_S is the unnormalised partial trace over the sites in S.
- q_n(C) = Σ_{S⊆[n]} (−1/2)^{|S|} ‖Tr_S C‖²_HS, with q_0(c) = |c|².

**Vectorisation and K_i.**
- vec C = Σ C_xy |x⟩⊗|y⟩, regrouped by site, so that site i carries the pair (row index x_i, column index y_i).
- Ω_i = Σ_j |j⟩|j⟩ = vec(I_d) at site i, and K_i = I − |Ω_i⟩⟨Ω_i|/2.

**The odd sector at d = 4.**
- ‖Ω_i‖² = 4, so P_i = |Ω_i⟩⟨Ω_i|/4 is a rank-one projection. In operator language, P_i is Y ↦ I_i ⊗ Tr_i(Y)/4, the identity component at site i; I − P_i is the traceless component.
- K_i = I − 2P_i.
- Π_∓ = Σ_{T odd / T even} ⊗_{i∈T} P_i ⊗_{i∉T} (I − P_i).
- W_odd = vec⁻¹(ran Π_−) = span{I_T ⊗ Y_T : |T| odd, Y_T ∈ ⊗_{i∉T} sl_4}. Here Y_T has vanishing partial trace at every site outside T.
- P_odd is the Hilbert–Schmidt orthogonal projection onto W_odd.

**Legs.**
- The output leg at site i is the smallest E ⊂ C^d with (P_E)_i C = C. Equivalently, it is the support of Tr_{[n]∖{i}}(CC†).
- The input leg at site i is the output leg of C†, i.e. the support of Tr_{[n]∖{i}}(C†C).
- A leg is k-supported if its dimension is ≤ k.

**Target statements.**
- T_n: q_n ≥ 0 on every C of rank ≤ 2, at fixed d.
- Z_n: q_n ≥ 0 on every C of rank ≤ 2 whose 2n legs all have dimension ≥ 3. This is the zero-leg class: no leg is 2-supported.

**Range quantities.**
- F is a two-dimensional subspace of H_n with projection P_F.
- κ(F) = sup_{0≠X∈W_odd} ‖X P_F‖²/‖X‖².
- s(F) = Σ_{|T| odd} 4^{−|T|} ‖Tr_T P_F‖_∞, where Tr_{[n]} P_F = 2.

**Contractions.** ⟨α|C|β⟩_i = (⟨α|_i ⊗ I) C (|β⟩_i ⊗ I), an operator on H_{n−1}.

## 3. Verdict per statement

Sxx are statement labels used only in this review. The packet's own labels (§n, Theorem k, Corollary k) appear in the second column.

| ID | packet statement | verdict |
|---|---|---|
| S1 | §1: T_0 is trivial; T_1 holds for every d | WRITTEN_SUPPORTED |
| S2 | §2: q_n(C) = ⟨vec C, (⊗K_i) vec C⟩ (every d) | WRITTEN_SUPPORTED |
| S3 | §2: identity (1); the sector description of W_odd; sector orthogonality; sector norms; dim W_odd = 30 (n=2) and 676 (n=3) | WRITTEN_SUPPORTED |
| S4 | Theorem 1 (vector dual) and its explicit n=2 and n=3 forms | WRITTEN_SUPPORTED |
| S5 | §2 "Two-sided use": a negative certificate from a Ky-Fan violator, and the zero characterisation under T_n | MINOR (m2) |
| S6 | §2 single-sector instances; equality iff Z has rank 1 | WRITTEN_SUPPORTED |
| S7 | Theorem 2 (range-wise dual), including bound (2) for both ran C† ⊂ F and ran C ⊂ F, and the converse | WRITTEN_SUPPORTED |
| S8 | κ(F) is invariant under local unitaries | WRITTEN_SUPPORTED |
| S9 | Theorem 3 (spread criterion) (3)/(4) and the explicit constants for n=2 and n=3 | WRITTEN_SUPPORTED |
| S10 | Maximally correlated families: every F ⊂ D_2 gives q_2 ≥ (1 − max w)‖C‖²; F ⊂ D_3 gives q_3 ≥ (15/16 − (3/2) max w)‖C‖², strict when max w < 5/8 | WRITTEN_SUPPORTED |
| S11 | Strict positivity on nonempty open subsets of the zero-leg classes Z_2 and Z_3 | MINOR (m4) |
| S12 | Lemma 4 (factorisation); q_1(\|u⟩⟨u\|) = 1/2 | WRITTEN_SUPPORTED |
| S13 | Lemma 5: identities (5) and (6) for every d; contraction preserves rank ≤ 2 and the leg inclusions at other sites | WRITTEN_SUPPORTED |
| S14 | Theorem 6 (ladder): (a) ⟺ (b) ⟺ (c); for s = n, (a) holds at every rank | WRITTEN_SUPPORTED |
| S15 | Corollary 1: T_n ⇒ T_m for m ≤ n; in particular T_3 ⇒ T_2 at d=4 | WRITTEN_SUPPORTED |
| S16 | Corollary 2: at d=4, n=3, positivity on the one-leg stratum ⟺ T_2 | WRITTEN_SUPPORTED |
| S17 | Corollary 3: 2-supported legs at n−1 distinct sites ⇒ q_n ≥ 0 at rank ≤ 2; legs at all n sites ⇒ q_n ≥ 0 at any rank | WRITTEN_SUPPORTED |
| S18 | Corollary 4: T_n ⟺ T_{n−1} ∧ Z_n, hence T_n ⟺ Z_2 ∧ … ∧ Z_n, and T_3 ⟺ Z_2 ∧ Z_3 at d=4 | WRITTEN_SUPPORTED |
| S19 | Corollary 5: zero characterisation through the iterated contractions | MINOR (m3) |
| S20 | Corollary 6: transfer of sufficient criteria through the contractions | WRITTEN_SUPPORTED (editorial note E1) |
| S21a | §6 coverage bullet "rank≤1" | MINOR (m2) |
| S21b | §6 coverage bullet "two distinct 2-supported legs" | MINOR (m1) |
| S21c | §6 coverage bullet "a 2-supported leg at all three sites, any rank" | WRITTEN_SUPPORTED |
| S21d | §6 coverage bullet "λ_1+λ_2+λ_3 ≤ 15/8 with margin (4); includes open subsets of Z_3" | WRITTEN_SUPPORTED |
| S21e | §6 coverage bullet "families in the earlier consolidated packet" | INCONCLUSIVE (outside the frozen inputs; not reviewed) |
| S21f | §6 n=2 coverage with μ_1+μ_2 ≤ 2, including every range inside D_2 | WRITTEN_SUPPORTED |
| S22 | §6 description of "the remainder" | MINOR (m1, m5) |
| S23 | §6 tracelessness remark (A=\|0⟩⟨0\|, B=2\|0⟩⟨0\| gives 13 > 12) | WRITTEN_SUPPORTED |
| S24 | §7 provenance and nonclaims (no source premise, no source-conditional bound, no target value) | WRITTEN_SUPPORTED: I found no source-conditional step in any proof |

## 4. Independent reconstruction of the load-bearing steps

**R1 (S2).** (⟨Ω_i| ⊗ I) vec C = vec(Tr_i C). Expanding ⊗_i (I − |Ω_i⟩⟨Ω_i|/2) over subsets therefore gives ⟨vec C, ⊗K vec C⟩ = Σ_S (−1/2)^{|S|} ‖Tr_S C‖² = q_n(C). This holds for every d.

**R2 (S3).** At d = 4, ⊗_i (I − 2P_i) = Σ_T (−1)^{|T|} ⊗_T P ⊗_{T^c} (I − P) = Π_+ − Π_− = I − 2Π_−. This gives identity (1).

- Sectors with different T are images of mutually orthogonal projections, so they are orthogonal.
- ‖I_T ⊗ Y‖² = 4^{|T|} ‖Y‖².
- Tr K_i = 16 − 2 = 14. Hence dim W_odd = Tr Π_− = (16^n − 14^n)/2, which equals 30 for n = 2 and 676 for n = 3. This agrees with Σ_{|T| odd} 15^{n−|T|}.
- The identity is specific to ‖Ω‖² = 4. At d = 3, K_i is not a reflection and (1) fails (negative control N1).

**R3 (S4).** By (1), T_n holds iff sup ‖P_odd C‖² ≤ 1/2 over unit C of rank ≤ 2.

- ‖P_odd C‖ = sup over unit X ∈ W_odd of |⟨X,C⟩|.
- For fixed X, sup over unit C of rank ≤ 2 of |⟨X,C⟩| is (σ_1² + σ_2²)^{1/2}. The upper bound is the von Neumann trace inequality followed by Cauchy–Schwarz; the value is attained at X_(2)/‖X_(2)‖.
- Exchanging the two suprema gives Theorem 1.
- The explicit forms follow from ‖A⊗I + I⊗B‖² = 4(‖A‖² + ‖B‖²) and ‖X‖² = 64|c|² + 4Σ‖Y_jk‖². Both identities need tracelessness, through sector orthogonality.

**R4 (S7, S8). An alternative derivation that I used as a check.** Define the right-multiplication map R_F(X) = X P_F.

1. R_F is a Hilbert–Schmidt-orthogonal projection on operator space.
2. ran R_F = {C : C = C P_F} is a 2dⁿ-dimensional linear space whose elements all have rank ≤ 2. Every C of rank ≤ 2 lies in such a space.
3. By (1), min over unit C in ran R_F of q_n(C) = 1 − 2‖P_odd R_F‖² = 1 − 2‖R_F P_odd‖² = 1 − 2κ(F).
4. So κ(F) = (1 − λ_min(q_n restricted to ran R_F))/2. This single formula gives (2), the equivalence, and the converse.
5. The orientation ran C ⊂ F follows from q_n(C†) = q_n(C), since Tr_S(C†) = (Tr_S C)†.
6. For local unitaries U, the map X ↦ U†XU preserves W_odd and the HS norm, so κ is invariant.

My controls compute κ both from the definition and through this formula; the two values agree.

**R5 (S9).** For a single sector, ‖(I_T ⊗ Y_T) P_F‖² = Tr[Y_T† Y_T · Tr_T P_F] ≤ ‖Tr_T P_F‖_∞ ‖Y_T‖². The triangle inequality and Cauchy–Schwarz with weights 4^{∓|T|/2}, together with ‖X‖² = Σ_T 4^{|T|} ‖Y_T‖², give κ ≤ s. The constants follow:

- n = 2: 1 − 2s = 1 − (μ_1 + μ_2)/2.
- n = 3: 1 − 2s = 15/16 − (λ_1 + λ_2 + λ_3)/2.

**R6 (S10).** For F spanned by f_r = Σ_j α_rj |j…j⟩, every reduction with |T| = 1 equals Σ_j w_j |j…j⟩⟨j…j|, where w_j = ⟨j…j|P_F|j…j⟩ ≤ 1. Hence:

- n = 2: s = (max w)/2.
- n = 3: s = 3(max w)/4 + 1/32.

At the uniform point w ≡ 1/2, the exact minima are:

| n | true min q/‖C‖² | packet's bound | tight? |
|---|---|---|---|
| 2 | 1/2 | 1 − max w = 1/2 | yes; κ = s = 1/4 |
| 3 | 3/8 | 3/16 | no, but valid; κ = 5/16 < s = 13/32 |

**R7 (S11).** Take C_0 = |g_0⟩⟨f_0| + |g_1⟩⟨f_1| with input and output ranges inside D_n and all w ≡ 1/2. Then:

- C_0 has rank 2 and all legs of dimension 4;
- s(F) = 1/4 for n = 2 and 13/32 for n = 3, both < 1/2.

Openness relative to rank-two operators follows from three facts:
1. C ↦ P_{ran C†} is continuous on the operators of rank exactly 2;
2. s is continuous;
3. leg dimension is the rank of a local reduction, which is lower semicontinuous, so "all legs = 4" is an open condition.

**R8 (S13).** Output case.

1. Compress K_i by P_E ⊗ I, writing Ω = Σ_a e_a ⊗ ē_a + Σ_b f_b ⊗ f̄_b in a basis adapted to E ⊕ E^⊥. This gives P_E ⊗ I − |Ω_E⟩⟨Ω_E|/2.
2. Partially transposing ∫|u⟩⟨u|^{⊗2} = (P_E⊗P_E + F_E)/6 gives ∫|u⟩⟨u| ⊗ |ū⟩⟨ū| = (P_E⊗P̄_E + |Ω_E⟩⟨Ω_E|)/6.
3. With |ū⊥⟩⟨ū⊥| = P̄_E − |ū⟩⟨ū|, this gives 3∫|u⟩⟨u| ⊗ |ū⊥⟩⟨ū⊥| = P_E⊗P̄_E − |Ω_E⟩⟨Ω_E|/2.
4. Adding P_E ⊗ (I − P̄_E) recovers the compression.
5. Each product term |α⟩⟨α| ⊗ |β̄⟩⟨β̄| ⊗ K_rest evaluates to q_{n−1}(⟨α|C|β⟩_i).

The input case is the mirror image. Two structural remarks:

- The compressed K_i is positive semidefinite, because ‖Ω_E‖² = 2 gives eigenvalue 0. This is why the s = n case holds at every rank.
- For a 3-dimensional leg, ⟨Ω_E, K Ω_E⟩ = 3 − 9/2 < 0 (negative control).

**R9 (S14–S18).** Theorem 6 is established as follows:

- (c) ⇒ (a): iterate R8. Contraction preserves rank ≤ 2 and the leg inclusions at the remaining sites.
- (a) ⇒ (b): immediate.
- (b) ⇒ (c): apply Lemma 4 to C′ ⊗ ⊗_L |u_i⟩⟨u_i|, using that q is symmetric under permutations of the sites.

The corollaries then follow:

- Corollary 1 uses (a) ⇐ T_n.
- Corollary 2 takes the union over the six choices of (site, orientation).
- Corollary 3 is the case s = n − 1 combined with T_1.
- Corollary 4: every C of rank ≤ 2 either has a 2-supported leg (then T_{n−1} applies via Theorem 6 with s = 1) or lies in Z_n's domain, and T_1 holds.

**R10 (rank one; supports S5 and S21a).** Let F_i swap site i between two copies of H_n. Then

q_n(|a⟩⟨b|) = ⟨a⊗b| ⊗_i (I − F_i/2) |a⊗b⟩,

because ‖Tr_S |a⟩⟨b|‖² = Tr[ρ^a_S ρ^b_S]. Since I − F_i/2 = Π_sym/2 + 3Π_anti/2 ≥ 1/2, it follows that q_n(|a⟩⟨b|) ≥ 2^{−n} ‖a‖² ‖b‖² for every d and n. Consequently W_odd contains no rank-one operator.

## 5. Findings

**m1 (MINOR; S21b, S22). The §6 wording overstates the two-leg coverage.**

- *The problem.* §6 says "every rank≤2 C with two distinct 2-supported legs", and the remainder is described as operators with "neither two supported legs …". Legs are indexed by (site, orientation), so "two distinct legs" literally includes the input and output legs at the *same* site.
- *Why it matters.* That same-site stratum is **not** covered. Positivity on it is equivalent to T_2:
  - (⇒) take C = |u⟩⟨v| ⊗ C′. Then q_3(C) = q_1(|u⟩⟨v|) · q_2(C′) with q_1(|u⟩⟨v|) = ‖u‖²‖v‖² − |⟨u|v⟩|²/2 > 0;
  - (⇐) apply Lemma 5.

  My exact witness has q_1 = 305/2 > 0. In a general same-site witness, all six nonzero contractions are rank-2 operators on H_2 whose legs all have dimension ≥ 3.
- *What is correct.* Corollary 3 itself ("n−1 **distinct sites**") is correct.
- *Fix.* Write "2-supported legs at two distinct sites" in the coverage list, and keep the same-site pair in the remainder.

**m2 (MINOR; S5, S21a). Rank-one positivity is asserted but not proved in this self-contained packet.**

- §6 lists "rank≤1" as proved, and the §2 "two-sided use" asserts that X_(2) "has rank2". The second claim needs W_odd to contain no rank-one element, i.e. rank-one positivity.
- Neither is proved in the packet. Both are true: R10 gives a two-line proof, and I checked it exactly at n = 1, 2, 2, 3.
- *Fix.* Add the R10 argument, or cite where it is proved.

**m3 (MINOR; S19). Corollary 5 states "every contraction … has q_{n−s} = 0".**

- From a zero integral one only gets μ-almost every.
- The upgrade to every u needs two facts: the integrand u ↦ q_{n−s}(⟨u|C|u⊥⟩_i) is continuous (it is a phase-invariant polynomial in u and ū), and Haar measure has full support.
- *Fix.* Add one sentence stating this.

**m4 (MINOR; S11). The topology and the strictness condition are under-specified.**

- "Open subsets" should say open relative to the operators of rank exactly 2 (or the rank ≤ 2 variety). The continuity and semicontinuity facts in R7 should be stated.
- "Since (4) is strict there" is not implied by "all w_j positive". For example, w = (1, 1/3, 1/3, 1/3) at n = 2 gives margin 0.
- Strictness needs max w < 1 for n = 2 and max w < 5/8 for n = 3; w ≡ 1/2 suffices for both.
- The conclusion (nonempty open subsets) is correct.

**m5 (MINOR; S22). The remainder paragraph uses an undefined term and loose wording.**

- "Concentrated range F" is undefined. Presumably it means s(F) > 1/2. With that reading, "T_3 ⟺ κ(F) ≤ 1/2 for every F with s(F) > 1/2" is true, because κ ≤ s.
- "Equivalently, it is the cross-sector Ky Fan inequality" conflates a *set of operators* with an *equivalent statement* of the open problem.
- *Fix.* Define the term and separate the two notions.

**E1 (editorial, not counted).** In Corollary 6, μ_j(X) should name the range used: input or output. For rank-deficient X, F may be any 2-dimensional subspace containing the range; rank ≤ 1 contractions are nonnegative anyway by R10.

**Not a defect.** The addendum's author check covers only Lemma 5 at d = 4, n = 2, with E = span{e0, e1} at site 1. My controls are independent of it and broader (§8).

## 6. What is proven and what remains open

**Proven in written form** (same-harness reviewed here; not formal):

- **Exact reformulations:**
  - identity (1);
  - Theorem 1 (T_n ⟺ the Ky Fan inequality σ_1² + σ_2² ≤ ‖X‖²/2 on W_odd);
  - Theorem 2 (T_n ⟺ κ(F) ≤ 1/2 for every two-dimensional F, with bound (2));
  - Theorem 3 (κ ≤ s, bound (4));
  - Lemmas 4 and 5;
  - Theorem 6 (ladder), with T_3 ⇒ T_2, one-leg stratum ⟺ T_2, and T_3 ⟺ Z_2 ∧ Z_3 (Z_2 ⟺ T_2 because T_1 holds).
- **Unconditional coverage of q_3 ≥ 0 at d = 4:**
  - rank ≤ 1 (R10; m2);
  - rank ≤ 2 with 2-supported legs at two **distinct** sites;
  - any rank with a 2-supported leg at all three sites;
  - rank ≤ 2 whose input or output range has λ_1 + λ_2 + λ_3 ≤ 15/8, with margin (4);
  - D_3 ranges with max w < 5/8, strictly;
  - nonempty relatively open subsets of Z_3 (and of Z_2 for n = 2).

**Not proven (the open q3 target).**
- T_3 itself (the original inequality).
- Equivalently Z_2 ∧ Z_3. In particular this includes:
  - T_2 ⟺ Z_2, i.e. σ_1² + σ_2² ≤ 2(‖A‖² + ‖B‖²) for all traceless A and B;
  - the one-leg stratum and the same-site two-leg stratum, each ⟺ T_2;
  - Z_3 outside the spread-covered ranges.

The packet claims none of these.

**My numerics are not evidence for the open target.** On random instances they are consistent with it:

- Ky Fan ratio (σ_1² + σ_2²)/‖X‖² ≈ 0.32–0.36 at n = 2 and ≈ 0.11 at n = 3;
- κ(F) ≈ 0.30–0.40 on random F.

Product ranges such as span{|00⟩, |10⟩} reach κ = 1/2 exactly, with q = 0 attained. So if the inequality holds, it is tight.

## 7. Exact dependency list

**Imports used by the packet's proofs** (standard facts):
- vectorisation identities;
- the Haar second moment on CP¹ and its partial transpose;
- the von Neumann trace inequality / Eckart–Young;
- Cauchy–Schwarz and the triangle inequality;
- Tr(AB) ≤ ‖B‖_∞ Tr A for A, B ≥ 0;
- compactness of the unit sphere of W_odd;
- implicitly, continuity of C ↦ ran C† on rank-2 operators and lower semicontinuity of rank (m4).

**Pinned data.** None: no certificates, solver outputs, numeric tables or target values.

**Conditional premises, as stated in the packet:**
- Theorem 6 (c) ⇒ (a) assumes T_{n−s};
- the §2 zero characterisation assumes T_n;
- Corollary 5 assumes T_{n−s};
- Corollaries 2 and 4 are equivalences, not proofs of T_2 or T_3.

**Packet-external dependencies:**
- S21e depends on `frontier-20261028-d4-source-independent-local-support-consolidated-v1.md` (`0ccc096a…`). Not reviewed.
- Rank ≤ 1 (S21a) has no proof in the packet; I supply one (R10).
- The other three cited packets are non-load-bearing cross-references. Not read.

**Source premises.** None. No HELD/ZERO/NONINPUT material was used by the packet as far as its text shows, and none was read by me.

## 8. Controls (reviewer-authored, actually run) and receipts

**Files.**
- Script: `f168rv-controls-v1.py`, SHA-256 `b8069bab7f4b9213fe3035cb22bfedc823f16b59a041202ef4e8b1cbbbb0bb5c` (62988 B). It uses only the standard library, numpy and mpmath, and does not import or execute any author code.
- Results: `f168rv-controls-v1-results.json`, SHA-256 `5f66069652c34587b903acd0ad158967d2128122bcee4743e57ff98c27cbcd12` (31351 B).
- Receipt: `f168rv-controls-v1-receipt.txt`.

**Recorded run.** `python3 -B f168rv-controls-v1.py`
- bash `/bin/date` before: Thu Oct 29 07:30:26 PDT 2026; in-script start 07:30:27.
- in-script end and bash `/bin/date` after: 07:30:59.
- Environment: Python 3.14.3, numpy 2.4.3, mpmath 1.4.1.
- Result: all 23 positive checks PASS; all 22 negative controls failed for the intended reason.

**Arithmetic and error model.**
- "Exact" means Gaussian-rational `Fraction` arithmetic.
- Numerical parts use float64 Hermitian eigen- and singular-value solvers. Each κ is computed two independent ways, and agreement within 1e-9 is required; observed agreement is about 1e-15.
- mpmath at dps 40 corroborates n = 2 results to 30 digits.

**Positive checks:**

1. **Identity (1), exact.**
   - Six random Gaussian-integer instances: n = 2 (two full-rank, two rank-2) and n = 3 (one full-rank, one rank-2). In every case q equals ‖C‖² − 2‖P_odd C‖². Example: n = 3 full-rank gives q = 174679/8.
   - The operator identity Π_− = (I − ⊗K)/2 holds; P_odd is idempotent; the sectors are complete, pairwise orthogonal and of the form I_T ⊗ (traceless).
   - K² = I and Tr K = 14 at d = 4. dim W_odd = 30 and 676 both exactly and as the numeric rank of an orthonormal sector basis.
2. **Theorem 1.**
   - Exact: random X ∈ W_odd (n = 2: three instances; n = 3: two instances with Y_jk ∈ sl₄⊗sl₄) satisfy P_odd X = X and the norm formulas.
   - Numeric: the Eckart–Young value is attained at X_(2); q(X_(2)/‖X_(2)‖) ≤ 1 − 2·ratio; 300 random rank-2 C never exceed the ratio. mpmath reconstructs the SVD with error < 1e-38.
   - Equality instances, exact: I⊗|0⟩⟨1| (n = 2) and I⊗|00⟩⟨11| (n = 3) give q(X_(2)) = 0, ‖P_odd C‖² = ‖C‖²/2 and P_odd C = X/2.
   - The tracelessness remark, exact: singular values (3, 2, 2, 2, 1, 1, 1, 0⁹), 13 > 12.
3. **Theorems 2 and 3.**
   - κ from the definition (30- and 676-dimensional W_odd Gram matrix) equals (1 − λ_min of q on {C = CP_F})/2. The minima over the left and right range spaces agree.
   - κ ≤ s on every tested F: 6 random F at n = 2, 3 random F at n = 3, the D_n uniform range, and the product range.

     | F | n | κ | s |
     |---|---|---|---|
     | random | 2 | 0.36–0.40 | 0.43–0.54 |
     | random | 3 | 0.30–0.32 | 0.44–0.49 |
     | D_2 uniform | 2 | 1/4 | 1/4 (tight) |
     | D_3 uniform | 3 | 5/16 | 13/32 |
     | product | 2 | 1/2 | 3/4 |
     | product | 3 | 1/2 | 33/32 |

     In this sample all three random F at n = 3 had s < 1/2. Sample of 3; not a claim.
   - Local-unitary invariance holds.
   - Converse chain at a maximiser X: ⟨X, XP_F⟩ = ‖XP_F‖² = κ, and q(XP_F)/‖XP_F‖² ≤ 1 − 2κ (equality observed).
   - Eight random all-variable D_2/D_3 ranges: the reductions equal Σ_j w_j |j…j⟩⟨j…j| to 1e-12, s matches the closed form, and λ_min ≥ 1 − 2s.
4. **Exact LDL positive-semidefiniteness certificates** on both {C = CP_F} and {C = P_F C} for the uniform D_n ranges:
   - n = 2: q_2 ≥ (1/2)‖C‖², with zero pivots, so the bound is tight;
   - n = 3: q_3 ≥ (3/16)‖C‖², minimum pivot 3/8.

   **Z-class witnesses (exact).** Rank 2, all legs of dimension 4, with (q, ‖C‖²) = (7, 8) at n = 2 and (6, 8) at n = 3. **Openness illustration (numeric only).** Nine factor perturbations of size up to 5e-2 keep s < 0.479, q/‖C‖² ≈ 0.72–0.76 and all legs equal to 4.
5. **Lemma 4, exact.** Checked for (m, k) = (1,1), (1,2), (2,1); q_1(|u⟩⟨u|) = ‖u‖⁴/2; site-permutation invariance holds.
6. **Lemma 5, exact.**
   - E is non-axis-aligned: columns of an exact Cayley rational unitary, verified U†U = I.
   - The 16×16 operator identities hold in both orientations.
   - The octahedron-design moment tensor equals the Bloch-sphere-moment tensor.
   - The compressed K_i is positive semidefinite for a 2-dimensional leg.
   - End to end, (5) and (6) hold at **every site**, both orientations, n = 2 and 3, for full-rank and rank-2 C: 20 cases. Two independent evaluations agree in every case: method A uses the octahedron design; method B uses the Bloch moments ⟨n_j n_k⟩ = δ_jk/3 with no design.
7. **Ladder witnesses, exact.**
   - One-leg stratum: legs (out@3 = 2, all others 4). The (5) sum equals q_3, and every contraction has rank 2.
   - Two distinct sites (out@1, in@2): the 100-term iterated sum equals q_3; every q_1 term is ≥ 0; leg inclusions survive contraction.
   - All three sites, rank 16: the 1000-term iterated sum equals q_3, which is ≥ 0.
   - Same-site pair: as described in m1.
   - n = 2 one-leg: every q_1 term is ≥ 0.
   - A generic random rank-2 C on H_3 has all six legs of dimension 4, so it lies in Z_3.
   - Product witness: q_3(C′ ⊗ |u⟩⟨u|) = q_2(C′) ‖u‖⁴/2.
   - T_1 holds on random rank-2 instances.
8. **Rank one, exact.** The swap decomposition equals q at n = 1, 2, 2, 3, and q ≥ 2^{−n}‖a‖²‖b‖².

**Negative controls (each fails for the intended reason):**

- **Identity (1).**
  - At d = 3, K is not a reflection and (1) fails: 1003/2 ≠ 4381/9.
  - Dropping the T = {1,2,3} sector breaks (1): 174647/8 ≠ 698661/32.
- **Converse direction and the spread bound.**
  - Outside W_odd, ‖XP_F‖²/‖X‖² = 13/24 > 1/2 yet q_2(XP_F) = 1/4 > 0. The converse needs W_odd, i.e. tracelessness.
  - Replacing ‖·‖_∞ by the normalised trace in (3) is violated: the product range has κ = 1/2 > 1/4.
- **The LDL tool.** It rejects bounds just above the true minimum: 5001/10000 for D_2 and 3751/10000 for D_3, on both sides.
- **Lemma 5 faults.** Each is detected at both the operator level and end to end:
  - weight 2 instead of 3;
  - dropping the E^⊥ term;
  - u in place of u⊥;
  - the wrong orientation formula.
- **Leg and rank hypotheses.**
  - A 3-dimensional leg makes the compressed K non-PSD.
  - With 3-dimensional legs at all sites, q_3(P_3^{⊗3}) = −27/8. With 2-dimensional legs the value is 0, the boundary case.
  - Corollary 3 needs rank ≤ 2: |0⟩⟨0|⊗|0⟩⟨0|⊗P_3 has rank 3 and q_3 = −3/8.
  - T_1 fails at rank 3: q_1(P_3) = −3/2.
- **R10.** It needs |a⟩⊗|b⟩, not |a⟩⊗|b̄⟩: the conjugated variant gives 26837/2 ≠ 26637/2.

## 9. Deviations and disclosures

- **Hash-only checks.** I hash-checked the author's script and result named in the addendum. Both match. I did not open them and did not execute anything of the author's.
- **Development runs.** Two `--dry` runs (07:24:42–07:25:14 and 07:28:34–07:29:08 PDT) used earlier versions of my script and wrote no files. The recorded run above is the only run that wrote files.
- **No caches or temp files.** I ran with `python3 -B`: no `__pycache__`, no temporary directories.
- **Files written.** Only these four, all in this review directory:
  - `f168rv-controls-v1.py`
  - `f168rv-controls-v1-results.json`
  - `f168rv-controls-v1-receipt.txt`
  - `review-v1.md`
- **Not used.** No web search, no external model or paid API, no Git, no deletion, no publication, no contact with the author.
- **Status-only safety controls received.** During this review Main sent two status-only safety controls, about f162 (Olson) and f161. I did not open or consume any f161 or f162 material; this wave is unrelated.
- **Scope of the dimension check.** All exact checks are at d = 4, plus the d = 3 negative. The "every d" scope of Lemma 5 and Theorem 6 rests on my hand reconstruction, which does not depend on d.

## 10. Summary

The packet reformulates the open d = 4 three-copy rank-≤2 q3 target in exact, source-independent terms. I checked each reformulation two ways: an independent derivation, and controls I wrote and ran.

- **Ky-Fan dual.** q_n(C) = ‖C‖² − 2‖P_odd C‖², with W_odd the span of odd-sector operators I_T ⊗ Y_T (Y_T traceless at every site outside T). This yields T_n ⟺ σ_1² + σ_2² ≤ ‖X‖²/2 on W_odd.
- **Range-wise dual and spread bound.** T_n ⟺ κ(F) ≤ 1/2, with the computable bound κ ≤ s.
- **Contraction identity.** Lemma 5 holds exactly at every site and in both orientations, with two independent integration methods.
- **Support ladder.** T_3 ⇒ T_2; the one-leg stratum ⟺ T_2; T_3 ⟺ Z_2 ∧ Z_3.
- **Strict positivity.** It holds on explicit open families of zero-leg operators.

I found no FATAL or MAJOR problem. The five MINOR items are precision fixes:

- m1: write "2-supported legs at two distinct sites"; the same-site pair is itself equivalent to T_2;
- m2: add the missing rank-one positivity proof;
- m3: give the almost-everywhere-to-everywhere step in Corollary 5;
- m4: specify the topology and the strictness condition for openness;
- m5: define "concentrated" in the remainder paragraph.

One §6 bullet depends on a packet outside this review's inputs and is INCONCLUSIVE. What remains open — and is not claimed — is the q3 target itself: T_3 ⟺ Z_2 ∧ Z_3, including T_2 (⟺ Z_2) and the zero-leg class Z_3 beyond spread ranges. This is a same-harness review and not human, independent-model-family, formal/kernel or novelty verification.
