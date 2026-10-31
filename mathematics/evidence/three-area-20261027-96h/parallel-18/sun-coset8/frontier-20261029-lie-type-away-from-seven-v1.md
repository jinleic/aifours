# Groups of Lie type away from characteristic 7: Sylow overgroups force index collisions

**Status: WRITTEN, with exact finite checks in the author's eval kernel; conditional on the named standard structure theory of finite groups of Lie type; UNREVIEWED.** Let S be a finite simple group of Lie type in characteristic p (Section 2 fixes the conventions; the Tits group ²F4(2)′ is not included). The candidate theorems are:

- **Theorem A (p≥11).** Among any three proper subgroups of S, two have index gcd at least min(p, D(S)) ≥ 10, where D(S) is the cyclotomic value in Table 1. Hence S satisfies Sun_k for every 2≤k≤min(p,D(S)); in particular Sun8(S) holds and S carries no direct P7 configuration. No Sun7, R8 or CFSG input is used.
- **Theorem B (p≠7).** If p≠7 and S≇PSL3(2), no three proper subgroups of S have all pairwise index gcds exactly 7. In particular S carries no direct P7 configuration, i.e. no eight pairwise disjoint left cosets with all 28 index gcds equal to 7.

Theorem B is stated for subgroup families, so it does not need disjointness. PSL3(2)≅GL3(2) is a genuine exception to the three-subgroup form: it has seven distinct index-7 subgroups. Its eight-coset Sun8 property is the separate, still-unreviewed Fano candidate `frontier-20261028-gl32-sun8-geometric-v1.md` SHA `d7c18486c27d7f50d792d57c6ed493f4ceb19c4a8df0c2ff041a59e3ff1c4da0`, and it is not assumed here. Characteristic 7 is **not** covered, and no claim is made for sporadic or alternating groups, arbitrary groups, global Sun8, novelty, formal verification or adoption.

## 1. Provenance and source order

Before any affected earlier source body or successor, read in order the complete pre-source overlays `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`, `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`, and `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. The withdrawn seven-index claim is not used. "Direct P7" means the eight-disjoint-coset condition of §3 of `mathematics/evidence/three-area-20261023-96h/parallel-18/sun-coset8/reduction-and-generation-v1.md` SHA `fa0497ae15bd3c765e05123996e4a94bd8038f2be1488b08dc7111f2fd7602c6`. Its Sun7-relative R8 reduction is prior work and is used only in the optional Corollary of §7.

The owner's 2026-10-28 wide-search preview frontier `frontier-20261028-sun-wide-search-preview-frontier-v1.json` SHA `4ca6a3bb90795334dcd5783463863efe3b194facf1ed92f58f14f44e8689a2e6` is cited as Main requires. Every displayed snippet is NONINPUT. Some displayed paths name older packets on particular Lie-type families; none of their lines, methods or conclusions is used, reconstructed or searched for here. The earlier round's final status retained written-support results for some SL/PSL and Sp/PSp families. The owner knows this only from the safe final-status summary recorded at intake (`startup-v1.json`) and has not reread those results. No priority over them or over the literature is claimed; Lemma 1 below is of a standard kind. This packet's direct lineage is the owner's earlier Sylow-overgroup candidates `frontier-20261028-common-sylow-two-overgroups-sun8-v1.md` SHA `5ca3941781212d47f8408c4a30b01ab622d994c0227b19991f3ffdaaab15b472` and `frontier-20261028-p7-four-sylow-overgroups-v1.md` SHA `78e9394256c0171ce08be0dce7fc6258e30548f70a4089503ffda1ca15217058`, both written before the preview. Neither is an input below. No historical hold, process finding or earlier review is modified.

## 2. Conventions and named imports

S denotes a finite simple group of Lie type: S=O^{p′}(G^F)/Z, where G is simple simply connected over the algebraic closure of F_p and F is a Steinberg endomorphism, with the usual q. For Suzuki and Ree groups this means ²B2(q) with q=2^{2m+1}≥8, ²G2(q) with q=3^{2m+1}≥27, and ²F4(q) with q=2^{2m+1}≥8. A group with several Lie-type descriptions may use any one of them.

The following standard facts are imported at statement level. Their proofs are not replayed. Representative references are Carter, *Simple Groups of Lie Type* (1972), especially the BN-pair and twisted-group chapters; Steinberg, *Lectures on Chevalley Groups* (1967); Carter, *Finite Groups of Lie Type* (1985), order formulas and parabolic/Levi structure; Kleidman–Liebeck (1990) for classical parabolic subgroups; Kleidman (1988) for ³D4; and Malle (1991) for ²F4. Chapter- or section-level locations are as recalled and should be checked by a reviewer.

- **(I1) Split BN-pair with root subgroups.** S has subgroups B=U⋊T and N with T=B∩N normal in N, and W=N/T is a finite Coxeter group whose simple reflections s_α correspond to the simple roots of a (relative) root system Φ. The non-divisible roots α carry root subgroups X_α with these properties: U=∏_{α>0}X_α is a Sylow p-subgroup and T normalizes each X_α; nX_αn^{-1}=X_{w(α)} for n∈N with image w; ⟨X_α,X_{−α}⟩ contains an element of N with image the reflection s_α; S=⟨U,U^-⟩ with U^-=∏_{α<0}X_α; S is the disjoint union of the double cosets BwB, and BwB=UẇTU for any lift ẇ of w; the parabolic subgroups containing B are P_J=⋃_{w∈W_J}BwB for J a set of simple reflections; and ℓ(s_αw)<ℓ(w) if and only if w^{-1}(α)<0.
- **(I2) Orders and indices.** For a proper parabolic P_J with Levi decomposition P_J=U_J⋊L_J, the index [S:P_J]=|G^F|_{p′}/|L_J^F|_{p′} is the value at q of an integer polynomial I_J(x). This follows from the Bruhat count [G^F:P_J^F]=Σ q^{ℓ(w)} over minimal coset representatives in the F-fixed Weyl group, or from the explicit Suzuki–Ree data. The order polynomials Π_G(x)=|G^F|_{p′} and the Levi p′-orders are those in §4. For untwisted types, Chevalley's factorization gives W(x):=Σ_{w∈W}x^{ℓ(w)}=∏_i(x^{d_i}−1)/(x−1) over the degrees d_i of W, and I_J=W/W_J. The largest degree of an irreducible Weyl group is its Coxeter number h, and h=ht(θ)+1 for the highest root θ.

No classification of finite simple groups, maximal-subgroup list, Jordan/Jones/Nagura theorem or Sun7 statement is used in Sections 3–6.

## 3. Lemma 1: overgroups of a Sylow p-subgroup lie in proper parabolics

**Lemma 1.** If U≤H<S, then H≤P_J for a proper set J of simple reflections. Consequently every proper subgroup of index prime to p is contained in a conjugate of a proper parabolic subgroup, and its index is divisible by the index of some maximal parabolic subgroup.

*Proof.* (i) If h∈H∩BwB, write h=uẇtu′ with u,u′∈U and t∈T. Since U≤H, ẇt=u^{-1}hu′^{-1}∈H∩N. Hence W_H:={w: H∩BwB≠∅} is the image of H∩N in W, a subgroup, and H⊆U(H∩N)U.

(ii) Let J=W_H∩{simple reflections}. Then W_J≤W_H. Suppose W_H≠W_J and choose w∈W_H∖W_J of minimal length, with a simple reflection s=s_α satisfying ℓ(sw)<ℓ(w). By (I1), w^{-1}(α)<0. Take n∈H∩N mapping to w. Then n^{-1}X_αn=X_{w^{-1}(α)}≤H, because X_α≤U≤H. Put β=−w^{-1}(α)>0. Since X_β≤U≤H, the group ⟨X_β,X_{−β}⟩≤H contains an element of N mapping to s_β, so s_β∈W_H. Now ws_βw^{-1}=s_{w(β)}=s_{−α}=s, hence sw=ws_β∈W_H. Minimality gives sw∈W_J, and s=(sw)w^{-1}∈W_H. Thus s∈J and w=s(sw)∈W_J, a contradiction. Therefore W_H=W_J.

(iii) By (i) and (ii), H⊆⋃_{w∈W_J}BwB=P_J. If J were all simple reflections, then W_H contains the longest element w_0. A lift n_0∈H∩N would satisfy n_0Un_0^{-1}=U^-≤H, so H⊇⟨U,U^-⟩=S. Hence J is proper. A subgroup of p′-index contains a Sylow p-subgroup U^g, so its g-conjugate contains U and lies in a proper P_J, which is contained in a maximal parabolic P_{J′}. Indices multiply along P_J≤P_{J′}. □

## 4. Lemma 2: a cyclotomic factor common to all maximal parabolic indices

**Table 1.** Φ_e denotes the e-th cyclotomic polynomial.

| S | D(S) |
|---|---|
| A_n(q), n≥1 | Φ_{n+1}(q) |
| B_n(q), C_n(q), n≥2 | Φ_{2n}(q) |
| D_n(q), n≥4 | Φ_{2n−2}(q) |
| G2(q) / F4(q), E6(q) / E7(q) / E8(q) | Φ_6(q) / Φ_12(q) / Φ_18(q) / Φ_30(q) |
| ²A_{m−1}(q)=PSU_m(q), m≥3 odd | Φ_{2m}(q) |
| PSU_m(q), m≥4 even | Φ_{2(m−1)}(q) |
| ²D_n(q)=PΩ^-_{2n}(q), n≥4 | Φ_{2n}(q) |
| ³D4(q) / ²E6(q) | Φ_12(q) / Φ_18(q) |
| ²B2(q) / ²G2(q) / ²F4(q) | q²+1 / q³+1 / Φ_12(q) |

**Lemma 2.** D(S) divides [S:P] for every proper parabolic subgroup P. With Lemma 1, D(S) divides [S:H] for every proper subgroup H of index prime to p.

*Proof.* By §3 it suffices to treat maximal parabolics P_J. In each case below, Φ_e(x) divides Π_G(x) but is coprime in Q[x] to the Levi p′-order Π_L(x). Since Π_G=I_J·Π_L with I_J∈Z[x], Φ_e divides I_J in Q[x], hence in Z[x] by Gauss's lemma (Φ_e is monic), and so Φ_e(q) divides I_J(q)=[S:P_J].

*Untwisted types.* Here Π_G=(x−1)^nW(x), Π_L=(x−1)^nW_J(x) and I_J=W/W_J. The Coxeter number h is the largest degree, so Φ_h divides x^h−1 and hence W. Every irreducible component K of a proper J has highest root θ_K≠θ, because θ has full support; thus its Coxeter number is ht(θ_K)+1≤ht(θ)<h. All degrees of W_J are therefore smaller than h, while Φ_h divides x^d−1 only when h divides d. Hence Φ_h is coprime to W_J.

*PSU_m(q).* Π_G=∏_{c=2}^m(x^c−(−1)^c). The maximal parabolic stabilizing a totally isotropic k-space, 1≤k≤⌊m/2⌋, has Levi p′-order ∏_{c=1}^k(x^{2c}−1)·∏_{c=2}^{m−2k}(x^c−(−1)^c) if 2k<m, and (x−1)∏_{c=2}^{k}(x^{2c}−1) if 2k=m. If m is odd, Φ_{2m} divides x^m+1. It divides x^{2c}−1 only when m|c, and divides x^c±1 for c≤m−2 never. If m≥4 is even, Φ_{2(m−1)} divides x^{m−1}+1. It divides x^{2c}−1 only if (m−1)|c, impossible for c≤m/2, and it divides no x^c±1 with c≤m−2.

*PΩ^-_{2n}(q), n≥4.* Π_G=(x^n+1)∏_{c=1}^{n−1}(x^{2c}−1). The maximal parabolic of a totally singular k-space, k≤n−2, has Levi p′-order (x−1)∏_{c=2}^k(x^c−1)·(x^{n−k}+1)∏_{c=1}^{n−k−1}(x^{2c}−1); for k=n−1 it is (x²−1)∏_{c=2}^{n−1}(x^c−1). Φ_{2n} divides x^n+1, but no x^c−1 with c<2n and no x^{n−k}+1 with 0<n−k<n.

*³D4(q).* Π_G=(x²−1)(x⁸+x⁴+1)(x⁶−1), and Φ_12 divides x⁸+x⁴+1=(x^{12}−1)/(x⁴−1). The two maximal parabolics, for the F-orbits {α_2} and {α_1,α_3,α_4}, have Levi p′-orders (x²−1)(x³−1) and (x⁶−1)(x−1). The indices are (x³+1)(x⁸+x⁴+1) and (x+1)(x⁸+x⁴+1).

*²E6(q).* Π_G=(x²−1)(x⁵+1)(x⁶−1)(x⁸−1)(x⁹+1)(x^{12}−1), and Φ_18 divides x⁹+1. Removing one F-orbit from {1,6},{3,5},{4},{2} gives maximal Levis of types ²A5, A2(q²)A1(q), A1(q²)A2(q) and ²D4. Their p′-orders are, respectively, (x−1)(x²−1)(x³+1)(x⁴−1)(x⁵+1)(x⁶−1); (x−1)(x²−1)(x⁴−1)(x⁶−1); (x−1)(x+1)(x⁴−1)(x²−1)(x³−1); and (x−1)(x+1)(x²−1)(x⁴−1)(x⁴+1)(x⁶−1). None is divisible by Φ_18, which divides x^d−1 only for 18|d and x^d+1 only for d an odd multiple of 9.

*Suzuki–Ree.* For ²B2(q) and ²G2(q), B is the only maximal parabolic, with index q²+1 and q³+1 respectively. For ²F4(q), Π_G=(x⁶+1)(x⁴−1)(x³+1)(x−1). The Levi p′-orders of types ²B2(q)×(q−1) and SL2(q)×(q−1) are (x²+1)(x−1)² and (x²−1)(x−1). Φ_12 divides x⁶+1=(x²+1)Φ_12 and is coprime to both Levi orders. □

The author's checker `frontier-20261029-lie-parabolic-index-check-v1.py` SHA `a795f85ff8fd7dd116fe52f628341e8f4578f00e1f419af17baac7cb8c1582e7`, 8809 bytes, ran in the author's eval kernel on 2026-10-29. It verified by exact integer-polynomial division that each displayed Levi p′-order divides Π_G and that Φ_e divides each quotient. Coverage was all maximal parabolics of G2, F4, E6, E7 and E8; A_n for n≤20; B_n and C_n for n≤15; D_n for 4≤n≤15 (589 index polynomials in all); ³D4, ²E6, ²F4, ²B2 and ²G2; PSU_m for 3≤m≤20; and PΩ^-_{2n} for 4≤n≤16 (226 index polynomials). This is a finite consistency check of the displayed formulas, not a replacement for the general-rank arguments above or for the imported structure theory.

## 5. Lemma 3: when D(S) can divide 7

**Lemma 3.** D(S)∉{1,7} except for S=PSL3(2) (D=Φ_3(2)=7) and the seven groups PSL6(3), Ω7(3), PSp6(3), PΩ_8^+(3), G2(3), PSU3(3), PSU4(3) (D=Φ_6(3)=7).

*Proof.* The Suzuki–Ree values are at least 65. For e≥2, Φ_e has constant term 1, so Φ_e(q)≡1 (mod q). Also Φ_e(q)≥2: for q≥3, |q−ζ|≥q−1 gives Φ_e(q)≥(q−1)^{φ(e)}≥2, and for q=2, |2−ζ|>1 for every root of unity ζ≠1. If Φ_e(q)=7 then q divides 6, so q∈{2,3}.

For q=3, 7≥2^{φ(e)} forces e∈{2,3,4,6}, with values 4, 13, 10, 7. For q=2 write Φ_e(2)=2^{φ(e)}∏_{d|e}(1−2^{−d})^{μ(e/d)}. Discarding the factors with μ=−1, which exceed 1, gives Φ_e(2)≥2^{φ(e)}∏_{d≥1}(1−2^{−d})≥2^{φ(e)}·(21/64)(7/8)>0.28·2^{φ(e)}. So φ(e)≤4, i.e. e∈{2,3,4,5,6,8,10,12}, with values 3,7,5,31,3,17,11,13. Table 1 has e=3 only for A_2. It has e=6 exactly for A5, B3, C3, D4, G2, PSU3 and PSU4. □

The checker independently confirms that among all e occurring in Table 1 for the ranges tested and all prime powers q<2000, Φ_e(q)∈{1,7} occurs only for (e,q)=(3,2),(6,3).

## 6. Proofs of Theorems A and B

**Theorem A.** Let p≥11, so q≥11 and D(S)≥(q−1)^{φ(e)}≥10 (or ≥65 in the Suzuki–Ree rows, which do not occur here). Of any three proper subgroups, two have indices both divisible by p or both prime to p. In the first case their gcd is at least p. In the second, Lemma 2 makes D(S) divide both. Thus some gcd is at least min(p,D(S))≥10>7. If 3≤k≤min(p,D(S)), every family of k disjoint cosets therefore has a pair with gcd≥k; Sun_2 holds since disjoint cosets cannot have coprime indices. Taking k=8 gives Sun8. A direct P7 configuration would contain three subgroups with pairwise index gcd 7. □

**Theorem B.** Let p≠7 and S≇PSL3(2). For proper subgroups H_1,H_2 of p′-index, Lemma 1 gives maximal parabolics M_1,M_2 (possibly of the same type) with [S:M_i] dividing [S:H_i]. Hence g=gcd([S:M_1],[S:M_2]) divides gcd([S:H_1],[S:H_2]). Outside the seven q=3 groups, D(S) divides g and D(S)∤7 by Lemma 3, so the gcd is not 7. For the seven groups the maximal parabolic indices, from the polynomials of §4 at q=3, are:

| S | maximal parabolic indices | all pairwise gcds g (incl. equal types) |
|---|---|---|
| PSL6(3) | 364, 11011, 33880, 11011, 364 | 28, 91, 364, 847, 11011, 33880 |
| Ω7(3), PSp6(3) | 364, 3640, 1120 | 28, 280, 364, 1120, 3640 |
| PΩ_8^+(3) | 1120, 36400, 1120, 1120 | 560, 1120, 36400 |
| G2(3) | 364, 364 | 364 |
| PSU3(3) | 28 | 28 |
| PSU4(3) | 280, 112 | 56, 112, 280 |

No listed g divides 7, so again gcd([S:H_1],[S:H_2])≠7. Consequently a family of proper subgroups with all pairwise index gcds exactly 7 contains at most one subgroup of p′-index. It also contains at most one of index divisible by p, because two such would have gcd divisible by 7p. Hence it has at most two members. □

The table values and gcds were computed exactly by the same checker; the general statement does not depend on any other enumeration.

## 7. Optional corollary and exact boundary

Assume the prior arbitrary-group Sun7 statement at its named written-composition scope, `institute/runs/six-lane-2026-10-18-96h/review/sun7-complete-written-composition-parent-verdict-v1.md` SHA `94abd506aec9879e294a5eb84129794af0c7ac78917b091d2f2c113d665c34f2`, and the prior R8 implication. The R8 argument is rechecked in `frontier-20261028-simple-seven-prime-support-v1.md` SHA `815c9e2374a96858f7bfd609aca9f592f293fb14a1822e774333dc41c4eb2faf`, §5; the full Sun7 proof DAG is not replayed. Then every finite simple group of Lie type of characteristic 2, 3 or 5, other than PSL3(2), satisfies Sun8, since a Sun8 counterconfiguration would be a direct P7 configuration. For characteristic at least 11, Theorem A gives Sun8 without these assumptions.

What remains outside this packet: Lie-type groups of characteristic 7; PSL3(2), covered only by the separate Fano candidate; and all non-Lie-type simple groups. No unrestricted Sun8 or P7 theorem follows.

A disjoint reviewer should attack the root-subgroup descent in Lemma 1, including the minimal-length step and the use of relative roots for twisted and Suzuki–Ree groups. They should also check the Levi p′-orders and F-orbit lists in Lemma 2, the cyclotomic coprimality claims and Gauss-lemma step, the q=2 product bound in Lemma 3, and the q=3 table. The proofs of the structure-theory imports were not replayed. No external human or model review, formal proof, priority search, novelty claim or historic-hold rehabilitation is made.
