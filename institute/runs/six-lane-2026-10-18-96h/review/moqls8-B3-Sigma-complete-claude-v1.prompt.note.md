# Independent review: Theorem M and Corollary Σ′/Σ (candidate LF1–142)

**Scope.**
- **Premises:** literal H1, H2 and H4(part), as fixed by scope-precision LF5, with rows 1 and 7 treated jointly (scope-precision LF9).
- **Background material:** I read AZ, its two errata, the scope note and Codex v1 only for the definition of Σ, the LF119 correction and history. No step below rests on them.
- **Method:** no tools, code or enumeration.

## Verdict

Theorem M and Corollary Σ′ (and therefore Σ) are **correct** under H1, H2 and H4(part). This holds for arbitrary complex phases and for every admissible pair q^1, q^7. Every step re-derives; N2 needs only a rescaling remark. The remaining findings concern presentation, attribution and bookkeeping.

| Category | FATAL | MAJOR | MINOR |
|---|---|---|---|
| New mathematics | 0 | 0 | 3 |
| Import / scope | 0 | 0 | 2 |
| Process | 0 | 0 | 1 |

## Re-derivation

**Notation.**
- ā is the complex conjugate.
- A := {1,2,3} is the coordinate set only; I write "A-part" for P_A Q_1(r,c).
- D := {0,4,5,6,7}.
- P_r := V_A ∩ (q^r)^⊥.

### Conventions, H1, F1, F2
- **Inner product.** LF17 and LF20 force ⟨u,v⟩ = Σ_d ū_d v_d. So a^r is the coordinate vector of q^r, Σ|a^r_d|² = 1, and Σ_d a^1_d ā^7_d = ⟨q^7,q^1⟩ = 0.
- **H1.** By [PRIM] LF210–216, 64 unit vectors Q_s(x)⊗Q_t(x) in C^64 form an ONB iff they are pairwise orthogonal. Since ⟨ψ⊗φ,ψ'⊗φ'⟩ = ⟨ψ,ψ'⟩⟨φ,φ'⟩, this is exactly H1. It constrains only cells that share no line.
- **F1** holds.
- **F2** holds:
  - Cells (0,d) and (i,c) with i ≥ 1 and d ≠ c share no line.
  - Because |w| = 1, the row-0 phase can neither create nor destroy a nonzero coordinate.
  - At a corner cell, every d ∈ D is admissible; d = 0 works via cell (0,0).

### Lemma 1: conjugations, line, frame, Gram formula
**The line.** Let x = P_A Q_1(r,c). Then:
- x_c = 0, from the column and H2.
- Σ ā_d x_d = 0, from the row, because q^r ∈ V_A gives ⟨q^r,Q⟩ = ⟨q^r,P_A Q⟩.

The bilinear complement of {ā, e_c} is spanned by ā × e_c:
```
ā×e_1 = (0, ā_3, −ā_2)    ā×e_2 = (−ā_3, 0, ā_1)    ā×e_3 = (ā_2, −ā_1, 0)
```
This matches LF30–32. The conjugate is essential: a × e_c is orthogonal to q̄^r, not to q^r.

**Frame identity (i).**
- Diagonal entries: Σ_{x≠d}|a_x|² = 1 − |a_d|².
- Each off-diagonal entry comes from a single line:
  - (1,2) from ℓ_3: ā_2·conj(−ā_1) = −a_1ā_2.
  - (1,3) from ℓ_2: −ā_3·a_1.
  - (2,3) from ℓ_1: ā_3·(−a_2).
- The sum is I − a a^*, with entries δ_ij − a_i ā_j. This is the orientation printed at LF48.

**Gram formula.** Since conj(ℓ_{r,c}) = a^r × e_c, the bilinear Lagrange identity gives, for any rows r and s:
```
⟨ℓ_{r,c}, ℓ_{s,c'}⟩ = ⟨q^s,q^r⟩·δ_{cc'} − a^r_{c'}·ā^s_c
```
- With r = s and c = c': ‖ℓ_{r,c}‖² = 1 − |a^r_c|², which lies in (0,1).
- With (r,s) = (1,7): the value is −a^1_{c'} ā^7_c ≠ 0 for all nine pairs (c,c'), as stated at LF37/LF51.
- Direct spot checks agree:
  - (1,1): a^1_2ā^7_2 + a^1_3ā^7_3 = −a^1_1ā^7_1.
  - (1,2): conj(−ā^1_2)·ā^7_1 = −a^1_2ā^7_1.

### Full-support use
All six numbers a^r_d are load-bearing:

| Step | Needs |
|---|---|
| LF40: corner set is a line | q^r ∉ span{e_c} |
| LF34/41 → LF65: supp ℓ_{r,c} = A∖{c}, so F2 removes both of those coordinates from squares 2–5 | a^r_d ≠ 0 for both d ≠ c |
| LF37/53: cross Gram ≠ 0 (drives LF84–86) | a^1_{c'} ≠ 0 and a^7_c ≠ 0 for all c, c' |
| LF113: distinct lines; LF117: masses in (0,1); weight uniqueness | all a^r_d ≠ 0 |

Full support is exactly what makes Lemma 2 tight. If one coordinate of A∖{c} vanished, ℓ_{r,c} would be a basis vector. One A-coordinate would then stay open to squares 2–5, giving six slots for five supports, and the singleton conclusion would fail.

### Lemma 2: five-support partition; projection vs whole-vector purity
- At a mixed cell the A-part is zℓ_{r,c} with z ≠ 0, so it is nonzero on both coordinates of A∖{c}. F2 removes these two coordinates from squares 2–5, and F1 removes c.
- Consider supp N together with supp Q_s(r,c) for s = 2,…,5:
  - These are five nonempty subsets of D.
  - They are pairwise disjoint by F2.
  - Since |D| = 5, they are singletons that partition D.
  - This step uses that there are exactly four other squares.
- **Squares 2–5:** their whole vectors are pure, Q_s(r,c) = ω_s e_{d_s} with |ω_s| = 1.
- **Square 1 is not pure:**
  - Q_1(r,c) = zℓ_{r,c} + βe_δ, with |z|²(1−|a^r_c|²) + |β|² = 1 and 0 < |β| < 1.
  - Only its complementary projection is a singleton.
- LF59–61 states exactly this. No later step treats Q_1 as pure: LF81 and LF86 always use both terms.

### Lemma 3: same-column leftover equality, off-diagonal condition, pure-A rule
For mixed cells (1,c) and (7,c'):
```
G_1((1,c),(7,c')) = −z̄_{1,c} z_{7,c'} a^1_{c'} ā^7_c  +  β̄_{1,c} β_{7,c'}·[δ(1,c) = δ(7,c')]
```
- **c' = c.** Column orthonormality forces the nonzero first term to cancel. This gives δ(1,c) = δ(7,c) and β̄_{1,c}β_{7,c} = z̄_{1,c}z_{7,c}a^1_c ā^7_c. Only the δ-equality is used later.
- **c' ≠ c with distinct δ's.** G_1 equals its nonzero first term, so G_s = 0 for every s ≥ 2. Equal δ is necessary for G_1 = 0; the candidate never claims it is sufficient.
- **Pure-A rule (LF86).**
  - It uses only Lemma 1 for the partner cell, whose A-part is z_{7,c}ℓ_{7,c} with z possibly 0.
  - It therefore holds without the partner being mixed.
  - It is symmetric in rows 1 and 7, since the swapped inner product is the conjugate.

### Theorem M: ordered-pair ownership and the 1+1+1 / 2+1 / 3 counts
Assume all six cells are mixed, and set δ(c) := δ(1,c) = δ(7,c).

**Basic constraints.**
- d_s(r,c) ∈ D∖{δ(c)}.
- Row orthonormality gives |T^r_s| = 3.
- Column orthonormality gives d_s(1,c) ≠ d_s(7,c).

**Matches are counted by intersections.**
- Send each x ∈ T^1_s ∩ T^7_s to the unique (c,c') with d_s(1,c) = x = d_s(7,c').
- c ≠ c' by the column constraint.
- The map is injective because d_s(1,·) is injective, and every match arises this way.
- Hence #matches(s) = |T^1_s ∩ T^7_s|.

**Ownership.** A match gives |G_s| = 1 whatever the phases. Then:
- **Against square 1:** H1 gives G_1 = 0, hence δ(c) = δ(c') by the contrapositive of Lemma 3.
- **Against any other t ≥ 2:** H1 gives G_t = 0, so t cannot match the same ordered pair on any coordinate. Ownership belongs to the cell pair {(1,c),(7,c')}.
- **Orientations:** (c,c') and (c',c) are different cell pairs, so both orientations are counted, with no factor-of-2 slip.

| δ multiplicities | Matches per square | Needed over 4 squares | Matchable ordered pairs |
|---|---|---|---|
| 1+1+1 | ≥ 3+3−5 = 1 | ≥ 4 (even 1 contradicts) | 0 |
| 2+1 | ≥ 3+3−5 = 1 | ≥ 4 | 2 |
| 3 | ≥ 3+3−4 = 2 | ≥ 8 | 6 |

These are all the partitions of 3, so the case split is exhaustive. Case 2+1 is symmetric in which column is the singleton. Every case contradicts the ownership bound.

### Corollary: frame-weight uniqueness
1. Compress Σ_{c=0..7}|Q_1(r,c)⟩⟨Q_1(r,c)| = I by P_A, using P_A|q^r⟩⟨q^r|P_A = |q^r⟩⟨q^r|. This gives LF111.
2. Under Σ′ in row r, Σ_c t_c ℓ_cℓ_c^* = Σ_c ℓ_cℓ_c^*, where t_c = |z_{r,c}|². A priori t_c = 0 is not excluded.
3. Each off-diagonal entry comes from a single line, and a_iā_j ≠ 0. So t_3 = t_2 = t_1 = 1.
4. Hence ‖P_A Q_1(r,c)‖² = 1−|a^r_c|² and ‖N_{r,c}‖² = |a^r_c|², both in (0,1). All three corners of that row are mixed.
5. Both rows are needed to reach Theorem M. Σ′ in one row constrains only that row, so no per-row conclusion follows, and none is claimed.
6. Σ ⇒ Σ′ under either reading of Σ ("exactly" or "within" columns 1–3). So the phrasings in AZ LF58, SC LF14 and parent-v2 item 4 all lead to the same result.

### Phases and axes
- **Phases** (w, ω, β, z, arg a^r_d) enter only in three ways:
  - non-vanishing of products of nonzeros;
  - moduli, such as |G_s| = 1;
  - bilinear cross-product and Lagrange identities, which hold over C.

  No step fixes or compares a phase.
- **Axis data:** the only data used is that q^1 and q^7 are orthonormal, lie in V_A and have full support. Any such pair works.
- **Never used:** H3/SB2, q^2–q^6, every column-0 vector of squares 2–5, the other template rows, and the "genuine" clause.

### LF119 against the pasted AZ text
- **Definition and quote:** the definition of Σ matches AZ LF58, and the quoted sentence is verbatim from AZ LF73.
- **The correction is mathematically right.** Lemma 1(i) is a weighted Parseval frame on the corner lines, with forced masses 1−|a^r_c|², for every unit full-support q^r. It therefore imposes no amplitude condition. This is the same identity as AZ erratum 1, E2, with B = [ℓ_1 ℓ_2 ℓ_3].
- **Status of Theorem L.**
  - AZ's H1, H2 and H4 contain this candidate's premises; AZ LF15 gives supp q_1^1 = supp q_1^7 = {1,2,3}.
  - So if this gate is accepted, Theorem L becomes a vacuously true conditional in its own scope, not a false one.
  - LF119's word "vacuous" is correct.

## Line findings

### New mathematics: 0 FATAL / 0 MAJOR / 3 MINOR

**N1 (MINOR) — LF34, 41, 58, 64–65, 94: notation.**
- **Problem:**
  - "A" is used as a coordinate set ("A∖{c}") without ever being defined.
  - LF58 then defines A := P_A Q_1(r,c), and LF64 uses both meanings in one sentence.
  - LF94 writes the vectors of squares 2–5 as e_{d_s(r,c)}, dropping the factor ω_s from LF59.
- **Effect:** none on the logic.
- **Fix:**
  - Define A := {1,2,3} after LF17.
  - Write A_{r,c} for the projection, as LF79 already does.
  - Write ω_s e_d at LF94.

**N2 (MINOR) — LF113–115: unnormalized projectors.**
- **Problem:**
  - The independence lemma is stated for "rank-one projectors", but it is applied to ℓ_{r,c}ℓ_{r,c}^*, whose trace is 1−|a^r_c|² ≠ 1.
  - The step "zero trace ⇒ affine dependence on the Bloch sphere" is valid only after normalizing.
  - The 2-dimensional space is never named; it is P_r, which contains each ℓ_{r,c} by LF41.
- **Effect:** rescaling by nonzero norms preserves linear independence, so the conclusion stands. The off-diagonal comparison above is a one-line replacement.

**N3 (MINOR) — LF132: "some of it" must be read jointly.**
- **Problem:**
  - "Hence, in such patterns, some of it lies in columns 4..7 or in pure-A corner cells" holds only if "it" means the combined A-content of rows 1 and 7.
  - Read per row, it is unproved: a row whose three corners are all mixed is not shown to need external A-content. Scope-precision LF9 also forbids the per-row reading.
  - For an A-free cell, the "Hence" relies on an unstated frame-uniqueness step: with zero external content, the coefficient of ℓ_{r,c}ℓ_{r,c}^* would have to be −1.
- **Effect:** confined to §6. Theorem M and the Corollary are unaffected.

### Import / scope: 0 FATAL / 0 MAJOR / 2 MINOR

**S1 (MINOR) — LF6, 7, 15, 107, 136: full support of q^1 attributed to [J].**
- **Problem:**
  - LF15 says the full support of q^1 is "as in the exact P1-B3 template [J]", and LF136 lists "[J] (template rows: full supports of q^1, q^7)".
  - The pasted [J] entry contains only `supports_row2to7`. Row 1 is absent.
  - The metadata key also does not establish that the listed entries are nonzero.
- **The existing bridge:**
  - Parent erratum v2, item 1, derives full support of q^1, and I checked it. q^1 lies in V_A ∩ {q^6,q^7}^⊥, which is spanned by conj(bc'−cb', ca', −ba'). If the first entry vanished, then (b',c') = λ(b,c), and orthogonality would force λ = 0.
  - The derivation is correct given exact supports for rows 2–7, H2 and column-0 orthonormality.
  - It is not part of this candidate, and it rests on the separate exactness binding.
- **Effect and rating:** none on the proofs, because H4(part) is an explicit premise here.
  - "B3 normal form" (LF6) and "every B3 axis and phase" (LF7, LF107) must be read as "every configuration satisfying H1, H2, H4(part)".
  - This is rated MINOR only because the scope note already restricts the claim. Read without that restriction, LF7 and LF107 would rest on an unbridged import.

**S2 (MINOR) — LF119: misattribution to Theorem L.**
- **Problem:** LF119 says "[AZ] Theorem L and its closing remark say…". The quoted sentence appears only in the AZ LF73 remark, after Theorem L's QED at LF71. Theorem L's statement and proof (LF58–71) make no amplitude claim.
- **Effect:** the substance of the correction is still right.
- **Fix:** attribute the sentence to the LF73 remark only.

### Process: 0 FATAL / 0 MAJOR / 1 MINOR

**P1 (MINOR) — LF119: stale AZ status.**
- **Problem:** "[AZ] … remains an unreviewed candidate" is stale. AZ was later reviewed and corrected, by worker erratum 1 (17:55:47, about four minutes after this candidate's 17:51:50 freeze) and by parent erratum v2.
- **Status:** already disclosed by scope-precision LF7, with no mathematical effect.
- **Unresolved:** the pasted material cannot show whether the statement was accurate at freeze time, because the AZ Codex review carries no timestamp.

### Observations (not counted)
- **"Genuine" is unused.** It appears at LF6, 13 and 91, but the theorem holds for any five MOQLS(8) satisfying H2 and H4(part). [PRIM] LF225 cuts off the set-level "classical" definition mid-sentence; this is immaterial for the same reason.
- **LF72–74 ("Assume further").** The cross-pair clause needs only (1,c) and (7,c') to be mixed.
- **H2** is a per-square isotopy normalization ((iii)). Taking it as a hypothesis is sufficient for this scope.
- **Timeline is consistent.**
  - SC freeze at 17:44:24, then this candidate at 17:51:50 (446 s, within the 1800 s checkpoint bound).
  - AZ erratum 1 followed at 17:55:47 and calls this candidate later and unused.
  - There is no circularity: erratum 1's E2 is a self-contained matrix identity, and this candidate cites no erratum.
- **Exposure** is disclosed at SC LF24. LF119 is the worker correcting their own earlier remark.

## Adjudication of Codex v1
- **Agreement:** I independently agree with all six of its PASS items. Its general Gram formula, its coefficient equation and its direct off-diagonal uniqueness argument are correct.
- **Its open point,** the LF119 attribution, could not be checked without the AZ text. It is now resolved: the quote is verbatim but misattributed to Theorem L (S2).
- **Coverage:** Codex mentioned the N2 rescaling without counting it as a finding. It did not raise N1, N3, S1, S2 or P1. None of these changes its zero-error verdict on the mathematics.

## What this verdict covers
**Established** under H1, H2 and H4(part), for all phases and all admissible q^1, q^7:
- Not all six cells of {1,7}×{1,2,3} are mixed.
- Σ′, for rows 1 and 7 jointly, is impossible.
- Therefore Σ is impossible.

**Not established and not claimed:**
- external A-content in each row separately;
- feasibility or exclusion of any corner pattern that is not all-mixed;
- the template-exactness bridge to "all B3";
- a full B3 no-go, or any global n = 8 result;
- any change to GB 15/18 or to the UNKNOWNs.

No Lean, human, novelty or full-problem certification is given.
