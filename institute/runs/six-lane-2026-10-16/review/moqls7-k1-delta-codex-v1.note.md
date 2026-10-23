DISPOSITION: ACCEPT-WITH-FIXES

**FATAL:** None found.

**MAJOR:** No new mathematical defect found. The original control discrepancy is substantially repaired; its remaining provenance wording is MINOR.

**MINOR:**

1. **“Separately built” exceeds the receipt.** `lane/review/K1-THEOREM.r3.md:94` asserts a build relationship. `parent/route2/receipt-route2.json:58–60` identifies a parent checker with a different binary hash; `parent/RESULT.json:61` confirms the binary difference and source identity. Neither supplies a build record. **Correction:** write “a separate parent checker with binary SHA-256 a46c0c71…8e37.” Retaining “separately built” requires a source/compiler/command/output-hash binding.

2. **Attribute original verification results to their saved summaries.** `lane/review/K1-THEOREM.r3.md:89` describes original checker stdout directly. The drivers retain a parsed, synthesized result—`lane/code/k1_certify.py:69–82` and `lane/code/k1_encB.py:112–116`—rather than original raw stdout. This is materially better supported than the withdrawn control claims, but the distinction should remain explicit. **Correction:** “The saved producer summaries report verification of all fourteen final proofs; parent route 2 independently records `s VERIFIED` for all fourteen.”

The mathematical conclusions below are conditional on K1’s certificate obligations. Receipt consistency and reported PASS results do not replace those obligations.

**Finding map**

All references use LF-only numbering. “RESOLVED” describes the correction, without retroactively repairing historical receipts.

| Original finding | Classification | Resolving passage / remaining issue |
|---|---|---|
| Codex MAJOR 1 | **PARTIAL — minor residue** | `lane/review/K1-THEOREM.r3.md:90–97` withdraws producer controls, corrects the proof-file description, and cites the matching parent receipt. The two wording fixes above remain. |
| Codex MAJOR 2 | **RESOLVED** | `lane/review/K1-THEOREM.r3.md:136–137` withdraws the exploration/count/minimality claims. Neither LEMMAS nor the corollary restores them. |
| Codex MINOR 1 | **RESOLVED** | Driver digest corrected at `lane/review/K1-THEOREM.r3.md:82`; baseline suffix corrected at `lane/README.md:7`. The baseline target itself is outside this snapshot. |
| Codex MINOR 2 | **RESOLVED** | `lane/review/K1-THEOREM.r3.md:66–67` distinguishes sets/lists and invokes Theorem 3.1. |
| Codex MINOR 3 | **RESOLVED** | `lane/review/K1-THEOREM.r3.md:51–53` distinguishes minimum key from the group-order quotient. |
| Codex MINOR 4 | **RESOLVED** | `lane/review/K1-THEOREM.r3.md:83–86` withdraws original run-specific versions; `:96–97` attributes versions to the parent replay. |
| Codex MINOR 5 | **RESOLVED** | Late documentation is explicitly identified at `lane/review/LEMMAS.md:3–6`; arguments appear at `:8–67`. Histories are expressly non-evidence at `lane/review/K1-THEOREM.r3.md:77–78` and `:158–160`. |
| Claude MINOR 1 | **RESOLVED** | Correct driver digest at `lane/review/K1-THEOREM.r3.md:82`; parent supplementation at `:73–77`. Parent replay pins the driver at `parent/route2/receipt-route2.json:739`. This does not add a hash to the original A summary. |
| Claude MINOR 2 | **RESOLVED** | `lane/README.md:7`. |
| Claude MINOR 3 | **RESOLVED** | `lane/review/K1-THEOREM.r3.md:85–86`. |
| Claude MINOR 4 | **RESOLVED** | `lane/review/K1-THEOREM.r3.md:90–96`: original outcome assertions withdrawn; explicit empty-clause step distinguished from an empty file. |
| Claude MINOR 5 | **RESOLVED** | `lane/review/K1-THEOREM.r3.md:136–137`. |
| Claude MINOR 6 | **RESOLVED** | `lane/review/LEMMAS.md:3–6` and `:38–52`: the referenced file now exists, with its late origin disclosed. |
| Claude MINOR 7 | **RESOLVED** | `lane/review/K1-THEOREM.r3.md:66–67`. The frozen shorthand at `lane/code/net_canon.c:7` is justified through this explicit sets/lists bridge. |
| Claude MINOR 8 | **RESOLVED** | `lane/review/K1-THEOREM.r3.md:51–53` and `:68–71`: quotient and free-action argument supplied. |
| Claude MINOR 9 | **RESOLVED** | `lane/review/K1-THEOREM.r3.md:65–78` now includes distinct keys, the invariant/fibre argument, conditional coverage, and parent technical evidence. |
| Claude MINOR 10 | **RESOLVED** | `lane/review/K1-THEOREM.r3.md:8–14`; also `lane/review/LEMMAS.md:9–14`. |
| Claude MINOR 11 | **RESOLVED** | `lane/review/K1-THEOREM.r3.md:129–131`. |
| Claude MINOR 12 | **RESOLVED** | `lane/review/K1-THEOREM.r3.md:172–177`; preservation argument documented at `lane/review/LEMMAS.md:54–67`. |
| Claude MINOR 13 | **RESOLVED** | `lane/review/K1-THEOREM.r3.md:148–157` identifies the 84 additions, 210 admissible removals, and evaluator/encoder distinction. |

**MAJOR 1: receipt and control audit**

All **38 manifest-listed file digests match** under `shasum -a 256`.

In particular, the route-2 receipt hashes to:

`506b466d0fef11578a06370dd7f94190fe72357fd81e1ad6425c2588b1189701`

This equals both `lane/review/K1-THEOREM.r3.md:93` and `parent/RESULT.json:25`.

The following LF references in the middle column are to `parent/route2/receipt-route2.json`.

| Control | `drat_runs` / `controls` LF | Raw output agrees |
|---|---|---|
| SAT CNF + empty-clause proof | `232–241` / `306–309`: rejected, exit 1 | `parent/route2/dt/ctl_sat_emptyclause.out:5`: `s NOT VERIFIED` |
| Contradictory units + empty proof | `244–253` / `311–314`: accepted, exit 0 | `parent/route2/dt/ctl_unsat_empty.out:3–4`: complementary units, `s VERIFIED` |
| A5 final proof against unblocked base | `256–265` / `316–319`: rejected, exit 1 | `parent/route2/dt/ctl_A5_base.out:47` |
| A6 final proof against unblocked base | `268–277` / `321–324`: rejected, exit 1 | `parent/route2/dt/ctl_A6_base.out:48` |
| B6 final proof against unblocked base | `280–289` / `326–329`: rejected, exit 1 | `parent/route2/dt/ctl_B6_base.out:13` |
| A6 final proof with weight-4 block removed | `292–301` / `331–334`: rejected, exit 1 | `parent/route2/dt/ctl_A6_minus_w4.out:44` |

Thus all six descriptions agree with both receipt representations and the raw outputs.

The requested phrases have these dispositions:

- **“Truly empty proof”: supported.** The proof digest at `parent/route2/receipt-route2.json:253` is the empty-file digest; `controls-binding.md:14` explicitly records zero bytes. This is distinct from the producer’s two-byte `0\n` file at `controls-binding.md:10`.
- **“Contradictory-unit CNF”: supported.** Its digest matches `controls-binding.md:9`, and the raw checker reports complementary units.
- **“Separately built checker”: unsupported as written.** Separate binary identity is supported; build provenance is not.
- **“All fourteen proofs”: supported as a receipt claim.** Entries A0/B0 through A6/B6 at `parent/route2/receipt-route2.json:63–230` each record verification and exit zero.
- **“Solver versions and binary hashes”: supported for the parent replay.** Binary pins appear at `parent/route2/receipt-route2.json:737–745`; versions and hashes at `:855–857`. They do not establish original producer runtime versions.

No original producer control outcome or run-specific solver-version claim survives. The remaining producer-provenance qualifications are:

- `lane/review/K1-THEOREM.r3.md:89`: original verification is supported through saved summary fields, rather than retained raw stdout; apply MINOR 2.
- `lane/review/K1-THEOREM.r3.md:77–78`: interrupted-classifier history remains unreceipted, but is expressly excluded as evidence.
- `lane/review/K1-THEOREM.r3.md:158–159`: retirement/archive history remains unreceipted here, but asserts no old violation result and is expressly excluded as evidence.

The last two could simply be labelled “unverified history.” I found no other surviving assertion of a never-saved producer output.

**MAJOR 2: exploration claims**

The 315-relation count, 97-contradiction count, and seven-relation minimum-size assertion are removed as claims from all three requested texts. “MILP” survives only in the explicit disclaimer at `lane/review/K1-THEOREM.r3.md:137`.

The minimum in `lane/review/LEMMAS.md:70–75` concerns the number of non-classical members of a counterexample, not phase-cycle size. It is a valid, separate argument.

**Correctness of the revisions and LEMMAS**

The r1→r2 changes correct the driver digest, sets/lists citation and unsupported exploration claims. They leave several other r1 defects intact; r3 supplies those repairs.

- **Straightening, ray criterion and C0:** `lane/review/K1-THEOREM.r3.md:8–14` is sound against `lane/sources/2607.12933v2.layout.txt:90–116`. A row supplies seven orthogonal rays. Exactly seven total rays places every entry in that row’s basis up to phase. Separate square-wise unitaries straighten both classical members without moving cells, preserving tensor orthogonality. This proves C0.
- **C1 and net transport:** `lane/review/K1-THEOREM.r3.md:16–28` correctly factors the product inner product. Equal classical symbols require orthogonality on the symbol line; unequal symbols supply the zero factor automatically. Net isomorphism transports the ONB-assignment and ray count, even when its class permutation is not a permitted set isotopy.
- **Flags and \(|par|\):** `lane/review/K1-THEOREM.r3.md:68–71` is correct. There are \(24\cdot49\cdot720=846720\) flags. A flag stabilizer fixes all frame-row points and hence every line of two other classes; their intersections fix every point. Equal reduced images have fibres of size \(|par|\). `lane/code/net_canon.c:47–53` records precisely the free entries of the reduced image; `:70–74` separately produces its minimum and distinct-image quotient.
- **Sets/lists:** The repaired citation matches `lane/sources/1406.3681v2.layout.txt:355–361`, `:382–397`, `:721`, `:776`, `:804` and `:860`. At \(k=2\), \((k-1)!=1\). The displayed orbit sizes sum by hand to \(341880+360+240=342480\). Actual key and enumeration correctness remains a certificate obligation, supplemented—not proved mathematically—by the parent reports.
- **Parent-check description:** The five PASS claims at `lane/review/K1-THEOREM.r3.md:75–77` agree with `parent/RESULT.json:10–15` and the five route receipts. The separation from the final theorem verdict agrees with `parent/RESULT.json:86`.

The corrected word proof at `lane/review/K1-THEOREM.r3.md:129–131` checks. Numbering the table’s relations \(E_1,\ldots,E_7\), each reads \(\Delta_q-\Delta_p=\pi\):

\[
\begin{aligned}
E_1+E_3:\quad
\Delta_{28}(4,6)
&\equiv\Delta_{34}(4,5)+\Delta_{29}(5,6),\\
E_7-E_6:\quad
\Delta_{26}(4,6)
&\equiv\Delta_{29}(0,6)-\Delta_{34}(0,4).
\end{aligned}
\]

Relations \(E_2,E_5\) equate the left sides. Additivity of \(\Delta\) then gives
\(\Delta_{34}(0,5)\equiv\Delta_{29}(0,5)\), contradicting \(E_4\). Equivalently, the signed sum has zero left side and
\((1-1+1-1+1+1-1)\pi=\pi\).
The listed points’ labels, common classes and overlaps also check directly against `lane/evidence/nets7_classes.json:1`.

The §7 correction is accurate. A C1 off-frame support has five coordinates, so its \(42\cdot7=294\) mutations divide into 84 forbidden-coordinate additions and 210 removals. Removals cannot reduce an off-frame overlap of at least three to one or create unique coverage. The independent evaluator is identifiable at `lane/code/pattern_check.py:19–42`; these are not matched executions of the fixed 4-net CNF encoders.

The §8 case split at `lane/review/K1-THEOREM.r3.md:172–177` is now correct: retain the unique heavy member when \(|Q|=1\), otherwise retain a non-classical member supplied by C0. The first replacement leaves the second square unchanged and light; the second preserves orthogonality to the first replacement. The conclusion concerns the **resulting** triple.

All of LEMMAS survives the mathematical check:

- **C0/C1:** `lane/review/LEMMAS.md:8–24` gives the valid arguments above.
- **W:** `lane/review/LEMMAS.md:26–36` correctly derives pairwise disjoint supports inside six coordinates, hence total weight at most six, individual weight at most four, and two singleton partners when one weight is four.
- **Frame/F1–F4:** `lane/review/LEMMAS.md:38–52` is correct. Coincident frame intersections would make two distinct net lines share two points. For F4, put line vectors in rows of a unitary: a uniquely covered column exhausts its covering row’s norm.
- **Arbitrary-basis Lemma 10:** `lane/review/LEMMAS.md:54–67` correctly supplies the reasoning behind `lane/sources/2607.12933v2.layout.txt:178–192`. An orthogonal entry of weight at most two has identical or disjoint support relative to the selected full two-coordinate support. Thus every old zero inner product survives, which preserves tensor orthogonality with all partners simultaneously. Supports shrink pointwise and termination is finite. Changing the fixed basis globally on that square preserves its Gram inner products.
- **G4:** `lane/review/LEMMAS.md:69–78` is sound. K1 forces a minimal non-classical triple to have \(m\ge2\). Classicalizing any light non-classical member would leave \(m-1\ge1\), contradicting minimality. Consequently every K2 triple is minimal given K1; applying the same conclusion to every K3 triple requires K2 first. The text states that prerequisite correctly.

The late-documentation disclosure is adequate. References to Gram packages absent from this snapshot cannot be checked for their actual use of these arguments.

**Correctness of the corollary note**

For Corollary 1, the **forward** implication of Zhang–Cao Lemma 2.2 is the one required: resolutions imply classical companions. The statement is present at `sources/source_fetch.receipt.json:117`.

The construction can also be checked directly: put \(B_r(i,j)=|k\rangle\) on transversal \(T_k^{(r)}\). Transversal shape makes each \(B_r\) Latin; its ONBs give \(A\perp B_r\) by C1; unique intersections make \(B_0,B_1\) orthogonal. These companions are literally computational-basis squares, hence classical in Ball–Simoens’s sense. Product-vector orthogonality agrees with the supplied ZC definition (`sources/SOURCES.md:17–30`).

Thus an \(A\) with more than seven rays would give exactly K1. ZC’s phase identification/cardinality convention agrees with the note’s convention. “Classical” in the conclusion means Ball–Simoens classicality, as explicitly specified—not that an arbitrary \(A\) already uses the computational basis. The cardinality-seven equivalence at `lane/review/K1-COROLLARY.r1.md:7–10` is correct.

For Corollary 2, each line \(y-x=b\) or \(y+x=c\) has one cell in every row and column, and is an ONB by the PQLS definition. Each family partitions the cells. Between families,

\[
x=(c-b)/2,\qquad y=(b+c)/2
\]

gives exactly one intersection in \(\mathbb F_7\). Hence PQLS(7) implies 2-RQLS(7).

The harmonic bridge at `lane/review/K1-COROLLARY.r1.md:44–48` also checks:

- \(x=c,y=c,y-x=b,y+x=b\) have directions \(\{\infty,0,1,-1\}\).
- The shear \((u,v)=(x,y+x)\) has determinant one, sends \(m\mapsto m+1\), and fixes the vertical direction.
- After reordering classes, its labels are
  \[
  (u,v,v-u,v-2u)=(x,y+x,y,y-x),
  \]
  giving the required class-5 net.

Here are ten direct four-coordinate checks against `lane/evidence/nets7_classes.json:1`, spanning every \(x\)-value:

| Point \(7x+y\) | Class 5: \((x,y,y-x,y-2x)\) | Class 6: \((x,y,y-x,y-3x)\) |
|---:|---|---|
| 0 | (0,0,0,0) | (0,0,0,0) |
| 6 | (0,6,6,6) | (0,6,6,6) |
| 7 | (1,0,6,5) | (1,0,6,4) |
| 9 | (1,2,1,0) | (1,2,1,6) |
| 14 | (2,0,5,3) | (2,0,5,1) |
| 20 | (2,6,4,2) | (2,6,4,0) |
| 23 | (3,2,6,3) | (3,2,6,0) |
| 28 | (4,0,3,6) | (4,0,3,2) |
| 38 | (5,3,5,0) | (5,3,5,2) |
| 48 | (6,6,0,1) | (6,6,0,2) |

The derivation through Corollary 1 invokes the full K1 exclusion. The **direct harmonic derivation requires only class-5 rigidity**, its explicit identification, and invariant transport of ONBs/rays. It needs neither seven-class completeness, maximal-net exclusion, the equianharmonic phase contradiction, §8, nor K2/K3.

**Novelty**

The acknowledgement at `lane/review/K1-COROLLARY.r1.md:20–25` is appropriate. ZC Lemma 2.2 supplies the general resolution/classical-companion equivalence; the supplied Ball–Simoens Lemma 21 anchor supplies the order-six graph reformulation (`sources/source_fetch.receipt.json:189–198`). These support the stated precedents, without establishing a literature-wide priority conclusion.

There is no affirmative “first,” priority or novelty claim, no value of \(M(7)\), and no K2/K3 exclusion claim.

**Significance**

Conditional on K1, the corollaries exclude **every non-classical** 2-RQLS(7) and PQLS(7), which is stronger than excluding cardinality 49 alone. They address the specific unresolved order-seven cases identified by the ZC §5 anchor at `sources/source_fetch.receipt.json:126` and HL §5 anchor at `:171`.

They do not exclude classical PQLS(7); for example, \(|y-2x\rangle\) works. The inherited-status statement at `lane/review/K1-COROLLARY.r1.md:3–4` and scope limitations at `:51–53` are correct.

**Scope.** I read only the snapshot: manifest, revisions/diffs, both reviews, README, LEMMAS/corrections/corollary, five code files, net data, parent receipts and six raw controls, and relevant source passages/anchors. Only reading and SHA-256 hashing were performed. I could not inspect absent CNFs/proofs, executables/build records, parent checking implementations, original raw producer stdout, or external PDFs/hyperlink targets; finite-enumeration claims therefore remain reported certificate evidence, not independently established premises.