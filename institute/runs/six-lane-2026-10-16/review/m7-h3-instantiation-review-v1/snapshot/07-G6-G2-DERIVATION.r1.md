# G6 singleton equalities are already implied by the frozen G1/G2 constraints

This is a proof-only addendum to AMENDMENT-2.r1.md. No encoder, cube, CNF or search changes.

Fix a square, the ONB line ell = row 0, an off-line point p, and q in ell. The cube fixes g(p,q)=1 and
all g(p,r)=0 for r in ell other than q. Let t differ from p and q.

- If t belongs to ell, g(p,t)=0 by the cube and g(q,t)=0 by G1.
- If t is outside ell, the set of common neighbours of p and t on ell has size exactly g(q,t): all contributions
  outside q vanish, and the contribution at q is g(p,q) AND g(t,q) = g(t,q).
  - If g(q,t)=0, G2's zero-common-neighbour implication gives g(p,t)=0.
  - If g(q,t)=1, G2's one-common-neighbour implication gives g(p,t)=1.

Thus g(p,t)=g(q,t) in every case, including when either predicate is absent because its points are collinear.
This derives every G6 equality appended by `code/k3_cubes.py` directly from the already frozen G1/G2 predicates
and the cube's 18 unit clauses. The same-ray vector argument in AMENDMENT-2 is also valid, but it is not an
additional assumption needed to strengthen the Boolean model.

At the encoder-A clause level, the AND definitions reduce the frame intersection auxiliaries to h_q=g(t,q) and
h_r=0 for r != q. Its two G2 clauses then reduce to `g(t,q) OR NOT g(p,t)` and
`NOT g(t,q) OR g(p,t)`. If g(p,t) is a collinear constant false, these reduce to g(t,q)=0. Encoder B's exact >=1/
>=2 counters encode the same implications. G6 is therefore redundant propagation, not a restriction to an ansatz.
