# info-6 frontier: zeros on singular subspaces and energy

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-28T23:03:50-0700**. **UNREVIEWED AUTHOR CANDIDATE**. This is an all-variable necessary-condition theorem and a narrow exclusion, not a target witness, unrestricted no-go, novelty claim, disjoint review, or formal verification. Its Walsh definitions are those of the parent-adopted caller; the cubic derivation and energy proof below are explicit and do not assume the separate unreviewed quartic-coupling candidate.

## Statements

Let f:F₂⁹→F₂ be balanced, let `T=⊕{x:f(x)=1}≠0`, and suppose `max|W_f|≤28`. On `K=T⊥` define `k=W_f/4` and the quadratic `q=k/2 mod 2`; let Z be the total number of Walsh zeros. If L⊂K is any linear s-dimensional subspace containing 0 on which q is identically zero, and s≥3, then

    Z ≥ #{a∈L:W_f(a)=0} ≥ 2^(s−3).                             (1)

Consequently q cannot be identically zero on K. If its polar has rank zero, q must instead be a nonconstant affine form, so `Z≥16` and the number of magnitude-28 Walsh peaks is at least **150**. This excludes only the constant-q case, not the rank-zero polar or unrestricted target.

The remaining table combines (1), the standard quadratic-form singular subspace dimensions, and the explicit energy bound in the pinned qzero-floor candidate. It applies only to the row's exact polar-rank and q-zero count z; m counts agreeing unordered T-pairs. The z=256 row is impossible, as 267 required peaks would exceed 256 odd frequencies.

| polar rank | z | singular dimension s | Z≥ | m≤ | peaks≥ |
|---:|---:|---:|---:|---:|---:|
| 0 | 256 | 8 | 32 | 56 | 267, impossible |
| 0 | 128 | 7 | 16 | 100 | 150 |
| 2 | 64 | 6 | 8 | 122 | 91 |
| 2 | 128 | 6 | 8 | 102 | 144 |
| 2 | 192 | 7 | 16 | 80 | 203 |
| 4 | 96 | 5 | 4 | 112 | 118 |
| 4 | 128 | 5 | 4 | 102 | 144 |
| 4 | 160 | 6 | 8 | 92 | 171 |
| 6 | 112 | 4 | 2 | 108 | 128 |
| 6 | 128 | 4 | 2 | 102 | 144 |
| 6 | 144 | 5 | 4 | 98 | 155 |
| 8 | 120 | 3 | 1 | 106 | 134 |
| 8 | 136 | 4 | 2 | 100 | 150 |

For z=64, the parent-adopted ≥92 peak bound is stronger than the table's 91. The independent author-written rank-eight sextic argument gives a stronger Z≥10, but is not an input to this table.

## Cubic zero indicator on L

Let `M={x:f(x)=1}`. For a∈K, define `n(a)=#{x∈M:a·x=1}`. The adopted caller gives

    k(a)=n(a)−128+128·1_{a=0},      n(a) even,                  (2)

so `g(a):=k(a)/2 mod 4` is `n(a)/2 mod 4`, including a=0. Choose coordinates a=(a₁,…,a_s) on L. For each x∈M, write the linear character bit as an XOR of the selected aᵢ. Its integer expansion modulo 8 is

    ⊕ bᵢ = Σ bᵢ − 2Σ_{i<j}bᵢbⱼ + 4Σ_{i<j<k}bᵢbⱼbₖ  (mod 8). (3)

Every linear coefficient in the sum n(a) is even because its parity is the corresponding basis vector's dot product with T. Dividing (3) by two therefore expresses g as a degree≤3 polynomial over Z/4, whose cubic coefficients are even. On L, `g mod 2=q=0`. Uniqueness of the Boolean algebraic normal form implies every coefficient of g is even modulo 4. Thus `g/2 mod 2` is a Boolean polynomial of degree≤3.

On L, q=0 and the peak bound imply k is 0 or ±4, so

    H(a):=1+g(a)/2 mod 2 = 1_{k(a)=0}.                          (4)

H has degree≤3 and H(0)=1. The elementary minimum-support bound for a nonzero Boolean polynomial of degree≤3 in s variables is `2^(s−3)`: induct on s using restrictions and the derivative, or use the standard Reed–Muller minimum-distance proof. This establishes (1). ∎

## Constant-q contradiction and rank table

If q is identically zero, take L=K in (1): Z≥32. The even-half k values are then 0 or ±4, giving even squared energy at most `224·16=3584`. On the odd half all 256 k values are odd and have magnitude≤7, giving energy at most `256·49=12544`. Their total is at most **16128**, contradicting the adopted Walsh/Parseval value `Σ k²=16384`. This proof does not use the odd-half quartic theorem, a solver UNSAT result, or any selected histogram. ∎

For the table, let the polar rank be 2t. If q is zero on its radical, the usual symplectic normal form has a totally singular space of dimension `8−t` in the plus case and `7−t` in the minus case; their q-zero counts are `128+2^(7−t)` and `128−2^(7−t)`. If q is nonzero on the radical, q has 128 zeros; the kernel of its radical linear form plus a graph over a Lagrangian quotient gives a singular space of dimension `7−t`. The rank-zero affine and constant cases are the evident t=0 limits. Applying (1) and the energy formula in the pinned predecessor gives the listed rows. These singular spaces are guaranteed lower-bound inputs; they need not contain every Walsh zero.

## Positive controls and limits

The checker constructs a **formal non-Boolean** k with q=0, exactly 32 zeros, even nonzero values all 4, and all odd values 7. Its zero indicator is an explicit cubic and reaches the support bound; its total energy is exactly 16128, so the first failing class is Parseval. Thus the two numerical sides of the constant-q contradiction are simultaneously sharp in this relaxed object. A second formal non-witness has nonconstant affine q and exactly 16 zeros, demonstrating sharpness of the cubic restriction on its seven-dimensional kernel. Neither is a full spectrum of a Boolean function.

The cubic minimum-support proof and the 13 rank rows have not received disjoint review. In particular the table does not show any original target exists, nor does it exclude all rank-zero polar functions. The broader witness-or-unrestricted-exclusion gap and global novelty remain.

| File | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-singular-cubic-zero-check.py` | `5192d81ea777408bcdbda67ae671d0d967f354f93c8616ce40abbadde32bfe35` | 45 | finite formal controls |
| `frontier-20261028-singular-cubic-zero-check-result.json` | `3b8115465a8be8e6d1c6e87a7ffac222c7785ee317f8eac676b1a46e710404a0` | 115 | finite receipt |
| `frontier-20261028-qzero-energy-floor-v1.md` | `f6bfcff8e7334bc0a0580959ea2d8602f7dce08e2c9c1e255bddee4f6293c981` | 64 | unreviewed energy predecessor |
| `institute/runs/three-area-2026-10-27-96h/dispositions/info-6-walsh-caller-and-mod4-coupling-parent-v1.md` | `721222262af91bc768227ce8bfae563cabf5a102437ac55e6583de38ec2d3c9d` | 23 | parent-adopted written caller |

**END.**
