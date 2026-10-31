# Exact full Choi spectrum of the three-site CP residual

**PhysicsResearch96h-2 / physics-1.** Native clock at completed exact check: Wed Oct 28 21:04:56 PDT 2026. This is a WRITTEN and exact-Fraction-checked **all-sector operator theorem** for the fixed source-independent residual CP map. It is not an evaluated physical input/state, a q3 counterexample or proof, a physical operational claim, source novelty, parent/f62, human/family or formal/Lean acceptance.

## 1. Exact residual and commuting local projectors

For the actual `Psi(X)=Tr(X)I4−X^T/2`, put `D(X)=Tr(X)I4` and `K(X)=Tr(X)I4−X^T`. The exact three-site all-input decomposition proved in `frontier-20261028-d4-global-separable-cp-decomposition-v1.md`, SHA256 `07cba1eace84a037efa9784117e4ef91d952b8cdb0cce529a7581fa223a9664d`, has residual

`R=(1/12)Σ_i K_i D_j D_k
  +(1/8)Σ_(i<j) K_i K_j D_k
  +(1/8)K_1 K_2 K_3`.

With input/output local Choi grouping, `J(D)=I`, `J(K)=I−F=2P_-`, where F is the local C⁴⊗C⁴ swap and `P_-` its antisymmetric projector. The complementary symmetric projector P_+ has dimension10; P_- has dimension6. The three local swap/projector operators commute because they act on distinct site pairs.

## 2. Complete sector spectrum

On a joint tensor sector with exactly k antisymmetric local factors, `J(D)` has scalar1 in every site and `J(K)` has scalar2 at precisely those k sites and0 at the others. Therefore the exact eigenvalue of J(R) is

`r(k)= k/6 + binom(k,2)/2 + binom(k,3)`,

and the total multiplicity among all site choices is `binom(3,k)·6^k·10^(3−k)`. For **every** k=0,1,2,3 this yields the complete spectrum:

| k | exact eigenvalue | total multiplicity |
|---|---:|---:|
| 0 | 0 | 1000 |
| 1 | 1/6 | 1800 |
| 2 | 5/6 | 1080 |
| 3 | 3 | 216 |

The multiplicities sum to4096; rank3096 and kernel `Sym²(C⁴)^tensor3` agree with the independent sum-of-PSD-kernels proof in `frontier-20261028-d4-separable-component-residual-choi-support-v1.md`, SHA256 `a098d7e0fe3d81fdc11be22978df3a98fe1a90bc611f9b0158886cc6ed38d9e9`.

The independent exact-Fraction checker `frontier-20261028-d4-residual-choi-sector-spectrum-check.py`, SHA256 `38225497ae2a776378bc0438c037bdba5f1b8e5a0e467047a5bdce89ecb55e18`, evaluated **all eight** local symmetry-sector combinations and their exact dimension multiplicities; result SHA256 `4e07611c7c13bd8278523dd673dedc04bb77254585d4875c7ee375d52c516bf8`, PASS. An intentionally omitted triple-K term was detected. The four sector labels are an exhaustive spectral decomposition of a fixed operator, not selected physical target states or parameter instances.

## 3. Crucial nonimplication

The exact Choi spectrum confirms R is CP and gives its entire source-space kernel/rank. For the original arbitrary PSD `rho` on H⊗C², however, the unpaid q3 step remains to prove

`S(rho)^(T_H)+[(R⊗id_2)(rho)]^(T_H) >= 0`

on all original global-isometry pure inputs. J(R)'s input-output Choi positivity/spectrum is a **different cut** from output H versus reference Q partial transpose, so this result alone neither proves residual PPT nor supplies a physical counterexample. No tensor-EB, original q3 strict/equality, all-d, physical operational, external human/model-family, formal/Lean or parent/f62 acceptance is inferred. Old held material is not a premise; the previously disclosed cadence gaps and prospective resumption remain unchanged.
