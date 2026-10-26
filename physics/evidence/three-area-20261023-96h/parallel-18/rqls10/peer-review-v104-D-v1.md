# v104-D — ENTIRE original Sun8 group-family review: PSL2(q) for every q and alternating/symmetric PP/PW

Reviewer: PhysicsRQLS10-2. Actual returned `/bin/date` before this NEW file: **Sun Oct 25 19:31:03 PDT 2026**. This is an observation bound, not an invented creation/completion clock.

## 1. Separate verdicts

### Family I — PSL2(q), EVERY prime power q>=2

**WHOLE MATHEMATICS: 0 FATAL / 0 MAJOR / 0 MINOR found.** I reconstructed the order/root/projective-line setup, upper/lower generation, perfectness/simplicity for q>3, ROOT containment, all small p-drop normalizer/subfield/Sylow-count/divisibility constraints, every large-field case and EVERY finite base q=2,3,4,5,7,8,9,16,25,32,49, including all omitted k and nonintegral t cases.

**DEPENDENCY / APPLICATION: 0 FATAL / 0 MAJOR / 0 MINOR found**, at named ordinary finite-group facts plus NC7. NC7 is used ONLY at q=7. Its supplied complete proof (II.1–II.4) was reconstructed at the named classical A7 simplicity and the elementary Eisenstein irreducibility of Phi7. No Jordan, Bertrand, minimal-index table, Dickson, CFSG, exceptional isomorphism, global Sun7/F7/MS or old verdict is consumed.

Exact supported statement:

```text
For every finite field F_q, q=p^f>=2, and G=PSL2(q):
any EIGHT pairwise-disjoint LEFT cosets of arbitrary subgroups of G
contain two cosets whose ACTUAL subgroup indices have gcd>=8.
```

It implies P7-freeness in this family only as a weaker special case.

### Family II — A_n/S_n prime powers and prime windows

**WHOLE MATHEMATICS: 0 FATAL / 0 MAJOR / 0 MINOR found** for PP, PW, the n=2p corollary and the stated n>=16 reduction.

**DEPENDENCY / APPLICATION: 0 FATAL / 0 MAJOR / 1 MINOR.** The supplied22LF classical-input record says BERTRAND is used only at u=p prime>7. The93LF v2 actually uses BERTRAND at u=floor(n/2) for EVERY n>=16, including PP with a>=2 and the general reduction. The same record does name the general theorem, and its strict upper inequality holds because 2u is composite. Thus this is a stale input-scope statement, not a mathematical gap. Future consumers must use the general named BERTRAND input for v2, not the old n=2p-only boundary.

Exact supported statements at JORDAN-PRIME and BERTRAND:

- **PP:** Sun8 holds for A_(p^a) and S_(p^a), p prime>7, a>=1. Prime n uses Jordan but not Bertrand; a>=2 also uses Bertrand.
- **PW:** if an odd prime p>7 divides n, n>=2p, and ONE prime q has n-p<q<=n, Sun8 holds for A_n and S_n. All n=2p, p prime>7, follow by Bertrand.
- **General reduction:** for EVERY n>=16 a counterexample would need at least SIX intransitive sources in A_n, or FIVE in S_n. This is a reduction only.

No full arbitrary-group Sun8, all A_n/S_n degrees, PGL2/field-automorphism extensions, other finite simple families, infinite groups or a counterexample is established.

## 2. Actual two-stage chronology and complete coverage

I checkpointed my whole RQLS primary BEFORE the opaque stage, read v9 FIRST, v10 immediately SECOND, v11 THIRD and HOLD, read only the opaque envelope fields with `post_release` excluded, and wrote/sent the actual ACK.

- Pre-ACK primary checkpoint: `checkpoint-primary-before-v104-D-opaque-v1.json`, SHA256 `7e03a64ba6e17ae25f6d3280380c47d96894454e57e280f8a213265374ec0cf4`, actual18:08:29.
- Opaque ACK: `peer-review-v104-D-opaque-ack-v1.json`, SHA256 `83bac62ccad3394f52df22c0e37f27ced6fba3bfc8dece7264ebf2dccb33dc90`, actual18:10:31; pin18:11:34.

I then waited while blocked, with no new manifest/scope/pins/receipt/part/body or primary work. A later v106-F opaque dispatch arrived while v104-D was unreleased. I did not open any v106 file, reported the serial authorization blocker, and v106-F remains queued. Main later reported that no earlier v104 release existed at its actual19:14:42 and released the ORIGINAL v104-D. I read that persisted release before the body.

- Release: RUN `peer-review-v104-D-explicit-body-release-v1.json`, SHA256 `dd3c8e85753d6c2361fa3efcf29574d786cff4e61a612e09f86acf6f4b5cd4f8`.
- Delayed-release intake: `peer-review-v104-D-delayed-release-intake-v1.json`, actual19:16:28. It records the wait as blocked, not as continuous active mathematics.
- Manifest: `peer-review-wave-eighteen-v104.json`, SHA256 `7eb601c586eea05377fd6b92455f72f640114f72edad99500eb22ea78d764b0c`; complete common contract and complete own entry/post_ack_entire_scope/source map read after release.
- Receipt: `peer-review-wave-eighteen-v104-packet-receipt-v1.json`, SHA256 `9bba2ab1cee99746653bbfeb34111ef67c04212b85a7178cb95494026727d1db`; common fields and BOTH own byte checks read. Its supplied equality assertions are not scientific replay.

ALL957 packetLF/endings were actually read:

|part|LF|SHA256|raw windows|
|---|---:|---|---|
|part1|728|`b245f0b3fe0e729b88e5b5314cebc252dfd2347510f36fa648f329e9880ae4c6`|1–240,239–500,499–728|
|part2|229|`555110789fa1745d5693f19cf96a9e77989d7a20d1c2f1710b45290e41079314`|1–229|

This covers all15 complete sources: v9/v10/v11; 184LF PSL2; 93LF orbit strata; complete181LF NC7 Part2; 22LF classical inputs; 49LF packet; the three current parents; checkpoint057; later findings v7/v6; and the v101 missing-scope finding. Principal mathematical/parent hashes were freshly observed equal to the pins. The intermediate own checkpoint is `checkpoint-v104-D-whole-reconstruction-v1.json`, observation19:22:16.

Prior exposure is not blind. My earlier actual v72 Sun8 rank4 review, the other completed reviews listed in the ACK and the release brief are disclosed. S14 includes my OWN two earlier RQLS process findings; they do not affect this mathematics. During this live review Main sent a notification-only message about returned reviews of my RQLS v6; I opened no new parent/source and transferred no information into this review.

## 3. Family I: actual setup, generation and simplicity

In SL2(F_q), choose any nonzero first column (q²-1 ways). For each, the determinant equation is one nonzero linear equation in the second column, with q solutions. Thus |SL2(q)|=q(q²-1), and with d=gcd(2,q-1),

```text
|G|=q(q²-1)/d.
```

On Omega=F_q union{infinity}, U={u(t)} acts by translations and fixes only infinity at every nonidentity element. It has order q, the full p-part. B=G_infinity consists of x->s x+b with s square, order q(q-1)/d. U is normal in B and is its unique Sylow p-subgroup. The lower group l(t) fixes only0.

Exact matrix products:

```text
w(a)=u(a)l(-1/a)u(a)=[[0,a],[-1/a,0]],
w(a)w(-1)=diag(a,1/a),
l(-c/a)[[a,b],[c,e]]=[[a,b],[0,1/a]]=diag(a,1/a)u(b/a), a!=0.
```

If a=0, w(1) makes the first entry nonzero. Hence upper/lower root groups generate G. The action is faithful, transitive and two-transitive, so primitive.

For q>3 choose a²!=1. Then [diag(a,1/a),u(t/(a²-1))]=u(t), so U<=G'. Its conjugates generate G, hence G is perfect. A nontrivial proper normal K would be transitive by primitivity, G=KB, and all conjugate root groups would have the same abelian image in G/K. Perfectness makes G/K trivial. Thus G is simple for q>3. No exceptional isomorphism is imported.

## 4. ROOT and characteristic p>7

If H is proper and p does not divide [G:H], H contains a full Sylow p-subgroup. Conjugate to assume U<=H for this subgroup property. If g in H moves infinity to z, h=u(-z)g lies in H and fixes0. Then hUh^-1 is a Sylow subgroup of the stabilizer of0, so equals the lower group. H would contain both root groups and equal G. Thus

```text
p-free proper index => H lies in some Borel => (q+1) | [G:H].
```

If p>7, at most one original index is divisible by p. The other at least seven are proper p-free and divisible by q+1>7, so two have gcd>7. Every field of characteristic>7 is closed.

## 5. Family I: actual small p-drop constraints

Let H be non-Borel. By ROOT, a=v_p([G:H])>=1. Suppose a<f and let P be Sylow in H, u=|P|=p^(f-a)>1. Conjugate P into U; then P=H intersect U=u(A), where A is an additive subspace of dimension f-a.

P fixes exactly infinity, so N_H(P) fixes infinity and lies in B. Conversely H intersect B normalizes H intersect U. Hence N_H(P)=H intersect B, of order ut, t the actual multiplier image.

Let K(A)={0} union{s!=0:sA=A}. It is closed under products/inverses. If s+r!=0, (s+r)A is contained in A and equal by injectivity. Thus K(A) is a subfield containing F_p, of size p^e. Then e|f and A is a K(A)-space, so e|(f-a). Therefore

```text
t | p^e-1, e | gcd(f,a), t | (q-1)/d.
```

Every nontrivial p-subgroup lies in one root group and has exactly that fixed point. Hence a Sylow subgroup of H with fixed point x equals H intersect U_x; distinct Sylows have distinct fixed points. Sylow conjugacy identifies their number with |H.infinity|. P is semiregular on finite points and H moves infinity, so with s=p^a,

```text
nu_p(H)=1+ku, 1<=k<=s,
[G:H]=s(q²-1)/(d t(1+ku)).
```

Since 1+ku is prime to p, integrality gives (1+ku)|(q²-1). From q=su and ku≡-1 modulo1+ku, multiplication by k² gives

```text
(1+ku) | (s²-k²).
```

If u>=s² and k<s, then0<s²-k²<1+ku. Therefore k=s, nu_p=q+1 and

```text
[G:H]=s(q-1)/(d t).
```

These are NECESSARY constraints; no tuple is assumed realized.

## 6. ALL large fields and buckets

Let b be largest with p^b<=7. At most one source has p^(b+1) dividing its index. Every source is Borel-contained, in that high bucket, or non-Borel regular with1<=a<=b.

For p=3,5,7,f>=3, b=1, a=1 and u>=p². The full formula gives p(q-1)/(2t), with t|p-1. Since2t divides both q-1 and2(p-1), every regular index is a multiple of

```text
pD, D=(q-1)/gcd(q-1,2(p-1)),
pD>=p(p²+p+1)/2>=39/2.
```

For p=2,f>=6, b=2. Both a=1,a=2 satisfy u>=s². Then t=1 for a=1 and t in{1,3} for a=2. Every regular index is a multiple of D=(q-1)/gcd(q-1,3)>=21.

In both cases the regular, Borel and high buckets each hold at most one source. At most three sources occur.

## 7. Every listed finite field, independently recomputed

The Borel bucket has capacity one because q+1>7. The high bucket has capacity one. I checked all orders: 504,4080,32736,7800,58800,360,168,60,60,12,6.

|q|row|DIV/k checks|t|necessary indices|
|---|---|---|---|---|
|8|a1,u4|FULL k=2; k1 needs5|3|1|14|
|8|a2,u2|k1:3|15; k2:5|12 false; k3:7|7; k4:9|0|1|84,36,28|
|16|a1,u8|FULL k=2|1|30|
|16|a2,u4|k1:5|15; k2:9|12 false; k3:13|7 false; k4:17|0|1,3|204,68;60,20|
|32|a1,u16|FULL k=2|1|62|
|32|a2,u8|k1:9|15,k2:17|12,k3:25|7 false; k4:33|0|1|124|
|25|a1,u5|6|24;11|21 false;16|16;21|9 false;26|0|1,2,4|260,130,65; k3 gives195/(2t), never integral; 60,30,15|
|49|a1,u7|8|48;15|45;22|40,29|33,36|24,43|13 false;50|0|1,2,3,6|1050,525,350,175;560,280;168,84,56,28|

The q16 t=3 values arise only at f4,a2, where e=2 is allowed. At q49,k2 the values560/3 and560/6 are not integers. Within each q25/q49 row the shared divisors are65,15,175,280,28, so each row has capacity one.

Thus q8,q16,q32 allow at most six, seven and four sources. q25 allows at most four, and q49 at most five. Eight is impossible.

### 7.1 q=9

Here |G|=360,a=1,u=s=3,d=2,t in{1,2}. DIV leaves k=1 and3 (k2 needs7|5). The necessary regular indices are30,15,12,6. Borel indices share10, high indices share9. The non6 values12,15,30 can occur at most twice because15 and30 are incompatible.

Any index6 coset action is faithful by simplicity and lies in A6 by perfectness. Order360 identifies G with A6 in that actual action.

No subgroup of order30 exists. If its Sylow5 is normal, it lies in N_A6(C5). In S6 this normalizer has order20, including an odd4-cycle multiplier, so the alternating normalizer has order10. Otherwise its six Sylow5 groups give24 elements. Ten Sylow3 groups would add20 more, impossible. Hence the Sylow3 is normal. A single3-cycle has S6 normalizer S3×S3, order36 with odd elements. A double3-cycle has centralizer order18 and normalizer36, again with odd elements. Both A6 normalizers have order18. Neither contains order30.

Thus index12 is absent and at least five original cosets have index6. Six would fill G, so exactly five occur.

Fix one index6 action. Another order60 subgroup K cannot be transitive: that would give KH=G and every pair of cosets would meet. Without a fixed point its possible orbit partitions give orders at most24,18 or4. Hence K is a point stabilizer in the SAME action. Disjoint point constraints form one rook row/column, and their complement is the missing sixth index6 coset. The three remaining sources must occupy the Borel, high and remaining regular buckets once each. Containment in the index6 coset gives both 6-divisibility. The regular index is30, and the Borel index is a multiple of30. Their gcd is at least30, contradiction.

### 7.2 q=4,5,2,3

For q=4,5, G is simple of order60. Indices2,3,4 would embed it in S4. The only proper indices are5,6,10,12,15,20,30,60. Coprime indices give HK=G, so their left cosets meet.

If index5 occurs, indices6 and12 are excluded. The high compatible pairs are only10/15 and15/20, while at most five index5 cosets fit. That gives at most seven.

If index6 occurs and5 does not, the compatibility graph on10,12,15,20,30,60 has edges10-12,10-15,12-15,12-20,12-30,15-20. Its only triangles are{10,12,15} and{12,15,20}. Eight sources would need five index6 cosets and one triangle. The triangle masses are1/4 and1/5, larger than the remaining1/6. Without5 or6 there are at most three distinct high sources. Disjoint cosets require mass at most1, not an assumed partition.

For q=2, |G|=6 is too small. For q=3, |G|=12; at most one index12 coset occurs and seven others of index at most6 have mass at least7/6.

### 7.3 q=7, the sole NC7 use

|G|=168. Seven-free indices are multiples of8, so at most one occurs. At least seven indices are7r with r|24 and pairwise coprime r. At most two r exceed1, so at least five have index7. An index7 coset meets every coset of seven-free index, hence no seven-free source exists. At least six have index exactly7. NC7 makes their complement one coset of an index7 subgroup L. The remaining two original cosets lie in it, their subgroups lie in L, and their relative indices are coprime. They meet, contradiction.

The cases cover p>7, p=3/5/7 with f=1,2 and f>=3, and p=2 with f=1–5 and f>=6. That exhausts every prime power.

## 8. NC7 II.1–II.4, completely reconstructed for this use

Two disjoint cosets of index7 subgroups have primitive prime-degree actions. A nontrivial image of one core in the other action would be transitive and force all corresponding cosets to meet. Hence all six subgroups share one core C. G/C is a finite faithful transitive degree7 group; completion lifts back. This works even for infinite G.

If the degree7 group F is not two-transitive, a proper orbital is a translation-invariant digraph with connection set S. Its eigenvalues are lambda_t=sum zeta^(ts). Phi7(x+1) is Eisenstein, so equal nonzero eigenvalues occur exactly when tS=uS; lambda0 is distinct.

- |L|=1 gives seven simple eigenspaces and only translations.
- |L|=2 gives the seven-cycle or complement, with D14.
- |L|=3 gives the two Paley tournaments, with automorphism group of order21.

Thus F is C7:C_d, d=1,2,3.

For two-transitive F, an actual3-cycle generates A7 by connected3-cycle induction. Otherwise its 3-part is3 and its order is one of42,84,168,336,210,420,840,1680. The odd-index-two kernel excludes210/420; A7 simplicity excludes420/840/1680; Sylow7 counts reduce84/42 to AGL(1,7). Order168 is simple by its seven-divisible normal subgroups and the56 case. Its triple-orbit analysis, double-three-cycle normalizer order6, A4 triple stabilizer and V4 normalizer contradiction force a7-triple Fano orbit, so F=GL3(2). Order336 has a normal GL3(2) whose unique Fano orbit forces F into GL3(2).

All index7 subgroups are affine point stabilizers, A7/S7 point stabilizers, or GL3(2) point/line stabilizers; an order24 subgroup cannot have orbits3+2+2 because Sylow2 of GL3(2) is nonabelian, and a basis triple has stabilizer6. Affine completion uses the zero sum of F7. Two-transitive families form rooks. In mixed GL3(2) families, cross disjointness flips incidence; 1+5 splits fail by3/4 counts; same-side cliques fail by incidence rectangles; the remaining four tables add the unique completing coset. Global inversion handles the reverse orientation.

II.5–II.9 of the same181LF file were read but are NOT consumed by the PSL2 proof.

## 9. Family II: prime-power and prime-window reconstruction

### PRIM

Let H be primitive and not contain A_n, n>=8. If3 is coprime to [G:H], H contains a Sylow3 subgroup. Every Sylow3 subgroup contains a single3-cycle by Sylow conjugacy. It fixes n-3>=5 points, so JORDAN-PRIME forces A_n<=H. The same holds for5. Thus15 divides every nonexceptional primitive index.

### IMPRIM

For n>=16 choose ONE prime q with floor(n/2)<q<2floor(n/2). Then q>n/2, q>7, q is odd and q divides |A_n|. A transitive imprimitive H has blocks a×b with a,b>=2, so |H| divides (b!)^a a!. Since a,b<=n/2<q, q divides its index.

### INTRANS for n=p^a

An intransitive H fixes a set of size k. Its set stabilizer has index binomial(n,k) in S_n and also in A_n, because S_k×S_(n-k) contains an odd transposition. Frobenius gives (1+x)^(p^a)=1+x^(p^a) over F_p, so every interior binomial is divisible by p.

### PP

For a=1, n=p>=11: no transitive imprimitive subgroup exists. Intransitive indices share p, nonexceptional primitive indices share15, and S_n can have at most one A_n coset. At most three sources occur.

For a>=2, n>=121: intransitive, imprimitive and nonexceptional primitive types share p,q,15 respectively. With the possible A_n coset, at most four sources occur.

### PW

Let p>7 divide n, n>=2p, and n-p<q<=n. Then q>n/2. A p-free H contains a full Sylow p subgroup P. If P fixed at least p points, an even p-cycle on them would enlarge P. Since p divides n, P is fixed-point-free. Intransitive orbits are multiples of p and each is at most n-p<q. Imprimitive blocks are below q. A primitive H contains a single p-cycle fixing at least p>7 points and contains A_n. At most one index contains p; at least seven sources in A_n or six in S_n are nonexceptional p-free and share q. For n=2p, Bertrand supplies p<q<2p.

### General n>=16

At most one nonexceptional primitive and one transitive imprimitive source can occur. Hence at least six intransitive sources remain in A_n, or five in S_n. No disjointness after set-stabilizer enlargement or index-list converse is used.

## 10. Exact dependency boundaries and nonclaims

Family I uses ordinary Sylow/Cauchy/Lagrange/orbit facts, finite fields and NC7. NC7 uses A7 simplicity and Eisenstein. Family II uses JORDAN-PRIME and BERTRAND plus ordinary finite-group facts. NC7 is not used in Family II, and Jordan/Bertrand are not used in Family I.

Named classical inputs are not newly proved: A7 simplicity; JORDAN-PRIME, read only as the supplied Jones1209.5169 Theorem1.1 statement; and BERTRAND, read through the supplied Galvin record, with the original Erdős body inaccessible. Their original proofs are **NOT_RECONSTRUCTED HERE**. No Mathematica/Galvin numerical estimate, prime-gap/BHP abstract, HSC/Guest/CFSG/GAP library or historical calculation is a premise.

Current parents are read at their scopes. The86LF prime-window adoption is not transferred to v2. The P7 source-barrier adoption is not an input. The global-kernel adoption supports NC7 at its own scope and carries its separate M1; NC7 itself does not depend on M1.

No full arbitrary-group Sun8, all A_n/S_n degrees, PGL2/field-automorphism groups, other simple families, infinite groups, eight-coset witness or numeric cutoff follows. Novelty/priority remain UNPERFORMED/UNCLEAR.

## 11. Process, assurance and return boundary

The owner's 33m10s cadence major, all earlier owner/parent findings, the v101 missing-frozen-scope finding and my own two disclosed RQLS findings remain permanent. A correct proof does not cure them. Parent delay before release is recorded only as reported and not attributed to this reviewer.

All reconstruction here is WRITTEN exact integer/finite-field/group reasoning, with source/hash/LF/date metadata only. No scientific interpreter/calculator/eval/program/CAS/enumeration/prime-or-field calculator/solver/replay/build/test/CLI/nested agent or GO was used.

This is ordinary same-harness written review, not blind/configured-family/human/formal/kernel/executable/novelty acceptance, parent adoption, a new owner, a deadline reset or round closeout. Original cutoff2026-10-27T11:05:38-07:00 and deadline12:35:38 are unchanged. Own RQLS primary and v106-F remain paused/queued until this actual RETURN and a separate qualified ACK.
