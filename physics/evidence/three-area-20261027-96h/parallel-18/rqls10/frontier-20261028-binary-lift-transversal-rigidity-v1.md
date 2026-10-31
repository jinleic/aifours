# High-degree binary phase lifts preserve absence of transversals

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED; one explicit q18 vector example independently checked.** Native `/bin/date` at sample check: **Wed Oct 28 19:44:48 PDT 2026**. This advances into a genuine q18 family beyond the q<=17 catalog frontier, but does NOT classify all BH(10,18) matrices or settle general QLS10.

## 1. General fixed-transversal rigidity

Let H be ANY n×n matrix of unit phases in a field F containing `zeta_n`, and let R be ANY n×n {0,1} mask. For a unit complex number z, set

`K_(t,c)(z)=H_(t,c) z^R_(t,c)`,
`psi_(r,c)(z)(t)=zeta_n^(r t) K_(t,c)(z)/sqrt(n)`.

Suppose z is transcendental over F, or algebraic of degree GREATER THAN TWO over F. If a fixed set T of n cells is an orthogonal transversal for psi(z), then **the SAME T is an orthogonal transversal for psi(z') for every unit complex z'**, in particular for z'=1. Indeed each pairwise inner product has the form

`sum_t zeta_n^((s-r)t) conjugate(H_(t,c)) H_(t,d) z^(R_(t,d)-R_(t,c))`,

with coefficients in F and exponents only -1,0,1. Multiplying by z gives a polynomial of degree at most2. If it vanishes at z, the degree hypothesis forces the polynomial to be identically zero. This holds separately for all pairs in T. All cell norms remain1 at any unit z'. No uniform-overlap, maximal-cardinality or K(z) Hadamard assumption is used in this implication.

Therefore if the base H has NO transversal, neither does K(z). More generally, for fixed H,R each candidate transversal that does not already work at z=1 is confined to at most2 algebraic exceptional values of z; if H has no transversal at1, at most `2*n!` values in total can admit one. This is a finite-union bound, not a statement that any exceptional value actually works.

If K(z) IS Hadamard at such a degree>2 z, the same polynomial argument applied to all K-column pairs shows K(z') is Hadamard for EVERY unit z'; in particular it is a genuine affine phase family, rather than an accidental isolated Hadamard at that z.

## 2. Concrete q18 consequence

Take n=10, H any BH(10,6), F=Q(zeta30), and z=zeta18. The compositum is Q(zeta90), and

`[Q(zeta30,zeta18):Q(zeta30)]=phi(90)/phi(30)=24/8=3`.

The catalog-conditional, independently certificate-replayed no-transversal theorem `frontier-20261028-all-bh10-6-product-no-transversal-v1.md` SHA **ae707c663690643c541edea9c54927672d48b9d561b4477a484e2d8bbb85b3de** therefore gives **NO T** for every QLS with

`K_(t,c)=H_(t,c) zeta18^R_(t,c)`, `R_(t,c) in {0,1}`,

including arbitrary K row/column phase gauges and permutations. The conclusion is conditional on the cited q6 classification/certificate result; it does not assert that every BH(10,18) has this binary-lift form. The same general argument applies whenever the cyclotomic extension degree exceeds2, e.g. binary q5->q25 and q12->q36 lifts using their corresponding no-T bases.

## 3. An actual new maximal QLS(10) in this q18 family

A nontrivial example was constructed from the FIRST Aalto BH(10,6) representative by multiplying the rectangle `rows={0,1}`, `columns={0,1,2,3,4}` by zeta18. `frontier-20261028-q18-binary-lift-v1.py` SHA **e5a227ae8bb35d95b45b855e47b103bff869008e96e5834f99aa544cc7df8662** derived the rectangle from exact vanishing partial row sums; its explicit K exponent table is `frontier-20261028-q18-binary-lift-result-v1.json` SHA **8d590dcbfab0f87bb04ed587003bbdd73b219e96fd4a5028cbb0b07d41f36f2c**.

Independent original-vector verifier `frontier-20261028-q18-lift-vector-check-v1.py` SHA **0726160af66f0c16cb38c9432a47eab0d63b6b3aa9682ca2bbce2894ad5d0b03** constructs all100 actual vectors in Q(zeta90), checks all20 row/column ONBs and all4950 ray pairs, and exhaustively tests ALL transversals for this ONE array. Actual output:

```text
PASS exact 100 norms,20 original row/column ONBs,4950 distinct ray pairs
PASS gauge-invariant q18 crossratio exponent 1 not a sixth root
transversal_found False complete_nodes 11
PASS all actual transversals excluded for this explicit sample only
```

The cross ratio `K_(r,c) K_(s,d) conjugate(K_(r,d) K_(s,c))=zeta18` for r inside the rectangle, s outside, c inside, d outside is invariant under row/column phase gauges; since it is not a sixth root, this K is NOT gauge-equivalent to a BH(10,6) matrix, even allowing row/column permutations. Thus the q18 family and the sample are not merely relabeled q6 matrices. It is an actual **100-ray QLS** but emphatically NOT a 1-RQLS.

## 4. Remaining gap

General BH(10,18) matrices with three residue levels or otherwise outside the binary-lift hypothesis, other q and continuous exceptional z, arbitrary nonproduct arrays and unrestricted 1-RQLS10 remain open. The no-T implication's degree premise and the imported base theorem require independent review; exact sample checking is not a formal proof, general classification or novelty clearance.
