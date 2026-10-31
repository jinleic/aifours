# State of originalQ1 after the 2026-10-29 reductions (navigation record, not a new theorem)

**Status: SUMMARY of same-author UNREVIEWED / UNADOPTED candidates; no new mathematics here beyond pointers.** Q1 asks whether every weakly E-unitary locally r-orthodox (regular) semigroup embeds in a seminormal-band-by-completely-simple semidirect product. It remains OPEN.

## 1. Logical chain now on file

| Step | Statement | File (SHA-256) |
|---|---|---|
| A | SN bands are exactly subdirect products of LEFTSN and RIGHTSN bands; least one-sided congruences lie in R and L | `frontier-20261029-SN-kimura-decomposition-v1.md` (`06abe46d…b5b6`) |
| B | Every original source S embeds subdirectly in S/λ_S (left-regular-local) × S/ρ_S (right-regular-local); hence Q1 ⇔ Q1 for right-regular-local (RRL) sources | `frontier-20261029-source-onesided-reduction-v1.md` (`40668a70…a63`) |
| C | With printed Fact1 imported: Q1 ⇔ matching RIGHTSN-host form for RRL sources ⇔ separation of same-fibre R-related idempotents by the canonical RIGHTSN host ("item4") | `frontier-20261029-matching-onesided-equals-Q1-v1.md` (`64ad0ee9…619a`) |
| D | In RRL sources every label-consistent RIGHTSN instance holds (no single-instance obstruction); 748-element RIGHTSN band Q4 gives exact canonical certificates | `frontier-20261029-rightSN-instance-lemma-and-canonical-certificates-v1.md` (`d50d288d…2ec`) |
| E | Sufficient SN-instance no-host certificate (any actor); bounded searches found none | `frontier-20261029-SN-instance-no-host-certificate-v1.md` (`2f4fecc8…d8a8d`) |

Supporting tools: exact idempotent-fibre representation (`frontier-20261029-exact-idempotent-fibre-class-v1.md`, `aabc39e5…6960`); nested-host flattening (`frontier-20261029-iterated-Pastijn-flattening-v1.md`, `5d7d0fb8…438c`).

## 2. Exactly what remains for Q1

Item4: for every RRL original source, distinct R-related idempotents in one actor fibre are separated by the canonical RIGHTSN host. Equivalently, the derived category of the actor map admits a faithful-on-parallel-arrows representation in a RIGHTSN band. The single-instance lemma (D) handles label-consistent rewrites; derivations through label-INCONSISTENT words are not controlled. Fact1 itself (Billhardt–Szendrei 2003) is imported; its proof and convention interface were not reconstructed (the open-archive article page presented a CAPTCHA and was not bypassed).

## 3. Evidence collected (finite, exploratory)

- Exact canonical RIGHTSN computations through Q4: 60/60 (checker) and 473/473 (kernel) random two-generated RRL sources faithful; non-RRL sources collapse, as they must for a one-sided band.
- Z3 RIGHTSN hosts, exactly rechecked: 8/8 (seed1) and 400/400 (seed2; sizes 12–40, up to16 local R-pairs; band sizes 3–9) RRL sources inside `P(B5^1,D8)`. Results file `frontier-20261029-RRL-rightSN-host-batch-seed2-results-v1.jsonl`, SHA `8bf4d4f779c00f1e6392b8465e7e5a677661330fb15e05fd1c6b1ce786f91a84`, 401 lines.
- S45 (no globally regular host) and S68 are RRL and have RIGHTSN hosts (B5² and B8).
- No SN-instance certificate found among ≈2×10⁵ generated seeded/random sources (v1–v4 searches); RIGHTSN-instance certificates cannot occur in RRL sources by lemma D.

These support, but do not establish, a positive answer. All source classes searched are subsemigroups of small physical hosts over the non-SN band B5¹ and C₂-actors; bias toward such families is acknowledged.
