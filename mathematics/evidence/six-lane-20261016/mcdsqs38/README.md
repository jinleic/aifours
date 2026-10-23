# mcDSQS(38) — six-lane round 2026-10-16 (math-1, third target)

Lane owner: worker `MathMcDsqs38`. Frozen contract (read-only):
`institute/runs/six-lane-2026-10-16/screening/math-1-mcdsqs38-contract.json`
(recorded 2026-10-17T02:54:44-07:00). Prior lanes `../kirkman57/`, `../rdsqs52/`, `../olson/`
are read-only; code patterns from `../rdsqs52/code/` are copied/adapted into `code/` here.

## 0. Headline (2026-10-17, host clock)

**An explicit mcDSQS(38) was constructed and checked by two independent lane programs**
(candidate; not peer reviewed; parent verification, priority audit and review pending).
Certificate `evidence/mcdsqs38-g342/mcdsqs38_g342_s0.txt`, sha256
`973f93e4646e48df64b70b3a64811afcdc87b10a1767222f54ffe65d3a303f1c` (2109 blocks; all 38
colourings explicit, 19 classes each, class sizes 12¹⁸6 at every point). Checks: lane Python
(stdlib) checker PASS under Python 3.14.3 and 3.9.6, lane C checker PASS, 15/15
intended-reason mutations (both checkers), symmetry audit PASS, byte-exact regeneration from a
3.5 KB seed with the stdlib expander, byte-exact re-run of the search. Construction: SQS(38)
invariant under the twisted affine group G = ⟨y+2, 3y+1⟩ ≤ AGL(1,Z38) (|G| = 342,
stabilizer ⟨9⟩), derived design at 0 coloured ⟨9⟩-invariantly, transported by G
(`sources/construction-g342.md`). Representation R1b (§3), experiment E6. The contract's
first ansatz Z38⋊⟨3⟩ admits no SQS(38) at all (E0), and no colouring can be invariant under
−1 (Lemma A).

## 1. Frozen target (written 2026-10-17 03:06 PDT host clock, before any search)

Find a set B of 4-subsets ("blocks") of X = {0,…,37} such that

1. every one of the C(38,3) = 8436 three-subsets of X lies in exactly one block
   (so |B| = 2109: B is an SQS(38)); and
2. for **every** x ∈ X, the derived design B_x = {b∖{x} : x ∈ b ∈ B} (222 triples on
   X∖{x}, an STS(37)) is partitioned into **exactly 19** colour classes, each a partial
   parallel class (pairwise point-disjoint triples). A class need not cover X∖{x}; class
   sizes are not prescribed (each is ≤ 12 since 3·13 > 37).

19 = χ′(37) by Tan–Zhou (1.1) (v ≡ 1 mod 6, v ∉ {7,13}); also 19 = ⌈222/12⌉, so 19 is
optimal. Success = an explicit labelled certificate listing all 2109 blocks **and all 38
colourings explicitly** (19 labelled classes each), accepted by direct definition-based
checkers that assume no symmetry. A restricted-model non-find, UNSAT under a prescribed group,
or a timeout is **not** nonexistence of mcDSQS(38).

Elementary counting used only as sanity checks (Lemma C, §3): in a 19-colouring of an
STS(37) every point lies in 18 triples in 18 distinct classes, so it is missed by exactly one
class; class c misses 37 − 3|c| ≥ 1 points; Σ_c (12 − |c|) = 228 − 222 = 6.

## 2. Primary status (lane reading; parent priority audit separate)

* Tan–Zhou arXiv:2503.11934v1, local read-only copy
  `../../../kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt` (sha256 `df52a8f1…c8164`):
  definitions lines 78–134 (derived design, r-colouring = partition into r PPCs, χ′,
  mcSTS, mcDSQS); §4(1) lines 1108–1110: "Find more examples of mcDSQS(v)s, for example, an
  mcDSQS(38) and an RDSQS(52) (the smallest unknown mcDSQS(6n + 2)s …)". Known small
  mcDSQS(6n+2): mcDSQS(20) (Shi–Xia–Krotov [16], cyclic SQS(20) of Phelps [14]) and the
  cyclic mcDSQS(26), mcDSQS(32) with explicit base blocks and colourings at 0 (Lemma 3.4,
  Appendix B, lines 1277–1372). The lane has no local copy of [16]/[14].

## 3. Frozen representation R1, lemmas, experiments, stop rules

**Points and groups.** X = Z38. For M ≤ U(38) = ⟨3⟩ ≅ C18 let G_M = {y ↦ m·y + b : b ∈ Z38,
m ∈ M}. Subgroups: ⟨3⟩ (18), ⟨9⟩ (9, = {1,5,7,9,11,17,23,25,35}), ⟨31⟩ = ⟨−7⟩ (6), ⟨7⟩
(3, = {1,7,11}), ⟨−1⟩ (2), {1}. Every multiplier m ≠ 1 fixes exactly {0, 19}.

**SQS (Kramer–Mesner).** Columns = G_M-orbits of 3-subsets, rows = G_M-orbits of 4-subsets
whose development covers every triple of each triple orbit it meets exactly once (computed
from orbit sizes in the lane code). Exact cover by kissat; samples by kissat seeds with
blocking clauses on the selected rows.

**Colouring at 0.** D0 = B_0 on X∖{0}, sought invariant under R ≤ M (R fixes 0 and 19).

* *Lemma A.* If an STS(37) has an involution σ with exactly one fixed point p, no
  19-colouring is σ-invariant. Proof: for x ≠ p the triple through {x, σx} is σ-fixed, so its
  third point is p; these are the 18 triples through p. A σ-fixed triple contains 1 or 3
  fixed points, so it is one of them. Each class containing a triple through p is fixed by σ
  (it contains a σ-fixed triple), and the unique class missing p (Lemma C) is fixed. In a
  class through p, σ fixes exactly one triple and pairs the others, so its size is odd, ≤ 11;
  the class missing p has no σ-fixed triple, so even size ≤ 12. Total ≤ 18·11 + 12 = 210 < 222. ∎
  In Z38, −1 fixes exactly 0 and 19, so **R ∌ −1**: R ∈ {⟨9⟩, ⟨7⟩, {1}} (the contract's C18
  option is empty in this representation).
* *Lemma B (class structure, lossless).* The 18 triples of D0 through the anchor 19 lie in 18
  distinct classes; the remaining class F misses 19 and is R-invariant. Classes ↔ anchored
  triples; the i-th R-orbit of anchored triples (sorted) is forced into the representative
  class of class orbit i at the identity coset; class-orbit stabilizer = anchored-triple
  stabilizer. R (odd order) acts freely on X∖{0,19}, so class orbits are [1, 9, 9] for
  R = ⟨9⟩ and [1, 3^6] for R = ⟨7⟩. For R = ⟨9⟩ counting forces |F| = 6 and all other
  classes of size 12 (|F| + 9a + 9b = 222, |F| ≤ 12); nothing else about sizes is imposed.
* *Lemma D (M ∋ 7).* Every block through a triple x·{1,7,11} (x ∉ {0,19}) is completed by 0
  or 19; translation by 19 pairs the unit coset u·{1,7,11} with the even coset
  (u+19)·{1,7,11}, exactly one of each pair completed by 0. Hence D0 contains exactly 6 such
  pairwise disjoint triples; with R = ⟨9⟩ these form F.
* Model: variables = (R-orbit of triples, class orbit k, coset of R/R_k) with the orbit's
  stabilizer ≤ R_k and no point clash inside the placed sub-orbit; exactly one placement per
  triple orbit; **at most one** triple per (representative class, point) (partial classes).
  R = {1}: plain 19-colour model with the same anchored labelling (18 anchored + 1 free class).

**Transport.** Translations y ↦ y + b are automorphisms of every G_M-invariant SQS and act
regularly on X; the colouring at x is the translate by x of the colouring at 0. The lane
audit checks (i) B is a union of G_M-orbits and (ii) every POINT section equals the
translate. The certificate lists all 38 colourings explicitly; checkers use no symmetry.

**Experiments (in order; each with recorded seeds, CNF hashes, caps):**

* E0: KM inventories for M ∈ {⟨3⟩, ⟨9⟩, ⟨31⟩, ⟨7⟩, ⟨−1⟩, {1}} and KM satisfiability.
* E1 controls/calibration (before E2): (a) Tan–Zhou mcDSQS(26), mcDSQS(32) transcribed from
  Appendix B (colouring at 0 + translation) → both lane checkers PASS; intended-reason
  mutations; (b) the same pipeline at v = 26 (M ∋ 9, R = ⟨9⟩, anchor 13) and v = 20, 32
  (R = {1}; U(20), U(32) are 2-groups, so Lemma A leaves only R = {1}).
* E2 main: M = ⟨3⟩, R = ⟨9⟩, anchor 19; ≤ 200 KM samples, colouring cap 60 s each.
* E3: M = ⟨9⟩, R = ⟨9⟩ (same caps).
* E4: M ∈ {⟨3⟩, ⟨31⟩, ⟨9⟩, ⟨7⟩}, R = ⟨7⟩; ≤ 100 samples each, colouring cap 300 s.
* E5: R = {1} on sampled G_M-invariant SQS, cap 600 s each (calibrated by E1b first).

**Stop rules.** First certificate passing both lane checkers → stop searching, pin it, run
mutations, seed/expander, symmetry audit, byte-exact replay, and report its SHA to the parent
immediately. If R1 is exhausted within these caps, freeze R2 here **before** searching it
(planned: 1-rotational X = Z37 ∪ {∞} under Z37 ⋊ C, C ≤ F37*, colourings at ∞ (anchor 0) and
at 0 (anchor ∞) invariant under odd-order R ≤ C). UNSAT/UNKNOWN remain scoped to the model.

**Resources.** ≤ 4 CPU workers, ≤ 8 GiB RSS, checkpoints ≤ 30 min, chunks ≤ 3 h, first cycle
≤ 2 h; all files in this lane (deadline of the round 2026-10-18 18:31:43 PDT).

### R1b — frozen 2026-10-17 03:24 PDT host clock, before any R1b search (after the E0 KM UNSAT)

**Why:** E2/E3 are void (no SQS(38) admits Z38⋊⟨3⟩ or Z38⋊⟨9⟩), and Lemma A forbids −1 in
R. The point-transitive subgroups G of AGL(1,Z38) = Z38⋊U(38) are Z38⋊H and the *twisted*
groups G_{H,φ} = {y ↦ m·y + b : m ∈ H, b ≡ φ(m) (mod 2)}, φ: H → Z2 a nontrivial
homomorphism (proof: |G| ≥ 38 forces G ∩ Z38 ∈ {2Z38, Z38}; if 2Z38, b mod 2 is a
homomorphism of the multiplier image H, nontrivial iff G is transitive). For H ≤ ⟨3⟩ this
leaves H ∈ {⟨3⟩, ⟨31⟩, ⟨−1⟩} with φ(3^k) = k mod 2; they contain only the even translations:

* G_{⟨3⟩,φ} (order 342; generators y+2, 3y+1; stabilizer of 0 = ⟨9⟩; contains y ↦ −y+19,
  which swaps 0 and 19);
* G_{⟨31⟩,φ} (order 114; generators y+2, 31y+1; stabilizer of 0 = ⟨7⟩);
* D19 (order 38, regular; generators y+2, −y+1).

KM over G-orbits exactly as in R1; colouring of D0 invariant under R = G_0 (anchor 19,
Lemma B unchanged: class orbits [1,9,9] with |F| = 6 and 18 classes of 12 for R = ⟨9⟩;
[1,3^6] for R = ⟨7⟩); Lemma D holds (y ↦ −y+19 pairs x·{1,7,11} with (−x+19)·{1,7,11}), so
for R = ⟨9⟩, F is the forced set of 6 triples x·{1,7,11} in D0. Transport: colouring at x =
g(colouring at 0) for the least g ∈ G (sorted image tuples) with g(0) = x; valid because G
preserves B (audited) and is transitive. Experiments: E6 G_{⟨3⟩,φ}, R = ⟨9⟩, ≤ 200 KM
samples, colouring cap 60 s; E7 G_{⟨31⟩,φ}, R = ⟨7⟩, ≤ 100 samples, cap 300 s; E8 D19,
R = {1}, cap 600 s. Stop rules and caps as for R1; non-finds are scoped to R1b.

## 4. Results log

Times are file mtimes (PDT) unless marked "host clock".

| Completed | Experiment | Outcome |
|---|---|---|
| 10-17 03:13–03:15 | E1a controls (`code/tanzhou_controls.py`, `controls/`) | Tan–Zhou mcDSQS(26) (sha256 `5516ebf9…7ca1`) and mcDSQS(32) (`70e6df5c…0b87`) transcribed from Appendix B: Python and C checkers PASS; 15/15 intended-reason mutations each (both checkers) |
| 10-17 03:16 | E1b pipeline calibration v=26, R=⟨9⟩ (order 3), anchor 13 (`runs/e1b/`) | M=⟨7⟩ (all U(26)): all 4 KM solutions coloured, 4/4 PASS; M=⟨23⟩: 4 PASS, 4 UNSAT; M=⟨9⟩: 8/8 PASS; 0.03–19 s; profiles [8¹²,4] and [8⁹,7⁴] |
| 10-17 03:17 | E0 KM inventory v=38 (`runs/e0/km_inventory_v38.json`) | Z38⋊⟨3⟩ UNSAT (14 cols/51 rows), ⟨9⟩ UNSAT (26/157), ⟨31⟩ UNSAT (42/222); ⟨7⟩ SAT 0.6 s (78/570); ⟨−1⟩, {1} UNKNOWN at 120 s |
| 10-17 03:19:44 | E0 cross-check (`code/km_crosscheck.py`, stdlib Algorithm X, `runs/e0/km_crosscheck.txt`) | exhaustive: ⟨3⟩, ⟨9⟩, ⟨31⟩ have 0 exact covers (same col/row counts); v=26 ⟨7⟩ has 4 = kissat enumeration. **No SQS(38) is invariant under Z38⋊⟨3⟩, ⟨9⟩ or ⟨31⟩**, so E2/E3 are void; in R1 only M=⟨7⟩, R=⟨7⟩ (E4) or R={1} (E5) remain |
| 10-17 03:18–03:24:55 host clock | E4 Z38⋊⟨7⟩, R=⟨7⟩, anchor 19 (`runs/e4/m7_r7_b1*`, code hashes in `runs/e4/code_sha256_at_launch.txt`) | 12 KM samples SAT; colourings of samples 0–2 UNKNOWN at 300 s; samples 3–5 killed, 6–11 not run (stop rule, after E6) |
| 10-17 03:24:20 | **E6 R1b: G=⟨y+2, 3y+1⟩ (342), R=⟨9⟩, anchor 19** (`runs/e6/g3phi_r9_b1/`) | KM 26 cols/167 rows SAT ≤0.03 s; **24/24 colourings SAT (0.25–1.94 s), 24/24 certificates PASS both lane checkers**; class orbits [9,9,1]; sample 0 pinned |
| 10-17 03:25–03:29 | hardening of the pinned sample (`evidence/mcdsqs38-g342/`) | Python (3.14.3 and 3.9.6) and C checkers PASS; 15/15 mutations as intended; symmetry audit PASS (group order 342, transitive, G_0=⟨9⟩, every g∈G maps the colouring at 0 onto the colouring at g(0); not invariant under y+1); seed → byte-identical certificate (`runs/seed_replay/`); search re-run byte-identical (`runs/replay_e6_s0/`) |
