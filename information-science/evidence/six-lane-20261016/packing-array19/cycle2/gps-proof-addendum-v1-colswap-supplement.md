# Column-swap WLOG supplement to the GPS written-spec addendum v1

This is a new file, written after host clock read 2026-10-18T14:3x-0700. It edits nothing, including `cycle2/gps-proof-addendum-v1.md` (SHA-256 `dec91dbfeacbf39be9f180400cd1f93c12432dffc2151402c8dbb13e8d89c14f`). Prompted by the Claude review MAJOR 1 relayed by the parent: the mismatch between the ms09 written statement, the probe, and its WLOG.

## Statement

**Notation.** In the ms09 relaxation R09 of addendum §2, the two remaining P1 columns are interchangeable. Write Φ for exchanging them.

**What Φ preserves.** Φ maps a choice (P2, P3, values, x) to (P3, P2, swapped values, b - x).
- Distinctness and compatibility of the pairs are preserved.
- Each row of the table of §2 maps to an entry of the same table.
- (C2) and (C3) exchange with each other, since y2 and y3 swap and x becomes b - x.

**Consequence: ordered vs unordered.** Feasibility over ORDERED pairs (P2, P3) equals feasibility over UNORDERED {P2, P3}.

**Consequence: the search restriction loses nothing.** Suppose some row has s(r) < 0. Let r0 be the lowest-indexed such row.
- Every R09 solution puts r0 in P2 or in P3: s(r0) = -1 needs exactly one pair; s(r0) = -2 needs both.
- Applying Φ when necessary gives a solution with r0 in P2.
- So `c1_L0` (frozen `src/gps1c1_probe_v1.py`, 8e9eaa0a…c52c) loses no solution when it restricts P2 to candidate pairs containing r0.
- When no row has s < 0, it ranges over all ordered pairs.
- Its single count test 0 <= 8 - a - y3 <= b is (C2), and (C3) then follows by Lemma B.

**What is not assumed.** Only Φ is used here: no row or quad permutation, and no change of the distinguished first column.

## Not claimed

This supplement establishes no application or coverage step. The following remain INCONCLUSIVE, as recorded by the parent:
- whether rows_of(sk)[i] matches each ext-list row;
- whether every extend_b generator satisfies T(σr) = π(T(r));
- list completeness;
- the exclusion counts.
