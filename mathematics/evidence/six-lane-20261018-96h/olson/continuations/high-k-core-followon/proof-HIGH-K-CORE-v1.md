# HIGH-K-CORE v1: candidate auxiliary necessary structure; HIGH-K-CORE-COVER NOT_PROVED

CANDIDATE written mathematics by hand; no parent/model gate has been run on it. Outcome category (c):
HIGH-K-CORE-COVER is NOT_PROVED, and NONE of the three mandatory uniform diagnostic families (LOW-CORE,
TOP-CORE, P-CRITICAL-DIAGONAL) is excluded. The new lemmas below are proved NECESSARY CONSEQUENCES of the
exact general-GRX condition (R2); because GRX is an exact criterion they prove that certain data subclasses of
HIGH-K-RES contain no actual NF, but they leave the HIGH-K-RES set itself unchanged. They are auxiliary filters,
not an exclusion region, residual replacement, feasibility statement, converse or classification.

Operative scope: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-olson-high-k-core-followon-v1.json
(SHA256 5b1bb517765e2c247679538ce25ad344f5f050bafb0511337531882dc4131b3f). Acknowledgement published before
any new reasoning; its governing-input count "16" is corrected to 15 in checkpoint01 (clerical). All permanent
process history (UPAR4 MAJOR, parent enumeration MAJOR, both terminal-k pre-ack MINORs, parent lower-terminal
scope MAJOR, clerical defects, initial HK1 P-source coverage history) remains uncured. Re-derived after
disclosed exposure; no independent-discovery, strict-preregistration, corroboration or priority claim.

## 0. Target, imports and what is NOT claimed

Target (scope LF8): every actual target NF in the ENTIRE unbounded HIGH-K-RES of accepted HK1 Sec.6 through all
governing errata: prime p>=7, SOME admissible terminal NF u of an increasing-original-index identity2p-subword
avoider of length4p-2, 2<=kappa<=p-1, p+2<=k<=p+2kappa, full(R0)-(R3). Here kappa means kappa_hat. Arbitrary
h_i pairs, exact occurrence data, the genuine empty-gap rule and zero rotation LETTERS (distinct from absent
gaps) are retained; no original-o_F, nonempty-run, rotation-pair or rigidity premise is added; only the
original-to-NF avoidance direction is used. This is ONE independent high-k class, not the only open gap.

Imports used, all at literal accepted scopes: HK1 verdict items3-4 with worker erratum1 and parent errata1-3
(the residual data, the exact GRX form (G) and the TOP necessary near-pair statement); general GRX at its own
lowodd-v2 acceptance; general NF data through HK1 (R0) and its own accepted chain; classical Cauchy-Davenport.
Theorem P enters only through HK1's literal (R1) gap floor and, in Sec.4, as a description of its own proof's
parameter count (a failed-step statement, not a new use). S(p) and lane CT are NOT used by any new lemma; the
residual's lower boundary kappa>=2 inherits S(p)'s secondary-statement trust through HK1. No Lev, special
k=p+1 UMR/UPAR lift/window/frame, FB-p/ARC0 word theorem, rotation-rigidity transfer or computation.

## 1. Literal data and the exact criterion

From accepted HK1 Sec.1/Sec.6: u = R_1 S_1 ... R_k S_k cyclically, S_i = sigma_(y_i)^(2h_i+1), r_i=|R_i|>=0,
r_i=0 implies y_(i-1)!=y_i, H=sum h_i=p-1-kappa, F=k+2H, R=2p+2kappa-k, and the TheoremP gap floor
Pgap=sum floor(r_i/2)<=p+2kappa-k. For z in{+1,-1}^k (z_i the sign of run R_i) let P={i: z_i=-1} be the
minus set, m(P) its number of maximal cyclic intervals, Phi=2m(P) for proper nonempty P (Phi=0 for P empty),
tau_i=y_i-y_(i-1) and T(P)=sum_(i in P) tau_i; this equals HK1's T(z)=sum_(z_i=+1)(y_(i-1)-y_i) because
sum_i tau_i=0. X^P is the multiset of SIGNED rotation values (value x in run i counted as z_i x). Then (G):
  u has an identity2p-subword iff for some P and some EVEN n with
  max(0,2kappa+2-Phi)<=n<=min(R,2p-Phi), some n rotation letters of X^P have signed sum T(P).
Complements: T(P^c)=-T(P), X^(P^c)=-X^P, m(P^c)=m(P). Actual distinct letters are always used.

Put delta:=p+2kappa-k. Since p+2<=k<=p+2kappa, 0<=delta<=2kappa-2, and the literal formulas give
  F=3p-2-delta, R=p+delta, Pgap<=delta.                                              (D)
Thus the P-CRITICAL-DIAGONAL k=p+2kappa is exactly delta=0: F=3p-2, R=p, every r_i<=1, so exactly p gaps hold
ONE rotation letter and the remaining k-p=2kappa gaps are genuinely empty.

## 2. ZERO lemma (every core cell)

Let z0 be the number of rotation LETTERS of value0 (an empty gap is not a letter).

LEMMA Z1. In every HIGH-K-RES cell, z0<=2kappa-1.
Proof. k>=p+2>p labels in F_p give blocks j!=j' with y_j=y_(j'). Let P be the cyclic run interval
R_(j+1),...,R_(j'): proper, nonempty, m(P)=1, Phi=2, T(P)=y_(j')-y_j=0. Its window is even n in
[2kappa,min(R,2p-2)]. If z0>=2kappa, take n=2kappa zero letters: signed sum0=T(P), and 2kappa<=z0<=R,
2kappa<=2p-2. (G) gives an identity2p-subword, contradicting avoidance. []

LEMMA Z2. If moreover kappa<=(p-1)/2, then z0=0 or z0>=delta+2.
Proof. Suppose 1<=z0<=delta+1. Then at least R-z0>=p-1 letters are nonzero. Since 2kappa+2<=p+1<k,
choose any 2kappa+2 distinct blocks and let P be the minus set of the pattern changing exactly there
(determined up to complement): Phi=2kappa+2, so the window is even n in[0,min(R,2p-2kappa-2)]; here R>=p and
2p-2kappa-2>=p-1, so every even n<=p-1 is admissible. Take p-1 nonzero letters; their signed values
s_1,...,s_(p-1) are nonzero. Iterated Cauchy-Davenport gives |{0,s_1}+...+{0,s_(p-1)}|>=min(p,p)=p, so some
index set I has sum_I s_i=T(P). If |I| is odd then |I|<=p-2; add one zero letter (distinct from the chosen
ones). The resulting even n<=p-1 lies in the window with the same signed sum. (G) gives an identity. []

COROLLARIES. (i) For kappa<=(p-1)/2, z0 in{0} union [delta+2,2kappa-1]. (ii) Every k=p+2 cell with
2<=kappa<=(p-1)/2 has delta=2kappa-2, hence z0=0; in particular EVERY LOW-CORE NF (k=p+2,kappa=2, p>=7) has
no zero rotation letter. (iii) On the diagonal (delta=0) with kappa<=(p-1)/2: z0 in{0} union [2,2kappa-1].
(iv) For kappa>=(p+1)/2 only Z1 is proved. These exclude no parameter cell.

## 3. TOP-CORE: candidate necessary structure (k=p+2, kappa=p-1)

### 3.1 Specialisation and accepted input

Here H=0: every block is ONE reflection sigma_(y_i), F=p+2, R=3p-4, and (G) fixes n=2p-Phi (C=Phi). Every
proper nonempty run set P, and P empty, is an admissible pattern (Phi<=p+1<=2p, n<=2p<=R).
Accepted HK1 verdict item3 (from HK1 Sec.5): there is a nonzero a such that every pattern with Phi>=4 has a
signed value of multiplicity>=2p-2, lying in the common original unsigned pair{a,-a}, and at most p-2 rotation
letters have value outside{a,-a}. For lambda in F_p^* the map (v,e)->(lambda v,e) is an automorphism of D_(2p)
preserving letter order, blocks, the empty-gap rule and identity subwords; use it to put a=1 (and below
possibly lambda=-1). This normalises only the given NF word u; nothing is transferred to the original word.

For run i let alpha_i, alpha'_i, d_i count letters of value1, -1, other ("deviants"); A=sum alpha_i,
A'=sum alpha'_i, D=sum d_i<=p-2, A+A'+D=3p-4, g_i=alpha_i-alpha'_i, G=A-A', G_P=sum_(i in P) g_i. Then
  S_+(P)=sum_(i notin P)alpha_i+sum_(i in P)alpha'_i,  S_-(P)=sum_(i notin P)alpha'_i+sum_(i in P)alpha_i
count the signed values +1/-1 in X^P, S_++S_-=3p-4-D, and Delta(P):=S_+-S_-=G-2G_P. Signed deviants are
never+1/-1. HK1 item3 gives, for m(P)>=2: max(S_+,S_-)>=2p-2, equivalently
  |Delta(P)|>=2(2p-2)-(3p-4-D)=p+D.                                                 (H)

### 3.2 LEMMA W (exact reformulation for heavy patterns)

If a pattern P has Phi>=2 and S_+(P)>=2p-2, then u has an identity2p-subword with this pattern iff
  T(P)+Phi in Sigma(W_P),   W_P := multiset{xhat-1 : xhat in X^P, xhat!=1}  (all elements nonzero),
where Sigma denotes the set of ALL subset sums (empty sum0). Proof. n=2p-Phi<=2p-2<=S_+, and the letters of
signed value!=1 number 3p-4-S_+<=p-2<=p-1<=n. Any V among them (|V|<=n) completes with n-|V| signed-1 letters
to sum n+sum_V(xhat-1); conversely every n-selection splits so. As n=2p-Phi, T-n=T+Phi mod p. []
(The heavy -1 case is the same statement for the complement P^c.) This is an exact criterion for ONE pattern,
not a feasibility or converse statement about HIGH-K-RES.

### 3.3 LEMMA BIG-RUN

Some single run q has |g_q|>=p+D.
Proof. Index runs mod N=p+2>=9. Take X0={1,5}. Grow X0 one run at a time to Xa=all\{2,6}; then pass
Xb=all\{1,2,6}, Xc=all\{1,6}, Xd=all\{1,5,6}, Xe=all\{1,5}=X0^c, each step changing one run. Every set
here has m>=2: for {1,5}subset X subset all\{2,6}, the complement contains 2 and 6 but not1 or5, so the
complement interval through2 lies in[2,4] and the one through6 in[6,N]; Xb..Xe have complements
{1,2}u{6}, {1}u{6}, {1}u{5,6}, {1}u{5}, pairwise non-adjacent pieces because N>=9. So(H) holds at every
step. Delta(X0^c)=-Delta(X0), and Delta never vanishes, so some step X->X' with X'=X xor{q} changes the sign
of Delta across the gap(-(p+D),p+D); then 2|g_q|=|Delta(X)-Delta(X')|>=2(p+D). []
Normalise with lambda=-1 if necessary so that g_q>=p+D. Then alpha_q>=p+D+alpha'_q>=p.

### 3.4 All-plus consequences and LEMMA SIDE

The all-plus pattern (P empty, Phi=0, n=2p, T=0): 2p letters of value1 would sum to0, so A<=2p-1; since
A>=alpha_q>=p, p letters1 plus p letters-1 would sum to0, so A'<=p-1. With O:=A-alpha_q,
  O<=p-1-D-alpha'_q,   A'+O=3p-4-D-alpha_q<=2p-4-2D.                               (AP)

LEMMA SIDE. If m(P)>=2 and q notin P, then S_-(P)<=p-2-D and S_+(P)>=2p-2; if m(P)>=2 and q in P, then
S_+(P)<=p-2-D and S_-(P)>=2p-2. Proof. For q notin P every signed-(-1) letter is a value-(-1) letter outside P or
a value-1 letter in P, the latter outside run q; so S_-(P)<=A'+O<=2p-4-2D<2p-2. By(H) S_+(P)>=2p-2 and
S_-(P)=3p-4-D-S_+<=p-2-D. The other case is the complement. []
Hence Lemma W applies to EVERY multi-interval P not containing q, with |W_P|=S_-(P)+D<=p-2.

### 3.5 LEMMA BALANCE (Phi=2)

Let P be a Phi=2 pattern with S_+(P),S_-(P)<=2p-2-D. If D>=1, u has an identity2p-subword. If D=0,
avoidance forces T(P) equal to 2S_+(P)+4 mod p.
Proof. n=2p-2. For a set E of e signed deviant letters, choose i signed-1 and j signed-(-1) letters with
i+j=n-e. Because S_+,S_-<=n-e, i ranges over the N_e=S_++S_--(n-e)+1=p-1-D+e consecutive integers of
[n-e-S_-,S_+], and the signed sum sigma(E)-(n-e)+2i runs through N_e<=p-1 distinct terms of a step-2
progression whose complement is the next p-N_e terms. For E the full deviant set (e=D) exactly one residue is
missed: mu=sigma_D-(n-D)+2(S_++1); avoidance needs T(P)=mu. If D=0 this is mu=2S_++4. If D>=1, drop one
deviant of signed value d (e=D-1, N=p-2): the missed residues are mu-d-1 and mu-d+1, so avoidance would need
d in{1,-1}, impossible for a deviant. Both selections use distinct actual letters. []

### 3.6 Exact failed step at TOP-CORE

For P not containing q with m(P)>=2, avoidance is EQUIVALENT (Lemma W) to T(P)+2m(P) notin Sigma(W_P), where
|W_P|<=p-2. Cauchy-Davenport gives only |Sigma(W_P)|>=|W_P|+1<=p-1, so no single pattern forces an identity.
A cover needs to couple the label sums T(P) across many patterns (with sum tau_i=0 and the empty-gap rule),
together with the Phi=2 and all-plus tests. That coupling argument is NOT supplied. TOP-CORE remains open;
the old Phi2 one-filler failure of HK1 is unchanged and Lemma BALANCE only removes BALANCED Phi2 patterns
when D>=1 (and fixes T when D=0). No full rotation rigidity, no TOP exclusion, no feasible configuration.

## 4. LOW-CORE and P-CRITICAL-DIAGONAL: proved facts and concrete failed steps

LOW-CORE (k=p+2,kappa=2; H=p-3, F=3p-4, R=p+2, delta=2, Pgap<=2): Corollary (ii) gives z0=0. For every
pattern with 6<=Phi<=p-1 the window is every even n<=p+1, i.e. ALL even-size signed sub-multisets, because R=p+2
is odd and 2p-Phi>=p+1; so avoidance there is exactly T(P) notin E(X^P), the set of all even-size signed subset
sums. FAILED STEP: HK1's kappa1 COLOR argument needs pure reflection identities of length4 to be forbidden; at
kappa2 the pure window starts at2kappa+2=6, so the interlaced ABAB/C=2A-B selection (length4) is allowed, and
HK1's size-2 cancellation lies below the Phi2 window[4,p+1]. No lower bound for |E(X^P)| strong enough to
reach Z_p is proved here. LOW-CORE is NOT excluded.

P-CRITICAL-DIAGONAL (k=p+2kappa, delta=0): F=3p-2, R=p, every r_i in{0,1}, exactly2kappa empty gaps; for
kappa<=(p-1)/2, z0 in{0}u[2,2kappa-1] by Corollary (iii). FAILED STEP: in Theorem P's own Boolean-box proof the
parameter count is M=(F-1)+sum floor(n_t/2)=3p-3 (every gap has at most one rotation), while its degree bound is
deg Q<=3(p-1)=M; the box lemma needs deg Q<M, so the method is exactly one parameter short. Adding a variable
for an isolated rotation keeps V linear only with rules 'select iff e XOR u_t', whose size parity contributes
e+u_t and is not identically even (each gap has one rotation); pairing isolated rotations of different gaps
makes V quadratic and leaves M=(7p-7)/2<4p-3. These are method failures, not no-go theorems. NOT excluded.

## 5. ENTIRE residual, diagnostics and exact first unproved lemma

The necessary system is UNCHANGED: HK1 HIGH-K-RES (R0)-(R3) literally, through worker erratum1 and parent
errata1-3, for every prime p>=7, 2<=kappa<=p-1, p+2<=k<=p+2kappa, with all actual NF data, genuine empty gaps,
zero letters, the full gap floor, EVERY sign pattern/admissible even n of (G), and CT only at its literal original
all-plus domain. Proved auxiliary necessary consequences (derived from (R2), not replacements): Z1/Z2 and their
corollaries in every cell; in TOP-CORE, BIG-RUN, the normalised (AP) bounds, SIDE, W and BALANCE, together with
HK1's accepted CT-top and Phi>=4 near-pair tests. They prove emptiness of the stated data subclasses only.

| Uniform family, all primes p>=7 | Outcome |
|---|---|
| LOW-CORE k=p+2,kappa=2 | NOT excluded; proved z0=0; failed step Sec.4 |
| TOP-CORE k=p+2,kappa=p-1 | NOT excluded; proved BIG-RUN/SIDE/W/BALANCE; failed step Sec.3.6 |
| P-CRITICAL-DIAGONAL k=p+2kappa | NOT excluded; proved zero restriction for kappa<=(p-1)/2; failed step Sec.4 |

FIRST UNPROVED LEMMA (unchanged): HIGH-K-CORE-COVER, no actual target NF in the entire unbounded HIGH-K-RES.
Outcome (c) NOT_PROVED. No full terminal k>=p+2 exclusion, no lower-terminal/original-o_F>p assembly, no full
ordered Olson, no p=5 statement, no feasibility/existence/converse/inverse-NF claim, no human/Lean/runtime claim.
All arguments are by hand; no scientific computation, enumeration, solver, test, model or network was used.
