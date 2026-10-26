# Exact SN<=2criterion for a coherent opposite-offset component; a new frustrated PPTgeometry is still SN<=2

PhysicsPPT44-2. Actual `/bin/date` before this manuscript: **Sun Oct 25 14:09:33 PDT 2026**. **AUTHOR-WRITTEN CANDIDATE; fresh independent reconstruction and parent disposition pending.** All arithmetic/rank/convex identities below are WRITTEN, not machine-checked. No NEWscientific eval/program/arithmetic interpreter/enumeration/symbolic computation/solver/replay/compile, nativeGO, externalCLIor nestedagent. HOLD/v9/v10/v11and originaldeadline remain binding; earlier checkpoint013cadence deviation is not repaired or withdrawn.

Interface `checkpoint-034-balanced-parity-exact-SN2-criterion-lead-v1.json`, SHA-256 `1c61c64c12928b36817c769d50435a95309c8c42b80dbd6a58717b0a99db07c4`, records informal written leads before this full body and is not retroactive preregistration. This is a new representation allowing high rays with ALLfour entries nonzero, beyond the earlier single-zero-mode templates. It does NOTsettle P44.

## 1. Exact component theorem

Let F_(j,0)=1/2,F_(j,1)=i^j/2and E_q e_j=|j,j-q>, with indices modulo4. For t>0, |gamma|<=1and Y0,Y1,Y2,Y3>=0define the PSDoperator

```
S=t E0F[1 gamma;conjugate(gamma) 1]F*E0*
                        +sum_j Y_jP(j,j-2),
cE=sqrt(Y0Y2), cO=sqrt(Y1Y3).                             (1)
```

**Theorem.** S has Schmidt number AT MOSTtwo if and only if

```
cE>=t|Im gamma|/2,
cO>=t|Re gamma|/2,
cE+cO>=t/2.                                               (2)
```

This is an EXACTcriterion for this stated component class, not all states or all PPTstates. Such a component by itself need not be PPT. It is useful because the actual two-high-block states split into two such operators after a local Bobshift.

### Necessity: complete range and rank argument

In any conic SR<=2decomposition of S, every vector lies in rangeS. It therefore has only difference0/2entries, and its high diagonal is

```
h_j=a+b i^j.
```

Simultaneous row/column ordering0,2,1,3makes its coefficient matrix blockdiagonal with two2by2blocks. If h!=0, both parityblocks are nonzero: vanishing h0,h2or vanishing h1,h3would force a=b=0. Since totalrank<=2, both blocks then have rank1. Consequently their off-diagonal products equal

```
h0h2=a^2-b^2, h1h3=a^2+b^2.                              (3)
```

If h=0the absolute-value inequalities below remain trivially valid, even when a low-only block has rank2. Summing absolute products and applying Cauchy to the actual low diagonal moments gives

```
sum |a^2-b^2|<=cE,
sum |a^2+b^2|<=cO.                                      (4)
```

The exact high covariance is

```
sum |a|^2=sum |b|^2=t/4,
sum a conjugate(b)=t gamma/4.                             (5)
```

For each complex a,b,

```
|a^2-b^2|>=2|Im(a conjugate(b))|,
|a^2+b^2|>=2|Re(a conjugate(b))|,
|a^2-b^2|+|a^2+b^2|>=|a|^2+|b|^2.                        (6)
```

The first two follow by squaring; the last follows from the two triangle bounds giving at least2|a|^2and at least2|b|^2. Equations(4)–(6)prove ALLthree necessary inequalities(2). No restriction to real coefficients has been made.

### Sufficiency A: explicit unit-circle phase distribution

Write u=Re gamma,v=Im gammaand

```
Amax=min(1,2cO/t), Bmax=min(1,2cE/t).
```

Under(2), these dominate |u|,|v|and Amax+Bmax>=1. Choose nonnegative A,Bwith

```
A>=|u|, B>=|v|, A<=Amax, B<=Bmax,
A+B>=1, A^2+B^2<=1.                                     (7)
```

An explicit choice is A=|u|,B=|v|if |u|+|v|>=1. Otherwise take A=max(|u|,1-Bmax),B=1-A. The required bounds follow from Amax+Bmax>=1and |u|+|v|<1.

Let L=A+B,R=sqrt(A^2+B^2). Except for an axis point L=R=1, the absolute coordinate pair(A,B)is represented by the three QUARTERunit-circle points

```
(A/R,B/R), (1,0), (0,1)
```

with probabilities

```
p=R(L-1)/(L-R), (1-p)A/L, (1-p)B/L.                      (8)
```

They are nonnegative, sum1and have mean(A,B). The axis case uses its one point; L=1orR=1otherwise is already included by(8). Independently flip the first and second signs with constant means u/A,v/B(where a zero denominator has zero coordinate and its sign is irrelevant). This gives at most12UNITcomplex phases xi_lwith probabilities p_lsuch that

```
sum p_l xi_l=gamma,
sum p_l |Re xi_l|=A,
sum p_l |Im xi_l|=B.                                     (9)
```

The phase distribution is an exact finite convex construction, not a numerical approximation to gamma.

### Sufficiency B: rank-two matrices and exact operator identity

For every positive p_lput

```
h_j^(l)=sqrt(t p_l/4)(1+conjugate(xi_l)i^j).
```

The sum of their high projectors is exactly the highblock in(1). Their opposite products have total moduli

```
L_E=sum_l |h0^(l)h2^(l)|=tB/2<=cE,
L_O=sum_l |h1^(l)h3^(l)|=tA/2<=cO.                        (10)
```

Set etaE=sqrt(Y0/Y2),etaO=sqrt(Y1/Y3)when the respective pair is positive. For a zero pairproduct, (10)forces all corresponding high products zero; use zero offentries and no ratio. For positive pairs, choose any unit square roots sigmaE,sigmaOof the phases of h0h2and h1h3(their zero products simply give zero entries).

For w in the FIVEroots of unity, form matrices with high diagonal h^(l)and entries

```
M_l(w)(0,2)=sigmaE sqrt(etaE |h0h2|)w,
M_l(w)(2,0)=sigmaE sqrt(|h0h2|/etaE)w^-1,
M_l(w)(1,3)=sigmaO sqrt(etaO |h1h3|)w^2,
M_l(w)(3,1)=sigmaO sqrt(|h1h3|/etaO)w^-2.                 (11)
```

Each parity2by2block has its offproduct equal to its diagonal product, hence rank1. The entire coefficient matrix has rank<=2. The five characters0,+1,-1,+2,-2are distinct modulo5; their EXACTaverage kills all high/lowand low/lowcross terms. Thus

```
(1/5)sum_(l,w)P(vecM_l(w))
```

has the desired high block and only diagonal low populations etaE L_E,L_E/etaE,etaO L_O,L_O/etaO. They are bounded by the four Y_jby(10). Adding the nonnegative residual product projectors gives S ITSELF. This is a full operator decomposition, not just diagonal domination. It proves sufficiency, including zero-noise boundaries as explicitly described. Normalization divides by TrS; pure-vector weights are their squared norms divided by5TrS, not uniform weights.

## 2. Why the new genuinely frustrated highblock is not an old zero-entry template

A nonzero I/Zray h_j=a+b i^jhas a zero entry only if |a|=|b|and a/bis one of the four root phases. Its normalized Bloch off-diagonal is then one of{1,-1,i,-i}. A positive conic mixture of such rays with equal coefficient diagonals therefore has

```
|Re gamma|+|Im gamma|<=1.                                (12)
```

Our next trial input gamma=1/2+3i/5has norm squared61/100<1but Blochl1=11/10>1. It cannot arise from ANYensemble consisting exclusively of the single-zero I/Zhighrays used in the14/24phase templates. At least one all-four-entry highray is necessary. This is a genuine representation escape, but by itself is NOevidence of Schmidt number3: the criterion above admits such all-four-entry rays.

## 3. Actual PPTcompletion with both highcoherences, not an attractive control promoted as a result

Here is the precise trial that was retired BEFOREclaiming an SN3pair. Let 0<s<1,t>0, gamma=u+ivwith u,v>0,u^2+v^2<1, and put

```
R0=F[1 s;s 1]F*, R1=tF[1 gamma;conjugate(gamma)1]F*,
b0=1+u+v, b1=1-u+v, b2=1-u-v, b3=1+u-v,
y0=t^2 b3^2/4, y2=t^2 b1^2/4,
y1=t^2 b0^2/[4(1+s)]+s/2,
y3=t^2 b2^2/[4(1-s)]+s/2,
z0=(1+s)^2/[4t(1+v)]+tv/2,
z2=(1-s)^2/[4t(1-v)]+tv/2,
z3=(1+s)^2/[4t(1+u)]+tu/2,
z1=(1-s)^2/[4t(1-u)]+tu/2,
R=sum_q E_q Rq E_q*, R2=diag(y),R3=diag(z).               (13)
```

All four original blocks are PSD. For the FULLpartial transpose use S_tau(j,k)=R_(j+k-tau)(j,k), with these exact Schur structures:

- tau0: highindices0,2have diagonal((1+s)/2,(1-s)/2), diagonal matching entries t b0(1-i)/4,t b2(1-i)/4to lowindices1,3, lowcross is i s/2. The exact Schur residual is `(s/2)[1 i;-i 1]`.
- tau2: highindices1,3have diagonal1/2,1/2and diagonal matching t b1(1-i)/4,t b3(1-i)/4to lowindices2,0. The lowcross is zero and the Schur residual is zero.
- tau1: highindices1,3have diagonal t(1+v)/2,t(1-v)/2and matching(1+s)(1+i)/4,(1-s)(1+i)/4to lowindices0,2. Lowcross is-itv/2. The Schur residual is `(tv/2)[1 -i;i 1]`.
- tau3: highindices0,2have diagonal t(1+u)/2,t(1-u)/2and matching(1+s)(1+i)/4,(1-s)(1+i)/4to lowindices3,1. Lowcross is-itu/2. Its Schur residual is `(tu/2)[1 -i;i 1]`.

Every residual is PSD. These are ALLfourcomplexblocks, not selected principal minors. For the specific input below all lowentries are positive, giving rankR12and PTrank3+2+3+3=11. It is not a single invertiblelocalfilter image of the old PTrank9coherent family; its full-rank local marginals also exclude a singular localfilter. No claim about convex/conic filtered closures is made.

### Explicit Gaussian-rational input and normalization

At s=1/2,t=1,u=1/2,v=3/5, the actual density matrix is

```
rho=[sum_q E_q Kq E_q*]/25129,
K0(j,k)=800(1+i^(j-k))+400(i^j+i^(-k)),
K1(j,k)=800(1+i^(j-k))+(400+480i)i^(-k)+(400-480i)i^j,
K2=diag(648,3152,968,816),
K3=diag(2085,1200,1460,2000).                            (14)
```

The block traces are6400,6400,5584,6745, summing25129. The raw scale is3200R, and TrR=25129/3200. Real/imaginary entries are integers divided by25129; allthese identities are WRITTEN, not interpreter checked. The negative adjacent q1edge b2=-1/10and nonzero opposite q1coherences make the phase structure genuinely different from the earlier one-coherence family.

## 4. The actual new input is SN<=2, not a winning P44candidate

Split(13)into R0+R2and R1+R3with their orthogonal embeddings. Each is of the component form(1), the second after a local Bobshift q1->q0,q3->q2.

For R0+R2, t0=1,gamma0=s=1/2, and

```
cE=99/400,
cO=sqrt(10047)/200>1/2.
```

Allthree conditions(2)hold. For R1+R3, gamma1=1/2+3i/5and

```
cE=sqrt(30441)/320>1/2,
cO=sqrt15/8>1/4.
```

These dominate the respective thresholds3/10and1/4, and their sum exceeds1/2. Thus BOTHpartialoperators have exact rank-two decompositions from Sections1's construction. Their sum is SN<=2. This is a physical upper bound for the actual new PPTinput, not just failure of one witnessclass.

The above phase-frustrated trial is therefore RETIREDhere, not promoted as an attractive PPTstate without a separator. The new criterion is useful precisely because it detects this failure despite the input's rigorous escape from zero-entry templates and its new PTrank.

## 5. Remaining primary gap and non-transfer boundaries

This is a complete WRITTENcomponent classification and a checked-in-writing application, pending fresh independent reconstruction. No machine/kernel/triplechecker/vendor/human/family/novelty/SOTAor P44acceptance is conferred. The finite phases define identities; they are not sampled product/rank-two positivity tests.

P44still requires an explicit rational PPTstate with a universally COMPLEXSR2nonnegative negative separator, or an unrestricted no-go. The component theorem does not classify arbitrary four-complex-block PPTstates, arbitrary highsupport outside the Fplanes, or lowblocks with genuinely coherent rank-three/fourstructure. Adding only a coherent02/20pair to an otherwise positive SR2residual also does NOTescape a decomposition, since that pair already has Schmidt rank<=2.

The next primary representation must genuinely escape these actual-state criteria and still prove BOTHactual PPTand universal complex separation; no new nativepermission is inferred. Earlier14/24operator records, prior moment-only statements, N4historicalUNKNOWN/exit-unestablished and old21unreconstructed gates remain unchanged. No deadline reset or scientificGO.
