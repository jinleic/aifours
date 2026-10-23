# Addendum 1 to 01-proof-to-code-map-v1.md and 05-input-resource-plan-v1.json

- Written: 2026-10-19T17:39:42-0700 (host /bin/date). Originals unchanged (mode x); this addendum only clarifies scope and corrects one count.

1. **Row C scope (minimality).** Row C is the statement "no Core(5) configuration in a minimal-order counterexample G (proof-v4 §3) has a labelled pattern in 𝓛 ∖ orbit(S-D)". T, K, PB and N2 need no minimality. FH2 uses rules-v1 L6 (F2), which at s = 5 applies Sun(5) to the proper subgroup H = W and therefore needs minimality of G; s = 2 uses L0.6 and s = 3, 4 use the imported Zhu Theorem 1.1. This is exactly the setting in which proof-v4 §7 uses the certificates. The checker's FH2 rejection test is unchanged; only the wording of row C is made explicit.
2. **Run count.** `05-input-resource-plan-v1.json` field `estimates.total_runs` says 46; the exact list is 45 runs (P0, I01–I07 including I06 and the optional I07, and the 37 fixtures P1–P3, N01–N15, S01–S19). The output upper bound 1.1e8 bytes is unaffected.
3. **PYTHONHASHSEED.** Outputs do not depend on it (only integer sets are iterated; records.tsv is in input-line order); setting it is harmless and not required.
