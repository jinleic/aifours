# Mixed-parity all-N construction and proof

Date: 2026-10-14 PT. Verdict: **SOLVED for the precise theorem below**. Evidence label: **Certification** (complete written algebraic proof, exact controls, and independent hostile review). FRONTIER: **DELIVERY-READY** for correctness; **NOVELTY-UNCLEAR** for priority. No new-integrable-model or kernel-verification claim.

**Historical-openness qualification:** the final gate in STATUS.md assigns **PARTIAL-OVERLAP** to both `c3 != 0` and `c3=0`. This theorem was **previously unproved in this project**, not certified previously unsolved in the literature. The correctness verdict does not clear the user's “not solved yet” requirement.

## 1. Exact theorem and scope

Let the coefficient field have characteristic zero, or work with real/complex parameters. Fix

`p(k)=c1*k+c2*k^2+c3*k^3`, `c2 != 0`,

and `P=D_t+c1 D_x+c2 D_x^2+c3 D_x^3`. The quadratic branch `c3=0` is included.

For any finite N, choose a type `epsilon_i=+1` (F) or `-1` (G), an independent amplitude `A_i`, and wave numbers `k_i,l_i`. Put

`eta_i=k_i*x+l_i*y+w_i*t`,

where `w_i=-p(k_i)` for F type and `w_i=p(-k_i)` for G type. Constant phases can be included in `A_i`.

Write `k_S=sum_{i in S} k_i`, `l_S=sum_{i in S} l_i`, `w_S=sum_{i in S} w_i`, `kappa_S=(k_S,l_S,w_S)`, and `eta_S=sum_{i in S} eta_i`; empty sums are zero. The symbol `P(kappa)` means `w+p(k)` and does not depend on l.

**Theorem.** The coefficients below give finite tau functions

`F=sum_S F_S exp(eta_S)`, `G=sum_S G_S exp(eta_S)`

which satisfy, identically for every N and every type pattern,

`P F.G=0`, `D_y P F.G=0`.

They have `F_empty=G_empty=1`, F-type singletons `(F_i,G_i)=(A_i,0)`, and G-type singletons `(0,A_i)`. No relation between `k_i` and `l_i` is imposed, beyond avoiding the displayed denominators. The same formula at `l_i=k_i`, restricted to `y=0`, solves `P F.G=0`, `D_x P F.G=0`.

For the **generic Hirota N-soliton property**, additionally require the usual recursion determinants `-2 l_S P(kappa_S)P(-kappa_S)` to be nonzero for `|S|>=2` (replace `l_S` with `k_S` for the reduction). The proof of the identities does not divide by these determinants; they are needed only to identify the formula with the unique generic recursive ansatz.

At the squarefree exponential `exp(eta_S)`, the endpoint coefficient matrix for the unknowns `(F_S,G_S)` is

```text
[[ P(kappa_S),          P(-kappa_S)       ],
 [ l_S*P(kappa_S),     -l_S*P(-kappa_S)   ]].
```

Its determinant is exactly the expression just stated.

This is the complete mixed-parity degree-two/three branch of the **scoped** all-N question. It does not settle arbitrary P, arbitrary higher-dimensional operator R, supersymmetric/discrete/q-deformed extensions, Lax integrability, elastic scattering, or regularity of logarithmic physical fields. Tau zeros are not forbidden. It is not a proof of the full book conjecture.

## 2. Closed coefficients, regular at the quadratic limit

Set

`lambda=3*c3/(2*c2)`.

Add an auxiliary index 0, preceding all physical indices, with `epsilon_0=+1`, `k_0=l_0=0`. This auxiliary index is **not** an extra physical soliton in the final formula. For distinct indices in this order define

```text
Q_ij(lambda) = (k_i-k_j)/(epsilon_i+lambda*(k_i+k_j)),       epsilon_i=epsilon_j,

Q_ij(lambda) = ((epsilon_i-epsilon_j)/2+lambda*(k_i-k_j))
              /(k_i+k_j),                                 epsilon_i != epsilon_j.
```

Let `a_i=(1+epsilon_i)/2` and `b_i=(1-epsilon_i)/2`, including index 0. Define antisymmetric kernels by their upper entries

```text
M_ij=(a_i*b_j*l_i-a_j*b_i*l_j)/(l_i+l_j),
N_ij=(b_i*a_j*l_i-b_j*a_i*l_j)/(l_i+l_j).
```

For an odd ordered set T, append a dummy `*` **last** with `M_i*=a_i`, `N_i*=b_i`; for even T do not append it. Denote this set by `T*`. The dummy has no k or l and is not included in Q-products. `Pf(empty)=1`.

For a physical subset S put

```text
d_S = sum_{i in S} epsilon_i,
W_S = (product_{i in S} A_i)
      (product_{i in S, epsilon_i=-1} k_i/(lambda*k_i-1)),
R_T = product_{i<j in T} Q_ij(lambda).
```

The coefficients are

```text
F_S = W_S R_S       Pf(M_{S*})          if d_S=1,
F_S = W_S R_{0+S}   Pf(M_{(0+S)*})      if d_S=0,
F_S = 0                                  otherwise;

G_S = W_S R_S       Pf(N_{S*})          if d_S=0,
G_S = W_S R_{0+S}   Pf(N_{(0+S)*})      if d_S=-1,
G_S = 0                                  otherwise.
```

Here `0+S` means index 0 followed by the physical indices in their original increasing order. This fixes every Pfaffian and pair-product sign. `code/tau_formula.py` implements this formula directly; the shared sibling verifier is not used to construct its coefficients.

**Domain.** Every denominator actually displayed in these formulas must be nonzero. A convenient generic domain has nonzero individual k and l, nonzero pair sums, and nonzero same-type factors `epsilon_i+lambda*(k_i+k_j)` and G factors `lambda*k_i-1`. These define a nonempty Zariski-open set for each N/type pattern. At `lambda=0` the same-type denominators are ±1 and G factors are -1: the formula is directly defined, not evaluated with a small floating parameter. Removable special cases outside this domain are not part of the generic claim.

For example, types F,G give

```text
F_12 = A1*A2*k1*l1*(2*c2+3*c3*k1-3*c3*k2)
       /((2*c2+3*c3*k1)*(k1+k2)*(l1+l2)),
G_12 = A1*A2*k2*l2*(2*c2+3*c3*k1-3*c3*k2)
       /((2*c2-3*c3*k2)*(k1+k2)*(l1+l2)).
```

At `c3=0` these become `A1*A2*k1*l1/((k1+k2)(l1+l2))` and its `k2*l2` counterpart. Same-type pairs have both coefficients zero. These expressions match an independent symbolic solution of the two pair equations.

## 3. Dimension-independent Pfaffian lemma

This section supplies the algebraic foundation instead of assuming the sibling's formerly conjectured odd-cubic formula. The block-matrix argument was developed concurrently with that worker; the derivative and sign identities below were independently derived here. It is shared standard Pfaffian algebra, not a second claimed discovery.

For an even antisymmetric matrix H, define

`[u1,...,u(2m)]_H = Pf([[H,U],[-U^T,0]])`,

where U has the listed vector columns in order; `[]_H=Pf(H)`. Write `u wedge v = u v^T-v u^T`. The identities needed are

```text
Pf(H+u wedge v) = Pf(H)-[u,v]_H,                         (3.1)
[V]_{H+u wedge v} = [V]_H-[u,v,V]_H,                     (3.2)
Pf(H)[u,v,w,z]_H = [u,v]_H[w,z]_H
                    -[u,w]_H[v,z]_H+[u,z]_H[v,w]_H.    (3.3)
```

For (3.1)–(3.2), expand the Pfaffian as alternating pairings: two occurrences of the decomposable two-form `u wedge v` vanish, and the one-occurrence contribution has the displayed minus sign. The sign can also be checked in dimension two, where `[u,v]_H=-u1*v2+u2*v1`. For invertible H, the block Pfaffian formula gives `[V]_H=Pf(H)Pf(V^T H^-1 V)`, and expansion of the 4-by-4 Pfaffian proves (3.3). Polynomial continuation proves it at singular H too. No invertibility is assumed in the lemma below.

Suppose vectors `r_j` obey `(r_j)_X=r_(j+1)`, `(r_j)_s=r_(j+3)`, and

`H_X=r1 wedge r0`, `H_s=r3 wedge r0-2*r2 wedge r1`.

For v independent of X,s, set `tau=Pf(H)`, `h=[r0,v]_H`. Differentiating (3.1)–(3.2) yields

```text
tau_X=[01],        tau_XX=[02],
tau_XXX=[03]+[12], tau_s=[03]-2[12],
h_X=[1v],          h_XX=[2v],
h_XXX=[3v]+[012v], h_s=[3v]-2[012v].
```

Brackets abbreviate r-vector indices. Thus

```text
(D_X^3-D_s) tau.h
  =3([12][0v]-[02][1v]+[01][2v]-tau[012v])=0
```

by (3.3). This is an all-dimension identity, proved without division.

## 4. A proved auxiliary odd-cubic family

We require only a typed specialization later, but prove the following finite-dimensional construction with arbitrary amplitudes. Fix M spectral parameters r_i, transverse parameters l_i, constants a_i,b_i, and an odd polynomial

`p0(r)=v*r+c3*r^3`, `c3 != 0`.

Use `X=x-v*t`, `s=-c3*t`, `f_i=exp(r_i X+r_i^3 s)`, `h_i=exp(l_i y)`, `alpha_i=a_i h_i`, `beta_i=b_i h_i`. Define

```text
A_ij=((r_i-r_j)/(r_i+r_j))*f_i*f_j,
B_ij=(l_i*alpha_i*beta_j-l_j*alpha_j*beta_i)/(l_i+l_j),
K=[[A,I],[-I,-B]],
q=(f,0), a=(0,alpha), b=(0,beta),
L=K+q wedge a, r0=q+a,
r_j=(r_i^j f_i,0) for j>=1,
sigma=(-1)^(M*(M-1)/2).
```

The two tau functions are

`Fhat=sigma Pf(L)`,

`Ghat=sigma(Pf(L)+[r0,a-b]_L)`.

### 4.1 Both bilinear equations hold for every M

The Cauchy factor in A gives directly

`L_X=r1 wedge r0`, `L_s=r3 wedge r0-2*r2 wedge r1`.

The lemma applied with `v=a-b`, together with oddness of `D_X^3-D_s`, proves `(D_X^3-D_s)Fhat.Ghat=0`.

To prove the transverse equation rather than assume it, put

`J=L-r0 wedge(a-b)=K+(q+a) wedge b`.

By (3.1), `Ghat=sigma Pf(J)`. Since `B_y=alpha_y wedge beta`, we have `K_y=-a_y wedge b`, and consequently

`J_y=(q+a) wedge b_y=r0 wedge b_y`.

Therefore `Ghat_y=-sigma[r0,b_y]_J=-sigma[r0,b_y]_L`: the second equality follows from (3.2), since the correction contains r0 twice. Applying the same lemma with `v=b_y` gives `(D_X^3-D_s)Fhat.Ghat_y=0`. Differentiating the first equation in y also gives `(D_X^3-D_s)Fhat_y.Ghat=0`. Subtracting these two equations proves

`D_y(D_X^3-D_s)Fhat.Ghat=0`.

Finally `P0=D_t+v D_x+c3 D_x^3=c3(D_X^3-D_s)` in these coordinates. Both desired P0 equations follow. No tau or amplitude is divided out.

### 4.2 Subset dictionary and zero-amplitude specialization

For any even subset T, the block minor sum is

```text
sigma Pf([[A,I],[-I,-B]]) = sum_{T even} Pf(A_T)Pf(B_T).  (4.1)
```

In a pairing expansion every identity-block edge matches the same index across blocks. Thus the indices used internally in the two blocks coincide. If `|T|=2m`, their reordering sign is `sigma*(-1)^m`, canceled by `Pf(-B_T)=(-1)^m Pf(B_T)`, proving (4.1).

For odd subsets, append a dummy index to both blocks with A-border f and B-border alpha and the new identity entry 1. Moving the extra top-block index past the original bottom block contributes `(-1)^M`, exactly the ratio of the two sigma signs. Expansion in the final identity entry yields

`Fhat=sigma(Pf(K)-[q,a]_K)`.

Schur's Pfaffian identity gives `Pf(((r_i-r_j)/(r_i+r_j))_T)=product_{i<j in T}(r_i-r_j)/(r_i+r_j)`. One elementary proof compares poles at `r_m=-r_j` and uses induction; their difference has no poles, is bounded at infinity, and vanishes when two r's coincide. For odd T append spectral value zero, whose border entries are 1, and use rational continuation for removable individual-zero cases.

It follows that

```text
Fhat_T = R_T(r) Pf(M0_{T*}),
Ghat_T = R_T(r) Pf(N0_{T*}),
R_T(r)=product_{i<j in T}(r_i-r_j)/(r_i+r_j),
M0_ij=(l_i*a_i*b_j-l_j*a_j*b_i)/(l_i+l_j), M0_i*=a_i,
N0_ij=(l_i*b_i*a_j-l_j*b_j*a_i)/(l_i+l_j), N0_i*=b_i.
```

The coefficient multiplies `exp(sum theta_i)`, `theta_i=r_i*x+l_i*y-p0(r_i)*t`. For G use `N=B-(alpha wedge beta)` in the lower block and (3.1)–(3.2); this gives `sigma(Pf(K)-[a,b]_K-[q,b]_K)`, equal to the Ghat expression above. This establishes the coefficient dictionary, including signs, without division by any b_i.

When each index is F-only or G-only, entries within a type vanish. Pairing counts show Fhat contains only total type charges 0 and +1, and Ghat only 0 and -1. This is an exact structural statement for all M, not a pattern inferred from small examples.

## 5. Gauge, charge projection, and the mixed seeds

First take `c3 != 0`. Define

```text
delta=c2/(3*c3)=1/(2*lambda),
v=c1-3*c3*delta^2,
p0(r)=v*r+c3*r^3,
r_0=delta, l_0=0,
r_i=k_i+epsilon_i*delta,
theta_0=delta*x-p0(delta)*t,
theta_i=r_i*x+l_i*y-p0(r_i)*t.
```

The exact polynomial identity is

`p(k)=p0(k+delta)-p0(delta)`.

Using oddness of p0, this gives `eta_i=theta_i-epsilon_i*theta_0` for **both** F and G types, with exactly the dispersions stated in §1. This explicitly accounts for the shifted background.

Introduce a formal nonzero charge variable u. In the proved auxiliary family of §4 with indices `0,1,...,N`, set

```text
(a_0,b_0)=(u,0),
(a_i,b_i)=(u*A_i,0)                                  for F type,
(a_i,b_i)=(0,u^(-1)*A_i*lambda*k_i/(lambda*k_i-1))    for G type.
```

The auxiliary `l_0=0` is legitimate: §4 needs only pair sums `l_i+l_j != 0`, not nonzero individual transverse parameters. It is a background device, not an illicit additional generic soliton.

By the charge counting just proved,

`Fhat=F0+u*Fplus`, `Ghat=G0+u^(-1)*Gminus`.

The coefficient of `u^1` in each bilinear identity is **only** the pair `Fplus.G0`. Hence `P0 Fplus.G0=0` and `D_y P0 Fplus.G0=0`. This projection is justified algebraically; no assertion that arbitrary coefficients of two tau functions remain a solution is used.

Define the physical mixed tau functions

`F=exp(-theta_0)*Fplus`, `G=G0`.

Hirota's exponential-shift rule gives

```text
P0(D)(exp(theta_0)F).G
 =exp(theta_0) P0(D_x+delta,D_t-p0(delta))F.G
 =exp(theta_0) P(D_x,D_t)F.G.
```

The auxiliary phase has no y dependence, so the same relation holds with D_y. Therefore F,G solve the mixed system.

The constant term of F comes from the auxiliary singleton and is 1; the constant term of G is the empty subset. An F-type physical singleton comes from Fplus without the auxiliary index and has amplitude A_i. A G-type singleton comes from the balanced auxiliary-F/physical-G pair in G0. Its coefficient is

`((r_i-delta)/(r_i+delta)) * A_i*lambda*k_i/(lambda*k_i-1) = A_i`.

Its F coefficient is zero by charge counting. Thus all generic one-sided seed patterns and independent active amplitudes are realized, not merely a constrained subclass.

## 6. Why the coefficient formula includes c3=0

For a term selected by the charge projection, its full index set T (possibly including the auxiliary index) has `m` F-type and `n` G-type entries with `m=n` or `m=n+1`. In the spectral product R_T(r),

- each same-type pair contributes `lambda*Q_ij`;
- each opposite-type pair contributes `lambda^(-1)*Q_ij`;
- each G amplitude contributes `lambda*A_i*k_i/(lambda*k_i-1)`.

The total power of lambda is

`binomial(m,2)+binomial(n,2)-m*n+n = (m-n)(m-n-1)/2 = 0`.

After canceling these powers **symbolically**, the remaining terms are precisely §2. The choice of T is determined by charge: F uses S when `d_S=1` and `0+S` when `d_S=0`; G uses S when `d_S=0` and `0+S` when `d_S=-1`.

The apparently divergent background phase also cancels **before** specializing lambda: `theta_T-theta_0=eta_S` for F terms and `theta_T=eta_S` for G terms, because the retained full-set charges are respectively 1 and 0. Thus no hidden exponential containing `1/lambda` remains in the final formula.

The coefficients in §2 are rational functions of lambda regular at zero on the stated generic k,l domain. Moreover `c3=(2*c2/3)*lambda`, and both physical dispersions are polynomial in lambda. Every bilinear coefficient is therefore a rational function regular at zero. It vanishes for generic nonzero lambda by §5, hence is the zero rational function and vanishes at lambda=0 as well. This proves the **quadratic branch for arbitrary N**, not just a fixed-N limit calculation.

## 7. Genericity, uniqueness, and diagonal reduction

For generic nonzero k and l, `p(k)+p(-k)=2*c2*k^2 != 0`, so the one-soliton equations force exactly the two one-sided seed types used here. We did not discard a generic two-amplitude branch: such a branch belongs to odd p, not `c2 != 0`.

For each subset with at least two elements, neither `P(kappa_S)` nor `P(-kappa_S)` is the zero polynomial in the free k's. For `deg p=d`, their top-degree part contains a mixed monomial `k_i^(d-1)*k_j` with coefficient `+d*c_d` or `-d*c_d`; the individual dispersion contributions contain no such mixed monomial. Thus the determinant nonvanishing conditions, and all displayed coefficient denominators, hold on a nonempty generic domain. The same is true after `l_i=k_i`. On that domain the shared recursion is unique, so the explicit solution proves its generic all-N test passes for every type pattern.

For the reduction, choose `l_i=k_i`. The final F,G depend on x,y through `x+y`, so D_y and D_x coincide on the pair. Restricting to y=0 yields the (1+1)-dimensional system with the same coefficients. This is not the erroneous substitution `F(x,x,t)` without rescaling.

## 8. Exact controls actually exercised

Command, from this folder:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/verify.py
```

Observed output:

```text
PASS: symbolic mixed pair, gauge identity, and arbitrary-cardinality alpha cancellation.
PASS: 12 independent polynomial-differentiation cases, cubic and quadratic.
PASS: 444 exact cases through N=7; all type patterns through N=5; formula equals shared recursion and every residual is zero.
PASS: 2 negative controls rejected. All-N claim rests on the written Pfaffian proof, not these samples.
```

The code's variable `alpha` denotes the mathematical lambda above. Three coefficient triples `(c1,c2,c3)` were fixed: `(1,3,2)`, `(-2,5,-3)`, `(4,7,0)`. Both D_y and reduced D_x systems were checked. All type patterns were used for N=1 through 5; six specified patterns for N=6 and 7. Parameters and every case are recorded in `results/verification.json`, along with the read-only shared verifier's SHA-256. The source `../phys-bilinear-higher-dim-integrability/code/hirota_ns.py` was imported, not copied or changed.

The independent small checks use ordinary polynomial differentiation and the binomial definition of Hirota derivatives on formal exponential variables, not the shared difference-symbol evaluator. Negative controls perturb a pair coefficient and give a G seed the wrong dispersion; both are rejected.

Finite controls have label **Empirical evidence** for the general formula and **Certification** only of those exact instances and symbolic identities. The arbitrary-N theorem is the written proof in §§3–7. No Lean/kernel verification is claimed.

## 9. Verdict, novelty, and review

The complete written proof closes the stated mixed-parity generic all-N construction obligation. The full book conjecture remains outside scope. Operator-level gauge equivalence with the known odd-cubic model is explicit, so this is not a claim of a new integrable model. The exact prior-art status of this parameterized seed family is unresolved because Peng et al.'s full paper was not accessible; see STATUS.md.

### Independent review and dispositions

The configured **gpt-6.1-sol / max** reviewer ran through Codex CLI 0.162.1 in a **read-only** sandbox and exited 0. Its unedited report is `review/codex-review.md`; prompt and frozen input hashes are in `review/codex-prompt.md` and `review/invocation.json`.

- **Verdict: CORRECT.** The reviewer identified no mathematical gap or counterexample and no remaining unproved step within the stated theorem.
- **Checks accepted:** rank-two Pfaffian signs and singular matrices; minor-sum dictionary; the separate transverse identity; unique charge-coefficient projection; both time signs and seed normalization; cancellation of the divergent background before the all-N quadratic specialization; every type pattern and doubled exponential coefficients.
- **Finding 5, low severity:** recursion notation `kappa_S` and its endpoint matrix were implicit. **Disposition: fixed.** §1 now defines all subset sums and displays the 2-by-2 matrix. The determinant and construction did not change.
- **Independent computations reported:** 12 rank-two/Jacobi checks in dimensions 0,2,4,6 including singular matrices; six direct Taylor checks of the bordered lemma; four block-dictionary/transverse checks; and 32 fresh coefficient cases with vacuum, singletons, cubic/quadratic branches, doubled exponents, zero amplitudes and a tau zero. The reviewer did not rerun the shared out-of-folder verifier and did not write files.
- **Trust boundary:** a written proof with model review and exact controls, not a Lean kernel certificate. The reviewer expressly accepted **SOLVED**, **Certification**, and **NOVELTY-UNCLEAR** with these qualifications. Prior-art completeness remains unverified.
- **Final changed-path replay:** after the review clarification and the vacuum-boundary addition, the command in §8 exited 0 and printed all four PASS lines again. The recorded symbolic block also includes `zero_soliton_vacuum=true`. No build, lint or formatter suite was run, and no shared source was modified.

### Final historical-openness gate

The literature-only gate appended to STATUS.md on 2026-10-14 leaves both coefficient branches at **PARTIAL-OVERLAP**. It separates the exact cubic equivalence to Hietarinta's a=0 pair from his inequivalent a≠0 pair, the exact quadratic equivalence to Li–Lou model (ii), and adjacent all-N sinh-Gordon/heat results whose generic F/G dictionary is not verified. Peng and several important older papers remain inaccessible in full. No primary source explicitly labels our complete seed statement open. The prior model review assessed mathematical correctness, not historical openness; no new mathematical construction or rerun was used to make this gate decision.
