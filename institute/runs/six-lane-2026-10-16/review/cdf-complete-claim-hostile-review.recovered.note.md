VERDICT: ACCEPT-WITH-FIXES

All six finite existence claims are correct. My code-free hand check of 801 and 901 found no failure, and the Lean statement expresses the definition faithfully. Every fix concerns ledger synchronisation, provenance wording or snapshot binding; none affects validity. Disclosure, as before: I am the model that wrote `cdf-claude-verifier-v1/checker.py`. The hand check below used no code.

## Fatal findings
None.

## Major findings
None.

## Minor findings

**m1. "Met … pending" contradicts itself.**
- **Where:**
  - [01] Headline, info paragraph: "met the same gate … pending one review".
  - [01] info-2 Status cell: "Gate met … pending".
  - [00] FRONTIER: "This meets … subject to the pending hostile review".
- **Problem:** [22] lists a hostile cross-vendor review as *required*, so the gate cannot be "met" while that review is pending.
- **Fix:** after recording this note, write "met; complete-claim hostile review ACCEPT-WITH-FIXES (‹link›)". Also add this review as a row in the [00] Verification table.

**m2. The ledger is stale against the verdict.**
- [01] info-2 "Verification level" says "901 replay pending". [11] shows it byte-identical, finished 00:29:10.
- [01] Next actions item 2 lists the 901 replay and the Lean parent replay as open. [20] finished 00:23:10.
- The info-2 row never mentions the parent-replayed Lean proofs.
- The title says "state at 2026-10-16 PT", but the contents run to about 00:29 on 2026-10-17.
- **Fix:** sync [01] with [00].

**m3. The replay summary drops qualifiers.**
- [00] FRONTIER says "parent source-rebuild/seed replay for all six". It omits that 801 was replayed from a later frozen source, not the discovery source.
- The [00] Verification table has an 801 replay row but no 901 row.
- **Fix:** append "(801 from a later frozen known source)". Add a 901 row citing [11]: source `68028470…`, binary `b1f56985…`, seed 41, 850.6 s, recheck VALID.

**m4. 801/901 provenance wording** ([00] "801 provenance caveat" and "901 provenance").

The substance of the 801 caveat is adequate. It needs no stronger warning, because validity does not depend on provenance. Three clarifications are needed:
- **(a) Which worker binary.** "Obtained the same binary hash as the worker" is ambiguous. State whether that hash is of the discovery binary (and when it was recorded) or of a post-discovery rebuild. Only the former bears on the original run.
- **(b) Different invocations.** [10] and [11] call `cdf_mq4` with different final arguments (`1` vs `0`). State what the 801 setting does (the verdict mentions a dump-only mode). Also state, after a scan, that the frozen source embeds no witness blocks; if it did, a byte-identical replay would not evidence generation.
- **(c) 901 freeze timing.** "Already-frozen … No source caveat" rests on a post-hoc check that the current hash equals the frozen copy. Either cite the frozen copy's creation time relative to the 23:42:00 run start, or write "no known source caveat; reproducibility per [11]".

**m5. Snapshot excerpts are unbound.**
- [22] gives no SHA-256 for the `contract.json` and `transitions.json` it was extracted from.
- [20] is trimmed. It shows no hashes for the 14 rebuilt modules, `ParentAudit.lean` or the toolchain, so I cannot tie the replay to [12]–[15] and [19].
- **Fix:** add the source hashes to [22]. Add per-module hashes to the snapshot and state that they equal the header hashes of [12]–[15] and [19].

**m6. The ledger lacks the corollary qualifier.**
- [00] says the other cases of Theorem 14 were "not re-verified here". The [01] headline and info-2 row do not.
- "What the evidence does not establish" has a bullet for the LKTS import but none for the CDF corollary.
- **Fix:** add "(other orders, including the prime and v = 21 cases ACF cite, not re-verified)" and a matching bullet.

**m7. Scope of the ledger review is unclear.**
- [01] "Ledger review" describes a Codex audit of "this ledger" but mentions only LKTS.
- If that audit predates the info-2 gate text, readers will assume the gate text was reviewed.
- **Fix:** give the reviewed snapshot's date and hash, and state that the CDF claims are covered by the CDF hostile reviews instead.

## Task results

### 1. Hand verification of [04] and [05]: PASS

**Method**
- For each block {0,a,b,c,d}, I computed the ten differences a, b, c, d, b−a, c−a, d−a, c−b, d−b, d−c and reduced each one to min(x, v−x).
- I bucketed the results by ranges of 50 and confirmed that each bucket contains each of its 50 values exactly once.
- To catch transcription slips, I confirmed that every block contributes exactly 10 entries across the buckets.
- A second pass redid every subtraction.

**801 = 3²·89:** 400 entries, and every class 1..400 occurs exactly once.
- Multiples of 89: 89 (B3: 328−239), 178 (B2: 620−442), 267 = v/3 (B1: 633−366), 356 (B5: 412−56).
- Class 400 comes from B31.

**901 = 17·53:** 450 entries, and every class 1..450 occurs exactly once.
- Multiples of 53: 53 (C1), 106 (C3), 159 and 371 (C11), 212 (C6), 265 (C10), 318 (C2), 424 (C4).
- All 26 multiples of 17 up to 442 occur once.
- Class 450 is 787−337 (C21).

**Structure checks**
- v is odd, so covering every class is equivalent to covering every ordered difference.
- Headers read `CDF 801 5` and `CDF 901 5`. Block counts are 40 = 800/20 and 45 = 900/20.
- Every block increases strictly from 0, so its entries are distinct. The largest entries are 794 < 801 and 891 < 901.

**Consistency**
- With LF line endings and a final newline, the displayed texts are 701 and 788 bytes. These match the worker reports bound in [08].
- All 45 rows of `data901` in [14] equal [05].

No failing block.

### 2. Lean semantics: faithful

**`Cdf.diffs`** ([12]) maps each (i,j,k) ∈ Fin n × Fin 5 × Fin 5 with j ≠ k to `B i j − B i k`.
- `Finset.univ` of any `Fintype` lists each triple exactly once, so this is the ordered-difference multiset with multiplicity.
- The filter decides j ≠ k through `DecidableEq (Fin 5)`, and `count` uses `instDecidableEqFin`. Coercions are `Fin.val`.
- `-` is core `Fin.sub`, which computes (v−b+a) % v. `blockOf_sub_val` and `Cdf.sub_eq_iff_modEq` confirm this.

**`IsCDF`** requires injective blocks, count 1 for every d with d.val ≠ 0, and count 0 at 0.
- This is the ACF/HBT definition. All six v are ≡ 1 (mod 5), so no short orbits arise.
- It is not weaker than the definition. `IsCDF.card_eq` forces 20n = v−1, and count 1 rules out repeated or translated base blocks.

**Binding of n, k and v.** The root types fix n, k = 5 (through `Fin 5`) and v.
- The roots are existentials with an explicit witness, so vacuity is not an issue. With n = 0, count 1 would fail.
- `cdf901_spec` shows that the `% v` in `blockOf` changes nothing.
- `isCDF_of_check` is independent of the data. Data shape is not load-bearing: a short row produces difference 0, which fails the mask check.

**`ParentStatement`** ([19]) inlines `diffs` and `IsCDF` verbatim.
- It guards against name-level substitution: the kernel must find the parent's literal text definitionally equal to the root type.
- That guard suffices. [20] shows `Target.lean` imports only `Mathlib.Data.Fintype.Prod`, so no worker instance or notation can change the meaning fixed there. For the same reason, it is harmless that the source scan does not look for `instance`, `notation` or `infix`.
- It does not provide a second, independent encoding. I accept the encoding on reading. A ZMod/`Finset` formulation proven equivalent would be an optional improvement.

**Facts.** Both definitions are correct.
- `IsStrictlyCyclicSteiner` describes an S(2,5,v) on Z_v:
  - every block has 5 points, and each pair of points lies in the block of exactly one index;
  - the indexing is injective, so each pair lies in exactly one block;
  - x ↦ x+1 is an automorphism, and all n block orbits have full length v.
- `IsPerfectOOC` requires:
  - weight 5;
  - |C_i ∩ (C_i′+τ)| ≤ 1 whenever (i,0) ≠ (i′,τ), which covers autocorrelation at τ ≠ 0 and cross-correlation at every τ;
  - Johnson-bound equality, 20n = v−1.

These modules were not parent-replayed, as the verdict discloses. The parent checker tests pair coverage and correlation directly on the certificates, so neither consequence depends on unreplayed code.

### 3. Gate and calibration

**Corollary.** It is correctly conditional in [00]. For [01], see m6.

**Gate.** It is justified for the frozen six-order set once this review is recorded and m1–m3 are applied. Each requirement is met:
- an independently checkable witness;
- independent parent verification: three checkers, replays and a kernel check;
- primary-source comparison;
- explicit priority limits;
- no restriction of the frozen quantifier.

**Timing.** The freeze at 22:08:23 precedes the worker-reported discovery at 22:59:50. It also precedes a parent-observed artifact, the 501 parent check at 23:00:54 ([26]). The ordering therefore does not rest on worker file times.

**Other checks**
- Attribution is correct: correlation is credited to the parent and worker checkers, not `checker.py`.
- All nine witnesses are bound in [08], and the parent checker's command-line rejection controls were exercised.
- NOVELTY-UNCLEAR and "modest specialist" are kept separate from correctness. I found no "first" claim and no method claim.
- In text outside the contract, prefer "closes the six possible exceptions" to "breakthrough".

### 4. Minimal defensible theorem and promotion

**Theorem.** For each (v,n) in {(321,16), (501,25), (621,31), (681,34), (801,40), (901,45)}, the n base blocks of the pinned file (SHA-256 as listed in [00]) form a cyclic (v,5,1) difference family in Z_v. Hence a perfect (v,5,1) OOC and a strictly cyclic S(2,5,v) exist.

**Kernel form.** `ParentCdfAudit.cdf{v} : ParentStatement v n`, using only the axioms `propext`, `Classical.choice` and `Quot.sound`, checked by one Lean kernel.

**Corollary.** This is conditional on ACF 2004 Theorem 14 and the cases it cites, which were not re-verified. A cyclic (v,5,1) difference family exists for every v ≡ 1 (mod 20) with 21 ≤ v ≤ 1001.

**Not claimed:**
- priority, or "first";
- a new method;
- an infinite family;
- v > 1001, or v ≡ 5 (mod 20).

**Promotion verdict**
- **Correctness:** ACCEPT for all six orders.
- **Gate:** met for the frozen info-2 target once this review is recorded.
- **Novelty:** NOVELTY-UNCLEAR.
- **Significance:** modest and specialist.

## What I could not verify

**Hashes**
- That the displayed texts hash to the pinned SHA-256 values. I checked byte counts only.
- That checkers `55dcbfc4…` and `8a8cea03…` are the files I audited previously; those hashes are absent here.

**Lean**
- The Data and Cert modules for 321–801, the Audit modules, and the Facts/Bridge builds.
- The mutated control sources behind [21].
- The full, untrimmed replay receipt.

**Records and producers**
- The integrity of `contract.json` and `transitions.json`.
- The worker timestamps and the creation time of the frozen source.
- The producer sources themselves.

**

**Literature**
- The HBT PDF hash, which is recorded in a receipt not included here.
- The 1996 Handbook (Remark 4.10.18), the 2007 Handbook §VI.16, and the paywalled sources listed in [26].

**Not load-bearing**
- The multiplier audits. I only confirmed that 622 (≡ 1 mod 9, ≡ −1 mod 89) and 52 (≡ 1 mod 17, ≡ −1 mod 53) are involutions, which fits the described pairing of blocks. I did not check the block-level counts.
