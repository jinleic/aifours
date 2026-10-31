# Shor RAW finite candidates — actual b-transition powers stabilize to rank one

Owner MathShor-2. Actual `/bin/date` before composing: **Mon Oct 26 06:37:38 PDT 2026** (earlier observation bound). WRITTEN/unreviewed. Exact symbolic proofs from a hypothetical actual finite code and the fixed literal b seed. No numeric parameter/control trial, withdrawn Taylor guidance, scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent or new GO.

This packet proves a MATRIX property of the ACTUAL finite raw parser. It explicitly does NOT transfer that property to the cyclic one-b residue graph without a preservation theorem. It therefore distinguishes a genuine finite-raw reset from the previously proved abstract residue/complement resets.

## 1. The actual finite flower graph, with labels and multiplicities retained

Let M be ANY finite RAW UD code containing b, and let L be its maximum codeword length. No completeness is needed for the matrix theorem. Build the finite directed labelled graph with one base state0 and, for EVERY codeword c of length ell>=2, its OWN private ell−1 interior states along the path spelling c from0 back to0. A length1 codeword is a loop at0. Private paths of different codewords are NOT merged. Let P,Q be the0/1-counting adjacency matrices for labels a,b respectively; multiple different paths are counted, never Boolean-clipped.

Every base-to-base path spells an actual M-word list, and conversely. UD makes that list unique. More generally there is AT MOST ONE path between ANY fixed two graph states with a given raw label: prepend the fixed path from0 to the starting interior state and append the fixed suffix path from the final state to0. Two different middle paths would give distinct full base-return paths with the same raw label, hence distinct M-word lists. This extension uses the actual private paths; it is not cancellation of a^n or b in M*.

In particular EVERY entry of EVERY letter-word matrix P/Q product is0 or1. This is a finite unambiguous graph, not a deterministic-automaton ansatz.

## 2. Exact b-factorization of long paths

There is no pure-b codeword other than b, by UD. Removing the base state from the flower graph leaves a disjoint union of directed paths, with no cycles of ANY labels. A b-only path can traverse at most L−1 interior edges before it either reaches0 or stops; once it reaches0 it can take the b loop. It can leave0 only along the proper initial b-segment of some codeword that later contains a, so such a departure lasts fewer than L b-edges before it stops or would need an a. There is no second nontrivial b-only return to0.

For a state u let ell_u be1 if its unique remaining private suffix path to0 is entirely b, and0 otherwise; set ell_0=1. For a state v let r_v be1 if its unique private prefix path from0 is entirely b, and0 otherwise; set r_0=1.

For EVERY integer k>=2L, any b^k path from u to v must reach0 and then, possibly after b loops, leave along that private prefix. It exists EXACTLY when ell_u r_v=1. The required numbers of initial/final b-edges are individually below L, so k leaves a nonnegative number of b loops; this path is unique. Consequently

    Q^k = ell r^T  for EVERY k>=2L.                      (RANK1)

The vectors are nonzero because their base coordinates are1, so this matrix has rank exactly1. This is an actual finite bound depending on the UNKNOWN actual M, not a uniform bound on the original completion problem.

Also r^T ell=1: a nonbase state cannot be reached from0 AND return to0 along entirely b-labelled private pieces, because its complete codeword would then be a forbidden pure-b word other than b. Thus the rank-one matrix E=ell r^T is an idempotent, EQ=QE=E, and the powers are genuinely stationary, not merely bounded or subsequential.

## 3. Spectral and finite-state consequences, without an eigensolver

The identity Q^(2L)=Q^(2L+1) implies that the minimal polynomial of Q divides x^(2L)(x−1). Hence every eigenvalue is0 or1, the1-eigenspace is simple, and all other generalized eigenspaces are nilpotent. This follows by polynomial algebra; no spectrum was evaluated.

Because every raw transition product has0/1 entries on a finite state set, the transition semigroup is FINITE. It contains the ACTUAL rank-one idempotent E represented by the raw word b^k for every k>=2L. If M is additionally complete, the preceding marker packet gives the stronger raw-language sandwich and synchronizing-pair statements. None is an inference from Perron radius alone.

Conversely a finite unambiguous graph with a rank-one b-idempotent is NOT automatically the flower graph of a finite complete code containing C. Base-return finiteness, literal short-word paths, all actual codeword cuts and completeness remain independent requirements. No arbitrary graph is called a completion here.

## 4. Exact comparison with the arbitrary-Y cyclic graph

The earlier actual-Y packets define a DIFFERENT graph on Z_n, with a-edges around the whole a-cycle and b-edges i->−j for the ACTUAL one-b residue pairs(i,j). Its border bijections give endpoint unambiguity, Perron radius1 and rational positive return potentials. Its canonical first-return code is finite iff every canonical i+j<n, and the Shor setting fails that finite branch.

Those facts do NOT identify that cyclic graph's b-matrix with Q of§1. Compressing long a-runs modulo n can insert/remove a^n blocks and alter short zero-gap cuts. No graph homomorphism/similarity that preserves all raw b^k path counts has been supplied. Therefore it is invalid to import RANK1 into that graph or use its failure there as a non-completion theorem.

**Precise missing bridge.** Either derive from the full actual M extraction a raw-label-preserving quotient/linear subquotient whose b-powers inherit RANK1 and which still retains the literal Shor paths, then prove those inherited requirements incompatible; OR construct a different finite raw parser satisfying them. Any claimed finite history splitting of the cyclic graph must state and prove which label-count/cut invariants survive. A bare finite complement automaton, abstract synchronizing word, bounded linear span or positive carry potential is not that theorem.

This is an all-finite-candidate invariant, with arbitrary word lengths/b-counts/delays retained. It is not an actual parser, finite witness, raw STAB conclusion or a repeated660/1320 filter. Original Shor completion **NOT_PROVED** either way.

I3/I4/I5 are NONPREMISES. H* remains FALSE/WITHDRAWN. Own permanent v109-A exactness MAJOR and NEW v34 written-scope MAJOR/all older findings remain; the withdrawn Taylor/control packet receives ZERO credit and is not repaired or repeated. No source/shared/frozen edit, git/deletion/publication, new scientific GO, formal/kernel/human/configured-family/executable/novelty acceptance or early final park. Same original cutoff and deadline.
