# Olson RUNS / INV_Res / restricted long-word theorem: parent verdict

Parent decision at 2026-10-18T02:37:32-07:00: **CORRECTNESS-ACCEPTED as written partial theorems, not a breakthrough gate and not full ordered Olson.** Accepted assembly: [v4](olson-runs-assembly-proof-v4.md), SHA `06579ba5d23f194cf4cf61241fbbc6eebdaa6fb991d004f1642f43277bb3b104`, read with all corrections below. The frozen proof files are unchanged. No finite census is a proof premise.

## Exact strongest statement

For every prime p>=5, every word of length 4p-1 in D_(2p) whose rotation letters lie in one set {rho_x,rho_-x}, x nonzero, and whose **maximal cyclic reflection runs are each constant**, contains 2p letters in increasing original index order with ordered product identity. Different reflection runs may have different values. This is RGR-LONG(p), not the statement for arbitrary words.

The accepted intermediate statements are precisely v4 §1.5 and Theorems A–C / Corollaries B', D, E:
- NMH(p), including both R>=2p-2 and the previously accepted R<=2p-3 branch.
- MIX_DEF_HIGH(p), MIX_DEF(p), and solvability for every RGR word of length4p-2 with F,R>=1, normalized A>=B and 1<=B<kappa, with arbitrary reflection parities.
- RUNS(p): every **inherited** avoider in RGR_(4p-2)(p), F,R>=1, has k<=p.
- Such inherited avoiders normalize to B=kappa=0; combining RUNS with the previously accepted PAR gives INV_Res(p): all 2k runs are odd and k<=p.
- DR-Res then gives RGR-LONG(p).

“Inherited” retains all five conditions in v4 §1.3: R<=3p-2; F+sum floor(r_i/2)<=3p-2; R+H<=3p-2; H<=p-1; and a_i,b_i<=p-1. The proof shows some are automatic, but this verdict does not erase them from the theorem statement.

**Not established:** INV*(p), either inverse-normalization half; full ordered Olson for D_(2p); arbitrary finite groups; p=3; non-inherited INV(p) or MIX_RUNS(p); formal verification; novelty or priority. A full dihedral conclusion still needs to force an arbitrary avoider into the RGR class.

## Review basis and accepted dependencies

1. [Codex assembly review](olson-runs-assembly-codex-v1.note.md), `4f2317413031a7f127dd9e2d56f839baaa08783115b00e28505e6f78153577aa`: ACCEPT-WITH-FIXES, 0 FATAL/MAJOR, 2 MINOR. New imports checked at stated scopes; its upstream-foundation gap is explicit.
2. [Claude assembly review](olson-runs-assembly-claude-v1.note.md), `aadb6d554f7a3e5ab36706406c3fadae9e2cb5e07988d93f5c5aaad74f5d1eab`: ACCEPT-WITH-FIXES, 0 FATAL/MAJOR, 7 MINOR. All U2–U10 paths checked except the then-unfinished H/HW and upstream filter foundations.
3. [Targeted foundation review](olson-foundations-claude-v1.note.md), `a063bc6b6cbc9ea580857618165cc0fbe2e1a14cb160142095b4f5edf9e3a6f5`: ACCEPT-WITH-FIXES, 0 FATAL/MAJOR, 6 MINOR. Full GR→WAS→HW/H equivalence, EGZ applications, gap Theorem P, Doubling, Davenport-alpha and DR-Res/DR/DR' are checked. Earlier Codex reviews supply the other family; [foundation desk result](olson-foundations-final-v1/RESULT.md) maps exact coverage and receipts.
4. [v2→v4 delta check](olson-foundations-final-v1/delta-v2-v4-check-v1.md), `213277234db3182180aee2222d9e41dd5571bf0f666917360568c166690a8a5d`: 26 change blocks, three substantive justification/consequence changes explicitly re-derived. Parent checked the affected branches below; no applied theorem hypothesis changed.

This verdict accepts U2–U10 at their exact cited scopes in v4 §6, including the corrected foundation interfaces. U1 (GC), Theorems M/P and their SEED-G/A0/C0W inputs retain their prior parent acceptances and errata ([GC](olson-gc-parent-verdict.md), [M/P](olson-par-mixlow-parent-verdict.md), [uniform chain](olson-c6-uniform-parent-verdict.md)). These are reviewed written proofs, not axioms added to a formal prover. Classical EGZ at n=p and D(Z_p × Z_(2p))=3p-1 remain explicit literature imports, not new theorems here.

## Independent parent checks

- [Input pins](olson-runs-parent-input-pins-v1.json), `a3863675ed8c792e7a38fe2242091404209cb0e1e49164006f99f29dc473f459`: all31 assembly-table paths re-hashed, 31/31 exact; assembly v4 hash matches. The parent read v4 §§0–7, the original HW/H formulas, the K0 proof, FWH proof, DR-Res, both assembly-review findings, foundation-review corrections, and the delta map. This is **not** a claim that the parent independently re-proved every page of U2–U10; the complete lower-level review is the two-family coverage above.
- [Arithmetic smoke](olson-runs-parent-arithmetic-smoke-v1.json), `dfc2ae4793740b7ce518320193bf78896c23f0af1fc9ac62b6251b772e407af0`: independent integer selection enumeration versus HW gives103,806/103,806 equal windows at p=5,7,11; 7,650 FWH parameter checks pass. No lane code imported or native child launched. The code ran in the parent eval transcript, not a pre-pinned script. These finite checks are aids only, not an all-prime certificate.

### Parent derivation of the assembly and critical interfaces

**HW/H.** Fix a sign pattern P with2m reflection-boundary changes and residual pair capacity h. Select C reflections from the even interval[2m,2m+2h], then n=2p-C rotations. With E+ and E- available positive/negative contributions, x=(a_+-a_-)/2=a_+-n/2 is realizable exactly when the four integer bounds on a_+ and C intersect. Eliminating C gives

    -min(p-m, E-+m+h-p, floor(E-/2)) <= x
      <= min(p-m, E++m+h-p, floor(E+/2)).

Parity is already even in C and n; no extra parity obstruction is lost. GR supplies the signed reflection sum, and division by2 is legitimate modulo odd p. For P empty/full, endpoints can reach±p only when A or B>=2p. On an avoider A,B<=2p-1, so zero avoidance is exactly min(A,B)<=kappa. This verifies the scope of the old correction; it does not remove that scope.

**Fact Z.** Normalize A>=B. If both A,B>=kappa+1, zero lies in the empty-pattern interval, contradicting avoidance; hence0<=B<=kappa. Since R=2p-o_F+2kappa=A+B<=2p-1+B, obtain o_F>=2kappa-B+1>=kappa+1. For B<kappa this improves to o_F>=kappa+2. In particular OR can be used, and its reduced all-odd word satisfies the low-branch kappa bound automatically.

**NMH and MIX_DEF_HIGH.** The integer R split is exact: R>=2p-2 uses FW+ (with FWH and BR/R2); R<=2p-3 uses GC with the **entire** NMH setting. OR preserves R,F,A,B,H,kappa and avoidance; M0 lowers(A,B,R,kappa) by(1,1,2,1), raises H by1, preserves kappa-B and A-B, and stops with pure/(1,1) rotation runs. If the reduced B is positive, all NMH hypotheses hold. If it is zero, R=A<=2p-1, so C0-B' or A1 applies; the purported R>=2p exit is vacuous. No inherited condition is transported through M0.

**RUNS coverage.** Under0<=B<=kappa there are only B=0<kappa, B=kappa=0, B=kappa>=1, and0<B<kappa; splitting the last two by integer o_F<=p / >=p+1 yields exactly the six branches. C1 uses OR and the all-positive lemmas. C3 is KB on the original word and retains D0 there; C4 is KBH; C5 uses OR and accepted MIX_low with kappa<=o_F-2; C6 is MIX_DEF_HIGH. C2 assumes k>=p+1 and B=kappa=0: R=2p-o_F>=k implies1<=o_F<=p-1 and R>=p+1>=6. Thus there is an even reflection run, and K0's two uses of k<=p are replaced by R>=5 and o_F<=p. Its parity step needs only e_R≡e_F mod2, automatic here. K0's old use of(P) to infer an even reflection run is unnecessary. D0 in C3 is the only inherited condition not automatic for avoiders.

**DR-Res.** For a length4p-1 RGR avoider, the classical EGZ/gap/Doubling/Davenport arguments establish all inherited conditions. Deleting only within a run of length>=2 changes no run count and cannot create a zero-product subword; each such deletion is inherited and length4p-2. RUNS gives k<=p, then PAR makes every run in each deletion odd. Two different long runs would force opposite parities for an unchanged run across the two deletions, impossible. Thus just one run is long, of length4p-2k>=2p. A reflection run supplies2p identical reflections; a rotation run contains p equal rotations and the reviewed Doubling lemma applies. Both contradict avoidance. Cyclic rotations change products by conjugation, so identity selections return to increasing original index order.

## Errata adopted without rewriting frozen files

The seven Claude/two Codex assembly findings are already repaired in v4; the foundation findings and delta nits are adopted here:
1. **m1 EGZ:** select p zero-sum rotations from R>=3p-1 using EGZ(n=p), then another p from the remaining>=2p-1. Their union has2p rotations and product identity. Do not cite EGZ(n=2p) at this shorter length.
2. **m2 marked formula:** call it the single-mark variant; the product is rho_V in the chosen cyclic frame and a conjugate in the original order. The invariant assertion is “identity iff V=0.”
3. **m3 Doubling:** choose a P-gap (for example t0) as the fixed gap; do not fix an M-gap when using the displayed union-of-colourings argument.
4. **m4 Davenport-alpha:** state N<=4p-1 and F>=2; begin the frame at a gap outside I. A zero-sum item subset then has size2p, not an uncontrolled multiple of2p. All load-bearing applications have N=4p-1.
5. **m5 OR:** use necessity of HW/H on the original and sufficiency on the reduced word. Empty-pattern conditions refer to the identical interval I(empty); the min(A,B)<=kappa shorthand needs A,B<=2p-1, true for avoiders.
6. **m6 reflection pairs:** rotate the wrapping cyclic reflection run before pairing, or conjugate the selection back; do not assert every chosen pair is linearly adjacent before choosing the frame.
7. **DC-1:** v4:122's “only Delta0>=3 and k>=7” is false as an unrestricted statement. GC also uses the full NMH setting and the identities named in GC verdict erratum5. Theorem A and B's reduced word satisfy all those hypotheses.
8. **DC-2–DC-5:** D0 is the only **nonautomatic** inherited hypothesis; the S1 Steps3–4 Codex check is its C0-B' paragraph; the change log omits two cosmetic changes; and C2's re-justification plus the new non-inherited B=0 remark are not merely wording. No theorem statement changes.
9. The old “not independently reviewed” theorem-P header and v4's missing-second-family status paragraphs are historical; this verdict and the foundation coverage supersede them. They are not retroactively relabelled preregistered.

## Boundary

Correctness acceptance is for the written restricted statements above, with classical imports and the displayed errata. No Lean/Comparator proof, external kernel, human review or publication. The finite E2/315-row material is not used. No novelty/significance verdict is made. The ongoing rotation/reflection INV* slices are still required for unrestricted ordered Olson and may not assume their own conclusion.
