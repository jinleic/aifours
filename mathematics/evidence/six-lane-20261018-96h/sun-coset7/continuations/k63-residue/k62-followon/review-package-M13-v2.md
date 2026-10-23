# M13 written review package v2: complete corrected snapshot, orientations (1,3)/(3,1)

Owner Sun63Successor; `/bin/date` 2026-10-19T09:01:27-0700. All M13 claims are CANDIDATE_UNVERIFIED. No model call or science computation is
launched by this worker. This is a standalone complete snapshot for a FRESH review, not a delta-only packet.

## 1. Reading order, repair and exact status
Read whole A-D through M13-ov. Old A-D bytes and all previous source pins are unchanged. The sole repair replaces C58-63:
it explicitly derives the extra alpha-row bound from the new alpha*-granularity by empty-fibre counting, and derives the
other row after inversion. No bound, centre, orientation or strictness changes. General RC outside RC-O/RC-i* is NOT an
accepted black-box rule. The new calculation is a proof obligation here.

Codex's earlier report (c8c4184bb4c71df3a34f04dcf1f03424b76df60ea9b229216eea6e89c14ef17d, R/sun7-K62-M13-codex-v1.prompt.stdout.txt) returned0F/0M/1MINOR; its M1 is the
proof-reference issue, not an independent premise. Claude's terminal NO_VERDICT was a capacity refusal, rc1, not a math
conclusion. This packet requests independent re-derivation of EVERY new A-D claim with the repaired proof.

CAP/DT is now accepted by V-CAP (84061c6f…); all former CONDITIONAL ON CAP/DT labels are discharged ONLY for its exact
C1/RC-O/RC-i* interfaces. New B/C/A dependencies are still unreviewed, not discharged by that verdict. Marked centres,
(1,3)/(3,1), full K6.2*, K7 and Sun(7) remain OPEN. Sun(5)/(6) remain computer-assisted transitive imports.

## 2. Candidate setting and VERBATIM statements
K6.2*, e_d>=4, e*=2, V={d,i*} disjoint-union O, |O|=5; work in (alpha_di*,alpha*_di*)=(1,3). INV transfers (3,1) by
swapping families. The class forces t in O, f*=1; the5-marker is anywhere admissible. The w's are pairwise coprime and
prime to30. Whole A-D proofs and the whole erratum are excerpted. Quotes below are raw source bytes at the given lines.
### A: `K/K62-M13-A-v1.md`; SHA256 `77ce4077584582c699ce1bec870f2b19c55242bfc05aac99febcfbd69c466a8d`
A:33-39:
```text
- **(a) Counts.** P*_c meets exactly n_d/2 fibres (c in O); P*_(i*) meets exactly 3 n_d / 4 fibres; none of them is U_d.
- **(b) Size.** |S*_F cap O| <= 3 for every F. Moreover |S*_F| <= 4, and |S*_F| = 4 only if {t, i*} is contained in
  S*_F.
- **(c) Complements.** For c in O: c is not in S*_F iff F lies in U_cU_d, a union of n_d/2 fibres. Likewise i* is not
  in S*_F iff F lies in U_(i*)U_d, a union of n_d/4 fibres.
- **(d) Counting facts.** sum over F of (|B*(F)| - 2) = n_d/2, every term is >= 0, and #{F : |B*(F)| >= 3} >= n_d/4 + 1.
- **(e) Four-piece fibres.** At least n_d/4 + 3 fibres have |S*_F| = 4; each of them contains t and i*.
```
A:70-70:
```text
- **(DG-1\*)** For non-empty Q contained in O, N*(Q) is a positive multiple of n_d / 2^(min(e_d, v2 T_alpha(Q))).
```
A:73-77:
```text
- **(DG-2\*)** Put A*_4 := #{F : |B*(F)| >= 4}. Then:
  - (i) N*(O) + A*_4 <= n_d/4 - 1;
  - (ii) the sum over 3-subsets R of O of N*(R) is <= n_d - 2 + 3 N*(O);
  - (iii) the sum over 4-subsets Q of O of N*(Q) is <= n_d/4 - 1 + 3 N*(O);
  - in particular N*(O) <= n_d/8 - 1/2.
```
A:85-90:
```text
- **(Theorem DG\*)** In (1,3), for the alpha-family, write r_S := min(e_d, v2 T_alpha(S)).
  - **(a)** If r_Q <= 4 for all five 4-subsets Q of O, then N*(O) <= n_d/16 and **the sum over the ten 3-subsets R of O of
    2^(-r_R) is <= 19/16 - 2/n_d**.
  - **(b)** Under the hypothesis of (a), at least two 3-subsets R have r_R >= 4, or exactly one does and it has r_R = 5.
    In the second case its alpha-values are (4,4,4), tau_alpha(R) = 16 and e_d >= 5. By DG-3 (G3 form, applied to
    Gamma*), every R with r_R >= 4 has alpha-values (2,4,4) or (4,4,4) and tau_alpha(R) in {8, 16}.
```
A:98-98:
```text
- **(C2\*)** In (1,3), write n_k(alpha) := #{O-pairs with alpha = k}. Then **n_4(alpha) >= 2 n_1(alpha) + 2**.
```
A:105-105:
```text
- **(C1\*)** In (1,3): v2 T_alpha(Q) >= 3 for every 4-subset Q of O, and v2 T_alpha(O) >= 4.
```
A:110-112:
```text
Write N_ab for the number of O-pairs with joint value (alpha, alpha*) = (a, b), for (a, b) in
J_O = {(4,1), (4,2), (1,4), (2,4), (1,1), (1,2), (2,1), (2,2)} (K62-E3 Lemma 2, Z11 (a), INV (b)). In (1,3):
  **2 N41 + 2 N14 + 5 N11 + 3 N12 + 3 N21 + N22 <= 6.**
```
### B: `K/K62-M13-B-v1.md`; SHA256 `455c58f9d35cc165f666eeaec9462e6b6ab6286196450532e619d6c0b9810058`
B:30-30:
```text
**For either family x in the setting above, |K_x| != 4.**
```
B:51-51:
```text
**In (1,3), |K_alpha*| != 5, hence |K_alpha*| <= 3 by B1.**
```
B:62-62:
```text
**In (1,3), |K_alpha| != 5, hence |K_alpha| <= 3 by B1.**
```
B:74-77:
```text
In (1,3), **|K_alpha| <= 3 and |K_alpha*| <= 3**. Consequently each i*-row has at least two O-entries >= 3. In particular,
- there are at least two vertices c in O with alpha_(i* c) >= 3, and for each such c, alpha*_(i* c) <= 3 (INV (b));
- for every v in O there is c_0 in O minus {v} with **alpha*_(i* c_0) <= 3**.
The analogous statement in (3,1) follows after exchanging alpha and alpha*.
```
### C: `K/K62-M13-C-v1.md`; SHA256 `13f2c8dc42a95be24b819ec3cf68dbb178140bb2cd876b2c491d941d1e552e12`
C:23-24:
```text
Let v be an unmarked O-vertex. **If there is c_0 in O minus {v} with alpha*_(i* c_0) <= 3**, then
  **gcd(n_v, T_alpha*(V minus {v})) = 6.**
```
C:66-68:
```text
Let y be either family, y' its opposite, v in O unmarked and a != b in O minus {v}. In the Phi^y-configuration at v put
X^v_j := Phi^y_v Phi^y_j. The following are inconsistent:
  y_va = y_vb = 4,  X^v_a = X^v_b,  and both va, vb tight (so y'_va = y'_vb = 2).
```
C:92-93:
```text
**Corollary CI13'.** At an unmarked v in O, in either family y, if y_va = y_vb = 4 and tau_y(vab) = 4 y_ab, then at least
one of va,vb has (y,y') = (4,1). (In particular y_ab = 1 forces this, and so do y_ab = 2, tau = 8 and y_ab = 4, tau = 16.)
```
### M13-ov: `K/K62-M13-erratum-v1.md`; SHA256 `a4c476c10aede99ed77420413eec21549988c93926ce5d5fc081f4feefc346d9`
M13-ov:29-29:
```text
**Row consequences (opposite-family orientation explicit).** At every unmarked v in O, **both rows satisfy 5/6**:
```
M13-ov:52-53:
```text
At i*, both rows satisfy 11/12 by accepted (RC-i*), since f* = 1. These are only global, nonstrict bounds. No subset or atom
grid at an O-vertex or i* is obtained, and no additional universally strict slack is asserted.
```
### D: `K/K62-M13-D-v1.md`; SHA256 `d5fabd614afd1ef626d206df01f165db25883e54668c5ceab1e8ca69b7462194`
D:38-38:
```text
If all four O-entries at unmarked v belong to {1,2}, the row violates the conditional 5/6 bound.
```
D:46-46:
```text
If at unmarked v exactly one O-entry equals 4 and the other three belong to {1,2}, **z is even**.
```
D:83-91:
```text
For a family x let H_x be the graph on O of x-4-pairs. At every **unmarked** v:
- **(L1) 1 <= deg_(H_x)(v) <= 3.** A zero degree contradicts D4 in the x-row. Degree 4 makes all opposite entries <= 2,
  contradicting D4 in the x'-row.
- **(L2) Degree 1 forces x_(v i*) even.** This is D3 applied to the x-row.
- **(L3) Degree 3 forces the opposite degree 1 and x'_(v i*) even.** Three opposite entries are <= 2 (INV (b)). D4 forces
  its fourth O-entry to be 4, and D3 forces its i*-entry to be even. This is the local degree-3 rule with the orientation
  stated explicitly.
- **(L4) Any degree-0 or degree-4 vertex of either graph must be marked (t or p, if p lies in O).** In particular a
  bowtie's common vertex must be marked. This is only the contrapositive of L1, not a bowtie exclusion.
```
## 3. Source/authority table: exact paths, SHA256 and inclusive ranges
JSON `review-excerpts-M13-v2.json` has the absolute path and whole-file SHA for every entry; disjoint ranges repeat the
source. Root aliases below are EXACT absolute prefixes, not alternate copies:
- K = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon`
- S = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7`
- O = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7`
- R = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review`
- R16 = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review`

| ID | Path | Whole-file SHA256 | Selected lines | Scope / authority |
|---|---|---|---|---|
| A | `K/K62-M13-A-v1.md` | `77ce4077584582c699ce1bec870f2b19c55242bfc05aac99febcfbd69c466a8d` | 1-138 | NEW: whole candidate; rederive all claims. |
| B | `K/K62-M13-B-v1.md` | `455c58f9d35cc165f666eeaec9462e6b6ab6286196450532e619d6c0b9810058` | 1-83 | NEW: whole candidate; rederive all claims. |
| C | `K/K62-M13-C-v1.md` | `13f2c8dc42a95be24b819ec3cf68dbb178140bb2cd876b2c491d941d1e552e12` | 1-110 | NEW: whole candidate; rederive all claims. |
| D | `K/K62-M13-D-v1.md` | `d5fabd614afd1ef626d206df01f165db25883e54668c5ceab1e8ca69b7462194` | 1-101 | NEW: whole candidate; rederive all claims. |
| Scope | `K/K62-M13-SCOPE-v1.md` | `e5795694e99c0d0ae535bd0b8edf6d8d58d2fd17683f1abbaf3498ac5ce5d625` | 1-24 | Navigation only; erroneous timing wording superseded by Process. |
| Process | `K/checkpoint-017-v1.md` | `1a400c410ec472da7c6652bffc70fa027ab81cce5b337d06ec6ee97d6a66cb54` | 38-44 | Process correction: exploratory derivation preceded scope freeze; no preregistration. |
| V-written | `R16/sun-coset7-written-parent-verdict-v1.md` | `73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35` | 5-11,18,23,60 | ACCEPTED written reduction/rules, exact scopes; no finite coverage. |
| V-LFC | `R/sun7-lfc-inv-parent-verdict-v1.md` | `8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18` | 5-10,33 | ACCEPTED scoped LFC/INV/E1/E6. |
| V-E3 | `R/sun7-K62E3-parent-verdict-v1.md` | `576969ddb99fc2d0f5c6382f66428a7f4d7d3a1b59f681fc4d9d0f458fecbb0f` | 5-10,25 | ACCEPTED E3 Lemmas1-3, proof subclaims and C1/C2 at their orientations. |
| V-SHDG | `R/sun7-K62-SH-DG-parent-verdict-v1.md` | `cae455c3252b9066c261bcebb05ee4917b838bb5e2370101689c8297a017ddda` | 5,9-11,16-19,23 | ACCEPTED SH(ii), orientation-free DG1, DG3, scoped DG theorem. |
| README | `O/README.md` | `2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1` | 21-29,33-50,85-92 | V-written: product/Sun2/R0, P0/P1 and K6.2* class. |
| Rules | `O/rules-k7-v1.md` | `77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee` | 7-24,38-49 | V-written: L1 T1-T3, VFC V1-V4/count only. |
| LFC | `S/K7-LFC-INV-v1.md` | `45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c` | 18-34,54-64 | V-LFC: LFC a-d; INV a-b through E1-E4/E6-E7. |
| LFC-ov | `S/K7-LFC-INV-erratum-v1.md` | `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5` | 12-32,49-63 | V-LFC: E1 range, Sun2, <=6 pieces, labelled tuple, q=alpha*. |
| E3 | `K/K62-E3-v1.md` | `70a60d551583e8d6ad920acadb829d3ddf0d9c5c46ac988f8677645ee5457372` | 15-27,36-38,57-60,105 | V-E3: setting, Lemma1/2/3, original low-family counts/C2 swap. |
| E3-ov1 | `K/K62-E3-erratum-v1.md` | `095c31dcb9623cf3aa3887aef8d0a2d92708a0037b3bc3c7a8ad64b06ef3f797` | 11-13 | V-E3: F2 stands, F1/F3 superseded. |
| E3-ov2 | `K/K62-E3-erratum-v2.md` | `f9f52e1bc4896d94cd014ed3f8915af0318ddcd06d1efc1ad7f14478685add4c` | 82-88,211-218,255-260,278-283 | V-E3: gcd9; light fibres; Z10 d-grids; Z11(a) O ranges. |
| SH | `K/K62-SH-v1.md` | `4f17451c60c6018e7fadbca8c36eb92fb23d3e6daef076506aed14f4c5446b5a` | 17-19,25-27,37-43 | V-SHDG: SH(ii), no high-row entry1 away from t. |
| DG | `K/K62-DG-v1.md` | `a4bfc41e832ebc4e77770cab7a8092a3341827cec93a01bfb437c978c1e84f52` | 7-9,20-21,29-36,44-45,50-61 | V-SHDG: DG1/2/4 statements and theorem proof template; orientation retained. |
| DG-ov1 | `K/K62-DG-erratum-v1.md` | `e435430c6d4ff855871dfa7a9004757561435821dae8f53e7304b10e64626801` | 1-6 | V-SHDG mandatory overlay record; P_ob proof not imported. |
| SHDG-ov | `K/K62-SH-DG-erratum-v1.md` | `755edc21abdf7484f9187078d7e8cb6b4111f076906e7880085428d54f1b9d75` | 193-194,211-220,251-252,266-267,323-328 | V-SHDG: G2 no-orientation scope; G3 proof; G5/G6 New text; orientation note. |
| CAP | `K/K62-CAP-v1.md` | `19dccc3d8bce5908a14ff96462a05beeb38ba966374c8c4740e6a66a312b16d5` | 67-77 | V-CAP: C1 only at own entry1; C2 f*=1 both rows. |
| CAP-ov1 | `K/K62-CAP-DT-erratum-v1.md` | `996f924c731f0bfb1bf2a336d50d6ac0be50e55fb4ce134fa4b3cec2a1e2466d` | 104-114,131-139,155-158 | V-CAP: corrected C2; RC cases/VFC form through ov2, not general RC rule. |
| CAP-ov2 | `K/K62-CAP-DT-erratum-v2.md` | `5970c0d5faeaeea4bb712899b4a50cdcfd4e81a303a0a51abf37d5c03cc68676` | 115-120,133,146,160-162 | V-CAP: V4-V7 restrict rule imports and correct provenance. |
| M13-ov | `K/K62-M13-erratum-v1.md` | `a4c476c10aede99ed77420413eec21549988c93926ce5d5fc081f4feefc346d9` | 1-59 | NEW: one Old/New proof repair C58-63, no bound change. |
| V-CAP | `R/sun7-K62-CAP-DT-parent-verdict-v1.md` | `84061c6fbdbd9fa834810efa43843024e04c2abce794df28446865ef635234a0` | 1-43 | CORRECTNESS_ACCEPTED_SCOPED_PARTIAL; exact interfaces at lines23-27. |

All 24 source pins of v1 remain present and unchanged. A few redundant accepted proof passages are replaced by their
accepted interfaces to keep the full packet bounded; no new M13 proof is omitted. New sources are M13-ov and V-CAP.
Read overlay New blocks, not withdrawn Old blocks. R0 preserves conjugated intersections. No engine counts, probe,
P_ob theorem, K63/FG, atom/subset grids at O/i*, or G-only global graph conclusion is imported.

## 4. Dependency and scope checks
| New claim | Required interface / status |
|---|---|
| A (all) | Accepted LFC/INV/E3/DG1/elementary triangle interfaces only; DG2*/DG* are fresh proofs. C2* and budget do NOT need DG*'s four-subset hypothesis. |
| B1/B2 | Fresh feasible certificates; SH(ii) only for high-row c!=t in B2. |
| B3/B section4 | V-CAP RC-i* is within scope because f*=1. New B1/B3 still need independent proof. |
| C1w | Arithmetic implication with explicit witness, not old C1 in a failed orientation. |
| C2 | Uses new B1/B3 to supply a witness distinct from each fixed v. |
| C row consequence | M13-ov is a FRESH light-fibre proof; alpha-row uses new C2. Inversion gives alpha*-row with accepted CAP C1 on alpha (own entry1); this other row is within old RC-O too. |
| CI13/CI13' | Fresh replay with new granularity, not old CI at entry3; unmarked apex only. |
| C combined claims | Also require new A. DG in each family retains its own capped-four-subset hypothesis. |
| D | Uses repaired C row bounds, not G-only R3/R4 imported. All centres unmarked; marked neighbours allowed. |

## 5. Exhaustive location map: Sun and index/count steps
Every direct Sun(2)/(3) instance, including implicit positive-support feasibility, is below; Sun(4) is included too.
Allowed-set heredity is from LFC(c), not an exhaustive run. L0.1 is in README section0 (section1 is R0).

| Source lines | Step / literal hypotheses to verify |
|---|---|
| A18-30 | Normalize g_d=1; INV preserves indices/markers and swaps matrices; inverse conjugated family (U_j), d-subgroup U_d. |
| A42-43 | LFC a/b: n_d/2 O-incidences,3n_d/4 i*-incidences; exclusive U_d empty. |
| A44-48 | Label gcd3 except(t,i*) gcd9; Sun(4) forces that pair in any four-piece fibre; forbids five pieces/four O-pieces. |
| A49-56 | L0.1 measures and written avoidance; two right-U_d-invariant sets disjoint with measures summing1; no normality. |
| A57-67 | New boundary count: |A|=3n_d/4,|A_t|<=n_d/2; >=n_d/4+1 fibres have|B*|>=3. Deficiency sum n_d/2; >=n_d/4+3 four-piece fibres. |
| A70-72 | Orientation-free DG1 on inverted config, with T_alpha and positive grid; no failed entry1 hypothesis. |
| A73-84 | b_k double counts give DG2*: b3+2b4+3b5=n_d/2, b3+b4+b5>=n_d/4+1; preserve-1. |
| A85-97 | Fresh DG*: capped four-subsets<=4; multiples use actual n_d/16, including odd cofactor; G5/G6 arithmetic retained. |
| A98-104 | Pair grid r=1+v2(alpha)<=3<e_d; binomial count and3/2 bound; strict<19 and integer counts imply<=18. |
| A105-118 | Positive four/five-subset grids versus strict counts give depths>=3/4; add original alpha* C2 (needs alpha_di*=1) and new alpha C2*. |
| B18-27,32-48 | Positive coprime labels isolated by Sun2; gcd2 half-labels forbid triple by Sun3. Fifth4: one4-label; fifth3/5: delete sole possible marker partner. d weight0; values1 or(k+3)/6. |
| B53-59 | SH(ii) forces four c!=t entries2; drop t. d+four labels have gcd2; Sun3 halves value25/24. |
| B64-71 | Low-row d has no3; Sun2 isolates1-labels, Sun3 bounds O-2+d halves;23/24>RC-i*11/12 at f*=1. |
| B74-77 | Two alpha entries>=3 imply two opposite<=3 (INV); after deleting any v a witness remains. |
| C29-50 | d,t exact k1; p then remainingO gcd6,k<=3; i* LAST gcd12,k<=2alpha*_(i*c0)<=6. All 2/3/5/w, absent/coincident/outsideO markers included. |
| C53-56 | Witness uses new B1/B3; C1w proves exact gcd6 for high family at unmarkedv. |
| M13-ov30-44 | NEW alpha-row proof: normalize g_v=1, W'=intersection U*_j, gcd(n_v,T)=6. W'U_v misses all L_j by explicit contradiction. M=[W':W'capU_v]>=n_v/6 (Lagrange). LFC a-c summation<=n_v-M yields nonstrict5/6. |
| M13-ov45-53 | Invert: subgroups U*_j, conjugates U_j, normalisation preserves T_alpha; CAP C1 on alpha entry1 gives q0|6, empty count>=n_v/q0>=n_v/6. Otherrow5/6; both i*-rows11/12 only at f*=1. |
| C72-76 | VFC light set lies in every X_j; L0.1/Lagrange measure>=1/6; opposite union<=5/6. Local labels opposite-family. |
| C77-84 | Tight equal complements; triples{a,b,j}, j=d or anotherO, have pairwise gcd<=2; Sun3 gives disjointness. i* is excluded. |
| C85-88 | Saturation1/3+1/2=5/6 forces containment. Sun2 forces even opposite entry; measure<=1/2 excludes4, leaves2. |
| C89-97 | Sun3 on{c,c',d} gives disjoint1/3 sets inside1/2. Apex equality L1(T3)+INV, then CI13 and INV/O range give(4,1). |
| D19-35 | Unmarked centre f*=1; odd-sharing neighbour only t for z3,p for z5,none for z1; p=t/outsideO covered. |
| D40-43 | R4: i*0; Sun2 isolates positive1 labels; Sun3 bounds O-2+d halves;11/2. |
| D52-55 | z1: Sun2 isolates1; half-pairs gcd2, Sun3;11/2. |
| D57-60 | z3,t-entry1/2: delete t; same Sun2/Sun3 support;11/2. |
| D62-69 | z3,t-entry4: delete t,half i* and d; no common3/5; Sun2/Sun3; value6. |
| D71-80 | z5,p outsideO: d0 avoids shared5,value15/2; p inO: deletep (includingp=t), Sun2/Sun3,value13/2 or11/2. |
| D83-96 | Degree1..3 and parity at UNMARKED centres only; degree3 forces opposite-degree1/opposite-entry even. Marked fifth vertex escapes G proof; no global K4/bowtie/diamond/free-family conclusion. |

## 6. Review contract and boundaries
Independently check every A-D claim, the high/low-family inversion, all positive supports, marker endpoints, actual-versus-
capped depths, and every conditional edge. Do not accept a co-packaged NEW lemma before deriving it. Accept prior imports
only at the table's literal scopes; retained accepted statements do not strengthen merely because a proof looks similar.

Return FATAL/MAJOR/MINOR counts for A1,DG1*/DG2*/DG*,C1*/C2*/budget,B1/B2/B3,C1w/C2/repaired rows,CI13/CI13',D4/D3,L1-L4,
with exact file:line, minimal repair and scope. Audit fresh M13-ov as part of the WHOLE candidate, not only the cited fix.
An empty findings list is valid. Do not infer full regime closure. No science computation or model call is requested from
this worker. Every marked centre and the higher-depth alternative remain OPEN. No novelty, Lean or human-referee claim.

## 7. Exact excerpt format and size
JSON is the Olson BASE2 ordered array of absolute path, whole-source sha256, one-based inclusive start/end. Candidate
A-D and M13-ov are whole-file; selected accepted imports supply literal interfaces. Embed raw bytes, not rendered tools.

Packaging metadata: 26 sources, 60 inclusive-range excerpts, selected raw UTF-8 83980 bytes;
JSON 15297 bytes; package 20009 bytes; combined 119286 bytes (<120000).
All whole-source hashes/ranges and verbatim quote ranges checked. Byte/hash operations are packaging, not science runs.
