# Selection addendum1 — source refresh and one next exact construction obligation

Observed immediately before creation: **2026-10-23T14:15:27-07:00**. This supplements, never overwrites, selection-v1. The all-(u,v) auxiliary-merge result remains **CANDIDATE/PARTIAL**, manuscript SHA-256 `40a09adc5773df89e3dc26fa5bbec2958efd1e9e881a71638bc25c3de88d346a`. Parent read only its first103lines when requesting this follow-on obligation; full source comparison and separate reconstruction remain queued. No promotion is implied.

## Primary-version refresh actually obtained

The arXiv abstract-page submission histories were retrieved directly, not inferred from HTML title-page dates. Retained `source-version-history-v1.json` records the response hashes and extracted histories:

- 2402.12966 shows only v1, 20February2024.
- 2509.07086 shows only v1, 8September2025. This strengthens the earlier insufficient inference from a v2 HTML404.
- 2609.11849 shows only v1, 10September2026.
- Park2602.09860 has v1 (10February), v2 (15February), **v3 (10March2026)**. The operative comparison is now [v3](https://arxiv.org/html/2602.09860v3), not v1. Its exact Theorem1.1 family and decomposability statement were read. Captured raw HTML SHA-256 `75b6f910a1c307c39999766f6d9265d5429818510e97798626040a5769ba97bc`.

Parkv3 retains the same relevant no-go: for the map

`L_pq^(d)(Z)=((1-p-q)/d)Tr(Z)I_d+pZ+q V Z^T V^*`,

with **V skew-symmetric unitary**, d/2-positivity implies decomposability. Therefore in d=4 no two-positive member of this family can detect a PPT state, regardless of whether that state itself is invariant. Local unitary/filter congruences, positive sums, or completely positive compositions of already decomposable members cannot repair that obstruction. Generalizing the state without leaving this witness cone earns no headroom. The original Breuer–Hall member is only one-positive, not a permissible SN3 separator.

The v3 introduction still contains the potentially misleading phrase “general upper bound” in a paragraph about prior constructive d/2 scaling. Its family-restricted theorem is **not** an unrestricted ququart SN upper bound. Do not use that wording as a solved-P44 claim.

A later witness-tool lead was also followed to the primary preprint: Xiong–Sze [2504.11213v1](https://arxiv.org/html/2504.11213v1). Its abstract, introduction and Example1 were read. Example1's SN3 two-ququart state is

`(1/2)P((|00>+|11>+|22>)/sqrt(3))+(1/4)P(|23>+|32>)`.

This is **NPT**: partial transpose restricted to span{|01>,|10>} is `[[0,1/6],[1/6,0]]`, whose antisymmetric vector has negative expectation. Thus its four-dimensional example does not answer P44. No numerical output from that paper was replayed or accepted. Its published APS page returned403; the accessible arXiv primary source supplies the stated claim boundary. A search lead pointing to 2604.02439 was directly read and found to be an **absolute** Schmidt-number/global-unitary paper, not the named witness source; it is not used as P44 evidence. Johnston's author publication page was read and still points to the same2609.11849 preprint; that page does not itself certify worldwide openness.

## Exactly one next construction obligation (not begun as a separator attack)

Keep the P44 target unchanged, but discard a direction with a **core-level component**, which is outside the proved auxiliary-merge mechanism. Define the single rational map `C:C^5 -> C^4` by

`C|0>=|0>`, `C|1>=|1>`, `C|2>=|2>`, `C|3>=|3>`, `C|4>=|0>`.

Its kernel is span{|4>-|0>}, not a subspace of the two auxiliary levels. With the exact R45 already frozen in selection-v1, fix **one state**, not a search grid,

`rho_*=(I tensor C)R45(I tensor C)^*/31`.

Equivalently, with `a,b,c` as in the frozen manuscript,

`31 rho_* = P(a)+P(b)+P(c)+3P(|02>+|30>)+3P(|20>+|33>)`
`            +3P(|30>)+3P(|32>)+3P(|23>)+3P(|00>)`.

This is an exact rational 16 by 16 positive trace-one PPT state, by its displayed positive sum and the local-filter relation to the explicit PPT input. Merely producing this PPT matrix is **not** a positive P44 result.

**Next exact mathematical obligation:** either supply an explicit finite Schmidt-rank-at-most-two conic decomposition of `31 rho_*`, or produce an exact Hermitian W with `Tr(W rho_*)<0` and a proof of two-block-positivity over **all complex rank-at-most-two coefficient matrices**. The latter W must lie outside Park's decomposable two-positive family and its decomposability-preserving filtered/summed closure. No specific valid outside-class witness is yet available. No generic parameter sweep, second follow-on construction, solver, executable certificate replay or new paper queue is authorized or proposed by this addendum.

The initial bounded written action, if continued after this freeze, is to work with this single input's coefficient-matrix range, not to claim that a numerical optimum or a failed decomposition proves SN3. Any scientific execution still requires a separately pinned exact parent GO. Current unrestricted verdict: **OPEN/UNRESOLVED HERE, UNCERTIFIED-OPEN literature status**. Current accomplished delta: the fully written all-complex auxiliary-merge barrier, pending reconstruction.
