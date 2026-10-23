# K7-35-erratum-v1: repair of the mixed-case step in K7-35-v1 section 3 (2) (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T01:10:27-0700.
- **Overlays:** `K7-35-v1.md`, sha256 5624d9783f5fb0236283a870109ce45c3655123949fd0e6dfcb0546ad517fc5a (frozen, unchanged).
- **Source of the finding:** parent full read (IRC at about 01:45 PDT); not yet a CLI review.

## K1: section 3, step (2), after "Hence W3 = F*_t ... and alpha_wu1 = alpha_wu2 in {1, 2}"

**Defect.** The text then treats "these entries are 1" and "these entries are 2" as if the choice were the same for all
three w in W3; ROW-2 (b') only gives, for each w separately, alpha_wu1 = alpha_wu2 in {1, 2}, and the value may differ
between different w.

**Replacement (no case split).** Let u1 be either vertex of W cap F_t. Its three entries towards W3 lie in {1, 2} (by the
per-w statement just quoted, using symmetry alpha_u1w = alpha_wu1), and alpha_u1u2 lies in {1, 2, 4} (u1 is not in W3,
so alpha_u1u2 != 3, and step (1) excludes 5). So every unmarked entry of u1 lies in {1, 2, 4} and ROW-2 (c') applies at
u1: its full row has at least three entries 4. The entries towards W3 are <= 2, so the three entries 4 must be exactly
those towards u2, p and t; in particular **alpha_u1p = 4**. Since alpha_wp = 3 for every w in W3 (ROW-2 (b'), k3 = 2),
the row of p has unmarked entries 3 (towards W3) and an unmarked entry 4 (towards u1), contradicting ROW-1 (b) at p (its
only marked neighbour t carries just the 3-marker): an entry 3 forbids any entry 4. Hence W3 is empty.

This replaces the two sentences beginning "If these entries are 1" and "If they are 2". Nothing else changes.
