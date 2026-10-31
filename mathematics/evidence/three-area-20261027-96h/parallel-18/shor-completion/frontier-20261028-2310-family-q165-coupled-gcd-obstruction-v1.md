# Shor completion: coupled gcd obstruction for Q165 in the 2310 family

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 22:13:31 PDT 2026**. **HIGH-CONSEQUENCE UNREVIEWED CANDIDATE: WRITTEN mathematics plus exact finite integer domain checks.** Not an adopted theorem, formal verification, independent-model-family review, human review, or novelty clearance.

## 1. Exact claim and limits

For every integer `k>=0`, put `t=k+1` and `n=2310*2^k=2^t*3*5*7*11`. There is no direct tiling

    P direct-sum Q = Z_n,
    |P|=7*2^t,  |Q|=165,
    {0,3,8,11} subset P,  {0,1,7,13,14} subset Q.              (1)

Subject to the actual-word border theorem, this excludes the corresponding actual multi-b-border cardinality of any finite UD factor-complete extension of the literal Shor code. This claim does not exclude other Q sizes or solve the original problem. It depends on the named Łaba–Londner T2 import and the finite domain tables explicitly displayed below.

Combined **conditionally** with the earlier unreviewed odd-tail candidates `frontier-20261028-2310-family-odd-tail-joint-prime-obstruction-v1.md` (SHA256 `b61890594ce5233fd0050d5524a4318a29020aa0ed0d30bded1d37d976d0db80`) and `frontier-20261028-2310-family-odd-tail-three-residuals-v1.md` (SHA256 `fce25631427ffa6e6d128383ebe3afcd4c69abbd46e73a31bc372dbfe166c23b`), it would leave only odd `|Q|=55` in this order family. The separate Q55 candidate is **not imported or assumed accepted** here. All of those candidates require disjoint scientific review. Even-Q orders in this family and the original unrestricted finite-completion problem remain OPEN.

## 2. Sources and cyclic transversals

The actual-word border factorization for finite complete UD codes containing `b,a^n` is the Restivo–Salemi–Sportelli theorem as stated in Cordero, [arXiv:2301.13566v1, p. 3, Theorem 1.1](https://arxiv.org/pdf/2301.13566v1); the relevant borders consist of actual `a^i b^+` and `b^+ a^j` atoms. The present claim (1) is stated directly for an arbitrary cyclic tiling, with no one-b restriction.

We use Sands divisor exclusion: distinct P- and Q-differences cannot have the same gcd with n. The full statement appears in Łaba–Londner, [arXiv:2106.14042v3, p. 10, Theorem 2.5](https://arxiv.org/pdf/2106.14042v3). Old P differences use gcds 3,5,11, so Q may not; old Q differences use gcds 1 and 7, so P may not.

The only deep additional input is Łaba–Londner, [arXiv:2106.14042v3, p. 26, Corollary 6.2](https://arxiv.org/pdf/2106.14042v3): if at most two prime factors of a cyclic tiling period divide both factor cardinalities, both masks satisfy Coven–Meyerowitz T2. Here `|P|=7*2^t` and `|Q|=3*5*11=165` are coprime, so no prime divides both and the corollary applies. Each prime-power cyclotomic dividing one side's cardinality is owned by that side by the tiling identity and evaluation at1. T2 then puts every `Phi_d`, `d>1`, with `d` dividing that cardinality into that side's mask. Folding modulo its cardinality shows

    P is exactly one head in each class mod 7*2^t;
    Q is exactly one tail in each class mod 165.                (2)

In particular each mod-7 head class contains both parities, indeed every 2-adic residue. These properties are consequences of the stated import, not a claim about arbitrary tilings.

## 3. Exact old-anchor domain tables

Write old tails `Y={0,1,7,13,14}`. For each `r in Z_165`, denote the unique Q-tail by `x_r`; write its abstract state as `(E or O, v)`, where v=`x_r mod7`. If two tails have different parity, their difference is odd and its gcd with n is precisely the product of those among `3,5,7,11` at which their residues agree. Residues for 3,5,11 are determined by r; the residue for 7 is v. Thus all following domain comparisons are independent of t.

For a forbidden set F of **odd** gcds, form the old-anchor domain of r by retaining every `(parity,v)` that has no odd-difference gcd in F with any old tail. The following exact domains were checked by the explicit 14-state rule in §7. `E*` means all seven even states `(E,0),...,(E,6)`; `O1..6` means all six odd states with v=1,...,6.

    F={3,5,11}:
        r=2:  O0             r=3:  E6 or O0
        r=4:  O0             r=10: O0
        r=11: E1 or O0       r=12: O0

    F={3,5,11,105,231}:
        r=2: O0              r=11: E1 or O0     r=44: E*

    F={3,5,11,105,385}:
        r=2: O0              r=44: E*            r=55: O1..6

    F={3,5,11,231,385}:
        r=2: O0              r=4: O0             r=8: E6 or O0
        r=33: E6 or O1..6    r=69: E*.

No omitted state is possible under the displayed F; the table itself does not assume that any remaining state extends to a full Q.

## 4. Three fixed Q gcds and a coupled three-way condition

First use only F=`{3,5,11}`. Tail x3 cannot take E6: against x12=O0 its odd difference has gcd3. Therefore x3=O0. Similarly x11 cannot take E1: against x2=O0 its odd difference has gcd3; hence x11=O0. The table also gives x10=O0. Comparing each with old x0=0 shows Q uses all three odd gcds

    gcd(x3-0,n)=21,  gcd(x10-0,n)=35,  gcd(x11-0,n)=77.        (3)

Moreover Q must use **at least two** of `{105,231,385}`. If it avoided any two, the corresponding table leads to a contradiction:

* Avoid 105 and231. x2=O0 and x11 is E1 or O0. E1 versus x2 has gcd3, so x11=O0. x44 is even; versus x2 it must have v=0 to avoid gcd3. But then x44 versus x11 has gcd231, forbidden under the assumption.
* Avoid 105 and385. x2=O0; x44 must be even with v=0, again to avoid gcd3 versus x2. x55 is odd with nonzero v, so its difference with x44 has gcd11, forbidden.
* Avoid 231 and385. x2=x4=O0. x8 cannot be E6 because it would have gcd3 versus x2, so x8=O0. x33 cannot be E6 because it would have gcd5 versus x8, so it is odd with nonzero v. x69 is even and must have v=0 to avoid gcd5 versus x4. Its difference with x33 then has gcd3, forbidden.

All stated gcds use opposite-parity pairs. Therefore (3) is forced and at least two of `{105,231,385}` are Q-difference gcds.

## 5. Head structure and the two easy cases

By Sands, P avoids 7,21,35,77 by old Q and (3), and P can use at most one of `{105,231,385}` by §4. Each mod-7 P class has an even and an odd head. For any opposite-parity pair in the same mod-7 class, its gcd is one of

    7,21,35,77,105,231,385,1155,

because it is odd and divisible by7. The first four are forbidden. P cannot avoid all of `{105,231,385}`: otherwise an odd head in the mod-7 class of old head0 would have gcd1155 with 0, hence be 0 modulo 3,5,11; compared with even old head8 it differs at each of 3,5,7,11 and would have gcd1, also forbidden. Thus P uses **exactly one** of these three gcds. Call it h.

If only h can be used, every even/odd pair within a mod-7 head class has gcd h or1155. As every class has both parities, all heads in that class share the two odd-prime coordinates dividing h/7. We rule out h=105 and h=231 explicitly.

* **h=105=3*5*7.** In the class 0 mod7 containing old 0, every head is 0 mod3 and0 mod5. Choose an odd head u there. Since even old8 has residues `(2,3,8)` modulo `(3,5,11)`, u differs from 8 modulo3,5,7; avoiding gcd1 forces u mod11=8, so u has triple `(0,0,8)`. In class 4 mod7 containing old11, every head is `(2,1)` modulo `(3,5)`. Choose an even head v. Comparison with odd old3, whose triple is `(0,3,3)`, forces v mod11=3, so v has triple `(2,1,3)`. The odd difference u-v differs at 3,5,7,11 and has gcd1: contradiction.
* **h=231=3*7*11.** In class 1 mod7 containing old8, every head is 2 mod3 and8 mod11. An odd head u there must be 0 mod5 to avoid gcd1 versus even old0; its triple is `(2,0,8)`. In class 3 mod7 containing old3, every head is 0 mod3 and3 mod11. An even head v there must be 1 mod5 to avoid gcd1 versus odd old11; its triple is `(0,1,3)`. Again u-v is odd and differs at all four odd primes, giving forbidden gcd1.

## 6. The h=385 case: all pure two-powers forced

Now h=385=5*7*11, so P avoids105 and231. All heads in a fixed mod-7 class share mod5 and mod11.

* In the class 0 mod7 containing old0, these coordinates are `(0,0)`. Every odd head u there must be 2 mod3 to avoid gcd1 against even old8; hence its `(mod3,mod5,mod11)` triple is `(2,0,0)`.
* In the class 1 mod7 containing old8, these coordinates are `(3,8)`. Every odd head v there must be 0 mod3 to avoid gcd1 against even old0; hence its triple is `(0,3,8)`.

Any such u,v differ modulo **all** of 3,5,7,11. By (2), each of those two mod-7 classes contains a head in every odd residue mod `2^t`. For each `j=1,...,t`, choose odd residues whose difference has 2-adic gcd valuation exactly j: use residues `1` and `1+2^j` if `j<t`, and the same residue if `j=t`. Their difference gcd is exactly `2^j`. Therefore P uses every one of

    2,4,...,2^t.                                                (4)

By Sands Q must avoid every pure two-power in (4). Consider the required tail x2 in class 2 mod165.

* If x2 is even, compare it with even old0. Its mod-165 label 2 differs from 0 modulo 3,5,11. Avoiding a pure 2-power gcd requires `x2=0 mod7`. But then its odd difference with old13 is divisible by 11 and by none of 3,5,7, so has forbidden gcd11.
* If x2 is odd, compare it with even old14. Their mod-165 difference is -12, divisible by3 and by neither5 nor11. To avoid forbidden gcd3, x2 must be 0 mod7, the same as14. But then its even difference with odd old1 differs at all of 3,5,7,11, so has a pure two-power gcd, contradicting (4).

This excludes h=385 as well and completes the conditional Q165 contradiction. It applies for `t=1` too: then the only pure power forced in (4) is 2.

## 7. Exact checks, control, and review boundary

The four domain tables in §3 were computed in the owner's persistent Python eval kernel by enumerating e=0,1 and v=0,...,6, using integer modular equality only. The following is a complete specification of the check; e=0 means E and e=1 means O:

```python
Y = (0,1,7,13,14)
def domain(r, F):
    out = set()
    for e in (0,1):
        for v in range(7):
            ok = True
            for y in Y:
                if e == y % 2:
                    continue  # the actual difference is even
                g = 1
                for p in (3,5,7,11):
                    equal = ((v-y) % 7 == 0) if p == 7 else ((r-y) % p == 0)
                    if equal:
                        g *= p
                if g in F:
                    ok = False
                    break
            if ok:
                out.add((e,v))
    return out
```

The kernel reported exactly the domains shown in §3. It also checked the cited domain-conflict pairs, and the odd-gcd sets with `math.gcd` on finite representatives; the proof for arbitrary t is the written prime/parity argument, not extrapolation from a list of k values. No native solver or background scientific job was run. The three pairwise Q-exclusion implications are written in §4 and do not rely on an unreported SAT search.

**Positive Q-only control, demonstrating the need for the coupled pure-power argument.** At n=18480 (`t=4`), select one residue for each `r=0,...,164` by the following CRT recipe. Give it mod-7 value v and mod-16 value w as follows:

* `(w,v)=(0,0)` for `r in {0,17,56,68,69,72,110,111,123}`;
* `(w,v)=(1,1)` for `r in {1,55,124,127}`;
* `(w,v)=(7,0)` for r=7, `(13,6)` for r=13, and `(14,0)` for r=14;
* `(w,v)=(1,0)` for every remaining r.

For each r take the unique x modulo 18480 satisfying `x=r mod165`, `x=v mod7`, `x=w mod16`. The kernel checked 165 distinct residues, all five old Y, and **no pair gcd in `{2,3,5,8,11,385}`**. This tail-only relaxation is SAT: Q need not use 2 or385 in isolation. It does use 105 and231 and also uses pure powers4 and16; the coupling in §§5–6 rules out a compatible P. The control is not a factorization or code completion.

Review must verify the named T2 and Sands hypotheses, all actual-border quantifiers if used for code D, every finite domain and conflict table, the three-way pigeonhole, the all-2-power head construction, and the separate positive control. Until then (1) is unreviewed. No conclusion about even Q, Q55, other order families, or the unrestricted original problem is asserted.

**END OF Q165 COUPLED-GCD CANDIDATE.**
