# Audit: few-odd chain (SOURCE00–SOURCE04)

## Dispositions

| Source | Disposition |
|---|---|
| SOURCE00 OLSON-FEW v2 | **ACCEPT-WITH-FIXES.** (a) is complete given REFL-few-odd. (b) is a correct combination but carries the open status of SOURCE02 Sec. 1. |
| SOURCE01 INV*-FEW v2 | **ACCEPT-WITH-FIXES**, with the same split as SOURCE00. |
| SOURCE02 ROT-FEW-E v2 | **ACCEPT-WITH-FIXES** for Sec. 0 and Sec. 2. **INCONCLUSIVE** for Sec. 1 (Lemma SHgen-E): its content is claims about the *proof* of SHgen-v2, which is not in the packet. |
| SOURCE03 KAPPA01 v2 | **ACCEPT-WITH-FIXES.** Its empty-run branch carries SOURCE02 Sec. 1. |
| SOURCE04 REFL-few-odd r2 | **ACCEPT-WITH-FIXES.** The interface holds at every call site. Claim MON is verified against the file's own description of moves P1–P4. |

There are no FATAL or MAJOR findings, and no counterexample to any stated step.

## Checks that hold

**SOURCE00**
- **Coverage.** R ≤ 2 goes to Case 1; R ≥ 3 goes to Case 2 or Case 3.
- **Case 1 (L25–26).** F ≥ 4p−3 and Σ⌊l_i/2⌋ = (F−o_F)/2 ≥ p. This holds because every B used satisfies B ≤ 2p−3: 4 ≤ 7, and (2p+4)/5 ≤ 2p−3 for p ≥ 3.
- **Case 2 (L27–29).** The block keeps length ≥ 2 and no run changes, so o_F drops by exactly 1; INV* is used only at ≤ B−1. Re-inserting σ_y into an all-σ_y run keeps that run constant, and the rotations are untouched.
- **Case 3 (L30–35).**
  - Deleting one rotation creates at most one new adjacency, so at most one fusion and no cascade. The fused block has the common value, and its outer neighbours already differed from it. Hence o_F(w_i) ≤ o_F(w).
  - A third rotation has a nonzero value lying in both {±c₁} and {±c₂}, so the two pairs coincide.
  - Two consecutive reflections of different values in w stay consecutive in w₁, so w's runs are constant.
- **Ranges.** INV* is needed exactly up to B: B = 3 at p = 5 (ROT-o3 is accepted for p ≥ 5) and B = 4 at p ≥ 7.
  - p = 5 with o_F = 4 is correctly excluded. Case 3 would need INV* at o_F = 4, p = 5, which neither (a) nor (b) supplies (5·4 > 14).
  - The range values at L40 are right.
- **RGR-LONG (SOURCE05:7)** needs nothing beyond RGR and length 4p−1, so its use is correct.

**SOURCE01**
- **(a).** ROT-o2/o3/o4 are used exactly at their accepted scopes (SOURCE06:9, SOURCE07:7–10). The REFL instance has o_F ≤ 4 ≤ p.
- **(b)(i).** The given representation of u°(h) is its maximal decomposition:
  - its blocks are constant;
  - nonempty runs separate distinct maximal runs;
  - empty runs lie only between different values.

  Pair deletions keep parities, so o_F(u°(h)) = k ≤ o ≤ (2p+4)/5 ≤ p. An empty run between different values puts two values in one maximal run, so that run is not constant.
- **Consistency of "every block stays nonempty".** Expanding the heavies deletes E/2 pairs. (H) 2H ≥ E is exactly the condition that these fit into the k odd blocks without emptying one, since Σ(l_i−1)/2 = H.
- **Diff (L60–105).** The hunk headers (−1,13 +1,15; −26,7 +28,8; −36,7 +39,8) match the body. Only the header, citations and status words change.

**SOURCE02 Sec. 0 and Sec. 2**
- **F = 0 is excluded** by EGZ applied twice (SOURCE05:54).
- **Terminal forms.**
  - PM* applies while an even block exists among ≥ 2 blocks. So the process ends either with all blocks odd and empty runs only between different values, or with a single block.
  - A single even block is impossible. K1 forces F = 2p−1, which is odd (SOURCE06:32). Alternatively, Davenport gives F/2 ≥ p, and 2p equal reflections have product σ_y^{2p} = 1 with no adjacency needed.
  - Each step changes the odd count by 0 or −2, so k ≤ o and k ≡ o (mod 2).
- **κ ≤ k−1 (L28–29).** R = 2p+2κ−k, and R+H ≤ 3p−2 is equivalent to κ ≤ k−1.
- **Sec. 2** is valid given Sec. 1 and ROT-few-v3 Steps 1–5.

**SOURCE03**
- **Slice bookkeeping.** κ(w^) = κ(w) − (o−k)/2, so the slice cases at L17–20 are right.
- **All-plus pattern.** A zero-sum T of Y in Z₂×Z_p (|T| even, Σx = 0), plus (2p−|T|)/2 equal pairs taken inside blocks, is an identity selection. This needs |T| ≥ 2+2κ.
- **K0.**
  - L = 2p−k ≤ 2p−2, so Y is zero-sum-free, with e = k−1.
  - MULT's condition 3e+2 = 3k−1 ≤ 2p holds.
  - d_j ≤ k ≤ p−2 (at p = 5, k ≤ 3).
  - (H): 2p−2 ≥ k−1.
  - (K) is equivalent to 5k ≤ 4p−1, which follows from 3k ≤ 2p+1 for p ≥ 4.
- **K1 (κ = 1).**
  - Only length-2 zero-sums survive. Pairwise-intersecting edges form a star or a triangle: an edge meeting all three triangle edges contains two of its vertices.
  - A triangle forces 2Y(a) = 0, i.e. Y(a) = (1,0).
  - MULT parameters: e = k−3, k−2, k−1 in cases (i), (ii), (iii). Then 3e+2 = 3k−7, 3k−4, 3k−1, all ≤ 2p.
  - Case (iii): pg = (1,0) would need some d_j = p, but d_j ≤ k < p.
  - Case (ii): m′ ≥ 2p+2−3k/2 ≥ k−1, which is equivalent to 5k ≤ 4p+6. The zero-sum c₀g^d has length ≤ k ≤ 2p, so d = 1.
  - (H): 2p−4 ≥ k−2. (K) is equivalent to 5k ≤ 4p+2.
- **Corollary.** κ(w) = 1 with κ(w^) = 0 gives k = o−2 and 3k ≤ 2p−5, so K0 applies.
- **p = 5.** The corollary needs 3o ≤ 11, so o_F = 4 is excluded.
  - K0 and K1 bound k, not o. At p = 5 with o = 4 they reach only k = 2.
  - There MULT gives Σ(d_j−1) ≤ 1, so E = 0 without SHgen. Accepted K2 on the two-block form w^ already gives the same conclusion (SOURCE06:9, 29).
  - So nothing goes past the accepted scope in SOURCE07:11.
- **Binding constraint.** 3k ≤ 2p+1 is tight exactly where MULT is used with e = k−1 (K0 and K1(iii)), as L71 says.

**SOURCE04**
- **Remark (L25–27)** is correct.
- **Claim MON (L60–71).**
  - P1, single fusion: the result keeps X's parity.
  - P1, double fusion: the odd count goes from [X odd]+[Y odd] to [|X|+|Y| odd], i.e. 2→0, 1→1, 0→0. X = Y only if R = 0, which is handled by Lemma AR.
  - P2: the even block is absorbed and the merged run is nonempty, so nothing fuses.
  - P3: the filled run lay between different values, so no block changes.
  - P4: one fusion, with the parity of the sum.
- **Main logic (L53–58).** MON gives k ≤ o_F(terminal) ≤ o_F(w₀) ≤ p, which the small-k verdict excludes.
- **Interface at every call site.** Conditions (a) length 4p−2, (b) rotations in one nonzero pair, and (d) o_F ≤ p hold at all of these:

  | Call site | Word | o_F bound |
  |---|---|---|
  | SOURCE01:29–30 | w | ≤ 4 |
  | SOURCE01:33–37, SOURCE03:33–34, 58 | u°(h) | k ≤ (2p+4)/5 or (2p+1)/3 |
  | SOURCE01:37–38, SOURCE03:66 | w | ≤ (2p+4)/5 or (2p+1)/3 |
  | SOURCE00:23, via SOURCE01 | w′, w₁, w₂ | ≤ B |

## Findings

**FATAL:** none. **MAJOR:** none.

**MINOR**

- **m1, SOURCE00:10; also SOURCE03:14 and SOURCE03:34.** These cite INV*-FEW v1 (026753c9…), which SOURCE01 v2 (e71ece9e…) supersedes. There is no logical effect (SOURCE01:58). *Repair:* cite v2. In KAPPA01, cite SOURCE04 Sec. 4 directly.
- **m2, SOURCE00:8–9, SOURCE00:18; SOURCE01:19–20, SOURCE01:42–43.** The dependency list for (b) is incomplete. Besides SHgen and REFL-few-odd, (b) also uses:
  - ROT-FEW-E v2: its normal form, Lemma SHgen-E and Sec. 2 (v2 is unreviewed, SOURCE02:6);
  - ROT-few-v3 Sec. 1–6: MULT and Steps 1–5 (SOURCE02:13, 49–51).

  *Repair:* name both in the CONDITIONAL line and in Scope.
- **m3, SOURCE00:25–26.** A cyclically wrapping block can contribute a pair that is not linearly adjacent (RUNS erratum m6, SOURCE05:59). *Repair:* add one sentence:
  - start the frame at a rotation (R ≥ 1) or at a value change (R = 0);
  - a single constant cyclic run needs no pairing (σ_y^{2p} = 1);
  - conjugate back as in SOURCE05:49.
- **m4, SOURCE00:30.** Case 3 never uses "every odd block has length 1". For R ≥ 3, Case 3 alone suffices, so Case 2 is redundant. This is harmless. *Repair:* drop the clause, or note the redundancy.
- **m5, SOURCE01:33–37.** For the REFL instance on u°(h), two conditions should be stated:
  - c ≠ 0, as SOURCE04:15 requires; it follows from "no rotation is ρ₀" (SOURCE02:50);
  - this branch is entered only when w^ has an empty run (SOURCE02:35), so the empty run in the argument exists.
- **m6, SOURCE02:21–23.** "Read them as one (even) block … each such step lowers the number of odd blocks by 2" is false when one of the two equal-valued blocks is even.
  - *Counterexample:* take one maximal run with blocks A (odd, value u) | E1 (even, value v) | E2 (even, value u), empty runs between them, and nonempty runs outside.
  - PM* across E1 merges the two empty runs and absorbs E1 into A or into E2.
  - Either way, two u-valued blocks meet across an empty run and fuse into one block of odd length |A|+|E1|+|E2|. The odd count stays at 1.

  *Repair:* write "read them as one block (parity of the sum); the odd count drops by 2 or 0". The conclusions k ≤ o, k ≡ o (mod 2) and the two terminal forms are unaffected.
- **m7, SOURCE02:35–41 (the basis of the INCONCLUSIVE grade).** Observations (1) and (2), and "the induction step is unchanged; u° keeps the empty runs", are claims about SHgen-v2's proof (FLEXa, Ua, Sec. 4).
  - "The empty run survives" also needs two facts that the text never states. No rotation letter of u°(h), or of any induction descendant, may be placed into an empty run. No block may be merged or recoloured.
  - The text says only that reflection pairs are deleted inside blocks and that blocks stay nonempty.

  *Repair:* state these facts with SHgen-v2 line citations, and have SHgen-E checked against SHgen-v2 Sec. 4 by a reviewer who has that text. This item decides (b) of SOURCE00/01 and the empty-run branch at SOURCE03:33–34.
- **m8, SOURCE03:15 and SOURCE03:20 vs SOURCE03:37.** Name clash: "Proposition K1" at L20 is the accepted one-block K1 (SOURCE06:9), but Sec. 2 is also titled "Proposition K1". *Repair:* rename Sec. 2, e.g. to KAP1.
- **m9, SOURCE03:18.** The claim κ(w^) ≥ 0 has no reason given. *Repair:* add one line. w^ avoids (by PM*), and H(w^) ≥ p would give p equal pairs, i.e. an identity 2p-subword.
- **m10, SOURCE03:35 and SOURCE03:58.**
  - "If E ≥ 2 … so E = 0" silently uses that E = Σ(d_j−1) is even, which holds because every d_j is odd. *Repair:* say so.
  - Only (H), (K) and η ≥ 1 are checked against SHgen. *Repair:* list the remaining SHgen-v2 Sec. 0 clauses with c := g.
  - If the Step-4 bound E ≤ k−1−|N| (SOURCE02:50) is one of those clauses, it holds. |N| = 0 in K0 and K1(i); |N| = 1 with E ≤ k−2 in K1(ii).
- **m11, SOURCE04:69–70.** P4 must insert σ_yσ_y into, or beside, a block of value y.
  - *Counterexample:* inserted inside an even block of another value z, it raises o_F by 2: σ_zσ_z → σ_z σ_yσ_y σ_z.

  *Repair:* write "into a block of value y" and cite RED-r2 L144–147 for it.
- **m12, SOURCE04:55–56.** The argument needs only k ≤ o_F(terminal). The stated equality "k = o_F" holds only if the RES_< representation is the maximal decomposition, as L59 asserts. *Repair:* say this explicitly.
- **m13, SOURCE04:82–88; SOURCE00:8, SOURCE01:7, SOURCE03:12.** The interface report covers only ROT-FEW-E v1, and r2's review status is labelled differently in each file. *Repair:* have every user cite SOURCE04 Sec. 4 directly, and use one current status for r2 throughout.

## Audited versus imported

**Audited here**
- SOURCE00:22–36, the whole proof.
- SOURCE01:22–38 and its diff, L60–105.
- SOURCE02 Sec. 0 (L18–29), the Sec. 2 combination (L48–53), and its diff (L72–93).
- SOURCE03:16–66: all arithmetic, the star/triangle analysis, MULT parameters, (H)/(K), the slices, and the p = 5 scope.
- SOURCE04:11–27 (statement and Remark), Claim MON at L57–71 relative to its own description of P1–P4, and Sec. 4 at all call sites. Hash cross-references among SOURCE00–04 match.

**Imported, not re-checked**
- Accepted results:
  - RGR-LONG (SOURCE05:7);
  - GRX, PM*, K1/K2, ROT-o2 and errata M1/M4 (SOURCE06);
  - ROT-o3 for p ≥ 5 and ROT-o4 for p ≥ 7 (SOURCE07);
  - Davenport-alpha with erratum m4, EGZ, and (D) D(Z_2p) = 2p.
- The statement of SHgen-v2.
- ROT-few-v3 Sec. 1–6 (MULT (ii)/(iii), Steps 1–5), as characterised at SOURCE02:13, 49–51 and SOURCE03:28–29.
- RED-r2's proof (moves P1–P4, exits, terminal state in RES_<) as paraphrased at SOURCE04:53–70; the small-k verdict; Lemma AR.
- ELT0-FEW (SOURCE03:26), which the corollary does not use.
- **Not available, hence INCONCLUSIVE:** the SHgen-v2 proof facts behind Lemma SHgen-E (m7).
