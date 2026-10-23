# The "2q+1" framework: exact reduction and starter conditions

Written 2026-10-16 (lane `kirkman57`). Status: Theorem A and Propositions B, C
have **written proofs below (elementary) and are UNREVIEWED** (no independent
review yet); the existence of packages is established only **by computer for
q=19, 31, 43** and shown **impossible for q=7** (exact KM UNSAT). No statement
for other q is claimed; at q=67 a bounded run found STS-level packages but no
resolved package before it was stopped (README results log). Not peer reviewed.

## Setting

q a prime with q≡7 (mod 12) (the arguments below also work verbatim for prime
powers q≡7 (mod 12) with F_q in place of Z_q). `Q≤F_q*` the squares,
`m=|Q|=(q−1)/2` (odd, 3|m), `N=F_q*∖Q=−Q`, ω∈Q of order 3, χ the quadratic
character. `X={∞}∪F_q×{0,1}`, points written `x_j`. `v=|X|=2q+1≡15 (mod 24)`.

    G = {x_j ↦ (ax+b)_j : a∈Q, b∈F_q},   ∞ fixed,   |G|=qm.

`τ_b`: translation, `μ_a`: multiplication. Every non-translation element of G
has order dividing m and fixes exactly `F_c={∞,c_0,c_1}` for one c; nontrivial
translations fix only ∞.

## Theorem A (sufficiency; no symmetry of resolutions needed)

Let (S,R_S), (B_1,R_1), (B_2,R_2) be KTS(2q+1) on X with S Q-invariant and B_1,
B_2 translation-invariant (as block sets), such that **(P)** for every G-orbit O
of triples exactly one of the following holds:
(i) S∩O is a single Q-orbit and B_1∩O=B_2∩O=∅; (ii) S∩O=∅ and, for exactly one
k, `B_k∩O` is a single translation orbit while the other `B_{k'}∩O=∅`.
Then `{τ_b S : b∈F_q} ∪ {μ_a B_k : a∈Q, k=1,2}`, each with the transported
resolution, is an LKTS(2q+1).

*Proof.* There are q+2m=2q−1=v−2 systems, each a KTS (image of a KTS). Fix O.
Case (i): let `S∩O=Q·T`. Then `|Q·T|=|O|/q` forces `Stab_G(T)≤Q` (orbit–stabilizer
in G and in Q). If `τ_bμ_aT=τ_{b'}μ_{a'}T` then `(τ_{b'}μ_{a'})^{-1}τ_bμ_a∈Stab_G(T)≤Q`,
whose translation part is 0, so b=b'. Hence the q sets `τ_b(Q·T)` are pairwise
disjoint, each of size |O|/q, so they partition O; the B-families miss O since
`μ_aB_k∩O=μ_a(B_k∩O)=∅`. Case (ii) is symmetric: `B_k∩O=Z_q·T` with
`|Z_q·T|=|O|/m`, so `Stab_G(T)≤Z_q`, and `μ_a(Z_q T)=μ_{a'}(Z_q T)` forces a=a'.
So every triple lies in exactly one system. ∎

## Proposition B (necessity of the shape)

If an LSTS(2q+1) L on X admits G, then L is exactly of the form in Theorem A
with suitable S, B_1, B_2 (block sets), and (P) holds. *Proof.* As in
Proposition 87-D of `automorphism-lemmas.md` (q=43 there; the proof uses only
that non-translations have orders dividing m with fixed set some `F_c`, that 3|m,
that nontrivial translations have no fixed triple, and Lemma 2): the ω_c-owned
constituents form one orbit of q with stabilizers `Q^{(c)}`; the others have
stabilizers inside Z_q, hence form orbits of length m; `v−2−q=2m` gives two such
orbits. (P) is the statement that the systems partition each G-orbit. ∎

(For q≡7 (mod 12), Aut(L) of an LSTS(2q+1) has odd order by Lemma 3 and the
reverse-STS parity, since v≡15 (mod 24); so G is a natural maximal choice inside
`AGL(1,q)`.)

## Orbit inventory (all forced placements made explicit)

Regular G-orbits of triples: `4(2q+1)/3`, namely
* `INF_within(j)` = G·{∞,0_j,1_j} (j=0,1);
* `INF_cross(ε)` = G·{∞,0_0,d_1}, χ(d)=ε (ε=±1);
* `AAB_{ij}(w)` = G·{0_i,1_i,w_j}, w∈F_q, (i,j)=(0,1),(1,0) — **these 2q orbits
  are pairwise distinct and exhaust the two-copy triples** (the only element of
  AGL(1,q) swapping 0 and 1 is x↦1−x, with multiplier −1∉Q);
* `(q−4)/3` orbits of triples inside each copy.

Short orbits: the q lines `F_c` (stabilizer `Q^{(c)}`) and four orbits of
ω-cycles `{c+e,c+ωe,c+ω²e}_j` (stabilizer of order 3). Forced by Lemma 2:
`F_0∈S` and all ω_0-cycles lie in S. Forced by counting: ∞ lies in q blocks of
B_k, one translation orbit; an orbit `Z_q·{∞,x_j,y_j}` would cover every pair
`{∞,z_j}` twice, so it is an `INF_cross` orbit. Two B's need two such orbits and
exactly two exist (χ(d)=±1), so B_1, B_2 take one each (opposite characters), and
the two Q-orbits of ∞-blocks of S other than `F_0` are the two `INF_within`
orbits: `S ⊇ Q·{∞,1_0,s_0} ∪ Q·{∞,1_1,t_1}` with s,t∈N (so that each copy is
matched Q↔N). Pair counting in B_k gives `3x_0+n_{01}=3x_1+n_{10}=m`,
`n_{01}+n_{10}=m` (`x_j` inner-copy base blocks in copy j, `n_{ij}` two-copy base
blocks with two points in copy i), hence `x_0+x_1=m/3`; S then uses the remaining
`(q−7)/3` inner-copy and `q+1` two-copy orbits.

## Starter conditions (field form)

A two-copy orbit `AAB_{ij}(w)` placed in B_k is described by a multiplier
`a_w∈Q`: `B_k ⊇ Z_q·{0_i,(a_w)_i,(a_w w)_j}`. With `d_k` the cross difference of
B_k's ∞-orbit and analogous data for inner-copy base blocks, B_k is an STS iff

* (within copy i) the multisets `{a_w : (i,j,w)∈B_k}` together with the
  Q-representatives of the differences of B_k's inner-copy base blocks in copy i
  are exactly Q (each element once);
* (cross) `{d_k} ⊎ {a_w w, a_w(w−1) : (0,1,w)∈B_k} ⊎ {−a_w w, −a_w(w−1) : (1,0,w)∈B_k}`
  is exactly F_q (copy-1 point minus copy-0 point).

S is described by a translate `b_w` per assigned orbit (`S ⊇ Q·{b_i,(1+b)_i,(w+b)_j}`),
and S is an STS iff each of its `4q+9` Q-orbits of pairs (3 among the fixed
points; 4 of type `{∞,x_j}`; 8 of type `{0_i,x_j}`; `q−2` inside each copy among
nonzero points; `2(q−1)` cross pairs among nonzero points) is met exactly once
(the KM model for q=43 has 181=4·43+9 such columns). Resolvability of each base is an additional,
independent condition (Theorem A needs only that each base is resolvable).

## What is known about packages

| q | v=2q+1 | package | evidence |
|---|---|---|---|
| 7 | 15 | **none** (KM exact cover UNSAT, kissat 0.007 s) | `evidence/family-2q1-controls/q7_stdout.txt` |
| 19 | 39 | found (LKTS(39), a known order) | `evidence/family-2q1-controls/lkts39_q19.txt`, 3 checkers PASS |
| 31 | 63 | found (LKTS(63), a known order) | `evidence/family-2q1-controls/lkts63_q31.txt`, 3 checkers PASS |
| 43 | 87 | found (LKTS(87), previously open) | `evidence/lkts87-g903/` |

**Open (exact missing lemma for a uniform theorem):** existence, for every
prime q≡7 (mod 12) with q≥19, of a Q-invariant KTS S and two translation-invariant
KTSs B_1, B_2 satisfying (P). No closed-form choice of the data
`(s,t,d_k,a_w,b_w,…)` is known to us; the three computed packages show no
evident algebraic pattern (`code/analyze_2q1.py` output in the README log).

## Bounded closed-form attempt (2026-10-16, after 21:00 PDT): structured ansatzes

To look for an algebraic (cyclotomic) family, extra symmetry was imposed on
the bases and the STS-level exact cover re-solved (kissat; models are exact for
the stated restriction; UNSAT = no package *with that extra symmetry*):

| Ansatz | q=19 | q=31 | q=43 |
|---|---|---|---|
| both B_k invariant under ψ_k = (x_0↦λx_0, x_1↦λ(x_1−d_k)+d_k), ord λ = m/3 (forced center d_k by Lemma 1) | n/a (m/3=3) | UNSAT 0.04 s | UNSAT 0.05 s |
| only B_1 twisted as above | n/a | UNSAT 0.04 s | UNSAT 0.06 s |
| S additionally invariant under an order-3 element commuting with Q that cycles three of the Q-orbits Q_0,N_0,Q_1,N_1 and multiplies the fourth by ω (three placements sE1–sE3) | UNSAT ×3 | UNSAT ×3 | UNSAT ×3 |

Evidence: `evidence/family-2q1-ansatz/` (stdout files and CNF hashes;
generator `code/g2q1_struct.py`, `code/g2q1_ansatz.py`). Conclusion: the computed
packages are not instances of these natural symmetric patterns; a uniform
existence proof for the 2q+1 family would need a different idea (no such proof
is offered).

### Round 2 (CNF file mtimes 21:18:07–22:05:22 PDT, 2026-10-16; round 1 runs 21:09:01–21:11:xx)

**Proposition C (written proof, UNREVIEWED: no multiplicative twist of a B-base beyond involutions).**
Let (S,B_1,B_2) be a package and let ψ fix ∞ and act by `x_j ↦ (λx+c_j)_j`
(same λ∈F_q*, any c_0,c_1). If ψ(B_k)=B_k then λ=±1.
*Proof.* B_k contains a block T inside one copy j (it has `x_0+x_1=m/3≥1` such
translation orbits). `ψ²(T)=μT+c` with `μ=λ²∈Q`, so `ψ²(T)=g(T)` for
`g:x↦μx+c` in G; thus `ψ²(T)∈B_k∩G·T`, which is a single translation orbit by
(P), so `ψ²(T)=T+y` and `h=τ_{−y}g∈G` fixes T setwise. A non-translation
`x↦ax+b` of G fixing a triple inside a copy either fixes its center
`b/(1−a)` and two further points (forcing a=1) or swaps them (forcing a=−1∉Q),
or permutes T cyclically (a=ω^{±1}, T an ω-cycle, which lies in a short orbit
and hence in S by (P)). So h is a translation fixing T, i.e. h=id, μ=1, λ=±1. ∎

Consequently no B-base admits a cyclotomic symmetry of any fixed index e>2 of
the form above; the index-6 twists tested in round 1 were impossible for this
reason (and single-base runs confirm: twisted B_1 alone is UNSAT at q=31, 43).

Further exact KM runs (kissat; UNSAT = no package with that extra symmetry):

| Ansatz | q=19 | q=31 | q=43 |
|---|---|---|---|
| `B_2=φ(B_1)`, φ = multiplication by a fixed non-square on both copies | **SAT** 0.24 s | **SAT** 0.31 s | **SAT** 64.7 s |
| S invariant under σ:(x,0)↦(x,1),(x,1)↦(nx,0) | UNSAT | UNSAT | UNSAT |
| σ-invariant S and `B_2=φ(B_1)` | UNSAT | UNSAT | UNSAT |
| S invariant under all of F_q* (multiplication by a non-square) | UNSAT | UNSAT | UNSAT |
| B_1 invariant under the twisted involution `x_0↦−x_0, x_1↦−(x_1−1)+1` | UNSAT | UNSAT | UNSAT |
| both B's invariant under their twisted involutions | UNSAT | UNSAT | UNSAT |

(`code/g2q1_ansatz2.py`, `code/g2q1_ansatz3.py`, `code/scratch/twist_single.py`;
CNF hashes `evidence/family-2q1-ansatz/cnf_hashes_round2.txt`.) The only
symmetry-reducing restriction that survives is the B-pairing `B_2=φ(B_1)` (it
halves the B data but gives no fixed-index structure). Cyclotomic-class
statistics of the computed packages (`code/cyclo_stats.py`) show no regularity.
**Status of the uniform-theorem target: blocked within this framework** — any
proof would need non-multiplicative explicit constructions or a different
framework; nothing beyond Theorem A, Propositions B–C and the finite cases is
claimed.
