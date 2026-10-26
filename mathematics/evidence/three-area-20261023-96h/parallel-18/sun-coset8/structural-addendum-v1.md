# Prime-seven structural addendum v1: subnormal vertices and normal private-prime quotients

Observed before creation: `2026-10-23T14:13:52-0700` (`/bin/date`). **CANDIDATE, written only; no execution and no novelty/acceptance claim.** Supplements, without editing, `reduction-and-generation-v1.md`, SHA256 `fa0497ae15bd3c765e05123996e4a94bd8038f2be1488b08dc7111f2fd7602c6`. P7 means eight disjoint left cosets with indices7r_i, r_i pairwise coprime. Every theorem below applies to the full P7 residual, with no private-prime, valuation or solvability restriction.

## 1. A subnormal subgroup index divisibility lemma

Let H be a finite-index SUBNORMAL subgroup of G, and K any subgroup. Choose a finite subnormal chain

    H=H_0 ◁ H_1 ◁ ... ◁ H_m=G.

Put K_j=K∩H_j. Since K_j/K_{j-1} embeds in H_j/H_{j-1},

    [K_j:K_{j-1}] divides [H_j:H_{j-1}].

Multiplying the finite index relations gives

    [K:K∩H] divides [G:H].

No normality of K is used. This is an elementary re-derivation, not a new-priority assertion.

## 2. No subnormal vertex in P7

**Theorem SN.** A P7 configuration cannot have even ONE subnormal U_v. This strengthens the normal-vertex exclusion in the preceding candidate.

**Proof.** Write n_i=7r_i. Define

    α_vj=[G:U_v∩U_j]/(7r_vr_j),  j≠v.

The denominator is lcm(n_v,n_j), so α_vj is a positive integer. By the subnormal divisibility lemma with H=U_v and K=U_j,

    [G:U_v∩U_j]=n_j[U_j:U_j∩U_v] divides n_j n_v.

Therefore α_vj divides7. The product formula gives

    |U_vU_j|/|G|=α_vj/7.

Disjointness of the chosen left cosets implies U_vU_j≠G, so α_vj<7. Primality of7 forces α_vj=1 for all seven neighbours j.

Apply the elementary fibre calculation of the preceding candidate with W=U_v (whose index is n_v, not necessarily7). Each other original coset meets

    [U_j:U_j∩U_v]=r_v

left U_v-cosets, none equal to g_vU_v. In any common U_v-coset, its translated piece has subgroup index

    [U_v:U_v∩U_j]=r_j.

Those seven indices r_j are pairwise coprime. Thus no two different neighbours can meet the same U_v-coset, by the elementary coprime-index intersection lemma. Seven neighbours require7r_v distinct U_v-cosets outside g_vU_v, but only n_v−1=7r_v−1 exist. Contradiction. QED.

The proof is valid for arbitrary original G by the common finite-core quotient (subnormality survives quotienting) or by direct finite-index counts. It imports neither S7 nor Zhu once P7 is assumed. Conjugacy preserves subnormality, so it applies to the inverted subgroups U_i^* as well. Consequently, relative to the literal S7 reduction, Sun8 HOLDS whenever at least one original U_i is subnormal. This is a scoped consequence, not the unrestricted theorem.

The all-α-one obstruction used here is consistent with Margolis–Schnabel, Corollary3.9, <https://arxiv.org/pdf/1803.03569>, read at its literal statement. The present proof is written out and does not import that corollary as an unexamined premise.

## 3. Exact quotient projection criterion

**Lemma Q.** Let N◁G and let eight cosets g_iU_i be pairwise disjoint. Put

    c_i=[N:N∩U_i],
    d_i=[G:NU_i],
    n_i=c_i d_i.

If the c_i are pairwise coprime, then the projected cosets in G/N are pairwise disjoint, with subgroup indices d_i.

**Proof.** The factorization is the standard second-isomorphism/index formula because N is normal. If two projected cosets overlap, choose a common left N-coset C meeting both original cosets. Each nonempty intersection with C is, after left translation into N, a left coset of N∩U_i or N∩U_j. Their indices in N are c_i,c_j. Coprimality forces the two pieces to intersect, contradicting original disjointness. QED.

This proves disjointness of projected cosets; projecting disjoint subsets does NOT in general preserve disjointness without the coprime-fibre condition. No such unjustified projection is used here.

## 4. Removing normal 7′-subgroups without restricting the problem

Suppose G is finite, the configuration is P7, and N◁G has order coprime to7. Then each c_i above divides |N| and n_i=7r_i, so c_i divides r_i. Since the r_i are pairwise coprime, so are the c_i. LemmaQ therefore gives another P7 configuration in G/N, of indices

    d_i=7(r_i/c_i),

whose private cofactors remain pairwise coprime. Thus a P7 counterexample in a group with nontrivial normal7′-subgroup always descends to a SMALLER finite quotient counterexample.

**Corollary MIN.** If P7 has a finite counterexample, choose one with minimal group order. It has **no nontrivial normal7′-subgroup**, i.e. O_{7′}(G)=1. It also has no subnormal U_i by SN, and its five-wise generation property in both orientations follows from G5 of the preceding candidate.

The existence of a minimal finite group is justified by the common finite-core reduction and the well-ordering of positive orders. MIN is a necessary reduction only; it does not prove G is simple, nonsolvable, bounded in order or drawn from a finite classification. The private cofactors can still contain arbitrarily large primes and powers.

## 5. Exact barrier after these written attacks

R8 reduces the unrestricted target to P7. G5 excludes a large actual group-geometric class; SN excludes every subnormal vertex; Q/MIN remove normal private-prime quotients in a least-order example. **None proves that the remaining class is empty.** The exact open obligation is still the nonexistence or genuine realization of P7, now necessarily having:

- arbitrary pairwise-coprime positive private cofactors r_i (at most one may carry any given prime);
- no subnormal vertex;
- every five subgroups generating G, both before and after inversion;
- in a least-order finite example, O_{7′}(G)=1.

A common index-seven overgroup for five vertices would contradict G5, but no argument here forces such an overgroup. In particular the general elementary fact that a generated subgroup has index1 or7 permits index1; treating it as necessarily7 would be exactly the missing, false-as-a-general-rule step. Likewise cyclic congruence impossibility does not transfer to arbitrary groups: Menon's2026 primary Ginosar counterexample makes that shortcut invalid.

Requested independent reconstruction: the chain-index divisibility lemma, the all-α-one fibre count, the quotient-coset overlap-to-fibre bridge, and the precise MIN scope. No modelCLI, scientific execution, proof-assistant kernel, human review or novelty clearance has occurred.
