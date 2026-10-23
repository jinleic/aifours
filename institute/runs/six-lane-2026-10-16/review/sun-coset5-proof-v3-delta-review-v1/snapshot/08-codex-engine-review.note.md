**INCONCLUSIVE for the finite bridge.** Static inspection found no FATAL false-elimination path or unsound representative shortcut. The remaining MAJOR obligation is independent verification of the serialized certificates; C4 does not provide that.

All nine supplied SHA-256 hashes match. Only snapshot reads, searches, and hashes were used.

- **MAJOR — shared-code checking is described as independent verification.** [SOURCE02:110](snapshot/02-proof-v1.md:110) overstates C4. `recheck` bypasses first-firing selection, which is useful, but shares the essential implementation: `tau_min/tau_max`, `link`, `p_bounds`, `rule_N2`, and `fibre_search` ([SOURCE00:544](snapshot/00-core5_engine_v1.py:544)). FH2 repeats both searches through the same routine. A defect in those helpers can survive every recheck. **Repair:** describe C4 as a shared-code witness recheck and attach the independent parent replay before accepting the finite bridge.

- **MAJOR — C4 does not validate the serialized artifact or its coverage.** At [SOURCE00:670](snapshot/00-core5_engine_v1.py:670), it zips the original keys with in-memory lines, ignores the parsed `code`, and constructs the pattern from the original key. It never reopens the certificate file. Witness validation is permissive: T ignores its recorded bounds; K/P ignore recorded totals; FH2 ignores recorded V2 and assignment counts; N2 accepts extra payload. PB can return success through a Ppair contradiction instead of checking the stated PB conclusion. These do **not** establish a false elimination in the supplied rows, but they prevent treating this function as a strict certificate parser. **Repair:** independently parse each record, derive its pattern from its code, validate the witness schema and domain, and compare complete key sets without truncating `zip`.

- **MINOR — controls do not fail the run on failure.** SOURCE00:676–678 records recheck failures and continues; the other controls similarly produce observations rather than enforced pass conditions. The supplied observations show no reported failures. C1–C3 remain sanity evidence, particularly because realised configurations use `core=False` and consequently bypass N2/FH2.

- **MINOR — retain the written-review corrections.** [SOURCE01:139](snapshot/01-rules-v1.md:139) names the wrong linking vertex: use U or V, not W. SOURCE01:266 demands an invalid arbitrary-mutation property; the recorded result is only 94,067 broken certificates among 634,470 mutations. The named K/P demonstrations actually select T/K respectively. Neither erroneous expectation controls elimination. [SOURCE02:53](snapshot/02-proof-v1.md:53) also needs the specified-pair clarification for R5: apply the two-coset theorem directly to the j,k fibre pieces. SOURCE03:38–39 reverses the implication-arrow labels.

The universe calculation reconciles exactly. For the seven cycle types of S5:

| Cycle type | Class size | Edge cycles | Fixed vertices |
|---|---:|---:|---:|
| 1⁵ | 1 | 10 | 5 |
| 2·1³ | 10 | 7 | 3 |
| 2²·1 | 15 | 6 | 1 |
| 3·1² | 20 | 4 | 2 |
| 3·2 | 20 | 3 | 0 |
| 4·1 | 30 | 3 | 1 |
| 5 | 24 | 2 | 0 |

Burnside gives \(\sum |C|3^c/120=792\). Including the two independently chosen markers gives \(\sum |C|3^c(f+1)^2/120=21{,}150\), from \(3^{10}6^2=2{,}125{,}764\) raw triples.

SOURCE00:281–343 implements the corresponding quotient correctly: canonicalize alpha, retain its entire stabilizer, then quotient the ordered marker pair under that stabilizer. None and coincident markers are included. The fixed-width code is injective. Static searches establish 21,150 distinct, ordered record keys and 792 distinct alpha strings; they do not independently establish equality with the complete canonical orbit set.

The rule implementations match the proved hypotheses:

- **T/K:** SOURCE00:64–113 uses exact integers and rational arithmetic. The triangle maximum is floored correctly. A link detected at τ_min attains a T2 upper bound, so any feasible larger τ is impossible. K uses the correct product orientation and correctly rejects sums **≥ 1**.
- **Ppair/PB:** SOURCE00:117–151 rounds the lower bound upward and upper bound downward by the exact quantum. Containment is checked on the smaller-set side; equal sizes require both directions. Increasing intersection bounds decreases the Bonferroni expression, so substitution of all upper bounds is conservative. Equality at 1 violates the required strict inequality.
- **Fibres:** SOURCE00:161–248 enumerates every allowed membership subset for every t, fixes one inside vertex to coset zero through a valid label symmetry, and applies F3 to every t=1 vertex. Every occupied fibre of size 2–5 is checked. Omitting further constraints on subsets of an occupied fibre only weakens elimination. FH2 tests both global H2 alternatives. In Core(5), H1/H2 give proper subgroups, and SOURCE01:30 supplies the full-target minimality needed for five-piece fibres.
- **Representative r:** For \(m=4\), \(\lambda_l=r_lt_l\); for \(m=2\), \(\lambda_l=2r_lt_l\). No prime ≥5 can enter a pairwise gcd. The other endpoint’s bounded multiplier caps the common valuation, so each actual gcd divides the representative gcd. Integrality excludes no actual Core(5) assignment because \(m\mid4r_l\). Cofactors equal to 1, coincident E2/E3, and arbitrarily large prime powers are covered.

The supplied certificate totals are confirmed by static searches:

| Rule | Rows |
|---|---:|
| T | 20,465 |
| K | 637 |
| PB | 20 |
| N2 | 5 |
| FH2 | 22 |
| SURVIVE | 1 |

There are no Ppair or FH1 records.

The rare certificates also admit direct static checks. All 20 PB witnesses evaluate to the recorded value 1. All 22 FH2 records use pair {0,1}, V2={2,3,4}, and counts 864/16. For index 4, these are \(4\binom42^3=864\) assignments; every fibre has capacity at most two, so eight memberships fill all four fibres. Both singleton vertices would then need even cofactors, contradicting coprimality. For index 2, all five vertices occupy singleton fibres and every pairwise λ-gcd is 2; five memberships in two fibres force a forbidden triple. The five N2 records are precisely the five marker orbits of the all-2 alpha pattern, and L5’s argument covers them.

[SOURCE04:11866](snapshot/04-certificates.tsv:11866) is the sole survivor, `1122333333/10`. It matches SOURCE05 exactly: the stated S-D alpha array, E2=1, E3=0, and representative indices `[1620,448,44,52,68]`. SOURCE07’s engine hash and uncompressed-certificate hash match SOURCE00 and SOURCE04. The compressed artifact itself is absent, so its extraction provenance cannot be independently checked here.

Required parent runtime evidence is:

1. Independent canonical-key generation and exact set equality with all 21,150 records, including orbit coverage.
2. Independent checking of every serialized witness against its own decoded pattern, without shared engine helpers or first-firing assumptions.
3. Strict rejection of malformed records, duplicate/missing/extra keys, invalid vertices and witness shapes, and inconsistent metadata.
4. A hashed verifier source and result report tied to these snapshot hashes. Matching counts alone is insufficient.