# The local-band transport closes: N3 holds throughout the orthodox book subclass

MathSemigroup, math-4. Actual precreation clock: **Sun Oct 25 04:28:24 PDT 2026** (`/bin/date`).

**Status: WRITTEN; not independently reconstructed, not parent accepted, NOVELTY_UNCLEAR.** No scientific computation, table, checker, symbolic interpreter, solver, execution or nested agent. The proof is written semigroup algebra. This is NOT a full embedding theorem and NOT a nonembedding obstruction.

## 1. Additive correction and exact theorem

This is an additive successor to `n3-local-band-transport-v1.md`, SHA-256 `81648c29fd4d97085f6dc440c213fd031f24db206fac2b3dcc18349df8c28aae`. Preserve that packet. Its Sections 5 and 8 describe the band transport implication as open at creation; the proof below CLOSES that implication. The suggested N3 source lift is therefore no longer a live counterexample route in this class. The original target's all-contextual compatibility, arbitrary-infinite pure quotient, and full embedding gaps are NOT closed by this addendum.

**Theorem.** Let S be an orthodox E-unitary regular semigroup whose band E(S) is locally regular. Let `a,A,b,B,e,f,g` satisfy

    a sigma b,   A in V(a),   B in V(b),   e,f,g in E(S),
    eaA=e=ebB,
    Bb f Aea f g = f Aea f g.                      (T)

Then

    ea f g = eb f Aea f g.                         (N3)

There is NO finite-cardinality, C2-grading, group-commutativity, pairwise-distinctness or global regular-band hypothesis. The usual additional N2 premise `Aafg=fg` is not needed for this theorem.

Consequently the written N3 witness protocol cannot yield a qualifying countermodel in the orthodox book subclass, at ANY order or any group grade. This is a mathematical exclusion conditional only on the explicitly named classical imports, not a search miss or a finite computation. It does not turn the known necessary N3 condition into a sufficient embedding criterion.

## 2. The band lemma that was missing

**Band transport lemma.** Let D be a locally regular band. Let p,k,l,r form a possibly degenerate 2-by-2 rectangular subband with

    kl=p,   kr=k,   lr=r,   rl=l.

Let v be an idempotent satisfying `vr=r`, and let Y belong to D with `vY=Y`. Then

    pY R kY.                                      (BT-R)

If in addition `(kY)(pY)=kY`, then `pY=kY`.

**Proof.** Since `rl=l`,

    vl=v(rl)=(vr)l=rl=l.

Thus l,r,Y all lie in the principal right ideal vD. By the completely written one-sided-ideal lemma in the predecessor's Section 4, vD is a REGULAR BAND. The equations `lr=r` and `rl=l` mean `l R r` in that very band. Its R relation is a congruence, so

    lY R rY          in vD.

R is a left congruence in EVERY semigroup: if `s=t u` and `t=s w`, then `ks=(kt)u` and `kt=(ks)w`. Therefore, in D,

    k(lY) R k(rY),
    pY R kY.

This is (BT-R). Both values are idempotents. For R-related idempotents P,Q, `QP=P`; the additional assumption says `QP=Q`. Hence P=Q. QED.

This proof is the representation change that resolves the previous blockage: use the regular principal right ideal **vD**, not an unproved inclusion `Y in uD`. The last N2 equation already supplies `Y in vD`. The rectangular row l,r can be multiplied there first, and only THEN transported by left multiplication k. No external right translation is asserted to preserve R.

## 3. Substitution giving the exact formerly open implication

For arbitrary idempotents f,g of D set

    H=pfg,       Y=fpfg=fH,       K=kY.

Then

    pY=p f p f g=(pf)^2 g=pfg=H,
    KH=k f H H=k f H=K.

Consequently `vr=r` and `vfpfg=fpfg` imply H=K by the band lemma. Thus in EVERY locally regular band,

    rectangular p,k,l,r,
    vr=r,
    v f p f g=f p f g
        ==> pfg=kfpfg.                            (BT)

Even `rv=r`, the support u, `p<=u`, and `ufg=fg` are unnecessary. The narrower implication stated as open in the predecessor follows immediately. A strict counterconfiguration satisfying that predecessor's full premises cannot exist.

## 4. Complete substitution back to the regular source

Take the least group map pi of S. Its kernel is idempotent pure by the named E-unitary characterization, so `pi(a)=pi(b)=h` and all inverse-grade products below are actual idempotents.

Use the predecessor's direct calculation, reproduced here so the main theorem does not depend on an unproved minimum-inverse-congruence claim:

    x=ea, y=eb, c=Ae, t=Be,
    xc=e=yt, ex=x, ey=y, ce=c, te=t.

Purity gives `(cy)^2=cy`. Multiplying on the left by x and right by t gives

    (xc)y c(yt)=(xc)(yt),
    e y c e=e,
    yc=e.

Similarly `(tx)^2=tx`, multiplied on the left by y and right by c, gives `xt=e`.

Put

    p=cx, k=cy, l=tx, r=ty, v=Bb.

They are idempotents. The equations `xc=yc=xt=yt=e` give the required rectangular multiplication, in particular

    kl=c(yt)x=p,
    kr=c(yt)y=k,
    lr=t(xt)y=r,
    rl=t(yc)x=l.

Moreover

    vr=BbBeb=Beb=r.

The last premise in (T) is exactly

    v f p f g = f p f g.

Apply (BT) in D=E(S) to obtain

    pfg=kfpfg.

Finally left multiply by x. Since `xc=e`, `ex=x`, `ey=y`,

    x(pfg)=x c x f g=ea f g,
    x(kfpfg)=x c y f p f g=eb f Aea f g.

This proves (N3). The premise `Aafg=fg` was nowhere used. QED.

## 5. Named imports and verification boundary

The nontrivial classical imports are exactly:

1. E-unitary regular implies orthodox and idempotent-pure least group congruence (Hartmann thesis Theorem 2.1; actual source bytes/pin listed in the predecessor).
2. R is a congruence on a regular band. This is the standard regular-band structure theorem: regular bands are subdirect products of left regular and right regular bands. In a left regular band R is equality; in a right regular band R is D, a congruence. The idempotent equations characterizing R make this preservation pass to the subdirect product. No more general locally regular R-congruence theorem is assumed.

The principal-right-ideal lemma is PROVED in the predecessor, not imported. R being a left congruence, R's idempotent multiplication criterion, inverse equations and associativity are elementary definitions/properties used explicitly above. The D-semilattice import of the predecessor is not needed for this addendum's proof.

Hartmann's necessary N3 theorem is relevant only for identifying the retired obstruction route; the new positive N3 implication itself does not invoke that necessary theorem or its proof. The older source-dependent reduction from P/R hosts to band-by-group hosts is likewise not needed to prove this addendum.

This is a complete WRITTEN proof at those imports. No claim of Lean/kernel verification, source-free proof of the band structure theorem, independent reconstruction, parent acceptance, novelty, human/cross-vendor review or publication.

## 6. Remaining original gap and immediate effect

- **N3 route:** CLOSED NEGATIVELY AS A COUNTEREXAMPLE ROUTE for all orthodox book-class sources, subject to reconstruction of this written proof. No generated checker or admitted execution exists or is needed to state the theorem. The protocol remains an unchanged historical preparation, not a renewed search instruction.
- **Full embedding:** STILL UNPROVED. N3 is only one necessary host condition. The canonical homomorphism still lacks endpoint/idempotent separation; all-later-contextual compatibility is open.
- **Nonorthodox/infinite:** the predecessor's Rees-typed local-corner and one-birth identities remain valid at the assumed pure completely simple quotient, but neither its existence for every infinite source nor all-context compatibility is established.

The exact next mathematical obligation is now the genuine canonical separation/all-context construction, or a DIFFERENT source-valid obstruction. Another N3 table search, another helper grading, or a band counterconfiguration to (BT) would contradict the delivered written theorem rather than advance this task.
