# Hostile written review: K3 package v1 (PKG `652cb66b…`, PRF `35ea47b0…`)

This review uses only the pasted text. No tools, files, computation or enumeration were used. Hashes, ranges and timestamps were not re-checked; the parent owns those.

Source keys: **PRF** = proof-K3-v1.md, **PKG** = review-package-K3-v1.md, **PL** = proof-LOWER-v1.md, **ERR** = LOWER parent erratum, **CJ** = cj-cjx verdict, **FB** = proof-FB-v1.md, **ZX** = zx-s1c verdict, **GRX** = notes-GRX-v1.md.

## Counts

**FATAL 0 · MAJOR 0 · MINOR 3**

I found no mathematical flaw in any load-bearing step.

- **Theorem K3** (every prime p ≥ 13) is correct relative to the accepted inputs at their literal scopes.
- **Theorem K3-11** (p = 11) is correct as a conditional on (H11), evaluated in a fixed admissible frame.
- The frozen target (every p ≥ 11) is **not closed**. The outcome remains a labelled partial.

## Claim-wise verdicts

| Claim | Source | Verdict |
|---|---|---|
| Frame at κ=3 (windows, t-labels, W, #1, \|b\|, u+) | PRF LF25–53 | Correct, re-derived (§A) |
| Lemma N3 (all p ≥ 11, no (H11) needed) | PRF LF57–71 | Correct (§B) |
| Lemma FULL (a) p≥13, (b)–(d) p=11 | PRF LF75–90 | Correct; (a) is tight at p=13 (§C) |
| FULL converse (single-signed ⇒ not full) | PRF LF175–176 | Correct, not load-bearing (MINOR-3) |
| Lemma F3 (F1)–(F5) under (ALL4) | PRF LF94–120 | Correct for N ≥ 12 (§D) |
| Lemma RIG3 under (ALL4) | PRF LF124–133 | Correct (§E) |
| Sec. 6 final cases ν0 = 0/1/2/3 | PRF LF137–168 | Correct; every selection is realizable and in-window (§F) |
| **Theorem K3** | PRF LF16; PKG LF15 | **CORRECT**, scoped partial (p ≥ 13) |
| **Theorem K3-11** | PRF LF17–18; PKG LF16–18 | **CORRECT as a per-frame conditional on (H11)**; MINOR-1 |
| Residual and routes R1–R4 | PRF LF172–186; PKG LF19 | Not claims. Description is consistent, R1–R4 arithmetic checks, and nothing is closed by them |
| Imports and scope | PRF LF188–203; PKG LF27–30, 46–49 | Consistent; MINOR-2 |

## Re-derivation record

### A. Frame (PRF LF25–53)

**Parameters.** κ=3 gives R=p+5, N=p+1, F=3p−7, H=p−4, and R+F=4p−2.

**Windows.** With all l_i odd, GRX (GRX LF14–19; PL LF47–50) gives Φ=2m, δ=N−2m and C_max=2m+2H. Hence n ∈ [8−2m, 2p−2m] ∩ [0, p+5].

| m | window | valid for |
|---|---|---|
| 0 | [8, p+5], target 0 | — |
| 1 | [6, p+5] | p ≥ 7 |
| 2 | [4, p+5] | p ≥ 9 |
| 3 | [2, p+5] | p ≥ 11; tight at p=11 (2p−6 = 16) |
| 4 | [0, min(p+5, 2p−8)] | equals [0, R] iff p ≥ 13 (tight at 13: 18 = 18); [0, 14] at p=11 |

At m=4, n=0 corresponds to C = 2p = C_max, which is admissible.

**Bound on Z.** Every zero-sum of Y has even length at most |Y| = p+5 < 2p. The m=1 window at P0 removes lengths 6,…,p+5, so |Z| = 2t ≤ 4 directly (see MINOR-2).

**Setting (S′)** (FB LF12–17), with k′=p−1 and κ′=2:
- 2p+2κ′−k′ = p+5 = |Y|.
- t ≤ 2 = κ′.
- L = p+5−2t ≥ p+1 = 2p−k′.

**ZSTRUCT + FB.** These give n₊+n₋ = 2t, n₋ ≥ 1, s_j odd and Σs_j = n₊. The surviving cases are:
- t=1: (1,1) with s=1.
- t=2: (2,2) with s=(1,1), or (3,1) with s=3.

The shapes (4,0), (1,3) and (0,4) are impossible. PRF LF36–37 is correct.

**Parity of W.** L is even, so W ≡ 0 (mod 2). This gives W ≤ 2p−2 for t=0,1, and W ≤ 2p−1−n₊ ≤ 2p−3, hence W ≤ 2p−4, for t=2.

**Counts of 1-labels.**

| t | m1 ≥ | #1 = m1 + n₊ ≥ |
|---|---|---|
| 0 | (p+17)/2 | (p+17)/2 |
| 1 | (p+11)/2 | (p+13)/2 |
| 2 | (p+7)/2 | (p+11)/2 |

So #1 ≥ (p+11)/2 in all cases.

**Label size.** a_max ≤ W−(L−1) = p−6, p−4, p−4 for t = 0, 1, 2. Hence |b| ≤ p−4.

**Light side.** By LT (PL LF102–104), o(P0) ≤ 3, so u+ ≥ (p+5)/2.

### B. Lemma N3 (PRF LF57–71)

**Location of large negative labels.** c = −B with B ≥ 5 forces l ∈ P0 with a-label B, because negative C0 labels are only −1 or −3.

**Part (a).** The excess of the other a-labels is at most p−6−B (t=0) or p−4−B (t=1,2). This gives:
- #1 ≥ (p+14+B)/2, (p+10+B)/2, (p+8+B)/2 for t = 0, 1, 2.
- Hence u+ ≥ (p+2+B)/2 ≥ B, using B ≤ p−4.
- So there is an integer zero-sum of size B+1 ∈ [8, p−3], which (SR) at P=∅ forbids.

**Part (b).** Assign weights 2, 4, 6 to labels −1, −3, −5.
- The sub-multisets of sum 8 are {2,6}, {4,4}, {2,2,4} and {2,2,2,2}.
- If x(A−) ≥ 8 and none of these occurs, then a 6 is present, no 2 is present, and at most one 4 is present. (Without a 6, the total is at most 6.)
- The forbidden zero-sum sizes are then:
  - 8, with w ≤ 7 ≤ u+;
  - 10, for {−5,−3}, with w = 8;
  - 12, for {−5,−5}. Here #1 ≥ (p+21)/2, (p+17)/2, (p+15)/2, so u+ ≥ (p+9)/2 ≥ 10.
- All three sizes lie in [8, p+5].
- At p=11 the {−5,−5} branch is vacuous, since W−L ≤ 6 < 8.

**Conclusions.** Seven sets survive, ν0 ≤ 5, and 2Π0+3+ν0 = 2B*+3−ν0 ≥ 2p+8.

### C. Lemma FULL (PRF LF75–90)

- **(a)** The window [0, R] contains every even |J|, and the claim follows from SS.
- **(b)** Take a minimal J; it has no zero sub-multiset.
  - If |J| ≥ 15, J contains at least u+−1 ≥ 7 letters with c=+1, all with one X^(Q)-sign ε.
  - Any letter of the opposite sign has |c| ≤ 7 and cancels against |c| of them.
  - So J is single-signed. Since |J| is even, |J| = 16, which forces X^(Q) to be single-signed, a contradiction.
- **(c)** Correct as stated.
- **(d)** Both (H11) disjuncts are covered, for both Q and Qᶜ:
  - A two-signed run must lie in Q (it has a c<0 letter) and outside Q (it has a c>0 letter), which is impossible.
  - Since m=4, Q has at least 4 runs, all without c>0 letters.
- **Converse** (PRF LF175–176). B* = W+2n₊ is even and at least 16. For a single-signed X^(Q), the value ±B* needs |J| = 16 > 14, so Q is not full. Fullness at p=11 is therefore exactly two-signedness.

### D. Lemma F3 (PRF LF94–120), N ≥ 12

**(F2) θ via full pairs.**
- Q_i and Q_i∪{i} both have m=4, using the margins N−6 ≥ 6 and N−7 ≥ 5.
- |d| ≤ 2p−2−B* ≤ p−7, and two increments at i agree mod 2p by CRT (p odd), so they are equal.
- θ_i is defined only through full pairs, as ERR LF6 requires.

**(F3) Connectivity.**
- Shrinking each interval turns any member into an independent quadruple.
- Advancing or retreating v_j moves one unit between g_j and g_{j−1} when the donor gap is at least 2.
- Routing one unit lowers Σ|g − target| by 2; intermediate gaps are at least 2 after receiving.
- The rotation advances v4, v3, v2, v1 in turn, passing through (2,2,3,N−11), (2,3,2,N−11), (3,2,2,N−11). This needs N−11 ≥ 1.

**(F4) f0 = 0.** P1∪P2 = {0,1,3,4,6,7,9,10}; 11 is excluded, so m=4. Lemma A applies with the N3 inequality.

**(F5) Total.** Q0ᶜ has intervals {1}, {3}, {5}, {7..N−1}, so m=4, and Lemma C applies.

### E. Lemma RIG3 (PRF LF124–133)

1. N is even, so S_ev and S_od are independent and |S| ≥ 6.
2. The top four of each set lie in F4, so their sum is at most −1−ν0. Hence θ_(4) ≤ −1.
3. Summing over both sets and using (F5): B*−2ν0−2p ≤ −2−2ν0−(p−7). So B* ≤ p+5 = R ≤ B*.
4. Equality must hold in each set. This gives θ_(j) = −1 for j ≥ 4, θ_(1)+θ_(2)+θ_(3) = −ν0, and Σ_S(θ+1) = 3−ν0.

### F. Sec. 6 (PRF LF137–168)

**(A) No empty runs.** This step needs ν0 ≥ 1. An empty run has θ_e even and θ_e ∈ [−1, 1], so θ_e = 0. Then τ_e ≡ 0, contradicting the empty-run rule. At ν0=0, θ_e = 2 is not excluded; that case goes to CJ''' instead, which is correct.

**(B) Unit runs.** Σ(r_i−1) = 4 gives at least p−3 singleton runs. Hence there are at least p−9+ν0 unit runs, each with τ = −2.

| Case | P | m / window | T(P) | −1's in X^(P) | Selection | n |
|---|---|---|---|---|---|---|
| ν0 ∈ {2,3} | two non-adjacent units | 2 / [4,p+5] | −4 | ν0+2 ≥ 4 | four −1 | 4 |
| ν0=1, θ_e=1, e ≠ {−1} | {e, unit} | 2 / [4,p+5] | −1−s_e | s_e+2 | all −1 plus one +1 (p+3−s_e ≥ p−2 available) | s_e+3 ∈ {4,6,8} |
| ν0=1, e = {−1} | {e, i, j} | 3 / [2,p+5] | −2 | exactly 2 | both −1 | 2 |
| ν0=1, four θ=0 runs | {e (both +1), unit} | 2 / [4,p+5] | −4 | 4 | four −1 | 4 |
| ν0=0 | CJ''' (CJ LF8, 13) | — | — | — | — | — |

Notes on the table:
- s_e is odd because s_e ≡ r_e ≡ θ_e (mod 2).
- Unit-run supply: p−7 (ν0 ≥ 2); p−8 with at most 2 adjacent to e (θ_e = 1); p−6 with at least p−8 ≥ 3 non-adjacent to e (e = {−1}); p−4 (four θ=0 runs).
- CJ''' literal scope is met: all rotations are one non-identity rotation, F ≥ 1, the S_i are maximal and odd (by the empty-run rule), empty runs are genuine, κ=3, R=p+5 ≥ 8, 2κ = 6 ≤ p−1, Δ = −3.

### Endpoints

| | p = 11 | p = 13 |
|---|---|---|
| N, R | 12, 16 | 14, 18 |
| m=4 window | [0,14] (cut) | [0,18] = [0,R] (tight) |
| u+ ≥ | 8 | 9 |
| N3(a): B, size | 7, 8 | 7/9, 8/10 (≤ p−3 = 10) |
| N3 {−5,−5} | vacuous | only t ≥ 1; u+ ≥ 11 |
| F3 target gap vector | (2,2,2,2) | (2,2,2,4) |
| \|S\| | 6 | 7 |
| unit runs at ν0 = 1/2/3 | 3/4/5 | 5/6/7 |

All steps hold at both endpoints, and uniformly for p ≥ 13.

## Findings

### MINOR-1: frame quantifier in K3-11 and the residual (statement precision; correctness unaffected)

**Where.** PRF LF17–19, LF172–174; PKG LF16–19.

**Issue.** The labels c_l, and therefore (H11), depend on the frame. Specifically:
- Given P0 and γ, each b_l is the unique odd integer in (−p, p) congruent to (X^(P0)-value)/γ. This holds because all labels lie in [−3, p−4], so Z does not matter.
- P0 (any T=0 arc) and the index-<1 generator g do matter. g is omitted from PKG's "(any admissible choice of the T=0 arc and light side)".
- The light side is forced. If both P0 and C0 were light, N3 applied in both orientations (c′ = −c) would give p+5 = R ≤ 6.

The proof fixes one frame throughout, so it proves the per-frame statement. PRF's "in the integer frame" leaves this quantifier implicit.

**Consequence.** The theorem is not overstated under any reading. However, the residual is exactly the set of (avoider, qualifying NF, admissible frame) triples where ¬(H11) holds. A consumer who reads "the frame" as canonical could misdelimit what remains open.

**Repair.**
- K3-11: "no avoider has a qualifying NF together with an admissible frame (P0, longest Z, index-<1 g) in which (H11) holds."
- Residual: "(H11) fails in the chosen frame."

### MINOR-2: import-list hygiene (non-load-bearing)

**Where.** PRF LF33; PKG LF29; PRF LF201.

**Issue.**
- **(i)** S1(a) at κ′=2 is cited for |Z| ≤ 4, but the bound is immediate from (SR) at m=1 and |Y| < 2p. The pasted ZX LF19 does not show the sequence S1(a) applies to. The adjacent ZX LF18 carries 3k ≤ 2p+1, which k′ = p−1 violates. The citation is avoidable scope exposure.
- **(ii)** PKG's input list omits the Setting fact, which is inherited via PL LF78 and LF89; PRF LF201 does list it. It is dispensable at κ=3: s_j ≤ 3 ≤ m1+1 because m1 ≥ (p+7)/2, and K3 derives its m1 and #1 bounds from W parity alone.

**Consequence.** None for either theorem.

**Repair.** Replace the S1(a) citation with the one-line direct argument (as the K2 verdict did at κ=2). Either list the Setting fact or mark it as unneeded at κ=3.

### MINOR-3: placement of the FULL converse (wording)

**Where.** PKG LF21, PRF LF75–77, PRF LF175–176.

**Issue.** PKG LF21 says fullness at p=11 holds for "exactly the two-signed ones". Lemma FULL as stated (PRF LF75–77) proves only the "if" direction. The converse appears only in the not-claimed Sec. 7 (LF175–176). It is correct (see §C) and not used.

**Repair.** Add the converse as FULL(e), or drop "exactly" from PKG LF21.

## Errata and scopes applied

- **ERR LF7 (m(P) convention):** m(∅) = 0 gives the [8, p+5] window, and F4 members are proper sets.
- **ERR LF6 (θ only via full pairs):** satisfied by the (Q_i, Q_i∪{i}) construction.
- **ERR LF5 (CR), LF8, LF9:** these are not used.
- **CJ''':** both R ≥ 4κ−4 and 2κ ≤ p−1 are retained, and it is used only for the ν0=0 all-equal case.
- **K2:** not a premise. N3, FULL, F3 and RIG3 rest only on the PL interfaces. Theorem P, CR and FB-E are unused.

## Correctness vs completeness, process, priority, computation

- **Correctness.** K3 is correct relative to the accepted imports: NF, GRX if-direction, SC0, ZSTRUCT/FB in (S′), CJ''' and the PL interfaces. K3-11 is correct conditional on (H11), per frame. No load-bearing dependency is unresolved.
- **Completeness.** The frozen target is not closed. p=11 without (H11) remains open, and this review does not infer that (H11) holds or fails generically. R1–R4 are route remarks, not results. Not settled here: the whole p=11 cell, other cells, reflection rigidity, INV*, o_F assembly, and full ordered Olson.
- **Process.** Pins, timestamps and throttle compliance were not checked by this review. All three MINORs are erratum-level and need no re-review.
- **Priority.** No novelty or priority claim is made or endorsed. I read the "[NEW]" tags as "derived in this packet, not imported".
- **Computation.** None was used by the candidate or by this review. This is a hand check of written mathematics, not an executable or formal verification. No approval of the research target or runtime is given.
