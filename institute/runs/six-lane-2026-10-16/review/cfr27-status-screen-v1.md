# Applicability screen for CFR(5,27) = cyclic (Z_27, 6; 1) difference matrix (written 2026-10-17 14:55:04 PDT)

Scope and rule: CFR(5,27) exists iff a (Z_27, 6; 1)-DM over the CYCLIC group Z_27 exists (notes/facts-v1.md E2).
A DM over the additive group of GF(27) (elementary abelian Z_3 x Z_3 x Z_3) or over Z_9 x Z_3 is NOT a cyclic
Z_27 DM and does not give a CFR(5,27); such objects are recorded as NOT APPLICABLE. Every imported construction
below names its group. A miss is not novelty.

## Checked (pinned in sources/web/*.pin.json)
1. SageMath designs database, develop @ 0835358cba62dc19fccdff54f32e52fded9f22b0 (database.py sha256 55a30e8a…23a9)
   and tag 6.4 @ 21d9db20 (4222abc4…b905): the DM table `DM = {...}` has g in {12,21,24,28,33,35,36,39,44,45,48,
   51,52,55,56,57,60,75,273,993}; no g = 27 entry, no AdditiveCyclic(27), no Z_9 x Z_3 group anywhere in the file.
   Groups of the relevant entries: DM_21_6_1 over AdditiveCyclic(21) = Z_21 (k = 6 -> CFR(5,21), a known CPro1 dev
   instance); DM_33_6_1 over AdditiveCyclic(33) = Z_33 (k = 6 -> CFR(5,33), prior art for the killed target).
2. Sage `difference_matrix()` constructor (difference_matrices.py @ same commit, sha256 3ef40ca4…3222): for prime
   powers g it returns `FiniteField(g)` with M = [[x*y]]; its doctest row "27 27" is therefore a (27,27;1)-DM over
   GF(27)^+ = (Z_3)^3 -- NOT APPLICABLE to Z_27. (Likewise "25 25" is over GF(25)^+ = (Z_5)^2, not Z_25.)
   No product construction yields a cyclic group of order 27 (27 is a prime power; the code takes the field branch).
3. arXiv API, title "difference matrices", newest 100 (sources/web/arxiv-ti-difference-matrices.xml): 9 entries,
   none about cyclic groups of order 27 or about F_c(n).
4. OEIS JSON search "orthogonal orthomorphisms", "circular florentine", "diagonally cyclic latin orthogonal":
   no sequence for F_c(n) or for the maximum number of pairwise orthogonal orthomorphisms of Z_n.
5. CPro1 problem_def.py (sha256 44f4d4ff…70aa): OPEN_INSTANCES contains [5,27]; DEV_INSTANCES contains [4,27].
6. Web search snippets (no pinned bytes; listed for completeness): queries on "Z_27" difference matrix /
   orthomorphisms, F_c(27), "circular Florentine" 27, MODCLS tables, Evans orthomorphism-graph tables: no claim
   of a cyclic (Z_27,6;1)-DM, of 4 pairwise orthogonal orthomorphisms of Z_27, or of F_c(27) >= 5 was seen.
7. arXiv 2308.04837v1 (Zhang-Vinterbo, sha256 6e959a71…e713): quotes only the F(n) (non-circular) table; no F_c(27).

## Not readable (access holes; status of CFR(5,27) NOT established by these)
* Handbook of Combinatorial Designs 2nd ed. III.3 (MOLS, DM examples), VI.17 (difference matrices), VI.62 (Tuscan
  squares, Table 62.27 F_c(n)) -- not accessible.
* H.-Y. Song 2000 (Comput. Math. Appl. 39(11) 31-35) -- ScienceDirect 403 (per screen v2).
* A. B. Evans, Orthomorphism Graphs of Groups (1992) and Orthogonal Latin Squares Based on Groups (2018) -- books.
* I. M. Wanless, Diagonally cyclic latin squares, EJC 2004 (author PDF): HTTP 503 at fetch time.
* A. B. Evans, Quasigroups and Related Systems 23 (2015) survey: www host DNS failure, bare host HTTP 429; reader
  conversion produced no text.
* Discrete Math. 2022 note on pairs of orthogonal orthomorphisms of cyclic groups (S0012365X22003284): 403.

## Conclusion
No cyclic (Z_27,6;1)-DM / CFR(5,27) was found in the readable scope; the field/elementary-abelian (27,k) DMs are
explicitly NOT APPLICABLE. Proceeding with CFR(5,27) per the parent decision (14:5x PDT), with a mandatory
post-result priority recheck (including the DM/orthomorphism literature) if anything is found.
