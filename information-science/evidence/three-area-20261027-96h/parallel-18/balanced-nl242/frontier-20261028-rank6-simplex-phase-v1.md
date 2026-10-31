# info-6 frontier: exact phase counts on the rank-six simplex boundary

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing: **2026-10-28T19:07:41-0700 PDT**. This is an **UNREVIEWED AUTHOR CANDIDATE**, additive to the immutable `frontier-20261028-rank6-simplex-obstruction-v1.md` (SHA-256 `121f8ade103f4d5ae2dad76ae9367f2cda6cd1665ac612b0860e44d05489e12b`, 60 LF). It neither changes any frozen review scope nor resolves the original target.

## Exact necessary phase pairs

For an actual balanced peak≤28 Boolean target, use the same rank-six even-half polar B, odd-half quadratic Q, odd peak/unit indicator P, and counts A_t as in the pinned predecessor. Under `rank(B)=6` and `wt(P)=224`, the following pairs are the **only** possibilities:

| `wt(Q)` | `A₃+A₋₅ = #{P=0,Q=1}` |
|---:|---|
| 112 | 12 or 28 |
| 128 | 16 |
| 144 | 4 or 20 |

The predecessor's modulo-eight conclusion for Q weights 112/144 is an immediate consequence. In particular the previously described formal histogram with `(wt(Q), A₃+A₋₅)=(144,16)` is impossible. The table is necessary, not a claim that any row is realized by an actual target.

## Proof

The predecessor proves, from the forced quartic part and symplectic incidence alone, that h=1+P has weight 32 and is the indicator of `S×R`, where R is the two-dimensional radical and S is an eight-point affine symplectic simplex in the six-dimensional quotient. This slice conclusion does **not** use the predecessor's additional assumption that Q is nonbalanced. Every three points of S have nondegenerate difference span, S affinely spans the quotient, and the XOR of its eight points is zero.

If Q has a nonzero linear term on R, then Q takes value one on exactly two of the four radical points above every x; therefore `wt(Q)=128` and the intersection with h has size `8·2=16`.

Otherwise Q is independent of R. Translate one simplex point to zero, with the other seven vectors v₁,…,v₇ satisfying `B(v_i,v_j)=1` for i≠j and `Σ_i v_i=0`. As shown in the predecessor, the number `t=Σ_{x∈S}Q(x)` is odd, so t∈{1,3,5,7}. The seven vectors span the quotient with exactly the one relation that all seven sum to zero. Hence every quotient vector is represented **uniquely** by a subset of the seven vectors of even cardinality: a subset and its complement represent the same vector, and their cardinalities have opposite parity.

Put `s_i=(−1)^{Q(v_i)+Q(0)}` and `m=#{i:s_i=−1}`. Quadratic polarization gives the exact Gauss sum

    G = Σ_{x∈F₂⁶} (−1)^{Q(x)}
      = (−1)^{Q(0)} Re Π_{i=1}⁷ (1+i s_i)
      = (−1)^{Q(0)} 2^(7/2) cos((7−2m)π/4).                              (3)

If Q(0)=0 then m=t; if Q(0)=1 then m=8−t. In either case (3) yields

    t:      1    3    5    7
    G:     −8   +8   −8   +8.

On the full eight-dimensional odd half, `wt(Q)=4·(64−G)/2`, while `#{P=0,Q=1}=4t`. This gives `(144,4)`, `(112,12)`, `(144,20)`, or `(112,28)`, exactly as in the table. ∎

## Finite controls and limits

A separate script checked all 128 affine shifts of an explicit rank-six quadratic against one symplectic simplex. It found the four nonbalanced phase pairs with multiplicities 8,56,56,8 and independently checked the balanced-radical intersection count. These are finite controls; the written proof is all-variable and remains subject to disjoint review.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-simplex-phase-check.py` | `a7d2baabea73f9c2a3df7d2e1500fbc8e1e5b285dd542cd04cd634b90b004d6b` | 37 |
| `frontier-20261028-simplex-phase-check-result.json` | `f8c3d9501bc53e91e24670176627548e8073c3053602c915b3491069d9f67efc` | 41 |
| `frontier-20261028-rank6-simplex-obstruction-v1.md` | `121f8ade103f4d5ae2dad76ae9367f2cda6cd1665ac612b0860e44d05489e12b` | 60 |

No four-zero general impossibility, actual balanced witness, or unrestricted contradiction is claimed. **END.**
