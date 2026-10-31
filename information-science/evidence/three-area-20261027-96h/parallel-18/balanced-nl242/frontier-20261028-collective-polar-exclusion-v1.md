# info-6 frontier: collective polar-rank obstructions

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-28T23:14:17-0700**. **UNREVIEWED AUTHOR CANDIDATE**. This consolidates and strengthens the immutable 71-LF low-polar precursor; no frozen review is amended. The proof uses the parent-adopted Walsh caller/mod-4 coupling at exact written-support scope, standard quadratic Fourier facts, and the elementary derivation below. It does not use the unreviewed quartic/orbit candidates or any solver UNSAT verdict. No unrestricted exclusion, target witness, novelty, disjoint review, or formal verification is claimed.

## Original-object theorem

Let f:F₂⁹→F₂ be balanced, let `T=⊕{x:f(x)=1}≠0`, and suppose `max|W_f|≤28`. On T⊥ write `k=W_f/4`, `q=k/2 mod 2`, and let B be the quadratic polar of q. Denote its number of zeros by z. Then

    rank(B)≠0;
    rank(B)=2  => z=64;
    rank(B)=4  => z=96.                                            (1)

In the surviving rank-two case, if Z is the number of Walsh zeros and `D=n₁+n₃`, where n_j counts odd-half coefficients of magnitude j after division by four, then

    D≡0 (mod 4),     Z+2D≤64,     D≤28,     108+D/2≤m≤122.       (2)

Here m is the number of agreeing unordered T-pairs. In the surviving rank-four case D is even and D≤24. These are author-written necessary conditions; ranks 2 and 4 are **not** completely excluded. Ranks 6 and 8 and the witness-or-unrestricted-exclusion question remain open.

## Common quadratic Fourier identity

The adopted caller gives k even on the even half and odd on the odd half. The odd quadratic `Q=1_{k≡3 mod 4}` has the same polar B as q. On the odd half define

    h=1_{|k|∈{3,5}},   n_j=#{|k|=j},   D=n₁+n₃,
    g=(-1)^Q,   k₀=g(12h−7),   k=k₀−8δ,   wt(δ)=D, δ∈{−1,0,1}. (3)

On a switched |k|=3 position `δg=+1`; on a switched |k|=1 position `δg=−1`, so `Σ δg=n₃−n₁`. Put `rank(B)=2t`, `L=2^(8−t)`, and let Y be the Walsh support of g. Standard completion of squares yields `|Y|=2^(2t)` and `Walsh(g)(y)=Lσ(y)` for y∈Y, with σ(y)∈{−1,1}. Set

    S=Σ_{y∈Y} σ(y)v(y),      v(y)=Walsh(k)(y)/128∈{−1,0,1}.       (4)

Parseval gives `Σ_Y σ Walsh(hg)=2^t wt(h)` and `Σ_Y σ Walsh(δ)=2^t(n₃−n₁)`. Transforming `k=k₀−8δ`, multiplying by σ and summing over Y yields

    3wt(h)−2(n₃−n₁) = 448+2^(5−t)S.                              (5)

Also `wt(h)=n₃+n₅`. The odd-half energy deficit from 256·7² is

    8(m−60)=3wt(h)+2D+4n₁ = 448+2^(5−t)S+4D.                  (6)

As `|S|≤2^(2t)`, this is an all-variable necessary condition. Balance makes m even.

For rank zero, (6) says `m=116+4S+D/2≥112+D/2`. For rank two it says

    m=116+2S+D/2 ≥108+D/2,     D≡0 (mod 4).                     (7)

For rank four it says

    m=116+S+D/2 ≥100+D/2,      D is even.                        (8)

No chosen histogram or selected inverse frequency is used: Y is the entire quadratic Walsh support.

## Even energy and rank zero/two/four-plus

The even-half coefficients are `0,±2,±4,±6`. At q-zero positions their squares are at most 16, at q-one positions at most 36. With Z≥1 because k(0)=0,

    64m≤16(z−Z)+36(256−z).                                      (9)

A polar-zero q is affine with q(0)=0, hence z=256 or 128; (9) gives respectively m≤62 or m≤102, contradicting (6)'s m≥112. At rank two, z∈{64,128,192}; (9) gives m≤122,102,82, respectively. The latter two contradict m≥108. At z=64, combine (7) and (9) to obtain `Z+2D≤64`; the evenness/divisibility in (7) then yields D≤28 and the m range in (2).

At rank four, z∈{96,128,160}. The z=160 upper bound m≤92 contradicts m≥100. At z=96, (8) and (9) give D≤24. It remains to rule out z=128, whose even-energy upper bound is m≤102.

## Rank-four z=128: modulo three and quotient integrality

Assume z=128 and rank(B)=4. From (8), m is 100 or 102 and D is even, with exactly the following possibilities:

    m=100: D=0, S=−16;
    m=102: (D,S)=(0,−14),(2,−15),(4,−16).                      (10)

For y∈Y, `Walsh(g)=64σ`. The actual inverse equality and (3) give

    3 Walsh(hg)(y)−112σ(y)−2 Walsh(δ)(y)=32v(y).

Modulo 3, setting `d_y=σ(y)Walsh(δ)(y)` gives

    d_y+σ(y)v(y)≡1 (mod 3).                                     (11)

If D=0, (11) forces σv=1 at every y∈Y, contrary to S=−16 or −14. If D=2 and S=−15, at least 15 of the 16 σv values are −1. Each such d_y is even, has |d_y|≤2, and is 2 modulo 3, hence equals +2. The remaining term is at least −2, so `Σ_Y d_y≥28`; but Parseval gives `Σ_Y d_y=4(n₃−n₁)`, whose magnitude is at most 8. Contradiction.

Finally let D=4,S=−16. Every σv is −1, and (11) forces `d_y∈{−4,2}`. Let A={y∈Y:d_y=−4}. Since `Σ_Y d_y=4(n₃−n₁)` and `n₁+n₃=4`, its size can only be 4 or 8.

The Walsh transform of four ±1 atoms has magnitude 4 precisely where all four signed characters agree. Therefore A is an affine subspace of Y. On A, `Walsh(δ)=−4σ`, so σ restricts to an affine sign character there. The quadratic dual phase σ on the four-dimensional affine Walsh-support Y has nondegenerate polar; its totally isotropic subspaces have dimension at most 2. Thus |A|=8, which would have dimension 3, is impossible.

If |A|=4, A has dimension 2 and σ is affine on it. Then

    Walsh(δ)(y)=σ(y)(2−6·1_A(y))   for all y∈Y.                  (12)

The four-dimensional Walsh transform of σ has magnitude 4 at every dual character; the transform of `σ1_A`, since σ is affine on A, is supported at exactly four dual characters. At any of the remaining 12, the transform of the right side of (12), divided by 16, equals ±1/2.

That is impossible: writing Y=y₀+U with U four-dimensional, the same divided transform equals `Σ_{x∈c+U⊥}δ(x)(−1)^{<y₀,x>}` for a spatial coset c, an integer. This excludes the last case and hence rank-four z=128. ∎

The standard dual-phase fact used here follows by splitting off the radical of B, Fourier transforming a nondegenerate four-variable quadratic, and completing the square: on its affine four-dimensional support the Walsh signs have a nondegenerate quadratic polar. The checker verifies all 32 such phases, all 30 affine 3-flats and all 60 isotropic affine 2-flats per phase, including the half-integer quotient obstruction.

## Controls and remaining gap

A pinned **formal labelled non-witness** has rank two, z=64, Z=8, D=0, m=108, `k(0)=0`, `max|k|=7`, correct total energy 16384, and common even/odd mod-4 quadratic. All four inverse coefficients on Y are the permitted ±128, attaining the collective bound. Other odd-half inverse coefficients have magnitude 768, so it is not a Boolean spectrum or target witness. This is an intended-reason positive control for the collective bound, not proof of rank-two realizability.

The separate checker also constructs an **actual balanced rank-four/z=128 high-peak non-target**, with T=86, m=250 and peak 496; direct character sums and FWHT agree. The low-polar precursor has actual high-peak rank-zero and rank-two-plus controls and an origin-relaxed formal object. They demonstrate that the peak/balance assumptions matter but do not constitute target witnesses.

The full proof, especially the rank-four affine-support and half-integer argument, and every finite control need disjoint full-scope review. Nothing here claims rank-two z=64, rank-four z=96, rank six, or rank eight is realizable or excluded.

| File | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-collective-polar-check.py` | `61c6be42be3870fe4e6931885c053602bd4a969eb3b80bb19d32de93ef10e834` | 117 | finite and positive controls |
| `frontier-20261028-collective-polar-check-result.json` | `4d1f774d53c0d74e30dcf47d7f504d974350aa3e8e4734b10b5309278fb9d85b` | 567 | control receipt and data |
| `frontier-20261028-low-polar-nearmiss-check.py` | `51baa5969baad3e60191c4ad3c39153330a52eddef55631c435089b2d11b0e6b` | 83 | earlier controls |
| `frontier-20261028-low-polar-nearmiss-check-result.json` | `d3733f2ae85c71aeab20638b435439c4c77551c1368c561c4cbbff5532a4ad6d` | 47 | earlier receipt |
| `frontier-20261028-low-polar-exclusion-v1.md` | `9b98a07d1d34e55282e410b0d5c24eb187ed95bacb1dbfe668849956590deaf2` | 71 | unreviewed superseded-strength precursor |
| `institute/runs/three-area-2026-10-27-96h/dispositions/info-6-walsh-caller-and-mod4-coupling-parent-v1.md` | `721222262af91bc768227ce8bfae563cabf5a102437ac55e6583de38ec2d3c9d` | 23 | parent-adopted written caller |

**END.**
