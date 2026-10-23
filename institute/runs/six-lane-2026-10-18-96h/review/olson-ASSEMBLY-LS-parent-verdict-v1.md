# Ordered Olson over D_(2p): ASSEMBLY-LS for all o_F <= p-1

Recorded at 2026-10-19T11:07:50-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL**, written mathematics relative to the exact parent-accepted interfaces below and, for p >= 11, Lev 2022 Theorem 2 as a statement-level external premise (proof not replayed). No computation is a premise for p >= 7. This is not unrestricted INV*(p), ordered Olson for all D_(2p), or the all-groups target.

## Exact accepted statements

Let p >= 7 be prime. o_F counts the odd blocks of the maximal cyclic constant reflection-block decomposition.

1. **Proposition ROT-LS.** If SOME admissible normal form of a length-(4p-2) avoider over D_(2p) has terminal 1 <= k <= p-1, then all rotation letters lie in one set {rho_c, rho_-c}, c != 0. There is no o_F hypothesis. For p >= 11, Lev enters exactly when the invoked normal form has floor(2p/3)+1 <= kappa-hat <= p-3; p=7 is Lev-free.
2. **Theorem ASSEMBLY-LS (A).** Every length-(4p-2) avoider over D_(2p) with o_F <= p-1 satisfies INV*: rotations lie in one nonzero pair and every maximal cyclic reflection run is constant.
3. **Theorem ASSEMBLY-LS (B).** Every length-(4p-1) word over D_(2p) with o_F <= p-1 has an identity 2p-subword in increasing original index order.

Statements 2-3 are conditional on Lev exactly as statement 1 for p >= 11. p=5 is not an LS consequence; only the separate citation union with the computer-assisted p5-lift verdict gives the corresponding p=5 statement, in its own trust class.

## Text of record and mandatory overlays

| Item | SHA256 |
|---|---|
| [Frozen scope](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/assembly-ls/ASSEMBLY-LS-scope-v1.md) | `53be77405c8b1369dfbde986a090350829a00cf2a83c3749fb7e87ff09c172a1` |
| [Proof v2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/assembly-ls/proof-ASSEMBLY-LS-v2.md) | `ac854c31ae1446c4710f3c19bb1beb80d8c25333aeb6b350c7f7d4dc7fafcfb3` |
| [Review package](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/assembly-ls/review-package-ASSEMBLY-LS-v1.md) | `fd710d3ec509a65a2b6f18d689d3744c8dde8f7009f5a09a0987812e08296295` |
| [Excerpt manifest](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/assembly-ls/review-excerpts-ASSEMBLY-LS-v1.json) | `b5158d37abc8c59dedd452c3bc93a63d631b7d18ef213959d58946242198c09d` |
| [Parent erratum v1](olson-ASSEMBLY-LS-parent-erratum-v1.md), residual E1-E2 | `572308b87c62237f77dab554afb29152b568b11c027dc8825c5923895b93f8f7` |
| [Parent erratum v2](olson-ASSEMBLY-LS-parent-erratum-v2.md), N1 trust labels and O4/O5/O6/O8 wording | `38458a8521f692e07b695a1c4553bb41bfaf6be9f93481b5d16f9c3e92d7c588` |

Read the proof, then erratum v1, then erratum v2. These change no main statement, case split or inequality. Optional O1 (cite fewodd addendum12 for the DAV empty-run instance), O2 (cite RUNS L49 or rely on the inline conjugation proof), O3 (termination measure is the author's elementary addition) and O7 (transitive trust inventory) are recorded here as citation notes only.

## Reviews

- [Codex](olson-ASSEMBLY-LS-codex-v1.prompt.stdout.txt) `1c16c90f23db55c0ce6e0159b6ebdb7666178b2d6dc04f5443f138ae73331df9`: gpt-6.1-sol/max/read-only. (A), (B), ROT-LS **ACCEPT**, 0 FATAL/0 MAJOR/2 MINOR residual wording; both fixed by erratum v1.
- [Claude](olson-ASSEMBLY-LS-claude-v2.prompt.note.md) `a95e9c6a7aa7b172a5cde4cd7fb975f0873e0ad88895365441e78c9460bf5b89`: claude-opus-5-5/max/no tools, corrected snapshot with erratum v1. (A) and (B) **ACCEPT**; ROT-LS **ACCEPT-WITH-FIXES**, 0 FATAL/0 MAJOR/1 required MINOR (Lev trust label), fixed by erratum v2. No interface is used outside its original domain and no proof gap was found.

## Parent independent checks

- Every admissible normal form has 1 <= k <= o_F; empty runs are allowed in NF, GRX, K1 and DAV. A single even terminal block is impossible by K1's odd F.
- GRX all-plus gives kappa-hat >= 0 and (ZP_kappa-hat). DAV gives R+H-hat = 3p-1+kappa-hat-k <= 3p-2, so kappa-hat <= k-1 <= p-2.
- R-(p+2kappa-hat+1)=p-1-k, so LS-ALL applies exactly for k<=p-1. Lev cells are floor(2p/3)+1<=kappa-hat<=p-3, nonempty only for p>=11; kappa-hat=p-2 is the Lev-free e=2 G-LS cell.
- Routing is exhaustive: k=1 to K1; kappa-hat=0 to accepted ROT-K01; kappa-hat>=1 to accepted ROT-FB(a), which has no 3k<=2p+1, F or o_F(w) hypothesis.
- Restricted REFL is applied to the original w with o_F<=p. The deletion ledger with B=p-1 preserves the class: Case1 has F-o_F>=3p-2>=2p; Case2 lowers o_F by one; Case3 does not raise it, and a common nonzero third rotation fixes the pair.

## Scope and open boundary

Previously accepted uniform dihedral coverage was 3o_F<=2p+1 and, separately, o_F<=p-1 with F-o_F>=2(p-1-floor(2p/3)). This verdict removes that F condition throughout o_F<=p-1 (Lev-conditional for p>=11). o_F=p remains open where every normal form has k=p, kappa(w)>=floor(2p/3)+1 and (S1) fails; o_F>=p+1 also needs reflection rigidity beyond o_F<=p and large-terminal rotation input. Candidate ONE-SHORT-LS and ROT-SING are separate pending results, not inputs here. No novelty, Lean or human-review claim.
