# Independent hostile review: UH-CONSTRAINTS v1

**Texts reviewed:**
- `proof-UH-CONSTRAINTS-v1.md` (56327b67…, L1–266), cited as **P**n.
- `obstruction-UH-EXCL-v1.md` (f2f1a232…, L1–138), cited as **O**n.
- Parent erratum v1 (8f1ea491…) is applied, then final erratum v2 (ac2a7f26…) last.

**Method:** written mathematics only. I used no tools, computation, enumeration, edits, delegation or launches. I did not recompute manifest hashes or byte counts, and I did not read the checkpoint files.

**Overall:** the outcome is O3 only. None of the six scoped results has a FATAL or MAJOR finding. UH-EXCL is not closed.

## Verdicts

| Result | Verdict | FATAL | MAJOR | MINOR |
|---|---|---|---|---|
| UH-A (P117–149) | **ACCEPT** | 0 | 0 | none required |
| MW (P151–172) | **ACCEPT** | 0 | 0 | none required |
| SH (P174–189) | **ACCEPT** (editorial S1, S2) | 0 | 0 | 2 |
| L (P191–213), explicit δ=0 | **ACCEPT** (editorial L1) | 0 | 0 | 1 |
| PH (P215–225), pure words with α_h ≥ p only | **ACCEPT** | 0 | 0 | 0 |
| E (P227–235) | **ACCEPT** with v2 #1 applied; without it, ACCEPT-WITH-FIXES at P234 | 0 | 0 | 0 |

The obstruction note, with v1 and v2 applied, is acceptable as an O3 record. It has no FATAL or MAJOR finding, but needs five further MINOR wording fixes that neither erratum covers (OB1–OB5).

## Per-result verification

### UH-A — ACCEPT

**SR.** All l_i are odd, so δ_GRX = #{f_i=0} = p+1−Φ and C_max = Φ+2(e−1). Setting n = 2p−C gives exactly max(0, 2κ+2−2m) ≤ n ≤ min(2p−2m, R), with n even. GRX already licenses every even C in [Φ, C_max]. The block-pair realisation is explanatory only and independent of how H is distributed or which runs are empty.

**Lemma P.**
- n = max(p−1, 2κ+2−2m) lies in SR: n ≤ 2κ, and n ≤ 2p−2m follows from 2m ≤ p+1 and κ ≤ p−1.
- Suppose μ ≤ 2κ. Then R−μ ≥ p−1, and 2(p−1) ≤ R holds because κ ≥ (p−1)/2.
- So Lemma M gives p−1 unequal pairs, with 0 ≤ n−p+1 ≤ 2κ−p+1 fillers.
- RS(b) with K=p−1, applied to the nonzero d_i, then gives all p residues.

**Lemma U.**
- 2(2κ+1) > R holds because 2κ > p−3.
- The case a=0 is refuted by the pigeonhole arc: m=1, T = y_j′−y_j = 0, at n = 2κ ≤ min(2p−2, R).

**Basic bounds.**
- A′ ≤ κ: use the all-plus pattern at n = 2κ+2.
- A ≤ 2p−1: use n = 2p when R ≥ 2p.
- Hence b ≥ p−2e and δ ≤ p−2.

**Window W.**
- φ_a = A−d and φ_−a = A′+d.
- λ = p−2−b and Λ = 2κ+1−A′, with d(all) = λ+Λ.
- g = p−2e+3+δ and λ ≤ 2e−2.
- Lemma H: g > λ is equivalent to b+δ ≥ 2e−4. Its first-passage argument uses only proper prefixes and singletons.
- Lemma D: A ≥ 2Λ is equivalent to A′ ≥ p−2e+3+δ. It is a sufficient condition only.
- Light sets give λ ≥ 0 and at most p−2 nonempty runs besides h.

**Branches.** Since 2e ≤ p+1, b ≥ p−3 implies b+δ ≥ 2e−4, so a high run h exists.
- b ≥ p−1: A ≤ 2κ < 2Λ, so light sets hold, and λ ≤ −1 then forces A′ ≥ p. Contradiction.
- b = p−2: A = 2κ+1 < 2Λ, so there are at least two empty runs.
- b = p−3, two high sets: the chain A ≥ α_h+α(P₂) ≥ 2Λ ≥ 2κ+2 = A is tight. This forces A′=κ, β_h = β(P₂) = 0, no a-letters outside, and δ = e−3.
  - W with (λ, Λ) = (1, κ+1) on {h}∪S gives β(S) ∈ {0} ∪ [κ, ∞), so all −a letters lie in one run.
  - On subsets of Q, each α_i is 1 or at least κ+1. There is at most one 1 (since κ ≥ 3) and at most two large values, so at most two runs contain a.
  - Hence at most e runs are nonempty, so at least κ+1 are empty.

**Residues.** The E-family equals all of G exactly when b ≤ n ≤ A.
- b = p−2:
  - n = 2κ is free.
  - n = 2κ+2 = A+1 is admissible at m=1 and allows exactly the nonempty J.
  - With |M| ≤ 1, this forces τ_i = −(2e−2)a and M = {2a}.
  - For an empty pair at n = 2κ (m=1, or m=2 since 2κ ≤ 2p−4) we get 2(e−1) ≡ 0 mod p. That is impossible because 4 ≤ 2e−2 ≤ p−1.
- b = p−3:
  - v = (2e−2)a ∈ M.
  - τ_i+2ea and τ_i+v differ by 2a, and τ_i+v ≠ v. So τ_i = −2a and M = {(2e−2)a, (2e−4)a}.
  - For an empty pair at n = 2κ+2: this length is ≤ 2p−4 iff e ≥ 3, tight at e=3. It then forces 4a = 0 or 2a = 0. Contradiction.

**Endpoints checked:**
- p=7 with κ=3 and κ=4; e=3; κ=(p−1)/2, where 2κ = p−1 ≥ b in both branches.
- ρ_0 as a deviant, where ω = −a ≠ 0.
- Adjacent versus separated empty runs; H in one block versus spread across blocks.

Optional notes: the "(e≥3)" at P140 is more than needed (κ ≤ p−2 suffices). P131 could name the "one large run plus one singleton" case explicitly.

### MW — ACCEPT

- **Length range.** K = R−n, and R is even. K_max = p−3+2m ≤ R because 2m−2 ≤ p−1 ≤ 2κ; this is implicit at P159.
- **Occurrence bounds.** w0 ≤ K ≤ φ gives 0 ≤ K−|J| ≤ φ. On the selected side:
  - |Jᶜ| ≤ n is equivalent to K−|J| ≤ φ.
  - n−|Jᶜ| ≤ φ is equivalent to |J| ≤ K.
  - So both occurrence bounds are retained, as P164–166 says.
- **Count.** |𝒦| ≤ e < p, so s𝒦 is an arithmetic progression of q distinct residues (s ≠ 0). RS(b) with K = w0 and nonzero ω, together with CD, gives at least min(p, w0+q) residues. The cases q=0 and s=0 are correctly excluded.
- **m = e with 3e ≤ p+2.** K = p−1 lies in 𝒦 because φ ≥ 2κ+1 ≥ p, so q ≥ 1.
  - If w0 ≤ 2κ+2−2e, then q = e and w0 ≤ κ−1.
  - Otherwise q = κ+1−⌈w0/2⌉, which forces w0 ≤ 2e−3. That is below 2p−4e+3 exactly when 3e ≤ p+2, so this branch is empty.
  - The two branches are exhaustive, so MW-e holds.

### SH — ACCEPT

- **Thresholds.** The low and high thresholds are κ−1−b and p+κ−A′, with gap p+1+δ. Complementing a set keeps m and swaps the two types.
- **Toggle path.** I checked it step by step, including e=3.
  - P0 has e intervals iff N ≥ 2e.
  - Every later step keeps e intervals provided the first addition does not join 0 to 2e−2. That needs only N = p+1 ≥ 2e+1, and in fact N ≥ 2e+2.
  - All intermediate sets are proper and nonempty, and the path ends at the complement of P0.
- **The jump.** A deletion is impossible, since −d_i ≤ β_i ≤ A′ ≤ κ. So the jump adds a run h with d_h ≥ p+1+δ.
- **Light sets.** A disjoint ordinary-high set P′ would give 0 ≥ 3+2δ. So light sets hold, λ ≥ 0, and there are at least two empty runs. No exclusion is claimed.

### L (explicit δ=0) — ACCEPT

**Attainable interval.**
- ε = A′+d lies in [0, p−2].
- For n = 2ν with ν ∈ [κ, p−1], the attainable values are x ∈ [ν−ε, min(ν, R−ε−ν)]. This uses ε < 2κ ≤ 2ν.
- These intervals are nonempty and consecutive ones touch.
- Their union is [κ−ε, U]. The bound ⌊(R−ε)/2⌋ ≥ κ follows from φ_a ≥ 2κ+1.

**Size and lift.**
- If U = p−1, then ε ≤ 2κ−p+1 ≤ κ−2, so the size is e+ε ≤ p−2.
- Otherwise the size is ⌊(p+1+ε)/2⌋ ≤ p−1.
- Either way the integer lift is unique in [U+1−p, κ−ε−1].

**Additivity.** ε₁+ε₂ = ε+A′.
- Upper bound when U = p−1: uses 2κ−A′ ≤ p, from A′ ≥ 2κ−p.
- Upper bound otherwise: needs e−ε−3 < ⌊(p−1−ε)/2⌋, which follows from 2e ≤ p+1.
- Lower bound when some U_j = p−1: U₁+U₂ ≥ p−1+κ.
- Lower bound otherwise: U₁+U₂ ≥ 2κ+p−2−(ε+A′)/2 > p+κ−ε−3.
- So |D| < p, hence D = 0.

**Arithmetic illustration (no existence claim).** Take p=7, κ=3, A′=2. An empty run has ε=2 and U=5, so its lift lies in [−1, 0] and is forced to be −1. This confirms O99–101: empty-run lifts can be negative.

### PH — ACCEPT (pure words with α_h ≥ p only)

- After orientation, A = R and A′ = δ = 0. Then A ≤ 2p−1 forces κ = (p−1)/2, R = 2p−2 and λ = p−2.
- Every arc avoiding h is low, with U = p−1−⌈α/2⌉. So −⌈α/2⌉ ≤ X ≤ (p−3)/2−α.
- D = X+α/2 is additive and at least −½ on each piece; empty runs have X ≥ 1.
- Therefore (E−1)/2 ≤ D(all) ≤ (α_h−p−1)/2, giving E ≤ α_h−p.
- But E ≥ α_h−p+2. Contradiction.

### E — ACCEPT (with v2 #1 applied)

- **What (E) is.** For empty-negative patterns, (E) is an exact restatement of avoidance at length n. Every n-subset of rotations is J together with n−|J| a-letters, so the displayed family equals Σ_n(X)−na.
- **M bounds.** |M| ≤ max(0, p−1−b) and 0 ∉ M are correct.
- **v2 #1 verified.** After UH-A, b ≤ p−4 < p−3 ≤ 2κ−2.
- **Why the general bound still matters.** The general |J| ≤ n bound remains substantive for three pairwise non-adjacent empty runs. There m=3 allows n = 2κ−4, which equals p−5 < b = p−4 at κ = (p−1)/2, c = 3. This supports keeping both bounds in general.

## Findings: exact line, gap, minimal repair

| ID | Sev | Line | Gap | Minimal repair |
|---|---|---|---|---|
| S1 | MINOR | P35–36 | Says "every set of runs avoiding h is low", but W is defined only for proper nonempty sets (P188 correctly says nonempty). | Insert "nonempty". |
| S2 | MINOR | P177, P179 | The SH thresholds L and U collide with Lemma U (P87), Proposition L and (L) (P191, P203), and U(P) (P194). n is reused as the run count. D (P108/161/207/220) and q (P73/156/198) are also overloaded. | Rename to L_e, U_e and N; the other renames are optional. |
| L1 | MINOR | P201 | In the U = p−1 branch, the size bound e+ε ≤ p−2 is left implicit. | State it. |
| G1 | MINOR | P20–23 | "Word formulation implies the NF formulation" is worded backwards. What is used is that the NF antecedent supplies such a u; equivalence holds because such a u is its own admissible NF. | Rephrase: "results proved for any such u apply under the NF antecedent". |
| G2 | MINOR (admin) | P10, P12, P242 | The "pending" status of PP1-EXCL and ROT-PP1 is stale (package §3; ROT-PP1 erratum v2). Neither is used. | Write "not used, whatever its status". |
| R1 | optional | P29; O30–31 | b ≥ p−2e is slack at e = (p+1)/2, since b ≥ 0 and so c ≤ p−1. δ ≤ p−2 is slack, since δ ≤ b ≤ p−4. Both are true, and nothing stronger is assumed. | Optionally tighten. |
| OB1 | MINOR | O47–48 | "No … unknown external datum that could be substituted for its proof" is an unsupported claim about methods. It conflicts with v2 ("other methods or mathematical input are not excluded"), and for each fixed p R-UH is a finite statement. | Replace with: "This packet does not reduce R-UH to any numerical evaluation or external datum; none is used, and nothing is claimed either way about whether one could suffice." |
| OB2 | MINOR | O89 | "At c=1,2 … plus one restricted non-free length" is inaccurate: c=1 used the non-free length n=A+1, while c=2 used free lengths only. | State each case separately. |
| OB3 | MINOR | O92–94 | "The missing local step is X OR Y" reads as exhaustive. | "Two possible completions of this route are X and Y; other routes are not excluded." |
| OB4 | MINOR | O119 vs P40/P225 | "All runs ≤ p−2" versus "every run < p" looks like a gap at runs of size p−1. There is none: in the pure case λ = p−2 and Λ = p, so W forbids any proper nonempty set with exactly p−1 letters. | Add that one sentence. |
| OB5 | MINOR | O129–130 | "o_F ≤ p cannot be supplied at k=p+1" reads as an impossibility claim. | "Is not supplied by any accepted interface." |

## Parent errata: all verified

- **v1 #1 (O32, O52).** The correct value is λ = A−2κ−1 = p−2−b = c−1. The correction is necessary, not cosmetic:
  - With c−2, R-UH would assume "d ≤ c−2 or d ≥ Λ", which is stronger than the proven W.
  - R-UH would then miss avoiders that have some d(P) = c−1, so proving it would not complete UH-EXCL.
  - With c−1, O53 (g > λ ⇔ b+δ ≥ 2e−4) is consistent.
- **v1 #2 (O85).** Correct: 2κ−2 ≥ p−3 > p−4 ≥ b, so the j = −1 length is free.
- **v2 #1 (P234).** Correct; see E above.
- **v2 #2 (O42).** Correct. UH-A together with R-UH implies UH-EXCL, but R-UH is essentially the target restated on the residual, and nothing shows it is minimal.

The set interface at O78–86 re-derives correctly after v1 #2:
- A free length n = 2κ+2j satisfies n ≤ A iff j ≤ μ = ⌊c/2⌋.
- −(2κ+2j)a ≡ (2e−2j)a.
- The four forced families and the m=2 cap j ≤ e−2 are as stated.
- 1 ≤ μ ≤ e−1, |M| ≤ c, and M = σ(ω(B))−M.

At O108–111, the RS(b) step survives capping, because Σ_x min(p−1, v_x) ≥ min(p−1, total).

## Failed-route and checkpoint dispositions (O §5–6)

All six dispositions are consistent with the mathematics shown. I checked them only against that mathematics, because the checkpoint files are not in the packet.

| Line | Disposition | Check |
|---|---|---|
| O117–119 | Using U = p−1 for every low arc was wrong. | Agrees with L: U(P) < p−1 whenever ε > 2κ−p+1. |
| O120–121 | "Two high sets impossible iff δ ≥ e−2" was too strong. | Lemma D gives sufficiency only. At b = p−3 the window inequalities alone allow two disjoint high sets at δ = e−3; only the residue step refutes that branch. |
| O122–123 | The simplified MW band is superseded. | Correct. |
| O124–126 | The "⌊c/2⌋+2 elements of M" bound is withdrawn. | Correct. Only \|M\| ≤ c and the forced families remain. |
| O127–128 | No FLEXa/PM* expansion is used. | Correct. |
| O129–130 | RGR, ASSEMBLY and RPδ are context only. | Correct; see OB5 for the wording. |

No count model is presented as a word (O7, O39–40). There is no tacit gain in cell count, and no κ cell is claimed excluded.

## Label audit

- **[RE-DERIVED].** Accurate. M, P, U, W, H, D and the light-set count are all re-proved in-file. H and D are correctly weakened to conditional ("tracked") forms compared with ROT-PP1 Steps 5–8.
- **[NEW].** For UH-A, MW, SH, L and PH this means new within this packet only; no novelty claim is made.
- **"WHOLE upper-half κ interval" (P25).** Accurate: the A-subcase is excluded at every κ. P30–31 qualifies this immediately.
- **"EXACTLY" (P195), "UNIQUE" (P202), "exact" (MW, E).** All supported by the proofs.
- **E's "[NEW statement]".** This is bookkeeping rather than new content; optional relabel.
- **Package §4 item 4.** "Dominant fillers" is looser than P153, where s is any nonzero value. This is package wording only.

## Import audit (separate)

| Interface | Used at | Scope check |
|---|---|---|
| NF: ROT-few-E-v4 L28–43, ZX overlay 2 (existential), lowodd item 2 / M1 | Sec. 0 antecedent: avoidance, same rotation multiset, k=p+1 odd blocks, empty-run rule (L38), κ̂ formula (L42) | Only Sec. 0 is used. The REFL(p) condition at fewodd addendum L12 belongs to SHgen-E and is not imported. DAV, K1 and overlay 3 are not needed. ✓ |
| GRX "if" direction: notes-GRX L7–20, lowodd item 1 / M2 | SR (P58–68), every pattern | The group law at P46 matches M2. Patterns with z₁ = −1 are covered by global sign reversal (GRX L20, M2). Empty runs are allowed. ✓ |
| RS(b): ROW L16–27 with R5 | Lemma P (K=p−1); UH-A and E (K=b); MW (K=w0); O110 (K=p−1) | Every use has integer K ≥ 0 and nonzero terms. ✓ |
| CD (classical) | MW sumset | Nonempty sets, p prime. ✓ |
| Elementary | Lemma M (proved at P73–77), pigeonhole, complement symmetry (O73) | ✓ |

No other theorem is used anywhere. CT, Lev, S(p), (S1), REFL, RPδ, ASSEMBLY-P, RGR-LONG/RUNS, PP1-EXCL, KP2-EXCL, ROT-PP1/TOP, endpoint candidates and code are all absent. The ROT-PP1-v2 excerpts are context only, and every step taken from them is re-proved. The "(ZP_κ)" identification at P68 is an unused remark whose definition is not in the packet.

## Original target: NOT closed

**UH-EXCL is not proved.** No (p, κ) cell is excluded. UH-A only rules out A ≤ 2κ+2, and the packet names this restriction explicitly, so the O3 outcome involves no silent substitution.

**Any remaining avoider with the full antecedent must satisfy:**
- A = 2κ+c with 3 ≤ c ≤ min(2e−1, p−1), and b = p−1−c;
- A′ ≤ min(κ, b);
- the window W with λ = c−1 and Λ = 2κ+1−A′;
- MW for every pattern;
- the SH structure, when 3e ≤ p+2.

**What stays open:** R-UH, in the v2 "remaining" sense (not "smallest"). The route gaps are:
- H applies only when b+δ ≥ 2e−4;
- D is a sufficient condition only;
- SH applies only when 3e ≤ p+2;
- the empty-run residue coupling for c ≥ 3 is unresolved;
- L needs δ=0 and a path whose subarcs are all low;
- PH covers only pure words with α_h ≥ p; pure words whose runs are all ≤ p−2 remain open.

The scope's O3 requirement of a "smallest missing claim" is met only in the weaker "remaining claim" form after v2.

## Not approved

This review approves none of the following:
- the whole UH-EXCL, or the lower range 1 ≤ κ < (p−1)/2;
- other values of k or κ̂;
- o_F, assembly, REFL or INV*;
- full ordered Olson, or p = 5;
- any existence or non-existence claim outside the stated antecedent;
- novelty, priority, Lean or human-review status.
