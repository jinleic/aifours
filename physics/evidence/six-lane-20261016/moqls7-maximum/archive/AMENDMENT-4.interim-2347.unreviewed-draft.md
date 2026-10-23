# Draft amendment 4 r2: proof-assisted all-frame K3 cardinality cuts

NOT FROZEN OR ACTIVE. No new cut CNF, enumerator or search is authorised by this draft. It revises the earlier
unfrozen `AMENDMENT-4.md` without altering it: C321/C411 now have producer-checked A certificates, while both C311
lex runs were resource-interrupted before their1800-second caps. Those interruptions are not evidence of
nonexistence or completed heuristic failures. The mathematical cut justification does not require a full-cap
C311 miss; it depends on the two independently justified local exclusions below. The representation is prepared
for a future resource-qualified continuation, not a blind restart with accumulated runtime falsely claimed.

## Load-bearing local exclusions
- Original A/C321 receipt: `evidence/k3cubes/cert_r2/A_C321.json`, SHA-256
  c3a30df311eff2ed9b9b5a3706c2ca03a8d4337d8663ea529a9978126fde9314.
- Original A/C411 receipt: `evidence/k3cubes/cert_r2/A_C411.json`, SHA-256
  5f117b60c6b7833978ea012b3c07921d2d19fa6d0a161c4b93d1d13cd6aa23cf.
Both record solver20/checker0/exact `s VERIFIED` without a safety stop. Their base G1–G5/heavy and three-cube
coverage bridges still inherit the parent's mathematical/integration acceptance requirements. G6 is redundant
by `G6-G2-DERIVATION.r1.md`; no new algebraic ansatz is introduced.

## Transport lemma
For any own row/column frame ell and point p off it, write w_a for the number of g_a-neighbours of p on ell.
G3 gives w_a>=1. G1 excludes the unique same-column/same-row point of the frame, and G5 makes the three neighbour
sets disjoint among the six remaining positions. Hence their weights sum to at most six.

If some w_a>=4, the weights are exactly(4,1,1). Permute square labels, row/column labels and, for a column frame,
transpose the cell array, to place ell at row0, p at(1,0), the four neighbours at columns1–4, and the singleton
neighbours at5/6. This is C411, contrary to its checked exclusion.

If distinct a,b have w_a>=3 and w_b>=2, the weights are exactly(3,2,1). The same transport puts it in C321, also
excluded. All G1–G5/heavy conditions transport; transposition preserves QLS and globally reindexes tensor ONBs,
regardless of whether it belongs to the source's narrower listed isotopy generators. Cube G6 follows automatically.

Thus every surviving minimal heavy K3 configuration must have, in every row/column frame,

    w_a <= 3;  never(w_a>=3 AND w_b>=2) for a!=b.

All heavy local types must be(3,1,1). This imports consequences of the two checked three-square cases, not the old
four-square theorem. It is a proof-composition step and must be reviewed as such.

## Direct clauses and obligations before activation
For each of14 frames,42 off-line points and6 structurally available positions:
- For every square and four-subset R append OR_{r in R} NOT g_a(p,r):26460 clauses.
- For every ordered distinct square pair, every three-subset R and disjoint two-subset T append
  OR_{r in R} NOT g_a(p,r) OR OR_{t in T} NOT g_b(p,t):211680 clauses.
Total238140 clauses, no auxiliaries. Overlapping subsets are already impossible by G5.

Before any use: accept/pin the transport bridge; independently check the cardinality schema over all local
unused/square1/square2/square3 assignments with each square nonempty; bind both upstream cube certificates;
implement and freeze exact generation/byte hashes; obey the parent's fresh>=12.2e9 plus projected-growth gate,
minimal retained logs/receipts and no duplicated CNF/proof files. A RAM/streamed input method would be needed if
new retained formulas are disallowed. No such implementation or finite-control execution is asserted here.

A subsequent SAT remains a Boolean pattern, not vectors. A new UNSAT needs regenerated checked proofs and the
separate independent-encoding/parent routes. Both upstream case proofs remain load-bearing. Until resource release
and all these gates, this draft remains inactive and M(7) is unresolved.
