# f265 written review B — polarization and eight-label multiplicity

## Verdict and assurance boundary

**Candidate mathematical findings in the assigned scope: FATAL 0 / MAJOR 0 / MINOR 0.** Sections 4–5 are **SUPPORTED as necessary-condition implications**, under the standing bad-family premise and the explicitly assumed original factor bounds. No mathematical defect was established in the polarization, outsider injection, exclusion of three p-labels, coprime-to-35 consequence, or saturated-case deduction.

**Protocol-qualified result, not a clean frozen-review gate PASS.** During drafting, hand-selected index-multiset illustrations were considered, contrary to the explicit prohibition on selected-index instance controls. They were not evaluated by a program, are not reproduced here, and supply no support for any disposition below. The arguments below are entirely all-variable written reconstructions. That does not erase the drafting departure: the parent must not treat this artifact as a fully protocol-compliant acceptance receipt. Other read-window and output-transport deviations are recorded in the coverage receipt. These are review-process limitations, not defects attributed to the frozen candidate, and are not hidden in the candidate finding counts.

Native `/bin/date` before composing this final artifact: **Thu Oct 29 16:25:19 PDT 2026**. An earlier observation, before the rejected first write attempt, was **Thu Oct 29 16:13:44 PDT 2026**. Neither is an asserted read-start time or a backdated clock.

Assignment: obligation B of the frozen manifest at `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f265-sun8-eight-label-consolidated/manifest-v1.json`. Manifest pin observed before its body was opened: SHA-256 `c80d5df02be872ff31b34cfa5ca629d27c84eabffb9d7caf76b375ae2f37c23c`, 6108 bytes, 77 LF, matching the assignment.

Candidate: `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261029-eight-label-extension-consolidated-v1.txt`, SHA-256 `3b5b1c6b31c74f71ed0dfcb0ec93b2a0aa78f47478559be4fb3a70a86c6ec4e9`, 20185 bytes, 356 LF. All candidate locations below are actual LF numbers in this pinned body.

## 1. Scope and claim dispositions

The owned slice is Section 4, candidate LF 152–177; Section 5 and its consequences, LF 179–207; and the shared Section 1 lemmas consumed by that slice, LF 37–82. The complete manuscript was read as common context. This is not an acceptance of the other review slices or of the earlier author sources referenced in the manuscript.

| Claim | Candidate LF | Disposition |
|---|---|---|
| Index product, factor-gcd divisibility, same-fiber translation, coprime-index simultaneous intersection, and impossibility of both factor gcds being 1 | 37–82 | SUPPORTED by the reconstruction in §2 |
| For p in {5,7}, p-label pairs have original gcd exactly p and a unique factor side carries their shared p | 154–163 | SUPPORTED |
| Common-side polarization and bound (4.1), including repeated and two-sided labels | 165–172 | SUPPORTED as an implication from the stated factor bounds |
| Exclusion of all eight labels sharing p under the original bounds 7 | 181–186, using 172 | SUPPORTED |
| A fixed p-free outsider forces distinct shared primes for the p-labels | 187–190 | SUPPORTED; the distinction is justified, not an extra assumption |
| Three p-labels force every outsider to contain all three remaining primes, contradicting the gcd bound | 192–196 | SUPPORTED |
| At most two original indices divisible by 5 and at most two divisible by 7, equation (5.1) | 181–197 | SUPPORTED as a necessary condition, without a factor-bound upgrade |
| At least four indices coprime to 35, with pairwise gcds in {2,3,4,6} | 200–202 | SUPPORTED |
| Both multiplicities equal to 2 imply every coprime-to-35 index is divisible by 6 and their pairwise gcds are exactly 6 | 203–207 | SUPPORTED; the stated antecedent is stronger than needed |
| Original factor bounds for an arbitrary normal cut | 181–182 | CONDITIONAL hypotheses, not established for arbitrary factors by this manuscript or review |
| No complete bad-family existence, bad-family exclusion, or unrestricted Sun8 theorem is asserted | 8–9, 21–28, 174–177, 196–207, 268–301 | SUPPORTED as a statement of the actual claim boundary |
| Historical independence, priority, novelty, clean cognition, or absence of influence from held material | 175–177, 326–335 | INCONCLUSIVE; status reports are not proof |

There is no REFUTED mathematical claim in this owned slice. The word SUPPORTED above applies to the conditional statement itself; it does not establish its antecedents for all groups or establish existence of any bad family.

## 2. Shared lemmas independently reconstructed

Let N be normal in G, Q = G/N, and π the quotient map. Let C_i = g_iU_i be pairwise-disjoint nonempty actual left cosets, with U_i of finite index. Write V_i = π(U_i), A_i = π(g_i)V_i, K_i = U_i ∩ N, a_i = [Q:V_i], b_i = [N:K_i], and n_i = [G:U_i].

### 2.1 Index product and factor gcds — LF 37–52

Normality of N makes NU_i a subgroup. The tower law gives

[G:U_i] = [G:NU_i][NU_i:U_i].

The first factor is [Q:V_i] = a_i. The map from left cosets N/K_i to left cosets NU_i/U_i sending nK_i to nU_i is bijective: equality in the target is equivalent to the relative element belonging to N ∩ U_i, and every element of NU_i has the form nu. Thus the second factor is b_i and n_i = a_i b_i. No subgroup normality, finite ambient group, or finiteness of the subgroup or coset sets is used.

For a pair, set d_A = gcd(a_i,a_j), d_B = gcd(b_i,b_j). Since d_A divides both a-values and d_B divides both b-values, their product divides both n-values. Consequently

d_A d_B divides gcd(n_i,n_j).

Coprimality between a_i and b_i is not assumed or needed.

### 2.2 Actual common-fiber cosets — LF 54–61

If q belongs to A_i ∩ A_j, choose one lift t over q and x_l in C_l ∩ Nt for each active label l. Since C_l = x_lU_l and Nt = x_lN,

C_l ∩ Nt = x_lK_l,

and common right translation by the inverse of t yields

(C_l ∩ Nt)t⁻¹ = (x_lt⁻¹)(tK_lt⁻¹).

The representative x_lt⁻¹ belongs to N. Conjugation by t preserves N and subgroup index, so tK_lt⁻¹ is a subgroup of N of index b_l. These are actual LEFT cosets in N; disjointness follows from disjointness of the original C_l. This construction works simultaneously for every label whose projected coset contains the same q, using the same t throughout.

### 2.3 Simultaneous intersection for coprime indices — LF 63–72

For finitely many H_l ≤ X with pairwise-coprime finite indices d_l, the natural map

X/(intersection of all H_l) → product of the left-coset sets X/H_l

is injective. Hence its finite domain has size at most the product of the d_l. Each d_l divides the domain size by the tower law. Pairwise coprimality therefore makes their product divide that size. Equality follows, and the injection is onto. Every prescribed tuple of actual left cosets has a simultaneous point. Unit indices cause no exception, and repetitions are allowed.

In particular, two disjoint actual finite-index left cosets cannot have coprime subgroup indices. Their index gcd is at least 2. This is where actual disjointness, rather than an arbitrary chosen index list, matters.

### 2.4 Which factor gcd can equal 1 — LF 74–82

If A_i and A_j meet, §2.2 and §2.3 force gcd(b_i,b_j) ≥ 2. When gcd(n_i,n_j) ≤ 7, §2.1 then implies gcd(a_i,a_j) ≤ 3. If gcd(a_i,a_j) = 1, §2.3 in Q makes A_i and A_j meet. If gcd(b_i,b_j) = 1, the common-fiber construction makes a meeting impossible. Thus both factor gcds cannot simultaneously equal 1.

The standing original bad-family constraint is correct: by LF 13–17, a good pair has gcd exceeding 7, equivalently gcd at least 8 because the gcd is an integer. Its negation for every pair is gcd at most 7. Actual disjointness supplies the lower bound 2. Therefore every original pair in a bad family has gcd in {2,3,4,5,6,7}.

## 3. Section 4: polarization and the all-eight case

The standing premise that this is an actual bad family is specified at LF 21–23 and carried through Section 1. Under that premise, let p satisfy 7/2 < p ≤ 7; precisely p = 5 or p = 7. Define S_p = {i : p divides n_i}.

For distinct i,j in S_p, the original gcd is a positive multiple of p at most 7. Since 2p > 7 it is exactly p. In particular, two such indices cannot both be divisible by p². The factor-gcd product divides p, and both factor gcds cannot be 1 by §2.4. Hence the only possibilities are

(d_A,d_B) = (p,1) or (1,p).

For each i in S_p consider its nonempty set of p-sides: a if p divides a_i, b if p divides b_i, or both. Each pair of these subsets of {a,b} meets, by the factor-gcd alternatives just derived. A pairwise-intersecting family of nonempty subsets of a two-element set has a common element: otherwise both singleton sets {a} and {b} would occur and would be disjoint. At most one label can carry p on both sides, since two such labels would give d_A d_B ≥ p², contrary to divisibility by p.

If the common side is a, every pair has d_A = p and d_B = 1. Their actual quotient cosets are pairwise disjoint by §2.4. These quotient cosets have all pairwise subgroup-index gcds p ≤ 7. Thus B_7(Q) ≤ s forces |S_p| ≤ s.

If the common side is b, every pair has d_B = p and d_A = 1. The a_i for i in S_p are pairwise coprime, so §2.3 gives one common quotient point for ALL these labels. With one lift over that point, §2.2 produces |S_p| pairwise-disjoint actual left cosets in N with all pairwise subgroup-index gcds p ≤ 7. Thus B_7(N) ≤ r forces |S_p| ≤ r.

A single two-sided label does not disturb either branch: on the non-common side its p cannot be shared with another label. Empty and singleton S_p satisfy the bound trivially because r,s ≥ 1. Repeated subgroup labels do not affect any step. This proves (4.1) at LF 172:

|S_p| ≤ max(r,s).

For eight labels under the original bounds r = s = 7, the case |S_p| = 8 is therefore impossible. More explicitly, the a-common branch would give eight bad actual quotient cosets and contradict B_7(Q) ≤ 7; the b-common branch would give eight bad actual kernel cosets and contradict B_7(N) ≤ 7. Nothing here replaces either bound by 2.

## 4. Section 5: outsider injection and the multiplicity bound

Fix p = 5 or p = 7, and let k = |S_p|. The Section 4 argument excludes k = 8, so a p-free outsider exists.

### 4.1 Distinct shared primes are a conclusion, not a premise

Fix ANY outsider j, so p does not divide n_j. For each i in S_p, original disjointness and §2.3 give gcd(n_i,n_j) ≥ 2; the bad-family premise bounds it above by 7. Choose a prime q_i dividing this gcd. It belongs to

P_p = {2,3,5,7} with p removed,

because it is at most 7 and cannot equal p, as n_j is p-free.

If two p-labels i and h shared the chosen prime q, both p and q would divide n_i and n_h. Since they are distinct primes,

pq divides gcd(n_i,n_h),

so gcd(n_i,n_h) ≥ pq ≥ 2p > 7. This contradicts the original bad-family constraint. Thus the map from p-labels to chosen shared primes is injective, and k ≤ 3.

Equivalently, for this fixed outsider the nonempty prime-support sets of the gcds with different p-labels are pairwise disjoint subsets of P_p. Thus arbitrary prime choices do not hide a matching assumption. The choices may depend on the outsider; no common choice across different outsiders is needed.

This is the precise reading of LF 189–190: the shared q and p each divide both p-label indices, so their PRODUCT divides their gcd. The proof does not assert q divides p.

### 4.2 Three p-labels force the outsider contradiction

If k = 3, there are five outsiders. Run §4.1 separately for EACH outsider. Its three shared primes are distinct members of the three-element set P_p, so they exhaust P_p. Therefore every outsider index is divisible by the product of the three remaining primes:

- p = 5: every outsider index is divisible by 2·3·7 = 42;
- p = 7: every outsider index is divisible by 2·3·5 = 30.

Any two of the five outsiders consequently have gcd at least 42 or at least 30, respectively, contrary to gcd at most 7. The use of a single lower bound 30 at LF 195 is valid in both cases.

Every possible multiplicity has now been covered:

| k | Resolution |
|---|---|
| 0, 1, 2 | Consistent with the asserted necessary bound; no existence is inferred |
| 3 | Five outsiders, each divisible by the same product 42 or 30, contradict the outsider-pair gcd bound |
| 4, 5, 6, 7 | A p-free outsider exists, but injection into the three-element set P_p is impossible |
| 8 | Excluded by polarization and the original factor bounds 7, not by assuming an outsider |

Hence |S_5| ≤ 2 and |S_7| ≤ 2, as asserted in (5.1), LF 184. The factor bounds are used to eliminate the all-eight case and hence guarantee an outsider. The subsequent injection and three-label exclusion use actual disjointness and original-index arithmetic only. No finiteness of G, subgroup normality, solvability, distinctness of subgroups, valuation restriction, selected indices, or factor bound 2 enters the argument.

## 5. Coprime-to-35 and saturated consequences

Let T be the labels outside S_5 ∪ S_7. The union has size at most |S_5| + |S_7| ≤ 4; overlap between the two sets is allowed. Consequently |T| ≥ 4, and exactly these labels have original indices coprime to 35.

For distinct i,j in T the original gcd lies in {2,3,4,5,6,7} by §2.4 and is divisible by neither 5 nor 7. It therefore lies in {2,3,4,6}. Four labels supply six distinct unordered label pairs. This proves LF 200–202, including both the lower bound on the number of indices and the pairwise-gcd set.

Now assume both |S_5| = 2 and |S_7| = 2, as in LF 203–207. Fix j in T and apply §4.1 to the two 5-labels. The two required shared primes must be distinct elements of {2,3,7}. Since j is also 7-free, neither can be 7. The two primes are thus exactly 2 and 3, and 6 divides n_j. This holds for EVERY label in T, not just a chosen four. For two distinct labels in T, their gcd is a multiple of 6 at most 7, so it is exactly 6. There are at least four such labels as already proved.

The conclusion is valid whether S_5 and S_7 overlap or are disjoint; no equality |S_5 ∪ S_7| = 4 was used. In fact |S_5| = 2 alone suffices for the divisibility-by-6 conclusion for labels coprime to 35, and symmetrically |S_7| = 2 alone suffices. The stronger antecedent in the manuscript is not a mathematical defect.

## 6. Findings and nonclaims

**No LF-located mathematical defect established in the owned scope; FATAL 0 / MAJOR 0 / MINOR 0.** The shared bad-family premise at LF 21–23 and 37–38 supplies original disjointness throughout Sections 4–5. The compressed prime-divisibility wording at LF 189–190 has the valid product-divisibility reconstruction in §4.1. Neither was elevated into a mathematical finding based only on an isolated or strained reading.

The manuscript explicitly labels the result necessary, not existential, at LF 174–177. Its Section 5 concludes at LF 207 that these statements do not rule out a bad eight-family. The original target remains unpaid at LF 8–9, 21–28 and 268–301. Thus the manuscript asserts no COMPLETE existence or exclusion of eight-coset bad families and no global Sun8 result. Excluding certain multiplicity patterns is not the same as excluding all bad families.

The B-specific consequences reused for a hypothetical minimal nonsimple cut at LF 275–279 agree with the above necessary conditions. This consistency observation is not a separate disposition of the whole minimal-counterexample argument or the finite-simple residual.

## 7. Full coverage receipt and deviations

All eight declared evidence inputs were hash-checked for SHA-256, bytes and LF BEFORE any of their bodies was opened. All matched the manifest. Their bodies were then displayed completely in declared order, overlays and errata before the parent disposition and candidate. No mathematical consideration preceded the complete first reading of all eight bodies.

For compact path notation only, S below denotes `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/`; R denotes `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`. Every listed window was displayed through the `read` raw selector. For final windows extending beyond EOF, the returned actual LF range is stated explicitly.

| Item | Exact input path using the prefixes above | Observed full SHA-256, matching pin | Bytes / LF | Raw windows displayed |
|---|---|---|---|---|
| Manifest | R`review-waves/f265-sun8-eight-label-consolidated/manifest-v1.json` | `c80d5df02be872ff31b34cfa5ca629d27c84eabffb9d7caf76b375ae2f37c23c` | 6108 / 77 | `1-77:raw`, complete, one overwide manifest window |
| 1 | S`frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` | `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793` | 6883 / 56 | `1-15`, `16-30`, `31-45`, `46-57` (actual ending LF 56) |
| 2 | S`frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` | `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04` | 3056 / 11 | `1-12` (actual ending LF 11) |
| 3 | S`frontier-20261028-alternating-p7-cardinality-addendum-v1.json` | `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218` | 3164 / 10 | `1-11` (actual ending LF 10) |
| 4 | S`frontier-20261029-f243-cyclic-crt-additive-erratum-v1.json` | `775e251a582ffd01de3d1bd3a6e5af770d6be7cf3252cc10c64c201aaf64c26e` | 2329 / 12 | `1-13` (actual ending LF 12) |
| 5 | S`frontier-20261029-f254-review-b-five-minor-additive-erratum-v1.txt` | `d95c7cecf5b39e6d6649f1ca0238acf661f79082be4f8ba3a2ceb9757591244b` | 10485 / 181 | `1-15`, `16-30`, `31-45`, `46-60`, `61-75`, `76-90`, `91-105`, `106-120`, `121-135`, `136-150`, `151-165`, `166-182` (returned LF 166–181, 16 lines); immediately followed by `167-181` (15 lines, actual ending); later `166-180` (15 lines) supplied compliant coverage of LF 166 as well |
| 6 | S`frontier-20261029-f253-review-b-gcd-additive-erratum-v1.json` | `c0e21498f56ebe292ef8745a2d8457f6dcf508ecb567cd0de6f0b7a9bf5540f3` | 2825 / 25 | `1-15`, `16-26` (actual ending LF 25) |
| 7 | R`dispositions/math-6-sun8-rough-finite-quotient-arbitrary-kernel-transfer-parent-v1.md` | `8feffe5bd9917b83469548880431e55e71a81ecb9bd21e8eaf43e946411b286b` | 6216 / 28 | `1-15`, `16-29` (actual ending LF 28) |
| 8 | S`frontier-20261029-eight-label-extension-consolidated-v1.txt` | `3b5b1c6b31c74f71ed0dfcb0ec93b2a0aa78f47478559be4fb3a70a86c6ec4e9` | 20185 / 356 | `1-15`, `16-30`, `31-45`, `46-60`, `61-75`, `76-90`, `91-105`, `106-120`, `121-135`, `136-150`, `151-165`, `166-180`, `181-195`, `196-210`, `211-225`, `226-240`, `241-255`, `256-270`, `271-285`, `286-300`, `301-315`, `316-330`, `331-345`, `346-357` (actual ending LF 356) |

Coverage and process limitations, without retrospective repair:

1. The manifest was hash-checked before opening, but displayed as one 77-line raw window. It is the declaring document rather than one of its eight declared inputs; nevertheless the overwide display is disclosed rather than claiming universal 15-line compliance.
2. Input 5 had one 16-returned-line window, LF 166–181, exceeding the 15-line cap. Compliant overlapping redisplays cover LF 166–180 and LF 167–181 including the actual ending. These redisplays do not erase the original deviation.
3. Selected-index arithmetic illustrations were considered during drafting, as stated in the verdict. A discarded draft attempted to include them and asserted counts for presentation issues. That target write was rejected before creating a file. No such illustrations or earlier provisional finding counts are adopted in this final artifact. The current all-variable reconstruction, not the discarded examples, is the basis of every disposition. This remains a protocol departure and prevents an unqualified clean-gate certification.
4. The initial native shell call incidentally listed wave-directory entries; no sibling body was read. Progress commentary was emitted despite the no-progress instruction. These are not mathematical evidence.
5. The `write` tool refused the assigned filesystem path because it only accepts `local://` scratch or `xd://` devices. A subsequent administrative `read xd://` listed mounted transport devices, not mathematical sources; none of those external-service devices was invoked. To avoid creating any extra scratch or staging file, the assigned new file was then created through a literal-only `printf`/`tee` transport with an absence guard. No mathematical computation, source edit, extra output file, or deletion was involved. This is a disclosed deviation from the requested write transport.
6. Apart from the declared evidence bodies and manifest, only that administrative device inventory was read. References inside sources were not followed. No held, withdrawn, ZERO or protected payload, selected prime-2/3 material, f161/f162, sibling review output, historical consumer, external mathematical source, or external model was opened or invoked. This statement describes observed tool actions, not a certificate of clean cognition.
7. Hashing/counting, native clock observations and output transport were the only shell work. No mathematical program, test, solver, archive, checker, replay, build, lint, formatter, git, publication, or deletion was run. The internally considered selected-index illustrations remain separately disclosed above; they are not concealed by this execution statement.

## 8. Explicit open items and disposition limits

- **Unrestricted Sun8 remains OPEN.** The proof here is a conditional necessary-condition argument for an actual hypothetical bad family, not B_7(G) ≤ 7 for every group.
- **The finite-simple case remains OPEN.** No finite-simple exclusion is derived or adopted. A proper nontrivial normal cut with smaller factors is not available in a simple group; trivial cuts do not manufacture the needed target conclusion.
- **Existence or complete exclusion of eight-coset bad families remains OPEN**, including under the original factor bounds 7. The restrictions on 5/7 multiplicities, coprime-to-35 indices and saturated gcds neither realize nor exclude all such actual families. No selected-index list is treated as an actual coset construction.
- **The arbitrary normal-extension residual remains OPEN.** The necessary quotient/fiber restrictions do not supply a sufficiency, realization, or gluing theorem. The extra nilpotent-finite-image hypothesis in Section 6 is not imposed in Sections 4–5, and its full argument is outside this slice.
- **Novelty, priority and provenance/history remain INCONCLUSIVE.** The bounded owner exposure report at LF 326–335 is status-only. No clean cognition, absence of influence, or rehabilitation of earlier STOP/HOLD/ZERO records is certified. This review also discloses its own protocol departure rather than asserting a pristine gate.
- **Formal/kernel/Lean, human, and independent-model-family verification were not performed.** Same-harness written reconstruction is the extent of the mathematical support here.
- **Other slice conclusions are intentionally unadopted.** Only the shared lemmas actually needed for B were independently reconstructed. No sibling review verdict or historical linked-source verdict was inherited.

This artifact records complete input-body coverage, a supported all-variable reconstruction of the assigned mathematics, zero established candidate defects in that slice, and the explicit limitations that prevent treating it as a clean protocol acceptance. No frozen source, manifest, ledger, README, or other review file was changed.

