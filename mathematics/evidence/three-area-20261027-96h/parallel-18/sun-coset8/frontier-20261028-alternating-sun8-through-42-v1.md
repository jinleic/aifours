# Alternating Sun8 through offset 42, conditional on Sun7 and R8

**Status: WRITTEN candidate, conditional on the explicitly named Sun7/R8 written imports, public A_r theorem and unreviewed exact quotient/factorial proofs; not independently reviewed, formally verified or accepted.** Let r≥419 be a prime not of the form (q^d−1)/(q−1) for any prime power q and d≥2. For 1≤t≤42 with r+1>7t!, the group A_(r+t) satisfies Sun(8), **provided** the stated Sun7 and R8 interfaces and the other inputs hold. This includes all residue classes at t=41,42. It does **not** establish direct P7 there: direct P7 is a stronger subgroup-index exclusion, and the saturated seven-cell frontier remains open for that question. No unrestricted all-alternating/global, published-priority or historical-novelty claim is made.

## 1. Exact conditional imports

- **S7:** the literal all-groups Sun(7) written-composition statement in `institute/runs/six-lane-2026-10-18-96h/review/sun7-complete-written-composition-parent-verdict-v1.md`, SHA-256 `94abd506aec9879e294a5eb84129794af0c7ac78917b091d2f2c113d665c34f2`. Its parent status is written-composition acceptance at its named dependency/errata scope, not human, formal, Lean, priority or public-proof verification.
- **R8:** the prior Sun7-relative reduction in `mathematics/evidence/three-area-20261023-96h/parallel-18/sun-coset8/reduction-and-generation-v1.md`, SHA `fa0497ae15bd3c765e05123996e4a94bd8038f2be1488b08dc7111f2fd7602c6`, Theorem R8: a Sun8 counterconfiguration has eight indices all pairwise gcd exactly 7. The earlier parent normal-section record supported that bridge at its own scope; the reduction is prior work, **not a new discovery** here. Its full Sun7 proof DAG is not replayed in this packet.
- Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2, plus the **unreviewed** exact quotient/window argument in `frontier-20261028-alternating-seven-cell-p7-v1.md`, SHA `5b359f8e23db44d4064646db971ab33e643f03b103eb927b9e74c9f90f46d80f`, and the **unreviewed** general factorial incompatibility lemma `frontier-20261028-alternating-factorial-general-v1.md`, SHA `83f5f6884f76466408bc48cd264aa12f61b030ba1a338641c4af54e547c7d05a`.

The writer was nonblind and the incidental cross-topic display is recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`. No such excerpt is used and no historical hold is rehabilitated.

## 2. Conditional proof

Assume eight pairwise disjoint left cosets in A_(r+t) have all index gcds at most 7. The imported S7/R8 statements imply all eight indices have pairwise gcd exactly 7. At most one is divisible by r>7, so at least seven are r-free. No index can be divisible by (r−2)!: such an index has another r-free index with gcd 7, contrary to the named general factorial lemma.

For each r-free label, the named exact projection/quotient chain therefore terminates at a full alternating block. Since the index is divisible by 7, that chain consumes at least one position h with 7|(r+h); otherwise each binomial window has length at most 6, its numerator and denominator are 7-free, and its exact quotient c|u! is 7-free. Different labels cannot consume the same cell, because the retained factor (r+h)/gcd(r+h,t!)>7 would divide both indices. Yet t≤42 consecutive positions contain at most ceil(42/7)=6 seven-cells. At least seven r-free labels require seven distinct cells, contradiction.

For t≤35 the earlier direct-P7 argument does not require S7/R8. For t=36,…,42 this packet proves only the **conditional Sun8** conclusion, with the separately named direct-P7 residue-class results retained at their own scopes. In particular the t=41 saturated six-label local model is not contradicted, since this argument requires seven r-free labels from eight cosets.

## 3. Control and review scope

`frontier-20261028-alternating-saturated-seven-check.py`, SHA `7bea97eb7487287079fa32ee5074e9ae227de834487d2b461b041c8e5e27202b`, 30 LF / 945 bytes, was run at 19:37:09 PDT and checked exact local 7-valuations for selected r at t=41; this is **not** a verification of Sun7, R8, any subgroup classification or the universal argument. The cell count at t≤42 is the elementary observation that six multiples of 7 fit in any block of 42 integers, not a numerical theorem input.

**Review-critical:** verify the old S7/R8 scopes and mandatory overlays, exact quotient and factorial inputs, seven-versus-eight label count and disjointness. No independent/formal/human review, global closure, historical novelty or old-hold modification is claimed.
