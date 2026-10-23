**GO-WITH-FIXES for ONE bounded split-path pilot of the four frozen intervals, conditional on closing MAJOR 1 below.** I found no demonstrated execution regression in the supplied delta. Full v6_3-to-v6_4 contract equality remains an evidence gap.

All **17 supplied SHA256 hashes and byte counts match**. Review used static snapshot reads, comparisons, and hashes; no source execution, writes, network, or delegation.

The proposed pilot is bound to:

- Contract SHA256: `41983dedd232232804b955df350de750c9e3feda7b45500293212932808edd5d`
- Plan SHA256: `73738d7689746908e7d8d08a0fe27ab9e272664916c0930e03fa09f0c14df6c2`

**Findings**

1. **MAJOR 1 — complete artifact equality cannot be independently verified from this snapshot.** The freezer hashes the named v6_3 contract, compares every field in `SAME`, and publishes only afterward (**SOURCE04:29–31,111–118**). That is a sound source-level invariant. However, the old contract is supplied only as a path/hash reference (**SOURCE00:62–65**); the new contract’s `identical_to_contract` repeats that declaration (**SOURCE12:102377–102394**). Neither supplies the old item bytes for comparison. Furthermore, runtime `verify()` does not repeat the comparison against the old contract (**SOURCE03:192–236**). Consequently, I can verify the preservation mechanism and current contract structure, but cannot independently certify that every old item, exclusion, and associated field is unchanged. **Repair:** include the exact v6_3 contract matching `835ca4…5a1930`, then provide a static comparison of all `SAME` fields. Prefer supplying both complete contracts and their exact diff. This requires an evidence-pack repair; no production-code defect is demonstrated.

2. **MINOR 1 — “only the loop iterable changes” overstates the delta.** The pack says this at **SOURCE00:20**. Executable additions also include plan validation, mandatory arguments, namespace generation, dual-lock handling, and summary provenance (**SOURCE01:20–151**). The freezer gains equality enforcement; the checker gains plan construction and additional controls (**SOURCE01:185–198,364–531**). These changes support the requested feature, but the literal claim is false. **Repair:** state: “The per-item execution body is unchanged; surrounding changes implement selection, isolation, validation, and provenance.”

3. **MINOR 2 — zero native children is declared rather than independently counted.** The receipt reports zero (**SOURCE09:555–558**), but its producer writes the literal `native_children_started: 0` (**SOURCE05:570**). This is inherited from the base checker (**SOURCE16:468**). Visible control paths support the declaration, as discussed below, but the field is not a process-spawn measurement. **Repair:** label it explicitly as a structural declaration, or instrument the spawn boundary and fail controls on any real child launch.

**BLOCKER:** none identified in the supplied delta. The MAJOR finding prevents unconditional certification of requirement (a).

**(a) Contract preservation**

The freezer’s equality field set covers `items`, `order`, exclusions, skeletons, binary authority, policy clocks, resource policy, checker limit, case and interval counts, retry prohibition, and singleton policy (**SOURCE04:30–31**). Equality of the complete ordered `items` array would establish preservation of every item field and position, including historical bindings and split-list denominators.

The current artifact contains **5,580 unique item IDs: 5,393 direct items and 187 intervals across 31 split cases**, yielding **5,424 contract cases**, with **82 exclusions**. Static scans confirm those counts. The extracted item-ID sequence and the separate `order` sequence have identical hashes; no duplicate item-ID lines were found. Declared counts appear at **SOURCE12:102039–102042**.

The resource reservation still charges all **5,580** items, with a whole-plan bound of **4,825,677,824 bytes**, a 600-second census TTL, and the existing resource-policy limits (**SOURCE12:86–96**). Selection does not reduce that reservation: runtime uses the full contract’s bound (**SOURCE03:341–345**).

The clocks remain **17:20 admission cutoff, 17:57 native end, and 120 seconds cleanup allowance** (**SOURCE03:43; SOURCE12:81–84**). Skeleton, supervisor, and binary bindings remain explicit (**SOURCE12:29–79**). Thus the implementation preserves the requested fields; independent old-versus-new artifact verification awaits MAJOR 1.

**(b) Selector validation and attempted scope**

The frozen plan selects exactly these entries, in contract order (**SOURCE08:25–44**):

| Contract position, zero-based | Item |
|---:|---|
| 617 | `ms01_b00957:00300-00309` |
| 4801 | `ms01_b00957:00200-00299` |
| 5151 | `ms01_b00957:00000-00099` |
| 5161 | `ms01_b00957:00100-00199` |

Independent enumeration of the contract’s item-ID lines confirms these positions. The four item bodies share the same frozen list hash and denominator **310** (**SOURCE12:10590–10612,81926–81948,88140–88162,88334–88356**).

`plan_items()` checks schema, contract binding, nonempty selection, exact entry fields, ID syntax, uniqueness, exclusions, membership, integer position, canonical item hash, prior attempts, order, and complete selected split cases (**SOURCE03:158–182**). It returns references to contract items; it does not reconstruct or renumber them (**SOURCE03:173–177**).

The **plan-file hash check belongs to `run_locked()`**, immediately before parsing and validating the plan (**SOURCE03:330–331**). Missing mandatory arguments fail during argument parsing, before chunk creation or claims (**SOURCE03:297–301**). Claims occur only inside `for x in selected` (**SOURCE03:348–357**).

These checks are assertion-based, consistent with the reviewed base. This clearance assumes an assertions-enabled invocation; optimized Python execution is outside it.

**(c) Namespaces, prior attempts, and singleton isolation**

Default task generation produces `_h6_4` primary records, pins, and commits, plus `m2h6_4_` claims (**SOURCE03:136–145**). The base uses `_h6_3` and `m2h6_3_` (**SOURCE15:127–136**). Chunk directories also change to `m2h6_4-chunks` (**SOURCE03:301**).

The only explicit `h6_3` task lookup in the selector checks for existing record, pin, commit, or claim and refuses the selection (**SOURCE03:175–176**). That lookup performs no publication. S15 reports the expected refusal for the already-attempted `ms01_b00045` (**SOURCE09:469–471**).

The runner acquires the **v6_3 lock first, then v6_4**, both exclusively and nonblocking, before entering `run_locked()` (**SOURCE03:303–316**). This excludes another runner of either version while the pipeline executes. T7 and S20 exercise both lock-refusal cases (**SOURCE05:401–409,500–507**).

**(d) Execution path and exhaustive delta assessment**

Direct static comparisons against SOURCE15 and SOURCE16 agree with the supplied runner/checker deltas. I examined every exact-diff hunk and the normalized delta.

Beyond the surrounding additions listed in MINOR 1, the runner’s per-item execution body remains unchanged. It retains claim handling, immutable-source checks, formula regeneration and historical-CNF comparison, and the same `OWNER.execute()` call (**SOURCE03:357–372**). Pre-pin and pre-worker refusals retain their existing retirement behavior (**SOURCE03:373–388**).

Publication still blocks SIGTERM/SIGINT, converts pre-publication cancellation to UNKNOWN plus persistent veto, publishes the commit before the primary record, and restores the prior signal mask (**SOURCE03:389–402**). SAT, integrity failure, HALT, and worker refusal still stop progression (**SOURCE03:409–410**).

Initialization retains metadata Capacity, union/record veto scans, binary observations, census reservation, cutoff, cancellation, and deadline checks (**SOURCE03:321–351**). The full five-admission predicate remains intact (**SOURCE03:70–86**).

The reader still binds contract, pin, commit, record hash, runner, recipe, source/binary authority, supervisor, interval, list hash, denominator, and historical receipt; it rejects cancelled UNSAT and delegates qualification to the existing exact evidence reader (**SOURCE03:247–280**).

The freezer adds equality checks without changing item derivation (**SOURCE01:155–204**). Checker changes adapt flows to mandatory plans and add S/I controls; existing control families are retained (**SOURCE01:310–532**). No production bypass was found in these additions.

**(e) Inventory and completeness**

Inventory traverses the **full contract**, records one qualification Boolean per item, groups by case, and counts a case only when **every** Boolean is true (**SOURCE07:28–37**). A MISSING interval therefore keeps the split case open.

Four qualified selected intervals cover **one case**, leaving **5,423 contract cases open** in the isolated v6_4 inventory. I1 and I2 exercise incomplete and complete split-case accounting (**SOURCE05:515–542; SOURCE09:522–535**).

Final readiness additionally requires formula verification, complete coverage, no issues, and no persistent vetoes (**SOURCE07:42**). Historical receipts and v6_3 pilot records do not become v6_4 qualifications. The output explicitly limits its scope to M2H (**SOURCE07:43**). Neither this subset nor the 5,580-match binding census establishes M2 or PA19 completeness (**SOURCE11:14–16; SOURCE00:528**).

**(f) Controls and pilot boundary**

The receipt contains **68 named passing controls**: G3, C2, O4, R20, T13, S21, I2, and V3. S0–S15 contain acceptance or specific rejection results; S16 lists exactly four owner calls, claims, and records; S17–S19 report refusal with no owner calls (**SOURCE09:381–515**).

These results correspond to executable checks, rather than merely family labels (**SOURCE05:446–507**). S16 uses `StubOwner`; inventory controls inject qualification states. Real-owner controls fail before native work or use fake supervision; C1 checks budget refusal and an empty child list (**SOURCE05:112–194,291–313**). This supports zero native execution structurally, subject to MINOR 2’s measurement limitation.

After MAJOR 1 is closed, permit only this frozen plan, at most four attempts, one pipeline, the existing clocks and gates, and no automatic retry. Require the actual split **publisher → exact reader → formula-verifying inventory** audit before expansion. The prior parent audit explicitly supplies direct-path evidence only (**SOURCE14:3–4**).