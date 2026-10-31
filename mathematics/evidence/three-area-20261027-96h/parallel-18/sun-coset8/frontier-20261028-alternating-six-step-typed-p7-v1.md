# Six-step alternating P7 exclusion from typed orbit branches

**Status: WRITTEN candidate, conditional on the named public A_r theorem and the earlier written orbit induction; not independently reviewed or accepted.** For every prime r≥419 which is not a prime-power repunit (q^d−1)/(q−1), d≥2, the actual simple group A_(r+6) has no seven proper subgroup indices whose pairwise gcd is exactly 7. Together with `frontier-20261028-alternating-orbit-induction-v1.md` SHA `bf0e726bb039e63a50da52c1bef884bb5923d2d8505d0525f72be4aa76fbc9f5`, this excludes direct P7 for **all six degrees** A_(r+1),…,A_(r+6) in each such prime block. The earlier packet's elementary prime-count argument gives infinitely many eligible r.

This removes the residue restriction from `frontier-20261028-alternating-six-step-p7-v1.md` SHA `90be5dd44ed0adecd9f9f2ab3bbd0235f309bcc02ad3840c03068c5d7eb02c19`. Its r=431 integer example remains correct as a limitation of the **coarse** divisor buckets, but does not obey the stronger typed binomial alternatives derived below; it was never a subgroup counterexample. No historical priority or novelty claim is made.

## 1. Named dependencies and nonblind provenance

The public classification import is Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2: an eligible prime r has a fixed Sylow-r subgroup of A_r with unique maximal overgroup AGL1(r)∩A_r. The earlier written orbit packet derives the base common-divisor statement in A_(r+1), the binomial divisors d_j below, their bound d_j>7 for r≥419 and j≤6, and the infinitude of eligible primes. These inputs and the exact source proof DAG are unreviewed; no Sun7 is assumed.

The writer had prior Sun exposure and the incidental cross-topic display recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`. No cross-topic excerpt is used in this proof. No clean-cognition, exhaustive-priority, historical-hold rehabilitation, or source-proof replay claim follows.

## 2. Keep the orbit type, not merely its gcd

For j=1,…,6 set
\[d_j=\frac{r+j}{\gcd(r+j,\operatorname{lcm}(1,\ldots,j))}>7.\]
In the earlier proof, an r-free proper subgroup H of A_(r+6) is conjugated to contain an r-cycle R. If H is transitive, pass to the stabilizer of a point fixed by R, retaining **exactly the same subgroup index** and retaining a proper subgroup containing R in A_(r+5). Repeat until either degree r+1 is reached, or the first intransitive subgroup appears at degree r+j, j≥2. In the first case call the index **type 1**, where it is a multiple of r+1=d1. In the second case its orbit containing the r moved points has complement size u∈{1,…,j}; call it **type j**, and retain the stronger fact that its index is a multiple of
\[\binom{r+j}{u},\qquad 1\le u\le j.\]
This full binomial is the index of an actual set stabilizer in A_(r+j); the equalities at all transitive descents preserve divisibility in the original group. It is divisible by d_j. A subgroup can have several valid types if there are choices; for the proof choose any one actual descent chain and one resulting type for each index.

## 3. Seven indices force types 1, 2 and 3

Suppose seven indices have pairwise gcd exactly 7. All are divisible by 7, and at most one is divisible by r>7. If all seven are r-free, their six possible types force two with the same type; both share d_j>7, contradiction. Otherwise precisely six are r-free. Their six chosen types must be **all different**: otherwise the corresponding pair shares d_j>7. Hence each of types 1,…,6 occurs once. In particular, indices N1,N2,N3 occur with the following stronger properties:

- N1 is divisible by r+1 and hence by 2.
- N2 is divisible by binom(r+2,u), u=1 or 2. Since r+2 is odd, **both** alternatives are divisible by r+2.
- N3 is divisible by binom(r+3,u), u=1,2 or 3.

For type 3, binom(r+3,1)=r+3 is even. Also binom(r+3,3) is even: (r+3)(r+1) is a product of consecutive even integers and is divisible by 8, while the denominator 6 removes only one factor 2. In either case both N1 and N3 are divisible by 2 and by 7, so their gcd is at least 14, a contradiction.

The remaining possibility is
\[\binom{r+3}{2}=\frac{r+3}{2}(r+2),\]
which is divisible by r+2. Then both N2 and N3 are divisible by r+2>7, again a contradiction. Therefore no seven-index P7 pattern exists in A_(r+6). This is an all-subgroup statement; it does not rely on the existence or nonexistence of specific coset representatives.

## 4. What happened to the coarse integer obstruction?

For r=431, the earlier residue packet's integers `(3017,3024,3031,1519,1015,763,3059)` do have pairwise gcd 7 and fit the six **coarse d_j** buckets. But its sole type-3-bucket integer 1519=7·217 is not divisible by any of binom(434,1), binom(434,2), binom(434,3). Its possible type cannot be realized by the actual first-intransitivity argument. This does not by itself classify subgroups of A437, but it identifies the missing mathematical information and explains why the old integer construction does not obstruct the present typed proof.

`frontier-20261028-alternating-typed-collision-check.py`, SHA-256 `23c0117eadd1dc9248519a0174b5be910fb294cb47af59f845684ec7cb1ccf6d`, 23 LF / 893 bytes, ran at 18:45:01 PDT on 2026-10-28. It used exact integer binomials and gcds to check type-2/type-3 identities at r=419,421,431 and the r=431 coarse-tuple distinction. These selected controls are not an all-subgroup proof, source verification, or novelty test.

**Review-critical:** rederive the full-binomial type from actual intransitive orbit stabilizers under arbitrary transitive descents; verify that six arbitrary chosen types must cover all six without unproved uniqueness; check the u=1,2,3 collision; reconstruct the source A_r condition and earlier base/prime-density proof. The result remains a conditional written candidate, not an independent or formal acceptance, and no old hold is modified.
