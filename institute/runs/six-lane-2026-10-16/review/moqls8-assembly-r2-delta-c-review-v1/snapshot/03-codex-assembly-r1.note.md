**FATAL: 0. MAJOR: 0. MINOR: 1.**

**MINOR M1 — SOURCE00:LF7, LF34; SOURCE01:LF4–154.** “Every artifact below is fingerprinted in [the registry]” overstates the registry’s explicit coverage. For example, the original CNF, encoder and full name-table identities cited at LF34 lack their own registry entries; their binding is imported through other records. This does not break the conditional implication.

**Repair:** say “The registry fingerprints the link documents, manifests and receipts; additional identities are pinned inline or through those binding records.” Alternatively, add the missing explicit entries in a new version.

**DISPOSITION: ACCEPT-WITH-FIXES — as a conditional proof skeleton.** If NF is discharged with its stated Boolean quantifiers and all six exact strengthened formulas receive the specified binding and qualified refutations, the chain proves the n=8 statement. No fatal or major interface gap was found.

1. **Target fidelity passes.**

   SOURCE10:LF642 asks:

   > “Problem 16. Is a set of n − 3 MOQLS(n), n ≠ 4, necessarily classical?”

   Thus n=8 means five squares, and the exception is automatically satisfied.

   SOURCE10:LF195–196 requires that:

   > “each row and each column forms an orthonormal basis of Cn”

   SOURCE10:LF209–217 defines orthogonality through the cellwise tensor products forming an orthonormal basis, and requires every pair of squares to be orthogonal.

   The set isotopy permits:

   > “multiplying each entry by a phase factor”  
   > “permuting rows and columns, simultaneously among all squares”  
   > “applying, separately to each square, a unitary transformation to all of its entries.”  
   > — SOURCE10:LF220–222

   Finally, classical means:

   > “if, up to isotopy, all entries are contained in {|1⟩ , . . . , |n⟩}.”  
   > — SOURCE10:LF223–224

   SOURCE00:LF11 matches these definitions. It adds no prime-power, coefficient, or individual-square non-classicality restriction.

2. **U → T16 passes within the accepted scope.**

   Row-0 standardisation applies to every genuine five-set because each first row is an ONB and separate square unitaries are permitted. A8’s **all-five/all-entries** premise, contraposed, supplies some entry of weight at least three; W8 makes its weight exactly three. This does not require weight-three entries in the other four squares.

   The normalisation then gives the seven-coordinate partition `123 / 4 / 5 / 6 / 7`. Common row/column moves and the accompanying unitaries are allowed; square relabelling is legitimate because the object is a set. SOURCE03:LF55–75 supplies exactly the hypotheses of the repaired property-form T16 in SOURCE04:LF15–38.

   Only Q1 needs a true w3 witness flag. The other flags can be false because the four other ALO clauses were deleted. No other-square P4 premise is reintroduced.

3. **T16 → D12/NF passes, and the sixteen cases are complete.**

   T16 covers **genuine counterexample images**, rather than arbitrary Boolean models of bare `F_one`. That is sufficient: a hypothetical counterexample produces a model of one exact `B_C`; subsequent Boolean UNSAT results eliminate that model.

   The partition is exact:

   | Route | Templates | Count |
   |---|---|---:|
   | D12 | P0-B1 through P0-B6 | 6 |
   | D12 | P1-B4, P1-B6 | 2 |
   | D12 | P2-C1 through P2-C4 | 4 |
   | NF | P1-B1, P1-B2, P1-B3, P1-B5 | 4 |

   In particular, P0-B6, P1-B6 and P2-C4 are retained. The old c112 shortcut and old thirteen-case interface are expressly excluded by SOURCE02:LF29 and SOURCE04:LF26–30.

   Each `B_C` uses the same weak body and the full **42 signed Q1 units**, fixing coordinates 1–7 for rows 2–7. SB2 and constants supply the remaining column-0 support bits. Nothing requires a Boolean cover of the unfixed base.

4. **NF → S6 supplies the implication the contradiction needs.**

   For each fixed C, the required statement is precisely:

   `SAT(B_C) ⇒ OR_s SAT(B_C AND M_s)`.

   The reverse implication is immediate from conjunction, so SOURCE00:LF84’s equivalence is justified. Neither preservation of each original model nor a permutation of every auxiliary ID is needed.

   The written local argument avoids importing T16’s unitary/rank reasoning into arbitrary Boolean models. It uses G2/G3 support consequences, isolates four edges, and explicitly excludes full K33 using the distinguished degree bounds. Its bounds give at least `[1,1,2,2]` permutation columns for B1/B2/B3/B5, respectively. The displayed stabilizers then yield exactly:

   `B1:{2}; B2:{2,4}; B3:{2}; B5:{2,3}`.

   For B5, two permutation columns ensure one has label outside the singleton orbit `{7}`. No additional representative is omitted. See SOURCE06:LF39–78 and LF130–149.

   Pending NF acceptance must cover this **full Boolean theorem**, including the retained core’s invariance and auxiliary extension. The finite local receipt is correctly labelled as supporting evidence.

5. **S6 → conclusion passes subject to the stated exact binding.**

   The necessary binding is semantic as well as numerical: every tail literal must name the intended  
   `g_s((0,c),(i,0))` through the same pinned primary map used by the original formulas.

   With those identities, the 126 clauses impose at most one supported coordinate for each row `i=2..7`. G3 supplies nonemptiness, SB2 supplies row 1’s singleton, and constants handle coordinate 0 and row 0. Thus the tail expresses exactly `M_s`, without imposing whole-square classicality.

   The counts agree:

   `5,740,226 + 42 + 126 = 5,740,394`.

   Refuting all six inputs therefore eliminates all four NF source leaves; D12 eliminates the other twelve. Every genuine counterexample image is excluded.

   These six receipts would not themselves be direct native replays of the four original formulas. SOURCE00:LF90 and SOURCE01:LF232 correctly leave acceptance of that coverage/amendment route pending.

The scope labels are otherwise accurate: n=8 only; no old stronger-input certificate transfer; no unconditional theorem, whole-base UNSAT, or novelty claim. No circular dependency was found.

**Audited versus imported:** I verified all eleven snapshot SHA256 values and audited the supplied definitions, written composition, case coverage, NF combinatorics and formula interfaces. A8/W8’s underlying proofs, encoder/map/byte-binding records and D12 solver/checker facts remain imported within their stated scopes. NF acceptance and all six strengthened-input bindings/refutations remain pending. Only static snapshot reads and hashes were performed.