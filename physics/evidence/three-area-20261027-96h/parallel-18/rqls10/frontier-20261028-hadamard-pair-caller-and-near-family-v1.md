# Fourier-product 1-resolution is a two-Hadamard problem

**WRITTEN author reduction, independently reviewable; exact finite Laurent checks and exploratory floating search stated separately.** `/bin/date` before the exact interpolation check: **Wed Oct 28 18:39:26 PDT 2026**. This is a representation of ONE restricted physical ansatz, not an equivalence for arbitrary QLS10 and not an unrestricted no-go.

## 1. One transversal already gives all ten

Let K be an arbitrary 10×10 complex Hadamard, `zeta=exp(2*pi*i/10)`, and set

`v_(r,c)(t)=zeta^(r t) K_(t,c)/sqrt(10)`.

Every column is a Fourier ONB and every row is K's column ONB. If ANY transversal T is an ONB, write it as cells `(r(c),c)`; the ten shifted sets

`T_s={(r(c)+s,c):c∈Z10}`, s∈Z10,

are also ONBs, because `v_(r+s,c)=D_s v_(r,c)` for the SAME diagonal unitary D_s. They are pairwise cell-disjoint and partition all100 cells. Thus, in THIS ansatz, an orthogonal transversal is equivalent to a 1-resolution. No property of a particular incidence Latin square is assumed.

Relabel the columns so that T uses r=c, and write H=K/sqrt(10), `F_(t,c)=zeta^(t c)`. Then T is an ONB exactly when `J=H∘F` is unitary, with ∘ entrywise product. Therefore the exact ansatz target is to find

1. H and H∘F both complex Hadamard unitaries, and
2. 100 distinct physical rays.

The 100-ray requirement has an exact inexpensive form: for all distinct c,d, the coordinate-wise column ratio `K_(t,c)/K_(t,d)` must NOT equal a constant times `zeta^(m t)` for any m∈Z10. Indeed such a ratio is precisely the condition that some two cells in columns c,d are projectively parallel; cells within one physical column are automatically orthogonal. This gives only `45×10` character tests. Conversely, any exact H satisfying both bullets yields all30 actual ONBs by cyclic shifts, and would solve the original target (not just its Gram relaxation).

This equivalence applies only to the Fourier-product ansatz; it is not a no-loss-of-generality statement for a general quantum Latin square. The all-BH(10,5) and all-phase two-block Diţă obstructions already delivered are proper subfamilies of this H/H∘F problem.

## 2. Exact one-phase family between two incompatible endpoints

One bounded floating search suggested an algebraic phase pattern; the following is now exact and independent of floating convergence. Let E be the explicit 10×10 exponent table embedded in `frontier-20261028-near-hadamard-pair-exact-v1.py`, SHA **be0a9fe04893282e8491e2804a7e40bfc354ed324fe5e33530216095c68dcdd3**. Define `a_(t,c)=floor(E_(t,c)/2)`, `m_(t,c)=E_(t,c) mod2`, and for an arbitrary unit complex z let

`H_(t,c)(z)=zeta^a_(t,c) z^m_(t,c)/sqrt(10)`, `J(z)=H(z)∘F`.

All entries remain flat of modulus 1/sqrt(10). Exact Laurent-polynomial audit `frontier-20261028-hadamard-interpolation-check-v1.py`, SHA **96f4660ebca5e8c41e79abccd99b419fe5bcae416151677eebf152859f947bd0**, reduces coefficients in Q(zeta) using Phi10 and checks all45 unordered column pairs of EACH matrix. For every |z|=1:

- H has exactly five potentially nonzero unordered column inner products, with common magnitude `|1-z/zeta|/2`; they vanish simultaneously iff z=zeta.
- J has exactly five potentially nonzero unordered column inner products, with common magnitude `|1-z|/2`; they vanish simultaneously iff z=1.
- The five H defect edges are `(0,2),(1,5),(3,4),(6,9),(7,8)`; the five J defect edges are `(0,1),(2,4),(3,9),(5,8),(6,7)`. Their union is a 10-cycle.

Thus no member is a Hadamard pair. Precisely, the total squared Frobenius loss for BOTH Gram matrices is

`L(z)=5/2*(|1-z/zeta|²+|1-z|²)`.

On the unit circle its exact minimum **within this one-phase family only** is

`10*(1-cos(pi/10))`, attained at `z=exp(i*pi/10)`.

At the midpoint all physical cells have distinct rays: the separate exact script `frontier-20261028-near-hadamard-pair-exact-v1.py` checks all45×10 character tests and reduces the exact objective modulo Phi20. Its output explicitly reports five nonorthogonal column pairs in H and five in J. Consequently this midpoint is NOT a Hadamard pair, NOT an exact QLS, and NOT a witness. The midpoint supplies merely a **feasible upper bound** on the nonnegative loss of the unrestricted flat-matrix optimization; no universal lower bound follows.

## 3. Bounded numeric exploration, no proof of impossibility

`frontier-20261028-general-hadamard-pair-search-v1.py`, SHA **f958404aa629e17ed9c290ad2000abc153fed5fed2d7e7eb3ae8e5a8e6080f96**, optimized H and H∘F simultaneously over arbitrary dephased flat phases, not the one-phase family, using 24 deterministic random initializations, each3500 Adam steps. A finite-difference gradient check agreed to approximately 4e-10. Result JSON `frontier-20261028-general-hadamard-pair-result-v1.json` SHA **9f12f80332cbe516f460f29b87052a91f4f9eda24919a846ce40548172dce161** and best float array SHA **453927e88176f901b3325d45a61232dd5d2a9a54776fc504d907f915bcd1e190** record all runs.

Best floating loss was approximately **0.48943483704846**, consistent with the exact one-family value above; its reported worst Gram error for both H and H∘F was approximately **0.1564344650**. No numeric candidate reached the prescribed 1e-10 ONB threshold. Several other local losses appeared. The repeated minimum is a heuristic observation, NOT evidence that the exact one-family value is the global minimum. The run cannot exclude any exact general H and is not a target solution.

## 4. Open gap

Find or rule out an exact general H/H∘F Hadamard pair with no Fourier-character column ratios. A valid pair would immediately give a full resolution by the cyclic action in §1, but a general product no-go would still leave ALL nonproduct QLS constructions open. No formal proof, peer acceptance, unrestricted conclusion or novelty claim is made.
