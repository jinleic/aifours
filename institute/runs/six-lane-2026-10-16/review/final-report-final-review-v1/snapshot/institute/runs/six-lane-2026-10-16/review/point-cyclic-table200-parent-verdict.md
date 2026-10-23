# Point-cyclic resolvable 2-(v,4,1) designs, v ≡ 4 (mod 12), 100 < v ≤ 200: parent verdict

## Result

Every order in the range now has a status. A **point-cyclic resolution** means a resolution of a 2-(v,4,1) design with an automorphism permuting the v points in one cycle (Topalova–Zhelezova 2026, Definition 5).

| v | Status | Basis | Evidence level |
|---|---|---|---|
| 112 | **exists** | explicit certificate (type T1; class orbits 1 + 28 + 4 + 4) | parent-verified finite certificate + Lean kernel |
| 124 | does not exist | Genma–Mishima–Jimbo 1997, Theorem 2.1 (31 prime, 31 ≢ 1 mod 12) | published theorem (author preprint read) |
| 136 | **exists** | explicit certificate (type T3, t = 17) | parent-verified finite certificate + Lean kernel |
| 148 | exists | Lam–Miao 1999 family (37 = 12·3 + 1, s odd), as quoted by Topalova–Zhelezova 2026 | cited; body not read; no certificate here |
| 160 | **exists** | explicit certificate (type T3, t = 5; class orbits 5 + 40 + 8) | parent-verified finite certificate + Lean kernel |
| 172 | does not exist | Genma–Mishima–Jimbo 1997, Theorem 2.1 (43 prime, 43 ≢ 1 mod 12) | published theorem |
| 184 | does not exist | this round's written 8p corollary (184 = 8·23, 23 ≡ 11 mod 12) | written proof, Claude and Codex ACCEPT; Lean only at v = 88 ([verdict](point-cyclic88-parent-verdict.md)) |
| 196 | **exists** | explicit certificate (type T2; class orbits 49 + 4 + 4 + 4 + 4) | parent-verified finite certificate + Lean kernel |

[Frozen target](../screening/info-2-point-cyclic-table200-contract.json) (DERIVED-OPEN). The source (Topalova–Zhelezova, Axioms 15 (2026) 762, p. 11) names only v = 88 as the smallest undetermined order; it states nothing about any order above 88. So this table **extends** that frontier rather than answering an explicitly named open target, and it is **not counted as an explicitly-named gate**.

## Certificates

| v | Certificate SHA-256 | Seed SHA-256 |
|---|---|---|
| 112 | `96265b66f4495e5927224599c941993d96bed85fb3d008b7dd53b925224a440d` | `9836c5030b61ad3c2bef183a4145a9029c605bdec7258e24c51e0236be22d4b1` |
| 136 | `61874100bd9333a6df83fbbecbbc807e139d985187ddcab6919ea4f815895c56` | `7f5057833fb25edabd3e6ad78d6dae81bed94a1a4a0aef4ef070ea484280da5b` |
| 160 | `8928dd9bd61c77da974d352f26f1980248445c5912428d943d4db3e22141a923` | `d81b4af2546c7130c6288c305c6cf948c87569aa2dfd953addfb4d0374f219f7` |
| 196 | `0828bf23d3bcd8a00a544cf7b8f1ae9e3a39279bc71a98fedd229eda5c6d8db5` | `2709520472d8941518674a584560e26c782fce663040de2cfd6f63338ba36d26` |

Pinned copies: [112](point-cyclic112-parent-inputs-v1/pin-receipt.json), [136](point-cyclic136-parent-inputs-v1/pin-receipt.json), [160](point-cyclic160-parent-inputs-v1/pin-receipt.json), [196](point-cyclic196-parent-inputs-v1/pin-receipt.json).

## Verification of the four existence results

| Check | Result | Evidence |
|---|---|---|
| Three independently written checkers (parent definition-first, prompt-only Claude-authored, lane) | All four certificates PASS: every pair once, every class a partition of Z_v, x ↦ x+1 maps the block set onto itself and every class onto a class | [112/136](point-cyclic112-136-parent-check-v1/parent-result.json), [160](point-cyclic160-parent-check-v1/parent-result.json), [196](point-cyclic196-parent-check-v1/parent-result.json) |
| Parent seed expansion (own code) | Each seed satisfies the residue and difference conditions and expands byte-identically to its certificate | same receipts |
| Intended-reason mutations | Point swap, duplicated block and global point transposition are rejected with the intended reasons at every order | same receipts |
| Parent-rebuilt native producers | `pc_tabu` (112/136/160) and `t2_twostage` (196) recompiled from pinned sources; every seed reproduced byte-identically, re-expanded and re-checked by parent code | [receipt](point-cyclic-table-producer-parent-replay-v1/parent-result.json) |
| Parent Lean replay | Literals bound to the raw certificates by the parent; generic modules byte-identical to the accepted v = 100 package; parent-authored unfolded statements for all four orders (design, resolution, single-cycle automorphism; `x ↦ x+1` named); fresh `leanchecker` 179 s; only `propext`, `Classical.choice`, `Quot.sound`; four statement mutations fail | [receipt](point-cyclic-table-kernel-parent-replay-v1/parent-result.json), [driver](point_cyclic_table_parent_kernel_replay.py) |

The existence results rest on the raw certificates alone. The lane's general orbit-type reduction (`GENERAL-REDUCTION.md`) only steered the searches; it is unreviewed and nothing here depends on it.

## Priority

[Bounded audit](point-cyclic-table200-priority-audit.md): no published theorem, table or explicit example decides 112, 136, 160 or 196; the published necessary conditions only narrow their possible types. Access holes: the Lam–Miao 1999 body, Fuji-Hara–Miao–Shinohara 2002, Lam–Miao 2001 (DCC), Mishima's 1999 thesis and the Handbook. The holes matter most at 196, which is forced to type T2, the type those works target. **NOVELTY-UNCLEAR.**

## Status

**FRONTIER:** the four constructed orders are **CORRECTNESS-ACCEPTED** finite existence results with parent fresh-kernel replay; the table as a whole is **DERIVED-OPEN** and **NOVELTY-UNCLEAR**. Calibrated significance: modest specialist table completion. Not an explicitly-named gate.
