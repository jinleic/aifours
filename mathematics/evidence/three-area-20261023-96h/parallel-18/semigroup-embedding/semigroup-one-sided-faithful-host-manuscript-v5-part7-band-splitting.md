# One-sided faithful-host manuscript — additive complete Part7, CRU-by-band splitting

Owner MathSemigroup-2, slot math-4. **AUTHOR-WRITTEN / UNREVIEWED.** Written after the actual v106-E review return (pinned 19:27:38) and the separate primary ACK `primary-resumption-after-v106-ack-v1.json` (actual 19:27:52). Exact WRITTEN semigroup algebra; no interpreter, calculator, program, CAS, enumeration, solver, replay or GO. Parts1–6 are unchanged and remain required in full; Part6 Theorem CG is consumed with its complete proof.

## 60. The least q-R-unipotent congruence

Let A be regular with an idempotent-pure q:A->C=M[G;I,Lambda;P]. Call a congruence rho on A **admissible** if rho is contained in ker q and A/rho, with the descended map, satisfies CRU (Part6 Section51). The descended map is pure: if q([a]) is idempotent then a, hence [a], is idempotent.

**Lemma 60.1.** ker q is admissible, and any intersection of admissible congruences is admissible. Hence there is a least admissible congruence psi_q.

Proof. A/ker q is isomorphic to q(A), a regular, hence completely simple, subsemigroup of C (Part1 Section8). There q is the identity, so equal images already mean equality.

Let rho be the intersection of admissible rho_i. Idempotents of A/rho lift to idempotents of A (regular A). If [e] R [f] in A/rho with equal q-images, then the images of e,f in every A/rho_i are R-related idempotents with equal images. These are equal by CRU, so (e,f) lies in every rho_i, hence in rho.

The least band congruence beta (A/beta the greatest band image) exists likewise, since subdirect products of bands are bands.

## 61. Theorem SB

**Theorem SB.** Suppose A is regular, its local idempotent corners E(eAe) are left regular bands (the one-sided S_R situation), and q is pure. If rho is admissible, beta' is a congruence with A/beta' a band, and rho intersect beta'=Delta, then

`Phi(s)=((b_[s]_rho, [s]_beta'), q(s))`

is an INJECTIVE homomorphism into P(B_rho cross A/beta', C). Here B_rho is the left regular band given by Part6 for A/rho, G acts on it by the Part6 automorphisms and trivially on A/beta', and the second coordinate is EXACTLY q. The base lies in W_L. Moreover, SOME pair (rho,beta') with these properties exists if and only if

`psi_q intersect beta = Delta`

holds for the least admissible congruence and the least band congruence, because any such pair contains (psi_q,beta). This criterion characterizes when THIS construction applies. It is NOT a characterization of all W_L-base embeddings: a source failing it may still embed by another method.

**Proof.**

*Multiplicativity.* For the product rule of Section0, G acts diagonally on B_rho cross A/beta'. The product of Phi(s),Phi(t) has base coordinate

`(b_[s] alpha_(g_s p)(b_[t]), [s][t])`.

Part6 Section55 gives the first component b_[st], because Phi_rho is multiplicative on A/rho over the descended q, and q([s])=q(s). The second component is [st] because A->A/beta' is a homomorphism. The C coordinate is q(s)q(t)=q(st).

*Injectivity.* Equal images give equal b-coordinates and q-images. Part6 injectivity on A/rho then gives [s]_rho=[t]_rho, and the band coordinate gives [s]_beta'=[t]_beta'. So (s,t) lies in rho intersect beta'=Delta.

*Base class.* B_rho is left regular. For A/beta': for an idempotent class x, lift it to an idempotent e. The corner x(A/beta')x is the image of the regular monoid M=eAe, whose idempotents form a left regular band. For every m in M with an inverse m', write phi(m)=phi(m)phi(m')phi(m). Using idempotency in the band image, phi(m)=(phi(m)phi(m'))(phi(m')phi(m))=phi(mm')phi(m'm). This lies in phi(E(M)), a subband because E(M) is a band. So the corner equals phi(E(M)), a homomorphic image of a left regular band, and is left regular. Hence A/beta' is in W_L. Corners of a direct product are products of corners, so the product base is in W_L. Part1 Section2 places P(B,C) in the original target class for every band B.

*Criterion.* By minimality, psi_q is contained in rho and beta in beta'. So psi_q intersect beta is contained in rho intersect beta'=Delta. Conversely apply the theorem to (psi_q,beta).

## 62. Scope, examples and composition with S

- If A satisfies CRU then psi_q=Delta; SB reduces to Part6 CG with a harmless extra band factor.
- If A is a band then beta=Delta; SB recovers the trivial embedding a->(a,q(a)).
- Mixed sources are new. For example, A=E5 cross G with q=q_E5 cross id_G fails CRU, since (0,1) R (1,1) have equal images. Yet psi_q is contained in the kernel of A->(E5's left-regular image {01,2,34}) cross G. That quotient satisfies CRU: its R-related idempotents coincide because its band factor is left regular. The projection A->E5 is a band congruence. The two kernels meet trivially, so SB applies. (This A also has an evident direct embedding; it illustrates the mechanism, not a new hard instance.)

For the original S, apply SB to S_R. By the opposite-semigroup duality of Part6 Section57, apply the dual statement (least L-unipotent congruence and least band congruence, R replaced by L) to S_L. Part2 Section16 then gives the original embedding over the same q, with base (LRB cross W_L-band) cross (RRB cross W_R-band). Corners of this product are left-regular times right-regular, hence regular, so the base lies in V. This strictly contains Part6 RU-LU (rho=psi_q=Delta on both sides) and every source whose one-sided factors are bands.

## 63. Exact remaining gap

The construction is unavailable exactly when, on some side, `psi_q intersect beta` is nontrivial. That means two distinct elements are identified both by the least admissible congruence (forced by R-related equal-image idempotents) and by every band image. No such original-class source is exhibited or excluded here. The general faithful W_L/W_R completion with all (M), loaded multigaps, shared rows and source-idempotent separation, or a genuine canonical obstruction, remains OPEN. So does existence of a pure completely simple quotient for arbitrary infinite nonorthodox input.

## 64. Assurance

Ordinary inputs: lattice/intersection properties of congruences, idempotent lifting in regular semigroups, and band identities, together with complete Parts1–2 and Part6 at their recorded assurance. No novelty claim. AUTHOR_WRITTEN/UNREVIEWED; it needs its own complete union gate. It is not formal, configured-family, human or executable acceptance, nor a solution of the full problem. All process findings, M1, the HOLD and the original cutoff/deadline remain.
