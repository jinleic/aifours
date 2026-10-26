# Reciprocal class — width positivity as a two-point monotonicity window, with exact contact values

Actual returned `/bin/date` BEFORE creation: **Sun Oct 25 22:45:23 PDT 2026**. InfoSPR7/info-2. **NEW WRITTEN LEMMA CANDIDATE**, word-independent. It applies to W_I, W_II and W_III of `reciprocal-class-exact-three-word-reduction-v10.md` (SHA256 `f19221c04fa29ae4ec5d3c4616efd1779bf6ff8e2241763dfa73fae1818ebfb7`), read with erratum-1 (`cd14290a4ab5aacc8452b79966beb2e8c87dbdecb2140100c53cf4d2c0bc93e1`).

The work is symbolic and exact. No numeric instance, interpreter, eval, program, CAS or GO is used.

## 1. Setting (v10 §2)

Let ΔE=Eplus−Eminus=2t(w1t²+w3t+w2), and put Δrev(t):=ΔE(t)/t=2(w1t²+w3t+w2). Here w1, w2, w3 are the coefficient half-widths, and the box has positive widths iff w1, w2, w3>0.

Every box in the reciprocal chart satisfies

- `P2−P3=t·Δrev·E_B` (so F=Δrev·E_B);
- `P3−P4=tΔO·O_B` with `ΔO(t)=t²Δrev(1/t)`;
- `P1+P3=P2+P4` and `P4(t)=t⁷P2(1/t)`.

## 2. Lemma A — the monotonicity window

**(i) Necessity.** If w1, w2, w3>0, then for all 0≤p<q:

`Δrev(p) < Δrev(q)`, and, when p>0, `Δrev(q)/q² < Δrev(p)/p²`.

Hence for every two positive points p<q,

`1 < Δrev(q)/Δrev(p) < (q/p)²`. (MW)

*Proof.* A quadratic with positive coefficients is strictly increasing on [0,∞). Also Δrev(t)/t²=2(w1+w3/t+w2/t²) is strictly decreasing on (0,∞). ∎

**(ii) Converse.** Suppose w2>0, Δrev is nondecreasing on [0,∞), and Δrev(t)/t² is nonincreasing on (0,∞). Then w3≥0 (from the derivative at 0) and w1≥0 (from the limit at ∞). So (MW), imposed for all pairs, is equivalent to nonnegative widths. Strict positivity of the widths is the strict version.

## 3. Lemma B — exact values of Δrev at every contact type

Let τ>0 be a contact, lying inside its corner's open cell, so E_B(τ)≠0. Since Δrev=(P2−P3)/(tE_B) and P2−P3=P1−P4:

| contact corner | identity used | Δrev(τ) | sign of E_B in that corner's cells |
|---|---|---|---|
| C2 (P2(τ)=0) | P2−P3=−P3 | −P3(τ)/(τE_B(τ)) | E_B<0 |
| C3 (P3(τ)=0) | P2−P3=P2 | P2(τ)/(τE_B(τ)) | E_B>0 |
| C1 (P1(τ)=0) | P2−P3=−P4 | −P4(τ)/(τE_B(τ)) | E_B<0 |
| C4 (P4(τ)=0) | P2−P3=P1 | P1(τ)/(τE_B(τ)) | E_B>0 |

Each value is a positive quantity, as it must be: the numerator and E_B have the stated opposite or equal signs, and the other pairings are positive away from their own contacts.

Also `Δrev(0)=F(0)=2w2`, and `Δrev(1/τ)=τ^{-3}(P3(τ)−P4(τ))/O_B(τ)`. The second identity comes from F(1/t)=t^{-6}(P4−P3) and E_B(1/t)=−t^{-3}O_B(t).

## 4. Consequence

Every pair of contacts, together with t=0 and the mirrored points 1/τ, gives an explicit exact inequality (MW) between pairing values and target-component values. These inequalities are necessary for W_I, W_II and W_III.

They depend only on the box structure, not on any chart parametrization. In particular, the exact small-r exclusion of `reciprocal-WI-small-r-exact-emptiness-v1.md` (SHA256 `a22b4ed15f143ef2aeda23f6d139ca9cf452012c58a48582c8ae3d8f25b289e6`) is a violation of the left inequality of (MW) near t=0. There, w3≤0 means Δrev fails to increase at 0.

## 5. Scope

This file supplies tools, not verdicts. No W_k is decided here, no point or emptiness is claimed, and nothing is said about the general class or universal SPR7. This is not formal, kernel, human, family, cross-vendor, executable or novelty acceptance, and not a GO. All four owner process majors and all parent findings remain; the cutoff and deadline are unchanged.
