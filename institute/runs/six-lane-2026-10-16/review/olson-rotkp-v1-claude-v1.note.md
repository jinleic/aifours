# Audit of Theorem ROT-KP (SOURCE00) and its corollaries

**Result: 0 FATAL, 0 MAJOR, 9 MINOR.** Every new argument checks, and every import stays inside its stated hypotheses. Two boundaries are met with equality, and both are admissible as the imports are stated:
- (K) can hold as k = 2p−η−a_max−1.
- REFL-few-odd is used at exactly o_F = p.

No fix below changes a statement.

| Item | Verdict | Findings |
|---|---|---|
| ARC | ACCEPT | none |
| DIST0 | ACCEPT | none |
| WIND | ACCEPT | m2 (editorial only) |
| ONE0 | ACCEPT-WITH-FIXES | m2, m3 |
| ZP-D | ACCEPT | none |
| PAIR1-P | ACCEPT-WITH-FIXES | m4 |
| TRIPLE-ARC | ACCEPT | none |
| Theorem ROT-KP | ACCEPT-WITH-FIXES | m1, m5, m6 |
| INV*-KP | ACCEPT-WITH-FIXES | m7, m9 |
| OLSON-KP | ACCEPT-WITH-FIXES | m8, m9 |

## Checks

**1. ARC (SOURCE00:34-38)**
- **Sign changes.** S_j lies between R_j and R_(j+1) (SOURCE01:11). So z_A changes sign exactly at S_j and S_j′, and Φ=2 for every j≠j′. The adjacent case j′=j+1 just gives a one-run arc.
- **C_max.** All blocks are odd, from the normal form (SOURCE03:37-41; the even terminal is excluded there). So δ=k−Φ and C_max=2H+2.
- **Target.** T(z_A)=Σ_{i=j′+1..j} θ_i telescopes to y_j′−y_j.
- **Range of m.** C∈[2,2H+2] is equivalent to m∈[2κ̂,2p−2], together with m≤R.
- **m=0.** This is explicit in GRX (SOURCE01:18, Σ_0={0}). It is realised by c=l on S_j and S_j′ and c=l−1 elsewhere, which totals exactly 2p iff κ̂=0. SOURCE09:37 and SOURCE10:26 make the same use.
- **Representation.** GRX needs neither maximal blocks nor nonempty runs (SOURCE02:7, :29).
- **Sign convention.** Replacing z by −z negates both X^z and T (SOURCE01:40-41). Every downstream use is symmetric:
  - DIST0 has target 0;
  - ONE0's target ±t can be handled with π_{±t};
  - TRIPLE-ARC allows an arbitrary target τ.

  So the sign of T cannot break anything.

**2. Part A**
- **DIST0** is correct.
- **π_t** is conjugate to x↦x+t with t≠0, so it is a single p-cycle.
- **WIND.**
  - Each A_j has displacement in [1,p−1], so it meets each run at most once.
  - Concatenating the arcs along the single cycle gives a closed forward walk of length w_t·p.
  - Hence every run lies in exactly w_t arcs, with 1≤w_t≤p−1.
- **ONE0, same run.**
  - x+x′≠0 by (ZP) at m=2≤R=p.
  - α∉A_j for p−w_t≥1 values of j, and each such j gives an (ARC) selection.
  - So no run carries two rotation letters.
- **ONE0, different runs.**
  - Only the orientation (β∈A_j, α∉A_j) produces +t.
  - Inclusion plus equal cardinality w_t gives equality of the two index sets.
  - Run α sits between blocks α−1∈Q and α∈P; run β sits between β−1∈P and β∈Q. Since each arc crosses each run at most once, "A_j contains exactly one of α, β" is equivalent to "j and π_t(j) lie in different parts".
  - So π_t(P)⊆P, which contradicts transitivity of a p-cycle.
- **c≠0** follows from (ZP).
- **Byproduct (not claimed in SOURCE00).** At k=p, κ̂=0 every run carries exactly one rotation. This is consistent with SOURCE08:44, where the obstruction is a sequence example only.

**3. Part B**
- **(S1)** holds directly; see m1.
- **ZP-D.** |A_2|=4 uses three facts: the terms are nonzero, a≠b, and a+b≠0. If some step fails to grow, then A=Z_p and −s_i gives a nonempty zero-sum. The count p+1>p closes the proof.
- **PAIR1-P, SC0 scope.** SC0 is applied at lengths p+2 and p+1. Both are inside SOURCE06:16 (t≥p+1), and S⁺ has length ≥p+2 (SOURCE06:12).
- **Parity.** W−L≤p−2 and W−L is even, so W−L≤p−3.
- **u≠Y(0).** Y(0)=p·g for every odd generator g, so u=Y(0) would force W≥2p.
- **The a≥3 contradiction.**
  - h counts v itself, so (a−1)+2(h−1)≤p−3, giving a≤p−2h.
  - The number of unit terms is m₁≥a+h+1.
  - These unit terms are distinct from v (coefficient ≥3) and from u∉Y₀. So gᵃu is a genuine zero-sum of even length ≥4.
- **Coefficient bounds.** Positive coefficients ≤p−2 exclude both −g and Y(0) from Y₀. So u is the only −1.
- **Involution branch.**
  - The pairs {v,x} and {u,y} must meet, which forces x=y and 2u=0, so the value is Y(0) with exactly three copies.
  - Y″=Y−{u,v} is pair-free of length p.
  - The parity lift works: an even-size projected zero-sum is a zero-sum of Y″, and an odd-size one together with x is.
  - ZP-D then gives Y(c)^(p−1).
- **Exhaustiveness.** The three branches cover every Y.

**4. TRIPLE-ARC**
- U₊+U₋=p−1, so [−U₋,U₊] is a complete residue system mod p, and c is invertible.
- The needed ρ_c letters are available on the chosen side, and at most 2 of the 3 ρ₀ are used.
- If |D| is odd then |D|≤p−2. So 2≤m≤p−1≤min(p+2,2p−2).
- The argument is valid for every arc, and the sign of ρ₀ is irrelevant.

**5. Theorem**
- **Weights.** PAIR1-P(i) bounds |b|≤p−2 before b is identified with the SHgen weight b_x, which is the order V3 requires (SOURCE10:26).
- **(H)** is immediate.
- **(K).**
  - Only KETA's k-free clause η+a_max≤E+2 is used (SOURCE08:16), not its k≤p−1 clause.
  - So 2p−η−a_max−1≥p=k.
  - Equality is attainable: a single heavy (p−2)c with E=p−3.
  - SHgen tolerates equality: FLEXa's contradictions are strict (SOURCE09:108, :111), and the induction preserves (K) (SOURCE09:120).
- **No hidden k≤p−1 in SHgen (SOURCE09).**
  - Sec. 0 needs k≥2, odd blocks and nonempty runs; empty runs go to SHgen-E.
  - κ is integral because F≡k.
  - Lemma Ua sends k≤p to KB (SOURCE09:66), and κ(u°)≥1 holds.
- **SHgen-E.**
  - Expansions keep k=p, the block values and the genuine empty runs (SOURCE03:52-59).
  - REFL is needed only for o_F≤k=p (SOURCE03:48), which SOURCE11:6 supplies at its boundary.

**6. Corollaries**
- **κ̂ ≤ κ(w).** The normal-form process preserves F, and o counts odd sub-blocks (SOURCE03:30-37). So κ̂=κ(w)−(o_F−k)/2≤κ(w)≤1.
- **k versus o_F.** k≤o_F and k≡o_F (mod 2), and κ̂∈{0,1} whenever k≥2.
- **Case split.** k=1 via K1, 2≤k≤p−1 via ROT-K01, and k=p via ROT-KP. The split is complete.
- **Deletion ledger.** Case 2 gives (o−1,F−1) and Case 3 gives (o or o−2,F). Both preserve o≤p and F−o≥2p−4.

## Findings (all MINOR)

- **m1 (SOURCE00:71; also :15, :25).** S1+ is redundant here. Zero-sums of Y have even length, R=p+2<2p+1, and (ZP) already excludes lengths 4 to p+1.
  - **Fix:** derive (S1) in one line and drop the S1+ dependency.
- **m2 (SOURCE00:52-53, :63-65).** Both the WIND count and the P/Q crossing parity rely on an unstated fact: an arc of displacement ≤p−1 contains each run at most once.
  - **Fix:** state that fact.
- **m3 (SOURCE00:56-67).** The logical structure of ONE0 is left implicit.
  - **Fix:** say explicitly that case 1 shows no run has two letters and case 2 shows letters in distinct runs are equal. Optionally record the one-letter-per-run byproduct.
- **m4 (SOURCE00:86, :92-94, :96-98).** PAIR1-P is not fully self-contained.
  - **Fix 1:** justify "zero-sums are pairs": odd elements are nonzero, zero-sums have even length, and (S1) applies.
  - **Fix 2:** state that the a unit copies are distinct from v and from u.
  - **Fix 3:** note that an odd generator g has the form Y(c) with c≠0.
  - **Fix 4:** replace "As in the PAIR1 proof (K01 verdict…)" with the two-line, length-free pair argument. PAIR1 itself is accepted only for k≤p−1 (SOURCE08:17).
- **m5 (SOURCE00:25, :124-125).** The REFL interface is under-specified.
  - **Fix 1:** list restricted REFL (via SHgen-E) and the in-file Lemma ZP-D among Part B's inputs.
  - **Fix 2:** write o_F(u°)≤k=p, following SOURCE11:11; only ≤p is needed.
  - **Fix 3:** state that k=p is carried through the induction and that r4 Sec. 4 condition (d) is checked at each base word (SOURCE11:16). Cite SOURCE10:26 and SOURCE08:36 as the template.
- **m6 (SOURCE00:122-123).** Two boundary facts should be on the record.
  - **Fix:** record the (K) equality case, and note that k=p reaches Ua's KB branch (SOURCE09:66) for the first time in this programme.
- **m7 (SOURCE00:132).** Two small statements are missing.
  - **Fix:** write "k=1: Proposition K1, including c≠0" and "κ̂≥0 from the GRX all-plus pattern" (both per SOURCE04:53).
- **m8 (SOURCE00:133-135).** The ledger arithmetic at o=p is not shown.
  - **Fix:** spell it out:
    - Case 1: (F−o)/2≥(4p−3−p)/2≥p and o≤p≤2p−3 (SOURCE10:53).
    - Case 2: deletion only from odd blocks of length ≥3.
    - Case 3: deletion of distinct rotation occurrences.
    - No even-block deletion (SOURCE04:58).
- **m9 (SOURCE00:139-140).** The scope wording overstates novelty.
  - **Fix 1:** say "outside every earlier uniform range" (SOURCE06:45, SOURCE08:55). Words with o_F=p that have some normal form with k=p−2 were already covered existentially by ROT-K01.
  - **Fix 2:** note that for avoiders the new band is F∈{3p−4, 3p−2}.

## What remains unverified

- **SHgen's internal imports.** KB, KBH, B′(b), C1 and Davenport-alpha (SOURCE09:13-18) were not re-checked, in particular KB's own range at k=p. I relied on SHgen's stated scope (SOURCE09:125-128) and SOURCE10:26.
- **SC0's foundation.** The Savchev–Chen/Yuan index-one theorem behind SC0 was not re-checked.
- **REFL.** The REFL-few-odd r4 text and its condition (d) are not in the packet.
- **Olson case structure.** RGR-LONG and OLSON-few-v3 L28-47, including Case 1's framed-equal-pair argument, are not in the packet.
- **Normal form.** PM*, DAV and the one-block K1 were checked only as excerpted.
- **Existence.** Whether avoiders with k=p exist is not addressed.
- **Verification level.** This is a written audit only: no finite check was run and nothing was formally verified.
