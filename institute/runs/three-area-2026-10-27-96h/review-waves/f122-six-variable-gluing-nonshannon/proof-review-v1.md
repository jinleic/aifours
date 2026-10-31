# f122 proof review v1 — six-variable gluing inequality Φ and its exact Shannon-cone witness

**Verdict: MINOR (no FATAL, no MAJOR; three non-blocking MINOR notes).** At the manifest's stated scope — "all finite entropy laws and the almost-entropic closure satisfy the explicit six-variable 16-term gluing inequality; a standalone exact six-variable Shannon polymatroid violates it, establishing non-Shannon-type cone separation, NOT novelty or an improved guessing-number bound" — every load-bearing statement was independently reconstructed and confirmed by exact arithmetic and by independently authored finite-law controls. Nothing beyond that scope is established here (see §6).

Review kind: INDEPENDENT_SAME_HARNESS_SCIENTIFIC_REVIEW (manifest). This is a same-harness Claude agent review. It is **not** human, **not** independent-model-family, **not** formal/kernel, and **not** a novelty review.

Clock observed before composing this file: `2026-10-29T03:00:17Z` (`2026-10-28T20:00:18-0700 PDT`). The file's mtime is the actual write time and is an upper bound.

## 0. Binding

| Item | Path | SHA-256 | Bytes | LF | Observed |
|---|---|---|---|---|---|
| Manifest | `.../review-waves/f122-six-variable-gluing-nonshannon/manifest-v1.json` | `b8bdc86c7281c3c8e1d0c6a2abdc980848e620650a8df95906cae854a6524907` | 2545 | — | 2026-10-29T02:48:43Z |
| Authority (read) | `.../three-area-2026-10-27-96h/contract-addendum-2-frontier-first-owner-direction-v1.json` | `5e18c2d4b94656fc12b5cfce4122889fa6073e24a21f1e0062c79d846b6037ce` | 3210 | — | 2026-10-29T02:49Z |
| Input 1 (proof) | `.../guessing-rminus/frontier-20261028-six-variable-gluing-inequality-v1.md` | `f5c83b572ecc2ec25a62b22e24e405a897b37152385a11a1e31f37f567a07075` | 5518 | 62 | 2026-10-29T02:48:49Z |
| Input 2 (witness) | `.../guessing-rminus/frontier-20261028-six-variable-nonshannon-witness-v1.json` | `10aa3d5daa42b42223193b5a465aa32e5883b592a916be5d5941ee00bc5dc169` | 1769 | 146 | 2026-10-29T02:48:49Z |
| Input 3 (author checker, read only) | `.../guessing-rminus/frontier-20261028-six-variable-witness-check.py` | `4b55faa53a9d3043eb4baa9d3fc497934247c37da83b0a04927854697d09fdf6` | 3550 | 73 | 2026-10-29T02:48:49Z |

All five SHA-256 values, byte counts and LF counts matched the manifest pins exactly. Inputs were read completely, in the declared order, with `:raw` selectors.

Not read, not executed, not used: the files named inside input 1 but absent from the manifest (`frontier-20261028-universal-gluing-inequality-v1.md`, `frontier-20261028-six-variable-gluing-separation-check.py`, its receipt, `frontier-20261028-crosspair-without-independence-candidate.json`, the author checker's result receipt). No web search, no external model, no author contact, no Git, no deletion. The author checker (input 3) was read but never imported or executed; the reviewer scripts contain no reference to it. The only author artifact consumed by reviewer code is the witness JSON, read as data and compared against an independent transcription of the markdown.

## 1. Claims under review (input 1)

- **C1.** For arbitrary finite random variables B,C,R,H,P,Q,
  Φ = −H(BC) − H(BR) + 2H(BCRH) + H(BCP) + H(BRP) − H(BCRP) − H(BHP) + H(BCHP) − H(BCRHP) − H(BQ) + H(BCQ) + H(BRQ) + H(BHQ) − H(CHQ) + H(CRHQ) − 2H(BCRHQ) ≥ 0, and the same on the almost-entropic cone by closure.
- **C2.** Identity Φ = I(B;R|CHPQ) + I(C;R|BPQ) + I(C;Q|BHP) + I(R;P|CHQ) + I(H;P|BQ) + I(H;Q|BCRP) + I(P;Q|BR) + I(P;Q|BC) − 2 I(P;Q|BCRH).
- **C3.** Gluing: no term of Φ contains both P and Q; replacing the conditional law of (P,Q) given Y=(B,C,R,H) by the product of its conditional marginals preserves every term of Φ and makes I(P;Q|Y)=0, so Φ equals a sum of eight CMIs.
- **C4.** Conditioning on any further vector Z preserves the inequality.
- **C5.** The 64 listed integers divided by 6,900,000 form a polymatroid r (all 246 elemental inequalities hold) with Φ(r) = −50548/6,900,000 = −12637/1,725,000 < 0.
- **C6.** Hence Φ ≥ 0 is not a nonnegative combination of the six-variable elemental Shannon inequalities (non-Shannon-type, cone-separation sense). Explicitly disclaimed by the author: novelty, any guessing-number bound, cross-model/proof-assistant verification.
- Statements in input 1 that are **outside** this review's inputs and were **not** verified: the 12-variable conditioned-instance correspondence; the 12-variable extension check "on all 67,596 elemental rows" and its value I(P;Q|X)=12599/34500; the 45,360 substitution LP statement; the four non-input SHA-256 values. Input 1 itself says the 12-variable provenance is not a premise; the manifest says the same.

## 2. Independent reconstruction

### 2.1 Encoding

Bits B=1, C=2, R=4, H=8, P=16, Q=32 (least to most significant), as stated in input 1 and `variable_order` of input 2. A mask is "mixed" if it contains both P (bit 16) and Q (bit 32), i.e. the 16 masks 48–63.

Transcribing the 16 written terms of C1 into masks: 3:−1, 5:−1, 15:+2, 19:+1, 21:+1, 23:−1, 25:−1, 27:+1, 31:−1, 33:−1, 35:+1, 37:+1, 41:+1, 42:−1, 46:+1, 47:−2. This is exactly `inequality_coefficients_by_mask` of input 2 (machine-compared, receipt §B). No written mask is mixed. The 64 integers of the markdown table equal `values_by_subset_mask` of input 2 entry-by-entry (machine-compared, receipt §B).

### 2.2 The nine-CMI identity (C2), expanded over all 64 coordinates

With I(a;b|z) = H(az) + H(bz) − H(abz) − H(z), the nine rows contribute (mask: sign):

| Row | +H | +H | −H | −H |
|---|---|---|---|---|
| I(B;R\|CHPQ) | 59 | 62 | 63 | 58 |
| I(C;R\|BPQ) | 51 | 53 | 55 | 49 |
| I(C;Q\|BHP) | 27 | 57 | 59 | 25 |
| I(R;P\|CHQ) | 46 | 58 | 62 | 42 |
| I(H;P\|BQ) | 41 | 49 | 57 | 33 |
| I(H;Q\|BCRP) | 31 | 55 | 63 | 23 |
| I(P;Q\|BR) | 21 | 37 | 53 | 5 |
| I(P;Q\|BC) | 19 | 35 | 51 | 3 |
| −2·I(P;Q\|BCRH) | −2×31 | −2×47 | +2×63 | +2×15 |

Mixed coordinates, each cancelling to 0: 49 (−1 from I(C;R|BPQ), +1 from I(H;P|BQ)); 51 (+1, −1 from I(P;Q|BC)); 53 (+1, −1 from I(P;Q|BR)); 55 (−1, +1 from I(H;Q|BCRP)); 57 (+1 from I(C;Q|BHP), −1 from I(H;P|BQ)); 58 (−1 from I(B;R|CHPQ), +1 from I(R;P|CHQ)); 59 (+1, −1 from I(C;Q|BHP)); 62 (+1, −1 from I(R;P|CHQ)); 63 (−1 from I(B;R|CHPQ), −1 from I(H;Q|BCRP), +2 from the −2 row). Surviving coordinates: 3:−1, 5:−1, 15:+2, 19:+1, 21:+1, 23:−1, 25:−1, 27:+1, 31:(+1−2)=−1, 33:−1, 35:+1, 37:+1, 41:+1, 42:−1, 46:+1, 47:−2 — exactly the 16 written terms; all 39 remaining coordinates (including the empty set, coordinate 0) are 0. The dense 64-coordinate machine comparison agrees (receipt §A: `dense_64_coordinate_identity_holds: true`, `count_nonzero: 16`, `empty_set_coordinate: 0`). The identity is a formal linear identity on set functions, hence holds for every polymatroid and every entropy vector. **C2 confirmed.**

Side computation: the coefficient sum is 0 (needed in §2.4) and in fact the sum of coefficients over terms containing any fixed variable is 0 for each of the six variables (receipt of `proof-extra-controls-v2.py`; recorded as an observation only).

### 2.3 Gluing proof (C3), written out

Let p be any law on finite alphabets for (B,C,R,H,P,Q); write Y=(B,C,R,H), y for its values. Define
p′(y,π,κ) = p(y)·p(π|y)·p(κ|y) for p(y)>0, and p′=0 where p(y)=0.

*Lemma A (marginal preservation).* Σ_κ p′(y,π,κ) = p(y)p(π|y) = p(y,π), so p′ and p have the same (Y,P) marginal; symmetrically the same (Y,Q) marginal. Every subset S ⊆ {B,C,R,H,P} has its marginal determined by the (Y,P) marginal, and every S ⊆ {B,C,R,H,Q} by the (Y,Q) marginal. Therefore H_p(S) = H_p′(S) for every non-mixed S. All 16 terms of Φ are non-mixed (§2.1), so Φ(p) = Φ(p′).

*Lemma B.* Under p′, (P,Q) are conditionally independent given Y by construction, so I_p′(P;Q|Y) = 0.

*Theorem.* Apply the formal identity C2 to the entropy vector of p′: Φ(p′) = Σ_{eight} I_p′(·;·|·) − 2·0 ≥ 0 since each CMI of a genuine law is nonnegative. By Lemma A, Φ(p) = Φ(p′) ≥ 0. Note the eight CMIs are evaluated under p′, not p (they generally differ; the finite-law receipt shows e.g. I(P;Q|BR) = 0.0822 under the original law versus 4.1×10⁻⁵ under the glued law), which is why the −2 I(P;Q|Y) term is what the gluing removes and nothing else. **C3 confirmed.**

Finite-law realisation (receipt `proof-finite-law-gluing-example-v2-receipt.json`): for an explicit rational law L on 2⁴×3×3 cells with I_L(P;Q|Y) = 0.1102 bits, all 47 non-mixed marginal *tables* of L and the glued G coincide exactly as rationals, all 16 mixed tables differ, G satisfies p′(y,π,κ)p′(y)=p′(y,π)p′(y,κ) exactly in every cell (L does not), Φ(L) = Φ(G) = 0.026505211821808222971… bits with difference exactly 0.0, Φ(G) equals the sum of its eight nonnegative CMIs to 2.3×10⁻⁶⁰, and the identity residual on actual entropies is ≤ 7.8×10⁻⁶¹ for both laws (mpmath, 60 digits).

### 2.4 Conditioning (C4)

For an additional finite Z: H(S|Z) = Σ_z p(z) H_{p(·|z)}(S), so Σ_S c_S H(S|Z) = Σ_z p(z) Φ(p(·|Z=z)) ≥ 0 by C1 applied to each conditional law. Because Σ_S c_S = 0, Σ_S c_S H(S|Z) = Σ_S c_S H(S∪Z), i.e. the conditioned inequality is the same 16-term pattern with Z adjoined to every term and no H(Z) term. **C4 confirmed**; numerically exhibited in receipt §7 (Σ c_S H(S,Z) = 0.023136602777386714853… = ⅓Φ(L)+⅔Φ(L₂), difference 1.7×10⁻⁶⁰). The author's specific 12-variable instantiation is not an input and is not verified.

### 2.5 Almost-entropic closure

{h ∈ ℝ⁶³ : Φ(h) ≥ 0} is a closed half-space containing Γ*₆, hence containing its closure. **C1 (closure part) confirmed.**

### 2.6 The witness (C5)

Reviewer check (`proof-identity-and-witness-check-v1.py`, §C/§D) verifies the polymatroid axioms **directly**, not only the elemental system: r(∅)=0; all 384 monotone steps r(S∪{i}) ≥ r(S); all 4096 pairs r(S)+r(T) ≥ r(S∪T)+r(S∩T); all 64 entries nonnegative integers. Separately the 246 elemental inequalities (6 + 15·2⁴) were enumerated: all hold, 61 are tight, minimum positive slack 6852 (scaled). Exact value: Σ c_m r[m] = −50548 (hand arithmetic in the running sum: −13,800,000 → +2,800,000 → … → −50548; machine identical from the 16-term vector and from the dense 64-coordinate CMI vector), i.e. Φ(r) = −50548/6,900,000 = −12637/1,725,000, gcd-reduced (12637 is coprime to 1,725,000 = 2³·3·5⁵·23). **C5 confirmed.**

### 2.7 Cone separation (C6), exact scope

Γ₆ (the Shannon/polymatroid cone) is the polyhedral cone cut out by the elemental inequalities; by Farkas' lemma a linear inequality is valid on Γ₆ iff it is a nonnegative combination of the elemental inequalities. Since r ∈ Γ₆ (direct axiom check) and Φ(r) < 0, Φ ≥ 0 is not valid on Γ₆, hence not a nonnegative combination of six-variable elemental inequalities. Combined with C1: Φ ≥ 0 is a valid inequality on closure(Γ*₆) that is not Shannon-type for n=6. Corollary (not claimed by the author, noted here): r ∉ closure(Γ*₆). **C6 confirmed at exactly this scope.**

## 3. Controls executed (all reviewer-authored; receipts in this directory)

| Script | SHA-256 | Bytes | Receipt | SHA-256 | Bytes | Exit | Clock (UTC) |
|---|---|---|---|---|---|---|---|
| `proof-identity-and-witness-check-v1.py` | `b2e6dfaae4f27806ff37d69f0884a93bac17c64ca503daf5fcddcbf9bf89201e` | 13609 | `proof-identity-and-witness-check-v1-receipt.json` | `cd9602a5a901ebd710f6ca20d52fd893ff5152dee3b4aff86c64f3e942ba77c6` | 6529 | 0 | 02:54:17–02:54:18 |
| `proof-finite-law-gluing-example-v1.py` | `cd1575ab940979c9087b88882e0012c05ad277f6801e56f1192232fdd6b1cd97` | 13557 | `proof-finite-law-gluing-example-v1-receipt.json` (empty, failed run) | `e3b0c442…b855` | 0 | 1 | 02:56:22 |
| `proof-finite-law-gluing-example-v2.py` | `7bac5268348ba771be00106a0bb26974a047e36dcf42a81a407e47379daa5c16` | 13914 | `proof-finite-law-gluing-example-v2-receipt.json` | `4560c264441d579f52ebb3e61d02037d98526f0c40703828cc7b6a0d7ca9dc93` | 4403 | 0 | 02:56:50–02:57:06 |
| `proof-extra-controls-v1.py` | `d365e88cc66c98152668b82a2c2325dd7f692a9ced53fb62873b79ff6c7664fd` | 5049 | `proof-extra-controls-v1-receipt.json` (empty, failed run) | `e3b0c442…b855` | 0 | 1 | 02:58:36 |
| `proof-extra-controls-v2.py` | `6b753ff138b3284d756c41e77cc6e360a86cc49137c0c5692928e8ab22b1c94d` | 5806 | `proof-extra-controls-v2-receipt.json` | `5d50cdec2e6a921fd2929fc898d9291435369263a487317137df0792db999262` | 1935 | 0 | 02:59:10 |

Failed attempts are retained, not edited. v1 of the finite-law script failed only its own mpf-equality assertion: identical rational tables summed in different key orders produced entropies differing by ~3×10⁻⁶¹; v2 sums in sorted order (bit-identical) — the exact rational table equality already held in v1. v1 of the extra controls failed only because it demanded the *first* reported failure family be submodularity, while raising r(BCR) also breaks the tight monotone step BCR→BCRH; v2 reports all failing families and asserts the targeted elemental is violated.

Control outcomes (all as expected):

- Identity mutations, must REJECT, with the exact differing coordinates recorded: negative coefficient −2→−1 (coords 15,31,47,63 differ); −2→−3 (same four); conditioning CHPQ→CHP on I(B;R|·) (8 coords); BR→BH on I(P;Q|·) (8); BCRH→BCH on the −2 row (8); swapped roles I(C;Q|BHP)→I(C;P|BHQ) (4); dropped row I(R;P|CHQ) (4); written coefficient of H(BCRHQ) −2→−1 (coord 47); written sign of H(CHQ) flipped (coord 42). Positive: permuted rows ACCEPT.
- Witness mutations, must REJECT: r(∅)=1; r(BCRHPQ)−1 (monotonicity BCRHP+Q, and H(B|CRHPQ) slack −130201 in the corrupt-r63 variant); raising the union of the tight pair I(B;R) (z=∅) by 1 → submodularity {B},{R}; raising r(BCR) by 1 on the tight nonempty-condition pair I(B;R|C) → I(B;R|C) = −1 (also I(H;P|BCR), I(H;Q|BCR) = −1 and the BCR→BCRH monotone step). Positive: 2·r ACCEPT with Φ doubled to −101096 (cone property); independent-uniform-bits polymatroid ACCEPT with Φ = 0; flipping the written coefficient at mask 3 changes the value to +13,749,452 (sensitivity).
- Finite-law negative control: Φ_bad := 8 CMIs − 3·I(P;Q|BCRH) = Φ − I(P;Q|BCRH) has the mixed coordinate 63 with coefficient +1; on the law "Y constant, P=Q uniform bit" Φ = 0 but Φ_bad = −1 bit; on the dependent law L, Φ_bad = −0.0837 bits while Φ(L) = +0.0265; gluing does not preserve Φ_bad (G gives +0.0265). So the wrong coefficient yields a genuinely false entropy inequality, and the mixed-term cancellation is load-bearing.
- Seeded random sweep (seed 122): 200 full-support and 100 sparse rational laws on 2⁴×3×3; min Φ = 0.0666 bits (all ≥ −10⁻⁴⁵), max identity residual 4.7×10⁻⁶⁰, max |Φ(law) − Φ(glued)| = 0.0, max I(P;Q|Y) under glued laws 5.9×10⁻⁶⁰; Φ_bad negative on 208 of 300 laws (min −0.184).

## 4. Findings

- **FATAL:** none.
- **MAJOR:** none.
- **MINOR-1 (wording, non-blocking).** Input 1 says the identity "then expresses the unchanged Φ as eight nonnegative CMIs"; for rigour it should say the eight CMIs are those of the *glued* law (they differ from the original law's CMIs, see §2.3). The argument as written is correct because only Φ, not the individual CMIs, is transported between the laws.
- **MINOR-2 (scope hygiene, non-blocking).** The provenance paragraph (12-variable extension, 67,596 rows, I(P;Q|X)=12599/34500, 45,360 substitutions) and four non-input SHA-256 values are unverified by this review and are not needed for C1–C6; input 1 already states they are not premises. Any downstream consumer must not treat them as reviewed.
- **MINOR-3 (checker coverage, non-blocking).** The author checker (read only) ties the JSON coefficient list to its hard-coded CMI rows and checks mixed-term cancellation and the elemental system, but it does not machine-tie the markdown's displayed 16-term inequality or the markdown's displayed 64-entry table to the JSON; that agreement is established here by independent transcription (receipt §B: both `true`).
- Observation (no finding): the witness is a boundary point of Γ₆ (61/246 tight), and Φ has zero coefficient sum in every variable.

## 5. Decision

**MINOR.** C1–C6 are independently reconstructed and exactly confirmed at the manifest's scope. The reviewer's own identity/witness checker, finite-law gluing example, mutation controls (wrong coefficient, wrong conditioned sets, swapped roles, dropped row, witness perturbations) and random sweep all behaved as required, with receipts and hashes above. No author code was executed.

## 6. Exact scope — established vs. not established

Established by this review (same-harness, exact arithmetic and written proof):
1. Φ ≥ 0 holds for every finite joint law of six finite random variables and on closure(Γ*₆); the conditioned form Σ c_S H(S∪Z) ≥ 0 holds for any further finite Z.
2. The listed r/6,900,000 is a polymatroid (verified against the defining axioms and the 246 elemental inequalities) with Φ(r) = −12637/1,725,000 < 0; hence Φ ≥ 0 is not implied by the six-variable Shannon inequalities (not a nonnegative combination of elemental inequalities), i.e. non-Shannon-type for n=6 in the cone-separation sense; corollary r ∉ closure(Γ*₆).

Not established, not examined, and not to be inferred from this review:
- Novelty of Φ, or whether Φ follows from known non-Shannon inequalities (e.g. instances of four-variable non-Shannon inequalities with auxiliary variables) — not tested, by manifest instruction.
- Any guessing-number bound, any graph-specific statement, any entropic realisation of any vector, the 12-variable provenance/correspondence, or resolution of the original R-minus target.
- Optimality of the coefficient −2 (only −3 was shown false; intermediate values were not tested and no claim depends on it).
- Human, independent-model-family, or formal/kernel verification.

## 7. Artifacts written by this review (all prefixed `proof-`, this directory only)

`proof-review-v1.md` (this file), `proof-identity-and-witness-check-v1.py` + `-receipt.json`, `proof-finite-law-gluing-example-v1.py` + empty failed `-receipt.json`, `proof-finite-law-gluing-example-v2.py` + `-receipt.json`, `proof-extra-controls-v1.py` + empty failed `-receipt.json`, `proof-extra-controls-v2.py` + `-receipt.json`. Hashes in §3; the hash of this file is recorded by the parent at delivery. Working directory, environment: macOS, Python 3.14.3, mpmath 1.4.1; all files created with shell `noclobber` (exclusive creation), none edited after creation.
