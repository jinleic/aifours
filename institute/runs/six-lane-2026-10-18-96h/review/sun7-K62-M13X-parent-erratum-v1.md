# M13X parent mutation-diagnostic erratum

Recorded at 2026-10-19T13:20:03-0700. Apply after proof `b86bb186e425ea5ac69a51d85ad5f56cfc1abd2a08c66c169fd54de074262db9`. Codex [review](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-M13X-codex-v1.prompt.stdout.txt) `9bf84a110b060e1a399d1f91e14f2eea8c72b1f97aae64d38ca25a6efa9b72aa` accepts every mathematical claim, 0 FATAL/0 MAJOR/2 MINOR diagnostic-reference findings. Main statements/proofs/imports unchanged; not a parent acceptance.

1. **X:313, mutation 2.** Replace the claim that losing DEG at t breaks FB(vii) by: "DEG at t is then unavailable in the final theorem's Step 1." FB(vii)'s isolated fifth vertex is not t, since t is already in Q in that case.
2. **X:317, mutation 7.** Retain "T16 survives". The full ONE statement needs EQS when the cherry apex is t. The relevant FB pointer is **FB(v)** when t=c or t=q, so one forced (2,4,4) triple has apex t. The forced apexes in FB(vi) are c,q, and in FB(vii) q; those are not t.

These are diagnostics of this route, not independence/countermodel assertions. Full M13 remains CANDIDATE_UNVERIFIED pending the corrected second-family review and parent decision. No orientation-(1,1) conclusion is added.
