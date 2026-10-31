# f2 independent written review — local classical-neighborhood rigidity

**VERDICT: 0 FATAL / 0 MAJOR / 0 MINOR at the exact declared mathematical scope.** I reconstructed the full nonlinear proof below; no defect was found in the stated metric, all-member quantifiers, actual edge zeros, graph anchors, leakage estimate, or `1/576` substitution. This is same-harness written review plus a SMALL independent exact combinatorial check, NOT a formal/kernel/human/configured-family proof, a universal enumeration, an unrestricted four-family solution, or novelty clearance.

Reviewer InfoResearch96h-2, own info-1 root. Actual native pre-write observation: `Wed Oct 28 17:08:25 PDT 2026`.

## Scope, source and review independence limits

I read the complete 20-line frozen `review-waves/f2-moqls-neighborhood/assignment-v1.json` first, then the WHOLE 141-LF author candidate, including §§8–9 and the ending:

`physics/evidence/three-area-20261027-96h/parallel-18/moqls8/frontier-20261028-uniform-classical-neighborhood-v1.md`, live SHA-256 `12d8a6e3e3c27ff0e5c776a196578a94ed1010f907986680ef74c0e7f42eb8aa`, 141 LF / 14567 bytes. Candidate coordinates below are its literal lines. Author's recorded finite experiment and receipt (lines 122–136) were READ AS CLAIMS, not executed or treated as my independent evidence; the theorem reconstruction does not need their source files.

For any integers n>=2, m>=1 satisfying `2(m+1)>n`, any ACTUAL labelled classical reference m-MOQLS(n), and any ACTUAL labelled complex m-MOQLS(n) Q on the same grid, the claim is: if EVERY member/cell projective chordal distance from its own reference ray is at most `eta=1/[8n(n+1)]`, then each member of Q has a separate unitary sending EVERY labelled cell to the corresponding reference ray, up to independent cell phases. There is no shared output unitary and no assumption that any member of Q is already classical. The theorem is conditional on the existence of the actual classical reference, and excludes a nonclassical actual Q only inside its ball.

I am not the physics-4 author. I had prior same-harness round status and broad cross-domain review exposure, including status-only physics-4 notices, and I previously returned UNCERTAIN on a lifetime exposure screen. This is not a claim of blind, fresh-model, lifetime clean-cognition or independent-vendor review. The present proof uses only the supplied candidate's actual definitions and ordinary linear algebra/combinatorics; no held historical outcome or source is treated as a premise, and no author contact occurred.

## 1. Reference incidence and connectivity, including vacuity

Candidate lines 13–44. In a classical member, each row and column is an ONB and entries are member-specific basis rays. Thus its symbol map is a Latin square, including when the input vectors have arbitrary phases. For a classical pair a,b, two same-cell product rays agree exactly when the corresponding ordered basis-symbol pairs agree; because the n^2 products are an ONB, all n^2 ordered pairs occur exactly once.

Fix member a and distinct reference symbols p,q. The n p-cells and n q-cells each meet every row, column, and every fixed symbol of every companion exactly once. Consequently row, column, and each of m−1 companion-symbol classes define m+1 PERFECT MATCHINGS between the two occurrence sets.

The matchings are pairwise edge-disjoint: a row-plus-column coincidence would be one cell; a row or column plus companion-symbol coincidence would repeat a symbol in that companion Latin row/column; two companion-symbol coincidences would repeat a pair in those two mutually orthogonal reference squares. Hence the union is a simple `(m+1)`-regular bipartite graph on n+n vertices. The degree immediately implies m+1<=n whenever an actual classical reference exists. Thus formally specified pairs with m+1>n have NO such reference and the implication is vacuous; no additional existence is assumed.

Under `2(m+1)>n`, neighborhoods of any two vertices on the same side are subsets of the opposite n vertices with sizes summing to more than n, and therefore intersect. Each same-side vertex is at distance at most two from ANY chosen vertex of that side. In particular it is at distance 0 or 2 from its first-row occurrence. The two first-row anchors themselves are linked by the row matching, so the whole graph is connected. The candidate's same-side anchor argument actually requires only the neighborhood-intersection fact; no classification of Latin nets or expansion estimate is imported. Strict inequality is needed for this proof, and the equality case is not claimed.

## 2. Gauge, phases and actual leakage

Candidate lines 46–67. For each member independently, first rephase each actual first-row vector so its reference overlap is positive real. If projective chordal distance d<=eta, then

    ||v-e||^2 = 2(1-sqrt(1-d^2)) <= 2d^2,

so each column differs by at most `sqrt(2)eta<=2eta`. If F and E are the actual/reference first-row unitaries in column order, then `||F-E||op<=||F-E||F<=2sqrt(n)eta<=2n eta`. The separate unitary `U=E F*` obeys `U F=E` and `||U-I||op=||E-F||op<=2n eta`. Applying U to the entire member preserves all within-member orthogonality; separate local unitaries preserve all pair-product inner-product zero conditions as well.

For any cell, after this unitary its vector is within `2(n+1)eta` of an appropriate reference unit vector. Projection to the complement of its intended reference ray therefore has norm at most this quantity. With

    delta = MAX over all members/cells of this ACTUAL leakage,
    delta <= 2(n+1)eta = 1/(4n) < 1,

the intended coefficient has modulus `sqrt(1-leakage^2)>0`. Rephasing every aligned cell to make that coefficient positive real is legitimate and preserves all zeros; the already aligned first-row coefficients remain +1. This pays the gauge and the common bound for EVERY member/cell, not just a selected vector or a first-order perturbation.

## 3. Every actual graph edge forces the selected-member zero

Candidate lines 69–81. If an edge represents a row or column, the selected member's inner product vanishes by its ACTUAL QLS condition. If it represents a companion reference symbol, both companion vectors have the SAME intended reference ray. Their positive intended coefficients each have modulus at least `sqrt(1-delta^2)` and the product of the complementary norms is at most delta^2. Hence their actual inner product has modulus at least

    (1-delta^2)-delta^2 = 1-2delta^2 > 0.

Orthogonality of the actual same-cell pair-products says the PRODUCT of the selected and companion overlaps is zero. The latter is nonzero, so the selected overlap is exactly zero. This argument remains valid for arbitrary complex vectors and phases, and simultaneously for all classical/quantum mixtures; it is not an appeal to the classical reference overlap alone or to tangent equations.

## 4. Nonlinear potential propagation and contradiction

Candidate lines 83–105. For an edge from a p-cell x to a q-cell y, after the gauge write

    psi_x=a_x e_p + sum_(r!=p)c_(x,r)e_r,
    psi_y=a_y e_q + sum_(r!=q)c_(y,r)e_r,

where `|c_(x,q)|,|c_(y,p)|<=delta`, all complement norms are <=delta and `0<=1-a_x,1-a_y<=delta^2`. The EXACT actual zero expands to

    0=a_x c_(y,p)+a_y conjugate(c_(x,q))
        +sum_(r!=p,q) conjugate(c_(x,r)) c_(y,r).

Cauchy–Schwarz bounds the sum by delta^2, including the n=2 empty-sum case. Replacing the two main coefficients by 1 adds at most 2delta^3. Thus the p-side potential `conjugate(c_(x,q))` and q-side potential `-c_(y,p)` differ on EVERY edge by at most `E=delta^2(1+2delta)`.

For each same side, the first-row occurrence has its relevant potential exactly 0 and every other occurrence is at distance at most 2 from it. Triangle inequality along this actual graph yields every coefficient `|c_(x,q)|<=2E`. Repeating for ALL members, all p and all q!=p and taking a Euclidean norm gives

    delta <= 2 sqrt(n-1) delta^2 (1+2delta).

If delta>0, division gives `1<=2sqrt(n-1)delta(1+2delta)`. But delta<=1/(4n) and sqrt(n−1)<=n imply

    2sqrt(n-1)delta(1+2delta)
       <= 1/2 + 1/(4n) < 1,

for n>=2. Contradiction. Hence delta=0; every aligned cell is exactly its labelled reference basis vector after the existing phases. Undoing each member's own unitary/phase gives the claimed classicality and the stronger labelled correspondence. The endpoint `distance<=eta` is included because the contradiction is strictly below 1 even at its upper bound. No tangent integration or limiting argument is required.

## 5. Boundary accounting, specialization and global ceiling

- n=2,m=1 satisfies the strict degree condition; the cross-component sum in section 4 is empty and the same argument applies.
- n=3,m=1 is also covered; no companion member is needed, and the two row/column matchings have degree 2>3/2. n=3,m=2 is covered when a reference exists.
- Configurations with m+1>n are vacuous because the required simple graph cannot exist. The proof does not claim a reference exists for every allowed integer pair.
- At `2(m+1)=n` or below, the candidate does not claim this theorem; neighborhood-intersection/diameter-two need not follow.
- For n=8,m=4, degree=5 and `2*5>8`; `eta=1/(8*8*9)=1/576`, `delta<=1/32`, and the author's coarse contradiction factor is at most `17/32<1`. A nonclassical family, IF one exists, has distance STRICTLY greater than 1/576 from each labelled classical reference; equality at the radius is excluded by the theorem.
- All members can be quantum a priori; tensor-product constraints are used on the actual family, with independent reference/output bases. Simultaneous row/column relabelings are absorbed by changing the labelled reference. The proof is a local obstruction only: it neither finds an actual nonclassical 4-MOQLS(8), rules one out outside these balls, proves path-connectedness, establishes M(8), derives the five-family theorem, nor establishes a QOA equivalence.

The tangential zero-kernel observation is compatible with this proof but is not used to infer nonlinear rigidity. The author's one GF8 finite control is not promoted into a universal net classification. External priority, stronger assurance, and earlier quarantined lines stay separate.

## 6. Independent exact small-order incidence check

I executed the following bounded Python cell in the session's local Eval runtime, with integer sets and `fractions.Fraction` only, no floats or external model. It generates all Latin squares for n=2,3,4; takes EVERY reduced first square, independently enumerates ordered orthogonal companions, and checks for every member/symbol pair that matching classes are disjoint, graph degrees equal m+1, and every same-side occurrence shares a neighbor with its first-row anchor. Reducing the first square uses row and first-member symbol relabeling; companion squares remain fully labelled. This is a finite diagnostic, NOT a proof for n=8 or arbitrary n.

```python
from itertools import permutations
from fractions import Fraction

def latin(n):
    perms=list(permutations(range(n))); columns=[set() for _ in range(n)]; rows=[]; out=[]
    def build():
        if len(rows)==n:
            out.append(tuple(rows)); return
        for p in perms:
            if any(p[j] in columns[j] for j in range(n)): continue
            rows.append(p)
            for j,x in enumerate(p): columns[j].add(x)
            build()
            for j,x in enumerate(p): columns[j].remove(x)
            rows.pop()
    build(); return out

def orth(A,B,n):
    return len({(A[i][j],B[i][j]) for i in range(n) for j in range(n)})==n*n

def verify_family(F,n):
    m=len(F)
    for a,A in enumerate(F):
        positions=[[i*n+j for i in range(n) for j in range(n) if A[i][j]==v] for v in range(n)]
        for p in range(n):
            for q in range(p+1,n):
                P,Q=positions[p],positions[q]; adj={x:set() for x in P+Q}
                assert len(P)==len(Q)==n
                for x in P:
                    i,j=divmod(x,n)
                    for y in Q:
                        k,l=divmod(y,n)
                        t=int(i==k)+int(j==l)+sum(F[d][i][j]==F[d][k][l] for d in range(m) if d!=a)
                        assert t<=1
                        if t: adj[x].add(y);adj[y].add(x)
                assert all(len(adj[x])==m+1 for x in P+Q)
                for side in (P,Q):
                    anchor=next(x for x in side if x<n)
                    assert all(x==anchor or bool(adj[x]&adj[anchor]) for x in side)
    return m*n*(n-1)//2

for n in (2,3,4):
    L=latin(n)
    reduced=[A for A in L if A[0]==tuple(range(n)) and all(A[i][0]==i for i in range(n))]
    counts={}; graphs={}
    for A in reduced:
        if 2*2>n:
            counts[1]=counts.get(1,0)+1; graphs[1]=graphs.get(1,0)+verify_family((A,),n)
        Bs=[B for B in L if orth(A,B,n)]
        if 2*3>n:
            for B in Bs:
                counts[2]=counts.get(2,0)+1; graphs[2]=graphs.get(2,0)+verify_family((A,B),n)
        if 2*4>n:
            for B in Bs:
                for C in Bs:
                    if orth(B,C,n):
                        counts[3]=counts.get(3,0)+1; graphs[3]=graphs.get(3,0)+verify_family((A,B,C),n)
    print('n=',n,'all_latin=',len(L),'reduced_first=',len(reduced),
          'ordered_families=',counts,'graphs_checked=',graphs)
eta=Fraction(1,8*8*9)
print('n8_m4: eta=',eta,'delta_bound=',2*9*eta,
      'contraction_bound=',Fraction(1,2)+Fraction(1,32))
```

Observed output:

```text
n= 2 all_latin= 2 reduced_first= 1 ordered_families= {1: 1} graphs_checked= {1: 1}
n= 3 all_latin= 12 reduced_first= 1 ordered_families= {1: 1, 2: 6} graphs_checked= {1: 3, 2: 36}
n= 4 all_latin= 576 reduced_first= 4 ordered_families= {2: 48, 3: 1152} graphs_checked= {2: 576, 3: 20736}
n8_m4: eta= 1/576 delta_bound= 1/32 contraction_bound= 17/32
```

These checks test the finite incidence implementation and arithmetic; they do not enumerate genuinely quantum families, reconstruct the author's separate GF8 source/receipt, or verify all n=8 Latin nets. The all-n theorem is supported here by the independent written derivation in §§1–4, not by these counts.

## 7. Exact findings and limitations

No FATAL, MAJOR or MINOR finding at the frozen theorem scope. The reference must be ACTUAL and classical, Q must be ACTUAL and satisfy all within-member and pair-product ONB conditions, the metric is the stated labelled max projective distance, and `2(m+1)>n` is strict. The result is a conditional local-rigidity theorem even when n=8,m=4; it is not a proof of the unrestricted existence/nonexistence target, numerical M(8), novelty, or any stronger assurance gate.

No external source or historical held result was used as a scientific premise; no author contact, nested agent, CLI model, Git, deletion or infrastructure mutation. A parent scientific disposition requires its own complete source/return read; this review's no-defect result is not automatic adoption.
