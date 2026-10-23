# Draft amendment 4 r1: own-row/column-frame cardinality cuts for the K3 C311 cube

**Status: DRAFT, NOT FROZEN, INACTIVE.** It must not be used in any solve until it has been reviewed, every
prerequisite in §0–§1 holds, and it has been frozen as a new version. Written 2026-10-18 00:53 PDT.

It succeeds the reviewed draft `review/drafts/AMENDMENT-4.md` (d9794b9d…47d7ee). It incorporates the K3 cover desk
RESULT (0f80460c…ef84, lines 106–115), Codex M2, Claude D1/D2 and the polish items m11–m14, as dispositioned by the
parent (fbfc0e10…f369, Q5). The interim unreviewed text written at 23:47 (`AMENDMENT-4.r2.md`, numbered before this
request) is retired to `archive/` and superseded by this draft. No claim about K3 or M(7) is made here.

## 0. Hypotheses (all must hold; stated explicitly)
H1. K1 is parent-accepted (`moqls7-k1-parent-verdict.md`, 1cd0603c…dfb8).
H2. K2 is parent-accepted (`moqls7-k2-parent-verdict.md`, 25ecb6ba…1242). With H1, every non-classical MOQLS(7)
    triple has three non-classical squares and minimises the number of non-classical squares. By the G4 argument
    (`GRAM-ENCODING.r2.md` §2, `LEMMAS.md` 69–78), every square is then heavy on all of its own ONB lines.
H3. Accepted encoder bridge(s): the G1–G5 necessary conditions of `GRAM-ENCODING.r2.md` for the encoder(s) used.
    Encoder B may be used only together with the B-map erratum and the passed runtime oracle
    (`K3-ERRATA.r1.md` E1; `evidence/k3cubes/bmap_oracle_r1.json`, 6e2bd95e…952c).
H4. Scope: K3 only. Three quantum squares; the ONB lines are the 14 rows and columns; there are no classical symbol
    lines. Only minimal configurations are covered, which by H1–H2 is every K3 configuration.
H5. Accepted three-cube cover and --sym WLOG (parent disposition Q1, with the K3-ERRATA E4 wording).

## 1. Gate on accepted exclusions, not on producer certificates
G1. A parent verdict accepting the exclusion of the exact C321 CNF (d598507d84a8d7595b30a100d528dca08bc0ce1aa71978583f09aac188298388).
G2. A parent verdict accepting the exclusion of the exact C411 CNF (2b92f5b15cd641e4a07ecec241b7957deac972aa3c7333056ff3e739e46addf2).
Both verdicts must state their standard (A-route only, or A+B). Producer certificate receipts alone do not satisfy
G1 or G2. A full-cap UNKNOWN or miss on C311 is **not** a premise: the cuts follow from G1, G2 and the transport
lemma alone. Both lex screens of C311 were resource-interrupted UNKNOWNs, and nothing is inferred from them.

## 2. Transport lemma (own row/column frames only)
Let ℓ be any of the 14 own row/column lines of the triple, and p any point off ℓ. For each square x let w_x be the
number of r ∈ ℓ with g_x(p,r) = 1.

- w_x ≥ 1. ψ_{x,p} is a unit vector expanded in the ONB on ℓ (Boolean: G3).
- The point of ℓ that shares p's other line (its column if ℓ is a row, its row if ℓ is a column) has g_x(p,·) = 0
  by G1. The neighbour sets of the three squares on the remaining six points are pairwise disjoint by G5.
  Hence w_1 + w_2 + w_3 ≤ 6.

**Case (4,1,1).** If some w_a ≥ 4, the counts are exactly (4,1,1), and all six positions are used. Apply:
- a transpose of the cell array first, if ℓ is a column;
- a row relabelling ρ with ρ(ℓ) = 0 and ρ(row of p) = 1, other rows arbitrary;
- a column relabelling κ with κ(column of p) = 0, the four a-neighbours to columns {1,2,3,4}, the b-neighbour to
  {5} and the c-neighbour to {6};
- square relabelling a → 1, b → 2, c → 3.
The image meets every one of C411's 18 signed literals, the --sym units (square 1 has neighbours in columns 1,2,3),
every G1–G5 constraint and every G4 heavy constraint (H2, all lines). G6 follows by `G6-G2-DERIVATION.r1.md`. This
contradicts G2.

**Case (3,2,1).** If w_a ≥ 3 and w_b ≥ 2 for distinct a, b, the counts are exactly (3,2,1). Use the same maps with
the a-neighbours to {1,2,3}, the b-neighbours to {4,5}, the c-neighbour to {6}, and a → 1, b → 2, c → 3. The image
is C321, contradicting G1.

Transposition preserves the QLS axioms and globally reindexes every tensor ONB. This is existence transport; it is
not claimed to be one of the source's listed set-isotopy generators. No transport through arbitrary ONBs or through
classical symbol lines is used.

**Consequence.** In every own row/column frame and at every off-line point, w_x ≤ 3 and never (w_x ≥ 3 and w_y ≥ 2)
for x ≠ y. Every heavy local type is therefore (3,1,1).

## 3. Cut generator specification (to be implemented, reviewed and frozen)
Each frame has 42 off-line points and each point has 6 structurally available positions; 14 × 42 = 588.
- At-most-three: for each square x and each four-subset R of the 6 positions, the clause
  OR_{r∈R} NOT g_x(p,r). Count 588 · 3 · 15 = 26460.
- Mixed: for each ordered pair x ≠ y, each three-subset R and each disjoint two-subset T, the clause
  OR_{r∈R} NOT g_x(p,r) OR OR_{t∈T} NOT g_y(p,t). Count 588 · 6 · 20 · 3 = 211680. Overlapping R and T are
  implied by G5 and are omitted.
- Total 238140 clauses, all distinct, no auxiliary variables.
- Per-encoder literal map: encoder A's map (asserted at run time) and encoder B's map (identical by the oracle).
- The generator binds its output SHA, the source cube CNF SHA, its own code SHA and the clause counts. It must
  stream, or include the strengthened CNF size in the projected growth of its launch gate. No duplicated CNF or
  proof files.

## 4. Controls before any use
C1. Finite local coverage: enumerate every assignment of the 6 positions to {unused, 1, 2, 3} with each square
    nonempty. Show that the cut clauses reject exactly the assignments of type (4,1,1) or (3,2,1), and keep the
    others.
C2. Clause distinctness and exact counts (26460 + 211680).
C3. Literal-map check for each encoder used, including B through the oracle.
C4. If combined with the AMENDMENT-3 lex leaders: the cut family is invariant under all row, column and square
    permutations and under transposition, and hence under the generators of H. The lex coverage argument then
    applies to base ∧ cube ∧ cuts. This is to be stated and reviewed, not assumed.

## 5. Instance and certification
- Name the instance before use: either the original C311 (7fca33f1e6324cbe17bc44bbea7f8d9188bcac187252d766fb0fa5e39e1c2001)
  plus cuts, or the lex C311 (059be6164176ee93c94d93bd47fa1d365477b6c94f3aa867df991f677e1a8c4f) plus cuts.
- The old C321/C411 proofs certify nothing about a strengthened C311 CNF.
- Any UNSAT needs a newly regenerated, DRAT-checked proof of the exact strengthened input on the protocol's
  independent route(s), plus parent replay. A SAT is a Boolean pattern only. A timeout is UNKNOWN.

## 6. Full composition to be reviewed by the parent
K1 ∧ K2 ⇒ G4 on all own lines ⇒ --sym WLOG ⇒ three cubes ⇒ {C321 and C411 accepted (G1, G2); transport ⇒ cuts;
C311 + cuts certified} ⇒ K3 excluded. Only after this composition is reviewed and accepted would the K1, K2 and K3
exclusions together bear on M(7). No such conclusion is drawn here.

## 7. Resource and freeze rules
Every native stage needs its own fresh gate: free space ≥ 12.2e9 bytes plus projected retained growth, with the
continuous 12e9 floor. A failed gate is reported once, and the worker then waits. The draft becomes usable only as a
new frozen version, after review, with H1–H5 and G1–G2 satisfied and C1–C3 (and C4 if lex is combined) passed.
