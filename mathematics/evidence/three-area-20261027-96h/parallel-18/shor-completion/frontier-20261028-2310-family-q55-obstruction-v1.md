# Shor completion: a universal 55-tail obstruction in the 2310 family

Owner **MathShor-2**, math-5. Actual clock of the finite controls: **Wed Oct 28 21:01:30 PDT 2026**.
**ALL-ORDER WRITTEN candidate, with exact bounded CRT/graph controls. It is not an unrestricted original-problem solution, formal proof, peer/cross-family acceptance or novelty claim.**

## 1. Exact statement

For EVERY integer `k>=0`, there is no direct cyclic tiling with

    n=2310*2^k,       |P|=42*2^k,        |Q|=55,
    A={0,3,8,11} subset P,    Y={0,1,7,13,14} subset Q.      (1)

Consequently no finite UD factor-complete extension of the literal Shor code can realize this particular actual order/border-cardinality family. This is an infinite family of NECESSARY-border exclusions, not a claim that other border sizes or all orders are impossible.

The actual-word border factorization and Sands' gcd-difference disjointness criterion are prior classical mathematics independently reconstructed in earlier pinned packets. This proof does NOT use the pending odd-Q/165-cofactor classification or the earlier all-k 165-cofactor Q55 theorem.

## 2. A saturated head class

Set

    m=2^(k+1),       N=7m,       n=165N.

Q has size55, coprime to3, so the direct-tiling identity forces P uniform modulo3. Since `|P|=3N`, exactly N heads are `1 mod3`.

Let V be the old-anchor-compatible head candidates congruent1 modulo3. The gcd classes of old tail differences are `{1,6,7,14}` when k=0, and `{1,6,7,12,14}` when k>=1. Define

    Z={x mod n:x==88 mod165},
    T=V\Z.

We prove below that every independent N-element subset of V under those forbidden gcd classes is **exactly Z**. Therefore the actual P contains all N elements of Z.

## 3. Exact structure of the head screen

All Z-elements pass the anchor screen: their differences from old heads3,8 are divisible by5 and their differences from0,11 by11, so none has an old-tail forbidden gcd.

Conversely take `x in V`. Since `x==1 mod3`, its difference from EVERY old head is not divisible by3. If x is odd, comparisons against even heads0 and8 have odd difference; the forbidden gcds1 and7 force each difference to be divisible by5 or11. Since8 is divisible by neither, the only resulting odd-part residues are `x==85 or88 mod165`. If x is even, the analogous comparisons against odd heads3 and11 give `x==91 or88 mod165`. Thus T consists only of odd elements85 mod165 and even elements91 mod165.

For k=0, the remaining old-anchor comparisons give the exact extra restrictions

    x==85 mod165, x odd:   x mod7 not in {3,4};
    x==91 mod165, x even:  x mod7 not in {0,1}.

For k>=1 they give exactly

    x==85 mod165, x odd:   x==3 mod4 OR x mod7 not in {3,4};
    x==91 mod165, x even:  x==0 mod4 OR x mod7 not in {0,1}.  (2)

Indeed, for the same-parity old-anchor comparisons the odd part of the difference has no factor3,5,11. A forbidden gcd14 occurs precisely when the difference has 2-adic valuation1 and is divisible by7; valuation at least2 is harmless for those comparisons. At k=0 every even difference has gcd14 exactly when divisible by7. This proves (2) and its k=0 counterpart, not merely their bounded checks.

## 4. Strict expansion forces all of Z

Join `x in T` to `z in Z` when their difference has an old-tail forbidden gcd. Their difference is congruent `+3 or -3 mod165`, so it is divisible by3 but not5 or11. An edge occurs exactly when the difference is not divisible by7 and:

* for k=0, the two elements have the same parity;
* for k=1, their difference is even;
* for k>=2, its 2-adic valuation is1 or2.

By CRT, every x in T has exactly

    d_T = 6                 (k=0),
          12                (k=1),
          9m/4              (k>=2)

neighbors in Z. Conversely every z in Z has strictly fewer T-neighbors: at most5 for k=0, at most11 for k=1, and at most `17m/8` for k>=2. For the last bound, only one parity type (85 or91) can neighbor z. Of the `m/4` residues with valuation1 and `m/8` with valuation2, at least `m/8` fall in the mod4 class where (2) excludes two residues modulo7. After also excluding z's mod7 value, such a residue offers at most5 rather than6 choices; hence `6(m/4+m/8)-m/8=17m/8 < 9m/4`. For k=1 the same two mod4 possibilities contribute at most6+5=11; for k=0 at most5.

For any nonempty `U subset T`, counting edges between U and its Z-neighborhood shows

    |N_Z(U)| > |U|,

because each member of U has degree d_T while every Z-vertex has degree strictly less. An independent set using U can include at most `N-|N_Z(U)|` Z-vertices, so it has fewer than N elements. Hence the unique independent N-set in V is Z itself. The actual P's N mod3-class1 heads must be exactly Z.

## 5. Projection to 165 and the final five-tail contradiction

Since P contains every residue `88 mod165`, for every proper divisor `h|N` it contains two heads with difference gcd `165h`. Thus two distinct Q-elements cannot be congruent modulo165: their difference gcd with n would be one of those forced classes. Projection Q→Z_165 is injective and preserves the55 elements and old anchors.

For EVERY divisor `h|N`, CRT also lets us choose a forced `z==88 mod165` such that

    gcd(z-3,n)=5h,       and separately gcd(z-0,n)=11h.

Indeed `gcd(88-3,165)=5`, `gcd(88-0,165)=11`, and gcd(165,N)=1; prescribe `z-a==h mod N` (or0 when h=N). Each such z differs from its old head a. Consequently two projected Q-elements cannot have difference gcd5 or11 with165: every possible lift of either class is already a P-difference class.

Q is uniform modulo11 with5 elements per class because P is coprime to11. Among the15 residues `7 mod11` in Z_165, screening against projected old Y while avoiding gcd5 and11 leaves exactly

    {7,62,73,106,117}.

All five would have to be selected. But `gcd(62-73,165)=11`, forbidden. This contradiction proves (1) for every k>=0.

## 6. Bounded checks and limits

`frontier-20261028-2310-family-q55-check.py`, SHA256 `e5b5dcfba1cc6ff3159ffbb977b3a53c7f310e4016b0eda780f5fbf1299d6580` (36 LF, 1699 bytes), checks k=0,...,5 by exact integer enumeration: the complete head-screen characterization, every T-degree and maximum Z-degree, all CRT lift classes, and the five projected tails/final conflict. These are bounded controls only; §§3–5 are the written all-k argument.

This family covers the Q55 border at orders2310,4620,9240,..., but does not exclude other border cardinalities or all odd multiples of2310. General border and Sands criteria are named classical imports; this specific deduction has not been independently reviewed or novelty screened. The original unrestricted finite-completion problem remains OPEN.

**END OF UNIVERSAL 2310-FAMILY Q55 BORDER OBSTRUCTION.**
