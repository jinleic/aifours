# A rational complex-hidden spectrum passes the centered moment tests

Status: **WRITTEN-checked-in-kernel with exact rational arithmetic**, a limitation of the preceding method—not a generator, a PH witness, or a new impossibility theorem.

Consider the formal seven-point spectrum

`0, -11/4 +/- i*sqrt(3)/2, -1 +/- i*sqrt(8/9)` with the latter pair repeated twice.

It is real-conjugate symmetric with a simple zero and two nonreal hidden roots. Center the corresponding formal moments by adding `h=(4+2*(11/4))/7`. Direct exact calculation gives

`tau2=593/504 > 0`,

`tau3=-1243/4704 < 0`,

`(107163/4)*[(25/42)*tau2^3-tau3^2]=49364791/2048 > 0`.

Thus this formal spectrum satisfies both `tau2>=0` and the centered seven-dimensional Metzler/symmetrization necessary inequality `(25/42)tau2^3-tau3^2>=0`, despite its hidden mean `11/4` being strictly below the algebraic threshold `r_*>3437/1000` proved conditionally for two real hidden roots. These are exact rational identities checked in the owner's SymPy kernel.

The implication is strictly methodological: the centered trace-two/three argument used in `frontier-20261029-ph7-critical-all-real-hidden-roots-bound-v1.md` cannot extend its mean threshold to arbitrary complex hidden roots merely by reusing those two inequalities. Other graph, higher-moment, Jordan, input/output, or PH constraints might still exclude the formal spectrum. No claim is made that any Metzler matrix or PH representation realizes it, or that it passes all M-matrix/JLL or other necessary tests. No unrestricted 8/9 verdict, formal proof, novelty, independent scientific review, or parent adoption is claimed.
