# ADDENDUM-1 to Parts 20–22: entrywise hand reconstruction of the two-block decompositions

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Mon Oct 26 01:19:05 PDT 2026**. Exact WRITTEN arithmetic only, no interpreter of any kind. This addendum is ADDITIVE: Parts 20, 21 and 22 are pinned and unchanged.

**Purpose.** Parts 20–22 prove operator identities R_x = Σ(pieces) through the coefficient calculus (B1.1). As an independent check, this addendum recomputes individual matrix entries ⟨ij|·|kl⟩ of every piece directly from the explicit coefficient rows. It then confirms that they add up to the entry of R_x computed from the generators. A sign or moment slip in the calculus would show up as a mismatch here. None was found.

Notation: ⟨ij|X|kl⟩ is written (ij,kl). For a family, E[ψ(ij) conj ψ(kl)] uses the H1.2 rows.

## A1. Part21 at s=1

Parameters: x=(1,1,1,1), κ=1/2, ρ=3/4, a0=c0=1/2, b0^2=3, ν0^2=1/12. Hence:
- D=Ee=5/2, m=n=1/4;
- G=61/24, F1+F2=G, X1+X2=-1/4.

Pieces:
- core: rows [1,β,δ,0], [χ,1,β,0], [-δ,-χ,1,0], δ·row1;
- (1-ρ)[P(b)+P(c)];
- B3: rows (B,B,A+B,B), 0, (C,0,0,C/ν), (A+νC, A, A+A^2/B, A+C);
- Φ2 on (d,f,g) = [[5/2,1/4,1/4],[1/4,F1,X1],[1/4,X1,F1]];
- Φ1 on (e,f,g) = [[5/2,-1/4,-1/4],[-1/4,F2,X2],[-1/4,X2,F2]].

| entry | R_x from generators | core | (1-ρ)b,c | B3 | Φ2 | Φ1 | sum |
|---|---|---|---|---|---|---|---|
| (00,00) | a:1 + 3h:3 = 4 | 1 | 0 | b0^2=3 | 0 | 0 | 4 |
| (02,02) | 3d + 3h = 6 | κ^2=1/4 | 0 | a0^2+b0^2=13/4 | D=5/2 | 0 | 6 |
| (02,33) | 3d: 3 | 0 | 0 | a0^2+a0c0=1/2 | D=5/2 | 0 | 3 |
| (33,33) | 3d + 3e = 6 | 0 | 0 | a0^2+c0^2+2a0c0=1 | 5/2 | Ee=5/2 | 6 |
| (32,32) | 3d + 3g = 6 | κ^2ρ=3/16 | 0 | a0^2+a0^4/3=13/48 | 5/2+2m+F1 | F2 | 3/16+13/48+3+61/24 = 6 |
| (30,30) | 3d + 3f = 6 | 3/16 | 0 | a0^2+ν0^2c0^2=13/48 | 5/2+2m+F1 | F2 | 6 |
| (30,32) | 3d: 3 | κ^2E[χβ̄]=0 | 0 | a0^2=1/4 | 5/2+m+m+X1 | X2 | 1/4+3-1/4 = 3 |
| (01,01) | b:1 + 3h:3 = 4 | ρ=3/4 | 1/4 | b0^2=3 | 0 | 0 | 4 |
| (01,12) | b: 1 | ρ | 1/4 | 0 | 0 | 0 | 1 |
| (00,11) | a: 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| (00,02) | 3h: 3 | E[δ̄]=0 | 0 | b0^2=3 | 0 | 0 | 3 |
| (02,30) | 3d: 3 | sκ^2E[χ̄]=0 | 0 | a0^2=1/4 | D+m=11/4 | 0 | 3 |
| (20,33) | 3e: 3 | 0 | 0 | a0c0+c0^2=1/2 | 0 | Ee=5/2 | 3 |
| (20,02) | none: 0 | -κ^2=-1/4 | 0 | a0c0=1/4 | 0 | 0 | 0 |

Each B3 entry averages the listed products. Every cross term carrying e^{±i(θ-φ)}, e^{±iψ}, e^{2i(θ-φ)} or e^{2iψ} is dropped because its mean is 0. For example:
- (02,02): E|A+B|^2 = a0^2+b0^2;
- (33,33): E|A+C|^2 = a0^2+c0^2+2a0c0, since A C̄ = a0c0 exactly;
- (20,02): E[C conj(A+B)] = c0a0.

All fourteen entries match.

## A2. Part20 C39, symbolic in x

Pieces:
- product family rows [1,r,r^2,0], [-r̄,1,r,0], [-zr^2,r̄,1,0], [ur^2,vr^2,vr^3,0];
- mixed family (A=te^{iθ}, C=(z/t)e^{iθ}, B, ν);
- K_03 on (d,g) = [[2-t^2, w̄],[w, g1]];
- K_23 on (e,g) = [[E, -zw̄],[-z̄w, g2]];
- a leftover diagonal on f, g, h, j.

Write V2=|v|^2, W2=|w|^2, Z2=|z|^2 so that the table cells contain no vertical bars.

| entry | R_x | product | mixed | K_03 | K_23 | leftover | sum |
|---|---|---|---|---|---|---|---|
| (02,33) | 3z̄ | 0 | t^2z̄+z̄ | (2-t^2)z̄ | 0 | 0 | 3z̄ |
| (33,33) | 3Z2+3 | 0 | t^2 Z2 + Z2/t^2 + 2Z2 | (2-t^2)Z2 | E=3-Z2-Z2/t^2 | 0 | 3Z2+3 |
| (32,32) | 3W2+3 | V2 | t^2 W2 + t^4/b0^2 | (2-t^2)W2+2W2+g1 | g2 | 3-V2-W2-t^4/b0^2-g1-g2 | 3W2+3 |
| (02,32) | 3w̄ | E[r^2 v̄ r̄^3]=0 | t^2 w̄ | (2-t^2)w̄+w̄ | 0 | 0 | 3w̄ |

All four match identically in the free parameters.

## A3. Scope

These are hand recomputations of selected entries. They are consistency evidence, not a proof replacement. The proofs remain the operator identities of Parts 20–22. Nothing here is formal/kernel/executable/cross-vendor acceptance. **Original physics-3/P44 remains UNMET.**

**END OF ADDENDUM-1 (Parts 20–22).**
