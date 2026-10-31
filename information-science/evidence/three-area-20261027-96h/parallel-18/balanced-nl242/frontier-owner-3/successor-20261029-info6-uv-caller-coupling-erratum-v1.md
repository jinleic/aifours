# f270 additive erratum: count correction, converse hypothesis, non-vacuity and Ω wording, and the explicit dependency ledger

**MANDATORY ADDITIVE AUTHOR ERRATUM (before-source; the immutable base is untouched and remains byte-identical).** Last native clock observed before composing: **2026-10-29T19:01:32-0700 PDT** (end of the corrected author control run; the file was written immediately after). Owner InfoBalancedNL242-3, slot info-6.

**Pins.** Base manuscript `successor-20261029-info6-uv-caller-coupling-necessary-v1.md`, SHA-256 `a1b7036f4b37738e3a5bb58527b46129eeaf3d5c733872a278a65b443cdc156a`, 19712 bytes, 135 LF — unchanged by this erratum. Review `review-waves/f270-nl242-uv-caller-coupling-necessary/review-v1.md`, SHA-256 `7d1f153a76283764ac8c178d4594843dbdd78bbad15a98ae3672bf8890065207`, 23878 bytes, 132 LF, verified before display and displayed completely in raw ≤15-LF windows 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–132 (the 106–120 window first failed on my own path typo and was immediately re-issued; no content affected). The wave manifest SHA `c95a07ec26abb0ec5154dd4a15da504c7d4a0abbffdd8eb2ea38ccda5e7f352d` (6243 B, 68 LF) is cited **as reported in the review** and was not opened by me. Review verdict: **ACCEPTED at the stated PARTIAL scope, 0 FATAL / 0 MAJOR / 4 MINOR**, plus two uncounted wording observations. This erratum addresses m1–m4 and folds in the two observations (E5). **No frozen body or review file was edited; no witness or exclusion is claimed; (U),(V) remain open; all NONINPUT controls remain binding.**

## E1 (m1) — corrected count in Theorem 2

Base LF 52–54 defines `p := #{y∈V: f(y+T)=1}` and then asserts `p = #{v=+1}`. **The equality is false as written.** Correct statement: with `p := #{y∈V: v(y)=+1}` and `n₋ := #{y∈V: u(y)=−1}` (at the frozen scope `n₋ = m/2 = 58` because `Σu=0` and `|supp u|=116` force `#{u=+1}=#{u=−1}=58`),

`q := #{y∈V: f(y+T)=1} = p + n₋ = p + m/2  (= p+58 at scope),`

by the pair partition (`f(y+T)=1` exactly on `{v=+1} ∪ {u=−1}`: v=+1 means f(y)=0, f(y+T)=1; u=−1 means both 1; u=+1 means both 0; v=−1 means f(y+T)=0). Cross-check: `wt(f|_V) = (|supp v|−p) + n₋ = 198−p` at scope, and `wt(f) = wt(f|_V) + q = 256`. The pair identity of the proof is exact in the form

`T = (⊕_{y∈supp v} y) ⊕ q·T`,  hence  `⊕_{y∈supp v} y = (1⊕q)·T`,

and only the parity of q is used; `q ≡ p + m/2 (mod 2)`, and at `m=116≡0 (mod 4)`, `q≡p (mod 2)`. **All conclusions of Theorem 2 stand unchanged at the frozen scope**: p odd (equivalently q odd; in general `p ≡ 1 + m/2 (mod 2)` is forced), `⊕_{supp v}y = 0`, `W_f(a₀)=4(p−70)`, `k(a₀)=p−70∈{±1,±3,±5,±7}`, `p∈{63,…,77}` odd, and `(i) ⟺ Σv≡2 (mod 4)` (the latter biconditional itself needs `|supp v|≡0 (mod 4)`, true at scope: 140). Outside the frozen scope the corrected count must be used as above; the parity-harmlessness is exactly the condition `m≡0 (mod 4)`.

## E2 (m2) — hypothesis for the reconstruction converse

Base LF 56 claims the couplings are "exactly equivalent to T-self-consistency — nothing more and nothing less" for *any* pair u,v with `uv=0`, `Σu=0`, p odd, `⊕_{supp v}y=0`. **As literally worded for arbitrary pairs this is false.** Corrected converse: for pairs with `uv=0` pointwise, `Σu=0`, **`n₋=#{u=−1}` even** (⟺ `m≡0 (mod 4)`, since `Σu=0` forces `n₋=m/2`), p odd and `⊕_{supp v}y=0`, the reconstruction `s|_V=u+v`, `s|_{V+T}=u−v`, `f=(1−s)/2` satisfies

`XOR(supp f) = (⊕_{y∈supp v} y) ⊕ ((p + m/2) mod 2)·T = 0 ⊕ (odd)·T = T`,

i.e. is T-self-consistent; without even `n₋` the reconstructed XOR is `(⊕_{supp v}y) ⊕ ((p+m/2) mod 2)T`, which equals T iff `p + m/2` is odd. The added hypothesis is **automatic at the frozen m=116** and inside Theorem 6's clause (U) (which pins the class profile and m=116, cf. the ledger `16·3+28·2+3·4+17·0=116`). The "nothing more and nothing less" phrasing is withdrawn as a claim about arbitrary pairs; it holds verbatim at the frozen scope.

## E3 (m3) — non-vacuity wording in Remark (a)

The sentence "a generic 16-set D fails (N1) with probability 63/64, so this is a genuine restriction, not a vacuity" is **withdrawn**. Corrected content of Remark (a):

1. (N1),(N2) are not implied by the adopted f244/f255/f263 statements — a formal observation about the frozen packet's statement list (none mentions ⊕D or ⊕z₀); it is not a global novelty claim.
2. Satisfiability-in-isolation of (N1) *within the plateaued class of §5* is shown by the explicit example `σ₁=(−1)^{x₁x₂+x₃x₄}` (D a 16-point subgroup, ⊕D=0), correctly hedged as not extending to u or f.
3. Whether some plateaued 16-support has `⊕D≠0` (i.e. whether (N1) genuinely restricts *within* that class) is **OPEN and not addressed**; no probabilistic statement and no selected test is made or implied. (The exact generic-16-set statistic is recorded only in the reviewer's control and is not relied upon here.)

## E4 (m4) — Ω wording in §3 and Theorem 6 (U)

Base LF 73's "Ω is thus determined blockwise by u's classes alone" is corrected to: the **per-block cardinality profile** of Ω (1 point on each of the 16 A₁ blocks, 2 on each of the 28 C₂/C₃/D₁ blocks, 0 on the 3 G blocks, 4 on each of the 17 O blocks) is class-determined; the **actual points** of Ω depend on the pointwise u (the gap positions `z₀(c)` and the occupied 2-sets) and are u-data — exactly the data constrained by (N2). Theorem 6's clause (U) is to be read accordingly: realizing the frozen system *plus (N1),(N2)* includes the within-block placements of u, not merely the class counts.

## E5 — the two uncounted observations (wording)

(a) §0 item 1's "reduces the odd-half congruence structure to XOR self-consistency" is tightened to: at the frozen scope, XOR self-consistency *forces* p odd and — via Theorem 2(ii) — (N1); **given** the adopted odd-half congruence, flatness `V̂≡2 (mod 4)` is *equivalent* to (N1) ∧ (VB) (the per-fibre sums). (b) Remark (b)'s "re-deriving the adopted zero placement from the interface" is corrected to "re-packaging": the never-zero consequence and the all-zeros-on-K placement are conditional on the same adopted oddness premise, reformulated — not independently derived.

## E6 — explicit dependency ledger (corrected assumptions)

**Unconditional** (derived from the Boolean object in the base, §§1–2,4–5, as corrected here): Theorem 1 (caller split); Corollary 1 (cap decoupling); Lemma 1 (all `W_f≡0 (mod 4)`; Û, V̂ even everywhere); the Parseval split; Theorem 2 in corrected form (E1, E2); the mod-4 identity of Theorem 3(i) (`V̂(r,s) ≡ Σ_cW_s(c) − 2(r·D̂)`); **the necessity of (N1),(N2)** (Theorem 3(iii) uses only Theorem 2(ii), i.e. XOR self-consistency — no import); Theorem 4 taxonomy with class-constant δ; the §5 plateaued characterization of D; the §6 energy ledgers and `ΣV̂²=35840`; the fibre sums. Given (N1) alone, `V̂(r,s) mod 4` is r-independent per fibre and equals `Σ_cW_s(c) mod 4 ∈ {0,2}`.

**Conditional on the named import** — the premise "`k(a)=W_f(a)/4` is odd for every a with `a·T=1`", quoted at frozen input 3 §4 (LF 84) and sourced to disposition `info-6-walsh-caller-and-mod4-coupling-parent-v1.md`, SHA-256 `721222262af91bc768227ce8bfae563cabf5a102437ac55e6583de38ec2d3c9d`, which is **not an input body of this release and is not independently derived here; it remains an explicitly adopted premise, not a verified one**: Theorem 3(ii) as a necessity statement about the actual object; `V̂∈{±2,±6,±10,±14}`; `V̂≠0` and hence all eight zeros on K; the three mixed congruences as necessary conditions; the |k|-spectrum value set and the ledger `n₃+3n₅+6n₇=1088`; Theorem 6's clause (V) residue requirement. The import is exactly what excludes the 0-residue fibres left open by the unconditional part.

**Corrected Theorem 6 (restated).** At the frozen f244 scope with m=116, `(e₁,e₂,e₃)=(0,4,8)`, `G₃=1`, local H=0, **and relative to the adoption of the named import**, the residual admits a balanced f with `max|W_f|≤28` iff: (U) u realizes the entire frozen u-side system (block identities and counts, f263 cross-fibre conditions, eight in-fibre zeros, within-block placements) together with (N1),(N2); and (V) v signs the u-determined Ω with `|V̂(r,s)|≤14` and `V̂≡2 (mod 4)` on all 256 characters, `p∈{63,…,77}` odd, and the three mixed congruences `Σ_{y∈Ω}v(y)χ_s(z(y))≡2 (mod 4)` (s=1,2,3); the reconstruction is T-self-consistent because m=116 (E2). **Unconditional variant:** drop `V̂≡2 (mod 4)` and the mixed congruences from the necessary side (they remain necessary under the import); everything else, including both caps, p-range, (N1),(N2) and the reconstruction, stands on the Boolean object alone.

## Author finite-identity control (allowed scope: finite identity checks only)

`author-control-e1-e2-v1.py`, SHA-256 `fdda02cae8943ab0d8febe03cb592ff8815821174f116146f51d213a14a4ab19`, 4387 bytes, Python standard library only, seeded synthetics (no target search, no spectrum/atom selection): 8 balanced Boolean functions on F₂⁵/F₂⁷/F₂⁹ with T≠0, covering `m≡0` and `m≡2 (mod 4)`. All checks pass (rc=0, 0.27 s, run ended 2026-10-29T19:01:32-0700 PDT): u/v construction identities; Theorem 1 split on all of K and K+a₀; Lemma 1; **E1 exactly** (`q=p+n₋` on every case, with the weight cross-checks); the exact pair identity `T=(⊕_{supp v}y)⊕qT`; **E2** (the reconstructed-XOR formula on all cases — which implies the sufficiency specialization whenever its hypotheses hold); `Σv=2p−|supp v|` with the biconditional `Σv≡2 (mod 4) ⟺ p odd` checked under its exact hypothesis `|supp v|≡0 (mod 4)`. **Disclosure:** the first run ended rc=1 at native clock 2026-10-29T19:01:00-0700 PDT because *my control script* asserted that biconditional unconditionally — a script defect that is itself the E1/E5 scope condition made concrete; the script was corrected (not the manuscript mathematics) and both runs are disclosed here. Control script and receipt paths are in the exclusive root; the reviewer's independent control (89/89) is separately receipted in the wave directory and is not re-executed or claimed by me.

## Remaining gap after this erratum (unchanged in structure)

- **(U)** realizability of the frozen u-side system *with (N1),(N2) and the within-block placements* — open; no witness; the f263 §8 formal placement remains a known non-realization (`U₂(0)=168/16`, `U₃(0)=11`).
- **(V)** solvability of the 256 capped linear forms over Ω with the parity/congruence side conditions as scoped in the corrected Theorem 6 — open, neither established nor refuted.
- The named odd-half congruence remains an externally adopted, unverified-here premise; in-class non-vacuity of (N1) (existence of a plateaued 16-support with ⊕D≠0) is open.
- No witness or exclusion for the residual `(G₃,H)=(1,0)`, the (0,4,8) case, the other six class-count pairs, m=114, other fibre patterns, rank two, or the global balanced NL242 target. Same-harness work; not human, independent-model-family, formal/kernel or novelty verification.
