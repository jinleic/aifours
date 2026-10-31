# One common numerator on an entire two-radius marker region

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** This replaces the earlier timed-out nonlinear certificate query on a two-radius asymmetric family with an exact all-frequency positive result for its entire strict five-marker region. It is not a claim about the same radii outside that marker region or about arbitrary septic boxes.

## Family and exact region

Let
\[
a_0(s)=(s+2)((s+1)^2+9)((s+2)^2+49)((s+1)^2+169)
\]
have ascending coefficients \((180200,141860,51664,15508,1814,269,10,1)\). Set \(r=3916561/67108864\),
\[
w^-=(1,3/20,1,1/10,2/5,4/5,3/4),\quad
w^+=(13/20,2/5,2/5,4/5,1/5,2/5,3/20),
\]
and for two nonnegative radii \(x,y\) put \(\rho_j=x\) for even \(j\) and \(\rho_j=y\) for odd \(j\). The independent monic box \(K_{x,y}\) has
\[
\ell_j=a_{0,j}(1-r\rho_jw_j^-),\qquad
u_j=a_{0,j}(1+r\rho_jw_j^+).
\]
Its leading coefficient is fixed at one.

Define five rational frequency-squared markers
\[
t_1=1631/219,\quad t_2=2640/139,\quad t_3=40877/870,\quad
t_4=47781/427,\quad t_5=67177/417.
\]
The **strict marker region** requires
\[
\begin{array}{c|ccccc}
t&t_1&t_2&t_3&t_4&t_5\\\hline
E_+&<0&<0&&&<0\\
E_-&&&>0&>0&\\
O_-&>0&&&>0&>0\\
O_+&&<0&<0&&
\end{array}
\]
where \(E_\pm,O_\pm\) are actual parity endpoints. The exact marker region in the nonnegative-radius quadrant is the rectangle
\[
0\le x<X:=\frac{139823162826427256012800}{139757322918906715521939},\qquad
0\le y<Y:=\frac{10800480007165365452800}{10798610284816241421039}.
\]
At the outer corner \((X,Y)\), the first four marker pairs are strict and \(E_+(t_5)=O_-(t_5)=0\). Each even-marker expression is affine in \(x\) only; each odd-marker expression is affine in \(y\) only. They are strict at \((0,0)\), so interpolation proves all ten signs for \(x<X,y<Y\); the two binding fifth-marker expressions prove no larger \(x\) or \(y\) satisfies these strict markers. All coefficient lower endpoints stay positive in the rectangle because they are positive at the outer corner.

## One numerator for the entire rectangle

For every \((x,y)\) in this rectangle, every \(a\in K_{x,y}\), and every real frequency, the following **same** monic degree-seven numerator is strictly positive real:
\[
\begin{aligned}
(b_0,\ldots,b_7)=\bigl(&1,\
\frac{91572031815602757478544556860234726369266707279262777422067594}
{1176857569682834013617412782319289414926459305283},\\
&14049000358452,6932820707971,1140041173944,59844538766,7660657129,1\bigr).
\end{aligned}
\]

At the outer boundary box, its four actual corner pairings are nonnegative on \(t\ge0\). Corner \((E_+,O_-)\) has the exact square factor \((t-t_5)^2\); the other three have no factor removed. All four residuals have strict rational Bernstein certificates, with 8, 8, 5, 8 leaves. For the nominal denominator,
\[
P_{a_0,b}(t)/(1+t)^7\ge1.
\]

Let \(R=\max\{x/X,y/Y\}<1\). The box \(K_{x,y}\) lies in the radial box obtained by scaling **both** outer halfwidth vectors by \(R\). Every actual radial corner is the affine combination \((1-R)a_0+R a_{c,*}\). Since pairing is affine in the denominator and the minimum over an independent box occurs at an actual parity corner,
\[
\frac{P_{a,b}(t)}{(1+t)^7}\ge1-R>0.
\]
The five marker signs give disjoint alternating even/odd root bands and rule out imaginary-axis roots for every denominator. The reference \(a_0\) has a positive rational Routh column; connectedness and monicity then prove all-member Hurwitz stability. Alternatively, the positive pairing itself protects the straight homotopy to the stable nominal polynomial.

With
\[
S_*=1+\sum_j u_{j,*}=
\frac{259427208733030241153439831333112282}{643044784579897332141669854117},
\]
the ratio satisfies \(\operatorname{Re}[b(i\omega)/a(i\omega)]\ge(1-R)/S_*^2>0\). Because all eight coefficients of \(b\) are positive, **no** finite nonzero nonnegative atom combination, on any frequencies or actual members of any box in this rectangle, can have all coefficient sums nonpositive.

The earlier nonlinear searches returned `unknown` on one 12-atom support and on three sparse supports. This theorem settles those searches mathematically within their frozen strict marker region, and more strongly excludes every other finite support there. It does not turn a timeout itself into an UNSAT certificate or settle stable boxes outside that region.

## Evidence and limits

Frozen nominal and seed endpoints, radii, markers, outer boundary, exact numerator, square factor, all Bernstein leaves and bounds: `frontier-20261028-joint-parity-marker-region-frozen-v1.json`, SHA-256 `cc85bd85b5aca4793f8a54ba6adf8240c24f1d19e2ad440212bc98ae2c6a00ee`.

Standalone independent checker `frontier-20261028-joint-parity-marker-region-independent-kernel-v1.py`, SHA-256 `822083fe57b84ab95002b4e41ac0e7ed7ee7fdb16255a08679d09c758fadcd3e`, reconstructs the nominal factorization and outer endpoints; checks the ten nominal signs, eight strict outer signs and two binding zeros; verifies the nominal Routh column, boundary square factor, every residual Bernstein coefficient and the eight-leaf center bound; and rejects corrupted leaf/factor controls. Receipt `frontier-20261028-joint-parity-marker-region-independent-result-v1.json`, SHA-256 `77b487488e9998274e1ca0488e13f2fb5374d74b013c90e556d983c1768de0b9`.

The witness was obtained by exact tangent-preserving Bernstein feasibility, not by accepting a finite-grid dual as a full certificate. The separate attempt to optimize the coefficient size returned `unknown`; the displayed larger rational vector was independently replayed. Exact computations used integer and `fractions.Fraction` arithmetic on one Python Eval host; the interval, sign-band and homotopy arguments are written mathematics. No formal verification, cross-vendor review, novelty clearance or unrestricted septic verdict is claimed.
