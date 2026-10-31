# Exact optimum after the full tested gluing-inequality family

**Status: WRITTEN with independent exact primal checks and matching published dual.** This is a separately scoped successor to `frontier-20261028-crossbranch-star-optimum-v1.md` (SHA-256 `1fb4cb0a74fd288e7fd96aaa2aba50b21901cd4385fa845ba28aa4a1656a54bf`). None of the publisher-LP or preceding star inputs was edited. This result is not an entropic realization and does not improve the original guessing-number upper bound.

## Added universal constraints

The 16-term inequality `L(X,D,F)>=0` and its conditional-gluing proof are in `frontier-20261028-universal-gluing-inequality-v1.md` (SHA-256 `a017351d672c37c170b5dff4cf6ce76467f5d2460fa04ce81d922de660b48dce`). It is valid for **every** finite joint entropy law and, by linearity/closure, for almost-entropic vectors. Its exact term map is separately pinned in `frontier-20261028-universal-gluing-term-map-check-result.json`, SHA-256 `26ef7de315636d0e0aad1728567953ea0b00e96467bc424f04e561d722a0c1ab`.

Use the star LP from the predecessor: two full 14-variable Shannon systems `(X,U,V)` and `(X,U,W)` sharing all `(X,U)` entropies, source-copy equalities and conditional independence of `U` from each other auxiliary branch given `X`. Add every instance of the one inequality `L>=0` obtained by

* choosing `D` among the three components of `V` and `F` among the three components of `W`; and
* assigning its four active original-variable roles to any ordered four distinct vertices, with the remaining six original variables as background.

There are `9*10P4=45,360` checked instances. Every term of each lies wholly in `(X,D)` or `(X,F)`, so its coordinates already belong to one of the two star systems. This is one universally valid inequality family; it is not a claim about all non-Shannon inequalities.

## Exact no-improvement result

The augmented LP, also including the predecessor's all-positive-`n` disjoint original-variable `F_n` family, has exact optimum **`1847/276`**. The common original profile again has all ten singleton values 1 and `h(X)=1847/276`.

* `(X,U,V)` is the same separately checked cross12 primal `frontier-20261028-crossbranch12-exact-candidate.json`, SHA-256 `1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739`.
* `(X,U,W)` uses the same 2,047 nonempty `(X,U)` entropy coordinates, but a new independently checked auxiliary assignment `frontier-20261028-crossbranch13-all-cuts-exact-candidate.json`, SHA-256 `1d7263364c8c543bdd07a4b140c7a7ab2d65753c38506f26c02072fc9bd29703`.

The second independent verifier reconstructs all 14-variable elemental Shannon rows and named copy/coupling equations, validates all applicable source rows, and separately evaluates **all 45,360** exact integer-scaled gluing instances; their minimum is zero. The combined verifier binds the shared profile, both independent primal receipts, all `1,920` publisher dual rows and the all-order base receipt. The feasible exact rational primal attains the unchanged published exact dual upper bound. Thus these particular universal inequalities, despite cutting the old star point, do not lower this LP optimum after auxiliary reoptimization.

This new primal is different from the earlier star primal and the old 4,397-coordinate partial assignment. The earlier star point's separation from the projected almost-entropic cone remains valid for its own fixed auxiliary values; passing this one family does not establish that the new point is entropic or almost-entropic. Rows mixing `V` and `W` in the full 17-variable Shannon system, additional universal inequalities or copy structures, and actual positive-gap FD laws remain open.

## Evidence

* All-cut producer `frontier-20261028-crossbranch13-all-cuts-exact.py` SHA-256 `c2a9cde983eb61d6f13533dceca7a7614a3cc2c2da06a7e7607349e4d548fe8d`; producer result SHA-256 `d76b3dc97684ffd93b573db5b5963a64afc5c5ebc0be0b2922f2d3054b51902b`. IPM supplied only a proposal; exact affine reconstruction and separate checks provide the evidence.
* Independent all-cut/14-variable verifier `frontier-20261028-crossbranch13-all-cuts-independent-check.py` SHA-256 `6114eec091790dfb8813ff58630486cfad0c6605ebecd8c14110bf03a518f621`; receipt SHA-256 `2575991ec2e5fc62fa3b606d5884dddb9d98f1ba270eae6d882cb641ecb4c76c`. It checks `372,750` Shannon rows, `1,539` copy equalities, seven coupling equalities, `1,491` applicable source rows, all 45,360 gluing cuts and six intended mutations.
* Independent combined binding checker `frontier-20261028-crossbranch-all-cuts-combined-check.py` SHA-256 `1b2e5f0323987a0f7d3c00149ff4ad44e0d32785d1d8678f5393a405c414c014`; receipt SHA-256 `e5bc0967f9e7ae84722a6fa9346c4a8fb1afa3d109a8041b89dc52a81ce39377`. It pins both candidate/checker receipts, shared profile, all publisher rows and dual, and the earlier all-order base receipt; its cross-only mutation controls are rejected.
* The published source dual, original graph/copy correspondence and `F_n` proof retain the review boundaries documented in the predecessor. No cross-model review, proof-assistant check or novelty clearance has been performed.
