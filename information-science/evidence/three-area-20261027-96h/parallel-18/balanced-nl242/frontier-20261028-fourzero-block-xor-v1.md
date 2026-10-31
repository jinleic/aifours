# info-6 frontier: four-block support XORs in the four-zero case

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing: **2026-10-28T21:34:18-0700 PDT**. This is an **UNREVIEWED AUTHOR CANDIDATE**, separate from and not an amendment to the consolidated phase packet or any frozen review. It gives necessary structure on the same original Boolean object, not an existence or global-exclusion claim.

## Statement

For any balanced f:F₂⁹→{0,1} with peak≤28 and exactly four Walsh zeros, let R be its zero plane, which is the rank-six even-half polar radical by the f131-scoped result in `frontier-20261028-four-zero-rank6-only-v1.md` (SHA-256 `3e6e7572808e287da2ac3d2fb175efd1878ae52e83fa0a5864290aa3a5fc1f37`, 43 LF). Put U=R^⊥ in the input space and choose a two-dimensional complement Y, so input points are u+y with u∈U and y∈Y. For each y let M_y={u∈U:f(u+y)=1} and `t_y=⊕_{u∈M_y}u`.

Then every |M_y|=64, each t_y belongs to `{0,T}`, and an **odd** number—one or three—of the four t_y equal the nonzero total support XOR T. Let y★ be the unique exceptional block: the unique T-block if there is one, or the unique zero-block if there are three. If ρ:R→F₂ is the odd-half radical phase of the consolidated packet, then

    ρ(r)=r·y★       for every r∈R.                                           (1)

Thus the phase-normalized input translation ρ=0 can be taken to put the exceptional block at label zero. This is a concrete four-block constraint for any putative target, not a claim that such blocks exist at peak≤28.

## Proof

The four zero Walsh coefficients on R say, by inverse Fourier transform over Y, that the signed sum of f on every coset y+U vanishes. Therefore every block has 64 ones. Since each block size is even, the offset y does not affect its support XOR and `T=⊕_{y∈Y}t_y`.

Identify U* with the quotient of frequency space by R, using representatives b that annihilate Y. For each y let W_y(b) be the ordinary seven-variable Walsh transform of `u↦f(u+y)`. The four-point Fourier inversion identity is

    W_y(b)=¼Σ_{r∈R}(−1)^{r·y}W_f(b+r)=Σ_{r∈R}(−1)^{r·y}k(b+r).        (2)

Consider b in the six-dimensional even quotient T^⊥/R with q(b)=0 and b≠0. The whole fiber has q=0, and none of its four frequencies lies in the zero plane. Since |k|≤7, all four k values are ±4. Their signed sum is divisible by 8, so (2) gives `W_y(b)≡0 mod8` for every y. A balanced seven-variable block has `W_y(b)/4≡b·t_y (mod2)`; consequently every such singular b annihilates every t_y.

The singular vectors of a nondegenerate quadratic on six variables span the whole quotient. If the quadratic has 36 zeros this is immediate because no hyperplane contains 36 points. If it has 28 zeros and they lay in a hyperplane, the restricted five-variable quadratic would have 28 zeros; its possible zero weights are 0,8,12,16,20,24,32, contradiction. Therefore each t_y annihilates the entire even quotient and lies in its one-dimensional annihilator span(T). The four t_y XOR to T, proving the one-or-three assertion.

To identify ρ, choose an odd frequency a₀ annihilating Y, so `a₀·T=1`. For nonzero r∈R, let `m=Σ_{x∈M}(a₀·x)(r·x)` as an integer count. The parity identity gives

    k(a₀+r)−k(a₀) ≡ n_r−2m (mod4),       n_r=128.

Thus `ρ(r)=m mod2`. Grouping M into blocks and using `a₀·y=0`, `r·u=0`, and t_y∈{0,T} yields

    ρ(r)=Σ_{y∈Y}(r·y)·1_{t_y=T} = r·(⊕_{y:t_y=T}y).

The XOR of all four Y labels is zero. Hence this last label is the unique exceptional block whether one or three t_y equal T, proving (1). The r=0 case is immediate. ∎

## Positive control and pins

A deterministic generator produced an **actual** balanced truth table with four prescribed zero-plane frequencies, rank-six polar radical R, and block XORs `[T,0,0,0]`. Independent direct 512×512 Walsh and seven-variable block transforms verify (2), the ρ/exceptional-block identity, and the singular-span controls. This table has peak **76**, 34 Walsh zeros and nonlinearity **218**: it is only a high-peak positive control, not a target or a sharpness example for the four-zero case.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-block-xor-control.py` | `13ec6d08f414f989c21af4854b8fee18843cf47bb738a1136c794998947284e6` | 71 |
| `frontier-20261028-block-xor-control-candidate.json` | `e58e27fcc511bef84f6ca38ebcbc8c8f37685a68ae3e5650ad0e13d574d8ef48` | 4 |
| `frontier-20261028-block-xor-control-result.json` | `79fd7577f8bd4783b5ee2bda013139ffee1b8faca1457338932246253b99b56e` | 30 |
| `frontier-20261028-block-xor-control-audit.json` | `bc95361405146c0e4f65c0af25e552b30a97e369ca08f97e61f658ba64dc9c91` | 598 |
| `frontier-20261028-block-xor-check.py` | `b4f924c3bb3d84d351c2fd6bbf84d37314f6b749a7ea2e9e1ef6c0242ef51f98` | 65 |
| `frontier-20261028-block-xor-check-result.json` | `f7e4c769a4dce793d314e41a0fa90d442cff6a84affdabfe6414db9dcc12af87` | 42 |

The finite control does not prove the all-variable theorem or substitute for disjoint review. **END.**
