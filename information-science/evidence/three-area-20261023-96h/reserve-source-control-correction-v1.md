# Reserve source audit: the displayed plus-sign matrix has a real repeated-pole fibre

Before-creation clock observed: **2026-10-23T13:20:18-07:00**. This is a source-control correction discovered while checking the reserve's primary baseline, **not activation or resolution of the (2,4,8) reserve**. Primary research remains the bounded-real surrogate model. No scientific program, solver or determinant computation was executed; all algebra below is written expansion. Status: **CANDIDATE source correction**, pending parent reconstruction. It is not a new generic-stabilizability theorem.

## 1. Actual primary source and the sign

Source: A. Eremenko, *Stabilizability by static output feedback*, dated 3 October 2026, [author-hosted PDF](https://www.math.purdue.edu/~eremenko/dvi/gpolep.pdf).

- Retained PDF: `sources/eremenko-gpolep-20261003.pdf`, SHA-256 `b03726a3c9d682b9c3ffd99a16d3b395b9278f44eb667e7ac3de20526ce416de`.
- The original PDF page 3 was rendered and **actually opened**: `sources/eremenko-gpolep-3.png`, SHA-256 `a2bca4bb69ac712186d4f40fd9482f9fe4b41623add6815f8064c07c4d05cc87`.
- The displayed second-row first entry is visibly **z+1**, not an extraction loss of a minus sign.

The source displays

    V_+(z) = [ z^2,  1,   z,  0
                z+1, z^2, 1,  z ],                         (1)

as an Anderson–Byrnes m=p=2 counterexample and says on page 4 that det[V_+(z);L]=c z^4 has no real solution. The literal displayed matrix does **not** have that property.

## 2. Explicit real fibre of the literal matrix

Let b be either real root of b^2-b-1=0, and set

    K = [ 1,    b
          1-b, -1 ],
    L = [ K, I_2 ].                                        (2)

The matrix L has rank 2 because its final two columns form I_2. Partition V_+=[D,N]. The block determinant identity gives

    det[V_+; L] = det(D-NK).

Here

    D-NK = [ z^2-z,    1-bz
                 bz,  z^2+z-b ].

Consequently

    det(D-NK)
      =(z^2-z)(z^2+z-b)-(1-bz)(bz)
      =z^4+(b^2-b-1)z^2
      =z^4.                                               (3)

Thus c=1 and a real L explicitly solve the very repeated-pole target claimed to be omitted. No numerical value or solver output is needed.

This only corrects the literal source control. It does not refute the 1984 existence theorem for genuinely nonstabilizable (2,2) systems, does not authenticate the original 1984 example, and gives no stabilizability conclusion for the (2,4,8) reserve.

## 3. A sign-corrected negative control, with complete fibre check

For clarity consider the one-parameter family

    V_tau(z) = [ z^2,   1,   z,  0
                 z+tau,z^2, 1,  z ].                       (4)

For any real tau!=0 this family is non-degenerate even over the complex numbers. To see this, its six 2x2 minors in order 12,13,14,23,24,34 are

    z^4-z-tau,  -tau z,  z^3,  1-z^3,  z,  z^2.           (5)

They have no common polynomial factor because z^2 and 1-z^3 are coprime, and their maximal degree is 4. Their one-dimensional linear relation space has coefficients

    q_12=q_14=q_23=q_34=0,  q_24=tau q_13.

A nonzero such coefficient 2-form cannot be decomposable, since its Plucker relation is

    q_12 q_34-q_13 q_24+q_14 q_23=-tau q_13^2!=0.

The complementary-minor/Hodge map takes a plane's decomposable Plucker coordinates to such a decomposable coefficient form; hence no complex rank-2 L makes the determinant identically zero. This establishes the claimed non-degeneracy, not merely a successful transfer at one gain.

For the fibre of a nonzero multiple of z^4, the coefficient of z^4 is the determinant of L's final two columns. It must be nonzero, so every such plane has a unique chart representative [K,I_2]. Write K=[[a,b],[c,d]]. Direct expansion of det(D-NK) yields coefficients

    z^4: 1,
    z^3: -(a+d),
    z^2: ad-bc,
    z^1: tau b+c-1,
    z^0: a-tau.

Therefore the complete z^4 fibre is characterized by

    a=tau,  d=-tau,  c=1-tau b,
    tau b^2-b-tau^2=0.                                    (6)

For tau!=0 there is a real fibre exactly when 1+4tau^3>=0. In particular:

- tau=+1, the literal source display, has two real chart solutions (2);
- tau=-1 gives b^2+b+1=0 and therefore has **no real fibre**;
- the tau=-1 matrix is a valid rational negative control for the author's stated repeated-pole test, established by the preceding complete chart and non-degeneracy argument.

The corrected matrix is thus

    V_-(z) = [ z^2,  1,   z,  0
                z-1, z^2, 1,  z ].

This is a written repair of the displayed sign, not a claim that the original 1984 paper used this exact matrix. Its full source formula remains to be authenticated before historical attribution.

## 4. Consequence for selection and preservation

The primary 2026 question about generic stabilizability is still the source's actual question. The 2002 Eremenko–Gabrielov paper, also opened during this audit, explicitly distinguishes nonsurjectivity for some pole-placement targets from generic stabilizability and leaves the latter even-even question open there. It does not automatically close the reserve.

However, the **unrepaired plus-sign display must not be used as a negative calibration/control** in any future reserve attack. The historical October 16 screening report's claim that this exact plus-sign example has no real z^4 fibre is source-faithful but mathematically false at the literal display. Those earlier files remain read-only; this addendum preserves the correction rather than altering their history. No external author contact or publication occurred.
