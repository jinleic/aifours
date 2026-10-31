# f115 independent finite whole-host transport review

## Disposition and scope

**PASS, finite diagnostic only. FATAL 0, MAJOR 0, MINOR 0 within the checks below. INCONCLUSIVE for the general infinite theorem, its complete written proof, and the canonical-`q` presentation.** The negative nonpure example is outside the candidate's hypotheses and is not a defect in that candidate. This is a same-harness review, not human, independent-model-family, formal/kernel, or novelty clearance. It does not adopt or alter any historical held result.

The construction below independently uses a five-element **free left-regular band**, not the author's tabulated five-element band. It exercises a nonnormal subgroup, a nontrivial band action, both collapsed Rees label maps, and a row gauge of order three outside the subgroup. The source consists of the entire 90-element physical host, not a selected source image. Every one of its 8,100 ordered products and all 8,100 ordered injection comparisons were checked exactly. These finite checks do not prove arbitrary/infinite transport or the actual syntactic-`q` consequence.

## Frozen input coverage and provenance

Manifest `manifest-v1.json` was read first and matched SHA-256 `6580d8208d704cb242e28e58951646d5ada674919b5569340e8252f566390426` (2,855 bytes, 39 LF). All four inputs were verified **before** reading their complete bodies, then read completely in manifest order. Each full hash, byte count and LF count matched:

| # | Input basename under `mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding/` | SHA-256 | bytes / LF |
|---|---|---|---:|
| 1 | `frontier-20261028-pure-actor-finite-band-pushforward-v1.md` | `abdfecbfb03b7931ad8dac0e7912f6c359279fe7afd47662a4f376942b2d9057` | 13,634 / 139 |
| 2 | `frontier-20261028-pure-CS-coinduced-whole-host-v1.md` | `b129099ed4ae481a0d212ec68c5271b91b700757721d8c41d712b55e9755bad2` | 7,225 / 82 |
| 3 | `frontier-20261028-pure-nononto-transport-checker-v1.py` | `dc8caf28977376a30827e736d80429d4c99fb3e0942e9d77ede8a9ceedb28400` | 2,780 / 48 |
| 4 | `frontier-20261028-local-global-coinduction-checker-v1.py` | `3a0d6c2f4dc6001f9e73ece7cf632d10b068f5956b274a73c39ee1e3d3ed8cfc` | 3,058 / 57 |

The independently written program did not import or execute either author's checker. It rereads the four frozen inputs as bytes solely to bind and verify provenance. No randomness, external model, web search, or paid API was used.

## Explicit independent physical host

Write a permutation as its ordered images on `0,1,2`; `gh` means apply `h` first. Let

- `e=(0,1,2)`, `t=(1,0,2)`, `u=(1,2,0)`, `v=(0,2,1)`, `z=(2,1,0)=ut`.
- `G1=S3`, `H={e,t}≅C2`, and `G0=C2={0,1}` with `φ(0)=e`, `φ(1)=t`. Indeed `utu⁻¹=v∉H`, so H is nonnormal; `u` has order three and is not in H.
- `B={ε,a,b,ab,ba}` is the free left-regular band on `a,b`: concatenate words and delete each letter already present. The nontrivial action `α1` swaps `a` and `b`, and `α0` is the identity. The program checks closure, all associativity and idempotence cases, the left-regular identity, both automorphisms, and all local-corner regular-band identities. Its five local corners have cardinalities `5,2,2,1,1`.

The source actor is `D0=M[C2; {0,1,2},{0,1,2};P0]` with rows of `P0` indexed by λ and columns by i:

```text
P0 = [[0,1,1],
      [1,0,0],
      [1,0,0]].
```

The target actor is `D1=M[S3; {0,1},{0,1};P1]`, where

```text
P1 = [[e, z],
      [u⁻¹, t]].
```

Both row and column maps are `(0,0,1)`, so each collapses source labels 0 and 1. The row gauges are `(e,t,u)` and the column gauges are `(e,t,v)`. Thus the actor map is

```text
f(i,g,λ) = (rowmap(i), row_gauge[i] · t^g · col_gauge[λ], colmap(λ)).
```

All nine gauge identities `vλ P1[colmap(λ),rowmap(j)] uj = t^P0[λ,j]` and all 324 actor-product identities were checked. `|D0|=18`, `|f(D0)|=8`, `|D1|=24`; source and target actor associativity were checked on all 5,832 and 13,824 triples, respectively. The program checked idempotence reflection/preservation at **all 18** source actors: the nine source idempotents are exactly `(i,P0[λ,i],λ)`, while the four target idempotents are `(0,e,0)`, `(1,z,0)`, `(0,u,1)`, `(1,t,1)`. Hence this particular f is idempotent-pure even though it is nononto and collapses rows and columns.

### All coinduced functions

Choose left-coset representatives `(e,v,u)`. In the following fixed function-coordinate order `(e,v,t,u,u⁻¹,z)`, the respective `r t^bit` bits are `(0,0,1,0,1,1)`. Define `J(c)(r t^bit)=αbit(c)` and `(γg F)(x)=F(xg)`. The complete computed `J` table is:

| c | e | v | t | u | u⁻¹ | z |
|---|---|---|---|---|---|---|
| ε | ε | ε | ε | ε | ε | ε |
| a | a | a | b | a | b | b |
| b | b | b | a | b | a | a |
| ab | ab | ab | ba | ab | ba | ba |
| ba | ba | ba | ab | ba | ab | ab |

`J` is injective by evaluation at e. The program explicitly checked its 25 band-product equations and all ten H-equivariance equations. It also checked the coordinate equation `(xg)k=x(gk)` for all 216 triples and that every right shift permutes the six coordinates, establishing the shift-action convention on every function in this finite power, not only on the five listed J-values.

The source physical multiplication for `(c,i,g,λ)` and `(d,j,h,μ)` is

```text
w = g XOR P0[λ,j]
(c,i,g,λ) · (d,j,h,μ) = (c · αw(d), i, w XOR h, μ).
```

With `R0={0,1,2}×{0,1,2}` rectangular and the pointwise band `C=B^S3`, the transported element is

```text
Ψ(c,i,g,λ) = ((i,λ), γrow_gauge[i] J(c), f(i,g,λ)).
```

The target band is `R0×C`, of cardinality `9·5^6=140,625`; the entire target physical host has `3,375,000` elements. These sizes follow from the construction; the checker does **not** enumerate all target-host pairs. It computes the 90 source elements, all 90 transported images, and every source product and corresponding target product. `finite-products-v1.json` stores the full source enumeration, 90 images, all actor images, all J-functions, and the full 90×90 product-index table; `Ψ(source_product)=target_product` was checked for each entry. Distinctness was checked for all 8,100 ordered source pairs. The source host was also checked associative on all 729,000 triples. Inspecting the recorded diagonal gives 45 host idempotents and zero mismatches between host idempotence and idempotence of its source-actor projection.

## Targeted negative controls

All host-pair counts below are among the 8,100 ordered pairs; omission collisions are **unordered** distinct source pairs.

| Mutation | Observed intended failure |
|---|---|
| Omit the entire source rectangle from Ψ | 80 collisions. One is `(ε,0,0,0)` versus `(ε,0,1,1)`. |
| Omit only its row factor | 30 collisions, including `(ε,0,0,0)` versus `(ε,1,1,0)`. |
| Omit only its column factor | 30 collisions, including `(ε,0,0,0)` versus `(ε,0,1,1)`. |
| Use left translation `F(gx)` in place of the right shift, both in the gauge image and target action | 4 of 10 H-equivariance checks fail and 1,440 host-product equations fail. For `c=a`, `g=t`, `x=v`, the correct value is `J(a)(vt)=b`, while the left-shift value is `J(a)(tv)=a`. |
| Use the inverse row gauge in Ψ while keeping the correct target action | 1,296 host-product equations fail; first witness indices `(0,30)` in the stored source enumeration. |
| Reverse target action weight from `g P1[λ,j]` to `P1[λ,j] g` | 816 host-product equations fail; first witness indices `(1,30)`. |

The one-sided left-shift mutation is not presented as a valid replacement action: in a nonabelian group its composition convention is reversed. Its purpose is to demonstrate that the actual coinduction convention matters. The inverse-gauge and reversed-weight counts are separate, targeted faults rather than arbitrary exceptions.

### Genuine failure without idempotent purity

Take a separate normalized group actor map `C2→S3`, sending **both** group elements to `e`, and retain the same band B and nontrivial action. This map is not pure: the nonidentity C2 element is not idempotent but maps to `e`. In the source physical host, `x=(ε,1)` has `x²=(ε,0)≠x`. Every element over target identity `e` in **any** band-by-group physical host is idempotent: `(c,e)²=(c·c,e)=(c,e)`. Thus any homomorphism over this nonpure actor map would identify `x` with `x²`, and no such embedding exists. As a concrete finite control, all 20 distinct possible assignments of their B-coordinates in the target identity fiber were rejected. This establishes a real obstruction in this example, not a failure of the pure-map theorem.

## Bound exact run

One invocation of the final independent program was observed:

```text
python3 -B finite-control-v1.py
native start: 2026-10-28T19:37:48-0700 PDT
native end:   2026-10-28T19:37:50-0700 PDT
Python:       /opt/homebrew/opt/python@3.14/bin/python3.14  (3.14.3)
result:       PASS_FINITE_DIAGNOSTIC_ONLY; exit 0
```

Artifacts in this directory:

| Artifact | SHA-256 | bytes / LF |
|---|---|---:|
| `finite-control-v1.py` | `dd5ae47cc5fc4b8d53ce4267221f579b85515a51d483d19037e3be82b4647351` | 15,459 / 349 |
| `finite-products-v1.json` | `26aea3851e87791b20073ecd6fa0c5a8c8b7103ca008c1bdc37d56e79047670d` | 31,627 / 1 |
| `finite-result-v1.json` | `cf05c67e2db7a078832f01f23cc59017c664070d2179dc8b9d19bb0bb4157c93` | 4,464 / 1 |

The receipt binds the manifest, all four frozen source hashes, byte/LF counts, program hash, product-table hash, runtime, clock, counts and controls. The program refuses to overwrite either output.

## Dependencies and limits

For arbitrary groups and actors, the written construction depends on the Rees-coordinate factorization and gauge identity, injection of the local group map from idempotent purity, existence of suitable coset representatives, closure of the locally-regular-band variety under the required products, and the pointwise right-shift action. The stronger onto specialization additionally depends on the local-group map being onto. The actual syntactic-`q` deduction further depends on an existing faithful source host, an onto pure actor, the correct lifting/reflection of idempotence contexts, the purity and completely-simple nature of the resulting quotient, and the actual free-band presentation and its mixed relations. None of these general or presentation-level dependencies is discharged merely by the finite diagnostic. In particular, this example constructs no arbitrary-source host and does not establish canonical-`q` faithfulness, novelty, or an independent-family review.
