# Non-packet controls: maximal reflection identities, their completion obstruction, and a two-rotation selector

Actual returned clock before creation: **Sun Oct 25 04:24:32 PDT 2026**. MathOlson-2, math-2. **WRITTEN candidate controls, not independently reviewed, not formally/kernel verified, novelty unclear.** These are the first representation explored on resumption, not premises of `proof-FIXED-ROTATION-DOUBLE-BOX-BAND-CLOSURE-v1.md`. No scientific arithmetic checks of these theorems were run. The corrected HOLD and the separate six-call exploratory disclosure remain binding.

## 1. Transporting optional occurrences through a fixed identity

For an actual selected subset S whose ordered product is 1, let P_r be the product of selected S occurrences strictly preceding an unselected occurrence h_r. Define

    tau_r=P_r*h_r*P_r^(-1).

For any increasing list T of further selected occurrences, exact telescoping gives

    product of S union T in original order
      =(product_(r in T increasing) tau_r)*(product S)
      =product_(r in T increasing) tau_r.                 (T)

The fixed prefixes cancel to reproduce precisely the selected stretches between the new occurrences. This does not commute any actual occurrence through a reflection. It is a group identity in the actual original order.

If all S occurrences and optional occurrences under discussion are reflections in D_(2p), each tau_r is one of the p actual group involutions sigma_a. If two optional tau's agree, adding those two named occurrences to S preserves identity and increases selected length by two.

**Theorem MI.** Every reflection list of length 3p-2 has an identity selection of exactly 2p-2 reflections. If it has no identity2p selection, then for EVERY such identity S of length 2p-2 the p transported complementary reflections are pairwise distinct, hence are a permutation of all sigma_a, a in F_p.

**Proof.** Start with the empty identity selection. As long as its even size is at most 2p-4, at least p+2 unselected reflections remain. Their transported involutions take only p possible values. Two agree; add their two actual occurrences using (T). After p-1 additions the selected size is exactly 2p-2. For any identity S of that size, exactly p reflections remain. A repeated transported value would extend S to identity2p, contradicting the stated avoidance. Therefore all p values are distinct. QED.

This theorem uses only pigeonhole and group transport, not a classical Davenport constant or the raw possible-switch matching.

For an actual rotation rho_x outside a reflection-only S, its transport is

    P_r*rho_x*P_r^(-1)=rho_(epsilon_S(r)*x),
    epsilon_S(r)=(-1)^(number of S reflections before r).

Thus adding TWO rotations to an identity S of size 2p-2 succeeds exactly when their transported coordinates sum to zero. This is an actual selector allowing any number of endpoints of each old matched pair.

## 2. A complete uniform obstruction to the stronger MI2 completion claim

The tempting stronger claim MI2 would say: in every REF-avoiding lower-branch band word, SOME reflection identity S of length 2p-2 has two transported inverse rotations. This is false even though all such words below have an explicit two-rotation identity with a NONIDENTITY reflection part.

Fix any prime p>=11, choose c!=0, and choose b!=0 with b not in {c,-c}. Use the actual word

    w_(p,b,c) = rho_c sigma0^p rho_b sigma0^(p-1)
                 rho_c sigma1 rho_c sigma2 ... rho_c sigma_(p-1).   (W)

There is one initial rho_c and one rho_c immediately before each of the p-1 displayed nonzero reflections. Hence there are p occurrences of rho_c and one rho_b. The reflection list is

    C_p=sigma0^(2p-1) sigma1 ... sigma_(p-1).

All rotations are nonzero; every cyclic reflection gap has at most one rotation; R=p+1, F=3p-2 and N=4p-1.

### 2.1 REF failure and every possible S

For ANY even-length reflection selection from C_p that uses t>=1 nonzero labels, write their ordinary integer representatives as

    1<=d_1<...<d_t<=p-1.

Every selected zero precedes these labels. Direct alternating multiplication gives coordinate -L, where

    L=(d_2-d_1)+(d_4-d_3)+...+(d_t-d_(t-1))       if t even,
    L=d_1+(d_3-d_2)+...+(d_t-d_(t-1))            if t odd.

In either case 1<=L<=p-1: the positive disjoint integer intervals lie in [0,p-1]. Thus no such selection has identity product.

There are only 2p-1 zero reflections, so an identity2p reflection-only selection is impossible. Every reflection identity of length 2p-2 must consist of 2p-2 of those zero occurrences, omitting exactly one. This re-proves the previously exposed C_p property rather than importing a numerical diagnostic.

### 2.2 Actual lower raw graph and unique maximum matching

The p cyclic gaps outside the long zero block are all occupied by rho_c. Their reflection vertices form the single path

    last zero, sigma1, sigma2, ..., sigma_(p-1), first zero,

with p+1 vertices. The internal rho_b joins zero occurrences p and p+1, which are distinct from the first and last zero vertices. It contributes a separate P2. Every other reflection vertex is isolated: all remaining gaps are empty between equal zeros.

Therefore the raw graph is exactly

    P_(p+1) disjoint union P2 disjoint union (2p-5)P1.

Both nontrivial paths have an even number of vertices and unique perfect matchings, by induction from an endpoint. The unique maximum matching has size

    (p+1)/2+1=(p+3)/2 <=p-3,     p>=11.

Thus (W) is genuinely in the lower raw-matching branch, not the critical branch.

### 2.3 Failure for EVERY S in MI2

For any possible reflection identity S of size 2p-2, all selected reflections are zero and their total count is even. The initial rho_c is before all of them, and every other rho_c is after all of them. All p such occurrences therefore have transported value c.

The single internal rho_b has transported value either b or -b. Two transported c values do not sum to zero because 2c!=0. A transported c and the one transported b value do not sum to zero because b not in {c,-c}. There are not two b occurrences. Hence NO pair of transported rotations is inverse for ANY possible S.

This disproves MI2 with all S and all rotation pairs quantified, not only one chosen maximal identity.

### 2.4 Explicit actual two-rotation solution nevertheless

Let j=b+c in F_p, represented by its unique integer in {1,...,p-1}; it is nonzero because b!=-c. Select:

- the actual initial rho_c and the actual rho_b;
- any p-1 zeros before rho_b and any p-2 zeros after it;
- the actual tail occurrence sigma_j;
- no other occurrence.

There are exactly 2+(p-1)+(p-2)+1=2p selected positions. Their actual ordered product is

    rho_c sigma0^(p-1) rho_b sigma0^(p-2) sigma_j
      =rho_(c+b) sigma0 sigma_j
      =rho_(c+b-j)=1.

The reflection part itself has coordinate -j!=0. This is exactly why the selector is not an MI2 completion. For p>=11 this actual selection also cannot take one endpoint from every edge of the displayed unique maximum matching: its P_(p+1) component has at least six matched edges but the selection uses at most its two zero endpoints and one nonzero reflection.

The family is explicitly SEL-covered by its 2p-1 zeros and internal sigma0 rho_b sigma0 triple. It is NOT a word satisfying the entire old residual; it does NOT refute L_RES or the packet-only residual variant. Its purpose is to reject the stronger MI2 representation before using it as a universal selector.

## 3. Stronger positive control: exactly TWO rotations suffice for every singleton-gap C_p insertion

The old insertion theorem covered every insertion of p+1 arbitrary rotations into C_p using P/SEL. Here is a direct stronger rotation-count result at singleton gaps. It remains an already removed reflection-family control, not the actual residual.

**Theorem C2.** Suppose the reflection list is C_p, exactly p+1 arbitrary rotations are inserted, and every cyclic reflection gap has at most one rotation. Then an identity2p selection exists using exactly TWO rotations, at most TWO nonzero reflection occurrences, and the remaining selected reflections all zero.

**Proof.** There are p gaps outside the zero block and 2p-2 internal zero-to-zero gaps. Hence at least one internal gap has a rotation rho_b.

First suppose an outside gap also has a rotation rho_c. Choose one such internal b and one outside c. The chosen b splits the 2p-1 zeros into L and R positive counts. If we select t=0,1 or2 tail reflections, we need C=2p-2-t zeros. The feasible integer counts l of selected zeros before b are

    max(0,C-R)<=l<=min(L,C).

This interval contains two consecutive integers: L,R>=1 and C is obtained by omitting t+1 of the 2p-1 zeros, with 1<=t+1<=3. Thus the transported sign epsilon of b can be prescribed either +1 or -1 while keeping the required total zero count. For t=0 this is exactly the choice of which side contains the one omitted zero; for t=1,2 there is at least the same parity freedom.

If b is c or -c, choose t=0 and epsilon so c+epsilon*b=0. The selected zero reflection count is even, so the outside c has sign +1. This gives the desired identity. This includes b=c=0.

Otherwise both c+b and c-b are nonzero. Let A be their set of ordinary representatives in {1,...,p-1}, and let B=-A in F_p, again represented there. Let a in {0,...,p-1} label the outside gap: it is after sigma_a and before sigma_(a+1), with a=0 meaning before sigma1 and a=p-1 meaning the cyclic gap after sigma_(p-1).

With one chosen tail label j the reflection coordinate is -j. The outside rotation has sign +1 if j<=a, and -1 if j>a. Consequently a one-tail solution exists if either

    some j in A has j<=a,  or some j in B has j>a.

Use the corresponding sign epsilon of b. If neither condition holds, then

    A subset {a+1,...,p-1},
    B subset {1,...,a}.

Since both sets are nonempty, 1<=a<=p-2. Choose d in B; then 1<=d<=a. Select the two tail reflections with labels

    j_1=a-d+1,  j_2=a+1.

They are valid distinct labels in {1,...,p-1}, their difference is d, and the outside rotation lies between them. The reflection coordinate is -d and the outside rotation has sign -1. As d belongs to B={-c+b,-c-b}, choose epsilon with d=epsilon*b-c. The total coordinate is -d+epsilon*b-c=0. The zero allocation already provides that epsilon and exactly 2p-4 zeros, so total size remains 2p.

It remains to handle the case that ALL p+1 rotations lie in internal zero gaps. Partition their values into the opposite classes {x,-x}, with zero its own class. There are only (p+1)/2 classes, so two actual rotations have equal opposite classes. They lie in distinct gaps. The two cyclic arcs between those gap positions each contain a zero reflection. Select these two rotations and 2p-2 of the 2p-1 zeros, omitting one zero in whichever arc gives the relative prefix sign that makes the transported rotation values inverse. Omitting on the other nonempty arc flips that relative sign. Both values zero also work. All selected reflection coordinates vanish, and the total selected size is 2p.

All products are calculated in the actual cyclic order. The same named subset returns to original order by the identity/conjugation argument already used in the main double-box packet. This proves C2. QED.

## 4. Relation to the assigned remaining gap

MI provides a new maximum-reflection-identity representation. MI2 is uniformly false on genuine REF-avoiding lower-graph words, but those words are SEL-covered. C2 is a uniform explicit actual selector on that old removed family and allows nonidentity reflection parts. Neither control is advertised as solving the old-caller-avoiding residual.

The separate double-box packet supplies the candidate full band closure without MI2, C2 or a maximum-matching restriction. These controls record the abandoned completion mechanism, so it is not silently recycled as the justification of the final candidate.
