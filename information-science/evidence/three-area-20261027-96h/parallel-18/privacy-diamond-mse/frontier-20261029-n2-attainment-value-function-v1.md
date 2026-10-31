# N=2 attainment: the value-function route, with the corrected two-line pointwise rule

Owner: InfoResearch96h-2 / info-1. Native clock observed before drafting: `Thu Oct 29 19:55:30 PDT 2026`.

**AUTHOR-WRITTEN, UNREVIEWED.** This packet establishes the EXISTENCE half of the f273-packet §5 item 1: attainment for (t_0,t_1) under the coupling, hence solvability of the coupled system — via a selection-free value function, avoiding profile-uniqueness issues. Uniqueness of the minimizing pair remains open, as does the standing condition itself.

**Standing condition (assumed in Theorems B–C, stated nowhere implicitly):** the actual-value cutoff is 2, i.e. `1<sqrt(2V)<=2`. Equivalently V>1/2. Whether this EVER holds is OPEN and is not attacked. No use of V<=1/2 is made anywhere (that fact is known only for ε>=ε0, where the N=2 system is vacuous).

**Mandatory read order:** this packet's premise is the f261 machinery (B1)–(B5) as corrected by addenda `6b8af7b2…` and `89f91e90…`, PLUS the self-found slack-case erratum `frontier-20261029-n2-coupled-complementarity-system-v1-addendum-1-slack-case-v1.md`, SHA `0b6e1c166f7b83479d50e8d4ad49b929af0536f6c0f2dd4933498357984f9f5d` (pinned 19:55:09), which corrects the source `d099eb4c…` §4 (P1)/(P2). The two blocks' regime boundaries do NOT coincide and are never assumed to: the slack case uses each block's OWN root; the active case uses the pooled root R_1.

## 1. Setup and the corrected pointwise rule

Fix ε>0, b=e^(−ε), m=b/(1−b), v=m(1+m), T2=m+2m², and λ>=0. Canonical profile boxes: B_0(y)=[t_0,2t_0−y] on [0,t_0]; B_1(y)=[t_1,2t_1−y] on [0,t_1]; coupling floors as in (CPL). Roots: R_0(y)=sqrt(max(λ−y²,0)), R_1(y)=sqrt(max(λ−v−y²,0))−m. At each height the joint block objective is separable convex in (F_0,F_1); by the addendum's two-line rule the pointwise minimum VALUE is

    m(y;t_0,t_1,λ)=min{ slack(y), active(y) },

    slack(y)=ψ_0(Π_0,y)+ψ_1(Π_1,y)   [used when Π_1>=Π_0+1],
    active(y)=ψ_0(S*,y)+ψ_1(S*+1,y), S*=proj(R_1, [max(t_0,t_1−1),min(2t_0−y,2t_1−y−1)]),

with ψ_0(z,y)=(z³−y³)/3+y²(z−y)−λ(z−y) and ψ_1(z,y)=T2 z+m(z²+y²)+z³/3+y²z−4y³/3−λ(z−y); on the corner interval (t_0,t_0+1/2] only the one-variable clip of R_1 enters; on (t_0+1/2,t_1] the free tail clip. (Constant-in-profile terms of the blocks are separate.)

Define the VALUE function on the admissible triangle A={t_0>=0, t_1>=t_0+1/2}:

    h_λ(t_0,t_1) := (1−b)·8∫_0^{t_0} m_0(y;t_0,λ)dy   [block-0 pointwise-min value]
                  + b·[const_λ(t_1) + 8∫_0^{t_1} m_1(y;t_0,t_1,λ)dy],

i.e. the exact minimum of H_λ=N−λZ over ALL profile pairs with parameters (t_0,t_1). This is selection-free: profile multiplicity (isolated, by joint convexity same-H segments) cannot affect h_λ.

## 2. Theorem A — continuity, coercivity, attainment of min_A h_λ (for every λ>=0, no standing condition)

(i) h_λ is finite and continuous on A. At each (y,λ), m and the block integrands are minima of finitely many continuous functions of (t_0,t_1) (the two-line rule's candidate values, with endpoints max/min of continuous functions); on any box 0<=t_i<=T the integrands are dominated by C(T,λ)·1_{[0,T]}, so dominated convergence applies to the moving-limit integrals, including the moving interval endpoints t_0, t_1 and the corner subinterval. The constant part const_λ(t_1)=(2/3)T4+(16/3)t_1T3+4t_1²T2−λ(8t_1m+2T2) is continuous.

(ii) h_λ is coercive on A: h_λ(t_0,t_1) >= (1−b)β_0(t_0)+bβ_1(t_1) with each β_i continuous, bounded below on [0,∞), and →+∞ quartically. For block 0: the pointwise min is at z=t_0 once t_0>=2sqrt(λ) (the box then lies above the root R_0), so

    β_0(t_0) >= 8∫_0^{t_0}[(t_0³−y³)/3 − λt_0]dy = 2t_0⁴ − 4λt_0² → +∞,

using y²(t_0−y)>=0 and −λ(t_0−y)>=−λt_0 on [0,t_0]. For the tail block the same argument at z=t_1 plus the positive 4t_1²T2 term dominates its λ-linear part. Since t_0+t_1→∞ in A forces t_0→∞ or t_1→∞, h_λ→+∞.

(iii) A is closed and h_λ continuous coercive, so sublevel sets are compact and min_A h_λ is ATTAINED for every λ>=0. (Includes the corner boundary t_1=t_0+1/2 and the slack region t_1>=t_0+1 by construction of the rule; t_0=0 gives the degenerate C_0={0} block with zero area, handled by the empty integral.)

## 3. Theorem B — V-characterization and existence of an optimal (t_0,t_1) pair (STANDING CONDITION assumed)

Assume 1<sqrt(2V)<=2. Then:

(i) Z>=2bT2>0 for EVERY admissible pair: the tail mass Z_tail>=2T2>0 (the j>=1 shells of the exact tail always contribute), and Z=(1−b)A_0+b·Z_tail.

(ii) m(λ):=min_A h_λ is finite, continuous, strictly decreasing with m(λ')<=m(λ)−(λ'−λ)·2bT2 for λ'>λ. (Evaluate the λ'-rule pair at a λ-minimizer and compare with the λ-rule pair, whose Z>=2bT2.)

(iii) m(0)>0 (all feasible N>0 since V>0), m(λ)<0 for λ>V (the f261-attained optimal pair has H_λ=(V−λ)Z<0, and h_λ at its parameters is <= that), and m(V)=0 (every explicit-rule pair is feasible with H_V>=0, so h_V>=0; the attained optimum gives equality). Hence V is the UNIQUE root of m(λ)=0.

(iv) Let t̂ attain m(V)=0 (exists by Theorem A at λ=V) and let (F̂_0,F̂_1) be ANY measurable selection of pointwise minimizers there (piecewise-continuous selections exist). The pair is feasible with parameters t̂, and H_V(F̂)=h_V(t̂)=0, so N(F̂)/Z(F̂)=V exactly: an EXPLICIT optimal pair exists in the two-scalar family, and the coupled first-variation/complementarity system (corrected rule) has a solution. No selection ambiguity affects the VALUE: any two selections give H_V=0 hence the same ratio V.

## 4. What remains open (unchanged, plus this packet's boundary)

1. UNIQUENESS of the minimizing (t_0,t_1) — no convexity/monotonicity analogue of the N=1 single-regime argument is established; the two blocks' different regime boundaries (the t_0-block root R_0 has no m-shift) block a direct transplant.
2. The standing condition: whether V>1/2 ever holds (equivalently the cutoff ever exceeds 1) is open; all N=2 statements here are conditional on it.
3. Deriving the explicit two scalar envelope equations (P3') from the corrected rule, including the newly identified slack branches (F_0=R_0 with F_1 at its lower box), and their joint solution — not done.
4. Everything previously open (ε<ε0, ε0-maximality, source/book equivalence, novelty, unconditional f261) remains open.

## 5. Diagnostics

None run for this packet beyond the written argument: no grid, no float probe. The exact-rational counterexample inside the erratum addendum (t_0=1/10,t_1=7/10,R_0=2,R_1=13/10) is arithmetic verification of the slack-case defect only. An earlier throwaway symbolic script's crash was already disclosed in the source packet §6.

## 6. Status

AUTHOR-WRITTEN, UNREVIEWED, NOT ADOPTED. Premises: f261 (B1)–(B5) with its two mandatory corrections, the prospective N=1 acceptance is NOT used, the source packet d099eb4c §2–§3 pooled-root analysis, and the erratum addendum 0b6e1c16. Standard imports: dominated convergence, Berge-type value continuity for jointly convex programs with continuously varying compact feasible sets, Weierstrass. All historical NONINPUT boundaries hold; the 0<ε<ε0 range is not attacked.
