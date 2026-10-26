# Shor's full16-word bayonet gate: exactly three complements of one cyclic tile

Owner MathShor / MathShor-2. Actual preceding `/bin/date`: `Sun Oct 25 14:08:51 PDT 2026`. WRITTEN CANDIDATE, unreviewed. No scientific execution or GO. The original finite raw UD factor-complete question remains NOT_PROVED.

This is a change of representation that retains ALL16 words. It eliminates an unknown one-b set Y and its arbitrarily long border products from an EXISTENCE gate, replacing them by TWO additional complement sets of the SAME unknown endpoint tile. It is NOT a raw finite-completion converse, a PR-saturated prefix or an all-order obstruction.

## 1. Definitions and exact theorem

Let

    I={0,3,8,11},
    J0={0,1,7,13,14},
    J2={0,2,4,6},
    J3={0,1,2}.

The literal Shor pairs are

    C_pairs=({0}xJ0) union ({3,8}xJ2) union ({11}xJ3).

Fix a positive n and a direct cyclic factorization A+B=Z_n with I subset A and J0 subset B, all seed residues distinct. Thus n>=20 and all C exponents are less than n. Use canonical representatives in[n]={0,...,n-1} whenever writing RAW words.

**Theorem (same n,A,B).** The following three EXISTENCE statements are equivalent:

**(ONE)** There is a finite residue set Y subset Z_n^2 containing C_pairs for which

    B x Y x A -> Z_n^2,
    (r,(i,j),s) -> (r+i,j+s)

is bijective.

**(TWO)** There are sets D2,D3 subset Z_n such that

    A+D2=Z_n directly, J2 subset D2,
    A+D3=Z_n directly, J3 subset D3.

Their cardinalities automatically equal |B|. Together with the GIVEN B, these are the three complements of A.

**(ALL)** There is a set Ytilde containing C_pairs such that for EVERY t>=0,

    B x Ytilde^t x A -> Z_n^(t+1),
    (r,(i1,j1),...,(it,jt),s)
       -> (r+i1,j1+i2,...,j_(t-1)+it,jt+s)

is bijective (the t0 map is B+A). The same n,A,B are preserved, but Ytilde need NOT equal a supplied Y in ONE.

Any finite full completion of C supplies ONE by the existing written long-run border extraction in the original dossier §3/B3. This hypothesis involves actual finite words and all-list UD/completeness; no cbc-realization conjecture is imported. Its extraction is recalled in §4.

## 2. ONE implies TWO: exact row slices with multiplicity retained

For k in Z_n, define a NONNEGATIVE integer counting function

    D_k(j)=#{(r,(i,j)) in B x Y : r+i=k}.

Bijectivity in ONE says

    D_k * 1_A = 1 on Z_n.

Because0 belongs to A, the coefficient at j of this convolution is at least D_k(j). Hence D_k(j)<=1 for every j: no hidden multiplicities survive. Thus D_k is the indicator of an actual subset, denoted by the same symbol. Summing coefficients gives

    |D_k||A|=n, so |D_k|=|B|,
    D_k+A=Z_n directly.

Since0 belongs to B, each C row at i=k contributes its right exponents to D_k. Therefore J2 subset D_3 (also J2 subset D_8), and J3 subset D_11. Set D2=D_3 and D3=D_11. These are the required common complements of THE SAME A. No pairwise compatibility or independent phases were assumed.

## 3. TWO implies ALL: an explicit row-homogenized witness

Define complements D_i of A for EVERY i in A by

    D_0=B,
    D_3=D_8=D2,
    D_11=D3,
    D_i=B for all other i in A.

Then put

    Ytilde = union_(i in A) ({i} x D_i).

These rows are disjoint, so |Ytilde|=|A||B|=n, and the entire literal C_pairs is included.

Fix an arbitrary output (x0,...,xt) in Z_n^(t+1). Its unique preimage is reconstructed successively:

1. B+A=Z_n gives the unique (r,i1) with x0=r+i1.
2. D_(i1)+A=Z_n gives the unique (j1,i2) with x1=j1+i2.
3. Continue using D_(ik)+A at every internal coordinate.
4. At the last coordinate, D_(it)+A gives the unique (jt,s).

At each step the selected pair is exactly a member of the row in Ytilde. This proves BOTH existence and uniqueness for every t, not a finite-depth check. For t0 use B+A directly. It also proves ALL implies ONE by taking t1, completing the equivalence.

This is an existential NORMAL FORM for this border gate, not a theorem that the original actual Y can be replaced inside an existing raw complete code while preserving its other words/delays.

## 4. How a full raw completion supplies the gate

For a hypothetical finite complete UD M containing C, let a^n be its unique pure-a word, A its end-exponent residues from words a^s b^d (including0 via b), B its start-exponent residues from b^e a^r, and Y its one-b residues from actual a^i b a^j words.

For each desired residue pair choose sufficiently LONG a-runs and pad with b-runs longer than the maximum word length:

    b^D a^E0 b a^E1 b^D.

Completeness supplies a parse. The unique word containing the middle b is a one-b word, the outer mixed words give B/A endpoints, and all remaining words are a^n. Reduction modulo n gives the stated ONE map's surjectivity. Any two residue preimages can be padded to common outer b lengths and common large a lengths, giving distinct actual M-lists for the same word; UD therefore gives injectivity, including raw-to-residue injectivity. The no-middle-b case supplies the direct factorization B+A.

This is the earlier all-run long-core proof restricted to t0/t1. No unproved general cyclic-factorization-to-code converse is used.

## 5. What a common-complement witness would actually deliver

TWO would construct the explicit FINITE RAW set

    M0={a^n} union {a^i b a^j : (i,j) in Ytilde, 0<=i,j<n}.

It contains all16 literal C words and b. **M0 is UD.** To prove this, take equal products of M0 words. Counting b's gives the same number t of Ytilde factors. Reducing the a-exponents modulo n gives two ALL preimages with outer markers r=s=0, so the Ytilde word sequences agree. The numbers of intervening a^n words are then fixed by each actual run length, including the two outer runs. Thus the original lists agree.

This proof is purely written and does NOT certify any M0 here, because D2,D3 and A,B have NOT been supplied.

### M0 could not itself be complete

If this UD set were finite factor-complete, the standard written Bernoulli identity would give, for every0<x<1,

    1=x^n+(1-x) sum_((i,j) in Ytilde) x^(i+j).

Hence sum x^(i+j)=(1-x^n)/(1-x)=1+x+...+x^(n-1). The right side has exactly15 terms in degrees0..14, counted with multiplicity. But C contributes16 terms with i+j<=14 to the left side. All coefficients are nonnegative. This is impossible.

So even a successful TWO witness yields a finite UD but INCOMPLETE code. It is not the required finite completion.

### Not even PR saturation follows automatically

M0 has the endpoint polynomials L=B, R=A and no isolated two-b words. PR would require the literal identity A(z)B(z)=S_n(z), not only its cyclic reduction. Wrapped sums generally require the nonzero isolated-word lift H of v2/LIFT. The construction above has not added or realized H, and arbitrary additions can break UD.

Therefore no 'residue-to-literal cancellation', raw cutover, or hidden PR/STAB completion is asserted. Actual delays, lifted isolated words, all internal gap classes and eventual bridge termination remain separate obligations.

## 6. New exact negative and positive frontier

- **Negative:** proving that no tile A at ANY order has three complements of the three stated types would exclude ONE/ALL and hence every finite raw completion. This is stronger than endpoint FACT because it uses EVERY row of C. No such theorem is supplied.
- **Positive:** one common A with these complements would give a genuine finite all16-word UD extension and an exact all-t border model by §3/§5. Its actual finite factor-completion would still require all PR/STAB/GP obligations.
- The complements must share one A and one modulus/cardinality. Constructing each for different tiles or independently unioning them is not a witness.
- The known forced-seed multiplier separator does not prove these complement sets exist and cannot rule them out by itself.

The remaining common-complement existence step is unproved. No novelty, formal, executable, independent-family or whole-book solution claim is made. All output here is WRITTEN; no scientific interpreter, enumeration, replay, solver, nested agent, external model CLI or GO occurred.
