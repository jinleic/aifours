# Checkpoint 015: coordinated errata round (import / KPS v4 / SLZ-EXT v2) frozen; STAB status

Owner ContinueOlson.  Written after /bin/date 2026-10-19T03:47:52-0700.  Continues checkpoint 014 (2f195a55961c33f8a43e1d759e3b78d17c17ac800c7e22d9fca5f941b816d763).

## Actual result since 014
- Errata answering Codex (0/0/3) and Claude (0/0/8 + 2 editorial) on the KPS/SLZ packet, one file per source:
  evidence/import-Sp-XiaYuan-v1-erratum-1.md df1c5ac2dba4f088b6aa402a1e1c1e9037063230a37776d8f50b704997c87269 (n-range at the secondary-statement trust level per Peng-Sun
  Thm 1.2-1.3 as read by the parent; exhaustiveness/definition trust items; SPLIT nonzero terms; Claim P without l = 0);
  evidence/proof-KPS-v4-erratum-1-v2.md 3ef936f19d2dc9eabadc8684ea842e19a92df2534fb582b11bb302b8375aa80b (proviso; SHgen v3 L39-42 definitions of eta (both signs) and
  a_max with the eta >= 2 derivation; caller scopes k <= p - 1 vs k = p; editorial O-2..O-4);
  evidence/proof-SLZ-EXT-v2-erratum-1.md 907b3d06dd2ac93686ea4f49cf812dfd41f80f9abdefa6fd2d4398821c234daa (t0 <= p - 1 in the FB instantiation; kappa = 0 by Davenport;
  notation; RED shrink step).  No statement or strategy changed.
- STAB (inverse statement at length 3kappa + 1; implies LS+ by the frozen addendum): worked, not frozen:
  * one-term extensions of E2(kappa - 1) that keep (ZP_kappa): y = c h with c <= 2p - 5 creates a level-4p window zero-sum
    (interval arithmetic as in Lemma MAX); y = -h is admissible once, a second -h creates h^(2p-3e-1) (3h)^(e+1) (-h)^2 of
    length 2kappa + 2; so the induction STAB(kappa - 1) => STAB(kappa) needs a finite but nontrivial classification of
    three-term extensions, plus the existence of three terms meeting every 2kappa-zero-sum while keeping a long zero-sum
    (not available in general).

## Exact blocker
STAB / LS+ beyond the partials: the three-term removal step of the induction, and the classification of (ZP_kappa)
three-term extensions of E2(kappa - 1), E3(kappa - 1).

## Pending with the parent
Verdicts on KPS v4 + import + SLZ-EXT (with this errata round); SLZ3 reviews; LS+ partials (v2 + addendum MAX v2) when
the parent decides.
