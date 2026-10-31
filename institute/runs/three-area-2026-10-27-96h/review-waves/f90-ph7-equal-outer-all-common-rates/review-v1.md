# review-v1 — f90-ph7-equal-outer-all-common-rates

Same-harness independent scientific review (Claude reviewer subagent of Main; not the author MathResearch96h-2). Binding manifest: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f90-ph7-equal-outer-all-common-rates/manifest-v1.json`, SHA256 `ce59823f3012236a5ce61c6566d204c4dc29e0539e54252588120839d4a0fb61` (version 1, no successor). Authority: `contract-addendum-2-frontier-first-owner-direction-v1.json` (fresh exact local computation permitted). Native clock observed with `/bin/date` immediately before this file was composed: **2026-10-28T19:53:55-0700 PDT**.

## 0. Verdict

**Candidate** `frontier-20261028-ph7-equal-outer-all-common-rates-critical-exclusion-v1.md` (pinned SHA256 `4e3dc5292f40e0d16dba0f57a4b106956ce78ae35d1d3cdcfdb680376981f9f3`, 9087 B, 111 LF).

**FATAL 0 · MAJOR 0 · MINOR 2** on the candidate, plus one process finding on the manifest (§1).

- The candidate's own new content — the five-rate coefficient elimination to `(s1,V)`, the `s>4` deduction, the Newton/Hankel sign necessity, and the exact two-variable open sign decomposition (23 projections, 17 factors, 25 positive roots, 26 base intervals, 82 cells) — is **independently replayed end-to-end with reviewer-written standard-library code and found correct**. The ≥3-distinct-common-rate branch of the theorem is verified unconditionally.
- The ≤2-distinct-common-rate branch rests on two named imports that are **not verified in this review** and have no review wave of their own under `review-waves/`: the two-valued theorem (`3daac4b2…`) and, transitively, its `4+1` import (`frontier-20261028-ph7-asymmetric-two-cycle-critical-exclusion-v1.md`, `2a9b73522733534d3082fab05b8760f1663c19429fb05c348ee571f75955df54`). The headline "for ALL five positive common rates" (LF7, LF111) is therefore verified **conditional on those imports**, exactly as the candidate declares at LF17.
- Scope of this review and of the result: **equal outer rates only; one eight-edge shape only (the 5-/7-cycle theta graph); `z=8/9` only.** Nothing is asserted about unequal outer rates, the other 13 eight-edge shapes, ≥9 transitions, unrestricted PH7 feasibility/exclusion at 8/9, minimum 8, or novelty. Same-harness review is not external-family, human, formal or novelty verification.

## 1. Inputs, hashes, process finding

Fresh SHA256 of every manifest input was computed before reading (`shasum -a 256`); all six equal the manifest `sha256` field, byte counts and LF counts:

| # | role | fresh SHA256 == manifest `sha256` | bytes/LF |
|---|------|---|---|
| 1 | PH order definitions `math-1-ph-order-definitions-v1.md` | `a4db7478…82e85` ✓ | 1534/17 |
| 2 | candidate | `4e3dc529…5d1d3cdc…f9f3` ✓ | 9087/111 |
| 3 | primary CAD checker `…open-cad-check.py` | `a16e89e7…1083` ✓ | 6504/139 |
| 4 | certificate `…open-cad-certificate.json` | `ebe39f83…0890` ✓ | 32782/1424 |
| 5 | stdlib Fraction replay `…open-cad-fraction-replay.py` | `78a93dee…105b` ✓ | 9373/205 |
| 6 | two-valued dependency `…two-valued-common-rates-critical-exclusion-v1.md` | `3daac4b2…7685` ✓ | 6678/77 |

**P1 (process, MINOR; manifest, not candidate).** The manifest's `expected` field for the candidate reads `4e3dc5292f40e0d16dba0f57a4b106956ce78ae35d1d7cdcfdb680376981f9f3` and `match:false`; it differs from the manifest `sha256` and from the fresh on-disk hash in exactly one hex digit (position 45: `7` vs `3`). The author's own later file `frontier-20261028-ph7-near-equal-outer-critical-gap-v1.md` LF20 cites the `…5d1d3cdc…` value, and Main's additive correction `checkpoints/056-f90-hash-transcription-correction-v1.json` (SHA256 `b0723d5585d7e3af43f38a91a9f544eadc279b1ba81aad9054b8a03fd0c7e83e`, hash verified by me) records that the author-reported digest equals the pinned and live hash and that the `expected` field is a transcription error made at manifest creation. Classification: **reported-digest transcription error; NOT source drift** — the pinned bytes are unchanged and were reviewed exactly as pinned. Checkpoint 056's phrase "does not match author-stated SHA" is superseded by that correction.

Additional read: the transitive import `…asymmetric-two-cycle-critical-exclusion-v1.md` (6931 B/90 LF, fresh SHA256 equals the value cited in input 6) was read raw **for scope matching only** (§3.8); it is not treated as verified. A grep of the run directory and evidence directory found no hold/withdrawal/quarantine naming either dependency file; no held body was used as a premise. No author contact; no writes outside this review directory; no external model or paid API; no Git; no deletion.

## 2. Reading receipt

All six inputs were read completely, in manifest order, in `:raw` windows before any computation or verdict (certificate in five raw windows: LF1–120, 120–420, 420–760, 760–1100, 1100–1424). Author scripts were read but never imported or executed.

## 3. Reconstruction (reviewer's own)

3.1 **Determinant structure (LF21–26).** The theta digraph (shared 4-edge path; return edge `b→a`; return path `b→e1→e2→a`) has exactly two directed cycles and no vertex-disjoint cycle pair, so the permutation expansion of `det(yI−M)` has the diagonal term and the two cycle terms only. Both cycles are even permutations; the products of 5 resp. 7 off-diagonal entries `−m_ij` give `−D1(y+V)²` and `−D3`. So `P(y)=A(y)(y+V)²−D1(y+V)²−D3` with `D1,D3>0` for positive edge weights. ✓

3.2 **Elimination (replay Part A).** With `D(y)=y[(y+1)²+8/9]²=y⁵+4y⁴+(70/9)y³+(68/9)y²+(289/81)y` and `Q=y²+py+q`: the `y⁶,y⁵` equations give exactly `p=s+2V−4`, `q=s2+2Vs+V²−4p−70/9` (LF28–29 ✓); `y⁴,y³` give (COEF) for `s3,s4` ✓; `y²` fixes `D1`; the `y¹` equation with `D1` substituted is independent of `s5` and `D1` and equals **`−(1/729)·(9V²−18V+17)·L`**, where `L` is the bracket displayed at LF38–39 — the displayed "`=0`" equation is exact (the constant is immaterial). `9V²−18V+17=9(V−1)²+8>0` and `d=45V²−54V+17=45(V−3/5)²+4/5>0` (LF41–44 ✓), so `s2=A2/(9d)` uniquely, with `A2` exactly as displayed at LF47–48 ✓. `A3=9d·s3` and `A4=81d·s4` were rebuilt from (COEF) and agree with the certificate. (LONG) LF52–53: `81d·(T2−2Vs4−V²s3)=(s−4)[9(V−1)²+8]³` holds as an exact polynomial identity, and the `y⁰` equation gives `81d·D3=V²·(s−4)[9(V−1)²+8]³`; with `D3>0,V>0,d>0` this forces `s>4` (LF55 ✓).

3.3 **Constraint polynomials (Part B).** The six polynomials reconstructed from scratch are identical to the six certificate strings (parsed by my own AST walker, no `eval`); degrees in `(s,V)` are `(1,0),(1,3),(1,4),(1,5),(2,8),(4,10)` (LF84 ✓). Verified as symbolic identities: `N=9(9d)²(s3²−2s2s4)`; `H=(9d)³·det[[5,p1,p2],[p1,p2,p3],[p2,p3,p4]]` using the Newton identities for `p2,p3,p4` (verified for five variables); the Newton normalisation `e3²≥e2e4 ⇔ s3²≥2s2s4` (LF60 ✓); and the Cauchy–Binet identity `det = Σ_{i<j<k}[(u_j−u_i)(u_k−u_i)(u_k−u_j)]²` (verified symbolically in `u1..u5`), which proves LF64: the Hankel determinant is `>0` iff at least three distinct rates occur and `=0` for at most two.
**Strict Newton (LF64 "strict for non-equal positive rates") — own argument.** Let `F(x,y)=∏(x−u_i y)`. `∂_y²∂_x F` is a binary quadratic form whose discriminant is `(5!)²(e3²−e2e4)`. Each partial derivative preserves real-rootedness (Rolle on the dehomogenisation; since all `u_i∈(0,∞)` no root sits at 0 or ∞ and every Rolle root lies strictly between existing roots, so this persists). A real-rooted binary form of degree `m≥3` that is not a power of one linear form has a derivative that is not a power either: with ≥3 distinct roots Rolle gives ≥2 distinct roots; with exactly 2 distinct roots one of them is multiple (as `m≥3`) and remains a root of the derivative, distinct from the Rolle root. Starting at degree 5 with not-all-equal `u_i`, three derivatives give a quadratic with two distinct real roots, so `e3²>e2e4`, i.e. `s3²>2s2s4` for all not-all-equal positive rates, in particular for ≥3 distinct ones. Exact random sanity on 400 tuples (2–5 distinct values) agreed, and the all-equal tuple gives equality.

3.4 **Projection (Part C).** Own Sylvester matrices and fraction-free Bareiss determinants over `Q[V]`; `disc=(−1)^{n(n−1)/2}Res(f,f')/lc`. 23 projection polynomials (6 leading coefficients, 2 discriminants, 15 pairwise resultants incl. with `s−4`), all nonzero, `V`-degrees: lead 0,3,4,5,8,8; disc 14 (newton3), 56 (hankel3); resultants 2,2,2,4,6,6,7,12,20,7,13,23,14,26,46 — maximum 56 ≤ the author's bound 60 (LF103 ✓). **Each of the 23 equals `scale·∏ factor^mult` as an exact polynomial identity, including the sign of `scale`**, with the 17 certificate factors (degrees 1,2,3,4,4,5,5,5,5,5,6,8,14,17,20,34,40), which are pairwise distinct, primitive, nonconstant and all used. Irreducibility of the factors is neither needed nor checked: the identity alone implies that the positive roots of the projections are exactly the union of the positive roots of the factors.

3.5 **Projection roots (Part D).** Own Sturm chains (content-only normalisation; see §6) give positive-root counts per factor `[0,0,1,0,0,1,1,1,1,1,2,3,2,1,0,2,9]`, total **25**; own bisection isolators refined to pairwise disjoint (hence 25 distinct roots); every certificate isolator verified (`0<lo<hi`, endpoints non-roots, exactly one root); the certificate's isolators are pairwise disjoint; its ordered root table is consistent with its factor tables; my isolators align one-to-one with the certificate's; **26** open base intervals.

3.6 **Section census (Part E).** For each base interval I used **two** base points: the certificate's `V` and a reviewer-chosen one (`hi/3`; `lo+(hi−lo)/3`; `lo+2` for the unbounded interval), none a projection root. At each: the specialised degrees stay `1,1,1,1,2,4`; all `s`-roots `>4` of the five nontrivial polynomials isolated by own Sturm/bisection and refined to disjoint; cells `(4,r₁),(r₁,r₂),…,(r_m,∞)` sampled at own points; all six polynomials nonzero there. **Every cell has at least one strictly negative constraint.** Cells per base interval `3,2,4,6,4,6,5,5,3,3,3,3,4,2,3,5,3,1,1,1,1,2,2,3,3,4` — **82** at the author's base points and **82** at mine; root-curve orders and negative sets are identical at the two base points of every interval (consistent with delineability). Negative-set histogram over the 82 cells: `{hankel3}:30, {newton3,hankel3}:27, {newton3}:16, {s4,hankel3}:5, {s2,s4,hankel3}:3, {s2,s4,newton3,hankel3}:1`; `A3` is never negative. The certificate's recorded `s_roots` (counts and isolators), `samples` (in-cell) and `negative_constraint_index` values were all verified.

3.7 **Delineability and strict boundary (LF86) — own reasoning.** On an open base interval containing no root of any leading coefficient, discriminant or pairwise resultant (including the resultants with `s−4`), each polynomial has constant `s`-degree, simple roots depending continuously on `V`, no two root curves of distinct polynomials meet, none crosses `s=4` or escapes to infinity; so the sign vector is constant on each cell and the structure at one base point is the structure over the interval. The feasible set `{V>0, s>4, A2,A3,A4,N,H>0}` is open; the complement of the union of open cells (25 vertical lines and finitely many continuous root curves) has empty interior; a nonempty feasible set would therefore meet an open cell, contradicting 3.6. ✓

3.8 **Case split (LF64, LF88).** ≥3 distinct common rates ⇒ `s>4, A2,A3,A4>0, N>0, H>0` necessary ⇒ impossible by 3.4–3.7. ≤2 distinct ⇒ imports: the two-valued file covers `3+2` (its theorem needs only `U>0`), and its import covers `4+1` with the fifth diagonal an **arbitrary real** `W`, hence also the all-equal case; both assume equal outer rates and this graph. The split is complementary and complete. The imports' internal proofs ((RES32) factorization with Bernstein positivity; the `4+1` no-real-root Sturm counts) were **not** verified here.
**Load-bearing structure revealed by the census:** 30 cells (including the first cell `4<s<r₁` of every base interval) are closed **only** by `H>0`, and 16 only by `N>0`. Hence the Hankel strictness (≥3 distinct rates) is essential — the two-valued import cannot be dropped from this proof — and strict Newton is essential, which 3.3 secures.

## 4. Findings on the candidate

**F1 — MINOR (LF7, LF15, LF26).** The strict positivity of the normalised escape rates `u_i,V` (and the identification of the `y`-frame) is used but not justified in this file. In the PH application the `y`-frame diagonal is `(−T_ii−c)/(a−c)`; positivity needs `λ_max(T)=−c` and irreducibility. Both hold: for irreducible `T` with `α≥0, α1=1` and exit vector `−T1≥0` nonzero, the Perron residue `(α·v)(w·(−T1))/(w·v)` is `>0`, so the Perron root is a pole of the transform and equals the real pole `−c`; the theta digraph is strongly connected; for irreducible Metzler `n≥2`, `T_ii<λ_max` strictly. The dependency file states this in one sentence (two-valued LF17); the candidate should state it, since LF15 applies the matrix theorem to PH representations. No change to the result.

**F2 — MINOR (LF17, LF88, LF111).** The two-valued import itself imports the `4+1` theorem (`…asymmetric-two-cycle…`, SHA256 `2a9b7352…df54`), which the candidate neither names nor hashes; the full-generality claim ("arbitrary", "ALL five positive common rates") rests on both. Name both with hashes and state that neither has an independent review (none exists under `review-waves/`).

Notes, not defects: **N1** LF38–39 — the displayed product is `−729×` the natural residual `−3V²s4−2V³s3+2V·T2−T1`; as an "`=0`" equation it is exact. **N2** LF76–80 — "SIX" followed by seven listed inequalities; the parenthetical resolves it; cosmetic. **N3** LF84 — "17 distinct nonconstant factors": irreducibility is not needed; the exact factorization identity suffices and was verified. **N4** LF103 — actual maximum projection degree 56 ≤ 60 ✓.

## 5. Named unverified imports and scope limits

- Two-valued theorem (`3daac4b2…7685`): read, hash-verified, scope-checked; its (RES32)/Bernstein proof, certificate and scripts **not verified**.
- `4+1` theorem (`2a9b7352…df54`): read, hash-verified, scope-checked (arbitrary real `W` ⇒ includes all-equal); its certificate and scripts **not read or verified**.
- Perron-normalisation step (F1): own standard argument above; not in the candidate.
- Classical imports: Sturm's theorem; Newton's inequalities (strictness argued in 3.3); Cauchy–Binet (identity verified symbolically for this case); root continuation/delineability (argued in 3.7).
- Not performed: external-family, human, formal (Lean/kernel) or novelty verification; nothing about unequal outer rates, the other 13 eight-edge shapes, ≥9 transitions, or `z≠8/9`.

## 6. Reviewer artifacts and honesty record (all exclusive-create in this directory; Python 3.14.3 arm64, standard library only)

| file | SHA256 | bytes/LF | status |
|---|---|---|---|
| `review-replay.py` (v1) | `d5d3bdca1e1202189fe83fa1bb0cfd072a564b06f772708039124e0c3941815e` | 30309 | stopped in its own helper self-test (too-strict disjointness assertion on touching isolators) and carried a `None+2` slip for the last-interval reviewer sample; no receipt |
| `review-replay-v2.py` | `d42878a227ca34bc93f4b877b48996f103392f218eff6365117170813aaedac1` | 29595 | Parts A–C passed; **hung in Part D** because its Sturm chain normalised every remainder to a positive leading coefficient (multiplying chain elements by −1 destroys the sign-variation property; probe showed 23 phantom positive roots for the degree-40 factor); killed at the 1800 s tool deadline; no receipt |
| `review-replay-v3.py` | `95335ce4225c9183e2d691ff43150f806b7efa3975f3c8a3b8fbbb2992bcbeba` | 31649 | chain fixed (positive content only) with self-tests of known real-root counts that detect the v2 defect; Parts A–D passed in 1.75 s; stopped in Part E on an own degenerate first cell (isolator starting exactly at the floor `s=4`); no receipt |
| `review-replay-v4.py` | `64918a56274b1f331d3bfcff3e052893dac34c45a21a4a19d5c4c1ab59f05f24` | 32515/688 | **complete PASS**, 1.63 s wall; isolators refined strictly above the floor before cell formation |
| `review-replay-v4-receipt.json` | `d663f875f8cebe1f6587b90b0d1dcc1769e8e0dc2873bd27ed885e599b7f8f71` | 104391/1868 | per-part receipt incl. all 26×(two-point) sections, own isolators, negative sets |

The v2 defect was in my code only; the author's checker and replay normalise by positive content and are unaffected. The mathematics of Parts A–C is unchanged across v2–v4.

**Replay receipt (v4):** elimination identities exact; six polynomials exact; **23** projection polynomials (own Bareiss), all nonzero, **23/23** exact factorization identities; **17** factors; **25** positive projection roots (own Sturm/bisection), **26** base intervals; **26 sections × 2 base points**; **56** `s`-root isolators above 4 per census; **82 + 82** cells, every cell with a strictly negative constraint; feasible open cells: **0**.

## 7. Bottom line

The candidate's exclusion of the 5-/7-cycle theta graph with equal outer rates at `z=8/9` for all five common rates with **at least three distinct values** is correct and was reproduced here from the elimination upward with independent code; the extension to **all** positive common rates holds exactly to the extent that the named two-valued (`3+2`) and `4+1` imports hold, which this review did not verify. Two MINOR presentational/dependency-bookkeeping findings; no FATAL or MAJOR defect found.

END review-v1.
