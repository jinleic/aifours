# Addendum 1 — dual VERT, closed-suffix lemma, and two impossible R-pair obstructions

Owner **MathSemigroup-2 / original math-4**. Clock before writing (`/bin/date`): **Tue Oct 27 06:28:41 PDT 2026**.

This is an additive **AUTHOR-WRITTEN / UNREVIEWED** successor to `semigroup-SEP-comparable-fibre-separation-and-RL-reduction-v1.md` (d7e9a9a269a6b9805c62a1d24da3c79d293988f5c72dbf24ee56dc7aec309d5a), which is not edited.

- Authority, sources, exclusions and assurance are the same as in that packet's §0.
- The proofs are WRITTEN by hand only.
- Notation is that packet's: placements, closed sets Ψ, closures Ψ_X, w(s,t), fibres E_c.

## 1. Duality

S^op is again an original-class semigroup: regularity, book weak E-unitarity, local orthodoxy and local regular bands are all self-dual. The syntactic congruence τ uses two-sided contexts, so the same map q is a pure onto homomorphism S^op → C^op, and C^op is completely simple. Hence every lemma of the main packet holds for S^op. Its R-classes are the L-classes of S.

**Lemma 1.1 (VERT^L).** Let t ∈ S. Suppose b1, b2 ∈ L_t, s ∈ S, s·b2 ∈ L_t and q(s·b1) = q(s·b2). Then s·b1 ∈ L_t.

*Proof.* Apply main Lemma 4.2 in S^op to the idempotent t'·t, which is L-related to t. ∎

## 2. The dual vertex closure of a placement

Fix a placement (v,t). For b ∈ L_t, put u_b = v·g_t·g_b⁻¹; this is the placement of b that ends where (v,t) ends. Define

`Ψ^L_(v,t) = { (u_b·w(s,b)⁻¹, s) : b ∈ L_t and s·b ∈ L_t }`.

**Lemma 2.1.**
- (a) Ψ^L_(v,t) contains (v,t).
- (b) Ψ^L_(v,t) is closed.
- (c) Consequently, Ψ_(v,t) ⊆ Ψ^L_(v,t).

*Proof.*

(a) Take b = t'·t. It is idempotent, b L t, and t·b = t. Since g_b = p_(λ_t, i_b)⁻¹, the position of t is

u_b·w(t,b)⁻¹ = v·g_t·g_b⁻¹·p_(λ_t, i_b)⁻¹·g_t⁻¹ = v.

(b) Direct proof in S. Write ε = v·g_t, and for any x ∈ S put u_x = ε·g_x⁻¹, so that g_x = u_x⁻¹·ε. By (P1), u_(s·b) = ε·(w(s,b)·g_b)⁻¹ = u_b·w(s,b)⁻¹. So the placement of an edge s before a vertex b is u_(s·b).

- **Factorization.** Let (p, s1·s2) have witness b, so s1·s2·b ∈ L_t and p = u_(s1·s2·b).
  - The chain s1·s2·b ≤_L s2·b ≤_L b, with s1·s2·b L b, gives s2·b ∈ L_t.
  - Witness b places s2 at u_(s2·b). Witness s2·b places s1 at u_(s1·s2·b) = p.
  - By (P2), g_(s1·s2·b) = w(s1,s2)·g_(s2·b), so p·w(s1,s2) = u_(s2·b).
  - Hence (p, s1) and (p·w(s1,s2), s2) lie in Ψ^L_(v,t), exactly as factorization requires.
- **Composition.** Let (p, s1) have witness b1 (s1·b1 ∈ L_t, p = u_(s1·b1)), and let (p·w(s1,s2), s2) have witness b2 (s2·b2 ∈ L_t, u_(s2·b2) = p·w(s1,s2)). Put b' = s2·b2 ∈ L_t.
  - Position: u_(s1·s2·b2) = u_(s2·b2)·w(s1,s2)⁻¹ = p.
  - Equal images: both s1·b1 and s1·b' have row i_(s1) and column λ_t. Their group coordinates agree: g_(s1·b1) = p⁻¹·ε, and g_(s1·b') = w(s1,s2)·g_(s2·b2) = w(s1,s2)·(p·w(s1,s2))⁻¹·ε = p⁻¹·ε. So q(s1·b1) = q(s1·b').
  - Lemma 1.1 (applied to s1, the given s1·b1 ∈ L_t, and b') gives s1·s2·b2 = s1·b' ∈ L_t.
  - Hence (p, s1·s2) ∈ Ψ^L_(v,t), with witness b2.

(c) follows from (a) and (b). ∎

**Lemma 2.2 (closed suffix).** Let x, t ∈ S and w = w(x,t). If (1,x) ∈ Ψ_(w,t), then x·t L t.

*Proof.*

1. By Lemma 2.1, (1,x) = (u_b·w(x,b)⁻¹, x) for some b ∈ L_t with x·b ∈ L_t.
2. The vertex t itself has u_t = w, and the dual position of x before t is w·w(x,t)⁻¹ = 1. So x is placed identically before b and before t.
3. Equal placements and equal end points give q(x·b) = q(x·t). The group coordinate is u⁻¹·v·g_t in both cases, the row is i_x and the column is λ_t.
4. Lemma 1.1 gives x·t ∈ L_t. ∎

## 3. Two natural all-host obstructions for R-pairs are impossible

**Background.** In every host j and every band B, if [b_x] ≥ [α_w(b_t)] in the structure semilattice of B, then b_x·α_w(b_t) L α_w(b_t). The reason: put d = α_w(b_t); in a band, [x] ≥ [d] gives d·x·d = d. Moreover, (1,x) ∈ Ψ_(w,t) forces [b_x] ≥ [α_w(b_t)], because the set {(u,s) : [α_u(b_s)] ≥ [α_w(b_t)]} is closed.

Consequently, consider a configuration:

- **(OP)** e ≠ f is an R-pair in E_c, e = x·t and f = y·t with w(x,t) = w(y,t) = w, and (1,x), (1,y) ∈ Ψ_(w,t).

Such a configuration would force b_e L b_f and b_e R b_f, hence b_e = b_f in every host. By U5 it would be an actual all-host obstruction.

**Proposition 3.1.** (OP) never occurs in an original-class S.

*Proof.* Lemma 2.2 gives e = x·t L t and f = y·t L t. So e L f. Together with e R f this gives e H f. Two idempotents in one H-class are equal, so e = f. ∎

**Proposition 3.2 (common right identities are cut simultaneously).** Let e ≠ f be an R-pair in E_c. Call k ∈ E(S) a common right identity if e·k = e and f·k = f, and put w_k = w(e,k) = w(f,k). Then:

- (a) (1,e) ∉ Ψ_(w_k, k), and likewise (1,f) ∉ Ψ_(w_k, k).
- (b) The union Ψ_RI of the sets Ψ_(w_k, k), taken over all common right identities k, is closed and contains neither (1,e) nor (1,f).

*Proof.*

(a) The placements (1,e) and (1,f) lie in exactly the same closed sets: e = f·e and f = e·f, and w(f,e) = w(e,f) = 1. If (1,e) were in Ψ_(w_k, k), Proposition 3.1 with x = e, y = f, t = k would give e = f.

(b) Let k1, k2 be common right identities.

1. **The product is a common right identity.** e·k1·k2 = e and f·k1·k2 = f. Also q(k1·k2) = q(k1), because both images are idempotents of column λ. So k1·k2 is idempotent by purity.
2. **It sits at the right position.** Since w(e,k1)·w(k1,k2) = w(e,k2), we have (w_k1, k1)·(w_k2, k2) = (w_k1, k1·k2).
3. **Its closure contains both.** Ψ_(w_k1, k1) ∪ Ψ_(w_k2, k2) ⊆ Ψ_(w_k1, k1·k2).
4. **Conclusion.** The family is therefore directed. A directed union of closed sets is closed, and by (a) no member contains (1,e). ∎

**Meaning.** In Theorem E of the main packet, take Ψ ⊇ Ψ_RI. Then every ≈_Ψ link through a common right identity is cut. This is exactly what is needed in the band {g, e, f}. It does **NOT** prove (R) in general: other link types (outside suffix chains that do not pass through a common right identity) are not yet controlled.

## 4. Status

**New WRITTEN author-level results:**

- Lemmas 1.1, 2.1 and 2.2;
- Propositions 3.1 and 3.2.

The original problem is still not solved in general. The remaining gap is exactly (R)/(L) of the main packet, now with:

- the closed-suffix obstruction (OP) excluded;
- common-right-identity links cut uniformly.

The same review requirements, quarantines and limits as in the main packet apply.
