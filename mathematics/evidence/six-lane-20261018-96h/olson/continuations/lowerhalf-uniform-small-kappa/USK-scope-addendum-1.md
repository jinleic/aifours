# Addendum 1 to USK-scope-v1.md: Main IRC (K3 accepted context; input hygiene), recorded before the proof text

Owner OlsonUniformSmallKappa. Written after /bin/date 2026-10-20T00:40:01-0700. Read after the immutable USK-scope-v1.md (SHA256
fabc84fbe78dc978cb7164da1ecd34ed62925f3c2c178984b1669dac1eeec17e, frozen 2026-10-20T00:25:01-0700). The exact target, the full
antecedent, write rules, claim limits and non-goals are UNCHANGED. No proof text had been written when the IRC arrived
(only checkpoints/checkpoint-001.md, 00:39:24).

1. Added accepted CONTEXT (not a premise): K3 verdict RUN/review/olson-K3-parent-verdict-v1.md SHA256
   9281cbc64bd2bc59edf7a8404481765d5d5d39c351ce5b2b28c35b6e6e03a9f6 (recorded 2026-10-20T00:34:09-0700: kappa_hat=3 excluded
   for every prime p>=13; p=11 only conditionally) with governing erratum RUN/review/olson-K3-parent-erratum-v1.md SHA256
   8653cb3e183a6c8d21e95e971de95b598a5a29cb94e90bb69de6173623c332af. The kappa=3 sub-case of the target is re-proved here by
   the uniform argument; K3 lemmas are not imported.
2. Input hygiene (narrows the frozen input list; nothing added as a premise):
   - S1(a) is NOT used. Every zero-sum of the sequence Y at the zero-target arc has even length <= |Y| = R <= 2p-2, and
     (SR) at that arc (m=1, window [2kappa,R]) excludes every even length from 2kappa through R; so a longest zero-sum has
     length 2t <= 2kappa-2. This is proved at the exact range 3<=kappa<=floor((p-1)/4) (it needs only R<2p).
   - The Setting fact (m-slack>=3), Corollary FB-E and Theorem P are NOT used. Where PL's Lemma D needs every label to be
     at most (number of 1-labels)+1, the s-labels are bounded by ZSTRUCT (s_j <= 2t-1 <= 2kappa-3) and the a-labels and the
     number of 1-labels by direct counts from SC0/FB (W + n+ <= 2p-1, L >= p+1), all written out in the proof.
   - Every general-kappa prerequisite of PL Secs. 2, 4-7 that the proof uses is restated with its exact hypotheses at this
     range; frame quantifier: the argument runs in ANY admissible frame (zero-target arc P0, longest zero-sum Z, index-<1
     generator g, light-side choice), and such a frame always exists.
3. P11R remains unreviewed and is not used; proof-P11R-v1.md has not been read.
