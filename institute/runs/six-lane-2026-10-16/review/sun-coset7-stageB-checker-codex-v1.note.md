**Overall: SOUND for the conditional implication `COMPLETE_VALID ⇒ class excluded under SOURCE08’s accepted rules`.** I found no FATAL or MAJOR code-soundness defect. There are MINOR format, metadata, and provenance issues below.

All eleven snapshot hashes and byte lengths match the supplied inventory. This was a static audit; SOURCE09’s execution claims remain independently unverified because its manifests, producer certificates, and result files are absent.

| Component | Verdict |
|---|---|
| Universe coverage | **SOUND**, with deliberate K52 overcoverage |
| Symmetry | **SOUND** |
| Walk and closures | **SOUND** |
| Leaves and RPLP | **SOUND** for exclusion; minor format laxity |
| Parsing and integrity | **SOUND-WITH-FIXES**, concerning metadata handling and provenance |
| Overall conditional implication | **SOUND** |

The universe enumeration covers the requested classes. `CAPPED` contains the complete CAP cube, and `enum_labelled` recursively tries every profile at every labelled position, applying every preceding pair constraint (`SOURCE00:245, 305`). Neither enumeration is restricted to producer-listed profiles. Equality between the two enumerations alone would not exclude a shared omission: they share the cube, gcd function, and enumeration routine. Direct inspection supplies the additional assurance here.

KII matches README’s class: X is 2-only/5-divisible, Y is 3-only/5-divisible, and the remaining five vertices are C with zero 5-valuation (`SOURCE00:271`). The CERT-FORMAT enumeration derives that last restriction through its pair constraints: a 5-divisible C would share both 2 and 5 with X. The X–Y gcd forces minimum 5-valuation one.

K52 is **larger than README’s K5.2***: it permits no C vertex in E, including the already eliminated D2′ case (`SOURCE00:267, 299`; `SOURCE01:94`). This is disclosed in SOURCE09:425 and cannot omit a target configuration. Because every vertex is even, the permitted pair gcds also automatically prohibit two 5-divisible vertices. Alpha domains are exactly `1,…,g−1`, both during walking and when validating stored representatives (`SOURCE00:781, 911`).

Symmetry is sound. Sorting within the contiguous role runs gives representatives for \(S_2\times S_5\) in K52 and \(S_5\) in KII. Every enumerated labelled tuple is explicitly assigned to such a representative, with orbit–stabilizer accounting checked (`SOURCE00:468`). The stabilizer independently generates the Cartesian product of all permutations within equal **role-and-profile** groups (`SOURCE00:342`). Profile markers therefore cannot be exchanged improperly.

Leaf canonicalization minimizes over that complete stabilizer. A leaf line’s canonical string is recomputed from its validated representative; lookup includes both the profile tuple and canonical string (`SOURCE00:784, 949`). Consequently, a line for a different orbit cannot cover a reached leaf. A witness on another representative of the same orbit is sufficient because the accepted predicates are invariant under that relabelling.

The tree walk satisfies F-3. Every profile representative enters recursion; every assigned edge tries all `g−1` values. A node either closes through a locally verified predicate, reaches a checked leaf, or recursively expands the next edge (`SOURCE00:908`). Completed triangles are exactly `{h,i,j}` with `h<i` when edge `(i,j)` is assigned. Descendant assignments are cleared on return. The degree shortcuts are correct for this edge order: the endpoint degrees are `j` and `i+1`.

T uses the opposite vertex’s ℓ-valuations, exact integer divisibility, and downward-rounded upper bounds; only `tau_min > tau_max` kills (`SOURCE00:198, 214`). Its memo key injectively encodes three profile IDs and three alpha values; the base-eight alpha fields cannot collide.

K-partial checks completed linked pairs and enumerates every compatible additional-neighbour subset, including all required pairwise links (`SOURCE00:865`). The scale 60 is exact for every permitted gcd, and the kill comparison is correctly `sum≥1`. Checking only subsets implicated by newly completed triangles does not create an unjustified closure.

VFC signatures come from the checker’s own assigned edges and precomputed valuations, rather than producer-provided node claims (`SOURCE00:923`). A signature enters `killed` only after **every** q-vector verifies. The allowed-mask recurrence enforces the hereditary condition: the current subset needs a qualifying pair, and every immediate smaller subset must already be allowed (`SOURCE00:175, 601`). Exact nonnegative dual weights, all allowed-set inequalities, and objective `≥1` are checked independently.

RPLP also checks every q. Its product is generated locally, with exact certificate-count equality before zipping (`SOURCE00:635`). Both ordered forced-containment tests are recomputed, with the correct complement implication. Grid bounds use exact `Fraction` arithmetic, ceiling for lower bounds, floor for upper bounds, and the strict K2 adjustment—including both directions when measures agree (`SOURCE00:638, 653`).

For each nonempty forced-compatible A, the checker maximizes the scaled a-sum over **every allowed S⊆A**. Initializing the maximum to zero explicitly includes empty S (`SOURCE00:722`). This is equivalent to checking every column. The pair contribution is correctly `l−u`; u and l must be nonnegative; the objective uses `−u*yhi+l*ylo` and rejects values below one (`SOURCE00:695, 731`). R certificates require the independently computed key and verified VFC dual. Producer coefficients supply witnesses, never coverage.

Dropping a required leaf cannot pass: each first reached orbit requires an `OK` line, duplicates produce persistent rejection, and missing or unverified orbits also fail survivor reconciliation (`SOURCE00:789, 957, 1063`). Producer counts are informational. The recursive traversal establishes coverage; its count identity provides an additional consistency check.

I did construct an accepted **padding case**, which exposes format laxity without defeating exclusion:

- Use K52 profile `((2,0,0),(2,0,0),(1,1,0)×4,(2,1,0))`.
- Set every alpha to one except `α56=2`; its canonical code is twenty ones followed by two.
- At vertex 5, repeat a P certificate for all 500 q-vectors, with only `u46=l46=6` nonzero.

For neighbour pair `{4,6}`, `lo=1/3`, `hi=1/6`, so the objective is exactly one; every column coefficient is zero. Yet triangle `{4,5,6}` fails T (`tau_min=2`, `tau_max=1`), so this orbit is never a reached leaf. Appending this line and updating the manifest would preserve acceptance.

**MINOR — SOURCE00:1040, 1050:** extra lines and whether stored representatives were reached are reported, not enforced. For exact file correspondence, reject unequal reached/listed key sets. Alternatively, document explicitly that verified extra lines are permitted under F-2’s sufficient-coverage interpretation. This padding cannot replace a missing required orbit.

Parsing otherwise fails closed. Certificate JSON rejects duplicate keys, float literals, and nonfinite constants recursively (`SOURCE00:99, 116`). Rational strings are parsed exactly, integer fields exclude booleans, and gzip contents pass through the same strict parsers. JSONL rejects internal empty lines and missing final newlines; the zero-leaf newline special case still undergoes the full walk. Hashes cover the compressed input bytes actually retained and subsequently parsed (`SOURCE00:437`). Malformed gzip, decoding errors, and unexpected exceptions cannot select `COMPLETE_VALID`; definitive rejections remain sticky (`SOURCE00:1087, 1110`).

Two further MINOR fixes apply:

- **SOURCE00:1028, 1072:** failed comparison-only `run.json` parsing sets `run=None`, but subsequent unconditional `.get` calls cause `INCOMPLETE`. Normalize malformed metadata and nested statistics to dictionaries. This is a false-negative/availability bug.
- **SOURCE00:425:** the manifest digest is recorded, not checked against a trusted expected digest. Add an expected-manifest hash argument or an explicit caller-side pin check to bind acceptance to SOURCE09’s named artifacts. Self-consistent replacement manifests still face the complete proof checks.

The eleven controls meaningfully exercise missing leaves, malformed profile/orbit matching, missing q certificates, coefficient signs, packing constraints, and objective thresholds (`SOURCE10:7`). I1 additionally probes lost VFC pruning. Their reported outcomes are receipt assertions, not independently inspected results.

Important untested corruptions include same-count wrong-orbit substitution, duplicate keys/leaves, floats/nonfinite values, truncated gzip, hash mismatch, and forged signature/key binding. C6 does not isolate empty-S handling: SOURCE09:272 reports failure at `A=1`. C10 can fail on a singleton and therefore does not establish hereditary multi-subset checking. Add witnesses whose **only** violation is respectively an empty-S column or a larger allowed subset.

The remaining uncertainty is evidentiary: genuine execution, manifest anchoring, certificate bytes, and control-result authenticity. The static code implication survives this audit; the actual recorded class exclusions await those artifact checks.