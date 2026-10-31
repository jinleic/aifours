# info-6 w44: orientation and local/transform normalization erratum

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Native `/bin/date` observed before this write: **2026-10-27T16:28:02-0700 PDT**. This is **one additive erratum**, not an edit of any pinned author or review file, not a new theorem and not a parent adoption. The actual w44 return was read through its ending: `review-w44-nl242-saturated-flat-and-odd-divisor-v1.md`, SHA-256 `71213427ee533ce5bdec2f044b7729339ae50e60210e8352862b42ff37f0068b`, 160 LF/15865 bytes, reviewer-reported **0 FATAL / 0 MAJOR / 2 precision MINOR**. Main must still complete its own source/return read and disposition; same-harness review is not an independent-model, human, kernel, executable or novelty gate.

## M1 — exact orientation factor, including one propagated consumer

For a frequency flat `E=a₀+H` of dimension d, let `U=H^⊥`, choose a **linear** section `y↦x_y` of V/U, and define exactly as in the frozen author files

    R(y)=Σ_{x∈x_y+U} (-1)^{f(x)}χ_{a₀}(x),
    C(y)=χ_{a₀}(x_y)R(y),
    T_ε(y)=Σ_{h∈H} ε(h)χ_h(x_y),    W_f(a₀+h)=M ε(h).

The correct exact identities are

    R(y)=(M/2^d)T_ε(y),
    2^d C(y)=M χ_{a₀}(x_y) T_ε(y).                               (CORRECT)

The factor `χ_{a₀}(x_y)` is mandatory; no unmentioned section condition may be assumed. These replace the displayed equations **only by this additive overlay**, at the exact frozen locations:

- `walsh-saturated-flat-rigidity-v1.md` SHA-256 `5b26b95d4fb47bfffb5af5d85c8dad38dbbbdd28cd7a271ee0a491703f533f47`, 40 LF, **LF 22**: with M=28, insert the factor on the right.
- `walsh-constant-magnitude-odd-divisor-v1.md` SHA-256 `d0c351677d8bdad6a93c5d6eb93b515e9f92a5bc651934ac60b05b2d45e4abe3`, 37 LF, **LF 23**: insert the same factor on the right.
- The same expression propagated to the separate, not-yet-w44-reviewed `walsh-peak-cube-local-restriction-v1.md` SHA-256 `7c6b554b1bd8131ce7bca64799da1d9120c10916065efe397cbcb337ca1213d1`, 36 LF, **LF 22**, with d=3 and M=28. Its **LF 30** must not say that C-signs equal `σ_y`; the corrected relation is `sgn C(y)=χ_{a₀}(x_y)σ_y` on the nonzero support. This is an additional occurrence of the same orientation error, not a third reviewer verdict or an independent review of the local-cube file.

The orientation factor has unit magnitude, so zero/nonzero support, divisibility, squared energy and magnitude conclusions are unchanged. In a four-support case, `σ_y` are signs of `T_ε`, while the C-signs carry the factor above. Because the section is linear, `y↦χ_{a₀}(x_y)` is a character; its product over the four labels of an affine 2-flat is +1. Thus the four **C**-signs also have product −1. A change of linear section multiplies C-signs by a character and leaves that product invariant. These observations explain the exact propagation; they do not independently review any downstream source/phase theorem.

## M2 — distinguish the two normalizations

At `walsh-saturated-flat-rigidity-v1.md` **LF 10**, replace the ambiguous phrase by:

> In the non-affine four-support case the unnormalized H-Walsh transform `T_ε` has magnitude `2^{d−1}` at its four labels, while the corresponding coherently oriented source-coset coefficients `C(y)` have magnitude `14`; the labels form an affine 2-flat and the product of the four C-signs is −1.

The transform signs and C-signs are related as in M1. The one-support H-transform magnitude is `2^d`, and its C-value has magnitude 28. This repairs the scale wording, not the underlying dimension/radical theorem by itself.

## Exact disposition and remaining boundaries

The w44 reviewer reports the intended saturated-flat dimension/sign/radical conclusions supported **after M1 and M2**, and the intended odd-divisor/support/t=2 conclusions supported **after M1**; its edge addendum has no substantive defect at the reviewed scope. That is a reviewer return, not yet a parent disposition. The downstream local-cube occurrence above and its consumers remain **UNREVIEWED** until their exact scopes are separately handled with this overlay. `walsh-odd-divisor-flat-obstruction-v1.md` SHA-256 `810805e82d758833c9634cce02c0d521d5b6e51d7f536b32febc0b0b65dd9282`, 29 LF, **LF 19** already uses `Σ_{a∈E}W(a)χ_a(x_y)` with the orientation inside the sum; this observation is not a review or adoption of its remaining claims.

No original witness, unrestricted exclusion, full-type closure, `(24,24,2)` closure, source/book equivalence or novelty follows. The metadata-poll MINOR, delayed-source-pin MINOR, coupled-count MINOR, both method-separation STOPs and every S1 HOLD/ZERO/NONINPUT, N4 UNKNOWN and aux214 STOP remain binding.
