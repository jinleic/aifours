# A four-relation globally regular-band obstruction for the 68-source

**Status: NEW AUTHOR WRITTEN PROOF plus exact finite controls; UNREVIEWED / UNADOPTED.** This strengthens the B5-power-only obstruction in `frontier-20261028-quotient68-sixband-host-and-obstruction-v1.md`, SHA `b24ce079030e75e6f1d5dfaa2a88696f4531eb53963f507c0876d4b0ad9f599c`, to **all globally regular bands**. It does not rule out the seminormal/locally-regular bands of the original problem: the same source has the explicit faithful SN host in that predecessor.

## 1. A universal four-relation band lemma

Let B be a regular band, `xyxzx=xyzx`. Suppose in B that

`E=v p q`, `F=v q=u p q`, and `F E=E`.                  (1)

Then E=F. Indeed, substitute `x=q`, `y=v`, `z=p` into the regular-band identity and multiply by v on the left:

`v q v q p q = v q v p q`.

Since `(v q)²=v q`, this says

`(v q)(p q) = (v q)(v p q) = F E = E`.

But `F=u(pq)` and `(pq)²=pq`, so `F(pq)=F`. Thus E=F. This proof does not use the opposite Green relation, commutativity, a finite-band hypothesis, or a computer search.

## 2. Exact source instantiation

For the 68-element S and its actual 8-element pure-CS actor q in the predecessor, use the source indices

`v=8`, `p=24`, `q₀=53`, `u=60`, `e=37`, `f=61`.

The source table has

`8·25=37`, `8·53=61`, `24·53=25`, `60·25=61`, and `61·37=37`.

Each of these products has actual physical group weight 0. The 68-source data additionally verifies e≠f and `q(e)=q(f)`. For any physical homomorphism over the actual q, denote band coefficients by c; then the four source relations yield

`c_e=c_8 c_24 c_53`,
`c_f=c_8 c_53=c_60 c_24 c_53`, and `c_f c_e=c_e`.

By §1, `c_e=c_f` in every **globally regular** band. Since the actor coordinates also agree, any such actual-q physical map identifies the two distinct source idempotents. Hence no faithful globally-regular-band physical host exists over actual q.

Under the separately unreviewed all-actor restriction/onto pushforward in `frontier-20261028-regular-source-any-actor-characterization-v1.md`, SHA `73d3951b03ecdbc6574a21753665e612c28aa0570158e7936a7228e36deade5d`, any faithful globally regular-band host over an arbitrary CS actor would yield one over actual q, retaining the band up to product with a rectangular band. Products/subbands of globally regular bands are globally regular, and rectangular bands are globally regular. Subject to that exact named transport, S has **no globally-regular-band-by-any-CS host**. Without that import, only the actual-q statement is asserted.

## 3. The crucial nonextension to the original band variety

The six-element SN band C of the predecessor satisfies the same four coefficient equations with

`(v,p,q,u,E,F)=(5,3,2,0,1,0)`.

In particular `E≠F` and `F E=E`: its table gives `5·3·2=1`, `5·2=0=0·3·2`, and `0·1=1`. The exact checker verifies C's 1,296 seminormal substitutions and associativity. Thus the lemma is **false for seminormal/locally regular bands**; applying it to all permitted original hosts would be wrong. The actual 68-source embeds in `P(C^5,D)` by the pinned 68×5 witness, so this is emphatically not a Q1 counterexample.

## 4. Checks and source provenance

`frontier-20261028-quotient68-regular-collapse-checker-v1.py`, SHA `aa209250b31c29b8eede4bd2dfe6d2b497674206ded5763872f1466e7d09806f`, executed in the Python eval kernel before Wed Oct 28 21:58:20 PDT 2026, rechecks the six source products including both R directions, all six zero action weights, q(e)=q(f), and the SN-band separating countermodel. It is independent of Z3 but shares the author's source data with the predecessor.

As a search aid, `frontier-20261028-rrb-source-relations-certificate-v1.py`, SHA `719ae65816da1e6080ecdae0e4a349df10228da99a5f6caf17fe0cdddd20587e`, checked a 1,956-word free right-regular band congruence and exposed the short factorization argument; the written §1 proof is stronger and does not rely on this program or on the right-regular subcase. No cross-model/human review, formal proof, independent finite-witness certification, novelty or universal original-class conclusion is claimed.
