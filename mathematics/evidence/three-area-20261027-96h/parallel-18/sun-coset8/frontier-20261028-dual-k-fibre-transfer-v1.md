# A dual normal-extension transfer from quotient to group

**NEW WRITTEN CANDIDATE; not reviewed/adopted/formally verified or novelty-cleared.** Actual native prewrite clock **Wed Oct 28 17:11:54 PDT 2026**. The theorem below has no Sun7 import and applies for EVERY integer k>=2. It is complementary to, not a substitute for, the kernel-to-group prime-order transfers.

## 1. Exact statement

For any group X, write `Sun_k(X)` for: every k pairwise-disjoint ACTUAL LEFT cosets of finite-index subgroups of X have a pair of subgroup indices with gcd at least k. This property is vacuous if no such k cosets exist.

Say that a group N has **pair-gap k** when, for EVERY TWO pairwise-disjoint actual left cosets of finite-index subgroups H,K of N,

    gcd([N:H],[N:K]) >= k.

This is an explicit condition on N, not a consequence of `Sun_k(N)` alone.

**Theorem.** For every integer k>=2, every group G, and every normal subgroup N, if N has pair-gap k and `Sun_k(G/N)` holds, then `Sun_k(G)` holds. The result includes infinite G, N and quotient, nonsplit extensions, arbitrary finite-index (not necessarily normal) original subgroups and noncovering cosets.

**Index-spectrum sufficient condition.** It is enough that for every pair of finite-index subgroups H,K of N,

    gcd([N:H],[N:K]) = 1  or  gcd([N:H],[N:K]) >= k.         (1.1)

A simpler sufficient condition is that EVERY finite-index subgroup of N has index whose prime divisors are all >=k. In particular, for k=8 this holds for a finite normal p-group N with p>=11, including the trivial N. These are sufficient hypotheses; no necessity is asserted.

## 2. Proof on actual fibre cosets

Suppose a counterconfiguration exists: k pairwise-disjoint actual G-cosets `g_i U_i`, finite n_i=[G:U_i], with `gcd(n_i,n_j)<k` for every i≠j. Let pi:G->Q=G/N and put

    a_i=[Q:pi(U_i)],   b_i=[N:N∩U_i],   n_i=a_i b_i,
    C_i=pi(g_i) pi(U_i).

The index identity follows from the finite-index chain and `NU_i/U_i ≅ N/(N∩U_i)` as coset spaces. Each C_i is an actual left Q-coset of finite-index subgroup pi(U_i), not an arbitrary subset.

Suppose C_i and C_j meet. Choose a common quotient point q and representative t. The fibres of the two original cosets in tN, translated by t^-1, are nonempty ACTUAL disjoint left N-cosets of N∩U_i and N∩U_j. Their indices are b_i,b_j. Pair-gap k implies `gcd(b_i,b_j)>=k`, and because b_i|n_i and b_j|n_j, `gcd(n_i,n_j)>=k`, contradiction. Therefore ALL quotient cosets C_i are pairwise disjoint.

Apply the stated `Sun_k(Q)` to these SAME quotient cosets. Some pair has `gcd(a_i,a_j)>=k`, and a_i|n_i and a_j|n_j imply the same lower bound for the original indices. This contradicts the counterconfiguration and proves `Sun_k(G)`. □

This proof carries actual representatives and subgroups through each map. It does not assert that any independently selected system of N-fibres lifts to G, that Sun_k(N) follows from Sun_k(Q), or that the two properties are equivalent.

## 3. Proof of the sufficient kernel-index conditions

For two disjoint finite-index N-cosets with subgroup indices r,s, `gcd(r,s)>=2`: if r,s were coprime, the diagonal map from N/(H∩K) into N/H × N/K would be injective, its domain size would be both at most rs and divisible by r and s, and hence exactly rs; every specified tuple of cosets would occur, contradicting disjointness. This argument works for nonnormal H,K and infinite N.

Under (1.1), that gcd is nontrivial and therefore at least k, establishing pair-gap k. If all prime divisors of every finite subgroup index of N are at least k, any nontrivial gcd has such a prime divisor and hence is at least k, also establishing (1.1). When N is a finite p-group with p>=11, each subgroup index is a power of p, by Lagrange, so the k=8 condition follows. The trivial N has pair-gap k vacuously.

The spectrum hypothesis is stronger than what the proof needs. For a SINGLE configuration, it suffices that no pair of its specific kernel indices b_i,b_j has gcd in `[2,k−1]`; then a counterconfiguration's meeting fibres are already impossible, and the same quotient argument applies. This is a sufficient actual-configuration condition, not an arbitrary specification of free fibre data.

## 4. Complementarity and exact limitation

Previously supported v2 used `Sun_8(N)` plus a quotient `(R7)` index-spectrum condition to force a COMMON quotient fibre. The theorem here instead uses a stronger TWO-COSET kernel condition plus `Sun_8(Q)` to force the quotient cosets to be PAIRWISE DISJOINT. It transfers in the opposite direction and requires no universal Sun7 premise. Neither statement proves general extension closure from `Sun_8(N)` and `Sun_8(Q)` alone.

The new index2/3 candidates and prior index>=5 results additionally yield a conditional solvable-quotient transfer at the separately stated Sun7 and prior theorem imports. The present theorem can apply where the quotient is not solvable, provided the ACTUAL quotient's `Sun_8` property is independently known. It does not prove that property for finite simple quotients, or settle an arbitrary kernel, and claims no novelty.

A separate elementary observation explains the A5 experiment below: assuming `Sun_7(X)`, if no finite-index subgroup of X has index divisible by7, then `Sun_8(X)` holds. Indeed a putative eight-counterconfiguration contains a seven-subfamily whose Sun7 pair has gcd exactly7, forcing its indices divisible by7. For a finite group of order not divisible by7, Lagrange provides the no-seven-index condition. This observation is conditional on `Sun_7(X)`, not an independent validation of the imported theorem.

## 5. Bounded actual-coset computations

These computations check specific finite instances only, NOT the general theorem or novelty. Both programs enumerate the subgroup closure from the identity by adding each possible group element. Every finite subgroup has a finite generating set, so by induction on its generators this process reaches it; each produced subgroup is also checked directly for multiplication closure. For each subgroup the program generates actual LEFT cosets and checks that they partition the group. It searches for eight pairwise disjoint cosets whose actual subgroup indices have pairwise gcd<=7. A returned counterconfiguration would still need a separate witness verifier before acceptance.

**D22 actual instance:** `frontier-20261028-dihedral22-coset-check.py`, SHA256 `4442abb3c8415df9f5205259cd673f542759d883cdefd4ea202770c81d1e029a`.

```text
/opt/homebrew/bin/python3 frontier-20261028-dihedral22-coset-check.py
group_order: 22
subgroup_count: 14
subgroups_by_order: {1: 1, 2: 11, 11: 1, 22: 1}
left_coset_count: 146
cosets_by_index: {1: 1, 2: 2, 11: 121, 22: 22}
search_nodes: 140
RESULT: no eight-coset counterconfiguration in D22
Wed Oct 28 17:11:46 PDT 2026
```

The group is the explicit semidirect product C11⋊C2, so its normal kernel C11 meets pair-gap8 and its quotient C2 satisfies Sun8 vacuously. This is a positive instance, not a new family or a proof of the theorem. The listed clock was observed after the command and the two program hashes completed.

**A5 actual instance:** `frontier-20261028-a5-exact-coset-search.py`, SHA256 `0d22c17cb7b735e5f7cd8e182414085e2575fc78e0f6d97b4354b5472d176b5a`. Actual bounded command output:

```text
/opt/homebrew/bin/python3 frontier-20261028-a5-exact-coset-search.py
group_order: 60
subgroup_count: 59
subgroups_by_order: {1: 1, 2: 15, 3: 10, 4: 5, 5: 6, 6: 10, 10: 6, 12: 5, 60: 1}
left_coset_count: 1019
cosets_by_index: {1: 1, 5: 25, 6: 36, 10: 100, 12: 72, 15: 75, 20: 200, 30: 450, 60: 60}
clique_search_nodes: 171
RESULT: no eight-coset counterconfiguration in A5
```

The finite search completed before the 17:11:46 native-clock observation; no separate completion clock was recorded. Its greedy proper-color upper bound prunes clique branches and was not independently checked by a second implementation. A5 is a concrete nonsolvable test, but the preceding Sun7/no-seven-index observation already gives its result CONDITIONALLY; neither this enumeration nor its output establishes Sun7 or a new nonsolvable extension theorem.

## 6. Remaining scope

This dual lemma is a genuine uniform sufficient bridge with an explicit strong kernel condition. It leaves open arbitrary kernels and arbitrary perfect quotients, including any general `Sun_8(N) + Sun_8(Q) => Sun_8(G)` implication. Original unrestricted Sun8, full proof/primary source of the Sun7 import, novelty, human/kernel/independent-family acceptance and publication remain unpaid. Quarantined historical results are not adopted by the new work; no unaffected-cognition claim is made.
