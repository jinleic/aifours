# Peer reconstruction — RQLS PROJECTOR-INVARIANT v1

Reviewer: PhysicsMOQLS8, temporarily performing the ONE parent-assigned review, then returning to physics-4. Actual clock observed immediately before this record: **2026-10-23T14:18:33-0700**. Written mathematics only; no scientific executable, numerical check, modelCLI or nested agent.

## Snapshot and actual read scope

Author source: `physics/evidence/three-area-20261023-96h/parallel-18/rqls10/candidate-PROJECTOR-INVARIANT-v1.md`.

Observed SHA256: **032a900df29722b71e8806524291e665cb16331c359b5538c7db957958d57ad9**, matching the parent's frozen review assignment. Complete lines1–156 were read. Also read the complete selection and baseline dependency freeze; companion GRAM-CERT TheoremG/explicit extraction at lines7–39; actual Zhang–Cao cached source definitions/theorem at lines76–110 and Lemma2.2 at lines138–165. I did NOT review the companion's real-Nullstellensatz/positive-certificate completeness machinery, and do not certify it here.

## Verdict at the requested scope

**No substantive mathematical defect found: 0 FATAL / 0 MAJOR / 0 MINOR findings.** This is an actual in-harness written reconstruction with the supplied proof and shared definitions, not a blind/cross-vendor/human/formal review. It supports only the listed necessary invariants, exact relaxation obstruction and REAL equality-point exclusion. It does not produce a complex equality lift or maximal 1-RQLS(10).

## Independent reconstruction

### 1. Domain, forced kernel and ranks — source lines7–34

The source definition really supplies three partitions of the100cells into ten exact ONBs each: rows, columns and one arbitrary Latin B resolution. Distinct parallel classes intersect in one cell per line pair. Their contrast spaces each have dimension9 and are mutually orthogonal, and the constant direction is independent. Thus the actual indicator span has dimension28, for EVERY B.

For P_p=q_pq_p* and Q_p=P_p-I/10, an ONB line has sum Q_p=0. Therefore its indicator lies in ker C. This proves rank C<=100-28=72; diagonal C_pp=9/10 gives trace90. Summing all ten row resolutions gives H1=10·1, hence C1=0 and H=C+J/10 has rank<=73. This derivation keeps the operator Gram matrix C distinct from the ordinary vector Gram G. No independence of100projectors was assumed.

### 2. Ordered-pair count and fourth moment — source lines36–63

For each cell the three ONB lines contribute3*9=27 distinct required neighbors. Of the99othercells,72 are line-disjoint. Their squared overlaps sum to10-1=9. Thus

    sum_nonedge (h-1/8)^2
      =sum_nonedge h^2 -(1/4)*9 +72/64
      =sum_nonedge h^2-9/8.

Summing over100rows of H and restoring its100diagonal terms gives100+900/8=425/2. The7200 nonedges and2700 required edges are ORDERED pairs, consistent with the fourth-moment sum over all(p,q). Nonnegative summands give the exact equality condition h=1/8 on every nonedge. Some such overlap is at least1/8, so a finite100-ray configuration has0<eta<=7/8; no attainability is inferred.

The rank derivation agrees: tr(C^2)>=(90^2)/72=225/2, and tr(H^2)=100+tr(C^2). All arithmetic above is displayed written arithmetic, not a program.

### 3. Universal H0 really passes the stated relaxation — source lines65–109

The three line-indicator projections E_c have pairwise product P0=J/100. Therefore their common constant direction plus27contrasts is a direct orthogonal decomposition, and R=I-sum E_c+2P0 is a rank72orthogonal projection. Its entries are18/25 on the diagonal, -2/25 on required edges, and1/50 on nonedges.

Multiplying R by5/4 then adding J/10 gives H0 entries1,0,1/8. Its eigenvalues are10 on constants,0 on27contrasts and5/4 on the72remaining directions. It has rank73, centered rank72, all required line sums, nonnegative entries, strict off-diagonal values below1, and the exact minimum fourth moment. This works independently of the choice of Latin B.

Consequently the stated first-level necessary conditions cannot yield infeasibility: this is a genuine route barrier, not a physical witness. The proof correctly does NOT identify an abstract PSD factor with rank-one Hermitian cell projectors. Equality in the rank argument uniquely fixes C0, since a trace90 PSD operator on a72-space attains225/2 squared trace only with all72eigenvalues5/4.

### 4. Complex equality lift and counts — source lines111–133

Writing G=I+S/sqrt8 and expanding G^2=10G gives S^2=72I+16sqrt2 S. Hermitian symmetry, unit diagonal and this idempotent relation force Gram spectrum0/10 and rank10; required edge zeros supply all30bases. Thus the displayed support/unit-modulus conditions together with this equation really are necessary and sufficient for lifting H0, not for all possible target witnesses.

The common-neighbor counts are correct for every Latin B. Adjacent cells have8othercells on their common line plus two cross-class intersections, totaling10. Nonadjacent cells have the six intersections from distinct coordinate-class choices; Latin uniqueness keeps these distinct. Subtracting unions among the98othercells gives56 and50 line-disjoint common neighbors, respectively. This justifies the source's equation sizes without restricting B to a group table.

### 5. Real-only no-lift boundary — source lines135–143

If the rays admitted representatives that are all real after a common output unitary and individual phases, their Gram matrix in that gauge would be real. Therefore S has signs±1 on nonedges. At a nonedge, the left side of S^2=72I+16sqrt2 S is an integer, whereas the right side off the diagonal is±16sqrt2, impossible.

The independent dimension argument agrees: real centered rank-one projectors lie in traceless Sym(10,R), of dimension55-1=54. Hence real arrays have rank C<=54 and fourth moment at least100+90^2/54=250>425/2. The author correctly leaves arbitrary complex phases and nonuniform complex arrays unaffected. Neither the triangle inequality nor the real obstruction excludes the complex equality point.

## Import, significance and acceptance boundaries

- The actual primary ray/transversal/resolvability definitions match the selection. Order10 remains a named exception in the source theorem; an exception is not a no-go.
- The mathematical argument uses elementary frame/incidence/PSD linear algebra and the locally reconstructed Gram-sufficiency theorem only. Old WH/F-family/E1 numerical or structural results are not premises.
- Items1–3 are standard-method consequences/diagnosed route limits. I found no new existence or universal nonexistence statement and do not promote their novelty or significance.
- No new source completeness, exact witness, kernel replay, scientific execution or runtime admission follows from this review. The unrestricted target, complex equality lift and inherited HOLD obligations remain unresolved.

The author can continue the genuine complex-lift/stronger-invariant obligation; repeating the already feasible first-level relaxation would not advance the target.
