# Notes (unreviewed, NOT a claim): the k = p case under ROT-ZB's tools; exact remaining obstruction

Owner ContinueOlson.  Written after /bin/date 2026-10-19T00:47:25-0700.  Uses only candidate proof-ROT-ZB-v2.md (65dbedbf...f5f1, unreviewed)
and accepted inputs; nothing here is submitted for acceptance.

Observation K-P1.  Let w^ have terminal k = p, 2 <= kappa^ <= min((p+7)/4, p/2), and suppose the rotation sequence Y has
a longest zero-sum Z with |Z| = 2t < 2kappa^.  Then L = |Y - Z| = p + 2kappa^ - 2t >= p + 2, so SC0/REALIZE/ZSTRUCT apply;
Lemma BAL1 gives balance when L + n+ >= 4t - 1, which holds since p + 2kappa^ + 1 >= 6(kappa^ - 1) iff 4kappa^ <= p + 7;
Lemma ROOM (2kappa^ + p <= 2p) gives E <= p - 1 - 2kappa^ + n+ <= p - 1 - 2kappa^ + 2t <= p - 3; KETA then gives
eta + a_max <= p - 1, i.e. SHgen's (K) at k = p; (H) holds as 2H = 2p - 2 - 2kappa^ >= p - 1 - 2kappa^ + n+.  With
SHgen/SHgen-E (restricted REFL at o_F <= p) the rotations lie in one nonzero pair.
Exact remaining obstruction at k = p (for these kappa^): the case t = kappa^, where Y - Z has length exactly p and the
Savchev-Chen-type structure S(p) (notes-SC-lengthp-v2, open) is not available; and kappa^ > (p+7)/4.
