# info-6 frontier: rank-eight P=210 exclusion from even energy

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-28T22:57:05-0700**. **UNREVIEWED AUTHOR CANDIDATE**, additive to the immutable 140-LF consolidated extremal theorem pinned below. It is a conditional rank-eight obstruction, not an unrestricted NL242 resolution, independently reviewed proof, novelty claim, or formal verification. The decisive predecessor and the quartic/count caller remain author-only.

## Precise claim

For any balanced f:F₂⁹→F₂ with nonzero support XOR T, `max|W_f|≤28`, and full-rank even-half polar B, the author candidate asserts

    wt(P)≠210, hence wt(P)≤206,                                  (1)

where `P=1_{|W_f|∈{4,28}}` on the odd frequency half. The second conclusion uses the prior unreviewed rank-eight bound `wt(P)≤210` and its congruence `wt(P)≡2 (mod 4)`. Thus the magnitude-28 count is also at most 206 in rank eight. Other ranks and the original witness-or-unrestricted-exclusion gap remain.

More generally, before using the predecessor, the same assumptions imply the following elementary energy bound. If z is the number of zeros of the even-half quadratic q, and m counts agreeing unordered T-pairs, then

    z=120 => m≤106,       z=136 => m≤100.                         (2)

As a further exact conditional corollary, in the still-open rank-eight `wt(P)=206` branch the number of magnitude-28 coefficients must be at least 170 when z=120, or at least 178 when z=136. These lower bounds do not assert the branch exists.

## Proof

Let `k=W_f/4`. On the even frequency half k is even, and by peak≤28 has values only `0,±2,±4,±6`. The quadratic `q=k/2 mod 2` has polar B. Therefore at each q-zero, `k²≤16`, and at each q-one, `k²≤36`. A quadratic on F₂⁸ with nondegenerate polar has z=120 or 136 zeros. With the ternary half u of the predecessor, `wt(u)=m` and even-half Parseval is

    Σ_{a∈T⊥} k(a)² = 64m ≤ 16z+36(256−z).                         (3)

For z=120 the right side is 6,816, giving m≤106.5; for z=136 it is 6,496, giving m≤101.5. Since balance makes m even, (2) follows.

If `wt(P)=210`, the unreviewed consolidated extremal candidate proves `m≥126`. This contradicts (2), so P=210 is impossible at that same written-support scope. Together with the earlier rank-eight bound and congruence, this gives (1). No solver result is used in this contradiction. ∎

For the last corollary put `n_j=#{odd-half |k|=j}`. If `wt(P)=206`, then `n₃+n₅=50` and the predecessor's odd-half energy identity gives

    8(m−60)=6n₁+5n₃+3n₅=150+6n₁+2n₃.                         (4)

Using m≤106 gives n₁≤36, hence `n₇=206−n₁≥170`; using m≤100 gives n₁≤28 and n₇≥178. ∎

## Actual non-target control and evidence

The pinned deterministic control is a **real balanced Boolean function**, with T=256, q-zero count 120, polar rank eight, and m=126, but its even-half Walsh peak is 64 and full peak is 68 (NL=222). It does not satisfy the target peak assumption and is not a target witness. It illustrates why the coefficient bounds in (3) cannot be retained after dropping peak≤28; no claim is made that it has P=210.

The 512×512 direct character-sum verifier and independent FWHT agree on its full Walsh spectrum, balance and peak. A second checker independently computes T and m from its truth table, checks every quadratic second derivative, obtains rank eight by GF(2) elimination, and checks the even Parseval identity. These are same-owner controls, not a disjoint review.

The consolidated extremal packet includes the orbit proof, three complete finite tables, pinned underlying caller, and a deliberately peak-relaxed modular positive control; a reviewer must check that entire dependency chain rather than treating m≥126 as established.

| File in this directory | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-rank8-extremal-union-v1.md` | `dc5d0e916b586bdcee2033224a4d6b15b8959f021204a1f9be09627da94746f1` | 140 | unreviewed decisive predecessor |
| `frontier-20261028-rank-bound-sharpening-v1.md` | `f741e11a0cc0a73e8c094f6c2c74a09f3f902db58100e3dc9e76bf059c109aab` | 60 | unreviewed prior N bound |
| `frontier-20261028-rank8-high-agreement-control.py` | `9e92e0c7cbeac213482096b0fb09a16b32a62edf26c5caa6cf98c9c5fc86aef2` | 72 | control generator |
| `frontier-20261028-rank8-high-agreement-control-candidate.json` | `5012f1d69ef57373d815f924a29ab88778ca457d52779d029ae168953ab83453` | 11 | actual non-target truth table |
| `frontier-20261028-verify.py` | `3eab1464d222b017034ee709fb163fe216047533f4f164342bdd1126e8c4a8ca` | 114 | direct/FWHT verifier |
| `frontier-20261028-rank8-high-agreement-control-audit.json` | `5b2d71185256f75f197d11c83c5f52ebcd5e38c02984062b43354751a2b3d50c` | 600 | spectrum audit |
| `frontier-20261028-rank8-high-agreement-audit.py` | `e6d0695b39a9dd6a2b350c22b963a5a341a74979dd2fc232d7cdbd05127ca4fa` | 38 | independent polar audit |
| `frontier-20261028-rank8-high-agreement-rank-audit.json` | `de35f3b5b87687dc84af89402ea2004d14e2317a72013f34873f41914ef1ce17` | 23 | polar/derivative receipt |

**END.**
