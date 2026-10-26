# Residual PH6: the hidden pole is faster than every holding rate, forcing a Hamiltonian input-output path

Before-creation clock observed: **2026-10-23T14:14:30-07:00**. Slotmath-1, same repeated-pole PH problem. Status: **CANDIDATE / NOVELTY_UNCLEAR**, written reasoning only. No graph enumeration, matrix experiment or symbolic program was run.

## 1. Exact claim

Use H,K,a,c,b,d as in the slot selection and suppose an arbitrary PH6 representation exists with

    b^2>d^2/2.

Write det(sI-T)=D5(s)(s+u), lambda_i=-T_ii, v=u-c and x_i=lambda_i-c.

**Candidate theorem HP6:**

1. v>2d and every diagonal satisfies **lambda_i<u**.
2. The positive simple-path numerator identity has R5>0. Hence there is a positive initial-to-exit **Hamiltonian path through all six states**.
3. In an L6 doubled-layer placement, at least one positive within-layer edge connects the two vertices and is used by such a path. In the six-singleton-layer placement, the layer5 vertex has a positive exit. A branch placement with no Hamiltonian input-output path cannot realize this residual target.

These are topology-unrestricted necessary restrictions, not six-state impossibility or minimum7. They supplement, rather than replace, the nonuniform-rate gap candidate.

## 2. Spectral/positivity prerequisites

The reduced degree5 denominator binds the six-state characteristic polynomial to D5(s)(s+u). Above beta^2=1/5, deleting an unreachable state would give a forbidden order<=5 representation, so all states are reachable. Every transient state can reach an exit. The positive Perron-asymptotic argument in the corrected L6 packet, also reconstructed in the nonuniform-gap proof, then gives spectral abscissa-c and u>=c.

The same L6 argument gives irreducibility in the present region beta^2>1/2>1/3; its intermediate trace comparison is used only for blocks with ell>=1, as corrected by addendum001. Therefore x_i>0. Only x_i>=0 is needed in the calculation below.

Trace identities for M=T+cI give

    sum_i x_i=4d+v,
    tr(M^2)=v^2+4(d^2-b^2)>=sum_i x_i^2.                  (1)

Equivalently, center T by its holding-rate mean mu=a+h. Then v=2d+6h, h>=-d/3, and

    tr[(T+mu I)^2]=12dh+30h^2-4(b^2-d^2/2)>=0.

If h were between-d/3 and0, the right side would be strictly negative because6h(2d+5h)<=0 and b^2-d^2/2>0. Thus h>0 and

    v>2d.                                                (2)

This step requires no equal-diagonal assumption.

## 3. A diagonal cannot reach the hidden-pole rate

Suppose some x_i>=v and write x_i=v+e, e>=0. The remaining five nonnegative x values sum to4d-e, so0<=e<=4d. By Cauchy–Schwarz,

    sum_j x_j^2 >= (v+e)^2+(4d-e)^2/5.

Substitute in(1) and subtract v^2:

    4(d^2-b^2)
      >=16d^2/5+(2v-8d/5)e+(6/5)e^2.

By(2), the coefficient2v-8d/5 is strictly positive. The right side is at least16d^2/5, implying b^2<=d^2/5. This contradicts the assumed b^2>d^2/2. Therefore no x_i can be at least v, proving

    lambda_i=c+x_i<c+v=u for every i.                    (3)

The inequality is strict, and it concerns every holding rate, not merely the rate of one selected omitted vertex.

## 4. Positive numerator forces a Hamiltonian path

For the corrected L6 path identity, let W_m>=0 be the total weight of simple four-edge initial-to-exit paths omitting m and R5>=0 the total weight of simple five-edge initial-to-exit paths. Its exact cofactor proof gives

    sum_m W_m=K>0,
    K u=sum_m W_m lambda_m+R5.

Since(3) holds for every m,

    sum_m W_m lambda_m<K u,

so R5>0. A summand in R5 is a positive product of an initial mass, five positive off-diagonal rates and an exit rate. Its path is simple and visits six distinct vertices; it is therefore an actual Hamiltonian input-output path, not just a Hamiltonian cycle somewhere in an unobserved graph.

This also rules out the attempted escape R5=0: in that case u would be a weighted mean of omitted holding rates and could not exceed all of them.

## 5. Consequences for the one-extra-state layers

The L6 graph has one state in each distance layer0–4 and one extra vertex either in a doubled layer ell in0–4 or in singleton layer5. Any edge can advance at most one layer, and initial/exit supports lie in the prescribed extreme layers.

In a doubled-layer graph, a simple path visiting all six states must move through both vertices of the double layer consecutively using a within-layer edge. To see this, every other layer has a unique vertex. Once a path has moved beyond the double layer, returning to its other vertex would require revisiting a previously used unique layer before it could reach an exit, or would require a forward jump of more than one layer. Likewise it cannot bypass a lower unique layer and return later. This retains arbitrary backward edges in the graph; it only shows they cannot appear on the Hamiltonian initial-to-exit path without violating simplicity or the forward-layer bound.

If there are six singleton layers0–5, the only possible Hamiltonian layer order is0,1,2,3,4,5. Consequently the final layer5 vertex must be a positive exit for R5 to be nonzero. A non-exiting tail vertex in layer5 cannot supply a residual representation.

Thus, after ordering along a positive Hamiltonian path, all five spine edges are positive. The doubled layer can allow the two local one-vertex shortcuts around that pair; all other forward jumps are forbidden by the layer bound. Backward feedback remains arbitrary and must not be discarded in the next classification step.

## 6. Remaining obstruction and review boundary

The new theorem removes all non-Hamiltonian branches and proves u>max lambda_i, a stronger binding than the earlier u>=c. It still allows a genuine class of irreducible nonuniform-rate spine/feedback graphs. No theorem that all such graphs are companion-similar with positivity preserved has been proved, and applying an arbitrary similarity would be an invalid shortcut.

A concrete next obligation is to use the local doubled-layer numerator and the fully positive spine to bound its canceled zero or derive a new all-topology coefficient inequality. The rate-gap and HP6 conditions alone are not declared sufficient or impossible. This packet is outside the accepted v2/G7 baseline and requires actual separate written reconstruction and parent disposition. All shared provenance/verification errata remain operative; no formal/kernel or scientific-priority claim is made.
