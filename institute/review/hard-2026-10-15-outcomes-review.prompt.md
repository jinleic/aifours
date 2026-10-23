You are an independent, read-only reviewer. Do not modify any file. Read only paths under
/Users/jinleic/repos/aifours and the engine /Users/jinleic/jinleic-workspace/research-institute/explorer/ri.py.
Do not read credentials, keychains, home-directory dotfiles or any other path.

Goal: find overclaims, wrong numbers, wrong times, misattributions or missing caveats in a parent-written
summary of a finished three-problem research run. The generated records are the authority.

Authority (generated; compare against these):
- institute/runs/hard-2026-10-15/problems/{math-p0039,info-p0403,phys-p0422}/record.json
  (log entries with t=="attempt": epochs 0, 1, 2; `output` holds attack/replay/review outputs; epoch 2 = batch 03)
- institute/runs/hard-2026-10-15/run.json, parent-check.json, supervisor.log
- engine outcome semantics: ri.py functions decide_review and final_outcome, and the OUTCOMES table

Parent-written material to check:
1. institute/review/hard-2026-10-15-outcomes.md (main target)
2. institute/runs/hard-2026-10-15/batches/03/receipt.json (numbers, hashes of copied files vs originals)
3. institute/review/physics-subcavity-control/{trials.json,result.json}: does the control keep the
   certified laws in attack-e2/certificates/trials.json unchanged except alpha, and do results match the
   ledger's numbers? Was the snapshot hash unchanged?
4. institute/review/information-degree-theorem-audit.md: is the proof audit mathematically right?
   (balanced nine-variable Boolean functions, Walsh divisibility and Parseval; attack-e1/degree-bound-proof.md)
5. The 2026-10-15 run paragraphs in README.md, institute/README.md (Budget section and the outcomes pointer),
   institute/runs/hard-2026-10-15/README.md, mathematics/README.md, information-science/README.md and
   physics/README.md (only their "Difficult-problem visit (2026-10-15)" sections).

Check specifically:
- every time (PT = UTC-7), duration, minute total, claim count, verdict count and numeric bound;
- that "no claim judged wrong or unsupported" is scoped to batch 03 only;
- that mathematics' larger C-run ranges are never presented as certified bounds;
- that information science never claims existence or nonexistence of a balanced 242 function;
- that physics is never called novel, formally verified or peer reviewed, and that the prior-art
  statements (Franz–Leone for even k as summarized by Mertens–Mézard–Zecchina; Lelarge–Oulamara
  condition (4) for odd arity) are fair to the cited sources if you can open them;
- that the decision not to requeue is consistent with the recorded times and the 18:02:24 PT cutoff.

Output: a Markdown review. Start with a one-line verdict: ACCEPT, ACCEPT-WITH-FIXES or REJECT.
Then list each finding with severity (blocker/major/minor), exact file:line, the evidence you read and
the exact replacement text. If nothing is wrong in a category, say so briefly. Do not restate the summary.
