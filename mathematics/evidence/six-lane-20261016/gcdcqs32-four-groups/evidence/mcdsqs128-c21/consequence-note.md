# Consequences of the gcDCQS(32⁴ : 0) certificate (lane note, E11f)

Written 2026-10-17 after 15:48:10 PDT (host clock) by worker `MathMcDsqs128`. This is a short written
note, **not a formal proof**: the imported theorems are named, not re-proved, and the source's
constructions are taken as published. No novelty, priority or significance claim; the parent's priority
audit is separate.

Sources: Tan–Zhou arXiv:2503.11934v1, pinned text `mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt`
(sha256 `df52a8f1…4c3c8164`; line numbers below) and, for exact statements, the v1 LaTeX e-print
`sources/e11/arxiv-2503.11934v1-mcDSQS-0314.tex` (sha256 `ca37944c…9550`).

## A. Explicit and checked: an mcDSQS(128) = mcDSQS(2⁷)

Construction 2.1 (lines 292–335) with (g, n, s) = (32, 4, 0) needs a gcDCQS(32⁴ : 0), an mcDSQS(32)
and a gcDSQS(32, 0); with s = 0 the last is again an SQS(32) with minimum colourable derived designs,
so the Appendix B mcDSQS(32) of Lemma 3.4 serves for every group. Inputs: the gcDCQS certificate
`evidence/gcdcqs32-c23/gcdcqs32_c23.txt` (sha256 `e38945b1…0f46`) and the Appendix B transcription
`sources/tz_appb_mcdsqs32.json` (sha256 `5ab58710…d8aa`; E0, and E11a: matched by a Ghostscript text
route and by the LaTeX source). Output `mcdsqs128_c21.txt`, sha256
`a97b1ae50fa8f0dc7f3bb6908e6c714fdd233eeede2607c2d16c2101380fd326`. Acceptance does not rest on the
construction: two definition-first checkers verify every 3-subset of the 128 points once and, at all
128 points, 64 partial parallel classes partitioning the derived STS(127). Minimality of 64 needs no
import: a partial parallel class on 127 points has at most 42 triples and 63 · 42 = 2646 < 2667.

## B. Conditional family via Corollary 2.6 (lines 684–693; written argument only)

Corollary 2.6: for m ≡ 4, 8 (mod 12), a gcDCQS(m⁴ : 0) and an mcDSQS(m) give an mcDSQS(m · 4ᵗ) for
every t ≥ 2 (the source writes n for t).

* m = 32: 32 = 2 · 12 + 8 ≡ 8 (mod 12).
* gcDCQS(32⁴ : 0): the certificate above. mcDSQS(32): Lemma 3.4 / Appendix B (lane-checked).
* The proof applies Construction 2.4 (statement lines 568–569, proof 571–679; hypothesis
  4m + s = 128 ≡ 2 (mod 6)) and imports Theorem 2.5 (lines 680–683):
  (1) a 2-RSQS*(4ᵗ) for every t ≥ 2 ([21] Xu–Bao–Ji, DCC 88 (2020), Cor. 3.2);
  (2) an RDTD(3, 4, 32), since gcd(32, 4) = 4 ≠ 2 and gcd(32, 18) = 2 ≠ 3 ([9] Ji–Yin, JCTA 117
  (2010); [21]).
  This yields a gcDCQS(32^(4ᵗ) : 0), and Construction 2.1 with the mcDSQS(32) (s = 0) an
  mcDSQS(32 · 4ᵗ).
* 32 · 4ᵗ = 2^(2t+5) = 2^(2n+1) with n = t + 2, so t ≥ 2 ⇔ n ≥ 4. This is the source's own
  conditional statement in §4(2) (lines 1111–1113).

Taken together, and conditional on the imported theorems and on Constructions 2.1 and 2.4 as
published: an mcDSQS(2^(2n+1)) exists for every n ≥ 2. Here n = 2 (order 32, Appendix B) and n = 3
(order 128, part A) are explicit and lane-checked, and n ≥ 4 is the written Corollary 2.6 argument.
Order 128 is not covered by Corollary 2.6, which needs t ≥ 2; it comes from Construction 2.1 directly.

## C. Imported application (not checked here)

Corollary 1.4(1) (lines 186–187; LaTeX: q₀′(3, 4, n) = n/2 + 1) rests on [16, Theorem 5]
(Shi–Xia–Krotov, JCTA 200 (2023)). It states that for n ≡ 2 (mod 6), n ≥ 20, an mcDSQS(n) gives
q₀′(3, 4, n) = n/2 + 1. Since 2^(2n+1) ≡ 2 (mod 6), this would give q₀′(3, 4, 128) = 65 from part A, and
q₀′(3, 4, 2^(2n+1)) = 2^(2n) + 1 for n ≥ 4 under part B's conditions. Imported statement only.

## Checked versus imported

| Item | Level |
|---|---|
| gcDCQS(32⁴ : 0), sha256 `e38945b1…0f46` | explicit certificate; lane checkers + parent's three routes |
| mcDSQS(32), Appendix B | explicit; lane-checked (E0 check, E11a three-route transcription match) |
| mcDSQS(128), sha256 `a97b1ae5…d326` | explicit certificate; two definition-first lane checkers, 20 retained mutations, byte-identical replays; parent verification pending |
| Constructions 2.1, 2.4 (general), Corollary 2.6 | source proofs, not re-proved here |
| 2-RSQS*(4ᵗ), t ≥ 2; RDTD(3, 4, 32) | imported (Theorem 2.5, [21], [9]); not re-proved, no certificate |
| q₀′(3, 4, n) values | imported (Corollary 1.4, [16]); not checked |
