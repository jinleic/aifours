# Hostile audit: SOURCE00 `proof-ROT-K01-v1.md`

I used only the inlined texts. I took the SHA256 values as given; I could not recompute them. No K0 file, residual note, search result or model suggestion is used as a premise.

## Verdicts

| Statement | Verdict |
|---|---|
| KETA (SOURCE00:17-22) | **ACCEPT** |
| Sequence Lemma K1 (SOURCE00:24-57) | **ACCEPT-WITH-FIXES**. The mathematics is correct; fixes m2, m3, m9 |
| ROT-K01 (SOURCE00:61-74) | **ACCEPT-WITH-FIXES**: m2, m5, m9 |
| Uniform INV*-K01 (SOURCE00:77, 81-82) | **ACCEPT-WITH-FIXES**: m2, m4 |
| Uniform OLSON-K01 (SOURCE00:78-79, 83-84) | **ACCEPT-WITH-FIXES**: m10 |

There are 0 FATAL, 0 MAJOR and 10 MINOR findings.
- The explanation given at SOURCE00:94 is false (m1).
- "Subsumes ROT-K0" at SOURCE00:91 cannot be checked from this packet, so it is INCONCLUSIVE (m7).

## 1. KETA

**Heavy weights.** A heavy rotation is ρ_x with x ∉ {±c}. Its weight b_x is odd and |b_x| ≠ 1, so a_j ≥ 3. For ρ_0 the weight is p ≥ 5 (SOURCE03:39-42).

**The bound.**
- E ≥ (a_max−1) + 2(η−1), so a_max + 2η ≤ E + 3.
- For η ≥ 1 this gives η + a_max ≤ E + 2.
- With E ≤ k−1: 2p−η−a_max−1 ≥ 2p−k−2 ≥ k, which holds exactly when k ≤ p−1. This is (K) (SOURCE03:48).

**The case η = 0.** No (K) is needed: E = 0 and every rotation is light. Conversely, E = 0 forces η = 0, because each heavy adds at least 2 to E. E is always even (used in §5).

The proof is self-contained and does not depend on K0. It replaces the chain at SOURCE01:33 and is the reviewed form of the suggestion that SOURCE01:47 did not adopt.

## 2. Sequence Lemma K1

**Pair graph.**
- Odd elements give zero-sums of even length. So under (S1) at κ=1, the zero-sums are exactly the edges of the occurrence pair graph G.
- Two disjoint edges would form a zero-sum of length 4. So G has no two disjoint edges, which makes G a star or a triangle.
- SOURCE00:39-40 proves this directly. With P′={v,x} and P″={u,y}, we get x=y. Then x+v = x+u = u+v = 0, so 2u=0 and u=v=x=(1,0).

**Triangle (SOURCE00:41-44).**
- Any further edge must meet all three triangle edges, so none exists.
- Y−{u,v} is therefore zero-sum-free of length 2p−k ≥ p+1.
- The SC0 coefficient a of (1,0) satisfies ag = pg with a ≤ 2p−1, so a = p.
- The coefficient sum is at least p+(2p−k−1), which is ≥ 2p exactly when k ≤ p−1. This contradicts SC0 ✓.

**Star.**
- L = 2p+1−k ≥ p+2 and W−L ≤ k−2 ✓.
- (ii.1): v=(1,0) would give W ≥ 3p−k ≥ 2p+1 ✓.
- (ii.2): W−L ≥ (a−1)+2(h−1), so a ≤ k+1−2h, and m−a ≥ 2p−2k+h ≥ 3.
  - The copies of g lie in Y_0, so they are distinct from u.
  - g^a·u is then a zero-sum of length a+1 ≥ 4, which (S1) forbids. So a=1 ✓.
- Then a_i ≤ k−1 ≤ p−2, so b_g = a_i > 0, and b_g(u) = −1.
- Y_0 contains no −g, since it would pair with v. So E = W−L ≤ k−2 and N=1 ✓.
- Every other pair has the form {u, copy of g}, which is consistent with a star.

**Case (i).** R ≥ p+3, cost ≤ k−3, a_i ≤ k−2 and N=0 ✓.

**Edge cases (the text says nothing about them).**
- For k ≤ 2, case (i) cannot occur: SC0 would give R ≤ Σa_i ≤ 2p−1 < R.
- For k=1, case (ii) cannot occur either, since W−L ≤ −1.
- So no Y exists at k=1. The bound "|b| ≤ 0" is vacuous, and no negative cost is ever realized.
- At k=2 the lemma forces Y = g^{2p−1}(−g). This does satisfy (S1), with cost 1.

**Boundary k=p−1.** The triangle complement has length p+1, still inside SC0, and m−a ≥ 2+h.

**Example p=5, k=4.** g^6(3g)(−g) in Z_10 satisfies (S1), with E=2. Replacing u by −3g creates the zero-sum g^3(−3g).

## 3. ROT-K01

**Setup.**
- Y is the image of the rotations under ρ_x ↦ (1,x) ∈ Z_2×Z_p ≅ Z_(2p). This is the ZX convention, which is not inlined.
- R = 2p+2κ̂−k (SOURCE04:42).
- κ̂ is an integer because F ≡ k (mod 2), and it is assumed to lie in {0,1}.

**From (ZP) to (S1).** GRX gives (ZP) (SOURCE04:43). S1+ covers integers 0 ≤ κ ≤ (p+1)/2 (SOURCE05:19, 51) and gives (S1) ✓.

**The two κ̂ cases.**
- κ̂=0 (re-derived here):
  - The sequence has length 2p−k ≥ p+1.
  - SC0 gives Σ(a_i−1) ≤ k−1, so a_i ≤ k ≤ p−1. Since a_i is odd, a_i ≤ p−2, and N=0 ✓.
- κ̂=1: the new lemma applies with 2 ≤ k ≤ p−1 ✓.

**Weights.** g = (1,c) with c≠0, because g is a generator. An odd b with |b| ≤ p−2 and bc ≡ x is exactly SHgen's b_x (SOURCE03:39-41). So E agrees with SHgen's E, and ρ_0 (weight p) is absent ✓.

**Conditions.**
- (H): 2H = 2p−2−2κ̂ ≥ 2p−4 ≥ k−1 ≥ E ✓.
- (K): by KETA ✓.

**Closing the argument.**
- If all runs are nonempty, SHgen applies.
- Otherwise SHgen-E applies, since empty runs separate distinct values (SOURCE04:38).
  - Expansions keep k, the block values and the empty runs (SOURCE04:52-59).
  - Every base word u°(h) has length 4p−2, rotations in {ρ_c,ρ_−c}, and o_F = k ≤ p−1 ≤ p (SOURCE04:66-70). This is within REFL-few-odd (SOURCE04:48; SOURCE01:33) ✓.
- Because ŵ avoids, η = 0. ŵ and w have the same rotations (SOURCE04:37) ✓.

**k=1.** SOURCE00:74 must mean the accepted Proposition K1. The new lemma is vacuous at k=1 and cannot serve (m2).

## 4. Uniform corollaries

**(a), INV\*-K01.**
- The normal-form process applies to every avoider. It ends with 1 ≤ k ≤ o odd blocks (SOURCE04:30-43).
- κ̂ = κ(w)−(o−k)/2 ≤ 1.
- κ̂ ≥ 0 for k ≥ 2 by GRX (SOURCE03:37; SOURCE01:41). This step is missing at SOURCE00:81 (m4).
- If k=1, Proposition K1 gives the pair with c≠0.
- If k ≥ 2, ROT-K01 applies, since k ≤ o ≤ p−1.
- Restricted REFL then applies to the original word, since o_F ≤ p−1 ≤ p ✓.
- κ(w) < 0 only leaves the k=1 case.

**(b), OLSON-K01.**
- Case 1: o ≤ p−1 ≤ 2p−3 gives (F−o)/2 ≥ p framed pairs (SOURCE07:31-36).
- Case 2 gives (o−1, F−1): o′ ≤ p−2 and F′−o′ = F−o.
- Case 3 gives (o or o−2, F): o′ ≤ o and F−o′ ≥ F−o (SOURCE05:58).
- Each w′ and w_i is a length-(4p−2) avoider satisfying (a). RGR-LONG then gives the increasing-order identity subword ✓.

**Examples.**
- p=7: ⌊27/5⌋=5, so the new class is o_F=6 with F ≥ 16. ZX+ covers o ≤ 5 (SOURCE05:32) ✓.
- p=11: ⌊43/5⌋=8, so o_F ∈ {9,10} with F ≥ o_F+18 ✓.
- p=13: o_F ∈ {11,12} with F ≥ o_F+22 ✓.
- p=5: the band is {4}, which is already unconditional (SOURCE05:27, 31). So it is empty (m6).

## 5. What actually fails at k=p (SOURCE00:94)

The reason given for κ̂=1 is wrong. At k=p, |Y_0| = 2p+1−k = p+1, which is inside SC0's range t ≥ p+1 (SOURCE01:16; SOURCE02:22).

Tracing the proof at k=p (diagnostic only; no extension is claimed):
- Case (i) (R=p+2) survives.
- (ii.1) survives, since W ≥ 2p.
- (ii.2) survives, since m−a ≥ h ≥ 1.
- E ≤ p−2 and E is even, so E ≤ p−3 and (K) still holds by parity. SOURCE00:22's chain as written, however, needs k ≤ p−1.

**The failing step is the involution-triple exclusion, SOURCE00:41-44.** Y−{u,v} has length p, below SC0's range. Also p+(2p−k−1) = 2p−1, which is no contradiction. This is a real failure, not just a gap in the proof.

**Counterexample at the sequence level.**
- Take x≠0 and Y = (1,0)^3 (1,x)^{p−1}. Its length is p+2 = 2p+2−p.
- A subsequence with j copies of (1,0) and i copies of (1,x) sums to ((i+j) mod 2, ix). This is zero only when i=0 and j is even.
- So every zero-sum has length ≤ 2 and (S1) holds.
- But (1,0) = pg for every generator g, so |b_g| = p > k−1.
- For p=5 this is 5^3·1^4 in Z_10.

The triangle at k=p forces exactly this shape. x·T is zero-sum-free exactly when the Z_p-projection of T is zero-sum-free of length p−1, which by the classical result makes it constant. No avoider with rotation multiset ρ_0^3ρ_x^{p−1} is claimed or refuted.

**κ̂=0, k=p.** SC0 does stop at length p ("S(p)" is not defined in the packet). There are two further problems:
- (1,0)(1,x)^{p−1} is zero-sum-free of length p and contains ρ_0.
- g^{p−2}(3g)((p−2)g) has coefficient sum 2p−1, E = p−1, η = 2 and a_max = p−2. Then 2p−η−a_max−1 = p−1 < k, so (K) fails.

## Findings (all MINOR)

- **m1** SOURCE00:94. Replace with: "k=p: for κ̂=1 the involution-triple exclusion (Sec. 2 (ii.0)) fails. Y−{u,v} has length p, and (1,0)^3(1,x)^{p−1} satisfies (S1) at κ=1 with R=p+2 while containing ρ_0. Sec. 1's chain also needs k ≤ p−1. For κ̂=0, SC0 stops at length p, (1,0)(1,x)^{p−1} is zero-sum-free, and (K) can fail. No word-level counterexample is claimed."
- **m2** SOURCE00:13, 24, 68, 74, 81. The name "K1" collides with the accepted Proposition K1. Rename the Sec. 2 lemma "Lemma PAIR1". At lines 13, 74 and 81, write "Proposition K1 (lowodd verdict v2), including c≠0".
- **m3** SOURCE00:26, 33-36, 45-47. Add: "For k ≤ 2, case (i) does not occur. For k=1, case (ii) does not occur either (W−L ≤ −1), so the lemma is vacuous at k=1."
- **m4** SOURCE00:81. Insert: "κ̂ ∈ ℤ, and κ̂ ≥ 0 for k ≥ 2 by GRX (SOURCE03:37)."
- **m5** SOURCE00:73. Replace with: "If η=0, we are done. Otherwise SHgen, or SHgen-E (generalized ZS v2 overlay V3), applies. Every expansion preserves k, the block values and the empty runs. Every base word has length 4p−2, rotations in {ρ_c,ρ_−c} with c≠0, and o_F = k ≤ p−1 ≤ p, so REFL-few-odd discharges REFL. The resulting identity subword contradicts the avoidance of ŵ."
- **m6** SOURCE00:88-90. Write: "uniformly ⌊(4p−1)/5⌋ < o_F ≤ p−1 with F ≥ o_F+2p−4, outside every earlier uniform range; empty at p=5."
- **m7** SOURCE00:6, 91-92. "Subsumes ROT-K0" cannot be verified from the packet. Write instead "re-derives κ̂=0, 2 ≤ k ≤ p−1 independently". Replace "by the same method" with "via SC0 and the pair graph, not the ZX exchange".
- **m8** SOURCE00:93-95. Add "k ≥ p+1 with κ̂ ∈ {0,1}" to the list. State that this route covers no κ̂ ≥ 2 at all.
- **m9** SOURCE00:28-29, 65-69. Define Y, Y(c) and b_g, with |b| ≤ p−2 and b_g((1,0)) = p. Define cost = E+N, where N is the number of negative coefficients. These are ZX definitions that are not inlined. Note that ROT-K01 uses only |b| and E.
- **m10** SOURCE00:83-84. Cite SOURCE05:58 and SOURCE07:31-46. State that o ≤ p−1 ≤ 2p−3 in Case 1, and that each w′ and w_i satisfies (a).

## Audited versus imported

**Audited here:**
- KETA.
- The whole sequence lemma, including the pair graph, the triangle, k ≤ 2 and k=p−1.
- The κ̂=0 re-derivation.
- The weight identification, (H), (K) and the SHgen-E caller discharge.
- The corollary inequalities, the deletion bounds and the examples.
- The k=p trace and both counterexamples.

**Imported and not re-certified:**
- SC0, and through it the index-one theorem (SOURCE01:16, 28; SOURCE06:9-11) and D(C_2p).
- S1+ and S1(a).
- GRX and (ZP).
- The normal form, PM* and Proposition K1.
- SHgen, and SHgen-E with ZS v2 overlay V3 (V3 is not inlined).
- REFL-few-odd. Its statement is not inlined; I took its scope o_F ≤ p from SOURCE01:33-34 and SOURCE04:48.
- RGR-LONG and the OLSON case structure and deletion ledger.
- The ZX definitions.
- For the k=p diagnostic only, the classical structure of length-(p−1) zero-sum-free sequences in C_p.
