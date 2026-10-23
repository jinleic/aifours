# HIGH-K-CORE handoff v1 — NOT_PROVED with candidate auxiliary necessary structure

Metadata clock:2026-10-21T17:16:12-0700 (`/bin/date` before exclusive creation).
Owner OlsonThirdCutWindow, same math2 slot/one-third throttle. CANDIDATE ONLY; parent alone runs gates/verdicts.

## 1. Outcome

Outcome (c): HIGH-K-CORE-COVER NOT_PROVED. None of LOW-CORE, TOP-CORE, P-CRITICAL-DIAGONAL is excluded.
The complete necessary system is UNCHANGED: accepted HK1 HIGH-K-RES (R0)-(R3) through worker erratum1 and
parent errata1-3 (all pasted). The first unproved lemma is still HIGH-K-CORE-COVER on the whole unbounded core.

Candidate auxiliary necessary consequences of (R2), proved by hand in proof-HIGH-K-CORE-v1.md (14345B/185LF,
SHA2562e3c17a67bdb617df60d2896b1d7a91fbe6a7df484b56651ea6662e2d7da76db). GRX is exact, so these leave the
residual set unchanged; they are not exclusions, replacements, feasibility, exactness or converse claims:
- Z1: every core cell has at most 2kappa-1 zero rotation letters. Z2: if kappa<=(p-1)/2, either none or at
  least delta+2, where delta=p+2kappa-k. So every k=p+2 cell with kappa<=(p-1)/2, including all of LOW-CORE,
  has no zero rotation letter. Empty gaps are distinct from zero letters throughout.
- TOP-CORE (normalised by an automorphism): BIG-RUN (some run has |#a-#(-a)|>=p+D, by an explicit five-step
  single-run path keeping m>=2 across accepted HK1 Phi>=4 heaviness); all-plus bounds; SIDE (heavy sign iff the
  big run is outside the minus set); exact W-form for heavy patterns; Phi2 BALANCE (D>=1: no balanced Phi2
  pattern; D=0: T forced). These use HK1 item3, general GRX and classical Cauchy-Davenport only.
Concrete failed steps: TOP needs label coupling of T(P) across patterns (one pattern never suffices, since
|Sigma(W_P)|<=p-1 is allowed); LOW: pure length-4 identities are permitted, so HK1's COLOR step is unavailable;
diagonal: Theorem P's own Boolean-box count is M=3p-3=deg-bound, exactly one short, and singleton-rotation
variables break even parity or linearity. These are method failures, not no-go theorems.

## 2. Sources (two parts; Main notified before the second)

1. review-sources-HIGH-K-CORE-part1-v1.txt:84058B/876LF, 13 blocks,
   SHA25697330ace81e0fff95dac679ba62796f8451e0a3b940633d3134e83782a73f55f: new proof, operative scope,
   acknowledgement, cp01-04, HK1 verdict, parent errata1-3, worker erratum1, full HK1 proof.
2. review-sources-HIGH-K-CORE-part2-v1.txt:61901B/648LF, 14 blocks,
   SHA2567725ce41355187418ca3862541c28a7053d31b9b736b461f7c67fc120903e0e7: HK1 disposition, entire Theorem P
   proof with its own verdict/errata1-2/disposition, UPAR5 boundary erratum2, scope addendum2, deviations v12,
   and the own records actually used for general GRX (notes-GRX-v1 whole + lowodd verdict v2 whole) and NF data
   (few-E v4 LF28-43 only, the accepted normal-form paragraph + fewodd addendum whole + zx-s1c verdict whole).
All15 scope governing inputs are pasted whole. S(p) and lane CT are NOT premises of new lemmas; S(p) trust is
inherited only through HK1's kappa>=2 boundary, CT only as HK1's literal all-plus test in the residual.
Ordered manifest review-manifest-HIGH-K-CORE-v1.json (8262B, SHA2569cfb2699866c85538c7e79c3e4d77929c151996142aed9bc168a67361a7b9e64)
gives format/header-reuse rules and exact blocks; coverage source-coverage-HIGH-K-CORE-v1.json (12287B,
SHA256dbe4b691474cbb0eddf5f56364858d3951c1b82ad245fd0cf7e191afd9e54e1d) gives whole/partial status per file.
Both parts go to EVERY family; any load-bearing omission triggers both-family re-review, not a patch.

## 3. Process and machine ledger

Operative scope read first (5b1bb517765e2c247679538ce25ad344f5f050bafb0511337531882dc4131b3f), then mkdir
and the exposure acknowledgement (16:27:40) BEFORE any new reasoning; its "16" governing-input count is a
clerical error, corrected to 15 in cp01 at Main's instruction. Then shasum/wc of all inputs (all pins match),
full reads of the governing bodies, hand derivation, checkpoints cp01-04 (16:40:00, 16:52:33, 17:07:22,
17:13:43; gaps740/753/889/381s, all <1200s), exclusive creation of the manuscript, metadata rendering of
the two parts (source-line numbering only), manifest/coverage creation, shasum/wc, /bin/date17:15:37 and
17:16:12. Progress and the second-part notice were sent to Main before creation. Permanent history (UPAR4
MAJOR, parent enumeration MAJOR, both terminal-k pre-ack MINORs, parent lower-terminal scope MAJOR, clerical
defects, initial HK1 P-source coverage history) is uncured. No scientific code/computation/enumeration/
assertion/test/solver/Lean/native/model/network/nested agent, /tmp, git or deletion; all writes exclusive in
this directory. No full ordered Olson, lower-terminal, p=5, novelty, human/Lean or runtime claim.

| Preceding file | Bytes | LF | SHA256 |
|---|---:|---:|---|
| HIGH-K-CORE-exposure-acknowledgement-v1.md |7658|92|3dcddebaeec1c871692e33eb390b9cf41bdf9e398c8a189a200b0626fdf23b19|
| proof-HIGH-K-CORE-v1.md |14345|185|2e3c17a67bdb617df60d2896b1d7a91fbe6a7df484b56651ea6662e2d7da76db|
| review-sources-HIGH-K-CORE-part1-v1.txt |84058|876|97330ace81e0fff95dac679ba62796f8451e0a3b940633d3134e83782a73f55f|
| review-sources-HIGH-K-CORE-part2-v1.txt |61901|648|7725ce41355187418ca3862541c28a7053d31b9b736b461f7c67fc120903e0e7|
| review-manifest-HIGH-K-CORE-v1.json |8262|39|9cfb2699866c85538c7e79c3e4d77929c151996142aed9bc168a67361a7b9e64|
| source-coverage-HIGH-K-CORE-v1.json |12287|44|dbe4b691474cbb0eddf5f56364858d3951c1b82ad245fd0cf7e191afd9e54e1d|
| checkpoints/cp-01.md |2370|27|d51baa55ab6e9640cc8374e718ea234d4a950639e7d1633bd6c2d9eb0d9a6c06|
| checkpoints/cp-02.md |1945|24|5f0ed2a3fb454110d3a0e95484f8fcc6cf3a189bf613d96697a97bd7246b8329|
| checkpoints/cp-03.md |1964|22|42107d3e74cb7cc7430e36ae6f7b8a76cdcbae2ed5687d59f22bd79031b848fa|
| checkpoints/cp-04.md |2037|23|cb99ba9b0757ecf20cd8ec3d2a4a095757bc97067f1afa2d13653eda4adf889f|

This package is bound by cp05. Park after handoff; no new target, derivation or model launch.
