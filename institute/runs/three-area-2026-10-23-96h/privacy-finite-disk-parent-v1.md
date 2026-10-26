# Privacy: every positive-radius disk core is strictly improvable — parent disposition

Actual clock observation preceding this record: **2026-10-23T15:52:38-0700 PDT** (`/bin/date`). No scientific program, numerical integration, sampler or formal kernel was used.

## Decision

**SUPPORTED at the in-harness written-check level:** for every `0<b<1` and every `r>0`, there is an explicit compact convex origin-containing core `S_tau`, invariant under signed coordinate permutations, with the same area `pi r^2` and the same diamond support `sqrt(2) r` as the radius-r Euclidean disk, whose complete Minkowski-shell law:

- satisfies the **full continuous-diamond Borel privacy condition**;
- has exactly the same positive normalizer as the disk-core law (identical shell areas for **every** integer k);
- has strictly smaller full squared-Euclidean cost, with quantitative margin `36 m r w tau/(35 Z)`, `m=b/(1-b)`.

Therefore **no positive-radius disk-core law minimizes V at any finite epsilon**. This is an exact obstruction to that ansatz family. It does not give V, does not prove a positive gap from an unattained infimum over disk radii (no attainment argument), does not handle the zero-radius limit, and does not restrict the all-law target to symmetric/convex cores. Mechanism ancestry remains prior; novelty stays UNCLEAR.

## Actual evidence and full reads

- Complete376-line `information-science/evidence/three-area-20261023-96h/parallel-18/privacy-diamond-mse/proof-no-finite-disk-core-optimum-v1.md`, SHA256 `44b68f86550f36cc560d31683f887b188a3310c63f175ebfb0abaf7fb868c7b4`, including the raw untruncated shell-justification line.
- Its notation repair `proof-no-finite-disk-core-optimum-ADDENDUM-1-notation.md`, SHA256 `e013b011ebaaaddb365e7458a019a8037423b55caa5f0fcf3739b0bb77e6a2e4`: the parent found the literal `u_1`/`nu_1` mismatch itself (raw line59 defines `u_1`, later lines use `nu_1`); the addendum is operative, the original stays unchanged.
- Actual complete return `mathematics/evidence/three-area-20261023-96h/parallel-18/ordered-olson/peer-review-privacy-finite-disk-obstruction-v1.md`, SHA256 `685711cbe6b502ece6d13ed89ef858f2ef88b939822e13f90e13f02076478e0b`: verdict **0F/0M/0 unresolved minor** for the operative two-file packet, prior octagon exposure disclosed without verdict transfer.

The parent performed the complete read and the hand checks below; it did not run or numerically sample anything.

## Parent hand reconstruction

The bump `phi(s)=(1-(s/w)^2)^3` is C² with vanishing value/derivative/second derivative at `+-w`; the two translates sit strictly inside `(0,a)` and are disjoint. Identical supports give `integral psi=0` (area preserved) and `integral psi^3=0` (cubic term cancels identically). The chosen amplitude bounds `tau` are explicit positive rationals in b and r; no unspecified constant is used.

`tau||psi''||<=9/(32r)` together with `F''<=-1/r` gives `F_tau''<=-23/(32r)<0`. Since the perturbation vanishes near0 and a, the endpoint data `F_tau(0)=r`, `F_tau(a)=a`, `F_tau'(0)=0`, `F_tau'(a)=-1` are unchanged; strict decrease plus concavity give the sector bound and, via the inverse-branch second derivative, the concavity of the full quadrant boundary `q`. The eight-octant set is an intersection of hypographs, hence convex.

For the shell profile: on the curved arc the outward normals have first coordinate exceeding the second, so the diamond's support maximizer is `(1,0)` and the arc translates by `(k,0)`; at the diagonal normal the sum of the corner maximizer `(a,a)` and the diamond edge gives exactly `x+y=k+2a` up to `y=a+k/2`. This is a genuine support-function Minkowski computation with no unlisted facet regime. Integrating gives `|A_k^tau|=pi r^2+8ak+2k^2`, **tau-independent for every k**, hence exactly the disk normalizer (with `8a=4sqrt2 r`).

Minkowski inclusion gives both index inequalities for every diamond shift, including boundaries, so the full Borel privacy condition holds. The core lies in `2aD`, giving the uniform `2/3(k+2a)^4` moment bound and finite geometric moments.

For the moment change, only the curved cap changes. Expanding `(k+F_tau)^3-(k+F)^3` and using `F^2+y^2=r^2` plus both integral identities leaves exactly `16 k A tau+8 tau^2(kP_2+B_0)`. The cubic term is identically zero. Summing the tails gives `N_tau-N_0=16 m A tau+8 B tau^2`. With `|A|>=3rw/35` and `B<=64(m+r)w/35`, the amplitude choice forces `B tau<=m|A|/2`, so the change is at most `-12 m|A| tau<=-36 m r w tau/35`. Division by the identical normalizer is the stated strict improvement.

## Boundary and next obligation

The earlier checked octagonal comparison and sharp leading asymptotic are separate; nothing here verifies the new all-law peak-envelope relaxation candidate. Finite-V remains open. The same owner may continue the genuinely all-law structural attack (peak-envelope/coupled-plateau obstruction or a matching dual), not further core-family perturbations. Each new packet needs its own actual review. No execution is authorized; deadline unchanged.
