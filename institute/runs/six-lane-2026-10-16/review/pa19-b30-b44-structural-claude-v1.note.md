## Verdict: **ACCEPT**

There are no FATAL or MAJOR findings. The lemma (SOURCE00:15) follows from the definition and the explicit profiles alone, and both case applications are correct. The MINOR items below are editorial and do not change the verdict.

## Step audit

1. **171 saturation** (SOURCE00:17).
   - P0 column: 6 + 5·3 = 21.
   - P1 column: 2·6 + 3·3 + 1 = 22.
   - Total: 105 + 66 = 171 = C(19,2).
   - Each of the 171 pairs agrees in at most one column, and the agreement counts sum to 171. So every pair agrees exactly once. ✓
2. **Row sum 18** (SOURCE00:18). Σ_c(|G_c(r)|−1) counts the (r′, c) agreements with r′ ≠ r. Grouped by r′, that is 18·1. ✓
3. **h contributes 14 + {1,1,2}** (SOURCE00:19).
   - Each P0 column has exactly one size-4 group, so Q_c and every row's membership are well defined. All other P0 groups have size 3, giving 4·3 + 2 = 14 and a residual of 4.
   - P1 groups have sizes 4,4,3,3,3,2 only, so each contribution is 1, 2 or 3. There is no 0 and nothing ≥4.
   - 1+1+1 = 3, and every other multiset except {1,1,2} sums to at least 5.
   - Each P1 column has exactly one size-2 group. So h's two size-2 memberships lie in two different columns, each with a unique partner. ✓
4. **u ≠ v** (SOURCE00:20). If u = v, the pair (h, u) would agree twice. ✓
5. **Avoidance** (SOURCE00:21). If u ∈ Q_i for some i ∈ T(h), then (h, u) agree in column i and in the P1 column. Hence T(u) ⊆ {j}. ✓
6. **Empty partner** (SOURCE00:22). T = ∅ gives 10 from P0, so P1 must supply 8. With one contribution equal to 1, the maximum is 1+3+3 = 7. Equivalently, an empty row's P1 multiset is forced to {3,3,2}, so it never sits in a size-2 group. ✓
7. **Conclusion** (SOURCE00:23). A row with T = {j} cannot be a listed type, because listed types have at least 2 memberships (SOURCE02:6, SOURCE04:26). So such rows are exactly the 4−deg(j) private rows. ✓
8. **b30** (SOURCE00:24, :28).
   - It equals `skeletons[30]` in SOURCE01:1, 0-based. I recounted the whole list: the block sizes 4/6/10/15/14/11/6/3/1/1 match `per_h`, and index 30 falls in the 4-type block (indices 20–34).
   - The listed types pairwise share at most one quad.
   - deg(4) = 3, so there is exactly one {4} row. In the SOURCE02:83–86 and SOURCE04:24–31 row order this is row 13, matching SOURCE03:33.
   - Rows total 4 + 10 + 5 = 19. ✓
9. **b44** (SOURCE00:25, :29).
   - It equals `skeletons[44]` (5-type block, indices 35–48).
   - deg(4) = 4, so there are zero {4} rows. Rows total 5 + 8 + 6 = 19.
   - Every Q4 row shares a quad with h, so h has no admissible partner at all. ✓

## Escape routes tried (all closed)

- **Two size-2 memberships of h in one column:** impossible. Each column has one size-2 group, and each row is in one group per column.
- **P1 contribution 0 or ≥4:** excluded by the explicit profiles (SOURCE00:6, SOURCE01:1), which have no size-1 group. Whatever `L=0` means, the proof does not use it.
- **Partner in Q_j plus another quad:** excluded by step 5.
- **|T(h)| = 5:** outside the hypothesis, and absent from b30 and b44.
- **Encoder semantics:** SOURCE02:14 and :107–111 ("no repeated ordered pair in any two columns") is equivalent to "two rows agree in at most one column." Membership and profiles are built as the definition states (SOURCE02:79–88).
- **Symmetry breaking and placements** (SOURCE02:144–177, :256–500): these only restrict the case and the proof does not use them. Excluding the skeleton case excludes every placement subcase of it.
- **Robustness of the b30 step:** the contradiction only needs "at most one {4} row." That follows from |Q4| = 4 and three distinct non-singleton Q4 rows, even without the fill rule.

## Findings

- **FATAL:** none.
- **MAJOR:** none.
- **MINOR:**
  1. **SOURCE00:19** does not say why each P1 contribution is 1, 2 or 3. Suggested addition: "P1 group sizes are {4,4,3,3,3,2}: no singleton, maximum 4, and exactly one size-2 group per column."
  2. **SOURCE00:24** has two wording issues:
     - "the other nonsingleton memberships" should read "the listed types containing 4."
     - "exactly ONE" should read "at most one (exactly one by the fill rule)," so the step does not lean on the fill convention.
  3. **SOURCE00:6, :15** use `L=0` and "all-P1" without defining them. This is harmless; either define them or say "three P1 columns, no other special profile."
  4. **Checker only, not a proof premise:**
     - SOURCE04:82 hard-codes `'CONTRADICTION'`.
     - Control SOURCE04:86 has no 4-membership row, so it passes trivially through the filter at SOURCE04:42–43. Only the control at SOURCE04:85 tests the "fewer than 2" threshold.
     - Rows with |T| = 5 are silently skipped.

     SOURCE03:103 already disclaims these limits.

**Corrections and counterexamples:** none needed. Every step is forced, and none admits a counterexample.

**Aside (out of scope, not part of the verdict):** the same argument, with residual 3 giving {1,1,1}, also excludes any row lying in all five quads. That covers `skeletons[3]` `[[0,1,2,3,4]]` in SOURCE01:1. The candidate does not claim this, and it would need its own disposition.

## Boundary

- **Audited statically, by hand:**
  - every step and all arithmetic in SOURCE00:15–25;
  - the b30 and b44 contents against a full recount of SOURCE01:1;
  - the private-row and total-row counts, and the pairwise quad overlap of listed types;
  - that SOURCE02:79–88 matches the stated representation;
  - that SOURCE04:24–61 mirrors the lemma;
  - that the SHA strings agree across sources (SOURCE00:9/11/13, the source headers, SOURCE03:4–8 and SOURCE04:15–17).
- **Imported, not audited:**
  - the actual SHA256 digests, which I did not recompute;
  - the contents of the contract and ext.json files: A2 tags, per-skeleton SHAs, the 2858/547 denominators and the 29/6 interval counts. I only checked ⌈2858/100⌉ = 29 and ⌈547/100⌉ = 6;
  - that those placement lists are refinements of exactly these two skeletons;
  - the execution behind SOURCE03.
- **Not assessed:** completeness of the skeleton or profile-multiset enumeration, any other case, and global existence, nonexistence or optimality of PA(19,8,6). The production effect stays NONE until the parent's disposition (SOURCE00:33).
