# proof-k6-v3: candidate proof composition for Sun's disjoint-coset conjecture at k = 6 (CONDITIONAL; supersedes proof-k6-v2)

- **Freeze record:** host-clock time and sha256 are in `evidence/erratum-v3.sha256`.
- **Status:** candidate proof written in this lane. It is computer-assisted and has not been checked in Lean. No k = 6 theorem, gate or novelty is claimed. The parent's final verdict decides.
- **Changes from proof-k6-v2 (fa471307…78d1):** this version cites `rules-k6-erratum-v3.md`, the cumulative erratum that supersedes v1 and v2, and `CERT-FORMAT-k6-v3.md`. It also corrects the closure wording (C18). The engine, the certificates and the rule predicates are unchanged.

## Components and review status

**R0 and R1(6).**
- Files: README §2; erratum-v3 C1 and C12.
- Codex accepted them in the rules-v1 review, and the parent re-derived them.
- The frozen contract binds Core(5) proof-v3. That dependence is discharged through the accepted verdict 2cf02436…, which binds proof-v4 (C12).

**Core(5).** `R/sun-coset5-parent-verdict-v1.md` records it as CORRECTNESS-ACCEPTED.

**Reviews.**

| Item | Where it is written | Review status |
|---|---|---|
| T, K, P, F, H5, RLP, M1/M2 | rules-k6-v1, with erratum-v3 C2–C10 and C13 | Codex and Claude: ACCEPT or ACCEPT-WITH-FIXES |
| L9 hereditary Sun | rules-k6-v2; proof-k6-lemmas-v1 §1, with C15–C17 | Codex delta: ACCEPT; Claude delta: ACCEPT-WITH-FIXES (MINOR, applied as C15/C16) |
| L10 XE | — | ACCEPT from both families |
| L11 N2-6 | proof-k6-lemmas-v1 §3 | Codex delta: ACCEPT-WITH-FIXES. Claude delta: ACCEPT-WITH-FIXES, with one MAJOR proof gap ("τ involves only the primes 2 and 3"), repaired by **C14**. C11 corrects the E3 test. |
| L12 RPLP | — | ACCEPT from both families |
| Certificate format | CERT-FORMAT-k6-v3, which adds the §6 fail-closed clauses | — |

**Certificates.** `evidence/engine-v3-core56/`, hashes in `evidence/engine-v3-run.sha256`. They are unchanged.

## Composition

1. **R0.** G may be taken to be finite.
2. **The minimal frame.** Suppose Sun(6) fails, and let G be a counterexample of minimal order. By R1(6), G carries a Core5(6) configuration.
   - Sun(k) holds in every group for k ≤ 4, and also for k = 5 by the accepted Core(5).
   - Sun(6) holds in every proper subgroup of G. It is used only in an FH5 fibre of some H < G when six vertices meet one coset (C4, C15).
3. **Patterns.** Up to S6, the configuration's pattern is a labelling of one of the 8 types.
   - If a triangle is T-forbidden, the labelling is impossible.
   - Otherwise it is one of the 1,575,031 T-consistent leaves, which fall into 61,124 orbits.
4. **Certificates.** Each orbit carries a certificate:

   | Rule | Orbits | Notes |
   |---|---|---|
   | K | 55,159 | |
   | RLP | 5,513 | exact duals for every admissible q |
   | FH5 | 134 | all seven E5 placements |
   | N26 | 108 | |
   | PB | 55 | |
   | RPLP | 155 | exact duals or Farkas vectors for every admissible q |

   - There is no SURVIVE line.
   - The certificates are valid for every admissible τ (M1) and for every r with the given markers (M2, using saturation C5/C16). E5 does not affect any rule other than FH5 (C19).
5. **Closure (C18), conditional.** Suppose the parent's final verdict accepts the certificate replay under the fail-closed clauses of CERT-FORMAT-k6-v3 §6, together with the lemma reviews. Then:
   - no minimal-order Sun(6) counterexample carries a Core5(6) configuration;
   - by step 2, no minimal counterexample exists, so **Sun(6) holds for every group**;
   - unrestricted Core5(6) follows from Sun(6).

## Verification status (reported by the parent; the parent holds the record)

**Done.**
- Independent parent check of every one of the 1,575,031 leaves.
- Exact orbit coverage.
- Every K, RLP, PB, N26 and RPLP witness checked.
- FH5 replay: 134 of 134 passed.

**Pending.**
- The separate-author full checker.
- The final composition reviews from both families.
- The post-result priority audit.
- Lean (not attempted).

**Not evidence.** The lane self-check core56_checkB_v1 was stopped with outcome UNKNOWN (receipt 162bb488…3424).

No publication, no "first", no "novel".
