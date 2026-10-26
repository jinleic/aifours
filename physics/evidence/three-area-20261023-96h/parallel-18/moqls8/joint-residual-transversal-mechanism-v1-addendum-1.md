# Joint residual addendum 1: fixed-cell range compressions exclude four strata

Observed pre-freeze clock: **2026-10-25T04:03:20-0700 PDT** (`/bin/date`). Owner PhysicsMOQLS8, physics-4. This is a NEW additive packet. The pinned `joint-residual-transversal-mechanism-v1.md`, SHA256 `8d2ab33eff4381be7f8e8bab97ce47df69fa83cbc686fe89c4143bfdfa6a3245`, remains unchanged under v28-B review. No verdict on that original is anticipated here.

**Status: AUTHOR-WRITTEN new exclusions, with the finite rational bookkeeping WRITTEN-checked-in-kernel as specified in §10.** The proof is not proof-assistant/kernel verification, independent review, parent acceptance, cross-vendor review or novelty clearance. No native scientific process, solver, background job, network, CLI, git operation or nested agent was used. The authorized owner eval kernel used integers and `fractions.Fraction` only. Global scientific-launch HOLD v2 remains binding.

## 1. Literal result and retained target

The target is the unrestricted ordinary five-MOQLS(8) problem. Here q3 means exactly three genuinely nonclassical members Q1,Q2,Q3 and two actual classical mates. All 64 entries, all row/column ONBs and every pair's full 64-cell product ONB remain premises. There is no phase, real, affine-net, catalogue or selected-support restriction.

For member s let a_s be its real projector-span dimension and f_s its COMPLETE multiplicity-8-ray count. Put r_s=8-f_s and b_s=a_s-f_s. The new conclusions for ANY member in ANY genuine q3 family are:

| Previously open selected stratum | New author-written disposition |
|---|---|
| f=4, r=4, b=10 (a=14) | EXCLUDED, §7.1 |
| f=4, r=4, b=9 (a=13) | EXCLUDED, §7.2 |
| f=5, r=3, b=9 (a=14) | EXCLUDED, §7.1 |
| f=5, r=3, b=8 (a=13) | EXCLUDED, §7.2 |
| f=4, r=4, b=8 (a=12) | NOT excluded; exact remaining joint parameter barriers in §9 |
| f=5, r=3, b=7 (a=12) | NOT excluded; reduced to TWO joint parameter patterns in §9 |

There is also NO q3 family with all three a_s=12 (§8). Thus this is genuine incremental exclusion, not another selected-square dimension bound or a claim that the quaternion control is a family.

The new representation is the compression of an ACTUAL orthogonal range projection, rather than a compression of the covariance contraction itself. Fixed-ray matchings in the OTHER two members determine its entries exactly. Its rank, trace, squared trace and a known constant direction then conflict on the four strata above.

## 2. Named imports and the complete small parameter boundary

Consumed at the existing same-harness written boundary:

- `proof-q3-component-span-reduction-v1.md`, SHA256 `8fbd48630a85b4976ccb841924d429a96f5e091b61c7aaacdd5b87087f2897da`, especially §§2–3, 9. Parent disposition: `institute/runs/three-area-2026-10-23-96h/wave-v20-q3-component-parent-v1.md`. This supplies component additivity, singleton=fixed-ray equivalence, ISOLATE2, b>=2d-1 generally and b>=2d in irreducible dimensions 3,4,5.
- The individually supported uniform a_s>=12 and covariance surplus sum(a_s-8)<=14, explicitly consumed in that same proof. The covariance derivation is `proof-global-gram-defect-v1.md`, SHA256 `3b54a3e46ceb9ffa9edccab28664e13e322f5b47707fdffb77a51beba9a608d8`, with mandatory `proof-global-gram-defect-v1-erratum-1.md`, SHA256 `ef32720fe1b7c64a8539d6ae8cf5d94a0605e10a002aeb8483a5a2ac8eeb5d59`.
- The actual two-classical-member four-net bridge, retained in the v16 C4NET parent section and the pinned joint-residual packet. No catalogue classification is consumed.

In q3, 12<=a_s<=14 and a_1+a_2+a_3<=38. The component bounds give the following COMPLETE possibilities before the new argument:

| a_s | possible f_s |
|---|---|
| 12 | 4,5 |
| 13 | 2,3,4,5 |
| 14 | 1,2,3,4,5 |

Indeed f=0 gives a>=15, f=1 gives a>=14, f=2 gives a>=13 (a six-component or two three-components), f=3 gives a>=13, and f=4 gives a>=12. f=5 uses uniform12; f=6/7 are impossible for a nonclassical member after taking ALL fixed rays, by ISOLATE2/maximality. These are necessary bounds, not classifications of the larger-span cones.

Consequently the only unordered span triples are (14,12,12), (13,13,12), (13,12,12), (12,12,12). This finite list follows from the full physical hypotheses, not from a search cutoff.

## 3. Fixed matchings form actual partial parallel classes

Write M_(s,i) for the eight occurrence cells of fixed ray i in Q_s. It meets every actual row, column and each classical-symbol line exactly once. The classical-symbol assertion follows because Q_s is an ONB on every such line and its residual vectors are perpendicular to every fixed ray.

Moreover, for t!=s, the vectors of Q_t on M_(s,i) are an ONB of the FULL C^8: all selected Q_s factors are the same ray, so full product orthogonality gives eight orthogonal Q_t vectors. This ONB must contain exactly one occurrence of EACH global fixed ray of Q_t. Therefore

`|M_(s,i) intersect M_(t,j)|=1`

for every pair of fixed rays from different members. These are actual full-vector ONBs; no projected frame is called a basis.

The four net parallel classes (rows, columns, two classical symbols) and any fixed-ray matchings from different quantum members have pairwise intersection at most one. In particular, among any six classes used below, two distinct cells share AT MOST one line.

Let C be the set of cells where all THREE quantum members have fixed rays; write c=|C|. Let N_k count cells where exactly k of these members have fixed rays. For F=f_1+f_2+f_3 and P=f_1 f_2+f_1 f_3+f_2 f_3, pair-intersection counting gives

`N_3=c; N_2=P-3c; N_1=8F-2P+3c; N_0=64-8F+P-c.`

More precisely the number of cells fixed ONLY in member s is

`N_(1,s)=f_s(8-f_t-f_u)+c >=0.`                         (COUNT)

A useful consequence is `c>=f_s(f_t+f_u-8)` whenever the right side is positive. This is genuine joint information absent from the quaternion selected-square control.

## 4. Range projections, the leftover projection and c<=d

Work on real cell space R^64. Put p=J/64. For a four-net parallel class let R_i be its line-constant orthogonal projection, with entries 1/8 on a common line and zero otherwise. The projection

`E4=I-R_1-R_2-R_3-R_4+3p`

has rank35. The covariance operators T_s=H_s/8-p of the three quantum members have mutually orthogonal ranges inside E4. Let Q_s denote the ORTHOGONAL PROJECTION onto range(T_s), not T_s itself. Then

`rank Q_s=a_s-1; Q_s Q_t=0; L=E4-Q_1-Q_2-Q_3`

is an orthogonal projection of rank

`d=38-(a_1+a_2+a_3)`, hence `d in {0,1,2}`.              (DEFICIT)

For fixed cells x,y of member s,

`Q_s[x,y]=(1/8) 1_(same fixed ray)-1/64.`

This follows from the actual Gram block J_8 on each fixed matching; its full Gram-range projection has J_8/8 on that block and no cross block to residual cells. Removing p gives Q_s. This is where actual range projections are essential; arbitrary covariance eigenvalues are not set to one.

For x,y in C, L has diagonal 7/32 and off-diagonal either 3/32 (no common line among the seven classes) or -1/32 (one common line). A 1-, 2- or 3-point principal matrix, multiplied by32, is positive definite: diagonal7 and each off-diagonal has absolute value<=3, so the 3-point case is strictly diagonally dominant, and the smaller cases are immediate. Rank(L)=d<=2 therefore implies

`c<=d.`                                                  (TRIPLE)

For clarity this is not a bound for arbitrary d; only d=0,1,2 occurs here.

One further parity input will be used. Let O be the cells with an ODD number of fixed quantum members, so |O|=N_1+c. Each actual net line has F fixed incidences. Hence every line meets O in parity F mod2. If F is odd then |O|>=8. If F is even and O is nonempty then |O|>=6: through any point of O, its four net lines require four DISTINCT other O-points; also |O| is even by summing one parallel class. For f=(4,4,4) and c=1, |O|=4, a contradiction. Equivalently the single triple point would require at least four single-fixed points, but only three exist.

## 5. The exact six-class compression

Fix selected member s and let t,u be the other two. Let Z_s be its 8r_s residual cells. Let A_s be the orthogonal projection onto the real Gram range of its RESIDUAL projectors, embedded by zero outside Z_s. This definition permits several residual components; its rank is b_s=a_s-f_s. It contains the normalized vector

`z_s=1_(Z_s)/sqrt(8r_s)`.

Indeed the residual projectors sum to 8 I_(r_s), so the residual Gram matrix has constant row sum8. The full Gram-range projection is A_s plus the f_s fixed-matching blocks. Thus A_s is perpendicular to L, and

`R_s=A_s+L`

is an actual orthogonal projection of rank m=b_s+d, containing z_s.

Let D_s consist of cells fixed in BOTH t,u but residual in s. Put p0=f_t, q0=f_u. Their p0*q0 fixed-matching intersections are all distinct, and deleting the c triple cells leaves

`n=|D_s|=p0*q0-c`.

On D_s, the fixed blocks of the selected member vanish. The range identity in §4 therefore determines the compression K_s=R_s[D_s,D_s] EXACTLY:

`K_s=I_(D_s)-(1/8) sum_(six classes) L_class[D_s,D_s]+6 J_(D_s)/64.`

The six classes are the four actual net classes and the fixed matchings of t and u. Consequently

`K_s[x,x]=11/32;`

`K_s[x,y]=-1/32 if x!=y share one of those lines;`

`K_s[x,y]=3/32 otherwise.`                                (K)

No local amplitudes or phases have been discarded to obtain this formula. It is an identity forced by the FULL physical family, not a proposed support encoding.

If e counts ORDERED distinct pairs in D_s sharing a six-class line, then

`tau=tr K_s=11n/32;`

`sigma=tr(K_s^2)=[121n+9n(n-1)-8e]/1024.`                 (MOMENTS)

For eight lines and n points, convexity of integer occupancies gives the sharp universal lower bound

`g8(n)=(8-v)w(w-1)+v w(w+1), where n=8w+v, 0<=v<8.`

In the p0-by-q0 intersection grid, deleting c points removes at most 2c(p0+q0-2) ordered rook pairs (pairs among deleted points only improve the bound). The other four parallel classes contribute at least 4g8(n), with no double counting. Therefore

`e>=e_min=(p0*q0-2c)(p0+q0-2)+4g8(n).`                    (EDGES)

## 6. The constant-aware rank inequality

Choose an orthonormal column basis V for range(R_s), with first column z_s. The positive matrix B=V^T diag(1_(D_s)) V has the same nonzero eigenvalues, trace and squared trace as K_s. Its first diagonal entry is

`mu=n/(8r_s)`.

Writing B in first-coordinate block form, the squared norm of the off-block is nonnegative and Cauchy–Schwarz on the remaining m-1 diagonal block eigenvalues gives

`sigma >= mu^2+(tau-mu)^2/(m-1).`                          (CONST)

All m here exceed1. This is valid even if the compression loses rank. Combining (MOMENTS), (EDGES), (CONST) gives the universal necessary inequality

`mu^2+(tau-mu)^2/(m-1) <= [121n+9n(n-1)-8e_min]/1024.`   (TEST)

The weaker rank inequality rank(K_s)>=tau^2/sigma is occasionally enough. K_s is a COMPRESSION of a projection, not assumed itself idempotent. The normalized residual constant, which is known to be in the actual range, makes (CONST) strictly stronger than using trace/rank alone.

## 7. Four complete per-residual exclusions

### 7.1 a=14: f4/b10 and f5/b9 are excluded

The other two spans must be12, and therefore each other f is4 or5. Here d=0, so c=0. By (COUNT), any pair of f-values summing above8 is impossible because the third f is positive. Thus an f5 member is impossible in this case; f5/b9 is excluded.

For selected f4/b10, all three f-values must then be4. Take D_s of size16. Here e_min=160, tau=11/2 and sigma<=11/4. Hence rank K_s>=11. But rank R_s=b_s+d=10. Contradiction. This excludes f4/b10 without assuming any classification of its rank-one cone.

The same method incidentally excludes a14/f3: r=5, b=11, m=11, n=16. The left side of (TEST) exceeds 11/4 by exactly 11/1000. a14/f1 and a14/f2 are NOT excluded.

### 7.2 a=13: f4/b9 and f5/b8 are excluded

There are exactly two possible other-span patterns.

**Other spans12,12 (d=1).** Their f-values are4 or5. A selected f5, or any other f5 together with selected f4, forces c>=4 by (COUNT), contradicting c<=1. Thus the only candidate is f=(4,4,4). The c=1 case is excluded by the four-net parity argument in §4. At c=0, D_s has16 cells and rank K_s>=11, while selected f4/b9 has rank R_s=b+d=10. Contradiction.

**Other spans13,12 (d=0).** Again c=0 and pairwise f-sums must be<=8. Since the a12 member has f>=4, selected f5 is impossible: f5/b8 is excluded.

For selected f4/b9, the a12 member must have f4. The other a13 member has f2, f3 or f4:

- Other f4: the 16-point compression gives rank>=11>9.
- Other f3: select the f4/b9 member. Then p0,q0=3,4; n=12; e_min=92; tau=33/8; sigma<=119/64. The elementary rank lower bound is 1089/119>9, contradicting b=9.
- Other f2: instead select THAT a13/f2 member. Its residual has r=6, b=11 and its other f-values are4,4. Thus n=16, m=11, mu=1/3, tau=11/2 and sigma<=11/4. But (CONST) requires sigma>=1001/360, exceeding 11/4 by **11/360**. Contradiction.

These cases exhaust the full physical possibilities and prove both a13 exclusions. The last case illustrates why retaining the known residual constant is material: trace/rank alone only reaches rank11 and would leave this case unresolved.

## 8. Additional whole-family exclusion: all three spans12

Now d=2 and each f is4 or5. Any f5 together with another f>=4 forces c>=4 by (COUNT), contradicting c<=2. Hence f=(4,4,4).

- c=0: the 16-point compression requires rank>=11, but b+d=8+2=10.
- c=1: excluded by four-net parity as above.
- c=2: D_s has14 cells. The lower bound e_min=120 gives tau=77/16 and sigma<=593/256. Here m=10 and mu=14/32=7/16. The constant-aware lower bound is 5341/2304, which exceeds 593/256 by **1/576**. Contradiction.

Thus NO genuine q3 family can have (a_1,a_2,a_3)=(12,12,12). This does not exclude the other three span patterns, and it does not prove a universal nonclassical span13 bound: a12 members still occur in the remaining necessary parameter patterns.

## 9. Exact remaining barriers for the two unexcluded residuals

The table below is the COMPLETE survivor list of the NECESSARY integer counts, c<=d, the elementary parity test and (TEST), up to permutation of quantum members. A pair (a,f) records a member's span and full fixed-ray count. These are NOT realizability claims, tensor witnesses, classicality failures or sufficient conditions. Every full product and line equation remains mandatory.

| Span/fixed-ray pairs of the three members | c | residuals still represented |
|---|---:|---|
| (14,1), (12,4), (12,4) | 0 | f4/b8 |
| (14,2), (12,4), (12,4) | 0 | f4/b8 |
| (13,2), (13,2), (12,4) | 0 | f4/b8 |
| (13,2), (13,3), (12,4) | 0 | f4/b8 |
| (13,3), (13,3), (12,4) | 0 | f4/b8 |
| (13,2), (12,4), (12,4) | 0 or1 | f4/b8 |
| (13,3), (12,4), (12,4) | 1 | f4/b8 |
| (13,2), (13,2), (12,5) | 0 | f5/b7 |
| (13,2), (13,3), (12,5) | 0 | f5/b7 |

In particular every nonclassical member with f>=4 now has a=12 at this AUTHOR-WRITTEN boundary, so the old six-stratum residual reduces to f4/r4/b8 and f5/r3/b7. There is at least one such member because the old whole-q3 reduction remains in force. The f5/r3/b7 case necessarily has two other a13 members, with fixed-ray counts (2,2) or (2,3), and c=0.

Exact barriers, not an implied closure:

1. The six-space b11 at (a,f)=(13,2) is the general connected lower-bound equality case, NOT one of the already excluded 3/4/5-component minimal cases. For other f-values (5,3), its constant-aware inequality misses exclusion by 69/2048 at the conservative e_min; nothing permits replacing that negative gap with a positive one. For (5,2) the negative gap is 1709/4608. A sharper actual six-space cone/channel or incidence theorem would be needed.
2. The r3/b7 selected case with other f=(2,3) has conservative constant-aware gap -341/1536; with (2,2), gap -845/3456. These do not contradict (TEST). Their full three-dimensional span is not assumed real, and the old U3-6 exclusion does not apply.
3. The r4/b8 survivors can have higher-span, low-fixed-ray mates or rank-one L. The projection entries are known only on the fixed-fixed intersection subset. No argument here fixes the unknown entries on the remaining cells or supplies full mates.
4. The pinned quaternion f4/b10 QLS control remains a valid selected-square control at its exact original scope: it has no classical mate and is ineligible for q3. The new f4/b10 exclusion USES two classical mates, both other quantum members, their fixed matchings and the global range budget; it does not contradict that control.

A proposed next representation is the actual six-space b11 equality cone or the rank-one deficit L together with its complete fixed-matching cross entries. Neither is established by the present inequality. This is a parkable exact barrier, not another uninformative finite-range extension.

## 10. Finite arithmetic actually exercised

All scientific work was written mathematics plus finite exact arithmetic in this owner's existing eval kernel. The latter used only Python integers, `fractions.Fraction` and `itertools.product`; no floats, solver, sympy, scientific subprocess or background job. The known-true control checked (11/2)^2/(11/4)=11 before applying the new inequalities. Exact operations exercised:

- the stated n/e_min/tau/sigma rational bounds for (p0,q0)=(4,4),(5,4),(5,5),(2,4),(3,4),(2,5),(3,5),(3,3);
- constant-aware positive margins 11/360, 11/1000, 1/576 and the negative margins named in §9;
- ALL108 combinations of the four ordered span patterns, their allowed f-values and c=0..d. This is finite PARAMETER bookkeeping, not enumeration of physical arrays or a witness search. Each tested necessary obstruction is fully derived above.

The checked counts were:

| ordered spans | count failure | parity failure | compression failure | surviving ordered parameter cases |
|---|---:|---:|---:|---:|
| (14,12,12) | 16 | 0 | 2 | 2 |
| (13,13,12) | 19 | 0 | 6 | 7 |
| (13,12,12) | 26 | 1 | 2 | 3 |
| (12,12,12) | 21 | 1 | 2 | 0 |

The seven (13,13,12) survivors include the two swaps of unequal first-two f-values; quotienting those swaps yields the §9 table. The three (13,12,12) survivors are (f,c)=(2,4,4;0), (2,4,4;1), (3,4,4;1).

For reproducibility, the finite check's mathematical predicates are exactly:

1. allowed f-values in §2 and d=38-sum(a);
2. for c=0..d, reject negative N_(1,s) or N_0;
3. put odd=sum_s N_(1,s)+c; reject odd<8 when F odd, or 0<odd<6 when F even;
4. for EACH s compute n=f_t f_u-c, e_min by (EDGES), m=a_s-f_s+d, tau=11n/32, mu=n/[8(8-f_s)], sigma_max by (MOMENTS); reject when the exact Fraction value mu^2+(tau-mu)^2/(m-1)-sigma_max is positive.

The four per-residual proofs in §7 and the whole-span proof in §8 are written without relying on an unseen enumeration. The finite table cross-checks their complete boundary and records exact failures of the method on the remaining patterns. No external checker, independent implementation, mathematical reviewer, Lean or parent reconstruction has yet accepted THIS addendum.

## 11. Scope and next acceptance boundary

New deliverable: four full-physical q3 stratum exclusions, one all-a12 exclusion, and exact remaining parameter barriers. Labels: WRITTEN for the new proof; WRITTEN-checked-in-kernel ONLY for the finite rational/integer arithmetic listed above. This terminology is NOT proof-kernel acceptance.

q1/q2, both remaining q3 strata and unrestricted classicality remain OPEN. Original A10 (all eighteen exact GB inputs), A11 (final composition acceptance), the three GB UNKNOWNs, native/runtime HOLD, proof retention/provenance and historical exit-attestation limitations are not changed. In particular physical exclusions do not imply Boolean UNSAT for an old necessary-condition formula. A separate additive gate assessment follows only after reading those precise authorities.

Before promotion, an actual reviewer must reconstruct the fixed-matching intersections, the distinction Q_s versus T_s, the orthogonal projection L, the six-class compression and its constant direction, and the complete cases in §§7–8. The review of the earlier pinned quaternion packet is not a review of these NEW claims.
