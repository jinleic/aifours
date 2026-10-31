# info-6 frontier: rank-two sparse-sign obstruction

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-28T23:20:30-0700**. **UNREVIEWED AUTHOR CANDIDATE**. It depends on the unreviewed collective-polar identity pinned below plus an explicit finite signed-relation-code classification, not on the quartic/orbit candidate or solver UNSAT. This is a branch-conditional necessary condition, not an unrestricted NL242 resolution, target witness, independent review, novelty claim, or formal verification.

## Statement

Under the original balanced nine-variable Boolean, `T≠0`, peak≤28 hypotheses, suppose the even-half polar has rank two. With the notation of the collective-polar candidate, `D=n₁+n₃` counts odd-half `|W/4|∈{1,3}`. Then

    z=64,    D∈{12,16,20,24,28},    114≤m≤122,
    Z≤40,    n₇≤184.                                             (1)

Here z is the even quadratic's zero count, Z is the number of actual Walsh zeros, m counts agreeing unordered T-pairs, and n₇ counts magnitude-28 Walsh coefficients. This is not a claim that any remaining D is realizable. The z=64, divisibility D≡0 mod4, m≤122, m≥108+D/2, and `Z+2D≤64` inputs are author-only results of the pinned collective-polar paper.

## Modulo-three support constraint

As in the predecessor, write the odd-half spectrum as

    k=k₀−8δ,  k₀=(-1)^Q(12h−7),  δ∈{−1,0,1},  wt(δ)=D,
    Walsh(k)=128v, v∈{−1,0,1}.

For a quadratic Q of polar rank two, the Walsh transform of `g=(-1)^Q` is supported on a four-point affine plane Y. Reducing `Walsh(k)=12Walsh(hg)−7Walsh(g)−8Walsh(δ)` modulo 3 yields

    Walsh(δ)(y)+v(y)≡Walsh(g)(y) (mod 3).                        (2)

Define `M=#{y∈F₂⁸:Walsh(δ)(y)≠0 mod 3}`. On the 252 indices outside Y, (2) and v∈{−1,0,1} say v(y) is nonzero exactly when Walsh(δ)(y) is nonzero mod3. As `wt(v)=256−m`,

    |M−(256−m)|≤4.                                                (3)

D is a multiple of four and at most 28. If D=0, M=0, so (3) forces m≥252, contradicting m≤122.

For D=4, four distinct signed atoms have affine rank 2 or 3. If rank 3, their character signs realize all 16 patterns equally often and M=160. If they are a rank-two affine plane, the product of the four signs is either +1 or −1: the possible character sums are respectively `−4,0,4` with M=64, or `−2,2` with M=256. In all three cases (3) is incompatible with `108+D/2≤m≤122`. Thus D≠4.

If D=8, the same m bounds give `112≤m≤122`, and (3) requires

    130≤M≤148.                                                    (4)

The finite classification in the next section shows this interval is impossible. Hence D≠8. Together with D≡0 mod4 and D≤28, this proves the D set in (1). Then `m≥108+D/2≥114`, `Z+2D≤64` gives Z≤40, and odd-half energy `64(256−m)≥256+48n₇` gives n₇≤184. ∎

## Complete eight-atom relation-code classification

Translate one atom to 0; translation multiplies the entire Walsh transform by a sign character and does not change M. Let r be the affine rank of the eight distinct support points. Then 3≤r≤7. The linear relations among their augmented `(1,x)` columns form a binary even-weight code R of dimension `7−r`; R has no word of weight 2 because the points are distinct. A choice of the eight ±1 signs is exactly a syndrome on R. For each such code/syndrome, count sign patterns with a sum nonzero modulo 3; each pattern occurs equally often up to global sign, which does not change nonzeroness.

* r=7: no relation; the 256 sign patterns give M=170.
* r=6: the sole nonzero even relation has weight 4, 6, or 8. The six possible M values are `116,152,164,176,188,224`.
* r=5: enumerate every two-dimensional even relation code whose nonzero words have weight≥4. There are 1,225 codes and four sign syndromes each. The possible M values are `104,128,152,176,200,224`.
* r=4: enumerate every three-dimensional such relation code. There are 1,605 codes and eight sign syndromes each. The possible M values are `80,128,176,224`.
* r=3: eight distinct points exhaust a three-dimensional affine space. Every sign pattern count is repeated 32 times across F₂⁸, so M is a multiple of 32.

None lies in [130,148]. The 74-LF checker constructs the relation codes directly as bit masks, checks their dimensions and minimum relation weight, counts all 256 sign patterns and all syndromes, and asserts the full frequency table in its 69-LF receipt. It also verifies an explicit rank-six eight-atom example with M=164. This finite check is an explicit part of the claimed argument; it is not a numerical SAT/UNSAT verdict and has not been independently reviewed.

## Intended-reason near miss and gap

The same checker supplies 12 distinct signed atoms whose Fourier transform has M=144. That falls inside the coarse interval in (4) and is compatible with the rank-two m-window at this **single modulo-three support-count level**. It is not placed into a common Walsh spectrum, does not establish any of the 511 full-spectrum correlations, and is not a Boolean function or target witness. It shows the relation-code argument is genuinely specific to D≤8 rather than a vacuous rejection of all sparse signed supports.

The excluded D values do not exclude the five remaining rank-two cases. Rank-four z=96, rank six, rank eight, actual construction and unrestricted exclusion remain unresolved; the finite enumeration and collective predecessor need disjoint review.

| File | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-eight-switch-code-check.py` | `4cd1aa5d7fceae85c06e14a7d6a719f243e3c6ee9371d149103e635288d043c5` | 74 | complete finite relation-code check |
| `frontier-20261028-eight-switch-code-check-result.json` | `50c78076cc01929aae157d8b1871590a1493a2f2f9aaf4a1e5b4486574ed1f9b` | 69 | finite receipt and D12 near miss |
| `frontier-20261028-collective-polar-exclusion-v1.md` | `e562e6074dec7beb4a713eed24c3044d6115965de0c60b5c9faf7827da86426d` | 108 | unreviewed collective predecessor |

**END.**
