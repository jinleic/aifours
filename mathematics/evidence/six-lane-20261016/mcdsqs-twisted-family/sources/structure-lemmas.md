# Structure lemmas for the twisted model T1 (proofs; lane notes, not peer reviewed)

Setting (README §2): p ≡ 7 (mod 12) prime, F = F_p, S/N squares/non-squares (−1, 3 ∈ N;
−3 ∈ S), ω a primitive cube root of unity (ω ∈ S), X = F × Z2,
G = {g_{a,b}: (x,i) ↦ (ax+b, i+[a ∈ N])}, A = {x ↦ ax+b : a ∈ S} (copy-preserving part acting
on one copy), σ = g_{−1,0}: (x,i) ↦ (−x, 1−i). Every statement below is about G-invariant
objects only; none is a hypothesis about arbitrary mcDSQS(2p).

## L1. Orbits on triples

(a) A acts regularly on unordered pairs of F (|A| = C(p,2); the only candidate for a
non-identity element fixing {0,1} is x ↦ 1−x, whose multiplier −1 ∉ S). Hence G acts
regularly on same-copy pairs (A on each copy, N swaps copies).
(b) Type B triples (2+1 points): p orbits, represented by {(0,0),(1,0),(z,1)}, z ∈ F.
(c) Type A triples (3 points in one copy) ↔ A-orbits of 3-subsets of F. A non-identity element
of A fixing a 3-set permutes it cyclically (A has odd order), so it has multiplier ω^{±1};
the fixed 3-sets are the "equilateral" triangles. There are exactly two A-orbits of them
(through {0,1}: third vertex −ω or −ω²), each with stabilizer of order 3; the other
(p−4)/3 orbits are regular. Each regular orbit contains exactly 3 triples through the pair
{0,1}, each equilateral orbit exactly one.
(d) Normalization: a triple T ⊃ {x,y} with y−x ∈ S is A-equivalent to {0,1,t},
t = (z−x)/(y−x), by the unique element of A sending (x,y) ↦ (0,1).

## L2. Block structure and the pairing condition

A block through a copy-0 triple T is (4,0) (four points in copy 0) or (3,1). Let k be the
number of (4,0)-blocks through a copy-0 pair (constant by A-transitivity on pairs). The pair
P×{0} lies in p−2−2k (3,1)-blocks (distinct copy-1 points), so the copy-1 points not used,
L0(P) (2+2k of them), must be covered by exactly 1+k (2,2)-blocks P×{0} ∪ Q×{1}: the Q's
partition L0(P). Let Π be this partition for P0 = {0,1}. By A-equivariance the (2,2)-blocks
are {g(P0)×{0} ∪ g(Q)×{1} : g ∈ A, Q ∈ Π}.
**Claim.** These blocks are σ-invariant (and then every type-B triple with its pair in copy 1
is covered exactly once) iff Π is invariant under
Φ{q1,q2} = {q1/d, (q1−1)/d}, where the labels are chosen with d = q1 − q2 ∈ S.
*Proof.* σ(P0×{0} ∪ Q×{1}) = (−Q)×{0} ∪ {0,−1}×{1}. The element g(x) = dx − q1 of A maps
(0,1) ↦ (−q1,−q2), so the (2,2)-partners of −Q are g(Π); thus σ-invariance of the block
through P0 and Q ⟺ {0,−1} ∈ g(Π) ⟺ g^{−1}{0,−1} = {q1/d, (q1−1)/d} = Φ(Q) ∈ Π. A-equivariance
transports the statement to all pairs, and σ-invariance turns the copy-0 coverage property
into the copy-1 one (the copy-1 completions are f′(T′) = −f(−T′), so L1(Q) = −L0(−Q)). ∎

## L3. Φ is an involution; its fixed pairs are {w−1, w}

Φ(Q) carries the difference 1/d ∈ S, and Φ(Φ(Q)) = {q1, q1 − d} = Q. Φ(Q) = Q forces
d = 1 (then Q = {w, w−1}) or q1 = 0, q2 = −1; the remaining case gives d² = −1, impossible
since −1 ∈ N. ∎
**Corollary (k = 0).** A G-invariant SQS(2p) without (4,0)-blocks is the same as an
A-equivariant completion f of copy-0 triples into copy 1 (equilateral triples go to their
centroid, the unique fixed point of their order-3 stabilizer) such that z ↦ f({0,1,z}) is
injective on F∖{0,1} and misses exactly two **consecutive** values {w−1, w}.

## L4. Hessian completions (negative, scoped)

For T = {0,1,z} the Hessian points (fixed points of the order-3 Möbius maps cycling T) are
h1(z) = −ω²z/(z+ω) and h2(z) = −ωz/(z+ω²) = h1^{−1}(z); at h1 the cycle 0→1→z→0 has
multiplier ω. In the coordinate w = z/(z−1), h1 is w ↦ λw with λ = −ω ∈ N (order 6), and
χ(z(z−1)) = χ(w). The canonical rule H_ω (orientation with (x−y)(y−z)(z−x) ∈ S, multiplier
ω) is A-equivariant and reads ψ(w) = λw (w ∈ S), λ^{−1}w (w ∈ N).
(i) The only pole (Hessian point ∞) is at w = λ, i.e. the equilateral orbit of {0,1,−ω²};
the other p−3 values of z are mapped bijectively onto F∖{0,1,−ω²}. Only the value −ω² at the
pole would make the missing pair consecutive ({0,1}), but a (3,1)-block forces the centroid.
(ii) Patch P1 (centroid of that orbit in copy 1) collides: ψ(λ) = λ² = ψ(−1), i.e.
f({0,1,−ω²}) = f({0,1,1/2}); so P1 never gives an SQS (every pair has one collision; confirmed
at p = 19, 31, 43 in `runs/f3/hessian_p*.json`).
(iii) Patch P2 (the equianharmonic (4,0)-orbit of {0,1,−ω²,1/(1−ω)}, k = 2) is injective with
|L0(P0)| = 6 (formulas: {0,1,−ω²,1/2,(1−ω)/2,(2+ω)/2} if χ(1−ω) = 1, and
{0,1,−ω²,1/2,(1−ω)²/6,−ω²/2} if χ(1−ω) = −1), but for p = 19, 31, 43 and both ω no
Φ-invariant pairing exists (computed). A symbolic proof for all p was not attempted.
(iv) **Lemma H (proved, any p ≡ 7 mod 12).** The two Hessian points of the 3-term progression
{0, 1/2, 1} are the centroids (1−ω)/3 and (1−ω²)/3 of the two equilateral triangles
{0,1,−ω}, {0,1,−ω²} on the same segment (check: h1(1/2)·3 = (1−ω) ⟺ ω²+ω+1 = 0). Hence in
any G-invariant SQS(2p) in which both equilateral triples through {0,1} lie in (3,1)-blocks
(in particular whenever k = 0), the progression orbit is **not** completed by a Hessian point.
In w-coordinates: Hessian-type completions are ψ(w) = λ^{δ(w)}w; finiteness forces δ(λ) = +1,
δ(λ⁻¹) = −1, injectivity forbids δ(w) = +1, δ(λ²w) = −1, and the 3-cycle λ → −1 → λ⁻¹ under
×λ² then has no admissible δ. So **no k = 0 SQS is Hessian-type** (generalizes (ii)).
(v) Hole bookkeeping for "Hessian except the progression orbit": generic cosets c⟨ω⟩ (full
×λ²-cycles) need constant δ and map onto −c⟨ω⟩; the cosets ⟨ω⟩∖{1}, 2⟨ω⟩∖{2},
(½)⟨ω⟩∖{½} leave one hole each in −⟨ω⟩, −2⟨ω⟩, −(½)⟨ω⟩, plus the holes 0, ∞ (w), i.e.
z ∈ {0,1}. The progression completion u (z-value of f({−1,0,1})) gives the w-values
{v, 2−1/v, (2v−1)^{χ(2)}} with v = u/(u−1). Covering {0,∞} forces u = 0 (the **midpoint**
completion f({x,(x+y)/2,y}) = (x+y)/2) and the hole −1 in −⟨ω⟩ (pattern δ(ω²) = −1,
δ(ω) = +1); then the holes 2λ ∈ −2⟨ω⟩ and λ/2 ∈ −(½)⟨ω⟩ (patterns ++) give the leftover
z-pair {λ/(λ−2), 2λ/(2λ−1)}, and 2λ/(2λ−1) − λ/(λ−2) = −3λ/((2λ−1)(λ−2)) = 1 identically
(λ² = λ−1): a **consecutive** pair for every p. Remaining condition (open): an orbit-wise
choice of Hessian points realizing these δ-patterns (δ(w) = ε(orbit)·χ(w), ε constant along
the generic orbit–coset incidence graph).
(vi) **Vertex orbit (proved, k = 0).** φ(t) ∈ {0,1} means the triple is completed by the
point above one of its vertices; then the two pairs through that vertex give the two values
0 and 1 (two equal values would violate injectivity), and Hessian points and centroids never
take the values 0, 1. Hence W ∩ {0,1} ∈ {∅, {0,1}}; if W ≠ {0,1} (needed for colourings, L6a)
exactly one A-orbit is completed by a vertex (in the F3.2c/F3.4 solutions: {0,1,3} → 0 at
p = 19, {0,1,3} → 3 at p = 31, {0,1,6} → 6 at p = 43).
(vii) Data (F3.4): the minimum number of non-Hessian orbits is 4/5, 6/9, 6/13 at
p = 19, 31, 43; besides the progression and the vertex orbit, the free orbits show no
p-independent pattern. Hessian points are therefore not a good basis for a uniform rule.

## L5. Colouring structure under R = S (the T1 colouring symmetry)

D = derived design at (0,0) (2p−1 points). S fixes exactly (0,0), (0,1) and acts freely on
the other points and on the triples through (0,1); the triples of D fixed by ω are the
(p−1)/3 pairwise disjoint triples x·{1,ω,ω²}×{i} completed by (0,0) (exactly one of each pair
{xC×{i}, (ax)C×{1−i}}, a ∈ N, by the element g_{a,0} that swaps (0,0) and (0,1)).
Class orbits are [(p−1)/2, (p−1)/2, 1]; writing p−1 = 6k, |F| + 3k(a+b) = (2p−1)(p−1)/3 =
24k²+2k with |F| ≤ 4k forces |F| = 2k = (p−1)/3 and a = b = 4k = (2p−2)/3. So F is the set of
ω-fixed triples of D, and every other class misses exactly one point, namely a point covered
by F. In the **k = 0 model** the copy-0 ω-fixed triples x·C×{0} are completed by their
centroid (0,1), so F = {x·C×{1}} covers copy 1 ∖ {(0,1)}, and every other class is a
parallel class of X∖{(0,0),(m,1)} for a unique m ∈ F*; labelling classes by m, C_{sm} = sC_m.
(For k > 0, F may contain copy-0 triples and the missing points change accordingly.)
**Equivalently (k = 0):** choose C_1 and C_{−1} (parallel classes of X∖{(0,0),(±1,1)}) whose
S-orbits partition D∖F — a rainbow pair of near-perfect matchings in the 3-graph D∖F
coloured by its 4(p−1)/3 free S-orbits.
In the k = 0 model the (2,2)-derived triples b_y = {(y,0)} ∪ L0({0,y})×{1} (one per y ∈ F*)
are distributed 2 per class in one class orbit and 0 in the other (β ∈ {0,2}, β₁+β₋₁ = 2 by
parity 2α+β = p−1), and the class with β = 0 restricts to a perfect matching of F*×{0}.

## L6. Two further constraints in the k = 0 model (proved)

(a) **W ≠ {0,1} always (proved; supersedes an earlier colouring-parity version).** If
W = L0({0,1}) = {0,1}, every (2,2)-block is P×Z2 (W = {0,1} is forced, e.g., by invariance
under G×⟨τ⟩, τ(x,i) = (x,1−i), which makes the completion AGL(1,p)-equivariant so that
x ↦ 1−x gives W = 1−W). Then a triple {(0,0),(x,1),(y,1)} with x,y ∈ F* distinct lies in no
(2,2)-block (its copy-0 pair would have to be {0,z} with L0 = {0,z} ∋ 0) and in no copy-0
(3,1)-block, hence in a copy-1 (3,1)-block completed by (0,0); triples {(0,0),(0,1),(y,1)}
lie in {0,y}×Z2. So the copy-1 triples completed by (0,0) form an STS on the p−1 points of
F*, impossible because p−1 ≡ 0 (mod 6). **Hence no G-invariant k = 0 SQS(2p) has W = {0,1}**
(confirmed: F3.5(a) UNSAT at p = 19, 31). (The colouring-parity argument recorded earlier
for this case is correct but vacuous.) The F3.2c solutions have W = {6,7}, {3,4}, {24,25}.
(b) **Copy-0 shadow (necessary condition).** Writing F* = ⟨g⟩ and y = gᵃ, the S-orbits of
copy-0 pairs {y,y′} ⊂ F* are the pairs {a,b} ⊂ Z_{p−1} modulo even translations: p−2 types
((p−1)/2 with b−a odd, ordered from the even end; (p−3)/2 with b−a even, with a parity bit).
The copy-0 parts of C_1 and C_{−1} are a perfect matching of Z_{p−1} and a perfect matching of
Z_{p−1} ∖ {e, o} (e even, o odd: the two b-triples lie in the β = 2 class, one from each
S-orbit of b-triples) that together contain every type exactly once — a "starter relative to
2Z_{p−1}". The lifts f({0,y,y′}) and the copy-1 (c)-triples must then complete both classes.

## L7. Link to Tan–Zhou Construction 2.7 (a published reduction; lead for the next cycle)

Tan–Zhou Construction 2.7 (text lines 732–769): for n ≡ 0 (mod 3), a 1cDCQS(gⁿ : 2) and an
RDSQS(g+2) give an mcDSQS(gn+2). With g = 2 (RDSQS(4) trivial) and n = p−1 ≡ 0 (mod 3):
**mcDSQS(2p) ⟸ 1cDCQS(2^{p−1} : 2)**. Such a CQS with stem {x0}×Z2 and groups {x}×Z2 fills to
an SQS containing every block {x0,x}×Z2. Inside T1 with k = 0 this is impossible: G-invariance
would put every P×Z2 into the SQS (W = {0,1}), excluded by L6(a). For k > 0 or for structures
with less symmetry (e.g. invariant only under the stabilizer of the stem) the route is open; it
remains a concrete alternative formulation, not evaluated.

## Open (irreducible) steps for a uniform proof

(O1) an explicit A-equivariant completion (any k) satisfying L2 for all p ≡ 7 (mod 12),
with W ≠ {0,1} if k = 0 (L6a);
(O2) an explicit rainbow pair (C_1, C_{−1}) as in L5/L6b for that SQS.
Finite evidence only: T1 solutions found by SAT for p = 19 (24/24 samples), p = 31 (sample 0);
p = 43 UNKNOWN within the probe caps (general model 4×480 s; k = 0 model 300 s). The k = 0
SQS layer alone (F3.2c) is SAT at p = 19, 31, 43 and its colouring SAT at 19 (1.1 s) and 31
(3.5 s).
