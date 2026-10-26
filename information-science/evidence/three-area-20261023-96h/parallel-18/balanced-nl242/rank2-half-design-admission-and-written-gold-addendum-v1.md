# Mandatory admission correction and independent written Gold construction

Owner InfoBalancedNL242, info-6. Actual clock after receipt of the parent correction: `Sun Oct 25 04:12:01 PDT 2026`.

This is an additive mandatory overlay on `resume-ack-v1.json`, `resumption-checkpoint-001-v1.json`, `rank2-half-design-literal-profiles-v1.json`, and `rank2-half-design-and-gold-barrier-v1.md`. Their frozen bytes are preserved. The earlier packet's SHA-256 is `07bfc5d42ad7d65751f555f82387f090b1f066c76ee68a5882f3dbd90a7d135b`; its literal JSON is `95f72b0484168159c4d67dd1df872ce2b4bf1f9cf9ac109311cb4aa2948b7e6d`.

## 1. Parent permission correction is binding

The parent withdrew checkpoint026's blanket allowance for scientific arithmetic/enumeration in evaluation kernels. Under the corrected authority, **no further scientific interpreter, certificate replay, enumeration, symbolic/numerical computation or solver work is permitted without a separate exact source/input-pinned named GO**. Written reasoning, source reading and metadata clocks/hashes remain allowed. No new scientific computation was performed after this correction. No earlier computation was rerun for exit attestation or validation.

The owner's earlier evaluations occurred under that explicit, now-withdrawn parent permission, not a named scientific GO. The parent stated that the erroneous permission came from the parent and is not attributed to owners. This overlay neither retroactively admits those calculations nor invents an owner-fault verdict.

Accordingly, the earlier label `WRITTEN-checked-in-kernel` describes **observed, now-unadmitted evaluation output**, not accepted scientific verification under HOLD v2. Withdraw any implication that those checks were admitted or satisfy the round's verification gate. The literal data are preserved as unadmitted candidate observations. No independent execution, resource supervision, actual child-exit attestation, formal proof or independent review follows from them.

The universal half-design theorem in §§2–3 of the earlier packet is ordinary **WRITTEN mathematics** with a self-contained proof; it does not require the finite calculations. The written construction below also supplies an algebraic proof of both explicit S profiles without invoking the prior interpreter results. These written results remain candidates for independent reconstruction, which was **not performed** here.

## 2. Actual scientific computations already performed

They occurred after the returned resumption clock `Sun Oct 25 03:46:36 PDT 2026` and before the returned final pre-correction clock `Sun Oct 25 04:09:01 PDT 2026`. Individual call execution clocks and independent child exits were not captured; no more precise chronology is asserted.

The following operations actually ran inside the owner's Python evaluation kernel:

1. A Walsh H² identity on an8-entry control and the phi residue control; finite-field multiplication modulo X^4+X+1; a single unsigned Gold-graph transform.
2. All64 homogeneous quadratic signs on that single16-point Gold graph, with256-point integer Walsh transforms and S checks.
3. The two displayed signed Gold S profiles, affine-rank and support-moment calculations, and two explicit balanced sign/subset constructions. A failed one-exchange assertion for the second subset was followed by a two-exchange construction; prior partial state was retained.
4. The nine F2 constraints on37 quadratic ANF coefficients, their rank/nullspace, and the fixed407-member quadratic sign-lift family (zero/one/two nullbasis changes), with restricted balancing masks.
5.101 eligible five-removal/three-addition character switches on coordinate affine3-flats of one b profile; no L20 S profile was found in that restricted family.
6. Both literal beta arrays, a=phi(Hbeta), all256 direct XOR-convolution N residues, the integer Boolean norms, canonical congruences, balanced512-bit maps and all512 Walsh coefficients.
7. U-coset occupancy and sign tables, quotient parity/ANF calculations, the frozen outer/W squared sums, and elementary signed fourth-moment congruence/lower-bound calculations for the two T supports. The latter produced no contradiction.
8. Extraction of the literal field/support tables and JSON serialization of the observed arrays.

There was also one syntax-error cell, which did not execute its body. None of these observations is hidden, renamed as metadata, credited as an admitted replay, or used to infer a historical process exit. The global HOLD remains binding. No native solver/scientific process or external model CLI was launched by this owner.

## 3. Written construction replacing the S-profile computation claim

All reasoning in §§3–6 below was performed **in writing after the correction**, with no further evaluation or replay. It establishes the S identities and full affine rank algebraically. It does **not** establish the previous literal inadmissible controls' detailed histograms, their seven/twelve R failures, or their N checks; those remain preserved unadmitted observations unless separately reconstructed.

Let V=F16 as a four-dimensional F2-space, with alpha^4=alpha+1. Let A be the graph

    A={(t,t^3):t in V} in V x V.

Use the polynomial basis1,alpha,alpha²,alpha³. On the six-dimensional exterior square define the linear map

    mu(u wedge v)=u v²+u² v=u v(u+v).                 (A1)

It is alternating and F2-bilinear. A nonzero decomposable bivector represents a two-dimensional F2-plane with nonzero elements u,v,u+v; its image under mu is the product of those three elements, hence is nonzero.

In coordinates z_01,z_02,z_03,z_12,z_13,z_23, the Pluecker quadratic is

    Q_P(z)=z_01 z_23+z_02 z_13+z_03 z_12.            (A2)

A nonzero bivector is decomposable iff Q_P=0: this is the four-dimensional alternating-matrix rank2/Pfaffian identity. Thus every nonzero element of K=ker(mu) has Q_P=1.

Since dim(exterior-square V)=6 and dim V=4, dim K>=2. It cannot contain a three-dimensional subspace: on such a space a quadratic polynomial has even total sum over all8 points, whereas a function1 at all7 nonzero points and0 at0 has odd sum. Therefore

    dim K=2, and mu is surjective.                   (A3)

In particular Q_P restricted to K is the anisotropic quadratic on a two-space; its polar form is nondegenerate. On any nonzero affine fiber mu^{-1}(c), restriction of Q_P consequently has either one or three zeros among its four elements.

### 3.1 Choose a genuinely different quadratic sign

Put q_0(t)=t_0 t_1 and let lambda be its alternating polar functional on the exterior square, so lambda(u wedge v)=q_0(u+v)+q_0(u)+q_0(v).

It is essential that lambda not vanish on K. This can be seen explicitly without enumeration. Let e_i=alpha^i and

    kappa=e_0 wedge e_1+e_0 wedge e_2
          +e_0 wedge e_3+e_1 wedge e_2.

Using alpha^4=alpha+1, the four images in (A1) are respectively

    alpha+alpha², 1+alpha+alpha², alpha², 1+alpha².

Their sum is0, so kappa lies in K; and lambda(kappa)=1. Thus lambda|K is nonzero.

Define the signed graph delta(t,t^3)=epsilon(t), where

    epsilon(t)=−(−1)^(q_0(t)).

The same argument works for every quadratic q whose polar functional is nonzero on K, with arbitrary affine terms. There are48 such homogeneous quadratics: the restriction map from the six-dimensional space of alternating forms to K* is onto, and its kernel has dimension4. This count is a dimension argument, not reliance on the previous64-item evaluation.

### 3.2 Its Walsh values have only the required five values

For a linear functional a on V and a linear functional L on the second V,

    h(a,L)=Hdelta(a,L)
      =−sum_t (−1)^(q_0(t)+a(t)+L(t^3)).             (A4)

The exponent is quadratic in t. Its polar functional is lambda+L composed with mu. Its restriction to K is lambda|K, so it is never zero. A nonzero alternating form in dimension4 has rank2 or4. Splitting into its radical and a nondegenerate quadratic complement gives the elementary quadratic Walsh values0,±8 in rank2 and±4 in rank4. Therefore

    h takes values only0,±4,±8.                      (A5)

No finite Walsh table is imported here.

On those five integers, the following polynomial is exactly the ternary representative:

    phi(h)=(48h−h³)/128.                            (A6)

Write b=phi(Hdelta), C=Hb, and let star denote XOR convolution. Since H(h³)=256(delta star delta star delta), (A6) yields

    C=96delta−2(delta star delta star delta).        (A7)

It remains to determine the signed triple convolution, not to enumerate its256 entries.

## 4. Written signed-triangle calculation: C=4delta or±12

At a graph point (s,s³), every repeated-entry ordered triple contributes epsilon(s). There are3*16−2=46 such triples. There are no all-distinct triples there: otherwise four distinct graph points would sum0, giving a nonzero decomposable bivector in ker(mu), impossible by (A1). Thus

    (delta star delta star delta)(s,s³)=46epsilon(s).

For a point (s,t) outside A, put c=t+s³!=0. Its ordered graph triples have parameters

    s+u, s+v, s+u+v,

where u,v form a basis of a two-plane P and mu(P)=c. Each such plane supplies its six ordered bases. The cubic identity is

    (s+u)^3+(s+v)^3+(s+u+v)^3=s³+mu(u wedge v).

The product of their three signs is

    epsilon(s)*(−1)^(lambda(P)).

Consequently the triple convolution at (s,t) equals

    6epsilon(s) sum_(P decomposable, mu(P)=c) (−1)^lambda(P).  (A8)

The full fiber mu^{-1}(c) has four elements. Because lambda|K is nonzero, its signed character sum is0. By (A3) exactly one or three elements of that fiber are decomposable. If one is decomposable, its sum is±1. If three are decomposable, their sum is minus the sign of the omitted fourth element, again±1. Therefore (A8) is always±6.

Substitution in (A7) proves the complete identity

    C=4delta on A; |C|=12 off A.                     (A9)

This proves the entire nu0 S identity for this signed graph **by written algebra**, independently of the unadmitted arrays.

Its support has full affine rank8. Indeed, an affine relation ell(t)+L(t³)+c=0 on the graph has c=0 by t=0. Polarization gives L composed with mu=0; surjectivity of mu gives L=0, and then ell=0. There is no proper affine hyperplane containing A.

Parseval in (A9) gives

    256*wt(b)=16*16+240*144=34816,

hence wt(b)=136. This is also a written consequence of (A9), not imported numerical evidence.

## 5. Both L16 count branches have written S witnesses

Use the eight-bit index x=t+16y and q=2e0−1_U, reserving q_0 for the quadratic sign above.

### First branch: U={0,4,8,12}

On y-frequency0, (A4) is the four-variable transform of −(−1)^(t_0t_1). It equals−8 at a=0 and is0 when a has a nonzero bit2 or bit3. Therefore

    b|U=(1,0,0,0), q|U=(1,−1,−1,−1).

Thus E is empty, alpha=1, B=q−b is ternary, and wt(B)=136−1+3=138. Its zero support has size118. Equation (A9) supplies S self-consistency with exactly16 defects. W is x_2=x_3=0 and D=x_2+x_3+x_2x_3.

If an R completion existed, its weight118 and the retained R energy identity would force u=24. **This is an S witness with the necessary first-branch counts, not an actual u=24 full-system witness.**

### Second branch: U={0,1,2,3}

Modulate delta by the character (−1)^(t_2). Oddness of phi makes C modulate by the same character, so (A9) is preserved. Its b is the former b translated by4. The four U values now come from a=4,5,6,7 in (A4), hence all are0. Therefore E is empty, alpha=0, wt(B)=136+4=140 and |T|=116. The support still has affine rank8 and L=16. Here W is x_0=x_1=0.

An R completion would force u=32, but no such completion is proved. This establishes algebraically that **neither L16 count branch can be rejected using S alone**. It does not give the half-subset required by Theorem HD.

## 6. Corrected deliverable and exact remaining gap

The load-bearing new written results are:

1. Theorem HD and its full512-bit reconstruction, from the earlier packet, independent of evaluation output.
2. The complete signed-Gold S theorem (A9), full affine rank and both count-branch constructions above, now proved without replay.

The literal control functions, direct N checks, detailed histograms and specialized outer-profile exclusions in the earlier packet are retained as **unadmitted observations / unreconstructed candidate consequences**, not accepted in-kernel verification. No claim that they have been independently checked survives this overlay.

Per-case scientific verdicts remain:

- **(16,24): UNRESOLVED.** A full-rank S profile with T118 is proved in writing; the required59-point prescribed-XOR half-design satisfying every slab is not constructed or excluded.
- **(16,32): UNRESOLVED.** A full-rank S profile with T116 is proved in writing; the analogous58-point half-design is not constructed or excluded.
- **(20,24): UNRESOLVED.** No S profile or universal S exclusion is proved; any such profile still needs the59-point half-design on its T118.
- **U2: UNPROVED.** Its exact replacement is HD-U2: no unpruned S-consistent delta admits the prescribed-XOR half-subset with all256 discrepancies at most3.

This is a documented new-representation barrier, not a restatement of two independent ternary choices or a promise of a later solver. Both Boolean transforms, the full C+3P lift, the original balance and all512 coefficients remain explicit. No unrestricted balanced NL242 or whole-type claim follows. Independent review, novelty clearance and formal verification are **not performed**.
