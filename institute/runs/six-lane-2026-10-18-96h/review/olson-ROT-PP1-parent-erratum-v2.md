# ROT-PP1 parent notation and route-diagnostic erratum v2

Recorded at 2026-10-19T12:31:12-0700. Read after immutable proof `99143ea503a01a6376bed91a2a7ca8b91591617351f35ce4864117bf2949f1ca`, obstruction `4839cbd37d178038747a07e6c603ba344718d1c4c74508cfc7229aae417528dc` and parenterratumv1 `7f192a89e50ab349a37999669d0e1d411034f626730fac6118c0a546b886e479`. Disposes Codex `7fda7f0bcc77c01a6adaabac658947ba4f1bd17db852ce25e1b17aebd9758525`: mainVAC/M/P/U/TOPandNSfactsaccepted;0F/0M, fourMINOR plusoneMINORsource-limitation. No main theorem or top-cell proof changes. Each Old span occurs once.

## m1 subset notation

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/assembly-p/proof-ROT-PP1-v2.md

Old:
````text
For I in {1, ..., p-1} put
````

New:
````text
For I contained in {1, ..., p-1} put
````

## m2 CT diagnostic

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/assembly-p/obstruction-ROT-PP1-v2.md

Old:
````text
     - Step 3 (b <= p-1 from CT with n = p-3) is proved only for e = 2.
````

New:
````text
     - CT at n = p-3 remains admissible throughout the P/U range because R-(p-3)=2kappa^+2. The top-cell proof only stated b<=p-1 there; this is not a failed CT hypothesis. The supplementary argument below extends that estimate (still a candidate observation in this corrected review).
````

## m3 possible inputs, not mathematical minimality

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/assembly-p/obstruction-ROT-PP1-v2.md

Old:
````text
       this follows from b <= p-1 for every delta >= 1, but for e >= 3 it needs delta >= e-1 even granting b <= p-1.
````

New:
````text
       this follows from b <= p-1 for every delta >= 1; for e >= 3, delta >= e-1 suffices uniformly given b<=p-1, but is not necessary for each particular b.
````

## m3 heavy-run condition remains

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/assembly-p/obstruction-ROT-PP1-v2.md

Old:
````text
     Smallest missing lemmas for this route: (L1) a replacement for Step 6 when 1 <= delta <= e-2; (L2) a statement on
````

New:
````text
     Possible additional inputs for this route (no necessity, completeness or minimality claim): a proof or replacement of the separate heavy-run condition b+delta>2e-5; (L1) a replacement for Step 6 when 1<=delta<=e-2; (L2) a statement on
````

## m4 selectable-subset qualification

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/assembly-p/obstruction-ROT-PP1-v2.md

Old:
````text
       tau_i + 2a{1, ..., e} from an empty run R_i; their union has at most 2e-1 elements, so counting alone gives no
       contradiction.
````

New:
````text
       tau_i + 2a{1, ..., e} from an empty run R_i, only at lengths for which EVERY J in B is selectable (b<=n<=A). In general avoidance excludes only the sums over J with |J|<=n and n-|J|<=A, and CD gives |M|<=max(0,p-1-b). The stated coarse cardinality estimates give no uniform contradiction; this is not an impossibility claim about refined set structure.
````

## m5 unsupplied FLEXa interface

Source: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/assembly-p/obstruction-ROT-PP1-v2.md

Old:
````text
- (F2) Expansion to the kappa^ = p-1 cell (replace a heavy of weight 3 by three copies and delete one pair from the triple
  block, as in SHgen's u°(h)): the accepted Lemma FLEXa is stated in SHgen's setting (nonempty runs, condition (K)), and the
  target cell k = p+1, kappa^ = p-1 is not accepted; not used.
````

New:
````text
- (F2) A formal expansion to the kappa^=p-1 cell was considered (R+2,F-2 preserves length). No complete mutation-preservation interface or proof was supplied for this use, so it was not used; no full FLEXa hypothesis audit or endpoint approval is asserted.
````

## Supplementary CT estimate for the diagnostic range (CANDIDATE, not a new accepted theorem)

At k=p+1 and (p-1)/2<=kappa^<=p-2, CT at n=p-3 has R-(p-3)=2kappa^+2 in its window and capped sum<=2p-5. LemmaU gives delta<=p-2. Arrange A>=A'. If A<=p-3, then A'<=p-3, and capping the deviant total delta at p-3 loses at mostone occurrence, so capped sum>=R-1>=2p-3, contradiction. Thus a contributesp-3. ZP forbids2p equal copies and forbids a^(p-1)(-a)^(p-1), so A<=2p-1,A'<=p-2; every deviant multiplicity<=delta<=p-2. The remaining capped-count argument gives b<=p-1. This is the exact extension proposed by Codex and hand-checked by the parent; the corrected second-family packet must assess it independently. It does not prove rigidity at lower kappa.
