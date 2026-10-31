# info-6 frontier: bounded search from a shared-cubic inverse

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-29T03:34:25-0700**. This records a bounded stochastic search on **actual balanced truth tables**. None is a target witness, no unrestricted exclusion is claimed, and all receipts are same-owner checks, not disjoint review or novelty evidence.

## Route and exact outcome

Start from the pinned formal shared-cubic NON-WITNESS. A bounded sign-swap exploration kept its labelled q/Q and cubic classes but did not reach a Boolean inverse. Rounding the signs of one such inverse and adjusting the least-absolute inverse coordinates to balance produced the pinned actual Boolean seed. Direct 512×512 character sums plus independent FWHT audit gave weight256, W(0)=0, peak52, NL230, 33 zeros: **not** the target.

Three bounded balance-preserving annealer runs from successive best actual truth tables had these observed outcomes:

| run | seed | iterations | accepted swaps | best peak | NL | tail objective | target |
|---|---:|---:|---:|---:|---:|---:|---|
| a | 20261029094 | 5,000,000 | 3,045 | 36 | 238 | 155 | false |
| b | 20261029095 | 20,000,000 | 13,792 | 36 | 238 | 148 | false |
| c | 20261029096 | 30,000,000 | 21,507 | 36 | 238 | 148 | false |

The independently audited a/b/c best truth tables are balanced and have peaks 36; their zero counts are respectively 17,20,20. All runs completed their stated iteration budgets without timeout. They do **not** improve the previously audited balanced peak32/NL240 near-target, do not prove any neighbourhood exhaustive, and do not show no peak28 witness exists. The intermediate sign-swap exploration was not instrumented as an exhaustive search and is not claimed as a complete or independently replayed result; the actual rounded seed is pinned so the three bounded runs can be replayed directly from it.

The annealer updates the Walsh spectrum incrementally under opposite truth-bit swaps and recomputes the entire transform before writing each candidate. The separate verifier recomputes every coefficient by direct character sums and FWHT and checks balance/Parseval/inverse. The pinned binary is the one used; its source and verifier are pinned, but the binary-source build provenance is not independently established here. No round-level conclusion follows from the failure of these bounded stochastic runs.

## Pins

| File in this directory | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-shared-cubic-rounded-candidate.json` | `978bb15b4273dcbcf862eb961ca007747f340597ca5d97948dfcdc414fe79cde` | 7 | actual balanced seed, non-target |
| `frontier-20261028-shared-cubic-rounded-audit.json` | `7131a99c0c7636be82636d9e7595d80892d9392dac1629673e2fd47ec93d0e12` | 592 | seed direct/FWHT audit |
| `frontier-20261028-rounded-search-a-result.json` | `e2f99a0fc00b52151acf057b16399039a0fae379441841b1193656b328b9d9d7` | 16 | bounded a receipt |
| `frontier-20261028-rounded-search-a-candidate.json` | `d11f6e57e709b5f290b8a05b6aebddf87fe231b8c81ab0c105469c272ad31815` | 8 | actual a non-target |
| `frontier-20261028-rounded-search-a-audit.json` | `416b9faa0c698980ee74f0ce35e0f9fbdc6c90ff55cd630cbe4ae9684ab61caf` | 572 | a direct/FWHT audit |
| `frontier-20261028-rounded-search-b-result.json` | `d48183e986a52af96b5c55a4fdbf231a3f5f6fdf2d7805b5ab980e9d12c7e4aa` | 16 | bounded b receipt |
| `frontier-20261028-rounded-search-b-candidate.json` | `ef9242fc5ef9abd2f5a75b38a02ac8d7cb157db5122eabe053f40ed6d76abcf3` | 8 | actual b non-target |
| `frontier-20261028-rounded-search-b-audit.json` | `d036cdaa4a5da16f10c6143b5cb26a1c03b1d276bbc43a78f9830e9a2394e164` | 575 | b direct/FWHT audit |
| `frontier-20261028-rounded-search-c-result.json` | `5ab67eea95d81fff55ae737a3d8dfb41e1c2b20a9a9ce80f368be7964a20f843` | 16 | bounded c receipt |
| `frontier-20261028-rounded-search-c-candidate.json` | `612d2cc47be367ef9b202d591f1eb898678c57bf37c3e56a998916a4ccabd1b0` | 8 | actual c non-target |
| `frontier-20261028-rounded-search-c-audit.json` | `583021af761d60dc6d855a1bb9c8e72a5a42b0087375a6b9dc87070f2da51a9e` | 575 | c direct/FWHT audit |
| `frontier-20261028-balanced-anneal.cpp` | `f5d330bdd642bb1c4e3c80bf350a1421b511756e2409fa436c3bd3bb0d97f8f8` | 183 | search source |
| `frontier-20261028-balanced-anneal` | `9a910f8491c80637fe08e0093b3d8d52347ce2a20f333181c7c1934204dc30c3` | binary | used search executable |
| `frontier-20261028-verify.py` | `3eab1464d222b017034ee709fb163fe216047533f4f164342bdd1126e8c4a8ca` | 114 | separate verifier |
| `frontier-20261028-rank2-shared-cubic-barrier-v1.md` | `7af42130c732d96f3ac63ee65e2d18f574c74462efafaf34887673c313ebab7c` | 39 | originating formal NON-WITNESS |

**END.**
