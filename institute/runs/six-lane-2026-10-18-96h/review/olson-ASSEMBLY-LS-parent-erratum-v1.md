# ASSEMBLY-LS: parent residual-wording erratum v1

Recorded at 2026-10-19T10:28:09-0700. Applies after proof-ASSEMBLY-LS-v2.md, SHA256 ac854c31ae1446c4710f3c19bb1beb80d8c25333aeb6b350c7f7d4dc7fafcfb3. Original proof, package and manifest remain unchanged. Main statements and proof Sections3-5 do not change. This disposes the two residual-commentary MINOR findings of Codex review 1c16c90f23db55c0ce6e0159b6ebdb7666178b2d6dc04f5443f138ae73331df9; it does not grant parent mathematical acceptance. Full second-family review is pending.

## E1: proof lines225-226, distinguish sufficient hypotheses

Old:
````text
Exact blocking hypothesis: (S1) at kappa^ for |Y| = p+2kappa^ (the
  ROT-KP+ / ROT-FB(b) input at k = p).
````

New:
````text
Exact blocking hypothesis: (S1) at kappa^ for |Y| = p+2kappa^ (the
  missing ROT-KP+ hypothesis at k = p; ROT-FB(b) supplies a stronger sufficient condition).
````

## E2: proof lines242-245, failure of a bound is not impossibility

Old:
````text
For k >= p+1: |Y| = 2p+2kappa^-k <= p+2kappa^-1 (below every LS
  threshold); ROT-FB's setting fails (L >= 2p-k no longer gives L >= p+1, so SC0/index-one is unavailable); and the SHgen-E
  caller would need REFL for o_F up to k >= p+1, outside restricted REFL. Missing inputs: a sequence lemma for zero-sum-free
  complements of length <= p, and REFL beyond o_F <= p.
````

New:
````text
For k >= p+1: |Y| = 2p+2kappa^-k <= p+2kappa^-1 (below every LS
  threshold); ROT-FB(a) is outside its stated k-domain. The bound L >= 2p-k no longer guarantees L >= p+1, and the
  SHgen-E bound o_F(u°) <= k no longer automatically discharges restricted REFL. These are obstacles to this uniform
  route, not proof that every particular complement has length <= p or every base word has o_F > p. A uniform extension
  would need to establish those caller hypotheses by another argument or supply suitable replacement lemmas.
````

Each Old span was independently checked to occur exactly once in the immutable proof. These are descriptive residual-map corrections only. No LS at a shorter length, no o_F>=p theorem and no individual-complement obstruction is accepted here.
