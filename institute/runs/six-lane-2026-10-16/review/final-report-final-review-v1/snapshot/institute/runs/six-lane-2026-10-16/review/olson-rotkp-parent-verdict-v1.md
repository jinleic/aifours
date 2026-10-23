# Olson D_2p: Theorem ROT-KP (terminal k=p, kappa^ in {0,1}) accepted with uniform corollaries

Recorded at 2026-10-18T14:51:04-07:00.

**CORRECTNESS-ACCEPTED, with the mandatory overlay below.** Theorem ROT-KP, Corollary INV\*-KP and Corollary OLSON-KP hold at their stated scope relative to the parent-accepted dependencies. **No ordered-Olson theorem for D_2p in general, no INV\*(p), and no novelty claim follows.** The math-2 full target remains OPEN.

## Text and reviews

- [Candidate](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-KP-v1.md), SHA256 `472e43cf6c2652ecbc68704dea99fc84263ea241ef3a3147feb51902c43a800e`. Its 11 cited dependency hashes match the packet snapshot ([manifest](olson-rotkp-v1-review-v1/manifest.json)).
- [Codex](olson-rotkp-v1-codex-v1.note.md), SHA256 `29c35a62d419bc723a847a43b9360db43d69a66bc3d7d91a28c7b0b9c062d402`: ACCEPT on all ten items, 0 FATAL/MAJOR/MINOR. It checked that SHgen has no hidden k≤p−1 restriction and that the SHgen-E caller uses restricted REFL at o_F=p.
- [Claude](olson-rotkp-v1-claude-v1.note.md), SHA256 `1bf9430596fb17fd344a23330092305f62998e142ecc7721e0f2dbf547c5288d`: 0 FATAL, 0 MAJOR, 9 MINOR (editorial or self-containment). Six items ACCEPT and four ACCEPT-WITH-FIXES; no fix changes a statement. It checked the two equality boundaries: SHgen (K) at k=2p−η−a_max−1, and REFL-few-odd at o_F=p.

## Accepted statements

Let p≥5 be prime and w an avoider of length 4p−2 over D_2p.

1. **Theorem ROT-KP.** If some admissible normal form of w has terminal k=p and κ̂∈{0,1}, then every rotation letter of w lies in one set {ρ_c, ρ_−c} with c≠0. When κ̂=0 all rotation letters are equal.
2. **INV\*-KP.** Every avoider of length 4p−2 with o_F≤p and F−o_F≥2p−4 satisfies INV\*.
3. **OLSON-KP.** Every word of length 4p−1 over D_2p with o_F≤p and F−o_F≥2p−4 has an identity 2p-subword in increasing index order.

Relative to earlier uniform ranges, the new coverage is the boundary o_F=p. For length-(4p−2) avoiders this means F∈{3p−4, 3p−2}. Words with o_F=p that have some normal form with k≤p−1 were already covered existentially by ROT-K01.

## Independent parent derivation

**(ARC).** For blocks j≠j′, the arc pattern changes sign exactly at S_j and S_j′, so Φ=2. Its target telescopes to y_j′−y_j. Since all terminal blocks are odd, C∈[2,2H+2] is equivalent to m=2p−C being even with 2κ̂≤m≤2p−2, and m≤R from GRX. With κ̂=0, m=0 is admissible: the empty selection has sum 0 and GRX explicitly permits 2p−C=0.

**Part A (κ̂=0).** This needs only GRX and the normal form.
- Equal block values contradict ARC at m=0. So y is a bijection onto Z_p, and π_t=y⁻¹∘(+t)∘y is a single p-cycle.
- Arcs A_j=(j,π_t(j)] have displacement in [1,p−1], so each contains each run at most once. Concatenated along the cycle, they form a closed forward walk covering every labelled run exactly w_t times, with 1≤w_t≤p−1.
- **Two letters in one run.** Their sum t≠0 by (ZP). Every arc avoiding the run gives ARC with m=2, so the run would lie in all p arcs. That contradicts w_t≤p−1.
- **Letters x≠x′ in different runs α,β.** With t=x−x′, avoidance forces {j: β∈A_j}⊆{j: α∈A_j}. Equal cardinalities force equality. Crossing parity then gives π_t(P)⊆P for the nonempty proper block set P={α,…,β−1}, which no p-cycle allows.
- Two zero letters violate (ZP), so c≠0.

**Part B (κ̂=1).** Here R=p+2 and H=p−2. Zero-sums have even length; (ZP) excludes lengths 4..2p, and p+2<2p, so every zero-sum is a pair. As Claude's m1 notes, S1+ is not needed.
- **Lemma ZP-D** is the elementary subset-sum growth bound.
- **PAIR1-P branches.**
  - No pair: SC0 at length p+2.
  - A pair whose one-endpoint deletion Y_0 is zero-sum-free: SC0 at length p+1 gives W−L≤p−3 by parity. The h-count gives m_1−a≥h+1, so if v=a·g with a≥3, the occurrences g^a u (distinct from u and v) form a zero-sum of length ≥4. Hence v=g and u=−g.
  - Otherwise: three copies of the involution Y(0). Y″ is pair-free of length p, its Z_p projection minus x is zero-sum-free of length p−1, and ZP-D gives Y(0)³Y(c)^(p−1).
- **TRIPLE-ARC.** It refutes that exceptional sequence using the p consecutive integers [−U₋,U₊] and parity padding by at most two ρ₀ letters, with 2≤m≤p−1.
- **Otherwise SHgen applies.** (H) holds since 2H=2p−4≥p−3≥E. (K) holds since KETA's k-free inequality η+a_max≤E+2≤p−1 gives 2p−η−a_max−1≥p=k, with equality allowed. Empty runs route through SHgen-E, whose base words keep k=p and o_F=p≤p, inside restricted REFL-few-odd.

**Corollaries.** Normal forms have k≤o_F, k≡o_F (mod 2), and κ̂=κ(w)−(o_F−k)/2≤κ(w)≤1. The case split is: k=1 by Proposition K1; 2≤k≤p−1 by accepted ROT-K01; k=p by ROT-KP. Restricted REFL applies to w because o_F≤p. In the deletion ledger, Case 1 uses o≤p≤2p−3, Case 2 gives (o−1,F−1) and Case 3 gives (o or o−2, F); each preserves both inequalities. RGR-LONG then completes OLSON-KP.

## Mandatory overlay (Claude MINORs; no statement changes)

- **m1.** (S1) follows directly from (ZP), parity and R=p+2<2p. Drop the S1+ dependency.
- **m2.** State that an arc of displacement ≤p−1 contains each run at most once.
- **m3.** Make ONE0's structure explicit: no run carries two letters, and letters in distinct runs are equal. Hence each run carries at most one letter.
- **m4.** Justify that zero-sums are pairs, that the a unit copies are distinct from u and v, and that every odd generator is some Y(c) with c≠0. Replace the cross-reference to the PAIR1 derivation with the length-free pair-intersection argument; PAIR1 itself is accepted only for k≤p−1.
- **m5.** List restricted REFL (via SHgen-E) and Lemma ZP-D among Part B's inputs. Write o_F(u°)≤k=p, and note that k=p and REFL condition (d) are checked at each base word.
- **m6.** Record the (K) equality case and that k=p reaches SHgen Lemma Ua's KB branch.
- **m7.** k=1 is Proposition K1 including c≠0; κ̂≥0 comes from the GRX all-plus pattern.
- **m8.** Spell out the ledger arithmetic at o=p.
- **m9.** Say "outside every earlier uniform range" rather than "new", and give the avoider band F∈{3p−4,3p−2}.

## Imports and limits

Imports are the accepted GRX, normal form, DAV and K1, SC0 (with the explicit Savchev–Chen/Yuan index-one import), KETA, ROT-K01, SHgen and SHgen-E with the V3 overlay, restricted REFL-few-odd, RGR-LONG and the deletion ledger, all at their accepted scopes and overlays. Neither reviewer re-checked SHgen's internal imports (KB, KBH, B′(b), C1, Davenport-alpha), the REFL r4 text or RGR-LONG; they remain trusted at their accepted scopes.

No computation, Lean or human review was done, and no novelty claim is made. **Not covered:** κ̂≥2 at k=p, o_F>p, and κ̂≥2 outside accepted ranges. A separate candidate, ROT-ZR, is under review and is not used here.
