# Slot info-4 — recursive MDS at order 18: selection v1

Owner: `InfoRecursiveMDS18`. Exact owned root is this directory. Last clock actually observed before creation: **2026-10-23T14:02:09-0700** (`/bin/date '+%Y-%m-%dT%H:%M:%S%z'`). Governing contract: `institute/runs/three-area-2026-10-23-96h/contract-v2-eighteen-slots.json`, together with both named parent errata. The expansion did not reset the deadline, **2026-10-27T12:35:38-07:00**.

## Literal target and quantifiers

Set `X={0,...,17}`. Determine whether there exists **any** binary operation `L:X×X→X` such that all three conditions hold:

1. for every `x`, the map `y↦L(x,y)` is a permutation of `X`;
2. for every `y`, the map `x↦L(x,y)` is a permutation of `X`;
3. for every `x`, the map `y↦D(x,y)=L(y,L(x,y))` is a permutation of `X`.

For Latin `L`, the columns of `D` are automatically permutations, so (3) says exactly that `D` is Latin. The desired full code is all **324** words `(x,y,L(x,y),D(x,y))`. No idempotence, group isotope, affine law, congruence, symmetry, fixed recursion period, distinct entries within recursion cycles, or restricted family is imposed. A positive answer must provide exact 324 entries or an equally explicit mechanism with a complete proof. A negative answer must cover every such operation, not one construction ansatz.

## Book relationship — intentionally limited

The source-volume entry `books/README.md` identifies the information-science volume (2011, ISBN 978-7-03-031911-1; PDF SHA-256 `9b3f16ee6b558f7c289a7208cec01a9811091863631d09908b8f4cb66d2027db`; PDF page = printed page +21). The current parent selection identifies the coding/decoding articles at printed pp.394–395 and464–466. I read the retained actual extraction `information-science/evidence/three-area-20261023-96h/sources/book-coding-394-395.txt`, whose title is *纠错码的译码问题* and whose substantive question is average-case decoding complexity after discussing worst-case hardness and code distance. Its extraction is garbled in places; no verbatim mathematical symbols are reconstructed from guesses.

The present finite recursive-MDS existence question is a modern code-construction question related to that chapter's code/distance subject. **It is not the book's full decoding-complexity problem, not a solution of average-case decoding, and not claimed to be printed verbatim in the book.** The exact target comes from the modern primary source below. Parent `selection-v1.md` candidate C and `selection-v2.md` candidate CGMN are baseline status records, not this worker's findings.

## Matched primary baseline and current status

Actual first source: [Petr Klimov, arXiv:2604.01105v2](https://arxiv.org/html/2604.01105v2), dated16June2026, *On the Construction of Recursively Differentiable Quasigroups and an Example of a Recursive [4,2,3]_26-Code*. I read the definitions, Introduction/Theorem1, directed-standard construction, Theorems3–8, spectrum statements and Conclusion. Retained raw HTML SHA-256 is `b73b05341666d987313e2e16fd092e7ce2a578b903bc9dbc71f126ac4a1a73a0`; source-only cleaned text SHA-256 is `d03b1d4cb8682451eb5d7230989fde91d649ffad938aee4acc39e802ccff1b95`.

- Theorem1 explicitly authenticates the full-recursive-code/quasigroup equivalence at length4.
- Theorem5 says an `(n+2)`-perfect `(v,k,1)` Mendelsohn design with `0≤n≤k−3` gives an n-recursively differentiable quasigroup. Thus a **3-perfect** suitable design suffices here.
- Theorem6/7 gives a solution from a perfect `(v,k,1)` design with `k≥4`. This is a **sufficient construction**, not an equivalence for arbitrary Latin `L`.
- Theorem8's converse requires extra idempotence, precise recursion-period identities and exclusions. Those hypotheses are NOT present in this assignment and will not be silently imposed.
- Klimov constructs q26 using the pre-existing `(26,5,1)` PMD construction and lists **q14 and q18 as the two remaining cases** in the Conclusion. This is a dated primary open statement for the exact target at18.
- The `(18,6,1)` PMD is among the exceptions to the quoted existing block-size-six spectrum. An exception to a theorem is not a nonexistence assertion.
- The live unversioned arXiv record and search result identify v2 as the latest listed version. Bounded later searches for recursive differentiability/order18 did not locate a matched later solution. Search misses are not proof of current openness or novelty: status is **PRIMARY-OPEN as of16June2026; current resolution not found in this bounded screen / NOVELTY_UNCLEAR**.
- A separate q14 public lead is Zenodo21499738 / DOI10.5281/zenodo.21499738, attributed Nithil R. in earlier repository screening. The parent had403 on that page; this worker has not authenticated its object/proof. It neither resolves18 nor supplies a trusted import here.

Older primary check: [Izbash–Syrbu2004, pp.257–263](https://dml.cz/bitstream/handle/10338.dmlcz/119454/CommentatMathUnivCarolRetro_45-2004-2_6.pdf), read through Proposition3/Corollary1, independently states the binary recursive-code equivalence and that only the `(E1,D)` pair remains to be made orthogonal once `L` is Latin. These are classical baselines, not new results.

Primary access boundary: Syrbu–Kuznetsova2023, *On recursive1-differentiability of the quasigroup prolongations*, BASM102(2),102–109, is a relevant required comparison. Its actual journal issue/entry was located, but HTTP returned an unrelated fallback page and HTTPS failed certificate verification at this read. The body is not yet an authenticated import. The Abel–Bennett–Zhang2000 block-six DOI returned bibliographic metadata, not the body. No claim about what those unread bodies prove is made.

## Mandatory corpus screen

Local `/Users/jinleic/jinleic-workspace/math/lean/docs` and `math/preprints` were searched for `Mendelsohn`, `quasigroup`, `recursively differentiable`, `recursive.*MDS` and `Klimov`; the only Klimov substring hits were unrelated Klimovsky references. The remote openai/math lean/docs and preprints inventories were opened. A fresh remote `CONTENTS.md` (719 manuscripts /372 families) was retained as source text, SHA-256 `cc7c0b8a1cdedd845a777e77cf682657308503daf8346c1349e06e9259d063c2`; full keyword screening for `quasigroup`, `Mendelsohn`, `recursive code`, `recursive MDS` found no matches. This is a title/abstract/source-keyword screen, not a semantic audit of every proof or guarantee against an unindexed equivalent.

## Missing ingredient and consequential delta

The missing ingredient is a construction or obstruction at18 which escapes the known failed/direct-product/PMD special families. Ordinary orthogonal Latin squares at18 do not automatically satisfy a common recursion rule. Conversely absence of a selected PMD or affine model cannot rule out the larger cycle decompositions which Klimov explicitly suggests.

A full18 witness would settle the q18 CGMN instance. A complete obstruction would refute the conjecture at18. A scoped structural theorem is useful route evidence but must be labeled **PARTIAL**, with18 still unresolved.

## First bounded written attack and chronology

First independently derive the exact congruence/quotient constraints on an unrestricted solution at18, particularly possible quotients of orders2,3,6,9 and size-two fibers. This tests whether any block-extension mechanism can work and can produce a precise all-order obstruction to a whole structural class, rather than another affine calculation. Then derive the exact three-distance cyclic-word construction interface **allowing repeated symbols and diagonal pairs**, and compare it to Klimov's more restrictive PMDs before proposing a finite certificate/search.

Chronology disclosure: during source screening I considered the quotient-size-two cancellation and the general cycle-cover characterization conceptually; no completed proof or computational result existed before this freeze. This is not falsely represented as a pristine pre-idea registration. Parent InfoResearch96h reports an earlier **unproved exploratory suspicion** about ordinary one-transversal Bruck prolongation; it is not adopted as an established result or claimed as mine.

## Verification, compute gate and redirect

Written proofs must be complete and a finished candidate pinned before parent and separate in-harness reconstruction. Correctness, classical import trust, scope, finite verification, formal proof, novelty and significance stay separate. No Lean/kernel/human/external-model review is claimed.

**No scientific execution has occurred or is authorized.** Source extraction, keyword screening and metadata hashing are the only programs used. If finite work becomes necessary, propose exact immutable source/input hashes, one bounded experiment, positive/negative controls, resource ceiling and cooperative settlement for a named parent GO. No Latin search, solver, executable certificate check, compilation or enumeration may be launched from this assignment alone.

If an accessed primary source already solves18, report it immediately and propose a genuinely distinct replacement for parent collision checking; never count a solved target as active-unsolved. If a structural route is excluded, preserve the exact theorem and change the representation, not the target. UNKNOWN is not UNSAT and access gaps are not novelty.
