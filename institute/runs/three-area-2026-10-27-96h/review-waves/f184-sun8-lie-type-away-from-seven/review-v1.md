# f184 — independent same-harness review of the Lie-type away-from-seven candidate

## 1. Verdict and exact boundary

**Candidate scientific findings: FATAL 0 / MAJOR 0 / MINOR 2.** The two MINORs concern an overloaded length convention in (I2) and the absent orbit-to-Levi pairing in the ²E6 paragraph. Neither invalidates the displayed order ratios, cyclotomic divisibility, or the conditional proofs of Theorems A and B.

**Theorem A, p ≥ 11:** conditionally supported as written, including the three-subgroup gcd bound and Sun_k for 2 ≤ k ≤ min(p,D(S)), under the explicitly enumerated Lie-structure premises below and the standard disjoint-coset meaning of Sun_k. No Sun7, R8 or CFSG premise is needed for this conclusion.

**Theorem B, p ≠ 7 and S not isomorphic to PSL3(2):** conditionally supported as written: there is no family of three proper subgroups with all three index gcds exactly 7, even without disjointness. Repeated subgroups or repeated parabolic types do not create a loophole. This excludes the candidate's explicitly stated eight-disjoint-coset / 28-gcd-7 condition.

The manifest's scope string lost the negation and said “p=7.” This is a **parent paraphrase error, not an author mathematical defect**. The actual source says p≠7 at lines 6 and 85 and excludes characteristic 7 at lines 8 and 104. After I notified the parent, the parent froze `parent-characteristic-sign-scope-erratum-v1.json` (SHA-256 `4189f0afdc3ccc4c8e5b285c3802b62cd80672b10dd39e0c55293c589d0bb9d5`, 1243 bytes, 14 LF), expressly authorizing only the actual p≠7 scope. No characteristic-7 theorem is assessed or accepted here.

| Claim | Disposition | Exact dependency / limit |
|---|---|---|
| Lemma 1, lines 29–35 | Conditionally supported; no FATAL/MAJOR | BN/root-subgroup premises C1 below, the specified finite-Coxeter facts, Sylow conjugacy. The minimal-length descent is valid, including relative non-divisible roots. |
| Lemma 2 / Table 1, lines 39–67 | Conditionally supported; MINOR-1 and MINOR-2 | Lemma 1, parabolic/Levi/index imports C2–C8, plus elementary polynomial algebra. All displayed maximal-Levi ratios and common factors checked independently. |
| Lemma 3, lines 73–79 | Supported as elementary arithmetic conditional only on the displayed Table 1 assignment | The q=2 product bound and both finite cyclotomic tables reconstruct correctly. The exceptional list is complete for those assignments. |
| Theorem A, lines 5 and 83 | Conditionally supported | Lemmas 1–2, q≥p≥11 and the cyclotomic lower bound; elementary Sun_2 proof supplied below. |
| Theorem B, lines 6, 85–97 | Conditionally supported for p≠7 only | Lemmas 1–3, correct q=3 maximal-parabolic table, and the two index-divisibility classes. |
| q=3 table, lines 87–94 | Arithmetic supported; group-identification import remains conditional | Every listed index and every gcd including equal types agrees with independently computed Weyl-orbit polynomials; classical geometric counts also agree. |
| PSL3(2) exception, line 8 | Verified as a genuine exception to the three-subgroup statement | Direct GL3(2) construction finds 7 point and 7 line stabilizers, 14 distinct subgroups of index 7; any three point stabilizers give the required three gcds 7. Saying it “has seven distinct” is true, not a claim that the total is seven. No finding charged. |
| Optional §7 Sun8 corollary in characteristics 2,3,5 | **INCONCLUSIVE / not reviewed** | Its Sun7 composition and R8 implication are cited-but-unlisted inputs and were not opened or adopted. The implication would be conditional on precisely those additional premises. |
| Equivalence to the external source-specific term “direct P7” | **INCONCLUSIVE as source attribution** | The cited older §3 is unlisted and was not opened. Exclusion of the literal eight-coset/28-gcd-7 condition stated in this candidate is proved; transfer to an external definition requires that definition to entail at least three proper-subgroup indices with pairwise gcd exactly 7. |
| Author checker execution / historical provenance | Not independently certified | No author code was opened/imported/run. The counts 589 and 226 are arithmetically consistent, but the author's execution assertions remain assertions. |

This is a **same-harness written-mathematics review**, not a human review, independent-model-family review, clean-cognition certificate, formal/kernel proof, novelty check, bibliographic-source verification, global Sun8 theorem, or parent adoption decision.

## 2. Binding, complete source consumption, and scope hygiene

The manifest SHA-256 was checked against the assignment and equals
`a98023d69587bd411b3c17012f30039a3259199afa4da2fa611013027379f572` (4617 bytes, 51 LF). All five declared inputs matched their full SHA-256, byte count and LF count before mathematical interpretation. All have terminal LF and zero CR bytes. I read all their contents, not just excerpts, in this declared order:

| Order | Declared input basename | Bytes / LF | Full SHA-256 |
|---:|---|---:|---|
| 1 | `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` | 6883 / 56 | `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` |
| 2 | `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` | 3056 / 11 | `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04` |
| 3 | `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` | 3164 / 10 | `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218` |
| 4 | `frontier-20261028-sun-wide-search-preview-frontier-v1.json` | 2402 / 27 | `4ca6a3bb90795334dcd5783463863efe3b194facf1ed92f58f14f44e8689a2e6` |
| 5 | `frontier-20261029-lie-type-away-from-seven-v1.md` | 16887 / 106 | `d2af4a0dfa7cbf3a55274aeb30b5657a593737eef6ffd97d2d38a461ea579736` |

Inputs 1–3 are binding overlays, not rehabilitations of old alternating results. In particular, arbitrarily repeated cofactor 1 is not restricted by pairwise coprimality, and seven index-7 labels / seven disjoint cosets are not an eight-disjoint-coset Sun8 counterexample. Control C4 also independently replays the explicit A7 point-stabilizer partition to demonstrate this scope distinction; it imports no alternating classification or earlier theorem.

Input 4 was read only as the required exposure/process frontier: **all its displayed older snippets remain NONINPUT**. I did not open or reconstruct any named older payload. This review does not certify the author's exposure hygiene or resolve the preview's historical pause/resumption status.

The candidate cites each overlay and the preview with the correct manifest SHA. The cross-references overlay 2→overlay 1 and overlay 3→overlays 1,2 also match. I parsed the entire four JSON inputs with my own `json.loads` code, and parsed every generated control result and receipt completely. No certificate was accepted by spotting a PASS line.

The parent scope-only erratum was subsequently read and parsed in full after C4 run1 and before C2 run2. Its related-f188 paragraph is process metadata only; no f188 mathematics or review was read or adopted. This late parent correction changes no source bytes and supplies no mathematical lemma.

Input/sequence receipts: `reviewer-input-receipt.json` SHA-256 `bd9ed5bd68569a283c6ec56f9fcc0bb54b0b0c2b6c1eb6d93a27a9201ae46ae7`; additive later scope/control record: `reviewer-scope-and-control-addendum.json` SHA-256 `e16040eff8a6a3432f9279db4f6cf6a04242e47c916bc2e9c9da2d81bb98ead0`.

## 3. Exact conditional structure-theory premises

The following statements are **conditional imports**, not proved by recalling a reference title or by finite controls. The candidate names Carter, *Simple Groups of Lie Type* (1972), BN-pair/twisted-group chapters; Steinberg, *Lectures on Chevalley Groups* (1967); Carter, *Finite Groups of Lie Type* (1985), order and Levi structure; Kleidman–Liebeck (1990), classical parabolics; Kleidman (1988), ³D4; Malle (1991), ²F4. None is a declared readable primary-source file/URL here, so I did not check chapter/page locations or open any of them. The review supports the implications **assuming the exact statements below**, not a claim that these sources were directly verified.

### C0 — group conventions, exhaustion, and central passage

S is the indicated simple quotient of the subgroup generated in defining characteristic in G^F, for simple simply connected G and Steinberg F. The standard untwisted and twisted type list used by Table 1 is exhaustive for that convention; this uses the structure/classification of simple algebraic groups and Steinberg endomorphisms, not CFSG. The groups with nonsimple small parameters are not silently treated as simple. The allowed Suzuki–Ree parameters are ²B2(q), q=2^(2m+1)≥8; ²G2(q), q=3^(2m+1)≥27; ²F4(q), q=2^(2m+1)≥8. The Tits group is excluded. Passing to the stated central simple quotient preserves the parabolic indices and the needed root-subgroup/BN data. A valid alternative Lie-type description may be used; no assertion of a unique characteristic is needed.

### C1 — the full root-subgroup/BN premise needed by Lemma 1

1. B=U⋊T, T=B∩N normal in N, W=N/T a finite Coxeter group with its stated simple reflections and a positive/negative **relative** root system.
2. For non-divisible relative roots α, the subgroups X_α exist, are T-normalized, multiply over the positive roots to U (a Sylow p-subgroup), and multiply over the negative roots to U^-; S=⟨U,U^-⟩.
3. A lift n∈N of w sends X_α to X_(wα), and ⟨X_α,X_(-α)⟩ contains a lift in N of s_α. This is needed for **every non-divisible root**, not just a simple root.
4. Bruhat disjointness and the factorization BwB=U·w-lift·T·U hold, and P_J is exactly the union of BwB for w∈W_J. Proper J gives proper P_J; all proper parabolics lie in a maximal one.
5. Finite reflection/Coxeter facts: a nonidentity w has a left descent; ℓ(s_αw)<ℓ(w) iff w^(-1)α is negative; W preserves non-divisibility and root signs appropriately; s_(-β)=s_β and w s_β w^(-1)=s_(wβ); the longest element sends positive roots to negative roots and its lift sends U to U^-.

For twisted unitary groups the non-reduced BC convention must package the multipliable root subgroup inside the non-divisible-root group; β=−w^(-1)α is still non-divisible. The relevant relative reflection systems are BC_r/C_r for the unitary families, B_(n−1) for ²D_n, G2 for ³D4, F4 for ²E6, rank one for ²B2/²G2, and dihedral I2(8) for ²F4. The same five properties, rather than untwisted absolute-root substitutions, are the premise in each case. In particular the Ree–Suzuki rank-one root groups and the I2(8) reflection lifts are not proved by the ordinary untwisted Chevalley relation alone.

### C2 — parabolic index and polynomiality

For the corresponding rational parabolic and Levi,
[S:P_J]=|G^F|_(p′)/|L_J^F|_(p′)=I_J(q), with I_J∈Z[x], and Π_G=I_J Π_L as the displayed polynomial identity. This includes the agreement between the rational group, the specified simple quotient, and its parabolic image. For ordinary graph twists one may justify polynomiality by summing q^(absolute Weyl length) over σ-fixed distinguished representatives in W_absolute/W_J; equivalently use an unequal-parameter relative length. **Do not use the unweighted relative Coxeter length from C1** (MINOR-1 below). Suzuki–Ree polynomiality uses the explicit data, or absolute length/2 with the correct convention.

My alternative Weyl-cell controls also condition on this Bruhat-cell point-count interpretation (and the usual fixed-point/flag correspondence); they do not independently prove all of rational algebraic-group structure.

### C3 — untwisted degrees, highest roots and Levi formulas

For untwisted rank r, Π_G=(x−1)^r W(x), Π_L=(x−1)^r W_J(x), and I_J=W/W_J. Chevalley's Poincaré factorization is W(x)=∏(x^d−1)/(x−1). The degree lists used are A_n: 2,…,n+1; B_n,C_n: 2,4,…,2n; D_n: 2,4,…,2n−2 together with n; G2: 2,6; F4: 2,6,8,12; E6: 2,5,6,8,9,12; E7: 2,6,8,10,12,14,18; E8: 2,8,12,14,18,20,24,30. The largest degree is h=ht(θ)+1. The ambient highest root θ has full support and strictly larger height than the highest root of each proper standard irreducible root subsystem. The same degree/highest-root facts apply to those subsystem components.

### C4 — unitary maximal parabolics and orders

For PSU_m(q), the maximal parabolics are the stabilizers of totally isotropic k-spaces, 1≤k≤floor(m/2). With empty products 1,
Π_G=∏_(c=2)^m (x^c−(−1)^c), and
- for 2k<m: Π_L=∏_(c=1)^k(x^(2c)−1) · ∏_(c=2)^(m−2k)(x^c−(−1)^c);
- for 2k=m: Π_L=(x−1)∏_(c=2)^k(x^(2c)−1).

This includes the special determinant/torus restriction in the balanced 2k=m case; using the other branch there would be wrong.

### C5 — minus-orthogonal maximal parabolics and orders

For PΩ^-_(2n)(q), n≥4, the maximal parabolics are the totally singular k-space stabilizers, 1≤k≤n−1. Π_G=(x^n+1)∏_(c=1)^(n−1)(x^(2c)−1). For k≤n−2,
Π_L=(x−1)∏_(c=2)^k(x^c−1)·(x^(n−k)+1)∏_(c=1)^(n−k−1)(x^(2c)−1);
for k=n−1, Π_L=(x²−1)∏_(c=2)^(n−1)(x^c−1).

### C6 — triality parabolics and orders

For ³D4, Π_G=(x²−1)(x⁸+x⁴+1)(x⁶−1). With Bourbaki central node 2, triality cycles 1,3,4. Retaining J={2} gives Π_L=(x²−1)(x³−1) and I_J=(x³+1)(x⁸+x⁴+1); retaining J={1,3,4} gives Π_L=(x⁶−1)(x−1) and I_J=(x+1)(x⁸+x⁴+1). These are the two maximal parabolic types.

### C7 — ²E6 graph action, actual orbit pairing and orders

Use the E6 chain 1–3–4–5–6 with 2 attached to 4. The graph action swaps 1↔6, 3↔5, fixing 2 and 4. Π_G=(x²−1)(x⁵+1)(x⁶−1)(x⁸−1)(x⁹+1)(x¹²−1). The exact **removed orbit → Levi type → p′-order** premise is:

| Removed orbit | Levi derived type | Π_L including its torus |
|---|---|---|
| {2} | ²A5 | (x−1)(x²−1)(x³+1)(x⁴−1)(x⁵+1)(x⁶−1) |
| {4} | A2(q²)A1(q) | (x−1)(x²−1)(x⁴−1)(x⁶−1) |
| {3,5} | A1(q²)A2(q) | (x−1)(x+1)(x⁴−1)(x²−1)(x³−1) |
| {1,6} | ²D4 | (x−1)(x+1)(x²−1)(x⁴−1)(x⁴+1)(x⁶−1) |

The two lists in source line 65 are correct as unordered sets but not in corresponding order (MINOR-2).

### C8 — Suzuki–Ree parabolics and orders

²B2 and ²G2 have relative rank one: their sole maximal parabolic is B, with index q²+1 and q³+1 respectively. For ²F4,
Π_G=(x⁶+1)(x⁴−1)(x³+1)(x−1), and the two maximal Levi p′-orders are (x²+1)(x−1)² and (x²−1)(x−1), with the indicated ²B2(q)×(q−1) and SL2(q)×(q−1) types. In the absolute F4 diagram the retained orbits are {2,3} and {1,4} respectively. This imports both completeness and orders, not a list of all maximal subgroups.

Elementary ingredients not being smuggled in as structure theory: Sylow conjugacy, Lagrange/index multiplication, reflection identities as explicitly stated above, monic polynomial division/Gauss's lemma, irreducibility and primitive-root characterization of Φ_e, Euler's totient and Möbius product, and the elementary gcd arguments. No classification of maximal subgroups, CFSG, Sun7, R8, or alternating/sporadic result enters the proofs of A/B.

## 4. Reconstruction of every load-bearing step

### 4.1 Lemma 1: the minimal-length step works

For h∈H∩BwB, factor h=u n t u′. Since U≤H and t∈T≤N, n t=u^(-1)h(u′)^(-1) lies in H∩N. Conversely an element of H∩N lies in its Bruhat cell. Thus W_H is exactly the image of H∩N, a subgroup, and H⊆U(H∩N)U.

Let J=W_H∩simple reflections. If w is a shortest element of W_H\W_J, w is nonidentity and has a left descent s=s_α. Then w^(-1)α<0 and β=−w^(-1)α>0. Conjugating X_α by the chosen lift of w inside H puts X_(-β) in H; U already supplies X_β. By the explicitly imported rank-one reflection-lift property, s_β∈W_H. The reflection identity gives w s_β w^(-1)=s and hence sw=w s_β∈W_H. The crucial order is correct: **membership of sw is proved before using minimality**. Its shorter length forces sw∈W_J; also s∈W_H, so s∈J and w=s(sw)∈W_J, contradiction.

Consequently W_H=W_J and H≤P_J. If J were full, a lift of w0 in H would put U^- into H; ⟨U,U^-⟩=S contradicts properness. Every p′-index subgroup contains a Sylow p-subgroup, so conjugation and the maximal-parabolic containment give the claimed index divisibility.

This argument survives a non-reduced relative system because W preserves non-divisibility and the reflection lift is imported for X_β, not an unproved absolute simple-root replacement. In rank-one Suzuki/Ree cases it reduces to: an element outside B supplies the unique reflection, then U and U^- generate S. In ²F4 it uses the same finite reflection facts for I2(8), not a crystallographic-root height assertion. C3 checks concrete overgroups for both twisted unitary rank-one/rank-two cases and Sz(8). C4 exhaustively checks the purely Coxeter descent core in I2(8) as well as smaller Coxeter groups. Neither finite check replaces the uniform root-subgroup import.

### 4.2 Lemma 2: common factors and Gauss's lemma

First put each proper parabolic inside a maximal one. For each maximal type, Φ_e divides Π_G but is coprime to Π_L in Q[x]; irreducibility gives Φ_e|I_J in Q[x]. Since Φ_e is monic and I_J∈Z[x], polynomial division has integer quotient and zero remainder. Evaluating gives an **integer divisibility**, not just an inequality or numerical near-integer.

- Untwisted: e=h. Φ_h divides (x^h−1)/(x−1). Every degree in W_J is at most its component's Coxeter number <h, so Φ_h divides none of its x^d−1 factors. The height inequality uses the highest-root dominance fact named in C3, not merely “different roots have different heights.” The resulting table is A_n: Φ_(n+1), B_n/C_n: Φ_(2n), D_n: Φ_(2n−2), G2: Φ6, F4/E6: Φ12, E7: Φ18, E8: Φ30.
- Odd m unitary: Φ_(2m) divides x^m+1; it could divide x^(2c)−1 only if m|c, impossible for c≤floor(m/2); a factor x^c±1 with c≤m−2 is too small to contain a primitive 2m-th root of the required sign.
- Even m unitary: replace m by m−1 in the cyclotomic order. Here m−1>m/2 and no remaining unitary factor has degree reaching m−1 with the required sign. Thus Φ_(2(m−1)) is coprime to every displayed Levi. The balanced Levi branch also avoids it.
- Minus orthogonal: a primitive 2n-th root satisfies ζ^n=−1. No x^c−1 with c<2n, no x^(n−k)+1 with 0<n−k<n, and no x^(2c)−1 with c<n can vanish at ζ. Thus Φ_(2n) survives all maximal indices, including k=n−1.
- Triality: x⁸+x⁴+1=(x¹²−1)/(x⁴−1) contains Φ12; both Levi orders have cyclotomic orders only dividing 1,2,3,6. Both displayed index polynomials match independently computed fixed-Weyl-cell sums.
- ²E6: Φ18 divides x⁹+1. A primitive 18th root can vanish on x^d−1 only for 18|d and on x^d+1 only when d is an odd multiple of 9. None of the factors in any of the four true Levis satisfies this. All four ratios match the correct removed-orbit Weyl-cell calculations.
- ²B2 / ²G2: D is the entire unique maximal-parabolic index.
- ²F4: x⁶+1=(x²+1)Φ12, and neither Levi contains Φ12. Independent fixed-Weyl calculations give the two index polynomials and agree exactly with the displayed Π_G/Π_L ratios.

C1 derives the indices by Weyl orbits / fixed Weyl elements rather than merely dividing the candidate's polynomials and checking them against themselves. C2 directly enumerates classical polar subspaces; C3 enumerates actual overgroups of a Sylow subgroup. All agree at their stated finite scope.

Some exact small-q values, independently calculated from (q^e−1)=∏_(d|e)Φ_d(q), are below. q=2 or q=3 entries whose parameter is nonsimple are only polynomial evaluations, not assertions that the corresponding group is simple.

| e / representative Table-1 types | Φ_e(2) | Φ_e(3) | Φ_e(11) |
|---|---:|---:|---:|
| 2: A1 | 3 | 4 | 12 |
| 3: A2 | 7 | 13 | 133 |
| 4: B2,C2 | 5 | 10 | 122 |
| 6: A5,B3,C3,D4,G2,PSU3,PSU4 | 3 | 7 | 111 |
| 8: ²D4 | 17 | 82 | 14642 |
| 10: PSU5,PSU6 | 11 | 61 | 13421 |
| 12: F4,E6,³D4,²F4 | 13 | 73 | 14521 |
| 18: E7,²E6 | 57 | 703 | 1770231 |
| 30: E8 | 331 | 8401 | 233669041 |

The actual smallest Suzuki–Ree parameters give ²B2(8):65, ²G2(27):19684, ²F4(8):4033. Full supplemental exact code, values, clock and code hash are in `reviewer-small-q-cyclotomic-values.json` (SHA-256 `2811e3caa8ee638f05994fe089d116e423ef3e2a234ecbdf1d90665775390e30`). General-rank correctness is the argument above; the finite sample is not a rank-uniform proof.

### 4.3 Lemma 3: q=2 product bound and the complete exceptions

For e≥2, Φ_e(0)=1, so Φ_e(q)≡1 mod q. Its value is an integer >1: for q≥3 use ∏|q−ζ|≥(q−1)^φ(e), and for q=2 every |2−ζ|>1 because ζ≠1. Therefore Φ_e(q) is never 1, and Φ_e(q)=7 forces q|6; a prime power q≥2 must then be 2 or 3.

At q=3, 2^φ(e)≤7 gives φ(e)≤2, i.e. e=2,3,4,6. The values are respectively 4,13,10,7.

At q=2, Möbius inversion gives the candidate's product. Each μ=−1 factor is >1; discarding those factors lowers the expression. The remaining factors form a subset of factors in (0,1), so including **all** positive integers d lowers the product further. The otherwise unexplained constant at source line 77 is justified exactly by

- first three factors: (1−1/2)(1−1/4)(1−1/8)=21/64;
- tail: ∏_(d≥4)(1−2^(−d))≥1−∑_(d≥4)2^(−d)=7/8, by the finite-product inequality and a limit;
- total ≥147/512>7/25=0.28.

Thus Φ_e(2)>0.28·2^φ(e). If it equals 7, then 2^φ(e)<25, so φ(e)≤4. With e≥2 this is exactly e=2,3,4,5,6,8,10,12, whose values are 3,7,5,31,3,17,11,13. Only e=3 gives 7; Table 1 assigns that only to A2. At q=3 the e=6 rows are exactly A5,B3,C3,D4,G2,PSU3,PSU4. The Suzuki–Ree values are already ≥65. This proves the stated exception list.

C1's independent recurrence and direct evaluations verify these tables; its unpruned scan covers every e=2,…,60 and every prime power q<2000, while its bounded/pruned wider scan covers all e≤300 and the Table-1 range through the tested ranks (up to e=398). Both find only (e,q)=(3,2),(6,3) yielding a value in {1,7}, always value 7. This is a consistency check of the written global argument, not its substitute.

### 4.4 Theorem A, including Sun_2

Set t=min(p,D(S)). Since p≥11, q≥11 and D≥(q−1)^φ(e)≥10. Among any three proper-subgroup indices two are p-divisible or two are p′. Their gcd is respectively ≥p or divisible by D, hence ≥t≥10. For k≥3 with k≤t choose any three of the k disjoint cosets; the pair supplied has gcd≥t≥k. A coset of S itself cannot occur in a disjoint family of size≥2, so all these subgroups are proper.

For Sun_2: if m=[S:H] and n=[S:K] were coprime, [S:H∩K] is divisible by mn and at most mn, so |HK|=|S|. Therefore HK=S and any left coset of H meets any left coset of K. Disjointness contradicts coprime indices. This supplies the elementary base case rather than importing Sun7.

Taking k=8 is permitted. The literal eight-coset gcd-7 pattern would already violate the three-subgroup bound. Lemma 3 and the q=3 exception table are not needed for Theorem A.

### 4.5 Theorem B and the q=3 table

For two p′-index subgroups choose maximal parabolics M_i with [S:M_i]|[S:H_i]. Their parabolic-index gcd g divides the original gcd. Outside the seven q=3 exceptions (and the expressly excluded PSL3(2)), D|g and D does not divide 7, ruling out an original gcd 7.

For the seven q=3 cases I independently obtain:

| S | Maximal parabolic indices | Complete gcd set, equal types included |
|---|---|---|
| PSL6(3) | 364,11011,33880,11011,364 | 28,91,364,847,11011,33880 |
| Ω7(3) | 364,3640,1120 | 28,280,364,1120,3640 |
| PSp6(3) | 364,3640,1120 | 28,280,364,1120,3640 |
| PΩ8^+(3) | 1120,36400,1120,1120 | 560,1120,36400 |
| G2(3) | 364,364 | 364 |
| PSU3(3) | 28 | 28 |
| PSU4(3) | 280,112 | 56,112,280 |

All agree with the source. No g divides 7. Including equal types is essential and has actually been checked, so repeated indices cannot reintroduce the withdrawn repeated-unit error from the overlays.

In any family with all pairwise gcds exactly 7, at most one index can be p′ by the preceding argument. At most one can be divisible by p: two such indices would have gcd divisible by 7p because p≠7. Three members are impossible by these two classes. The p≠7 condition is used precisely here. C3 explicitly exhibits the failed p-divisible step for the characteristic-7 description PSL2(7), which is the excluded isomorphism type PSL3(2); this is not a statement about other characteristic-7 groups.

For PSL3(2) in defining characteristic 2, maximal parabolic indices are 7,7 and the exception is real: GL3(2) has order 168; the seven point stabilizers and the seven line stabilizers in its Fano action are fourteen distinct subgroups of order 24. Three point stabilizers have the three index gcds 7. This proves the exception without opening the separate unreviewed Fano/Sun8 packet. No eight-coset conclusion for this group is made.

## 5. Findings (scientific count: 0 FATAL, 0 MAJOR, 2 MINOR)

### MINOR-1 — distinguish absolute/weighted Bruhat length from the relative Coxeter length

**Location:** candidate line 23, read with line 22. Line 22 uses the Coxeter length of the relative Weyl group for Lemma 1. Line 23 then writes a Bruhat sum Σq^ℓ(w) over the F-fixed Weyl group without saying that a different, absolute or unequal-parameter weighted length is required for the twists.

**Exact probe:** for PSU3(q), the relative Weyl group has order 2 and relative lengths 0,1, so the literal unweighted-relative reading gives 1+q. The true index is 1+q³ (the nonidentity representative has absolute A2 length 3). C4 also detects this mismatch for both PSU4 parabolics and both ³D4 parabolics, while the absolute-length sums agree with every displayed formula.

**Impact:** no FATAL/MAJOR consequence: I_J∈Z[x] is separately imported in (I2), and the correct explicit Π_G/Π_L formulas establish the divisibility proof. Lemma 1 correctly uses relative length. **Repair:** specify absolute length on σ-fixed distinguished representatives for ordinary graph twists, or explicitly define the unequal-parameter relative length; retain the separate Suzuki–Ree convention. Do not change the correct index tables.

### MINOR-2 — make the ²E6 removed-orbit / Levi correspondence explicit

**Location:** candidate line 65. The removed-orbit list {1,6},{3,5},{4},{2} is followed by the Levi-type list ²A5, A2(q²)A1(q), A1(q²)A2(q), ²D4. The correct correspondence is in the **opposite ordering**, as table C7 above states. A positional reading is wrong. The source's “respectively” explicitly applies to the Levi-type→order list, which itself is correct; the issue is the omitted pairing between the preceding two lists.

**Exact probe:** independent σ-fixed fundamental-weight orbits give unique matches {1,6}→²D4; {3,5}→A1(q²)A2(q); {4}→A2(q²)A1(q); {2}→²A5 (C1 and C4). The positional matching fails.

**Impact:** no change to the unordered set of four Levi orders, to their completeness, or to the common Φ18 factor, so Lemma 2 and A/B remain conditionally valid. **Repair:** state this explicit map or reorder the orbit list to {2},{4},{3,5},{1,6} alongside the existing Levi list.

No additional finding is charged merely because a proof uses honestly named standard imports. Nor is a correct but compressed elementary step (the q=2 product bound) charged once it reconstructs exactly.

## 6. Independently authored, actually executed exact bounded controls

All scripts are reviewer-authored stdlib Python 3.14.3. Each actual subprocess had an explicit **120-second cap**, stdin=DEVNULL, start/end native clock, elapsed time, exit code, script SHA, stdout/stderr SHA and byte count. **No cap occurred.** A cap would have been UNKNOWN, never acceptance. No author code was imported, run, or inspected. These counts are bookkeeping, not independent statistical trials or formal certificates.

### Accepted exact runs and hashes

| Control | Native start → end (PDT, 2026-10-29) | Seconds / exit | Exact coverage |
|---|---|---:|---|
| C1 run2 | 08:55:32−0700 → 08:55:39−0700 | 7.015 / 0 | 80 check objects; 259 untwisted and 78 twisted/Suzuki–Ree maximal-parabolic polynomials; cyclotomic/Gauss/divisibility and q=3 tables; intended negative cases. |
| C2 run2 | 09:22:25−0700 → 09:22:33−0700 | 7.843 / 0 | 16 check objects; direct finite-field polar-space enumeration; all positive counts integer-exact and mutants rational-exact. |
| C3 run1 | 09:02:39−0700 → 09:02:46−0700 | 6.467 / 0 | 41 check objects; actual matrix/permutation groups, exhaustive overgroup lattices of U, index/gcd checks; three intended-reason negative probes. |
| C4 run1 | 09:20:12−0700 → 09:20:13−0700 | 1.040 / 0 | 15 check objects; exhaustive Coxeter core, twisted-length counter-reading, ²E6 pairing, coverage counts, A7 scope control. |

| Run | Script SHA-256 | Result JSON SHA-256 |
|---|---|---|
| C1 run2 | `1ca5471fff07a2b99cc5d8c53376de2524461ed6fc551793f32b2007ef40cbc5` | `d9f7bcce9457cfdb664f7ba98043b96273c1308374b76898c495b6d92de4ce0c` |
| C2 run2 | `e4be5abdaf92c2a8e6143036c60e66b8783d0fe94978aa5e2e993985964f2b6a` | `e7fa31cfba099a0393ecdc53fa78d68ad4de856a24dfc92c8d383eb42c9fe9c4` |
| C3 run1 | `759003bae6154cddd478e3af7b0f8610078164122bd1533434a28c7f0e721891` | `d7ced77c39b0ad24bca94db434132f99e26f6db2ce724fbac2e69f41a641602b` |
| C4 run1 | `e7261182673e09fddf18f573e179e735eabdf24687f7cbf4522e42998383a974` | `52ad9a9150dda67369dc893b6f6e81fc515f865f34b84393f2c1abd8124a7674` |

All exact receipt data, including both initial runs and their retained errors/qualifications, are in `reviewer-control-receipts.json` SHA-256 `63cfc3005a2ffaa8d38b359da19196f1ffd99998af7f2c58ec60b1e99327aef5`. Every stderr was empty (SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`).

**C1 method and range.** Maximal untwisted indices come from Coxeter-length-graded fundamental-weight orbits, with W_J independently cross-checked by a subdiagram orbit chain and W(x) checked against the degree product. A_n for 1≤n≤14, B_n/C_n for 2≤n≤9, D_n for 4≤n≤9, and all exceptional G2,F4,E6,E7,E8 types are covered. Twisted simply-laced types use σ-fixed orbit points: PSU_m, 3≤m≤12; ²D_n, 4≤n≤9; all maximal parabolics of ³D4 and ²E6. Suzuki–Ree types enumerate W(B2),W(G2),W(F4), their automorphism-fixed elements, and minimal-coset representatives, using absolute length/2; the fixed group orders are respectively 2,2,16 and all resulting q exponents are integral. Quotients agree with the correctly matched displayed order data, Φ_e divides every index, and no relevant Levi contains Φ_e. Wrong e=h+1, parity-swapped PSU Table-1 rows, sign-mutated O^- Levis, and plus-versus-minus forms are rejected for the intended reasons. PSL3(2) correctly triggers the gcd-7 exception.

**C2 method and exact outputs.** Points and orthogonality are enumerated directly over F2,F3,F4,F9; ordered independent isotropic projective-point tuples are counted and divided by the exact number per k-space. No candidate checker is involved. U3(2):9; U4(2):45,27; U5(2):165,297; U6(2):693,6237,891; U3(3):28; U4(3):280,112. Minus orthogonal O^-_8(2):119,1071,765; O^-_10(2), k=1,2 only:495,19635; O^-_8(3):1066,29848,22960. O7(3) and Sp6(3) give 364,3640,1120; O^+_8(3), k=1,2:1120,36400. Plus-type O^+_8(2) has 135 points rather than the minus-type 119; the deliberate SU-factor sign mutation gives U5(2) point ratio 1485/7 rather than 165 and U6(2) ratio 891 rather than 693. The run2 mutants use `Fraction`, not floating-point tolerances. O^-_10(2) k=3,4 and O^+_8(3) solid-family splitting are not claimed as brute-force C2 coverage; C1 handles the relevant polynomials.

**C3 method and range.** All overgroups of U are enumerated as product-closed unions of U-double cosets. The product table is exact because (Ur_iU)(Ur_jU) is the union over u∈U of Ur_iur_jU; finite product-closed unions containing U are subgroups. Starting from U and closing after each added double coset exhausts every overgroup. B=N(U) is computed from double-coset sizes, B-double classes are obtained, and the simple-reflection classes are detected by B∪BsB being a subgroup. For every proper H found, the computed J=W_H∩simple recovers W_H=W_J, H≤P_J and P_J proper. Maximal overgroup indices agree with the candidate parabolics and every p′-index is divisible by D.

Concrete cases: PSL2(q) with q=4,5,8,9,11,13,16,25,27; PSL3(3), PSL3(4); PSL4(2); PSp4(3); PSU3(3), PSU4(2), PSU3(4); Sz(8), plus the exception/negative descriptions PSL3(2), PSL2(7). Generated orders equal the expected group orders; U has the full p-part in each. Sz(8) has order 29120, U order 64, B order 448, a 65-point orbit, and only proper U-overgroup indices 65,455. The construction additionally checks symplectic-form preservation; its standard Suzuki identification is not a general classification proof. PSU4(2) has maximal U-overgroup indices 27,45; PSU3(3) has 28; PSU3(4) has 65. The larger Ree groups are not concretely enumerated in C3 and remain conditional on C1/C8.

Intended-reason negatives actually found: (i) fourteen distinct index-7 subgroups of PSL3(2); (ii) fourteen order-24 subgroups found in the PSL2(7) action, three giving p-divisible indices 7 with three gcds 7, illustrating the p≠7 step; (iii) replacing defining-characteristic U in PSL3(2) by a Sylow 3-subgroup yields proper-overgroup indices 7,7,8,8,14,14,28,56, whose common gcd is 1, showing the defining-characteristic hypothesis matters.

**C4 method.** Exhaustively enumerated subgroups of I2(2),I2(3),I2(4),I2(6),I2(8),A3,B3,A4. The core property “w∈W′ and ℓ(sw)<ℓ(w) imply w^(-1)sw∈W′” holds exactly for their standard parabolics, recovering J=W′∩simple. For I2(8), 4 of 19 subgroups satisfy it, precisely the 4 standard parabolics; all 15 nonstandard subgroups fail. An explicit non-simple-reflection subgroup in A2 fails, so the control is discriminating. Relative-length sums versus absolute-length sums expose MINOR-1; unique orbit/Levi matching exposes MINOR-2. The author's reported counts 589 and 226 agree with the arithmetic number of maximal parabolic types over the stated ranges, but that is not an execution replay. The A7 control enumerates 2520 even permutations, seven distinct point stabilizers of index 7, and seven genuine left cosets that partition A7 with all gcds 7; it supplies no eight-coset counterexample and does not enter the Lie-type proof.

### Retained unsuccessful / qualified initial controls (not erased)

1. **C1 run1:** 08:53:59→08:54:08 PDT, 8.858s, exit 1, not capped. 79/80 checks passed. The sole failed assertion was **my incorrectly designed NEG2**, which supposed Φ_m cannot divide every PSU_m maximal index. It can for PSU6 and PSU10; neither the candidate nor its D assignment asserts otherwise. The original script (`reviewer-c1-lie-index-polynomials.run1-script.py`, SHA `e64f7de0b9f4b842e8daa3e92e9f4a8af186b9354c2b9ef7620537703c28f8fd`), result (SHA `a51880229fa5a6fa0f3645f9dcf67eb25e2e96c7da649ab7ec4cd96642738083`) and receipt remain. Run2 changes only this intended negative to the opposite-parity Table-1 row and records the original PSU6/PSU10 observation as informational. This is a reviewer-control error, not a candidate finding.
2. **C2 run1:** 08:58:23→08:58:37 PDT, 13.590s, exit 0, not capped. Positive counts are integer-exact, but my auxiliary mutated-Levi ratios used `/` and displayed floats. I do not count that negative as an exact-rational acceptance run. Its original script copy (SHA `8764c99d956f35f6053b0114d2d3f27523463cc4595a5b3cf1d21d17e52e9e2f`), result (SHA `559b39af3f73a38929c0cae6f75ab4fc69034c5f941ec2c5624de12f2384d11b`) and receipt remain. Run2 replaces only that division with `Fraction` and reruns the same cases; 16/16 checks pass using exact arithmetic throughout.

## 7. Other process deviations, non-access and hand-off

- Before displaying the manifest I performed its SHA check and a wave-directory metadata listing in parallel with a required read of `skill://independent-snapshot-review` (workflow instructions only). This is a deviation from a literal “manifest is the first read” rule. No candidate/overlay mathematical body was read or interpreted before the manifest; no delegate/external model was launched. The five declared mathematical/process inputs themselves were consumed completely in the mandated order.
- A reviewer C2 authoring edit initially targeted the wrong line range. It was repaired before C2's first execution; no author bytes or frozen source were touched. The actual executed script versions are pinned in their receipts.
- The parent scope erratum arrived after the initial source read and most controls; actual exposure order is recorded, not backdated. It corrects the parent's p=7 paraphrase to the existing p≠7 source and is not charged to the author.
- No unlisted mathematical file/source body, held f161/f162 material, sibling review, external source, author checker, Fano packet, prior Sun7 proof DAG, R8 proof, Git state or credential was opened. No author contact, web search, external model/API, publication, deletion or infrastructure change occurred. Parent-supplied same-harness system/memory/roster context is inherited context, not a clean-cognition certificate.
- Only this review and reviewer-prefixed artifacts were written by me in the assigned wave directory; the parent separately created its scope erratum. Frozen candidate/overlays/manifest are unchanged by this reviewer. No unrelated build, lint, formatter or test suite was run.

**Hand-off:** Theorems A and B have reconstructed conditional proofs with the stated two MINOR presentation repairs. Any parent disposition must retain C0–C8, the actual p≠7 scope, the source-definition transfer qualification, all reviewer-control corrections, and the distinction between finite controls and uniform structure theory. It must not promote §7, characteristic 7, PSL3(2) Sun8, novelty, historical-hold rehabilitation or unrestricted Sun8/P7 from this review.

The SHA-256 of this complete review and the exact reviewer-created file inventory are supplied in `reviewer-review-receipt.json` and the final hand-off, not embedded self-referentially in this file.
