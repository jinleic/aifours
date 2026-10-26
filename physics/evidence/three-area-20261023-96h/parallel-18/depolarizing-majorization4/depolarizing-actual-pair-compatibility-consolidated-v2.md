# Actual-pair compatibility: swap-sector energy, tight-face rigidity and the remaining strict quartic

Actual `/bin/date` before this consolidation: **Sun Oct 25 06:58:13 PDT 2026**. Owner PhysicsDepol4 / physics-2. **NEW WRITTEN CANDIDATE**, not separately reviewed or parent accepted. This is ONE consolidated successor after the next substantive actual-pair step. No prior pinned packet, review, checkpoint or parent record is edited.

**New result at the exact physical interface:** for every actual mixed/pure rho and complex rank-k orthogonal Pi, k=2,3,4,

`a=0 iff b=0`, and either equality forces `a=b=c=d=0`.     (FACE)

The a=0 quadratic-interior branch is therefore PHYSICALLY EMPTY. The entire U2-tight face b=0 is also nonviolating. The proof uses the actual factorization `omega=rho^T tensor Pi`, positivity, purity and projection geometry, not a four-number relaxation. It supplies a quantitative actual-state energy inequality as well.

**Still open:** D>=0 on the remaining actual positive-excess region a>b>0. No complete low-noise index and no actual counterexample is claimed.

## 1. Authority, exact variables and supplied support

Parent `depol-quartic-frontier-parent-v1.md`, observed SHA256 `47e727b0b6a03c4ac693057eec6c174d913c3174e1e3ccf6b0360cd33c8ec7a6`, and its receipt were read completely. The actual271-line reconstruction `stochastic-hinf-preview/peer-review-depol-exact-quartic-noise-v1.md`, SHA256 `c7d9656356d25326655619faeeb70f1f96eb58c26c89bc6e8b5fa14bce3502bf`, was read in full. The supported author consolidation has SHA256 `8b5ae28f34795f2b750e11e1c57f458935bb5af3fcb421bf531a7800878db4b1`.

Retain the actual unnormalized-identity maps

`X_j(rho)=sum_(|I|=j) rho_I tensor I_(I^c)`.

For the SAME actual density rho and rank-k complex orthogonal projector Pi, let

`r=Tr(Pi rho)`, `d=1-r`,

`a=3k+1-Tr(Pi X1)`, `b=3k+3-Tr(Pi X2)`,

`c=Tr(Pi X3)-(k+3)`.

The accepted scalar reduction says that for0<p<2/3, u=p/[2(1-p)], the actual channel trace gap satisfies

`G/a3=c-au²-bu-d/u=-q(u)/u`,

`q(u)=au³+bu²-cu+d`, `a3=(1-p)^3p/2>0`.

Its remaining interior test is

`D=27a²d²+18abcd+4b³d-b²c²-4ac³>=0`                    (Q4)

for a>0,0<c<3a+2b, with4bd>=c² at a=0. That exact scalar theorem is an import, not re-proved or confused with a physical inequality here.

New work below is WRITTEN reasoning only. No scientific interpreter/eval/arithmetic or symbolic program, enumeration, sampling, replay, solver, CLI, nested agent or GO was used. Static reading of the old U2 dual certificate suggested the swap-sector representation; its boolean fields and historical computations are NOT proof premises. The representation is derived explicitly below and is an analytic reconstruction of an old decomposable-certificate mechanism, not a new-priority claim.

## 2. An exact actual-product swap-sector identity

Define the linear map

`A(rho)=3 Tr(rho) I-X2(rho)+3rho`.

For a trace-one input this is `3I-X2+3rho`. This is NOT another unproved signed-map target: its positivity and its role in the actual-pair face are proved now.

Use input copy A and output copy B of four qubits. The Choi convention is

`J_Lambda=sum_(x,y) |x><y|_A tensor Lambda(|x><y|)_B`.

Let Gamma transpose ONLY the complete OUTPUT copy B. Let F_i swap input/output qubit i, acting identically on the other sites. The four F_i commute. The single-qubit maximally entangled vector is UNNORMALIZED, `|Omega_i>=|00>+|11>`, so `(|Omega_i><Omega_i|)^Gamma=F_i` without an extra factor.

Consequently

`J_A^Gamma=3I-sum_(i<j) F_iF_j+3F1F2F3F4`.             (1)

Indeed the trace-and-insert-identity map has Choi I; each two-retained-site X2 summand gives F_iF_j after Gamma; and the identity map gives the full swap product. This checks all normalization factors directly.

Let P2 be the projector onto the sum of the simultaneous swap eigenspaces with EXACTLY TWO antisymmetric sites:

`P2=sum_(|T|=2) product_(i in T)(I-F_i)/2`

`                    *product_(i notin T)(I+F_i)/2`.

On a swap-sign vector f_i=±1 with m negative signs, the eigenvalue of(1) is

`3-sum_(i<j)f_i f_j+3 product_i f_i`.

Using `sum_(i<j)f_i f_j=((sum_i f_i)^2-4)/2`, its five values for m=0,1,2,3,4 are respectively0,0,8,0,0. Hence EXACTLY

`J_A^Gamma=8P2>=0`.                                    (2)

Now use the ACTUAL product operator

`omega=rho^T tensor Pi`, `omega^Gamma=rho^T tensor Pi^T>=0`.

The Choi trace identity and output partial transpose give

`Tr(Pi A(rho))=Tr(omega J_A)`

`                  =8 Tr(P2 omega^Gamma)>=0`.           (3)

In particular A(rho)>=0, by choosing rank-one output projectors. At the actual deficit coordinates, (3) is the more precise identity

`b-3d=8 Tr(P2 omega^Gamma)>=0`.                         (ENERGY)

This retains the factorized state/projector origin of omega and its exact transposes. It is not a merely feasible PPT operator being declared physical.

An immediate analytic consequence is `X2(rho)<=3I+3rho`, and therefore `K_k(X2)<=3k+3` for1<=k<=5, exactly the product-reference sums there. Thus this particular inherited U2 range also has a short complete WRITTEN analytic proof; no rational-certificate replay is needed for this derivation. It is the old decomposable-certificate mechanism explicitly reconstructed, not a new scientific-priority assertion.

Identity(ENERGY) alone is also compatible with larger relaxations. The essential new tightness proof below uses purity, actual projection containment and true marginal compatibility in addition to it.

## 3. Pure-state compatibility needed at zero energy

This section is ONLY for a pure input `rho=|psi><psi|`. Let the one-qubit Bloch lengths be t_i, put `R=sum_i t_i²`, and let

`C=|<psi|sigma_y^tensor4|bar(psi)>|²`.

We need the exact identities

`sum_(|I|=2) Tr(rho_I²)=2+R+C`,

`<psi|A(rho)|psi>=4-R-C`,

`R+4C<=4`.                                             (4)

Here is a written derivation, not an import of a computed spectrum. Expand rho in Hermitian four-qubit Pauli strings and let A_j be the sum of squared coefficients of weight j, with A0=1,A1=R. Purity gives

`1+R+A2+A3+A4=16`.

For each pure one-versus-three cut the marginal purities agree. Summing those equalities gives

`(4+3R+2A2+A3)/8=(4+R)/2`,

so `A3=12+R-2A2` and `A4=3-2R+A2`.

Global spin flip reverses the odd Pauli sectors. Therefore

`C=(1-R+A2-A3+A4)/16=(A2-R-2)/4`,

and `A2=R+2+4C`. Summing the six two-qubit purities gives

`(6+3R+A2)/4=2+R+C`.

For a pure input `<psi|rho_I tensor I|psi>=Tr(rho_I²)`. Since rho²=rho, the middle formula in(4) follows from3−(2+R+C)+3.

For the last inequality, Schmidt-decompose across qubit i:

`psi=sqrt(mu)|0>alpha+sqrt(1-mu)|1>beta`.

The spin flip interchanges the two single-qubit basis vectors up to phases. Its overlap with psi consists of two cross terms, each with coefficient sqrt(mu(1-mu)), and each remaining inner product has modulus at most1. Thus

`C<=4mu(1-mu)=1-t_i²`.

If one Schmidt coefficient vanishes, the local spin-flipped factor is orthogonal and C=0, giving the same conclusion without dividing by a zero coefficient. Summing over the four sites proves R+4C<=4.

In particular

`4-R-C >= (3/4)(4-R)>=0`.                              (5)

No pure-state moment relation is imposed directly on a general mixed input.

## 4. Entire U2-tight face b=0: actual inputs, not relaxed tuples

Assume b=0. From(ENERGY), d=0. For a pure input, r=1 and Pi is an orthogonal projector, so psi belongs to Ran(Pi) EXACTLY; this is not an approximate-containment assumption.

Also `Tr(Pi A(rho))=b-3d=0`. A(rho)>=0, so its compression on Ran(Pi) vanishes. In particular

`<psi|A(rho)|psi>=0`.

Equations(4)–(5) give R+C=4 and R+4C<=4. Hence C=0 and R=4. Each t_i²<=1, so every one-qubit marginal is pure. Repeated Schmidt decomposition makes psi a physical pure product.

After physical local unitaries take that product to0000. The actual operator A has Hamming-sector eigenvalues

- vacuum: `3-6+3=0`;
- one excitation: `3-3=0`;
- two excitations: `3-1=2`;
- three/four excitations:3.

Thus `ker A=span{vacuum, four one-excitation vectors}`. Since Tr(Pi A)=0, Ran(Pi) lies in that FIVE-dimensional space. Since d=0 it also contains the vacuum. For k2,3,4, Pi therefore consists of the vacuum and an arbitrary complex(k−1)-plane in its one-excitation orthogonal complement.

On this exact subspace X1 has eigenvalues4 and3, X2 has6 and3, and X3 has4 and1. Consequently

`Tr(Pi X1)=4+3(k-1)=3k+1`,

`Tr(Pi X2)=6+3(k-1)=3k+3`,

`Tr(Pi X3)=4+(k-1)=k+3`, `Tr(Pi rho)=1`.

Thus a=b=c=d=0 for EVERY pure input with b=0.

For mixed rho, choose ANY finite pure decomposition `rho=sum_j lambda_j rho_j` with positive weights. At the SAME actual Pi, b is affine in rho and every component obeys `b_j>=3d_j>=0` by(ENERGY). Therefore b=0 forces each b_j=0. The pure argument gives a_j=c_j=d_j=0 for every component. Those quantities are also affine at fixed Pi, so a=c=d=0 for the original mixed input.

This extension averages ONLY linear traces/deficits; it does NOT average D-values or infer any quartic convexity.

## 5. Entire U1-tight face a=0, including exact mixed-state geometry

Here we independently characterize a=0 and prove the converse in(FACE).

Diagonalize each actual one-qubit marginal by local unitaries and order their Bloch lengths `t1>=t2>=t3>=t4>=0`. Then

`X1=2I+(1/2)sum_i t_i Z_i`.

Write T=sum t_i. Its leading signed sums correspond to the four smallest subset sums

`0, t4, t3, min(t2,t3+t4)`.

This ordering remains correct with zeros and ties, with multiplicities. It gives

`K2(X1)=4+t1+t2+t3`,

`K3(X1)=6+(3/2)(t1+t2)+(1/2)(t3+t4)`,

`K4(X1)=max{8+2t1+t2+t3+t4, 8+2(t1+t2)}`.             (6)

Each is bounded by3k+1. If a=0, both the state-dependent Ky-Fan bound and the actual Pi variational bound must be equalities.

### k3 and k4

Equality10 in K3's formula forces all four t_i=1 because all four displayed coefficients are strictly positive. For K4 the second expression is at most12, while the first is at most13 with equality only when all four t_i=1. Thus a=0 forces all one-qubit marginals pure and rho itself a pure product, even if it was initially called mixed.

For the product X1, the vacuum eigenvalue4 is separated from the Hamming-one eigenvalue3, itself separated from the next eigenvalue2. Equality in the actual rank-k variational trace requires Pi to contain the vacuum and have its remaining(k−1) dimensions in the Hamming-one space. This statement permits arbitrary COMPLEX subspaces inside the degenerate eigenspace; no computational-basis projector ansatz is imposed. The traces in §4 then give b=c=d=0.

### k2

Equation(6) forces t1=t2=t3=1 but permits arbitrary t4. Positivity of the density matrix means that a pure marginal fixes its tensor factor: if a marginal is P, the positive state has zero trace against I−P and is supported on P tensor the remaining space. Applying this three times gives the ACTUAL state

`rho=tau tensor |000><000|`,

up to physical local unitaries and a qubit permutation, for an arbitrary one-qubit density tau. This is not a marginal tuple being presumed realizable.

If tau is pure, the preceding pure-product projector geometry applies. If tau is mixed, write its eigenvalues mu>=nu>0. The two highest X1 eigenvalues are3+mu and3+nu, strictly above the next2+mu because their gap is2nu>0. Thus the ONLY actual rank-two maximizing projector is

`Pi=I_qubit tensor |000><000|`.

Its range contains rho's whole support. Compressing X2 to this range gives `3I+3tau`: three retained-pure-pair terms give3I and three mixed-qubit/pure-qubit terms give3tau. Compressing X3 gives `I+3tau`: erasing the mixed qubit gives I and erasing each pure qubit gives tau. Therefore

`Tr(Pi X2)=9`, `Tr(Pi X3)=5`, `r=1`.

Again b=c=d=0. The maximally mixed tau case is included; changing the basis within its two-dimensional top eigenspace does not change the projector.

Combining §§4–5 proves(FACE) for every actual mixed/pure input and arbitrary complex orthogonal Pi at k2,3,4:

`a=0 iff b=0`, and either forces `a=b=c=d=0`.

## 6. Quantitative actual-state compatibility away from the face

These inequalities retain actual input data; they are not replacements of the full quartic obligation.

### 6.1 U2 energy versus pure-state departure from product

For a pure input put p=Pi psi and q=(I−Pi)psi. Since A>=0 and

`A<=3I+3rho<=6I`,

the triangle inequality for A^(1/2) gives

`sqrt(4-R-C)<=sqrt(<p|A|p>)+sqrt(6d)`.

The positive compression Pi A Pi has largest eigenvalue at most its trace b−3d. Since ||p||²=1−d,

`<p|A|p><=(1-d)(b-3d)`.

Thus the ACTUAL pure pair obeys

`4-R-C <= [sqrt((1-d)(b-3d))+sqrt(6d)]²`.               (7)

Together with(5),

`4-R <= (4/3)[sqrt((1-d)(b-3d))+sqrt(6d)]²`.            (8)

At d=0 this gives `b>=4-R-C>=(3/4)(4-R)`. Small b and d therefore force genuine local purity, rather than merely permitting an arbitrary relaxation point near b=d=0. The inequalities include d=1 and all zero cases without dividing by1−d.

### 6.2 U1 energy gives actual product overlap

Let delta_i=1−t_i in the sorted order. Since actual Tr(Pi X1)<=K_k(X1), equation(6) yields

- k2: `a>=delta1+delta2+delta3`;
- k3: `a>=(3/2)(delta1+delta2)+(1/2)(delta3+delta4)`;
- k4 when a<1: `a>=2delta1+delta2+delta3+delta4`.

For the last statement, the alternative K4 branch has deficit at least1, so it cannot be the maximizing branch if a<1. These statements are valid for mixed inputs too.

Let P_i be a top marginal eigenprojector. The commuting-projector union bound gives

`Tr[rho product_i P_i]>=1-(1/2)sum_i delta_i`.

Consequently a pure input has some full product-vector overlap at least

- `max(0,1-a/2)` at k2: first project onto the top three qubits; the remaining projected pure vector fixes a one-qubit factor;
- `max(0,1-a)` at k3;
- `1-a/2` at k4 if a<1.

If the k2 three-qubit projection vanishes, its lower bound is already nonpositive and no normalization of a zero vector is used. These are quantitative compatibility consequences, not a new input-restricted substitute for the original target, and no unreviewed near-product theorem is imported to manufacture an index closure.

## 7. The remaining quartic frontier is strictly physical and strictly positive in a,b

Write

`s=Tr(Pi tilde(rho))>=0`,

where global spin flip is a positive state map. Inclusion-exclusion gives the EXACT same-pair identity

`c=a-b-d-s`.                                           (9)

Indeed `X3=I-X1+X2+rho-tilde(rho)` and direct substitution of the four deficits yields(9). Hence

`q(1)=a+b-c+d=2b+2d+s>=0`.

With(ENERGY) and the elementary U1 spectrum, the scalar reduction's deficit signs and endpoint can therefore also be supplied analytically for these k values, rather than read solely from an unreplayed historical certificate. This is a new written assurance route, not a claim of historical replay or priority.

The new physical face theorem has the following precise effect:

1. a=0 forces c=0, so the quadratic-interior branch `a=0,c>0` is EMPTY for actual pairs. Thus4bd>=c² holds there trivially, with all four deficits zero.
2. b=0 likewise forces c=0; no actual U2-tight violating pair exists.
3. Every hypothetical actual positive-excess pair has

`a>b>0`, `0<=3d<=b`, `c=a-b-d-s>0`.

In particular c<=a<3a+2b, so every actual c>0 pair is already in the strict a>0 interior branch of the accepted scalar theorem. The formerly automatic positive-c noninterior branch is physically empty.

Thus the STILL-OPEN universal problem is exactly to prove(Q4) for every remaining actual pair in this strict region, or supply a genuine rho,Pi with D<0 and its exact p*. There is no averaging of D.

Even the actual containment face d=0 with b>0 is not settled here. There, if c>0, the quartic would be `D=-c²(b²+4ac)<0`, giving a genuine counterexample. This observation identifies a necessary physical sub-obligation; it is not evidence that such a pair exists and not a narrowing of the complete d>=0 target. Proving the d=0 subcase alone would still leave the quantitative d>0 tradeoff.

No new relaxed tuple is constructed or offered. The previously displayed relaxation controls cannot be promoted to actual pairs: their b=0,c>0 pattern is now excluded by(FACE) using actual purity/projection structure. Positivity of a relaxed omega^Gamma by itself does not supply the missing factorization and rigidity proof.

## 8. Per-index ledger and exact remaining gap

|index|new actual-pair result|remaining target|
|---|---|---|
|k2|all a=0 and all b=0 actual pairs have a=b=c=d=0; quantitative(7)–(8) and product-overlap bound proved WRITTEN|D>=0 for every remaining actual a>b>0,c>0 pair, or actual strict failure; low-noise index OPEN|
|k3|same exact face rigidity and quantitative pure-state compatibility|same full remaining quartic obligation; low-noise index OPEN|
|k4|same exact face rigidity, with the stated a<1 product-overlap consequence|same full remaining quartic obligation; low-noise index OPEN|

There is no unrestricted all-p composition, no actual counterexample matrix and no solution count. The accepted central/high-noise statements retain their prior scopes; the newly explicit analytic U2/endpoint proofs require their own actual reconstruction before parent promotion.

## 9. Attribution, precision and assurance

The swap-sector/Choi decomposition is elementary and its coefficients are already implicit in the old U2 decomposable dual certificate. This packet's contribution is an explicit written physical energy identity and its actual tight-face/quantitative consequences, not a new mechanism or prior-art clearance. The pure sector-length/spin-flip tools are classical and fully derived above at the exact scope used.

Zhang's matched complementary clipped-tail ancestry and ambiguous public uniform-weight support remain binding through the unchanged source-audit-v2 note. No clean novelty claim is restored by replacing a computer-assisted certificate with a short written derivation.

The scalar p* formula is an exact real radical/rational expression for arbitrary real data. Algebraicity over Q is conditional on algebraic data, in particular rational matrix entries; no unconditional algebraicity claim is required for the scalar equivalence.

All new statements are WRITTEN, not formal/kernel, human, cross-vendor, executable or parent accepted. Static certificate reading is not replay. Pre-correction unadmitted computations remain disclosed with zero verification credit. HOLD/v7/v8, exclusive owned-root writes and the original deadline remain unchanged.

**Parkable current state:** the entire genuine a=0 branch and U2-tight b=0 face are closed at the WRITTEN level, with actual omega structure explicitly used. The full positive-a,positive-b physical quartic remains open. The next attack must establish that tradeoff or produce an actual strict failure, not restart signed-map targets, produce another relaxed tuple or silently replace the full state/projector quantifiers by a special ansatz.
