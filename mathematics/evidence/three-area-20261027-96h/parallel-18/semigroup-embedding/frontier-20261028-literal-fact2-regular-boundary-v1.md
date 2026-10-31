# Literal Fact 2 cannot include a larger regular subclass without changing its target

**NEW AUTHOR WRITTEN SCOPE BOUNDARY with exact finite control; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 20:59:39 PDT 2026**. The printed Question2 asks to extend Fact2 to as large a regular-semigroup subclass as possible. This note answers only the **literal unchanged-target interpretation**; it does not decide which generalized target the question permits or solve that open-ended extension.

## Exact statement

For a regular semigroup S, the following are equivalent:

1. S embeds in a homomorphic image of a semidirect product of a semilattice by a group.
2. S is inverse.

The forward direction is true even if the homomorphism is NOT idempotent-separating. The reverse direction follows from the printed Fact2, which gives the stronger idempotent-separating image for every inverse semigroup. Thus preserving the literal Fact2 target cannot enlarge the regular source class beyond the inverse semigroups.

## Proof of the forward direction

A semilattice-by-group semidirect product A is inverse: it is regular, and its idempotents are the semilattice coordinates over the group identity, which commute.

Any homomorphic image U of a regular semigroup is regular. If `π:A→U` is onto and e∈E(U), choose x∈A with π(x)=e, and a mutual inverse z of x². Then `p=x z x` is idempotent, and π(p)=e because `π(x² z x²)=e π(z)e=e`. Thus every idempotent of U lifts to an idempotent of A. Idempotents of an inverse semigroup commute, so any e,f∈E(U) commute as images of commuting idempotents. Therefore U is a regular semigroup with commuting idempotents and is inverse (the standard inverse-semigroup characterization).

If a regular S embeds in inverse U, the idempotents of S commute because they are idempotents in U. S is regular, so the same characterization makes S inverse. Equivalently, every source inverse is the unique ambient inverse and lies in S. No assumption about a particular actor, band variety, idempotent-purity or finite cardinality is needed.

## Concrete boundary and interpretation

The two-element right-zero band S={e,f}, with ef=f and fe=e, is regular and weakly E-unitary, and every local monoid is a singleton, so it is locally inverse and locally r-orthodox. It is NOT inverse because e and f do not commute. S is seminormal and embeds in the physical seminormal-band-by-CS product `P(S,1)`, yet it cannot embed into any literal Fact2 target by the theorem above.

`frontier-20261028-literal-fact2-boundary-checker-v1.py`, SHA `d70081e6a5f162f2817fce2fb9629828be12d3edf530e16014424b4981223ba0`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 20:59:39 PDT 2026**, exit0. It checks the two-element source's associativity, local corners, seminormal identity and noncommuting idempotents, and a4-element semilattice-by-C2 inverse product. The arbitrary-image/subsemigroup argument is the written proof, not inferred from that control.

The regularity hypothesis on S matters: a nonregular subsemigroup of a group, such as the positive integers under addition inside Z, is not an inverse semigroup. The printed Question2 may intend a genuine GENERALIZATION of Fact2, e.g. changing semilattice/group to appropriate band/CS objects or changing the image requirement; this note does not choose or settle such an extension. No full printed-Q2, novelty, independent review or formal proof is claimed.
