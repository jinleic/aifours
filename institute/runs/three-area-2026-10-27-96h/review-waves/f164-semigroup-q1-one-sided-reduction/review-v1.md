# Review v1 — wave `f164-semigroup-q1-one-sided-reduction`

* Reviewer: `ReviewF164SemigroupQ1` (independent same-harness review). Clock observed with `/bin/date` immediately before this file was written: **Thu Oct 29 08:06:42 PDT 2026**.
* Manifest: `manifest-v1.json`, SHA-256 `ba256a23ffb62d2e6bc9233fee603bf1a39c05a615f8f0fc7b56860782ac8d2e` (equals the value in my task). Author: MathSemigroup-2.
* **Nature of this review.** Same-harness review by an agent of the same model family as the author. It is **not** a human referee report, **not** an independent-model-family review, **not** formal/kernel verification and **not** a novelty or priority assessment. Author "PASS"/"verified"/"exact control" statements were not used as evidence; no author script was executed. No solver was used.

## 0. Bottom line

**Counts: FATAL 0 / MAJOR 1 / MINOR 5.**

The band-level Kimura-type theorem, the source-level theorem (λ_S ⊆ R, ρ_S ⊆ L, both inside ker q, λ_S ∩ ρ_S = Δ via H ∩ ker q = Δ, one-sided original quotients), the duality reduction "Q1 for all original sources ⟺ Q1 for right-regular-local (RRL) sources", the Fact-1-conditional equivalence with "separation of same-fibre R-related idempotents by *some* SN host", and the instance lemma `exeyexe = eyexe` are correct; I reconstructed each proof and checked it on explicit finite semigroups I built myself. One step is missing. The last reformulation, "separation by **the canonical RIGHTSN host**" (the source note §3 final clause; the matching note's item 4 and its "4⇔3"), needs the canonical host over the source's actor q to be universal for hosts with *arbitrary* CS actors. The bundle never proves this (**MAJOR M1**). It is repairable: I sketch a repair in §7 and illustrate it numerically. Every host-level step also relies on a "physical host" convention that the bundle never defines. Q1 itself remains open.

## 1. Inputs and read order

All bytes were verified at Thu Oct 29 06:54:26 PDT 2026 (SHA-256, byte count, LF count; CR count 0; last byte LF), before any interpretation. Every file was read completely with an exact `:raw` read, erratum first.

| # | file (…/parallel-18/semigroup-embedding/) | role | SHA-256 | bytes | LF |
|---|---|---|---|---|---|
| 1 | frontier-20261028-natural-order-weu-audit-erratum-v1.md | mandatory erratum | 801f699b…c345c28 | 4943 | 31 |
| 2 | frontier-20261029-SN-kimura-decomposition-v1.md | band theorem | 06abe46d…30eb5b6 | 5060 | 37 |
| 3 | frontier-20261029-source-onesided-reduction-v1.md | source reduction | 40668a70…ca63 | 5264 | 31 |
| 4 | frontier-20261029-matching-onesided-equals-Q1-v1.md | equivalence | 64ad0ee9…619a | 3295 | 24 |
| 5 | frontier-20261029-rightSN-instance-lemma-and-canonical-certificates-v1.md | instance lemma | d50d288d…cf9dd2ec | 4058 | 23 |

The inputs contain no certificate JSON. The full hashes are in `rf164-receipt-v1.txt`.

## 2. Conventions (Green's relations spelled out)

For a semigroup S:
* `a R b ⟺ aS¹ = bS¹`, `a L b ⟺ S¹a = S¹b`, and `H = R ∩ L`. R is always a left congruence and L a right congruence.
* For idempotents: `e R f ⟺ ef = f, fe = e`, `e L f ⟺ ef = e, fe = f`, and `e ≤ f ⟺ e = ef = fe`. In a band every H-class is a singleton.
* Local monoid: `eBe = {x : exe = x} = {x : x ≤ e}`. Local band: `E(gSg) = {x ∈ E(S) : gxg = x}`.
* Natural (Nambooripad) order, as set by the erratum: `a ≤ b ⟺ a = eb = bf` for idempotents e, f that may differ. WEU means E(S) is upward closed for this order.

**Original source** (bundle definition):
* S is regular;
* q: S → D is onto and idempotent-pure, with D completely simple (CS);
* every E(gSg) is a regular band, i.e. satisfies `abaca = abca`.

RRL/LRL mean that all E(gSg) are right regular (`xyx = yx`) or left regular (`xyx = xy`). LEFTSN/RIGHTSN bands are bands whose local monoids are left/right regular.

## 3. Erratum (read first; applied throughout)

* **E1. Two-witness natural order.** WRITTEN_SUPPORTED. arXiv:1207.4296 (Kudryavtseva–Lawson), p.2, prints "a ≤ b if and only if a = eb = bf for some idempotents e and f". I checked this in the downloaded PDF, so the citation locates the definition exactly.
* **E2. Four-element table.** WRITTEN_SUPPORTED. The table is associative and regular, with E = {0,1,3}. We have 0 = 0·2 = 2·3 and 2² = 1, and no idempotent e satisfies e2 = 2e = e. So the simultaneous test misses 0 ≤ 2 (**NEG-8**), while the two-witness test finds 0 ≤ 2 with 2 ∉ E. The semigroup is therefore not WEU.
* **E3. A pure map to a CS semigroup gives WEU.** WRITTEN_SUPPORTED. If `e = us = sv` (e, u, v idempotent), then `q(e) = q(u)q(s) = q(s)q(v)`, so q(e) ≤ q(s) in D. On a CS semigroup the natural order is equality (checked on 7 CS semigroups: D8, D4r, D4c, Z2, Z3, D12 and the 2×2 rectangular band). Hence q(s) = q(e) is idempotent, and purity gives s ∈ E.
  The Rees-row repair also checks out: `a = eb` gives row(a) = row(e) and `a = bf` gives row(a) = row(b). With `e = (i, p_{λi}⁻¹, λ)` and `b = (i, g, μ)`, we get `eb = b`, so a = b.
* **E4. Transformation-semigroup counts 687 / 321 / 145.** WRITTEN_SUPPORTED for the three numbers, which I reproduced independently: 687 distinct subsemigroups generated by at most 3 maps on 3 points, 321 of them regular, 145 of those WEU under the two-witness order. The wrong simultaneous test would call 218 of the 321 WEU. The further claim "none of those 145 had non-CS actual q" was **not reviewed**, because "actual q" is undefined in the bundle.
* **E5.** The erratum's statements about S68, the 68-source checker, the Horn scripts, the q1 finite-product note and the upper-cone note concern files outside this bundle. I did not review them, and nothing below depends on them.

## 4. Kimura-type decomposition note (K)

### Reconstruction

Let B be a band whose local monoids are regular.

**Step 1.** Work in a regular band M with x R y, i.e. x = yx and y = xy. Then:
* xwy = (yx)wy = y·x·w·y;
* by the regular identity with letters (y, x, w), yxwy = yxywy;
* yxy = (yx)y = xy = y, so the author's "y = yxy" is correct.

Hence `xwy = ywy`. Dually, x L y gives `xwy = xwx`.

**Step 2.** Take x, y ∈ eBe with x R y, and z ∈ B. Put w = eze ∈ eBe.
* xzy = (xe)z(ey) = xwy = ywy = yzy.
* So (xz)(yz) = yzyz = yz, and symmetrically (yz)(xz) = xz. Hence xz R yz.
* R is a left congruence, so uxv R uyv for all u, v ∈ B¹.
* λ is the equivalence closure of these translates, so λ ⊆ R. Dually ρ ⊆ L.
* λ ∩ ρ ⊆ H = Δ.

**Step 3.**
* For M = eBe, the local monoids of M are fMf = fBf (f ≤ e), which are regular. Any two R-related elements of M lie in the common local monoid M. So Step 2 applied inside M makes R_M a congruence.
* In every band xyx R xy, because (xyx)(xy) = xy and (xy)(xyx) = xyx. Hence M/R_M is left regular.
* The local monoid of B/λ at [e] is π(eBe). Since R_M ⊆ λ, it is a quotient of M/R_M, so it is left regular.
* **Leastness.** Left regular local monoids are R-trivial (y = xy = xyx = yx = x). So any congruence κ with LEFTSN quotient contains every local R-pair, giving λ ⊆ κ.

**Subdirect embedding and converse.**
* λ ∩ ρ = Δ gives the subdirect embedding B ↪ B/λ × B/ρ.
* Left regular bands are regular, since zxzyz = (zx)yz = zxyz; right regular bands likewise.
* SN is equationally defined (`exeyexezexe = exeyezexe`), so it is closed under products and subbands. Every subdirect product of a LEFTSN and a RIGHTSN band is therefore SN.

### Controls (from `rf164-controls-v1.log.txt`)

**Exhaustive small bands.**
* I enumerated every band of order ≤ 5. Labelled counts: 1, 4, 35, 604, 16727. Isomorphism classes: 1, 3, 10, 46, 251. For each order the orbit–stabiliser sum equals the labelled count.
* I added B¹ for every class, giving **622 bands** of order ≤ 6; 620 are SN, and 2 of those 620 are SN but not regular.
* For every SN band all of the following hold: λ ⊆ R; ρ ⊆ L; λ ∩ ρ = Δ; λ and ρ are congruences; B/λ is LEFTSN; B/ρ is RIGHTSN; the internals of Steps 1–3 check out; λ and ρ are invariant under every automorphism.
* Over the full congruence lattices (8371 congruences across all 622 bands; the first two checks below apply to the 620 SN bands, the third to all 622):
  * B/θ is LEFTSN ⟺ λ ⊆ θ, and B/θ is RIGHTSN ⟺ ρ ⊆ θ. The 1421 congruences with a non-LEFTSN quotient are the negative side of this biconditional.
  * (λ∨θ) ∩ (ρ∨θ) = θ for every θ. This also follows from K1 applied to B/θ, because λ_{B/θ} = (λ∨θ)/θ.
  * The §3(c) criterion "θ = Δ ⟺ θ separates comparable pairs, R-pairs and L-pairs" holds for all 622 bands.
* For all 622 bands, RIGHTSN ⟺ ∀e,x,y `exeyexe = eyexe`, and LEFTSN ⟺ ∀e,x,y `exeyexe = exeye`.
* **Converse.** All 2601 products L × R with |L|, |R| ≤ 4 (L LEFTSN, R RIGHTSN) are SN.

**Free band F3** (my own Green–Rees normal form):
* |F3| = 159; it is a band and SN but **not** regular.
* It has 84 local R-pairs and 84 local L-pairs, and |F3/λ| = |F3/ρ| = 51.
* All K checks hold, plus 150 random principal congruences.

**Negative controls.**
* **NEG-1 (local regularity dropped).** F3¹ is not SN: its local monoid at 1 is F3¹, which fails abaca = abca. In that local monoid ab R aba, but (ab)c(aba) ≠ (aba)c(aba), so Step 1 fails. And abac λ abc although the two are not R-related, so λ ⊄ R. This fails for the intended reason.
* **NEG-9 (checker sanity).** On F2¹ the checker correctly reports "λ ⊆ L" and "R ∩ R = Δ" as false.

### Verdicts (K)

* **K1** (λ ⊆ R, ρ ⊆ L, λ ∩ ρ = Δ): WRITTEN_SUPPORTED.
* **K2** (B/λ LEFTSN, B/ρ RIGHTSN, both least): WRITTEN_SUPPORTED.
* **K3** (B is a subdirect product of B/λ and B/ρ): WRITTEN_SUPPORTED.
* **K4** (converse; SN = subdirect products of LEFTSN and RIGHTSN bands): WRITTEN_SUPPORTED.
* **K5** ("for B regular this recovers Kimura's B↪B/R×B/L"): **MINOR m1.** This is false as literally stated for regular bands without an identity.
  * The left-zero band LZ2 is regular with trivial local monoids, so λ = ρ = Δ, while L is universal. B/ρ = LZ2 is not right regular (**NEG-6**).
  * Of the 248 regular non-monoid bands of order ≤ 5, 208 have λ ≠ R or ρ ≠ L.
  * The remark is true for regular band monoids (all 370 tested have λ = R and ρ = L), and for any regular B if one applies the theorem to B¹ and restricts back to B.
  * The remark is not load-bearing.
* **K6** (§3 universality `B_LEFTSN = B_SN/λ`, `B_RIGHTSN = B_SN/ρ`, and (a)): WRITTEN_SUPPORTED as a consequence of K1–K3 plus standard universal algebra. It is **conditional** on the imported canonical V-band definition (`finite-source-canonical-decision`, SHA b6f54918…, not in the bundle). "Characteristic ⇒ G-invariant" is correct for any action by automorphisms.
* **K7** (§3(b)): WRITTEN_SUPPORTED conditional on the same import, with **MINOR m2.** §3 is stated "for a semigroup S with a homomorphism r". But "e ↦ X_(1,e) is a band homomorphism" and the chain in (c) need the idempotent fibre F to be a band, which holds when r is idempotent-pure, as for original sources. For non-pure r, F can contain non-idempotents, and then efe and ef need not be idempotent. In my host model, trivial weights at idempotent actors and the multiplicativity of band coordinates on idempotent fibres hold (11 hosts, 73 RRL in-host sources).
* **K8** (§3(c)): the chain `e ≥ efe R ef L fef ≤ f` and "injective on F ⟺ separates comparable pairs, R-pairs and L-pairs" are WRITTEN_SUPPORTED. The clause "exactly decided by the semilattice Horn criterion" rests on an unreviewed import (`canonical-comparable-horn-exact`, SHA a93c69d9…) and is **INCONCLUSIVE (not reviewed)**.
* **K9** (§4 author controls): not evidence. I reproduced 159, SN, 84/84 and 51/51 independently. I did **not** reproduce the author's runs on all 12561 principal quotients or on 6186 random non-principal quotients.

## 5. Source one-sided reduction note (S)

### Reconstruction

**(1)** Let g ∈ E(S), x, y ∈ E(gSg) with x R y, and z ∈ S. Put v = gz, choose v' ∈ V(v), and let h = vv' ∈ E(S).
* x = xg, so xz = xv. Also xh = xvv' ∈ xvS and xv = xhv ∈ xhS, so xv R xh; likewise yz R yh. And gh = g·gz·v' = h.
* x ≤ g gives q(x) ≤ q(g), hence q(x) = q(g) (the CS order is trivial).
* gh = h gives q(g)q(h) = q(h), so q(h) lies in the row of q(g).
* Then q(xh) = q(h) is idempotent, so xh ∈ E by purity, and likewise yh.
* h̃ = ghg satisfies q(h̃) = q(g), so h̃ ∈ E(gSg) by purity (equally, (hg)² = hg directly).
* xhy = (xg)h(gy) = xh̃y = yh̃y = yhy, by Step 1 of K inside the regular band E(gSg).
* Hence (xh)(yh) = yh and (yh)(xh) = xh, so xh R yh, and therefore xz R yz.
* R is a left congruence, so λ_S ⊆ R.
* The generating pairs satisfy q(x) = q(g) = q(y), so λ_S ⊆ ker q.
* Dually, with v = zg, h = v'v and hg = h, we get ρ_S ⊆ L ∩ ker q.

**(2)** We have λ_S ∩ ρ_S ⊆ H ∩ ker q. Let s H t with q(s) = q(t), and choose s' ∈ V(s).
* q(s't) = q(s's) is idempotent, so s't ∈ E by purity.
* s't R s': s' = s'ss' and s ∈ tS¹, so s' ∈ s'tS¹.
* s't L s: t = ss't, so t ∈ S¹s't ⊆ S¹t, giving s't L t L s.
* s's also lies in the H-class R_{s'} ∩ L_s. An H-class contains at most one idempotent, so s't = s's, and t = ss't = ss's = s.

Only purity is used, so **H ∩ ker ψ = Δ for every idempotent-pure homomorphism ψ of a regular semigroup**.

The Petrich citation is **located exactly**. The pinned copy has SHA-256 0514fe1f…, matching the citation. It is Petrich, "Onesided inverses for semigroups", Acta Math. Univ. Comenianae 75(1) (2006), Lemma 2.1: "H_b contains an inverse of a iff there exist e, f ∈ E(S) such that a R e L b R f L a; then the inverse of a in H_b is unique."
* Apply it with a = t, b = s', e = ss', f = s's.
* "tt' = ss'" then takes one more line: both are the idempotent of the H-class R_t ∩ L_{s'}.
* As shown above, the lemma is not actually needed.

**(3)** λ_S ⊆ ker q, so q induces q̄: S/λ_S → D, which is onto and pure: q̄(πs) ∈ E(D) ⇒ s ∈ E.
* For each idempotent ē of S/λ_S, Lallement's lemma gives an idempotent e of S with π(e) = ē. Applied to the regular semigroup eSe, it gives E(ēS̄ē) = π(E(eSe)).
* The author instead imports the exact fibre formula E(eSe) = eF_{q(e)}e. I re-proved it: "⊆" because x ≤ e forces q(x) = q(e); "⊇" because q(efe) = q(e) forces efe ∈ E.
* π restricted to E(eSe) kills R_{E(eSe)}, because every such R-pair generates λ_S. So the local band of S/λ_S at ē is a quotient of E(eSe)/R, which is left regular.
* Dually for ρ_S.

### Host-level consequences: the reviewer's model

The bundle never defines "physical host". I used the model T(B, D) below, which is consistent with every formula the bundle displays.
* D = M[G; I, Λ; P], with G acting on the band B by automorphisms.
* Multiplication: `(b,x)(c,y) = (b·w(x,y)c, xy)`, where `w((i,g,λ),(j,h,μ)) = g p_{λj}`.

In this model:
* The product is associative, because w(x,yz) = w(x,y) and w(xy,z) = w(x,y)w(y,z).
* Elements whose actor is idempotent are idempotent, because w(x,x) = 1 when x is idempotent. Hence a faithful host always has a pure actor.
* The canonical host is `s ↦ (X_(1,s), r(s))`, with relations X_(u,st) = X_(u,s)X_(uw(s,t),t). It is universal among hosts **over the same actor** r, via X_(u,s) ↦ u·b_s.
* Products: T(B₁,D₁) × T(B₂,D₂) ≅ T(B₁×B₂, D₁×D₂).
* Opposites: Φ(b,(i,g,λ)) = (g⁻¹·b, (λ,g⁻¹,i)) is an isomorphism T(B,D)^op → T(B^op, D*), where D* = M[G; Λ, I; P*] and p*_{iλ} = p_{λi}⁻¹. I derived this for arbitrary G and checked it on 11 explicit hosts with cyclic G.
* Functoriality: T(B,D) → T(B/ρ_B, D) and T(B/λ_B, D) are homomorphisms, checked on the same 11 hosts.

### Source controls

I built **353 original sources** (sizes 1–56; all 353 verified original):
* 118 regular subsemigroups of 11 hosts T(B,D), with B ∈ {F2¹ (two actions), RB(2×2)¹ (two actions), free right regular monoid, free left regular monoid, LZ3¹} and D ∈ {D8, D4r, D4c, Z2, Z3, D12};
* 195 quotient sources S/θ(a,b) with q(a) = q(b); these need not lie in any host;
* 40 opposite sources.

Of these, 281 are RRL, 72 are not RRL, 31 are RRL with local R-pairs, 35 have both local R-pairs and local L-pairs, and 66 have λ_S ≠ Δ.

For every source the following hold:
* associativity, regularity, purity, CS target, regular local bands;
* λ_S ⊆ R, ρ_S ⊆ L, both ⊆ ker q; λ_S ∩ ρ_S = Δ; H ∩ ker q = Δ;
* WEU (two-witness order) for S, S/λ_S and S/ρ_S;
* the exact fibre formula and the Lallement lift;
* S/λ_S and S/ρ_S are original, with left/right regular local bands respectively;
* S^op swaps λ and ρ;
* for RRL sources, ρ_S = Δ and S/λ_S is locally inverse.

Internals of (1) and (2), including Petrich uniqueness and tt' = ss', were checked for every source with |S| ≤ 48.

Injectivity lemma:
* 3163 principal congruences θ(a,b) ⊆ ker q each identify two distinct idempotents.
* Over the full congruence lattices of 240 sources with |S| ≤ 12 (1809 congruences, 838 of them pure): every pure θ has H ∩ θ = Δ; every pure, idempotent-separating θ is Δ; every θ ⊆ ker q gives an original quotient.

Negative controls:
* **NEG-10.** 232 non-pure idempotent-separating congruences are nontrivial, so purity is needed.
* **NEG-2.** Z2 with the trivial actor is not pure; there H ∩ ker q ≠ Δ, and the universal congruence separates idempotents but is not Δ.
* **NEG-3.** F2¹ with q = id is pure but its target is not CS, and λ_S ⊄ ker q. Eight pairs x < g have q(x) ≠ q(g), so the CS step is needed.
* **NEG-4.** RZ2 with q = id is original with λ_S = Δ, but the congruence generated by *all* R-related idempotents leaves ker q. So the "common local band" restriction is needed.

### Verdicts (S)

* **S1** ((1)): WRITTEN_SUPPORTED.
* **S2** ((2), including H ∩ ker q = Δ): WRITTEN_SUPPORTED. The citation is exact; the cited lemma is dispensable.
* **S3** ((3)): WRITTEN_SUPPORTED. The imported fibre formula is elementary and re-proved above.
* **S4** ("Hosts combine"; "Duality ⇒ Q1 holds for all original sources iff for RRL ones"): WRITTEN_SUPPORTED, conditional on the host convention.
  * **MINOR m3.** The bundle does not define physical host, actor, weight, pure actor or canonical host. The properties these steps need (closure under products, opposites with band B^op, functoriality B → B/ρ_B, idempotent actor ⇒ idempotent element) are verified only in the reviewer's model above.
* **S5** (for RRL sources: ρ_S = Δ, and S/λ_S is locally inverse and WEU): WRITTEN_SUPPORTED. WEU follows directly from E3, so the author bridge is not needed.
* **S6** (a homomorphism into a host with pure actor is injective iff injective on idempotents): WRITTEN_SUPPORTED, with **MINOR m4.**
  * "φ(ss') = φ(ts') forces ss' = ts', likewise s's = s't, so s H t" only gives s ≤_R t and s ≤_L t. The symmetric step with t' ∈ V(t) is also needed.
  * "then s = t by (2)" must apply the argument of (2) to the pure actor of φ, not to q. The argument works there, as noted under (2).
* **S7** (conditional on Fact 1: Q1 ⟺ in every RRL source, same-q-fibre R-related idempotents are separated by *some* SN host): WRITTEN_SUPPORTED, conditional on Fact 1 and the host convention.
  * For ⇐, take the product of the Fact-1 host of S/λ_S with the separating hosts. Its actor is pure because λ_S ⊆ ker q.
  * Infinitely many factors are allowed in the model.
* **S8** ("by §3(b) this is the same as separation by the canonical RIGHTSN host"): **MAJOR M1** (§7).
* **S9** (Fact 1 citation): **MINOR m5** (§8).
* **S10** (§4 author controls: S68, 300 and 290468 random sources): not evidence; not reproduced.

## 6. Matching note (items 1–4)

* **1⇔2** (no Fact 1): WRITTEN_SUPPORTED, conditional on the host convention (m3).
  * 1⇒2 is trivial.
  * For 2⇒1: S ↪ S/λ_S × S/ρ_S; S/ρ_S is RRL; (S/λ_S)^op is RRL because S/λ_S has left regular local bands. Then use opposite and product hosts.
* **3⇒2**: WRITTEN_SUPPORTED, since RIGHTSN ⊆ SN.
* **2⇒3**: WRITTEN_SUPPORTED, conditional on Fact 1 and the host convention. I reconstructed every step:
  * ρ_B is characteristic, hence G-invariant.
  * Distinct idempotents e, f with the same idempotent actor and ρ_B-related band coordinates satisfy b_e b_f = b_e and b_f b_e = b_f (since ρ_B ⊆ L). By the trivial weight and injectivity, ef = e and fe = f, so e L f.
  * Such a pair is not λ_S-related, because λ_S ⊆ R.
  * Normal bands are RIGHTSN: in eBe, xy = exye = eyxe = yx.
  * The product actor is pure, because a faithful host's actor is pure.
  * Model check on 73 RRL in-host sources: 27 have collapses; all 64 collapsed pairs are L-related and λ_S-separated; and S → T(B/ρ_B, D) × S/λ_S is injective.
* **4⇒3**: WRITTEN_SUPPORTED, conditional on Fact 1 and the host convention. The canonical host's actor is q, which is pure.
* **3⇒4, and "4⇔3"**: **MAJOR M1.**
* **§3, "the sole remaining obligation for Q1 is item 4"**: holds only conditionally (Fact 1, host convention, and a repair of M1). "All finite examples examined … are consistent" is an author claim, not evidence.

## 7. MAJOR M1 — the canonical host's actor is not controlled

**The gap.** Kimura §3(b) compares the canonical SN and RIGHTSN hosts **over one fixed actor** r. Item 4, and the last clause of source note §3, speak of "the canonical RIGHTSN host", that is, over the source's own q ("in one actor fibre"). Proving 3⇒4 (equivalently Q1 ⇒ item 4) needs an extra step: a faithful RIGHTSN host with an arbitrary CS actor t must give separation by the canonical host over **q**. Universality over q only covers hosts whose actor is q. Neither the bundle nor any import it cites at this point supplies the step. Without it, item 4 could in principle be strictly stronger than Q1, and the advertised equivalence would not follow.

**Reviewer repair sketch** (in the model of §5; it needs writing up):
1. Every homomorphism from S to a CS semigroup has a regular, hence CS, image. A regular subsemigroup of a CS semigroup is simple with primitive idempotents, so it is CS. Therefore every CS actor t factors through q_κ: S → S/κ, where κ is the least CS congruence (it exists because the class of CS quotients is closed under subdirect products), and q also factors as q = τ_q∘q_κ.
2. Write the factor of t through q_κ as τ: S/κ → D'. Any homomorphism between normalised Rees matrix semigroups has the form τ(i,g,λ) = (α(i), u_i ω(g) v_λ, β(λ)). Then the weights transform as w'(τx, τy) = u_i ω(w(x,y)) u_j⁻¹.
3. **Pull back.** b̂_s = u_{i(s)}⁻¹·b_s turns a host over t into a host over q_κ with the same band.
4. **Push forward.** Since q = τ_q∘q_κ is pure, τ_q is pure, hence H-separating by (2), and onto. The normalised idempotents (i,1,λ₀) and (i₀,1,λ) map to the identity of their image H-class. Hence ω_q is an isomorphism. Then b'_s = u_{i(s)}·b_s gives a host over q with the same band.
5. Pairs with equal q but different q_κ-images lie in different rows or columns of q_κ(S). The rectangular band I_κ × Λ_κ, with trivial action, separates them; it is normal, so it lies in SN and RIGHTSN.
6. The product host over q, with band B × (I_κ × Λ_κ), therefore separates every same-q-fibre idempotent pair that the original host separated. By universality over q, so does the canonical V-host over q.

**Numerical illustration** (control section S6c). I checked 303 regular sources in T(F2¹, D4r), each meeting both rows, with the pure coarse actor τ onto Z2:
* the twisted map S → T(F2¹, Z2) is a homomorphism in all 303;
* twisted × rectangular coordinate is an injective homomorphism into T(F2¹ × LZ2, Z2) in all 303;
* **NEG-7:** without the twist the map fails to be a homomorphism in 301 of the 303.

This illustrates only the push-forward direction, and only in my model.

**Fix options.** Either restate item 4 as "separated by some RIGHTSN host (equivalently, by the canonical one over a suitable CS actor)", or prove the transport lemma above inside the authors' own host convention.

## 8. Fact 1: dependency map and citation

**Statements that depend on Fact 1:**
* S7 (Q1 ⟺ separation by some SN host);
* S8;
* matching items 3 and 4 and the implications 2⇒3, 4⇒3 and 3⇒4;
* the "sole remaining obligation" sentence.

**Statements that do not depend on it:**
* all of K;
* S1–S6;
* matching 1⇔2 and 3⇒2;
* the instance lemma.

**Citation: MINOR m5.** The bundle gives only "Billhardt–Szendrei 2003", plus a paraphrase ("every weakly E-unitary locally inverse semigroup embeds in a Pastijn product of a normal band by a completely simple semigroup").
* There is no title, venue, theorem number, page, URL or pinned copy.
* The label "printed Fact1" is not tied to any document in the bundle.
* The citation therefore does **not** locate Fact 1 exactly. I did not read Fact 1: no URL is named, and web search was forbidden.
* Two things remain unverified:
  * whether Fact 1's notion of weakly E-unitary matches the two-witness WEU used here;
  * whether its "Pastijn product" matches the bundle's "physical host" (the author also flags this).

## 9. Instance lemma and certificates (I)

**Lemma.** For S regular, q idempotent-pure to a CS semigroup, and S RRL: if q(exe) = q(e) = q(eye), then `exeyexe = eyexe`. **WRITTEN_SUPPORTED.** Reconstruction, for e ∈ S arbitrary (not necessarily idempotent) and e' ∈ V(e):
* Put f = ee', p = exee' and r = eyee'.
* q(p) = q(e)q(e') = q(f) is idempotent, so p ∈ E by purity; likewise r.
* fp = p = pf, using ee'e = e and e'ee' = e'. So p, r ∈ E(fSf), which is right regular, giving prp = rp.
* Using ee'e = e: prp = (exeyexe)e' and rp = (eyexe)e'.
* Right-multiply by e: both words end in e and ee'e = e, which gives the claim.

The words must be evaluated **literally**: for non-idempotent e, (exe)(eye)(exe) ≠ exeyexe in general.

Finite checks:
* 415061 admissible triples across all 353 sources;
* **zero** violations in all 281 RRL sources;
* 44996 checks of the proof internals (p, r ∈ E(fSf), prp = rp, both expansions).

Negative controls:
* **NEG-5 (sharpness).** Each of the 72 non-RRL sources violates the identity. The reason is structural: for an idempotent f with E(fSf) not right regular, take e = f and x = p, y = r with prp ≠ rp.
* **NEG-2.** Without purity (Z2, trivial actor), (e,x,y) = (1,g,1) violates the identity, and p is not idempotent.

**"Why this is the relevant instance" paragraph: INCONCLUSIVE.** It is not load-bearing and depends on unbundled certificate definitions. In my model, label-consistency of `exeyexe`/`eyexe` does reduce to t(exe) = t(e) = t(eye). ker t ⊇ ν' is true for any homomorphism to a CS semigroup. I did not check "consistent words keep their source evaluation…".

**§2 structural claims about Q4: WRITTEN_SUPPORTED.** I re-implemented the invariant (first letter, last new letter from the right, invariant of the suffix):
* Q3 has 51 elements; Q3 = F3/ρ exactly (homomorphism, onto, kernel = ρ(F3)).
* Q4 has 748 elements, matching Σ C(n,k)k!(k−1)!k. It is an associative band whose local monoids are all right regular; it is not LEFTSN; letter relabellings are automorphisms; and the invariant is compatible with concatenation on all word pairs of length ≤ 4 plus 20000 random pairs.
* Freeness of Q4 was not checked, in line with the author's own caveat.

**§2 canonical-host certificates** (60/60, 473/473, 45/45, 8/8): **INCONCLUSIVE**. I did not reproduce them: the random sources are unpinned, and author scripts may not be executed.

## 10. A hand-checkable example (`rf164-illustration-v1.py`, SHA 54436de2…)

Take S = FRR2¹ ⋊ Z2, where FRR2¹ is the free right regular band monoid {1, a, b, ab, ba} and Z2 acts by swapping letters. The actor is q(u,g) = g. The program prints the 10×10 table and reports that S is associative and regular and that q is pure.

Green's relations:
* R-classes: {(1,0),(1,1)}, {(a,0),(a,1)}, {(b,0),(b,1)}, {(ab,0),(ba,0),(ab,1),(ba,1)};
* L-classes: {(1,0),(1,1)}, {(a,0),(b,1)}, {(b,0),(a,1)}, {(ab,0),(ba,1)}, {(ba,0),(ab,1)};
* every H-class meets each q-fibre at most once, so H ∩ ker q = Δ.

Local structure:
* The local band at (1,0) is {(1,0),(a,0),(b,0),(ab,0),(ba,0)}; it is right regular.
* The only local R-pair is ((ab,0),(ba,0)): indeed (ab,0)(ba,0) = (ba,0) and (ba,0)(ab,0) = (ab,0). There are no local L-pairs.

Results:
* λ_S has classes {(ab,0),(ba,0)} and {(ab,1),(ba,1)}, plus singletons; λ_S ⊆ R and λ_S ⊆ ker q; ρ_S = Δ.
* |S/λ_S| = 8, and its local bands are semilattices.
* The instance identity holds on all 250 admissible triples.
* The run ended with "ILLUSTRATION: AS EXPECTED".

## 11. Controls and receipts

* **`rf164-controls-v1.py`** (SHA-256 `cf5918c35ea48a6def558daa19496950bbf67ab2a6f5bc993360c1328a37c444`, 54765 bytes). Evidence run: `python3 -B` with Python 3.14.3, numpy 2.4.3 and seed 20261029, from Thu Oct 29 08:01:50 PDT 2026 to 08:02:18 PDT 2026, exit 0.
  * Log: `rf164-controls-v1.log.txt` (SHA-256 `63d6d4e3c180d2b894f082c1abd24e2f4ab59dce3351f26ee8c34869d8bb9188`, 444 lines). It ends "unexpected outcomes: 0 / RESULT: ALL CONTROLS AS EXPECTED".
  * Sections: S0 erratum; S1 band enumeration; S2 Kimura on small bands; S3 F3 and NEG-1; S4 Q3/Q4; S5/S6 sources and host model; S6b the 2⇒3 scenario; S6c actor transport; S7 NEG-2, NEG-3, NEG-4.
  * Negatives tagged in the log: NEG-1 through NEG-9. NEG-5 is checked per non-RRL source and NEG-10 in the aggregate.
* **`rf164-illustration-v1.py`**: run at Thu Oct 29 08:03:50 PDT 2026, exit 0. Its stdout was not saved; the key lines are quoted in §10.
* **`rf164-receipt-v1.txt`**: all hashes and clocks, including the public-source copies under `rf164-work/`.

## 12. Exact dependency list

**Imports, none reviewed here:**
1. **Fact 1** (Billhardt–Szendrei 2003; see §8).
2. The author bridge `frontier-20261028-weakE-localorth-pure-cs-proof-v1.md` (d339b316…). It identifies "original source" with the regular, weakly E-unitary, locally r-orthodox class. It is needed only to connect the bundle's Q1 to the printed problem, whose text is not in the bundle.
3. `frontier-20261028-finite-source-canonical-decision-v1.md` (b6f54918…): the canonical V-band/host. Needed for K6–K7 and item 4.
4. `frontier-20261028-canonical-comparable-horn-exact-v1.md` (a93c69d9…): needed only for the Horn clause in K8.
5. `frontier-20261029-exact-idempotent-fibre-class-v1.md` (aabc39e5…): re-proved here; not needed.
6. Petrich 2006, Lemma 2.1 (pinned copy 0514fe1f…): located exactly; dispensable.
7. `frontier-20261028-local-regular-seminormal-equivalence-v1.md` (bf7af7af…) and its erratum (dfedbf04…): explicitly not needed by this packet.
8. `frontier-20261029-SN-instance-no-host-certificate-v1.md` (2f4fecc8…): used only in a motivational paragraph.

**Unstated convention:** the physical-host / Pastijn-product formalism (weights, actor, pure actor, products, opposites, functoriality). It is load-bearing for S4, S6–S8 and every host statement in the matching note.

**Pinned data:** no theorem statement depends on pinned data. S68, P(B5¹, D8) and Q4 appear only as controls or certificates.

## 13. Deviations and disclosures

* **Files created only inside my review directory.** I downloaded the named arXiv:1207.4296 PDF to `rf164-work/` and extracted pp.1–3 as text there, in order to verify p.2. I did not delete them, since deletion is forbidden.
* **Petrich copy.** I hashed and read the pinned Petrich 2006 copy: only its title block and the Lemma 2.1 statement (pdftotext lines 86–100). A preceding line-number grep also showed short fragments of about ten other lines. No file was written.
* **Bug in my own check, caught before the evidence run.** I made three smoke runs of my script (stdout only). The first reported 502 surprises. All of them came from my own check, which evaluated (exe)(eye)(exe) instead of the literal word, wrong whenever e is not idempotent; after the fix everything passed. The author's lemma was never at fault.
* **Tool side effects.** The write tool auto-set the executable bit on my two scripts. I used `> /dev/null` once, to suppress the stdout of the evidence run (no file was written). `python3 -B` was used, so no pycache was created.
* **Exploratory runs.** Prototype timings of the band enumeration and the F3 construction ran in the eval kernel and wrote nothing to disk.
* **Forbidden actions not taken.** No web search, external model, paid API, author contact, Git, deletion, publication or infrastructure change. I read no held or quarantined payload. The IRC notices about f161 and f162 concern materials I never opened.
* **Commands not run.** The build, lint, test and formatter commands are unrelated to this review and were not run.

## 14. What remains open for the original Q1

1. **Q1 itself.** No proof and no counterexample is claimed, by the author or by me.
2. **Unconditional reduction** (given only a host convention with products and opposites): Q1 ⟺ Q1 for RRL original sources.
3. **Within RRL sources** (Fact-1-conditional):
   * Q1 ⟺ every pair of distinct R-related idempotents in one q-fibre is separated by some SN or RIGHTSN host.
   * Equivalence with separation by the **canonical RIGHTSN host over q** additionally needs the M1 repair.
   * The instance lemma removes every single-instance RIGHTSN obstruction. What is still uncontrolled is derivations that pass through label-inconsistent words. This separation problem is the open core.
4. **Conditional premises still to be checked:**
   * Fact 1: its exact statement, source location, WEU notion, and fit with the host convention.
   * The host convention itself.
   * The canonical-host import.
   * The bridge from the bundle's "original source" to the printed problem class.

## 15. Summary

I reconstructed every load-bearing proof of this bundle with Green's relations written out, and tested it on independently built finite semigroups:
* all 622 bands of order ≤ 6 (with their full congruence lattices), the 159-element free band F3, and 353 non-band original sources;
* explicit negative controls showing that dropping local regularity, purity, the CS target, the common-local-band restriction or RRL breaks the corresponding conclusion for the intended reason.

I found nothing false in the mathematics proper. The Kimura-type decomposition, λ_S ⊆ R, ρ_S ⊆ L, λ_S ∩ ρ_S = Δ (through H ∩ ker q = Δ, which holds for any idempotent-pure map), the one-sided original quotients, the duality reduction to RRL sources and the instance lemma `exeyexe = eyexe` all stand. Fact-1-conditional, the equivalence with separation by some SN host holds in the reviewer's host model.

Remaining issues:
* **MAJOR M1:** the final reformulation in terms of *the canonical* RIGHTSN host omits an actor-independence step. It is repairable via the least-CS-congruence transport sketched in §7.
* **MINOR m1–m5:**
  * m1: the "recovers Kimura" remark is false as literally stated for regular bands without an identity;
  * m2: a purity assumption in Kimura §3(b)/(c) is left implicit;
  * m3: the bundle never defines the host convention;
  * m4: the injectivity-lemma proof is elliptical;
  * m5: the Fact 1 citation is inexact.

Fact 1, the canonical-host definitions, the Horn criterion and the problem bridge are unreviewed imports, and Q1 remains open. This is a same-harness review only: not a human, independent-model-family, formal/kernel or novelty verification.
