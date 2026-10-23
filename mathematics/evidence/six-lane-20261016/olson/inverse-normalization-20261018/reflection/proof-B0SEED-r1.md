# Theorem B0S-seed: under R >= 4 kappa + 1 one "seed" interval suffices (strengthens Theorem B0S++)

Owner OlsonReflectionRigidity.  Written after host clock 2026-10-18T06:38:59-0700.  Status: written proof [W], UNREVIEWED.
Builds on proof-B0SPP-r5.md (d388d391...bd64; Codex reviewed r4 ACCEPT-WITH-FIXES, r5 = errata): its Sec. 1 facts, Lemmas C1, C2
and Sec. 3 (B0S-r4 Secs. 3-5 with x_t := w_t) are used verbatim; only the hypothesis (D) of B0S++ and Lemma SIGMA-2P are replaced.
Scope: B = 0 only; no statement about rotation values, INV*(p), REFL(p) or ordered Olson.

## 0. Statement

Setting and notation of proof-B0SPP-r5.md: w of length 4p - 2, all rotations rho_1 (B = 0), all maximal blocks odd, kappa >= 1,
genuine empty runs allowed, g(E) = min(E - kappa, floor(E/2)), Delta := k - p - kappa - 1, and (H) R >= 4 kappa + 1.
**Definition (good step, seed).**  For a proper interval A and a run t adjacent to it, the step A -> A u {t} is GOOD if, with
s := m(A u {t}),  s >= 2 Delta - 1,  or  s = 2 Delta - 2 and R - r_t is even.
A SEED is a proper interval S of runs with (i) m(S) >= 2 Delta - 1, (ii) m([k] \ S) >= 4 Delta - 3, and (iii) an ordering of S as
S_1 = {s_0} c S_2 c ... c S_L = S (each S_(i+1) = S_i u {t_i} an interval) in which every step is good.
Examples: a single run of mass >= 2 Delta - 1 (L = 1); an adjacent pair of mass >= 2 Delta - 1; an adjacent pair {a, b} of mass
2 Delta - 2 with R - r_b even, followed by a run of mass >= 1 adjacent to it; in each case provided (ii).
**Theorem B0S-seed.**  If (H) holds and either Delta <= 0 or w has a seed, then w has an identity 2p-subword.
Theorem B0S++ is the special case in which (D) gives two disjoint heavy pairs: either pair {s, s+1} is then a seed, since (ii)
holds: the other pair lies outside it, and m([k] \ {s, s+1}) >= ... -- see Remark (1) for the comparison; B0S-seed needs only ONE
seed.

## 1. Two facts

**Lemma P (exact threshold).**  Let A be a proper interval, t a run adjacent to A, rest := [k] \ (A u {t}), and suppose
m(A) + m(rest) = R - r_t and m({t} u rest) = R - m(A) are both > 2 kappa.  Then (B') of Lemma C1(c) holds for the split
(A, {t}, rest) of A u {t} iff the step A -> A u {t} is good (or s > 2 kappa).
Proof.  The pair sums are s = m(A u {t}), R - m(A) and R - r_t; the last two are floor terms, so if s <= 2 kappa,
(B') = s - kappa + floor((R - s + r_t)/2) + floor((R - r_t)/2).  If R - r_t is even this is R - kappa + floor(s/2); if R - r_t is odd
it is R - kappa + floor(s/2) for odd s and R - kappa + s/2 - 1 for even s.  As R - kappa - 1 + Delta = p - 2, (B') >= p - 2 iff
floor(s/2) >= Delta - 1 (R - r_t even), resp. s >= 2 Delta - 1 (R - r_t odd): this is the definition of good.  If s > 2 kappa all
three are floor terms and (B') >= R - 1 >= p - 1.  []
**Lemma Sub.**  Under (H), if c(Y) = 0 for a proper interval Y, then c(Y') = 0 for every sub-interval Y' of Y.
Proof.  Write Y = L u Y' u M (consecutive, L or M possibly empty).  By Lemma C2(a) and C1(c), c(Y) >= c(L u Y') + c(M) >= c(L) + c(Y')
+ c(M) (omitting empty parts), and all terms are >= 0 (C2(c)).  So c(Y') <= c(Y) = 0.  []

## 2. Lemma SIGMA-SEED and the proof of the Theorem

**Lemma SIGMA-SEED.**  Under (H), if Delta <= 0 or w has a seed, then J = 0, i.e. the singleton representatives sum to p.
Proof.  Delta <= 0: Lemma SIGMA-2P of proof-B0SPP-r5.md.  Let S = [a, b] be a seed.  No run has mass > R - 2 Delta + 1
(proof-B0SPP-r5.md Sec. 1 and P0: otherwise the other runs carry <= 2 Delta - 2 letters and n_E >= p + 3 > 2 kappa), so for every run
t, m([k] \ {t}) >= 2 Delta - 1 > 2 kappa - ... more precisely R - r_t >= 2 Delta - 1, and R - r_t > 2 kappa unless r_t >= R - 2 kappa;
in all steps below the two non-light pair sums are > 2 kappa because they contain the complement of a set of mass <= m(Y) with Y
light or S-like, or contain S and an outer interval of mass >= 2 Delta - 1 (see (a)-(c)).
(a) c(S) = 0.  Along the ordering of S, each step S_i -> S_(i+1) is good, its rest is [k] \ S_(i+1), whose mass is >= m([k] \ S) >=
4 Delta - 3 >= 2 kappa + 1 - ... [mass condition checked: R - m(S_i) >= m([k] \ S) and R - r_(t_i) >= m([k] \ S); both are
>= 4 Delta - 3; if one of them is <= 2 kappa the triple has two light pair sums, impossible as any two pair sums add up to >= R >=
4 kappa + 1; so they are floor terms].  Lemma P gives (B'), Lemma C1(c) gives c(S_(i+1)) <= c(S_i) + c({t_i}) = c(S_i), so
c(S) <= c({s_0}) = 0, and c(S) = 0 by C2(c).
(b) The outer arc O := [b + 1, a - 1] has m(O) >= 4 Delta - 3.  Let x* be the last run of O (in the order b + 1, ..., a - 1) such
that m([x*, a - 1]) >= 2 Delta - 1 and x* <= a - 2 if |O| >= 2 (x* = b + 1 if |O| = 1).  Then m([x* + 2, a - 1]) <= 2 Delta - 2
(empty if x* = a - 2), hence m([b + 1, x* + 1]) >= m(O) - (2 Delta - 2) >= 2 Delta - 1.
(c) Y1 := [a, x*] (S followed by b + 1, ..., x*) and Y2 := [x* + 1, b] (a - 1, a - 2, ..., x* + 1 followed by S).  Grow Y1 from S by
adding b + 1, ..., x* in turn: when i is added the three pair sums are m([a, i]) >= m(S) >= 2 Delta - 1, m([i, a - 1]) >=
m([x*, a - 1]) >= 2 Delta - 1 and R - r_i >= 2 Delta - 1, and at most one of them is <= 2 kappa; by Lemma C2(b) (B') holds, so
c(Y1) <= c(S) = 0, i.e. c(Y1) = 0.  Grow Y2 from S by adding a - 1, ..., x* + 1: the pair sums are m([i, b]) >= m(S),
m([b + 1, i]) >= m([b + 1, x* + 1]) >= 2 Delta - 1 and R - r_i; so c(Y2) = 0.
(d) Y1 u Y2 = [k], so Y1^c = [x* + 1, a - 1] is a sub-interval of Y2 and c(Y1^c) = 0 by Lemma Sub.  Lemma C1(b):
J = c(Y1) + c(Y1^c) = 0.  []
**Proof of Theorem B0S-seed.**  Suppose w avoids.  By SIGMA-SEED, x_t := w_t satisfy sum x_t = p; proof-B0SPP-r5.md Sec. 3 (which
uses only this, the singleton gaps and (H)) yields a killing pattern: contradiction.  []

## 3. Remarks

(1) B0S++ assumed two disjoint adjacent pairs of mass >= 2 Delta - 1; B0S-seed needs one seed, e.g. one such pair whose outside
mass is >= 4 Delta - 3 (always true when the other heavy pair is disjoint from it?  not needed: the outside-mass condition is
checked directly), or a parity-good pair of mass 2 Delta - 2 with a nonempty neighbour, or a single run of mass >= 2 Delta - 1.
Example now covered, not covered by B0S++: p = 13, kappa = 3, k = 19, R = 13 (all nonempty runs of mass 1, six empty runs): any
three consecutive runs rho_1 form a seed ({a, b} has mass 2 = 2 Delta - 2 with R - 1 even, then a mass-1 neighbour gives 3), and
three consecutive nonempty runs exist because 13 runs rho_1 lie in at most 6 blocks between the empty runs.
(2) Still open in regime (H): seedless words (Delta >= 2, no run or adjacent pair of mass >= 2 Delta - 1, and no parity-good pair
of mass 2 Delta - 2 that extends), and words whose only seeds leave outside mass < 4 Delta - 3.  Seedless words exist, e.g.
p = 17, kappa = 4, k = 24, R = 18 with eighteen runs rho_1 and six empty runs: every adjacent pair has mass <= 2 = 2 Delta - 2 and
R - 1 is odd.  And regime R <= 4 kappa remains open.
