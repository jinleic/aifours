# Peer reconstruction: Shor factor-coprime multiplier saturation v1

Reviewer: MathSun8 (math-6), ordinary in-harness peer, supplied-proof reconstruction; not blind, cross-vendor, human or formal review. Observed before creation: `2026-10-23T14:19:10-0700` (`/bin/date`). Assigned by `institute/runs/three-area-2026-10-23-96h/peer-review-wave-eighteen-v1.json`.

## Snapshot and verdict

Reviewed source: `mathematics/evidence/three-area-20261023-96h/parallel-18/shor-completion/proof-multiplier-saturation-v1.md`, **complete lines1–97**, actual metadata SHA256 observed by `shasum -a 256`:

    67d8b1fdd87c4010bf1818971b4cd6dbabb5ef054160563d4b1fb36c54a4068a

This matches the parent's frozen pin. **0 FATAL / 0 MAJOR / 0 MINOR at the explicit scope below. No substantive defect found.** The written separator and all-t injectivity are correct. Application to every factor-coprime transform is correct RELATIVE TO the stated actual-border and external-theorem interfaces. This is a failure/saturation of a known-word collision route, NOT a new order restriction, noncompletion theorem, completion construction, surjectivity theorem or full-target acceptance.

## What I read independently

- Actual slot selection, complete `shor-completion/selection-v1.md`, especially exact code/quantifiers, border orientation and trust boundaries.
- Old dossier `mathematics/shor-code-finite-completion/README.md` lines1–66 and `evidence/raw-instance.json` (all16 pairs).
- `mathematics/shor-code-finite-completion/proof.md` lines34–169, in particular the actual border definitions, all-t tiling map, inclusions R0/L0, and existing multiplier cardinality conditions.
- October22 operative erratum, complete `continuation-20261022/OPERATIVE-ERRATUM-AND-REVIEW-DISPOSITION-v1.md`, and the Rédei manuscript lines1–99. These explicitly retain the unread Szabó–Sands monograph proof and unauthenticated2006 source limits and deny a genuinely new numerical condition.
- Cordero2023 retained primary `sources/cordero2023.txt` lines302–323 (difference-graph definition and Proposition2.4) and1148–1195 (Theorem7.2 statement and its displayed proof). Theorem7.2 states d1 prime to |Q| for the LEFT exponent and d2 prime to |P| for the RIGHT exponent, preserving compatibility and the same border. I retain this as an explicitly imported theorem, not a kernel-checked theorem. The author independently declares that same boundary.

No source/checker/solver/Lean/modelCLI was executed. Hashing and source reads are metadata/literature operations, not scientific replay.

## Raw reconstruction

### 1. Exact differences and residue separator (author lines51–65)

The ordered left exponents are0,3,8,11. Their six positive pair differences are3,8,11,5,8,3, whose support is exactly D={3,5,8,11}.

Row0 right exponents0,1,7,13,14 have difference support {1,6,7,12,13,14}; rows3/8 with0,2,4,6 contribute {2,4,6}; row11 with0,1,2 contributes {1,2}. Their union is exactly S={1,2,4,6,7,12,13,14}. R0 differences are the row0 list, and L0 differences are D.

Because8,3,5,11 divide n, the corresponding divisibility tests on Z_n are independent of the representative. If gcd(v,330)=1, then v is odd and prime to3,5,11. Each s∈S is prime to5 and11, has 2-adic valuation at most2, and if divisible by3 is even (s=6 or12). Thus ±vs belongs to T and is nonzero modulo n. In contrast, for odd u, ±3u is odd and3-divisible, ±5u and ±11u are divisible by their respective forbidden primes, and ±8u is8-divisible. Odd ud with d∈{3,5,11} cannot vanish modulo8; ±8u is nonzero by the explicit guard. Hence every nonzero row difference is outside T.

This proves S1's16-point injectivity: different source rows cannot merge; within one row different right exponents cannot merge. It uses no assumption that u or v is a unit modulo n.

### 2. Graph direction and mixed multipliers (author lines67 and40)

The primary graph is on DISTINCT points/words: an edge has source i−i' and target j'−j. Therefore a source-zero edge in a transformed C uses the same source row and distinct right exponents, so its target is a nonzero element of T. Every nonzero source lies in ±uD and hence outside T. T therefore has no outgoing edges, even after superposing all admissible transforms. A nonempty path leaving0 enters T and cannot continue or return. No source0→target0 self-edge is supplied by the primary distinct-word graph definition.

This checks the required orientation and confirms the claim is not the false statement that the UNION of all transformed word sets is a UD code. Edges are formed inside individual transforms, although different edges in the superposition may come from different transforms.

### 3. The all-t border product (author lines69–75)

For t=0, equality r+l=r'+l' yields Δr=−Δl. A nonzero Δr is in T; a nonzero Δl is outside T. Since T=−T, this is impossible. If one vanishes, both vanish.

For arbitrary finite t≥1, equal first coordinates give Δr=−Δi1. The same separation forces both zero, hence the first source rows agree. The first right difference is now either zero or in T. Equality at the next coordinate forces it to equal the negative of the next row difference (zero or outside T), so both vanish. Repeat through all t middle positions. The final coordinate compares the last right difference with a difference in L0 and forces both zero. S1 supplies distinctness inside every transformed row. Thus all input coordinates agree. This is an induction for every t, not a finite sample or bounded-length test.

The argument only compares two tuples using the SAME chosen Z_k at position k, exactly as author line47 states. It proves INJECTIVITY on R0×Z1×...×Zt×L0, not tiling by unknown full borders and not surjectivity onto Z_n^(t+1).

### 4. Covering the complete permitted multiplier class (author lines81–87)

The imported actual border is (P,Q)=(R,L), so the primary permission is gcd(u,ell)=1 on left exponents and gcd(v,r)=1 on right exponents. Since ell is even, u is odd. The declared Rédei cardinality input gives an odd prime p|ell; if n|8u then p|u, contradicting gcd(u,ell)=1. Thus the nonunit guard8u≠0 mod n is satisfied. Finally330|r and gcd(v,r)=1 imply gcd(v,330)=1. Every permitted transform of the forced16 pairs is therefore covered by the purely combinatorial theorem. Repeated permitted transformations multiply admissible factors and preserve these necessary conditions; fixed arbitrary positionwise choices are already covered by the all-t result.

Cordero's theorem is applied to a full hypothetical n-cbc family; C itself need not have n elements. Its transformed16 points are forced SUBSETS of those full transforms. Injectivity of these subsets creates no existence assertion for a compatible full n-cbc, full border, or finite raw-word code.

## Trust, scope, novelty and significance

- **Correctness:** written reconstruction finds no substantive defect at S1–S3 and the conditional application boundary.
- **Import trust:** actual completion→border/all-t data remain an inherited written interface; the Rédei cardinality theorem retains its unread-monograph-proof boundary; Cordero7.2 is an explicit primary theorem import. This review does not promote their formal status.
- **Scope:** the known-word/known-border multiplier-collision route is closed by a separator. Unknown words and unknown border elements, actual cardinality n and finite-code realization remain unrestricted and unresolved.
- **Novelty:** not cleared against the original2006 argument, the inaccessible Sands construction or other earlier equivalents. This review supplies no novelty certificate.
- **Significance:** useful attack-pruning / method-limit result. It is NOT a stronger n-restriction or progress count toward an all-order noncompletion theorem merely because it handles non-units.

The assigned bounded reconstruction is complete. I now return to the Sun8 primary problem; no reviewer-only slot or nested delegation was created.
