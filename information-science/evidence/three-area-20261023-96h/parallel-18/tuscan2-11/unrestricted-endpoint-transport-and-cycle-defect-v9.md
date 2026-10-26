# Unrestricted Tuscan11 — endpoint transport permutations and the exact12-cycle defect budget

Observed before creation: **Sun Oct 25 15:40:55 PDT 2026**, `/bin/date`. Owner InfoRecursiveMDS18-2. NEW WRITTEN CANDIDATE identities/bounds, not independently reviewed/formal/executable/novelty accepted. No scientific interpreter/eval/arithmetic program/enumeration/replay/solver/modelCLI/nested agent/GO. All arithmetic and permutation proofs below are written.

This representation covers EVERY original arbitrary/asymmetric array. The cyclic object is an EXACT bookkeeping extension by ONE new symbol, not cyclic development, a Latin-column assumption or wraparound imposed on the original linear rows. It retains all boundary defects, which must NOT be silently set to zero.

## 1. Current supported boundary and literal original residual

There are eleven arbitrary Hamilton row permutations R_s of X, indexed by their unique start s. Exact110 LINEAR ordered adjacencies gives unique ends and endpoint derangement tau(s). The actual second/penultimate functions are f(v),p(v); neither is assumed bijective. Define counts c_f(x)=#{v:f(v)=x}, c_p(x)=#{v:p(v)=x}.

At the original Tuscan-2 target, Gamma records the99 LINEAR distance-two events, with no collisions. Thus `Gamma=J11-I11-M`, where M is simple zero-diagonal with11 arcs, row degree c_p and column degree c_f. Completed actual center turns satisfy `sum K_v=I+Gamma+GF=J+GF-M`, with genuine f,p/GF, all ten-step layers and Hamilton11 cuts still REQUIRED.

The complete actual-row low-support theorem m>=7 is NOW WRITTEN_SUPPORTED by `institute/runs/three-area-2026-10-23-96h/tuscan-entire-m3-through-m6-parent-v1.md`, SHA256 `58334a063096a944637d648f938d3c4f64cf8c91d52ada61aad40ab03f508834`. Its actual233LF review SHA256 `bf383f713b9dcd47c63c9b6a95976bbb8a11cac31785a7782b9599fe966fed1c` and the full parent body/end were read AFTER the v92 Sun return and checkpoint027, as recorded in028. The base interface remains `unrestricted-boundary-turn-coupling-v1.md`, SHA256 `e54953336e35bd7a535d147ca6a564f9db30ddca966f1ad31dc58485167d8275`.

NO m7/v7/v8 acceptance is inherited. The new m7 candidate leaves one110-face theta+leaf(v3,w4,l<=6) and all m>=8; the ENTIRE original actual m>=7 residual remains at the accepted boundary. No11x11 table or unrestricted all-support obstruction is delivered here.

## 2. ACTUAL endpoint predecessor/successor permutations at EVERY center

Fix y in X. Define L_y on X\{y} by

`L_y(s)=the predecessor of y in the actual row STARTING s`.

This exists for every s!=y. All ten incoming arcs to y occur once, so L_y is a PERMUTATION of X\{y}. Its fixed points are EXACTLY the rows with y SECOND: a row starting s has predecessor s immediately before y iff y is its second symbol. Therefore

`fix(L_y)=c_f(y)`.                                      (2)

Independently define R_y on X\{y}, this time indexed by END labels,

`R_y(e)=the successor of y in the actual row ENDING e`.

All ten outgoing arcs from y occur once, so R_y is also a permutation of X\{y}. Its fixed points are EXACTLY the occurrences of y in the PENULTIMATE position, giving

`fix(R_y)=c_p(y)`.                                      (3)

These are not guessed permutations replacing the rows: they are derived from their ACTUAL endpoints. Notice the reversed f/p order in(2)/(3); confusing it would give the wrong M margins.

### Consequence: both boundary counts are at most EIGHT

Let s=tau^{-1}(y), the start of the row ending y. Its predecessor p(y) cannot equal s, because that would repeat the first symbol at the penultimate position of an eleven-symbol permutation. Thus L_y is NOT the identity.

Likewise, in the row starting y with end e=tau(y), successor f(y) cannot equal e: the second and last symbols are different. Thus R_y is NOT the identity.

A nonidentity permutation on ten elements moves at least two. Consequently EVERY original array satisfies

`c_f(y)<=8`, `c_p(y)<=8`.                               (4)

This improves the trivial nine obtained just by excluding the first/last rows. Also, SECOND and PENULTIMATE positions are different, and neither can occur in the row starting or ending y. Hence

`c_f(y)+c_p(y)<=9`.                                    (5)

For example, c_f(y)=8 makes L_y a TRANSPOSITION on its two nonfixed row-start labels. One is the start of the row ending y; the other is the sole row in which y is neither first/second/last. This is an actual endpoint-coupled derangement, not a symmetry convention.

## 3. Exact coupling to tau and the completed center permutation

Delete y from its actual tau-cycle and call the resulting permutation of X\{y} tau_y:

- tau_y(s)=tau(s) if tau(s)!=y;
- tau_y(tau^{-1}(y))=tau(y).

Even when tau has a2-cycle through y, this simply gives a fixed point at its partner. No endpoint cycle is removed from the family by assumption.

Write k_y for K_y restricted to X\{y}. Then the exact FUNCTION identity is

`k_y = R_y o tau_y o L_y^{-1}`.                         (6)

Proof: in a row R_s with s!=y and tau(s)!=y, the actual internal turn through y sends predecessor L_y(s) to successor R_y(tau(s)). For the one row ending y, L_y(tau^{-1}y)=p(y), and tau_y skips to tau(y). The row ending tau(y) is the row STARTING y, whose successor at y is f(y). Thus(6) gives exactly the added boundary p(y)->f(y). It is not a wrapped turn inside one original row.

Equation(6) retains more information than the aggregate `sum K=J+GF-M`: the endpoint deletion tau_y is tied to the SAME actual tau, while the fixed-point counts of L_y,R_y are exactly the degrees of M. No GF=M, independent row reversal, regular M or Latin middle column is introduced.

### An unrestricted parity identity

Deleting one point from a nontrivial permutation cycle changes its sign, so `sign(tau_y)=-sign(tau)` for EVERY y. On the110 arcs, T follows actual row segments. If tau has c cycles, sign(T)=(-1)^(110-c)=-sign(tau). Arc reversal has55 transpositions, sign-. The center rotations multiply to product sign(k_y); hence sign(T)=-product sign(k_y), giving

`product_y sign(k_y)=sign(tau)`.

Multiply the signs in(6) over ELEVEN centers. Since sign(L_y^{-1})=sign(L_y),

`sign(tau)=product sign(R_y)sign(L_y) *(-sign(tau))^11`.

Therefore EVERY actual order11 array satisfies

`product_y sign(L_y)sign(R_y)=-1`.                       (7)

This is not the unreviewed global-asymmetry candidate; it is a direct actual-row endpoint/turn parity calculation. In the current m7 one-face candidate, signs of k_y give opposite L/R parities only at the4-cycle center; all other centers have equal L/R parity. That remains a derived necessary condition, not a constructed system.

## 4. Exact extension to ELEVEN Hamilton12-cycles — ALL arrays, not a family

Adjoin one new symbol infinity. For EACH original row

`(s,...,tau(s))`

make the directed cycle

`(infinity,s,...,tau(s),infinity)`.

Let P_s be its12-by12 permutation matrix (tail row/head column). Every P_s is ONE Hamilton12-cycle. Original110 arcs occur once, and the11 infinity-to-start and11 end-to-infinity arcs also occur once by the endpoint bijections. Thus

`sum_(s in X) P_s=J12-I12`.                            (8)

Conversely, ANY eleven Hamilton12-cycles partitioning all directed arcs of K12*, cut at the SAME infinity, give eleven actual Hamilton rows with exact LINEAR adjacency coverage. Their starts/ends are automatically bijective. This is a bijection on the ENTIRE original Tuscan-1 array class, not an assumption of cyclic development or a transitive automorphism.

The adjacency extension is standard: [Golomb and Hess, *Optimum Seating Arrangements and Tuscan Squares*, Ars Combinatoria129(2016),397–402](https://combinatorialpress.com/article/ars/Volume%20129/volume-129-paper-31.pdf), especially p398. I read ALL six scanned pages via source-only rasterization after the text reader reported incomplete extraction. The PDF is retained as `source-golomb-hess-seating-2016-v1.pdf`, SHA256 `2c3c5987ac62ec396ac1021906707254779c94daaa888878371b448665e0c4b7`; checkpoint024 pins all six rendered pages and discloses curl/pdftoppm as SOURCE-EXTRACTION, not mathematical checks. This paper gives no Tuscan-2(11) table or current-status settlement. Its old n6/n7 tables/counts are source reports, not newly verified certificates. No novelty claim attaches to the standard extension.

## 5. EXACT linear-distance-two defect blocks: H is NOT GF

Put `S=sum_s P_s^2`, counting all cyclic two-step events on the extended twelve symbols. Define the finite endpoint-wrap matrix

`H[e,s]=1 iff tau(s)=e`.

Thus H is the permutation matrix of tau^{-1} in tail/head convention, zero-diagonal with11 arcs. It records end->infinity->start, NOT the center-boundary p(v)->f(v) counted by GF.

On finite x,y the cyclic two-step events are the original99 LINEAR events plus exactly these11 endpoint-wrap events:

`S_(X,X)=Gamma+H`.                                    (9)

The other two cyclic events per row are penultimate->infinity and infinity->second, so

`S[x,infinity]=c_p(x)`, `S[infinity,y]=c_f(y)`,
`S[infinity,infinity]=0`.

Let `D_infinity=S-(J12-I12)`. Under the ORIGINAL Tuscan-2 condition, the FULL block identity is

`D_infinity = [ H-M       c_p-1 ]`
`             [ (c_f-1)^T     0 ]`.                    (10)

All margins sum to zero, as they must because each P_s^2 is a permutation matrix. The finite row deficit of H-M is1-c_p, exactly canceled by the infinity column; the column statement is analogous. This binds ACTUAL endpoints and actual missing-graph degrees, not arbitrary independent marginals.

### Full exact construction criterion retained

Given any eleven Hamilton12-cycles satisfying(8), define their ACTUAL endpoint-wrap H by cutting at infinity. Their original rows satisfy Tuscan-2 IF AND ONLY IF

`Gamma=S_(X,X)-H` has every entry<=1.                   (11)

Nonnegativity/zero diagonal and99-event total are automatic from the actual row cuts. This iff does not require the fringes c_f,c_p to be1 and does not set H=M.

By contrast, demanding the STRONGER circular two-step condition S=J12-I12 is equivalent to simultaneously `c_f=c_p=1` and `H=M`. That is a SPECIAL SUBCLASS, not a licensed original normalization. We do NOT demand it. In particular the false general identity GF=M is not smuggled in by confusing GF with H.

## 6. A uniform ALL-SUPPORT collision/energy budget

Let

`C_collision=sum_(a,b) binomial(S[a,b],2)`,
`h0=|support(H) intersect support(M)|`.

No event enumeration is executed here. In the finite block, each S-entry is Gamma0/1 plus H0/1; it is2 exactly where an H-edge is NOT in M. Thus there are11-h0 finite collisions. The infinity row/column contribute the usual multiplicity pairs. Therefore

`C_collision=11-h0 +sum_x binomial(c_f(x),2)`
`                         +sum_x binomial(c_p(x),2)`
`            =(sum c_f^2+sum c_p^2)/2-h0`.             (12)

Also S has132 events and zero diagonal. Hence

`||D_infinity||_F^2=2 C_collision`.                     (13)

This can equally be checked directly from(10): finite norm22-2h0 plus the two fringe norms sum c_f^2+sum c_p^2-22 gives the same result. These are exact WRITTEN integer identities, not interpreter checks or a claimed finite-certificate replay.

### Bound C_collision<=45-h0 from ACTUAL simple M

Regard M's11 arcs as11 edges of a SIMPLE bipartite incidence graph, tail-copy on one side and head-copy on the other. Its vertex degrees are c_p,c_f, all<=8 by(4). Set

`T_degree=sum c_f^2+sum c_p^2`.

If its maximum degree d<=4, then T_degree<=d*22<=88. If5<=d<=8, choose a d-edge star and let R=11-d be the other edges. The number W of pairs of incident edges is bounded by

`W<=binomial(d,2)+R+binomial(R,2)`.

Indeed a remaining edge not at the star center meets at most ONE star edge at its other endpoint, while all remaining-edge pairs give at most their total binomial count. Simplicity prevents two edges sharing both endpoints. Since T_degree=22+2W,

`T_degree<=d^2+R^2+d+3R=2d^2-24d+154`.

This convex quadratic has endpoint values84 at d5 and90 at d8, hence is<=90 throughout that interval. Together with the d<=4 case,

`T_degree<=90`,
`C_collision<=45-h0<=45`,
`||D_infinity||_F^2<=90-2h0`.                          (14)

This bound holds for EVERY unrestricted target candidate, regardless of m or symmetry. Equality in T_degree90 requires maximum degree8 (the d<=4 bound is88 and the quadratic is smaller at5/6/7), hence a transposition L_y or R_y at some center by(2)/(3). This is only a consequence, not an assumed concentration of M.

## 7. What is genuinely open, and why this does NOT solve the original problem

The exact new all-array representation is: eleven ACTUAL Hamilton12-cycle permutations partition all arcs as(8); their original cuts supply H,L_y,R_y,tau and the full boundary transport(6); the finite block in(11) has no collisions after subtracting H. The endpoint/defect identities(7),(10),(12) and budget(14) are necessary coupled constraints. All asymmetric arrays remain.

A construction would require literal cycles/rows satisfying the FULL iff(11), not only the scalar C_collision bound or an abstract M/degree profile. An obstruction would have to exclude ALL such full systems. For example a universal lower bound C_collision>=46 for every applicable Hamilton decomposition would suffice, but NO such lower bound is proved or assumed here; failure to prove it is not a change of target. Nor is C_collision<=45 alone sufficient for a table.

Thus **first unproved step remains an actual11x11 Tuscan-2 array or an obstruction for the ENTIRE original m>=7 system**, including the currently unreviewed exact-m7 one-face theta+leaf and ALL m>=8. No finite cap, stronger circular condition, regular missing graph, Latin-column or group-developed family may replace that residual.

The m>=7 low-support theorem has its separate current WRITTEN support; these NEW transport/energy statements require their OWN complete source-bound reconstruction. No old verdict or source report automatically validates them. V9/v10/v11/HOLD, all unadmitted-computation and32:24/59:57 cadence histories remain immutable. No actual table, all-support nonexistence, formal/kernel/executable/human/configured-family/novelty/publication acceptance, new scientific GO or round completion is claimed. Actual research continues at the full unrestricted coupled system.
