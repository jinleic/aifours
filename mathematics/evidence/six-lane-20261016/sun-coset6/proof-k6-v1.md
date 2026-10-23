# proof-k6-v1: candidate proof structure for Sun's disjoint-coset conjecture at k = 6 (CONDITIONAL)

- **Freeze record:** host-clock time and sha256 are in `evidence/proof-k6-v1.sha256`.
- **Status:** a candidate, written in this lane. It is computer-assisted and not Lean-checked. No k = 6 theorem is claimed and no gate is claimed. Novelty is not claimed: the parent's pre-check found no k = 6 claim, but a search miss is not novelty.
- **What the conclusion is conditional on:**
  - (i) an independent replay, by a separate author, of the certificates in `evidence/engine-v3-core56/`, following `CERT-FORMAT-k6-v1.md`;
  - (ii) hostile reviews of rules-k6-v2/v3 and of `proof-k6-lemmas-v1.md`;
  - (iii) the accepted Core(5) record `R/sun-coset5-parent-verdict-v1.md`.

## Target

Sun(6): if a_1G_1, …, a_6G_6 are pairwise disjoint left cosets of finite-index subgroups of a group G, then gcd([G:G_i], [G:G_j]) ≥ 6 for some i < j.

## Step 1. Reductions

- **R0.** G may be taken finite. See README §2.
- **R1(6).** Sun(6) is equivalent to Core5(6), given:
  - Zhu Theorem 1.1;
  - Prop 4.5, as proved in sun-coset5 proof-v4 §2;
  - the accepted Core(5).

  The written proof is in README §2, with the wording fixes of `rules-k6-erratum-v1.md` E1.
- **Core5(6).** No finite group has six pairwise disjoint cosets g_iU_i with [G:U_i] = 5r_i and the r_i pairwise coprime.

## Step 2. Minimal-counterexample frame

Suppose Sun(6) fails. Take G of minimal order among finite groups that contain six disjoint cosets whose pairwise index-gcds are all ≤ 5. Then:

- R1(6) holds group by group, so G carries a Core5(6) configuration.
- Every proper subgroup of G satisfies Sun(6).
- Every group satisfies Sun(k) for k ≤ 4 (Zhu Theorem 1.1, plus L0.6).
- Every group satisfies Sun(5) (accepted Core(5)).

Sun(6) is used only inside proper subgroups H < G: in the FH5 fibres, and only when six vertices meet one H-coset (`rules-k6-erratum-v1.md` E4).

## Step 3. Patterns and complete enumeration

For the configuration, put α_ij = [G:U_i∩U_j]/(5r_ir_j). Each α_ij lies in {1, 2, 3, 4} (L0.3). The markers are E2 with its class, E3, and E5. Every configuration gives a pattern.

**Types.** Up to S6, every pattern is a labelling of one of the 8 types listed in CERT-FORMAT §1. That section also proves the 8 types are complete.

**Killed by T.** Labellings with a T-forbidden triangle are impossible by rules-k6-v1 L1.

**The orbits that remain.** Every other labelling is a T-consistent leaf. Its stabiliser orbit is one of the 61,124 orbits listed in `orbits.jsonl.gz`. The engine enumerated:
- every labelling of each type, by backtracking, pruning only on completed T-forbidden triangles;
- 1,575,031 T-consistent labelled leaves in total, with per-type counts and leaf-code hashes in `run.json`.

## Step 4. One certificate per orbit

Every orbit line carries a certificate. There are no SURVIVE lines.

| rule | orbits | lemma | written proof |
|---|---|---|---|
| K | 55,159 | rules-k6-v1 L3 (generic M-S Lemma 3.5) | sun-coset5 rules-v1 L3, with erratum-v3 |
| RLP | 5,513 | rules-k6-v1 L7 with v2 L9, exact duals y(q) for every admissible q | proof-k6-lemmas-v1 §1; sun-coset5 proof-v4 §5 for R1–R3 and R5′ |
| FH5 | 134 | rules-k6-v1 L5 and L6 (H5), with v2 L9, all 7 E5 placements | rules-k6-v1 L6; proof-k6-lemmas-v1 §1(a); erratum E4 and E6 |
| N26 | 108 | rules-k6-v3 L11, using L10 (XE) | proof-k6-lemmas-v1 §2 and §3 |
| PB | 55 | rules-k6-v1 L4 | sun-coset5 rules-v1 L4 |
| RPLP | 155 | rules-k6-v3 L12, an exact dual or Farkas vector for every admissible q | proof-k6-lemmas-v1 §4 |

**Why each certificate is valid for every instance:**
- **Every admissible τ:** rules-k6-v1 L8 (M1). Every rule is upward-closed in τ, and links pin τ.
- **Every r with the given markers:** M2, using the saturation argument of erratum E5. maxgcd saturates at the partner's q-part or t-part.
- **E5:** only FH5 can see it, and FH5 refutes all 7 placements.

## Step 5. Closure (conditional)

Suppose the certificate set passes an independent replay under CERT-FORMAT-k6-v1. Then no orbit of any type admits a configuration. Combined with Steps 2 and 3, this means no Core5(6) configuration exists in a minimal counterexample. Hence Sun(6) holds for every group.

This conclusion is conditional on (i)–(iii) in the status block above. It is **not** claimed now.

## Dependencies and boundary

**Imported:**
- Zhu Theorem 1.1;
- the accepted Core(5) record;
- Prop 4.5 as proved in sun-coset5 proof-v4;
- elementary group facts.

The Gong thesis is not used.

**Written in this lane (unreviewed):**
- rules-k6-v2 L9;
- rules-k6-v3 L10–L12;
- proof-k6-lemmas-v1.

**Reviewed with fixes:** rules-k6-v1 was reviewed by Codex and Claude. They found no FATAL and no MAJOR mathematical issues. Their fixes are recorded in `rules-k6-erratum-v1.md`.

**Finite evidence:**
- `engine-v3-core56`: lane-produced certificates.
- `checkB-v1-run1`: a lane self-report by the same author. It applies the v2 rules only and is not independent.

**Not done:**
- the independent certificate replay, which the parent will commission from a separate author;
- Lean;
- a post-result priority audit.
