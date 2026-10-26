# Joint S/R realization obstruction for the archived (8,136), L=8 profile

Observed before creation: **2026-10-23T15:06:24-07:00**. Author: InfoBalancedNL242, info-6. **CANDIDATE WRITTEN PROOF**, awaiting actual independent reconstruction and parent checking. No scientific program, solver, enumeration, Walsh replay or formal verification was executed.

This is one joint-realizability packet, not another per-defect increment. It introduces an exact signed-support invariant beyond the already saturated boundary-plus-Parseval composition. Its conclusion excludes **one archived canonical count profile from every spatial placement**. It does not exclude either full-rank type in its entirety, any of the other seven type families, or balanced242 existence.

## 1. Exact frozen sources and trust boundary

All paths below are relative to the aifours repository root.

| Source | Observed SHA256 | Exact role |
|---|---|---|
| `information-science/evidence/hard-continuation-20261015/quadratic-distance/remaining-types/results/explore.json.gz` | `1e1470a7d5380bb61ac5ebb95221f531c44fdd67f53a3463fe7e4fc3c98d5136` | member `explore.json`, exact `(8,136)` canonical-pair count vector |
| `information-science/evidence/hard-continuation-20261015/quadratic-distance/remaining-types/result.json` | `5548853b6be9c2af0d251afe2ca4101c4b70437fdda19e1d5c21977e4aa16d2c` | archived finite-audit receipt; stats z=70,c=2,L=8,w_R=88,Gamma=-4096 |
| `information-science/evidence/hard-continuation-20261015/proof.md` | `d2c1605d8ee20423e137066b62b3dac31406bd4380d075c1b85064c01cf6dff9` | canonical odd-spectrum normalization and quadratic-residue lemmas, §§2,4 |

The archived profile and receipt were read, not rerun. The new support theorem and all dimension/sign cases below are proved here. The new packet does **not** import the pending sparse/four-five/six/seven-defect conclusions, the unrestricted covering-radius242 claims, the unreviewed round2 claims, or an unavailable classification. Its m=236 contradiction stands independently of acceptance of those later small-defect manuscripts.

The canonical imported facts are: both K_g,K_h are2 modulo8; H K_g,H K_h are±256 pointwise; the square residues are quadratic. These are classical tools, not new discoveries here. Quadratic Fourier magnitudes and H²=256I are also standard elementary identities and used explicitly.

## 2. Literal profile and quantifiers

Let V=F_2^8, and `H v(x)=sum_{u in V}v(u)(-1)^(u.x)`.

Consider **any assignment** of canonical pairs `(K_g(u),K_h(u))` to the256 positions having the following multiplicities:

|K_g|K_h|count|
|---:|---:|---:|
|2|18|2|
|2|-22|22|
|2|26|44|
|-6|18|1|
|-6|-22|22|
|10|10|18|
|10|18|1|
|-14|2|6|
|-14|10|1|
|-14|-14|52|
|18|10|1|
|-22|2|19|
|-22|-6|20|
|26|2|47|

Suppose they are genuine canonical Boolean spectra, so their transforms are±256 and their quadratic difference residue has the stated type `(polar rank8,weight136)`. The claim is that **no such assignment exists**. No position, coordinate basis, defect set or sign pattern is fixed in advance.

Set

`S=K_g+K_h`, `R=K_g-K_h`, `p=R/8`, `D=p mod2`, `chi=(-1)^D`.

Canonical congruences give `S=4+8D mod16`. Under the cap28, `T=chi S` lies in `{-28,-12,4,20}`. Let

`A={u:T(u)=-12 or4}`, `L=|A|`,

`delta(u)=chi(u)` when T=-12, `delta(u)=-chi(u)` when T=4, and0 otherwise.

Thus delta has exactly L nonzero entries, all±1, and `S=-chi+delta mod3`.

The profile has the magnitude counts

`(N_0,N_4,N_8,N_12,N_16,N_20,N_24,N_28)`

`=(70,1,2,7,50,61,134,187)`.

In particular L=8, d=wt(D)=136, and

`sum R^2=90112`, `sum S^2=172032`,

`Gamma:=sum chi S=-28*187-12*7+4+20*61=-4096`.

A quadratic of weight136 on eight variables has nonsingular polar form, and hence `W_D=H chi` takes only±16. Put `Q=W_D/16`; then Q is a sign function.

## 3. Why the profile forces m=236

Define phi(n) to be the unique member of `{0,+1,-1}` congruent to the integer n modulo3. Put

`b=phi(H delta)`, `m=|supp b|`, `B=(H S)/512`.

Because `H K_g,H K_h` are±256, exactly one of H S,H R is nonzero at every x, and its value is±512. In particular B takes only0,±1 and

`w_R:=#{x:B(x)=0}=sum R^2/1024=88`.                       (1)

Since512=-1 modulo3, transforming `S=-chi+delta mod3` gives

`B=phi(Q-H delta)`.

For Q=±1, the exact sine addition formula, or its three residue cases, gives

`B=Q(1-(3/2)b^2)+(1/2)b`.                                 (2)

Thus:

- b=0 implies B=Q;
- b=Q implies B=0;
- b=-Q implies B=-Q.

The count of b=Q is exactly w_R. It follows that

`sum Q B=(256-m)-(m-w_R)=256+w_R-2m`.

Character symmetry also gives

`Gamma=(1/256)sum W_D(H S)=32 sum Q B`.

Therefore every genuine spatial realization of this profile must satisfy

`m=(256+w_R-Gamma/32)/2`.

Substituting the actual profile values w_R=88 and Gamma=-4096 yields

`m=(256+88+128)/2=236`.                                   (3)

This conclusion uses the actual complementary S/R Fourier supports and the actual quadratic sign Q. It is not a scalar Parseval inference alone, nor an assumed placement of the count vector.

## 4. Sharp eight-point signed-support bound

**Lemma.** For any function `delta:F_2^8 -> {0,±1}` with exactly eight nonzero entries,

`m=wt(phi(H delta))<=224`.                                (4)

The bound is sharp. We prove it for every possible affine dimension and every sign pattern, without enumeration.

### 4.1 Universal preliminary constraints

Let d be the affine dimension of the eight distinct support points. Necessarily `3<=d<=7`: a two-flat has only four points, and eight points span at most seven affine directions.

The zero/nonzero pattern of phi(H delta) depends only on the restriction of the transform character to the direction space of the affine span. An affine support translation merely multiplies H delta by a sign character, and phi is odd. Consequently

`2^(8-d) divides m`.                                      (5)

Parseval, reduced modulo3, gives another exact constraint:

`m =sum (H delta)^2 =256 sum delta^2=256*8=2 mod3`.         (6)

The first equality here is a congruence modulo3: an integer square reduces to0 or1 exactly according as its residue phi is0 or±1. It is not an equality over Z.

For d=3 or4, equation (5) makes m a multiple of16. Among multiples of16 at most256 satisfying (6), the largest is224. This covers **every** support and sign pattern at these dimensions, without needing to classify their relation codes.

### 4.2 A single exact formula for the higher-dimensional cases

Write the support as u_1,...,u_8, and its signs as epsilon_i. Define the affine relation code

`C={c in F_2^8: sum c_i=0 and sum c_i u_i=0}`.

The map with columns `(1,u_i)` has rank d+1, so

`dim C=7-d`.

Every nonzero relation has even weight4,6 or8. Weight2 would equate two distinct support points and is impossible. For P in C put `e_P=product_{i:P_i=1}epsilon_i`; the map P->e_P is a character of C.

Let `K_j(w)=[z^j](1-z)^w(1+z)^(8-w)` and put

`F(w)=K_1(w)+K_4(w)+K_7(w)`.

The relevant exact values, obtained by the displayed binomial products, are

`F(0)=86`, `F(4)=6`, `F(6)=-18`, `F(8)=54`.               (7)

For clarity, K_1,K_4,K_7 at weights4,6,8 are respectively

- w=4: `0,6,0`;
- w=6: `-4,-10,-4`;
- w=8: `-8,70,-8`.

To derive the support formula, include both global signs in the eight signed character evaluations. Their phase vectors form a coset of C-perp. For a phase vector having j negative signs the sum is8-2j, divisible by3 exactly for `j in {1,4,7}`. The character indicator of the coset is

`(1/|C|)sum_{P in C}e_P(-1)^(P.phase)`.

Each phase vector occurs `2^(8-d)` times as `(x,global sign)` varies. Dividing by2 to remove the global sign and summing the indicator gives the exact ambient zero count

`#{x:phi(H delta)(x)=0}=86+sum_{P in C\{0}}e_P F(wt P)`.

Hence

`m=170-sum_{P in C\{0}}e_P F(wt P)`.                     (8)

This is an exact relation-code identity, not a search miss or a sampled evaluation.

### 4.3 Affine dimension7: no relation

Here C=0, so (8) gives

`m=170`.

All signs are included: affine sign characters on eight affinely independent points can realize every sign pattern; equation (8) also shows the value is independent of the signs directly.

### 4.4 Affine dimension6: one even relation, all weights and signs

Here dim C=1. Its unique nonzero relation P has weight4,6 or8; its sign e_P can be±1. Formula (8) gives the complete list:

| wt P | e=+1 | e=-1 |
|---:|---:|---:|
|4|164|176|
|6|188|152|
|8|116|224|

Thus no dimension6 sign case exceeds224. In particular, **one relation exhausts this dimension** because the augmented affine evaluation map has rank7 and its kernel in eight coefficient variables has dimension1. There are no additional even relations being silently omitted.

### 4.5 Affine dimension5: two relations, all weight triples and characters

Here dim C=2. Its three nonzero words P_1,P_2,P_3 satisfy `P_3=P_1+P_2`. Their signs satisfy `e_1 e_2 e_3=1`, giving exactly four sign triples.

Each of their weights is4,6 or8. Each coordinate appears in either zero or two of these three words, so the sum of their weights is at most16. Up to permutation the only possible triples are

`(4,4,4)`, `(4,4,6)`, `(4,4,8)`, `(4,6,6)`.

This list follows from evenness and the lower bound4; a triple starting with6 would already have sum at least18. Applying (7)–(8) to each of the four sign characters gives the exhaustive table:

| weight triple | (+,+,+) | (+,-,-) | (-,+,-) | (-,-,+) |
|---|---:|---:|---:|---:|
|(4,4,4)|152|176|176|176|
|(4,4,6)|176|152|152|200|
|(4,4,8)|104|224|224|128|
|(4,6,6)|200|128|176|176|

Repeated weights may make some columns equivalent, but no sign character is dropped. Every value is at most224.

The dimension3/4 congruence argument, the dimension5 table, the dimension6 table and the dimension7 identity cover every possible affine rank and every signed support. This proves (4).

### 4.6 Exact sharpness control for the auxiliary lemma

Let U be any linear three-flat of V and set

`delta=1_U-2 1_{0}`.

It has eight support points, seven signs+1 and one sign−1. Its transform is

`H delta=8 1_{U-perp}-2`.

This is6 at the32 points of U-perp and−2 at the other224 points. Therefore phi(H delta) is zero at32 and nonzero at224. This proves sharpness of (4) symbolically. It is a signed-support control, **not** a Boolean242 witness or a full S/R realization.

## 5. Exclusion of the single archived profile

Equation (3) forces m=236 for every putative genuine canonical realization of the exact archived multiplicities. Lemma (4) gives m<=224 because its signed defect support has exactly eight points. Since236>224, no such realization exists.

The conclusion is stronger than rejection of a chosen spatial ordering: **all assignments of the table's pairs to all256 positions are covered** through all possible affine dimensions and signs of delta. It is weaker than a type exclusion: other multiplicities of type(8,136), including other L=8 profiles, remain outside this contradiction.

## 6. One consolidated boundary-redistribution consequence

The same new input gives a useful full-rank L=8 condition beyond the old boundary-plus-Parseval composition. Put

`z=N_0`, `c=N_8`, `u=z+2c`, `d=N_8+N_24`.

Canonical magnitude accounting and S/R partition give

`w_R=64+(5/16)d-u/4`,

`Gamma=40d-6656-64L-32u`.

The first follows from `sum R^2=65536+320d-256u`; the second follows by summing `T^2+8T=560-512 1_A` and using `sum(S^2+R^2)=262144`.

Combining these with section3 gives

`m=264-(15/32)d+(3/8)u+L`.                                (9)

At L=8, d=120 makes m>=216 and d=136 makes m>=209, since u>=0. The proof of the lemma gives a stronger discrete fact in this range: **m>200 forces m=224**. Indeed at affine dimensions<=4 the multiples-of16/mod3 constraints have no value between200 and224 other than224, and each higher-dimensional table has the same gap.

Therefore every genuine full-rank L=8 target must satisfy

`m=224`, `w_R=96`, `Gamma=-3072`,

and, by (9),

- type(8,120): `N_0+2N_8=22`;
- type(8,136): `N_0+2N_8=42`.

The archived profile has u=74 and is rejected. These are new **conditional joint-realizability** constraints at the existing boundary, not a claim that those remaining aggregate values are attainable or that L=8 is globally impossible.

## 7. Honest scope and updated residual state

If this candidate passes actual reconstruction, the exact archived `(8,136),L8` vector is removed. Of the previously five surviving archived scalar vectors, this packet leaves four unexcluded by its check:

`(2,192),L8`; `(6,112),L17`; `(6,128),L17`; `(8,120),L10`.

These are still count profiles, not Boolean functions. The two earlier L2 vectors were already removed by the all-type multiplicity bound. There are **still seven entire residue types unexcluded**, and there is still no balanced242 truth table or unrestricted upper exclusion.

The earlier composition-saturation decision remains valid: this packet uses genuinely additional signed-support code realizability, not merely the old boundary theorems plus Parseval. It is the one remaining joint-realizability direction authorized by the parent, kept as one standalone packet rather than per-defect appendices.

Correctness level: complete author-written candidate; actual separate reconstruction and parent checking pending. Formal verification: not performed. Scientific execution: none. Priority of the elementary signed-support bound is not cleared, and no discovery, new-general-method or full-book-solution claim is made.
