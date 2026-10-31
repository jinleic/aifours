# Conditional assembly: arbitrary-group Sun8 from Sun7, R8, descent and a simple-group P7 census

**Status: CONDITIONAL ASSEMBLY, UNREVIEWED.** This note does not prove arbitrary-group Sun8 unconditionally and claims no adoption. It records the exact implication obtained by combining the following, each with its own status:

- three prior interfaces: an arbitrary-group Sun7 statement, the R8 implication, and finite-core reduction with actual-P7 normal-section descent;
- the classification of finite simple groups, at statement level;
- a census of finite simple groups carrying no direct P7 configuration, assembled from the components C1–C6 in §2. Several components are unreviewed owner candidates.

If every premise and component holds, then Sun8 holds for every group: every eight pairwise disjoint left cosets of finite-index subgroups have two subgroup indices with gcd at least 8. Any premise or component may still fail review; the conclusion is exactly as strong as the weakest one.

## 0. Source order and provenance

Read in order before affected earlier bodies: `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`; `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`; and `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. The false all-alternating seven-index claim stays withdrawn; A7 genuinely has seven disjoint index-7 cosets, and so does GL3(2). The owner's preview frontier `frontier-20261028-sun-wide-search-preview-frontier-v1.json` SHA `4ca6a3bb90795334dcd5783463863efe3b194facf1ed92f58f14f44e8689a2e6` is cited. Its displayed snippets are NONINPUT and are not used, reconstructed or searched for. The R8 and descent mechanisms below are prior work, credited as such. No historical hold, process finding or review is modified.

## 1. Premises and the implication

- **(S7)** Arbitrary-group Sun7, at the written-composition scope of `institute/runs/six-lane-2026-10-18-96h/review/sun7-complete-written-composition-parent-verdict-v1.md` SHA `94abd506aec9879e294a5eb84129794af0c7ac78917b091d2f2c113d665c34f2`. Its full proof DAG is not replayed here.
- **(R8)** Relative to S7, every Sun8 counterconfiguration has all 28 pairwise index gcds equal to 7. This is Theorem R8 of `mathematics/evidence/three-area-20261023-96h/parallel-18/sun-coset8/reduction-and-generation-v1.md` SHA `fa0497ae15bd3c765e05123996e4a94bd8038f2be1488b08dc7111f2fd7602c6` (§3), rechecked in writing in `frontier-20261028-simple-seven-prime-support-v1.md` SHA `815c9e2374a96858f7bfd609aca9f592f293fb14a1822e774333dc41c4eb2faf`, §5.
- **(D)** Finite-core reduction and actual-P7 normal-section descent. A finite group carrying direct P7 data has a nonabelian simple composition factor carrying direct P7 data; a cyclic factor would have to be C7 with eight nonempty disjoint singleton cosets, which is impossible. Same-harness parent support at its scope: `institute/runs/three-area-2026-10-23-96h/sun8-normal-section-parent-v1.md` SHA `8a8480e2d66f0098fc80ae2960bafcdab36a9976e80b671ddee01c5048fec475`.
- **(CFSG)** Every finite nonabelian simple group is alternating, sporadic, the Tits group ²F4(2)′, or of Lie type, possibly in several isomorphic descriptions. Statement-level import.

**Implication.** Suppose some group fails Sun8. By (D) there is a finite quotient with the same eight indices and disjointness. By (S7) and (R8) its eight indices have all pairwise gcds 7, i.e. it carries direct P7 data. By (D) some finite nonabelian simple composition factor S carries direct P7 data. By (CFSG) S lies in one of the classes of §2, each of which carries no direct P7 configuration. Contradiction. □

## 2. The census: no finite nonabelian simple group carries direct P7

| | Class | Reason no direct P7 | Status |
|---|---|---|---|
| C1 | A5, A6 | 7 does not divide the order | elementary |
| C1 | A7 | written A7 argument, §3 of `frontier-20261028-simple-seven-prime-support-v1.md` SHA `815c9e23…`; also §4 of `frontier-20261028-alternating-small-written-sun8-v1.md` SHA `cb2c2ae8…` | unreviewed written |
| C1 | A8–A13 | Sun8 from criterion (i) of the f151 disposition `institute/runs/three-area-2026-10-27-96h/dispositions/math-6-sun8-source-free-support-criteria-parent-v1.md` (μ≥8, at most two primes above 7) | same-harness parent support |
| C1 | A_n, n≥14 | four proper indices force a gcd ≥9 | parent disposition `math-6-alternating-n14-nagura-jordan-parent-v1.md` SHA `f7c0c3ed…`, conditional on the Nagura and Jordan statements |
| C2 | M11, M12, J3, Tits group | 7 does not divide the order | exact orders |
| C2 | M22, M23, M24, J1, J2, HS, McL, Suz, Co3, Co2, Co1, He, Ly, Ru, O'N, HN, Th, Fi22, Fi23 | no subgroup of index ≤7, since \|S\| does not divide 2520; the eight pairwise coprime cofactors a_i>1 would need eight distinct primes of \|S\|/7, but only at most 7 occur | exact orders; elementary argument |
| C2 | J4, Fi24′, B, M | a Sylow r-subgroup has a unique maximal overgroup (r=29, 29, 47, 71; H=29:28, 29:14, 47:23, L2(71)), so no three proper subgroups have pairwise gcd ≤7 | BBGT Table D (statement import) |
| C3 | Lie type, characteristic ≠7, not PSL3(2) | no three proper subgroups with pairwise index gcd exactly 7 | `frontier-20261029-lie-type-away-from-seven-v1.md` SHA `d2af4a0d…`, unreviewed |
| C4 | Lie type, characteristic 7, not PSL2(7) | exceptional groups by unique overgroups; classical groups by odd-index reduction; PSL2(49) by prime support | `frontier-20261029-lie-type-characteristic-seven-v1.md` SHA `be029572…`, unreviewed |
| C5 | PSL3(2)≅PSL2(7)≅GL3(2) | Sun8 holds, and direct P7 is an eight-coset family with all gcds 7<8 | `frontier-20261028-gl32-sun8-geometric-v1.md` SHA `d7c18486…`, unreviewed |

Groups with several descriptions are covered through at least one of them, for example A5≅PSL2(4)≅PSL2(5), A6≅PSL2(9)≅Sp4(2)′, A8≅PSL4(2), PSU4(2)≅PSp4(3), G2(2)′≅PSU3(3) and ²G2(3)′≅PSL2(8). The derived groups Sp4(2)′, G2(2)′ and ²G2(3)′ are reached only through those isomorphisms, and the Tits group through C2.

**Sporadic data.** Orders were taken from the pinned page `frontier-20261029-wikipedia-sporadic-group-source.html` SHA `b22e8da1b42c3bf62bbfacff1bc795bafad3932527dff941a000eca907f349af`, a secondary source summarizing the ATLAS. The author's checker `frontier-20261029-sporadic-support-check-v1.py` SHA `a77eaf9a659e683262206f4742c09c0bca1c8d92306585745a7fe40d804fed14` (3422 bytes) ran in the author's eval kernel. It verified that each stated factorization multiplies to an order printed on that page, that no order divides 2520, and that the coverage partition above is complete. The four Table D rows were extracted from the pinned BBGT HTML `frontier-20261029-bbgt-2307.13976v2-source.html` SHA `6cf5530f8386133e7208e6e0b77b1b44de78d8546549f2c3faf5144d403f9bfc`. Lemma U of the characteristic-7 packet converts a unique maximal overgroup of a Sylow r-subgroup, r>7, into the three-index exclusion, since every proper subgroup index of a sporadic group is at least 8.

**Prime-support argument (C2 middle row).** If S has no subgroup of index ≤7, a direct P7 configuration has indices 7a_i with pairwise coprime a_i>1 dividing |S|/7. Each a_i needs its own prime divisor of |S|/7, so |S|/7 needs at least eight distinct prime divisors.

## 3. What remains unpaid

1. Independent review of the unreviewed components: A7 (815c §3 or cb2c §4), PSL3(2) (d7c18486), Lie type away from 7 (d2af4a0d), and Lie type in characteristic 7 (be029572). The latter two rely on standard structure theory and on the Maslova and BBGT classifications.
2. The premises S7 (full DAG not replayed), R8 and D (same-harness support at their own scopes), and the statement-level imports CFSG, Nagura, Jordan, BBGT, Maslova and Zsigmondy. Their proofs are not replayed.
3. No Lean or formal verification, human or independent-model-family review, or priority search has been done. The assembly is not adopted, and no unconditional or novelty claim is made.

A reviewer should check, beyond the components: completeness of the case split under CFSG, including exceptional isomorphisms; that each component excludes the eight-disjoint-coset direct P7 definition rather than a different P7 notion; the sporadic partition; and that the implication in §1 uses (S7), (R8) and (D) exactly at their recorded scopes.
