# Addendum 4 to evidence/fourier-co-ansatz-v1.md: status after the parent's Proposition FCO-2p

Recorded 2026-10-19T06:27:04-0700 (from /bin/date). Author ContinueRQLS10b. No earlier file is edited. Status labels
follow the parent's records; nothing here upgrades them.

1. Parent verdict RUN/review/rqls10-FCO-2p-parent-verdict-v1.md
   (141450a2c49adb3c02e4e2e5a86e51b29c84d3ac6cf38d9a2e61712ea0a4ac00): Proposition FCO-2p, CORRECTNESS_ACCEPTED_SCOPED_PARTIAL
   (restricted negative): for n = 2p, p an odd prime, no permutations pi, rho make
   q_ij(t) = zeta^(t j + pi(t) rho(i)) / sqrt n a QLS orthogonal to Cay(Z_n) with classes {(i, i + s)}; equivalently
   H = [zeta^(i t + rho(i) pi(t))] is never complex Hadamard. Texts: derivation
   RUN/review/rqls10-FCO-2p-nogo-parent-derivation-v1.md (355718b429d69f6892bf1dda4342dcde35ab92cd18f90d0963d41e118ee23569)
   with erratum 1 (013893adb51a4c5cd1aaff3faed4c961e8dac6a9b0948227995253a225bb4978); reviews Codex ACCEPT 0/0/0 and
   Claude ACCEPT 0/0/6 MINOR (disposed). Proof sketch from the read-only scout QuantumGroupTableNoGo3; the parent wrote
   and checked the derivation. No novelty or priority claim (possibly folklore among Fuglede specialists).
2. It is the analytic counterpart, for n = 10 (and every n = 2p), of the one-producer exhaustive enumeration of
   code/fourier_co_enum_v1.py run by the parent (RUN/review/rqls10-FCO-parent-run-v1/, audit f8b5a8e2...5807). FCO(8)
   (n = 0 mod 4) and n = 2m with m odd composite remain covered only by enumeration or not at all.
3. Consequence through Lemma F8 (addendum 2, 2e4f9124...b010) and F9 (addendum 3, 18933031...3b99), both STILL
   UNREVIEWED: if F8 holds, then for n = 2p no Fourier-separable QLS(n) (entries omega^(f(t) lambda(j) + g(t) rho(i)
   + k(t) + l(i, j)) / sqrt n) has any orthonormal transversal; in particular there is no Fourier-separable 1-RQLS(10)
   for ANY resolution and at ANY cardinality. This conditional statement is not parent-accepted and is not claimed
   until F8 / F9 are reviewed.
4. Unaffected: unrestricted 1-RQLS(10) (UNKNOWN), unrestricted QLS mates of Cay(Z_10) or Cay(D_5) (the fixed-B assay
   remains the live route, written only until the supervisor qualifies), and every non-monomial or non-separable family.
