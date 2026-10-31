# Independent same-harness review: f166 rank-two coset-exclusion chain

Reviewer `ReviewF166RankTwo`. Wave `f166-walsh-rank-two-coset-exclusion`. Manifest `manifest-v1.json`, SHA-256 `5a56e9643461d0ca63d1731387e3eebc322f8943cd5c80c69f2c5bd385de887a`, 4662 B (verified). Author `InfoBalancedNL242-2-2` (slot info-6). Native `/bin/date` immediately before composing this file: **2026-10-29T08:49:01-0700 PDT**. That is an observed clock, not an asserted file-creation time.

This is a same-harness review of written mathematics, supported by exact computation that I wrote independently. It is **not** a human review, an independent-model-family review, a formal or kernel verification, or a novelty assessment. I did not use author "PASS" or Z3 statements as evidence. I did not open or execute any author checker, author receipt or out-of-manifest source.

## 0. Inputs

I read all seven inputs completely, in the declared order. Before interpreting any of them, I checked its SHA-256, byte count and LF count against the manifest; all seven matched exactly. I read the three mandatory corrections before the sources they correct.

| # | file (directory as in manifest) | role | SHA-256 prefix | bytes | LF |
|---|---|---|---|---:|---:|
| 1 | `frontier-20261028-cubic-divisibility-withdrawal-v1.md` | mandatory withdrawal 1 | `7b6596b4e5ca` | 4349 | 33 |
| 2 | `frontier-20261028-cubic-common-top-erratum-v1.md` | mandatory erratum 2 | `b4e20dcf0fdb` | 2889 | 28 |
| 3 | `frontier-20261028-rank2-shared-cubic-barrier-v1.md` | mandatory correction 3 | `7af42130c732` | 5194 | 39 |
| 4 | `info-6-four-zero-rank6-radical-parent-v1.md` | adopted f131 framework, scope only | `12efd10b4a9d` | 5831 | 31 |
| 5 | `frontier-20261028-collective-polar-exclusion-v1.md` | collective polar exclusion | `e562e6074dec` | 8627 | 108 |
| 6 | `frontier-20261028-lowrank-valid-profile-v1.md` | low-rank profile (P1) | `910d3b68e5e2` | 6167 | 63 |
| 7 | `frontier-20261028-rank2-coset-exclusion-v1.md` | rank-two coset exclusion | `95aecd59e7d1` | 10881 | 161 |

The manifest contains no certificate JSON.

## 1. Result

**Counts: FATAL 0, MAJOR 1, MINOR 3.**

The coset argument is a correct conditional proof for exactly the profiles it treats, namely m ∈ {118,120,122}. Even so, **the chain does not exclude even-polar rank two.** The low-rank packet's rank-two list, (D,m) ∈ {(12,118),(16,120),(20,122)}, does not follow from the constraints the packet states. Those constraints also allow m=114 and m=116, and neither value is treated.

| ID | claim (source) | verdict |
|---|---|---|
| W1a | H=x₀x₁x₂⊕x₃x₄x₅⊕x₀x₁x₃ has degree 3 and weight 14; the divisor-8 lemma is false (input 1) | WRITTEN_SUPPORTED |
| W1b | The collective, low-rank and coset sources do not use the withdrawn divisor-8 or Z-table material (inputs 1, 5–7) | WRITTEN_SUPPORTED (checked by reading) |
| W1c | Properties of the formal Z=14 even-half non-witness (input 1; receipt outside the manifest) | INCONCLUSIVE (not load-bearing) |
| E2a | h=x₀x₁x₂⊕x₃x₄x₅⊕x₀x₆x₇: weight 68, 6-dimensional coset weights {8,8,20,32}; the odd total-divisibility claim is withdrawn (input 2) | WRITTEN_SUPPORTED |
| E2b | No source in this chain uses the odd common-top total claim | WRITTEN_SUPPORTED |
| C3a | With a fixed rank-two polar, the odd Q has weight 64, 128 or 192; the radical linear term decides between 128 and {64,192} (input 3) | WRITTEN_SUPPORTED |
| C3b | No source in this chain uses the incomplete D28 Q-weight list | WRITTEN_SUPPORTED |
| C3c | Finite properties of the labelled D12 shared-cubic object (receipts outside the manifest) | INCONCLUSIVE (not load-bearing; the stated counts are arithmetically consistent) |
| CP1 | Decomposition k=g(12h−7)−8δ and identities (5)–(6) (input 5) | WRITTEN_SUPPORTED |
| CP2 | rank B ≠ 0 | WRITTEN_SUPPORTED |
| CP3 | rank 2 ⇒ z=64, D≡0 (mod 4), Z+2D≤64, D≤28, 108+D/2≤m≤122 | WRITTEN_SUPPORTED |
| CP4 | rank 4 ⇒ z=96 (excluding z=160 and z=128), D even, D≤24 | WRITTEN_SUPPORTED |
| LR1 | Odd energy 64(256−m), m≡n₃ (mod 3), deficit 8(m−60)=6n₁+5n₃+3n₅, and no further residue (input 6) | WRITTEN_SUPPORTED |
| LR2 | Rank-two list: 17 profiles, (D,m) ∈ {(12,118),(16,120),(20,122)}, 104≤n₇≤113, Z≤24 | **MAJOR (M1)** |
| LR3 | Rank-four list: 50 profiles in 10 (D,m) pairs, 126≤n₇≤146 | **MAJOR (M1, same root cause)**. Z≤40 holds conditional on D≥8. |
| LR4 | D≥12 at rank 2 (sparse-sign predecessor) and D≥8 at rank 4 (rank-four predecessor) | INCONCLUSIVE (outside the manifest, not read) |
| RC1 | Coset setup: q=0 exactly on R, block Poisson form, (1), mod-3 identity (2), Parseval (3), 81-vector class table (input 7) | WRITTEN_SUPPORTED |
| RC2 | Z≡0 (mod 4) via the parent-adopted congruence E₂+2n₃≡0 (mod 4) | Implication WRITTEN_SUPPORTED; premise INCONCLUSIVE (imported, outside the manifest) |
| RC3 | P2: Z≥8 | WRITTEN_SUPPORTED by my own reconstruction (§6.3); the out-of-manifest P2 file is not needed |
| RC4 | L1–L6 and the flat fact | WRITTEN_SUPPORTED (exhaustive checks) |
| RC5 | Case analysis over all (m,Z,e-patterns) induced by P1's list | WRITTEN_SUPPORTED, with MINOR m1–m3 |
| RC6 | Conditional theorem: P1 ∧ P2 ∧ parent congruence ⇒ rank B ≠ 2 | WRITTEN_SUPPORTED as a conditional |
| RC7 | Chain conclusion: rank two is impossible for actual targets | **MAJOR, inherited from M1** (counted once) |

## 2. Mandatory withdrawals and errata

**Withdrawal 1.** I recomputed H on F₂⁶: degree 3, weight 14. Translating by a support point gives H(0)=1 with weight still 14. This is a valid counterexample to "every degree≤3 polynomial on F₂⁶ has weight divisible by 8"; the correct divisibility is 2^(⌈6/3⌉−1)=2. I then checked each source for reliance on the withdrawn material:
- The collective packet uses quadratic Fourier analysis, mod 3 and energy only.
- The low-rank packet uses mod 3, the energy deficit and the collective identity.
- The coset packet uses Z∈{8,12,16,20,24}, which includes values not divisible by 8. Its Z≡0 (mod 4) comes from the parent congruence, not from cubic divisibility.

None of them uses divisor 8, the withdrawn Z table, or the withdrawn G₃ table. A side observation: Z=14 at m=118 would force E₂=5, which is odd. That conflicts with the parent congruence and fits the record's statement that the formal object has no odd half.

**Erratum 2.** I recomputed h on F₂⁸: degree 3, weight 68. The four 6-dimensional cosets obtained by fixing (x₀,x₁) have weights {8,8,20,32}; fixing (x₀,x₂), (x₀,x₆) or (x₀,x₇) gives the same multiset. The weights agree mod 4, but their sum is 4 mod 8. The withdrawal is correct, and no input in this chain uses the odd total claim.

**Correction 3.** Fix the anisotropic rank-two q with radical R. Then Q=q+λ+c has weight 128 when λ|_R≠0 (504 of 512 choices) and weight 64 or 192 when λ|_R=0 (4 choices each). That is the corrected list {64,128,192}. Neither the collective nor the coset packet uses Q weights. The low-rank packet explicitly leaves balanced and unbalanced Q open, so it does not use them either. The D12 object's stated counts are consistent with my arithmetic: (n₁,n₃,n₅,n₇)=(2,10,134,110) gives 8·58=464=6·2+5·10+3·134, m≡n₃ (mod 3), S=−2 and Z=8 from E₂=8. I did not verify its 512-integer receipts, which are outside the manifest.

**f131 disposition.** I read it as scope-only context and did not review it. Its reconstruction text states |Z₈|≥8 when rank B≤4. My discharge of P2 in §6.3 is an independent derivation and does not rely on that statement.

## 3. Common layer: reconstructed and tested on actual functions

The parent-adopted caller lives in a file outside the manifest, so I re-derived each fact this chain uses:

- **k and its parity.** For a≠0, W_f(a)=−2Σ_{x∈S}(−1)^{a·x}=4N_a−512. Hence k=N_a−128, and its parity is N_a mod 2 = a·T. So k is even exactly on K=T^⊥.
- **q is quadratic.** On K, q=⌊N_a/2⌋ mod 2 = e₂(a·x : x∈S) by Lucas, which is quadratic. Its polar on K is B(a,b)=Σ_{x∈S}(a·x)(b·x).
- **Q has the same polar.** Q=1_{k≡3 (mod 4)} is the restriction of the same e₂ to the odd coset, so its polar is B.
- **The inverses u and w.** Put T last and define u=(F(y,0)+F(y,1))/2 and w=(F(y,0)−F(y,1))/2. They have complementary supports. Walsh(u)=2k on K and Walsh(w)=2k on the odd half, so Walsh(k|_K)=128u and Walsh(k|_odd)=128w. Since Σu=0, m is even.

All of these held exactly on seven explicit balanced nine-variable functions with T≠0 (Part A of the controls): four random functions of polar rank 6 or 8, and three actual high-peak functions of polar rank 0, 2 and 4 obtained by point swaps out of an affine hyperplane. In every case the FWHT agreed with the direct 512×512 character sums.

## 4. Collective polar exclusion (input 5)

**CP1.** I checked the decomposition case by case. With g=(−1)^Q and h=1_{|k|∈{3,5}}, the base k₀=g(12h−7) agrees with k except at |k|∈{1,3}, where k−k₀=∓8. The resulting δg is +1 at |k|=3 and −1 at |k|=1, so Σδg=n₃−n₁.

Inverting g on its Walsh support Y gives Σ_{y∈Y}σ(y)Walsh(φ)(y)=2^t Σφg. This identity held exactly on actual functions of ranks 0, 2, 4, 6 and 8. Those functions also confirmed |Y|=4^t, magnitude 2^(8−t), Y affine, and σ quadratic of full polar rank on Y. Identities (5) and (6) follow.

**CP2–CP3.** Enumerating every quadratic with q(0)=0 gives these zero sets z:

| polar rank | possible z |
|---:|---|
| 0 | {128, 256} |
| 2 | {64, 128, 192} |
| 4 | {96, 128, 160} |
| 6 | {112, 128, 144} |
| 8 | {120, 136} |

The table agrees with 300 random quadratics. The even bound (9) is 64m≤16(z−Z)+36(256−z).
- Rank 0: z=256 gives m≤62 and z=128 gives m≤102, against m≥112.
- Rank 2: z=128 gives m≤102 and z=192 gives m≤82, against m≥108.
- Rank 2, z=64: Z+2D≤64 with Z≥1. Since m is even, D≡0 (mod 4), so D≤28.

**CP4.** z=160 gives m≤92, against m≥100. At z=96 the bounds are m≥100+D/2 and m≤114−Z/4. D=26 would force m≥114 and hence Z≤0, so D≤24, using that m is even.

For z=128, the list (10) is complete. Dividing the inverse equation by 4 gives 32v=3W(hg)−112σ−2W(δ). Reducing mod 3 gives d_y+σv≡1 (mod 3), which matches (11). The three sub-cases then close:
- **D=0:** σv=1 on all 16 points, contradicting S∈{−16,−14}.
- **D=2:** Σd_y≥28 while |4(n₃−n₁)|≤8.
- **D=4:** d_y∈{2,−4}, so |A|∈{4,8} with A=Y∩{|W(δ)|=4} affine. |A|=8 is impossible because a nondegenerate 4-dimensional phase has no affine 3-flat on which it is affine; I checked all 32 phases. |A|=4 leads to the half-integer contradiction, which I verified for all 32 phases and all 60 isotropic 2-flats per phase.

## 5. Low-rank valid profile (input 6)

**LR1** holds. The odd energy is Σk²=64(256−m). Mod 3 this gives m≡n₃, since 64≡256≡1. The deficit gives 6n₁+5n₃+3n₅=8(m−60). Total Parseval mod 3 yields the same relation and nothing new, so I agree that no further residue exists.

**M1 (MAJOR): the rank-two and rank-four profile lists do not follow from the stated constraints.** I implemented exactly the stated enumeration:
- D in the stated range;
- S∈[−4,4] at rank 2 or [−16,16] at rank 4;
- m=116+D/2+2S (rank 2) or 116+D/2+S (rank 4);
- m even, m≤122 or 112, and the even-half bound with Z≥1;
- n₁ from 0 to D, m≡n₃ (mod 3), and the deficit (3);
- n₃, n₅, n₇ nonnegative.

As an internal check, every profile also satisfies the odd energy and the collective identity (5). The result:

| case | profiles | (D,m) pairs | n₇ range | Z max |
|---|---:|---|---|---:|
| rank 2, stated constraints | 91 | 15: (12,114…122), (16,116…122), (20,118…122), (24,120/122), (28,122) | 99–124 | 40 |
| rank 2, claimed in the packet | 17 | 3 | 104–113 | 24 |
| rank 4, stated constraints | 121 | 25 | 123–146 | 40 |
| rank 4, claimed in the packet | 50 | 10 | 126–146 | 40 |

**Where the claimed lists come from.** Both claimed lists, including their (D,m) pairs and n₇ extrema, are reproduced *exactly* when one extra filter is added: m≡1−D (mod 3). The packet explicitly calls that relation spurious and says it is not used. Substituting m=116+D/2+cS shows the filter is equivalent to S≡1 (mod 3) at rank 2, so every claimed rank-two pair has S=−2; at rank 4 it is equivalent to S≡2 (mod 3).

**Explicit counter-profile.** (D,m,S,n₁,n₃,n₅,n₇)=(12,114,−4,12,0,120,124) satisfies every stated constraint, as well as the odd energy 9088=64·142 and identity (5): 384=448−64. It lies outside the claimed list.

**Out-of-manifest premises.** The packet cites the collective and sparse-sign predecessors. The collective packet restricts nothing beyond what I enumerated. The sparse-sign predecessor is outside the manifest and was not read. If it proves an additional restriction such as S≡1 (mod 3), the packet has to state that restriction and bring it under review; as written, the lists are unsupported. LR4 (D≥12 at rank 2, D≥8 at rank 4) also rests on those unread predecessors.

**Consequence for the chain.** The coset case analysis depends only on (m,Z), so it automatically covers every stated pair with m∈{118,120,122}. It does not cover:
- m=116 (D∈{12,16}): Z≤32 and E₂=16−Z/2≤12;
- m=114 (D=12): Z≤40 and E₂=20−Z/2≤16.

An exploratory probe with my exact relaxation model shows that the coset packet's own lemma set does **not** exclude (m,Z,pattern)=(116,16,(0,4,4)). In that configuration Hyp₂=Hyp₃ is still forced, but |F₂∩F₃|=2+2H is even, so the parity contradiction disappears. The model found 2 geometrically placed region vectors with feasible counts. One example is A₁=16, C₂=C₃=4, D₁=18, G₂=G₃=2, O=18 and H=0, with |F₂∩F₃|=2. This is a relaxation and makes no realizability claim; it shows only that closing the gap needs new arguments.

There are two repair paths:
- justify the missing restriction, or
- extend the case analysis to m=114 and m=116.

## 6. Rank-two coset exclusion (input 7)

### 6.1 Setup

At rank 2 with z=64, q must vanish on R. Otherwise the radical linear term would make q balanced (z=128), as the enumeration in Part B shows.

The value sets Ŵ(r,0)∈{0,±8} and Ŵ(r,s≠0)∈{±4,±12} follow. Parseval gives 256m=64(64−Z)+16E₂+144(192−E₂), so E₂=248−Z/2−2m, which is (1).

U_s=W₆(v_s)/16 and v=3σ−2τ. Since 16≡1 and −2≡1 (mod 3), this gives t≡U (mod 3), which is (2). All entries of (3) check, as does Σ_sU_s²=4n_c.

I verified the block Poisson identity, its inverse, U_s≡n_c (mod 2), Σ_sU_s²=4n_c and L1 exactly on all seven actual functions. Each function was tested with both the coordinate split and a random GL₈ split. The generalized split also held exactly: with τ=centered(v mod 3) and σ=(v+2τ)/3, I confirmed 16U=3W(σ)−2W(τ) and W(τ)≡U (mod 3).

### 6.2 Z≡0 (mod 4)

This step needs only "E₂ even". From (1), E₂ even ⇔ Z≡0 (mod 4), and then L1 makes every e_s even. The source is the parent-adopted congruence E₂+2n₃≡0 (mod 4), whose file is outside the manifest and was not read.

I tried to derive E₂ parity myself and could not. I combined:
- full and even-subcode binomial-moment (dual-code) integrality;
- the 255/256 counts;
- Parseval and 64m;
- the rank-two z=64 counts.

E₂ parity is not forced by these: it takes both values on the integer kernel, and a particular integer solution exists (Part G). The premise is therefore imported, not reproduced. If it failed, the cases with every e_s odd, namely (m,Z)∈{(120,10),(120,14),(118,10),(118,14),(118,18),(118,22)}, would be untreated.

### 6.3 Discharging P2: my reconstruction

I derive Z≥8 under the explicit hypotheses (rank B=2, peak≤28) without using the P2 file.

1. **Residues of k².** For a∈K: k²≡4 (mod 32) when q=1, 0 on Z₈, and 16 otherwise. Quadratic weights on a 5-flat are multiples of 4. Hence Σ_A k²≡16(wt(q|A)/4+|A∩Z₈|) (mod 32) for every coset A of a 5-dimensional L⊂K.
2. **Constancy over cosets.** Σ_{a∈b+L}W²=|L|Σ_{x∈L^⊥}(−1)^{b·x}C(x). Here C(0)=512, and for x≠0, C(x)=−512+8·#{unordered pairs {y,y+x}⊂S}; so C(x)≡0 (mod 8) for every x. So Σ_A k²=2Σ±C(x) is constant mod 32 over all cosets of L.
3. **Even quadratic part.** At global rank 2, every B|_L has rank ≤2. Then wt(q|A)∈{0,8,16,24,32}, so wt(q|A)/4 is even.
4. **Constant parity.** By steps 1–3, |A∩Z₈| mod 2 is constant over the 8 cosets of each L.
5. **Degree and support bound.** Every affine 6-flat is a union of two cosets of some L, so it meets Z₈ evenly. Hence deg 1_{Z₈}≤5 on K. Since 0∈Z₈, RM(5,8) gives |Z₈|≥2^(8−5)=8. Under the peak bound Z₈ is exactly the set of Walsh zeros, so Z≥8.

**Controls on actual functions:**
- Step 2 and the residue formula held for 60 random L on each of the seven actual functions.
- deg 1_{Z₈}≤5 held for the rank-0 and rank-2 functions (degrees 0 and 2).
- Negative: all four random rank-6/8 functions reach degree 6.
- Negative: a formal +4 perturbation at one q-zero frequency breaks constancy in 60/60 trials while the pointwise residue formula still holds, so constancy is exactly the Boolean content.

### 6.4 Local lemmas (exhaustive)

- **Class table.** The 81 ternary 4-vectors give exactly the 17 |U| patterns of the class table: A₁₋₃, B, C₁₋₃, D₁₋₃, E, F, G₁₋₃, H, O. Σ_sU_s²=4n holds for all of them, and for n=3 the product U₀U₁U₂U₃=−3.
- **L4.** The e=2 local states (|U|,t_rel,W) are (0,0,0), (1,−2,4), (2,2,12), (3,0,16) and (4,−2,20). Enumerating every 5-tuple with sum 64 gives exactly the κ=0…4 family. All 8064 two-atom τ give {t=0} equal to an affine hyperplane.
- **L6.** I enumerated all 317,688 four-atom τ (taking p₁=0 by translation invariance and ε₁=+1 by global sign). The histograms are (24,32,8) for 312,480 of them, exactly the affinely independent ones; (48,0,16) for 2604; and (0,64,0) for 2604. Every geometric claim held:
  - Hyp is an affine hyperplane and F an affine 3-flat with F⊂Hyp;
  - {t=0}=Hyp∖F;
  - {|t|=4} is a 4-flat in the (48,0,16) case.
- **Flat fact.** The 620 affine 3-flats of F₂⁵ meet pairwise in 0, 2 or 4 points (8 only for identical flats). Negative control: in F₂⁶, two 3-flats can meet in exactly 1 point, so the step "Hyp₂=Hyp₃" is genuinely needed.
- **L1–L3 and L5.** I re-derived each by hand from the class table and found them correct.

### 6.5 Case analysis

I re-derived each geometric case by hand:
- **(2,2,2) at Z=12.** κ₁=κ₂=κ₃ from the three N₁ equations. For independent normals, b+2h=3κ−11, and κ≤2 follows from E=4−2κ≥0. Equal or complementary normals and dependent normals contradict as stated.
- **(0,4,4) at Z=8.** G₂=G₃=2, C₂=C₃=5−2H, D₁=17+2H, O=17+H. Then |H∪O|≥17 forces Hyp₂=Hyp₃, and |F₂∩F₃|=1+2H is odd, which the flat fact forbids.
- **(2,2,4) at Z=8.** κ₁=κ₂ and A₃+B+F=12, with transversality. A₃+G₃+κ=5 comes from the U₃ energy, and y−w=24−4G₃−2A₃ from ΣW². Placements 1–3 fail on y−w or nonnegativity; placement 4 forces 9B+F=−92. In the independent case A₃+B+E+G₃+2H+f₁₁=1, so κ=4. The sub-case (1,0) needs a quadrant intersection of size 3, and the sub-case (0,1) gives y−w=22 instead of 20.

As an independent cross-check I built an exact nonnegative-integer model with no solver library: a DFS with interval propagation, validated against brute force on 300 random systems. It has one variable per class and t-state region. Each geometric case was solved over **every** region vector realizable by actual affine placements in F₂⁶: 13 vectors for (2,2,2), 59 for (2,2,4) and 48 for (0,4,4). The model relaxes the real hypotheses (signs are omitted), so infeasibility in the model implies infeasibility of the real system. All 16 (m,Z,pattern) cases induced by P1's list are infeasible. The three geometric cases are feasible by counting alone (examples are in the result JSON) and infeasible once geometry is imposed. This agrees with the packet's account; I did not rely on its Z3 runs.

**MINOR findings:**
- **m1.** In the (12,118,12) independent-normals step, "2B+4H=6κ−22<0" silently uses κ≤2, which comes from E=4−2κ≥0. For κ=4 the right-hand side is +2.
- **m2.** For (2,2,4), the stated reason that the s=3 histograms (0,64,0) and (48,0,16) "fail the U₃ energy or ΣWt=256" is inaccurate. Each satisfies all four s=3 local equations: (0,64,0) has the unique local solution N=(0,40,24,0,0), and (48,0,16) has a one-parameter family. They fail only jointly with the s=1,2 counts, the U₀ energy and the quadrant counts:
  - (0,64,0): B+F=24 versus B+F=12;
  - (48,0,16): D₁+D₂=κ+B+2H+6 while N₂^(3) gives D₁+D₂≤3+κ.

  The conclusion is correct.
- **m3.** In L1, "each sum in (3) is ≡#{n_c odd} (mod 4)" holds only for the Σ_cU_s² sums, not for ΣW², Σt² or ΣWt. The conclusion is unaffected.

### 6.6 Are the case splits complete?

| split | status |
|---|---|
| Normal-configuration splits (independent / equal or complementary / dependent; span or not span) | complete |
| Histogram splits (L6) | complete |
| Pattern splits per (m,Z) | complete |
| P1 profile split | **incomplete (M1)**: m∈{114,116} missing |
| Z mod 4 split | complete only through the imported congruence (§6.2) |
| P2 | not a gap, by §6.3 |

## 7. Dependency list

- **Standard facts.** The chain uses the following written mathematical inputs:
  - Lucas' theorem;
  - classification of quadratic forms (zero counts, Walsh support, dual phase), which I checked by enumeration;
  - the RM(r,n) minimum weight 2^(n−r);
  - degree ≤d ⇔ every (d+1)-flat sum vanishes;
  - dimension count for affine-flat intersections, checked in F₂⁵;
  - Parseval and Poisson summation.
- **Parent-adopted caller.** File `info-6-walsh-caller-and-mod4-coupling-parent-v1.md`, SHA `721222262af9…`, outside the manifest and not read. Its caller facts were re-derived in §3. The congruence **E₂+2n₃≡0 (mod 4)** was imported and not reproduced (§6.2).
- **Author-only premises outside the manifest, not read:**
  - `rank2-sparse-sign-exclusion-v1` (`b16317ae852e…`): D≥12 at rank 2, load-bearing for P1;
  - `rank4-mod3-sparse-v1` (`9745f7681788…`): D≥8 at rank 4;
  - `singular-cubic-zero-v1` (`6fba1086e8be…`): P2, discharged by §6.3.
- **Defective conditional premise.** P1, the low-rank list (M1).
- **Pinned data, solvers and author code.** None used.

## 8. Controls and receipts

| file | SHA-256 | bytes | LF |
|---|---|---:|---:|
| `rv-f166-controls-v1.py` | `29ee96a09f75536edb887403d1579ae6699d4520a8606527e02e439628b4dd4b` | 40654 | 835 |
| `rv-f166-controls-v1-result.json` | `8bfe045271de0a6c53509e13898b9663aa9acfd5b989d0f3660715b9b5537ded` | 25760 | 1644 |
| `rv-f166-controls-v1-receipt.json` | `ea91862a59552ac6fb7076db1e9f291ef157884352260425ae813dd20a221f65` | 2640 | 38 |

The control script was written by me and imports only numpy and the standard library. I ran it as `python3 -B rv-f166-controls-v1.py rv-f166-controls-v1-result.json`. Observed clocks: **2026-10-29T08:39:12-0700 PDT** before, **08:43:10-0700 PDT** after, exit 0, reported runtime 237.0 s, Python 3.14.3, numpy 2.4.3. I took the script hash immediately before the run.

**Positive controls:**
- **A.** The seven actual functions: every caller, inverse, polar, Parseval, collective, block, mod-3, L1, Z₈-constancy and residue check is true.
- **B.** Zero counts, Q weights and the rank-four phase facts.
- **C.** The enumerator reproduces the packet's 17/50 profiles exactly once the disclaimed filter is added.
- **D.** The L4 family, the τ geometry and the flat fact.
- **E.** The solver matches brute force, and the geometric cases are feasible by counting alone.
- **H.** deg≤5 at rank ≤2.

**Negative controls, each failing for the intended reason:**
- **A.** A balanced T=0 function has no odd half. The perturbed formal spectrum has a non-integral inverse and breaks coset constancy in 60/60 trials, and a +4 block perturbation makes U_s non-integral.
- **C.** The explicit counter-profile.
- **D.** A one-point intersection of two 3-flats in F₂⁶.
- **E.** Every P1-list case is infeasible once geometry is imposed.
- **G.** E₂ parity is not determined.
- **H.** Rank-6/8 functions reach degree 6.

## 9. Deviations and process notes

- **Exploration in memory.** Before writing the saved script I explored in an in-memory Python kernel, which wrote no files. Two exploratory cells were interrupted by their cell time limits: an early unvectorised τ loop at 30 s, and a gap enumeration for m=114/116 at 2400 s. Neither partial output is used. Every number cited here comes from the saved result JSON and receipt, or from the hand derivations shown above.
- **File mode.** The write tool set the executable bit on `rv-f166-controls-v1.py`.
- **No pycache.** I used `-B`, so no pycache was created.
- **Not opened or used.** Z3, web search, external models, Git, author contact, author checkers and receipts, and every out-of-manifest source were all left unopened or unused. No named primary source was needed.
- **Unrelated safety notices.** I received two status-only safety notices about the f162 (Olson) and f161 episodes. I accessed no material from either.
- **Writes.** I wrote only uniquely prefixed `rv-f166-*` files and this review, all in this directory.

## 10. Summary

The mandatory corrections are correct, and the reviewed sources do not rely on the withdrawn divisor-8 lemma, the odd common-top total, or the incomplete D28 Q-weight list. The collective packet's results hold as written: rank 0 is impossible, rank 2 forces z=64, rank 4 forces z=96, together with the D/m constraints. The coset packet's local lemmas and case analysis are correct for every (m,Z) induced by m∈{118,120,122}; I reconstructed them by hand and confirmed them with an exact relaxation over all affine placements. Its P2 premise (Z≥8) follows independently from a degree-≤5 argument at rank ≤2.

The chain nevertheless fails to exclude even-polar rank two. The low-rank packet's rank-two list does not follow from its stated constraints, which also admit m=114 and m=116, for example (12,114,−4,12,0,120,124). The claimed lists coincide exactly with the output of the relation m≡1−D (mod 3) that the packet itself disclaims, and the coset analysis does not treat the missing profiles. Two further premises remain imported and unverified here: the parent congruence (E₂ even) and the out-of-manifest D≥12 premise.

Verdict: FATAL 0, MAJOR 1 (M1, which also makes the chain conclusion unsupported), MINOR 3. This is same-harness evidence only, not human, independent-family, formal or novelty verification.
