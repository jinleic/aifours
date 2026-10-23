# Erratum 1 to structural-note-S2-v1.md (2026-10-19T03:39:56-0700, ContinueCFR21)

Base note: /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/structural-note-S2-v1.md, sha256 8426a3295102d66f1942a9f3bff74071f30450366492d8f6d5da62b5dbfb1321 (preserved unchanged).
Found by the parent (message 2026-10-19, read of S2 v1).

E1 (sign error, section 1(c)). With the stated rule tau'_g = tau_g + (1 - mu_g) a and mu_z = -1, one has
tau'_z = tau_z + 2a, so the translation must be a = -tau_z / 2 (2 is a unit mod 39), NOT a = tau_z / 2 as written.
The remaining steps of 1(c) are unchanged and give tau_s = 0 after this translation.

E2 (simpler uniform argument; replaces 1(c) and the C2/C3 remarks). Checked on the actual anchor raw file
(sha256 3c8dbe62da8705eb6e713e85dae4d2fbf303614b2254f832a7291fe2f38a882a) by a direct stdlib check in the worker kernel:
the all-zero column c0 is one of the 39 columns, both generators (16,(012)(345)) and (-1,id) fix c0, and both map the
column set onto itself. Hence every g in G6 fixes c0. If f(g.c) = mu_g f(c) + tau_g for all g, then at c = c0:
f(c0) = mu_g f(c0) + tau_g, i.e. tau_g = (1 - mu_g) f(c0) for every g in G6 (and in every subgroup). Translating
f' = f - f(c0) (which keeps [D; f'] a DM) gives tau'_g = tau_g + (1 - mu_g)(-f(c0)) = 0 for all g. So every twisted
G6-, C3- or C2-equivariant seventh row of this anchor is a translate of an untwisted one with f'(c0) = 0. The scope
of T1 (and of the planned C3/C2 runs) therefore covers the twisted cases.
Status: T1 remains a single-producer scoped negative pending the independent route-2 replay.
