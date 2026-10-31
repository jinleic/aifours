# Excluding factorial terminals through 33 alternating positions

**Status: WRITTEN structural candidate, conditional on the named public A_r classification and prior actual projection lemma; not independently reviewed or accepted.** Let r≥419 be a prime which is not a prime-power repunit (q^d−1)/(q−1), d≥2, and let 1≤t≤33. If seven proper subgroup indices in A_(r+t) all have pairwise gcd exactly 7, **none** of them is divisible by (r−2)!. Consequently no r-free projection chain ending at a proper subgroup of A_r can occur in such a pattern. This is an actual-subgroup branch exclusion, not an assertion that all P7 patterns are excluded for t≥16, nor a claim of priority or novelty.

The previous twelve- through fifteen-step proofs used the stronger special fact that at most five large primes are available. That count fails at t=16: the possible-prime support can have six members. The replacement below permits up to ten possible primes and uses the actual impossibility of certain indices 7p.

## 1. Source and elementary group facts

The only non-elementary source input is Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2: a Sylow r-subgroup of A_r has unique maximal overgroup M0=AGL1(r)∩A_r, of index (r−2)!. The actual alternating-block projection/divisibility and transitive point-stabilizer descent are written in `frontier-20261028-alternating-twelve-step-projection-p7-v1.md`, SHA `79c5c3ce09f854b0e46536fd7e7497b756b7efd80e7e780e4495ebc38754b33a`. These source and written inputs remain unreviewed. We also use standard Sylow, Lagrange and A_n simplicity/order facts. No Sun7 is assumed.

The writer had nonblind Sun exposure. The incidental cross-topic display is recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`; no such excerpt is an input and no historical hold is changed.

## 2. No actual r-free subgroup index 7p

Let p be prime with r<p≤r+t. There is no proper subgroup H<A_(r+t) of index 7p. Its index is r-free, so conjugate H to contain a fixed r-cycle R. Descend through fixed-point stabilizers while the subgroup is transitive; the subgroup remains proper, contains R and retains index 7p.

If this reaches A_r, the source theorem forces (r−2)!|7p, impossible because (r−2)!≥(r−2)(r−3)>7(r+33)≥7p. Otherwise at the first intransitive stage A_(r+j), the orbit containing the r moved points has complement size u∈{1,…,j}, j≤t, so B=C(r+j,u) divides 7p. If u≥2, then u≤33<(r+j)/2 and
\[B\ge\binom{r+1}{2}>7(r+33)\ge7p,\]
a contradiction. Thus u=1 and B=r+j. Since r+j>7 but r+j≤r+t<7p, the only divisor possibility is B=p. The subgroup then fixes one point and has index
\[[A_{p-1}:H]=[A_p:H]/p=7,\]
impossible: every proper subgroup of A_(p−1) has index at least p−1>7 by simplicity and the faithful coset-action order comparison. This uses actual subgroups, not a divisor-list relaxation.

## 3. At most ten large primes

The only possible primes of |A_(r+t)| in [r−1,r+t] are r and prime members of r+2,r+4,…,r+2E, where E=floor(t/2)≤16; r−1 and r+odd are even and greater than 2.

Among the E odd candidates at least floor(E/3) are composite multiples of 3. For E≤13 this gives at most 1+E−floor(E/3)≤10 primes including r. For E=14,15,16, each residue r mod 5 supplies at least three 5-divisible offsets already within 2,…,28:

- r≡1: 4,14,24;
- r≡2: 8,18,28;
- r≡3: 2,12,22;
- r≡4: 6,16,26.

Each triple is spaced by 10 and has three distinct residues mod 3, so at least two of its composite multiples of 5 are additional to the 3-divisible candidates. Hence for E=14,15,16 the possible-prime count is at most 1+E−floor(E/3)−2≤10 as well. All such multiples exceed 5.

## 4. Factorial-terminal contradiction

Suppose F=(r−2)! divides one P7 index N0. It contains 7² and every prime at most r−2. For each of the other six indices Ni, gcd(N0,Ni)=7 forces Ni=7ai where ai>1, the ai are pairwise coprime, and every prime divisor of ai lies in [r,r+t]. All such primes exceed (r+t)/2, so each occurs to exponent at most 1 in |A_(r+t)|; in particular each ai is squarefree.

The six nonempty pairwise-disjoint prime supports use at most ten primes by Section 3. At least two supports must therefore be singletons: otherwise one singleton and five supports of size at least two would already require eleven primes. At most one singleton can be the prime r. Hence some Ni=7p with p prime in (r,r+t], contradicting the actual-subgroup lemma in Section 2. This proves the asserted factorial-terminal exclusion for all 1≤t≤33.

## 5. Actual finite control and remaining gap

`frontier-20261028-alternating-factorial-bound-check.py`, SHA-256 `b5999825444b9d9c4a763c630661fd99eeb491bf2f901b598e588dab8b7d07c4`, 19 LF / 724 bytes, ran at 19:22:38 PDT on 2026-10-28. Exact integer arithmetic checked the 3/5 residue upper bound for all eight residues coprime to 15 and all t=1,…,33, and the two inequalities at r=419,t=33. This is a finite arithmetic control only, not a group enumeration, proof of the public classification, or independent review.

**Review-critical:** reconstruct the no-7p argument including the first-intransitive-stage divisibility and all-transitive A_r case; verify squarefreeness of the large-prime cofactors, the ≤10 prime count, and that two singleton supports force one p>r. The lemma does not eliminate nonfactorial projection chains, prove P7 beyond other explicitly named packets, or modify any historical hold.
