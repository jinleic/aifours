# info-6 selection v1 — balanced nine-variable nonlinearity 242

Freeze clock actually observed: **2026-10-23T14:01:27-07:00**, `/bin/date -Iseconds`. One problem only. Deadline remains 2026-10-27T12:35:38-07:00. No scientific program has been run. Source and written research only.

## Literal target and conventions

Does there exist **any** function `f:F_2^9 -> F_2` such that

- `sum_{x in F_2^9} f(x)=256`, and
- for **every** `a in F_2^9`, `|W_f(a)| <= 28`, where `W_f(a)=sum_x (-1)^(f(x)+a.x)`?

Equivalently, balanced `f` has `NL(f)=min_{a,b} wt(f+a.x+b)=256-(1/2)max_a|W_f(a)| >=242`. Arithmetic inside the exponent is in F_2; Walsh sums are unnormalized integers. Input index `x=0,...,511` has coordinates `x_i=(x>>i)&1`, and truth-table character `bits[x]` means `f(x)`. A submitted truth table must specify literal bit order and exact bytes; hexadecimal alone without its expansion convention is insufficient.

Success is an explicit 512-bit truth table passing independent definition-level checks, or a proof excluding **all** such functions. No half truth table, symmetry class, residue type, zero count, local radius or corpus is fixed in the target. Those are only labeled subcases.

## Book and modern source relationship

The book article is *The Tight Upper Bound of the Nonlinearity of Resilient Boolean Functions*, Zhang Weiguo and Xiao Guozhen, pp.403–405, PDF pp.424–426, information-science volume (2011, ISBN 978-7-03-031911-1). Read `books/README.md`, the saved page-424 image and the preserved `sources/info-p0403-q9bal242/excerpt.txt` in the 2026-10-15 catalog. The book asks the odd-n balanced maximum for n>=9 and constructions exceeding the bent-concatenation value; the present n=9 threshold 242 is the first even value above 240, not a claim to solve its all-n program.

Accessible matched primary open statement: Lou–Xu–Wang, [arXiv:2610.17897v1](https://arxiv.org/html/2610.17897v1), §4 Open problem 1: “Does there exist a 9-variable balanced Boolean function with nonlinearity 242?” The unversioned abstract/raw history currently exposes only v1, submitted 2026-10-13. Wang–Lou–Wang, [arXiv:2610.17871v1](https://arxiv.org/html/2610.17871v1), §6 explicitly also leaves this balanced question open. Their claimed unrestricted covering-radius upper bound 242 is not a balanced construction and is not imported as a verified theorem here.

**Fresh source delta versus the old dossier:** Hou–Sabo–Slaughter, [ePrint 2026/2529](https://eprint.iacr.org/2026/2529), received 2026-10-18 and revised 2026-10-19 according to the source history, gives a separate computer-assisted claim `rho(RM(1,9))=242`. Read the full manuscript through its authors' public [repository PDF](https://raw.githubusercontent.com/FreemanSlaughter/Covering-Radius/main/RM(1%2C9).pdf) (repository blob `0670ac076d1bb704e5c63bb8a0a420f70c73f545`). Its Proposition 7, subsequent exclusions and Theorem 11 concern peak24/nonlinearity244, then exclude243; its attaining242 table is explicitly the Kavut–Yücel unbalanced baseline. It does not settle this slot. The paper and notebook have **not** been independently replayed. Its PDF title-page date is October11, while the ePrint publication history is October18/19; preserve that distinction.

Kavut–Yücel [arXiv:0808.0684](https://arxiv.org/pdf/0808.0684), read introduction/definitions, constructs unbalanced242 functions and explicitly says their spectra have no zero. Adding an affine output cannot balance those particular tables.

## Governing local baseline

Read root `README.md`, domain `information-science/README.md`, `hard-continuation-20261015/proof.md`, `quadratic-distance/{PROOF,SHARPER}.md`, `zero-geometry/{README,PROOF}.md`, the underlying zero-moment candidate, and `remaining-types{,-round2}/{README,PROOF}.md` with the round2 receipt.

- All252 listed remaining fixed-half classes were closed earlier; that is not unrestricted coverage and is not new work here.
- The reviewed odd-half bound is `wt(J_g+J_h)>=112`.
- The entire balanced `(polar rank4,weight128)` type was excluded under the recorded model-reviewed imports; no kernel/human-review claim.
- The **current** `remaining-types-round2/result.json` still says **no additional type excluded**. Seven types remain in that evidence: `(2,192),(4,160),(6,112),(6,128),(6,144),(8,120),(8,136)`.
- Round2 proofs are explicitly model-written and lack their own independent proof review. Their count/slice witnesses are not Boolean truth tables. Do not elevate them beyond their receipt.
- Four of the seven types provably cannot be excluded by the old single-character projection lever even with perfect equivariance. The other three have explicit realizability/alignment or S-side bottlenecks. Longer count-relaxation runs are not a justified next input.

The matched attainable balanced baseline is240. An elementary local argument places the balanced maximum in `{240,242}`; the independent new covering-radius claim is supporting prior literature, not a round result or a replayed import.

## Corpus refresh and status limits

Before novelty/discovery work, screened local `/Users/jinleic/jinleic-workspace/math/{CONTENTS.md,overview.tex,lean/docs,preprints}` with explicit combinations of balanced/resilient Boolean nonlinearity, bent concatenation, Patterson–Wiedemann, Reed–Muller and the two arXiv identifiers. Only an unrelated high-noise balanced-Boolean hit appeared. Read the current remote [openai/math CONTENTS](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md), currently reporting719 manuscripts/372 families, and searched it for nonlinearity, resilient, Reed–Muller, Patterson, bent concatenation and balanced Boolean; only unrelated Patterson cubic-Gauss-sum entries matched. This is a bounded text/index screen, not inspection of every remote PDF or proof clearance.

Web queries `"balanced" "242" "9-variable" Boolean 2026` and `"balanced" "nonlinearity" "242" after:2026-10-13` found the later covering-radius paper but no matched balanced solution in the inspected sources. **PRIMARY-OPEN-STATEMENT-LOCATED; current universal openness is not certified by search misses; NOVELTY-UNCLEAR.**

## Missing ingredient, delta and first bounded attack

The missing ingredient is **spatial Boolean realizability jointly on both canonical spectra**, not another scalar histogram. An unrestricted exclusion must reach all seven surviving types (and preserve all possible zero sets); a construction may occupy any one type but must produce all512 bits without silently fixing a half.

First written attack: derive a new *all-shift* S–R compatibility/defect constraint from the complementary Fourier supports, retaining their common coordinates rather than reducing each coset to a count. Investigate whether its modular form obstructs the known surviving low-defect configurations; explicitly prove any reduction and record where it stops. This is additional necessary-condition research, not permission to declare a type excluded. The exact complete witness-verification route will be frozen separately.

Chronology: possible algebraic routes were considered during source screening, before this freeze; no complete candidate or scientific computational result informed this selection. All substantive candidate claims are to be written subsequently, with this disclosure rather than a fictitious pristine preregistration.

## Verification and redirect

Complete written candidates need a frozen byte hash, parent read and an actual separate reconstruction before promotion. Truth-table acceptance requires strict parsing, balance, a complete512-coefficient Walsh transform and independent direct character sums, exact NL and meaningful rejection controls on pinned bytes. Any executable scientific check, enumeration, solver or compilation needs exact parent admission first. No native run is authorized from this launch.

Do not restart old jobs, exhaust another known half-corpus, reuse a SAT/UNKNOWN verdict as nonexistence, or call Fraction/Python arithmetic a proof-assistant kernel. No nested agents/CLI or sibling/shared-index writes. All files here are immutable; corrections use numbered successors.

Redirect condition: if a matched current primary source already solves the balanced target, report it immediately and propose a **distinct** replacement outside the eighteen-slot roster for parent collision checking; otherwise keep this full target and report partial claims honestly. A new representation with a rigorously identified blocker can satisfy this bounded attack; a no-find or another plan cannot be called a solution.
