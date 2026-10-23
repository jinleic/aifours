# K7-NF / K7-REM: independent hostile assembly review (package v2)

**Result: 0 FATAL / 0 MAJOR / 4 MINOR.** The partition is correct, all eight block matches hold, and K7-REM follows. All four findings are about wording or provenance, and each has a one-line repair. I recommend accepting K7-NF as an **elementary assembly with no new mathematical contribution** (§5).

**Basis.** I read only the embedded text:
- package v2 `1b94bcd9…a180`, the only authoritative package; v1 ignored
- candidate `K7-NF-v1.md` `734613fd…3e97`
- scope `2469a967…351c`
- the 43 manifest excerpts
- the parent overlay `21f31a50…23f2`, applied last

I used no tools, hashing, computation or delegation.
- **Hash strings:** they agree across the package table, the manifest, the candidate and scope abbreviations, and the pins inside every verdict and erratum.
- **Not verifiable from the packet:** file bytes, byte counts, and the abbreviated Sun(5)/Sun(6) pins at `:140-141`.
- **Not used as evidence:** the Codex outcome, and every verdict frontier sentence (VZ2:7, V35:37, VU1:24-28, VZP:13).

Below, a bare `:n` means `K7-NF-v1.md` line n.

## Coverage (re-derived independently from Lemma MK)

| 2/3 placement | 5 absent | 5 on a 2/3-marked vertex | 5 on a further vertex |
|---|---|---|---|
| neither | B1 → M0 | — | B2 → M1 |
| 3 only, on t | B3 → M1 | B4 (on t) → M1 | B5 → K7-35 |
| 2 only, on z | B6 → Z2 | B6 (on z) → Z2 | B6 → Z2 |
| 2, 3 coincident on z | B7 → U1 | B7 (on z) → U1 | B8 → Z23-P5 |
| 2 on z ≠ 3 on t (= F) | (a1) → R2 | (a1) (z or t) → R2 | (a2), OPEN |

Outside F there are 11 sub-cases in 8 blocks. The blocks are pairwise disjoint and together exhaustive.

## 1. SHAPE / MK / PART: ACCEPT (0/0/0)

- **SHAPE (`:22-26`).** gcd(6r_i, 6r_j) = 6·gcd(r_i, r_j) gives both directions.
  - It matches README row 91 inside CE: C = V forces every gcd to be 6 by P1(iii) (README:49), and SHAPE gives the converse.
  - a ≤ 1 holds because 5 ∤ 6.
- **Valuations (`:30-31`).** e = 1+v₂r, f = 1+v₃r, h = v₅r. So a vertex is a 2-, 3- or 5-marker exactly when e ≥ 2, f ≥ 2 or h ≥ 1, which is the language of Z2 and H35.
- **MK (`:35-37`).** |Z|, |T|, |P| ≤ 1 by pairwise coprimality. This is README P1(ii)-(iii) with C = V, as `:37` itself says.
- **Complement of F and PART (`:41`, `:73-81`).**
  - Given MK, (Z,T) has five possibilities, and the fifth is F.
  - Each P sub-case is listed exactly once.
  - The displayed marker products follow, including B′ ≥ 0 in B6 and B7.

## 2. Blocks: each ACCEPT (0/0/0)

Every parenthetical in the cited hypotheses also holds in its block:
- Z2: m_z = 2^ε5^{h_z}, and "at most one further p … h_z = 0"
- H35: m_t = 3^A, m_p = 5^B, and five unmarked vertices
- U1: six unmarked vertices
- Z23-P5: every other vertex unmarked

So each match is literal whether those clauses are read as consequences or as extra hypotheses.

| Block | Literal statement + overlay | Literal check | Accepted scope / groups |
|---|---|---|---|
| B1 `:91-92` | M0: LFC:113-114; LFCE:10, 84 | m_i = 1, so n_i = 6w_i with w_i = r_i pairwise coprime and prime to 30 | VLFC:21, 23 |
| B2–B4 `:93-96` | M1: M1:56-57 + F2 (M1E:19-22); M1E:8 | \|M\| = 1, e = 1, m = 5^B, 3^A or 3^A5^B; F2 admits A = 0 or B = 0 | VM1:5 "Exponents are arbitrary" (M1:78's "capped excesses" is pre-F2 wording); R0 via M1:56 + VM1:13 |
| B5 `:97-99` | K7-35: K35:13-18; K35E1:21, K35E2:25 | Z = ∅; f_t ≥ 2 with m_t = 3^A, since 5 sits on p ≠ t; h_p ≥ 1 with m_p = 5^B; W unmarked | V35:11, 13 |
| B6 `:100-103` | Z2: Z2:20-24; Z2E:8 | e_z ≥ 2 and T = ∅; H puts no condition on P, so all three placements are covered | VZ2:5; the p ≠ z ROW-1 caveat (Z2:109-110) is discharged by Z2E G1 (:12-16) + VM1 |
| B7 `:104-105` | U1: U1:30-32, 158; E-1 (U1E:14-16, 103) | \|M\| = 1, m_z = 2^E3^A5^{B′}, B′ ≥ 0 | VU1:5-8 |
| B8 `:106-108` | Z23-P5: ZP:10-20; ZPE:8-9 | Exact index tuple 6·2^E3^A·w_z, 6·5^B·w_p, 6w_u, with E, A, B ≥ 1 | VZP:5 |

Supporting checks:
- **Lift (`:109-111`).** Block membership depends only on the labelled index tuple, and R0 preserves that tuple, so "no separate lift" is correct.
- **Remarks (`:113-118`).** They are accurate: K7-35 is not used on B4, U1 not on B8, Z2 not on B7/B8, and M1 not on B6/B7.
- **Omitted overlay ranges.** LFCE:11-81, Z2E:26-84, U1E:28-100 and ZPE:11-95 are not in the packet. Each is covered by an in-packet "no statement/scope change" line: LFCE:10, Z2E:8, U1E:9-10 and ZPE:8-9.

## 3. K7-REM: ACCEPT after wording fix (0/0/1)

- **Definitions.**
  - (a1) at `:122-123` matches VR2:9: z ≠ t, Bz·Bt = 0, W unmarked, and a third 5-vertex lies outside (a1).
  - (a2) at `:124-125` matches TR25:11, used as a definition only.
- **Split (`:126-128`).** Both inclusions hold, and the two parts are disjoint by |M|.
- **Corollary.** VR2:5 is the acceptance sentence, not a frontier sentence. So K7 \ F = ∅ and (a1) = ∅ give K7 = (a2).
- **Boundaries (`:132-133`).** These are correct, and A2X is not used.
- **Observation (not counted).** The import is verdict-level: `:54` has "—" in the statement column. The optional corollary in SCOPE:28-29 requires nothing more.

## 4. Provenance / boundaries: ACCEPT-WITH-FIXES (0/0/3)

Checked, no finding:
- CANDIDATE_UNVERIFIED labels at `:5` and `:136`.
- No full-K7, Sun(7), novelty, Lean or human-review claim (`:132-133`, `:142-143`; package:22-23, 110-111).
- A2X is not a premise.
- Sun(5)/Sun(6) are disclosed as computer-assisted transitive imports at `:139-141`, which matches VLFC:18 and VZP:15.
- No source proof is re-claimed (`:11`, `:57`, `:137-138`).
- Every v2 pointer (package:31, 37, 54, 97-105) matches the candidate's line numbers.
- The manifest's 43 entries from 26 sources match the table.
- The scope was frozen at 16:07:20, before the candidate at 16:10:40. The pre-freeze sketch is disclosed (SCOPE:42-48) and is identical to the delivered result.

**Resolved by the parent overlay (not counted).**
- `:143` "No computation of any kind was run" contradicted `:44`, where the author says they hashed the pinned files, and package:7-8 and 115-116.
- It also sat badly next to VZP:15, which says the inherited Sun(t ≤ 6) chain is not computation-free.
- The overlay replaces exactly that sentence and changes no mathematics. Together with `:139-141`, that is sufficient.

## Findings

| ID | Group | Location | Finding | Minimal repair |
|---|---|---|---|---|
| m1 | K7-REM | `K7-NF-v1.md:120` | The header says "(navigation; accepted results only)", but the corollary rests on the candidate Theorem K7-NF (`:129`; `:131` "accepted results plus Theorem K7-NF"; `:136`). | Change the header to "(navigation; accepted results plus the candidate Theorem K7-NF)". |
| m2 | Prov. | `K7-NF-v1.md:56`; `K7-NF-SCOPE-v1.md:38` | An external unit "MK" is listed as not used. Meanwhile this file's own Lemma MK (`:35-37`) is used at `:41, :73, :79, :99, :107, :126-127`. This is a name collision only: Lemma MK is proved in-file from SHAPE. | Add: "'MK' at :56 is the external unit of that name, distinct from this file's Lemma MK (:35-37)", or rename the lemma. |
| m3 | Prov. (bears on K7-REM) | `K7-NF-v1.md:55-57` | The "Not used anywhere" list includes TC/CELL. But the (a1) closure that K7-REM imports is accepted through TC-A22, TC-B, CELL-A and CELL-B (VR2:17), and this transitive use is not disclosed (unlike Sun at `:139-141`). Also, "A1" is undefined in the packet; the rules addendum A1/F7 is imported by Z2:13-14, U1:20 and ZP:34-36. | Change "Not used anywhere" to "Not cited directly". Add "TC/CELL enter only transitively, inside the accepted (a1) closure (VR2 line 17)". Pin "A1" by path and sha256. |
| m4 | Boundary | `K7-NF-v1.md:11-12` | SHAPE and MK are called "new items". SHAPE is the K7 normal form every source already uses (LFC:10-11, M1:12-13, Z2:20, U1:30, VR2:9), and MK re-derives README P1(ii)-(iii), as `:37` admits. | "The only items written here are elementary bookkeeping, not new mathematics: SHAPE (standard normal form), MK (P1(ii)-(iii) in K7), PART, the literal matching, and K7-REM." |

## 5. Acceptance: elementary assembly vs. new contribution

- **Correct as an elementary assembly.**
  - K7 \ F is partitioned exactly.
  - Each block lies inside the literal accepted scope of a single theorem.
  - This holds at actual, unbounded exponents and cofactors, in arbitrary groups.
  - K7-REM then correctly gives: every K7 configuration lies in (a2).
- **No new mathematical contribution.**
  - The exclusion is exactly the union of the accepted scopes of M0, M1, Z2, K7-35, U1 and Z23-P5, plus the (a1) closure for K7-REM.
  - What is added is a checked bookkeeping certificate: exhaustiveness plus literal matching. It confirms, against the statements themselves, what VU1:24-28 and VZP:13 had said in frontier prose.
  - It is not a new theorem and not progress on (a2). It is not an exclusion of K7 or Sun(7), and it has no novelty, Lean or human-review status.
  - All of the mathematical weight sits in the cited sources, including the computer-assisted Sun(5)/Sun(6).
- **Status.**
  - Every new claim stays CANDIDATE_UNVERIFIED until the parent verdict.
  - If the parent accepts, the K7 frontier is exactly (a2), which is still OPEN, and A2X is untouched.
