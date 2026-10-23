# HIGH-K-CORE erratum 1 — precision repairs (co-governing)

Clock:2026-10-21T17:17:25-0700 (`/bin/date` before exclusive creation). Applies to proof-HIGH-K-CORE-v1.md,
SHA2562e3c17a67bdb617df60d2896b1d7a91fbe6a7df484b56651ea6662e2d7da76db, 185LF, which stays unchanged.
Requested by the parent after reading the complete manuscript. No lemma, inequality, case, residual test or
outcome changes; outcome (c) NOT_PROVED and all candidate status are unchanged.

1. Sec.1 LF38-44, full-domain convention. For P empty (all runs plus) AND for P = all runs (all minus) put
   m(P)=0 and Phi(P)=0: neither pattern has a sign change. For proper nonempty P, m(P) is the number of maximal
   cyclic intervals and Phi=2m(P). With this convention T(P^c)=-T(P), X^(P^c)=-X^P and m(P^c)=m(P) hold for
   EVERY P, including P empty/all (T(all)=sum_i tau_i=0=-T(empty); the all-minus pattern is the global sign
   flip of the all-plus pattern, with the same window). No proof uses any other reading.
2. Sec.4 LF168-172, diagonal failed step. Read the sentence beginning "Adding a variable for an isolated
   rotation keeps V linear only with rules..." as a statement about the SPECIFIC encoding attempted here:
   within the family of single-letter selection rules tried (never, u_t, 1-u_t, or a new binary e with
   'select iff e XOR u_t'), the only rule introducing a new variable while keeping V affine is the last, whose
   size parity contributes e+u_t and is not identically even when each gap holds one rotation; the attempted
   cross-gap pairing makes V quadratic and leaves M=(7p-7)/2<4p-3. It is NOT a classification of all possible
   linear encodings (for example encodings using zero-valued letters, complemented variables or other
   parametrisations are not analysed). Method failure only, not a no-go theorem.
3. Sec.4 LF160-161 (LOW-CORE) and the package's matching sentence. "the interlaced ABAB/C=2A-B selection
   (length4) is allowed" and "pure length-4 identities are permitted" mean only: NOT FORBIDDEN by the kappa=2
   pure-reflection padding window, which starts at 2kappa+2=6. No existence or feasibility of such a
   configuration inside an avoiding NF is asserted.

Both physical source parts of the corrected packet carry this erratum; the earlier v1 parts/manifest/coverage/
package remain immutable and are superseded for handoff by the v2 set, not edited or deleted.
