## Verdict

**FATAL 0 · MAJOR 0 · MINOR 3.** All three are completeness, wording or process issues. I found no correctness defect, backward edge, cycle, unbound Sun5/6 site, or silently dropped premise.

- **Global closure:** VALID relative to the named boundaries.
- **I1 and I2 bindings:** CONFIRMED.
- **What this closes:** this gate only. Full Sun7 remains UNACCEPTED pending the parent verdict.
- **Taken at accepted boundaries, not re-proved:**
  - R1b's statement
  - the label list at FULLV LF9
  - FB's discharge argument
  - the local proof bodies

## I1 — R1c ⊆ Prop 4.5: CONFIRMED

- **Provider (S56W LF68–69):** applies to every group. It forbids four disjoint left cosets with indices 2r₁, 4r₂, 4r₃, 4r₄, where the r are pairwise coprime and r₁ is odd.
- **Governing errata add no restriction.** Erratum v1 LF5 adds only the disjointness standing hypothesis. Erratum v2 LF9, LF10 and LF12 add:
  - qualification through the written re-proof, which is accepted at S56V LF10;
  - no frames;
  - finite G via the all-group R0.
  
  None of these imposes a cofactor, parity, distinctness or minimality restriction.
- **Instance (type 2, |C|=4, |D|=3, a≤1):**
  - D⊆E is R1b's output. My one-line check: Sun3 applied to d∉E, d′∈D, c∈C∖E fails because all three gcds are 2. The edge N19→N20 exists.
  - P1(iii) gives some i∈C with e_i=1.
  - r₁ = n_i/2 = 3^f·5^h·w is odd. Each r_{s+1} = n_{d_s}/4 is a positive integer.
  - D–D gcd 4 gives coprime r values.
  - C–D: gcd(2r₁, 4r) = 2·gcd(r₁, r) = 2, so these are coprime too.
  - Deletion is covered by v5 m3.
- **Graph:** the edge N06→N20 already exists (LEDGER LF237). No graph change is needed.

## I2 m1 — COVER's K6.2* leaf ⊆ FULL LF17–24: CONFIRMED (equality after R0)

Every FULL clause follows from README LF92 plus P0/P1 (LF37–50):
- **d:** f_d=0 and e_d≥2.
- **i\*:** e\*≥2 and f\*≥1.
- **c∈O:** e_c=1 and f_c≥1.
- **d–i\*:** P={2} with both vertices in E. By P0(c), min(e_d, e\*)=2, so gcd 4.
- **d–c:** gcd 2.
- **C–C:** gcd 6, and at most one vertex has f≥2 (P1(iii), using f_d=0).
- **5-part:** a≤1 means at most one vertex has h≥1.
- **w's:** pairwise coprime by P0(b).
- **Markers:** the 3-marker cannot sit on d. Both markers fall within FULL's "all placements".

The converse also holds. A finite FULL configuration satisfies README LF92. So E3-T's scope (E3V LF5, used at FULL LF26) matches FULL's class. No exhaustiveness is used (v13 n2).

## I2 m2 — corrected contract: CONSISTENT, apart from MINOR-2

I checked the contract against v2 m1, v4 m5, the v13 query (SD LF318–329) and v14 m2/m3/M2:
- **Label (1,3):** α_(d i\*)=1, so the conditional DG applies to the α\*-family.
- **Same label, α-family:** its premise fails, so M13-A's DG\*/C2\* covers it, with its own-family hypothesis.
- **Marker f\*≥2:** only (1,1) remains for this case, because (1,3) forces f\*=1.
- **Label (3,1):** reduced to (1,3) by actual INV/E6.
- **FB:** internal to N58.
- **e_d<4:** excluded by E3.

No new edge is required.

## Global claims

1. **Gate coverage — VALID.**
   - Consolidation LF77–86 partitions N01–N58 among the eight gates. Each gate has an accepted disposition.
   - Each pending condition was later closed:
     - BROW's H5/J5 → v10 m2
     - ARED's v6 dependency → DEFORDER
     - CK62's CUT2-M12 condition → v14 LF12
   - Post-gate exports also sit inside a gate:
     - v12 m6 → CA2 scope (CA2 JSON LF4)
     - v13 and v14 → CK62 / CUT2-M12
2. **Order, roots, reachability and acyclicity — VALID.**
   - I checked every input cell, including errata X2/X3, v2, v4, v5, v6, v7, v9, v11 and v13.
   - All edges are forward in N01–N08, N15, N09–N14, N16–N59.
   - The only roots are N01 and N02.
   - Every node is reachable from N59; N16 is reached via N57→N58.
   - No cycle runs through DEF, INV, ROWU, RW, NF, TRANSFER, DG or FULL.
3. **Export propagation — VALID, except MINOR-1 and MINOR-2.**
   - The DEF predicates do not carry exhaustiveness.
   - Consumer-owned gcd cells exist for N29/N30, N37/N38, N40, N41/N43 and N49.
   - I re-derived v12 m3's three N49 cells: the w's are coprime and x≤4, and the 3- and 3·5^B-labels are coprime to the {1,2,4} entries.
4. **CI62 — VALID.**
   - The capping import is exactly the restricted one (CI62 verdict LF6–11 and erratum m1–m4).
   - The ancestry N16→N57→N58 is retained.
   - v14 M2 inserts no CAP into DG\*/C2\*.
5. **Sites S1–S12 — VALID.** Each has a consumer and an N07/N08 path. In each, the cosets are:
   - left cosets in G, U_v or U\*_v;
   - right fibres translated and then inverted;
   - at most six pieces;
   - allowed to share subgroups.

   The E8 calls at N≤4 add no Sun5/6 instance.
6. **Residuals and CUT2-M12 — VALID, except MINOR-3.**
   - RES-1, 2, 4, 5, 6 and CUT

2-M12 are discharged or explicitly permitted (v13 m4; LEDGER LF318; this gate; v5 m6; RWV with CI62; v14 LF8–12).
   - Historical, certificate, seven-piece and frame premises are excluded explicitly, not silently (S56 erratum v2 m6; LEDGER LF309–312; v9 m4; v13 n3; v14 items 4–5).

## MINOR-1 — completeness: N42 is listed as an S6 consumer but has no N14 edge

- **Where:**
  - v11 m6 (LF11)
  - X7 (worker erratum LF16)
  - N42 row (LEDGER LF259, with v11 m1 LF5)
  - consolidation LF92 and LF100
- **Issue:**
  - v11 m6 puts "ROW-2 at D23P's z … with its own CE1 PF1 label-matrix check" inside site S6, and X7 lists N42 as an S6 inheritor.
  - N42 is the only one of the 13 X7 inheritors with no N14 edge.
  - No pasted cell names ROW-2's provider.
  - Under v6 MIN-2 (LF22), a consumer that checks the abstract premise must import ROW-U-deg from N14.
- **Related inconsistency:** v11 m6 says "X7 lists both N41/N43". X7 and consolidation LF100 omit N43, and also N49.
- **Consequence:**
  - Order and ancestry are unaffected: N14 is already an ancestor of N42 through N33 and N40, and any repair edge is forward.
  - One ROW-U instance lacks a literal provider edge.
- **Repair:**
  - Name ROW-2's provider in N42's cell. If it is N14's ROW-U-deg instantiated at U_z/U\*_z, add N14→N42. Otherwise cite the N33 or N40 export.
  - List the N≤4 E8 calls at N41, N43 and N49 separately, as N14 consumers with no Sun5/6 instance, or delete v11 m6's sentence about X7.

## MINOR-2 — wording: the (a)/(b) labels for DG mean two different things

- **Where:**
  - v4 m5 (LF5)
  - v13 m2 (LF6)
  - v13 query (LF9)
  - CI62 erratum m3 (LF7)
  - I2 contract (erratum v3 LF22)
- **Issue:**
  - **Sense 1 — export items:** v4 m5 defines (a) as the conditional DG statement and (b) as the G5/G6 argument. v13 m2 uses this sense: "N56 (DG-1, DG-3/G3, (b)) and N58 ((a) only)".
  - **Sense 2 — theorem parts:** v13's own query, CI62 erratum m3 and the I2 contract use DG(a)/DG(b) for the two parts of Theorem DG.
- **Misreading:** read alongside the I2 contract, K04-DG appears to say two things that contradict v4 m5 and the contract:
  - FULL does not consume DG(b);
  - M13-A consumes the conditional DG(b).
- **Consequence:** there is no mathematical gap if v4 m5's definitions govern. The contract is not literally exact against the K04-DG cell.
- **Repair:**
  - Rename v4 m5's items, for example DG-stmt and DG-arg.
  - K04-DG would then read:
    - N58 consumes DG-stmt, parts (a) and (b), under the orientation and every-four-subset-depth premises of SD LF318–329.
    - N56 consumes DG-1, DG-3/G3 and DG-arg.

## MINOR-3 — process: residual and governing-text traceability

- **Where:**
  - consolidation LF102
  - LEDGER RES-3 (LF319)
  - v10 and the BK63 disposition JSON
  - closure statement C2 (LEDGER LF282–284, with v4 m4 LF8)
  - CI62 erratum m1 and m3 (LF5, LF7)
  - v13 m4 (LF8)
- **Issue 1:** the consolidation says RES-3 (RPE 3594dd19) is "inside BK63's N39 scope". Neither v10 nor the BK63 disposition names RPE. The only literal checks remain FR LF43 and DW LF20.
- **Issue 2:** CAP-DT erratum v2 ("CD-e2") governs the rule discipline of N57 and RES-1.
  - It has no SHA256 pin anywhere in the pasted chain.
  - It is missing from C2's list of governing text outside the census snapshots.
- **Consequence:** none mathematical. RPE is wording-only, and N57 is not used operatively in the six-class contradiction.
- **Repair:**
  - Cite where the BK63 packet included RPE. Otherwise, record RES-3 as a permitted wording-only residual resting on FR LF43 and DW LF20.
  - Pin CD-e2 and add it to C2.

## Not approved

- full Sun7 (the parent verdict is still pending)
- runtime
- novelty
- Lean or human-review status

None of the three findings is a correctness or computation issue.
