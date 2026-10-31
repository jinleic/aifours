# info-6 frontier: sharpened extremal center bound

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-28T22:41:21-0700**. **UNREVIEWED AUTHOR CANDIDATE**, additive to the immutable sign-syndrome paper. It relies on that paper's unreviewed three-orbit reduction and its 1,536-phase modular check, plus the new complete center-sign check below. No theorem here is adopted, disjointly reviewed, an actual witness, a global exclusion, or a novelty claim.

## Precise refinement

Under the hypotheses of the pinned sign-syndrome paper—balanced f, `T≠0`, peak≤28, rank-eight even-half polar, and odd-half `wt(P)=210`—write `n_j=#{odd-half |W/4|=j}`. Then

    n₁+n₃≥55 and is odd;     n₇≤201.                              (1)

Let m be the number of agreeing unordered T-pairs as in the support-floor paper. In this extremal `wt(P)=210` branch,

    m≥96,  equivalently wt(D_T f)≤320.                             (2)

At equality m=96, necessarily `(n₁,n₃,n₅,n₇)=(10,45,1,200)`. These bounds **do not** apply to the other rank-eight branch `wt(P)<210` and do not replace the all-rank-eight m≥80 claim of the separate support-floor candidate.

## Center sign and Parseval

Use the exact baseline k₀ and bit difference δ from the pinned sign-syndrome paper. Its phase identity says

    Walsh(δ)(y) ≡ A(−1)^{<p,y>} (mod 16),  A=±5,                 (3)

with D:=`Σ_x δ(x)²=n₁+n₃`, and p the representative-dependent center. The original finite checker pins p and A. The **new** checker establishes the following additional facts for every one of the same 512 Q phases of each of the three representatives:

| A | baseline residue r(p) | baseline bit b₀(p) | allowed δ(p) |
|---:|---:|---:|---|
| +5 | 3 | 1 | 0 or −1 |
| −5 | 5 | 0 | 0 or +1 |

Let `α=sign(A)` and `t_y=α(−1)^{<p,y>}Walsh(δ)(y)`. Then each integer `t_y≡5 (mod 16)` and Fourier inversion gives

    (1/256)Σ_y t_y=αδ(p)≤0.                                      (4)

For every integer t congruent to 5 mod 16, the adjacent allowable values surrounding zero are −11 and 5. Consequently

    (t−5)(t+11)≥0,   i.e.  t²≥55−6t.                            (5)

Averaging (5), using (4) and Walsh Parseval, gives

    D=(1/256)Σ_y t_y² ≥55−6αδ(p)≥55.                            (6)

The parity of D is odd because every Walsh(δ)(y) has parity D, while (3) is odd. Also `n₃≤wt(h)=46`, so `n₁=D−n₃≥9`; as `n₁+n₇=wt(P)=210`, this gives n₇≤201.

The exact odd-half energy identity is

    8(m−60)=6n₁+5n₃+3n₅=138+2D+4n₁.                           (7)

With D≥55 and n₁≥9, its right side is at least 284. Since m is even, m≥96. If m=96, then `D+2n₁=75`. Together with `D≥55` and `n₁≥D−46`, this forces D=55 and n₁=10. Therefore n₃=45, n₅=1, and n₇=200. ∎

The same proof gives the optional sharper conditional split: if δ(p)=−α, then (6) yields D≥61, hence n₁≥15, n₇≤195, and m≥100. If m=96, equality in (6) forces δ(p)=0; the center remains an |k|=5 entry.

## Controls, gap and evidence

The additional 51-LF checker independently reconstructs the three representatives, checks all 1,536 Q phases, verifies that the center lies in h and the signed pair `(A,r(p))` is always (+5,3) or (−5,5), and checks the full modular identity against the pinned transform routine. The inequality (5) is elementary for the infinite congruence class; the script's finite sample is only a control. The predecessor's deliberately peak-relaxed one-coordinate construction and wrong-center mutation remain the positive control for the syndrome, not a Boolean witness. No solver verdict is used as a proof.

Other `wt(P)` branches, actual realization of the m=96 boundary, the ten-zero case in general, and the unrestricted witness-or-exclusion target remain open at this author-written scope. All dependencies and the complete finite tables require disjoint full-scope review.

| File in this directory | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-extremal-center-sign-check.py` | `c08efb40e3081da1f35c8d2fc6f1cfca23c0bb8a200d773341837d31ad438c12` | 51 |
| `frontier-20261028-extremal-center-sign-check-result.json` | `d6b190754a8c995fc36016e4bf4976fb7e6509986245f97bbab77b9963ec9f8b` | 29 |
| `frontier-20261028-extremal-sign-syndrome-v1.md` | `3bdfd54f174f33ded7c577a2dc7c27afecbb4c62d8fb1e6f60e5877fb0567435` | 71 |
| `frontier-20261028-extremal-sign-syndrome-check.py` | `aacaf9e79c9d01325fb0c6f7310c96e5085a70040f91c1a620cc84d502db7f2f` | 63 |
| `frontier-20261028-extremal-sign-syndrome-check-result.json` | `8d80d4f6b53ec7e2ffd39d8357602944e80f67c2f8a1445b568648f8180cd287` | 60 |
| `frontier-20261028-fullrank-extremal-phase-v1.md` | `e12b3a32a3f7f19b9dea35615bbf4c8fbd6ba970d1491ca33f3fc8f4bacc6fd4` | 100 |

**END.**
