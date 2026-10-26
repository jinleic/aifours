# Above z=1/2, any PH7 realization must be irreducible: an all-topology SCC obstruction

Status: WRITTEN AUTHOR CANDIDATE, requiring a fresh complete reconstruction. Actual pre-write `/bin/date` returned `Sun Oct 25 12:59:20 PDT 2026`. Same original102319 PH primary, original cutoff/deadline and HOLD v2/v9/v10/v11. The actual v84-B privacy review was returned to Main before the separate post-v84 primary-resumption ACK and this body. No scientific interpreter/program, symbolic calculation, enumeration, solver, replay, kernel check or nested agent.

## 1. Exact new exclusion and the still-open original point

For c,d>0, b_pole>0, z=b_pole^2/d^2, consider the SAME original law

`H(s)=K/[(s+c)((s+c+d)^2+b_pole^2)^2]`,

`K=c[(c+d)^2+b_pole^2]^2`.

THEOREM CANDIDATE. If z>1/2 and an ACTUAL PH realization of H has at most7 transient states, it has exactly7 states and its whole transient off-diagonal graph is strongly connected. In particular EVERY actual PH7 at z=8/9 must be irreducible, irrespective of holdings, initial/exit support, principal blocks, feedback layout or dominator allocation.

Additional necessary consequences: every physical holding rate is strictly greater than c, and the two cancelled roots in the shifted characteristic lie strictly in the left half-plane. In dimensionless y=s+c coordinates the hidden quadratic is y^2+p y+q with p,q>0. These are consequences, not assumptions used to reject reducible tuples.

This closes the ENTIRE reducible/zero-shifted-upstream-phase mechanism, not just another selected holding interval. It does NOT exclude irreducible PH7. No PH7 witness at8/9 or all-topology empty-intersection certificate is supplied; the unrestricted minimum there remains{7,8} at the retained lower/upper boundaries. No new exact-band endpoint or book solution follows.

The pure6x6 matrix barrier below is reconstructed EXPLICITLY. It is NOT inferred merely from the old B6 PH-transfer theorem: that inference would not be justified for an arbitrary principal spectrum. Its lineage is `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`, whose complete195-LF body has been read, including fresh proof components LF1-138 and139-195. No B6 upper construction, old arithmetic output, unreviewed time-reversal reduction or selected quotient is a correctness premise here. The centered moment argument and all model-specific transfer/SCC steps are given in full.

Classical imports are ordinary real/complex linear algebra, the symmetric spectral theorem and compact Lagrange-multiplier argument, Perron–Frobenius for nonnegative/irreducible Metzler matrices and their positive semigroups, and elementary integration/positive matrix-exponential path expansion. Their general theories are not formalized here. No novelty or priority claim is made for the moment/spectral mechanisms or their PH consequence.

## 2. Actual PH trimming, characteristic AND numerator binding

It suffices to prove the theorem for d=1 by the actual time change T->T/d, with c->c/d and b_pole->b_pole/d. This does not change the graph, PH order or proper initial/exit normalization. Write

`D_z(y)=y[(y+1)^2+z]^2`, `H(s)=K/D_z(s+c)`.

Start with a proper PH pair(alpha,T) of order at most7: T is Hurwitz Metzler, omega=-T1>=0, alpha>=0 and alpha1=1. Remove states unreachable from alpha's positive support. The reachable set is closed under outgoing positive transient edges, so its restricted generator has the SAME row sums/exits, initial mass1, stability and exact transform. Let its actual dimension be n<=7. Every remaining phase reaches a positive exit: otherwise a final nonabsorbing communicating class would contradict Hurwitz transience.

Set G=T+cI on this reachable subsystem. The actual adjugate formula and the original equality give

```
P_n(y)=det(yI-G),
N_n(y)=alpha adj(yI-G)omega,
N_n(y)D_z(y)=K P_n(y).
```

Since K is a nonzero constant and D_z is the reduced target denominator, there is a REAL MONIC polynomial Q_n such that

`P_n=D_z Q_n`, `N_n=K Q_n`, `deg Q_n=n-5`.              (T)

In particular n>=5. These are the SAME characteristic AND actual input/exit numerator, including accidental common factors. We do not place a freely selected hidden polynomial in a chosen principal block.

The exact target density asymptotic is

`f(t)=[K/(1+z)^2]exp(-ct)+O(t exp(-(c+1)t))`.

Every dominant irreducible block is initial-reachable and exit-co-reachable. At a fixed positive pre/post time tau, the restricted vectors alpha exp(T tau) and exp(T tau)omega are strictly positive there. Paths confined to it and a positive Perron vector bound f(t+2tau) below by a positive constant times exp(rho t). Thus rho>-c contradicts the displayed exact asymptotic. Since -c is an actual pole, it is an eigenvalue. Hence

`spectral abscissa(G)=0`.                             (PF)

This is a positivity/reachability statement, not an assumption that every characteristic mode is observable. Every principal SCC block has spectral abscissa at most0.

## 3. Centered-Metzler third moment, proved at its needed scope

Let X be ANY real6x6 Metzler matrix with tr X=0. Put tau2=tr(X^2)>=0. Define symmetric S by

`Sii=Xii`, `Sij=Sji=sqrt(Xij Xji)` for i!=j.

Then tr S=0 and tr(S^2)=tau2. In the cubic traces, diagonal terms and terms with exactly two distinct indices agree. For each unordered triple, put A=Xij Xjk Xki>=0 and B=Xik Xkj Xji>=0. The contributions are3(A+B) for X and6sqrt(AB) for S, so AM-GM gives

`tr(X^3)>=tr(S^3)`.

This remains true with arbitrary REAL centered diagonals, zero edges and reducibility; X need not be entrywise nonnegative.

For the six real eigenvalues of S, normalize their square sum to1 if tau2>0 and minimize their cube sum on the compact zero-sum unit sphere. Lagrange multipliers give3r_i^2=lambda+2mu r_i, so there are exactly two distinct values at a minimum. If the negative value has multiplicity k, the constraints give

`negative=-sqrt((6-k)/(6k))`,

`positive=sqrt(k/(6(6-k)))`,

and cubic sum(2k-6)/sqrt(6k(6-k)). For k<=3 its most negative value occurs at k1, since k(6-k) is then minimal; k>=3 cannot improve the negative minimum. Thus the minimum is-4/sqrt30. Rescaling gives

`tr(X^3)>=-(4/sqrt30)tau2^(3/2)`.                      (M6)

If tau2=0, S=0 and the preceding comparison gives the same conclusion. This supplies the pure matrix inequality without any PH-transfer import.

## 4. Pure6x6 spectral obstruction, not a PH theorem substituted for one

CLAIM M6S. No real6x6 Metzler matrix can have spectrum

`0, -d+i beta twice, -d-i beta twice, -v`,

where d>0,v>=0 and beta^2>d^2/2. Algebraic multiplicities are meant; no diagonalizability is assumed.

Suppose such a matrix B exists. Put

`h=(v-2d)/6>=-d/3`, `Delta=beta^2-d^2/2>0`,

`X=B+(d+h)I`.

Its centered eigenvalues are d+h,-d-5h,h+i beta twice,h-i beta twice. Consequently

```
tau2=12dh+30h^2-4Delta,
tau3=-12h R,
R=(3/2)d^2+6dh+10h^2+Delta.
```

The first trace is nonnegative for a Metzler matrix because it is a squared-diagonal sum plus nonnegative reverse-edge products. For-d/3<=h<=0 the term6h(2d+5h) is nonpositive, so Delta>0 makes tau2 negative. Hence h>0 and R>0.

M6 gives12hR<=(4/sqrt30)tau2^(3/2). Tau2=0 is already impossible since tau3<0, so squaring is legitimate and gives EXACTLY

`tau2^3>=270h^2 R^2`, since `12^2*30/16=270`.

Put tau20=6h(2d+5h) and R0=(3/2)d^2+6dh+10h^2. Then tau2<=tau20 and R>=R0. Direct multiplication gives

```
270h^2 R0^2-tau20^3
 =54h^2[(45/4)d^4+58d^3h+90d^2h^2]>0.
```

For a transparent expansion, the bracket is5R0^2-4h(2d+5h)^3: its d^3h coefficients subtract90-32=58, its d^2h^2 coefficients subtract330-240=90, and its dh^3,h^4 coefficients cancel. Thus tau2^3<=tau20^3<270h^2R0^2<=270h^2R^2, a contradiction.

This proves M6S for EVERY such Metzler matrix, not just a spectrum asserted to come from a PH6 numerator. The strict beta^2>d^2/2 boundary is essential; the old half endpoint is not excluded here.

## 5. Every possible proper SCC carrying the visible poles is excluded

Normalize d=1 as above and write beta=sqrt z. All SCCs below are the ACTUAL irreducible blocks of the whole G, not the arbitrarily selected upstream/downstream principal blocks of a feedback interconnection. Their characteristic polynomials really multiply to P_n.

A block of size1 has only a real eigenvalue. A real2x2 Metzler block has real eigenvalues, since its discriminant is a squared diagonal difference plus a nonnegative opposite-edge product. A3x3 Metzler SCC containing -1±i beta has a real Perron third eigenvalue -u. By(PF) and Perron dominance,0<=u<=1. Nonnegative reverse-edge products and diagonal Cauchy imply

`u^2+2(1-z)=tr(B^2)>=sum Bii^2>=(u+2)^2/3`.

Therefore `(u-1)^2>=3z`, impossible when z>1/2. So EVERY SCC containing even ONE visible conjugate pair has at least4 states.

The two visible copies cannot lie in distinct SCCs: those would require at least8 states, while n<=7. Thus ONE SCC contains the conjugate pair with algebraic multiplicity at least2. Any extra coincidence from Q_n only increases that requirement, never reduces it.

Such a block cannot have size4: its four visible nonreal eigenvalues would leave no real Perron eigenvalue. If its size is5, its remaining eigenvalue is its real Perron -u with0<=u<=1. The same trace comparison gives

`u^2+4(1-z)>=(u+4)^2/5`, hence `(u-1)^2>=5z`.

Again impossible for z>1/2.

If its size is6, its two remaining eigenvalues must be REAL: one is the real Perron eigenvalue, and reality of its polynomial makes the last remaining root real too. Write them-u,-v with v>=u>=0. Irreducible Metzler strict Perron dominance over the nonreal roots gives u<1. Shift this ACTUAL block by uI. Its spectrum is

`0, -(1-u)±i beta each twice, -(v-u)`.

Here d'=1-u>0,v'=v-u>=0, and beta^2>(d')^2/2 because beta^2=z>1/2 and d'<=1. M6S excludes it uniformly, including every possible hidden real pair and every holding/internal-edge arrangement. If both extra roots had instead been nonreal there would be no real Perron root, already impossible.

Thus the SCC containing the two visible copies has at least7 states. Since n<=7, it has EXACTLY7 and is the WHOLE reachable matrix. No phase could have been removed from the original at-most7 realization either. This proves the theorem: order is7 and the full actual graph is irreducible.

This is an all-topology reducible-branch exclusion tied to the original transfer/pole multiplicities and proper PH normalization. It is not a trace-screen rejection of a selected tuple elevated to an original-point no-go. The entire remaining irreducible7-state feasibility problem is still present.

## 6. Strict holdings, hidden-root stability and actual Perron coordinates

For the full irreducible G with spectral abscissa0, Perron–Frobenius gives v>0,Gv=0, with simple0 and every other eigenvalue strictly in the left half-plane. Each row has a positive off-diagonal entry because its graph is strongly connected and has more than one state. Therefore

`Gii v_i=-sum_(j!=i)Gij v_j<0`.

Hence Gii<0 for EVERY i, equivalently the physical holding rate-Tii is strictly greater than c. A chosen zero-shifted-holding upstream phase cannot be repaired by changing other coefficients: that entire reducible/Perron mechanism is now excluded uniformly.

At n7 the ACTUAL identities(T) have monic quadratic Q. The simple Perron0 cannot be a root of Q, and all its roots have strictly negative real parts. Thus, in y coordinates,

`Q(y)=y^2+p y+q`, `p>0`, `q>0`,

whether its roots are real or nonreal. No particular hidden pair or discriminant was fixed.

There is a useful EXACT change of raw coordinates, not a positive quotient. Let S=diag(v). Then

`L=S^(-1)GS`, `L1=0`,

`beta=alpha S>=0`, `gamma=S^(-1)omega>=0`.

The SAME transfer is beta((s+c)I-L)^(-1)gamma. The row budget of L is exactly conservative. But this is a RAW positive realization: gamma need NOT equal c1, and beta need NOT have mass1. Claiming otherwise would falsely assert arbitrary diagonal similarities preserve the physical PH row/exit ties.

The proper normalizer is h=S^(-1)1>0. It satisfies(L-cI)h=-gamma and beta h=1, and its positive diagonal normalization restores the original actual PH pair. Conversely, any irreducible conservative7x7 Metzler L with nonnegative beta,gamma realizing the exact target raw transform has h=(cI-L)^(-1)gamma>0 and beta h=H(0)=1; scaling by diag(h) gives a proper PH realization with all actual row/initial/exit ties. This is a construction coordinate system for the surviving problem, NOT an already feasible witness or a quotient-cone assumption.

The original relative degree is also retained. From the exact SAME input/output transfer,

`alpha G^k omega=0 for k=0,1,2,3`, `alpha G^4 omega=K>0`.

Shift G by a sufficiently large scalar times I to a nonnegative matrix. The same zero prefix and positive fourth term persist by the binomial expansion. Positive walk expansion then gives shortest input-to-exit off-diagonal path length EXACTLY4. A fourth walk using a diagonal hold would imply a shorter positive path, which the zero prefix forbids. These input/output identities are not discarded in the new raw conservative representation.

## 7. Exact residual and assurance

No model-specific correctness import is hidden in the pure matrix/SCC proof: the needed centered-Metzler inequality,6x6 barrier, proper-transfer binding, reachability/Perron argument and every block-size case are supplied above. The old B6 source is the disclosed lineage, not an automatic review of this new SCC consequence. The generic PF/symmetric-spectral/elementary-calculus facts remain the explicitly named classical boundary. No computational output is used.

For z=8/9 the new uniform conclusion is ONLY: every possible PH7 is irreducible, all physical holdings exceed c, its hidden quadratic is strictly stable in shifted coordinates, and the exact conservative raw-coordinate problem is equivalent with actual normalization. Arbitrary irreducible principal/input/exit couplings, arbitrary shifted positive holdings, all dominator allocations and all allowed feedback remain unresolved. The prior583-LF selected holding-simplex candidate is preserved but is not a correctness premise here or an all-topology solution.

The retained pointwise upper8 source is `proof-eight-state-cubic-cancellation-v1.md`, SHA256 `e110dd1fa23bdec2f7a2498e98b3dbfe31a645496f2f94641a97e3599b7b137a`; its theorem is background, not newly reconstructed here. With the lower bound7, the actual unrestricted minimum at8/9 is still{7,8}. This packet does not decide it or the full existence band.

This is a substantive global branch closure plus a documented replacement for the zero-upstream-phase witness direction, not a terminal gate/park. It requires a fresh complete written review before parent support. WRITTEN is not formal/kernel, human/configured-family, executable, novelty or publication acceptance. No new book/discovery count, historical arithmetic credit, scientific GO or deadline change is claimed. The primary continues in the surviving irreducible actual-input/exit problem.
