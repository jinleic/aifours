# info-6 frontier: corrected low-rank energy profiles

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-29T01:10:41-0700**. **UNREVIEWED AUTHOR CANDIDATE**. This additive proof uses the pinned unreviewed collective and sparse-sign results plus the parent-adopted caller. The 17/50-profile and balanced-Q checks are same-owner finite enumeration, not disjoint review. Neither the original target nor all low-rank cases are settled; no witness, unrestricted no-go, novelty, or formal verification is claimed.

## Precise necessary conditions

For an actual balanced f:F₂⁹→F₂ with `T=⊕{x:f(x)=1}≠0` and `max|W_f|≤28`, use the predecessor notation: B is the even-half polar, z the zero count of its quadratic q, Q the odd quadratic, `n_j=#{odd-half |W/4|=j}`, `D=n₁+n₃`, m the number of agreeing unordered T-pairs, and Z the number of Walsh zeros.

* If `rank(B)=2`, then `z=64`, and `(D,m)` is one of `(12,118),(16,120),(20,122)`. Further `104≤n₇≤113` and Z≤24. Neither balanced nor unbalanced Q is excluded by this packet.
* If `rank(B)=4`, then `z=96`, and `(D,m)` is one of `(8,104),(8,110),(10,108),(12,106),(12,112),(14,110),(16,108),(18,112),(20,110),(24,112)`. Further `126≤n₇≤146` and Z≤40.

The profile lists are **necessary only**. The finite receipt lists the 17 and 50 unsigned profiles before imposing any unlisted filters; it is not a construction. No listed profile is shown realizable.

## Exact energy residue

On the odd frequency half put `k=W/4`. Its 256 values are odd and, by the peak assumption, lie in `±1,±3,±5,±7`. Write `v=Walsh(k)/128∈{−1,0,1}` for the actual odd inverse. If m of the 256 T-pairs agree, `wt(v)=256−m`, and Parseval gives

    Σ k²=64(256−m).                                               (1)

Every allowed odd square is 1 modulo 3 except the ±3 square, which is 0. Since **64≡256≡1 mod3**, (1) yields

    m≡n₃=D−n₁ (mod 3).                                          (2)

Equivalently the same identity follows from the odd-energy deficit

    8(m−60)=6n₁+5n₃+3n₅=3(n₃+n₅)+2D+4n₁.                     (3)

There is no additional independent residue obtained by comparing the total odd energy to this deficit; in particular no spurious relation `m≡1−D` is used.

## Branch enumeration

The pinned collective and sparse-sign author candidates give:

* rank 2: z=64, `D∈{12,16,20,24,28}`, m≤122, and `m=116+D/2+2S` with S a sum of four elements of {−1,0,1};
* rank 4: z=96, D even in [8,24], m≤112, and `m=116+D/2+S` with S a sum of sixteen elements of {−1,0,1}.

In both cases m is even. Enumerate all possible integer S in [−4,4] or [−16,16], all n₁ from 0 through D, and enforce (2), the exact relation (3), nonnegative n₃,n₅,n₇, and the even-half bound `64m≤9216−20z−16Z` with Z≥1. The checker in the table performs only these bounded integer loops and deduplicates identical profiles. It produces 17 rank-two and 50 rank-four unsigned profiles, with exactly the `(D,m)` pairs and n₇ extrema in §1. The enumeration does not assign spectra, use a solver UNSAT verdict, or establish any profile's sufficiency.

Since m≥118 at rank 2 and m≥104 at rank 4, the same even-energy inequality gives Z≤24 and Z≤40 respectively. ∎

## Additional rank-two balanced-Q sign filter

An exploratory balanced-Q sign derivation assumed without proof that the unweighted `Σδ` equals the Q-weighted `Σδg`. Its proposed two-profile reduction is withdrawn. No Q-weight restriction is claimed here; all 17 rank-two unsigned profiles remain under this packet's necessary conditions.

This correction affects only the present unreviewed work. The rank-two and rank-four D/m/peak/Z conditions above are the claimed author-written conclusions.

## Controls and explicit provenance

The pinned D12 coarse control has an actual rank-two quadratic, 12 signed atoms and a ternary v satisfying the mod-three inverse relation and collective identity. It meets `(D,m,S,n₁,n₃,n₅,n₇)=(12,118,−2,8,4,132,112)` in the coarse profile arithmetic. Its `Walsh(v)` has peak 38 (allowed at most 14), fails 25 peak entries and mismatches Q at 136 positions; it is **not** a Boolean target witness. An actual balanced rank-two high-peak control has T=228 and peak 504 and is likewise non-target. These are not claims of full spectrum realizability.

Two earlier unsent drafts made separate mod-three errors: one used `256≡−1`, and another lost the factor 64 in (1). Their files and associated checker/receipt are explicitly **INVALID/NONINPUT** in the pinned withdrawal records. The additional balanced-Q claim in this packet is also withdrawn as stated above. The valid 17/50 profile enumeration must be reviewed independently; in its checker, the balanced-sign block and the `balanced_Q_sign_cases` output are exploratory **NONINPUT**, not a proof. No inherited acceptance is inferred.

| File | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-lowrank-valid-profile-check.py` | `77c82174412580278940cb12610bf828f275881d88caad9c82ad9e556edcbb2b` | 98 | profile loop valid; balanced-sign block NONINPUT |
| `frontier-20261028-lowrank-valid-profile-check-result.json` | `71e34280dae3f7843b00ea6ccf948ca53b6fc791997c578779aba319e5910fe6` | 691 | profile receipt; balanced-sign field NONINPUT |
| `frontier-20261028-lowrank-mod3-profile-v1.md` | `fd94da6dbb2f7154463d35ea24aa7f6d5431cd85d72f14f2759c7847d3a77522` | 9 | withdrawn first draft |
| `frontier-20261028-lowrank-global-mod3-v1.md` | `98ac7952a1f10d9f9780b34bc284d144ca54b10f2e793a641154f708fdec4666` | 9 | withdrawn second draft |
| `frontier-20261028-collective-polar-exclusion-v1.md` | `e562e6074dec7beb4a713eed24c3044d6115965de0c60b5c9faf7827da86426d` | 108 | unreviewed collective predecessor |
| `frontier-20261028-rank2-sparse-sign-exclusion-v1.md` | `b16317ae852eb710c7f473b4e2ffcc0d519a9d62af20b37e2a76dc89c6a2143a` | 63 | unreviewed rank-two predecessor |
| `frontier-20261028-rank4-mod3-sparse-v1.md` | `9745f768178832f5679148c3a9e33e3b248a46b839fe6ea6fca0ba22834909e4` | 66 | unreviewed rank-four predecessor |

**END.**
