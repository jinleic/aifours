# Sun(7): CAP-62 and DT-A/B/C

Recorded at 2026-10-19T08:37:47-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** Finite representation and necessary conditions inside K6.2*, e_d>=4, e*=2. No complete subfamily exclusion or finite coverage has been established. Computer-assisted Sun(5)/Sun(6) remain transitive imports. No novelty, Lean or human-referee claim.

## Frozen text and reading order

- [K62-CAP-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-CAP-v1.md) `19dccc3d8bce5908a14ff96462a05beeb38ba966374c8c4740e6a66a312b16d5`
- [K62-DT-A-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-DT-A-v1.md) `cd7266d4071a8c91ac753b1f9900d690b72cf667f74046a1f90b5b449afd1a70`
- [K62-DT-B-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-DT-B-v1.md) `51960d44d60fa50901a3201143410f935750852d1ccd4c6e116f81a9c601604f`
- [K62-DT-C-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-DT-C-v1.md) `7e8bde21d6f5a162d5ecd5bd5950c90cbcd18763880bd1ee781d240b91f2186b`
- [K62-DT-C-erratum-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-DT-C-erratum-v1.md) `0f785140e10fe0e650ed683186e9e51f95abffce356e962172fcb0446a271a3b`
- [K62-CAP-DT-erratum-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-CAP-DT-erratum-v1.md) `996f924c731f0bfb1bf2a336d50d6ac0be50e55fb4ce134fa4b3cec2a1e2466d`
- [K62-CAP-DT-erratum-v2.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon/K62-CAP-DT-erratum-v2.md) `5970c0d5faeaeea4bb712899b4a50cdcfd4e81a303a0a51abf37d5c03cc68676`

Read the originals through combined erratum-v1, then erratum-v2. The original DT-C single erratum is superseded by combined CD21. The parent read v2 and the load-bearing light-fibre proof; all remaining reviewer fixes are explicit, with no strengthened theorem.

## Accepted scopes

Setting is exactly CAP §0: V={d,i*} disjoint-union O, |O|=5; n_d=2^e_d 5^h_d w_d, n_i*=4*3^f*5^h*w*, n_c=2*3^f_c5^h_c w_c, pairwise coprime w parts coprime to30, at most one higher3 marker and at most one5 marker. All arithmetic and necessary tests retain this setting.

1. **CAP-62:** every actual configuration maps into finite U62. Its listed normalised quantities, capped depths and pair-label gcds are pattern functions; absolute indices, counts and unnormalised slacks are not. No surjectivity or realisability assertion is made.
2. **Granularity:** C1 at an unmarked O vertex for family x with x_(d i*)=1; C2 at i* when f*=1, for both families and every orientation (gcd equals12).
3. **Row counts:** RC-O gives the x-row bound5/6 only when v is unmarked and the OPPOSITE entry x'_(d i*)=1. RC-i* gives11/12 when f*=1. These bounds are nonstrict; no extra slack or proper-subset grid. General light-fibre arithmetic is proof context, not an extra pattern-level rule outside these two instances.
4. **CAP(D):** a complete rule cover would imply exclusion, but no cover has been supplied. Strict consequences carry the LOSSY label and are never used as equivalences. The S_x replacement is genuinely weaker at n_d=16,32. The N(O) strict-count comparison is equivalent by integrality, but that equivalence is withdrawn as unneeded and does not make the count a pattern function.
5. **DT-A:** apex table in both families (admissible does not mean realised); CI/CI' at unmarked v for the family's OWN distinguished entry1; deep-triple types, raw-versus-capped depth, C2 and budget consequences only in the stated (1,1) setting and with Theorem DG's explicit four-subset hypothesis. The inequality 2theta4+3theta5>=3+4theta2+12theta1 is necessary, not equivalent to full DG(a).
6. **DT-B/C in G only:** no O vertex carries either marker; higher3 marker lies at i* or is absent, and5 marker lies at d/i* or is absent. Both distinguished entries are1. Accepted: positive-support R3/R4, B1-B5 including degree/no-K4/bowtie/diamond restrictions and oriented parity; residual description only (no connectedness or realisability claim). DT-C gives
   2N41+2N14+5N11+3N12+3N21+N22<=6,
   3<=|H_alpha|,|H_alpha*|<=7,
   s=N41+N14 in {1,2,3}, N11=0,
   N42+N24>=5,>=6,=7 respectively; at most3 O-pairs carry an entry1. Every graph implication retains its G hypotheses.

## Review and dependency closure

- Original dual reviews are frozen in [6cb9a897 package](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-CAP-DT-review-freeze-v1.json); proof repairs then received a separate dual review [freeze](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-CAP-DT-repair-review-freeze-v1.json) `78cd1f690611bdceb102299655bc7896788b069eefb0276e3d9b1b8032dd9084`.
- [Codex repairs](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-CAP-DT-repair-codex-v1.prompt.stdout.txt) `ea2292637a09e66fa0108107766b126a3955eb4312ebc71c9df708d221575c97`: observed gpt-6.1-sol/max, 0 FATAL/0 MAJOR/2 MINOR.
- [Claude repairs](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-CAP-DT-repair-claude-v1.prompt.note.md) `816ceaf719a0b93364c480fe0df8bfa5a6ab49af2243984845415cd328ed4497`: observed claude-opus-5-5/max, 0 FATAL/0 MAJOR/9 MINOR, plus pairing editorial.
- Erratum-v2 V1–V14 disposes all findings: RC rule scope/provenance, exact W1 withdrawal, LOSSY operational wording, CI' in residual conditions, pattern forms, full row citations, stale DG label, DG-4's unmarked-added-vertex scope and raw depths, L1+INV apex-table citation, oriented pairing.
- SH/DG authority is [cae455c3 verdict](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K62-SH-DG-parent-verdict-v1.md), with both mandatory DG errata. Direct small Sun uses do not remove transitive computer-assisted Sun(5)/(6).

## Remaining open
All O-marked cases, including (1,3)/(3,1); remaining G-patterns including f*>=2 and5-on-d branches; the higher-depth alternative for e_d>=5; complete U62 coverage; full K6.2* e_d>=4/e*=2; K7; Sun(7). M13 A–D are separate unreviewed candidates and are not imported by this verdict. No pattern-only implication is treated as a group realisability theorem.
