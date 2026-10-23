# Checkpoint 010: SLZ/EXT candidate frozen; LS reduced to its threshold length; base case analysis in progress

Owner ContinueOlson.  Written after /bin/date 2026-10-19T02:46:30-0700.  Continues checkpoint 009 (f28423a6...cc4b).

## Actual result
- CANDIDATE (unreviewed): evidence/proof-SLZ-EXT-v2.md 2495300317299fda49c0fb7d4b22daa81dfcecf1aef8c161361b9c04861bd751
  (Lemma SLZ, Lemma EXT, Corollaries PROP, RED; conditional consequence: LS for all kappa <= p-2 => INV*/ordered Olson for
  all o_F <= p-1).  Bundle v3: evidence/lane-summary-bundle-v3.md 2bddecc5...cd4c.
- Probe v12 (aid): (ZP)-and-not-(S1) multisets reach length p + 2kappa - 1 at p = 11, kappa = 9 (g^18(3g)^10, g^21(15g)^7),
  with no single term in all long zero-sums; so the threshold of LS is within 2 of sharp and 'common element' arguments
  cannot close the base case in general.

## Exact blocker (LS base case, length thr = p + 2kappa + 1)
By induction on kappa (base: S1-sharp) a counterexample Y contains a zero-sum Z of length exactly 2kappa, with complement C
of length p + 1.  Worked out (not yet frozen): if for some term z, Y - z satisfies (S1) with a 2kappa-zero-sum Z' whose
complement in Y is zero-sum-free, then Lemma FB-p (KPS-cond) plus the EXT descent at L = p closes the case (the EXT bounds
sum (s_i - 1) <= 2p - 2 - 2kappa and c + A(H) + |H| <= 2p + 2kappa + 1 still hold at L = p), except the rho_c/rho_0 family (X).
Open: (a) every complement of a 2kappa-zero-sum contains a zero-sum (each of length >= 2p + 2 - 2kappa); (b) every Y - d
fails (S1) and no Y - d has the boundary shape.

## Next bounded action
Write the boundary-case lemma (EXT at L = p) as a candidate addendum; analyse case (a) (complement C of length p + 1 with a
zero-sum) and the structure Z = g^(n+) N B for C zero-sum-free; keep LS unpromoted.
