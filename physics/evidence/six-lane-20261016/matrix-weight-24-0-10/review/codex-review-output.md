{
  "verdict": "ACCEPT",
  "constraints_checked": [
    {
      "name": "Index domain and input integrity",
      "pass": true,
      "note": "I(24) = {(i,j,t,p): 0 <= p <= t <= min(i,j), i+j <= 24+t}. Checked all 20,475 indices, including omitted zeros. The 1,616 listed entries have valid integer indices, integer values, and no duplicates."
    },
    {
      "name": "Eq. (38): prescribed weight distribution",
      "pass": true,
      "note": "lambda(i,0,0,0) = lambda(i,i,i,i) = A_i for every i. A_0=1; A_10,A_12,...,A_24 have the eight specified values; all other A_i vanish."
    },
    {
      "name": "Eq. (31): normalization",
      "pass": true,
      "note": "x(0,0,0,0)=1."
    },
    {
      "name": "Eq. (31): anticommutation",
      "pass": true,
      "note": "x(i,j,t,p)=0 whenever t-p is odd."
    },
    {
      "name": "Eq. (31): permutation symmetry",
      "pass": true,
      "note": "x(i,j,t,p)=x(i',j',t',p') whenever t-p=t'-p' is even and (i,j,i+j-t-p) and (i',j',i'+j'-t'-p') are permutations. Checked all 2,265 applicable orbit classes, including zero classes."
    },
    {
      "name": "Eq. (31): projector equations",
      "pass": true,
      "note": "For every r=0,...,24: sum_{i+j-t-p=r} lambda(i,j,t,p) = 2^24 lambda(r,0,0,0). Total lambda is 2^48=281474976710656."
    },
    {
      "name": "Eq. (31): Knill–Laflamme equations",
      "pass": true,
      "note": "For j=1,...,9: sum_{i=0}^{24} K_j(i;24) lambda(i,0,0,0) = 2^24 lambda(j,0,0,0). The PDF explicitly gives 0<j<delta; the HTML extraction truncates this range."
    },
    {
      "name": "Eq. (31): block positivity",
      "pass": true,
      "note": "For every integer a=0,...,24 and k=a,...,floor((24+a)/2), checked M^(a,k) >= 0, where M_ij=sum_{t=max(0,i+j-24)}^{min(i,j)} sum_{p=0}^{t} alpha(i,j,t,p,a,k)x(i,j,t,p), with inclusive row and column indices i,j=k,...,24+a-k. All 169 blocks pass exactly."
    },
    {
      "name": "Eq. (32): purity",
      "pass": true,
      "note": "x(i,j,t,p)=0 whenever {i,j,i+j-t-p} intersects {1,...,9}."
    },
    {
      "name": "Eq. (33): shadow parity",
      "pass": true,
      "note": "For every odd j=1,3,...,23: sum_{i=0}^{24} (-1)^i K_j(i;24) lambda(i,i,i,i)=0."
    },
    {
      "name": "Eq. (33): self-duality",
      "pass": true,
      "note": "For every j=0,...,24: sum_{i=0}^{24} K_j(i;24) lambda(i,i,i,i)=2^24 lambda(j,j,j,j)."
    },
    {
      "name": "Eq. (34): nonnegativity",
      "pass": true,
      "note": "Every x=lambda/gamma is nonnegative."
    },
    {
      "name": "Eq. (34): integrality",
      "pass": true,
      "note": "Every lambda is an integer. Integrality is imposed on lambda, not x."
    },
    {
      "name": "Eq. (35): Type II",
      "pass": true,
      "note": "With logical dimension k=0, sum_{j even} lambda(j,j,j,j)=2^(24-0)=16777216. The Type I alternative is not imposed."
    },
    {
      "name": "Redundant trace and additional LP inequalities",
      "pass": true,
      "note": "sum_i A_i=2^24. Also checked B_j>=A_j and S_j>=0 for every j."
    },
    {
      "name": "Genus-2 MacWilliams identity",
      "pass": true,
      "note": "Independently derived the specified T from the binary symplectic character pairing. Verified W(Tz)=2^48 W(z) coefficient by coefficient over integers, including all 20,475 possible degree-24 monomials. No probabilistic acceptance or saved system matrices were used."
    },
    {
      "name": "Partial genus-2 MacWilliams identity",
      "pass": true,
      "note": "Also independently derived the transform acting on the first codeword and verified W(T1 z)=2^24 W(z) coefficient by coefficient."
    },
    {
      "name": "Two-dimensional-subspace divisibility",
      "pass": true,
      "note": "For independent pairs, put (b,c,e,d)=(j-t,i-t,p,t-p). Under permutation of (b,c,e), a coefficient must be divisible by the stabilizer size, namely the product of factorials of repeated-value multiplicities. All 406 nonzero independent-pair orbit classes pass. Their ordered-pair total divided by six is 46912487729835=(2^24-1)(2^24-2)/6."
    },
    {
      "name": "Joint weight marginals",
      "pass": true,
      "note": "For every i,j, sum_{t,p} lambda(i,j,t,p)=A_i A_j."
    }
  ],
  "independent_verifier_summary": {
    "input": "evidence/lambda_24_0_10.json",
    "sha256": "15a159af1078468defea70d4394f25d896b51d471ed8f2f59453502357fe73e1",
    "execution": "Fresh inline Python, read-only, using fractions.Fraction and integer arithmetic. No lane modules imported, no files written, no network access, no delegation. The independent Eq. (31)–(35) verifier was implemented and run before inspecting the lane's verifier.",
    "primary_sources": [
      "sources/amh-2603.19901v1.txt, Section 3.3 and Appendix A",
      "sources/rational-sdp-2603.19901.txt, PDF transcription",
      "sources/amh-repo/fun.jl, used to resolve the malformed gamma expression"
    ],
    "exact_formulas": {
      "notation": "x(i,j,t,p)=lambda(i,j,t,p)/gamma(i,j,t,p). Binomial C(s,r)=0 unless s>=0 and 0<=r<=s. Terms with zero binomial factors are omitted before evaluating powers.",
      "gamma": "gamma(i,j,t,p)=3^(i+j-t) 2^(t-p) 24! / [p! (t-p)! (i-t)! (j-t)! (24-i-j+t)!].",
      "beta": "beta^{m,t}_{i,j,k}=sum_{u=0}^{m} (-1)^(t-u) C(u,t) C(m-2k,m-k-u) C(m-k-u,i-u) C(m-k-u,j-u).",
      "alpha": "alpha(i,j,t,p,a,k)=beta^{24-a,t-a}_{i-a,j-a,k-a} 3^((i+j)/2-t) sum_{g=0}^{p} (-1)^(a-g) C(a,g) C(t-a,p-g) 2^(t-a-p+g).",
      "Krawtchouk": "K_j(i;24)=sum_{h=0}^{j} (-1)^h 3^(j-h) C(i,h) C(24-i,j-h).",
      "block_dimension": "24+a-2k+1, from inclusive indices k,...,24+a-k.",
      "pair_polynomial": "W(z)=sum lambda(i,j,t,p) z00^(24-i-j+t) z0x^(j-t) zx0^(i-t) zxx^p zxy^(t-p). Coefficients are orbit totals; no additional multinomial factor is inserted."
    },
    "PSD_method": "Exact symmetric Schur elimination, equivalent to LDL^T. Negative pivots fail; a zero pivot requires the remaining corresponding row to vanish. For full blocks, diagonal congruence by diag(3^(i/2)) removes all radicals. Separately repeated the test using the printed alpha directly on the supported even indices; both calculations agree.",
    "PSD_results": {
      "blocks": 169,
      "total_block_rows": 1547,
      "rank_sum": 170,
      "nullity_sum": 1377,
      "rank_histogram": {
        "0": 44,
        "1": 84,
        "2": 37,
        "3": 4
      },
      "engine_controls": "Rejected [[0,1],[1,0]] and [[1,2],[2,1]]; accepted the singular matrix [[1,1],[1,1]]."
    },
    "normalization_control": "Exhaustively counted all 256 ordered label pairs at n=2; all 15 orbit cardinalities agree with gamma."
  },
  "mutation_results": [
    {
      "mutation": "Increase lambda(10,10,0,0) from 405476 to 405477.",
      "rejected": true,
      "failures": "Permutation symmetry, projector equation r=20, five PSD blocks, and genus-2 identity.",
      "PSD_witness": "The rationally congruent block (a,k)=(0,1) has a negative elimination pivot -25/481176247338."
    },
    {
      "mutation": "Swap lambda(10,10,0,0)=405476 and lambda(10,10,1,1)=2095878.",
      "rejected": true,
      "failures": "Permutation symmetry, projector equations r=18 and r=20, ten PSD blocks, and genus-2 identity.",
      "PSD_witness": "The rationally congruent block (a,k)=(0,1) has a negative elimination pivot -1690402/80196041223."
    }
  ],
  "positive_control": {
    "construction": "Constructed the hexacode over GF(4)=F2[w]/(w^2+w+1) from generator rows (1,0,0,1,1,1), (0,1,0,1,w,w^2), (0,0,1,1,w^2,w).",
    "independent_checks": "Enumerated 64 distinct words; checked additive closure and trace-Hermitian orthogonality. Size 2^6 then establishes additive self-duality.",
    "parameters": {
      "n": 6,
      "delta": 4,
      "A": [1, 0, 0, 0, 45, 0, 18]
    },
    "pair_enumeration": "Brute-forced all 4096 ordered pairs, obtaining 17 nonzero matrix weights.",
    "all_constraints_pass": true,
    "PSD": "All 16 blocks pass exactly: eleven rank-zero blocks and five rank-one blocks.",
    "additional_controls": "Full and partial genus-2 identities and subspace divisibility pass. Explicit Pauli multiplication with labels 1=X, w=Z, w+1=Y confirms phase cancellation and Gamma equal to the pair-membership indicator for all 4096 codeword pairs."
  },
  "findings": [
    {
      "severity": "informational",
      "issue": "Eq. (41) is malformed in both supplied text versions: it contains unspecified a_l and an apparent duplicated multinomial/factorial expression.",
      "fix": "State the orbit-cardinality gamma formula explicitly. It follows from Eq. (27), agrees with the authors' gamma_field implementation, and passes exhaustive small-n counting. Acceptance uses this intended normalization."
    },
    {
      "severity": "informational",
      "issue": "The HTML loses Eq. (31)'s Knill–Laflamme index range. Appendix B also describes block sizes without the +1 required by inclusive indices.",
      "fix": "Use the PDF's 0<j<delta range and Eq. (31)'s inclusive block indices. The verifier used all 169 full blocks with dimension 24+a-2k+1."
    },
    {
      "severity": "informational",
      "issue": "Passing these constraints does not establish realizability by a stabilizer code. Integrality of orbit totals does not restore information discarded by the relaxation.",
      "fix": "Retain the lane's explicit restriction to a putative enumerator and SDP feasibility. Make no code-existence or complete-realizability claim."
    }
  ],
  "interpretation_assessment": "The lane's interpretation is faithful to Open Problem 1 as a request for a putative integer matrix weight enumerator satisfying the displayed necessary conditions. The submitted table completely answers that finite feasibility question under the intended orbit normalization. The additional genus-2 and divisibility claims also pass independent exact verification. I found no Pauli-Y convention error, orbit-normalization error, unsupported symmetry assumption, or mathematical defect in the table. These results do not settle existence of a [[24,0,10]]_2 code."
}