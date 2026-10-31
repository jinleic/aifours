# Shor completion: three residual odd-tail obstructions in the 2310 family

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 22:07:06 PDT 2026**. **UNREVIEWED WRITTEN candidate with a finite exact-integer propagation check in the owner's eval kernel.** This is not a formal proof, independent-model-family review, accepted no-go, or novelty claim.

## 1. Scope and exact conclusions

For every integer `k>=0`, let `n=2310*2^k`. In any direct tiling `P direct-sum Q=Z_n` with same-factor anchors

    A={0,3,8,11} subset P,       Y={0,1,7,13,14} subset Q,

the following three cases are impossible:

    (|P|,|Q|) = (22*2^k,105), (10*2^k,231), (6*2^k,385).    (1)

This is a necessary-border statement and thus conditionally applies to actual multi-b borders of a finite UD factor-complete extension of the literal Shor code. It does not itself exclude other cardinalities, even Q, or the original problem.

Combining (1) with the **separate, still-unreviewed** joint-prime/matching candidate `frontier-20261028-2310-family-odd-tail-joint-prime-obstruction-v1.md`, SHA256 `b61890594ce5233fd0050d5524a4318a29020aa0ed0d30bded1d37d976d0db80`, would leave only

    |Q| in {55,165}                                             (2)

when Q is odd. This combination is conditional on both candidates surviving review. The separate Q55 exclusion is NOT imported here; 55 and 165 both remain open in (2). No claim is made that either is feasible. The unrestricted original question remains OPEN.

## 2. Classical imports and transversal reduction

The actual D-border theorem is Restivo–Salemi–Sportelli as stated in Cordero, [arXiv:2301.13566v1, p. 3, Theorem 1.1](https://arxiv.org/pdf/2301.13566v1). The necessary Sands divisor-exclusion criterion is stated in Łaba–Londner, [arXiv:2106.14042v3, p. 10, Theorem 2.5](https://arxiv.org/pdf/2106.14042v3): no nonzero P- and Q-differences may have the same gcd with n. The P-anchor differences already use gcds 3,5,11, so Q differences may not use those three.

All Q sizes in (1) are odd. Since `n=2^(k+1)*3*5*7*11` has each odd prime to exponent one, `gcd(|P|,|Q|)=1`. We invoke Łaba–Londner, [arXiv:2106.14042v3, p. 26, Corollary 6.2](https://arxiv.org/pdf/2106.14042v3): a cyclic tiling in which at most two primes divide both factor cardinalities has T2 for both factors. Here zero primes divide both. The tiling identity places each prime-power cyclotomic in the factor whose cardinality contains that prime, and T2 supplies all products of distinct such prime powers. Consequently each factor is a transversal modulo its own cardinality: after folding modulo `X^|P|-1` or `X^|Q|-1`, its mask is the all-ones polynomial. In particular Q contains exactly one residue in every class modulo q=`|Q|`. This is the sole deep extra import, not a general arbitrary-tiling claim.

All differences used in §§3–5 are between elements of the same Q or the same P. If two tails have opposite parity, their difference is odd; knowing equality or inequality modulo each of 3,5,7,11 then determines its gcd with n, independently of k. We use only the necessary bans gcd 3,5,11 for Q in the three small-domain arguments, deliberately ignoring all even-gcd bans until §5.

## 3. q=385: three forced tail residues

Here the only odd prime not dividing q is 3. By the transversal property choose unique tails `x_3,x_24,x_25` in the three residue classes `3,24,25 mod 385`. For each, retain only `(parity, residue mod 3)` possibilities that do not give a gcd 3,5,11 with any old tail in Y. Direct comparison gives the complete table

    residue mod 385       remaining (parity, mod 3)
          3                    (odd,2)
         24                    (odd,2)
         25                    (even,0), (even,2).

For example, at residue 3 an even tail of mod-3 value 1 conflicts with old tail 1 by gcd3, while either other even value conflicts with old tail13 by gcd5; an odd tail of value 0 conflicts with old0 by gcd3, and an odd tail of value1 conflicts with old14 by gcd11. The row 24 is analogous using old1,13,14. For residue25, odd values 1,2 conflict with old0 by gcd5, odd value0 conflicts with old14 by gcd11, and even value1 conflicts with old1 by gcd3.

If x25 is even and 0 mod3, its odd difference with x3 has gcd11: modulo 385 their difference is 22, divisible by 11 but neither 5 nor 7, and their mod-3 values differ. If x25 is even and 2 mod3, its odd difference with x24 has gcd3: their residue difference is 1 modulo 385 and their mod-3 values agree. Both are forbidden by A. Thus q=385 is impossible for every k.

## 4. q=231: four forced tail residues

Here the only odd prime missing from q is 5. Choose unique tails in classes 22,25,26,36 modulo 231. Their complete old-anchor-compatible `(parity, mod 5)` domains, considering only the odd gcd bans 3,5,11, are

    22 -> {(odd,0)}
    25 -> {(odd,4)}
    26 -> {(even,0),(even,4),(odd,4)}
    36 -> {(even,0),(even,1),(even,4)}.

These are elementary finite comparisons against Y; the exact domain-check recipe is in §6. The even-0 option at 26 conflicts with x22 by gcd5, while the even-4 option conflicts with x25 by gcd5; hence x26 must be odd and 4 modulo5. The even-0 and even-1 options at 36 both conflict with x25 by gcd11, leaving x36 even and 4 modulo5. But `36-26=10 mod 231` is divisible by none of 3,7,11, and their mod-5 values agree, so their odd difference has gcd5. Contradiction. Thus q=231 is impossible for every k.

## 5. q=105: incompatible forced gcd 2

Write `t=k+1`, so `n=2^t*3*5*7*11`, `|P|=11*2^t`, and `|Q|=105`. We show both factors must use gcd2, contrary to Sands.

### 5.1 P must use gcd2: written argument

Assume P avoids gcd2. P is a transversal modulo `11*2^t`, so it contains a head x satisfying

    x=1 mod 11,       x=1 mod 2^t.

It is odd. Compare it with even old heads0 and8. Their differences are odd. Because Q uses gcds 1 and 7 (from old tails), each such P-difference must be divisible by one of 3,5,11. Neither is divisible by 11. Since 0 and8 are different modulo both 3 and5, the only possible ordered pair `(x mod 3, x mod 5)` is `(0,3)` or `(2,0)`.

If it is `(0,3)`, then `x-11` is even and divisible by none of 3,5,11. If it is `(2,0)`, the same is true of `x-3`. In either case the two-adic gcd valuation is exactly 1 when `t>=2` because `x=1 mod4` and both 3,11 are 3 mod4; when `t=1` the gcd valuation is also exactly 1 because n has just one factor of2. The only remaining odd prime 7 may or may not divide the difference, so its gcd is either 2 or 14. Q already uses 14 from old tails0,14; under the assumption that P avoids2, both are forbidden. Contradiction. Thus P uses gcd2.

### 5.2 Q must use gcd2: finite projected-domain proof

Because Q is a transversal modulo 105, it contains a distinct tail `x_r` for each r in

    R=[0,1,5,7,10,11,13,14,16,71,72].

For each r, use the 22 possible abstract states `(e,v)`, where `e=x_r mod2` and `v=x_r mod11`; for r in `{0,1,7,13,14}`, pin the state to the corresponding actual old tail. Two states at different residues are incompatible if their parities differ and their difference has exactly one of 3,5,7,11 as a common odd prime divisor, namely 3,5, or11. The common-prime test for 3,5,7 uses the difference of the residue labels modulo 105; for 11 it uses the difference of v-values. Such an incompatibility is exactly an odd gcd in `{3,5,11}`, which Q cannot use because of A. No other Q restrictions are needed for this propagation.

Repeated exact arc-consistency removal on these eleven finite domains gives the following **complete fixed-point domains**, all singletons:

    r:        0     1     5     7    10    11    13    14    16    71    72
    (e,v):  (0,0) (1,1) (0,0) (1,7) (1,0) (0,1) (1,2) (0,3) (1,1) (0,1) (0,7)

The exact algorithm and reported checks are in §6. In particular x0, x71, x72 and x14 are even. For consecutive pairs `(0,71),(71,72),(72,14)`, their q-residue differences are nonzero modulo every one of 3,5,7, and their forced 11-residues are respectively `(0,1),(1,7),(7,3)`. Thus each difference has **no odd prime divisor in common with n**. If Q avoided gcd2, then for `t>=2` each consecutive even difference would be divisible by4; hence `x0=x71=x72=x14 mod4`. But old tails x0=0 and x14=14 differ modulo4. If `t=1`, even the first difference has gcd2 directly. In all cases Q uses gcd2, contradicting §5.1.

## 6. Reproducible finite checks and their exact limits

All finite checks were executed in the owner's persistent Python eval kernel, using only integers, `math.gcd`, sets and finite loops; no native solver or background scientific process was started. The exact arc rule for §5.2 is fully specified by this pseudocode:

```python
R = [0,1,5,7,10,11,13,14,16,71,72]
Y = [0,1,7,13,14]
D = {r: {(e,v) for e in (0,1) for v in range(11)} for r in R}
for y in Y:
    D[y] = {(y % 2, y % 11)}

def conflict(r, a, s, b):
    if a[0] == b[0]:
        return False
    shared = tuple(p for p in (3,5,7,11)
                   if ((a[1]-b[1]) % p == 0 if p == 11 else (r-s) % p == 0))
    return shared in ((3,), (5,), (11,))

changed = True
while changed:
    changed = False
    for r in R:
        for s in R:
            if r == s:
                continue
            keep = {a for a in D[r] if any(not conflict(r,a,s,b) for b in D[s])}
            if keep != D[r]:
                D[r] = keep
                changed = True
```

The actual kernel run reported `OPEN` with exactly the singleton domains in §5.2, not UNSAT; the gcd2 path is a separate written deduction. Each removal is sound: a value with no compatible value in another required tail's domain cannot occur in a global selection. Because there are finitely many values and only deletions, the propagation terminates. It is not asserted to decide general tiling satisfiability. The earlier full 105-residue relaxed propagation gave the same singleton assignments; the eleven-residue certificate deliberately ignores the other 94 variables.

The kernel separately enumerated each `(parity, missing-prime residue)` against all five old tails to obtain the tables in §§3–4; every common odd-prime set and every displayed contradiction pair is checked by exact modular arithmetic. These finite checks and the named classical imports remain subject to disjoint scientific review.

**Nonvacuity and boundary for q=165.** At n=9240, the following 56-element head-only set contains A, has one representative of each residue mod56, and avoids pairwise gcds `{1,2,6,7,12,14}`:

    [0,3,8,11,1793,1738,1573,1518,1353,1298,1133,1078,913,858,
     693,638,473,418,253,198,33,3058,2893,2838,2673,2618,2453,
     2398,2233,2178,2013,1958,396,63,68,183,128,243,132,303,248,
     363,88,483,428,543,264,603,548,663,608,275,143,668,308,671].

It is a positive head-only relaxation with gcd2 banned, not a border factor or a tiling. Separately, a 165-element Q-only relaxation at the same n is obtained for each r=0,...,164 as the unique solution of

    x=r mod165,
    x=(1 if r=1, 6 if r=13, otherwise 0) mod7,
    x=({0:0,1:1,7:7,13:5,14:6}.get(r,3)) mod8.

The kernel directly checked 165 distinct residues, all old Y, and pairwise avoidance of old head classes `{3,5,8,11}`. The two relaxations are not claimed mutually compatible: in fact this displayed head set's further forbidden gcds leave only 54 individually compatible tail candidates, and at least 116 mod-165 classes absent. Neither is a completion. They explain why no q=165 no-go is claimed here.

Odd Q=55 and 165, even Q, other orders, and the unrestricted original problem remain OPEN. No q=55 theorem, solver timeout, fibre conjecture, or prospective result has been silently adopted.

**END OF THREE RESIDUAL ODD-TAIL OBSTRUCTIONS.**
