# Olson BASE2: standalone packing and low-defect exclusions

Recorded at 2026-10-19T09:05:56-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** P1 is an elementary standalone packing result. P2/P3 exclude configurations only in the exact threshold LS-counterexample setting; they do not prove the general BASE2 LS family S3.

## Governing text
[Proof](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/proof-S3-lowdefect-core-v1.md) `3847ade3f32e9d9edd11a7cbbd246b68b1a63c8e16beda796250d7c9d64c662a` read through [single erratum](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/erratum-1-S3-lowdefect-v1.md) `ae6096dd8bbd23dc970bace31a21488ae467781319f0e4abc3756e04b0c965f3`. Parent read both in full. No Lev, index-one, AP', greedy or I-small is a proof input in this package.

## Accepted statements
- **P1:** p=6m-1 prime, m>=3, h=2m-2. A sequence S of nonzero residues modulo p, |S|>=2m+3, with every nonempty occurrence subsum avoiding[0,h], has no occurrence submultiset of size>=3 and residue-1. This length-lower-bound statement is proved in-file, not imported from exact-length B2-1.
- **P2:** for a threshold BASE2 LS counterexample (p=6m-1 prime, m>=3, kappa=4m, odd Y of length14m satisfying ZP_4m and containing a zero-sum of length>=2p+2), with CF data at dominant g0, delta0!=2.
- **P3:** in the same setting, for EVERY inclusion-maximal mod-p zero-sum occurrence submultiset Z0<=U, possibly empty, delta'=delta0-|Z0|!=1. The nonempty-Z0 proof uses only F*/F', cardinality and the actual occurrence complement Z0-{z}. The empty case is the accepted restricted B2-1 (or in-file P1 plus restricted L1).

## Required scope/explicitness repairs
The erratum disposes all shared/editorial Claude findings: historical accepted L1/B2-1 status restricted to CFg0 threshold scope; d>=1 from CF(a), not dichotomy; full equality-use inventory of earlier B2-1(a)/(b)/(f); explicit x=1, lifted-pair, wrap, pair-window and least-representative steps; P2/P3 threshold quantifiers; no unused sigma'-symmetry premise in the nonempty-Z0 proof; d3 empty positive range; disjoint necessary residual below; general index-one inequality is orientation only, not exclusion.

## Verification
- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-S3-lowdefect-codex-v1.prompt.stdout.txt) `f5724e97b026f925239b4bab186fd19afa190c9d926c891f33dffd8d3ba2249b`: observed gpt-6.1-sol/max, all3 ACCEPT0F/0M/0m requiring repair.
- [Claude](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-S3-lowdefect-claude-v1.prompt.note.md) `55592d1d41c358e515373fcdf230e22c04ca230359005af499b8b65f57147d66`: observed claude-opus-5-5/max, no mathematical gap; editorial/shared/optional MINORs. Shared findings counted once, not summed per claim.
- Parent checks: length extension uses n+1>=2m+4 and n>=9 wherever earlier exact length mattered; all complement arguments are occurrence-disjoint including empty/full cases; the forbidden translated interval zeta+[1,h] covers the three stated residue regions; first crossing j+2S_j>=d has j>=2,1<=S_j<=d-2<h and no wrap. This is written verification, not a finite enumeration/smoke. Earlier accepted CF/DGM/dichotomy/LS-II'/L1 imports remain at their recorded boundaries.

## Residual and limits
Every possible threshold counterexample has3<=d<=2m-3. For every inclusion-maximal Z0 exactly one necessary alternative remains:
1. Z0 empty, delta'=d in[3,2m-3]; or
2. 2<=|Z0|<=d-2 and delta' in[2,d-2], requiring d>=4.
Neither alternative is asserted to exist or be empty. All general-m alternatives remain unresolved by this package; an index-one length inequality does not itself exclude them. Separate accepted LS(17,12)/LS(23,16) already close m3/4; p29 is the first still-open BASE2 prime. delta'=2 needs nonempty Z0 and d>=4. The later Lev-normalization candidate is a DIFFERENT unaccepted statement. No universal S3/LS/LS+/STAB, INV*, ordered Olson, novelty or matched-SOTA claim.
