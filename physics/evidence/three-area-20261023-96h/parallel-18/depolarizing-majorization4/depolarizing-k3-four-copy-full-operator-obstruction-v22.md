# Actual k3 continuation v22 — exact S4/three-code full-operator route is FALSE at first order

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 06:20:50 PDT 2026**. Owner PhysicsDepol4-2. **NEW exact WRITTEN method obstruction, not a physical channel counterexample or exhaustion of the target.** This settles the genuinely new full four-copy certificate attempted in checkpoint082: its remaining scalar sector is NEGATIVE at first order, so proving additional positive blocks cannot establish that full operator inequality. No scientific execution, numeric parameter instance, decimal probe, interpreter/calculator/eval/CAS/program/enumeration/solver/replay/CLI/nested agent/GO. All old files remain immutable; same18/HOLD/OWN root/October27 cutoff11:05:38/deadline12:35:38 PDT.

## 1. Literal actual-code lifting and the tempting stronger certificate

Let H=(C^2)^tensor4. Use copies0 (reference) and1,2,3 (three codewords), regrouped sitewise. At site i let F_(0a)^(i) swap physical qubit i between copies0 and a, and define

    K(u)=sum_(a=1)^3 tensor_(i=1)^4 [F_(0a)^(i)+u I],
    L3(u)=(1+u)^3(1+3u).

For an ACTUAL rank-three orthogonal projector Pi, its normalized Slater vector C_Pi in wedge^3H has EACH code marginal Pi/3. The partial-swap contraction for a product of rho0 and C_Pi gives

    <psi tensor C_Pi|K(u)|psi tensor C_Pi>
      =Tr[Pi H_u(|psi><psi|)].                             (LIFT)

There is no extra3: the sum over a cancels the code marginal1/3. Thus `K(u)<=L3(u)I` on ALL of `H tensor wedge^3H` would imply the ORIGINAL rank3 comparison at every u>=0. It is stronger than testing only actual reference-times-Slater vectors, and its first-order version was not licensed by the rank2 S3 theorem.

For a qubit site, the four-copy Schur-Weyl S4 types are(4),(31),(22), multiplicities5,3,1; all other Young types vanish because there are only two physical levels. Restrict to S3 permuting code copies1,2,3. Type(4) is trivial; type(31) is trivial+standard; type(22) is standard. These standard Schur-Weyl/branching facts are named ordinary finite-dimensional inputs; the explicit matrices below independently specify the affected sector. The GLOBAL code-sign isotypic subspace is precisely the wedge^3H code sector, not a fictitious locally alternating type.

## 2. Explicit local matrices, retaining all standard-sector cross terms

In the real standard plane E={z in R^3:sum z=0}, let q_a=e_a-(1,1,1)/3, so

    q_a.q_b=delta_ab-1/3, sum_a q_a q_a^T=I_E.

For local type(31), use its code-trivial vector t=(3,-1,-1,-1)/sqrt12 and E on code coordinates. Directly swapping coordinates0,a gives

    F_a^(31)=[[-1/3, (2/sqrt3)q_a^T],
              [(2/sqrt3)q_a, I_E-q_aq_a^T]].              (31)

It has trace1 and squareI, with standard-plane q_a direction eigenvalue1/3 in its compressed lower block, not a freely diagonalized scalar. For type(22),

    F_a^(22)=3q_aq_a^T-I_E.                               (22)

The latter is the actual S4 action on the two-dimensional complement to the constant vector in the permutation representation of the three pair partitions; it restricts to the same code standard. Both displays retain the SAME code permutation action at every active site.

On any global S3-sign vectors v,w, code conjugation sends the a=1 term to each other a, and the two signs cancel. Hence every SIGN-block entry of K is exactly THREE times the a=1 tensor entry. This is a symmetry identity, not enumeration or averaging of independent spectra.

## 3. The neglected all-four-(31) scalar sector

Put all FOUR physical sites in local type(31), and use only their standard E subspaces. The S3-sign component of E^tensor4 has dimension3 and, under physical-site S4, is the irreducible [31] module. To see the relevant multiplicity, the characters on code S3 are: identity2^4, transposition0,3cycle(-1)^4; pairing with sign gives(16+2)/6=3. Under site permutations the same projection has character3 on a site transposition,? — no character value is used below; instead the explicit weight support gives the full restriction directly.

Choose the orthonormal standard-plane basis h parallel to q_1 and k perpendicular. In this basis the lower block of `F_1^(31)+uI` is diagonal with entries

    b=u+1/3 on h, c=u+1 on k.

Every sign vector of E^tensor4 has support ONLY on tensors with an ODD number of k factors: under the code reflection fixing h and reversing k, sign is negative. There are potential weights1 and3. Code120-degree rotation invariance leaves a three-dimensional sign space; explicitly it is the space of tensors encoded by coefficients x_i at the four weight-one-k positions and y_i at the complementary weight-three-k positions satisfying

    sum_i x_i=sum_i y_i=0, y_i=-x_i

up to one common basis/sign convention. Equivalently, the antisymmetric two-form on E in any two slots times the symmetric metric in the remaining two, with the one Plucker relation, spans it. In particular every normalized sign vector has HALF its squared norm at weight1 and HALF at weight3. This equality also follows from a90-degree simultaneous rotation h->k,k->-h: it commutes with the sign projector and exchanges the two weights, acting as a scalar on this three-dimensional sign component. No state/parameter instance is chosen.

Therefore the restriction of `tensor_i(F_1^(31)+uI)` to this subspace is the SCALAR `(b^3c+bc^3)/2`. K's sign restriction is consequently

    K_scalar(u)=(3/2)bc(b^2+c^2).

A direct symbolic expansion gives

    L3(u)-K_scalar(u)
       =(1+u)[3u^2+(4/3)u+4/9] >0  for u>=0.              (SAFE)

Thus this **all-standard degree4 scalar is NOT the obstruction**. It is written here to keep the attempted block accounting honest, not to bury a negative block by omitting it.

The actual obstruction is the complementary S4-symmetric combination mixing TWO standard-site factors with FOUR standard-site factors, described next. In checkpoint082 it was the remaining trivial2x2 block, not the already checked standard3x3 block.

## 4. Exact TWO-by-TWO block and its first-order negative determinant

Within all-four local type(31), the global sign subspace decomposes by the number j of standard factors: j=2 has dimension6, j=3 dimension4, j=4 dimension3. For j=2 the six pairwise antisymmetric standard tensors transform under site S4 as wedge^2 of the permutation representation, i.e.[31]+[211], so no trivial component occurs there. The j=3 sign tensor of E^tensor3 is the symmetric imaginary cubic; its four choices of missing site transform as the four-dimensional permutation representation, i.e.[4]+[31]. The j=4 sign part is[211] (NOT[31]). Consequently the actual remaining scalar is the j=3 **trivial** component, and it does NOT mix with any j=2/j=4 scalar. This is the correct site-symmetry accounting; the apparent2x2 scalar in the attempted informal route is absent. The correction is made NOW before any claimed certificate, not edited into checkpoint082.

Take h,k as above. The normalized code-sign cubic tensor is

    T=( |hhk>+|hkh>+|khh>-|kkk> )/2,

up to an irrelevant common sign. It is invariant under the code120-degree rotation and odd under its reflection, so is an actual unit sign vector of E^tensor3. For each missing site i let v_i have t at i and T in the other THREE physical sites. The v_i are orthonormal. Their symmetric normalized sum v=(sum_i v_i)/2 lies in the global code-sign sector and is a legitimate entangled reference/code vector in H tensor wedge^3H.

Put a=u-1/3,b=u+1/3,c=u+1 and g=2sqrt2/3, the actual off-diagonal t<->h entry in(31). Then direct a=1 contraction gives

    <v_i|tensor(F_1+uI)|v_i>=a(3b^2c+c^3)/4,
    <v_i|tensor(F_1+uI)|v_j>=g^2bc/4  (i!=j).

For the off-diagonal formula the two standard factors not i,j must be hk or kh, each with cubic amplitude1/2; hence their TWO contributions give g^2bc/2, NOT g^2bc/4. The CORRECT complete expression is therefore

    <v|K(u)|v>=(3/4)a c(3b^2+c^2)+(9/2)g^2bc
              =(3/4)a c(3b^2+c^2)+4bc.

The corrected factor2 is load-bearing: it retains BOTH hk/kh coherences. Expanding with the stated a,b,c yields

    <v|K(u)|v>=(1+u)(3u^3+3u^2+3u+1),
    L3(u)-<v|K(u)|v>=u(1+u)(1-u).                        (GAP)

This expression is NONNEGATIVE for0<=u<=1 but NEGATIVE foru>1. Thus the attempted all-u FULL operator certificate is refuted ONLY beyond the original low-noise interval by this block; it does NOT refute the needed0<=u<=1 certificate or supply the promised first-order negative obstruction. The next section records the correct settled outcome rather than silently asserting the title's initial hypothesis.

## 5. Settlement — no valid first-order obstruction was proved in this draft

**The title's first-order-negative diagnosis is WITHDRAWN as a working hypothesis.** The actual displayed block has gap u(1+u)(1-u), so is eligible on the original target interval and fails only u>1. At no point is that failure promoted to an actual product-reference/Slater channel witness. The 3x3 standard gap in checkpoint082 and the above scalar remain compatible with a FULL low-noise0<=u<=1 operator certificate. The all-u extrapolation (used successfully at rank2) is FALSE for this FULL rank3 operator block, but original high-noise comparison still follows its separate inherited boundary or a physical spin-flip transfer IF a valid physical low-noise proof is completed.

This evolving draft has displayed the exact abandoned site-irrep labeling and off-diagonal factor in sequence to preserve the author's mathematical trail; it is NOT a completed full-certificate source. The first unresolved step is the ENTIRE remaining S4-sign block spectrum/PSD on0<=u<=1, in particular [211] mixing j=2/j=4 and the scalar sectors with local(22) factors. No partial block, informal dimension count or wrong intermediate label is accepted as a full theorem. All checkpoint082 stronger completion implications are withdrawn; its explicit3x3 candidate identity remains just a candidate pending correct full block reconstruction. No scientific interpreter/CAS/enumeration/solver was used and no exact parameter instance was probed.

This is a written research trail and method-boundary packet, not a physical refutation/globalclosure/final answer. It leaves all original k3/CLIP-prime/quarticquantifiers OPEN. The next substantive continuation must either derive the missing physical low-noise blocks correctly or change representation with this precise boundary retained. All process/zero-credit/cadence/freeze/read-order histories remain permanent; source-correct later work would not cure them. Same18/HOLD/OWNroot/cutoff/deadline, active continuation NOT a park.
