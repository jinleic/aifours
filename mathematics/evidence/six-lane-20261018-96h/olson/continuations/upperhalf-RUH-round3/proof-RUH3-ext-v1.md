# RUH3-ext: R-UH for every 5<=e<=(p-1)/2 (closes the part e<=(p-1)/2 of residual R1; e=(p+1)/2 stays open), v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T18:14:02-0700. Status: CANDIDATE_UNVERIFIED written proofs. Same frozen scope
(RUH3-scope-v1.md, SHA256 c6601f27ab4b1752b7d76ae769c1c1229160367b20b8da0ba4ab60a138815bbb) and authority as the companion
proof-RUH3-v1.md (SHA256 027ac177c9b14e76ef86d1f0c881629eb1011f1dec32c9570f48be7e0b626b31, same round and review package; cited
below as "R3"). Read together with R3: this file says exactly which parts of R3 are reused, replaces R3's uses of the SH range
by Lemma L* and a new window, and adds Lemma E*, Lemma POS* and Theorem U. All case work by hand; no script, assertion,
enumeration, solver, Lean or computation over scientific data. Inputs as in R3 Sec. 9 (NF, GRX if, RS(b), CD; UH-A only for
Corollary U). Not used: RUH2, KP3, KP4, R7, UH-SH/MW/L/PH. No novelty, priority, Lean or human-review claim.

## 0. Statements (full antecedent of R3 Sec. 0 throughout; nu:=p+1-2e)

Let p be prime and 5<=e<=(p-1)/2 (so p>=2e+1>=11), k'':=min(e, floor((p+2-e)/2)) and k:=floor(e/2)+1.
LEMMA L* [NEW]. Every proper nonempty set P of runs with d(P)<=c-1 ("low") and 1<=m(P)<=k'' satisfies
d(P) <= c - min(e, 2m(P)-1). (In the SH range k''=e, so this contains R3's Lemma L.)
LEMMA H [NEW]. There is a run h with d_h>=p+1+delta; every nonempty set avoiding h is low.
LEMMA E* [NEW]. If 5<=e<=(p+1)/2 and e<=c<=2e-1, then E<=ceil(c/2)-1 and E+C_E<=e+eps-1, where eps=c-2floor(c/2) and C_E is the
number of maximal cyclic intervals ("clusters") of the set of empty runs.
LEMMA POS* [NEW]. For 5<=e<=(p-1)/2 and e<=c<=2e-1, the conclusions of Lemmas H and E* are contradictory.
THEOREM U [NEW, uniform]. For every prime p and every e with 5<=e<=(p-1)/2, no avoider with the full antecedent has
3<=c<=2e-1 (c<=e-1: Theorem A*, Sec. 6; c>=e: Lemmas E* and POS*).
COROLLARY U. With accepted UH-A: for every prime p>=11 and every kappa with (p+1)/2<=kappa<=p-5, no avoider of length 4p-2 has
an admissible NF with terminal k=p+1 and kappa^=kappa.
NOT PROVED: e=(p+1)/2, i.e. kappa=(p-1)/2, for every prime p>=11 (Sec. 7).

## 1. What is reused from R3

- R3 Sec. 1 (word form, SR, notation): unchanged. For e<=(p-1)/2 every j in [m,m+e-1] with 0<=m<=e satisfies 0<=2p-2j<=R,
  because 2e+1-p<=0 and j<=2e-1<=p-2.
- R3 Sec. 2: unchanged. Lemma P needs 2e<=p+1, Lemma U needs p-2e+3>0, and A<=2p-1 uses n=2p<=R, i.e. R-2p=p-1-2e>=0.
- R3 Sec. 3: Lemma MW is unchanged. (MWe) and the m=e path are NOT used; Lemma H (Sec. 3 below) replaces them. "Light sets"
  and "Counts" are reused verbatim: they use only d_h>=p+1+delta and (W).
- R3 Sec. 4 (Lemma L, SH range only) is replaced by Lemma L*. R3 Sec. 5 (Lemma S) is unchanged.
- R3 Secs. 6-8 are re-run below for e<=(p-1)/2 with the stated changes; this also re-proves R3's results by another route.

## 2. Proof of Lemma L* [NEW]

Put m:=m(P), g:=c-d(P)>=1. Under z_P the signed value a has multiplicity phi=A-d(P) and w0=R-phi=p-1-g. For j in
[m,m+e-1] (all admissible, Sec. 1) and K_j=p-1-2e+2j: K_j>=w0 iff j>=e-g/2, and K_j<=phi iff j<=(p+1+g)/2. Suppose g<=e-1
and g<=2m-2; we show that the number q of such j is >=g+1, contradicting MW (q>=1 forces w0+q<=p-1, i.e. q<=g).
 Case A, m>=e-floor(g/2): the j in [m, min(m+e-1, floor((p+1+g)/2))] count, at least min(e, floor((p+1+g)/2)-m+1) of them;
 e>=g+1, and m<=k''<=floor((p+2-e)/2)<=floor((p+1-g)/2)=floor((p+1+g)/2)-g because g<=e-1.
 Case B, m<e-floor(g/2): the j in [e-floor(g/2), min(m+e-1, floor((p+1+g)/2))] count: m+floor(g/2)>=g+1 of them if the
 minimum is m+e-1 (g<=2m-2), otherwise floor((p+1+g)/2)-e+floor(g/2)+1>=g+1, because p>=2e+1 gives
 (p+1+g)/2>=e+1+g/2, hence floor((p+1+g)/2)>=e+ceil(g/2).
Hence g>=min(e,2m-1). Note also 2k''-1>=e and 2k''>=e+2: k''=e, or k''=floor((p+2-e)/2)>=(p+1-e)/2>=(e+2)/2. []

## 3. Proof of Lemma H [NEW]

k<=k'' (k<=e; 2k<=e+2<=p+2-e) and 2k-1>=e. Let P be proper with m(P)=k. If P is low, Lemma L* gives d(P)<=c-e. If P is high,
P^c is low with m(P^c)=k, so d(P)=d(all)-d(P^c)>=(Lambda+c-1)-(c-e)=Lambda+e-1. As Lambda=2kappa+1-A'=p-2e+2+c+delta, the two
types are separated by the gap (Lambda+e-1)-(c-e)=p+1+delta, and complements swap them. With runs 0..N-1, N=p+1>=2k+2
(p>=2e+1>=e+6), the single-run toggles of R3 Sec. 3 with e replaced by k (add N-1,...,2k; remove 0; for i=1..k-1 add 2i-1
and remove 2i; add 2k-1) keep m=k from P0={0,2,...,2k-2} to P0^c. Oriented from its low end to its high end, some step
crosses the gap; a removal would need beta_x-alpha_x>=p+1+delta>kappa>=A'; so a run h is added with d_h>=p+1+delta. R3 Sec. 3
(light sets) then shows that every nonempty set avoiding h is low, and (counts) E+|Q|>=c+1, |Q|<=c-1 if Q is nonempty, E>=2,
d(P)>=|P n Q| for P inside (empty runs) u Q. Let X be the set of runs other than h holding a letter !=a: |X|<=b=p-1-c, and
every run other than h is empty, in Q, or in X. []

## 4. Proof of Lemma E* [NEW]

Run R3 Sec. 6 (proof of Lemma E) with mu=floor(c/2) and three changes; Case II (c=2e-1) occurs only for e<=(p-1)/2 (for
e=(p+1)/2, b=p-1-c>=0 gives c<=2e-2).
(a) Only sets Y of empty runs with m(Y)<=M0:=ceil((e+1)/2) are used (B0 uses Y empty). For them J(Y) lies in [1,M0+e-1] and
 M0+e-1<=3e/2<=(p+1+c)/2 (c>=e, p+1>=2e), so every j in J(Y) is admissible (j>=1>=(2e+1-p)/2, j<=p) and free; B0 lies in
 [1,e-1]. Also e-mu<=(e+1)/2<=M0 because c>=e.
(b) In (I.5) and (II.3), with m1, m2 and max(m_i,e-mu) at most M0<=(e+2)/2, the defect satisfies
 D>=2L-R'-(e+2)+m+e-1>=L-c-1>=-c>-p (Case I; c<=p-1) and D>=2-2M0-(e-m)>=1-2e>-p (Case II, where 2e<=p-1); the upper
 bounds D<=max(3mu+eps-e, c-2)<=2e-2<p and D<=2e-1<p are unchanged. Additivity is applied only to sets with m<=M0.
(c) In (I.6) take a union Y' of k6:=floor(mu/2)+1<=M0 intervals of Y+: k6<=theta(Y')<=R'-k6-e+1<=mu-k6 (R'<=L+c-1<=e+mu-1),
 impossible; so m(Y+)<=floor(mu/2) and |Y+|+m(Y+)<=theta(Y+)+m(Y+)<=R'-e+1. (I.7) is unchanged (it uses e-mu<=M0 intervals):
 m(Y-)<=e-mu-1 and |Y-|<=e-mu-L. In (II.3) a union of M0 intervals of the empty runs would give |Y'|+M0<=e with |Y'|>=M0,
 impossible as 2M0>=e+1; so C_E<=M0-1, and |Y|+m(Y)<=e holds for Y = all empty runs.
Conclusions. E<=ceil(c/2)-1 exactly as in (I.8) and (II.3). Every cluster contains a maximal interval of Y+ or of Y-, and
distinct clusters contain distinct ones, so C_E<=m(Y+)+m(Y-). Case I: if Y+ and Y- are nonempty,
E+C_E<=(R'-e+1)+(e-mu-L)+(e-mu-1)=R'-L+e-2mu<=e+eps-1; if Y+ is empty, E+C_E<=2e-2mu-2<=e+eps-2 (e<=2mu+eps); if Y- is
empty, E+C_E<=R'-e+1<=mu<=e-1. Case II: E+C_E<=e=e+eps-1. []

## 5. Proofs of Lemma POS* and Theorem U [NEW]

Lemma POS*. Use the path (h removed), clusters, S-blocks, Q-blocks, r_Q, n_in, the set I and P:=Q u I of R3 Sec. 7, with
2m(P)-1>=E-1. By Lemma E*: E<=ceil(c/2)-1<=e-1, 3E<2(c+1), |Q|>=c+1-E>=c+2-e; and 2k''-1>=e.
(alpha) m(Q)>=k''. Let P1 be the union of k'' largest Q-blocks: k''<=|P1 n Q|<=d(P1)<=c-e (Lemma L*). As c-e<=e-1<2k'', the
 k''-th largest block, hence every block outside P1, is a single run, and |Q|<=c-e+m(Q)-k''. Consecutive Q-blocks on the
 path are separated by segments whose runs are empty or in X; each segment contains a whole cluster or a run of X, distinct
 segments distinct ones; so m(Q)-1<=C_E+|X|<=(e+eps-1-E)+(p-1-c). Hence c+1-E<=|Q|<=c-e+1+(e+eps-1-E)+(p-1-c)-k'', i.e.
 c+k''<=p-2+eps. If k''=e, already k''<=c-e gives c>=2e, impossible. Otherwise k''=floor((p+2-e)/2), so 2k''>=p+1-e, and
 c>=e+k'' gives c+k''>=e+2k''>=p+1>p-2+eps. Contradiction.
(beta) m(Q)<k''<m(P). Delete runs of I from P until m=k'': the resulting P1 contains Q, and Lemma L* gives |Q|<=c-e<c+2-e.
(gamma) m(P)<=k''. Cases (ii), (iii-a) and (iii-b) of R3 Sec. 7 apply verbatim: they use Lemma L only at m(P) and at
 m(P')=E/2+1<=(e+1)/2<k''. []
Theorem U. Let 5<=e<=(p-1)/2. If e<=c<=2e-1, Lemma H and Lemma E* give the hypotheses of Lemma POS*: contradiction. If
3<=c<=e-1, apply Theorem A* (Sec. 6). []

## 6. Theorem A* [RE-DERIVED for e<=(p-1)/2] and Corollary U

Theorem A*. Let 5<=e<=(p-1)/2 and 3<=c<=e-1. The proof of R3 Sec. 8 (Theorem A) applies with h from Lemma H and Lemma L* in
place of Lemma L: its uses of Lemma L have m<=floor((c+1)/2)+1<=floor(e/2)+1<=k''; its last step uses j=e, admissible for
m(Y)<=c+1<=e (n=2kappa in [0,R]) and free (2kappa<=A, and 2kappa>=b as 2e<=p+1+c). []
Corollary U. For (p+1)/2<=kappa<=p-5, e=p-kappa lies in [5,(p-1)/2]; UH-A's literal antecedent holds ((p-1)/2<=kappa<=p-3,
p>=7), Lemma U gives the nonzero common class with A>=A', and UH-A gives 2kappa+3<=A<=2p-1, i.e. 3<=c<=2e-1, which Theorem U
excludes. []

## 7. The excluded boundary e=(p+1)/2 (NOT PROVED; failed route retained)

For e=(p+1)/2 (nu=0, N=2e, R=2p-2), K_j=2j-2 and, for a low set with g=c-d, the MW window is j in [e-g/2, e+g/2]; it holds at
most 2floor(g/2)+1 lengths, so for odd g one always has q<=g and MW gives no constraint. Lemma L* (Case B needs
floor((p+1+g)/2)>=e+ceil(g/2), false for odd g), the window of Lemma H and the run h are therefore unavailable by this route.
Lemma E* still holds there (its proof does not use h; Case II does not occur), but Lemma POS* needs h and Lemma L*. The
exact remaining cell is recorded in the residual note of this round.
