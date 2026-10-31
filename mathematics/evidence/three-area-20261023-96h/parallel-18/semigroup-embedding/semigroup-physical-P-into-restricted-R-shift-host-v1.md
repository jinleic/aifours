# An explicit physical-P to restricted-R embedding over the SAME completely simple actor

MathSemigroup-2, original math-4. Actual `/bin/date` BEFORE this new body: **Mon Oct 26 10:15:06 PDT 2026**. AUTHOR-WRITTEN / UNREVIEWED / no novelty claim. This follows ACTUAL v131-A RETURN, NEW whole primary ACK `77777dbd2ad1fdf72fe0049e0403c7a802a183f6023627ed3c56259e70dec563` WRITTEN/SENT, Main's actual complete read and EXPLICIT prospective original-primary direction v64, SHA256 `e81b3ef9966cc93e48d09eb7ad9e708c64df90bac049df559d9b160e9101eb36`, actually read COMPLETELY before this proof. No primary work was interleaved with v131. Every previous process/exactness/intake/cadence finding remains permanent.

## 1. Exact target conventions and claim

The frozen selection-v1.md LF12–20 was actually re-read before writing. Its TWO separate conventions are retained:

- Physical P(B,C), C=M[G;I,Lambda;P], G acting on B by automorphisms alpha, on the WHOLE B×C with

  `(b,(i,g,lambda))(d,(j,h,mu))=(b alpha_(g p_(lambda,j))(d),(i,g p_(lambda,j)h,mu))`.

- Restricted R(D,C), C acting on D by endomorphisms beta, with carrier `beta_(c c')(f)=f` for an inverse c' of c, and product `(f,c)(u,d)=(f beta_c(u),cd)`.

**Theorem PR.** For EVERY band B and EVERY physical P(B,C), there is an explicit band D in the SAME local band variety as B, an ACTUAL C action on D by endomorphisms, and an INJECTIVE homomorphism

`Xi:P(B,C)→R(D,C)`

whose second coordinate is the identity on C. The image satisfies the restricted carrier condition for EVERY inverse c' of c, so the construction works under either the existential or universal inverse wording of this fixed carrier. If B has regular local corners, the WHOLE restricted target constructed here is regular, weakly E-unitary and locally r-orthodox.

This is a ONE-WAY embedding of ACTUAL displayed products. It is NOT a bare assertion that the P and R definitions coincide, and no reverse implication is claimed. It supplies no physical P embedding of an arbitrary source by itself.

## 2. The actual coefficient band and semigroup action

Take the full function band

`D=B^C={f:C→B}`

with pointwise product. It is nonempty because B is nonempty and constant functions exist. Define for x∈C

`(beta_x f)(y)=f(yx)` for EVERY y∈C.  (SHIFT)

Each beta_x is a band endomorphism: beta_x(fu)(y)=f(yx)u(yx)=(beta_x f)(y)(beta_x u)(y). The action law is

`(beta_x beta_z f)(y)=(beta_z f)(yx)=f((yx)z)=f(y(xz))=(beta_(xz) f)(y)`.

Thus beta_x beta_z=beta_(xz), with the displayed order, no inverse/group-action fiction. Beta need not be injective or an automorphism; the fixed R convention asks for endomorphisms.

D is a BAND by coordinatewise evaluation. If B∈V, every corner dDd is a subband of product_(y∈C) d(y) B d(y), so its regular-band identity xyxzx=xyzx holds pointwise. The same argument holds for LEFT-regular or RIGHT-regular local corners. No unit or common source-idempotent is adjoined to B.

## 3. The explicit map and carrier proof

For b∈B and source actor row i∈I define the function F_(b,i)∈D by

`F_(b,i)((j,h,mu))=alpha_(h p_(mu,i))(b)`.  (COEF)

Then define

`Xi(b,(i,g,lambda))=(F_(b,i),(i,g,lambda))`.  (MAP)

Let c=(i,g,lambda), and take ANY mutual inverse c' of c. Its product e=cc' is an idempotent with row i, hence e=(i,p_(nu,i)^-1,nu) for some nu. For arbitrary y=(j,h,mu),

`y e=(j,h p_(mu,i) p_(nu,i)^-1,nu)`.

Consequently

`(beta_e F_(b,i))(y)=F_(b,i)(y e)`

`=alpha_(h p_(mu,i) p_(nu,i)^-1 p_(nu,i))(b)`

`=alpha_(h p_(mu,i))(b)=F_(b,i)(y)`.

Thus beta_(cc') F_(b,i)=F_(b,i) for EVERY inverse c'. The displayed map lands in the genuine restricted R carrier, not just the larger unrestricted semidirect product D⋊C.

## 4. Multiplication for EVERY pair and actual injectivity

Take X=(b,c), c=(i,g,lambda), and Y=(d,t), t=(k,l,eta). At an arbitrary test coordinate y=(j,h,mu), the first coefficient of Xi(X)Xi(Y) is

`F_(b,i)(y) (beta_c F_(d,k))(y)`

`=alpha_(h p_(mu,i))(b) F_(d,k)(y c)`

`=alpha_(h p_(mu,i))(b) alpha_(h p_(mu,i) g p_(lambda,k))(d)`

`=alpha_(h p_(mu,i))(b alpha_(g p_(lambda,k))(d))`.

Here the LAST equality uses exactly that the original G action alpha is by automorphisms. Since c t has row i, this is F_(b alpha_(g p_(lambda,k))(d),i)(y), the first coefficient of Xi(XY). The second coordinates are both c t. Equality holds at EVERY y, proving Xi(XY)=Xi(X)Xi(Y) for ALL physical-product pairs, with all source/Rees factors retained.

If Xi(b,c)=Xi(d,t), then c=t, so their row index i agrees. Fix ANY j∈I and mu∈Lambda, and evaluate their equal functions at

`y=(j,p_(mu,i)^-1,mu)`.

The action weight in (COEF) is1, so this equality reads b=d. Hence X=Y. This is an explicit separating evaluation, not a faithfulness assumption about a function diagram. Arbitrary infinite B,G,I,Lambda are allowed. If B and C are finite, D is finite; this is a conditional finite construction, not an executed table/enumeration.

## 5. The WHOLE restricted carrier is a regular semigroup

This section verifies the ambient R host needed for the original target, rather than infer its properties from the image.

For a general f∈D and c∈C, requiring beta_(cc')f=f for ONE inverse c' is equivalent here to requiring it for EVERY inverse. Indeed all possible cc' are the idempotents in c's R-class. Two such idempotents e,v satisfy ve=e and ev=v by the Rees formula. If beta_e f=f, then beta_v f=beta_v beta_e f=beta_(ve) f=beta_e f=f.

**Closure.** Take (f,c),(u,t) in the carrier and let v be ANY range idempotent of c t. It is in the same R-class as c, so beta_v f=f and v c=c. Therefore

`beta_v(f beta_c u)=(beta_v f)(beta_(v c) u)=f beta_c u`.

Thus their ordinary displayed semidirect product lies in the restricted carrier. Associativity follows from the endomorphism action law, or by restricting the ordinary semidirect product.

**Regularity.** Given (f,c), choose a mutual inverse c' of c and put u=beta_(c')f. Then (u,c') belongs to the carrier, since for ANY inverse z of c',

`beta_(c'z) u=beta_(c'z c')f=beta_(c')f=u`.

The products (f,c)(u,c') and (u,c')(f,c) have coefficients f and u, respectively: f beta_(cc')f=f and u beta_(c')f=u²=u. Their final triple-product coefficients are again f and u, because beta_(cc')f=f and beta_(c'c)u=beta_(c'cc')f=u. The actor triples are cc'c=c and c'cc'=c'. Hence this is an actual mutual inverse INSIDE the restricted carrier.

**Pure projection.** If c²=c and (f,c) is in the carrier, fix any inverse c'. Then beta_(cc')f=f implies beta_c f=beta_c beta_(cc')f=beta_(c²c')f=f. Thus (f,c)²=(f,c). The converse, that an idempotent has idempotent projection, follows from projection being a homomorphism. Therefore R(D,C)→C is idempotent-pure.

**Local orthodoxy and exact local-band containment.** Let H=(d,e) be an idempotent carrier pair. Any local idempotent in H R H must have actor e, the sole idempotent of the group eCe. Write it (u,e). Since both d,u are fixed by beta_e, the local identity equations are exactly du=u=ud. Hence its coefficient u lies in dDd. Conversely any u∈dDd fixed by beta_e gives such an idempotent. The fixed-point set of an endomorphism is a subband, so these local idempotents form a SUBBAND of dDd under ordinary band multiplication. If D∈V their band is regular. A local monoid of a regular semigroup is regular (sandwich a chosen mutual inverse by H), hence this local monoid is orthodox with a regular idempotent band. This proves local r-orthodoxy of the ENTIRE restricted host.

**Book weak E-unitarity.** For any regular semigroup with pure projection to a CS actor, an equation E=FA=AH with E,F,H idempotent forces q(F),q(A) to have the same row: the row of E is the row of F from FA and the row of A from AH. The Rees idempotent formula then gives q(F)q(A)=q(A), so q(E)=q(A) is idempotent. Purity makes A idempotent. Apply this to R(D,C)'s projection. This is the literal book condition, not a stronger orthodox-group convention.

## 6. Application and exact scope

EVERY actual source embedding j:S→P(B,C) over q therefore gives an ACTUAL embedding Xi j:S→R(B^C,C) over the SAME q, preserving the local band variety. This may be used for the whole new F/F2/FC/F3 positive theorem ONCE that complete named theorem union and this transfer body have each been separately reconstructed/adopted. It is not permission to insert this LATER body into the currently LIVE v133 freeze.

For emphasis, the current candidate F3 yields an original locally r-orthodox REGULAR source embedding under supplied pure onto q and FULL-CS. If it is supported, Theorem PR transfers THAT restricted-hypothesis positive result to the fixed restricted-R reading. The transfer itself does not require FULL-CS or complete regularity, but it DOES require an already supplied faithful physical-P host. It therefore does NOT close the arbitrary NONFULL source's missing physical coefficient-band completion, and supplies no q for arbitrary infinite inputs. No nonembedding claim follows from failure of any current construction.

The predecessor source text's 'no P/R equivalence established' remains historically correct at its earlier scope; this new ONE-WAY explicit construction is not a retroactive equivalence claim. No reverse restricted-to-physical theorem is established here.

## 7. Imports and assurance

Only the fixed product definitions, Rees multiplication/idempotent rows, ordinary band product/subband closure and semigroup endomorphism/action facts enter PR. Every new map, carrier condition, product, separating evaluation and ambient-host property is proved above. No scientific computation or external classification theorem is an input. No identity was machine-checked; no scientific interpreter/calculator/eval/program/CAS, numerical/state/control/boundary/magnitude/decimal probe, enumeration/table/checker, solver/replay/build/test, external CLI, nested agent or GO. No withdrawn-guidance reuse or frozen/shared edit.

This new body is AUTHOR-WRITTEN, UNREVIEWED, not formal/kernel/human/configured-family/executable/novelty certification. All earlier process/intake/read-order/cadence/admission/math-withdrawal findings and ZERO-credit histories persist. Same18/exclusiveOWN/HOLD/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/actual30minsubstantiveJSON/noearlypark or round closeout. Original unrestricted embedding/obstruction acceptance remains UNMET.
