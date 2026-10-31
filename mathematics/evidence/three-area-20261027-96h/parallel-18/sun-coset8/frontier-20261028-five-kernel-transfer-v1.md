# Sun8 transfers from quotient through a normal five-index-power kernel

**NEW WRITTEN CANDIDATE, not reviewed/adopted/formally verified or novelty-cleared.** Actual native prewrite clock **Wed Oct 28 17:18:13 PDT 2026**. The theorem is conditional on explicitly stated group properties and applies to non-solvable quotients.

## 1. Exact statement

`Sun_k(X)` means every k pairwise-disjoint ACTUAL LEFT cosets of finite-index subgroups of X have a pair whose subgroup indices have gcd at least k.

**Theorem.** For ANY group G and normal subgroup N, assume

1. every finite-index subgroup of N has index a power of5, including1;
2. `Sun_8(N)` and `Sun_8(G/N)`;
3. `Sun_7(G)`.

Then `Sun_8(G)`. The hypotheses include ANY finite normal5-group; no finiteness, splitting, solvability, nonnormal-subgroup exclusion, or coset-cover condition is placed on G or G/N.

For a group N with this index spectrum, `Sun_7(N)` is SUFFICIENT for `Sun_8(N)`: in any eight actual disjoint cosets apply Sun7 to seven. Its pair index gcd is a power of5 at least7, hence at least25>=8. Therefore the previously licensed arbitrary-group Sun7 statement, if admitted, supplies both Sun7(G) and the kernel Sun8(N); the quotient Sun8 remains explicitly required. The Sun7 theorem is not proved or primary-source-authenticated here.

## 2. Actual quotient/fibre dichotomy

Suppose eight pairwise-disjoint actual G-cosets `g_i U_i` have finite indices n_i and all pair gcds<=7. Put Q=G/N, pi:G->Q and

    a_i=[Q:pi(U_i)],  b_i=[N:N∩U_i],  n_i=a_i b_i,
    C_i=pi(g_i)pi(U_i).

The index identity follows from `[G:U_i]=[G:NU_i][NU_i:U_i]` and `NU_i/U_i ≅ N/(N∩U_i)`. Each b_i is a power of5. Two overlapping actual C_i,C_j induce two nonempty disjoint actual N-cosets in a common fibre, of indices b_i,b_j. Their gcd is at least2: two cosets of coprime finite indices always meet, by the injective diagonal coset map whose domain index is divisible by and bounded by the product of the coprime indices.

Let I={i:b_i>1} and r=|I|. If i,j∈I are distinct, 5 divides both n_i,n_j, so their gcd, positive and at most7, is EXACTLY5. It follows that `gcd(n_i/5,n_j/5)=1` and, in particular,

    gcd(a_i,a_j)=1 for distinct i,j∈I.                          (2.1)

An outside label j∉I has b_j=1, so its nonempty N-fibre is the whole N. Actual disjointness forces its quotient coset C_j to be disjoint from EVERY other quotient coset. Hence for every i∈I,

    gcd(a_i,a_j)>=2,  and this gcd<=7.                           (2.2)

If r<=1, all eight quotient cosets are pairwise disjoint and `Sun_8(Q)` contradicts the counterconfiguration. If r=8, the a_i are pairwise coprime, so the diagonal coset map in Q proves a common quotient point; the eight actual N-fibres contradict the EXPLICIT `Sun_8(N)` premise. Thus assume 2<=r<=7.

`Sun_7(G)` applied to every seven-subfamily forces at least THREE original n_i divisible by7: the guaranteed pair has gcd exactly7, and if at most two labels carried7 one could omit one and obtain a seven-subfamily with at most one.

## 3. Two seven-divisible outside labels not divisible by5

Since b_i is a power of5, 7|n_i iff 7|a_i. By (2.1), at most ONE cluster label i∈I has 7|a_i.

If one such cluster label exists, its original index is divisible by35, so no seven-divisible outside original index can also be divisible by5: their gcd would be at least35. The three-label count then gives at least TWO outside seven indices, both prime to5.

If no cluster label carries7, there are at least THREE seven-divisible outside indices. Any two have gcd exactly7 under the counterconfiguration bound; at most one can also be divisible by5. Again there are at least TWO outside seven indices, both prime to5.

Choose two such actual outside labels J,K. Then

    7|a_J,a_K,     5∤a_J,a_K,     gcd(a_J,a_K)=7.                (3.1)

Their quotient cosets are disjoint from every cluster quotient coset and each other, by the actual b=1 fibre observation.

## 4. Cluster indices forced to 7 and 6

For any cluster i whose a_i is NOT divisible by7, its quotient coset is disjoint from both C_J and C_K. Thus both gcd(a_i,a_J),gcd(a_i,a_K) are nontrivial and <=7. The only possible common primes are2 or3: the two outside indices are prime to5 and a_i is prime to7. Since gcd(a_J,a_K)=7, they cannot share2 or3, so the two nontrivial intersections must use DIFFERENT primes. Consequently

    6|a_i for each cluster i with 7∤a_i.                        (4.1)

By pairwise coprimality of cluster a_i, there can be at most one such non-seven cluster label, and at most one seven-divisible cluster label. Since r>=2, necessarily r=2. Name the seven-divisible cluster A and the other cluster B. Then

    7|a_A,   6|a_B,   gcd(a_A,a_B)=1.                           (4.2)

After exchanging J,K if necessary, their shared primes with B are

    2|a_J,   3|a_K,   3∤a_J,   2∤a_K.                          (4.3)

The last two exclusions follow from gcd(a_J,a_K)=7. Both remain prime to5.

## 5. Remaining outside labels give a contradiction

There are six outside labels. No third outside label T can have 7|a_T. Indeed `35|n_A`, so 5∤a_T; and its gcd with a_J and a_K must be exactly7, so 2∤a_T and 3∤a_T by (4.3). But C_T is disjoint from C_B, whose index a_B is divisible by6 and is NOT divisible by7 because `7|a_A` and the cluster indices are coprime. Their nontrivial quotient-index gcd is at most7, so it would require a common prime among2,3,5,7. T has none of2,3,5 and B has no7. Contradiction. Thus exactly J,K among the outside labels carry7.

Choose any other outside label F. Its a_F is not divisible by7. Because C_F is disjoint from C_J and C_K, and each quotient-index gcd is nontrivial and <=7, (3.1) and (4.3) force `2|a_F` and `3|a_F`, respectively: J,K are prime to5, J has no3, and K has no2.

Also C_F is disjoint from C_A. Since a_A is coprime to a_B and `6|a_B`, a_A is prime to2 and3. Since `7∤a_F`, their nontrivial quotient gcd<=7 must contain5. Therefore `5|a_F`, and every outside label other than J,K has index divisible by30.

There are four such F labels; two have original indices n_F=a_F with gcd at least30, contradicting the pairwise <=7 bound. This completes all r cases and proves `Sun_8(G)`. □

All Q disjointness and gcd uses above are for the SAME ACTUAL quotient cosets projected from the original G configuration. No independent fibre packing, split extension, or quotient-index-product flattening is assumed.

## 6. Conditional structural consequence

Assume the previously licensed arbitrary-group Sun7 statement. Then the spectrum assumption supplies Sun8(N) as in Section1, so any normal finite5-group kernel with Sun8 quotient transfers Sun8 to G. If a finite minimum-order counterexample exists, it has no nontrivial normal5-group: the quotient by such a kernel is smaller and has Sun8 by minimality.

Combine this conditional consequence with the separately pinned seven-kernel transfer `frontier-20261028-seven-kernel-transfer-v1.md`, SHA256 `676627da3c52ba07169c225ebb1373ec4fb48a5691009e2ad399599992a765c0`, and the dual pair-gap transfer for primes>=11, `frontier-20261028-dual-k-fibre-transfer-v1.md`, SHA256 `1c4631d57fb6c118d1d1859f9cfb33fae521433a65cfea74e4a2f41de14d1b67`. Subject to full review of EACH, every nontrivial normal p-subgroup of a minimum finite counterexample has p=2 or3. Thus the prime divisors of its Fitting subgroup are contained in {2,3}. This is a structural restriction on a hypothetical finite minimal counterexample, NOT a proof it is simple, a classification, or unrestricted Sun8.

## 7. Exact bounded support overapproximation

Executed `/opt/homebrew/bin/python3 frontier-20261028-five-kernel-support-check.py`, deadline20 seconds, source SHA256 `54b56ff2d80d7d1106c1505ab1b4d745f0876f6c8fb5bbf7002e464a372a78dd`. Actual output:

```text
cluster_size=2: cluster_support_sets=25; terminal_models=0
cluster_size=3: cluster_support_sets=10; terminal_models=0
cluster_size=4: cluster_support_sets=1; terminal_models=0
cluster_size=5: cluster_support_sets=0; terminal_models=0
cluster_size=6: cluster_support_sets=0; terminal_models=0
cluster_size=7: cluster_support_sets=0; terminal_models=0
PASS: no abstract models for cluster sizes 2..7
Wed Oct 28 17:17:56 PDT 2026
```

The checker enumerates squarefree quotient-index supports on2,3,5,7. For cluster labels it uses projected originals `5*a_i`; every such projection divides the true `n_i`, so the gcd upper constraints are necessary. Every outside/cluster or outside/outside disjoint quotient-coset pair must have a shared prime <=7, which these signatures retain. Seven-divisibility is preserved because all kernel indices are powers5. Omitting larger primes/higher exponents overapproximates. The checker supports the finite incidence exclusion for r=2,...,7; it does not prove actual coset facts, Sun7, quotient Sun8, r=0/1/8, or general extension closure.

## 8. Exact remaining limits

No earlier held result is adopted as a premise or retrospectively validated; prior exposure is not claimed erased. Source-first priority, formal/kernel/human/independent-family review, proof of Sun7, unrestricted Sun8 and normal 2/3-kernel extensions remain open. Parent and reviewer must inspect the whole proof and dependencies before adoption.
