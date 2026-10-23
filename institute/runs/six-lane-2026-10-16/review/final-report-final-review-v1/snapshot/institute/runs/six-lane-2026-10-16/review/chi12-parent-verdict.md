# Random 12-regular graph colouring: parent verdict

## Result and exact scope

**For the uniformly random 12-regular simple graph G_{n,12}, χ(G_{n,12}) = 5 asymptotically almost surely as n → ∞.** Every residue class of n modulo 5 is covered; this is not restricted to random lifts or balanced vertex counts.

This closes Kemkes–Pérez-Giménez–Wormald's (KPW) {5,6} window at degree12. Their Theorem1 uses k=6 here, since 8log4 < 12 < 10log5, and its exact-value clause 12 > 9log5 fails. Ayre–Coja-Oghlan–Greenhill Table1 leaves degree12 undetermined for five colours (d_{5,smm}=11, d₅=15). Achlioptas–Naor's sharper constant ℓ₅=(128/15)log4≈11.8297, also used by Nir–Pérez-Giménez for random lifts, is below12.

[Frozen contract](../screening/phys-2-random12reg-colour-contract.json). This is **DERIVED-OPEN**, not a source explicitly naming this individual degree as open. It is the same mechanism as the accepted [χ8 result](chi8-parent-verdict.md), with priority and significance shared; it is not counted as a separate new method or explicitly-named gate.

## Frozen proof

[Final r3](chi12-parent-inputs-r3/PROOF_CHI12.r3.md), SHA-256:

`04f5f370f13f84ebf2e0f08ac9421209a07309fc040bd74b05d05e4cfa2c1f39`

- [r3 manifest](chi12-parent-inputs-r3/manifest.json), parent [r2→r3 diff](chi12-parent-inputs-r3/parent-r2-to-r3.diff): exactly the two final explanatory corrections plus bookkeeping.
- [r2 manifest](chi12-parent-inputs-r2/manifest.json), parent [r1→r2 diff](chi12-parent-inputs-r2/parent-r1-to-r2.diff), read in full (327 lines).
- [Reviewed r1 and primary sources](chi12-parent-inputs-v1/manifest.json); r1 `0b608b07…d85e` is unchanged.

## Mathematical bridge

1. **Exact finite-n second-moment bound.** Keep KPW's 25 per-cell edge constraints rather than relaxing their sum. Pointwise entropy weak duality with multipliers μ_u=c₀+(11/12)log m_u gives

   U(M)=−11log5+6log(2E(M)),   E(M)=Σ_{unordered allowed {u,v}}(m_um_v)^{11/12},

   with 200 allowed cell pairs and polynomial factor P₁₂(n)=e²⁶(12n+1)^{25/2}(6n+1)^{401/2}. Empty overlap cells are handled. The duality and Φ₁ closed form are standard/Galanis–Štefankovič–Vigoda–Yang precursors, not new here.
2. **Global decay at k=5.** Inclusion–exclusion and two Cauchy–Schwarz inequalities give E(M)≤Σ_pF(r_p), F(r)=(3/2)(Σr_j^{11/12})²+(1/2)Σr_j^{11/6}. On the uniform five-point space F(r)=40‖T_{1/4}r^{11/12}‖₂². The resampling-chain log-Sobolev constant α=3/(5log4), with Gross hypercontractivity and duality, yields strict variance decay because a=11^{−5log4/12}>1/4. The decisive inequality 11⁵<e¹² follows from the exact22-term Taylor partial sum. Thus

   E(M)≤E(J)−κ‖M−J‖²,   U(M)≤U(J)−C₁₂‖M−J‖²,

   on row-stochastic matrices for E and doubly stochastic matrices for U, with κ=(121/18)(a²−1/16)>0 and C₁₂=6κ/E(J)>0. An interval proof is supplementary, not load-bearing.
3. **Retained KPW machinery.** At (k,d)=(5,12), (H1)=5>0. Lemma9's counting inequality is32>25. Both Lemma8 ε-conditions are audited: ε²<17/20480000 implies ε²<51/40000; the degree cancels in both. The S₁ Hessian has determinant5²⁴/17¹⁶. S₂/S₁=O(n²⁴²exp(−C₁₂ε²log²n/256))→0.
4. **Small subgraph conditioning.** Ratio11/16 and Σλ_iδ_i²=8log(16/5) match the second moment. Use only Wormald's conditional-contiguity conclusion: the size-biased measure has P(Y=0)=0, hence P(Y=0|X₁=0)→0; conditioning further on no double edges gives the uniform simple model. The overstrong generic positivity-equality formulation is not used ([shared clarification](colouring-ssc-formulation-addendum-v1.md)).
5. **Every n.** For n≡r(mod5), r=1,2,3,4, remove r well-separated triangle-free vertices, match their12r neighbours into6r distinguished edges, and use KPW Theorem10's marked-colouring argument. The map has exactly (12r)!/(12!)^r preimages; the four counts are1,2704156,3384731762521200,235809301462142612780721600. The final proof supplies a supporting derivation of marked-space cycle laws and exact uniformity; the remaining mixed-moment and concentration sketches inherited from KPW are disclosed.
6. **Lower bound.** Molloy–Reed gives4(3/4)⁶=729/1024<1, so χ>4 a.a.s.; a self-contained first-moment derivation also proves this.

## Verification

| Evidence | Observed result | Limit |
|---|---|---|
| Parent independent rational arithmetic | 15 exact checks pass; 11⁵<e¹² via partial-sum excess545861266838/761674375; C₁₂∈(586620539754832511083,586620539754832511084)/10²⁴; both ε-bounds, variance factor, moment bases, degree242 and all four residue counts ([script](chi12_parent_rational_check.py), [receipt](chi12-parent-rational-arithmetic-v1.json)) | Constants/counts, not the universal inequality or probability argument |
| Parent replay of frozen r1 verifier | byte-identical output, all_required_true ([receipt](chi12-parent-verifier-replay-v1/parent-result.json)) | Replay, not independent implementation |
| Parent replay of r2 extension verifier | byte-identical output, all_required_true; includes exact Gaussian/mean identities and tiny marked-space controls ([receipt](chi12-parent-verifier-replay-r2/parent-result.json)) | Same |
| Codex CLI `gpt-6.1-sol`, hostile complete r1 review | ACCEPT-WITH-FIXES, no fatal/major; independently audits retained KPW/W99/D–SC sources and every proof step; flags the generic SSC formulation ([note](chi12-codex-hostile-review-v1.note.md)) | Model review, not peer review |
| Claude CLI `claude-opus-5-5`, complete r1 review | ACCEPT-WITH-FIXES, no fatal/major; six completeness minors, five requiring changes ([note](chi12-claude-complete-review-v1.note.md)) | No-tools review using complete proof and targeted primary-source extracts; residual reliance disclosed |
| Codex CLI `gpt-6.1-sol`, r2 delta review | ACCEPT-WITH-FIXES; verifies valid SSC/marked-space additions and preservation of load-bearing r1 parts; two explanatory minors ([note](chi12-r2-delta-codex-review-v1.note.md)) | Delta only |
| Parent final delta review | Reads both complete diffs; all findings applied in r2/r3 ([dispositions](chi12-review-dispositions.json)) | r3 not itself re-reviewed; no verifier changed in r3 |

## Trust, priority and significance

This is a reviewed written proof, **not Lean-checked**. It imports published KPW machinery, Wormald's Theorems2.6/4.1, and Diaconis–Saloff-Coste/Gross hypercontractivity. It retains the explicitly disclosed KPW marked mixed-moment and concentration sketches.

The [bounded priority audit](chi8-priority-audit.md) covers both degree8 and degree12 and found no source giving these exact uniform-model results. The theorem/inequality is a further consequence of the χ8 mechanism; no separate novelty claim is made. A search miss is not priority clearance. Unlike at(4,8), keeping the per-cell constraints is **not shown necessary** at(5,12): numerical optimisation suggests the older relaxed exponent may also maximise at J, but that is not a proof and is not used.

**FRONTIER: CORRECTNESS-ACCEPTED — reviewed written proof at(5,12), every admissible n; DERIVED-OPEN, NOVELTY-UNCLEAR. The frozen χ(G_{n,12})=5 target is resolved (2026-10-17 PT), sharing the χ8 contribution and its potentially substantive specialist significance.**

No commit, push, publication or external contact was authorized.


**Attribution addendum (2026-10-17 15:19:38 PDT, appended; text above unchanged):** a new-surface audit found a method precedent or general theorem that this verdict did not cite; see [physics-priority-addendum-v1.md](physics-priority-addendum-v1.md). No correctness change.
