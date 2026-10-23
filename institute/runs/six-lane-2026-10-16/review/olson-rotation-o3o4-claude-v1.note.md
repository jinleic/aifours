**Scope.** I read only the seven inline texts. I used no tools, ran no computation and did not check any hashes. These imports from 06 are taken as given: GRX, PM*, (D), (Z1), (Z2), the pairs bound, and Davenport-alpha with its erratum. Every new lemma of 00/01 (INC, DEL, K2', K3', star/triangle) is re-derived here. This is advisory only, with no gate authority and no novelty assessment.

## Findings — 00 (ROT-o3-v3)

**FATAL: none. MAJOR: none.**

**MINOR**
1. **INC and K2' do not state that p is prime** (`00:15`, `00:23`, `00:36`, `00:47`).
   - The step "a ≠ (1,0) ⇒ a is a generator" (`00:23`) and the Remark (`00:36`) need p prime.
   - Counterexample to the step: in Z₂×Z₉, a = (1,3) ≠ (1,0) has order 6.
   - Repair: write "Let p ≥ 5 be prime" in both INC and K2'.
2. **One-value case and a typo at `00:23`.**
   - The case n = 0 (Y = a^L) is never written. It only needs: aa is not a zero-sum, so a ≠ (1,0), so a is a generator.
   - "would make a a a zero-sum" should read "would make the pair aa a zero-sum".
3. **The inequality chain at `00:28` fails at p = 5.** "m ≥ ⌈L/2⌉ ≥ p−2 > 3" is false there.
   - Correct split: p ≥ 7 gives m ≥ 5. p = 5 with e ≤ 2 gives L ≥ 7, so m ≥ 4.
   - Only p = 5, e = 3, m = 3 remains.
4. **The exceptional case at `00:28-32` is vacuous.**
   - There 3 = m < d < 2p−m = 7 and d is odd, so d = 5 and b = 5a = (1,0). Then bb (n = 3) is already a zero-sum.
   - The ordering b a a a b b is computed correctly: deltas 1,2,2,2,4, extras 6, using b ∉ {±a, ±3a} and 2a ≠ 0. It is just superfluous.
   - Repair: replace it with the one-line exclusion.
   - This branch is unused anyway: 00 applies INC only with e = 2, and 01 only at p ≥ 7.
5. **DEL needs three explicit statements** (`00:40-43`).
   - (i) The resulting representation may be non-maximal: a merged run after deleting a 1-block, or equal adjacent blocks across empty runs.
   - (ii) GRX, PM*, the pairs bound and Davenport-alpha are applied to that representation, with H = Σ⌊lᵢ/2⌋ over representation blocks. None of them uses maximality.
   - (iii) o is read only on the maximal blocks of the original w.
   - Also state DEL for general o ≥ 3 (o odd blocks → o−1), since `01:15` uses it with o = 4.
6. **Two citations for the Davenport-alpha instance are unsupported** (`00:9-10`, `00:48`).
   - "Parent erratum m4" is not in the supplied 06 text. "As in GR0 (d)" cites an unreviewed file (`05:3-9`).
   - The needed instance is elementary, and I re-verified it:
     - Interior gaps of a constant block are empty, with bracket value y−y = 0.
     - Every second interior gap per block gives a pairwise non-adjacent set; gaps in different blocks are separated by a run gap.
     - The frame can be any run gap, which is not in I.
     - All R rotations are items, and total size ≤ N ≤ 4p−1 < 4p.
   - Repair: put this argument inline, pin the erratum by hash, and drop the GR0 citation.
7. **Case logic at `00:75-79` is implicit.**
   - Define #g as the multiplicity of g in Y.
   - State that 3g ∈ Y forces Y' = g^{2p−4}(3g), because Y' = g^{2p−3} gives #g ≥ 2p−3.
   - That is what licenses "Y' = g^{2p−3}: Z within {g, −g, −3g}".
8. **`00:90` overstates the scope.** Reword as: rotation rigidity (half (a) of INV*) for avoiders whose maximal blocks include at most 3 odd ones. It gives no reflection constancy and is not full ROT/INV*/ordered Olson.
9. **Finite aids at `00:92-95` are unaudited.** This includes "K2' is sharp in length". They are correctly not premises.

**Verified, no finding**
- **INC (a)–(c).**
  - The budget Σ(δ_t−1) ≤ e holds.
  - In (b), A₂+c is disjoint from A₂, including a+b+c (by parity and no zero-sum pair), giving extras 4.
  - In (c), the trichotomy on d gives d = 3.
- **Repaired n ≥ 2 step.**
  - If m+6 ≥ 2p, then bb·a^{2p−6} is a zero-sum.
  - Otherwise the second b adds (m+4..m+6)a, which are distinct since m+6 < 2p, so extras ≥ 4.
  - Classification: e = 0,1 gives g^L; e = 2,3 gives g^L or g^{L−1}(3g).
- **K2' pattern translation.**
  - (+,+) gives m ∈ [2κ+2, 2p].
  - (+,−) gives Φ = 2, δ = 0, C_max = 2H+2, so m ∈ [2κ, 2p−2] with T = θ₁.
  - R + H = 3p−4+κ, so κ ≤ 2.
- **K2' κ = 0.** All four (parity of α, s) cases are correct, including m = 0 (C = 2p = C_max).
- **K2' κ = 1.** Pairwise-intersecting pairs give empty, star or triangle. The triangle is killed by INC (e = 2) plus the Remark.
- **K2' κ = 2.**
  - |Z| = 2: u = ag with a ∈ [3, 2p−3] forces u = −3g, and then (3g)g^{2p−3} is a zero-sum.
  - |Z| = 4: Y' is zero-sum-free since 6, 8 ≤ 2p. The weight-0 enumeration is complete.
  - At p = 5, W = −10 gives only (−g)(−3g)³, and W = +10 is impossible. The exclusions (−3g)²g⁶ and (3g)²g^{2p−6} are valid at p = 5.
- **Sign of T.** No step depends on the sign of T (`06:30`): every use of (AP) covers all residues.

## Findings — 01 (ROT-o4-v2)

**FATAL: none for the written p ≥ 7 proof.**

**MAJOR**
- **M1. The theorem claims p ≥ 5, but p = 5 rests on an unsupplied census** (`01:1`, `01:9-10`, `01:116-118`).
  - That census is unreviewed, and it claims something much stronger: "every avoider of length 18 over D₁₀ is RGR". It is not endorsed here.
  - The written proof really does stop at p ≥ 7:
    - `01:67`: W = ±10 is possible at p = 5.
    - `01:100`: |Z| = 6 makes Y' zero-sum-free only if 6+6 ≤ 2p.
    - `01:103`: (3g)²g^{2p−6} has length 6 at p = 5, which κ = 3 does not forbid.
    - `01:106`: the step needs 12 ≤ 2p.
  - Repair:
    - State Theorem ROT-o4 for primes p ≥ 7.
    - Move p = 5 to a separate [F] claim that awaits its own review.
    - Restrict `01:118` to p ≥ 7 and make it conditional on ROT-o3 being accepted.

**MINOR**
1. **01 depends on new lemmas of 00** (`01:7-8`, `01:15`, `01:32`, `01:46-48`).
   - It uses INC with e = 2 and 3, DEL, and the star/triangle analysis.
   - These are not inherited acceptances. They stand only on an audit of 00; this one finds them correct.
   - DEL is quoted as "unchanged", but 00 states it only for o = 3.
2. **Normalisation at `01:27-28` is loose.**
   - "After INC" should be "after each case's classification", since g depends on the case.
   - State the automorphism ρ_v↦ρ_{v/c}, σ_v↦σ_{v/c}.
   - Weights are the fixed integer representatives 1, −1, ±3, −5.
3. **The completeness parenthetical at `01:70-71` is false.**
   - n₁−n₂−3n₃+3n₄ = 0 with Σn = 4 has five solutions; g(−g)(3g)(−3g) is missing.
   - That multiset is excluded in this branch by `01:68` ("3g in Z forces Z without g"), so the conclusion stands.
   - Repair: list all five and dismiss the fifth explicitly.
4. **The Y' list at `01:76` includes an excluded multiset.**
   - g^{2p−4}(3g)(−3g) is excluded: (−3g)g³ together with Z is a length-6 zero-sum.
   - "As for κ = 1" is inaccurate, since κ = 1 excluded it (`01:49-50`).
   - This is a harmless superset; label it as such.
5. **The extraction at `01:99` needs one more line.**
   - If |Z₁| = 2, apply (D) to the 2p elements of Y−Z₁ to get |Z₂| ≤ 6.
   - A total length of 8 is excluded because 8 ≤ 2p, so |Z| ∈ {4, 6}.
6. **Two claims at `01:100-101` need justification.**
   - |Z| = 6: a zero-sum of Y' (length 2, 4 or 6) plus Z has length 8, 10 or 12, all ≤ 2p for p ≥ 7.
   - |Z| = 4: a 4- or 6-zero-sum of Y' gives 8 or 10, and two disjoint pairs give 8. So Y' has only pairwise-intersecting pairs.
7. **`01:105-106`: "Σ_S b ≤ 10" uses |S| ≥ 2.** This holds because each b+1 ≤ 6 < 8; state it.
8. **Two remarks at `01:38` and `01:41` test only one integer representative.** These are "contains αᵢ+2 only" and "but not αᵢ+1". They are not needed, since the argument only uses the two failing combinations. Drop them.
9. **Finite aids at `01:120-124` are unaudited.** They are correctly not premises for p ≥ 7, but they are the only p = 5 input (see M1).

**Verified, no finding**
- **k = 3 pattern translation.**
  - Up to global sign there are four classes. For "+ on run i only": Φ = 2, δ = 1, C_max = 2H+2, T = θᵢ.
  - R = 2p−4+2κ and R+H = 3p−5+κ, so κ ≤ 3.
- **κ = 0.**
  - W0 has p−2 elements in both parities.
  - The failing combinations are exactly as stated, and the parity contradiction (Σα = 2p−5 is odd) holds.
  - An empty run (αᵢ = 0) changes nothing.
- **κ = 1.**
  - Star and triangle are handled via INC with e = 2 and e = 3.
  - The survivor g^{2p−4}(3g)(−g) fails in every (APᵢ), including the cases E₊ = 0 and E₋ = 0.
- **κ = 2.**
  - Both branches leave only g^{2p−1}(−3g).
  - When E± ≥ 3, W0 has p consecutive even values; t ∈ {−2, 0, 2} is reached with m = 4.
  - The cases α₁ ∈ {2p−3, 2p−2, 2p−1} all check out.
  - The final (AP_{i'}) is correctly run on an empty run, with no hidden nonemptiness assumption.
- **κ = 3.**
  - Every h lies in {−g, −3g, −5g, 3g}, with at most one 3g, and the prefix argument holds.
  - The p = 7 exception holds: #g = 9 forces N ⊆ {−5g} with |N| ≥ 6, and (−5g)⁴g⁶ = −14g = 0 has length 10 ∈ [8, 14].
  - Then T ≤ 6, 3g is absent, and Y = g^{2p−1}(−g)³.

## Dispositions

- **00 ROT-o3 (o = 3, all primes p ≥ 5): ACCEPT-WITH-FIXES.** 0 FATAL, 0 MAJOR, 9 MINOR. The fixes are wording and scope only; no formula or proof step changes.
- **01 ROT-o4 (o = 4, written proof, primes p ≥ 7): ACCEPT-WITH-FIXES.** This is conditional on 00's INC/DEL (audited correct here) and on fixing M1.
- **01 as printed (p ≥ 5): not accepted.** The p = 5 extension is **INCONCLUSIVE and not endorsed** from these texts.

## Audited vs imported

- **Audited here:**
  - INC (e = 0..3, p prime), DEL (o = 3 and its o = 4 variant), K2' and K3'.
  - The intersecting-pairs classification and the Davenport-alpha interior-gap instance.
  - The assembly of both theorems.
- **Imported, not re-audited:**
  - GRX (any representation, convention `06:7`), PM*, (D), (Z1), (Z2) and the pairs bound.
  - Davenport-alpha with its erratum (N ≤ 4p−1, F ≥ 2, frame outside I), and the marked formula behind it (`04:20-25`).
- **Not used and not endorsed:**
  - All finite aids (00 §4, 01 §4) and the p = 5 census.
  - Any claim of full ROT, INV*, reflection constancy or ordered Olson.
- **Circularity:** none. The dependency chain is 01 → 00 → 02/03/04, with no back-edge.
