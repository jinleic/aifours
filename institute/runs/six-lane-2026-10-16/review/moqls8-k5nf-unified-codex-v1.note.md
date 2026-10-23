DISPOSITION: UNIFIED-r2=ACCEPT; DELETIONS-v1=ACCEPT

Dispositions concern the written bridge and deletion specification only. Target hashes and the inspected import-copy hashes match their pins.

**UNIFIED-r2**

FATAL: none. MAJOR: none. MINOR: none.

- **U1 — A8 is imported with the accepted quantifiers.** `review/N8_UNIFIED_ONE_P4_BRIDGE.r2.md:38–51` correctly requires five MOQLS and **all** entries of **all** squares to have weight ≤2 in one row-standard frame. The underlying argument holds: sequential Lemma-10 replacements preserve orthogonality and row 0; the four classical replacements give six net classes; Lemma 3 applies on every line; the resulting simple bipartite graph is 6-regular, connected because two a-vertices share ≥4 neighbours; `(0,a)` excludes the full support class (`review/PROOF_K1_K2.r1.md:38–48`; `review/PROOF_K1_K2.r2.md:23–48`). Classicality matches the source: separate square unitaries and entry phases make “all weights 1 in row-standard form” equivalent to a classical set (`sources/2607.12933v2.raw.txt:220–225`). Its contrapositive with W8 therefore supplies a weight-exactly-3 entry.

- **U2 — Normalisation works for an arbitrary non-classical five-set.** The moves at `review/N8_UNIFIED_ONE_P4_BRIDGE.r2.md:55–69` preserve the required properties. After moving the witness to `(1,0)`, disjointness and nonemptiness force the partition \(3+1+1+1+1=7\). A permutation fixing 0 maps the four singletons to 4,5,6,7 in their existing square order; no further square relabelling is needed there. Sorting rows 2–7 preserves the witness and establishes the encoder’s non-strict ROWLEX (`code/gram_a.py:248–281`). No reduced-K5 or other-square P4 hypothesis enters.

- **U3 — The canonical extension satisfies every retained family.** G2 follows from mutual orthogonality; G3 from changes between ONBs; G4 from zero/single-term Parseval; G5 from equal rays. Constants, AND, u5 and lexeq receive consistent defining values (`code/gram_a.py:63–76,127–138,150–232,248–270`). Choose Q1’s witness flag true and its other flags false: every six-subset of eight coordinates intersects its three-element support. For squares 2–5 choose **all** flags false. Source inspection proves those variables occur positively only in their ALO and negatively in their 28 implications; subsequent families never reference them (`code/gram_a.py:233–281`). The desk census corroborates this; it is unnecessary as a premise. The assertion at `review/N8_UNIFIED_ONE_P4_BRIDGE.r2.md:33–34` is sound.

- **U5 — Template coverage extends beyond reduced K5.** Both degree bounds use five aligned, nonempty ONB supports sharing seven available positions. The component classification and the \(6+6+4=16\) templates then follow without other-square non-classicality (`review/K5_COLUMN0_TEMPLATE_COVER.r1.md:9–55,66–109`). Explicitly,
  \[
  Q'_s(i,\sigma(j))=P_\sigma Q_s(i,j),\qquad
  s\mapsto \sigma(s+2)-2\quad(s\ge2).
  \]
  For \(\sigma\in\mathrm{Sym}(A)\times\mathrm{Sym}(B)\), this preserves standard form, restores singleton labels, preserves Q1’s witness support **as a set**, and permits the row re-sort. It need not fix the witness vector. Thus the earlier relabelling/Sym(A) documentation concerns conceal no gap here. TPL MINOR 2’s reduced-class restriction remains relevant to the **old-F certification claim**, but does not restrict this new argument; the earlier c112 citation concern is irrelevant because c112 is not imported.

- **U6/U7 — The consequence is logically complete and conditional.** Every hypothetical counterexample yields an assignment satisfying one of the 16 weakened formulas (`review/N8_UNIFIED_ONE_P4_BRIDGE.r2.md:86–101`). All 16 require new strict refutations and independent parent replay. Since \(F_{\mathrm{one}}\subset F\), neither old c112 acceptance nor the 13 old-F template results discharge any new case. A proof checked against old F’s input is not thereby certified against the weakened input. Neither Boolean coverage nor whole-base \(F_{\mathrm{one}}\) UNSAT is needed. R2, R1 and `README.md:373–390` are consistent; “FULL n8 instance” correctly describes the conditional conclusion’s scope.

**DELETIONS-v1**

FATAL: none. MAJOR: none. MINOR: none.

- **U4 — The specification is consistent.** `evidence/UNIFIED_ONE_P4_DELETIONS_v1.json:8,12–17` correctly uses original zero-based clause indices, clause numbers +1 and file lines +2. Source counting gives 5,732,160 clauses before P4. Each square contributes \(56\cdot28+1=1569\), yielding exactly the five stated ALO indices in square order (`code/gram_a.py:233–247`). Every ALO contains its square’s 56 positive off-row-0 flags. Q1 is kept. The proposed headers correctly retain 509,915 variables and give 5,740,226 clauses, or 5,740,268 after 42 units.

- The five printed line hashes agree with `desk/DELETION_EXTRACT.json:19–96`. The original CNF and full compressed name table are absent from this snapshot; their byte-level verification was **not independently performed here**. “Read/hash once” and “independently identified” remain reported provenance, not premises of this audit. The same qualification applies to the bridge’s `:27–29`.

- **Generator receipt obligation:** `evidence/UNIFIED_ONE_P4_DELETIONS_v1.json:19–20` specifies a future result. The receipt must bind the exact source bytes/header/count and name table; verify all five original-index line hashes including LF and literal meanings; delete exactly four lines; retain Q1 and every remaining clause byte in original order; preserve variable numbering; and bind the resulting header, size and SHA. Each case must additionally bind its exact 42 units and the CNF delivered to solver/checker, followed by independent parent replay.

Novelty: not established by this static audit. Significance: a conditional route covering arbitrary non-classical five-sets; no result on Problem 16, K4 or K5 is established here.

UNIFIED-r2 FATAL=0 MAJOR=0 MINOR=0
DELETIONS-v1 FATAL=0 MAJOR=0 MINOR=0