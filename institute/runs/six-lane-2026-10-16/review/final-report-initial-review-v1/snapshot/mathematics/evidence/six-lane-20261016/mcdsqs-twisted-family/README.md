# mcDSQS(2p) for primes p ≡ 7 (mod 12) — twisted-AGL family lane (math-1)

Lane owner: worker `MathMcDsqs38`. Frozen contract (read-only):
`institute/runs/six-lane-2026-10-16/screening/math-1-mcdsqs-twisted-family-contract.json`
(recorded 2026-10-17T03:36:30-07:00). Status label: DERIVED-RESEARCH-TARGET (the primary
source asks for more mcDSQS examples and constructions; it does not state this prime family).
Prior lane `../mcdsqs38/` (the verified p = 19 case) is immutable; its code is copied into
`code/` here (hashes in `runs/copied_code_sha256.txt`).

## 0. Cycle 1 status (2026-10-17, written after 04:41:00 PDT host clock)

**No uniform proof and no counterexample.** The family question is open in this lane.
Delivered: (i) bounded prior-art audit — no located construction covers 2p for p ≡ 7 mod 12
beyond the verified p = 19 example; (ii) proved reductions and constraints for the twisted
model T1 (`sources/structure-lemmas.md`): SQS layer ⟺ A-equivariant completion + Φ-invariant
pairing (k = 0: injective completion missing a consecutive pair W); colouring layer ⟺ a rainbow
pair of near-perfect matchings; negative lemmas (all p ≡ 7 mod 12): no Hessian-type k = 0 SQS
(Lemma H); W ≠ {0,1} for every k = 0 SQS (else an STS(p−1) would exist) — so in particular no
G×⟨copy-swap⟩-invariant k = 0 SQS; exactly one vertex-completed orbit; (iii) finite evidence
only: T1 mcDSQS found at p = 19 and p = 31 (unpinned `runs/f1/p31/mcdsqs62_sample0.txt`, sha256
`196b4b2d…2bdb`, and the k = 0 certificates in `runs/f3/`), p = 43 UNKNOWN within the caps.
**Irreducible next steps:** (O1) a uniform completion rule (Hessian points are a poor basis:
4/5, 6/9, 6/13 orbits must deviate); (O2) a uniform rainbow pair (C_1, C_−1) satisfying the
copy-0 "relative starter" shadow of L6(b); alternative route (L7): a 1cDCQS(2^{p−1}:2) gives
mcDSQS(2p) by Tan–Zhou Construction 2.7, but needs less symmetry than T1 with k = 0.
Deviations on record: automatic deletion of intermediate CNFs/mutated files in the earlier
code (`sources/incident-deletion-20261017.md`); `code/sqs_layer_sat.py` gained the F3.2c/F3.5
branches after earlier runs (behaviour of those modes unchanged; pre-edit hashes not recorded)
and had an UNKNOWN-as-SAT status-parse bug (fixed; statuses re-read from retained logs).

## 1. Frozen target (written 2026-10-17 between 03:44:08 and 03:44:52 PDT host clock, before any search)

For every prime p ≥ 19 with p ≡ 7 (mod 12): does there exist an SQS(2p) whose derived
STS(2p−1) at **every** point has a colouring into p partial parallel classes (pairwise
point-disjoint triples)? p = ⌈((2p−1)(2p−2)/6)/⌊(2p−1)/3⌋⌉ = χ′(2p−1) (Tan–Zhou (1.1);
2p−1 ≡ 1 mod 6, 2p−1 ∉ {7, 13}). Wanted: a uniform construction with a complete proof, or a
complete counterexample proof. Group invariance, block types and class-size profiles used
below are search/proof **ansätze**, never hypotheses of a nonexistence claim; a model-scoped
UNSAT or timeout is not a counterexample. Finite successes alone do not prove the family.

## 2. Notation and frozen representation T1

F = F_p, S = nonzero squares, N = non-squares (−1 ∈ N, 3 ∈ N, −3 ∈ S), χ the quadratic
character, ω a primitive cube root of unity (ω ∈ S). X = F × Z2. The twisted affine group
G = {g_{a,b} : (x,i) ↦ (ax+b, i+χ'(a))}, χ'(a) = 0 for a ∈ S and 1 for a ∈ N; G ≅ AGL(1,p),
|G| = p(p−1), transitive, stabilizer of (0,0) = {x ↦ ax : a ∈ S} (odd order (p−1)/2).
Implementation: Z_{2p}, y ↔ (y mod p, y mod 2), generators y ↦ y+2 and y ↦ g·y+1 with g the
least primitive root mod p made odd (g or g+p); colouring symmetry R = ⟨g²⟩ (the squares),
anchor y = p ↔ (0,1). For p = 19 this is exactly the verified mcDSQS(38) model.

## 3. Experiments (frozen order; ≤ 4 CPU, ≤ 8 GiB, checkpoints ≤ 30 min, first chunk ≤ 3 h)

* A0 prior-art audit (bounded, before claims): Tan–Zhou constructions (§2–3 of the local
  source, not only the short list) against 2p for p ∈ {31, 43, 67, 79, …}; equivalence of T1
  with Netto / Schreiber / affine SQS constructions. Recorded in `sources/prior-art-audit.md`.
* F0: reproduce p = 19 from the copied code (same command as `../mcdsqs38` E6; the certificate
  must be byte-identical to sha256 `973f93e4…3f1c`; no new pin).
* F1: probes p = 31 (v = 62) then p = 43 (v = 86) with the same pipeline: ≤ 4 KM samples,
  ≤ 15 min wall per prime, colouring cap 300 s. Certificates stay in `runs/` (not promoted).
* F2: structure: classify the block-orbit types of T1 solutions; restricted Kramer–Mesner
  models by block type (in particular "(3,1)+(2,2) only", no 4 points in one copy), scoped.
* F3: parameterized algebraic ansätze for blocks and colourings; each formula family is
  frozen in this README before it is evaluated, and only then compared with p = 19, 31, 43.
* Proof work (the main deliverable of the cycle): `sources/` notes; every lemma either proved
  in full or marked open.

### F3.1 — frozen 2026-10-17 before 04:04:53 PDT (first F3.1 output mtime), before any evaluation (SQS layer only)

Reduction (proved in `sources/structure-lemmas.md`): a G-invariant SQS(2p) is given by an
A-equivariant choice, for each copy-0 triple T, of a block through T (A = {x ↦ ax+b, a ∈ S});
(2,2)-blocks are then forced to pair the leftover copy-1 points L0({0,1}) into pairs whose
partition is invariant under the involution Φ{q1,q2} = {q1/d, (q1−1)/d}, d = q1−q2 ∈ S.
**Hessian rule H_ω:** ω a primitive cube root of unity, λ = −ω; every copy-0 triple T is
oriented cyclically so that (x−y)(y−z)(z−x) ∈ S, and completed in copy 1 by the fixed point
of multiplier ω of the order-3 Möbius map x→y→z→x (a Hessian point of T); equivalently, in
the coordinate w = z/(z−1) of the normalized triple {0,1,z}, the completion is λw (w ∈ S),
λ⁻¹w (w ∈ N). Exactly one Netto orbit has its Hessian point at ∞ (pole); variants:
(P1) complete it by its centroid in copy 1; (P2) use the (4,0)-blocks of the A-orbit of the
equianharmonic quadruple {0, 1, −ω², 1/(1−ω)} (pole Netto triangle + centroid, same copy) and
H_ω on all other copy-0 triples. For each p ∈ {19, 31, 43} and both choices of ω, evaluate:
completion collisions, L0({0,1}), and every Φ-invariant pairing of L0({0,1}); a resulting
SQS(2p) must pass `code/check_mcdsqs.py`-equivalent SQS checks. Colourings are a separate
later step (to be frozen before evaluation).

### F3.2 — frozen 2026-10-17 before 04:16:22 PDT (first F3.2 output mtime), before any evaluation (SQS layer, k = 0)

After F3.1 and Lemma H (`sources/structure-lemmas.md` L4(iv)–(v)): equilateral orbits →
centroid, the progression orbit → **midpoint** ((x+y)/2 for {x,(x+y)/2,y}), every other
copy-0 orbit → one of its two Hessian points (a free bit per orbit). Constraint model (SAT,
kissat, guarded code, all CNFs retained): z ↦ f({0,1,z}) injective, missing pair consecutive.
Evaluated at p = 19, 31, 43 only. If SAT, record the bit pattern ε against the coset
structure of L4(v); if UNSAT, the next variant frees the orbits of w = ω, ω² as well
(frozen here now: "F3.2b"), still only at p = 19, 31, 43. Non-finds are scoped to the model.
F3.2c (frozen between 04:16:28 and 04:16:56 PDT, after F3.2/F3.2b UNSAT): the **full** k = 0 model (every
non-equilateral orbit free, p candidates; equilateral → centroid as forced by L1), same SAT
constraints, p = 19, 31, 43 — decides whether T1 admits any SQS without (4,0)-blocks.
F3.3 (frozen before 04:19:17 PDT, first output mtime, before evaluation): colourability of the F3.2c k = 0
SQS(2p) (the single SAT model per p) under the T1 colouring model (R = squares, anchor (0,1),
`code/ppcsym.py`), p = 19 and 31 only, one kissat run each, cap 300 s; results stay in
`runs/f3/` (unpromoted; no new pins).
F3.3b (frozen between 04:19:22 and 04:19:36 PDT, after F3.3 SAT at 19 and 31 in ≤ 3.5 s): the same single
run at p = 43 (cap 300 s) to compare with the F1 p = 43 UNKNOWN; no further orders.
F3.4 (frozen before 04:30:56 PDT, first output mtime, before evaluation; SQS layer, k = 0): every
non-equilateral orbit takes a Hessian point unless it is declared *free* (any completion);
minimize the number K of free orbits (K = 1, 2, 3, … until SAT, cap 60 s per call) subject to
L2/L3 and W ≠ {0,1} (L6a), at p = 19, 31, 43 only; record the free orbits' algebraic
description to look for a p-independent pattern. Time box 40 min; no colourings here.
F3.5 (frozen before 04:37:25 PDT, first output mtime, before evaluation; lead L7): (a) the full k = 0 SQS layer
with W = {0,1} forced (doubling-type SQS {P×Z2} ∪ (3,1)-blocks) at p = 19, 31, 43; (b) for
its p = 19 (and, if SAT in ≤ 300 s, p = 31) solution, colourability of the derived design at 0
under the smaller symmetry R = ⟨ω⟩ (order 3, anchor (0,1); S-invariance is excluded by
L6a), one kissat run each, cap 300 s. Results unpromoted in `runs/f3/`.

**Stop rules.** F1 caps are hard. No accumulation of larger finite certificates (at most one
retained per prime, unpinned). If an algebraic formula is found, freeze it, then prove it;
computer checks of the formula at specific p are controls, not the proof. Report candidate
proofs/witnesses to the parent immediately with SHAs.

## 4. Results log

Times are file mtimes (PDT) unless marked "host clock".

| Completed | Experiment | Outcome |
|---|---|---|
| 10-17 03:44:52 | F0 p=19 replay from copied code (`runs/f0/p19_replay/`) | certificate byte-identical to the pinned mcDSQS(38) (`973f93e4…3f1c`), KM CNF `a91690c2…fc104` |
| 10-17 03:46–03:55 host clock | A0 bounded prior-art audit (`sources/prior-art-audit.md`) | no stated construction (Tan–Zhou §2–3, Shi–Xia–Krotov, web) yields mcDSQS(62), (86) or the family; bounded search only |
| 10-17 03:47 (cert mtime) | F1 p=31 probe, old copied code (`runs/f1/p31/`, log `runs/f1/p31.log`) | KM 42 cols/507 rows, 4 samples SAT ≤0.03 s; sample 0 colouring SAT in 72.3 s → `mcdsqs62_sample0.txt` sha256 `196b4b2d428d54cf5e9b0f0edf1ff2a4ff7a4ca296fabfba23234dc8cf732bdb`, lane Python (3.9.6) and C checkers PASS, profile 20³⁰10 (unpinned probe result); samples 1–3 not finished — run cancelled gracefully at 03:50:19 after the parent's safety correction |
| 10-17 03:53 host clock | **Incident: automatic deletion of intermediate files** (`sources/incident-deletion-20261017.md`, `runs/incident_inventory.json`) | the copied producer had removed km_1–km_3.cnf of F1 (and the frozen mcdsqs38 lane's runs lost KM/colouring CNFs and mutated files, inventoried there); cleanup disabled in `code/pipeline.py` (`95b58673…a749`) and `code/mutation_controls.py` (`c14763f1…24bc`) with a raising no-delete guard and fresh-directory rule; no further probes until the parent acknowledges |
| 10-17 04:04:53 | F3.1 Hessian completions (`code/hessian_sqs.py`, `runs/f3/hessian_p{19,31,43}.json`) | P1: one collision on every pair (p(p−1)/6 pole triples patched), L0 = {0,1,−ω²}; P2: injective, \|L0\| = 6 as predicted, but **no Φ-invariant pairing** for p = 19, 31, 43, both ω → no SQS from F3.1 (scoped) |
| 10-17 04:09:06 | F1 p=43 probe, guarded code `95b58673…a749` (`runs/f1/p43/`, `runs/f1/p43.log`; parent OK 04:00) | KM 58 cols/1036 rows, 4 samples SAT; **4/4 colourings UNKNOWN at 480 s** (4 workers, wall 8 min); all 4 KM and 4 colouring CNFs + logs retained. Not a counterexample |
| 10-17 04:16:22–28 | F3.2 / F3.2b (`code/sqs_layer_sat.py`, `runs/f3/layer_F3.2*_p*/`, CNFs retained) | Hessian + midpoint progression (+ free orbits of w = ω, ω² in F3.2b): **UNSAT** at p = 19, 31, 43 (both modes; scoped) |
| 10-17 04:16:56 | F3.2c full k = 0 model (`runs/f3/layer_F3.2c_p*/`) | **SAT** at p = 19, 31, 43; expanded block sets checked directly: valid SQS(38), SQS(62), SQS(86) with no (4,0)-blocks; missing pairs W = {6,7}, {3,4}, {24,25} |
| 10-17 04:19:22 | F3.3 colourability of the F3.2c SQS (`code/colour_layer.py`, `runs/f3/colour_F3.3_p{19,31}/`) | p = 19 SAT 1.1 s, p = 31 SAT 3.5 s; certificates `26e2be6d…ad36a` (v=38) and `5bc041ad…69b9` (v=62) pass the lane Python checker (unpromoted, not pinned) |
| 10-17 04:24:36 | F3.3b same at p = 43 (`runs/f3/colour_F3.3b_p43/`) | UNKNOWN at 300 s (12794 vars). Not a counterexample |
| 10-17 04:2x–04:41:00 (final mtime) | proof notes `sources/structure-lemmas.md` L4(iv)–(v), L5 (scope fixed to k = 0), L6 | Lemma H (Hessian-type completions impossible, all p), identity giving a consecutive leftover pair, parity Lemma P (W = {0,1}, in particular G×⟨τ⟩-invariant SQS, admit no S-invariant colouring; later shown vacuous), copy-0 shadow "relative starter" condition |
| 10-17 04:30:58–04:31:11 | F3.4 minimal free sets (`code/sqs_layer_minfree.py`, `runs/f3/minfree_p*_K*/`, CNFs retained) | minimum number of non-Hessian orbits (W ≠ {0,1}): p = 19: K = 4 of 5; p = 31: K = 6 of 9; p = 43: K = 6 of 13. Free orbits always include the progression orbit (Lemma H) and one orbit completed by a vertex point (supplying the values 0, 1, which Hessian points never take); the others show no p-independent algebraic pattern |
| 10-17 04:39:26 | F3.5(a) doubling-type SQS layer, W = {0,1} forced (`runs/f3/layer_F3.5_p*/`) | **UNSAT** at p = 19, 31; p = 43: kissat `s UNKNOWN` at 120 s (log retained), then the script crashed because its status parser read UNKNOWN as SAT — no result.json written; parser fixed in `code/sqs_layer_sat.py` and `code/sqs_layer_minfree.py` afterwards (all earlier statuses re-read from the retained kissat logs: correct). Then **proved for all p** (L6(a) revised): W = {0,1} would make the copy-1 triples completed by (0,0) an STS(p−1), impossible as p−1 ≡ 0 (mod 6). F3.5(b) therefore void; the earlier "parity Lemma P" is vacuous |

Time-label correction (recorded after 04:41 PDT host clock): the freeze labels of F3.1–F3.5 and
§§0–1 originally carried estimated clock times (04:07, 04:20, 04:17, 04:20, 04:20, 04:33,
04:42, 04:45, 03:45) that were later than the actual edits; they are replaced above by bounds
from file mtimes. Every freeze edit was made before the corresponding evaluation.
