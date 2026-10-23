# REFL(p) for kappa >= 1: reduction to the all-odd pure-run class RES_<(p)

Owner OlsonReflectionRigidity.  Written after host clock 2026-10-18T03:08:56-0700.  Status: written proofs [W], UNREVIEWED.
Notation, G-words, Lemmas H0, SPEC, FUS, SL, TR, PM0, BC', CH, facts (Z0), (Pairs), (V), (P0), (Par) and Theorem K0*: proof-K0star-r1.md
(sha256 99a8f2e0403877bb571b66134be3889e9d606d4da16c9040b6bf0407edb69488, this directory).  p >= 5 prime; words have length
4p - 2 and rotation letters in {rho_1, rho_-1} (normalised x = 1); "avoider" = no identity 2p-subword in increasing index
order.  Nothing here concerns rotation values (rotation slice), INV*(p) as a whole, or ordered Olson.

## 0. Imports and their exact status

* GRX (rotation/notes-GRX-v1.md, afc6c31a...0a30) and PM* (rotation/proof-ROT-lowodd-v1.md Sec. 1, 8ba3e6c7...f9785):
  parent CORRECTNESS-ACCEPTED for every cyclic constant-block representation with empty rotation gaps
  (R/olson-rotation-lowodd-parent-verdict-v2.md, 0853f4ac...ba29).  With rotations in {rho_1, rho_-1}, GRX is Lemma GR0 of
  proof-K0star-r1.md Sec. 1 (its "Specialisations" paragraph), and PM* is Lemma PM0.  So GR0 and PM0 are now accepted imports;
  H0 is the algebra of proof-K0star-r1.md Sec. 1 on top of GR0 (unreviewed, but it is the computation of the reviewed Lemma H of
  inverse-parity/proof-PAR-K0.md L32-44, which never uses r_i >= 1).
* RGR results, parent CORRECTNESS-ACCEPTED (R/olson-runs-parent-verdict-v1.md, 82adbddd...9237; R/olson-par-mixlow-parent-
  verdict.md), used ONLY on genuine RGR words (no empty run), each at its stated scope:
  (I1) Corollary B'(b) of R/olson-runs-assembly-proof-v4.md L160-164: every RGR word of length 4p - 2 with F, R >= 1, A >= B and
       1 <= B < kappa is solvable (any k, any reflection parities, no inherited hypothesis).
  (I2) B = 0 < kappa: Lemma OR (inverse-parity/proof-PAR-Kplus-partial-r2.md L24-35), then for the all-odd merged word Theorem
       C0-B' (inverse-run-count/proof-RUNS.md L318-320: ANY RGR word, all rotations rho_1, all reflection runs odd, R <= 2p - 2,
       kappa >= 1, no inherited hypothesis), Lemma A1 (same file L348-350: R = 2p - 1) and the trivial cut (L364: A >= 2p).  These
       are the B^ = 0 exit of v4 Theorem B and branch C1 of v4 Theorem C (both inside the accepted assembly; the verdict's
       "NMH and MIX_DEF_HIGH" paragraph re-derives exactly this exit).  Consequence used: an RGR avoider with B = 0 has kappa = 0.
  (I3) Theorem K0 (inverse-parity/proof-PAR-K0.md L94-96, Codex ACCEPT, accepted with Theorem P) for k <= p, and for k >= p + 1
       branch C2 of v4 Theorem C (the verdict's "RUNS coverage" paragraph: K0's uses of k <= p are replaced by R >= 5 and
       o_F <= p, which hold for every RGR word with kappa = 0 since R = 2p - o_F >= k >= o_F).  Consequence used: an RGR avoider
       with kappa = 0 has all runs odd.
  (I4) Theorem KB (Kplus-r2 L238-241) and Theorem KBH (inverse-run-count/kappaB-high/proof-KBH.md L10-14, branch C4 of v4
       Theorem C, no inherited hypothesis).  Used only through Lemma TII below.
* Theorem P, Davenport-alpha, EGZ, Lemma AR: as in proof-K0star-r1.md Sec. 1.

## 1. Single-window facts at an empty run

**Lemma SING.**  Let w be a G-avoider, normalised A >= B (so B <= kappa), and t an empty run whose two neighbouring blocks
contain beta_t even ones.  Then lambda({t}) = B - kappa + 1 - beta_t and lambda({t}^c) = L_t := min(p, A - kappa + 1 - beta_t,
floor(A/2) + 1), so u_t avoids [1 - L_t, B - kappa - beta_t] and 0 (mod p).  If A = 2p - 1 and kappa + beta_t <= p, then L_t = p
and the residues still allowed for u_t are exactly the nonzero residues of [B - kappa - beta_t + 1, 0]: there are
kappa - B + beta_t - 1 of them; w is solvable if kappa - B + beta_t <= 1, and u_t = -1 is forced if kappa - B + beta_t = 2.
Proof.  Lemma H0 with m = 1, D_({t}) = 0, D_({t}^c) = A - B: lambda({t}) = min(p, B - kappa + 1 - beta_t, floor(B/2) + 1), and
B - kappa + 1 - beta_t <= 1 <= floor(B/2) + 1; lambda({t}^c) = min(p, A - kappa + 1 - beta_t, floor(A/2) + 1).  For A = 2p - 1:
floor(A/2) + 1 = p and A - kappa + 1 - beta_t >= p.  The complement of [1 - p, B - kappa - beta_t] in [1 - p, 0] is
[B - kappa - beta_t + 1, 0]; remove 0 (genuine).  []

## 2. The case B = kappa for all-odd G-words

Throughout this section w is an all-odd G-avoider (every maximal block odd, so beta(P) = 0 and o_F = k), normalised A >= B,
B = kappa >= 1; d_j = a_j - b_j (d_j = 0 at empty runs); D = A - B = 2p - k by (0.1).  For a cyclic interval Q, Lemma H0 gives
lambda(Q) = f(D_Q), f(x) := min(p, x + 1, floor((x + B)/2) + 1), and D_Q >= -B_Q >= -B.  Facts: (i) f(x) = x + 1 for -B <= x <= 0;
(ii) f(x) >= min(p, ceil(x/2) + 1) >= 2 for x >= 1 (B >= 1); (iii) f(x) >= min(p, h(x)) for x >= -B, h(x) := min(x + 1,
(x + B + 1)/2) = (x + B + 1)/2 - max(0, B - 1 - x)/2.  (V) and (Z0): B = kappa <= k - 1.
**Lemma KB* (uncapped, k <= p).**  If k <= p and every d_j <= 2p - 2, w is solvable.
Proof (Theorem KB's uncapped case, Kplus-r2 L249-273, re-derived; it never uses r_j >= 1).  Lemma BC (no boost) with the k
single runs in cyclic order.  (a) sum_j f(d_j) >= sum_(d_j >= 1) (d_j/2 + 1) + sum_(d_j <= 0) (d_j + 1) = D/2 + D_N/2 + k with
D_N := sum_(d_j <= 0) d_j >= -B, i.e. >= p + (k + D_N)/2 >= p + (k - B)/2 >= p + 1/2, hence >= p + 1.  (b) lower: for intervals
X, Y, Z partitioning the cycle, if none is capped the sum is >= (D + 3B + 3)/2 - (1/2) sum max(0, B - 1 - D_Q), which is
>= (D + 3B + 3)/2, (D + B + 4)/2, (D + 5)/2, D + 3 when s = 0, 1, 2, 3 of them have D_Q <= B - 2 (one part: D_Q >= -B; two parts:
D_a + D_b >= -B; three: sum = D), so >= 1; if one is capped (= p) the other two give >= 2 - B (both <= 0) or >= 1 - B + 2, so the sum
is >= p + 2 - B >= 3.  (b) upper: the unions X u Y, Y u Z, Z u X have D-values summing to 2D >= 2p; uncapped, the sum is
>= min(D + (3B + 3)/2, D + (B + 4)/2, (3D + 5)/2, 2D + 3) >= p + 1 (two small unions cover the cycle, so their D-values sum to
>= D - B); if one is capped with x, y the D-values of the other two (x + y >= D - B >= 1): a second capped union leaves a third term
>= 1 - B and the sum >= 2p + 1 - B >= p + 2; otherwise the two give >= 1 (both >= 0 by (i), (ii); or x < 0 < y and
f(x) + f(y) >= min(x + y + 2, (2x + y + B + 3)/2) >= min(D - B + 2, (D - B + 3)/2) >= 1).  (c) if d_j <= 0: f(d_j) + f(D - d_j)
>= (1 - B) + min(p, B + 1) >= 2 (D - d_j >= D >= p >= B + 1); symmetric if d_j >= D; else both >= 2.  []
**Lemma CAP (capped, k <= p).**  If k <= p, some d_j >= 2p - 1, and w has an empty run, then w is solvable.
Proof.  sum_(i != j) d_i = D - d_j <= 1 - k, while sum_(i != j) d_i >= -sum_(i != j) b_i >= -B >= -(k - 1).  So equality holds
throughout: a_i = 0 (i != j), b_j = 0, B = k - 1, a_j = d_j = D + B = 2p - 1 = A.  Lemma SING (beta_t = 0, A = 2p - 1,
kappa - B = 0) at any empty run t: no residue is allowed.  []
**Lemma KBH* (o_F >= p + 1; any reflection parities).**  A G-avoider (not necessarily all-odd) with A >= B and B = kappa >= 1
has o_F <= p.
Proof.  Theorem KBH (proof-KBH.md Secs. 2-4) re-checked for G-words.  Segments = maximal sets of runs (empty runs included)
strictly between cyclically consecutive odd blocks; each is a nonempty cyclic interval of runs and a union Q of 1 <= c <= o_F - 1
consecutive segments has m = 1, beta = 0, so its window (Lemma H0) is [-L_Q, U_Q] with U_Q = min(p - 1, D_Q, floor((D_Q + B)/2)),
L_Q = min(p - 1, D - D_Q, floor((D - D_Q + B)/2)), D = A - B = 2p - o_F >= 0.  Lemma ZS (pigeonhole on p + 1 prefix sums over p
consecutive segments; Q_ij proper because o_F >= p + 1) and Steps 1-3 (greedy theta with lo(x) = max(0, ceil((x - B)/2),
x - p + 1)) use only the integers d_G, P_G = max(0, d_G) <= A_G, N_G = max(0, -d_G) <= B_G, A <= 2p - 1 (trivial cut otherwise),
1 <= B <= p - 1 and D >= 0; segments consisting of empty runs simply have d_G = 0.  Where KBH uses D >= 1 ((2b), "D + B >= 2"),
D = 0 forces B >= 1 and A = B, and then r >= 2 tight intervals would need sum D_(Q_r) >= 2(B + 1) > A: impossible, so (2b) holds.  []
**Corollary B=K.**  No all-odd G-avoider with an empty run has B = kappa (KB*, CAP for k <= p; KBH* for k >= p + 1).
(kappa = 0 is Theorem K0*.)

## 3. kappa = 1, B = 0

**Lemma K1*.**  No all-odd G-avoider with an empty run has kappa = 1 and B = 0.
Proof.  All rotations are rho_1, R = 2p - k + 2, k >= 3 (Z0), so R <= 2p - 1; by (P0) g <= e_R <= 2, and the k - g nonempty runs give
k - g <= R, so k <= p + 2 and R >= p >= 5.  For a cyclic interval Q (m = 1, beta = 0): lambda(Q) = min(p, R_Q, floor(R_Q/2) + 1) =
floor(R_Q/2) + 1 - [R_Q = 0].  Partition: the k single runs in cyclic order; each empty run is a genuine single part with
lambda = 0, boosted to 1.  (a) sum lambda' = sum_i (floor(r_i/2) + 1) = (R + k + e_R)/2 = p + 1 + e_R/2 >= p + 1.  (b) lower: some of
X, Y, Z has R_Q >= 2, lambda >= 2; the others have lambda' >= 0.  (b) upper: the three unions have R-values summing to 2R, floors
>= R - 1; a union with R_U = 0 loses 1, and two such unions would cover the cycle (R = 0), so the sum is >= R + 2 - 1 = 2p - k + 3
>= p + 1.  (c): one of P_s, P_s^c has R_Q >= 3.  Lemma BC'.  []

## 4. Type (II) and the last FUS step

**Lemma TII (type-(II) shape; from (I4)).**  An RGR avoider w (F, R >= 1), A >= B, with B = kappa >= 1 has o_F <= p, and its OR-merge
w~ (k~ = o_F runs, Lemma OR) has one run with a = 2p - 1 = A, b = 0, and k~ - 1 runs equal to a single rho_-1; kappa = B = k~ - 1.
In w itself every even block lies inside the OR-segment G carrying the 2p - 1 letters rho_1.
Proof.  KBH gives o_F <= p.  KB (whose (D0) is needed only in its capped case) then shows that w~ has a run G with
d_G >= 2p - 1 (otherwise w is solvable).  As in CAP: sum_(j != G) d_j <= (2p - k~) - (2p - 1) = 1 - k~ and >= -B >= -(k~ - 1) by
(V), so all those runs have a = 0, b_G = 0, B = k~ - 1, a_G = 2p - 1; every run of an RGR word is nonempty, so each of the k~ - 1
runs is one rho_-1.  A segment with one rotation letter has one run and no internal block; even blocks are internal to segments.  []
**Lemma QQ.**  Let w' be a G-avoider with exactly one empty run t, whose neighbouring blocks S_(t-1) = sigma_u^(e1),
S_t = sigma_v^(e2) are both EVEN, and suppose a FUS step at t yields an RGR word w_end that is an avoider with B = kappa >= 1.
Then w' does not exist.
Proof.  FUS at t can recolour either even block, and both results are avoiders (Lemma FUS); both merge S_(t-1), S_t into one even
block E and keep A, B, H.  By Lemma TII for w_end, A = 2p - 1, kappa(w') = B, and E lies inside the segment G of w_end; hence in
w' the run t is internal to the segment G, whose other runs carry all 2p - 1 letters rho_1 and are nonempty (t is the only empty
run).  Lemma SING (beta_t = 2, kappa - B = 0, kappa <= p - 3 as H >= 2) forces u_t = -1, i.e. v = u + 2.  Let a' >= 1, a'' >= 1 be the
numbers of rho_1 in G before and after t, a' + a'' = 2p - 1, and O, O' the odd blocks opening and closing G.
Q' := (runs of G up to and including t): boundaries O (odd), S_t (even).  Recolouring S_t to u gives an avoider in which the
runs of G before E form a pattern with the same m, beta, D, B, kappa, hence the same window I(Q'), and with u-value
(y_O - u)/2 = u_(Q') + (v - u)/2 = u_(Q') + 1.  So both u_(Q') and u_(Q') + 1 avoid I(Q'); hence |I(Q')| <= p - 2.  By Lemma H0
(B = kappa, beta = 1, D = 2p - 1 - kappa): |I(Q')| + 1 = l1 + l2 with l1 = min(p, a', floor((a' + kappa)/2) + 1),
l2 = min(p, a'' - kappa, floor(a''/2) + 1).  If a' <= p - 1 (so a'' >= p), l1 + l2 >= p in each case: (l1, l2) = (a', a'' - kappa):
2p - 1 - kappa >= p; (a', floor(a''/2) + 1): >= a' + (2p - 2 - a')/2 + 1 >= p; (floor((a' + kappa)/2) + 1, a'' - kappa):
>= 2p - (a' + kappa + 1)/2 >= p as a' + kappa <= 2p - 2; (floor((a' + kappa)/2) + 1, floor(a''/2) + 1): >= (2p - 1 + kappa)/2 + 1 > p;
l2 = p: >= p + 1.  So |I(Q')| >= p - 1: contradiction.  If a' >= p, use Q'' := (runs of G from t to the end; boundaries S_(t-1)
even, O' odd) and the recolouring of S_(t-1) to v, which gives the u-value (v - y_O')/2 = u_(Q'') + 1; the same computation with
a' and a'' exchanged gives |I(Q'')| >= p - 1.  []
(Arithmetic aid, not a premise: the four-case bound was also checked for all primes p <= 307, 1 <= kappa <= p - 3,
1 <= a' <= 2p - 2: 0 exceptions; eval transcript of this worker, 03:0x PDT.)

## 5. Theorem RED

Define RES_<(p): G-words of length 4p - 2 (rotations rho_1, rho_-1; normalised A >= B) with at least one (genuine) empty run,
every maximal constant block of ODD length, every rotation run pure (only rho_1 or only rho_-1) or empty, and B < kappa.
**Theorem RED.**  Assume (I1)-(I4).  If REFL(p) fails, some word of RES_<(p) with kappa >= 2 is an avoider.  Conversely every
avoider in RES_<(p) violates REFL(p).  Hence REFL(p) <=> RES_<(p) contains no avoider with kappa >= 2.
Proof.  Let w0 be an avoider violating REFL(p); normalise x = 1 and A >= B.  It is a G-word with g >= 1 (F >= 2, R >= 1 as before).
Run the following process; every move preserves avoidance, the length and rigidity of rotations; A >= B is kept (TR keeps A, B;
M0' lowers both by 1; the other moves keep them).  At every state with g >= 1, kappa >= 1 by Theorem K0*.
 P1 (FUS) at an empty run adjacent to an even block.
 P2 (PM0) across an even block whose two neighbouring runs are nonempty.
 P3 (TR-fill) if some run has a, b >= 1 and r >= 3: move one rho_1 rho_-1 pair from it into an empty run (it becomes a (1,1)-run;
    the donor stays nonempty).
 P4 (M0') if some run is a (1,1)-pair: delete its two letters (the run becomes empty) and insert sigma_y sigma_y into some block
    sigma_y^l.  Avoidance is preserved because, for the representation, every lambda(P) and I(empty) shrink (B and kappa drop by
    1, D_P, m, beta unchanged: the proof of Lemma M0, proof-RUNS.md L408-410, with Lemma H0); in the maximal decomposition the two
    neighbouring blocks may fuse (if equal-valued), which lowers kappa by one more.  No empty run is destroyed.
Apply the first applicable move.  The triple (kappa, g, k) decreases lexicographically at every move (P1: g; P2: k; P3: g; P4:
kappa), so the process stops.  Exits with g = 0 happen only through P1 or P3:
 Exit P3: the RGR avoider produced has B >= 1 and a (1,1)-run; by (I1) B = kappa; by Lemma TII every run of its OR-merge is
   pure: the (1,1)-run lies in some segment, which then contains both letters.  Contradiction.
 Exit P1: let w' be the last state with g >= 1 and w_end = FUS(w') the RGR avoider.  The step kills every empty run of w', so
   (C1) g(w') = 1 and the empty run t has an even neighbour, or (C2) g(w') = 2: sigma_u^a [] sigma_v^b [] sigma_u^c with b even.
   B(w_end) = B(w') =: B and kappa(w_end) = kappa(w') - [C2 with a, c odd].  By (I1), (I2) B = kappa(w_end).
   - kappa(w_end) = 0: then kappa(w') >= 1 forces C2 with a, c odd, and w_end contains the even block sigma_u^(a+b+c) with kappa = 0,
     contradicting (I3).
   - kappa(w_end) >= 1: Lemma TII gives A = 2p - 1.  Apply Lemma SING in w' (kappa(w') + beta <= p since an even block exists):
     C2 with a, c odd: kappa(w') - B = 1 and beta_t = beta_(t+1) = 1 force u_t = u_(t+1) = -1; but u_t + u_(t+1) = (u - v)/2 +
     (v - u)/2 = 0 and p is odd.  C2 otherwise (kappa(w') = B): an outer block odd gives an empty run with beta = 1: solvable;
     both outer blocks even give beta = 2 at both runs, u_t = u_(t+1) = -1, the same contradiction.  C1 (kappa(w') = B): beta_t = 1
     is solvable; beta_t = 2 is excluded by Lemma QQ.
 Terminal state with g >= 1: P1 and P2 do not apply, so there is no even block; P3, P4 do not apply, so every run is pure or empty.
   kappa >= 1 (K0*), B <= kappa.  B = kappa is excluded by Corollary B=K; kappa = 1 forces B = 0 and is excluded by Lemma K1*.  So
   the terminal state is an avoider in RES_<(p) with kappa >= 2.  The converse direction is trivial.  []

## 6. The residual RES_<(p), kappa >= 2: what is known and why it is open

Necessary relations for an avoider in RES_<(p) (from Z0, P0, V, Lemma SING): 2 <= kappa <= p - 1; 0 <= B <= kappa - 1;
A = R - B <= 2p - 1; R = 2p - k + 2 kappa; k >= 2 kappa - B + 1 >= kappa + 2; g + (number of even nonempty runs) <= 2 kappa;
k - g <= R, so k <= p + 2 kappa; at every empty run u_t avoids [1 - L_t, B - kappa] and 0; if A = 2p - 1 then kappa - B >= 2.
Finite status (aids): p = 5: empty (all 3,730 D10 avoiders of length 18 are RGR, olson/README.md Sec. 5.1).  p = 7: words with
k <= 9 are inside the normal form NF of c2/invstar/proof-GR0-r1.md (all blocks odd and runs pure satisfy NF (i), (ii)) and were
excluded by gwas2 (unreviewed code, c2/invstar/results.md Sec. 3); k = 10..19 are NOT computed here (contract: no blind
extension; a rough count of run data alone, before value search, is ~1.5e8 at p = 7).  For all p, nothing beyond the relations
above is proved for this class.
Why the available certificates stop here (concrete failures, not attempts merely abandoned):
(F1) Single-window boosts vanish: for kappa - B >= 2 the empty-run singleton has lambda({t}) = B - kappa + 1 <= -1, and the
     genuineness residue 0 lies outside I({t}); the single-run Lemma BC partition loses kappa - B per empty run (K1* and KB* are
     exactly the cases kappa - B <= 1 with B = 0, resp. kappa - B = 0).
(F2) The RGR proofs of the analogous RGR statements (C0-B'/S1' for B = 0, Theorem M and NMH-iii for B >= 1) use lifts and defect
     counts in which every run has r_t >= 1: e.g. S1' Step 1 needs R - r_t >= 2 kappa - 1 for every run (Kplus-r2 L181), which fails
     for a run carrying almost all rotations when g is large, and its Step 2 bound Phi(Z) >= 2 kappa + 2 uses rho_Z >= |Z|
     (Kplus-r2 L192-193), false when Z contains empty runs (whose lifted brackets bh_t = 2x_t are even and nonzero).  They cannot be
     imported by renaming (contract).
(F3) Filling an empty run with rho_1 rho_-1 and removing one reflection pair gives an RGR word w° with 1 <= B + 1 < kappa + 1, which
     is solvable by (I1); but its windows exceed those of w exactly at the patterns P with D_P + B odd and
     floor((D_P + B)/2) + 1 < min(p - m + 1, D_P + B - kappa + m) (and the complements), so (I1) only yields: an avoider in RES_<(p)
     with g = 1 has some such P with u_P = (D_P + B + 1)/2 or the mirror condition.  No contradiction follows from this alone.
So the exact open statement for this slice is:  REFL-RES(p): no word of RES_<(p) with kappa >= 2 avoids.
