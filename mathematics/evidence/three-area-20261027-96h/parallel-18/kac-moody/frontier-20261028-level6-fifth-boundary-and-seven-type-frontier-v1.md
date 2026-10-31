# Level-six fifth-boundary transport and the seven-type frontier

MathKacMoody-2, original math-3. Actual `/bin/date` before this new write: **Wed Oct 28 22:20:36 PDT 2026**. **WRITTEN, exact certificate-supported, UNREVIEWED.** Named source/minor inputs below remain substantive; no parent adoption, formal/kernel, independent-model/human or novelty acceptance.

## 1. New actual-boundary theorem

For every allowed FULL complex Cartan realization of the original A(r,s), let S be its original full Serre quotient. On either boundary **r=5,s>=5** or **s=5,r>=5**, ORIGINAL D3 is injective on each ENTIRE primitive source P_(a,b,6)=ker f1 intersect ker f2 for

    (a,b)=(2,2),(3,2),(3,3),(4,3),(4,4),(5,5),(6,6),

and on the mirrors (2,3),(3,4). This is not inferred by extrapolating the r,s>=6 source identification: Section 2 pays the new level-six Serre-seed quotient explicitly.

Inputs: the full-Cartan/free-Levi identification and original lowering conventions in `frontier-20261028-Levi-free-quotient-critical-reduction-v1.md`, Sections 0–4 (including its named level-one and PBW inputs), the complete finite-Levi decomposition interfaces, and the two maximal-minor tables pinned by the boundary certificate. No identity between a free source and a Serre quotient is assumed without the argument below. Equality of those stored tables with actual matrix minors still requires its own reconstruction; the four new full-source/shifted-grid replays are currently running and are not called PASS here.

## 2. Why the actual source does not change on these primitive types

Work in the exact positive fixed-Levi presentation l_+ semidirect FreeLie(V), V=adjoint sl3, with v=e3 its lowest vector and u=e1·v. At r=5 the first repeated-node3 seed is

    q1=(ad e3)^6 e1=-(ad v)^5 u,

of degree (1,0,6). It is nonzero: its tensor expansion has a nonzero v^5u coefficient, with v,u independent in V. By the already fixed local presentation and Jacobi, f1 and f2 kill q1 (f2 commutes with both original letters; the f1 contraction is a repeated ad_v applied to h1 and vanishes after the second step). Its Levi weight is (-4,-7). The finite-dimensional l-module it generates is therefore the irreducible lowest-weight type (4,7), dimension 260. Equivalently finite-sl3 complete reducibility applied to one lowest vector proves this, not an assumed free-presentation quotient. At s=5 the symmetric q2 has degree (0,1,6), type (7,4), also dimension 260.

Through level five neither new seed occurs. At level six the full positive Serre ideal, after imposing the fixed-node1/2 relations, contains ONLY the applicable seed modules Q1 and/or Q2: any bracket with a positive-level free vector would have level >=7; level-zero Levi action generates precisely those modules. This uses the whole positive/negative ideal transport already named in Sections 0–4, so no additional lower-level relation is silently discarded. If both r=s=5, the two nonisomorphic modules have zero intersection. Hence

    S5 = L5(V),
    S6 = L6(V)/(Q1 if r=5, plus Q2 if s=5).

The seven critical primitive types have respective Levi labels

    (4,4),(2,5),(3,3),(1,4),(2,2),(1,1),(0,0),

with dual labels for the two mirrors. None is (4,7) or (7,4). Since the Levi module is completely reducible, the quotient map induces an ISOMORPHISM on each of these lowest-vector spaces: it loses no copy and creates no new copy there. The ACTUAL target S5 is unchanged. Moreover D3(Q1)=D3(Q2)=0 whenever present, by full Serre-ideal stability and the absence of any level-five ideal. Thus the original lowering on these actual primitive spaces is precisely the same affine free-Levi pencil evaluated at r=5 or s=5. This proves the required transport, rather than treating a free rank as an actual quotient rank.

## 3. All fourteen boundary polynomial proofs

Put x=r-6,y=s-6. The boundaries are x=-1,y>=-1 and y=-1,x>=-1. On every selected line, the two specialized maximal minors A(t),B(t) satisfy exact identities

    A(t)=g(t) a(t),    B(t)=g(t) b(t).

Every coefficient of g(z-1) has one weak sign and its constant is NONZERO, so g(t)!=0 for every REAL t>=-1. The certificate gives an explicit finite-field Bezout identity `u a+v b=1 mod p`, with p prime and BOTH quotient degrees preserved on reduction. Hence a,b are coprime over Q[t] and cannot have any common complex root. Therefore the two minors never vanish simultaneously on the whole real half-line t>=-1; at every required integer parameter value at least one actual maximal minor is nonzero. This proves Section 1 after the source transport in Section 2.

Producer `frontier-20261028-level6-boundary-five-positive.py`, SHA `104082bfc7b9044982666b0ecba781cd597889f1f76a723382a042768e6a6883`, checks all fourteen lines. Output `frontier-20261028-level6-boundary-five-positive-v1.json`, SHA `f049b40075c0ff7cc17d94208488e0fa56d3497feca57c62fb7d9e8aa3cd35c8`. Independently authored standard-library replay `frontier-20261028-level6-boundary-five-positive-replay.py`, SHA `6dc04a4f2dd468c1a6c0fc7d6a6e83b4c09c353ad7f03494e0508eb1de156edd`, imports NO FLINT/SymPy/producer, reconstructs both polynomials from every pinned original table/factor source, checks all 28 exact product identities, every shifted-gcd coefficient, all 14 complete Bezout identities, primality and degree preservation. Output SHA `305990e5087b7885b7c400cc7d21eb8dfa541e21826999071028e375234a9696`, PASS in the call ending **Wed Oct 28 22:17:59 PDT 2026**. No Hensel, root search, numerical approximation or finite-box extrapolation is needed in this positive-gcd proof.

## 4. Consequences for the current seven-type frontier

Combine Section 1 with the prior r,s>=6 candidates at their SAME named source/minor cuts. For integers r,s>=5:

| Primitive degree, up to mirror | Current candidate conclusion |
|---|---|
| (2,2,6) | Entire map injective for EVERY pair. |
| (3,2,6), (2,3,6) | Entire maps injective for EVERY pair. |
| (6,6,6), the 20-dimensional invariant space | Entire map injective for EVERY pair. |
| (3,3,6) | At most 7998 exceptional pairs; every fifth-boundary pair now excluded from that exception set. |
| (4,3,6), (3,4,6) | At most 6480 exceptional pairs per orientation, all with r,s>=6. |
| (4,4,6) | At most 19312 exceptional pairs, all with r,s>=6. |
| (5,5,6) | At most 9801 exceptional pairs, all with r,s>=6. |

The last two bounds come from NEW residual pairs of degrees 136/142 and 99/99. Exactly the same positive-factor removal, constant x-leading coefficient, modular y=0 Bezout and projective Bezout argument as `frontier-20261028-level6-336-436-cofinite-candidate-v1.md` applies. Algebra certificates `frontier-20261028-level6-446-fast-pair-algebra-v1.json` (SHA `fa89bc070dc9cb9f1df566815122ffcece87dfbc6838a9f57f2313bdd1eadeeb`) and `...-556-...` (SHA `59696dbb71006afd8d879dce42c9c84ebdd17d5ecb7e7f5637d7ef0792ce27ab`) were replayed by the dependency-free coefficient/Bezout checker. Replay outputs SHA `6e3f7e0f8989d6d9f27ac58ecc0d7e15cd46109598b3e1e57b67e40b2d970095` and `dd59718435b941d4faa1a7e148ab3f4c5982eb48d84396e665eb84b9c22ed893`, PASS in the call ending **Wed Oct 28 22:18:02 PDT 2026**. Stored-minor/source equality is not supplied by those algebra-only replays.

By a union bound the entire displayed primitive bundle can fail injectivity at at most 50071 parameter pairs r,s>=5, with every possible exception strictly inside r,s>=6. This bounds a sufficient finite certificate's unresolved locus, not actual kernel counts or existence. The omitted coordinate-boundary primitive types and lower-level predecessor obligations are NOT discharged by this bundle. In particular **no F6/B6 or whole-band Serre theorem follows here**. The regime min(r,s)<=4 remains a genuine actual-ideal/target-quotient problem.

All conclusions remain candidates until full scientific review and parent disposition. Direct native resultant jobs have not returned a verdict and are not inputs. Earlier immutable process findings and quarantines remain historical; no held guide is accepted as a premise.

**END — exact fifth-boundary transport and fourteen-line proof, with explicitly conditional seven-type frontier; original broad target still open.**
