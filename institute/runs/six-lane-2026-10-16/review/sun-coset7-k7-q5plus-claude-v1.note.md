# Audit: Lemma K7-Q5⁺ (SOURCE00)

**Verdicts.** No FATAL findings.

| unit | verdict |
|---|---|
| Step 1 (SOURCE00:19–28) | **ACCEPT** |
| Step 2 (SOURCE00:30–57) | **ACCEPT**, with editorial MINORs only |
| Lemma K7-Q5⁺ (SOURCE00:15–64) | **ACCEPT-WITH-FIXES**: 1 MAJOR (scope of :64) and 3 MINORs |

## Checks

**(1) |U| and markers.**
- |U| ≥ 4 comes from |M| ≤ 3 (SOURCE01:21–23), not from Q5.
- At |U| = 4 there are three marked vertices. Each carries at least one marker, and each of the three markers sits on at most one vertex. So markers and marked vertices are in bijection.
- The resulting profiles are z₂ = (e≥2, 1, 0), z₃ = (1, f≥2, 0) and z₅ = (1, 1, h≥1).
- The table at SOURCE00:39–41 uses these profiles without stating them.

**(2) Step 1.**
- If h_z = 0 then δ_z(5) = 1, because v₂5 = v₃5 = 0. Unmarked apexes have δ ≡ 1.
- So τ_min = lcm(5, α_vz, α_v′z) and τ_max = ab. All three grids are 1/6, and the K2 bars depend on α only.
- The condition set is therefore exactly the all-unmarked one (SOURCE03:16).
- Only the kill half of K7-U is needed:
  - T leaves only the type (a,5,5), since 5·lcm(a,b) > ab when b ≤ 4.
  - For a ≤ 4, at the unmarked endpoint of the a-edge (or at z), lo = a/6 > hi = (a−1)/6, because a+5 ≥ 6 (SOURCE01:88–92).
- Hence α_vz = 5, q = 1 and d_z = m_z·w_z. Only |U| ≥ 2 is needed for this step.

**(3) Step 2.**
- **Local indices.** These are the full q·m·w indices, as SOURCE03:48 requires.
- **Gcds.** gcd(d_{z₂}, d_{z₅}) = gcd(2^{e−1}, q₅) and gcd(d_{z₃}, d_{z₅}) = gcd(3^{f−1}, q₅). Unmarked neighbours are isolated.
- **Allowed sets.** {z₂, z₃} has gcd 1, so the triple is excluded by heredity. The only allowed set of size ≥ 2 is:
  - {z₂, z₅} when q₅ ∈ {2, 4};
  - {z₃, z₅} when q₅ = 3;
  - none otherwise.
- **Weights.** All three choices are feasible:
  - q₅ = 1: y ≡ 1 gives Σ = 1.
  - q₅ = 5: y ≡ 1 gives Σ = 10/6.
  - q₅ ∈ {2,3,4}: weight 0 on the partner gives Σ = (4+q₅)/6 ≥ 1.
- **Strictness.** VFC-count gives Σ ≤ 1 − μ(U_v) < 1 (SOURCE04:49). This strict inequality is what kills q₅ ∈ {1, 2}, and it is valid.
- **Coverage is complete.**
  - V1 forces q = 1 at the unmarked neighbours.
  - Step 1 forces q = 1 at z₂ and z₃.
  - q₅ ranges over all of 1..5, whatever α_{vz₅} is.

**(4) Hidden assumptions.**
- None on α_{vz₅}.
- The profiles used are only those derived in (1).
- K7-Q5 is invoked only for |U| ≥ 5. Its proof (SOURCE01:164–183) uses neither mixed triangles nor the deleted example at :185.

## Findings

**MAJOR, SOURCE00:64.** This repeats the X2 defect.

*The gap.*
- K7-COV(i) assumes T and Ppair only on U-triangles and on triangles with two vertices in one twin block, plus VFC-count at unmarked vertices (SOURCE02:41–46).
- Under Q5 every block is a singleton, so the twin clause is vacuous.
- Step 1's mixed triangles {v, v′, z} are therefore not among the hypotheses.

*Counter-pattern* (passes the current hypotheses of (i)):
- Take Q5 with |U| = 4, and α_{vz₃}, α_{vz₅} ≤ 4 for every v. The U-triangles are (5,5,5), which pass.
- At each v, take q_{z₂} = 1, q_{z₃} = q_{z₅} = 2, and q = 1 at the unmarked neighbours.
- All three marked pairs have gcd 2, and no triple is allowed.
- The LP maximum of Σ is 3/6 + (5/2)/6 = 11/12 < 1, so this pattern passes (i) as stated.

*Reading of "for every admissible q".* It must be read existentially. The universal reading makes (i) vacuous: q ≡ 1 gives pairwise coprime indices and Σ = 1 at every unmarked vertex of every K7 pattern.

*Fix.* Either:
- add "T and Ppair on every {v, v′, z} with v ≠ v′ ∈ U and z ∈ M not carrying marker 5" to (i); or
- drop Q5 only from the enumeration in (v), which concerns actual configurations.

**MINOR, SOURCE00:17.** State the rules the lemma consumes:
- for |U| = 4: T and Ppair on {v, v′, z₂} and {v, v′, z₃}, then V1 and VFC-count at one v ∈ U, for every admissible q;
- for |U| ≥ 5: VFC-count alone.

**MINOR, SOURCE00:32.** Add the pigeonhole sentence and the profile consequences from (1). Subscript e, f, h and w at :39–41.

**MINOR, SOURCE00:54–55.**
- Label the cases by q₅ value: 1, 5, {2,4}, 3. The row "neither pair, q₅ ≥ 2" is only q₅ = 5.
- Replace "two positive weights" with "the only allowed set of size ≥ 2 is that pair, with weight 0+1".

## Bottom line

K7-Q5⁺ is correct at the configuration level. The :64 fix is needed only for its pattern-level use in K7-COV. K7 remains OPEN. This is a written check only; nothing was computed.
