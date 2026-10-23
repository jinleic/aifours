# GB necessity / genuine-bridge / adapter — review erratum r2 (x-created)

Incorporates erratum r1 (`review/GB_REVIEW_ERRATUM.r1.md`, SHA256 `7b51788c6881efd339a2a9b10732f1292684e7775773021d33f4482ac77d1c4e`, preserved unchanged) together with the findings of two reviews:
- Codex, `R/n8-gb-necessity-bridge-codex-v1.note.md`, SHA256 `ad9e5f04e9eedcf0f5daaf612010b3bd0fa6e86f786dbcbb3412fe8fe44113fc`: necessity ACCEPT; bridge and adapter ACCEPT-WITH-FIXES, 3 MINOR (E1–E3).
- Claude, `R/n8-gb-math-bridge-claude-v1.note.md`, SHA256 `4aeed1e22213477a220681ec9eff004f73ec6b1caa5f623455d990b4c03d15e9`: necessity and genuine NF ACCEPT-WITH-FIXES, 0 FATAL/MAJOR, 6+6 MINOR (G1–G6, N1–N6).

The originals are preserved unchanged:
- `review/GB_ONE_P4_NECESSITY.r2.md`, SHA256 `b9b4a595ca50b1334419d8584edc128e852dd4f206cd21fc5a07a793a2e72365` (cited "NEC");
- `review/GB_NF_GENUINE_BRIDGE.r1.md`, SHA256 `1a352d364a2e2c68a344735537db7e6f10861e01d520cf75dcbef7a61fbf504b` (cited "BR").

Read each listed line through its replacement. "LF" means the 1-based line of the pinned original.

What does not change: code, flags, byte conventions, formulas, hashes and receipts. In particular the adapter `code/gb_one_p4_r2.py` `5ca7c0da82c5ddd308acbbc2424da1ac6b4a0db08d0571f656eda5e841ffe262` and the GB encoder `code/gram_b_r2.py` `4b593e557fe5b26053537e7107ca5e7a11b3df8ce011bdf78981bc7e068beae0` are untouched. No generation or native launch was made for this erratum.

Status of this text: wording and attribution corrections only. It is not a parent acceptance, not a GB refutation, not proof certification and not an n=8 gate. GB remains HELD.

## Part I — Codex findings (carried verbatim from erratum r1)

## E1 — bridge r1, LF15 (ROWLEX domain)
Original:
> - **ROWLEX:** the rows are sorted ascending non-strictly by Q_1's column-0 support key.

Replacement:
> **ROWLEX:** rows 2–7 are sorted ascending, non-strictly, by the Q1 column-0 support bits in coordinate order 0,…,7, coordinate 0 most significant, False < True, with no secondary key. Rows 0 and 1 are fixed.

## E2 — bridge r1, LF17 (sixteen-template coverage vs. four-template setting)
Original:
> By U and T16 (accepted, `N8_ASSEMBLY.r2.md` §§2–3), every genuine non-classical five-set reaches such a configuration for one of the sixteen templates.

Replacement:
> By accepted U and T16, every genuine non-classical five-set reaches row-0 standard form, SB2 and ROWLEX with one of the sixteen templates. For the following argument, condition on its template belonging to {P1-B1, P1-B2, P1-B3, P1-B5}.

The "Template" bullet at LF14 restricts C to these four. It is read as the conditioning hypothesis introduced by E2, not as a claim that U/T16 produce only these four.

## E3 — necessity r2, LF84 (allocator wrapper)
Original:
> The GB file is unchanged. The adapter subclasses only its clause-storage F: F.new/encode are inherited without

Replacement:
> The GB file is unchanged. `encode` is unchanged. `Sink.new` delegates allocation unchanged to the original `F.new` and adds control bookkeeping; `Sink.c` replaces clause storage with the original CLI serialization.

The rest of LF84–85 stands as written: `Sink.c` writes exactly `join(str(lits)) + ' 0\n'` into a RAM bytearray.

## Part II — Claude findings on NEC (G1–G6) and the stale controls wording

### G1 — NEC LF30–31 (scope of coverage)
Original:
> Every genuine normalised configuration at the corresponding accepted unified/T16 or normal-form leaf has a
> canonical assignment satisfying these GB constraints. Conversely, no arbitrary GB SAT pattern is asserted to

Replacement:
> Every genuine normalised configuration in template C (accepted unified/T16 normal form) has a canonical assignment satisfying the GB template constraints GB_C (defined in N6). The same holds for GB_{C,s} whenever X_s is a permutation matrix. Covering ALL of a P1 template C through the six strengthened inputs needs the separately reviewed GENUINE normal form (BR, as corrected by N1–N6). It does NOT use the accepted GA Boolean-model lemma, which yields no genuine configuration satisfying M_s. Conversely, no arbitrary GB SAT pattern is asserted to supply vectors.

### G2 — NEC LF38–40 (no-classical and allocation line references)
Original:
> - **Constants/G1 (89–97):** one explicit TRUE variable T is forced at36–37. Identical cells map to T;
>   distinct cells sharing a row/column map to−T. Each real row/column is an ONB. No classical-net constraints
>   appear because ngen0 makes the classical list empty. Primary nonconstant g variables name unordered cell pairs.

Replacement:
> - **Constants (89–97):** `glit` maps identical cells to T and distinct cells sharing a row or column to −T. T is allocated first and forced true at 36–37.
> - **Primary allocation:** lines 138–140 allocate every nonconstant g in (s, combinations) order with sorted keys, so all 245 column-0 primaries `('g',s,(0,c),(i,0))` exist.
> - **No classical data:** `classical = list(range(100, 100+ngen))` (line 39) is empty for ngen = 0. The classical families at 53–85, 143–145 and 218–219 therefore emit nothing.
> - **No fixed Gram data:** `fixg = None` skips 153–159. The assert at 217 fixes len(Q) + len(classical) = n − 3 = 5.

### G3 — NEC LF84–85 (how the sink is bound; exact newline), superseding erratum r1 E3
Original:
> The GB file is unchanged. The adapter subclasses only its clause-storage F: F.new/encode are inherited without
> logical edits, while F.c writes exactly the original CLI serialization `join(str(lits)) + ' 0\\n'` into a RAM bytearray.

Replacement:
> The GB file is unchanged. `encode` is a module function that instantiates the module-global `F` (gram_b_r2.py LF35). It is not inherited by a subclass. The adapter therefore REBINDS `gram_b_r2.F` to its sink class immediately before `encode` and restores the original in a `finally` block (adapter LF331–335; same pattern in the n3 control at LF253–257).
>
> `Sink.new` delegates allocation unchanged to the original `F.new` and adds control bookkeeping. `Sink.c` replaces clause storage with the original CLI serialization `" ".join(map(str, lits)) + " 0\n"` (gram_b_r2.py LF251), appended to a RAM bytearray, with no filtering, sorting or deduplication.

Executed evidence that the sink, not the original list storage, produced the bytes:
- n3 parity control (adapter LF249–261). It encodes n=3 with the original `F`, rebinds to the sink, re-encodes, and requires equal variable count, name table, clause count and body bytes (7057 clauses, 1711 variables, body SHA256 `59da8ae983dc032ef7759dd18e1c67b4ec70072243d7de9fabcda34f01e870fb`). Recorded PASS in manifest `evidence/GB_ONE_P4_MANIFEST.r2.json`, SHA256 `4daf8fcf9cbc5645fa74eeafc498484dd4a1aa2397b24f428b081d31050b680d`.
- Full n8 run. LF338 raises if the inherited list `f.cl` is non-empty, and the base body (350550717 B, SHA256 `f5da05206f44ff72e5aeade076820e2de52c9d2352f58b048ded1df76bdbf1b9`) came from `f.body`, which only the sink defines.
- Independent agreement. The parent binder `R/moqls8-gb-parent-binding-v1/GBBINDING.json` (SHA256 `d917203deb29a13e212c290e227a001a695765d080a897141d6dc154d79fc673`, script `bind_gb_v2.py` `188c88de64fa994ca7e212f8d1618da9a0eb3433e2e162a835139bbfa4985f51`) reports the same body bytes as CLI-equivalent output.

A future control asserting the sink object type and header directly would be redundant with these, and is not added here.

### G4 — NEC LF96 and LF113–116 (decode and binding: cite executed receipts)
Original LF96:
> No component is yet reported as run/PASS. Adapterr1 is preserved. Formula emission, flags and all byte-order
Original LF113–116:
> **Hash controls:** flip one template unit in P0-B1 and one M2 literal in P1-B1.M2, preserving clause counts;
> both full formula hashes must change. These are BINDING controls only, not SAT/UNSAT or proof-checker tests.
> **Decode controls:** every appended unit and every M_s literal is checked against the inverse GB OWN table;
> the245(s,c,i) primary entries and TRUE constant are output as a mapping table, alongside the full own names.

Replacement:
> These controls are no longer "not yet run". All of them executed in the admitted adapter run at 2026-10-18T07:46:20-07:00 (rc0; prelaunch receipt `evidence/GB_ONE_P4_RUN.r2.prelaunch.json` `0c6b7e1f4b85fc62039fd0470ff73e537e4acb1b592bea5bc3d836d5f5a2ed05`) and PASSED. Recorded in manifest `4daf8fcf9cbc5645fa74eeafc498484dd4a1aa2397b24f428b081d31050b680d` and own-hash receipt `evidence/GB_ONE_P4_OWN_HASHES.r2.json` `9781c877728b6a6f53511ecdd618eb4fc4ed3e87369398e82892cb4da0d9943f`:
> - **component checks:** conj 4 cases; counter2 and atleast3 for every prefix width 0..8 (511 cases each); 216 signed/constant/alias cases; G3 256; G4 512; P4 256; both wrong-threshold outputs rejected;
> - **storage parity:** n3 PASS;
> - **classical control:** relaxed classical positive control PASS (evaluation only; no unrelaxed SAT claim);
> - **hash flips:** both sign flips changed the formula hash;
> - **decode:** every appended unit and M_s literal decoded through GB's own table, with 245 mapping rows in `evidence/GB_ONE_P4_MAPPING.r2.json` `56aac1e2a2b41690afa8492b982c56572cf164b750f6911eec9cdef2883170ea`; the 7/7 source-derived inverse samples matched.
>
> Byte-level correctness of all 22 appended tails does not rest on that comparison alone. The parent binder GBBINDING (`d917203d…` above) independently decodes every appended literal of all 22 formulas through GB's own name table: field `controls.c_decode_inverse_name_table`, one entry per formula. Its `name_table` record reports TRUE id = 1, 245 distinct primaries in 2..V, an injective table of 7841 entries, and `observation_ids_equal_1568(s-1)+49c+7i-5` = true. The lane mapping file satisfies id(g_s((0,c),(i,0))) = 1568(s−1) + 49c + 7i − 5 for all 245 rows (static check at this erratum, no generation). For example Q2, row 1, coordinate 4 gives 1766, matching Claude's independent prediction. The lane-versus-parent comparison `evidence/GB_ONE_P4_PARENT_COMPARISON.r2.json` `df3fb6e6661f46b5cb9673bfc8750482c69978cf0b64d7ea7224f4a434f0b651` reports ALL 22 MATCH (SHA256, bytes, headers).

### G5 — NEC LF60–62 (unused Boolean-invariance remark)
Original:
> The written Boolean normal-form proof's local G2/G3 premises and primary relabelling apply to these same
> support rules. GB has a different canonical auxiliary extension through its threshold counters and anonymous
> single variables. This observation is a necessity argument, NOT a new parent acceptance of that transfer.

Replacement:
> [UNUSED, not load-bearing] Applying GA's Boolean-model relabelling to GB's rules would need its own invariance argument for GB's P4/atleast3 and G5 auxiliaries. No such argument is made or used. The GB P1 route uses only the GENUINE normal form (BR as corrected), never a Boolean transfer.

### G6 — NEC LF9 and LF25 (what is "the same")
Original LF9:
> ## 1. Exact GB instance and same semantic leaf statements
Original LF25:
> These formulas assert the SAME support facts as their GA counterparts:

Replacement LF9:
> ## 1. Exact GB instance; formulas implied by the same genuine leaf

Replacement LF25:
> These formulas are IMPLIED BY THE SAME GENUINE LEAF as their GA counterparts. The appended primary facts (42 template units; M_s at-most-one binaries) state the same support facts. The complete Boolean formulas differ: GB has no ROWLEX and different auxiliaries, so GB relaxes GA. The two formulas are not claimed to be equivalent or to share models. In particular:

## Part III — Claude findings on BR (N1–N6)

### N1 — BR LF17 (state the authority), extends E2
Original:
> By U and T16 (accepted, `N8_ASSEMBLY.r2.md` §§2–3), every genuine non-classical five-set reaches such a configuration for one of the sixteen templates.

Replacement:
> By U and T16, every genuine non-classical five-set reaches row-0 standard form, SB2 and ROWLEX with one of the sixteen templates. This is conditional on their parent acceptance: unified parent disposition `R/moqls8-unified-parent-disposition-v1.md`, SHA256 `29d17f380416045f73cd4e4b6923e55316bed8a62a45dd6310235cb239f8eaeb`, items 1–3, with its stated conditions. For the following argument, condition on the template belonging to {P1-B1, P1-B2, P1-B3, P1-B5}.

### N2 — BR LF35 (attribute each fact)
Original:
> **Consequence.** X_1 is the P1 template matrix. Rows 1 and 7 are {1,2,3}, row 6 is {2,3}, and rows 2..5 are the B-type list. NF §1 is a purely combinatorial argument from (A), (B), (C) and these X_1 rows, so it applies verbatim. At least the stated number of X_2..X_5 are permutation matrices: ≥1 for B1, B2 and B3, and ≥2 for B5.

Replacement:
> **Consequence.** Row 1 of X_1 is {1,2,3} by SB2, not by the template. Rows 2..7 of X_1 come from the template table: rows 6 and 7 are {2,3} and {1,2,3}, and rows 2..5 are the B-type list. Both of these facts, and the one-counts m, are imported from WMAN `evidence/n8_one_p4_templates_v1/MANIFEST.json` (SHA256 `355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74`) as bound by the parent binding `R/moqls8-one-p4-parent-binding-v1/RESULT.json` (SHA256 `65311ab0b3109412383b47113b36c6a4b3d74f8132fc334cb2f5194b480928b0`). The parent finite receipt `R/moqls8-p1-normalform-parent-v1/RESULT.json` (SHA256 `e075aff8f56994777bda4d893f07c62f20d0598a56d0cd9a5ab08c440a25cbc2`, `template_checks`) records ones = 12, 14, 16, 17 and minimum other-permutation counts 1, 1, 2, 2 for B1, B2, B3, B5. NF §1 is a purely combinatorial argument from (A), (B), (C) and these X_1 rows, so it applies verbatim: at least one of X_2..X_5 is a permutation matrix for B1 and B2, and at least two for B3 and B5. For B3, ≥ 1 is all the proof needs.

### N3 — BR LF52 (template-preservation condition explicit)
Original:
> - **The template and ROWLEX are kept.** NF §4 checks that each displayed pair preserves every Q_1 column-0 support mask in its FINAL row. So the 42 template bits hold for Q'_1, and the ROWLEX keys are row-wise identical.

Replacement:
> - **The template and ROWLEX are kept.** Writing T_i for the template support of Q_1(i,0) (i = 2..7), the move preserves the template if and only if σ(T_i) = T_{ρ(i)} for i = 2..7. This is the Boolean condition of NF §4 (NF r2 LF137–139, "each displayed pair preserves every Q1 column0 support mask in its FINAL row"). It is imported from that accepted text and from the parent finite stabilizer/orbit check `R/moqls8-p1-normalform-parent-v1/RESULT.json` `e075aff8f56994777bda4d893f07c62f20d0598a56d0cd9a5ab08c440a25cbc2` (`template_checks`: group orders 24, 4, 8, 2; orbits as listed; representatives {2}, {2,4}, {2}, {2,3}). It is not re-derived here. Under it, the 42 template bits hold for Q'_1 and the ROWLEX keys are row-wise identical.

### N4 — BR LF62 (M_s means at most one)
Original:
> A permutation X_s means every Q_s(i,0), i = 2..7, has singleton support in {1..7}. That is exactly the property encoded by the 126 binaries M_s.

Replacement:
> M_s (126 binaries) says that each Q_s(i,0), i = 2..7, has AT MOST one support coordinate in {1..7}. "Exactly one" additionally needs nonemptiness, which comes from (A) / G3. Only the implication "X_s is a permutation ⇒ M_s holds" is used here.

### N5 — BR LF64 (cite both sources)
Original:
> **Proof.** By Lemma 1, some X_s (s ≥ 2) is a permutation matrix, and for B5 at least two are. Its label s+2 lies in B. Choose the Lemma 2 moves exactly as NF §4 does:

Replacement:
> **Proof.** By Lemma 1 and NF §1 (NF r2 LF47–78), some X_s (s ≥ 2) is a permutation matrix, and for B5 (also B3) at least two are. Its label s+2 lies in B. Choose the Lemma 2 moves exactly as NF §4 does:

### N6 — BR LF73–75 (define GB_C and GB_{C,s}; keep the GA alternative out of the GB chain)
Original:
> 1. **GB.** Suppose the GB necessity note is accepted, i.e. the canonical GB assignment of a normalised genuine configuration in template C satisfies GB(B_C). By the Proposition, the moved configuration also satisfies the M_s binaries. So GB(B_C ∧ M_s) UNSAT for every s ∈ Rep(C) excludes every genuine configuration in template C. This bridge needs GB's necessity, not NF's Boolean model transformation. GB has no ROWLEX, so omitting it only weakens the GB formula.
> 2. **Input identity.** The six GB strengthened counterparts are exactly these (C,s) pairs; ALL22 GB input identities MATCH (`evidence/GB_ONE_P4_PARENT_COMPARISON.r2.json`).
> 3. **GA alternative (not a replacement unless accepted).** The canonical GA assignment of the moved configuration satisfies F_one and the 42 units (U's accepted necessity and canonical extension). Because X_s is a permutation, it also satisfies the 126 M_s clauses. So GA S_j UNSAT for all s ∈ Rep(C) would also exclude genuine configurations in template C without NF's Boolean auxiliary re-extension. That would remove the m8 dependency list from the trust base of the four P1 leaves, at the cost of excluding only genuine images rather than proving Boolean UNSAT of B_C. The assembly only needs genuine images (`N8_ASSEMBLY.r2.md` §3). Whether to adopt this alternative is a parent decision; until then, NF remains the accepted route.

Replacement:
> **Definitions.** GB_C = the GB base formula (exact flags above) plus the 42 GB-own-name template units of C. GB_{C,s} = GB_C plus the 126 GB-own-name M_s binaries (M_s^GB).
>
> 1. **GB.** Assume parent acceptance of the GB necessity note (as corrected by this erratum). Then the canonical GB assignment of a normalised genuine configuration in template C satisfies GB_C. By the Proposition, the moved configuration also satisfies M_s^GB. Hence UNSAT of GB_{C,s} for every s ∈ Rep(C) excludes every genuine configuration in template C.
> 2. **Input identity.** The six GB strengthened inputs are exactly these (C,s) pairs. All 22 GB input identities MATCH (`evidence/GB_ONE_P4_PARENT_COMPARISON.r2.json` `df3fb6e6661f46b5cb9673bfc8750482c69978cf0b64d7ea7224f4a434f0b651`; parent GBBINDING `d917203deb29a13e212c290e227a001a695765d080a897141d6dc154d79fc673`). This is identity only.
> 3. **GA alternative (OUTSIDE the GB chain; optional, unaccepted).** It imports GA's canonical extension and is not part of the GB argument.
> 4. **Shared trust base; independence only at CNF construction.** The GA and GB P1 routes share:
>    - NF §1 combinatorics;
>    - the NF §4 stabilizer/representative choice and its parent finite check;
>    - the WMAN template table;
>    - the U/T16 reduction.
>
>    The two-encoding independence therefore holds at the level of CNF construction: separately written encoders, own names, auxiliaries and byte streams. It does not hold for these shared mathematical inputs.

## Part IV — hypotheses made explicit (Claude §3)
1. GB necessity starts only after normalisation. Normalisation presupposes non-classicality: A8/Lemma 10 gives a weight-3 entry, which yields the U/T16 SB2-sorted representative.
2. The strengthened inputs exclude only the MOVED configurations. So for the four P1 templates ALL six GB_{C,s} must be refuted, including both for B2 and both for B5. The full GB counterpart also needs the twelve direct GB_C refuted. The four GB P1 template formulas GB_C (C ∈ P1-B1/B2/B3/B5) are input identities only.
3. The setting is fixed at n = 8, five quantum squares, ngen = 0 (gram_b_r2.py LF217).

## Scope
With E1–E3, G1–G6 and N1–N6, both reviews' conditional conclusions stand. Conditional on accepted U/T16 and on parent acceptance of the GB note and the genuine NF:
- every normalised genuine configuration in a T16 template has a canonical GB assignment;
- every genuine configuration in a hard P1 template reaches one of its strengthened GB inputs.

No arbitrary-GB-model transformation, solver result, proof certification or gate closure is claimed. Parent acceptance of the GB necessity note and the genuine NF remains pending, and this erratum does not anticipate it.
