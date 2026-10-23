# Ordered Olson: full balance and room without the earlier length restriction

Recorded at 2026-10-19T02:20:21-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIALS (written).** Lemma FB, Corollary FB-E, Theorem ROT-FB clauses(a)/(b), and Corollary INV*/OLSON-FB hold relative to their recorded accepted imports and mandatory erratum1. No computation is a premise.

## Exact accepted scope

**FB:** in(S′), for EVERY longest zero-sum Z and EVERY index-<1 generator g of its zero-sum-free complement Y′, S(N)≤2p−1−W. Thus S(N)=n_+ and W+n_+≤2p−1. There is no comparison hypothesis between L=|Y′| and |Z|=2t. The requirements L≥p+1, t≤kappa<p and the stated sequence length/oddness remain essential.

**ROT-FB:** for primep≥7 and a length-(4p−2) avoider overD_(2p), rotation rigidity follows if some admissible normal form has kappa^≥1 and either:
- 2≤k≤p−1 with(S1) at kappa^ (automatic from GRX plus S1-sharp when kappa^≤floor(2p/3)); or
- k=p and EVERY zero-sum of its rotation sequence has length≤2kappa^−2. This forces L≥p+2, not L=p.

**Uniform consequence:** for primep≥7, o_F≤p−1 and F−o_F≥2(p−1−floor(2p/3)) imply INV* for every length-(4p−2) avoider and an identity2p-subword in increasing index order for every length-(4p−1) word. Atp31,o_F30 the condition is F≥50, compared with the preceding ZB+ condition F≥60. These are sufficient conditions, not claims that avoiders exist elsewhere.

## Frozen evidence

- [Candidate](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-FB-v1.md) SHA256 `339dcadcd914a9f036ea71a5ec2b5d3f0678cc100e22aca9de2d75751373cc6b`.
- [Mandatory erratum1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-FB-v1-erratum-1.md) SHA256 `33de46d245ec89a31cce1a06ac44a11f2c81c91a713b0830c59f31686245e202`.
- [Codex](olson-fb-codex-v1.prompt.stdout.txt) SHA256 `1c585d1f8a7dcb105cf8f3ed69714ad7642479f8d9500c36ae2ff1ca3e0477e1`: ACCEPT allfour items includingk=p; no required finding. Observed CLIgpt-6.1-sol.
- [Claude](olson-fb-claude-v1.prompt.note.md) SHA256 `0521132c5d97c2a1e6db46df22f07f9db71fb7b12da5183cf497769f691d9997`: FB/FB-E/uniformcorollary ACCEPT, ROT-FB ACCEPT-WITH-FIXES, 0FATAL/0MAJOR/2requiredMINOR +5optional. Observed CLIclaude-opus-5-5.
- [Accepted ROT-KP caller scope](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-rotkp-parent-verdict-v1.md) SHA256 `dfb2fd0bdd05ae33a02b41fec318823115384ce7126758d27fe837a6e3bbfcf3`: parent re-read thek=p SHgen/SHgen-E scope and equality-case overlays, resolving R1 independently of the worker's citation.

## Independent parent derivation

Setdelta=2p−W. If S(N)≥delta, order the negative weights decreasingly and let r≥2 be the first crossing, x=r−1, y=S_r−delta. Then x s_r≤delta−1 and y≤s_r−1. The elementary inequality(x−1)(s_r−1)≥0 gives y+r≤s_r+x≤x s_r+1≤delta. The available unit count m≥slack+3 exceeds y, so removing y units of Y′ and the r largest negative occurrences from Y produces an actual occurrence-subsequence Z*. Its coefficient sum is2p+n_+−S(N), divisible by2p. Its length exceeds|Z| by L−(y+r)≥L+W−2p≥2, contradicting longestness. Thus S(N)≤slack; congruence and0≤n_+<2p force balance.

FB-E gives E≤k−1−2kappa+n_+, with n_+≤k−1 and, for t≥1, n_+≤2t−1. Hence SHgen(H) holds for k≤p. SHgen(K) follows from KETA's k-free inequality E+2: for k≤p−1 it is≤k; at k=p the stronger t≤kappa−1 gives≤p−2 (or≤p−1 ift0). The k=p branch still uses L≥p+2, so no index-one/REALIZE theorem is used at its invalid length-p boundary. Normal forms and the accepted deletion ledger preserve the uniform bound on F−o_F; restricted REFL is applied to the original word witho_F≤p−1.

## Review dispositions and earlier wording correction

R1 is closed by the accepted ROT-KP k=p caller/equality scope and ZXoverlay4/generalizedV3. R2 replaces the opaque ROUTE-ALL(T) label by its explicit E_c/H/K content; if the longest zero-sum has length exactly2kappa, (S1) is automatic. The integer crossing bound, redundant(b)hypothesis removal, canonical E_c identification and residual qualifications are recorded in erratumO1–O5.

The old ROOM argument needed longestness AND L≥2t, but not balance for its W-bound. Earlier parent shorthand “only longestness” omitted the L≥2t hypothesis. FB genuinely removes that comparison hypothesis while retaining L≥p+1; erratumO3 governs that wording.

## Open boundary and trust limits

Within terminalk≤p−1, the remaining rotation cases have kappa^>floor(2p/3) and(S1) failing (then GRX(ZP) forces a zero-sum of length≥2p+2). Atk=p, kappa^≥2 with a zero-sum of length exactly2kappa^, or(S1) failing, remains open. Terminalk≥p+1 and reflection rigidity foro_F>p remain open. A word is residual only if EVERY admissible normal form misses accepted criteria.

Classical index-one/Savchev–Chen/Yuan, EGZ and the previously accepted word-level chain remain imports; their2007proof bodies were not read here. No Lean, human review, novelty clearance, full dihedral theorem or all-groups Olson result. The length-sensitive S1 conjecture and conditional S(p) note are separate, unaccepted research directions.
