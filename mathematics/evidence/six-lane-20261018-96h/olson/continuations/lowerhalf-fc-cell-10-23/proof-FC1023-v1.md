# FC1023 v1: the full (kappa,p)=(10,23) terminal cell, using run parity and upper windows

Owner: OlsonThirdCutWindow (same throttled math2 slot). Drafted by hand after /bin/date 2026-10-20T20:44:03-0700.
Scope FC1023-scope-v1.md, SHA256 190f9656606750f184963724d211bfaaf7165b05e7dc16c3fe5d78397d3cdf1e, frozen
2026-10-20T20:35:36-0700 before any NEW local derivation. Authority written-olson-fc-cell-10-23-transition-v1.json,
SHA256 efa20631f20ea4970627ff06e326bc0547cbc4ea5caa95a6303e05e29ea15aea, LF1-59 (absolute paths in Sec. 6).
OUTCOME: FULL CELL PROOF COMPLETE, relative to accepted UMR at literal scopes. Written candidate, NOT yet reviewed
or accepted. No unproved local step or residual is left. Every frame is covered, not just an illustrative hybrid.
No UFC lemma is a premise, and no claim about another cell, prime, kappa, terminal k or full ordered Olson is made.

## 0. Exact statement and premise boundary

THEOREM FC1023. No word w of length90 over D_46 without an identity46-subword in increasing original index order
has SOME admissible NF with terminal k=24 and kappa_hat=10. Extra reflection pairs may lie anywhere in the odd
blocks; every empty NF run separates different reflection values. No o_F, nonempty-run, rotation-pair or rigidity
hypothesis is added. The count proves Xi(S_ev)+Xi(S_od)<=-1 in EVERY frame of EVERY such NF.

Only accepted UMR (verdict a2535971..., through parent errata v1 and v2) supplies the mathematical premises. The
cell lies in its exact range: floor((23+7)/4)=7<10=(23-3)/2. Use the frame, odd labels and Lemma5(c),(d), Lemma2
windows, Lemmas7-8 upper representatives, UMR-F/Lemma13 identification U'=Theta, Lemma10's FULL run parity and
nonzero-even empty theta, and Lemma14 total identity. The restricted Lemma13 connectivity link is respected.
No UMR Lemma15-20, UB, RES, saturation or converse is used. No UFC lemma (including E0/ENV) or accepted FC717/FC19
internal lemma is used. Their authorship/method exposure and the untrusted parent check are disclosed, not premises.

COUNT LEMMA WC1023. The reduced integer data (A1)-(A3) of Sec.1 alone imply Xi(S_ev)+Xi(S_od)<=-1. The total identity
(A4) is used only after proving this count, to contradict e>=0 and exclude the word/NF. Thus the argument covers all
frames that would be in the candidate R23, but does NOT assume R23 membership or any selected certificate failure.

## 1. Literal UMR data and elementary facts

N=24, R=42, 2p=46, g=4, d=g/2=2, h=12, delta=16, H=12 (UMR LF18-19,49-51). Central levels are2..11. Fix ANY
admissible target NF and ANY of its frames; a frame exists and the properties hold in every frame (UMR LF111-112).
(A1) The sets L_i of letter OCCURRENCES of the 24 runs partition 42 letters. Each letter l has an odd nonzero label
c_l (UMR LF88-110). Put A={l:c_l<0}, A^c={l:c_l>0}, a=|A|, a'=42-a, nu=sum_A |c_l|, B=sum_all |c_l|, e=B-42.
Then nu>=a, e>=0 (as |c_l|>=1) and a'>=(p+kappa+1)/2=17 (UMR Lemma5(d), LF118). For a run set Q put L(Q)=union_(i in Q)L_i,
l(Q)=|L(Q)|, Theta(Q)=sum_(i in Q)theta_i. All cardinalities count occurrences, not residue values.
(A2) Every theta_i is an integer with
  theta_i = sigma_i = sum_(l in L_i)c_l = |L_i| (mod2),                              (Parity)
by UMR Lemma10 LF201-203 and the integer sigma_i definition LF109-110; the last equality is from odd c_l.
If L_i is empty, theta_i is NONZERO EVEN (UMR Lemma10 LF203,208-209). Nonzero is load-bearing, and parity for
NONEMPTY runs is also used; it is not replaced by only the empty-run rule.
(A3) S_ev={0,2,...,22}, S_od={1,3,...,23}, each of 12 pairwise non-adjacent runs. Every 6- or7-subset Q of either
is a proper independent central set (UMR LF55-56,252-254). Put
  q(Q)=|L(Q) symdiff A|, q'(Q)=42-q(Q) (UMR Lemma5(c), LF117-118),
  chi6(Q)=max(1,10-q(Q),8-q'(Q)), chi7(Q)=max(1,8-q(Q),10-q'(Q)).
For every such subset:
  |Q|=6: Theta(Q)<=-2-nu+chi6(Q);  |Q|=7: Theta(Q)<=-2-nu+chi7(Q).                   (U6/U7)
Indeed UMR Lemma2 LF64-68 gives (ell6,M6)=(10,8), (ell7,M7)=(8,10). Lemmas7-8 LF137-139,161-165 give upper
-2-nu+x_r with x_r=max(q mod2,ell_r-q,M_r-q'); replacing q mod2 by1 only WEAKENS this upper bound. UMR-F/Lemma13
LF238-239 identifies U'=Theta. No new realisation claim or extension of a window is imported.
(A4) Xi(S)=Theta(S)+nu+2 (UMR LF254). UMR Lemma14 LF256-258 gives Xi(S_ev)+Xi(S_od)=e>=0. Equivalently UMR-F gives
Theta(all)=B-2nu-46=e-2nu-4. WC1023 uses (A1)-(A3), NOT this identity, until Sec.5's final contradiction.

For a run set Q write n(Q)=number of nonempty runs, E(Q)=number of empty runs, and
  alpha(Q)=|A\L(Q)|, beta(Q)=|L(Q) intersect A^c|,
  alpha'(Q)=|A^c\L(Q)|, beta'(Q)=|L(Q) intersect A|.
Thus q=alpha+beta, q'=alpha'+beta', l=a-alpha+beta, and n(Q)<=l(Q). Disjoint run sets have disjoint letter sets.
LEMMA 1 (signed run cost). If theta_i>=0, theta_i+|L_i|>=2. If theta_i<=0, -theta_i+|L_i|>=2. Consequently a set Q
of nonnegative runs has Theta(Q)+l(Q)>=2|Q|, and a set of nonpositive runs has Theta(Q)<=l(Q)-2|Q|.
Proof. If |L_i|=0, (A2) gives |theta_i|>=2. If |L_i|=1, (Parity) makes theta_i odd, so a nonnegative theta is>=1,
and a nonpositive one<=-1. If |L_i|>=2 its length alone is>=2. Sum the inequalities; the second follows equally
by applying the first reasoning to -theta_i, whose parity is unchanged. []
LEMMA 2 (disjoint-letter counts). For disjoint run sets Q1,Q2:
(a) a<=alpha(Q1)+alpha(Q2), a'<=alpha'(Q1)+alpha'(Q2).
(b) At most alpha'(Q1)+alpha(Q2) letters lie outside L(Q1) union L(Q2). If Q_i is inside S_i for the opposite
    alternating sets and B_i is inside S_i\Q_i, then, with z1=q'(Q1), z2=q(Q2), l(B1)+l(B2)<=z1+z2.
Proof. Every letter is outside at least one of the disjoint letter sets. A letter outside both lies in A^c\L(Q1)
or A\L(Q2). The bottom letters lie outside both, and each nonempty run consumes at least one distinct occurrence. []

Sort the 12 runs of each S by decreasing theta (ties arbitrary, consistently). J=J6(S) is top6, t=t6 its last
value, B6=S\J (six runs). K=J7(S)=J union {u} is top7, t+=t7, C7=S\K (five runs). Runs of a bottom set have theta
no larger than the corresponding last top value. If that value is<=-1, the bottom sum is <=-b-E(bottom), where b
is its run count (empty negative theta<=-2). If it is<=-2, the bottom sum is<=-2b. If the top threshold is=-1,
its r top runs have sum>=2r-3n(top): empty top theta>=2, nonempty top theta>=-1. These follow directly from (A2).

## 2. Exhaustive top-set types and the positive-threshold pair

The type of J6(S) is exactly one of
  G6: q>=9,q'>=7 (chi6=1); Q6: z=q<=8 (chi6=10-z); P6: z=q'<=6 (chi6=8-z).
The type of J7(S) is exactly one of
  G7: q>=7,q'>=9 (chi7=1); Q7: z=q<=6 (chi7=8-z); P7: z=q'<=8 (chi7=10-z).
The cases follow by expanding the maxima and q+q'=42; P and Q cannot coincide at either level.
LEMMA 3 (near-A nonnegative tops are impossible). A Q6 set has t6<=-1; a Q7 set has t7<=-1.
Proof. If its r top runs were all nonnegative, Lemma1 gives Theta+l>=2r. But for Q6, (U6) and l=a-alpha+beta give
  Theta(J6)+l(J6)<=8-nu-q+l=8-(nu-a)-2alpha<=8<12.
For Q7 the same expression is <=6-(nu-a)-2alpha<=6<14. Both contradict the cost bound. []
LEMMA 4 (positive P6 closes the whole pair). If a P6 top has t6>=1, then Xi(S)+Xi(S')<=-6 for the other set S'.
Proof. (U6) gives 6<=Theta(J6)<=6-nu-q'(J6). Thus nu=q'(J6)=0 and Theta(J6)=6. Since all six top theta>=1, they
are all1, so t6=1. nu=0 means A is empty. q'(J6)=0 means L(J6)=A^c, so all42 letters lie in J6 and every run of B6
and S' is empty. Bottom theta<=1, and nonzero-even emptiness forces theta<=-2; hence Theta(S)<=6-12=-6, Xi(S)<=-4.
For S', its J6 has q=0 (Q6). Lemma3 gives t6(S')<=-1; that threshold is even, so <=-2. Its top upper sum is<=8
and its bottom six sum<=-12, giving Xi(S')<=8-12+2=-2. The combined bound is<=-6. No all-unit or e=0 assumption
is made: positive labels may have arbitrary allowed odd weights. No E0, lower window or total identity is used. []
If either alternating set meets Lemma4 we have already proved WC1023. Henceforth suppose neither does. G6 has
negative threshold (its top upper bound is<=-1-nu), Q6 does by Lemma3, and a P6 now has t6<=0. Thus the following
FIVE classes exhaust the two sets:
  C1: J6 is G6;  C2: J6 is P6 (t6<=0, including threshold0);
  C3: J6 is Q6 and J7 is G7;  C4: J6 is Q6 and J7 is Q7;
  C5: J6 is Q6 and J7 is P7 (hybrid).
In C5, t7<=t6<=-1. This proves, rather than assumes, that the prior illustrative nonnegative hybrid cannot occur.
LEMMA 5 (one-set bounds; z has the type-specific meaning above).
(a) G6: Xi<=-5-E(B6). G7: Xi<=-4-E(C7).
(b) P6 with t6<=0: Xi<=2-z AND Xi<=-4-z+l(B6).
(c) Q7: Xi<=3-z-E(C7)<=3-z AND Xi<=-2-z+l(C7). If t7<=-2, Xi<=-2-z.
(d) C5 hybrid: Xi<=5-z+-E(C7), with z+=q'(J7)<=8.
Proof. (a) The top upper sum is<=-1-nu and the negative bottom contributes<=-6-E(B6) or<=-5-E(C7). Add nu+2.
(b) The P6 upper sum is<=6-nu-z. Every bottom theta<=0, so Lemma1 gives Theta(B6)<=l(B6)-12; this proves the mass
bound. If t6<=-1, the negative bottom bound gives Xi<=2-z-E(B6). If t6=0, then 0<=Theta(J6)<=6-nu-z, so nu+z<=6;
letters outside L(J6) number alpha(J6)+alpha'(J6)<=a+z<=nu+z<=6. Thus l(B6)<=6 and the mass bound gives Xi<=2-z.
(c) The Q7 upper sum is<=6-nu-z. By Lemma3 its bottom five are negative, so either use -5-E(C7), or Lemma1's mass
bound l(C7)-10, or -10 when t7<=-2; add nu+2.
(d) Hybrid t7<=-1 as just proved, and its P7 top sum is<=8-nu-z+; add -5-E(C7) and nu+2. []

## 3. Every nonhybrid pair

LEMMA 6. If neither set is C5 (and neither is a positive P6 already handled by Lemma4), the Xi sum is<=-1.
Proof. The four remaining classes have individual Xi upper bounds -5,2,-4,3 respectively (Lemma5). If one has a
G6 or G7 top, the sum is<=-4+3=-1. Otherwise only P6 and Q7 tops remain.
Two P6 are impossible: Lemma2(a) gives 17<=a'<=alpha'(J6^1)+alpha'(J6^2)<=q'(J6^1)+q'(J6^2)<=12.
For P6 with Q7, let z1=q'(J6^1), z2=q(J7^2). Their bottom LETTER masses satisfy l(B6^1)+l(C7^2)<=z1+z2 (Lemma2(b)).
The two mass bounds of Lemma5(b),(c) therefore give
  Xi(S1)+Xi(S2)<=-4-z1+l(B6^1)-2-z2+l(C7^2)<=-6.
This includes every threshold0 P6 case without a spare-letter or saturation assumption.
For two Q7 write z_i=q(K_i), K_i=J7(S_i), alpha_i=alpha(K_i), beta_i=beta(K_i), t_i=t7(S_i), C_i=S_i\K_i.
All t_i<=-1 by Lemma3. Lemma2(a) gives a<=alpha_1+alpha_2, hence l(K_i)=a-alpha_i+beta_i<=alpha_(3-i)+beta_i.
If both t_i=-1, the empty-top lower estimate and the Q7 upper window give
  14-3(alpha_(3-i)+beta_i)<=14-3n(K_i)<=Theta(K_i)<=6-nu-alpha_i-beta_i.
Adding the two inequalities gives z1+z2>=8+nu. Thus Lemma5(c) bounds the sum by<=6-z1-z2<=-2-nu.
If both t_i<=-2, the sum is<=-4-z1-z2<=-4. If t1<=-2,t2=-1 (or vice versa), Lemma5(c) gives
sum<=-2-z1+3-z2-E(C_2)=1-z1-z2-E(C_2). Since t2=-1, 14-3n(K_2)<=Theta(K_2)<=6-nu-z2<=6, so n(K_2)>=3.
But n(K_2)<=l(K_2)<=alpha_1+beta_2<=z1+z2. Hence z1+z2>=3 and the sum is<=-2. This exhausts ordinary pairs. []

## 4. Every hybrid pair

LEMMA 7. If S is C5 (Q6/P7) and S' is the other alternating set, then Xi(S)+Xi(S')<=-1.
Proof. Set z0=q(J6)<=8, z+=q'(J7)<=8 and {u}=J7\J6 (u is the seventh run). Write beta(u),beta'(u) for that run's letter
counts. Since J7=J6 union {u},
  z+=(a'-beta(J6)-beta(u))+(a-alpha(J6)+beta'(u))
    =42-z0-beta(u)+beta'(u)>=42-z0-beta(u).
Thus beta(u)>=42-z0-z+>=26. Also a=beta'(J7)+alpha(J7)<=z++alpha(J6)<=z++z0<=16, so a'>=26. For any run set Q
inside S', its A^c letters lie outside L(J7), giving beta(Q)<=alpha'(J7)<=z+<=8. Therefore
  q'(Q)>=alpha'(Q)=a'-beta(Q)>=18.
S' cannot be P6 or have a P7 top. Its only possible classes are C1 (G6), C3 (Q6/G7), C4 (Q6/Q7). This also excludes
hybrid/hybrid pairs without an assumed giant-pair or nonempty-run restriction. The >=26-letter seventh run was
DEDUCED from the two deficits, not imposed as a premise.
By Lemma5(d), Xi(S)<=5-z+-E(C7). Let o=number of letters outside L(J7). Then
  o=alpha(J7)+alpha'(J7)<=alpha(J6)+alpha'(J7)<=z0+z+.
If S' is C1, the eleven runs C7 union B6(S') have at most o letters, so their empty count is>=11-z0-z+. Lemma5(a):
  Xi(S)+Xi(S')<=5-z+-E(C7)-5-E(B6(S'))<=z0-11<=-3.
If S' is C3, the ten runs C7 union C7(S') give an empty count>=10-z0-z+, and
  Xi(S)+Xi(S')<=5-z+-E(C7)-4-E(C7(S'))<=z0-9<=-1.
If S' is C4, put z'=q(J7(S')). Lemma2(b), now with the near-A^c set J7(S) and near-A set J7(S'), bounds the letters
outside both by z++z'. Thus E(C7)+E(C7(S'))>=10-z+-z', and Lemma5(c) gives
  Xi(S)+Xi(S')<=5-z+-E(C7)+3-z'-E(C7(S'))<=8-10=-2.
These exhaust hybrid pairs. []

## 5. Count completion, word-level exclusion and scope

PROOF OF WC1023. Fix any data satisfying (A1)-(A3), with any tie choices for the sorted runs. If either top6 is
positive P6 (t6>=1), Lemma4 gives the sum<=-6. Otherwise Sec.2's five classes are exhaustive; if either set is
hybrid, Lemma7 gives the sum<=-1, and if neither is hybrid, Lemma6 gives the sum<=-1. Thus
  Xi(S_ev)+Xi(S_od)<=-1
for all the reduced integer data, without the total identity. This proves WC1023.
PROOF OF THEOREM FC1023. An admissible target NF of a length90 avoider has a frame, and every frame supplies
(A1)-(A3) at the exact accepted UMR scopes. WC1023 gives the negative sum in every frame. Now and only now use (A4):
the same sum is e=sum_l(|c_l|-1)>=0. Contradiction. Therefore no target NF exists; since the original antecedent is
SOME admissible NF, the full existential NF/word cell is excluded. []

There is NO residual left in this cell relative to the accepted inputs. No selected UB or sign/type subset was
assumed; all positive, zero and negative threshold cases are accounted for before invoking the identity. The
argument therefore includes every frame that would satisfy the candidate UFC R23 description, including all its
giant, ordinary, hybrid and mixed-window cases, without treating that candidate description as a lemma premise.
The illustrative nonnegative hybrid is excluded by the general run-cost Lemma1 and Lemma3, NOT by silently replacing
the full target with it. Only upper6/upper7, signed run parity, empty nonzero-even theta, disjoint occurrences,
nu>=a and a'>=17 enter the count. Neither E0, ENV nor a lower-window extension is required.
No assertion of acceptance, any other cell, kappa, prime or k, a full p23 union, inverse/rigidity/o_F assembly,
full ordered Olson, priority, novelty, human-referee, Lean or runtime verification is made. Parent alone reviews
and accepts. No computation, enumeration, solver, test, assertion statement or model call was used.

## 6. Literal interface and exposure

| Input | Absolute path; whole-file SHA256 | Inclusive LF | Scope/use |
|---|---|---|---|
| Authority | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-olson-fc-cell-10-23-transition-v1.json; efa20631f20ea4970627ff06e326bc0547cbc4ea5caa95a6303e05e29ea15aea | 1-59 | Full cell and all R23 cases; freeze/rules; prior parent exposure |
| Frozen scope | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-fc-cell-10-23/FC1023-scope-v1.md; 190f9656606750f184963724d211bfaaf7165b05e7dc16c3fe5d78397d3cdf1e | 1-77 | Full prior authorship/exposure; no NEW derivation before freeze |
| Accepted UMR scope | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-verdict-v1.md; a2535971cb214e399433235a4b9fca2de7328d15bec2c2f4eece35c05456c772 | 3-26 | UMR-F/Lemmas0-13 at literal scopes; Lemma14 total; exact primitive imports LF24 |
| UMR proof | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-middle-range/proof-UMR-v1.md; c403bfbae9f1c7b75698010cae78515a253154e689336e79006c588ff15023a9 | 18-28,49-56,64-68,88-118,137-139,161-165,201-209,238-239,252-258 | All data imports in Sec.1; theta parity is the literal Lemma10 LF202 conclusion with sigma_i LF109-110 |
| UMR erratum v1 | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-erratum-v1.md; b83313b3fe828ee19a0902e9a5149db42ee55318500f92bac577b4bbd7088c5f | 1-10 | Connectivity-link scope retained; no saturation gloss used |
| UMR erratum v2 | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-erratum-v2.md; 2a5f142ef136b04c15304137a4ba19946d0fee115ce18e8660817cd25bc902a2 | 1-9 | No converse or residual/existence inference |
| UFC candidate, prior exposure only | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-fc/proof-UFC-v1.md; 2d03076c9bbf1afa3d68e42bfc2fe9eeb4a62ee64b59e6c94c53f65a32b670c5 | 1-347 (prior authorship) | No lemma premise, including E0/ENV; all local arguments re-derived |
| Parent UFC check, untrusted exposure | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UFC-parent-written-check-v1.md; 0bc950ea8c165732115036c2281b91b1da558abd561c8d63ad8c2c7d9ff8e927 | 1-14 (read after freeze) | Not a theorem or premise; zero-negative/all-unit scoping exposure is in authority LF50 |

The primitive inputs enter ONLY through accepted UMR and are exactly UMR verdict LF24: NF; GRX if-direction; SC0
applied to Y'z; ZSTRUCT/FB at exact (S') parameters (p-1,kappa-1); the S1 definition; stated LOWER conventions.
No FCW or balfull theorem/erratum is promoted as a mathematical input. Accepted FC717/FC19 cell statuses are context
only (their paths/hashes/LF ranges are recorded in the frozen scope); no claim of a p23 frontier union is made.
Process: all mathematics by hand after freeze. Early unused local E0/lower-window, sparse-letter and equality-split
routes are disclosed in checkpoints01-02, not premises. Files are exclusive and immutable. Machine categories:
date, SHA256, byte/LF counts, reading files, mkdir, exclusive drafted-text creation; no scientific computation.
