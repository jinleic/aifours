# Erratum 3 to `proof/me3-theorem-v5.md` (wording only; amends errata 1 and 2)

Worker `MathPhaseType3`, 2026-10-18 PDT. This is a static erratum, created as a new file. It changes no file and
involves no computation.

**Frozen and unchanged (sha256):**
* `proof/me3-theorem-v5.md`: 1504ec692f2b0e26e2292e789c79ebde65f4f9ce171343a52ca9ce39d83cec60
* `proof/me3-theorem-v5-erratum-1.md`: 9f1e72e8220c61afe5bb2247cfd53c927dfb45c6ebd6e0506f77634bdac8e7b4
* `proof/me3-theorem-v5-erratum-2.md`: bef33e9103e9b8e39ea79547f937024d791cf8c434b01a018eeda035f698243b
* `proof/charts-spec-v2.md`: d401774ec8c531560dd2e2cf3de52249547b6737dab5f14245a5da3e1acd5437
* `reductions/proof/reductions-v4.md` (be1f7190…6eb1) and its erratum 1 (4e5564eb…1085)
* every spec, run, certificate, audit and receipt
* pin v3 (`receipts/me3-candidate-pin-v3.json`, fa9327f2b35c31544128e612c55024caf97540d9fe05bdaf184861d8604d8b4b)

There is no re-pin, on the parent's instruction.

**Source.** `institute/runs/six-lane-2026-10-16/review/me3-v5-erratum2-codex-v1.note.md`, sha256
d7c7b735ce5ddaa2976c4b31ae313a43c4b8fa0222f26f7e6e36ab949b7c9605.
* Verdict: ACCEPT-WITH-FIXES, with 0 FATAL, 0 MAJOR and 3 MINOR findings, all about wording.
* Every one of m1–m8 is answered, and the precedence erratum 2 > erratum 1 > v5 is unambiguous.
* The review's SOURCE numbers follow its prompt manifest (`me3-v5-erratum2-codex-v1.prompt.txt`, LF7–13): SOURCE00 is
  erratum 2, SOURCE01 is erratum 1, SOURCE02 is v5 and SOURCE05 is charts-spec-v2. "LF n" below means line n of the
  named file.

**Precedence.** Erratum 3 > erratum 2 > erratum 1 > v5. Erratum 3 amends only the passages listed below. Everything
else reads as in erratum 2, including its precedence table.

## F1 (MINOR 1). The domain of Q_T — erratum 2 LF107–108

**Old (verbatim, erratum 2 LF107–108):**

```
**Lemma D.** Fix δ ≥ 0 and ω > 0, and put ξ = δ − iω. Let K be as at LF124 (with m1). For y > 0 put
Q_T(y) := (κy² − 2y + 2)/y³, and for θ > 0 put W(θ) := Q_T(θ(1+ξ))/Q_T(θ). Suppose that for every θ > 0, W(θ) has a
```

**New (replaces those two lines; the statement continues unchanged with "representation" at erratum 2 LF109):**

```
**Lemma D.** Fix δ ≥ 0 and ω > 0, and put ξ = δ − iω. Let K be as at LF124 (with m1). For z ∈ ℂ∖{0} put
N(z) := κz² − 2z + 2 and Q_T(z) := N(z)/z³ = (κz² − 2z + 2)/z³; for real y > 0, Q_T(y) > 0 (step (b)). For θ > 0 put
W(θ) := Q_T(θ(1+ξ))/Q_T(θ), which is well defined because θ(1+ξ) ≠ 0 (Re(1+ξ) = 1 + δ > 0) and Q_T(θ) > 0. Suppose
that for every θ > 0, W(θ) has a
```

* Step (a) of the proof is unchanged. It uses Q_T at the complex points θz with Re z > 0, which are nonzero.
* Step (b) is unchanged. It is the positivity statement for real arguments only: N > 0 on ℝ, so Q_T(y) > 0 for y > 0.

## F2 (MINOR 2). The δ = 0 aside — erratum 2 LF286–287 and erratum 1 LF83–84

The individual CERT predicates are valid at the δ = 0 points of their boxes. A D1 conclusion for a whole cone,
however, needs every test centre to be covered. Erratum 2 LF285 ("Points with δ = 0 are D1 and are handled by
Cor 5.7.") is unchanged.

**Old (verbatim, erratum 2 LF286–287):**

```
  * The dual certificates are also valid there, since Lemma D allows δ = 0. That consequence (SCV ≥ T on those D1
    cones) is consistent with L5 but is not used (Claude m6, consistency probe).
```

**New (replaces erratum 2 LF286–287):**

```
  * Individual CERT predicates remain valid at the δ = 0 points of their boxes, since Lemma D's certificate forms allow
    δ = 0. Each certifies the representation of W(θ) only at the test centres θ = s/(1−s) of those points. A whole D1
    cone (δ = 0, fixed ω) gets SCV ≥ T from Lemma D only if every s ∈ (0, 1) at that pole lies in CERT leaves, i.e.
    complete CERT coverage. Examples:
    * 0 < ω ≤ 1/5: SWC, all of whose leaves are CERT;
    * ω > 40: G, whose SKIP boxes all have ω_h ≤ 40, and LW, all of whose leaves are CERT.
    An unrestricted reading is false. The D1 ray with ω = 1, cos φ = 35/37 and sin φ = 12/37 has
    SCV = 773/3844 < T (reductions-v4 Thm 5.6). So at (δ, ω) = (0, 1) ∈ P̄ some s ∈ (0, 1) lies in no CERT leaf; by the
    tiling it lies only in G SKIP leaves. The restricted consequence is consistent with L5 (Lemma 5.4 for ω ≤ 1/5;
    Lemma 5.5 for ω ≥ 4). The assembly does not use this aside: every δ = 0 pole is handled by Cor 5.7.
```

**Old (verbatim, erratum 1 LF83–84; the review's "SOURCE01:83–84"):**

```
No change is needed for δ = 0 points of CERT leaves (G, SWC, LW). Lemma D holds for every δ ≥ 0, so those D1
configurations get SCV ≥ T, and Cor 5.7 also applies.
```

**New (replaces erratum 1 LF83–84):**

```
No change is needed for δ = 0 points of CERT leaves (G, SWC, LW): their D1 poles are handled by Cor 5.7. The CERT
predicates remain valid at those points, but they give SCV ≥ T for a whole D1 cone only under complete CERT coverage
of every s ∈ (0, 1) at that pole (for example 0 < ω ≤ 1/5 or ω > 40); see erratum 3 F2.
```

**charts-spec-v2 LF83–84.** The parent's relay of this finding named charts-spec-v2 LF83–84. In this review's
numbering, however, "SOURCE01:83–84" is erratum 1 LF83–84, restricted above; charts-spec-v2 is SOURCE05.
* charts-spec-v2 LF83–84 state the LD s-union (δ ≥ 64). They make no D1 or δ = 0 claim.
* Its coverage section (LF86–96) is stated for D2 poles only (δ > 0, LF86).
* So no restriction is needed there. For the avoidance of doubt: the δ = 0 points of any chart box are read as in F2.

**Checks on the examples.**
* For ω ≤ 1/5, Lemma 5.4 with Lemma 4.2 gives SCV ≥ (553/2000 − 1/25)/(1 + 1/25) = 11825/52000 > 11/50.
* For ω ≥ 4, Lemma 5.5 gives SCV > 0.33 > 11/50.
* At ω = 1, 773/3844 < 11/50.

## F3 (MINOR 3). Coefficient notation — erratum 2 LF376–377

**Old (verbatim, erratum 2 LF376–377):**

```
  * Its coefficient on e^{−t} is a > 0: by Lemma 6.1 for D2, and for D1 by Lemma 5.1 (a ≥ √(b² + c²) > 0, as the pair
    contributes).
```

**New (replaces erratum 2 LF376–377):**

```
  * Its coefficient on e^{−t} is a > 0: for D2 by Lemma 6.1; for D1, in the §2 notation H = a + Re(ce^{−ξt}) with
    δ = 0, Lemma 5.1 reads a ≥ |c|, and a ≥ |c| > 0 since the pair contributes (c ≠ 0).
```

**Why this is the same statement.** Lemma 5.1 writes the D1 cone with real coefficients, as
e^{−t}(a + b cos ωt + c_{5.1} sin ωt) with a ≥ √(b² + c_{5.1}²). In the §2 notation, b = Re c and c_{5.1} = −Im c, so
√(b² + c_{5.1}²) = |c|. Erratum 1 E1 gives the general correspondence b = Re c, b′ = −Im c.

**No such bound is claimed in D2,** where a ≥ |c| fails in general. For example, the extreme ray e^{−t}h_τ with τ > 0
has a = 1 and |c| = √(1 + r²)e^{δτ} > 1. There only a > 0 is used (Lemma 6.1).

## Passages governed by erratum 3

| Passage | Governing text |
|---|---|
| erratum 2 LF107–108 (Lemma D statement, definition of Q_T) | F1 |
| erratum 2 LF286–287 (δ = 0 aside) | F2 |
| erratum 1 LF83–84 (δ = 0 points of CERT leaves) | F2 |
| erratum 2 LF376–377 (coefficient on e^{−t}) | F3 |

The review also notes that the exact reductions-v4 sublabels and the external replay assertions remain imports,
because their files were absent from its snapshot. For information only: those files are in the lane and are bound by
pin v3 and the parent's closure files.
