# Six-lane math-2: ordered Olson EGZ (lane `olson`)

Lane owner: worker MathOlson. Run contract: `institute/runs/six-lane-2026-10-16/contract.json`
(deadline 2026-10-18 18:31:43 PDT). Prior dossier (read-only):
`mathematics/olson-ordered-egz/` (README, proof.md, HMZ round).
Timestamps below are actual host times (`date`) unless marked "approx"; the lane
directory was created 2026-10-16 ~18:35 PDT (file mtimes), this README first
written 18:57 PDT.

## 1. Frozen target (unchanged quantifiers)

For every finite group G, n = |G|, and every word a_1..a_{2n-1} over G there are
indices 1 <= i_1 < ... < i_n <= 2n-1 with a_{i_1} a_{i_2} ... a_{i_n} = 1
(product in the ORIGINAL index order; no rearrangement).  One finite group and
one length-(2n-1) word with no such increasing n-subword refutes it.

## 2. Primary status recheck (2026-10-16 PDT)

Full query log: [sources/search-log.md](sources/search-log.md).

| Source | What it establishes |
|---|---|
| Open Problem Garden, M. DeVos, posted 2007-03-10 (re-read) | exact increasing-index statement; z(G); only trivial z(G) <= |G|(|G|-1)+1 known to the poster |
| Mohar page (2006), Halasz CanaDAM 2015 abstract | exact ordered statement; "save some special cases ... remains open" (2015) |
| Dimitrov, Math. Balkanica 18 (2004) 129-140 (full OCR: `sources/dimitrov-ocr/`) | ordered statement for all finite p-groups (Thm 2), via modular group algebra D(G x C_n) <= L(G)+n-1; Cor. 2 (soluble) is UNORDERED |
| Agarwal-Lou, IMSA 2016 abstract (re-read by lane and parent) | experimental LOWER bounds only (4m-1 for D_{2m}, m odd; 3m even) |
| Zhao-Wang 2603.21052, Oh-Ribas-Zhao-Zhong 2511.18246, Avelar-Brochero-Ribas 2302.11754, Bass JNT 2007 | Gao constant / Davenport constants with unordered sequences |
| Frick et al. 2310.17065 (FoMS 2025) | topological proof of Olson's UNORDERED theorem (reordering via their Prop. 3.3) |
| EulerSolve index, Zenodo API, openai/math CONTENTS (2026-10-16 19:29-19:30 PDT) | no relevant hit |

No primary source located proving the ordered statement for any non-nilpotent
family.  Status: open as far as located (literature miss is not novelty).

## 3. Baseline

abelian (EGZ 1961); p-groups (Dimitrov 2004); trivial z(G) <= n(n-1)+1; prior
dossier partial results (odd-dihedral one-short word, boundary insertion,
restricted run families).  Parent's separate Codex note (unverified):
z(G) <= (n^2+1)/2 (odd n).  Abelian analogue of the strengthening in Sec. 5.3:
Bollobas-Leader, J. Number Theory 78 (1999) 27-35 (via Grynkiewicz's Caltech
thesis, `sources/grynk-thesis.txt` lines 2836-2850): if 0 is not an m-term sum
of S (|G| = m) then |m^S| >= |S| - m + 1.

## 4. Attack protocol (frozen before substantial computation; unchanged)

A1 finite-exact exhaustive search over ALL words (exact ordered product-set
automaton, exact-key memo, final-horizon pruning, Aut x rotation normalisation);
controls: abelian / p-groups, known one-short avoiders, corrupted-table
rejection; any avoider re-verified by raw subset enumeration in a permutation
representation.  A2 theory: "fixed-twist abelian adjustment" (fix the selected
non-A letters; A-letters then form an abelian subset sum with fixed twists).

## 5. Results so far (evidence levels kept separate)

### 5.1 Finite-exact (computer, exhaustive, all words)

| Group | Words checked | Result | Tool / receipt |
|---|---|---|---|
| S3 (=D6) | all length 11 | no avoider; 126 normalised avoiders at length 10 | `code/olson_dfs.cpp`, `evidence/groups/S3.*` |
| D10 | all length 19 | no avoider; 3730 normalised avoiders at 18 (63 classes under rotation x Aut x reverse-inverse) | same; cross-checked by identity-reduction search `code/olson_dfs_id.cpp` (all e) |
| controls C6, C10, D8, Q8 | all length 2n-1 | no avoider (as theory requires); D8/Q8 have none already at length 12 | same |
| A4, Dic3 (=C3:C4), D12 | length 23 | NO avoider (all words).  D12, Dic3: two independent methods, chunked orbit-normalised DFS (36/36 chunks, coverage set checked exactly) and identity-letter reduction e=11..0 all 0.  A4: identity-letter reduction e=11..0 all 0 (e=0 done, 5438.8 s; direct chunked run not done, single method). Frozen receipt `evidence/runs/order12.freeze.receipt.json` (host 22:20:03 PDT; table validation + order fingerprints, source/binary/table hashes, chunk coverage, brute-force cross-check of the counter at (L,K)=(5,3),(6,4) all equal and nonzero, corrupted-table mutation rejected); earlier snapshot `order12.freeze.receipt.2155.json` (A4 e=0 then running) | `code/olson_dfs.cpp`, `code/olson_dfs_id.cpp`, `code/chunk_driver.py`, `code/receipt_order12.py` |

Identity-letter reduction (proved in the source header of `olson_dfs_id.cpp`):
w with e identity letters avoids iff the identity-free remainder avoids
identity k-subwords for every k in [n-e, n].

### 5.2 Structure of extremal (length 4p-2) dihedral avoiders (finite-exact, p=5)

All 3730 normalised D10 avoiders of length 18 satisfy (checked by script):
* P_{10}(w) = G \ {1} exactly (every non-identity element is an ordered 10-subword product);
* cyclically, w alternates rotation-blocks and reflection-blocks, every block is a
  run of ONE repeated letter of ODD length; rotation letters are r^{+-x};
* every "bracket" (last reflection of a block, following rotation block, first
  reflection of next block) has the same product r^c.
Reduction lemma (written proof, lane): if every length-(4p-2) avoider of D_{2p}
is a cyclic alternation of odd constant blocks, then D_{2p} has NO avoider of
length 4p-1 (every deletion of an avoider is an avoider; block-parity count).
So ordered Olson for D_{2p} <= this inverse statement.  Inverse statement NOT proved.

### 5.3 New conjecture: ordered Bollobas-Leader (OBL)

OBL(G): for every word w over G (|G| = n) with 1 not an ordered n-subword
product, |P_n(w)| >= min(n, |w| - n + 1), where P_n(w) is the set of ordered
n-subword products.  OBL at |w| = 2n-1 is exactly ordered Olson.  Abelian G:
Bollobas-Leader.  Exhaustively verified (all words, all lengths <= 2n-1) for
C6, S3, D8, Q8, C10, D10 (`code/growth_dfs.cpp`; D10: 1.30e9 checked states, 0
violations).  The step form (adding any letter strictly enlarges P_n) FAILS
(e.g. S3, D8, D10), and the all-k "ordered Hamidoune" analogue FAILS in S3 for
k=3 (word c c t t c^2 c^2): OBL is specific to k = n.

### 5.4 Reflection-coset threshold (finite-exact)

All-reflection words in D_{2m}: identity 2m-subword guaranteed at length 3m-1,
not at 3m-2, for m = 3..9 (`code/dihedral_family_dfs.cpp`, WORD_ALPHABET=F).

### 5.5 Theory status

Fixed-twist reformulation for D_{2p} (exact): selection = even set Phi of
reflections + set T of rotations; value = V(Phi) + sum_{i in T} s_i(Phi) x_i with
signs fixed by Phi; equivalently (marked form) value = sum_{gaps in Minus}
beta_t + sum_{marked rotations} x_i, all signs +, sum of all items = 0, with a
twisted size constraint.  Generic words are settled by Cauchy-Davenport with
large slack; the unresolved part is exactly the degenerate (rigid) words, whose
extremal structure is Sec. 5.2.  No complete proof yet.

### 5.6 Proved D_{2p} components (all odd primes p) and exact residual

Written proofs: `proof-theoremP.md` (Theorem P), `proof-dihedral-partial.md`
(Doubling, Davenport-alpha, Theorem R rigid words, Corollary R', dependency map),
`proof-T0.md` (Theorem T0: <= 1 odd reflection run => solution; group algebra
F_p[Z_p x Z_p], rotation nests).  Reviews (cross-vendor at commissioning time,
parent then Claude-family): `review/codex-theoremP/receipt.json` (correct),
`review/codex-T0-R/receipt.json` (T0, Doubling, R' correct; R, Davenport-alpha,
TRI minor fixes, all applied).  Exact residual class with proved count
constraints: `residual-class.md` (>= 2 odd reflection runs, o_F + k_O >= 5).
Ordered Olson for all D_{2p} is NOT proved: the covering argument for the
residual (fullness of reflection-pairing units) is open; finite-exact bracket
degeneracy data in `code/bracket_full.py`, `code/bracket_depth.py`.  An
unreviewed Codex consult launched 2026-10-17T04:32:22Z (`review/codex-consult-residual/`)
returned partial progress; its obstruction family and main lemmas were verified in
`verify-consult.md` (exact computations p = 3..13, counter-controls) and reviewed by
Claude opus-5-5 max (cross-vendor relative to the current parent):
`review/claude-consult-verify/receipt.json`, obstruction CORRECT.  Consequence:
no catalogue of bounded-length TOP-LEVEL blocks can give full tilings for all of
Res (w_p, p >= 5, has a direct solution, so the target is untouched).  Next routes:
units growing with p, or a structural argument for constant reflection runs.

### 5.7 Route (b): Lemma GR for run-constant reflection words (RGR)

`proof-GR.md`: Lemma GR, an exact iff-criterion for RGR words (rotations in
{rho_x, rho_-x}, every maximal reflection run constant), any length; Corollary
GR-W (a window of >= p even integers forces a solution), which covers the
obstruction family w_p for every p >= 5.  Claude opus-5-5 max review
`review/claude-lemmaGR/receipt.json` (correct with minor fixes, applied); parent's
independent raw-DP check of the GR equations PASS (parent-owned receipt).

### 5.8 Window-avoidance representation (WAS) and the deletion reduction

`repr-WAS.md` (frozen 2026-10-17 00:13 PDT before compute): an RGR word avoids iff
sum_{i in P} theta_i is outside the window W(P) for every zone set P
(theta_i = y_{i-1} - y_i); exact solver `code/was_search.cpp`, independent DP
verifier `code/was_verify.py`, outputs `evidence/was/`.
* Controls: p = 5, N = 18 avoider classes from WAS (105 keys) EXACTLY equal those of
  the 3730 exhaustive D10 length-18 avoiders (all RGR); N = 19: none; shrunken-
  window mutants (35 at p = 5, 12 at p = 7) all rejected by DP; all emitted
  avoiders (420 at p = 5, 3738 at p = 7, N = 26) DP-confirmed.
* Finite-exact: every RGR word of length 27 over D14 has an identity 14-subword
  (4,086,788,695 rotation-canonical run data, all theta; 3,427,632 no-window
  residual run data decided by the WAS DFS).
* Complete extremal structure at length 4p-2 (p = 5, 7; every theta): every RGR
  avoider has all runs odd, constant rotation runs, all brackets equal to rho_{+-x},
  and k <= p, with a unique theta per run datum.
* `proof-DR.md` (written proof): Theorem DR, INV(p) => every RGR word of length
  4p-1 is solvable; Corollary DR', INV*(p) (every length-(4p-2) avoider is RGR) +
  INV(p) => ordered Olson for D_{2p}.  INV(5), INV(7), INV*(5) hold finite-exactly;
  all-p INV and INV* are OPEN.
* Observation (p = 5, 7 only): certificate patterns need >= (p-1)/2 brackets.
Hostile review: the full WAS + DR + code review `review/claude-WAS-DR/` TIMED OUT
(exit 124 after 3300 s, empty output; receipt records no verdict, not an
acceptance).  Focused math review (Claude opus-5-5 max, cross-vendor relative to
the current parent; `review/claude-DR-math/receipt.json`, 08:46:40Z-08:52:27Z):
Lemma WAS correct with a minor fix (hypotheses stated, applied in repr-WAS.md
Sec. 5), Theorem DR correct, Corollary DR' correct.  The code-fidelity and
finite-exact claims are UNREVIEWED (controls in repr-WAS.md Sec. 4 only).

### 5.9 INV stage (inverse statement at length 4p-2)

`repr-INV.md` (frozen 01:56:00 PDT), `proof-INV-reduction.md`: Theorem DR-Res (only
avoiders inheriting (E),(P),(V),(Pairs),(D0) need the inverse statement; Claude max
review correct with minor fixes, applied).  Open all-p lemmas: PAR(p) (k <= p =>
all runs odd) and RUNS(p) (k <= p).  Finite-exact: PAR and RUNS hold at p = 5, 7;
PAR is certified there by single brackets (empty + cyclic intervals; elementary
brackets alone do not suffice); RUNS needs more brackets (p = 5: up to three, for
the fully alternating words).  Handoff state: `inv-handoff.md`.

## 6. Chronological log (actual PDT)

* 18:35 lane created; 18:57 README frozen protocol; 18:59 S3/D10/controls exhaustive.
* 19:10-19:30 family exploration (BRK/BRK1/PAIRS), avoider-structure analysis.
* 19:31-19:39 OBL formulated and checked (C6,S3,D8,Q8,C10,D10).
* 19:40 identity-reduction search validated on D10; A4 switched to it.
* 19:58, 20:19 parent checkpoints (Theorem P, Doubling, rigid).
* ~20:4x proof-dihedral-partial.md written (exact time not observed).
* 20:56-20:59 checkpoint to parent; it was mislabelled "21:10" (host clock read
  20:59:24 just after sending).  Later labels use the host clock only.
* 21:11:52 host clock read; proof-T0.md written shortly after.
* 04:13:34Z-04:18:46Z Codex review of T0/Doubling/R/R'/Davenport (receipt).
* 21:21:16 PDT T0 checkpoint to parent; 21:33:22 PDT host clock read after
  residual-class.md; D12/Dic3 identity-reduction e=0 complete (0) by then.
* 21:54:28 new bounded cycle (parent IRC); 21:55:55 first freeze receipt.
* 21:59:31 consult verification computations done; 05:00:03Z-05:18:08Z Claude
  max hostile review; 22:18:43 provenance driver; 22:20:03 refreshed receipt
  (A4 e=0 complete).
* 00:13:00 (2026-10-17) new cycle; repr-WAS.md frozen before compute;
  00:18-00:20 p = 5 controls; 00:21:57-00:35:27 p = 7 N = 27/26 searches;
  00:35:45-00:49:23 family/mutation runs; 00:52 checkpoint to parent;
  01:01:05 p = 7 N = 26 all-theta structure; Claude review of WAS/DR started
  after 00:50:26.
* 01:46:20 full WAS/DR/code review found timed out (no verdict); 01:46:40-01:52:27
  focused Claude max math review (WAS minor fix, DR and DR' correct); 01:52:37
  fixes recorded (repr-WAS.md Sec. 5, proof-DR.md header).
* INV cycle: repr-INV.md frozen (freeze time recorded in its Sec. 4) before any INV
  computation; target INV(p) (parent IRC after the WAS/DR checkpoint).
* 01:56:00 repr-INV.md frozen (INV cycle); 01:57-02:19 certificate-family runs
  (evidence/inv/); proof-INV-reduction.md: Theorem DR-Res + open lemmas PAR, RUNS;
  09:21:27Z-09:29:57Z Claude max review (DR-Res correct with minor fixes, applied;
  a wrong "step-4" formula for fully alternating words corrected to step 2);
  inv-handoff.md written for a fresh worker.
