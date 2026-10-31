# info-6 frontier: rank-eight derivative-support floor

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-28T22:33:31-0700**. **UNREVIEWED AUTHOR CANDIDATE**. This is a conditional original-target necessary condition, not an existence witness, unrestricted exclusion, novelty claim, disjoint review, or formal proof. It depends on the unreviewed full-rank quartic support bound and extremal phase theorem pinned below.

## Statement

Let f:F₂⁹→F₂ be balanced, have `T=⊕{x:f(x)=1}≠0`, and satisfy `max|W_f|≤28`. Suppose its even-half polar B has rank eight. Among the 256 unordered pairs `{x,x+T}`, let m be the number on which f has equal values. Then

    m≥80,    equivalently  wt(D_T f)=2(256−m)≤352.                 (1)

In particular, a balanced ternary even half of support 62 with a full-rank quadratic and peak ≤24, constructed and directly checked below, cannot be extended to a function satisfying the full target. This nonextension is a consequence of (1), not a claim that the ternary half is itself an f.

## Proof

Change linear coordinates so `T=(0,…,0,1)` and complement f if necessary so `f(0)=0`. Write `s(y,t)=(-1)^{f(y,t)}` and

    u(y)=(s(y,0)+s(y,1))/2,    v(y)=(s(y,0)−s(y,1))/2.            (2)

These are ternary, have disjoint supports partitioning F₂⁸, and `wt(u)=m`. Balance gives `Σu=0`, so m is even. For `k=W_f/4` on the odd frequency half,

    k(a,1)=½ Σ_y v(y)(−1)^{a·y},
    Σ_a k(a,1)²=64(256−m),    Σ_a k(a,1)=128v(0)∈{0,128}.         (3)

The last assertion uses `s(0,0)=1`: either `u(0)=1,v(0)=0` or `u(0)=0,v(0)=1`. The assumed peak and T≠0 make the odd-half k values belong to `{±1,±3,±5,±7}`. Let `n_j` count odd-half coefficients of magnitude j. Then

    n₁+n₃+n₅+n₇=256,
    8(m−60)=6n₁+5n₃+3n₅.                                        (4)

The second equality is the odd-half energy deficit from the maximum 256·7². In the pinned rank-eight bound, `h=1−P` for `P=1_{|k|∈{1,7}}` satisfies `wt(h)=n₃+n₅≥46` and `wt(h)≡2 (mod 4)`. Equation (4) therefore gives m≥78. If m=78, then `n₃+n₅≤48`; the congruence forces `n₃+n₅=46`, and (4) reduces to `n₃+3n₁=3`. The only possibilities are

    case I:  (n₇,n₅,n₃,n₁)=(210,43,3,0),
    case II: (n₇,n₅,n₃,n₁)=(209,46,0,1).                          (5)

Both have `wt(P)=210`, so the pinned extremal phase theorem applies. Its six possible `(w,c)=(wt(Q), wt(hQ))` pairs are `(136,10),(136,24),(136,26),(120,20),(120,22),(120,36)`. Here `Q=1_{k≡3 mod 4}` on the odd half.

In case I, let `j` be the count of +3 entries. Then `0≤j≤3` and a direct sum by signs gives

    Σ_odd k = 14w−24c−1264+16j.                                  (6)

Indeed the +7 count is `w−c`, the −7 count is `210−w+c`, the +3/−3 counts are `j,3−j`, and the −5/+5 counts are `c−j,43−c+j`. In case II, let `e` be the count of −1 entries; e is 0 or 1, and similarly

    Σ_odd k = 14w−24c−1232−16e.                                  (7)

The complete arithmetic table is:

| w | c | case I possible odd sums | case II possible odd sums |
|---:|---:|---|---|
| 136 | 10 | 400, 416, 432, 448 | 432, 416 |
| 136 | 24 | 64, 80, 96, 112 | 96, 80 |
| 136 | 26 | 16, 32, 48, 64 | 48, 32 |
| 120 | 20 | −64, −48, −32, −16 | −32, −48 |
| 120 | 22 | −112, −96, −80, −64 | −80, −96 |
| 120 | 36 | −448, −432, −416, −400 | −416, −432 |

None is 0 or 128, contradicting (3). Thus m≠78. Since m is even and m≥78, m≥80, proving (1) conditional on the pinned preceding results. ∎

## Controls and limitations

The 85-LF checker recomputes all six table rows by independently building their sign counts and checks the asserted Q weights and intersections. It also constructs an actual eight-variable ternary u with 31 positive, 31 negative and 194 zero values; `Σu=0`, `u(0)=1`, every even-half `k=½ Walsh(u)` is even with `k(0)=0` and `max|k|=6`, and the quadratic `k/2 mod 2` has polar rank eight. Its 256 u and k values are in the result JSON. It has m=62 and 26 half-spectrum zeros. The other ternary half needed for an f is not supplied; (1) forbids a peak≤28 extension if its author-proof dependencies hold.

For a positive near miss to the floor's boundary, the separate ten-zero formal labelled placement in the pinned packet has even-half energy `5120=64·80` and meets its listed mod-8, quartic, phase and scalar-dual filters. It fails 502 nonzero-shift correlations and 479 inverse coordinates and is **not** a Boolean realization. A distinct bounded Z3 search for a specified ten-zero even half returned `unknown` after approximately 12 s; no no-go or result is inferred from that timeout. The six-line written contradiction above, not any UNSAT solver status, is the candidate proof. The witness-or-unrestricted-exclusion gap remains.

## Pins

| File in this directory | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-fullrank-support-floor-check.py` | `b019b03b1b5cb7fc86d0d74843e09a97907e4f88d669ca9ae29d7f13d310ad2e` | 85 |
| `frontier-20261028-fullrank-support-floor-check-result.json` | `5786202aa785762d79e48b69d2f6fb0df4f3ae0fe3a444ffdf2edf86867089c8` | 612 |
| `frontier-20261028-fullrank-extremal-phase-v1.md` | `e12b3a32a3f7f19b9dea35615bbf4c8fbd6ba970d1491ca33f3fc8f4bacc6fd4` | 100 |
| `frontier-20261028-rank-bound-sharpening-v1.md` | `f741e11a0cc0a73e8c094f6c2c74a09f3f902db58100e3dc9e76bf059c109aab` | 60 |
| `frontier-20261028-tenzero-common-placement-v1.md` | `4b587b60028d1344386fccde7db565fb7a6e4a990f715307f60f2e555fcf267f` | 47 |
| `frontier-20261028-tenzero-even-half-search.py` | `ae3125a957d40cd08cc9235b2d4e05c4dd34049d5a1fe3a9a01992c5103f5931` | 52 |
| `frontier-20261028-tenzero-even-half-search-result.json` | `48acd9511904b4e97c1c696826f46ba761916f737d6fa0bb673dbc31d40c9884` | 7 |

**END.**
