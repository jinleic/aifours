# Shor — the ACTUAL one-b set: exact complement automaton and a finite linear border criterion

Owner MathShor / MathShor-2. Actual `/bin/date` before writing: **Sun Oct 25 15:55:40 PDT 2026**. WRITTEN CANDIDATE, unreviewed. No scientific interpreter/program/arithmetic execution/enumeration/replay/solver/CLI/nested agent/new GO. This is NOT a solution of finite raw completion.

## 0. Why this successor is needed

`shor-common-mate-carry-cocycle-and-reset-control-v1.md`, SHA256 `5cd70c2f82e473c7e651856f8ed2da5babfe22f072cbe3383f801cc39a0820f7`, deliberately analyzed an EXISTENCE-normal-form Y. Its bounded-carry-potential obstruction must not be generalized to an arbitrary hypothetical original completion without a preservation theorem.

The present representation uses the ACTUAL arbitrary one-b residue set Y of a candidate. It allows every unknown row, output, cyclic wrap and original support; no restriction row(i)inA or normalization of Y is made. The result concerns ONLY the long-run cyclic border interface. It still does not encode actual short gaps, raw lifting/isolates, multib words or their finite realization.

## 1. Exact data and matrix orientation

Fix n, nonempty A,B subsets of Z_n with A+B=Z_n direct and0inA. Write a=|A|,b=|B|,ab=n. Let Y be ANY set of residue pairs, represented by its0/1 matrix

    H(i,j)=1 iff(i,j)inY.

For every residue r let P_r be the permutation matrix whose entry(row d,column i)is1 iff d+i=r in Z_n. For a row vector U define

    T_r(U)=U P_r H,
    (T_r U)(j)=sum_(d+i=r) U(d)H(i,j).                    (1)

All these are integer maps; multiplicities are retained, not clipped. Start with U_empty=1_B, and put U_(wr)=T_r(U_w). Define the convolution operator K_A on row functions by

    (K_A U)(r)=sum_(j+s=r)U(j)1_A(s).                      (2)

The ALL-t border map is the actual tuple map

    B x Y^t x A -> Z_n^(t+1),
    (d,(i1,j1),...,(it,jt),s)
      ->(d+i1,j1+i2,...,jt+s).                            (BT)

For a prescribed output(r0,...,rt), its exact fiber size is

    (K_A U_(r0...r_(t−1)))(rt).                           (3)

This follows by expanding (1): it counts ALL choices of successive actual Y pairs and the actual initial B element, then (2) counts the final A element. It does not assume uniqueness in advance.

## 2. Exact all-t equivalence, with all hidden multiplicities controlled

The following are equivalent for this FIXED n,A,B,Y:

1. BT is bijective for EVERY t>=0.
2. EVERY reachable U_w satisfies K_A U_w=1.
3. EVERY reachable U_w is the0/1 indicator of a genuine direct complement D_w of the SAME A.

The equivalence1<=>2 is the fiber count(3), including all possible final outputs. For2=>3, every reachable U is nonnegative integral. Since0inA, its own coefficient U(j) is one of the nonnegative summands in(K_AU)(j)=1. Thus U(j)<=1; no internal path multiplicity or colliding residue tuple has been discarded. The convolution identity then gives an actual direct tiling, and summing gives |D_w|=b. The converse is immediate.

In particular a candidate satisfying ALL-t BT has an exact finite deterministic automaton of reachable COMPLEMENTS, with transition D->T_r(1_D). There are at most binomial(n,b) such indicators. This finite automaton is not guessed from a dimension count: (1) and the nonnegative fiber argument establish its exact states and transitions.

For an arbitrary pair D outside this reachable family, T_r(D) may instead be a multiset or fail to complement A. Such a transition is a genuine border failure, not silently projected back into the state space.

For the original Shor seeds, the one-step states U_3,U_8 contain J2 and U_11 contains J3, because0inB and the literal Y rows3/8/11 supply those outputs. U_3 and U_8 are NOT assumed equal, and no unknown row of the actual Y has been set equal to a preferred mate. This recovers the exact three-complement necessary gate without canonical narrowing.

## 3. A finite-depth LINEAR test for the fixed candidate

Let

    N_A=ker(K_A) over Q,
    d=dim_Q N_A.

Nonempty A makes K_A nonzero, so d<=n−1. Assume the t0 condition A+B=Z_n. Define the differences

    v_w=U_w-1_B,
    V_k=span_Q{v_w: |w|<=k},   V_0={0}.                   (4)

Equation(1) gives the affine recurrence

    v_(wr)=T_r(v_w)+v_r,
    V_(k+1)=span(V_k, {T_r v:v inV_k, allr}, {v_r:allr}). (5)

If V_(k+1)=V_k at ANY stage, (5) makes V_k invariant under all T_r and includes all v_r, so all later spaces are equal to it. This is a proof of stabilization of THIS linear span, not raw-code STAB.

**Finite border criterion.** BT is bijective for EVERY t iff it is bijective for EVERY0<=t<=d+1.

Proof of sufficiency. The assumed finite list and(3) imply every v_w with |w|<=d+1 lies in N_A, hence V_(d+1)subsetN_A. A chain starting with dimension0 cannot have d+1 STRICT increases while staying in a d-dimensional space. Some V_k=V_(k+1), k<=d. By(5) all future differences lie in that same subspace, still contained in N_A. Hence K_A U_w=K_A1_B=1 for EVERY word, and §2 gives ALL-t bijectivity with the original nonnegative counts. Necessity is immediate.

Equivalently, if ANY border failure exists for this fixed candidate, one exists with t<=d+1. This does NOT give a universal finite-depth obstruction for the original unknown n/Y or for actual raw multib completion.

No Fourier or numerical matrix rank was executed. If desired, standard finite Fourier diagonalization identifies d with the number of Fourier zeros of1_A, but that characterization is unnecessary for the proof.

## 4. Structural rank bound from actual tiling, with equality characterized

The convolution matrix K_A has rank at least b: the b translated indicators1_(A+x), x inB, are columns with disjoint nonempty supports partitioning Z_n, hence linearly independent.

More precisely, rank(K_A)=b iff A is a coset of a subgroup. Here is the full equality argument, not an imported uncertainty slogan.

If the rank is b, every translate1_(A+x) is a linear combination of the above b disjoint tile indicators. On each nonempty block A+y the combination is constant. Since1_(A+x) is binary, each coefficient is0 or1. Its cardinality is a, equal to ONE block, so exactly one coefficient is1. Thus EVERY translate of A equals one of these b tile blocks.

The translation orbit therefore has b members. The stabilizer H of A has size n/b=a. Since A is H-invariant, it is a union of H-cosets of total size |H|, hence ONE coset. Conversely, if A is a coset of H, its translates are exactly the b disjoint H-cosets, so the convolution matrix has rank b.

In the Shor setting0,3,8inA. If A were a subgroup, the two elements3,8 generate ALL Z_n because gcd(3,8)=1, so A=Z_n and b=1, contradicting the distinct J0 seeds. Consequently

    rank(K_A)>=b+1,
    d<=n−b−1,
    d+1<=n−b.                                            (6)

Thus t<=n−b is a valid sufficient finite border depth for EACH fixed hypothetical Shor candidate. This is NOT a new lower bound on n or a proof that any such candidate exists. Unknown n,b and all raw obligations remain unbounded.

## 5. What this settles and what it explicitly does not

This successor removes the normalization caveat for the FINITE RESIDUE-CLOSURE statement: every actual Y satisfying the true all-t border interface, not merely the special row form, has the exact finite complement automaton of §2 and the finite linear border criterion of §3. No selected seed architecture or caller-supplied multiplier family was substituted.

The representation is useful for an actual future symbolic candidate: every failure produces a real repeated-residue tuple count at a bounded depth depending on that candidate's exact A. It is not a certificate that a finite raw code has been constructed. Its states ignore how many actual a^n blocks were inserted or cannot be cancelled, short internal gaps, isolated-word lifts H, and the b-count/length of a new raw bridge.

A concrete control from the earlier common-mate construction makes the logical boundary explicit: if a common-mate witness exists, the row-normal Y already satisfies ALL-t BT and therefore all finite tests above, yet the corresponding one-b-only M0 is necessarily incomplete because its sixteen C pairs overfill degrees0..14 in the complete-code Bernoulli identity. That is a conditional control, not an actual witness whose existence has been proved.

Therefore neither finite automaton closure, linear-span stabilization, a fixed-candidate finite-depth test, nor a synchronizing residue word may be renamed raw STAB/GP. The missing theorem must treat actual positive PR lifts and every real higher-gap macrocode at arbitrary lengths and heterogeneous delays, OR deliver an actual finite complete UD extension. No such theorem or extension is supplied here.

The normal-form positive carry-cycle/potential obstruction remains ONLY at its stated scope; it has not magically become an obstruction for every actual Y or arbitrary multib bridges. A raw finite extension can change transitions/costs rather than be a bounded potential correction to the old row-normal automaton.

## 6. Named dependencies, original gap, and assurance

The sole problem-specific imported interface is the actual long-run border extraction from a hypothetical finite raw completion, with raw-to-residue injectivity and0inA,B, as written in `shor-common-complement-uniform-trades-consolidated-v1.md` §§1–2, SHA256 `1697ed1a7d7051d9c5a63e2531abb539e7af96e12a41046c8e862adc51b7ca83`. This interface remains WRITTEN/unreviewed in that successor; it is not being relabeled formal or an independently accepted new theorem. The matrix orientation, finite automaton equivalence, finite-depth criterion and rank equality proof are completely supplied above.

Elementary finite-dimensional rational linear algebra, orbit–stabilizer for the finite translation action, and nonnegative integer counting are the classical imports. No Cordero realization converse, H*, Coven–Meyerowitz conjecture, complete-known-construction classification or unsupplied splitting theorem is a premise.

Original Shor FACT, common-mate existence, k7/Phi_n-divisible and ALL larger trades, actual PR-saturated raw finite prefixes, every higher-gap arity and eventual raw STAB remain OPEN here. All-order FACT660 versus extra full-code1320 distinctions remain. H* as formalized is WITHDRAWN, not an open usable premise.

All calculations are WRITTEN only, not formal/kernel, executable, triple-witness, configured-family, human, independent-review, novelty/SOTA or publication acceptance. No source/frozen parent/shared file was edited. The original cutoff2026-10-27T11:05:38-07:00 and deadline12:35:38 remain unchanged; the96-hour round is not closed.
