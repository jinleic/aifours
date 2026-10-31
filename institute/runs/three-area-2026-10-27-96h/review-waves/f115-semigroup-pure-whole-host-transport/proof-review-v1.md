# f115 proof review — pure whole-host transport along an idempotent-pure completely-simple homomorphism

**Kind:** INDEPENDENT_SAME_HARNESS_SCIENTIFIC_REVIEW (written reconstruction + one reviewer-written exact finite diagnostic). Same-harness only: this is **not** human, independent-model-family, formal/kernel or novelty clearance.
**Review id:** `f115-semigroup-pure-whole-host-transport`. **Authority:** `contract-addendum-2-frontier-first-owner-direction-v1.json` (frontier-first). Historical held outcomes are not premises here; no historical review is changed; no arbitrary-source host is constructed.
**Observed clock before this file was written:** `2026-10-29T03:04:08Z` = `2026-10-28 20:04:08 PDT` (`/bin/date`, run immediately before writing; all other stamps below are copied from `/bin/date` output in the recorded runs).

## 0. Manifest and inputs (verified before reading)

`manifest-v1.json` SHA-256 `6580d8208d704cb242e28e58951646d5ada674919b5569340e8252f566390426`, 2855 bytes — matches the assignment. Inputs were hashed/counted first and then read **completely, in manifest order, with `:raw`**:

| # | role | file | SHA-256 | bytes | LF | match |
|---|------|------|---------|-------|----|-------|
| 1 | predecessor onto proof + Rees gauges | `.../semigroup-embedding/frontier-20261028-pure-actor-finite-band-pushforward-v1.md` | `abdfecbf…9057` | 13634 | 139 | yes |
| 2 | general whole-host candidate | `.../frontier-20261028-pure-CS-coinduced-whole-host-v1.md` | `b129099e…bad2` | 7225 | 82 | yes |
| 3 | author finite nonnormal transport control | `.../frontier-20261028-pure-nononto-transport-checker-v1.py` | `dc8caf28…8400` | 2780 | 48 | yes |
| 4 | author coinduction convention control | `.../frontier-20261028-local-global-coinduction-checker-v1.py` | `3a0d6c2f…cfc` | 3058 | 57 | yes |

Full hashes are in `proof-f115-hashes-v1.txt`. Author scripts (3, 4) were **read as text only**, never executed or imported.
**Not read (deliberately):** the sibling-prefixed files present in this directory at 19:37–19:39 PDT (`finite-control-v1.py`, `finite-products-v1.json`, `finite-result-v1.json`, `finite-review-v1.md`) — not in my manifest; the non-frozen documents/scripts cited inside the inputs (unit-sandwich Rees lift `8822d5ac…`, `frontier-20261028-unit-rees-coarse-actor-checker-v1.py`, `frontier-20261028-surjective-actor-gauge-checker-v1.py`, "cryptogroup note", any U3 record). No web search, no external model, no Git, no deletion.

## 1. Definitions the frozen inputs leave implicit (reconstructed; see Finding F1)

* **Rees matrix semigroup** `M[G;I,Λ;P]`: `(i,g,λ)(j,k,μ) = (i, g p_{λj} k, μ)`. Rows = R-classes, columns = L-classes, every H-class `{(i,·,λ)}` is a group with identity `(i, p_{λi}^{-1}, λ)`.
* **Idempotent-pure** `f`: `f(x)∈E ⇒ x∈E`. (Homomorphisms always send `E` to `E`.)
* **Physical band-by-CS product** `P(B,D)` for a band `B` with an action `α:G→Aut(B)`: elements `(b,(i,g,λ))`,
  `(b,(i,g,λ))·(c,(j,k,μ)) = ( b·α_{w}(c), (i, w k, μ) )`, `w = g p_{λj}` (the "physical weight"). This is nowhere defined in the four inputs; it is forced by input 1 §4 / input 2 §4 ("`w0 = g P0_(λ,j)`", band coordinate `b·α_{w0}(d)`) and by the author's `sm`/`source` functions. **Associativity** (not stated in the inputs; needed for the object to exist): for three factors both bracketings give actor `(i, g p_{λj} k p_{μ l} m, ν)` and band `b · α_{g p_{λj}}(c) · α_{g p_{λj} k p_{μl}}(d)`, using only that each `α_x` is an automorphism and `α` is an action. ✔ (independently checked on all 162³ triples of my instance).
* **`τ_S`**: the syntactic congruence of `E(S)`: `s τ_S t ⇔ ∀x,y∈S¹: (xsy∈E ⇔ xty∈E)`. Reconstructed from "complete contexts", "absent context", "saturates idempotents by the absent-absent test". `τ` is the largest congruence saturating `E`; the empty context shows it saturates `E`.
* **`V`**: bands whose local submonoids `eBe` are regular bands, i.e. the identity `(exe)(eye)(exe)(eze)(exe) = (exe)(eye)(eze)(exe)`; a variety, hence closed under products and subbands. Rectangular bands satisfy it (`exe=e`).

## 2. Independent all-variable reconstruction of the transport theorem

Throughout: `f:D0→D1` idempotent-pure homomorphism, `D0=M[G0;I0,Λ0;P0]`, `D1=M[G1;I1,Λ1;P1]`, `B∈V` nonempty with `α:G0→Aut(B)`. I write `ρ:I0→I1`, `σ:Λ0→Λ1` for the author's row/column maps `a,b` (to avoid the clash with band elements), `φ` or `h` for the group map.

### 2.1 Local groups (inputs 1 §2, 2 §2) — VERIFIED
For `e∈E(D0)`, `eD0e` and `f(e)D1f(e)` are groups (Rees model), `f` restricts to a group homomorphism. *Injective:* `f(x)=f(y)` ⇒ `f(xy^{-1}) = f(y)f(y^{-1}) = f(yy^{-1}) = f(e)` is idempotent ⇒ (purity) `xy^{-1}∈E(eD0e)={e}` ⇒ `x=y`. *Onto when `f` is onto:* `z=f(x)` ⇒ `exe∈eD0e`, `f(exe)=f(e)zf(e)=z`. No row/column injectivity used. ✔ Purity is necessary (`C4→C2` control).

### 2.2 Normalized Rees gauge, (RH) and (RH-P) (input 1 §3, input 2 §2) — VERIFIED
*Gauge.* With `A_i=p_{λ0 i}`, `B_λ=p_{λ i0} p_{λ0 i0}^{-1}`, `θ(i,g,λ)=(i,A_i g B_λ,λ)`, `p'_{λi}=B_λ^{-1}p_{λi}A_i^{-1}`: `θ` is an isomorphism `M[G;I,Λ;P]→M[G;I,Λ;P']` because `B_λ p'_{λj} A_j = p_{λj}`; `p'_{λ0 i}=B_{λ0}^{-1}=1` and `p'_{λ i0}=(p_{λi0}p_{λ0i0}^{-1})^{-1}p_{λi0}p_{λ0i0}^{-1}=1`. ✔
*Factorization in normalized coordinates.* `E_i=(i,1,λ0)`, `F_λ=(i0,1,λ)`, `T_g=(i0,g,λ0)`; `E_iT_gF_λ=(i,g,λ)` and `T_gT_h=T_{gh}` (both use `p_{λ0 i0}=1`). Writing `f(E_i)=(ρi,X_i,σλ0)`, `f(F_λ)=(ρi0,Y_λ,σλ)`, `f(T_g)=(ρi0,K_g,σλ0)`, `p*=P1(σλ0,ρi0)`: `K_{gh}=K_g p* K_h`, so `h(g):=K_g p*` is a homomorphism with `h(1)=1` (`f(T_1)` idempotent forces `K_1p*=1`). Then
`f(i,g,λ) = (ρi, X_i p* K_g p* Y_λ, σλ) = (ρi, u_i h(g) v_λ, σλ)`, `u_i=X_ip*`, `v_λ=Y_λ`  **(RH)**;
`F_λE_j=T_{p_{λj}}` ⇒ `Y_λ P1(σλ,ρj) X_j = K_{p_{λj}}` ⇒ (right-multiply by `p*`) `v_λ P1(σλ,ρj) u_j = h(p_{λj})`  **(RH-P)**. ✔
*Undo gauge (arbitrary coordinates).* The same element has original group coordinate `g` with `g'=A_igB_λ`; so `f(i,g,λ)=(ρi, u'_i h(A_i) h(g) h(B_λ) v'_λ, σλ)`: set `u_i=u'_ih(A_i)`, `v_λ=h(B_λ)v'_λ`; then `v_λP1u_j=h(B_λ)h(p'_{λj})h(A_j)=h(p_{λj})`. (RH),(RH-P) hold in **original** coordinates. ✔ (Finite diagnostic §3: derived from `f` as a black box, 0 violations; omitting the undo step gives 12/4 violations.)
*Conjugation statement.* With `p0=P0(λ0,i0)`, `p1=P1(σλ0,ρi0)`, the group parameter of `(i0,xp0^{-1},λ0)` maps to `u_{i0}h(x)u_{i0}^{-1}` because (RH-P) at `(λ0,i0)` gives `v_{λ0}=h(p0)u_{i0}^{-1}p1^{-1}`. Hence `h` is injective by 2.1, bijective if `f` is onto. ✔ Row/column maps need not be injective, `h(G0)` need not be normal. ✔

### 2.3 Coinduction with nonnormal image (input 2 §3) — VERIFIED
`H=φ(G0)≤G1`; left cosets `rH`, representatives `R∋1`; every `x∈G1` is uniquely `rh`. `C=B^{G1}` pointwise (a band in `V`, products of `V`-bands). `(γ_gF)(x)=F(xg)`: `γ_gγ_kF(x)=γ_kF(xg)=F(xgk)` so `γ_gγ_k=γ_{gk}`, a **left** action by automorphisms (pointwise). `J(b)(rh)=α_{φ^{-1}(h)}(b)` is well defined (unique decomposition), a band homomorphism (pointwise, `α` automorphisms), injective (`J(b)(1)=b` since `1=1·1`), and for `h0∈H`: `γ_{h0}J(b)(rh)=J(b)(r(hh0))=α_{φ^{-1}(hh0)}(b)=α_{φ^{-1}(h)}α_{φ^{-1}(h0)}(b)=J(α_{φ^{-1}(h0)}b)(rh)`. ✔ Nonnormality of `H` is irrelevant because right multiplication by `H` preserves each left coset `rH`. The convention is essential: with left shifts `F(g^{-1}x)` or with right cosets `x=hr` the decomposition does not stay in the coset (controls in §5 below: 12/18 failures each).
*Dependency remark (not a defect):* `R` is a set-theoretic selection (choice for infinite index). Also any fixed band element `b0` as constant padding off `H` would give an equivariant injective hom too (`b0b0=b0`), so "no selected element" is a convenience, not a necessity.

### 2.4 Whole-product homomorphism and injection (input 1 §4, input 2 §4) — VERIFIED
`R0=I0×Λ0`, `(i,λ)(j,μ)=(i,μ)`; `G1` acts trivially on `R0`, by `γ` on `C`. `Ψ(b,(i,g,λ)) = (((i,λ), γ_{u_i}J(b)), f(i,g,λ))`.
*Weight identity.* Source weight `w0=gp_{λj}`; target weight `w1 = (u_iφ(g)v_λ)·P1(σλ,ρj)` and by (RH-P) `v_λP1(σλ,ρj)=φ(p_{λj})u_j^{-1}`, so `w1=u_iφ(w0)u_j^{-1}`. ✔
*Homomorphism.* Target band coordinate `γ_{u_i}J(b)·γ_{w1}γ_{u_j}J(c) = γ_{u_i}J(b)·γ_{u_iφ(w0)}J(c) = γ_{u_i}( J(b)·γ_{φ(w0)}J(c) ) = γ_{u_i}( J(b)J(α_{w0}c) ) = γ_{u_i}J(bα_{w0}c)`; rectangle `(i,μ)`; actor `f((i,g,λ)(j,k,μ))`. This is `Ψ` of the source product for **every** `b,c` and actor pair. ✔
*Injective.* Rectangle recovers `(i,λ)`; then equal actors give `u_iφ(g)v_λ=u_iφ(g')v_λ` ⇒ `g=g'` (`φ` injective); then `γ_{u_i}J(b)=γ_{u_i}J(b')` ⇒ `b=b'` (`γ` bijective, `J` injective). ✔ Row/column collapse is harmless because the rectangle keeps **source** labels (control: dropping it leaves 72 of 162 images in my instance).

### 2.5 Onto specialization with the same `B` (input 1 §§1,4; input 2 §4 end) — VERIFIED
If `f` is onto, `h` is bijective (2.1–2.2), `H=G1`, one coset, `J(b)(z)=α_{h^{-1}(z)}(b)`; `J(B)` is a `γ`-invariant subband isomorphic to `B` (`γ_zJ(b)=J(α_{h^{-1}(z)}b)`), so `Ψ` lands in `P(R0×J(B),D1)≅P(R0×B,D1)` with `G1` acting on `B` by `γ_z=α_{h^{-1}(z)}`; input 1's direct formula `Ψ(b,(i,g,λ))=(((i,λ),γ_{u_i}(b)),f(i,g,λ))` is this restriction and its proof (`γ_{u_i}(b)·γ_{w1}γ_{u_j}(d)=γ_{u_i}(b·α_{w0}d)`) is the same computation. `R0×B∈V`; finite if `B,I0,Λ0` finite; no power of `B`. ✔

### 2.6 Facts used in input 1 §5 about `P(B,D0)` — VERIFIED
`(b,(i,g,λ))` with idempotent actor has self-weight `gp_{λi}=1`, so its square is `(b²,(i,g,λ))=(b,(i,g,λ))`: `E(P(B,D0))=B×E(D0)`, hence the actor projection `π` is pure on any faithful `j:S↪P(B,D0)` (`r(s)∈E ⇒ j(s)∈E ⇒ j(s²)=j(s) ⇒ s²=s`). Also `P(B,D0)` is regular (`(b,d)(α_{(gp_{λi'})^{-1}}b,d')(b,d)=(b,d)` for an inverse `d'=(i',·,·)` of `d`). ✔

## 3. Separate analysis: `τ_S`, purity of the `τ`-quotient, actual-`q` host, and the free-`V`-band / R / L assertions

### 3.1 `s τ_S t ⇔ r(s) τ_{D0} r(t)` for **onto pure** `r` (input 1 §5 (3), input 2 §5) — VERIFIED
(⇐) For a context `(x,y)∈S¹×S¹`: `xsy∈E ⇔ r(xsy)∈E` (hom + purity) `⇔ r(x)r(s)r(y)∈E ⇔ r(x)r(t)r(y)∈E` (`τ_{D0}`, with absent ↔ absent) `⇔ xty∈E`. (⇒) Every `D0¹`-context is `(r(x),r(y))` by ontoness (absent ↔ absent) and the same chain runs. Hence `S/τ_S ≅ D0/τ_{D0}` canonically and `q_{τ_S}` is `f∘r` up to this isomorphism. ✔ Both hypotheses are necessary: non-pure onto `C4→C2` violates (3) (control: 4 of 16 pairs); pure **non-onto** inclusion of one row of `D0` violates the forward direction (control: 3 classes vs 6; 12 violations). Regularity of `S` is **not** used here (Finding F5).

### 3.2 `f:D0→D0/τ_{D0}` is pure, onto, between completely simple semigroups — VERIFIED (one classical dependency)
`τ` saturates `E` (empty context). If `x² τ x`, take an inverse `t` of `x²` (`x²tx²=x²`, `tx²t=t`). Then `(xtx)²=x(tx²t)x=xtx` is idempotent. Because `τ` is a congruence and `x² τ x`, substituting `x` for each `x²` in `x²tx²` gives `x²tx² τ xtx`; but `x²tx²=x² τ x`. Hence `xtx τ x`, and saturation gives `x∈E`. ✔ (The inputs assert "x t x is an idempotent in its class" without this line — Finding F6.) Ontoness is trivial. **Classical dependency:** a homomorphic image of a completely simple semigroup is completely simple (image of a completely regular semigroup is completely regular; image of a simple semigroup is simple; simple + completely regular ⇒ completely simple). Not re-proved here; verified on the instance (quotient simple and completely regular). ✔

### 3.3 Faithful host over the actual `q_{τ_S}` — VERIFIED as a consequence of §2 + 3.1–3.2
Given a faithful `j:S↪P(B,D0)` with onto pure actor `r=π∘j`, `Ψ∘j:S↪P(R0×B, D0/τ_{D0})` is injective with actor `f∘r`, i.e. `q_{τ_S}` after the canonical isomorphism; the band is `R0×B∈V` with the same `B` (2.5). ✔ This is a **conditional transport**: it presupposes the initial host `j`, exactly as both inputs state. Instance: `ker f2 = τ_{D0}` was verified by brute force, so `Ψ2` in §5 is literally a same-`B` host over the actual `τ`-quotient of that `D0`.

### 3.4 Canonical free-`V`-band map, `κ_q`, `β`, and "same-q R/L idempotent separations" — **NOT PRESENTED in the frozen inputs; left CONDITIONAL**
The sentences "map every generator `X_(u,s)` to the transported action `α'_u` of the band coefficient of `Ψj(s)`. Source multiplicativity proves every mixed relation, and the V identities/context relations hold in the constructed band. Hence `κ_q` is faithful. All same-q R- and L-idempotent separations follow" (input 1 §5) and "the canonical free-V-band universal map proves `κ_q` injective" (input 2 §5) rely on objects (`κ_q`, generators `X_(u,s)`, "mixed relations", "context relations", `β`, the R/L obligations) that are **defined nowhere in the four inputs**. Whether the existence of a faithful physical host over `q_τ` implies `κ_q` faithful depends on the (external) definition of `κ_q` and on the universal property's exact relation set; I cannot confirm or refute it from the frozen material and did not read other sources. **Status: INCONCLUSIVE at this review's scope; the actual-q deductions are conditional on that external presentation being reviewed.** Likewise input 1 §6 (unit-sandwich Rees sources, removal of `τ_{D0}=equality`) and §1's "their actual canonical κ_q and both same-q R/L obligations are faithful for arbitrary such D0" inherit this condition plus the non-frozen predecessor `8822d5ac…` (regularity, weak E-unitarity, local r-orthodoxy, condition (UL), the initial faithful host): all **conditional**, not checked here. No upgrade of any historical U3 or held record is made or implied.

## 4. Edge cases

* **No band identity / no α-fixed point.** Neither is used anywhere: `J` is defined for every `b`; `C` is pointwise; `R0` needs no distinguished element. My instance's `B` (right-zero(3)×semilattice(2)) has no identity and a fixed-point-free `C3`-action; all of §5 passes. ✔
* **Infinite groups / infinite index.** No finiteness is used in 2.1–2.5 or 3.1–3.3. `C=B^{G1}` becomes infinite when `|B|≥2` and `G1` is infinite — the inputs correctly make no finite-target claim there; the onto case keeps `R0×B` (finite iff `B,I0,Λ0` finite). Coset representatives need choice in general (dependency, 2.3). Written argument only; not finitely testable.
* **Row/column collapse (`ρ`,`σ` non-injective).** Handled by the source-label rectangle (2.4); instance has both maps `3→2` collapsing, with `ker f2 = τ_{D0}` identifying exactly the collapsed rows/columns. ✔ Without the rectangle: 72 of 162 images (collision), as the inputs' own controls also claim.
* **Degenerate cases checked by hand:** `G0` trivial (then `H=1`, `J(b)` constant, construction reduces to `R0×B` with trivial action); `|I0|=|Λ0|=1` (`D0` a group, `R0` trivial); constant `f` onto a single idempotent (pure iff `D0` is a rectangular band; then `G1=1`, `C≅B`). All consistent with the theorem.
* **Non-pure `f`.** Excluded by hypothesis; then `φ` need not be injective and `J` is undefined (`C4→C2` control). The inputs say so.

## 5. Independent finite diagnostic (reviewer-written; required control evidence)

**Design (differs from the author's S3/C2/5-element data in every parameter):** `G0=C3`, `G1=A4`, `H=φ(C3)` nonnormal; `B=` right-zero(3)×semilattice(2) (6 elements, in `V`, not rectangular, no identity, fixed-point-free action, weight-sensitive); `D0=M[C3;3,3;P0]` with `P0=[[0,1,0],[0,1,1],[2,0,0]]` (not normalized; `A_1=1`, `B_2=2`), `D1=M[A4;2,2;P1]`, `ρ=(0,0,1)`, `σ=(0,1,1)`; `f` pure, image 12 of 48, not injective. Gauges `(ρ,σ,h,u_i,v_λ)` are **derived from `f` as a black box** by the §2.2 recipe (not copied from the construction) and `Ψ` uses the derived values. Every assertion is a complete enumeration.

**v1 (`proof-f115-finite-diagnostic-v1.py`, exit 1 — reviewer control-design defect, disclosed, kept as record):** I first chose a *left*-zero factor, for which `b·α_w(c)=(b0,min(b1,c1))` is independent of `w`; the section-5 homomorphism check then could not see the weight, the `u_i` gauge or the shift convention, so my two negative controls there were vacuous and the script stopped at its own `assert bad_nogauge>0 and bad_leftshift>0` (sections 1–4 incl. their controls had passed; 6–7 unreached). Record: `proof-f115-finite-diagnostic-v1-run-FAILED.txt` (START `2026-10-29T02:53:54Z`, END `02:54:01Z`). Not an author defect.

**v2 (`proof-f115-finite-diagnostic-v2.py`): right-zero factor + explicit non-vacuity assertion; nothing else changed. Single evidence run** `/opt/homebrew/opt/python@3.14/bin/python3.14 -B`, START `2026-10-29T02:57:55Z` (`19:57:55 PDT`), END `02:58:05Z`, **EXIT=0**, 9.6 s, Python 3.14.3; verbatim record `proof-f115-finite-diagnostic-v2-run.txt`:

| § | positive result (all complete enumerations) | negative control (must trip) |
|---|---|---|
| 1 | `D0`,`D1` associative; `f` homomorphism (27²), pure, image 12 (nononto, noninjective) | — |
| 2 | `f` injective on all 9 local groups; none onto | nonpure `C4→C2`: local map not injective |
| 3 | derived gauges: (RH) 0 violations, (RH-P) 0; `h` injective; base local map `= u_{i0}h(x)u_{i0}^{-1}` | un-gauge omitted: 12 (RH) / 4 (RH-P) violations |
| 4 | 4 left cosets; `γ` is a left action (`RIGHT[gk]=RIGHT[k]∘RIGHT[g]` on all 12³ indices); `J` hom, injective, `H`-equivariant | left-shift convention 12/18 failures; right-coset convention 12/18 failures |
| 5 | `P(B,D0)` (162) associative on 162³, regular, `E=B×E(D0)`; `Ψ` homomorphism on all 26244 pairs (0 violations), injective | no rectangle: 72/162 images; no `u_i` gauge: 19440 violations; left-shift convention: 17496 violations |
| 6 | onto `f2:D0→D2` (12), pure, local maps onto, derived `h2` bijective, (RH)/(RH-P) 0/0; `Ψ2` into `P(R0×B,D2)` with the **same** `B`: 0 violations, injective; `J2(B)` `γ`-invariant | — |
| 7 | `τ_S=π^{-1}(τ_{D0})` on all 26244 pairs (12 classes each); `τ` saturates `E`; quotient map pure; quotient simple + completely regular; `ker f2 = τ_{D0}` | nonpure onto `C4→C2`: 4/16 violations of (3); pure nononto row inclusion: 3 vs 6 classes, 12 forward violations |

**Limits:** one finite instance; it corroborates every step on that instance and shows each hypothesis/convention is load-bearing; it is not the proof. The all-variable arguments are §2–3.

## 6. Author finite controls (inputs 3, 4) — read only

Both scripts encode exactly the conventions of §2: physical weight `g⊕Q[λ][j]`, `(γ_gF)(x)=F(xg)`, left-coset decomposition with identity as first representative, `J(b)(rh)=α_h(b)`, gauge `γ_{u_i}` with `u_i=row[i]`, target sandwich `P=C_l^{-1}H[Q1]R_i^{-1}` satisfying (RH-P), purity asserted in both directions, whole-host products and injectivity asserted over all pairs, rectangle-removal collision asserted on a named pair (input 3), left-shift failure count asserted `>0` (input 4). Their printed outputs in input 2 §6 are **author-reported**; I did not execute them, so they are not independent evidence here. Input 4's last block (a nonregular subsemigroup of an "original 45-element source") is outside this review's scope. Input 1 §7 cites two further scripts/outputs that are **not** in the frozen set (Finding F3).

## 7. Findings

| id | severity | finding |
|----|----------|---------|
| F1 | MINOR (presentation) | The objects the theorem is about — the product law of `P(B,D)` with its weight convention, idempotent-purity, `τ` as the syntactic congruence of `E` with `S¹` contexts, and `V` — are used but never defined in the four frozen inputs; associativity of `P(B,D)` is never stated. The theorem is verified **under the reconstruction in §1**; a frozen definitional preamble would remove this dependency. |
| F2 | MINOR → CONDITIONAL scope | `κ_q` faithfulness, the free-`V`-band universal map, `β`, and "same-q R/L idempotent separations" (input 1 §§1,5,6; input 2 §5) have no formal presentation in the frozen inputs; the categorical phrasing in input 1 §1 ("do **not** need the extra hypothesis `τ_D0=equality`") and §6 ("`κ_q` is faithful for ALL unit-sandwich sources…") must be read as conditional on that external material (and on the non-frozen predecessor `8822d5ac…`). INCONCLUSIVE here; not a detected error. |
| F3 | MINOR (evidence) | Input 1 §7 reports two executed checks whose scripts/outputs are outside the frozen inputs; unverifiable in this review. |
| F4 | remark | Coset representatives are a selection (choice for infinite index), and constant padding by any band element also works; the "no selected element" advantage is nominal. No defect. |
| F5 | MINOR (presentation) | Input 2 §5 hypothesizes "regular source S" for (3); regularity of `S` is not used (regularity of `D0` is, for 3.2). |
| F6 | MINOR (presentation) | Input 1 §5 / input 2 §5 state "`xtx` is an idempotent in its class" without the one-line congruence step `x²tx² τ xtx`; supplied in §3.2. |

**No FATAL or MAJOR defect found** in the written transport mathematics (2.1–2.6) or in the τ-inverse-image / purity / actual-`q`-host consequences (3.1–3.3).

## 8. Scoped verdict

* **Whole-host transport theorem (input 2 §§1–4; general, nononto, nonnormal image, row/column collapse, no identity/fixed point, infinite groups allowed) — VERIFIED at same-harness level**, by independent all-variable reconstruction (§2) and an independent exact finite diagnostic with tripping negative controls (§5). MINOR presentation items F1, F4.
* **Onto same-`B`/rectangle specialization (input 1 §§1–4; input 2 §4 end) — VERIFIED** likewise (§2.5, §5 §6).
* **`τ_S=r^{-1}(τ_{D0})`, purity and CS-ness of the `τ`-quotient, faithful host over the actual `q_{τ_S}` given an initial faithful host over an onto pure actor — VERIFIED** (§3.1–3.3) with one named classical dependency (image of CS is CS) and the reconstruction of `τ` (F1, F5, F6 MINOR).
* **`κ_q` / free-`V`-band / same-q R/L / unit-sandwich application (input 1 §§1,5,6; input 2 §5 second half) — CONDITIONAL / INCONCLUSIVE at this scope** (F2): not presented in the frozen inputs; no error asserted, no acceptance granted.
* **Author finite controls** — consistent with the construction as read; their runs are author-reported, not independent evidence (F3 for the two unfrozen scripts).

**Explicit dependencies:** Rees theorem for completely simple semigroups; closure of the band variety `V` under direct products/subbands; homomorphic image of a completely simple semigroup is completely simple; choice of coset representatives; the reconstructed definitions of §1. **Not claimed:** novelty, original-source closure (no initial host is produced — both inputs say so), non-pure actors, human/independent-family/formal/kernel review.

## 9. Disclosures

* `__pycache__/proof-f115-finite-diagnostic-v1.cpython-314.pyc` was created in this directory by my `python3 -m py_compile` sanity step; removal is blocked by tool policy (`rm`), so it remains. It is a reviewer byproduct, not evidence; the evidence runs used `-B`.
* v1 of my diagnostic failed at its own negative-control assertion (reviewer defect, §5); v1 and its run are kept as records; v2 is the evidence run. A diagnostic probe (same script prefix executed to print the two control counts) was run to find the cause; it produced no artifact.
* **Shared-scratch collision (process incident, no bearing on the mathematics):** my first draft of this review was staged at the generic scratch name `local://proof-review-v1.md`; the harness scratch namespace is shared with sibling reviewers, and between my write and my copy a sibling overwrote that scratch file with an **f122** review ("six-variable gluing inequality Φ"). My `cp` therefore placed that sibling's 18814-byte file at `proof-review-v1.md` in this directory (20:02 PDT) until it was overwritten by the present file; I read only its first three lines (title and the start of a MINOR-verdict sentence) while diagnosing, then stopped. Conversely, my f115 draft may have transiently replaced the sibling's scratch copy; the f122 lane should verify its own `proof-review-v1.md` content/hash. This file was staged under the unique name `local://f115-proof-review-v1.md`; all `proof-f115-*` artifacts used unique names and were verified intact by content and hash.
* Sibling `finite-*` files in this directory were not read. A scratch probe (`local://f115-probe.txt`) exists only in session scratch.

## 10. Hashes

Inputs: as in §0 (full values in `proof-f115-hashes-v1.txt`). Own artifacts at the time of writing this file:
`proof-f115-finite-diagnostic-v1.py` `27a066db62bfa864227007f830f61ef1497748497de2160f190054eda6b9e442` (21069 B, 398 LF);
`proof-f115-finite-diagnostic-v1-run-FAILED.txt` `732b1a2d06865158bde912ebd15af4d4692181c8c1dd7ff8f114ae1c03fe3980` (2595 B, 32 LF);
`proof-f115-finite-diagnostic-v2.py` `67f5084e3be74211b207e29c92821df43f0c22880162e8c7e614e0080bc9568c` (21558 B, 404 LF);
`proof-f115-finite-diagnostic-v2-run.txt` `96c4b875817034fe12e0c8f1fcb9d03bca6c6b3a4771efc97964bb799914c2cc` (2398 B, 23 LF).
The SHA-256 of this file is recorded in `proof-f115-hashes-v1.txt`, written after it.
