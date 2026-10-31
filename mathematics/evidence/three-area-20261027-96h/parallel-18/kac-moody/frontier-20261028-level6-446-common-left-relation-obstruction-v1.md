# An exact 446 relation forbids identical invertible left images

**MathKacMoody-2 / math-3.** Native clock before this additive write: **Wed Oct 28 19:39:39 PDT 2026**. This is an exact-program-assisted negative result for a specified linear-algebra normalization, UNREVIEWED; it is not a D3 kernel, parent/formal/human/independent-model, novelty or priority verdict.

## 1. Exact all-operator obstruction

Use the same entire **1780 target-row/162 source-column** original level-six `(4,4,6)` pencil `D=A+mL+dK` and named full-Cartan/free-Levi/PBW inputs of `frontier-20261028-level6-446-full-target-accretivity-obstruction-v1.md`, SHA `9f33be3c50520ae08deeb6cb318b00e959e0e2e8e8d82ef7442cf06a741d3ac0`. Here `A=D(6,6)` and `L` is the diagonal-parameter leading operator; both have rational entries in the faithful tensor-word host.

The new exact certificate supplies TWO integer vectors `u,v in Z^162` such that

\[
Au+Lv=0\quad\text{in EVERY one of the 1780 full target rows},\qquad u+v\ne0.\tag{1}
\]

The first coordinate of `u+v` is exactly `745188412809525652990927884`. Both complete vectors are listed in the pinned witness JSON. They are NOT proportional; this relation is not of the form `(A+cL)u=0`.

It follows immediately that there is **no** linear map `T:C^1780 -> C^162` with

\[
TA=TL=G\quad\text{for any invertible }162\times162\text{ matrix }G.\tag{2}
\]

Indeed applying T to (1) gives `G(u+v)=0`, contradicting invertibility. This rules out every real or complex left test with IDENTICAL invertible images of A and L, not only a scalar `L+gamma A` or a finite list of candidate tests.

## 2. How the relation was found and checked

The search used a full-target integer-scaled `[A L]` matrix, 200 pivots modulo prime32749, modular solves and rational reconstruction over twelve distinct small primes to propose a relation. The modular rank is a LOWER bound on the rational rank; this paper does NOT claim the exact rational rank is200. The modular calculations serve only as a search mechanism.

The resulting two integer vectors were then checked by **direct exact rational summation in ALL 1780 target rows**, independently of the search's CRT reconstruction, and their sum was checked nonzero. A separately authored replay reads the immutable full target and vectors, repeats every row sum with Python Fraction arithmetic, verifies the displayed first coordinate of `u+v`, and verifies that u and v are not proportional. This is an exact certificate of (1); it does not require trusting a modular-rank upper bound or a numerical fit.

|Owner-root artifact|LF|SHA-256|
|---|---:|---|
|`frontier-20261028-level6-446-common-left-relation-search.py`|110|`5329681a70f0cd5e420e2847b2c822f3bbaaaa519e9b45d240534a8cd5b5972e`|
|`frontier-20261028-level6-446-common-left-relation-search-v1.json`|366|`dd409b42568b9bff4547eee0dc70c31f59ba5b848736b4b7fe97907984ca5f42`|
|`frontier-20261028-level6-446-common-left-relation-replay.py`|37|`29652f6f36cf98fa2e62cbe751b97f31ba2fe46310763620cedb239bfc248a0a`|
|`frontier-20261028-level6-446-common-left-relation-replay-v1.json`|16|`dd13f6516fa5bea9e5e28842da173f42f04d281c60e57d62d13dfd9fd16228fd`|

The search returned `EXACT_RELATION_OBSTRUCTS_EQUAL_LEFT` at **19:37:46 PDT**; the independent full-row verification returned `PASS exact relation on all1780 rows, u+v nonzero, u/v not proportional` at **19:39:11 PDT 2026-10-28**. The underlying target pencil is itself a separately replayed new source; all source/ideal/PBW and shared-helper qualifications remain.

## 3. Strict nonclaims

(2) forbids only the special normalization `TA=TL` with a common invertible image. A left operator may have DIFFERENT invertible/positive Hermitian images of A and L, and its existence is not decided here. The vectors u and v are different inputs, not a single source vector killed by the original pencil. Hence (1) is not a non-Serre witness, full D3 kernel, integer-parameter counterexample or an obstruction to every possible ratio-cone argument. The previously given 446 cofactor cone and staged replay remain unchanged and await the parent gate/review. Prior incidental older cone-status methodological exposure and all ZERO/STOP/HOLD/process findings remain as disclosed.

**END — exact full-target obstruction to one overly strong common-left normalization only.**
