# Hostile review: standalone G-LS (`proof-general-LS-Lev-v1.md`, bc4f4c70…, lines 1–206)

I reviewed the proof by hand against the embedded interface ranges, overlays and verdicts. I used no tools or computation and did not read the primary source. The parent lead and the pending BASE2/NORM/PIN/P1–P3/LS-lin bodies were not used, and no line of the proof relies on them.

## Verdict

**G-LS: ACCEPT-WITH-FIXES, conditional.** FATAL 0, MAJOR 0, MINOR 3, plus one optional observation. Every fix is citation or wording. No statement, inequality or case split changes. I found no invalid import domain and no algebraic or occurrence-level gap.

- **e = 2 (κ = p−2):** valid on accepted internal imports alone. Lev is never invoked.
- **e ≥ 3:** valid on accepted internal imports plus Lev 2022 Theorem 2 *as transcribed* in c2cb60cc lines 17–24. The theorem is used as an explicit statement-level premise and is not strengthened (see §4).

## 1. Interface audit (original scopes plus mandatory overlays)

| Interface | Original scope | Use in G-LS | Status |
|---|---|---|---|
| RED (+E-2, M-8) | p≥5, 0≤κ≤p−2 | LS fails ⇒ a counterexample of length exactly thr exists | In scope, since κ≥κ0+1≥5. The argument is a minimal counterexample, and the shrink step is the contrapositive of PROP. Failure of (S1) is never claimed hereditary. |
| CF(a) (+E1) | p≥5, 0≤κ≤p−1, any odd generator | (ZP) ⇒ (F) for g0, with δ0=d | In scope. CF(b)/(L) is never used: σ(W*)≡−j is re-derived from ord g=2p, so R4 is moot. |
| DGM-p (+E4) | (p−3)/2≤κ≤p−1 | unique generator g0 with M≥2κ+3 | In scope. |
| Threshold dichotomy (+E3/E4) | exactly κ0+1≤κ≤p−2, \|Y\|=thr, g=g0 | only "(I) ⇒ δ0≤e−2" | In scope. |
| LS-II′ (+D-1) | p≥7, κ0+1≤κ≤p−2, threshold Y with a long zero-sum, relative to g0; no H′ or SH | excludes case (II) | In scope. |
| AP (R6) | n≥1, 3n<p, arc ≤2n | N=e−1−⌊δ′/2⌋≥e/2≥2, 3N≤3e−6<p, l≤2N | In scope. I re-derived the R6 proof. |
| AP′ (D1, D-2) | n≥1, 3n+2<p, arc ≤2n+1 | N=e−2, 3e−4<p, l≤2e−3 | In scope. I re-derived the D1 proof. Authority wording is finding m1. |
| SLZ3 (+erratum) | p≥5, κ0+1≤κ≤p−1; bounds only the shortest long \|T\| | \|T\|≤3κ+1 | In scope and never used to bound \|Y\|. It is dispensable (O1). |
| Lev Theorem 2 | external | applied to U′ over C_p | Premise; see §4. |

## 2. Step verdicts

**§0 Statement and ranges: ACCEPT-WITH-FIXES (m1, m2).**
- e≥2 and 3e≤p−1. For p≡1 (mod 3), e≤(p−1)/3; for p≡2, e≤(p−2)/3.
- κ0+1≥5 whenever p≥7.

**§1 Threshold, e=2, F\*, Z0: ACCEPT.**
- |Y|=3p−2e+1 and d≥1. Case (I) plus LS-II′ gives 1≤d≤e−2.
- At e=2 this d-range is empty. The contradiction therefore arrives before any Z0, Lev or AP′ call, so an N=0 call never arises. This matches the accepted LS(p,p−2).
- F\*: |W|+2ρ≤r+2h=p−1+d<2p. So CF(F) forces |W|+2ρ≤d−1 exactly when ρ≤h, including W=∅.
- A maximal Z0 gives k≤d−1, a zero-sum-free U′, and n=p−2e+1+δ′. F′ follows from the disjoint union with Z0.

**§2 Few-sums bound and Lev: ACCEPT.**
- Avoiding [t,h] needs 2t+2>δ′. This holds for t=max(1,⌊δ′/2⌋) at every δ′≥1, and t≤h.
- So |Σ_inc(U′)|≤p−e+t, and 2n−(p−e+t)=p−3e+2+2δ′−t≥1+2+δ′≥**4 for every δ′** (the minimum is at δ′=1).
- Lev's hypotheses hold: U′ is zero-sum-free and n≥e+3.
- a≠0 because the terms are nonzero. Hence ord a=p and S<p.
- Coefficient interval: any representing subset has x-sum in [0,S]⊂[0,p−1], so the lift is unique at occurrence level.

**§3 Pinning: ACCEPT.**
- For ρ∈[t,h], the point ρb lies in I=[S+1,p−1]. S=p−1 is impossible, and l≤2e−2−δ′.
- **δ′≥2 (forces e≥4):** l≤2N because 2⌊δ′/2⌋≤δ′. AP gives b=±1. b=1 puts the ρ=t point at t≤h<n≤S, outside I.
- **δ′=1:** N=e−2≥1 and l≤2N+1. AP′ gives b∈{±1,±2}.
  - b∈{1,2} fails at ρ=1.
  - b=−2 fails at ρ=h, since p−2h=n≤S.
- **e=3:** forces d=δ′=1, k=0, N=1, p≥11.
- Hence a=−1 in the original μ-coordinates, with no translation, and S≤p−e.

**§4 Localization and positive crossing: ACCEPT.**
- 1≤R≤e−δ′≤h.
- Since S+h≤p−1, the bands [1,h−1], [h,S+h] and [S+h+1,p−1] exhaust [1,p−1].
  - Middle band: excluded by {z}∪W′_{ζ−h}, which has disjoint occurrences and residue h.
  - Left band: ζ≤⌊(d−2)/2⌋.
  - Right band: ν∈[1,R−1], which is empty iff R=1. There are no positives when d≤3.
- First crossing: j0≥2 and P_{j0}≤d−2≤h−3. The integer sum is therefore the least residue, contradicting F\*.
- Conclusion: q+2P≤d−1 and P<h.

**§5 Negative crossing: ACCEPT.**
- N_V∈[R,2R−2], and s=p−N_V−h lies in [p−3e+3+2δ′, S]⊂[1,S].
- V∪W′_s has actual least CF residue h. Signed sums enter only through the congruence. This contradicts F\*.
- The cases Z⁻=∅ and R=1 are trivial.

**§6 Witness: ACCEPT.**
- |T|=2p+2j with 1≤j≤J=⌊(p−3e+1)/2⌋, and J≥1.
- From i+|W\*|+2σ≡0 (mod 2p): σ≡−j (mod p) and |W\*|≥d+2j.
- No j=1 assumption, no use of L1, and no |Y| bound taken from SLZ3.

**§7 Signed lift and contradiction: ACCEPT (m3 is wording only).**
- τ=ζ̃−s lies in [−p+h+1, P].
- Lifts of −j: −j−p<−p+h+1, and p−j>h>P because j≤J<p−e+1. Hence τ=−j.
- Then d+2j≤|W′|+ℓ≤s+ℓ, so ζ̃≥d+j−ℓ≥j+1≥2. Since ζ̃≤P<h, Z\* is nonempty with ρ(Z\*)=ζ̃.
- ℓ+2ζ̃≥d+j+ζ̃≥d+3>d−1. This contradicts F\* on an actual occurrence subset.
- RED then closes every |Y|≥thr.

**§8 Boundary statements: ACCEPT.** They are accurate and do not overclaim.

**Endpoint sweep (no counterexample found):** δ′=1 versus δ′≥2; e=3 and e=4; d≤3; Z0=∅; Z⁻=∅ and R=1; S=n and S=p−e; j=1 and j=J.

## 3. Findings and minimal fixes

**FATAL:** none. **MAJOR:** none.

**m1 [import authority, not domain].** The embedded ac8ead13 lines 7–16 accept LS-small and "Proposition I-small … with corrected AP-prime proof". They do not list Lemma AP′ as a standalone accepted statement, but proof lines 51–54 treat it as one.
- **Fix:** cite the parent line that admits AP′ standalone, if one exists outside lines 7–16. Otherwise have the parent admit it explicitly (statement: smalldelta-v1 lines 30–31; proof: D1).
- **Why it is not blocking:** I re-derived D1 for all n≥1, 3n+2<p, l≤2n+1, including degenerate arcs. The instance used here, n=e−2 with 3e−4<p, is the same one D-2 m2.1 records inside the accepted I-small.

**m2 [citations].** Proof §0 and the package table disagree on line ranges:

| Source | Proof §0 | Package table |
|---|---|---|
| RED | 96–101 | 91–101 |
| ROW | 29–37 | 10–37 |
| SLZ3 | 10–18 | 10–30 |
| LS-II′ addendum | 6–8, 10–26 | 1–26 |

- **Fix:** align §0 with the governing v2 manifest. This has no mathematical effect.

**m3 [wording, lines 184 and 187].** At j=1 the lift p−j=p−1 lies outside the stated open interval (−p,p−1). The listed candidates are still a valid superset, so the conclusion stands.
- **Fix:** write "among integers ≡−j (mod p), only −j and p−j can lie in [−p+h+1,P]⊂(−p,p); and p−j>h>P."

**O1 [optional, not a defect].** Neither SLZ3 nor the minimality of T is needed.
- Any long T⊆Y has 2p+2j≤3p−2e+1, so j≤⌊(p−2e+1)/2⌋ and p−j≥(p+2e−1)/2>h.
- §7 uses only j≥1, p−j>h and (12).
- The current text is correct and in scope; dropping SLZ3 would remove one interface.

## 4. External-import and trust boundary

- **Sole new premise (e≥3):** Lev, arXiv:2110.01081v3, §1 Theorem 2, exactly as transcribed in c2cb60cc lines 17–24.
  - I have not authenticated the transcription. The hash c2cb60cc binds the local notes, not the remote bytes.
  - Lev's proof is not replayed.
  - G-LS at e≥3 is exactly as trustworthy as that statement.
- **What the proof actually consumes:**
  - Hypothesis: α zero-sum-free in C_p with |Σ_inc(α)|<2|α|, and *no length hypothesis*.
  - Conclusion: α_u=x_u·a with integers x_u≥1, Σ_inc(α)={0,a,…,Sa}, and S=Σx_u<ord(a).
  - The facts a≠0, ord a=p, n≤S and the occurrence-level interval are derived in §2, not imported. Nothing is silently strengthened.
- **Robust to likely transcription slips:**
  - Inclusive versus nonempty Σ, and strict versus non-strict inequality: the margin |Σ_inc(U′)|≤2n−4 absorbs both.
  - The "no +1" recurrence and the ordering are unused. The Σ-equality and S<ord(a) would follow equally from the "+1" form with x_1=1 plus zero-sum-freeness.
- **Load-bearing and not checkable here:** the absence of a length hypothesis.
  - For e≤5, every application has n>p/2.
  - At (p,κ,δ′)=(19,13,1), however, n=9<p/2. A half-order hypothesis like Theorem 1's (per the record) would not cover G-LS.
  - The parent's primary re-read must confirm this clause specifically.
- **Internal interfaces:** these are accepted at their original scopes and carry their own transitive imports (Cauchy–Davenport via RS; RED's SLZ/EXT/PROP chain; SLZ3's S1-sharp/S1+/index-one). They are not replayed here, except AP (R6) and AP′ (D1), which I re-derived.

## 5. Conditional coverage check (separate; not a G-LS input)

**YES.** If G-LS is accepted, S1-sharp (bd4a0a60) together with G-LS covers the entire original LS definition, with no missing endpoint.

- **p=5:** κ0=3=p−2, so S1-sharp covers κ=0..3, which is every original cell. The G-LS interval is empty at p=5 (κ0+1=4>3), so its p≥7 restriction loses nothing.
- **p≥7:** [0,κ0] ∪ [κ0+1,p−2] = [0,p−2].
  - κ0≤p−3, so the S1-sharp block sits inside the original domain and meets G-LS at κ0/κ0+1.
  - κ=0 is covered by S1-sharp.
  - κ=p−2 is covered by G-LS at e=2, which is Lev-free and also matches the accepted LS-small.
  - At p=7 the G-LS block is only κ=5 (e=2), so p=5 and p=7 are covered without Lev.
- **Statement match:**
  - S1-sharp has no length hypothesis. Adding |Y|≥p+2κ+1 yields LS(p,κ), and its conclusion "every zero-sum has length ≤2κ" is (S1_κ).
  - G-LS is LS(p,κ) verbatim.
  - Z_(2p) versus C_(2p), and subsequence versus occurrence subsequence, differ only in notation.
- **Mismatches:** none in primes, κ-range, endpoints or statement form.
- **Caveat:** the two blocks rest on different trust bases, since the e≥3 cells of G-LS also depend on Lev. This is a range and statement comparison only, not a reviewed assembled theorem.
