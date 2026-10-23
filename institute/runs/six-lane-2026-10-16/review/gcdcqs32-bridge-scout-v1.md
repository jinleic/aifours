**Verdict: BRIDGE-HOLDS.** I found no mathematical gap on either route:

- **Reproducibility route.** Construction 2.3 with (m,g,n,s) = (8,4,4,0) produces the certificate, and `build_c23.py` follows it.
- **Family route.** Corollary 2.6 plus Lemma 3.4 give the n ≥ 4 family. Construction 2.1 also gives order 128.

The bridge does rely on published results that I did not re-prove (listed at the end). Some checks have only been run by the worker, not by the parent. These affect how well-evidenced the route is, not whether it is correct.

**Limits of this audit.** This session had no shell, eval or clock tool.
- I could not read the host clock; the only date I have is the session date, 2026-10-17.
- I ran no `python3 -B -c` checks and recomputed no hashes. Every SHA below is copied from a receipt or README.
- Everything else comes from reading files and arithmetic by hand. My own derivations are marked [INFERENCE].

Paths are under `/Users/jinleic/repos/aifours`. TZ = `mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt` (arXiv:2503.11934v1, https://arxiv.org/abs/2503.11934v1, 15 Mar 2025). LANE = `mathematics/evidence/six-lane-20261016/gcdcqs32-four-groups`. REV = `institute/runs/six-lane-2026-10-16/review`.

## 1. Construction 2.3 and the definitions it uses (restated in symbols)

**Basic notions**
- **GDD(t,K,v)** (TZ:48–59): a set X with a partition G into groups and a block family B. Block sizes lie in K, each block meets each group at most once, and each t-subset drawn from t distinct groups lies in exactly one block. The type is the multiset of group sizes (61–62); type 1^v is a Steiner system S(t,K,v) (63–66).
- **PPC and PC** (69–70): a partial parallel class (PPC) of Y is a set of pairwise disjoint blocks inside Y; a parallel class (PC) is a PPC that partitions Y.
- **Derived design** (78–80): at x, the blocks through x with x removed.
- **Colourings** (90–100): an r-colouring partitions the blocks into r PPCs. χ′(v) is the minimum of χ′(D) over all STS(v) D.
- **(1.1)** (109–125, citing [19]): χ′(v) = (v+1)/2 for v ≡ 1 (mod 6), v ∉ {7, 13}.
- **mcSTS and mcDSQS** (127–130).

**Designs used directly by Construction 2.3**
- **STS(v,h) and gcSTS(v,h)** (211–220): the blocks of a GDD(2,3,v) of type 1^{v−h}h¹ with hole H. It is good colourable if the blocks split into r = χ′(v) PPCs of X, of which s = χ′(v) − (v−h)/2 are PPCs of X∖H. For v ≡ 1 (mod 6) this gives (r,s) = ((v+1)/2, (h+1)/2).
- **SQS(v,h) and gcDSQS(v,h)** (227–236).
- **KF(m^v), Kirkman frame** (237–240): a GDD(2,3,mv) of type m^v whose blocks split into classes, each a PC of X∖G for some group G.
- **GDD(3,4,mv) of type m^v** (241–242): its derived design at x ∈ G is a GDD(2,3,m(v−1)) on X∖G.
- **RDTD(3,4,m)** (243–246): an RDGDD(3,4,4{m}), i.e. a GDD(3,4,4m) of type m⁴ whose derived design at every point is resolvable.
- **FDGDD(3,4,v{m})** (246–247): a GDD(3,4,mv) of type m^v whose derived design at every point is a KF(m^{v−1}).
- **s-FG(3,(K₁,…,K_s,K_T),v)** (248–255): (X, G, B₁, …, B_s, T) with G a partition of X. Each (X, G ∪ Bᵢ) is a Steiner 2-system and (X, G ∪ ⋃Bᵢ ∪ T) is a Steiner 3-system. The type is the multiset of group sizes.
- **CS and CQS** (256–270): a stem S, with groups partitioning X∖S. Every t-subset not inside S ∪ G is in exactly one block, and no t-subset inside S ∪ G is in any block. A CQS is the case t = 3, K = {4}.
- **gcDCQS(gⁿ:s)** (279–288): a CQS(gⁿ:s) such that
  - (1) for x ∈ G, the derived design (X∖{x}, (G∪S)∖{x}, A_x) is a gcSTS(gn+s−1, g+s−1);
  - (2) for x ∈ S, the derived design is a KF(gⁿ).

**Construction 2.3, statement (444–447).** Assume:
- a 1-FG(3,(K₁,K),gn) of type gⁿ;
- integers m, s with mgn+s ≡ mk₁+s ≡ 2 or 4 (mod 6) for every k₁ ∈ K₁;
- a gcDCQS(m^{k₁}:s) for every k₁ ∈ K₁;
- an FDGDD(3,4,k{m}) for every k ∈ K.

Then a gcDCQS((mg)ⁿ : s) exists.

**Proof.** The 4 (mod 6) case is deferred to [3, Lemma 5.14] (line 449). Only the 2 (mod 6) case is proved here (449–541), and it is the case used.
1. **Set-up** (451–452): Y = (X×I_m) ∪ S, groups H = {G×I_m}, and H_B = {{x}×I_m : x ∈ B}.
2. **Blocks B ∈ B** (453–465): put a gcDCQS(m^{|B|}:s) A_B on (B×I_m) ∪ S. At (x,i), its colouring consists of:
   - classes A_B^{y,j}(x,i) for y ∈ B∖{x}, j ≤ m/2. The label y carries no condition.
   - classes A_B^j(x,i) for j ≤ (m+s)/2. These are PPCs of (B∖{x})×I_m.
3. **Blocks B ∈ T** (467–476): put an FDGDD D_B on B×I_m. At (x,i) its derived design is a KF with classes D_B^{y,j}(x,i), each a PC of (B∖{x,y})×I_m.
4. **Block set** (477–482): F = ⋃A_B ∪ ⋃D_B. The source says it is "routine" that F is a CQS.
5. **Colouring at (x,i), x ∈ G** (495–531):
   - for y ∉ G: F^{y,j} = A_{B₁}^{y,j} ∪ ⋃_{{x,y}⊂B∈T} D_B^{y,j}, where B₁ is the B-block through x and y (498–508);
   - for y ∈ G∖{x}: F^{y,j} = ⋃_{{x,y}⊂B∈T} D_B^{y,j} (508–514);
   - F^j = ⋃_{x∈B∈B} A_B^j.
   The F^{y,j} with y ∈ G∖{x}, and all the F^j, avoid the hole. Stem points are handled at 532–540.

**Output (541).** A gcDCQS((mg)ⁿ:s). With (8,4,4,0):
- number of classes: (gn−1)m/2 + (m+s)/2 = 64 = χ′(127);
- hole-free classes: (g−1)m/2 + (m+s)/2 = 16.

[INFERENCE] I re-proved, for s = 0, the steps the source leaves as "routine" (482) or "it follows" (523).
- **CQS property.** Classify each big triple by its projection to X:
  - Three distinct points, not all in one group: they lie in exactly one B- or T-block, so exactly one ingredient block covers the triple.
  - Pattern {a,a,b} with a, b in different groups: only A_B for the B-line through a and b covers it. The D copies cannot, because their blocks meet each {y}×I_m at most once.
  - Triples inside one big group: nothing covers them. B-lines meet a group once; T-blocks contain at most 2 points of a group; D blocks are transverse.
- **Colouring.** The T-blocks through {x,y} split X∖B₁ when y ∉ G, and X∖G when y ∈ G. The B-blocks through x split X∖G. So every F-class is a PPC, and every ingredient class is used exactly once.

## 2. Implementation versus construction

**`build_c23.py` (sha 6255e32b…) is faithful to the construction.**

| Step | What the code does | Source |
|---|---|---|
| Labels | (p,i) ↦ 32u(p) + 8w(p) + i, so the big groups are G_u×I₈ | H, 451 |
| A_B | I2 point 8t+i ↦ (B_t, i); asserts every B-line meets each group once | H_B, 452–453 |
| D_T | I3 point 8s+i ↦ (T_s, i), with T sorted | 467 |
| Block count | asserts 80384 = 16·1184 + 48·1280 = (C(128,3) − 4·C(32,3))/4, so no duplicates collapsed | 477 |
| A-classes | at c = 8u(x)+i, splits I2 classes by whether they meet the hole; asserts 4 avoiding and 12 not. The 12 go to F^{y,j}, 4 per y; the 4 go to F^j | 456–461, 498–521 |
| D-classes | assigns y = T[group the class misses]; asserts 4 classes per y. This is the property the PPC argument needs | 467–476 |
| Output | 60 F^{y,j} + 4 F^j = 64 classes; the stem part is empty | 523–531 |

The parent's assembler replay was byte-identical (`REV/gcdcqs32-parent-producer-replay-v1/result.json`). That replay re-ran the assembler only.

**What `check_ingredients.py` covers, hypothesis by hypothesis**

| Hypothesis | Check | Status |
|---|---|---|
| H1: 1-FG(3,({4},{5}),16) of type 4⁴ | `check_fg` | Complete for this instance: partition into 4 groups of 4, sizes 4 and 5, every pair once in G ∪ B, every triple once in G ∪ B ∪ T |
| H2: 128 ≡ 32 ≡ 2 (mod 6); 31 ∉ {7,13} | not encoded | Arithmetic; holds |
| H3: gcDCQS(8⁴:0) | **not in this file**; done by `check_gcdcqs.py` / `.c` | I read `check_gcdcqs.py` and it is a complete definition-first check (r = 16, s = 4, nonempty PPCs, derived design exact, exactly 4 hole-free). I did not read the C version |
| H4: FDGDD(3,4,5{8}) | `check_fdh` | Complete: transverse blocks, each transverse triple exactly once, and at all 40 points the classes partition the derived design into PCs of X∖(G_x ∪ G′). The count of 4 classes per missed group is forced by counting [INFERENCE] |

**Concrete gaps.** None of these affect correctness, because the 128-point certificate is checked directly.
- **G1 (H3 checker not in this file).** The I2 PASS results exist only as strings in `LANE/evidence/gcdcqs32-c23/receipt.json` and in README:218. No checker output file is pinned for I2.
- **G2 (H2 not encoded).** Trivial arithmetic, but not written into the checker.
- **G3 (no parent-run ingredient check).** The parent has not run any ingredient check. The 10/10 ingredient controls were run by the worker.
- **G4 (shared parsers).**
  - `build_c23` imports `read_fdh` from the checker itself, so I3's checker and assembler share one parser.
  - I2 is read by the lax `seed_tools.read_cert` but checked by the strict `check_gcdcqs.parse`. They agree on any file that passes the strict parser [INFERENCE].
- **G5 (error handling).** Some malformed files cause tracebacks with exit 1 rather than a FAIL line.
- **G6 (control coverage).** No control has an FDH class that meets G_x, misses two groups, or is empty.

**Why the gaps are mitigated** [INFERENCE]. Given the build as read, if the 128-point certificate passes, I1 must be a valid 1-FG and the I2/I3 copies must cover correctly. Any defect would leave big triples uncovered or doubly covered, or would trip the 80384-block assertion.

**My hand spot-checks**
- (X, G ∪ B) is AG(2,4): at all 16 points, the four B-lines through the point partition the 12 points outside its group, and all 16 B-lines are transversal.
- Point 0: for all 15 pairs {0,a}, the T-blocks through the pair partition X minus the line through 0 and a. So all 90 non-collinear triples at 0 are covered exactly once, and 15 T-blocks pass through 0.
- This is not a full check of T.

## 3. The bridge to the infinite family

**Exact statement.** Corollary 2.6 (TZ:684–685, proof 687–693), which §4(2) invokes at lines 1111–1113:

> "Let m ≡ 4, 8 (mod 12). If there exist a gcDCQS(m⁴ : 0) and an mcDSQS(m), then there exists an mcDSQS(m · 4ⁿ) for any integer n ≥ 2."

The proof applies Construction 2.4 (568–679) with s = 0, using 2-RSQS*(4ⁿ) and RDTD(3,4,m) from Theorem 2.5 (680–683), to get gcDCQS(m^{4ⁿ}:0). It then fills holes with Construction 2.1 (292–335).

**Hypotheses checked for m = 32, in the same order as the m = 20 verdict (REV/gcdcqs20-parent-verdict.md:38–41)**

1. **Definitions** (211–220, 227–236, 279–288).
   - w = 127, h = 31, so r = 64 and s = 64 − 48 = 16.
   - More than 16 hole-free classes is impossible. Each of the 31 hole points lies in 48 derived triples and in at most one triple per class, so 31·48 ≤ 31(64 − s).
   - χ′(127) ≥ ⌈2667/42⌉ = 64 by counting.
2. **Known input mcDSQS(32), Lemma 3.4** (903–907).
   - This is the authors' own cyclic SQS(32): 40 base blocks at TZ:1326–1332, which develop under Z₃₂ to 1240 blocks (orbit lengths 32×38, 16, 8).
   - The derived STS(31) at 0 is split into 16 PPCs at 1341–1372 (sizes 10¹³ 9 8 8, total 155). Cyclic translation carries this to every point.
   - Lane check E0 (worker-run): PASS, with 4/4 corruption controls rejected (README:129).
   - I compared the lane JSON with the text by reading: all 40 base blocks and all 16 parts match.
   - **No parent-run check exists** (checkpoints.md:331 says "worker level"). For m = 20 the parent did rebuild this input independently.
3. **Corollary 2.6.**
   - 32 ≡ 8 (mod 12); the gcDCQS(32⁴:0) is supplied by e38945b1…0f46.
   - Theorem 2.5(1) gives 2-RSQS*(4ⁿ) for every n ≥ 2, and 4ⁿ ≡ 4 (mod 12) as line 571 requires.
   - Theorem 2.5(2) gives RDTD(3,4,32), since gcd(32,4) = 4 ≠ 2 and gcd(32,18) = 2 ≠ 3.
   - Construction 2.4: 4m + s = 128 ≡ 2 (mod 6) and δ = 16. The input's derived colouring has 3m/2 + δ = 64 classes, the last 16 hole-free, which is exactly the gcSTS(127,31) condition.
   - Construction 2.1: 32·4ⁿ ≡ 2 (mod 6), so the proved branch (line 295) applies. gcDSQS(32,0) with an empty hole is just an mcDSQS(32) (227–236).
   - Result: mcDSQS(32·4ⁿ) for n ≥ 2, which is mcDSQS(2^{2N+1}) for N ≥ 4.
4. **Order 128 directly by Construction 2.1** (292–335).
   - Inputs: gcDCQS(32⁴:0), with mcDSQS(32) filled into each of the four groups.
   - At each point x:
     - merge the 16 hole-free classes with the 16 classes of the filled STS(31) at x;
     - keep the other 48 classes unchanged.
   - Result: 64 classes covering 2667 triples, which is minimum because ⌈2667/42⌉ = 64. The block count is 80384 + 4·1240 = 85344 = C(128,3)/4.
   - §4(2) does not state this case. REV/gcdcqs20-priority-audit.md:94 already noted it. No explicit 128-point object has been built yet.

**The consequence, exactly as the source supports it**
- **Stated by the source** (Corollary 2.6 with Lemma 3.4, §4(2) lines 1112–1113): given a gcDCQS(32⁴:0), an **mcDSQS(2^{2n+1}) exists for every integer n ≥ 4**.
- **From the source's constructions but not stated**: mcDSQS(128) via Construction 2.1. Together with Lemma 3.4 (order 32), this gives mcDSQS(2^{2n+1}) for every n ≥ 2.
- **Downstream, optional**: Corollary 1.4(1) (186–187) would give q₀′(3,4,2^{2n+1}) = 2^{2n} + 1. That step needs [16, Thm 5] through Theorem 1.3 (177–184). The order-32 case is already Theorem 3.10(2) at line 1085.
- None of this is formally proved (no Lean proof), and the imports below are not re-proved.

## 4. Imports

- **Tan–Zhou's own results.** Constructions 2.1 and 2.4, Theorem 2.5 and Corollary 2.6, all from arXiv v1. The journal version (DCC 93(10) 4117–4140) was not compared.
- **[21] Xu–Bao–Ji**, Des. Codes Cryptogr. 88 (2020) 2377–2386, Corollary 3.2: 2-RSQS*(4ⁿ) for n ≥ 2 (TZ:1181–1182). This is needed for every order from 512 up. I did not re-read it; two searches found no accessible copy. Tan–Zhou's own Theorem 3.2 (line 896) relies on the same result.
- **[9] Ji–Yin**, JCTA 117 (2010) (TZ:1146–1147), together with [21]: RDTD(3,4,m). For m = 32 this import can be avoided [INFERENCE]:
  - Take blocks {(k, a_k) : a ∈ F₃₂⁴, Σa_k = 0}.
  - At a point (1, a), the classes are P_t = {(b, ωb + t, a + (1+ω)b + t)}, indexed by t, for a fixed ω ∉ {0, 1}.
  - These classes form a resolution, and by symmetry the same works at every point.
- **Lemma 3.4 / Appendix B.** A finite object; only worker-checked so far (see §3 item 2).
- **(1.1), via [19] (Hanani triple systems).** Not load-bearing [INFERENCE]: counting gives the lower bound, and the explicit or constructed colourings give the matching upper bound.
- **Not used.** [3] (the 4 mod 6 cases) and [17] (KF existence). Chang–Zheng–Zhou 2019 ([2], FDH designs) was read only at abstract level by the lane; it is a pointer for the priority audit, not part of the bridge.

## 5. Inputs for the separate 128-point fill

**Source text:** TZ (sha df52a8f1…c8164).
- Anchor lines: 1321 and 1334.
- Base blocks: lines 1326–1332.
- The 16 parts: lines 1341–1372, each part being a pair of consecutive lines.

**Lane files**

| File | Contents | Hash |
|---|---|---|
| `LANE/sources/tz_appb_mcdsqs32.json` | `base_blocks` (40), `parts` (16), `derived_at` 0. Matches the text by my reading | 5ab58710…d8aa (README:129) |
| `LANE/code/tz_appb_mcdsqs32.py` | `extract`, `check`, `controls` modes | a4a91e54…df06 (`runs/e3a_code_sha256_at_launch.txt:22`; not in receipt.json) |
| `LANE/controls/e0_appb_controls/` | 4 mutant files plus `control-results.json`, all rejected | — |

The E0 PASS output itself is not pinned; it exists only as README:129. README:101 spells the JSON as `tz_appB_…` with a capital B (nit).

**Parent tools to adapt**
- **`REV/mcdsqs80_parent_fill.py`** is hard-coded for 20/80. A 32/128 variant needs these changes:

  | Setting | 80-point script | 128-point variant |
  |---|---|---|
  | Data key | `cells` | `parts` |
  | Local transport | `(p + local) % 20` | `(p + local) % 32` |
  | Parameters | (80,4,20,40,10) | (128,4,32,64,16) |
  | Hole-free classes | 10 | 16 |
  | gcDCQS pin | 80-point certificate | `REV/gcdcqs32-parent-inputs-v1/gcdcqs32_c23.txt` |

- **`REV/check_mcdsqs_independent.py`** works for any v, with colours = ⌈D/M⌉: 16 at v = 32 and 64 at v = 128. It can check a rendered mcDSQS(32) as well as the 128-point fill.
- **`REV/check_gcdcqs_parent.py`**: its `parse()` returns (v, n, g, r, s, groups, blocks, sections).
- Memory use at v = 128 is unmeasured; the triple sets hold about 341k entries.

The worker's hypotheses note (SHA fe44e159…, as reported by you; not recomputed) agrees with this audit, and like it, makes no claim about the family.
