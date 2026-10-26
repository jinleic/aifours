# ADDENDUM: flat low-rank CES witnesses cannot hide in a local-filtered ME3 scalar orbit

PhysicsPPT44-2. Actual `/bin/date` before creation: **Sun Oct 25 13:02:56 PDT 2026**. **AUTHOR-WRITTEN CANDIDATE; independent reconstruction and parent disposition pending.** Additive to `nonME-three-ray-complement-scalar-obstruction-v1.md`, SHA-256 `7f520ee82c7e26df39a5ac69943ec956ebd751dc38a250bcd1e838e3f6a657c4`. That pinned body is unchanged. The interface was recorded in checkpoint026after informal written reasoning, not retroactive preregistration.

Written linear algebra ONLY. No eval, scientific arithmetic interpreter, enumeration/program, symbolic/numerical computation, solver/replay/compile, newGOor nestedagent. HOLD/v9/v10/v11, old cadence deviation and exact deadline remain unchanged. This is geometry validation and a local-filter orbit rigidity lemma, NOTa new Schmidt3state, unrestricted P44no-go, cone separation or rescue of the already obstructed flat branch.

## 1. General single-filter rigidity lemma

Let Q>=0onC4tensorC4satisfy:

1. rankQ<=3;
2. no nonzero vector in rangeQhas Schmidt rank<=2;
3. at least one of its reduced operators is not a scalar identity.

For every lambda>0, the Hermitian operator lambdaI16-Qhas NOrepresentation

```
lambdaI16-Q=F(muI16-R_ME)F*,
F=F_A tensorF_B,
R_ME=sum_(j=1)^m p_j P(Phi_Uj),
0<=m<=3, p_j>0, Ujunitary4by4.                          (1)
```

No orthogonality/linear-independence restriction is imposed on those MEterms, and no assumption that the old operator is two-positive is needed. The statement concerns ONEEXACTsame-dimension local-filter congruence, not sums/convex combinations of such operators.

### Step A: exclude singular filters and force mu>0

On kerQthe target has eigenvalue lambda>0of multiplicity at least13. Thus it has rank>=13and at least13positive eigenvalues. If either localfilter were singular, rankF<=3times4=12, contradicting ranktarget>=13. Therefore F is invertible. If mu<=0, muI-R_MEhas no positive eigenvalue; invertible congruence preserves inertia, again impossible. Hence mu>0.

Rearrange(1)as

```
S=muFF*-lambdaI16=F R_ME F*-Q.                          (2)
```

Since both right-hand PSDterms have rank<=3, the positive and negative inertia indices of Sare each<=3. In particular rankS<=6and its zero eigenspace has dimension>=10.

### Step B: classify the possible product positive spectrum

Write muFF*=A tensorBwith A,Bpositive definite4by4, absorbing the scalar muintoA. If AorBis scalar, every nonzero spectral group ofA tensorB-lambdaIhas multiplicity divisible by4. The inertia indices<=3therefore force NOpositive and NOnegative group, so S=0.

Suppose both A,Bare nonscalar. Use a common index set of positive spectral values a_lfor Aand reciprocal values lambda/b_lforB, appending zero multiplicities for unmatched values. Let m_lbe the multiplicity of a_linAand n_lthat of lambda/a_linB. The number of products equal to lambdais

```
n_zero=sum_l m_l n_l.
```

Each multiplicity vector is a nontrivial partition of total4; its sum of squares is at most3^2+1^2=10. Consequently

```
10<=n_zero<=sqrt[(sum m_l^2)(sum n_l^2)]<=10.            (3)
```

Equality throughout forces both partitions to be3+1with the SAMEtwo matched values (the Cauchy equality scalar is1because both totals are4). Thus, for distinct a,a'and corresponding b=lambda/a,b'=lambda/a',

```
A has eigenspaces A3,a1of dimensions3,1,
B has eigenspaces B3,b1of dimensions3,1,
a b=a'b'=lambda.
```

The two cross products a b'and a'bdo not equal lambdaand lie on opposite sides of it. Therefore S has rank6, with its complete support

```
rangeS=(A3 tensor b1) directsum(a1 tensor B3).           (4)
```

Every vector in this support is u tensor b1+a1tensor v, hence has Schmidt rank<=2. This is a whole six-dimensional subspace statement, not point enumeration.

### Step C: contradict the CESrange, or reduce to local unitaries

In the nonscalar case rankS=6. The span of the two PSDterm ranges on the right of(2)has dimension at most6and contains rangeS; rank6therefore forces equality. In particular rangeQsubsetrangeS, contradicting hypothesis2and Q!=0. The nonuniform marginal hypothesis ensures Qis nonzero.

Thus only S=0can occur. A tensorB=lambdaIforces each factor scalar, so Fis an overall scalar times a LOCALunitary. Equation(2)then gives Q=F R_ME F*. Local unitaries preserve the MEproperty, and a positive MEconic sum has both reduced operators equal to its total weight timesI4/4. This contradicts hypothesis3. The lemma follows.

## 2. Application to the new non-MEthree-ray family

For

```
phi=alphaPhi_I+betaPhi_Z, |alpha|^2+|beta|^2=1,
Q_phi=P(phi)+P(Phi_X)+P(Phi_ZX), alphabeta!=0,
```

Q_phiis a rank3projection. Its range is contained in the accepted four-Weylrange, every nonzero vector of which has Schmidt rank>=3. The named WRITTENrange import is Section4of `four-Weyl-rectangle-consolidated-obstruction-v1.md`, SHA-256 `eb1ed1c5aba2bb444a817b48a39ff3d7206c1aacc65421cca7073cffe64a5e02`, at `ppt-four-Weyl-semigroup-two-choice-parent-v1.md` (parent record SHA-256 `562ec6fde1da880b73a5f67e490b9e3d05c66e122795a740cca1e916f1a40c34`). No new executable/formal/stronger acceptance is added to that import.

With v_r=(alpha+beta i^r)/2,

```
Tr_BQ_phi=I4/2+diag(|v_0|^2,...,|v_3|^2).
```

For alphabeta!=0the marginal is nonuniform: the real and imaginary phase cross terms cannot both vanish unless alphaconjugate(beta)=0. All three hypotheses hold. Therefore lambdaI-Q_phifor lambda>0is outside every SINGLEexactlocalfilter orbit of the old arbitrary<=3MEscalar-completion family, not merely outside its displayed unfiltered parameterization. Singular filters are already excluded by rank, not silently omitted.

This does NOTassert that it lies outside convex/conic closures of old witnesses. It does NOTassert an advantage over the PPTcone. The predecessor's new uniform structured PTbound still closes the entire valid flat-completion family at its own written imports; this addendum does not alter that conclusion or supply an anisotropic separator. The live full16Dcoherent-target/peel interface remains exactly the simultaneous complex positivity and negative PPTscore gate stated in `coherent-PPT-target-and-low-rank-peel-lifting-gate-v1.md`, SHA-256 `f7f7eb1befb0a9ff3fe368c91f69ca2373cb616737fa6219418befa8f4b3ab37`.

No novelty/SOTA, formal/kernel, scientific replay, vendor/family/human or P44acceptance is claimed. This is a complete WRITTENorbit-rigidity proof, with the actual family application conditional only on the named accepted range import. Primary research continues; no new scienceGOor deadline reset.
