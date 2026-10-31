# f170 independent same-harness scientific review — review-v1

- Wave: `f170-sun8-sylow-overgroup-and-small-index`
- Manifest: `manifest-v1.json` SHA-256 `f1d49cf6eb5e8c52b4b551ad4f3b6f924105e2cdfe068f9a69ceb4140d6ac128` (verified Thu Oct 29 06:54:14 PDT 2026, then read in full)
- Reviewer: `ReviewF170Sun8Sylow` (same-harness subagent); author `MathSun8-2` was not contacted
- Observed native clock immediately before creating this file: `Thu Oct 29 07:52:10 PDT 2026`
- Capacity pause: received about 07:44–07:45 PDT. After it I did only status hashing (07:45:11). I resumed on Main's instruction and the parent file `parent-capacity-resume-v1.json` SHA-256 `02504ae6b8a6304cedec9128b34223b735e8ae84b38092a294441e8975b7678d`; that file sits in this directory, and I hashed it but did not otherwise use it. I ran no computation after the pause.

## 0. Scope and limits

The scope is exactly the manifest scope:
- (a) the elementary classification candidate: a nonabelian simple group with a subgroup of index ≤7 is A5, A6, A7 or GL3(2);
- (b) direct P7 with μ≥8 forces every Sylow p-subgroup (p>7) into ≥4 distinct maximal overgroups;
- (c) μ≥8 plus a prime p>42 whose Sylow subgroup has ≤2 actual maximal overgroups gives Sun8 without Sun7.

Here μ(G) is the minimum index of a proper subgroup.

This review has the following limits:
- It is a same-harness review. It is not human review, independent-model-family review, formal/kernel verification, or novelty/priority review.
- Author statements such as "PASS", "self-contained" or "the eval kernel listed…" are not used as evidence.
- The review adopts nothing and composes no result. It changes no hold.
- I did not access any f161 or f162 material. Main sent two status-only controls about them, and neither was relevant to this wave.

## 1. Inputs, read completely in the declared order

I verified every byte count, LF count and SHA-256 at 06:54:34 PDT, before interpreting anything. Each file was read in full with exact `:raw` reads. All files end in LF. The three overlay JSONs were parsed completely with my own code, giving 69, 9 and 8 leaves respectively.

| # | Role | File (under `mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/`) | SHA-256 | Bytes | LF |
|---|---|---|---|---|---|
| 1 | mandatory overlay 1 | `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` | `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` | 6883 | 56 |
| 2 | mandatory overlay 2 | `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` | `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04` | 3056 | 11 |
| 3 | mandatory overlay 3 | `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` | `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218` | 3164 | 10 |
| 4 | small-index candidate | `frontier-20261028-simple-small-index-elementary-v1.md` | `b38eb77160a4bb4a507e32c8afc7a99c1591affcaace761f0aeabf7c02fce576` | 10570 | 53 |
| 5 | P7 four overgroups | `frontier-20261028-p7-four-sylow-overgroups-v1.md` | `78e9394256c0171ce08be0dce7fc6258e30548f70a4089503ffda1ca15217058` | 5705 | 39 |
| 6 | common Sylow, two overgroups | `frontier-20261028-common-sylow-two-overgroups-sun8-v1.md` | `5ca3941781212d47f8408c4a30b01ab622d994c0227b19991f3ffdaaab15b472` | 6185 | 47 |

**How the overlays bear on the candidates.** Overlay 1 corrects two inequalities in alternating-family packets. Overlays 2 and 3 withdraw the false claim that A7 has no seven proper-subgroup indices with pairwise gcd 7. Overlay 3 also requires the seven-index assertion and the eight-disjoint-coset assertion to be kept separate, and forbids inferring a source-specific P7 definition from its name. I checked each candidate against this:
- None of the three candidates uses the corrected inequalities or the withdrawn claim.
- Candidate (a) lists A7 among the groups that have an index-7 subgroup, so it is consistent with the counterexample in overlays 2–3.
- Candidate (b) states its hypothesis explicitly as eight pairwise disjoint left cosets with all pairwise index gcds exactly 7. I review that explicit statement (§4).

**Not read** (all outside the manifest; no conclusion here depends on their content):
- the P7 definition source `mathematics/evidence/three-area-20261023-96h/parallel-18/sun-coset8/reduction-and-generation-v1.md` (SHA `fa0497ae…`);
- the three inputs of the small-index candidate's §5 Sun8 corollary:
  - `frontier-20261028-source-free-support-consolidated-v1.md` (`eefaac64…`);
  - `frontier-20261028-alternating-small-written-sun8-v1.md` (`cb2c2ae8…`);
  - `frontier-20261028-gl32-sun8-geometric-v1.md` (`d7c18486…`);
- the predecessor packet `frontier-20261028-common-sylow-triple-p7-sun8-v1.md` (`4ce24ffd…`);
- every file in overlay 1's binding inventory, the all-degree and small-degree alternating packets, and the f116/f81 reviews.

Historical statements in the candidates about these files (for example "that packet gave p>168") are unverified here.

## 2. Verdicts

| Claim | Verdict | F/M/m |
|---|---|---|
| (a) Every finite nonabelian simple group with a proper subgroup of index ≤7 is ≅ A5, A6, A7 or GL3(2), by elementary means | **WRITTEN_SUPPORTED** | 0/0/0 |
| (a′) Small-index candidate §5 and opening paragraph: conditional Sun8 for all nonabelian simple groups with at most two prime divisors >7 | **INCONCLUSIVE**: depends on three unreviewed inputs outside the manifest | not assessed |
| (b) Explicit hypothesis below, with μ(G)≥8 ⇒ every Sylow p-subgroup (p>7, p dividing \|G\|) lies in ≥4 distinct maximal proper subgroups (≥5 if p divides no index) | **WRITTEN_SUPPORTED** for the explicitly stated hypothesis. Equivalence with the source-specific "direct P7" definition: **INCONCLUSIVE** (not reviewed) | 0/0/0 |
| (c) μ(G)≥8, p>42 dividing \|G\|, Sylow p in ≤2 actual maximal proper subgroups ⇒ Sun8; also p>7 with ≤1 overgroup ⇒ Sun8; no Sun7/R8 | **WRITTEN_SUPPORTED** | 0/0/1 (m1, wording) |

**Totals: FATAL 0, MAJOR 0, MINOR 1.**

## 3. Claim (a): independent reconstruction

**(a1) Reduction to A7.**
- Let H<S be proper of index m. The kernel of S acting on S/H is core_S(H), a proper normal subgroup, so it is trivial and the action is faithful.
- Composing with the sign map gives a normal subgroup of index ≤2. By simplicity it is all of S, so the image lies in A_m.
- For m≤4, S would embed in the solvable group A_m, which is impossible.
- So m∈{5,6,7}, and S embeds in A_m ≤ A7 (via point stabilizers). Correct.

**(a2) Degree ≤6, so |S| divides 360.**
- If 5∤|S|, then |S| divides 72. S is not a p-group, so 6 divides |S|.
  - n₃ divides 8 and n₃≡1 (mod 3), so n₃∈{1,4}.
  - n₃=1 gives a normal Sylow 3-subgroup.
  - n₃=4 gives a nontrivial, hence faithful, conjugation action into the solvable group S4.
  - Both are impossible, so 5 divides |S|.
- n₅ divides |S|/5, which divides 72, and n₅≡1 (mod 5), so n₅∈{6,36}. Hence 30 divides |S|.
- Orders 90, 120 and 180 would give subgroups of the simple group A6 of index 4, 3 and 2. A6 would then act nontrivially and faithfully on at most 4 points, which is impossible since 360>24.
- Order 30: n₅=6 gives 24 elements of order 5. n₃=10 would add 20 more, and 44>29.
- So |S|∈{60,360}. Order 360 gives S=A6.

**(a3) Order 60 implies S ≅ A5.**
- n₅=6 and n₃=10 (n₃=4 would give an embedding into S4). That accounts for 44 nonidentity elements and leaves 15.
- n₂∈{5,15}: n₂=1 gives a normal subgroup, and n₂=3 gives an embedding into S3.
- n₂=5 gives a faithful action into S5 whose image has order 60, hence the unique index-2 subgroup A5. (That S5 has a unique index-2 subgroup is used implicitly; it is elementary.)
- n₂=15:
  - Cyclic C4 Sylow subgroups would need 30 elements of order 4, more than the 15 left, so the Sylow 2-subgroups are V4.
  - An involution x has |C(x)| ∈ {4,12,20}.
  - |C(x)|=20 gives a class of size 3 and an embedding into S3, which is impossible.
  - |C(x)|=12 gives a class of size 5, hence S≅A5.
  - If every centralizer has order 4, each involution lies in exactly one Sylow 2-subgroup (an abelian Sylow containing x lies in C(x)), giving 45 involutions, more than 15.
- The argument is correct and complete.

**(a4) Degree 7.**
- 7 divides |S|, and P=⟨7-cycle⟩. N_{S7}(P)=AGL(1,7) has order 42.
- The map x↦−x fixes 0 and is three transpositions, so it is odd. Hence |N_{A7}(P)|=21 and |N_S(P)|∈{7,21}.
- n₇ divides [A7:P]=360 and n₇≡1 (mod 7), so n₇∈{1,8,15,36,120}.
- The admissible orders dividing 2520 are {56,105,168,252,315,840,2520}. Note 36·21=756 does not divide 2520.
- Exclusions:
  - **840:** index 3 in the simple group A7, impossible.
  - **56:** there are 48 elements of order 7, so the remaining 8 elements form a unique, normal Sylow 2-subgroup.
  - **105:** N_S(P) must have order 7, so n₇=15. n₅∈{1,21}, and 90+84>104, so n₅=1 and a Sylow 5-subgroup is normal.
  - **315:** the point stabilizer has order 45 and a normal C5 (n₅ divides 9, so n₅=1), so it lies in N_{A6}(C5), which has order 10. (N_{S6}(C5) has order 20 and contains the odd 4-cycle x↦2x.) Impossible.
  - **252:** n₇ must be 36, giving 216 elements of order 7. The order-36 point stabilizer then consists of exactly the 36 elements of order ≠7, a union of conjugacy classes, so it is normal.
- That leaves 168 and 2520, and 2520 means S=A7. Correct.

**(a5) Order 168: the Fano plane.**
- H=S_a has order 24 and acts faithfully on the other six points.
  - An H-orbit of size 1 would put H inside the pointwise stabilizer of two points, A5 (order 60), and 24∤60.
  - An orbit of size 3 would put H inside the 3-set stabilizer in A6, of order 18.
  - So an intransitive H has orbit pattern 2+4 or 2+2+2. The pattern 2+2+2 would embed H in (S2)³, of order 8.
- In the 2+4 case:
  - The paired suborbit has the same length (an elementary fact the candidate uses without proof), so the size-2 suborbit is self-paired.
  - Its orbital graph is then an undirected, simple, vertex-transitive 2-regular graph on 7 vertices. That is a union of equal cycles of length ≥3 dividing 7, i.e. a 7-cycle.
  - Its automorphism group has order 14<168, a contradiction. So S is 2-transitive.
- n₂(H)≠1:
  - A normal subgroup of order 8 would have equal-size orbits (orbits of a normal subgroup of a transitive group are blocks; also used without proof).
  - Those sizes are powers of 2 dividing 6, and faithfulness rules out size 1, so the pattern is 2+2+2. That forces the subgroup into (S2)³∩A6, of order 4.
- So n₂(H)=3. The conjugation image in S3 is not C3, since a C3 image would make the order-8 kernel normal.
- The image is therefore S3, with kernel K of order 4. K's orbits form a canonical matching. The matching stabilizer in A6 has order 24, so it equals H.
- J=S_{p,q} has order 168/42=4.
  - Inside the even matching stabilizer, J fixes the partner x of q.
  - J acts as the regular Klein four-group on the remaining four points, so Fix(J)={p,q,x}.
- Equal orders give S_{p,q}=S_{q,p}=S_{p,x}=S_{q,x}. So the block through any pair is Fix(S_{u,v}), and gS_{u,v}g⁻¹=S_{gu,gv} gives S-equivariance. This is a Steiner triple system STS(7).
- Uniqueness of STS(7): I re-derived the forced triples {1,4,6}, {2,3,6}, {2,4,5}.
- The candidate's F2³ labelling makes every triple zero-sum.
- Collineations are additive, hence linear, and |GL3(2)|=7·6·4=168. So S≅GL3(2). Correct.

**Independent finite cross-check (control A).** I enumerated A7 exhaustively by cyclic extension, which uses no CFSG and no database:
- There are 947 cyclic subgroups, cross-checked against direct element counts.
- There are 40 conjugacy classes and 3786 subgroups.
- Exactly six classes are nonabelian simple: A5 with orbits 5+1+1, A5 with orbits 6+1, two transitive GL3(2) classes, A6 with orbits 6+1, and A7.
- Each of the six was identified by an isomorphism that the script constructed and re-checked on every pair of elements.

Together with (a1), this is a complete computational re-derivation of claim (a) for groups of every order.

I did not run the requested search "for simple groups of order <10⁴" as such. Listing the simple groups of order <10⁴ would itself require CFSG, and the A7 enumeration already covers every order. A further cross-check: PSL(2,8), whose order 504 divides 2520, is simple and has no subgroup of index ≤7; its minimum index is 9.

Every intermediate of (a2)–(a5) was confirmed numerically. For both order-168 classes this includes: |H|=24 and transitive on 6 points, n₂(H)=3, |K|=4 with three 2-point orbits, H equal to the even matching stabilizer, |S_{pq}|=4 with exactly 3 fixed points, an STS(7), and an automorphism group of order 168 containing S. There are exactly 30 labelled STS(7), all in one S7-orbit. No transitive subgroup of A7 has subdegrees {1,2,4}.

**Dependencies of (a).**
- Sylow's theorems, Lagrange, orbit–stabilizer and the sign homomorphism.
- Solvability of A_m for m≤4 and of S3 and S4.
- Simplicity of A6 and A7, which the candidate names as standard.
- That S5 has a unique index-2 subgroup.
- That paired suborbits have equal length, and that orbits of a normal subgroup of a transitive group have equal size.
- Uniqueness of STS(7) and Aut(Fano)=GL3(2), both proved inline.
- No CFSG, Jones or database; no pinned data. The candidate's "eval kernel" divisor listing is not relied on, and I recomputed it.

**(a′) The §5 corollary.**
- The case split is coherent given (a): either an index ≤7 exists, giving one of the four groups, or μ≥8.
- The Sun8 conclusion rests on three outside-manifest, unreviewed files: the support lemma, the A5/A6/A7 bridge and the GL3(2) Fano proof.
- None of A5, A6, A7 or GL3(2) has a prime divisor >7, so their Sun8 status comes entirely from those unreviewed files.
- The corollary is therefore **INCONCLUSIVE**. This review gives no verdict on Sun8 for any of the four groups or for the claimed simple-group family.

## 4. Claim (b): independent reconstruction

**Statement reviewed, exactly as written in the candidate.**
- G is finite, and no proper subgroup has index <8.
- There are eight pairwise disjoint left cosets g_iH_i with gcd([G:H_i],[G:H_j])=7 for all i≠j.
- p>7 is a prime dividing |G|.

**(b1) Selection.**
- Write m_i=7a_i. The a_i are pairwise coprime.
- Each prime divides at most one a_i, and p∤a_i ⇔ p∤m_i.
- At most one index is removed for each of p, 2, 3 and 5, so |J|≥4, and |J|≥5 if p divides no index.
- Control B confirms this exhaustively over every placement of {2,3,5,p}: the minimum is exactly 4, and 5 when p is unused.

**(b2) Coefficient induction.**
- Let X_t be the intersection of the first t subgroups and I_t=[G:X_t]=7A_tc_t, with c_t 5-smooth.
- For the next cofactor a: gcd(a,A_t)=1 by coprimality and gcd(a,c_t)=1 because gcd(a,30)=1. So gcd(I_t,7a)=7 and lcm=7A_t·a·c_t.
- The next coset is disjoint from an earlier one, so H_iH≠G. (xA∩yB=∅ ⇔ x⁻¹y∉AB.)
- Hence X_tH⊆H_iH≠G, and |X_tH|=|X_t||H|/|X_t∩H|<|G| gives I_{t+1}<I_t·7a=7·lcm.
- As a common multiple, I_{t+1}=lcm·c' with 1≤c'≤6. So p∤I_{|J|}, and the intersection contains a full Sylow p-subgroup P. Correct.

**(b3) Distinct maximal overgroups.**
- [G:⟨H_i,H_j⟩] divides 7, and μ≥8 rules out index 7, so ⟨H_i,H_j⟩=G.
- Maximal subgroups M_i⊇H_i (i∈J) all contain P and are pairwise distinct.
- Conjugation carries the conclusion to every Sylow p-subgroup. P=G is impossible because P≤H_i, which is proper. Correct.

**Observation O1** (non-defect; my own elementary deduction, not in the candidate, not adopted):
- Under μ≥8 no index equals 7, so every a_i≥2. The remark that "units may repeat" is therefore vacuous under the theorem's own hypothesis. It is harmless and the proof does not use it.
- Eight pairwise coprime integers ≥2 have pairwise distinct prime factors, all dividing |G|. So the hypothesis of (b) forces |G| to have at least eight distinct prime divisors.

**Dependencies of (b).**
- Sylow existence and conjugacy, the product formula, the coset-disjointness criterion, Lagrange, and existence of maximal subgroups containing a proper subgroup.
- Conditional premises: μ(G)≥8 and the explicit eight-coset, gcd-exactly-7 hypothesis.
- **P7 definition dependency.** The candidate calls this hypothesis "the prior direct P7 condition" and refers to §3 of `reduction-and-generation-v1.md` (SHA `fa0497ae…`). That file is outside the manifest and was not read. Following overlay 3, I draw no equivalence from the name. My verdict covers exactly the explicitly stated hypothesis. Whether a source-specific P7 definition, or a Sun8 counterexample through any Sun7/R8 reduction, implies it is **INCONCLUSIVE** here. The candidate itself correctly gives no unrestricted Sun8.

## 5. Claim (c): independent reconstruction

**Statement reviewed.** G is finite with μ(G)≥8. Then:
- (i) if p>42 divides |G| and a Sylow p-subgroup lies in ≤2 actual maximal proper subgroups, Sun8 holds in G;
- (ii) if p>7 and a Sylow p-subgroup lies in ≤1 such subgroup, Sun8 holds.

**Reading of Sun8.** Every eight pairwise disjoint left cosets include two whose indices have gcd ≥8. This is the candidate's own §3 usage ("violate Sun8" means all pairwise gcds ≤7). I read no separately frozen Sun8 definition.

**(c1) Pair lemma.** Disjointness gives H_iH_j≠G. Then I_ij<m_im_j=lcm·d_ij, so I_ij=lcm·c_ij with 1≤c_ij<d_ij. In particular d_ij≥2. If d_ij≤7 and p>7 divides neither index, then p∤I_ij. Correct.

**(c2) Triple lemma.** (H_i∩H_j)H_k⊆H_iH_k≠G gives I_ijk=lcm(I_ij,m_k)·c' with 1≤c'<gcd(I_ij,m_k). Correct.

**(c3) Bound (3).**
- The valuation identity gcd(lcm(a,b),c)=lcm(gcd(a,c),gcd(b,c)) holds because exponent lattices are distributive.
- Also gcd(xy,z)≤gcd(x,z)·y.
- Together these give gcd(I_ij,m_k) ≤ (d_ij−1)·lcm(d_ik,d_jk) = B.
- With p≥B and p dividing none of the three indices, c'<B≤p. So I_ijk is p-free and the triple shares a Sylow p-subgroup. Correct.

**(c4) §2: five indices always contain a triple with B≤42.**
- By pigeonhole, three of the five lie on one side of 7-divisibility.
- Three 7-divisible indices have all pairwise gcds equal to 7, so B=6·7=42.
- Three non-7 indices: I re-derived every case of the a≤b≤c split, including the impossibility of (4,5,6). The gcd-4 and gcd-6 edges share a vertex, which makes the other two indices even, so their gcd cannot be 5. Correct.

**(c5) §3: the contradiction.**
- Two indices divisible by p>7 would have gcd >7, so at least seven indices are p-free.
- For p>42, choose five of them. (c4) and (c3) give a triple sharing a Sylow P.
- Pair generation follows from μ≥8, because [G:⟨H_i,H_j⟩] divides d_ij≤7.
- That gives three distinct maximal overgroups of P, contradicting the bound of two.
- Clause (ii) needs only (c1) and a pair.
- The case P=G is correctly dismissed: in a p-group every proper index is a power of p, so p-free indices would make the cosets equal G and not disjoint. Correct.

**MINOR m1** (wording only). The status paragraph says "More generally, if p>7 and a Sylow p-subgroup has at most one maximal proper overgroup, Sun8 holds." Clause (ii) is not a generalization of clause (i). It has a weaker prime threshold but a strictly stronger overgroup hypothesis, so the two statements are incomparable. Both are proved and nothing mathematical changes. Suggested additive fix: replace "More generally" with "Separately".

**Observation O2** (non-defect; control B, informational). Every valid 4-multiset of indices (10,873 scanned) already contains a triple with min-B≤42. So "five" in §2–§3 could be "four". The claim does not change, since seven p-free indices are available.

**Observation O3.** In PSL(2,23) with p=11, and in PSL(2,47) with p=23, a Sylow p-subgroup lies in three actual maximal subgroups (two conjugate Borels and the dihedral torus normalizer). These form only two conjugacy classes. This confirms the candidates' warning that the overgroup hypotheses concern actual subgroups, not conjugacy classes.

**Dependencies of (c).**
- The same group-theory imports as (b), plus the gcd/lcm identities above.
- Conditional premises: μ(G)≥8, p dividing |G| with p>42 (or p>7), and the actual maximal-overgroup bound.
- No Sun7, R8, Jones or CFSG.

**Where the hypotheses actually hold (control D).** This shows only where the hypotheses apply. It is not a test of the theorems.
- For prime q from 11 to 47:
  - μ(PSL(2,q))≥q≥8 is derived inside the computation: any subgroup of index <q contains a Sylow q-subgroup, and every proper overgroup of that Sylow subgroup has index ≥q+1.
  - The Sylow q-subgroup lies in exactly one maximal subgroup, the Borel. So clause (ii) applies to every listed q.
  - Clause (i) applies to (q,p)=(43,43) and (47,47).
  - The ≤3 exclusion in (b) applies to all 15 (q,p) pairs computed, including (23,11) and (47,23), which have 3 overgroups.
- The group generated by the standard M11 generators has order 7920. Its Sylow 11-subgroup lies in exactly one maximal subgroup, of order 660, and μ≥11.
- |A8|=20160=2⁶·3²·5·7 has no prime divisor >7, so (b) and (c) say nothing about A8.
- Any Sun8 statement for these groups would only be a conditional consequence of the written proof. This review neither asserts nor adopts one.

## 6. Controls and receipts

All four controls are my own code under the prefix `f170r-`, run as `python3 -B` (Python 3.14.3, numpy 2.4.3, no installs). No author code was read or executed. Hashes were taken at 07:45:11 and re-verified unchanged at 07:51:56 PDT.

| Control | Script SHA-256 | Output file / SHA-256 | Run (PDT, from /bin/date) | Result |
|---|---|---|---|---|
| A: A7 lattice and steps of (a) | `f170r-ctrl-a-small-index.py` `b65f152aea7c7d37dc718912ca21f410b127808002e0515d725a6f00cad63614` | `f170r-ctrl-a-small-index.out.txt` `ae5985b7cbf2dea3e0ee174594bc7c789ce3d72f79f08af02c2b945b530b37ab` | 07:22:05–07:22:23 | 45/45 as expected |
| B: exhaustive arithmetic for (b), (c) | `f170r-ctrl-b-arith.py` `ce3816293772ed8be77842196148c09235ca4ceff56f9b5339450f6bdaeab271` | `f170r-ctrl-b-arith.out.txt` `6da53772817ee9effbb2bd789d2e0a21945fa36ddebfca5f6e1c0d1f6f20a161` | 07:27:25–07:27:28 | 23/23 |
| C: coset/index lemmas on real groups; (b) induction | `f170r-ctrl-c-cosets.py` `59111c785708eb665df0dcb4e60fb8bf19c56737b12d841d04ec6baac5f9525b` | `f170r-ctrl-c-cosets.out.txt` `00216f1b6b980780d9727ebde6d2dede22f6c6fc6c05e4f9f1248eb2a918aeb9` | 07:44:06–07:44:22 (final run; see exception) | 32/32 |
| D: actual maximal overgroups of Sylow p (p>7) | `f170r-ctrl-d-overgroups.py` `7cf46ef5d3ff960afb462b49c7267b62d8125eeb0042801d6ff1206443617a27` | `f170r-ctrl-d-overgroups.out.txt` `6a424c2a6c420b3309294a419738fb71f4ebf1afdf07f4d7858e9fdfc86e0219` | 07:44:06–07:44:11 | 29/29 |

**Positive cases:**
- A: the full A7 class table, the explicit isomorphisms, the order-60, degree-7 and order-168 intermediates, and PSL(2,8).
- B: the complete capped-exponent model, in which only the exponents of 2, 3, 5, 7, capped at 3, 2, 2, 2, matter.
  - There are 108 types and 5,955 valid triples.
  - The maximum non-7 min-B is 40, attained by (15,20,12) with gcd pattern (3,4,5). The 7-side value is 42.
  - All 15,896 valid 5-multisets contain a triple with min-B≤42.
  - Bound (3) holds on 112,564 integer cases.
- C:
  - For all ordered pairs in A5, S5, GL3(2), AGL(1,11) and A6 (3,481 / 24,336 / 32,041 / 1,444 / 251,001 pairs): |HK| computed as explicit sets agrees with the product formula, and for every g, H and gK are disjoint exactly when g∉HK.
  - Whenever HK≠G, c<d and d≥2.
  - Triple lemma (2)+(3) on 182,212 / 3,501,467 / 5,376,944 / 43,665 ordered triples, with equality gcd=B attained.
  - In AGL(1,11), the p-free consequences for p=11 hold on all qualifying cases: 6 pairs and 8 triples.
  - (b) induction on A7 point stabilizers: I_t=7, 42, 210, 840, 2520, 2520, 2520 with c'=6, 5, 4, 3, 1, 1.
  - (b) induction on GL3(2): 26,390 ordered chains of index-7 subgroups.
  - Explicit disjoint families in A7×Z143: for p=13, I_J=7·11·360; for p=11, I_J=7·13·360. The Sylow p-subgroup lies in the intersection in both.
- D: the PSL(2,q) table in §5, the M11-generated group, and A8 vacuity.

**Negative cases** (each fails for the intended reason):
- A:
  - A planted classification without order 168 is rejected by the simple order-168 classes.
  - Ignoring the parity step adds orders {210, 504, 630}.
  - In A7 itself, Fix(S_{01})={0,1}, so there is no triple system there.
  - The isomorphism finder rejects S4 versus SL(2,3), and accepts relabelled S4 as a positive control.
- B:
  - The unrealizable gcd pattern (4,5,6) has min-B=48>42.
  - The product variant of the valuation identity fails at (2,2,2).
  - Without coprimality, zero indices are selected.
  - An even cofactor gives gcd(42,14)=14.
- C:
  - Pairs with HK=G have c=d exactly, in 237 / 1,103 / 1,141 / 187 / 2,033 cases.
  - A nondegenerate S5 triple with H_iH_j=G violates bound (3): (m_i,m_j,m_k,I_ij,gcd,B)=(60,2,120,120,120,60).
  - In A7×Z2, an even cofactor gives gcd(I₂,14)=14 and c'=10≥7.
- D has no planted negative. The (23,11) and (47,23) rows contrast actual counts with conjugacy-class counts.

**What the controls do not establish.** They verify the load-bearing lemmas, the arithmetic case analysis and claim (a) by exhaustive enumeration. They do not test the conclusions of (b) or (c) on any actual P7 or Sun8-violating configuration; none is known in the tested groups. They prove nothing about Sun8 in any group.

**Counterexample attempt.**
- For (a), no counterexample can exist once the A7 enumeration is complete.
- For (b) and (c), the exhaustive checks found no failure of any load-bearing step in any tested group or arithmetic model.

## 7. Deviations and exceptions

1. **Guessed paths before reading the manifest.** One hash/size command on five guessed, nonexistent paths (`lanes/mathematics/owners/sun8-2/attack-e1/...`) ran in parallel with the manifest read, just after 06:54:14. All five returned "No such file". No content was displayed.
2. **Control C was rerun and its first output overwritten (exception).**
   - The first run (07:32:52–07:33:06, 35/35, earlier script version) produced degenerate triple-negative witnesses, each using an index-1 vertex with B=0.
   - I then edited the script (file timestamp 07:34) to require nondegenerate witnesses: every index >1 and d_ij≥2.
   - The final run (07:44:06–07:44:22) **overwrote** `f170r-ctrl-c-cosets.out.txt`, so the first-run output bytes are **not preserved**.
   - The count dropped from 35 to 32 only because three degenerate NEG entries became INFO lines ("no nondegenerate triple with H_iH_j = G violated bound (3)" for A5, GL3(2) and AGL(1,11)). The S5 witness above remained the one nondegenerate negative.
   - Every receipt in §6 refers to the final bytes.
3. **Control B edit slip.** A line-number slip while editing temporarily broke the script's bound-(3) loop. I repaired it before the only run; the run used the final script `ce381629…`.
4. **Capacity pause.** The kill requests for the final C run and for D arrived after both jobs had already finished (07:44:22 and 07:44:11), so there are no partial outputs. After the pause I did only hashing, then wrote this file.
5. **Scoping of the requested search.** The "order <10⁴ subgroup-index search" was replaced by the complete A7 enumeration, which is CFSG-free and covers all orders (see §3). Exhaustive enumeration is a cross-check, not a replacement for the candidate's elementary proof, which avoids enumeration.
6. **Writes and environment.** Nothing was written outside this directory. No temp files, no pycache (I used `-B`), no web search, no external model, no Git, no deletion, no publication, no infrastructure change, and no unrelated builds or tests. The parent file `parent-capacity-resume-v1.json` in this directory is not mine and was only hashed.

## 8. Files created by this reviewer (this directory only)

- `f170r-ctrl-a-small-index.py`, `f170r-ctrl-a-small-index.out.txt`
- `f170r-ctrl-b-arith.py`, `f170r-ctrl-b-arith.out.txt`
- `f170r-ctrl-c-cosets.py`, `f170r-ctrl-c-cosets.out.txt`
- `f170r-ctrl-d-overgroups.py`, `f170r-ctrl-d-overgroups.out.txt`
- `review-v1.md` (this file)

## 9. Summary

I reconstructed every elementary step of the three frozen candidates and found no fatal or major defect. The small-index classification (a) is correct by its written elementary argument: faithful actions into A_m, Sylow and normalizer exclusions, a self-paired orbital and the 7-cycle, the canonical matching, unique third fixed points, and STS(7)=Fano with Aut=GL3(2). A complete CFSG-free enumeration of A7's 3786 subgroups independently finds exactly A5, GL3(2), A6 and A7 as its nonabelian simple subgroups. The P7 four-overgroup theorem (b) is correct for its explicitly stated hypothesis: eight pairwise disjoint cosets, all pairwise index gcds exactly 7, μ≥8. Its equivalence to the separately frozen "direct P7" definition, which is outside the manifest, is unreviewed. The two-overgroup Sun8 criterion (c) is correct without any Sun7/R8 import. Its only defect is one wording MINOR ("More generally"). Controls A–D confirm the lemmas, the exhaustive gcd case analysis and where the hypotheses hold, for example PSL(2,43) and PSL(2,47) for the p>42 clause. The small-index candidate's Sun8 corollary stays INCONCLUSIVE because its three inputs are outside the manifest and unreviewed. This same-harness review is not human, independent-model-family, formal/kernel or novelty verification, and it adopts nothing.
