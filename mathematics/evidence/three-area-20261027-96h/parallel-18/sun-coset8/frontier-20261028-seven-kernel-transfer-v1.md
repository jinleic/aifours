# Sun8 transfers from quotient through a normal seven-index-power kernel

**NEW WRITTEN CANDIDATE, not reviewed/adopted/formally verified or novelty-cleared.** Actual native prewrite clock **Wed Oct 28 17:16:33 PDT 2026**. This is a quotient-to-group theorem with an explicit kernel index spectrum, including nonsolvable quotients. The proof uses `Sun_7(G)` as a named hypothesis; the universal Sun7 statement is a separate conditional import.

## 1. Theorem and scope

For any group X, `Sun_k(X)` means that every k pairwise-disjoint ACTUAL LEFT cosets of finite-index subgroups have a pair of subgroup indices with gcd at least k.

**Theorem.** Let G be ANY group and N normal in G. Assume

1. every finite-index subgroup of N has index a power of7 (including the power 7^0=1);
2. `Sun_8(G/N)`;
3. `Sun_7(G)`.

Then `Sun_8(G)`.

No finiteness, splitting, solvability or simple-quotient restriction is placed on G or G/N; original subgroups need not be normal and cosets need not cover. In particular the kernel hypothesis holds for every finite normal 7-group. The proof includes an independent elementary proof of `Sun_8(N)` from hypothesis1; it is not silently assumed. The universal Sun7 statement used to discharge hypothesis3 is the previously licensed statement-only import, not reproved or independently source-authenticated here.

This is not a general extension theorem for arbitrary normal kernels, and `Sun_8(G/N)` remains an explicit quotient premise. The named Sun7 import, full review and novelty are unpaid. No quarantined historical result is treated as a proved premise.

## 2. The seven-index spectrum itself gives Sun8(N)

Let H<=N have index7. Its left-coset action gives a homomorphism N->S7 with finite-index kernel core(H)⊂H. By hypothesis `[N:core(H)]` is a power of7, so the image is a finite 7-group. It acts transitively on seven points, and its order divides 7!, whose 7-adic valuation is1. Hence the image has order7. Since core(H)⊂H and both have index7, H=core(H) is normal.

If H,K are distinct normal index7 subgroups, HK is a subgroup containing H properly, hence HK=N because H has prime index7. Every left coset of H intersects every left coset of K: HK=N supplies a solution to the corresponding membership equation. Therefore any pair of DISJOINT index7 cosets must have the SAME index7 subgroup.

Suppose eight disjoint finite-index N-cosets have pairwise index gcd<=7. No index is1, since its coset is all N. Every index is a positive power of7; if two were divisible by49 their gcd would be at least49. Thus at least seven of the eight cosets have index exactly7. Their subgroups must all be identical, as just proved. Seven distinct cosets of that index7 subgroup exhaust N, so no eighth nonempty coset can be disjoint from them. Contradiction. Thus `Sun_8(N)` follows from hypothesis1 without any Sun7 or solvability theorem.

## 3. Actual quotient fibre setup

Suppose, toward contradiction, that eight actual disjoint G-cosets `g_i U_i` have finite indices n_i and `gcd(n_i,n_j)<=7` for all distinct i,j. Write Q=G/N, pi:G->Q,

    a_i=[Q:pi(U_i)],   b_i=[N:N∩U_i],   n_i=a_i b_i,
    C_i=pi(g_i)pi(U_i).

All a_i,b_i are finite and b_i is a power of7. The index product is the usual finite-index formula `NU_i/U_i ≅ N/(N∩U_i)`.

When two actual quotient cosets C_i,C_j meet, choose a common point and lift it to t∈G. Translating their actual disjoint fibres in tN into N produces two disjoint ACTUAL left cosets of N∩U_i and N∩U_j. Consequently `gcd(b_i,b_j)>=2`. Indeed coprime finite indices force two cosets to intersect: the diagonal map of the intersection-subgroup cosets into the product of coset spaces is injective, and the intersection index is a common multiple of the two coprime indices bounded above by their product, hence the map is onto.

Let I be the labels with b_i>1, r=|I|. For i∈I, 7|n_i. For distinct i,j∈I, the counterconfiguration bound forces `gcd(n_i,n_j)=7`, so after dividing each n by7,

    gcd(n_i/7,n_j/7)=1,  hence gcd(a_i,a_j)=1.                 (3.1)

If j∉I then b_j=1. Its translated N-fibre, wherever nonempty, is the WHOLE N, and thus cannot be disjoint from the nonempty fibre of any other actual coset. Therefore C_j is disjoint from EVERY other C_i. In particular, quotient cosets outside I are pairwise disjoint and disjoint from each cluster coset C_i, i∈I.

## 4. Low cluster sizes and the seven-divisibility count

If r<=1, any two quotient cosets meet only if their kernel indices have nontrivial gcd; at most one is nontrivial, so all eight C_i are pairwise disjoint. The explicit `Sun_8(Q)` hypothesis yields two quotient indices with gcd>=8, and those divide the corresponding original indices. This contradicts the counterconfiguration.

If r=8, the a_i are pairwise coprime by (3.1), so ALL eight prescribed quotient cosets have a common point. The diagonal map Q/(∩pi(U_i))->∏Q/pi(U_i) is injective; its domain index is divisible by the product of pairwise coprime a_i and at most that product, hence it is surjective. At the common quotient point the eight actual fibres are disjoint N-cosets, contradicting `Sun_8(N)` proved in Section2. This is a common point for the same actual original cosets, not an independently specified collection of fibres.

It remains to consider 2<=r<=7. First, `Sun_7(G)` forces at least THREE n_i to be divisible by7: apply it to every seven-member subfamily. Its guaranteed pair has gcd exactly7 under the counterconfiguration bound; if at most two labels carried7, omitting one would give a seven-subfamily with at most one such label.

Fix j outside I. Its quotient coset C_j is disjoint from EVERY C_i, i∈I, so the two-coset gcd fact applied in Q gives

    gcd(a_i,a_j)>=2 for EVERY i∈I.                              (4.1)

If 7|a_j, then 7|n_i and n_j=a_j, so `gcd(n_i,n_j)=7`. Since `a_i|n_i`, (4.1) forces `gcd(a_i,a_j)=7` and hence 7|a_i for EVERY i∈I. This contradicts the pairwise coprimality of at least two a_i in (3.1). Thus

    7∤a_j for EVERY j outside I.                                (4.2)

If r=2, (4.2) says no outside original index n_j=a_j is seven-divisible. Only the two cluster original indices carry7, contradicting the three-label consequence of Sun7(G).

## 5. Cluster sizes at least three

Let 3<=r<=7, so at least one outside label j exists. For each i∈I, (4.1) supplies a prime dividing gcd(a_i,a_j). This gcd divides the corresponding original index gcd and is <=7. Because 7∤a_j, the selected prime lies in `{2,3,5}`. The a_i are pairwise coprime, so the r selected primes are pairwise distinct. Therefore r<=3.

If r=3, EACH outside quotient index a_j is divisible by all three primes2,3,5. There are eight−three=5 outside labels, so two such original indices n_j=a_j have gcd at least30, contradicting the <=7 bound. Thus r=3 is impossible as well. All cases r=0,...,8 have been closed; `Sun_8(G)` follows. □

The proof never collapses the cluster to an intersection quotient coset and never attempts to flatten a product gcd. The previously pinned four-coset compression obstruction is compatible with this theorem: for a cluster of size3 the obstruction uses only ONE outside label, whereas a hypothetical eight-coset configuration necessarily has FIVE.

## 6. Conditional minimal-counterexample consequence

Assume the previously licensed arbitrary-group Sun7 statement. If a finite minimum-order Sun8 counterexample G exists, it has no nontrivial normal finite 7-group N: otherwise `G/N` is strictly smaller and satisfies Sun8 by minimality, and the theorem gives Sun8(G). For every prime p>=11, the independently written dual pair-gap theorem `frontier-20261028-dual-k-fibre-transfer-v1.md` (SHA256 `1c4631d57fb6c118d1d1859f9cfb33fae521433a65cfea74e4a2f41de14d1b67`) likewise rules out a nontrivial normal finite p-group, with NO Sun7 import in that dual step.

Thus, conditional on these candidate proofs and Sun7, all nontrivial normal p-subgroups of a minimum finite counterexample have p∈{2,3,5}. Equivalently, the prime divisors of any normal finite nilpotent subgroup lie in {2,3,5}, because its Sylow subgroups are characteristic in it and hence normal in G. Combined with the separate conditional finite-solvable-quotient result, the counterexample must also be perfect. Perfect is NOT simple; these are structural constraints, not an unrestricted solution.

## 7. Bounded independent support computation

Executed `/opt/homebrew/bin/python3 frontier-20261028-seven-kernel-support-check.py` with a20-second deadline. SHA256 **`845934a1c03cb5c786ef3144499eedf6e5b14c4bc180b18dd79e6643bb52c3f1`**. Actual output:

```text
cluster_size=2: cluster_support_sets=25; terminal_models=0
cluster_size=3: cluster_support_sets=10; terminal_models=0
cluster_size=4: cluster_support_sets=1; terminal_models=0
cluster_size=5: cluster_support_sets=0; terminal_models=0
cluster_size=6: cluster_support_sets=0; terminal_models=0
cluster_size=7: cluster_support_sets=0; terminal_models=0
PASS: no abstract models for cluster sizes 2..7
Wed Oct 28 17:15:55 PDT 2026
```

This enumerates squarefree prime supports of quotient indices on `{2,3,5,7}`, requiring pairwise coprime cluster supports; outside/cluster and outside/outside quotient gcd between2 and7; original projected gcd<=7; and at least three original seven-divisible labels. Under a genuine counterconfiguration with r=2,...,7 each quotient coset outside the cluster is disjoint from each cluster coset, so all such relevant gcds are nontrivial and <=7. Projecting to the four prime supports preserves those necessary conditions: primes>7 cannot be a shared divisor under the original bound, and forgetting higher exponents overapproximates. The finite output supports the incidence arithmetic, not the actual quotient-coset CRT, Section2 group argument, quotient Sun8, Sun7 import or a proof of unrestricted Sun8. The r=0,1,8 boundaries are handled in writing, not by this program.

## 8. Scientific and provenance limits

All conclusions remain written candidates until full independent scientific review. The old held Sun episode and all earlier quarantined outputs are not silently accepted or retrospectively validated; prior exposure is not claimed erased. No primary-source proof of Sun7, full finite-perfect classification, complete normal-kernel transfer, human/kernel/independent-family verification, priority or publication claim is made.
