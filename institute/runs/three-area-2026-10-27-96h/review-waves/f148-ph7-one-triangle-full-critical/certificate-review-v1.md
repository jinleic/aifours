# PH7 one-triangle: exact coefficient and certificate review

**Scoped result: 0 FATAL / 0 MAJOR / 0 MINOR for the stated coefficient-equation-to-positivity certificate.** The independently written exact calculation reconstructed the complete cubic, all four of its theta-Bernstein coefficients, all four specified five-rate polynomials, and every one of the 2,311 claimed cover leaves. It found matching canonical coefficient hashes, counts, and individual degrees; complete prefix-free covers; nonnegative leaf coefficients; and positive global-open-cube corners. The inference below is conditional on the stated actual coefficient equations and on positive rates. This review does **not** adopt a graph theorem, the PH caller, any global PH7 exclusion, or novelty/priority.

The implementation was written after reading all assigned inputs, including both author checkers: it was **not blind**. Neither author checker was imported or executed. This is an independent implementation in the same harness, not a human, independent-family, formal/kernel, or publication/novelty verification.

## Frozen inputs and execution

Manifest `manifest-v1.json`: SHA-256 `a30381bbdf9a0a8722122243450e9ee608f7f197948ecef30ee333fb38496f8f`, 3,674 bytes, 52 LF. Every listed text input was read completely in manifest order; the complete certificate JSON was parsed with duplicate keys rejected, and every path was processed. All five pinned SHA-256/byte/LF triples matched, and all five files ended in LF:

| Input, in manifest order | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `math-1-ph7-global-irreducibility-eight-edges-parent-v1.md` | `42ae3d996ffb7f46cc5ad72a0d18f3eae665290f8d7901e994ac7776a6b4d281` | 6,427 | 31 |
| `frontier-20261028-ph7-one-triangle-full-critical-exclusion-v1.md` | `2e30b352597880b78bfc59baa3adead91e4d4f0f1717a8cf7f684cee0a92decc` | 7,612 | 102 |
| `frontier-20261028-ph7-one-triangle-full-critical-check.py` | `dd323a51986972808cdcc209bbc2df58b81214072c2ec760480546c04996a6d3` | 4,147 | 77 |
| `frontier-20261028-ph7-one-triangle-full-critical-certificate.json` | `d1195a6f0099d105eb34e5a6acbeb1fec3d81c333658af7a3c8b2ea5ac79f2c9` | 51,575 | 2,377 |
| `frontier-20261028-ph7-one-triangle-full-critical-integer-replay.py` | `7c20fce389e2b87f4e4df3d9ac31f33bb62b40e8fcd19cb3e53f982fc13b7536` | 5,483 | 128 |

Actual run: `certificate-exact-check-v1.py`, SHA-256 `290f72c0702cfd5d837bda9c789a457a5f389dda4b3de53c8a88168e6a0bd598`; Python 3.14.3 and NumPy 2.4.3. Start `2026-10-28T21:19:26-07:00`, finish `2026-10-28T21:19:44-07:00`, monotonic elapsed **18.615 s**, with a 600 s wall-clock bound. Receipt `certificate-results-v1.json`, SHA-256 `80b6b70224f293f411aaaf186f2881418f503dfa7f1b56fda56f4023bb053327`, contains input pins, individual results, clocks, and control outcomes. NumPy arrays use `dtype=object` and Python arbitrary-precision integer operations, not floating point or fixed-width arithmetic.

A supplemental execution of the same independently written engine recorded every theta-power and theta-Bernstein coefficient, including the otherwise unpinned `b2`: `certificate-cubic-coefficients-v1.json`, SHA-256 `04f2afb222f07823777e23f2070b91cb9099117718a1bbe8eeff418a72e69052`, start `2026-10-28T21:20:33-07:00`, finish `2026-10-28T21:20:34-07:00`, elapsed 1.241 s. The engine source hash was checked before that execution; it did not import an author checker.

## Reconstruction from the actual equations

Let `s1,...,s4` be the elementary symmetric functions of the five positive rates, `h=u1*u2*u3`, `O=u4+u5`, and `w=h*theta`. The displayed actual equations are

```text
p = s1+t-4,
q = s2+t*s1+r-4*p-70/9,
E4 = s3+t*s2+r*s1-w-[4*q+(70/9)*p+68/9] = 0,
E3 = s4+t*s3+r*s2-w*(O+t)-[(70/9)*q+(68/9)*p+289/81] = 0.
```

The constants are indeed those of `y*((y+1)^2+8/9)^2`: the coefficients after `y^5+4*y^4` are `(70/9)*y^3+(68/9)*y^2+(289/81)*y`. To reconstruct, define integer-polynomial quantities

```text
A  = 9*s2-36*s1+74;       B  = s1-4;
D0 = 9*s3-70*B-68;        C0 = D0-4*A;
E  = 9*s2-70;             F0 = 81*s4-70*A-612*B-289.
```

Then `E4=(A/9)*t+B*r+(C0-9*h*theta)/9` and `E3=((D0-9*h*theta)/9)*t+(E/9)*r+(F0-81*h*O*theta)/81`. For the Cramer quantities in the candidate,

```text
den = (Delta0+Delta1*theta)/81,
tn  = (T0+T1*theta)/81,
rn  = (R0+R1*theta+R2*theta^2)/729,

Delta0=A*E-9*B*D0;                 Delta1=81*B*h;
T0=B*F0-C0*E;                      T1=9*h*(E-9*B*O);
R0=9*C0*D0-A*F0;                   R1=81*h*(A*O-C0-D0);
R2=729*h^2.
```

Thus `N=-19683*(tn^2-4*rn*den)=sum(nj*theta^j,j=0..3)`, exactly, with

```text
n0=(-9*T0^2+4*R0*Delta0)/3,
n1=(-18*T0*T1+4*(R0*Delta1+R1*Delta0))/3,
n2=(-9*T1^2+4*(R1*Delta1+R2*Delta0))/3,
n3=4*R2*Delta1/3 = 78732*B*h^3.
```

These divisions were checked coefficientwise exact. This is a genuine cubic polynomial symbolically, though it can have lower degree at special rate values. Its cubic Bernstein coefficients are

```text
b0=n0;  b1=n0+n1/3;  b2=n0+(2*n1+n2)/3;  b3=n0+n1+n2+n3.
G=4*b1*b3-3*b2^2.
```

All coefficients were explicitly constructed as sparse integer polynomials. `b2` has 1,747 terms, individual degrees `[4,4,4,4,4]`, and canonical SHA-256 `638eb1e3e8faec946a588334f3876e3c352a6baecfeebc86ae0ee72d12176079`; the input certificate does not separately pin `b2`. The supplement records `n0`–`n3` and all `b0`–`b3`, including hashes and degrees. In addition to the symbolic construction, six rational controls at two five-rate tuples and `theta=0,1/3,1` compared the original equations, their linear coefficients/Cramer numerator, the cubic, and its Bernstein form exactly.

## Complete coefficient and leaf comparison

Canonical hash means SHA-256 of compact JSON containing lexicographically sorted rows `[five-exponent-list, decimal-integer-coefficient-string]` with no zero coefficients. All four counts, five individual degrees, and hashes below matched the pinned certificate exactly.

| Polynomial | Terms | Individual degrees | Canonical coefficient SHA-256 | Leaves | Depths | Leaf coefficients | Open corners |
|---|---:|---|---|---:|---|---:|---:|
| `b0` | 1,753 | `[4,4,4,4,4]` | `7c1ebd087490f5487db2851fb09b90bdd688983ae6929852637e04f55679f69e` | 657 | 5–15 | 2,053,125 | 6,726 |
| `b1` | 1,753 | `[4,4,4,4,4]` | `88dcb1549c2e21e686249ca8a790851c0412f9a0038900f5d352a2c71c2f24c7` | 567 | 5–10 | 1,771,875 | 3,846 |
| `b3` | 1,717 | `[4,4,4,4,4]` | `35f6c146f349a4a49a1561e3eb497f4a91f5cf5e92e6d28776847656b096072e` | 522 | 5–10 | 1,631,250 | 3,216 |
| `G` | 31,422 | `[8,8,8,8,8]` | `e6231a6ae92b5c6366ecf3e312f0b8889354990b23cb53755a3ae2ee1d360d07` | 565 | 5–11 | 33,362,685 | 3,846 |
| **Total** | | | | **2,311** | | **38,818,935** | **17,634** |

For every record, a binary trie rejected duplicate/prefix-overlapping paths and required both children at every non-leaf. Every leaf was reached exactly once; all recorded paths had depth at least five. Bits `0` and `1` select the left and right dyadic halves, respectively. At zero-based path depth `m`, the split axis is `m mod 5`. Consequently every coordinate was split at least once on every leaf.

For `P(u)=sum_k a_k*u^k` and individual degrees `d_i`, the compactified polynomial is

```text
F(x) = product_i (1-x_i)^d_i * P(x_1/(1-x_1),...,x_5/(1-x_5)).
```

Its root tensor Bernstein coefficient at multi-index `k` is `a_k/product_i binom(d_i,k_i)`. The root arrays multiply these by the positive common integer scale `product_i lcm_j binom(d_i,j)`: `248832` for degrees `[4]*5`, and `1721036800000` for `[8]*5`. At a midpoint split of degree `d`, a line of current integer coefficients `B_k` is transformed by the exact formulas

```text
Left_j  = 2^(d-j) * sum_(k=0)^j     binom(j,k)   B_k,
Right_j = 2^j     * sum_(k=0)^(d-j) binom(d-j,k) B_(j+k).
```

Both children therefore retain the actual Bernstein coefficients times one common, strictly positive factor `2^d` per split. The check examined **every** tensor coefficient on **every** leaf and found it nonnegative. It examined **every** leaf corner lying in the global open cube and found its corresponding corner coefficient strictly positive; the final two table columns count these exact checks.

## Strict positivity and dependencies

The compactification is a bijection from positive rates to the open five-cube, and its clearing factor is strictly positive there. For any open-cube point and a closed dyadic leaf containing it, each coordinate interval has at least one endpoint in the global open interval. If the point is at a leaf endpoint, that endpoint is itself globally interior; otherwise either endpoint has positive local Bernstein weight and at least one is globally interior. Choosing such endpoints coordinatewise gives a global-open leaf corner whose tensor basis weight at the point is strictly positive. Its coefficient is strictly positive, and all other coefficients are nonnegative. Hence `F`, and thus the original polynomial, is strictly positive at that point, including points on internal subdivision boundaries. This establishes `b0>0`, `b1>0`, `b3>0`, and `G>0` for all five positive rates, not just sampled boxes.

The symmetric matrix `[[3*b1,3*b2/2],[3*b2/2,b3]]` has positive first principal minor and determinant `(3/4)*G>0`; its quadratic form on `(1-theta,theta)` is therefore strictly positive. Together with `b0>0`, the identity

```text
N(theta)=b0*(1-theta)^3
         +theta*(3*b1*(1-theta)^2+3*b2*theta*(1-theta)+b3*theta^2)
```

implies `N(theta)>0` for all `theta in [0,1]`, endpoints included. If the stated two equations hold for real `t,r` and `den!=0`, Cramer's rule gives `t=tn/den`, `r=rn/den`, and `t^2-4*r=-N/(19683*den^2)<0`; if moreover `t=v1+v2`, `r=v1*v2` for real `v1,v2`, this contradicts `(v1-v2)^2>=0`. If `den=0`, the very definition gives `N=-19683*tn^2<=0`, contradicting positivity without dividing. The applicability of the actual equations, `theta` bound, and real outside rates to a graph or PH representation is outside this certificate review.

## Executed controls

All failures below were caught by the named intended reason, not merely by some exception; the receipt gives each one separately.

* Replacing the equation's `K=70/9` by `71/9`, and separately changing one exact `b0` coefficient, each produced `COEFFICIENT_HASH`.
* Removing one actual `b0` leaf produced `COVER_MISSING_BRANCH`.
* Replacing theta-domain metadata by `[0,2]` produced `DOMAIN_THETA`; actually substituting `theta=2*tau` produced the expected `COEFFICIENT_HASH` mismatch for `b1`.
* Replacing z metadata by `1` produced `DOMAIN_Z`; independently reconstructing the equations at `z=1` produced the expected `COEFFICIENT_HASH` mismatch for `b0`.
* A genuine known-positive polynomial `1+sum_i u_i^2` on the entire positive five-rate domain passed a complete 32-leaf cover, 7,776 nonnegative tensor coefficients, and 32 strict open-corner checks. The negative polynomial `-1` failed with `NEGATIVE_BERNSTEIN_COEFFICIENT`; the zero polynomial passed nonnegativity but failed the strictness check with `OPEN_CORNER_NOT_POSITIVE`.

The controls exercise the targeted failure modes but do not replace the exact derivation, the leafwise sign checks, or the written positivity inference above.
