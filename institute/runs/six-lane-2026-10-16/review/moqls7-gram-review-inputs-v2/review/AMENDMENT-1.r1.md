# Protocol amendment 1 (lane moqls7-maximum): Gram-support representation for K2/K3; production certification

Frozen before any production (certification) run, after exploration only. It amends README §0.4 Phase C and §0.5.
Nothing here changes the frozen target or definitions.

## A. Why
- The single-frame pattern CNFs for K2 (free classical square, W3) and K3 (W3+sym) ended UNKNOWN at 1800 s each:
  `explore/k2/k2A_w3.out`, `explore/k3/k3A_w3sym.out`. That is a calibrated obstruction, so the representation
  changes.

## B. Representation (exact statements and proofs in `review/GRAM-ENCODING.md` once frozen)
- Unknowns: Gram supports g_a(p,q) for each quantum square a. Conditions G1 (collinear ⇒ 0), G2 (consistency in
  every ONB line frame), G3 (unitary transition patterns between ONB lines) and G5 (product orthogonality exactly ⇔
  edge-disjoint supports; orthogonality to classical L ⇔ G1 on L lines).
- G4 heavy: in a non-classical 3-set minimising the number of non-classical squares, every non-classical square is
  heavy in every ONB. The proof uses Theorem K1 and Lemma 10 in an arbitrary basis. Consequently every own ONB line
  has an off-line point with ≥ 3 neighbours on it.
- G4 depends on Theorem K1 (`review/K1-THEOREM.r1.md`; parent routes completed, CLI reviews pending, §8 under review).
  Every K2/K3 claim inherits that dependence and states it.

## C. Production runs (sequential; ≤ 2 busy processes; proofs streamed through a FIFO, never stored)
1. **K2**, for each of the 147 main classes in `evidence/ls7_main_classes.txt` (898065c8…8158): instance =
   2 quantum squares + fixed L (class representative from its key) + heavy.
   - Encoder A: `code/gram_enc.py`, build(2, L, heavy=True), with CaDiCaL.
   - Encoder B: `code/gram_encB.py --squares 2 --net-L L --heavy`, with kissat.
   - Each run is checked by the lane drat-trim (`env/drat-trim`, source d834b649…c2ee).
   - Driver: `code/gram_certify.py`. Record: instance id, CNF SHA-256, solver return code, drat-trim verdict (exact
     `s VERIFIED` after stripping CR), seconds.
2. **K3**: one instance with 3 quantum squares, heavy and sym, under both encoders; same recording.
3. **Chunks.** Each solve gets ≤ 3 h. A K3 UNKNOWN is not UNSAT. If the K3 instance does not finish, it is split
   only by a further amendment frozen before use: cubes on the row-0 frame neighbourhood of the fixed heavy point,
   with a coverage proof.
4. **SAT outcome.** Any SAT is decoded and kept. It is not a witness. Next comes a numerical realisation attempt
   (exploration), and only then exact reconstruction with two checkers.

## D. Controls (already run on genuine exact data; both encoders)
- Classical triple: SAT.
- Genuine non-classical pair (Ψ(f), Φ(m)) of Ball–Simoens Ex. 15 (q = 7, H = {1,2,4}, f shifted): SAT.
- Ψ(f) alone on its 3-net with heavy: SAT.
- Classical K2-shaped data (encoder B): SAT.
- Files: `explore/gram/gram_controls_v1.json`, `explore/gram/gram_controlsB_v1.json`.
- Before production, encoder A and B controls are re-run once on the frozen code, and the code SHAs are recorded in
  the certification output.

## E. Exploration already done (not evidence)
- `explore/k2classes/screen_v1.jsonl` (encoder A): stage 1 (one heavy assignment) SAT for all 147 classes; stage 2
  UNSAT for all 147, each ≤ 23.5 s.
- `explore/k2classes/screenB_v1.jsonl` (encoder B, kissat): in progress at freeze time.
- `explore/gram/k3G_heavy_sym.cnf`: CaDiCaL in progress at freeze time.
