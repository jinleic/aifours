# f369 — Independent finite shadow and complex-phase audit

Status: WRITTEN FINITE RECONSTRUCTION SUPPORTED; standalone checker supplied; EXECUTION NOTRUN.

This is a fresh same-harness finite-author result, not an independent-model-family review, human review, formal/kernel certificate, novelty assessment, original-target acceptance, actual AME construction, full support enumeration, or global t=24 exclusion. The inherited no-OLS(6) provenance is retained, not waived.

## 1. Frozen inputs and actual chronology

Assigned wave: f369-ame-t24-profile-shadow-and-phase-independent-finite-check.

Parent-supplied metadata, not reviewer-native hashes:

- Manifest SHA256: 34bf20954abd0fa0726e4aaf23da6cfed378312c3190760760616a95f3cd105d.
- Freeze-receipt SHA256: 997bea41ab082f3196e1e68d36fff60d4fd2ffc4e83d48ae9716db7240d44387.
- Literal-packet SHA256: fa0807349a97a80a89f24256dd1631d6c7c5ebd3fbd288ef5c4eec2205778027; 21,677 bytes, 394 LF.
- S1 candidate SHA256: 535c28f3ec6827285fc569271d9a8374c5cd026d9486d5b4865c486c97a80001; complete rendered source lines 1–374.
- S2 inherited-interface SHA256: 3c37fb8e669de19d50317b08d363ca40165fd1817174acf1ed6e799d4558c99c; complete source lines 1–18.

I read the entire manifest, freeze receipt, parent metadata supply and dispatch receipt; then all six named permission/status controls; sent Main a direct pre-body acknowledgement; then read literal-packet-v1.md completely, in ascending raw windows 1–20, 21–40, ..., 361–380, 381–394, including both source endings. Only after that complete packet read did I derive the finite identities and prepare this checker. The assignment and manifest already previewed the shadow equations, named profile classes, and requested phase obstruction before that acknowledgement. The acknowledgement is therefore not a claim of blindness or a cognitive-isolation certificate.

The supplied native clock observations 2026-10-30T09:31:55-0700 PDT and 2026-10-30T09:40:19-0700 PDT belong to Main. Neither is claimed as my native start, derivation time, completion time, or code-execution time. No native hash/date execution is claimed.

All controls were used only for status and permissions. No sibling output, held f337/f340 payload, parent held-claim reasoning, or held diagnostic consumer was read or used. I did not follow the historical-review links in S2. I did not independently fetch the paper cited in S1; the phase necessity below is derived directly and does not import that lemma or any novelty conclusion.

## 2. What is independently checked in writing

For 24 maximal words, the exact shadow is

sum(n_k)=24,
sum(k n_k)=C=6 sum(q_i)-48,
sum(binomial(k,2) n_k)=M=sum_{i<j} q_i q_j-72,

with q sorted in {3,4,5}^4 and all n_k nonnegative integers.

For every k=0,1,2,3,4,

binomial(k,2)-2k+3 = (3,1,0,0,1)_k.

Consequently 3n0+n1+n4=M-2C+72. This identity is useful for the written reconstruction but is deliberately NOT used to generate the checker’s histograms: the code directly enumerates every weak composition of 24 into five parts and tests the two defining moments. There are binomial(28,4)=20,475 such compositions and 15 sorted profiles.

### Complete raw histogram sets

Every row below concerns the two moment equations only, before additional pair-injectivity restrictions. The tuple order is (n0,n1,n2,n3,n4).

| q | C | M | Complete raw set |
|---|---:|---:|---|
|3333|24|-18|empty|
|3334|30|-9|empty|
|3335|36|0|empty|
|3344|36|1|empty|
|3345|42|11|empty|
|3355|48|22|empty|
|3444|42|12|empty|
|3445|48|23|empty|
|3455|54|35|empty|
|3555|60|48|{(0,0,12,12,0)}|
|4444|48|24|{(0,0,24,0,0)}|
|4445|54|36|{(0,0,18,6,0)}|
|4455|60|49|{(0,0,13,10,1), (0,1,10,13,0)}|
|4555|66|63|{(0,0,9,12,3), (0,1,6,15,2), (0,2,3,18,1), (0,3,0,21,0), (1,0,3,20,0)}|
|5555|72|78|{(0,0,6,12,6), (0,1,3,15,5), (0,2,0,18,4), (1,0,0,20,3)}|

These are written exact-arithmetic results, not claimed observed program output.

In particular, 3444 requires M=12 although M>=C-24=18; 3445 requires 23 although M>=24; and 3455 requires 35 although M>=2C-72=36. The three exclusions do not depend on phases or residual moduli. The six profiles with two or more three-symbol parties also violate the raw moments; the separate necessary pair-capacity condition q_i q_j>=12 independently excludes them.

### Separate pair-injectivity restrictions

The code derives these bounds independently by exhaustive enumeration of outside-pair footprints of k=1 words, not by trusting the claimed integer bound.

A k=1 word has exactly three outside-alphabet coordinates, hence three outside pair values. Two P words cannot share any pair value. Forgetting the inside symbol gives a relaxation: any pair-injective collection of actual k=1 words maps to distinct pair-disjoint footprints. A footprint cannot be repeated, because it contains three pair values.

- 4555 has seven possible footprints: one with its sole inside party at the four-symbol party, and two for each of the other three inside-party choices. Exhausting all 128 subsets gives maximum pair-disjoint size two. Thus n1<=2. This removes exactly (0,3,0,21,0).
- 5555 has four possible footprints. Any two share an outside pair; exhausting all 16 subsets gives maximum one. Thus n1<=1. This removes exactly (0,2,0,18,4).

The footprint maxima follow directly in writing as well. For 4555, a word inside at the four-symbol party conflicts with every other k=1 word. Otherwise, among three such words, two share the same outside symbol at that party; their two-element subsets of the other three parties intersect and force a repeated pair. Two distinct four-party footprints with different outside symbols at the four-symbol party are compatible, so the relaxed maximum is exactly two. For 5555, two three-element outside-coordinate subsets intersect in at least two parties, whose outside symbols are unique, so the maximum is exactly one.

After these separate restrictions, the complete histogram sets agree with all the candidate’s tables: 4555 has its four listed histograms and 5555 has its three; every other raw set is unchanged. There are 14 raw histograms in total and 12 after the separate bounds. These counts are not claims of feasible complete supports.

### Forced residual degree shadows

For the three forced k=2,3 shadows, equation (9) is

n3(i,a)=Q-q_i-6-2r_i(a), with 0<=n3(i,a)<=6-r_i(a).

Together with sum_a r_i(a)=12 and 2<=r_i(a)<=min_{j!=i} q_j, this gives exactly:

- 3555: (4,4,4) at the three-symbol party; (2,2,2,3,3) at each five-symbol party.
- 4444: (3,3,3,3) at every party.
- 4445: (3,3,3,3) at each four-symbol party; (2,2,2,3,3) at its five-symbol party.

The checker independently enumerates these bounded nondecreasing degree sequences. It does not assert simultaneous realizability of the different pair graphs.

## 3. Direct all-three-cut parity-support check

Use the source-supplied support, in this variable order:

0000, 0011, 0101, 0110, 1001, 1010, 1100, 1111.

In every displayed matrix, row and column labels are 00,01,10,11. A dash is a structural zero. These matrices are written constructions, not captured execution output.

12|34:

row 00: 0000, -, -, 0011
row 01: -, 0101, 0110, -
row 10: -, 1001, 1010, -
row 11: 1100, -, -, 1111

13|24:

row 00: 0000, -, -, 0101
row 01: -, 0011, 0110, -
row 10: -, 1001, 1100, -
row 11: 1010, -, -, 1111

14|23:

row 00: 0000, -, -, 0110
row 01: -, 0011, 0101, -
row 10: -, 1010, 1100, -
row 11: 1001, -, -, 1111

Thus all six coordinate-pair projections have all four binary pair values, each with multiplicity two. Each flattened graph has exactly two isolated full K2,2 blocks. The checker reconstructs all entries, connected components, degrees and phase vectors directly from the supplied words.

For a nonzero 2x2 block with entries a,b;c,d, row orthogonality says a conjugate(c)+b conjugate(d)=0. The two nonzero complex summands have opposite arguments. Therefore theta_a-theta_b-theta_c+theta_d=pi modulo 2pi, regardless of whether the four moduli are equal. This is a necessary complex-phase equation, not a real-sign assumption.

Define A=theta0000+theta1111, B=theta0011+theta1100, C=theta0101+theta1010, D=theta0110+theta1001. Sorting blocks by their smallest row gives all six equations:

E0: A-B=pi mod 2pi  (12|34, rows 00/11)
E1: C-D=pi mod 2pi  (12|34, rows 01/10)
E2: A-C=pi mod 2pi  (13|24, rows 00/11)
E3: B-D=pi mod 2pi  (13|24, rows 01/10)
E4: A-D=pi mod 2pi  (14|23, rows 00/11)
E5: B-C=pi mod 2pi  (14|23, rows 01/10).

The ordinary INTEGER relation is

E0-E2+E5=0 on every phase variable,

whereas its right-hand side is pi-pi+pi=pi mod 2pi. Thus 0=pi mod 2pi, impossible. Equivalently, for unknown integers m_j, the sum would say 0=pi(1+2(m0-m2+m5)). No restriction of the theta variables to 0 or pi is used.

The supplied code also discovers an odd-RHS integer relation from the six directly reconstructed vectors by an independent deterministic search. It checks integer coefficient cancellation exactly, not modulo two.

This certifies the phase obstruction on this supplied support in writing. It does not independently enumerate the supports capable of forcing that support, certify every external-partner closure argument, or settle any of the six surviving alphabet profiles.

## 4. Complete computational deliverable and execution status

Standalone complete source: local://f369_independent_finite_verifier_v1.py (17,775 bytes reported by the scratch-file write tool).

Suggested final materialization name: f369_independent_finite_verifier_v1.py beside this author-candidate-v1.md in the assigned wave. No wave-path write is claimed; Main must exclusive-create any permanent copies and record their actual hashes.

Argv after Main materializes the exact source:

python3 -I -B /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f369-ame-t24-profile-shadow-and-phase-independent-finite-check/f369_independent_finite_verifier_v1.py

Execution: NOTRUN. The review tool policy permits only the listed read-only git/jj/gh shell operations, not a Python/native-clock/hash shell execution. I did not bypass that restriction through another tool. The permitted scratch writer created the source and this report; no repository file was edited, and no build, test runner, scientific executable or external-model CLI was launched. There is no stdout receipt, exit status, actual runtime, RSS observation, or checker hash to report.

The complete source has only standard-library imports and no network/subprocess/package installation or file mutation. It reads its own bytes for a checker hash only when actually run. It prints its receipt to stdout; it neither creates an output file nor deletes artifacts. The enumeration is statically small: two passes of 20,475 weak compositions (baseline plus a targeted moment mutation), 15 profiles, 128+16 footprint subsets, three 4x4 flattenings, and a bounded {-1,0,1}^6 integer-relation search. A 55-second cooperative guard is supplied. Actual <=60-second performance and modest memory remain unobserved until Main runs it.

### Intended-failing controls supplied, not claimed run

1. Change maximal count 24 to 23: reject MAXIMAL_WORD_COUNT.
2. Change M=24 to M=25 against the canonical 4444 histogram: reject SHADOW_SECOND_MOMENT.
3. Re-enumerate with the second-moment offset changed by one: reject HISTOGRAM_SET_MISMATCH at 4444.
4. Omit a 4555 histogram from the claimed set: reject HISTOGRAM_SET_MISMATCH, demonstrating full-set rather than cardinality-only comparison.
5. Weaken the independently derived 4555 n1 bound by one: reject HISTOGRAM_SET_MISMATCH.
6. Weaken the 5555 n1 bound by one: reject HISTOGRAM_SET_MISMATCH.
7. Delete support word 0000: reject PAIR_DEGREE, specifically row 00 in 12|34 has degree one rather than two.
8. Replace the valid relation (1,0,-1,0,0,1) by (1,0,1,0,0,1): reject PHASE_INTEGER_LHS. The latter cancels only modulo two and has an odd RHS, so this control guards precisely against a real-sign-only false certificate.
9. Change E5’s RHS from pi to zero: the fixed selected relation must reject PHASE_RHS_EVEN. This control concerns that exact certificate; it does not assert consistency of all remaining mutated equations.
10. Change all six RHS values to (1,0,1,0,1,0) in pi units: reject PHASE_RHS_EVEN for the contradiction certificate. A separate positive control verifies the explicit solution theta0000=pi and all other phases zero for that mutated equation system. The altered RHS system is an equation-only control, not physical unitary orthogonality.

Each control catches only the verifier’s intended exception class and exact invariant code. An arbitrary exception, wrong rejection code, or accepted mutation fails the overall run. No assert statements are relied on, so -O cannot silently remove checks.

## 5. Verdict and remaining boundaries

No discrepancy was found by this written finite reconstruction in the complete shadow sets, the separate 4555/5555 pair-injectivity bounds, the three forced degree shadows, or the supplied parity support’s genuine complex-phase contradiction. The standalone checker is complete but NOTRUN; its future PASS must not be backdated or described as an observed result now.

Remaining exact unpaid step: Main reviews the complete supplied source, materializes immutable copies, executes the stated argv once within the bounded role, and records actual checker hash, output, exit status and elapsed time. This is the user-requested execution fallback, not a claim that execution has occurred.

Even a future successful run certifies only the finite shadow equations and the supplied eight-word obstruction. It does not enumerate full AME tensors/supports, establish physical realizability of a surviving histogram, prove a global t=24 or N=48 exclusion, remove the inherited no-OLS(6) condition, provide independent-family/human/formal acceptance, establish novelty, or alter the deadline 2026-10-31T21:23:27Z.
