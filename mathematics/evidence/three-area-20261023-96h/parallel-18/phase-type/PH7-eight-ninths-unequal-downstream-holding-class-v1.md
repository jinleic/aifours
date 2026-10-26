# PH7 at8/9 — an unequal-downstream holding class is uniformly impossible

Actual returned `/bin/date` before this freeze: **Sun Oct 25 10:42:57 PDT 2026**. MathResearch96h, math-1. ONE consolidated new PRIMARY successor under `primary-continuation-20261025-102319-v1.json`. WRITTEN algebra only; no scientific interpreter/eval/program, symbolic program, enumeration, solver, replay, compile, external-model CLI or nested agent. Metadata/source/date/hash operations only. No parent arithmetic-eval output is a premise.

V9,V10,V11 and HOLD were read in the required order before the new primary body; the separate exposure ACK is `primary-continuation-20261025-102319-ack-v1.json`. V11 is a LATER evidence overlay, not retroactive freeze content. In particular the old parent09:51:10 header is not an observed-clock premise. The full346-LF baseline and25-LF parent boundary were freshly read before this new unequal-holding derivation. Current metadata pins are `86312277159c0b278638cf424325f772ac9189907dea05aa33f88f2fc8094076` and `d60d57894d8bf70509451a170f75e0cf06452c31796c8467b133e119c2a3895e`. V11's pin is `3ce29e3c49d4789106431978152ffab28a3d14402a748ec3828c825f31c4d9e7`.

## 1. New actual class, theorem and honest original-target status

The target is STILL the original repeated-pole PH law, at b_pole²/d²=8/9:

`H_(c,d)(s)=c[((c+d)²+(8/9)d²)]²`

`              /[(s+c)(((s+c+d)²+(8/9)d²))²]`,  c,d>0.

The normalized d=1 proof below is independent of c>0. The original unrestricted minimum remains{7,8} at its retained B6/upper8 imports; those are NOT premises of the class contradiction.

**NEW theorem:** no raw-positive seven-state matrix in the complete3+3 class below can have this transfer. All internal upstream edges, all downstream backward edges, all nonnegative upstream inputs, ALL r/f/Dback and the CLOSED downstream holding interval q∈[1,2] are quantified. For q>1 the downstream holdings(1,1,q) are genuinely UNEQUAL, outside the previously closed equal-downstream class. The upstream holdings are(1,1,2); neither arrangement is asserted WLOG.

The new argument does NOT just reuse the old equal-rate coefficient identities. Changing the last downstream holding changes its characteristic's X² coefficient, its row cofactors, the central trace, the exact high-coefficient cone and the forced p bound. We derive the changed identities first, then a new uniform scalar contradiction on the entire q interval.

This is an AUTHOR-WRITTEN candidate needing independent reconstruction, not an actual PH7 witness or an arbitrary-topology impossibility. Section11 gives the ENTIRE exact residual.

## 2. Literal ACTUAL matrix and boundaries

Set d=1,y=s+c and

`D(y)=y[(y+1)²+8/9]²`, `K=D(c)>0`.

Choose q∈[1,2], put epsilon=q-1∈[0,1], and take arbitrary REAL NONNEGATIVE a,b,g,h,u,v,w. Define actual principal matrices

```
A=[-1,1,h
    a,-1,1
    g,b,-2],

F_q=[-1,1,0
      u,-1,1
      w,v,-q].
```

Let b0=e3,t0=e1 and

```
G=[ A      b0        0
    r^T   -ell       t0^T
    Dback  f         F_q ],

beta=(C,B,1,0,0,0,0),     gamma=K e7,
B,C>=0.
```

Every entry of r,f,Dback is an actual nonnegative matrix entry, with no omitted backward term. Ell is initially any real number. The proof rules out the target characteristic/numerator match even before imposing principal stability or PH row sums; their imposition cannot repair the contradiction. The designated positive forward path is normalized to1, not claimed WLOG for zero-path cases or multiple upstream exits.

## 3. Actual cofactor identities — the precise equal-rate property that fails

Put X=y+1 and define the following nonnegative actual quantities:

```
Abar=a+b+h*g,
eta=Abar-a=b+h*g,
Gamma=g+h*a*b,
G0=a+Gamma,
U=u+v,
Z=w+epsilon*u,
M=Abar+U.
```

Direct determinants/adjugates are

```
a_R=X³+X²-Abar X-G0,
v_R=adj(yI-A)b0=(1+hX, X+a h, X²-a)^T,

a_S=det(yI-F_q)=X³+epsilon X²-U X-Z,
w_S=t0^T adj(yI-F_q)=(X²+epsilon X-v, X+epsilon,1).
```

For the downstream identity, multiply the printed w_S by

`yI-F_q=[[X,-1,0],[-u,X,-1],[-w,-v,X+epsilon]]`.

Its result is(a_S,0,0). The constant of a_S is-w-epsilon*u, so Z≥0 is tied to the SAME physical return entries; it is not a free sign choice. The upstream column multiplication similarly gives(0,0,a_R)^T as in the explicit matrix.

For q>1 the old a_S=X³-U X-W is FALSE: it now has a POSITIVE X² term epsilon. The actual r3 high-coefficient triple changes from(1,0,-(a+U)) to(1,epsilon,-(a+U)), and f1 changes from(1,1,-(Abar+v)) to(1,q,epsilon-Abar-v). The old EXACT R4 formula without an r3 term is therefore unavailable. The central trace becomes ell=p-q-2, not p-3. Consequently the old H=2/9-M and p≥11 collection cannot be asserted here. The correct replacement below allows M<2q-16/9 and only forces the weaker uniform p≥50/9.

This is a changed principal holding/cofactor coupling, not redistribution of feedback in the old cone. As before, internal returns also make the old low-dimensional quotient remainder nonpositive in general; no such quotient-positive assumption is reused.

## 4. Initial polynomial, complete transfer and literal PH ties

The ACTUAL initial polynomial is

```
Q(X)=beta_R v_R=X²+Bbar X+Cbar-a,
Bbar=B+h C>=0,
Cbar=C+a h B>=0.
```

Write Q(y)=y²+p y+q_H, where

`p=Bbar+2`, `q_H=p-1-a+Cbar`.

The symbol q is the DOWNSTREAM HOLDING; q_H is the hidden quadratic constant and is not fixed or independently chosen. Both real/nonreal hidden pairs are allowed. Necessary nonnegativity of Bbar,Cbar is used without asserting a converse realization for arbitrary independent effective values.

The downstream numerator is w_S(K e3)=K. Full single-center elimination gives the literal polynomial determinant and adjugate:

```
P7=(y+ell)a_R a_S-a_S r^T v_R-a_R w_S f-w_S Dback v_R,

beta adj(yI-G)gamma=KQ.
```

One obtains this by solving the actual two principal resolvents and the remaining scalar middle equation; clearing denominators makes it a polynomial identity even at singular principal y. No additional product of independently selected return weights is introduced.

The transfer is KQ/P7. Equality to K/D, with K≠0, REQUIRES the entire polynomial identity

`P7=DQ`,                                                (T)

even under coincident/cancelled factors. Trace forces

`ell=p-q-2`, `k=ell-1=p-q-3`.

Thus the exact residual is

`R=(X+k)a_R a_S-DQ`

` =a_S r^T v_R+a_R w_S f+w_S Dback v_R`.                 (C)

If a raw candidate satisfying(T) also had G-cI Hurwitz, its fixed forward path would give a positive normalizer h0=(-(G-cI))^(-1)gamma. Then Tph=diag(h0)^(-1)(G-cI)diag(h0),alpha=beta diag(h0),omega=diag(h0)^(-1)gamma would have Tph1=-omega and alpha1=K/D(c)=1, with sole exit K/(h0)_7. Thus actual initial/exit ties are retained, not assumed from a spectrum. The impossibility below occurs before any such successful pair exists.

## 5. The COMPLETE changed high-coefficient cone

Let Rj=[X^j]R. Every actual generator triple([X5],[X4],[X3]) is:

|Coefficient|Triple|
|---|---|
|r1|(0,h,1+epsilon*h)|
|r2|(0,1,epsilon+a*h)|
|r3|(1,epsilon,-(a+U))|
|f1|(1,q,epsilon-Abar-v)|
|f2|(0,1,q)|
|f3|(0,0,1)|
|D11|(0,0,h)|
|D12|(0,0,1)|
|D13|(0,1,epsilon)|
|D21|(0,0,0)|
|D22|(0,0,0)|
|D23|(0,0,1)|
|D31|(0,0,0)|
|D32|(0,0,0)|
|D33|(0,0,0)|

These follow by multiplying the actual a_R,a_S,v_R,w_S. For example a_S v3 has leading1,next epsilon and third-(a+U); a_R(w_S)_1 has leading1,next1+epsilon=q,third epsilon-Abar-v. All15 entries are accounted for, including those affecting only lower coefficients.

Consequently the SAME feedback entries give

```
R5=r3+f1>=0,

T4:=R4-epsilon*R5=h*r1+r2+f1+f2+D13>=0,

S:=R3+M*R5
 =(1+epsilon*h)r1+(epsilon+a*h)r2+eta*r3
    +(epsilon+u)f1+q*f2+f3
    +h*D11+D12+epsilon*D13+D23>=0.                      (G)
```

The replacement T4, not the old equal-rate R4 equality, is the load-bearing second constraint. Every coefficient in(G) is nonnegative throughout the CLOSED q interval. No hidden row/exit assumption or trace-square screen is used to obtain them.

## 6. Full actual coefficient expansion and the forced p bound

Put

`nu=16/9`, `rho=64/81`, `chi=34/9`,

`K0=M+nu`, `V=G0+Z`, `L=q+1`.

K0 is a local comparison quantity, NOT the normalizer K=D(c). In X coordinates the actual target is

`D=(X-1)(X²+8/9)²`,

`Q=X²+(p-2)X+Cbar-a`.

Its X7,...,X3 coefficients are

`1, p-3, Cbar-a-p+chi, nu(p-3)-Cbar+a,`

`nu(Cbar-a-p+2)+rho`.

The entire baseline principal product is

```
a_R a_S=X6+q X5+(epsilon-M)X4
 -(G0+U+Z+epsilon*Abar)X3
 +(Abar*U-Z-epsilon*G0)X2
 +(Abar*Z+G0*U)X+G0*Z.
```

Subtracting with k=p-q-3 and collecting gives EXACTLY

```
R5=L*p-L²-chi-(M-a)-Cbar,

T4=q*Cbar-[K0+q(q-1)]p
       +(q+3)M-q*a+(q-2)U-V+F(q),

F(q)=nu(q+2)+q³-q.                                     (E1)
```

For later reconstruction one may first take

```
R3=Abar*U-Z-epsilon*G0
    -k(G0+U+Z+epsilon*Abar)
    -nu(Cbar-a-p+2)-rho.
```

Then S=R3+M R5 collects to

```
S=[nu+2M+(q-2)U-V]p-K0*Cbar
   +Abar*U-M²+K0*a-(nu+6)M+(6-q-q²)U
   +4G0+(q+2)Z-(2nu+rho).                              (E2)
```

These are actual coefficient identities, not a free polynomial pretending to be a generator.

R5≥0 and Cbar,M-a≥0 imply

`p>=L+chi/L>q+2`,

because chi>q+1 on[1,2]. Compare the UPPER Cbar bound from R5≥0 with the LOWER one from T4≥0. Multiplying the first by q>0 and collecting yields

```
H(p-q-2)>=q(a+nu)+epsilon*eta+U+Gamma+Z,
H=2q-nu-M.                                             (H)
```

For direct verification, the upper-minus-lower expression at p=q+2 is precisely the NEGATIVE of the displayed right side. Its right side is strictly positive, since q*nu>0. Therefore H>0, and

`M<2q-nu`,

`p>=P(q):=q+2+nu*q/(2q-nu)`.

The denominator is positive since q≥1 and nu<2. Furthermore

`P(q)-(2nu+2)=2(q-nu)²/(2q-nu)>=0`.

Hence every putative solution must have

`p>=50/9`.                                             (P)

At q=1 the exact bound is11; at q=2 it is28/5. Thus the old11 bound does NOT transfer to this unequal family. All new signs/bounds were derived rather than silently inherited.

## 7. Substituting the correct LOWER input bound

Because q>0, T4≥0 gives

```
Cbar >= { [K0+q(q-1)]p-(q+3)M+q*a
             -(q-2)U+V-F(q) }/q.                       (CL)
```

The coefficient of Cbar in(E2) is-K0<0, so substituting this LOWER bound gives an UPPER bound on S. Exact collection produces

```
S <= -D0(M,q)*p + Abar*U + (3/q)M²+A1(q)M+A0(q)
   +(2-q)[q+3-K0/q-p]U
   +[4-K0/q-p]G0+[q+2-K0/q-p]Z,                       (S1)

D0(M,q)=K0²/q-(3-q)M-(2-q)nu,
A1(q)=q²-7+nu+5nu/q,
A0(q)=nu*q²-80/27+512/(81q).
```

To verify the coefficients without a symbolic program: the M² term comes from-M²+((q+3)/q)M²; the M coefficient is-6+3nu/q+nu+2nu/q+q²-1; and the constant is nu²(1+2/q)+nu(q²-1)-(2nu+rho). These simplify to exactly the displayed A1,A0. The coefficient of U factors because6-q-q²=(2-q)(q+3). Gamma/return quantities are still the actual nonnegative G0,Z, not invented signs.

The p coefficient has the needed strict sign:

```
q*D0=M²+(q²-3q+2nu)M+nu(q²-2q+nu),
q²-3q+2nu=(q-3/2)²+47/36>0,
q²-2q+nu=(q-1)²+7/9>0.
```

Thus D0>0. It is legitimate to use the LOWER bound(P) only after establishing this sign.

The three remaining bracket terms in(S1) are nonpositive:

- p≥50/9>4 makes4-K0/q-p<0.
- p≥P(q)>q+2 makes q+2-K0/q-p<0.
- For the U bracket,

`q+3-K0/q-p <=1-nu/q-nu*q/(2q-nu)<0`,

because nu/q≥nu/2=8/9 and nu*q/(2q-nu)>nu/2. Also2-q≥0. Hence its entire U term is≤0.

All internal returns remain nonnegative: in particular Z=w+epsilon*u≥0 uses the CHOSEN q≥1 range. We do not claim this deletion remains valid at q<1.

Drop these nonpositive terms and use Abar*U≤M²/4. Then

`S <=-D0*p+(3/q+1/4)M²+A1(q)M+A0(q)`.                  (S2)

## 8. Three exact scalar bounds give a UNIFORM strict contradiction

Insert p≥50/9 in the NEGATIVE term of(S2), using D0>0. Regard the resulting expression as a quadratic in M≥0.

Its M² coefficient is

`1/4-23/(9q)<=-37/36<0`.

For its M coefficient, multiplication by the positive81q gives

```
P1(q)=81q³-450q²+927q-880
     =-178+(q-2)[81(q-16/9)²+95] <=-178<0.              (C1)
```

Thus that coefficient is strictly negative on the ENTIRE closed interval, not just at endpoints.

For its constant coefficient, multiplication by the positive729q gives

`P0(q)=1296q³-7200q²+12240q-8192`.

Let r=q-1∈[0,1]. Its exact expansion and bound are

```
P0=-1856+1728r-3312r²+1296r³
  <=-1856+1728r-2016r²
   =-2016(r-3/7)²-10400/7 <0.                          (C0)
```

The only inequality used is r³≤r² on[0,1]. This proves the constant coefficient strictly negative as well, including q=1 and q=2.

Therefore the upper bound in(S2) is STRICTLY NEGATIVE for every M≥0, even if M=0. It contradicts the ACTUAL feedback identity S≥0 in(G). No characteristic/numerator match is possible anywhere in the new q∈[1,2] class. The proof includes every internal/cross-feedback zero boundary, every input-zero boundary and both holding endpoints. No numerical evaluation, finite testing, trace screen or hidden-root discriminant was used.

## 9. Actual PH input/exit law and general d scaling

The initial/exit normalization was not lost by treating a spectrum as a PH pair. If a successful raw candidate were positive and G-cI Hurwitz, every phase would reach the sole raw exit via the designated positive path; h0=(-(G-cI))^(-1)gamma would be strictly positive. The normalized Tph,alpha,omega described in §4 would satisfy ALL row sums, initial mass1 and the exact target law. This proves the transfer-to-PH bridge for any candidate in the class, while the polynomial contradiction says none succeeds.

Conversely, positive designated forward rates can be unit-normalized by a positive diagonal raw-coordinate change. Diagonals/holding rates remain unchanged, and all backward coefficients stay nonnegative. This is NOT an assertion that an arbitrary diagonal similarity preserves PH row sums: raw input/output positivity is what is needed for the necessary coordinate change. Relative degree5 forces the upstream third input positive in this path arrangement, even with h shortcut; positive reciprocal boundary scaling sets beta3=1 and gamma7=K. The actual adjugate leading coefficient is then exactly K.

For arbitrary d>0 rescale time to d=1,c to c/d. The excluded physical holding pattern is upstream offsets d,d,2d and downstream offsets d,d,qd from the dominant pole c, q∈[1,2], in this specified3+3 arrangement. All positive path rates and all internal returns are included through the stated raw normalization. No such holding pattern or upstream-exit pattern is declared WLOG for arbitrary PH7.

## 10. Genuine advance relative to the equal-downstream theorem

This is NOT feedback redistribution inside the old class: the downstream principal characteristic gains epsilon X², its cofactor row gains epsilon X,epsilon, and its constant return combination becomes Z=w+epsilon*u. The trace shifts to ell=p-q-2. The old second cone identity is replaced by R4-epsilon R5>=0, with a changed lower input bound and changed forced regime. The uniform p bound is50/9, not11, and M may now lie below2q-16/9 rather than2/9.

The new all-q scalar bounds(C1)/(C0) and strictly signed p substitution are what close this enlarged unequal-holding regime. They were derived from the SAME actual matrix, numerator and fifteen feedback generators. It is not an isolated q=2 tuple or a restatement of the q=1 boundary. The q=1 overlap retains its earlier history, while q>1 is new primary mathematics.

## 11. ENTIRE exact residual and first unproved arbitrary-topology step

The theorem settles only the specified unequal family(1,1,q),q∈[1,2], with upstream(1,1,2), one upstream exit e3, one downstream entry e1 and final exit at phase7. Still unexcluded are:

1. General unequal downstream triples, especially changes in the first two downstream holdings; q<1 or q>2 is also outside this argument.
2. Simultaneous other upstream holding patterns, including varying the third upstream rate while downstream holdings vary.
3. Multiple upstream exits into the central phase, or upstream graphs lacking the designated positive path ending at that exit.
4. Other initial/exit arrangements, complete degree allocations and the other normal-form/time-reversal representatives.

The internal-edge, raw-input and r/f/Dback freedoms quantified here are NOT still open within this class. The first remaining actual step is a common-matrix witness outside the four restrictions above, or a justified reduction covering those mechanisms; no such reduction is asserted. Negative coefficients in a translated scalar polynomial or a mere hidden spectral pair still do not constitute a witness or an arbitrary-topology contradiction.

Unrestricted8/9 therefore remains NOT_PROVED and minimum remains{7,8} at its retained B6/upper8 imports. Neither import is a premise of this new algebraic contradiction. This manuscript is a new WRITTEN candidate awaiting complete independent reconstruction, not parent/formal/kernel/human/cross-vendor/configured-family/executable/novelty acceptance. Original deadline/new-science cutoff and HOLD remain unchanged; V11 is only a later evidence overlay, never new permission or backdated freeze content.
