# moqls8 encoder binding v1 (parent verification, phys-1 lane, Ball–Simoens Problem 16, n = 8)

Created 2026-10-17T15:18:43-07:00 (host clock). Worker id Moqls8EncoderBinding.
Scope: bind the ACTUAL K5 base CNF (lane evidence/gram_dev_v1/GA5L_K5_sb2.cnf, SHA 6ecb77a7…469b, gram_a.py bf1aada1…d05a)
and the K4 weight-1 CNF (lane evidence/k4_w1_v1/GA3_K4w1.cnf, SHA 7bb806fc…01f7, gram_a_r3.py 40622a6f…dbb) to the
clause families of review/K4K5_ENCODING_SOUNDNESS.r2.md, against obligations C1–C12 of
review/moqls8-k4k5-claude-review-v1.note.md and the findings of review/moqls8-k4k5-codex-review-v1.note.md.
K4 and K5 are NOT excluded by anything here; no exclusion is claimed.

Rules: writes only in this directory (exist_ok=False, files mode x); lane and snapshot read-only; encoders copied
byte-identically from the snapshot (code/); CNFs regenerated in memory and stream-hashed, never stored; no lane
runners, no solver on a full base CNF, no proof checker; <= 1 busy CPU, <= 6 GiB RSS (sampled; SIGTERM + bounded
wait on trip, never SIGKILL); free-disk floor 12e9 bytes; no network, model CLIs, deletion, /tmp or git mutation.

Plan: (1) regenerate both bases with the pinned encoders' own main()/argparse/build path (writer replaced by a
streaming hash of the identical serialisation) and compare with the recorded and stored SHA-256; (2) classify every
clause of the regenerated stream through the encoder's name table (g entries cross-checked with the lane map JSON)
into the note's families with semantic validation, plus an independent expected-family generator compared as
multisets; (3) C12 positive control with an AG(2,8) set of 5 MOLS(8) built and verified here, and an exhaustive P4
gadget test; (4) receipt binding-result.json.

Checkpoints: CHECKPOINT-*.md files (README is not rewritten; mode x).
