# F820 — factorized exact local finite corroborator for the even-E common slice

**Status: NEW COMPLETE SOURCE, UNRUN; conditional written reconstruction, not an adopted result.** The exclusive source is `finite-even-E-common-slice-v1.py` in this directory. No scientific program, test, solver, compiler, CAS, or external CLI was run in preparing it. No PASS, actual counts, runtime, physical witness, or parent disposition is asserted. Parent must read the **whole source**, pin the actual bytes and interpreter, and issue a **separate GO** before any execution. The program uses only the standard library, has no input or output files, network or subprocesses, prints one JSON record, and has a cooperative 38-second internal wall deadline; a parent execution must additionally use a wall limit of at most 55 seconds. Deadline exit is explicitly `PARTIAL_COOPERATIVE_DEADLINE` (exit 2), not a pass. A failed check is `FAIL_CHECK` (exit 1); an unexpected exception is not converted to success.

## Exact scope and source interface

The mathematical object is the **same actual named rank-two m116 five-span object**: the physical `f/R,a,g,u,x=U0,y=U3`, inverse, local-H-zero and count interface, given transported original-DC character `t`, `X=(-1)^t x`, `Y=(-1)^t y`, all U0 divisibilities/caps, the simultaneous seven same-X quotient profiles, actual physical same-b graph mates and phase, `J=1`/residue, energy and all 64 common-Y U3 caps. These are imports, not consequences proved by this program. There are four D0 locations among the 16 graph mates and six ell-zero E sites. Write `d=d_E`, `k_i` for graph D0 occupancy in row `i`, and `sum k_i=4-d`. The independently imported same-X theorem excludes odd `d`; this candidate treats `d=0,2,4` and **does not delete the E sites**. There are respectively 12, 14 and 16 graph D3 mates. Physical E-site placements, the other six nonzero quotient-profile flat/sign conditions, a common ell-zero X completion, the actual inverse/phase bridge, a common full Y, the full caller, and source identity are not enumerated or established by the source.

The local checks are stronger than a single selected fixture but weaker than a physical-object search. They exhaust individual graph rows with their actual D0 positions and signs; aggregate those rows by a provably sufficient four-valued parity signature; exhaust an explicitly larger phase/slope quotient; separately exhaust local mate sign products and physical row exponents; and check direct same-array graph/mate transforms on one constructed parity-projection representative per nonempty ordered occupancy, with every distinct two-bit phase permutation, every odd F table and two representatives each of graph and mate sign parity. The separate factors are **not** asserted to be a single common enumerated Y, and the symbolic global mate weights do not count executed full-Y objects.

The following is a self-contained conditional reconstruction of what this source is intended to corroborate; it is written mathematics, not observed machine output.

## 1. One-row identity and physical phase action

All vectors and covectors are two-bit vectors; write `Q(a0,a1)=(a1,a0)`, `q(b)=b0*b1`, `chi_alpha(b)=(-1)^alpha(b)`, and add/XOR in `F2`. In graph row `i`, let `S_i(b)=X(1,F_i,i,b)` be a sign, let `d_i(b)` be the sign of the D0 mate divided by 2 at its `k_i` occupied b positions and zero elsewhere, and set

`P_i = XOR{b : S_i(b)=-1}`, `B_i = XOR{b : d_i(b)!=0}`, `B_D = XOR_i B_i`.

Row-zero is `sum_b S_i(b)+2 sum_b d_i(b)=0`. Let `n_i` be the number of negative `S_i`. Then `sum d_i=n_i-2`, so `n_i` and `k_i` have the same parity. Hence if `k_i` is even, `S_i` is a signed affine character `sigma_i chi_xi_i` (the constant character is allowed), with `xi_i=Q P_i`. If `k_i` is odd it is a signed 3:1 row: `S_i=sigma_i (-1)^(q+nu_i)` with `nu_i=(1,1)+Q P_i`. These statements include all `k=0,1,2,3,4`; the negative support can be the singleton or its three-point complement.

For any nonzero `alpha`, the graph quotient is

`4 Z_(1,i)(s,alpha) = (-1)^(s F_i) [sum_b S_i(b) chi_alpha(b) + 2(-1)^s sum_b d_i(b) chi_alpha(b)]`.

It is an integer multiple of 4: compared to `alpha=0`, each character flips either zero or two graph signs, while the mate part changes by a multiple of four. Reducing the quotient modulo 2 using row-zero gives the **exact local identity**

`Z_(1,i)(s,alpha) = 1 + s k_i + alpha(P_i+B_i) (mod 2)`.

The sign `(-1)^(sF_i)` does not change parity. A valid nonzero same-X profile is either a singleton `+/-2` or four `+/-1` entries on an affine two-flat. Its graph-plane intersection has 0, 2 or 4 entries, so the sum of its graph entries is even; in the singleton case it is also even. Summing the displayed identity over the four rows, and using even `sum k_i=4-d`, gives `alpha(sum_i P_i+B_D)=0` for every nonzero alpha. Therefore

`sum_i P_i = B_D`.  (The `s=0` equations alone already give this; the even total ensures the same expression for `s=1`.)

This is only a necessary projection of the seven actual profiles: it does not imply their full affine-flat support, product-minus-one, or a common E-side completion.

Under the imported actual `Y=-agX` graph phase, the four row covectors `lambda_i` are distinct and have XOR zero. Row constants are absorbed in signs. For even `k_i`, the Y graph row is bent with covector `theta_i=lambda_i+Q P_i`. For odd `k_i`, the two quadratic terms cancel and the Y graph row is an affine character with covector `kappa_i=lambda_i+(1,1)+Q P_i`. The number of odd `k_i` is even; consequently

`sum_even theta_i + sum_odd kappa_i = Q B_D`.  (1)

No equality of the odd-row offsets, no special occupancy, and no freedom to choose the physical covectors on a given object is used.

## 2. Uniform slice by an exact sign-product factorization

Let `A_ell(s,alpha,beta)` be the physical `(h,i,b)` partial Walsh transform of the same Y. For each `(s,alpha,beta)`, an even-k graph row has Walsh magnitude 2; an odd-k graph row contributes a signed 4 exactly at `alpha=kappa_i`, and zero elsewhere. Each D3 mate contributes a signed 2. Put `N=(12+d)+#even_rows`; both terms on the right have the same parity, so `N` is even. In `A_1/4`, the N magnitude-two terms are an integer half-sum. For N signs their half-sum is `N/2 + number_of_negative_signs (mod 2)`, so its parity is controlled by their **product**. The odd-row magnitude-four terms contribute

`m_alpha = #{odd i : kappa_i=alpha} (mod 2)`.

For every physical row, the XOR of its surviving D3 b-positions equals the XOR of its D0 positions, because the XOR of all four b values is zero. Thus the mate product's alpha exponent is `alpha(B_D)`; its sign dependence is only the parity of the negative mate signs. The beta exponent of the product is

`beta(sum_even i + sum_i (4-k_i)i) = beta(sum_i i) = 0`,

and its s exponent is

`s [sum_even F_i + sum_i (4-k_i)(1+F_i)] = s sum_i F_i = s`.

The equalities are in `F2`: each row appears once in the beta coefficient, `#odd_rows` is even, and the actual F table has odd parity. In the bent-Walsh product the `q(alpha)` terms cancel because `#even_rows` is even; the remaining alpha slope is `Q sum_even theta_i`. Therefore for an object-dependent constant `c`, including `N/2`, the actual graph row signs and the actual negative-mate parity,

`A_1(s,alpha,beta)/4 = c+s+m_alpha+alpha(v) (mod 2)`,

`v=B_D+Q sum_even theta_i`, `sum_odd kappa_i=Qv`.  (2)

The support of `m` has size 0, 2 or 4: its parity is the number of odd rows. Its support XOR is `Qv`. For size 0 or 4, `v=0` and `m` is constant. For size 2, `v!=0`; the two support points differ by `Qv` and therefore have the same `alpha(v)`, so they form one affine line on the four-point dual. Its indicator has slope `v`. Thus `m_alpha+alpha(v)` is constant on all four alpha, **including alpha=0**. Equation (2) gives one entire even and one entire odd `s`-slice of `A_1/4`, for every `d=0,2,4` and every graph occupancy satisfying the imports. This proof does not assume that all four Y graph rows are affine or that the mate signs can be chosen independently of a physical object.

## 3. Exact two-E count and physical Z4 gap

For `d=2`, the actual ell-one Y energy is `16+14*4=72`. Common residue `4 mod 8`, cap 12 and total energy 128 imply that each of the 64 full coefficients has magnitude 4 or 12, with exactly eight magnitude-4 coefficients: `16 N4+144(64-N4)=64*128`, so `N4=8`. The two full coefficients over a partial frequency are `A_0 +/- A_1`; the two caps are exactly `|A_0|+|A_1|<=12`, and `A_0/4,A_1/4` have opposite parity.

Let `n` be the number of even-slice `|A_1|=8` pairs and `m` the number of odd-slice `|A_1|=4` pairs. The other values have magnitudes respectively 0 and 12. Partial Parseval yields `4n+m+9(16-m)=144`, hence `n=2m`. If `h` counts odd-slice 4-pairs with `A_0=0` and `z` counts even-slice zero-pairs with `|A_0|=4`, exact counting of all eight small full coefficients gives `8=3m+h+2z`, `0<=h<=m`. Including `0<=z<=16-n`, the only integer solutions `(n,m,h,z)` are `(0,0,0,4)`, `(2,1,1,2)`, `(4,2,0,1)` and `(4,2,2,0)`. Therefore the entire odd slice has at most two nonzero `A_0`, each of magnitude 8.

The actual 16-point inverse in `(alpha,beta)` bounds every `|Y(0,0,i,b)+(-1)^s Y(0,1,i,b)|` on this same odd slice by `2*8/16=1`. At the unique physical Z4, `b!=0`; its opposite-h site at the **same** `(i,b)` is another Z site of magnitude at most 2. The corresponding sum or difference has magnitude at least `4-2=2`, a contradiction. This is conditional on the physical Z classification and same-object imports, not on free spectral arrays. The source's inverse and pair checks verify the integer gap only; they do not reconstruct that physical classification. Neither the even-E common-slice calculation nor this finite source proves a broader rank-two union by itself.

## 4. Exact intended program coverage and controls

* `one_row`: all four b positions; every D0 subset, every sign on that subset and every graph sign row satisfying row-zero. It checks the negative XOR, character/3:1 form, both s and all three nonzero alpha quotient parities, and all four lambda and four alpha physical graph-phase/Walsh cases. The expected unweighted row counts, derived combinatorially rather than observed in a run, are `k=0:6, 1:32, 2:84, 3:96, 4:44`; total 262. They are not hard-coded as a supposed observed receipt.
* `weighted_graph_projection`: dynamic programming counts **actual local row assignments** by `P_i XOR B_i`, separately for all ordered `sum k=4,2,0` occupancies. The `even_support_weighted` count is the multiplicity of row assignments whose XOR is zero. It is a necessary-profile relaxation, not a count of actual seven-profile X arrays, physical f/R, or callers. Weights count mathematically compressed assignments, not separately executed array visits.
* `slope_quotient`: every even odd-row mask, all 256 four-row `P` tuples and all 24 distinct lambda permutations. Its nominal 49,152 quotient states are an algebraic **superset**, not 49,152 physical examples. It checks (1), `sum kappa=Qv`, support XOR, all 0/2/4 support sizes and the full alpha slope, plus the bent quadratic factor. No nmate assignment is conflated with this abstract count.
* `mate_factor`: every D0 subset of a local four-position row and every D3 sign assignment, all four alpha and both external row signs, including complement XOR. The weight `2^(nmate-1)` for each global negative-sign parity class at `nmate=12,14,16` is **symbolic**, justified by flipping any one mate sign, not a claim to have enumerated those global assignments. `physical_row_geometry` separately checks every eligible ordered occupancy, odd F, beta and s exponent.
* `direct_factorized_representatives`: one actual row-zero graph/mate assignment selected from each **nonempty parity-projection occupancy**, then all 24 phase permutations, all eight odd F tables, a baseline/one graph-sign-flip and a baseline/one mate-sign-flip, on every `s,alpha,beta` cell. These direct checks explicitly include all available 12-, 14-, and 16-mate groups, but only representative X rows and two sign representatives. The algebraic and local product factors, not an unexecuted claim of full-Y enumeration, explain how the general sign dependence factors.
* `integer_census_and_inverse`: all 16 ordered pairs of possible full coefficients; the complete four integer solutions above; the two-nonzero/16-point upper bound; and both signs of an actual-Z4/mate magnitude relaxation. The Z4 location and mate classification are imported, not generated.
* `targeted_mutants`: row-zero, negative XOR, physical phase, mate XOR, slope identity, odd F, slice nonuniformity, failure to switch slices, energy, small count, nonzero-b Z4, Z-mate bound and inverse gap are each required to raise their **named** `Rejection` reason. Acceptance, the wrong reason or an unrelated exception is not counted as detection. The mutants are synthetic controls, not counterexamples to physical realizability.

The source checks a 38-second monotonic deadline throughout the potentially large loops. JSON lists only stages completed before a timeout and, during the direct representative stage, exact completed representative/cell progress; an in-progress earlier stage is not reported as complete. If complete, its counters must be read as the scope labels above say, rather than as executions of the weighted Cartesian product. No former source code was read or imported.

## 5. Exposure, controls, frozen-source coverage and boundaries

Before any packet body or mathematics I read the complete manifest, actual dispatch receipt, freeze receipt, final binding, parent live metadata and all 22 manifest-listed controls through their endings. Controls were used solely for status/permissions. I sent Main a **direct PREBODY ACK** naming each exact control, the ordered packet and its LF count, and stating no body or mathematics had been read/done. Only after that ACK I read the sole packet part serially in `:raw` windows `1-20,21-40,...,701-720,721-726`, including every long line and its ending, before research or comparison. Administrative-file internal ordering was not required. The sole part is `literal-packet-part-01-v1.md`, 726 LF, with **parent-supplied**, not independently rehashed, SHA-256 `dda72dbf247a007ac66964ecb62625c370fc62d9aa16f10b7fb6483335450d3c`. The manifest SHA supplied by the actual receipt is `19c2b2a855571cd384eacfc1af007d2d5ef7ad848692b88a9e48d2f12897165a`; those are byte-binding assertions from parent metadata, not a claim of independent source-identity verification.

The nine packet bodies were complete and read to their endings: S1 uniform candidate (25 LF), S2 even-E/census disposition (52), S3 local-H/general-g foundation (13), S4 all-graph disposition (29), S5 four-E disposition (31), S6 split-graph disposition (17), S7 double-graph author candidate (200), S8 split-graph author candidate (179), and S9 f803 parent finite-run receipt (142). Their full paths and hashes are those in the complete `manifest-v1.json`, not newly verified direct-source hashes. S9 is a prior reported local run at its own scope, **not** a run of this source or a full-Y enumeration. The source was newly written from the packet interface, without old code, outgoing links, held episode or held consumer input. All held episodes and **all** their consumers remain NONINPUT; this is nonblind same-harness general-author work and no cognitive-isolation certification is made.

No d=0 all-graph or d=4 written obstruction is newly audited/adopted here; they remain their own named imported dispositions and exact interfaces. The general common-slice reconstruction and d=2 gap require independent review of every physical import and of this source before any promotion or named union. In particular, no full caller, V, original-source identity, all-rank-two/five-span, NL242, novelty, independent-family, human, kernel or parent-adoption result is claimed. Corrections, if any, must be additive new files or a new complete immutable successor; these initial bytes are not to be edited or overwritten.
