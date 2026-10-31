# f20 — seven-power kernel transfer and fibre-collapse obstruction

Reviewer **PhysicsPPT44-2**. Actual native clock immediately before creation: **Wed Oct 28 17:21:10 PDT 2026**.

**Verdict: NO_SUBSTANTIVE_DEFECT AT EXACT STATED SCOPES — 0 FATAL / 0 MAJOR / 0 MINOR.** The transfer holds for arbitrary G, N normal, quotient Q, and all finite-index subgroup indices of N powers of 7, provided the explicit hypotheses `Sun8(Q)` and `Sun7(G)` hold. The C7×C_L family is a genuine partial actual-coset obstruction to a quotient-merge lifting principle, not an eight-coset counterexample. The finite minimum-counter consequences retain their stated imports. Sun7 is **not proved or authenticated** here; no unrestricted Sun8, formal/kernel, human, configured-family, novelty or publication acceptance follows.

## 1. Bound inputs and review frontier

- Complete assignment `f20-sun-seven-kernel-transfer/assignment-v1.json`, SHA256 `e04b6be5ca44b3f60affa8f7d3b0536c408fc69d64287b2fb8375b315fea0d36`.
- Complete 97-LF `frontier-20261028-seven-kernel-transfer-v1.md`, SHA256 `676627da3c52ba07169c225ebb1373ec4fb48a5691009e2ad399599992a765c0`.
- Complete 81-LF `frontier-20261028-fibre-collapse-obstruction-v1.md`, SHA256 `dd5009890b2999fe47b20fb94d91f16e0880f3e8f1ccd720dda859e779886756`.
- Registered actual-left-coset definitions and my prior complete f1/f16 reviews of the needed fibre and dual-transfer arguments were consulted at their exact conditional scopes. The f16 review SHA256 is `44cd1e9b36b6737a26c05044295c2f6e2f60a0320869e1bae9c878a7caac8235`.

I have prior Sun-coset familiarity and authored those prior same-harness reviews; this is not blind, independent-family or clean-cognition review. No author contact, nested agent, prior quarantined outcome or author program result is a proof premise. All group reasoning below is rederived from the current definitions and elementary facts; my independently implemented bounded checks are §7.

## 2. Spectrum premise independently implies Sun8(N)

`Sun_k(X)` concerns every k pairwise-disjoint **actual left cosets** of finite-index subgroups and demands a pair of indices with gcd≥k. It is vacuous if there are too few such cosets. Assume every finite-index subgroup of N has index a power of 7.

Let H≤N have index 7. The left action on N/H has core `K=core_N(H)` as kernel, so K is finite index and `[N:K]=7^t` by the spectrum premise. Its image is a transitive subgroup of S7, of order a 7-power dividing 7!. Lagrange and transitivity show its order is exactly 7. Hence `[N:K]=[N:H]=7` and K⊆H give K=H; every index-seven subgroup is normal. This remains valid for infinite N, since only the permutation image is finite.

For distinct normal index-seven subgroups H,K, their product HK strictly contains H and hence equals N. Given any left cosets of H,K, the resulting factorization supplies an actual common element. Therefore disjoint index-seven cosets must use the same subgroup.

Now suppose eight disjoint finite-index N-cosets had pairwise gcd≤7. An index-one coset is all N, so none has index 1. Every index is a positive power of 7; at most one can be divisible by 49, since two would have gcd≥49. At least seven have index exactly 7. Their pairwise-disjoint cosets all use the same normal subgroup H, and seven distinct H-cosets exhaust N, leaving no nonempty eighth coset. Contradiction. Thus the spectrum premise **itself** yields Sun8(N), without Sun7 or solvability.

## 3. Actual fibres and cluster consequences

For original disjoint cosets `g_iU_i` in G put `n_i=[G:U_i]`, `a_i=[G/N:π(U_i)]`, `b_i=[N:N∩U_i]`, and `C_i=π(g_i)π(U_i)`. Normality makes NU_i a subgroup and gives `n_i=a_i b_i`; all a_i,b_i are finite. If actual C_i,C_j meet, the two original cosets intersect the same quotient fibre in disjoint nonempty actual N-cosets of indices b_i,b_j. Two disjoint finite-index cosets in any group have noncoprime subgroup indices: the diagonal map from the intersection-subgroup coset space to the two coset spaces is injective, and coprimality forces its domain cardinality to equal the product and hence the map to be surjective. Thus meeting C_i,C_j require `gcd(b_i,b_j)≥2`.

Assume a counterconfiguration of eight actual G-cosets has all original gcds≤7. Let `I={i:b_i>1}` and r=|I|. Each b_i is a power of 7. Every i∈I has 7|n_i; for distinct cluster indices i,j their original gcd is exactly 7. Dividing both n-indices by 7 gives coprime integers, and both a_i and a_j divide those quotients. Consequently the cluster quotient indices a_i are pairwise coprime.

If j∉I then b_j=1. Its nonempty fibre at any point of C_j is the whole N, so original disjointness makes C_j disjoint from **every** other C_i. All quotient cosets outside the cluster are therefore pairwise disjoint and also disjoint from all cluster quotient cosets. This uses actual fibres; it does not replace the cluster by an intersection coset or assume separate local packings lift.

## 4. Every cluster size r=0,…,8

**r=0 or 1.** If any two C_i meet, their kernel indices have nontrivial gcd, impossible when at most one b_i is >1. Thus all eight actual C_i are disjoint. `Sun8(Q)` supplies a pair of quotient indices with gcd≥8, hence the corresponding original gcd is ≥8, contradiction.

**r=8.** The eight a_i are pairwise coprime. The diagonal injection `Q/(∩π(U_i))→∏ Q/π(U_i)` has domain size divisible by each a_i and at most their product; pairwise coprimality forces equality and surjectivity. Thus the eight prescribed actual quotient cosets share a point. Their eight disjoint actual N-fibres contradict Sun8(N) from §2.

**r=2,…,7.** Every outside C_j is disjoint from each cluster C_i. The elementary two-coset lemma applied in Q gives `gcd(a_i,a_j)≥2`. If 7 divided an outside a_j, then n_j=a_j and every cluster n_i is seven-divisible; original gcd≤7 forces `gcd(n_i,n_j)=7`. Since `gcd(a_i,a_j)` divides that gcd and is nontrivial, it equals 7 for every i∈I. This makes every cluster a_i divisible by 7, contradicting their pairwise coprimality because r≥2. Therefore **every outside a_j is prime to 7**.

`Sun7(G)` applied to every seven-subfamily of the eight original cosets forces at least three original indices divisible by 7: the guaranteed pair has gcd exactly 7 under the counterconfiguration bound, and if at most two labels carried 7, one could omit one and leave at most one such label in a seven-subfamily. Outside labels now carry no 7 because n_j=a_j. Hence r=2 is impossible.

For every outside j and each cluster i, choose a prime dividing the nontrivial `gcd(a_i,a_j)`. That gcd divides the corresponding original gcd and is ≤7; the outside index is 7-free, so the prime is in {2,3,5}. Pairwise coprimality of the cluster a_i makes these selected primes distinct. Thus r≤3: the cases r=4,5,6,7 all fail. If r=3, every outside a_j is divisible by all 2,3,5. There are five outside labels; two have original indices a_j with gcd at least 30>7. Thus r=3 fails too. This closes every boundary 0≤r≤8.

The transfer theorem is therefore established for the stated spectrum, `Sun8(Q)` and `Sun7(G)` hypotheses. No finite, solvable or split quotient hypothesis is used, and the quotient premise is not inferred merely from Sun8(N).

## 5. Conditional minimum-counterexample consequences

Assume the arbitrary-group Sun7 statement. If a minimum-order finite Sun8 counterexample G has nontrivial normal finite 7-group N, then G/N is strictly smaller and satisfies Sun8 by minimality; the seven-power index spectrum holds by Lagrange; the theorem contradicts the counterexample.

For a nontrivial normal finite p-group N with p≥11, every finite subgroup index is a p-power. The independently reconstructed dual theorem from f16 gives pair-gap 8 for N and transfers Sun8 from the smaller quotient, so these p-groups are also excluded. Thus all nontrivial normal p-subgroups have p in {2,3,5}, subject to the Sun7 import where the p=7 step uses it.

If K is a finite normal nilpotent subgroup of G, each of its Sylow subgroups is unique and hence characteristic in K, therefore normal in G. Its prime divisors must belong to {2,3,5}. The separate finite-solvable-quotient transfer reconstructed in f16 makes the same minimum counterexample perfect, **conditional** on universal Sun7 and the earlier named prime transfers. Perfect does not mean simple and no counterexample is excluded globally.

## 6. Exact actual-coset quotient-collapse obstruction

Let P be a set of distinct primes from {2,3,5}, with `L=∏_(p∈P)p≥8`; then |P|≤3 and gcd(7,L)=1. In the actual additive group `G=C7×C_L`, with normal N=C7×{0}, choose distinct first coordinates z_i and form

`U_i={0}×p_i C_L`, `g_i=(z_i,0)` for p_i∈P,

and `U_*=C7×{0}`, `g_*=(0,1)`. Cluster cosets `{z_i}×p_i C_L` are disjoint by the distinct first coordinates. The outside coset `C7×{1}` is disjoint from each cluster coset because 1 is not in any p_i C_L. Their actual G-indices are `7p_i` and L. Distinct cluster pairs have gcd 7, and each cluster/outside pair has gcd p_i≤5.

Under the actual quotient map to C_L, the cluster cosets are `p_i C_L`, with intersection `{0}`; the outside coset is `{1}`. Both are cosets of the trivial subgroup of quotient index L, so the merged pair has gcd L≥8 although no original pair does. The discrepancy is the product of different cluster quotient factors; it is not an eight-coset configuration or a counterexample to Sun8.

The argument is valid for every permitted P and distinct z_i, including the two-prime and three-prime choices. For P={2,3,5}, L=30 and z=(0,1,2), the source's four actual indices are 14,21,35,30 and the six gcds are 7,7,2,7,3,5. The original cluster/outside disjointness and the quotient intersection and outside coset are proved above independently of the author's two checkers.

## 7. Independently executed checks and their limits

I wrote `frontier-20261028-review-f20-seven-kernel-check.py`, SHA256 `79e76988d734bdaf10d5caa9c04f6e72e68570181359c5848e46f4041d04bc5c`, and ran

`PYTHONDONTWRITEBYTECODE=1 /usr/bin/env python3 frontier-20261028-review-f20-seven-kernel-check.py`.

For each 2≤r≤7 it searches squarefree quotient-index supports on {2,3,5,7}; cluster original-index representatives are `7a_i`, outside representatives a_j. It requires all original representative gcds≤7, quotient gcd≥2 whenever an outside label is involved, and at least three seven-divisible original indices. This is an **overapproximation** of necessary support constraints: retained supports divide actual quotient indices; multiplying a cluster support by 7 still divides its original index, and a required quotient gcd cannot rely only on a prime >7 under the original bound. It intentionally does not generate actual groups/cosets or verify Sun7. The corrected output reported **zero terminal models for each r=2,3,4,5,6,7**.

A first execution revealed a checker accounting defect: its `terminal_models` field incorrectly reused the number of eight-label prefixes *before* the seven-count leaf prune (r=2 printed 126 with `first=null`). I corrected that field to count only leaves surviving the stated seven-divisibility condition and reran; 126 remains explicitly labeled as the pre-prune prefix count, while the surviving terminal count is zero. This was a local reviewer-checker bug, not an author-proof finding. Neither count replaces the written proof in §§2–4.

The same independent program realizes the concrete obstruction as actual residue classes in Z/210Z under the CRT isomorphism to C7×C30: indices `(14,21,35,30)`, representatives `(0,15,30,1)`. It observed coset sizes `(15,10,6,7)`, all six actual pair intersections zero, pair gcds `(7,7,2,7,3,5)`, quotient cluster intersection `{0}`, outside quotient coset `{1}`, and merged gcd 30. Changing the outside representative to 0 gave one intersection with the first cluster coset; changing the second cluster representative to 0 gave five. Those are actual finite checks and negative controls, not a proof that this partial configuration extends to eight cosets. The author's programs and reported counts were not used as independent evidence.

## 8. Exact disposition

| Claim | Disposition |
| --- | --- |
| Seven-power spectrum ⇒ Sun8(N) | NO_SUBSTANTIVE_DEFECT; arbitrary N, including infinite groups |
| Quotient-to-group transfer, cluster boundaries r=0,1,8 and all r=2,…,7 | NO_SUBSTANTIVE_DEFECT with `Sun8(G/N)` and `Sun7(G)` explicit |
| Minimum-counterexample normal-p and nilpotent restrictions | NO_SUBSTANTIVE_DEFECT conditional on universal Sun7 and the independently reviewed dual transfer; perfectness also needs the separately named solvable-quotient transfer |
| C7×C_L actual-coset fibre-collapse family | NO_SUBSTANTIVE_DEFECT at the stated partial-configuration scope |

No gap requiring a counterexample to the stated conditional theorem was found. No arbitrary-kernel transfer, source/book equivalence, Sun7 proof, unrestricted Sun8 solution, simple-counterexample conclusion or novelty claim follows. The parent must inspect complete candidate and review before adoption; earlier historical quarantine findings remain historical, not retrospectively certified.
