# Sun8 transfers through an index-two normal extension, conditional on Sun7

**NEW WRITTEN CANDIDATE, not reviewed/adopted/formally proved/novelty-cleared.** Actual native prewrite clock **Wed Oct 28 17:04:34 PDT 2026**. This proof is independent of the optional finite support checker and explicitly exposes its Sun7 premise.

## 1. Exact theorem

For a group X, `Sun_k(X)` denotes the assertion: every k pairwise-disjoint ACTUAL LEFT cosets of finite-index subgroups of X have a pair whose subgroup indices have gcd at least k.

**Theorem.** For every group G and normal N with `[G:N]=2`, the conjunction `Sun_8(N)` and `Sun_7(G)` implies `Sun_8(G)`.

This includes infinite G and N, nonsplit extensions, nonnormal original subgroups, repeated index values and noncovering configurations. `Sun_8(N)` is an explicit kernel hypothesis; it is not inferred from Sun7. The theorem is a conditional mathematical statement with `Sun_7(G)` exposed, independent of whether the Sun7 statement is globally known.

**Corollary conditional on the previously licensed arbitrary-group Sun7 STATEMENT.** An index-two extension of any `Sun_8` group is `Sun_8`; the same follows for finite 2-group quotients by an elementary prime-order normal series. Section6 states a further finite-solvable-quotient consequence using the separately identified earlier p=3,5,7 and p>7 transfers. The global Sun7 statement is an IMPORT, not proved here; no universal Sun8 claim follows without all named premises.

## 2. Actual quotient fibres and necessary gcds

Assume eight actual pairwise-disjoint cosets `g_i U_i` of finite-index subgroups have original indices n_i with `gcd(n_i,n_j)<=7` for every distinct pair. Let `pi:G->G/N` and define

    b_i=[N:N∩U_i],   a_i=[G/N:pi(U_i)],   n_i=a_i b_i.

The index identity is the finite-index multiplication formula together with `NU_i/U_i ≅ N/(N∩U_i)` as coset sets. Since the quotient has order2, `a_i` is1 or2. Call labels with a_i=2 **proper-image**, so their actual quotient coset is one point; labels with a_i=1 are **full-image**, so their actual image coset is all of the quotient.

When two quotient-image cosets meet, choose a common quotient point and a representative t. Each original coset intersects tN in `t x_i(N∩U_i)` for some x_i in N; translated into N these are disjoint ACTUAL cosets with indices b_i. If their indices were coprime they would intersect: the diagonal map from N/(intersection) into the product of the two coset spaces is injective, while the intersection index is divisible by both coprime indices and bounded above by their product, so the map is bijective. Thus every pair with meeting quotient images satisfies

    gcd(b_i,b_j)>=2.                                            (2.1)

A full-image label meets every other label's image. If there were zero or one proper-image label, ALL eight images would share a quotient point, so the actual kernel premise `Sun_8(N)` would yield `gcd(b_i,b_j)>=8`, hence `gcd(n_i,n_j)>=8`. Therefore at least two labels are proper-image.

For any two proper-image labels i,j,

    gcd(n_i,n_j)=2 gcd(b_i,b_j)<=7,
    so gcd(b_i,b_j)<=3.                                         (2.2)

## 3. Seven-divisibility forced by Sun7

Apply `Sun_7(G)` to each seven-member subfamily of the eight actual disjoint cosets. The pair it supplies has gcd exactly7 under the counterconfiguration bound, so its two original indices are seven-divisible. There must be at least THREE seven-divisible original indices: otherwise one can omit one of at most two such labels and leave a seven-subfamily with at most one.

At most one proper-image label is seven-divisible, because two such original indices would both be divisible by14. Therefore at least two full-image original indices are seven-divisible. Any two such full indices have gcd exactly7. In particular at most one of them is even, and no prime besides7 divides two of them.

## 4. No proper-image label is seven-divisible

In this case at least three full-image labels have indices divisible by7. At most one is even, so choose two whose full indices V and W are odd. Their gcd is7.

Let A be ANY proper-image label. Since `7∤b_A` and its quotient point is met by both full images, (2.1) gives nontrivial common divisors `gcd(b_A,V)` and `gcd(b_A,W)`. Each is at most7 because b_A divides the corresponding original n_A. V and W are odd, b_A is not seven-divisible, and the only remaining possible shared primes at most7 are3 and5. Since `gcd(V,W)=7`, these two intersections use distinct primes: one forces3|b_A and the other forces5|b_A. Thus `15|b_A` for EVERY proper-image label A.

There are at least two proper-image labels, whose b gcd is then at least15, contradicting (2.2). This closes the case.

## 5. Exactly one proper-image label is seven-divisible

Let A denote that label. Because `14|n_A`, every full seven-divisible index is odd: an even such index would share14 with n_A. There are at least two; call them V and W, so `gcd(V,W)=7`.

There is at least one other proper-image label B; its b_B is not divisible by7. Its actual quotient fibre meets both full labels. Their nontrivial b_B intersections with V and W have prime divisors in `{3,5}` and must use DISTINCT primes because `gcd(V,W)=7`. After interchanging V and W,

    3|V,   5|W,   15|b_B.                                      (5.1)

For ANY additional proper-image label B', the identical argument gives `15|b_B'`, which would contradict (2.2) with B. Thus exactly A and B are proper-image and the remaining six labels are full-image. Choose any third full label F distinct from V,W.

If `7|n_F`, then n_F is odd by the first paragraph. It cannot be divisible by3 or5 because n_F and V (respectively W) would then share21 (respectively35), contradicting the <=7 bound. Yet its image meets B's, so (2.1) requires a shared prime at most7 with b_B. That prime cannot be2,3,5, or7: n_F is odd, not divisible by3/5, and `7∤b_B`. Contradiction. Hence `7∤n_F`.

The full-image cosets indexed by F and V meet in EVERY quotient fibre, so their actual kernel-index gcd is at least2. It is at most7 by the original bound. Since V is odd and `7∤n_F`, a common prime must be3 or5. But 5 cannot divide V because `5|W` and `gcd(V,W)=7`. Hence `3|n_F`. The same argument for F,W shows `5|n_F`, because 3 cannot divide W. Thus `15|n_F`.

But `15|b_B` from (5.1), so `15|n_B=2b_B` also. Their original gcd is at least15, a contradiction. The F,V,W,B fibre constraints refer to the SAME actual cosets, not separately chosen local constructions.

The two cases are exhaustive; the counterconfiguration cannot exist. Therefore `Sun_8(G)` holds. □

## 6. Conditional closure for finite solvable quotients

Combine the present written index-two theorem, the separately pinned index-three candidate `frontier-20261028-c3-normal-transfer-v1.md` SHA256 `5c9099385c75e451a60f8bebe1c133dc1da07285e504aa822799e91027e70668`, and the previously parent-supported v3 prime5/7 transfer and v2 `(R7)` transfer for primes greater than7. Each uses `Sun_8` of the ACTUAL normal kernel; prime2,3,5,7 additionally invoke the stated Sun7 property where used. The Sun7 universal statement is treated as a named external/imported statement, NOT independently proved in this packet.

**Conditional corollary.** Assuming the arbitrary-group Sun7 statement and those p>=5 transfers at their stated scopes, if N is normal in G, `Sun_8(N)`, and G/N is finite solvable, then `Sun_8(G)`.

For a finite solvable quotient Q, each factor of its derived series is finite abelian. A finite abelian group has a chain with prime-order factors: choose a nonidentity element, take a power of prime order, quotient by its cyclic subgroup, and induct on the order. Every intermediate subgroup is normal in the next because the ambient factor is abelian. Pull these chains back within the consecutive derived subgroups and concatenate. Pull the resulting normal series back from Q to G. At each prime-order extension apply the corresponding named theorem, starting from the actual N; induction yields the conclusion. This is NOT a claim that Q is nilpotent or that the prime factors act trivially.

Taking N trivial proves every finite solvable group satisfies Sun8 under these explicit imports: the trivial group has no eight pairwise-disjoint cosets, so its Sun8 assertion is vacuous. Any solvable group G, even infinite, also follows by the finite-core reduction: intersect the finite-index cores of the eight subgroups, project the configuration into the resulting finite solvable quotient while preserving indices and disjointness, and apply the finite case. Each core has finite index because the action on finitely many cosets has finite image. No unrestricted conclusion follows for nonsolvable finite quotients.

As an additional conditional constraint, a minimum-order finite counterexample (if any) must be perfect: if its abelianization were nontrivial, its commutator subgroup would be a smaller normal group and hence satisfy Sun8 by minimality, while its quotient would be finite solvable, contradicting the transfer. Perfectness is NOT simplicity and does not rule out a counterexample.

## 7. Bounded exact support experiment

Executed `/opt/homebrew/bin/python3 frontier-20261028-c2-support-obstruction-check.py` with a30-second command deadline. SHA256 **`11c373657b29e91bc3a9b670993d7308adbcdfb0c1733bb3f629fc6d7d327f3c`**. Actual output and clock:

```text
no_proper_seven: partial_counts=[1, 24, 243, 924, 132, 0]; terminal_models=0
one_proper_seven: partial_counts=[1, 24, 243, 249, 72, 0]; terminal_models=0
PASS: no abstract model for either C2 obstruction scenario
Wed Oct 28 17:04:09 PDT 2026
```

The 48 enumerated signatures retain primes2,3,5,7 to bounded exponent caps3,2,1,1 and divide the actual b indices. Every actual configuration with original pair gcd<=7 maps to a signature satisfying the checker's upper bounds; every nontrivial intersection gcd must have a common prime at most7 and is retained. The first case assumes two non-seven proper labels and three seven full labels; the second assumes one seven proper, one other proper, two seven full and one further full label. Both are necessary subconfigurations in their respective cases. Discarding private larger primes and higher powers overapproximates actual possibilities, so zero abstract models is a bounded necessary-constraint check, not an executable coset classification, a formal proof, a Sun7 verification, or evidence of novelty.

## 8. Limits and provenance

The all-variable actual-fibre proof above is new work after the explicit prospective research direction. Previous quarantined output is not accepted as a theorem or retroactively validated; prior exposure is not claimed erased. Exact source identity, independent-family/human/kernel verification and novelty remain open. The original arbitrary-group Sun8 target remains open at the finite nonsolvable/perfect interface; the kernel hypothesis, Sun7 import and previously supported transfers are not hidden. Parent/reviewer must inspect full bodies and imports before adoption.
