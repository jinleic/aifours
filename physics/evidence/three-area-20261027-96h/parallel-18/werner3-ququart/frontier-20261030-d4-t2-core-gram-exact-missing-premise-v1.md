# The exact missing PSD/Gram premise of the rank-two dual inequality

**Status: WRITTEN-ONLY owner candidate, UNREVIEWED.** One substantive result under the 2026-10-30 future-only direction: a universal two-term identity for the operator-space polar form and the exact identification of the single frame-level inequality that would close the corrected rank≤2 partial-trace inequality `q(R)≤2||R||²` on the entire original dual domain — including the nonzero-trace, non-EP, both-supports≥3 core, whose narrowing remains **conditional on unreviewed antecedents** (my own bb09c6bf/b96fcf9f/4bb8a5de/ce6a6288 chain) until f288/f286/f289 return. **No computation, program, code, chosen operator/state, numerical instance or heavy run was used**; every statement below is a written all-variable derivation. Excluded inputs honored: quarantined cross-term episode, f284/f285 review bodies and dispositions, false f198. The (Q)⇔T2 frame is the corrected master chain (c9003960 + errata fd5cd81e, e2e7fd97), itself UNREVIEWED.

## 1. Two definitions and the universal identity

For ANY operator `R` on `C^m⊗C^n` define the Hermitian polar form

`G(R,R') := ⟨R,R'⟩_F + Tr(R†)Tr(R') − ⟨Tr_B R, Tr_B R'⟩_F − ⟨Tr_A R, Tr_A R'⟩_F`,

so that `q(R) = ||R||² + |TrR|²/2 − G(R,R)`. For `rank R ≤ 2` write the thin SVD `R = s1|u1⟩⟨v1| + s2|u2⟩⟨v2|` (`s1≥s2≥0`, both frames orthonormal) and define

`c_i = ⟨v_i,u_i⟩`, `γ = Tr R = s1c1+s2c2`, `p_i = ⟨u_i⊗v_i, (P_-^A⊗P_-^B)(u_i⊗v_i)⟩ ≥ 0`,

`C12 = ⟨Tr_B|u1⟩⟨v1|, Tr_B|u2⟩⟨v2|⟩_F + ⟨Tr_A|u1⟩⟨v1|, Tr_A|u2⟩⟨v2|⟩_F`, `δ := c1·conj(c2) − C12`.

**Identity.** `G(R,R) = 4(s1²p1 + s2²p2) + 2 s1 s2·Re δ`.  (1.1)

*Proof.* The pinned rank-one swap identity gives `||Tr_B|u_i⟩⟨v_i|||²+||Tr_A|u_i⟩⟨v_i|||² = 1+|c_i|²−4p_i`; expanding both partial traces of `R` in the orthonormal frames inserts the cross Gram `C12`; `|TrR|² = Σs_i²|c_i|² + 2s1s2·Re(c1 conj(c2))`. Substituting into `G(R,R)` cancels all diagonal `c`-terms against `||R||² = s1²+s2²`, leaving (1.1). Every step is a written expansion; no instance is evaluated. ∎

## 2. The exact missing premise (CORE-GRAM)

**CORE-GRAM.** For every doubly-orthonormal frame (`{u1,u2}`, `{v1,v2}` in any `C^m⊗C^n`):

`Re δ = Re( c1·conj(c2) − C12 ) ≥ −4√(p1 p2)`.  (2.1)

**Theorem (conditional chain, all written).** CORE-GRAM implies `G(R,R) ≥ 0` for every `rank R ≤ 2`, hence

`q(R) ≤ ||R||² + |TrR|²/2 ≤ 2||R||²`  (2.2)

(using `|TrR| ≤ s1+s2 ≤ √2·||R||`), hence (Q), hence — via the corrected master equivalence — the **full original T2 statement** for all traceless `A,B∈M4(C)`. *Proof of the first step:* by (1.1) and (2.1), `G(R,R) ≥ 4(s1²p1+s2²p2) − 8 s1 s2√(p1p2) = 4(s1√p1 − s2√p2)² ≥ 0`. ∎

**Sharpness/equivalence of the premise.** For a fixed frame, `G(R,R) ≥ 0` for ALL singular-value ratios `t=s1/s2>0` is EXACTLY equivalent to (2.1): (1.1) reduces it to `Re δ ≥ −2(t p1 + p2/t)` for all `t`, whose right side has infimum `−4√(p1p2)` at `t=√(p2/p1)`. The rank-one case `s2=0` is automatic. Thus CORE-GRAM is not an arbitrary strengthening: it is precisely the statement that the genuine Hermitian form `G` is nonnegative on the rank-two cone, uniformly in the singular values. At `p1=p2=0` it reads `Re(c1 conj(c2) − C12) ≥ 0`.

## 3. Why this is the FIRST missing premise, and what may not be assumed

`G` is a true Hermitian sesquilinear form on operator space (Gram pieces of `I`, `Tr`, `Tr_B`, `Tr_A`); its rank-one diagonal is `G(r,r)=4p(r)≥0` by the swap identity. The unpaid step is exactly positivity on rank-**two** sums, which by (1.1) is CORE-GRAM. The tempting shortcut — Cauchy–Schwarz for `G` on the rank-one variety, `|G(r1,r2)|² ≤ 16 s1²s2² p1 p2` — **must not be assumed**: the rank-one operators span but do not form a subspace, so positivity on the variety does not transfer to cross terms; that shortcut is stronger than CORE-GRAM and is not a consequence of any written fact. No impossibility claim is made about CORE-GRAM itself: it is open, and it is the exact target.

## 4. Scope and nonclaims

CORE-GRAM is SUFFICIENT for the full theorem but NOT known necessary: (Q) only requires `G(R,R) ≥ |TrR|²/2 − ||R||²`, a weaker demand with trace slack in `[−||R||², 0]`; a CORE-GRAM failure at some frame would not by itself refute T2. All content here is UNREVIEWED, rests on the corrected-but-unreviewed master chain and my own unreviewed antecedents for the narrowed core, and claims no unrestricted T2/T3/Z2/q3, no f274 `η>2L`, no physical counterexample, no execution, no novelty. Prior packet bytes and all holds/quarantines remain unchanged.
