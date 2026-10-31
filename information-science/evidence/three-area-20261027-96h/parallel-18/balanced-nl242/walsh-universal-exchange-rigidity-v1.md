# info-6: exact all-pair balanced exchange criterion and peak-cube rigidity

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Native `/bin/date` observed before this write: **2026-10-27T16:21:33-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** It is a universal theorem about every possible adjacent actual Boolean object, not a chosen swap/control, witness construction, unrestricted no-go, original rank/type selection, numerical improvement, formal/kernel or novelty claim. No scientific program or selected-state/pair probe was used.

## 1. Exact criterion for every balanced exchange

Let f be any actual balanced Boolean function on V=F₂⁹ with |W_f|≤28. For **every** x with f(x)=1 and **every** y with f(y)=0, let f^{x,y} exchange those two truth values and put d=x+y≠0. The exchanged function is balanced, and for every a

    W_{f^{x,y}}(a)−W_f(a)=2[χ_a(x)−χ_a(y)].                     (1)

Since all original Walsh values are multiples of 4, a nonpeak coefficient has magnitude at most 24 and cannot cross 28 under (1). Thus the exchange preserves the full peak bound **if and only if**

    sgn W_f(a)=−χ_a(x)  for every peak a with a·d=1.              (2)

All frequencies with a·d=0 are unchanged. This is exact for all original truth pairs and all frequencies, including when the active peak set below is empty; no pair is selected or tested.

For an arbitrary d let S_d={a:|W_f(a)|=28 and a·d=1}, and let X_d be the solution set of the binary linear equations `χ_a(x)=−sgn W_f(a)` for all a∈S_d. Elementary linear algebra gives an exact phase-only obstruction:

    X_d≠∅  iff  Π_{a∈R}[−sgn W_f(a)]=1
                  for every R⊆S_d with Σ_{a∈R}a=0.                (3)

When consistent, X_d is an affine space of dimension 9−dim span(S_d); if S_d is empty, X_d=V. A valid actual exchange of difference d exists exactly when some x∈X_d has f(x)=1 and f(x+d)=0. Thus phase consistency alone is not a substitute for the **same actual** truth table.

## 2. Every non-affine peak cube constrains every exchange direction

On the odd Walsh half, let Q be the common mod-4 quadratic phase. For every fully peak affine 3-flat E=a₀+H on which its sign pattern is non-affine, the local bilinear form has a unique nonzero radical direction r_E∈H. Define R_f as the span of **all** such r_E; if there are none, take R_f={0}.

Every peak-preserving balanced exchange must have

    d∈R_f^⊥.                                                     (4)

Indeed, if d·r_E=1 then the active portion of E in (2) is an affine 2-flat with direction J=H∩d^⊥ not containing r_E. The nonzero alternating form on H restricts nontrivially to J: if it vanished on J, its radical would have a nonzero vector in J. But (2) requires the peak-sign quadratic Q to equal the affine function a↦a·x throughout that active 2-flat, impossible when its second difference on J is nonzero. Hence d·r_E=0 for every E, giving (4).

In particular, if R_f=T^⊥, then no such exchange exists. For d≠0, (4) would force d=T; every peak has a·T=1, so an entire non-affine peak cube would be active, contradicting its required affine sign in (2). This is a **conditional isolation statement**, not a claim that R_f=T^⊥ or that an original witness exists. ∎

## Exact inputs and unresolved step

Uses only the S1 definition packet and `prerequisite-derivation-v1.md` SHA-256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF, plus the unreviewed `walsh-odd-half-quadratic-sign-v1.md` SHA-256 `be6421feeb80f076373e09aaccb4a6ed1401591db892e82fe77c64831aa215e7`, 35 LF, and local cube form in `walsh-peak-cube-shift-coupling-v1.md` SHA-256 `c0b51e5c3684c487641b27a482173f416909d5ddbccb2037434cb7288f572e16`, 25 LF. Main-notified prior written support does not adopt this new theorem. The truth-set X_d and all exchanges are quantified symbolically; no actual swap, state, numeric control or program was executed.

The result does not prove that any non-affine peak cube or exchange exists, does not exclude an isolated or non-isolated original object, and gives no solution to the unrestricted witness-or-no-go. All original ranks/weights and `(24,24,2)` remain open. It uses neither old Gate-I/candidate/HELD bodies, the stopped half-split/canonical method nor the stopped global truth-degree/ANF branch or any consumer. Book-source equivalence is only at the separately authorized internal bridge; full-scope independent review, human, formal/kernel, executable and novelty remain unperformed for this result. Prior exposure, both documentary MINORs, S1 STOP/HOLD/ZERO, N4 UNKNOWN and aux214 STOP persist.
