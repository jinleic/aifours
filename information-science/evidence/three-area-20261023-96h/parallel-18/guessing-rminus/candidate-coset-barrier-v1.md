# Candidate: localization barriers for non-normal group codes on R-minus

Observed immediately before this snapshot: `2026-10-23T14:12:32-0700`.

**Status: CANDIDATE — written derivation, awaiting separate reconstruction.** No scientific executable check has run in this slot. This is a scoped construction barrier, not a new unrestricted numerical bound and not a solution of gn(R-minus). The interval remains `20/3 <= gn(R-minus) <= 1847/276`. Novelty is UNCLEAR.

## 1. Exact claims

Let G be any finite group and H_1,...,H_10 any subgroups, not assumed normal, with

`intersection_{u in N(v)} H_u <= H_v` for every v of the fixed graph in `inputs-v1.json`.

Write K=intersection_v H_v and form the **full uniform coset code**

`C(G;H) = { (gH_1,...,gH_10) : g in G }`.

Let X be uniform on C, equivalently use a uniform g in G. Then

`H(X_A)=log [G:intersection_{v in A} H_v]`,

`Phi(X)=2 sum_v H(X_v)-3H(X_V)`.

The new claims are:

**A. Small effective-group barrier.** If `Phi(X)<0`, then

`|G / core_G(K)| >= 960`.

Thus every such code with effective ambient group of order **strictly less than 960** obeys

`[G:K]^3 <= product_v [G:H_v]^2`.

The number 960 is an exact necessary threshold from the proof, **not claimed tight**. No witness at 960 is given, and no lower bound on |C| is asserted by this group-order statement.

**B. Prime-field projective barrier.** For every prime p and every choice of all ten subgroups in either

`G=PSL(2,p)` or `G=PGL(2,p)`,

the same inequality holds:

`[G:K]^3 <= product_v [G:H_v]^2`.

In particular **none** of the familiar Ingleton-violating groups PGL(2,p), p>=5, with any ten-subgroup placement satisfying all R-minus FDs, yields a uniform coset code beating 20/3, including through the previously reviewed triangle-balancing procedure.

These claims cover independent Cartesian products of the specified FD-consistent codes, coordinatewise injective relabellings, harmless alphabet enlargement and multiplication by parity codes on graph triangles. They do **not** cover arbitrary subgroups of products of ambient groups, arbitrary reweightings or subsets of C, nonuniform mixtures, prime-power q not prime, or unrestricted nonlinear codes. Every application must preserve the stated full uniform coset law and the exact FDs.

## 2. Imports and trust boundary

All input identities and source bytes are pinned in `inputs-v1.json`.

### I1. Existing deletion certificates, not a new claim

The earlier dossier records, for every vertex v, the following inequality on FD-consistent polymatroids of the induced graph R-minus minus v:

`3 h(V-minus-v) <= 2 sum_{u!=v} h(u)`.

Its exact rational coefficients are in `evidence/certs/avg-ratio-9vertex.json` under the prior dossier; `code/avg_ratio_certs.py` defines the Shannon-row order, nine-vertex masks, FD rows and signs. This is an internal finite coefficient identity, not an external theorem and not a newly replayed certificate. Its recorded `identity_exact` flags are not independent verification by this slot. A fresh independent reconstruction of this import is part of the acceptance boundary for Claim A and the antichain lemma below.

### I2. Existing single-diamond identities, not a new claim

For each of the following eight quadruples `(U,V;P,Q)`, put Z=V(graph) minus {U,V,P,Q} and define

`J(U,V;P,Q | Z) = I(U;V|Z,P)+I(U;V|Z,Q)+I(P;Q|Z)-I(U;V|Z)`.

The quadruples are

`(2,4;1,3), (2,6;1,7), (3,5;1,4), (5,7;1,6),`

`(3,10;4,8), (4,9;3,8), (6,10;7,8), (7,9;6,8)`.

The prior exact rational certificates give, on the graph FDs,

`Phi = J + 3 S`, where S is a nonnegative linear combination of elemental Shannon terms.

For example, the complete raw certificate `diamond_3_10_4_8.json` was read; its singleton weights are all 2/3, its J multiplier is 1/3, and its ten FD multipliers are -1/3. `S-explicit-diamond-3-10-4-8.json` gives the 155 named Shannon summands. These finite identities can be checked by expanding conditional mutual information into subset entropies. No reliance on a floating LP optimum is needed. They have **not** been executable-replayed here.

For Claim B only the disjoint quadruples `{1,2,3,4}` and `{6,7,8,9}` are needed, through `diamond_2_4_1_3.json` and `diamond_7_9_6_8.json`. Their complements cover all ten vertices. The precise orientation of J above matters; a transposed Ingleton convention is not substituted.

### I3. Standard finite-group facts

- Every group of order below 120 satisfies the subgroup Ingleton inequality. Mao–Hassibi, [arXiv:0910.1335v1](https://arxiv.org/pdf/0910.1335v1), §§III–IV, is the primary computer-assisted source; Craven, [arXiv:2505.22565v1](https://arxiv.org/pdf/2505.22565v1), introduction and §5, supplies a later confirming classification. This is a **published/reported finite computational import**, not our own exhaustive certificate or a formal proof. Claim A explicitly inherits it. For Claim B it is used only for A4, S4, A5 and groups smaller than these.
- Metacyclic groups satisfy Ingleton: Craven Theorem 1.1, with its written proof in §3. A metacyclic group has a cyclic normal subgroup and cyclic quotient; subgroups of one are metacyclic by intersection with the cyclic normal subgroup. We do not import the older incorrect general nilpotent proof.
- The subgroup types for PGL(2,q), q odd, are Cameron–Omidi–Tayfeh-Rezaie, [EJC 13 (2006), R50](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v13i1r50/pdf/), Theorem 2, pp.3–4, actually read. At q=p prime every subgroup is cyclic, dihedral (including V4), Cp semidirect Cd, one of A4/S4/A5, the unique PSL(2,p), or PGL(2,p). The only elementary-abelian p-subgroup is Cp, and there are no proper subfield groups. We use only this exhaustive **type** statement, not the OCR-degraded congruence/count formulas. For PSL(2,p), the corresponding proper-subgroup list is also stated as Dickson's theorem in Nachman, [arXiv:1210.2073](https://arxiv.org/pdf/1210.2073), Theorem 1, pp.1–2, actually read.

The proof below does not import Craven's more delicate normal-subgroup reduction theorem; in particular it makes no inference from a merely nontrivial intersection with a normal subgroup.

## 3. An entropy consequence: a Phi-negative law has no comparable coordinates

This step applies to **any** finite FD-consistent distribution, not just group codes.

Fix a vertex v and condition on Y=X_v. For every y of positive probability, the remaining nine coordinates satisfy exactly the FDs of the induced graph with v deleted: where v was a decoder input it has become a fixed parameter. Apply I1 to each conditional law and average:

`3 H(X_{V-minus-v}|Y) <= 2 sum_{u!=v} H(X_u|Y)`.

Using the entropy chain rule gives the complete inequality

`Phi(X) >= 2 sum_{u!=v} I(X_u;X_v) - H(X_v)`.                 (3.1)

Indeed, the right side equals

`2 sum_{u!=v} H(X_u) - 2 sum_{u!=v} H(X_u|Y) - H(Y)`,

while `H(X_V)=H(Y)+H(X_{V-minus-v}|Y)` gives (3.1) after the displayed conditional bound.

Consequences:

1. If X_v is constant, then Phi>=0.
2. If X_v is a function of any other single coordinate X_u, then I(X_u;X_v)=H(X_v), so Phi>=H(X_v)>=0.
3. If Phi<0, then every coordinate is nonconstant and, for every v,

   `sum_{u!=v} I(X_u;X_v) < H(X_v)/2`.

For a uniform group code, `H_u <= H_v` makes X_v a deterministic function of X_u. Therefore Phi<0 implies that all ten H_v are proper subgroups of G and are **pairwise incomparable** under inclusion. This is stronger than merely asking for non-normal coordinate subgroups.

## 4. Exact localization of a conditional Ingleton violation

For a diamond quadruple D and complement Z, write

`L_Z=intersection_{z in Z} H_z`, and `A_i=L_Z intersection H_i` for i in D.

Fix any attainable value x_Z. Its preimage in G is a left coset g0 L_Z: two group elements have the same observed cosets exactly when their quotient lies in every H_z. Conditional on x_Z, a uniform g is therefore uniform on g0 L_Z. Left multiplication by g0 and the identification of each coordinate's possible cosets induce bijections, so its four-variable conditional entropy profile is precisely

`h_Z(A)=log [L_Z:intersection_{i in A} A_i]`.

The profile is independent of the attained x_Z. Consequently, `J(D|Z)` is the ordinary Ingleton expression of the four subgroups A_U,A_V,A_P,A_Q inside L_Z.

By I2, if Phi<0, then `J(D|Z)<0` for **every** listed diamond. Hence every L_Z is an Ingleton-violating group. By I3,

`|L_Z| >= 120`.                                               (4.1)

Also, for every vertex z there is a listed complement Z containing z. Since L_Z<=H_z, each H_z must itself contain an Ingleton offender. This localizes the obstruction inside the coordinate stabilizers, not merely inside the ambient G.

## 5. A subgroup-interval lemma

**Lemma.** Let L<G be finite groups. If there are six pairwise incomparable groups H with `L<H<G`, then `[G:L]>=8`.

**Proof.** Suppose m=[G:L]<8. An intermediate group's relative order [H:L] is a nontrivial proper divisor of m. Thus prime m and m=1 allow none; only m=4 or m=6 need consideration.

For any H with [H:L]=2, L is normal in H, so H<=N_G(L). Let N=N_G(L).

- If m=4 and N<G, then [N:L] is 1 or 2, so at most one such H exists. If N=G, then G/L has order 4, with at most three proper nontrivial subgroups (the V4 case). Hence at most three intermediate groups exist.
- If m=6, intermediate groups have relative order 2 or 3. There is at most one of relative order 3: two distinct such groups would be distinct index-two subgroups of G, with intersection of index 4; since L lies in that intersection, 4 would divide 6, impossible. For relative order 2, if N<G then [N:L] is 1,2 or 3, so at most one exists. If N=G, the quotient has order 6 and has at most three subgroups of order 2 (cyclic or S3). Thus there are at most three of relative order 2 and at most one of relative order 3, four in total.

Neither case allows six incomparable intermediate groups. QED.

This is a written finite-group argument, **not an enumeration**.

## 6. Proof of Claim A

Assume Phi<0. Choose any listed diamond D, for example `(3,10;4,8)`, and let L=L_Z.

Section 3 makes the six groups H_z, z in Z, pairwise incomparable proper subgroups of G. They all contain L. The containments are strict: if L=H_z for one z, then H_z<=H_w for each of the other five w, contradicting incomparability. The interval lemma therefore gives `[G:L]>=8`. Section 4 gives |L|>=120. Multiplication yields

`|G|=[G:L]|L| >= 8*120 = 960`.

For the effective-order statement let N=core_G(K)=intersection_{g in G} gKg^{-1}. This is normal in G and contained in every H_v. Replace G,H_v by G/N,H_v/N. All intersections, FD inclusions, coset cardinalities and entropies are unchanged, and the quotient still has Phi<0. Applying the result just proved to that quotient gives `|G/N|>=960`. QED.

## 7. Proof of Claim B

Call a group Ingleton-good if all quadruples of its subgroups satisfy the subgroup Ingleton inequality. This property is inherited by subgroups. If G itself is Ingleton-good, then every L_Z is good and I2 already forces Phi>=0.

For p>=5, Dickson's list and I3 show that **every proper subgroup of PSL(2,p) is Ingleton-good**: the cyclic, dihedral and Cp semidirect Cd types are metacyclic, and A4/S4/A5 have order at most 60. If a PSL coset code had Phi<0, Section 3 would make each H_v proper; Section 4 would make each H_v contain an offender. This contradicts the proper-subgroup statement. Thus Phi>=0 for G=PSL(2,p).

Now let G=PGL(2,p) and N=PSL(2,p). At p>=5, the full PGL subgroup list says every subgroup **not containing N** is metacyclic or isomorphic to A4, S4 or A5; hence it is Ingleton-good. This does **not** say N is good: PSL(2,11), for example, is an Ingleton violator in Craven's table.

Suppose Phi<0. For every diamond, its offending L_Z cannot be good, so it must contain N. Use specifically D_a={1,2,3,4} and D_b={6,7,8,9}. Their complements Z_a,Z_b cover V. Therefore N<=H_v for every v. All coordinates factor through G/N=C2. Intersections and entropies are exactly those for subgroups H_v/N of C2, an abelian and hence Ingleton-good group. This contradicts the conditional violation from Section 4. Thus Phi>=0 also for PGL.

For p=2 and p=3 the groups have order below 120 (PSL2(2)=S3, PSL2(3)=A4, PGL2(2)=S3, PGL2(3)=S4), so they are good by I3. This covers every prime. QED.

## 8. Conversion back to coding, and nonclaims

Uniformity gives `H(X_V)=log |C|=log[G:K]` and `H(X_v)=log[G:H_v]`. Thus Phi>=0 is exactly the displayed integer cardinality inequality. For a declared common alphabet of size s with all [G:H_v]<=s, it implies |C|^3<=s^20 and hence log_s|C|<=20/3. For unequal alphabets it says the strict aggregate test needed for triangle-balancing cannot hold.

Phi adds under independent Cartesian products. A parity code on a triangle has Phi=0. These facts give the closure claims in §1, but no closure under arbitrary restrictions or correlations is asserted. In particular an arbitrary subgroup of PGL2(p)^r is **not** an independent Cartesian product of the codes just excluded.

This barrier differs from the earlier unpromoted normal-kernel/homomorphism argument: all ten coordinate subgroups here may be non-normal, and PGL2(p) is itself Ingleton-violating. The new work is the graph-specific conditional localization, the antichain/interval amplification and the socle-collapse application. The group Ingleton results and all entropy certificates remain explicit imports.

**Scientific effect:** it rules out a natural family suggested by the prior dossier and gives a representation-independent small-effective-group exclusion, but does not improve 20/3 or 1847/276. The unrestricted problem, nonuniform reweightings and larger/more complicated group actions remain open here. Significance is a modest specialist barrier unless stronger consequences emerge; priority is not cleared by the bounded search.
