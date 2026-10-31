# info-6 frontier: the even and odd radical phases must differ

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` before writing: **2026-10-28T21:23:32-0700 PDT**. **UNREVIEWED AUTHOR CANDIDATE**, additive to the immutable zero-phase result `frontier-20261028-fourzero-radical-phase-exclusion-v1.md`, SHA-256 `49b97bf0463870565cd8351ed44d86df1933cbf850767c86517072f13a8142ca`, 57 LF. No frozen review scope is changed; the original unrestricted problem remains open.

## Statement

For any actual balanced f:F₂⁹→{0,1} with full Walsh peak≤28 and exactly four Walsh zeros, let R be their rank-six even-half polar radical. Let `λ:R→F₂` be the even-half mod-8 radical functional, and `ρ:R→F₂` the odd-half Q radical linear functional, as in the pinned predecessor. Then

> **λ≠ρ as linear functionals on R.**

The previously excluded λ=ρ=0 case is included, and the equal nonzero case is now also excluded. The three types not eliminated here are `λ=0≠ρ`, `ρ=0≠λ`, and λ,ρ nonzero and linearly independent. In particular, a nonbalanced Q still forces the central `A₋₂+A₆` count; this theorem does not rule out the remaining four-zero branch.

## Character-modulated proof

Suppose λ=ρ and define the character `χ(r)=(−1)^{λ(r)}` of R. On each coset F=a+R put

    E_F=Σ_{r∈R} k(a+r)²,       S_F=Σ_{r∈R} χ(r)k(a+r).

The value S_F may change sign with the representative a, but S_F² does not. Multiplication by χ leaves E_F unchanged. On the zero fiber all entries are zero; on any other even q-zero fiber the modulated entries remain ±4.

On an even q-one fiber, the preceding fiber-rigidity theorem gives

    k(a+r) ≡ k(a)+4λ(r) (mod 8).

If λ(r)=1, the even value k(a) is 2 or 6 mod8, so `−k(a+r)≡k(a) mod8`. Hence all four modulated values are in one of the two classes `{−6,2}` or `{−2,6}`. On an odd fiber, Q changes by ρ(r)=λ(r), while negating an odd value exchanges its two mod-4 Q classes. All four modulated values therefore lie either in `{−7,−3,1,5}` or in its negative.

The three pointwise inequalities proved in the pinned predecessor apply verbatim to the **modulated** entries:

    S_F² ≥ 10E_F−640    on nonradical even q-zero fibers,
    S_F² ≥ 10E_F−864    on even q-one fibers,
    S_F² ≥ 10E_F−1464   on odd fibers.                                       (2)

There are `(z−4)/4`, `(256−z)/4`, and 64 of those fibers respectively, where z=|{q=0}| is 112 or 144. Parseval gives `Σ E_F=16,384`; summing (2) gives

    Σ_F S_F² ≥ 16,384+56(z−16) > 16,384.                                     (3)

But the exact Boolean autocorrelation caller says `R(0)=16,384`, `R(r)=0` for r≠0. Character orthogonality on each R-fiber gives

    Σ_F S_F² = Σ_{r∈R} χ(r)R(r) = 16,384,

contradicting (3). Hence λ≠ρ. ∎

The character sign is essential: omitting it leaves mixed-phase fibers which need not satisfy the pointwise bounds. This proof neither uses the exploratory solver's UNSAT status nor assumes any sign or magnitude ordering inside a fiber.

## Finite controls and pins

The separate control checks every allowed q-one, q-zero and odd four-entry pattern for each of the four equal functionals λ=ρ, and checks that deliberately omitting the character makes selected mixed-phase patterns violate the bounds. These controls supplement the all-variable proof and do not replace disjoint review.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-equal-phase-character-check.py` | `cfe6a14ada0380091f7dc9b046c28647c109e9adc4de2fe924c19817dda6a57b` | 44 |
| `frontier-20261028-equal-phase-character-check-result.json` | `1c2012652a38c8210eee836e0c3f0dfc24e4d70d636c33ed895f3ef5b4878714` | 27 |
| `frontier-20261028-fourzero-radical-phase-exclusion-v1.md` | `49b97bf0463870565cd8351ed44d86df1933cbf850767c86517072f13a8142ca` | 57 |
| `frontier-20261028-radical-fiber-autocorrelation-v1.md` | `7fef5e3cec28f32fe824f742ccdf1124b6b2019527e671e14ba9f4eee15a3260` | 56 |

No actual Boolean witness, general four-zero contradiction, or novelty claim follows. **END.**
