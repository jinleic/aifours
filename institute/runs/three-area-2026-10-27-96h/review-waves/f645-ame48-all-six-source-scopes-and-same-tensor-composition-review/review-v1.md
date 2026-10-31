# ReviewF645AMEScopes — complete source-scope and same-tensor composition review

**Status: UNADOPTED. Returned in full for parent materialization and full-read disposition.**

**Overall correctness: correct at the explicitly conditional, adopted-source scope below.**  
**Findings within that scope: 0 FATAL / 0 MAJOR / 0 MINOR.**  
**Confidence: 0.98 for the source-scope and composition audit, not for independent verification of unprovided source proofs.**

The eleven supplied dispositions support two distinct conclusions:

1. **Conditional t24 no-go:** retaining the named no-OLS(6) import, no actual complex AME(4,6) tensor has support exactly48 and exactly24 maximal coefficients.
2. **Conditional necessary residual:** additionally retaining the adopted maximal-count boundary and its exact f113 provenance, any support48 tensor would necessarily have exactly28 maximal coefficients.

Neither conclusion excludes t28 or all support48. Neither establishes existence, N≥49, an exact support minimum, source authenticity or novelty.

## 1. Read order, coverage and independence

I read the complete manifest, freeze receipt, parent metadata supply, actual dispatch record, and all fifteen status-only controls through their endings. I then delivered a successful **direct pre-body ACK to Main before opening any mathematical packet body**.

The subsequent first mathematical read covered the entire literal packet consecutively in raw windows:

**1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–220, 221–240, 241–260, 261–280, 281–300, 301–320, 321–340, 341–354.**

Every source ending was included. No packet elision or truncation requiring recovery appeared. Derivation began only after the final S11 ending.

The identities below are **parent-supplied bindings**, not independently measured child hashes:

- Manifest: **bd787485de8d080c1f146f10403bd88f22cfb7861ec5a007a1257c89af9d4661**
- Freeze receipt: **6602e6ed622bdb000c000dfaf6c63faffa9c4cdb7e756ba6fb5473ac48baa7af**
- Literal packet: **ba22c67a960b61b00b96a91ca7d750dfd0f8657c17f2c67e24028a48b1d8ffd6**

Complete body coverage:

| Source | Supplied disposition | Source LF read | Packet LF |
|---|---|---:|---:|
| S1 | Composed no-distance-one/no-six-symbol interface | 1–18 | 3–20 |
| S2 | Alphabet shadows and complex external-partner obstruction | 1–28 | 21–48 |
| S3 | Entire4444 exclusion | 1–23 | 49–71 |
| S4 | Entire4445 exclusion | 1–27 | 72–98 |
| S5 | Entire actual3555 exclusion | 1–37 | 99–135 |
| S6 | Entire actual4455 exclusion | 1–49 | 136–184 |
| S7 | Entire actual4555 exclusion | 1–45 | 185–229 |
| S8 | Entire actual5555 exclusion | 1–41 | 230–270 |
| S9 | Support48 maximal-count restriction and distance interface | 1–36 | 271–306 |
| S10 | Standalone support48/t27 exclusion | 1–31 | 307–337 |
| S11 | N47 and global maximal-count compositions at f113 provenance | 1–17 | 338–354 |

All references below use the packet’s **Sx source-LF labels**, not transport line numbers or linked originals.

No linked author proof, prior reviewer body, sibling return, author code, held payload or excluded consumer was opened. No scientific executable, CAS, interpreter, solver, replay, new selected diagnostic instance, Git operation, build, test, lint or formatter was used. The mathematical work was written reconstruction of the supplied general predicates and explicitly named profile classes.

## 2. The common predicate being composed

For one arbitrary normalized complex four-party local-dimension-six state in one product basis, define:

- \(U=6\psi\);
- all three balanced \(36\times36\) flattenings of this **same U** are unitary;
- \(N=|\operatorname{supp}U|\);
- \(t\) counts entries of U of modulus1, equivalently coefficients of \(\psi\) of modulus \(1/6\);
- \(P\) is the actual set of those maximal words;
- \(E=\operatorname{supp}U\setminus P\);
- \(A_i=\pi_i(E)\), \(q_i=|A_i|\).

At N48/t24, P and E each have24 words. Since a unitary row has norm1, the nonzero residual amplitudes have modulus strictly between0 and1. No equal-modulus or real-phase restriction has been added.

A modulus-one entry exhausts its row and column in every balanced flattening. Consequently P projects injectively onto every physical pair. Removing P leaves a \(12\times12\) unitary with24 nonzeros and no singleton line; thus every residual line has degree2. Orthogonality rules out a longer degree-two support cycle, leaving six full \(2\times2\) blocks in each cut.

Therefore, for **each** physical pair ij:

- \(R_{ij}=\pi_{ij}(E)\) has size12;
- each value in \(R_{ij}\) has exactly two E extensions;
- \(\pi_{ij}(P)=[6]^2\setminus R_{ij}\).

These are the actual common-P/E interfaces in S2 LF7, S3 LF11, S4 LF11, S5 LF9, S6 LF11, S7 LF9 and S8 LF5. They do not permit choosing a different P, E or pair complement for a different cut.

**Disposition: SUPPORTED at the supplied-source scope.**

## 3. Independent reconstruction of the complete sorted profile list

### 3.1 Exact imported alphabet restriction

S1 LF7–10 states, for the actual N48/t24 tensor and **conditional on no-OLS(6)**:

- E has no distance-one pair;
- no residual party uses all six symbols;
- every \(q_i\) is3,4 or5.

The source explicitly identifies this as a composition replacing an earlier no-distance-one hypothesis by the classical import; see S1 LF3 and LF14.

I retain this dependency. The six-profile list is **not** being treated as an unconditional alphabet classification.

### 3.2 Common-P moments

For \(w\in P\), let \(k(w)\) count its coordinates lying in their respective residual alphabets.

At party i, the residual degrees sum12 and the maximal occurrence count is \(6-r_i(a)\). Thus

\[
C=\sum_{w\in P}k(w)
=\sum_i(6q_i-12)
=6\sum_i q_i-48.
\]

For pair ij, the internal P pair values are exactly the \(q_iq_j-12\) internal values outside \(R_{ij}\). Pair injectivity of the **same P** gives

\[
M=\sum_{w\in P}\binom{k(w)}2
=\sum_{i<j}q_iq_j-72.
\]

These recover S2 LF9–12 without replacing common-P incidence by independent pair counts.

For integer \(0\le k\le4\),

\[
\binom{k}{2}\ge k-1,\qquad
\binom{k}{2}\ge2k-3.
\]

Summing over24 P words yields exactly

\[
M\ge C-24,\qquad M\ge2C-72.
\]

### 3.3 Exhaustiveness and exclusions

Every \(R_{ij}\) contains12 distinct values in \(A_i\times A_j\), so \(q_iq_j\ge12\). Hence two three-symbol parties are impossible.

If there is exactly one three-symbol party, sorting leaves precisely the supplied classes3444,3445,3455,3555. The first three fail the reconstructed inequalities:

| Profile | C | M | Contradiction |
|---|---:|---:|---|
| 3444 | 42 | 12 | \(12<42-24=18\) |
| 3445 | 48 | 23 | \(23<48-24=24\) |
| 3455 | 54 | 35 | \(35<2(54)-72=36\) |

Thus3555 is the only remaining sorted class containing a3.

If there is no3, all four entries are4 or5, so the complete sorted alternatives are4444,4445,4455,4555,5555.

The necessary list is therefore exactly

\[
\boxed{\{3555,4444,4445,4455,4555,5555\}}.
\]

There is no omitted three-symbol case or four/five-symbol case. This reproduces S2 LF14 from its actual same-tensor predicates, with the S1 import retained.

**Disposition: SUPPORTED, conditional on the named no-OLS-dependent alphabet interface.**  
**Realizability of any listed profile: not asserted.**

## 4. Audit of all six whole-profile consumers

The consuming theorem endpoints are complete fixed-profile exclusions, not finite fixtures or conditional local lemmas.

| Class produced by the list | Consuming endpoint | Exact scope match |
|---|---|---|
| 3555 | S5 LF3 | One actual U, three unitary balanced cuts, N48/t24, profile3555 up to physical party permutation; arbitrary complex amplitudes |
| 4444 | S3 LF7 | One normalized complex AME tensor, all three cuts unitary, N48/t24, four residual symbols at every party |
| 4445 | S4 LF7 | The same actual U, N48/t24, profile4445 up to physical party permutation |
| 4455 | S6 LF3 | Entire4455 stratum, including nonregular four-party patterns and both maximal-word regimes |
| 4555 | S7 LF3 | Entire4555 stratum, all stated histograms, degree patterns and ordinary/exceptional placements |
| 5555 | S8 LF3 | Entire5555 stratum, all histograms and ordinary/exceptional degree placements |

Each consumes the same normalization, support count, maximal-entry count and definition of residual alphabet used by the classification.

Physical party permutations do not create a missing branch:3555,4445,4455 and4555 explicitly include them;4444 and5555 impose the same alphabet size at every party. A party permutation acts jointly on U, P, E and their projections. It is not an independent pairwise gauge choice.

### 4.1 S3: entire4444

**SUPPORTED as a whole-profile source import.**

- S3 LF7 allows arbitrary complex phases and nonzero moduli.
- S3 LF3 explicitly excludes no-distance-one and no-OLS as prerequisites of this fixed-profile theorem.
- S3 LF11–15 describes a universal common-P normal form and the ensuing forbidden rectangle.
- S3 LF13 expressly distinguishes the simultaneous relabeling of arbitrary common P from six unrelated pair normalizations.
- S3 LF21 expressly limits finite evidence: it does not enumerate all raw P or E, and does not replace the written universal reduction.

No additional canonical-P hypothesis must be supplied by the composition caller.

### 4.2 S4: entire4445

**SUPPORTED as a whole-profile source import.**

- S4 LF7 is the actual same-tensor theorem, including party permutations.
- S4 LF3 disclaims no-distance-one, no-OLS and modulus/phase restrictions.
- S4 LF15 couples T and F through the same global matching incidence.
- S4 LF17 explicitly includes the distance-one-allowed, exactly-two-equal partition case.
- S4 LF23 confines the finite work to necessary interfaces and leaves the universal actual-to-interface implication to the written proof.

The caller is not required to impose a no-distance-one hypothesis or select a special low-symbol slice.

### 4.3 S5: entire3555

**SUPPORTED as a whole-profile source import.**

- S5 LF3 covers arbitrary complex residual amplitudes and party permutations without no-OLS, no-distance-one, equal-modulus or independent-pair-gauge assumptions.
- S5 LF11 uses the correct3555 moments60/48, explicitly not49.
- S5 LF19–29 covers one, two, three and zero off-label interaction edges.
- The zero-edge endpoint in LF29 allows distance-one pairs and ends in a single nonzero complex-product contradiction.
- The older S2 LF20 conditional external-partner statement is not being promoted to “every block contains a low-degree row.” That stronger assertion was expressly not adopted there and is unnecessary to importing S5’s complete endpoint.

### 4.4 S6: entire4455

**SUPPORTED as a whole-profile source import.**

- S6 LF3 covers the entire stratum, including nonregular four-party patterns and both maximal-word regimes.
- The absence of four-party twins is derived in LF21–23, not imposed on the input.
- The direct contradiction in LF31 uses injectivity of the same P.
- S6 LF33 says that endpoint needs only its Sections1–3, not rounding or an external no-OLS theorem.
- The separate six-projection rounding in LF37–39 is not substituted for the primary direct-P proof.
- S6 LF41 leaves the optional Euler–Tarry/Betten source assurance unpaid.
- S6 LF47 expressly marks the two-component weak fixture NOTTESTED; the source assigns the union step to the written common-E multiplicity argument.

Thus no unverified external classical reference or untested global fixture is silently required by this fixed-profile consumer.

### 4.5 S7: entire4555

**SUPPORTED as a whole-profile source import.**

- S7 LF3 includes every listed four-party pattern, including5322, all stated maximal-word histograms and ordinary/exceptional five-party placements.
- S7 LF23 covers the no-A-twin alternatives.
- S7 LF27–29 covers full4,4, partial5,3 and full3,3 A twins.
- S7 LF31 states their exhaustion using the same U/P/E.
- S7 LF35 identifies the fresh f618 source and preserves the entire f596 episode and its consumers as HELD/NONINPUT.
- S7 LF41 expressly limits f634 to local interfaces: its positive components, residual-only structures and predicate mutations are not complete4555 tensors or actual global-tensor mutants.

The entire4555 conclusion is imported from the adopted written endpoint, **not inferred from f634’s finite success or any f596 material**.

### 4.6 S8: entire5555

**SUPPORTED as a whole-profile source import.**

- S8 LF3 covers all stated histograms and ordinary/exceptional placements without no-OLS, no-distance-one, equal-modulus or real-phase assumptions.
- S8 LF15–19 derives the twin and low-low restrictions from actual complex amplitudes.
- LF23, LF25 and LF27–29 cover zero, one and two twin coordinates.
- The ordinary/ordinary/exceptional/exceptional arrangement in LF27 is derived within5555, not borrowed from4455.
- LF31 names all six physical pair consumers in the final common-P collision.
- LF39 confines finite verification to local necessary interfaces and expressly excludes global tensor enumeration or continuous phase/modulus scanning.

No extra degree placement or independently chosen complement is needed at the composition boundary.

### Scope of this six-source audit

These are **source-endpoint and assumption-matching dispositions**. I have not re-certified the linked author proofs or reproduced unprovided proofs from their summaries. Their adopted theorem endpoints are the expressly supplied source imports. Their reported prior review counts are not being used as a substitute for this fresh composition reconstruction.

## 5. SAME-TENSOR quantifier composition

Let \(B_{24}(U)\) denote the actual complex AME predicate above with N48/t24, and let H denote the retained no-OLS(6) import.

The classification supplies

\[
H\land B_{24}(U)\Longrightarrow
\operatorname{sort}(q(U))\in\mathcal S,
\]

where

\[
\mathcal S=\{3555,4444,4445,4455,4555,5555\}.
\]

For every \(s\in\mathcal S\), the corresponding supplied whole-profile endpoint states

\[
B_{24}(U)\land\operatorname{sort}(q(U))=s
\Longrightarrow\bot.
\]

Start with one arbitrary hypothetical U satisfying \(B_{24}(U)\). Its actual E determines one actual sorted profile. The classification places that profile in \(\mathcal S\), and the corresponding exclusion consumes **that same U**, with its unchanged P and E.

There is no exchange of quantifiers requiring a common support to be assembled from independently feasible pair graphs. There is no need to combine different candidate tensors. There is no missing consumer for any produced profile.

Therefore

\[
\boxed{H\Longrightarrow\neg\exists U\,B_{24}(U)}.
\]

### Disposition 1: conditional whole support48/t24 no-go

**SUPPORTED**, taking the exact adopted source endpoints as imports and retaining no-OLS(6).

This excludes the **whole actual N48/t24 branch**, not merely local fixtures, one histogram, a no-distance-one subclass, equal-modulus residuals or real phases.

This conclusion itself does **not** require f113 or the global t≤28 boundary.

## 6. Separate audit of the ONLY-t28 necessary residual

This is a second composition with an additional provenance boundary.

### 6.1 Exact maximal-count import

S9 LF7–9 states:

> For support exactly48, t belongs to {24,27,28}, at the adopted t≤28 boundary and its classical no-OLS provenance.

S9 LF11 supplies \(t\ge24\) from residual minimum degree2. LF13–18 eliminates25 and26, including the corrected disjoint-support subcase and component-squareness justification. Neither repair is represented as having appeared in the original author source.

The required upper boundary is supplied explicitly by S11 LF9:

- f113 gives t≤29;
- the separately named no-exactly29 record excludes29 for any support;
- hence t≤28.

This is a global maximal-count statement applied to the same hypothetical support48 state, not an inference from the N47 exclusion.

### 6.2 Exact t27 consumer

S10 LF7 excludes N48 with exactly27 maximal coefficients for arbitrary complex amplitudes, product bases and all three cuts of the same tensor.

S10 LF3 explicitly says the standalone t27 theorem is **no-OLS-independent**. Its use here must not be confused with either:

- the N47/t27 exclusion mentioned in S11 LF7; or
- the inherited provenance of the combined count statement.

The N47 theorem alone would not consume an N48 hypothesis. S10 is the correct consumer.

### 6.3 Final residual

At the retained maximal-count provenance, an arbitrary hypothetical support48 tensor has

\[
t\in\{24,27,28\}.
\]

Section5 removes24 under H. S10 removes27. Therefore

\[
\boxed{N=48\Longrightarrow t=28}
\]

at the combined source-import scope.

### Disposition 2: conditional ONLY-t28 necessary residual

**SUPPORTED**, retaining the adopted count boundary, its f113 provenance, the no-OLS-dependent t24 classification, and the standalone S10 exclusion.

“Only t28” means **necessary if a support48 tensor exists**. It does not mean:

- a t28 tensor exists;
- t28 is feasible;
- t28 has been excluded;
- support48 has been excluded.

The implication may be vacuous. No t28 construction or obstruction is furnished by this composition.

## 7. Exact no-OLS, f113, source and ACK limits

### 7.1 Classical no-OLS import

S1 LF14 identifies the relevant classical obstruction as nonexistence of the OA(36,4,6,2) completion under no-OLS(6). The supplied packet does not furnish a classical proof or independently authenticated original source for that obstruction.

S6’s optional Euler–Tarry/Betten reference is expressly not a verified substitute for this missing source proof; see S6 LF41.

**Disposition:** the conditional use is SUPPORTED. Independent proof or source authentication of no-OLS(6) is **INCONCLUSIVE / not performed**.

### 7.2 f113 and the earlier boundary

S11 LF3 retains both:

- the classical no-OLS(6) theorem;
- the prior t≤30 boundary.

S11 LF5 names the f113 t≤29 record as:

**physics-6-maximal-coefficients29-parent-v1.md**  
SHA **86968ac972bf26f1f6cac6936bbccd23b27696487c96a9779be5ef0553723d9b**

S11 LF9 names the no-exactly29 record as:

**physics-6-ame46-no-exactly-29-maximal-coefficients-parent-v1.md**  
SHA **bbe7f05da8e80c640000f2dea88b51c9ede9defeac265d9785b9ef0bf9b3d1c3**

Those bodies are not supplied here. Their names, hashes and adopted consequences are source-level provenance, not newly verified proofs. The prior t≤30 boundary must not be omitted merely because the final endpoint is t≤28.

**Disposition:** importing S11’s adopted endpoint with that provenance is SUPPORTED. Independent reconstruction of f113, its classical source or its prior bound is **INCONCLUSIVE / not performed**.

### 7.3 Unrestricted selection lemma and source identity

S9 LF30 expressly does not prove the source’s unrestricted standalone P2 six-word selection theorem or authenticate its exact source-identity description. A separate use would have to preserve its actual AME-scoped multiplicity2, simultaneous unitarity, isolation and distinct-word conditions.

This composition uses the adopted AME-scoped endpoints, not an unrestricted P2 theorem.

**Disposition:** no unrestricted P2 or source-authenticity conclusion is supported.

### 7.4 f316 ACK chronology

S10 LF29 records the actual sequence:

1. an attempted ACK file write was refused;
2. packet reading **and mathematical derivation** occurred;
3. only afterward did the first successful direct IRC occur.

That is **not a timely pre-body ACK**. It is not cured by calling the refusal an administrative transport issue or by later delivering a complete review.

The supplied disposition says the owner reconciliation did not treat this deviation alone as mathematical contamination and retained the reconstructed theorem. I import S10 at that expressly qualified adopted scope. I do not independently verify the linked reconciliation bodies or turn their reported decision into a claim that the original sequence passed.

**Disposition:** mathematical use of the adopted S10 endpoint is SUPPORTED at its stated qualification; a timely-f316-ACK claim would be REFUTED by S10 LF29. No clean-cognition certificate follows.

This fresh review’s successful direct ACK preceded its first mathematical packet read; it does not retroactively repair f316.

### 7.5 Parent source-read qualification

S11 LF16 says the earlier parent read the complete review but only the first12 lines of the72-LF author source, relying on the reviewer’s complete-read receipt for the remainder.

Nothing in this review upgrades that to a complete earlier parent source read. My complete read is of the supplied17-LF **S11 disposition**, not of the unprovided72-LF author proof.

## 8. Historical remaining lists and quarantined material

The packet contains dated frontier statements. They are not all simultaneous current claims.

Examples include:

- S1 LF16: t25/26 and later branches then open;
- S2 LF28: six surviving profiles then unpaid;
- S3 LF23, S4 LF27, S5 LF5 and S6 LF7: successively reduced historical lists;
- S8 LF41:4555 remained at that disposition;
- S10 LF23:24 and28 remained before the fresh t24 composition.

I used the theorem endpoints and reconstructed their prospective union, not any stale “remaining” sentence as current authority.

The entire f596 episode and all its consumers remain NONINPUT. S7 identifies fresh f618 as its source; it does not rehabilitate f596. The held f337/t28 compression episode, the parent compression consumer, auxiliary diagnostics and every other quarantined episode/control were used only for exclusion status. None contributed a premise, method, case selection or confidence conclusion.

The withdrawn N48 and certificate-dependent material mentioned in S11 LF11 was not used.

## 9. Claim-level final dispositions

| Claim | Disposition |
|---|---|
| The supplied no-OLS-dependent interface and same-P moments leave exactly the six sorted profiles listed | **SUPPORTED conditionally** |
| Every listed profile has a supplied entire actual complex N48/t24 exclusion with matching predicates | **SUPPORTED as adopted source imports** |
| Party permutations or omitted3/4/5-symbol cases leave a coverage hole | **REFUTED by the reconstructed case coverage** |
| The union excludes the whole N48/t24 branch | **SUPPORTED conditionally on no-OLS(6) and the adopted endpoints** |
| At the retained f113/count provenance, support48 necessarily has t28 | **SUPPORTED conditionally** |
| The standalone S10 t27 exclusion mathematically needs no-OLS | **REFUTED by its explicit standalone scope** |
| f316 passed the original pre-body ACK sequence | **REFUTED by S10 LF29** |
| f634’s finite checks constitute a global4555 tensor proof | **REFUTED as a description of the supplied evidence** |
| t28 exists or is physically feasible | **INCONCLUSIVE** |
| t28 is excluded | **INCONCLUSIVE** |
| All support48 is excluded | **INCONCLUSIVE** |
| N≥49 or an exact AME support minimum follows | **INCONCLUSIVE / unsupported by this packet** |
| no-OLS, f113 or linked original proofs are independently authenticated here | **INCONCLUSIVE / not performed** |
| Printed-source equivalence, worldwide priority or novelty is established | **INCONCLUSIVE / not performed** |
| Human, independent-family or formal/kernel acceptance is established | **Not performed; no such acceptance** |

## 10. Final verdict

**Correct at the precisely conditional source-import scope.** The six-profile classification and six whole-profile exclusions match on the same original complex tensor, P and E, so their union excludes N48/t24 under the retained no-OLS(6) import. Combining that result with the supplied count restriction and standalone t27 exclusion leaves t28 only as a necessary residual, retaining the exact f113 and ACK qualifications.

**No new FATAL, MAJOR or MINOR composition defect found.** The unprovided classical/source proofs, broader support claims and all stronger assurance remain unverified rather than silently accepted.

**All output remains unadopted until parent full-read and explicit disposition. No repository file was modified.**