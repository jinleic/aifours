# KP3-EXCL review package: exact terminal k=p+1,kappa^=p-3 exclusion, v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T14:03:09-0700. CANDIDATE_UNVERIFIED written proof. Parent owns model-family
reviews and verdicts. No scientific computation/enumeration, solver, model CLI, test/build or Lean run. No novelty, priority,
human review or formal verification claim. This is the EXACT NEXT CELL, not whole-upper-half exclusion.

## 1. Frozen scope and exact candidate

WHOLE proof-KP3-EXCL-v1.md, SHA256 d72f277f5bdcc89526217d45c47aac973f668b26832eafe9735b8b8dfb9ff0e4,
lines1-248,21,574bytes. Scope KP3-EXCL-scope-v1.md, SHA256
58ca7d6281f5532b85536efb1cb7c0fb6e30dcabbca3bac3e0fea7b8c678c169,lines1-45,4,136bytes; frozen13:54:42 BEFORE derivation.
It explicitly records Main's UNVERIFIED guided hypotheses; classification/exhaustive reduction were not known at freeze.
Authority transition mathematics-slot-transition-olson-20261019-1353-v1.json whole SHA256
0387d1c89f3d093876b77a6c46e60607ad1e6aa515fc8c986c784676c76c59bf; no additional problem/runtime authority.

THEOREM KP3-EXCL: for every primep>=7, no length-(4p-2) avoider w over D_(2p) has SOME admissible NF u with terminal k=p+1,
kappa^=p-3. H^=2 is arbitrarily distributed among odd blocks (one length5 or two length3; others singletons), F=p+5,R=3p-7.
No o_F, nonempty-run, reflection-rigidity or rotation-pair hypothesis. Every empty NF run separates DIFFERENT block values.
Stronger word form is explicitly proved: no avoider u with that cyclic odd-block/empty-run representation exists.

Keep the FULL NF/word antecedent on every consequence. No unrestricted rotation-multiset exclusion or other-cell statement is
requested or asserted. Accepted PP1/KP2 endpoints, pending UH/ROT-PP1 arguments and ASSEMBLY-P/RPdelta are not premises.

## 2. Manifest, input trust and embedded boundary

Governing review-excerpts-KP3-EXCL-v1.json SHA256 e6ec72f1a3ee6653682cd497c686f906c0eb25558c95f0c015582bcbb390835c
(3,655bytes): JSON list {path,sha256,start,end}, whole-file SHA256, inclusive LF line ranges, absolute paths. 15 ranges from13
files; selected raw bytes49,628, LF-numbered selected bytes51,759. Package+manifest+numbered excerpts remains below100,000bytes.

ONLY accepted inputs: NF (ROT-few-E-v4 28-43, empty rule38, accepted lowodd item2/M1/M4, fewodd addendum1 line12, ZX overlays1-3);
GRX IF direction (notes-GRX7-20, lowodd item1/M2, every cyclic constant-block representation and pattern, empty runs allowed);
RS(b) (proof-ROW16-27, mandatory R5 at prerequisite erratum36-38: integer K>=0/nonzero terms); classical Cauchy-Davenport
(proof-ROW4-5). CT is not needed. No inverse zero-sum or critical-sumset theorem is imported.

Old UH excerpts and its parent erratum are comparison context ONLY: new proof Secs.2-4 re-derive each needed argument in full.
The shorthand "upper-half/proof-UH-CONSTRAINTS-v1.md" at the proof footer denotes the actual
terminal-pplus1-upperhalf-exclusion/proof-UH-CONSTRAINTS-v1.md absolute path in the manifest. Its corrected lambda=c-1 is used;
no old proof file is modified. Main's suggested critical missing-set classification and reduction have their proofs here,
not the status of an accepted premise.

## 3. Argument map / requested hostile checks

A. Sec.1: F=p+5,R=3p-7; all blocks odd give delta_GRX=p+1-Phi, C_max=Phi+4. At a fixed parity f_i, available counts in block i
are f_i+2j_i,0<=j_i<=h_i, with sumh_i=2. Thus EVERY C=Phi,Phi+2,Phi+4 is realised for either H-distribution. SR3 uses
max(0,2p-4-2m)<=n<=min(2p-2m,R), even. No empty/nonempty shortcut.

B. Sec.2 [RE-DERIVED]: unequal pairs M; P uses n=max(p-1,2p-4-2m), p-1 pairs, p-5 unpaired fillers, and RS(b) on p-1 nonzero
swap differences. Dominant signed count>=2p-5 and unique class {a,-a}; a!=0 via repeated y_j arc at n=2p-6. All-plus gives
A<=2p-1,A'<=p-3. Ordinary W low threshold lambda=A-2p+5, high Lambda=2p-5-A'. No rotation-pair conclusion is assumed.

C. Sec.3 [RE-DERIVED at this cell]: MW3. For the dominant signed value s!=0, minority w0<=p-2 and phi>=2p-5>=p+2. Omit any
minority subset plus dominant fillers to reach K=p-1,p+1,p+3 when K<=phi; these correspond to the three m=3 lengths.
RS(b)+CD yields min(p,w0+q). If phi>=p+3 then q3 gives w0<=p-4,phi>=2p-3. Otherwise phi=p+2 gives w0+q=2p-7>=p,
contradiction (p=7 equality included). Check all occurrences/fillers, distinct translates, no zero s.

D. Sec.4 [RE-DERIVED in full]: m=3 split gap p+1+delta; explicit single-toggle path from {0,2,4} to its complement, all m3,
valid also at cyclelength8. A low->high step cannot delete a run since beta_i<=p-3; it adds h with d_h>=p+1+delta. Any ordinary
high set avoiding h overloads A. All sets avoiding h are ordinary-low; lambda>=0 (else A'>=p); hence
A=2p-6+c,c1..5,lambda=c-1. The usual nonempty-run count forces >=2 empty runs. Every m3 set avoiding h is STRONG-low,
d(P)<=c-3. The reduction does NOT import UH-A: c1,c2 are handled anew below.

E. Sec.5: actual non-a letters B, weights (x-a)/(2a), subset sums G, missing M with |M|<=c,0 not in M. Negative-empty-side
patterns leave every rotation positive. Every J subset B with |J|<=n,n-|J|<=A gives an actual selection. If b<=n<=A,
t-n/2=t+j is in M. If n=A+1, every NONEMPTY J is allowed, so t+j is in M or0. Do NOT replace G_nonempty with G: zero may have
only the empty representation. All m0,m1,m2 lengths used satisfy n>=b (2p-8>=p-2 for p>=7).

F. Sec.6 [NEW closing changed-cell cases]:
- c1: j3 free, j2 has n=A+1 => empty t=-2,M={1}; pair j3 forces-1 inM.
- c2: all-plus j2 plus single j2/j3 => empty t=-1,M={1,2}; pair j2 forces0.
- c3: all-plus j1 has n=A+1 but residue1!=0, so1 inM; j2 gives2. For an empty t, j1 is non-free, j2/j3 free. Unless t=-1,
  a length3 interval avoiding0 joins {1,2}, requiring>=4 missing residues against<=3. Empty pair j2 then forces0.
- c4: all lengths used free; I_t=t+[1,3] inM and base{1,2},|M|<=4 force t=1,M={1..4}. Pair j3 requires5.
All pair lengths used are admissible whether the two empties are adjacent or not.

G. Sec.7 [NEW elementary complete classification c5]: |M|<=5,base{1,2},I_t=t+[1,3] inM. Canonical t in[1,p-4] from0 notinM
and t!=0. If t>=3 then M is two components of sizes2 and3; its only three-interval is I_t. Any second empty has the same t;
adjacent pair forces t=0, nonadjacent pair forces t=-1, both impossible. Thus t in{1,2}. If t2 exists, M={1..5}; its pair
with t1/t2 forces6 inM, impossible. All t1: a nonadjacent pair requires all1..6 inM; thus empties are pairwise adjacent,
so exactly TWO on a cycle>=8. Their adjacent pair gives M={1..5}. This PROVES the guided classification, no inverse theorem.

H. Sec.8 [NEW final position count and cycle lemma]: exactly two empties, h nonempty. Of p-2 nonempty outside-h runs at most
b=p-6 carry a non-a letter, so at least4 are pure-a. Their whole set is ordinary-low with total d<=lambda4; therefore EXACTLY
four pure-a SINGLETON runs Q. With disjoint adjacent empty pair E, construct P subset Q union E with m3 and at least3 Q.
If Q has an independent triple, use it. Otherwise induced Q components are a path4 or two paths2+2. In the path4 case one E
vertex has no Q neighbor (otherwise cyclelength6), supplying the third interval to a suitable Q triple. In the2+2 case either
an E vertex is isolated from Q, or E is the gap2: drop a neighboring Q endpoint and take that E vertex, creating three
intervals with3 marked vertices. P avoids h, but d(P)>=3 contradicts strong m3 low bound c-3=2.

## 4. Endpoint, scope and verdict requests

Check p=7 throughout: R=14, m3 lengths4/6/8, phi=p+2 branch, b=p-6=1,c5, cyclelength8. Check arbitrary extra-pair distribution,
rho_0 among deviants, a=0 only in the explicitly excluded Lemma U branch, empty adjacency and all free/non-free n=A+1 uses.
No ordinary-window-only contradiction is claimed: ordinary lambda4 permits the four pure-a singletons; the m3 constraint is
essential. No missing-set cardinality bound alone is called a classification.

Requested verdict: correctness of KP3-EXCL at the EXACT full NF antecedent and the stronger stated word-form assertion,
relative to the listed accepted interfaces; separately flag import-domain issues and errors in new/re-derived labels. Parent
owns both-family review and verdict. Not requested/claimed: other terminal cells, whole upper half, reflection rigidity,
INV*, full REFL/ordered Olson, o_F assembly, p=5, multiset-only non-existence elsewhere, novelty/priority, Lean/human review.
