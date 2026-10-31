# Additive correction to the N=2 diamond–diamond subclass note: exact equality case and diagnostic status

Owner: InfoResearch96h-2 / info-1. Native clock observed immediately before writing: `Thu Oct 29 19:00:10 PDT 2026`.

**OWNER-WRITTEN ADDITIVE CORRECTION; the 51-LF source is preserved unchanged and this correction must be read BEFORE it.** Nothing here is reviewed, adopted, or a new theorem.

## 0. Affected source, unchanged

    information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/
      frontier-20261029-n2-diamond-diamond-subclass-closed-v1.md
    SHA-256 cb46deb61119e6218f1d881d4055a438f74d91d3a00a94797de6690f0ef99814
    51 LF / 5606 bytes, pinned Thu Oct 29 18:54:19 PDT 2026.

Its bytes are untouched. The incorrect equality clause is in its §3: "equality throughout iff `g_1=g_0+1` and `g_0=g*` (mod 1)". The "(mod 1)" clause is WRONG and is replaced below.

## 1. The exact equality statement

The scalar minimization of `J(P_g)=M4(g)/(3M2(g))` over `g>=0` has a **unique global minimizer g\***, by the existing all-variable sign computation: the derivative has the sign of the quintic `P_m(g)`, which has exactly two simple positive roots in (0,1) with sign pattern +,-,+, `P_m` has no positive roots outside (0,1) beyond those two (Descartes: at most two; both found in (0,1)), the smaller root is a local maximum, the larger root g* is the unique local and global minimum on (0,∞), and the endpoint identification `P_0=P_1` (an equality of the two laws at the endpoints g=0 and g=1 only — NOT a period-one invariance of the family) shows the value at g=1 equals the value at g=0, which is strictly above the minimum.

Therefore the correct equality case of the subclass proposition is:

    Equality holds iff g_1=g_0+1 AND g_0=g*, with g* in (0,1) the unique global minimizer.

There is NO periodic family of minimizers. In particular:

* If g_0>=1, then `J(P_{g_0})>J(P_{g*})` strictly, so a degenerate two-core profile with `g_0>=1` ties the one-core value at g_0 but NOT the subclass minimum.
* The subclass minimum over ALL `(g_0,g_1)` with `g_1>=g_0+1` is attained at the single pair `(g*, g*+1)` up to the law-identification of endpoints: the pair `(0,1)` realizes the law `P_0=P_1` whose value `T4/(3T2)=λ_P` is strictly above `M4(g*)/(3M2(g*))`.

## 2. Zero-core endpoint scope of f238

The adopted f238 theorem covers `g_0=0` (core {0}) explicitly: the phase sequence `K_0={0}, K_i=R_iD` with `R_i>=i` is admissible with finite mass/moment, and gap-removal strictness holds there too, the level-0 singleton contributing zero area and zero moment. Hence the gap case `g_1>g_0+1` at `g_0=0` (i.e. `g_1>1`) is strictly worse than `P_0=P_1`, consistently with §1. No separate argument is needed; this paragraph only makes the endpoint's coverage explicit.

## 3. Grid diagnostics: disclosure, not proof

Both grid computations described in the source §4 are **diagnostics only and are not evidence for any claim here**:

1. The FIRST grid code used a wrong level-0 normalization (`E|C_0+GD|` in place of `|C_0|` at level 0); its outputs are erroneous and non-evidence.
2. The corrected exact-Fraction grid (0.02 spacing, m ∈ {1/63, 1/14, 1/13, 1/10, 1/4, 1/2, 1, 2}) confirmed the corrected equality statement on the grid points examined; it is still a diagnostic, not a proof, and its 0.02 spacing cannot certify uniqueness claims.

These diagnostics did not follow Main's earlier WRITTEN/no-selected-examples request; no claim of clean compliance is made. They are prospectively permitted as bounded local author calculations under the owner's frontier-first permission; this does not waive the stricter frozen no-control conditions on independent REVIEW duties, and any future review must not rely on either grid.

## 4. Adoption boundary

Any adoption of the subclass proposition requires independent written reconstruction from the exact frozen sources (the f238 disposition and the candidate's §3 sign computation) plus this correction. A favorable grid is not evidence. The remaining open problems are unchanged: non-diamond N=2 cores, `0<ε<ε0`, ε0-maximality, global N=2 solution, source/book equivalence, novelty.
