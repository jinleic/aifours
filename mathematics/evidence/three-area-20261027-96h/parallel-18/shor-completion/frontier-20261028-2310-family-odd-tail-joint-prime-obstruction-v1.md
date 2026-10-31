# Shor completion: joint-prime and matching obstructions for odd tails in the 2310 family

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 21:57:31 PDT 2026**. **UNREVIEWED WRITTEN candidate, with exact finite integer checks in the owner's eval kernel.** No unrestricted noncompletion, unconditional order exclusion, formal proof, independent-family review, peer acceptance or novelty claim is made.

## 1. Exact conditional statement

Let `k>=0`, `n=2310*2^k`, and let `P,Q` be the SAME actual multi-b-atom border factors of a hypothetical finite uniquely decipherable, factor-complete extension of the literal Shor code

    b{1,a,a^7,a^13,a^14}
      union {a^3,a^8}b{1,a^2,a^4,a^6}
      union a^11 b{1,a,a^2},

with actual pure-a atom `a^n`. Thus `A={0,3,8,11} subset P` and `Y={0,1,7,13,14} subset Q`. If `|Q|` is odd, the necessary conclusion is

    |Q| in {55,105,165,231,385}.                              (1)

These are necessary cardinalities only, and none is asserted feasible. The separate unreviewed all-k Q55 obstruction is **not used** here, so 55 is explicitly retained. Even Q, other orders, and the original finite-completion problem remain OPEN. The conclusion depends on the explicitly named Łaba–Londner T2 import and the stated finite matching certificates.

The actual-border theorem gives `P direct-sum Q=Z_n`, `|P||Q|=n`, using all actual words `a^i b^+` and `b^+ a^j`, not just one-b atoms; see Restivo–Salemi–Sportelli as stated in Cordero, [arXiv:2301.13566v1, p. 3, Theorem 1.1](https://arxiv.org/pdf/2301.13566v1). It also follows directly from the long guards `b^L a^g b^L` and UD: coverage is the terminal b-run atom, copies of the unique pure-a atom, and the initial b-run atom; directness follows by padding two equal-residue border representations to the same `b^H a^G b^K` actual word. Pure-a existence follows by embedding a sufficiently long a-run and uniqueness by UD. The theorem is a prior import; the reduction here is conditional on its hypotheses.

## 2. Coprime size and the named T2 import

Because `n=2^(k+1)*3*5*7*11`, the odd primes occur to the first power. If q=`|Q|` is odd, then `|P|` contains the entire two-power and every odd prime is allocated to just one size. Consequently `gcd(|P|,|Q|)=1`.

We invoke Łaba–Londner, *Combinatorial and harmonic-analytic methods for integer tilings*, [arXiv:2106.14042v3, p. 26, Corollary 6.2](https://arxiv.org/pdf/2106.14042v3): in a cyclic tiling `U direct-sum V=Z_M`, if after ordering the prime divisors of M, every prime except possibly the first two divides at most one of `|U|,|V|`, then both masks satisfy Coven–Meyerowitz T2. In the present case **no** prime divides both sizes, so its hypothesis holds. T2 means that if prime-power cyclotomic factors belonging to pairwise distinct primes divide a tile mask, the cyclotomic factor of their product divides it.

For every prime power dividing `|P|`, the corresponding cyclotomic factor divides P, because the cyclic tiling identity forces it into P or Q and its value at 1 is a prime which does not divide `|Q|`. T2 thus gives **every** `Phi_d`, `d>1`, with `d | |P|`. Their product is `1+X+...+X^(|P|-1)`, so the P-mask folded modulo `|P|` has one head in each residue. The identical argument makes Q a transversal modulo q. More generally, if two different primes divide `|P|`, P is uniform modulo their product. This is a necessary consequence of the named import, not a general assertion about arbitrary cyclic tilings.

## 3. Three missing joint-prime residue classes

At all k, the old-tail difference gcd classes include 1 and 7. Sands divisor exclusion says that a P-difference gcd cannot also occur among the Q-difference gcds. This classical statement appears as [Łaba–Londner, arXiv:2106.14042v3, p. 10, Theorem 2.5](https://arxiv.org/pdf/2106.14042v3). Therefore if a putative P-head x is individually compatible with all of A, then for each old head a at which `x-a` is odd, its difference cannot have gcd 1 or 7 with n. Since the odd prime factors of n are 3,5,7,11, such a difference must be divisible by at least one of 3,5,11.

For odd x, compare the even old heads 0,8; for even x, compare the odd old heads 3,11. These comparisons prove that the individual head screen has none of the following residues:

* `x=4 mod 15`. The two opposite-parity comparisons are divisible by neither 3 nor 5. Both would have to be divisible by 11, but the two compared heads are different modulo 11.
* `x=1 mod 33`. Both comparisons are divisible by neither 3 nor 11. Both would have to be divisible by 5, but the compared heads are different modulo 5.
* `x=2 mod 55`. Both comparisons are divisible by neither 5 nor 11. Both would have to be divisible by 3, but the compared heads are different modulo 3.

The relevant old-head pairs have residues `(0,8)` or `(3,0)` modulo 11, `(0,3)` or `(3,1)` modulo 5, and `(0,2)` in both cases modulo 3, respectively. Hence T2 uniformity makes it impossible for P to contain any two of the three prime factors 3,5,11. Equivalently, **at least two of 3,5,11 divide q**.

Since q is an odd divisor of 1155, the complete remaining list at this point is

    q in {15,33,55,105,165,231,385,1155}.                     (2)

This is a written all-k argument, not an extrapolation from tested orders. It eliminates, in particular, every q coprime to 3,5,11 and does not invoke the Q55 result.

## 4. Excluding q=1155 for every k

By §2 Q is a transversal modulo q. If `q=1155`, it must contain x congruent to 2 modulo 1155. This is impossible by the old Q anchors and the old P differences of gcd 3 and 5:

* If x is even, `x-7` is odd, divisible by 5 and divisible by none of 3,7,11, so `gcd(x-7,n)=5`. But 7 is in Q and 5 is a P-difference gcd, from old heads 8 and 3.
* If x is odd, `x-14` is odd, divisible by 3 and divisible by none of 5,7,11, so `gcd(x-14,n)=3`. But 14 is in Q and 3 is a P-difference gcd, from old heads 3 and 0.

This contradiction is independent of k and of all other Q entries.

## 5. Excluding q=15 and q=33 by two lifted matchings

These branches are written out as finite certificates plus an all-k lifting argument. For `n=2310*2^k`, define

    G_k = {gcd(y-y',n): distinct y,y' in Y},
    C_k = {x in [0,n): for each a in A,
                        x=a or gcd(x-a,n) not in G_k}.

The exact sets are `G_0={1,6,7,14}` and `G_k={1,6,7,12,14}` for `k>=1`. No two distinct P-heads can have a difference gcd in `G_k`.

For q=33, P has `|P|=70*2^k` and is uniform mod 5 with `14*2^k` heads in each residue class. Use screened head classes 2 and 4 modulo 5. For q=15, P has `|P|=154*2^k` and is uniform mod 11 with `14*2^k` heads in each class. Use screened head classes 1 and 6 modulo 11. The endpoint screens and the pair certificates below are exact finite arithmetic; no head outside the stated screen can belong to P.

| k | candidates in EACH relevant class | required in EACH class | disjoint conflicting cross-pairs |
|---:|---:|---:|---:|
| 0 | 14 | 14 | 2 |
| 1 | 30 | 28 | 6 |
| 2 | 72 | 56 | 34 |

Every row contradicts its two quotas: the total quota is greater than `2*candidates - number_of_pairs`. The first two rows' certificates are

    q=33, k=0: (2192,129), (1977,344)
    q=33, k=1: (1067,129), (4287,344), (2192,2439),
                (792,2654), (4502,3564), (1977,3839)
    q=15, k=0: (1145,336), (1596,2195)
    q=15, k=1: (3455,336), (1145,963), (3906,1568),
                (1596,2195), (2828,2646), (2223,4505).

The 34 disjoint pairs for q=33 at n=9240 are

    (5687,129),(7587,209),(8907,344),(1397,459),(6152,594),
    (4422,1664),(2717,1779),(7472,1914),(792,2654),(987,2849),
    (1122,2984),(4037,3099),(8792,3234),(9122,3564),(1977,3839),
    (2307,4169),(2442,4304),(737,4419),(872,4554),(1067,4749),
    (4287,4964),(3627,5489),(3762,5624),(2057,5739),(4947,6809),
    (462,6944),(3512,7194),(5412,7274),(6267,8129),(4502,8184),
    (1782,8264),(77,8379),(6597,8459),(4832,8514).

The 34 disjoint pairs for q=15 at n=9240 are

    (8075,336),(7536,578),(5435,633),(3213,875),(5765,963),
    (8526,1568),(1838,1656),(8856,1898),(6755,1953),(7448,2646),
    (3158,2976),(936,3218),(1233,3515),(4478,4296),(2223,4505),
    (2256,4538),(155,4593),(2553,4835),(3455,4956),(1145,5583),
    (1178,5616),(3576,5858),(1475,5913),(3873,6155),(3906,6188),
    (2498,6936),(4896,7178),(2795,7233),(2828,7266),(573,7475),
    (3818,8256),(4115,8553),(1893,8795),(6843,9125).

In each list the first endpoint is in the first named residue class, the second in the second class, all 68 endpoints are distinct, all endpoints lie in `C_2`, and every pair difference has gcd in `G_2`. The lists need not be maximum matchings.

**All-k lift.** For k>=2 put `M=2^(k-2)` and write each residue uniquely as `x_0+9240*t`, `0<=x_0<9240`, `0<=t<M`. In the two selected pairs of head classes no old head A lies in either class. Since `9240` contains all odd prime factors of n and is divisible by 8, a difference from an old head is in `{1,6,7,12,14}` exactly when the corresponding base difference is: the membership decision depends only on the odd factors 3,5,7,11 and on two-adic valuations 0,1,2, all unchanged by adding a multiple of 9240. Hence each of the four screen classes contains exactly `72M` candidates.

Lift every one of the 34 pairs by adding the same `9240*t` to both endpoints. The pair difference is unchanged and its gcd remains in `G_k`; all `34M` lifted pairs have distinct endpoints. Thus the two selected head classes permit at most `144M-34M=110M` elements in total, while their required total is `2*14*2^k=112M`. This excludes q=15 and q=33 for all k>=2; the table handles k=0,1.

Combining §§3–5 proves (1), subject to the named T2 theorem, written reductions, and the finite pair checks. It does not rely on the earlier Q55 family candidate.

## 6. Actual finite checks, failed intermediate, and limits

In the owner's persistent Python eval kernel, integer `math.gcd`, sets, and exact finite loops were used. For each k=0,1,2,3,4 the kernel reconstructed all of `C_k` directly from A,Y,n, confirmed the complete `G_k`, and counted both mod-5 classes 2/4 and both mod-11 classes 1/6. Their common counts were respectively `14,30,72,144,288`. For the displayed k=0,1 and k=2 matching certificates, exact integer checks tested class membership, every old-anchor screen comparison, all pair gcds, and distinct endpoints; separate in-kernel augmenting-path enumeration also obtained matchings of sizes `2,6,36` at k=0,1,2. The two displayed 34-pair subcertificates were independently checked after explicitly rebinding n=9240 and the correct head screen. All-k propagation is the written congruence/gcd argument above, not a finite-sample extrapolation.

During exploratory offset compression, a mutable kernel-global `n,C` had been overwritten by an unrelated preceding calculation. The first offset output `525/158` therefore used the wrong universe and was discarded; it is NOT evidence. The variables were rebound explicitly to n=9240 and its head screen before the displayed 34-pair checks. No standalone checker or independent reviewer has yet been run for this packet.

The separate Q55 all-order candidate remains UNREVIEWED and is not imported. Therefore q=55 remains in (1); no odd-tail existence or unrestricted completion/noncompletion claim follows. Further adoption requires independent written review of the imported theorem's hypotheses, cyclic actual-border/screen reductions, every finite certificate, and the lift.

**END OF ORDER-2310-FAMILY ODD-TAIL JOINT-PRIME OBSTRUCTION.**
