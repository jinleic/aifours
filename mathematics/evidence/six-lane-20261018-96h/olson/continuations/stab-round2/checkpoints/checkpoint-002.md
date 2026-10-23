# Checkpoint 002 (Slice A, OlsonSTABSuccessor)

Written after /bin/date 2026-10-19T05:01:22-0700.  All items CANDIDATE [W], unreviewed; nothing assumed of LS/LS+/STAB.
- proof-CF-XT-v1.md aa602d45e154a7787ac3f0270a3c26deb5e8c6a70736cf4a82c700f5368c191f: Lemma CF (exact integer reformulation of (ZP_kappa), long zero-sums and LS/LS+ for
  ANY odd generator); Lemma XT (all <= 3-term (ZP_kappa)-extensions of E2(kappa-1), E3(kappa-1): only h, -h, -3h, h^2, h(-h), h^3;
  closes the handoff's open pairs); conditional Proposition STAB(kappa-1) + TR(kappa) => STAB(kappa) for kappa >= kappa0 + 2.
- note-STAB-range-v1.md 5b8faa3ab578c373e6fa01be32b10b476950f450f93a00580dd082366a630115: scout example 1^21 5^10 (Z_22) verified by hand; STAB false at kappa = p - 1;
  range kappa0 + 1 <= kappa <= p - 2 (as already frozen).
- proof-ROW-v1.md a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d: Lemma RS (rows + Cauchy-Davenport), Lemma DGM-p (proved from Cauchy-Davenport,
  DGM not imported), Theorem U (every (ZP_kappa) sequence has length <= 2p + kappa - 1, sharp by an (S1) example), Lemma ROW and the
  LS-threshold dichotomy (I) delta0 <= e - 2 / (II) one dominant value with >= p - 2e + 2 copies and <= e - 2 others.
- Exact obstruction now: in CF terms the long zero-sum must buy e - 1 (LS) / 2e - 2 (LS+) over Theorem U; sumset counting
  alone cannot (Theorem U is sharp for (S1) sequences).  The three-occurrence transversal TR remains unproved.
- Next bounded action: case (II) at the LS threshold via the AP-in-arc argument (two-value core plus <= e - 2 terms); then case (I).
