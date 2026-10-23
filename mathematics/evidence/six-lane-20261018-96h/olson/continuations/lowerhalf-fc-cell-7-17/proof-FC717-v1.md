# FC717: the (kappa,p) = (7,17) terminal cell, conditional completion of the final count

Owner: OlsonThirdCutWindow (same math2 slot). Drafted after /bin/date 2026-10-20T09:32:13-0700.
Scope freeze: FC717-scope-v1.md, sha256 869d0ca7ab1cfd76d4e2c170b5813c5d6da53cc8260363ad06c8c01ec111fcad,
frozen 2026-10-20T09:26:06-0700 before any new derivation. Authority: written-olson-fc-cell-7-17-transition-v1.json,
sha256 ce7d4759924f0bcb7c9debf26160d1dd74018b86abb6bcb8a4aa5a43500e01de, LF1-70 (absolute paths in Sec. 7).
Outcome: CONDITIONAL PROOF COMPLETE. The balanced-level count below is proved by hand; its application to the word
uses the expressly conditional UMR premises, NOT an accepted UMR verdict. No failing step remains relative to those
premises. No computation, enumeration, solver, test or assertion over mathematical objects. No other cell or k is claimed.

## 0. Exact statement and conditional premise

THEOREM FC717 (CONDITIONAL). Assume the literal UMR-F and UMR Lemmas 3, 5, 7, 8, 10, 13 at (kappa,p) = (7,17), with the
UMR parent erratum v1 applied. Then no word w of length 66 over D_34 without an identity 34-subword in increasing
original index order has SOME admissible NF with terminal k = 18 and kappa_hat = 7. Extra reflection pairs may be
anywhere in the odd blocks and the genuine empty-run rule is retained; no o_F, nonempty-run, rotation-pair or rigidity
hypothesis is imposed. The proof works in EVERY frame supplied by those UMR premises, including RES.

UMR is not accepted at the time of this assignment (one review family plus parent written check, second family
pending). This theorem is therefore conditional on those premises. It is not an independently accepted exclusion.
The parent erratum restricts UMR Lemma 13's isolated-run addition to g/2 <= m <= kappa and withdraws its LF328-330
saturation gloss. Neither that gloss nor a converse to UMR Lemma 20 is used here. In fact neither RES nor UB is used in
the count: all frames satisfying the literal window conclusions are covered.

NEW COUNT LEMMA WC717 (proved below). The finite run/letter data and five-subset windows (A1)-(A4) of Sec. 1 imply
Xi(S_ev)+Xi(S_od) <= -1. This is a statement about integer sums, proved by hand without relying on the UMR final count.
The UMR total identity gives Xi(S_ev)+Xi(S_od) = e >= 0, so WC717 supplies the contradiction and proves Theorem FC717.
The distinction is explicit: WC717 is proved from (A1)-(A4); their availability from the NF word is CONDITIONAL on UMR.

## 1. Literal conditional inputs and the reduced count contract

At this cell N = 18, R = 30, 2p = 34, g = 4, delta = 10, h = 9, H = 9 and F = 36. Thus (7,17) belongs to UMR's range:
floor((17+7)/4) = 6 < 7 = (17-3)/2. UMR's central levels are 2..8. Fix ANY one of its frames.

The following are the only data needed for WC717 (the total identity is added only when applying it to the word):
(A1) The cyclic runs are 0..17. Their pairwise-disjoint sets of letter OCCURRENCES L_i partition 30 letters.
     Each letter l has an odd nonzero integer c_l. Put A := {l : c_l < 0}, A^c := {l : c_l > 0}, a := |A|, a' := 30-a,
     nu := sum_(l in A)|c_l|, B := sum_l |c_l|, e := B-30. Then nu >= a and
       e >= nu-a >= 0.                                                              (1)
     Indeed e = sum_l(|c_l|-1), and the contribution from A is nu-a. Also a' >= 13.
(A2) Each run i has an integer theta_i. An empty run (L_i empty) has theta_i a NONZERO EVEN integer.
     For a run set Q put L(Q) := union_(i in Q)L_i and Theta(Q) := sum_(i in Q)theta_i.
(A3) S_ev := {0,2,...,16}, S_od := {1,3,...,17}. Each has 9 pairwise non-adjacent runs. For Q contained in either S,
     |Q| = 5, put
       q(Q) := |L(Q) symdiff A| = |A outside L(Q)| + |L(Q) intersect A^c|,
       q'(Q) := 30-q(Q) = |L(Q) symdiff A^c|,
       chi(Q) := max(1, 6-q(Q), 6-q'(Q)).
(A4) Every such five-subset satisfies the TWO-SIDED bound
       e-2-nu-chi(Q) <= Theta(Q) <= -2-nu+chi(Q).                                     (W)

Why these data follow CONDITIONALLY, at the literal UMR scope:
- UMR frame definitions (LF49-56, LF99-118) give (A1)'s labels and counts. Its Lemma 5(d) gives
  a' >= (p+kappa+1)/2 = 25/2, so the integer a' is >= 13. Equation (1) is derived above, not an imported extra margin.
- UMR-F and Lemma 10 give (A2). Empty-run evenness is the only use of the genuine empty-run rule in the new count.
- Every five-subset of S is a proper independent set with m(Q) = 5. At level 5, UMR Lemma 2 gives ell = M = 6 and the
  selection window [6,24]. UMR Lemmas 7-8 give
    x(Q) = y(Q) = max(q(Q) mod 2, 6-q(Q), 6-q'(Q)),
    e-2-nu-x(Q) <= U'(Q) <= -2-nu+x(Q).
  UMR-F identifies U'(Q) = Theta(Q). Since x(Q) <= chi(Q), weakening the bounds gives (W). No extension to any other
  level or new realisation claim is being imported.
- UMR-F also gives Theta(all 18 runs) = B-2nu-34 = e-4-2nu. Hence for
    Xi(S) := Theta(S)+nu+2,
    Xi(S_ev)+Xi(S_od) = e >= 0.                                                       (T)

In the rest of Secs. 2-5 we prove WC717 using only (A1)-(A4), NOT (T).
Notation: type P and type Q below are classifications, not additional hypotheses on the word. Cardinalities count occurrences,
not residue values; in particular L(Q_1) and L(Q_2) are disjoint when Q_1, Q_2 are disjoint run sets.

## 2. Top-five bounds and the cases with negative fifth theta

For an alternating set S, order its 9 runs by decreasing theta (ties arbitrarily). Let J_S be the top 5, t_S the fifth
value and B_S := S outside J_S the bottom 4. Put e_B := number of empty runs in B_S, n_B := number of nonempty runs
there. Write simply J, t, B_S for one S when unambiguous.
Types of J:
  G: min(q(J),q'(J)) >= 5 (then chi(J) = 1);
  P: k := q'(J) <= 4 (then chi(J) = 6-k);
  Q: k := q(J) <= 4 (then chi(J) = 6-k).
These exhaust the cases and P, Q cannot coincide since q+q' = 30. Every run in B_S has theta <= t.

LEMMA 1 (one set).
(a) Type G: t <= -1 and Xi(S) <= -3.
(b) Type P or Q: t <= 0; if t <= -2 then Xi(S) <= -2-k; if t = -1 then Xi(S) <= 2-k-e_B.
(c) Type Q cannot have t = 0.
(d) Type P with t = 0 (case H): nu+k <= 4, a <= nu <= 4, and at most four letters are outside L(J). More precisely
    |L(J)^c| <= a+k <= nu+k <= 4, and Xi(S) <= -2-k+2n_B.
Proof. (a) Theta(J) <= -1-nu < 0 by (W), whereas t >= 0 would make all top five values nonnegative. Thus bottom four
are <= -1 and Theta(S) <= -5-nu.
(b) Theta(J) <= 4-k-nu <= 4 < 5, and 5t <= Theta(J), so t <= 0. If t <= -2, the bottom four sum to <= -8. If t = -1,
all bottom values are <= -1 and the empty ones are <= -2 (nonzero even); their sum is <= -4-e_B. Add nu+2.
(c) Suppose t = 0, so all top values are nonnegative and nu+k <= 4. Let l := |L(J)|. Type Q gives l <= a+k, and at least
5-l runs of J are empty (a nonempty run consumes at least one letter). Those empty top runs have theta >= 2, so
  10-2a-2k <= 10-2l <= Theta(J) <= 4-k-nu,
which forces 6 <= 2a+k-nu <= nu+k <= 4, impossible.
(d) Again 0 <= Theta(J) <= 4-k-nu. Type P means k = |A^c outside L(J)| + |L(J) intersect A|. Thus letters outside J
are in A (at most a letters) or in A^c outside L(J) (at most k), so the stated bound holds. Bottom nonempty runs have
theta <= 0, empty ones <= -2, so Theta(S) <= 4-k-nu-2(4-n_B). []

LEMMA 2 (two types with t <= -1). Let S_1, S_2 be the two alternating sets and write J_i, k_i, t_i for their data.
(a) Both J_i cannot be type P.
(b) If one is P, the other Q, and t_1,t_2 <= -1, then Xi(S_1)+Xi(S_2) <= -4.
(c) If both are Q and t_1 = t_2 = -1, then k_1+k_2 >= 6+nu, and Xi(S_1)+Xi(S_2) <= -2-nu.
(d) If both are Q and one t_i <= -2 (neither t_i is 0), then Xi(S_1)+Xi(S_2) <= -1.
Proof. (a) Every letter of A^c is outside L(J_1) or outside L(J_2), because these sets are disjoint. Hence
  13 <= a' <= q'(J_1)+q'(J_2) <= 8, impossible.
(b) Suppose J_1 is P, J_2 is Q. A letter outside L(J_1) union L(J_2) belongs to A^c outside L(J_1) (at most k_1) or to A
outside L(J_2) (at most k_2). There are 8 bottom runs in B_1 union B_2, so at least 8-k_1-k_2 are empty. The t=-1 bound
of Lemma 1(b) remains valid whenever t <= -1; summing gives Xi(S_1)+Xi(S_2) <= 4-k_1-k_2-(8-k_1-k_2) = -4.
(c) For type Q write alpha_i := |A outside L(J_i)|, beta_i := |L(J_i) intersect A^c|, so k_i = alpha_i+beta_i. As the
L(J_i) are disjoint, a <= alpha_1+alpha_2, so |L(J_i)| = a-alpha_i+beta_i <= alpha_(3-i)+beta_i. The top five of S_i
have at least 5-alpha_(3-i)-beta_i empty runs, whose theta is >= 2 (top values >= t_i = -1 and empty values nonzero
even); every other top value is >= -1. Thus
  10-3alpha_(3-i)-3beta_i <= Theta(J_i) <= 4-nu-alpha_i-beta_i,
  6 <= 3alpha_(3-i)+2beta_i-alpha_i-nu.
Summing gives 12 <= 2(k_1+k_2)-2nu. Lemma 1(b) now gives Xi(S_1)+Xi(S_2) <= 4-k_1-k_2 <= -2-nu.
(d) If both t_i <= -2, Lemma 1(b) gives sum <= -4. Otherwise, say t_1 <= -2 and t_2 = -1: the sum is
<= -k_1-k_2-e_(B_2). This is <= -1 unless k_1=k_2=0. In that case L(J_1)=A=L(J_2) and disjointness forces A empty;
all runs of J_2 are empty, so their fifth value t_2 cannot be the odd integer -1. []

## 3. Sparse alternating sets (the lower-window step)

LEMMA 3 (sparse sets). Suppose nu <= 4 and S is an alternating set.
(a) If |L(S)| <= 2, its fifth theta t_S is <= -2.
(b) |L(S)| <= 1 is impossible under (A1)-(A4).
Proof. Write l_J := |L(J_S)| and l := |L(S)|. Since a <= nu <= 4, a' >= 26. For l <= 2,
  q'(J_S) >= a'-l_J >= 24,
  q(J_S) = a+l_J-2|L(J_S) intersect A| >= l_J-a.
Consequently (W) gives
  Theta(J_S) <= max(-1-nu, 4-nu-q(J_S)) <= 4-l_J.                      (2)
If t_S >= -1, each empty run of J_S has theta >= 2 and each other run theta >= -1. A nonempty run consumes a letter,
so Theta(J_S) >= 10-3l_J. Together with (2): 10-3l_J <= 4-l_J, i.e. l_J >= 3, contradicting l_J <= 2. This proves (a).
For (b), let K be the BOTTOM five runs of S (positions 5..9 in the decreasing order). By (a), Theta(K) <= -10. Yet
  q(K) >= a-l, q'(K) >= a'-l >= 25,
  chi(K) <= 6-a+l
(the right side is >= 2, so it also bounds the constant 1 in chi). The LOWER half of (W), followed by (1), gives
  Theta(K) >= e-2-nu-(6-a+l)
           = e-(nu-a)-8-l >= -8-l >= -9,
a contradiction. This proves (b). []
This lemma uses two-sided windows on five-subsets only. It does not say that an empty-run bonus or the failure of UB
implies anything about every other half-certificate.

## 4. Case H: type P with fifth theta zero

LEMMA 4. If J_1 is type P and t_1 = 0, then Xi(S_1)+Xi(S_2) <= -1.
Proof. Write k := q'(J_1), B_1 := S_1 outside J_1 and n := n_(B_1). By Lemma 1(d), nu+k <= 4, a <= nu <= 4,
  |L(B_1) union L(S_2)| <= a+k <= 4,
  Xi(S_1) <= -2-k+2n.                                                (3)
As the letter sets of runs are disjoint, n nonempty runs of B_1 consume at least n of these four letters. Thus
  |L(S_2)| <= 4-n.                                                    (4)
Also q'(J_2) >= a'-|L(S_2)| >= 26-4 = 22, so J_2 is type G or Q, never P. By Lemma 1(c), a Q-type J_2 has t_2 <= -1.
We now cover every integer n in 0..4 explicitly.

n = 3 or 4. Equation (4) gives |L(S_2)| <= 1. This is impossible by Lemma 3(b).

n = 2. By (4) and Lemma 3(a), t_2 <= -2. If J_2 is G, (W) and the four bottom values <= -2 give
  Xi(S_2) <= (-1-nu)-8+nu+2 = -7,
so the sum with Xi(S_1) <= 2-k is < -1. If J_2 is Q, put k_2 := q(J_2); Lemma 1(b) gives Xi(S_2) <= -2-k_2, and
  Xi(S_1)+Xi(S_2) <= -k-k_2.
This is <= -1 unless k=k_2=0. In that exception L(J_1)=A^c and L(J_2)=A. A letter in a nonempty run of B_1 must be
outside L(J_1), hence in A, but A is already entirely in L(J_2), disjoint from L(B_1). This contradicts n = 2.

n = 1. Equation (3) gives Xi(S_1) <= -k <= 0, and (4) gives |L(S_2)| <= 3. If J_2 is G, Xi(S_2) <= -3. If J_2 is Q
and t_2 <= -2, Xi(S_2) <= -2-k_2. Both give the desired sum. It remains to treat Q with t_2 = -1. Put
l_2 := |L(J_2)| <= 3. The proof of (2) still gives Theta(J_2) <= 4-l_2: here q'(J_2) >= a'-3 >= 23, and
q(J_2) >= l_2-a. The empty/nonempty top count with t_2=-1 gives Theta(J_2) >= 10-3l_2. Therefore l_2 >= 3, so l_2=3
and both bounds equal 1:
  Theta(J_2) = 1.
All letters of S_2 lie in J_2 (|L(S_2)| <= 3), so the four bottom runs of S_2 are empty. They have theta <= -2, giving
  Theta(S_2) <= 1-8 = -7, Xi(S_2) <= nu-5 <= -1.
The sum is <= -1.

n = 0. Equation (3) gives Xi(S_1) <= -2-k. Type G or type Q with t_2 <= -2 immediately gives a sum < -1. For type Q
with t_2 = -1, Lemma 1(b) gives
  Xi(S_1)+Xi(S_2) <= -k-k_2-e_(B_2).
This is <= -1 unless k=k_2=e_(B_2)=0. But k=k_2=0 means L(J_1)=A^c and L(J_2)=A, so EVERY run outside J_1 union J_2
is empty; in particular all four runs of B_2 are empty, giving e_(B_2)=4, not 0. This exhausts n=0.
All cases n=0..4 have been proved, so Lemma 4 follows. []

## 5. Completion of the count and the conditional cell exclusion

Proof of WC717. If a top-five set has t=0, it is type P by Lemma 1(a),(c), so Lemma 4 applies. Otherwise all fifth
values are <= -1. If a top-five set is G, its Xi is <= -3 and the other set's Xi is <= 2 (Lemma 1), so their sum is
<= -1. With no G, both top-five sets are P or Q. Both P is impossible by Lemma 2(a); mixed P/Q is handled by Lemma
2(b); both Q is handled by Lemma 2(c),(d). Hence in every case
  Xi(S_ev)+Xi(S_od) <= -1.                                             (FC717)
This completes the proof from (A1)-(A4). []

Proof of Theorem FC717 (CONDITIONAL on UMR). Assume an avoider w has some admissible NF with terminal k=18 and
kappa_hat=7. Its normalised word u is an avoider with those parameters, as in the conditional UMR standing setting.
Fix ANY frame supplied there; its labels and theta satisfy (A1)-(A4) by Sec. 1 and also (T). WC717 gives the sum
<= -1, whereas (T) gives the same sum = e >= 0. Contradiction. This holds for every such frame, without assuming UB
or excluding the RES alternatives. Thus, under the permitted conditional UMR premises, no such NF word u or original
avoider w exists. []

Outcome relative to the input boundary: the full cell (7,17) is covered, including arbitrary extra-pair placements,
empty runs, all-equal rotation configurations, giant pairs, and every RES frame. No failing step remains after the
conditional input. UMR itself is not proved or accepted by this packet; its acceptance remains a prerequisite for an
accepted word-level exclusion. We do not claim the selected UB conditions become universal: FC717 bypasses them.

## 6. Scope, unused routes and process boundary

The count fixes level m=5, where ell=M=6 at (7,17); it does NOT claim a further fixed-deficiency family, another
middle cell, another terminal k, full p=17, reflection rigidity, INV*, o_F assembly, or full ordered Olson. Neither
UMR Lemma 20 nor its withdrawn saturation gloss is used. In particular we never infer failure of all half-certificates
from failure of UB. The empty-run bonus is retained in Lemmas 1(b), 2(b), 4(n=0); lower windows enter Lemma 3(b).
The large-offset case H is controlled by the small NUMBER of letters outside the top five, not by a rigidity premise.
Only the five-subset window is required for the new count; no window at m=0 or m=1 is imported or extended.

The scope was frozen before any NEW derivation. Prior exposure includes the author's entire UMR attempt (including
its (7,17) constants and failed RES routes), disclosed in FC717-scope-v1.md. Post-freeze, an unused exploratory route
considered extending the low-m windows to bound a+nu, but the delivered proof does not use or claim that extension.
All new mathematics was by hand. Exact machine steps, drafting replacements and checkpoint times are disclosed in
the review package; files are exclusive and immutable. No scientific computation, assertion, solver, test, Lean,
network access, model call, human-review or runtime claim.

## 7. Literal interface table (all paths absolute; LF ranges inclusive)

| Input | Absolute path | Whole-file SHA256 | LF lines | Scope and use |
|---|---|---|---|---|
| Authority | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-olson-fc-cell-7-17-transition-v1.json | ce7d4759924f0bcb7c9debf26160d1dd74018b86abb6bcb8a4aa5a43500e01de | 1-70 | Single (7,17) cell; conditional UMR permitted, not accepted; no other cell scope |
| Frozen scope | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-fc-cell-7-17/FC717-scope-v1.md | 869d0ca7ab1cfd76d4e2c170b5813c5d6da53cc8260363ad06c8c01ec111fcad | 1-75 | Frozen before new derivation; full prior-exposure disclosure |
| CONDITIONAL UMR framework, frame definitions and level-5 windows | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-middle-range/proof-UMR-v1.md | c403bfbae9f1c7b75698010cae78515a253154e689336e79006c588ff15023a9 | 1-406; used 18-28, 49-56, 99-122, 137-173, 201-209, 238-248, 252-258 | NOT accepted. UMR-F/Lemmas 3,5,7,8,10,13 at literal (7,17) scope, with governing erratum. Supplies (A1)-(A4) and (T); no extension of a window or a lemma |
| Governing UMR erratum v1 | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-erratum-v1.md | b83313b3fe828ee19a0902e9a5149db42ee55318500f92bac577b4bbd7088c5f | 1-10 | Lemma 13 link restricted to g/2<=m<=kappa. LF328-330 saturation gloss withdrawn; RES is selected-UB failure only; all-frame quantifiers retained |
| Review-status record only | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-first-family-parent-disposition-v1.json | 18ee4b8fa322d362bfc4c056bf85823296f9692deb84993604cb03e86c54a68f | 1-24 | One-family support, not an accepted input; not an additional mathematical premise |
| Accepted frontier context only | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FQW-parent-verdict-v1.md | a9388a49e227b3bf418e2250b515860a33f880dba816b5318a834faa5da9e566 | 1-9 | LF9 gives the remaining-middle-range frontier. No FQW lemma is used and no terminal-cell union is proved here |
| Range provenance context only | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-terminal-union-range-clarification-v1.md | c7789ee917f80e558c114a635a4c7b4efda55d3386bd968891a900ddc2bac39a | 1-7 | Not a mathematical premise of the new count |

Not claimed: acceptance or an independent proof of UMR; unconditional word-level exclusion without the explicitly
conditional UMR premises; other cells, kappa values, primes or terminal k; full p=17; full ordered Olson; INV*,
reflection rigidity or o_F assembly; a universal UB assertion; a saturation theorem for RES; priority, novelty, Lean,
human-referee or runtime verification. No model review is run by this worker. The parent alone controls reviews,
acceptance and any composed frontier statement.
