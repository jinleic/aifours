# B2 span13 — the discrete two-channel coherence plane is excluded, candidate v1

Actual clock observed before this manuscript: **2026-10-23T14:44:16-0700**. AUTHOR-WRITTEN CANDIDATE, no separate/parent acceptance. This is non-load-bearing continuation; `conditional-full-assembly-v1.md` remains unchanged. No scientific program, enumeration, numerical check, solver, CLI or nested agent.

## 1. Exact remaining branch

Assume a full physical five-MOQLS(8) family with the literal P1-B2 axes in `proof-B2-span13-v1.md`, and square1's full real projector span S has dimension13. Its axis span has dimension11. Put B=span(e4,e5), and define the real-linear B/complement cross map

    C(P)=P_B P P_(B-perp).

For a cell vector v, C(vv*)=v_B v_(B-perp)* is a complex2-by6 matrix of rank1 when both components are nonzero, and zero otherwise. Since C annihilates the11-dimensional axis span,

    dim_R C(S)<=2.

Dimension0 would globally isolate B. Dimension1 fixes both physical factor rays of every nonzero cross outer product and gives the one-channel case. Both were excluded by the sector and one-channel arguments, with their candidate trust boundary. Hence the branch under study has dim_R C(S)=2.

Choose two actual mixed cell images X_1,X_2 spanning this real plane, and write them as nonzero multiples of b_1 c_1* and b_2 c_2*, with unit b_j in B and c_j in B-perp.

**Claim DTC.** It is impossible that BOTH b_1,b_2 are complex-linearly independent and c_1,c_2 are complex-linearly independent.

Thus a surviving two-real-dimensional plane must have a common physical B factor or a common physical complement factor. This is a necessary reduction of a genuine continuous branch, not its complete exclusion.

## 2. Why the independent-factor plane has exactly two real channels

If both factor pairs are independent, any nontrivial combination alpha X_1+beta X_2 with alpha beta!=0 has rank2, even for complex alpha,beta. To see this, restrict to the two-dimensional column/row factor spaces and choose their independent vectors as bases. The combination becomes an invertible left/right change of bases of a diagonal2-by2 matrix with nonzero diagonal coefficients.

Every actual nonzero cell image C(vv*) has rank1 and is a REAL combination of X_1,X_2. It therefore lies on exactly one of the real lines R X_1 or R X_2. Its B component is parallel to b_j and its complement component to c_j. Every mixed cell is consequently in one of the fixed two-spaces

    F_j=span(b_j,c_j),       j=1,2,

with both components nonzero. All remaining cells are B-pure or B-perp. Both channels occur, because X_1 and X_2 came from actual independent cell images.

In an actual row, the cross outer products sum to zero. The two real channel directions are independent, so their coefficient sums vanish separately. If channel j occurs in a line, it therefore occurs at least twice. Its vectors are orthogonal in a two-space, so there are exactly two, forming an ONB of F_j. The same holds for every column.

Let k_j be the number of rows containing channel j. There are2k_j channel-j cells and therefore k_j corresponding columns. Along these cells, square1 has a two-regular board of ONB pairs in F_j.

The elementary transition-capacity fact used below is: two disjoint ray-occurrence matchings on the same m actual rows and columns, which are ONBs of the same m-space in EACH of the four other squares, require m>=6. For a fixed first-matching cell, the transition row has TWO distinct row/column-forced zeros. FOUR nonempty supports must be disjoint by product orthogonality, giving4<=m-2. All subspaces are square-specific.

## 3. Nonorthogonal B directions

Assume <b_1,b_2>!=0. Since the factors are independent, their unordered B-ray-pairs beta_j={b_j,b_j-perp} are different. A row cannot contain both channels: two ONBs of F_1,F_2 in the same row would make those subspaces orthogonal, which would force b_1 perpendicular to b_2. Thus the channel row sets are disjoint; their column sets are likewise disjoint.

A row containing channel j has two mixed F_j-vectors and exactly one B-pure b_j-perp vector. Every nonmixed row has exactly two B-pure vectors giving some orthonormal ray-pair alpha in B. Let m_alpha count such nonmixed rows. Then

    k_1+k_2+sum_alpha m_alpha=8.

For each OTHER square, span its entries on the pure-B ray-pair classes. Different classes have all cross overlaps nonzero in square1, so these spans are orthogonal. Class beta_j has m_beta_j copies of b_j and m_beta_j+k_j copies of b_j-perp, yielding dimension at least m_beta_j+k_j; other classes have lower bound m_alpha. These lower bounds add to8, forcing every one tight.

Mixed channel-j entries are orthogonal to every other pure-B class, and to the pure-b_j entries in beta_j. Hence in each other square they lie in a k_j-dimensional subspace W_{s,j} obtained from the saturated beta_j span by removing its m_beta_j-dimensional pure-b_j span.

Group the channel-j board by orthonormal ray-pairs in F_j. The pair-class row sizes ell_a sum to k_j; each repeated ray forces dimension at least ell_a, while different pair classes give orthogonal spans in W_{s,j}. Saturation makes their two ray matchings bases of the SAME ell_a-space. The transition-capacity fact gives ell_a>=6, hence k_j>=6.

Both channels occur, and their row sets are disjoint. Therefore8>=k_1+k_2>=12, contradiction.

## 4. Orthogonal B directions

Now assume b_1 perpendicular to b_2, so beta_1=beta_2=beta. Rows may contain both channels only if F_1 and F_2 are orthogonal; no such coexistence is assumed. Let h be the number of rows containing both channels. A row with only channel j has one B-pure ray on b_(3-j). A row with both has no B-pure vectors. A nonmixed row has two B-pure vectors giving beta or another pair alpha.

Let m_beta count the nonmixed beta rows, and m_alpha the nonmixed alpha rows. The actual disjoint row count is

    8=m_beta+sum_alpha m_alpha+k_1+k_2-h.                  (1)

There is at least one alpha. Indeed the actual B-axis ray-pairs{e4,e5} and{q^4,q^5} are different, so beta cannot contain all those pure-B rays. Any pure-B ray outside beta lies in a nonmixed row and column and therefore in such an alpha class.

Fix channel j and one other square s. Its entries on each alpha class span K_{s,alpha} of dimension at least m_alpha; different alpha spans are orthogonal. Pure b_j occurs at

    m_beta+k_(3-j)-h

cells: once per nonmixed beta row and once per row with only the OTHER channel. Their entries in square s are orthonormal, by the repeated square1 ray, and span L_{s,j} of exactly that dimension. L_{s,j} is orthogonal to all K_{s,alpha}, because b_j overlaps both rays of every alpha different from beta.

Every channel-j entry of square s is orthogonal to all K_{s,alpha} and to L_{s,j}. Thus its available ambient subspace has dimension at most

    8-sum_alpha m_alpha-(m_beta+k_(3-j)-h)=k_j,             (2)

by(1).

On the other hand, grouping its channel-j board by F_j ray-pairs forces span dimension at least k_j: class sizes sum to k_j and different classes give orthogonal spans in square s. Therefore equality holds in(2), including dim K_{s,alpha}=m_alpha for EVERY alpha. Both alpha ray-occurrence matchings are hence ONBs of the same m_alpha-space in each other square. The transition-capacity fact gives

    m_alpha>=6.

The same equality makes each channel-j pair class complete in its ell-space, giving ell>=6 and therefore k_j>=6. Alpha rows are nonmixed and disjoint from channel-j rows. For any actual alpha and either nonempty channel j,

    8>=m_alpha+k_j>=12,

a contradiction. This handles overlap h without double-counting rows or assuming h has the same value for columns. Only each separate k_j equals its column count; the beta ray counts came from the displayed actual row partition.

Sections3–4 prove Claim DTC.

## 5. Exact surviving coherence family

If two actual independent rank-one image generators share neither factor, Claim DTC excludes the full configuration. Otherwise their real span has a common B factor b or a common complement factor c, and every actual mixed image shares it. If both factors were common, all mixed cell vectors would lie in one fixed two-space; the one-channel theorem already excludes that case.

What remains can therefore contain a genuine real two-plane of complement directions with fixed b, or a real two-plane of B directions with fixed c. These can support a three-dimensional rank-one cone. They must NOT be replaced by just two discrete rays or by real signs without proof. This manuscript supplies no exclusion or exact physical construction for that shared-factor case.

The result is conditional on the earlier written isolated/one-channel steps only for removing cross-image dimensions0/1. Claim DTC itself is a direct physical ONB/product-orthogonality argument under its explicit two-channel hypothesis. No GB formula, old K closure, T16 exhaustion or computational certificate is a mathematical premise. The primary full target and all original UNKNOWN/HOLD/gate qualifications remain unchanged.
