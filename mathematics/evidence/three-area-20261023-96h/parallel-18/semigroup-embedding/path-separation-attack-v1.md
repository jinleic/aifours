# Focused continuation of the ONE band-amalgam construction

MathSemigroup, math-4. Actual clock immediately before writing: **2026-10-23T14:28:44-0700**.

**CANDIDATE / PARTIAL / NOVELTY_UNCLEAR.** This continues the canonical mixed-relation separation gap, not another problem or a claimed full embedding. It proves an exact path-typing barrier in the orthodox reduction and rejects one tempting bridge construction on an already embeddable infinite example. No scientific executable or enumeration was run. The broad nonorthodox source and general pure completely-simple grading are not silently replaced by this group-graded diagnostic case.

## 1. The exact diagnostic subcase

Let S be E-unitary orthodox with locally regular idempotent band E, and let sigma:S --> G be its least group quotient. Thus sigma^(-1)(1)=E. These are precisely the orthodox hypotheses of the existing reduction of the book target. This section uses the group-grading specialization of `construction-gap-v1.md`, not a new target in place of the broad P/R question.

For every u in G and s in S view X_(u,s) as an arrow

    u --> u sigma(s).

A nonempty word of letters is **path-typed** if consecutive arrow endpoints match. Its value in S is the product of its s-labels, and its group grade is determined by its starting/ending objects. The multiplication relations

    X_(u,st)=X_(u,s) X_(u sigma(s),t)               (M_G)

are precisely the composition relations of this actual derived semigroupoid. Either direction preserves path typing, endpoints and S-value in any path-typed context.

Use the local regular-band identity in the sandwich form

    P Z P X P Z P Y P Z P = P Z P X P Y P Z P.     (LR_P)

Together with W^2=W it presents the free locally regular band on the letter alphabet; concatenation already builds in associativity. All substitution words here are nonempty.

## 2. New written step: every path-typed LR transition is already valid in S

**Lemma.** Suppose one side of an elementary substitution of (LR_P), inside a path-typed word context, is path-typed. Then the other side is path-typed with the same endpoints and has the same S-value.

**Proof of typing.** Each substitution block P,Z,X,Y is itself a substring of a path and hence is a path. Repeated occurrences of a block have the same endpoints because letters carry their actual starting objects. Both sides of (LR_P) have exactly the same set of adjacent block pairs:

    PZ, ZP, PX, XP, PY, YP.

Consequently their endpoint matching constraints are identical. If P has endpoints a-->b, then each of Z,X,Y has endpoints b-->a. The two complete expressions both run a-->b. Contexts are therefore preserved as well.

**Proof of values.** Write the four S-values as p,z,x,y. Their grades satisfy

    sigma(z)=sigma(x)=sigma(y)=sigma(p)^(-1).

Hence pz,px,py are actual idempotents by E-unitarity. Choose p' in V_S(p) and put e=pp'. Then ep=p. For t in {z,x,y}, define

    c_t=p t e.

It lies in eSe, since e c_t=c_t=c_t e. It is idempotent: using ep=p,

    c_t^2=p t e p t e=p t p t e=(pt)^2 e=pt e=c_t.

The idempotents of eSe form a regular band by the exact source hypothesis. Therefore

    c_z c_x c_z c_y c_z = c_z c_x c_y c_z.

Multiplying by p on the right and using ep=p at each junction gives exactly

    p z p x p z p y p z p = p z p x p y p z p.

These are the values of the long and short sides of (LR_P). No global regular-band identity on all E has been assumed. The sandwich localization is the step that avoids that false assumption. QED.

This proof actually needs purity of the group grading and local regularity at pp'; it does not rely on the fixed-section formula that failed in `construction-gap-v1.md`.

## 3. Where a genuine canonical collapse must leave the path category

An idempotency contraction WW-->W is path-typed only if W is a loop, because WW can compose only when end(W)=start(W). If W is a loop, its value has grade1 and is an idempotent, so contraction and expansion preserve S-value. An expansion W-->WW of a **nonloop** path is the one way this primitive band identity can leave path typing.

Combine this with §2 and (M_G): every finite derivation using the displayed generating relations and remaining path-typed at all stages preserves S-value. In particular it cannot identify X_(1,e) and X_(1,f) for distinct e,f in E.

**Precise structural barrier.** If the canonical locally regular band construction collapses two distinct source idempotents in this orthodox case, then **every** derivation of that collapse, refined into elementary (M_G), idempotency and (LR_P) rewrites, contains an expansion of a nonclosed path W to WW. At the first stage that ceases to be a path, neither (M_G) nor (LR_P) can be responsible. A local regular-band identity inside a correctly typed path is not itself a counterexample mechanism.

This is not an exclusion of all untyped derivations. It identifies the exact transition that an eventual path-completion construction must handle. In particular, replacing the proof by an evaluation of only typed paths would beg the remaining question.

## 4. Actual bridge attempt and its exact failure boundary

One natural attempted repair is to complete every word to a path by inserting a bridge between every incompatible pair of adjacent object labels. Choose a fixed bridge b_(v,w) in S with sigma(b_(v,w))=v^(-1)w, depending only on the ordered object pair(v,w). A bridge at compatible endpoints may be omitted rather than inserting an unnecessary identity element; S need not be a monoid.

This completion handles (M_G) and the local identity surprisingly well. For (LR_P), if the individual completed blocks have endpoints

    P:a-->b, Z:c-->d, X:f-->g, Y:h-->k,

absorb the fixed bridges into

    Z_tilde=b_(b,c) Z b_(d,a),
    X_tilde=b_(b,f) X b_(g,a),
    Y_tilde=b_(b,h) Y b_(k,a),

omitting any bridge at an already matched pair. Then each tilde block is b-->a and the completed relation is exactly the path-typed instance proved in §2. Internal block completions repeat identically. Thus the real difficulty is not the local identity but global band idempotency.

For a nonloop path W:a-->b of S-value s, completion of WW introduces b_(b,a), and preservation of the idempotency relation would require

    s b_(b,a) s = s                               (ABS)

for **every** S-value of an a-->b path. Since a one-letter path already realizes every s in the corresponding grade, this is a simultaneous inner-inverse requirement for the whole grade fibre. It is not implied by choosing a single arbitrary preimage of the inverse group element.

### Exact rejection control: the ansatz fails even for an already embedded infinite source

Let

    S=(Z,min) cross C2,
    C2={1,g}, g^2=1,

with componentwise multiplication and sigma(n,h)=h. This is an inverse semigroup, E-unitary, with a semilattice idempotent band. It already is the allowed semidirect product with trivial action, so is certainly NOT a counterexample to the book problem.

Consider paths1-->g with values s_n=(n,g). A single fixed bridge g-->1 must have value(m,g) for some integer m. But

    s_n (m,g) s_n=(min(n,m),g).

For n>m this differs from s_n. Thus no fixed in-S bridge for the object pair(g,1) can satisfy (ABS) for all such paths.

This rejection is a direct written infinite calculation, not a finite search. It shows that the simple endpoint-only, in-S bridge construction is too restrictive even on an explicitly embeddable source. Failure of (ABS) cannot be promoted to nonembeddability. Allowing value-dependent bridges, a larger auxiliary band, or a rigorously controlled path-extension normal form is genuinely necessary for this approach.

For an individual path W one may choose its own mutual-inverse path W' and replace WW by WW'W, whose value is s s' s=s and which is path-typed. The unresolved issue is **coherence under subsequent rewrites**: inserting W' changes the letters on which later band transitions act. No proof that these individual repairs compose into a well-defined separating band functor is given here.

## 5. Primary-source refresh tied to this construction

A new relevant primary source was actually read:

[Hu–Liu–Guo, On Locally Regular Cryptogroups (2013)](https://ccj.pku.edu.cn/Article/DownLoad?id=313742555&type=ArticleFile), all8pages, especially Definition0.4 and Corollary1.13. Its quasiregular band identity is

    a x y z y x a = a x y a y z y a y x a,

and Corollary1.13 identifies that band variety with L(regular bands), exactly the book's seminormal-band condition. This gives a useful additional search term and identity presentation; it does not prove any desired embedding. The source's 'regular cryptogroup' is its specified band-of-groups variety, NOT the vacuous assertion that local corners are regular semigroups. Search summaries conflated those meanings; they are not adopted.

Also read [Hartmann, Embedding into almost factorizable orthodox semigroups (2007)](https://www.acta.hu/download.phtml?id=2927), including its path/congruence-extension construction. Its Theorems3–4 and bridge arguments use the **global regular-band** orthodox hypothesis. They do not automatically establish the locally regular extension. This is a direct older primary comparison, not a claim of a new path method.

The new canonical band construction is likewise calibrated against the already-read [Szendrei1993](https://acta.hu/download.phtml?id=2201), Theorem2.2/Corollary2.7: the orthodox group-graded universal criterion is classical. The new file's purpose is the explicit local-corner verification in §2 and the sharply delimited path-completion failure in §4, not priority for the canonical construction.

A renewed attempt to open Billhardt1998 at its actual publisher PDF URL returned403; OpenAlex still lists only that publisher location and no repository copy. The specific counterexample's local regularity is therefore still unverified, not presumed true or false from its left-semiregular label. The original2002 problem body remains inaccessible through the inspected lawful routes. No contact, login, access-control bypass or request-copy action occurred.

## 6. Exact result and next obligation

The proven bounded attack is: typed composition and typed local-regularity rewrites are harmless; any canonical collapse must exploit a nonloop idempotency expansion and an untyped excursion. The attempted fixed endpoint-only bridge completion fails on an already embedded infinite inverse semigroup. Neither conclusion is a full negative or full positive answer.

The ONE remaining construction is still to preserve idempotent-fibre separation in the canonical band amalgam. In the orthodox group-graded route, it has now been localized further to **coherent repairs of nonloop duplication across untyped intermediate words**, with local regular identities already verified at all typed substitutions. The broad nonorthodox/Pastijn case still needs its corresponding Rees-typed extension; no claim that the group-graded argument covers it has been made. A complete candidate normal-form or a genuine source-preserving collapse would need fresh pinned written review before promotion.
