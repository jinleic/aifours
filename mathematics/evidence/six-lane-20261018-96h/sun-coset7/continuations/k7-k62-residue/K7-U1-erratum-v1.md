# K7-U1-erratum-v1: correct frontier, explicit remainder weights, labels and pinned navigation (no theorem change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T03:12:00-0700.
- **Overlays:** `K7-U1-v1.md`, sha256 d4e6cdc9e11320bee2456e589459c2b0e961bec466e1b7c05e7ff4003e751965, frozen byte-identical.
- **Source:** parent full re-derivation; Codex `RUN/review/sun7-U1-codex-v1.prompt.stdout.txt` (ACCEPT, 0 FATAL / 0 MAJOR /
  1 MINOR) and Claude `RUN/review/sun7-U1-claude-v1.prompt.note.md` (ACCEPT-WITH-FIXES, 0 FATAL / 1 MAJOR scope sentence /
  7 MINOR). RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`. The MAJOR concerns the frontier
  sentence/title only; both reviews find ROW-1*, CROSS*, LIGHT* and Theorem K7-U1 correct at exactly |M| = 1.
- **Status:** written overlay. It changes no statement of ROW-1*, CROSS*, LIGHT* or Theorem K7-U1 and makes no new
  exclusion claim. No computation, novelty, Lean or human-review claim.

## E-1 (Claude MJ1): title and exact remaining frontier

In the title, replace `(in particular: 2- and 3-markers on one vertex)` by **`(in particular: 2- and 3-markers on one
vertex, no other vertex marked)`**. The theorem's exact hypothesis |M| = 1 was and remains mandatory: a vertex y != z
carrying the 5-marker is outside Theorem K7-U1.

In section 6, first bullet, replace the final sentence starting `With accepted K7-M0 ...` by:

**If this candidate is accepted, then with the accepted K7-M0, K7-M1, K7-Z2 and K7-35 at the exact scopes pinned in
E-5 below, K7 remains open for configurations with |M| >= 2 carrying both a 2-marker and a 3-marker. The 2- and
3-markers either sit on different vertices (5-marker absent, on one of them, or on a third vertex), OR sit together
on one vertex z while the 5-marker sits on y != z. Neither remaining family is excluded by K7-U1.**

The first checkpoint `checkpoint-001-v1.md` candidate-table scope shorthand `6 / m_z` means **6 divides m_z**, not a
quotient. Its working notes concerned only the different-vertex family and did not claim to cover the same-vertex
2/3 + separate-5 family; that family is expressly retained above.

## E-2 (Codex M1, Claude m1): explicit weights for k3 = 3 with an entry 4

In section 1 (b), case `Some alpha_vu = 4 with k3 = 3`, replace the phrase `standard weights give ...` by:

**Put y_z = 0 and weight each of the three R3 elements by 1/3. For the two remaining elements {4, x} use these
explicit weights (not the universal ROW-U half/quarter formula):**

| x | weights on (4, x) | remainder contribution | total contribution |
|---|---|---|---|
| 1 | (1, 1) | 5 | 8 |
| 2 | (1/2, 1/2) | 3 | 6 |
| 4 | (1/2, 1/2) | 4 | 7 |

Feasibility: x = 1 puts the two elements in different coprime classes (no allowed pair); x in {2,4} leaves a
two-element R24 class, whose only allowed non-singleton is that pair, with weights summing to 1. The R3 class is
coprime to this remainder, so the three R3 weights are independently feasible. With y_z = 0 heredity extends them
as in section 1. The k3 = 4 singleton-four case already has explicit weight 1 and total 8 and is unchanged.

## E-3 (Claude m2): LIGHT labels

Rename section 4 LIGHT* items `(L1)`, `(L2)`, `(L3)` to **`(LT1)`, `(LT2)`, `(LT3)`**, and their inverted counterparts
`(L1*)`, `(L2*)`, `(L3*)` to **`(LT1*)`, `(LT2*)`, `(LT3*)`**. Read every LIGHT citation in sections 4-5 in that sense.
`L1 (T1)-(T3)` in the import list and the triangle computations keeps its old meaning: the general triangle rule.
No statement is changed.

## E-4 (Claude m3): how the accepted Z2 proof removed x = 5

In section 6, last-but-one bullet, replace `(and h_z = 0 to kill x = 5)` by:

**`(Z2 removed x = 5 via alpha + alpha* <= 6 forcing x* = 1, which the inverted triangle test kills; a 5-marker at
the centre was allowed)`**.

Here K7-U1 instead removes x and x* in {3,5} globally on W-pairs before CROSS*. This is a description of the old
proof, not an added premise.

## E-5 (Claude m4, m5): pinned results and F7 acceptance

All paths below outside RUN/review are relative to the parent lane
`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7`.

- **K7-M0:** `K7-LFC-INV-v1.md` sha256 45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c with
  `K7-LFC-INV-erratum-v1.md` sha256 7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5, accepted by
  `RUN/review/sun7-lfc-inv-parent-verdict-v1.md` sha256 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18.
  Exact scope: no K7 configuration with M empty.
- **K7-M1:** `K7-M1-v1.md` sha256 6e9b2d09aa5c55698dd96d95266243701ca077c98ec615aa57b648ebf3f95d63 with
  `K7-M1-erratum-v1.md` sha256 4094b53783244e8b824dd64409d28380d0a635e76d74035e361f5ca22a26c510, accepted by
  `RUN/review/sun7-M1-parent-verdict-v1.md` sha256 7121ceeedc1f1b0de8d9642c8f5c2aed052d9f2e83140afee33ffcd2f71ced84.
  Exact scope: exactly one marked vertex whose marker product is odd (markers 3 and/or 5; no 2-marker).
- **K7-Z2:** `K7-Z2-v1.md` sha256 cda7573de2401c220493d55e37fdc09b3292590522fc0258ba9a5ca6e27ecbe7 with
  `K7-Z2-erratum-v1.md` sha256 3aa305553cd44946de32cea5cb2703b1864489a6a12de2154feda4884ee456f9, accepted by
  `RUN/review/sun7-Z2-parent-verdict-v1.md` sha256 0f6b9aa3e0552b0140bf581ac5a4d425b0732bcba639bdc49b61518d5fe5b19c.
  Exact scope: a 2-marker is present and no 3-marker is present, 5-marker anywhere. This verdict explicitly accepts
  the **general T/VFC/F7 rules** used here, and is added as the immediate acceptance reference for F7 (the prior
  written-rule verdict 73a25ba6...9f35 is also accepted but was not embedded in the U1 review packet).
- **K7-35:** `K7-35-v1.md` sha256 5624d9783f5fb0236283a870109ce45c3655123949fd0e6dfcb0546ad517fc5a with
  `K7-35-erratum-v1.md` sha256 b13e1cf28dd55cd0983c5cc8259520e6723206d556dbcad27389ac6aaec66e32 and
  `K7-35-erratum-v2.md` sha256 93f99707c5700ec2f7f1c9f9f088ce00866e02b073c8e38c052650dd1bd20d44, accepted by
  `RUN/review/sun7-K63DE-K735-parent-verdict-v1.md` sha256 1a1c639093dd334cb404a8216ca70a839ea85454978c9fdf354cc5bc577a3919.
  Exact scope: **no 2-marker**, and the 3- and 5-markers are present on distinct vertices; all exponents unbounded.
  It therefore does NOT cover 2/3 on z plus 5 on y != z.

These are navigation/scope references. Theorem K7-U1 does not use K7-M1, K7-Z2 or K7-35 as premises; its own ROW-1*,
CROSS* and LIGHT* were re-proved in the frozen candidate under U1. F7 itself is used at the scope already accepted
in the pinned Z2 verdict.

## E-6 (Claude m6, m7): valuation notation and symmetry

Add to section 0: **`e_z := E + 1, f_z := A + 1, h_z := B`** (the actual valuations of n_z; E,A are the extra
2-/3-exponents beyond the factor 6, B is the 5-exponent). Also **alpha and alpha* are symmetric matrices**: I_ij = I_ji
and lcm(n_i,n_j) is symmetric, and alpha* is the alpha-matrix of the inverted configuration. All uses of edge
symmetry in propagation, W3 closure and CROSS* refer to this fact.

## Unchanged

Theorem K7-U1 excludes exactly |M| = 1. The arbitrary-group lift through R0, all unbounded-exponent arguments and
all four terminal cases stay unchanged. The original proof and every old artifact remain byte-identical.
