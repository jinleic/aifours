# Erratum 1 to `reductions/proof/reductions-v4.md` (wording only)

Worker `MathPhaseType3`, the lane's integration owner, 2026-10-18 PDT. The reductions author, subagent
`ME3Reductions`, has finished. This is a static erratum, created as a new file. It changes no file and involves no
computation.

**Frozen and unchanged (sha256):**
* `reductions/proof/reductions-v4.md`: be1f7190ba71f06b3e951886581d285cc74435a49e3c2983776cebb6101f6eb1
* `reductions/STATUS-v4.md`: 1ffe3de816c3060e0e3a155e7dbee190075e9692b7a3562c923842c43af70e50
* `reductions/proof/reductions-v4.diff-from-v3.txt`: 5a6a37f44c28d8a9ee68d4fc28a1649b7ec1d70792cd6b843d0835354794b08b.
  This file is the historical record of the v3→v4 change, so its LF275–277 still show the old wording.
* the integration proof v5 and its errata 1–2, every certificate and run, and pin v3
  (`receipts/me3-candidate-pin-v3.json`, fa9327f2b35c31544128e612c55024caf97540d9fe05bdaf184861d8604d8b4b).
* There is no re-pin, on the parent's instruction.

**Source.** `institute/runs/six-lane-2026-10-16/review/me3-reductions-v4-delta-codex-v1.note.md`, sha256
60d659ed586c2d1dc745d9a5e6141045fb700ac63c5476f126955d8a1ab38825.
* Verdict: ACCEPT-WITH-FIXES with 0 FATAL, 0 MAJOR and 1 MINOR.
* Location of the MINOR:
  * SOURCE00 LF777–779, which is reductions-v4 LF777–779;
  * SOURCE01 LF523–525, which is the same text in the parent's v1→v4 diff (not a lane file).
* The finding: the premise "If the theorem holds" gives only equality of the infima; that I_2 = v_cos is unattained
  needs, in addition, strictness on every D2 cone.

Erratum 2 of this family is reserved for any MINOR findings that the pending Claude reductions delta review may report.

## E1. Remark 7.2a, first bullet — reductions-v4 LF777–779

**Old (verbatim, LF777–779):**

```
* Cor 7.1(2) gives only I_2 ≤ v_cos. If the theorem holds, I_2 = v_cos is an unattained infimum over the union of the
  D2 cones, so strictness for D2 laws cannot be read off any statement about I_2. Cor 7.2 supplies it cone by cone,
  using attainment inside each fixed cone (Lemma 2.4(1)).
```

**New (replaces LF777–779):**

```
* Cor 7.1(2) gives only I_2 ≤ v_cos. Cor 7.2 supplies strictness cone by cone, using attainment inside each fixed cone
  (Lemma 2.4(1)). Once Lemmas D/M and Corollary 7.2 establish strictness on every D2 cone, Corollary 7.1(2) implies
  that I_2 = v_cos is an unattained infimum.
```

**Exact change.** Three edits; nothing else in the bullet changes.
1. Deleted: "If the theorem holds, I_2 = v_cos is an unattained infimum over the union of the D2 cones, so strictness
   for D2 laws cannot be read off any statement about I_2."
2. "Cor 7.2 supplies it" becomes "Cor 7.2 supplies strictness", because the antecedent of "it" was in the deleted
   sentence.
3. Appended, verbatim from the review's concrete repair and the parent's instruction: "Once Lemmas D/M and Corollary
   7.2 establish strictness on every D2 cone, Corollary 7.1(2) implies that I_2 = v_cos is an unattained infimum."

The other bullets of Remark 7.2a (LF780–785) are unchanged.

**Why the new sentence holds** (no new mathematics; reductions-v4 Cor 7.1 and Cor 7.2).
1. Strictness on every D2 cone means SCV(f) > v_cos for every f in every D2 cone K∖{0}. Hence
   I_2 = inf{S_2(r, ω, φ) : r > 0, ω > 0, 0 ≤ φ ≤ θ1(r)} ≥ v_cos. Here every S_2 value is the SCV of an element of a
   D2 cone (LF747–749).
2. Corollary 7.1(2) gives I_2 ≤ v_cos. So I_2 = v_cos.
3. Every D2 law has SCV > v_cos = I_2, so no D2 law attains the infimum.

**Gap per cone, but no uniform gap.** This distinction, noted by the review, is preserved.
* Within each fixed D2 cone K, min_{K∖0} SCV exists (Lemma 2.4(1)) and exceeds v_cos (Cor 7.2), so each cone has a
  positive gap.
* There is no uniform positive gap across all D2 cones, because their infimum is v_cos (Cor 7.1(2)).

## Propagation pointers (information only; no change)

The review notes that the propagation of its earlier findings 3 and 5 outside reductions-v4 "cannot be verified from
this snapshot". In the integration proof:
* **Finding 3**, D1 via Lemma 2.4 + Lemma 5.1 rather than "by definition": `proof/me3-theorem-v5.md` LF102–103 and
  LF243–244, and erratum 2 m8.
* **Finding 5**, the lower bound labelled conditional and unused: v5 LF104–108.
* **Labels:** `reductions/STATUS-v4.md` LF14–16 and LF35–36.
