# RUH3 residual note: exact remaining part of R-UH after proof-RUH3-v1 and proof-RUH3-ext-v1, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T18:16:27-0700. Companion of proof-RUH3-v1.md (SHA256
027ac177c9b14e76ef86d1f0c881629eb1011f1dec32c9570f48be7e0b626b31; "R3") and proof-RUH3-ext-v1.md (SHA256
0c4efe594bde2c6c3afe2916048d52beb36b9b296b6c6d0f545c4729d96feecd; "R3-ext"). CANDIDATE_UNVERIFIED. This note records where the routes stop; it does not
claim that any cell is false or that an avoider exists, and the missing claim below is a route target, not a lemma shown
necessary. No counterexample word is supplied. Full NF antecedent throughout; no multiset-only statement.

## 1. What is proved (pointers)
- R3: SH range (p>=13, 5<=e<=(p+2)/3): R-UH for every 3<=c<=2e-1 (Theorems A, R2); Corollary SH with UH-A.
- R3-ext: every prime p and every 5<=e<=(p-1)/2 (so p>=11): R-UH for every 3<=c<=2e-1 (Theorem U); Corollary U with UH-A:
  for every prime p>=11 and (p+1)/2<=kappa<=p-5 no avoider of length 4p-2 has an admissible NF with terminal k=p+1 and
  kappa^=kappa. This contains the SH result, closes residual R2 of RUH2, and closes the part e<=(p-1)/2 of RUH2's residual R1
  (for example p=11 with e=5, p=13 with e=6, p=17 with e in {7,8}).

## 2. Exact residual of R-UH on the frozen range (p>=11 prime, (p-1)/2<=kappa<=p-5, 3<=c<=2e-1)
(R1b) e=(p+1)/2, i.e. kappa=(p-1)/2, for every prime p>=11, and every c with 3<=c<=p-1 (c<=2e-1=p and b=p-1-c>=0).
  Examples: p=11 (kappa=5, e=6), p=13 (kappa=6, e=7), p=17 (kappa=8, e=9). Here N=2e=p+1, R=2p-2, A=p-1+c, b=p-1-c,
  Lambda=p-A', lambda=c-1, Lambda-lambda=2+delta.
  Constraints proved there under the full antecedent: Lemmas P and U, (W), A'<=kappa (R3 Sec. 2; n=2p is not admissible, A<=2p-1
  comes from accepted UH-A), Lemma MW, Lemma S with |M|<=c and 0 not in M, and, for e<=c<=p-1, Lemma E* of R3-ext:
  E<=ceil(c/2)-1 and E+C_E<=e+eps-1. The MW count of R3-ext Sec. 7 also gives, for a low set P with g:=c-d(P) EVEN: g>=2m(P)
  or g>=2(e-m(P))+2 (if g/2+1<=m(P)<=e-g/2, the g+1 lengths j in [e-g/2,e+g/2] are admissible, 1<=j<=p, and counted, against
  MW). Remaining profiles: avoiders of this cell satisfying all of these; no run h with all avoiding sets low is known.
Nothing else in the frozen range remains: c<=2 is UH-A, and e<=(p-1)/2 is Theorem U.

## 3. Failed routes and exact failing inequalities (retained)
(G1) MW parity at e=(p+1)/2: K_j=2j-2, and for a low set the counted lengths lie in [e-g/2,e+g/2], at most 2floor(g/2)+1 of
     them; for odd g one always has q<=g, so MW gives nothing. Hence Lemma L* (Case B needs floor((p+1+g)/2)>=e+ceil(g/2)),
     the window of Lemma H and a super-heavy run are not obtained, and Lemma POS* and Theorem A* (which need h and Lemma L*)
     do not apply.
(G2) Ordinary first passage: the forced jump is Lambda-lambda=2+delta; a high single run follows only if 2+delta>c-1.
(G3) Two disjoint high sets need A>=2Lambda, i.e. A'>=(p+1-c)/2=kappa+1-c/2; for a given delta this is compatible with
     A'<=p-1-c-delta exactly when c+2delta<=p-3=2e-4.
(G4) The m=e window and its toggle path (RUH2 F1 as qualified by its erratum 2, N4) are unavailable at N=2e: the only sets with
     m=e are the two alternating sets.
(G5) RUH2's routes F1-F5 and missing claims MC1/MC2 are superseded for e<=(p-1)/2 (closed by R3/R3-ext); MC2's uniform
     missing-set classification was replaced by Lemma E/E* (component of M containing B0, additive lifts) and the position
     lemmas.

## 4. Smallest missing claim of this route (not claimed necessary)
(MC1b) For e=(p+1)/2: a run h such that every nonempty set avoiding h is low, plus d(P)<=c-min(e,2m(P)-1) for the sets
       avoiding h with m(P)<=floor(e/2)+1 that Lemma POS* and Theorem A* use, including the case of odd c-d(P); or another
       mechanism replacing MW where c-d is odd. With these, R3-ext Secs. 4-6 would apply (Lemma E* already holds there).
