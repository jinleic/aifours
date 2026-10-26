# Candidate v1 — exact written exclusion of the e=0 all-three deficit profile

Observed immediately before creation: `2026-10-23T14:50:31-0700`. PhysicsAME46, physics-6. This is resumed OWN primary research after returning both parent-assigned MOQLS reviews. Written CANDIDATE / PARTIAL; no program, solver, enumeration, numerical tensor, CLI or nested agent.

## Theorem and exact delta

**Candidate theorem.** No AME(4,6), with arbitrary complex coefficients in any product orthonormal basis, has e=0 and deficit profile

    {3,3,3,3}⁴.

Here A=6ψ, T={x:|A_x|=1}, N=supp A\T, d_(i,a)=6−|{x∈T:x_i=a}|, and e=|supp A|−(72−|T|). This profile has h=12,t=24 and therefore support48 at e=0.

This is a full exclusion of this four-thick-axis profile, not merely the coherent-matching ansatz ruled out by `officer-holonomy-v1.md` (SHA256 `8be8781d6d0f4a4b32e0ca6a108b028282431c5c42432368c25f8812a291d498`). The new ingredient is an exhaustive WRITTEN normal form for the actual officer matchings, followed by two forced pair-lines and a one-term row inner product. It uses no old computational lower bound or old support enumeration. It does NOT exclude every support48 profile and does not prove lower49. The documented unrestricted gap remains48..60.

The normal form below is derived, not asserted as a symmetry catalogue. All reductions use only local coordinate-value relabelings (permutation unitaries), which preserve all six AME marginals and support counts.

## 1. Exact AME inputs and the24-officer structure

For all six coordinate pairs, the actual reduced density matrix is I36/36. Therefore every fixed pair-value line has squared A-norm1. An officer is its only support point; officers cannot agree in two coordinates; every line without an officer meets N. Every non-officer point uses only positive-deficit values in each coordinate.

At e=0 every such hole line has exactly two nonzero entries, because each of the three36×36 unitary flattenings has t singleton rows and h non-officer rows, with total support t+2h. A row/column with N has degree2. Two unitary rows cannot meet in exactly one nonzero column. These are exact two-party norm/coherence conditions, not a one-body or approximate replacement.

Let A_i be the four active local values of coordinate i and B_i its two inactive values. The previous holonomy note derives from the historical officer-count identities

    Σ_T c(x)=48,      Σ_T binom(c(x),2)=24,      |T|=24,

where c(x) counts active coordinates. Since Σ_T(c−1)(c−2)/2=0 and Σ_Tc=2|T|, every officer has exactly two active coordinates. For each unordered pair{i,j}, there are four such officers, denoted T_ij. Each active value at i has exactly one active officer neighbor at j (its other three A_j pair-lines are holes). These neighbors define bijections F_ij:A_i→A_j with F_ji=F_ij^(-1). The four T_ij officers use every pair of binary inactive values at the other two coordinates, because their projection there is injective and has four points.

For completeness, the count identities follow by summing6v_i−h on active single-coordinate values and v_i v_j−h on active pair grids, with v_i=4,h=12. They are an existing baseline mechanism, not new theorem credit.

## 2. Deriving the complete officer matching normal form

First identify A_2,A_3,A_4 with A_1 via F_12,F_13,F_14, so these three bijections become the identity. Label every A_i by the same four symbols (x,y)∈F2² as follows. In the officer T_12(a), let x,y be its inactive bits in coordinates3,4. Those four inactive pairs are all distinct, so a↦(x,y) is bijective. Arbitrarily label each inactive B_i by F2 initially; flipping an inactive bit is an allowed value permutation.

Two different T_ij/T_ik officers with the SAME active value at i already agree at i; they cannot agree also in the fourth (inactive) coordinate. Their inactive bits there must be opposite. Applying this at coordinate1 shows that the inactive data for T_13 and T_14 have the form

    T_12(a): inactive3=x,       inactive4=y,
    T_13(a): inactive2=z(a),    inactive4=y+1,
    T_14(a): inactive2=z(a)+1,  inactive3=x+1.

Both(z,y) and(z,x) must be bijections F2²→F2², because T_13/T_14 each use all four inactive pairs. The2×2 binary Latin-square condition forces z=x+y+constant. Flip the inactive coordinate2 label to set that constant to0.

Now examine each active value at coordinates2,3,4. Inactive bit1 in T_23 as a function of its active coordinate2 label is a function alpha_2 independent of both x and y, hence

    alpha_2=x+y+c2.

Indeed T_23's other inactive bit is y+1 and T_24's other inactive bit is x+1, while their inactive1 bits are opposite. Each corresponding pair must use all four binary values. Flip inactive coordinate1 to set c2=0.

At coordinate3, T_13 has inactive bits2=x+y and4=y+1. Consequently the inactive1 bit in T_23 is independent of both y and x+y, giving

    alpha_3=x+c3.

At coordinate4, the inactive1 bit in T_24 is independent of both x and x+y, giving

    alpha_4=y+c4.

These elementary binary claims use no enumeration: a bit function independent of the two coordinate bits of a2×2 array is their XOR or its complement; changing to the independent coordinate pair(y,x+y) or(x,x+y) gives the other two displayed forms.

Equate the two inactive bits of the SAME officer when reading it from either active endpoint. This gives, with p=c3, q=1+c4 and r=p+q,

    F_23(x,y)=(x+y+p, y+1),
    F_24(x,y)=(x+1, x+y+q),
    F_34(x,y)=(y+r, x+r+1).

For example T_23's inactive4 bit equals y_2+1 from its coordinate2 endpoint and y_3 from its coordinate3 endpoint, while its inactive1 bit equals x_2+y_2 and x_3+c3. These give F_23. T_24 similarly equates inactive3 and1. For T_34, inactive2 gives x_4+y_4=x_3+y_3+1, and inactive1 gives y_4=x_3+c3+c4, yielding the last formula and r=p+q.

Conjugate all four active alphabets by the SAME translation (x,y)↦(x+q,y+p). The three constants transform respectively as

    p -> p+p=0,       q -> q+q=0,       r -> r+p+q=0.

The identity F_1j maps stay the identity. Thus every officer set in this profile has, after allowed local relabelings, the following missing-active-pair maps:

    F_12=F_13=F_14=id,
    F_23(x,y)=(x+y,y+1),
    F_24(x,y)=(x+1,x+y),
    F_34(x,y)=(y,x+1).

No coefficient/phase assumption entered this reduction. Label 0=(0,0),1=(1,0),2=(0,1),3=(1,1). The maps are explicitly

    symbol:       0  1  2  3
    F_23:         2  3  1  0
    F_24:         1  2  3  0
    F_34:         2  0  3  1.

## 3. Two forced hole lines contradict unitarity

All points of N lie in A_1×A_2×A_3×A_4, and must avoid every officer pair-line. In the derived normal form a tuple(a,b,c,d) can therefore occur in N only if

    b!=a, c!=a, d!=a,
    c!=F_23(b), d!=F_24(b), d!=F_34(c).                 (*)

Conversely a fixed active pair-value line outside its matching has no officer, so it must contain exactly two N entries at e=0. We use this only for two explicitly named lines, not as sufficiency of(*) for a tensor.

### Line12=(3,0)

This is outside F_12=id, hence a hole. Conditions(*) give

    c in{0,1},     d in{0,2}.

Here c avoids3 and F_23(0)=2, while d avoids3 and F_24(0)=1. The last condition removes d=2 when c=0, because F_34(0)=2, and removes d=0 when c=1, because F_34(1)=0. Exactly two positions remain:

    X=(3,0,0,0),       Y=(3,0,1,2).

The hole line needs two nonzeros, so BOTH are in N. In M_(12|34), row(3,0) has precisely columns(0,0),(1,2).

### Line34=(1,2)

This is outside F_34, since F_34(1)=0!=2, and is another hole. Conditions(*) force

    a in{0,3},     b in{0,3},     b!=a.

Indeed a must avoid c=1,d=2; b must avoid F_23^(-1)(1)=2 and F_24^(-1)(2)=1. Therefore its only two possible rows are(3,0) and(0,3). The first contains Y already; the exact-two property forces

    Z=(0,3,1,2) in N.

Thus rows(3,0),(0,3) of M_(12|34) meet in column(1,2). They cannot meet in column(0,0), because(0,3,0,0) is forbidden by c=a under F_13=id. Row(3,0) has no other nonzero columns. The two row inner products consequently have exactly ONE nonzero term,

    A_(3,0,1,2) conjugate(A_(0,3,1,2)) !=0,

contradicting unitarity. This is valid for arbitrary complex phases and moduli. The profile is impossible. ∎

## Verification and remaining target

The proof uses all six pair-line norm/occupancy constraints induced by the original two-party reductions and the actual off-diagonal row orthogonality of12|34. It does not claim diagonal constraints alone are sufficient for AME. No new state or lower-support witness is being offered, so no numerical normalization or omitted pair reduction is hidden.

The complete normal form and the two forced lines are now the bounded verification targets: independently reconstruct the binary endpoint functions, the translation eliminating p,q,r, the three explicit four-symbol maps, and the one-term contradiction. No finite software check has run. This is not proof-assistant/kernel or human verification and not novelty clearance.

The older holonomy snapshot correctly recorded an unresolved twisted-matching obligation at that earlier stage. This numbered new manuscript closes that SPECIFIC all-three/e0 profile by deriving, rather than discarding, its twisted matching data. Other three-/four-thick-axis profiles and the required e>0 cases remain; the unrestricted numeric bound has not changed.
