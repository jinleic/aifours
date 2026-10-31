# Shor completion: an all-order obstruction for a 55-tail border

Owner **MathShor-2**, math-5. Native clock of the finite controls: **Wed Oct 28 20:23:54 PDT 2026**.
**ALL-ORDER WRITTEN candidate, with bounded exact CRT/gcd controls; not an all-order completion/noncompletion result, formal proof, peer/family acceptance or novelty claim.**

## 1. The theorem

Let `k>=2`, `m=2^k`, and `n=165m`. There is **no** direct tiling `P+Q=Z_n` satisfying

    {0,3,8,11} subset P,      {0,1,7,13,14} subset Q,
    |P|=3m,                    |Q|=55.                          (1)

Therefore a finite UD factor-complete extension of the literal Shor code cannot have both order `n=165*2^k` and an actual b-run tail border of cardinality55. This is an infinite branch obstruction, NOT a claim that all extensions are impossible.

In particular it simultaneously excludes the border pairs `(P,Q)=(12,55),(24,55),(48,55),(96,55),...` at orders `660,1320,2640,5280,...`. The first three had previously received order-specific candidates; this proof does not rely on their finite searches. The general same-code border factorization and Sands gcd-difference disjointness criterion are prior classical results, independently reconstructed in the earlier packets; no priority claim is made for this new anchor deduction.

## 2. Uniform 2-power fibres and a forced head rectangle

Because Q has odd cardinality55, its mask cannot be divisible by any `Phi_2,Phi_4,...,Phi_m`: each would give an even value at1. The direct-tiling identity therefore puts every such factor in P. Their product is `1+X+...+X^(m-1)`, so P is uniform modulo m, with **exactly3 elements in every class**.

The old tail differences have gcd classes `{1,2,6,12}` with n. Sands disjointness makes each P-element individually avoid those classes against old heads `A={0,3,8,11}`. We claim that for ANY residue `r mod m` with `r==1 or2 mod4`, the only three allowed odd-part residues are

    x mod165 in {33,88,143},

or equivalently `x==3 mod5` and `x==0 mod11`, with the mod3 residue free. CRT makes exactly one element of `Z_n` for each such odd-part residue and fixed r. Since P needs three elements in that r-class, ALL of them are forced.

Proof of the claim, using only congruences:

* If `r==1 mod4`, compare x against3 and11. Both differences have 2-adic valuation1; avoiding gcd2 and6 forces EACH to be divisible by5 or11. Since their difference8 is divisible by neither5 nor11, the only possibilities are `(x mod5,x mod11)=(3,0)` or `(1,3)`. In the latter case, comparison against0 forces `x==0 mod3` to avoid gcd1, whereas comparison against8 forces `x==2 mod3`, impossible. The former case passes all four anchor checks, with mod3 unrestricted.
* If `r==2 mod4`, comparisons against0 and8 have valuation1. They similarly give `(x mod5,x mod11)=(0,8)` or `(3,0)`. In the former case comparisons against3 and11 force incompatible mod3 values0 and2. The latter passes all four checks with mod3 unrestricted.

Thus the displayed forced rectangle is an all-k statement, not extrapolation from finite sampling.

## 3. Six forced divisor classes and projection injectivity

The old heads give P-difference gcds3,5,11. The forced rectangle supplies three further gcd classes, for every k>=2:

* Choose a forced x with `x==1 mod m`, `x==143 mod165`. Then `gcd(x-8,n)=15`.
* Choose a forced x with `x==1 mod m`, `x==33 mod165`. Then `gcd(x-3,n)=30`.
* Choose forced x,y with `(x mod m,x mod165)=(1,33)` and `(y mod m,y mod165)=(2,88)`. Then `gcd(x-y,n)=55`.

Call these six classes `H={3,5,11,15,30,55}`. Their 2-adic valuations are at most1, so if a difference has gcd in H modulo660, it has the SAME gcd with n.

There is one further consequence of the forced rectangle. For each `a=2,...,k-1`, take the forced heads with r-residues `1` and `1+2^a` modulo m and the SAME odd-part residue33 modulo165. Their difference has gcd exactly `165*2^a` with n. Therefore Q cannot contain two residues congruent modulo660: any distinct such pair would have gcd `165*2^a` for some `2<=a<k`. For k=2, n=660 and injectivity is immediate. Thus reducing Q modulo660 gives a SET of exactly55 distinct residues, still containing Y.

## 4. Four possible projected tails versus five required

Because |P|=3m is coprime to11 and |Q|=55, the direct-tiling identity forces Q to be uniform modulo11: exactly5 elements in each class. Projection modulo660 is injective and preserves mod11, so the projected set also has5 elements in class7 modulo11.

But this projected set must individually avoid the six classes H against all old projected anchors Y. Direct exact integer enumeration among the60 residues of class7 modulo11 yields only

    {7,73,337,601}.

Four candidates cannot supply the required five. This proves the all-order theorem (1).

## 5. Exact controls and limits

`frontier-20261028-universal-55-tail-family-check.py`, SHA256 `9d129c91ca6da908a64c0ac0d53723a7e40e8768a142d9bb9eb72a8b6a42c34e` (24 LF, 1191 bytes), checks k=2,...,10: the complete forced-head rectangle, its required gcd witnesses, every projection-injectivity gcd and the exact four projected tail candidates. Those are finite controls only. Sections2–4 supply the written proof for ALL k>=2.

This result excludes just the named infinite family of border CARDINALITY branches. It does not rule out other borders at any of those orders, establish unrestricted Shor noncompletion, perform novelty screening or pass human/peer/formal/independent-family review. The original completion problem remains OPEN.

**END OF UNIVERSAL 55-TAIL BORDER OBSTRUCTION.**
