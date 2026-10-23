# E11 frozen plan — explicit mcDSQS(128) by Tan–Zhou Construction 2.1 (s = 0)

Written 2026-10-17 after 15:39:09 PDT (host clock), before any E11 computation, by worker
`MathMcDsqs128` (consequence/reproducibility slice of the existing math-1 gcDCQS(32⁴ : 0) slot; not a
new target). Earlier lane files are read-only; every E11 output is a new, exclusively created file or
directory. No novelty or priority claim; no claim that any gate is met.

## Target (definitions from the pinned text, sha256 `df52a8f1…4c3c8164`)

mcDSQS(128) (lines 127–130): an SQS(128) whose derived design at every point is minimum colourable,
i.e. admits a χ′(127)-colouring; χ′(127) = (127 + 1)/2 = 64 by (1.1) (lines 110–125; 127 ≡ 1 mod 6,
127 ∉ {7, 13}). Independently of (1.1), 64 is a lower bound for every STS(127): a partial parallel class
of 127 points has at most 42 triples and 63 · 42 = 2646 < 2667 = 127 · 126 / 6.

## Inputs (pinned, read-only)

* I_A: gcDCQS(32⁴ : 0) `evidence/gcdcqs32-c23/gcdcqs32_c23.txt`, sha256
  `e38945b1204e78937527f17db3d87f147e47885dc160c04b6a4de49377da0f46` (parent-verified certificate).
* I_B: Appendix B (Lemma 3.4) cyclic mcDSQS(32) transcription `sources/tz_appb_mcdsqs32.json`, sha256
  `5ab58710b0c4d312844ad987c9245dcbee94b999db2de8e79a267cdcfd15d8aa` (E0, 10-17 08:20:07; extractor/checker
  `code/tz_appb_mcdsqs32.py` sha256 `a4a91e54…df06`; text lines 1326–1332 and 1341–1372; E0 controls
  `controls/e0_appb_controls/` 4/4 rejected).

## E11a — input pinning and independent re-transcription (before the build)

1. Re-run the unchanged E0 check on I_B; retain its output (`runs/e11/`), since E0 kept no output file.
2. Route G: Ghostscript `txtwrite` text of the Appendix B pages of the pinned PDF (sha256
   `1a7e0dc3…e291`), a different extraction engine from the pdftotext file used by E0; parsed by new code
   (`code/e11_appb_retranscribe.py`, no code shared with `tz_appb_mcdsqs32.py`).
3. Route L: the arXiv v1 LaTeX source (public e-print, fetched into the lane, sha256 recorded), parsed by
   the same new script; skipped and recorded if the e-print is not LaTeX.
4. Route V: page images rendered by `pdftoppm` (retained): visual check of the part layout and of the
   short-orbit underlines against the computed orbit lengths (lane observation only).
5. Acceptance: base blocks (ordered list of 4-sets) and parts (ordered list of sets of triples) of I_B
   equal those of route G, and of route L if available. Any mismatch → record, stop, report; no build.

## E11b — construction (`code/build_mcdsqs128.py`, new, stdlib only, modelled on the gcdcqs20 lane's
`code/build_mcdsqs80.py` sha256 `606321e8…352e`)

1. S32 = {B + i mod 32 : B ∈ base blocks, i ∈ Z32}; assert 1240 blocks, every 3-subset of Z32 in exactly one.
2. Q_a^k = part_k + a (mod 32), k = 0…15; at **every** a ∈ Z32 assert: each Q_a^k is a partial parallel
   class and the 16 classes partition the derived STS(31) of S32 at a (checked directly at each a).
3. Read I_A (`code/seed_tools.read_cert`); assert `GCDCQS 128 4 32`, `COLOURS 64`, `HOLEFREE 16`,
   groups G_i = {32i, …, 32i + 31}.
4. Blocks F = A ∪ {32i + B : B ∈ S32, i = 0…3}; assert |F| = 80384 + 4 · 1240 = 85344.
5. At x = 32i + a: the classes of the I_A colouring at x containing no point of G_i ∖ {x} (exactly 16,
   asserted), in index order; the k-th gets {32i + t : t ∈ Q_a^k} appended; the other 48 classes are kept;
   class indices unchanged (Construction 2.1, lines 321–326, with s = 0: the gcDSQS(g + s, s) on the
   other groups is again an mcDSQS(32)).
6. Output (exclusive create) `runs/e11/build/mcdsqs128_c21.txt`: two `#` lines with the input sha256s,
   `MCDSQS 128`, `COLOURS 64`, `BLOCKS` (sorted 4-tuples), then `POINT x` / `CLASS j` with sorted
   triples; sha256 printed.

## E11c — two definition-first checker routes (no symmetry assumed by either)

* `code/mcdsqs/check_mcdsqs.py` — byte-identical copy (`cp -n`) of the gcdcqs20 lane's
  `code/mcdsqs/check_mcdsqs.py` (sha256 `e2dc212d…63a3`), run by `/usr/bin/python3` 3.9.6.
* `code/mcdsqs/check_mcdsqs.c` — byte-identical copy (sha256 `7d04c404…bc72bd`; MAXV = 128),
  compiled `clang -O2` into `code/bin/check_mcdsqs_c`.
Both check every 3-subset of the 128 points once and, at all 128 points, 64 nonempty partial parallel
classes exactly partitioning the derived STS(127).
**Pin rule:** the first build passing both → `cp -n` into `evidence/mcdsqs128-c21/`, sha256 reported to
the parent at once.

## E11d — controls (all mutated files retained)

* Generic: copied `code/mcdsqs/mutation_controls_mcdsqs.py` (sha256 `49ab9782…106a`), 15 mutations,
  both checkers, intended-reason regexes.
* Construction-specific (new `code/mcdsqs/e11_construction_mutations.py`, same intended-reason rule):
  (m1) a merged local part split off as a 65th class; (m2) a local part moved into a non-avoiding class;
  (m3) one local triple replaced by the corresponding triple of another translate; (m4) one local
  SQS(32) block dropped.
* Builder input controls (the builder must abort before writing): base-block digit changed, base block
  dropped, part-triple digit changed, triple moved between parts, and the retained gcDCQS mutant
  `evidence/gcdcqs32-c23/mutations/kempe_swap_no_hole_avoiding_class.txt` (15 hole-avoiding classes).

## E11e — producer replay

Rebuild from the pinned inputs into a fresh directory; `cmp` must report byte identity.

## E11f — consequence note and receipt

Short written note (Corollary 2.6 arithmetic for m = 32; imports named, not re-proved; not a formal
proof) and `receipt.json` (hashes of inputs, code, binary, outputs; commands; checker results; controls;
CPU / max-RSS / disk observations).

## Resources and stops

≤ 4 busy processes (expected ≤ 3), ≤ 8 GiB RSS (expected < 1 GiB), ≤ 10 GiB new data (expected
≈ 0.15 GB), host free disk ≥ 12,000,000,000 bytes checked before write-heavy steps; `/usr/bin/time -l`
on every compute step. Native limits or SIGTERM + bounded wait only; no SIGKILL, no
`subprocess.run(timeout=…)`; any stop recorded. Host-clock labels only.
