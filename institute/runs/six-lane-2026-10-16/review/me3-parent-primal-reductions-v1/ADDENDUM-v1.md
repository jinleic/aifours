# Addendum v1 — why the c02 control E2 ("drop φ from the r-derivative") is benign

ME3ParentPrimal, 2026-10-18 06:11 PDT. `RESULT-v1.json` (9a72e3e7…65e3) and `AUDIT-v1.md` (8489b589…0691) are
unchanged; this note and `RESULT-addendum-v1.json` are new.

**Algebra (exact sympy, run c03 X1).** The mutation uses L_k − φ in place of L_k. Since Re P_k = 1 − a_k,
a_k′_mut = −Re(P_k(L_k − φ)) = a_k′ + φ(1 − a_k). D is linear in (a0′, a1′, a2′), so the dropped contribution is
D_mut − D = φ·E, with E = a1a2 + a0a1 − 2a0a2 = a1(a0 + a2 − (1+S)a1). By hand (AM–GM),
a0 + a2 ≥ a1√(2(1+S)), hence E ≥ a1²√(1+S)(√2 − √(1+S)) ≥ 0 whenever S ≤ 1.

**Certified on all 8,018 DPOS leaves (parent evaluator `p_core_v1`, Arb at 128 bits, exact boxes):**
* E > 0 on every whole box by the naive ball (c03 X2). The minimum certified lower bound is 0.0890312, on cell 135,
  path 00101001.
* φ_lo ≥ 0 on every DPOS box (exact).
* S < 1, i.e. a0a2 < a1², on every box (c03 X4; this is the hypothesis of the AM–GM remark).
* DPOS with the dropped term replaced by its sign-aware worst case φE ≥ φ_lo·E_lo ≥ 0 (c04 X5):
  lower(D) + φ_lo·E_lo > 0 on 8,018/8,018 leaves. 8,017 pass directly. Cell 64, path 10101001 passes after one
  recorded bisection, and it is the same leaf that needed bisection for D > 0 in r01. The minimum bound is 0.0105.

So on every DPOS box D_mut = D + φE ≥ D > 0: the mutation cannot be rejected there. It is benign, and this is now
certified rather than inferred. It replaces the "[INFERENCE]" sentence about E2 in AUDIT-v1.

**Kept visible (not certified as stated):** c03 X3 used a plain ball product φ-ball × E-ball and got 8,016/8,018.
* Cell 128, path 00000101 failed through ball wrapping: a φ-range touching 0 gives the product a negative lower
  end, although the true range is ≥ 0.
* Cell 64, path 10101001 failed because its whole-box D enclosure is not positive.

The sign-aware X5 supersedes X3 and certifies both leaves.

Both new scripts were AST-audited before running (a02, a03): no float literals, no `float()`, no `math`.
