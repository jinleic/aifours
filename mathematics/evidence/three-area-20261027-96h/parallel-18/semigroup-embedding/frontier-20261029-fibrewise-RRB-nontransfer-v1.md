# Globally right-regular fibres do not give a right-regular host over CS actors

**Status: NEW AUTHOR OBSERVATION combining a new exact check with an existing unreviewed obstruction; UNREVIEWED / UNADOPTED.** It explains why Szendrei's one-sided group-actor theorem cannot simply be applied fibrewise.

## 1. Statement

The 45-element source S45 of `frontier-20261028-all-cs-globally-regular-band-obstruction-v1.md` (SHA `2f9f6a68a153449b61cda78305174c5b601e28fba49ec391bc1107aaba8e31af`) has:

- every one of its 9 idempotent actor fibres a **globally** right regular band (`xyx=yx` for all fibre elements), and all local idempotent bands right regular;
- (from that existing record, conditional on its named Kimura and actor-transport inputs) **no** faithful physical host with a globally regular band, for any CS actor or action — hence none with a right regular band;
- a faithful host with the RIGHTSN, non-globally-regular band B5² (`frontier-20261028-ambiguous-source-local-host-checker-v1.py`).

## 2. Meaning

For a group actor, Szendrei's theorem (Semigroup Forum 32 (1985), Theorem 2.2, dual form; pages pinned in `frontier-20261029-szendrei-1985-public-scan-index-v2.json`, SHA `92eed241f971b13e338bf70d12cb4a13da2d2df35e02c17e3ab3566e37181b2b`) embeds an E-unitary orthodox semigroup with right regular band into a right-regular-band-by-group product. With a CS actor, the single band E(S) splits into fibres that are glued by twisted cross-fibre products, and S45 shows that globally right regular fibres can force a host band that is only LOCALLY right regular. So the CS-actor problem is genuinely about RIGHTSN (local) structure, matching the reduction in `frontier-20261029-Q1-reduction-state-v1.md` (SHA `231a862f484d1d304d7094319e98f715fa5f5442522d227a7a87ac0df9a66157`).

## 3. Check

`frontier-20261029-S45-RRB-fibres-checker-v1.py`, SHA `deb0ba28b0733b2b501f05f8f7d4a61b3e56d01772b5981864a36c29ba9eca9c`, completed in the Python kernel before ThuOct29 06:29:14 PDT2026: 45 elements, 24 idempotents, 9 fibres, each closed and globally right regular, all local bands right regular, and the same-fibre R-pair (1,1,1),(1,3,1). The nonexistence of a regular host is the earlier written argument, not this check.

Related breadth evidence for item4: `frontier-20261029-RRL-C3-rightSN-host-batch-v1.py` (SHA `6c0c47e4dad0b0708ffa8e987e6f2c8c48eaa3e883839a8d3080fb7eb84c69cb`) produced exactly rechecked RIGHTSN hosts (band sizes 3–7) for 60/60 RRL sources of sizes 12–60 with up to 18 local R-pairs inside `P(B012^1, M[C3;2,2;P])` (results file SHA `65f19cee4a6ee0d683cc2d64c5e22b23313494657b3c07afcc032d178efca55e`).
