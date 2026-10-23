# DELTA2-PAIR-COVER: hostile written review (single family; pasted text and hand reasoning only)

**Verdict:** ACCEPT-WITH-FIXES as a candidate.
**Counts:** FATAL 0 / MAJOR 0 / MINOR 6.
- LOW: 0 findings.
- ARC: 5 findings (2 mathematical wording, 1 source citation, 1 process, 1 cosmetic).
- Coverage metadata: 1 finding.

**Basis and limits:**
- I used no tool, code, enumeration, solver, Lean, network or delegation.
- The parent hand check was not supplied and is not used as a premise.
- Only part1v1 and part2v2, plus the manifest, coverage and handoff metadata, were read. The superseded part2v1 was not used.

## 1. LOW (`proof-DELTA2-LOW-v1.md`): every step PASS, no errata

| Step (LF) | Hand check | Verdict |
|---|---|---|
| §1 (40-50) | κ=2 gives H=p−3 and k=3p−4−2H=p+2=R. Z0 gives B≤2. Theorem P applies (N=4p−2≤4p−1), so Σ⌊r_i/2⌋≤2. R=k gives e=Σ_nonempty(r_i−1)≥v, and v≤2. | PASS |
| §2 window (54-59) | m∈[3,(p−1)/2] is nonempty iff p≥7, and 2m≤p−1<k. For every E∈[0,p+2]: E+m−3≥E, and p−m≥(p+1)/2=⌊R/2⌋. So γ_m(E)=⌊E/2⌋. | PASS |
| Even CRT lift (61-72) | e0(t)=(p+1)t mod 2p is the unique even class with e0(t)≡t (mod p); it is additive and injective. ψ(P)=e0(2u_P)−E(P) and Σα_i=−D. Both directions of "W holds ⇔ ψ(P) has a representative in [−R,0]" re-derived: with t=s+E even, t/2∈[−⌊(R−E)/2⌋,⌊E/2⌋]. The complement of [−(p+2),0] modulo 2p is exactly [1,p−3], since (p+3)+(p−3)=2p. | PASS |
| §3 increments (76-85) | Each edge increment lies in [−(p−4),p−4], an interval of 2p−7<2p integers, so h_i is unique. It is independent of the edge and of the layer. On each layer, N=c_m+Σ_P h_i. P and P^c lie on the same layer, so c_m cancels and no cross-layer comparison is needed. (6) and (7) hold. CONNECT applies because 1≤m and 2m<k. | PASS |
| Counts (87-98) | h_i≡d_i≡r_i (mod 2). For an empty run, θ_i≠0 and e0 is injective, so h_i is nonzero even. Zero labels occur only in nonempty even runs, so e≥v≥z and z≤2. Pointwise w_i≥1+1_E0−1_Z0, plus 1 extra for each of the v−z nonzero even runs, gives S≥k+e+v−2z≥k. S≡D≡R is odd. If S=k, then e=v=z; odd runs have r=1 and \|h\|=1; even runs have r=2 and h=0; empty runs have \|h\|=2; every weight is ≤2. This structure is derived, not assumed. | PASS |
| §4 case A | S≥p+2>p−4. | PASS |
| §4 case B | k is odd, so 2m0≤k−1 and m0=U+1, with 2m0=p+1≥8. Flipping the lightest stretch removes exactly 2 boundaries. The new sum is ≥(p+2)(p−1)/(p+1)=p−2/(p+1)>p−4. | PASS |
| §4 case C | n≥k−4m0 gives 9>4, 5>2 and (p=7) 5>4, so γ<1. Flipping interior vertices only adds exactly 2f boundaries. Lower bound: ≥p−4+2m0−z+(1−γ)e. Strictness holds in all three subcases, including m0=1 with z=2 via e≥z. | PASS |
| §4 case D (p=7, m0=2) | 4 stretches on 9 vertices force one of length ≥3, hence an interior vertex. If S≥11, w≤3 gives ≥5>3. If S=9, w≤2 gives ≥5>3. LIGHT is not used with n=1. | PASS |
| §4 case E | LIGHT with f=3 on the k-cycle (k≥9). S(p−4)/(p+2)>p−4 iff S>k. | PASS |
| §5 congruence (146-153) | Using ±(p+2)+(p+2−2B) with B∈{0,1,2} and 2p≥14: positive sum ⇔ B=2, negative sum ⇔ B=0, and B=1 is impossible. A≥p and at most 2v≤4 letters sit in even runs, so at least p−4 letters sit in positive singletons. | PASS |
| B2 test (m=1) | θ_i≡2, u=1, E+=3. γ_1(3)=1 and γ_1(p−1)=(p−1)/2, so 1 lies in the W interval. | PASS |
| B0 test (m=2) | u_j=−1 and the singletons have u=0. There are ≥5 singletons, so a non-adjacent i exists. E+=1, γ_2(1)=0, γ_2(p+1)=(p+1)/2, so −1∈[−(p+1)/2,0]. If e=0, all θ_i=0, so all 3p−4≥2p reflections are the same σ_y and σ_y^{2p}=1. | PASS |

**Hostile orientation check.** The B0 test depends on which side of the interval uses E+. With the reversed interval [0,(p+1)/2], the value −1 would be missed.
- I re-derived the orientation from the pasted GRX and GR0/H0 under lowodd M2 (LF 30): z_1=+1, (v,e)(v',e')=(v+ev',ee').
- That derivation gives V=σ−T(z) and T(z_P)=2u_P, with t≤A+≤E+(P)=A_P+B_{P^c}.
- So the upper endpoint is γ(E+(P)), as printed in v5 LF 43 and as used in LOW §2 and §5.
- The P↔P^c symmetry is consistent, and the signs of α, h and (7) agree with this orientation.

## 2. ARC (`proof-DELTA2-arc-cover-v1.md`)

| Lemma | Hand check | Verdict |
|---|---|---|
| §1 (D1),(D2) | P0 with e_F=0 gives o_R≥k−2κ=p−2, so x∈[0,4] and d≤x+1. T≡R is odd for every labelling; after BAL, odd \|T\|≤d forces \|T\|≤2t+1. c=(k−o)/2 with o odd and o≤q (or q−1) gives c≥p−3−H+⌈x/2⌉. | PASS (ERR-2) |
| (W2), GW2 | γ=min(s,E+H−s,⌊E/2⌋). The two values of a pair differ because its internal empty run is genuine. CD gives at least min(p,G+1) residues; the interval has Γ+1. The pigeonhole step does not depend on orientation. | PASS |
| (F_t), T1 window | For \|T\|=2j+1, E∈{h+1+j, h−j} and the floor-halves sum to h. Checking the extreme E values suffices. β_t−α_t=H−t verified for h even and odd, t=0,1,2. The T1 window [L_H,U_H] corresponds to s∈[α_0,β_0]. | PASS |
| Short segments (3/4/5 blocks) | Any edge subset is a union of ≤⌊L/2⌋ maximal intervals, with distinct endpoints a_s<b_s+1<a_{s+1}. Alternating roles give a fixed sign ±½Σδ. CD on {0,δ_i} gives ≥L residues. Even insertion preserves c_i parity, z, T, E± and the outer gap roles; internal runs have d=0. Segments act independently. The m-rise is ≤⌊L/2⌋. Total is (Π+1)+(h+1)=p+1. ARC+ is not used. | PASS |
| Flexible BAL | Needs G0+2m0≤k and k−2G0>0. A singleton move at the free index costs no pair. The partner move follows e5/I.7. Δ∈{−2,0,2}, and a pair is lost only through a split, which forces Δ≥0. | PASS (ERR-2) |
| Fixed-count | Removing the first two blocks of M_l lowers capacity by exactly 1. Block count G0+2m0+1≤k. Compensation keeps exactly 2m0 arcs. At most one pair is lost. BAL guarantees i'≠i. | PASS |
| §4 free-bit injection | Bits at non-rigid edges are determined by z. G+ξ is even. A pattern fixes z up to global sign. "At most one" holds only for signed T=+1. | FIX (ERR-1) |
| Sign-fill, J∈{2,3,4} | Rigid edges form a forest of paths (r<q). Each component has magnitude ≤r+1+x≤J+1. Greedy orientation gives 0≤F≤J+1. n≥p+2−2J>J and \|1−F\|≤J. Parity: n≡1−F because R is odd. So there are ≥n≥2 labellings. For J=2, p≥11, the binomial index lies in [3,n−3], giving ≥C(p−2,3). | PASS |
| One-rigid count, C1, C2 | Equal and opposite cases each give C(p,(p−1)/2). C(p,3)−C(p+1,2)=p((p−3)²−10)/6≥p. For C2: n²−7n−6=(n−9)(n+2)+12, C(n,3)≥(7/3)C(n,2), and C(n,2)/3≥12. | PASS |
| MP (κ=h) | c≥Π+1 at p≥11: width h−2−t≥2, 2s0≥h, 2m0−G0=3h−1−2s0≥2h−6, k−2G0=2h−1. p=7, t=0: F_0=[2,4]. c=Π: x=0 and all M_i odd, so BAL costs no pair (3h−2s0≤2h+1). p=7, t=1: s'=5 only after two deletions; Γ pairs (2,1),(3,0) recomputed. p=7, t=2: c≥4, F_2={3}. | PASS |
| MM (κ=h−1) | c≥Π+1 with 2s0≥h+2. p=7, t=2: (2,2),(3,1),(3,0). c=Π: r=2−x, J=2, window 2−ε≤ξ≤2h−ε, only ξ=0 bad. c=Π−1: x=0, one rigid edge, f=2h, need 4−ε≤ξ; bad patterns ≤1+C(p+1,2)<C1. Base ≥4 arcs; G+2=Π. | PASS |
| END (κ=h−2, p≥11) | c≥Π+1: s0=α_t+2, width h−t≥4. c=Π: r=4−x, J=4 (needs p>10). c=Π−1: odd case J=3 with 2−ε≤ξ; even case ξ≡1−ε with 3−ε≤ξ, bad ≤p<C(p−2,3). c=Π−2: 5-block or two 3-block segments, r'∈{1,2}; bad ≤1+C(p+1,2)<C2; G+4=Π. | PASS |
| TOP4 (H=0..3) | All window minima recomputed for h=2a+1 (a≥3) and h=2a+2 (a≥1); every γ≥0, including p=7 pairs (2,0),(3,0). Capacity c≥2h−4−H+⌈x/2⌉ fails G0+1 only at (p=7,H=1,x=0,c=3) and (p=11,H=3,x=0,c=5). Budgets 5−h, 6−h, 7−h, 7−h, 8−h, 2H−h+5 all hold. 2m0−G0≥2h−6≥2. Γ_min+G0−1=p−1 in every row. Exceptions: p=7, s'=4 gives (2,1); p=11 gives 6+5≥10. | PASS |
| §9 union | Pieces are consecutive. p=11 and p=13 substituted by hand. At p=7, κ∈{3,4,5,6} is covered by MM, MP and TOP4. κ=2 comes from LOW, which is independent of ARC, so there is no circularity. RP-2NE at δ=2 is [3,(p−5)/2]; I.14 K2P+ at δ=2 is [(p+3)/2,p−5]; both are any-B accepted statements in setting (S). The Bprime/CJ prior-credit boundaries are stated correctly. | PASS |

## 3. Minimal new errata (frozen files unchanged)

- **ERR-1** (ARC LF 129, 141, 145-148, 190-251; MINOR). In §§4–7, "T1 labelling" means signed T=+1 (its arc system has \|T\|=1). In §2 (LF 85-87), "T1" means \|T\|=1. Every lower count already constructs T=+1, and the counts survive either consistent reading.
- **ERR-2** (ARC LF 58-59, 107-108; MINOR). Read "BAL gives \|T\|≤d" as "after the BAL parity change, or if \|T\|≤d already". In the flexible construction, take BAL's i to be the index of the M_i that has a non-pair block.
- **ERR-3** (ARC LF 31-33; MINOR, source). The erratum-5 ranges actually used are LF 1-33, 59-78 (I.4–I.7) and 146-158 (I.14). e5 LF 32-33 states that no other Part I item changes a used statement. "1-164 / all PartI" is a governing pointer, not a pasted or used range.
- **ERR-4** (ARC LF 3; MINOR, process). "Drafted after 20:20:50" contradicts cp04 LF 4-6 (Sections 0–6 drafted by 20:15:04) and cp05 LF 17-18 (header inserted before creation). Read it as "clock observed before exclusive creation; drafting began earlier".
- **ERR-5** (coverage LF 666-850 and handoff LF 122-124; MINOR, metadata). "All other … NOT-PASTED objects are named" overclaims. These pointers inside pasted text are unnamed:
  - `proof-dihedral-partial.md` (GRX LF 9; K0star LF 70-71)
  - `proof-GR0-r1` Lemma AR (K0star LF 66)
  - RED / SMALLK / FEW (v5 LF 22-26)
  - `proof-DR.md` (K0star LF 26)
  - reflection README (RP-LIFT binding 1)

  None is load-bearing (see §4).
- **ERR-6** (ARC LF 89-102 vs 217, and LF 139-141; cosmetic). The symbols L, U and F are overloaded. Rename the window to [L_E,U_E] and the component sum to F_c.

## 4. Source gate: PASS. Load-bearing missing bodies: NONE.

**Used closure, complete in the pasted pair:**
- W (v5 LF 42-44) ← H0 (K0star LF 55-65) ← GR0 (LF 40-54) ← GRX (complete) plus M1/M2 (LF 27-30).
- L2.1, L3.1, BAL with I.6, e5 with I.4/I.7.
- Full CONNECT and LIGHT, with overlay and bindings.
- P0, full Theorem P with its own verdict and both errata.
- Z0 via I(empty); Cauchy-Davenport (classical).
- Baseline: RP-2NE verdict LF 8-10; v5 verdict LF 40; I.14 LF 155-156; m6.

**Unpasted bodies cited inside the used chain, and why they are not load-bearing:**
- GR0 cites the Ach computation in `proof-GR.md` §2. I re-derived Ach exactly from GRX by hand (σ=A+−A−, A±≤E±, C even in [Φ,C_max]).
- GRX takes its group convention from `proof-dihedral-partial.md`. The convention is supplied explicitly in lowodd LF 7/30 and K0star LF 14.
- (V), Lemma AR (only needed for R=0), RED, SMALLK, FEW and RGR are not used.

**Declared omissions, and why they are not load-bearing:**
- Audit LF 94-116.
- e5 LF 34-58, 79-145 and 159-198.
- The rest of v5.
- lowodd LF 11-26 and 31-43.
- EDGE. The Step0 R-values claim is also supported by CJ LF 41, and Step0 is not a premise.
- The RP2NE, SEG-k, TRANSFER, B and B′ bodies.
- The DELTA1 locators.

Since no omitted body is load-bearing, no both-family re-review is triggered.

## 5. Import trust and nonclaims

**Checked by hand here:**
- Every LOW and ARC step.
- The proofs of CONNECT, LIGHT, L2.1, L3.1, BAL/I.6 and e5/I.7.
- The full W-orientation chain, including Ach.

**Spot-checked only:**
- Theorem P's degree budget (deg Q≤3(p−1)<M).

**Accepted statements, not replayed:**
- RP-2NE.
- The I.14 K2P+ band.
- K0*/H0/GR0 acceptance.
- Theorem P acceptance.
- Cauchy-Davenport.

**Confirmed unused by either proof:** CJ, TRANSFER, EDGE, SEG-k, B/B′, Part II, S(p), Lev, CT, HK1, HIGH-CORE, any DELTA1 lemma, RP-LIFT FWIN/ILIFT/SIGN, and RP2NE SIGN-2Z.

**Nonclaims:**
- This is a single-family written check. It is not acceptance and not a both-family gate.
- No formal, kernel, Lean, human, novelty, priority or runtime claim.
- Hashes, byte/LF counts and clocks were not forensically verified. Only their internal arithmetic was checked:
  - 14+31=45 blocks from 38 distinct files.
  - 99404+99872=199276 B and 1264+965=2229 LF.
  - part2 v2−v1 = 826 B / 8 LF.
  - Clock gaps 605 / 1674 / 620 / 349 / 366 / 577 / 326 / 684 s.
- Scope is exactly the δ2 class. Nothing is claimed for other R, arbitrary words, REFL, INV*, full ordered Olson or p=5.

## 6. Permanent history (retained, not cured)

- **Cadence miss:** the cp01→cp02 gap is 1674 s, which is 474 s over the 1200 s target and below the 1800 s ceiling. The 19:44:29 clock is not a checkpoint.
- **Pre-gate M2 correction:** part2v1 (99046 B / 957 LF) was superseded before any gate by part2v2, which adds lowodd LF 27-30. part2v1 is not a third operative part.
- **Earlier qualifications:** UPAR4, enumeration, scope, reportv11, context, cadence, pre-ack, metadata, source-history and the withdrawn DELTA1 x0 allegation all remain.
- **New addition:** ERR-4.
- No chronology is certified.
