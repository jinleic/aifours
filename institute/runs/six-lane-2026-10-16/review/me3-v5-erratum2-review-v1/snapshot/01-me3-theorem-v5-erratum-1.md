# Erratum 1 to `proof/me3-theorem-v5.md` (wording and provenance only)

Worker `MathPhaseType3`, 2026-10-18 PDT. This is a static erratum, created new. It changes no file.

**Files left unchanged:**
* `proof/me3-theorem-v5.md`, sha256 1504ec692f2b0e26e2292e789c79ebde65f4f9ce171343a52ca9ce39d83cec60;
* `reductions/proof/reductions-v4.md`, sha256 be1f7190ba71f06b3e951886581d285cc74435a49e3c2983776cebb6101f6eb1;
* the chart specifications, and every certificate, run, audit and receipt;
* the candidate pin v3, `receipts/me3-candidate-pin-v3.json`, sha256
  fa9327f2b35c31544128e612c55024caf97540d9fe05bdaf184861d8604d8b4b.

This erratum was written after pin v3 and is not in its manifest. On the parent's instruction it is wording-only, so
there is no re-pin.

**Source.** The parent delta audit of pin v3:
* `institute/runs/six-lane-2026-10-16/review/me3-parent-delta-audit-v1/RESULT-v1.json`, sha256
  6947d9381ea15127a277e71ece485619f3097e5d874c65b5d1256b449ff63422;
* `AUDIT-DELTA-v1.md`, sha256 a0b4850353e438559c1bb2986fe2a3dbe987e1ce025d74ef27e8c189ed386605, the value listed in
  RESULT-v1.json.

Its verdict is COVERED-WITH-NOTES, with no GAP and 77 exact checks. Its §5 lists notes N1–N7.

**Reading rule.** Each "Old" quote is verbatim from the named file and line (LF). Where a "New" text is given, it
governs. No item changes a definition used by a proof step, a certificate, or the Theorem's statement or conclusion.

## E1 (N1). "Real span" drops the sine direction — v5 LF126 and LF21–22

The displayed definition at v5 LF124 governs. It is the one every step of §2, §4 and §5 uses:
  K := {f = e^{−t}H : H(t) = a + Re(ce^{−ξt}) with a ∈ ℝ, c ∈ ℂ, and H(t) ≥ 0 for all t ≥ 0}.
It agrees with reductions-v4 LF762–763 (Cor 7.2) and with the cone the parent dual desk derived.

The gloss after it was wrong. With real coefficients b₁, b₂, the function b₁e^{−(1+ξ)t} + b₂e^{−(1+ξ̄)t} is
real-valued only when b₁ = b₂, which leaves the cosine direction only. Witness: e^{−t}(1 − e^{−δt} sin ωt) ∈ K, with
a = 1 and c = i (coefficients ±i/2 on the complex exponentials).

* **v5 LF126.**
  * Old: "the cone of ALL nonnegative functions in the real span of e^{−t}, e^{−(1+ξ)t} and e^{−(1+ξ̄)t}."
  * New: "that is, the convex cone of ALL nonnegative functions a·e^{−t} + b·e^{−(1+δ)t}cos ωt + b′·e^{−(1+δ)t}sin ωt
    with a, b, b′ ∈ ℝ: the nonnegative functions in the real-coefficient span of e^{−t}, e^{−(1+δ)t}cos ωt and
    e^{−(1+δ)t}sin ωt. The correspondence is b = Re c and b′ = −Im c, since Re(ce^{−ξt}) = e^{−δt}(Re c·cos ωt −
    Im c·sin ωt)."
* **Addition after v5 LF130**, a second witness for the sine direction: "Likewise e^{−t}(1 − e^{−δt} sin ωt) ∈ K, with
  a = 1 and c = i."
* **v5 LF21–22.**
  * Old: "1. §2 (delta finding 1, MAJOR): K is defined explicitly as all nonnegative functions in the real span,
    restoring v3's definition."
  * New: "1. §2 (delta finding 1, MAJOR): K is defined explicitly (LF124) as the set of all nonnegative
    e^{−t}[a + Re(ce^{−ξt})] with a ∈ ℝ and c ∈ ℂ, i.e. all nonnegative functions in the real-coefficient span of
    e^{−t}, e^{−(1+δ)t}cos ωt and e^{−(1+δ)t}sin ωt. This restores v3's definition."

## E2 (N2). Parent-audit provenance overstated — v5 LF74–75, and LF335

* **v5 LF74–75.**
  * Old: "The parent audit passed reductions v1/v2: `review/me3-parent-primal-reductions-v1/RESULT-v1.json`, sha
    9a72e3e7133de30301785af96604b31838b9726d94055717291f3111744c65e3, run x01-red-checks."
  * New: "The parent primal desk audited reductions v1: `review/me3-parent-primal-reductions-v1/RESULT-v1.json`, sha
    9a72e3e7133de30301785af96604b31838b9726d94055717291f3111744c65e3, run x01-red-checks. Of the reductions files, it
    rehashed only `reductions-v1.md`, `vcos-lower-bound-v1.md` and `STATUS.md`; it was written at 06:05, before
    reductions v2 existed. The deltas reductions v1→v2→v3→v4 (and theorem v3→v4→v5) are covered by the parent delta
    audit,
    `review/me3-parent-delta-audit-v1/RESULT-v1.json` (sha 6947d938…3422), with verdict COVERED-WITH-NOTES and no
    GAP."
* **v5 LF335.**
  * Old: "  * reductions audit: PASS."
  * New: "  * reductions audit (reductions v1): PASS. For v2–v4, see the parent delta audit above."

## E3 (N4). G's SKIP boxes — v5 LF228–230 and LF23–24

G's δ-range starts at δ = 0. A `SKIP:in-primal-P` box can therefore contain δ = 0 points. Those are D1
configurations, and Lemma M (stated for r₀ > 0) does not apply to them.

* **v5 LF228–230.**
  * Old: "So all their pole configurations lie in P and are handled by Lemma M (§3), not by Lemma D."
  * New: "So all their pole configurations lie in P (a closed set), and none is handled by Lemma D.
    * Those with δ > 0 are D2 configurations assigned to P. Lemma M (§3) supplies Cor 7.2's hypothesis, and Cor 7.2
      gives SCV > v_cos on the whole cone (§5).
    * Those with δ = 0 are D1 configurations, handled by Cor 5.7 (SCV ≥ v_cos)."
* **v5 LF23–24.**
  * Old: "G's SKIP leaves are covered by P (Lemma M);"
  * New: "G's SKIP leaves lie in P: their δ > 0 points are handled by Lemma M with Cor 7.2, and their δ = 0 points (D1)
    by Cor 5.7;"

No change is needed for δ = 0 points of CERT leaves (G, SWC, LW). Lemma D holds for every δ ≥ 0, so those D1
configurations get SCV ≥ T, and Cor 5.7 also applies.

## E4 (N5). The reductions-v4 header still describes the file as v2 — reductions-v4 LF48–55

The file title (reductions-v4 LF1) and its status paragraphs (LF3–35, explained at LF34–35 and LF45) identify the
document as v4. Only the inherited LF48–55 header was not updated. Read:

* **LF50.**
  * Old: "(host-clock times are in `../STATUS-v2.md`)"
  * New: "(host-clock times are in `../STATUS-v4.md`; earlier ones are in `../STATUS.md`, `../STATUS-v2.md` and
    `../STATUS-v3.md`)"
* **LF51–52.**
  * Old: "This v2 supersedes `reductions-v1.md`, which is kept unchanged (sha256 ad6c5091…5536)."
  * New: "This file is reductions v4 (sha256 be1f7190…6eb1). It supersedes reductions v1, v2 and v3, which are kept
    unchanged (sha256 ad6c5091…5536, bd497389…1e3f and e5c75b24…b15c)."
* **LF55.**
  * Old: "Labels used in v2:"
  * New: "Labels used in v4 (as defined in v2; unchanged):"

## E5 (N6). The density clause is a consequence, not a hypothesis — v5 LF55

* **v5 LF55.**
  * Old: "**Theorem.** Let X be a continuous ME(≤3) law; its density f satisfies f ≥ 0, ∫f = 1 and ∫(1+t²)f < ∞.
    Then"
  * New: "**Theorem.** Let X be a continuous ME(≤3) law with density f. Then"
* **Remark, added after the statement:**
  * The properties f ≥ 0, ∫f = 1 and ∫(1+t²)f < ∞ are consequences, not hypotheses. Reductions-v4 Theorem L1(a)(3)
    (LF148) shows that f = −αAe^{At}𝟙 is a density of X with f ≥ 0 on [0, ∞), ∫₀^∞ f = 1 and all moments finite.
  * The Theorem assumes only the contract's setting: HSTZ 2016 Definitions 1, 2 and 5, i.e. continuous X with an ME
    representation of order ≤ 3.
  * The "positive-mass hypothesis" at v5 LF78–79 is a hypothesis of the general measure-theoretic statements
    (reductions-v4 §0.2 and Lemmas 2.2–2.3). Every ME(≤3) density satisfies it (∫f = 1; Remark 2.3a), so it adds
    nothing to the Theorem.

## E6 (N3; not in the parent's list, added for completeness). The Lemma M proof is abbreviated — v5 LF158–162

The v5 text omits two justifications that v3 §3 gave: the continuity and C¹ regularity of σ, and the reason a covering
leaf must be DPOS. The argument is unchanged. The governing full proof, identical in substance to v3 §3 (LF102–112;
v3 is invalid only for its SWC chart evidence), is:

1. If S(r₀, ω₀, φ₀) ≥ T, we are done, since T > 773/3844 ≥ v_cos. Otherwise put σ(r) := S(r, ω₀, φ₀) for r ∈ [0, r₀];
   then σ(r₀) < T.
2. **Feasibility.** For 0 < r ≤ r₀, φ₀ ≤ θ₁(r₀) ≤ θ₁(r), because θ₁ is decreasing (reductions L6, Lemma 6.5), so
   (r, ω₀, φ₀) is feasible. The point r = 0 is the D1 ray e^{−t}(1 − cos(ω₀t − φ₀)), defined for every φ₀.
   **Containment.** Every such point lies in R_P: r ≤ r₀ ≤ 3, ω₀ ∈ [1/5, 40] and φ₀ ≤ θ₁(r₀) < 2π < 31416/5000.
3. **Regularity.** The moments a_k = 1 − Re(cζ^{k+1}) are analytic in (r, ω, φ), including at r = 0, where they reduce
   to the D1 moments (reductions Lemmas 6.6 and 5.2). Along the path, a₁ = m₁ > 0, since each point is a nonzero
   nonnegative density. So σ = 2a₀a₂/a₁² − 1 is continuous on [0, r₀] and C¹ on (0, r₀].
4. Let J := {r ∈ [0, r₀] : σ < T on [r, r₀]} and r* := inf J. Then r₀ ∈ J. For every r ∈ (r*, r₀] some r′ ∈ J has
   r′ < r, so σ < T on [r, r₀].
5. Take r ∈ (r*, r₀] and the point p = (r, ω₀, φ₀). Let B be any leaf box of the c03 tiling containing p; one exists by
   the tiling audits.
   * B is not INFEAS, because it contains the feasible point p.
   * B is not SGE, because S(p) = σ(r) < T.
   * Hence B is DPOS, so ∂_r S(p) > 0, i.e. σ′(r) > 0.

   Thus σ is strictly increasing on (r*, r₀].
6. Suppose r* > 0. If σ(r*) < T, continuity would give σ < T on [r* − ε, r₀] for some ε > 0, contradicting
   r* = inf J; so σ(r*) ≥ T. But by continuity and monotonicity, σ(r*) = lim_{r↓r*} σ(r) ≤ σ(r₀) < T, a
   contradiction. Hence r* = 0.
7. σ is strictly increasing on (0, r₀] and continuous at 0. So
   σ(r₀) > σ(r₀/2) ≥ σ(0) = SCV(e^{−t}(1 − cos(ω₀t − φ₀))) ≥ v_cos. ∎

## N7

No text change is needed. v5 §1 and reductions-v4 (§5, §7 and STATUS-v4) already label the U ball, the Sturm/Arb Δ₃
brackets, the θ₁ table, Theorem 5.8 and the contract-band check as optional or conditional. No assembly step uses
them.
