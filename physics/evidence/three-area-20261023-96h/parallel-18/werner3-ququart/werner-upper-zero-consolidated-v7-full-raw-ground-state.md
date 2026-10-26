# Werner upper zero — a GLOBAL full-raw ground-state mass inequality and exact new compatible completion

PhysicsResearch96h-2 / physics-1. **NEW immutable WRITTEN OWNER-CANDIDATE, not parent-read/reviewed/adopted.** Actual immediately preceding `/bin/date`: **Sun Oct 25 14:33:18 PDT 2026**, precreation observation only. Same ENTIRE all-positive-spectrum complex full mixed9/p12q6 target; no park/new slot/GO/deadline reset.

The new all-positive-spectrum theorem is a genuine pointwise mass comparison for the ACTUAL full raw q kernel, including the potentially negative commutator ROW SUMS. It yields a new exact full-raw compatible-square identity with different p weights from FALSE G13. **It does NOT yet prove E_full>=0 globally.** The remaining full p/q compatibility is kept explicitly; no positive component or false standalone certificate is promoted to the target.

All algebra/inequalities here are WRITTEN, not machine-checked. No scientific interpreter/eval/program, arithmetic/symbolic routine, enumeration, matrix solve, solver/replay, compilation, CLI or nested agent. Source/metadata only. V1–v11/HOLD and original October27 cutoff/deadline unchanged.

## 1. Named operative inputs, not false certificate premises

Use the actual raw operators/physical normalization from:

- `generic-upper-zero-operator-checkpoint-001-v1.md`, SHA256 `249c1becd5e89ff08a3badebaab8234f3e89d7cb7879430e8e9152eabff18a7e`: G1–G12, NOT G13. In particular the exact p row variance and cross pairing are used.
- Its ADDENDUM1 `1b0e9a523810b5fb29cfa3c53ad287112d19803dc8110913d1b1f975817e6eb5`: G13 is FALSE, not imported as a sign estimate.
- Its ADDENDUM2 `ef401cddef2d596c1b3bbd53bbfac3f05a48f53c3d43cf3f61c6b242b78cda64`: ENTIRE Qraw correction/commutator Gram and F3/F5. No entrywise inverse-order statement is imported.
- `full-spectrum-pair-condensation-v1.md`, `1a814168eec30b5a8698b669fceae33145862f58c1b380d0f6b679caecf8fe98`: actual K_full P4 and physical Schur equivalence P10, NOT unproved P11.
- `all-reference-four-residuals-v1.md`, `8f152a21a9b453241c672770b5f53bf9eb9fd3a777f65c760a48de7beceec277`: literal q/cross and final residual definitions, NOT their unproved signs.
- RUN/`wave-v24-werner-generic-parent-v1.md`, `55d24c07c592c8e2e3d5bdd06aa0ca2c6c1ce9d9d2a3a527398251c5b8d29248`: original written operative-identity/full-raw support, not this new proof. RUN=`institute/runs/three-area-2026-10-23-96h/`.

The region theorems in v4/v5/v6 are NOT mathematical premises of the new global mass/completion result. They remain distinct WRITTEN candidates at their exact import unions; no related review transfers acceptance here. Ordinary imports: Hermitian ground-state expansion of a finite symmetric Z-matrix, elementary AM–GM and algebraic inequalities, completion of complex Hermitian squares. Every new coefficient and sign argument is displayed.

## 2. All variables and actual raw kernel

Assume EVERY ci>0, sum ci²=1. Put

    xi=ci², di=1-xi, dij=(di+dj)/2,
    D=diag(di), Q=I-cc^T,
    r=(sum_i1/di)^(-1), W=e3(d)=1+2e2(x)-e3(x).

The p domain is ALL complex Zc=0, dimension12. The q domain is ALL complex symmetric zero-diagonal U, dimension6. Write

    Uij=ci*cj*z_ij, z_ij=z_ji,
    Fij=dij*Uij=w_ij*z_ij, w_ij=ci*cj*dij>0.

The actual q energy is

    Qraw(U)=(1/2)F^dagger K_full F,

with K_full diagonal3-2dij*dkl/W, shared entry -cj*ct/(2djt) between ij,it, and0 disjoint. The BASE kernel K_c has diagonal1+di*dj/dij² and shared entry -di*cj*ct/(2dij*dit). Its exact mass with w is

    m_ij=w_ij*(K_c*w)_ij=xi*xj*g_ij,
    g_ij=dij-(di-dj)²/4>=1/4.

Define the ACTUAL full-raw conductances and masses

    gammaF_(i;jt)=xi*xj*xt*dij*dit/(2djt)>0,
    mF_ij=w_ij*(K_full*w)_ij=xi*xj*gF_ij.                 (GFR1)

There are12 row-difference conductances, one for each adjacent pair of the six unordered edges. Ground-state expansion gives the EXACT full raw form

    2Qraw(U)=sum_edges mF_ij|z_ij|²
        +sum_i sum_(j<t;j,t!=i) gammaF_(i;jt)|z_ij-z_it|². (GFR2)

At this point positivity of mF is not presumed merely from K_full>0. It is proved next. Explicitly,

    gF_ij=dij²*(3-2dij*dkl/W)
          -(dij/2)*sum_(t!=i,j) xt*(dit/djt+djt/dit).     (GFR3)

This includes all shared-edge raw terms and therefore all commutator cross terms; it is not the raw correction's diagonal alone.

## 3. Exact mass difference, including its signed commutator rows

Let delta_ij=di-dj, S=di+dj, and let k,l be the complementary indices. Subtract the actual K_c entries from K_full and multiply by the ground-state weights. If A=diag(w)(K_full-K_c)diag(w), its shared entry is

    A_(ij,it)=-xi*xj*xt*(di-dj)*(di-dt)/(8djt).

Its diagonal is the sum of

    2xi*xj*dij²*(1/2-dij*dkl/W)
    and xi*xj*(di-dj)²/4.

These are exactly the diagonal raw remainder and commutator contributions with the correct factor2 for the kernel difference. Adding ALL row entries for edge ij yields

    gF_ij-g_ij
      = S²/(8W)*[2W-S(3-S)]
       +delta_ij²/4*
          [1-S*sum_(t!=i,j) xt/((di+dt)(dj+dt))].         (GFR4)

For the shared terms, the needed cancellation is

    (di-dt)/djt-(dj-dt)/dit
       =2(di-dj)(di+dj)/[(di+dt)(dj+dt)].

Thus(GFR4) is a direct row-sum identity, not an entrywise-positivity assumption about the commutator Gram. The bracket in its second line CAN be negative near some boundary directions. It must be paid; the next proof does so.

## 4. GLOBAL theorem: actual full masses dominate the base masses

Put

    T=2-S=xi+xj in(0,1), h=xi*xj, v=xk*xl.

Then sum_outside xt=1-T=S-1 and di*dj=S-1+h>=S-1. Each denominator (di+dt)(dj+dt)>=di*dj, so

    S*sum_outside xt/[(di+dt)(dj+dt)]<=S,

and the signed bracket in(GFR4) is at least -(S-1)=-(1-T). Also delta_ij²=(xi-xj)²<=T².

The exact normalized four-variable identity is

    W=1+2T(1-T)+(1+T)h+(2-T)v,
    2W-S(3-S)=3T(1-T)+2(1+T)h+2(2-T)v.                  (GFR5)

AM–GM gives h<=T²/4 and v<=(1-T)²/4, hence

    W<=3/2+3T(1-T)/4.

Consequently

    3S²-2WT
      >=3(2-T)²-2T[3/2+3T(1-T)/4]
       =(3/2)(1-T)(T+4)(2-T)>=0.                        (GFR6)

Combining the exact signed difference with these bounds gives

    gF_ij-g_ij
      >=3S²*T(1-T)/(8W)-T²(1-T)/4
       =T(1-T)/(8W)*(3S²-2WT)
      >=3T(1-T)²(T+4)(2-T)/(16W)>0.                     (GFR7)

Thus, for EVERY positive four-spectrum and EVERY edge,

    gF_ij>=g_ij>=1/4,
    mF_ij>=m_ij>0.                                      (GFR8)

The simple g bound follows by writing u=dij in[1/2,1] and |di-dj|<=2(1-u): g>=u-(1-u)²>=1/4. These are exact WRITTEN bounds, not an interpreter spot check.

Equivalently, on the ONE SPECIFIED positive ground-state vector,

    (K_full-K_c)w>=0 ENTRYWISE.                           (GFR9)

This is not K_full-K_c entrywise positive, not an entrywise-inverse order, and not a sign assertion for an arbitrary forcing vector. It is a new global weighted mass comparison. The q conductances/masses in(GFR2) are now all positive, giving a genuine full-raw ground-state representation.

## 5. Exact full-raw p/q pairing and all complex variables

For the actual p test introduce directed coordinates Tij=Zij/(ci*cj), including the diagonal. The condition Zc=0 is sum_j xj*Tij=0. Define

    gamma0_(i;jt)=di*xi*xj*xt/2,
    e_ij=ci*cj*(di*Zij+dj*Zji).

The imported exact row/cross identities are

    <Z,B'Z>=2sum_i;j<t gamma0_(i;jt)|Tij-Tit|²,
    <Z,QZ^TQ>=sum_ij conj(Zij)Zji,
    2Re<Z,h(U)>
      =-sqrt(2)Re sum_i;j<t gamma0_(i;jt)
                              conj(Tij-Tit)*(z_ij-z_it)
        -(1/sqrt(2))Re sum_edges conj(e_ij)*z_ij.          (GFR10)

All row differences are complex; no transpose symmetry/normality/reality restriction is placed on p. The q potentials have ONE common symmetric value for each unordered edge. They are not independent row variables.

Complete the actual raw graph squares using gammaF, and the mass squares using mF. The EXACT ENTIRE joint form is

    J_full(Z,z)=Praw_c(Z)
      +(1/2)sum_i;j<t gammaF_(i;jt)*
          |z_ij-z_it-beta_(i;jt)*(Tij-Tit)|²
      +(1/2)sum_edges mF_ij*|z_ij-a_ij(Z)|²,              (GFR11)

where

    beta_(i;jt)=sqrt(2)*gamma0/gammaF
               =sqrt(2)*di*djt/(dij*dit),
    a_ij(Z)=e_ij/(sqrt(2)*mF_ij).

The base p coefficient left by a graph square is2gamma0-gamma0²/gammaF. This is NOT the old constant-half coefficient. It simplifies to

    2gamma0-gamma0²/gammaF
      =xi*xj*xt*omega_(i;jt),
    omega_(i;jt)=di*(di²+dj*dt)/[(di+dj)(di+dt)].         (GFR12)

Indeed subtracting the fraction reduces the numerator to di²+dj*dt. Therefore the residual has a regular PHYSICAL expression

    Praw_c(Z)
      =sum_i;j<t omega_(i;jt)*|ct*Zij-cj*Zit|²
         +r*sum_ij conj(Zij)Zji
         -sum_edges |di*Zij+dj*Zji|²/(4gF_ij).            (GFR13)

The cancellation of xi*xj*xt uses

    Tij-Tit=(ct*Zij-cj*Zit)/(ci*cj*ct).

Thus(GFR13) itself has no division by an individual ci. The interior q chart is nevertheless the declared domain of the compatible-square identity, and no new boundary inverse is evaluated.

## 6. Useful new row structure, and what is NOT implied

The p variance weights have the exact factorization

    omega_(i;jt)=di*(a_ij*a_it+b_ij*b_it),
    a_ij=di/(di+dj), b_ij=dj/(di+dj), a_ij+b_ij=1.

Hence each row's remaining variance is a sum of TWO weighted Lagrange forms. It is positive as a row form, with0<omega<di. But omega is NOT asserted>=di/2 in every row. Middle-di rows can fall below that value. Thus one cannot import the old B'/2-Hodge budget unchanged, assume positivity of the swap term, or revive FALSE G13.

The exact original target is now, equivalently,

    E_full,c(Z)=Praw_c(Z)+min_(one complex symmetric z6)
          {THE TWO COMPATIBILITY SUMS IN(GFR11)}.         (GFR14)

The minimum is over ALL six q directions with the SAME z in every square. Its positive pivot is the actual full raw kernel in these coordinates. The varying beta centers are NOT assumed mutually integrable/attainable. No circulation-rank assertion from the old constant-center completion is automatically transferred.

A proof of Praw>=0 for all Zc=0 would be a valid SUFFICIENT certificate for the full target. It is NOT a necessary condition, is NOT proved in this packet, and a negative Praw would refute ONLY that new sufficient estimate. The actual minimum and full raw correction remain until the original E_full sign is proved or genuinely separated. This is not replacing the real task by an easier/stronger problem or suppressing a correction when an estimate fails.

Compared with false G13, BOTH ingredients have changed by an exact use of the FULL q operator: row coefficient di/2 becomes omega_(i;jt), and edge mass g becomes gF>=g. In particular the strong-row variance budget near a product vertex need not remain artificially halved. This is a documented new full-raw operator mechanism, not reuse of the known false certificate or an inconsequential spectrum enumeration.

## 7. Current entire frontier and acceptance boundary

New GLOBAL WRITTEN theorem: the explicit full-raw masses dominate the base masses with the positive lower gain(GFR7), paying the signed commutator rows rather than dropping them. New exact identity: the whole p12/q6 compatible completion(GFR11)–(GFR14), retaining actual output-c, all mixed terms and the common q6 minimization.

Still NOT_PROVED: actual E_full/Z_up on ALL positive spectra, including the remaining rank-three-face/core couplings; the new standalone Praw sufficient sign; other three canonical F_up/F_low/Z_low signs; whole asymmetric co-Choi route and unrestricted rank<=2 W4. No exact full-target falsifying spectrum or physical Werner witness. Negative old C+S forms or negative sufficient residuals would not answer these different targets.

The v4/v5/v6 WRITTEN candidates establish their stated boundary regions only, at their COMPLETE named import union. They remain unreviewed/unadopted as last consumed and are not declared all-simplex coverage. This packet does not promote them, and the unrelated v85/v88 review returns confer no physics acceptance.

All current new conclusions require actual complete-source reconstruction and parent disposition. No formal/kernel/human/configured-family/executable/triple-witness/novelty gate, scientific GO or park follows. Continue the SAME entire target under the unchanged2026-10-27 science cutoff11:05:38 PDT and delivery deadline12:35:38 PDT.
