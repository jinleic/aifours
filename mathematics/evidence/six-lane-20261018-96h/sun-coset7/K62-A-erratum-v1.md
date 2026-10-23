# K62-A-erratum-v1: imports in subset form; explicit inversion (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T02:15:17-0700.
- **Overlays:** `K62-A-v1.md` (sha256 d3cde0bf343cd0c42a51a7e9673fbe10d86dc5ded7ccd5ccf45a2933e07da6b5), frozen.
- **Source:** parent full re-derivation (no mathematical gap found), received by IRC before this file was created;
  same import correction as `K63-D-erratum-v2.md` H5 and `K63-E-erratum-v3.md` J5.

## A1: imports and section 3 (b)
In the import list, replace "ROW-U standard weights and value bound (E8) under ROW-U-deg (M1-erratum F3)" by "the
ROW-U class analysis with its standard weights and the value bound min(N, 4), in the subset form used by the accepted
Theorem K63-U0 Step 1 (`K7-LFC-INV-v1.md` section 5) and `K7-LFC-INV-erratum-v1.md` E8". In section 3 (b) replace "so
ROW-U-deg holds for the five C-neighbours and the standard weights apply" by "so the five C-neighbours of i* have
g = 6 and labels whose pairwise gcds equal the gcds of their alphas, which is all that the subset-form class analysis
(K63-U0 Step 1, E8) uses; its standard weights apply to these five neighbours". The six-neighbour hypothesis
ROW-U-deg is not used. The value table of section 3 (b) is unchanged.

## A2: the inverted configuration, explicitly
Section 2 (last sentence), section 3 (a) and section 4 use the inverted configuration (g_i U_i)^-1. Made explicit:
it consists of pairwise disjoint left cosets of conjugates of the U_i with the same indices n_i, hence the same
gcds, the same class K6.2*, the same distinguished vertices i* and d, the same markers on the same vertices and the
same Hypothesis A (INV (a), LFC-erratum E6); its alpha-matrix is alpha* and its own inverted configuration is the
original one (alpha** = alpha). Therefore Steps 1 and 2 hold for it with alpha and alpha* exchanged; in particular,
where section 3 (a), run for the inverted configuration, invokes "LFC (d) for the inverted configuration", that is
LFC (d) for the original configuration. Section 4's "Steps 1-2 apply verbatim to the inverted configuration" is to be
read in this sense: the alpha*-entries of i* towards C form the multiset {2, 2, 4, 4, 4}.

Theorem K62-A is unchanged.
