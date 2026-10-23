# Review packet index (lane `kirkman57`)

Inputs a reviewer should pin (SHA256 at the time of writing; re-hash before use):

| Item | Path | SHA256 |
|---|---|---|
| LKTS(57) certificate | `../evidence/lkts57-g513/lkts57_g513.txt` | `09a9d8ca0602ed28541e170ada7f096871311c29fd4515b6fea3e25f72b05f09` |
| LKTS(57) seed | `../evidence/lkts57-g513/lkts57_g513_seed.json` | `7c032dd406017a8cb17018ece32fcc2532db05c7d7fc4224a05cbb022df7cbb8` |
| LKTS(87) certificate | `../evidence/lkts87-g903/lkts87_g903.txt` | `65ab29ae6d24545c4ed41c3a4ea027becdf497b6810384b728379cfd0cae273e` |
| LKTS(87) seed | `../evidence/lkts87-g903/lkts87_g903_seed.json` | `d967896610216e16f70981e762b80c533d1f597b8c653da95474801bd3f16cef` |
| Seed expander (stdlib) | `../code/expand_seed.py` | `f776c276df903b8e3de5de8b58144617c5ac2ecadf6515290c03c164b4518d4e` |
| Lane checkers | `../code/check_lkts57.py`, `../code/check_lkts57.c` | hashes in the receipts |
| Lemmas | `../sources/automorphism-lemmas.md` | re-hash (changes logged in README) |
| Pre-review lemma snapshot | `automorphism-lemmas-pinned-v1-184ba0ab.md` | `184ba0ab5532f39c08396d986c274b2f323c0079ca36130ea11d69228cc29263` |
| Framework (2q+1) | `../sources/framework-2q1.md` | re-hash |

Reviews already performed by the parent (receipts in
`institute/runs/six-lane-2026-10-16/review/`): independent stdlib checker on both
certificates; G513 action audit; Codex gpt-6.1-sol (cross-vendor) independent
verification of the 57 certificate (VALID); a read-only lemma review
(accept-with-fixes; fixes applied, see `../sources/automorphism-lemmas.md`
Lemma 3, prime corollary, Corollary 5a); seed replay of both files; priority
screen. Reviews still useful: cross-vendor review of the 87 certificate and of
Theorem A / Proposition B in `framework-2q1.md`.

What a reviewer should try to break: (1) any false PASS path in the checkers
(e.g. accepted duplicates, missing pairs, header handling); (2) whether the
claimed group actions really permute the block sets (the certificates are
valid regardless); (3) the proofs of Lemmas 2–5, Proposition 87-D, Theorem A,
Proposition B; (4) novelty/priority statements, which are limited to "no earlier
construction located".
