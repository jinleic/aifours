# info-6: written four-zero kernel-pairing certificate

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing: **2026-10-28T21:55:41-0700 PDT**. **UNREVIEWED AUTHOR CANDIDATE, NOT A PARENT DISPOSITION.** This packet supplies (i) the exact pairing relaxation and its original-object soundness, (ii) a short human-checkable written contradiction independent of solver UNSAT, and (iii) an independently checked positive near-miss. It proposes exclusion of the **exactly-four-Walsh-zero subcase only**; it does not exclude balanced peak≤28 functions with six or more zeros, solve the unrestricted target, claim novelty, or claim disjoint/human/formal verification.

## 1. Precise conditional claim and prerequisites

**Author candidate.** No balanced Boolean function `f:F₂⁹→{0,1}` with `max_a|W_f(a)|≤28` has exactly four Walsh zeros. Equivalently, within this peak≤28 setting, the four-zero branch would be excluded if the written dependencies and this certificate pass the required review. The original balanced NL242 witness-or-unrestricted-exclusion question remains open.

The same-harness parent disposition `info-6-four-zero-rank6-radical-parent-v1.md`, SHA-256 `12efd10b4a9de2ac70cd49541e36e6a0c5df6bd4deecbb74e085c2eb48795dc3`, 31 LF, establishes **under T≠0** that four zeros are the rank-six polar radical R and that `z=|{q=0}|` is 112 or 144. It carries reviewer minors M1–M4 and does not adopt the later phase work. For the original target, T≠0 is separately parent-supported in `info-6-support-xor-peak-multiplicity-parent-v1.md`, SHA-256 `600bfca7bc17013e7587015c7601d21bd69a4dbec03736a7d6ef3719dc89c1b9`, 27 LF, with its mandatory coupled-count correction. A self-contained alternative T=0 contradiction is also in §2 of the consolidated author packet.

The even-fiber λ theorem used below is **not yet parent-adopted**. Its full one-support/mod-8 proof, quadratic vanishing lemma, exact Boolean caller and f131 geometry are written in `frontier-20261028-fourzero-phase-consolidated-v1.md`, SHA-256 `8c6afc0d19a9707089c5aebf1240f21ef69b1418a2c7009fcaa650712fc5707a`, 154 LF. The present proof uses that λ theorem, but does **not** use the unequal-phase theorem, the finite mod-8 census, any prior histogram elimination, or Z3's verdict as a premise. The separate histogram-specific `C(r₀)≥2016` candidate remains unchanged.

## 2. Soundness: from an actual four-zero target to the pair system

Suppose for contradiction that such an f exists. Write `k=W_f/4`, `K=T^⊥`, `q=k/2 mod2` on K, and let the odd-half quadratic be `Q=(k−1)/2 mod2`. The f131 reduction gives R=Z, dim R=2, rank(q)=6 and `z=|{q=0}|∈{112,144}`. The full Boolean caller is

    C(b)=Σ_a k(a)k(a+b)=16,384·1_{b=0};       Σ_a k(a)²=16,384.             (2)

The reviewed scope has not established the later mod-8 phase; the consolidated author proof supplies a linear λ:R→F₂ with `k(a+r)≡k(a)+4λ(r)q(a) (mod8)` for a∈K. The radical part ρ of Q is also linear. Input translation multiplies k(a) by `(−1)^{a·t}`, leaves T, q and the zero plane unchanged, and replaces ρ by `ρ+(r↦r·t)`. Every R-character is realized by a translation, so we may work with an actual translated target having **ρ=0**. Its own λ exists by the same four-zero theorem. No nonzero-λ assumption is needed: a linear map from a two-plane to F₂ always has a nonzero kernel element r₀.

Then λ(r₀)=ρ(r₀)=0. Pair the 512 frequencies by a↔a+r₀. The two all-zero pairs lie in R. The other pairs have exactly these domains:

- even q-zero: `{−4,4}` in either order; there are `(z−4)/2` pairs;
- even q-one: one pair lies in `{−6,2}` or in its negative `{−2,6}`; there are `(256−z)/2` pairs, because (10) of the consolidated packet makes k mod8 equal at the two endpoints;
- odd: one pair lies in `{−7,−3,1,5}` or in its negative `{−5,−1,3,7}`; there are 128 pairs, because ρ(r₀)=0 makes Q equal at the endpoints.

All domains follow from |k|≤7 and the parity and mod-4 definitions; no sign distribution or selected histogram is assumed. For a pair (x,y), set `e=x²+y²`, `c=xy`; for an odd pair let p=1 exactly when one endpoint is peak/unit (`|k|∈{1,7}`) and the other is not. For even pairs set p=0. Equation (2) gives

    Σ_pairs e=16,384,       Σ_pairs c=C(r₀)/2=0.                             (3)

It remains to show the total odd crossing-pair count d is 0,64 or128. Choose a₀ outside K and define on K

    g(x)=k(x)/2 mod4,       u(x)=(k(a₀+x)−1)/2 mod4,
    P(x)=1_{u(x)∈{0,3}}=1_{|k(a₀+x)|∈{1,7}}.

The phase conditions give `D_{r₀}g=0 mod4` and `D_{r₀}u` even. For M the one-support, let `m(x)=#{v∈M:a₀·v=x·v=1}`. The integer parity identity gives

    u(x)−g(x) ≡ (k(a₀)−1)/2 − m(x) (mod4).                                  (4)

As a function of x, m modulo four has only linear terms and even quadratic terms; equivalently every third additive difference vanishes modulo four. Since its r₀-derivative is even, half that derivative has vanishing second differences modulo two and is affine. Adding 2 modulo four toggles P, so **D_{r₀}P is affine**. An affine Boolean function on the eight-dimensional odd half has weight 0,128 or256. Each crossing pair contributes two points to this weight, so

    d=Σ_odd pairs p ∈ {0,64,128}.                                             (5)

This proves that every actual target maps to the relaxation used below. The direction r₀, common q, Q, phase functions and pairings all refer to **one same translated original f**; the proof does not assemble independent marginal models.

## 3. Human-checkable contradiction

For the pair types above the following exact pointwise bounds hold. Q's other odd class is the negative of the displayed class, so e, c and p are unchanged.

| Pair class | Allowed unordered values | If p=0: `7e−6c` | Always: `3e−2c−96p` | If p=1: `7e+2c` |
|---|---|---:|---:|---:|
| even q-zero | `(−4,−4)`, `(−4,4)`, `(4,4)` | ≤320 | ≤128 | ≤256 |
| even q-one | `(−6,−6)`, `(−6,2)`, `(2,2)`, or negatives | ≤352 | ≤144 | ≤576 |
| odd Q-class | unordered pairs from `{−7,−3,1,5}`, or negatives | ≤392 | ≤196 | ≤448 |

The even entries have p=0 in all cases, so the first and last columns apply to them regardless of the odd crossing case. For transparency, the ten odd Q-class pairs give the following values; a dash is a deliberately inapplicable branch, not an omitted pair:

| Odd pair | p | `7e−6c` if p=0 | `3e−2c−96p` | `7e+2c` if p=1 |
|---|---:|---:|---:|---:|
| (−7,−7) | 0 | 392 | 196 | — |
| (−7,−3) | 1 | — | 36 | 448 |
| (−7,1) | 0 | 392 | 164 | — |
| (−7,5) | 1 | — | 196 | 448 |
| (−3,−3) | 0 | 72 | 36 | — |
| (−3,1) | 1 | — | −60 | 64 |
| (−3,5) | 0 | 328 | 132 | — |
| (1,1) | 0 | 8 | 4 | — |
| (1,5) | 1 | — | −28 | 192 |
| (5,5) | 0 | 200 | 100 | — |

Let `n₀=(z−4)/2`, `n₁=(256−z)/2`, and n₂=128. The zero pairs contribute zero. Using (3):

- If d=0, all odd pairs have p=0. Summing the first inequality would require `7·16,384≤320n₀+352n₁+392·128`.
- If d=64, summing the middle inequality would require `3·16,384−96·64≤128n₀+144n₁+196·128`.
- If d=128, all odd pairs have p=1. Summing the last inequality would require `7·16,384≤256n₀+576n₁+448·128`.

Every required inequality is false by the following positive, exact integer margins (left minus right):

| z | d=0 | d=64 | d=128 |
|---:|---:|---:|---:|
| 112 | 21,888 | 640 | 2,048 |
| 144 | 22,400 | 896 | 7,168 |

Thus none of the three affine-derivative cases is possible. This completes the **written author proof candidate** of the four-zero subcase exclusion, subject to independent review of every stated dependency. ∎

## 4. Intended-reason positive control

The original full integer pairing model returned Z3 UNSAT, but that status is **not** the proof above. To check non-vacuity, a separate run changed **only** its final crossing constraint from `{0,64,128}` to 72. It returned SAT, and an independently written checker directly verified the following explicit formal pairing multiset:

| Group | Unordered pair × multiplicity |
|---|---|
| even q-zero | (−4,4)×54 |
| even g=1 | (−6,−6)×10; (−6,2)×26 |
| even g=3 | (−2,6)×10; (6,6)×26 |
| odd Q=0 | (−7,−7)×25; (−7,1)×1; (−7,5)×46 |
| odd Q=1 | (−5,7)×26; (−1,7)×3; (7,7)×27 |

Add two zero-zero radical pairs. The control has z=112, odd Q weight 112, P weight 184, 180 peaks, `Σe=16,384`, `Σc=0`, and crossing **72**; the checker also verifies the original solver's other scalar/rank/phase conditions and all 257 nonnegative integral dual coefficients. Crossing 72 is deliberately **not** an affine derivative possibility, so this is an intended-reason formal near-miss, not a labeled spectrum, Boolean function, or target witness. The full pairwise checker exhausts the finite pair domains, verifies all six positive margins and rejects a one-unit tightening of every displayed maximum.

## 5. Exact evidence and review boundary

| File | SHA-256 | LF | Role |
|---|---|---:|---|
| `frontier-20261028-fourzero-phase-consolidated-v1.md` | `8c6afc0d19a9707089c5aebf1240f21ef69b1418a2c7009fcaa650712fc5707a` | 154 | Written Boolean/λ foundations; phase portion unreviewed |
| `frontier-20261028-kernel-direction-histogram-bound-v1.md` | `4ab21bf6fd28a430de542dee6bbe90f4038253a3feaa395cdbf9b6c4438fccc3` | 57 | Separate histogram-specific C≥2016 candidate |
| `frontier-20261028-fourzero-kernel-pairing.py` | `999a33bd73e705a7197bc0f5adb4939125ff8687fd76f52cf736d0f2d8e16111` | 68 | Original full integer relaxation |
| `frontier-20261028-fourzero-kernel-pairing-result.json` | `f0051bf8e7cb4573c82b9b53fb9b62ad4e4f1d39fbd2c75fb2a9b64aad86451c` | 5 | Z3 UNSAT observation, **not proof** |
| `frontier-20261028-kernel-pair-inequalities-check.py` | `eadb7819aa2ba4b55c8c32b2430261d5f40aae67c89cfac5fbab6968ed9b83f6` | 53 | Exact pair/margin control |
| `frontier-20261028-kernel-pair-inequalities-check-result.json` | `bab447669b4dc32575dd01bd95a32c756fd5bd36ba0e04a21eb9dc61a8607104` | 454 | Exact finite receipt |
| `frontier-20261028-kernel-nearmiss.py` | `6d89820221ba99ec6b8e478dd7940f78a023865be5029f079f8107f46d3fc600` | 45 | Replaces only crossing with 72 |
| `frontier-20261028-kernel-nearmiss-result.json` | `ddf52839c3b54c7421defa85702fd0efe909ee64c1eab4f1d81f959e535f7d4f` | 377 | Formal SAT near-miss |
| `frontier-20261028-kernel-nearmiss-check.py` | `c955608ae14c10c65750e3ec089db0a179cdd89c181e7e6b0becadf37b97d05e` | 60 | Independently written direct verifier |
| `frontier-20261028-kernel-nearmiss-check-result.json` | `63781a03341a6bdd5882536a2d4de961d1b3e3e8e2284f2296ad9ce31fa0594d` | 17 | Positive-control receipt |

All paths above are in the owner root unless explicitly identified as parent dispositions. The written candidate and its λ foundation require a **disjoint full-scope scientific review** before any adoption; f131's parent disposition does not itself establish this new claim. The near-miss is not a witness. No claim of unrestricted target completion follows. **END.**
