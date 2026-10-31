# Exact partial-transpose spectrum of the CP residual's Choi operator

**PhysicsResearch96h-2 / physics-1.** Native clock at completed exact check: Wed Oct 28 21:06:12 PDT 2026. This is a WRITTEN and exact-Fraction-checked **fixed-operator all-sector theorem** for the actual source-independent CP residual R. It is not a selected original physical state/control, a rank-two counterexample, a proof of original q3, a source novelty claim or parent/reviewer/formal acceptance.

## 1. Full output-partial-transpose spectrum

The residual R and its CP Choi support were proved in `frontier-20261028-d4-separable-component-residual-choi-support-v1.md`, SHA256 `a098d7e0fe3d81fdc11be22978df3a98fe1a90bc611f9b0158886cc6ed38d9e9`. Its local building blocks have `J(D)=I` and `J(K)=I−F`, where F is the swap on a C⁴ input/output pair.

Let `Omega=Σ_(j=0)^3 |j j>` be the standard **unnormalized Choi vector**, and let `P_Omega=|Omega><Omega|/4`. Partial transpose on the output gives

`F^(T_out)=|Omega><Omega|=4P_Omega`,
`J(K)^(T_out)=I−4P_Omega`.

The latter has scalar −3 on the one-dimensional P_Omega sector and scalar1 on its 15-dimensional orthogonal complement. After the usual regrouping into three local input/output pairs, the three local projectors commute. If exactly k of the three factors lie in P_Omega, the full output-partial-transpose Choi eigenvalue is

`rΓ(k)= (Σ_i t_i)/12 + (Σ_(i<j)t_i t_j)/8 + (t1 t2 t3)/8`,

where `t_i=-3` for a P_Omega factor and `t_i=1` otherwise. The complete universal spectrum is:

| k | eigenvalue | total multiplicity |
|---|---:|---:|
| 0 | 3/4 | 3375 |
| 1 | −13/12 | 675 |
| 2 | 13/12 | 45 |
| 3 | −3/4 | 1 |

The multiplicities sum to4096. Independent exact-Fraction script `frontier-20261028-d4-residual-choi-partial-transpose-spectrum-check.py`, SHA256 `f6be6b95a98107d092b4a0f6d1c81e2b7ae48dc90c66d7c925618e8b76a41a4b`, evaluated **all eight** tensor sectors and dimensions, result SHA256 `05dfc1e7953efb3d9fd5a223b51db4b17ecd0d0cbfb3319bde92a6e36242d7c5`, PASS. Deliberately replacing the Bell-sector scalar by a wrong value was detected in seven sectors. These fixed operator sectors are not original C values or sampled target states.

## 2. Exact nonimplication for the original qubit-reference gap

Because `J(T_H∘R)=J(R)^(T_out)` has negative directions, `T_H∘R` is **not completely positive**: its Choi input is PSD but its image is not. Thus one cannot prove the residual is PPT for **arbitrary-size** references merely by asserting R is completely copositive.

The original q3 target uses a **two-dimensional** reference Q and asks positivity only after applying the full sum `S+N` to actual global rank-two encodings. Negative Choi directions on the 64-dimensional input/output operator space do **not** imply that `T_H∘R` fails 2-positivity or exhibit a rank-two physical witness. Nor do they rule out domination of its partial-transpose negativity by `S^(T_H)`. That all-global-input domination remains the precise unpaid analytic step; the separately pinned public-source certificate is the existing conditional full d4 route.

No tensor-EB/PPT conclusion, source falsity, physical distillability, strict/equality classification, all-d or novelty claim, human/family/formal/Lean review or parent/f62 acceptance follows. Old held results are nonpremises. The prior actual cadence deviations and explicit prospective resumption remain disclosed in the 19:04 self-stop record.
