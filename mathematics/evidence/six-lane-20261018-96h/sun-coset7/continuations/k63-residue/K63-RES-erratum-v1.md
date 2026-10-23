# K63-RES-erratum-v1: wording of standing fact (F3) and scope of the star remark (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T03:22:35-0700.
- **Overlays:** `K63-RES-v1.md`, sha256 1542a551f6d9787784a2434d18a5aa7275f673b23aab4901a384518206f67515 (frozen, unchanged).
- **Source:** my own full re-read of the frozen file, before sending it to the parent.

## R1: (F3) in section 3
**Defect.** (F3) states that u in O' with x_u in {1, 2, 4} is compatible with no element of T5. This is false when
u = p (the 5-marked vertex of O): type(p) = 5^(h_p) x_p and type(f) = 5^(h_f + 1) share the prime 5.
**Replacement.** "(F3) u in O' with x_u in {1, 2, 4} is compatible with no element of T3 and not with d (by (F1)).
It is compatible with no element of T5 unless u = p. Two such elements u, u' have gcd(type(u), type(u')) =
gcd(x_u, x_u')."
**Effect.** None on the proof: the T5 clause of (F3) is used only in case (1b), where h_d >= 1, so no C-vertex is
5-marked and u != p; cases (2)-(6) have T5 empty (k5 = 0). The last clause (used for the standard weights and in
case (4)) is correct because x_u, x_u' have no factor 5 and at most one of u, u' is 5-marked.

## R2: section 6, scope of the star remark
The sentence "the withdrawn star statement is valid for such v" is asserted only in the setting of section 0 (the
K6.3 residue: 3-marker on d, 2-marker on i*), because Lemma FG is proved only there. No star statement is made for
other K6.3 configurations.

Nothing else in K63-RES-v1 changes.
