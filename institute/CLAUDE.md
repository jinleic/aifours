# aifours — agent rules

This repository is the research institute: a sequential explorer of the open problems in
《10000个科学难题》 (mathematics, physics, information science). Read `README.md` first.
`AGENTS.md` is a symlink to this file.

## Spending model time

- `python3 ri.py run` spends Claude and Codex subscription quota. Run it only when the owner asks,
  with `--problems` and/or `--hours` (and any `--quota-scale`) stated in your reply.
- A generic request such as "start the research" or "run the institute" authorizes only
  `python3 ri.py status` and a question about the bound.
- Never install a launchd/cron driver unasked. Batches run from a real terminal or tmux
  (`caffeinate -i python3 ri.py run ...`), never from an agent's background shell.
- Before unattended batches, the owner runs `codex login` once (the Codex CLI otherwise shares a
  rotating refresh token with the OMP sessions in `~/jinleic-workspace`).

## Records

- `problems/<id>/record.json` is an append-only log and the only authority for a problem. Never
  hand-edit records, `attack-e*/`, or the generated `INDEX.md` and `TABLE.md`.
- More time for a problem is always `python3 ri.py requeue <id> --stage <stage> --reason "..."`.
- The sweep orders first visits only. It never continues, refills or revisits a problem by itself.
  The owner chose the book-order traversal (2026-10-14) as an exception to the workspace's
  FRONTIER_METHOD §1/§6. FRONTIER_METHOD still governs each visit, and every outcome carries a §5
  state.

## Code

- `ri.py` is stdlib-only Python. After any change run `python3 -B tests/test_ri.py`, which makes no
  model calls. Keep the stage prompts in `prompts/` and the strict schemas in `schemas/` in step:
  the tests validate the fixtures against the schemas.
- Test changes against a scratch root (`ri.py --root <copy> run --quota-scale 0.5 ...`), never
  against `problems/`.

## Boundaries

- The explorer reads, but never writes, these paths in `~/jinleic-workspace` (`config.json`
  `workspace`):
  - the book PDFs and the dossiers in `ai4s/`;
  - `docs/knowledge-system/DELEGATE_MODELS.json`, the single source for models and efforts;
  - `math/` and the archived `research-institute/` trees, used as local literature leads.
- `ai4s/` belongs to separate live sessions. The queue skips `inventory/ai4s-owned.json` and any
  article an ai4s dossier names. Do not attack those without the owner's go-ahead.
- Commits use the noreply identity configured in this repo. Do not push unless the owner asks.
