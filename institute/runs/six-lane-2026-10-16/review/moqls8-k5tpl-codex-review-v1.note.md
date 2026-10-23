DISPOSITION: K5TPL-r1=ACCEPT; K5NF-r3-IMPORTS=ACCEPT

**K5TPL-r1**

FATAL: none. MAJOR: none. MINOR: none.

Correctness checks:

- **T1:** The five supports are nonempty by ONB completeness, disjoint by G2, and avoid the aligned cell. Thus each has size ≤3. For the column-0 frame, p=(0,k), k≠0, is off the frame and the excluded cell is (0,0). Both degree bounds, U=[1]⊕U′, and column 1=A follow. (`review/K5_COLUMN0_TEMPLATE_COVER.r1.md:9–20`)
- **T2:** The classification is complete. The degree-2 argument forces the shared extra neighbour and closes its neighbourhood; rank excludes the 3×2 component. Transposition handles degree-2 columns. In the cubic case, the six incidences permit only {3,3} or {2,2,2}; the latter forces ab/ac/bc and then x=y=z. No support pattern is missing. (`review/K5_COLUMN0_TEMPLATE_COVER.r1.md:31–55`)
- **T3:** Sym(A) may change Q1(1,0)’s coefficients, but preserves its required support. The simultaneous column/basis action, square relabelling and common row sort preserve every bridge hypothesis. P0/P1/P2 exhaust the distinguished component; their canonical choices leave sufficient independent freedom for the complementary block. (`review/K5_COLUMN0_TEMPLATE_COVER.r1.md:59–77`; `desk/BINDING_EXTRACT.json:31–33`)
- **T4:** All 16 displayed sequences are reachable and nondecreasing in the encoded order. Both complementary-block decomposition lists are complete. Independently counting gives **10 c064, 3 c096, 3 c112**, with exactly the three identified c112 templates. (`review/K5_COLUMN0_TEMPLATE_COVER.r1.md:84–113`; `code/gram_a.py:248–270`)
- **T5:** The 42 units are precisely V1–V6. Thirteen independently replayed refutations plus the imported c112 refutation suffice conditionally through this **genuine-vector cover**. Template realizability is unnecessary. The separate manifest, unchanged Boolean ledger and K4 caveat are correctly scoped. (`review/K5_COLUMN0_TEMPLATE_COVER.r1.md:117–126`)

Novelty: unestablished by this packet. Significance: a conditional finite semantic reduction; no K4/K5 exclusion follows yet.

**K5NF-r3-IMPORTS**

FATAL: none. MAJOR: none. MINOR: none.

**T6:** The reduced-class definition, invariance, three *normalisation* hypotheses, active-family list, ROWLEX orientation/non-strictness, residual action and square-label formula are correct. P4 remains an underlying reduced-class requirement. (`review/K5_RESIDUAL_NORMAL_FORM.r3-IMPORTS.md:11–38,42–51,63–74`; `review/K4K5_ENCODING_SOUNDNESS.r3.md:103–119`; `desk/BINDING_EXTRACT.json:27–33`)

The V1 decoding and labels 64/96/112 are correct. At line 59, the receipts provide complementary checks: binding C9 verifies variable meanings; the root-cover audit verifies index/sign orientation. Neither supplies additional proof replay. The final bridge statement stays within the accepted imports. (`review/K5_RESIDUAL_NORMAL_FORM.r3-IMPORTS.md:53–59,72–75`; `desk/BINDING_EXTRACT.json:39–49`; `parent/moqls8-k5-root-cover-audit-v1.md:19–23`)

Novelty: documentary clarification. Significance: makes r2’s imports explicit; r2’s projection argument remains separately reviewed.

K5TPL-r1 FATAL=0 MAJOR=0 MINOR=0
K5NF-r3-IMPORTS FATAL=0 MAJOR=0 MINOR=0