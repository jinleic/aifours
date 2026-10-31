# A minimal weak obstruction must reach higher odd-root bands

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:50:11 PDT 2026**. **WRITTEN universal necessary theorem candidate**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. It concerns the weak original-box certificate, not the direct strictly-negative-coordinate certificate.

## Statement

Let \(K\) be any all-Hurwitz independent monic septic box with globally ordered odd-root bands \([a,b],[c,d],[e,f]\). Suppose a weak odd-canceling/eight-Vieta-vertex no-go measure has, after merging coincident nodes and removing odd-zero atoms, at most **five** distinct positive finite nodes, with an optional infinity atom. Then it must have
\[
\#\{i:t_i\in[c,d]\}\ge1\quad\text{or}\quad
\#\{i:t_i\in[e,f]\}\ge2. \tag{1}
\]
In other words, no such no-go exists if no selected finite node lies in the second odd-root band and at most one lies in the third. The counts use **distinct** positive finite frequencies; band endpoints are included. This is a necessary geometric restriction, not a claim that satisfying (1) suffices for a certificate.

## Proof

Assume the contrary. The six-location and minimal-pair theorems in `frontier-20261029-vieta-weak-obstruction-six-support-v1.md`, SHA-256 `d6ffee1555fbde2dd7e29d477c64ceab07632db3b6eb6cc69b90e5ac3267cc0b`, and `frontier-20261029-minimal-weak-circuit-pair-v1.md`, SHA-256 `9993e2e0bf89bf36a3dfc4efc42b98f466c138e6fd6f952a55c854400d4a1282`, imply that the no-go has exactly five retained finite nodes, a positive infinity atom, and is a positive combination of two four-finite-plus-infinity odd circuits. A five-finite-only circuit cannot be a constituent in this minimal no-go: its odd signs would alternate, whereas the mandatory reversed even-band pair forces one adjacent repeated odd sign.

In either circuit the finite odd signs are \((- ,+,-,+)\). Before the first odd band every actual odd value is positive; in \((b,c)\) it is negative; in \((d,e)\) it is positive; after the third odd band it is negative. No selected node is in \([c,d]\), and at most one is in \([e,f]\).

The first two circuit nodes must both lie in \((a,b)\). The first is negative, so it cannot precede \(a\). If the second positive node were later than \(b\), it would lie in \((d,e)\) or in the third band. A later negative third node could then only lie in the third band or after it; a subsequent positive fourth node would require a *second* third-band node. This contradicts the hypothesis. Hence the second lies in the first band and, because it follows a negative node, the first does too.

The negative third node lies strictly before \(c\). Otherwise, with no second-band nodes it must be in the third band or after it; a later positive fourth node would again require a second third-band node. Finally the fourth node cannot lie in \((c,d)\), by the hypothesis.

Both circuits therefore satisfy the corrected first-band four-circuit exclusion: their first two nodes lie in the first odd band, their third is before \(c\), and their fourth is outside \((c,d)\). The relevant source is `frontier-20261029-first-band-four-circuit-extension-v1.md`, SHA-256 `02014c2e520266977bb9fd157dbb5e92793513190d9c89c2c932c0566e79d465`, **only with both mandatory corrections** `frontier-20261029-first-band-second-odd-tail-erratum-v1.md`, SHA-256 `c786730ef8de45ddd13d3021b16715f32ede6c0bb18c67a8607f573e394a0745`, and `frontier-20261029-first-band-phase-coverage-erratum-v2.md`, SHA-256 `c5f09bc7b393c556ce01871c9be2e7db039f922009dd7d800eeadfe5d89b2818`. Each circuit has strictly positive even pairing at the **same** Vieta vertex \(F=(-t)(c-t)(d-t)\). Their positive combination therefore cannot be nonpositive at every vertex, contradiction.

## Limits

The result does not address six or more positive finite frequencies. It also does not rule out a five-finite-plus-infinity certificate meeting (1), nor settle universal synthesis or produce an eligible-box no-go. The proof imports author-written, unreviewed statements at the exact qualified scopes above; the sign-order deduction is written mathematics. No formal proof, independent scientific review, parent adoption or novelty clearance is claimed. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
