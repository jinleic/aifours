# Complete level-six primitive inventory: cofinite injectivity and actual fourth-row quotients

MathKacMoody-2, original math-3. Last returned native observation before this write: **Wed Oct 28 22:58:24 PDT 2026** (not a completion clock). **WRITTEN, exact-computation-supported candidate; independent scientific review and parent disposition PENDING.** No formal/kernel, independent-model/human, priority or novelty acceptance.

## 1. Exact theorem and its boundary

Let S=G_C/J be the ORIGINAL full complex Serre quotient of A(r,s), for every allowed FULL Cartan realization C. Write S6 for its positive level-six part, graded by alpha3=6, and use ORIGINAL lowerings f1,f2,f3. At the named actual-source interfaces in Section 2 there is an explicit finite set E of integer parameter pairs, contained in r,s>=6, with

    |E| <= 57757,

such that for EVERY integer r,s>=4 outside E,

> **The complete simultaneous primitive kernel in S6 is zero:** ker(f1) intersect ker(f2) intersect ker(f3)=0, over ALL root degrees of that level, not merely the seven earlier displayed types.

E is a sufficient certificate's unresolved locus, NOT a set of known actual kernels. Its emptiness, its integer points and the exact number of possible actual exceptions have not been determined. The cofinite primitive theorem does NOT assume B5. A whole-band consequence is only the pointwise conditional **B5(r,s) implies B6(r,s)** in Section 7; B5 has not been certified here. In particular no unconditional whole-band F6/B6, arbitrary-GCM/all-level book solution, H13 authentication, negative witness, novelty or priority is claimed.

## 2. Actual-source interfaces

Use the complete level-one adjoint-sl3 candidate `frontier-20261028-fixed-levi-level1-independent-v1.md` and the full-Cartan/free-Levi/whole-ideal/original-lowering construction of `frontier-20261028-Levi-free-quotient-critical-reduction-v1.md`, Sections 0–4, with their explicitly named Cartan, PBW/normalized-transcription and finite-Levi inputs. These are substantive mathematical inputs, not a source-count header or an adopted result inferred from a computation.

For r,s>=6, no repeated-node3 seed occurs through level six, so S6=L6(V), S5=L5(V), V=adjoint sl3. For fifth and fourth boundary rows the source/target are NOT replaced by those free spaces: Sections 5–6 pay the exact extra ideals and targets. Every free primitive basis is checked as a whole basis by independent horizontal actions plus its full character multiplicity (or the earlier complete horizontal reconstruction).

## 3. The COMPLETE primitive inventory

The generator degree weights are (0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2). Exact integer arithmetic checks

    ch L6(V) = (V^6 - psi2(V^3) - psi3(V^2) + psi6(V))/6.

Lowest-vector multiplicities are extracted by multiplying with the finite-sl3 lowest Weyl denominator. Any lowest degree (a,b,6) satisfies 2a-b<=6 and 2b-a<=6, hence 0<=a,b<=6. The complete table has **24 oriented types, 15 up to node exchange**, and the sum of multiplicity times irreducible dimension is **43596**, matching Witt's total (8^6-8^3-8^2+8)/6.

The full table is `frontier-20261028-level6-full-lowest-character-table-v1.json`, SHA `d64f550fd89490a2124b32b62c5eb02088107e18b09ae283bcf6d7b3498db1f9`. The earlier informal seven-type inventory was incomplete; its correction `frontier-20261028-level6-inventory-scope-addendum-v1.json` is mandatory. No omitted coordinate/wall type is silently excluded below.

| Representative (a,b), plus mirror if unequal | Free primitive multiplicity at r,s>=6 | Candidate conclusion on r,s>=6 |
|---|---:|---|
| (0,1) | 1 | All pairs; nonzero scalar multiple of s-5. |
| (0,2) | 1 | All pairs; nonzero scalar multiple of s-1. |
| (0,3) | 1 | All pairs; nonzero scalar multiple of s-2. |
| (1,1) | 5 | All pairs; one-sign maximal minor. |
| (1,2) | 12 | All pairs; one-sign maximal minor. |
| (1,3) | 12 | All pairs; two quintic factors, resultant has integer roots only -3,-2 in y=s-6. |
| (2,2) | 34 | All pairs; previously delivered full two-minor resultant candidate. |
| (3,2) | 54 | All pairs; previously delivered full two-minor resultant candidate. |
| (2,4) | 24 | All pairs; the alternative 24x24 minor has one-sign coefficients. |
| (3,3) | 109 | At most 7998 exceptional pairs. |
| (4,3) | 107 | At most 6480 exceptional pairs PER orientation. |
| (4,4) | 162 | At most 19312 exceptional pairs. |
| (4,5) | 90 | At most 3843 exceptional pairs PER orientation. |
| (5,5) | 118 | At most 9801 exceptional pairs. |
| (6,6), full invariant source | 20 | All pairs; previously delivered full two-minor resultant candidate. |

The scalar descriptions in the first three rows are **up to a nonzero rational normalization of the source/target vectors**. Their exact stored determinant coefficients control signs and normalization; only nonvanishing is used.

## 4. Complete finite arithmetic supporting the table

The six newly added positive-minor cases (0,1),(0,2),(0,3),(1,1),(1,2),(2,4) have standard-library full-source/shifted-grid replay `frontier-20261028-level6-positive-small-replay-v1.json`, SHA `f582ca54bb70dca51294b5d92ac2b2c3245fd4ebfd00f883f123d5a047a985aa`. It reconstructs all Lie combinations/actions, checks their full Witt multiplicities and independence, and verifies each determinant polynomial on an entire shifted unisolvent grid with independent integer Bareiss arithmetic. For (2,4), the positive alternative minor is `frontier-20261028-level6-246-minor-seed1-v1.json`, SHA `3519d2896193fd6029427844903683d3d581b4ee36ee42ed1e50d955820a4739`.

For (1,3), the complete producer certificate is SHA `9484c65f306309766029429bc1ddfbe544fac36761f1c1397c32c4d629d63a64`; the independent full-source/minor/Hensel replay is SHA `013d3a8f4dcccd0406c6b6b560ad206df2c5340cf18c7e074e5fd9a1e0ef33c1`. An additional WHOLE resultant reconstruction, `frontier-20261028-level6-136-full-resultant-replay-v1.json` SHA `843e2596d2fd5c2e4ab508665fa6c4eb3456a1998a1b267db0bffb0a9843dd1f`, checks all 26 exact 10x10 Sylvester determinants in a degree-bound-25 unisolvent set. Thus its integer-root claim is not based on modular spots.

For the five cofinite representatives, remove positive linear factors and a positive-coefficient common factor from two actual maximal minors. The remaining residual total degrees are respectively 86/93, 80/81, 136/142, 61/63 and 99/99. Their x-leading coefficients are nonzero constants; an explicit modular y=0 Bezout identity with degrees preserved proves the residual polynomials coprime over Q[x,y] and C[x,y]. Projective Bezout bounds distinct common affine points by the product of degrees. Any actual primitive kernel makes both maximal minors vanish, so is in this finite locus.

For EACH pair, the dependency-free `frontier-20261028-level6-coprime-pair-replay.py` checks every exact rational coefficient product back to BOTH pinned minor tables, positivity, leading constants, primality and every modular Bezout coefficient. Full source/both-minor identities are separately reconstructed by the independent tree-Jacobi source plus shifted-grid replay. The latter shares FLINT exact determinant arithmetic with native producers; this is an explicit shared-library boundary, not independent arithmetic-library assurance.

For the last wall pair (4,5), the algebra certificate SHA is `8954b307772f8c31bd66aa8ce2fbffc4c86e8e2e0c3c458cefbe48f6f2a5f3cd`; its dependency-free polynomial replay SHA is `4e8b39eca7a15afa4a42dc8c77ca36d6cc3f43e5f2e47cd8666927b6bf000d24`; full 90-dimensional source/both-minor replay SHA is `8b2e911fcba7e95d67be2bdb8dd9fe69523598636aaa4cb9d8afa4d5859b21b6` (4186 shifted determinant checks per minor). The preceding four pairs are pinned in the earlier cofinite/fifth-boundary manuscripts and their exact replay files; all four full-source replays have now completed.

Taking the union over BOTH orientations where necessary gives

    7998 + 2*6480 + 19312 + 2*3843 + 9801 = 57757.

This union is over the COMPLETE 24-type inventory, not the earlier incomplete seven-type bundle.

## 5. Fifth boundaries, including the true seed-deletion cases

At r=5/s>=5 or s=5/r>=5, the new level-six source ideal consists only of the applicable irreducible seed modules of types (4,7)/(7,4), lowest degrees (1,0,6)/(0,1,6), dimension260. Target level five is unchanged. Complete reducibility makes the actual primitive source unchanged on every OTHER type. The two exceptional lowest seed lines themselves are entirely deleted when their seed parameter is five: the actual source is zero, so injectivity is true but no false free one-dimensional rank claim is used.

The displayed-seven boundary proofs are in `frontier-20261028-level6-fifth-boundary-and-seven-type-frontier-v1.md`, using all fourteen positive shifted-gcd/quotient/Bezout identities. The omitted small cases extend by exact substitution x=u-1,y=v-1: all coefficients have one sign and nonzero constant for (0,2),(0,3),(1,1),(1,2),(2,4), recorded in `frontier-20261028-level6-positive-small-min5-shifts-v1.json` SHA `4ec6b23efba41e96db2af05223fbe97dfc601e0efe25030012d7cb64becec9a8`. For (1,3), all removed linear factors stay positive on x,y>=-1, and its only integer resultant roots -3,-2 are below -1.

The last wall type's TWO fifth-boundary proofs are `frontier-20261028-level6-wall45-fifth-boundaries-v1.json`, SHA `379024486f7bbe2350ae42265364ae12a4ad2e9a75846ee3514a0d9a36868dc4`: exact quotient products, positive shifted gcds of degrees20 and21, and complete modular Bezout identities, all rechecked in plain integers in the retained kernel. This is same-owner kernel arithmetic, not a separate independent program. The actual source transport applies because its type (3,0), or mirror (0,3), is not a seed type. Thus NO possible exceptional pair has r=5 or s=5.

## 6. Fourth rows are ACTUAL quotient calculations

For r=4,s>=6 or s=4,r>=6, the level-five seed is present and its level-six descendants AND level-five target ideal are retained. No free-source equality or free-target substitution is made. Finite-sl3 complete reducibility proves

    P_mu(L6/I6) = P_mu(L6)/(I6 intersect P_mu(L6)).

Hence reduce the entire free primitive basis modulo I6, retain independent classes, and apply ORIGINAL D3 modulo the FULL I5 target. Source-ideal containment is checked on every source-ideal basis vector at two affine parameter values. The exact univariate minor is then checked for every nonnegative integer parameter by one-sign coefficients or Hensel/Cauchy; there are no unresolved nonnegative roots.

Selected-seven actual-family producer receipts are `frontier-20261028-level6-r4-quotient-family-v1.json` SHA `faf56d4b36edb59fb962448ba02e6b4952fb5539e1e13f7929e0accad964d096`, and its s4 counterpart SHA `eb685e72af53dc081fdef31d257eab2f3466f1c891eaddcbeb3c316642c4f33f`. Omitted-eight producer receipts have SHA `6eaee4bfb55a037073fa0fcf7e8ef2e64d37f035ee9080d36be1806efea92235` (r4), `0f4db177de3562db43a8966a195a7d3f2a31f8bf42dd3a2551e58083dca5cc9f` (s4).

FOUR completed independent whole-ideal/source/target replays regenerate the ideals separately, check both directions of subspace equality, reconstruct the actual primitive class basis and every affine selected entry, check shifted determinant grids, and re-prove integer-root exclusion at a different prime. They also verify t=-1 (the other parameter five), except the genuine (0,1,6) seed-deletion endpoint: there the free minor vanishes and the NEW opposite level-six seed deletes the actual primitive line, explicitly checked. Replay SHA values are:

    r4 selected7: d5f7029d01d4cc249fb496adb73456a3ecc3554a6c4d1686522c3a4182ea5f07
    s4 selected7: 5674d5fe2025b84f28ae85e1c98bda11e4ac2c6e2fc59fe22d5b15f8a0b812d3
    r4 omitted8:  3b9df1430801b86cd306c439943baaaf71decd20766651816dcf712bec3eeb35
    s4 omitted8:  feebd9565228b5ad74b40f012e374772ecb18a8d3cd3b8e568d8cc1ff4b4481c

This covers all15 representative types and their mirrors on BOTH fourth rows, other parameter >=5. Empty root lists in producer one-sign cases mean nonnegative-root exclusion, not a census of every negative integer root; the replay labels distinguish those scopes.

The corner (4,4) uses the separately NAMED CLASSICAL SYMMETRIZABLE SERRE THEOREM: diag(4,4,1) symmetrizes A(4,4). This classical diagonal import is not a new computation or novelty claim. Therefore no possible exception has r=4 or s=4 either. The regime min(r,s)<=3 is NOT covered by this theorem.

## 7. The precise conditional whole-band consequence

Let R=tau/J in the original realization, and B5(r,s) mean R vanishes on ALL positive/negative levels through five, with the full Cartan boundary retained. If R6 were nonzero, its finite-dimensional Levi submodule would contain a nonzero lowest vector v. Then f1v=f2v=0 and f3v belongs to R5=0, contradicting the complete primitive theorem outside E. Chevalley transport gives the negative level as well. Thus, at every r,s>=4 outside E,

    B5(r,s) => B6(r,s).

The previously written all-parameter B5 composition is still an UNREVIEWED candidate; it is NOT promoted or assumed established here. This implication is not an unconditional band-six solution, still less an all-level or arbitrary-GCM result.

## 8. Assurance and remaining gap

Every conclusion is at the named actual-source/finite-Levi/Witt/PBW interfaces. Finite calculations are exact integers, rationals and finite fields; neither numerical rank nor finite-box sampling supplies the parameter-family statements. Multiple programs and representations were used, but all were written by the same owner, and large-minor producers/replays share FLINT arithmetic. Independent-model review was not performed. Full scientific review/parent disposition remain pending; no novelty/priority clearance or publication is claimed.

The remaining mathematical gaps are the explicit finite exceptional loci, min(r,s)<=3, and the separately unverified predecessor/whole-band inputs. Native 336/436 resultant jobs have not returned a verdict and are NOT consumed. Cancelled slow factorization/full-horizontal-RREF jobs remain uncompleted, not passed. Earlier frozen process findings and quarantines remain historical; no held output is accepted as a premise.

**END — complete-inventory, actually quotiented, cofinite primitive candidate at an explicit source cut; broad original target remains open.**
