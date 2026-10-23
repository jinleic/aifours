**DISPOSITION: ACCEPT-WITH-FIXES**: 0 FATAL / 0 MAJOR / 9 MINOR. This disposition is advisory only. It carries no gate authority and makes no novelty claim.

Claim MON holds for every move and for both normalisations. Combined with RED-r2's accepted process and the accepted small-k corollary, it proves REFL(p) on o_F ≤ p. No further hypothesis is placed on w0. Every finding concerns citation, scope wording or interface documentation. None changes a case or the conclusion. I found no counterexample, and none can exist given the imports.

## 1. MON, re-derived

Write o_F = F − 2H, with H taken over the maximal blocks (SOURCE02:29-30). Then Δo_F = ΔF − 2ΔH.

| Step | Avoidance (re-checked) | ΔF | ΔH | Δo_F |
|---|---|---|---|---|
| x = 1 and N (SOURCE01:136) | automorphisms (SOURCE02:15-16, 35-36) | 0 | 0 | 0 |
| P1, single fusion | FUS + SPEC (SOURCE02:80-92) | 0 | 0 | 0 |
| P1, double fusion X·E·Y, Y = u across an empty run | same | 0 | [x, y both odd] | −2·[x, y both odd] |
| P2, both runs nonempty | PM0 (SOURCE02:107-114) | 0 | 0 | 0 |
| P3 | TR (SOURCE02:104-106) | 0 | 0 | 0 |
| P4, neighbours unequal | M0′ via H0 | +2 | +1 | 0 |
| P4, neighbours equal (they fuse) | same | +2 | 1 + [both odd] | −2·[both odd] |

**Avoidance checks**
- **FUS.** For c ≤ l, take c letters σ_u. For c > l with c − l even, take all σ_u and c − l letters σ_v. For c − l odd, l′ even forces c − l + 1 ≤ l′, so take l − 1 letters σ_u and c − l + 1 letters σ_v. In the second form the even σ_v part comes first.
- **TR.** The two moved letters have opposite effective signs in every zone, so E±(z) are fixed.
- **PM0.** The patterns of w′ are the patterns of w that do not separate j and j+1, and their windows are equal.
- **M0′.** In H0 (SOURCE02:56-58), D_P, m, β, θ, B − κ and A − κ are all unchanged. The terms ⌊(D_P+B)/2⌋, ⌊A/2⌋ and ⌊B/2⌋ can only fall. So every λ(P) and both ends of I(∅) shrink, while u_P is unchanged.

**Empty runs and cyclic wrap**
- g ≥ 1 forces k ≥ 2.
- P1 at k = 2: the far run of E leads back to X.
  - It cannot be empty, because then R = 0 (Lemma AR, SOURCE01:138-139).
  - So P1 is a single fusion to k = 1, with Δo_F = 0.
- Double fusion needs k ≥ 3, and it cannot cascade. Each outer empty run of the fused block borders a value ≠ u, by genuineness, so it stays genuine.
- P2 cannot occur at k = 2 with g ≥ 1.
- The new empty run created by P4 is absorbed when its neighbours have equal value, so g does not decrease.
- A P4 that produces κ ≤ 0 with g ≥ 1, or produces R = 0, is already a contradiction (K0*, Pairs at SOURCE02:69, or AR).
- The exits with g = 0 are contradictions inside RED, so MON is needed only at the terminal state.

**Relation of k to o_F.** In RES_<(p) every maximal block is odd (SOURCE01:133), so k = o_F exactly. Hence k(w_T) = o_F(w_T) ≤ o_F(w0) ≤ p.

## 2. Composition, κ-cases, smuggling

**Terminal state.** The terminal state w_T (with g ≥ 1) has these properties:
- no even block, since P1 and P2 are exhausted and k ≥ 2;
- every run pure or empty, since P3 and P4 are exhausted;
- κ ≥ 1 (K0*), and B ≤ κ (Z0, SOURCE02:68);
- B ≠ κ (Cor. B=K; since k ≤ p, KB* and CAP suffice);
- A ≥ B is kept.

So w_T ∈ RES_<(p). It is then excluded by SOURCE03:3,13:
- B = 0 is covered by B0S (SOURCE03:11), with κ > 0.
- B ≥ 1 is covered by MXG (SOURCE03:12).

The listed errata are met. Rotations are ρ_{±1}, so ρ_0 does not occur. A, B ≤ 2p − 1 holds by (Z0).

**κ-cases**
- **κ(w0) = 0:** K0* settles it directly (SOURCE02:156-159).
- **κ = 1:**
  - A P4 step from κ = 1 with g ≥ 1 gives κ ∈ {0, −1}, contradicting K0* or Pairs.
  - A terminal state with κ = 1 and B = 1 is excluded by B=K.
  - A terminal state with κ = 1 and B = 0 is excluded by K1*. B0S also excludes it here, so K1* is redundant for this corollary.
- κ ≥ 2 at the terminal state is not needed.

**Smuggling.** No hypothesis is placed on w0.
- (I1)-(I4) act only on the RGR words produced at the exits, including via TII and QQ (SOURCE01:150-161).
- No INV* result and no SHgen result is used.
- However, GRX and PM*, which are rotation-lane files, do enter through RED/K0* (SOURCE01:17-22; SOURCE04:7). They are accepted and self-contained, so there is no circularity with ROT-few-E. See m1.

## 3. Interface (Sec. 4)

Conditions (a), (b) with c ≠ 0, and (d) on the maximal decomposition are correct and sufficient. The Remark (SOURCE00:25-27) is correct: odd+odd gives even, and odd+even gives odd. The contrapositive is also correct. An empty run between different values, in any representation, means two consecutive distinct reflection letters.

ROT-few-E uses REFL at exactly two sites:

**U1: u°(h)** (SOURCE06:32-34)
- (a) and (b) are asserted there.
- (d) holds because the blocks are the k odd blocks of w^ (SOURCE06:19-20), with pairs deleted inside blocks (SOURCE06:33).
- By the Remark, o_F(u°) ≤ k ≤ o ≤ ⌊(2p+4)/5⌋ ≤ p.

**U2: w** (SOURCE06:46-47)
- (b) follows from the first conclusion of the theorem.
- o_F(w) = o ≤ p.

So the use matches the interface on the available text, subject to m8 and m9.

## 4. Findings (all MINOR)

**m1.** SOURCE00:5, 37-41, 49
- The import list is not "exact", and "no rotation-lane result" is literally false.
- Omitted:
  - GRX and PM*;
  - H0;
  - Theorem P, EGZ/AR and Davenport-alpha (SOURCE01:38);
  - Lemma M0 of proof-RUNS L408-410, used for P4 (SOURCE01:146);
  - Lemma BC of PAR-K0 (via SOURCE02:129);
  - SING, KB*, CAP, KBH*, K1*, TII and QQ;
  - the imports of B0S/MXG (SOURCE03:30, 46).
- Repair: say that no rotation-*rigidity* result is used, and that GRX/PM* enter only via RED-r2/K0star-r2 at the scopes in SOURCE04 (read with the dispositions at SOURCE04:39).

**m2.** SOURCE00:1
- The title says "odd maximal reflection blocks". It should say "odd maximal **constant** reflection blocks".
- Read as runs, the scope is wrong. Example at p = 5: w = (σ0 σ1 ρ1)^6. It has six maximal reflection runs, all of even length, so zero odd runs. It has 12 maximal constant blocks, all of length 1, so o_F = 12 > 5. (κ = 4 and R = 6, consistent with (0.1).) It is outside the corollary.

**m3.** SOURCE00:53-54
- "Neither step changes a block" is inaccurate: both normalisations change block values.
- What they preserve is the partition, the lengths, and the inequality of neighbouring values. That is what keeps k, g, H and o_F fixed.

**m4.** SOURCE00:65
- PM0 is cited as L107-110. Cite SOURCE02:107-114.
- The bookkeeping that P2 actually relies on is at L113-114.

**m5.** SOURCE00:69-71 against SOURCE01:147
- RED's "lowers κ by one more" is the overstated bookkeeping noted at SOURCE04:39. The extra drop happens only for odd+odd fusion.
- SOURCE00's own count is right, but it should note the erratum. It could also add the one-line proof via o_F = F − 2H from the table above.

**m6.** SOURCE00:14-20
- State the standing imports: (I1)-(I4), K0*, RED-r2, and B0S/MXG together with their errata (SOURCE03:44-48).
- "No RGR hypothesis" should say "on w0", since RGR theorems are used in the exits.

**m7.** SOURCE00:23-24
- Lemma AR is at SOURCE01:138-139 and SOURCE02:66-67, 161, not at L136.

**m8.** SOURCE00:82-88
- The report is unchecked hearsay.
- "That representation is the maximal decomposition, o_F(u°) = k" does not follow from SOURCE06:33, which does not say that rotation runs stay nonempty.
- Repair: replace it with "o_F(u°) ≤ k (Remark)" and cite SOURCE06:19-20, 32-34, 39-47.

**m9.** SOURCE00:75-81, read with SOURCE06:27-35
- Add "p ≥ 5 prime, u over D_(2p)" to the checklist.
- Lemma SHgen-E is stated under (K) only, which allows k > p. If ROT-few-E is rebased on REFL-few-odd, SHgen-E must carry k ≤ p. That holds at its only call, since k ≤ (2p+4)/5.
- (d) must also be checked for the base-case u°(h) at every induction level (SOURCE06:29, 35). This depends on SHgen-v2, which is not in the bundle.

## 5. Counterexample search

No counterexample is possible, since MON is an exact count. The −2 branches are attained, for example:
- P1: ρ1·σ0·σ2σ2·σ0·ρ1 becomes ρ1·σ0⁴·ρ1, so the contribution drops from 2 to 0.
- P4: σ3·ρ1ρ−1·σ3 becomes σ3σ3, so the contribution drops from 2 to 0.

So o_F is a monovariant, and k(w_T) ≤ o_F(w0) can be strict.

## 6. Audited versus imported

**Audited here:**
- MON and both normalisations, including the edge cases;
- avoidance preservation for P1-P4, a light re-derivation;
- the Remark;
- the composition RED-terminal → RES_<(p) with k = o_F → small-k;
- the κ routing;
- the absence of smuggled hypotheses;
- the Sec. 4 conditions;
- the two ROT-few-E use sites against SOURCE06's text.

**Imported, not audited:**
- RED-r2's exits, together with B=K, KB*, CAP, KBH*, K1*, TII, QQ and SING, plus termination and terminal completeness;
- K0*;
- (I1)-(I4);
- GRX, GR0, H0 and PM*;
- Theorem P, EGZ/AR and Lemma M0;
- B0S and MXG;
- SHgen-v2 and the construction of u°(h);
- the correctness of ROT-few-E itself.
