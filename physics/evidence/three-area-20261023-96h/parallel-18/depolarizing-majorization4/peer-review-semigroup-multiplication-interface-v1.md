# v37-E — written reconstruction of quotient-preserving sandwich multiplication

Actual `/bin/date` before creation: **Sun Oct 25 05:24:06 PDT 2026**. Reviewer PhysicsDepol4-2. Same-harness cross-domain supplied-proof review; WRITTEN only, not blind/cross-vendor/human/formal/kernel or novelty acceptance. HOLD/v7 binding.

## 1. Pin, full coverage, exposure and serial prerequisites

Source: `mathematics/evidence/three-area-20261023-96h/parallel-18/semigroup-embedding/semigroup-embedding-consolidated-v1.md`, SHA256 `841a5490df82da288589470939e285dd6a7ccf5351f9b04b8add673b878e6fe3`, **complete LF1–314**.

Literal packet: `peer-review-wave-v37-semigroup-multiplication-interface-sources-v1.md`, SHA256 `4681d8093afec21c8c5bc2bb4cfd722504ff6e3bd7a1c0ac2ae73dbf9c862869`. All323 packet lines, containing every source LF1–314, were actually read in two ranged calls. No truncated source line remains unread.

Manifest observed SHA256 `eb3d6f624c9e191702658bf2a8c969b2904e9aa347c91df173b131c0be1dba54`. Packet receipt observed SHA256 `a6f2954275c0599fca95790b3471fdf66f1faabaa846191e0a43d70c6d4b75c2`, read completely. Source/packet hashes match the frozen entry. The receipt's literal-equality statement is parent metadata; no independent packet-regeneration program was run.

The exposure ACK `peer-review-semigroup-multiplication-interface-ack-v1.json` preceded reading the source body or new derivation. Parentv7 was reread in full beforehand. Actual v35-B was returned to Main before this source was opened; v32-H was already returned. No other semigroup review or parent correctness preview was imported.

No scientific eval/interpreter/arithmetic program/symbolic computation/enumeration/replay/solver/GO/CLI/nested agent was used. Tools were source reads and metadata clocks/hashes; all mathematics below is written reconstruction.

All LF references below refer to the314-line AUTHOR SOURCE.

## 2. Verdict and mathematical scope

**0 FATAL / 0 MAJOR / 0 MINOR** at the assigned multiplication-interface scope.

For arbitrary s,t in a REGULAR semigroup, with their chosen mutual inverses, the source constructs a nonempty rectangular band of actual sandwich idempotents h. Every such h yields st=sht and the asserted composable inverse-pair restriction factorization. For any supplied homomorphism to a completely simple Rees semigroup, every such h has the stated crossed idempotent type and preserves the quotient value of BOTH factor restrictions. Global orthodoxy is not needed; in the orthodox subclass h=fe is indeed a canonical valid choice.

The conclusion is LOCAL multiplication-interface support only. It neither proves the global coordinate descent nor the canonical presentation's fibre separation, and does not supply a missing completely-simple pure quotient for arbitrary infinite nonorthodox input semigroups.

## 3. Actual inverse pairs and nonempty sandwich choices

**Reconstructed: LF235–247.**

Let s' be a mutual inverse of s and t' a mutual inverse of t. Put e=s's and f=tt'. These are actual idempotents, and se=s,ft=t. The source does not assume e=f.

Because S is regular, ef has a mutual inverse z, meaning

`(ef)z(ef)=ef`, `z(ef)z=z`.

Set h=fze. Associativity and idempotency of e,f give

`h²=fzefze=f[z(ef)z]e=fze=h`,

`he=fze²=h`, `fh=f²ze=h`,

`ehf=efzef=ef`.

Thus the set

`H(e,f)={h in E(S):he=h,fh=h,ehf=ef}`                 (H)

is nonempty. This does not require ef to be idempotent, any global closure of E(S), finiteness or uniqueness of z.

In fact every h in(H) is itself a mutual inverse of ef: `h(ef)h=(he)(fh)=h` and `(ef)h(ef)=e(fh)ef=ehe f=ehf=ef`. Also fhe=h. Consequently the all-choice set(H) is exactly the set of fze obtained from mutual inverses z, not a larger family whose nonemptiness or properties are assumed separately.

## 4. Product identity with no commutation or cancellation assumption

**Reconstructed: LF249–251.**

For EVERY h in(H),

`sht=(se)h(ft)=s(ehf)t=s(ef)t=(se)(ft)=st`.

The substitutions use only se=s,ft=t and ehf=ef. There is no cancellation law in S and e,f are not commuted. This works for already composable as well as originally noncomposable arrows.

## 5. Both restrictions are actual inverse-pair arrows

**Reconstructed: LF253–268.**

For A=sh and A'=hs',

`A'A=hs'sh=heh=h`,

`AA'=sh²s'=shs'`.

The latter is idempotent because

`(shs')²=sh(s's)hs'=shehs'=shs'`.

The mutual inverse equations are

`AA'A=sheh=sh=A`,

`A'AA'=hehs'=hs'=A'`.

Thus `(sh,hs')` has source h and target shs'. Dually, for B=ht and B'=t'h,

`BB'=htt'h=hfh=h`,

`B'B=t'h²t=t'ht`,

and `(t'ht)²=t'h(tt')ht=t'hfht=t'ht`. The two inverse equations follow from hfh=h. Hence `(ht,t'h)` has source t'ht and target h.

The shared middle object is the SAME actual h, not merely the same q-image. The two arrows are therefore genuinely composable. Their product and inverse are

`(sh)(ht)=sht=st`, `(t'h)(hs')=t'hs'`.

The endpoints can also be checked directly:

`(t'hs')(st)=t'he t=t'ht`,

`(st)(t'hs')=s f h s'=shs'`.

Here he=h and fh=h are used in their actual ordered positions. Thus t'hs' is an explicit mutual inverse of st with exactly the asserted endpoints.

For natural order, sh=(shs')s=sh and sh=s h, with both shs' and h idempotent. Similarly ht=h t=t(t'ht), with h and t'ht idempotent. These are the standard regular-semigroup natural-order witnesses sh<=s and ht<=t; no claim that every principal one-sided ideal is a regular semigroup is needed.

## 6. ALL sandwich choices form a rectangular band

**Reconstructed: LF270–279.**

Take h,k in(H), not assumed equal or obtained from the same inverse z. Then

`hkh=(he)k(fh)=h(ekf)h=h(ef)h=(he)(fh)=h`.

The symmetric calculation gives khk=k, so `(hk)²=hkhk=hk`. Its one-sided conditions are

`(hk)e=h(ke)=hk`, `f(hk)=(fh)k=hk`.

For the remaining condition, use fk=k, ehf=ef and ekf=ef in exactly that order:

`ehkf=eh(fk)f=(ehf)kf=(ef)kf=e(fk)f=ekf=ef`.

Thus hk belongs to(H), which is a band, and hkh=h for every pair. This is precisely a rectangular band. The proof establishes closure as well as the rectangular identity; merely proving hkh=h would not by itself have justified calling a non-closed set a band.

If S is orthodox, ef and fe are idempotent. Taking h=fe gives he=h,fh=h, and `ehf=efef=(ef)²=ef`. This verifies the canonical orthodox choice without assuming e,f commute. The arbitrary-regular construction remains needed outside that subclass.

Rectangularity does not imply that two choices are equal, or that their coordinate-band endpoints are identical. This distinction is retained in the source's descent gap.

## 7. Exact Rees typing and both quotient-preservation equations

**Reconstructed: LF281–287, using only the literal product at LF36–39.**

Let q:S->C be the supplied homomorphism, where

`(i,g,lambda)(j,h,mu)=(i,g p_(lambda,j)h,mu)`.

For this typing argument, neither purity nor surjectivity is needed once such a homomorphism is given. Write q(s)=(i_s,g_s,lambda_s),q(t)=(i_t,g_t,lambda_t).

The column of q(e)=q(s's) is lambda_s, even though its row can depend on s'. The row of q(f)=q(tt') is i_t, even though its column can depend on t'. From he=h, equality of Rees columns forces the column of q(h) to be lambda_s. From fh=h, equality of rows forces its row to be i_t. Since h is idempotent, so is q(h).

In Rees H-class(i,lambda), the idempotent equation for a group coordinate g is `g p_(lambda,i)g=g`, equivalently `g=p_(lambda,i)^(-1)`. There is therefore exactly one idempotent in that H-class, and every h in(H) has

`q(h)=(i_t,p_(lambda_s,i_t)^(-1),lambda_s)`.

Let p0=p_(lambda_s,i_t). Direct multiplication in the correct noncommutative order gives

`q(sh)=(i_s,g_s p0 p0^(-1),lambda_s)=q(s)`,

`q(ht)=(i_t,p0^(-1) p0 g_t,lambda_t)=q(t)`.

No sandwich factor is omitted from either product. The result does not rely on making an arbitrary inverse-of-ef choice canonical. Different actual h may map to this same idempotent without being equal in S.

## 8. Transport on the actual composable restrictions

**Reconstructed: LF106–127 as the needed transport interface, LF289–293.**

The groupoid uses an ACTUAL inverse pair(a,a'), from e=a'a to f=aa', not an arbitrary element labelled only by quotient endpoints. If x is idempotent with ex=x, then axa' is idempotent and left-fixed by f:

`(axa')²=ax e x a'=axa'`, `f(axa')=axa'`.

It is multiplicative on B_e, since `axa' aya'=ax e y a'=axy a'`. Its reverse composite on B_e is exe=xe, R-related to x. Indeed x(xe)=xe and(xe)x=x. Hence it induces an isomorphism L_e=B_e/R ->L_f. The dual argument on D_e uses xe=x, reverse composite ex and L-relatedness. Existence of the coordinate-band congruences is the declared principal-regular-band interface, not a global R/L-congruence assumption on E(S).

For composable pairs, literal associativity gives theta_a theta_b(x)=ab x b'a'=theta_(ab)(x). Apply it to a=sh,a'=hs',b=ht,b'=t'h. The resulting formula is

`theta_(sh)(theta_(ht)(x))`

` =sh(ht x t'h)hs'=sht x t'hs'=st x t'hs'`.

This is theta_(st) with the SPECIFIED inverse t'hs' and domain/target idempotents t'ht,shs'. It holds on the corresponding one-sided quotient bands as well. It does not assert equality with every transport constructed using some other inverse of st at different endpoints.

For completeness of the local hypotheses, source Theorem3.1 makes the actual B_e,D_e regular bands without global orthodoxy. Its closure argument uses that xe,ye lie in E(eSe), so xye is idempotent; multiplying that identity by y recovers idempotency of xy. The regular identity is recovered from rho_e(x)=xe by right multiplying words with common last letter x. Thus the required local congruences are not assumed on an arbitrary non-closed E(S). No full new verdict on all other consolidated semigroup claims is transferred from this multiplication review.

## 9. Whole-source scope audit and explicit remaining gaps

The full314-line body was inspected, not only the new section. It explicitly makes the actual idempotent-pure quotient a SUPPLIED prerequisite at LF43. The literal sandwich construction in §3 above needs only regularity; quotient typing in §7 needs only a homomorphism into the stated completely simple Rees product. Purity matters elsewhere in the canonical construction and cannot be silently conjured for arbitrary infinite nonorthodox S.

The source does not infer a global embedding from the composable squares. Two valid h,k have the same q-image, but may have different actual domain objects t'ht,t'kt and range objects shs',sks'. Faithfulness on one fixed hom-set compares PARALLEL arrows; it does not identify those different objects or make all restriction maps agree after global gluing. Nor does a rectangular band of choices establish that the canonical presentation preserves distinct idempotents in every q-fibre.

The following are explicitly **NOT_RECONSTRUCTED / NOT_ACCEPTED by this review**:

1. Global choice-compatible gluing of all endpoint coordinate bands and sandwich squares with the actual Rees/group action.
2. The canonical presentation's idempotent-fibre separation(SEP), injectivity of kappa_q, or a full P/R embedding theorem.
3. A genuine nonembedding obstruction, especially one based only on collapse over an arbitrarily coarser quotient.
4. Existence of a suitable pure completely simple quotient for every arbitrary infinite nonorthodox book-class input.
5. Universal N3 and the full Rees-local/contextual-birth theorems as independent review gates. Their complete bodies were read for hidden premises; they are not needed to establish the new sandwich multiplication formulas and no old verdict is transferred to them here.
6. Historical process attestations, scientific/executable/finite-certificate verification, formal/kernel, human, cross-vendor or novelty acceptance.

No exact scope mismatch or mathematical defect was found in the assigned multiplication-interface result. Classical Hall/Munn/inductive-groupoid analogues and the source's NOVELTY_UNCLEAR qualification remain; this review does not supply priority clearance.

**Disposition:** the one-h factorization, ALL-choice rectangular sandwich structure, orthodox h=fe case, actual composable inverse-pair restrictions and both exact Rees quotient-preservation equations are supported by a complete WRITTEN reconstruction at this pinned scope. The global descent/SEP and quotient-existence gaps remain real and explicit.
