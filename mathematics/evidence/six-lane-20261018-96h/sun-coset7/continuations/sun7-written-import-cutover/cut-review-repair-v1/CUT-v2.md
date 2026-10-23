# CUT-v2 — corrected written-import audit, literal interfaces and expanded dependency order [CANDIDATE_UNVERIFIED]

Written: `/bin/date` read at 2026-10-19T18:42:07-0700, immediately before exclusive create. Owner SunM13MixedFibres, math-1.
Frozen finding map: CUT-REPAIR-SCOPE-FINDING-MAP-v1.md (f613d78f720a5beec412e1e84d0197f7026b0a09ac7a582026ebeb83e6070d23),
before this source audit. Responds to CUT Codex 0F/3M/1m review (24ded7bf47b199a051d060743ddfb426fd328e7d49fac15cbedf7c3c2748e2fb).
This is an immutable replacement audit, not a new class proof, acceptance or full Sun(7) verdict. Prior artifacts unchanged.

## 0. Withdrawal, notation and current gate boundary
CUT-v1 (3d0a98fb647c2c5939c84501f5da1c5c76a8073a0d876e407ceac51af50fe8f8) lines9,37-38,77-82,91-94,111's assertions
that the entire expansion was checked, no unresolved dependency existed, and every check was a non-premise are WITHDRAWN.
In particular: 'not an existence claim' does NOT imply 'not a premise'; agreement of scalar values does NOT establish
certificate feasibility or coverage. The replacements below use proof-path evidence, not those invalid inferences.
Completeness/no-computation certification remains WITHHELD pending independent review of this replacement and its packets.

Roots (all source identifiers below resolve here; full paths/hashes/ranges in the manifests):
- S = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7; D = S/continuations/k7-k62-residue; K62 = S/continuations/k63-residue/k62-followon.
- O16 = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016; R = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review; R16 = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review.
Physical source line numbers are one-based inclusive. 'Inherited' means the accepted historical import envelope; 'proof-use'
means the actual scoped dependency traced in the named text. A source's broader co-packaged results are not automatically
premises of an imported substatement. We retain explicitly imposed parent import envelopes even when a narrower proof-use
trace is available. No historical computer-assisted provenance is retrospectively removed.

Current observed statuses: A2X ACCEPTED at its inherited boundary (R/sun7-A2X-parent-verdict-v1.md,
9ad41f219dc7b6d6421dab03ac4cda46318c7d048669569ffea8986e5b0501f3); H5 and H6 ACCEPTED cores at their own scopes (R/sun5-C5W-
parent-verdict-v1.md; R/sun6-C56W-parent-verdict-v1.md). Their acceptance is NOT acceptance of the all-group S56W composition.
S56W remains pending as of this audit; only its parent erratum, not a parent verdict, was present at status read. Full Sun(7)
UNACCEPTED. StageB F-1 remains permanent. No runtime, Lean, human-review, novelty, priority or publication claim.

## 1. What remains valid: the conditional theorem-statement assembly
**SUN7-COND (conditional assembly, not a computation-free certification).** Assume the correctness of S56W with the parent
disjointness/wording erratum, and use H5/H6 at their now-accepted core scopes. Then S5W/S6W can replace every Sun(5)/Sun(6)
THEOREM-STATEMENT input below. Together with the accepted scoped class statements (including A2X), they imply Sun(7): every
seven pairwise disjoint LEFT cosets of finite-index subgroups of any group (equal subgroups allowed) have a pair of index
gcd at least7. Proof: R0 and the accepted six-class reduction give K7, K6.2*, K6.3, K5.2*, K5.3 or KII. Respectively use
K7-REM+A2X, K62X, K63-D/E/RES, K52W, the X1 deletion bridge+written X1, or KIIW. No class is omitted or narrowed.
The Codex CUT review supports this theorem-statement assembly separately from its rejected completeness assertions.

**Exact substitution interface (m1).** S5W/S6W have 'identical mathematical index-gcd statements and scope, with notation
normalized', NOT 'verbatim'/'word-for-word' text. S5W: any five pairwise disjoint left cosets, some index gcd>=5. S6W: any six,
some index gcd>=6. Both apply to every group, including any subgroup used for actual fibre traces, with possibly equal
subgroups; no cover/normality/least-order restriction. S56W LF35 has standing PAIRWISE DISJOINT cosets for L3/K2; no
unrestricted standalone L3/K2 is imported. H5 = no finite-group five-coset tuple4r_i with coprime r_i; H6 = no finite-group
six-coset tuple5r_i with coprime r_i. They do not alone assert S5W/S6W. S56W's R0, R1(5), R1(6) and exact Prop4.5 remain
necessary composition nodes; R1(5)/K2 there are distinct from R1(7)/the (a1) closure and the R2 row lemma K2.

## 2. Finding M1: E3 numerical compatibility check — proof-path resolution
Sources: K62/K62-E3-v1.md LF6-13,25-105,107-120; its erratum-v1 F2 and erratum-v2 Z1-Z12; E3 parent verdict LF14-31;
R/sun7-K62E3-codex-v1.prompt.stdout.txt LF235-244. The last source, NOT E3 verdict LF29 alone, identifies the numerical
example: with e_d=4 the necessary inequalities permit gcd=16 and M=n_d/16; at n_d=16,M=1 the incidence inequality is44<=45.
It appears in the reviewer 'requested mutation controls' section after the proof, and in E3-v1 LF117-120 as a suggested
boundary sanity check. It does not occur in Lemmas1-3, theorem steps1-4 or the corollary derivations.

The complete mathematical path used by the imported E3 conclusions is:
1. E3 Lemma1: labels at d have pair gcd3 except the stated t/i* pair when entry3; uniform1/3 at d forces entry1 if the
   exceptional pair is absent. INV gives at least one distinguished entry1. No numerical feasibility input.
2. Lemma2: explicit Sun2-incompatibility weights exclude O-O3, three O-O1s and (if h_d>0) O-O5; the inverse handles the
   all-five alternative. Erratum-v1 F2 states the redundant retained item(ii) is not needed by any case.
3. Lemma3 (Z6) orders t,p first then unmarked vertices; Lagrange/product formula bound each added factor by<=5 (<=4 in the
   no5 case). Thus gcd(n_d,T*_O)=2^min(e_d,v2T*_O). Z10 repeats the chain on every nonempty subset Q of O.
4. After actual inversion FIRST and normalisation SECOND (Z7), incidence is11n_d/4, every ordinary fibre has<=3 pieces
   (Sun4), and the M light fibres have<=1 piece, with the own fibre empty (Z8). Hence M<=n_d/8-1/2<n_d/8. Lagrange gives
   M>=n_d/gcd(n_d,T*_O), forcing gcd>8 and therefore e_d>=4,e*=2. This proof is symbolic at every allowed parameter.
5. C1: the same subset chain plus the count of four-missing fibres yields v2T*_Q>=3. C2 (Z11): explicitly excludes the h_d=0
   five, derives pair granularity n_d/2^(1+v2alpha*), double-counts missing pairs, obtains4n1+2n2+n4<19, and integrality yields
   n4>=2n1+2. Neither uses the e_d=4 numerical example. Swaps use actual INV/E6 only.
Thus the compatibility example is outside the theorem/corollary proof paths, not merely a nonexistence/existence wording
issue. Removing it leaves every used proof and conclusion intact. **M1 proposed RESOLVED by this trace.** The example is not
new evidence for realizability, and the proof does not exclude e_d=4. General LFC's historical Sun5/6 inputs remain until
proper S5W/S6W substitution.

## 3. Finding M2: reachable M13-A, not all M13 A-D
K62-FULL-v1 LF64,82-92 and its parent verdict LF23 import exactly **DG* (a)-(b) and C2*** of K62-M13-A in orientation(1,3),
accepted M13 items1-2. Actual inversion covers(3,1). FULL does not use M13-B/C/D, joint-budget section3 of A, D3/D4 row
certificates, or their objective values. This follows from the literal FULL import/FAM clauses and the following complete
A proof-use expansion (K62-M13-A-v1 LF7-16,18-107):
| A node | inputs actually read | exact output/scope |
|---|---|---|
| A1(a) | LFC(a)-(b), INV/E6 | inverted incidence13n_d/4: O pieces n_d/2, i*3n_d/4; own fibre empty |
| A1(b) | E3 Lemma1 gcd calculation, LFC(c)/Sun4 | <=3 O pieces, <=4 total; a4-piece fibre contains t and i* |
| A1(c) | E3 step3 / SH erratum S2 disjointness argument, L0.1, INV | product sets complement the inverted meeting sets; exact half/quarter measures |
| A1(d)-(e) | A1(a)-(c), elementary incidence sums | missing>=3 on >=n_d/4+1 fibres; >=n_d/4+3 four-piece fibres |
| DG-1* | DG-1 applied to Gamma*, whose conjugated groups are the original U_j | positive n_d/2^r_Q multiple for N*(Q) |
| DG-2* | A1(d), binomial missing-subset double counts (written LF78-84) | N*(O)+A4*<=n_d/4-1, triple/quad sums, N*(O)<=n_d/8-1/2 |
| DG*(a) | DG-1*/2*, own alpha-family hypothesis r_Q<=4 for ALL five four-subsets | N*(O)<=n_d/16; sum_(10 triples)2^-r_R<=19/16-2/n_d |
| DG*(b) | DG*(a), DG-3 G3 written bounds | >=2 deep triples, or exactly1 with r=5,type444,tau16,e_d>=5 |
| C2* | E3 Lemma2 + Z11(a), DG-1*/2*, written pair count LF99-104 | n4(alpha)>=2n1(alpha)+2 |
There are no row-weight/LP certificates on this path. The ten triples/five four-subsets are universal finite index sets in
a written counting argument, not a computed coverage import. DG*(b)'s lower bounds10/8 and9/8+1/16 are written, not an LP
optimum. The DAG does not import M13-D3/D4, so no statement about their feasibility/coverage/provenance is needed or asserted.
CUT-v1 LF59,82's 'hand weights re-derived by both reviews' claim is withdrawn, not silently repaired by scalar agreement.

**Parent envelope kept, not erased.** FULL parent erratum-v2 LF7 explicitly retains the accepted transitive closure of
M13-A items1-2, including CAP/RC. We therefore retain a conservative inherited edge from the restricted CAP-C1/RC-i* (and the
common L1/T3/VFC interface) to M13-A in section7, even though A's proof-use table does not read those interfaces. CAP/RC are
registered in section4 below, not broadened to M13-B/C/D or the G-only DT graph results. The M13 parent erratum LF5-20 narrows
C's imports and does not change A's DG*/C2* (FULL parent erratum-v2 LF9-11). **M2 proposed RESOLVED by reachability plus this
explicit conservative envelope; no D-certificate claim survives.**

## 4. K62 literal interfaces, including every restricted retained input (M3a/b)
Standing K62 setting: V={d,i*} disjoint-union O, |O|=5; gcd6 in C={i*}cup O,4 on d-i*,2 on d-O. n_d=2^ed5^hdw_d (no3),
n_i*=4*3^f*5^h*w*, n_c=2*3^fc5^hcw_c; ed>=4,e*=2; at most one higher3 and one5 marker; all w coprime/prime30. No normality,
bounded exponent or cofactor assumption. A 'family x' is an ACTUAL family, x' its actual inverse.
| id | literal retained interface | restrictions and derivation closure |
|---|---|---|
| E1 / L0.3 | I_ij=lcm(n_i,n_j)alpha_ij, alpha positive integer<=g_ij-1; mu(U_iU_j)=alpha/g | disjoint pair, finite quotient; E1 LF12-19 re-proves from Lagrange/product formula/L0.2; no engine |
| E3 | all K62 have ed>=4,e*=2; O-O entries1,2,4 in both families; C2 for x when x'_(di*)=1 | previous section2; C1/C2 are at their own subset/orientation scopes, not extra global exclusions |
| DG-1 | N(Q) positive multiple of n_d/2^min(ed,v2T*_Q), nonempty Q subset O | no distinguished-entry1 hypothesis; proof via a union of double cosets + E3 subset-chain, no normality |
| DG-2 | N(O)+A4<=n_d/4-1; triple sum<=n_d-2+3N(O); quad sum<=n_d/4-1+3N(O) | original configuration with alpha_di*=1; symbolic missing-subset counts |
| DG-3 | delta(R)=1+v2tau, lcm of edge values divides tau<=product of smallest2 | G3 explicitly derives from L0.1/Lagrange, NOT L1/VFC; deep types244/444, tau8 or16 (16 only444) |
| DG-4 | delta(Q)<=delta(R)+v2min_(j in R)x_ej | ADDED vertex e UNMARKED; RAW depth, not arbitrary capped-depth transport; k<=m, not k dividing m |
| DG(a)/(b) | under r_Q<=4 for every4-subset: N(O)<=n_d/16; triple sum<=19/16-2/n_d; >=2 deep triples or one at capped depth EXACTLY5 | x-family requires x'_(di*)=1; G5 corrects arithmetic N(O)>=n_d/8+1/3; G6 gives exactly5. For ed>=5 a deep4-subset remains an alternative until FULL discharges it. No assumption it vanished. |
| CAP-C1 | gcd(n_v,T_x(V minus v)) divides6 | v UNMARKED in O; specified OWN-family entry x_di*=1. Chain d,i*,t,p then unmarked, added k<=3; no general marked-apex conclusion |
| CAP-C2 | gcd(n_i*,T_x(V minus i*)) divides12 (in this setting equals12) | f*=1; both actual families/orientations. CD2: first O-step after d has gcd2,k=1 exactly, including t absent |
| RC-O | feasible x-row weighted sum<=5/6 | v UNMARKED in O; OPPOSITE entry x'_di*=1 (C1 for x'); NONSTRICT, no extra slack/subset grid |
| RC-i* | feasible x-row weighted sum<=11/12 | f*=1; C2 for opposite family; NONSTRICT, no proper-subset/atom grid |
| RC proof context | sum y x/g<=1-1/gcd(n_v,T_x'(V minus v)) | CD3 written light-fibre proof + LFC(a)-(c), INV/E6, L0.1/Lagrange. V2 V4/V7: import ONLY RC-O/RC-i* as pattern rules, not a general numerical pattern bound |
| CAP-62 finite representation | actual configurations map to U62; listed normalized measures/gcds/capped depths are pattern functions | ABSOLUTE indices, counts and unnormalised slacks are NOT pattern functions. No surjectivity, realizability, enumeration or finite coverage/exclusion. The old CAP finite-coverage bridge is not used. |
| M13-A | section3's DG*/C2*, plus section2 A proof closure above | orientation(1,3); DG* retains own-family four-subset hypothesis; (3,1) via actual INV. Other M13 parts excluded from proof-use graph; conservative CAP/RC envelope retained |
| K62X | no full K62 configuration, every orientation/marker placement, arbitrary group | FULL-v1+worker erratum+parent provenance/errata v1/v2; SG/R4S/CIS etc are proved there, not imported from pending MK/M13X/M3R/R2MIX or G-only DT-B/C. GS cross-check only. |

## 5. Common T/VFC/F7, ROW and D23/RICH scopes (M3c)
All common rules refer to pairwise disjoint finite-index left cosets, after R0 if needed. k<=7; every applied local subfamily
has2<=size<=6; no Sun7-in-subgroup or least-order frame is permitted.
| node | literal scope / content | inputs and prohibited broadening |
|---|---|---|
| L1=T1-T3 | triangle L=lcm(n_a,n_b,n_c), T=Ltau; alpha_xy divides ell_z*tau; apex measure tau/(gamma_y alpha_xz), bounded by adjacent pair measures; tau_min=lcm(alpha_xy/gcd(alpha_xy,ell_z)), tau<=tau_max | L0.1/Lagrange, indices; every labelling, opposite-vertex ell. Applies to either actual family, not an invented matrix |
| VFC V1-V4/count | D_j=U_vg_jU_j disjoint from X_j=U_vU_j, muD=q/g,1<=q<=g-alpha; local right-fibre indices q n_j/g; all hereditary subset Sun conditions; unionD avoids U_v | proof reduces actual right traces to disjoint LEFT cosets in U_v. q=alpha* by INV. No relaxation to arbitrary q as a sufficient existence test |
| F7 only | tau_min*g_va >= gamma_v alpha_ab alpha_va implies X_a subset X_b (Y_b subset Y_a) | addendum A1 F7 LF56-67: T3 lower/apex upper force equal finite measures and containment. This imports F7 proof ONLY, NOT RPLP LP/dual/certificates or finite coverage |
| ROW-U / ROW-U-deg | six neighbours all unmarked => entries1,2,4, <=1 one, >=3 fours; proof transfers when every neighbour-label gcd equals corresponding entry gcd | standard class weights from LFC; R3 size<=3, R5<=5, R24<=4 via Sun4/6/5. E8 subset value>=min(N,4). No assertion for an arbitrary marked neighbourhood |
| ROW-1(a)-(c) | five unmarked labels + one odd {3,5}-smooth marked label: k5=0 or5; k3>0=>k3>=3,no4/5,marked entry1/2; if no3/5 on five labels, full ROW-U conclusions | original unmarked-apex theorem; M1 F2 actual unbounded3/5 exponents; marked-apex transfer requires EXACT five-unmarked/one-odd-marked label hypothesis and g=6,LFC(d), as Z2 G2. Not for even marked neighbour |
| ROW-2(a')-(c') | four unmarked labels + separate3^A/5^B labels: k5>0=>all4 and t-entry5; k3>0=>k3>=2,no4/5,t-entry!=4; k3=2=>p-entry3 and equal remaining1/2; no unmarked3/5=>full ROW-U conclusions | K7-35 local proof with K2 arithmetic erratum. PF1 explicitly transfers to marked apex z by its exact six-label gcd matrix; H35's no2-marker hypothesis belongs to the global K7-35 theorem, NOT this transferred local proof |
| D23-CENTER | distinct2/3 centres z,t: no BOTH z-rows4-type; 5-marker anywhere | 4-type means entries1,2,4,<=1 one,>=3 fours; T/F7/VFC/INV and ROW-1 envelope, no computed pattern census |
| D23-MIX | no EITHER z-row4-type when all five W=V minus z,t are unmarked | 5 absent/on z/on t ONLY. Both rows3-type: z-W1,2,3,>=3 threes,zt1/2. Not valid at a third5-marker without D23-a2 |
| D23P | in(a2), both z-rows(b'): >=2 W'-threes, other W' entries1/2,zt!=4; exactly2=>zp3 and equal remaining1/2 | ROW-2 marked transfer+D23-CENTER+T/F7/VFC/INV; no RICH/FG import; unbounded E,A,B |
| RICH G0/FG7/Cor5/6 | G0 product lower bound; in(a1), FG7 marked-first chain for any subset/auxiliary beta<=5; gcd(n_u,T_Q) divides6 for unmarked u notinQ; val<=5 at u inW in both actual families, equality on EVERY occupied fibre | chain scope RF1 and equality RF2 mandatory. Auxiliary beta<=5 statement stays in(a1); it is NOT exported to(a2). E8 weights on subsets remain hereditary with zero-weight labels |
| RICH NO5/R3/TR/CC | no W-W/W-t5; rows with W-three have c3,e2 and S1-S4 only (LOCAL-TEST survivors, not coverage or realization); TR: L_t subset L_z iff D_t subset X_u; CC excludes configuration ONLY if D_t cap D_u=empty for every u inT* | (a1) and actual families; CC separation hypothesis mandatory; D23-MIX/E1/LFC/INV/T/VFC/ROW-U-E8. RF4 records exactly where standard weights are used |
| RICH theorem/TZ/LZ | no T* subset W3 or T subset W3*; TZ(i) cross entries3/4,(ii) properT=>W3empty and cross4,(iii)T=W orT*=W; LZ ifT=W then v2T*_W>=2 (ifzt2,E>=2,v2>=3), so 1-edge graph disconnected | (a1), all actual exponents. Corrected NO5 proof erratum R-1 and RF1-RF9 mandatory. No unrestricted(a2) transfer or excluded abstract-pattern claim |

## 6. TZ/TC/CASE, BRIDGE and TRANSFER exact lists (M3d/e)
**(a1) source scopes and their internal order.** A1-STRUCT section0 triangle/two-four subroutines, W3, E3, PFG-t/CorL,
B, CASEB read RICH/D23-MIX and common rules. W3 removes W-threes in BOTH families; E3 removes t-three. PFG-t/CorL require the
family's OWN <=2-edge graph on W CONNECTED. CorL is a necessary row list, not realization; its '>=2 opposite t-fours'
consequence uses Sun2/3 only, while its full list contains explicit Sun5 clauses. B (c=3 and >=3 W-entries<=2) forces row1224
or2224,E>=2,t-entry4. CASEB assumes T=W,T* proper, gives |T*|=3 and its displayed matrix; its mirror uses actual INV.

TC Lemma is for distinct u,a,j and either actual family: L_j^(u) subset L_a^(u) iff D_j^(a) subset X_u^(a), hence disjoint
from D_u. FG-V is in finite G (R0 lift), at UNMARKED a inW, full VFC union<=5/6 for either actual family. TC.4's R1 row2244|3|2
holds for EVERY E>=1 (the maximal-set display is labelled E>=2); TC rows R3,R4,R5 and1114|c|1 exclusion keep E>=2 at the
A1/A2 import boundary. TC-B assumes CASEB and gives starred2 on the T* triangle and outside pair. TC-P assumes EXACT TC.11
matrix data; OV2 V2.8 supplies its minimal transfer+V4 proof. TC-A22 requires CaseA (T=T*=W) AND exactlytwo W-fours in EACH
family at every W-vertex, every E>=1. It is not the whole CaseA exclusion.

R2 (K23/CELL+all29 repairs) consumes exactly those scopes. TZ(iii) splits into CaseA/B/mirror; A22 removes all-(2,2), K23
classifies the other CaseA degree branches into the refined K2,3 family, CASEB/TC-B/CASEB-T fix the CaseB row. K23's c=3 R4,
R6 equal-four step, distinctness of K3/IN and the S-f triangle proof are its OWN repaired proof steps, not broadened TC
imports. CELL's literal interface is vertex-wise at K,L index3 with LK=G: index(K cap L)=9; a vertex inK with m^L=3 has a
piece of index n_v/3 in every cell of its K-column. Such vertices need NOT occupy distinct K-columns. CELL(ii)/(iii) keep
their actual piece-index and pairwise-disjoint-coset hypotheses; Sun2/3 applies inside K cap L. R2 is(a1) ONLY: it imports
no R3 candidate, and it exports no automatic(a2) closure.

**BRIDGE — the COMPLETE permitted A2.10 list (OV1 LF621-628).** In(a2-no5), W=W'cup{p}, and T,T*,W3,W3* defined with this W:
- Theorem K7-D23-RICH: no T* subset W3 or T subset W3*;
- G0; Cor5/6 WITH occupied-fibre equality at EVERY u inW, both orientations; NO5;
- R3 with S1-S4 as LOCAL-TEST survivors only and CorR3; TR;
- CC UNDER its separation hypothesis; TZ(i)-(iii); LZ.
ONLY these claims transfer. No blanket FG7/auxiliary beta<=5; its uses are replaced by the adapted actual-family chain.
RICH navigation/residue sections do not transfer. Actual(a2-no5) pair parameters<=4: OV2 V2.6 orders z,t then W on every
nonempty Q; empty/singleton specified separately. Prime-to30 part is the product of ORIGINAL w_j and v5T_Q=B[p inQ]. The
auxiliary chain on W is allowed only for beta<=4. Never substitute w'_p=5^B w_p as a prime-to30 part or assume5 notdividingT_W.
FG-a2 itself has precise conditions: at u inW', beta_zt!=5 OR3 notdividing beta_zp OR beta_tp odd; at p, beta_zt!=5 AND beta_zu<=3
onW'. Cor5/6-a2's x-row/equality uses the OPPOSITE actual family's beta. D23-a2 (when x_zt!=5) replaces D23-MIX data; F6's use
of FG-a2(a) is not circular (that chain does not use F6). These restrictions also govern A2X's Unit2/3 consumers.

**TRANSFER — the COMPLETE permitted V2.7 list (OV2 LF183-206).** In(a2-no5) with W=W'cup{p}, RICH replaced by BRIDGE, ONLY:
- A1-STRUCT: CorW3, E3, PFG-t with CorL, B, CASEB, with load-bearing section0 subroutines;
- TC: Lemma TC, FG-V; R1 for allE>=1; R3,R4,R5 and1114|c|1 exclusion EACH for E>=2; TC-B; TC-P for its stated matrix data;
- TC-A22: its theorem, not its navigation section.
NOT transferred: A1-STRUCT sections6-7; TC sections5-6 (including Q_B'); A22 section4; unrestricted FG7 for auxiliary beta<=5.
Any later substantive source erratum requires the transfer audit again. In particular: V2.7(iv) FG-V at p needs beta_zu<=3
onW' (D23P for the actual family); (iv') the2244|3|e,e1/2 equal-fours step uses actual gcd matrix with p's5-part retained, feasible
value5 vectors and Cor5/6-a2 occupied-fibre equality. PFG-t uses gcd(n_t,T_W)=6, NOT the false5-freeT_W assertion. CC retains
separation; all local indices use ACTUAL q=x*<=4, never an arbitrary formal vector. These are the permitted input interfaces,
not a general substitution of(a1) by(a2).

A2X now joins separately reviewed Units1/2/3: Unit1 imports only common foundations and PROVES wider-scope row/cell tools
under explicit H_A/G_z/G_t hypotheses; Unit2 imports F/FG-a2/D23-a2/S1-S5 and proves the normalised zt5 bounds; Unit3 consumes
them plus the restricted BRIDGE/TRANSFER. It does not transfer R2's(a1) theorem wholesale. The accepted A2X verdict and unit
errata retain this acyclic order and keep the p-marker in every label.

## 7. Expanded topological dependency order (M3f)
This is the proposed retained import graph at theorem/lemma-module granularity, not a claim that any black-box has no
proof. Each module's external inputs are listed; internal steps of E3/M13-A and BRIDGE/TRANSFER are expanded above. Each
predecessor is EARLIER in the table. 'E' includes elementary finite-group actions, Lagrange, product/coset criterion and
index arithmetic; no mathematical engine, LP output or enumeration is hidden in E. 'Sun<=6' is E's Sun2+Zhu+S5W/S6W, the
last two still CONDITIONAL on S56W here. The historical graph has old Sun5/6 at exactly those theorem leaves instead.
| order | node | predecessors (external imports) |
|---|---|---|
| 01 | E: elementary group/index facts, Sun2 | none |
| 02 | Zhu Sun3/Sun4 | classical external |
| 03 | R0 (finite core quotient, preserving intersections/conjugation) | E |
| 04 | E1/L0.3 pair identities/ranges | E |
| 05 | L1/T1-T3/tau bounds | E,E1 |
| 06 | F7 forced containment ONLY | L1,E1 |
| 07 | INV/E6/E7,q=alpha* | E,E1 (VFC's q is a definition, not a proof-cycle) |
| 08 | Prop4.5 exact tuple(2r1,4r2,4r3,4r4),r1odd | E,R0,E1,L1,elementary L3/K2 WITH disjointness (S56W sections2-3) |
| 09 | H5/Core(5), C5W | E,R0,ZhuSun3; own restricted fibre count/INV re-proved, NOT generalLFC |
| 10 | H6/Core5(6), C56W | E,R0,ZhuSun3/4; own restricted fibre count/INV re-proved, NOT H5/generalLFC |
| 11 | S56W R1(5) | E |
| 12 | S56W R1(6) | E |
| 13 | S5W | R0,R1(5),Prop4.5,H5,ZhuSun3/4 |
| 14 | S6W | R0,R1(6),Prop4.5,H5,H6,ZhuSun3/4 (optional S5W route uses the same earlier inputs) |
| 15 | LFC(a)-(d), including E2/E3 | E,R0,E1,ZhuSun3/4,S5W,S6W |
| 16 | VFC(V1)-(V4)/count | E,R0,E1,ZhuSun3/4,S5W,S6W; q identification by INV |
| 17 | ROW-U/ROW-U-deg, standard weights/E8 | LFC,E1 |
| 18 | ROW-1, M1 F2/F3/F5 | LFC,ROW-U/degree,E8 |
| 19 | ROW-1-deg (Z2 G2 local transfer) | ROW-1,LFC,E1 |
| 20 | ROW-2 with K2 correction, PF1 marked-apex transfer | LFC,ROW-U/degree,E8; conservative K7-35 import envelope ROW-1-deg |
| 21 | K7-M0 | ROW-U,INV,R0 |
| 22 | K7-M1 | ROW-1,ROW-U,INV,R0 |
| 23 | K7-Z2 | ROW-1-deg,ROW-U,LFC,INV,L1,F7,VFC,R0 |
| 24 | K7-35 | ROW-2,ROW-1-deg,ROW-U,INV,R0 |
| 25 | K7-U1 | ROW-U,LFC,INV,L1,F7,VFC,R0; its even-marker row proof is inline (not ROW-1) |
| 26 | K7-Z23-P5 | ROW-1-deg,ROW-U,LFC,INV,L1,F7,VFC,R0; CROSS/LIGHT re-proved at own scope |
| 27 | D23-CENTER | LFC,INV,L1,F7,VFC,R0; conservative header ROW-1-deg/ROW-U |
| 28 | D23-MIX/3-type row dichotomy | D23-CENTER,ROW-1-deg,LFC,INV,L1,F7,VFC |
| 29 | RICH G0, FG7 chain, Cor5/6 + equality | E,R0,E1,LFC,INV; actual/auxiliary(a1) scope |
| 30 | RICH NO5 -> R3/CorR3 -> TR/CC -> theorem -> TZ/LZ | D23-MIX,previous RICH chain,ROW-U/E8,LFC,INV,L1,VFC; NO5 R-1 and RF1-RF9 overlays |
| 31 | D23P | D23-CENTER,ROW-2 marked transfer,LFC,INV,L1,F7,VFC,R0 |
| 32 | A1-STRUCT section0/W3/E3/PFG-t/CorL/B/CASEB | RICH module,LFC,INV,L1,VFC,ROW-U/E8 |
| 33 | TC transfer, FG-V, rows, TC-B, scoped TC-P | A1-STRUCT,RICH,LFC,INV,L1,VFC; OV1 then OV2 |
| 34 | TC-A22 | A1-STRUCT,RICH,TC (R1 allE),LFC,INV,VFC |
| 35 | FG-a2 chain, Cor5/6-a2 | E,E1,LFC,INV,RICH G0/Cor5/6 proof,D23P for the p-interface |
| 36 | A2 LemmaF preliminary F1-F5 | D23P,LFC,INV,ROW-U/E8 |
| 37 | A2 LemmaF F6/F7, completed no5/zt5 partition | preliminaryF1-F5,FG-a2/Cor5/6-a2,LFC,INV,ROW-U/E8 |
| 38 | D23-a2 | D23P,preliminaryF3,LFC,INV |
| 39 | ZT5 S1-S5 | LemmaF,D23-a2,E,G0,LFC,INV (S5's t,p-first chain is written inline) |
| 40 | BRIDGE A2.10 EXACT list | D23-a2,FG-a2/Cor5/6-a2,RICH proofs,LFC,INV,L1,VFC; no5,OV2 adapted chain |
| 41 | TRANSFER V2.7 EXACT list | BRIDGE,A1-STRUCT,TC,TC-A22,FG-a2,D23P; no5/actual family restrictions |
| 42 | K23/CASEB-T | A1-STRUCT,TC,TC-A22,RICH,LFC,INV,L1,VFC,R0; all R2-specific repairs |
| 43 | CELL EQ/SUB/IN/vertex-CELL, CELL-A/B | K23,A1-STRUCT,TC,RICH,E,E1,LFC,INV,VFC,ZhuSun3,R0 |
| 44 | (a1) closure | RICH TZ(iii),TC-A22,K23/CASEB-T,CELL,TC-B,INV,R0 |
| 45 | K7-NF | M0,M1,Z2,K7-35,U1,Z23-P5,R0; marker partition only |
| 46 | K7-REM | K7-NF,(a1) closure |
| 47 | A2 Unit1 wider row/cell/H_A tools | E,E1,R0,LFC,INV,VFC,L1,ZhuSun3/4; its G_z/G_t/CL are hypotheses, no Unit2/3 import |
| 48 | A2 Unit2 normalised S-setting | E,E1,R0,LFC,INV,VFC,L1,FG-a2,LemmaF,D23-a2,ZT5; no Unit1/3 import |
| 49 | A2 Unit3 no5/zt5 consumers+join | Unit1,Unit2,LemmaF,FG-a2,D23-a2,BRIDGE,TRANSFER,E,R0,LFC,INV,VFC,L1 |
| 50 | A2X at accepted inherited scope | Unit1,Unit2,Unit3 + mandatory parent unit errata; no R2 theorem as an(a2) premise |
| 51 | full K7 exclusion | K7-REM,A2X |
| 52 | K62 E3 Lemmas1-3/theorem/C1/C2 | E,E1,R0,LFC,INV; section2 proof-path audit |
| 53 | K62 DG-1/2/3/4 | E,E1,E3,LFC,INV; G1 withdraws L1/VFC citations, G3 gives elementary triangles |
| 54 | Theorem DG with G5/G6 | DG-1/2/3, E3; distinguished-entry1/four-subset hypotheses retained |
| 55 | CAP-C1/C2 | E,E1,E3,INV; their explicit chains; CD2 first O-step; finite-representation metadata not a premise |
| 56 | RC-O/RC-i* interfaces | CAP-C1/C2,E,E1,LFC(a)-(c),INV; no general RC-pattern rule |
| 57 | M13-A items1-2 DG*/C2* | E,E1,R0,LFC,INV,E3,DG-1/2/3,TheoremDG G5/G6; conservative inherited envelope L1/T3,VFC,CAP-C1/RC-i* |
| 58 | K62X | E,E1,R0,LFC,INV,VFC,E3,TheoremDG,M13-A items1-2; FULL's SG/graphs written inline, no M13B-D/DTB-C import |
| 59 | K63-D | E,E1,R0,LFC,INV,ROW-U/degree/E8; mandatory D/H repairs |
| 60 | K63-E | E,E1,R0,LFC,INV,ROW-U/degree/E8; mandatory J repairs; K63-D setting only |
| 61 | K63-RES | E,E1,R0,LFC,INV,VFC,Sun<=6; FG/RowLemma written inline, TG/CLIQUE broadening withdrawn |
| 62 | full K63 exclusion | K63-D,K63-E,K63-RES,exact f_d/2-marker partition |
| 63 | KIIW | E,R0,ZhuSun3; its own FC23/INV, no general LFC or StageB |
| 64 | K52W | E,R0,ZhuSun4; its own FC24/INV, no general LFC or StageB |
| 65 | X1 written exclusion | E,E1,R0,L1,its own pairwise fibre bound/Sun2; no general LFC/Sun3-6 |
| 66 | Sun7 six-class reduction | E,R0,E1,ZhuSun3/4,Prop4.5,S5W,S6W,VFC and written D2/D2' |
| 67 | K5.3 exclusion | six-class definition/deletion bridge (addendum LF159),X1 |
| 68 | SUN7-COND | six-class reduction,K7 exclusion,K62X,fullK63,K52W,K5.3 exclusion,KIIW |
No module above imports node68 or Sun7. In particular S5W/S6W do not import general LFC/ROW; A2 Unit1/2 do not import Unit3;
RICH's(a1) proof does not import BRIDGE/TRANSFER; DG's corrected elementary proof does not import M13; CAP-C1/RC do not
import M13. This graph includes the conservative retained CAP/RC envelope, so acyclicity does not depend on pruning it.
Acyclicity is PROPOSED at this literal retained import boundary, subject to checking that no source import was omitted;
this file is not the parent certification of completeness.

## 8. Unchanged clear class scopes, computational disposition and residual gates
| branch | exact accepted interface | disposition |
|---|---|---|
| KII | any seven-coset configuration with all pair gcd<=6 and exactlytwo5-divisible indices, arbitrary group | KIIW replaces StageB KII, elementary+ZhuSun3 only |
| K5.2* | exact README LF94 matrix: C5 gcd6,d1-d2/d-s gcd4,d-O4 gcd2; all admissible markers/cofactors | K52W replaces exact StageB K52 only; larger D2' stays separately in reduction |
| K5.3 | deletion into(3r1,3r2,6r3,6r4,6r5),r1,r2odd,factorscoprime | written X1+bridge; no generalLFC/StageA |
| K6.3 | f_d=1: D; f_d>=2,no C2-marker: E; f_d>=2,C2-marker: RES | exhaustive3-way split; RES Sun6 six-gcd5 case is a LOAD-BEARING theorem input, replaced only via S6W |
| K7-NF | outside distinct nonempty2/3 markers excluded by M0/M1/Z2/35/U1/Z23P5 | includes absent/coincident/distinct5, all exponents; REM additionally uses(a1), NOT A2X |
Every Sun5/6 use is still an import until S56W is accepted and the substitution is adopted. We do not erase it because a
new proof has smaller direct Sun uses. No claim that 'only two computational dependencies existed' is made by scanning
verdict labels. Instead the proposed graph exposes the retained scientific premises. E3's diagnostic is disposed by its
proof path; M13-D certificates by actual nonreachability. LFC parent controls, K63-RES controls and other exploratory
checks remain non-premises only at the explicitly recorded accepted boundaries, not by analogy to E3 or certificate names.

Proposed finding dispositions: M1 proof-path resolved; M2 reachable-A closure resolved/no D-certificate claim; M3a-f supplied
literal interfaces and expanded ordering; m1 wording/disjointness fixed. ALL are CANDIDATE_UNVERIFIED audit repairs until
parent/hostile review. Conditional theorem-statement assembly remains supported; complete expanded-written-chain/no-hidden-
computation certification remains WITHHELD. Remaining full-result gates: S56W composition parent verdict; independent
review of this expanded CUT; final Sun7 composition/quantifiers; inherited process and formal/human/priority boundaries.
Historical records retain their original acceptance/computer-assisted/process labels; no old record is rewritten.
