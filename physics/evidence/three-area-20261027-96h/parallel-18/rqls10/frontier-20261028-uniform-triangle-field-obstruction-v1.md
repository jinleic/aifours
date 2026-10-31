# Uniform QLS(10): an intrinsic triangle-phase field obstruction

**NEW WRITTEN AUTHOR CANDIDATE, unreviewed.** Native `/bin/date` before writing: **Wed Oct 28 17:48:31 PDT 2026**. The result is gauge-invariant and applies to EVERY incidence L and EVERY physical uniform M_* lift, but it does not prove that a physical lift exists or that arbitrary QLS are uniform. The original unrestricted 100-ray QLS10 target remains open.

## 1. Exact field and cyclotomic statements

For an actual uniform-pattern 1-resolvable QLS(n), n>=4, write `G_xy=<psi_x,psi_y>`. Whenever x,y,z are pairwise nonorthogonal, their normalized Bargmann triangle phase is

`tau_xyz=(n−2)^(3/2) G_xy G_yz G_zx`,

which has modulus1 and is unchanged by ANY per-cell phases and ANY common unitary. For EVERY nonorthogonal pair x,y,

`sum_(z: x,y,z pairwise nonorthogonal) tau_xyz = (n−2)^(3/2)`.       (1)

In the original n=10 case there are EXACTLY50 summands and their sum is `16 sqrt(2)`. Therefore, for EVERY nonorthogonal pair x,y, the field generated over Q by its50 intrinsic triangle phases contains sqrt(2). In particular, for every positive integer q with **8 not dividing q**, at least one of those50 phases is NOT a q-th root of unity. Equivalently, no gauge can make all nonzero normalized Gram phases q-th roots when 8 does not divide q.

This is a statement about **projective triangle phases / normalized Gram gain phases**, NOT the coordinate-entry alphabet in the separate prime-power theorem. For example, a q=12 coordinate alphabet need not make normalized Gram gains q=12 roots: dividing an overlap by its modulus introduces sqrt(2). No incompatible conclusion is drawn from the mere q=12 one-pair examples.

More generally, (1) forces the triangle-phase field to contain `sqrt(n−2)` whenever n−2 is nonsquare. It is an exact necessary condition, not a proof that such a field-valued set of phases can be realized.

## 2. Complete SAME-array triangle identity

Every row is an ONB and there are n rows, so for the SAME rank-one projectors `P_z=|psi_z><psi_z|`,

`sum_z P_z=n I`.

For a fixed nonorthogonal pair x,y, the physical uniform pattern gives `tr(P_x P_y)=1/(n−2)`. Thus

`sum_z tr(P_x P_y P_z)=n tr(P_x P_y)=n/(n−2)`.

The terms z=x and z=y each equal `1/(n−2)`. Any other z orthogonal to either x or y contributes0. The sum over the remaining pairwise-nonorthogonal triangles is therefore exactly1. Each such triple trace is `G_xy G_yz G_zx` and has modulus `(n−2)^(-3/2)`. Multiplying by `(n−2)^(3/2)` proves (1), including its real positive sign; no Gram gauge, phase assumption or scalar-relaxation lift is inserted. At n=10 the right side is `8 sqrt(8)=16 sqrt(2)`.

## 3. ALL-L count of the 50 terms at order10

In the nonorthogonality graph, a cell has `3(n−1)` forced-orthogonal neighbors, because its row, column and transversal intersect pairwise only in that cell. For nonorthogonal x,y their row/column/transversal blocks are all different across the same class. The two forced-neighbor sets have exactly SIX common cells: one intersection for each pair of different classes, and all six are distinct. They cannot coincide because two blocks through x intersect only at x, two through y only at y, and x,y do not share a block.

There are n²−2 cells besides x,y, and the union of their forced-neighbor sets has size `6(n−1)−6`. Thus their number of COMMON nonorthogonal neighbors is

`n²−2−[6(n−1)−6]=n²−6n+10`.

At n=10 this is50. The zero-neighbor count and triangle count are incidence statements for every L, not a particular classical vector choice. A second independent derivation from the formal incidence matrix is `A²=(4−n)A+2(n−2)I+(n−2)(n−3)J`, for A the nonorthogonality adjacency matrix. At n=10 the exact checker below observes degree72, adjacent common-neighbor50, and forced-orthogonal common-neighbor56.

## 4. Cyclotomic conductor 8: complete elementary proof

If all50 triangle phases through x,y lie in a field K, (1) gives `16 sqrt(2) in K`, hence sqrt(2)∈K. In particular if they are q-th roots of unity then sqrt(2)∈Q(zeta_q). We now show exactly when that can happen.

If 8|q, `sqrt(2)=zeta_8+zeta_8^(-1)` belongs to Q(zeta_q). Conversely suppose 8 does NOT divide q, and put N=lcm(q,8), g=gcd(q,8), so g∈{1,2,4}. By the Chinese remainder theorem choose a satisfying

- `a≡1 (mod q)`;
- `a≡3 (mod 8)` when g=1 or2, or `a≡5 (mod 8)` when g=4.

The congruences are compatible because g divides a−1. The resulting a is odd and is coprime to q, hence gcd(a,N)=1. The cyclotomic automorphism `zeta_N -> zeta_N^a` fixes zeta_q, but sends `zeta_8+zeta_8^(-1)` to its NEGATIVE for a≡3 or5 modulo8. Thus it fixes Q(zeta_q) pointwise while negating sqrt(2), contradicting its membership there.

Therefore `sqrt(2)∈Q(zeta_q)` **iff 8|q**. It follows that if 8∤q then EVERY nonorthogonal edge has at least one triangle phase not a q-th root. The proof uses standard cyclotomic automorphisms/irreducibility and CRT, explicitly named; it does not inspect selected complex vectors or assume phases are real.

## 5. Exact finite check and surviving boundary

`frontier-20261028-uniform-triangle-check-v1.py`, SHA256 **114f246c4213e82582e6df58236ca7e7fa7cd978f8b917c9555fbc9c292a133a**, independently constructs the support graph from the verified Parker published Latin resolution and checks ALL4950 unordered cell pairs. Actual output:

```text
exact 100-cell support graph: {(False, 56): 1350, (True, 50): 3600}
every nonzero Gram edge has 50 common triangle neighbors: PASS
CRT automorphism existence checked q=1..256; iff 8 does not divide q: PASS
```

These are finite corroboration only: the ALL-L graph count and ALL-q field theorem are proved in §§3–4. The checker operates on an incidence graph, not a physical uniform Gram witness.

The divisor condition is NECESSARY, not sufficient. It cannot be strengthened to “8 divides q is impossible” merely by the single triangle sum: with zeta8=e^(2pi i/8),

`16 zeta8 + 16 zeta8^(-1) + 9(1-1) = 16 sqrt(2)`

is a sum of exactly50 eighth roots. This is a scalar multiset only, not a globally compatible set of triangle phases or a QLS construction. Higher compatibility constraints among the SAME 100 rays remain unproved.

## 6. Open scope

The theorem rules out a broad intrinsic finite phase class within the uniform-overlap branch and recovers the real-sign obstruction as a special q=2 case. It does NOT exclude all q divisible by8, all non-root or mixed-field triangle phases, the nonuniform branch, any other resolution, or the original global 100-ray target. Whether a physical M_* lift exists remains open. This candidate requires independent review and novelty screening; no actual witness, global no-go, external-model or formal proof is claimed.

**END — intrinsic triangle-phase field condition, not unrestricted QLS10 closure.**
