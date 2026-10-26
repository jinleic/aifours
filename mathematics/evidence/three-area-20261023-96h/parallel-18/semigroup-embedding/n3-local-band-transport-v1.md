# N3 as a local-band support-switch problem

MathSemigroup, math-4. Actual precreation clock: **Sun Oct 25 04:24:50 PDT 2026** (`/bin/date`).

**Status: WRITTEN, PARTIAL, NOVELTY_UNCLEAR.** This is an algebraic reduction and a new Rees-typed local validation lemma, not an embedding theorem or a nonembedding example. The assignment's positive/negative acceptance criterion is **NOT MET**. There is no table, generated checker, search, symbolic/arithmetic interpreter, solver, certificate replay, external model CLI, nested agent or scientific execution in this resumption. The parent's withdrawal of the purported in-kernel arithmetic exception is binding; `resume-permission-addendum-v1.json` records that no such computation had been performed here. Original packets remain unchanged.

## 1. Inputs, imports and exact retained target

The target remains the universal finite/infinite book question, with the actual P and R products fixed in `countermodel-witness-protocol-v1.md`, not merely band-by-group embedding or an idempotent-separating image.

Read and pinned for this packet:

- Run-root `semigroup-coherent-birth-parent-v1.md`: SHA-256 `54b9e20e58710749ff9fca9c47b761d543a49d0f56b3546727d32a6d8c415dfe`.
- Run-root `semigroup-contextual-loads-parent-v1.md`: SHA-256 `19cbd84cd5aa0dd901779e83189aef67c8b5e0fab2896ef0652362cbdf8640d1`.
- Own `countermodel-witness-protocol-v1.md`: SHA-256 `b5f523e7cfd521413c20a01faad88a7c512dfc6dd99f7647eb68699866c024b1`.
- Own `construction-gap-v1.md`: SHA-256 `eea9fe1352cf9e1cb83200f114209103f75d1266c022f6fdf4aad699f8a12b10`.
- Own `path-separation-attack-v1.md`: SHA-256 `60d967621f44e20f36f25c4ce402446ff4d4bd6f5f7dbf4c6a0fe68a4451ff4d`.
- Hartmann's 2007 thesis, `mathematics/regular-semigroup-embedding/hmz-lean-20261014/sources/hartmann2007-thesis.pdf`: SHA-256 `3a7e7cea4516f8afb1ead44d42eb78e1d88672155619cd7db924edb5899d42b2`. The actual extracted definitions, Theorem 2.1, graph construction and Theorem 3.4 were read; no new claim of inspecting Billhardt's original proof.

Named classical imports:

1. For an E-unitary regular semigroup the least group congruence is idempotent pure; the semigroup is orthodox (Hartmann Theorem 2.1). Thus, with the least group map `pi`, `E(S)=pi^(-1)(1)`.
2. The D-classes of a band are rectangular bands and its D-quotient is a semilattice. In particular, if `D(a)<=D(b)`, then `aba=a`.
3. In a regular band, Green R and L are congruences; equivalently, the standard regular-band spined-product description gives the same preservation fact. Only the R-congruence consequence is used below.
4. The necessary N1/N2 => N3 theorem is Hartmann 3.4 [Billhardt]. Its full statement and the P/R-to-band-by-group bridge remain exactly those in the existing protocol. Sections 2–5 do not reprove the imported nonembedding criterion or claim a new criterion sufficient for embedding.

In the orthodox book subclass, the existing weak-to-strong E-unitarity reduction permits import 1. Nothing below applies that reduction to arbitrary nonorthodox sources. Section 6, by contrast, explicitly does not assume orthodoxy.

## 2. Direct common-inverse identities; no new gamma-congruence import

Let `a,A,b,B,e,f,g` satisfy N1 and N2 in an E-unitary regular semigroup, where `A in V(a)`, `B in V(b)` and `a sigma b`. In particular:

    eaA=e=ebB,
    Aafg=fg,
    Bb f Aea f g = f Aea f g.

Let `h=pi(a)=pi(b)`. Define

    x=ea,       y=eb,       c=Ae,       t=Be.

Then

    xc=e=yt,       ex=x, ey=y,       ce=c, te=t.

All products of one grade-h and one grade-h^(-1) factor are idempotent by purity. In particular `(cy)^2=cy`. Multiply this equality on the left by x and on the right by t:

    x(cycy)t = x(cy)t,
    (xc)y c(yt) = (xc)(yt),
    e y c e = e,
    yc=e.

Here `ey=y` and `ce=c` justify the last simplification. The dual calculation with `(tx)^2=tx`, multiplied on the left by y and right by c, gives

    xt=e.

Consequently c and t are both mutual inverses of both x and y. For example `ycy=ey=y` and `cyc=ce=c`. This conclusion uses actual grade purity and the displayed source equations; it does not assume that arbitrary equal helper grades prove sigma, and does not import a characterization of the minimum inverse congruence.

## 3. The two N3 values are faithfully represented by idempotents

Put

    u=Aa,       v=Bb,
    p=cx=Aea,   k=cy=Aeb,
    l=tx=Bea,   r=ty=Beb.

All eight of `u,v,p,k,l,r,f,g` belong to the actual band `E(S)`.

The four elements `p,k,l,r` form a possibly degenerate 2-by-2 rectangular subband, with this structural multiplication display (not a proposed source table):

| product | p | k | l | r |
|---|---|---|---|---|
| p | p | k | p | k |
| k | p | k | p | k |
| l | l | r | l | r |
| r | l | r | l | r |

Every entry follows from `xc=yc=xt=yt=e`. For example

    pk=cxcy=c(xc)y=cey=k,
    kl=cytx=c(yt)x=cex=p,
    lk=txcy=t(xc)y=tey=r,
    rp=tycx=t(yc)x=tex=l.

No pairwise distinctness is asserted. Further,

    p<=u,       r<=v,                              (B1)

where the band natural order means both-sided absorption. For example `up=AaAea=Aea=p` and `pu=AeaAa=Aea=p`; the r,v calculation is identical. Rectangular multiplication and (B1) imply

    uk=k,       kv=k,       vl=l,       lu=l.

The two remaining N2 equations become the purely band equations

    ufg=fg,
    v f p f g = f p f g.                           (B2)

Define two idempotents

    H=pfg,               K=k f p f g.

Let the original N3 sides be

    L=ea f g=xfg,
    R=eb f Aea f g=y f p f g.

Then exactly

    cL=H,       cR=K,
    xH=L,       xK=R.                              (B3)

The recovery identities use `xc=e`, `ex=x`, `ey=y`. Therefore

    L=R  iff  H=K,       and       L!=R  iff  H!=K. (B4)

This is not merely a homomorphic projection that may lose the desired inequality. The SAME fixed left multiplier x recovers both original values from the two band values.

**Consequence.** Every N3 countermodel in the orthodox book class produces an actual locally regular band, a rectangular quadruple, two natural upper supports satisfying (B1), the two equations (B2), and the STRICT band inequality `pfg != kfpfg`. This consequence has no finiteness or C2 assumption.

The converse is NOT proved: an abstract band configuration satisfying these equations is not yet a regular-semigroup countermodel. It would also need a genuine regular, pure group-graded transport realizing a,A,b,B,e and all associativity equations. A failed band transport implication, by itself, must not be advertised as nonembedding.

## 4. Every principal one-sided ideal of the source band is regular

**Lemma.** For a band D the following are equivalent:

- every `dDd` is a regular band;
- every principal right ideal `dD` is a regular band;
- every principal left ideal `Dd` is a regular band.

**Proof of the nontrivial direction.** Fix d and set `T=dD`. It is a band with left identity d. Define

    rho:T -> dDd,        rho(z)=zd.

For z,t in T, `dt=t`, so

    rho(z)rho(t)=zdtd=ztd=rho(zt).

Thus rho is a homomorphism. For x,y,z in T, the regular-band identity in dDd gives

    rho(xyxzx)=rho(xyzx).

Both words end in x. Also `xdx=x` because `dx=x` and x is idempotent. Consequently right multiplication by x recovers each word from its rho image:

    (xyxzx)d x=xyxzx,
    (xyzx)d x=xyzx.

They are equal, proving that dD is regular. The left-ideal assertion is dual. Conversely dDd is a subband of either one-sided ideal, so regularity of the latter implies local regularity. QED.

The lemma concerns the BAND `E(S)`. It does **not** assert that `eS` is a regular semigroup; that stronger statement is false in general and is not used to invoke an embedding theorem on `eS`.

## 5. The exact support switch required by an N3 countermodel

Write `z=fg` and `Y=fpfg=fH`. Equation (B2) says

    z in uE(S),          Y in vE(S).

Both p and k lie in `uE(S)`, by `up=p` and `uk=k`.

If in addition `uY=Y`, then p,k,Y all lie in the REGULAR band `uE(S)` supplied by Section 4. Since `p R k` there, the classical R-congruence property gives

    pY R kY.

But `pY=p f p f g=pfg=H` by idempotency of pf, while `kY=K`. Independently H and K are L-related in the band E(S):

    KH=K,
    HK=H(kf)H=H,

because `D(H)=D(p) meet D(f) meet D(g) <= D(kf)` and `D(k)=D(p)`. Being both R- and L-related idempotents in a band forces equality. Hence `H=K` and N3 follows.

Thus every genuine N3 violation in the locally regular orthodox class must exhibit the STRICT support switch

    fg in uE(S),
    fpfg in vE(S) but NOT in uE(S),
    u(fpfg) != fpfg.                               (SWITCH)

More generally it cannot have a common idempotent left unit j for p,k,Y: those three would all lie in the regular band jE(S), and the same argument would give H=K. In particular a common left unit for u and v excludes the violation.

This is a new necessary support obstruction, not a claim that such a switch exists with the rectangular transport and source lift. Nor is `uY=Y` silently inferred from `ufg=fg` and `p<=u`: that additional absorption is UNPROVED here and cannot replace the actual second N2 equation. The exact still-open band transport implication is

> For every locally regular band, do rectangular p,k,l,r, (B1) and (B2) imply `pfg=kfpfg`?

A positive proof would eliminate the entire N3 obstruction route for the book's orthodox subclass, NOT prove its embedding theorem. A negative band example would still require the source lift stated after (B4). These two proof boundaries are separate.

## 6. A Rees-typed extension of the local-corner validation

This section removes the global-orthodoxy/group-only hypothesis from ONE earlier local validation step; it does not claim the full Rees-typed derivation-completion construction.

Let S be regular and locally r-orthodox. Suppose an actual homomorphism

    q:S -> C

is idempotent pure, with C completely simple. Existence of this q for arbitrary infinite book-class S is NOT assumed proved. Let `p,z,x,y in S`, and suppose for each `t in {z,x,y}`

    q(ptp)=q(p).                                   (RINV)

Choose a mutual inverse `p' in V_S(p)` and put `e=pp'`. For each t define `c_t=pte`.

These are actual elements of eSe, because `ep=p` and `e^2=e`. Write `r=q(p)` and `r'=q(p')`. Then (RINV) gives

    q(c_t)=q(p)q(t)q(e)
          =r q(t) r r'
          =(r q(t) r)r'
          =rr'=q(e).

The last value is idempotent. Purity makes each c_t an idempotent of eSe. Its idempotents form a REGULAR band by local r-orthodoxy, whether or not E(S) itself is a subsemigroup. Therefore

    c_z c_x c_z c_y c_z = c_z c_x c_y c_z.

Right multiplication by p, followed only by `ep=p`, gives

    p z p x p z p y p z p = p z p x p y p z p.      (RLR)

This proof uses neither a global band identity in E(S) nor an orthodoxy assumption. For a group quotient, (RINV) reduces to the earlier inverse-grade condition. For a genuine Rees quotient it retains the row/column constraints rather than discarding the sandwich entries.

Explicitly, if `q(p)=(i,h,lambda)` and `q(t)=(j,k,mu)` in `M[G;I,Lambda;P]`, then (RINV) is exactly

    h p_(lambda,j) k p_(mu,i) = 1.                 (RCOORD)

This is the correct noncommutative order. It is an INNER-inverse condition in C; `q(t)q(p)q(t)=q(t)` is not needed for this lemma. No completely simple factor has been replaced by a rectangular group.

## 7. Cyclic contextual birth also has an exact Rees formula

Retain the hypotheses on S and q in Section 6. Consider nonempty source word w with contexts ell,r, with at least one context present. Do not interpret an absent context as an element of S. Suppose the whole contextual product `ell w r` has idempotent q-image. Let beta be the nonempty cyclic complement `r ell`, omitting either absent context.

Then the literal whole-word equation is

    ell w beta w r = (ell w r)^2 = ell w r.         (RCINV)

The final equality is purity of q followed by idempotency in S. This is a proof of ONE contextual equation, not a common solution of all later equations.

It remains to verify that beta has the correct Rees inner-inverse type for w. When both contexts are present, write

    q(ell)=(i_L,g_L,lambda_L),
    q(w)  =(i_W,g_W,lambda_W),
    q(r)  =(i_R,g_R,lambda_R).

Idempotency of the whole q-image is precisely

    g_L p_(lambda_L,i_W) g_W
        p_(lambda_W,i_R) g_R p_(lambda_R,i_L) = 1.

Let `A=g_L p_(lambda_L,i_W)`, `B=g_W` and `D=p_(lambda_W,i_R) g_R p_(lambda_R,i_L)`. The condition is `ABD=1`, hence `BDA=1`. The middle coordinate of `q(w r ell w)` is `B D A B=B`, and its row/column are those of q(w). Consequently

    q(w beta w)=q(w).

If just ell is absent, idempotency of `q(wr)` gives `q(w)q(r)q(w)=q(w)` by the same two-factor Rees computation; the case of absent r is dual. The case where both contexts are absent is an ordinary loop idempotency step, not a nonloop birth requiring a nonempty beta.

Thus the cyclic complement supplies a genuine Rees-typed contextual birth solution as well as the source equation. The noncommutative sandwich-coordinate condition is checked WRITTEN, not by an interpreter.

## 8. Parkable mathematical boundary

The new reduction (B3)–(B4), the one-sided-ideal lemma, the necessary support switch, and (RLR)/(RCINV) are complete WRITTEN arguments at their named imports. They have not received separate reconstruction or parent acceptance. No claim of novelty, formal proof, Lean/kernel checking, human review or cross-vendor review follows.

Still missing for the ORIGINAL target:

1. In the orthodox N3 route, prove the displayed local-band transport implication or construct a strict counterconfiguration AND its genuine regular source lift. No such configuration/source has been delivered.
2. In the canonical construction route, prove compatibility of ALL later contextual bridge equations or an actual endpoint-separating transformation. Sections 6–7 solve only local Rees typing and one birth equation; they do not solve that compatibility.
3. For arbitrary infinite nonorthodox book-class S, establish an idempotent-pure completely simple quotient outside the already-covered classes. Section 6 explicitly conditions on that prerequisite.

The previously displayed canonical Pastijn map remains a homomorphism, not a proved injection. There is no delivered nonembedding witness or completed embedding proof. The exact next written action is to attack the band transport implication with (B1),(B2) intact; assuming all-context solvability, replacing the source lift by a diagram failure, or returning to an unadmitted table search would not close any of these gaps.
