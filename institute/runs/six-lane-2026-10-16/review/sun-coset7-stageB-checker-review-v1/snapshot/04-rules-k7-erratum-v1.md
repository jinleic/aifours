# rules-k7-erratum-v1: two wording repairs required by the Codex written review (overlay; no frozen file edited)

- **Freeze record:** host-clock time and sha256 in `evidence/erratum-v1.sha256`.
- **Source:** `institute/runs/six-lane-2026-10-16/review/sun-coset7-written-v1-codex-v1.note.md`, sha256 6c9872c4363272243631bbec7b1475333df164517be60fcfb89ea5822d4808ea. Verdict: AWF, with no FATAL or MAJOR findings and two MINOR ones. The relayed parent message carried this hash.
- **Overlaid files:** `rules-k7-v1.md` (77b9afec…) and `rules-k7-addendum-v1.md` (fb2c306b…1066). Both stay frozen and byte-identical. Read each of them together with this file.
- **Status:**
  - All six residual classes stay OPEN.
  - The completed finite coverage is INCONCLUSIVE until the independent replay is done and reviewed.
  - FH stays UNUSED.

## W1 — rules-k7-v1 line 32 (L5, F): the subfamily size condition

**Frozen text:** "every subfamily T of the vertices meeting one H-coset has a pair with gcd(λ,λ′) ≥ |T| (Sun(|T|) in H; |T| = 7 only if H < G in the minimal frame)".

**Read instead:** for every subfamily T with **2 ≤ |T| ≤ 6** of the vertices meeting one H-coset, some pair l ≠ l′ in T has gcd(λ_l, λ_l′) ≥ |T|. This is Sun(|T|) in H, an import. The case **|T| = 7** is allowed only when H < G in a least-order CE, under the licence of README §6. A singleton has no pair, so |T| = 1 imposes no condition.

**Effect: none on any computed result.**
- L5 is used only by FH. FH is UNUSED (rules-k7-addendum-v1 §A4), and neither engine version (v1, v2, v3) implements it.
- The rules that are used already carry the condition 2 ≤ |T| explicitly: VFC (V3) says "every T ⊆ S_R with |T| ≥ 2", and Corollary VFC-count calls T allowed if |T| ≤ 1 or every T′ ⊆ T with |T′| ≥ 2 has a pair. In those rules |T| ≤ k − 1 ≤ 6, so no licence for |T| = 7 is involved.

## W2 — rules-k7-addendum-v1 line 106 (RPLP-k7): the system Farkas' lemma applies to

**Frozen text:** "If the primal system for q is infeasible, Farkas' lemma gives a direction with (★) holding with right-hand side 0 and Obj > 0. Scaled to Obj = 1, it is a (P) certificate, since 0 ≤ 1."

**Read instead:**
- **Closed relaxation.** Let P(q) be the closed system consisting of x ≥ 0 on the columns 𝒞(q) together with (E1), (E2) and (B). It **excludes (TOT)**.
- **Farkas case.** If P(q) is infeasible, Farkas' lemma gives rationals a, b (free) and u, l ≥ 0 such that the left side of (★) is ≤ 0 on every column of 𝒞(q) and Obj > 0. Scaled to Obj = 1, this vector satisfies (★) with right-hand side 0 ≤ 1. So it is a (P) certificate.
- **Strict system.** Infeasibility of the strict system "P(q) and Σx < 1" does **not** by itself give such a vector. For example, the single-variable system {x = 1, x < 1} is infeasible, while its closed part {x = 1} is feasible.
- **What the kill relies on.** The RPLP-k7 kill accepts only certificates that satisfy (★) ≤ 1 on every column of 𝒞(q) and Obj ≥ 1. Either such a vector refutes q directly, by the weak-duality argument at rules-k7-addendum-v1 lines 100–104, which is unchanged and valid as written; or it comes from Farkas applied to P(q) as above.

**Effect.** This repairs wording only. No certificate is regenerated, and no checker acceptance condition changes. The test is still (★) ≤ 1 on all columns of 𝒞(q) with Obj ≥ 1, in exact arithmetic, for every q.

[INFERENCE, from reading the engine source; not established by any run] The P-route LP in engines v1–v3 maximises c·z subject to Mz ≤ 1 and z ≥ 0. Its LP dual is "minimise Σx over P(q)". So the engine's unbounded-dual (Farkas) branch is the closed-relaxation case of W2. The independent replay must not rely on this remark; it verifies each vector directly.
