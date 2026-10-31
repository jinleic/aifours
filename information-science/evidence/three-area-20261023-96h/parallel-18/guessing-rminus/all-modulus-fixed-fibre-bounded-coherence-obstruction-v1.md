# ORIGINAL R-minus, ALL moduli — fixed-defect-fibre orthogonal transport needs coherence growing at least as sqrt(m/10)

Owner **InfoGuessingRminus-2**, info-5. Actual preceding returned `/bin/date`: **Mon Oct 26 08:20:15 PDT 2026**.

**Complete exact WRITTEN architecture obstruction, AUTHOR-UNREVIEWED.** This is on the ORIGINAL Z_m baseline for EVERY integer m>=2, including composites/nonunits. It removes the field, bilinear-Fourier and phase restrictions from the preceding all-selector barrier. Arbitrary WORD-DEPENDENT complex amplitudes and zeros are allowed, subject only to the stated coherence bound. A universal one-fixed-defective-vertex-per-class orthogonal transport cannot have coherence bounded independently of m. Flat full-fibre bases are excluded for ALL m>10, irrespective of phases.

This is NOT a global Hall/no-SECTION impossibility, a positive trade or a guessing-number bound improvement. Certified20/3..1847/276 and T300 unmet remain unchanged. The exact next representation is mixed multiple-fibre support, sufficiently concentrated/sparse amplitudes, or matchings depending on the ACTUAL FD subset A. No certificate is constructed or declared passed here.

No scientific interpreter/calculator/Eval/program/CAS/enumeration/solver/replay/build/test/CLI/nestedagent/newGO. All counts/inner-product identities are exact WRITTEN finite algebra, not matrix software or a physical quantum witness.

## 1. Complete original model and quantified statement

Use the literal original FULL neighbours

`N1=234567`, `N2={1,3,7,9,10}`, `N3={1,2,4,8,9}`,

`N4={1,3,5,8,10}`, `N5={1,4,6,9,10}`, `N6={1,5,7,8,9}`,

`N7={1,2,6,8,10}`, `N8={3,4,6,7,9,10}`,

`N9={2,3,5,6,8}`, `N10={2,4,5,7,8}`.

All26 edges, including34 and absent9–10, remain. Ten chosen triangles are `A123,B145,C167,D239,E(2,7,10),F389,G(4,5,10),H(4,8,10),I569,J678`; physical tuple orders are `1:ABC,2:ADE,3:ADF,4:BGH,5:BGI,6:CIJ,7:CEJ,8:FHJ,9:DFI,10:EGH`.

For ONE Z_m, arbitrary m>=2, the baseline C has all ten triangle sums0 and size M=m^20. Every syndrome class is an actual translate of C, size M. Any word of syndrome eta obeys the exact original decoder identity `x_v=f_v^0(x_N(v))+d_v(eta)`; hence an ENTIRE syndrome class is FD. Competing subsets remain arbitrary nonlinear, partial and coordinated across classes.

A pair is **confusing** iff some changed FULL own physical symbol has zero difference at its FULL original neighbourhood. A pair is **FD** iff it is nonconfusing. For a word x outside C its TRUE compulsory-removal set is the union

`R(x)=union_(v:d_v(eta(x))!=0) F_v(x)`,

`F_v(x)={c in C:c_N(v)=x_N(v)}`.

These are exactly baseline conflicts. Thus `(C\D) union A` is original-FD iff A is original-FD and R(A) subset D, with the ACTUAL R(A)=union_x R(x). This is the literal TRADE interface, not a deletion/projection relaxation.

Keep the ENTIRE thirteen-parameter family

`eta1=(0,0,0,d,0,f1,0,h,i,j)`,

`eta2=(a,b,0,0,0,f2,0,0,i,j)`,

`eta3=(0,c,0,0,e,0,g,h,k,j)`,

`eta4=(a,0,q,0,0,0,0,h,0,j)`,

with H: `a,b,c,q,f1,f2,h,j!=0`, `b!=c`, `f1!=f2`, `(d,i)!=(0,0)`, `(e,g,k)!=(0,0,0)` in the SAME Z_m. No value is assumed invertible. The family includes ENTIRE CRIT-OR e0 OR i=k without requiring either. Empty small-m hard instances are empty cases, not a field restriction.

### The universal certificate architecture

For EACH class j choose ONE fixed original vertex v_j with d_(v_j)(eta_j)!=0. Assign EACH potential word x in that ENTIRE class a unit vector v_x in C^C, supported INSIDE its actual single fibre F_(v_j)(x). Require orthogonality whenever two DISTINCT outside words are original-FD.

Allow arbitrary word-dependent amplitudes, phases and zeros, with a classwise coherence bound kappa_j>=1:

`|v_x(c)|^2 <= kappa_j / |K_(v_j)|` for every x,c,

where `K_v={c in C:c_N(v)=0}`. The bound is meaningful even when the support is sparse; no covariance/Fourier/equal-phase condition is imposed. Let kappa=max_j kappa_j.

> **Theorem COHERENCE-NOGO.** Any certificate of the stated architecture must have TWO classes using different vertices, and for SOME such pair `kappa_j kappa_l>=m/10`. Consequently `kappa>=sqrt(m/10)`. In particular no such certificate exists when `m>10 kappa^2`; arbitrary-phase FLAT full-fibre bases (kappa1) fail for EVERY m>10.

The more precise different-vertex inequalities are in §4. This theorem does NOT cover arbitrary vectors using multiple actual conflict fibres, unbounded growing coherence, or a matching chosen separately for the actual FD set A.

## 2. Actual kernel geometry and cardinalities, with COMPOSITES retained

Baseline decoding gives c_v=0 whenever c_N(v)=0, so K_v is supported on `U_v=V\(N(v) union{v})`.

The two hub kernels have ALL solutions

- K1: `8=(s,t,0),9=(0,-s,0),10=(0,0,-t)`, other0;
- K8: `1=(s,t,0),2=(-s,0,0),5=(-t,0,0)`, other0.

Their TWO free parameters in Z_m prove |K1|=|K8|=m^2 with no field/rank assumption. Their active supports are{8,9,10} and{1,2,5}, disjoint.

For peripheral vertices the full anti-neighbour/trace table is:

|v|U_v cyclic order|ALL five TWO-corner triangle traces|
|---|---|---|
|2|4,5,6,8|B:45,G:45,H:48,I:56,J:68|
|3|5,6,7,10|C:67,E:7-10,G:5-10,I:56,J:67|
|4|2,7,6,9|C:67,D:29,E:27,I:69,J:67|
|5|2,3,8,7|A:23,D:23,E:27,F:38,J:78|
|6|2,3,4,10|A:23,D:23,E:2-10,G:4-10,H:4-10|
|7|3,4,5,9|B:45,D:39,F:39,G:45,I:59|
|9|1,4,10,7|B:14,C:17,E:7-10,G:4-10,H:4-10|
|10|1,3,9,6|A:13,C:16,D:39,F:39,I:69|

Each U_v is an induced C4, so no chosen triangle is wholly inside it. A singleton trace forces its slot0; a two-corner trace has ONE free Z_m parameter, with its other slot the negative. Distinct chosen triangles use disjoint slots even at the same physical site, so these FIVE parameters are independent for EVERY m. Thus each peripheral |K_v|=m^5. This also explicitly proves every relevant fibre size without an executed rank census.

Any two distinct peripheral U-sets in the displayed table intersect in at most TWO physical vertices. If the intersection has two vertices, a baseline word there has one free parameter for each chosen triangle containing BOTH; a pair belongs to at most TWO chosen triangles, from the literal ten-list. Hence

`K_v intersect K_w is isomorphic to Z_m^r`, with r in{0,1,2},

for distinct peripheral v,w. This is a FREE-parameter statement, not an invalid dimension claim over a composite ring. With at most one intersection site, the baseline word is0. Edge34 may occur as an anti-intersection pair, but no chosen triangle contains BOTH3 and4; that case still has r0.

A hub U-set intersects ANY other U-set in at most ONE physical site, directly from its displayed three-site set and the peripheral rows. Thus all hub/peripheral and hub/hub intersections are{0}, of cardinality1. We never confuse the zero subgroup with an empty intersection.

Finally, for S=K1+K8, the four hub parameters are independent, so |S|=m^4. They give active coordinates at ALL SIX sites{1,2,5,8,9,10}. Every original neighbourhood has at least FIVE sites, and the complement of that six-set has only FOUR; therefore every N(u) observes one active site. At EACH active site, some observed slot is one free parameter with coefficient1 or−1, unmixed with the other three. The image of `S->c_N(u)` therefore projects SURJECTIVELY onto a Z_m coordinate, even when m is composite. Its kernel satisfies

`|S intersect K_u|<=m^3` for EVERY physical u.        (HUB-SURJ)

This is the explicit composite-modulus replacement for the field “proper subspace has codimension1” shortcut; mere noncontainment would not suffice over Z_m.

## 3. Whole same-class fibres force orthonormal BASES, not assumed Fourier matrices

Fix two distinct syndrome classes eta,theta using vertices v,w. Full baseline neighbour projection is surjective (no chosen triangle is wholly in N(v)); equivalently the displayed trace/kernel construction lets one set the neighbours and solve every remaining triangle slot. Choose exact b_eta,b_theta with their respective full neighbourhoods0.

ALL class-eta words with N(v)=0 are `b_eta+K_v`, and ALL class-theta words with N(w)=0 are `b_theta+K_w`. Each single-class set is original-FD and has exactly |K_v| or |K_w| words. Their assigned unit vectors are orthogonal within the class, and are supported on coordinates K_v/K_w. Thus EACH family is an orthonormal BASIS of that coordinate subspace, regardless of arbitrary phases, zeros, word dependence or how a larger class basis was defined.

Let U andV be the matrices whose columns are those two bases. Their cross-inner-product matrix is G=U*V. Ordinary finite projection algebra gives

`sum_(x,y)|G_xy|^2 = Tr(V* U U* V)`

`=Tr(P_(K_v) P_(K_w)) = |J|`, J=K_v intersect K_w.    (FROB)

The projections are coordinate projections, so their product has exactly |J| ones on its diagonal. No matrix entry calculation/program or numerical spectrum is invoked.

The coherence bounds and triangle inequality give for EACH entry

`|G_xy| <= |J| sqrt(kappa_eta kappa_theta/(|K_v||K_w|))`.

Consequently the number Z of NONZERO entries obeys

`Z >= |K_v||K_w| / (kappa_eta kappa_theta |J|)`.      (NONZERO)

This is exact even if the right side is not an integer; Z is simply an integer satisfying that real inequality. Flat Fourier/complex-Hadamard bases are only the special kappa1 case. Arbitrary cancellation is fully allowed in G; FROB prevents too many entries vanishing.

## 4. Actual ORIGINAL confusing pairs are too few for bounded coherence

Put S=K_v+K_w and h=b_eta−b_theta. The difference map `(k_v,k_w)->k_v-k_w` has kernel the diagonal J. Thus EACH delta in S has EXACTLY |J| preimages among these actual word pairs.

A possible original confusion at physical u requires `(h+delta)_N(u)=0`. On S the solution set is EMPTY or one coset of S intersect K_u, of cardinality |S intersect K_u|. Ignoring the additional own-symbol-nonzero requirement only INCREASES our upper count. Hence the total number T of original CONFUSING pairs is at most

`T <= 10 |J| max_u |S intersect K_u|`.                (MASK)

This is the union bound over ALL TEN ORIGINAL full-neighbour witnesses. It is not a projection relaxation used as a code: it is an honest upper count on the actual forbidden pairs, enough to prove existence of an FD pair below.

### 4.1 Two peripheral vertices

Here |K_v|=|K_w|=m^5, |J|=m^r, r<=2. Since every |K_u|<=m^5,

`T<=10 m^(5+r)`, while `Z>=m^(10-r)/(kappa_eta kappa_theta)`.

Every nonzero inner product MUST correspond to a confusing pair if the certificate is to satisfy FD orthogonality. Therefore Z<=T would require

`kappa_eta kappa_theta >= m^(5-2r)/10`.              (PERIPH)

Since5−2r>=1, a uniform kappa with m>10kappa^2 violates this necessary inequality. Thus an actual ORIGINAL-FD pair has nonzero inner product. Nonunit zero divisors do not alter the group cardinalities used here.

### 4.2 One hub and one peripheral vertex

Now |K_v||K_w|=m^7 and |J|=1. MASK gives T<=10m^5, NONZERO gives Z>=m^7/(kappa_eta kappa_theta). Orthogonality therefore requires

`kappa_eta kappa_theta>=m^2/10`.                     (MIXED)

Again m>10kappa^2 implies a contradiction. The actual pairs have distinct syndromes, so no diagonal/equal-word ambiguity enters the count.

### 4.3 The two hubs

Here |K_v||K_w|=m^4, |J|=1 and S=K1+K8. The explicit HUB-SURJ proof gives T<=10m^3. Thus

`kappa_eta kappa_theta>=m/10`.                       (HUBS)

This handles the exceptional small support without pretending that a composite-ring proper subgroup must have index m. Every observed free slot was explicitly surjective.

These three cases exhaust every DIFFERENT selected-vertex pair. In all cases the necessary coherence product is at least m/10. If m>10kappa^2, FROB's nonzero count strictly exceeds the total original confusing-pair count, so some actual FD pair has NONZERO inner product. This is a complete finite algebraic contradiction, not an executed enumeration or a numerical parameter probe. The threshold is derived from ten witnesses, not an arbitrary search cap.

## 5. Every SAME-vertex choice for all four classes is impossible even without a coherence bound

If all four classes chose one vertex, the choices1/3/5/9/10 are excluded by the architecture's required NONZERO selected defect:

`d1(eta1)=0`, `d3(eta3)=0`, `d5(eta4)=d9(eta4)=0`, `d10(eta2)=0`.

We do not assert that every nondefective fibre is disjoint from all other conflicts; it is simply NOT the selected-defective-fibre architecture being analyzed.

For remaining common vertices2,4,6,7,8, an actual equal-defect pair has a neighbourhood-preserving NO-confusion obstruction. Here is the complete necessary graph argument.

### Peripheral obstruction, reconstructed for ALLm

If delta has d_v(delta)=0 and r_N(v)=0, then r_v=0. A confusion witness cannot be v or one of its zero neighbours, so it must be w in U_v. Suppose TWO nonzero delta triangles have traces equal to ADJACENT singleton vertices a,b of the C4 U_v. Every w in that C4 is adjacent to at least one of a,b. At a claimed witness w, r_N(w)=0 too, so the corresponding nonzero triangle is wholly fixed inside N(v) union N(w), forcing its sum0. Contradiction. Thus EVERY representative of that delta with N(v)=0 is NONconfusing. This uses only actual sums/nonzero values, valid for composite m.

The required full data are

|v|equal class pair|two NONZERO delta columns|adjacent singleton sites|
|---|---|---|---|
|2|2/4|C:q,F:f2|6 and8|
|4|1/4|A:a,F:f1|2 and9|
|6|1/2|B:b,F:f1−f2|4 and3|
|7|1/2|A:a,H:h|3 and4|

The anti-neighbour C4 orders are in §2; the chosen triangle list directly gives these singleton traces. All listed nonzero values follow from H, including f1−f2 at every composite modulus. Signs do not require units or characteristic2.

### Hub8 obstruction

At U8={1,2,5}, centre1/leaves2,5, classes3/4 have equal d8. Their delta has nonzero C=q on the centre singleton and at least ONE nonzero leaf singleton among E=e,G=g,I=k, by H. A leaf witness is blocked by the centre singleton; the centre witness by that bad leaf. The same full-neighbour triangle-sum argument excludes EVERY confusing representative zero on N8.

### Two whole fibre bases cannot cross-orthogonalize

For any such equal pair, ALL words of its first class with N(v)=0 and ALL words of its second class with N(v)=0 are cross-FD, by the just-proved necessary obstruction. Each class contributes |K_v| unit vectors forming a basis of coordinates K_v. Cross-FD would require the two ENTIRE bases to be orthogonal to each other, impossible in the SAME |K_v|-dimensional space. Equivalently their coordinate row masses would sum to2 and violate Bessel<=1.

This argument has no phase/Fourier/coherence/field hypothesis. Together with the five excluded zero-defect choices it exhausts ALL TEN common vertices.

Thus a certificate must use at least two DIFFERENT vertices. PERIPH/MIXED/HUBS then force some coherence product>=m/10 and hence max coherence>=sqrt(m/10), proving **COHERENCE-NOGO**. ∎

## 6. Exact strength, next representation and original scientific ceiling

The earlier173LF field-trace-Fourier no-go is a SPECIAL CASE. The present Frobenius proof covers arbitrary complex phases—including nonlinear output chirps/F2-only choices—and arbitrary word-dependent amplitude zeros, as long as the stated coherence bound holds. It also applies to ORIGINAL ALLm Z_m, not just prime powers. No field dimension or selected numeric instance is smuggled into the composite count.

What it does NOT exclude is equally important: a certificate may use coherence growing with m, genuinely concentrated/sparse amplitudes, support spanning more than one actual defect fibre per class/word, other baseline directions, or a matching depending on the ACTUAL chosen FD subset A rather than one universal all-word assignment. Those are the required next representations. The theorem does not assert that any of them works, and absence of a universal certificate is never an improving FD code.

All original arbitrary-four/larger-family questions, nonflat CRIT-OR roles/covers, actual global Hall/injection, positive-gain FD trade with its ENTIRE TRUE union and global optimum remain OPEN. The field all-alphabet embedding remains a separate self-contained route; the original all-m/nonunit route has now been explicitly retained in this obstruction. Small m may satisfy m<=10kappa^2, but a cofinal bounded-coherence family cannot avoid the growing necessary lower bound. No new numerical bound follows.

**Certified20/3..1847/276 UNCHANGED; T300 UNMET.** This is the exact documented barrier and next-interface deliverable, not another necessary-condition count advertised as gn progress. All work is AUTHOR-WRITTEN/UNREVIEWED at ordinary finite group/unitary/Bessel/Frobenius facts. The needed actual graph/trace/zero-boundary arguments are reproduced above; no265FLAT1/176bridge/M5 negative theorem is a correctness premise. The old literal baseline238/282 trace geometry is source ancestry, not a hash waiver or fresh computer check.

The proof was saved074 actual08:17:39 before this body, after the proper actual v120 RETURN→NEW062→separate06:45:36 ACK/SEND sequence before resumed source/math. Permanent v25/024/034,parentv101,v9/v10/v11/laterthroughv34/ZEROscience/N4 UNKNOWN and all source/math withdrawals remain. No old false criterion/failed055/057 control guides this proof; no cure/backdating/global cognition-runtime census, parent adoption/formal/kernel/human/configured-family/executable/novelty/priority or physical-quantum-witness claim.

Same original18/exclusive ownroot/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/HOLD/actualsubstantivecheckpoints<=30min. No early final park, frozen edit, scientific program/replay/CLI/nestedagent/Git/publication/config/deletion/newGO. Original research continues beyond fixed bounded-coherence single-fibre transport.
