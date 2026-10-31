# f97: independent same-harness review of alternating window families

Native `/bin/date` clock observed immediately before this file was created: **Wed Oct 28 19:11:58 PDT 2026**.
Binding manifest: `manifest-v2.json`, SHA-256 `6ae720c59a57f8f9649293607a87701859511c81d63e152429e5fca10cb4c9b5`. Review is conditional on the explicitly named public group-classification theorem, not an external-family, human, formal, novelty, or prior-hold acceptance.

## Verdicts and findings

| Candidate | FATAL | MAJOR | MINOR | Scope of verdict |
|---|---:|---:|---:|---|
| Seven-step, `frontier-20261028-alternating-seven-step-p7-v1.md` | 0 | 0 | 1 | Conditional mathematical reconstruction found no defect in the stated seven-step conclusion. One minor false inequality is inherited from the frozen orbit import; see M1. The old checker is qualified, not an independent proof. |
| Interval packing, `frontier-20261028-alternating-interval-packing-p7-v1.md` | 0 | 0 | 0 | No defect found in the stated exact-gcd-7 bound under its full size condition and imported A_r theorem. The false inequality in M1 is not needed for this proof. |
| Saturated windows, `frontier-20261028-alternating-saturated-windows-p7-v1.md` | 0 | 0 | 0 | No defect found in the stated t=10,11 exact-gcd-7 exclusion under the stated size condition and imports. M1 is not needed for this proof. |

**M1 — minor, inherited boundary typo, not a counterexample to the asserted bound.** `frontier-20261028-alternating-orbit-induction-v1.md:26`, used for d_1,...,d_6 at `frontier-20261028-alternating-seven-step-p7-v1.md:13`, asserts `r+j>420` for *every* r>=419, 1<=j<=6. At r=419,j=1 the left side is exactly 420, not greater. The desired conclusion d_j>7 nevertheless follows: for j=1, d_1=r+1>=420>7; for j>=2, r+j>=421>420>=7 L_j. Record a targeted additive correction rather than treating the exact displayed inequality as true. This is one inherited minor, counted once above.

**Control qualification, no additional finding:** `frontier-20261028-alternating-seven-step-p7-v1.md:48` accurately describes the *old* multiplication-by-7 control, but it does not establish the minimal common-7 multiple condition. The prospective qualification `frontier-20261028-alternating-five-type-control-qualification-v1.json:8-11` correctly makes that distinction. For example a=7,b=14 yield gcd(7a,7b)=49, but gcd(lcm(7,a),lcm(7,b))=7. The replacement checker at `frontier-20261028-alternating-five-type-exact-check.py:12-17` uses the correct minimal multiples. My own independent enumeration below reproduces the relevant finite implication without running either author checker. The written proof relies instead on genuinely common divisors, or common 2 and 7.

**Process/order:** v1 listed the old checker before its qualification, contrary to the assignment's specified qualification-first order. I notified Main before reading either. Main issued v2, explicitly swapping those entries without changing input hashes. The first three bodies had been read under v1 before v2 existed; their hashes were unchanged and verified under v2. Thereafter I read the complete qualification before the complete old checker and completed all remaining v2 inputs in order. No old checker body was read before the qualification. Both manifests are retained. This resolution is not a scientific finding or a claim that a past ordering violation was cured.

## Input identity and complete read

All ten v2 inputs were read completely in raw line windows in the manifest order. Each live SHA-256, byte count and LF count matched the v2 manifest. The table names files under `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/`.

| Order | File | SHA-256 | bytes / LF |
|---:|---|---|---:|
| 1 | `frontier-20261028-alternating-orbit-induction-v1.md` | `bf0e726bb039e63a50da52c1bef884bb5923d2d8505d0525f72be4aa76fbc9f5` | 6917 / 53 |
| 2 | `frontier-20261028-alternating-six-step-typed-p7-v1.md` | `b58cde595c44155c158d0d2226b721ace070322233774611d79b7c4772c57aa4` | 6005 / 41 |
| 3 | `frontier-20261028-alternating-seven-step-p7-v1.md` | `58e64b1565069c041cb51b8e1040eddf7ddc055da027aef4124e348290029806` | 6685 / 50 |
| 4 | `frontier-20261028-alternating-five-type-control-qualification-v1.json` | `ddd774df8e98732a35cbb1b424fadfbf4fa28a7f60b3ad670bbd76d08212b9bf` | 1576 / 14 |
| 5 | `frontier-20261028-alternating-five-type-check.py` | `2508dfd5a74034e682a29c0f848c8b54cfb0ca83e27fc7a1130944929e490be0` | 801 / 20 |
| 6 | `frontier-20261028-alternating-five-type-exact-check.py` | `a18291356aab51a2c28541736f16ba4d847bc2c3490a7e26d07db3fba9de4801` | 790 / 19 |
| 7 | `frontier-20261028-alternating-interval-packing-p7-v1.md` | `cc6aa191d75c2658a6f93e92468d6ac9aab178c1cfc54effa3c0e50e1cc11e4f` | 5997 / 39 |
| 8 | `frontier-20261028-alternating-interval-check.py` | `d2f9790348db6ac5eff588c7663f798275e9d6b4b5abd26f9bcb985b4528e6d3` | 1729 / 65 |
| 9 | `frontier-20261028-alternating-saturated-windows-p7-v1.md` | `15bc2773dac68277ccfebb228dfba5e090fec11e7908353391a71ac10d707403` | 5048 / 34 |
| 10 | `frontier-20261028-alternating-saturation-check.py` | `a8aae12d6bff39aaca24bc8080afe81b82473d681b0a722ab02680fc6f729366` | 1698 / 59 |

The predecessor manifest v1 SHA matched v2's recorded `dbf7c653a9b93023f1ad998744cf876bd564190007e28d8be0f69990d0e307c3`; the binding v2 SHA also matched the value communicated by Main. Hashes establish byte identity, not mathematical validity.

## Independent reconstruction

### Source, base and typed descent

I directly fetched the public primary source [Baumeister–Burness–Guralnick–Tong-Viet, Theorem 2(i)(d)](https://arxiv.org/html/2307.13976v2#Thmtheorem2). It states that for G=T=A_r, r odd, r not 11 or 23, and r=5 or r not a prime-power repunit `(q^d-1)/(q-1)`, the fixed Sylow-r subgroup has unique maximal overgroup `AGL_1(r) ∩ G`. Thus its statement covers every eligible r>=419 here. I did **not** reconstruct or formally verify the theorem's classification proof or dependencies; that is the principal unverified import. Standard Sylow, Lagrange, orbit-stabilizer, and alternating-group facts are also used.

For the base (`orbit-induction-v1.md:15-17`), an r-free index permits conjugating H to contain an r-cycle R. If H is intransitive in A_(r+1), its R-orbit of size r forces H to fix the remaining point, so r+1 divides its index. If H is transitive, the fixed-point stabilizer H_x is proper in A_r and contains R. By the imported theorem, its order divides r(r-1)/2. Hence |H| divides (r+1)r(r-1)/2, which divides r!/2: r+1 divides (r-2)! because both 2 and (r+1)/2 are distinct factors in that factorial for the present r. Thus |H| divides |A_r| and `[A_(r+1):H]=(r+1)|A_r|/|H|` is divisible by r+1. I independently reconstructed this argument from the pinned orbit body; the separately named `frontier-20261028-alternating-successor-degree-v1.md` was **not opened** or independently hash-checked.

For t<r, R remains a Sylow r-cycle in A_(r+t). At a transitive descent through an R-fixed point, the subgroup stays proper, contains R, and the index is exactly unchanged. At the first intransitive stage A_(r+j), the orbit containing the r moved points has complement size u in 1,...,j. Its set stabilizer has index binom(r+j,u): the symmetric set stabilizer has odd permutations, so intersecting with A_(r+j) does not change the index. Thus a selected r-free index is divisible by the full binomial, or by r+1 if the base is reached. With L_j=lcm(1,...,j), the identity `u*binom(n,u)=n*binom(n-1,u-1)` gives d_j=(r+j)/gcd(r+j,L_j) dividing every relevant binomial. These claims reconstruct `orbit-induction-v1.md:21-37` and `six-step-typed-p7-v1.md:15-19`, subject to M1.

### Seven-step collisions

At `seven-step-p7-v1.md:19-28` write n_j=r+j. Type 1 is even, type 2 carries n_2, and type 3 either is even and carries d_3 (u=1 or 3), or carries both n_2 and d_3 (u=2). For u=3, 3 does not divide n_3 because r>3 is prime, and n_3 divides the binomial. Hence types 1,2,3 cannot all occur. Type 4 has n_4 at u=1,2; d_3 at u=2,3; and a divisor greater than 7 of n_2 at u=3,4. Type 5 with odd u is even; u=2 carries n_4; u=4 carries n_2/gcd(n_2,24)>7. These are integer divisibility statements, including the factorial cancellation.

For the three remaining four-subsets at `seven-step-p7-v1.md:34-38`: (1245) type 2 forces type 4 to carry n_4 and type 5 then collides in every alternative; (1345) type 1 forces type 3 to u=2, after which its n_2 replaces type 2 in the same argument; (2345) type 2 forces type 3 to u=1 or 3, which is even and carries d_3, forcing type 4 to u=1 and then excluding every type-5 alternative. In a seven-index exact-gcd-7 pattern, at most one index is divisible by r; six chosen r-free types are distinct since each common d_j>7. Six distinct types among 1,...,7 include at least four from 1,...,5, giving the contradiction (`seven-step-p7-v1.md:42-44`). For the seventh step the condition is exactly d_7=(r+7)/gcd(r+7,420)>7; r>=2934 implies it. This argument is **not** a proof that all eight-index Sun8 configurations are excluded.

### Overlap, packing and saturation

For `interval-packing-p7-v1.md:17-25`, the size assumption gives t<r. If two selected numerator windows share h, put a=r+h and g=gcd(a,t!). From a|u! binom(r+j,u) and u!|t!, we get `(a/g) | (t!/g) binom(r+j,u)`; gcd(a/g,t!/g)=1, so a/g divides each relevant binomial. It also divides the base r+1 for window {1}. Since a/g >= (r+1)/t! > 7, the two index gcds cannot equal 7. No unproved cancellation or assumed coprimality of the indices is needed.

At `interval-packing-p7-v1.md:29-33`, exact pairwise gcd 7 makes every index divisible by 7 and permits at most one even index. An odd endpoint j with odd u has even binomial, since `(r+j)/gcd(r+j,u)` is even and divides it. Each other odd endpoint injects into the even predecessor j-1; each even endpoint injects into itself. Disjointness makes all those representatives distinct. Consequently e+o<=floor(t/2)+1 r-free indices, and one possible r-divisible index gives floor(t/2)+2 in total. This independently checks the inclusive t<=9 direct-P7 and conditional eight-index conclusions.

For `saturated-windows-p7-v1.md:13-28`, seven indices at t=10 or 11 force exactly six r-free indices and one r-divisible index. The above injection then saturates all five even positions 2,4,6,8,10 and uses exactly one odd-endpoint even-binomial exception. Each represented even position belongs to a different index. If the representative is an even endpoint, any length >=3 would also occupy the already represented k-2, impossible; thus its length is 1 or 2 and it carries r+k. If the representative is the predecessor of a nonexceptional odd endpoint, its even length must be 2, because a length >=4 would also occupy k-2; that binomial likewise carries r+k. For k=2 the longer alternatives are unavailable. Among the five distinct resulting indices, r+2 and r+8 are multiples of 3 when r=1 mod 3, while r+4 and r+10 are multiples of 3 when r=2 mod 3. The corresponding indices also have factor 7, contradicting exact gcd 7 via the factor 21. This checks the saturation equality case without assuming that the exceptional window or its index has any additional special property.

### Eligibility and density

`orbit-induction-v1.md:43-47`: for excluded odd prime r<=x with d=2, q=r-1 is an even prime power, hence 2^a, giving O(log x) choices. For d>=3, q<=sqrt(x) and d<=log_2(x+1), so counting all integer q (not just prime powers) gives O(sqrt(x) log x). The central-binomial argument gives pi(x) bounded below by a constant times x/log x. Their ratio tends to zero. The finitely many exceptions and the fixed-t size threshold preserve relative density one of eligible primes; this does not give density one among all integers or any claim for t growing with r.

## Independent exact controls

I wrote and ran `independent-check-v1.py` (SHA-256 `c353d588cdfb2c23d652a5e62091700bdc2da577d6166d05ea139477f400c247`); its exclusive-create `independent-check-receipt-v1.json` has SHA-256 `345a33b935c2be292ec8cd22ff2495d56d6a80d826b72b5a991b3a99c19de003`, records exit 0, and includes every reported result. It uses Python integer arithmetic, independently enumerates prime-power repunit bases, and enumerates disjoint windows left-to-right rather than executing an author replay. Negative eligibility controls include 65537=2^16+1 and 8191=1+2+...+2^12. As an important positive check, 421=1+20+20^2 is still eligible because 20 is not a prime power.

| r | prime, eligible | d_1,...,d_7 | exact four-type choices / survivors |
|---:|---|---|---:|
| 419 | yes | 420,421,211,141,106,85,71 | 274 / 0 |
| 421 | yes | 422,423,212,425,71,427,107 | 274 / 0 |
| 431 | yes | 432,433,217,145,109,437,73 | 274 / 0 |
| 1,000,000,007 | yes | 1000000008,1000000009,500000005,333333337,250000003,1000000013,166666669 | 274 / 0 |

Here the pairwise collision test uses lcm(7,binomial), not 7*binomial; subset counts for 1234,1235,1245,1345,2345 are 24,30,40,60,120 respectively. Every tested d_j also divides every binomial of its type for j<=11.

For all four r, enumerating disjoint typed windows yielded maximum 6 under the at-most-one-even condition at both t=10 and t=11, but maximum 5 once at-most-one-3-divisible is also imposed; the maximum using pairwise exact gcd 7 of the minimal multiples was also 5. At t=10 the numbers of six-window parity-only selections are respectively 33,57,33,33; at t=11 they are 75 each. For every such six-window selection the checker verifies that the five represented even positions are distinct and their binomials contain the full factors r+2,...,r+10. The same program independently reproduced the author's eligible examples: r=2,540,173 at t=9 gives maximum 5 under the parity bound, and r=279,417,613 at t=10,11 gives maximum 5 under the parity-plus-3 bound.

**Crucial scope of the controls:** r=419,421,431 do satisfy the seven-step d7 criterion but **do not** satisfy r+1>7t! at t=7,9,10,11. Their disjoint-window enumeration therefore checks the abstract integer packing conditional on disjointness; it cannot establish that actual subgroup windows are disjoint at these r, nor apply the interval/saturation theorems to them. For t=10,11, 7t! is 25,401,600 and 279,417,600. The large eligible r=1,000,000,007 satisfies both thresholds (and t=7,9); its smallest overlap divisor in the checked t=10 and t=11 cases is 1,984,127>7. Finite controls do not enumerate actual subgroups or prove any universal claim.

## Precise limits and named unverified material

The seven-step and saturation statements exclude configurations of **seven** indices with every pairwise gcd exactly 7, conditional on the named source; interval packing proves the explicitly quantified size bound for such collections and, for t<=11, excludes eight only when all pairwise gcds are exactly 7. That is not unrestricted Sun8, and no Sun7/R8 bridge is imported. The orbit input's separate t<=6 result for pairwise gcd at most 7 has its own stated scope and does not extend to t=7,10,11 merely from these proofs.

Unverified imports: the cited public Theorem 2(i)(d)'s proof/classification chain; the independently unopened `frontier-20261028-alternating-successor-degree-v1.md`; the older `frontier-20261028-alternating-six-step-p7-v1.md` and incidental-cross-topic provenance record mentioned by the inputs, neither used as a proof premise; and standard group-theoretic background not formally checked. The public theorem's *statement* was checked directly, not its proof. No author contact, external model, held/withdrawn/quarantined body, historical-hold change, publication, or global/novelty conclusion is part of this review.
