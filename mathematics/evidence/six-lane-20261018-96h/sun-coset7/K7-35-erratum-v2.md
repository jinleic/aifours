# K7-35-erratum-v2: contributions in ROW-2 (b'), explicit inversion in step (3), imports (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T02:04:19-0700.
- **Overlays:** `K7-35-v1.md` (sha256 5624d9783f5fb0236283a870109ce45c3655123949fd0e6dfcb0546ad517fc5a) and `K7-35-erratum-v1.md` (sha256 b13e1cf28dd55cd0983c5cc8259520e6723206d556dbcad27389ac6aaec66e32; time label withdrawn by
  `evidence/timing-addendum-v1.md`, sha256 030192f2e21f7d3a46c4f73f90e40310327326ef912612eff7ac1f4b812ba5d7). All frozen.
- **Source:** hostile reviews RUN/review/sun7-three-written-codex-v1.prompt.stdout.txt (Codex MAJOR D1) and RUN/review/sun7-three-written-claude-v1.prompt.note.md (Claude MINORs), relayed by the parent.

## K2 (Claude MINOR K-1): ROW-2 (b'), k3 = 3 with x = 1, and k3 = 4
The totals add p's *weight* (2/3) where its *contribution* y_p alpha_wp belongs. Corrected: for x = 1 the
contribution of p is 1 (alpha_wp in {1, 5}: y_p = 1, contribution >= 1), (2/3) alpha_wp >= 4/3 (alpha_wp in {2, 4}),
or 1 (alpha_wp = 3, y_p = 1/3); so the total is >= 3 + 4/3 + 1 + 1 = 19/3. For k3 = 4 and alpha_wt = 4 the same weights
on p give total >= 4 + 4/3 + 1 = 19/3. Both exceed the bound 6 that the proof needs (LFC (d) is strict).

## K3 (Claude MINOR K-2): step (3), the inverted configuration
Replace "Steps (0)-(3) apply verbatim to the inverted configuration (same markers, alpha** = alpha)" by: "Steps (0)-(3)
apply to the inverted configuration with alpha and alpha* exchanged: it has the same labelled indices (INV (a), E6),
its own inverse is the original configuration (alpha** = alpha), so wherever step (0) used LFC for the inverted
configuration it now uses the original LFC; ROW-1 is applied to the alpha*-rows at t and at p through the ROW-1-deg
transfer, exactly as in `K7-M1-erratum-v1.md` F6. This gives |A4*(v)| >= 3 for all v."

## K4 (Claude MINOR K-3): imports
Add to the import list: `K7-LFC-INV-erratum-v1.md` E1 (L0.2/L0.3: 1 <= alpha_ij <= g_ij - 1, so every alpha lies in
{1, ..., 5} in K7), which the proof uses throughout.

Theorem K7-35 is unchanged.
