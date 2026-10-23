# Tz43TriplingAudit — dispositions of the two static CLI reviews

Recorded 2026-10-18 at about 01:05 PT (host clock). Both reviews were static.

* **Codex.** The stderr log shows only `nl`, `sed`, `rg`, `cat`, `grep` and `shasum` commands, with no Python
  executed.
* **Claude.** It had no tools.
* **What was reviewed.** v1 of the lemma note, the generator and the runner, at these SHA-256 values:
  * `lemma-v1.md`: `ff2569b3…337d`
  * `code/build_tripled_fdgdd.py`: `6c0db393…2d02`
  * `code/run_checker_matrix.py`: `08c9ba07…4084`
* **v1 files.** All v1 files are preserved unchanged. Every fix below lives in new, versioned files.

## Review receipts

| Reviewer | Name | Prompt SHA-256 | Note SHA-256 | Duration | Disposition |
|---|---|---|---|---|---|
| Codex gpt-6.1-sol, max, read-only | `tz43-tripling-codex-v1` | `168835b2…533e` | `910d6afd0fc45972b793ecc07a2e84552f7c56b6f15b6e6171cc21567ee159d8` | 193.5 s | **ACCEPT**, `Findings: none` |
| Claude claude-opus-5-5, max, no tools | `tz43-tripling-claude-v1` | `4dee3198…94d7` | `2fb871c2d04ab9c0a0c3e3b46254f6388f1bb08d93a3d4446f7ca93f805117a2` | 867.0 s | **ACCEPT-WITH-FIXES**: 10 MINOR, 0 MAJOR, 0 FATAL |

Neither review timed out, so no retry was needed.

Both reviewers independently re-derived the third-part step (iii).
- **Existence** follows because (U1) at c is onto, and **uniqueness** because it is injective.
- (U3) is used only through the condition u(c,e) = s − z − p1 − p2.

Both also re-derived the degree counts n_b = n_c = n_d = g/2 from D1(2) and D1(3). Their notes give the detail
under "Third-part audit" and "Degree-count audit".

## Claude findings: all accepted, none affecting the certificate

| # | Finding (abridged) | Disposition | Evidence |
|---|---|---|---|
| 1 | E^s is written as a set, but the proof uses an indexed family. With parallel edges, λ would be ill-defined. | **Applied.** lemma-v2 §0 defines E^s = (L(e;x,y,s−x−y))_{(e,x,y) ∈ E×Z3²}. A subfamily is a subset of the index set. For simple H the set reading is equivalent. Theorem 3 is unaffected, because D_p has no repeated triples. | `lemma-v2.md` |
| 2 | Step (iii) silently assumes that no lift of an edge with c_e ≠ c contains (c, z). | **Applied.** A containment bullet is added to (iii). "No other edge" is now explicit, citing existence and uniqueness. | `lemma-v2.md` (iii) |
| 3 | \|D\| = 72 and \|A0\| = 540 are asserted, not derived. | **Applied.** \|D\| = 24·9/3 is derived in the g = 6 case of Lemma 2. \|A0\| = 2160/4 is derived in Theorem 3(a). | `lemma-v2.md` |
| 4 | The generator docstring cites a nonexistent "Theorem 2". | **Applied** in the v2 generator: "Lemmas 1–2 and Theorem 3". Behaviour is unchanged. | `code/build_tripled_fdgdd_v2.py` `fa53d802…217b` |
| 5 | The mut_b wording says "uniqueness". Existence also fails at C-copies. | **Applied** in the v2 generator's mutation text, carried into `build-manifest-v2.json`, and in lemma-v2 §5(b). The fixture bytes are unchanged. | manifest v2 `c1bdce46…3fbf` |
| 6 | The mut_c analysis checks only 54 distinct points, not equality with (X\G_x)\G_j. | **Applied** in the v2 generator. Manifest v2 records `all_classes_still_parallel_classes: true` under the stronger test. Independently, the parent checker's class-status histogram is `{"OK": 3240}` for mut_c in all runs. | manifest v2; `checker-matrix-v2.json` |
| 7 | The rendered bytes are never re-parsed, and the prefix identity is only reported. | **Applied** in the v2 generator. It raises on any header/GROUPS/BLOCKS prefix mismatch, and re-parses all POINT/FRAME/triple records against the in-memory classes. The run with `--verify-existing` passed and confirmed byte equality for all six files written by v1. The certificate's validity never rested on these internal checks: both external checkers check the written bytes. | `runs/build-v2-verify.stdout.txt`; manifest v2 `mode` |
| 8 | Manifest TOCTOU: the manifest is hashed, then re-opened. The checkers are hashed only before the matrix. | **Applied** in the v2 runner. Manifest bytes are read once and hashed and parsed from the same bytes. Both checkers are re-hashed after the matrix; `checkers_unchanged_after_matrix: true`. | `code/run_checker_matrix_v2.py` `6fd919cc…1af6`; matrix v2 `0bed7f73…f8a` |
| 9 | The manifest's generator, master and original hashes are not bound. The prompt also shows a mutation-analysis key the generator does not emit. | **Binding applied** in the v2 runner. The generator SHA `fa53d802…` is bound on the CLI; the master `89133772…db2c` and original `3e22f502…a998` are bound as full constants. **Key:** this is a reformatting by the prompt builder, not another generator revision. `code/make_review_prompts.py` (`cc0bf2e9…ed9`) lines 43–45 rename `class_defects_uncovered_multicovered_by_part` and flatten its `{A,B,C}` dicts into lists. The v1 manifest records generator `6c0db393…`, the reviewed file. The verdict quotes the manifest fields verbatim. | `build-manifest.json`; `verdict-v1.md` |
| 10 | A stale per-run report could be scored, and an existing output JSON is caught only at the end. | **Applied** in the v2 runner. Before any run it refuses an existing report path or output JSON, and it uses a fresh `runs-v2/` created with `os.mkdir`. v1 was already fail-closed for the stale-report case. The parent checker opens `--out` in mode `'x'`, so a pre-existing report raises `FileExistsError` and writes to stderr. v1 requires empty stderr, so such a run could be scored only NOT-OK, never OK. | `code/run_checker_matrix_v2.py` |

The v2 runner reproduced the v1 outcomes exactly: 52 of 52 executions came out as expected, with every fixture hash
checked before and after and both checkers unchanged.

The v2 lemma note and v2 code were **not** re-reviewed. Every change above is a clarification, an added internal check
or added binding. No mathematical statement, construction or written certificate/fixture byte changed.
