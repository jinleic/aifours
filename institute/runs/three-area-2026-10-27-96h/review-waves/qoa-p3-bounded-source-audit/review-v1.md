# QOA generalized cube: independent source and proof audit, v1

Observation used while preparing this report: 2026-10-28T17:05:17-0700 PDT. All mathematical inputs below are the named public v1 article, elementary linear algebra and finite-field calculations reconstructed here; no prior aifours review or disposition is used as a proof or premise.

## Verdict and findings

**Proposition 4.8 is correct as an existence/generation equivalence**, for fixed vector representatives, fixed physical tensor factors and fixed bases on the three address parties. Its converse is constructible, not merely asserted. Appendix H contains three dimensionally incorrect trace subscripts, corrected below. The article's stronger, literal claim of a **one-to-one correspondence between QOA row arrangements and generalized cubes** is false for its own Definition 4.1: distinct valid arrays can have the same coherent row sum and hence generate the identical cube. This does not refute the proposition's existence equivalence.

* **MAJOR-1 — S1.p3, S1.p5, S4.p1 and S5.p2, object-level one-to-one wording.** The explicit orthonormal-row counterexample in §5 gives two genuinely distinct QOA arrangements, not related by row permutation or row phases, with exactly the same sum and the same generated cube. A bijection is recovered only after quotienting QOAs by equality of their coherent sums and fixing the address basis; the article does not state that quotient. This is not an error in the weaker wording of Proposition 4.8 itself.
* **MINOR-1 — Appendix H, case 3 `A8.Ex32.m1` and `A8.p5.m4`; case 4 `A8.Ex34.m1`.** Case 3 writes `Tr_{l_1,...,l_{t-1}}` twice, although it introduced only `t-2` traced output parties and must retain two output parties. Replace both occurrences by `Tr_{l_1,...,l_{t-2}}`. Case 4 writes `Tr_{l_1,...,l_{t-2}}` after the preceding line correctly traces `t-3` outputs; replace by `Tr_{l_1,...,l_{t-3}}`. Literally adding the extra traced party leaves respectively a `d²`-dimensional or `d²`-dimensional operator where `I_{d³}` is asserted; as written some indices are also undefined. These are exact-source rendering errors, not parser artifacts: both TeX annotation and visible MathML show the same subscripts. The corrected expansion in §3 proves the result.
* **MINOR-2 — Definition 4.1, phase convention.** The formula involves the coherent sum of row **vectors**, so individual row phases are mathematically relevant; a list of physical pure-state rays alone does not determine whether (7) holds. §5 exhibits the same row rays with one phase changed, one representative satisfying (7) and the other not. Interpreting the source's explicit kets as phase-fixed vectors resolves the ambiguity; the proposition under that convention is sound.
* **FATAL:** none identified in the reconstructed existence equivalence. No general proof is inferred from a checked example.

The strongest target-relevant negative result here is exact: **even at `d=8`, a 3-uniform seven-party state and its fixed-plane generalized four-square array need not consist of product cells across the four physical output parties** (§6). Thus generalized QOA/GMOQLC existence is not, by itself, an ordinary four-MOQLS8 nonclassicality result. A classical ordinary four-family can nevertheless be exhibited from the same finite-field seed; it is not a genuinely nonclassical witness.

## 1. Source identity and actual read coverage

Primary article: Yajuan Zang, Paolo Facchi and Zihong Tian, *Quantum combinatorial designs and k-uniform states*, arXiv:2111.04055v1, local copy `public-sources/zang-facchi-tian-2111.04055v1.html` under the run root; 1,446,860 bytes, SHA-256 `9b5efb907f2172be70c7d463a8bbbbc25e63e9a1a7654d7e9015b988a34d724e`. Appendix H is exactly UTF-8 bytes `[972061,1019565)` of that file, SHA-256 `3da2eecce9c80126564f3d077ee5c71c9f22981c92ef12b39e2b317cd955ec1b`. The separately retained `public-sources/qoa-example-free-part-3-v1.html` has SHA-256 `10f36755c68b0c2929806a9a5e2faf785e96fe67b1ebd99c47fba9ca3c40896e`; it was hashed but not used as a proof input.

Read in full, including every equation and surrounding prose: Definition 4.1 (`S4.Thmtheorem1`, QOA); Definition 4.6 (`S4.Thmtheorem6`, equations 15–22); Remark 4.7; Proposition 4.8; and all of Appendix H (`A8`, equation 33 and all four cases). Also read the needed original definitions and dependencies: `S4.p1`–`S4.p3`, Definition 4.2 (generalized squares), Definition 3.3 (QLC), Definition 3.6 and `S3.SS2.p5` (ordinary mutual cube orthogonality), the classical-cube discussion and Lemma 3.1 in `S3.SS1`, Definitions 2.5, 2.6 and 2.8, Lemma 2.7 and `S2.SS2.p3`–`p4` (ordinary/classical QLS), Example 4.9 and `S4.p7`, and the article's conclusions `S5.p2`. Proposition 4.4 and its opening expansion were read for context, but §7 proves the needed square bridge directly. This is not a claim to have read every unrelated part of the paper.

The complete math of each named definition, Remark 4.7, Proposition 4.8, Example 4.9's formula, and Appendix H was read from HTML `alttext`; every such MathML node has a TeX annotation and its annotation matches the alt text. Appendix H contains 49 such nodes; Definition 4.6 contains 23. The only image in those primary proof/definition scopes is the cube-index sketch in Definition 4.6, which has no mathematical alt text; its associated public image `https://arxiv.org/html/2111.04055v1/cube2.png` was inspected visually and is simply the three-index arrangement of the stated cells. That separately served image is not covered by the local HTML hash and is not needed for any proof below. The disputed H subscripts were additionally checked against visible MathML, not merely OCR or generated prose.

## 2. Definitions and normalization

Let `d >= 2`, `t >= 3`, `H = C^d`, and let `x=(i,j,k) in [d]^3`. A QOA `(d³,t+3,d,3)` in the article is an ordered arrangement of `d³` **unit vectors** `phi_r in H^(tensor (t+3))`, satisfying for each three-party set `S`

```
sum_{r,s} Tr_{S^c} |phi_r><phi_s| = I_{d³}.                 (Q)
```

There is no individual-row orthogonality or product-across-columns requirement in Definition 4.1. Put `Phi = sum_r phi_r`. Equation (Q) is exactly `Tr_{S^c}|Phi><Phi| = I_{d³}`. Taking its trace gives `||Phi||²=d³`; the normalized 3-uniform state is `Phi/d^(3/2)`, whose three-party reductions are `I_{d³}/d³`. A pure state with these normalized reductions is all that is used in the proof. The phrase `r=d³` concerns the number of QOA rows; it does not force `d³` nonzero computational-basis amplitudes in a fixed basis.

For chosen product bases on three chosen address parties, define uniquely

```
Phi = sum_{i,j,k} |i,j,k> tensor psi_{i,j,k},
psi_{i,j,k} = (<i,j,k| tensor I) Phi in H^(tensor t).       (1)
```

Each `psi` is a whole `t`-partite vector: **no factorization across those `t` parties is assumed**. A `t`-GMOQLC in Definition 4.6 consists of these `d³` unit vectors, with the full orthogonality and partial-trace equations (15)–(22), not merely `d³` unrelated orthogonal states. For `t>3` they occupy only a `d³`-dimensional subspace of a `d^t`-dimensional output Hilbert space. For `t=3` they are an orthonormal basis of the entire output space.

## 3. Complete four-case reconstruction, in both directions

For any three-party set write `A` for its surviving address coordinates, `B` for its surviving output parties, `|A|+|B|=3`; let `a,a'` denote their address values and let `u` denote the discarded address values. In the tensor order `A` then `B`, direct partial trace of (1) gives

```
R_{A,B} = sum_{a,a'} |a><a'| tensor E_B(a,a'),
E_B(a,a') = sum_u Tr_{outputs outside B} |psi_{a,u}><psi_{a',u}|.  (2)
```

This is an entrywise identity, including off-diagonal `a != a'`; the required condition is `E_B(a,a') = delta_{a,a'} I_{d^|B|}`. Empty sums of traced parties mean the identity operation. All cases and source equation numbers are:

| Surviving address parties `A` | Surviving outputs | Explicit requirement / definition equation |
|---|---:|---|
| `{1,2,3}` | 0 | `<psi_{i',j',k'}|psi_{i,j,k}> = delta_ii' delta_jj' delta_kk'`, (15). This fixes each cell's norm to 1. |
| `{1,2}` | any 1 `s` | `sum_k Tr_{outputs except s}|psi_{i,j,k}><psi_{i',j',k}| = delta_ii' delta_jj' I_d`, (18). |
| `{1,3}` / `{2,3}` | any 1 `s` | same formula summing `j` / `i`, respectively (17) / (16). |
| `{1}` | any 2 `s,r` | `sum_{j,k} Tr_{outputs except s,r}|psi_{i,j,k}><psi_{i',j,k}| = delta_ii' I_{d²}`, (20). |
| `{2}` / `{3}` | any 2 `s,r` | sum `i,k` / `i,j`, respectively (21) / (19). |
| empty | any 3 `s,r,v` | `sum_{i,j,k} Tr_{outputs except s,r,v}|psi_{i,j,k}><psi_{i,j,k}| = I_{d³}`, (22). |

The first case gives `1` reduction, the next `3t`, the next `3*binom(t,2)`, and the last `binom(t,3)`, totaling `binom(t+3,3)`—every three-party set exactly once. In particular `t=3` means zero output traces in the final case. Comparing the matrix blocks in (2) proves both implications: all QOA triple reductions equal `I_{d³}` **iff** equations (15)–(22) hold.

For the stated converse, start with a generalized cube satisfying all these equations, form (1), and choose the `d³` QOA rows

```
phi_{i,j,k} = |i,j,k> tensor psi_{i,j,k}.                  (3)
```

Each is a unit vector by (15); (2) yields (Q) for every three-party set. Their sum is exactly (1). Thus the source's forward and converse existence statements are both proved; no assumption that the input QOA rows were originally of form (3) is needed. Applying (3) after extraction generally produces a **different** QOA row decomposition, which is the distinction exploited in §5.

## 4. Product-valued cubes, and restriction to a square

An ordinary `t`-MOQLC in Definitions 3.3/3.6 is a family `u^s_{ijk} in H`, one QLC for every named physical output `s`, with every line an ONB, every corresponding plane of each pair an orthogonal pair of QLS, and every triple of cubes yielding a `d³`-vector product ONB. For `t>=3`, it is equivalent to a `t`-GMOQLC **whose every cell is fully product across the fixed output parties**:

```
psi_{ijk} = u^1_{ijk} tensor ... tensor u^t_{ijk}.
```

All single-party factors can be taken unit, absorbing an overall phase into one factor. From generalized to ordinary, take diagonal blocks of (16)–(18), (19)–(21), and (22): they are sums of respectively `d`, `d²`, and `d³` normalized rank-one projectors equaling the corresponding identity. A square matrix with those vectors as columns is unitary, so the line, paired-plane, and triple-product sets are ONBs. From ordinary to generalized, the diagonal blocks give these same identities. For the off-diagonal two-address blocks, each summand vanishes because, with the summed address fixed, any two traced-out output cubes have orthogonal superimposed plane entries. For an off-diagonal one-address block, at least one traced-out output cube has orthogonal entries on the line where the kept address varies. Triple-product ONBs give (15), and (22) is the triple-product ONB resolution. This also justifies both directions implicit in Remark 4.7; it does not assume separability for a general cube.

Fix any one address, e.g. `i=i0`. The `d²` cells `psi_{i0,j,k}` satisfy generalized-square Definition 4.2: (15) gives their orthogonality; (17) and (18), with `i=i'=i0`, give the two one-output line identities including cross terms; (20), with `i=i'`, gives the two-output identity. Thus **every** generalized cube yields a generalized square slice. If that particular slice is fully product, it yields an ordinary `t`-MOQLS by the same diagonal-identity argument; full separability of all other slices is not needed for that conclusion. Conversely an arbitrary generalized or ordinary square has not thereby been shown extendible to a cube: a completion must supply the other `d-1` slices and all cross-slice equations. This audit proves no general extension theorem.

## 5. Exact counterexample to a literal one-to-one row correspondence

Use the `d=8`, seven-party classical QOA from §6. For field elements `0,1,alpha`, let `A,B,C` be the three normalized computational product rows of the constant polynomials `0,1,alpha`, respectively; they are mutually orthogonal. Replace only these rows by

```
R1 = ( 2A -  B + 2C)/3,
R2 = ( -A + 2B + 2C)/3,
R3 = ( 2A + 2B -  C)/3.
```

The displayed coefficient matrix is real orthogonal and all its row and column sums are 1. Therefore `R1,R2,R3` are mutually orthonormal unit vectors, also orthogonal to all untouched rows, and `R1+R2+R3=A+B+C`. The new and original arrays both satisfy Definition 4.1 because their complete coherent sums are exactly equal; each gives the same coefficient cube in (1). Yet `R1` has nonzero components along three original orthogonal product rows and is not a phase multiple of any original row. Thus even restricting to orthonormal rows, this is not a row permutation or row-phase change.

For the phase-convention point, replace `R1` by `-R1` while keeping all the same rays. In the total sum, the amplitudes of `A,B,C` become `-1/3, 5/3, -1/3` instead of `1,1,1`. Their output parts are orthogonal, so the reduction on the three original address parties has corresponding diagonal values `1/9,25/9,1/9`, not `1,1,1`; (Q) fails. Thus QOA membership is not determined by the individual row rays without choosing their phases. The finite-field proof of validity of the original array is in §6, not assumed from a source example.

## 6. Exact d=8 entangled-cell construction and source example

Work in `F_8=F_2[alpha]/(alpha³+alpha+1)`. The polynomial has no `F_2` root and is irreducible. Use the seven distinct evaluation points

```
0, 1, alpha, alpha², alpha³, alpha⁴, alpha⁵
= 0, 1, alpha, alpha², alpha+1, alpha²+alpha, alpha²+alpha+1.
```

For every polynomial `f(z)=u+vz+wz²`, let `(a,b,c)=(f(0),f(1),f(alpha))`, and let `L_1(a,b,c),...,L_4(a,b,c)` be its values at the other four points. Lagrange interpolation shows that the coefficient of `a` in every `L_s` is

```
(z_s+1)(z_s+alpha)/alpha != 0.
```

Consequently, at fixed `b,c`, `a -> L_s(a,b,c)` permutes `F_8` for each `s`. The classical unnormalized state is

```
Phi_0 = sum_{a,b,c in F_8} |a,b,c,L_1(a,b,c),...,L_4(a,b,c)>.
```

Any three evaluation coordinates give an invertible 3-by-3 Vandermonde matrix, so every three-symbol tuple appears exactly once. When any three parties are retained, the remaining four distinguish all 512 rows (already any three do), hence the reduction of `Phi_0` is exactly `I_512`, not merely diagonal with the correct trace.

Let `Tr(z)=z+z²+z⁴ in F_2` and `H|a> = 8^(-1/2) sum_x (-1)^Tr(xa)|x>`. The character matrix is unitary: for nonzero `x`, multiplication by `x` is bijective and `Tr(1)=1`, so its character sum vanishes by translation. Apply `H` to the first address party only. This preserves every three-party identity reduction and gives cells

```
psi_{x,b,c} = 1/sqrt(8) sum_{a in F_8} (-1)^Tr(xa)
              |L_1(a,b,c), L_2(a,b,c), L_3(a,b,c), L_4(a,b,c)>.
```

Each cell is normalized. At fixed `x,b,c`, each output coordinate is a permutation of `a`; tracing any other three outputs leaves `I_8/8` on the remaining output. Hence **every cell has Schmidt rank 8 across each physical output vs the other three**, and none is fully product. Fixing `x=0` gives a `4`-GMOQLS(8) whose 64 cells all have this property. Local unitaries on individual output parties, per-cell phases, or permutations of those parties cannot turn these cells into product states. This rigorously falsifies the inference from generalized square/cube existence to a product-valued ordinary array at these fixed parties and this fixed address basis. The inverse Hadamard on the *address* returns the classical seed, so this example does not assert an obstruction for every possible address basis.

For comparison, fixing `a=0` **before** the Hadamard yields four classical Latin squares `L_s(0,b,c)`. Every line is a permutation and each pair of outputs is jointly bijective because each relevant three-evaluation projection, including the fixed `a` coordinate, is invertible. These are a genuine ordinary four-family, but every member's rays come from the same computational ONB. It neither exhibits a nonclassical member nor proves that none can exist.

The article's Example 4.9 gives a separate `d=7` instance: its first three systems are `i,k,i+j+k`, which are bijective addresses, and its four output systems are

```
|i+2j+4k> tensor (1/sqrt(7)) sum_l omega^(i*l)
                    |l+j, l+2j+5k, l>,  omega=exp(2*pi*i/7).
```

At every fixed address the last three-output state has seven orthogonal terms on each side of every single-party cut, so it is GHZ-type entangled and not a product. Its complete 3-uniform condition was also checked exactly, but this selected example is not used to prove the universal proposition.

## 7. Exact bridge to the actual ordinary four-family question

At fixed physical parties there is a direct **square**, not cube, equivalence useful for the target. Let `d=8` and `Omega` be a phase-fixed vector on two address parties and four output parties, with norm squared `d²` and every two-party reduction equal to `I_{d²}`; write `Omega=sum_{j,k}|j,k> tensor psi_{jk}`. The two-address, one-address/one-output, and two-output cases of the same block calculation yield Definition 4.2. If, and only if, every `psi_{jk}` is product across the four fixed outputs, the normalized factors form an ordinary four-MOQLS: diagonal line blocks are rank-one resolutions of `I_d`, and diagonal two-output blocks are rank-one resolutions of `I_{d²}`. Conversely, any ordinary four-family supplies `Omega` by tensoring its four cell vectors. Its two-address reduction is the identity by pair-product orthogonality, its one-address/one-output reductions use line ONBs and vanish off diagonal termwise because another output QLS has orthogonal same-line entries, and its two-output reductions are pair-product ONB resolutions. Canonical rows `|j,k> tensor psi_{jk}` give a QOA `(d²,6,d,2)`.

There is also an exact factorization/nonclassicality test. For each cell define its one-output density matrix `P^s_{jk}`. Since each cell is pure and normalized, it is fully product iff all four `P^s_{jk}` have rank 1. Once this holds, a member `s` is classical in the per-member global-ONB-ray sense iff all `Tr(P^s_{jk} P^s_{j'k'})` belong to `{0,1}`. Indeed the first row is an ONB; binary overlaps force every other ray to coincide with one of its rays. Therefore a genuinely nonclassical four-family is equivalent, in this six-party square representation, to product rank-one reductions in every cell **and** at least one pair of cell rays of one output satisfying

```
0 < Tr(P^s_{jk} P^s_{j'k'}) < 1.
```

This is an exact reformulation, not a construction, no-go theorem, or new equivalence between the original target and arbitrary seven-party QOA/cubes. A cube-derived square is one special source of a two-uniform state; arbitrary square solutions have not been shown to admit a cube extension. No claim is made here about the current literature status, any maximum-family number, or a nonclassical four-family witness.

## 8. Executed exact checks and unresolved scope

`check-exact-v1.py` in this directory, SHA-256 `9d12390ac9d9eacd8b1fbf7c5ffc16afd415336dd7702939fdcb8b9920a12c35`, was written completely before execution. Command: `python3 -B check-exact-v1.py`. It uses only Python's standard library. Actual output:

```
q7 source Example 4.9: 35/35 exact triple reductions = I_343; 2401 distinct support kets, max trace-group=7, pair terms=112847; exact in Z[z]/(Phi_7), including 1/7 amplitude-square
q8 classical seed: 35/35 strength-three projections bijective; at a=0: four Latin squares and 6/6 orthogonal pairs
q8 transformed: 35/35 exact triple reductions = I_512; 4096 distinct support kets, max trace-group=8, pair terms=573440; exact signed integers including 1/8 amplitude-square
q8 fixed-x=0 plane: 64/64 cells mutually orthonormal; 256/256 one-output marginals equal I_8/8 (Schmidt rank 8)
```

The `d=7` computation aggregates every traced-complement pair and compares all matrix entries in the exact cyclotomic basis `1,z,...,z^5` with `z^6+...+z+1=0`; the `d=8` computation aggregates signed integer contributions, including all off-diagonal terms. The q8 field, Vandermonde argument, local-unitary invariance, cell entanglement, row nonuniqueness and general theorem above are also proved symbolically and do not rely on numerical floating-point equality. These are bounded checks, not independent external review.

**Unresolved:** existence or impossibility of a genuinely nonclassical ordinary four-MOQLS8 is not settled; a generalized slice requires the stated cell-product and nonclassical-ray conditions before it answers that question. No arbitrary-square-to-cube completion has been established. No independent external referee or latest-literature/priority survey was performed. The reconstructed Proposition 4.8 needs no genuinely unsupplied external premise beyond the source's Definition 4.1 and standard finite-dimensional tensor/trace arithmetic; the conventional quantum-state-as-ray language needs the phase-fixed-vector qualification above.
