# BOTTOM checkpoint 002: empty runs excluded; residual narrowed to empty-free row-critical patterns

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T18:43:18-0700. Previous checkpoint-001.md SHA256
7d99be13b5022d72389db84f7fa5b23f30aa2c4046a64b280f8de83631d248d1 (18:36:55). Written derivation only; claims CANDIDATE.
New hand derivation (not frozen as a proof yet): the q=g odd-gap rigidity holds whenever g=2r+1<=e-1 and r+1<=m<=e-r,
not just the violating small-m sets. Toggling an empty keeps g and changes m by at most 1 and T by nonzero tau_i, so two
such critical patterns are impossible. For a low bound violation at m<=k=floor(e/2)+1, E>0 is therefore possible only when
e is even, m=k and g=e-1, and every empty run has the SAME sign as both neighbours (only increasing m leaves the critical
window). For e odd no violating pattern remains. Thus under E>0 the low bound has cap ell=e (e odd) or ell=e-1 (e even);
the m=k toggle path gives h with d_h>=2ell+delta>=p-1+delta, enough to make all avoiding sets low. Counts give E>=2.
- c<=ell-1: independence/RS argument re-derived as Theorem A.
- c>=e: missing-set lemma (Case I only here) gives E<=ceil(c/2)-1<=e-2, E+C_E<=e+eps-1; position proof works with cap ell,
  including the large-Q-block branch (c+k<=p-1+eps against c>=e+k-1).
- remaining c=e-1 (e even): an independent set of k vertices would be all empty and would itself be a top critical pattern,
  but its selected empties are isolated, contradicting the flat-sign condition. Equality then gives E=e and RS contradicts M.
Hence E=0 in every surviving avoider. With E=0, absence of a violating low pattern gives cap e, h and E>=2, so an escape
pattern exists. The g=1 escape is excluded: E=0 forces >=4 singleton rotation runs; critical rigidity makes all such runs
signed -a and isolated in a two-interval pattern (at most 3 isolated vertices), impossible. Remaining escape g is odd >=3.
Next: freeze full inline proof of these claims; exact residual (E=0, rotations supported on {+/-a,+/-3a}, every low critical
pattern has signed other letters 3a and 2T=D_z; no assumed closure), failed-route note, package and manifest.
