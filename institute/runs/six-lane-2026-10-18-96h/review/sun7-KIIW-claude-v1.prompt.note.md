# KII-W-v1: independent hostile written review

**Result: FATAL 0 · MAJOR 0 · MINOR 5.** Theorem KII-W (`KII-W-v1.md:162-170`) checks out as stated. SHAPE must be read relative to a configuration (MINOR-1).

- Every step below was re-derived by hand.
- I used no tools, computation, edits or delegation.
- Hashes, timestamps and prior verdict labels were not used as evidence.

Line references are to `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/kii-written/KII-W-v1.md` unless prefixed.

## 1. Claim-by-claim verdict

| Claim | Lines | Verdict |
|---|---|---|
| SHAPE (⇒) | 43-52 | Correct. Uses Sun(2) on the actual cosets. |
| SHAPE (⇐) | 52-53 | Correct when read relative to a configuration. MINOR-1. |
| Markers i*, t; min(a_x, v₂ r_i*) ≤ 1 | 55-57 | Correct |
| R0 | 60-62 | Correct |
| MU and the KII multiplier ranges | 64-68 | Correct (overlay E1) |
| INV, (I1), (I2) | 70-76 | Correct. No VFC needed (E7). Same tuple gives same markers (E6). |
| FC23, including the in-file Sun(2) | 78-91 | Correct. Uses only 2- and 3-subsets. Own fibre excluded (E3). |
| Choice of c, plainness | 94-97 | Correct in all 7 t/i* placements |
| Labels and masses in both families | 98-102 | Correct |
| GCD table | 103-111 | Correct and exact (no capping) |
| K1–K6 | 113-120 | Correct |
| Lemma B | 123-125 | Correct |
| Lemma A | 126-129 | Correct |
| Lemma Z | 130-131 | Correct. MINOR-3 (wording). |
| Main Lemma, M1–M4d | 134-159 | Correct. MINOR-5 (presentation). |
| Theorem KII-W | 162-170 | Correct. MINOR-3 (wording). |
| DAG and Sun boundary | 173-185 | Accurate |

## 2. Requested audits

### 2.1 SHAPE, both directions, and the shared factor 2

**(⇒)**
- Every pairwise gcd lies in [2,6]: ≤ 6 because the configuration is a CE, ≥ 2 by Sun(2).
- Take j ∉ A₅. Then gcd(n_x, n_j) is prime to 5 and has no prime ≥ 7, so x ∈ A₂ ∪ A₃. The same holds for y.
- gcd(n_x, n_y) is a multiple of 5 and ≤ 6, so it equals 5. Hence x and y share neither 2 nor 3.
  - This also rules out x ∈ A₂∩A₃, which would force gcd(n_x, n_y) ≥ 10.
  - So after naming, x ∈ A₂∖A₃ and y ∈ A₃∖A₂.
- Take j ∈ C.
  - gcd(n_x, n_j) is prime to 3 and to 5, so 2 | n_j.
  - gcd(n_y, n_j) is odd and prime to 5, so it equals 3, and 3 | n_j.
  - Hence C = A₂∩A₃.
- The four gcd identities need only (S1). For example, gcd(10r_x, 15r_y) = 5·gcd(2r_x, 3r_y) = 5·gcd(r_x, r_y), because 2 ∤ 3r_y and 3 ∤ r_x. The other three identities follow the same way.
- The bound ≤ 6 then gives (S2) and (S3). For gcd(r_y, r_c) ≤ 2 ⇒ 1, the proof silently uses that r_y is odd (`:51`).

**(⇐)** The identities give gcds 5, 2·{1,2}, 3 and 6. Also 5 ∤ 6r_c, so A₅ = {x, y}. Therefore any configuration with this tuple is a CE with a = 2.

**Shared factor 2.**
- gcd(n_x, n_c) = 4 iff both r_x and r_c are even.
- By (S2) that can only happen for c = i*, and (S3) caps the gcd at 4. This is exactly README:96 (using e_c ≥ 2 ⇔ 2 | r_c).
- The cap is load-bearing in exactly one place: K6's gcd(X, I) ≤ 2 for γ ∈ {1, 3}, used by M4b and M4c. Without it, {x, i*, p₂} would be admissible there with weight 3/2.

### 2.2 R0, MU and INV

- **R0.**
  - Each core is the kernel of the action on G/U_j, so it has finite index, and N ≤ U_j.
  - Each g_jU_j is a full preimage of its image in G/N. So all n_j, all [G : U_i∩U_j] and disjointness pass to G/N.
  - INV is used only after R0, so no lifting question arises.
- **MU.**
  - Lagrange gives lcm | I.
  - L0.1 gives |U_iU_j|/|G| = α/g.
  - L0.2 plus disjointness gives U_iU_j ≠ G, so α ≤ g − 1.
- **INV.**
  - (g_jU_j)⁻¹ = g_j⁻¹ · g_jU_jg_j⁻¹.
  - Conjugating by g_i⁻¹ sends U_i*∩U_j* to U_i∩hU_jh⁻¹.
  - Since h ∉ U_iU_j, the double cosets U_iU_j and U_ihU_j are distinct, hence disjoint. This gives α + α* ≤ g.
  - (I1): α_yc and α*_yc are both ≥ 1 and sum to ≤ 3, so one of them equals 1.
  - The inverse is again KII with the same x, y, C, i*, t, because every marker is index-defined.

### 2.3 FC23 over every actual fibre set

- The index chains are correct: λ_j = n_jα/g and t_j = n_vα/g.
- g_jU_j meets exactly t_j fibres and never g_vU_v.
- Inside a fibre, the pieces b⁻¹p_j(U_j∩U_v) are pairwise disjoint left cosets in U_v with indices λ_j.
- In-file Sun(2) (`:86-88`): coprime λ, λ′ ⇒ λλ′ | [U_v : H∩K] ⇒ HK = U_v. This is correct.
- Zhu's Sun(3) applies to any 3 of the pieces.
- Every actual S_B, of any size up to 6, therefore satisfies the 2- and 3-subset conditions. FC23 only requires the weights to respect this larger family of sets, so no Sun(t) with t ≥ 4 enters.
- The double count over the n_v − 1 fibres is correct.
- **The strict gap 1/n_v is load-bearing.** These cases reach exactly 1:
  - B with e = 1;
  - A;
  - M1 with n₁ = 0;
  - M2 and M3;
  - M4a with γ = 2;
  - M4b and M4c.

### 2.4 Apex c in every placement, and x in both families

| Placement | c | C-neighbours of c |
|---|---|---|
| i* absent; t absent or t = y | any C-vertex | 4 plain |
| i* absent; t ∈ C | t | 4 plain |
| i* present; t absent or t = y | any vertex of C∖{i*} | i* and 3 plain (t = y gives v₃ r_i* = 0) |
| i* present; t ∈ C∖{i*} | t | i* and 3 plain |
| i* present; t = i* | any vertex of C∖{i*} | i* with v₃ ≥ 1, and 3 plain (v₃ Y = 0) |

- t = x is impossible because 3 ∤ r_x.
- In every row, a plain p is neither t nor i*, so r_p is prime to 30.
- When c = t, the factor 3 | r_c does not appear in any label at apex c, since the labels use n_j for j ≠ c.
- c ≠ i* means r_c is odd, so g_xc = 2. By MU applied separately to α and to α* (both are actual configurations), Φ_xc = 1 in both families. Hence X = 5r_x and μ_x = ½ in both.

### 2.5 GCD table and K1–K6

- The prime-to-30 parts of X, Y, I and P divide r_x, r_y, r_i* and r_p. This holds because φ, γ, π ≤ 5 are 30-smooth.
- By (S2) and (S3), those r values pairwise share no odd prime, which gives the formula at `:103`.
- I re-derived all twelve table entries.
- I checked K1–K6, including K4 for each value of t ∈ {y, i*, c, absent}.
- K6 correctly omits gcd(X, I) for γ ∈ {2, 4}, where it can be 4 or 8 (for example a_x ≥ 2, v₂ r_i* = 1, γ = 4). The only case with γ ∈ {2, 4} and a positive weight on i* is M4a, and M4a sets w_x = 0.

### 2.6 Weight feasibility against all admissible sets, zero-weight items included

| Case | Positive weights | Bound for every admissible S | Objective |
|---|---|---|---|
| B | p: 1, q: 1 | gcd(P, Q) = 1 (K3), so p and q never occur together | (5+e)/6 ≥ 1 |
| A, π = 3 | x: 1, p: 1 | gcd(X, P) = 1 (K1) | ½ + ½ |
| A, three 1s | x: 1; pᵢ: 1 | each pᵢ is a singleton (K2) | ½ + 3/6 |
| M1 | y: 1; each 4: 1/n₄; each 1: 1 | S with y lies in {x, y, i*}, where x and i* weigh 0. Otherwise the positive part is a subset of the 4s. | ≥ ⅓ + ⅔ |
| M2 | y: 1; 2s: ½; 1s: 1 | S with y lies in {x, y}. Otherwise S has at most two 2s (pairwise gcd 2, Sun(3)). | ⅓ + 4/6 |
| M3 | y: 1; the 2: 1; 1s: 1 | S with y lies in {x, y, i*}. Otherwise S has at most one positive item. | ⅓ + ⅓ + ⅓ |
| M4a | y: 1; i*: ½; 2s: ½; 1: 1 | gcd(Y, I) = 1. S has at most two of {i*} ∪ 2s. **w_x = 0 is needed** because {x, i*, p₂} can be admissible. | 5/6 + γ/12 ≥ 1 |
| M4b | x, y, i*: ½; 2s: ½; 1: 1 | S with y lies in {x, y}. All pairs in {x, i*} ∪ 2s have gcd ≤ 2, so S has at most two of them. | ¼ + ⅙ + 1/12 + ½ = 1 |
| M4c | x, i*: ½; 2s: ½; 1: 1 | S has at most two of {x, i*} ∪ 2s. **w_y = 0 is needed** because {x, y, i*} is admissible when t = y and a_x ≥ 1. | ¼ + ¼ + ½ = 1 |
| M4d | y, i*: ½; 2s: ½; 1: 1 | {x, y, i*} is admissible and weighs 1. Otherwise S has at most two of {i*} ∪ 2s. **w_x = 0 is needed** because gcd(X, I) ≥ 5. | 13/12 |

### 2.7 Exhaustiveness and the y–c multiplier choice

By (I1), fix the family Φ with Φ_yc = 1 at the same c. Then:

1. **Some plain entry is 5.**
   - If some C-entry is not 5, Lemma B applies (q may be i*).
   - Otherwise all four C-entries are 5. By (I2) and MU, all four C-entries of Φ′ equal 1, and Lemma A applies in Φ′. Lemma A does not need Φ′_yc = 1.
2. **No plain 5, and some plain 3 or at least three plain 1s.** Lemma A applies.
3. **Otherwise all plain entries are in {1, 2, 4} with at most two 1s.** The Main Lemma applies:
   - n₄ ≥ 1: M1.
   - n₄ = 0 and i* absent (N = 4, so n₂ ≥ 2): M2.
   - n₄ = 0 and i* present:
     - (n₁, n₂) = (2, 1): M3.
     - (n₁, n₂) ∈ {(1, 2), (0, 3)}: M4a–d, split by γ.
     - (3, 0) is already excluded.
   - γ is unconstrained in M1–M3, where w_i* = 0.

There is no gap in the case split.

## 3. Findings and smallest repairs (all MINOR; none changes a step)

**MINOR-1. SHAPE is stated for a bare tuple** (`:38`, `:53`; elision at `:51`).
- "KII tuple" is never defined, and the CE definition (README:33-35) is about configurations.
- Read as plain arithmetic (all gcds ≤ 6, a = 2), (⇒) is false. For example, (5, 5, 7, 11, 13, 17, 19) satisfies both conditions but has no SHAPE form.
- Read as "the tuple of an actual KII configuration", (⇐) would assert that such configurations exist.
- Only the configuration-relative reading is consistent. It is the reading the proof and every use (`:71`, `:165`) need.
- I kept this MINOR rather than MAJOR because it has no downstream effect.
- **Repairs:**
  - `:38`: "Let g_jU_j (j ∈ V) be pairwise disjoint left cosets in a finite group. Their tuple has all gcds ≤ 6 and a = 2 iff …".
  - `:53`: "…so the configuration is a CE with a = 2".
  - `:51`: add "(gcd(r_y, r_c) ≤ 2 is 1 since r_y is odd)".

**MINOR-2. Where SHAPE gets Sun(2)** (`:43-44`).
- "FC23 below proves Sun(2)" points to an argument written inside U_v (`:86-88`), but SHAPE needs Sun(2) in G.
- **Repair:** "the argument of `:86-88` with U_v replaced by G (finite by R0); also README L0.6".

**MINOR-3. Wording around "entry"** (`:130`, `:167`, `:164`).
- The row of c has six entries, not four.
- Read literally, `:167`'s "some entry differs from 5" is always true, because Φ_cx = 1. Lemma B also needs q ∈ C.
- "Both values of every multiplier" only fits φ.
- **Repairs:**
  - `:130`: "four C-entries Φ_cq, q ∈ C∖{c}".
  - `:167`: "some C-entry differs from 5 (Lemma B with that q)".
  - `:164`: "every value of every row-c multiplier".

**MINOR-4. Symbol overloading.** No step is affected, and overlay A-1 is respected (5-valuations are always written v₅).
- The marker t (`:57`, `:94-97`, `:107`, `:116-117`, `:137`) clashes with the fibre counts t_j (`:79`, `:83`, `:90`).
- N is used both in R0 (`:60`) and in the Main Lemma (`:135`).
- The index I_ij (`:64`) clashes with the label I (`:101-120`).
- **Repair:** rename t_j → m_j and the Main Lemma's N → N_pl, or add one notation line.

**MINOR-5. Admissibility checks are implicit in places.**
- "compatible" is never defined (`:127`, `:136-137`).
- M2 (`:141-142`) does not restate the bound for sets containing y.
- M4c (`:152-154`) does not say why {x, y, i*} is harmless.
- **Repairs:**
  - after `:81`: "j, j′ compatible iff gcd(λ_j, λ_j′) ≥ 2".
  - M2: "sets with y lie in {x, y}".
  - M4c: "w_y = 0, so {x, y, i*} weighs ≤ 1".

## 4. Computation-dependency boundary

- **Used:**
  - Lagrange;
  - L0.1 (product formula) and L0.2 (coset-intersection criterion);
  - finite-index cores;
  - disjointness of distinct double cosets;
  - Sun(2), proved in the file (`:86-88`);
  - Zhu's Sun(3), used only through FC23's 3-subset condition, in M2 and M4a–d only.
- Lemmas B, A, Z and Main cases M1, M3 need Sun(2) alone.
- **Not used, confirmed step by step:**
  - Sun(4), which the scope allowed but the proof never needs;
  - Sun(5), Sun(6) and Sun(7);
  - the general LFC(c) and VFC;
  - any StageB certificate, output or code;
  - K52-W;
  - minimal-counterexample frames and exponent caps;
  - any enumeration or computation.
- All valuations and objective sums are hand arithmetic, re-done here.
- **Not verified here:**
  - Zhu's proof and the citation at `:30`, which I took as the classical import the brief allows;
  - file hashes;
  - novelty.
- **Program level** (correctly stated at `:182-185`):
  - KII is defined from the index tuple by a = 2, so KII-W is computer-free modulo Zhu.
  - The reduction that makes the six classes exhaustive still uses Sun(6) (README:61) and Sun(5) (README:63), both computer-assisted.
  - Classes K7, K6.2\*, K6.3, K5.2\* and K5.3, and the StageB F-1 qualification, are unaffected.
