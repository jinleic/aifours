# Olson ONE-SHORT-LS: exact length p+2kappa

Recorded at 2026-10-19T12:11:41-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL**, written mathematics relative to the original accepted CF(a), CT, ROW and standalone AP' interfaces, plus **Lev2022 Theorem2 at statement level**. This proof invokes Lev in case(I) for every e=p-kappa>=2, including e=2. Lev's proof is not replayed. No word-level, unrestricted INV*, ordered Olson, LS+ or STAB claim is accepted by this record.

## Exact accepted statements

1. **Theorem ONE-SHORT-LS.** Prime p>=7, integer floor(2p/3)+1<=kappa<=p-2, Y a sequence of odd elements of C_(2p) of **exact length** |Y|=p+2kappa. If Y has no zero-sum subsequence of length in [2kappa+2,2p] (ZP_kappa), then every zero-sum has length<=2kappa (S1_kappa).
2. **Lemma IP and Corollary IP'.** At their printed standing hypotheses on odd prime p, integer0<=kappa<=p-1 and odd Y with ZP, every long zero-sum T (|T|>=2p+2) has |T|-v_iota(T)>=2p+1. Consequently the stated at-most-d-1 non-{g,iota} hypothesis excludes a long zero-sum. Read IP' with the mandatory explicit standing-hypothesis overlay.
3. **Lemma DOM.** At the theorem's exact-length/range hypotheses and with a long zero-sum, some odd generator g has 2kappa+2<=v_g(Y)<=2p-1, hence1<=d<=2e-2 and r<=p-2.
4. **Lemma AP-double-prime.** Prime p, N>=1, p>=3N+5, nonzero x in Z_p: if N+1 progression points lie in an arc of at most2N+2 residues, then x is in {1,-1,2,-2}, or N=1 and x=+-3, at the printed hypotheses.

## Text of record

| Item | SHA256 |
|---|---|
| [Frozen scope](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/one-short-ls/ONE-SHORT-LS-scope-v1.md) | `2b9cfbcdf66cf43b173aa2f9a43542c906b50e04cbae690a860e3c321dd5b872` |
| [Proof v2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/one-short-ls/proof-ONE-SHORT-LS-v2.md),276lines | `c544aad2ab0cadc4c76870dc97382b6a749bbdda85f96596bdb128efe9b19ffc` |
| [Review package](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/one-short-ls/review-package-ONE-SHORT-LS-v1.md) | `46a23fd0f1ae9f47762587e617ecab72cd666e45e83514fb00fc0b3d2cc07343` |
| [Excerpt manifest](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/one-short-ls/review-excerpts-ONE-SHORT-LS-v1.json) | `b1b3d3a8ad47b7b7eee397cb9531964edd60d7e33a9a419e6761d624fed2adc5` |
| [Review freeze](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ONE-SHORT-LS-review-freeze-v1.json) | `90a0121949af62e748331a4b75b6a90274cf3004d84536514bf048cedc7a3d92` |
| [Mandatory parent erratum](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ONE-SHORT-LS-parent-erratum-v1.md) | `35bcae46730f606d9fc24d3dbca4777b68b4e0adba569979faa36a48a8cbaf9a` |

Read the immutable proof/package and then this erratum. Six editorial/accounting findings: IP' standing hypotheses; why Lev's a is nonzero; all nonzero lifts rather than only +-p; Lev e=2 trust distinction; ROW constant citation; no unproved exclusivity-of-method claim. No main theorem/range/case split changes.

## Both-family reviews

- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ONE-SHORT-LS-codex-v1.prompt.stdout.txt) `dd2ec5570d1be85fbff8e6fe710b3a4d61e14caccbf3ca400ea0a2be1d5b7220`: gpt-6.1-sol/max/read-only, theorem and IP/IP'/DOM/AP-double-prime ACCEPT,0F/0M/0m.
- [Claude](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-ONE-SHORT-LS-claude-v1.prompt.note.md) `d718f61eee3445ca407fa11d066df05a0bf3e99f75152aac4cc9fdb33ee4142c`: claude-opus-5-5/max/no tools, all claims ACCEPT,0F/0M/6editorial/accountingMINOR; no interface-domain issues. Applied by erratum above.

## Parent checks and trust boundary

- IP: remove the even number |T|-2p of involutions if available; remaining2p zero-sum violates ZP. The corrected IP' standing hypotheses are met at both uses.
- DOM: CT at n=p-2 has |Y|-n=2kappa+2 and excess p-2e+4. Two heavy values exhaust the truncated bound; the residue j0 argument fails only at excluded kappa=p-1. One heavy generator gives the stated exact shifted constants.
- Few-sums core: n=p-2e+delta', |A|<=p-e+t and2n-(p-e+t)=p-3e+2delta'-t>=2. Maximal Z0 gives zero-sum-free U'. A term with coefficient1 makes Lev's a nonzero in C_p, hence orderp; actual occurrence subsums realize the integer interval because S<p.
- AP-double-prime: intersection size is max(0,l-d0)+max(0,l-p+d0); the two-piece case is<N by p>=3N+5. In the remaining case every nonzero shifted lift has absolute value>=l, forcing consecutive actual lifts to differ by x-tilde. Then N*d0<=2N+1, leaving only the stated N=1 exception.

The prior accepted verdicts record CT/ROW's classical Cauchy-Davenport imports and no computer-assisted premise for these interfaces; this is not a new exhaustive audit of every transitive proof body. Lev primary statement was parent-read in the earlier G-LS admission and is reused at its exact zero-sum-free/inclusive-few-sums scope, not re-proved.

## Delta and open boundary

This lowers the applicable sequence threshold by ONE at the stated high-kappa range; it does not prove a result at any length below p+2kappa or at kappa=p-1 (the displayed two-heavy counterexample remains). Accepted LS+2/linear/BASE1+ already cover the specified overlapping cells at their own Lev-free trust; new internal coverage is the remaining3<=e, p<10e-13 cells outside BASE1+, conditional on Lev. Search/primary-priority limits remain in notesv5/v6; no novelty or matchedSOTA claim. Word-level ASSEMBLY-P remains a separately reviewed candidate; after this verdict its ONE-SHORT premise can be discharged exactly here, while ROT-SING is still pending.
