# Direct P7 under normal index-seven subgroups and a prime-support bound

**Status: WRITTEN, UNREVIEWED.** Let G be a finite group. If 7 does not divide |G|, or if every subgroup of index 7 is normal and |G|/7 has at most seven distinct prime divisors, then G admits no eight pairwise disjoint left cosets whose subgroup indices have every pairwise gcd exactly 7. This is the exact direct P7 condition in the earlier R8/P7 source, not a no-seven-indices claim. If additionally Sun7(G) holds, the earlier R8 implication yields Sun8(G). This is a restricted arbitrary-finite-group result, not a theorem for all groups or a novelty/acceptance claim.

Read the pre-source overlays in order before affected earlier bodies: `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`; `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`; and `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. This proof changes none of them. The earlier `mathematics/evidence/three-area-20261023-96h/parallel-18/sun-coset8/reduction-and-generation-v1.md` SHA `fa0497ae15bd3c765e05123996e4a94bd8038f2be1488b08dc7111f2fd7602c6`, Theorem R8 and §6, already contains the Sun7-relative all-eight gcd-7 reduction and the more general no-normal-vertex observation. Their prior status is not a new discovery; the specialized index-7 argument below is a written recheck. Full prior proof DAG and Sun7 are not independently replayed.

## 1. A normal index-seven vertex is impossible

Suppose for contradiction that eight pairwise disjoint cosets have indices m_i=7a_i with the a_i pairwise coprime, and some U_1 is normal of index 7. Write W=U_1 and π:G→G/W. The quotient has prime order 7. For i≥2, if π(U_i) were nontrivial it would equal G/W, and π(g_iU_i) would contain π(g_1), forcing g_iU_i to meet the entire fiber g_1W. This contradicts disjointness. Hence every U_i≤W for i≥2.

Each g_iU_i then lies in a single W-coset. If two occupied the same W-coset, translating into W would give disjoint cosets of subgroup indices [W:U_i]=a_i and [W:U_j]=a_j. These indices are coprime, so the relative cosets must intersect: the index of the subgroup intersection is both a multiple of their product and at most that product, giving the whole subgroup product. Thus the seven cosets indexed i≥2 need seven distinct W-cosets, but g_1W already occupies one of the seven, leaving only six. Contradiction.

## 2. The cofactor bound

If 7∤|G|, Lagrange forbids an index divisible by 7. Otherwise suppose that every index-7 subgroup is normal. Section 1 shows no subgroup in a direct P7 configuration can have index 7, so every a_i>1. Since m_i=7a_i divides |G|, each a_i divides |G|/7. Their pairwise coprimality forces eight different prime divisors of |G|/7, contrary to the bound of seven. Count 7 itself among these divisors whenever 7² divides |G|; no assumption that 7 occurs to the first power is made.

The restriction 'every index-7 subgroup is normal' is vacuous for groups with no such subgroup, and is not asserted for arbitrary finite groups. A7 and GL3(2) have nonnormal index-7 subgroups and therefore are **not** covered by that condition; their separately written geometric treatments have their own review scopes.

## 3. Optional local Sun7 composition

The prior R8 theorem says Sun7(G) forces every hypothetical Sun8 counterconfiguration to have all eight pairwise index gcds exactly 7. The short written recheck, with its original provenance, appears in §5 of `frontier-20261028-simple-seven-prime-support-v1.md` SHA `815c9e2374a96858f7bfd609aca9f592f293fb14a1822e774333dc41c4eb2faf`. Under the explicit local Sun7(G) assumption, Section 2 therefore excludes a Sun8 counterconfiguration in the present class. The earlier arbitrary-group Sun7 statement `institute/runs/six-lane-2026-10-18-96h/review/sun7-complete-written-composition-parent-verdict-v1.md` SHA `94abd506aec9879e294a5eb84129794af0c7ac78917b091d2f2c113d665c34f2` has only its named same-harness written-composition/errata scope; its entire proof is not independently replayed here.

## 4. Review boundary

A disjoint reviewer should check quotient-fiber reasoning and left-coset orientations, the repeated-unit exclusion, the cofactor prime bound including 7-adic powers, and the precise optional Sun7/R8 dependency. This is not an all-finite-groups P7 theorem, a finite-simple-to-arbitrary-group bridge, a formal proof, a priority result, or historical-hold rehabilitation.
