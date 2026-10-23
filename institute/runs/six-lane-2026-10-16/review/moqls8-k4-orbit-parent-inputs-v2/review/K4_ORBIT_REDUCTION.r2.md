# K4 split: orbit reduction by verified CNF automorphisms — note and ledger contract, r2
# (supersedes r1 89e8c52e…7286, which is unchanged; model-authored; NOT IN FORCE until the parent's GO(b))

Fixes: Claude orbit review v1 M1 (bind the verified permutations to what the ledger applies), M2 (path literal
sets), m1 (independent second-path check), m2 (DRAT transport qualified, non-load-bearing), m3 (hash = parsed bytes,
parse identities), m4 (combined acyclicity, R ≠ L, exact partitions, one record, pinned alphabet), m5 (strict JSON
booleans, pinned hashes), m6/m9 (planning-only/commentary labels), m7 (lane-map cross-check not cited as a binding),
m8 + Codex minor 2 (the false "only V1–V3" remark is withdrawn), m10 (checker hygiene), m11 (stronger controls);
Codex minor 1 (DRAT conventions).

## 0. Pinned objects (lane-relative paths)
- F4 = evidence/k4_w1_v1/GA3_K4w1.cnf, SHA-256 7bb806fc8f7793fa5088cc78caf3ebf5b49a72cad82c527f47cf6faced4301f7.
- Permutation arrays (little-endian int32, entries 0..V with entry 0 = 0, V = 513184):
  π_g1 = evidence/k4_split_v1/auto_r3/PERM_g1.i32le, SHA-256 8b09da43870aad811bf45d581a91f813fd0b816ee4859ec38cdb2da2fc115b2a;
  π_g2 = evidence/k4_split_v1/auto_r3/PERM_g2.i32le, SHA-256 e0a2bc4c26eaa613389c3d43f68d5bc9771e619cfc0b9b2b2eb213dffc7dcfd3.
- Path A (NumPy): code/k4_automorphism_r3.py SHA-256 a03e9d500744c53cb68997e432e99ba296a4409a660138f34b3172b7eedb9866,
  receipt evidence/k4_split_v1/auto_r3/RECEIPT.json SHA-256 c7154dc32d60e6cb3ab5d409432df1107bd8b1bae0d5b79fc4545af4b07e3ff8
  (17:23:49–17:24:12 PDT, 22.3 s, max RSS 1.34 GiB).
- Path B (pure Python, own DIMACS reader, stdlib `array` loader, no NumPy, no name table):
  code/k4_auto_secondpath.py SHA-256 ad0ee835b1de13da13251906f94ef19ad5dc06e724c8b222eb64678649a02d45, receipt
  evidence/k4_split_v1/auto_r3/SECONDPATH_RECEIPT.json SHA-256 2990e2167116dfdab98f18a15592ec5cab91d19118be17ee8f849aa1400a1275
  (17:24:21–17:25:35 PDT, 73.5 s, max RSS 1.25 GiB).
- Name table (construction only): parent review/moqls8-encoder-binding-v1/K4.names.json.gz, SHA-256
  ed0462bc4de7fdcbc34397e1b05304160e47b9ba4a1bd1c858c5f997df3f8e2d.
- Validator: code/k4_orbit_r2.py (pins all of the above); in-memory controls code/k4_orbit_controls.py →
  evidence/k4_split_v1/auto_r3/ORBIT_VALIDATOR_CONTROLS.json (14/14 PASS). The r1 draft code/k4_orbit.py was never run.

## 1. Transfer lemma (load-bearing) and DRAT remark (NOT load-bearing)
Let F be a CNF on 1..V and π a permutation of {1..V}, π(−v) := −π(v). If π(F) = F as multisets of clauses (a clause
taken as the multiset of its literals), then for every literal set c: F ∧ c SAT ⇔ F ∧ π(c) SAT. Proof: given α ⊨ F ∧ c,
β(π(v)) := α(v) is total (π onto) and satisfies every clause D = π(C) of F and every unit π(l); conversely use π⁻¹.
Remark (not used): a binary-DRAT refutation P of F ∧ c becomes one of F ∧ π(c) if renamed IN PLACE (line order and
literal positions kept, so the RAT pivot stays first; deletion lines renamed literally; π extended by the identity on
proof variables > V; re-encoded as binary DRAT). This does not apply to LRAT/FRAT/LPR as is. Certification below uses
only the lemma, never a transformed proof.

## 2. What is established about the PINNED arrays
Both paths load the arrays from the pinned files and check, on the actual F4 bytes (whose SHA-256 is computed on the
very bytes parsed): entries in [1,V], bijection of 1..V; EXACT clause-multiset equality π(F4) = F4 (A: per length,
sorted int32 rows, lexicographically sorted matrices compared element-wise; B: sorted list of packed sorted clauses,
list equality); g1² = g2² = id, g1g2 ≠ id, (g1g2)³ = id, closure order 6, all six elements automorphisms; every
element maps V1 root assignments to V1 root assignments and V2 assignments to V2 assignments (B; A for the
stabilisers). Parse identities (A): last token 0; Σ lengths + #terminators = #tokens; #terminators = header clauses;
max |literal| = header variables; warnings are errors. Controls: A — identity PASS; σ = (4 5), ρ = id FAIL;
π_g1 with images of 57/64 swapped FAIL; polarity flip FAIL; non-injective FAIL. B — identity PASS; swap FAIL;
polarity flip FAIL. Soundness rests only on: the pinned F4 bytes, the pinned arrays, these two exact checks, the lemma,
and the ledger's set and graph checks (§3). How the arrays were constructed (σ = (5 6) / (6 7) on rows, columns and
coordinates with ρ = (Q2 Q3) / (Q3 Q4), via the name table) is commentary, as is any explanation of WHY they are
automorphisms. Orbit tables (64 root orbits; stabiliser orders 6/2 with 64/96 child orbits) are PLANNING ONLY: a wrong
table can only leave leaves UNKNOWN, it cannot certify one.

## 3. Ledger contract r2 (implemented by code/k4_orbit_r2.py)
Definition: lits(X) := all cube literals on the path root → X, i.e. exactly the unit clauses appended to F4 in X's
leaf CNF; it is DERIVED from the tree (root: canonical V1 assignment of its index; child: lits(parent) followed by the
canonical V_d assignment of its index), never read from a stored field.
A leaf L may be CERTIFIED with the single evidence record {kind: "orbit", source: R, word: [h1,…,hm] over {"g1","g2"},
automorphism_receipt: {path, sha256 = c7154dc3…3ff8}} iff:
 (a) the receipts and arrays match all pins (§0), receipt hashes (script, names, CNF = ledger base, arrays) match, and
     every verdict field is JSON true (checked by identity); "g1"/"g2" denote exactly the pinned arrays;
 (b) π_w := π_{h1} ∘ … ∘ π_{hm} composed from the pinned arrays only; every literal has 1 ≤ |l| ≤ V;
     π_w(lits(R)) = lits(L) as literal sets; for a strict source the receipt's literal list equals lits(R) and its
     leaf-CNF hash is the base + those units (inherited strict-receipt identity check);
 (c) R ≠ L; R is SETTLED: strict CERTIFIED, or REFINED with all of its exactly 128 children settled (exact 128-way
     partition by the declared list is enforced by the unchanged base validator), or orbit-CERTIFIED from a settled
     source; the combined dependency graph (refined node → children, orbit leaf → source) is acyclic;
 (d) L is terminal (no children) and carries exactly one evidence record.
Consequence (not an extra rule): every group element preserves the V1 and V2 variable sets (§2) and |π(S)| = |S|, so
for full path cubes of equal depth the equality in (b) forces π_w to map the source's root cube onto the leaf's root
cube and the source's V2 assignment onto the leaf's V2 assignment; for two children of the same parent P this means
π_w ∈ Stab(P). (Codex: g1 sends root c032 with child index 32 to root c016 with child index 16 — indices are never
copied between roots.)
Use: depth 1 — strict runs for every root except the ten non-representatives c032, c064, c033, c065, c080, c096,
c081, c097, c044, c076, each certified by orbit from its settled representative (c016, c017, c048, c049, c028);
depth 2 — for a refined representative P, one child per orbit of Stab(P) is run strictly and the others are
certified by orbit from a sibling. Completeness unchanged: complete ⇔ every terminal leaf CERTIFIED (strict or orbit)
with no validation problem. The withdrawn r1 remark ("only V1–V3") is not a rule; deeper orbit certificates are
possible whenever (b) holds (e.g. g2 maps the depth-4 assignment indices (0,0,0,32) to (0,0,0,64)).

## 4. Validator controls (in memory, code/k4_orbit_controls.py; 14/14 PASS)
Positive: v001 + strict pilot receipts; c021 ← c037 via g1; c069 ← c037 via g2; chained c069 ← c021 via (g2, g1);
regression after restoring pins. Mutations rejected: wrong word; source = leaf; unsettled source (UNKNOWN c016);
two-node cycle; unknown generator; orbit leaf with a child; tampered array pin; extra evidence field; foreign receipt.

## 5. Parent replay
(1) Re-run path B (or any independent exact check) on the pinned arrays; (2) re-solve each representative's strict
leaves; (3) run code/k4_orbit_r2.py validate on the ledger. Orbit certificates add to the trusted base: the two exact
checks above, the lemma and the validator's set/graph rules.
