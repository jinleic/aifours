# Rank-two completion as four coupled64-point streams: exact local grammar and written Gold occupancies

Owner InfoBalancedNL242, info-6. Actual precreation observation: `Sun Oct 25 04:31:47 PDT 2026`.

**WRITTEN ONLY.** This packet was derived after finishing the assigned v30-D Shor review. No scientific eval, arithmetic interpreter, program, enumeration, certificate replay or solver was used. Metadata clocks/hashes/source reads only. The parent v7 correction and scientific HOLD remain binding. Independent review of this new packet was **not performed**; the ongoing v30-C review concerns the earlier pinned half-design/Gold pair, not this successor.

This is a materially different primary representation: replace the global half-subset discrepancy variables by64 local four-entry Boolean blocks, with an exact finite local Hadamard grammar and four coupled six-variable transforms. It retains every word of the original S/R/N requirements. For both explicit Gold S profiles, their previously observed quotient-occupancy histograms are now obtained by a written radical-incidence argument, not by reuse of unadmitted output.

## 1. Retained interfaces and scope

Use the exact unpruned S system from `rank2-two-spectrum-completion-v1.md`, SHA-256 `2a0d363458746f20e9c226db71c8460869386ebc95381fc6c62e51dca8612f6e`:

    b=phi(Hdelta), E={x in U:b(x)=−q(x)}, P=H(q1_E),
    B=phi(q−b)=q−b−3q1_E, S=2HB,
    Hb+3P=4delta on supp(delta), magnitude12 elsewhere.

The fixed normal form is D=1−1_W, dim W=6, U=W-perp of dimension2, q=2e0−1_U. Let T={B=0}. No independent placement of B,T,delta or E is allowed.

The universal half-design theorem is retained as WRITTEN from `rank2-half-design-and-gold-barrier-v1.md`, SHA-256 `07bfc5d42ad7d65751f555f82387f090b1f066c76ee68a5882f3dbd90a7d135b`, together with its mandatory admission/written-Gold overlay `rank2-half-design-admission-and-written-gold-addendum-v1.md`, SHA-256 `9482f1df4dd79354250b96b9b75a756b895182a2a111022dea1dc3f58b1a5e60`.

Only the overlay's algebraic Gold construction is used below. Its unadmitted literal arrays, numerical histograms, restricted searches and control functions are **not** proof inputs. The new results are written candidates, not parent-accepted or formally checked statements.

## 2. Exact local-to-global block theorem

Choose a linear complement C to U in the Boolean-sign domain, so G=C direct-sum U. Use dual coordinates (y,r), y in C*, r in U*, satisfying

    (y,r) dot(c+u)=y dot c+r dot u.

Then the frequency space W is exactly r=0. This is only a change of coordinates; it fixes no truth-table half.

For each c in C define its actual occupancy

    A_c={u in U:c+u in T},   m(c)=|A_c|.

Choose signs a_c(u)=±1 for u in A_c and put a_c(u)=0 otherwise. Define four INTEGER streams

    d_r(c)=sum_(u in U) (−1)^(r dot u) a_c(u),   r in U*.  (B1)

Equivalently, the vector d(c) is the four-point Walsh transform of a_c. The inverse local condition is

    (1/4) sum_r (−1)^(r dot u) d_r(c)
      is ±1 on A_c and0 off A_c.                    (B2)

All four streams are therefore coupled at every c; arbitrary independent arrays with the same scalar energies are not allowed.

**Theorem BS (WRITTEN).** Fix any unpruned S-consistent delta, with its actual B and T. It extends to the complete original S/R/N system iff local blocks (B2) can be chosen such that

    H6[d_0](y) in {0,+8,−8} for all y,
    H6[d_0](0)=0,                                   (B3)
    H6[d_r](y) in {+4,−4,+12,−12}
                       for all y and every r!=0.    (B4)

Here H6 is the unnormalized64-point Walsh transform on C. These are the entire256 R coefficients, not a projection or a necessary-only relaxation.

### Proof

Assemble a(c+u)=a_c(u). Splitting the eight-point character gives exactly

    H8 a(y,r)=H6[d_r](y).                            (B5)

The inverse local condition makes a ternary sign array supported exactly on T, hence the exact INTEGER norm a²+B²=1 holds. Conditions (B3),(B4) say p=H8a/4 lies in0,±2 on W, in±1,±3 off W, and p(0)=0. Thus p modulo2=D. Set beta=phi(p). Since Hp=64a and64=1 modulo3, phi(Hbeta)=a. Every coordinate of R now follows, and the integer norm gives the original convolution N by the retained exact norm/convolution argument. Both Boolean inverse signs B+a and B−a are genuine.

Conversely, any full solution supplies a=phi(Hbeta), supported exactly on T by N. Restriction to each U-coset gives (B2); the original R condition gives (B3),(B4) through (B5). This proves both directions without pruning E or dropping its integer carry.

For the complete512-bit reconstruction, set

    F(x,0)=(1−B(x)−a(x))/2,
    F(x,1)=(1+B(x)−a(x))/2.

The norm makes these literal bits. The zero-frequency condition gives sum a=0 and therefore exact weight256. Its full Walsh sectors are2Ha=8p and2HB=S. Thus both Boolean transforms, balance and all512 coefficients are present. The blocks are not a witness until every stream condition holds.

## 3. The complete four-site grammar, including positions and signs

Write chi_r(u)=(−1)^(r dot u). The following is an analytic classification on a single four-point group, not an executed enumeration.

- **m=0:** all d_r=0.
- **m=1**, occupied point u_0: d_r=epsilon chi_r(u_0), epsilon=±1.
- **m=2**, occupied u_1,u_2: for independent signs epsilon_1,epsilon_2,

      d_r=epsilon_1 chi_r(u_1)
            [1+epsilon_1 epsilon_2 chi_r(u_1+u_2)].

  Exactly two components are0 and two have magnitude2. The active pair is the actual affine hyperplane of r specified by the bracket; its location cannot be freely reassigned independently of the occupied sites.
- **m=3**, missing point u_0: for epsilon=±1 and r_* in U*,

      d_r=epsilon chi_r(u_0) [4*1_(r=r_*)−1].        (B6)

  Exactly one component has magnitude3 and the others magnitude1. Inversion gives epsilon chi_(r_*)(u+u_0) off u_0 and0 at u_0. Every assignment on the other three points is an affine character restriction, so this is exhaustive and has no hidden sign omission.
- **m=4:** either d has one component±4 and the others0, or every component has magnitude2 and the product of the four component signs is−1. The first case is precisely an affine character on U. In the other case the four Boolean signs have odd negative parity; every character modulation preserves that parity, so each Walsh component is±2. The resulting four-component sign product is−1, as follows by modulation of a one-negative Boolean vector.

In all cases

    d_r(c)=m(c) mod2 for every r,
    sum_r d_r(c)^2=4m(c).                            (B7)

The embedded support A_c is part of the grammar. Magnitude patterns without those position/sign conditions are not sufficient.

## 4. Global energy identities and their exact limitation

Let n=|T|. If (B3),(B4) hold, let z be the number of zero coefficients of the r=0 stream, and let c_r be the number of magnitude4 coefficients in the r!=0 stream. Thus c=sum_(r!=0)c_r is the actual count |p|=1.

Parseval in each64-point stream gives

    sum_c d_0(c)^2=64−z,
    sum_c d_r(c)^2=144−2c_r,   r!=0.                 (B8)

Summing (B7) and (B8) recovers the actual occupancy identity

    z+2c=496−4n=4(124−n).                            (B9)

This does not create a witness: it is a consequence of ALL stream alphabets, and cannot be used to assign a nominal u to an inadmissible array.

Let O=#{c:m(c) is odd}. Squares modulo4 in (B7),(B8) also give the support-determined restrictions

    z=−O mod4,
    2c_r=−O mod4 for each r!=0.                     (B10)

They are local-to-global compatibility tests, not an alternative to (B3),(B4). The old relation z=2c_r modulo4 follows, but (B10) identifies its value from the actual S-side support before any beta is selected.

## 5. Written radical incidence for the first Gold S profile

Use V=F16 with alpha^4=alpha+1 and t in the polynomial basis. The retained written construction is

    delta(t,t³)=−(−1)^(t_0t_1),
    U={0,4,8,12} in the first four frequency/sign coordinates.

For a linear functional L on the second V, the first-four-bit slice Hdelta(a,L) is the Walsh transform of the four-variable quadratic

    q_L(t)=t_0t_1+L(t³).

Let mu(u wedge v)=uv²+u²v. The written Gold proof gives: mu is onto; K=ker(mu) has dimension2; the polar lambda of t_0t_1 is nonzero on K; and every polar

    F_L=lambda+L composed with mu

is nonzero. Thus each F_L has rank2 or4. The same proof establishes wt(b)=136, without any finite table. For a rank4 slice all16 Walsh coefficients are nonzero; a rank2 slice has exactly4 nonzero coefficients. Hence if N_4 is the number of rank4 slices,

    16N_4+4(16−N_4)=136,

so N_4=6 and there are10 rank2 slices. This is a dimension/Parseval consequence, not reuse of the former evaluated count.

For a rank2 slice, let R_L be its two-dimensional polar radical. Its nonzero Walsh support P_L is an affine two-plane with direction R_L-perp. Put

    X=U-perp in V=span(e_0,e_1).

Then

    dim(direction(P_L) intersect U)=dim(R_L intersect X). (B11)

This follows by taking annihilators: (R_L-perp intersect X-perp)=(R_L+X)-perp. Consequently:

- if R_L intersect X has dimension0, each of the four U-cosets meets P_L once;
- in dimension1, two U-cosets meet P_L twice and two do not meet it;
- in dimension2, P_L is a U-coset.

### 5.1 Six radicals meet X in a line; four are transverse

For each nonzero v in X, the map w -> mu(v wedge w)=vw(v+w) has kernel {0,v}, hence a three-dimensional image. The functional w -> lambda(v,w) vanishes on that kernel. There are therefore exactly two linear functionals L on V satisfying

    L(mu(v wedge w))=lambda(v,w) for all w.

These are exactly the F_L having v in their radical. None has rank0, so they all have rank2.

No R_L equals X. Such a form would have to be the sole nonzero alternating form theta with radical X, namely its e_2,e_3 coefficient. In the earlier written proof,

    kappa=e_0 wedge e_1+e_0 wedge e_2
          +e_0 wedge e_3+e_1 wedge e_2

lies in K and lambda(kappa)=1, while theta(kappa)=0. But every F_L agrees with lambda on K. This excludes that form.

The three nonzero v in X therefore give six DISTINCT rank2 forms meeting X in a line: overlap of two would force the entire X into the radical. The remaining four rank2 forms are transverse. This proves the complete incidence count, not a selected placement assumption.

### 5.2 Exact occupancy histogram

Before the four-point q correction, T_0={b=0} has no points in each rank4 slice. In a rank2 slice it is the complement of P_L. Thus:

- six rank4 slices give24 empty U-cosets;
- six line-intersection slices give12 cosets of occupancy2 and12 of occupancy4;
- four transverse slices give16 cosets of occupancy3.

At L=0, q_0 has radical span(e_2,e_3), transverse to X. The earlier written calculation b|U=(1,0,0,0) says that replacing −b by B=q−b changes precisely the U-coset at L=0: one formerly excluded point is added to T and its three other points are removed. Its occupancy changes3 to1. Hence the final histogram is proved in writing:

    occupancy m:   0   1   2   3   4
    coset count:  24   1  12  15  12.                (B12)

The support size is118 and O=16. No unadmitted array was read or replayed to prove (B12).

## 6. The second Gold branch also has a written occupancy histogram

For delta modulated by (−1)^(t_2), use U'={0,1,2,3} and X'=span(e_2,e_3). The polar forms F_L do not change under this linear modulation, so the rank counts remain6 and10.

Now exactly ONE rank2 form has radical X': it is lambda itself at L=0. Uniqueness follows because the only nonzero alternating form with that radical is lambda and mu is onto. The three nonzero v in X' still each lie in the radicals of exactly two forms by the preceding three-dimensional-image argument. The L=0 radical accounts for three of these incidences; the other three forms each meet X' in a line. Thus the rank2 classes are:

    one parallel, three line-intersection, six transverse.

Before q correction their complementary Walsh supports give25 empty cosets,6 occupancy2,24 occupancy3 and9 occupancy4. Modulation moves the L=0 nonzero Walsh support from U' to U'+4. Therefore U' itself is a full T_0 coset. The written b|U'=0 calculation makes the q correction remove exactly its four points from T. Its occupancy changes4 to0. The final histogram is

    occupancy m:   0   1   2   3   4
    coset count:  26   0   6  24   8.                (B13)

It has n=116 and O=24. This also is a new written derivation, independent of the earlier evaluation.

## 7. Consequential first-case constraints, retaining the full stream problem

For the first Gold support (B12), use the local grammar to define:

- A_3: number of the15 occupancy3 blocks whose magnitude3 component is r=0;
- B_2: number of the12 occupancy2 blocks with r=0 active;
- C_4: number of the12 occupancy4 character blocks peaking at r=0;
- D_4: number of occupancy4 noncharacter blocks (all four magnitudes2).

The one occupancy1 block always contributes1 to d_0². Therefore the EXACT local energy is

    sum_c d_0(c)^2=16+8A_3+4B_2+16C_4+4D_4,
    z=48−8A_3−4B_2−16C_4−4D_4.                    (B14)

If a full R completion exists, n=118 forces u=24. Compose (B10), O=16, with the retained written R theorem z>=8, c>=2 and at least two occupied outer cosets. Since c_r is even for every outer stream, c>=4, so z<=16. Thus

    z in {8,12,16},
    2A_3+B_2+4C_4+D_4 in {10,9,8},                 (B15)

with corresponding z values8,12,16. In particular no more than five occupancy3 blocks can place their large component at r=0. Signs and placements must ALSO obey the exact grammar, the zero-frequency balance and all four transforms; the count condition is not sufficient.

For (B13), the analogous energy is

    z=40−8A_3−4B_2−16C_4−4D_4.

Here n=116 forces u=32. O=24 again makes z a multiple of4 and all c_r even, giving only z in {8,12,16,20,24}. These are necessary consequences for the explicit second S support, not realizability assertions or classifications of all L16 deltas.

## 8. Exact new barrier and unchanged per-case verdicts

The first Gold (16,24) branch is now a completely explicit **64-block problem**:

- 24 blocks are identically zero;
- 1 block has the fixed two-choice occupancy1 grammar;
- 12 blocks have the actual-site occupancy2 grammar;
- 15 blocks have the missing-site occupancy3 grammar;
- 12 blocks have the occupancy4 character/noncharacter grammar;
- all four64-point transforms must meet (B3),(B4), including exact balance.

No Boolean transform or common coordinate is hidden in this description. Its local coupling is the part lost if one solves the four energy rows separately. The first unproved step is a contradiction for every permitted choice of these local characters/signs, or a complete choice satisfying all four transform alphabets. Neither has been obtained.

Per-case verdicts:

- **(16,24): UNRESOLVED.** This packet proves the block formulation and the written Gold occupancy/energy restrictions. It does not exclude every block assignment even for this one S support, and does not exclude all S supports.
- **(16,32): UNRESOLVED.** Its explicit Gold support has the different exact grammar histogram (B13), but no simultaneous four-stream completion/noncompletion is proved.
- **(20,24): UNRESOLVED.** Theorem BS applies to every S-consistent support, with n=118 if completed. No S construction or universal S obstruction for L20 is supplied.
- **Universal U2: UNPROVED.** The exact replacement obligation is nonexistence of the coupled block/stream system for every unpruned S-consistent delta. It is equivalent to, not a relaxation of, the original system.

All prior pinned files remain unchanged. The specialized literal control functions and their old finite computation receipts remain unadmitted; this packet claims only the new written proofs actually given above. No scientific-launch permission, executable verification, independent review, formal proof or novelty clearance is inferred.
