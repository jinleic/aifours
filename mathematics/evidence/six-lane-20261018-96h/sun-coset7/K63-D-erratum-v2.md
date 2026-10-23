# K63-D-erratum-v2: H2 (D5 Step 2 certificate), D5 Step 1 wording, D0 (a) wording, imports (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T02:04:19-0700.
- **Overlays:** `K63-D-v1.md` (sha256 f4027779f19a4733614f543d56a4cf596af9383f04510fbc725a5a7a3ebed255) and `K63-D-erratum-v1.md` (sha256 75478241f060873f3911b897ad65a41cb46a3637dd8d15bfe8e09f3e7f3dae90; its time label is withdrawn by
  `evidence/timing-addendum-v1.md`, sha256 030192f2e21f7d3a46c4f73f90e40310327326ef912612eff7ac1f4b812ba5d7). All frozen.
- **Source:** hostile reviews RUN/review/sun7-three-written-codex-v1.prompt.stdout.txt (Codex MAJOR D1) and RUN/review/sun7-three-written-claude-v1.prompt.note.md (Claude MINORs), relayed by the parent.

## H2 (Codex MAJOR D1 = Claude MINOR D-1): D5 Step 2, the marked neighbour may carry both the 2- and the 3-marker
**Defect.** "The marked neighbour c is compatible only with d, and only when m_c is a power of 2 and alpha*_vd = 2"
omits m_c = 2^E 3^F (E, F >= 1), possible when |M_C| = 1 and one C-vertex carries both markers. Then
gcd(m_c w_c, 5^(h_d) w_d * 2) = 2, so {c, d} is allowed and the "otherwise" weights y_c = y_d = 1 are infeasible
(Codex: all w = 1, n_v = n_u = 6, n_x = 36, n_d = 15, labels 1,1,1,1,6,10).
**Replacement.** "The marked neighbour c (label m_c w_c with m_c {2,3}-smooth) is compatible only with d, and only when
2 | m_c (m_c = 2^E or 2^E 3^F) and alpha*_vd = 2: then y_c = y_d = 1/2 gives 1/2 + 2 units. Otherwise (m_c odd, or
alpha*_vd = 1) c and d are coprime to every other label and y_c = y_d = 1 gives 1 + 2 alpha*_vd >= 3 units. With the
>= 4 unmarked units the total is >= 4 + 1/2 + 2 = 13/2 > 6 (and >= 5 + 2 alpha*_vd >= 7 if v has no marked
neighbour)." The conclusion of Step 2 is unchanged.

## H3 (Claude MINOR D-1, second part): D5 Step 1 wording
"(m_x a power of 2 or of 3)" should read "(m_x {2,3}-smooth)". The conclusion is unaffected: m_x has no prime 5, so
x's label is coprime to the fives and to lambda_d = 5^(h_d) w_d.

## H4 (Claude MINOR D-2): D0 (a) wording
"Their value is >= 5 if some alpha = 5" should read "if some **unmarked** alpha = 5" (the marked neighbour has y = 0;
e.g. a marked x with alpha_vx = 5 and unmarked row (1,1,1,1) gives 4, not 5). The bound >= 4 used in the sum still
holds in every sub-case.

## H5 (Claude MINOR D-3): imports
In the import list, replace "(used only for neighbours whose labels have alpha-gcds, under hypothesis ROW-U-deg of
`K7-M1-erratum-v1.md` F3)" by: "applied, in the subset form, to a set of N in {4, 5} C-neighbours of v with g = 6
whose labels have alpha-gcds, exactly as in the accepted Theorem K63-U0 Step 1 (`K7-LFC-INV-v1.md` section 5: the
class analysis needs only that these neighbours are unmarked with g = 6) and `K7-LFC-INV-erratum-v1.md` E8 (value
bound min(N, 4), stated there for K63-U0 Step 1)". ROW-U-deg (six-neighbour form) is not used.

Theorem K63-D is unchanged.
