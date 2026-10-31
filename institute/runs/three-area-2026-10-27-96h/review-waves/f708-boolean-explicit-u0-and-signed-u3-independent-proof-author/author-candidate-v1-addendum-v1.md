# Addendum 1: exact lambda calculation in the location proof

**Correction to the unadopted author-candidate-v1.md, section 2.** The displayed line there incorrectly leaves an uncancelled `d_f(sum k_st)` after already replacing the actual f-values by quotient representatives. The correct calculation, with all sums in F2 and k=sum_(s,t) k_st, is

    lambda(X_D)
      = sum_(s,t) [1+f(su+tv+k_st)] + d_f(k)
      = sum_(s,t) f(su+tv) + sum_(s,t) d_f(k_st) + d_f(k)
      = sum_(s,t) f(su+tv)
      = B_f(u,v) = 1.

The four `1` terms cancel. The second equality uses k_st in the radical, and the third uses linearity of d_f on K. The first uses X_D in L and the definition of the radical lift: lambda reads the h-coordinate after subtracting the lift `(0,d_f(k),k)`; addition and subtraction coincide in F2. Thus the claimed value and the subsequent lambda-column product are unchanged, but the original displayed equation is not literally correct. This addendum is the correction, not an overwrite, and is subject to the same independent parent review and nonadoption boundaries as the original. No scientific executable was run.
