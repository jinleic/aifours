# Original Tuscan-2(11), unrestricted family: distance two as near-disjointness of the eleven K-matrices; the Latin case is exactly idempotent Latin squares with ten-periodic Hamilton faces

Actual `/bin/date` before this body: **Mon Oct 26 15:35:06 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE on the original distance-two coupling for ALL eligible arrays. This is the pivot requested by Main after v108, not another T1 family. It is not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, chosen row or chosen control.

## 1. Setting

- (R1)–(R3) are the original requirements of `selection-v1.md` lines 7–11 (SHA256 `fd62055310684ffcd28be47c3f0c6e8698e6d72bae7118aa1818b5d17df3af2b`).
- The notation τ, f, p, F, G, K_x, T and M is that of v1 (SHA256 `e54953336e35bd7a535d147ca6a564f9db30ddca966f1ad31dc58485167d8275`) and of the interface v108 (SHA256 `b1c6504a65fa911aeb016d77daca5c6b24f3efee893ae7de539b7354b67802ed`).
- K_x is a permutation of X with K_x(x) = x (v1 Lemma 1). P_x is its 11×11 permutation matrix, with row = tail and column = head.

Under (R1)–(R2), v1 eq. (1) reads Σ_x P_x = I + Γ + GF. Here Γ counts distance-two events, and GF is the boundary-turn matrix (entry (p(x), f(x)) for each x).

## 2. Theorem A: distance two is near-disjointness, for all arrays

Assume (R1)–(R2). Remove from each P_x its diagonal entry (x,x) and its boundary entry (p(x), f(x)). The remaining 9 entries of P_x are exactly the distance-two events with middle x (v1 §2). Hence:

**(R3) holds iff these 11·9 = 99 entries are pairwise disjoint.**

Equivalently, every off-diagonal cell (a,b) is covered by at most 1 + GF(a,b) of the P_x. Then the number of covers is exactly 1 + GF(a,b) − M(a,b), which is v1 eq. (2). A diagonal cell (a,a) is covered by P_a and by every P_x with a loop p(x) = f(x) = a.

**Proof.** A cell (a,b), a ≠ b, carries one internal entry of P_x for each distance-two event (a,b) with middle x. (R3) says there is at most one such x. ∎

**Middle-symbol form.** Put μ(a,b) = x when (a,b) carries the distance-two event with middle x.
- Row a of μ has distinct symbols, because (a,x) is a single adjacency.
- Column b has distinct symbols, because (x,b) is a single adjacency.
- By Theorem A, cells are single-valued.

So μ is a partial Latin square with 99 cells. Symbol x fills 9 cells, missing rows x and p(x) and columns x and f(x). Its row-to-column map is the internal part of K_x.

## 3. Theorem B: the Latin case

For an eligible array the following are equivalent:
- (i) GF = M;
- (ii) Σ_x P_x = J;
- (iii) the K_x are the symbol permutations of an idempotent Latin square Q of order 11, i.e. Q(a,b) = x iff K_x(a) = b.

**Proof.**
- (i)⇔(ii) follows from Σ_x P_x = J + GF − M (v1 eq. 2).
- (ii)⇒(iii): each cell lies in exactly one P_x, so Q is well defined. Symbol x occupies the cells of the permutation matrix P_x, hence occurs once per row and per column. Q(a,a) = a because P_a covers (a,a).
- (iii)⇒(ii): the symbol matrices of a Latin square partition its cells. ∎

(i) is not implied by (R1)–(R3). The written n = 4 calibration of v1 §4 has GF = I. So the Latin case is a proper subcase. It is used below only as an exact characterization, never as an assumption on unrestricted arrays.

## 4. Theorem C: Latin-case reconstruction

Let Q be any idempotent Latin square of order 11. Put K_x(a) = the b with Q(a,b) = x, and T(a,x) = (x, K_x(a)) on the 110 arcs.

Eligible arrays with GF = M whose centre permutations are these K_x correspond exactly to a choice, on each T-cycle C, of one phase class mod 10 (C must have length 10ℓ_C), such that:
- **(a)** the heads of the arcs in the chosen classes (the terminal arcs) run over every symbol exactly once;
- **(b)** every 10-arc segment from one terminal arc to the next visits 11 distinct symbols.

For such data, (R3) holds automatically.

**Proof.**
- Rows are the 10-arc segments, read as symbol sequences. By (b) each is a permutation of X (R1). Condition (b) also rules out ℓ_C = 1, since such a segment would start and end at one symbol.
- T permutes all 110 arcs, so every ordered adjacency occurs exactly once (R2).
- By (a), each symbol ends exactly one row and starts exactly one row.
- An internal triple (a,x,b) is a T-step, so K_x(a) = b and Q(a,b) = x. Two internal triples with the same (a,b) would share x = Q(a,b), hence the arc (a,x), hence they are one triple. So (R3) holds.
- At a cut v the T-step is the boundary turn, so K_v(p(v)) = f(v). The cell (p(v), f(v)) is covered only by P_v, so it carries no distance-two event and lies in M. Distinct v give distinct cells. There is no loop, since (a,a) is covered only by P_a while p(a) ≠ a. With |M| = 11 this gives GF = M.
- Conversely, an eligible array with GF = M yields Q by Theorem B. Its T is v1's T (v1 Theorem 2), with faces of length 10r, cuts every 10 arcs, each symbol cut once, and Hamilton segments. ∎

**Consequence.** In the Latin case, the distance-two requirement is entirely absorbed by the Latin property of Q. What remains is the ten-periodic Hamilton face structure (a)–(b) of Q's T-map.

## 5. Defect trichotomy for the general case

GF and M are both 11-entry matrices with the same margins (v1 lines 65–70). An eligible array lies outside the Latin case iff at least one boundary turn x is of one of these kinds:
- **(D-loop)** p(x) = f(x). There are β of these, and M has no diagonal.
- **(D-hit)** cell (p(x), f(x)) also carries a distance-two event with another middle.
- **(D-share)** two boundary turns lie on one cell.

The number of M-cells hit by no boundary turn equals β + (number of D-hit turns) + (number of D-share turns on M-cells beyond the first on each cell). The n = 4 calibration is all D-loop.

## 6. Restricted-source remark (illustration of Theorem C only; not a substitute family)

Consider a diagonally cyclic idempotent Latin square Q(a,b) = a + φ(b−a) over Z_11, where φ(0) = 0 and both φ and d ↦ φ(d) − d are bijections. Such a Q never satisfies Theorem C.
- Write an arc as (tail a, difference e). Then T(a,e) = (a+e, θ(e)), with θ(e) = φ^(-1)(e) − e a permutation of Z_11^*.
- A T-cycle has length L or 11L. Here L ≤ 10 is the length of the θ-cycle of e, and the factor 11 occurs iff that θ-cycle's sum S is non-zero.
- Length ≡ 0 (mod 10) with at least two rows forces length 11L with L = 10. Then θ is one 10-cycle on Z_11^*, so S = Σ_(e≠0) e = 0. Contradiction.

This recovers, inside the Latin case, the known failure of odd cyclic development (screen noted in `selection-v1.md` line 45). It says nothing about unrestricted arrays.

## 7. Result

- **WRITTEN:** Theorem A (distance two is the near-disjointness of the eleven K-matrices, for all eligible arrays), and the middle-symbol partial-Latin form.
- **WRITTEN:** Theorem B (the Latin case GF = M is exactly idempotent Latin squares).
- **WRITTEN:** Theorem C (in the Latin case, eligibility is exactly a ten-periodic Hamilton cut system on Q's T-cycles, and (R3) is automatic).
- **WRITTEN:** the defect trichotomy for GF ≠ M.
- **Remark:** diagonally cyclic Q fail (restricted; illustration only).

**Not claimed:** that eligible arrays must be in the Latin case, or any existence or nonexistence at order 11.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
