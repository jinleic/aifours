# M13 written review package v1: orientation (1,3)/(3,1), Parts A-D

Owner Sun63Successor. Written after `/bin/date` 2026-10-19T08:33:20-0700. **CANDIDATE_UNVERIFIED**, written mathematics only.
No review or computation is launched by this worker. The four candidates are unchanged. Review every new claim rather
than accepting one co-packaged candidate as an import. No (1,3)/(3,1), full K6.2*, K7 or Sun(7) exclusion is claimed.

## 1. Frozen setting, candidates and verbatim statements
K6.2*, e_d>=4, e*=2, V={d,i*} disjoint-union O, |O|=5. Work in (alpha_di*,alpha*_di*)=(1,3); INV transfers (3,1) by swapping
families. The class forces t in O and f*=1. The 5-marker may be anywhere admissible. At most one O-vertex has f>=2 and at
most one vertex has h>=1; the w's are pairwise coprime and prime to30. Each quote below is VERBATIM at the stated source
lines; the JSON also selects the ENTIRE A-D files, with every proof and scope restriction.
### Part A
`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-M13-A-v1.md`; SHA256 `77ce4077584582c699ce1bec870f2b19c55242bfc05aac99febcfbd69c466a8d`; whole file lines 1-138.
Lines 33-39:
```text
- **(a) Counts.** P*_c meets exactly n_d/2 fibres (c in O); P*_(i*) meets exactly 3 n_d / 4 fibres; none of them is U_d.
- **(b) Size.** |S*_F cap O| <= 3 for every F. Moreover |S*_F| <= 4, and |S*_F| = 4 only if {t, i*} is contained in
  S*_F.
- **(c) Complements.** For c in O: c is not in S*_F iff F lies in U_cU_d, a union of n_d/2 fibres. Likewise i* is not
  in S*_F iff F lies in U_(i*)U_d, a union of n_d/4 fibres.
- **(d) Counting facts.** sum over F of (|B*(F)| - 2) = n_d/2, every term is >= 0, and #{F : |B*(F)| >= 3} >= n_d/4 + 1.
- **(e) Four-piece fibres.** At least n_d/4 + 3 fibres have |S*_F| = 4; each of them contains t and i*.
```
Lines 70-70:
```text
- **(DG-1\*)** For non-empty Q contained in O, N*(Q) is a positive multiple of n_d / 2^(min(e_d, v2 T_alpha(Q))).
```
Lines 73-77:
```text
- **(DG-2\*)** Put A*_4 := #{F : |B*(F)| >= 4}. Then:
  - (i) N*(O) + A*_4 <= n_d/4 - 1;
  - (ii) the sum over 3-subsets R of O of N*(R) is <= n_d - 2 + 3 N*(O);
  - (iii) the sum over 4-subsets Q of O of N*(Q) is <= n_d/4 - 1 + 3 N*(O);
  - in particular N*(O) <= n_d/8 - 1/2.
```
Lines 85-90:
```text
- **(Theorem DG\*)** In (1,3), for the alpha-family, write r_S := min(e_d, v2 T_alpha(S)).
  - **(a)** If r_Q <= 4 for all five 4-subsets Q of O, then N*(O) <= n_d/16 and **the sum over the ten 3-subsets R of O of
    2^(-r_R) is <= 19/16 - 2/n_d**.
  - **(b)** Under the hypothesis of (a), at least two 3-subsets R have r_R >= 4, or exactly one does and it has r_R = 5.
    In the second case its alpha-values are (4,4,4), tau_alpha(R) = 16 and e_d >= 5. By DG-3 (G3 form, applied to
    Gamma*), every R with r_R >= 4 has alpha-values (2,4,4) or (4,4,4) and tau_alpha(R) in {8, 16}.
```
Lines 98-98:
```text
- **(C2\*)** In (1,3), write n_k(alpha) := #{O-pairs with alpha = k}. Then **n_4(alpha) >= 2 n_1(alpha) + 2**.
```
Lines 105-105:
```text
- **(C1\*)** In (1,3): v2 T_alpha(Q) >= 3 for every 4-subset Q of O, and v2 T_alpha(O) >= 4.
```
Lines 110-112:
```text
Write N_ab for the number of O-pairs with joint value (alpha, alpha*) = (a, b), for (a, b) in
J_O = {(4,1), (4,2), (1,4), (2,4), (1,1), (1,2), (2,1), (2,2)} (K62-E3 Lemma 2, Z11 (a), INV (b)). In (1,3):
  **2 N41 + 2 N14 + 5 N11 + 3 N12 + 3 N21 + N22 <= 6.**
```
### Part B
`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-M13-B-v1.md`; SHA256 `455c58f9d35cc165f666eeaec9462e6b6ab6286196450532e619d6c0b9810058`; whole file lines 1-83.
Lines 30-30:
```text
**For either family x in the setting above, |K_x| != 4.**
```
Lines 51-51:
```text
**In (1,3), |K_alpha*| != 5, hence |K_alpha*| <= 3 by B1.**
```
Lines 61-62:
```text
## 3. Lemma B3 (the low distinguished-entry family has a gap) [CONDITIONAL ON CAP/DT VERDICT]
**In (1,3), |K_alpha| != 5, hence |K_alpha| <= 3 by B1.**
```
Lines 74-77:
```text
In (1,3), **|K_alpha| <= 3 and |K_alpha*| <= 3**. Consequently each i*-row has at least two O-entries >= 3. In particular,
- there are at least two vertices c in O with alpha_(i* c) >= 3, and for each such c, alpha*_(i* c) <= 3 (INV (b));
- for every v in O there is c_0 in O minus {v} with **alpha*_(i* c_0) <= 3**.
The analogous statement in (3,1) follows after exchanging alpha and alpha*.
```
### Part C
`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-M13-C-v1.md`; SHA256 `13f2c8dc42a95be24b819ec3cf68dbb178140bb2cd876b2c491d941d1e552e12`; whole file lines 1-110.
Lines 23-27:
```text
Let v be an unmarked O-vertex. **If there is c_0 in O minus {v} with alpha*_(i* c_0) <= 3**, then
  **gcd(n_v, T_alpha*(V minus {v})) = 6.**
This is a candidate implication proved from accepted arithmetic imports; existence of the witness for every v is
obtained in C2, conditionally on M13-B B3.
```
Lines 53-54:
```text
In (1,3), **C1w's hypothesis holds at every unmarked v in O**, hence gcd(n_v, T_alpha*(V minus {v})) = 6 at every such v.
```
Lines 58-63:
```text
**Row consequences (opposite-family orientation explicit).** At every unmarked v in O, **both rows satisfy 5/6**:
- the alpha-row: Lemma RC with the alpha*-family granularity supplied by C2;
- the alpha*-row: Lemma RC with CAP (C1) for the alpha-family, whose distinguished entry alpha_(d i*) = 1 meets its
  hypothesis.
At i*, both rows satisfy 11/12 by (RC-i*), since f* = 1. These are only global, nonstrict bounds. No subset or atom grid
at an O-vertex or i* is obtained.
```
Lines 66-70:
```text
Let y be either family, y' its opposite, v in O unmarked and a != b in O minus {v}. In the Phi^y-configuration at v put
X^v_j := Phi^y_v Phi^y_j. The following are inconsistent:
  y_va = y_vb = 4,  X^v_a = X^v_b,  and both va, vb tight (so y'_va = y'_vb = 2).
**This includes y = alpha*, whose distinguished entry is 3.** It does not apply the original CI statement outside its
x_(d i*) = 1 scope; it replays that proof using the new granularity in C2 instead of the original chain hypothesis.
```
Lines 92-93:
```text
**Corollary CI13'.** At an unmarked v in O, in either family y, if y_va = y_vb = 4 and tau_y(vab) = 4 y_ab, then at least
one of va,vb has (y,y') = (4,1). (In particular y_ab = 1 forces this, and so do y_ab = 2, tau = 8 and y_ab = 4, tau = 16.)
```
### Part D
`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-M13-D-v1.md`; SHA256 `d5fabd614afd1ef626d206df01f165db25883e54668c5ceab1e8ca69b7462194`; whole file lines 1-101.
Lines 38-38:
```text
If all four O-entries at unmarked v belong to {1,2}, the row violates the conditional 5/6 bound.
```
Lines 46-46:
```text
If at unmarked v exactly one O-entry equals 4 and the other three belong to {1,2}, **z is even**.
```
Lines 83-91:
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
## 2. Process scope and conditional edges
- Scope: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-M13-SCOPE-v1.md`, SHA256 `e5795694e99c0d0ae535bd0b8edf6d8d58d2fd17683f1abbaf3498ac5ce5d625`, lines 1-24.
- Process: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/checkpoint-017-v1.md`, SHA256 `1a400c410ec472da7c6652bffc70fa027ab81cce5b337d06ec6ee97d6a66cb54`, lines 38-44.
The Process excerpt supersedes scope's claim "before any derivation": exploratory hand reasoning preceded the scope
freeze, although the scope preceded A-D file writes. No preregistration claim. Scope's "C1 fails" means its hypothesis
was unmet, not that a counterexample was proved.

| Candidate steps | Conditional status / exact dependency |
|---|---|
| A, all; B1/B2 | New unreviewed claims using accepted interfaces only. A's DG2*/DG* are FRESH proofs; the old theorem is not applied with a failed orientation hypothesis. |
| B3 and B section4 | CONDITIONAL ON CAP/DT VERDICT: RC-i* at f*=1. B1/B3 imply two large alpha i*-entries and hence a small alpha* witness distinct from any fixed v. |
| C1w | Arithmetic implication given the explicit small-entry witness; accepted elementary imports only. |
| C2 / row consequences / CI13 / CI13' | CONDITIONAL ON CAP/DT and the new B proof. Low-family C1 is used at entry1 only. For the high-family row, freshly rederive the light-fibre calculation with C1w; do NOT import old RC-O outside its distinguished-entry1 scope. |
| D, all | CONDITIONAL ON C's two row bounds (hence CAP/DT and B/C). R3/R4 certificates are new, not imports of G-only DT-B. |
| C section4 combined claims | Also require new A, not just CAP/DT acceptance. |

CAP/DT was still awaiting a parent verdict when this package was prepared. Its repaired proof context is supplied below;
minor-only reviewer recommendations are NOT parent acceptance. V2 limits black-box RC rule imports to RC-O/RC-i*: this
review must establish any M13 extension from the supplied light-fibre proof, not assume a stronger accepted interface.

## 3. Import and authority table
Whole-file hashes bind the sources, not just excerpts. Line ranges are one-based INCLUSIVE and match the JSON. Authority
IDs name the complete path/hash/range row of that verdict. Old and New text, when both occur in an overlay, are distinct;
only governing New text is operative. Accepted proof bodies need not be re-audited beyond checking literal interfaces.

| ID | Source path; whole-file SHA256 | Lines | Authority / scope used |
|---|---|---|---|
| V-written | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-written-parent-verdict-v1.md`; `73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35` | 5-11,18,21-23,60 | CORRECTNESS-ACCEPTED: Accepted README R0/P0/P1/class; T/VFC at literal scopes, mandatory overlay. |
| V-LFC | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-lfc-inv-parent-verdict-v1.md`; `8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18` | 5-10,33 | CORRECTNESS-ACCEPTED SCOPED PARTIAL: Accepted LFC/INV/E1/E6; Sun(5)/(6) provenance retained. |
| V-E3 | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62E3-parent-verdict-v1.md`; `576969ddb99fc2d0f5c6382f66428a7f4d7d3a1b59f681fc4d9d0f458fecbb0f` | 5-10,25,31 | CORRECTNESS_ACCEPTED_SCOPED_PARTIAL: Accepted K62-E3 statements/proof subclaims; C2 swap only with opposite entry1. |
| V-SHDG | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-SH-DG-parent-verdict-v1.md`; `cae455c3252b9066c261bcebb05ee4917b838bb5e2370101689c8297a017ddda` | 5,9-11,16-19,21-23,36 | CORRECTNESS_ACCEPTED_SCOPED_PARTIAL: Accepted SH(ii), DG1 without orientation; DG theorem has orientation/four-subset hypotheses. |
| README | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/README.md`; `2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1` | 21-29,33-50,85-92 | V-written: Product formula, Sun2, R0, prime-incidence data and K6.2* definition. |
| Rules | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/rules-k7-v1.md`; `77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee` | 7-24,38-49 | V-written: L1 T1-T3; VFC V1-V4/count. No FH/RPLP import. |
| LFC | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-LFC-INV-v1.md`; `45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c` | 18-74 | V-LFC: LFC a-d; INV a-b through E1-E4/E6-E7. |
| LFC-overlay | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-LFC-INV-erratum-v1.md`; `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5` | 12-32,49-63 | V-LFC: E1 range/product; Sun2; <=6 pieces; labelled tuple; q=alpha*. |
| E3 | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-E3-v1.md`; `70a60d551583e8d6ad920acadb829d3ddf0d9c5c46ac988f8677645ee5457372` | 15-38,57-60,76-79,105 | V-E3: Class, Lemma1/2/3 statements, low-family count and C2 swap condition. |
| E3-overlay1 | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-E3-erratum-v1.md`; `095c31dcb9623cf3aa3887aef8d0a2d92708a0037b3bc3c7a8ad64b06ef3f797` | 11-13 | V-E3: F2 only; other items superseded. |
| E3-overlay2 | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-E3-erratum-v2.md`; `f9f52e1bc4896d94cd014ed3f8915af0318ddcd06d1efc1ad7f14478685add4c` | 82-88,211-218,255-260,278-283 | V-E3: Z2 gcd9; Z8 light fibres; Z10 grids; Z11(a) O ranges. |
| SH | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-SH-v1.md`; `4f17451c60c6018e7fadbca8c36eb92fb23d3e6daef076506aed14f4c5446b5a` | 17-43 | V-SHDG: SH(ii) excluding high-row entry1 away from t; SH1/2 context. |
| DG | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-DG-v1.md`; `a4bfc41e832ebc4e77770cab7a8092a3341827cec93a01bfb437c978c1e84f52` | 7-9,20-21,29-36,44-45,50-61 | V-SHDG: DG1/2/4 statements, exact DG theorem and proof template. |
| DG-overlay1 | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-DG-erratum-v1.md`; `e435430c6d4ff855871dfa7a9004757561435821dae8f53e7304b10e64626801` | 1-6 | V-SHDG: Mandatory governing record; P_ob proof unused. |
| SHDG-overlay | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-SH-DG-erratum-v1.md`; `755edc21abdf7484f9187078d7e8cb6b4111f076906e7880085428d54f1b9d75` | 74-79,183-194,211-220,235-237,251-252,266-267,323-328 | V-SHDG: S2; G2-G6 New text and orientation note. |
| CAP | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-CAP-v1.md`; `19dccc3d8bce5908a14ff96462a05beeb38ba966374c8c4740e6a66a312b16d5` | 67-77 | PENDING CAP/DT: CONDITIONAL C1/C2 only at frozen hypotheses. |
| CAP-overlay1 | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-CAP-DT-erratum-v1.md`; `996f924c731f0bfb1bf2a336d50d6ac0be50e55fb4ce134fa4b3cec2a1e2466d` | 104-114,131-158 | PENDING CAP/DT: CONDITIONAL CD2 C2 proof; CD3 RC proof/cases, through v2. |
| CAP-overlay2 | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-CAP-DT-erratum-v2.md`; `5970c0d5faeaeea4bb712899b4a50cdcfd4e81a303a0a51abf37d5c03cc68676` | 115-120,133,146,160-162 | PENDING CAP/DT: CONDITIONAL V4-V7 rule-scope restriction and RC provenance. |

No P_ob result, prior engine record, K63 proof, FG shim, graph closure from G, subset/atom grid at O/i*, or scientific
computation is an import. The DG-overlay1 body concerns P_ob and is not needed here. For DG3 in A, check the elementary
L0.1/Lagrange derivation on Gamma* (or L1+INV), not an unpreserved scope assumption. In A/B/C "accepted imports only" never
means the NEW conclusions are accepted. Lagrange and finite subgroup cardinalities are elementary, stated index steps.

## 4. Complete map of Sun and index/count steps in the NEW proofs
The references below are to the frozen A-D source lines. Every Sun(2)/(3) invocation, including feasibility arguments
where the name is implicit, is included. General allowed-set heredity is the definition in LFC(c), not a computational
premise. Sun(4) is listed too; Sun(5)/(6) remain computer-assisted imports through LFC/VFC and class reduction.

| Source lines | Step and literal hypothesis to check |
|---|---|
| A18-30 | Normalize g_d=1; invert cosets, preserve labelled indices/markers and swap matrices; inverted conjugated family is (U_j), d-subgroup U_d. |
| A42-43 | LFC a/b gives n_d/2 O-incidences and 3n_d/4 i*-incidences, none at exclusive U_d. |
| A44-48 | Labels have gcd3 except (t,i*) gcd9. Sun(4): every four-piece set contains both, forbidding five pieces and four O-pieces. |
| A49-56 | L0.1 product measures and explicit disjointness; measures add to1, giving fibre complements. No normality assumption. |
| A57-67 | New counts: |A|=3n_d/4, |A_t|<=n_d/2; at least n_d/4+1 fibres have |B*|>=3. Sum deficiencies n_d/2 and four-piece count >=n_d/4+3. |
| A70-72 | Accepted DG1 applied to Gamma*: its conjugated index is T_alpha(Q); positivity and grid do not require entry1. |
| A73-84 | Fresh DG2* count in b_k; verify each pair/triple/four-subset double count and the -1 term. |
| A85-97 | Fresh DG*: capped-four-subset hypothesis explicit; round multiples of n_d/16, not a capped substitute for n_d; G5/G6 arithmetic retained. |
| A98-104 | Pair grid r=1+v2(alpha)<=3<e_d; binomial double count and 3/2 bound; strict <19 plus integer counts gives <=18. |
| A105-107 | Four/five-subset positive grids versus strict count bounds give depths>=3/4. |
| A110-118 | Original alpha* C2 needs alpha_di*=1; new C2* supplies alpha; add them using ten joint pairs. No G-only import. |
| B18-27,32-48 | Labels b_c pairwise coprime/odd. Sun(2) isolates positive coprime labels; Sun(3) excludes three gcd2 half-labels. Fifth entry4: one 4-label. Entry3/5: delete its only possible marker partner. Zero-weight d irrelevant by heredity. |
| B53-59 | SH(ii) applies to c!=t in high row; drop t. The four remaining labels and d have pairwise gcd2; Sun(3) validates halves; value25/24. |
| B64-71 | Low row has no3 in d-label. Sun(2) isolates 1-labels; Sun(3) bounds O-2 labels plus d. Value23/24 contradicts RC-i*11/12 (f*=1). |
| B74-77 | At least two alpha entries>=3; INV gives two opposite entries<=3, so one remains after deleting v. |
| C29-50 | New chain: d,t exact k=1; later O steps gcd6,k<=3; i* LAST has gcd12 and k<=2 alpha*_(i*c0)<=6. Check every 2/3/5/w case including absent/coincident/outside-O 5-marker. |
| C53-63 | Witness existence uses B3. Alpha-row requires a fresh opposite-family light-fibre argument with new gcd6; alpha*-row uses old low-family C1 at entry1. RC-i* uses f*=1. No atom grid. |
| C72-76 | Light set lies in all X_j, mu>=1/6 by L0.1/Lagrange; union D'_j<=5/6, nonstrict. Local indices belong to opposite family. |
| C77-84 | Equal tight complements; every possible triple {a,b,j} has pairwise gcd<=2. Sun(3) forces D disjoint from D'_j. i* is not among these triples. |
| C85-86 | Saturation of 1/3+1/2=5/6 forces remaining O-sets inside D'_d; no unwarranted strict slack. |
| C87-88 | Sun(2) forces gcd>=2, hence even opposite entry; measure<=1/2 excludes4, leaving2. Odd parts cannot be shared. |
| C89-90 | Sun(3) on {c,c',d} gives disjoint 1/3 sets inside1/2, contradiction. |
| C92-97 | Apex measure equality from L1(T3)+INV (or elementary G3), then CI13. INV/O range converts non-tight into opposite entry1. |
| D19-35 | At unmarked centre f*=1: only odd-sharing neighbour is t for z3, p for z5, none for z1. p=t and p outside O included. |
| D40-43 | R4: i* weight0. Sun(2) isolates positive1 labels; Sun(3) allows at most two positive halves (O-2 and d); value11/2. |
| D52-55 | z1: positive1 labels isolated (Sun2), half-label pairs gcd2 (Sun3); value11/2. |
| D57-60 | z3,t-entry1/2: delete t, same Sun2/Sun3 support; value11/2. |
| D62-69 | z3,t-entry4: delete t, put halves on both i*,d; after deletion they and O-2 have gcd2, 1-labels isolated; Sun2/Sun3, value6. |
| D71-74 | z5,p outside O: original support; y_d=0 avoids the shared5 with d; Sun2/Sun3, value15/2. |
| D76-80 | z5,p in O: delete p (including p=t), eliminating common5; Sun2/Sun3, value13/2 or11/2. |
| D83-96 | Degree1..3 and parity only at UNMARKED centres. Degree3 forces opposite degree1/opposite i*-entry even. Marked centres/fifth vertices escape; no no-K4/no-bowtie/free-family closure. |

## 5. Reviewer focus and requested response
Audit every claim and conditional edge with exact source scope, especially: the inverse four-piece exception in A; the
boundary-fibre count that replaces the old three-piece premise; B1's exceptional odd-marker deletion; C's general-RC
proof application versus the now-restricted imported cases; all C1w multiplier/prime factors; and D's modified positive
supports. Do not treat a co-packaged new lemma as proven until re-derived.

Return a verdict with FATAL/MAJOR/MINOR counts for A1, DG1*/DG2*/DG*, C1*/C2*/budget, B1/B2/B3, C1w/C2/row consequences,
CI13/CI13', D4/D3 and local L1-L4. Cite exact file:line, minimal repair and precise conditional/import scope. Flag any
unjustified promotion from low to high family, raw to capped depth, or unmarked to marked centre. An empty findings list
is acceptable. No need or authorization to launch science computation. Full (1,3)/(3,1), K6.2* and Sun(7) stay OPEN.

## 6. Excerpt manifest and size
`review-excerpts-M13-v1.json` is a plain ordered array of {{path, sha256, start, end}} exactly as in the Olson BASE2 format.
Whole-file SHA256, absolute path, one-based inclusive ranges; repeat a source for disjoint excerpts. Embed RAW selected
UTF-8 lines, not rendered read-tool output. Candidate A-D are included whole. Accepted formal interfaces and governing
corrections are supplied; omitted accepted proof bodies are not new M13 premises.

Measured packaging metadata: 24 whole source files, 58 excerpts, 81938 selected raw UTF-8 bytes;
JSON 14782 bytes; this package 22704 bytes; combined raw excerpts + JSON + package 119424 bytes (<120000).
No mathematical computation was performed. Parent owns review launches and the eventual verdict.
