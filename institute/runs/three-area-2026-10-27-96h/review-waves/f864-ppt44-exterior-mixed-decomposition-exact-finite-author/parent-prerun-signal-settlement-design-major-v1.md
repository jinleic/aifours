# F864 pre-run signal/settlement correction

Recorded UTC 2026-10-31T02:50:36.159Z. The complete v1 source has a cooperative40-second deadline but no nonthrowing SIGINT/SIGTERM latch, and its per-case/terminal stdout was not explicitly flushed. Thus a supervisory stop could terminate before the protected failure path or strand partial evidence. Classify ONE pre-run lifecycle DESIGN MAJOR; v1 is retained UNRUN.

A new immutable v2 installs nonthrowing sticky SIGINT/SIGTERM handlers inside the protected run, checks the latch in the existing guard, and flushes per-case and terminal status lines. It preserves all scientific and control statements. The hard external timeout can still kill before a cooperative guard or on broken stdout; any missing status is NO VERDICT, never fabricated settlement. No source version was run by a child, no predecessor overwritten, and no GO is granted by this note. Parent must display all v2 bytes before a separate one-shot GO.

V1 {"path":"/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f864-ppt44-exterior-mixed-decomposition-exact-finite-author/finite-ppt44-mixed-exact-v1.py","sha256":"1be5ad786ffde98241a686572ef38179eb7ee4293602bb86641515bbe7b55df7","bytes":22759,"LF":643}
V2 {"path":"/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f864-ppt44-exterior-mixed-decomposition-exact-finite-author/finite-ppt44-mixed-exact-v2.py","sha256":"0346b17766af27e3950ef6eeb87ada45909eaa09c1bddf1359bc503ce83c2b48","bytes":23099,"LF":654}
