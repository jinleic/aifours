<!-- Parent capture 2026-10-18T00:28:53-07:00; unreviewed scout derivations, no execution. -->

## Summary

**Verdict.** No published theorem I could access says that a bare H(5,g,4,3), inflated by zero-sum TD(3,4,3), has a Kirkman frame at every point. The screen did find two short arguments that need no search. They give theorem-level progress under §4(4) and new infinite families, all built from objects the lanes already have. Neither argument has been executed or reviewed yet.

1. **Zero-sum tripling lemma (proof written in this screen, not executed).** Every 3-regular 3-partite 3-graph has a zero-sum 3-blow-up that splits into 9 perfect matchings. Consequence: **every** 3-GDD of type 6⁴ triples to a KF(18⁴), so **every** H(5,6,4,3) gives an FDGDD(3,4,5{18}) with frames written down explicitly. This holds because g/2 = 3. When g ≡ 0 (mod 4), a parity obstruction can block every odd-weight inflation.
2. **Fan widening (bridge only).** Construction 2.3 accepts any 1-FG, not just fans from RDS designs. Deleting a point from Denniston's S(3,5,26) gives one. With the existing seeds this yields **mcDSQS(450·4ʲ+2)** and **mcDSQS(800·4ʲ)** for all j ≥ 0, plus a separate lead **RDSQS(200·4ʲ+2) → LKTS(600·4ʲ+3)** whose priority is unchecked.

**Pick: T1** (below). It is cheap and theorem-level, and it closes Q1. If the parent wants a new slot target after T1 that yields new mcDSQS orders and is more than seeding existing constructions, nothing qualifies: T2 is compute-seeded and T3 gives no mcDSQS orders. In that case, screen another book family. A general mcDSQS product construction is **NOT-JUSTIFIED**: there is no concrete mechanism, and the Yuan–Kang product proof is unread.

## Q1. Known theorem? Definitions, and what the new lemma adds

**Five notions that must not be conflated.**

| Notion | What it requires | Source |
|---|---|---|
| FDH / FDGDD | The *derived* design at every point is a Kirkman frame | CZZ abstract; TZ LF246–247 |
| RDH / RDGDD | The *derived* design at every point is fully resolvable | TZ LF243–245; Liu–Lei §2 |
| RH (block-resolved H) | The 4-*blocks* themselves split into parallel classes | Zhang–Ge 2010 |
| H-frames | Block-level holey classes (a keyword in Zhang–Ge 2010; definition text unread) | Zhang–Ge 2010 |
| 3-frames F(3,4,n{2}) | Group size 2 only (definition unread) | Teirlinck 1994; Muse–Phelps 2003 |

- CZZ abstract: "A frame-derived H-design FDH(v, g, 4, 3) is an H(v, g, 4, 3) whose derived design at every point forms a Kirkman frame." It also says "direct constructions for FDH(v, 2, 4, 3)s are displayed by using automorphism groups." (https://link.springer.com/article/10.1007/s10623-018-0536-8, online 2018-08-21)
- Zhang–Ge 2010: "When α = 1, a (1, α)-resolvable H-design of type gⁿ is simply called a resolvable H-design and denoted by RH(gⁿ)" (https://link.springer.com/article/10.1007/s10623-009-9363-2, 2010-01-26).
- Muse–Phelps, zbMATH summary: "Orthogonal quadruple systems with an additional nesting property are shown to provide a new construction of 3-frames F(3,4,n{2})" (https://zbmath.org/?q=Orthogonal+quadruple+systems+and+3-frames).
- Necessary conditions at v = 5 (my counting): FDH needs g even; RDH needs 6 | g; RH needs 4 | g.

**Nearest prior results. None of them is the theorem asked about.**
- Natural weighting needs a master that is already frame-derived (lane Lemma W; RDTD-per-block, as in TZ Construction 2.4).
- Liu–Lei 2023 is a precedent for the *method*: inflate a master that is not resolvably derived, then find resolutions by computer. "For every block A … there exists a TD(3, 4, 3) on A × Z₃ … We can check that the derived design of the GDD at every point is resolvable" (arXiv:2210.06214v2, 2023-02-12). That covers RDGDD type 3⁸ from SQS(8) and type 3¹⁴ from SQS(14), with no general lemma.
- The CZZ body and Chang–Zhou 2013 are unread.

**Screen-derived results. Not executed, not reviewed.**
- **Decoupling lemma.** In a 3-GDD of type g⁴, a point y ∈ G_a has n_b, n_c, n_d triples missing groups G_b, G_c, G_d. Pair counts give n_c+n_d = n_b+n_d = n_b+n_c = g, so each is g/2. Hence a KF(g⁴) on that GDD is the same thing as a 1-factorization of each of its four missing-group families. Each family is (g/2)-regular, linear and 3-partite. Inflation acts on each family separately.
- **Tripling lemma (r = 3).**
  - Take a proper 3-edge-colouring u: incidences → Z₃ of the 3-regular incidence graph (König). Then Σ_{v∈T} u(v,T) = 0+1+2 = 0 for every edge T.
  - Give the lift ((a,x),(b,y),(c,z)) of T = (a,b,c), with x+y+z = s, the label (x+u(a,T), y+u(b,T)) ∈ Z₃².
  - At a point (a,x), label P is hit exactly once: the edge is forced by u(a,T) = p₁−x.
  - At (b,y) the edge is forced by u(b,T) = p₂−y.
  - At (c,z) the edge is forced by u(c,T) = s−z−p₁−p₂.
  - So the 9 label classes are perfect matchings. Linearity is not needed. With g = 6 this gives T1b below.
- **Parity boundary.** Suppose some S ⊆ V meets every edge in a number of points ≡ c (mod 2), and |S| ≢ g·c (mod 2). Then F has no perfect matching, and neither does any odd-weight inflation of F, with any TD(3,4,w) per block.
  - If r is odd, no such S exists.
  - If r is even it can exist; for example, any family containing a TD(3,2) component when g = 4.
- **Does it give new order-family output?** Not by itself. FDGDD(5{18}) was already certified, and further orders are gated by gcDCQS(h⁴:2) seeds. What it does is remove the computer-found ingredient from the §4(3) family. The new orders come from the fan widening.

## Q2. Published necessary/sufficient results

- **H(5,g,4,3).** Zhang–Ge 2013, author copy: "for n = 5, an H(g⁵) exists if g is divisible by 4 or 6 … Ji [11] … showed that an H(g⁵) exists whenever g is even, g ≠ 2 and g ≢ 10, 26 (mod 48)" (http://staff.ustc.edu.cn/~drzhangx/papers/new%20proof%20sqs.pdf). The PDF extraction drops the ≠ and ≢ signs; the paper's Theorem 1.2 restates the result. So H(5,6,4,3) exists (Mills), and H(5,10,4,3) is open.
- **KF existence.** TZ LF239–240: "A KF(mᵛ) exists if and only if m ≡ 0 (mod 2), v ≥ 4 and m(v − 1) ≡ 0 (mod 3)".
- **FDH(5,g≥4).** No published sufficient result located. CZZ's accessible text covers only g = 2. Liu–Lei cite CZZ only for "an RDSQS(2v) for v ∈ {23, 29, 41, 47, 53, 59, 71, 83}".
- **RDGDD(3,4,5{g}).** No published result located. Counting forces 6 | g. Known RDGDDs of other types: 10{2} (TZ Lemma 3.7); 8{3} and 14{3} (Liu–Lei).
- **Kirkman frames on a prescribed GDD.** No published criterion located.
- **Novelty status of the tripling lemma.** Elementary, so possibly folklore: NOVELTY-UNCLEAR.

## Q3. Ranked targets (pick T1)

**T1 (PICK): Frame-free FDGDD plus fan-widened families.** Mostly a write-up: about 4–8 h, at most 2 busy, under 2 GiB. The optional explicit order-452 build needs about 1–3 GiB in C.
- **Exact statements.**
  - (a) The tripling lemma.
  - (b) Every H(5,6,4,3), zero-sum inflated, is an FDH(5,18,4,3).
  - (c) The parity boundary for g ≡ 0 (mod 4).
  - (d) For every S(3,5,v) and j ≥ 0: mcDSQS(18·4ʲ(v−1)+2), mcDSQS(32·4ʲ(v−1)), and RDSQS(8·4ʲ(v−1)+2).
- **Chains for (d).** No search is needed; the seeds and imports are listed below.
  - Construction 2.3 with (m_j,1,v−1,s).
  - m_j grows ×4 via (m,4,4,s) and the classical type-4⁴ fan (lane I1).
  - FDGDD(5{m·4ʲ}) comes from weighting by RDTD(3,4,4ʲ) (TZ Thm 2.5(2)).
  - Construction 2.1 fills with mcDSQS(18·4ʲ+2), mcDSQS(2^{2j+5}) or RDSQS(2^{2j+3}+2).
- **Seeds and imports for (d).** gcDCQS(18⁴:2); gcDCQS(32⁴:0) with FDH(5,8,4,3) (gcdcqs32 lane); RDCQS(8⁴:2) (TZ Lemma 3.1). S(3,5,26) from the KKW table row "26 5 260 ≥1 … [8], [9]" (Denniston 1976; https://web.math.pmf.unizg.hr/~krcko/results/steiner3.html). The table lists S(3,5,41) and S(3,5,50) as "?" (unknown).
- **Open attestation.** TZ LF1117: "(4) Develop more effective recursive constructions for mcDSQS(v)s." TZ LF1114–1116 uses only Lemma 3.8 fans: "By Construction 2.2 or 2.3 and Lemma 3.8, the existence of an mcDSQS(18 · 4ⁿ + 2) would be obtained…"
- **Baseline.** The lane's SAT frames on one master (2.17 s and 3.88 s). The TZ families 2·9ⁿ+2 and 18·4ⁿ+2.
- **Approaches already exhausted.** Every symmetric size-6 frame-derived seed model the lane tried was UNSAT (restricted). TZ's RDTD criterion skips m = 3. TZ uses only RDS fans.
- **New representation.** The König/AG(2,3) labelling; the point-deleted S(3,5,26) as a 1-FG.
- **Falsification and controls.**
  - Run the explicit labelling on the lane's D15 master and the Z5×Z3 and Z3×D5 KM masters. The output must PASS both lane FDGDD checkers at all 90 points with no SAT.
  - A non-proper u must FAIL.
  - A g = 4 instance with a TD(3,2) family component: realizability is not yet shown; SAT test.
  - Check the S(3,5,26) data and the 1-FG property.
  - Optional: build mcDSQS(452) explicitly and check it directly (3,822,225 blocks).
- **Correctness / novelty / significance.**
  - Correctness: proof sketch only.
  - Novelty: none of 452, 1802, 800, 3200 sits in a known family in scope (a miss is not novelty).
  - Significance: moderate. It is an infinite-family extension of TZ §4(3).
- **Separate lead, outside this slice.** RDSQS(202) → LKTS(603) imports the mod-4 branches of Constructions 2.1/2.3, whose proofs are in unread Chang–Zhou 2013. Its LKTS priority has not been screened (Wang only covers v < 200), and FDH(5,8,4,3) is lane-checked only. Status: INCONCLUSIVE; do not claim.

**T2: new seeds gcDCQS(18⁵:2) [92 points] and FDGDD(3,4,6{18}) [108 points].**
- **Consequence.** mcDSQS(18·5ᵗ+2) for all t ≥ 1, via RDS(3,6,5ᵗ+1) (TZ Lemma 3.8, q = 5). Also 380 from S(3,6,22) and 740 from S(3,6,42).
- **Attestation.** A derived target from TZ §4(1)/(4).
- **Exhausted.** [INFERENCE, in the style of Lemma R] no TZ recursion outputs gcDCQS(18⁵:2).
- **Representation.** A regular Z5×H₁₈ action with groups as Z5-classes, a stem swap from an index-2 subgroup of H, and a μ₂ multiplier, which is compatible with Lemma I. FDGDD(3,4,6{18}) from a zero-sum-tripled bare H(6,6,4,3) plus coupled KF(18⁵) SAT. The tripling lemma does not cover 5 groups.
- **Control.** A restricted UNSAT is not a nonexistence proof.
- **Significance.** Moderate, but it is a compute-range extension.
- **Feasibility.** Medium-low. The 18⁴:2 seed needed |G| = 288 and about 3 h of pivots.

**T3: odd-r tripling conjecture (g ≡ 2 mod 4).**
- **Statement.** Every r-regular 3-partite 3-graph with r odd (at least those that occur as missing-group families) has a 1-factorizable zero-sum 3-blow-up.
- **Consequence.** FDH(5,3g,4,3) whenever H(5,g,4,3) exists. Known cases: r = 1 (trivial) and r = 3 (T1).
- **Falsification.** SAT on random 5- and 7-regular instances, and on pairs of disjoint bachelor Latin squares of order 5. nauty (geng, genbg, labelg) and kissat/cadical are installed in /opt/homebrew/bin.
- **Significance.** Contributes to the FDH spectrum only; no mcDSQS orders.
- **Feasibility.** A proof in 18 h is unlikely.

## Screens run (metadata/abstract level; misses are not novelty)
- **Citers of CZZ (OpenAlex and zbMATH):** 6 works. Tan–Zhou's *Tilings* paper (arXiv 2512.22754) mentions FDH only in its references; Etzion–Tan–Zhou 2510.24132 has no FDH or frame material.
- **arXiv abstract search:** nothing relevant after 2503.11934.
- **DataCite topic queries** (frame-derived, Kirkman frame, H-design, mcDSQS, design titles since 2026-06): nothing on frames or colourings. The only SQS items are Liu–Feng (2026-09-20) and McMaster theses.
- **Zenodo AI-author families via DataCite** (Ferudun, Vos, Raval, Kirtchakov, Long): no design-theory titles since 2026-08-01; the newest Ferudun record is 2026-10-18T06:11:15Z. Titles only; Zenodo itself was not queried.
- **Sage design catalog:** has KTS, SQS, TD/OA and difference matrices; no H-designs, frames or CQS. OEIS is not applicable.
- **Access holes:** CZZ body (paywall); Chang–Zhou 2013 (OpenAlex marks it bronze OA, but ScienceDirect and CORE return 403); Xu–Ji 2021/22/24; the Zheng thesis; the Mills and Ji bodies; the Yuan–Kang product proof; the journal version of TZ §4. There is no host clock; only server timestamps were seen.

## Files
- `/Users/jinleic/repos/aifours/mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt:237-255,281-345,444-541,680-688,1070-1071,1094-1117`: definitions, Constructions 2.1–2.3, Theorem 2.5, Lemma 3.8, §4.
- `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/tz43-gcdcqs18/evidence/fdgdd18-d15-inflated/construction-note.md:1-52`: the bare D15 master, the zero-sum inflation and the SAT frames.
- `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/tz43-gcdcqs18/sources/tz43-family-consequence-v1.md`: the family bridge, which uses RDS fans only.
- `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/tz43-gcdcqs18/sources/tz43-feasibility-and-bridge-v1.md`: Lemma W and the seed models.
- `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/tz43-gcdcqs18/README.md:131-160`: Lemmas N, K, R and W.
- `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/gcdcqs32-four-groups/README.md:224-236`: the type-4⁴ fan and FDH(5,8,4,3).
- `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/screening/math-1-tz43-priority-screen-v1.md`: the prior screen and its access holes.
- `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/checkpoints.md:249`: the mcDSQS(2p) target closed as NEEDS-NEW-REPRESENTATION, so it is not repeated here.
- `/Users/jinleic/repos/aifours/mathematics/kirkman-large-sets-57-87/sources/wang-2607.21521.txt:486-495`: LKTS known for v < 200 except 57 and 87.

## Architecture
H(5,6,4,3) →(tripling lemma)→ FDGDD(5{18}). Then gcDCQS(18⁴:2) + an S(3,5,v) fan →(Construction 2.3)→ gcDCQS(18^{v−1}:2) →(Construction 2.1 + mcDSQS(20))→ mcDSQS(18(v−1)+2). Group size m grows ×4 through type-4⁴ fans combined with RDTD(3,4,4ʲ) weighting.
