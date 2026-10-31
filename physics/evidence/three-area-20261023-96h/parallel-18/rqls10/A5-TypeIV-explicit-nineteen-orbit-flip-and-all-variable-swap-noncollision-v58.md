# RQLS10 v58 — ALL19 TypeIV orbit coordinates, explicit flip, and exact swapped-cell noncollision budgets

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW complete manuscript: **Mon Oct 26 13:57:48 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact graph-orbit/parity/linear-algebra proof only, NOT machine/kernel checked. No scientific Eval/interpreter/arithmetic/CAS/program/enumeration/solver/replay/newGO/private approximate scout/backconversion. Earlier permitted metadataJSONassembly has its own exact characterization; no blanket execution/cognition census is asserted.

## 1. Scope: the ENTIRE all-variable TypeIV algebra, not a new chosen control

Import the COMPLETE ordinaryTypeIV master v31 and the COMPLETE flip theorem v34: physicalHspace is C^10 on the duads of{1,2,3,4,5}, with naturalA5 action, a0={1,2}, H=Stab(a0)=S3, and A=Comm(U(H)) has complexdimension19. Every allowed reference seed is an ARBITRARY unitary V inA. The actual row/column condition is V and F(V) bothunitary; arbitraryLatinL/fullresolution and ALL100ray inequalities remain separate.

We now expand the ENTIRE19-complex-dimensional algebra and F exactly, without any chosen matrix/control/ansatz, root alphabet, coefficient restriction or scientific program. This is still an explicitlyA5-covariant model, NOT WLOG for the original problem. No premise from the Gaussian/tenthrootpair branch or its publishedclassifier is used.

## 2. Complete intrinsic labeling of ALL19 triple-duad orbits

Use three ORDERED duads(a,b,c): originalrow, originalcolumn, physicalcoordinate. View distinctduads as edges ofK5. For exactlyTWOequal duads let r=D for disjointness of the unequal edges, r=I for intersection. Assign labels

    h:       a=b=c;
    X_r:     a=b!=c;
    Y_r:     a=c!=b;
    Z_r:     b=c!=a.

For allTHREEdistinct, the three-edge graph is exactlyONE of: triangle; three-star; four-vertexpath; or adjacenttwo-edgepath plus an isolatededge. Three disjointedges would need6vertices and are impossible. Set

    T:       triangle;
    S_+,S_-: three-star, with orientationbelow;
    P_a^+,P_a^-,P_b^+,P_b^-,P_c^+,P_c^-:
             four-vertexpath, subscript is its MIDDLEedge label;
    E_a,E_b,E_c:
             adjacentpair plus isolatededge, subscript is ISOLATEDedge label.

For a star with center s and leaves l_a,l_b,l_c on its respectivelylabelededges, let z be the remaining fifthpoint. Its orientation is the parity+/- of(s,l_a,l_b,l_c,z) relative to(1,2,3,4,5).

For a path, orient its fourvertices(u0,u1,u2,u3) from the endpoint lying in the SMALLER-labeled endedge to the endpoint in the LARGER-labeled endedge, using fixed labelorder a<b<c. Append the unused fifthpointz. Its orientation is the parity of(u0,u1,u2,u3,z).

These labels are A5-invariant. They are COMPLETE: for each labeledgraph type S5 acts transitively. In the triangle case, the transposition of the two unusedvertices is an ODD pointwiseedge stabilizer, so its S5orbit does NOT split underA5. The isolatededge case similarly has the ODDswap of its endpoints. A labeledstar or labeledpath has trivial pointwiseedge stabilizer, so its S5orbit splits into EXACTLYTWO A5orbits, separated by the defined parity. Exactlytwoequal disjointedges have stabilizerC2xC2 inS5, with evenpartC2; intersectingedges have an oddswap of their two unusedpoints, with trivial evenpart. Allthreeequal has stabilizerS2xS3 with evenpartS3. This exhausts all cases.

For fixed a=a0, orbit sizes of(b,c) are1 forh,3 foreachDlabel,6 foreachIlabel, and6 forEVERYall-distinctlabel. Thus the reference counts sum

    1+3*3+3*6+12*6=100,

and the number of labels is1+6+1+2+6+3=19. This is a written orbit proof, not a computer enumeration.

For ARBITRARY19complex coefficients z_l define the ACTUALfull10-by-10 matrix

    V(z)[c,b]=z_{label(a0,b,c)}.                 (ENTRY)

Each H-invariant matrixentry function is constant on exactly theseorbits, so(ENTRY) is a bijection C^19->A. No further coordinate is missing.

## 3. Full flip and matrix-adjoint tables;13plus and6minus dimensions

Let tau swap the firstTWO edge labels(a,b), and gamma swap the LASTTWO(b,c). The exact coefficient operations are

    F(V(z))=V(z^tau),   (z^tau)_l=z_{tau(l)};
    V(z)*=V(z^gamma_bar), (z^gamma_bar)_l=conj(z_{gamma(l)}).

The COMPLETE tag tables are:

    label       tau(label)       gamma(label)
    h           h                h
    X_r         X_r              Y_r
    Y_r         Z_r              X_r
    Z_r         Y_r              Z_r
    T           T                T
    S_+         S_-              S_-
    S_-         S_+              S_+
    P_a^eps     P_b^eps          P_a^eps
    P_b^eps     P_a^eps          P_c^eps
    P_c^eps     P_c^eps          P_b^eps
    E_a         E_b              E_a
    E_b         E_a              E_c
    E_c         E_c              E_b

Here r ranges overBOTH D,I and eps overBOTH+,-; this notation includesEVERYcoordinate. The tauformula follows from Q(F(V))_(a,b)=Q(V)_(b,a), alreadyprovedinv34. The gammaformula is the ordinary matrix-adjoint swap of b,c in(ENTRY).

For the orientation signs: a star swaps two specifiedleaves under eithertransposition, hence changesparity. On a path with middlec, tau reverses its fourvertexorder, an EVENpermutation, so its sign isunchanged. If the middlea/b labels interchange, the rule for the smaller endedge keeps the same vertexorder. The corresponding gamma cases are the same, with middlea fixed by evenreversal and middleb/c exchanged. This proves every orientation entry, not just the unlabeledgraph cases.

Consequently tau has SIXtranspositions: (Y_D,Z_D),(Y_I,Z_I),(S_+,S_-),(P_a^+,P_b^+),(P_a^-,P_b^-),(E_a,E_b), and SEVENfixedlabels. Thus F has complex(+1)-eigenspace dimension13 and(-1)-eigenspace dimension6. Hilbert-Schmidt coefficient weights are the orbit sizes insection2, matching across all exchangedpairs; this also explicitly exhibits its Hilbert-Schmidt isometry.

The COMPLETE all-variable row/column system can now be written without any groupconjugation matrices:

    V(z)* V(z)=I_10,
    V(z^tau)* V(z^tau)=I_10,                    (BI)

with EVERYentry given by(ENTRY). This is an exact coordinate form of the fullmaster, not a claim that diagonal normequations alone replace(BI).

## 4. General norm identities and the TWO actual relation classes

For any solution of(BI), the firstcolumn ofV, firstrow ofV, and firstrow ofF(V) give respectively

    |h|^2+3|X_D|^2+6|X_I|^2=1,
    |h|^2+3|Y_D|^2+6|Y_I|^2=1,
    |h|^2+3|Z_D|^2+6|Z_I|^2=1.                (N0)

For a disjointcolumn b=34, its ten coordinate labels are: Y_D once, Z_D once, E_a twice, E_b twice, and P_c^+,P_c^- eachtwice. Therefore

    |Y_D|^2+|Z_D|^2
      +2(|E_a|^2+|E_b|^2+|P_c^+|^2+|P_c^-|^2)=1. (ND)

For an intersectingcolumn b=13 they are: Y_I,Z_I,E_c,T onceeach; S_+,S_- onceeach; and P_a^+,P_a^-,P_b^+,P_b^- onceeach. Thus

    |Y_I|^2+|Z_I|^2+|E_c|^2+|T|^2
      +|S_+|^2+|S_-|^2
      +|P_a^+|^2+|P_a^-|^2+|P_b^+|^2+|P_b^-|^2=1. (NI)

These multiplicities follow directly from the edgeclass definitions. For b=34 the four c meeting botha0,b are paths with middlec, twoofeachparity; the two remaining intersecting c isolate b. For b=13, the unusedpointswap4<->5 pairs oppositeparities within each star/path case. The remainingnorm equations follow by the COMPLETEtau/gammatables. They remain NECESSARY normbudgets only; all offdiagonal equations of(BI) are still required.

## 5. Exact all-variable obstruction to swapped-cell ray collisions

Put V_-=(V-F(V))/2 and use its SIXunrestrictedcomplex coordinates

    u_D=(Y_D-Z_D)/2,       u_I=(Y_I-Z_I)/2,
    u_E=(E_a-E_b)/2,       u_S=(S_+-S_-)/2,
    u_+=(P_a^+-P_b^+)/2,   u_-=(P_a^--P_b^-)/2.

For reference b disjoint or intersecting, define beta_r=||V_- e_b||^2. The completeentry counts/tau table give EXACTLY

    beta_D=2|u_D|^2+4|u_E|^2,
    beta_I=2(|u_I|^2+|u_S|^2+|u_+|^2+|u_-|^2),
    ||V_-||_HS^2=3 beta_D+6 beta_I.              (BETA)

ForD, the twoY/Zcoordinates contribute2|u_D|^2, the twoE_a andtwoE_b coordinates4|u_E|^2, while bothP_c coordinates are taufixed and vanish. ForI, twoY/Zcoordinates, twooppositestarcoordinates, and eachP_a/P_b paritypair contribute the printedterms; E_c andT are taufixed and vanish. This proves the WHOLE formulas in sixcomplexvariables, not a selected-control value.

For ANY distinctduads a,b there is an EVENinvolution g interchanging them: for a=12,b=34 use(13)(24); for a=12,b=13 use(23)(45); conjugacy covers allrelations. Exactvectorcovariance gives

    U(g) q_(a,b)=q_(b,a).

Hence q_+=(q_(a,b)+q_(b,a))/2 and q_-=(q_(a,b)-q_(b,a))/2 are orthogonal +1/-1 eigencomponents of U(g). They have squarednorms1-beta_r andbeta_r. Their rayoverlap is therefore REAL with absolutevalue|1-2beta_r|; that particular pair is nonproportional IFF0<beta_r<1. Consequently ALL swapped-cell pairs are nonproportional IFF

    0<beta_D<1 and 0<beta_I<1                    (SWAP)

A5 transitivity makes eachbeta constant within its relation. Thus(SWAP) is a NECESSARY condition for the originalALL100distinctness inside the ENTIRETypeIV model; it settles EXACTLY the45swapped-cell pair comparisons, NOT the other maximality comparisons.

In particular both(u_D,u_E) and(u_I,u_S,u_+,u_-) must be nonzero vectors, and0<||V_-||_HS^2<9. No maximal solution can lie in eitherpureF-eigenspace. The+eigenspace gives q_(a,b)=q_(b,a), atmost55rays; the-eigenspace has q_(a,a)=0 and cannot even be a QLS. A scalarF-eigenvalue is necessarily+/-1 byF^2=I, so no otherpureeigenbranch was omitted. This is a general necessary symmetry-breaking statement, not a demand to choose a new ansatz/control.

## 6. Remaining original task, live-review scope and assurance

All19coefficients remainfree subject to the COMPLETE(BI), the v32/v33all-scalarphase mixing/rank restrictions, the ENTIREv31 arbitraryLatinL/fullresolution equations and every other strict100-ray comparison. No V,L or original100rayresolvedarray is produced, and no impossibility of thisfullsystem is proved. The newrepresentation does not make covariance or swapped-pair tests WLOG for arbitrary originalarrays.

The parent-confirmed livev151A/B gate remains the IMMUTABLEENTIREv2/asofS55/96claimnodes/9branches. Completev3/asofS57 is a DISTINCTFUTUREjointgate, not an expansion ofv151 or acceptedmetadata/mathematics. This newsource is a further UNREVIEWEDsuccessor and must enter a NEWCOMPLETEcurrentunion, retainingALLoldbranches/independentunrestrictedv50andv33; it inherits no parentverdict. Its mathematics uses ONLY the separateTypeIVv31/v34 sources and ordinary finitegraph/representation/linearalgebra facts, notNRphase5classification orGaussianflat-factorizationclaims.

All unrestricted originalintrinsic10/4+6/5+5remainOPEN. No A5-WLOG, originalwitness/unrestrictedno-go, finitechecker/control/vendor/formal/kernel/family/human/current-openness/noveltypromotion. All oldprocess/mathfindings, v9/v14withdrawals, source/clock/cadencehistories andZERO-creditquarantinespersist. SameHOLD/noGO/18/exclusive-root/30minactualsubstantivecadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark.
