# One-face Tuscan-1(11): the only possible face symmetry is the negation half-row double

Actual `/bin/date` before this body: **Sun Oct 25 22:55:34 PDT 2026**. InfoRecursiveMDS18-2, slot info-4. NEW WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO.

## 1. Why this matters for the unrestricted target

Every Tuscan-1(11) array is row-asymmetric (no symbol or global-reversal automorphism of its row set; unreviewed `unrestricted-prime-order-asymmetry-v1.md`, SHA256 `ac898bee2bb750d48b171f364c10a3e356f06c3d0105bf613dfb726f336235e7`; the symbol-automorphism half is re-derived in §3). A construction ansatz could still try a symmetry of the T-FACE whose shift is not a multiple of 10, because then rows are not mapped to rows. This packet classifies all such face symmetries for one-face arrays. The actual control (v24, SHA256 `e1fa1bd4dc53a90559b7b40a41bfbcab35ad31f96057f7d0121fb15a37194422`) shows the one-face regime is nonempty for Tuscan-1(11).

## 2. Setting

A one-face Tuscan-1(11) array is a cyclic sequence s_0,...,s_109 over eleven symbols in which every ordered pair of distinct symbols is consecutive exactly once, and the windows W_(10b)=(s_(10b),...,s_(10b+10)) are the eleven rows (permutations). Each symbol occurs exactly ten times. A **face symmetry** is a symbol permutation sigma and a shift k in Z_110 with s_(i+k)=sigma(s_i) for all i, (sigma,k) not (id,0). Distinct consecutive arcs force the face to have no proper period, so sigma has order exactly t=110/gcd(k,110).

## 3. Classification theorem

**Theorem.** If a one-face Tuscan-1(11) array has a face symmetry (sigma,k), then k=55 and sigma is an involution with exactly one fixed symbol. After relabeling, sigma is x->-x on F_11.

**Proof.** Let g=gcd(k,10). The window at 10b+jk is the sigma^j-image of the row W_(10b), hence a permutation; the starts 10b+jk run over all multiples of g modulo 110.

- **k a multiple of 10.** Then sigma maps row b to row b+k/10 entrywise. If sigma=id the face has period k<110 and repeats an arc. Otherwise a power tau of sigma of prime order q is a nontrivial row automorphism; a row fixed by tau is fixed entrywise, forcing tau=id, so tau acts freely on the eleven rows and q=11. So sigma is an 11-cycle and, relabeled as x->x+1, the rows are R+j for one row R; every difference e then occurs exactly once among R's ten consecutive differences, whose sum R_10-R_0 equals the sum of all nonzero residues, 0. So R_10=R_0, impossible.
- **g=1.** Every window of length eleven is a permutation. Consecutive windows W_i, W_(i+1) then force s_(i+11)=s_i, so the arc (s_0,s_1) recurs at position 11. Impossible.
- **g=2.** Windows at all even positions are permutations, so {s_(2c),s_(2c+1)}={s_(2c+11),s_(2c+12)}. These two arcs occupy different positions, so they are reverse arcs: s_(2c+11)=s_(2c+1) and s_(2c+12)=s_(2c). Hence s_(j+10)=s_j for every odd j, and the eleven odd positions 1,11,...,101 carry the same symbol: it occurs at least eleven times. Impossible.
- **g=5.** Then k=5m with m odd. If 11 does not divide m, gcd(k,110)=5 and sigma has order 22; an element of order 22 in S_11 needs cycle lengths with least common multiple 22, i.e. a 22-cycle or a 2-cycle plus an 11-cycle, more than eleven points. So k=55 and sigma is an involution. If sigma fixed two symbols a,b, the arc (a,b) at position i would recur at i+55. So sigma fixes at most one symbol, and exactly one because eleven is odd. QED.

## 4. Exact structure forced by the remaining case

Assume sigma(x)=-x and k=55. Then g=5: every window starting at a multiple of 5 is a permutation. Put X_j=(s_(5j),...,s_(5j+5)) for j in Z_22 (six symbols; consecutive X_j share the junction s_(5j+5)).

1. X_j ∪ X_(j+1) is all of F_11 and they meet only in their junction u_j=last(X_j)=first(X_(j+1)). Hence as SETS X_(j+1)=(F_11 minus X_j) ∪ {u_j} and X_(j+2)=(X_j minus {u_j}) ∪ {u_(j+1)}: every two steps one symbol is swapped.
2. X_(j+11) = -X_j, and row b is X_(2b) followed by X_(2b+1) (junction counted once). Equivalently row b = H_b followed by -H_(b+6) with H_b:=X_(2b), joined at H_b's last symbol = -(first symbol of H_(b+6)), and the cut condition first(H_(b+1)) = -(last symbol of H_(b+6)).
3. **Arcs (Tuscan-1).** The 55 arcs inside X_0,...,X_10 must contain exactly one arc from each of the 55 negation orbits {(a,b),(-a,-b)}: five orbits {(0,b),(0,-b)}, five {(a,0),(-a,0)}, five {(a,-a),(-a,a)} and forty generic.
4. **Junction multiplicity.** Every symbol is the junction symbol of exactly two of the 22 half-rows. Proof for a symbol x: outside junctions x alternates between consecutive half-rows; a junction at x puts x in two consecutive half-rows; a gap between consecutive junctions of x has odd length, the total length is 22, so the number J of junctions of x is even, and x then lies in 11+J/2 half-rows, counted with junction overlaps as 11-J/2 face occurrences. Ten occurrences give J=2. For x=0 the two junctions are 11 half-rows apart.
5. **Distance-2 (Tuscan-2) in this ansatz.** Interior distance-2 events are the four internal events of each X_j (88 in negation pairs) and the events across even junctions j=2b (11, middles at row position 5); odd junctions are row cuts. Tuscan-2 holds iff the 44 internal events of X_0,...,X_10 lie in 44 distinct negation orbits and the eleven even-junction events are pairwise distinct and lie in the eleven remaining orbits.

Item 1 is the set recursion only; no claim about the internal orders is made. Items 3–5 are exact restatements under the hypothesis of §4, not existence claims.

## 5. Consequences and nonclaims

- Any symmetric construction ansatz for a ONE-face Tuscan-1(11) or Tuscan-2(11) array must be the negation half-row double of §4; every other face symmetry, and every row symmetry, is impossible.
- Whether a negation half-row double Tuscan-1(11) exists is OPEN here; nothing above excludes it, and Etzion's control has no face symmetry (its s_0=9,s_1=10,s_2=1 against s_55=1,s_56=9,s_57=6 would need sigma(9)=1 and sigma(1)=6, not an involution).
- Multi-face arrays (several T-faces, possibly permuted by sigma) are NOT covered.
- No Tuscan-2(11) table and no all-array obstruction is supplied. The original target remains: a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array, which must use the distance-2 condition (v24 §7).

All cadence, private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
