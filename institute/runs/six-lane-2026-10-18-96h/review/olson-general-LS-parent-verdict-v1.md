# Ordered Olson sequence lemma: general LS on the new interval (G-LS) and the original-domain union

Recorded at 2026-10-19T09:45:44-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL, conditional on one declared external statement-level theorem.** G-LS holds as stated below, relative to the parent-accepted internal interfaces at their original scopes and, for e=p-kappa>=3 only, to Lev 2022 Theorem 2 (arXiv:2110.01081v3, Theorem 2) as a premise whose proof was not replayed here. Cells with e=2 (and therefore every cell with p=7) use no Lev input. This is a sequence-level written result. It is not LS+, STAB, INV*, ordered Olson or a word-level theorem. No Lean, human-referee or novelty clearance.

## Exact accepted statements

1. **G-LS.** Let p>=7 be prime and floor(2p/3)+1<=kappa<=p-2. For every sequence Y of odd elements of C_(2p) with |Y|>=p+2kappa+1 and no zero-sum (occurrence) subsequence of length in [2kappa+2,2p], every zero-sum subsequence of Y has length <=2kappa.
2. **Corollary LS-ALL (range union).** LS(p,kappa) holds on the entire original LS definition (/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/LS-scope-v1.md lines 9-15): every prime p>=5 and 0<=kappa<=p-2. Proof: accepted S1-sharp ([verdict](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-s1sharp-parent-verdict-v1.md) `bd4a0a60cdea0765517ca33a9a2ddefb664b24fad7b20e709835bbdec1e94f41`, items 1) gives the same implication with no length hypothesis for 0<=kappa<=floor(2p/3), and G-LS covers floor(2p/3)+1<=kappa<=p-2 for p>=7. At p=5, floor(2p/3)=3=p-2, so S1-sharp alone covers every original cell. Both reviewers independently answered YES with no missing endpoint. The two blocks have different trust bases: e>=3 cells of G-LS also rest on the Lev statement.

## Text of record

| Item | Path | SHA256 |
|---|---|---|
| Proof (whole, 206 lines) | [proof-general-LS-Lev-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/proof-general-LS-Lev-v1.md) | `bc4f4c7035353bf904a202bd41811684a76cb5e9401905a2860e20222fec06dc` |
| Frozen scope (before derivation) | [GENERAL-LS-Lev-scope-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/GENERAL-LS-Lev-scope-v1.md) | `5daf9b391dba6c78e75928e1688839978d0fd479a68f86ea0595679f2ea5947e` |
| Review package | [review-package-general-LS-Lev-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/review-package-general-LS-Lev-v1.md) | `14e3ef417fb8712924f2e0826da58997418bac92b7de7f784f67ad256578c22e` |
| Governing excerpt manifest v2 | [review-excerpts-general-LS-Lev-v2.json](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/review-excerpts-general-LS-Lev-v2.json) | `0e938437bbf575aded19e9064255c8e00536edb0c2e901e247bf928219b72903` |
| Review freeze | [olson-general-LS-Lev-review-freeze-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-general-LS-Lev-review-freeze-v1.json) | `f4eac5c14b59f2a6266bda1c44c7d0598c5f1394491cc0d97fe3cf4096779338` |

Parent verified every manifest entry (whole-file SHA256 and inclusive line range) before freezing one identical prompt for both families (prompt SHA256 `c949d43099184ffbe5ed6dda1fed3bdc66dd841559392eac93fb06f44d23fa20`).

## Reviews

- [Codex](olson-general-LS-Lev-codex-v1.prompt.stdout.txt) `cdf42adcb42997bcbbb1efe4554aff0cd1c94689d7c881a263d7e0974215f0fc`: observed gpt-6.1-sol, max, read-only sandbox. **ACCEPT, 0 FATAL / 0 MAJOR / 0 MINOR**; every internal interface in scope; conditional coverage YES.
- [Claude](olson-general-LS-Lev-claude-v1.prompt.note.md) `1110f84e6d5960e15824578a95939a257acbb50e455b48c35a0ac07eb82ceaee`: observed claude-opus-5-5, max, no tools. **ACCEPT-WITH-FIXES, conditional, 0 FATAL / 0 MAJOR / 3 MINOR** plus optional O1; re-derived AP (R6) and AP' (D1); conditional coverage YES.

## Dispositions (no statement, inequality or case split changes)

- **m1, AP' authority.** The δ verdict `ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5` item 2 accepts Proposition I-small "with corrected AP-prime proof" but does not list Lemma AP' standalone. **Parent admits Lemma AP' standalone** at its literal scope: for prime p, n>=1 and 3n+2<p, if an (n+1)-term progression with nonzero difference x lies in an arc of size <=2n+1 of Z_p, then x is in {1,-1,2,-2}. Text: statement proof-LS-caseI-smalldelta-v1.md lines 30-31; proof D1 of erratum-1-delta-APprime.md lines 7-17, which supersedes the v1 proof per erratum-2-delta-consolidated.md D-2 m2.3. Parent derivation: with d=|x~|<=(p-1)/2, the n points with rho>=1 lie in I∩(I+x) of size max(0,l-d)+max(0,l-p+d). Case d>=l gives an empty intersection. Case p-l<d<l gives 2l-p<=4n+2-p<n. Otherwise d<=l-n<=n+1, and the integer lift stays in one window because p>3n+1 and l+n<p, so nd<=l-1<=2n and d<=2. Claude re-derived D1 independently and Codex accepted the interface.
- **m2, citations.** Where proof section 0 and the package table disagree on line ranges, the governing manifest v2 ranges control. No mathematical effect.
- **m3, mandatory wording overlay at proof lines 184 and 187.** Read: "among integers congruent to -j (mod p), only -j and p-j can lie in [-p+h+1,P], which is contained in (-p,p); and p-j>h>P." At j=1 the old open interval (-p,p-1) omitted p-1, but the candidate list was already a valid superset; the conclusion tau=-j is unchanged.
- **O1, optional, not adopted.** Claude notes that SLZ3 and minimality of T are dispensable because any long T gives j<=floor((p-2e+1)/2) and still p-j>h. The frozen text remains in scope; no change is needed.

## External theorem and parent primary re-read

Parent re-read [arXiv:2110.01081v3](https://arxiv.org/html/2110.01081v3) (HTML, dated 01 Jun 2022) at this verdict. Theorem 2: "Suppose that α=(a1,…,an) is a zero-sum-free sequence of elements of an abelian group. If |Σ(α)|<2n then …" there are a and integers 1=x1<=…<=xn with x(k+1)<=x1+…+xk, a_k=x_k a, Σ(α)={0,a,…,(x1+…+xn)a}, and x1+…+xn<ord(a) for finite order. Σ(α) includes the empty subsequence. **No length hypothesis appears**; the paper states the conclusion holds when the sum set is small "not necessarily because 'the whole group is exhausted'". This closes Claude's load-bearing check: at (p,kappa,delta')=(19,13,1) the core has n=9<p/2, and a half-order hypothesis (Theorem 1, Savchev-Chen/Yuan) would not have covered it. The proof consumes only the hypothesis and the structure/interval conclusion; a≠0, ord a=p, n<=S and the occurrence-level coefficient interval are derived in the proof. Lev's proof is not replayed, and the local transcription hash is not a remote byte hash.

## Independent parent checks (supplementing, not replacing, the reviews)

- Few-sums margin: with n=p-2e+1+delta', t=max(1,floor(delta'/2)) and 3e<=p-1, 2n-(p-e+t)=p-3e+2+2delta'-t>=3+delta'>=4.
- e=2 has an empty case-(I) d-range, so no core, Lev call or N=0 AP' call is made; this matches accepted LS-small.
- Witness: 1<=j<=floor((p-3e+1)/2)<p-e+1, hence p-j>h=e-1, excluding the positive lift.
- Every internal interface (RED, CF(a), DGM-p, threshold dichotomy, LS-II', AP R6, AP', SLZ3 shortest-only) is used inside its original scope; this agrees with both review tables.

## Boundary and status of other candidates

- Not claimed: LS+, STAB (the 3kappa+1 bound), INV*, any word-level transfer, ordered Olson for D_(2p) or all groups. Word-level consequences require a separate reviewed assembly.
- Transitive imports retain their own scopes and trust: index-one/Savchev-Chen/Yuan, S1-sharp's chain, RED/SLZ/EXT/PROP, Cauchy-Davenport via RS. The computational aids recorded elsewhere are not premises.
- The narrower pending candidates (Lev-normalization, BASE2-Lev-closure, S3/P1-P3 bodies) remain at their own statuses; their unlaunched Claude reviews stay held by [queue replacement](olson-general-LS-review-queue-replacement-v1.json) `62e33b0ae043…`. Already accepted narrower cells (LS-lin, LS-small, BASE1, BASE2 cells) are subsumed in range but their verdicts are unchanged.
- No priority or novelty statement. A read-only priority scout (OlsonGLSPriority) is pending; a search miss will not be reported as novelty.
