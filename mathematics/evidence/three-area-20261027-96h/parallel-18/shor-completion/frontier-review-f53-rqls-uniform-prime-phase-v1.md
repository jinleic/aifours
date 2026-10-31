# f53 — physical uniform RQLS phase obstructions and the p=41 boundary

Reviewer **MathShor-2 / math-5**; author **PhysicsRQLS10-2 / physics-5**.
Native `/bin/date` observed before writing: **Wed Oct 28 17:47:16 PDT 2026**.

## 1. Verdict, exact source scope and historical limits

**NO_SUBSTANTIVE_DEFECT AT EXACT STATED SCOPE: 0 FATAL / 0 MAJOR / 0 MINOR.** The SAME-array uniform support/zero multiplicity and fourteen-partner caller, even-n real and specified two-phase no-gos, ALL-prime-power root lemma including p=41 and arbitrary e, the local complex conference fragment, and the arbitrary-basis support bound are reconstructed below. The genuine hypothesis is a PHYSICAL uniform M_* lift with the stated phase alphabet, **not** an arbitrary complex order-10 resolvable QLS. No original 100-ray no-go, witness, general complex-phase exclusion, novelty, formal/kernel/human or independent-model-family acceptance follows.

The f53 assignment was read FIRST, then the two complete candidate files IN ITS ORDER through endings. Native hashes matched dispatch:

| Source | LF / bytes | SHA256 |
|---|---|---|
| `frontier-20261028-uniform-prime-power-phase-obstruction-v1.md` |85 /7988 | `2b9ac43797a5720e01746dda9f3343c3ea9227f7dcae36f2f1d7c9ddcd7c8467` |
| `frontier-20261028-uniform-phase-obstructions-v1.md` |113 /15017 | `11ae022040c391e2d4151446a6a88e47ab5feefcb27e5d38815e54c4dd945` |
| Original `physics-5-rqls10-packet-v1.md` |35 LF | `10445b20cea55ecf5abb2e35393281a4c43492cfae6d91b4d3dc9b60e7de3863` |
| Parent Gram/physical-uniform disposition | complete status body | `d174add293a61a15ea1c96fff91d3e2889d8ac0396eb3b4e26772d302bad6484` |

The original target is100 pairwise nonparallel rays in C^10 forming row, column and ten transversal ONBs, or an UNRESTRICTED no-go. The parent's M_* is an accepted scalar relaxation; it is not a physical rank-one-projector lift. The present proofs assume an actual physical uniform lift and NEVER infer one from M_*.
My earlier bounded PPT/PH7/RQLS and same-harness documentary contacts remain disclosed; this is not blind, a clean-cognition certificate or retrospective validation of a historical held outcome. No author contact, nested agent, external-model/API, secret, deletion, push/publication or infrastructure mutation.

## 2. Physical row support, zero-pair multiplicity and conference blocks

For arbitrary n>=4, let a SINGLE actual array have three partitions into ONBs: rows, columns and disjoint transversals, the latter each meeting every row and column once. Assume every distinct pair sharing one block has overlap0, and every other pair has squared overlap1/(n−2). Fix ANY reference row ONB as coordinates `e_0,...,e_(n−1)`, indexed by their columns. Its labelled transversal through e_j is T_j.

A nonreference cell x in column i and transversal T_j has i!=j: otherwise that transversal would contain two cells in column i. It is orthogonal to reference e_i and e_j. For every other k it shares no block with e_k, so its squared coordinate modulus is exactly1/(n−2), nonzero. Thus its zeros are EXACTLY {i,j} and all other n−2 coordinates have the stated flat magnitude.

Conversely, for any unordered pair {i,j}, i!=j, the cell at column i on transversal T_j is unique and lies off the reference row; likewise the cell at column j on T_i. They are distinct and are the ONLY cells with that zero pair. Every unordered zero pair therefore occurs exactly twice. Total reference-basis support is `n+n(n−1)(n−2)`, namely730 at n=10.

Any column block containing e_i has n−1 other vectors in e_i^perp. Their OTHER zeros are all distinct, because each transversal is met once. Indexing coordinates/vectors by those other zeros and rescaling by sqrt(n−2) gives an (n−1)-square matrix with zero diagonal, unit-modulus offdiagonal and Gram `(n−2)I`: a complex conference block. The analogous statement holds for a transversal block through e_i. These are necessary blocks of the SAME physical array; separate feasible blocks are not automatically glued.

## 3. At least fourteen seven-overlap nonsharing partners

At n=10 let x be any nonreference cell in column i and T_j, with zeros {i,j}. In T_i remove the cells in columns i,j. Exactly8 remain, each with zeros {i,k}, k!=i,j. None shares x's column or transversal, and at most one shares x's row. At least7 thus share no block with x.

Similarly, in column j remove the cells on T_i and T_j. Eight remain, with zeros {j,k}, k!=i,j; again at least7 share no block with x. The two resulting groups are disjoint: a zero pair sharing exactly i cannot also share exactly j. Thus EVERY such x has at least14 nonsharing partners in the SAME actual array. Each such pair has precisely three distinct zero labels in total and therefore exactly7 common support coordinates. Its squared physical inner product must be1/8. The proof works for EVERY Latin resolution L, not merely the tested cyclic one.

## 4. Gauge cancellation and the seven-term equation

Under the prime-power hypothesis, every nonzero coordinate has form

    psi_x(j) = lambda_x d_j zeta^(k_jx) / sqrt(8),

where the cell phases lambda_x and common coordinate phases d_j are arbitrary units and zeta is a primitive p^e-th root. For any actual nonsharing seven-overlap pair, multiplying coordinates in the inner product cancels each `d_j` and yields the COMMON unit prefactor `conj(lambda_x)lambda_y`; the seven remaining factors are arbitrary powers of zeta. Thus

    |<psi_x,psi_y>|² = |sum_(ell=1)^7 eta_ell|²/64,

and the required physical value1/8 is EXACTLY `|sum eta_ell|²=8`. No individual eta is assumed1, no phase of the sum is fixed, and the seven exponents need not be independent global array variables. Their global coupling could only add constraints; the local necessary equation already suffices for the prime-power no-go.

## 5. Complete prime-power lemma, including ALL powers of41

Let q=p^e, e>=1, zeta primitive q, and eta_l=zeta^(a_l). For d mod q let c_d count ORDERED pairs `(i,j)` with `a_i−a_j=d`; `sum c_d=49` and `c_0=sum_v m_v²`, where m_v are multiplicities. If the squared sum were8, the integer polynomial

    F(X)=(c_0−8)+sum_(d=1..q−1)c_d X^d

would satisfy F(zeta)=0 and F(1)=41.

The q-th cyclotomic polynomial is

    Phi_q(X)=sum_(j=0..p−1) X^(j p^(e−1)).

It is irreducible by Eisenstein after X->1+X: modulo p the transformed polynomial is `X^(p^(e−1)(p−1))`, and its constant term is p, not divisible by p². Thus Phi_q divides F over Q; since Phi_q is monic and F integral, ordinary long division gives an INTEGRAL quotient. Evaluating at1 proves p divides41. This rules out every p except41 without any numeric approximation or assumed relation among the seven phases.

For p=41 set h=41^(e−1), so q=41h and `Phi_q=1+X^h+...+X^(40h)`. Since deg F<41h, its integral quotient has degree<h. Consequently the41 coefficients of F in each class r modulo h are all the same integer b_r. For r!=0 they are counts and nonnegative; for r=0, `b_0=c_h>=0` (h is a nonzero difference class). Also `sum_r b_r=F(1)/41=1`.

Since `c_0=sum m_v²=7+2 sum binom(m_v,2)` is odd and at least7, `b_0=c_0−8` is nonnegative and odd, hence at least1. The sum1 forces b_0=1 and all other b_r=0, so c_0=9 and every NONZERO c_d is0 or1. But c_0=9 means exactly ONE repeated pair among the seven exponents. Its doubled value and any other distinct value generate the same nonzero difference in at least two ordered index pairs, contradicting c_d<=1. This works when e=1 (h=1) as well as every e>1. For the degenerate alphabet q=1 the squared sum is49, not8.

Together with §§2–4 this proves the claimed physical uniform-branch obstruction for every p,e,L and arbitrary admitted gauges. It does not establish that arbitrary complex vectors can be put into any prime-power alphabet.

## 6. Earlier real and specified two-phase no-gos

If n is even and a uniform physical array becomes real after arbitrary cell phases in one common ONB, choose the reference row as a real ONB and rotate it to the coordinate axes. Any two nonreference cells in one column have distinct second zero coordinates, hence share exactly n−3 nonzero coordinates. Each real coordinate product is `±1/(n−2)`. Since n−3 is odd, their sum cannot be zero, contradicting column orthogonality. The argument holds for every even n>=4 and every L; it excludes a common-real-basis lift only.

For the order10 two-phase branch put `zeta=omega²=(-3±i sqrt(7))/4`. In the SAME seven-overlap caller, arbitrary cell/coordinate gauges again contribute only a common unit prefactor. Let a,b,c be the counts of relative factors `1,zeta,conj(zeta)`; a+b+c=7. Then

    16 |a+b zeta+c conj(zeta)|²
      =[4a−3(b+c)]²+7(b−c)²
      =49(a−3)²+7(b−c)².

This is divisible by7, whereas a required squared sum8 would give128, not divisible by7. All 36 nonnegative triples are covered algebraically; there is no unannounced phase normalization. The ratio zeta is not a root of unity because `zeta+zeta^(-1)=−3/2` would then be a rational algebraic integer, necessarily an integer. Thus the two-phase theorem is a genuinely separate alphabet case, not already covered by the prime-power root result.

## 7. The prior complex local fragment and arbitrary-basis support caller

Et-Taoui's actual [arXiv:1409.4282v1](https://arxiv.org/html/1409.4282v1), §2, defines the odd-order finite-field conference construction and its order9 case with `Re(omega²)=−3/4`. I checked the explicit GF(9) specialization independently rather than importing its matrix as an assumed proof. With `F_3[t]/(t²+1)` and quadratic character chi, the matrix with offdiagonal entries `(1+chi(x−y)i sqrt(7))/8` and zero diagonal has exact UU*=I. Embed its nine columns in e0^perp and add the reference ONB; this gives two ONBs with one shared ray,19 distinct nonparallel rays, and each nonreference vector has two zero reference coordinates and eight squared overlaps1/8. It is a 19-ray fragment, NOT a100-ray array or evidence that the globally shared two-phase alphabet glues. Source/priority authenticity beyond this direct local comparison is not claimed.

For the support bound, let P_x be the actual rank-one projectors and let B be the incidence matrix of all 3n blocks. Since two different partitions' blocks meet once, their centered incidence subspaces are orthogonal. With J the all-one matrix, the ACTUAL uniform projector Gram is

    M=(n I−B^T B+J)/(n−2)
     = n P_1 + [n/(n−2)] P_U,

where U is orthogonal to the all-one line and the three centered block spaces. Define `(T X)_x=tr(P_x X)` on the REAL Hilbert space of Hermitian matrices. Then TT*=M. Since each row ONB sums to I, `sum_x P_x=nI`; T maps traceless X into the orthogonal complement of the all-one line. Hence

    sum_x tr(P_x X)^2 <= [n/(n−2)] tr(X²)

for every traceless Hermitian X. For any unit e take X=ee*−I/n; the constant and traceless outputs are orthogonal, yielding

    sum_x |<e,psi_x>|^4 <= 1+(n−1)/(n−2)=(2n−3)/(n−2),
    sum_x |<e,psi_x>|²=n.

Cauchy–Schwarz on the m(e) NONZERO coordinates gives `m(e)>=ceil(n²(n−2)/(2n−3))`. At n=10 this is48. Summing over any ONB gives at least480 nonzero vector entries; if q vectors have support>=5, at most `400+6q` entries are possible, so q>=14. Every use of M here is tied to an assumed actual physical array; formal PSD of M_* alone does not realize rank-one P_x.

## 8. Independent exact computations and their scope

Reviewer-owned `frontier-review-f53-rqls-check.py`, SHA256 **99e8ab6f7c4cd60c30c63c015b9b25b13370f636d690962e51e61b5219bb7cc2**,182 LF /6282 B, imports NO author program/data. Actual command:

    python3 -B frontier-review-f53-rqls-check.py

Observed exact integer outputs:

- Cyclotomic-polynomial division checked ALL seven-root multisets for q=2,3,4,5,6,7,8,9,10,12,15. Counts were respectively8,36,120,330,792,1716,3432,6435,11440,31824,116280; solution counts0 through q=10, then192 at12 and60 at15. This is finite corroboration, NOT the all-prime-power proof.
- The exact q=12 multiset `(0,0,0,3,3,4,8)` passes: it represents `1+1+i+i+(1+zeta_3+zeta_3²)=2+2i`, squared modulus8. Thus a single seven-overlap arithmetic obstruction cannot exclude every composite-order alphabet. It is NOT a full physical array.
- Exact integer partitions of7 give15 cases and only `(2,1,1,1,1,1)` has c_0=9, supporting the p=41 contradiction; the symbolic argument above covers arbitrary e, not a sampled e-list.
- All36 two-phase count triples were checked; none gives the forbidden target128. On an independently generated cyclic Latin incidence, all10 reference rows/900 nonreference cells had each zero pair twice and between14 and16 qualifying partners. Its FORMAL integer overlap matrix satisfied `B²=10B+56J` at all10000 entries; this does NOT construct a physical lift.
- Independent GF(9) arithmetic checked all81 entries of UU*=I and all171 pairwise nonparallel comparisons of the resulting19 rays. This is only two ONBs.

All claims beyond these stated finite computations rely on the written uniform proofs, not a numerical match. I did not rerun or independently adopt the author's finite-run receipts; their stated failed-first-check/corrected-scaling history remains as reported in the candidate.

## 9. Final decision and residual

**NO_SUBSTANTIVE_DEFECT AT EXACT STATED UNIFORM-BRANCH SCOPE — 0 FATAL / 0 MAJOR / 0 MINOR.** The all-prime-power result includes the p=41 exceptional route and all e>=1; the seven-summand reduction preserves arbitrary cell/coordinate gauges. The older real/two-phase proofs and support/caller distinctions are paid.

The seven-term composite counterexample, feasible isolated complex conference block, and scalar M_* PSD do not provide an actual uniform QLS. Conversely the arithmetic obstruction does not exclude composite/non-root phases or ANY nonuniform physical array. Full original order10 100-ray resolvability and novelty remain open at this review's scope. Same-harness written review plus finite exact checks only; no formal/kernel/human/independent-model acceptance.

**END OF COMPLETE f53 SCIENTIFIC REVIEW.**
