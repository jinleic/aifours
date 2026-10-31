# Exact support50/e0 — signed block matrix rank at least FIFTEEN, forcing TWO independent physical N-only additive charges

Owner PhysicsAME46-2 / physics-6. Actual `/bin/date` immediately before this NEW write: **Mon Oct 26 08:49:23 PDT 2026**. Precreation observation only.

**NEW COMPLETE WRITTEN MATRIX/PHYSICAL-CHARGE FRONTIER CANDIDATE, UNREVIEWED.** The pure matrix theorem is self-contained. Its application to the ENTIRE actual e0/support50 stratum explicitly consumes the new no-Hamming1 and linear-incidence author proofs at a prospective joint input boundary, NOT their automatic adoption or old I48/J49. It is NOT an odd-kernel existence theorem, feasibility certificate, tensor, noexact50/minimum or numerical promotion.

## 0. Original-primary order and exact new input union

All current work follows actualv121FRETURN and the separate07:12:45whole-primaryACK WRITTEN/SENT before source/reasoning, SHA256 `2905623b9bcb3a543d84bbc914324d12b712d0efadcf3e6fc880e14d5b54e835`. The new rank/equality-exclusion/charge proof was saved in checkpoint60 at08:47:47. All prior leads and permanent findings remain exposed; no later gate is backdated as preregistration.

For the ACTUAL AME corollary define the new prospective written input union J_charge to include:

- `support50-e0-global-no-Hamming1-v1.md`,121LF, SHA256 `0da8a5de3c48b7fea657b93459b41ba5d248781df554b60ade7dc76c90f147dc`, ENTIRE NH50/coarse-capacity/physical-surgery theorem, including its exact adopted O28/O30 interfaces;
- `e0-six-site-three-rectangle-odd-relation-v1.md`,100LF, SHA256 `ff0b111cc462c997e5afdc1a69f33bdb7e9063155133e1a2350ee4b5fd4da4ae`, explicit local odd certificate and the no-Hamming1 cross-cut intersection argument (recalled in §1);
- the self-contained R15/physical-gauge/officer proofs HERE.

Those author bodies remain separately UNREVIEWED unless an actual newer full parent disposition is read. This source records a new theorem composition CANDIDATE at the named literal proof union, not acceptance by author title/hash or a blind old-verdict transfer. No historical lower48/I48/J49/native proof is a premise. The103LF odd-coefficient graph-floor packet is related but is NOT needed for R15 or the charge dimension bound.

## 1. Exact LINEAR support-matrix hypothesis

Take a literal e0 support on28 globally indexed N sites, partitioned into SEVEN actual K2 blocks in EACH of THREE cuts. Give each block its integer checkerboard row; B is21x28. Every row has exactly FOUR±1 entries, each column exactly THREE±1 entries, one in each cut class. Blocks in one cut are disjoint.

Assume the different-cut block incidence is LINEAR: two such blocks intersect in at most ONE N site. This matrix hypothesis does not itself assert physical realizability or existence of phases.

For the later actual tensor application, NH50 supplies no-Hamming1. Then two different-cut blocks cannot share adjacent corners: they would preserve different coordinate pairs and force Hamming<=1, while an opposite corner has distance4. A shared diagonal pair instead forces the explicit six-site/three-rectangle relation(1,-1,1) of odd sum, impossible for an actual complex tensor. Thus actual phase-realizable no-Hamming1 supports have precisely the linearity needed here. No arbitrary scalar incidence matrix is silently treated as physical.

**Theorem R15. For EVERY B with the stated three-cut/linear signed support, rank_R(B)>=15.** The theorem does not require that a phase solution or an odd relation exists.

## 2. Exact trace lower bound, with the EQUALITY case still to exclude

Let G=B B^T, a positive21x21 real symmetric matrix. Every diagonal entry is4. Two different rows have inner product0 or±1, by linearity; same-cut rows have inner product0.

Each row has four sites; at each site two other-cut blocks meet it. All EIGHT such neighbours are DISTINCT, or two blocks would share two sites. Hence each row of G has exactly EIGHT off-diagonal entries±1. Therefore

    Tr G=21*4=84,
    Tr G^2=21*(4^2+8)=504.

For positive eigenvalues lambda_1..lambda_r, Cauchy gives `(TrG)^2<=r TrG^2`. Since84^2=14*504, this proves rank>=14, but NOT yet15.

If rank were14, equality in Cauchy would force ALL FOURTEEN positive eigenvalues equal84/14=6. Thus

    G^2=6G.                                            (Eq)

The following actual sign/incidence argument rules out this equality; it is not a numerical near-rank estimate.

## 3. Equality14 contradicts the shared-site sign and seven-block connectivity

Pick adjacent rows A,B in two different cut classes, with unique shared site p. Write `G_AB=alpha=±1`. The third cut has the unique row C0 through p, and

    G_AC0 * G_C0B
      =(B_Ap B_C0p)(B_C0p B_Bp)=alpha.                  (Plus)

Linearity is needed: these inner products each consist of THAT one shared site, not an independently selected signed correlation.

For the off-diagonal(A,B) entry of(Eq), the two diagonal terms contribute8alpha. The only other possible terms come from COMMON neighbours in the THIRD cut; different rows within A's or B's own cut are orthogonal. Consequently

    sum_(common C) G_AC G_CB = -2alpha.                 (Sum)

There are at most FOUR common C-neighbours, because each row meets four DISTINCT blocks of the third cut. One term is alpha by(Plus); every other term is±1. Dividing by alpha, the target is-2 with a mandatory+1. With at most four terms, this is possible ONLY with FOUR common neighbours and all other THREE terms-1. (Fewer terms have either the wrong parity or minimum greater than-2.) Therefore EVERY adjacent A/B pair has IDENTICAL four-element C-neighbour set.

The A-B incidence graph is simple4-regular on SEVEN vertices in each class. ANY two A-vertices share a B-neighbour, since two four-subsets of a seven-set intersect. Hence this bipartite graph is CONNECTED. Along its edges the equality of C-neighbour sets propagates, so ALL fourteen A/B rows must share the SAME four C-neighbours.

The remaining THREE C-rows would then have NO A- or B-neighbour, contradicting that EACH C-row has four neighbours in EACH other cut class. Equality14 is impossible. Since rank is an integer, rank>=15, proving R15.

No graph enumeration, determinant, eigenvalue program, integer-instance probe or scientific interpreter was used. All signs, traces, exact equality and connectivity facts were displayed.

## 4. Physical one-party phase gauges belong to the RIGHT kernel

Now assume the rows/columns come from actual physical rectangles. Let V=sum_i v_i be the total number of ACTIVE physical values across the four parties. Form the INTEGER28xV incidence matrix W with

    W_(x,(i,a))=1 if x_i=a, else0,

for each N site x and each active party-value column. Each N row has four ones.

An arbitrary vector f of column values represents an additive one-party phase function

    F(x)=sum_(i=1..4) f_i(x_i).

Every physical checkerboard row of B annihilates it: at a party belonging to the block's row-label pair, its first/second row values each occur once with+ and once with-; the same holds for the block's column-label parties. Thus

    B W=0.                                             (Gauge)

Therefore `rank W<=dim ker(B)<=28-15=13` at R15's hypotheses. There are always THREE trivial constant relations in ker(W): take each f_i constant c_i with sum_i c_i=0. These do not represent a new physical restriction and must be factored out when counting charges.

The dimension of ADDITIONAL additive relations is consequently at least

    dim ker(W)-3 >= V-13-3=V-16.                       (Charge)

W has integer entries, so its real/rational ranks agree; one can choose a rational basis of its kernel/complement to the constant subspace and clear denominators. These additional relations can therefore be represented by INTEGER functions f_i on the ACTUAL active alphabets. No such functions were computed or arbitrarily assigned; their existence and minimum dimension are exact linear algebra.

## 5. ENTIRE actual t22/h14 has at least EIGHTEEN active values

This step uses actual officers and includes all outside physical levels; it is not an assumed generic gauge rank.

Positive deficits d_i(a)=6-#{officers at i=a} sum to h14, are at least2 and at most6. Thus every party has at least3 active values. If one party has EXACTLY3, at least one deficit is>=5. Its partner hole neighbours must all be active, so EVERY other party has at least5 active values. Hence V>=3+5+5+5=18.

Otherwise every v_i>=4. If V<=17, the ONLY possibilities are4444 and4445. Let f_c count the SAME22 officers with c active coordinates, retaining all c=0..4. Actual active single/pair counts give

    kappa1=6sum v_i-4h,
    kappa2=sum_(i<j)v_i*v_j-6h,
    22-kappa1+kappa2=f0+f3+3f4>=0.

At4444, kappa1=40,kappa2=12 and22-40+12=-6, impossible. At4445, kappa1=46,kappa2=24 and the nonnegative identity is0, forcing f0=f3=f4=0. Every officer would then have only ONE or TWO active coordinates, but their total active incidence46 exceeds2*22=44. Impossible.

Thus V>=18 for EVERY actual AME tensor with t22, independent of e0. No officer active-coordinate cap was imposed before it was derived, and no computer-assisted lower bound or support profile was imported.

## 6. Exact TWO-charge frontier for the whole remaining e0 case

At the explicitly named candidate proof union J_charge, an actual exact50/e0 tensor is no-Hamming1, has linear three-cut block incidence, hence rankB>=15. The actual one-party support incidence W therefore has rank<=13, while V>=18. Equation(Charge) yields

    AT LEAST TWO independent NONTRIVIAL integer-additive relations
    sum_i f_i(x_i)=0 for EVERY actual N site x.         (Two)

More precisely the additional relation dimension is at least V-16; larger active alphabets force more than two. This is not the unproved assertion `rank W=V-3`: the theorem shows surviving supports MUST FAIL that generic independence by a substantial amount.

The charges annihilate the NONOFFICER SUPPORT ONLY. Extend their values on inactive levels if desired, but no proof says they vanish on officers or that the FULL AME state has zero total charge. Claiming a continuous global state symmetry without that officer check would erase the original compatibility problem. Likewise existence of additive charges alone does not prove infeasibility; constrained supports might have such relations.

The first unproved original step is to use these ACTUAL additional charge relations together with officer extensions/all six marginals to contradict or classify every physical support, or to supply an actual phase-compatible tensor. The signed integer LEFT-kernel odd-relation question is also not answered by the RIGHT-kernel gauge count. No odd z, feasible phase vector, concrete support, global GLOBAL-ODD/noexact50/minimum or numerical promotion is supplied.

## 7. Dependency and assurance boundary

R15 needs only the displayed linear three-cut signed matrix incidence. Gauge/active-value/charge facts use actual checkerboard physical coordinates, intrinsic officers/holes and elementary integer/rational linear algebra. Their specialized applications are proved here. To apply them to the ENTIRE e0 stratum, J_charge additionally needs the complete new NH50 and HEX proofs at their exact input scopes; no previous branch review or author hash automatically audits that union. It remains a separate full mathematical AND dependency/application gate obligation.

This is a genuinely new algebraic representation of the remaining physical support, not a repeated B^Tz criterion, presumed full rank, phase-alphabet relaxation or independent spectral mode. It neither authenticates old I48/J49/native proof histories nor alters their conditional boundaries. Numerical48..60, exact tensor/upper witness and all stronger gates remain unchanged. E4 A/A-transpose/twoD2 compatibility and original minimum remain active open obligations.

All old proof/ACK/checkpoint histories persist, including the07:58:35cp55 mathematical false-lead withdrawal, unconsumed here. Both AME pre-ACK majors, v100-E written-exactness ZEROcredit, originalv107read-order/prospectivecorrection, FULL06:05:05..06:57:52cadence MAJOR, characterized unadmitted cells and every parent/owner/reviewer finding remain. No processPASS/retropreregistration/falseblind/global hidden-cognition/runtime/access/cadence census or execution/falsity-from-process inference.

Exact WRITTEN symbols/fractions/integer products only, including private scoping; no decimals/new numeric parameter trials/scientific interpreter/Eval/calculator/CAS/program/enumeration/solver/replay/CLI/nestedagent/newGO. ExclusiveOWN/immutable sources/noGit/deletion/publication. No formal/kernel/configured-family/human/executable/novelty/SOTA acceptance. Original18/HOLD/October27sciencecutoff11:05:38/deadline12:35:38/substantiveactivecheckpoints<=30min unchanged. Incremental ACTIVE original research, NOT an early final-park or96-hour closeout.
