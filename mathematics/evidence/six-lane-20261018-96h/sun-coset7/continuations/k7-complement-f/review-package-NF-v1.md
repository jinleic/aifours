# K7-NF written review package v1: class K7 outside F has no configuration (assembly of accepted theorems) [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T16:12:05-0700, immediately before this exclusive write.
- **Owner:** SunM13MixedFibres. Written mathematics only; no scientific computation, model call or nested agent. Packaging
  used only sha256, byte counts and raw line-range extraction. The parent owns reviews and verdicts.
- **Candidate:** `K/K7-NF-v1.md`, sha256 `734613fd21d9ea21aa940293c489f40549b74a3ac13d1ce3720db6bc98f73e97` (151 lines, 17,152 B). **Frozen scope:** `K/K7-NF-SCOPE-v1.md`,
  sha256 `2469a967b81d15ade6a11a981678c831b12b60d4e12404733fef8f7d943b351c` (written before derivation; discloses the pre-freeze case sketch).
- Root aliases (exact absolute prefixes): K = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-complement-f`;
  S = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7`; O16 = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7`;
  RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`; R16 = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review`.

## 1. Claim and exact status
**Theorem K7-NF:** no configuration of class K7 (all 21 pairwise index gcds 6) in any group with finite-index subgroups lies
outside F, where F requires a 2-marker z and a 3-marker t with z != t. Every absent/coincident marker case and every
admissible 5-marker placement is covered; all exponents and cofactors are unbounded. **It is an ASSEMBLY**: an exact
elementary eight-block partition (Lemma PART, with marker uniqueness Lemma MK) whose blocks are matched to the literal
hypotheses of the accepted theorems K7-M0, K7-M1 (three blocks), K7-35, K7-Z2, K7-U1 and Z23-P5. No accepted subfamily is
re-proved or counted as new mathematics. **Corollary K7-REM (navigation):** with the accepted (a1) closure, every K7
configuration lies in (a2); (a2) remains OPEN, the A2X candidate units are NOT used. Not claimed: exclusion of K7, of (a2),
or Sun(7); novelty, Lean, human review. Sun(5)/Sun(6) remain computer-assisted transitive imports of the cited theorems.

## 2. Reading order
1. Scope (whole); transition record (whole). 2. Candidate (whole). 3. For each block, the quoted literal statement in the
source file, then its mandatory overlay ranges (each states no statement change), then the accepting verdict lines.
4. For K7-REM only: R2 verdict lines 1-31 ((a1) definition and acceptance) and the (a2) setting in the 1325 transition.

## 3. Verbatim key statements (raw candidate lines)
K7-NF-v1.md:84-86
```text
**Theorem K7-NF [CANDIDATE_UNVERIFIED; assembly of accepted theorems].** No group with finite-index subgroups contains a
configuration of class K7 outside F. Equivalently: every K7 configuration, in any group, has a 2-marker z and a 3-marker t
with z != t. This holds for every admissible 5-marker placement and all exponents and w-cofactors.
```
K7-NF-v1.md:59-71 (partition table)
```text
## 2. Lemma PART (exact partition of K7 \ F)
Every K7 configuration outside F lies in exactly one of the following eight blocks (z, t, p denote the elements of
Z, T, P when nonempty; E, A, B >= 1 are the actual exponents v2 r_z, v3 r_t (or v3 r_z), v5 r_p (or v5 of the 5-marked
vertex), unbounded):
| block | Z, T, P | marked set and marker products |
|---|---|---|
| B1 | Z = T = P = empty | M empty |
| B2 | Z = T = empty, P = {p} | M = {p}, m_p = 5^B |
| B3 | Z = empty, T = {t}, P = empty | M = {t}, m_t = 3^A |
| B4 | Z = empty, T = P = {t} | M = {t}, m_t = 3^A 5^B |
| B5 | Z = empty, T = {t}, P = {p}, p != t | M = {t, p}, m_t = 3^A, m_p = 5^B |
| B6 | Z = {z}, T = empty, P in {empty, {z}, {p} with p != z} | M = {z}, m_z = 2^E 5^(B') with B' >= 0; or M = {z, p}, m_z = 2^E, m_p = 5^B |
| B7 | Z = T = {z}, P contained in {z} | M = {z}, m_z = 2^E 3^A 5^(B') with B' >= 0 |
```
K7-NF-v1.md:129-133
```text
**Corollary K7-REM.** By Theorem K7-NF and the accepted (a1) closure (R2 verdict line 5: "(a1) contains no actual
disjoint-coset configuration, in any group"), every K7 configuration in any group lies in (a2). Equivalently, class K7
minus (a2) has no configuration, by accepted results plus Theorem K7-NF.
**Boundary.** (a2) remains OPEN: the A2X units are candidates under review and are NOT used. K7-REM is not an exclusion of
K7 or of Sun(7).
```

## 4. Source/authority table (rows = manifest entries in order; whole-file sha256; inclusive one-based ranges)
| ID | Path | SHA256 | Lines | Scope / authority |
|---|---|---|---|---|
| NF | K/K7-NF-v1.md | 734613fd21d9ea21aa940293c489f40549b74a3ac13d1ce3720db6bc98f73e97 | 1-151 | NEW candidate (whole): Lemmas SHAPE/MK/PART, Theorem K7-NF, Corollary K7-REM |
| SC | K/K7-NF-SCOPE-v1.md | 2469a967b81d15ade6a11a981678c831b12b60d4e12404733fef8f7d943b351c | 1-54 | frozen target, premise discipline, pre-freeze disclosure |
| TR | RUN/control/six-slot-written-resumption-20261019-1603-v1.json | ac09b46532a233c6d9ce1b227c3dffecee9655bd83413d96d3a403065a0ef0f8 | 1-42 | parent authority (slot math-1) |
| README | O16/README.md | 2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1 | 27-29, 33-52, 85-97 | accepted (written verdict): R0, CE, P0, P1, class K7 row |
| WV | R16/sun-coset7-written-parent-verdict-v1.md | 73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35 | 16-23, 44-46 | accepting verdict for README; overlay A-1 (h_i) |
| LFC | S/K7-LFC-INV-v1.md | 45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c | 8-11, 111-121 | accepted: K7 notation; Theorem K7-M0 statement and proof |
| LFCE | S/K7-LFC-INV-erratum-v1.md | 7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5 | 1-10, 82-85 | mandatory overlay: no statement change |
| VLFC | RUN/review/sun7-lfc-inv-parent-verdict-v1.md | 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18 | 1-23 | acceptance of K7-M0 (item 4), arbitrary groups (item 6) |
| M1 | S/K7-M1-v1.md | 6e9b2d09aa5c55698dd96d95266243701ca077c98ec615aa57b648ebf3f95d63 | 1-21, 54-57, 76-79 | accepted: notation, setting, Theorem K7-M1, scope |
| M1E | S/K7-M1-erratum-v1.md | 4094b53783244e8b824dd64409d28380d0a635e76d74035e361f5ca22a26c510 | 1-66 | mandatory overlay (whole): F2 actual exponents; no statement change |
| VM1 | RUN/review/sun7-M1-parent-verdict-v1.md | 7121ceeedc1f1b0de8d9642c8f5c2aed052d9f2e83140afee33ffcd2f71ced84 | 1-13 | acceptance of K7-M1 |
| Z2 | S/K7-Z2-v1.md | cda7573de2401c220493d55e37fdc09b3292590522fc0258ba9a5ca6e27ecbe7 | 1-24, 104-110 | accepted: hypothesis H, Theorem K7-Z2, scope |
| Z2E | S/K7-Z2-erratum-v1.md | 3aa305553cd44946de32cea5cb2703b1864489a6a12de2154feda4884ee456f9 | 1-25, 85-89 | mandatory overlay: statements unchanged; G1/G2 imports |
| VZ2 | RUN/review/sun7-Z2-parent-verdict-v1.md | 0f6b9aa3e0552b0140bf581ac5a4d425b0732bcba639bdc49b61518d5fe5b19c | 1-16 | acceptance of K7-Z2 (5-marker at centre or elsewhere) |
| K35 | S/K7-35-v1.md | 5624d9783f5fb0236283a870109ce45c3655123949fd0e6dfcb0546ad517fc5a | 1-18, 84-88 | accepted: hypothesis H35, Theorem K7-35, scope |
| K35E1 | S/K7-35-erratum-v1.md | b13e1cf28dd55cd0983c5cc8259520e6723206d556dbcad27389ac6aaec66e32 | 1-21 | mandatory overlay (whole): proof repair, no statement change |
| K35E2 | S/K7-35-erratum-v2.md | 93f99707c5700ec2f7f1c9f9f088ce00866e02b073c8e38c052650dd1bd20d44 | 1-25 | mandatory overlay (whole): Theorem K7-35 unchanged |
| V35 | RUN/review/sun7-K63DE-K735-parent-verdict-v1.md | 1a1c639093dd334cb404a8216ca70a839ea85454978c9fdf354cc5bc577a3919 | 1-13, 19, 34-37 | acceptance of K7-35 (line 11), R0 (line 13) |
| U1 | S/continuations/k7-k62-residue/K7-U1-v1.md | d4e6cdc9e11320bee2456e589459c2b0e961bec466e1b7c05e7ff4003e751965 | 1-45, 156-158, 183-188 | accepted: hypothesis U1, Theorem K7-U1, scope |
| U1E | S/continuations/k7-k62-residue/K7-U1-erratum-v1.md | a795c5b7cafca0dbfdc4c250f92262b2f8f0179ee441cb89d02ae65be3b999d5 | 1-27, 101-104 | mandatory overlay: E-1 |M| = 1; theorem unchanged |
| VU1 | RUN/review/sun7-U1-parent-verdict-v1.md | 44dfbe8514b03a6d981c61abdfddc8722bda18d29ccac5c83bcc4787585c5c86 | 1-32 | acceptance of K7-U1 |
| ZP | S/continuations/k7-k62-residue/K7-Z23-P5-v1.md | 632550329619f441868f38c3435d4a42559e599e20c1c2db100945dff9ff8e04 | 1-53, 219-230 | accepted: exact index scope, Theorem Z23-P5, scope |
| ZPE | S/continuations/k7-k62-residue/K7-Z23-P5-erratum-v1.md | 737e82a331929432422f6a9dec535e7af8a5f697c86ae78870af7d7296ec823d | 1-10, 96-100 | mandatory overlay: statement unchanged |
| VZP | RUN/review/sun7-Z23P5-parent-verdict-v1.md | 7179e5645df3b840a1e4a9735e554ae7be4114d2e34f2b418face51e017c6f8d | 1-15 | acceptance of Z23-P5 |
| VR2 | RUN/review/sun7-K7-R2-parent-verdict-v1.md | 9b0f7df54165575c2cee4818896738e886ae77ff2fcd6c1a328d5946cd1b926d | 1-31 | acceptance of the (a1) closure (Corollary K7-REM only) |
| TR25 | RUN/control/mathematics-slot-transition-sun-20261019-1325-v1.json | 4b617b815ae3ae96adc769e86b84e7840fd79612967da605be5e113800092697 | 1-22 | definition of the (a2) setting (navigation only) |
The JSON manifest `K/review-excerpts-NF-v1.json` lists the 43 ranges as {path, sha256, start, end} in this order.

## 5. Block-to-statement check list
| block (K7-NF lines) | accepted statement (source lines) | literal hypothesis to verify |
|---|---|---|
| B1 (91-92) | K7-M0 (LFC 113-114; VLFC 21, 23) | all n_i = 6 w_i, w_i pairwise coprime, prime to 30 |
| B2-B4 (93-96) | K7-M1 (M1 56-57; M1E F2 19-22; VM1 5) | exactly one marked vertex, markers in {3,5}, e = 1; actual A, B >= 0, A + B > 0 |
| B5 (97-99) | K7-35 (K35 13-18; errata unchanged; V35 11, 13) | no e >= 2; f_t >= 2 with m_t = 3^A; p != t with m_p = 5^B; five unmarked |
| B6 (100-104) | K7-Z2 (Z2 20-24; Z2E 8; VZ2 5) | e_z >= 2 and no f >= 2; P unrestricted (h_z >= 0; separate p allowed) |
| B7 (105-106) | K7-U1 (U1 30-32, 158; U1E 14-16, 103-104; VU1 5-8) | exactly one marked vertex, any marker product |
| B8 (107-109) | Z23-P5 (ZP 10-20; ZPE 8-9; VZP 5) | n_z = 6*2^E*3^A*w_z, n_p = 6*5^B*w_p, others 6*w_u, E, A, B >= 1 |
| K7-REM (120-133) | (a1) closure (VR2 5, 9, 17) | (a1)/(a2) split of F: P empty/{z}/{t} versus a third vertex |
Also check: Lemma PART exhaustiveness/disjointness (lines 59-82); Lemma MK and SHAPE (lines 22-37); that every cited
statement is for arbitrary groups; that no theorem is applied outside its literal hypothesis (Remarks, lines 114-119).

## 6. Review contract
Independently verify the partition and each match above. Return FATAL/MAJOR/MINOR counts per group (SHAPE/MK/PART;
blocks B1-B8; K7-REM; provenance/boundaries) with exact file:line and minimal repair. An empty findings list is valid.
Accept imports only at the literal scopes quoted; verdict frontier sentences are not premises. The candidate must not be
read as a K7 or Sun(7) exclusion.

## 7. Packaging metadata
43 inclusive-range excerpts from 26 sources; selected raw UTF-8 bytes 85,005. Every whole-file sha256 and
every range was re-checked against the files immediately before this write. Byte/hash operations are packaging, not
science runs.
Manifest: `K/review-excerpts-NF-v1.json`, sha256 `7eba0a3487ba044894c3e84626473cd93da4b62b46d58354c12247773c6bfbd6` (10,186 B). Package plus selected source: 96,380 B (<= 100,000).
