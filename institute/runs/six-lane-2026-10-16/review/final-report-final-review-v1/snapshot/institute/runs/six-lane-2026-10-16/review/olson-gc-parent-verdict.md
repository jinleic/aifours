# Theorem NMH-iii (Lemma GEN, Lemma GC) — parent verdict (math-2) — 2026-10-18 00:53:19 PDT (host clock)

**Disposition: CORRECTNESS-ACCEPTED as a written proof (partial result toward ordered Olson for D₂ₚ; NOT a gate).** NMH(p), MIX_DEF_HIGH(p), RUNS(p), INV*(p) and ordered Olson are **not** concluded here.

- **Theorem NMH-iii — ACCEPTED, with the corrected scope sentence.** For every prime p ≥ 5, every normalized NMH word with R ≤ 2p−3 has an identity 2p-subword. The setting is that of `c3/proof-C-r1.md` Sec. 0 and `c6/proof-SEEDG-r2.md` Sec. 0. The word class consists of the item-(iii) words and the ZSI-B words **with R ≤ 2p−3**. The printed parenthetical "every ZSI-B word" (LF109–110) overreaches. Codex gave the counterexample p=5, k=6, d=(3,−1,1,1,1,1), which satisfies (4.1) but has R=8>7; the desk re-checked it by hand. The theorem is accepted only with the qualifier.
- **Lemma GEN** (the exact iff for genericity of a proper pattern) and **Lemma GC** (for every run t there is an actual generic configuration Q with t∉Q and with Q and Q+t proper and generic, for k≥7 and Δ0≥3) are ACCEPTED as written.
- **Correctness:** VERIFIED as a written proof that imports only parent-accepted or reviewed results, each inside its own hypotheses. **Novelty:** UNCLEAR. **Significance:** a uniform step inside this run's own positive-excess decomposition. It is not a published open target.

## Claim and imports

| File | sha256 | Status |
|---|---|---|
| `mathematics/evidence/six-lane-20261016/olson/inverse-run-count/mixdef-high/c6/proof-GC.md` | `f968a396facf396854662cbcb566c614e7e1e1dac415ca23ae70309878998425` | accepted text, with the errata below |
| `c6/proof-SEEDG-r2.md` (TS, QS, actual-empty alternative, NW, GS (a)/(b)) | `353b0e95…30b7` | parent-accepted ([cycle-6 verdict](olson-c6-uniform-parent-verdict.md)) |
| `c6/proof-A0-r1.md` (Corollary (a)/(b), C0-all) | `fba51b12…81a0` | parent-accepted |
| `c6/proof-C0WB-r2.md` (DF, C0W) | `7900f468…36f1` | parent-accepted; used only inside B≥g+1, 3g+1≤p |
| `c3/proof-C-r1.md` Sec. 0, Kill lemma, Sec. 2 identities | `b5eb9fa7…b65b` | Codex ACCEPT |
| `c6/c5-fixes/proof-Cplus-r2.md` ((B1+), (B2+), C4) | `00e850cf…8bd3` | r1 reviewed; C4 delta parent-verified |
| `inverse-parity/proof-PAR-K0.md` (Lemma H with β=0, with its 07:39 correction; BC Claim) | `4b107fff…9a38` | Codex ACCEPT |

## Evidence

1. **Parent derivation** ([spot note](olson-gc-parent-math-spot-v1.md), `ade134829f5f994afd48c1cdd9e0cc6d7b51b3d694fb0fec19b69ba7d24293fd`). Written before the reviews, it independently derives the diamond criterion behind GEN and checks the walk/window/crossing core. It was withheld from both reviewers and agrees with them.
2. **Hostile reviews** (static; identities from receipts):

| Review | Disposition | FATAL | MAJOR | MINOR |
|---|---|---|---|---|
| Codex `gpt-6.1-sol` ([note](olson-gc-review-codex-v1.note.md), `e8360d1c…e305`) | ACCEPT-WITH-FIXES | 0 | 0 | 2 |
| Claude `claude-opus-5-5` ([note](olson-gc-review-claude-v1.note.md), `e4e5e70b…04e8cc`) | ACCEPT-WITH-FIXES | 0 | 0 | 8 |

   Both reviewers and the desk independently re-derived three points. GEN is an exact iff and is parity-tight, since D ≡ Δ0 ≡ k (mod 2). GC holds for every k ≥ 7, with the walk taking exactly k−3 moves. The window cannot be skipped because D±W′ is even.
3. **Desk smoke** ([summary](olson-gc-review-summary-v1.md) `fa0fbfda…8c3c`, [result](olson-gc-review-result-v1.json) `811aec4a…c460`). It is a stdlib script written from the definitions and imports no producer code. It found 0 mismatches over 1,249,684 GEN patterns and 0 failures over 14,630 literal walks for p = 5..23. Every designed mutation was detected, except a +1 bound shift, which parity makes undetectable. The theorem's conclusion was checked directly in D₁₀ by exhaustion (437,500 words up to rotation and conjugation, p=5 only). These finite results are aids, not premises.

## Errata carried by this verdict (frozen files are not rewritten)

1. LF109–110 and LF118: read "every ZSI-B word **with R ≤ 2p−3**".
2. LF118: the path is `proof-MH.md` relative to `mixdef-high/`, not `../proof-MH.md`.
3. LF16–17: the parent-verdict path is relative to the repository root, and the verdict was read by the worker (c6 README LF652–655).
4. LF105: the walk has exactly k−3 unit moves; the lowering pass is empty.
5. LF103–104: Remark (1) also uses Lemma H with β=0, (1.1), |d_s| ≤ e_s+1, e_s ≥ 0 and E = Σe_s.
6. LF113–115: the "empty seed intersection" is the accepted actual-empty alternative. The canonical bound [λ({t}),U({t})] and the GS (a) bound are inconsistent; an empty interval is not a seed, and this is not an empty (QS) window.
7. LF119–123: "supersedes" holds only as a conclusion and only because of this acceptance. Any NMH(p) or MIX_DEF_HIGH(p) assembly additionally requires acceptance of `c2/proof-C2.md` (R ≥ 2p−2) **and** of the README Sec. 1 reductions (OR, M0, ALT, B0/C0-B′/A1 and the trivial cut). That assembly is with the OlsonRunsAssembly desk and is not decided here.

## Limits

No Lean, no human referee and no novelty search. A Δ0 = 2 probe outside scope showed that the written (M) step fails exactly when k ≡ 0 (mod 4), yet the conclusion held on every sampled target. That probe is information only; R = 2p−2 belongs to `c2/proof-C2.md`, which this verdict does not judge.
