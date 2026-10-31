# F873 pre-run signal/settlement correction

Recorded UTC 2026-10-31T03:01:47.093Z. V1 installs a THROWING55-second SIGALRM before the protected try and has no TERM/INT latch; the handler can interrupt setup/settlement. Unexpected exceptions also bypass its named failure status. ONE pre-run lifecycle DESIGN MAJOR; v1 is retained UNRUN, neverGO.

New immutable v2 changes allthree signals to a nonthrowing sticky latch, installs them inside the protectedtry with40-second internal alarm/cooperativeguard, and emits ERROR_NOT_PASS/nonzero for other exceptions. Parent separately enforces outer<=55s; hardkill or broken output remains NO VERDICT, no invented settlement. All mathematical checks and enumerationdomains unchanged. Complete v2 read and a separate one-shot GO are still required.

V1 {"path":"/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f873-olson-nine-run-actual-selector-exact-finite-author/actual-selector-offset-p7-v1.py","sha256":"6e060cc38d2a059739b1fd1e3247b41cba5d0dc9e7064e5c8327fc55d7857a20","bytes":23898,"LF":581}
V2 {"path":"/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f873-olson-nine-run-actual-selector-exact-finite-author/actual-selector-offset-p7-v2.py","sha256":"08aa1ae57a266e4bab76d5910988844188bdf8c18181be6b3882ab2d76105892","bytes":24258,"LF":590}
