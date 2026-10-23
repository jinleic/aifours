# Row lemma, the multiplicity lemma DGM-p, a universal (ZP_kappa) length bound, and two structural dichotomies, v1

Owner OlsonSTABSuccessor (Slice A).  Written after /bin/date 2026-10-19T04:53:25-0700.  Status: CANDIDATE, written proofs [W], UNREVIEWED.
Uses Lemma CF of proof-CF-XT-v1.md (aa602d45e154a7787ac3f0270a3c26deb5e8c6a70736cf4a82c700f5368c191f) and one classical import: the Cauchy-Davenport theorem
(|A + B| >= min(p, |A| + |B| - 1) for nonempty A, B in Z_p, p prime).  Nothing else; LS, LS+, STAB not assumed.  The
multiplicity lemma below is the prime-order special case of the DeVos-Goddyn-Mohar bound suggested by the parent's scout
(run review/olson-priority-parent-note-v2.md); it is proved here from Cauchy-Davenport, so DGM itself is NOT imported.
No novelty claim (statements of this type are standard in zero-sum theory); no Lean.

## 0. Notation
As in proof-CF-XT-v1.md: p >= 5 prime, e := p - kappa, (ZP_kappa), long, CF data (delta0, U) of a sequence Y w.r.t. an odd
generator g; r := |U|; rho(W) := sigma(W) mod p.  For a sequence S over Z_p, v_x(S) is the multiplicity of x; Sigma_n(S) is
the set of sums of n-term subsequences; Sigma_(<=K)(S) the set of sums of subsequences with at most K terms (the empty sum 0
included).  Subsequences are occurrence subsequences.

## 1. Lemma RS (rows)
Let S be a sequence over Z_p.
(a) If 1 <= n <= |S|, then |Sigma_n(S)| >= min(p, sum_x min(n, v_x(S)) - n + 1).
(b) If all terms of S are nonzero and K >= 0, then |Sigma_(<=K)(S)| >= min(p, 1 + sum_x min(K, v_x(S))).
Proof.  List the T := sum_x min(n, v_x) chosen occurrences value by value (min(n, v_x) occurrences of each value x) and put
the k-th listed occurrence into row (k mod n) + 1.  The occurrences of one value are consecutive and at most n, so each row
A_i is a SET of values; in (a) T >= min(n, |S|) = n, so every row is nonempty.  Choosing one element from each row selects n
distinct occurrences, so A_1 + ... + A_n <= Sigma_n(S), and iterated Cauchy-Davenport gives |A_1 + ... + A_n| >=
min(p, sum |A_i| - (n - 1)) = min(p, T - n + 1).  (b) Same with n := K rows (K = 0 trivial) and B_i := A_i u {0}
(possibly A_i empty): choosing at most one element per row gives a subsequence of at most K terms, so
B_1 + ... + B_K <= Sigma_(<=K)(S) and |B_1 + ... + B_K| >= min(p, sum(|A_i| + 1) - K + 1) = min(p, 1 + sum_x min(K, v_x)).
(0 is not a term, so |B_i| = |A_i| + 1.)  []

## 2. Lemma DGM-p (one dominant generator)
Let p >= 5 prime, (p - 3)/2 <= kappa <= p - 1, and let Y be an odd sequence over C_(2p) with (ZP_kappa) and |Y| >= p + 2kappa + 1.
Then exactly one element g0 of Y has multiplicity >= 2kappa + 3; g0 is a generator; and |Y| - v_(g0)(Y) <= p - 2.
Proof.  Write the odd elements as (1, a) in C_2 x C_p and let A be the sequence of C_p-coordinates.  A subsequence of exactly
2kappa + 2 <= 2p terms is a zero-sum iff its C_p-coordinates sum to 0; (ZP_kappa) excludes this, so 0 is not in
Sigma_(2kappa+2)(A) and Lemma RS(a) gives sum_x min(2kappa + 2, v_x) <= p + 2kappa < |Y| = sum_x v_x.  So some value x0 has
v_(x0) >= 2kappa + 3, and then sum_(x != x0) min(2kappa + 2, v_x) <= p - 2 < 2kappa + 2 (kappa >= (p - 3)/2); hence every other
value has v_x <= p - 2 (so min = v_x and the others total <= p - 2), and x0 is unique.  If x0 were the involution (1, 0) = p,
x0^(2kappa+2) would be a zero-sum of length 2kappa + 2.  So x0 is a generator.  []

## 3. Theorem U (universal length bound for (ZP_kappa))
Let p >= 5 prime and (p - 3)/2 <= kappa <= p - 1.  Every odd sequence Y over C_(2p) with (ZP_kappa) has |Y| <= 2p + kappa - 1.
The bound is attained by g^(2p-1) (-g)^kappa (g any odd generator), a sequence satisfying (ZP_kappa) AND (S1_kappa).
Proof.  If |Y| <= p + 2kappa we are done (kappa <= p - 1).  Otherwise take g := g0 of Lemma DGM-p and its CF data: M = v_g >= 2kappa + 3,
delta0 = 2p - M >= 1, r = |Y| - M <= p - 2.  If r < delta0 then |Y| < 2p.  Otherwise choose W0 <= U with |W0| = delta0 and
put V := U - W0.  For every V' <= V, W := W0 V' has delta0 <= |W| <= |W| + 2rho(W) <= r + 2e - 2 <= 2p (e <= (p + 3)/2), so by
CF (F) rho(W) is not in [0, e - 1]: the set Sigma_(<=|V|)(V) (all subset sums of V, 0 included) avoids the e residues
-sigma(W0) + [0, e - 1].  By Lemma RS(b) with K := |V| it has at least min(p, |V| + 1) elements; so |V| + 1 <= p - e, i.e.
r <= delta0 + p - e - 1 and |Y| = 2p - delta0 + r <= 3p - e - 1 = 2p + kappa - 1.
Example: with g, the zero-sums of g^i (-g)^j (i <= 2p - 1, j <= kappa) need i = j (mod 2p), so i = j and the length is
2j <= 2kappa.  []
(At kappa = p - 1 this is the classical s_(2p)(C_p) - 1 = 3p - 2; at kappa = 0 it is D(C_(2p)) - 1.)
Use for LS: LS(p, kappa) asks for |Y| <= p + 2kappa = (2p + kappa - 1) - (e - 1) under the extra long zero-sum; LS+ asks for
(2p + kappa - 1) - (2e - 2).  So the long zero-sum must be worth e - 1 (LS) resp. 2e - 2 (LS+) terms; a pure counting bound
that does not use the long zero-sum cannot prove either (it is attained by the (S1) example above).

## 4. Lemma ROW (the large-subset constraint) and the dichotomies
Lemma ROW.  Let Y satisfy (ZP_kappa), g an odd generator with CF data (delta0, U), r >= delta0 and r + 2e - 2 <= 2p.  Put
K := r - delta0.  Then sum_x min(K, v_x(U)) <= p - e - 1.
Proof.  Every W <= U with |W| >= delta0 has delta0 <= |W| + 2rho(W) <= 2p, so rho(W) is not in [0, e - 1] (CF (F)).  Writing
W = U - X, |X| <= K, this says: Sigma_(<=K)(U) avoids the e residues sigma(U) - [0, e - 1].  Lemma RS(b).  []
Dichotomy at the LS threshold.  Let floor(2p/3) + 1 <= kappa <= p - 2 and let Y be a counterexample to LS of length exactly
thr := p + 2kappa + 1 (accepted RED: LS fails iff such Y exists).  With g := g0 (DGM-p): M >= 2kappa + 3, so delta0 <= 2e - 3,
r = p - 2e + 1 + delta0 <= p - 2, and K = p - 2e + 1.  Then either
  (I) every value of U has multiplicity <= K, and then r <= p - e - 1, i.e. delta0 <= e - 2 (M >= p + kappa + 2); or
  (II) exactly one value mu1 has multiplicity v1 >= K + 1 = p - 2e + 2, and the other terms of U number at most e - 2.
(Two values above K would give 2K <= p - e - 1, i.e. p <= 3e - 3, false; in (II) the others then have v_x <= K, so their
total is <= p - e - 1 - K = e - 2.)
Dichotomy at length 3kappa + 2 (LS+).  Let |Y| = 3kappa + 2 with (ZP_kappa), and let g be a generator with M = v_g >= p - e
(so r + 2e - 2 <= 2p).  Then K = p - 3e + 2 and either (I+) every value of U has multiplicity <= K and delta0 <= 2e - 3
(M >= 2kappa + 3), or (II+) some value of U has multiplicity >= p - 3e + 3 (and sum_x min(K, v_x) <= p - e - 1).
No generator with M >= p - e is guaranteed at length 3kappa + 2 by the results above (DGM-p needs |Y| >= p + 2kappa + 1).

## 5. Exact status
Nothing here proves LS, LS+ or STAB.  The lemmas reduce an LS counterexample to the two structured cases (I), (II); they
are recorded because they are the first places where the long zero-sum condition (L) of CF must enter.
