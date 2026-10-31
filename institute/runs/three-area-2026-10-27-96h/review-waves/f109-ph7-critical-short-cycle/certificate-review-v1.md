# Independent review: PH7 critical-ratio Bernstein certificate

Native clock observed immediately before writing: **2026-10-28T19:22:52-0700 PDT**. Reviewer: `PH7BernsteinProofAttack`, same harness. Scope: the E4/E3 reconstruction, D/N discriminant polynomials, complete dyadic covers, and strict positivity on the five-variable positive orthant. This does not independently decide the PH application, the irreducibility import, or novelty.

## Verdict

**0 FATAL / 0 MAJOR / 0 MINOR in the assigned coefficient-and-certificate scope.** Subject to the explicitly stated trusted-computation assumptions below, the exact reconstruction and all-leaf replay support `Dpol>0` and `Npol>0` for every five-tuple of positive real rates. The computed strictness is on the open cube/positive orthant, not on its compactified boundary. This is not a formal/kernel-checked proof, human review, independent-family review, PH7 existence or nonexistence result, or novelty clearance.

## Frozen inputs and execution

The manifest was read first and had SHA-256 `8f1fa208bdb84a0fbbb44c12c9a1ce22af20a9076ec5ec650babb09db0cb4f75`. I read all seven specified mathematical inputs completely in their listed order, including the author code only as text; all full SHA-256 pins matched. The receipt repeats their paths, hashes, byte lengths and LF counts in order, rechecking each from disk. The author certificate pin was `7d3b69a2eee8917e0fcd43adc0b9f973b16b5060c40b3dbbfaab12b51ab85151`. No author code was imported or executed.

- Own standard-library-only code: [`certificate-replay-v1.py`](certificate-replay-v1.py), 381 LF / 16,628 bytes, SHA-256 `7142f9c6f2ef2b5efd1d9b54e301c6f05a7b4ee5d6595e18f82e2bfd5e44902f`.
- Exclusively created machine receipt: [`certificate-receipt-v1.json`](certificate-receipt-v1.json), 165 LF / 5,821 bytes, SHA-256 `98ea699d0fe2ae169d14eaff00226383d419e99c51d1c7ea0252e3af0721468b`.
- Actual command: `python3 -B certificate-replay-v1.py` in this directory; Python 3.14.3, successfully completed and printed `PASS`. Native start `2026-10-28T19:22:13-0700 PDT`, finish `2026-10-28T19:22:15-0700 PDT`. This command computed the result and controls, not an execution of either author program.

## Independent coefficient reconstruction

The replay constructs sparse rational polynomials in the seven variables `u0,...,u4,t,r`, indexed by their exponent tuples, and also performs exact coefficient convolution in `y`. It expands the known target directly as

`y*((y+1)^2+8/9)^2 = y^5+4y^4+(70/9)y^3+(68/9)y^2+(289/81)y`.

Independently it constructs `product_i(y+u_i)*(y^2+t*y+r)`, equates the two leading lower coefficients to eliminate the monic quotient's `p,q`, then extracts the actual `y^4,y^3` residuals. Let `s_j` be the elementary symmetric functions of the five `u_i`. The quotient coefficients are

`p=s1+t-4`, `q=s2+t*s1+r-4p-70/9`.

The replay verifies the resulting residuals are affine in `t,r` and independently checks their six coefficient polynomials against

```
E4 = (s2 - 4s1 + 74/9)t + (s1 - 4)r
     + s3 - 4s2 + (74/9)s1 - 28/3,
E3 = (s3 - (70/9)s1 + 212/9)t + (s2 - 70/9)r
     + s4 - (70/9)s2 + (212/9)s1 - 1007/27.
```

For `E4=a00*t+a01*r+b0` and `E3=a10*t+a11*r+b1`, the independent sparse products construct

```
den = a00*a11 - a01*a10
 tn = a01*b1 - b0*a11
 rn = b0*a10 - a00*b1
  D = 81*den
  N = -19683*(tn^2 - 4*rn*den).
```

Cramer's rule gives `t=tn/den`, `r=rn/den` when `D>0`; then `t^2-4r=-N/(3D^2)`. The coefficient comparison checks all terms, not sampled substitutions. The six sparse coefficient term counts in order `b0,a00,a01,b1,a10,a11` are `26,16,6,21,16,11`.

| Polynomial | Nonzero integer monomials | Individual degrees | Canonical coefficient SHA-256 |
|---|---:|---|---|
| D | 96 | `(2,2,2,2,2)` | `5449296f6d105d2c1303053930dfb69ab16c606d64201b6e36311c6f094c4009` |
| N | 1,753 | `(4,4,4,4,4)` | `7c1ebd087490f5487db2851fb09b90bdd688983ae6929852637e04f55679f69e` |

The digests agree with the pinned certificate. Their canonical serialization is sorted `[exponent-vector, decimal-integer-string]` pairs, encoded as compact JSON. Digest equality binds the independently reconstructed full arrays to the certificate; it is not by itself the positivity argument.

## Cover and strict positivity

The replay parses each path list as an explicit binary trie. It rejects duplicates, nonbinary paths, prefix conflicts, and every internal node missing either child. The root is present, all internal nodes have exactly two children, and every listed leaf is visited. Therefore the listed finite dyadic boxes cover the entire closed cube, with disjoint interiors and possible shared faces; this is a partition up to shared boundaries, not a disjoint partition of closed sets. Bit `0` or `1` chooses the left or right half, with splitting axis `depth mod 5`. Every leaf has depth at least five, hence every coordinate was split at least once.

For `P=D,N`, `d=2,4`, use `Ptilde(x)=P(x/(1-x))*product_i(1-x_i)^d`. Its tensor Bernstein coefficient at index `k` is `[u^k]P/product_i binom(d,k_i)`. Initial positive common integer scales are `32` and `248832`. For one axis the replay uses the closed-form midpoint de Casteljau transforms, multiplying both child grids by the positive factor `2^d`; it records a SHA-256 over every computed leaf path and full integer coefficient array. The row counts below include zero coefficients, not just support.

| Replay measurement | D | N |
|---|---:|---:|
| Leaves / internal nodes | 513 / 512 | 657 / 656 |
| Leaf depth range | 5–10 | 5–15 |
| Integer Bernstein coefficients checked | 124,659 | 2,053,125 |
| Zero coefficients among those | 1,880 | 10,776 |
| Strictly positive global-open-cube leaf corners checked | 3,746 | 6,726 |
| Leaf-array SHA-256 | `87431612ba78d5b3c3ce6c4a1edb39f1ddb63e72cc0994a3b8e3c38e761a4421` | `c2b5c2343db089dca110baaf9e6ccc09ab10f5c5417c4327a0b3e4a0c770c05f` |

All coefficients on every leaf were nonnegative, and each corner of each leaf that lies in the global open cube was strictly positive; each leaf had at least one such corner. The strictness argument also handles points on internal subdivision faces: for an arbitrary `x` in the global open cube, choose any closed leaf containing it. In each coordinate where `x` is a leaf endpoint, choose that same endpoint; it is globally interior. In each coordinate where `x` lies strictly between the leaf endpoints, choose any globally interior endpoint, which exists because that axis has been split. The chosen tensor corner is globally interior, its coefficient is strictly positive, and its Bernstein basis function is strictly positive at `x`. All remaining terms are nonnegative. Thus `Ptilde(x)>0` even at internal faces and corners, and the positive compactification factors give `P(u)>0` for all finite `u_i>0`.

## Controls actually exercised

Each item below ran for **both** D and N unless otherwise noted; each mutation was in memory and rejected for the intended specific reason.

- Remove one path: `MISSING_CHILD`; append a duplicate: `DUPLICATE_PATH`; append a descendant of an existing leaf: `PREFIX_COLLISION`.
- Increment the lexicographically first coefficient, which is the constant term, by one: `COEFFICIENT_DIGEST`. The unaltered constant terms are D `2452` and N `91421104`.
- Replace the entire reconstructed polynomial by its negative: `NEGATIVE_BERNSTEIN_COEFFICIENT` during all-leaf sign checking, rather than merely a digest failure.
- At the compactified global corner `(1,1,1,1,1)`, both root coefficients are exactly zero. A demand for strict positivity there was rejected as `ZERO_BOUNDARY_NOT_STRICT`; this boundary corresponds to infinite rates and is not part of the theorem's open domain.
- At the shared internal corner `(1/2,...,1/2)`, direct sparse compactified evaluation equals every one of the 32 incident leaf evaluations: D `7/64`, N `709/4096`. A further direct non-grid interior point `(1/3,2/5,3/5,4/7,5/8)` matched its leaf evaluation: D `50787/280000`, N `364306486221/768320000000`.
- Degree-2 and degree-4 mixed-sign one-dimensional Bernstein arrays were split and evaluated with exact rationals on **both** children; both matched direct parent evaluation at the corresponding half-coordinate. These specifically control the two de Casteljau orientations and scale.

The receipt records the actual counts, exact control rejections, and both leaf-array hashes. No claim is made that these controls prove the absence of every implementation defect.

## Trust and scope boundaries

The all-leaf conclusion relies on the Python 3.14.3 standard library's arbitrary-precision integers, `Fraction`, combinatorial functions, SHA-256 and JSON parser, as well as the correctness of this reviewer's sparse-polynomial, trie, Bernstein conversion and subdivision implementations. The readable identities, closed-form split formula, strict-positive corner argument, certificate hashes and explicit targeted controls make those dependencies inspectable, but they do not turn this replay into a formal proof or independent hardware/model-family replication. The author supplied the cover paths, which were independently parsed and checked rather than trusted.

The short-cycle application additionally needs its graph/characteristic-coefficient reasoning and the separately named irreducibility/normalization import. This review is not an adoption of those separate arguments. In particular, neither this computation nor the conditional short-cycle restriction proves or excludes any PH7 realization at `z=8/9`, settles the PH minimum, or assesses mathematical novelty.
