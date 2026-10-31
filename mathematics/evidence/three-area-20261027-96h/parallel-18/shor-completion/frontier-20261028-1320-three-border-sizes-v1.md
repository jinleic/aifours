# Shor completion: a two-class Hall obstruction at order 1320

Owner **MathShor-2**, math-5. Native `/bin/date` from the finite check: **Wed Oct 28 19:17:55 PDT 2026**.
**Conditional written deduction with two exact finite Hall counts. This is not an n=1320 exclusion, unrestricted no-go, formal proof, independent-family review or novelty clearance.**

## 1. Result

For any hypothetical finite UD factor-complete extension of the literal Shor code with pure-a order1320, the same-code direct border factorization must satisfy

    |P| in {20,24,44},    |Q| in {66,55,30}.                    (1)

The preceding `frontier-20261028-1320-four-border-sizes-v1.md` had the four cases `{12,20,24,44}`. This packet independently rules out the `|P|=12, |Q|=110` case by a small two-residue Hall obstruction. The remaining three pairs are NOT asserted feasible, and n=1320 remains OPEN.

## 2. Necessary uniformity and the candidate graph

If `|P|=12`, then `|Q|=110`. Since 11 divides1320 only once and 11 does not divide |P|, the direct-tiling Fourier identity forces Q uniform modulo11. Thus Q contains exactly10 elements in each of the classes0 and3 modulo11.

The predecessor's old-anchor gcd screen defines C_Q as all residues individually compatible with the actual old tail anchors `Y={0,1,7,13,14}`. It uses the classical Sands divisor-difference condition, with an explicit proof in `frontier-20261028-1320-divisor-class-obstruction-v1.md`. Let

    L={q in C_Q : q==0 mod11} minus {0},
    R={q in C_Q : q==3 mod11} minus {14}.

Both L and R have exactly25 residues. The anchor0 itself belongs to Q and is in the first mod11 class; 14 belongs to Q and is in the second. Hence a putative Q must select exactly9 vertices from each of L and R.

Connect `x in L` and `y in R` if `gcd(x-y,1320)` is one of `{3,5,8}`. Each of these gcd classes is present among old head differences, so no actual Q may select both endpoints of any such edge. We use only these edges, not any stronger assumed code property.

## 3. Exact Hall counts

`frontier-20261028-1320-hall-check.py` independently reconstructs C_Q, L, R and the complete bipartite edge relation from integers and gcd. It exhaustively checked the following two orientations:

* Every one of the `C(25,9)=2,042,975` nine-subsets of L has at least18 neighbors in R. The minimum18 is attained by11 subsets.
* Independently in the transposed graph, every one of the `C(25,8)=1,081,575` eight-subsets of R has at least17 neighbors in L. The minimum17 is attained by10 subsets.

Either count suffices. For the first, nine selected L-elements forbid at least18 of the25 R-elements, leaving at most7, fewer than the required9. For the second, eight selected R-elements already forbid at least17 L-elements, leaving at most8, fewer than the required9. Thus `|Q|=110` is impossible.

The check records complete neighborhood histograms and minimizing examples, asserts the exact combinatorial counts, and checks the two anchors are compatible with all vertices as required by the independently generated candidate set. It uses exact integer bit operations and gcd only; no SAT solver or approximate computation is used.

The new `|P|>=20` further strengthens the preceding graded same-code tradeoff: `N_out<264` forces at least **16** actual multi-b suffix-border atoms. Together with `|Q|>=30`, the condition `N_Y<220` forces at least **25** actual multi-b prefix-border atoms; if both conditions hold, these are at least41 distinct atoms. These are necessary conditions only.

## 4. Witness pin and scope

`frontier-20261028-1320-hall-check.py`, SHA256 `715b325871c8148c1d62647e4925fca1edc23a4a9e71840bd41a6250b59404b6` (33 LF, 1522 bytes), produced the counts above and both full histograms. This finite enumeration is computer-assisted same-harness evidence; it is neither a formal proof nor an independent-model-family review. The prime-balance and gcd-disjointness facts are explicitly inherited from the preceding written packets; the latter is a classical Sands theorem. This result has not been independently reviewed or novelty screened.

The original finite UD factor-completion problem remains OPEN, and the `{20,24,44}` cases have not been resolved by this packet.

**END OF THREE-SIZE ORDER-1320 REDUCTION.**
