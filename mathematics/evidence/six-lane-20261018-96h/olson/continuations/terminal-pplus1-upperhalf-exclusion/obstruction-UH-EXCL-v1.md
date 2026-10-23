# UH-EXCL obstruction: what remains after UH-A / MW / SH / L, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T13:46:10-0700. Status: CANDIDATE_UNVERIFIED written partial results and honest
obstruction, outcome O3 of UH-EXCL-scope-v1.md 6ff7fec519944d57c3162f45e1b19403b12a8bea19647634dc86ba20e03d15e9.
Companion proof-UH-CONSTRAINTS-v1.md 56327b678bf9f7fe62d6f518499ab692f00897a3ecff2c62ddecac4a42a5115c contains full proofs
and the import/scope table. Neither this packet nor the parent model-review process has proved the frozen target UH-EXCL.
No genuine word counterexample is supplied. No abstract count configuration is described as a word or an avoider.

## 1. Original target and exact delivered restriction

Original UH-EXCL: prime p>=7, (p-1)/2<=kappa<=p-3, NO length-(4p-2) avoider w has SOME admissible normal form u with terminal
k=p+1,kappa^=kappa; H=e-1 (e=p-kappa) is arbitrarily distributed among its p+1 odd blocks; every empty run separates different
block values. No o_F, nonempty-run or reflection-rigidity hypothesis.

Delivered instead (explicit O3, no silent replacement):
- UH-A excludes the subcase A<=2kappa+2, UNIFORMLY at every kappa in the original interval. A is the larger multiplicity in the
  common nonzero dominant pair from the re-proved Lemma U. This is a word-level necessary constraint, not a multiset-only
  non-existence theorem outside the stated NF antecedent.
- MW is a new omitted-letter/count-of-lengths constraint on every non-constant pattern; no dominant pair is silently assumed
  for an arbitrary value s, and s!=0,q>=1 are explicit.
- SH, only when 3e<=p+2, forces a super-heavy run, ordinary light sets outside it, and at least two empty runs. It is NOT an
  exclusion for this e-band.
- L gives exact pair-valued low-arc windows and their additive lifts; delta=0 is an explicit extra hypothesis. PH excludes only
  the pure case with a run of >=p letters. It does not exclude the pure case with every run <p.
No entire kappa cell is claimed excluded by this packet. The range 1<=kappa<(p-1)/2 is not addressed.

## 2. Residual parameter and word-level interface

Every putative remaining avoider with the FULL antecedent must have
  A=2kappa+c, 3<=c<=2e-1, b=R-A=p-1-c in [p-2e,p-4],
  A'<=kappa, delta=b-A'>=0, delta<=p-2,
  d(P)=alpha(P)-beta(P)<=lambda=c-2 OR d(P)>=Lambda=2kappa+1-A'
for every proper nonempty set of runs P. The actual word's block values y_i determine tau_i=y_i-y_(i-1), tau_i!=0 at empty
runs; sum_i tau_i=0. These residues cannot be chosen independently for different arcs: T(z_P)=sum_(i in P)tau_i.

For each pattern z with 2m changes, SR requires every even n in
  [max(0,2kappa+2-2m),min(2p-2m,R)]
to MISS its target T(z) among actual n-letter signed sums. Both the block values/order and each occurrence's own run are part
of the remaining problem. Counts satisfying W/MW alone do not supply such a word. The distribution of H within odd blocks
changes no SR endpoint, but it must still be realised by actual odd block lengths in any word counterexample.

Smallest unresolved residual statement in this proof decomposition (not asserted mathematically necessary among all possible
methods):
  (R-UH) Under precisely the full word/NF antecedent and the residual bounds above, some sign pattern z and some even n in SR
  have T(z) among their actual n-letter signed sums.
UH-A covers the complementary A-range, so proving R-UH would complete UH-EXCL. R-UH is NOT supplied as a lemma or a premise;
it is the remaining word-level claim. There is no missing numerical evaluation or unknown external datum that could be
substituted for its proof. The narrower route gaps below identify where this attempted derivation stops.

## 3. Exact heavy-run / light-set gap, with the inequalities retained

The ordinary W gap is g=p-2e+3+delta; lambda=p-2-b=c-2. The first-passage proof gives a high SINGLE RUN only when
  g>lambda <=> b+delta>2e-5 <=> b+delta>=2e-4.
If this fails, all single runs may stay low in the inequalities and a prefix jump of size g need not exceed lambda. No heavy
run is inferred then. Even if a high h exists, a disjoint high set forces only
  A>=2Lambda <=> A'>=p-2e+3+delta.
This contradicts A'<=kappa whenever delta>=e-2; it need not contradict it for delta<=e-3. The exact sufficient bound is
A<2Lambda, not the uniform delta bound as a necessary condition. When A=2kappa+2, equality forced the two-high-set structure
used in UH-A. For c>=3 equality has slack: alpha_1+alpha_2 can exceed 2Lambda, and beta on the high sets need not vanish.
The collapse of all -a letters into one run was proved ONLY for c=2 and is not reused at c>=3.

When 3e<=p+2, SH resolves these two route gaps by a different path argument: alpha_h-beta_h>=p+1+delta and all sets avoiding h
are ordinary-low. This still stops at the empty-run/residue problem of Sec. 4. When 3e>p+2, the strong m=e MW consequence
can fail at its arithmetic branch: the possible band
  2kappa+3-2e <= w0 <= 2e-3
is no longer empty. There is no claimed super-heavy run outside the SH range.

## 4. Exact empty-run residue constraints and why the endpoint argument stops

If a high h with ordinary-light sets exists, Sec. 2 of the proof gives lambda>=0 and >=2 empty runs. Let B be all b non-a
rotation occurrences, omega(u)=x_u-a!=0, G their subset-sum set, M=Z_p minus G. RS(b) gives
  |M|<=p-1-b=c; 0 not in M; M=sigma(omega(B))-M
(the last identity is complement symmetry of subset sums). For a pattern with negative side empty, the exact restriction is
  T-na not in {sum_J omega: J contained in B, |J|<=n, n-|J|<=A}.
Only if b<=n<=A is every subset J allowed and T-na in M justified. Large n>A requires a lower bound |J|>=n-A; small n<b
requires the upper bound |J|<=n. These constraints are not dropped.

For a concise set interface, divide all residues by 2a (a!=0), write M*=M/(2a), t_i=tau_i/(2a) for empty runs, mu=floor(c/2).
With c>=3 and 3<=e<= (p+1)/2, 1<=mu<=e-1. From lengths n=2kappa+2j that are FREE (b<=n<=A) one obtains:
  all-plus, j=1,...,mu:                  [e-mu,e-1] contained in M*;
  one empty run i, j=0,...,mu:           t_i+[e-mu,e] contained in M*;
  two ADJACENT empty runs i,l:           t_i+t_l+[e-mu,e] contained in M*;
  two NONADJACENT empty runs i,l:        t_i+t_l+e-j in M* for every j with
                                       -1<=j<=min(mu,e-2) and 2kappa+2j>=b.
For the last line the j=-1 length can fail the free lower bound at the bottom endpoint, so its qualification is retained.
All intervals are integer intervals reduced mod p. Also t_i!=0 for each empty run. This is a concrete new interface for
coupling all-plus/single/pair constraints without assuming nonempty runs or ignoring filler availability.

At c=1,2 these constraints plus one restricted non-free length produced the UH-A contradiction. At c>=3, |M|<=c alone is not
a contradiction to one forced interval of length mu+1, nor has this work shown that the union of the forced single/pair
sets always has >c elements. M is an actual subset-sum complement with the stated symmetry, NOT an arbitrary set of c
residues, and sums from the non-free lengths must also be used if needed. The missing local step is an exclusion of actual
word-realised (B,empty positions,tau) data satisfying these constraints, OR an argument using the nonempty runs to find an
additional pattern. No blanket assertion that "two empty runs are impossible" is made for c>=3.

## 5. Pure-pair and lift route: precisely what is and is not closed

With the explicit delta=0 hypothesis, low arcs have an exact forbidden interval [kappa-epsilon,U] modulo p. Its complement
has unique representatives in [U+1-p,kappa-epsilon-1], NOT necessarily a nonnegative interval. Proposition L proves the
representatives add along a path all of whose consecutive subarcs are low. Empty runs have nonzero lifts, but those lifts
can be NEGATIVE when U<p-1. Thus counting every empty lift as >=1 is invalid in the general pair case.

The pure-heavy corollary PH is special: kappa=(p-1)/2 and all rotations are a, with a run of >=p letters. There every empty
lift has lower bound 0, hence is >=1; the pieces between empty runs have D>=-1/2, giving the budget contradiction. Without
that large run, it was not established that the needed path consists only of low arcs. With mixed a,-a letters, even such
a path can have negative empty lifts. No PH extension to all pure words, all delta=0 words, or all upper-half cells is made.

The first direct single-run omission attempt also stops exactly: for a pattern with one negative run, omitting p-1 letters
selects 2kappa rotations. If A-alpha_i>=p-1, the free weights have b+alpha_i-beta_i nonzero terms, so RS(b) with K=p-1 forces
  alpha_i<=beta_i+p-2-b = beta_i+lambda.
At lambda>=1 this allows pure-a light runs; they do not all consume a scarce non-a letter. The proof of UH-A used arbitrary
sets and then the c<=2 empty-run analysis, not a false single-run count at larger c.

## 6. Failed-route and checkpoint corrections (old checkpoints preserved)

The checkpoint files are exploratory notes, not review premises. Read them with these explicit dispositions:
- Checkpoint 001's sketch of excluding the whole pure cell used U=p-1 for low arcs, which is incorrect in general. The correct
  U=min(p-1,floor((R-epsilon)/2)) is proved in Proposition L. Only the pure-HEAVY corollary PH is claimed. Checkpoint 002
  already recorded this issue; its "all runs <=p-2" branch is not closed here.
- Checkpoint 001's wording "two high sets impossible iff delta>=e-2" is too strong. Delta>=e-2 is a uniform SUFFICIENT condition;
  the exact inequality is A<2Lambda. Neither mathematical necessity nor impossibility in every smaller-delta case is claimed.
- Checkpoint 002's simplified general-m MW band is superseded by the exact calK/count statement of Lemma MW; only its m=e
  consequence under 3e<=p+2 is claimed. Empty calK and the minority-size/filler constraints are explicitly handled in the proof.
- Checkpoint 003's sketch that two empty runs force floor(c/2)+2 elements of M by CD was NOT established uniformly and is NOT
  a claimed bound. The exact forced-set families and |M|<=c above replace that shorthand. No subset-sum upper bound is inferred
  from an occurrence count.
- No FLEXa/PM* expansion from a lower-kappa word to PP1/KP2 was proved; deleting a reflection pair and inserting rotations
  need not preserve avoidance for selections using exactly one inserted letter. No endpoint candidate is used as a shortcut.
- RGR-LONG/RUNS and accepted ASSEMBLY-P/RPdelta notices were read as context only; none is an allowed premise here. In particular
  o_F<=p cannot be supplied at terminal k=p+1, and a pure-pair rotation conclusion supplies no REFL extension.

## 7. Review and handoff boundary

Review the new candidate NECESSARY constraints and restricted exclusions, not UH-EXCL as a proved theorem. The interface table
in the companion proof pins NF, GRX, RS(b), CD; no other premise. New versus re-derived labels are explicit. Old packets are
unchanged, all files exclusive-created. No model CLI, scientific computation, solver/enumeration/test/build/Lean run, paid API,
external contact, publication or commit. Model-family reviews and verdicts belong to the parent. No novelty/priority, human
review, full REFL/INV*/ordered-Olson, or lower-half result is asserted.
