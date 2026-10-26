# Sun8 — complete ACTUAL source-lift bridge: uniform six forces an index-seven block quotient and a contradiction

Owner MathSun8 / math-6. Actual `/bin/date` before this body: `Sun Oct 25 15:11:40 PDT 2026`.
Status: **NEW WRITTEN CANDIDATE at the EXACT named union below; NOT ACCEPTED.** Current v92 reviews of the 644-LF three-part manuscript remain unchanged and do not retroactively include this successor. This is ONE complete bridge and both applications, not another catalogue of local quotient restrictions. HOLD/v9/v10/v11: no scientific eval/interpreter/arithmetic program, symbolic execution, enumeration, solver, replay, external CLI, nested agent or new GO.

## 1. Exact direct theorem and the current unaccepted source union

The direct theorem concerns an ACTUAL finite group G with EIGHT pairwise-disjoint LEFT cosets, [G:U_l]=7r_l, all private r_l positive and pairwise coprime. Select one coset and left-translate all eight so it is U containing identity. Six of the other full original subgroups are indexed j=1,...,6 and called regular; the remaining one is e. Assume an ACTUAL subgroup M<=G with

[G:M]=7t,  gcd(t,r_j)=1 for every regular j,
[U_j:U_j∩M]=6t,  gcd(r_j,6)=1 for every regular j.

No regular U_j is replaced by its intersection, and the original selected U, exceptional U_e and their coset representatives are retained. The theorem is:

> **UNIFORM-SIX SOURCE CLOSURE:** no such actual eight-coset family and M exist.

The proof below uses two fully written finite-group ingredients from COMPLETE manuscript Part2: NC7 (six disjoint index-seven cosets have one index-seven complement), and the complete faithful degree-seven group/index-seven-subgroup classification. Their source is `sun8-global-kernel-section-complete-v1-part2.md`,181 LF, SHA256 `2c8949dfa512ca3d89549b04d42bea9be8a515081cb3a3ba7762dd3b2e7b46e8`. It is an UNREVIEWED new candidate at v92, not an adopted premise by headline. The proof adds the standard CLASSICAL simplicity of A6 at the one explicit index-five point-stabilizer step. A7 simplicity/Eisenstein remain the named inputs of the Part2 NC7 proof. No CFSG, transitive-group catalogue or computed character table is used.

For the two Sun8 applications, COMPLETE manuscript Part1 (246 LF, SHA256 `b6e3125ab95b8e67dd974f965f2472002e37c7df82291b92abdda321ee4a0130`) derives actual kernels at GLOBAL binary-C rank three and ODD-Q GLOBAL REGULAR ternary rank two. COMPLETE Part2 derives M=N_G(B), [G:M]=7t, t|s and the exact uniform-six full-source index. Thus all displayed direct hypotheses hold there. Those parts are supplied proofs requiring their own new union audit; this successor claims no prior acceptance of them. COMPLETE Part3 is NOT mathematically needed for the closure: its fine common-core, prime-five and four-power section classifications are bypassed, not used as hidden assumptions.

## 2. TWO actual orbits of each full original regular U_j

Let Omega be the SET G/M of 7t left M-cosets, with its actual left G-action. For ANY U_j-orbit through gM, the stabilizer intersection index gives

7t divides [G:U_j] times orbit length =7r_j times orbit length.

Since gcd(t,r_j)=1, every such orbit length is a multiple of t. The orbit through the basepoint M has length [U_j:U_j∩M]=6t. The remaining t points form ONE further orbit, not an arbitrary subset. Denote this UNIQUE small U_j-orbit T_j, of size t. The basepoint M is outside T_j.

This constructs T_j from the FULL original group U_j and its action on the SAME actual G/M. No quotient diagram, individual conjugation or independently chosen partition has been substituted.

## 3. Complete elementary representation argument for the shared component

Use the standard Hermitian permutation modules X=C[Omega] and Y_j=C[G/U_j]. A G-equivariant matrix Y_j->X is constant on the diagonal G-orbits in Omega times G/U_j, which correspond to U_j-orbits on Omega. Therefore the space of such intertwiners has dimension TWO by §2.

For clarity, the elementary representation facts used next have the following content. A unitary finite-group module decomposes into orthogonal irreducibles by taking invariant orthogonal complements recursively. A map between irreducibles is zero or an isomorphism by its kernel/image; over C a commuting endomorphism is scalar because subtracting an eigenvalue has nonzero kernel. Thus the intertwiner dimension is the sum of products of irreducible multiplicities. Both transitive permutation modules contain constants once. The remaining dimension ONE means there is EXACTLY ONE shared nontrivial irreducible chi_j, with multiplicity ONE in BOTH X and Y_j. No character table or scientific computation is being imported.

Construct the ACTUAL integer incidence matrix I_j with rows omega in Omega and columns gU_j, putting entry one iff omega lies in gT_j. It is well-defined because T_j is U_j-invariant and is a G-intertwiner. Each column has t ones; G-transitivity of Omega and the total incidence count give row degree r_j. Its columns are proper nonempty subsets, so it has nonconstant image. Consequently its image is EXACTLY the constants plus the unique chi_j-subspace of X. Denote that nontrivial subspace W_j.

All matrices below are explicitly defined incidence operators from original subgroup actions. None was generated or evaluated by a program. The adjoint is the ordinary transpose, since entries are real.

## 4. DISTINCT shared irreducibles are impossible by an original-index divisibility

Suppose W_j and W_k are different irreducibles. They are orthogonal invariant subspaces of X. Hence I_j^* I_k kills the entire nonconstant image of I_k and passes only constants. Column size t and row degrees r_j,r_k give the exact matrix identity

I_j^* I_k = (t/7) J,

where J has all entries one. To check the scale, applying it to the constant column vector gives r_k t times the constant vector on G/U_j, while that vector has 7r_k entries. In particular

|T_j∩T_k|=t/7.

If this is not an integer it is already impossible. More fundamentally it is a POSITIVE size of a subset invariant under A=U_j∩U_k, because both T_j and T_k are actual orbits invariant under their full groups.

The two ORIGINAL left cosets of U_j,U_k are disjoint. Therefore U_jU_k is not G. Pair-index divisibility and the actual product-size formula give

[G:A]=7r_jr_k d,  1<=d<=6.

For ANY A-orbit of length ell on Omega, 7t divides7r_jr_k d ell. Since gcd(t,r_jr_k)=1, t divides d ell, and every such orbit has length a positive multiple of t/gcd(t,d). But gcd(t,d)<=d<=6, so

t/gcd(t,d) > t/7.

The nonempty A-invariant subset T_j∩T_k of size t/7 cannot contain even one such orbit. Contradiction. This is the actual full-source index bound d<=6, not a chosen local arrangement or mere pairwise correlation estimate.

Thus EVERY regular j has the SAME shared irreducible W in X. Pairwise private coprimality and the ORIGINAL disjointness were both essential. No simple-G assumption is used.

## 5. Equal shared component forces ONE actual seven-block system

Let d_W be the complex dimension of W and E its orthogonal projection in X. Since W has multiplicity one, Schur's scalar argument gives

I_j I_j^* = (r_j/7) J_Omega + lambda_j E.

The constant eigenvalue is t r_j: I_j^* sends the constant row vector to t times the constant column vector and I_j sends that to t r_j times the constant row vector. Its trace is 7t r_j (the row degree on each diagonal entry). Therefore d_W lambda_j=6t r_j, and

(I_j I_j^*)/r_j = J_Omega/7 +(6t/d_W)E

is the SAME matrix for every regular j.

For two points x,y let c_j(x,y) be their integer number of common incident columns in I_j, between zero and r_j. For any distinct regular j,k,

c_j(x,y)/r_j=c_k(x,y)/r_k.

Since gcd(r_j,r_k)=1, c_j(x,y) is a multiple of r_j and is either ZERO or r_j. Thus two incidence rows are either identical (common count r_j) or disjoint (zero).

Partition Omega by identical rows. Any column gT_j contains only points from one class, since two points in it share a column and cannot have disjoint rows. Conversely every point with the same row as one member also lies in that column. Thus EVERY gT_j is exactly one equivalence class, of size t. There are SEVEN classes. The G-equivariance of I_j makes this an ACTUAL G-invariant block system.

It is the SAME system for all six regular j: their normalized Gram matrices are equal, so the identical-row relation is identical. In particular every T_j is one of those seven actual blocks. Let Delta_0 be the block containing the basepoint M. Since M fixes that point and preserves the partition, it preserves Delta_0. Its stabilizer L contains M and has index seven. This is a GENUINE original-group overgroup, not one inferred from an integer divisor. It is not yet asserted to be a collision-free replacement for U; the next argument uses the actual normal quotient instead.

Each U_j fixes its small block T_j and is transitive on all points outside it (its large orbit of size6t). Hence its induced action is transitive on the OTHER SIX blocks.

## 6. Faithful degree-seven quotient and FULL images of all regular groups

Let K=core_G(L), the kernel of this actual seven-block action, and pi:G->F=G/K. This K is a NEW actual NORMAL subgroup of G, not the older B and not the common-core C of the section analysis. F is faithful transitive on seven blocks. Every pi(U_j) fixes one block and is transitive on the other six. Thus F is two-transitive.

The COMPLETE degree-seven classification proved in current Part2 gives F one of the affine group42, GL3(2), A7, S7. Their natural point-stabilizer orders are6,24,360,720. The index of pi(U_j) inside that block's full stabilizer divides r_j: [F:pi(U_j)] divides [G:U_j]=7r_j and has factor seven from the fixed block. Since gcd(r_j,6)=1, that relative index is one, except possibly FIVE for A7/S7.

The latter is impossible by classical A6 simplicity, explicitly named here. A6 has no index-five subgroup, since its coset action would inject it into S5 of smaller order. S6 has no index-five subgroup either: its action on five cosets restricted to simple A6 is either injective (impossible by order) or trivial; the latter puts A6 inside a subgroup of order144, also impossible. Hence in ALL cases

pi(U_j) is the FULL block point stabilizer,  [F:pi(U_j)]=7.

The exact original K-kernel index is consequently

[K:K∩U_j]=r_j.

This step did NOT assume that private r_j are prime, that none owns seven, or that an original U_j is already one of the degree-seven point stabilizers in G.

## 7. Normal-core projection preserves ALL EIGHT original cosets

For any original subgroup U_l put d_l=[F:pi(U_l)] and k_l=[K:K∩U_l]. Exact indices give d_l k_l=7r_l. For the SIX regulars, d_j=7,k_j=r_j, so their projected cosets in F are pairwise disjoint by their coprime private K-kernel indices.

At most ONE private factor among the regulars owns seven. Choose ONE regular j with7 not dividing r_j (there are at least five). Its kernel index r_j is coprime to BOTH k_i and k_e, because these divide7r_i and7r_e and all private factors are pairwise coprime. Therefore its index-seven projected coset is disjoint from both the selected and exceptional projected cosets.

If either d_i or d_e lacked seven, that projected subgroup index would be coprime to seven, making its coset intersect EVERY index-seven coset in F. This contradicts the disjointness just proved. Thus seven divides BOTH d_i,d_e. Write d_i=7a_i,d_e=7a_e, where a_i|r_i,a_e|r_e. Then k_i=r_i/a_i and k_e=r_e/a_e divide their OWN private factors.

Now ALL EIGHT K-kernel indices are pairwise coprime. At any common K-fibre their original pieces would be left cosets of coprime-index subgroups of K and intersect. Hence ALL EIGHT projected cosets in F are pairwise DISJOINT, including the selected/exception pair. This restores disjointness by an ACTUAL normal-core calculation; it does not reuse the invalid selected/exception disjointness after the different section quotient R/C.

Apply NC7 to the SIX regular index-seven projected cosets. Their complement is an index-seven coset containing selected pi(U), hence identity; it is a SUBGROUP L' containing all selected pi(U) and all exceptional coset Y. Their subgroup indices INSIDE L' are a_i and a_e, divisors of the two original COPRIME private factors. They must intersect, contradicting their projected disjointness.

This proves the direct **UNIFORM-SIX SOURCE CLOSURE** for arbitrary finite G. It did NOT need G simple, the older global Sun7 reduction, a source-preserving shift of e, or a fabricated collision-free replacement by M.

## 8. Exact high-global-character applications at the current written union

COMPLETE current manuscript Part1 derives actual kernels for the GLOBAL binary-C rank-three family, including EVERY new visible initial-rank-two/duplicate corner, and for ODD-Q GLOBAL REGULAR ternary rank two, including visible INITIAL REGULAR rank one. In BOTH families the six regular r_j are ODD and THREE-FREE, all source kernels and original private indices are retained. COMPLETE Part2 proves the actual M=N_G(B) has index7t with t|s, and ALL six full original indices [U_j:U_j∩M]=6t. Since t|s|r_i, it is coprime to every regular r_j. Thus every direct hypothesis of §1 is supplied by those actual proofs.

At the UNION of those explicitly supplied but still UNREVIEWED Part1/Part2 proofs, this bridge, classical Sun3/Sun4 and the exact R4 import used in Part1, the conclusions are:

* NO achieved-minimum finite P7 witness has GLOBAL binary C-character rank THREE. The actual-source lift is excluded for ALL three binary kernel types and ALL four original e-types, not merely some small M/B sections. The earlier local C=1/V4/E16, four-power and class-two residuals no longer survive at THIS CANDIDATE composed implication, but have not been accepted by it automatically.
* NO achieved-minimum finite P7 witness with ODD Q has GLOBAL REGULAR ternary-B rank TWO. ALL three actual odd section lifts18/54/162, whole and aligned, and the initial-regular-rank-one aligned corner are excluded by this ACTUAL global normal-core lift.

No conclusion uses an older initial-three-character review as a global theorem. These implications require a FRESH JOINT UNION AUDIT; the current v92 no-defect returns, if any, would not alone audit this later bridge or its added classical A6 input. COMPLETE manuscript Part3 is not a prerequisite of the new closure and is not silently promoted.

## 9. Precise first remaining original gap and assurance

The original arbitrary-group Sun8 problem is STILL OPEN here. Remaining direct finite-P7 branches include EVERY GLOBAL binary C-rank<=2 configuration (arbitrary nonabelian quotients included), ODD Q with GLOBAL REGULAR ternary rank<=1, a second ternary direction carried only by the EVEN-private exception, the other odd/no-index-two/maximal/self-normalizing vertices and private-three/five/seven/composite source-preserving enlargement barriers. The earlier elementary-two-rank<=3 boundary is not a total-involution bound and does not remove these branches. The inherited global Sun7/finite-core/normal-section connection remains NAMED CONDITIONAL provenance, not newly authenticated; the bridge itself starts directly in finite P7 and needs no simple-G assumption.

**First unproved step:** derive a comparable actual full-source orbit/kernel representation or a legal all-seven-neighbour-preserving enlargement for these remaining LOW GLOBAL-rank configurations, rather than presume they have six regular uniform-six sources. No claim classifies all rank-two source multiplicities or nonabelian normalizers. Working tetrahedral rank-two ideas are NOT imported as a proved hypothesis here.

This is WRITTEN ONLY with exact finite matrices and indices defined on the original full groups, not a finite executable certificate, formal/kernel proof, configured-family/human/model-independent acceptance, numeric lower-bound promotion, novelty/priority clearance or round completion. All frozen current v92 sources and older correction histories remain unchanged. Primary research continues under the original scope/cutoff/deadline, with no scientific GO.
