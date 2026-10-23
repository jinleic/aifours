## Verdict: ACCEPT-WITH-FIXES

I found no mathematical error and no error in the checker's logic. If this checker passes, the table satisfies Eqs 31–35 and 38 as written in your contract (γ re-derived, α and β taken from Appendix A). The fixes below concern how the evidence is bound and labelled; none of them changes the mathematics. A re-run after fixes 1–2 should give identical results.

## Fixes

1. **The reported SHA-256 is not tied to the bytes that were verified.** `load_table` parses `path.read_text()`. `verify` then hashes a separate `path.read_bytes()` after all the gates have run. Read the file once and hash exactly what you parse:
   ```python
   data = path.read_bytes()
   input_sha = hashlib.sha256(data).hexdigest()
   raw = json.loads(data.decode('utf-8'), object_pairs_hook=reject_duplicate_keys)
   ```
2. **Duplicate JSON keys are silently accepted.** `json.loads` keeps whichever `"entries"` comes last. Add the hook shown above so that any repeated key raises an error. The pasted table has a single `"entries"`, so this table is unaffected. Otherwise parsing is strict:
   - `type(v) is int` rejects bool, float and `1e3`;
   - JSON with leading zeros fails to parse;
   - large integers are read exactly.
3. **The report's labels go beyond the claim or misstate it.**
   - The docstring and `'source'` cite Eqs 29–35 and 41–42. The claim is Eqs 31–35 and 38, and the checker deliberately does not use printed Eq41. Replace the source with something like: `"AMH v1 Eqs 31-35,38; alpha,beta per App. A; gamma re-derived (printed Eq41 typo) = multinomial(24;24-i-j+t,j-t,i-t,p,t-p)*3^(i+j-t)*2^(t-p)"`.
   - If Eqs 29–30 contain more than definitions, either check them or drop them from the citation.
   - The status `FULL_AMH_MOMENT_POINT_VERIFIED` reads as "the full hierarchy was checked". Rename it, e.g. `AMH_EQ31_35_38_FEASIBLE_POINT_VERIFIED`.
4. **"PSD path is load-bearing" needs a precise scope.**
   - The bad point shows one thing: on this affine family, the linear gates do not imply PSD.
   - It does not validate α. Only the colour polynomial is an independent implementation; β and the 3-power factor come from the same transcription the worker used. Say this.
   - Archive the bad point together with M^(3,3)_{10,10}. A negative raw diagonal entry is a self-contained certificate (a negative 1×1 principal minor).
   - Optional and non-blocking: compare α exactly, entry by entry, against the authors' public code. Alternatively, run a positive control on a genuine code at its own n, such as hexacode [[6,0,4]] or dodecacode [[12,0,6]] with λ computed by pair enumeration; every block must pass.

## What I checked (by reading and by hand arithmetic)

**Checker against the contract**
- **Orbit enumeration:** `orbits` is a bijection onto the admissible set, and 20475 = C(28,4).
- **γ:** `orbit_size` equals the contract's γ. It also equals the q-ary γ of Gijswijt–Schrijver–Tanaka (2006) at q=4; this comparison is from memory.
- **Linear gates:**
  - x_{0000}=1 is checked directly.
  - t−p is exactly the number of anticommuting positions, so the commuting gate is the right condition.
  - Triple symmetry is tested over the whole index set, including implicit zeros.
  - Skipping odd t−p in the symmetry test is sound, because the commuting gate already forces those classes to zero.
  - γ is invariant under the triple permutation, so symmetry of x and symmetry of λ are the same condition.
- **Equalities:** row sums (d ∈ 0..24), KL for j=1..9, MacWilliams for all j, the shadow for odd j, Type II and Eq38 all match the contract.
- **Purity:** Eq32 only needs testing on nonzero entries.
- **Defaultdict:** it is only accessed at admissible keys, so it never inserts spurious entries.
- **Block range:** 169 = Σ_a(⌊(24−a)/2⌋+1), with indices k..24+a−k.
- **α:**
  - The `color_polynomial` coefficient equals the Σ_g sum in the paper.
  - The β loop covers every u that can give a nonzero term.
  - Python's `%` gives the correct sign when t−u ≤ 0.
  - The exponent (i+j)/2−t is always ≥ 0 and is unchanged by the shift (i,j,t)→(i−a,j−a,t−a).
  - α and β agree with GST's q-ary formulas at q=4 (from memory).
- **Rationality:**
  - The branch for odd i+j fails closed, and every nonzero entry has even i and j.
  - Using D⁻¹MD⁻¹ with D=diag(3^{i/2}) would remove the parity restriction; this is not needed here.
- **Gram routine:**
  - It is sound whatever the pivoting logic does: every d is positive and the reconstruction is checked exactly.
  - It is complete on PSD input, because a zero diagonal forces a zero row.
  - It handles zero pivots and all-zero blocks.
  - The two controls exercise both rejection branches.
- **Block sums:** summing only over nonzero entries is correct, since x=0 everywhere else.

**Table (spot checks, not exhaustive)**
- **Support count:** I counted admissible orbits with i, j, d ∈ {0,10,…,24} and even t−p, giving 25 + 1591 = 1616, which is the reported count.
  - So the table's support is exactly the allowed set, and every allowed orbit is strictly positive.
  - The per-group counts match: 22 for (10,10), 35 for (12,12) and 9 for (24,24).
- **Sums:**
  - The d=0 row (diagonal entries) sums to 2^24, and Σ A_i = 2^24.
  - All nine (24,j) groups sum to A_24·A_j. The i=24 row therefore equals 2^24·A_24, which under the enforced symmetry is the d=24 row sum.
  - (10,10) sums to A_10² = 331,822,656, and (12,12) sums to A_12² = 24,489,746,064.
- **Symmetry equalities** that hold:
  - (10,12,10,0) = (12,12,12,2)
  - (10,12,10,2) = (10,10,8,0)
  - (16,18,12,4) = (18,18,14,6)
  - (14,16,9,5) = (16,16,11,7)
  - (24,24,24,24−d) = (d,24,d,0) for every d
- **Eq38:** Σ iA_i = 18·2^24 and Σ i²A_i = 657·2^23, so B_1 = B_2 = 0.
- **Two 1×1 blocks:**
  - (24,24): M = 6^{−24} Σ_p (−1)^p 2^p λ_{24,24}^{24,p}, which is positive because every nonzero p is even.
  - (0,12): M = (12!)²/(24!·3^12) · Σ_t (−1)^t Λ_t / C(12,t), where Λ_t = Σ_p λ_{12,12}^{t,p}. Exactly, 27720·Σ = 23,014,759,680 > 0.

**Side observation** (not part of the claim): every group I summed satisfies Σ_{t,p} λ_{i,j}^{t,p} = A_i·A_j. That is consistent with a genus-2-type construction.

## Not checked
- I ran nothing. I did not verify the runtime, the SHA, the archived Gram factors, the other 167 blocks, the remaining row sums, or the full gate evaluations.
- I did not read the paper. Whether Eqs 31–35, 38 and Appendix A are transcribed faithfully, and whether no condition was left out, rests on your contract and the other reviewer.
  - A pointer for that reviewer: the classical GST template also has the bound 0 ≤ x ≤ x_{i,0}^{0,0} and a second PSD family in x_{i+j−t−p,0}^{0,0} − x.
  - They should confirm in writing that Eq31 in v1 has no analogue of either.
- I did not check the bad control point, because it was not provided.
- I did not assess the genus-2 family, the extra MacWilliams identities, whether a code exists, or novelty.
