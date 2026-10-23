# K62-FULL written review package v1: no configuration of class K6.2* (all orientations, all marker placements) [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T13:20:11-0700, immediately before this exclusive write.
- **Owner:** SunM13MixedFibres. Written mathematics only; no computation, model call or nested agent; packaging used only
  sha256, byte counts and line-range extraction. The parent owns model reviews and verdicts.
- **Candidate:** `K/K62-FULL-v1.md`, sha256 `fabf04dd6abb1d3ec7e71b1cc3d459e008e9a96b5186b5a1f571fedac1312e5b` (283 lines, 30,335 B), read with **`K/K62-FULL-erratum-v1.md`**, sha256
  `4b8ae281e8759f2bfd4d543f60f2fdaed0a3d58931619b4b262610cfc6980cc0` (one pointer correction in a section-10 thought experiment; no proof change). **Frozen scope:**
  `K/K62-FULL-SCOPE-v1.md`, sha256 `8ee636479aa4742a260f3248343b2a04a30ab447a4f9b8af3572f52a62878303` (13:14, before derivation). **Authority:** transition `444d7524b2fd9e785565dd94f98f13d5b5aff208b5f1dde29d59e301be31a0cf`.
- Root aliases (exact absolute prefixes): K = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-full-closure`;
  K62 = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon`;
  S = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7`; O16 = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7`;
  RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`; R16 = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review`.

## 1. Claim and exact status
**Theorem K62X (CANDIDATE_UNVERIFIED):** no group with finite-index subgroups contains a K6.2* configuration — every
orientation, every admissible 3-/5-marker placement (3-marker on t in O, on i* with any f* >= 2, or absent; 5-marker on d, i*,
a vertex of O, or absent), all exponents and w-cofactors. Not claimed: K7, K6.3, K5.2*, KII, Sun(7); novelty, priority,
significance, Lean or human review. Sun(5)/Sun(6) remain computer-assisted transitive imports. For the sub-case G (no O-marker)
the statement is the accepted GS Theorem GE; nothing new is claimed there.

## 2. Reading order
1. Scope (whole) and the transition record. 2. Candidate whole, then the erratum (F1 replaces one sentence of section 10).
3. Accepted imports at the literal ranges of section 4 (statements, not headings). 4. Pending texts (M13X, R2MIX, MK) ONLY for
attribution/comparison; they are not premises, and every borrowed step is re-proved in the candidate.

## 3. Verbatim key statements (raw candidate lines)
K62-FULL-v1.md:70-72
```text
**Lemma OR (exact d-i* orientations).** In every K6.2* configuration: (i) alpha_(d i*) and alpha*_(d i*) lie in {1, 3}; (ii) they
are not both 3; (iii) if one of them is 3, the 3-marker lies on some t in O, so f_t >= 2 and f* = 1. Hence
(alpha_(d i*), alpha*_(d i*)) is (1,1), or (1,3) or (3,1) with t in O.
```
K62-FULL-v1.md:77-80
```text
**Reduction R.** If alpha_(d i*) = 3, the actual inverted configuration Gamma* is of class K6.2* with the same indices and
markers, and its pair is (alpha*_(d i*), alpha_(d i*)) = (1, 3) by OR (i)-(ii). So it suffices to exclude configurations with
**alpha_(d i*) = 1**; then alpha*_(d i*) = 1, or alpha*_(d i*) = 3 with t in O and f* = 1. All marker placements of section 0
remain allowed in the case alpha*_(d i*) = 1, including f* >= 2.
```
K62-FULL-v1.md:82-85
```text
**Lemma FAM (both-family inputs).** Let alpha_(d i*) = 1. For both families x:
(C2_x) n_4(x) >= 2 n_1(x) + 2;
(DG_x) if min(e_d, delta_x(Q)) <= 4 for all five 4-subsets Q of O, then at least two O-triples R have min(e_d, delta_x(R)) >= 4,
or exactly one does and it has min(e_d, delta_x(R)) = 5, type (4,4,4) and tau_x(R) = 16.
```
K62-FULL-v1.md:124-125
```text
**Statement.** In every K6.2* configuration, for both families z and every non-empty R in O:
T_z({d} cup R) = lcm(n_d, n_j : j in R) * 2^s for some integer s >= 0. Consequently, **for every v in O: gcd(n_v, T_z(V minus {v, i*})) = 6.**
```
K62-FULL-v1.md:144
```text
**Lemma R4S.** For both families x and every v in O, the four O-entries x_vu (u in O minus {v}) do not all lie in {1, 2}.
```
K62-FULL-v1.md:160
```text
**Lemma CIS.** For a family x, v in O and a != b in O minus {v} with x_va = x_vb = 4, X^v_a = X^v_b and x'_va = x'_vb = 2: contradiction.
```
K62-FULL-v1.md:215
```text
**Lemma FB.** For each family x and every 4-subset Q of O: delta_x(Q) <= 4.
```
K62-FULL-v1.md:241-243
```text
**Theorem K62X.** No group with finite-index subgroups contains a configuration of class K6.2*: every orientation, every
admissible placement of the 3- and 5-markers (including f* >= 2 and the 5-marker on d, i* or a vertex of O), all exponents
e_d, e*, f's, h's and all w-cofactors.
```

## 4. Source/authority table (rows = manifest entries in order; whole-file sha256; inclusive one-based ranges)
| ID | Path | SHA256 | Lines | Scope / authority |
|---|---|---|---|---|
| F | K/K62-FULL-v1.md | fabf04dd6abb1d3ec7e71b1cc3d459e008e9a96b5186b5a1f571fedac1312e5b | 1-283 | NEW candidate, whole: re-derive every claim |
| FE | K/K62-FULL-erratum-v1.md | 4b8ae281e8759f2bfd4d543f60f2fdaed0a3d58931619b4b262610cfc6980cc0 | 1-27 | NEW overlay: one mutation-check pointer (F1); no proof change |
| FSC | K/K62-FULL-SCOPE-v1.md | 8ee636479aa4742a260f3248343b2a04a30ab447a4f9b8af3572f52a62878303 | 1-55 | frozen target/premise discipline, pre-freeze disclosure |
| TR | RUN/control/mathematics-slot-transition-sun-20261019-1311-v1.json | 444d7524b2fd9e785565dd94f98f13d5b5aff208b5f1dde29d59e301be31a0cf | 1-11 | parent authority for this target |
| README | O16/README.md | 2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1 | 9-29, 31-52, 85-97 | accepted: imports, R0, P0/P1, class K6.2* (R16 written verdict) |
| RULES | O16/rules-k7-v1.md | 77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee | 7-24, 38-46 | accepted: L0.3, L1; VFC (V1)-(V4) |
| WV | R16/sun-coset7-written-parent-verdict-v1.md | 73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35 | 16-23, 58-60 | verdict for README/rules; Sun(5)/(6) provenance |
| LFC | S/K7-LFC-INV-v1.md | 45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c | 18-45, 52-71 | accepted: LFC (a)-(d), INV (a)-(b) |
| LFCE | S/K7-LFC-INV-erratum-v1.md | 7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5 | 12-32, 47-63 | mandatory overlay: E1-E3, E6, E7 |
| LFCV | RUN/review/sun7-lfc-inv-parent-verdict-v1.md | 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18 | 5, 16-23 | verdict: LFC, INV, R0 lift |
| E3 | K62/K62-E3-v1.md | 70a60d551583e8d6ad920acadb829d3ddf0d9c5c46ac988f8677645ee5457372 | 15-34, 36-55, 91-105 | accepted: setting, theorem, Lemmas 1-2, C1/C2 incl. the swapped form (line 105) |
| E3E2 | K62/K62-E3-erratum-v2.md | f9f52e1bc4896d94cd014ed3f8915af0318ddcd06d1efc1ad7f14478685add4c | 80-89, 276-297 | mandatory overlay: Z2, Z11 |
| E3V | RUN/review/sun7-K62E3-parent-verdict-v1.md | 576969ddb99fc2d0f5c6382f66428a7f4d7d3a1b59f681fc4d9d0f458fecbb0f | 5, 14-25 | verdict for E3 |
| DG | K62/K62-DG-v1.md | a4bfc41e832ebc4e77770cab7a8092a3341827cec93a01bfb437c978c1e84f52 | 20-36, 50-61 | accepted: DG-1, DG-2, Theorem DG and its swapped form (line 61) |
| SHDGE | K62/K62-SH-DG-erratum-v1.md | 755edc21abdf7484f9187078d7e8cb6b4111f076906e7880085428d54f1b9d75 | 240-268, 323-327 | mandatory overlay: G5, G6; DG (b) conditionality and orientation note |
| SHDGV | RUN/review/sun7-K62-SH-DG-parent-verdict-v1.md | cae455c3252b9066c261bcebb05ee4917b838bb5e2370101689c8297a017ddda | 14-24 | verdict: DG items 2-4 |
| M13A | K62/K62-M13-A-v1.md | 77ce4077584582c699ce1bec870f2b19c55242bfc05aac99febcfbd69c466a8d | 18-31, 69-107 | accepted at (1,3): DG*, C2* for alpha |
| M13V | RUN/review/sun7-K62-M13-parent-verdict-v1.md | 2fac7a30ab4b832166c770492fdd6d0f555660e5c3eabcb95d514797a39c4e34 | 5-20 | verdict: exact accepted M13 scope |
| GSV | RUN/review/sun7-K62-GS-parent-verdict-v1.md | 3a01c9e495a9bc6d7fbf8f03cbf981df9aa9a9dc70b8e9273ffe87803c19dfc2 | 5-13 | accepted GS (G empty): cross-check only, not a premise |
| X | S/continuations/k62-m13-mixed/K62-M13X-v1.md | b86bb186e425ea5ac69a51d85ad5f56cfc1abd2a08c66c169fd54de074262db9 | 101-129, 132-142, 157-181 | PENDING (Codex accept relayed; parent erratum pending): SG, R4S, CIS origin, attribution only |
| R2MIX | S/continuations/k62-r2-mixed/K62-R2MIX-v2.md | b75e6dc7e72b8c0b1cd5388e8845a3bcd23854b0fbd83292fa6ff7c22ade0806 | 77-95 | PENDING: Lemmas 1-2 origin, attribution only |
| MK | S/continuations/k62-regimes/K62-MK-v2.md | ab7cfcb6ccebb19465eb6dfc3f96580d58c599a2507aee697604f691ad5abee9 | 141-166, 185-225 | PENDING (1,1): R4*/DEG, FB-M/DEEP/MK origin, attribution only |
The JSON manifest `K/review-excerpts-FULL-v1.json` lists the 39 ranges as {path, sha256, start, end} in this order.

## 5. Wider-scope obligations and where they are discharged
| Obligation (scope section 1) | Candidate lines | Interface |
|---|---|---|
| (a) exact d-i* orientation set | 70-75 (OR) | E1 (g = 4), E3-L1 for both families, INV (b) sum <= 4, marker uniqueness |
| (b) (3,1) via the actual inversion | 77-80 (R) | INV (a)-(b) with E6; OR (i)-(ii) |
| (c) both-family C2/DG | 82-92 (FAM) | E3-C2 and Theorem DG on Gamma (alpha_(d i*) = 1) and on the actual Gamma* (its entry alpha*_(d i*) = 1) in (1,1); M13-A C2*/DG* in (1,3) |
| (d) no 3-marker on O vs t in O; f* >= 2; every 5-marker | 123-141 (SG), 144-150 (R4S), 160-177 (CIS/EQS), 27-28 (labels) | i* never in Q; e = t ordering; k <= 3 suffices without t; label coprimality for every placement |
| O-values in every orientation | 94-100 (P1) | E3-L2 (both families, any orientation) + the Z11 (a) 5-argument re-proved |
| assembly | 179-252 | BUD (FAM), T16, ONE, TRI, FB, DEEP (FAM), Steps 1-2; R0 lift |

## 6. Location map of Sun instances and index/count steps
| Candidate lines | Step to verify |
|---|---|
| 97-100 | x_vu = 5, h_d = 0: lambda_u = 5 ell_u and lambda_d = 2^(e_d-1) w_d coprime (Sun(2)); val 5/6 + 1/2 > 1. |
| 107-112 | light fibres of a subset Q: count, avoidance, incidence bound with y vanishing off Q. |
| 114-117 | VFC light set of Q: inside every X_j, outside every D_j, measure >= 1/gcd. |
| 126-138 | SG chain: T_1 = L_1; gcd 6 at each step (2-, 3-, 5-, w-parts, e = t case); k <= 3; k = 3 => product equality => Lemma 2 at d vs #both = #neither >= 1 (degrees n_d/2, own fibre); final gcd 6 at v = t and v != t. |
| 145-150 | R4S certificate: 1-labels isolated (Sun(2)), 2-labels and d pairwise gcd 2 (Sun(3)); 11/12 > 5/6. |
| 161-177 | CIS steps 1-5 (Sun(3), saturation 5/6, Sun(2) parity, Sun(3) disjointness, 2/6 + 2/6 > 1/2); EQS one-tight (Sun(2)). |
| 180-206 | apex identity, triangle bounds, prime-to-6 parts, BUD, T16, ONE. |
| 215-234 | FB cases (N), (i)-(vii), including t absent (case (a) only). |
| 237-252 | DEEP via FAM (DG_x); Step 1 triangle/diamond; Step 2 complement of a diamond; R0. |

## 7. Review contract
Independently re-derive every claim, especially: OR from the accepted statements (not from headings); FAM's application of
E3-C2/DG to the actual inverted configuration in (1,1) and M13-A's exact scope in (1,3); SG in both the t-case and the no-t case
(f* >= 2, 5-marker on i*/d/O); R4S/CIS at t and at a 5-marked O-vertex; P1's 5-argument for both families; FB with and without t;
DEEP's use of DG (b)'s alternatives. Return FATAL/MAJOR/MINOR counts per claim group (OR/R/FAM; P1; Lemmas 1/1'/2; SG;
R4S/DEG; CIS/EQS; P2-P4/BUD/T16/ONE/TRI; FB; DEEP/K62X) with exact file:line and minimal repair. Empty findings are valid.
Imports only at the table's literal scopes; pending texts are not premises.

## 8. Packaging metadata
39 inclusive-range excerpts from 22 sources; selected raw UTF-8 bytes 98,506 (<= 100,000). Every whole-file
sha256 and every range was re-checked immediately before this write. Byte/hash operations are packaging, not science runs.
Manifest: `K/review-excerpts-FULL-v1.json`, sha256 `ec110973f2a385daf2341dc62a6bc73f6411d47098fa4b7853ab6245179ef3f8` (9,624 B).
