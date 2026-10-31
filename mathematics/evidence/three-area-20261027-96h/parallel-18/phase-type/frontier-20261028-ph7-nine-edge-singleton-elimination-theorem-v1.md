# Singleton elimination and a universal nine-edge PH path restriction

Status: **WRITTEN-checked-in-kernel**, awaiting independent review of this construction and application. It imports the standalone six-state Metzler spectral lemma in §4 of `frontier-20261028-ph7-global-irreducibility-v1.md` (SHA256 `729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49`), previously independently reconstructed in parent review f61. It does not claim a new unrestricted PH6 barrier, nor does it solve PH7 at `8/9`.

## 1. Theorem

Let `G` be a row generator on seven vertices, with precisely two vertex-disjoint directed triangle cycles, one singleton `x`, and three connector edges forming a directed cycle among the contracted components. Each listed transition is positive. Let the connector cycle omit the triangle vertices whose diagonal rates are `t_1,...,t_m`, and let the singleton diagonal rate be `x>0` (the same symbol also denotes the singleton vertex where clear from context).

If `G` has an algebraically repeated eigenvalue `-d+ib` with `d>0` and `b^2/d^2>1/2`, then

`x != t_j` for every omitted triangle vertex `j`.

If the connector is Hamiltonian, there are no omitted vertices and this statement is vacuous. It is a spectral statement, independent of any PH input or exit vectors.

## 2. Exact six-state construction if one rate equals x

Write the three positive diagonal rates on triangle `A` as `a_1,a_2,a_3`. Exactly one vertex is its connector-departure fork. If its internal-triangle outgoing fraction is `theta_A`, then `0<theta_A<1`; all other vertices send their entire diagonal rate to their triangle successor. Thus the directed triangle product is

`w_A = theta_A*a_1*a_2*a_3`.

Define `theta_B,w_B` analogously. The connector cycle passes through a nonempty consecutive directed segment of each triangle. Its transition product equals

`w_7 = x*(1-theta_A)*(1-theta_B)*prod_{v visited in A union B} u_v`.

Suppose an omitted vertex `t` has rate `u_t=x`. Construct a row-conservative six-state Metzler generator by deleting the singleton and joining the triangles with one connector edge in each direction. Preserve all six triangle diagonal rates and the two fractions `theta_A,theta_B`. In the triangle containing `t`, extend the connector's directed segment by exactly `t`: if `t` is the predecessor of the old entry, move the entry to `t`; otherwise it is the successor of the old departure, and move the departure fork to `t`. If the fork moves, put the same internal fraction `theta` at the new fork and restore the old fork's sole internal transition to its full diagonal rate. A nonempty proper contiguous segment of a directed three-cycle always has the selected omitted vertex as its predecessor or successor, so one of these moves works. Retarget the intertriangle connector endpoints accordingly. The other triangle's segment is unchanged.

Every row of the new generator sums to zero, all eight listed transition rates are strictly positive, and the new graph is strongly connected. Its two triangle products remain `w_A,w_B`. The new connector visits exactly the old triangle vertices plus `t`; its product is

`w_6=(1-theta_A)*(1-theta_B)*prod_{v visited in A union B plus t} u_v = (u_t/x)*w_7 = w_7`.

Let `A(y)=prod_{v in A}(y+u_v)-w_A` and `B(y)` analogously. Because the only simple cycles are the two triangles and the connector, directed-cycle expansion gives

`det(yI-G)=(y+x)*A(y)*B(y)-w_7*prod_{j=1}^m(y+t_j)`.

The six-state generator `H` has characteristic polynomial

`det(yI-H)=A(y)*B(y)-w_6*prod_{j != selected}(y+t_j)`.

With `x=t_selected` and `w_6=w_7` this is the exact **polynomial identity**

`det(yI-G)=(y+x)*det(yI-H)`.

The construction was checked algebraically in the owner's kernel and replayed by `frontier-20261028-ph7-nine-edge-singleton-elimination-check.py` (SHA256 `422c1466347241a8e44fe6815333bbec6ea62f4a47b89a8eee0e3e1610b7d530`): SymPy 1.14 expanded actual `yI-G` and `yI-H` matrices, checked every row tie, and verified the identity for all nine canonical connector shapes and all 18 possible omitted-vertex choices with symbolic rates and symbolic fractions. The replay reuses the same approach and is not an independent mathematical review, a positivity proof, a numerical witness, or a formal proof assistant.

## 3. Spectral contradiction

Because `lambda` is nonreal, `lambda+x!=0`; the polynomial identity makes `lambda` and its conjugate double eigenvalues of the six-state row generator `H`. The generator also has eigenvalue zero; the only sixth eigenvalue is real and nonpositive, by conjugation and the spectral bound of a row-conservative Metzler matrix. Thus after dividing by `d` its spectrum is exactly the spectrum covered by the imported six-state lemma,

`0, -u, -1 +/- i*sqrt(z) each twice`, `u>=0`, `z>1/2`.

That lemma excludes `H`. Hence no omitted triangle rate equals `x`, proving §1. This does not reuse or rebuild the PH6 input-output theorem; it applies the separately stated **spectral** lemma with its actual hypotheses.

## 4. Consequence for the actual PH input and exit

Suppose in addition that a nonnegative input/exit pair realizes the target transform with relative degree five. **At least one supported simple input-to-exit path must visit the singleton.** If all avoided it, every supported simple path would have length at most five, and none could have length below four because path weights are positive. The adjugate numerator expansion would have a factor `y+x`: a length-five path leaves only the singleton; a length-four path leaves the singleton and one other vertex, and their principal 2-by-2 determinant contains the factor `y+x` because this graph has no 2-cycle. Therefore the target's hidden quadratic `Q` has root `-x`, so `det(-x I-G)=0`.

But the determinant formula yields

`det(-x I-G)=-w_7*prod_j(t_j-x)`,

which is nonzero by §1 (and is `-w_7` if `m=0`). Contradiction.

For the contracted orientation `A -> B -> singleton -> A`, this excludes **all** choices whose input support is entirely inside `A` and whose exit support is entirely inside `B`, on every connector length, because all their simple supported paths avoid the singleton. It is stronger than the earlier length-six-only input-output restriction but still leaves many multisupport patterns open.

The graph-specific theorem uses only this explicit template plus the named six-state spectral import. To apply it to every nine-transition critical PH7, one also needs the separately pending nine-edge graph-template theorem and its capacity/overlap-budget inputs, and the separately supported irreducibility/Perron-normalization caller. No claim is made for graphs with ten or more transitions, existence/exclusion of PH7 at `8/9`, formal verification, new PH6 science, independent review of this theorem, or novelty.
