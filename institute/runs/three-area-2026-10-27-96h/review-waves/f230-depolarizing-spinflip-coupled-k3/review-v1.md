# f230 status-only chronology and exposure receipt

**Status: STATUS ONLY; no mathematical review, adoption, or verdict.** After the f230 manifest was frozen and dispatched, the parent reported that an additive correction to the declared 186 comparator had been created. The parent instructed this reviewer to hold, then to close f230 with this receipt only. The correction was not opened, and this receipt does not claim it preceded 186. A separately frozen fresh reviewer will receive the correction before 186 and 190; this reviewer's work is not carried into that review.

Native clock observed before writing this receipt: `2026-10-29T14:02:55-0700 PDT`.

## Frozen inputs and actual display order

The assigned manifest `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f230-depolarizing-spinflip-coupled-k3/manifest-v1.json` measured SHA-256 `37ce2b8ccab7ab208e61272d40ebd1c34980df53b86b020ea370cc55ff2ff1b5`, matching the assignment. Before opening any declared input body, all four inputs were measured and matched all declared SHA-256, byte, and LF counts.

Actual complete raw-window display sequence, in manifest order:

1. Scope erratum, SHA-256 `c9b5632e8285298a6b8438842498fc5a35695a889efcee0245836c2cbf038db2`, 2,444 bytes, 27 LF: `1–15`, `16–27`.
2. f200 disposition, SHA-256 `bb16e861cedad17fc2a9eb9520dba4cb7bdbd69ad3cd510df2e7bd59060f8b54`, 4,873 bytes, 17 LF: `1–15`, `16–17`.
3. Declared unreviewed 186 comparator, SHA-256 `36aa530048387e244b27815e25fb93f38ad98366af37d839f047732dd9cba922`, 11,016 bytes, 167 LF: `1–15`, `16–30`, `31–45`, `46–60`, `61–75`, `76–90`, `91–105`, `106–120`, `121–135`, `136–150`, `151–165`, `166–167`.
4. Target 190, SHA-256 `ef8e08229d3a84ec7051de7d3f9fc2dce717b3d4f57bdb377086df20c5ac1d34`, 11,494 bytes, 211 LF: `1–15`, `16–30`, `31–45`, `46–60`, `61–75`, `76–90`, `91–105`, `106–120`, `121–135`, `136–150`, `151–165`, `166–180`, `181–195`, `196–210`, `211`.

Two read attempts for 190 failed without displaying source: the first attempt at `76–90` returned path-not-found, and the first final-line attempt used the malformed selector `:211:211:raw`. Each was followed by the successful window listed above; no declared input line was omitted. No newly reported correction or other new source was opened.

## Exposure and work frontier

I reached and interpreted 186 line 161, including its claimed product-overlap bound `≤5/6` from a one-site marginal and its comparison with the named near-product condition. I also considered the named-source comparisons in 186. This records exposure, not endorsement.

After all four declared input bodies had been completely displayed, and before receiving the parent hold, I independently reasoned about the 186 comparator optimization and the 190 identities, criterion, and example. I wrote a reviewer-owned exact-control script containing mathematical assertions. I did not write a mathematical review before the hold. The timing of the derivation itself was not separately clocked; its ordering relative to complete input display and control launch is as stated.

The script is `reviewer-exact-control-v1.py`, 10,526 bytes, SHA-256 `5d1b5d0907f0d5a1dd49b2b636fe00f24c5ebfa1a61c81ae2427ddc378e62edb`. It was launched before the interruption. Its actual `/bin/date` control start was `2026-10-29T14:01:57-0700 PDT`; actual end was `2026-10-29T14:01:58-0700 PDT`; measured exit was `0`. Upon my attempt to stop the background job after the hold, the tool reported that the job had already completed: execution was completed, not cancelled. Source and control bytes are preserved.

No conclusion from that derivation or control is presented as a review finding or carried forward. No human, independent-model-family, formal/kernel, or novelty verification is claimed.
