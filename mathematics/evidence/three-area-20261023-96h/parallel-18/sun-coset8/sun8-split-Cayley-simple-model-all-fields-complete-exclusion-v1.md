# Sun8 direct P7 — the split-Cayley AUTOMORPHISM simple model over ALL finite fields

Owner MathSun8-2. Actual pre-write observation: `Mon Oct 26 10:56:36 PDT 2026`.
**NEW WRITTEN CANDIDATE; unreviewed/unadopted.** Every algebra/field/group/matrix/weight/factorization identity below is written exact arithmetic. No interpreter, calculator, scientific program, group enumeration, primality program, solver or replay was used.

## 1. Exact model, theorem and supported input cut

Let q=p^f>=2. Define the split Zorn algebra O over F_q to consist of `(a,x;y,b)`, with a,b in F_q and x,y in F_q^3, with identity `(1,0;0,1)` and multiplication

`(a,x;y,b)(c,u;v,d)=(ac+x.dot(v), a*u+d*x-y.cross(v); c*y+b*v+x.cross(u), bd+y.dot(u))`.

Dot and cross are the ordinary coordinate dot product and determinant cross product, valid also in characteristics two and three. Let G be the FULL group of F_q-linear, identity-preserving algebra automorphisms of this explicit algebra. **Assume G is NONABELIAN SIMPLE.** This is the actual model/hypothesis, not a classification of simple groups or a theorem that this group is simple for every parameter. In particular no assertion identifies an exceptional small DERIVED group at q=2 with this full automorphism model or with a unitary group.

**Theorem CAY.** G supports NO direct P7 family of EIGHT actual nonempty pairwise-disjoint LEFT cosets with ALL original indices `7r_l`, positive pairwise-coprime private r_l, including the possible private-seven owner and all powers.

The only special direct-mathematics input is the ENTIRE supported 178-LF rank-free Gram/Farey theorem SHA256 `76aa8a6fbfd6a2fcf4587ca5bec29e14215bcdfd5ec81dd47f56de9c4ea60e15`: three actual P7 cosets supply SOME nontrivial irreducible of degree d<=1728, not a bound on the full orbital module. Simplicity makes it faithful. The complete parent76 SHA256 `9dbce6f9b7afab2fc0c9e35dbb0034ff47f45c0cb3d8e40ab4c3f739c34ff726` was actually read and supplies this exact ordinary-written cut. All automorphism/order/transitivity/root/weight/finite-field claims for this model are reconstructed below, not a G2 order/character/subgroup catalogue import.

For arbitrary-original-group application also supply the ENTIRE supported 88-LF normal-section source SHA256 `b401c139141c451755174f8151942b86916e5677f734715ede48299394716202`. Its actual simple factor with eight own-label private divisors cannot be this model if the new theorem passes its whole gate. No CFSG, Lie simplicity, Borel–Tits, Chevalley commutator table, Jordan, Stone–von Neumann or unadmitted historical computation is used.

## 2. Exact idempotent set and its cardinality

Put `Tr(X)=a+b`, `N(X)=ab-x.dot(y)`. Direct multiplication gives the ENTIRE identity

`X^2-Tr(X)X+N(X)I=0`:

the diagonal entries of X^2 are a^2+x.dot(y), b^2+x.dot(y), and the off-diagonal vectors are `(a+b)x,(a+b)y`, since a vector's cross product with itself is zero. A NONTRIVIAL idempotent is nonscalar, so this identity and X^2=X force Tr(X)=1,N(X)=0; conversely those two equations imply X^2=X. Thus the nontrivial idempotents are EXACTLY

`b=1-a`, `x.dot(y)=a(1-a)`.

For a=0 or1, the number of pairs with dot product zero is

`q^3+(q^3-1)q^2=q^5+q^3-q^2`.

For each other a it is `(q^3-1)q^2=q^5-q^2`. Consequently the total is

`2(q^5+q^3-q^2)+(q-2)(q^5-q^2)=q^6+q^3=q^3(q^3+1)`.

These are actual algebra elements; no unsupported Peirce-transitivity assertion has yet been made.

## 3. Exact stabilizer and three explicit types of algebra automorphisms

Let `e_+=(1,0;0,0)`, `e_-=I-e_+`. An automorphism fixing e_+ fixes e_- and preserves the actual three-dimensional subspaces U of pure upper vectors and V of pure lower vectors, obtained by the indicated left/right multiplications by e_+,e_-. The product of upper x and lower y is `(x.dot(y))e_+`, so if its action on U is A, its action on V must be A^(-T). The product of two upper vectors is their lower cross product. The elementary determinant identity

`(A x).cross(A u)=det(A) A^(-T)(x.cross(u))`

therefore forces det(A)=1, since cross products span F_q^3. Conversely dot and both cross products show that EVERY A in SL_3(q) acts by

`(a,x;y,b)->(a,A x;A^(-T)y,b)`.

This proves the FULL stabilizer of e_+ is EXACTLY this embedded SL_3(q), not merely that it contains such a subgroup. The representation is injective on that subgroup.

Direct substitution in the Zorn product also proves the automorphism

`Theta(a,x;y,b)=(b,-y;-x,a)`.

For example its upper cross term is `-x.cross(u)`, precisely the upper term obtained after the swap; the lower becomes `+y.cross(v)`. The diagonal dot terms are unchanged. Theta squares to identity and swaps e_+,e_-.

For a third class of explicit automorphisms, let Q be the subalgebra with vectors only in coordinate1, identified with Mat_2(F_q), and put `l=(0,e_2;e_2,0)`. Direct multiplication gives l^2=I and the vector-space decomposition `O=Q+Ql`. If `B=[[c,u],[v,d]]` in Q, then B*l has upper vector `(0,c,-v)` and lower vector `(0,d,u)`, with zero scalar entries. Thus for Q-matrices A,B,C,D the FULL product in these coordinates is

`(A+B*l)(C+D*l)=(AC+bar(D)B)+(DA+B bar(C))*l`,

where `bar(C)=trace(C)I-C` is the 2-by-2 adjugate. This is a generic identity in the displayed Zorn coordinates, not an imported doubling theorem. To make coefficient tracing explicit, with `A=[[a,x],[y,b]], B=[[c,u],[v,d]], C=[[e,z],[w,f]], D=[[g,s],[t,h]]`, its first matrix has entries

`ae+xw+ch-vs; az+fx-ds+uh; ey+bw-ct+vg; bf+yz+dg-ut`,

and its second matrix has entries

`ag+ys+fc-uw; eu+bs+xg-cz; at+yh+fv-dw; ed+bh-vz+xt`.

They are respectively `AC+bar(D)B` and `DA+B bar(C)` by ordinary matrix multiplication. Therefore for ANY P in GL_2(q), simultaneous inner conjugation

`A+B*l -> P A P^-1+(P B P^-1)*l`

is an ACTUAL automorphism: conjugation preserves products and the adjugate, so it preserves both displayed components. No determinant restriction on P or unprovided Cayley-basis extension is needed.

## 4. A full short-root formula, valid in EVERY characteristic

Take `P_t=[[1,t],[0,1]]` in §3 and then compose its automorphism with the embedded SL_3 matrix `I+tE_(2,3)`. Using the Q/Ql coordinates just given, the resulting ACTUAL automorphism X_1(t) is

`a'=a+t y_1`, `b'=b-t y_1`,

`x_1'=x_1+t(b-a)-t^2 y_1`, `x_2'=x_2`, `x_3'=x_3`,

`y_1'=y_1`, `y_2'=y_2+t x_3`, `y_3'=y_3-t x_2`.

Indeed inner conjugation first changes x_2 to x_2-t x_3 and y_3 to `y_3+t(y_2-x_2)+t^2x_3`, with y_2 to y_2+t x_3; the SL_3 factor cancels exactly those unwanted x_2/y_2 terms. This proves the full formula, not just its first-order part. It also proves `X_1(s)X_1(t)=X_1(s+t)`: the new x_1 cross term is `-2st y_1`, giving exactly `-(s+t)^2 y_1`. There is no division by2 here.

Cyclic coordinate conjugation in SL_3 gives X_2,X_3. Put `Y_j(t)=Theta X_j(t)Theta`. In particular

`Y_3(t): a'=a+t x_3, b'=b-t x_3, x_1'=x_1+t y_2, x_2'=x_2-t y_1, x_3'=x_3, y_1'=y_1, y_2'=y_2, y_3'=y_3+t(b-a)-t^2x_3`.

These are genuine algebra automorphisms in small characteristics as well. No Chevalley root-group existence theorem or symbolic-program calculation has been substituted.

## 5. Complete transitivity on idempotents, including q=2

First q>=3. If x=0,y!=0 use Theta so x becomes nonzero. SL_3 can send any x!=0 to e_1 by extending x to a determinant-one basis. The first y-coordinate then equals x.dot(y)=a(1-a).

If a is NOT0 or1, that coordinate is nonzero. The determinant-one stabilizer of e_1 contains matrices `[[1,c],[0,I_2]]`; its inverse-transpose action subtracts arbitrary multiples of y_1 from the other y-coordinates. Thus it sends y to `a(1-a)e_1`. The full idempotent now lies in Q=Mat_2 and is rank one of trace one. An inner GL_2 conjugation sends any such projector to e_+ by choosing its image and kernel as a basis.

If a is0 or1, after normalizing x=e_1 its Q-component is `[[a,1],[0,1-a]]`, also a rank-one idempotent. Choose t outside {0,1}; the rank-one projector `[[t,1],[t(1-t),1-t]]` is GL_2-conjugate to it. Apply the simultaneous Q/Ql automorphism of §3. The Ql-component stays in Ql and cannot affect the scalar coordinates, so the resulting full idempotent has scalar a=t. It is now the preceding generic case. If x=y=0 the idempotent was e_+ or e_-, already connected by Theta. This proves ALL transitivity for q>=3, not just a generic open subset.

At q=2 the preceding choice of t is NOT available. Instead a is0 or1 and x.dot(y)=0. For a fixed a there are FOUR coordinate types: both zero; upper only; lower only; both nonzero and orthogonal. SL_3(2) is transitive on each nonzero type. For the last, send x to e_1 and use the embedded SL_2(2) on the other two coordinates to send the nonzero remaining covector to e_2.

Starting at e_+ with a=1, the actual X_1(1) and Y_1(1) give respectively upper-only and lower-only types. Applying Y_2(1) after X_1(1) gives `x=e_1,y=e_2,a=1`, the both-nonzero orthogonal type. Theta gives the four a=0 types. Thus all `2(1+7+7+21)=72` idempotents are in one ACTUAL orbit. This is a four-case coordinate-orbit proof, not a scientific enumeration of groups or coset witnesses.

Orbit-stabilizer and §2/§3 now prove for EVERY q>=2 the ENTIRE order formula

`|G|=q^3(q^3+1)*|SL_3(q)|=q^6(q^6-1)(q^2-1)`.

Here `|SL_3(q)|=q^3(q^3-1)(q^2-1)` follows by counting ordered bases for GL_3 and dividing by its onto determinant map. No transitivity, order table, simple-model identification or unprovided theorem is assumed in this formula.

## 6. First faithful-degree lower bound, ALL characteristics

Inside the exact SL_3 stabilizer is the ACTUAL additive group

`R={I+aE_(1,2)+bE_(1,3): a,b in F_q}` of order q^2.

The SL_2(q) block on coordinates2,3 normalizes R and acts transitively on its nonzero characters. Indeed identify its characters with F_q^2 using a fixed pth root of unity and the field trace. That trace is nonzero: its polynomial has degree less than q and leading coefficient one, so cannot vanish on all of F_q; it is onto F_p. The determinant-one block is transitive on nonzero dual vectors, by extending a nonzero vector to a determinant-one basis.

A faithful complex representation of G is nontrivial on R, so at least one nonzero R-character occurs and then ALL q^2-1 occur. Thus `d>=q^2-1`. Under direct P7, the supported small constituent is faithful by simplicity, giving

`q^2-1<=1728`, hence `q<=41`, since `42^2-1=1763>1728`.

This bound does not restrict the entire permutation module, only the faithful constituent actually supplied by the full rank-free theorem.

## 7. Full contact-group bound in characteristic at least five

We now prove a stronger bound for p>=5 without invoking a character table or a Heisenberg classification. In the SL_3 stabilizer let L_ij(t)=I+tE_(i,j), acting on upper x and inverse-transpose on lower y. Consider the FIVE actual groups

`L_12(a), L_23(b), X_1(s), Y_3(t), Z(c)=L_13(c)`.

The ENTIRE commutator table is

`[L_12(a),L_23(b)]=Z(ab)`, `[X_1(s),Y_3(t)]=Z(-3st)`,

with every other pair commuting and Z central. Here is a traceable derivation of the only less immediate coefficient, not a copied Chevalley constant. From §4 write `X_1(s)=I+sD+s^2D^2/2`, `Y_3(t)=I+tE+t^2E^2/2`. Their displayed coordinates give D^3=E^3=0, and

`DE-ED` sends `x_1 -> -3x_3`, `y_3 -> 3y_1`, all other output coordinates to zero.

Thus `DE-ED=-3F`, where F is the linear part of Z. Directly F annihilates D,E on BOTH sides. Consequently D^2 commutes with E, E^2 commutes with D, and expansion gives

`X_1(s)Y_3(t)=Z(-3st)Y_3(t)X_1(s)`.

For further coefficient tracing, DE sends x_1 to -2x_3 and y_3 to y_1, whereas ED sends x_1 to x_3 and y_3 to -2y_1. The long-pair coefficient is ordinary upper-triangular SL_3 multiplication. Each other mixed long/short derivative commutes, by the coordinate formulas in §4, hence so do its complete quadratic polynomials. These checks supply every table entry. Division by2 is legitimate ONLY in this p>=5 section; the p=2/3 cases below use §6 instead.

The table puts every word in a canonical five-parameter form. The scalar a-row's coefficients on y_1,x_3 recover s,t. After removing those groups, the remaining three upper SL_3 parameters are unique. Hence this is an ACTUAL subgroup of order q^5, not just five formal root labels. Its centre is exactly Z of order q: the two alternating commutator pairs have coefficients1 and -3, nonzero here. No additional central direction is hidden.

The subgroup A generated by L_12,X_1,Z is ABELIAN of order q^3 and normal in this contact group. Let psi be any occurring nontrivial character of Z in a faithful complex representation. On its weight space choose an occurring A-character chi. An element outside A has a nonzero L_23 or Y_3 parameter; commutation with L_12 or X_1 then ranges over ALL Z. It cannot fix chi. Thus the stabilizer of chi is EXACTLY A, and its contact-group orbit has q^2 distinct characters. Therefore each nontrivial central-character space has dimension at least q^2.

The embedded SL_3 torus `diag(z,z^-1,1)` normalizes this group and scales Z(c) by c->z*c for EVERY z in F_q^*. This scalar action is transitive on the q-1 nontrivial additive characters: a nontrivial character fixed by z!=1 would be trivial on `(z-1)F_q=F_q`. Faithfulness supplies at least one, so all occur. Thus

`d>=q^2(q-1)` for p>=5.

This proves the full bound with the SAME actual subgroup, centre and torus, without Stone–von Neumann or external root relations. Under d<=1728 it forces q<=12, since `13^2*12=2028>1728`. Hence the ONLY p>=5 fields are q=5,7,11.

## 8. The exhaustive forced small-field factor identities

For p=2, §6 leaves exactly q=2,4,8,16,32. For p=3 it leaves q=3,9,27. Together with §7 the ONLY possible fields are the following ELEVEN. These are forced by the universal inequalities, not chosen numerical trials, magnitude scouts or executed group enumeration.

Since `q^6-1=(q^3-1)(q^3+1)`, the following COMPLETE factor identities bound all prime owners of |G|. The only extra prime beyond the three factor columns is the characteristic prime from q^6.

|q|q^2-1|q^3-1|q^3+1|All possible prime owners of G|
|---|---|---|---|---|
|2|3|7|3^2|2,3,7|
|3|2^3|2*13|2^2*7|2,3,7,13|
|4|3*5|3^2*7|5*13|2,3,5,7,13|
|5|2^3*3|2^2*31|2*3^2*7|2,3,5,7,31|
|7|2^4*3|2*3^2*19|2^3*43|2,3,7,19,43|
|8|3^2*7|7*73|3^3*19|2,3,7,19,73|
|9|2^4*5|2^3*7*13|2*5*73|2,3,5,7,13,73|
|11|2^3*3*5|2*5*7*19|2^2*3^2*37|2,3,5,7,11,19,37|
|16|3*5*17|3^2*5*7*13|17*241|2,3,5,7,13,17,241|
|27|2^3*7*13|2*13*757|2^2*7*19*37|2,3,7,13,19,37,757|
|32|3*11*31|7*31*151|3^2*11*331|2,3,7,11,31,151,331|

For completeness the primality of every displayed factor is certified by the following written divisions, not a program. All are odd; 2,3,5 are prime. In each row r^2>ell, and the listed nonzero remainders cover ALL odd primes below r; thus no prime at most sqrt(ell) divides it.

|ell|r|odd-prime:remainder|
|---|---|---|
|7|3|none|
|11|4|3:2|
|13|4|3:1|
|17|5|3:2|
|19|5|3:1|
|31|6|3:1,5:1|
|37|7|3:1,5:2|
|43|7|3:1,5:3|
|73|9|3:1,5:3,7:3|
|151|13|3:1,5:1,7:4,11:8|
|241|16|3:1,5:1,7:3,11:10,13:7|
|331|19|3:1,5:1,7:2,11:1,13:6,17:8|
|757|28|3:1,5:2,7:1,11:9,13:3,17:9,19:16,23:21|

Each row is simply integer division with the displayed remainder; the factor products themselves reproduce q^2-1,q^3-1,q^3+1 in the first table. No unadmitted historical arithmetic or certificate is being counted. In ALL eleven cases |G|, and hence |G|/7 whenever P7 is assumed, has at most SEVEN distinct prime owners.

## 9. ALL eight original indices and finish

Each original r_l divides |G|/7 because its unchanged subgroup index 7r_l divides |G|. If all eight private r_l were nonunit, pairwise coprimality would assign them eight DISTINCT prime owners, contrary to §8. Therefore an ORIGINAL subgroup has index EXACTLY seven. No private-seven valuation was restricted; its owner was included in the same divisor argument.

The actual seven-point action of SIMPLE G is nontrivial and hence faithful. But §5's full order formula gives, for EVERY q>=2,

`|G|>=2^6*(2^6-1)*(2^2-1)=12096>5040=7!`.

It cannot embed in S_7. This contradiction proves Theorem CAY over ALL finite fields at its explicit simple full-automorphism-model hypothesis. The original EIGHT cosets and full subgroup indices were never replaced by abstract root data or independently assigned fibres.

## 10. Actual application, source boundaries and remaining gap

All special algebra automorphisms, idempotent cardinality/TRANSITIVITY, exact stabilizer/order, short-root formulas, contact coefficient -3, all characteristic branches, weight dimensions, forced field list, factor/primality identities and original-index application are reconstructed in this complete body. No assertion that a generic idempotent computation covers q=2, or that a p>=5 Heisenberg computation covers p=2/3, is made. Those boundaries were handled separately and completely.

The direct input is exactly the full supported rank-free SOME-constituent theorem, plus the explicit NONABELIAN-SIMPLE hypothesis on the ACTUAL group defined here. The arbitrary-original-group application additionally uses the full supported 88-LF normal-section proof to obtain an actual simple P7 factor with eight own-label divisors. If that factor is this split-Cayley automorphism model, Theorem CAY excludes it. There is no general identification of all remaining simple groups with this model, no new proof of every parameter's simplicity, and NO automatic theorem about a small DERIVED q=2 group or its identification with another family.

The separate new unitary and orthogonal bodies keep their exact models, pending-gate statuses and source cuts; none is a correctness premise here. All older SL/PSL/Sp/PSp/An results retain their own named imports and findings. Remaining finite simple models/coset configurations below B, exceptional/twisted/sporadic/small-derived-model identifications, general Sun8-to-P7/global Sun7 ancestry, actual witnesses, finite assays, numerical R8, unrestricted Sun8 and novelty/priority/SOTA remain unestablished. No value of B was evaluated or used to launch a search.

The frozen v9 request remains qualified RAW_UTF8_NOT_VALID_JSON under its permanent documentary SYNTAX MINOR and additive qualification; it was NOT edited or reparsed to confirm the reported failure. All OWN057/047/078/COUNT/M1/v26/v31-two-findings/v33 and parent/reviewer histories remain, with all withdrawn historical trial guidance ENTIRELY ZERO. The finite field cases here are exhaustively forced by proved uniform inequalities and displayed exact algebra, not re-used exploratory capacity probes. Both Eval kernels stay dead. This is exact WRITTEN primary work after actual v123-C RETURN and the separately WRITTEN-AND-SENT primary ACK; no scientific interpreter/calculator/Eval/program/CAS/enumeration/solver/replay/build/test/CLI/nested agent/new GO/source-author-shared-frozen edit was used. No formal/kernel/human/configured-family/executable/novelty acceptance, clean cognition/runtime census or round closeout is claimed. Original arbitrary-group research continues at its exact residual; this is not an early final park.
