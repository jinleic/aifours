# v36-B — written reconstruction of unrestricted prime-order Tuscan asymmetry

Reviewer MathOlson-2-2 (owner MathOlson-2), author InfoRecursiveMDS18. Actual returned clock before creation: **Sun Oct 25 05:11:30 PDT 2026**. The exposure ACK `peer-review-tuscan-prime-asymmetry-ack-v1.json` was created before reading the literal source body.

## 1. Verdict

**WRITTEN_RECONSTRUCTED at the literal complete-array and safe-action scope. Findings: 0 FATAL / 0 MAJOR / 0 MINOR.** No author correction requested.

Reconstructed conclusions:

1. A complete Tuscan-1 square of every odd order n>=3 has NO reversal-symbol automorphism under one global row reversal and one common symbol permutation.
2. At odd PRIME order p its symbol automorphism group is trivial.
3. Consequently a hypothetical unrestricted Tuscan-2(11) square has trivial automorphism group under the stated row-permutation/symbol-relabel/global-reversal action, and its equivalence class has exactly22 distinct SAFE standard-form arrays.

This is neither an existence theorem nor an all-array nonexistence theorem. It does not extend trivial symbol automorphisms to odd composite order. No column-Latin, wraparound, arbitrary column-permutation or independent-row-reversal action is used.

Same-harness supplied-proof written reconstruction only: not blind, cross-vendor, configured dual-family, human, formal/kernel, executable or novelty acceptance. Parent disposition is separate. No scientific interpreter, eval, arithmetic program, symbolic computation, enumeration, replay, solver, nested agent or external CLI was used.

## 2. Snapshot, exposure and literal coverage

Read the exact v36-B entry and full packet receipt, and reread all39LF parent erratumv7 before ACK. Fresh metadata hashes:

- Manifest `peer-review-wave-eighteen-v36.json`: `5479e372314da599f6cded96e604621305b3fda081a4f108a45025ba409edbfe`.
- Packet receipt `peer-review-wave-eighteen-v36-packet-receipt-v1.json`: `29752d9ea2e5972dfc281471f2b0907eccf53381a466714115d30f078109362e`.
- Literal packet `peer-review-wave-v36-tuscan-prime-asymmetry-sources-v1.md`: `c95e70b17b30a6c446e76d46fc5f9facdb8065ae56b547fa1224c663895f262b`,8435bytes. Read raw ranges1–107 and108–109, the entire109-LF packet with every author line1–100.
- Actual author source `information-science/evidence/three-area-20261023-96h/parallel-18/tuscan2-11/unrestricted-prime-order-asymmetry-v1.md`: `ac898bee2bb750d48b171f364c10a3e356f06c3d0105bf613dfb726f336235e7`,100LF,7861bytes, matching manifest. The receipt reports literal equality; this review independently observes the source/packet hashes and full literal text, not a new programmatic re-render.

The linked mandatory `kernel-admission-correction-addendum-v1.md` was additionally read completely through LF35 and freshly hashed as `b3ca05c7e7710af1f987c2b100b7873602424ffd62b50f288a91f333b9e8d68b`. Its prior computation disclosures receive no verification credit. They are not premises of the new symmetry proof.

No prior whole-body read of this new theorem occurred in this runtime before ACK. Earlier round summaries exposed the Tuscan target but supplied no verdict inherited here. Citations below refer to original author-source LF.

## 3. Exact objects and safe group action

The source LF9–11 assumes n COMPLETE rows, each an ordered permutation of the same n-element symbol set X, and a bijective linear adjacency covering. These are Tuscan-1 squares, not incomplete rectangles or capped partial arrays. Rows are distinct: otherwise two identical length-n permutations would repeat each of their n-1 adjacent ordered pairs.

Write R for the row set. Simultaneous symbol permutations act entrywise. Let Rev reverse every row in the same global orientation. Rev commutes with all symbol permutations. Therefore the safe row-set automorphisms form a genuine subgroup

    K <= Sym(X) x C2.

The reversal bit is a homomorphism; its kernel G is precisely the symbol automorphism group. Arbitrary row permutations are absorbed by treating rows as a set. This does not erase an additional automorphism: because the rows are distinct, a given symbol/orientation operation preserving R determines its induced row permutation uniquely. If it is the identity operation, the only row permutation fixing the labelled array is the identity.

No other column operation is present. In particular Rev is not an independent reversal of selected rows and is not a cyclic shift of columns.

## 4. Endpoint counts and free actions

For a symbol a there is exactly one occurrence in each of the n rows. Every occurrence except a terminal one contributes one outgoing adjacency event. Since there are exactly n-1 distinct ordered pairs (a,b), b!=a, and all are covered once,

    n-e(a)=n-1, hence e(a)=1.

Likewise incoming events give exactly one row starting with a. This proves LF23–27 without requiring Latin columns. It only says that the first and last columns are permutations as a derived consequence; it does not make every other column Latin.

If g in G fixes one row as an ordered tuple, it fixes all n symbols in that row and is the identity. Thus G acts freely on the n-element row set. Each orbit has |G| elements, so |G| divides n (LF29–31).

If a nonidentity g fixed a symbol a, it would preserve the unique row beginning with a. That would fix an ordered row, a contradiction. Thus G also acts freely on symbols. It acts freely on adjacency EVENTS as well: an event is (row,c),0<=c<=n-2, and a symbol permutation changes its row but preserves c; an event stabilizer would fix that row. These are free actions on actual tuples/events, not an assumed cyclic-development action.

The adjacency-event set has n(n-1) elements and maps bijectively, by coverage, to all n(n-1) ordered distinct symbol pairs. This map is equivariant for every allowed symbol/global-reversal operation. That exact bijection, rather than only an event count, is the key to the reversal proof.

## 5. No reversal-symbol automorphism at odd order

Since |G| divides odd n, |G| is odd. If K contains a reversal-bit-one element, the reversal projection is onto and |K|=2|G|. Cauchy's elementary theorem gives an involution outside G, necessarily (h,Rev), with h^2=id (LF37–41).

There is also a direct check avoiding any ambiguity about Cauchy: if k has reversal bit1, k^2 belongs to the odd group G; let its order be the odd integer m. Then k^m has reversal bit1 and square1, so gives the required involution. The square condition is in the actual direct-product action, not merely in an abstract quotient.

On an adjacency event its action is

    (row,c) -> (h(Rev(row)), n-2-c).

Odd n makes n-2 odd. The equation c=n-2-c has no integer solution. Hence this involution has no fixed adjacency event, whether or not its row is preserved.

If h has a transposition (a b), its action on the ordered pair (a,b) is

    (a,b) -> (h(b),h(a))=(a,b).

The pair's UNIQUE covering event must then be fixed by equivariance of the adjacency bijection, impossible. An involution h has only fixed points and transpositions, so h must be the identity (LF43–54).

The remaining involution would be pure global reversal. Its induced permutation on an odd number n of rows must fix a row, since nonfixed orbits have size2. But an ordered row permutation equal to its reversal would have equal first and last entries; they are distinct for n>=2. Contradiction. This excludes every reversal-symbol automorphism, not only those originally of order2 (LF56–58).

Both parity uses are essential and correctly scoped: n odd removes fixed adjacency positions and forces a fixed row under pure reversal. No wraparound adjacency is inserted; the last-to-first pair is not an event.

## 6. Prime-order symbol rigidity

At n=p odd prime, |G| divides p. If G were nontrivial, it would have order p and be cyclic. Its free actions on both p rows and p symbols are therefore regular. Choose a generator and label the symbols by F_p along its symbol orbit so that it acts by x->x+1. The row set is the p translates of one starter permutation

    a0,a1,...,a_(p-1).

For each nonzero delta, the p directed pairs (x,x+delta) form one translation orbit. A starter edge with difference delta develops into ALL p pairs of that orbit. Two starter edges of the same difference would cover that entire orbit twice; a missing difference would leave its whole orbit uncovered. Thus the starter's p-1 linear adjacent differences enumerate every nonzero field element once (LF62–72).

Their sum is zero: pair each delta with -delta, which is distinct from it at odd p. But their telescoping sum is a_(p-1)-a0, nonzero because the starter is a permutation with distinct first and last entries. Contradiction. Therefore G is trivial (LF72–76).

This is a proof for EVERY possible symbol automorphism: the cyclic development is DERIVED from the group action, not imposed as a search ansatz. At odd composite n, the group could be a proper nontrivial divisor-order subgroup; the regular-p argument would not follow, and the source does not claim otherwise.

The consequences in LF78 are also correctly limited. A hypothetical complete eleven-row set invariant under any nonidentity multiplicative/QR/power symbol permutation is ruled out at Tuscan-1 level. A family of possible rows can still be used to select an asymmetric eleven-row set; no such mixture is excluded by the group statement alone.

## 7. Exactly22 safe standard forms

At p=11, both symbol and reversal-symbol automorphisms are absent. For each original row r and orientation epsilon in {0,1}, orient ALL rows by epsilon. The chosen row is an eleven-symbol permutation, so there is exactly one global symbol relabelling g taking it entrywise to (0,1,...,10). Apply g to the entire row set.

The endpoint count says there is exactly one row starting with each symbol. Sorting by that first symbol uniquely orders the rows; the chosen natural row is row0. The resulting first column is (0,1,...,10), with no extra column-Latin assumption.

For injectivity, suppose choices (r,epsilon,g) and (r',epsilon',g') give the same standard array. Equality of their row sets makes

    (g')^(-1)g composed with Rev^(epsilon+epsilon')

an automorphism of the original row set. The theorem forces the symbol map and reversal bit both to be identity. Thus epsilon=epsilon' and g=g'. The common bijection cannot take two different oriented rows to the same natural tuple, so r=r'. All 11*2=22 outputs are distinct (LF84–90).

For surjectivity, any safe equivalent array with row0 natural and first column natural comes from a global orientation, a symbol permutation and a row permutation. Its natural row0 identifies one oriented original row r and fixes the symbol relabelling uniquely. Its natural first column fixes the row ordering uniquely by the endpoint count. It is therefore exactly the output of that (r,epsilon) choice. Thus22 is exact, not merely an upper bound (LF92).

The lexicographically least of this complete22-element set is consequently an invariant canonical representative for the stated safe equivalence class. It does not assert that there are22 equivalence classes or any existing square.

Tuscan-2 status is preserved by every safe operation: row permutation reorders events, symbol relabelling bijects their ordered labels, and global reversal swaps ordered endpoint labels while bijecting their linear positions for each distance. At order11 there are110 adjacency events and99 distance2 events. The proof requires exact adjacency coverage, but does not incorrectly demand coverage of all110 pairs by the99 distance2 events.

## 8. Exact limits and NOT_RECONSTRUCTED obligations

- **NOT_PROVED:** existence or nonexistence of any complete asymmetric Tuscan-2(11) array. All theorems here are conditional statements about a complete array if one exists.
- **NOT_RECONSTRUCTED:** any old finite-family, projective-colouring, suffix-prefix or unrestricted search/cutoff calculation. The linked admission addendum lists their unadmitted computation history; none is a premise of the new proof or accepted by this review.
- **NOT_CLAIMED:** odd-composite trivial symbol automorphism; even-order reversal exclusion; rectangle/partial-array rigidity; arbitrary column symmetry; independent row reversal; a cyclic-row restriction; Latin middle columns; circular/wraparound adjacency; or any fixed second row.
- **NOT_PERFORMED:** external priority/SOTA audit, human or formal/kernel verification, independent executable reconstruction, resource/exit attestation, or parent acceptance. The classical starter sum identity is correctly credited as classical rather than advertised as new.

No missing mathematical assumption was found within the explicitly stated complete Tuscan-1 and safe-action scope. LF96–100 correctly preserve the actual target: an eleven-by-eleven table with the full linear adjacency/distance2 criteria or an argument covering every asymmetric array. The structural symmetry theorem supplies neither target deliverable by itself.

**Disposition:** zero author findings, no repair requested; ordinary written support at exactly the above scope is justified. Parent retains its separate full-source disposition and all v7/admission qualifications. No new scientific launch or GO follows.
