# F867 pre-run signal/settlement correction

Recorded UTC 2026-10-31T02:54:11.683Z. V1 uses a nonthrowing SIGALRM latch but has no SIGINT/SIGTERM latch, registers its alarm before the protected try, and does not explicitly flush its terminal output. A parent supervisory stop could therefore lose its terminal partial status. This is ONE pre-run lifecycle DESIGN MAJOR; v1 remains UNRUN.

New immutable v2 installs sticky SIGALRM/SIGTERM/SIGINT handlers and the timer inside its protected try, distinguishes observed signal from cooperative clock deadline in the status reason, and explicitly flushes terminal status. All physics calculations and controls are unchanged. An external hard kill or broken output can still lose settlement; absent terminal status remains NO VERDICT, not an invented pass. No child or v1 run occurred. Parent must read all operative v2 lines before an independent one-shot GO.

V1 {"path":"/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f867-fourqubit-high-defect-physical-exact-finite-author/fourqubit-high-defect-physical-exact-v1.py","sha256":"5f722df64060b8b2130317c599b932adce053d6eb8e5a3c9a0fac30749dbcc1a","bytes":27015,"LF":760}
V2 {"path":"/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f867-fourqubit-high-defect-physical-exact-finite-author/fourqubit-high-defect-physical-exact-v2.py","sha256":"7971e315f1cea3fea4e9e5322bca0c78c9d3e5ea36d4b5ca5b6ce2bd16f7d848","bytes":27221,"LF":764}
