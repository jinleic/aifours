# SUN7-COMP-v1: proof-level composition of Sun(7) — CONDITIONAL on two untrusted new nodes [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T16:35:05-0700, immediately before this exclusive write. Owner SunM13MixedFibres, slot math-1.
- **Frozen scope:** `C/SUN7-COMP-SCOPE-v1.md`, sha256 a7f304f0456e9ff5011b300ce8d1e06d3ecd6e1dd398353e1a59162fa6ae0c38 (frozen before this
  text; it discloses the pre-freeze reading and the expected shape). **Outcome (A) of that scope:** a complete
  CONDITIONAL composition; no missing class or mathematical interface was found (section 8).
- **Authority:** `RUN/control/mathematics-slot-transition-sun-composition-20261019-1623-v1.json` (769525e0…c3b5) and
  `RUN/review/sun7-X1-stale-route-correction-v1.json` (d272679d…5ff0).
- **What this file is.** An ASSEMBLY. It proves Sun(7) only CONDITIONALLY on two untrusted new nodes, (H-NF) and (H-A2X),
  and relative to accepted nodes three of which are computer-assisted (Sun(5), Sun(6), StageB). It is NOT a proof of
  Sun(7), grants no acceptance, and claims no novelty, Lean or human review. New items here: Lemma CE-LIFT (restated),
  the coverage check of section 1, Lemma K7-SPLIT, Theorem SUN7-COMP (conditional), and the DAG/gate tables.
- Root aliases (exact absolute prefixes): O16 = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016`;
  S = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7`; K = S`/continuations/k7-complement-f`;
  A = S`/continuations/k7-a2-closure`; C = S`/continuations/sun7-composition`; RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`;
  R16 = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review`.

## 0. Target, CE and the finite-core lift
**Sun(7)** (O16/sun-coset7/README.md line 11, sha256 2a6d6d6e…3fd1): for any group G, subgroups U_1..U_7 of finite index
(possibly equal) and pairwise disjoint left cosets g_1U_1..g_7U_7, some i < j has gcd([G:U_i],[G:U_j]) >= 7.
**CE** (README lines 33-35): a FINITE group with seven pairwise disjoint left cosets g_iU_i and gcd(n_i, n_j) <= 6 for all
i != j, n_i = [G:U_i]; n_i = 2^(e_i) 3^(f_i) 5^(h_i) w_i (the written verdict's overlay A-1 names the 5-exponent h_i),
A_p = {i : p | n_i}, C = A_2 cap A_3, E = {i : e_i >= 2}, a = |A_5|, D = V \ C.
**Lemma CE-LIFT (restatement of accepted R0).** If Sun(7) fails for some G, U_i, g_i, then a CE exists. *Proof.* Failure
means gcd(n_i, n_j) <= 6 for all i != j. R0 (README lines 27-29; accepted, written verdict R16/sun-coset7-written-parent-verdict-v1.md
(73a25ba6…9f35) line 18): N = intersection of the cores is normal of finite index, contained in every U_i; every n_i,
every [G : U_i cap U_j] and pairwise disjointness are preserved in G/N. So the image data in the finite group G/N is a
CE. QED. No minimal-order frame, exponent cap or common index factor is assumed here or below.

## 1. Exact six-class coverage (accepted reduction; this section only re-checks exhaustiveness)
Accepted: README sections 2-5 (P0, P1, Theorem R1(7), R1a-c, D2, D2', class table lines 85-96) with the written verdict
(73a25ba6) lines 20-21 and its mandatory overlay (lines 44-56): "The exact remaining six classes are K7, K6.2*, K6.3, K5.2*,
K5.3, KII". The case tree below follows the accepted statements literally; every leaf is a class or an accepted removal.
| node of the accepted case tree | condition | leaf | accepted authority |
|---|---|---|---|
| a >= 3 | three 5-vertices | impossible | R1(7) proof step 1 with Sun(6) |
| a = 2 | R1(7) (II): A_5 = {x, y}, C = V \ {x, y} | **KII** | R1(7) step 2 |
| a <= 1 | R1(7) (I): \|C\| >= 4 (step 3, Sun(5)); D uniformly type 2 (D in A_2\A_3) or type 3 (D in A_3\A_2) | split by \|C\| | R1(7) step 3 |
| \|C\| = 7 | D empty, a <= 1, C = V | **K7** | class table line 91 |
| \|C\| = 6, type 3 | D = {d} in A_3 \ A_2 | **K6.3** | line 93 |
| \|C\| = 6, type 2, gcd(n_d, n_i) = 2 for all i in C | | impossible | D2 (README line 82; rules-k7-v1 section 3, overlay B-1) |
| \|C\| = 6, type 2, some gcd(n_d, n_i) != 2 | P1(i): that gcd is 4, so d, i in E; P1(iii): \|C cap E\| <= 1, so C cap E = {i} =: {i*} | **K6.2*** | line 92 |
| \|C\| = 5, type 3 | D = {d_1, d_2} in A_3 \ A_2 | **K5.3** | line 95 |
| \|C\| = 5, type 2 | R1b: D in E; C cap E empty -> impossible (D2'); C cap E = {i*} -> K5.2* | **K5.2*** | R1b (line 73), D2' (line 83), line 94 |
| \|C\| = 4, type 3 | \|D\| = 3 | impossible | R1a (line 71), Sun(4) |
| \|C\| = 4, type 2 | \|D\| = 3 | impossible | R1b + R1c (lines 73-79), Sun(3) + Prop 4.5 |
Since a in {0,1,2} (R1(7)) and 4 <= \|C\| <= 7 in (I), the rows exhaust every CE. **Corollary COVER:** every CE lies in
K7 cup K6.2* cup K6.3 cup K5.2* cup K5.3 cup KII (with the README section-5 definitions).

## 2. Class exclusions at their literal scopes
| class | literal accepted statement (source lines) | mandatory overlays | accepting verdict | why the literal hypothesis covers the README class |
|---|---|---|---|---|
| **KII**, **K5.2*** | "no configuration of the residual classes K5.2* (with the D2' case) or KII exists" (R16/sun-coset7-stageB-classes-parent-verdict-v1.md line 5) | written-verdict overlay F-2/F-3/F-4 (lines 52-54) | same file, sha256 fd14952c…c13f | named classes verbatim; the K52 universe deliberately over-covers K5.2* incl. D2' (line 20); the KII universe matches the README class (line 26). COMPUTER-ASSISTED (section 6) |
| **K5.3** | bridge "X1 => K5.3 (restated)" (O16/sun-coset7/rules-k7-addendum-v1.md line 159; accepted written verdict line 24) + X1: "No group admits five pairwise disjoint left cosets of finite-index subgroups with indices (3r_1,3r_2,6r_3,6r_4,6r_5), where r_1,r_2 are odd and all five r_i are pairwise coprime" (RUN/review/x1-written-parent-verdict-v1.md line 5) | X1 clarification (49f956b2…c0a9) and overlays 1-2 (verdict lines 19-20) | RUN/review/x1-written-parent-verdict-v1.md, 84d7d8ab…0c4c | K5.3: D = {d_1, d_2} in A_3 \ A_2 has e = 0, so r_d = n_d/3 is odd; C-vertices give r_c = n_c/6; gcds 3 (pairs meeting D) and 6 (C-C) make the five r's pairwise coprime; deletion keeps disjointness (addendum line 159). StageA is NOT used |
| **K6.2*** | Theorem K62X (S/continuations/k62-full-closure/K62-FULL-v1.md lines 241-243; class at lines 17-24) | worker erratum K62-FULL-erratum-v1.md (4b8ae281…0cc0); parent provenance erratum (15ce0f5d…65ca); parent errata v1 (61c1c02d…9691) and v2 (299e73f4…5c52) | RUN/review/sun7-K62-FULL-parent-verdict-v1.md, f3b22e53…1f0c | lines 17-24 restate README line 92 with P0-P1: d in A_2\A_3 (no factor 3), i* the unique C cap E vertex (e* >= 2, f* >= 1), O = C \ {i*} with e = 1, min(e_d, e*) = 2, gcds 6/4/2; every 3-/5-marker placement and all exponents/cofactors included (lines 22-24, 241-243; verdict line 9) |
| **K6.3** | K63-D: "no K6.3 configuration with f_d = 1" (S/K63-D-v1.md line 24); K63-E: "No K6.3 configuration has f_d >= 2 and no vertex with e >= 2" (S/K63-E-v1.md line 19); K63-RES: "no K6.3 configuration has f_d >= 2 and a C-vertex with e >= 2" (S/continuations/k63-residue/K63-RES-v1.md lines 42-43) | K63-D errata v1-v2; K63-E errata v1-v3; K63-RES errata v1-v2 (hashes in section 5) | RUN/review/sun7-K63DE-K735-parent-verdict-v1.md (1a1c6390…3919) lines 9-10; RUN/review/sun7-K63RES-parent-verdict-v1.md (5ac59529…7bac) line 5; correction RUN/review/sun7-K63-frontier-status-correction-v1.json (b41e47fc…) line 9 | d in A_3 \ A_2 gives e_d = 0 and f_d >= 1; a 2-marker (e >= 2) can only lie in C. So exactly one of f_d = 1 / (f_d >= 2, no C-vertex with e >= 2) / (f_d >= 2, some C-vertex with e >= 2) holds; the three statements cover all marker/exponent data (verdict K63RES line 5) |
| **K7** | Lemma K7-SPLIT (section 3) + (H-NF) + accepted (a1) closure (RUN/review/sun7-K7-R2-parent-verdict-v1.md line 5: "(a1) contains no actual disjoint-coset configuration, in any group") + (H-A2X) | R2 verdict reading order (its lines 19-31) | R2 verdict 9b0f7df5…b926d | section 3 |
Each authority above is stated for arbitrary groups with finite-index subgroups (or for finite groups plus R0); a CE is a
finite group, so it applies directly.

## 3. Lemma K7-SPLIT (new, elementary; proved here, not imported from the candidate K7-NF)
Let a configuration of class K7 be given (README line 91: a <= 1, C = V; all 21 pairwise gcds 6). Then n_i = 6 r_i with
r_1..r_7 pairwise coprime (gcd(6r_i, 6r_j) = 6 gcd(r_i, r_j)). Put Z = {i : 2 | r_i}, T = {i : 3 | r_i}, P = {i : 5 | r_i};
each has at most one element, since a prime dividing r_i and r_j (i != j) divides gcd(r_i, r_j) = 1. Define
- **F** (frozen in the K7-NF transition `RUN/control/six-slot-written-resumption-20261019-1603-v1.json`, ac09b465…f0f8):
  \|Z\| = \|T\| = 1 and Z != T;
- **(a1)** (R2 verdict line 9): z != t with r_z = 2^E 5^(Bz) w_z, r_t = 3^A 5^(Bt) w_t, E, A >= 1, Bz Bt = 0, the five other
  vertices unmarked (r_u = w_u), all w's pairwise coprime and prime to 30;
- **(a2)** (A/K7-A2-SCOPE-v1.md lines 14-17): distinct z, t, p with r_z = 2^E w_z, r_t = 3^A w_t, r_p = 5^B w_p, E, A, B >= 1,
  the four other vertices unmarked, all w's pairwise coprime and prime to 30.
**Lemma K7-SPLIT.** Every K7 configuration lies in exactly one of: K7 \ F, (a1), (a2).
*Proof.* If not in F, it is in K7 \ F. In F let Z = {z}, T = {t}, z != t. Write r_i = m_i w_i with m_i the {2,3,5}-part of
r_i and gcd(w_i, 30) = 1. Since \|P\| <= 1, either P is empty or P = {z} or P = {t} or P = {p} with p not in {z, t}. Every
vertex outside Z cup T cup P has m_i = 1 (its r_i is prime to 30). Since Z = {z} != {t} = T, m_z has no factor 3 and m_t no
factor 2. In the first three cases m_z = 2^E 5^(Bz), m_t = 3^A 5^(Bt) with E = v2(r_z) >= 1, A = v3(r_t) >= 1 and at most
one of Bz, Bt positive (both 0 if P is empty): exactly (a1). In the last case m_z = 2^E, m_t = 3^A,
m_p = 5^B with B >= 1: exactly (a2). The w's are pairwise coprime (they divide the pairwise coprime r's) and prime to 30.
(a1) and (a2) are disjoint (the 5-marker lies in {z, t} or outside), and both lie in F. QED

## 4. Theorem SUN7-COMP (conditional)
**Hypotheses (UNTRUSTED new nodes; neither is accepted; no review result is used):**
- **(H-NF)** Theorem K7-NF (K/K7-NF-v1.md, sha256 734613fd21d9ea21aa940293c489f40549b74a3ac13d1ce3720db6bc98f73e97, lines 84-86): no group
  with finite-index subgroups contains a K7 configuration outside F.
- **(H-A2X)** Theorem A2X (A/K7-A2-UNIT-3-v1.md, a2b40a9e…59be, lines 143-146, as the acyclic join with A/K7-A2-UNIT-1-v1.md
  79d948bf…9d51 and A/K7-A2-UNIT-2-v1.md 1bef6d8c…942b): no configuration of K7(a2) exists in any group with finite-index
  subgroups, for all E, A, B >= 1 and all cofactors.
**Theorem SUN7-COMP [CANDIDATE_UNVERIFIED; CONDITIONAL].** Assume (H-NF) and (H-A2X). Then, relative to the accepted nodes
of section 5 at their literal scopes (including the computer-assisted Sun(5), Sun(6) and StageB nodes), Sun(7) holds for
every group.
*Proof.* Suppose Sun(7) fails. By Lemma CE-LIFT there is a CE; by Corollary COVER it lies in one of the six classes.
KII and K5.2*: impossible by StageB (section 2). K5.3: the bridge gives an X1 configuration in the same finite group,
impossible by the accepted X1 theorem. K6.2*: impossible by K62X. K6.3: impossible by K63-D, K63-E or K63-RES according to
the exhaustive three-way split. K7: by Lemma K7-SPLIT it lies in K7 \ F (impossible by (H-NF)), in (a1) (impossible by the
accepted (a1) closure) or in (a2) (impossible by (H-A2X)). Every case is contradictory. QED
*Remarks.* (1) (H-NF) is itself only an assembly of the accepted theorems K7-M0, K7-M1, K7-Z2, K7-35, K7-U1 and Z23-P5; its
proof is in its own review unit. (2) (H-A2X) carries the only genuinely new outstanding mathematics. (3) Removing either
hypothesis leaves the exact open remainder: K7 \ F (resp. (a2)); nothing else is open at the class level.

## 5. Exact dependency DAG
Statuses: ACC = accepted at the cited verdict's literal scope with all listed overlays; NEW = this lane's untrusted
candidate. "->" lists direct imports. Every full or abbreviated sha256 below was recomputed by me from the file bytes in this session, except the StageB checker digest (quoted from the StageB verdict line 10) and the external Zhu import.
| id | node and scope | text of record (sha256) | mandatory overlays | acceptance (sha256) | status | direct imports | computation |
|---|---|---|---|---|---|---|---|
| N0 | Sun(7) statement, L0.1/L0.2/L0.6 (Sun(2)), deletion, R0, CE, P0, P1 | O16/sun-coset7/README.md (2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1) lines 11, 21-52 | overlay A-1 | R16/sun-coset7-written-parent-verdict-v1.md (73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35) lines 16-18 | ACC | — | none |
| N1 | Sun(3), Sun(4) for every group | Zhu, arXiv:0807.2207, Thm 1.1 (external) | — | contract accepted import (README line 15; written verdict line 60) | ACC import | — | none |
| N2 | Sun(5) for every group | O16/sun-coset5/proof-v4.md (3d17efcc034cca643515e581fa4667515086d0844a58b951e2641080d6c94516) | O16/sun-coset5/rules-v1-erratum-v3.md (1b3e126e1c398a71…) | R16/sun-coset5-parent-verdict-v1.md (2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301) | ACC | N0, N1 | **computer-assisted** (verdict lines 5, 19-23); its proof uses a minimal-order frame internally (verdict line 18), not a frame of this composition |
| N3 | Sun(6) for every group | O16/sun-coset6/proof-k6-v3.md (2aa4fa430dfb414d…) | O16/sun-coset6/rules-k6-erratum-v3.md (71cfeccbfb708c11…) | R16/sun-coset6-parent-gate-verdict-v1.md (efe1d849a082404d778bb2bde6984b62915822f8a381ec7c9019948b0a241e29) | ACC | N0-N2 | **computer-assisted** (verdict lines 7, 17) |
| N4 | M-S Prop 4.5 tuple (2r_1,4r_2,4r_3,4r_4) not G-harmonic | O16/sun-coset5/proof-v4.md section 2 | — | Sun(5) verdict; written verdict line 21 | ACC | N0 | written |
| N5 | written rules: VFC, T/K/P, RPLP, CAP, D2, D2'; X1 bridge | O16/sun-coset7/rules-k7-v1.md (77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee); O16/sun-coset7/rules-k7-addendum-v1.md (fb2c306b17a258181bb770c7c6c38585da77c0e312c68463cee7dc0f15fd1066) | O16/sun-coset7/rules-k7-erratum-v1.md (75a61776871748a53191d4d3b6fe3d4435c6b8216929a9c60067b9f28d705560); verdict overlay items 1-9 | written verdict lines 20-24, 44-56 | ACC | N0-N4 | written |
| N6 | six-class reduction (R1(7), R1a-c, D2, D2'; Corollary COVER) | README lines 54-107 | overlay | written verdict lines 20-21 | ACC (coverage re-checked in section 1) | N0-N5 | written; **N2 load-bearing** (\|C\| >= 4), **N3 load-bearing** (a >= 3) |
| N7 | LFC, INV (E6), ROW-U, K7-M0 | S/K7-LFC-INV-v1.md (45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c) | S/K7-LFC-INV-erratum-v1.md (7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5) | RUN/review/sun7-lfc-inv-parent-verdict-v1.md (8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18) | ACC | N0-N3, N5 | written; LFC applies Sun(t), t <= 6, to simultaneous fibre pieces |
| C1 | KII and K5.2* (incl. D2') excluded | StageB receipt (e044a4eb…e074), checker v2 (f4af3f7c…7b54) | written-verdict overlay F-2/F-3/F-4 | R16/sun-coset7-stageB-classes-parent-verdict-v1.md (fd14952c31852fe6c9b291114f99809f090a5f3bbb0caf07065ba50fffd3c13f) | ACC | N0-N6 | **computer-assisted, one independent checker** (verdict line 46); F-1 permanent (line 40) |
| C2 | K5.3 excluded (bridge + X1) | RUN/review/x1-written-parent-candidate-v1.md (09948b0cc35203683abd1ff0ccf50d10ff9b5fbb2797b5ec8a817568ce0825af); addendum line 159 | RUN/review/x1-written-parent-candidate-v1-clarification-v1.md (49f956b2c6d0b8a17abaf2bd59e070b483792243f49d2fb54ac9def65297a0c9); verdict overlays 1-2 | RUN/review/x1-written-parent-verdict-v1.md (84d7d8abef60fad092713fbf9530abba03ce0d269eb24a0494ac8d2729d40c4c) | ACC | N0 (R0, Lagrange, product formula); pairwise fibre bound proved in the clarification | written; computation-free (verdict line 5) |
| C3 | K6.2* excluded (K62X) | S/continuations/k62-full-closure/K62-FULL-v1.md (fabf04dd6abb1d3ec7e71b1cc3d459e008e9a96b5186b5a1f571fedac1312e5b) | K62-FULL-erratum-v1.md (4b8ae281…0cc0); RUN/review/sun7-K62-FULL-parent-provenance-erratum-v1.md (15ce0f5d…65ca); RUN/review/sun7-K62-FULL-parent-erratum-v1.md (61c1c02d…9691); …-erratum-v2.md (299e73f4…5c52) | RUN/review/sun7-K62-FULL-parent-verdict-v1.md (f3b22e536ea6f0e93647cde167a50101735baf4bf4d13ee71c4e704e3da21f0c) | ACC | N0, N5, N7; E3 (RUN/review/sun7-K62E3-parent-verdict-v1.md 576969dd…); DG/G5/G6 (sun7-K62-SH-DG-parent-verdict-v1.md cae455c3…); M13-A items 1-2 (sun7-K62-M13-parent-verdict-v1.md 2fac7a30…, erratum 99276f6d…) with their CAP-62/RC-i* interfaces (verdict line 23; erratum v2 item 3) | written; transitive N2/N3 |
| C4 | K6.3 excluded: K63-D, K63-E, K63-RES | S/K63-D-v1.md (f4027779…d255); S/K63-E-v1.md (73bcde10…4de8); S/continuations/k63-residue/K63-RES-v1.md (1542a551…7515) | K63-D errata v1 (75478241…), v2 (891567ee…); K63-E errata v1 (b5d07d06…), v2 (20fb0b0a…), v3 (159def41…); K63-RES errata v1 (e70a5518…), v2 (c31d7623…) | RUN/review/sun7-K63DE-K735-parent-verdict-v1.md (1a1c639093dd334cb404a8216ca70a839ea85454978c9fdf354cc5bc577a3919); RUN/review/sun7-K63RES-parent-verdict-v1.md (5ac595295727218cd86d0888720213972fe0520f64cea8d93a5c50ef18ed7bac); correction json (b41e47fc15cb9030…) | ACC | N0, N5, N7 | written; **N3 load-bearing in K63-RES** (verdict line 19) |
| K0 | Lemma K7-SPLIT | this file, section 3 | — | — | NEW | N0 | written, elementary |
| K1 | (H-NF) Theorem K7-NF | K/K7-NF-v1.md (734613fd…3e97) | parent wording erratum RUN/review/sun7-K7-NF-parent-erratum-v1.md (21f31a50ae7a1fcb1746a7f9108892a108e6cdab9c381b880857561293d623f2; proof line 143 wording only) | none; parent review freezes (e3f4c0d7…373f; Claude v2 1d990afd…ba6c) are not verdicts | NEW, UNTRUSTED | N0, N7 (K7-M0); K7-M1 (sun7-M1-parent-verdict-v1.md 7121ceed…), K7-Z2 (sun7-Z2-parent-verdict-v1.md 0f6b9aa3…), K7-35 (C4's verdict 1a1c6390…), K7-U1 (sun7-U1-parent-verdict-v1.md 44dfbe85…), Z23-P5 (sun7-Z23P5-parent-verdict-v1.md 7179e564…) at literal scopes (its section 1) | written; transitive N2/N3 |
| K2 | (a1) closure | R2 texts per RUN/review/sun7-K7-R2-parent-verdict-v1.md lines 21-29 | R2 verdict reading order lines 31, 40 | RUN/review/sun7-K7-R2-parent-verdict-v1.md (9b0f7df54165575c2cee4818896738e886ae77ff2fcd6c1a328d5946cd1b926d) | ACC | N0, N5, N7; A1/A2 repairs (RUN/review/sun7-K7-A1-A2-repairs-parent-verdict-v1.md 2a7c5b6c…6966); RICH/D23P (RUN/review/sun7-K7-D23RICH-D23P-parent-verdict-v1.md 1167bc4f…aec0) (R2 verdict line 46) | written; transitive N2/N3 |
| K3 | (H-A2X) Theorem A2X | A/K7-A2-UNIT-1-v1.md (79d948bf6ee3b6ae7a9737af604e285d8d70d7df1db9bdb89a609d45c8199d51); A/K7-A2-UNIT-2-v1.md (1bef6d8ca1b0b62c15dbb703e96cc73c26b8c3295ebd5953965d205075a2942b); A/K7-A2-UNIT-3-v1.md (a2b40a9eecc1f8373cca60355217f9a5ac449105fc77886616f6cdad387d59be) | none of its own | none; parent records RUN/review/sun7-K7-A2-unit2-parent-premise-addendum-v1.md (cca3de2a…5b11) and review freezes are not verdicts | NEW, UNTRUSTED | N0, N5, N7; A1/A2 verdict items Lemma F, FG-a2, D23-a2, S1-S5, BRIDGE (OV1 A2.10), TRANSFER (OV2 V2.7); RICH/D23P (unit-3 table, lines 16-26) | written; transitive N2/N3; direct Sun(2)-(4) |
| T | Theorem SUN7-COMP | this file, section 4 | — | — | NEW, CONDITIONAL | N0, N6, C1-C4, K0-K3 | inherits N2, N3, C1 |
The graph is acyclic: N0 -> N1..N7 -> {C1..C4, K1..K3} -> T, with K0 -> T; no class node imports another class node,
and neither K1 nor K3 imports T or each other.

## 6. Computation boundary
**Load-bearing computer-assisted nodes (the conditional theorem is computer-assisted relative to them):**
- **N2 Sun(5):** finite pattern bridge with independent verifier (Sun(5) verdict lines 19-23). Used in N6 (R1(7) step 3:
  \|C\| >= 4), in every LFC application with five simultaneous pieces, and inside N3's proof.
- **N3 Sun(6):** primary finite verifier checker_v2 (Sun(6) verdict line 17). Used in N6 (R1(7) step 1: a >= 3), in C4's
  K63-RES (all-gcd-5 six-neighbour case), and in LFC applications with six pieces.
- **C1 StageB:** the only authority for K5.2* (incl. D2') and KII; exhaustive certificate re-walk by ONE independently
  authored checker plus parent re-execution (StageB verdict lines 10-32, 46).
**Recorded but NOT load-bearing:** StageA (K5.3 now rests on C2; correction json d272679d); the K63-RES exact-weight row
controls (K63RES verdict line 12: "not a premise"); producer/engine counts; every exploratory search. **Written-only
class chains:** C2 (computation-free), C3, C4, K1-K3 (each transitively imports N2/N3 through N6/N7).

## 7. Full-result gate table (no automatic promotion)
| gate | requirement | recorded status at this writing | source |
|---|---|---|---|
| G1 | (H-NF): independent two-family reviews and a parent verdict | open. First family: Codex accepts, 0F/0M/1m (RUN/review/sun7-K7-NF-codex-v1.prompt.stdout.txt, dabb4ede…, as quoted in the parent erratum line 3); the 1m is fixed by parent wording erratum 21f31a50…23f2. Second family (Claude) frozen (1d990afd…ba6c), no result; no parent verdict | RUN/review/sun7-K7-NF-parent-erratum-v1.md; RUN/review/sun7-K7-NF-claude-v2-freeze-v1.json |
| G2 | (H-A2X): units 1-3 two-family reviews and a parent verdict | open. Per parent IRC: Codex mathematical passes for all three units (unit 2 on the corrected OV2 v2 snapshot, reported 0F/0M/0m, "d67c75b2"); Claude units 1-2 running, unit 3 next. Parent independent derivation check RUN/review/sun7-K7-A2-parent-mathematical-check-v1.md (397ae0d8596f5fa3d86d37d1283dc5abf5c2807bd5814aff707a456b31c23575) reports no additional gap and is NOT a verdict (file hashed, content not used) | parent IRC; RUN/review/sun7-K7-A2-unit*-review-freeze-*.json |
| G3 | this composition: two-family review and parent composition check | open | this unit |
| G4 | load-bearing computation: two independently authored checkers (StageA verdict RUN/review/sun7-stageA-K53-parent-verdict-v1.md, 0927a0d4…822b, line 24) | C1: ONE checker recorded (StageB verdict line 46), so NOT MET as recorded. N2/N3: status to be established by the parent's gate audits; not determined here | StageA verdict line 24; StageB verdict line 46 |
| G5 | process | StageB F-1 late certificate/RPLP freeze is a permanent deviation (StageB verdict line 40) | — |
| G6 | formal / human | none exists for any node | all verdicts |

## 8. Mathematical gaps and exact obligations
- **No missing class and no missing mathematical interface was found.** Section 1 re-checks the accepted case tree;
  section 2 matches each class to a literal accepted statement; Lemma K7-SPLIT matches F, (a1) and (a2) to the exact
  definitions used by K7-NF, the R2 verdict (line 9) and the A2 scope (lines 14-17).
- **Exact outstanding obligations for an unconditional full-Sun(7) record:** G1 and G2 (the two untrusted hypotheses),
  G3 (this assembly), and G4 for C1 (a second independently authored checker for K5.2* incl. D2' and KII, or a written
  proof of those classes) and for N2/N3 as the parent's audits determine. G5 stays disclosed.
- Interface notes for reviewers (not gaps): StageB excludes CEs under the accepted written rules, so it applies to the
  CE of Lemma CE-LIFT; CAP is an accepted written lemma (written verdict lines 23, 42), not an exponent-cap assumption;
  the minimal-order frame occurs only inside N2's own proof.

## 9. Review units (each independently complete, <= 100 KB raw excerpts)
U0 composition (this file, scope, authorities' literal statements); U1 K7-NF (full body + literal imports); U2 A2 unit 1
(full body); U3 A2 unit 2 completed with the whole OV2; U4 A2 unit 3 completed with its whole body. Exact files and hashes
are in `C/review-index-COMP-v1.json`. Context-only lines in U0 never replace the proofs of K0-K3: K0 is proved here,
K1-K3 are proved in full in U1-U4.

## 10. Scope and non-claims
Claimed (CANDIDATE_UNVERIFIED, written, single author): Lemma CE-LIFT (restated), Corollary COVER (re-check of an accepted
reduction), Lemma K7-SPLIT, Theorem SUN7-COMP as a CONDITIONAL statement, and the DAG/gate tables. Not claimed: Sun(7);
acceptance of K7-NF, A2X or this file; that any gate is met; novelty, priority, Lean, human review. No scientific computation was run; only hash, byte and line-range metadata operations.
