# A different P44 representation: diagonal-minus-Bell witnesses, Grassmannian soundness and a phase-Gram PPT dual

Observed clock before writing: **Sun Oct 25 04:33:56 PDT 2026** (`/bin/date`). Owner PhysicsPPT44-2 / physics-3. **WRITTEN CANDIDATE ONLY.** No scientific interpreter, eval, arithmetic program, enumeration, certificate replay or solver was run for this packet. All algebra below is written reasoning. No source/input-pinned GO exists.

This follows completion of the assigned v30-E written review. It is a materially different representation from compressing the Krebs–Gachechiladze state or increasing its normalized Bose level. It does not use the unadmitted x1111 finite table as a proof premise.

## 1. Scope and exact mathematical outcome

The physical target is still an explicit4 by4 rational PPT density matrix of Schmidt number at least3, or a proof excluding every such state. Neither is obtained here.

This packet proves three elementary reductions for a named witness class:

1. Universal **complex** two-block-positivity is exactly a scalar inverse-Gram inequality over the complex Grassmannian of two-planes in C4. There is no real-vector/grid replacement.
2. Whether such a witness detects **any PPT state**, without imposing a restriction on the original tested state, is exactly a four-dimensional positive-Gram optimization after a diagonal-unitary average. Every negative point gives an explicit PPT density matrix.
3. Two-positivity already excludes every dual Gram point whose entrywise absolute-value matrix is completely positive in the real nonnegative sense. A rational Gram control shows that this residual restriction is not automatic: taking entrywise absolute values can destroy positive semidefiniteness.

These are written representation/certificate lemmas, not an unrestricted no-go. In particular, no assertion is made that this witness class actually contains a two-positive indecomposable member. That headroom/source-status question and the two remaining quantified inequalities remain open here; no scientific assay is proposed or authorized.

## 2. Witness class and a complete Grassmannian test

Fix strictly positive real coefficients a_ij for i,j=0,1,2,3. Define

```
Omega = 00+11+22+33,
W(a) = sum_(i,j) a_ij P(ij)-P(Omega).
```

For a coefficient matrix C, its expectation is

```
Q_a(C)=sum_(i,j) a_ij |C_ij|^2-|Tr C|^2.             (1)
```

Let U be ANY complex4 by2 isometry, `U*U=I2`, and put

```
u_j=U* e_j,
A_j(U)=U* diag(a_0j,a_1j,a_2j,a_3j) U.
```

Each A_j is positive definite by strict positivity of all a_ij. Define

```
H_a(U)=sum_(j=0)^3 u_j* A_j(U)^(-1) u_j.            (2)
```

**Lemma. W(a) is two-block-positive if and only if H_a(U)<=1 for EVERY complex isometry U.**

Proof. A rank-at-most-two C can be written C=UZ by extending its column space to a two-plane. Let z_j be the jth column of Z. Then

```
sum a_ij|C_ij|^2=sum_j z_j* A_j z_j,
Tr C=sum_j u_j* z_j.
```

Weighted Cauchy–Schwarz gives

```
|Tr C|^2 <= H_a(U) sum_j z_j* A_j z_j.
```

Thus (2)<=1 is sufficient. Conversely choose `z_j=A_j^(-1)u_j`. Both the trace and the positive energy equal H_a(U), so (1) is `H_a(U)[1-H_a(U)]`. H_a(U) is positive; if it exceeds1 this is an explicit complex rank-at-most-two negative direction. This proves necessity and includes rank-one C as well.

Changing the orthonormal basis of the same two-plane conjugates all A_j and u_j consistently, leaving H invariant. Thus the true parameter is the complex Grassmannian, not an extra arbitrary choice of basis. A2 by2 inverse is its adjugate divided by a strictly positive determinant, so this condition has an exact algebraic form in the real and imaginary entries of U. No finite table proves it without a full quantified argument.

## 3. An unrestricted-input PPT reduction for this witness class

W(a) is invariant under every local diagonal unitary `D tensor conjugate(D)`. Averaging any tested PPT state over these four independent phases preserves positivity, PPT and its W expectation. Finite root-of-unity averaging of sufficient order gives the same entry selection, so no measure-theoretic assumption is essential.

The surviving unnormalized operator has the form

```
R = sum_(i,j) r_ij |ii><jj|
    +sum_(i!=j) s_ij P(ij),                         (3)
```

where r is a Hermitian4 by4 matrix. Positivity of R is exactly `r>=0` and `s_ij>=0`, because these act on mutually orthogonal supports. Bob partial transpose has singleton diagonal entries r_ii and, for each unordered pair i,j, the block

```
[ s_ij       r_ij ]
[ conj(r_ij) s_ji ].
```

Consequently the exact PPT condition is

```
r>=0, s_ij>=0, s_ij s_ji>=|r_ij|^2.                 (4)
```

Write `d_i=a_ii-1` and `c_ij=sqrt(a_ij a_ji)>0`. For a fixed r, minimizing the pair contribution `a_ij s_ij+a_ji s_ji` subject to (4) gives

```
2 c_ij |r_ij|,
s_ij=|r_ij| sqrt(a_ji/a_ij),
s_ji=|r_ij| sqrt(a_ij/a_ji).                         (5)
```

This follows either by completing a square or by the arithmetic–geometric mean inequality; equality is explicit, including the zero-correlation case.

Hence define the exact reduced PPT objective

```
F_a(r)=sum_i d_i r_ii
       +2sum_(i<j)[c_ij |r_ij|-Re(r_ij)].           (6)
```

**Lemma. W(a) has negative expectation on SOME PPT state if and only if F_a(r)<0 for SOME nonzero Hermitian r>=0.**

One direction uses the phase average and lower bound (5). For the other, build (3) using (5), and divide by its positive trace. This is a fully specified PPT density matrix with negative W expectation. Thus, together with Section2, any exact pair a,r satisfying the two indicated conditions would prove SN>=3 with a universally sound complex witness.

This does not claim that arbitrary PPT states have the form (3); only the W-preserving local-unitary average has that form. The tested input was unrestricted before averaging. The witness family remains restricted throughout.

For a rational-state construction, it suffices to take a_ij and all real/imaginary parts of r rational, with |r_ij| rational and every square root in (5) rational. For example, choosing the a_ij as positive rational squares makes the ratios in (5) rational. These are sufficient exact arithmetic design conditions, not a claimed found solution.

## 4. A dimension-four matching inequality forced by two-positivity

For any perfect matching M of the four indices and any nonnegative real vector z, construct C supported on the two matched2 by2 blocks. Set C_ii=z_i. On an edge i,j choose nonnegative off-diagonal entries whose product is z_i z_j and which minimize their weighted energy; its value is `2c_ij z_i z_j`. Each block has determinant zero and rank at most one, so the whole C has rank at most two. Zero z entries cause no exception.

Two-block-positivity therefore implies, for every z>=0,

```
Q_M(z) = sum_i d_i z_i^2
         +2sum_(ij in M)(c_ij-1)z_i z_j
         -2sum_(ij not in M)z_i z_j >=0.             (7)
```

In particular, with

```
Q_all(z)=sum_i d_i z_i^2+2sum_(i<j)(c_ij-1)z_i z_j,
```

we have

```
Q_all(z)=Q_M(z)+2sum_(ij not in M)c_ij z_i z_j>=0.   (8)
```

This is a necessary copositivity condition, not a sufficient replacement for the Grassmannian condition. Its dimension-four origin is explicit: two rank-one blocks cover all four indices while keeping rank at most two. Applying the same construction indiscriminately to five indices would increase the rank and is not justified.

## 5. A complete-positive absolute-Gram no-detection barrier

Assume the nonnegative real matrix `B_ij=|r_ij|` has a completely positive decomposition

```
B=sum_l z_l z_l^T, with every z_l entrywise nonnegative.    (9)
```

This term means the real nonnegative matrix cone; it is not the unrelated phrase “completely positive quantum map.” From `Re r_ij<=|r_ij|`, (6) gives

```
F_a(r)>=sum_i d_i B_ii+2sum_(i<j)(c_ij-1)B_ij
       =sum_l Q_all(z_l)>=0                         (10)
```

for every two-block-positive W(a), by (8). Thus **any negative dual Gram point in this new representation must have a non-completely-positive entrywise absolute-value matrix**. Rank-one r is automatically excluded, because its absolute-value matrix is `|v||v|^T`. This rules out a naive pure coherent block without assuming any special state compression or Park covariance.

No classification theorem equating completely-positive and doubly-nonnegative matrix cones is imported. In particular this packet does not replace (9) by bare entrywise nonnegativity or by an unproved assertion about absolute values preserving positivity.

Two simpler preflight exclusions are also exact. Two-positivity gives d_i>=0 by testing ii. If all c_ij>=1 then every term in (6) is nonnegative. More generally put `b_ij=max(1-c_ij,0)`. If

```
d_i>=sum_(j!=i) b_ij for each i,
```

then `|r_ij|<=sqrt(r_ii r_jj)` and u_i=sqrt(r_ii) give

```
F_a(r)>=sum_i d_i u_i^2-2sum_(i<j)b_ij u_i u_j
 =sum_i[d_i-sum_j b_ij]u_i^2
  +sum_(i<j)b_ij(u_i-u_j)^2>=0.
```

Any proposed indecomposable witness in this class must escape these sufficient no-detection regions as well as pass the full complex test (2).

## 6. Literal rational control: absolute values can destroy positivity

Take four rational vectors

```
g0=(1,0), g1=(1,1/2), g2=(1/2,1), g3=(-1/4,1)
```

and their Gram matrix

```
r = [ 1     1    1/2  -1/4  ]
    [ 1     5/4  1     1/4  ]
    [ 1/2   1    5/4   7/8  ]
    [ -1/4  1/4  7/8  17/16 ].
```

It is PSD by this displayed Gram factorization. The rational vector

```
v=(1,-7/3,13/6,-1)
```

satisfies `sum_i v_i g_i=0`, hence v^T r v=0. Entrywise absolute value changes only entries03 and30, each by +1/2. Therefore

```
v^T |r| v=2*(1/2)*v0*v3=-1<0.
```

Thus |r| is not PSD and cannot satisfy (9). This is an exact written control showing that the residual phase-Gram requirement is not vacuous. It is **not** a Schmidt-three example, nor a claim that some sound W(a) detects the PPT state obtainable from this r. No coefficient a meeting both required conditions has been supplied.

## 7. Exact next gap and provenance boundaries

The earlier x1111 state-specific packet and its21-pair table are not inputs to any lemma here. The captured Yang–Leung–Tang source1603.03534v1 proves its M3-to-M3 theorem; it is not an M4 classification and is not imported as one. The old Park symplectic family is likewise not assumed to cover this16-parameter diagonal witness class. A literature-wide status/novelty/headroom audit of this class has not been performed, so it is not declared a novel open class or a promising indecomposable family.

The exact new written obligations are:

- exhibit positive rational a and an all-complex proof of (2)<=1, not merely the matching necessary inequalities;
- exhibit a rational Hermitian r>=0 escaping (9) and the other preflight barriers with F_a(r)<0, or prove impossibility uniformly for this witness class;
- even a uniform no-go for this class would **not** exclude all two-block-positive witnesses or all P44 states.

No numerical minimization, parameter grid, exact polynomial program or future GO is requested by this packet. New computation remains blocked under HOLD v2 and erratum v7. Correctness is author-WRITTEN only; independent reconstruction, formal verification, scientific admission, novelty clearance and the original full-target acceptance are all absent.
