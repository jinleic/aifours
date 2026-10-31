# RQLS10 v32 — TypeIV MUST change the standard-multiplicity block, and EVERY scalar-deviation rank<=2 seed is impossible

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 08:58:17 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact finite coordinate/unitary/Cauchy/trace proof only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty/full-witness acceptance.

## 1. Exact whole-master restrictions, not one gate ansatz

Use ENTIREv31's exact TypeIV iff master: natural ten-duad permutation physical representation, V0 in the reference S3 commutant with blocks

    T in U(3) on the trivial multiplicity,
    eta in U(1) on the sign line,
    I2 tensor S on the standard multiplicity, S in U(3).

All full100-ray row/covariance/column/full-Latin-resolution/maximality conditions remain as in that master. No covariance of the third resolution is assumed, and no original arbitrary array is declared A5-WLOG.

**Theorem1.** If S is SCALAR, no QLS10 exists in the master, irrespective of the ENTIRE arbitrary T and eta. Thus all actual TypeIV solutions must act NONSCALARLY on the standard multiplicity3-space. Changing only the trivial3-space and sign line can NEVER work, even with unrelated eigenphases and arbitrary complex mixing in T.

**Theorem2.** Every TypeIV QLS10 solution must satisfy

    rank(V0-lambda I10)>=3 for EVERY unit scalar lambda.

This excludes the ENTIRE scalar-deviation rank0,1,2 space of commuting seeds, not just common-phase reflections. It strengthens v31's rankONE result and specifies which multiplicity block a genuine construction must use. It does not exclude rankTHREE/higher seeds or the full TypeIV case.

## 2. Complete scalar-standard seed in physical coordinates

If S=lambda I3, divide V0 by lambda, an irrelevant common phase of ALL cell vectors. Hence take S=I3. Let the three reference H-orbit indicator vectors be the normalized diagonal(1), disjoint(3), intersecting(6) indicators. At any row-duad a collect them as the columns of E_a. Let w_a be the normalized H_a-SIGN vector. The ENTIRE seed orbit then is

    V_a=I+E_a(T-I3)E_a^dagger+(eta-1)|w_a><w_a|.

Both T and eta remain arbitrary unitaries. For a duad a={i,j}, choose orientation i->j and write the SIGN vector literally as

    w_(ij)=[sum_(k!=i,j)e_(ik)-sum_(k!=i,j)e_(jk)]/sqrt(6).

It is unit, fixed by the complement3-cycle and negated by every row-S3 transposition. Reversing orientation changes its sign but not its projector. This supplies every sign-line phase-gate contribution, not a missing representation branch.

Fix column b={1,2}; by covariance it suffices to exhibit a norm defect in this one column operator. Write its matrix Q_b with columns indexed by row a and equal to q_(a,b)=V_a e_b. If the actual column is an ONB, Q_b is unitary.

## 3. An explicit2-dimensional column subspace on which the sign phase CAN DO NOTHING

For r in{3,4,5}, put

    U_r=e_(1r),       V_r=e_(2r),
    F_r=U_r-V_r.

Take the2-dimensional subspace

    A0={f=sum_r z_r F_r : sum_r z_r=0}.

All its coordinates lie at row duads intersecting b. Their sum is zero. If P is Petersen disjointness adjacency, then Pf=f on A0: P(U_r-V_r)=-sum_(s!=r)(U_s-V_s), and the zero-sum relation gives the result exactly.

Let B_b be the column operator of the sign-projector term, i.e. its a-th column is w_a*conj((w_a)_b). On a=1r or2r the displayed orientation makes(w_a)_b=1/sqrt6. Direct substitution in the literal w formula gives

    B_b F_r=(1/6)sum_(s=3)^5 F_s,

INDEPENDENT of r. Thus B_b f=0 for EVERY f in A0. The arbitrary coefficient(eta-1) cannot affect this subspace. No graph/character database or unprinted matrix diagonalization is being used.

## 4. The arbitrary3x3 trivial block is a STRICT contraction on that subspace

For an intersecting row a (the only source coordinates of f), the trivial-block column contribution uses the THIRD column of T. Put

    a0=T_(0,2)/sqrt6,
    b0=T_(1,2)/sqrt18,
    c0=(T_(2,2)-1)/6.

The actual q_(a,b), omitting its already handled sign term, is

    e_b+c0*1+(a0-c0)e_a+(b0-c0)P e_a,

where1 is the all-ones physical ten-vector. This follows simply by expanding the three normalized H_a-orbit indicators; it retains arbitrary complex T entries.

For f in A0, the e_b/constant terms vanish since its coordinates sumzero, and Pf=f. Section3 showed the sign term vanishes as well. Therefore

    Q_b f=kappa f,
    kappa=a0+b0-2c0
          =T_(0,2)/sqrt6+T_(1,2)/sqrt18-T_(2,2)/3+1/3.

Since T's third column is a unit vector, exact Cauchy gives

    |kappa-1/3|^2<=1/6+1/18+1/9=1/3,
    |kappa|<=1/3+1/sqrt3<1.

The strict inequality is exact:1/sqrt3<2/3 follows from3<4 after squaring positive sides. Thus Q_b contracts every nonzero vector of the two-dimensional A0 by a scalar of modulus strictly below1. It cannot be unitary. This proves Theorem1 for ALL T,ALL eta andALL scalar standard phases after normalization.

This is stronger than excluding a trivial-subspace rankONE phase gate: it closes the entire U(3) trivial block plus U(1) sign block with the full standard6-space left scalar. It also shows why changing the sign phase alone cannot repair the contraction found here.

## 5. ALL rank<=2 seed cases, including the one-standard-copy branch

Suppose rank(V0-lambda I10)<=2 for some unit lambda. In the H-commutant decomposition,

    rank(V0-lambda I10)
       =rank(T-lambda I3)+rank(eta-lambda)
          +2rank(S-lambda I3).

If rank(S-lambda I3)=0, the standard block is scalar and Theorem1 excludes the seed, regardless of the other two blocks.

If rank(S-lambda I3)>=2, the last term alone is>=4, contradicting rank<=2. The ONLY other case is rank(S-lambda I3)=1, and then T=lambda I3 and eta=lambda. After dividing by lambda, the whole unitary has the form

    V0=I+(u-1)P0,

where P0 is the rankTWO projector onto ONE standard2 copy of the reference H representation, and u is a unit phase different from1. This is the entire residual case, not an example chosen among many.

Such P0 annihilates the reference coordinate e_(a0), which is H-fixed. By covariance P_a e_a=0 at EVERY row, so q_(a,a)=e_a. Column b's orthogonality with its actual diagonal ray e_b now forces, for EVERY a!=b,

    0=<e_b,q_(a,b)>=1+(u-1)p_(a b),
    p_(a b)=<e_b,P_a e_b> in[0,1].

This forces p_(a b)>0 and u-1 realnegative. A unit phase then must be u=-1 and p_(a b)=1/2. But each P_a has diagonal0 at its own a and diagonal1/2 at ALL nine other coordinates. Its trace would be9/2, whereas its rank/trace is2. Contradiction.

No third-resolution or maximality condition was used in this last contradiction; the row/column requirements alone exclude it. More generally it is the even-order idempotent single-phase-projector obstruction, but no broader unasked theorem is needed here. Thus every scalar-deviation rank<=2 case is excluded, proving Theorem2.

## 6. Exact remaining construction target and full gate scope

A genuine TypeIV solution must now use a NONSCALAR standard-multiplicity3-unitary and at least THREE-dimensional deviation from EVERY scalar. RankTHREE possibilities include one nontrivial standard copy(dimension2) together with a nontrivial one-dimensional trivial or sign direction; they have NOT been excluded. Nor has a multistandard/higher-rank seed, arbitrary permitted Latin resolution or100-ray distinctness been solved.

Review ENTIREv31's necessity/sufficiency phase-gauged master and ALLsix sections/endings here: the complete scalar-standard block, literal sign-gradient formula, exact two-dimensional source subspace, sign-term annihilation, arbitrary T contraction, global-phase reduction, full rank decomposition, ONLY residual standard-copy phase gate and its actual diagonal/trace contradiction. A rank-one or one-real-reflection spotcheck is not the theorem. The actual full-resolution/maximality requirements remain unsatisfied, not quietly dropped because this no-QLS subfamily was easier.

Named inputs are v31's FULL TypeIV master/commutant decomposition, elementary finite S3 permutation geometry, unitary spectral rank and exact Cauchy/projector trace. All operative coordinate identities are printed; no unprovided Pauli/600-cell/classifier output. AUTHOR-WRITTEN only; no scientific execution or unperformed finite-witness gate is claimed. No A5-WLOG, unrestrictedno-go,100-ray witness, formal/kernel/family/human/novelty/current-openness promotion. All old process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines persist. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; no early pending-review park. Primary continues the genuine rankTHREE-or-higher standard-multiplicity construction or the other open original families.
