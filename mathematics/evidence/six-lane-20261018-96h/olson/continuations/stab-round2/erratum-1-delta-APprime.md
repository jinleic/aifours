# Erratum 1 to the delta package: corrected proof of Lemma AP' (proof-LS-caseI-smalldelta-v1.md); AP pointer for addendum 1

Owner OlsonSTABSuccessor.  Written after /bin/date 2026-10-19T05:58:20-0700, on the parent's instruction that the delta package read the corrected AP.
Applies to proof-LS-caseI-smalldelta-v1.md (2ad172a026ee64441f00fd228b8b402a0a5f2e0d85df04512c87f0e70e5a68b1) and proof-LS-caseII-v2-addendum-1.md
(c289db226c86ea7703af4a23c4a93dce543669cb911d36b5845e70aad2c98718); neither is edited.  Statements unchanged; no scope added.  Unreviewed.

## D1: Lemma AP' (statement unchanged), corrected proof
Let n >= 1, 3n + 2 < p, d := |x~| in [1, (p - 1)/2], I an arc of l <= 2n + 1 consecutive residues containing the n + 1 points
a + rho x (0 <= rho <= n).  The n distinct points with 1 <= rho <= n lie in I n (I + x), whose size is
max(0, l - d) + max(0, l - p + d).
(i) d >= l: l - d <= 0 and l - p + d <= 2d - p < 0, so the intersection is EMPTY: contradiction.
(ii) p - l < d < l: l - d < 2l - p and l - p + d < 2l - p, and if both are positive their sum is 2l - p; as 2l - p <= 4n + 2 - p < n,
the intersection has fewer than n points: contradiction.
(iii) Otherwise d <= p - l and d < l, so l - p + d <= 0 and n <= l - d: d <= l - n <= n + 1.
Lifting (induction): L = [alpha, alpha + l - 1] maps onto I, y_0 in L lifts a, y_rho := y_0 + rho x~.  If y_rho is in L then
y_(rho+1) is in [alpha - n - 1, alpha + 3n + 1] and its residue is in I, so y_(rho+1) is in L + mp; m >= 1 is impossible as
p > 3n + 1, and m <= -1 is impossible as l + n < p.  So y_n, y_0 are in L, n d <= l - 1 <= 2n, d <= 2: x in {1, -1, 2, -2}.  []
## D2: pointer
proof-LS-caseII-v2-addendum-1.md uses Steps 1-4 of proof-LS-caseII-v2.md, whose Step 1 cites Lemma AP: the corrected proof of
Lemma AP in erratum-2-prereq-consolidated.md R6 governs there.  proof-STAB-base-p1mod3-v1.md and proof-LSplus-e2-v1.md use neither
AP nor AP'.
