# Partial next-case result: no support48 state with exactly27 maximal coefficients

Owner **PhysicsAME46-2**. Native clock before writing: `Thu Oct 29 10:17:34 PDT 2026`; not an exact completion time. **WRITTEN author candidate**, not independently reviewed, adopted, formally verified, or novelty-cleared. This is an exact-t27 support48 obstruction, not a global support49 theorem. No classical theorem, no-Hamming-one result, SAT, LRAT or held material is a premise.

## 1. Exact claim

A normalized complex AME(4,6) state in any product basis cannot simultaneously have support `N=48` and exactly `t=27` coefficients of modulus1/6.

The other possible maximal counts at N=48, and all earlier global lower-bound compositions, are outside this packet. In particular no48-term witness is claimed and the overall N=48 question is not decided.

## 2. Shared residual and local degree structure

For every cut, `U=6ψ` is a36×36 unitary. The27 maximal entries occupy singleton rows and columns; deleting them leaves a9×9 unitary V with21 nonzeros and no singleton line, i.e. excess3. The elementary excess-three classification is one full3×3 block plus full2×2 blocks. Its proof (connected positive component has size≤6; degree-two disjoint pairs/two higher neighbours exclude sizes4,5,6) is fully written in `frontier-20261028-unitary-three-excess-classification-v1.md`, SHA-256 `a37a958ab0fca716ddeddd527a5e0cc4e8e35938c628f42e264f815488742bc2`, and reconstructed in the recorded f141 bridge. It is an ordinary complex-unitarity lemma, not a classical external import.

Every pair system therefore has nine E-carried values: **three heavy values** of multiplicity3 and six ordinary values of multiplicity2. The three heavy rows and three heavy columns belong to the full3×3 block, so their entire nine-word rectangle is forced nonzero in E, in each cut.

For a residual local symbol a at i, pair partition gives `d_i(a)=6−m_i(a)=|π_j(E_a)|`, independent of j, where m_i(a) counts maximal P words using a. It is≥2 (otherwise E_a would be a singleton), and the d values sum to9. Thus residual alphabets have size≤4, and pair capacity9 makes each size≥3.

The number of heavy pair values using a is `h_i(a)=|E_a|−2d_i(a)`, also j-independent, and the h values sum to3. Its positive support H_i therefore has size1,2 or3.

Maximal-word activity counting gives `6Σr_i−Σ_{i<j}r_i r_j≤9`, exactly as for support47 because t and n are the same. This excludes profiles3333,3334,3344 (left18,15,11), leaving3444 or4444. Hence **at least three parties** have residual alphabet size4 and degree vector `(2,2,2,3)`.

## 3. No party can have three distinct heavy symbols

Suppose party C has `|H_C|=3`. Fix another party A and one of its heavy symbols a. It belongs to at least one heavy AB pair, where B is chosen different from A,C. Let D be the remaining party. The heavy AB×CD rectangle is full; the three heavy CD values use all three H_C symbols. Thus E_a projects to at least three distinct C values and `d_A(a)≥3`.

This applies to **every** heavy symbol of each A≠C. Among the other three parties there are at least two with residual alphabet size4, since at least three parties in all have that size. At such a party, only its unique degree3 symbol can be heavy. Hence both such parties have a single heavy symbol carrying all three heavy pair values. Their mutual pair system would then need three distinct heavy values at one fixed pair of symbols, impossible.

Therefore every H_i has size≤2.

## 4. Three heavy edges force a common major/minor form

If `|H_i|=1`, all three heavy pair values in any pair containing i would need different values at the other party. But every other heavy-symbol set has size≤2, so this is impossible. Thus every H_i has size exactly2; its two h values are2 and1. Label them **major**0 and **minor**1 respectively.

For any two parties, the heavy pair graph is simple with three edges on a2×2 grid, row and column degrees `(2,1)`. The unique form is every pair except `(1,1)`: the major row and major column each meet both symbols, while the two minor symbols do not form a heavy pair. This form holds simultaneously in all six pair systems, with no independent basis choice between cuts.

## 5. Four forced extensions overload one heavy pair

Fix the heavy AB value `(0,0)`.

- In the AB|CD cut, CD values00,01,10 are heavy. The full heavy3×3 rectangle therefore forces all three corresponding E words.
- In the AC|BD cut, the word with CD value11 has AC=(0,1) and BD=(0,1), both heavy. Its full heavy rectangle forces that fourth E word too.

Thus the heavy AB value00 has at least four E extensions, contradicting its multiplicity3. This excludes the assumed state.

## 6. Scope and review points

The proof is actual common-three-cut complex unitarity plus the shared P/E pair partition. The only imported lemma is the explicitly identified excess-three unitary-support statement, also re-derived in the recorded f141 work; its mathematical correctness and the normal-form steps require independent review. In particular, the case `|H_i|=3` is excluded only because the P activity count supplies at least two other size4 parties. A three-heavy-symbol core on smaller local alphabets is not claimed combinatorially impossible in isolation.

No exact-CNF certificate or solver status is used. This leaves support48 with other maximal-coefficient counts unresolved and does not compose any global lower bound.
