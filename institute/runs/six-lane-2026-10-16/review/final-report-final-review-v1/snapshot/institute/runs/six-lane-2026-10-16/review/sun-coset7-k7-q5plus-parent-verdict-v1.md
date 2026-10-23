# Sun k7: Q5 subfamily excluded; COV quantifiers clarified

Recorded at 2026-10-18T15:12:19-07:00.

**CORRECTNESS-ACCEPTED: no actual class-K7 configuration has quotient family Q5**, for any number of unmarked vertices. K7 itself remains OPEN (Q23/Q24), as do K6.2*, K6.3 and, pending separate disposition, K5.3. No finite enumeration or Sun(7) theorem.

Sources: [candidate](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/K7-Q5-strengthening-v1.md), SHA256 `71705ab36d850435182c4017cec4f004a39a431de49acbb7bfa42234f1e12791`; [Codex](sun-coset7-k7-q5plus-codex-v1.note.md), SHA256 `88de0105cf817f6cfd0515010438dd74afb68fcb20f02f1fb7716d8e569e30c4`; [Claude](sun-coset7-k7-q5plus-claude-v1.note.md), SHA256 `78183cb2b6d11c3bb1e74d9a1d1e376ccf838602e7d768f4fbfc12e2c6e9cec2`. Codex accepts Step1 and accepts Step2/the lemma with two MINOR corrections. Claude accepts both steps and the lemma with a MAJOR abstract-pattern scope correction and three MINORs. Neither finds a configuration-level proof defect. Both checks are written, not computation.

## Exact proof checked by the parent

K7 has at most one carrier of each marker2,3,5, hence |M|≤3 and |U|≥4. The already accepted K7-Q5 excludes |U|≥5. At |U|=4 the three marked vertices carry exactly one distinct marker each: z₂=(e≥2,1,0), z₃=(1,f≥2,0), z₅=(1,1,h≥1).

For z∈M without marker5 and v≠v′∈U, the opposite edge vv′ has label5. Its triangle divisor δ_z(5)=1; the two unmarked divisors are also1. All three P-grids are1/6, and T/Ppair coincide exactly with the all-unmarked tests. Of the surviving types, only(5,5,5) contains5. Thus α_vz₂=α_vz₃=5 and V1 forces both q-values to1.

Apply VFC at one v∈U. The local indices are three isolated w_j, then2^(e−1)w_z₂,3^(f−1)w_z₃,q₅·5^h·w_z₅. The first five q-values are1. Among marked neighbours, z₂z₃ is forbidden; z₂z₅ is allowed iff q₅ is even; z₃z₅ iff3 divides q₅. Since1≤q₅≤5, at most one pair is allowed. Heredity forbids triples.

Use coordinates(u₁,u₂,u₃,z₂,z₃,z₅):

| q₅ | Feasible weights y | Σ y_j q_j/6 |
|---|---|---|
|1 or5|(1,1,1,1,1,1)|1 or10/6|
|2 or4|(1,1,1,0,1,1)|1 or8/6|
|3|(1,1,1,1,0,1)|7/6|

All allowed singletons have weight≤1; the sole allowed pair has weight0+1. Every admissible q supplies a contradiction to VFC's strict bound Σyq/6≤1−μ(U_v)<1. Restricting q₅ further by its actual α only reduces this covered domain. Thus |U|=4 is also impossible.

## COV scope and quantifier correction (mandatory)

Both reviews correctly object to dropping Q5 from the old abstract pattern statement without adding Step1's mixed-triangle tests. Those tests are automatic for actual configurations but were absent from COV(i)'s listed hypotheses. The accepted conclusion above is **configuration-level**, not unconditional elimination of every previously admitted abstract pattern.

For an amended abstract COV statement, require T/Ppair on every mixed triangle{v,v′,z} with v≠v′∈U and z not carrying marker5, in addition to its previous triangle tests.

**Also correct the wording in [structure verdict v1](sun-coset7-k7-structure-parent-verdict-v1.md) item6 and source erratum X2:** an actual configuration supplies its own q at each vertex; it need not pass VFC for every possible q. Precisely:
- a VFC **kill** requires **for every admissible q, some nonnegative weight vector** feasible on every hereditary allowed subset and giving objective≥1;
- a pattern **survives** this kill iff there exists an admissible q with no such contradiction, at each tested vertex.

Thus the abstract coverage premise is survival under the exhaustive-q kill rule, NOT universal feasibility for all q. At Q5 the proof constructs a contradiction for every q, so no actual configuration or amended surviving pattern is lost. This distinction is essential: q≡1 is already contradictory at unmarked vertices, but other q can be realizable. Do not infer an all-pattern exclusion from the contradictory q≡1 alone.

This correction does not alter any accepted StageA/B computation: their checkers require every q to be certified before a VFC closure. No generic new representation or compute GO follows.

## Other findings and boundary

State marker pigeonhole and profiles explicitly. State that Step1 consumes the mixed T/Ppair tests, then V1/VFC at an unmarked vertex; the |U|≥5 branch needs VFC alone. Replace "two positive weights" by "the sole allowed pair has weights0 and1". Label cases by q₅∈{1,5,2/4,3}.

Imports are accepted K7-TRI/U, V1/VFC-count and the |U|≥5 Q5 lemma, with their overlays. No FH, no minimal counterexample, no Lean or human review, no priority claim. Q23/Q24 and their marked cases remain unresolved. The original files and reviews are preserved; this note is the controlling overlay.
