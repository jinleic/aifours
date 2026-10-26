# Every coherent merge of the two auxiliary levels has Schmidt number two

Observed immediately before creation: **2026-10-23T14:09:38-07:00**. PhysicsPPT44 / physics-3. Immutable candidate v1. **CANDIDATE — complete written algebra; separate reconstruction and parent acceptance not yet performed.** No scientific program or executable check has been run.

## 1. Exact statement and scope

Let `|ij> = |i>_A tensor |j>_B` in the displayed computational bases and write `P(x)=|x><x|` for an unnormalized vector. Define

- `a = |00>+|11>+|22>`,
- `b = |01>+|12>`,
- `c = |10>-|21>`,
- `d_v = |02>+v|33>`,
- `e_u = |20>+u|33>`,
- `f=|30>`, `g=|32>`, `h=|03>`, `j=|23>`.

For **every** `u,v in C` (including zero), put

`R(u,v) = P(a)+P(b)+P(c)+3P(d_v)+3P(e_u)`
`         +3P(f)+3P(g)+3|v|^2 P(h)+3|u|^2 P(j)`.

Its trace is `T(u,v)=19+6(|u|^2+|v|^2)>0`, so `rho(u,v)=R(u,v)/T(u,v)` is an exact 16 by 16 density matrix.

**Theorem.** For all complex u,v, `rho(u,v)` is PPT and has Schmidt number **exactly two**. In particular there is no Hermitian two-block-positive W with `Tr(W rho(u,v))<0`.

This is a structural no-go for **one complete two-complex-parameter compression mechanism**, not a no-go for all 4 by 4 PPT states. The unrestricted P44 target remains unanswered.

### Relationship to the published 4 by 5 input

Krebs–Gachechiladze [2509.07086v1](https://arxiv.org/html/2509.07086v1), Theorem5, Fig.1, Eqs.(10)–(11), uses the unnormalized state

`R45 = P(a)+P(b)+P(c)+3P(|02>+|34>)+3P(|20>+|33>)`
`      +3P(|30>)+3P(|32>)+3P(|23>)+3P(|04>)`.

Here a,b,c are embedded in 4 by 5. This input has trace31. Define `B_uv:C^5 -> C^4` by keeping levels0,1,2 fixed and sending `|3>` to `u|3>` and `|4>` to `v|3>`. Then

`R(u,v)=(I_4 tensor B_uv) R45 (I_4 tensor B_uv)^*`.

For `(u,v)!=(0,0)`, B_uv has rank4. Thus the theorem covers **every coherent identification of the two auxiliary Bob levels while retaining the three core Bob levels**, with arbitrary complex amplitudes and imbalance. It also covers arbitrary further local filters and convex combinations of these outputs, because those cannot increase Schmidt number. It does **not** cover a general rank4 filter whose kernel has a component in the original three Bob levels.

The source already proves the SN2 property of a particular intermediate 4 by 4 endpoint in SupplementE. That is a baseline, not our result. Our candidate is the uniform all-complex merging decomposition below; novelty relative to all other literature is **UNCLEAR**.

## 2. Direct positivity, normalization, and PPT proof

Positivity follows from the displayed positive sum. The trace calculation uses

`||a||^2=3`, `||b||^2=||c||^2=2`,
`||d_v||^2=1+|v|^2`, `||e_u||^2=1+|u|^2`,
`||f||^2=||g||^2=||h||^2=||j||^2=1`.

These give `3+2+2+3+3+3+3+6|v|^2+6|u|^2=T`.

For an explicit positive partial transpose, first set

`R3=P(a)+P(b)+P(c)+3P(|02>)+3P(|20>)`.

A direct entrywise partial transpose gives

`R3^{Gamma_B} = P(|02>+|11>-|20>) +2P(|02>+|20>)`
`                 +P(|01>+|10>)+P(|12>+|21>)+P(|00>)+P(|22>)`.

For clarity, the nontrivial 02/11/20 block on the right has diagonal `(3,1,3)` and off-diagonal entries `(+1,+1,-1)` on pairs `(02,11)`, `(02,20)`, `(11,20)`, respectively. These are exactly the transposes of the 01/12, 00/22, and 10/21 source coherences. All other nonzero coherences are the two displayed rank-one 01/10 and 12/21 blocks.

Let `s=|u|^2+|v|^2`. Then the whole partial transpose is

`R(u,v)^{Gamma_B}=R3^{Gamma_B}`
`  +3P(|32>+conj(v)|03>)+3P(|30>+conj(u)|23>)`
`  +3s P(|33>)`.

For example, `P(d_v)` adds `conj(v)|03><32|+v|32><03|` after partial transpose, which is the cross term in the first new positive projector. The same calculation with e_u gives the second. This proves PPT for arbitrary complex u,v without an imported numerical certificate.

## 3. A finite character average, not a numerical sample

Use exactly

`Z4={1,i,-1,-i}`, `Z3={1,omega,omega^2}`, `omega=exp(2 pi i/3)`.

For any integer r, `sum_{z in Z4} z^r` is4 when 4 divides r and0 otherwise. The corresponding identity for Z3 has3 in place of4. Consequently, for two distinct pairs of exponents modulo `(4,3)`, averaging the product of one character and the conjugate of the other gives zero.

This is the finite Fourier identity for cyclic groups, valid exactly over the algebraic numbers. The argument below is a symbolic identity for arbitrary complex u,v. The twelve phase values are used to **define** a decomposition, not to infer an all-parameter theorem from point tests.

## 4. First decomposition: `|v|^2 <= 3|u|^2`

For z in Z4 and w in Z3, define the unnormalized vector

`psi_A(z,w) = a + z c + z^(-2) d_v`
`            + w f + w z^(-2) g`
`            + v z^(-2) w^(-1) h + v w^(-1) j`.

Its coefficient matrix is

```
M_A(z,w) = [ 1   0    z^(-2)    v z^(-2) w^(-1) ]
           [ z   1       0                  0   ]
           [ 0  -z       1          v w^(-1)   ]
           [ w   0   w z^(-2)         v z^(-2)  ].
```

Writing rows with zero-based indices, the identities

`row_2 = z^2 row_0 - z row_1`,
`row_3 = w row_0`

hold exactly. Therefore `rank M_A<=2` and `SR(psi_A)<=2`. In fact rows0 and1 are independent, but only the upper bound is needed.

The seven coefficient characters in the vector definition have exponent pairs

`(0,0), (1,0), (-2,0), (0,1), (-2,1), (-2,-1), (0,-1)`,

which are pairwise distinct modulo `(4,3)`. Therefore

`A_A := (1/12) sum_{z in Z4,w in Z3} P(psi_A(z,w))`
`     = P(a)+P(c)+P(d_v)+P(f)+P(g)+|v|^2P(h)+|v|^2P(j)`.

Subtracting this exact identity from the definition of R yields

`R = A_A + P(b)+2P(d_v)+3P(e_u)+2P(f)+2P(g)`
`          +2|v|^2P(h)+(3|u|^2-|v|^2)P(j)`.

Every displayed scalar is nonnegative under the section's hypothesis. Each residual vector has Schmidt rank at most two: b,d_v,e_u have at most two product terms, and f,g,h,j are product vectors. Thus this is an explicit finite conic Schmidt-rank-two decomposition.

## 5. Second decomposition: `|u|^2 <= 3|v|^2`

Define

`psi_B(z,w) = a + z b - z^(-2) e_u`
`            + w z^(-2) f - w g`
`            - u w^(-1) h + u z^(-2) w^(-1) j`.

Its coefficient matrix is

```
M_B(z,w) = [      1   z    0             -u w^(-1) ]
           [      0   1    z                      0 ]
           [ -z^(-2)  0    1    u z^(-2) w^(-1)   ]
           [ w z^(-2) 0   -w              -u z^(-2) ].
```

The exact row identities are

`row_2 = -z^(-2) row_0 + z^(-1) row_1`,
`row_3 = w z^(-2) row_0 - w z^(-1) row_1`.

Thus every psi_B has Schmidt rank at most two. Its seven exponent pairs are

`(0,0), (1,0), (-2,0), (-2,1), (0,1), (0,-1), (-2,-1)`.

They too are pairwise distinct modulo `(4,3)`; signs do not affect the diagonal character average. Hence

`A_B := (1/12) sum_{z in Z4,w in Z3} P(psi_B(z,w))`
`     = P(a)+P(b)+P(e_u)+P(f)+P(g)+|u|^2P(h)+|u|^2P(j)`.

It follows that

`R = A_B + P(c)+3P(d_v)+2P(e_u)+2P(f)+2P(g)`
`          +(3|v|^2-|u|^2)P(h)+2|u|^2P(j)`.

Again this is a finite positive sum of projectors on Schmidt-rank-at-most-two vectors whenever the section's hypothesis holds.

## 6. All parameters, exact Schmidt number, and the witness consequence

For any nonnegative x,y, at least one of `y<=3x` and `x<=3y` holds. For a deterministic unambiguous choice, use the first decomposition if `|u|>=|v|`, and the second otherwise. This covers all complex u,v, with no division by u or v and no excluded endpoint, including `(0,0)`.

To turn either conic decomposition into a normalized convex decomposition, divide by T, normalize each nonzero vector, and multiply its coefficient by its squared norm/T. The weights are nonnegative and sum to one because the operator sum is exactly R. No unspecified limiting procedure is needed. There are at most twelve averaged terms plus seven residual terms.

For the matching lower bound SN>=2, project locally onto Alice levels0,1,2 and Bob levels0,1,2. The resulting nonzero unnormalized state is exactly R3. Its range consists of coefficient matrices

```
C = [ a  b  d ]
    [ c  a  b ]
    [ e -c  a ].
```

If C has rank at most one, its minors using rows0,1 / columns0,1 and rows1,2 / columns1,2 give

`a^2-bc=0`, `a^2+bc=0`.

Over C these imply a=0. Thus every product vector in the range is orthogonal to the nonzero range vector `|00>+|11>+|22>`. R3 cannot be a positive sum of product projectors: the range of any such sum is spanned by those product vectors, whereas the displayed a direction would be missing. Hence R3 is entangled. Local projections cannot turn a separable state into an entangled state, so R(u,v) is entangled as well. Combining with SN<=2 proves SN=2.

Finally, if W is two-block-positive, its expectation on each vector appearing in either finite decomposition is nonnegative. Linearity therefore gives `Tr(W R)>=0` and `Tr(W rho)>=0`. A negative separator cannot exist for this entire family.

## 7. Imports, novelty, and what this does not settle

The proof imports only elementary coefficient-matrix/Schmidt-rank equivalence, the definition of Schmidt number, the elementary range-of-a-positive-sum fact, and finite root-of-unity orthogonality. The state family's provenance is the explicitly pinned primary source; no source theorem asserting its SN3 is needed for the restricted upper bound proved here. The direct PPT identity also avoids relying on a solver or on the published PPT claim.

- **Correctness:** complete author-written candidate; parent and separate reconstruction pending.
- **Finite/scientific execution:** not performed; no Python arithmetic, SDP, enumeration, numerical replay or formal build.
- **Formal/kernel verification:** not performed.
- **Outside-model CLI or human review:** not performed.
- **Scope:** complete for arbitrary complex coherent merges of the two auxiliary Bob levels and all further local filtering/convex mixing of those outputs. Not general 4 by 4 PPT states, not arbitrary 5-to-4 Bob filters, not all local extensions.
- **Novelty:** unclear. SupplementE already closes a coordinate endpoint. No priority claim follows from the bounded search.
- **Significance:** a precise reason the simplest dimension-saving compression cannot improve the known 4 by 5 construction to P44; no broad book problem or unrestricted no-go is claimed.

The next genuinely different P44 route must either mix a core Bob level into the discarded direction, alter the PPT core/extension data, or produce an indecomposable two-positive map outside the already-classified symplectic family. The current theorem is an obstruction to the frozen route, not permission to silently change targets.
