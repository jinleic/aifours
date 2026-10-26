# v87-C — complete analytic fourteen-vector SN<=2 decomposition on the closed coherent rectangle

MathSemigroup-2, serial cross-domain reviewer. Actual clock observed BEFORE this write: **Sun Oct 25 14:16:17 PDT 2026** (`/bin/date`), an observation bound, not an invented completion timestamp. **WRITTEN mathematical verdict: 0 FATAL / 0 MAJOR / 0 MINOR defects found at the complete238LF operator-decomposition scope plus the EXPLICIT61LF eligibility input.** No scientific interpreter/eval/program, arithmetic/symbolic calculation, generated matrix/ensemble, enumeration, solver, replay, finite-checker/triple-witness or formal acceptance was used.

## 1. Exposure, actual own checkpoint and complete literal coverage

The new `peer-review-ppt-full-rectangle-SN2-ack-v1.json` was written at actual **Sun Oct 25 14:12:17 PDT 2026**, BEFORE opening the new proof, selected eligibility or author checkpoint bodies. My actual PPT exposure includes v43,v48,v52,v55,v78,v82; the last PPT review was actually returned at `peer-review-ppt-actual-face-rigidity-v1.md`, SHA256 `4e109a9e85c3a2cc86d8d63d50a29dae08c228eb604339d08645486aafc2a489`. The subsequent v84-C CLIP review was also actually returned before own-primary continuation, SHA256 `fb97d3cead4e0bce4d8d646b138662a0aa2e0c94022157cbde1ee7d12a9f835e`. This is not blind or different-model-family evidence.

The actual own-primary checkpoint preceded this temporary review: `primary-102319-row-memory-before-v87-checkpoint-v1.json`, SHA256 `e988210f6becf8d5cc833552f5ada2917425ebec4d87baa8109f24701795836f`, observed **Sun Oct 25 14:11:04 PDT 2026**. It retains the unsolved faithful semigroup V-band/CS-host upgrade and does not call its auxiliary wreath map an original embedding.

Read EVERY physical LF1–453 of the sole literal part, including endings, with coverage1–193,194–370,371–453. S1/v9 was FIRST, S2/v10 SECOND, S3/v11 THIRD before the new body. This includes COMPLETE238LF main theorem, EXACT originalLF1–61 ONLY of the217LF eligibility/peel paper, and COMPLETE15LF checkpoint. I do NOT claim the omitted156LF of the peel paper were supplied, read or reconstructed. No whole-file hash substitutes for that selected-range boundary.

Observed live pins:

- Manifest `institute/runs/three-area-2026-10-23-96h/peer-review-wave-eighteen-v87.json`: `761e7866e8d11e5d5f343a01cd443c6a860ada32f68311e131729c03f585e297`.
- Receipt `peer-review-wave-eighteen-v87-packet-receipt-v1.json`: `7daf09cb575a18f6a9513e3dc066c1aa475c0345e1e957dbe7edd70fc9724fd0`.
- Sole part `peer-review-wave-v87-v87-C-part1-v1.md`: `05042a0b923c7a7b2e6d75f720a87f6f698b0dd5500ca73fc38324af867f69f7`.
- New `physics/evidence/three-area-20261023-96h/parallel-18/ppt-schmidt44/coherent-full-rectangle-SN2-14phase-kernel-certificate-v1.md`: `dcebacbc78e7a5ab25c4914a3b413d58d87398b093b617e1246e4ca73a0725d6`.
- Selected eligibility `coherent-PPT-target-and-low-rank-peel-lifting-gate-v1.md` there: whole-file `f7f7eb1befb0a9ff3fe368c91f69ca2373cb616737fa6219418befa8f4b3ab37`, coverage ONLYLF1–61.
- Author `checkpoint-032-coherent-full-rectangle-14phase-SN2-lead-v1.json`: `83e6699c6a0cafe536669446eb29dfda0704bc37df2d53d3e5d5cc6b213b39fd`.

Mandatory complete corrections retained: v9 `b7c92143cda18c88c7c56017859ab3c7f08fa92ef3d00fd85ba29f41ac258034`; v10 `d61acbf77fefa3a8d55d0cf74e9ebe0b680edb28d273f5b22255d09cbd66aa62`; v11 `3ce29e3c49d4789106431978152ffab28a3d14402a748ec3828c825f31c4d9e7`. No older cadence, execution, source-coverage, freeze-order or clock correction is erased or backdated.

## 2. Target, conventions, positivity, normalization and rank

All indices are modulo4. Use coefficient vectorization `vec M=sum M_ij|i,j>`, Bob partial transpose Gamma, and P(v)=|v><v|. E_q maps e_r to |r,r-q>. Let u_j=1,v_j=i^j, F=[u/2,v/2], B=FF*. F*F=I2 because sum i^j=0. The target is

`R=sum_(q=0)^3 E_q Rq E_q*`,

`R0=F[1,s;s,1]F*`, `R1=tB`,

`R2=diag(y0,y1,y2,y3)`, `R3=diag(z0,z1,z2,z3)`,

`y0=y2=t^2/4`,

`y1=t^2/[4(1+s)]+s/2`, `y3=t^2/[4(1-s)]+s/2`,

`z0=z3=(1+s)^2/(4t)`, `z1=z2=(1-s)^2/(4t)`.

For0<s<1,t>0, the two high blocks have rank2 and are PSD: their nonzero eigenvalues are1±s and t,t. All eight low diagonal entries are positive. The four difference sectors are disjoint, giving rankR=2+2+4+4=12.

Their traces give EXACTLY

`N=2+2t+s+t^2(2-s^2)/[2(1-s^2)]+(1+s^2)/t>0`.

Indeed sum y=s+t^2/2+t^2/[2(1-s^2)], and sum z=(1+s^2)/t. Thus R/N is an actual trace-one PSD state. No reverse-peel theorem from the omitted part of the eligibility paper is needed for this calculation.

The classified CLOSED rectangle is

`1/2<=s<=2/3`, `9/10<=t<=11/10`.

It lies strictly inside the nonsingular0<s<1,t>0 domain. No s/t endpoint in this rectangle is silently omitted.

## 3. Reconstruct ALL four COMPLEX partial-transpose blocks

The general entry of a difference block becomes `|r,k-q><k,r-q|` under Bob transpose, so the total index tau=r+k-q is preserved. On the basis |r,tau-r>, the exact shuffle is

`S_tau(r,k)=R_(r+k-tau)(r,k)`.

The actual high entries are

`R0(r,k)=[1+i^(r-k)+s(i^r+i^(-k))]/4`,

`R1(r,k)=t[1+i^(r-k)]/4`.

In particular R0 diagonals are `(h_plus/2,1/2,h_minus/2,1/2)`, where h_plus=1+s,h_minus=1-s. Its opposite entries are R0(0,2)=R0(2,0)=0, R0(1,3)=is/2,R0(3,1)=-is/2. R1's opposite entries are ALL zero. R2,R3 are diagonal.

Put c_t=t(1-i)/4.

- **tau0**, ordered high rows0,2 then low rows1,3: high block `diag(h_plus/2,h_minus/2)`, high-to-low block `c_t I2`, low block `[y1,is/2;-is/2,y3]`. The Schur complement is exactly `(s/2)[1,i;-i,1]`, PSD rank1. The high block is positive rank2, so S0 is PSD rank3. The SIGN of the imaginary low cross entry is fixed by R0(1,3)=is/2.
- **tau2**, ordered high rows1,3 then low rows2,0: high block `(1/2)I2`, high-to-low `c_t I2`, low `(t^2/4)I2`. Its Schur complement is zero because `|c_t|^2/(1/2)=t^2/4`. There are two disjoint rank1 blocks, so rankS2=2.
- **tau1**, pairs(high,low)=(1,0) and(3,2): for h=h_plus,h_minus respectively, the block is `[t/2,h(1+i)/4;h(1-i)/4,h^2/(4t)]`. Both diagonals are positive and the determinant is `h^2/8-h^2/8=0`. Each is rank1, hence rankS1=2.
- **tau3**, pairs(0,3) and(2,1): exactly the same respective h_plus,h_minus blocks, INCLUDING upper phase1+i, not just a rounded modulus. Thus rankS3=2.

This is exhaustive, not a selection of principal minors. Off-diagonal q2/q3 entries vanish; opposite high entries are precisely the ones listed; every other candidate matrix entry either is the displayed paired adjacent high entry or that unique tau0 imaginary cross term. All sixteen physical basis kets occur in the four total-index sectors, with no off-sector coupling. Therefore R/N is PPT and its PT rank is3+2+2+2=9 throughout the rectangle (indeed throughout0<s<1,t>0).

The nonzero is/2 opposite coherence in R0, absent in R1, also verifies the claimed additional asymmetry: joint X translation would send it to the zero R0(2,0), and J would move it to a high block with zero opposite coherence. The state is explicitly a four-difference-block/Z-twirled state; no extra X/J invariance is assumed. The PT rank9 cannot be supported in the old rank8 PT face. None of this imports the omitted peel material.

## 4. Literal prototype rank with BOTH kernels and the nonzero minor

Put H=1-s^2=h_plus h_minus, u=t^2, a=H/u>0, d=sqrt(t/8), and A=A_h=sqrt(h/8), h=h_plus or h_minus. Define

`b_h=(i-1)(1-a)d^2/A`,

`c_h=(1+i)(1-1/sqrt2)A^3/(a d^2)`,

`e_h=(1+i)a d^3/A^2`,

`f_h=-i sqrt2 A^2/d`.

For nonzero complex w, the source matrix is

`M_h(w)=[2A,0,0,(1+i)dw;`

`        2idw,(1+i)A,0,b_h w^2;`

`        0,(i-1)dw,0,e_h w^3;`

`        f_h w^-1,c_h w^-2,0,(1-i)A]`.

Column2 is zero, so the FIRST literal null vector is e2. The SECOND is

`xi_h=(1,-a(d/A)(1+i)w,0,-(A/d)(1-i)w^-1)^T`.

Here are all four row products, after removal of their indicated common powers1,w,w^2,w^-1:

`2A-A(1+i)(1-i)=0`,

`2id-2iad-2id(1-a)=0`,

`2a d^2/A-e_h(A/d)(1-i)=0`,

`f_h-a(d/A)(1+i)c_h+2iA^2/d=0`.

The third uses (i-1)(1+i)=-2 and (1+i)(1-i)=2. In the fourth, the middle term is `2i(1-1/sqrt2)A^2/d=i(2-sqrt2)A^2/d`; together with f_h=-i sqrt2 A^2/d it cancels2iA^2/d exactly. No complex conjugate has been inserted into a kernel equation.

The vectors are independent because xi_0=1,xi_2=0. The rows0,1/columns0,1 minor is `2(1+i)A^2!=0`. Thus rankM_h(w) is EXACTLY2, not merely a possibly zero rank<=2 vector.

All denominators A,d,a,H,u,h_plus,h_minus are nonzero on the whole positive domain and therefore at every closed-rectangle endpoint. The factor1-a may vanish elsewhere but is not divided by; it causes no missed rank branch.

## 5. The minus prototype is an ACTUAL local-unitary shift, with transformed kernels

Use `M_plus=M_(h_plus)` and `M_minus=X^2 M_(h_minus) X^(-2)`. X is the cyclic shift. This moves EACH physical row AND column by2, preserving difference q. Since (X^2)^T=X^(-2)=X^2, it corresponds to the actual local-unitary transformation X^2 tensor X^2 of the coefficient vector, not an arbitrary relabeling of one subsystem.

For the minus prototype its literal kernels are

`e0`,

`X^2 xi_(h_minus)=(0,-(A_minus/d)(1-i)w^-1,1,-a(d/A_minus)(1+i)w)^T`.

They are independent; the shifted rows2,3/columns2,3 minor is the same nonzero `2(1+i)A_minus^2`. Thus every minus vector also has rank exactly2 over C.

The q0 high vector changes from A_h(1+i^j) to A_h(1-i^j), and q1 from d(i+i^j) to d(i-i^j), because i^(j-2)=-i^j. Low positions move

`13->31`, `31->13`, `23->01`, `30->12`.

These shifts, including their row positions, are the ones used in the population accounting below.

## 6. All SIX mod7 characters and EVERY cross term

Write the coefficient vector as six groups with exponents

`0: q0 high vector`, `1: q1 high vector`,

`2: b_h E13`, `-2: c_h E31`,

`3: e_h E23`, `-1: f_h E30`.

The residues are0,1,2,5,3,6, all distinct modulo7. For w running through ALL seventh roots of unity, `bar(w)=w^-1` and the projector cross term between groups k,l carries w^(k-l). If k!=l, its difference is nonzero modulo7 (indeed its absolute value is at most5), so its exact character sum vanishes. This includes high/high across q0/q1, EVERY high/low term, the two q2 low positions, the two q3 low positions and every low term across q2/q3. Within each coherent high group, all entries have the SAME exponent and are retained. Each low group is a single matrix unit.

The plus and minus families are averaged SEPARATELY and their projectors ADDED, not superposed as one vector, so there are no unaccounted plus/minus cross terms. This is an exact finite symbolic operator identity, not a seven-point approximation to universal positivity or an ensemble tool replay.

## 7. The high operator blocks match EXACTLY, not just their moments

The two retained q0 projectors are

`[(1+s)/8]P(u+v)+[(1-s)/8]P(u-v)`.

Expanding gives `(1/4)[P(u)+P(v)+s(|u><v|+|v><u|)]`, exactly F[1,s;s,1]F*. This includes the imaginary opposite coherence is/2, not just diagonal weights.

The q1 vectors are d(iu+v) and d(iu-v). Their projectors sum to `2d^2[P(u)+P(v)]`; since d^2=t/8, this is tB, with entries `t(1+i^(j-k))/4`. No further high Fourier component is discarded or inserted.

## 8. Every q2/q3 population and the exact residual operator

Let kappa=3-2sqrt2=(sqrt2-1)^2. Direct squared-modulus calculation gives

`B_h=|b_h|^2=(u-H)^2/(4h u)`,

`C_h=|c_h|^2=kappa u h^3/(8H^2)`,

`|e_h|^2=a^2 t^3/(4h^2)=(2-h)^2/(4t)`,

`|f_h|^2=h^2/(4t)`.

For C_h use `2(1-1/sqrt2)^2=kappa`, A^6=h^3/512 and a^2d^4=H^2/(64u). For e_h use H=h(2-h). These verify every denominator and coefficient, not just a positivity sign.

In q3, plus contributes row2 h_minus^2/(4t)=z2 and row3 h_plus^2/(4t)=z3. The shifted minus contributes row0 h_plus^2/(4t)=z0 and row1 h_minus^2/(4t)=z1. Thus ALL of R3 is exactly reproduced, including its nonuniform populations.

In q2, plus contributes B_plus at row1 and C_plus at row3. The shifted minus contributes C_minus at row1 and B_minus at row3. Rows0,2 receive no phase contribution. Therefore the EXACT remaining coefficients are

`r0=y0=u/4`, `r2=y2=u/4`,

`r1=y1-B_plus-C_minus`,

`r3=y3-C_plus-B_minus`.

With all cross terms already accounted for, this proves the OPERATOR identity itself:

`R=(1/7)sum_(w in Omega7)[P(vec M_plus(w))+P(vec M_minus(w))]`

`                      +sum_(j=0)^3 r_j P(j,j-2)`.

No unlisted matrix entry is being replaced by a diagonal or objective-moment equality.

## 9. Residual algebra and UNIFORM rational bounds on the CLOSED rectangle

Since H=h_plus h_minus, subtraction of B_h gives

`u/(4h_plus)-B_plus=h_minus/2-h_plus h_minus^2/(4u)`,

`u/(4h_minus)-B_minus=h_plus/2-h_minus h_plus^2/(4u)`.

After adding s/2 and subtracting the appropriate C term,

`r1=1/2-[h_plus h_minus^2/(4u)+kappa u h_minus/(8h_plus^2)]`,

`r3=1/2+s-[h_minus h_plus^2/(4u)+kappa u h_plus/(8h_minus^2)]`.

Throughout the ORIGINAL closed rectangle,

`81/100<=u<=121/100`, hence STRICTLY `4/5<u<5/4`,

`3/2<=h_plus<=5/3`, `1/3<=h_minus<=1/2`,

`0<kappa<1/5`.

The last strict bound follows from sqrt2>7/5, since49/25<2; positivity is its square definition. The relaxed u bounds remain STRICT at both actual endpoints, because81/100>4/5 and121/100<5/4.

For r1's first bracket term, h_plus<2,h_minus^2<=1/4 and1/u<5/4 give `<5/32`. For its second, use kappa<1/5,u<5/4,h_minus<=1/2,h_plus^2>=9/4 to get `<1/144`. Their sum is `<47/288`, so

`r1>97/288>0`.

For r3, h_minus<=1/2,h_plus^2<=25/9 and1/u<5/4 give the first term `<125/288`. The other term, using h_minus^2>=1/9, is `<15/32`. Their sum is `<65/72`; since1/2+s>=1,

`r3>7/72>0`.

Also `81/400<=r0=r2<=121/400`, so all four product residuals are uniformly positive. No original closed endpoint was changed to an open condition, and no numerical/program simplification was used.

## 10. Actual normalized nonuniform weights, with their sum proved

Each phase vector is nonzero rank2. For unit seventh roots its squared norm is independent of w, since its six entry groups have disjoint matrix support and |w|=1. Explicitly

`m_h=||M_h(w)||_F^2`

`   =h+t+B_h+C_h+[(2-h)^2+h^2]/(4t)`

`   =h+t+B_h+C_h+(1+s^2)/(2t)>0`.

The shifted minus has the same norm as M_(h_minus). Define unit vectors `psi_plus/minus(w)=vec M_plus/minus(w)/sqrt(m_plus/minus)`. The actual convex weights are

`lambda_plus/minus(w)=m_plus/minus/(7N)`,

`lambda_product,j=r_j/N` for the unit product ray |j,j-2>.

There are seven vectors in each phase family and four product vectors. The phase weights are NOT uniformly1/14; in particular positive residual weights remain. Their exact sum is1: m_plus+m_minus contributes the traces2+2t, all four phase q2 populations, and the entire sum z; sum r contributes sum y minus those same phase q2 populations. Together they are exactly N. Division by N gives total1.

Thus the identity is a genuine convex decomposition of R/N into fourteen Schmidt-rank2 rays plus four product rays on EVERY point of the closed rectangle. By definition of the Schmidt-number cone it proves SN AT MOST2. It does not prove exact SN2, separability failure, or an ensemble with rational-only vectors/weights. No numerical finite certificate, generated matrices or triple replay is being accepted.

## 11. The concrete Gaussian-integer/332 density is exactly identified

At s=1/2,t=1, the four blocks satisfy Kq=48Rq:

`K0(r,k)=12(1+i^(r-k))+6(i^r+i^(-k))`,

`K1(r,k)=12(1+i^(r-k))`,

`K2=diag(12,20,12,36)`, `K3=diag(27,3,3,27)`.

Indeed y=(1/4,5/12,1/4,3/4), z=(9/16,1/16,1/16,9/16), and the displayed high formula multiplied by48 gives exactly K0,K1. N=83/12; hence48N=332 and

`rho(1/2,1)=sum_q E_q Kq E_q*/332`.

The block traces are96,96,80,60, summing332. Every real and imaginary entry is an integer over332, not necessarily a real-rational entry. The theorem's algebraic phase vectors/weights decompose this density; Gaussian-rational density entries do not imply rational-only pure vectors. This is written identification, not a machine-generated matrix or certificate check.

## 12. Exact scientific disposition, imports and exclusions

The actual operator decomposition establishes that NO witness universally nonnegative on ALL complex Schmidt-rank<=2 vectors, of ANY form, can have negative expectation on a state in this rectangle. This follows from the explicit convex decomposition, not from a restricted witness family or a moment relaxation. It retires this exact rectangle as an SN3-target branch at the ordinary-written assurance level. It does not classify all0<s<1,t>0, arbitrary PPT states or P44.

The old24-phase region is UNSUPPLIED/NOT_RECONSTRUCTED here, and no conclusion about its proof is inherited. The217LF peel source is covered ONLY at originalLF1–61; its omitted rank-refinement/peel theorem and named Yang–Leung–Tang ancestry are NOT correctness inputs for the present decomposition. The15LF checkpoint's future gamma/template/replacement lead is a LEAD ONLY, not a reconstructed eligible state, separator or SN3 conclusion. No automatic older DAG closure, N4 UNKNOWN/exit-resource repair or old21-table recertification follows.

Ordinary imports actually needed are finite-dimensional complex linear algebra, vectorization/Schmidt-rank equality, local unitary invariance of rank, exact cyclic-character orthogonality, Schur-complement PSD with positive high block, and the definition of the Schmidt-number convex cone. All load-bearing kernels, phases, operator blocks, ranks, residual formulas, uniform bounds, weights and normalization have their actual derivations above. No new formula at that exact scope is left to a hash/headline or an unexecuted checker.

**Decision:** scoped no defect found in the full238LF analytic theorem and exact61LF eligibility domain. No formal/kernel, human/configured-family/cross-vendor, executable/triple-witness, novelty/SOTA or publication acceptance; no exactSN2, all-parameter/P44 no-go or actualSN3 claim. All permanent correction histories and HOLD remain; the original October27 cutoff/deadline is unchanged. This review is not roundcompletion. I return to the original semigroup faithful-band/CS-host lift at the actual checkpoint.
