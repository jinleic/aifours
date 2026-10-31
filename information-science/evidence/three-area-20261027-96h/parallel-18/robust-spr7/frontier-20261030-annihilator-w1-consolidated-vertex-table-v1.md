# W1 annihilator: corrected consolidated vertex table, proven dominations, and exact remaining inequalities

Owner InfoSPR7-2, info-2. Native clock before writing: **Fri Oct 30 03:47:47 PDT 2026**. WRITTEN, unreviewed, no experiments this turn. This packet (i) corrects `frontier-20261030-annihilator-w1-first-vertex-written-v1.md` (062635af…), (ii) supersedes its §3, and (iii) delivers the full per-vertex reduction Main directed.

## 0. Correction (independently confirmed)

062635af §3 claimed vertex (a,b,e) via the §2 ratio proved at (a,c,d). That is invalid: the §2 ratio uses the (a,c,d)-cancelled terms. Recomputing at (a,b,e) with worst endpoints O₋ at u₁,u₂: |t₁| = (b−u₁)²(e−u₁)/((d−u₁)D₁), t₂ = (b−u₂)²(e−u₂)/((d−u₂)D₂), so
t₂/|t₁| = ψ(b)²ψ(e)/[ψ(d)ψ(u₃)ψ(u₄)ψ(u₅)],  ψ(v) := (v−u₂)/(v−u₁),
in agreement with the parent's derivation. §2's lemma itself stands at its literal scope (the (a,c,d) shape); §3 is DOWNGRADED to unproven. No other claim of 062635af is affected; the two addenda stand.

## 1. Setup and exact worst-endpoint term table (Lemma A)

Nodes 0<u₁<a<u₂<u₃<b<u₄<c<u₅<d…<u₅∈(d,e); u₄∈(b,c) [gap] or (c,d) [band]. Envelopes O₋=λ₋(a−t)(d−t)(e−t), O₊=λ₊(b−t)(c−t)(f−t), λ₋≥λ₊>0. Annihilator weights wᵢ=c₀/(uᵢOᵢ(uᵢ)H′(uᵢ)), H′ signs (+,−,+,−,+); Dᵢ:=Π_{j≠i}|uᵢ−uⱼ|>0. Test F=−t(b−t)(e−t). Pairing P = c₀·Σ Tᵢ. With E(t)=(x−t)(y−t)(z−t), x∈{0,a}, y∈{b,c}, z∈{d,e}, exact cancellation at the worst endpoints gives:

T₁(x=0) = u₁(y−u₁)(z−u₁)(e−u₁)/(λ₊(c−u₁)(f−u₁)D₁) > 0;
T₁(x=a) = −(y−u₁)(z−u₁)(b−u₁)/(λ₋(d−u₁)D₁) < 0;
T₂ = (x−u₂)(y−u₂)(z−u₂)(b−u₂)/(λ₋(a−u₂)(d−u₂)D₂) > 0; at x=a: (y−u₂)(z−u₂)(b−u₂)/(λ₋(d−u₂)D₂);
T₃ = −(x−u₃)(y−u₃)(z−u₃)(e−u₃)/(λ₊(c−u₃)(f−u₃)D₃) > 0;
T₄(gap, y=b) = (x−u₄)(z−u₄)(b−u₄)²/(λ₋(a−u₄)(d−u₄)D₄) > 0;
T₄(gap, y=c) = (x−u₄)(z−u₄)(e−u₄)/(λ₊(f−u₄)D₄) < 0;
T₄(band, both y) = (x−u₄)(y−u₄)(z−u₄)(b−u₄)/(λ₋(a−u₄)(d−u₄)D₄) > 0;
T₅(z=e) = −(x−u₅)(y−u₅)(e−u₅)²/(λ₊(c−u₅)(f−u₅)D₅) > 0;
T₅(z=d) = −(x−u₅)(y−u₅)(b−u₅)/(λ₋(a−u₅)D₅) < 0.

**Lemma B (domination/boundedness).** Each term equals Kᵢ/Oᵢ with Kᵢ = E(uᵢ)F(uᵢ)/(uᵢH′(uᵢ)) sign-fixed by the placement; the minimum over actual Oᵢ of the required sign is attained at the displayed envelope endpoint and is finite: the band nodes u₂,u₃ (valid sign-range touching 0) have K₂<0 resp. K₃>0 with required signs −,+, so their terms are positive and minimized at O₋(u₂),O₊(u₃); the gap/band u₄ and gap-adjacent u₅ ranges are bounded away from 0. No unbounded-negative direction exists; the table is the exact pointwise worst case.

## 2. Lemma C (matching) and proven dominations

For v,w>u₂: ψ(v)/ψ(w)>1 ⟺ v>w, since (v−u₂)(w−u₁)−(v−u₁)(w−u₂)=(u₂−u₁)(v−w). From §1, at every x=a vertex t₂/|t₁| = ψ(y)ψ(z)ψ(b)/[ψ(u₃)ψ(u₄)ψ(u₅)ψ(d)] (both terms carry 1/λ₋; the ratio is scale-free).

**Proven (gap):** at (a,c,d): ratio = ψ(c)ψ(b)/[ψ(u₃)ψ(u₄)ψ(u₅)] (ψ(d) cancels) — match c↔u₄, b↔u₃ (both strict, gap has c>u₄, b>u₃), leftover 1/ψ(u₅)>1: t₂>|t₁| STRICT. At (a,c,e): ratio = ψ(c)ψ(e)ψ(b)/[ψ(u₃)ψ(u₄)ψ(u₅)ψ(d)] — match c↔u₄, e↔u₅, b↔u₃, leftover 1/ψ(d)>1: STRICT.

**Proven vertices (all terms positive, Lemma A signs):** gap (0,b,e); band (0,b,e) and (0,c,e).

## 3. Exact remaining inequalities (nothing hidden)

GAP: (a,b,e): t₂>|t₁| ⟺ ψ(b)²ψ(e)>ψ(d)ψ(u₃)ψ(u₄)ψ(u₅) [RI-1]; (a,b,d): ψ(b)²>ψ(u₃)ψ(u₄)ψ(u₅) [RI-2], then T₃+T₄ᵇ>|T₅ᵈ|; (0,b,d): T₁⁰+T₂+T₃+T₄ᵇ>|T₅ᵈ|; (0,c,e): T₁⁰+T₂+T₃+T₅ᵉ>|T₄ᶜ|; (0,c,d): T₁⁰+T₂+T₃>|T₄ᶜ|+|T₅ᵈ|; (a,c,e): x=a part proven, remaining T₃+T₅ᵉ>|T₄ᶜ| (both 1/λ₊); (a,c,d): x=a part proven, remaining (t₂−|t₁|)+T₃>|T₄ᶜ|+|T₅ᵈ|.
BAND: T₄>0 always; (a,b,e): RI-1′ ψ(b)ψ(e)·[match b↔u₃, e↔u₄] leftover ψ(b)>ψ(u₅)ψ(d) [RI-3]; (a,b,d): RI-2 (same reduced form); (a,c,e): match b↔u₃, e↔u₄, leftover ψ(c)>ψ(u₅)ψ(d) [RI-4]; (a,c,d): match b↔u₃, d↔u₄, leftover ψ(c)>ψ(u₅) [RI-5]; all (·,·,d): additionally T₃+T₄>|T₅ᵈ|.
Each RI is an explicit rational inequality in the five node variables and band endpoints (λ-free); e.g. RI-2: (b−u₂)(u₄−u₁)(u₅−u₁) > (b−u₁)(u₄−u₂)(u₅−u₂).

## 4. Status and scope

Proven all-variable: the §1 table (Lemma A), boundedness (Lemma B), the two gap x=a dominations (Lemma C), and three all-positive vertices — gap (0,b,e), band (0,b,e), band (0,c,e). Everything else is reduced to the displayed exact inequalities (RI-1…RI-5 plus the listed partial/total-sum bounds). No sampled count is used as proof. Residuals unchanged: 5 gap + 3 band vertices beyond the proven dominations; W1 other placements; 16 further annihilator-admitting m=6 words; all m=7 (239), m=8 (1842); no support-reduction claim; the m≤5 lower bound is not promoted. Process ancestry dfb30abd… status only; no clean-cognition claim.
