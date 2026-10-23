# UPAR2 v1: global positive-P elimination, exact jump defect, and a larger uniform exclusion

Owner OlsonThirdCutWindow, SAME throttled math2 slot. Drafted by hand after /bin/date 2026-10-21T06:28:58-0700.
Scope UPAR2-scope-v1.md, SHA256 fb7a82ee074190a10cdba54fd006419d26821d7a3ae952d4c8fae23cb1b5bba4, frozen
2026-10-21T05:51:25-0700; historical exposure expanded by exposure-addendum-1-UPAR2-scope-v1.md. Authority
written-olson-par-cover-followon-v1.json, SHA256 74a6d80c11e403d9d46533076ac79dd11bcd5fddf309cabbf1745bcef28913d5,
LF1-119 (full paths/pins in Sec.8 and the actual numbered primary-source packet).
STATUS: WRITTEN CANDIDATE, NOT REVIEWED OR ACCEPTED. Full T remains OPEN. A STRICTLY LARGER uniform region is proved;
ALL SEVEN named cells are excluded as its instances. The entire positive-balanced-P residual type is excluded on
ALL T. A complete refined late-jump residual remains; JUMP-COVER is the exact first UNPROVED uniform step.

## 0. Exact statements and premise boundary

T: p>=17 prime, floor((p+7)/4)<kappa<=(p-3)/2. The antecedent is a length4p-2 word over D_(2p) without an identity
2p-subword in increasing ORIGINAL index order, with SOME admissible NF, terminal k=p+1,kappa_hat=kappa. Extra
reflection pairs are arbitrary in odd blocks; every empty run separates different reflection values. No o_F,
nonempty-run, rotation-pair or rigidity hypothesis. EVERY frame of EVERY such NF is considered.
Put d=(p+1)/2-kappa>=2. Define the NEW uniform region T2, within T, by
  kappa EVEN: kappa<=8d-2 (equiv9kappa<=4p+2),
  kappa ODD:  kappa<=8d+1 (equiv9kappa<=4p+5).                                      (T2)
THEOREM UPAR2-P. No target NF exists throughout T2. The contradiction works in every frame, not a selected frame.
The accepted old T_PAR={kappa<=4d} union{(10,23),(13,31)} is contained in T2. Containment is strict: (16,37),d3,
even kappa16<=22 lies in T2 but not old T_PAR. This is a uniform parameter theorem, not seven isolated cells.
THEOREM UPAR2-R. Every hypothetical surviving frame on ENTIRE T\T2 induces the complete R2 data of Sec.7, a
fixed-parameter finite relaxation with only late-jump cases. Neither residue class nor high parameters are dropped.
No residual existence, converse, inverse NF characterisation or no-go assertion. The first unproved uniform lemma
is JUMP-COVER (Sec.7), excluding actual NF/frames in that residual. Full T is NOT claimed excluded.
Unlike earlier identity-free count presentations, this proof USES the accepted total identity INSIDE the exact
defect and zero-defect arguments. It does not claim an identity-free count from upper windows alone.

Mathematical premises: accepted UPAR at its exact scoped-partial verdict through parent erratum and cutoff binding;
accepted UMR literal frame/parity/windows/identity/conditional UB/one-way Lemma20; accepted UFC exact cutoffs and
E0/ENV scopes. No reviewer extension is a premise. All new facts below are derived, not taken from the unaccepted
reviewer hint. No other terminal k, full ordered Olson, novelty/priority, human-referee, Lean or runtime claim.

## 1. Literal common data and the inherited full residual

Use the accepted UMR/UPAR notation: h=kappa+d, N=2h=p+1, R=p-1+2kappa=4kappa+2d-2, delta=2kappa-2d. Run letter
OCCURRENCE sets L_i partition R letters, c_l odd nonzero labels, A={c_l<0}, a=|A|, a'=R-a, nu=sum_A|c_l|,
e=sum_all(|c_l|-1). Then nu>=a, e>=nu-a>=0, a'>=(3kappa+2d)/2. For Q, L(Q)=union L_i, l(Q)=|L(Q)|,
Theta(Q)=sum theta_i, n(Q)=nonempty-run count and E(Q)=empty-run count. Put A^c={c_l>0},
beta(Q)=|L(Q) intersect A^c|, beta'(Q)=|L(Q) intersect A|, alpha(Q)=|A\L(Q)| and alpha'(Q)=|A^c\L(Q)|. Literal UMR parity is
  theta_i congruent sigma_i=sum_(l in L_i)c_l congruent |L_i| MODULO2,
not an integer equality of theta_i and sigma_i. Empty theta_i is nonzero even. Consequently
  theta_i>=0 => theta_i+|L_i|>=2; theta_i<=0 => -theta_i+|L_i|>=2.                    (Cost)
For an empty run this is nonzero evenness, for a singleton odd theta has magnitude>=1, and for length>=2 length
alone gives2. This derives the all-run cost, without a fixed-cell lemma.
For central r in[d,kappa+1], every r-subset of either alternating h-run set is proper/independent. Put
  ell_r=2kappa+2-2r, M_r=2r-2d, q(Q)=|L(Q) symdiff A|, q'(Q)=R-q(Q), eps=q mod2,
  x_r=max(eps,ell_r-q,M_r-q'), y_r=max(eps,M_r-q,ell_r-q').
The literal accepted window is
  e-2d+2-nu-y_r(Q)<=Theta(Q)<=-2-nu+x_r(Q).                                         (W)
It also holds for ALL central mixed sets, with r=m(Q), the cyclic interval count. Xi(S)=Theta(S)+nu+d and
  Sigma:=Xi(S_ev)+Xi(S_od)=e>=0.                                                    (ID)
All these primary UMR ranges are included literally, not merely cited transitively, in the numbered source packet:
18-28,49-56,64-68,88-118,137-139,161-165,201-209,238-239,252-258,266-274,300-302,315-324 (including320-321).

Write alpha(Q)=|A\L(Q)|, beta(Q)=|L(Q) intersect A^c|, alpha'(Q)=|A^c\L(Q)|, beta'(Q)=|L(Q) intersect A|.
Then q=alpha+beta, q'=alpha'+beta', l=a-alpha+beta; disjoint run sets have disjoint letter sets. Sort each alternating
set by decreasing theta with fixed arbitrary ties. J_r(S) is its top r, t_r(S) its last value. The upper types are
  G_r: q>=ell_r-1,q'>=M_r-1; Q_r: q<=ell_r-2; P_r: q'<=M_r-2.
They are disjoint/exhaustive since R>ell_r+M_r. On Q/P the respective upper endpoints are
2kappa-2r-nu-q, or 2r-2d-2-nu-q'; on G the bound is<=-1-nu. Q_r with2r>kappa cannot be all nonnegative, by(Cost).

Accepted UPAR defines h=2j-epsilon, epsilon1 for p1mod4, epsilon0 for p3mod4. Then
kappa=2j-d-epsilon, j>=d+2, kappa>=j+2, ell_j=2j-2d+2-2epsilon, M_j=2j-2d.
Its negative-empty cap is: if a<=delta+1 and c=ceil((a+1)/2), each alternating set has<=d+c-1 negative empty runs
(UPAR Lemma2). Its positive-P budget (Lemma3), if t_j=1, is
  z=q'(J_j), L=j-2d-2, nu+z<=L, l(S\J_j)+lambda<=a+z<=nu+z<=L, lambda=l(S'),           (PB)
and the opposite balanced top is negative G_j or Q_j; also a<=L<=delta+1. These are accepted ALL-T statements.

For any hypothetical survivor outside old T_PAR, accepted UPAR-R supplies ALL R_PAR tests, not just its coarse r
range: literal mixed windows/parity/label bounds/reservoir, identity, E0, mass/ENV tests, exact UB failure and BOTH
one-way Lemma20 clauses. In particular either(PB) occurs, or there is an LJ first exit. The complete baseline
R_PAR definitions and CM/DM/ENV formulae are reproduced literally in the numbered packet (UPAR LF216-275), governed
by its erratum: 'no empty tail' means exactly no run of S'\P_(S') is empty. No nonempty-run assumption or converse.

## 2. Positive balanced P is impossible on ALL T

LEMMA 1. No actual target frame has a positive balanced P threshold.
Proof. Accepted(PB) gives t_j=1. Put B=S\J_j, c=ceil((a+1)/2). Every empty run in B has theta<=1 and is nonzero even,
so it is NEGATIVE. The accepted cap applied to S gives E(B)<=d+c-1, hence
  l(B)>=n(B)>=(h-j)-(d+c-1)=j-epsilon-d-c+1.
In S' the cap gives<=d+c-1 negative empties and its negative j-th value permits<=j-1 positive empties. Its at most
lambda nonempty runs therefore give lambda>=h-(d+c-1)-(j-1)=j-d-epsilon-c+2. Add these lower bounds and(PB):
  2j-2d-2epsilon-2c+3<=l(B)+lambda<=L=j-2d-2,
so j-2epsilon+5<=2c. But
  2c<=a+2<=nu+2<=L-z+2=j-2d-z.
Thus2d+z+5-2epsilon<=0, impossible for d>=2,z>=0,epsilon<=1. The cap's hypothesis a<=delta+1 follows from(PB).
Both alternating sets were used. No all-unit assumption, fixed deficiency, selected frame or high-parameter cutoff
was inserted. This eliminates the ENTIRE old positive-P residual branch, not just its small-parameter part. []

## 3. Exact late-jump defect and predecessor bounds

Fix any hypothetical remaining frame outside old T_PAR. By accepted UPAR-R and Lemma1 it is LJ. Let S have the
P_(r+1) first exit, and S' be the other set. Put
  I=J_r(S), K=J_(r+1)(S)=I union{u}, Q=J_r(S'), X=S\K, Y=S'\Q,
  z0=q(I), zP=q'(K), zQ=q(Q), b=2r-kappa, F=4r-2kappa-4d+2=2b-4d+2.
Both predecessor tops are Q_r with negative thresholds, at least one threshold is-1; r+1 is central and r>=j.
The inherited exit condition F>=0 gives b>=2d-1; b is congruent to kappa modulo2. Every theta in X,Y is negative.
Define NONNEGATIVE quantities
  W=beta'(K)+beta(Q),
  sP=(2r-2d-nu-zP)-Theta(K), sQ=(2kappa-2r-nu-zQ)-Theta(Q),
  C=l(X)+l(Y)-2(|X|+|Y|)-Theta(X)-Theta(Y).
The first two are upper-window slacks on the actual P/Q branches; C>=0 by(Cost) on negative tails. Letter partition
algebra gives zP+zQ-l(X)-l(Y)=2W. Adding the top and tail expressions, with h=kappa+d, proves the EXACT identity
  F-e=2W+sP+sQ+C.                                                                (Defect)
Here(ID) is used explicitly to replace Sigma by e. No slack, sign or equality is asserted from a mere inequality.

LEMMA 2 (stronger threshold-1 count). A near-A top J_r with t_r=-1 has n(J_r)>=b=2r-kappa.
Proof. The empty-top estimate and(W) give3n>=4r-2kappa+nu+q=2b+nu+q. Also n<=l<=a+q<=nu+q. Hence3n>=2b+n. []
LEMMA 3 (necessary predecessor inequalities).
(a) If one predecessor threshold is<=-2 and the other=-1, then kappa>=3b+2d+2e.
(b) If both are-1, then kappa>=3b+2d-1+3e/2.
Proof. (a) Accepted QQ-mixed bounds use the PREDECESSOR deficits z0+zQ, not zP+zQ. They give
e<=kappa-r-d-z0-zQ-E(other bottom), with z0+zQ>=n(other top)>=b (Lemma2). Rearrange using2r=kappa+b.
(b) Accepted QQ-1 gives e+nu+E(pred bottoms)<=4kappa-6r=kappa-3b. Set w=beta(Q); then zQ>=w and
l(Q)=a-zQ+2w. The threshold-1 top lower bound and the exact endpoint expression yield
  2r-3l(Q)<=Theta(Q)=2kappa-2r-nu-zQ-sQ,
  2b+nu-3a+4zQ-6w+sQ<=0.
Since nu>=a,zQ>=w, this implies a+w>=b+sQ/2. From(Defect), 2w+sQ<=F-e. Therefore
  a>=b+sQ/2-w>=b-F/2+e/2+sQ>=2d-1+e/2.
Combine nu>=a with the QQ-1 bound to obtain(b). All e terms are the actual label excess from(ID). []

## 4. Zero-defect exits: both mixed orientations impossible; a high threshold for the remaining orientation

Assume F=0 in an LJ actual frame. Then b=2d-1, kappa is odd, r=(kappa+2d-1)/2. From(Defect) every nonnegative
term is zero: e=W=sP=sQ=C=0. Hence every |c_l|=1 and nu=a, as a CONSEQUENCE, not an all-unit hypothesis.
K contains only A^c letters, Q only A; I subset K also contains only A^c. Each run in X or Y is empty with theta=-2
or a singleton with theta=-1: zero signed-cost slack gives theta_i=|L_i|-2<0. Put
  A0=kappa-2d+1, P0=kappa-1; then
  Theta(Q)=A0-a-zQ, Theta(K)=P0-a-zP, Theta(I)<=A0-a-z0,
  z0=a+beta(I), l(Q)=a-zQ, |X|=(kappa-1)/2, |Y|=(kappa+1)/2.                        (Z)
Order theta_u<=-1 implies zP>=z0+b. If t_r(S)<=-2, theta_u<=-2 implies zP>=z0+b+1.
A threshold-1 I gives beta(I)>=a+b; a threshold-1 Q gives a>=b+2zQ. These follow by comparing their top lower
bounds2r-3l with the near-A upper bounds; use2r-A0=2b. No equality of a window is assumed for I.

LEMMA 4 (positive opposite singleton extension). Under(Z), if zQ<=(kappa-8d+3)/4, Y contains no A^c letter.
Proof. Any such letter is a singleton v with theta_v=-1. The INDEPENDENT subset Q union{v} has central size r+1;
it need not be the next sorted top. Its q is zQ+1 and its theta sum is A0-a-zQ-1. At that level ell=A0,M=kappa+1,
so its upper maximum has entries eps<=1, A0-zQ-1 and zQ-3kappa-2d+4. The assumed bound gives
  A0-zQ-1>=3(kappa-1)/4>1,
  zQ-3kappa-2d+4<=(-11kappa-16d+19)/4<0.
Thus the near-A entry dominates and the upper theta is<=A0-a-zQ-3, two below the actual sum. Contradiction. []

LEMMA 5 (no zero exit with mixed predecessor thresholds).
Proof. Let C0=(kappa-4d+1)/2. In either mixed orientation accepted QQ-mixed gives z0+zQ<=C0, since Sigma=e=0.
First let I be strong(t_r(S)<=-2), Q threshold-1. Then a>=b+2zQ and z0>=a, so C0>=b+3zQ, i.e.
zQ<=(kappa-8d+3)/6. If its numerator is negative this is already impossible; otherwise it implies Lemma4's bound.
All runs in X have theta<=-2; under zero tail slack they must be EMPTY. Also zP>=z0+b+1>0, so some positive letter
lies outside K. Q has no A^c letters and X is empty; all such letters must be in Y, contradicting Lemma4.
Next let I be threshold-1 and Q strong. beta(I)>=a+b, so z0>=2a+b and a<=(C0-b)/2=(kappa-8d+3)/4 (a negative right
side is already impossible). This ensures
a<=delta+1 because delta+1-(kappa-8d+3)/4=(7kappa+1)/4>0. Q's negative threshold makes every Y theta<=-2; hence
Y is entirely empty and negative. The accepted cap gives
  (kappa+1)/2=|Y|<=d+ceil((a+1)/2)-1<=d+a/2.
But then kappa+1<=2d+a<=(kappa+3)/4, impossible for positive kappa. Both orientations are excluded. []

LEMMA 6 (zero exit with both predecessors-1). Necessarily
  kappa>=16d-7+8zQ>=16d-7, beta(Y)=0,
  zP>=8d-4+4zQ, zP<=(kappa-1)/2.                                                  (Zero-support)
Proof. The two threshold-1 top estimates in(Z) give a>=b+2zQ and beta(I)>=a+b. Thus z0>=2a+b; order gives
zP>=z0+b>=2a+2b>=4b+4zQ=8d-4+4zQ. Since zP<=M_(r+1)-2=kappa-1, obtain zQ<=(kappa-8d+3)/4. Lemma4 gives
beta(Y)=0. All positive letters outside K are then in X, and zP counts exactly those letters because K has no A.
The zero-slack tails have at most one letter per run, so zP<=|X|=(kappa-1)/2. Combine with the preceding lower bound.
The lemma is a NECESSARY condition, not a statement that a large-parameter zero exit exists. []

## 5. The larger uniform theorem and all seven required cells

PROOF OF UPAR2-P. The old accepted T_PAR is contained in T2: kappa<=4d lies in either parity cutoff for d>=2, and
the two exceptions(10,23),(13,31) have d2,d3 and satisfy their respective new cutoffs. Use its accepted exclusion
there. On the ENTIRE old complement a hypothetical survivor has R_PAR data. Lemma1 eliminates its positive-P type,
so it is LJ. At least one predecessor threshold is-1; both strong are already excluded by accepted QQ bounds.
If F=0, Lemmas5-6 force odd kappa>=16d-7, larger than8d+1 since d>=2. This cannot be in T2.
If F>0 and kappa is even, b is even and b>=2d; Lemma3 requires kappa>=8d-1 in the both-minus1 case, hence >=8d
by evenness, and >=8d directly in the mixed case. Both contradict even kappa<=8d-2.
If F>0 and kappa is odd, b is odd and b>=2d+1. Lemma3 requires kappa>=8d+2, hence >=8d+3 by oddness, or >=8d+3
directly in the mixed case. Both contradict odd kappa<=8d+1. No actual frame exists in the new region. A target NF
always has a frame, so no target NF/word exists. EVERY frame was covered, not a specially chosen one. []

All seven named cells are instances of this UNIFORM theorem; no local result is extended to a uniform lemma.
| (kappa,p) | d | kappa parity; allowed upper kappa | word/group; terminal k | Written outcome |
|---|---|---|---|---|
| (13,29) | 2 | odd;17 | length114/D58;k30 | PROVED |
| (14,31) | 2 | even;14 | length122/D62;k32 | PROVED |
| (17,37) | 2 | odd;17 | length146/D74;k38 | PROVED |
| (16,37) | 3 | even;22 | length146/D74;k38 | PROVED |
| (17,41) | 4 | odd;33 | length162/D82;k42 | PROVED |
| (18,43) | 4 | even;30 | length170/D86;k44 | PROVED |
| (20,47) | 4 | even;30 | length186/D94;k48 | PROVED |
The full existential NF/original-order/extra-pair/empty-run quantifiers of Sec.0 apply to every row. The extension
is not claimed independent corroboration of any earlier same-author cell work. All new proofs await parent review.

## 6. Complete refined residual on ENTIRE T\T2

Define R2 for each fixed (kappa,p) by the following INTERSECTION, with no omitted old tests. This is a numerical
relaxation for actual NF/frames, not an existence assertion, inverse theorem or characterisation of avoidance.
(1) Keep EVERY corrected R_PAR condition (literal UPAR LF216-275 with its mandatory erratum and notation binding):
odd labels/occurrence partition; full modulo2 run parity; |theta|<2p and max|c|<=p-6/reservoir; ALL central mixed
windows; ID; E0; mass/ENV bounds; exact UB failure and BOTH one-way Lemma20 clauses. The boundary means exactly
'no run of S'\P_(S') is empty'. The literal UMR UB/Lemma20 source ranges, including320-321, are in the packet.
Replace the parameter set by T\T2; this is inside old T\T_PAR. No B,ENV,empty-run,lower-window or giant test is deleted.
(2) Positive balanced P is excluded by Lemma1, on ALL T. Thus the old R_PAR(P+) type is removed BY PROOF, not by
silently narrowing the assignment. Keep its entire LJ type: fixed consistent sorted ties, both Q chains from j to r,
first near-A^c exit at r+1, no generic-only earlier exit, only one P exit, negative thresholds and at least one
predecessor exactly-1, deduced beta(u)>=2kappa+4d-2. The inherited r interval is only a COARSE NECESSARY superset:
  max(j,ceil((kappa+2d-1)/2))<=r<=kappa-d-1.
All old QQ-1/QQ-mixed inequalities apply at that predecessor and remain required, not just the both-strong test.
(3) Define b,F,W,sP,sQ,C exactly as in Sec.3. Require their nonnegativity and exact(Defect). For every threshold-1
near-A predecessor retain n>=b. If both thresholds are-1, retain all the inequalities of Lemma3(b), in particular
  a>=2d-1+e/2 and kappa>=3b+2d-1+3e/2.
For a mixed pair retain kappa>=3b+2d+2e, together with the unweakened QQ-mixed deficits/counts from the baseline.
These are one-way tests. There is no assertion that parameters passing only one scalar inequality survive the others.
(4) If F=0, BOTH predecessors must be-1 (Lemma5). Require all zero consequences(Z), beta(Y)=0 and
  zP>=8d-4+4zQ, zP<=(kappa-1)/2, kappa>=16d-7+8zQ,
as well as e=0, unit labels DERIVED, W=sP=sQ=C=0 and the empty-2/singleton-1 tail conditions. If F>0 retain both
possible predecessor sign orientations and all defect tests; necessarily even kappa>=8d or odd kappa>=8d+3.
No high-parameter or parity class is discarded. F0 at very large odd kappa and F>0 cases both remain open.

THEOREM UPAR2-R (proof). Every hypothetical survivor outside T2 has all baseline R_PAR data by accepted UPAR-R.
Lemma1 rules out(P+). The new exact defect, predecessor and zero-exit lemmas prove every additional test(2)-(4).
Thus every surviving frame induces R2. Conversely is NOT claimed; other NF/generator/block-value constraints may
still prevent a tuple from occurring. Finiteness is ONLY for EACH FIXED (kappa,p), using the literal coefficient/
theta bounds. The unbounded union is not asserted finite. []
FIRST UNPROVED UNIFORM LEMMA, JUMP-COVER: no actual target NF/frame on T\T2 induces R2. This has NOT been proved.
It is the full remaining target, expressed as a stricter complete late-jump relaxation, not a proved reduction in
logical difficulty, no-go result, necessary mathematical obstruction, residual existence or converse. Full ordered
Olson, other terminal k, reflection rigidity and inverse/o_F assembly are outside this claim.

## 7. Source binding, exposure and schedule

Every mathematical import is at its accepted literal scope. The REQUIRED actual numbered packet contains the new
proof, scope/addendum and all used primary ranges with original LF numbers, whole-file SHA256 and absolute paths.
It is not replaced by a manifest. Primary UMR fields, especially parity/windows/UB/Lemma20, are provided literally,
not inferred to have been read from a transitive citation or an earlier model's reference to LF202.
| Input | Absolute path; whole-file SHA256 | Inclusive LF used |
|---|---|---|
| Authority | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-olson-par-cover-followon-v1.json; 74a6d80c11e403d9d46533076ac79dd11bcd5fddf309cabbf1745bcef28913d5 | 1-119 |
| Scope | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-par-cover-followon/UPAR2-scope-v1.md; fb7a82ee074190a10cdba54fd006419d26821d7a3ae952d4c8fae23cb1b5bba4 | 1-86 |
| Historical exposure addendum | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-par-cover-followon/exposure-addendum-1-UPAR2-scope-v1.md; cb4dcf7a35f03d4c77c3dda4c6ddfa5d3f0201d4300c2cbdb02e7c41e5e23e8a | 1-13 |
| Accepted UPAR verdict | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UPAR-parent-verdict-v1.md; 1d13a0ca4fed3e652378e1f72b9e0802d9cd116b0344733091cdb14b45be5f40 | 1-11 |
| UPAR erratum | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UPAR-parent-erratum-v1.md; 69374d0748e124708d4e9b699f4f777f1b573ed777f6f39fbb5fbe29ba1aa819 | 1-15 |
| Literal cutoff/notation binding | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UPAR-cutoff-binding-and-notation-v1.md; fdffe1d80e65c31a8e6bb02e246304d7cf0a5792bb85ec12b1e4daf6935de3f3 | 1-9 |
| UPAR primary | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-full-uniform-parity/proof-UPAR-v1.md; f75d55674586b714c12f8ffeb6e57ef0fee9ffc4615e96c7b0def522501cbcef | 66-122,146-155,216-275 |
| UMR verdict | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-verdict-v1.md; a2535971cb214e399433235a4b9fca2de7328d15bec2c2f4eece35c05456c772 | 1-26 |
| UMR erratum1 | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-erratum-v1.md; b83313b3fe828ee19a0902e9a5149db42ee55318500f92bac577b4bbd7088c5f | 1-10 |
| UMR erratum2 | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-erratum-v2.md; 2a5f142ef136b04c15304137a4ba19946d0fee115ce18e8660817cd25bc902a2 | 1-9 |
| Literal UMR primary | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-middle-range/proof-UMR-v1.md; c403bfbae9f1c7b75698010cae78515a253154e689336e79006c588ff15023a9 | 18-28,49-56,64-68,88-118,137-139,161-165,201-209,238-239,252-258,266-274,300-302,315-324 |
| UFC verdict | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UFC-parent-verdict-v1.md; 10596e3df9eab24f0451910eb84ae3029721c60a211f9b4b22d5fff943d0c060 | 5-14 |
| UFC erratum | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UFC-parent-erratum-v1.md; b2719ef394c2920d144f39ff2b4a8752eab05161aa67226308309edaf88af40e | 1-6 |
| Literal UFC cutoff/E0/ENV | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-fc/proof-UFC-v1.md; 2d03076c9bbf1afa3d68e42bfc2fe9eeb4a62ee64b59e6c94c53f65a32b670c5 | 23-27,200-225 |

The literal UFC T0 cutoffs are +5/+7 numerators, not UPAR's newly defined +9/+11 T1. Old T_PAR is used in its
canonical accepted form, including the two existing family exceptions; no new independent corroboration is claimed.
The reviewer note /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UPAR-primary-complete-claude-v1.prompt.note.md,
SHA256 d8400a6da7172c9229efc7a3cd432959ef3d69bd893661efb444b3c09c70a8dc, LF1-210, was read only after freeze.
Its optional extension at LF205-210 is NOT a premise. The stronger bounds here were independently derived; no
model's unaccepted numeric suggestion is promoted. Primitive mathematical inputs are ONLY those at UMR verdict
LF24 through UMR; no FCW/balfull theorem promoted. Prior same-author unpublished p29 reasoning is disclosed in the
addendum, not treated as a proof or strict preregistration. The general zero-exit lemmas are written in variables,
not extrapolated from an old cell. No new derivation before the recorded freeze and no external/model contact.
All mathematics by hand; metadata-only clock/hash/byte/LF and source-numbering operations disclosed in the package.
New derivation must stop08:40PT and handoff09:00PT at latest; actual creation/binding times are in checkpoints.
