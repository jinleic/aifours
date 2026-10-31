# A three-state Metzler logarithmic-derivative sector lemma

Status: **WRITTEN**, awaiting independent review. This supplies a shorter all-variable replacement for the `z>=3/4` full-three-cycle lemma in `frontier-20261028-ph7-nine-edge-hamiltonian-cycle-exclusion-v1.md`: the new threshold is the strictly larger domain `z>1/2`, and the matrix need not have a cycle graph. The result is a spectral lemma, not an unrestricted PH6 theorem or a solution of PH7 at `8/9`.

## 1. Lemma

Let `M` be a real 3-by-3 Metzler matrix whose spectral bound is nonpositive. For `lambda=-d+ib` with `d>0`, `b>0`, and `z=b^2/d^2>1/2`, put `C(y)=det(yI-M)`. Then `C(lambda)!=0` and

`Im(C'(lambda)/C(lambda)) < 0`.

If `-t` is **any real root** of `C`, then also

`Im([(C(y)/(y+t))'/ (C(y)/(y+t))]_{y=lambda}) < 0`.

Roots and their multiplicities are taken algebraically; no diagonalizability is assumed. The analogous signs for `b<0` follow by conjugation.

## 2. Proof

If all three roots are real, every term in the logarithmic derivative `sum_j 1/(lambda-root_j)` has negative imaginary part. Removing any one real-root factor leaves two such terms, so both assertions follow.

Otherwise the real Perron eigenvalue is `-t`, with `t>=0`, and the other two eigenvalues are `-h +/- iv`, with `h>=t` and `v>0`. This remains true for reducible Metzler matrices: their spectral bound is a real eigenvalue, and the only real root must equal it. Shift by `t I` and divide by `d`. The nonreal pair becomes `-(h-t)/d +/- i v/d`, and the real eigenvalue is zero. The elementary Metzler trace-square inequality

`tr(X^2) >= (tr X)^2/3`

therefore yields `v^2 <= (h-t)^2/3`.

Scale by `d` and temporarily use `h,t,v` for the scaled values. We claim

`(h-1)^2+z-v^2 > 0`.

For `0<=t<=1`, the trace bound and completing the square give

`3*((h-1)^2+z-v^2) >= 2*(h-(3-t)/2)^2 + 3*(z-1/2+t-t^2/2) > 0`.

For `t>=1`, the lower bound `3*((h-1)^2+z)-(h-t)^2` is increasing in `h` on `h>=t`: its derivative is `4h+2t-6 >= 6(t-1)>=0`. At `h=t` it equals `3*((t-1)^2+z)>0`, establishing the same strict inequality.

The quotient by the real-root factor is `C_2(y)=(y+h)^2+v^2`, and direct complex arithmetic gives

`Im(C_2'(lambda)/C_2(lambda)) = -2*b*((h-1)^2+b^2-v^2)/|C_2(lambda)|^2 < 0`.

Here the display is in scaled units, so `b^2=z`. The strict numerator inequality also proves `C_2(lambda)!=0`. Finally `Im(1/(lambda+t))<0`; adding it proves the full-cubic result. In the complex-pair case the real root was unique, so the quotient assertion covers every possible real root. Undoing the positive scaling preserves signs. □

## 3. Immediate graph consequences

For a triangle block from the nine-edge connector template, the matrix with its actual internal rates and outgoing-leak diagonal is Metzler and has spectral bound at most zero, so the lemma applies. Therefore the Hamiltonian-connector exclusion in the earlier manuscript holds already for **all `z>1/2`**, not merely `z>=3/4`: at a repeated nonreal root, the imaginary parts of `1/(lambda+x)+A'/A+B'/B` are strictly negative.

Likewise, the universal omitted-rate harmonic condition in `frontier-20261028-ph7-nine-edge-connector-harmonic-obstruction-v1.md` holds throughout `z>1/2`: the proof there uses only strict negativity of the two full-block logarithmic derivatives. Its 8/9-specific numerical band retains its stated target scope. The singleton-elimination theorem separately imports the round's six-state spectral lemma and does not depend on this new result.

This manuscript's algebra is written and directly checkable; the lemma has not received an independent full mathematical audit or formal verification. No assertion is made for `z<=1/2`, a selected generator, original PH7 existence/exclusion, ten-or-more-transition graphs, novelty, or parent adoption.
