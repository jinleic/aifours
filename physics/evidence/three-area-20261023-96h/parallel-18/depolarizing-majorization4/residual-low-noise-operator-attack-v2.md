# Low-noise operator attack v2 — paired Werner–Holevo form and a false symmetry shortcut

Observed before creation: **2026-10-23T15:21:13-0700**. PhysicsDepol4. This resumes the one primary residual after the assigned SPR review, whose only MINOR has an actually read, hash-matched immutable repair. No scientific executable was run.

**Current accepted boundary:** parent `priority-written-dispositions-v1.md` §3 supports the all-state central theorem at its named written-check level. Its actual MathSemigroup return was read in full and independently hash-matched `48164f6ecc917835665331c8c9beab1d9dd51bd902d31fa0e273a0c137160841`. Full high-noise majorization retains the inherited certificate trust boundary; those certificates were not replayed. The genuine residual is k=2,3,4 for 0<p<2/3. The Zhang matched prior claim and **NOVELTY_UNCLEAR** qualification remain operative.

## 1. Aim and outcome of this bounded attack

The sufficient missing compatible-marginal inequality is still

`K_k(X_3(rho))<=k+3`, k=2,3,4, for every pure four-qubit rho.

A proof would finish the full channel target with the established X_2 bounds. A failure of this sufficient lemma would **not** automatically be a channel counterexample: it must still satisfy the exact common-projector/noise eligibility condition in `residual-low-noise-witness-profile-v1.md`.

This attack derives an exact, unrestricted two-ququart operator form and checks the tempting Schmidt-spectrum reduction. The form is valid, but that reduction is **false**, as shown by an exact endpoint control below. No remaining Ky-Fan inequality is proved here; the representation and shortcut failure must not be counted as solution progress or a new weaker input-region theorem.

## 2. Fixed two-qubit magic coordinates, explicitly normalized

Group the physical qubits as A=(1,2), B=(3,4). On either pair take the orthonormal basis

`e1=i(|00>+|11>)/sqrt(2)`,

`e2=(|00>-|11>)/sqrt(2)`,

`e3=(|01>+|10>)/sqrt(2)`,

`e4=i(|01>-|10>)/sqrt(2)`.

Every e_j is fixed by the two-qubit antiunitary `Theta_2=(sigma_y tensor sigma_y)K`, so Theta_2 is ordinary complex conjugation in these coordinates. Each of the six physical single-qubit Pauli operators on a pair is odd under Theta_2. Its matrix in this basis is therefore purely imaginary, Hermitian and transpose-skew. These six matrices are mutually Hilbert–Schmidt orthogonal, each of squared norm four.

The real vector space of imaginary Hermitian 4x4 skew matrices has dimension six. Let

`L_ab=i(|a><b|-|b><a|)`, a<b,

whose squared Hilbert–Schmidt norm is two. Consequently the six physical Pauli matrices and the six matrices sqrt(2)L_ab differ by a real orthogonal change of basis in this space. Summing their conjugation maps gives, for every complex 4x4 matrix X,

`sum_(six physical Pauli) S X S =2 sum_(a<b) L_ab X L_ab`

`                                =2[Tr(X)I_4-X^T]`.                (1)

The last identity is entrywise: its diagonal entry i is sum_(j!=i) X_jj and its off-diagonal (i,j) entry is -X_ji. This is an exact operator-basis identity, not an invocation of a numerical magic-basis transformation.

## 3. The exact unrestricted two-ququart form

Let rho now denote the same four-qubit state expressed in the fixed A:B bases above, with rho_A,rho_B its actual partial traces. All transposes below are in these **fixed** bases. Summing (1) on A and B yields the Pauli-error operator

`Z=sum_(i=1..4,a=x,y,z) sigma_a^(i)rho sigma_a^(i)`

` =2[I_A tensor rho_B+rho_A tensor I_B-rho^(T_A)-rho^(T_B)]`.        (2)

No partial-transpose positivity of rho is assumed. The combination on the right is positive because it is the explicitly derived sum of twelve positive conjugations. Its trace is twelve for trace-one rho.

Equivalently define the standard four-dimensional Werner–Holevo map

`W_4(X)=[Tr(X)I_4-X^T]/3`,

and `N=(W_4 tensor id+id tensor W_4)/2`. Then Z=12N(rho). The general map convention agrees with Eq.(1) of the primary [Roofeh–Karimipour 2310.15353v6](https://arxiv.org/html/2310.15353v6); no other claim in that paper is needed here, since the Kraus identity (1) is derived explicitly.

Using the exact physical identity `X_3=2rho+Z/2` gives

`F(rho):=X_3(rho)`

` =2rho+I_A tensor rho_B+rho_A tensor I_B-rho^(T_A)-rho^(T_B)`

` =2rho+6N(rho)`.                                                (3)

This is a positive trace-eight operator for every input, and is unitarily equivalent to the original X_3. Pure rho corresponds to an **arbitrary complex 4x4 coefficient matrix**, with no rank, reality or symmetry restriction. Thus a proof of `K_k(F)<=k+3` at k2,3,4 in these coordinates would genuinely cover the needed sufficient lemma; it is not a special physical input ansatz.

A still stronger sufficient estimate would be `K_k(N(rho))<=(k+1)/6`, because Ky-Fan subadditivity gives `K_k(2rho+6N(rho))<=2+6K_k(N(rho))`. That stronger inequality is the old Z-lemma in this representation; it is **not proved or assumed**.

## 4. Ordinary two-ququart Schmidt covariance is unavailable

Although W_4 is covariant, its covariance is contragredient:

`W_4(U X U^dagger)=bar(U) W_4(X) U^T`.

For an input transformed by U on A and V on B, the first N summand is conjugated on output by `bar(U) tensor V`, while the second is conjugated by `U tensor bar(V)`. In general these are different output unitaries. Thus the sum cannot be put into its original form by one common arbitrary U(4)xU(4) output conjugation. The additional term 2rho in (3) also carries the ordinary, not contragredient, conjugation.

The allowed real orthogonal changes in the magic coordinates are consistent, but replacing them silently by all local U(4) transformations would discard precisely the transpose-sensitive data. An ordinary bipartite Schmidt reduction does not establish the required Ky-Fan estimate.

## 5. Exact control showing the lost data matter

Both inputs below have A:B Schmidt spectrum `(1,0,0,0)`, but their X_3 spectra differ.

**Control B (two physical Bell pairs).** Take `psi_B=e1 tensor e1`. Up to a global phase this is Phi_+ on physical12 times Phi_+ on physical34. Since e1 is real in the magic coordinates,

`Z=2[(I-P_e1) tensor P_e1+P_e1 tensor(I-P_e1)]`.

The two displayed rank-three projections are orthogonal and orthogonal to rho_B. Therefore

`spec(X_3(psi_B))=(2,1,1,1,1,1,1,0,...,0)`.

Its trace is eight and its largest eigenvalue is two.

**Control P (four physical product qubits).** Let `u=(e1+i e2)/sqrt(2)=i|00>` and take `psi_P=u tensor u`, which is a physical pure product up to phase. Here u is orthogonal to bar(u). The same two rank-three projections now intersect in exactly span(psi_P); their other four directions are orthogonal. Equation (2) gives Z eigenvalue four on psi_P and eigenvalue two on those four directions. Hence

`spec(X_3(psi_P))=(4,1,1,1,1,0,...,0)`.

This is the required product reference spectrum. Yet both controls are rank-one product vectors across the paired A:B split and have the same ordinary Schmidt coefficients. Their X_3 spectra are not equal. Therefore any reduction asserting dependence only on those coefficients is rigorously false, not merely unproved. Both controls obey the conjectured inequality; neither is a channel counterexample or a newly discovered state family.

The data retained by the transpose terms include the self-overlaps `u^T u`, `v^T v`; these distinguish the two controls. Dropping them before a spectral argument is not a legitimate relaxation for a proof of the target.

## 6. Exact remaining inequality and scientific disposition

The unresolved operator obligation is now explicitly

`K_k(2|A><A|+I tensor rho_B+rho_A tensor I`

`       -(|A><A|)^(T_A)-(|A><A|)^(T_B))<=k+3`,

for **every normalized complex 4x4 A**, k2,3,4, retaining the fixed transpose structure. A two-sided Werner–Holevo Ky-Fan inequality or another argument controlling its transpose-sensitive interference is missing. No known primary theorem found in the bounded erasure/Pauli/WH searches supplied it; that search miss is not a statement of literature-wide openness.

This bounded attempt rules out one attractive but invalid Schmidt-spectrum shortcut and preserves an unrestricted exact representation. It does not close another input region, solve a surrogate norm problem, justify rerunning the old loose PPT encoding, or earn a new scientific-result count. The actual low-noise target remains open at the parent-supported central/high-noise boundary.
