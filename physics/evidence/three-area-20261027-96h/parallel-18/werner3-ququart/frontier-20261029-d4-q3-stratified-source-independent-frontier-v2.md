# Source-independent stratified frontier for the original q3 target (consolidated v2)

**PhysicsResearch96h-2 / physics-1. WRITTEN, source-independent, all-variable; UNREVIEWED.** This self-contained packet supersedes `frontier-20261029-d4-q3-kyfan-dual-and-support-ladder-v1.md` (SHA256 `319e03163a67c5ab4bcf57ba1c013314c569e582cfcf137368e1f12169b27e48`, kept unchanged) as the single review candidate for this line. It adds a range-wise dual and an explicit **spread criterion**. The criterion proves strict positivity on explicit open subsets of the zero-leg classes.

It uses no source-certificate premise and introduces no source-conditional bound. It does **not** prove the full original inequality, the two-copy statement T_2, or the zero-leg classes Z_2, Z_3. It makes no literature-status, novelty or priority claim and no parent/f62/f153/human/family/formal/Lean/physical-operational acceptance claim. No selected target operator or numerical q value is evaluated.

## 1. Setting

For d≥2, n≥0 put `H_n=(C^d)^tensor n`. For any complex operator C on H_n define

`q_n(C)=Σ_(S⊆{1..n}) (−1/2)^|S| ||Tr_S C||HS²`,

with unnormalized partial traces and `Tr_∅ C=C`; for n=0, `q_0(c)=|c|²`. The original functional is q_3 at d=4.

**Target statements.** `T_n` (fixed d) says that `q_n(C)>=0` for all complex C of rank≤2. The original target is T_3 at d=4. T_0 is trivial. T_1 holds for every d, since `|Tr X|<=σ1+σ2<=sqrt2||X||` for rank≤2 X.

**Legs.** At site i, the output leg of C is the smallest E⊂C^d with `(P_E)_iC=C`; the input leg is the output leg of C†. A leg is k-supported if its dimension is ≤k. `Z_n` says that `q_n>=0` on all rank≤2 C whose 2n legs all have dimension ≥3.

## 2. Exact negative-space dual (d=4)

Write `vec C=Σ C_xy|x>⊗|y>`, regrouped by site. Put `Ω_i=Σ_j|j>⊗|j>` and `K_i=I−|Ω_i><Ω_i|/2`. Since `(<Ω_i|⊗I)vec C=vec(Tr_i C)`, we have the original identity `q_n(C)=<vec C,(⊗_iK_i)vec C>`. This identity is also recorded in `frontier-20261028-d4-positive-map-all-subsets-addendum-v1.md`, SHA256 `8cd42f794b79fec63fd8d607b41554891b3b6409d75efb7278ac29c962cbf500`.

At d=4, `||Ω_i||²=4`, so `K_i=I−2P_i` is a reflection, with `P_i=|Ω_i><Ω_i|/4`. Let `Π_−` be the sum of `⊗_(i∈T)P_i⊗_(i∉T)(I−P_i)` over odd T. Then

`q_n(C)=||C||HS²−2||P_odd C||HS²`,                                      (1)

where `P_odd` is the orthogonal projection onto `W_odd=vec^(−1)(ran Π_−)`. This is the span of the sector operators `I_T⊗Y_T`, where T is an odd set of sites and `Y_T∈⊗_(i∉T)sl_4`. Distinct sectors are Hilbert–Schmidt orthogonal. `||I_T⊗Y_T||²=4^|T|||Y_T||²`, and `dim W_odd=Σ_(|T| odd)15^(n−|T|)`, i.e. 30 for n=2 and 676 for n=3.

**Theorem 1 (vector dual).** At d=4, `T_n` holds iff `σ1(X)²+σ2(X)²<=||X||²/2` for every X∈W_odd. Explicitly:

- **n=2:** `X=A⊗I+I⊗B` with A,B∈sl_4; the condition is `σ1²+σ2²<=2(||A||²+||B||²)`.
- **n=3:** `X=cI+I_1⊗Y_23+I_2⊗Y_13+I_3⊗Y_12` with Y_jk∈sl_4⊗sl_4; the condition is `σ1²+σ2²<=32|c|²+2Σ||Y_jk||²`.

*Proof.* By (1), T_n is equivalent to `sup||P_odd C||²<=1/2` over unit rank≤2 C. We have `||P_odd C||=sup_(X∈W_odd,||X||=1)|<X,C>|`. For fixed X, the sup of `|<X,C>|²` over unit rank≤2 C equals `σ1(X)²+σ2(X)²`, by Eckart–Young/von Neumann. It is attained at `C=X_(2)/||X_(2)||`, where `X_(2)` is the two-term truncated singular value decomposition. Exchanging the two suprema proves the claim. ∎

**Two-sided use, unconditional.** If X∈W_odd is unit and `σ1²+σ2²>1/2`, then `C=X_(2)/||X_(2)||` has rank2 and `q_n(C)<=1−2(σ1²+σ2²)<0`. Conversely, under T_n, a nonzero rank≤2 C has `q_n(C)=0` iff `||P_odd C||²=||C||²/2`. In that case `X=P_odd C` is Ky-Fan-extremal and C/||C|| maximizes `|<X,·>|`.

**Single-sector instances.** If `X=I_i⊗Z`, its singular values are those of Z repeated four times, so `σ1²+σ2²=2σ1(Z)²<=||X||²/2`. Equality holds iff Z has rank1. The open content lies in cross-sector superpositions.

## 3. Range-wise dual and the explicit spread criterion (d=4)

For a two-dimensional subspace F of H_n with projection P_F, put

`κ(F)=sup_(0≠X∈W_odd) ||X P_F||²/||X||²`.

**Theorem 2 (range-wise dual).** T_n holds iff `κ(F)<=1/2` for every two-dimensional F. More precisely, for every C of rank≤2 and every two-dimensional F containing ran C† **or** ran C,

`q_n(C) >= (1−2κ(F))||C||²`.                                          (2)

*Proof.* If `ran C†⊂F`, then `C=CP_F` and `<X,C>=<XP_F,C>`, so `|<X,C>|<=||XP_F||·||C||`; hence `||P_odd C||²<=κ(F)||C||²`, and (1) gives (2). If `ran C⊂F`, use `<X,C>=<P_FX,C>` and `||P_FX||=||X†P_F||`, with W_odd closed under adjoints. For the converse, let some F have κ(F)>1/2 and take X attaining it (compactness); `C=XP_F` has rank≤2, satisfies `<X,C>=||XP_F||²`, and therefore `||P_odd C||²>=κ(F)||C||²>||C||²/2`, i.e. `q_n(C)<0`. ∎

κ(F) is invariant under arbitrary local unitaries `F→(U_1⊗…⊗U_n)F`, because conjugation by them preserves W_odd and its norm.

**Theorem 3 (spread criterion).** For two-dimensional F,

`κ(F) <= s(F) := Σ_(T odd) 4^(−|T|) ||Tr_T P_F||_∞`,                    (3)

where Tr_T traces out the sites in T and, for T={1..n}, `Tr_T P_F=2`. Consequently

`q_n(C) >= (1−2 s(F))||C||²`                                          (4)

for every rank≤2 C with ran C† ⊂F or ran C⊂F.

*Proof.* Decompose `X=Σ_T I_T⊗Y_T` into orthogonal sectors. For each sector,

`||(I_T⊗Y_T)P_F||²=Tr[(I_T⊗Y_T†Y_T)P_F]=Tr[Y_T†Y_T·Tr_T P_F]<=||Tr_T P_F||_∞||Y_T||²`.

The triangle inequality and Cauchy–Schwarz then give

`||XP_F|| <= Σ_T ||Tr_T P_F||_∞^(1/2)||Y_T|| <= (Σ_T 4^(−|T|)||Tr_T P_F||_∞)^(1/2)(Σ_T 4^|T|||Y_T||²)^(1/2)`.

The last factor is ||X||. ∎

**Explicit forms.**

- **n=2:** with `μ_j=||Tr_(3−j)P_F||_∞` (the local reduction at site j), `q_2(C)>=(1−(μ_1+μ_2)/2)||C||²`. So `μ_1+μ_2<=2` suffices.
- **n=3:** with `λ_i=||Tr_i P_F||_∞` (two-site reductions), `q_3(C)>=(15/16−(λ_1+λ_2+λ_3)/2)||C||²`. So `λ_1+λ_2+λ_3<=15/8` suffices, and strict inequality gives strict positivity.

**Maximally-correlated families (all-variable).**

- **n=2.** Let F lie in `D_2=span{|jj>}` and be spanned by orthonormal `f_r=Σ_jα_rj|jj>`. Both local reductions equal `Σ_j w_j|j><j|` with `w_j=|α_0j|²+|α_1j|²`. These are the diagonal entries of a rank2 projection, so `w_j<=1`. Hence **every** such F satisfies `μ_1+μ_2<=2`, and `q_2(C)>=(1−max_j w_j)||C||²>=0` for every rank≤2 C whose input or output range lies in D_2.
- **n=3.** Let F lie in `D_3=span{|jjj>}`. Every two-site reduction equals `Σ_j w_j|jj><jj|`, giving `q_3(C)>=(15/16−(3/2)max_j w_j)||C||²`. This is strictly positive whenever `max_j w_j<5/8`, for instance whenever all four `w_j=1/2`.

When all w_j are positive, F has local support4 at every site. Pairing such an input range with an output range of the same kind gives operators in which all legs have dimension4. Since (4) is strict there and s(F) is continuous in F, the criterion proves strict positivity on **nonempty open subsets of the zero-leg classes Z_2 and Z_3**. No numerical target value is computed; these are symbolic families with explicit reduced spectra.

## 4. Exact one-leg contraction identity

**Lemma 4 (factorization).** `q_(m+k)(C′⊗D)=q_m(C′)q_k(D)`, since subsets split and the coefficients factor. For a unit local vector u, `q_1(|u><u|)=1/2`.

**Lemma 5 (contraction identity, every d).** Let E⊂C^d be two-dimensional, with orthonormal bases {e_a} of E and {f_b} of E⊥, and Haar probability μ on S(E). For u∈S(E), let u⊥∈E be a unit vector orthogonal to u. Write `<α|C|β>_i=(<α|_i⊗I)C(|β>_i⊗I)`. If `(P_E)_iC=C`, then

`q_n(C)=3∫_(S(E)) q_(n−1)(<u|C|u⊥>_i)dμ(u)+Σ_(a,b) q_(n−1)(<e_a|C|f_b>_i)`.   (5)

If `C(P_E)_i=C`, then

`q_n(C)=3∫ q_(n−1)(<u⊥|C|u>_i)dμ(u)+Σ_(a,b) q_(n−1)(<f_b|C|e_a>_i)`.        (6)

*Proof.* In the output case, K_i may be replaced by `P_E⊗I−|Ω_E><Ω_E|/2`, with `Ω_E=Σ_a e_a⊗ē_a`. Two Haar moments, `∫|u><u|^tensor2=(P_E⊗P_E+F_E)/6` and its partial transpose `∫|u><u|⊗|ū><ū|=(P_E⊗P̄_E+|Ω_E><Ω_E|)/6`, together with `∫|u><u|=P_E/2` and `|ū⊥><ū⊥|=P̄_E−|ū><ū|`, give

`P_E⊗I−|Ω_E><Ω_E|/2=3∫|u><u|⊗|ū⊥><ū⊥|dμ+P_E⊗(I−P̄_E)`.

For a product term `|α><α|⊗|β̄><β̄|`, direct index contraction gives `(<α|⊗<β̄|⊗I)vec C=vec(<α|C|β>_i)`, and its contribution is `q_(n−1)(<α|C|β>_i)`. The input case is the same with `I⊗P̄_E−|Ω_E><Ω_E|/2=3∫|u⊥><u⊥|⊗|ū><ū|+(I−P_E)⊗P̄_E`. Legs of dimension0 or1 are covered by extending E. ∎

Contraction does not increase rank, and it preserves leg inclusions at the other sites.

## 5. The support ladder and its consequences

**Theorem 6 (ladder equivalence, every d).** For n≥s≥0, any s distinct sites L and a chosen leg at each, the following are equivalent:

(a) `q_n>=0` on all rank≤2 C whose chosen legs at L are 2-supported;
(b) the same with 1-supported legs;
(c) `T_(n−s)`.

For s=n, (a) holds for C of every rank.

*Proof.* (c)⇒(a): iterate Lemma 5 over L; the result is a positive-weight integral of values `q_(n−s)(X)` with rank X≤2, and for s=n each X is a scalar with `q_0=|X|²`. (a)⇒(b) is immediate. (b)⇒(c): apply Lemma 4 to `C′⊗⊗_(i∈L)|u_i><u_i|`. ∎

**Corollaries.**

1. `T_n⇒T_m` for m≤n. In particular the original T_3 implies the full two-copy statement T_2 at d=4, i.e. the inequality of Theorem 1 for every `A⊗I+I⊗B`.
2. At d=4, n=3, positivity on the stratum of operators with at least one 2-supported leg is **equivalent** to T_2.
3. For every n,d, if n−1 distinct sites carry 2-supported legs (orientation chosen per site), then `q_n>=0` on rank≤2 C. If every site carries one, this holds at any rank. This generalizes the two-leg theorem of `frontier-20261028-d4-source-independent-local-support-consolidated-v1.md`, SHA256 `0ccc096a2eb7309bb6398872660cc24ad8213119d88eb917110fec8ab238c01c`.
4. `T_n⇔T_(n−1)∧Z_n`, hence `T_n⇔Z_2∧…∧Z_n`. For the original problem, `T_3⇔Z_2∧Z_3` at d=4.
5. Assume T_(n−s). Then in the s-leg class, `q_n(C)=0` iff every contraction occurring in the iterated identities has `q_(n−s)=0`.
6. **Transfer.** The identities (5)/(6) carry any sufficient criterion for q_(n−s) into the s-leg class, contraction by contraction. For example, take a 2-supported leg of C at site3 (d=4, n=3). If every contraction X in (5)/(6) satisfies either the n=2 spread condition `μ_1(X)+μ_2(X)<=2` or has its own 2-supported leg, then `q_3(C)>=0`.

Corollary 4 is consistent with the earlier dense-boundary lemma `frontier-20261028-d4-dense-local-support-boundary-extension-v1.md`, SHA256 `4e6fe20463ddba8ebf32fba9cfd9139d058837b05a618732cc0b85eb91bffff3`: positivity on the open dense full-support set already implies T_3, and hence T_2.

## 6. Unconditional coverage now, and the exact remainder

The following are proved source-independently in WRITTEN form, all unreviewed:

- rank≤1;
- every rank≤2 C with two distinct 2-supported legs;
- every C with a 2-supported leg at all three sites, at any rank;
- every rank≤2 C whose input **or** output range F has `λ_1+λ_2+λ_3<=15/8`, with the quantitative margin (4); this includes open subsets of Z_3;
- the explicit two-product-projector/product-rank-one/support families in the earlier consolidated packet.

For n=2, the analogous coverage holds with `μ_1+μ_2<=2`, including every range inside D_2.

**The remainder.** Rank-two operators that have neither two supported legs nor a spread input/output range. This contains the one-leg stratum, which is exactly equivalent to T_2, and its neighbourhood in Z_3. Equivalently, it is the cross-sector Ky Fan inequality of Theorem 1, or `κ(F)<=1/2` for every concentrated range F. Tracelessness of the Y_T is essential, not merely a normalization. On the larger space of all `A⊗I+I⊗B` with A, B not required to be traceless, the n=2 Ky Fan inequality is false. For example, `A=|0><0|`, `B=2|0><0|` give singular values 3, 2 (three times), 1 (three times) and 0 (nine times), so `σ1²+σ2²=13>12=||X||²/2`. In (3), tracelessness enters only through the orthogonality of the sectors. This is a remark about the hypothesis, not an evaluation of q on a target operator.

## 7. Provenance and nonclaims

The proofs use only:

- the original trace functional and vectorization;
- elementary Haar second moments;
- rank monotonicity under contraction;
- Eckart–Young/von Neumann;
- Cauchy–Schwarz and partial-trace operator-norm bounds.

No source premise, executable checker, selected target value, or elected HELD/ZERO/NONINPUT episode, consumer or guidance is used. The separate source-conditional packets are not changed. Historical process findings and frozen f153/f62 boundaries are unchanged. No claim is made about the literature status of T_2, Z_2 or Z_3.
