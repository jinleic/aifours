# KP4 review package: terminal k=p+1, kappa^=p-4 excluded for every prime p>=11; p=7 pure case; p=7 obstruction, v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T16:33:32-0700. CANDIDATE_UNVERIFIED written proofs, outcome O3 (NOT KP4-EXCL for
every prime p>=7). Parent owns both-family reviews and verdicts. No scientific computation, enumeration by machine, solver,
model CLI, test/build or Lean. No novelty, priority or human-review claim.

## 1. Review exactly these frozen texts

- proof-KP4-v1.md, SHA256 a6308ea8e265869795028fcddbdfaaa5a01f0ec514b587da0a6c227af1efaacf, lines 1-243, 22,409 bytes, read
  with erratum-1-proof-KP4-v1.md, SHA256 cb2802c6e7fb7942e83fd84b3dd720e99cfd4103866340f4266184780f9747ef (wording only:
  the arc in the (5,2,1^5) profile of Sec. 7.3; the scope of the Sec. 3 heading).
- obstruction-KP4-p7-v1.md, SHA256 cdac29f484dfd5de4587b2ada214c27c0018052ce8bf8a01df929c3c85ff0462, lines 1-74.
- Scope KP4-EXCL-scope-v1.md, SHA256 ba13fdd35cb02b11b179c8a9087737cf35e55f9197ae4512dac62edf9cc51c4f, frozen 16:04:10
  BEFORE derivation, with the prior KP3/UH sketches disclosed as plans. Authority: RUN/control/six-slot-written-resumption-
  20261019-1603-v1.json, SHA256 ac09b46532a233c6d9ce1b227c3dffecee9655bd83413d96d3a403065a0ef0f8 (slot math-2).

Claims (all under the FULL antecedent: some admissible NF of a length-(4p-2) avoider has terminal k=p+1, kappa^=p-4, H^=3
distributed arbitrarily among odd blocks, empty runs separating different reflection values; no o_F/run/pair hypothesis):
(A) Theorem KP4-A: no such avoider for any prime p>=11 (stronger word form proved).
(B) Proposition KP4-7P: at p=7, no such avoider whose rotation letters are all equal.
(C) Lemma KP4-7N: necessary conditions at p=7 (dominant class, A>=7, A'<=3, window, dominant !=8 at m=2,3).
(D) Obstruction note: Lemma PR (pair case delta=0: attained sets depend only on epsilon=A'+d(P); empty-run bounds) and Lemma
B1 (all-plus constraints for b non-a letters), plus the exact residual R7 and route failures F1-F4.
Not claimed: KP4-EXCL at p=7 with a non-constant rotation multiset; other cells; whole upper/lower half; reflection rigidity,
INV*, REFL, o_F assembly, ordered Olson, p=5; multiset-only non-existence outside the full NF antecedent.

## 2. Manifest, imports and byte boundary

Governing review-excerpts-KP4-v1.json, SHA256 0ed2ba4edb3be82ab4ee1fa86bbe8cf253e54bb0bdbe0870bcdda9eebed58fe1 (4,316 bytes):
JSON list {path,sha256,start,end}, whole-file SHA256, inclusive LF line ranges, absolute paths; 18 ranges from 17 files;
selected raw bytes 63,488, LF-numbered 65,979. Package + manifest + numbered excerpts stay below 100,000 bytes.
Load-bearing inputs of proof-KP4-v1.md ONLY: NF (ROT-few-E-v4 28-43; lowodd item 2/M1/M4, fewodd addendum 1 line 12, ZX
overlays 1-3), GRX if direction (notes-GRX 7-20; lowodd item 1/M2), RS(b) (proof-ROW 16-27 with R5) and classical
Cauchy-Davenport (proof-ROW 4-5). CT, Lev, S(p), KP3/UH candidates, PP1/KP2 endpoints, ASSEMBLY-P and RPdelta are not used.
Input change recorded in the obstruction note ONLY: accepted UH-A (RUN/review/olson-UH-CONSTRAINTS-parent-verdict-v1.md 7c7b90f2...
with errata v1-v3, all in the manifest) narrows the p=7 residual to A in {9,10,11}. It is not used by the proof file.

## 3. Argument map and hostile-review focus

1. SR4 (Sec. 1): all l_i odd, delta_GRX=N-Phi, C_max=Phi+6; every even C in [Phi,Phi+6] by GRX's own statement; n=2p-2j with
   j in {m,...,m+3}; 2p<=R needs p>=9.
2. Sec. 2 [RE-DERIVED]: p-1 unequal pairs need 2(p-1)<=R=3p-9 (p>=7), p-7 unpaired fillers; dominant >=2p-7 in a common
   class {a,-a}, a!=0 (pigeonhole arc, n=2p-8); A'<=p-4 (n=2p-6), A<=2p-1 (n=2p, p>=9); window gap p-5+delta.
3. Sec. 3: Lemma MW (exact omission counts, s!=0, q>=1; CD on q distinct translates). Instances: K-values p-9+2m+{0,2,4,6};
   m=2: phi>=2p-5; m=3: phi>=2p-4 (p>=10); m=4: phi>=2p-4 (p=11 needs the phi=15 check).
4. Sec. 4 [RE-DERIVED]: the m=4 toggle path from {0,2,4,6} (N>=12); super-heavy h with d_h>=p+1+delta; light sets
   (0>=3+2delta); lambda>=0; A=2p-8+c, c=1..7; |E|+|Q|>=c+1, |Q|<=c-1, |E|>=2; strong bounds L2 (c-3), L34 (c-4).
5. Sec. 5: actual subset sums of b weights; n>=2p-12>=b; r=8-c-2j; free (r<=0) and (N1) (r=1) cases; integers <=10 distinct
   for p>=11.
6. Sec. 6 [NEW]: c=1,2,4 by forced missing residues; c=3 by no independent triple in E u Q then four empties and a triple at
   j=3; c=5,6 by |E|=2 and the pure-a singleton runs Q with m=2/m=3 sets; c=7 by t<=3, s-bounds for pairs, |E|<=3 (consecutive
   triple), then |Q|>=5 with m=2/3/4 sets (the middle empty supplies the third interval).
7. Sec. 7 [NEW, p=7]: exact attained intervals [max(-nu,nu-alpha), min(nu,12-alpha-nu)]; seven-residue instances
   (m=1 alpha=6; m=2,3 alpha=4,6,8); empties t in {1,2}, no two non-adjacent empties; profile enumeration for |E|=0,1,2
   (read Sec. 7.3 with erratum E1).
Endpoints: p=11 (MW m=4 phi=15; s+5=11 wrap in c=7), p=13; N=12 cycle facts (no triangle, path toggles); every free/(N1)
use; filler bounds n-|J|<=A and |J|<=n; the p=7 profile lists' completeness; a=0 only in the excluded Lemma U branch.

## 4. Requested verdict boundary

Judge (A) and (B) at the exact full-NF antecedent, (C) and the two lemmas of (D) as necessary conditions, and confirm that the
obstruction does not overstate (R7 is the unfinished word-level target of this route, not a proven-necessary lemma). Flag
import-scope issues separately from mathematical gaps and check the [RE-DERIVED]/[NEW] labels.
