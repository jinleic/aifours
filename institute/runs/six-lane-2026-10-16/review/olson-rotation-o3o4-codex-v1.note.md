- **MAJOR — unsupported scope:** `01:LF9–10,116–118` asserts the p=5 extension using an unsupplied census. This packet does not establish it. **Repair:** restrict the written theorem and its at-most-four corollary to **primes p≥7**; identify p=5 separately as an unverified external claim. This does not affect the p≥7 proof.

- **MINOR — inaccurate enumeration wording:** `01:LF68–71` does not list every weight-zero four-element multiset over `{g,-g,-3g,3g}`: it omits `g(-g)(3g)(-3g)`. The preceding restriction already excludes this multiset: it would give at least `2p−3` copies of g together with 3g, producing the forbidden zero-sum `(3g)g^(2p−3)`. **Repair:** say “all admissible weight-zero multisets after the preceding restriction,” or list and exclude this fifth multiset explicitly.

**SOURCE00 ROT-o3-v3: DISPOSITION ACCEPT**, exactly for **three odd maximal cyclic constant reflection blocks and primes p≥5**.

**SOURCE01 ROT-o4-v2: DISPOSITION ACCEPT-WITH-FIXES**, exactly for **four odd maximal cyclic constant reflection blocks and primes p≥7**, with the statement and enumeration repairs above. The p=5 extension receives no endorsement.

No FATAL finding or MAJOR mathematical gap was found within these two requested ranges.

The substantive checks were:

- **INC — `00:LF15–36`:** The subset-sum expansion and extras budget are valid. Three distinct odd elements force extras `0+1+3=4`. The majority value is a generator under the stated prime and odd-first-coordinate hypotheses. In the exceptional disjoint case `p=5,e=3,m=n=3`, the inequalities force `b=5a=(1,0)`, immediately contradicting zero-sum-freeness through `b²`; the longer argument also excludes it. The repaired `n≥2` step works: either `b²a^(2p−6)` is available, or the first two copies of b contribute four extras. Consequently e=0,1 permit only `g^L`; e=2,3 additionally permit `g^(L−1)(3g)`. These displayed families are indeed zero-sum-free.

- **DEL and framing — `00:LF40–43,48–52`; `01:LF14–26`:** Deletion preserves avoidance and the rotation multiset. A singleton block disappears; subsequent reductions retain a **representation**, without requiring maximality. Empty runs cause no obstruction. At least two or three odd blocks survive respectively, so PM* never requires an invalid k=1 merge. For Davenport-alpha, choose the H empty interior gaps corresponding to disjoint adjacent reflection pairs, and frame at a gap outside that set. Its accepted length scope includes `4p−3`. Thus the bounds κ≤2 and κ≤3 follow. The stated GRX ZP/AP intervals, including their lower endpoints and size restrictions, are correct.

- **K2′ — `00:LF53–84`:** All κ=0,1,2 branches close. The pairwise-intersecting graph argument correctly yields a star or an involution triangle, with the latter excluded by INC. The κ=0 AP windows cover every residue, including empty selections where permitted. Both zero-sum extraction branches and their copy counts work. For p=5, the only additional nonzero weight sum actually occurring in the four-letter enumerations is `W=−10`, giving `(-g)(-3g)^3`; `(-3g)²g⁶` is available and forbidden. No wrap-around case remains.

- **K3′, κ=0,1,2 — `01:LF31–95`:** The corrected interval `[3−β_i,α_i+2]` is right. All missing-residue claims and selection-length bounds check out, including zero effective-sign counts. The κ=0 parity contradiction is valid. The κ=1 exceptional multiset is eliminated by the AP windows. In κ=2, all extraction branches reduce to rigidity or `g^(2p−1)(−3g)`; its AP argument covers every allocation, including empty runs. The four-entry residual lists are harmless supersets: their extra entry `g^(2p−4)(3g)(−3g)` already contains the forbidden length-four zero-sum `(-3g)g³`.

- **K3′, κ=3 — `01:LF98–110`:** Extraction is valid: after an initial pair, a second length-six zero-sum would itself create a forbidden length-eight union. The residual classifications and generator-copy bounds hold. The negative-weight prefix argument works when `#g≥10`. The remaining possibility is exactly p=7, `#g=9`; its bad prefix forces only negative weight −5, and the displayed `(-5g)^4g⁶` has weight `−14` and forbidden length ten. The final counting argument then forces `g^(2p−1)(−g)³`. No nonempty-run or RGR assumption is used.

I treated GRX, PM*, K1/K2, EGZ, the pairs bound, classical (D)/(Z1)/(Z2), and Davenport-alpha with the specified erratum as accepted imports. INC, DEL, the graph classifications, K2′ and K3′ were independently checked here; no finite aid was used as a premise. No circular dependency was found.

These conclusions establish only the stated partial rotation-rigidity results. They do not establish full ROT, INV*, or ordered Olson.