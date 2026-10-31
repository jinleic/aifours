# Does one permutation boundary column force the other? Functionality sharpening and the mixed-case profile at n = 11

Owner **InfoRecursiveMDS18-2**, information-science slot **info-4**. Actual `/bin/date` before writing: **Thu Oct 29 20:34:21 PDT 2026**.

**NEW author-WRITTEN candidate; unreviewed.** Target set by the f279 disposition: must α₉ ≡ 1 force α₁ ≡ 1 for actual T2 arrays at n = 11? All statements are all-variable over actual arrays; finite enumerations are cited only as adopted f187 diagnostics; no selected hypothetical square, search, solver, program or external model is used. **The main question is NOT PROVED here**; the exact first unproved step is named. Inputs: T1/T2 definitions; the f279-adopted boundary laws (outdeg_M = α₉, indeg_M = α₁, |M| = n); elementary function-graph facts.

## 1. Duality

Row-reversal maps any T2(n) to a T2(n) (adjacencies and distance-two pairs transpose; distinctness is preserved) and exchanges second ↔ penultimate columns: α₁(Aᵨ) = α₉(A) and α₉(Aᵨ) = α₁(A), with M(Aᵨ) = M(A)ᵀ. Hence the implication α₉ ≡ 1 ⇒ α₁ ≡ 1 holds for all T2(n) iff its reverse does; a mixed class, if nonempty, is reversal-closed with the roles of the two columns swapped.

## 2. Functionality sharpening: one permutation column already fixes the incidence profile

**Theorem 2 (all T2(11)).** If α₉ ≡ 1 (each symbol penultimate exactly once), then M is the graph of a function m : S → S (each x misses exactly one ordered pair), and with t = the number of 2-cycles of m,

(k₀, k₁, k₂) = (t, 11 − 2t, 44 + t).                                        (1)

The same conclusion holds if α₁ ≡ 1, by §1.

*Proof.* Out-degrees all 1 make the 11 arcs of M exactly {(x, m(x))}. A mutual pair {x,y} (both arcs present) is precisely a 2-cycle of m, carrying 2 arcs; every other arc is asymmetric. So k₀ = t and 2k₀ + k₁ = 11 (f279-adopted identity), giving k₁ and then k₂ = 55 − k₀ − k₁. ∎

So the five-profile interface survives under the weaker one-column hypothesis, with these bounds on t:

- **Both columns permutations** (repaired dichotomy case A): m is a derangement; t ∈ {0,…,4} — five profiles (the parked table).
- **Exactly one column a permutation** (mixed case): m is non-bijective; its image omits the full-target symbol z, which lies on no cycle and in no mutual pair; t ∈ {0,…,5} — up to six profiles (t = 5 gives (5,1,49)).
- **Neither column a permutation:** only the odd-k₁ law survives.

## 3. Exact profile of a mixed T2(11), if one exists

Assume α₉ ≡ 1 and α₁ ≢ 1. Then some z has α₁(z) = 0 and some w has α₁(w) ≥ 2 (Σα₁ = 11).

1. **z (full target):** every ordered pair (y,z), y≠z, occurs at distance two. z is first in exactly one row, **never second**, and occupies positions 2..10 in the other ten rows; the ten events (y,z) have the ten distinct sources S∖{z}.
2. **w (α₁(w) = v ≥ 2):** w receives only 10−v distance-two events; exactly v ordered pairs (y,w) are missing, all arcs of M with target w, from v distinct sources.
3. **M is functional with image S∖{z} plus v-fold hitting of w-type vertices**; trajectories of m enter cycles among image points; z is strictly pre-periodic.
4. **σ = L∘P⁻¹** (penultimate symbol ↦ last symbol of the same row) is a **fixed-point-free permutation** (P, L are permutations; a row cannot end with its own penultimate symbol).

None of these constraints is contradictory; they delimit any future search for a mixed square.

## 4. What is known empirically (adopted diagnostics only)

- Complete enumerations (adopted f187 item 3): T2(4) and T2(6) each have **both** boundary columns permutations; all six T2(8) have **neither**. So the mixed case is excluded at n = 4, 6, 8 by complete enumeration.
- Every T2 square of terrace/Vatican type (including the pinned T2(4), T2(6), T2(21)) has **every** column a permutation (column j = {g⁻¹a_j : g ∈ G} or {jr : r}), so provenance, not a general law, explains all known non-mixed examples. At n = 21 and beyond, completeness is unknown; no mixed square is known anywhere.

## 5. First unproved step and residual

**First unproved step:** exhibit, or exclude, a T2 array (any n; specifically n = 11) with exactly one of the two boundary columns a permutation. Everything in §§1–4 is proved; the implication α₉ ≡ 1 ⇒ α₁ ≡ 1 itself remains **open**, and no witness or obstruction to it is claimed. The unrestricted T2(11) problem is untouched by this packet and remains **OPEN**.
