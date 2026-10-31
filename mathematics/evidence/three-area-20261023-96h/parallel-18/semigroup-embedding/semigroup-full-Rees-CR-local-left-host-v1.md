# A full-Rees embedding for completely regular sources with full local group images

MathSemigroup-2, original math-4. Actual `/bin/date` before this new body: **Mon Oct 26 09:28:03 PDT 2026**. AUTHOR-WRITTEN / UNREVIEWED / novelty unresolved. Exact all-variable written mathematics, not scientific execution or the unrestricted embedding theorem. This follows explicit prospective parent direction v56 (`249d62954bf564ed8fc89674108d1942793a38d92a5e5d20045fff88e8165e45`) and the resumed primary checkpoint at09:24:44. All prior process findings, including the distinct cadence major, remain permanent. No frozen source is edited.

## 1. Hypotheses and new scope

Let S be a nonempty COMPLETELY REGULAR semigroup. Write s^0 for the identity of its maximal subgroup H_(s^0), and E=E(S), which is NOT assumed closed under multiplication. Suppose every eSe is orthodox and its idempotent band is LEFT regular (xyx=xy). Let an ACTUAL supplied idempotent-pure homomorphism q:S→C onto an ACTUAL completely simple semigroup

`C=M[G;I,Lambda;P]`, `(i,g,lambda)(j,h,mu)=(i,g p_(lambda,j) h,mu)`

be given. For e∈E write q(e)=(i_e,p_(lambda_e,i_e)^-1,lambda_e). Assume

**FULL-CS:** `q(H_e)=H_(q(e))` for EVERY e∈E.

This is fullness onto the LOCAL maximal group of C, not a requirement that a subgroup cover all Rees rows/columns. Purity makes q injective on H_e: if q(a)=q(b) for a,b∈H_e, then q(ab^-1)=q(e), so ab^-1 is idempotent by purity and equals e in the group H_e. Thus q:H_e→H_(q(e)) is an isomorphism under FULL-CS.

The result below includes nonorthodox S and arbitrary nonnormalized sandwich P. It extends the earlier group-actor FULL orthogroup construction without supposing E itself is a band. FULL-CS and complete regularity remain substantive restrictions.

Named classical imports: the Clifford/Rees structure theorem that a completely regular semigroup is a semilattice of completely simple semigroups, and the Rees matrix representation of a completely simple semigroup. The notation S=(Y;S_alpha) and these structure conventions are those of Petrich–Reilly, used in Section1 of Wang–Feng–Chen, *Some special congruences on completely regular semigroups*, arXiv:1901.08776v1 (https://arxiv.org/html/1901.08776v1), whose returned Section1, including Lemmas1.1–1.6, was actually read before writing. No unprinted later theorem from that paper is an input. The structure theorem is a NAMED classical import, not newly proved or formally verified here. All lemmas needed beyond it are proved below.

## 2. The crucial identity does not need global orthodoxy

**Lemma L0.** Under the local LEFT-regular hypotheses on S, for EVERY x,y∈S,

`(xy)^0=(x y^0)^0`.  (L0)

*Proof.* Let f=y^0, z=xf, and let f∈S_beta, z∈S_gamma in the classical semilattice of completely simple components. Then gamma≤beta, zf=z, and xy=zy. If gamma=beta, the two elements z and zy in the same completely simple component have the same row and column: right multiplication by y retains the row and installs the column of f, which is already the column of z because zf=z. Their H-class identity is therefore the same.

Suppose gamma<beta and put T=S_gamma=M[K;J,Omega;R]. Multiplication by any element s∈S_beta is a left and a right translation of T. In Rees coordinates these have the form

`s(j,a,omega)=(F_s(j),c_(s,j) a,omega)`,

`(j,a,omega)s=(j,a d_(s,omega),R_s(omega))`.  (TR)

Here c_(s,j),d_(s,omega)∈K. For completeness: left multiplication preserves L-classes' column in the target, because x=x e for an idempotent e in x's column implies sx=(sx)e. It preserves the relation R on source rows, because x=yu and y=xv imply sx=(sy)u and sy=(sx)v. Hence its output row depends only on the input row. The translation law s(xy)=(sx)y, applied after factoring an arbitrary Rees element through any fixed auxiliary row/column, then makes its group coordinate a FIXED left multiple c_(s,j) of a. Dually right multiplication preserves the row, its output column depends only on the input column, and its group coordinate is a fixed right multiple. One explicit dual factorization is

`(j,a,omega)=(j,a R_(nu,l)^-1,nu)(l,1,omega)`;

applying the right translation to the second factor gives exactly the second formula of (TR). This argument is independent of normalizing the sandwich entries.

By (TR), fTf consists of ALL Rees elements whose rows lie in F_f(J) and columns in R_f(Omega): for any chosen preimage row j and column omega, its middle coordinate c_(f,j) a d_(f,omega) ranges over K. In particular it is a nonempty full Rees submatrix. All its idempotents lie in the local band E(fSf), which is LEFT regular. Fix one of its rows. Two idempotents u,v in that row satisfy uv=v and uvu=u by the explicit Rees idempotent formula, so LEFT regularity forces u=v. Consequently there is ONLY ONE column in R_f(Omega); call it omega_*.

The identity yf=y gives R_y=R_f∘R_y on the columns of T. Hence R_y is constant omega_*. Also zf=z forces the column of z to be omega_*. Right multiplication by y preserves z's row and places it in column omega_*, so z and zy lie in the SAME H-class of T. Each such H-class has a unique idempotent. Thus z^0=(zy)^0, proving (L0). ∎

No commutation of distinct idempotents, Green congruence on S, group-section compatibility or global E-band identity was used.

## 3. Definition of the coefficient band

For e,f∈E and w∈G let r(e,w,f) be the UNIQUE element of H_e with

`q(r(e,w,f))=(i_e, w p_(lambda_e,i_f)^-1,lambda_e)`.  (RDEF)

It exists by FULL-CS. Define

`pi(e,w,f)=(r(e,w,f) f)^0`,

`B=E×G`, `(e,k)(f,m)=(pi(e,k^-1 m,f),k)`,

`alpha_g(e,k)=(e,gk)`.  (BDEF)

These formulas define products for ALL band arguments, whether or not their Rees indices match or their group translates are in any particular source subgroup. That is precisely where FULL-CS is used; no partial multiplication is totalized by assumption.

**Theorem F.** B is a band, every alpha_g is an automorphism, every local corner of B is LEFT regular, and

`Psi:S→P(B,C)`, `Psi(s)=((s^0,1),q(s))`  (MAP)

is an INJECTIVE homomorphism into the physical P product over the SAME actual q. No quotient replacement or carrier restriction is needed.

## 4. Associativity and idempotency

Fix e,f,h∈E and w,v∈G, and put u=w^-1 v, a=r(e,w,f), b=r(f,u,h), p=pi(e,w,f), z=pi(f,u,h). By Lemma L0,

`(ab)^0=(a f)^0=p`,

so ab belongs to H_p. Rees coordinates give i_p=i_e and lambda_p=lambda_f, because p is the identity of the group containing af. Moreover

`q(ab)=(i_e, w p_(lambda_e,i_f)^-1 p_(lambda_e,i_f) u p_(lambda_f,i_h)^-1,lambda_f)`

`       =(i_p, v p_(lambda_p,i_h)^-1,lambda_p)`.

Thus uniqueness in (RDEF) gives `ab=r(p,v,h)`.

Similarly i_z=i_f and lambda_z=lambda_h. Consequently q(r(e,w,z))=q(r(e,w,f)), because (RDEF) uses ONLY the row i_f of its third argument. Both elements lie in H_e, so

`r(e,w,z)=a`.

Using L0 again, first with the second factor bh,

`pi(e,w,z)=(a (bh)^0)^0=(abh)^0=(r(p,v,h) h)^0=pi(p,v,h)`.  (ASSOC)

The two parenthesizations of (e,k)(f,m)(h,n), after setting w=k^-1m and v=k^-1n, are exactly the two sides of (ASSOC), with the SAME second coordinate k. Thus B is associative for arbitrary arguments. For idempotency, r(e,1,e)=e because its Rees coordinate is q(e); hence pi(e,1,e)=(ee)^0=e. Therefore (e,k)^2=(e,k). B is a BAND, despite E(S) not being a band.

## 5. Exact local corners

For fixed e,k, take f,m arbitrary and put p=pi(e,k^-1m,f). In B,

`(e,k)(f,m)(e,k)=(pi(p,1,e),k)`.

We have i_p=i_e, so r(p,1,e)=p: the required coordinate p_(lambda_p,i_e)^-1 equals p's idempotent coordinate because i_p=i_e. Thus pi(p,1,e)=(pe)^0.

Write a=r(e,k^-1m,f). Since ea=a, e(af)=af. Multiplying on the right by the inverse of af in H_p yields ep=p. Therefore `(pe)^2=p(ep)e=pe`, and e(pe)=(ep)e=pe=(pe)e. Hence pe is an idempotent in eSe, and pi(p,1,e)=pe. Every corner element of B consequently has the form (x,k) with x∈E(eSe).

Conversely if x∈E(eSe), then q(x)=q(e): q(x) is an idempotent in the GROUP q(e)Cq(e), whose only idempotent is q(e). Thus i_x=i_e, lambda_x=lambda_e and r(e,1,x)=e; as ex=xe=x, (e,k)(x,k)(e,k)=(x,k). Hence the corner is EXACTLY

`(e,k) B (e,k)=E(eSe)×{k}`.  (CORNER)

For x,y∈E(eSe), q(x)=q(y)=q(e), so r(x,1,y)=x. Since eSe is orthodox, xy is idempotent and pi(x,1,y)=(xy)^0=xy. Thus (CORNER) is an actual band ISOMORPHISM, not just an identification of labels. It is LEFT regular by the source hypothesis. Therefore B∈W_L⊂V.

## 6. Action, multiplication of the map and injectivity

For all g,k,m, `(gk)^-1(gm)=k^-1m`. Thus alpha_g preserves (BDEF); its inverse is alpha_(g^-1) and alpha_g alpha_h=alpha_(gh). This is an ACTUAL group action by band automorphisms.

Let q(s)=(i_s,g_s,lambda_s), q(t)=(i_t,g_t,lambda_t), e=s^0, f=t^0. The first coordinate of Psi(s)Psi(t) is

`(e,1)(f,g_s p_(lambda_s,i_t))`

`=(pi(e,g_s p_(lambda_s,i_t),f),1)`.

The element in (RDEF) has q-coordinate (i_s,g_s,lambda_s) and belongs to H_e, so it is s itself. Therefore the first coordinate is ((s f)^0,1)=((st)^0,1) by L0; the second coordinate is q(st). This proves Psi(s)Psi(t)=Psi(st) for EVERY product in S.

If Psi(s)=Psi(t), then s^0=t^0 and q(s)=q(t). The two elements lie in the same maximal subgroup H_(s^0), on which q is injective. Hence s=t. This is the separating invariant; no image-diagram faithfulness or source-H-class merging is assumed.

## 7. The actual host satisfies the required structural properties

For any band B, action alpha and Rees actor C as above, the physical P(B,C) is regular. Indeed for X=(b,(i,g,lambda)), choose any j,mu and put

`h=p_(lambda,j)^-1 g^-1 p_(mu,i)^-1`, `a=alpha_((g p_(lambda,j))^-1)(b)`.

Then Y=(a,(j,h,mu)) satisfies XYX=X and YXY=Y: the first products XY and YX have band coordinates b and a, respectively, because each relevant translated coordinate equals the same idempotent b or a; their last multiplication has action weight1. The Rees coordinates are the ordinary mutually inverse ones. Thus no regularity claim is inferred from the embedded source alone.

The projection to C is idempotent-pure: if c=(i,p_(lambda,i)^-1,lambda) is idempotent, the square of (b,c) has action weight1 and equals (b,c). Conversely an idempotent has idempotent projection. For an idempotent U=(b,c), the idempotent band of U P(B,C) U is EXACTLY `(bBb)×{c}`. To see this, an idempotent in this local monoid must project to the only idempotent c of the local group cCc. In a sandwich U(d,x)U with that projection, the weight acting on the final b is1, so its coefficient is b alpha_t(d)b for the appropriate Rees weight t, hence is in bBb. Conversely every (bdb,c) is U(d,c)U. Multiplication on these idempotents is just the B multiplication, since the Rees weight c·c is1. The local monoid is regular (sandwich a regular inverse by U), and its idempotents are closed because bBb is a band. It is therefore orthodox with LEFT regular idempotents when B∈W_L, in particular locally r-orthodox.

Finally any regular semigroup with an idempotent-pure map to a completely simple semigroup satisfies the BOOK's weak E-unitarity. If E=FA=AH with E,F,H idempotent, q(A) has the same row as q(E) from AH and the same column as q(E) from FA. The equation q(F)q(A)=q(E), together with their equal rows and the Rees idempotent formula for q(F), forces the middle coordinate of q(A) to be exactly that of q(E). Hence q(A)=q(E) is idempotent, and purity makes A idempotent. Apply this to the physical host projection. Thus the displayed host really belongs to the original ambient class and uses the specified physical product.

## 8. Boundaries and the next actual obstruction

Theorem F proves a COMPLETE explicit positive construction under its ONE-SIDED local hypothesis, complete regularity, supplied pure q and FULL-CS. It is not the unrestricted target. It does not assume global orthodoxy, crypticity, a trivial sandwich, finitely many J-classes or finiteness of S/G. It does NOT prove FULL-CS, does not supply q when none is known, and does not handle non-completely-regular sources.

Compared with the earlier Theorem Q, the new steps are: L0 in nonorthodox completely regular sources; Rees-compensated r(e,w,f); its dependence on the THIRD-argument row in the associativity proof; and the exact corner computation without assuming pe or xy idempotent globally. This is not a reinterpretation of the unfinished multilayer-transversal route. A source with non-full local group images still leaves (RDEF) undefined for some w; neither a quotient nor a choice of representatives supplies the missing element.

Only this one-sided theorem is established in this body. Extending it to arbitrary regular LOCAL idempotent bands via the earlier intrinsic source-splitting theorem requires a separate explicit application/union argument at its named source boundary; it is not silently bundled here. Likewise the restricted-action R reading is not obtained merely by giving the physical map a new name.

## 9. Assurance

All identities and constructions above are conventional exact all-variable WRITTEN algebra. No identity was machine-checked; no scientific interpreter/calculator/program/CAS, numerical/state/control/magnitude/decimal probe, enumeration/table/checker, solver/replay, build/test, external CLI, nested agent or GO. No withdrawn-guidance reuse. Named structure imports are classical and unformalized; this body has not been independently reconstructed, parent-adopted, kernel/formally checked, human/cross-vendor reviewed or novelty-cleared. All five earlier candidate bodies remain at their prior boundaries. All process, source, admission and cadence findings remain. Same18/HOLD/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/prospective substantive30minJSON/no early final park. Original unrestricted acceptance remains UNMET.
