# info-6 frontier: D28 first-moment profile and stopping point

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-29T00:31:46-0700**. This is an **UNREVIEWED AUTHOR CHECKPOINT**, not a witness, no-go, disjoint review, novelty or formal-verification claim. It assumes the unreviewed rank-two D28 endpoint packet at its exact scope; frozen predecessors are unchanged.

## Exact first-moment relation

In the rank-two D28 branch, the pinned endpoint shows `m=122`, `Z=8`, `n₁+n₃=28`, `3n₅+n₁=356`, and the odd Q-support inverse equals minus the quadratic Walsh sign. Its notation is

    k₀=(-1)^Q(12h−7),   k=k₀−8δ,
    D=wt(δ)=28,   h=1_{|k|∈{3,5}}.

Set `e=Σδ`, `w=wt(Q)`, `H=wt(h)`, `H₁=wt(hQ)`, and `s=Σ_odd k`. The possible Q weights are 64 or 128, and normalization gives s=0 or 128. The sign-weighted switch sum is fixed by the Q-support equations:

    Σ δ(-1)^Q = n₃−n₁ = 28−2n₁.

It is **not** the same as e. The correct unweighted first moment is

    s = 12(H−2H₁)−7(256−2w)−8e,                                (1)
    H=(440−4n₁)/3,     n₁∈{2,5,8,11,14,17,20,23,26}.          (2)

All nine H values are multiples of 4, namely 112,116,…,144. For example, the pinned labelled formal non-witness has `w=128,s=128,n₁=11,H=132,H₁=62,e=−4`, and (1) holds exactly.

An exact enumeration of the basic integer profiles constrained only by (1), the magnitude ranges, and separate bounds on `Σ_{Q=0}δ=(e+28−2n₁)/2` and `Σ_{Q=1}δ=(e−28+2n₁)/2` is not performed by the pinned checker: the checker deliberately uses the looser universal bounds ±28 on those two class sums. Even this coarse relaxation retains **all 36** combinations of the two w choices, two s choices and nine n₁ choices. It is not an actual spectrum, code, or proof that any one profile is realizable. The formal example checks one of them and independently fails cubic/inverse tests as recorded in its own packet.

## Failed draft and remaining work

A first draft of the local profile checker incorrectly used a weight formula and then substituted `Σδ(-1)^Q` for the unweighted e in (1). Both assertions failed before producing a result file; the checker was corrected before the pinned successful run. The wrong intermediate did not alter the prior immutable D28 packet, and no invalid profile exclusion is claimed here. Since all nine H values are divisible by four, the elementary degree-three weight divisibility does not resolve D28. Full degree-three common placement, all 511 correlations and Boolean inversion still remain, as do every other rank and the original witness-or-unrestricted-exclusion gap.

| File | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-rank2-D28-profile-check.py` | `04efa405dd790dceac391b9ea03322a5999cc3d0096aade1037cb96ae8e9c4db` | 50 | coarse integer profile checker |
| `frontier-20261028-rank2-D28-profile-check-result.json` | `03af5abb3417c3d425150588eb779420cfff3d26752f6dbce0c7d940f8f32b2e` | 4242 | loose formal profile list |
| `frontier-20261028-rank2-D28-placement-v1.md` | `328edda0aced90b4c13632f3bb432ea96e76777d41bbb68675707812de2aa0ff` | 57 | unreviewed endpoint and non-witness |

**END.**
