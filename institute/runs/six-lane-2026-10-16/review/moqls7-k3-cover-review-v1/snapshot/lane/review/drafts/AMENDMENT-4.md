# Draft protocol amendment 4: proof-assisted all-frame K3 cardinality cuts

NOT FROZEN OR AUTHORISED FOR SEARCH YET. This is a prepared representation for use only after the original C321
and C411 cubes have checked UNSAT certificates, and only if C311 remains UNKNOWN after its frozen residual-symmetry
screen. It is not a claim that either cube is already certified. It changes no target or previous evidence.

## 1. Transporting the two local exclusions
Assume the original C321 and C411 cube CNFs are UNSAT under G1-G5 plus their exact cube units. Their G6 additions
are redundant by `G6-G2-DERIVATION.r1.md`. Consider any row or column frame ell, any point p outside it, and define

    w_a(p,ell) = number of r in ell with g_a(p,r)=1.

For each of the three squares this count is nonzero. G1 excludes the unique point of ell sharing p's other line
(column for a row frame, row for a column frame); G5 makes the three neighbour sets disjoint. Thus

    w_1 + w_2 + w_3 <= 6, each w_a >= 1.

If some w_a >= 4, these counts must be (4,1,1). Relabel square a as square1, transport ell to row0 (transpose
rows/columns if ell was a column), p to (1,0), the four neighbours to columns1-4 and the singleton neighbours to
columns5/6. This gives precisely C411, contradicting its UNSAT certificate.

If w_a >= 3 and w_b >= 2 for distinct squares, the counts must be (3,2,1). The same transport gives C321, again
contradicting its certificate. All row/column/square permutations preserve G1-G5 and the heavy conditions. A
transpose preserves QLS and globally reindexes every tensor ONB, so this is existence transport, not an assertion
that transpose belongs to the source's listed set-isotopy generators. Non-classicality and all projective-ray sets
are unchanged.

Consequently every surviving heavy K3 configuration must satisfy, for every own row/column frame and off-line p:

    w_a <= 3;
    not (w_a >= 3 and w_b >= 2), for every ordered a != b.

Every heavy occurrence is therefore type (3,1,1). This conclusion depends explicitly on the two previously checked
cube exclusions and is not imported from the old four-square theorem.

## 2. Boolean cut schema (to append, never replace the original encoders)
There are14 frames and42 off-line points per frame, with6 available neighbour positions each.
- At-most-three: for each square a and each four-subset R of the available positions, append
  OR_{r in R} not g_a(p,r).
- Mixed cut: for each ordered pair a != b, each three-subset R and each disjoint two-subset T of the available
  positions, append OR_{r in R} not g_a(p,r) OR OR_{t in T} not g_b(p,t).
  Overlapping subsets are already impossible by G5 and need no additional clause.

Combinatorial counts:14*42*3*C(6,4)=26460 clauses of the first kind and
14*42*6*C(6,3)*C(3,2)=211680 of the second kind, total238140, with no auxiliary variables. The implementation must
check these exact counts, verify all literals refer to actual non-collinear g variables and bind its output SHA.

## 3. Pre-activation obligations and controls
Before this amendment can be frozen or any new CNF generated:
1. Bind successful original C321 and C411 certificate receipts, their CNFs and the exact mathematical transport
   used above. If either certificate is absent, UNKNOWN or unverified, stop: these cuts are not justified.
2. Finish the already frozen C311 lex screen. If it is UNSAT, prefer the simpler original three-case proof rather
   than adding this layer. If it is SAT, keep that model and treat all cut-based work only as an explicitly
   conditional refinement.
3. Add finite controls of the cardinality schema across all assignments of six positions to unused/square1/
   square2/square3 with every square nonempty, showing that the appended clauses reject exactly types containing
   (4,1,1) or (3,2,1), and retain the other allowed local size types. This checks Boolean coverage, not vectors.
4. Leave original inputs unchanged; freeze code hashes and the complete representation before use. A separate
   parent/hostile review must accept this proof-composition step before any unrestricted theorem verdict.

After activation, screen at most one selected C311 instance for <=1800 native seconds. UNKNOWN remains UNKNOWN;
SAT is only a pattern. A new UNSAT needs regenerated DRAT certificates and an independent encoding route. The two
upstream cube certificates remain load-bearing evidence in any final proof using these cuts.
