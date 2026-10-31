# No prime-power relative-phase alphabet for the Weyl/MUB construction

**WRITTEN + EXACT INTEGER/CYCLOTOMIC-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at completed exact symmetry checks: **Wed Oct 28 19:02:17 PDT 2026**. This closes BOTH the affine and all100 non-affine fifth-root ratio cases left open in `frontier-20261028-character-ratio-obstruction-v1.md` SHA **ae331153fb2b082ab50382e12531c2766b288e4cc654aacca11b86cdaf4036b8**. It remains a restricted Weyl/diagonal-transversal result, not an unrestricted QLS10 no-go.

## 1. Statement

Take the explicit triple of MUBs `I10,F10,D10 F10` and CRT decomposition from `frontier-20261028-weyl-mub-qls-equivalence-v1.md` SHA **f063984a0ac5ff0a51e064b8e32eb901ba2e7edaff6e2667e0f6c7f47ad43a5d**. A common unbiased unit vector must have

`phi=(|0> tensor a+|1> tensor b)/sqrt(2)` with `a,b in C5` flat and orthonormal.

**Claim:** there is NO common unbiased phi for which all five ratios `b_t/a_t` lie in a single coset `lambda*mu_(p^e)` of roots of unity of ANY prime-power order p^e. The common factor lambda may be an arbitrary unit complex phase. Consequently any solution of this Weyl-orbit construction must have relative phases outside EVERY such prime-power coset. No rational-phase, root-of-unity, circulant-general or WLOG assumption is made for a general original 1-RQLS.

## 2. Reduction to a fifth-root permutation

Orthogonality gives `sum_t b_t/a_t=0`, since `|a_t|²=1/5`. Suppose the five ratios lie in lambda*mu_(p^e). Divide by lambda and form `P(x)=sum_t x^(k_t)`, with exponents 0<=k_t<p^e. If P vanishes at a primitive p^e-th root, it is divisible in Z[x] by

`Phi_(p^e)(x)=1+x^(p^(e-1))+...+x^((p-1)p^(e-1))`.

The quotient has degree less than p^(e-1); each coefficient in a fixed residue class mod p^(e-1) is therefore repeated p times. In particular p divides the total5. Thus p=5, and the five ratios are one coset of the FIVE distinct fifth roots. There is a permutation sigma∈S5 with

`b_t=lambda omega^sigma(t) a_t`, omega=exp(2*pi*i/5).      (1)

If sigma is affine, (1) is a nontrivial character ratio and the odd-cycle proof in the cited character-ratio packet excludes the common vector. It remains to exclude ALL non-affine permutations.

## 3. Triple-preserving symmetries reduce to one non-affine permutation

The 5D bases from the CRT decomposition are I5, `U_(t,j)=omega^(3tj)/sqrt(5)`, and `V=D5 U` with `D5_tt=omega^(4t²)`. For any c∈F5^*, d∈F5, define the common monomial unitary

`(T v)_t=omega^(eta t²) v_(c t+d)`,

where eta=0 if c²=1 and eta=4 if c²=4 mod5. T preserves the standard basis and permutes the two other bases up to column phases/permutations: it sends a basis with quadratic exponent q∈{0,4} to one with exponent `eta+q c²`, which again runs over {0,4}. The linear exponent maps bijectively because c!=0. Thus T preserves the condition that a rank-two projection has diagonal2/5 in all THREE bases.

Applying T to both a,b replaces sigma(t) by `sigma(c t+d)`. Swapping a,b negates sigma, and changing b by a global fifth-root phase adds a constant. Therefore the projection feasibility problem is invariant under

`sigma(t) -> epsilon*sigma(c t+d)+b`, epsilon∈{+1,-1}.      (2)

All100 non-affine permutations are one orbit of (2), represented by

`sigma0=(0,1,2,4,3)`.

This is a finite exact claim: `frontier-20261028-nonaffine-fifthroot-cert-v1.py`, SHA **a568e81fbd5ea800aaa18d9951e102edc37bb74f80a8eb572c649195d648683c**, checks that the200 parameter choices yield exactly the100 non-affine permutations (stabilizer `(1,1,0,0),(-1,-1,2,2)`). Independently, `frontier-20261028-mub5-symmetry-check-v1.py`, SHA **cb340e2351b4049e9fd672b2ef03f4154d564ce1940bbaafc1929c5f937f9f34**, checks all1000 coordinate exponent identities establishing the claimed basis preservation. Thus it suffices to rule out sigma0.

## 4. A single-gap spectral obstruction for sigma0

Let `P=|a><a|+|b><b|` be the rank-two projector required by common unbiasedness. Write `p_t=sqrt(5)*a_t`, so |p_t|=1. Under sigma0,

`y_t=5 P_(t+1,t)=p_(t+1) conjugate(p_t) (1+omega^(sigma0(t+1)-sigma0(t)))`.

The difference pattern is `(1,1,2,4,2)` mod5. Flat diagonal of `U† P U` forces `sum_t y_t=0`. Flat diagonal of `V† P V` forces `sum_t y_t omega^(2t)=0`: the `(t+1,t)` entry of `D5† P D5` is `omega^(2t+1) P_(t+1,t)`, and the common omega factor is irrelevant. Hence the Fourier expansion of y has support only at indices {1,2,4}:

`y_t=c1 omega^t+c2 omega^(2t)+c4 omega^(4t)`.             (3)

Let `d_k=(1/5)sum_t |y_t|² omega^(-k t)`. Comparing (3) gives

`d0=|c1|²+|c2|²+|c4|²`,
`d1=c2 conjugate(c1)`,
`d2=c1 conjugate(c4)+c4 conjugate(c2)`.                       (4)

The phases of p_t cancel from |y_t|. Three positions have squared modulus `(3+sqrt(5))/2` and the other two `(3-sqrt(5))/2`. Direct fifth-root arithmetic yields

`d0=(15+sqrt(5))/10 < 2`,
`|d1|=(5-sqrt(5))/10`, `|d2|=(5+sqrt(5))/10`,
`d1*d2²=-(5+sqrt(5))/50 < 0`.                                (5)

For an explicit check, the small positions are t=2,4; thus `d1=-(sqrt(5)/5)(omega³+omega)` and `d2=-(sqrt(5)/5)(omega+omega²)`, and

`(omega³+omega)(omega+omega²)²=1+omega+omega^4=(1+sqrt(5))/2`.

The exact checker above verifies all identities modulo `Phi5` without floating arithmetic.

Write `c1=p exp(i alpha)`, `c2=q exp(i beta)`, `c4=r exp(i gamma)` with p,q,r>0, and `phi=beta-alpha`. Equation (5) says `d2 exp(i phi/2)` is purely imaginary. By (4), its real part is

`r*(p+q)*cos((alpha+beta)/2-gamma)`.

It follows that this cosine vanishes, and hence `|d2|=r*|p-q|`, while `|d1|=p q`. By the arithmetic–geometric mean inequality,

`d0=p²+q²+r² >= 2 p q + 2 r|p-q|
                       =2(|d1|+|d2|)=2`,

contradicting (5). So even the necessary flat-diagonal projection P does not exist for sigma0. By §3, none exists for ANY non-affine sigma. Together with the affine odd-cycle obstruction, §1 follows for every prime-power root coset.

## 5. Scope, imports, and remaining gap

The flat-projector counterexample from `frontier-20261028-mub-triple-rank2-reduction-v1.md` is not contradicted: its ratio is an AFFINE fifth-root permutation, for which the flat P exists but the X/Y cross gates fail. The present spectral argument excludes only NON-affine fifth-root ratios at the P-flatness stage.

This proof uses the written CRT/MUB equivalence and the odd-cycle character-ratio lemma cited above, plus the fully stated finite orbit and cyclotomic arithmetic checks. Neither external model nor numerical optimizer is a premise. It does NOT exclude composite-order ratio alphabets, arbitrary continuous phases, non-diagonal Weyl resolutions, noncirculant/nonproduct QLSs, or the general original target. Full independent review is required before adopting the result.
