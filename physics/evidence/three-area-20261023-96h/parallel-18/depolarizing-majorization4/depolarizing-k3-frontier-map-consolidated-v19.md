# Four-qubit depolarizing majorization — consolidated per-index verdict and the k3 frontier map (v19)

Actual `/bin/date` before drafting: **Sun Oct 25 23:33:59 PDT 2026** (checkpoint071). Owner PhysicsDepol4-2 / physics-2. **CONSOLIDATION ONLY: no new theorem in this file.** It maps every current statement to its pinned source, imports and assurance so one gate can read the k3 frontier at once. Pinned sources are not edited; their own wording governs. Strict WRITTEN/static-read/metadata work; no interpreter/eval/program/CAS/enumeration/solver/CLI/nested agent/GO. HOLD, own root, October27 cutoff11:05:38/deadline12:35:38, all process findings (including the checkpoint062 own cadence lapse) retained. Zhang's matched clipping claim (`source-audit-v2-zhang-prior-claim.md`) and unclear priority remain binding; no novelty claim.

## 1. Target and reduction

Target (SWTF arXiv:2609.37240v1 Eq.(2), d=2, n=4): lambda(D_p^(tensor4)(rho)) is majorized by lambda(D_p^(tensor4)(|0000><0000|)) for every rho and 0<=p<=4/3. With z=p/[2(1-p)], D_p^(tensor4)(rho)=(1-p)^4[rho+zX3+z^2X2+z^3X1+z^4 I]. For rank k the comparison is implied by the U-type bounds and, at low noise, reduces per (rho,Pi) to the scalar cubic/quartic frontier (`depol-quartic-frontier-parent-v1.md`).

## 2. Per-index verdicts (exact assurance)

|index|verdict|authority|
|---|---|---|
|k1,k5,k11-k15; high-noise k2-k4 (p in[2/3,4/3])|inherited computer-assisted certificates, NOT replayed this round|six-lane frozen-partial-v1|
|k2 (all p)|WRITTEN_SUPPORTED (parent), M1 branch overlay mandatory|`depol-original-k2-operator-parent-v1.md`|
|k4 (all p)|WRITTEN_SUPPORTED (parent): Tr(Pi X3)<=7 for all rho, all rank-4 Pi|`depol-original-global-k4-parent-v1.md`|
|k6-k10 (all p)|WRITTEN_CHECKED (parent dispositions §3)|`priority-written-dispositions-v1.md`|
|k3 (0<p<2/3)|OPEN for arbitrary states; containing faces parent-supported; large author-candidate union below|`depol-global-CLIP-v6-parent-v1.md` and §3|

The unrestricted all-index statement is therefore NOT claimed.

## 3. k3 frontier: sufficient statements (each AUTHOR-WRITTEN unless marked)

All rows prove U3 at rank three, K3(X3)<=6, on the stated set (hence original k3 at every physical p via v13 §5, and on convex hulls/LU images), unless stated otherwise.

|set of pure states|source (sha256 prefix)|status|
|---|---|---|
|every containing projector (Pi contains psi)|CLIP parent (204b6ebd)|parent-supported|
|TC-zero (epsilon=0) locus|`depol-tc-zero-rigidity-parent-v1.md` (9b55c9a1)|parent-supported|
|R<=1/5; pairs with a<=9d (SOS, channel level)|v8 (6be989b5)|candidate|
|eta_SP=0 locus|v10 (7fe5d9a3)|candidate|
|R=0 critical locus; C>=8/9|v11 (b54bb1af)|candidate|
|paired-parity span; general W class|v12 union (5bf8194c)|candidate|
|permutation-symmetric sector|v13 (1b0afc41)|candidate|
|K2(Gamma)<=4 (R1); two nearly pure qubits 6(e1+e2)<=(4-2sqrt R)^2 (R2)|v14 (f609beec)|candidate|
|maximal product overlap G>=124/125 (NP)|v15 (b3aba176)|candidate|
|four-cycle family (all G)|v16 (401eb453)|candidate|
|balanced even family; lambda4(X3)>=1 (via parent k4)|v17 (dc3d9e81)|candidate|
|EVERY parity eigenstate Z^(tensor4)psi=+-psi and all LU images (Theorem PAR)|v18 (bee7c7ac)|candidate|

Dependencies: v16-v18 import Z<=4I (v9, via the k4 parent); v14 imports CLIP/UP2/K2M (v6 parent) and the Schur bound (v9); v15 is self-contained linear algebra plus v13 §5. Same-owner chains (v17 on v16) are disclosed; v18 proves v16's open Lemma E directly and does not need v17.

## 4. Exact remaining k3 gap

Pure states with NO product-Pauli eigen-symmetry lying outside every row of §3, with arbitrary complex rank-three projectors and no positive cutoff: prove K3(X3)<=6 (sufficient) or the full off-face quartic D>=0 on its nonautomatic branch, or exhibit an actual state/projector/noise failure. Known structural facts about any U3(3) violator: lambda4(X3)<1 (parent k4); in closest-product normal form it needs a nonzero weight-three amplitude block (else even, Theorem PAR) and G<124/125 (NP); its pair (psi,Pi) must be off-face with a>9d (v8) and violate the exact F2 condition of v14. None of these closes the gap, and no counterexample is known.

## 5. Assurance ceiling

Same-harness author writing and parent written dispositions only; no formal/kernel/human/configured-family/executable/novelty acceptance. The union of candidate rows is not an accepted theorem; each needs its own gate. Parkable consolidation, not a park of the active primary.
