# PH7 six-rate Q/H certificate: independent zero-face review

**Scoped verdict: 0 FATAL / 0 MAJOR / 0 MINOR; exact nonnegative-domain certificate PASS.** The two polynomials defined below are strictly positive on every point of `[0,∞)^6`, including every zero-rate face and their intersections. This is a same-harness, independently written exact-arithmetic review of that polynomial/certificate claim only. It is **not** a proof or review of geometric-mean symmetrization, characteristic-coefficient comparison, the PH caller, original-target closure, priority/novelty, human or independent-model-family review, or a formal/kernel verification. The certificate's own graph-scope metadata is narrower than the newer candidate's application; the present verdict concerns the polynomial inequalities, not a change to that graph-scope metadata.

Native clock observed immediately before this review was written: `2026-10-28T21:19:46-0700 PDT`. The successful exact run began at `2026-10-28T21:18:46-0700 PDT` and sampled `2026-10-28T21:18:48-0700 PDT` immediately before writing its receipt. The artifact hash observation at `2026-10-28T21:19:20-0700 PDT` is an upper bound on receipt completion, not an invented creation timestamp.

## Frozen input and reproducible execution

The manifest was read first and its complete bytes hashed: `manifest-v1.json`, 4,473 bytes, 66 LF, SHA-256 `6ddba0f76b0183136dae7cd3cc822f24e1c591342fcc0c88c12dd7accbc41476`. All seven declared inputs were UTF-8 decoded and completely read in manifest order; the certificate JSON was parsed in full and every path subsequently traversed. Full byte length, LF count, trailing LF, and SHA-256 matched the manifest for each input. The engine also rejected duplicate JSON object keys and nonfinite JSON constants. The following table uses the manifest's role names; complete paths are in the receipt.

| Role | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| Prior positive-rate Q/H disposition | 6,488 | 37 | `789b687ad2aab722b405cfb0b2d2a7bdd29aca44bdf29ed6650747367886253f` |
| PH normalization/irreducibility disposition | 6,427 | 31 | `42ae3d996ffb7f46cc5ad72a0d18f3eae665290f8d7901e994ac7776a6b4d281` |
| Mandatory-triangle candidate | 8,157 | 95 | `d2437a46148569e7f43c76853331132a3481c20cff06317de57e538c92348612` |
| Imbalanced-triangle candidate | 4,133 | 40 | `37660f6c71e0de842093db7dd570913846781d9dd14addf4a959659de037fa88` |
| Six-variable certificate | 254,486 | 10,697 | `b2674b8221205230df969c205c0975486c2079202c896f6d4e37f4c6269e87d8` |
| Author replay, read/hash only | 3,631 | 90 | `ac5b069e3d4d5c108b9b9a6e3df12172f5bc360390f92c119a0af58e48116177` |
| Author boundary wrapper, read/hash only | 1,655 | 33 | `03d2853e583ddb5284eb2d5a35a0bae063ab1b104df40350a5283128359ee204` |

I wrote and actually ran `python3 -B certificate-engine-v1.py` in this review directory; it exited successfully and printed `PASS_EXACT_NONNEGATIVE_SIX_RATE_DOMAIN`. It imports neither author nor prior-reviewer code. Its exact integer tensor engine and coefficient reconstruction use only Python standard-library code. Files and post-run SHA-256s:

- [`certificate-engine-v1.py`](certificate-engine-v1.py), 19,195 bytes, `7bec8fbcd780fc678e5293c17fbc84a15d1c15306c67faf0c990f55c2d8b56d1`.
- [`certificate-result-v1.json`](certificate-result-v1.json), 9,077 bytes, `15cd3b11ae082168b11e3656b1f509a06c210fe009f848b5c60fbdd65b846e21`. It records the input bindings, depth distributions, all counts, control reasons and hashes, exact positive controls, and execution clocks.

## Independent elementary-symmetric reconstruction

For six nonnegative rates `u_1,…,u_6`, let `f_k` be their degree-`k` elementary symmetric polynomial and let `x` be a seventh rate. The seven-rate functions satisfy `e_k=f_k+x f_{k-1}`, where `f_0=1`. From the displayed elimination system,

```
E4 = e3 - 4 e2 + (74/9)e1 - 28/3 = A x + B,
E3 = e4 - (70/9)e2 + (212/9)e1 - 1007/27 = h0 + h1 x,
q  = e2 - 4 e1 + 74/9 = A + (f1-4)x,

A  = f2 - 4 f1 + 74/9,
B  = f3 - 4 f2 + (74/9)f1 - 28/3,
h0 = f4 - (70/9)f2 + (212/9)f1 - 1007/27,
h1 = f3 - (70/9)f1 + 212/9.
```

Thus, under `E4=0` and `A≠0`, `Aq=A²-(f1-4)B` and `A E3=h0 A-h1 B`; equivalently `q=Qpol/(81A)` and `E3=-Hpol/(243A)` for

```
Qpol = 81[A²-(f1-4)B],    Hpol = -243[h0 A-h1 B].
```

The executable reconstructs the `f_k` from the product recurrence `∏(1+t u_i)` and performs integer polynomial convolution. Its denominator-free expressions, independently obtained from these definitions, are

```
A9=9f2-36f1+74,       B9=9f3-36f2+74f1-84,
h027=27f4-210f2+636f1-1007,  h19=9f3-70f1+212,
Qpol=A9²-9(f1-4)B9,  Hpol=3h19 B9-h027 A9.
```

The reconstructed nonzero monomials are sorted lexicographically by their six exponent tuples and serialized as compact JSON rows `[exponent-list, decimal-coefficient-string]`. The resulting SHA-256s equal the certificate's claimed digests exactly:

| Polynomial | Terms | Degree in each variable | Canonical coefficient SHA-256 |
|---|---:|---|---|
| Qpol | 168 | `(2,2,2,2,2,2)` | `2e26d6364f4682fc2578d8b90ef4350dfb84736a51ce453241bb68138c29658b` |
| Hpol | 435 | `(2,2,2,2,2,2)` | `9453ccad0fb8ace79ac98b59e9ae4433a48aad33c6be315af0da0f85eb3f6cc2` |

The asserted elimination formulas are conditional on `E4=0`; the positivity claim itself is unconditional on all six finite nonnegative rates. In particular, positivity also rules out simultaneous `A=B=0`. No conclusion about whether the seven-rate spectral premises actually hold is made here.

## Full partition, tensor conventions, and exhaustive result

Put `t_i=u_i/(1+u_i)` and define

```
F_P(t) = ∏_i(1-t_i)² P(t_1/(1-t_1),…,t_6/(1-t_6)).
```

For either reconstructed polynomial `P=∑_a c_a u^a`, every exponent `a_i` is at most 2. Therefore, in the degree-two tensor Bernstein basis, the root coefficient at multi-index `a` is exactly `c_a/∏_i binom(2,a_i)`. The engine stores it multiplied by `64=2^6`, which clears every denominator. At path depth `d`, the split axis is exactly `d mod 6`, with `0` the lower half and `1` the upper half. For an axis-wise Bernstein triple `(a,b,c)` already in the current integer scale, the left and right child triples are

```
(4a, 2(a+b), a+2b+c),  (a+2b+c, 2(b+c), 4c).
```

Consequently each leaf's integers equal its true local tensor Bernstein coefficients multiplied by the strictly positive scale `64·4^d`. There is no floating-point arithmetic. The engine strictly checks binary paths, rejects duplicates and ancestor/descendant collisions, and verifies that each nonleaf has both children. This establishes a finite, complete prefix tree whose closed dyadic boxes cover the full closed cube; overlaps occur only on shared faces. Each leaf has depth at least six and every coordinate has been split at least once.

All `3^6=729` coefficients on **every** leaf were checked nonnegative, and every leaf corner whose six global coordinates are all `<1` was checked strictly positive. Counts below are corner incidences, not deduplicated global points; the receipt also records depth histograms. All 64 possible exact zero-coordinate masks occur among the checked corners for **each** polynomial.

| Check | Qpol | Hpol |
|---|---:|---:|
| Leaves | 5,332 | 5,334 |
| Internal nodes | 5,331 | 5,333 |
| Nonnegative integer Bernstein coefficients | 3,887,028 | 3,888,486 |
| Strictly positive finite corners, total | 289,883 | 236,463 |
| …with 0 zero coordinates | 230,864 | 190,246 |
| …with 1 zero coordinate | 43,184 | 31,502 |
| …with 2 zero coordinates | 12,606 | 11,752 |
| …with 3 zero coordinates | 2,844 | 2,608 |
| …with 4 zero coordinates | 358 | 330 |
| …with 5 zero coordinates | 26 | 24 |
| …with 6 zero coordinates | 1 | 1 |

Thus the actual run checked **10,666 leaves, 7,775,514 coefficients, and 526,346 finite corner incidences**, including **105,236 incidences on one or more zero-coordinate faces**.

## Why finite corners cover every finite nonnegative point

Let `t∈[0,1)^6`. Completeness of the prefix tree puts `t` in at least one closed leaf box, including when it lies on one or several internal split faces. In that leaf, write its local coordinates as `z_i∈[0,1]`. Independently in each direction, choose the lower corner if `z_i<1`, and the upper corner if `z_i=1`. The corresponding degree-two Bernstein factor is `(1-z_i)^2>0` in the first case and `z_i²=1` in the second. The chosen lower endpoint is always `<1`; a chosen upper endpoint equals `t_i` and is also `<1`. Hence the resulting six-dimensional corner is one of the strictly positive finite corners actually checked. If some `t_i=0`, its chosen lower endpoint is exactly zero; the argument works unchanged for any number of zeros. The product of the six selected basis factors and the corresponding corner coefficient is strictly positive, while every other Bernstein term is nonnegative. Therefore `F_P(t)>0` on all of `[0,1)^6`.

The compactification is a bijection from `[0,∞)^6` to `[0,1)^6`, and `∏(1-t_i)^2` is strictly positive there, so `P(u)>0` for every finite nonnegative six-rate vector. No point with any `t_i=1` is asserted: such a coordinate represents an infinite rate, outside the domain, and the audit deliberately does not demand positivity at corners with coordinate 1.

## Actually run positive and intended-reason negative controls

- Exact positive boundary controls evaluated both original polynomials directly and independently evaluated the selected leaf's Bernstein tensor, comparing the two after compactification. At `(0,0,0,0,0,0)`, `Qpol=2452` and `Hpol=21094`. At `(0,1,0,2,0,3)`, `Qpol=1525` and `Hpol=13141`; the compactified values are respectively `1525/576` and `13141/576` at `(0,1/2,0,2/3,0,3/4)`. The latter also lies on internal dyadic split faces. All four values are strictly positive.
- Removing Q leaf `0000000` was rejected as `missing-child: 000000`; duplicating it was rejected as `duplicate-leaf: 0000000`; inserting its ancestor was rejected as `prefix-collision: 000000`. The receipt hashes the original and in-memory mutated path arrays.
- An in-memory **leaf-tensor-only** mutation changed the Q origin-corner integer on leaf `0000000` from `2571108352` to `0`, leaving every other coefficient unchanged, all coefficients nonnegative, and its strictly positive open-cube corner unchanged. The finite-boundary predicate rejected `nonpositive-finite-corner: 0000000:zero-mask=63`, demonstrating that an open-cube-only check would not catch this zero-face failure. This is a deliberate certificate-data corruption, not a claim that a nonzero polynomial can differ only on a boundary face. The receipt records the original and mutated tensor hashes.
- The exact domain predicate accepted the boundary examples and rejected both `t_1=1` and `t_1=-1/100` for the intended `domain-not-finite-nonnegative` reason.

These controls exercise the checker but do not replace the exhaustive leaf audit or the written coverage proof. Exactness relies on the stated Python integer, JSON, and SHA-256 semantics and on the reviewed executable; shared certificate data and same-harness execution are not independent-family or formal verification.
