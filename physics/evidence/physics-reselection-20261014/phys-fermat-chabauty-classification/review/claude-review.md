# Referee report: universal proof in `RESULTS.md` (Chabauty limits of Fermat spirals)

## Verdict: **CORRECT-WITH-FIXES**

I found no mathematical gap or error anywhere in the proof of Theorems 1–2 (`RESULTS.md:13-21`). All required fixes are about prior art, attribution, quotation and wording. This is a written audit done by a model. It is not a Lean or kernel-checked certificate.

**What I read:** README.md, STATUS.md, RESULTS.md, both pinned PDFs in full (Tevet v2, pp. 1–13; Bacher, journal pp. 3–27), both OpenAlex JSONs, and manifest.json.

**What I did not read or check:** `source/problem.zh.txt` and `review/` (outside the authorized set), and code/finite controls (outside scope). I did not recompute the SHA-256 hashes because I ran no commands.

## Findings, by severity (none affects Theorems 1–2)

**1. Moderate: Bacher's Remark 1.2 is missing from the overlap analysis.**
- Bacher journal p. 5 (PDF p. 4), right after Theorem 1.1:
  - Remark 1.2(2): "if θ is irrational we have lim vol V(n) = π" (V(n) is the Voronoi cell of the n-th point).
  - Remark 1.2(1): for rational θ the local lattices degenerate into rank-1 subgroups.
- Bacher p. 12 calls Prop 6.1 "a straightforward consequence" of the Voronoi areas tending to π. Bacher p. 10 links large partial quotients a_k to cusp excursions with bad Voronoi cells, which is the thin-lattice mechanism.
- My own inference (not stated by Bacher): along a lattice limit, Voronoi cells converge to the limit's cell. So Remark 1.2(2) already asserts, without proof in the remark, a yes answer to the covolume question for every irrational angle.
- `STATUS.md:35-44` and `RESULTS.md:101` cite only Thm 1.1, Prop 3.1/Cor 3.2, Rem 3.3 and Prop 6.1. `STATUS.md:55` nonetheless says the relevant sections were read in full.
- **Fix:** add these remarks to STATUS §3. At `RESULTS.md:23`, change "answers the p. 12 covolume question" to "gives a complete proof of the affirmative answer, which Bacher asserted in Voronoi-area form."

**2. Moderate: the target paper's own YSS21 pointer was not screened.**
- Tevet p. 10, Remark after Prop 12: covolume π "clearly follows from the main result" of [YSS21] (Yamagishi–Sushida–Sadoc, *Nonlinearity* 34, 2021), "where they prove that the area of Voronoi cells converges to π."
- YSS21 does not appear in STATUS §§3–4. Its hypotheses on α cannot be checked from the pinned files. If they include non-BA α, it already covers the covolume part.
- **Fix:** list YSS21 as directly relevant prior art that was not inspected.

**3. Low: Bacher's Prop 6.1 is cited as a proved theorem, but Bacher gives no proof.**
- Bacher p. 13: "We leave the proof to the reader."
- The citation appears at `RESULTS.md:206` and `STATUS.md:40`.
- **Fix:** cite Akiyama 2020 (*Nonlinearity* 33, 2533–2540, via Tevet pp. 1 and 4) as the proof source, marked uninspected. Only the optional "BA has no empty limit" sentence depends on it.

**4. Low: several steps repeat arguments from the pinned sources without credit.**
- Rational case: Tevet p. 2, "It is easy to show … the empty set and lines" (`RESULTS.md:200`).
- Relative density passes to limits: Tevet Prop 4, p. 3 (`RESULTS.md:178`).
- Non-BA spirals are not relatively dense: Akiyama, via Tevet Cor 7.
- Choosing the limit's angle by shifting the index (using density of e^{2πiαb}): Tevet's proof of Thm 2 part 2, p. 11 (`RESULTS.md:184-196`). The o(n)-window version in RESULTS is cleaner but has this precedent.
- The constant √(1/4+4π²) at `RESULTS.md:153` is Bacher Cor 3.2. The bound ℓ² ≤ 2A/√3 at `:113` is Bacher Rem 3.3's √(2π/√3).
- The BA statements are Tevet Cor 5, Thm 2 and Prop 12.

**5. Low: the p. 12 quote cuts off its antecedent.**
- `STATUS.md:13` omits the sentence before it on Tevet p. 12: "As noted above, the author conjectures that the limits are isomorphic to ∅, R, Z², and Z × R."
- Without that sentence, the quote does not show that "they are all achieved" includes Z × R.

**6. Low: wording.**
- "Confirms the no-plane part" (`RESULTS.md:23`) undersells the result. Theorem 1 proves the whole p. 4 containment: every nonempty limit is of type R or Z².
- "The only … are A, B, C" can also be read as an exact list. Phrasing that works under both readings: "proves the p. 4 containment in sharpened form; Z × R never occurs, contrary to the p. 12 computational suggestion."
- Otherwise, the distinction between the conjectured containment list and the attainability suggestion (`STATUS.md:17`) is correct.

**7. Low: standard facts used implicitly.** I checked each one and all hold; a one-line justification for each would make the text self-contained.
- Tevet's metric (p. 2) is equivalent to the full-set formulation at `RESULTS.md:11`.
- Translating a closed set by a convergent vector, or applying a convergent invertible matrix, is continuous in this topology (`RESULTS.md:131, 188, 196`).
- The liminf-over-convergents definition of BA is equivalent to inf_q q‖qα‖ > 0 (`RESULTS.md:202`).
- §7 needs an explicit h_j (for example ⌊√n_j⌋) and a diagonal choice of ε_j.

**8. Low: labels not supported by the read set.** The "Certification" label for finite controls (`RESULTS.md:219`) and the book-bridge excerpt cannot be checked from these files. Keep both pending.

## Steps I checked independently

1. **The local lattice L_n.** Its basis determinant is −π for every real α, so it is always a genuine lattice. Bacher's (3.1) generators are exactly v_n(q_{j−1}, p_{j−1}) and v_n(q_j, p_j), using δ_k = (−1)^k θ_{k+2}/(q_k + θ_{k+2} q_{k+1}) from Bacher p. 9. The two lattices are equal as sets.
2. **Lemma 2.1 (forward inclusion).**
   - |q| ≤ n/2, so n + q ≥ 1.
   - |qα − p| ≤ 1/(8π), so p is the unique nearest integer.
   - The identity a = u + u²/(2r) and the bound |u| ≤ 2|a| hold.
   - The three-term identity checks algebraically, and the error is at most 3R²/r.
   - The sign of q plays no role.
3. **Lemma 2.2 (reverse inclusion).**
   - The 25R/24 bound holds.
   - Re(r + z) > 0, so the principal argument lies in (−π/2, π/2). This gives |qα − p| < 1/4, with no lift ambiguity and no half-integer tie.
   - |b| ≤ 12R/11 and |v| ≤ 563R/264 < 3R.
   - z is exactly the Lemma 2.1 point for the same (q, p), so the error is at most 45R²/r.
4. **Corollary 2.3.** Both directions go through using neighbourhoods of the full other set, so nothing goes wrong at the ball's boundary. The error does not need to be small relative to the lattice spacing.
5. **Lemma 3.1.**
   - The shortest vector is primitive; the basis extension, reduction and the bound ℓ² ≤ 2A/√3 are correct.
   - Thick case: the limit is exactly BZ² with covolume A, not a sublattice or superlattice.
   - Thin case: points off the shortest line are at least A/ℓ_j → ∞ away from it, so the limit is a line.
   - The two cases cover every subsequence, which rules out a point, Z, R × Z and R².
6. **§4 (recentering).** n_j → ∞, and the shifted sets converge to Y − y. The argument does not use Tevet's Thm 1 or Prop 8.
7. **§5 (lattice limits).** |δ_j| < 1/q_{j+1}. At n = q_j², both basis entries are bounded as claimed and the determinant is ±π.
8. **§6 (lines and empty limits).** The exact identity πq|δ|(N/n + n/N) holds and tends to 0. The relative-density transfer is valid, and the points c_j used for the empty limit escape to infinity.
9. **§7 (orientation).** The diagonal identity is exact. The pigeonhole argument gives an ε-dense set of phases with a window length that does not depend on n. Only translations are used.
10. **§8 (rational and BA).**
    - Rational: the shortest vector is b/(2r), and all other vectors have vertical component at least 2πr/b.
    - BA: |v|² ≥ 2πc.

Quotes and metadata: the quotes at `STATUS.md:9,13` match the PDF verbatim, and the publication metadata matches the OpenAlex JSON (citing works: 0). The acceptance date at `STATUS.md:21` cannot be verified from the pinned files.

**Unproved or imported steps:** none in the chain of Theorems 1–2. The only imported result is BA ⇒ relatively dense, which is optional.

## Prior-art assessment

- **No pinned source explicitly states this exact non-BA classification.** Tevet poses it as a question; Bacher never uses Chabauty limits or mentions R × Z.
- **Bacher's 2014 paper already contains most of the ingredients:** L_n itself, area π, the uniform approximation, both length bounds, the rational degeneration and the Voronoi-area assertion.
- **What is actually new here:**
  - explicit two-sided error constants, with a rigorous way of picking p (principal argument);
  - the exclusion of R × Z;
  - all affine lines and the empty set realized for every non-BA α, using translations only.
- **"Classical corollary / quantitative certification" is honest wording.** Once Findings 1–2 are added it is also accurate.
- **The zero-citation result is correctly not used as evidence of priority** (`STATUS.md:57`).

## Strongest defensible wording

> For every real α, every nonempty translation-only Chabauty limit of X_α is an affine line or an affine lattice of covolume exactly π. Every irrational α has a covolume-π lattice limit. For every irrational non-BA α, the empty set and every affine line also occur. This proves Tevet's p. 4 containment in sharpened form and answers the p. 12 covolume question. It also shows that Z × R, suggested on p. 12 to be attained, never occurs. The proof is an explicit quantitative form of Bacher's 2014 linearization (Thm 1.1, Cor 3.2, Rem 3.3; Rem 1.2(2) already asserts that Voronoi areas tend to π) combined with elementary compactness of fixed-covolume planar lattices. No priority is claimed; YSS21 and Akiyama 2020 were not inspected.

`★ Insight ─────────────────────────────────────`
- Tevet's computer pictures likely showed "Z × R" because of finite windows. When the shortest vector has length ℓ, the parallel rows are π/ℓ apart. With a small but fixed ℓ, a window sees several dense rows. In the limit, either ℓ stays bounded below (giving a lattice) or ℓ → 0, so the rows separate infinitely far (giving one line). An exact covolume of π rules out anything in between.
- Measuring closeness against the *whole* other set, rather than comparing the two sets inside the same ball, is what lets 45R²/r → 0 suffice even when that error is far larger than ℓ.
`─────────────────────────────────────────────────`
