# f159 review v1 — PROOF ATTACK: no PH representation with at most seven states at z = 8/9

Reviewer: `ReviewF159ProofAttack`, a same-harness subagent. Native clock observed immediately before writing: **2026-10-29T15:08:33Z (08:08:33 PDT)**. Wave manifest `manifest-v1.json`: SHA-256 `0302af70a2f3186aec20309e0e8f8ba10aad21ef478d81203ec9c1bc55bbc63a`, verified at 13:54:07Z before anything else was read. Output ownership follows the parent addendum `manifest-output-addendum-v1.json` (SHA-256 `ff37df59…88b6`): I own `review-v1.md` and `proofF159pa-*` only.

**This is a same-harness written and exact-arithmetic review.** It is not human review, not independent-model-family review, not formal or kernel verification, and not a novelty or priority assessment. Author statements of "PASS" were not used as evidence, and no author code was imported or executed.

## Verdict

**0 FATAL / 0 MAJOR / 4 MINOR.**

**Main claim: "for every c,d>0 with z=b²/d²=8/9, H has no phase-type representation with at most seven states."**

Verdict: **WRITTEN_SUPPORTED**, conditional on the imported PH caller. The caller is the adopted parent disposition, input 1. I checked its statement, its hypotheses, and its interface to G. I did not re-review its proof, because its sources are outside this wave.

I independently reconstructed every other load-bearing step and checked it as follows:
- **Written proofs:** Lemmas 1–4, the characteristic-polynomial matching, and the whole of Lemma C, including cases (a)–(d).
- **Exact replay:** both certificates, by my own exact-integer engine.
- **Exact controls:** each with positive and negative cases.

I found:
- no sign error;
- no missing case;
- no use of the girth-four certificate outside its hypotheses;
- no gap between the caller's normalization and the symmetrized matrix.

**Corollary: "the minimum order at 8/9 is exactly 8."** Verdict: **INCONCLUSIVE in this wave.** The upper bound of 8 comes entirely from the cited-but-unread `proof-eight-state-cubic-cancellation-v1.md` (SHA `e110dd1f…`). That file is not an input here, and I neither read nor verified it.

## 1. Process record

**Actual read order:**
1. `manifest-v1.json` (`:raw`, hash verified).
2. One `shasum`/`wc` pass over all nine inputs. All SHA-256 values, byte counts and LF counts matched the manifest **before any input was read**.
3. The inputs in declared order 1→9:
   1. irreducibility parent disposition (`:raw`, complete);
   2. girth-four parent disposition (`:raw`, complete);
   3. girth-four certificate JSON — keys and metadata through JSON queries; the leaf arrays were parsed completely by my own code later;
   4. no-2-cycle candidate (`:raw`, complete);
   5. residual certificate JSON — keys and metadata queries; parsed completely by my code;
   6. `reduction-check.py` (`:raw`, read only);
   7. `integer-replay.py` (`:raw`, read only);
   8. main 8/9 candidate (`:raw`, complete);
   9. `symmetrization-identity-check.py` (`:raw`, read only).
4. A stdlib profiling one-liner over both JSON files: leaf counts and path lengths. Q paths have lengths 6–29, H paths 6–24, residual paths 3–22.
5. At 14:46:21Z, the parent addendum `manifest-output-addendum-v1.json`. It is control-plane material, output ownership only, and was read after it appeared.

**Not opened:**
- Nothing cited but not listed: no upper8 file, no irreducibility manuscript, no f61 or f129 reviews, no historical or held material.
- None of the other agents' files that appeared in this directory: `certificates-replay-v1*`, `parent-cover-*`, `parent-direct-residual-*`, `parent-input-residual-certificate-v1.json`.

**Messages:**
- Naming-only IRC exchange with `ReviewF159Certificates`. No scientific content passed either way. I first proposed the prefix `rvF159pa-`; it was never used and was replaced by `proofF159pa-` on Main's instruction.
- Main's instructions on file naming, scope labeling, and the positive-versus-nonnegative check of Qpol/Hpol were followed.
- Status-only hold notices for f162 (Olson) and f161: I accessed none of those materials.

**Environment:** Python 3.14.3 standard library for every exact decision; NumPy 2.4.3 only in labelled floating diagnostics. SymPy and SciPy are absent and were not installed. Every run used `PYTHONDONTWRITEBYTECODE=1`, so no pycache was written, and no temporary directory was used.

**Deviations, all disclosed:**
- **(i) JSON reading.** Leaf arrays were checked by complete parsing in code, not by displaying them.
- **(ii) Failed first run of the lemma controls.** Script SHA `affbba90…`, 14:21:10–14:21:15Z, exit 1. The failure was in my own L5 negative control, which wrongly assumed E4 depends on z. For that matrix e1(ut)=6, and E4_z − E4_{8/9} = 2(k_{8/9}−k_z)(e1−6) = 0. The control was corrected and the script rerun as `45fcdf25…`, exit 0. The failed run wrote no result file.
- **(iii) Two ad-hoc read-only one-liners**, not saved: the leaf-length profile and a summary of the continuation result.

## 2. Claim-by-claim verdicts

| # | Claim | Verdict |
|---|---|---|
| C1 | PH caller (input 1, imported): z>1/2 and at most 7 states ⇒ exactly 7 states, strongly connected T. Then G=(T+cI)/d is irreducible Metzler with s(G)=0, and det(yI−G)=y[(y+1)²+8/9]²(y²+py+q) | IMPORTED, at its boundary (statement only). Interface: **WRITTEN_SUPPORTED** |
| C2 | p>0, q>0 from irreducibility | WRITTEN_SUPPORTED |
| C3 | Matching constants: p=e1−4, q=e2−4e1+74/9, E4=e3−4e2+(74/9)e1−28/3, E3=e4−(70/9)e2+(212/9)e1−1007/27 | WRITTEN_SUPPORTED (exact control L0) |
| C4 | Lemma 1: s(S)<0 | WRITTEN_SUPPORTED (exact L4); see m3 |
| C5 | Lemma 2: cover identity with one-way and virtual cycles, ω=(√w₊−√w₋)² | WRITTEN_SUPPORTED (exact L3, L5) |
| C6 | Lemma 3: coefficient extraction | WRITTEN_SUPPORTED (exact L3, L5) |
| C7 | Lemma 4: Ky Fan | WRITTEN_SUPPORTED (standard; exact in L5, floating in L3) |
| C8 | Lemma C: the crude system is infeasible for seven positive reals. Covers the identities (SPLIT), case (a) f1<4, case (b), case (c), case (d) | WRITTEN_SUPPORTED (exact L1, L2; certificate replays) |
| C9 | Imported Qpol>0, Hpol>0 for six **positive** rates (pinned girth-four certificate) | WRITTEN_SUPPORTED (my complete exact replay); see m1 on wording |
| C10 | Residual 3-parameter certificate, 1653 leaves | WRITTEN_SUPPORTED (complete exact replay, plus my own independent cover) |
| C11 | No-2-cycle theorem (input 4), as a special case of the chain | WRITTEN_SUPPORTED, conditional on C1 |
| C12 | **Main theorem: no ≤7-state PH at z=8/9** | **WRITTEN_SUPPORTED, conditional on C1** |
| C13 | Corollary: minimum order exactly 8 | **INCONCLUSIVE** (upper8 not in this wave) |
| C14 | Section 6 diagnostics: crude system feasible to ≥0.87; PH7 band edge about 0.82042 | Not premises. My floating diagnostics are consistent (Section 8) |

## 3. Independent reconstruction

**R1 — Caller to G.** From input 1 (statement and steps 1–2):
- The reduced transform has the simple pole −c and the double poles −a±ib. Its numerator is constant, so there is no cancellation.
- Any representation's characteristic polynomial contains these roots with at least those multiplicities.
- With at most 7 states and z>1/2, there are exactly 7 states, a single strongly connected component, and s(T) ≤ −c. Because −c is an eigenvalue, s(T) = −c.
- Hence G=(T+cI)/d is Metzler and irreducible (same off-diagonal pattern), with s(G)=0.
- Its eigenvalues are 0 and (−a+c±ib)/d = −1±i√z, each at least twice; the degree count gives the monic quadratic factor.
- For irreducible Metzler G, the matrix G+tI is primitive for large t. So 0 is simple and every other eigenvalue has real part below 0. Both hidden roots therefore have negative real part, and p>0, q>0.

Exit rates, the absorbing state and reducible preliminary forms never enter after the caller. The absorbing state is not a vertex of G; zero exit rates do not affect G's diagonal, which is negative because Gr=0 with r>0 and every row has an off-diagonal entry. **No gap.**

**R2 — Matching (any z).** Put k=1+z, so D=y⁵+4y⁴+(4+2k)y³+4ky²+k²y. Matching the coefficients of y⁶ down to y³ gives:
- p = e1−4
- q = e2−4e1+12−2k
- E4 = e3−4e2+(12−2k)e1+12k−32
- E3 = e4−(4+2k)e2+(16+4k)e1+3k²−48

At k=17/9 these become exactly the candidate's constants. This was verified exactly for 8/9 and six other rational z.

**R3 — Lemma 1.** Take c0 ≥ max u_i and P=G+c0I. P is nonnegative and irreducible with Perron root c0, and positive right and left Perron vectors r and l.
- With Dg=diag(√(l/r)), the matrix M=Dg P Dg⁻¹ has v=√(l∘r) as both its right and left Perron vector.
- Therefore M_s=(M+Mᵀ)/2 is irreducible and satisfies M_s v = c0 v, so ρ(M_s)=c0.
- The matrix S+c0I is nonnegative, has the same diagonal as M_s, and has off-diagonal entries √(M_ij M_ji) ≤ (M_s)_ij by AM–GM.
- If S+c0I ≠ M_s, strict monotonicity of ρ for an irreducible dominating matrix gives λ_max(S) < 0.
- Otherwise M is symmetric, so G has real spectrum, which contradicts −1±i√(8/9).

Inequality directions: correct.

**R4 — Lemma 2.** Expand both determinants as det(yI−M) = Σ over sets L of disjoint directed cycles (length ≥2) of ∏(−w) · ∏ over uncovered vertices of (y−M_ii). The sign of a k-cycle is (−1)^{k−1}·(−1)^k = −1.
- **2-cycles** have the same weight G_ijG_ji in S.
- **Bidirected-only cycles** of length ≥3 are exactly the two orientations of an undirected cycle Γ of F. In S each orientation weighs s_Γ=√(w₊w₋).
- **One-way cycles** have length ≥3 and are absent from S.
- Since w₊+w₋ = 2s_Γ+ω_Γ, expanding ∏_Γ(−s_Γ−s_Γ−ω_Γ) and regrouping gives a bijection with (L, an S-linear subgraph on V∖∪L). S has the same diagonal as G.

**Correct.**

**R5 — Lemma 3.** Extra cycles have at least 3 vertices, and two disjoint ones cover at least 6, so their det factor has degree ≤1. Hence:
- [y⁴] = e3(ut) − Σ_{|C|=3} ω_C
- [y³] = e4(ut) − Σ_{|C|=3} ω_C tr(A_{V∖C}) − Σ_{|C|=4} ω_C

**R6 — Lemma 4.** Cauchy interlacing (or Ky Fan) gives tr(A_J) ≥ ut₁+…+ut₄ for every |J|=4. Note that tr(A_{V∖C}) = Σ_{i∉C} u_i.

**R7 — Assembly.**
- E4(ut) = W ≥ 0.
- E3(ut) − E4(ut)S4(ut) = Σ_{|C|=3} ω_C (tr(A_{V∖C}) − S4(ut)) + C4 ≥ 0.
- p and q are the same numbers as in R1, because det(yI−G) is the same polynomial.
- ut > 0 by Lemma 1, and ut is sorted.

This is exactly the hypothesis of Lemma C, so the four directions and the "four smallest" convention match.

**R8 — Lemma C.** Let x=v₇ be the largest value and f_k the elementary sums of v₁…v₆. Then S4 is the sum of the four smallest of those six. The identities (all verified exactly in L1):
- e_k = f_k + x f_{k−1}
- q = A + x(f1−4)
- E4 = Ax + B
- E3 = h0 + x·h1
- K = E + xD, with EA − BD = h0A − h1B

**Case (a), f1<4.**
1. p>0 gives x > 4−f1 > 0.
2. q>0 then gives A > x(4−f1) > (4−f1)².
3. But 5f1²−12f2 = Σ(r_i−r_j)², so A−(4−f1)² ≤ −58/63 − (7/12)(f1−24/7)² < 0.

This holds for all six positive rates. It uses only p>0 and q>0.

**Case (b), f1≥4 and A≤0.**
- f1=4: then q = A ≤ 0.
- A<0: E4≥0 gives x ≤ B/|A|. q>0 forces f1>4 and x > |A|/(f1−4). Together these give Qpol<0.
- A=0: E4=B≥0 gives Qpol = −81(f1−4)B ≤ 0.

Each subcase contradicts the **strict** inequality Qpol>0. Strictness is needed for A=0.

**Case (c), f1≥4, A>0 and D≤0.** E4≥0 gives x ≥ −B/A. Because D≤0, K ≤ E − BD/A = −Hpol/(243A) < 0. This needs strict Hpol>0.

**Case (d), f1≥4, A>0 and D>0.** In the six-rate split:
- D = K1 + β₁K2 (β₂ cancels), and A = … + β₂.
- Relaxations: Abar−A = (r₅−r₆)²/4 ≥ 0, and Dbar−D = α₁α₂/6 − α₃ ≥ 0. The latter is ½Σ a_i(a_j−a_k)² by an exact identity.
- 3α₁²−8α₂ = Σ(a_i−a_j)² gives τ ∈ (0,1].
- β₁ ≥ 2·max a_i ≥ α₁/2 gives γ ≥ 0.

The displayed polynomials 144·Abar, 144·Dbar and 2(f1−4) equal my substitutions exactly. Case (d) would therefore give Abar>0, Dbar>0 and f1≥4 at an admissible point (y>0, τ∈(0,1], γ≥0). The certificate shows that at every such point Abar≤0, or Dbar≤0, or f1<4. Non-strict selectors are enough for Abar and Dbar; f1 needs the strict selector, which is the one used. The cases are exhaustive, and every inequality direction checks.

**R9 — Certificate semantics.**
- **Compactification:** u=x/(1−x), multiplied by (1−x)^deg. The factor is positive at finite points.
- **Bernstein form:** compactified axes take coefficient c_i/C(d,i); the τ-axis uses the standard power-to-Bernstein conversion. Bernstein basis functions are nonnegative.
- **Girth-four strictness:** every leaf splits each axis at least once (checked). All coefficients are ≥0 and every vertex coefficient inside the open cube is >0 (checked). For an open-cube point, choose the touched endpoint, or else an endpoint inside the open cube. Its basis weight is positive, so the polynomial is >0 on (0,1)⁶, which corresponds to positive rates.
- **Hypotheses:** Lemma C applies Qpol and Hpol to ut₁…ut₆, which are >0. That is the certificate's polynomial hypothesis. Its JSON `scope` string describes the earlier graph theorem, not a hypothesis of the polynomial inequality. **No misuse.**

## 4. Attack log (targeted hunts)

- **Inequality signs.** All checked in R3 and R8: the orientation of the AM–GM comparison, the division by A<0 in case (b), xD ≤ (−B/A)D in case (c), the strict-versus-non-strict selectors, and Ky Fan with "four smallest". Exact sample control L2 used 12,000 sorted rational 7-tuples, including 6,000 near equal rates 0.85–0.95, the tightest region. Results:
  - no tuple satisfied all four conditions;
  - every case implication held;
  - Qpol and Hpol were >0 throughout;
  - case (d) never occurred;
  - the best min(p,q,E4,K) was −0.0178.
- **Missing cases.**
  - Boundaries f1=4 and A=0 are covered.
  - Equal and repeated rates are fine: ordering ties do not matter and Ky Fan allows ties.
  - Overlapping one-way and virtual cycles are excluded by disjointness.
  - Extras that cover all 7 vertices give an empty det factor, equal to 1.
  - Three disjoint extras are impossible (they would need ≥9 vertices).
  - The absorbing state, zero exit rates and reducible forms are handled before G (R1).
- **Certificate misuse.** None (R9).
- **Caller to S gap.** None. S(G) = (S(T)+cI)/d, and S is invariant under the diagonal similarity G→R⁻¹GR. Lemmas 2–4 need only that G is Metzler; Lemma 1 additionally needs irreducibility, s(G)=0 and a nonreal eigenvalue, all supplied by C1.
- **Falsification attempts at z=8/9** (floating, Section 8). No counterexample was found. This is not proof.

## 5. Findings (all MINOR; none load-bearing)

- **m1 — Overbroad import wording.** Section 2 of the main candidate says "Qpol>0, Hpol>0 on all six **nonnegative** rates". The admitted inputs establish this only for six **positive** rates: input 2 says "strictly positive for all six positive rates", input 4 says "for EVERY six positive rates", and the certificate argument covers the open cube.
  - Not load-bearing: Lemma 1 makes every ut positive.
  - My reviewer-side probe (`proofF159pa-boundary-probe-v1`) found no nonpositive vertex coefficient at finite boundary vertices: 289,883 Q and 236,463 H vertices.
  - Per Main's instruction, this observation is a **diagnostic only and is not promoted** to an admitted zero-face claim.
  - Fix: say "positive".
- **m2 — Notation clash.** `A := −S` in Lemmas 1–4 versus Lemma C's `A = f2−4f1+74/9`. Presentational.
- **m3 — Lemma 1 hypotheses are implicit.** As a standalone statement it is false without them. For example, a symmetric or reversible G with s(G)=0 gives s(S)=0, which my exact control L4 confirms. The proof does use irreducibility, s(G)=0 and the nonreal pair. They should be stated in the lemma.
- **m4 — Scope labeling of "exactly 8".** The title and END line assert "the minimum PH order there is exactly 8" without the conditionality the body gives it. The upper bound rests entirely on the unreviewed upper8 import. The title should be conditional, or should state only the lower bound proved here (order ≥ 8).

## 6. Exact dependencies

1. **PH caller** — statement of input 1 (parent disposition `42ae3d99…`, adopted). Its proof rests on `frontier-20261028-ph7-global-irreducibility-v1.md` (SHA `729926c5…`) and the f61 review. Neither is an input here, and neither was read. **Verification boundary: statement and interface only.**
2. **Pinned data: girth-four certificate** (input 3, `b2674b82…`). The polynomial definitions come from inputs 2 and 4. Its positivity was re-established here by my exact replay. Its checker, replay and boundary-check hashes cited in the candidates (`8f5fc02b…`, `ac5b069e…`, `03d2853e…`) are not inputs and were not used.
3. **Residual certificate** (input 5, `45256245…`): re-established by exact replay plus my own cover.
4. **Written reductions** of input 4, Sections 2–4, and of input 8, Sections 2–4: reconstructed above.
5. **Standard results:**
   - finite SCC and permutation-cycle determinant expansion;
   - Perron–Frobenius for irreducible nonnegative and Metzler matrices: positive Perron vectors, simple Perron root, strict dominance of real parts via primitivity, and strict monotonicity of ρ under an irreducible dominating matrix;
   - AM–GM;
   - Cauchy interlacing / Ky Fan;
   - Bernstein basis nonnegativity and de Casteljau subdivision.
6. **Conditional premise:** existence of a ≤7-state representation, assumed for contradiction.
7. **Corollary only:** upper8 (`e110dd1f…`), cited but not read; **not verified**. The subsumed six-state barrier (`8ba04931…`) is not a premise.

## 7. Controls and receipts

All files are in this directory. Runs used `PYTHONDONTWRITEBYTECODE=1 python3`; clocks are `/bin/date -u`.

| Artifact | SHA-256 | Run | Result |
|---|---|---|---|
| `proofF159pa-cert-replay-v1.py` (25,695 B / 645 LF) | `86264dea919cef71109ff0d023f05ecf39a35dfe91c883c294f566b795aa73e3` | 14:14:59Z → 14:15:07Z, exit 0 | `-result.json` `4172a6b92f75b147eb052bb5f7c3209949dab52f8469435815a8f299f24e43d6` |
| `proofF159pa-lemma-controls-v1.py` (28,559 B / 654 LF) | `45fcdf25e0afdf4eb141a1e30be4a63ced754f6a13ca906a34580989fbb782d5` | 14:24:15Z → 14:24:20Z, exit 0 (earlier `affbba90…` exit 1, see §1) | `-result.json` `a012578b6b9d4984c987c77d7517a43833110c68c1d35b3466af1637e4916ac3` |
| `proofF159pa-boundary-probe-v1.py` (5,510 B / 143 LF) | `6addb0279ba25475d1e0266df54fd9df8bf3cd993ef5e96aa1ddd536e6371cf7` | 14:30:12Z → 14:30:14Z, exit 0 | `-result.json` `cd62ad5777a15a11fe62775fcfc0608552385e78ddd1ecfaa7cdb5aaa19c2756` |
| `proofF159pa-numeric-attack-v1.py` (11,274 B / 305 LF; floating) | `80a98f0eeae895f9d8766f4d51a0d537f7dcf66d3e6bb53a034a5bb2067324d1` | 14:26:57Z → 14:38:49Z, exit 0 | `-result.json` `945a42c98dfb59ab8d1f7874b64d84411b62930206bfbd0ffaec526c493c7b47` |
| `proofF159pa-numeric-continuation-v1.py` (7,265 B / 200 LF; floating) | `589f8b1eadfae944d16362a9b206c50a9f3ee5bcba25e0752defd60267c81e7b` | 14:42:44Z → 15:04:25Z, exit 0 | `-result.json` `8af64ec356354a0378015cb7dd614205fdc341f4d55c9dbd803eed807ec83cd3` |

### Certificate replay (exact integers; both JSON files hash-checked and parsed completely)

**Girth-four certificate.**
- From the definitions, I rebuilt Qpol (168 terms) and Hpol (435 terms), each of degree 2 in every variable. My canonical digests equal the pinned `2e26d636…` and `9453ccad…`.
- All 5,332 Q leaves and 5,334 H leaves form prefix-free, complete covers; every axis is split on every leaf.
- All 7,775,514 Bernstein coefficients are ≥0. All 421,110 open-cube vertex coefficients (Q 230,864; H 190,246) are >0.
- An exact engine self-test (Bernstein value equals direct value at rational points) passed.

**Residual certificate.**
- Abar, Dbar and 2(f1−4) were rebuilt from the definitions. Digests `da5b0bb5…`, `67f810b9…` and `b0e02228…` match, and the parsed `expr` strings are identical to my polynomials.
- 1,653 leaves (800 / 789 / 64), prefix-free and complete; every selector holds.
- **My own independent cover**, with a different split rule (widest side) and selector order, closes with 1,654 leaves (807 / 798 / 49), maximum depth 22.
- 24,000 exact samples found no violation of the residual statement and no relaxation violation (A ≤ Abar and D ≤ Dbar at real six-rate tuples).

**Negative controls**, each detected for its intended reason:
- deleting a residual leaf is reported "uncovered" at exactly that path;
- relabelling an Abar leaf as Dbar fails its selector (maximum coefficient 786,432);
- the shifted threshold 2(f1−4)+1 makes a strict f1-selector fail (maximum 0);
- deleting a girth-four leaf is reported uncovered;
- Q−5, which is negative at rates 9/10 where Q=6821/2000, changes the digest and produces a negative coefficient on the containing leaf.

### Lemma controls (exact Fractions)

- **L0 — matching.** The candidate's constants at 8/9 match my general-z closed forms at seven rational z. Negative: the z=0.87 constants differ.
- **L1 — algebra.** All 18 identity checks pass, including the displayed 144·Abar and 144·Dbar. The 19th recorded entry is a negative control, which detects an altered Dbar coefficient.
- **L2 — case logic.** As described in Section 4.
- **L3 — Lemma 2 cover identity.** 15 random rational 7×7 Metzler matrices in five modes (mixed, mixed-dense, all-bidirected, one-way-only, sparse). Bidirected pairs (st, s/t) make S rational. The instances include 3,563 virtual and 1,060 one-way extra cycles; each all-bidirected instance alone has 1,172 virtual cycles.
  - The identity holds exactly at 8 values of y, and the Lemma 3 coefficients are cross-checked by Faddeev–LeVerrier and by principal-minor sums.
  - Negative controls: dropping virtual cycles is detected in 8 of 8 applicable instances; using w₊+w₋ in 8 of 8; dropping one-way cycles in 12 of 12.
- **L4 — Lemma 1.**
  - Positive: 12 strongly connected zero-row-sum G, each with a nonreal eigenvalue (checked in floating point), all have −S positive definite by an exact Sylvester test. Floating values: s(G) is within 5×10⁻¹⁵ of 0, and λ_max(S) ≤ −0.0475.
  - Negative, intended equality case: a reversible G with π = squares gives det(−S) = 0.
- **L5 — exact end-to-end chain on actual matrices.** Z₇ circulants with quadratic-residue weights 4 and 1, and 9 and 1. Their characteristic polynomials are exactly y((y+1)²+z)³ with z = 9/175 and 16/175. F = K₇ gives 1,172 virtual cycles each.
  - Exact spectra of −S: {6/35, 34/35⁶} and {12/35, 33/35⁶}.
  - E4_z(ut) = W exactly (176/1225 and 292/1225).
  - E3 matching holds; K_z = 3792/30625 and 37524/214375, both >0.
  - Ky Fan holds exactly; p=2 and q=1+z.
  - Negative controls: the 8/9 constants break both the q and E3 matchings; dropping the virtual cycles breaks E4 = W.

## 8. Floating diagnostics (not premises)

- **Spectral attack.** By diagonal similarity, a zero-row-sum G is WLOG, and all 42 entries were parametrized as θ².
  - Random starts converged at z=0.5 (27 of 40) and failed at 0.7 and 0.78.
  - Continuation from five z=0.5 solutions reached z_max ≈ **0.82031–0.82042** on every path, numerically matching the candidate's stated PH7 band edge of about 0.82042. Near that edge the solutions have no 2-cycles and W ≈ 0.
  - Attacking z=8/9 from those edge solutions with 200 starts gave a minimum relative residual of 7.1×10⁻⁴. Random starts gave a minimum residual of 0.805. No counterexample was found.
- **"Just below the bound" controls.** 35 chain checks along the continuation, z from 0.5 to 0.8204:
  - λ_max(S) ≤ −0.948, p ≥ 3.03, q ≥ 2.06;
  - |E4−W| ≤ 8.9×10⁻⁹ and |E3−(T3+C4)| ≤ 7.2×10⁻⁹, which is the solver's residual level;
  - the cycle-side slack Σω(tr−S4)+C4 is ≥ 3.5×10⁻¹⁴ everywhere.

  The single flagged item, coefficient-side K = −1.7×10⁻⁸ at the extremal endpoint z = 0.82042 where E4 ≈ K ≈ 0, is a tolerance artifact of approximate divisibility, not a violation.
- **Crude-system feasibility** (Nelder–Mead on seven rates).
  - Positive maximum of min(p,q,E4,K) at z = 0.80, 0.85, 0.87 and 0.875. Each was rationalized and **verified feasible exactly**, and the same rational point is exactly infeasible under the 8/9 constants.
  - The maximum is negative at 0.88 (−0.0048) and at 8/9 (−0.0157).
  - This confirms the candidate's statement that the crude system is "feasible to at least 0.87" and is consistent with Lemma C at 8/9.

## 9. Summary

I independently reconstructed the whole decisive chain:
- the caller interface;
- characteristic matching;
- the geometric symmetrization lemmas: Perron/AM–GM strictness, the cover identity with one-way and virtual cycles weighted (√w₊−√w₋)², coefficient extraction and Ky Fan;
- Lemma C, including the f1<4 case, the Qpol/Hpol cases, and the 3-parameter residual case.

I replayed both certificates completely with my own exact-integer code and built an independent residual cover. I found **no FATAL and no MAJOR issue** and four presentational MINORs:
- m1: "nonnegative" should read "positive" rates;
- m2: the A notation clash;
- m3: Lemma 1's implicit hypotheses;
- m4: the unconditional "exactly 8" in the title.

On that basis, **"no phase-type representation with at most seven states exists at z=8/9" is WRITTEN_SUPPORTED, conditional only on the adopted PH caller.** That caller was used at its stated scope (z>1/2, at most 7 states), and I did not re-review its proof. The claim "minimum order exactly 8" remains **INCONCLUSIVE here**, because its upper bound is an unread, unreviewed import.

Floating diagnostics place the numerical limit of 7×7 Metzler double-pair realizability near 0.8204 and crude-system feasibility near 0.875–0.88, both below 8/9. These diagnostics are consistent with the theorem but are not part of the proof.

This is same-harness review evidence only. It is not human, independent-model-family, formal/kernel or novelty verification, and it is not adoption.
