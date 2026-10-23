# RPdelta parent erratum: five second-family MINOR findings

Recorded at 2026-10-19T13:03:37-0700. Read the eight candidate texts with their earlier errata, then the [consolidated overlay](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/erratum-1-RPdelta-consolidated-v1.md) `2450446d526305e561ee2c8c05b1946dd704363f31d95eef58df5797d73a2136`, then this overlay last. K/K-e/T/B/B-e1/B-e2/BP/BP-e mean the exact source pins in [the v2 review freeze](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RPdelta-claude-v2-deferred-freeze-v1.json) `2e4fb95f6ab459a999cd6b428e6ff26eb24aa2d052f20515c37f937729f078d9`. Existing files are unchanged.

Source: [Claude v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RPdelta-claude-v2.prompt.note.md) `a6bd0e096ecb62897638715909f37b016ca8f6354ac8463d8f6cf5487d8caaac`: ACCEPT-WITH-FIXES, no FATAL/MAJOR; five distinct MINOR findings K-1, K-2, T-1, B-1, B-2 (the last two are shared by B and BP, not two further findings). No theorem statement or range changes. The earlier five Codex findings remain disposed by the consolidated overlay E1-E5.

## K-1: K-e:19-21, remove the absent erratum-4 proof reference

Replace e3 by: Corollary SEG-k first excludes kappa < 0 by Pairs. Its first hypothesis then gives R = 2p-k+2kappa <= 2p-2kappa-5 <= 2p-5. Hence Pi_need = p-ceil(R/2) >= 2. Only the accepted v5 erratum-5 I.12 positive-budget loop is needed here; no appeal to erratum-4 or its obsolete narrowing is needed.

## K-2: K:34-41, exact parity endpoints and ledger

Read the comparison and remaining-cell paragraphs through v2 package D1/D2 and consolidated E1. Specifically the lower condition is not always ceil((p+3delta+2)/4): for even delta with p+3delta congruent to 3 modulo 4, SEG-k reaches the endpoint (p+3delta+1)/4. This endpoint exists exactly under D2. It can exist when the SEG-num interval is empty (p=31, delta=4, endpoint 11, SEG-num interval [12,11]). K:34-41 is superseded as a coverage description by those exact formulas; no broader band or realizability claim follows.

## T-1: T:59-60, a sufficient rectangle bound, not an attained box minimum

Replace the assertion that the minimum of 2g-b occurs at (1,B0), with its claimed equivalence, by: on the entire allowed box, 2g-b >= 2-B0. Therefore A0+floor(D0/2) <= p+1 suffices for the second SEG-k inequality. If B0=0 the corner (1,0) is excluded by g+b>=2; no attained-minimum or necessary-condition claim is made. T2's sufficient hypothesis is unchanged.

## B-1: B:27,30 and BP:17, justify d >= 1

Within each stated range used by B.2 or B-prime, p-delta >= 1. P0 forces at least k-2kappa = p-delta odd rotation runs. An odd run is nonempty and its imbalance a_j-b_j is an odd integer, hence has absolute value at least 1 even if the run is mixed. Thus d = max |a_j-b_j| >= 1. Supply this argument before B.2(v) and (vii), and again when BP rechecks the required B.2 bounds rather than invoking B.2 outside its range.

## B-2: B:67,71-76 and BP:24-25, zero remaining gain

The correct unconditional estimate is G_need <= max(0, Pi_need-a-lambda+2). If G_need=0, choose all t_j=0; the already established width m_hi>=m_lo+1 gives B.3 immediately. Apply the chains bounding ceil(G_need/2) and G_need-W2/2 in B:71-76 and BP:24-25 only in the remaining case G_need>0, where Pi_need-a-lambda+2 is positive. In that case the printed chains are valid. This is also the reading already specified by the v2 package section 4.5 and the Codex review; no negative upper bound on a zero G_need is asserted.

## Unaccepted suggestion

Claude's separate observation about excluding (p,eps,delta)=(17,0,1) is not part of either theorem range or this acceptance. It would require its own written addendum and review. No claim that this packet resolves that cell is made.
