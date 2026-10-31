# Failed two-cycle-star coefficient route and standalone Q/H certificate

Status: **FAILED GRAPH-CALLER ROUTE** with independently implemented exact integer replay of a standalone polynomial inequality. The displayed polynomial certificate does not prove a two-cycle-star spectral exclusion. No independent scientific review, parent adoption, or PH7 existence/exclusion result is claimed.

## 1. Goal and exact failure

The attempted target was a no-triangle critical row generator whose directed two-cycles share a common vertex. The proposed reduction incorrectly transplanted triangle coefficient formulas to two-cycles; the correct outside-sum corrections in §3 block the claimed graph conclusion. The separate mandatory-triangle theorem aims at a stronger conclusion but is not imported here.

## 2. Two-cycle simplex

Scale `d=1` and let `x>0` be the common-vertex diagonal escape rate and `u_1,...,u_6>0` the other rates. For each directed two-cycle between `x` and `u_i`, put its positive product as `x*k_i`; absent two-cycles have `k_i=0`. If `s_i` is the outgoing row fraction from `x` to `u_i`, then the reverse rate is at most `u_i`, hence

`0<=k_i<=s_i*u_i`, `sum_i s_i<=1`.

Therefore `lambda_i=k_i/u_i>=0` and `sum_i lambda_i<=1`; the vector `k` is a convex combination of zero and the six vertices where exactly one `k_i=u_i`.

Let `f_j` be the elementary symmetric sums of the six `u` rates, and define

`A0=f_2-4*f_1+74/9`, `B0=f_3-4*f_2+(74/9)*f_1-28/3`,

`h0=f_4-(70/9)*f_2+(212/9)*f_1-1007/27`, `h1=f_3-(70/9)*f_1+212/9`,

`K=sum_i k_i`, `J=sum_i k_i*sum_{j != i} u_j`.

Set

`Q(k)=81*[A0*(A0-K)-(f_1-4)*B0]`,

`H(k)=-243*[h0*(A0-K)-(h1-J)*B0]`.

Both are affine in the vector `k`. At zero, `Q,H>0` by the existing one-triple universal lemma at triangle weight zero (`frontier-20261028-ph7-critical-two-triangle-vertex-sets-v1.md`, SHA256 `b08ddcaca076342c98089bef3592475c1698b8ee7762b0617111e4eaf7ce6793`), including its exact mixed-domain certificate and independent-code replay. At each one-cycle endpoint `k_i=u_i`, strict positivity follows from the new symmetric six-rate `Q1,H1` certificate in §4 (relabel `u_i` as its first rate). Affine interpolation gives `Q,H>0` for every admissible multi-two-cycle vector.

## 3. Full coefficient accounting

Write the characteristic polynomial `D(y)*(y^2+p*y+q)`, where `D(y)=y*((y+1)^2+8/9)^2` and `q>0` by irreducible row-generator stability. Every two-cycle contains `x`, so two such cycles cannot be vertex-disjoint; all products of two disjoint two-cycles vanish. If there are no directed triangles, the **correct** contributions of these two-cycles to the `y^5,y^4,y^3` coefficients are respectively

`-x*sum_i k_i`, `-x*sum_i k_i*(f_1-u_i)`, and `-x*sum_i k_i*e_2(u_{j != i})`.

The `y^3` coefficient also subtracts `V4>=0`, the sum of the products of all directed four-cycles. Thus the correct coefficient equations are

`q=A0+x*(f_1-4)-x*sum_i k_i`,

`B0+x*[A0-sum_i k_i*(f_1-u_i-4)]=0`,

`h0+x*[h1-sum_i k_i*(e_2(u_{j != i})-6-2z)]-V4=0`, `z=8/9`.

Consequently the polynomials in §2 are not the actual two-cycle elimination polynomials. The proposed graph theorem is **not proved**, and the certificate in §4 remains a standalone polynomial fact. A valid replacement must certify the corrected higher-degree terms and the actual determinant caller; no failed equation is used as a premise.

## 4. Standalone exact polynomial evidence

The exact primary constructor `frontier-20261029-ph7-single-two-cycle-QH-check.py` SHA256 `9414532e80325474a2f8c3a7a15dabc2701494a99f09d539e553ca7e1e6f2412` generated `frontier-20261029-ph7-single-two-cycle-QH-certificate-v1.json` SHA256 `017e258fc2533b0b037ab7a4e1c45770abe24c467da47f71c4338ad35a9fd1f5`, containing 2,025 strict `Q1` leaves and 2,613 strict `H1` leaves. The separately implemented stdlib `Fraction`/integer replay `frontier-20261029-ph7-single-two-cycle-QH-integer-replay.py` SHA256 `3deeae076490cbe51a033d32a1b48aa9b8f0e23fe3939ca6ee8ee0f56c4dba68` reconstructed the polynomials, hashes, complete trees and strict interior vertex signs, and returned PASS. This confirms exactly those **displayed polynomials**, not the incorrect PH coefficient caller and not a scientific review or formal proof.

No two-cycle-star exclusion, new PH6 result, minimum-PH-order result, unrestricted `8/9` existence/exclusion, novelty, or parent adoption is claimed.
