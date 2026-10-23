DISPOSITION: ACCEPT-WITH-FIXES

**FATAL:** None found in the reviewed delta. All supplied hashes match. The actual clause builders remain unchanged, but the following gaps should be fixed before proof mode.

**MAJOR M1 — The “exact” CNF schema specifies the wrong pair order.** [review/V4_PROOF_SCHEMA.r1.md:11](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/ame46-support/review/V4_PROOF_SCHEMA.r1.md:11) specifies `01,02,03,12,13,23`; the base and linking code use `01,23,02,13,03,12`, inherited from [code/ame_e0_cnf.py:22](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/ame46-support/code/ame_e0_cnf.py:22). This changes hole-variable allocation and clause order. An in-memory mixed-profile comparison produced different DIMACS hashes, with the first difference at DIMACS line 116. The officer builder separately uses the sorted order. Publish a corrected schema distinguishing these orders before independent regeneration.

**MAJOR M2 — A late guard trip can still publish EXCLUDED.** [code/large_t_joint5.py:284](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/ame46-support/code/large_t_joint5.py:284) snapshots UNKNOWN while the watchdog remains active until line 302. A trip between that snapshot and report construction can produce `outcome="EXCLUDED"`, `excluded=true`, and a non-null `guard_tripped`. I reproduced that interleaving using the extracted aggregation statements. Finalization must synchronize with the watchdog and evaluate its settled state.

**MINOR m1 — W’s shape assertion omits the common value pair.** [code/large_t_joint5.py:111](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/ame46-support/code/large_t_joint5.py:111) checks a common differing coordinate, but never checks that all three doubled pairs use the same `{a,a′}`. Replacing one clause in a correctly sized 2,592-clause family with the negative literals for  
`3333,4333,3344,5344,4443,5443` passes every assertion. Its doubled pairs are `{3,4}`, `{3,5}`, `{4,5}`, so it is outside Lemma 20. The pinned generator itself is correct. Assert six literals and one common value pair explicitly.

**MINOR m2 — Recorded blocker cardinality is trusted rather than checked.** [code/large_t_joint5.py:210](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/ame46-support/code/large_t_joint5.py:210) immediately blocks the extracted positive point variables without checking `|Y|=2h+e`. B3 guarantees this for a valid SAT model; the recorder does not validate that assumption. An incomplete model can yield a smaller, component-rejected Y whose short blocker excludes unchecked supersets. Assert the recorded cardinality before adding the block, and independently check it during binding.

**MINOR m3 — Some failures abort instead of recording UNKNOWN.** The handler at [code/large_t_joint5.py:179](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/ame46-support/code/large_t_joint5.py:179) catches binding `AssertionError`s correctly. However, a four-literal W clause raises an uncaught `IndexError`; checker startup and proof-file errors at [code/large_t_joint5.py:201](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/ame46-support/code/large_t_joint5.py:201) likewise escape. These paths do not falsely exclude, but fail the promised UNKNOWN/reporting contract.

**MINOR m4 — One proof-checker assertion remains optimization-dependent.** [code/lratcheck_py.py:52](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/ame46-support/code/lratcheck_py.py:52) uses `assert` for the hint terminator. Inherited `PYTHONOPTIMIZE` can remove it. Replace it with an explicit error. Parent `python -O` alone does not propagate that flag to the checker subprocess.

The v4 disposition audit follows. Line numbers in this table refer to `code/large_t_joint5.py` unless another file is named.

| V4 finding | V5 assessment |
|---|---|
| Codex M1 | Fixed: proof requires joint, lines 145–146; completion fallback and completion rejection are excluded from proof mode, lines 249 and 274–276. |
| Codex m1 | Fixed: returned phase flags and closed-2×2 scope preserved, lines 243–247. |
| Codex m2 | Normal paths fixed: completion errors, checker false results, and UNKNOWN-over-candidate precedence work. Late-guard and exception gaps remain above. |
| Claude MAJOR-1 | B3 EQK fixes cardinality for every e; T-independent rejection and final all-rejected aggregation are present. Add the recorded-Y check above. |
| Claude MAJOR-2(a) | Pinned V/d conventions agree; explicit comparison at lines 61–64. |
| Claude MAJOR-2(b) | Two-sided hl clauses verified at lines 51–56; actual builder supplies both directions. |
| Claude MAJOR-2(c) | Actual offsets, shared allocation counter, variable ranges, linking and fresh lex allocation are correct. Checks at lines 57–92 and 177–178. |
| Claude MAJOR-2(d) | W rejects nonzero e in `build`; e and flags are recorded, lines 99–100 and 135–136. |
| Claude MINOR-1 | B/C/K naming clarified in ENGINE_V5 §2. |
| Claude MINOR-2 | Complete witness, including officer auxiliaries and two-sided hl, supplied in §5. |
| Claude MINOR-3 | Orientation, formula and count/duplicate checks implemented. Shape validation remains incomplete as above. |
| Claude MINOR-4 | K4/K5 discriminating controls are implemented and their expected outcomes recorded. |
| Claude MINOR-5 | Reconstruction is gated to e=0; failed reconstruction remains an unresolved candidate, never a rejection. |
| Claude MINOR-6 | Profile sums and C3 ranges explicitly guarded, lines 46–47 and 66–68. |

All new binding checks use explicit raises: there are **zero `assert` statements in v5**. Compilation at optimization levels 0/1/2 preserved them; an injected binding failure under level 2 produced UNKNOWN. Neither checker returning false can yield EXCLUDED through the normal path.

Proof handling records the exact final CNF hash, compressed proof SHA, and both checker results. Per-Y records retain N and component rejection information, verified rational Stiemke vectors, or explicit verified phase certificates. These rejection systems depend on N, independently of T.

Independent pure enumeration matched all normal profiles for the requested cases:

| `(t,e)` | Profiles | Lemma17 skips | Remaining profiles |
|---|---:|---:|---:|
| (30,6) | 2 | 1 | 1 |
| (28,4) | 7 | 2 | 5 |
| (27,3) | 6 | 3 | 3 |
| (26,2) | 25 | 1 | 24 |
| (24,0) | 158 | 5 | 153 |

After the fixes, use complete profile coverage, `--joint` throughout, and W only at `(24,0)`. Any lower-bound claim still needs independent final-CNF binding, proof replay, and rejection verification for every blocked Y. Controls supply no proof.

No files were written; no solvers, engine main, network, or delegation were used.