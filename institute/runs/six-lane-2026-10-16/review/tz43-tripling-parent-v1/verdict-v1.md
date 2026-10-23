# Tz43TriplingAudit: verdict on the SAT-free frame step (auxiliary to §4(3), which is already closed)

Recorded 2026-10-18 at about 01:08 PT (host clock).

This is auxiliary verification of the already-accepted §4(3) FDGDD(3,4,5{18}) ([parent verdict](../tz43-parent-verdict.md)).
It is **not** a new problem slot and adds **no new gate**.

The binding receipt is `receipt-v2.json`, written last; it hashes this file. `receipt-v1.json` is retained, but its
hash of this verdict predates two later additions: the `tmp/` desk-size note and this paragraph.

## Answer

**Yes, as a purely constructive replacement of the frame-SAT step.**

1. **Proof.** `lemma-v2.md` proves a general result, importing only Hall's theorem: **every** GDD(3,4,30) of type
   6^5, i.e. every H(5,6,4,3), zero-sum-inflated by Z3 is an FDGDD(3,4,5{18}), and its Kirkman frames are explicit.
   * At (p, β), each missing-group family of the master derived 3-GDD of type 6^4 is 3-regular and 3-partite
     (Lemma 2).
   * König's theorem gives a proper 3-edge-colouring u of its incidence graph.
   * Each lift ((a,x),(b,y),(c,z)) with x+y+z = −β gets the label (x+u(a,e), y+u(b,e)). The nine label classes are
     the frame classes (Lemma 1).
2. **Finite instance.** On the pinned master, the stdlib generator wrote the certificate
   **`fdgdd_5_18_konig_tripled.txt`**, SHA-256 `5442b8c71612f9e021bdb990ea8931cf0919514bf4685f70d59dd80ce804ff12`.
   * Its 14,580 blocks are the same as the original's. Its first 14,588 lines are byte-identical to
     `3e22f502…a998`, with prefix SHA-256 `1887ddc9…c34b`.
   * It contains 3,240 frame classes built from the incidence colouring, written at all 90 points with no SAT and no
     symmetry transport.
   * Two independent existing checkers accept it, and both reject every intended mutation for its intended reason.
3. **Acceptance conditions.** The acceptance of this new finite certificate was conditional on two passes by
   independent checkers and on review. Both conditions are met.
   * Codex returned **ACCEPT** with no findings.
   * Claude returned **ACCEPT-WITH-FIXES** with 10 MINOR findings. All were applied in versioned files or explained;
     see `dispositions-v1.md`.

### What is replaced, and what is not

| Pipeline ingredient | Before | Now |
|---|---|---|
| Kirkman frames at the 90 points of the inflated design | SAT at the representatives (0,0) and (0,1), plus transport by the master group and copy negation | **The tripling lemma.** Per point, per family: a König colouring and Z3² labels. No search and no symmetry. |
| Master H(5,6,4,3) | Pinned 540-block master from a Kramer–Mesner SAT model, checked directly | **Unchanged.** Theorem 3 accepts any H(5,6,4,3), and existence is classical according to the scout's secondhand quotation of Zhang–Ge 2013. No SAT-free master was built or pinned here. |
| Block inflation by the zero-sum TD(3,4,3) | Explicit | Unchanged. Re-derived from the master; byte-identical blocks. |
| gcDCQS(18⁴:2), mcDSQS(74), the 18·4^t+2 family | Search- and import-based, as in the parent verdict | **Not affected**, not re-examined. |
| Accepted §4(3) FDGDD witness | `3e22f502…a998` | Unchanged; it remains the accepted witness. `5442b8c7…ff12` is an alternative explicit witness of the same object with constructive frames. Nothing was overwritten. |

## Evidence

**Construction**

| Item | SHA-256 | Result |
|---|---|---|
| Pinned master `inputs/master_H_5_6.json` | `891337721265767e7136aee41a8e0da5f2219decec4216a62e8f6b70ac90db2c` | Exclusive copy; source hash checked |
| Original certificate (read in place, read-only) | `3e22f5021631ac82ea5b5fa6f884984bb874f1f9a384fd35bfeff523e731a998` | Block set equal; first 14,588 lines byte-identical; first difference at line 14,591 |
| Generator v1 `code/build_tripled_fdgdd.py` | `6c0db3937a6722eaab2b690042e794724e8e3de66b84a03cfd59dd8f54a82d02` | Wrote all outputs after the internal checks |
| Generator v2 `code/build_tripled_fdgdd_v2.py` | `fa53d8026f95fe10273a8e96b9ad53339f082491572a9ccce5446434b418217b` | `--verify-existing`: all 6 outputs byte-equal; re-parse and prefix check enforced |
| Cross-interpreter replay (v1, Python 3.14.3 `-O -B`, hashes only) | `runs/replay-brew-OB-hashes-v1.json` `8b0129b9…09ae3` | Same output hashes and stats as the 3.9.6 write run |
| New certificate `fdgdd_5_18_konig_tripled.txt` | `5442b8c71612f9e021bdb990ea8931cf0919514bf4685f70d59dd80ce804ff12` | 700,931 B, 76,238 LF, 90 POINT, 3,240 FRAME |
| Incidence colourings `incidence-colourings.json` | `d70a8e6b43d8076cefd0f4b27db302ca5ab1064cc21ad38b1b206e50dcb4734f` | 120 families (p, j), each with 18 edges and u |
| Manifest v1 / v2 | `0bab3d48…0cc4` / `c1bdce46…3fbf` | Hashes, counts, mutation specs and analyses |

**Checker matrices**

| Item | SHA-256 | Result |
|---|---|---|
| Matrix v1 (`run_checker_matrix.py` `08c9ba07…4084`) | `checker-matrix-v1.json` `9ec69c1a…cd48` | 52/52 as expected |
| Matrix v2 (`run_checker_matrix_v2.py` `6fd919cc…1af6`) | `checker-matrix-v2.json` `0bed7f73…f8a` | 52/52 as expected; manifest, generator, master and original hashes bound; checkers unchanged afterwards |

Generator counts:
- master: 2,160 transverse triples, each covered once, and 72 derived triples per point;
- 120 missing-group families, each 3-regular (degree histogram `{"3": 2160}`);
- 90 points × 36 classes × 18 triples;
- 648 derived triples per point.

These internal checks support the construction. The certificate's validity rests only on the two external
checkers below.

### Each verifier separately

| Checker | Positive | mut_a: vertex swap, POINT 7 | mut_b: A-vertex shift, POINT 31 | mut_c: wrong s, POINT 56 | mut_d: duplicate class, POINT 89 | Argument controls |
|---|---|---|---|---|---|---|
| Parent definition checker `check_fdgdd_format_d.py` `0312f859…a9d4`, unchanged | PASS; class status `{"OK": 3240}` | FAIL = {F05, F06}; 9 classes OVERLAP | FAIL = {F05, F06}; 9 classes OVERLAP | FAIL = {F04} only; all 3,240 classes still OK as PCs | FAIL = {F04} only | `--m 6` → {C01_HEADER} |
| Claude-authored checker `checker.py` `2b2a7f19…dd10`, unchanged | valid | `frame.parallel` ("LF 19388: triple {38,60,75} … meets the triple at LF 19387 in point 38") | `frame.parallel` (point 81 = copy of master 27, a **C**-part vertex) | `derived.not_block` ("{18,38,56,78} is not a block") | `derived.repeat` ("LF 75575 … already listed at LF 75556") | wrong EXPECTED_SHA (the original's) → `sha256`; EXPECTED_V 89 → `order` |

- **Combinations.** Each cell was run 4 times: Python 3.9.6 and 3.14.3, each with `-B` and `-O -B`. All 4 agreed.
- **Hash binding.**
  - The parent checker's self-reported input hash equaled the fixture hash.
  - The Claude checker was bound to the fixture SHA via EXPECTED_SHA.
  - Every fixture was hashed before and after its runs, and all stderr was empty.
- **Mutation fixtures.** Each is a full certificate that differs from the positive only inside one POINT section:
  - `mut_a` `7fef9567…f522`;
  - `mut_b` `9cbb24a7…a86e`;
  - `mut_c` `0a786662…79ad`;
  - `mut_d` `84afd6b0…81d7`.

**Verbatim manifest fields** (`build-manifest.json`, disposing Claude finding 9):

```
mut_a_colour_vertex_swap:
  "edge": [12, 19, 26], "u_before": [0, 1, 2], "u_after": [1, 0, 2], "edge_sum_after_mod3": 0,
  "vertex_colours_after": {"12": [1, 1, 2], "19": [0, 0, 2]},
  every class: "class_defects_uncovered_multicovered_by_part" = {"A": [1, 1], "B": [1, 1], "C": [0, 0]}
mut_b_colour_shift_A_vertex:
  "a_star": 12, "edges_at_a_star": [[12, 18, 28], [12, 19, 29], [12, 23, 27]],
  "still_vertex_proper_everywhere": true, "edge_sums_mod3_at_a_star": [1, 1, 1],
  every class: "class_defects_uncovered_multicovered_by_part" = {"A": [0, 0], "B": [0, 0], "C": [3, 3]}
mut_c_wrong_third_sum_constant:
  "correct_s": 1, "used_s": 2, "all_classes_still_parallel_classes": true,
  "listed_triples_that_are_derived_at_point": 0, "listed_triples": 648
```

**What the mutations show about the lemma**

- **mut_b (third-part audit).** u stays a bijection at every vertex, and the zero sum is broken only on the three
  edges at a\*. Defects then appear only at C-copies, both missing and doubled, while A- and B-copies stay exactly
  covered. This is exactly what step (iii) predicts: it is the only place (U3) is used.
- **mut_a.** Breaking (U1) at two vertices while keeping (U3) moves the defects to the A- and B-copies instead.
- **mut_c.** With a wrong constant s′ = s+1, Lemma 1 still gives perfect matchings, but they are of the wrong
  triples. Only the parent's partition check F04 fails.

**Reused evidence (no SAT rerun).** The block list is byte-identical to the original's. The original's parent-desk
checks therefore apply unchanged:
- C10 exact transverse-triple universe;
- D02 derived GDDs;
- the solver-free re-expansion from the master and the zero-sum RDTD(3,4,3).

See `../tz43-fdgdd18-parent-v1/result.json` `3197db9c…f243f` and `../tz43-parent-verdict.md`. Both checkers above
re-verified coverage directly on the new file anyway.

## Reviews

| Reviewer | Note SHA-256 | Disposition |
|---|---|---|
| Codex gpt-6.1-sol, max, read-only; static (only nl, sed, rg, cat, grep, shasum) | `910d6afd…59d8` | ACCEPT; `Findings: none` |
| Claude claude-opus-5-5, max, no tools; LF-numbered packet | `2fb871c2…7a2` | ACCEPT-WITH-FIXES; 10 MINOR, all disposed in `dispositions-v1.md` |

Both reviewers re-derived the third-part existence and uniqueness and the g/2 degree counts.

The v2 note and v2 code were not re-reviewed. Their changes are clarifications and extra checks only. No
statement, construction or certificate byte changed.

## Correctness, novelty and significance, kept separate

- **Correctness.**
  - Lemma 1, Lemma 2 and Theorem 3 hold as written (lemma-v2), with Hall/König as the only import. Two static
    reviews support this.
  - The new finite certificate passes both independent definition checkers. Its intended-failure controls behave
    as designed.
- **Novelty.** **NOT CLAIMED.**
  - Lemma 1 is a short, routine consequence of König's edge-colouring theorem, and the tripling is likely folklore.
  - This desk ran **no** literature screen; the scout status is NOVELTY-UNCLEAR.
  - No new method is claimed, and no new infinite family is claimed.
- **Significance.**
  - The frame ingredient of §4(3) no longer depends on a computer search.
  - FDGDD(3,4,5{18}) was already certified, so no new orders or families follow from this desk.
  - The scout's broader leads remain outside this desk and need a separate screen before any statement: the
    fan-widened mcDSQS/RDSQS families, the T2 seeds, the odd-r conjecture and the even-r parity boundary.
- **Scope limits.**
  - Only group size 6 → 18, i.e. r = 3, on 5 groups.
  - No claim for g = 4, 8 or general g.
  - Existence of H(5,6,4,3) is quoted secondhand.
  - No Lean or formal proof, and no human review.
  - **Verifier vendor relation.** The two executing checkers are independent implementations. Both are Claude-side,
    however:
    - one is the parent-side desk checker, whose model family is not re-verified here (presumably Claude-family);
    - the other is a prompt-only claude-opus-5-5 checker.

    The only cross-vendor element for **this** certificate is the static Codex review. No Codex in-memory verifier
    was run on `5442b8c7…`; the task did not ask for one.

## Procedure

- **Disk gate.** The gate failed once, at 00:38 PT: free space was 12,060,577,792 B, below 12.2e9 plus growth.
  This was reported once to Main, and nothing was launched. A fresh check before the next launch, at 00:43 PT,
  showed 17,730,867,200 B, so work resumed. Every later launch was preceded by a fresh check.
- **Resources.**
  - One process was busy at a time, with child RSS ≤ 68.3 MB.
  - Every native child ran with TMPDIR set to `tmp/` and RLIMIT_CPU.
  - There were no timeouts or kills.
- **Desk size.** About 7.8 MB.
  - `tmp/` holds 2.7 MB in 561 files: Node compile-cache files and one empty temp directory left by the two reviewer
    CLIs, because their TMPDIR pointed at `tmp/`. They are retained, not deleted.
  - The rest is the certificate, the fixtures, the per-run checker reports for both matrices and small JSON/markdown
    files.
- **Writes outside the desk.** Only the 2 prompts and the reviewer outputs written by the review runners, under new
  names `../tz43-tripling-{codex,claude}-v1.*`.
- **Not done.** No Git operation, no publication, and no change to any existing evidence.
