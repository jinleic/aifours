# v68-B — full written reconstruction of global ONB local deformation and cycle obstruction

Actual returned `/bin/date` before writing: **Sun Oct 25 09:45:09 PDT 2026**. MathResearch96h-2, mathematics reviewing PhysicsRQLS10-2. Strict WRITTEN mathematics only; metadata/source/date/hash operations only. No scientific interpreter/eval/program/enumeration/symbolic program/replay/solver, build/test, external-model CLI or nested agent. V9, immediately followed by v10, was read FIRST; all earlier errata/HOLD remain binding.

## 1. Binding, exposure, complete coverage and verdict

Exposure ACK `peer-review-rqls-global-ONB-deformation-ack-v1.json` preceded the proof body. My own346-LF PH primary had already been returned; it is separate and supplies no RQLS correctness premise. No Paley/H0/RT table or earlier review verdict was inherited.

Read ALL349 LF of the sole literal part `peer-review-wave-v68-v68-B-part1-v1.md`: complete S1/v9 LF1–35, S2/v10 LF1–31, S3/NEW theorem LF1–227 and S4/freeze LF1–33. No source truncation was reported by these reads; no omitted footer block is treated as proof. Fresh metadata hashes match:

- Part: `ee4ad53740a902add4b01e96c50b5af10da3e840edfaef3fd420343a7d7d14f4`.
- NEW `global-onb-deformation-and-cycle-obstruction-v1.md`: `580d3f3d9d760ad2de93af9186f5bc06dc5e4c87f9c9052821ad0f8954fc1415`.
- Route freeze: `ef124028be32d86e37c73cd3236b11f05d3cc63ceaa06b6c5a9c8239485e33f0`.

All LF references below mean ORIGINAL NEW theorem LFs.

**Overall verdict:0 FATAL /0 MAJOR /0 MINOR for the complete stated local/classical-seed theorem, ALL n≥3 and ALL orthogonal Latin pairs(L,M). New load-bearing obligations NOT_RECONSTRUCTED: NONE.** The exact nonlinear/tree system, full second-order criterion, separation condition and all limitations reconstruct below. This is NOT a100-ray witness or unrestricted maximal1-RQLS10 theorem.

The only analytic theorem imported is finite-dimensional REAL-analytic IFT with the square invertible tree Jacobian verified below. The resolution/classical-mate equivalence is also reconstructed directly. Reported source-access/freeze/no-execution histories in the author documents are not independently attested merely by their hashes; this reviewer performed no scientific execution. Parent disposition and stronger configured-family/human/formal/kernel/executable/novelty gates remain separate.

## 2. B0 — resolved contexts, legitimate first-row normalization and exact(O)

LF19–38.

A partition into n disjoint transversals gives a Latin label M: each symbol occurs once in each row and column. Conversely a Latin M partitions the cells into those transversals. Pair products with the classical square |M(c)> split into n mutually orthogonal symbol sectors. They form an n²-ONB exactly when the q_c in EACH M-fiber form an n-ONB. This proves the resolved/classical-mate equivalence without using an external witness or a fixed-core ansatz.

For the classical seed, Latinity of L gives one occurrence of each symbol in every row/column, and orthogonality(L,M) gives one in every M-fiber. Thus all3n contexts are exact ONBs initially.

For any nearby ONB array, choose unit representatives of its first-row rays near their prescribed basis representatives. Their ordered columns give a unitary; its adjoint sends that ENTIRE row to the prescribed ordered computational rays. One common unitary and individual ray phases preserve every original ONB. For each remaining normalized ray the leading coordinate at e_a remains nonzero and can be made positive real. Its projective ratios then give exactly

`q_c=(e_a+sum_(k≠a)z_(c,k)e_k)/sqrt(1+sum|z_(c,k)|²)`.

These are unique coordinates for rays in this slice, with all first-row coordinates0 and ALL other off-diagonal coordinates arbitrary complex numbers. They are not claimed to be a unique quotient representative for common-unitary equivalence: diagonal unitaries preserving the first-row rays still act, and the source correctly retains that residual stabilizer.

For context cells c,d labelled a≠b, direct inner-product expansion has numerator

`z_(d,a)+conj(z_(c,b))+sum_(k≠a,b)conj(z_(c,k))z_(d,k)`.

The denominators are positive. Thus(O) is EXACT, not a Taylor approximation. The chart already imposes unit norms; n mutually orthogonal unit vectors span C^n. Hence all(O), over ALL3n contexts, are necessary and sufficient for the whole fixed-resolution design. No real-only direction, fixed overlap, support profile or first-column condition was introduced.

## 3. B1 — three distinct perfect matchings, simple graph and all component bounds

LF40–50.

Every a-cell has exactly one b-cell in its row, column and M-fiber, and conversely; these are three perfect matchings on n+n vertices. Distinct cells cannot share both row and column. Sharing row AND M-symbol, or column AND M-symbol, contradicts Latinity of M. Therefore no matching edge is duplicated: Gamma_ab is SIMPLE, bipartite and3-regular, not a multigraph whose small components could evade the count.

In a component, counting its edges from each bipartition gives3n_a=3n_b, so both parts have the same size k. A vertex needs three DISTINCT opposite neighbours; hence k≥3. Summing k over components gives c_ab≤floor(n/3). These are symbolic all-input deductions, not a seed census.

The unique first-row a- and b-cells are joined by their ROW matching edge e0, hence are in one distinguished component C_ab^0. There are exactly two first-row nodes in this graph and they are both fixed by the chart.

## 4. B2 — complete(T1), conjugation conventions and real tangent dimension

LF52–72.

The linear term of(O) is x_(d,a)+conj(x_(c,b))=0. Conjugating yields x_(c,b)=-conj(x_(d,a)). Under the printed definitions w_ab(c)=x_(c,b),w_ab(d)=-conj(x_(d,a)), it is exactly w_ab(c)=w_ab(d) along every matching edge. Thus w is constant on every connected component.

Both first-row endpoints of e0 have zero coordinates, so the distinguished constant is0. Conversely assigning one arbitrary complex constant to each OTHER component reconstructs all pair coordinates by x_(c,b)=w(c) on the a-side and x_(d,a)=-conj(w(d)) on the b-side. Every linear edge equation then holds.

Each off-diagonal cell coordinate belongs to exactly ONE unordered symbol pair, so different graph systems have disjoint coordinate sets; there are no unlisted cross-pair linear equations. This is a real-linear parametrization (conjugation is present), with two real parameters for each of c_ab-1 constants. Therefore the full first-row-fixed Jacobian kernel has dimension

`2 sum_(a<b)(c_ab-1)`.

It is a tangent/kernel dimension ONLY. It is neither the dimension of the nonlinear zero set nor a smooth quotient-moduli count, and no integration of arbitrary tangent vectors is inferred.

## 5. B3 — injective Jacobian gives actual isolation; disconnected graphs give the full converse

LF74–107.

When all Gamma_ab are connected, Section4 gives ker DF(0)=0 for the real constraint map formed from all real/imaginary(O). Finite-dimensional compactness of the unit sphere gives c>0 with||DF(0)z||≥c||z||. Differentiability gives||F(z)-DF(0)z||≤(c/2)||z|| in a small ball. Hence ||F(z)||≥(c/2)||z||>0 for nonzero z. This proves ACTUAL isolation, including potential curves with zero first derivative; it does not require surjectivity of the full overdetermined Jacobian or a regular submersion hypothesis.

Undoing the first-row chart gives only common-unitary/per-ray-phase classical equivalents nearby. Conversely a classical equivalent that also lies in this ordered first-row slice must have its common unitary diagonal on the computational rays; it therefore gives the same seed rays, namely z=0. Thus the normalized-isolation and equivalence-class formulations agree.

If a graph has a component C other than C0, replace a,b cells there by

`(e_a+u e_b)/sqrt(1+|u|²)`,

`(-conj(u)e_a+e_b)/sqrt(1+|u|²)`.

Their inner product is(-conj(u)+conj(u))/(1+|u|²)=0 and each norm is1. Every context's a/b matching edge has both endpoints in C or neither; every other context ray lies in the orthogonal complementary coordinate subspace. Hence ALL3n ONBs remain exact. The first row is untouched.

For nonzero finite u, the two new rays have both a,b coordinates nonzero, are mutually orthogonal, and differ from every computational ray. The proper component leaves occurrences of BOTH a,b outside it, including the first-row pair; the other n-2 axes remain. Hence there are exactly n+2 distinct rays, not n². Letting u→0 gives arbitrarily close genuine nonclassical designs and proves the converse of the local rigidity criterion. Independent bases on the components of this ONE symbol pair work for the same context reason; no mixed-pair claim is needed here.

### ALL possible resolutions near a classical L

There are finitely many labelled Latin resolution patterns M. A non-mate M has an M-fiber with two cells of the SAME L-symbol; their seed overlap has modulus1 and remains nonzero in a neighbourhood. Such a pattern cannot support nearby ONBs. Every actual mate with all graphs connected has its own rigidity neighbourhood. Intersect the finitely many neighbourhoods; equivalently pass to a constant-M subsequence of any alleged arbitrarily close family. Nonclassical resolved arrays near L therefore exist iff SOME classical mate has a disconnected graph. This is the stated ALL-resolution LOCAL result, not a global connectedness assertion or an executed enumeration of order10 mates.

## 6. B4 — exact nonlinear(N), correct signs and all mixed coordinates

LF109–126.

The graph-node convention is a real-linear bijection on all off-diagonal coordinates, with inverse z_(c,k)=w_(a,k)(c) for a<k and z_(c,k)=-conj(w_(k,a)(c)) for k<a. This includes BOTH sides of every pair, rather than independently assigning two streams.

For a directed edge c(a)→d(b), conjugating(O) gives

`z_(c,b)+conj(z_(d,a))=-sum_(k≠a,b)z_(c,k)conj(z_(d,k))`.

The left side is w(c)-w(d), precisely(N) with the printed negative sign and conjugations. The right side is homogeneous quadratic in the REAL/imaginary coordinates, not holomorphic. Its terms from other symbol pairs are retained. Restricting to one a/b switch makes them0, but they cannot be discarded for mixed deformations.

## 7. B5 — full square tree elimination, both first-row roots, IFT and exact bijection

LF128–153.

In C0 choose a spanning tree CONTAINING e0, then delete that edge. Its two components each contain one fixed first-row root. A forest with V0 vertices has V0-2 kept edges and V0-2 nonroot unknown node values. Each other component has one free complex root parameter, Vj-1 kept edges and Vj-1 nonroot unknowns. Thus the complete kept system is SQUARE in the non-root variables; for one Gamma_ab both counts are2n-c_ab-1 complex quantities. The parameters have c_ab-1 complex coordinates.

The first-row edge e0 is identically satisfied for ALL chart values: both endpoints have all coordinates0, so their mixed quadratic right side also vanishes. It may safely be omitted. No other edge is declared redundant.

At zero, quadratic right sides have derivative0. The kept Jacobian is therefore exactly the rooted forest/tree incidence map, separately for each unordered symbol pair. Eliminating leaves produces diagonal coefficients±1 (and the same invertible map on real and imaginary parts). It is invertible despite the rest of the original constraints being overdetermined. The ordinary finite-dimensional REAL-analytic IFT applies and yields unique small nonroot coordinates depending real-analytically on the free roots u. Inverting the real-linear graph chart gives Z(u), with Z(0)=0. Conjugates preclude any holomorphic assertion.

All remaining edges outside the original spanning trees are actual chord residuals. In the distinguished component some chords join the two rooted forest pieces; their paths through the original tree use e0. They MUST be retained, because they impose nonlinear compatibility between the two zero roots. The source's “all other edges” rule indeed retains them; it does not silently treat the forest as if it had only one root.

For every such edge Omega_e is exactly its linear difference minus the quadratic R_e evaluated at Z(u). If all residuals vanish, every kept edge, every chord and e0 holds, so all original(O) and all context ONBs hold. Conversely a nearby normalized solution has definite free root values; uniqueness in the IFT neighbourhood forces it to be this Z(u), and its chords vanish. This proves the claimed EXACT bijection between all nearby normalized solutions and small simultaneous zeros of ALL Omega_e. It is not merely a map producing some solutions, and it asserts no residual independence or dimension of their common zero set.

The chart's positive square-root normalization is real-analytic near0; it introduces no hidden extra constraint into this argument. The residual diagonal stabilizer remains an equivalence action, not a second coordinate choice invalidating uniqueness within the labelled slice.

## 8. B6 — complete second-order circulation iff, including BOTH first-row zeros

LF155–170.

Take real t and z(t)=t x+t² y+O(t³), with x satisfying(T1). The graph transformation is real-linear, and R_e is homogeneous real-quadratic. The t² coefficient of(N) is exactly

`w_y(c)-w_y(d)=-sum_(k≠a,b)x_(c,k)conj(x_(d,k))=R_e(x)`.

There is no missing1/2: y is the t² coefficient, not the second derivative. Traversing a fixed a→b edge backward contributes MINUS R_e, not an additional conjugation; the physical conjugations have already been built into R_e and w.

Necessity of zero oriented circulation around every cycle is telescoping of this complex potential difference. Conversely integrate along paths from a root; zero circulations make the potential path-independent. At C0 the two prescribed first-row values can BOTH be0: the direct e0 edge has R_e0(x)=0 because every first-row x coordinate is0. Thus setting one root0 automatically sets the other0, and cycle conditions enforce consistency along every alternate path. No extra nonzero path integral between those roots is left unchecked. Other components have free additive constants.

Different symbol-pair node systems have disjoint y coordinates, so solving their potential equations simultaneously reconstructs one legitimate full y. The right sides depend on mixed pairs, but they are fixed known values once x is fixed. The condition is therefore necessary AND sufficient for ALL3n ONBs THROUGH second order.

There is no independent norm equation: normalization is exact in the projective chart, and its diagonal t² correction cannot change the off-diagonal numerator equations(O). Tree elimination at second order gives the same cycle/fundamental-chord conditions. Omega_e has zero constant/linear terms because its first-order reconstructed values obey(T1); its quadratic terms are exactly these circulations (including the e0 path condition). Higher residual orders need not vanish. A successful second-order jet is NOT an actual finite-t solution or an integration theorem.

## 9. B7 — signature injectivity, compatible constants and conditional n²-ray extraction

LF172–184.

If two occurrence cells of the same L-symbol have identical component signatures, every pair's component constant is equal at those nodes. Their off-diagonal first-order coordinates therefore coincide, including the negative-conjugate convention when that symbol is the larger one. They cannot split at first order in this chart.

Conversely assign DISTINCT complex constants to the components of EACH unordered pair, with0 on C0 and distinct nonzero values elsewhere. The same constant is used on both bipartition sides with the required conjugation; it is not chosen separately for individual cells or ordered pairs. Distinct unordered pairs have disjoint coordinate systems by Theorem A, so these choices are globally compatible as ONE tangent vector. Injective signatures make every repeated same-symbol pair differ in at least one such coordinate. This proves the exact iff for FIRST-order separation, not a nonlinear integration claim.

If an ACTUAL real-analytic zero-set curve through u(0)=0 exists and its induced derivative is separating, same-symbol chart differences are t times a nonzero vector plus O(t²), hence remain nonzero on some punctured interval. The projective chart is unique, so different coordinates mean nonparallel rays. Different seed symbols already have distinct limiting rays and retain that distinction by continuity. Finitely many pairs permit one common small nonzero-t interval, yielding n² rays. This is a correct CONDITIONAL extraction. Signature injectivity alone, an arbitrary tangent vector or second-order jet does not supply the curve. Failure of first-order signatures also does not rule out higher-order splitting or disconnected nonclassical components.

## 10. B8 — exact elementary-switch cardinalities at n10, not a general no-go

LF186–196.

A simple3-regular bipartite component contains at least three occurrences of each symbol, so c_ab≤floor(n/3). A one-pair switch supplies at most two rays per component within span(e_a,e_b); its other n-2 rays are the unchanged axes. Therefore its cardinality is at most n-2+2c_ab, which is≤14 at n=10. Switching just one proper component gives n+2=12, not100.

For k DISJOINT symbol pairs, their coordinate2-spaces are mutually orthogonal, so their separate switches remain exact simultaneously. The analogous cardinality bound is n-2k+2sum c_ab. At n10, c_ab≤3 and k≤5 give10+4k≤30. These are all-input symbolic bounds for the elementary controls; no order10 seed or component list was enumerated. They do not bound overlapping-pair solutions of the exact nonlinear system, higher-order-separated families or globally disconnected quantum components.

## 11. Scope, imports, source trust and exact residual

**New load-bearing obligations NOT_RECONSTRUCTED: NONE at the complete227-LF mathematical scope.** The resolution equivalence and legitimate all-complex chart, all graph/matching/component statements, full tangent/kernel count, actual local isolation/escape, all-resolution local argument, exact nonlinear signs, two-root forest/square real Jacobian/IFT, ALL chord residuals, second-order iff and first-order signatures have written reconstructions above.

The implicit-function theorem is the stated classical analytic import with its hypotheses verified. The author's bibliography/source-reading claims and novelty/current-status screen are not independently authenticated by this algebraic review. Basic unitary switching remains attributed as established framework. No Paley/H0/RT finite table or old236/52 scientific output is a premise.

No ACTUAL order10 seed table, nonzero mixed root solution, separating analytic curve,100-ray family, complete RT result or disconnected nonclassical component is supplied. To finish the original primary one still needs actual rays/parameters satisfying EVERY exact residual and all100 projective distinctions, or a genuinely unrestricted impossibility covering all resolutions/components. Local rigidity is not global nonexistence, and no theorem here assumes every nonclassical design connects to a classical seed.

Original maximal1-RQLS10 remains OPEN at its registered source/import boundary. Parent full-body disposition and stronger formal/kernel/human/cross-vendor/configured-family/executable/novelty gates remain separate. V9/v10 historical corrections stay intact; no scientific permission, new primary cutover, deadline reset or continuous-runtime assertion follows.
