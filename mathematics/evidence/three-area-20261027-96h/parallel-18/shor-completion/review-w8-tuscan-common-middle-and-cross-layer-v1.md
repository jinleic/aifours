# w8 — Tuscan common-middle and cross-layer v2–v4: full written review

Reviewer **MathShor-2 / math-5**; author slot **info-4, InfoRecursiveMDS18-2**.
Actual `/bin/date` before writing: **Tue Oct 27 15:03:35 PDT 2026**.

## Scope, coverage and assurance

I read the complete frozen manifest, then every line of the sole literal packet in contiguous raw windows **1–225 and 226–376**, including every ending. Sources:
- **S1**, 37 LF: exact literal modern T2 definition and controls, SHA256 6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c.
- **S2**, 144 LF: v2 common-middle Laplacian, SHA256 8dec8f35e53114009c9e2f10f2e37f54ec078af002133e6779d324fa3f2c1b97.
- **S3**, 95 LF: v3 cross-layer overlap, SHA256 0cbe329eaf589fe0a4aa8ed7465355676c7eed37c616e45ad741776b9b51279a.
- **S4**, 84 LF: v4 reciprocity, SHA256 94ec05b2ac521136ac08c633513afe5ee9143f957669d2767b15c346f5b5036c.

All verdicts below are fresh exact WRITTEN reconstructions from those literals, not inherited confidence. No other source, old body, author contact, execution, interpreter/CAS/calculator, selected numeric/control probe, finite search, solver, build/test or nested agent. The fixed original n=11 specializations are symbolic consequences of proved formulas, not scientific tests.
Prior cross-domain exposure and all old owner/reviewer findings/quarantines remain; I claim neither blindness nor clean cognition/independent-family provenance. I performed no historical-contact lookup. Own Shor primary reasoning was paused for this bounded duty, and none of the Tuscan statements is a Shor premise.
The context is the supplied first-party modern definition: n actual LINEAR permutation rows, exact directed distance-one coverage and directed distance-two noncollision. There is no wraparound, Latin-column condition or assumed regularity of the missing-distance-two graph. No book-pixel authentication or current-openness certification is added.

## Summary verdicts

| Source / claim group | Mathematics | Dependency/application | Findings |
|---|---|---|---|
| S2 v2: identity, connectivity, regularity, n=11 and cuts | **NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE** | Supported as necessary common-row constraints only | 0 FATAL / 0 MAJOR / 0 MINOR |
| S3 v3: column transport, odd-order capacity and pair-level sharpness | **NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE** | Supported; sharp pair is not a full-array construction | 0/0/0 |
| S4 v4: reciprocal inequalities and extreme-overlap refinement | **NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE** | Supported at the distinct pair/global antecedents stated | 0/0/0 |

There is no asserted converse from these graph/count conditions to actual rows. The original eleven-row existence/impossibility question is not decided.

## 1. S2 v2: exact common-middle identity

**S2 LF17–67 — reconstructed.** For one actual consecutive triple (a,b,c), put u=f(a)-f(b), v=f(c)-f(b). Then

    2uv=(f(a)-f(b))^2+(f(b)-f(c))^2-(f(a)-f(c))^2.

Every interior adjacency occupies two consecutive triples, while the first and last adjacency occupy exactly one each. Every distance-two event has exactly its own middle occurrence and belongs to one triple. Thus

    2Q=2E1-EB-E2.

Distance-one events cover all ordered distinct pairs, and distance-two events are distinct with n missing ordered pairs. Therefore `E2=E1-EM`, and the disjoint adjacency sets B,I give `E1-EB=EI`. Hence

    2Q=EI+EM.                                             (CM)

This counts boundary events rather than treating every adjacency as having multiplicity two. Every difference uses the SAME actual triple and middle; independent distance-layer margins cannot supply that multiplicity proof.
The identity applies to every real f simultaneously. Since rows are permutations there are no repeated labels within a triple or loop events. The stated n>=3 identity boundary and n>=5 strictness boundary are kept separate.

## 2. S2 v2: interior connectivity and exact Laplacian

**S2 LF69–114 — reconstructed.** Each symbol occurs in n rows and has exactly n-1 outgoing adjacency events, so it is last once; similarly it is first once. These are distinct occurrences.
For a cut of size k with no interior edge, all `2k(n-k)` oriented adjacency pairs crossing it must belong to B, whose size is 2n. If 2<=k<=n-2, then

    2k(n-k)>=4(n-2)>2n    for n>=5,

impossible. If one side is a singleton x, its total directed adjacency incidence is `2(n-1)`. Boundary incidences are at most n+2: two from its first/last occurrences and at most n from second/penultimate positions, which are distinct within a row here. Since `n+2<2(n-1)` for n>=5, an interior incidence exists. The bound is loose but sufficient; it is not an assumed endpoint distribution. Thus I is connected.
Forget orientation but retain every directed I and M event as a separate undirected edge. Its energy is `f^T L_G f=EI+EM`, so `Q=(1/2)f^T L_G f`. The I-subgraph is connected, hence the kernel is exactly the constants and every nonconstant f has Q(f)>0.
In the original triple product expansion, only the common middle contributes a square term. Each symbol is middle in n-2 occurrences, so the quadratic-form matrix has diagonal n-2. Comparison with L_G/2 gives degree `2(n-2)` at every vertex of G. This is a conclusion about the combined multigraph, NOT regularity of M.
For an unordered pair, its two orientations contribute `2-b_xy` interior edges and `m_xy` missing edges, giving multiplicity `g_xy=2-b_xy+m_xy`, between zero and four. Opposite orientations or an I/M overlap are retained as parallel edges. Off-diagonal signs and zero row sums agree with the Laplacian.
At n=11: I has `n(n-3)=88` events; M has 11; G has `n(n-2)=99` edges, degree 18, and Q's matrix has diagonal 9 and rank 10. The zero-sum nonzero real subspace contains no constants and has strict positivity. No stronger support or missing-graph claim follows.

## 3. S2 v2: subset cuts

**S2 LF116–138 — reconstructed.** At f=1_A, a triple product is one exactly when both outer labels lie on one side and the middle on the other, and zero otherwise. Thus Q=Alt(A). The total oriented cut energy is `2|A|(n-|A|)`, yielding

    2 Alt(A)+Bcut(A)=2|A|(n-|A|)+Mcut(A).

Since Bcut<=2n and Mcut>=0, `Alt(A)>=|A|(n-|A|)-n`. Connectivity makes Alt(A)>=1 for every proper nonempty cut at n>=5. At a singleton x, only its n-2 internal middle occurrences contribute, proving the exact singleton value n-2.
These equations hold for all subsets of ONE array simultaneously; they are not independently satisfiable cut certificates offered as a converse.

## 4. S3 v3: exact transport and odd-order overlap bound

**S3 LF15–61 — reconstructed.** Each row s has n-2 distinct D2 events. Exact D1 coverage assigns each to one actual row r. It cannot be s: in a single permutation row the same two symbols cannot be both adjacent and separated by one position. Hence C_ss=0 and each column sums to n-2.
For odd n, write source row s=(x1,...,x_n). Its D2 edges are the odd-index path O=(x1,x3,...,x_n) and the even-index path E=(x2,x4,...,x_(n-1)). If r contained all n-2 edges as adjacency events, these paths would be contiguous blocks in r, necessarily in order OE or EO. The first order repeats s's first symbol as a row start, and the second repeats its last symbol as a row end. Global endpoint uniqueness excludes both. Therefore C_rs<=n-3 for distinct rows.
At n=11, an entire column has nine events, zero diagonal and entries at most eight, so at least two other actual rows supply its events. The argument needs the global endpoint-ownership fact, not merely two arbitrary locally collision-free Hamilton paths.

## 5. S3 v3: full universal pair-level sharpness family

**S3 LF63–83 — reconstructed at its exact pair scope.** Let n=2m+1>=5 and 1<=k<=m-1. The proposed row r is

    (x2,x4,...,x_(2k), x1,x3,...,x_n,
     x_(2k+2),x_(2k+4),...,x_(2m)).

The three blocks are nonempty and use every symbol once. Relative to D2(s), all odd-path edges remain, and the even path loses exactly one edge. The two splices change index parity, so neither adds a D2(s) edge. Hence C_rs=n-3.
No D1(s) edge appears in D1(r): within a block the index increases by two, while both splices decrease the index. No D2(s) event appears in D2(r): inside a block its index difference is four; crossing one splice gives opposite index parities; a two-step event cannot cross both splices because the middle odd block has m+1>=3 vertices. This also covers a singleton initial/final even block at extreme permitted k. The starts x2 versus x1 and ends x_(n-1) versus x_n are distinct.
Thus the bound cannot be improved using only the stated two-row collision and endpoint conditions. No extension of these two rows to an original n-row array is asserted or supplied.

## 6. S4 v4: general reciprocal capacity, including endpoints

**S4 LF25–45 — reconstructed for ANY two actual permutation rows, n>=3.** Call r's adjacent edges good when they belong to D2(s); let `b=n-1-C_rs` be the number of other edges. Two consecutive good edges in r would have s-positions j,j+2,j+4. Their outer pair is therefore not an adjacency of s. Every event counted by C_sr must use at least one other edge of r.
Each interior adjacent edge is in two legal triples and each boundary edge in one. Consequently

    C_sr<=2b,
    2C_rs+C_sr<=2(n-1).

Exchanging r,s gives the reverse inequality; addition yields `3(C_rs+C_sr)<=4(n-1)`. If b_boundary counts the two actual boundary edges that are not good, the precise incidence upper bound is `2b-b_boundary`, proving the optional refinement. A triple with two bad edges is overcounted, which is safe for this upper bound. No cyclic event is inserted.

## 7. S4 v4: maximum odd-order overlap forces reverse overlap at most two

**S4 LF47–69 — reconstructed with all block cases.** Assume original odd n>=5 and C_rs=n-3. Exactly one D2(s) edge is absent from r. Deleting it from the two parity paths leaves three nonempty directed paths. The retained adjacency edges force each path to be contiguous in r, so r is a concatenation of these three blocks. Internal two-step pairs have index difference four, not one.

### Missing edge in the even path

The intact O contains both endpoints of s. Global first/last uniqueness forces it into the middle, with the two split even blocks on either side. At entry into O, crossing two-step events end at x1 or x3. The one ending at x1 cannot be a forward index-one pair; the other can be such a pair only when it starts at x2. Hence at most one. At exit from O, events start at x_(n-2) or x_n; only the first could be followed by x_(n-1), again at most one. O has at least three vertices, so no triple crosses both splices. Total at most two.

### Missing edge in the odd path

Let A=O1 start at x1, B=O2 end at x_n, and E be the intact even path. Endpoint uniqueness excludes A first and B last. Exactly the following block orders remain:

    B E A,    B A E,    E B A.

In B E A, each available crossing two-step pair has source-index difference `4-n`, which is negative for n>=5; E has at least two vertices, so no triple crosses both splices. The contribution is zero.
In B A E or E B A, the odd/odd splice yields no index-one pair, because its outer indices have the same parity. The sole odd/even splice contributes at most two crossing triples. A further triple could cross both splices only if the middle odd block were a singleton. If A={x1}, the A-to-E adjacency x1->x2 repeats D1(s); if B={x_n}, the E-to-B adjacency x_(n-1)->x_n repeats D1(s). Original D1 noncollision excludes both. Thus there is no additional event, and C_sr<=2 in all cases.
This refinement uses the full array's endpoint uniqueness and its pairwise D1 noncollision. It is not claimed for arbitrary two unconstrained permutations.

At n=11 this gives `2C_rs+C_sr<=20` and its reverse, `C_rs+C_sr<=13` by the integer consequence of `3 sum<=40`, and `C_rs=8 => C_sr<=2`. These are simultaneous necessary common-array conditions, not independent transport-matrix realization certificates.

## 8. Dependencies, exact limits and final decision

All load-bearing claims reconstruct from S1's literal actual-row definition and explicitly supplied proofs, with elementary finite double counting, graph connectivity, quadratic-form energy and directed-path order. S4's use of S3 is paid by the complete S3 reconstruction. No specialized theorem or historical numerical import is missing.
The authors reference v1 Lemmas1–3 as an earlier full row-realization equivalence. That body is not supplied here and I give it **no fresh verdict**; none of the necessary claims reviewed above consumes its converse. No gap is silently filled by a hash or another source.
Connected regular G, positive Q, compatible cut data or feasible C alone do not give actual rows. These sources claim no such sufficiency, actual eleven-row witness, universal impossibility, support exclusion, book equivalence or current-status/novelty theorem. Their common-row and exact-boundary assumptions must remain attached to every caller.

**FINAL: NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE for each of S2 v2, S3 v3 and S4 v4. Total mathematical findings: 0 FATAL / 0 MAJOR / 0 MINOR.** Same-harness WRITTEN review only; not formal/kernel, executed, human, independent-model-family or novelty acceptance. All prior process findings, HOLD, ZERO quarantines, N4 UNKNOWN/historical exit unestablished and aux214 STOP remain.

**END OF COMPLETE w8 REVIEW.**
