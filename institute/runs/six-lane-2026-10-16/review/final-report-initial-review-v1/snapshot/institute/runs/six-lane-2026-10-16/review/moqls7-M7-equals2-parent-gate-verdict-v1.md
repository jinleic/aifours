# Exact M(7)=2: final parent K3 composition and gate verdict v1

Recorded at 2026-10-18T13:00:17-07:00.

## Decision and exact scope

**GATE MET for the frozen phys-2 M(7) target. CORRECTNESS-ACCEPTED, computer-assisted: M(7)=2.** Every set of three mutually orthogonal quantum Latin squares of order7 is classical. A non-classical orthogonal pair exists. The statement allows **arbitrary complex unit vectors**, with product-vector orthogonality and the source's set-isotopy convention: independent unitaries per square and simultaneous row/column permutations.

This is not nonexistence of classical triples (they exist), not a bound on the ray count of one QLS, not a result about entangled Latin arrangements, and not M(n)for alln. No Lean proof, human peer review or novelty claim.

This is the final **decision8** composition disposition under [AMENDMENT-4 parent decisions](moqls7-amendment4-parent-disposition-v1.md). The formerly pending Links3,7,10,11,14 are accepted at the reconciled scopes below. The A+B standard is fully retained.

## Text and final reviews

- [K3-COMPOSITION r5](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-B-cube-parent-replay-v1/composition/K3-COMPOSITION.r5.md), SHA256 `7ed11c72a563cfea617e8d2ee3578e1db26ec02d5094fdd610398fbb80b5eecf`, read with this verdict's overlay. Its frozen pending/conditional statuses are superseded only by this final decision.
- [Exact r4→r5 diff](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-B-cube-parent-replay-v1/composition/K3-COMPOSITION.r4-to-r5.diff), SHA256 `61b7c88cf235ca4403ddf6aedf0c585a85118088b06866bf7e00bfa425dd06d8`.
- [Codex final review](moqls7-k3-composition-r5-final-codex-v1.note.md), SHA256 `f65cbd2f9eca8fef815f30b47d2e8449f86ebe630b979eb640ba9c1984db5fd6`: **COMPLETE-COMPOSITION ACCEPT**,0FATAL/MAJOR/newMINOR.
- [Claude final review](moqls7-k3-composition-r5-final-claude-v1.note.md), SHA256 `cdf97163ebe4fdd46e3c7d02928b3294e054e1447906cdd53330ac7c5a732291`: **COMPLETE-COMPOSITION ACCEPT-WITH-FIXES**,0FATAL/MAJOR,7documentation/importMINORs, all disposed below.

Both final reviews explicitly conclude that accepted components plus the reviewed bridge establish K3 andM(7)=2. Their reads were static: they did not run solvers. Actual finite outcomes are the parent's recorded replays, not invented review execution.

## Six exact K3 formula facts

All are parent-accepted UNSAT, with solver self-exit20 and checker self-exit0 and exact singletonstatus lines after CR removal only.

| Formula | SHA256 | Variables / clauses | Authority |
|---|---|---:|---|
| A_C321 | `d598507d84a8d7595b30a100d528dca08bc0ce1aa71978583f09aac188298388` | 96,978 /627,486 | [G1](moqls7-k3-G1-parent-verdict-v1.md), [A-side replay](moqls7-k3-A-cubes-parent-verdict-v1.md) |
| B_C321 | `8b7b8124dbaf7088626ae853f4e10fe9590459dde1676377326ceecfb6d812c6` | 461,370 /1,629,732 | [G1](moqls7-k3-G1-parent-verdict-v1.md), B_C321-a3 |
| A_C411 | `2b92f5b15cd641e4a07ecec241b7957deac972aa3c7333056ff3e739e46addf2` | 96,978 /627,556 | [G2](moqls7-k3-G2-parent-verdict-v1.md), [A-side replay](moqls7-k3-A-cubes-parent-verdict-v1.md) |
| B_C411 | `01acf46491feef2fc26060266af8c2dead0cec9832c9e9ecbed83f886ecb8bf8` | 461,370 /1,629,802 | [G2](moqls7-k3-G2-parent-verdict-v1.md), B_C411-p3 |
| A lex C311+cuts | `18583aabb486b2d7fdf2159ed2172c9dfc9b29bbd2e50c63a5d7d94d44ba2e5e` | 107,513 /897,308 | [A-cut verdict](moqls7-k3-A-C311cuts-parent-verdict-v1.md) |
| B C311+cuts | `ae3b8309601d115e2258782ae3cb793f4dc4b5950064b9536b1eca61521f783a` | 461,370 /1,867,942 | [B-cut verdict](moqls7-k3-B-C311cuts-parent-verdict-v1.md), [raw audit](moqls7-B-C311cuts-parent-audit-v1.json) |

C321/C411 gates contain neither cuts nor lex blocks. The C311 facts use the exact238,140-clause derived cut block `05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd`. A additionally uses the **seven C311-specific generators**, not another cube's group or all22generators.

The final B-cut pipeline ended12:05:22PDT. Its raw audit verifies all43assembled conditions and39grouped parent predicates, including complete measured38353647-byte feeds, input/source/native pins and clean owned-process settlement. Its checker consumed842,063,946proof bytes. A-cut consumed705,539,296bytes. No interrupted or disarmed attempt contributes.

## Parent derivation of the complete bridge

The parent read the full definitions/basis-free replacement argument, r5's cover/cut/lex/composition interfaces, the accepted H3/G1/G2/A+Bcut verdicts, and both final audits. The key implications were independently re-derived:

1. **C0 and minimality.** Separate per-square unitaries straighten each individually classical member in its existing cells, preserving tensor-product orthogonality. Thus a set is classical iff every member is classical. If aK3square were light in some ONB, selectively rotating all weight2entries on a chosen2-coordinate support preserves every pre-existing zero inner product: an orthogonal outside-support entry must have disjoint support, because a single-coordinate overlap cannot cancel. At least one weight2entry disappears and none is created. Iteration classicalizes that square and preserves both partners simultaneously. The new square is distinct from both partners; otherwise a QLS would be orthogonal to itself, requiring49orthogonal vectors inC7. This produces a forbiddenK2triple. Therefore everyK3member is heavy in every ONB, givingG4on all14ownlines, not only one chosen frame.
2. **Normalization and three cubes.** Choose a heavy own line and off-line point, then apply `--sym` and the separate residual column/square normalization. At that point all3supportsets are nonempty and pairwise disjoint in the6coordinates outside the meetpoint. The first contains3fixedcoordinates. The only types are(3,1,1),(3,2,1),(4,1,1), giving the18assignments covered by the3signed cubes. No new forcedweight3lemma from the older four-square problem is substituted.
3. **Encoder instantiation.** Both bases express the stated necessary Gram conditions, with collinear predicates false. A'sproduct auxiliaries andB'sproduct/threshold auxiliaries receive their actual conjunction/prefix-threshold values. G2/G3/G4lists have5or6candidates, making malformed empty/Nonebranches unreachable. Own-line heaviness gives the guards; singleton supports giveG6. The runtime B-map oracle and the reviewed allocation order bind the same2,646gvariables. The [H3 verdict](moqls7-k3-h3-parent-verdict-v1.md) is now applied with its hypotheses supplied by the normalizedK3configuration.
4. **Uncut gates imply the cuts, without circularity.** In any own frame, eachsquare'sneighbour count is positive and the3sets are disjoint in6coordinates. A count≥4 forces(4,1,1); counts≥3and≥2force(3,2,1). Transposition and row/column/square permutations carry those local types to the exact uncut gateinputs, preserving individual raysets and heaviness on the image. G1/G2therefore exclude them. The uniform family has14·42·3·binom(6,4)=26,460at-most3clauses and14·42·6·binom(6,3)·binom(3,2)=211,680mixedclauses. Their sum is238,140. These are derivedK3consequences underK1/K2/G1/G2, not unconditional QLSaxioms.
5. **Existential lex representative.** The C311-specific group preserves the base/cube/cut conditions; every orbitmember is again aK3configuration. A finite orbit has a lexminimum satisfying all7generator comparisons. For arbitrary comparatorlength, prefixvariables set to “all prior positions agree” satisfy the emitted clauses when lexorder holds; conversely the first1→0difference contradicts its forcedtrueprefix. No involution assumption or bounded-length truth-table premise is used. Auxiliaries may be reconstructed. Thus **some** C311representative satisfies A's strengthened input; the original normalized configuration satisfies B'sinput.
6. **Closure.** C321contradictsG1, C411contradictsG2, andC311contradicts the two accepted strengthenedUNSATfacts. This provesK3. With acceptedK1/K2 everytriple isclassical. Any non-classicalt-set,t≥3, contains a non-classicalmember byC0; choosing it and2distinctpartners gives a non-classicaltriple, impossible. HenceM7≤2.

## Lower bound: actual exact check

The prior Fourier construction usesf=(0,6,5,1,3,4,2), Psi_ij(x)=ω^(i·f(x)+j·x)/sqrt7 andPhi_ij=|4i+j>. The parent wrote [an independent exact checker](check_m7_published_pair_parent_v1.py), SHA256 `3737822396d07fa7297d597ff1fa230f533cf2929ee7467d07844dbb03d0e7b2`, using the minimal polynomial1+…+X6 ofω7; no floating-pointzero tests. [Actual result](moqls7-published-pair-parent-check-v1.json), SHA256 `1980a137dac1f9076b9ff4d50f2f70e0a0a7ccf5a77081c530dcf2c062deb849`: all1,176distinctcellpairs checked, bothQLSvalid, mutuallyorthogonal,49distinctPsi rays (therefore non-classical). ReplacingPhi4byPhi2fails orthogonality; an affinef gives only7rays and is correctlyclassical. ThusM7≥2independently corroborates the known lowerbound. This construction is prior work, not a new contribution of thisrun.

## Final MINOR finding dispositions

1. **Anticipatory statuses** (Claude m1): Links3,7,10,11,14are now accepted by this verdict. G1's earlier “accepted” wording is read through this final reconciliation, not as earlier authority.
2. **Implementation premises** (m2): the [hash-bound implementation index](moqls7-final-implementation-premises-v1.json) explicitly lists the original cutfamily source, regeneration/appender drivers, cutcontrols, encoders and lexmetadata. Fidelity of the blocktoits mathematicallyderivedfamily and serialization/appending are reviewed trustedimplementationpremises. Current parent-source lineage includes [v11staticGO](m7-launch-v11-codex-v1.note.md), SHA256 `d7ed4c3a078ba765e735b262a29488bcc60ec1256e82243b926454c8abe8c61a`, which checks B's exactcomposition, [v12staticGO](m7-launch-v12-codex-v1.note.md), SHA256 `e1e6f94c35019c5e7715e9c8aa7c5f3802b0663003aff265dd1fefcc0e4e6be7`, which checks A'sexactcomposition, and [v14parent sourceGO](m7-v14-known-zombie-parent-source-go-v1.json), SHA256 `4e675c166726bc9ffd92d22108ed912352c70f07df333cfae3bea46fa29e623d`. These are scoped source/changeset reviews, not a new claim that every original historical produceractivation event is independently authenticated in this finalsnapshot.
3. **Generator identity** (m3): the header alone cannotidentifyH311. It is bound by theactual C311generator source, lexmetadata7bef0b78…190d and signed-unit preservation evidence, not merely10,535auxiliaries/31,612clauses.
4. **Identical quiet logs** (m4): a16-byte` s UNSATISFIABLE` log(without the illustrative leading space) hashes identically across manyruns because its exact bytes are`s UNSATISFIABLE\n`. Runidentity comes from boundreceipts/driverinputs, not the common loghash or equal proofbytecounts.
5. **PRODUCER label** (m5): r5Link13's olderparagraph means “producer result,evidenceonly”; the parentB-cutverdict and thisfinalcompositionstatus governacceptance.
6. **Old Aattempts** (m6): r8/r9producerattempts remain non-contributing here. Link12rests on A_C311cuts-p2; no missingoldproducerPASS is silentlyinferred.
7. **C0/control limits** (m7): subsetclosureuses the source's per-square-unitary convention and distinctpartners. ClassicalAG(2,7) cutchecks are near-vacuous because localweightsare1; semantic evidence is the structuralcutproof,C1localcoverage and the AMENDMENTreviews, not a nonexistent genuineK3positive.

All12priorcompositionMINORs (Codex3,Claude9) remain closed by r5'sfixmaps. Empty-log templates are false and remain frozen; actualB-cutrawlogs16/478bytes,A-cutraw16/475bytes. A's466-bytefield is CR-normalized, notraw. The firstB-cutparentaudit's object/scalarschemafailure is retained; correctinggate.rss_cap.value didnotrerunscience.

## Inherited evidence limits — not upgraded

**K2provenance caveat, verbatim:** “35 classes (0-33, 35) have no script-hash-observed parent replay for either encoder; their acceptance rests on receipt content, hash-bound native logs (exact status, matching parse dims), regenerated CNF = producer r4 CNF, and A+B producer+parent verification; same-dims different-formula substitution excluded only by the edit-log account.” No backfilledhash or concealmentrerun is claimed.

The26matchedcontrols followedK2production; otherhash-boundcontrols were reused. No genuineK3positivecontrolis possible withoutrefutingthetheorem, so the explicitcomponent-levelruling remains. No parent-authoredthirdencoderexists. Classificationinputs enterthroughacceptedK1/K2 and Egan–Wanless; those literaturepremises remain imports.

**M7proofstreams are notretained or digested.** Parent replaymeans freshly re-solving the exactCNF and checking that stream, notidenticalproducerproofbytes. Rechecking thesameoldstream isunavailable. The existingM7exact-CNFprotocol permits this; n8'sstricterproof-digestprotocol isnotappliedretroactively. CaDiCaL/kissat areuntrustedproducers; drat-trim, CPython,compiler,OS,hardware and reviewedserialization aretrusted. NoLean,Comparator,independentformal kernelorhumanreview.

## Priority and significance

The [fresh exact-M7 primary comparison](../screening/phys-2-moqls7-M7-post-candidate-priority-v2.md), SHA256 `6138411f55adbe79ddc02aa0bdf4fbbb5f270f68e8562835013812c6d5b673a6`, found no earlierM7=2ororder7tripleconstruction/exclusion in bounded scope. It includescurrentprimarypapers,all36DataCitequantumLatinrecords,arXiv/citers/authors andexplicitaccessholes. No novelty orpriority proof. Same-dayfinalannouncementrefresh remains scheduled.

Scientificdelta: the inspectedBall–Simoenspreprint had2≤M7≤4; thisrunfirstprovedupper3andnowupper2. Thisexactdetermination is a substantive specialist result inquantumcombinatorics, refiningthesameorder7program—not an unrelatedphysicalcapacityclaim or a claimaboutallorders. Publication/contactremainsunauthorized.
