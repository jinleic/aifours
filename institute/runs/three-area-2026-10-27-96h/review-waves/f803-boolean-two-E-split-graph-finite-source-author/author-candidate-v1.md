# F803 — split-graph parity interface, independent finite-source proposal

**Status:** fresh nonblind same-harness GENERAL AUTHOR work; **SOURCE PREPARED, UNRUN, NO GO, NOT VERIFIED, NOT PARENT-ADOPTED.** UTC clock observed before this exclusive creation: `2026-10-31T01:32:19.714344+00:00`. This is a factorized necessary-interface checker proposal plus a written conditional reduction. Its expected counts and control reasons below are design claims, **not observed output**. Parent must whole-read the exact source and separately decide whether to GO; no automatic acceptance, caller, family, human, kernel, source-identity or novelty assurance follows.

## 1. Frozen target and named imports

Fix one actual normalized rank-two five-span object at the packet's local `H_loc=0`/count interface, with one common physical `f/R,a,g,u,x=U0,y=U3`, inverse, graph and specified original-DC transported character `t`. Only for analysis put `X=(-1)^t x`, `Y=(-1)^t y`; do not select a new `t`, phase, inverse, spectrum or Y. The physical coordinates are `(ell,h,i,b)` with `ell,h` bits and `i,b` in `F_2^2`. The graph at row i is `ell=1,h=F_i`, and its physical **same-b** mate is `h=1+F_i`; `XOR_i F_i=1`.

The branch is exactly two E-site D0 (`d_E=2`) and two graph-mate D0 in **different graph rows**. There are 15 physically distinct pairs of E D0 positions: three with both in one E row and twelve in different E rows. The graph mates are distinct as physical points because their graph rows differ; **their b-coordinates may coincide**. The other graph rows have no D0 mates. Actual imports from packet S1/S4/S6/S7 are: the same-X zero-flat and all seven profile conditions; graph signs ±1; graph D0 and E D0 and Z2 have |X|=2; the remaining D3/Z0/Z4 and two full sites have X=0; physical graph relation `Y=-agX` with q(b)=b0 b1 and the four distinct row covectors `rho_i`; one common Y, J=1, all 64 U3 coefficients congruent to 4 mod 8 and capped by 12; spatial Y energy 128; the actual Z4 is at `ell=0,b!=0` and its opposite-h site at the **same** `(i,b)` is a Z of magnitude 0 or 2. The graph half has spatial Y energy `16+14*4=72`. The source does not independently prove these imports or construct the inverse, a common physical Y, or the original caller.

## 2. What the finite source is designed to check

Exclusive source: `finite-split-graph-parity-v1.py`; 22,232 bytes, 526 LF, SHA-256 `a3d16e362fce48806751940e68045ea84f6e7aca0f1c5b54fbc9aa34a4e49566`. This digest is computed from the bytes supplied to the exclusive creation, not an executed or independently reviewed result. Standard-library only; no input files, network or child processes. It writes its structured result only to stdout. A 300-second cooperative deadline makes the run `INCOMPLETE_DEADLINE`, not PASS. A false guard produces `FAILED_CHECK` with reason; unexpected exceptions produce `INCOMPLETE_EXCEPTION`; guards do not rely on Python `assert`. The deadline is a designed bound, not an observed runtime or substitute for parent resource supervision.

1. It generates all 8 odd F tables, all 6 pairs of physical graph rows, every signed 3:1 graph row (8 signs/rows), each of the 4 b-positions per occupied row and the required mate sign, and each signed nonzero character in the other two rows (6 per row). This is intended to cover `8*6*(8*4)^2*6^2 = 1,769,472` cases, 36,864 per F/row-pair; the counts are guards, not measured runs. It separately checks all 15 actual E position pairs and retains both E occupancy shapes. The cross-row equal-b case is specifically allowed and counted; it is not treated as a collision.
2. The full mathematical profile alternatives are generated as the 16 signed singletons and 112 four-entry affine planes with negative sign product on the eight `(ell,i)` sites. Every graph projection is checked against that generated set, including a graph-full-plane sign check, and the abstract projection characterization is independently compared on all `{-1,0,1}^4` graph vectors. For every one of the **same graph rows'** six nonzero-alpha slices, it checks the parity and the L=0/1/2 slice-count alternatives; lambda has the two graph entries. This is a necessary projection test: the E completions are generated **column by column**, and no claim is made that one common ell-zero X realizes all seven, or that all surviving graph rows are physical callers. E-side singleton profiles remain included.
3. It checks the row-support/parity identity from all graph placements and verifies the physical phase link over all 24 assignments of the distinct `rho_i`, all 6 row pairs, `nu` in `F_2^2`, nonzero theta in `F_2^2`, and both actual mate positions. It separately checks direct affine/bent Walsh transforms, all three-supported D3-mate sign rows at each missing position, and all four-supported D3-mate sign rows. No arbitrary missing virtual site replaces an actual mate.
4. The mixed-Y residue check is factored. After proving that all physical parameter choices obey the same XOR link, it ranges independently over the four affine/bent covectors, the two product-sign bits and one unoccupied-mate residue bit, all odd F and row placements, and all `(s,alpha,beta)`; this deliberately includes a relaxation, not fewer physical cases. It computes the partial graph expression directly and compares its residue with the paired-product formula and the slice-switch rule. The individual occupied mate locations enter through their XOR; the preceding physical-link and local-mate checks cover every individual pair and the mod-4 reduction. The source's intended static bound is 98,304 factor cases and 3,145,728 partial-frequency cells. These are not full-Y or all-mate-array enumerations.
5. It generates all 16 ordered full coefficient pairs from `{-12,-4,4,12}`, derives the six absolute `(A1,A0,small)` types, and checks the energy-72/eight-small integer possibilities stated below. It includes intended-reason controls for F parity, graph-row distinctness, signed 3:1, mate sign and position, nonzero other-row character, physical E position, profile support/geometry/sign, parity link, mixed-Y uniformity and slice switch, energy and small-count failures. The equal-b distinct-mate case, both E occupancy shapes, and an E singleton are positive controls. Mutants are synthetic, not claimed to be actual physical objects.

No scientific child execution, compilation, test, solver, external CLI, old code, external source, network, Git operation, installation or deletion was used for this source. Its finite scope is **necessary projection and residue/census only**; it does not enumerate one common ell-zero X, complete Y, U3-capped callers, or physical inverse/ternarity.

## 3. Conditional mathematical bridge for scrutiny

Let the occupied rows be `a,a'`, and the other rows `b,b'`. Their physical two-bit row labels satisfy `Delta=a XOR a'=b XOR b' != 0`. On each occupied row, zero-flat forces a signed 3:1 graph and a D0 mate of value `2 epsilon_i` at its actual `z_i`; the graph is `sigma_i(-1)^(q(b)+nu_i·b)`. On an unoccupied row zero-flat makes the graph a signed nonconstant character `theta_i`. For the occupied row, direct four-point transform gives a unique nonzero s slice for each alpha:

` s_i(alpha) = 1 + q(alpha) + alpha·(J nu_i + z_i)`,

where `J` swaps the two bits. In each nonzero-alpha column let `L(alpha)` count how many of the two other rows have character alpha. A profile plane has 0, 2 or 4 graph entries; the graph rows here never supply a singleton of magnitude 2. Consequently both slice counts are even, equivalent to

` s_a(alpha)+s_a'(alpha) = 1_[alpha=theta_b]+1_[alpha=theta_b'] (mod 2)`.

The right side is the linear functional `alpha·J(theta_b+theta_b')`, including the equal-theta case. Hence this one common graph dataset satisfies the necessary identity

` z_a+z_a' + J(nu_a+nu_a'+theta_b+theta_b') = 0`.  (1)

A positive four-graph sign product is also disallowed; the source checks it separately, rather than equating parity with complete simultaneous profile realizability. The E-side singleton/plane possibilities when there are zero graph entries remain genuine alternatives. The source does not infer that admissible projected columns can be joined into one ell-zero X.

Under the actual graph phase import, the occupied graph Y rows are affine with covectors `phi_i=rho_i+nu_i`; the other graph Y rows are bent with covectors `mu_i=rho_i+theta_i`. The four distinct rho values XOR to zero. Thus (1) is the cancellation of the alpha coefficient in

` z_a+z_a' + J(phi_a+phi_a'+mu_b+mu_b')`.

For each occupied physical graph mate, `D_i=Y_mate/2` vanishes at `z_i` and is ±1 at the other three b values. Its Walsh sum is `d_i(-1)^(alpha·z_i) mod 4`, with `d_i=±1`. Each unoccupied mate has four ±1 values and its Walsh sum is independent of alpha modulo 4 and insensitive to an overall sign. The actual graph Fourier pieces are ±4 delta functions for the affine rows and ±2 bent signs for the other rows. Consequently, for the same partial transform `A1(s,alpha,beta)`, writing `R_b,R_b'` for the signed bent terms and `T_a,T_a'` for the occupied-mate residue terms, the proposed direct identity is

` A1/4 = k + 1_[alpha=phi_a]+1_[alpha=phi_a'] + (1+R_b R_b')/2 + (1+T_a T_a')/2 (mod 2)`,

where k is alpha/beta/s independent. The two beta coefficients cancel because the two **physical** row pairs have the same Delta. The s coefficient is `XOR_i F_i=1`. The delta pair is affine in alpha with linear part `J(phi_a+phi_a')`; the remaining alpha terms cancel by (1). Thus the written conditional consequence is `A1/4 = c+s (mod 2)` for every alpha and beta. The source is designed to corroborate this factorization if later admitted; no run result is claimed here.

## 4. Energy 72 and the actual-Z4 boundary

With all full coefficients congruent to 4 mod 8 and capped by 12, their magnitudes are 4 or 12. Parseval at total spatial energy 128 forces exactly eight magnitude-4 full coefficients. Let `n` count `|A1|=8` in the even-parity s slice and `m` count `|A1|=4` in the odd slice, each having 16 partial frequencies. Partial Parseval at ell-one energy 72 gives `4n+m+9(16-m)=144`, hence `n=2m`. Each of the n+m pairs supplies at least one small full coefficient, so `3m<=8`. With H the number of odd-slice |A1|=4 pairs with A0=0, and Z4 the number of even-slice A1=0 pairs with |A0|=4, the exact small-count equation is `8=n+m+H+2Z4`. The only written solutions `(n,m,H,Z4)` are `(0,0,0,4)`, `(2,1,1,2)`, `(4,2,0,1)`, `(4,2,2,0)`.

Hence on the odd slice the actual common `A0` has at most `m-H<=2` nonzero coefficients, all of magnitude 8. The fixed-slice 16-point inverse then bounds `|Y(0,0,i,b)+(-1)^s Y(0,1,i,b)| <= 1`. At the actual Z4 its same-`(i,b)` opposite-h partner is another Z of magnitude 0 or 2, giving magnitude at least 2. This is a **conditional written contradiction** only if every listed same-object, physical phase, profile, residue/cap/energy and Z4 imports is separately established. The proposed source does not check the actual ell-zero Y, Z4 partner, Walsh inversion, full caps or any common Y. Neither this author return nor a prospective local finite PASS is a parent disposition or a full original-caller/global proof.

## 5. Exact open boundaries

* Parent static whole-read, disjoint scrutiny and separate GO are unpaid. This source has not been run; no control outcome, runtime, finite PASS or failure is observed.
* The column projections and free phi/mu residue family are necessary relaxations; common ell-zero simultaneous profiles and common physical Y are not enumerated. No positive witness is constructed.
* The local actual-g/phase, original-DC transport, physical inverse/ternarity, residue/J bridge, U3 caps, same-b Z4 partner and Walsh inversion remain imports here. A parent must explicitly assess those boundaries; S1 is unadopted, and S6/S7 retain only their actual recorded scopes.
* This is only d_E=2 with graph occupancy 1+1. Graph occupancy 2, remaining d_E=0 cases, V, selected-T/rank/eight-zero lifting and global rank-two/five-span/NL242 are not settled. No blind, independent-family, human, kernel, original-source-identity or novelty claim is made.

## 6. Packet, controls and process coverage

After Main's direct actual-receipt notice, before any packet body, I read actual `dispatch-receipt-v1.json`, complete `manifest-v1.json`, `freeze-receipt-v1.json`, `final-pre-dispatch-binding-v1.json` and `parent-live-metadata-supply-v1.json` through their endings. I read all **22** manifest-listed status/permission controls through endings: prospective-author method restoration; contract addendum 2; parent L1, privacy, core-gram, AME-compression, PH-registration quarantine controls; f439, f444, f448, f508, f513, f586, f602, f596, f653, f654, f659, f660 and f662 quarantine controls; the parent remaining-D0 E-row omission and prerun f746/f749 design-correction controls. They are status/permission only. All genuinely held episodes and ALL proof/method/selection/planning/verification/reporting/confidence/downstream consumers remain NONINPUT. I sent Main a direct PREBODY ACK naming those controls and the ordered part count before body access.

There was one part, `literal-packet-part-01-v1.md`, manifest-supplied SHA-256 `cb27c6e8096055247d931057fb778465a7f7a354dcd009c723c649f44d230de9`, **907 LF**. It was then read serially RAW in windows `1–20, 21–40, …, 881–900, 901–907`, through its ending and complete long lines before mathematical work. All S1–S10 complete bodies were included. Manifest-supplied source pins/counts, not independently rehashed here:

| Source | Complete body | LF | SHA-256 |
|---|---|---:|---|
| S1 | f788 author candidate | 179 | `1c51df762a1878cae342b32b4a34fead49ca39c2813bdab41ba3e7a9ed3b737d` |
| S2 | f748 E-singleton gap | 7 | `79a618853b07f6e9dd30bc16592cb378a861c6b625cc7e3171e0a2779c2f0dca` |
| S3 | f753 quotient erratum | 9 | `90c4242e118be887f19b61ccba23f4af0c6062516142962b9a315557c0e03606` |
| S4 | f753 author candidate | 121 | `e4e1c4a1812a03d0334dbee16dec50650d6a904e0e68b75dbcddae22e73aefa8` |
| S5 | f754 additive clarification | 15 | `4dddaf7084e784b8c8d2b51b857320a26438a6a669b1ad9dee2f8d19268c4114` |
| S6 | E-row parity/census parent disposition | 52 | `f1dec4722410e8db8e55c4a66a4da1d3b23d542b49b672049ed6d80373bd26d2` |
| S7 | four-E obstruction parent disposition | 31 | `4e3ef5738027dbb107d1f50d2d2b24c87afa0a54440a22a1fe3ebed0474707f5` |
| S8 | f755 parent local-profile run receipt | 256 | `d3cdcca328bf4c902c214ddbb9b5d42fccb41f56406147681c3baf2880f5aaf1` |
| S9 | f778 parent one-shot run receipt | 182 | `72ce3e26ffc187528890a9d0a808066ceb13b5d6fb9040644cf82f60b9871d08` |
| S10 | recovered local-H/general-g foundation | 13 | `a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef` |

No linked source, old checker code, sibling result or held payload was opened. The parent-reported prior S8/S9 runs have only their own stated scopes; they are not executions or verification of this source. This record does not assert unseen cognition or retrospective permission.
