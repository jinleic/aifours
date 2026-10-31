# f159 certificate replay — ReviewF159Certificates

Wave `f159-ph7-eight-ninths-impossibility`. I verified the manifest SHA-256 `0302af70a2f3186aec20309e0e8f8ba10aad21ef478d81203ec9c1bc55bbc63a` before reading anything else. My role was **certificate replay only**. I checked two certificates with my own exact standard-library code:

- the pinned girth-4 six-rate certificate, SHA-256 `b2674b82…87d8`, called **G4** below;
- the new 1,653-leaf residual certificate, SHA-256 `45256245…6be`, called **RS** below.

Native clock observed by `/bin/date` immediately before writing this file: **Thu Oct 29 07:46:02 PDT 2026**. This is a same-harness review. It is not human review, independent-model-family review, formal or kernel verification, or a novelty check, and it does not adopt anything. I treat author "PASS" lines as claims, not evidence. The proof-level parts are the job of the parallel proof reviewer: Lemmas 1–4, the PH caller, the case logic and Ky Fan. I assess only what the two certificates establish and whether the polynomials they bound are the ones the candidates write down.

**File naming.** This report is `review-certificates-v1.md`, not `review-v1.md`. ReviewF159ProofAttack owns `review-v1.md` (its own reply, Main's instruction, and `manifest-output-addendum-v1.json`). My only other files start with `certificates-replay-v1`.

## 1. Verdicts (F/M/m = 0/0/2)

| # | Claim | Verdict |
|---|---|---|
| C1 | **G4 certificate (b2674b82…)**: Qpol>0 and Hpol>0 at every point of the open positive orthant (0,∞)^6. | **COMPLETE_VALID**, WRITTEN_SUPPORTED. All 5,332 Q and 5,334 H leaves pass. 7,775,514/7,775,514 Bernstein coefficients are ≥0. All 421,110 leaf vertices inside the open cube are >0. Each leaf splits every coordinate at least once. |
| C2 | **RS certificate (45256245…)**: on every closed leaf box of a complete cover of [0,1]^3 in (s,τ,g), Abar≤0 or Dbar≤0 or f1−4<0. | **COMPLETE_VALID**, WRITTEN_SUPPORTED. All 1,653 leaves pass their label: 800 Abar≤0, 789 Dbar≤0, 64 f1−4<0. The two needed boundary faces τ=1 and g=0 are covered (checked separately, §2). |
| C3 | The certificates bound exactly the written Qpol, Hpol, 144·Abar, 144·Dbar and 2(f1−4), and the reduction identities tying them to cases (b)–(d) hold. | WRITTEN_SUPPORTED. I re-derived every polynomial (§3). The JSON digests and expressions were compared only after that derivation. |
| C4 | Degree and subdivision conventions match the stated ones; the leaf sets are complete, prefix-free partitions. | WRITTEN_SUPPORTED, with **MINOR m1**. |
| C5 | The main candidate's description of the G4 import. | **MINOR m2**. |

**m1 (MINOR, presentational, pinned data).** The G4 JSON says only `split_axis: "path depth modulo 6"`. It does not say which half bit 0 means, and none of the f159 inputs restates it. The replay passes with bit 0 = lower half. The reversed reading fails on 616 Q leaves and 797 H leaves, so the convention is forced, but the pinned artifact does not document it. The RS JSON does state its convention (`0=s,1=tau,2=g; bit 0=lower half`).

**m2 (MINOR, wording; not load-bearing).** Main candidate §2, Import 2, calls the import "Qpol>0, Hpol>0 on all six **nonnegative** rates". The f129 assertion is narrower:

- the [girth-4 disposition](../../dispositions/math-1-ph7-girth-four-two-or-three-cycle-parent-v1.md) asserts strict positivity for open-cube points, i.e. all six **positive** rates;
- the no-2-cycle candidate also says "for EVERY six positive rates".

The main candidate's sentence is therefore an unpinned blanket statement covering the zero faces, which goes beyond the f129 assertion. f159 needs only positive rates (§2), so this is a wording fix ("positive rates"), not a gap.

## 2. Domains: what f129 asserts, what f159 needs, and the boundaries (per Main's request)

**What f129 asserts (G4).** Strict positivity of Qpol and Hpol on the open positive orthant (0,∞)^6. In compactified coordinates (u_i = x_i/(1−x_i), times ∏(1−x_i)^2) that is the open cube (0,1)^6. The argument is: all leaf Bernstein coefficients are ≥0, and every leaf vertex lying in the open cube is >0. I did **not** read any domain off the JSON metadata; the field name `Q_positive_compactified_binary_leaf_paths` is not treated as evidence.

**What f159 needs from G4.** Exactly the open orthant. Lemma C is applied to seven positive reals:

- in the no-2-cycle text these are escape rates u_i>0;
- in the main text they are the eigenvalues ut_k>0 from Lemma 1.

The six non-largest values are therefore positive. Cases (b) and (c) use Qpol>0 and Hpol>0 only at such six-tuples, and case (d) uses only RS.

**Vertex argument for the needed domain (re-derived by me).** Take x in (0,1)^6 and a leaf box containing it. Every axis interval of the box has width ≤1/2, so at least one of its two endpoints lies in (0,1). Choose a box vertex as follows:

- if x_i sits on a box face, take that endpoint;
- otherwise take an endpoint inside (0,1).

That vertex lies in the open cube, so its coefficient is >0, and its basis weight at x is >0. All other terms are ≥0. Hence P̃(x)>0.

**G4 boundaries, considered separately:**

- **x_i = 1** (u_i = ∞): not points of the domain. Not needed; no claim made.
- **x_i = 0** (u_i = 0, the zero faces): not needed by f159 and not part of the f129 assertion. My replay also computed, as a separately labelled check with scope `supp` (excluded from the verdict), that all 526,346 leaf vertices with coordinates in [0,1)^6 (289,883 Q + 236,463 H) are strictly positive. That is my own computation. It is not an f129 assertion, it is not inferred from metadata, and I do not adopt it as the import.

**RS: what f159 needs.** Case (d) maps six positive rates to y = α1 > 0, τ = 8α2/(3α1²) ∈ (0,1], γ = β1 − y/2 ≥ 0. I re-verified the three facts behind this exactly:

- 3α1² − 8α2 = Σ_{i<j}(a_i−a_j)² ≥ 0, so τ ≤ 1;
- α2 > 0, so τ > 0;
- β1 − α1/2 = ¼Σ_i[(r5−a_i)+(r6−a_i)], which is ≥ 0 under the ordering, so γ ≥ 0.

In compactified coordinates the needed domain is s ∈ (0,1), τ ∈ (0,1], g ∈ [0,1). The certificate is checked on closed leaf boxes that cover the closed cube [0,1]^3.

**RS boundaries, considered separately:**

- **τ = 1** is attained (all four smallest rates equal). 65 closed leaves tile this face exactly (area 1).
- **g = 0** is attained (all six rates equal). 158 closed leaves tile this face exactly (area 1).
- Faces s=0, τ=0 (not admissible) and s=1, g=1 (not finite points) are covered by closed boxes but are not needed, and I draw no conclusion from them.
- Four Dbar leaves are tight (maximum coefficient exactly 0): 101101, 101111, 111101, 1111111. In each, the zero coefficients sit at the non-finite corner s=1, g=1, where compactified Dbar equals its y³γ coefficient, which is 0. The non-strict selectors are sound: case (d) requires A>0 and D>0, hence Abar ≥ A > 0 and Dbar ≥ D > 0 strictly.
- The f1−4 selector is strict on all 64 of its leaves. The largest coefficient on those leaves is −1/32.

## 3. What I re-derived (exact, own code, standard library only)

**Characteristic matching.** I expanded D(y) = y[(y+1)²+8/9]² = y⁵ + 4y⁴ + (70/9)y³ + (68/9)y² + (289/81)y. Matching coefficients against y²+py+q gives:

- p = e1 − 4
- q = e2 − 4e1 + 74/9
- E4 = e3 − 4e2 + (74/9)e1 − 28/3
- E3 = e4 − (70/9)e2 + (212/9)e1 − 1007/27

**Seventh-rate splitting.** Substituting e_k = f_k + x·f_{k−1} in seven variables and splitting by powers of x reproduces the written A, B, h0 and h1 exactly.

**Qpol and Hpol.** I built Qpol = 81[A² − (f1−4)B] and Hpol = −243[h0·A − h1·B]:

- integer coefficients; 168 and 435 terms; degree 2 in each variable; S6-symmetric;
- canonical digests `2e26d636…658b` and `9453ccad…6cc2`, equal to the G4 JSON digests and to the RS JSON `imported` digests;
- elimination identities A·q = Qpol/81 + (f1−4)·E4 and A·E3 = −Hpol/243 + h1·E4, so that at E4=0, q = Qpol/(81A) and E3 = −Hpol/(243A).

**Residual chain** (a1..a4 the four smallest, r5, r6 the two largest of the six). All of these hold as exact identities:

- K = E3 − E4·S4 = E + x·D, and E·A − B·D = h0·A − h1·B;
- D = K1 + β1·K2 (β2 cancels), and the stated split of A;
- Abar − A = (r5−r6)²/4 and Dbar − D = α1α2/6 − α3;
- the sum-of-squares identities for α1α2 − 6α3 and 3α1² − 8α2;
- the γ ≥ 0 identity from §2;
- the case-(a) identities (5f1² − 12f2 as a sum of squares, and the completed square giving −58/63).

**Three-variable polynomials.** Substituting α1 = y, α2 = (3/8)τy², β1 = γ + y/2 into the written Abar and Dbar definitions gives 144·Abar, 144·Dbar and 2(f1−4) in (y, τ, γ). These equal the candidate's written §4 lines and the JSON `expr` strings (each parsed by my own parser). Degrees are [2,1,2], [3,1,1] and [1,0,1], and all three digests match.

All written formulas I relied on were asserted as literal substrings of the hashed candidate bytes.

## 4. Replay method and results

**G4: two independent methods.**

1. For each leaf, a direct tensor change of basis using the blossom (polar form) from the dyadic box read off the path. The axis is depth mod 6 and bit 0 is the lower half.
2. Separately, an integer midpoint de Casteljau walk down the tree.

The two give identical integer tensors on **all 10,666 leaves**. I also evaluated the compactified polynomial directly at all 64 vertices of 112 sampled leaves (7,168 vertices), and the original polynomial at u = x/(1−x) on 8 leaves (288 open-cube vertices). Both match the vertex coefficients exactly. There are no gaps. Some coefficients are exactly zero (23,811 for Q, 5,217 for H), which is why the strict-positivity claim rests on the vertex argument rather than on all coefficients being positive.

**RS: two independent methods.**

1. Explicit affine substitution followed by power-to-Bernstein conversion on each leaf box.
2. Exact Fraction de Casteljau subdivision from the root.

These agree on all 4,959 tensors (3 polynomials × 1,653 leaves). All 39,672 vertex coefficients match direct evaluation of both the compactified and the original polynomial. 27,280 labelled coefficients were checked, and 62,814 coefficients were computed in total. With all three selectors evaluated on every leaf, exactly one leaf satisfies both Abar≤0 and Dbar≤0. The Abar leaf closest to failing has maximum coefficient −1051947/268435456.

**Structure of all three leaf sets** (G4-Q, G4-H, RS): each is binary, has no duplicates, is prefix-free, has exact Kraft sum 1, and an explicit tree walk finds no uncovered node. Path lengths are 6–29 (Q), 6–24 (H) and 3–22 (RS). The label counts equal the JSON `leaf_counts`.

## 5. Controls and receipts

**Recorded run** — `python3 -B certificates-replay-v1.py`; bash clock 07:38:22 PDT, script clock 07:38:23–07:39:03 PDT; exit 0. 115 checks, 0 failed, split by scope: G4 41, RS 42, both 27, supplementary 5.

| File | SHA-256 | Size |
|---|---|---|
| `certificates-replay-v1.py` | `dd6e9e17ccf7e1751a6137fbda0fe006945c0a1e620098d4f3ff56432a595626` | 49,064 B / 903 LF |
| `certificates-replay-v1-result.json` | `69bd3de32382a4a6244f0f46a0e155202b1929b3f7d4207b2614d16acb539042` | 147,330 B / 9,343 LF; per-leaf RS maxima and all check details |
| `certificates-replay-v1-stdout.txt` | `acd4e780b28f014b074ed847666fe6773854932c3cd93301a78b521b114da631` | 12,560 B / 130 LF |

**Positive cases.** Both actual certificates pass, and the cross-method agreements in §4 hold.

**Negative controls.** Each one is rejected, and for the intended reason.

| Control | Result |
|---|---|
| Qpol − 50 (= Qpol − (Qpol(1⁶)+1); value −1 at u=1⁶) | Rejected. 3,586 leaves have a negative coefficient, and all 64 leaves whose box contains x = (1/2)⁶ are among them. |
| Hpol − 449 | Rejected. 2,339 leaves have a negative coefficient, including all 64 leaves containing (1/2)⁶. |
| Reversed bit convention | Rejected: G4-Q 616 leaves, G4-H 797 leaves, RS 674 label failures. |
| Structural edits | Dropping a leaf gives Kraft sum 63/64 (G4-Q) or 127/128 (RS) plus an uncovered node. Duplicating a leaf is detected. Adding a child of a leaf gives a prefix collision. |
| RS relabel of leaf 001001000 from Abar to Dbar | Rejected: Dbar coefficient 8. |
| RS with 74/9 → 83/9 in Abar | Rejected on 556 Abar leaves. |
| RS with f1−4 → f1−7/2 | Rejected on 27 f1 leaves, some with maximum exactly 0, which shows the strictness of that selector matters. |

**Supplementary controls** (scope `supp`, not used for the verdicts):

- (CHAR) holds exactly on 3 rational 7×7 matrices with no 2-cycles and W>0, C4>0.
- Adding one 2-cycle shifts [y⁵] by exactly −G_ij·G_ji, as intended.
- A Lemma C falsification sweep of 20,000 exact rational 7-tuples found 0 satisfying all four conditions (10,876 satisfy three). This is diagnostic only, not a proof.

## 6. Dependencies

The verdicts rest on the following.

- **Arithmetic and parsing.** Python 3.14.3 exact `int`/`Fraction` arithmetic, plus `json` and `hashlib`, on the same machine and harness. Both JSON files were parsed completely with duplicate keys rejected.
- **Pinned data.** The G4 leaf lists (b2674b82…) and the RS leaf/label list (45256245…).
- **Written definitions.** The no-2-cycle candidate §§2–4 (46659f60…) and the main candidate's Lemma C (599feaa5…).
- **G4 bit convention.** Bit 0 = lower half, which is unstated in the inputs (m1).
- **Standard mathematics.** Bernstein basis functions are nonnegative and sum to 1 on a box. Subdivision and blossoming are exact. The factor (1−x)^d is positive for x<1. A vertex coefficient equals the polynomial's value at that vertex. A finite prefix-free binary code with Kraft sum 1 is a complete dyadic partition.
- **Conditional premises outside my role.** The irreducibility/PH caller, Lemmas 1–4 and the case split (a)–(d) were not reviewed here. I checked only their certificate-facing algebra (§3) and that cases (b)–(d) use the certificates exactly on the domains verified in §2.
- **Use of G4 outside its stated scope.** The G4 JSON `scope` field ("graphs without directed 2- or 3-cycles") describes its original use. Its content is a graph-independent inequality about six positive reals, so f159's reuse is consistent with what was verified. This is a note, not a finding.
- **Digest format.** The canonical digest serialization (sorted `[[exponents],"int"]`, compact separators) was learned by reading the author scripts. It serves only as a binding check; the replay itself never uses author code or the JSON polynomials.

## 7. Read order, communications, collisions, deviations

**Actual read order:**

1. 06:54:06 PDT: listed the wave directory (only `manifest-v1.json` was present) and hashed the manifest.
2. Read the manifest in full (raw).
3. 06:54:18 PDT: hashed all 9 inputs. Bytes, LF counts and SHA-256 matched; all are LF-terminated with no CR.
4. Inputs 1 and 2: read in full (raw). They were issued in one parallel batch and displayed in declared order.
5. Input 3 (G4 JSON): displayed raw lines 1–120 and the last 12 lines; parsed completely by my code.
6. Input 4: read in full (raw).
7. Input 5 (RS JSON): parsed completely by my code; only a structure summary was displayed.
8. Inputs 6 and 7 (author checker and replay): read in full (raw) in one batch. Read and hash only; never imported or executed.
9. Inputs 8 and 9: read in full (raw) in one batch. Input 9 is the author regression script, read only.
10. 07:42:40 PDT, after the recorded run: read `manifest-output-addendum-v1.json` (SHA `ff37df59…88b6`; created by the parent at 07:20; it covers output ownership only).

No mandatory errata or overlays were declared.

**Not opened:** any `proofF159pa-*` file, `parent-direct-residual-*`, `parent-input-residual-certificate-v1.json`, the f61/f129 review files, the girth-4 candidate manuscript, and any HELD/quarantined material. That includes the f161 and f162/Olson items named in Main's status-only controls, none of which I accessed.

**Communications.** I had one naming-only exchange with ReviewF159ProofAttack: I asked about filenames; it replied that it owns `review-v1.md` with prefix `proofF159pa-`; I acknowledged my names. No scientific content was exchanged in either direction. From Main I received the naming instruction, the domain-distinction instruction and two status-only controls.

**Collisions and cross-exposure.** No output collision: I never created or touched `review-v1.md` or any `proofF159pa-*` file. No cross-exposure.

**Deviations:**

- I prototyped the same computations in the harness's Python eval kernel, in memory with no files written. The counts agreed with the recorded run.
- I ran three `--dry-run` passes of my script; none wrote any file.
  - Dry run 1 (07:21:59–07:22:41, script SHA `3e75ad88…`): every certificate check passed. My supplementary (CHAR) control failed because of a design flaw: two of its random matrices had no directed 3- or 4-cycles, so its "W, C4 nonzero" requirement failed. The (CHAR) identities themselves held, which I confirmed in the kernel. The run then crashed at the end because a variable was shadowed.
  - Dry run 2 (07:27:48–07:28:30, script SHA `ecf6a98e…`): all 110 checks passed.
  - After Main's domain instruction I edited the script in place: tight-leaf and per-leaf receipts, the separate needed-face checks, and the zero-face check relabelled as `supp`. Dry run 3 (07:37:12–07:37:54) used the final script bytes, SHA `dd6e9e17…`, and passed all 115 checks.
  - The earlier script versions were my own unrecorded drafts and no longer exist. The receipts bind to the final SHA.
- I used `python3 -B`; no bytecode, cache or temporary files were created.
- Shell output was filtered through `grep` for display only; the full stdout was saved by the script itself.

## 8. Summary

I parsed both certificates completely and replayed them with my own exact standard-library code, using two independent methods each.

**G4 (b2674b82…) is COMPLETE_VALID.** All 10,666 leaves pass: 7,775,514/7,775,514 Bernstein coefficients are ≥0 and all 421,110 open-cube leaf vertices are >0. The polynomials are exactly the written Qpol and Hpol, re-derived from the characteristic matching and confirmed by digest. This proves strict positivity on the open positive orthant, which is the f129 assertion and exactly the domain f159 needs.

**RS (45256245…) is COMPLETE_VALID.** All 1,653 leaves of a complete prefix-free cover of the closed cube satisfy their selectors (800 Abar≤0, 789 Dbar≤0, 64 f1−4<0). The polynomials are exactly the written 144·Abar, 144·Dbar and 2(f1−4), with every reduction identity checked. The needed domain, including its attained faces τ=1 and g=0, is covered.

Intended-reason negative controls (mutated polynomials, reversed bit convention, structural edits, relabelling, wrong constants) are all rejected. Findings: 0 FATAL / 0 MAJOR / 2 MINOR — the G4 bit convention is undocumented in the pinned data, and the main candidate overstates the import as covering "nonnegative rates", which goes beyond the f129 positive-orthant assertion; f159 needs only positive rates. My zero-face positivity computation is reported separately as a reviewer-only diagnostic and is not adopted. This is same-harness computer replay evidence. It is not human, independent-model-family, formal/kernel or novelty verification, and it does not review the PH caller, Lemmas 1–4 or the overall theorem.
