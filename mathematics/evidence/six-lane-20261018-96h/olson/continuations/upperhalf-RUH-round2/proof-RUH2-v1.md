# RUH2: strong windows, R-UH for c<=e-1 in the range 3e<=p+2, and the whole cell kappa=p-5 for p>=13, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T17:25:14-0700. Status: CANDIDATE_UNVERIFIED written proofs. LABELLED PARTIAL
of the frozen target (RUH2-scope-v1.md, SHA256 b1cdfaeee6db5985a2af1f8f98c4f66cd7a8e8e8fe77cbebab372f270d4c5dd0, frozen
2026-10-19T17:07:02-0700 before derivation): R-UH is proved only on the exact parameter ranges of Theorems A and B below;
residual-RUH2-v1.md states the exact remaining residual. All case work is by hand; no script, assertion, enumeration or
computation over scientific data. Inputs: accepted NF, GRX (if direction), RS(b), classical Cauchy-Davenport (CD), and accepted
UH-A at literal scope (only to state Corollary B). The super-heavy run (UH-SH) is NOT used as an import: it is re-derived
in Sec. 3 because the transition's accepted list names only UH-A/L/E. KP3, KP4 and R7 are candidates and are not cited; the
arguments taken from them are re-proved here and labelled [RE-DERIVED]. [NEW] marks new arguments. No novelty, priority,
Lean or human-review claim.

## 0. Statements

Throughout: p prime, e:=p-kappa, and the FULL antecedent: an avoider w of length 4p-2 over D_(2p) (no 2p letters in increasing
original index order with identity product) has SOME admissible NF with terminal k=p+1 and kappa^=kappa; H^=e-1 extra
reflection pairs anywhere in the odd blocks; every empty NF run separates different reflection values. a, A, A', c are as in
UH-A: a is the nonzero dominant class, A>=A', A=2kappa+c. "SH range": p>=13 and 5<=e<=(p+2)/3, i.e. 3e<=p+2.
LEMMA L [NEW]. In the SH range there is a run h such that every nonempty set P of runs avoiding h with 1<=m(P)<=e satisfies
d(P) <= c - min(e, 2m(P)-1).
THEOREM A [NEW, uniform]. In the SH range no avoider with the full antecedent has 3<=c<=e-1.
THEOREM B [NEW, cell]. For e=5 (kappa=p-5) and every prime p>=13, no avoider with the full antecedent has 3<=c<=9.
COROLLARY B. With accepted UH-A (which excludes c<=2) and A<=2p-1 (c<=2e-1=9): for every prime p>=13 no avoider of length 4p-2
has an admissible NF with terminal k=p+1 and kappa^=p-5.
NOT PROVED here: R-UH for 3e>p+2 (in particular p=11, and p=13 with e=6,7), and R-UH in the SH range for e>=6 and e<=c<=2e-1.
No hypothesis on o_F, reflection runs, nonempty runs or rotation pairs; no multiset-only statement outside the antecedent.

## 1. Word form, selection rule, notation

Group law (v,eps)(v',eps')=(v+eps v',eps eps'), rho_x=(x,+1), sigma_y=(y,-1), x,y in Z_p. By NF (proof-ROT-few-E-v4.md 28-43,
overlays in Sec. 8) an admissible NF u is an avoider of length 4p-2 with the same rotation multiset, written cyclically
R_0 S_0 ... R_p S_p (N:=p+1 runs, block S_i between R_i and R_(i+1)), all blocks odd, sum (l_i-1)/2=e-1, F=p+2e-1,
R=3p-1-2e, empty runs allowed, every empty R_i with y_(i-1)!=y_i. We exclude such u (word form).
GRX (notes-GRX-v1.md 7-20, if direction): all l_i odd give delta_GRX=N-Phi, C_max=Phi+2(e-1); every even C in [Phi,Phi+2e-2]
with 0<=2p-C<=R is admissible. Writing Phi=2m and n=2p-C=2p-2j:
  (SR) admissible j are j in [m, m+e-1] with 0<=2p-2j<=R.
For a set P of runs, z_P:=-1 on P; m(P):=number of maximal cyclic intervals of P; T(z_P)=sum_(i in P) tau_i,
tau_i:=y_i-y_(i-1), tau_i!=0 for empty R_i. Cyclic cuts conjugate products, so order and identity are preserved.
In the SH range 2e<=p-1, so every j in [m,m+e-1] with m>=0 has 2p-2j<=R, and 2p-2j>=0 for m<=e.

## 2. Pairing, dominant class, window [RE-DERIVED for general e]

Lemma M. A multiset of size N' and maximal multiplicity mu has q disjoint unequal pairs if 2q<=N' and q<=N'-mu (cap
multiplicities at q, pair x_i with x_(i+q) in a value-sorted list of 2q capped occurrences).
Lemma P. Every non-constant z has a signed value of multiplicity >=2kappa+1. (n:=max(p-1,2kappa+2-2m) is admissible; if all
multiplicities were <=2kappa=R-(p-1), Lemma M gives p-1 unequal pairs (2(p-1)<=R as e<=(p+1)/2), the R-2(p-1)=2kappa-p+1
unpaired letters contain the n-p+1 fillers, and RS(b) with K=p-1 on the swap differences gives every residue.)
Lemma U. All non-constant z have their dominant value in one class {a,-a}, a!=0 (2(2kappa+1)>R; a=0 is excluded by the
block-value pigeonhole arc with T=0 and n=2kappa).
Orient A:=v_a>=A':=v_(-a); delta:=R-A-A'. d(P):=alpha(P)-beta(P) (letters a minus letters -a in the runs of P), additive.
All-plus: A'<=kappa (n=2kappa+2: kappa+1 letters each of a,-a), and in the SH range A<=2p-1 (n=2p). Write A=2kappa+c,
b:=R-A=p-1-c, lambda:=c-1, Lambda:=2kappa+1-A'. Lemmas P/U give for every proper nonempty P:
  (W) d(P)<=lambda or d(P)>=Lambda; Lambda-lambda=p-2e+3+delta>0.

## 3. Omission windows and the super-heavy run [RE-DERIVED from UH Sec. 4-5 and KP4 Sec. 3-4]

Lemma MW. Let z be non-constant with Phi=2m, s in {a,-a} its dominant signed value with multiplicity phi, W the w0=R-phi other
letters, omega_u:=s_u-s!=0 (signed values), G_s their subset sums. For admissible j put K_j:=R-(2p-2j)=p-1-2e+2j; let q be the
number of admissible j with w0<=K_j<=phi. If q>=1 then w0+q<=p-1.
Proof. For such j and any J in W, omit J and K_j-|J| letters of value s (0<=K_j-|J|<=phi); the 2p-2j selected letters have
sum D-K_j s-sum_J omega (D the total signed sum). The q values K_j s are distinct (the j's differ by <e<p, s!=0); RS(b) gives
|G_s|>=min(p,w0+1) and CD gives >=min(p,w0+q) attained residues. If w0+q>=p, T(z) is attained. []
(MWe) m=e in the SH range: every P with m(P)=e has a dominant multiplicity >=p+kappa.
Proof. The K_j (j in [e,2e-1]) are p-1,p+1,...,p+2e-3, all >=w0 (w0<=p-2 by Lemma P). Write phi=p-1+2r+eps (eps in {0,1},
r>=0; phi>=2kappa+1>=p). If r<=e-2, q=r+1 and w0=2p-2e-2r-eps, so MW needs r>=p-2e+2-eps, whence e-2>=p-2e+2-eps and
3e>=p+4-eps>=p+3: impossible. So r>=e-1, q=e, w0<=p-1-e=kappa-1, phi>=R-kappa+1=p+kappa. []
Hence for m(P)=e: d(P)<=c-e or d(P)>=p+kappa-A', a split with gap p+1+delta; complements swap the two types.
Path. With runs 0..N-1 (N=p+1>=2e+2), single-run toggles keep m=e from P0={0,2,...,2e-2} to its complement: add N-1,
N-2,...,2e (extending the interval of 0); remove 0; for i=1..e-1 add 2i-1 and remove 2i; add 2e-1. (The block [2e,N-1] stays
nonempty; 2e-1 separates 2e-2 from 2e until the last step; 0 and 1 separate N-1 from 2.)
Super-heavy run. Some step goes from the low to the high type across the gap p+1+delta. Removing a run would need
beta_i-alpha_i>=p+1+delta>kappa>=A'. So a run h is added with d_h>=p+1+delta (and alpha_h>=d_h).
Light sets. If a nonempty P' avoiding h were high in (W), alpha(P')>=Lambda and A>=alpha_h+alpha(P')>=3p-2e+2+delta-A', while
A=3p-1-2e-delta-A': impossible. So every nonempty set avoiding h has d<=c-1.
Counts. E:=number of empty runs; Q:=set of nonempty runs other than h holding only letters a; at most b runs other than h hold a
letter !=a. So E+|Q|>=p-b=c+1, and |Q|<=d(Q)<=c-1 when Q is nonempty; hence E>=2.

## 4. Lemma L [NEW]

Let P be nonempty, h not in P, 1<=m:=m(P)<=e, d:=d(P), g:=c-d>=1 (light sets). Under z_P the dominant value is a with phi=A-d,
w0=R-phi=b+d=p-1-g. For admissible j: K_j>=w0 iff j>=e-g/2; K_j<=phi iff j<=(p+1+g)/2. Suppose g<=e-1 and g<=2m-2; we show
q>=g+1, contradicting MW (q>=g+1>=1 forces w0+q<=p-1, i.e. q<=g). Note (p+1+g)/2>=(3e-1+g)/2 as p>=3e-2.
 Case A, m>=e-floor(g/2): j runs over [m, min(m+e-1, floor((3e-1+g)/2))] at least; since m<=e this has >=min(e,
 floor((e+1+g)/2)) elements, and floor((e+1+g)/2)>=g+1 because g<=e-1.
 Case B, m<e-floor(g/2): j runs over [e-floor(g/2), min(m+e-1, floor((3e-1+g)/2))]. If the minimum is m+e-1 the count is
 m+floor(g/2)>=g+1 because g<=2m-2; otherwise it is floor((e-1+g)/2)+floor(g/2)+1>=g+1 because floor((e-1+g)/2)>=g.
Hence g>=min(e,2m-1), i.e. d(P)<=c-min(e,2m(P)-1). []

## 5. Positive selections and the missing set [RE-DERIVED]

B: the b letters !=a; omega_u:=(x_u-a)/(2a)!=0; G: their subset sums (0 included); G_(>=r): sums over >=r elements;
M:=Z_p minus G; |M|<=p-1-b=c (RS(b), K=b) and 0 is not in M.
Lemma S. Let P be a set of EMPTY runs (P empty allowed; m=m(P)), t:=T(z_P)/(2a). For an admissible j put n=2p-2j. If
t+j=sum_J omega for some J in B with max(0,n-A)<=|J|<=min(n,b), u has an identity 2p-subword. In particular, if
n<=A and n>=b (j>=e-c/2 and j<=(p+1+c)/2: "free"), then t+j is in M; if n=A+1 (j=e-(c+1)/2, c odd: "(N1)"), then t+j is not
in G_(>=1), so t+j is in M or t+j=0.
Proof. Every letter keeps its value (no letter in P). J plus n-|J| letters a sums to 2a(n/2+sum_J omega)=2a(-j+sum_J omega)
(mod p); equality with T=2at is the stated condition; SR and GRX. []

## 6. Proof of Theorem A [NEW]

Let 3<=c<=e-1 (SH range); h, Q, E as in Sec. 3; S:=E u Q (runs other than h with d>=0 and no letter !=a). Every P contained in S
has d(P)>=|P n Q|>=0.
(1) No P in S has m(P)=floor((c+1)/2)+1 (this number is <=e): Lemma L would give d(P)<=c-min(e,2m-1)<0, since 2m-1>=c+1 and
e>c. A set in S with more intervals contains a subset with exactly that many. So the independence number of S (on the cycle,
S misses h) is <=floor((c+1)/2).
(2) S is a union of disjoint paths of lengths L_i with sum |S|>=c+1 and independence number sum ceil(L_i/2)>=|S|/2>=(c+1)/2.
With (1): c is odd, |S|=c+1 and every L_i is even. Every run of S lies in a maximum independent set (each even path has two
alternating ones); such a set P has m(P)=(c+1)/2 and Lemma L gives d(P)<=c-min(e,c)=0, so P holds no run of Q. Hence Q is empty
and E=c+1.
(3) For every nonempty set Y of empty runs, m(Y)<=c+1<=e, so j=e is admissible (j in [m,m+e-1]) and free (2p-2e=2kappa<=A and
2kappa>=b as 2e<=p+1+c); Lemma S gives t(Y)+e in M. RS(b) with K=c+1 on the c+1 nonzero values t_i=tau_i/(2a) gives at least
min(p,c+2)=c+2 subset sums, hence at least c+1 nonempty ones, all in M-e. So |M|>=c+1>c: contradiction. []

## 7. Proof of Theorem B (e=5, p>=13) [NEW]

Here R=3p-11, A=2p-10+c, b=p-1-c, |M|<=c, Lemma L reads: sets avoiding h have d<=c-1 (m=1), d<=c-3 (m=2), d<=c-5 (m>=3).
Lengths for a set of empty runs with m intervals: j in [m,m+4]; free iff 2j>=10-c (n<=A; n>=b holds for j<=7 as p>=13);
(N1) at 2j=9-c. All residues used are integers in [-4,10], distinct mod p (p>=13). E>=2; |Q|<=c-1; E+|Q|>=c+1. For a set P
in Q u E: d(P)>=|P n Q|. Theorem A covers c=3,4.
c=5. All-plus: j=3,4 free and (N1) j=2: [2,4] in M. One empty run t: t+{3,4,5} in M, and t+2 in M or t+2=0. If t+2!=0 the four
consecutive residues t+[2,5] avoid 0 and meet [2,4] in >=2 elements (|M|<=5): t=-1 (M contains [1,4]) or t=1 (M=[2,6]); if
t+2=0, t=-2 and t+{3,4,5}={1,2,3}. If some t=1, M=[2,6] excludes 1, so all t=1, and two empty runs (j=5 adjacent, j=6
non-adjacent, both free) put 7 or 8 in M: impossible. So all t in {-1,-2}, M contains [1,4]; a pair needs s+3 in M (j=3 free
for m=1,2), so s=-2 and both t=-1; three empty runs give s+3=0 in M. So E=2, |Q|=4. If Q has >=3 components, one run from each
of three: m=3, d>=3>0; two components: P=Q, m=2, d>=4>2; one component q1q2q3q4: {q1}u{q3,q4}, m=2, d>=3>2. Contradiction.
c=6. All-plus j=2,3,4: [2,4] in M. One empty: t+[2,5] in M meets [2,4] (|M|<=6) and avoids 0: t in {-1,1,2} (giving [1,4],
[2,6], [2,7]=M). Pairs: adjacent needs s+[2,5], non-adjacent s+[2,6]. (-1,-1): 0. (1,1): adjacent gives M=[2,7], non-adjacent
needs 8. (1,2),(2,2): need 8 or more. (-1,1): s=0, [2,6] in M=[1,6]: allowed. (-1,2): M would contain [1,7]: impossible.
Triples: {1,1,1} needs three pairwise adjacent runs; {1,1,-1} gives M containing [1,7]; pairs (-1,-1) excluded. So E=2,
|Q|=5. >=3 components: m=3, d>=3>1; two: P=Q, d>=5>3; one block q1..q5: {q1,q2}u{q4,q5}, m=2, d>=4>3.
c=7. All-plus j=2,3,4 and (N1) j=1: [1,4] in M. One empty: t+[2,5] in M and t+1 in M or 0. If t+1!=0: t+[1,5] avoids 0 and
meets [1,4] in >=2 (|M|<=7), so t in {1,2} (M contains [1,6], resp. M=[1,7]); else t=-1. Pairs (adjacent: s+[2,5], (N1) s+1;
non-adjacent: s+[2,6]): (-1,-1) gives 0; (1,1) adjacent only (non-adjacent needs 8); (1,2),(2,2) need 8; (-1,1) and (-1,2)
allowed. A triple needs all three pairs allowed: at most one -1, the 2 is compatible only with -1, two 1's must be adjacent:
only {-1,1,1}; a fourth empty run is incompatible. So E<=3, |Q|>=5. >=3 components: m=3, d>=3>2; two: d>=5>4; one block of
>=5: {q1}u{q3}u{q5}, m=3, d>=3>2.
c=8. All-plus j=1..4: [1,4] in M. One empty: t+[1,5] in M avoids 0 and meets [1,4] (|M|<=8): t in {1,2,3}. Pairs (adjacent
s+[1,5], non-adjacent s+[2,6]): (1,1) allowed (M contains [1,8]); (1,2) adjacent only (non-adjacent needs 9); any pair with a 3,
and (2,2), need 9 or more. So no t=3 (E>=2), at most one 2. Triples: {1,1,1} with m=1 needs [4,8] (allowed), with m=2
[5,9] or m=3 [6,10] (not allowed); {1,1,2} needs 9. Four empty runs {1,1,1,1}: s=4, m=1 needs 9. So E<=3, |Q|>=6. >=4
components: m=4, d>=4>3; three: P=Q, d>=6>3; two: d>=6>5; one block of >=6: {q1,q2}u{q4}u{q6}, m=3, d>=4>3.
c=9. All j>=1 are free. All-plus j=1..4: [1,4] in M. One empty: t+[1,5] in M, 1<=t<=p-6. If t>=5, M=[1,4]u[t+1,t+5]
exactly, whose only five consecutive residues avoiding 0 form [t+1,t+5]; all empty runs share t, and a pair needs
[2t+1,2t+5] (adjacent) or [2t+2,2t+6] (non-adjacent) equal to [t+1,t+5], i.e. t=0 or t=-1: impossible. So all t<=4 and M
contains [1,t+5]. For a set Y of empty runs with m intervals, s(Y)+[m,m+4] is in M; it must meet [1,t_max+5] (else |M|>=11),
so M contains [1,s(Y)+m+4] and s(Y)+m<=5, where s(Y)>=|Y|>=m. Hence E<=4, and E=4 means four consecutive empty runs with t=1.
|Q|>=10-E>=6. >=5 components: m=5, d>=5>4; three or four: P=Q, d>=6>4; two: a component of length >=3 loses an interior
run, m=3, d>=|Q|-1>=5>4 (two components of length <=2 hold <=4 runs); one block of >=7: {q1,q2}u{q4,q5}u{q7}, m=3, d>=5>4;
one block of exactly 6: then E=4 (four consecutive empties e1e2e3e4), and {q1,q2}u{q4,q5,q6}u{e2} has m=3 (e2's
neighbours e1,e3 are empty and not chosen) and d>=5>4.
Every c=3,...,9 is contradictory. Corollary B follows with UH-A. []

## 8. Scope and interface table

- [RE-DERIVED]: Secs. 1-3 and 5 (pairing, window, MW, the m=e window, the toggle path, the super-heavy run, light sets, counts,
  Lemma S). [NEW]: Lemma L, Theorem A, the e=5 analyses of Theorem B.
- Accepted inputs: NF, GRX (if), RS(b), CD; UH-A only for Corollary B (c<=2). Not used: UH-SH/MW/L/PH/E as imports (SH and MW
  are re-derived), KP3/KP4/R7, PP1/KP2, ASSEMBLY-P, RPdelta, REFL, RUNS, S(p), Lev, (S1), LS-family, CT.
Aroot=/Users/jinleic/repos/aifours; ROT=Aroot/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation;
SR2=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2; R16=Aroot/institute/runs/six-lane-2026-10-16/review;
R18=Aroot/institute/runs/six-lane-2026-10-18-96h/review.
| Input | Text, LF lines, whole-file SHA256 | Accepted scope; use |
|---|---|---|
| NF | ROT/proof-ROT-few-E-v4.md 28-43; ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | R16 lowodd item 2/M1/M4, fewodd addendum 1 line 12, ZX overlays 1-3 |
| GRX | ROT/notes-GRX-v1.md 7-20; afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | R16 lowodd item 1/M2; if direction; C in [Phi,Phi+2e-2] |
| RS(b) | SR2/proof-ROW-v1.md 16-27; a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d; erratum-2-prereq-consolidated.md 36-38; fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5 | R18 CFXT item 4; K=p-1, w0, b, c+1 |
| CD | classical; proof-ROW-v1.md 4-5 | MW translates |
| UH-A | R18/olson-UH-CONSTRAINTS-parent-verdict-v1.md lines 9,15; 7c7b90f2745ba0cb7a8300c3f914a72c4b457259e4fcd45385266db15e4a71e3; errata v1 8f1ea491eb2ab8ab4d4f1006896cb9aad63d6c51e270acb190de7bdaf4074ee3, v2 ac2a7f26ef941366e70e939545bae07a5baea6564005af29e5c9185560aaaa50, v3 0dc678867d10f28abc2f1681b21805658318fa9fc3a4c379062152cc1aef813f | Corollary B only (c<=2 excluded) |
Verdicts (whole-file SHA256): R16/olson-rotation-lowodd-parent-verdict-v2.md 0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29;
R16/olson-zx-s1c-parent-verdict-v1.md 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af;
R16/olson-fewodd-parent-verdict-v1-addendum-1.md 279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a;
R18/olson-CFXT-ROW-LSII-parent-verdict-v1.md ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0.
Context only (not premises): terminal-pplus1-upperhalf-exclusion/obstruction-UH-EXCL-v1.md
f2f1a232c98b3ef6eb45fa0486912bd54170521e5adc00e09c436b1fb8c7849d (R-UH definition, line 44) and its parent errata.
