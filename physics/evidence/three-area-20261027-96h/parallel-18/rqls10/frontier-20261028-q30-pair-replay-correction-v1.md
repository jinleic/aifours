# Correction: q30 pair-shape replay v1 was invalid and its output was overwritten

Native `/bin/date`: **Wed Oct 28 22:52:06 PDT 2026**. This is an additive chronology for a local auxiliary check, NOT a QLS10 result.

The initial `frontier-20261028-q30-even-pair-replay-v1.py` SHA **c75b10f7668e75216eb8482cd49e794fa2a56b62d3a8d64273a3654f4032f398** returned the histogram `[1,0,0,802,6559,32954]` at **2026-10-28T21:12:04.678607-07:00**. It was INVALID: when reconstructing w4 the program omitted the required subtraction of w3. A concrete accepted false witness in five `(u,u+5)` exponent pairs was `[(0,0),(0,6),(15,15),(3,6),(15,21)]`; direct exact recomputation showed both the ordinary and Fourier-weighted sums nonzero.

During diagnosis the same v1 script was invoked a second time and overwrote its v1 JSON output at **2026-10-28T21:12:31.077277-07:00**. The initial v1 JSON hash was NOT recorded and its original bytes are no longer preserved; the currently existing overwritten v1 JSON SHA is **ca8667ada0fe38ceb0ff00b3ce80f3963be1f86f9ab7c305c72658d392a689e3**. This overwrite is disclosed, not represented as an append-only receipt or as a successful independent replay.

New corrected `frontier-20261028-q30-even-pair-replay-v2.py` SHA **f41fe3627228760ddf895ac39db307104bc3bc82b937e1a5c6900e4f74069b47**, result SHA **a95afcaa47c5233b6a3fa013d8717bf5065c85b03b42b07fb9f8e9adcfe67701**, uses `w4=-(w0+w1+w2+w3)` and independently matches the producer's exact coefficient-shape histogram `[1,0,0,396,6676,31500]`. These are ONLY pairwise necessary-shape counts, not a proof of any complete transversal or exclusion. The invalid v1 histogram is not input to the q30 no-go (none claimed), the even-order family results, or the order10 conclusions.
