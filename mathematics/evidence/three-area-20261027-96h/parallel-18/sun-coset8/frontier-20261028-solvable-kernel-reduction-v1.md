# Sun8 is unchanged by a solvable normal kernel — conditional written candidate

**NEW WRITTEN CANDIDATE, not reviewed/adopted/formally verified/novelty-cleared.** Actual native prewrite clock **Wed Oct 28 17:20:39 PDT 2026**. This successor proves the missing normal **2- and 3-kernel** steps and removes the extra kernel-Sun8 assumption from the earlier5-kernel candidate. Together with the named7-kernel and dual-large-prime candidate proofs, it yields a conditional solvable-radical reduction. It does NOT solve the nonsolvable quotient.

## 1. Exact statements and imports

For any group X, `Sun_k(X)` means that every k pairwise-disjoint ACTUAL LEFT cosets of finite-index subgroups have a pair of indices whose gcd is at least k.

**Small-prime kernel theorem.** Let p∈{2,3,5}. For ANY group G and normal N, suppose every finite-index subgroup of N has p-power index. If `Sun_7(G)` and `Sun_8(G/N)`, then `Sun_8(G)`. No `Sun_8(N)` or `Sun_7(N)` is assumed, and G, N and G/N may be infinite.

**Solvable-normal-kernel corollary.** Assume the previously licensed statement that `Sun_7(X)` holds for EVERY group X. Also assume the separately pinned proofs of the normal seven-index-power kernel theorem `676627da3c52ba07169c225ebb1373ec4fb48a5691009e2ad399599992a765c0` and the dual pair-gap/large-prime theorem `1c4631d57fb6c118d1d1859f9cfb33fae521433a65cfea74e4a2f41de14d1b67`. Then for ANY G and normal R whose every finite homomorphic image is solvable,

    Sun_8(G)  iff  Sun_8(G/R).

This includes every finite solvable R and every solvable R of finite derived length. `Sun_8(G)=>Sun_8(G/R)` itself needs NO imported theorem. The reverse implication needs the explicit universal Sun7 import and both separately named kernel-transfer candidates; neither is silently taken as newly accepted by this packet. In particular, this is not an unconditional claim that every nonsolvable group satisfies Sun8.

## 2. Actual index/fibre setup and quotient heredity

In any normal extension `1->N->G->Q->1`, suppose k actual pairwise-disjoint finite-index G-cosets `g_i U_i` exist. Define

    C_i=pi(g_i)pi(U_i),
    a_i=[Q:pi(U_i)],  b_i=[N:N∩U_i],  n_i=[G:U_i]=a_i b_i.

If C_i,C_j meet, translating their actual fibres in one common quotient point gives disjoint N-cosets of subgroup indices b_i,b_j. Two disjoint cosets cannot have coprime indices: the diagonal map from cosets of the intersection subgroup to the product of the two coset spaces is injective, and the domain index is divisible by and bounded by the product of coprime indices, so it is surjective. Thus overlapping quotient images imply `gcd(b_i,b_j)>=2`.

If b_j=1, its N-fibre is the whole N wherever nonempty. Therefore actual disjointness forces C_j disjoint from EVERY other C_i. This is a statement about the SAME original cosets; there is no independent fibre selection.

For any surjection G->Q, `Sun_k(G)` implies `Sun_k(Q)`: pull back each of k actual disjoint Q-cosets to a G-coset of a finite-index preimage subgroup. They remain disjoint and the indices are exactly preserved. This pays the forward direction of the corollary, for arbitrary groups and k, with no normal-kernel restriction.

## 3. Seven labels and two outside test cosets for p=2,3,5

For the small-prime theorem, suppose eight actual disjoint G-cosets have original indices n_i with pairwise gcd<=7. Put I={i:b_i>1}, r=|I|. If r<=1, all eight quotient cosets are pairwise disjoint by Section2, and `Sun_8(Q)` produces an original pair with gcd>=8, contradiction. Assume r>=2.

`Sun_7(G)` applied to each seven-subfamily forces at least THREE original indices divisible by7: every supplied pair must have gcd exactly7, so omitting one of at most two seven-labels would contradict that seven-subfamily.

All indices b_i are powers of p. Hence for i∈I, p|n_i. At most ONE cluster original index is seven-divisible, because two such indices would share 7p>7. Therefore at least two seven-divisible labels lie OUTSIDE I, where b_j=1 and n_j=a_j.

There are in fact TWO such outside seven-indices V,W both prime to p:

- If a cluster label A carries7, its n_A is divisible by 7p. Every outside seven-index must be prime to p, else its original gcd with n_A is at least7p.
- If no cluster label carries7, at least three outside indices carry7. Any pair has gcd exactly7, so at most one of these outside indices is divisible by p; select two others.

Thus `7|a_V,a_W`, `p∤a_V,a_W`, and `gcd(a_V,a_W)=7`. The outside actual quotient cosets are disjoint from ALL other quotient cosets.

Let q and s be the two distinct primes in `{2,3,5}\{p}`. For ANY cluster label i whose n_i is not seven-divisible, 7 does not divide a_i. Its quotient coset is disjoint from C_V and C_W. Hence the two quotient-index gcds are nontrivial and each divides the corresponding original gcd<=7. Their shared prime factors must lie in `{q,s}`: V,W are prime to p and a_i is prime to7. Since V and W share no prime other than7, their two nontrivial intersections must use DISTINCT primes q and s. Therefore

    q s | a_i,  and  p q s=30 | n_i.                            (3.1)

Two non-seven cluster labels would have original gcd>=30, impossible. Together with at most one seven cluster label, this gives r<=2. Since r>=2, there are exactly TWO cluster labels: A with 7|n_A and B with 7∤n_B. By (3.1), `q s|a_B` and `30|n_B`. After exchanging V,W if needed,

    q|a_V,  s|a_W,  s∤a_V,  q∤a_W.                             (3.2)

These are deductions from actual quotient-coset disjointness and the counterconfiguration bound, not independent hypothetical fibre choices.

## 4. The six outside labels yield the contradiction

Since r=2, there are SIX outside labels. Besides V,W, no outside label T can be seven-divisible. Indeed n_A is divisible by7p, so p∤a_T; its original gcd with each of a_V and a_W is exactly7, so (3.2) forces q∤a_T and s∤a_T. Meanwhile 7∤a_B because B is non-seven. But C_T is disjoint from C_B, and a nontrivial gcd of their indices bounded by7 would need a shared prime among `{p,q,s,7}`. T has none of p,q,s and B has no7. Contradiction.

Therefore choose ANY one of the four outside labels F other than V,W; it is not seven-divisible. Its quotient coset is disjoint from C_V and C_W. By (3.2), p∤a_V,a_W, 7∤a_F, and the two nontrivial quotient-index gcds are <=7. Consequently q|a_F and s|a_F, so

    q s | a_F=n_F.

For p=2, q s=15; for p=3, q s=10. Both exceed7 and divide n_B by (3.1), contradicting `gcd(n_B,n_F)<=7`.

For p=5, q s=6. Both n_A and n_B are divisible by5; their original gcd must therefore be exactly5. Dividing by5 shows `gcd(a_A,a_B)=1`; since6|a_B, a_A is prime to2 and3. C_F is also disjoint from C_A, so their quotient indices have a common prime <=7. The only possibility is5: a_A has neither2 nor3 and a_F has no7. Thus `5|a_F`, and `30|a_F` and `30|n_B`, contradiction.

Every r is exhausted. This proves the small-prime kernel theorem, including all p=2,3,5, without using a kernel Sun8 premise. □

## 5. Prime-power kernels and finite solvable normal kernels

For p=7, the separately pinned seven-kernel candidate proves the analogous implication using Sun7(G) and Sun8(Q), and independently establishes the required Sun8(N) from the seven-index spectrum. For p>=11 the separately pinned dual pair-gap theorem applies: any disjoint N-coset pair has gcd>=p>=11, so quotient images of a hypothetical counterconfiguration are pairwise disjoint and Sun8(Q) suffices even without Sun7(G). Consequently, conditional on those two complete proofs and Sun7(G) when p<=7, the quotient-to-group transfer holds for EVERY p-power-index kernel.

Now let F be a FINITE group with a finite solvable normal subgroup R and assume Sun8(F/R). A finite solvable group has a derived series with finite abelian factors. Each finite abelian factor decomposes into its p-primary characteristic subgroups: the elements killed by a power of p form a characteristic subgroup, and their products over any selected set of primes are characteristic. Pulling a chain of those products back through each derived factor gives a series

    1=R_0 < R_1 < ... < R_d=R

in which EVERY R_i is normal in F and EVERY R_i/R_(i−1) is a finite p-group. The required normality follows because the derived subgroups are characteristic in R, the chosen primary-factor products are characteristic in their abelian factors, and R is normal in F. No assertion that R is nilpotent is made.

Starting from the assumed Sun8(F/R), apply the prime-kernel implication successively to

    F/R_(i−1)  ->  F/R_i,

whose kernel is the finite p-group R_i/R_(i−1). The UNIVERSAL Sun7 statement supplies each needed `Sun_7(F/R_(i−1))`. Descending i from d to1 gives Sun8(F). The quotient direction was already proved in Section2. Thus, under the named imports, finite solvable normal kernels preserve Sun8 in BOTH directions.

## 6. Arbitrary groups whose kernel has only solvable finite images

Let G be arbitrary and R normal with every finite image solvable. Assume Sun8(G/R). Given ANY hypothetical finite-index eight-coset counterconfiguration in G, intersect the finitely many subgroup cores `core_G(U_i)`. Each core has finite index, because G acts on the finite set G/U_i; hence K=∩core(U_i) is finite-index normal and lies in every U_i. The quotient F=G/K is finite, the eight image cosets are actual and disjoint, and their subgroup indices equal the original indices.

The image Rbar=RK/K is a finite homomorphic image of R and is solvable. F/Rbar is a quotient of G/R. Since Sun8 passes to arbitrary quotients as proved in Section2, `Sun_8(F/Rbar)`. Section5 gives `Sun_8(F)`, contradicting the projected configuration. Thus Sun8(G/R) implies Sun8(G). The converse is unconditional quotient heredity, proving the corollary.

For an ordinary solvable group R, every quotient, including every finite image, is solvable; for R=G this gives Sun8(G) for all solvable groups under the named imports. It does not assume every group with only solvable finite images is itself solvable.

## 7. Conditional finite-minimal-counterexample structure

Assume the named universal Sun7 statement and the complete 2/3/5,7 and >=11 kernel proofs. If a finite minimum-order Sun8 counterexample G exists, its solvable radical R is trivial: otherwise G/R is a smaller finite group, so it has Sun8 by minimality, while the solvable-kernel corollary gives Sun8(G). The finite solvable radical exists because products of solvable normal subgroups are solvable normal and finite order bounds an ascending product.

Separately, the prior conditional solvable-QUOTIENT transfer (index2/3 and previous5/7/>7 proof scopes) implies G is perfect. Therefore every such minimum counterexample is **perfect and has trivial solvable radical**. This does not imply it is simple: nonabelian-simple direct products and other radical-free perfect groups are not excluded. No unrestricted Sun8 theorem or simple-group classification is claimed.

## 8. Exact bounded incidence check and evidence ceiling

Executed `/opt/homebrew/bin/python3 frontier-20261028-small-prime-kernel-support-check.py` with a30-second deadline. SHA256 `f2b03ad785346a6d36c7f0f73b96873bc3a23323347f56fbf02f2ff2b37b421e`. Actual output:

```text
p=2, cluster_size=2: cluster_support_sets=53; terminal_models=0
p=2, cluster_size=3: cluster_support_sets=100; terminal_models=0
p=2, cluster_size=4: cluster_support_sets=147; terminal_models=0
p=2, cluster_size=5: cluster_support_sets=194; terminal_models=0
p=2, cluster_size=6: cluster_support_sets=241; terminal_models=0
p=2, cluster_size=7: cluster_support_sets=288; terminal_models=0
p=3, cluster_size=2: cluster_support_sets=39; terminal_models=0
p=3, cluster_size=3: cluster_support_sets=47; terminal_models=0
p=3, cluster_size=4: cluster_support_sets=47; terminal_models=0
p=3, cluster_size=5: cluster_support_sets=47; terminal_models=0
p=3, cluster_size=6: cluster_support_sets=47; terminal_models=0
p=3, cluster_size=7: cluster_support_sets=47; terminal_models=0
p=5, cluster_size=2: cluster_support_sets=25; terminal_models=0
p=5, cluster_size=3: cluster_support_sets=10; terminal_models=0
p=5, cluster_size=4: cluster_support_sets=1; terminal_models=0
p=5, cluster_size=5: cluster_support_sets=0; terminal_models=0
p=5, cluster_size=6: cluster_support_sets=0; terminal_models=0
p=5, cluster_size=7: cluster_support_sets=0; terminal_models=0
PASS: no abstract models for p=2,3,5 and cluster sizes 2..7
Wed Oct 28 17:20:00 PDT 2026
```

The finite abstraction retains squarefree prime supports `{2,3,5,7}`, permits REPEATED cluster signatures (essential for p=2,3), uses p*a_i as a divisor of each actual cluster original index, enforces necessary quotient-disjointness gcd>=2 and original gcd<=7, and preserves the >=3 seven-label condition. Shared primes >7 cannot occur in any original pair under the counterconfiguration bound; forgetting larger primes and high powers overapproximates. It supports only the finite incidence exclusion for r=2,...,7, not the quotient/fibre argument, r=0/1, Sun7, the solvable series, or a formal/global proof.

## 9. Remaining obligations

Main and a disjoint reviewer must inspect ALL the written proofs, quotient/kernel hypotheses, finite-core lift and the exact Sun7 import before any adoption. Earlier quarantine outcomes are not treated as proved premises or retroactively validated; prior exposure is not erased. Full Sun7 proof/primary-source authentication, finite radical-free perfect groups, arbitrary non-solvable normal kernels, unrestricted Sun8, human/kernel/independent-family verification, priority and novelty remain open. No simple-group reduction is claimed.
