# Addendum 2 — the projection-size barrier extends to every quasiuniform code law

Observed immediately before writing: `2026-10-23T14:35:42-0700`.

**CANDIDATE, not independently accepted.** This is a strict scope extension of the projection-index argument, not a new bound on gn(R-minus). Read the original candidate (`697c0f33…`) and Addendum 1 (`ca93f70f…`) for the pinned graph and entropy imports I1–I2. All original snapshots remain immutable.

## 1. Statement

Call a finite tuple X=(X_1,...,X_10) **quasiuniform** if every marginal tuple X_A is uniformly distributed on its support. Assume its support satisfies all ten R-minus FDs. If

`Phi(X)=2 sum_v H(X_v)-3H(X_V)<0`,

then, for each of the eight diamond complements Z,

`|support(X_Z)| >= 16`.

No group representation is assumed. The necessary finite-alphabet restriction is not claimed sufficient or sharp, and it does not exclude general uniform winning sets, whose proper marginals need not be uniform. It also does not rule out arbitrarily large quasiuniform counterexamples, so the full guessing-number interval is unchanged.

For group-characterizable laws this reduces to Addendum 1 and retains the effective ambient-group order lower bound 1920 after the **separate** order-120 Ingleton-group import.

## 2. Regularity facts

If X is quasiuniform, then conditioning on a positive-probability value x_Z preserves quasiuniformity of the remaining tuple. Moreover, the support cardinalities of each conditional marginal are independent of x_Z. To see this, both X_Z and (X_A,X_Z) are uniform; the probability of any positive atom x_A given x_Z is their constant probability ratio. The number of such atoms is therefore fixed.

Fix a diamond complement Z and let Omega=support(X_Z), m=|Omega|. X_Z is uniform on this m-point space. For z in Z write

`n_z=|support(X_z)|`, `n_zw=|support(X_z,X_w)|`.

Uniform marginals imply n_z and n_zw divide m: every marginal atom has the same number of preimages in Omega. Every pair has

`I(X_z;X_w)=log(n_z*n_w/n_zw)`,

and `max(n_z,n_w)<=n_zw<=n_z*n_w`.

The deletion-derived inequality (candidate §3, using I1) remains valid for these laws:

`sum_{u!=v} I(X_u;X_v) < H(X_v)/2` if Phi<0.              (2.1)

Consequently no coordinate is constant, and no coordinate is a function of another single coordinate. Thus, for distinct z,w in Z, `n_zw>max(n_z,n_w)`. Also `1<n_z<m`: equality n_z=m would make X_z determine all of X_Z and hence some other coordinate X_w, a contradiction.

## 3. A binary first variable forces Ingleton for a quasiuniform pair

Let (A,B) be quasiuniform and suppose A has at most two values. If A is constant, I(A;B)=0 and Ingleton is immediate. If A has two values, represent the joint support as a biregular bipartite graph with two left vertices. Every right vertex has the same degree, which is either 1 or 2.

- Degree 2 makes the support complete bipartite. Uniformity gives independence, so I(A;B)=0.
- Degree 1 means A is a deterministic function of B. Its entire mutual information is extractable as W=A.

In either case the common-information proof displayed in Addendum 1 §2 gives

`I(A;B|P)+I(A;B|Q)+I(P;Q)-I(A;B)>=0`

for **every** jointly extending pair P,Q; there is no extra uniformity requirement on P,Q for this step.

For a full quasiuniform graph law, apply this argument after fixing the complement of any diamond. If a first-pair coordinate has global alphabet size at most two, its conditional alphabet still has at most two values, so every conditional Ingleton is nonnegative. I2 then contradicts Phi<0.

Every peripheral v in {2,3,4,5,6,7,9,10} appears in the first pair of a listed diamond. Therefore

`n_v>=3` for all eight peripherals.                       (3.1)

This replaces the group-specific non-normality argument. Each diamond complement consists of five peripherals and one hub.

## 4. Excluding m<8 without subgroup theory

For m<=3, a peripheral has no proper divisor n_v with 3<=n_v<m. The same is true for m=4,5,7 (m=4 has only the proper divisor 2). For m=6, every peripheral has n_v=3. Any two have n_vw=6 by divisibility, strictness and n_vw<=9. Thus every peripheral has four other peripheral companions contributing

`4log(3/2) > (1/2)log3`,

contradicting (2.1). This strict inequality is equivalent to `3^8>3*2^8`, which follows already from `3^4>3*2^4` in Addendum 1.

## 5. Index 8: a simpler argument than the group proof

Every peripheral has n_v=4. A pair has n_vw=8, so its mutual information is log2. For any one of the five peripherals, the other four give total mutual information at least4log2, while half its entropy is log2. This violates (2.1). No normalizer or classification of groups of order8 is needed.

## 6. Index 9: an orthogonality-dimension argument

Every peripheral has n_v=3, and any pair has n_vw=9, hence the two coordinates are independent. On the uniform nine-point space Omega, the zero-mean real functions of one three-valued coordinate form a two-dimensional subspace of L2(Omega). Pair independence makes these subspaces orthogonal: E[f(X_v)g(X_w)]=E[f]E[g]=0.

Five peripherals would supply five pairwise orthogonal subspaces of dimension2, ten dimensions in total, inside the zero-mean space L2_0(Omega) of dimension8. This is impossible. This argument replaces the group-specific disjoint-overgroup count and is valid for arbitrary quasiuniform partitions.

## 7. Indices 10 through15

The proofs of Addendum 1 §§6–8 depend **only** on the following properties, all established here:

1. a complement contains five peripherals of alphabet size at least3 and one hub;
2. all six alphabet sizes are proper divisors of m;
3. every pair cardinality is a divisor of m, at most the product, and strictly larger than each individual cardinality;
4. the exact pair information is log(n_v*n_w/n_vw);
5. (2.1).

For clarity, their case conclusions are repeated rather than relying on any group interpretation:

- m=10 or14: all five peripherals have size r=5 or7, pair size2r, and pair information log(r/2). Four companions contradict (2.1).
- m=11 or13: there is no proper nontrivial divisor for an individual coordinate.
- m=12: peripheral sizes are3,4,6. The pair cardinality/information table in Addendum 1 §7 is unchanged. Its strict mutual-information constraints force exactly two size3 peripherals and three size4 peripherals, no size6. The hub can have size2,3,4,6; respectively, size2 has no allowable incomparable pair cardinality with size4, while sizes3,4,6 violate the same mutual-information constraints. All choices fail.
- m=15: there cannot be two distinct size3 coordinates, as their pair cardinality would have to be a divisor of15 larger than3 but at most9. Hence at least four peripherals have size5, their pair cardinality is15, and three companions contribute3log(5/3)>(1/2)log5. Again (2.1) fails.

This exhausts every integer m<16. QED.

## 8. Dependency clarification for the projective-group theorem

The original candidate's prime-field PSL/PGL theorem does **not need I1**. In candidate §4, every coordinate stabilizer H_v contains an Ingleton offender, because every vertex appears in at least one complement Z and each L_Z is offending when Phi<0. For PSL2(p), every proper subgroup is good, so all H_v would have to equal the whole group, making Phi=0. For PGL2(p), the subgroup list puts the unique PSL2(p) inside every offending H_v, collapsing all entropies to the good quotient C2. This is the same written proof with the unnecessary reference to properness from candidate §3 removed.

Thus the projective-group barrier depends on I2 and the specified classical/computational group imports, whereas the index16/effective-order1920 statements retain the I1 dependency. This distinction is useful if the two entropy-import families are reconstructed separately.

## 9. Why the current 2026 spectral source does not silently settle the target

Matveev–Romashchenko, `source-matveev-romashchenko-2602.16536v3.pdf`, SHA-256 `e29579a75d877fd0fdae20e03eef7c75f7fb0deb069b393b55904eff12f0a096`, actually read Theorem A and §§2–3, studies biregular support graphs and proves perturbed Ingleton under spectral control. It is compatible with the quasiuniform setup above, but the graph FDs do not supply the required uniform spectral bound. No unconditional upper-bound improvement is inferred from it.

The expanded group-coding source `source-mao-thill-hassibi-1202.5599v2.pdf`, SHA-256 `9b30beabd51f976c2a412fc86b855c8156c4df7fc6e40f376ef7734a64e1e4f6`, was also read at §§I,III,IV,VIII and AppendixA: it confirms the full uniform coset law, the minimum-order computational import and the caution that ambient Ingleton violation does not by itself construct a valid network code. It does not supply an R-minus bound.

The next load-bearing obligation is still a separate reconstruction of the finite rational entropy identities and this written argument; the proposed coefficient replay is explicitly **not authorized or executed**.
