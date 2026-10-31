# Independent frozen written-math review — wave `f270-nl242-uv-caller-coupling-necessary`

**Target manuscript:** `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/frontier-owner-3/successor-20261029-info6-uv-caller-coupling-necessary-v1.md` (SHA-256 `a1b7036f4b37738e3a5bb58527b46129eeaf3d5c733872a278a65b443cdc156a`, 19712 bytes, 135 LF), info-6 owner-3 uv-caller coupling necessary-consequence package at its stated PARTIAL scope.

Native clocks. Before any input was opened: **Thu Oct 29 18:31:42 PDT 2026**. Before composing this review: **Thu Oct 29 18:50:35 PDT 2026**. Bounded control run ended **Thu Oct 29 18:49:25 PDT 2026**. Nothing is backdated.

## Verdict

**ACCEPTED at its stated PARTIAL necessary-consequence / formulation-closure scope: 0 FATAL, 0 MAJOR, 4 MINOR.**

All six obligation groups (a)–(f) were independently rederived in writing. Theorem 1, Corollary 1, Lemma 1, the Parseval split, Theorem 4, Theorem 3(i)/(iii) with (N1),(N2), §5, and the §6 ledgers are **SUPPORTED** unconditionally at the frozen scope. Theorem 2's conclusions and Theorem 3(ii)'s equivalence are **SUPPORTED** at the frozen scope (its proof contains a repairable count mis-identification, m1 below; the mis-identification is parity-harmless exactly because m=116≡0 mod 4). Theorem 6 is **CONDITIONAL**: the necessity direction of its clause (V) (`V̂∈2+4Z`) rests on the *adopted* odd-half-k congruence, which the manuscript honestly flags (LF 7, 77, 90) as originating in a named caller disposition that is not an input body; the frozen packet's own use of that premise is at correction LF 84. No witness and no exclusion is claimed anywhere; (U),(V) are exactly the remaining gap; no other scope is touched. H is used only as the explicit local U₁=0-block/single-|U₀|=4-peak count (value 0); no historical label equivalence is asserted.

## 1. Integrity and display receipt

Manifest SHA-256 `c95a07ec26abb0ec5154dd4a15da504c7d4a0abbffdd8eb2ea38ccda5e7f352d`, 6243 bytes, 68 LF — matched before any body was opened. All seven declared inputs were SHA-256/bytes/LF verified **before** any body read; all matched exactly:

| # | Input (manifest order) | SHA-256 (verified) | bytes | LF |
|---|---|---|---:|---:|
| 1 | `written-releases/info6-owner3-continuation-v1.json` | `5f77b9eaaa69d7b342e66b1445c681d32861bbff0c382b5eadb9935184fb6484` | 5413 | 62 |
| 2 | `successor-20261029-info6-status-only-handoff-v1.md` | `790221d103c71d62ff6186f502daf0feab3b9eebe9c63bfcd58a12bd320f6c3f` | 5188 | 29 |
| 3 | `dispositions/…116-fibre-048-obstruction-parent-v1.md` | `18403a17269311682255e3bb9823a89a0a69cd7344a66ad02bdd841bcc52f912` | 4246 | 24 |
| 4 | `successor-20261029-f255-boolean-local-normalization-correction-v1.md` (correction) | `e0c3f4807732d6cd70d47485f1692366c0f77abfd1c5169e7a5782114bfddcf4` | 12388 | 151 |
| 5 | `successor-20261029-f244-residual-cross-fibre-placement-v1.md` (base) | `686dd9177d6ff8788b6463d8d4e444e8bda4231ce7060a76ad0cfdea5f39144c` | 13894 | 183 |
| 6 | `dispositions/…116-fibre-048-residual-10-cross-fibre-parent-v1.md` (f263 adoption) | `e09be9069bf8027bdb53e60a73c804f525b1c5c1953d517e417b5749b555ba09` | 8344 | 31 |
| 7 | TARGET `successor-20261029-info6-uv-caller-coupling-necessary-v1.md` | `a1b7036f4b37738e3a5bb58527b46129eeaf3d5c733872a278a65b443cdc156a` | 19712 | 135 |

Every input was displayed completely, in manifest order, in raw ≤15-LF windows including each actual ending (input 4 before input 5, correction before base; target last); no mathematical work began before the packet completed. Two window reads initially failed on reviewer-side path typos and were immediately re-issued successfully (windows 121–135 of input 4 and 91–105 of input 5); no content was affected. Premise consistency: the target's own provenance table (LF 127–133) lists exactly inputs 2–6 above with matching hashes.

Exposure compliance: only the seven declared inputs were opened. No held/withdrawn/ZERO/protected payload, no P1 roster, no f166 roster consumer, no f239/CR7, no m114 placement draft, no enumerator extension, no sibling review, no external source. The named-but-unread caller disposition `72122226…` was NOT opened; its role is assessed only as an explicitly adopted premise (see Theorem 3/6 below).

## 2. Written reconstruction, per obligation

Notation as in the packet: `s=(−1)^f`, `T=⊕supp f`, `K=T^⊥`, `a₀·T=1`, `V=a₀^⊥`, `u=[s(y)+s(y+T)]/2`, `v=[s(y)−s(y+T)]/2` on V.

### (a) Complete nonzero-shift caller — **SUPPORTED** (LF 25–37)

*Theorem 1 (LF 25–29).* For r∈K: r·T=0, so pairing x=y with x=y+T gives `W_f(r)=Σ_y(−1)^{r·y}[s(y)+s(y+T)]=2Û(r)`. For a=r+a₀ and y∈V: `a·y=r·y` (since a₀·y=0 — this is where V=a₀^⊥ is used) and `a·(y+T)=r·y+1`, giving `W_f(r+a₀)=2V̂(r)`. Both identities verified line-by-line; also re-verified on synthetic balanced functions (control A*.caller-split). `K∩⟨a₀⟩=0` (a₀·T=1), dim K=8, and restriction F₂⁹→V* has kernel ⟨a₀⟩, so K≅V*: correct (LF 23).
*Corollary 1 (LF 31).* `F₂⁹=K⊔(K+a₀)`; hence `max_{a≠0}|W_f| = max(2max|Û|, 2max|V̂|)`, so NL≥242 ⟺ both caps ≤14. The two caps constrain u and v separately; `Σ_KÛV̂=256Σuv=0` by Plancherel on V. Verified.
*Lemma 1 (LF 33).* `W_f(a)=−2Σ_{a·x=1}s(x)` for a≠0 (balance kills W_f(0)=0), the inner sum over 2⁸=256 signs is even; hence `W_f≡0 (mod 4)` globally, Û, V̂ even, k=W_f/4 integral everywhere, off K `k=V̂/2` (LF 35). Verified; control A*.lemma1.
*Parseval split (LF 37).* `Σ_K W_f²=4·256·116=118784`, `Σ_{K+a₀}W_f²=4·256·140=143360`, total 262144=2¹⁸; fibre split of `Σ_K k²=7424` as 896+2304+2176+2048 (56·16; 64·36; 4·4+60·36; 8·4+56·36); `4·7424=29696=256·116`; `ΣV̂²=35840`. All arithmetic re-performed and confirmed; control A*.parseval-split.

### (b) XOR/balance coupling — **SUPPORTED at scope** (LF 43–56), with MINOR m1/m2

Pair-split (LF 50): each pair {y,y+T} contributes `[f(y)⊕f(y+T)]·y ⊕ f(y+T)·T` (all four cases check), so with `q:=#{y∈V:f(y+T)=1}`, `T=(⊕_{supp v}y)⊕qT`, hence `⊕_{supp v}y=(1⊕q)T`; the left side lies in V and T∉V, forcing q odd and `⊕_{supp v}y=0` (LF 54). My independent reduction: `B:={f(y+T)=1}={v=+1}⊎{u=−1}`, so `q=p+#{u=−1}=p+m/2` (Σu=0 ⇒ #{u=+1}=#{u=−1}=m/2); at the frozen m=116, #{u=−1}=58 is even, so q≡p (mod 2) and **p odd** (i); `Σv=2p−140`, `W_f(a₀)=4(p−70)` (Theorem 1), cap ⇒ `|p−70|≤7`, p∈{63,…,77} odd, `k(a₀)=p−70∈{±1,±3,±5,±7}` (LF 45–48) — all confirmed. Lemma 1 makes `4(p−70)≡0 (mod 4)`, i.e. (i) ⟺ `Σv≡2 (mod 4)`; consistent with the adopted odd-k fact at a₀ (double forcing, coherent). Controls A*.count-identity (q=p+#{u=−1} exactly) and A*.T2-conclusion (q odd, ⊕supp v=0, `p≡1+m/2 (mod 2)`) pass on 8 synthetics covering both m mod 4 classes.

**m1 (MINOR, LF 52–54).** The proof defines `p := #{y∈V: f(y+T)=1}` and then asserts `p=#{v=+1}`. As integers these differ: `#{f(y+T)=1}=p+#{u=−1}=p+58` at scope (58≠0). Only the parity is used, and parity agrees exactly because 58 is even (m=116≡0 mod 4), so the argument and all conclusions stand; the equality claim itself is false as written. Prospective correction: replace the equality by `#{f(y+T)=1} ≡ #{v=+1} (mod 2)` (offset #{u=−1}=m/2, even at scope).

**m2 (MINOR, LF 56).** The "Reconstruction direction" claims the couplings are "exactly equivalent to T-self-consistency — nothing more and nothing less" for *any* pair u,v with uv=0, Σu=0, p odd, ⊕supp v=0. My recomputation of the reconstructed f: `XOR(supp f)=(⊕_{supp v}y)⊕((p+m/2) mod 2)·T`; with ⊕supp v=0 and p odd this equals T **iff m/2 is even (m≡0 mod 4)**. The literal "any pair" converse therefore needs the additional hypothesis #{u=−1} even; it is automatic at the frozen m=116, hence inside Theorem 6's (U) (which pins the class profile and m=116, cf. the ledger 16·3+28·2+3·4+17·0=116), so no downstream claim is affected. Prospective correction: add "with m=|supp u|≡0 (mod 4) (automatic at the frozen scope)".

### (c) New u-only conditions (N1),(N2) — **SUPPORTED** (LF 64–86)

*Theorem 4 (LF 64–71).* Per block, `W_s(c)=Σ_z v(c,z)χ_s(z)≡|supp v∩block| (mod 2)`: A₁ blocks (|U₁|=3 forces three entries aligned to ±χ₁ with a single gap z₀(c); per-block Parseval (9+1+1+1)/4=3 support points) carry exactly one v-point ⇒ W_s=δ_cχ_s(z₀(c)) odd for all four s; C/D blocks carry a complementary 2-set; G blocks (±4 peak = four aligned ±1) carry v≡0; O blocks carry a full ±1 4-vector with `Σ_s W_s²=16`, and since all four W_s share parity, only {spike (±4,0,0,0)} or {quartet (±2,±2,±2,±2)} occur. For the 28 pair blocks, writing δ_c=z₁+z₂=z₃+z₄: `{|U_s|=2}={s:χ_s(δ_c)=η₁η₂}`; because 0·δ=0 always, C₂ (pair {0,2}) and C₃ (pair {0,3}) force η₁η₂=+1 and δ_c the unique nonzero vector with annihilator {0,2} resp. {0,3}; D₁ (pair {2,3}) forces η₁η₂=−1 and annihilator {0,1} — three *distinct* nonzero δ's, one per class, i.e. δ is class-constant; v's pair options are the annihilator pair or its complement per the sign η₃η₄ (LF 67's option list is correct). Ledgers 16+56+68=140 and 48+56+12=116 confirmed. All finite identities control-verified (C.a–C.e, D1).
*Theorem 3(iii) (LF 82–86).* `Ω=supp v`; ⊕Ω=0 (Theorem 2(ii)) splits: R*-component = XOR over blocks with odd v-support = ⊕_{c∈D}c ⇒ **(N1)**; P*-component = ⊕_{c∈D}z₀(c) ⊕ (⊕_{C₂}δ) ⊕ (⊕_{C₃}δ) ⊕ (⊕_{D₁}δ) ⊕ (⊕_{O}⊕_{z∈F₂²}z)=⊕z₀(c), since the class-constant δ's fold to zero at the even counts 4,6,18 and the O-contribution is 0 ⇒ **(N2)**. The 28-pair cancellation is exactly this even-fold; verified generically (controls C.d, D6, D6b). (N1),(N2) are u-data only (D and the gaps z₀). *Non-implication (LF 89, first half):* SUPPORTED as a statement about the frozen list — the adopted f244/f255/f263 statements involve class counts (only |D|=16 for the s=1 fibre), the s=2,3 atom geometry and U-level identities; none mentions ⊕D or ⊕z₀. This is a formal-novelty-within-the-packet observation, not a global novelty claim (none is made; none is made here either).
*Non-vacuity (LF 89, 97).* The §5 illustration σ₁=(−1)^{x₁x₂+x₃x₄} (LF 97) was rederived: its F₂⁶-Walsh transform is `16(−1)^{c₁c₂+c₃c₄}` on D={c₅=c₆=0} and 0 elsewhere, a 16-point subgroup with ⊕D=0 — (N1) satisfiable in isolation, correctly hedged ("no claim that this σ₁ extends"). See m3 for the residual nuance.

### (d) Congruence equivalence and ledgers — **SUPPORTED** (equivalence reading CONDITIONAL on the adopted odd-half congruence) (LF 77–109)

*Theorem 3(i) (LF 79).* Oddness of W_s exactly on D (per-block parity above) plus `(−1)^{r·c}=1−2(r·c)` gives `V̂(r,s)≡Σ_cW_s(c)−2(r·D̂) (mod 4)` with `r·D̂` the XOR-fold pairing — verified symbolically and generically (control D2).
*Theorem 3(ii) (LF 80–81).* Flatness `V̂≡2 (mod 4)` everywhere ⟺ D̂=0 ∧ (VB) Σ_cW_s(c)≡2 (mod 4) ∀s: if D̂≠0 an r with r·D̂=1 changes the residue by 2 (contradiction), and at r=0 flatness is exactly (VB); conversely both give flatness for all r. At s=0, r=0, (VB) is `Σv≡2 (mod 4)` ⟺ p odd, so given p odd the flatness is equivalent to (N1) plus the three mixed congruences `Σ_{y∈Ω}vχ_s(z(y))≡2 (mod 4)`, s=1,2,3. Verified in positive and both negative directions on generic block systems (controls D3, D4, D5: breaking (N1) with per-fibre sums held fixed breaks flatness; breaking (VB) with D̂=0 breaks it at r=0). The reading "the adopted odd-half caller congruence is equivalent to …" is **CONDITIONAL** on the adopted premise (LF 77) that off-K k is odd; the manuscript states this dependence explicitly and does not claim to derive it (see open items).
*Ledgers (LF 101–109).* `Σ_sE_s=560=4·140`, `64E_s=Σ_RV̂(r,s)²`, `E_s=16+P_s+O_s` with ΣP_s=224=28·8, ΣO_s=272=17·16; spectrum ledger `n₁+n₃+n₅+n₇=256`, `n₁+9n₃+25n₅+49n₇=8960` ⟺ `n₃+3n₅+6n₇=1088`; per fibre `n₆(s)+3n₁₀(s)+6n₁₄(s)=2E_s−8`; the integer relaxation (168,20,20,48) satisfies both (Σ=256, 49·168+25·20+9·20+48=8960) and is correctly labeled non-witness; fibre sums `Σ_Rk(r,s)=32U_s(0)` and, at s=1, `6Σσ₁=32U₁(0)` ⟺ `U₁(0)=3W(σ₁)(0)/16` consistent with 16U₁=3W−2t₁, t₁=0. All arithmetic re-performed; confirmed. The value set {±2,±6,±10,±14} and "V̂ never vanishes ⇒ all eight zeros on K" (LF 90, LF 103) are CONDITIONAL on the same adopted congruence.
*§5 (LF 93–97).* `16U₁=3Walsh_R(σ₁)`, three-valued {0,±16}, Parseval 4096=256·16 re-pegs |D|=16; dual form `|Σ_{c∈D}ε_cχ_r(c)|=4 ∀r` (and conversely) follows by inversion σ₁(r)=¼Σ_{c∈D}ε_cχ_r(c); the dual sign field θ with `W(θ)=16ε·1_D` exists by explicit construction θ(c)=¼Σ_{r∈D}ε(r)χ_c(r). Verified.

### (e) Interface equivalence — **CONDITIONAL (as disclosed), reduction verified** (LF 113–119)

Sufficiency direction (⟸): given (U)+(V), the reconstruction `s|_V=u+v, s|_{V+T}=u−v` is balanced iff Σu=0 (2Σu), has W_f given by Theorem 1 (pair argument only), meets the cap via the two caps (u-side k∈{0,±2,±4,±6} ⇒ |Û|≤12; (V) gives |V̂|≤14), and is T-self-consistent iff (N1),(N2),p-odd — here my m2 recomputation applies: inside (U), m=116 so `XOR(supp f)=(⊕Ω)⊕((p+58) mod 2)T=T` exactly when p odd and ⊕Ω=0, which by Theorem 3(iii) is (N1)∧(N2). Sound. Necessity direction (⟹): an actual f at the frozen scope yields u,v with all of (U) (adopted packet + Theorem 3(iii)) and the cap/parity/p-range/mixed congruences; the flatness clause `V̂∈2+4Z` of (V) comes from the **adopted** odd-off-K congruence (LF 77), whose source is the named caller disposition not in this input set — the manuscript says exactly this (LF 7, 90). Hence Theorem 6 is an equivalence *relative to the frozen scope including that adoption*; without it, the unconditional statement is the same conjunction with (V)'s `V̂∈2+4Z` clause dropped from the necessary side. This is faithfully labeled "formulation closure", not a witness or exclusion.

### (f) Exact remaining gap and scope — **SUPPORTED** (LF 3, 121, 123–135)

(U) realizability of the frozen u-side system plus (N1),(N2) — open (the f263 §8 formal placement fails block compatibility at c=0: U₂(0)=168/16, U₃(0)=11; base LF 166–172). (V) solvability of the 256 capped congruent linear forms over Ω — open, "neither established nor refuted" (LF 121). **Confirmed: no witness, no exclusion of the residual/(0,4,8)/rank-two/global target is claimed; no statement about the other six class-count pairs, m=114, other fibre patterns, other ranks.** H appears only as the explicit local U₀-peak count, value 0 (LF 3, 123–135), with label-equivalence disclaimed. Nothing outside the declared scope was found in the manuscript.

## 3. Per-claim dispositions

| Claim (target LF) | Disposition | Basis |
|---|---|---|
| Theorem 1 caller split (25–29) | **SUPPORTED** | pair computation; V=a₀^⊥ gives a·y=r·y; control A*.caller-split |
| K≅V* identification (23) | **SUPPORTED** | ker(restriction)=⟨a₀⟩; K∩⟨a₀⟩=0 |
| Corollary 1 both-half cap decoupling (31) | **SUPPORTED** | F₂⁹=K⊔(K+a₀); Plancherel orthogonality 256Σuv=0 |
| Lemma 1 global mod 4 (33) | **SUPPORTED** | −2·(sum of 2⁸ signs); control A*.lemma1 |
| Parseval split 118784+143360=262144, fibre splits (37) | **SUPPORTED** | re-derived; control A*.parseval-split |
| Theorem 2(i) p odd ⟺ Σv≡2 (mod 4) (43–45) | **SUPPORTED at scope** | q=p+m/2 parity; needs m≡0 (mod 4), true at m=116; proof slip m1 |
| Theorem 2(ii) ⊕supp v=0 (46) | **SUPPORTED** | ⊕supp v=(1⊕q)T, LHS∈V, T∉V; control A*.T2-conclusion |
| k(a₀)=p−70∈{±1,±3,±5,±7}, p∈63..77 (48) | **SUPPORTED** | W_f(a₀)=4(p−70), cap ≤28 |
| Reconstruction converse / "nothing more and nothing less" (56) | **CONDITIONAL** | needs #{u=−1} even (m≡0 mod 4); automatic inside (U); m2 |
| Theorem 4 per-block taxonomy, class-forced δ, spike/quartet, ledgers (64–71) | **SUPPORTED** | per-block parity, annihilator algebra; controls C.a–e, D1 |
| Ω blockwise determined by u (73) | **SUPPORTED** (wording m4) | cardinality profile class-determined; positions are u-data (gap/2-set) |
| Theorem 3(i) W_s odd exactly on D; mod-4 identity (79) | **SUPPORTED** | per-block parity; control D2 |
| Theorem 3(ii) flatness ⟺ (N1)+(VB); s=0 ⟺ p odd; three mixed congruences (80–81) | **SUPPORTED** (equivalence); **CONDITIONAL** as a necessity statement for the object (adopted odd-half congruence) | controls D3/D4/D5 |
| Theorem 3(iii) (N1),(N2); 28-pair cancellation, counts 4,6,18 (82–86) | **SUPPORTED** | Ω-XOR decomposition; controls C.d, D6, D6b |
| Remark (a) non-implication by adopted statements (89) | **SUPPORTED** | formal: no adopted statement mentions ⊕D or ⊕z₀ |
| Remark (a) "generic 16-set fails with probability 63/64" (89) | **CONDITIONAL** (m3) | exact: P(⊕D=0)=(C(64,16)+63C(32,8))/(64C(64,16)); deviation from 63/64 = 585/27601853888≈2.1e−8 (control B); heuristic is for generic 16-sets, not the plateaued class |
| Remark (b) V̂∈{±2,±6,±10,±14}, zeros on K (90) | **CONDITIONAL** | on adopted odd-half congruence (disclosed) |
| Remark (c) ΣV̂=256v(0) (91) | **SUPPORTED** | inversion at 0 |
| §5 plateaued σ₁, |D|=16, dual pair, illustration (93–97) | **SUPPORTED** | 16U₁=3W(σ₁), 4096=256·16, dual construction; σ₁=(−1)^{x₁x₂+x₃x₄} re-derived |
| §6 energy/spectrum ledgers, n₃+3n₅+6n₇=1088, per-fibre 2E_s−8, relaxation, fibre sums (101–109) | **SUPPORTED** (value-set parts CONDITIONAL on adopted congruence) | arithmetic re-derived |
| Theorem 6 interface equivalence (113–119) | **CONDITIONAL** | ⟸ verified incl. m2-repair; ⟹ flatness clause rests on adopted odd-half congruence (LF 77) |
| Exact gap (U),(V); no witness/exclusion; no other scope; H local only (3, 121, 123–135) | **SUPPORTED** | full-read confirmation |

No claim is REFUTED; nothing is INCONCLUSIVE beyond the items marked above.

## 4. Findings (prospective corrections; frozen sources untouched)

**FATAL: 0. MAJOR: 0. MINOR: 4.**

- **m1** (LF 52–54): `#{y∈V: f(y+T)=1} = p` is asserted; true value `p+#{u=−1}` (=p+58 at scope). Parity — the only thing used — agrees because 58 is even. Conclusions unaffected.
- **m2** (LF 56): the converse/"exactly equivalent" claim needs `#{u=−1}` even (m≡0 mod 4) in addition to the listed hypotheses; automatic at the frozen m=116 and inside Theorem 6's (U), so no downstream effect; as literally worded for arbitrary pairs it is false (reconstructed XOR(supp f)=(⊕supp v)⊕((p+m/2) mod 2)T).
- **m3** (LF 89): the non-vacuity argument for (N1) is computed for *generic* 16-sets (and is essentially exact there: deviation 585/27601853888≈2.1×10⁻⁸, control B); D, however, is constrained to plateaued supports (§5), and non-vacuity within that class (existence of a plateaued 16-support with ⊕D≠0) is not shown. The satisfiability-in-isolation illustration (LF 97) is verified.
- **m4** (LF 73): "Ω … determined blockwise by u's classes alone" — only the per-block cardinality profile (1/2/0/4) is class-determined; the actual points depend on u's within-block placements (gap positions z₀, occupied 2-sets), as the same sentence then acknowledges. Wording imprecision only.

Observations (not counted): §0.1's summary "reduces the odd-half congruence structure to XOR self-consistency" (LF 7) is looser than Theorem 3(ii), which needs (N1) *and* the per-fibre congruences; Remark (b)'s "re-deriving the adopted zero placement from the interface" (LF 90) re-packages, but does not re-derive, the underlying oddness premise.

## 5. Reviewer-owned bounded exact control (receipt)

Script `reviewer-control-v1.py` (this wave directory), SHA-256 **`2f58c7ba92702b7e4887f3989c133f9529d612d6db7616150ba5ee2a98c618c2`**, 16235 bytes; receipt `reviewer-control-receipt-v1.json`. Python 3.14.3, standard library only, integer/Fraction arithmetic only (perf_counter for wall-clock only), no author code, no network, ≤120 s budget — actual **0.48 s**; run end **Thu Oct 29 18:49:25 PDT 2026**; **89/89 checks PASS**. Objects: seeded synthetic balanced Boolean functions on F₂⁹ with T≠0 (8 functions, m≡0 and m≡2 mod 4 both covered), the F₂⁴/k=4 brute-force analogue validating the subset-XOR character formula (then applied exactly to F₂⁶/k=16), all four-point block sign patterns on F₂², and a generic seeded 64-block class-profile system (16/4+6+18/3+17). The target object was never constructed; no universal claim was proven. Highlights: caller split, Lemma 1, Parseval split, orthogonality and the q=p+#{u=−1} identity on all synthetics; exact generic-16-set statistics N₀=7,633,243,745,820, N_x=7,633,233,227,520 over C(64,16)=488,526,937,079,580; class-forced δ, spike/quartet, even-fold 4/6/18 cancellation, W_s-odd-on-D, the mod-4 identity, flatness ⟺ (N1)+(VB) in positive and both negative configurations, Ω-decomposition and N2 non-vacuity. Disclosure: the first run reported 88/89 because my own acceptance threshold (10⁻⁸) was stricter than the true deviation |P(fail)−63/64|≈2.12×10⁻⁸; the threshold was corrected to 10⁻⁷ with the exact fraction recorded. No mathematical content of the control changed between runs.

## 6. Coverage receipt

| Item | Status |
|---|---|
| Manifest integrity (SHA/bytes/LF, before any body) | verified, all 7 matched |
| Full display, manifest order, raw ≤15-LF windows incl. endings, correction before base, target last | done (two reviewer path-typo window retries, disclosed) |
| Manuscript (target, 135 LF) | read completely; every theorem/lemma/remark rederived |
| Declared premises (inputs 1–6) | read completely |
| Excluded material (held/withdrawn/protected, P1 roster, f166 consumers, f239/CR7, m114 draft, enumerator extensions, sibling reviews, external sources) | not opened |
| Reviewer control | script + receipt in wave directory, ALL PASS, within limits |

## 7. Open items (exact remaining gap, unchanged by this review)

- **(U)** realizability of the frozen u-side system (f244/f255 block identities and counts, f263 cross-fibre conditions (C),(S), eight in-fibre zeros) *together with the new (N1),(N2)* — open; no witness, and the f263 §8 formal placement is a known non-realization (U₂(0)=168/16, U₃(0)=11).
- **(V)** solvability of the 256 capped (|V̂|≤14), congruent (V̂≡2 mod 4) linear forms over the u-determined Ω, with p∈{63,…,77} odd and the three mixed congruences — open, neither established nor refuted.
- The **adopted odd-half-k congruence** (off-K k odd) remains an externally adopted premise (used at correction LF 84; sourced to the named caller disposition `72122226…`, not an input body); Theorem 3's necessity reading and Theorem 6's (V)-flatness clause are conditional on it.
- Whether (N1) is non-vacuous *within* the plateaued class of §5 (i.e., whether some plateaued 16-support has ⊕D≠0) — not addressed by the manuscript, not addressed here.
- No witness or exclusion is claimed for the residual (G₃,H)=(1,0), the (0,4,8) case, the other six class-count pairs, m=114, other fibre patterns, rank two in general, or the global balanced NL≥242 target; all remain open. This review makes no novelty, formal-verification, independent-model-family, or human-verification claim; same-harness written reconstruction plus the bounded control above is the entire assurance boundary.
