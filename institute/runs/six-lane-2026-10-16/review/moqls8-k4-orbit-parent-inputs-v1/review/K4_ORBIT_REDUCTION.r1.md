# K4 split: orbit reduction by verified CNF automorphisms — math/certification note and ledger contract, r1
# (model-authored; NOT IN FORCE until the parent's both-CLI review and GO(b); no orbit certificate counts before that)

## 0. Pinned objects
- F4 = evidence/k4_w1_v1/GA3_K4w1.cnf, SHA-256 7bb806fc8f7793fa5088cc78caf3ebf5b49a72cad82c527f47cf6faced4301f7
  (513184 variables, 5833793 clauses), README §9.
- Name table (construction aid only, §2.3): review/moqls8-encoder-binding-v1/K4.names.json.gz (parent run directory),
  SHA-256 ed0462bc4de7fdcbc34397e1b05304160e47b9ba4a1bd1c858c5f997df3f8e2d; its g-entries agree with the lane map
  GA3_K4w1.map.json (0 mismatches).
- Checker code/k4_automorphism_r2.py SHA-256 ae9bcbb421d134b0cb492571937f0808d94fcc5f90183d9304b3516c126c708f;
  receipt evidence/k4_split_v1/AUTOMORPHISM_S3_567_r2.json SHA-256
  d688277f10096cd652293c31b7dc8ae337bb647fa914382d09c2d9c11844357c (run 17:02:06–17:02:28 PDT, 21.5 s, max RSS
  1.63 GiB, 1 CPU, alongside the K5 depth-2 pipeline as authorised).

## 1. Transfer lemma (pure logic)
Let F be a CNF on variables 1..V and π a permutation of {1..V}, extended to literals by π(−v) = −π(v) and to clauses
and formulas literal-wise. Call π an automorphism of F if π(F) = F as multisets of clauses (a clause compared as the
sorted vector of its literals). Then for every set c of literals: F ∧ c is satisfiable ⇔ F ∧ π(c) is satisfiable.
Proof: if α ⊨ F ∧ c put β(π(v)) := α(v). Each clause D of F equals π(C) for a clause C of F; α makes some l ∈ C true,
so β makes π(l) ∈ D true; each unit π(l) of π(c) has β(π(l)) = α(l) = ⊤. Conversely use π⁻¹, also an automorphism.
Moreover a DRAT refutation P of F ∧ c renames to a DRAT refutation π(P) of F ∧ π(c) (RUP and RAT are invariant
under variable renaming). Automorphisms of F form a group; for a word w = (h1, …, hm) of generators put
π_w := π_{h1} ∘ … ∘ π_{hm} (rightmost applied first).
Leaf CNFs are base + one unit per literal, so a leaf with literal set c is the formula F4 ∧ c (unit order irrelevant).

## 2. What the receipt establishes (exact checks on the actual CNF bytes)
2.1 Generators: σ1 = (5 6), σ2 = (6 7) acting on {0..7} simultaneously as rows, columns and coordinates
(cell (i,j) ↦ (σi, σj)), with ρ1 = (Q2 Q3), ρ2 = (Q3 Q4) (the squares whose (1,0) supports are {5},{6},{7}); Q1 and
the weight-1 square (label 5) are fixed.
2.2 For each of identity, π1, π2: π is total on all 513184 variables and a bijection; π(F4) = F4 EXACTLY — for every
clause length the lexicographically sorted matrices of ascending int32 literal rows of F4 and π(F4) are identical
(no hashing). Group: π1² = π2² = id, π1π2 ≠ id, (π1π2)³ = id, closure has order 6, and all six elements are
automorphisms (each checked exactly).
2.3 How π was built does not matter for soundness: any bijection passing 2.2 is an automorphism. The semantic name
table (canonical identities g ↦ (s,{p,q}); b3 ↦ (s,{x,y},z); c4 ↦ (s,a,{p,q}); u5 ↦ (s,line,q,a); w3 ↦ (s,line,p);
injective on all variables) is only the construction route; it also explains WHY π is an automorphism (the encoding is
invariant under the moves (α)+(β) with σ, which preserve row-0 standard form, L(1,0) = 1, L(i,0) = i, the K4 SB2 units,
all-frames P4 on Q1–Q4 and weight1 on L).
2.4 Cube variables: every group element maps each V1 root assignment (DIMACS 57,106,155,204,253,302,351) to a V1 root
assignment, and (rows 2, 3 are fixed by σ) the stabiliser of each root representative maps V2 assignments to V2
assignments. Orbits: 64 root orbits; non-singleton hard/moderate orbits {c016,c032,c064}, {c017,c033,c065},
{c048,c080,c096}, {c049,c081,c097}, {c028,c044,c076}; singletons c001, c112, c012, c013. Stabiliser orders:
6 for c001, c012, c013, c112 (64 child orbits each), 2 for c016, c017, c028, c048, c049 (96 child orbits each).
2.5 Controls: identity PASS; σ = (4 5) with ρ = id FAIL (moves the SB2 units); π1 with the images of variables 57
and 64 swapped FAIL (bijection kept, clause multiset differs).

## 3. Ledger contract (K4 ledger, implementation to be reviewed before use)
3.1 New evidence kind "orbit" for state CERTIFIED: {kind: "orbit", source: leaf id R, word: [h1,…,hm] over
{"g1","g2"}, automorphism_receipt: {path, sha256 = d688277f…357c}}. Validator obligations:
 (a) the receipt is the pinned one, its verdict fields are all true and its base SHA equals the ledger base SHA;
 (b) π_w is recomputed from the generator definitions (σ, ρ) and the pinned name table on the g-variables (leaf
     literals are g-variables only), and π_w(lits(R)) = lits(L) must hold as literal SETS; images outside the chain
     simply fail this test (V4–V6 are permuted among themselves and V7/V8 move to square-3/4 variables, so orbit
     certificates are available only for leaves whose literals lie in V1–V3; rows 2–4 are fixed by σ);
 (c) R is SETTLED: CERTIFIED by a strict receipt, or REFINED with every child SETTLED (closed subtree), or CERTIFIED by
     orbit from a settled source; the orbit-evidence graph must be acyclic (topological check);
 (d) L is a terminal leaf (never refined) — an orbit-certified leaf has no children.
3.2 Use at depth 1 (roots): the strict pipeline runs every root EXCEPT the non-representative members of the five
non-singleton hard/moderate orbits (c032, c064, c033, c065, c080, c096, c081, c097, c044, c076); those ten are
certified by orbit from their representatives (c016, c017, c048, c049, c028) once each representative is settled.
All other roots (including the other non-representatives, which are trivial) are run strictly.
3.3 Use at depth 2 (stabiliser reduction): an UNKNOWN representative root R is refined into its 128 V2 children as
usual; one child per orbit of the stabiliser H_R is run strictly, every other child is certified by orbit from a
sibling via a word with π_w ∈ H_R (so π_w(lits(R)) = lits(R) and π_w maps the sibling's literals to the child's).
3.4 Completeness is unchanged: complete ⇔ every terminal leaf CERTIFIED (strict or orbit) with all obligations; the
128-root partition and every 128-child family remain explicit in the ledger.

## 4. Parent replay
(1) Re-run code/k4_automorphism_r2.py (≈ 22 s, ≤ 1.75 GiB) or an independent automorphism check; (2) re-solve the
representatives' strict leaves; (3) validate the ledger with the orbit rule. Orbit certificates add no solver trust
beyond the representatives' DRAT checks.
