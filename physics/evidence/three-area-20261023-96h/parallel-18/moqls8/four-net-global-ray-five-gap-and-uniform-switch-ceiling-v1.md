# ORIGINAL FOUR-family q2 — ANY four-net ray-five gap; exact uniform-switch barrier

**PhysicsMOQLS8-2. NEW WRITTEN AUTHOR CANDIDATE**, no independent/parent/formal/executable/novelty acceptance. Actual returned clock precreation bound **2026-10-26T06:40:44-0700 PDT**. All old pinned sources unchanged.

## 1. Two distinct results and their exact original applications

**ResultA (all-object, new q2 residual exclusion):** On ANY actual order8 FOUR-net, for ANY arbitrary-complex Q unit assignment ONB on EVERY net-line, EVERY nonfixed actual ray has multiplicity<=4. In particular the ENTIRE multiplicity5 stratum is excluded in EVERY component dimension, not only intrinsicC2 or an affine construction. An original FOUR-family with TWO classical members gives exactly this FOUR-net for EACH of its two remaining members. Their coupled compatibility is still OPEN; the theorem does NOT presume those two members classical or exclude every irreducible3+ component.

**ResultB (bounded construction barrier, not all-object):** On the additive F8 Latin-square base, a SINGLE fixed irreducible unitary block applied exactly on a nonempty proper subset of rows can coexist with at most TWO ordinary affine classical mates. Every block of size>=3 admits NO such mate. Thus no original q1 FOUR-family with THREE affine classical mates can be obtained by this precise primitive. This is a documented exact barrier/new representation of the failed single-switch construction, NOT an exclusion of arbitrary/nonuniform or nonaffine four-families.

The accepted164LF triple construction and ANY-four-net intrinsicC2 companion obstruction remain SEPARATE. Neither is a premise of ResultA. ResultB explains a limitation of the single-switch primitive without pretending to strengthen the accepted C2 theorem into full four-family closure.

## 2. All-object positive-cell incidence at four classes

Let N have FOUR actual parallel classes of eight8-cell lines, with different-class lines meeting once. Q is ONB on each line. Fix an actual unit ray v of multiplicity m<8. It occurs on m distinct lines in EACH class. Put d=8-m and

    g_x=|<v,Q_x>|^2,
    S={x:0<g_x<1}, L=|S|.

Every line occupied by v has no other positive g. Each unoccupied line has positive mass1 and at least TWO S-cells; otherwise a sole positive entry would have g1 and be another v occurrence. The d unoccupied lines in EVERY class partition S. The unused d rows/d columns contain S, so

    sum_S g=d,    2d<=L<=d^2.

Join S-cells sharing an actual N-line. Different classes give disjoint edge sets. Cauchy applied to their d group sizes gives

    e(G)>=4 L(L-d)/(2d),   e(G)<=L(L-1)/2,
    hence (4-d)L<=3d.

At d1 the bounds give L<=1 versus L>=2; at d2 they give L<=3 versus L>=4. Thus m7,m6 are impossible. This derivation consumes only the ACTUAL four classes, not any fifth line or mate.

## 3. Complete m5 exclusion in every component dimension

Suppose m5, so d3. Then6<=L<=9. Each positive group in EACH class has size2or3: any non-row line meets the three unused rows in at most three cells, and a row meets only the three unused columns. Let n2+n3=3, L=2n2+3n3. Its group edge count is n2+3n3=2L-9, giving

    e(G)=8L-36.

Let H be the ACTUAL complement of G on S. Consequently

    e(H)=(L^2-17L+72)/2.

For L6 this is3, for L7 it is1, and for L8/L9 it is0. These values follow from the exact group identity; no enumeration was executed. In particular H has at most three edges.

The following spectral bound is complete. If H contains a triangle, its at-most-three edges make it EXACTLY K3 plus isolates, with largest adjacency eigenvalue rho2. Otherwise its clique number<=2. For nonnegative weights w summing1,

    sum_(ij edge)w_i w_j<=1/4.

Proof: maximize on the finite simplex and choose minimum positive support. Two nonadjacent positive vertices can have their mass moved to the one with larger linear coefficient without decreasing the maximum, contradicting minimal support. The support is a clique of size<=2, on which the maximum is1/4. For a nonnegative unit Rayleigh maximizer x, Cauchy yields

    rho^2=4(sum_edge x_i x_j)^2
          <=4e(H) sum_edge x_i^2 x_j^2
          <=e(H)<=3<4.

Thus rho<2 unless H is the exact K3-plus-isolates case. No phase assumption or unproved finite graph classification is involved.

Let B have the actual Q_x,x∈S as columns, C=B*B, T=BB*. Actual G-edges give C_xy0; all other off-diagonal moduli<=1. For any complex z,

    z*Cz<=||z||^2+2sum_(ij in H)|z_i||z_j|
          <=(1+rho)||z||^2.

Hence T<=(1+rho)I, whereas <v,Tv>=sum_S g3. The rho<2 cases are impossible. In the only equality case C<=3I and T<=3I force Tv=3v. The vector z=B*v has EVERY coordinate nonzero by S's definition, and Cz=3z. But an isolated H-vertex has C-row the corresponding identity row, forcing z_i=3z_i. Such an isolate exists because L>=6 and K3 has only three vertices. Contradiction.

This excludes ALL m5 supports/arbitrary phases/actual four-nets. Together with §2,

    m in{1,2,3,4,8}; m8 is fixed.                      (FOURGAP)

At m8 the ray occurs in EVERY board row and is orthogonal to every other actual ray, hence is a singleton intrinsic component. Fixed rays and classical families ARE ALLOWED. Every ray in any irreducible component of dimension>1 therefore has multiplicity<=4.

This is an ENTIRE q2 per-ray stratum exclusion, not a bound only for the author's selected two-ray triple, a projector-rank ansatz or a numerical graph sample. A putative original FOUR-family with TWO classical members must satisfy FOURGAP for BOTH remaining assignments, in addition to their full mutual product-ONB condition. This latter condition was NOT used in the proof and remains a separate exact barrier.

## 4. Precisely bounded single-switch primitive over F8

Let F=F8, with additive characteristic2. The classical base is Q0(x,y)=e_(x+y). Let T be a set of r>=2 basis labels. U is ONE unitary on span{e_t:t∈T}, whose coordinate-support graph on T is connected, and acts identically outside T. Let W be a nonempty proper subset of row indices. Define

    Q(x,y)=U e_(x+y) if x∈W and x+y∈T,
           e_(x+y) otherwise.

All rows are ONBs automatically. This definition is EXACT: the same U and label block T in every switched row, no multiple channels, phase-dependent sectors or separately chosen cell unitaries. If U has several irreducible blocks this theorem must be applied blockwise only after their potentially different incidence constraints are justified; it is not a claim about arbitrary multiswitches.

A mixed set {Ue_t:t∈S} union{e_t:t∈T\S} is an ONB on the T-space iff U preserves the coordinate subspace S. Indeed its switched vectors must be orthogonal to all unchanged complementary axes; unitarity then makes the complementary block invariant too. Connectedness of U on T therefore forces S=empty OR S=T. This argument retains arbitrary complex phases and does NOT require U to be fully supported.

Consequently column orthonormality requires, for every y, that W membership be constant on y+T. Let

    H={h∈F: W+h=W}

be W's full additive period subgroup. It is proper because W is nonempty/proper, so |H|<=4. For any t,t'∈T and any a, membership of a+t in W equals that of a+t', giving T-T⊆H. Conversely this period condition makes every column switch all T entries or none. In particular T lies in a coset of H and r<=|H|<=4.

## 5. All affine mates; why a3/4 block cannot evade the barrier

An affine classical square has slope m≠0. The exceptional slope1 is NOT a mate of the SWITCHED Q either: §4 gives r<=4, so choose t outside T; all EIGHT cells on its P_1 symbol line carry the unchanged same ray e_t. Thus every possible affine mate of Q has m≠0,1, not merely one required in advance to be orthogonal to the old base. Put

    delta=m/(1+m),

which lies in F\{0,1}. On a fixed P_m symbol line k, parameter t=x+y gives

    x=(k+m t)/(1+m),       y=t+x.

Its T entries switch according to W at those x values. The all-or-none lemma requires and suffices that delta(T-T)⊆H, because k/(1+m) runs over ALL F. This is exactly the actual classical-mate bridge, rederived here; no transpose or unverified completion is invoked.

If r>=3, T-T spans a two-dimensional additive subspace. Since H is proper and has size<=4, H must be exactly that span, of size4. The mate condition would imply delta H=H. But every nonzero delta≠1 in F8 has order7, because F8* has prime order7. For any nonzero h∈H its seven distinct delta^j h would all belong to H, impossible for |H|4. Thus EVERY r3/4 irreducible single switch has NO such affine classical mate. r>=5 was already impossible for a proper row switch even before adding a mate.

If r2, let tau be the nonzero difference of its two labels. Then tau∈H and a mate requires delta*tau∈H. The allowed deltas lie in H/tau excluding0,1, so there are at most |H|-2<=2. Distinct mates give distinct deltas, since m=delta/(1+delta). Therefore at most TWO ordinary affine classical mates coexist with the primitive.

The accepted triple uses r2, |H|4 and exactly two such deltas, so it saturates this precise primitive bound. That observation is NOT used to exclude any different construction. Requiring THREE affine classical mates, as in a q1 four-family, forces a replacement mechanism: nonuniform mutually coupled unitaries, different block incidence, or a nonaffine net. It cannot be achieved by adding one more slope to this uniform primitive, nor by increasing its block to3or4.

## 6. What remains, priority and permanent assurance

ResultA is a new all-object q2 ray restriction. ResultB is a complete but explicitly BOUNDED mechanism barrier and must never be promoted to all-object q1 closure. Neither proves exact M(8), excludes every unrestricted four-family, waives A10/A11/threeGBUNKNOWNs or supplies executable finite-witness acceptance. The new FIVE-net qutrit spectral exclusion is a SEPARATE prospective candidate, not a premise here; no older474LF/598LF gate is widened by this packet.

The full-line mate/rotation primitive has PRIOR Zhang–Cao/Ball–Simoens/Musto ancestry. The bounded current source comparison is not a novelty certificate. Generic complement-spectral/simplex/Cauchy/period-subgroup methods are ordinary PRIOR mathematics. Exact theorem priority and any specialist contribution are UNCLEARED.

All reasoning is WRITTEN and exact; no scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/CLI/nestedagent/newGO/privatefloat/decimal gloss/numeric parameter trials. Metadata date/hash/LF only. No independent/family/human/formal/kernel/executable/mutation/replay/novelty acceptance claimed. ENTIRE proof/dependency/application reconstruction is required for any promotion, not a review of the ray list or a headline.

Own permanent currentv112/visiblev105/v107/v109 intake read-order PROCESS MAJOR and all older owner/parent/reviewer findings remain. The HELDv3 false ALL-eight-columns/global-light and derived staircase-only reduction remain WITHDRAWN; neither is used in this packet. No later proof cures history or establishes clean-thought/runtime/trial-free cognition census.

Exclusive owner-root new writes; frozen/shared sources unchanged; no git/deletion/publication. Same18/originalprimary/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/cadence<=30min. No early final-park or96-hour closeout. The original q1 higher4-8-component, q2 coupled assignments and unrestricted family research continues.
