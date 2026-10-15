You are a hostile referee (control theory / real algebraic geometry). Do not delegate. Do not
browse the web. You may read files under /Users/jinleic/jinleic-workspace/ai4s/robust-spr-interval-synthesis/
(in particular work/theory.md, work/*.py) and the PDFs
/Users/jinleic/jinleic-workspace/scratch/ai4s-robust-spr-interval-synthesis/arxiv-2609.26541v2.pdf and
/Users/jinleic/jinleic-workspace/scratch/ai4s-robust-spr-interval-synthesis/QuinticSPR-English.pdf,
and the Lean sources under /Users/jinleic/jinleic-workspace/scratch/ai4s-robust-spr-interval-synthesis/{quintic,sextic}-spr-proof/.
Do not read any other path. Do not modify anything.

## Problem (book: 10000 Selected Problems in Sciences, Information Science, 2011, pp. 680-682, Yu Wensheng & Wang Long)
P^n: real polynomials of degree n; H^n: Hurwitz ones. For b in P^n and a in H^n, b/a is SPR iff
Re[b(jw)/a(jw)] > 0 for all real w. Open problem as posed: for a robustly Hurwitz interval polynomial
family of degree n > 4, does one fixed b exist with b/a SPR for every member a? (Book: n <= 4 known;
authors conjecture yes.) The authors' own papers (e.g. Wang & Yu, ACC 2001 = arXiv:math/0202242)
define interval families as MONIC: {s^n + sum a_i s^{n-i}, a_i in [a_i^-, a_i^+]}.

## Claims to referee
C1 (status). Monic case: n <= 4 classical (Hollot-Huang-Xu 1989; Anderson et al. 1990 n<=3; Wang-Yu 2001 n=4);
n = 5: Yu, Xu, Dou, Ji, Wang 2026 manuscript + public Lean 4 proof github dgjszy/quintic-spr-proof @866e2b5
(theorem SPR.N5.Direct.robustSPR); n = 6: arXiv:2609.26541v2 + Lean proof dgjszy/sextic-spr-proof @2b94aa7
(SPR.N6.Direct.robustSPR). Neither Lean development was rebuilt locally (disk limit); a static source audit found
no sorry/admit/axiom/native_decide/unsafe/implemented_by/extern, a single definition of each statement, and the
formal statements match the monic exact-degree strict-SPR question (closed intervals, degenerate allowed). So the
monic question is settled for n <= 6 (subject to the unreplayed Lean builds) and OPEN for every n >= 7, i.e. the
book's question "for all n > 4" remains open. Check the formal statements in the Lean sources yourself
(Lean/SPR/N5/Definitions/Frequency.lean, Lean/SPR/N6/Definitions/Frequency.lean, Lean/SPR/Common/Hurwitz.lean,
Lean/Main.lean) and say whether they faithfully formalize the monic question with numerator of exact degree n.

C2 (Lemma B, alternation certificate, all n). See work/theory.md. If there are a nonzero real b with deg b <= n,
nodes 0 <= t_1 < ... < t_{n+1}, members a_i of the box, a sign c, with
(E_{a_i}(t_i), t_i O_{a_i}(t_i)) = lambda_i c (-1)^{n+1-i} (O_b(t_i), -E_b(t_i)), lambda_i > 0, then no real beta
with deg beta <= n has Re(beta conj a_i)(j w_i) > 0 for all i. Proof: divided differences of
H = E_beta O_b - O_beta E_b (deg <= n-1) vanish on n+1 nodes.

C3 (Lemma C, closed-limit criterion, all n). If monic boxes K_k -> K_0 (endpoints converge) and K_0 has no nonzero
real beta (deg <= n) with F E_c + t G O_c >= 0 on [0, inf) for all four corners, then K_k is not synthesizable for
large k. Proof by compactness of the unit sphere of numerators.

C4 (Prop. D). Structure of fully-closed marginal boxes (all n-2 gaps between the alternating root bands of the
endpoint even/odd parts closed): tiling, which endpoint vanishes where, realizability = nonnegative coefficient
differences, and the n-2 forced double contacts. For n = 6 these coincide with the contacts and gap-closing odd
bounds U, V of arXiv:2609.26541 Prop. 4.1 / (3.5).

C5 (Prop. E). A non-monic box (leading coefficient in [alpha, beta], alpha > 0) is synthesizable iff the two
homothetic monic boxes B and (alpha/beta)B have a common numerator; hence the monic n = 5, 6 theorems do not by
themselves settle the non-monic variant.

C6 (empirical, exploratory, not a theorem). No counterexample was found: (a) 400 random near-boundary stable monic
boxes for each n = 5, 6, 7, 8 all had positive grid angular margin delta*; (b) random-walk samples of realizable
fully-closed marginal boxes, 2000 per n for n = 7..11 (300 for n = 5, 6), all had a grid-feasible closed problem
(float LP); for n = 10, 11 the float LP reported negative margins in 632 cases (596 + 36); 40 of them (for each n the
12 most negative and 8 random) were rechecked in 60-digit arithmetic after reducing to the 3-dimensional numerator
space left by the exact double contacts, and all 40 were grid-feasible (the float negatives were conditioning artifacts); (c) 150 random non-monic stable boxes for n = 3, 4, 5: all
feasible. Is any wording here an overclaim? What is the strongest defensible wording?

## Required output
JSON matching the provided schema: one item per claim C1..C6 (plus any extra item you need), with a concrete
objection (or "none") and a concrete fix. Be specific: cite the line/equation that is wrong. Then list
status-scoping issues, overclaims, and the single best next step toward resolving the open n >= 7 question.
