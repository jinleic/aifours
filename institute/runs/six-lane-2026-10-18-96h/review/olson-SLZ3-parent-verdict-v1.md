# Ordered Olson sequence work: shortest-long zero-sum bound accepted

Recorded at 2026-10-19T04:01:41-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIAL.** Let p>=5 be prime and floor(2p/3)+1<=kappa<=p-1. For an odd-element sequence Y overC_(2p) with nozero-sum subsequence of length[2kappa+2,2p], every shortest zero-sum T with |T|>=2kappa+2 satisfies **|T|<=3kappa+1**. Equivalently, any zero-sum sequence with these hypotheses and length>=3kappa+2 has a proper longzero-sum.

- [Candidate](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-SLZ3-v1.md) `0cfe637f919bdaab937f8292fa527d7fbd54e3af7d55bb07ddf137c0ad263c1c`; [mandatory overlay](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-SLZ3-v1-erratum-1.md) `483d9d1b70a895215a68654d329b73d8d8ab5221382fda290a933a937f5dda59`. All eleven Claude minors and two Codex minors addressed; p5 justification repaired, upperkappa bound explicit, inherited steps use the S1-sharp overlay, and length symbols/scope are unambiguous.
- [Codex](olson-SLZ3-codex-v1.prompt.stdout.txt) `29820717a8852727a15e76a4b794f61e75f94c77a92be1be865055c899fc9d49`: ACCEPT-WITH-MINOR-FIX0/0/2.
- [Claude](olson-SLZ3-claude-v1.prompt.note.md) `3579005a33ea332f2b197defd2ff75971c58ac801c417e258cf0b57253b8e0ec`: ACCEPT-WITH-FIXES0/0/11minor, no gap.
- Parent independently re-derived induction, exact2kappa properzero-sum extraction, range-sensitive Steps6-7 usingdelta<=p-2, the Step9 integerbase>=4, and F1 sharpness arithmetic before review; read complete overlay afterward.

## Mandatory comparison boundary
The earlier accepted SLZ statement in proof-SLZ-EXT-v2 has0<=kappa<=p-2. Therefore comparison with that accepted theorem is asserted **only on the common range floor(2p/3)+1<=kappa<=p-2**. Numerically3kappa+1<p+2kappa+1 wheneverkappa<p; at kappa=p-1 this result is still accepted but no prior-SLZ coverage is inferred. This qualifies the candidate's broad comparison wording.

F1 attains3kappa+1 whenp=1mod3 andkappa=(2p+1)/3. Forp=2mod3 at the first admissiblekappa, evenness rounds to2p+2=3kappa, attained byF1. No pointwise sharpness elsewhere, no strongerreferee observation adopted.

This bounds |T|, **not |Y|**. LS, LS+, STAB, INV* and unrestricted orderedOlson remain open. Proof is relative to acceptedS1-sharp/S1+ and the recorded classicalindex-one import; written/model-reviewed only, no Lean/humanreview/novelty clearance. The Zeng-Yuan overlap remains explicitly credited.
