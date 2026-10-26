# Repeated-pole PH candidates — parent written check v1

Before-creation clock observed: **2026-10-23T13:06 PT**.

## Verdict

**Theorem B (explicit order-5/6 band): WRITTEN_CHECKED (in-harness level), self-contained.** Three independent written reconstructions agree: author proof, InfoResearch96h peer review (0F/0M/0m), and this parent check.

**Theorem A (all-(r,q) algebraic-degree criterion): WRITTEN_CHECKED at the declared import boundary only** — conditional on Ellard–Smigoc 2017 Theorem 1.2 (read at theorem level by parent and reviewer; its 2006 proof is not authenticated here).

**Existence-threshold candidate (proof-H12-PH-existence-threshold-v1.md): parent full read done; verdict withheld pending the assigned independent review** and the parent's own check of the O'Cinneide import usage (the Liu–Yao–Zhang v2 statement opened by the parent matches the (A1)–(A3) hypotheses the manuscript claims).

## Parent reconstruction actually performed

- Hand expansion of `(x−4t)(x²+2tx+v)² = x⁵ − U x³ − V x² − W x − Z` with `U=12t²−2v, V=16t³+4tv, W=v(16t²−v), Z=4tv²`: verified symbolically and at multiple exact rational points in the parent kernel.
- Hand expansion of `(x²−d²)(x²+b²)² = x⁶ − A x⁴ − B x² − C` with `A=d²−2b², B=b²(2d²−b²), C=d²b⁴`: verified likewise, plus the shift identity `det(sI−G)=((s+a)²−d²)((s+a)²+b²)²` giving poles −c, −(c+2d), −a±ib twice, and `P₆(a)=K(c+2d)` verified exactly.
- Conceptual re-derivation of the degree lower bound (reduced denominator divides the characteristic polynomial), the exactly-r Frobenius-block count (irreducible Metzler ⇒ real algebraically simple spectral abscissa; only −c available), and the trace obstruction `tr M² ≥ (tr M)²/n` with nonnegative off-diagonal products, valid under Jordan structure.
- The six-state cancellation `u(sI−G)⁻¹w = K(z+d)/P₆(z)` and the initial row `(d/(c+2d), a/(c+2d), 0,…,0)` summing to one via `a+d=c+2d`: checked by the parent and independently by the reviewer.

## Outstanding obligations (blocking further promotion)

1. P1 at (r,q)=(1,1) must be shown to reproduce the accepted H_{1,1} threshold `1/√3 = cot(π/3)` — a free consistency anchor the project already holds.
2. A short structural remark explaining why the repeated-pole degree-5 threshold 1/√5 is unrelated to the simple-pole cot(π/n) pattern (Frobenius-block trace obstruction vs. cyclic realization).
3. Independent review of the existence-threshold manuscript.
4. Matched prior-art comparison for both candidates (Liu–Yao–Zhang gives a criterion, not these explicit formulas; no clearance claimed).

Novelty remains **NOVELTY_UNCLEAR** everywhere. No Lean/kernel claim. The book's general minimal-PH problem remains open; β∈(1/√2, β_*) minimum-order band remains open.
