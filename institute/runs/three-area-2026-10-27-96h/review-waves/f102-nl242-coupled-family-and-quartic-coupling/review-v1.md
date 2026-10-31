# Independent same-harness review: NL242 coupled family and quartic coupling

Observed native `/bin/date` immediately before creation: **2026-10-28T19:11:13-0700 PDT**. Assignment: `manifest-v1.json` (SHA-256 `c29840922e091f2b2df7ba5c7573c7744e9204c26da663b2e90174e4dc6f4037`). I read the two complete candidate bodies in manifest order, in raw windows, after checking the pinned hashes and LF/byte counts. No higher-version manifest was present in the assignment directory when inspected.

## Verdicts

1. **`frontier-20261028-coupled-family-affine-energy-obstruction-v1.md`: FATAL 0, MAJOR 0, MINOR 1.** No mathematical defect found in the stated fixed-q/P family exclusion. The minor finding concerns the provenance of the author's particular positive-control input, not the proof. I independently checked a different, explicitly specified genuine balanced NL240 control.
2. **`frontier-20261028-quartic-energy-coupling-v1.md`: FATAL 0, MAJOR 0, MINOR 0.** No defect found in the universal Pfaffian fourth-derivative condition, degree consequences, or mod-4 count consequence, within the reconstruction and limits below.

**Neither candidate excludes all balanced peak-at-most-28 functions with exactly four Walsh zeros. No four-zero exclusion follows.** Candidate 1 excludes one fixed coordinate q/P family, and candidate 2 provides necessary conditions. Neither provides a witness, a general contradiction, or sufficiency for the remaining formal count cases.

## Finding

**MINOR — first candidate, line 45, author control input not bound.** The candidate identifies its positive control as a real balanced NL240 table, but neither the cited `frontier-20261028-affine-energy-flat-check-result.json` nor the candidate identifies or hashes the actual file passed as `--balanced`. The cited checker `frontier-20261028-affine-energy-flat-check.py:9-14,25-27` accepts an externally supplied `bits` array and checks its length and sum, but does not assert each input is a Boolean bit or that its Walsh peak is 32. Thus the claim about **that particular** NL240 input cannot be checked from the pinned control artifacts alone. Bind the input bytes and invocation in the receipt and verify Boolean entries and the peak if this specific control is to be reproducible. This is not a counterexample to the general energy theorem: my separately constructed balanced Boolean peak-32 control verifies its identity on all 16 cosets.

## Pins, scope and imports

Paths below are relative to `information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/` unless stated otherwise. Live hashes matched every stated pin:

| Material | SHA-256 | Role and scope |
|---|---|---|
| `frontier-20261028-coupled-family-affine-energy-obstruction-v1.md` | `775ad16e5485ee524f47be864737d3c5fb6fe04a6dc4fe1c29e47052b6bd875a` | candidate 1, 4,204 bytes / 54 LF, fully read |
| `frontier-20261028-quartic-energy-coupling-v1.md` | `ceeaa06d3b2ae95b5ff779307a1246153ed4a465538de5bcfa94eb8e16c8e859` | candidate 2, 6,083 bytes / 61 LF, fully read |
| `frontier-20261028-even-half-four-zero-obstruction-v1.md` | `7344078fb115eb47f9d5e3c731a63d16567cb09d23af4868810c5d45ef38f8c4` | fully read; independently reconstructed T≠0 and q quadratic |
| `frontier-20261028-even-odd-quadratic-coupling-v1.md` | `30a9d8ec35a9a6d25da2e84caa172d5d019733a49f36b3d5767c75834e5b9c6f` | fully read; independently reconstructed the q-rank/weight fact used here |
| `frontier-20261028-four-zero-coupled-placement-result.json` | `ba99cc035f8cc8bbbcb9edfc99d9068263e93bdb93dfa9e368b2219f1e223c0f` | imported formal spectrum, hash checked and all 512 entries checked directly |
| `frontier-20261028-affine-energy-flat-check.py` / `frontier-20261028-affine-energy-flat-check-result.json` | `0fe4407d2e181791448bed5132ebe6a4d7b40b5c6e92ab975822b84841c727af` / `7fed6f73350cf61d11403cca1323e108bc435b2e61802ec5706bedeb49f93aba` | author control artifacts; read but not run or used as proof |
| `frontier-20261028-quartic-coupling-check.py` / `frontier-20261028-quartic-coupling-check-result.json` | `ae3acc554bc4046059110f24ccd1e8a64d321ebacb2019f073b2bcb7d748e648` / `c0c1d4e6d3f5610f08eed5c86a5575e8bdf2846779351d0874dbb4599d5cdd63` | author control artifacts; read after my checker was written and executed, not run or used as proof |

There was no input-hash mismatch. No unverified imported result is needed for either mathematical verdict: the structural statements actually used were reconstructed below. The original author `--balanced` file is **unnamed/unpinned and unverified**, as in the finding. Other material named transitively in the two prior papers is not reviewed or adopted: in particular the earlier `frontier-20261028-four-zero-spatial-barrier-v1.md` and its placement, the parent Walsh/mod-4 disposition, and the coupled-rank/Krawtchouk and prior checker artifacts. My check of the pinned coupled placement does not certify those other imports or any purported witness.

## Reconstruction: the even half and its rank

Write M for the 256 one-inputs, T for their XOR, and n(a) for the number of x in M with a·x=1. Directly from the Walsh definition, k(0)=0 and k(a)=n(a)−128 for nonzero a. Therefore k(a)≡n(a) (mod 4) for every a and k(a) mod 2=a·T.

On K=T-perp choose basis b_i. Put m_i=Σ_{x∈M}(b_i·x), which is even. The integer XOR identity modulo 4 gives

`q(Σ t_i b_i) = Σ (m_i/2)t_i + Σ_{i<j}(Σ_{x∈M}(b_i·x)(b_j·x)) t_i t_j` over F₂.

Thus q=k/2 mod 2 is degree at most two and q(0)=0; its polar is indeed `q(u+v)+q(u)+q(v)`. If T=0, K has dimension 9. The nonzero polynomial 1+q has at least 2^(9−2)=128 ones, by the usual split-on-one-variable induction. At those points |k|≤4 and at the others |k|≤6. Parseval then gives Σk²≤128·16+384·36=15,872, contrary to Σk²=16,384. Hence T≠0 and dim K=8. This independently reconstructs the load-bearing imported claim at candidate 2 lines 7–12, including why its polar has no missing q(0) term.

On the even half, q=0 iff k=0 or ±4, so `Z+F=#{q=0}`; outside K all k are odd. In an alternating symplectic basis of rank 2r, summing the sign of q over the radical gives either zero or magnitude 2^(8−r), and rank 8 has no radical. Consequently q has 120 or 136 zeros exactly at rank 8. For ranks below 8 the zero counts are among 0, 64, 96, 112, 128, 144, 160, 192, 256; q(0)=0 rules out zero zeros. This reconstructs precisely the rank classification used at candidate 2 lines 19–24 and 48, without relying on the prior paper's separate odd-Q assertions.

## Reconstruction: affine energy and the coupled family

For an arbitrary affine frequency 5-flat F=a₀+U-perp, with dim U=4, form `v_C=Σ_{u∈U}(-1)^{f(x_C+u)+a₀·u}` over the 32 cosets C of U. Character orthogonality on the quotient gives `Σ_F W²=32 Σ_C v_C²`, hence `Σ_F k²=2 Σ_C v_C²`. Every v_C is even; balance makes all Walsh coefficients multiples of 4, and therefore `Σ_C v_C≡W(a₀)≡0 (mod 4)`. An even number of v_C/2 are odd, so Σv_C²≡0 (mod 8), proving `Σ_F k²≡0 (mod 16)`. This checks candidate 1 lines 30–41 for every affine 5-flat, not just the displayed one.

For the displayed flat a₀=a₁=a₆=a₇=1, the even half has q=1 at 10 points. At even k, q=1 gives k²≡4 and q=0 gives k²≡0 mod 16. The odd half has four P=0 points and twelve P=1 points; their squared residues are respectively 9 and 1. The formal flat energy is therefore `10·4+4·9+12·1=88≡8 (mod 16)`, independent of signs and the allowed magnitudes. This contradicts the general caller and reconstructs candidate 1 lines 7–26. All 512 entries of the pinned formal placement have the asserted q/P categories; its actual flat energy is 984, while its q polar has rank 6 and its P has degree 3. The placement is not a Boolean witness: my separate inverse and shift calculations give 507 non-sign inverse values and 508 nonzero nontrivial autocorrelations.

## Reconstruction: quartic condition and count

For any 4-space L in K, an even affine coset A and any parallel odd affine coset B₀ together form a 5-flat. The squared-residue calculation and 16 odd positions imply

`Σ_A q − 2 Σ_{B₀}P ≡ 0 (mod 4)`.

A four-variable quadratic has weight 2 mod 4 precisely when its polar has rank 4, and otherwise weight 0 mod 4. The rank-4 condition is the Pfaffian of the 4-by-4 alternating matrix in any basis of L; over F₂ the determinant of any basis change is one. Hence the sum of P over every such affine 4-flat is the claimed Pfaffian, establishing candidate 2 lines 26–36 for every base point and independent direction tuple. A fifth coordinate difference therefore vanishes; the algebraic normal form of P has degree at most four. In symplectic coordinates the quartic part is `Σ_{i<j} x_i y_i x_j y_j`: it is nonzero when rank B≥4, and zero when rank B≤2. This also directly rejects the pinned placement: for directions e₀,e₁,e₂,e₃ its Pfaffian is 1 but its P derivative is 0.

For the weight claim at candidate 2 lines 40–48, expand XOR monomials as an integer sum modulo 4. A single monomial of degree at most four has weight divisible by 4; all triple and higher inclusion terms have coefficient divisible by 4; a double term survives only when two degree-4 monomials are disjoint and jointly use all eight coordinates. For rank 0,2,4,6 the forced quartics have no such pair, so wt(P)≡0 mod 4. Rank 8 has three complementary quartic pairs, hence wt(P)≡−6≡2 mod 4. Combining this with the rank/zero-count characterization proves the candidate's N congruence, noting |W|=4 or 28 occurs only on the odd half.

## Independently executed finite checks

The review-specific code and receipt were exclusive-created in this directory; the code imports no author checker. Command executed: `python3 -B independent-check-v1.py`. Script SHA-256 `83a5e18f8d07aaa5a45980ae2c93c6c561cde94aa677f1dfc9e327507042794b`; receipt `independent-check-v1.json` SHA-256 `a3ac50b5f94fd71b836d4f58c97cbc135e134f199aafb4d5287f6fdb95e7f843`. The script binds the formal placement hash before parsing. It produced the following exact results:

* Exhausted **2,048** four-variable quadratic/affine forms. Counts by `(polar rank, weight)` were `(0,0):1`, `(0,8):30`, `(0,16):1`, `(2,4):140`, `(2,8):840`, `(2,12):140`, `(4,6):448`, `(4,10):448`; all mod-4 and Pfaffian checks held.
* Seed 20261028: **125** eight-variable sample pairs, 25 at each rank 0,2,4,6,8, with random invertible linear coordinate systems and arbitrary sampled lower-degree terms. Checked **140,000** affine coordinate-direction 4-flats and **4,000** additional affine flats with independently sampled non-coordinate directions. All derivative, degree, and weight-mod-4 checks held. These are constructed polynomial samples, not actual Boolean spectra or an exhaustive eight-variable test.
* For the specified flat, direct counts were 10 even q=1 and 4 odd P=0, with actual placement energy 984≡8. Changing the category at index 455 makes the energy 944≡0 while violating the prescribed P category; this is a local sensitivity control, not a realization. A rogue quartic on rank-zero q gave derivative 1 against Pfaffian 0 and was rejected.
* The separately constructed Boolean function `f(x)=x₈+x₀x₁+x₂x₃+x₄x₅+x₆x₇` has 256 ones and peak 32, hence nonlinearity 240. Its 16 frequency cosets all satisfied the direct Walsh versus spatial-coset energy identity, each with k-energy 1024. It is a positive control for the general affine-energy identity, not a peak-28 target.
* Reconstructed q directly from support-parity counts on six balanced truth tables, one with T=0 and five with T≠0. These controls do not establish the peak bound or the nonexistence argument; the latter is the separate Parseval proof above.

## Limits

The written reconstruction is a same-harness scientific review, not an external-family, human, formal-proof or novelty verification. Exact finite checks support the algebra but do not replace it, and the random eight-variable samples do not establish existence or completeness of any realizable family. In particular, the known necessary inequalities and rank cases leave possible four-zero counts unexcluded; this review establishes no unrestricted four-zero exclusion.
