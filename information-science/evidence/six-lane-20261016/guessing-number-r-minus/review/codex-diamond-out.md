PROVED (option C): All eight conditional Ingleton inequalities can fail simultaneously in a genuine code satisfying every global FD. Moreover, all three right-hand-side mutual informations can vanish in every inequality. Thus (B) is false, and incompatibility of the eight AND/OR patterns cannot supply the proposed obstruction.

PROVED (five-vertex gadget): Consider a fan with hub T and rim path A-B-C-D. Use the following five binary words, uniformly:

T A B C D
0 0 0 0 0
0 0 1 1 0
1 0 0 1 0
1 1 1 1 0
1 0 0 0 1

Every vertex has a decoder using its fan neighbours. On these words,

A = T AND B,
D = T AND NOT C,
B = A OR ((NOT T) AND C),
C = (T OR B) AND NOT D,
T = A OR D OR (C AND NOT B).

These identities explicitly verify all five FDs.

PROVED (code on R^-): Independently choose one gadget word for each of these four fans:

Fan   T   A   B   C   D
1     1   2   3   4   5
2     1   2   7   6   5
3     8  10   4   3   9
4     8  10   7   6   9

Every required fan edge belongs to R^-. Every vertex appears in exactly two fans; its symbol is the ordered pair of its two gadget bits. This gives alphabet size s = 4 and exactly 5^4 = 625 distinct codewords.

Each symbol is recovered coordinate by coordinate using the displayed decoders and actual neighbours in R^-. Consequently every global FD holds, including every constancy consequence in (F5).

COMPUTED-BY-HAND (gadget entropies): Define the Ingleton gap by

J(U,V;P,Q | Z)
= I(U;V | Z,P) + I(U;V | Z,Q)
  + I(P;Q | Z) - I(U;V | Z).

Put

delta = 5/2 - (3/2) log2(3) > 0.

For the first fan diamond (A,C;T,B | D), the event D = 0 has probability 4/5. On that event, T,B are independent uniform bits and

A = T AND B,   C = T OR B.

All three positive terms in J vanish, and I(A;C | D=0) = delta. The event D = 1 is a singleton. Therefore

J(A,C;T,B | D) = -(4/5) delta.

For the second diamond (B,D;T,C | A), the event A = 0 also has probability 4/5. On that event, T,C are independent uniform bits and

B = (NOT T) AND C,
D = T AND NOT C.

Given either input, one output is constant. The output distribution is

Pr(B,D = 0,0) = 1/2,
Pr(B,D = 1,0) = Pr(B,D = 0,1) = 1/4.

Thus the three positive terms again vanish and I(B;D | A=0) = delta. The event A = 1 is a singleton. Hence

J(B,D;T,C | A) = -(4/5) delta.

PROVED (all eight diamonds): The two diamonds in each fan are exactly the eight listed in (F2), allowing swaps within the endpoint pair or the common-neighbour pair.

Entropy and conditional mutual information add across independent gadget factors. For any listed diamond, each of the other three fans contains at most one endpoint and at most one common neighbour. Its contribution to each of the four mutual informations is therefore zero.

Consequently, in the constructed alphabet-4 code, every listed diamond satisfies exactly

I(P;Q | Z) = 0,
I(U;V | Z,P) = 0,
I(U;V | Z,Q) = 0,
I(U;V | Z) = (4/5) delta > 0.

This realizes all eight of the relevant AND/OR entropy patterns under the full global FDs.

COMPUTED-BY-HAND (rate limitation): Writing h2 for binary entropy, the gadget bits T,B,C each have entropy h2(2/5), while A,D each have entropy h2(1/5). Therefore the full code has

H(V) = 4 log2(5),
max_v H(X_v) = 2 h2(2/5),

and

H(V) / max_v H(X_v)
= 2 log2(5) / h2(2/5)
< 20/3.

The last inequality is exactly equivalent to 5^7 > 16·3^6. Thus this construction does not achieve (A).

PROVED (arbitrarily close rates): Taking its direct product with m copies of the given alphabet-8 optimal linear code gives

s = 4·8^m,
|C| = 5^4·2^(20m),

and rate

log_s |C|
= (20m + 4 log2(5))/(3m + 2)
→ 20/3 from below.

The optimal linear factor has zero diamond gaps: equality in its F1 certificate forces both its nonnegative Ingleton gap and its S-slack to vanish. Hence all eight strict violations persist in these products. After normalization, both the violations and S-slack shrink proportionally; padding does not improve their trade-off.

COMPUTED-BY-HAND (exact verification targets): A computer can independently:

1. Enumerate the 625 words from the four five-row tables.
2. For every vertex, group words by neighbour symbols and check that its own symbol is unique within each group.
3. For all eight diamonds, verify the three conditional independences by integer cross-products of conditional counts.
4. Evaluate the remaining mutual information symbolically as (4/5) delta; positivity reduces to 27 < 32.

PROVED (scope): This supplies an explicit obstruction to (B) and to a proof based on forbidding simultaneous AND/OR patterns. The unresolved issue is their quantitative entropy cost relative to F1’s slack; no improvement over 20/3 is established here.