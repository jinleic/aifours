# EXCERPT of moqls7-k3-cover-claude-v1.note.md (source sha256 7ab7de84e6d6c7e38de2ea97562860b59834e8b2051d0550d8eab0c28b0479b3; 253 LF-lines by text.split('\n'))
# Prior Claude note (claude-opus-5-5). Omitted: LF4-121 (derivations of Q1-Q5) and LF217-end (scope).
# Lines are VERBATIM, prefixed with their ORIGINAL 1-based LF number. Cite as prior/prior-claude-note.findings-excerpt.md:LF<n>.
# DELTA-AUDIT USE ONLY: these are earlier reviewer findings, not premises and not parent conclusions.

----- original LF1-3 -----
LF1: DISPOSITION: ACCEPT-WITH-FIXES
LF2: 
LF3: Q5 is judged separately because it is an unfrozen draft. Its transport lemma and cut arithmetic are correct, but it needs fixes before any freeze (MAJOR D1–D2).
----- original LF122-216 -----
LF122: ## MAJOR
LF123: Q1–Q4: none. The following apply to the Q5 draft only.
LF124: 
LF125: **D1. AMENDMENT-4.md:8, :23, :28 — the bridge prerequisite is missing.**
LF126: - The C321/C411 CNFs impose G4 on every (square, line) except (1, row 0).
LF127: - A transported configuration satisfies them only if the source triple is heavy in every own ONB. That is justified only for a minimal triple, i.e. after K1 (accepted) and K2 (pending) are excluded (GRAM-ENCODING.r2.md:52-62; LEMMAS.md:75-78).
LF128: - The draft never says so; "surviving heavy K3 configuration" (:28) silently assumes it.
LF129: - *Correction:* add a hypothesis paragraph: "valid only under the G4 bridge: K1 accepted, K2 parent-accepted, encoder G1–G5 bridge accepted; K3 only (14 row/column lines, no L symbol lines; not for non-minimal configurations)."
LF130: 
LF131: **D2. AMENDMENT-4.md:3-4, :20, :22-23, :33-34, :50-51 — certificates are presented as exclusions, and the gate is too weak.**
LF132: - A producer DRAT certificate (cert_r2/A_C321.json:20-25; A_C411.json:20-25) shows UNSAT of one exact A-encoded CNF and nothing more.
LF133: - "contradicting its UNSAT certificate" and "previously checked cube exclusions" overstate this.
LF134: - §3.1 gates on "successful … certificate receipts". It does not require parent acceptance (hash chain, regeneration, encoder bridge), and it does not say whether the pending B route is required.
LF135: - *Correction:* gate on "parent-ACCEPTED exclusions of the exact C321 (d598…8388) and C411 (2b92…ddf2) CNFs, under the stated A-only or A+B standard, with K2 accepted". Rephrase the contradictions as "contradicting the accepted UNSAT of that CNF".
LF136: 
LF137: **Required before any final use of the cuts:**
LF138: 1. K1 accepted and K2 parent-accepted, so that G4 holds for K3.
LF139: 2. Accepted G1–G5 encoder bridge(s), plus the B-map erratum (MINOR 2) if B is used.
LF140: 3. Accepted cover and --sym WLOG (AMENDMENT-2 §1).
LF141: 4. Accepted C321 and C411 certificates.
LF142: 5. A reviewed transport lemma (as corrected) and a reviewed cut generator: literal map per encoder, exactly 238140 distinct clauses, output SHA bound, and the §3.3 control.
LF143: 6. If the cuts are combined with the AMENDMENT-3 lex comparators, an explicit statement that the cut family is H-invariant (MINOR 14).
LF144: 7. A new, regenerated, DRAT-checked UNSAT of the exact strengthened C311 CNF, on the protocol's independent route(s). The old cube proofs certify nothing about it.
LF145: 8. A parent review of the full composition: K1∧K2 ⇒ G4 ⇒ --sym ⇒ three cubes ⇒ {C321, C411 accepted; transport ⇒ cuts; C311+cuts certified}.
LF146: 
LF147: ## MINOR
LF148: 1. **AMENDMENT-2.r1.md:10, :31 — incomplete nonemptiness wording.** "Row 0 is an ONB" and "exactly one nonzero coefficient" omit that the (0,0) coefficient is zero by G1 (column 0). Add it.
LF149: 
LF150: 2. **AMENDMENT-2.r1.md:43-45 vs k3_cubes.py:59-60, :117-126 — B's map is not read or confirmed at runtime.**
LF151:    - "reads each encoder's actual g-variable order … must confirm" is false for B. The wrapper hard-codes the map and checks only nv ≥ 2646 (:126).
LF152:    - Index identity does hold by static reading (Q2(d) above).
LF153:    - desk:24 (A and B appended blocks byte-identical) is tautological, since one vmap serves both; it is not evidence.
LF154:    - *Correction:* record an erratum. Before relying on any B certificate, add a runtime oracle that leaves B untouched. Options: drive B's own --fix-json branch (gram_encB.py:203-215, which emits signed units in allocation order) with probe patterns, or replay the product-definition references (the desk:316-318 pattern) against variable_map.
LF155: 
LF156: 3. **G6-G2-DERIVATION.r1.md:8, :12 — two imprecise sentences.**
LF157:    - At :8, t=(0,0) is absent by G1, not fixed by the cube.
LF158:    - At :12, for collinear (p,t) the text should read "G1+G2 forbid a count of 1, so g(q,t)=0", not "gives g(p,t)=1".
LF159:    - The conclusions at :14 and :21 are right; only the wording needs changing.
LF160: 
LF161: 4. **AMENDMENT-3.r1.md:10, :20 — the invariance argument omits the --sym units and the G4 omission.**
LF162:    - C411's columns(3,4) (k3_lex.py:33) sends the --sym unit 109 = g_1(p,(0,3)) to 145 = g_1(p,(0,4)), which is not a base unit.
LF163:    - That generator preserves the cube CNF only because 145 is a positive C411 cube unit; it does not preserve the base CNF.
LF164:    - *Correction:* state that all generators fix square 1 and row 0, that the --sym units are implied by the cube units, and that invariance is of the cube CNF's g-projection.
LF165: 
LF166: 5. **AMENDMENT-3.r1.md:25-28 — T(X) is undefined.** Define Y_v = X_σ(v), as implemented (k3_lex.py:49, :120).
LF167: 
LF168: 6. **explore/k3lex/A_C311.meta.json:4-7 vs AMENDMENT-3.r1.md:46 — incomplete binding.**
LF169:    - The lex metadata binds neither the source-cube metadata SHA (3b2ab04f…) nor the control-receipt SHA; it records only an in-process "PASS" (k3_lex.py:110, :132).
LF170:    - Both are recoverable via explore/k3cubes/screenA_r1/A_C311.json:16-17 and AMENDMENT-3.bindings.r1.json:8.
LF171:    - *Correction:* add a sidecar binding.
LF172: 
LF173: 7. **AMENDMENT-3.bindings.r1.json:16-18 — stale certificate-driver binding.**
LF174:    - The binding names k3_cube_certify.py (0b291d74…, caps "1800/3600").
LF175:    - Both receipts were actually produced by k3_cube_certify_r2.py at 3600/3600 (cert_r2/A_C321.json:9, :18, :47).
LF176:    - Authority rests on the omitted K3-CERTIFICATION-DRIVER-DELTA.r2.json (GRAM-ENCODING.r2.md:15-16), which no receipt references.
LF177:    - The parent must check that this delta predates 21:39:49 (A_C321.json:2) and bind it.
LF178: 
LF179: 8. **AMENDMENT-3.r1.md:3 vs AMENDMENT-3.bindings.r1.json:2, :14 — freeze order.**
LF180:    - The text says "frozen before the new inputs", but the freeze record already contains the input SHA, so generation came first.
LF181:    - This is harmless (the output is deterministic and bound) but should be recorded.
LF182:    - Similarly, g6_controls_r1.json:2 (20:15:24) postdates the AMENDMENT-2 freeze and the first screen start. It is unbound but not load-bearing.
LF183: 
LF184: 9. **Missing K1/K2 prerequisite statements.**
LF185:    - The prerequisite is absent from AMENDMENT-3 (e.g. :49) and from the receipt scope fields (cert_r2/A_C321.json:61; A_C411.json:61).
LF186:    - AMENDMENT-2.r1.md:5 cites the r1 bridge, whose G4 reference was K1 §8 (gram_enc.py:15-16). That was corrected in GRAM-ENCODING.r2.md:26-27 and LEMMAS.md:69-78.
LF187:    - *Correction:* cite r2/LEMMAS and add "conditional on K2 acceptance".
LF188: 
LF189: 10. **GRAM-ENCODING.r2.md:136-138 — stale status line.** It also suggests certification alone makes an exclusion. Reword to "until certified, parent-accepted and composed with the K2-dependent bridge".
LF190: 
LF191: 11. **AMENDMENT-4.md:33 — unqualified conclusion.** "Every heavy occurrence" must read "every heavy occurrence in an own row/column frame". Nothing follows for other ONBs, because disjointness of the three supports is a line-frame consequence of G5.
LF192: 
LF193: 12. **AMENDMENT-4.md:18-20, :22-23 — under-specified maps.**
LF194:     - Specify the label/column correspondence: b becomes square 2 with S_b sent to {5} (or {4,5}); c becomes square 3 with S_c sent to {6}.
LF195:     - Note that the image satisfies the --sym units (S_1 ⊇ {1,2,3}) and that the target CNF does not impose G4(1, row 0).
LF196: 
LF197: 13. **AMENDMENT-4.md:13 — w_a ≥ 1 is asserted without proof.** Justify it by unit norm plus G1, or by Boolean G3.
LF198: 
LF199: 14. **AMENDMENT-4.md:61 — "selected C311 instance" is ambiguous.**
LF200:     - If the cuts are appended to the lex CNF, state that the cut family is invariant under every row, column and square permutation, hence under H, so AMENDMENT-3.r1.md:33-36 still applies.
LF201:     - §3.3 (:55-57) should also check clause distinctness and the per-encoder literal map.
LF202:     - Cosmetic: missing spaces at :37 and :44-45.
LF203: 
LF204: 15. **Non-load-bearing log hash.** explore/k3lex/screenA_r1/A_C311.json:20 has the same solver-log SHA as explore/k3cubes/screenA_r1/A_C311.json:19, although the return codes differ (−15 vs 0). Identical one-line logs are plausible; the desk should confirm their content.
LF205: 
LF206: ## Status
LF207: 
LF208: | Q | Status | Reason |
LF209: |---|---|---|
LF210: | Q1 | SOUND | 18 assignments in three 6-orbits; residual group and --sym WLOG preserve all base semantics; wording nit only (m1) |
LF211: | Q2 | SOUND | G6 follows from G1/G2 plus units in every case, for both encoders; 70/158/88 match the desk; B map correct by static reading, §3 wording needs an erratum (m2) |
LF212: | Q3 | SOUND | 22 generators stabilise the cube CNF; comparator ⇔ X ≤lex X∘σ; counts exact
LF213: 
LF214: ; lex-min coverage valid; documentation gaps (m4–m5) |
LF215: | Q4 | REQUIRES-FIXES | CNF composition, headers and regeneration correct; binding gaps (m6–m8); missing explicit K2 prerequisites and overstated certificate wording (m9–m10) |
LF216: | Q5 | REQUIRES-FIXES | Transport, forcing, (3,1,1) conclusion and 238140 distinct auxiliary-free clauses correct; needs prerequisites and acceptance gate (D1–D2), frame qualifier, map specification and lex-compatibility statement (m11–m14) |
