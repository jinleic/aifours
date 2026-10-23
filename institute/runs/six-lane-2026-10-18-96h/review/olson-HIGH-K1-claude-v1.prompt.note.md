# HIGH-K1 / HIGH-K-RES: independent hostile full review, through worker erratum 1

**How this review was done.** I worked by hand from the two pasted parts and the manifest/coverage metadata. I used no tools, code, computation, enumeration, assertions, network or delegation. I did not recompute any SHA256, byte or LF binding; the text is reviewed as pasted. This is a model-written review only. It makes no formal (Lean), human-referee, novelty/priority or runtime claim.

**Labels used below.**
- **proof LFn**: proof-HIGH-K1-and-core-v1 (f5b93572…).
- **E1**: erratum-1 (612f6cb3…).
- **GRX**: notes-GRX-v1 (afc6c31a…).
- **NF**: proof-ROT-few-E-v4 (ac560eb8…).
- **TP**: proof-theoremP (58a85ebe…).
- **PP1**: proof-ROT-PP1-v2 (99143ea5…).
- **CT**: proof-LSplus-e2-v1 (2effb09e…).
- **Sp / Sp-E1**: S(p) import note (d4d515cd…) and its erratum (df1c5ac2…).
- **K0R**: K0\*/RED verdict (879aeee7…).
- **KPS**: KPS-SLZ verdict.
- **STAB**: STAB-delta verdict.
- **ZX**: zx-s1c verdict.
- **LO**: lowodd verdict v2.
- **ALS**: ASSEMBLY-LS proof v2.

## 0. Disposition

| Item | Result |
|---|---|
| **Critical source gate** | **NOT TRIGGERED.** No removed or non-pasted body is load-bearing for any used step. One provenance defect (S-1: Theorem P's own acceptance record is not bound) is documentary. It escalates to **RE-REVIEW_REQUIRED for both families** if that record carries any overlay, scope restriction or trust class not visible in the packet. |
| HK1 (every prime p≥7, every k≥p+2, κ̂=1) | **ACCEPT-WITH-FIXES**, relative to S(p) at secondary-statement trust |
| Separate p=5 κ̂=1 statement | **ACCEPT-WITH-FIXES**: same trust, this NF family only |
| §5 top diagnostic (CT-top, Φ≥4 near-pair) | **PASS** as proved necessary structure; correctly not an exclusion, not Φ2, not rigidity |
| HIGH-K-RES (R0)–(R3) | **ACCEPT-WITH-FIXES** as the entire remaining residual |
| HIGH-K-CORE-COVER | Correctly labelled **UNPROVED** |
| Counts | 0 FATAL / 0 MAJOR / 5 required MINOR / 4 optional MINOR; 1 process observation the parent must check against its own records |

## 1. Critical source gate: every omission challenged

| Omitted body | Step that could need it | Substitute already in the packet | Load-bearing? |
|---|---|---|---|
| runs-parent-verdict (all) | Cyclic conjugation (proof LF77) | GRX LF41-42 and TP LF14-15 prove it inline. No RGR is used. | No |
| UPAR5 verdict LF1-10, 12-13; UPAR5 erratum v1 | None | UPAR5-E2 LF5 replaces the whole LF11 paragraph. The notice is placed correctly, and the withdrawn VAC clause is never used. | No |
| ALS LF63-76, 78-79 | GRX and DAV registry rows | GRX is bound directly. DAV is redundant (E1 item 2: κ̂≤p−1<k−1). | No |
| ZX LF21-48, 62-77 | NF/κ̂ overlays | Overlays 1-9 (LF49-61) are complete; items 1-3 are the ones used. | No |
| erratum-2-prereq | CT | CT's statement and its own proof use only RS(a) (CT LF16-19). The CF/R4 mandate in D-4 attaches to LS+2's second dependency, not to CT. | No |
| KPS-v4 (FB-p/ARC0) | §4 bipartition lemma, (X) | Proved inline at LF116-120 and LF130-135. See the credit note in §4. | No |
| REFLHI, refl-b0 | None | — | No |
| PP1 LF1-16, 23-37, 67-85, 103-211 | VAC, Lemma M | VAC statement LF21 and proof LF86-92; (SR) LF57-61; Lemma M LF96-102, re-proved at proof LF155-157 | No |
| GRX LF1-6, 43-54; NF outside 28-43; CT outside 13-19 | (G), NF, CT | The full statements, with GRX's proof, are pasted | No |
| S(p) parent range-check JSON (KPS LF8) | S(5) | KPS item 1 (p≥5) and Sp-E1 M-1/M-2 | No |
| 28 intake pins not in the range table | Step-0 only | k≤p+1 coverage is never a premise of HK1 or HIGH-K-RES | No |
| **terminal-κ0 corollary; TP LF1-7** | **Accepted status of Theorem P**, used at proof LF54-59, LF62-65 and LF122-128 | TP statement and setting (LF8-28). K0R LF7 says "Imports: Theorem P (accepted)", with no path or hash. v8 LF7 and cp-02 LF40-41 also refer to it. | **Not load-bearing for content; provenance defect, see S-1** |

On S-1: the user's rule admits declared accepted theorem statements as imports. P's full statement is pasted, and a supplied accepted parent verdict (K0R LF7) declares P accepted at a scope (length 4p−2, every p≥5) that contains the use here. No supplied text points to any P overlay.

The coverage claim that P's "accepting record [is] directly supplied" is not literally true, however. P is also the only used import whose own accepting verdict is not bound.

## 2. Per-claim verdicts

| # | Claim (proof LF) | Verdict | Severity | Evidence |
|---|---|---|---|---|
| C1 | General NF formulas; κ̂∈[0,p−1]; ZP_κ̂; one-way k/o_F (35-43) | PASS | — | NF LF37-43; ALS LF56-62; ZX ov.1-3 |
| C2 | (G) for every z; interval pattern Φ2, T=y_j'−y_j (44-52) | PASS | — | GRX LF14-19, 40-41; LO M1/M2; PP1 LF62-65 |
| C3 | P uses gap lengths, not multiplicities; band k≤p+2κ̂; κ̂0 is old coverage (54-59) | PASS | — | TP LF17-28; PP1 LF21; proof LF207 |
| C4 | Critical-cell structure (61-66) | FIX | MINOR, optional (M-1) | — |
| C5 | Pair padding / skeleton (68-77) | FIX | MINOR, required (M-2) | GRX LF24-29 |
| C6 | COLOR fact (79-89) | PASS | — | Re-derived in §3.2 |
| C7 | §3 zero-sum pair, x=0 and x≠0, no S(p) (91-102) | PASS | — | (G) at Φ2 admits n=2∈[2,p] |
| C8 | §4 S(p) coefficient split and cancellation (104-120; E1 item 1) | FIX | MINOR, required (M-3) | KPS item 1; Sp LF12-18; Sp-E1 |
| C9 | §4 disjoint palettes, ≥p+1 colours (122-128) | PASS | — | NF LF38 empty-run rule |
| C10 | §4 (X) fresh four-change argument (130-136) | PASS | — | (G) at Φ4 admits n∈[0,p] |
| C11 | HK1 for all p≥7 and all k≥p+2; separate p=5 statement (23-25, 138-141) | FIX | MINOR, required (M-4) | ALS LF77 (NF scope p≥5); Sp-E1 M-1/M-2 |
| C12 | Top family: exact n=2p−Φ; CT-top (145-151) | PASS | — | CT LF14-19; STAB item 6 |
| C13 | Top family: Φ≥4 near-pair; nonzero class (153-169) | PASS | — | Lemma M; Cauchy-Davenport (PP1 LF53-55) |
| C14 | Top family: Φ2 one-filler failure, not a no-go (170-171) | PASS | — | — |
| C15 | HIGH-K-RES (R0)-(R3) and top specialization (173-199; E1 item 2) | FIX | MINOR, required (M-5); optional (M-6, M-7) | §3.4 below |
| C16 | HIGH-K-CORE-COVER is unproved; no composition claimed (201-203) | PASS | — | Scope addendum 2, LF14 and LF21 |
| C17 | Coverage table; strict extension of VAC/P (205-214) | PASS | — | VAC gives only κ̂≥1. P does not fire: F+Pgap=3p−2<3p−1. |
| C18 | Scope, Step-0 result, withdrawn preview, UPAR5 boundary (7-31) | PASS | — | ALS verdict LF11-13; ASSEMBLY-P verdict LF11-13 and LF55; UPAR5-E2 LF5 |
| C19 | Source/process boundary statement (216-231) | FIX | MINOR, required (S-1) | — |
| C20 | Erratum 1 | PASS | — | No inequality or test changes |

No claim is REJECTED.

## 3. Re-derivation record

### 3.1 General NF, GRX and the P-gap reduction

**NF formulas.** With k≥2, every block is odd. So F=k+2H, κ̂=p−1−H and R=2p+2κ̂−k. Since H≥0, κ̂≤p−1. Avoidance transfers from w to u only (w→u).

**(G).** Because every l_i is odd, δ=#{i: f_i=0}=k−Φ and C_max=2H+Φ. Put n=2p−C. Then:
- C≤C_max is equivalent to n≥2κ̂+2−Φ.
- C≥Φ is equivalent to n≤2p−Φ.
- n is even exactly when C is even.

This is exactly LF49. Using an arbitrary z is legitimate because of the global sign symmetry (GRX LF40-41; LO M2). The all-plus pattern gives κ̂≥0 and ZP_κ̂.

**Theorem P.** The gaps of u are the r_i plus F−k internal zero gaps, so the floor sum is Pgap. An avoider therefore has Pgap≤p+2κ̂−k. Consequences:
- At κ̂=0, P alone already forces k≤p, so VAC is a second, redundant provider. No credit is claimed for it.
- At k≥p+2, P alone forces κ̂≥1.
- At κ̂=1, P forces k≤p+2.

**Critical cell k=p+2, κ̂=1.** Here H=p−2, F=3p−2, R=p and Pgap=0, so every r_i∈{0,1}. That gives p single letters, two empty runs, and p maximal cyclic reflection runs holding p+2 blocks. A ρ_0 is a letter, not an empty gap. ZP_1, together with the fact that odd zero-sums have even length, leaves only length-2 zero-sums.

### 3.2 κ̂=1 branches

**Padding.** The letters selected from one block are consecutive in the selected subsequence, and σ_y^(c+2j)=σ_y^c. Each block still holds h_i pairs whether c=0 or c=1. The admissible lengths are L∈[4,2p].

**COLOR fact.**
- σ_aσ_bσ_cσ_d=ρ_(a−b+c−d), so non-interlaced AABB/ABBA patterns give the identity.
- If three values are doubled, the only pairwise-interlaced arrangement is ABCABC, and (σ_Aσ_Bσ_C)²=1.
- So at most two values are doubled. Then exactly two are, A and B, and all p values occur.
- C=2A−B differs from A and B because p is odd, and it occurs once.
- On the A-to-A arc that avoids C, the selection A,B,A,C has product ρ_(2A−B−C)=1.

A by-product: every critical NF has some value occurring at least 3 times.

**§3, Y has a zero-sum pair.**
- x=0: two equal block values exist (k>p). Their interval pattern has Φ=2 and T=0, and selecting the two zero letters gives n=2.
- x≠0 with some value occurring ≥3 times: three occurrences split the runs into three arcs. One arc misses both marked letters, so both letters land in the same zone and their signed sum is 0.
- Otherwise every value occurs ≤2 times and COLOR applies.

No S(p) is used in §3.

**§4, coefficient split.** Let E=W−p≤p−1.
- s≥2: b≤p−2s+2≤p−s=u_one.
- s=1: b≤p, and b>u_one forces b=p, which is case (X).
- Bipartition lemma: either one coefficient-1 term on each side, giving size 2; or one b-term against b coefficient-1 terms, giving even size b+1≤p−1.

**§4, palettes.** If one value appears in two different maximal runs, both arcs between them contain a letter. That gives Φ=2, T=0 and a cancelling selection with n∈[2,p−1], which (G) admits. So the palettes are disjoint. Some run holds at least two blocks, and adjacent blocks in a run differ, so at least p+1 colours would be needed.

**§4, case (X).** Here g=(1,c) and pg=(1,0), so Y=ρ_c^(p−1)ρ_0.
- Take the minus set to be two nonadjacent runs; this gives Φ=4, which exists since k≥7.
- For each of the p consecutive integers d∈[−B,A], select |d| signed c-letters, plus ρ_0 when |d| is odd. The size is even and at most p−1.
- (G) admits [0,p] at this pattern, so every residue dc of F_p is reached.

**Exhaustion and quantifiers.** The three branches cover every Y. k≥p+3 is excluded by P. The distribution of the extra odd-block pairs never matters, since (G) depends only on 2H.

The p=5 case checks out: NF holds for p≥5, P is stated for every odd prime, S(5) holds at Sp-E1 trust, k=7 has nonadjacent runs, and min(5,6)≥4.

### 3.3 Top family: k=p+2, κ̂=p−1

**Setup.** H=0, all blocks are singletons, F=p+2 and R=3p−4. Every Φ is even and at most p+1, and (G)'s lower and upper bounds coincide at n=2p−Φ.

**CT-top.** CT applies with κ=p−1, n=p−4 and R−n=2p. This is the unique (R3) test at the top family. It gives the sum of min(p−4, v_x) is at most 2p−6.

**Lemma M step.** Apply Lemma M to the signed multiset with q=p−1; this needs μ≤2p−3. For Φ≥4, n lies in [p−1,2p−4]. The fillers needed, n−(p−1), lie in [0,p−3], and p−2 leftovers are available. Cauchy-Davenport on p−1 nonzero differences covers all of F_p, so T(z) would be attained. Hence μ≥2p−2.

**Consequences of μ≥2p−2.**
- The heavy value is unique, since 4p−4>R.
- The unsigned classes coincide across all Φ≥4 patterns.
- The class is not {0}: otherwise 2p−2 zero letters would satisfy a Φ2, T=0 pattern exactly.

**Φ2 is correctly left open.** It needs p−1 fillers but only p−2 exist, and the proof rightly treats this as a failure of the argument, not a no-go theorem.

### 3.4 HIGH-K-RES

**(R0).** κ̂≤p−1. κ̂≥1 holds by P. κ̂≠1 holds by HK1, which rests on S(p); together these give κ̂≥2. The band p+2≤k≤p+2κ̂ also holds.

**(R1).** Theorem P, applied with the gap-length reading.

**(R2).** The exact GRX criterion.

**(R3).** CT on its exact domain.

**Reviewer observation (no credit; supports M-6).** Take any datum with the (R0) shape that satisfies (R2). Read as a cyclic word, it is a length-(4p−2) avoider whose maximal cyclic constant blocks are exactly its k odd blocks, so it is its own admissible

NF. Hence (R0) together with (R2) is already exact. (R1), (R3), CT-top, the near-pair structure and the existential-NF antecedent are all implied consequences of it (the antecedent is met by taking w := u).

## 4. Findings and literal fixes

The source files are immutable. Each fix below is therefore to be applied by a new numbered worker erratum or a parent metadata correction.

### 4.1 Mathematical findings

All are MINOR. None changes a formula, case or conclusion.

**M-2 (required): proof LF77, wording of the index-order scope.**
- Old: `Cyclic cuts conjugate products and preserve identity in the original index order.`
- New: `Cyclic cuts of u conjugate products and preserve the existence of an identity 2p-subword in u's own index order; every identity selection below is built in u and contradicts u's avoidance, with nothing transferred back to w.`

**M-3 (required): after proof LF107 `summing W<=2p-1.`, insert the following.**
`Since g and every term are odd and parity is a homomorphism Z/2p->Z/2, every coefficient a with a·g equal to a term is odd; hence each least positive coefficient is odd and every larger coefficient is >=3 (used at LF111, LF112, LF119). For a bipartition Y=Y_+ ⊔ Y_-, a signed zero-sum is a selection whose Y_+ values minus Y_- values sum to 0 in F_p.`

**M-4 (required): proof LF138, HK1 is defined for p≥7 only.**
- Old: `This proves HK1 for all primes p>=5 at the declared S(p) trust.`
- New: `This proves HK1 (every prime p>=7) and the separate p=5 kappa_hat1 statement, both relative to S(p) at the declared secondary-statement trust, which enters only the zero-sum-free branch outside (X).`

**M-5 (required): trust label at proof LF26 and LF192.**
- At LF26, after `with 2<=kappa_hat<=p-1,` insert: `relative to S(p) at secondary-statement trust through HK1's zero-sum-free branch (without S(p), k=p+2, kappa_hat1 NFs with zero-sum-free Y would rejoin the residual),`
- At LF192:
  - Old: `accepted CT and HK1.`
  - New: `accepted CT and HK1 (hence S(p) secondary-statement trust for kappa_hat>=2).`

**M-1 (optional): proof LF66, the stated reason is a non sequitur.**
- Old: `Since |Y|=p is odd, either`
- New: `Since every nonempty zero-sum of odd terms has even length and all even lengths 4..p=R are excluded, either`

**M-6 (optional): proof LF195.**
- Old: `other necessary consequences may further shrink the data.`
- New: `other necessary consequences, including (R1), (R3) and Sec.5, are implied by (R0)+(R2) and serve only as derived tests; they cannot remove a datum satisfying (R0)+(R2).`

**M-7 (optional, editorial): notation clashes.**
- At LF150, rename the dummy index `a` to `x`. It clashes with the class {a,−a} at LF166.
- At LF188-189, rename `q` to `n_CT`. It clashes with Lemma M's q at LF155-159.

### 4.2 Source findings

**S-1 (MINOR, required; escalates under the condition in fix (a)).**

*Evidence.* Three places overstate what the packet binds for Theorem P:
- The coverage entry for the terminal-κ0 corollary says "accepting record are directly supplied".
- The coverage entry for the runs verdict says "P is supplied as its own accepted statement/admission".
- Proof LF219 says "Governing literal verdicts, mandatory overlays and actual used primary text are supplied".

What the packet actually binds is TP LF8-28, plus three path-free acceptance citations: K0R LF7, v8 LF7 and the worker's cp-02 LF40-41.

*Fix, either (a) or (b).*
- **(a)** Bind the parent record that accepts proof-theoremP.md (58a85ebe…), together with TP LF1-7. If that record carries any overlay, scope restriction or trust qualification, the result is **RE-REVIEW_REQUIRED for both families**. Theorem P is used at proof LF54-59, LF62-65, LF122-128 and in (R1).
- **(b)** Correct both coverage entries to read:
  `Theorem P's literal setting and statement (proof-theoremP.md LF8-28) are supplied; its accepted status is evidenced in-packet only by K0*/RED parent verdict LF7 ("Imports: Theorem P (accepted)", no path/hash), frontier-v8 LF7 and worker cp-02 LF40-41; its own acceptance record and TP LF1-7 are not bound.`
  
  Also, by new worker erratum, read proof LF219-220 `...actual used primary text are supplied` as:
  `...supplied, except Theorem P's own acceptance record; its accepted status is taken from K0*/RED verdict LF7.`

**S-2 (MINOR, optional, documentary).** The coverage field `outside_used_statement_reason` reads "non-premise; accepted-statement import, not transitive proof replay". It is attached to whole-pasted files that are not imports: the candidate proof, E1, the acknowledgements, scope/addenda and checkpoints. For every entry whose `not_pasted_ranges` list is empty, replace it with `n/a (whole file pasted)`.

### 4.3 Process findings

**P-0: retained records.** These remain permanent and uncured. This review does not reclassify any of them.
- UPAR4 arithmetic-before-scope PROCESS MAJOR (ack1 LF59-64).
- Pre-ack1 "equivalently" logical check, PROCESS MINOR (cp-01 LF9).
- Pre-ack2 algebraic planning, PROCESS MINOR (cp-02 LF9-14).
- Parent clerical path/deadline defect (addendum-1 LF6, LF11).
- Parent lower-terminal/equivalence/composition documentary MAJOR (ack2 LF27-30, LF42-43; addendum-2 LF13).

**P-1: observation for the parent (not asserted as a departure).**
- The proof file has no /bin/date clock line. Every sibling file has one (ack1 LF3, ack2 LF3, cp-01 LF3, cp-02 LF3, E1 LF3).
- The last supplied checkpoint is cp-02 at 14:23:16. E1 is stamped 15:00:42, which is 2246 s later.
- So compliance with the ≤1800 s substantive-checkpoint rule, and with "before long subcases" (ack1 LF88; ack2 LF96), cannot be verified across §§2-6 from this packet.
- The parent should check its own records for any cp-03 or later and for the proof's creation time, and classify only if a breach is found.

**P-2: no departure.** cp-02's 1295 s gap exceeds the 1200 s target but not the 1800 s hard limit, and cp-02 LF3-5 discloses it.

**Credit/exposure note (not a finding).** The §4 bipartition lemma, including its unique exception g^(p−1)(pg), parallels accepted FB-p (KPS item 2: "exceptional complement g^(p-1)(pg)"). The worker read FB-p as exposure. The inline proof is complete, so FB-p is not load-bearing. This reinforces the existing disclaimer of independence and novelty at LF213-214.

## 5. Retained trust boundaries

### 5.1 HK1 (p≥7, every k≥p+2, κ̂=1)

Imports used:
- **NF:** ROT-few-E v4 LF28-43, via fewodd addendum-1 LF12; ZX overlays 1-3; LO item 2, M1 and M4.
- **GRX:** LO item 1 with M1/M2.
- **Theorem P:** statement at TP LF25-28; accepted status as evidenced by K0R LF7 (see S-1).
- **S(p):** at secondary-statement trust (KPS item 1; Sp and Sp-E1, including the M-3 trust items; the Xia–Yuan primary text is unread).
  - It is used **only** in the zero-sum-free branch outside (X).
  - §3, COLOR, padding and (X) do not use it.

Not used: Lev, CT, VAC (P alone gives κ̂≥1 when k≥p+2), ROT-LS/ROT-P, UMR/UPAR lifts, windows or frames, FB-p/ARC0, and any computation or finite control.

New credit:
- Only the cell k=p+2, κ̂=1 is new.
- k≥p+3 at κ̂=1 is old P coverage.
- κ̂=0 is old VAC/P coverage. No duplicate credit.

### 5.2 The p=5, κ̂=1 statement

It rests on the same imports, at p=5:
- NF, whose scope is p≥5.
- GRX.
- Theorem P, at K0\*'s p≥5 scope.
- S(5), at Sp-E1 M-1/M-2 and KPS item 1 trust.

It covers this NF family only. There is no p=5 theorem and no computer-assisted lift, and Sp §6's finite controls are not premises.

### 5.3 §5 top family

It rests on:
- NF and GRX.
- CT (STAB item 6), with its transitive RS(a) dependency not replayed.
- Lemma M (re-proved inline) and classical Cauchy-Davenport.

It uses no S(p) and no Lev, and it establishes necessary structure only.

### 5.4 HIGH-K-RES

It holds relative to NF, GRX, Theorem P, CT and HK1; through HK1, the bound κ̂≥2 carries S(p) at secondary-statement trust. It is exact as a description (§3.4 observation). No member is asserted either to exist or not to exist.

## 6. Not established

- HIGH-K-CORE-COVER at any κ̂≥2, including the top family. That is, no full terminal k≥p+2 exclusion.
- Φ2 behaviour at the top family, and any rotation-pair or reflection rigidity.
- Any every-avoider or full ordered-Olson statement for D_(2p).
- Any NF exclusion at terminal k≤p.
- Any o_F equivalence or "only remaining gap" composition; the class of original o_F>p with terminal k≤p stays open.
- Any p=5 result beyond the κ̂=1 NF family.
- Novelty, priority, independent discovery or corroboration, and any formal/Lean, human-referee or runtime certification.
