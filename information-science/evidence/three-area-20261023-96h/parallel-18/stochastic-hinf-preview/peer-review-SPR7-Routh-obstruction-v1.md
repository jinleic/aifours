# In-harness reconstruction: full-width septic Routh-hull obstruction

Reviewer: **InfoHinfPreview**, info-3. Observed review clock **2026-10-23T14:18:54-0700**, `/bin/date '+%Y-%m-%dT%H:%M:%S%z'`. Assigned by `peer-review-wave-eighteen-v1.json`. Ordinary separate-agent written reconstruction with supplied proof, not a blind, cross-vendor, human or formal review. No scientific executable, numerical assay, CLI or nested agent was used.

## Snapshot and verdict

Read the entire author manuscript, its exact `selection-v1.md`, definitions and source/dependency boundary. Actual observed SHA256 of

`information-science/evidence/three-area-20261023-96h/parallel-18/robust-spr7/routh-obstruction-candidate-v1.md`

is **`47953be4805c2838a93204d077e71d2332e3468c09dc69fb973fba6563058cac`**, exactly the parent's assigned pin.

**No FATAL, MAJOR or MINOR mathematical defect found at the stated scope.** The all-parameter full-seven-width robust-Hurwitz box, explicit common numerator, uniform whole-frequency positivity, and unstable member of the normalized Routh-image coefficient hull reconstruct correctly. This establishes only the failure of the stated naive independent-hull induction. It neither disproves nor proves universal degree-seven SPR synthesis, and the generic failure of intervalized Routh reduction is prior art.

## Independent reconstruction of the load-bearing steps

### A. Pointwise stability and the actual reduction (lines27–41,53–106)

Expanding `-(t-1)(t-3)(t-6+d)+u` gives exactly

`-t^3+(10-d)t^2-(27-4d)t+18-3d+u`.

At `t=0,2,4,6` its signs are `+,-,+,-` throughout `0<d<=1/10`, `0<=u<=10d`: the endpoint bounds are `-4+11d<0`, `6-3d+u>0`, and `-15d+u<=-5d<0`. Thus there are exactly three simple even roots, respectively in `(0,2),(2,4),(4,6)`, interlacing the fixed odd roots. This is the stated degree-seven Hermite–Biehler import with the correct orientation.

For a general monic Hurwitz septic with `[s^6]p=c>0`, `O-E/c` cancels its cubic term and has signs `+,-,+` at the three even roots. It consequently has exactly two simple intervening roots and positive leading coefficient; both are positive, so its constant is also positive. The degree-six Hermite–Biehler order is correct after division by positive `c`. This checks that instability is not already present in an actual pointwise reduction.

For the base family `c=1`, direct substitution gives precisely the displayed sextic(3). Its correlated last coefficients sum to48. The proposed bad hull member takes its linear coefficient at `u=10d` and constant at `u=0`. At the largest even root `r=6-d`, its odd component is

`d((4-d)(2-d)-10)=d(-2-6d+d^2)<-2d<0`,

where a Hurwitz sextic requires positivity. At the other even roots it is `15-10d>0` and `-3-10d<0`. Thus there is no simultaneous even/odd zero, no zero at the origin, and the unstable root cannot be dismissed as an imaginary-axis ambiguity. Positive coefficients rule out positive real roots, so a right-half-plane nonreal conjugate pair exists, without needing its exact count.

### B. Numerator and exact residue identity (lines110–180)

Differentiation gives `C=(tO)'=-4t^3+36t^2-88t+48`; inserting `epsilon=d/104` reproduces every numerator coefficient in(6), with leading coefficient1 and degree7.

At the odd roots `2,4,6`, `O'=(-8,4,-8)`. The residues `A=(E/O')` are exactly

`((4-d-u)/8, (6-3d+u)/4, (15d-u)/8)`.

Their interval bounds(10) hold uniformly. Independently multiplying

`E/O=1+sum A_j/(t-r_j)` and `C/O=4+sum r_j/(t-r_j)`

gives double coefficients `alpha_j=r_j A_j` and simple coefficients

`B1=A1/2+2-A2-A3/2`,

`B2=2A2+4+2A1-2A3`,

`B3=13A3/2+6+3A1/2+3A2`.

The bounds quoted in(12) follow. In particular the delicate lower bound `B1>=2-67/40-3/32=37/160>0` is valid even after dropping its additional positive term. The upper bound for `B3` is exactly `2079/160<13`.

The respective square-completion loss terms are bounded by `405/232`, `135/38` and `169/(15d)`: these follow from `alpha1>=29/40`, `alpha2>=57/10`, `alpha3>=15d/4`. Their sum is below `6+12/d<13/d` because `6d<1`. No numeric samples or executable arithmetic were substituted for these parameter estimates.

### C. Global strict margin, including the poles, zero and tail (lines182–236)

The completed-square inequality leaves one-half of each positive double-pole coefficient and costs at most `26/d` before multiplication by `epsilon=d/104`. Hence the loss in front of `O^2` is at most1/4, giving(14). For `t>=1/2`, `t-1/4>=t/2` and `alpha_j>=5d/4` give the coefficient `5d^2/832` in(15).

The identity `sum Q_j/O'(r_j)=1` is valid polynomial interpolation: degree at most2 with three distinct prescribed nodes. Its Cauchy–Schwarz coefficient is `1/64+1/16+1/64=3/32`, so `sum Q_j^2>=32/3`. Multiplication yields exactly `5d^2/78`, not an inferred all-parameter conclusion from a finite test. Extending(14) across the poles is legitimate because the multiplied expressions are polynomials.

On `0<=t<=1/2`, the three positive factors of `E` are at least `1/2,5/2,27/5`, giving `E>=27/4`; `C>=C(1/2)=25/2`, so the lower bound is `675d/832`, larger than the required `5d^2/78`. This includes the origin.

For `t>=12`, the product bound `|O|>=t^3/8` gives `tO^2/2>=t^7/128`. Combining the compact bound through12 and `t/(1+t)>=12/13` proves the exact global `m_d(1+t)^7` estimate. The apparent finite interpolation in the manuscript has a legitimate degree argument; the global estimate does not rely on sampling.

### D. Full-seven-width box and denominator homotopy (lines240–286)

The `a_(d,u)+v` description gives exactly the seven displayed independent intervals. In particular the constant interval is the Minkowski sum of `[18-3d,18+7d]` and `[-rho_d,rho_d]`, and every coefficient choice in that interval is representable; this is not only a correlated subset of the box.

The numerator coefficient absolute sum is `105+176epsilon<=105+11/65<106`. With seven perturbed lower coefficients, `|v(iw)|<=7rho_d(1+t)^(7/2)`. Therefore the pairing error is bounded by `742rho_d(1+t)^7=(m_d/2)(1+t)^7`. The strict margin is uniform over the complete box and all real frequencies.

For a denominator homotopy `a_(d,u)+lambda v`, the same bound prevents an imaginary-axis zero: such a zero would force the real pairing with the fixed numerator to vanish. Monicity and bounded coefficients give a uniform root bound, so no root can escape through infinity. Root continuity therefore preserves strict Hurwitz stability from `lambda=0`. This is an actual denominator-stability proof, not a rational cancellation argument.

Finally `K_d subset B_d` implies `Hull(T(K_d)) subset Hull(T(B_d))`; the explicit bad sextic remains in the larger hull. No continuity or affine property of the nonlinear normalization map is falsely needed for this inclusion.

## Primary-source and trust boundaries

I independently opened:

* [Xu et al., arXiv2609.26541v2](https://arxiv.org/html/2609.26541v2), actual §2 definitions and Theorem2.1: the premise is a **whole robustly Hurwitz independent monic sextic box**, not merely a stable correlated family. The claimed Lean formalization was not replayed and is not used here. Its §3 restates the degree-six Hermite–Biehler orientation used above.
* [Wang–Yu, arXiv:math/0202242v1](https://arxiv.org/html/math/0202242v1), actual introduction and §2: fixed-even/fixed-odd synthesizability is cited as existing work, and the equal-degree SPR definition is explicit. I do not independently authenticate each older fixed-parity theorem; it is not needed for the author's explicit numerator proof.
* [Bokam et al.2021, DOI10.24425/acs.2021.137422](https://journals.pan.pl/Content/120111/PDF/art06.pdf), actual printed pp348–349 and §2.1: the introduction expressly records stable interval systems producing unstable interval models under earlier Routh-related reductions, and the paper uses a **modified** construction. Thus the manuscript's novelty limitation is justified. This review does not equate their modified method with map(1), does not replay their examples, and does not refute their stability claim.

Classical Hermite–Biehler and ordinary continuity of polynomial roots remain named standard imports. All candidate-specific coefficients, residues, signs, square-completion estimates and full-width bridges above were reconstructed in writing. No formal/kernel or exhaustive executable verification was performed.

## Consequence and unresolved target

The pinned candidate is mathematically supportable as a **specific all-parameter countercontrol to naive normalized-Routh-image interval-hull induction**, with a genuine explicit common numerator for its original full-width septic boxes. Universal degree-seven synthesis remains open in this review; correlation-preserving induction, a different stable enclosure and numerator lifting are not excluded. Novelty of the exact packet remains UNCLEAR, and generic interval-reduction instability must not be promoted as new.
