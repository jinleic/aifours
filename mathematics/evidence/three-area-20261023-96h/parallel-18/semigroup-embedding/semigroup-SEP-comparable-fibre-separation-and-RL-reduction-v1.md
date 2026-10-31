# The canonical band separates comparable syntactic-fibre idempotents; SEP reduces to R/L pairs

Owner **MathSemigroup-2 / original math-4**. Clock before writing (`/bin/date`): **Tue Oct 27 06:19:44 PDT 2026**.

This is a **NEW AUTHOR-WRITTEN / UNREVIEWED** packet under Main's prospective v202 authority (`institute/runs/three-area-2026-10-23-96h/post-review-four-owner-qualified-original-primary-directions-v202.json`, a478df73a26f199d68a7fef5046f4f7718e27de59cf841e958bea601eb580172), MathSemigroup-2 section. Assurance: WRITTEN hand proofs, universally quantified. I used no interpreter, Eval, CAS, calculator, program, table, enumeration, solver, replay, CLI, nested agent or GO, and no selected finite control. Nothing here is claimed as formal, kernel, cross-vendor, novelty or priority acceptance.

## 0. Provenance and separation

**Mathematical sources.** The proofs use only:

- the adopted elementary SQ-E proof `semigroup-syntactic-idempotent-pure-CS-quotient-v2-elementary.md` (130 LF, 93f216ee1a14cf9d4c9aca0de9d807efff3bbd39471d233a040423eb1ebfa968);
- the universal-actor manuscript `semigroup-syntactic-actor-universal-canonical-host-v1.md` (205 LF, 788c2e31dbecc8ab8266abe08e94aae2ffd247eb7e2a0a7619d03fe899da24f4).

I read both completely in this session after v202. Their adoption is recorded in my whole-state chain as parent 8d745378; I did not re-read that parent record in this session.

**Ordinary facts used:**

- Green's relations and Green's lemma;
- the Clifford–Miller theorem;
- existence of inverses inside R-classes of a regular semigroup;
- the natural partial order;
- D-classes of a band are rectangular bands, hence antichains for the natural order;
- semilattices are subdirect products of the two-element semilattice;
- free objects in varieties of bands.

**NOT opened or used:**

- the withdrawn 171 LF file (9c6fc327…);
- any post-v3 globalization, corner, homogeneity or representation guidance, or anything that consumes it;
- the old 160 LF OI source;
- any v145 body or parent claim. Main lifted the v145 hold prospectively at 06:11 (`semigroup-v145-nonFULL-reassessment-after-complete-reads-v2.md`, f4111a7a…). That body was not opened, and nothing here depends on it.

**Method provenance.** Every construction below was derived in this session from three things:

1. the universal property and SEP criterion of U205 §§6–8;
2. the semilattice reflection of the canonical band;
3. Green-relation calculations.

The vertex closure in §4 is the ordinary Schützenberger-graph idea, applied to the source's own R-classes. It is recorded here in full.

## 1. Setting and notation

S is a nonempty regular semigroup that satisfies:

- book weak E-unitarity: if e = fa = ag with e, f, g idempotent, then a is idempotent;
- local orthodoxy;
- the original local regular-band hypothesis.

By SQ-E, q = q_τ : S → C = M[G; I, Λ; P] is an onto, idempotent-pure homomorphism onto a completely simple semigroup. Write q(s) = (i_s, g_s, λ_s) and

`w(s,t) = g_s p_(λ_s, i_t)`.

Then q(st) = (i_s, w(s,t)g_t, λ_t). Hence:

- **(P1)** g_st = w(s,t)·g_t;
- **(P2)** w(s,tr) = w(s,t);
- **(P3)** w(st,r) = w(s,t)·w(t,r).

From U205 §6 we have:

- **The canonical band.** B_q is the free V-band on A = {X_(u,s) : u ∈ G, s ∈ S}, modulo X_(u,s)X_(v,t) = X_(u,st) whenever v = u·w(s,t) (relation M).
- **The coordinate map.** β(s) = [X_(1,s)].
- **SEP.** For idempotents e, f with q(e) = q(f), β(e) = β(f) implies e = f.

U205 Theorem U5 states:

> S embeds into some allowed host ⟺ SEP.

**Fibres.** For an idempotent c of C, let E_c = q⁻¹(c). By purity E_c ⊆ E(S). It is a subband, since q(ef) = c² = c. For a ∈ E_c, the corner aE_c a is a subband of E(aSa), which is a regular band, so E_c ∈ V.

For e, f ∈ E_c we have w(e,f) = p_(λ,i)⁻¹·p_(λ,i) = 1, so β(e)β(f) = β(ef). Thus β restricted to E_c is a band homomorphism, and **SEP ⟺ β|E_c is injective for every c**.

**Hosts.** For a band B ∈ V with G-action α, a *host over q* is a homomorphism j : S → P(B,C), written j(s) = (b_s, q(s)), with b_st = b_s·α_w(s,t)(b_t). By the universal property in U205 §6, every host j induces an equivariant θ : B_q → B with θ(β(s)) = b_s. Hence **j(e) ≠ j(f) implies β(e) ≠ β(f)**.

## 2. Theorem A — exact decomposition of SEP

SEP holds if and only if the following three conditions hold for every idempotent c of C:

- **(LEQ)** if e < f in E_c, then β(e) ≠ β(f);
- **(R)** if e, f ∈ E_c, ef = f, fe = e and e ≠ f, then β(e) ≠ β(f);
- **(L)** if e, f ∈ E_c, ef = e, fe = f and e ≠ f, then β(e) ≠ β(f).

*Proof.* The forward direction is trivial.

For the converse, let e, f ∈ E_c with β(e) = β(f).

1. Then β(efe) = β(e)³ = β(e), and efe ≤ e. By (LEQ), efe = e.
2. Similarly, fef = f.
3. Next, β(ef) = β(e)β(f) = β(e).
4. Using efe = e and fef = f:
   - e(ef) = ef and (ef)e = efe = e, so e and ef are R-related;
   - (ef)f = ef and f(ef) = fef = f, so ef and f are L-related.
5. By (R), e = ef. By (L), ef = f. Hence e = f. ∎

## 3. Theorem B — exact criterion for comparable pairs

**Placements.** Call (u,s) ∈ G × S a placement. Define two operations:

- *composition*: (u,s) and (u·w(s,t), t) give (u, st);
- *factorization*: (u, st) gives (u,s) and (u·w(s,t), t).

A set Ψ of placements is **closed** if it is closed under both operations. Let Ψ_f be the smallest closed set containing (1,f).

**Theorem B.** Let e ≤ f in E_c. Then β(e) = β(f) if and only if (1,e) ∈ Ψ_f. When (1,e) ∉ Ψ_f, the following semilattice host separates e and f:

- B = {0,1}^G with pointwise maximum (a semilattice, so B ∈ V);
- G acts by (α_v b)(x) = b(v⁻¹x);
- b_s(x) = 1 if and only if (x⁻¹, s) ∉ Ψ_f.

*Host check.* Closedness gives: (x⁻¹, st) ∉ Ψ_f if and only if (x⁻¹, s) ∉ Ψ_f or (x⁻¹w, t) ∉ Ψ_f, where w = w(s,t). Since (w⁻¹x)⁻¹ = x⁻¹w, this says

b_st(x) = max(b_s(x), b_t(w⁻¹x)) = (b_s·α_w(b_t))(x).

So j(s) = (b_s, q(s)) is a host. It separates e and f because b_e(1) = 1 and b_f(1) = 0.

*Converse.* The semilattice reflection Y_q of B_q is presented by the generators A and the joins [s@u] ∨ [t@uw] = [st@u]. This holds because semilattices lie in V, so assignments into semilattices that respect M extend from F_V(A) through B_q.

Let h : Y_q → ({0,1}, max) be a homomorphism. Then h⁻¹(0) is closed: it is closed under composition because of the join relation, and under factorization because each factor lies below the product. Conversely, every closed set arises this way.

Now compare the two images:

- Since e = e·f with w(e,f) = 1, every h satisfies h(e@1) ≥ h(f@1).
- (1,e) ∈ Ψ_f means that every closed set containing (1,f) contains (1,e). So every h satisfies h(e@1) ≤ h(f@1).

Therefore β(e) and β(f) have the same image in every semilattice quotient, so β(e) D β(f) in B_q. Also β(e) = β(e)β(f) = β(f)β(e), so β(e) ≤ β(f). Since D-classes of a band are antichains, β(e) = β(f). ∎

## 4. VERT, closure of the vertex set, and Theorem C (LEQ always holds)

Fix an idempotent f. For a ∈ R_f, put π(a,s) = g_a·p_(λ_a, i_s), and define

`Ψ°_f = { (π(a,s), s) : a ∈ R_f and as ∈ R_f }`.

**Lemma 4.1.** Ψ°_f contains (1,f) and is closed under factorization.

*Proof.*

- *Contains (1,f).* Take a = f: π(f,f) = p_(λ,i)⁻¹·p_(λ,i) = 1, and ff = f ∈ R_f.
- *Left factor.* Suppose a ∈ R_f and ast ∈ R_f. The chain ast ≤_R as ≤_R a, together with ast R a, gives as ∈ R_f. Also π(a,st) = π(a,s), because i_st = i_s.
- *Right factor.* The vertex as witnesses t, and

  π(as, t) = g_a·p_(λ_a, i_s)·g_s·p_(λ_s, i_t) = π(a,s)·w(s,t). ∎

**Lemma 4.2 (VERT).** Suppose a1, a2 ∈ R_f, t ∈ S, r := a2·t ∈ R_f, and q(a1·t) = q(a2·t). Then a1·t ∈ R_f.

*Proof.*

1. **Inverses.** For any x ∈ R_f there is x* ∈ V(x) ∩ L_f with x·x* = f: take any x' ∈ V(x) and set x* = x'f. In particular, choose r* with r·r* = f, and a_k* with a_k·a_k* = f. Put z_k = a_k*·a_k (an idempotent) and u12 = a2*·a1.
2. **Relations among them.**
   - Since f·a1 = a1, we get a2·u12 = a1.
   - u12·(a1*·a2) = a2*·f·a2 = z2.
   - z2·u12 = u12.
   - Hence u12 R z2.
3. **The element T'.** Put T' = t·r*·a2. Then:
   - z2·T' = a2*·(a2·t)·r*·a2 = a2*·f·a2 = z2;
   - T'·z2 = t·r*·f·a2 = T'.

   So T' L z2. Moreover T'T' = T'·(z2·T') = T'·z2 = T', so T' is idempotent.
4. **p' is an idempotent below z2.** Put p' = u12·T'. Using the hypothesis,

   q(p') = q(a2*)·q(a1·t)·q(r*·a2) = q(a2*)·q(a2·t)·q(r*·a2) = q(z2·T') = q(z2),

   which is idempotent. By purity, p' is idempotent. Also z2·p' = p' = p'·z2, so p' ≤ z2.
5. **w0 is idempotent.** By cyclic idempotence (SQ-E Lemma 2.2), w0 := T'·u12 is idempotent.
6. **Clifford–Miller twice.** All of these elements lie in D_(z2).
   - L_(T') ∩ R_(u12) = L_(z2) ∩ R_(z2) contains z2. So w0 = T'·u12 ∈ R_(T') ∩ L_(u12).
   - Hence L_(u12) ∩ R_(T') contains the idempotent w0. So p' = u12·T' ∈ R_(u12) ∩ L_(T') = H_(z2).
   - p' is an idempotent in H_(z2), so p' = z2.
7. **Conclusion.** Conjugate by a2 and a2*:

   f = a2·z2·a2* = a2·u12·T'·a2* = a1·t·r*·f = a1·t·r*.

   So f ∈ a1·t·S. Since also a1·t ∈ fS, we get a1·t R f. ∎

**Lemma 4.3 (COMP).** Ψ°_f is closed under composition.

*Proof.* Let (u,s) be witnessed by a, and let (u·w(s,t), t) be witnessed by b. Put v = as ∈ R_f. By Lemma 4.1, π(v,t) = u·w(s,t) = π(b,t). Both v and b lie in R_f (row i), so this equality is equivalent to q(vt) = q(bt). VERT, applied with a1 = v and a2 = b, gives ast ∈ R_f. Hence (π(a,st), st) = (u, st) ∈ Ψ°_f. ∎

**Theorem C (LEQ).** For every original S, every idempotent c of C, and every pair e < f in E_c, we have β(e) ≠ β(f). They are separated by the semilattice host of Theorem B.

*Proof.* By Lemmas 4.1 and 4.3, Ψ°_f is closed and contains (1,f), so Ψ_f ⊆ Ψ°_f.

Suppose (1,e) ∈ Ψ°_f. Then there is a ∈ R_f with ae ∈ R_f and g_a·p_(λ_a, i) = 1. Therefore q(ae) = c, so ae is idempotent by purity. Since ae and f are R-related idempotents, (ae)·f = f. But (ae)·f = a·(ef) = ae, so ae = f. Then fe = (ae)·e = a·(ee) = ae = f, while fe = e because e ≤ f. Hence e = f, contradicting e < f.

So (1,e) ∉ Ψ_f, and Theorem B applies. ∎

**Remark 4.4.** The earlier "2×2 grid" test is a special case of VERT and gives no obstruction. In that test, x, x' ∈ R_f with q(x) = q(x') and xy = x'y' = f; the conclusion is xy' = f.

## 5. Corollaries: semilattice level, and a new positive class

**Corollary D1.** Let

`H_S = P( ∏_(f ∈ E(S)) {0,1}^G , C )`,

with coordinates b^(f) given by Theorem B for Ψ_f. Then H_S separates every pair e, f in a common fibre with efe ≠ e or fef ≠ f.

*Proof.* Suppose efe < e. The coordinate b^(e) separates efe from e. If j(e) = j(f), then j(efe) = j(e), a contradiction. The case fef < f is symmetric. ∎

Equivalently, for every c the structure semilattice E_c/D embeds into the semilattice reflection of B_q.

**Corollary D2 (new positive class).** Suppose every fibre E_c is a semilattice, that is, τ-related idempotents commute. Then S embeds into P(Y, C), where Y = ∏ {0,1}^G is a semilattice, and so lies in V. The original embedding question therefore has a positive answer for every such S.

*Proof.* In a semilattice fibre, e ≠ f implies ef ≠ e or ef ≠ f, so D1 separates the pair. The injectivity argument of U205 §7 uses only that j is a host over q separating idempotents with equal q-image, so it applies to j:

1. If j(s) = j(t), choose s' ∈ V(s).
2. Purity makes s't and ts' idempotent.
3. Separation gives s's = s't and ss' = ts'.
4. Hence s = (ts')·t = t·(s't), so s ≤ t. Symmetrically t ≤ s, so s = t. ∎

**Scope note.** D2 is a written author-level theorem at the union of SQ-E, U205 and this packet. No literature or novelty status is claimed. In particular, I do not claim that every member of the class is new; the E-unitary inverse case is classical and is consistent with D2.

## 6. Exact remaining gap: (R) and (L), and a sufficient criterion

By Theorems A and C, **SEP (equivalently, the original embedding question for S) holds if and only if every R-pair and every L-pair lying inside a rectangular D-class of a syntactic fibre is separated by β.** Neither the semilattice reflection nor the CS quotients ξ ⊆ τ can do this in general. For example, in the band {g, e, f} with g an identity and {e, f} right zero, τ and ξ are both universal, yet S embeds into itself.

**Theorem E (sufficient criterion for an R-pair).** Let e ≠ f be an R-pair in E_c. Suppose there is a closed Ψ with (1,e) ∉ Ψ (equivalently (1,f) ∉ Ψ) such that (1,e) and (1,f) lie in different classes of the equivalence ≈_Ψ defined as follows. Let O be the complement of Ψ. Then ≈_Ψ is the equivalence on O generated by:

- (u,st) ≈ (u·w(s,t), t) whenever (u·w(s,t), t) ∈ O;
- (u,st) ≈ (u,s) whenever (u·w(s,t), t) ∈ Ψ (and (u,st) ∈ O).

Then β(e) ≠ β(f). A separating host is built as follows:

- Let Z = O/≈_Ψ, and let R¹ = Z ∪ {1} be the right-zero band Z with an identity adjoined. R¹ is right regular, hence regular, hence in V.
- Let B = (R¹)^G, with pointwise product and translation action.
- Set b_s(x) = 1 if (x⁻¹, s) ∈ Ψ, and b_s(x) = [(x⁻¹, s)] otherwise.

*Host check.*

- If (x⁻¹w, t) ∈ O, then (x⁻¹, st) ∈ O and b_st(x) = [(x⁻¹w, t)] = b_s(x)·b_t(w⁻¹x).
- If (x⁻¹w, t) ∈ Ψ, then b_t(w⁻¹x) = 1, and either:
  - both (x⁻¹, s) and (x⁻¹, st) lie in Ψ, giving 1 = 1; or
  - both lie in O and are ≈_Ψ-equivalent, giving equal classes.

The dual criterion, using left-zero labels and prefixes, handles L-pairs.

**Special cases.**

- Ψ = ∅ gives right-zero hosts. In that case b_t = (g_t, comp(t)), where comp is constant on left-multiplication components. These are too coarse whenever a completely simple kernel exists.
- In the example band, taking Ψ = Ψ_g (the closure of the common right identity) cuts the link through g. This works because (1,e) and (1,f) lie outside Ψ_g by Theorem C, since e < g and f < g.

**The open part, stated exactly.** It remains to construct, for an arbitrary original S and every R-pair (dually L-pair) in a fibre, either:

- a closed Ψ satisfying Theorem E, or some other V-host separating the pair; or
- an actual original-class source with an R-pair (or L-pair) e ≠ f that is identified by every host. By U5, such a source is an all-host obstruction.

I claim neither here. I do not claim that Theorem E is necessary, beyond the right-regular reflection.

## 7. Status and boundaries

**WRITTEN author-level results of this packet:**

- Theorem A (decomposition);
- Theorem B (exact comparable criterion and its semilattice host);
- Lemma 4.2 VERT and Lemma 4.3 COMP;
- Theorem C (LEQ for every original S);
- Corollaries D1 and D2 (the positive class with commuting τ-related idempotents);
- Theorem E (sufficient R/L criterion).

The original problem is **NOT** solved in general. The exact first unproved statement is now (R)/(L) separation inside rectangular D-classes of syntactic fibres.

This packet needs its own full mathematics review and its own dependency/application review before any parent use. No earlier source is edited. Earlier withdrawals, quarantines (ENTIRE 171 ZERO; post-v3 guidance ZERO), process findings, HOLD, N4 UNKNOWN and aux214 STOP all remain. Science cutoff 2026-10-27T11:05:38-07:00; delivery deadline 12:35:38-07:00.
