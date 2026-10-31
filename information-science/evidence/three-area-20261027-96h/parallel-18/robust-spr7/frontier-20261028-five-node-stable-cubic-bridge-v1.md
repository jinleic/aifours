# Five-frequency actual-box obstructions force a common Hurwitz cubic and three phase words

Owner **InfoSPR7-2**, slot info-2. Actual preceding `/bin/date`: **Wed Oct 28 18:02:48 PDT 2026**. **WRITTEN candidate with the explicitly named finite symbolic table checked in the owner's Eval kernel; not independently reviewed or adopted.** This constrains the previously remaining five-positive-frequency, two-endpoint branch. It does not prove such an annihilator exists or excludes every original box.

## 1. Scope and exact assertion

Import the COMPLETE all-variable `frontier-20261028-five-frequency-single-endpoint-exclusion-v1.md`, SHA256 `e8aae88916a5275f0cbe4fe057dd6bcc2eea809f6ab1d3f8bb5a897d2db23f2a`, including its actual-member frequency merging, six strictly separated root bands, phase-class ordering, zero/infinity signs and exact Vandermonde moment equations. That source is an unreviewed candidate; this successor does not claim parent adoption or use an old held proof.

Fix ANY actual original independent closed monic septic box K with EVERY member strictly Hurwitz. Suppose an actual positive annihilator has exactly five distinct positive finite squared frequencies `0<t_1<...<t_5`. The imported theorem forces BOTH endpoint atoms. Merge all same-frequency denominators into their positive-weight actual-box averages a_j; let `mu_j>0`, `eta0>0`, `etaI>0`, and let `H(t)=product_(j=1..5)(t-t_j)`. Define `A=-eta0 H(0)>0`.

**Theorem.** There are real alpha,beta such that the exact moment equations force

`alpha>0`, `beta<0`, `alpha*(-beta)>etaI*A`,

and the SAME real cubic

`c(s)=etaI*s^3+alpha*s^2-beta*s+A`

is strictly Hurwitz. At EVERY selected positive frequency,

`a_j(i sqrt(t_j)) / c(i sqrt(t_j)) = -1/[mu_j t_j H'(t_j)]`.

The right side is real and its signs in increasing j are exactly `(-,+,-,+,-)`. This identity concerns the ACTUAL averaged a_j of ONE K; c is a derived cubic comparator, not a claimed original numerator, member of K, or new lower-degree solution.

Put `tauE=A/alpha` and `tauO=(-beta)/etaI`. Then `0<tauE<tauO`; these are the positive roots of the even and odd parts of c, respectively. At most three generic phase words remain, listed in §3. In each, tauE lies in an actual O-root band of K and tauO lies in a later actual E-root band. No claim is made that any of these necessary patterns is realizable.

## 2. Full moment solution and monotone thresholds

Because m=5, `H(0)<0`, and the signs of `1/H'(t_j)` are `(+,-,+,-,+)`. The exact moment equations from the imported source have ALL solutions

`mu_j E_j=(alpha-A/t_j)/H'(t_j)`,
`mu_j t_j O_j=(beta+etaI*t_j)/H'(t_j)`,

where E_j,O_j are the actual averaged member's even/odd evaluations. Indeed `1/H'(t_j)` spans the one-dimensional nullspace of the four-row Vandermonde; the zero-endpoint particular solution follows from `sum 1/(t_j H'(t_j))=-1/H(0)`, and the infinity particular solution from `sum t_j^4/H'(t_j)=1`. Both numerator factors are strictly increasing functions of t>0.

At a node where one factor is zero, the corresponding E or O part is zero but the other is nonzero, since that actual a_j is Hurwitz. In the phase table assign the zero either adjacent sign/class, in a way consistent with the relevant increasing threshold; both choices are legitimate boundary classes. The two factors cannot simultaneously vanish at an actual node.

Let pE be the number of initial nodes assigned the negative sign for `alpha-A/t`; let pO be the number assigned negative for `beta+etaI*t`. Each is one of 0,...,5. With `s_j=sign(1/H'(t_j))=(+,-,+,-,+)`, the assigned E/O signs are `(s_j * sign_E(j), s_j * sign_O(j))`.

## 3. Exact necessary phase words and band locations

For actual denominators the possible phase classes q and E/O signs are

`q:  0   1   2   3   4   5   6`
`EO: ++  -+  --  +-  ++  -+  --`,

and the imported source proves `q_i<=q_j+1` for every i<j. The following table is the COMPLETE list that satisfies that necessary pairwise ordering, all monotone threshold placements, and the five derivative signs:

| pE | pO | E/O signs at nodes 1..5 | q_1,...,q_5 | band containing tauE | band containing tauO |
|---:|---:|---|---|---|---|
| 1 | 3 | `--, -+, +-, --, ++` | `2,1,3,2,4` | O-root 1 | E-root 2 |
| 1 | 4 | `--, -+, +-, -+, ++` | `2,1,3,5,4` | O-root 1 | E-root 3 |
| 2 | 4 | `--, ++, +-, -+, ++` | `2,4,3,5,4` | O-root 2 | E-root 3 |

For an exact finite check, `frontier-20261028-five-node-phase-words-kernel-v1.py`, SHA256 `1b1e5acd937098b7491e453efd81d827c1c795f4379780e47bef1a805ef88984`, was loaded in the Python Eval kernel. It iterates the 36 abstract `(pE,pO)` pairs, lists each node's at most two q values consistent with its symbolic signs, and retains a word iff every `q_i<=q_j+1` for i<j. The observed output is exactly the three rows above and no others. This finite combinatorial enumeration contains no numerical frequency, polynomial, box, solver, or floating-point arithmetic. It supplies only a NECESSARY phase classification; the pairwise ordering is not claimed sufficient for realizing actual denominators.

The band columns follow without enumeration: for example, in the first row `q_1=2`, `q_2=1`, and `t_1<t_2`, so both frequencies lie in the common first O-root band. Since pE=1, `tauE in [t_1,t_2]`, including a possible node equality, and hence tauE lies in that band. Likewise `q_3=3`, `q_4=2` put tauO in the second E-root band. The other rows use the same backward-one phase transitions: `(q_1,q_2)=(2,1)` for O1 or `(q_2,q_3)=(4,3)` for O2, and `(q_4,q_5)=(5,4)` for E3. The six actual bands are strictly ordered as proved in the predecessor.

Every surviving pE is 1 or 2 and every pO is 3 or 4, with pE<pO. Therefore each strictly increasing factor takes both signs across the five nodes. In particular alpha>0 and beta<0. Also `tauE in [t_1,t_3]`, `tauO in [t_3,t_5]`, and the particular table placements give **strictly** `tauE<tauO`, even if one threshold equals a node. Multiplying `A/alpha < (-beta)/etaI` by positive alpha*etaI gives `alpha*(-beta)>etaI*A`.

## 4. Derivation and stability of the common cubic

The cubic `c(s)=etaI s^3+alpha s^2-beta s+A` has all coefficients positive and its cubic Routh–Hurwitz determinant is `alpha*(-beta)-etaI*A>0`. The ordinary exact cubic Routh–Hurwitz criterion therefore proves every root of c lies in the open left half-plane. Its even part at t is `A-alpha*t`, and its odd part is `-beta-etaI*t`; their positive roots are tauE and tauO as stated.

The moment equations give

`E_j=(alpha*t_j-A)/[mu_j t_j H'(t_j)]`,
`O_j=(beta+etaI*t_j)/[mu_j t_j H'(t_j)]`.

These equalities hold even if one numerator vanishes. Hence

`a_j(i sqrt(t_j)) = -c(i sqrt(t_j))/[mu_j t_j H'(t_j)]`.

Since c is strictly Hurwitz, its value is never zero on the imaginary axis, including all five nodes. The ratio is therefore exactly the displayed real scalar, with signs `(-,+,-,+,-)`. This supplies one **common, explicitly derived Hurwitz cubic** linking all five actual denominators and all five nodes; it is not five independently chosen comparators.

## 5. Remaining original implication and assurance

An actual five-frequency certificate would have to realize BOTH endpoint atoms, one of the three phase/band words, the positive weights, the full shared-coefficient cancellations, and the common Hurwitz-cubic alternating-ray identity inside the SAME robustly Hurwitz coefficient box. It remains unproved whether ANY of these coupled patterns is realizable, or whether the common cubic and independent-box intervals rule them all out. Six or more positive frequencies remain outside this five-node result. Neither a free phase word nor a freely chosen stable cubic is an original obstruction.

The written algebra and exact 36-case symbolic kernel need full independent review together with the named complete predecessor and its root-band/moment interfaces. No original zero-certificate box, universal positive sign, finite numerical witness, optimal value, novelty, formal/kernel/human/configured-family acceptance or retrospective process clearance follows. No scientific subprocess, floating arithmetic, selected box/frequency, solver, external model, nested agent, Git action, deletion or publication was used in this derivation.

**END.**
