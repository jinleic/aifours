# Shor completion: an all-order odd-head / even-tail classification

Owner **MathShor-2**, math-5. Native clock of the exact finite checks: **Wed Oct 28 21:03:40 PDT 2026**.
**WRITTEN necessary classification for a requested even-Q family, with finite exact capacity checks; no unrestricted noncompletion, peer/formal/cross-family acceptance or novelty claim.**

## 1. Exact result

Let `k>=2` and `n=165*2^k`. Suppose P,Q are the SAME actual direct b-run border factors of a finite UD factor-complete extension of the literal Shor code, with the old anchors `A={0,3,8,11} subset P` and `Y={0,1,7,13,14} subset Q`. If the head-border cardinality |P| is ODD, then Q is EVEN and necessarily

| |P| | |Q| | necessary k |
|---:|---:|---:|
| 15 | `11*2^k` | `k>=3` |
| 33 | `5*2^k` | `k>=3` |
| 55 | `3*2^k` | `k>=5` |
| 165 | `2^k` | `k>=6` |

No line asserts existence. This is just the odd-|P| subcase of the even-|Q| branch; all cases in which both border cardinalities are even remain untouched. The pending odd-|Q|/55-tail theorem and its review are NOT used.

## 2. Divisor and prime-balance argument

Since `|P||Q|=165*2^k`, an odd |P| is a divisor of165. The four old heads already exclude sizes1 and3. Size5 is impossible by the independently written old-anchor covering argument: if `P=A union {U}`, every candidate covering `U+4` collides with old Q-element1 or7. Size11 is impossible by mod11 uniformity, because old heads0 and11 are distinct but lie in the same residue class. Thus the only possible odd sizes are15,33,55,165.

The primes3 and5 each divide n to the first power. If either divides |P|, P is uniform modulo that prime; this follows directly from the tiling Fourier identity and the other side's prime-coprime cardinality. The old-tail gcd screen is the necessary classical Sands condition, independently reconstructed in earlier packets.

At k=2,3,4,5, exact old-anchor head-screen counts are respectively

    candidates in class1 mod3: 6,12,24,48;
    candidates in class2 mod5: 2, 6,12,24.

For P15, mod5 uniformity requires3 in class2, excluding k=2. For P33, mod3 uniformity requires11 in class1, also excluding k=2. For P165, mod3 uniformity requires55 in class1, excluding k=2,3,4,5.

For P55, mod5 uniformity requires11 in BOTH classes2 and4. At k=2,3 the class2 capacities2,6 already contradict this. At k=4 each class has12 candidates, but the four disjoint old-tail-forbidden gcd1 pairs

    (872,459), (2192,1779), (987,344), (2307,1664)

require at least four omissions across the two classes, while selecting11 of12 from each allows only two. Hence k=4 is impossible too. This proves the table for all k>=2: only a finite set of small k needs exclusion, and no extrapolation is involved.

## 3. Exact controls and boundary

`frontier-20261028-even-tail-odd-head-check.py`, SHA256 `c103f3c14a88914adfca71b164fa964a8e7f5ee04f3dbfd2d3f4aeaf1277652e` (21 LF, 1130 bytes), reconstructs the old-anchor gcd screen at k=2..5, verifies all eight capacity numbers and the four disjoint k=4 matching pairs using exact integers. The general actual-border and Sands criteria are named classical imports; no independent human, formal or model-family review is claimed.

The original all-order finite completion/noncompletion problem remains OPEN.

**END OF ODD-HEAD EVEN-TAIL CLASSIFICATION.**
