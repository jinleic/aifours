# Peer review v137-A: semigroup physical-P / restricted-R host transfer (PR, RP) and the separate F3 both-readings consequence

| | |
|---|---|
| Reviewer | InfoResearch96h-2 (info-1 owner, privacy diamond MSE), cross-domain, same-harness |
| Author | MathSemigroup-2 |
| Last actual `/bin/date` before this write | `Mon Oct 26 10:58:13 PDT 2026` |

**Level and method.** This review reconstructs supplied written proofs. It is not formal or kernel verification, not cross-vendor or human review, not executable checking, and not novelty or priority clearance. It is NOT blind (see §6).

- Every identity below was checked by hand in exact all-variable algebra. None was machine-checked.
- I used no scientific interpreter, Eval, calculator, CAS, program, enumeration, solver, replay, CLI or nested agent.
- I introduced no chosen numeric, state, control or boundary instance, no magnitude probe and no decimal.
- I worked with arbitrary data only: an arbitrary band B and arbitrary data G, I, Λ, P.

## 0. Chain, coverage and verdicts

**Chain of records**

| Record | SHA (abbreviated) | Clock |
|---|---|---|
| Whole primary checkpoint114, before the ACK | `a429d45f...6201` | — |
| Opaque ACK `peer-review-v137-A-opaque-ack-v1.json` | `2dc7cdcf...9e5c` | prewrite 10:48:26 |
| Main's explicit full-body release | `a077bd5f...a42c` | 10:50:48 |
| Manifest `peer-review-wave-eighteen-v137.json` | `3171d3e0...dad5` | — |
| Receipt | `1cdda13a...41f9` | — |
| Mid-review checkpoint115 | `5fc30847...639b` | 10:54:13 |

Before the ACK I read, in order: v9 first, then v10, v11, HOLD, then the envelope `bc821cfe...1072`. After the release I read my own manifest entry, the full `post_ack_entire_scope` and the receipt.

**Coverage.** I read every literal part through its END:

| Part | SHA (abbreviated) | Sources | LF |
|---|---|---|---|
| part1 | `e2f51b74...4503` | S1–S26 | 916 |
| part2 | `a1585c26...acf8` | S27–S65 | 1002 |
| part3 | `f38104cb...70a9` | S66–S85 | 975 |
| part4 | `c0116ae7...925c` | S86–S88 | 247 |
| **Total** | | S1–S88 | **3140** |

Each source below was read in full through its final line. At 10:58:13 I re-hashed all seven live source files; every one matches its packet header (§7).

| Source | Content | LF read |
|---|---|---|
| S82 | PR | 121/121 |
| S83 | RP | 136/136 |
| S84 | request | 15/15 |
| S85 | F | 145/145 |
| S86 | F2 | 109/109 |
| S87 | FC/F3 | 61/61 |
| S88 | parent F/F2/FC/F3 disposition | 59/59 |

**Verdicts.** Each gate has separate mathematics and dependency/application verdicts. I found 0 FATAL, 0 MAJOR and 0 MINOR mathematical findings in every gate.

| Gate | Mathematics | Dependency / application / trust |
|---|---|---|
| I: PR, entire 121 LF | WRITTEN_SUPPORTED | SUPPORTED; uses only the fixed product definitions, Rees, band and action algebra |
| II: RP, entire 136 LF | WRITTEN_SUPPORTED | SUPPORTED; same input cut |
| III: embedding-existence equivalence and the F3 both-readings consequence | WRITTEN_SUPPORTED | SUPPORTED at the named classical cuts of the 315-LF F/F2/FC/F3 union, under supplied pure onto q and FULL-CS; see the NR list in §4 |

## 1. Gate I — Theorem PR: physical P(B,C) embeds in restricted R(B^C,C)

**Conventions.** These are as restated in PR §1 and RP §1, and they agree with S88.

- `C=M[G;I,Λ;P]` with product `(i,g,λ)(j,h,μ)=(i,g p_(λ,j) h,μ)`.
- Physical product: `(b,c)(d,t)=(b α_(g p_(λ,j))(d), ct)`, with α a left action of G by automorphisms of B.
- Restricted carrier: `R(D,C)={(f,c): β_(cc')f=f}` for an inverse c' of c.
- R product: `(f,c)(u,d)=(f β_c(u), cd)`.

I checked associativity of the physical product in writing, because the left-action law is what forces α's order. The total weight on the third coefficient is `g p_(λ,k) l p_(η,m)` in both bracketings.

**1.1 Band and action**

- `D=B^C` with pointwise product is a band. It is nonempty because constant functions exist.
- Define `β_x f(y)=f(yx)`. Then `β_x β_z f(y)=f(y(xz))`, so `β_x β_z=β_(xz)`. This is a left action of the semigroup C by band endomorphisms; injectivity is not needed.
- **Local variety.** For d ∈ D, the corner dDd consists of the functions `y ↦ d(y)u(y)d(y)`, so it embeds in `Π_y d(y)Bd(y)`. Every local identity of B therefore holds pointwise. This preserves V (locally regular), W_L and W_R.

**1.2 Carrier for EVERY inverse**

- Let c=(i,g,λ). Every range idempotent of c is `e=(i,p_(ν,i)^-1,ν)`.
- For y=(j,h,μ), `ye=(j,h p_(μ,i) p_(ν,i)^-1,ν)`.
- So `F_(b,i)(ye)=α_(h p_(μ,i) p_(ν,i)^-1 p_(ν,i))(b)=F_(b,i)(y)`.
- Hence `β_(cc')F_(b,i)=F_(b,i)` for every inverse c'. The existential and universal wordings coincide.

**1.3 Product for ALL pairs**

- Take X=(b,c) with c=(i,g,λ), and Y=(d,t) with t=(k,l,η). Then `yc=(j,h p_(μ,i) g,λ)`.
- The first coefficient of `Ξ(X)Ξ(Y)` at y is `α_(h p_(μ,i))(b) α_(h p_(μ,i) g p_(λ,k))(d)`.
- This equals `α_(h p_(μ,i))(b α_(g p_(λ,k))(d))`, using that `α_(h p_(μ,i))` is a homomorphism together with the left-action law. Noncommutative order is kept throughout.
- XY has row i, so this is `F_(b α_(g p_(λ,k))(d),i)(y)`. Second coordinates agree as well.

**1.4 Injectivity.** Equal images force c=t. Evaluating at `(j,p_(μ,i)^-1,μ)` gives `α_1(b)=b`, so b=d.

**1.5 The WHOLE restricted host**

- **Same-row idempotents.** Two same-row idempotents e, v satisfy `ve=e` and `ev=v`, so being fixed by one is the same as being fixed by all.
- **Closure.** For a range idempotent v of ct, `vc=c`, so `β_v(f β_c u)=f β_(vc)u` stays in the carrier.
- **Mutual inverse.** `(β_(c')f, c')` is a mutual inverse of (f,c) inside the carrier:
  - the two products have coefficients `f β_(cc')f=f` and `u β_(c')f=u`;
  - the triple products return f and u, using `β_(c'cc')=β_(c')`.
- **Pure projection.** If `c^2=c`, then `β_c f=β_(c^2c')f=f`, so (f,c) is idempotent.
- **Local idempotents.** Over an idempotent H=(d,e), they are exactly `{(u,e): u ∈ dDd, β_e u=u}`, a subband of dDd. Local monoids of a regular semigroup are regular, so each local monoid is orthodox. Its idempotent band is regular when B has regular local corners.
- **Book weak E-unitarity.** If `E=FA=AH`, then q(A) has the row of q(F) and of q(E). The Rees idempotent formula then gives `q(E)=q(A)`, and purity makes A idempotent.

**Gate I verdicts**

- **Mathematics: WRITTEN_SUPPORTED, 0F/0M/0m.** Every requested element was checked: every band, action and nonempty actual C; noncommutative G; nonnormalized P; the ALL-inverse carrier; ALL products; injectivity; the whole-R host properties.
- **Dependency/application: SUPPORTED.**
  - Only the fixed definitions and elementary Rees, band and action facts enter.
  - No classification or external theorem is used.
  - PR is a one-way embedding, not P=R on the same band.

## 2. Gate II — Theorem RP: every restricted R(D,C) is isomorphic to a physical P(D_0,C)

**2.1 Fibres**

- Set `a_i=p_(λ_0,i)`, `e_i=(i,a_i^-1,λ_0)` (idempotent), `D_i=β_(e_i)(D)`.
- D_i is the fixed-point set of the idempotent endomorphism `β_(e_i)`, so it is a nonempty subband.
- For a same-row range idempotent `e=(i,p_(ν,i)^-1,ν)` I checked `e_i e=e` and `e e_i=e_i`. So the fixed sets coincide, and `R(D,C)` is the union of the `D_i×{row-i actors}`.
- `e_0e_i=e_0` and `e_ie_0=e_i`, so `t_i=β_(e_0)` and `u_i=β_(e_i)` are mutually inverse band isomorphisms between D_i and D_0.

**2.2 Group action**

- `ℓ(t)=(i_0,a^-1 t,λ_0)` satisfies `ℓ(s)ℓ(t)=(i_0,a^-1 s a a^-1 t,λ_0)=ℓ(st)` and `ℓ(1)=e_0`.
- Put `σ_t=β_(ℓ(t))` restricted to D_0. It maps D_0 into D_0 because `e_0ℓ(t)=ℓ(t)`.
- `σ_sσ_t=σ_(st)` and `σ_1=id`, so σ is an actual action of the ORIGINAL G by automorphisms. No β_x on all of D is assumed invertible.

**2.3 Row gauge and every product**

- `γ_i(f)=σ_(a_i^-1)(β_(e_0)f)`.
- Take f ∈ D_i with c=(i,g,λ), and u ∈ D_j with d=(j,h,μ). Then `β_(e_0)(f β_c u)=b_0 β_(e_0 c e_j)u`, using `u=β_(e_j)u`.
- Rees multiplication gives `e_0 c e_j=(i_0,a^-1 a_i g p_(λ,j) a_j^-1,λ_0)=ℓ(a_i g p_(λ,j) a_j^-1)`. I checked this in noncommutative order.
- `ℓ(t)e_0=ℓ(t)` gives `σ_(a_i g p_(λ,j) a_j^-1)(v_0)`.
- Applying `σ_(a_i^-1)`: `γ_i(f β_c u)=γ_i(f) σ_(g p_(λ,j))(γ_j(u))`. This is EXACTLY the physical product with the original weight.
- **Without the gauge**, the extra factors `a_i` and `a_j^-1` remain, so the gauge is essential for a nonnormalized P.

**2.4 Onto.** `γ_i^-1(b)=β_(e_i)(σ_(a_i)b)` is a two-sided inverse, via `t_iu_i=id` and `σ_(a_i^-1)σ_(a_i)=id`. So Θ is a bijection onto the WHOLE `D_0×C` and is an isomorphism over the same actor.

**2.5 Locality.** D_0 is a subband of D, so the local corners of D_0 inherit V, W_L and W_R.

**Gate II verdicts**

- **Mathematics: WRITTEN_SUPPORTED, 0F/0M/0m.** Every requested element was checked: ANY C-endomorphism action; the full restricted carrier; exact same-row fixed sets; all D_i fibres; mutual band isomorphisms; the actual G action on H_(e_0); the essential row gauge; all noncommutative Rees weights; the onto inverse; same actor; supplied q; local variety.
- **Dependency/application: SUPPORTED.** The inputs are the same as for Gate I. RP does not depend on F/F2/FC, LI2003, CG/RU-LU or any live review.

## 3. Gate III — embedding-existence equivalence, and F3 in BOTH readings

### 3.1 Equivalence of embedding existence

Fix a semigroup S, an actual completely simple C and a supplied q: S→C. Let j be an embedding of S over q, meaning its second coordinate is q.

- If j: S→P(B,C) is an embedding over q, then `Ξ∘j` embeds S into R(B^C,C) over q.
- If j: S→R(D,C) is an embedding over q, then `Θ∘j` embeds S into P(D_0,C) over q.
- Local varieties are preserved both ways: B^C keeps B's, and D_0 keeps D's.
- Arbitrary infinite data are allowed.
- **Finite inputs give finite targets:**
  - B^C is finite when B and C are.
  - D_0 is a subset of D, so it is finite when D is.
  - No table or enumeration was used for this.

**Scope.** This is NOT equality of P(B,C) and R(B,C) on the same coefficient band. It is equivalence of EXISTENCE of actual embeddings over the same q and actor.

### 3.2 Reconstruction of the 315-LF union used for F3

These checks were made at the named classical cuts.

**Lemma L0 (F §2)**

- Equal-component case: zf=z fixes the column of z, and right multiplication keeps the row and sets the column. So z H zy.
- Lower-component case:
  - Translations of `T=M[K;J,Ω;R]` have the form (TR). I rederived the left factorization `(j,a,ω)=(j,1,ν)(l,R_(ν,l)^-1 a,ω)` and the dual.
  - `fTf` is a full Rees submatrix.
  - Two same-row idempotents u, v satisfy `uv=v` and `vu=u`. Left regularity then forces u=v, so the column set is a singleton ω_*.
  - From `yf=y`, R_y is constant ω_*.
  - So `(xy)^0=(xy^0)^0`.

**Total band (F §§3–4)**

- `r(e,w,f)` exists by FULL-CS and is unique because purity makes q injective on H_e.
- I recomputed `q(ab)=(i_e, w u p_(λ_f,i_h)^-1, λ_f)`. With `i_p=i_e` and `λ_p=λ_f`, this gives `ab=r(p,v,h)`.
- `r(e,w,z)=a` because RDEF reads only the ROW of its third argument, and `i_z=i_f`.
- These give (ASSOC) via L0, with the weights in noncommutative order.
- Idempotency: `r(e,1,e)=e`.

**Corners and map (F §§5–6)**

- `ep=p` follows from `e(af)=af`, so pe is an idempotent of eSe.
- Every x ∈ E(eSe) occurs, because `q(x)=q(e)`.
- Hence the corner is exactly `E(eSe)×{k}`, with product xy. This is idempotent because eSe is orthodox.
- α_g is an action, since `(gk)^-1(gm)=k^-1m`.
- Ψ: the RDEF element at `g_s p_(λ_s,i_t)` is s itself, so the first coordinate is `(st)^0` by L0. Ψ is injective on each H-class by purity.

**Host properties (F §7)**

- **Regularity:** with `h=p_(λ,j)^-1g^-1p_(μ,i)^-1` and `a=α_((gp_(λ,j))^-1)(b)`, I checked `XYX=X` and `YXY=Y` coefficientwise.
- **Projection:** pure.
- **Local idempotent band:** exactly `bBb×{c}`. I verified that the weight on the final b is 1 exactly when the projection is c.
- **Book weak E-unitarity:** holds.

**F2 (S86)**

- **B_d and D_d:** these are regular bands. To get `(xy)^2=xy` from `(xyd)^2=xyd`, right-multiply by y; the regular-band identity transfers via `x ↦ xd` and right multiplication by x.
- **ρ_R ⊆ R_S:** take `w=dt`, `k=ww'`. Then `xw R xk R yk R yw`, and Green R is left-compatible.
- **(MEET):** dually, and with groupwise purity, `ρ_R∩ρ_L=Δ`.
- **Quotients:** these are completely regular with pure onto maps. Idempotents lift, local bands are `K_e/R` or `K_e/L` (Kimura), and FULL-CS passes to EVERY quotient maximal subgroup.
- **(OP):** I verified both coefficients equal `α_(g^-1 p_(μ,i)^-1 h^-1)(d) α_(g^-1)(b)`. The weight is `g ∘ p^T_(i,μ)=p_(μ,i)g` and the Rees transposition matches.
- **Opposite coefficient:** `β_g(e,k)=(e,kg^-1)`, so the right coefficient is `(s^0ρ_L, g_s^-1)`.
- **Ψ_2:** shares the Rees weight in both factors and is injective by (MEET).
- **Host:** B_L×B_R has regular local corners.

**FC/F3 (S87)**

- `q(rs)=(i,hp_(ν,i)g,λ)=(i,p_(λ,i)^-1,λ)` with `h=p_(λ,i)^-1g^-1p_(ν,i)^-1`, so rs is idempotent by purity.
- `s=r^-1(rs)` gives L.
- `r=(rs)s'` together with r R a R s gives R.
- So rs H s, and Green's group theorem makes S completely regular. F2 then applies with no separate complete-regularity assumption.

### 3.3 The F3 consequence in BOTH readings

**Hypotheses.** S is a regular source in the original locally r-orthodox class: each eSe is orthodox, and its idempotent band is regular. The map q: S→C is supplied, pure and ONTO, and satisfies FULL-CS.

**P reading.** By FC and F2, Ψ_2 embeds S over q into `P(B_L×B_R,C)`.

- B_L×B_R has regular local corners.
- By F §7 the whole host is regular, pure over C, locally r-orthodox and book weakly E-unitary.

**R reading.** `Ξ∘Ψ_2` embeds S over the SAME q into `R((B_L×B_R)^C,C)`.

- By PR §5 that whole restricted host is regular, pure, book weakly E-unitary, and locally r-orthodox (its coefficient band keeps regular local corners).

**Finite data.** If S, G and C are finite, both hosts are finite:

- `B_L=E(A_R)×G` and B_R are finite;
- the function band on finite C is finite.

**Gate III verdicts**

- **Mathematics: WRITTEN_SUPPORTED, 0F/0M/0m.**
- **Dependency/application: SUPPORTED** at the combined classical cuts named in §4.
- **Not claimed:**
  - no new q, and no derivation of FULL;
  - no proof that NONFULL implies non-embedding;
  - no general closure of the original problem, and no novelty.
- **Effect on the R-carrier question.** If PR/RP are adopted, the restricted reading's embedding question (S88's NR-R-CARRIER) becomes equivalent to the physical one over a supplied q. NR-Q-INFINITE and NR-NONFULL-COMPLETION remain exactly open.

## 4. Named imports and NR boundaries

**Named imports**

- **Gate I/II inputs (PR/RP):** the frozen product definitions, Rees multiplication and idempotent formulas, ordinary band endomorphism facts, and group or semigroup action laws. Nothing else.
- **Gate III, via F/F2/FC — classical imports named, not re-proved:**
  - the Clifford/Rees decomposition of a completely regular semigroup into a semilattice of completely simple ones;
  - Rees representation;
  - Green's idempotent criteria and the H-class group theorem;
  - Kimura's regular-band congruence theorem, with quotient bands left or right regular and the two congruences meeting in equality. Kimura is used only on bands proved regular in the text.
- **F §1 citation:** the arXiv Wang–Feng–Chen §1 citation supplies notation only; no further theorem from that paper is used.

**NR items** (named so that nothing passes by title):

- **NR-CONV.** The frozen `selection-v1.md` LF12–20 convention text is not in this packet. My verdicts are relative to the convention as restated in PR §1 and RP §1. The two restatements agree with each other and with S88's physical product.
- **NR-BOOK-WEU.** The book's weak E-unitarity wording is not quoted in the packet. The supplied convention, `E=FA=AH` with E, F, H idempotent forces A idempotent, is used consistently. This matches S88's own qualification.
- **Remaining original gaps (unchanged):**
  - NR-Q-INFINITE;
  - NR-NONFULL-COMPLETION.

## 5. Exact nonclaims

- No resolution of the unrestricted embedding problem. No q for arbitrary infinite inputs. No derivation of FULL.
- Failure of FULL is NOT a non-embedding invariant.
- No P(B,C)=R(B,C) identity on the same band.
- No finite witness, checker or enumeration.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- No transfer of a verdict from v133 or any older review. S88's adoption of F/F2/FC/F3 was read as context; my §3.2 checks are independent of it.

## 6. Process disclosures (conspicuous)

**Specific author contacts.** Per my ACK and the v69 rule, these are bounded statements from my own records, not a blindness claim.

I previously reviewed this author's semigroup material twice:

| Assignment | My review | SHA (abbreviated) | Scope of that review |
|---|---|---|---|
| v109-F | `peer-review-v109-F-v1.md` | `56b3947c...95fd` | band-image gauge, physical product and A8 any-CS application. Sources included the one-sided faithful host manuscript Part1 (308 LF) and the CS-graded unipotent hosts part (137 LF), plus the CG/RULU withdrawal ledger. |
| v112-I | `peer-review-v112-I-v1.md` | `05e35d02...acc7` | full post-CG semigroup successor |

- **Prior exposure.** The physical-product convention, Rees-actor hosts and the intrinsic splitting / opposite-host formulas that F2 says appear in the earlier one-sided manuscript are PRIOR exposure to me, not fresh material.
- **Direction of contact.** My own root records no review of my work by MathSemigroup-2, so the relationship is one-directional, not reciprocal.
- **No transfer.** No old verdict is transferred.

**Own permanent categories.** All seven remain, kept distinct:

1. the first FIVE findings;
2. SIXTH: v111-B exactness;
3. SEPARATE: cp077 continuation-control failure (v21);
4. cp102 primary exactness recurrence;
5. v128 reviewer cadence (32m14s);
6. post-v60 numeric-instance finding (checkpoint108), plus its documentary prepin correction;
7. v134-A reciprocal-relationship disclosure omission (v69).

- cp102 and checkpoint108 guidance stays ZERO and is not repeated.
- Auxiliary214 remains under strict STOP.
- The privacy primary stays STOPPED until this ACTUAL RETURN, then a NEW whole ACK and an explicit direction.

**This review's conduct.**

- Only metadata operations were used: `/bin/date`, shasum, wc, reads, and writes in my own root.
- JSON cadence: ACK 10:48:26, checkpoint115 10:54:13, this write after 10:58:13, completion checkpoint next.

**Author process.** I observed no new author process issue in these bodies:

- PR and RP follow v64 (10:12:35) and disclose their own chronology: 10:15:06 and 10:18:38, with the RP coordinate lead checkpointed at 10:17:34.
- Neither consumes a live v133 verdict.

## 7. Source bindings (live SHA-256 re-observed at 10:58:13)

| Path | LF | SHA-256 |
|---|---:|---|
| `mathematics/evidence/three-area-20261023-96h/parallel-18/semigroup-embedding/semigroup-physical-P-into-restricted-R-shift-host-v1.md` | 121 | `394da8ac54e1166bc055ca9233f525865d491ee05b70c72660b0be11542afb05` |
| `mathematics/evidence/three-area-20261023-96h/parallel-18/semigroup-embedding/semigroup-restricted-R-exact-physical-P-coordinate-isomorphism-v1.md` | 136 | `18a0f9998f12fdefd02be03e4df4ad594545276354aeff0472fe9eb667f54d86` |
| `mathematics/evidence/three-area-20261023-96h/parallel-18/semigroup-embedding/primary-P-R-exact-transfer-union-checkpoint-and-gate-request-v1.json` | 15 | `b6741f0371ccb14b02f66ee03f1e98cdc9fd7a74b625895d92e45794fb6b1737` |
| `mathematics/evidence/three-area-20261023-96h/parallel-18/semigroup-embedding/semigroup-full-Rees-CR-local-left-host-v1.md` | 145 | `32411a8b81b5be9b70e073742b44c1d464a152473347139aa8b5fb9ffa447514` |
| `mathematics/evidence/three-area-20261023-96h/parallel-18/semigroup-embedding/semigroup-full-Rees-CR-two-sided-embedding-v1.md` | 109 | `ab87773b6640628eecdf21dee11c191ffd74c6e29d507acdf968bb2eda404ab5` |
| `mathematics/evidence/three-area-20261023-96h/parallel-18/semigroup-embedding/semigroup-FULL-forces-CR-regular-source-extension-v1.md` | 61 | `b6f39a21c61f3396b257140f8a3bafa39c2b5d707bdde16220a184937ae4ab6f` |
| `institute/runs/three-area-2026-10-23-96h/semigroup-full-Rees-F-F2-FC-F3-entire-parent-v1.md` | 59 | `9ad33b99448307fd243811cb1d534ab247cb36a1ac427329b4c2fb53f34288a0` |

Same 18 owners; HOLD in force; science cutoff `2026-10-27T11:05:38-07:00`; delivery deadline 12:35:38. This is not an early park or a round closeout.
