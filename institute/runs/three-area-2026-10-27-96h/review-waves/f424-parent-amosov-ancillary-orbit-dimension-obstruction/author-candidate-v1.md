# Public Amosov Proposition4: the stated ancillary orbit dimension is false

**Status: PARENT AUTHOR / SOURCE-STEP COUNTEREXAMPLE — UNREVIEWED.** Native parent observation before composition: 2026-10-30T10:58:07-0700 PDT. This identifies a false intermediate claim in the accessible public manuscript, not a counterexample to Proposition4's inequality, Proposition5's conclusion, depolarizing majorization or the original target.

## Literal primary source and exact point at issue

[Amosov, arXiv:2103.08515v6, §6 Proposition4](https://arxiv.org/html/2103.08515v6#S6) considers any unit vector f in K tensor H and the orbit span

L=span{(I_K tensor U_g)f : g in G}.

Immediately after saying the n² operators U_g are linearly independent, the accessible text states: **“Hence dim L=n”** and calls the restricted representation irreducible. The exact [rendered-reader excerpt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/source-screens/amosov-2022-proposition4-ancillary-proof-reader-excerpt-v1.md) and the broader [bounded source audit](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f413-depolarizing-w4-bounded-public-source-overlap-audit/review-v1.md) preserve the cited claim. The subscription journal text was not independently compared with this manuscript.

## Counterexample satisfying the literal qubit hypotheses

Take H=K=C², n=2 and the irreducible projective Pauli representation of G=Z2×Z2,

U_(0,0)=I, U_(0,1)=Z, U_(1,0)=X, U_(1,1)=XZ.

Its subgroup T={(0,0),(0,1)} restricts to the ordinary unitary representation {I,Z}. Let

f=(|00>+|11>)/sqrt2.

The four orbit vectors are the four mutually orthogonal normalized Bell states:

(I tensor I)f=(|00>+|11>)/sqrt2,
(I tensor Z)f=(|00>−|11>)/sqrt2,
(I tensor X)f=(|01>+|10>)/sqrt2,
(I tensor XZ)f=(|01>−|10>)/sqrt2.

Thus dim L=4, not n=2. The restricted action on L=K tensor H is the direct sum of two equivalent two-dimensional representations, not irreducible.

The channel assumptions can also be met without weakening the example. Choose Phi as the physical depolarizing channel at p=1/2, with Pauli weights (5/8,1/8,1/8,1/8). Its single-qubit pure outputs have spectrum q=(3/4,1/4); the cosets {I,Z} and {X,XZ} satisfy the ordered cross-coset weight hypothesis. The actual Bell output of (id tensor Phi) is diagonal in the four orbit vectors with spectrum (5/8,1/8,1/8,1/8). That particular spectrum IS majorized by q padded with two zeros. Thus the example refutes the proof's dimension/irreducibility step while explicitly NOT refuting the proposition's bound.

## Correct general orbit dimension

The source's asserted n² linearly independent matrices form a basis of End(H). If f has Schmidt rank r, choose a Schmidt decomposition f=sum_(i=1)^r s_i e_i tensor h_i with every s_i>0. The span of all (I tensor A)f with A in End(H) is exactly span{e_1,...,e_r} tensor H: the coefficient vectors A h_i can be chosen independently. Therefore

**dim L=n r**, and the restricted action is r copies of the irreducible representation. It is n-dimensional and irreducible only for Schmidt rank1. This is a statement about the source proof's assumptions; no assertion about arbitrary representations whose matrices do not span End(H) is made.

## Scientific and source boundary

Proposition4's output-majorization inequality might still be true by a different proof. Proposition5 and the arbitrary-N statement require their own independent adjudication; a false intermediate proof step alone is not a mathematical refutation of those claims or of classical-capacity conclusions known from other work. The inspected source audit also identified a newer paper explicitly treating general exact majorization as conjectural, but neither paper's authors' awareness or worldwide status is inferred.

Chronology: parent accessed and read the public §6 source and reasoned about the Bell orbit **before** creating this author freeze; [manifest/receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f424-parent-amosov-ancillary-orbit-dimension-obstruction/manifest-v1.json) record that fact. No scientific executable or independent review has yet been performed for this exact candidate. The Bell state is a prospective selected author example permitted by the owner direction. No held payload, private result, external-model CLI, paid/heavy run, installation, deletion, publication, commit, push or infrastructure mutation was used. Separate written and exact finite verification and a repair/falsification attempt remain required. No human, independent-model-family, formal/kernel, novelty or original-target acceptance is claimed.
