# A maximal QLS(10) with an exact half-resolution, and the m = 7 quantum Mann core

**WRITTEN + EXACT-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at the last pin before writing: Thu Oct 29 06:19:56 PDT 2026. This is an additive successor to `frontier-20261029-quantum-mann-dichotomy-k333-k555-v1.md` (SHA-256 `9fba4852172abd8629d1695ad2ec05bc14563628880c377108b21f9fa31dde3c`).

All objects below are explicit and exactly verified. The completion statements are exact finite searches inside one stated ansatz. No maximal 1-RQLS(10) is constructed or excluded. No external model, publication or novelty clearance was used.

## 1. Exact maximal QLS(10) with five disjoint orthogonal transversals

**Object.** It has four 5x5 quadrants, each indexed by x in Z5^2. The vectors are flat:

v_q(x)_j = zeta20^{4<c_j,x> + PHI2[q][j]} / sqrt10,

with characters T = [(0,0), (0,1), (1,0), (1,3), (2,2), (2,4), (3,1), (3,4), (4,2), (4,3)]. The integer phases PHI2 are given in the script. Grid placement:
- Q00: x goes to (x1, x2);
- Q01: x goes to (x1, 5+x2);
- Q10: x goes to (5+x1, x2);
- Q11: y goes to (5+y1, 5+y2).

**Exact facts** (script `frontier-20261029-half-resolved-maximal-qls10-v1.py`, SHA-256 `7800b9c940e0a22e14716ee888cabfea80782abee4b06f702bee80bd3b5c67ae`; result JSON SHA-256 `d56a0a7d889b1cfbc4e4ccd4de83d42de3dcb75dd94bdaf5242b1f03d11f04d9`, arithmetic modulo Phi20):
- All 10 rows and all 10 columns are orthonormal bases. The 100 rays are pairwise non-parallel. So this is a QLS(10) of maximal cardinality.
- The five classes T1(u) = {Q01 and Q10 cells with x1 + x2 = u} are orthonormal bases. They are disjoint transversals and together cover half of the cells.
- The exact orthogonality graph has 1225 orthogonal pairs. The complete enumeration of orthogonal transversals finds **exactly 5**, namely the T1 classes.

Consequently this array is **not** 1-resolvable. The half-resolution cannot be extended.

**How it arises.** Take the exact K5,5,5 core (quadrants Q00, Q01, Q10) and add the rows R1 and the columns C1. In the core, every pairwise intersection of the R1 and C1 complements is exactly 1-dimensional. That forces Q11, and the forced Q11 is again flat and Z5^2-covariant. In the flat torus language, the system for the types {R0, C0, T1, R1, C1} is consistent: it has 25 solvable offset choices, and the phases have denominator 2 in units of pi/5. Only the label type T0 is inconsistent.

*Scope.* This is one explicit array, with an exact census of its own transversals. Other maximal QLS(10), and other resolutions in general, are not addressed.

## 2. Exact K7,7,7 core: quantum Mann also fails at m = 7

Script `frontier-20261029-k777-exact-construction-v1.py`, SHA-256 `0008dd52ba63cf391e5eaa690317376a18a25dc08ac8a26f5e63900916e6c0fe`. Result JSON SHA-256 `e96690aecc823e6867cc05c036c002fb5572495ab70a78853550ee1b3d5fe4a7`. Arithmetic in Z[zeta28] modulo Phi28.
- It gives an orthonormal representation of L(K7,7,7) in C^14.
- All 1911 within-context pairs are exactly orthogonal, and the 147 rays are pairwise non-parallel.
- Characters: T = [(0,0), (0,1), (1,0), (1,1), (2,3), (2,5), (3,5), (3,6), (4,2), (4,6), (5,2), (5,4), (6,3), (6,4)].

Status of L(K_{m,m,m}) orthonormal representations in C^{2m}:
- m = 1: impossible (trivial).
- m = 3: impossible (Theorem A).
- m = 5 and m = 7: exist, with exact certificates.
- Even m: classical edge-colourings exist.

Existence for all odd m ≥ 5 is conjectured, not proved here.

## 3. The flat-diagonal full-square ansatz also fails at m = 7 (exact)

Script `frontier-20261029-flat-diagonal-m7-completion-search-v1.py`, SHA-256 `5b793f782ec7092e0785e9b5f645a5a483e4eeaebb6f40dcc34dafe186677d29`. Result JSON SHA-256 `032a66afd4dfb3976b49cb4f380b5ac22d6a3210c7d5ee3f84e2c34a41adef90`.
- The search used the same exact torus criterion as for m = 5.
- 10,717 uniform T were tested (normalised so that row alpha = 0 contains beta = 0). Of these, 5,544 have a solvable K-part.
- 358,092 completion cases were tested, with **0** solvable.

So for both m = 5 and m = 7, the parity core exists in this ansatz but the full Z2-quotient square never does.

**Mechanism (exact, general within the ansatz).** Write every pairing equation with π-units, so that its right-hand side is m + 2k (mod 2m). Suppose some integer left-kernel vector y of the equation matrix has an odd coefficient sum. Then y·rhs is odd, so it is nonzero modulo the even modulus 2m. The system is then inconsistent for every offset and every T-dependent term at once.

In every inspected m = 5 case, the full K4 quadrant system has a 3-dimensional left kernel. Two of its three basis vectors have odd sums, giving y·rhs = 5 (that is, pi) mod 10. The kernel is spanned by vector-valued circulations on the quadrant graph K4, and the odd ones are exactly the "quantum Mann parity cycles".

A general proof that such an odd circulation always exists, for every odd m and every admissible T, is not given here. The m = 5 and m = 7 statements rest on the exhaustive searches.

## 4. Floating evidence (not certificates)

These runs were in-kernel and are reported as discovery data only.
- **Heisenberg-type Z5^2 actions** (Weyl ⊗ I2, and 25 twisted Weyl ⊕ Weyl variants, without the Z3 symmetry): the best K5,5,5 core residual is 0.00157, with no zero. The same code finds the diagonal cores.
- **Non-flat diagonal weights**: over the 4 K-solvable T and all 850 completion setups each (3400 cases, 2 Levenberg–Marquardt starts), the best full-array residual is 0.0955.
- **Warm start**: a full 100-vector Levenberg–Marquardt from the exact core plus the forced Q11, using the best Latin T0 structure, stalls at 2.389 under perturbations.
- **Regular Z10^2 projective ansatz**:
  - Weyl(Z10) with Latin label lines k ∈ {1, 3, 7, 9}: residuals 0.168 / 0.0497.
  - Weyl5 ⊗ characters, and characters ⊗ Pauli: 0.5.
  - The purely linear case is excluded by the classical Hall–Paige argument for Z10.
- **Local moduli** of the exact K5,5,5 core: the Jacobian nullity is 177 against 174 gauge directions. That leaves 3, which equals the flat phase family. So the diagonal family is the whole local variety near the core.

## 5. Remaining gap

A 1-RQLS(10) still needs ten disjoint orthogonal transversals at full cardinality. The best explicit exact object here has five. Open questions:
- completion of a Z2-quotient square with a core from outside the diagonal family;
- label squares without a Z2 quotient;
- a universal obstruction.

Independent review is requested of the exact certificates and of the WLOG reductions.
