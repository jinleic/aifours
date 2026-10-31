# Erratum 1: withdraws the missing-pair permutation claim; retains the reversal bijection

Owner **InfoRecursiveMDS18-2**, info-4. Actual `/bin/date` before writing: **Thu Oct 29 19:58:53 PDT 2026**. Additive; the pinned packet `frontier-20261029-reversal-multigraph-and-missing-pair-structure-v1.md` (SHA-256 `abfc0a0bf95eb9ecfe40240f8b4621e0162cccd55f13b4714c5b7cac59f82635`) is preserved unchanged.

## 1. Withdrawn claims

1. **"M is a fixed-point-free permutation of the 11 symbols; p_x=s_x=1 for every x" (former Lemma 1 and item 1/2 of §4) is FALSE and is withdrawn.** The correct counting is: the source positions of linear distance-two events are positions 0..n−3; by T1, the last column is a permutation, so each symbol's missing out-degree is exactly its number of occurrences in the penultimate column, and dually its missing in-degree is its number of occurrences in the second column. Nothing forces these to be 1. At n=8 the pinned T2(8) arrays have penultimate/second-column multiplicities different from all-1, which contradicts the withdrawn claim directly.
2. **Lemma 4 / Corollary 4.1 ("G(row x) ≠ M-target(x)", "π fixed-point-free") is withdrawn**: it rested on the same false premise. The paragraph in Lemma 4 arguing that a penultimate symbol is always a distance-two target is invalid — a symbol may sit after position n−3.
3. **Lemma 3's H-loop/matching discussion and §2's "matching among symbols" statements are superseded**: the same-row double adjacency is impossible outright (this part was right), so those qualifiers are moot rather than wrong, but their presentation as separate lemmas was tangled and is not relied on.
4. Theorem 6's K₁₁ discussion is retained only in its corrected form below; the sentence beginning "no contradiction arises yet" through Theorem 7's assembly **is withdrawn as stated**, because it cites Corollary 4.1.

## 2. Corrected statement actually proved (elementary, all T1(n))

With rows indexed by first symbol, E(a)=last symbol of row a:

1. **The last column is a permutation** (each symbol is last in exactly one row).
2. **No unordered symbol pair has both directed adjacencies in one row** (a symbol has only one successor slot).
3. **Reversal bijection.** The map {x,y} ↦ {row(x→y), row(y→x)} sends the C(n,2) unordered symbol pairs bijectively onto the C(n,2) unordered row pairs. Equivalently, any two distinct rows share exactly one unordered pair {x,y} whose two directed adjacencies are split between them, one arc per row.

## 3. Corrected missing-pair structure (all T2(n))

Let α₉(x) = number of occurrences of x in the penultimate column and α₁(x) = number in the second column (for general n, positions n−2 and 1). Then

outdeg_M(x) = α₉(x),   indeg_M(x) = α₁(x),   |M| = n,

and α₉, α₁ ≥ 0 with Σ_x α₉(x) = Σ_x α₁(x) = n. No lower bound α₉(x) ≥ 1 holds in general. This corrects the packet's §1. The reviewer's n=8 profiles (penult/second multiplicities not all 1) already displayed the general behavior; at n=11 the same freedom exists, and only the sums are forced.

## 4. Status

The reversal bijection (2.3) and the boundary-degree description of M (§3) remain candidate written necessary conditions, still unreviewed. Everything else in the packet is not to be cited. T2(11) remains OPEN. This erratum was written before any reviewer or parent finding; the counting error was found by the author while re-deriving the position structure.
