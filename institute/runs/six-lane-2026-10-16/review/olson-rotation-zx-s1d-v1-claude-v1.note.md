# Hostile audit: Lemma S1(d) addendum v1 (SOURCE00)

This audit covers the written arguments only. There was no execution or network access, and SHA256s were not recomputed. The hash prefixes SOURCE00 cites for SOURCE02, 04 and 05 match the supplied headers. Not used as premises: notes-ZX-residual-v1, t-search run1 (ruled UNKNOWN), and any finite aid.

**Bottom line:** no FATAL or MAJOR findings. The lemma is correct relative to the declared index-one import, and every fix below is wording or citation.

## Verdicts

| Item | Verdict | FATAL / MAJOR / MINOR |
|---|---|---|
| Lemma S1(d), SOURCE00:42-116 | **AWF** | 0 / 0 / 6 |
| Corollary S1++, :125-126 | **ACCEPT** | 0 / 0 / 0 |
| ROT-ZX++ terminal, :134-136 | **ACCEPT** | 0 / 0 / 0 |
| ROT/INV*-ZX++ uniform, :138-146 | **ACCEPT** | 0 / 0 / 0 |
| OLSON-ZX++ ordered, :148-156 | **ACCEPT** | 0 / 0 / 1 (optional) |
| Sec. 3 tables and residual, :160-180 | **AWF** | 0 / 0 / 3 |

## 1. Lemma S1(d), re-derived step by step

**(1) Lengths.**
- A failure of (S1) is a zero-sum of length ≥ p+4. Lengths are even and p+4 is odd, so the length is ≥ p+5.
- (ZP) then forces N ≥ 2p+2.
- D(Z_2p) = 2p applied to T minus one occurrence (length ≥ 2p+1) gives a nonempty proper zero-sum T′.
- T′ and T−T′ are both shorter zero-sums, so each has length ≤ p+3.
- Hence N ∈ {2p+2, 2p+4, 2p+6}, and every proper nonempty zero-sum of T has length in [N−p−3, p+3]. ✓

**(2) Half-sum T₁, Claims A and B.**
- EGZ on any 2p−1 x-values gives T₁ with |T₁| = p and x(T₁) = 0, so its group sum is (1,0).
- M = T−T₁ has odd length N−p ≥ p+2 and x(M) = 0.
- Claim A, even case: an even V has |V| ≤ p < N, so it is proper and |V| ≥ N−p−3.
- Claim A, odd case: T₁V is a zero-sum of length ≤ 2p < N, so p+|V| ≤ p+3.
- Claim B: V₁V₂ is a zero-sum of even length ≤ 6, but (1) requires length ≥ N−p−3 ≥ p−1 ≥ 10. ✓

**(3) N = 2p+2.**
- If N ≥ 2p+4, then N−p−3 ≥ p+1 > p, so every Claim-A set is odd of size ≤ 3.
- |M| ≥ p+4, so Davenport gives V₁, and Davenport again on M−V₁ (≥ p+1 terms) gives a disjoint V₂. This contradicts Claim B.
- So N = 2p+2, and proper zero-sums have length p−1, p+1 or p+3. ✓

**(4) No (1,0) term.** The argument works at the level of occurrences.
- EGZ on the 2p+1 other occurrences places u in M.
- Davenport on p of the p+1 occurrences of M−{u} gives V.
- If V is odd (possibly another (1,0) occurrence), it is disjoint from {u}, contradicting Claim B.
- If V is even, then |V| = p−1. The two leftover occurrences have x-sum 0−0−0 = 0, giving a zero-sum of length 2 < p−1. ✓

**(5) M = C·V.**
- An odd V₀ has size 3, since size 1 would be (1,0).
- An even V₀ has size p−1, and then C = M−V₀ has size 3.
- Minimality is proved **over Z_p**. An even V″ would be a short zero-sum. An odd V″ makes V″ and V−V″ two odd x-zero subsets of M, forcing p−1 ≤ 6.
- Minimality in Z_2p alone would exclude only even V″ and would not meet the import's hypothesis. The proof supplies the stronger property. ✓

**(6) Index one.**
- The import applies: C_p with p ≥ 3, and length p−1 ≥ ⌊p/2⌋+2 = (p+3)/2 iff p ≥ 5.
- The element a is nonzero because Σxᵢ = ord(a) ≥ p−1 ≥ 2. So ord(a) = p, every xᵢ ∈ {1,2} (these are least residues, matching SOURCE01:11), and exactly one xᵢ equals 2.
- So V = ĥ^(p−2)·y with y = (1,2h) ≠ ĥ, and t ≥ p−2. ✓

**(7) Every other term.** Write z's x-value as ch; then c ∉ {0,1}.
- c even: β = p−c is odd, lies in [1, p−2], and β ≤ t. Then ĥ^β·z is a zero-sum of length β+1 ≤ p−1, so β+1 = p−1 and c = 2. This also handles z = y, and excludes c = p−1 (length 2).
- c odd: c ≤ p−2, so j ∈ [0, p−5]. z ∉ V, since V has only the values ĥ and y.
- The term y is V's fixed term, and the j copies of ĥ come from V, so all occurrences are distinct.
- The length p−c is even and lies in [2, p−3], contradicting (3). ✓

**(8) Contradiction.**
- From x(T) = 0: u ≡ −2 (mod p). Also 1 ≤ u ≤ 2p+2 and 3p−2 > 2p+2, so u ∈ {p−2, 2p−2}.
- u = 2p−2 gives t = 4 < p−2, impossible.
- u = p−2 gives t = p+4. Then ĥ^(p−6)·y³ is a zero-sum (x-sum p·h = 0) of even length p−3 < p−1. ✓

**Boundary cases.**
- **p = 11:** the only binding inequality is 6 < p−1 = 10, which holds. SOURCE00:118-121 is accurate: only Claim B and Step (5) need p ≥ 11, Step (8) needs p ≥ 7, and Steps (4) and (6) need p ≥ 5.
- **p = 7:** I recomputed the control. Take x-values 1¹³5³ in Z₂×Z₇.
  - The zero-sums (a,b) are (4,2), (9,1) and (13,3), of lengths 6, 10 and 16.
  - Lengths 12–14 are absent, so (ZP) holds; 16 > 10 violates (S1).
  - In the proof, T₁ = g⁷ and M = g⁶(5g)³ contains two disjoint half-sums g²(5g) of total length 6 = N−p−3.
  - Claim B is the first step to fail, so **S1(d) is false at p = 7**.
- **p = 5:** the argument fails there (p−1 = 4). Neither SOURCE00 nor this audit asserts anything at p = 5 or p = 7.
- **Where the branch matters:** the κ = (p+3)/2 branch is terminally non-vacuous only for p ≥ 13, since it needs k ≥ (p+5)/2 together with 3k ≤ 2p+1.

## 2. Consequences

**S1++.** An integer κ ≤ (p+3)/2 is either ≤ (p+1)/2, covered by S1+ (SOURCE02:19, integer domain), or equal to (p+3)/2, covered by S1(d). ✓

**Terminal (ROT-ZX++).** Fix some admissible normal form.
- k = 1: K1 gives one nonzero pair with c ≠ 0 (SOURCE02:53).
- k ≥ 2: κ̂ is an integer because F ≡ o ≡ k (mod 2), and κ̂ ≥ 0 by the GRX / H ≥ p argument (SOURCE02:53).
- GRX gives (ZP) (SOURCE05:43), S1++ gives (S1), and item 3 gives the pair.
- INV* still requires o_F(w) ≤ p, which SOURCE00:136 retains as SOURCE02:20 demands.
- The SHgen-E discharge is internal to item 3 and unchanged. ✓

**Uniform (INV*-ZX++).** A normal form exists, and every one has 1 ≤ k ≤ o (SOURCE05:37-43).
- Low branch: κ̂ ≤ k−1 ≤ o−1 ≤ (p+3)/2.
- High branch: (F−o)/2 ≥ (p−5)/2 gives κ(w) ≤ (p+3)/2, and κ̂ = κ(w) − (o−k)/2 ≤ κ(w).
- REFL on the original word needs o ≤ (2p+1)/3 ≤ p, which holds. ✓

**Ordered Olson (OLSON-ZX++).** Every subword of a counterexample is an avoider.
- Case 1 (R ≤ 2): F ≥ 4p−3 and o ≤ (2p+1)/3 ≤ 2p−3. So there are (F−o)/2 ≥ p framed adjacent equal pairs, and no INV* call is needed.
- Case 2 gives (o−1, F−1); Case 3 gives (o or o−2, F).
- In both, o′ ≤ o preserves 3o′ ≤ 2p+1 and the low branch, and F′−o′ ≥ F−o preserves the high branch. ✓

## 3. Tables and residual

| p | (p+5)/2 | ⌊(2p+1)/3⌋ | Check |
|---:|---:|---:|---|
| 11 | 8 | 7 | o ≤ 7, unchanged ✓ |
| 13 | 9 | 9 | every o ✓ (previously o = 9 needed F ≥ 19) |
| 17 | 11 | 11 | every o ✓ (previously o = 11 needed F ≥ 25) |
| 19 | 12 | 13 | o = 13 needs F ≥ 27, which is odd as required ✓ (previously 29) |
| 23 | 14 | 15 | o = 15 needs F ≥ 33 ✓ |

- **Residual threshold:** κ̂ ≥ (p+5)/2 forces k ≥ (p+7)/2, which is compatible with 3k ≤ 2p+1 iff p ≥ 19.
- **Listed pairs:** correct.
- **Wording:** :171 and :175 correctly state sufficiency only, with no existence or failure claim.

## Findings (all MINOR)

- **m1, SOURCE00:23, 29.**
  - "V. Savchev" should be "S. Savchev" (SOURCE01:7, 17).
  - Replace the "IRC 12:2x–12:3x" pointer with the parent record SOURCE01 (e4615144…35c6).
- **m2, SOURCE00:17.** SOURCE04 has no "Sec. 0". Cite SOURCE04:15-17 (Imports block) instead.
- **m3, SOURCE00:93.** Add: "a ≠ 0 since Σxᵢ = ord(a) ≥ p−1 ≥ 2; hence ord(a) = p."
- **m4, SOURCE00:57-66 and :75.** Claims A and B are proved for one T₁, but Step (4) re-chooses T₁.
  - This is valid, because the proofs use only |T₁| = p, x(T₁) = 0 and Step (1).
  - Fix: state the claims "for every half-sum T₁ ≤ T with |T₁| = p".
  - At :47, add "(lengths are even and p+4 is odd)".
- **m5, SOURCE00:34 vs :96.** The letter y is used both for a generic odd element and for the specific term (1,2h). Rename the generic one.
- **m6, SOURCE00:9-10.** The cross-reference to the (R1)–(R2) results of notes-ZX-residual cannot be verified here. Label it "informational, unaudited".
- **m7 (optional), SOURCE00:153-156.** State "3o′ ≤ 3o ≤ 2p+1" and "o ≤ (2p+1)/3 ≤ 2p−3" explicitly, as SOURCE04:82 does.
- **m8, SOURCE00:173-175.** Overlay 2 (SOURCE02:52) requires the residual to quantify over all normal forms. Proposed text:
  - "An avoider is outside this route only if every admissible normal form has k ≥ 2 and either 3k > 2p+1, or 3k ≤ 2p+1, κ̂ ≥ (p+5)/2 and (S1) fails."
  - "For INV*, also include the case o_F(w) > p."
  - "Outside 3k ≤ 2p+1 nothing is covered (SOURCE03 Sec. 6)."
- **m9, SOURCE00:174.** Label the pair list as examples. The general form is (p+7)/2 ≤ k ≤ ⌊(2p+1)/3⌋ with (p+5)/2 ≤ κ̂ ≤ k−1; for instance p = 31 adds six pairs.
- **m10, SOURCE00:179.** "Recorded outputs show … as this lemma requires" reads as corroboration from a run ruled UNKNOWN. Reword to: "records no …; ruled UNKNOWN; not evidence either way."

## Imports and scope

**Audited here, by hand:**
- Steps (1)–(8) of S1(d).
- Davenport's pigeonhole proof (SOURCE04:16-17).
- The S1++ combination.
- All inequalities and table entries in Sections 2–3.
- The p = 7 control.

**Classical, imported, not re-proved:**
- D(C_n) = n.
- EGZ for Z_p.
- The Savchev–Chen / Yuan index-one theorem:
  - SOURCE00:19-21 matches SOURCE01:9-11.
  - It is used once, at C_p with length p−1.
  - Neither the parent nor this audit read its proof.

S1(d) is therefore complete **relative to** this import and is not self-contained, exactly as SOURCE00:32 declares. A narrower import would suffice: every zero-sum-free sequence of length p−2 over C_p is g^(p−2) or g^(p−3)(2g).

**Parent-accepted, interfaces checked only:**
- S1+.
- Terminal item 3, with ZX, the normal form and DAV, GRX, K1, and SHgen/SHgen-E.
- REFL-few-odd at o ≤ p.
- The OLSON-few v3 case structure, RGR-LONG, and overlay 8.

**Scope of what is established:**
- (ZP) implies (S1) for every integer 0 ≤ κ ≤ (p+3)/2 and every prime p ≥ 11.
- INV* and ordered Olson hold only on the displayed sufficient classes.
- This is not ROT(p), INV*(p), general ordered Olson for D_2p, or the all-groups target.
- No existence or novelty claim is made.
