# Seminormal physical hosts, the actual canonical map and same-q idempotents

**NEW AUTHOR WRITTEN INTERFACE CANDIDATE with finite controls; unreviewed/unadopted.** Native successful-check observation **Wed Oct 28 20:55:00 PDT 2026**. This establishes equivalence ONLY for the explicitly displayed physical Rees-action product, conditional on the named band-identity and actor-transport proofs. It does NOT adopt the remaining printed-book product convention, any D1–D4 disposition, general R/L separation, or the original Q1/Q2 conclusion.

## 1. Exact physical interface

Let S be ANY regular semigroup whose actual idempotence-context quotient `q:S→D=S/τ` is pure and completely simple. Let V be the locally regular band variety, SN the seminormal band variety, and κ_q the canonical physical map using the actual q.

At the physical multiplication `(a,(i,g,λ))(b,(j,h,μ))=(a α_(gP_(λ,j))(b),(i,gP_(λ,j)h,μ))`, the following are equivalent:

1. S embeds into some SN-band-by-CS physical product, with arbitrary actor and action.
2. The actual κ_q is injective.
3. Its band coordinate separates every pair of distinct idempotents e,f with `q(e)=q(f)`.

`frontier-20261028-local-regular-seminormal-equivalence-v1.md`, SHA `bf7af7afe0440fda2774231c99577fa1d36ebf4b12f70628eddc380a162663ee`, supplies the WRITTEN identity proof `V=SN`. The actual-q/all-physical-actor characterization in `frontier-20261028-regular-source-any-actor-characterization-v1.md`, SHA `73d3951b03ecdbc6574a21753665e612c28aa0570158e7936a7228e36deade5d`, supplies 1⇔2 at V scope. The direct 2⇔3 proof below is independent of a particular band identity and uses no unprovided R/L reduction.

This theorem is conditional on those named prior WRITTEN inputs and ordinary Rees/natural-order facts. If an input fails review, the direct separation lemma still stands at its stated pure-CS/same-q assumptions, but do not adopt the combined interface.

## 2. Direct idempotent separation implies full injectivity

Let φ:S→P(B,D) be ANY homomorphism over a pure CS q. Assume that whenever e,f∈E(S) have q(e)=q(f) and equal φ-band coordinates, e=f. Suppose `φ(s)=φ(t)`, so q(s)=q(t).

Choose s'∈V(s). Because q(s') is an inverse of q(s), the four elements `ss'`, `ts'`, `s's`, `s't` all have idempotent actors: the first pair has the same actor, and so does the second pair. Purity makes all four source elements idempotent. Equality φ(s)=φ(t), multiplied by φ(s') on the appropriate side, gives equal physical images of each pair; their actor values agree. The separation assumption yields

`ts'=ss'`,       `s't=s's`.

Hence

`t s' t=(ss')t=s(s't)=s(s's)=s`.

Both `t s'` and `s't` are idempotent, so `s=(t s')t=t(s't)` is precisely `s≤t` in the regular-semigroup natural order. The witnesses also satisfy `ts'=ss' R s` and `s't=s's L s`, covering the customary Green-class formulation. Interchanging s,t and using any inverse t' gives t≤s. Antisymmetry yields s=t. Thus idempotent separation makes φ injective. The converse is immediate. The argument uses no cancellation and applies even when s,t themselves are nonidempotent.

## 3. Comparable, R and L separation — explicit conditional reduction

Within a pure idempotent actor fibre q^(-1)(d), every element is idempotent and the fibre is a band. The physical product weight of d with itself is the group identity, so β restricts to a band homomorphism on that fibre.

Assume β separates comparable same-q idempotents, and separately separates same-q R-pairs and L-pairs. If e,f have the same q and β(e)=β(f), put `h=efe`, `k=fef`. Both lie in the same fibre, satisfy h≤e and k≤f, and have β(h)=β(e), β(k)=β(f). Comparable separation gives e=efe and f=fef. In a band this says e D f. Put p=ef: `e R p` and `p L f`, while β(p)=β(e)=β(f). R separation gives e=p, L separation gives p=f. Thus e=f.

Conversely full idempotent separation implies all three special cases. Therefore SEP is equivalent to comparable + R + L **when the three properties are stated for the same q and band map**. This purely algebraic reduction does NOT prove comparable separation or either general R/L property for the canonical band. Applying an earlier comparable-fibre theorem requires its own exact reviewed hypotheses/corrections.

## 4. Finite controls and limitations

`frontier-20261028-same-q-separation-reduction-checker-v1.py`, SHA `6b042a892d3fa2d2186d62c5e7f9a4388c36876ca2e66a47914c9dd9f1d3a521`, executed `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 20:55:00 PDT 2026**. It uses the genuine original-class45 source, its actual actor and its pinned25-element seminormal host. All42 ordered distinct same-q idempotent pairs are separated. The actor-only singleton-band model deliberately collapses nonidempotents `s=(0,1,0)`, `t=(0,3,0)` and the same-q idempotents `s's=(0,2,0)`, `s't=(0,0,0)`, illustrating the contrapositive mechanism.

The first development run at20:54:34 failed because I had mistyped the source table's fourth row; I corrected the literal row before the passing run. The passing program output was observed, but the attached hash command then used a duplicated path and failed; I ran only the corrected hash command, not the program again. These mistakes and the exact successful checker hash are disclosed rather than relabeled as earlier success.

The printed book calls for a “seminormal band by a completely simple semigroup” semidirect product. If its formal convention is the displayed physical Rees-action formula and the named source/actor hypotheses match, the theorem gives the corresponding conditional interface. The original text's exact product convention, arbitrary original source hypotheses and remaining D1–D4 obligations are not silently substituted or declared adopted. General R/L/SEP, Q1 and Q2 remain open; no independent, human/cross-vendor/formal proof or novelty clearance is claimed.
