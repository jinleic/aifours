# Explicit512-bit ceiling-sharpness witness and exact symbolic Walsh certificate

Observed before creation: **2026-10-23T14:57:14-07:00**. Author: InfoBalancedNL242, info-6. Parent selected and approved this bounded construction-side action. Verification here is **written exact factorization and block accounting**, not an executable FWHT/direct-sum replay, proof-assistant check or independent-model review.

## 1. Pinned literal object and exact bit order

The complete literal truth table is

[`sharpness-q8-plus-t-v1.bits`](sharpness-q8-plus-t-v1.bits),

SHA256

`8430a917cff686cf702cc73138cd9728e88ae9982d1d57944c7052d0a2f82443`.

The write operation reports513 bytes:512 ASCII0/1 characters followed by one LF. The file was read back directly, and the SHA256 above was observed with `shasum -a 256`. No native scientific check or program generated these bits.

For character index `j=0,...,511`, use `x_i=(j>>i)&1`, i=0,...,8. Character j is f(x_0,...,x_8), with x_0 changing fastest. Put t=x_8. This is NOT a convention that reverses the whole hexadecimal integer.

For a readable complete representation, the following eight consecutive64-bit blocks give all512 bits. Each hex digit expands most-significant bit first within that digit; concatenate rows in index order.

| Character indices |16 hexadecimal digits|
|---|---|
|0–63|`111E111E111EEEE1`|
|64–127|`111E111E111EEEE1`|
|128–191|`111E111E111EEEE1`|
|192–255|`EEE1EEE1EEE1111E`|
|256–319|`EEE1EEE1EEE1111E`|
|320–383|`EEE1EEE1EEE1111E`|
|384–447|`EEE1EEE1EEE1111E`|
|448–511|`111E111E111EEEE1`|

## 2. Literal blocks implement the stated Boolean function

Define

`A=0001000100011110`, `B=1110111011100001=not A`,

`C=A A A B`, `D=B B B A=not C`,

where juxtaposition means concatenation, not multiplication. The64-bit strings are explicitly

`C=0001000100011110000100010001111000010001000111101110111011100001`,

`D=1110111011100001111011101110000111101110111000010001000100011110`.

The literal witness has block word

`C C C D D D D C`.                                         (1)

This block word is exactly the eight-row representation above.

For two input bits, the truth table of x_0x_1 in increasing integer order is `0001`. Adding the next pair product x_2x_3 gives three copies of this word and then its complement, hence A. Adding x_4x_5 gives C; adding x_6x_7 gives `C C C D`. Finally adding t complements that entire256-bit word in the second half, giving (1).

Thus the actual displayed literal table represents exactly

`q(x)=x_0x_1+x_2x_3+x_4x_5+x_6x_7`,

`f(x,t)=q(x)+t` over F_2.                                 (2)

No unlisted seed, input permutation, hidden half completion or numerical search is used.

## 3. Exact balance by block counts

The word A has six1s: `0001` occurs three times and `1110` once. B has ten1s. Therefore C has `3*6+10=28` ones, and D has36. The complete word has four copies of C and four of D, so its weight is

`4*28+4*36=256`.

Equivalently every fixed x gives opposite outputs for t=0 and1. Both are definition-level proofs that the pinned512-bit function is balanced.

## 4. Exact factorized Walsh transform at every frequency

Use the same unnormalized convention as the selection:

`W_f(a,b)=sum_{x in F_2^8,t in F_2}(-1)^(q(x)+t+a.x+bt)`.

For one pair and arbitrary alpha,beta in F_2,

`sum_{u,v in F_2}(-1)^(uv+alpha u+beta v)`

`=1+(-1)^alpha+(-1)^beta-(-1)^(alpha+beta)`

`=2(-1)^(alpha beta)`.

The last equality follows directly for the four possible alpha,beta; it is an exact finite algebraic identity, not inference from sampled parameter values.

The four independent pair sums multiply, giving for every a

`W_q(a)=16(-1)^(a_0a_1+a_2a_3+a_4a_5+a_6a_7)`.

The remaining t sum is

`sum_t(-1)^((1+b)t)=0 if b=0, and2 if b=1`.

Consequently the complete512-coefficient spectrum is exactly

`W_f(a,0)=0`,

`W_f(a,1)=32(-1)^(a_0a_1+a_2a_3+a_4a_5+a_6a_7)`.           (3)

This proves every coefficient in the full domain, rather than a histogram assumed by a producer.

The quadratic sign in (3) has total sign sum16, by the same four-pair factorization at frequency0. Its positive/negative counts therefore satisfy

`P+M=256`, `P-M=16`,

so P=136 and M=120. The **signed** spectrum has256 zeros,136 coefficients+32, and120 coefficients−32.

## 5. Explicit magnitude counts, including the actual definition of L

The magnitude-class counts over **all512 frequencies** are

| magnitude j |0|4|8|12|16|20|24|28|32|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| N_j |256|0|0|0|0|0|0|0|256|

Every other magnitude class has count0. Thus, by the literal counting definition used throughout this lane,

`L= #{(a,b): |W_f(a,b)| in {4,12}} =N_4+N_12=0+0=0`.

This is a counted fact, not an unstated inference from a peak. The peak is32, and

`NL(f)=256-(1/2)*32=240`.

As a separate consistency identity, `sum W_f^2=256*32^2=262144`, exactly the nine-variable Parseval total. The coefficient at frequency(0,0) is0, consistent with the independent block weight count.

## 6. What this concretely closes—and what it does not

This pinned literal object has, by the written exact certificate above:

-512 defined truth bits;
- weight256;
- exact Walsh spectrum0/+32/−32 with counts256/136/120;
- exact nonlinearity240;
- L=0 over all512 coefficients.

It therefore supplies the concrete attaining side of

`max {NL(g): g balanced on nine variables, L(g)<=3}=240`,

whose upper bound remains dependent on actual acceptance of the queued mod3 sparse-defect proof. The construction itself is the classical bent-concatenation family; no discovery or priority claim is made.

This function has peak32 and is **not** a balanced242 candidate, not a member of the peak28 residue frontier, and not a new obstruction for any of the seven unresolved types. The saturation decision and residual union remain unchanged.

## 7. Verification and trust ledger

**Performed:** manual exact block construction; direct read of the literal file; observed byte count from the write tool; SHA256 metadata pin; written weight count; complete all-frequency algebraic Walsh factorization and signed/magnitude counting.

**Not performed:** executable FWHT, executable direct character sums, affine-distance enumeration, mutation controls, three independent checker implementations, proof-assistant/kernel replay, outside-model CLI or human review. No scientific executionGO was requested or consumed. The parent explicitly approved the literal table with this factorized symbolic certificate, not an unadmitted native replay.

A separate reader can reconstruct (1) from the literal bytes and reconstruct (3) from (2). Any later executable check must obtain its own exact parent admission and bind the pinned bytes above. This immutable certificate records the written level only.
