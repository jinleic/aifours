# The N=2 diamond–diamond subclass is closed by the adopted f238 gap-removal theorem

Owner: InfoResearch96h-2 / info-1. Native clock observed before drafting: `Thu Oct 29 18:53:43 PDT 2026`.

**AUTHOR-WRITTEN NOTE, UNREVIEWED.** It closes exactly one subclass question posed by Main's option (ii), by citing one ADOPTED same-harness disposition and one elementary identification. No new machinery is claimed, and this note does not decide the general N=2 problem, the value V for any ε, or anything about `0<ε<ε0`.

## 1. Premises actually used

* **Adopted f238 disposition** `institute/runs/three-area-2026-10-27-96h/dispositions/info-1-privacy-fixed-core-parallel-gap-removal-all-epsilon-parent-v1.md`, SHA-256 `a0d8d728e66fc256495cd08b5644f2688051fe7fe2edf8b6aa4da4d76529e9ba`: for every ε>0, every compact canonical core C, every g>=0 and every radius sequence with `R_(i+1)>=R_i+1` and finite weighted mass/moment, the phase with levels `K_i=C+R_iD` satisfies `J(P_K)>=J(P_(K^0))`, equality iff `R_i=g+i` for all i; when a gap exists the weighted signed excess at the true V_b is strictly positive. Diamond levels are parallel dilations of a diamond core, so this class is exactly the C=gD radial diamond-phase family.
* **Adopted-with-qualification f266 N=1 statement of record** (prospective acceptance `9065e9cdbaaac3925ace542b0e35a3b2ff5afb0ff11bfb9c8291d98cc90d4a3f` accompanying `bc53f153…987` and the premature-read qualification `92a749aa…b9ee`): used ONLY for the already-adopted-from-f238-era fact that the one-core diamond family's minimum over g∈[0,1) — equivalently g>=0 under the P_0=P_1 identification — is attained at the larger positive root g* of the explicit quintic P_m, with value `M4(g*)/(3M2(g*))`. This scalar minimization fact is itself a direct Descartes/sign computation (candidate §3), not an optimizer theorem; it is cited at that scalar scope only.

No LAW642 theorem, held/withdrawn/ZERO body, MDA26 source text, f161/f162 or protected v214 material is used. Same continuing author; prior exposure disclosed; no independent-authorship claim.

## 2. The identification

Fix ε>0, b=e^(-ε). An **N=2 diamond–diamond profile** is a two-level geometric phase with `C_0=g_0 D` and `C_1=g_1 D`, `g_1>=g_0+1`, followed by the exact tail `C_1+jD, j>=1`. Its unnormalized mass and moment are

    Z = 2[(1−b)g_0² + b·M2(g_1)],
    N = (2/3)[(1−b)g_0⁴ + b·M4(g_1)],

with `M2(g)=g²+2mg+T2`, `M4(g)=g⁴+4mg³+6T2g²+4T3g+T4`, `m=b/(1−b)`. (Level 0 contributes its own area `2g_0²` and moment `(2/3)g_0⁴` at weight `(1−b)`; the tail from level 1 is the last-core geometric tail of `g_1 D` at weight `b`.)

**Degenerate case.** If `g_1=g_0+1`, then the levels `g_0D, (g_0+1)D, (g_0+2)D, …` are exactly the minimal-shell sequence of the single core `g_0D`. The phase law IS the one-core diamond law `P_(g_0)`. This is an equality of densities, not merely of costs: both have density `b^i` on the annulus between `i+g_0` and `i+g_0+1` diamond radii.

**Gap case.** If `g_1>g_0+1`, this is a fixed-core parallel diamond phase with at least one positive gap. The adopted f238 theorem applies verbatim with `C=g_0D`, `R_0=g_0`, `R_1=g_1`, `R_i=g_1+(i−1)` for i>=2 (all later increments are one): `J(P)>J(P_(g_0))`, strictly.

## 3. Conclusion of the subclass

**Proposition (diamond–diamond N=2 closure).** For every ε>0 and every `g_0>=0, g_1>=g_0+1`:

    J(N=2 diamond–diamond at g_0,g_1) >= J(P_(g_0)) >= min_(0<=g<1) J(P_g) = M4(g*)/(3M2(g*)),

with equality throughout iff `g_1=g_0+1` and `g_0=g*` (mod 1). Hence:

1. No two-core diamond–diamond profile ever beats the best one-core diamond law, at ANY ε.
2. The diamond–diamond subclass minimum equals the one-core diamond minimum for every ε.
3. Consequently, any genuine two-core improvement at any ε must use a NON-diamond core shape (square, rounded, nonconvex canonical, or genuinely nonparallel levels). Diamond–diamond competition is completely inert.

The same statement holds verbatim for N-level all-diamond profiles with any number of gaps, since f238 covers arbitrary gap collections (finite or infinite) at fixed core.

## 4. Consistency checks actually run

Exact Fraction computations at m ∈ {1/63, 1/14, 1/13, 1/10, 1/4, 1/2, 1, 2} on a 0.02-spaced grid over `(g_0, g_1)` with `g_1>=g_0+1` confirmed: the grid minimum always coincides with the one-core diamond minimum and is attained exactly on the degenerate line `g_1=g_0+1` at the grid point nearest g*; off the line the cost is strictly larger. An earlier version of the grid code used a WRONG tail normalization (`E|C_0+GD|` in place of `|C_0|` at level 0); it is disclosed as erroneous and non-evidence. These grid checks are diagnostics only; the proposition rests on the cited adopted theorem and the identification in §2.

## 5. What remains open (unchanged)

* Non-diamond two-core N=2 competition (square/rounded/nonconvex last cores, mixed shapes) — the genuine content of option (ii).
* `0<ε<ε0` one-core failure/extension (option (i)) — not attacked, per Main's release requirement.
* Global N=2 solution, ε0-maximality, V value below ε0, source/book equivalence, novelty — all open.

This note closes only the diamond–diamond subclass. It does not use the withdrawn 18:35 adoption as a settled premise: the scalar minimization fact cited in §1 predates and is independent of that withdrawal (it is the candidate's §3 sign computation, adopted within the prospective-acceptance record's scope and independently reconstructible by Descartes' rule and three sign evaluations).
