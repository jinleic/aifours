# b63 families 4 and 5: new review interface and residual v1

Written after host clock 2026-10-19T18:32:58-0700 by ContinuePA19d. New claims are TWO whole-family written exclusions, CANDIDATE_UNREVIEWED. **b63 itself remains UNDECIDED; zero whole cases or frontier counts change.**

## 1. Authority and preservation
The frozen assignment is RUN/control/written-slot-transition-pa19-20261019-1718-v1.json SHA256 76f00a6908c2f1e0599a75ce38179ffb1ef4633eb1094d4f4c32a7eb1033ebaa; scope-v1.md SHA256 27b13a5c19b9bc7dc885d7fc52030796dcacc53bff8dcf707c1f1d232fa7b269 froze b63 selection/exposure. Parent IRC after checkpoint-004 (whose bytes remain unchanged) directed: "Continue b63 exact six-family obligation under existing scope in new versions. Retain failed empty manifestv1 and clock erratum permanently; no timestamp inferred or evidence silently repaired. Next packet should resolve >=1 whole remaining family or explicitly isolate a mathematical blocker, not restate B1-B9. No scripts/assertions over cases; checkpoints<=1800s."

Old files are immutable. Retained failures/deviations: manifest-v1.json is empty (SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855), superseded by manifest-v2.json in the earlier delivery; b63-reduction-v1.md's unverified header clock remains in its original bytes and its required erratum is included in full. Scope's pre-freeze exposure and checkpoint history are not erased. This is a successor packet, not a modification to prior evidence.

## 2. Precise new claims and dependencies
| file | SHA256 | claim / dependency |
|---|---|---|
| b63-family4-exclusion-v1.md | 746bafcc91e857c00328d2c6cd7bbceeedc741f427fd5fdb0d201641c660c716 | NO array in family 4: G2-Q1-(a), occupancy-2 K_B, either L_B assignment, all row identities |
| b63-family5-exclusion-v1.md | a121e406a08bf954871379c488aab75344c723ff51373606e23ba9509fc2cee5 | NO array in family 5: G2-Q1-(a), occupancy-3 K_B, either z position, both high-quad positions for e0, all row identities |
| b63-reduction-v1.md | 6be58b9a82078ac9ed8df4fa4dc80d86ea91038b65885416087b05ef3a5c2aa9 | General b63 split B2; G2 common facts B4; Q1 split B6; Q1-(a) B7; spread B8; family-4 normal form B9. Supplied in FULL and NOT assumed accepted. |
| b63-reduction-v1-erratum-v1.md | 68c1ddd04d699890efacca2e0e8210b27a2329759fbd27d623a4f112a58d46c9 | Mandatory clock-only correction; no mathematical content changed |
| class-theorem-v1.md | 6343c3da3ed6c8a29da6216d90d46db7f9f095ea3726bd8e4a1173f05c9b954c | Section 1 general e=7 exact pair cover, row patterns, categories, I(r)=7, private rescue; supplied in FULL and proved, not a prior-acceptance premise |

Family-4 proof does NOT depend on family-5 proof; family-5 proof does NOT depend on family-4 proof. Both are deductions from the explicit row model and supplied general reductions. No earlier Codex/Claude PASS, pending b65 result, list coverage, numerical output or encoder execution is a mathematical premise. Finite case distinctions are by-hand written mathematical arguments; no computational enumeration, case-processing script, assertion, scientific CLI, import, compile or test occurred.

New mathematical steps, not a restatement of B1-B9:
- Family 4: derive P1 triple row distributions, force the private identity split, exhaust C-pair orientations via e0's B-triple, and exclude every remaining orientation by compatibility of the two occupancy-0 A-triples; one branch uses full P0 partner lists to force two different column-4 triples through one row.
- Family 5: force one low-quad private in each of A,B; rule out e0 in the low A-quad by f(e0)=0; force the unique P0 triple {s_L,s_A,e0}; split z's high/low position; in each position use e0 to force a high C-pair row into the other column's occupancy-0 triple. The remaining hand cases reduce to incompatible partitions of four named rows into two pairs, with every orientation and private assignment checked.

## 3. Exact case/interface binding
S = /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/cycle2/skel-b/skeletons-b-ms09.json, SHA256 7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0. FULL S is embedded. b_index 63 is zero-based half-open bytes [4256,4338), entry SHA256 6b03eb8ad5a5d05c6486cd04656e444f051a2a6677a136759c9cbf2e22149a6a:
{"types": [[0, 1, 2], [0, 4], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], "empty": 7}

The row map is g={0,1,2}, two-type rows 04,13,14,23,24,z=34; private rows p0,p0',p1,p2,p3; seven actual empty rows. In family 4 O/O' notation (written as p0*,p0*') and family 5 O/O' are the two distinct p0 rows in either order. In family 5 bare 1,2 abbreviate private p1,p2; they are NOT 2-type row labels or symbol values. No symmetry exchange of A,B is assumed for b63; only 1<->2 (13<->23,14<->24,p1<->p2) and p0<->p0' are used.

V10 = RUN/review/pa19-parent-frontier-v10.json SHA256 29c7cbe8e22cdad3bb1d196f9df12d9336652cb4942dc9538ac6d22225ebd90a. Its b63 entry is exact raw lines 4693-4740, bytes [65691,66347), embedded as source-v10-b63-v1.txt SHA256 66a3f931f5e7dc07fc28dc2d6edb4834c08c1f25ae9e42c8d871e90ce9be5026 (656 B). It binds status/identity only; ext.json denominator, interval counts and list pins are NOT premises. V10 is the frozen assignment snapshot, not a promise of latest parent counts. Binding uses b_index + exact skeleton content + whole-S SHA, never the s-tag.

Encoder definition E = PA/code/vendor/encode_skel_b.py SHA256 d0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5. Exact excerpts are E lines 3-8, source bytes [114,507), SHA256 d2badacac8e8224914d82ed27f64ee212b0ec1d9d99ed4c3d4ed8488e28f9790; E lines 77-99, bytes [3404,4286), SHA256 92f988ec1c8e36fbf50616e84c94847ca6ffd439c642bbaaba7bd891b7e94fe7. Embedded from the exact earlier excerpt files. These define types/private/empty row multiplicity and Q_c membership only; no execution, all-clause or caller certification.

## 4. Review tasks
Read the supplied reduction dependencies at their literal scopes, then audit the two NEW full proofs. Check particularly: (i) family-4 last subcase's partner lists and column assignments; (ii) family-5 exhaustiveness of the two z positions, e0 locations, C-pair orientations and a/b cases; (iii) each four-row partition obstruction is at most the three possible pair partitions, with every discarded partition's explicit repeated-pair or shared-index reason; (iv) private row identities, not just their types, stay distinct. A compatible nonempty projection is not asserted realizable; the arguments instead refute necessary conditions for every full array in each family.

## 5. Exact remaining obligation (candidate update, no ledger change)
If both new proofs are correct, all of G2-Q1-(a) (old families 4 and 5) is excluded. The remaining whole b63 obligation is precisely:
1. G1/T2 with B/C pair matching {13-24,14-23};
2. G1/T2 with {13-24,04-23} (and its 1<->2 image);
3. G2-C0 with every exceptional column and rescue triple listed in B5;
6. G2-Q1-(b): eps(L_B)=1, eps(L_C)=2, all remaining row/empty placements.
These four families remain genuinely open; no construction or infeasibility is inferred. No b63 or global PA19 closure, count gain, runtime qualification or novelty claim. Parent independent checking and both-family review still required. Next justified written slice: one of families 1/2 (T2) or 6; no such slice is started here. Park after this bounded packet.
