# KP4 obstruction at p=7: exact residual after Proposition KP4-7P, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T16:32:33-0700. Outcome O3 of KP4-EXCL-scope-v1.md (SHA256
ba13fdd35cb02b11b179c8a9087737cf35e55f9197ae4512dac62edf9cc51c4f). Companion: proof-KP4-v1.md (SHA256
a6308ea8e265869795028fcddbdfaaa5a01f0ec514b587da0a6c227af1efaacf) read with erratum-1-proof-KP4-v1.md (SHA256
cb2802c6e7fb7942e83fd84b3dd720e99cfd4103866340f4266184780f9747ef). Status of the new statements here (Lemma PR, Lemma B1):
CANDIDATE_UNVERIFIED written proofs. Everything else here describes where routes stop; it is NOT a claim that any cell is
false, that any avoider exists, or that the missing claim is mathematically necessary or minimal. No counterexample word is
supplied. No computation, enumeration by machine, model CLI or Lean.

## 1. What is proved (pointer) and what is not

Proved in the companion (full NF antecedent throughout): KP4-EXCL for every prime p>=11 (Theorem KP4-A); at p=7 the
pure-rotation subcase (Proposition KP4-7P) and the necessary conditions of Lemma KP4-7N (dominant class {a,-a}, a!=0, A>=7,
A'<=3, window, dominant multiplicity !=8 at m=2,3). NOT proved: KP4-EXCL at p=7 when the rotation multiset is not constant.

## 2. Exact residual at p=7 and the accepted UH-A narrowing (input change recorded)

Residual R7: p=7, an avoider w of length 26 with SOME admissible NF u having terminal k=8, kappa^=3 (H^=3 arbitrarily
distributed, empty runs separate different values), and not all twelve rotation letters equal; show that some sign pattern
and some admissible length attain the target.
Input change (only for this narrowing; the companion proof does not use it): Main accepted UH-A at exact scope at
2026-10-19T16:27:57-0700, RUN/review/olson-UH-CONSTRAINTS-parent-verdict-v1.md (SHA256
7c7b90f2745ba0cb7a8300c3f914a72c4b457259e4fcd45385266db15e4a71e3) with mandatory errata v1 8f1ea491..., v2 ac2a7f26..., v3
0dc67886.... Its shared antecedent (prime p>=7, (p-1)/2<=kappa<=p-3, some admissible NF with terminal k=p+1, arbitrary
H-distribution, empty-run rule) contains p=7, kappa=3. Hence A>=2kappa+3=9 at this cell, so in R7:
  A in {9,10,11}, b=12-A in {1,2,3}, A'<=b (and A'<=3), delta=b-A'.
Without UH-A, Lemma KP4-7N alone gives A in {7,...,11}.

## 3. Lemma PR (pair case, delta=0) [CANDIDATE; p=7]

Assume every rotation letter is a or -a. Under z_P exactly epsilon(P):=A'+d(P) letters have signed value -a and 12-epsilon(P)
have +a (a-letters in P and (-a)-letters outside P are the former). So the attained normalized sums are exactly the pure
intervals of proof Sec. 7.3 with alpha replaced by epsilon: [max(-nu,nu-epsilon), min(nu,12-epsilon-nu)], nu in V_m.
Consequences (same interval computations as Proposition KP4-7P): arcs never have epsilon=6; sets with m=2 or 3 never have
epsilon in {4,6,8}; an empty run has epsilon=A' and t in Allow_1(A') minus {0}, where Allow_m(eps) is the complement of the
attained set: Allow_1(1)={-1,0,1}, Allow_1(2)={-1,0}, Allow_1(3)={-2,-1}, Allow_2(1)={-1,0}, Allow_2(2)={-1},
Allow_2(3)={-2}, Allow_3(3)={-2} (from attained [2,5],[1,5],[0,4],[1,5],[0,5],[-1,4],[-1,4]). Hence:
- A'=1: single empty t=+-1; two empties (adjacent: Allow_1(1); non-adjacent: Allow_2(1)) need t+t'=0. So |E|<=2.
- A'=2: single empty t=-1; two empties give -2, outside Allow_1(2) and Allow_2(2). So |E|<=1.
- A'=3: single empty t in {-2,-1}; any two empties need both t=-1; three empties give -3, outside Allow_1(3), Allow_2(3)
  and Allow_3(3). So |E|<=2.
Missing for the pair case (R7a): the run-weight profile enumeration with weights w_i=alpha_i-beta_i (which may be -1 on a run
holding only a (-a)-letter, or 0 on a nonempty run), total 12-2A', against the forbidden values w(P)!=6-A' on arcs and
w(P) not in {4-A',6-A',8-A'} on m=2,3 sets, plus the empty-run t-constraints. This is the analogue of the profile
enumeration of Proposition KP4-7P (A'=0); it was not carried out.

## 4. Lemma B1 (all-plus constraints with few non-a letters) [CANDIDATE; p=7]

Let B be the b=12-A letters !=a, omega(u)=(x_u-a)/(2a)!=0, G their subset sums, M=Z_7 minus G. The all-plus lengths n=12,10,8
(j=1,2,3, normalized target j) give: sigma(omega(B))!=1 (n=12 forces J=B); 2 is not a sum over >=b-2 elements (n=10);
3 is in M (n=8, every J allowed). For b=1 (B={u}) this leaves omega(u) in {4,5,6}, i.e. x_u/a in {2,4,-1}: u is a
(-a)-letter or a deviant of value 2a or 4a. Missing for the deviant case (R7b, delta>=1): the attained sets then depend on the
deviant values and their runs; no reduction of R7b to the pair or pure tables is proved.

## 5. Route failures at p=7 (exact arithmetic retained)

(F1) Multi-length window. At p=7 the omitted counts are K in {0,2,4,6} (m=1), {2,4,6,8} (m=2), {4,6,8,10} (m=3),
{6,8,10,12} (m=4), with phi>=7, w0=12-phi<=5. Lemma MW excludes only (m in {2,3}, phi=8): calK={4,6,8}, w0+q=7. Every other
(m,phi) has w0+q<=6. So no strong window exists at p=7.
(F2) Super-heavy run. The p>=11 proof needs a run with d_h>=p+1+delta>=8. In the pure case every run holds <=5 letters
(proof Sec. 7.3: arcs never hold 6; a run with >=7 letters is excluded with the empties), so no argument valid for all
p=7 words can produce such a run; the p>=11 mechanism is unavailable at p=7.
(F3) Ordinary first passage. With lambda=A-7, Lambda=7-A', gap 2+delta, a high single run is forced only if A<9+delta;
with UH-A (A>=9) this needs delta>=A-8 (A=9: delta>=1; A=10: delta=2; A=11: never).
(F4) The p>=11 case analysis needs >=2 empty runs (from light sets) and distinct nonzero residues up to 10; at p=7 neither is
available, and |M|<=c=A-6 in {3,4,5} is not small relative to Z_7.

## 6. Smallest remaining claim of this route

(R7) For p=7, under the full NF antecedent with (via accepted UH-A) A in {9,10,11}: some pattern attains its target.
Split: (R7a) delta=0, A'=12-A in {1,2,3}: complete the weight-profile enumeration of Sec. 3; (R7b) delta>=1. Proving R7
together with the companion proof would give KP4-EXCL for every prime p>=7. R7 is named as the unfinished word-level target
of this route, not as a necessary or minimal lemma.
