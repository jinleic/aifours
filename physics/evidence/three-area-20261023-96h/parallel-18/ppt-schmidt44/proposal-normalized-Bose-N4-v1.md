# New preparation proposal — trace-corrected Bose certificate, N4

Observed clock before creation: **2026-10-23T14:57:16-07:00**. PhysicsPPT44 / physics-3. **NEW PREPARATION PROPOSAL ONLY; no approval or execution is inferred.** This is not the withdrawn bare-N2 experiment, not a silent N3 substitution, and not a P44 result.

The generic-kernel analysis now has a complete candidate SN2 region (`proof-generic-kernel-region-v1.md`, SHA `45dc404e005a74d7be5745df04539fbd89208ff4f8f22eefebd2514609dcda26`). The single proposed input x=(1,1,1,1) is honestly outside that region. A new certificate cone is needed because the entire bare Bose-lift PSD family has been proved PSD-only at every finite N in `proof-bare-Bose-lift-vacuity-v1.md`, SHA `7fab6757107cfc6a9ae11ac4adf6162ad5e1f26089831ff45570f2e69c8910b1`.

## 1. Material change: account for the canonical lifting trace

Use the **unnormalized** auxiliary vector `Omega_2=00+11`, or equivalently the singlet `S=01-10` after a fixed unitary on Alice's auxiliary qubit. Let

`Q_N(Y)=P_N [P(S)_(A0,B10) tensor Y_(A,B1) tensor I_spectators] P_N`,
`Q_N(I)=P_N [P(S) tensor I_physical] P_N`.

Unlike the bare condition, seek a Hermitian physical Y and scalar mu>=0 satisfying

`C_N(Y,mu):=Q_N(Y)+mu[I_Bose-2Q_N(I)] >=0`.                         (1)

The factor2 and the distinction between P(S) of trace2 and a normalized auxiliary projector are not optional conventions.

### Written implication: (1) certifies universal two-block-positivity

For an arbitrary normalized Schmidt-rank-at-most-two vector

`psi=s1 a1 tensor b1+s2 a2 tensor b2`,

with orthonormal local Schmidt vectors, nonnegative s_i, and `s1^2+s2^2=1`, put `ell=s1+s2`. Form

`A=sqrt(s1)|0,a1>+sqrt(s2)|1,a2>`,
`B=sqrt(s1)|0,b1>+sqrt(s2)|1,b2>`.

Their squared norms are ell. A fixed auxiliary unitary J on Alice, chosen so `(J tensor I)Omega_2=S`, preserves norms. Set

`A'=sqrt(ell) J A`, `B'=B/sqrt(ell)`.

Then `<S|_(aux)(A' tensor B')=psi`, `||B'||=1`, and `||A'||^2=ell^2<=2`. For every N,

`sigma_N=P(A') tensor P(B')^tensorN`

is positive and Bose-supported, has trace ell^2<=2, and its S-contraction onto A,B1 equals P(psi). Taking its expectation in (1) yields

`<psi|Y|psi> +mu(ell^2-2)>=0`,

hence `<psi|Y|psi>>=mu(2-ell^2)>=0`. Thus Y is two-block-positive over **all complex** rank-at-most-two vectors.

This is a genuinely changed trace-corrected certificate, not the source's bare finite sign test. It addresses the auxiliary-zero directions by retaining the canonical trace bound. The lift itself comes from Chen–Collins–Fawzi2505.22100v1 Lemma4/Eqs.(7)–(10), raw source SHA `c83cb1cc76311cc6bc41c41dfe0074a4d87732fcabbcdf466cead1a841c727f4`; the extra trace correction and its implication are derived here, not quoted as their theorem.

Normalize `Tr(Y)=16`. The certificate implies `<a,b|Y|a,b>>=mu` on every normalized product vector; summing a computational product basis proves mu<=1. Therefore `0<=mu<=1` is a justified compact scalar restriction, not a tuning choice.

## 2. Vacuity checks before proposing an assay

### The old obstruction still kills corrected N2

The all-level flag construction gives, for unit arbitrary physical psi, a Bose-supported unit vector whose expectation of Q_N(Y) is `<psi|Y|psi>/N` and whose expectation of Q_N(I) is1/N. Its expectation of (1) is

`<psi|Y|psi>/N +mu(1-2/N)`.

For N=2 the correction vanishes. Thus corrected N2 still forces Y>=0. It must not be run.

### Corrected N3 fails the maximally-entangled4 control

For an isotropic candidate `Y=gamma I-P(Omega_4)`, a necessary N3 condition obtained below is

`8/(4gamma-5mu)+2/(gamma+mu)<=1`,                                  (2)

with positive denominators. At gamma=4 and mu>0 the left side minus1 is

`(2mu+5mu^2)/[(16-5mu)(4+mu)]>0`.

At mu=0 it is4/gamma. Thus no gamma<4 can satisfy (2). Physical isotropic twirling preserves (1), so no candidate in this N3 cone detects the maximally-entangled4 state. This is a statement about that control, not proof that every N3 certificate is PSD-only. Nevertheless, N3 is not proposed as an uncalibrated intermediate assay.

### Corrected N4 has an exact non-PSD control certificate

At N=4 choose

`Y0=(31/8) I-P(Omega_4)`, `mu0=1/2`.

It has negative expectation `-1/8` on the normalized maximally-entangled4 state. Section3 derives an exact positivity certificate for (1), rather than asserting a numerical eigenvalue. After trace normalization use

`Yctrl=(31/29)I-(8/29)P(Omega_4)`, `muctrl=4/29`.

Then `Tr(Yctrl)=16` and its known negative control value is exactly `-1/29`.

This establishes **non-PSD headroom**, not indecomposable/PPT-detection headroom. Yctrl is a reduction-type witness; whether this N4 cone contains a useful indecomposable ququart witness is unknown. That uncertainty is precisely what a bounded single-input screen could investigate.

## 3. Exact control calculation and reduced matrix sizes

Everything in this section is a written derivation, not a numerical replay. On the Bose subspace, simultaneous auxiliary SU(2) acts on Alice's auxiliary and the N Bob auxiliaries. The singlet lift and (1) commute with this action.

Let b_(alpha,p) be the usual bosonic annihilator for auxiliary label alpha in{0,1} and physical label p in{0,...,d-1}. The contraction operator for the auxiliary singlet and physical Omega_d can be written

`L=(1/sqrt(N)) sum_(a,alpha,p) epsilon_(a,alpha) <a,p|_Alice tensor b_(alpha,p)`.

Consequently `Q_N(P(Omega_d))=L^*L` and, on the N-1 Bob output space,

`L L^*=(2d+N-1)/N * I`.                                           (3)

The latter follows directly from `sum b b^*=2d+(N-1)`.

For the control Y=gamma I-P(Omega_d), write

`D=(gamma-2mu)Q_N(I)+mu I`.

When D>0, positivity of (1) is equivalent to `L D^(-1)L^*<=I`.

On an output auxiliary spin-j sector, the possible Bob-input spins are j+1/2 and j-1/2. The corresponding Q_N(I) eigenvalues are

`q_plus=(N+2j+3)/(2N)`, `q_minus=(N-2j+1)/(2N)`.                    (4)

These follow from `Q_N(I)=1/2-(2/N) S_A dot S_B`. Let r,s be the squared norms of the two components of L^* applied to a unit output vector. They obey

`r+s=(2d+N-1)/N`,
`q_plus*r+q_minus*s=[(2d+N-1)(N+3)/2+2j(j+1)]/N^2`.                (5)

For completeness, the second identity follows by commuting total Bob spin through a creation operator:

`sum_(alpha,p) b_(alpha,p) S_B^2 b_(alpha,p)^*`
` =(2d+N+1)S_B^2+(3/4)(2d+N-1)I`

on the N-1 boson space, and using total auxiliary spin j and Alice spin1/2. Thus the scalar eigenvalue of `L D^(-1)L^*` is

`r/[mu+(gamma-2mu)q_plus]+s/[mu+(gamma-2mu)q_minus]`.                (6)

For N3,d4, output j=1 has `(q_plus,q_minus)=(4/3,1/3)` and `(r,s)=(8/3,2/3)`, giving necessary condition (2).

For N4,d4, the two output sectors are:

- j=3/2: `(q_plus,q_minus)=(5/4,1/4)`, `(r,s)=(35/16,9/16)`;
- j=1/2: `(q_plus,q_minus)=(1,1/2)`, `(r,s)=(9/4,1/2)`.

At gamma31/8, mu1/2, (6) equals respectively

`70/131+6/13=1696/1703<1`,
`2/3+8/31=86/93<1`.

D has minimum eigenvalue at least1/2. Therefore the unscaled control has the exact lower bound

`C_4(Y0,mu0)>=[7/3406] I_Bose`.

The trace-normalized control has the corresponding bound

`C_4(Yctrl,muctrl)>=[28/49387] I_Bose`.                              (7)

This supplies an exact positive anchor for the implementation, not a floating-point expectation of positivity.

### Constructive highest-weight reduction: two LMIs, sizes320 and260

The unreduced Bose support has dimension `8*binom(11,4)=2640`. Full auxiliary-spin sectors have J=5/2,3/2,1/2. On J=5/2 the auxiliary singlet term vanishes, and (1) is simply muI>=0. The nontrivial highest-weight multiplicities are320 and260, so only **two LMIs of those sizes** are needed.

The following explicit unnormalized bases avoid numerical diagonalization of a symmetry algebra. `Sym_B` denotes the average of the24 complete paired-Bob permutations; retain duplicate terms with their multiplicity.

For J=3/2, for every physical b in{0,...,3} and unordered physical triple T (20 choices), put

`U_(bT)=Sym_B(all four auxiliary labels0, physical multiset b+T)`,
`D_(b;T)=Sym_B(one auxiliary1 with physical b, the other three auxiliary0 with physical T)`.

Use `|0>_A0 D_(b;T)-|1>_A0 U_(bT)`, tensor each Alice physical basis vector. There are4*20*4=320 such vectors. The auxiliary raising operator sends both terms to the same U, so these are highest weights. Independence follows from their distinct one-down Bob occupations.

For J=1/2, fix each physical multiset M of size4 (35 choices). For every unordered two-submultiset S={s,t} of M, let F_S be `Sym_B` with those two physical positions carrying auxiliary1 and the complementary pair auxiliary0; let D_r mean one Bob auxiliary1 with physical r and all remaining physical labels M minus r carrying auxiliary0. Choose one reference pair S0 in each M. For every other S use

`|0>_A0(F_S-F_S0)`
` +|1>_A0(D_(s0)+D_(t0)-D_s-D_t)`,

again tensoring each Alice physical basis vector. Repeated labels contribute their multiplicity. Raising sends F_S to D_s+D_t, and every D_r to the same U_M, so the displayed combinations are highest weights. Their F components are independent. There are `(100-35)*4=260` vectors.

The omitted J5/2 multiplicity is35*4=140. Dimension check:

`6*140+4*320+2*260=2640`.

For the rectangular basis matrices B_J, impose

`B_J^* [K_4(Y)+mu(I-2K_4(I))] B_J>=0`.

Because the bases are not orthonormal, the identity term is their actual Gram matrix `B_J^*B_J`, never an inserted identity matrix. All basis coefficients can be rational (permutation averages only). SU(2) invariance makes positivity on these complete highest-weight multiplicity spaces equivalent to positivity of the full operator. This is a mathematical reduction, not permission to execute its construction.

## 4. Single proposed input and bounded future preparation

Keep the same rational target, with x=(1,1,1,1):

`R_x=P(a)+P(b)+P(c)+3P(02+|3> tensor x)+3P(20+33)`
`     +3P(30)+3P(32)+3P(23)+3P(|0> tensor x)`,
`rho_x=R_x/49`.

Proposed optimization: minimize `Tr(Y rho_x)` subject to the two exact highest-weight LMIs, `Tr(Y)=16`, and `0<=mu<=1`. For this real input, restricting Y to real symmetric loses no feasible objective: conjugating a feasible certificate and averaging preserves every real affine constraint. This is not Park's two-parameter covariant witness restriction.

If parent authorizes preparation, freeze a single small direct script plus source/interpreter/dependency/input pins. Proposed eventual admission limits: one CPU thread, at most8GiB, no install/config changes, one attempt, no adaptive parameter grid or hierarchy escalation. Use existing solver support only; unavailability is a reported prerequisite, not a reason to install a framework. Fresh aggregate-resource approval and an exact named GO remain mandatory before any scientific execution.

Proposed controls within that one future assay:

1. Build and compare the known Yctrl/muctrl blocks against the exact Gram-scaled lower bound (7), and confirm the objective -1/29 on Omega4. This is an implementation control, not another scientific discovery.
2. Solve the same certificate optimization against the separable00 state. A genuinely negative value contradicts the proved certificate implication and invalidates the implementation/solver result.
3. Perform the ONE target optimization. A negative float value is **CANDIDATE ONLY**, not a proved two-block-positive witness. Any promotion requires a separately admitted exact rational/algebraic PSD reconstruction and complete state/witness trace proof. Failure or nonnegative output means only that this finite certificate and input did not give a witness, not unrestricted nonexistence or SN2.

Parent may decline this preparation on cost/benefit grounds. No command is currently authorized and no program has been created or run. This proposal is one normalized-certificate mechanism with its vacuity checks and control, not an open-ended experiment queue.
