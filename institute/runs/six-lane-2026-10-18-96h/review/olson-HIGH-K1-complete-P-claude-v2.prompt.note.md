# HIGH-K1 / HIGH-K-RES: second-family full re-review on the S-1 input

**Method and reading limits.** I worked by hand from the pasted text only. I used no tools, code, computation, enumeration, assertions, network or delegation. I recomputed no SHA256, byte or LF count, so hashes are opaque labels to me. I only checked by eye that the main pins are cited consistently across documents: HK `f5b93572`, worker E1 `612f6cb3`, P `58a85ebe`, P verdict `c25230ad`, P errata `f908cbfa`/`dc73b8a3`, S(p) `d4d515cd`/`df1c5ac2`, both parts, manifest and coverage.

I cannot confirm any of the following:
- that the pasted bodies equal the hashed files;
- that the re-pasted parts equal the physical parts;
- the two-segment join of the earlier Claude note;
- model identities;
- any `/bin/date` stamp.

Earlier reviews, including this family's own first review, are treated as claims to re-check, not as evidence. This is a model-written review only. It makes no Lean, human-referee, novelty or runtime claim.

## 0. Disposition

| Item | Result |
|---|---|
| **Source gate** | **PASS.** The input now binds Theorem P's own acceptance record. No omitted body is load-bearing. This family does not trigger RE-REVIEW_REQUIRED. The first family's re-review is still required. |
| Theorem P import | **PASS** at its literal domain. The mandatory overlays change no HK step. |
| HK1 (every prime p≥7, every k≥p+2, κ̂=1) | **ACCEPT-WITH-FIXES**, relative to S(p) at secondary-statement trust |
| Separate p=5, κ̂=1 statement | **ACCEPT-WITH-FIXES**, same trust; covers this NF family only |
| §5 top family (CT-top, Φ≥4 near-pair) | **PASS** as proved necessary structure. Not an exclusion, not Φ2, not rigidity. |
| HIGH-K-RES (R0)–(R3) | **ACCEPT-WITH-FIXES** as the entire *necessary* residual. κ̂≥2 carries S(p) trust. |
| Exactness/converse observation from this family's first review | **REJECT** promotion. Parent erratum v2's M-6 text governs. |
| HIGH-K-CORE-COVER | Correctly labelled **UNPROVED** |

**Counts: 0 FATAL / 0 MAJOR.**
- Required MINOR already drafted and confirmed here: 5 (parent E1; parent E2 M-2 to M-5).
- New required MINOR: 1 documentary item, R-1, which closes S-1.
- Optional MINOR already drafted and confirmed: M-1, M-6, M-7, S-2.
- New optional MINOR: O-1 to O-3.

## 1. Theorem P: statement, domain, trust, order, degrees and every HK call

**Statement and domain.** The verdict (LF5) restates proof LF10–28:
- p is any odd prime;
- the word has N≤4p−1 and F≥1;
- n_t are the cyclic rotation-gap lengths between consecutive reflections;
- if F+Σ⌊n_t/2⌋≥3p−1, the word has an identity 2p-subword in increasing original order.

Nothing in the acceptance narrows this statement.

**Proof re-derived by hand (LF30–93).**
- **Steps 1–3.** M=(F−1)+Σ⌊n_t/2⌋≥3p−2. The map from parameters to selections is injective, because u_{t+1}=u_t⊕[f_t selected] and m_π=[π selected]⊕u_t. The selection is empty only at 0. The reflection count equals the number of colour changes around the cycle, so it is even.
- **Step 4.** By the product formula (P erratum v2, item 2), the prefix reflection parity before gap t or before f_t is ≡u_t, so the sign is c_t=(−1)^{u_t}. I checked three identities:
  - (c_t−c_{t+1})/2 = u_{t+1}−u_t in all four cases.
  - Summation by parts works with u_1=u_{F+1}=0.
  - c_t[m⊕u_t] = m−u_t for u_t∈{0,1}.

  Together these give V=Σ_{t≥2}β_t u_t+Σx_π m_π. V has degree ≤1 and may vanish identically (P erratum v1).
- **Step 5.** Z agrees with |S| on the box, and deg Z≤2. So deg Q≤3p−3<3p−2≤M. A monomial of degree <M omits some variable, and flipping that variable pairs terms of opposite sign. The point x=0 contributes +1, so a nonzero solution exists.
- **Step 6.** The selection is nonempty, has even size ≤4p−1, and its size is ≡0 mod p. So the size is exactly 2p.
- **Order.** Write the original word as AB and the rotated word as BA. Then P_A P_B = P_B^{−1}(P_B P_A)P_B, so the same positions give the identity in the original order (P erratum v2, item 1).

**Effect of the overlays.** The degree wording, product formula, original-order and notation overlays are exposition only. HK uses only the contrapositive of P's statement, so none of them can affect an HK step.

**Trust.** P is a written theorem, accepted at 2026-10-21T04:22:45 by both families and checked by a parent derivation. No computation and no unproved extension is a premise.

The header (LF1–7: brute-force checks, "NOT yet independently reviewed") lies outside the accepted mathematical text LF8–93. So do the Remarks (LF95–109: finite data, composite sharpness, conditional Brink extension). Both are historical, not re-executed, and not used by HK.

**Not backdated.** The HK manuscript postdates cp-04 (14:52:16), so its use of P falls within the gate's forward scope. Verdict LF13's non-backdating sentence concerns K0T/LOWER-K1, not HK.

The first packet's path-free evidence for P (K0*/RED LF7) is superseded, not retroactively upgraded. This family's earlier citation of P's p=5 scope through K0*'s p≥5 is likewise superseded by P's own "any odd prime" domain.

**Every HK call of P:**

| HK LF | P call | Check |
|---|---|---|
| 54–57 | For u, N=4p−2 and F=k+2H≥1. The gaps are the r_i plus F−k internal zero gaps. P fails, so F+Pgap≤3p−2. | F=2p−2+k−2κ̂ gives Pgap≤p+2κ̂−k ✓ |
| 57–59 | k≤p+2κ̂; k≥p+2 forces κ̂≥1; at κ̂=1, k≥p+3 gives F≥3p−1 | ✓ |
| 61–63 | Critical cell: Pgap=0, so each r_i∈{0,1}; R=p gives p singleton runs and 2 empty runs | ✓ |
| 182, 197 | (R1) keeps the full inequality; the top cell has Σ⌊r_i/2⌋≤2p−4 | ✓ |
| 207, 212–213 | κ̂=0 is old coverage; the critical cell has F+Pgap=3p−2, so P does not cover it | ✓ |
| p=5 | "Any odd prime" applies: k=7, F=13=3p−2, R=5 | ✓ |

P is applied to u itself, so "original order" there means u's own order. Nothing is transported back to w.

## 2. Per-claim verdicts (HK read through worker E1 and parent errata v1/v2)

A ✓ in the severity column means the fix is already drafted in the parent errata and is confirmed here.

| # | Claim (HK LF) | Verdict | Severity |
|---|---|---|---|
| C1 | General NF formulas; κ̂∈[0,p−1]; ZP_κ̂; one-way k/o_F relation (35–43) | PASS | — |
| C2 | (G) derived from GRX; interval pattern has Φ=2 and T=y_j′−y_j (44–52) | PASS | — |
| C3 | P uses gap lengths, not multiplicities; band k≤p+2κ̂; κ̂=0 is old coverage (54–59) | PASS | — |
| C4 | Critical-cell structure and zero-sum dichotomy (61–66) | PASS | optional M-1 |
| C5 | Pair padding / skeleton (68–77) | FIX | MINOR, required M-2 ✓ |
| C6 | COLOR fact (79–89) | PASS | — |
| C7 | §3, zero-sum-pair branch (91–102) | FIX | MINOR, required parent E1 ✓ |
| C8 | §4, S(p) coefficient split and bipartition lemma (104–120; E1 item 1) | FIX | MINOR, required M-3 ✓ |
| C9 | §4, disjoint palettes (122–128) | PASS | — |
| C10 | (X), fresh four-change argument (130–136) | PASS | — |
| C11 | HK1 for p≥7 and every k≥p+2; separate p=5 statement (23–25, 138–141) | FIX | MINOR, required M-4 ✓ |
| C12 | Top family: exact n=2p−Φ; CT-top (145–151) | PASS | optional M-7 |
| C13 | Φ≥4 common nonzero near-pair (153–169) | PASS | — |
| C14 | Φ2 one-filler failure, correctly not a no-go (170–171) | PASS | — |
| C15 | HIGH-K-RES (R0)–(R3) and top specialization (173–199; E1 item 2) | FIX | MINOR, required M-5 ✓; optional M-6, M-7, O-3 |
| C16 | HIGH-K-CORE-COVER unproved (201–203) | PASS (as a limitation) | — |
| C17 | Coverage table; strict extension of VAC/P (205–214) | PASS | — |
| C18 | Scope, Step 0, withdrawn preview, UPAR5 boundary (7–31) | PASS | — |
| C19 | Source/process boundary (216–231) | FIX | MINOR, required R-1; optional O-1, O-2 |
| C20 | Worker erratum 1 | PASS | — |
| C21 | Parent erratum v1 (block-label occurrences) | PASS | — |
| C22 | Parent erratum v2 (M-1 to M-7, S-1, S-2, P-1) | PASS | — |
| C23 | Theorem P import (§1 above) | PASS | — |
| C24 | Promotion of (R0)+(R2) exactness or a converse | REJECT | not in scope |

No mathematical claim is rejected.

## 3. Re-derivation record (condensed)

**General NF and GRX.** Every ℓ_i is odd, so δ=k−Φ and C_max=2H+Φ. Substituting n=2p−C into GRX LF18–19 gives (G) exactly. Because Σθ_i=0, an interval P=R_{j+1..j′} has T=y_j′−y_j. If H≥p, the all-plus pattern would give an identity, so κ̂≥0.

**Critical cell (p≥5, k=p+2, κ̂=1).**
- H=p−2, F=3p−2 and R=p.
- There are p maximal cyclic reflection runs. A ρ_0 is a rotation letter, not an empty gap.
- All-plus (G) forbids zero-sums of even length in [4,p], and every nonempty zero-sum of odd terms has even length.
- So Y is either zero-sum-free or has a zero-sum pair. The parity of |Y| plays no role (M-1).

**Padding.**
- In each block, reduce the selected count c to c mod 2; this is valid because σ_y^{c+2j}=σ_y^c.
- For c∈{0,1}, block i can take up to h_i extra pairs, and any total from 0 to H is realisable.
- So u has an identity 2p-subword exactly when the skeleton has an identity selection of even length L∈[2κ̂+2,2p].
- Arbitrary h_i are kept throughout; GRX sees the blocks only through 2H+Φ.

**COLOR.**
- σ_aσ_bσ_cσ_d=ρ_{a−b+c−d}, so two non-interlaced doubled labels give an identity of length 4.
- Three pairwise-interlaced doubled labels must sit as ABCABC, whose product is (σ_Aσ_Bσ_C)²=1.
- The count p+2 = (#labels present) + (#doubled labels) then forces exactly two doubles and all p labels present.
- C=2A−B differs from A and B and occurs once. The A-to-A arc that avoids C contains a B, and the selection ABAC has product ρ_{2A−B−C}=1.
- Padding needs (2p−4)/2≤H and (2p−6)/2≤H, which hold for p≥5.

The hypothesis is on **block labels**, as parent E1 states. A bound on raw reflection-letter multiplicity would contradict arbitrary h_i.

The hypothesis also cannot simply be dropped. cp-02 LF60–62 gives the representative sequence 0,0,0,1,…,p−1. That note is not a premise, but I rechecked it by hand: the sequence has no pure-reflection identity of even length ≥4, because alternating sums of a weakly increasing sequence lie in (−p,0]. This is why §3 has to handle a label occurring three or more times through rotations.

**§3 (Y has a zero-sum pair).**
- **x=0:** since k>p, some block label repeats. The Φ=2, T=0 interval pattern together with the two zero letters gives n=2∈[2,p].
- **x≠0, some label occurs ≥3 times:** three occurrences cut the cycle into three arcs, and one arc misses both marked letters. Taking P to be that arc, both letters get sign +1 and cancel.
- **Otherwise:** every label occurs at most twice, and COLOR plus padding applies.
- No S(p) is used in §3.

**§4, coefficients.** Parity is a homomorphism Z_{2p}→Z_2, so every a_i is odd (M-3). Put E=W−p≤p−1.
- s≥2: b≤E−2(s−1)+1≤p−2s+2≤p−s=u_one.
- s=1: b≤p. The case b=p is exactly (X); otherwise b≤p−2.
- s=0: every coefficient is 1.

The signed cancellations are either one coefficient-1 term on each side (size 2), or b against b coefficient-1 terms (size b+1, which is even and ≤p−1). Distinct occurrences are used throughout.

**§4, palettes.** Suppose equal labels sit in different maximal runs. Then both arcs between them contain rotations, T=0, and the cancellation size lies in [2,p−1]⊂[2,p]. So the p palettes are disjoint. There are p+2 blocks in p runs, and the empty-run rule forces some palette to have size ≥2. That would need at least p+1 colours, a contradiction.

**(X).**
- g=(1,c) with c≠0, and pg=(1,0), so the rotations are ρ_c^{p−1}ρ_0.
- Take two nonadjacent runs as the minus set; this gives Φ=4 and exists because k≥7.
- For each d∈[−B,A], select |d| signed c-letters, adding ρ_0 when |d| is odd. The size is even and ≤p−1, and the values dc cover F_p.
- At Φ=4, (G) allows n∈[0,min(p,2p−4)]=[0,p] for p≥5.

S(p) is used to *reach* (X). The deduction from (X)'s literal rotations is pure GRX.

**p=5.**
- NF (stated for p≥5), GRX and P (any odd prime) all apply.
- S(5) is the n=10 case of S(p) erratum M-1/M-2.
- Padding needs 3≤H=3 and 2≤3.
- Bipartition sizes are ≤4.
- The k=7 cycle has nonadjacent runs.

**Top family.** Here H=0, F=k, R=3p−4, Φ≤p+1 and n=2p−Φ.
- CT applies with κ=p−1, n_CT=p−4≥1 and |Y|−n_CT=2p, giving a capped sum ≤2p−6. This is the only (R3) test in this family.
- Lemma M (re-proved inline in HK) with q=p−1 needs μ≤2p−3. For Φ≥4, n∈[p−1,2p−4], so the fillers needed, n−p+1, lie in [0,p−3], within the p−2 available. Cauchy–Davenport on p−1 nonzero differences covers F_p. Hence μ≥2p−2.
- The heavy value is unique, since 4p−4>R. Its unsigned class is common to all Φ≥4 patterns, and such patterns exist.
- The class is nonzero. Otherwise 2p−2 zero letters plus a repeated label would give a Φ=2 pattern with n=2p−2 and T=0.
- So at most p−2 letters lie outside the class.
- At Φ=2 the method needs p−1 fillers but only p−2 remain. HK correctly treats this as a failed step, not a no-go.

**HIGH-K-RES.**
- κ̂≤p−1 follows from H≥0.
- κ̂≥1 follows from P.
- κ̂≠1 follows from HK1, and therefore depends on S(p).
- k≤p+2κ̂, and R≥p follows.
- (R1)–(R3) are literal. The (R3) domain is max(1,2κ̂−k)≤q≤2p−k−2 with q≡k mod 2. When it is empty, that k is not removed.
- Every surviving NF satisfies (R0)–(R3), so the residual is **necessary**. Nothing beyond that is credited.

## 4. Fixes

### 4.1 Already drafted: confirmed correct and sufficient (no change requested)

- **Parent E1** (HK LF97, LF101): count occurrences among the block labels y_1,…,y_k. This is necessary and correct, and changes no case.
- **E2 M-2** (LF77), **M-3** (after LF107) and **M-5** (LF26, LF192): correct as written.
- **E2 M-4** (LF138): correct. It is also more precise than this family's earlier wording, which said S(p) enters "only … outside (X)" (first review M-4 and §5.1). (X) is reached through S(p)'s coefficient split. The parent's boundary is right: S(p) is "used only in the zero-sum-free branch", with "no additional S(p) step" inside the (X) deduction. I withdraw the earlier phrasing.
- **Optional M-1, M-6 (the parent's non-promoting text), M-7 and S-2:** correct as drafted.
- **Worker E1** items 1–2: correct.

### 4.2 New

**R-1 (required, documentary MINOR; closes S-1).**
- (a) The HK1/HIGH-K-RES verdict should cite P's authority as follows, and should not cite K0*/RED LF7 as the evidence:

  > Theorem P, proof-theoremP.md `58a85ebe…` mathematical LF8–93, at its 2026-10-21T04:22:45 two-family acceptance (verdict `c25230ad…`, errata `f908cbfa…`, `dc73b8a3…`, disposition `c92632ce…`), used only at its literal statement; header LF1–7 and Remarks LF95–109 are historical, not premises.

- (b) Read HK LF219–220 "…mandatory overlays and actual used primary text are supplied;" as:

  > …are supplied, except that Theorem P's own acceptance record was absent from the first two-part packet; it is bound only in the S-1 re-review input and is not retroactively credited;

- If parent E2 LF21 ("old source-intake claims remain incorrect historically") is meant to cover LF219–220 already, record that explicitly instead of applying (b).

**O-1 (optional, trust precision).** At HK LF107–108 and LF223, after "primary Xia-Yuan proof unread", add:

> ; the KPS-SLZ item-1 bundle also carries the import note's (I1) index-one theorem at author-statement level and erratum-1 M-3 trust items (i)–(ii)

**O-2 (optional, editorial).** At HK LF224, change "Classical CD/CT retain…" to:

> Classical Cauchy–Davenport and the parent-accepted lane Lemma CT (STAB-delta item 6; RS(a) not replayed) retain…

CT is a lane result, not a classical theorem.

**O-3 (optional, non-promotion wording).** At HK LF26, change "induces the exact necessary residue system" to:

> induces the complete literal necessary residue system (necessary only; no converse, feasibility or exact-classification claim)

This aligns LF26 with the parent's M-6 text.

## 5. Source gate: PASS

- **S-1 is resolved by the input, not by a patch.** P's verdict, both errata, the disposition and the whole proof are present. The overlays preserve P's statement. P's trust class (a two-family written theorem with no computation premise) is at least what HK assumed.
- **Newly referenced items that are still not pasted are not load-bearing:**
  - The P review outputs, receipts and parent written check: P was re-derived above from the supplied text.
  - The HK review receipts.
  - The prerequisite consolidated erratum, which cp-05 says was read. STAB LF11 and delta D-2/D-4 attach its R4/R6 corrections to CF(L) and AP. AP′ erratum D2 says LSplus-e2 uses neither AP nor AP′. CT's own proof (LF16–19) uses only RS(a). So CT's statement carries no overlay from this erratum.
- **Previously removed bodies, re-challenged.** I re-checked the RUNS verdict; UPAR5 LF1–10, LF12–13 and its erratum 1; ALS LF63–76 and LF78–79; ZX LF21–48 and LF62–77; the terminal-κ̂0 corollary; KPS-v4; REFLHI; and refl-b0. None supplies a step used by HK1, §5 or HIGH-K-RES.
- **Historical coverage prose.** The RUNS and κ̂0-corollary coverage entries overstated what was supplied for P. That is now moot, since P's own record is bound.
- **Checked non-issue: ASSEMBLY-P erratum v1, m1.** It restricts that proof's *summary* NF-existence sentence to o_F≤p. HK never needs NF existence, because its antecedent is existential. The NF properties HK does use are stated generally in several places:
  - ROT-few-E v4 LF30–43;
  - ALS proof LF49–62 and row 77 ("every avoider");
  - ROT-LS, ROT-P and ROT-PP1, which apply NF with no o_F bound and at k≥p+1.
- **First family.** This return cannot discharge the first family's re-review on the same input. Its earlier source PASS on P relied on the coverage prose (Codex LF170).

## 6. Process (separate from the mathematics)

**Permanent and uncured:**
- UPAR4 PROCESS MAJOR (ack1 LF59–64).
- Pre-ack1 PROCESS MINOR (cp-01 LF9).
- Pre-ack2 PROCESS MINOR (cp-02 LF9–14).
- Parent clerical path/deadline defect (addendum 1).
- Parent lower-terminal documentary MAJOR (ack2 LF27–43; addendum 2).
- Inherited parent frontier-enumeration PROCESS MAJOR (v8 LF19).
- The first packet's incorrect P-coverage prose (S-1), kept as a historical record.

**P-1 (parent check confirmed).**
- Hand differences of the recorded stamps are 244, 1295, 1235, 505, 874, 739, 595 and 477 s.
- The target misses (95 s and 35 s) are disclosed, and no recorded interval exceeds 1800 s.
- The HK1 derivation falls between cp-02 ("NOT solved", 14:23:16) and cp-03 ("candidate", 14:43:51).
- The manuscript has no clock line. Its creation is bounded only from both sides:
  - after cp-04 (14:52:16);
  - before worker E1's creation, since E1 embeds the manuscript's hash.
- E1's 15:00:42 clock was read before E1 itself was created, and cp-05 binds both files at 15:06:50.
- All of these are self-reported stamps. There is no before-long-subcase or global compliance certificate.

**cp-07.** The refused duplicate exclusive-create (FileExistsError before any write) was disclosed. No departure is assessed.

**No new process departure found.**

## 7. Retained trust boundaries

**HK1 (p≥7):**
- **NF:** ROT-few-E v4 LF28–43 via fewodd addendum LF12; ZX overlays 1–3; lowodd item 2, M1 and M4.
- **GRX:** lowodd item 1, with M1/M2.
- **Theorem P:** the §1 authority, used at its statement only.
- **S(p):** KPS-SLZ item 1, with its import note and erratum, at secondary-statement trust. This includes (I1) and the M-3 trust items. It is used only in the zero-sum-free branch, including to reach (X).
- **S(p)-free parts:** §3, COLOR, padding and the (X) deduction.
- **Not used:** Lev, CT, VAC (redundant), FB-p/ARC0, UMR/UPAR frames, and any computation.

**p=5, κ̂=1:** the same imports, with S(5) at n=10 per S(p) erratum M-1/M-2. This covers only this NF family.

**Top family:** NF, GRX, CT (RS(a) not replayed), Lemma M as re-proved inline, and classical Cauchy–Davenport. No S(p).

**HIGH-K-RES:** NF, GRX, P, CT and HK1. The bound κ̂≥2 carries S(p) secondary-statement trust. The residual is necessary only, with no exactness or converse.

## 8. Not established

- HIGH-K-CORE-COVER for any κ̂≥2, including the top family.
- Φ2 behaviour; rotation-pair or reflection rigidity.
- Full terminal k≥p+2 exclusion.
- Any terminal k≤p NF exclusion, o_F equivalence or "only remaining gap" composition.
- Full ordered Olson for D_{2p}.
- Any p=5 result beyond the κ̂=1 family.
- Novelty, priority or independence; any formal, human or runtime certification.
