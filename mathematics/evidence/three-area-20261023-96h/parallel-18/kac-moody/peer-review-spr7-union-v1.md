# v29-A — written reconstruction of the SPR7 UNION barrier and crossed completion

Reviewer MathKacMoody-2; author InfoSPR7. Verbatim observed clock before creation: **Sun Oct 25 04:24:00 PDT 2026** (`/bin/date`). Same-harness supplied-proof review, NOT blind, different-vendor, human, formal/kernel or novelty review. No scientific eval, arithmetic interpreter, symbolic program, enumeration or certificate replay was performed. Only metadata date/hash commands were used. Parent erratum v7 is binding; neither the parent's withdrawn failures nor its unadmitted corrected PASS supplies proof credit.

## 1. Verdict, pins, exposure and complete coverage

**Author-defect findings: 0 FATAL / 0 MAJOR / 0 MINOR established at the scope below.**

**WRITTEN_SUPPORTED:** the literal independent two-width box is robustly strictly Hurwitz; BOTH entire real midpoint-profile spans fail on the SAME actual denominator, hence their UNION fails; the crossed numerator has the claimed global half-line margin; the seven-positive-width enlargement retains the obstruction and a margin at least one quarter. I reconstruct the positivity claim by explicit outward rational coefficient bounds below, NOT by accepting the 128 printed integers as a machine certificate.

**NOT_RECONSTRUCTED:** equality of EACH of the 128 literal transformed decimal coefficient strings to its defining sum, their reported exact minima/minimum indices, all twelve exact decimal strings in the Hermite–Biehler endpoint tables, and the precise decimal-exponent lower-bound table. Their strict signs needed for the mathematical conclusions are independently established in writing below. This is NOT a blanket finite-certificate PASS, executable verification, or an attestation that the historical arithmetic was admitted.

Pins freshly observed before review:

- Manifest `peer-review-wave-eighteen-v29.json`: SHA256 `fd47c873613f88a299c4cf170fdabba86125d03e592e02c40651b9f24d3504e8`.
- Literal packet `peer-review-wave-v29-spr7-union-sources-v1.md`: SHA256 `c96c6ea2e23f75fd093282df5c5bd4209e1797dc5e04da25961657b5d51e542d`.
- P = `two-profile-union-barrier-and-crossed-completion-v1.md`: SHA256 `9642433eab7f637a9e3b28a6475b0dd3907ec16de85fd7224ff708e9d35e063d`, declared LF1–301.
- C = `two-profile-union-barrier-rational-certificate-v1.json`: SHA256 `d4f4fa1158fa31ebc00ff0468043e16369177a3c4fd08e69a55fae44295167bc`, declared LF1–422.

I read the COMPLETE literal packet, physical LF1–737, using exact raw ranges 1–180,181–360,361–550,551–737. These contain all P1–301 and C1–422, without an omitted/truncated source line. Source references below use the ORIGINAL P/C line numbers printed in the packet, not physical packet line numbers. The exposure ACK is `peer-review-spr7-union-ack-v1.json`. Earlier exposure was only the qualified historical SPR ledger row and parent v7; no prior correctness verdict on these new bytes was inherited.

## 2. Literal box, anchors, pairing and named classical imports

P27–59 give a monic seventh-degree denominator with independent x in [1,99] and c in [10^13,99*10^13], all other positive coefficients fixed. Its even/odd evaluations are exactly E_x(t), O_c(t) in P47–49. There is no correlation between the two varying coefficients.

Write

    f0=250000000, L=500500250, U=2001001/2,
    F(t)=f0-Lt+Ut^2-t^3, k=10^10.

The midpoint identities follow directly from root sums/products:

    B=50U, C_den=50L, D=50f0,
    A=50+1000+10^10,
    K=50*1000+50*10^10+1000*10^10,
    c0=50*1000*10^10.

Thus the displayed F and Q are the ACTUAL prescribed midpoint anchors, not subsequently selected roots. For real coefficients,

    Re(a(iw) conjugate(b(iw)))=E_a(t)E_b(t)+t O_a(t)O_b(t), t=w^2.

The sign criterion for N/a therefore has exactly the pairing orientation used in P/C. Classical imports are finite polynomial algebra/degree counting, IVT, the stated seventh-degree Hermite–Biehler criterion, and root continuity for a bounded monic coefficient path. The new proof does not consume either older sufficient-budget theorem or an old positive-margin export (P17–21).

## 3. Robust Hurwitzness is reconstructed without trusting the endpoint decimal strings

For E_x use the six test points in P69–74 and monotonicity in x. Their strict signs follow already from the following outward bounds, so the precise large decimal equalities are unnecessary:

- At 2/5, D-C_den*(2/5)>2*10^9, while x*(2/5)^3<100; the quadratic contribution is positive.
- At 3/5, the upper bound D-(25025*10^6)*(3/5)+(501*10^5)*(3/5)^2 is negative; dropping the negative cubic only increases E_x.
- At 400, E_x < (501*10^5)*400^2-(25025*10^6)*400+D <0.
- At 600, E_x > -100*600^3+50*10^6*600^2-(25026*10^6)*600 >0.
- At 400000, E_x > -100*t^3+50*10^6*t^2-(25026*10^6)*t >0.
- At 60000000, E_x <= -t^3+51*10^6*t^2+D <0.

For O_c use P78–83. The six signs follow from c>=10^13, c<=99*10^13, A>10^10, A<10000002000, K>105*10^11 and K<10500000100000:

- At 3/5, c-Kt-t^3>0.
- At 200 and 600, 99*10^13+A t^2-Kt<0 using the outward upper A/lower K bounds.
- At 1100, 10^13+10^10*t^2-10500000100000*t-t^3>0.
- At 10^9, -t^3+10^10*t^2-10500000100000*t>0.
- At 2*10^10, -t^3+10000002000*t^2+99*10^13<0.

The three sign-changing intervals for EACH cubic are disjoint; each has exactly one root and exhausts degree three, forcing simplicity. The six intervals are strictly ordered as P95, including the shared rational separators 3/5 and 600, where neither polynomial vanishes. Positive constants and negative leading coefficients give the correct orientation for the monic polynomial E_x(-s^2)+s O_c(-s^2). Hermite–Biehler proves strict Hurwitzness for EVERY independent (x,c), including closed coefficient endpoints (P85–97). No numerator pairing is used circularly to establish this base stability.

## 4. Both entire real spans fail on the same actual denominator

### Odd derivative span (P101–135)

D_Q=(tQ)' has endpoint values 91999999228000 and -103000000273000 at 20,30; expanding the four terms by hand reproduces those values. On [20,30],

    D_Q'<=180A-2K=-19199999911000<0.

Thus its one simple root tau lies strictly between 20 and30. Q>0 there by its explicit roots, Q'<0 there by 60A-K=-9899999987000, and Q(20)=293999999412000<Delta. Therefore O_-(tau)=Q(tau)-Delta<0. At tau the u D_Q contribution vanishes and the pairing is v*tau*Q(tau)*O_-(tau). It is negative for v>0, zero for v=0, and for v<0 the leading coefficient v of t^7 is negative. These three cases cover ALL real (u,v), not just normalized or positive profiles.

### Even complementary-Euler span (P139–177)

H=4F-tF' has the displayed coefficients. Direct expansion gives the stated signs at 2*10^6 and 3*10^6, and the derivative bounds in P151–153 make it strictly decreasing there. Its simple root sigma is above every F root, so F(sigma)<0. The uniform bound in P159–163 is the termwise bound obtained by placing each signed monomial at the appropriate isolator endpoint; its positive value 173025024975000000000 is reproduced by hand.

For u>0 the pairing with a_(1,c0-Delta) at sigma is strictly negative, regardless of v. For u<=0 its zero-frequency pairing u F(0)D is nonpositive. Hence the WHOLE second real span fails. Both span obstructions use the SAME original denominator, and both anchors are the simultaneous actual midpoint ones. This establishes the UNION statement, but gives no obstruction to their sums or arbitrary numerator cubics.

## 5. Crossed numerator and reduced exact coefficient formulas

P183–195 and C26–35 give N=kF(-s^2)+sQ(-s^2). Expansion is consistent with all eight displayed coefficients; it is monic of exact degree seven. Its odd component Q is not proportional to H, and its even component kF is not proportional to D_Q, by leading/t^2 coefficient comparisons. It is outside each excluded span and inside their sum.

For G=2P_(a,N)-(1+t)^7, the following exact formulas reconstruct the polynomial WITHOUT relying on the printed expanded decimal vectors. They follow by two cubic convolutions and the binomial coefficients 1,7,21,35,35,21,7,1:

    g0 = 100k f0^2-1,
    g1 = -200k L f0+2c c0-7,
    g2 = 100k L^2+200k U f0-2K(c+c0)-21,
    g3 = 2K^2+2A(c+c0)-200k L U-2k(50+x)f0-35,
    g4 = 100k U^2+2k(50+x)L-2(c+c0)-4AK-35,
    g5 = 2A^2+4K-2k(50+x)U-21,
    g6 = 2kx-4A-7,
    g7 = 1.                                             (5.1)

For example g6 equals -20000004207 at x=1 and 1939999995793 at x=99, agreeing with C49/C77. The common positive portion of g2 is exactly 251000750500062500000000000000; subtracting 2K(c+c0)+21 gives the two displayed g2 values. The remaining bounds needed below are deliberately much looser than exact decimal identities.

## 6. Written positivity reconstruction by outward rational bounds

The following inequalities follow from (5.1), for ALL 1<=x<=99 and the two c endpoints. Every number here is an integer or exact rational; there was no numeric interpreter:

    g0 > 624*10^26,
    g1 > -241*10^27,
    g2 > 2197*10^26,
    g3 > -771*10^24,
    g4 > 581*10^21,
    g5 > 19701*10^16,
    g6 > -21*10^9,   g7=1.                              (6.1)

At c=10^13 additionally g2>240*10^27. At c=99*10^13 additionally g1>739*10^27 and g3>-752*10^24. To make the outward comparisons auditable: g1 is its fixed -200kLf0 term plus 2cc0; g2 uses L^2=250500500250062500 and the common portion in §5; the worst g3 uses x=99 and the lower c endpoint, while the higher endpoint raises its 2A(c+c0) term. For g4, 100kU^2>1001001*10^18 and 4AK<420001*10^18; its positive 2k(50+x)L term exceeds the discarded 2(c+c0)+35. For g5, A>10^10 and 2k(50+x)U<298298*10^13 at x<=99 yield g5>19701*10^16. The g6 bound follows immediately from x>=1 and A<10000002000.

### 6.1 Region [0,3/5]

With a=0, b=3/5, the transformed coefficient divided by S is

    sum_(r<=j) g_r b^r binom(7-r,j-r).

At the lower c endpoint, discard positive g4,g5,g7 contributions and use g0>6.24*10^28, g1>-24.1*10^28, g2>24*10^28, g3>-(771/10000)*10^28. The resulting eight lower bounds, after division by 10^28 and before the g6 correction, are EXACT rationals with finite decimal representations

    6.24, 29.22, 52.92, 44.6833464,
    15.5333856, 0.4400784, 0.0533856, 0.4033464.

For instance the smallest arises at j=6 from 7*6.24-6*(3/5)*24.1+5*(9/25)*24-4*(27/125)*(771/10000). The possible negative g6 contribution, in these units, is less than 1/1000. Every coefficient is therefore positive.

At the upper c endpoint g1,g2 are positive and may be discarded instead. The entire negative g3 contribution is at most 6*(27/125)*752*10^24<10^27, and the negative g6 contribution is less than 21*10^9. The retained g0 contribution is at least 624*10^26. Again all eight coefficients are strictly positive.

### 6.2 Region [3/5,500]

Write h_j=G^(j)(a)/j! at a=3/5 and d=500-a, so 499<d<500. The transformed coefficients divided by S are

    C_j/S=sum_(h<=j) h_h d^h binom(7-h,j-h).             (6.2)

The bounds (6.1), by the Taylor formula, give

    h0>0, h1>0, h2>218*10^27, h3>-771*10^24,
    h4>581*10^21, h5>197*10^18, h6>-21*10^9, h7=1.

Here h0>0 follows from the previous region's leading coefficient. For h1 the worst g1+2ag2+3a^2g3 remains positive. For h2 the retained g2-3a*771*10^24 exceeds 218*10^27. The positive g4/g5 terms dominate the tiny negative g6 terms in the h3,h4,h5 comparisons.

Coefficients j=0,1,2 are immediately positive. For j=3,4 use respectively d^2(5h2+h3d) and d^2(10h2+4h3d), both positive with the displayed bounds. For j=5 use

    d^2(10h2+6h3d+3h4d^2+h5d^3)>0.

For j=6 the following explicit lower bound for the expression after factoring d^2 is already >3*10^28:

    5*(218*10^27)-4*(771*10^24)*500
      +3*(581*10^21)*499^2+2*(197*10^18)*499^3
      -(21*10^9)*500^4 > 3*10^28.

This also makes the j=5 comparison transparent (its analogous lower bound exceeds 3*10^29). Finally j=7 is G(500). Since F(500)=0, |Q(500)|>2*10^15 and |O_c(500)|>3*10^15/2, with both negative, G(500)>3*10^33-501^7>0. Thus all eight transformed coefficients are positive.

### 6.3 Tail [10^10,infinity)

Put T=10^10. Divide each Taylor coefficient of G(T+u) by T^(7-j). The contributions of g7,g6,g5 alone exceed, for j=0,...,7,

    87/100, 17/4, 46/5, 127/10,
    267/20, 1037/100, 49/10, 1.

These are binom(7,j)-(21/10)binom(6,j)+(197/100)binom(5,j). The only discarded potentially negative terms are g3 and g1; their TOTAL normalized magnitude is less than 1/1000, since their denominators include T^4 and T^6. All other discarded terms are nonnegative. Hence every tail coefficient is strictly positive, and in particular G(T)>0.

### 6.4 Region [500,10^10]

At a=500, its Taylor coefficients h_j satisfy h0>0, h1>0, h2>0, h3>0, h4>0 and h5>197*10^18, while h6>-21*10^9, h7=1. For the only slightly delicate h1 comparison, the lower c endpoint gives a retained bound >13*10^30 and the upper c endpoint gives >8*10^30; the negative g6 term is less than 4*10^24. For h2,h3,h4 the same bounds give respectively >18*10^28, >88*10^25 and >1073*10^21. These are direct substitutions into the finite Taylor formulas, not root samples.

Thus j<=5 in (6.2) is positive. For j=6, with d=T-500<T,

    C6 >= d^5(2h5+h6d)>d^5(394*10^18-21*10^19)>0.

Coefficient j=7 is G(T)>0 from the tail argument. This proves positivity of all eight coefficients here as well.

Consequently the positivity property needed in P243–247 is reconstructed on every region for every original corner, without requiring trust in any of the 128 printed decimal equalities. This is a written proof of the SAME transformed-polynomial sign condition, not a new scientific replay.

## 7. Closed endpoints, all frequencies and coefficient convexity

The finite transformation formula in P211–219/C126 follows by expanding (a+bu)^r(1+u)^(7-r). Its coefficient C7 is S G(b), so its strict positivity covers the endpoint missed by the finite-u parametrization. C0 covers the other endpoint. Tail translation covers all t>=10^10. Thus G(t)>0 for every finite t>=0, implying P_(a,N)>(1/2)(1+t)^7 at each corner; the paper's weak >= bound is valid.

For fixed N and fixed t the pairing is affine in x,c. An arbitrary independent pair is the SAME convex combination of the four endpoint pairings, with N and t held fixed. Therefore the margin applies throughout the two-width coefficient box, not just to endpoint polynomials or separately chosen numerators. Base denominators were independently Hurwitz by §3. Monic equal degree gives positive high-frequency limit, so the claimed strict SPR conclusion has the required orientation and normalization.

## 8. Seven positive widths and root-continuity stability

P253–275 are reconstructed. Expanding all seven coefficient intervals by delta=10^-21 keeps them positive and keeps all midpoint anchors unchanged. Both original failing denominators remain actual members. Thus BOTH whole-span obstructions, and hence their UNION obstruction, persist.

Clipping gives four even errors bounded by delta(1+t)^3 and three odd errors bounded by delta(1+t)^2; the monic leading denominator coefficient does not vary. Direct summation of the eight numerator coefficients gives C_N=7515518025000051051<10^19. Bounding numerator component magnitudes by their positive absolute coefficient sums yields the stated looser delta*C_N*(1+t)^7 bound. It is <(1/100)(1+t)^7, so the base one-half margin leaves MORE than one quarter uniformly.

No stability is assumed in that perturbation inequality. Along the segment from the stable clipped denominator, the margin precludes any imaginary-axis zero, since such a zero makes both denominator components and hence the pairing zero. Fixed monic degree plus bounded path coefficients gives a uniform Cauchy root bound, so no root escapes through infinity. Root continuity then proves strict Hurwitzness for every enlarged denominator before any cancellation argument. This completes the full-independent-seven-width strengthening at the stated classical imports.

## 9. Exact unresolved obligations and nonclaims

1. **NOT_RECONSTRUCTED — literal coefficient equality/minima gate:** C42–93's expanded g-vector decimal strings are not each independently re-expanded digit by digit; C136–415's 128 transformed integer strings, the associated `min_coefficient`/`minimum_index` fields and P234–241's exact power-of-ten table are not exhaustively hand-evaluated. The algebraic polynomial and the strict positivity property required for the theorem are independently proved in §§5–6. Do not cite this review as exhaustive validation of every literal certificate integer.
2. **NOT_RECONSTRUCTED — exact endpoint decimal strings:** the twelve exact integers in P69–83 are not each reproduced. Their required strict signs and all resulting root placements are independently proved in §3. The isolator/derivative identities of P107–163 used for the two profile obstructions were reconstructed as described in §4.
3. The historical owner computations in P3/P297–299 and C4–6 have no admitted-execution or executable-verification credit under parent v7. No new scientific computation was performed by this reviewer, and no finite data gate is cleared by claiming an old interpreter output as proof.
4. P281–293's unrestricted SPR7 universality, hybrid-cone universality/existence, an unrestricted eight-coefficient dual obstruction, and an all-M obstruction remain OPEN. Neither failure of the UNION nor success of the one crossed numerator settles any of them.

No actual author mathematical defect is established, so none is fabricated merely to turn an explicit reconstruction limit into a MAJOR finding. The appropriate disposition is scoped written support for the mathematical barrier/completion and the independent bounds above, with the literal finite-certificate equalities/minima explicitly NOT_RECONSTRUCTED. Parent alone integrates the result. All process errata, scientific HOLD and frozen deadline remain binding.
