# Nonuniform Fourier–Hadamard product QLS: transversal root-length obstruction

**NEW WRITTEN AUTHOR CANDIDATE, unreviewed.** Native `/bin/date` before writing: **Wed Oct 28 18:04:38 PDT 2026**. Unlike the preceding M_* results, this theorem does NOT impose uniform overlaps or maximal cardinality. It is nevertheless restricted to a specific Fourier–Hadamard product construction and stated finite phase alphabets; it is NOT an unrestricted QLS10 no-go or a novelty claim.

## 1. Exact physical-vector family and theorem

Let n=2m>=4, zeta_n be a primitive n-th root of unity, and K be an n×n matrix whose entries have modulus1. Consider the ACTUAL n×n vector array

`psi_(r,c)(t) = zeta_n^(r t) K_(t,c) / sqrt(n)`,  `r,c,t in Z_n`.     (1)

Every vector is unit. Every fixed column c is automatically an ONB because its inner products are ordinary cyclic character sums. The array is a QLS exactly when the columns of K are pairwise orthogonal, i.e. `K* K=n I` (a complex Hadamard matrix). This statement is about the SAME vectors, not independent scalar overlaps.

Assume that, after arbitrary row/column phase multiplications of K, every K entry is a q-th root of unity. Equivalently, `K_(t,c)=d_t lambda_c eta_(t,c)` with unit d_t,lambda_c and eta_(t,c)^q=1. Common unitary changes of the physical vectors, arbitrary cell phases and row/column relabellings are also allowed; they do not change the existence of a transversal.

**Theorem A (all even n).** If (1) is a QLS and has even ONE orthogonal transversal, then there exists a vanishing sum of m q-th roots of unity. Hence:

- if `q=s^e` for a prime s, necessarily **s divides m**;
- if `q=p^a r^b` for distinct primes p,r, necessarily **m belongs to pN+rN**.

**Original order10 corollary.** For n=10 (m=5), the entire actual-vector family (1) has NO orthogonal transversal, and hence no 1-resolution of ANY L, if K's phase order is a prime power s^e with s!=5. For q with exactly two distinct prime factors p,r, it has NO transversal unless one factor is5 or `{p,r}={2,3}`. This conclusion does NOT need maximal cardinality or uniform overlaps. It does not settle phase order5^e, q containing5, the {2,3} two-prime family, orders with three or more prime factors, arbitrary phase K, or non-product QLS.

## 2. SAME-column Hadamard and opposite-row calculation

For fixed r and c!=d,

`n <psi_(r,c),psi_(r,d)> = sum_t conjugate(K_(t,c)) K_(t,d)`.

Thus a row is an ONB iff all K columns are orthogonal, and because K is square with unit-modulus entries this is precisely `K* K=nI`. For fixed c and r!=s,

`n <psi_(r,c),psi_(s,c)> = sum_t zeta_n^((s-r)t)=0`,

so columns are actual ONBs independently of K's phases.

Suppose T is ANY transversal ONB. It meets each row and column once, so in particular it contains cells `(r,c)` and `(r+m,d)` with c!=d. Since K is Hadamard,

`E+O=0`, where `E=sum_(t even) conjugate(K_(t,c))K_(t,d)` and `O` is the sum over odd t.

Since those two SAME cells of T are orthogonal and zeta_n^m=−1,

`E-O = n <psi_(r,c),psi_(r+m,d)> = 0`.

Over C this gives **E=O=0**. Each is a sum of exactly m unit phases. With the stated K gauges, `conjugate(K_(t,c))K_(t,d)` equals the common cell-column phase `conjugate(lambda_c)lambda_d` times a q-th root; the d_t phases cancel. Removing the one common nonzero phase gives a genuine vanishing sum of m q-th roots. No selected transversal or L is assumed; any putative T supplies the pair.

## 3. Prime-power and two-prime length conditions

For q=s^e and primitive zeta_q, write a vanishing m-term sum as an integer polynomial F(zeta_q)=0 with F(1)=m. Its irreducible monic cyclotomic polynomial

`Phi_q(X)=sum_(j=0)^(s−1) X^(j s^(e−1))`

divides F over Z, so evaluating at1 gives `s=Phi_q(1) | m`. Irreducibility follows from Eisenstein applied to Phi_q(1+X), as detailed in `frontier-20261028-uniform-prime-power-phase-obstruction-v1.md`, SHA **2b9ac43797a5720e01746dda9f3343c3ea9227f7dcae36f2f1d7c9ddcd7c8467**. This is a general length lemma; no uniform QLS premise from that earlier theorem is imported.

For q=p^a r^b with p!=r, the exact nonnegative-multiplicity proof in `frontier-20261028-uniform-composite-phase-obstruction-v1.md`, SHA **b69c642590aa1aee9ffe35bf26b9d7cb65768c0f26021bec873e9d02fd50a9bd**, gives `m=p A+r B` for nonnegative integers A,B. Briefly, use the product cyclotomic power basis, group exponents by the lower residues and reduce each p×r count matrix; vanishing forces `N_ij=a_i+b_j` with nonnegative integer a_i,b_j, so each group's length is `r sum a_i+p sum b_j`. Summing groups proves the asserted necessary condition. It is a number-theoretic statement, not an inference from the earlier candidate's status.

For m=5, a single prime divisor must be5. For distinct primes p,r, the equation `5=pA+rB` has a nonnegative solution only if one prime is5 or the pair is {2,3}. This proves the stated all-resolution order10 exclusions. The degenerate q=1 case is immediate because a sum of m identical unit phases is nonzero.

## 4. Exact local checks and NONuniform search

`frontier-20261028-hadamard-half-sum-check-v1.py`, SHA **798cc16637b9a31ca2931f2d2c52004bf26491c3077f530aa9ca45a306539e83**, enumerates five-root MULTISETS exactly in integer cyclotomic arithmetic at selected q. Actual output includes:

```text
q 2,3,4,7,8,9,14: 0 five-root zero multisets
q 5: 1   first (0,1,2,3,4)
q 6: 6   first (0,0,2,3,4)
q 10: 2  first (0,2,4,6,8)
q 12: 24 first (0,0,4,6,8)
q 15: 3  first (0,3,6,9,12)
q 20: 4  first (0,4,8,12,16)
```

These are SINGLE half-sum checks, not evidence that a complex Hadamard K, a transversal, or a full QLS exists at any surviving q. The all-q theorem is the written proof above; the finite checks only corroborate it.

I also searched the broader NONuniform product family with arbitrary continuous K phases and the published Parker resolution. Code `frontier-20261028-hadamard-product-search-v1.py` SHA **b149bf33abcfa73e384e90590e533e4b3ab4dd6e3eae26e426f6ff5106579cfa**, result JSON SHA **8cff17874562d549d30bb21a24a9244ea53e7ee5ada6abba07810d7dfbd1b634**, best actual numeric array SHA **fe067b55ef8514c79f4cb1d7ac9b7c1dca4641faf1964cd012a63bc6294dfbc4**. Twelve random restarts×4000 steps gave best loss42.4195620265; the independently written original-vector verifier `frontier-20261028-uniform-physical-verify-v1.py` SHA **e2fc32cb61bfda29336cc71ba69a0bbf085daeb752afe67f9bc85d2124c2c6a2** found worst REQUIRED ONB offdiagonal magnitude **0.9999863615468427**. It is emphatically NOT a QLS or a witness. The verifier's uniform-overlap metric is irrelevant to this NONuniform experiment and is not used as a no-go. The finite search is neither exhaustive nor evidence that arbitrary continuous K lacks a solution.

## 5. Remaining scope

The previously proved stronger parity theorem for the further-restricted character-graph choice `K_(t,c)=zeta_n^(c mu(t))`, at n=2p with p an odd prime, rules out a maximal resolvable array for ALL mu and ALL L; see `frontier-20261028-fourier-separable-parity-obstruction-v1.md` SHA **9d6689b74bebb25d622070add14f3d50b7d083bb7848e9c3eca3e079b122e241**. That special-family theorem does not cover arbitrary complex Hadamard K. The new m-term root-length condition applies to this strictly broader product family, but is only a necessary alphabet filter and leaves q=5^e, q with5, q with prime pair{2,3}, arbitrary K and arbitrary non-product QLS open.

No source/held result is presumed correct by chronology; the two-prime length proof is present in the named current written candidate and independently reviewable. All exact checks are at their stated finite scopes. Independent mathematical review, original 100-ray witness/no-go and novelty remain outstanding.

**END — all-L NONuniform Fourier–Hadamard product obstruction under stated root alphabet; original QLS10 target remains open.**
