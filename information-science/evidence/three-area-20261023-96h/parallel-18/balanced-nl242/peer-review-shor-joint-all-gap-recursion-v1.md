# v37-B — written reconstruction of the all-positive-gap recursion

Reviewer InfoBalancedNL242-2, info-6; author MathShor. Actual pre-return clock: `Sun Oct 25 05:13:05 PDT 2026`.

## 1. Binding, complete coverage and verdict

- Manifest `peer-review-wave-eighteen-v37.json`, v37-B: SHA-256 `eb3d6f624c9e191702658bf2a8c969b2904e9aa347c91df173b131c0be1dba54`.
- Literal packet `peer-review-wave-v37-shor-joint-all-gap-recursion-sources-v1.md`: SHA-256 `a70e701afd9c49487b46197621c2648017d7dd80118c0d4e1779df640de88aa1`.
- Source `shor-heterogeneous-completion-consolidated-v1.md`, LF1–365: SHA-256 `d249dd4129944f62beb73c78783bfee7a2e2feef155a1c941ffd3158cb4cb9a9`.

All three pins were freshly observed by metadata-only shasum. The exact packet receipt was read. Every source line was read through the374-line packet, followed by raw reads of the long provenance, GP, endpoint, shared-run, recursion, ALL/Q and restricted-root statements. No footer omission was treated as read. References below are SOURCE LF.

The exposure ACK is `peer-review-shor-joint-all-gap-recursion-ack-v1.json`. The reviewer previously reconstructed the author's pure-run/one-gap and joint-two-gap sources, but does not transfer their verdict to this successor: the new recursion and its finite interface are reconstructed below. This remains reciprocal same-harness supplied-proof cross-domain review, not blind, cross-model, human, formal or novelty acceptance.

**Verdict: 0 FATAL / 0 MAJOR / 0 MINOR at the reconstructed conditional written scope.** Exact all-positive-gap recursion, the empty/nonempty shared-run distinction, denominator control and the abstract finite invariant-subspace condition are supported at the named raw GP/automaton interface. No actual finite extension, universal many-gap feasibility or unrestricted Shor completion/noncompletion is accepted.

Parent v7 was reread. This review used written reasoning, source reads and metadata clocks/hashes only. No scientific interpreter/eval, enumeration program, symbolic program, certificate replay, solver or GO occurred.

## 2. Actual-word prerequisites and the joint matrix

LF32–73 correctly distinguishes a raw finite candidate containing b from endpoint polynomial data alone. No second pure-b word can coexist in a UD code. Any complete candidate must have exactly one pure power a^n; otherwise its zero-gap parses are length-bounded, or two pure powers give an ambiguity.

At zero b-gap a join requires both touching delays0. Thus the optional start/pure-power-chain/optional end and singleton-isolated cases are disjoint and exhaustive. Including the empty endpoint markers gives `LR/Delta+H=1/(1-z)`, hence PR. The cyclic factorization and LIFT follow by nonnegative residue coefficients and `(z^k-z^(k+nh))/Delta`; they do not realize a globally UD code merely by solving residues.

For LF77–109, P has row initial delay and column final delay. `L_e R_d/Delta+H_ed` counts all pure-run parses with those endpoints; subtracting1 only at(0,0) removes exactly the empty parse. Consequently P_00=z^n/Delta. Actual delay profiles remain attached to labels, and their row/column sums are not independently coupled.

T_g contracts a prior final delay with a subsequent initial delay. It supplies exactly the unique b surplus when d+e<=g. PZ attaches a nonempty pure prefix only to an initial bridge delay0, and ZP attaches a nonempty pure suffix only from final bridge delay0. Thus A=I+PZ and B=I+ZP include empty attachments exactly once with the stated matrix orientation.

W_gamma is an actual finite-word polynomial matrix, with positive a-run exponents and all listed positive internal gaps. A codeword cannot skip a core gap or hide extra a-runs in an outside b-padding margin. A finite candidate has finitely many nonzero W_gamma, but that does not bound the number of gaps in products of its words.

## 3. Exact JOIN and the first two specializations

For two distinct bridge words touching the same adjacent a-run, both touching delays must be0. The intervening pure material is either empty (Z) or a nonempty both-zero-endpoint parse (ZPZ). Therefore

    Z+ZP(y)Z=Z/(1-y^n).

This includes an empty intervening chain, not an empty codeword. Each bridge still consumes a positive segment of the shared a-run. Two independent attachment factors would introduce an arbitrary split of that same pure chain and overcount it.

The one-gap formula has precisely no crossing versus one crossing word. The two-gap formula has exactly neither crossing, first only, second only, two distinct words, or one word crossing both. These statuses are disjoint and exhaustive because a fixed gap can be crossed by at most one word in an ordered parse. Longer words cannot fit those smaller cores. This reconstructs the consolidated G1/G2 and JOIN at LF113–142 directly, not solely by citing the earlier review.

## 4. The new continuation E_j — every empty case retained

Fix gamma=(g1,...,gk), all gaps positive. D_empty=P counts a nonempty final a-run; it is not an identity matrix or an empty parse.

Suppose the word crossing the FIRST gap crosses exactly the first j gaps. It may start after an optional pure prefix of the first run; A supplies that prefix. Its last a-run lies in shared run j.

### j=k

There is no subsequent positive gap. What remains can be either an empty suffix or a pure-run suffix with zero-gap attachment. This is exactly B(x_k), including arbitrary actual final bridge delays for the empty-suffix case.

### j<k, nonempty adjacent a-material remains

There is a positive remainder of shared run j. The rest is counted by `D_(g_(j+1),...,g_k)(x_j,...,x_k)`; its first run is nonempty. The previous bridge can meet that remainder only if its final delay and the next word's initial delay are0. Left multiplication by Z selects exactly those two indices. This is the first term of E_j.

### j<k, no adjacent a-material remains

The previous bridge ends at the final a of run j. The next real boundary is positive gap g_(j+1), so T_(g_(j+1)) applies the actual delay inequality and unique b surplus. The remaining core starts in run j+1, giving the second D in E_j, with no extra x_j power.

When j=k−1, that latter D is D_empty(x_k)=P(x_k): the final a-run is still nonempty. No nonexistent x_(k+1) is introduced. The two continuation branches cannot describe the same raw parse because they differ by whether any a remains in run j. Both allow all actual finite outer delays without replacing them by a common tail.

This establishes R1/R2 at LF204–219, including their endpoint indexing and dimensions.

## 5. Inductive proof of R3: necessity and converse

If no word crosses the first positive gap, every a in run0 is covered by a nonempty pure-run parse P(x0). The next actual boundary uses T_g1; everything after it is exactly the shorter positive-gap core. This gives the first term of R3.

Otherwise there is a unique first-gap crossing word. Its raw interval determines the last positive gap it crosses, j. It is therefore one of the actual labels in W_(g1,...,gj), not an arbitrary correction polynomial. The prefix and continuation are uniquely determined by that same raw parse and by the preceding empty/nonempty alternatives. The second term of R3 lists it exactly once.

Conversely, each product term concatenates actual labels, legal zero/positive boundaries and their uniquely determined b surplus. It produces a raw free-end parse of the claimed core. The prefix choice, crossing word, j and continuation distinguish all terms, so neither labelled parses nor alternative cuts are counted twice.

Every D on the right has strictly fewer positive gaps: the no-crossing term uses k−1; the two j<k branches use k−j or k−j−1. Together with D_empty=P this proves the recursion inductively for every finite positive-gap word, with no length cutoff or bound on a word's number of a-runs.

At k=1 the suffix is B, giving G1. At k=2, the first-bridge continuation is

    Z[P(y)T_hP(z)+A(y)W_h(y,z)B(z)]+T_hP(z).

Its no-second-crossing terms combine into `(I+ZP(y))T_hP(z)=B(y)T_hP(z)`. Its two-bridge term contains `ZA(y)=Z+ZP(y)Z=Z/Delta(y)`. The j=2 term is the one word crossing both gaps. Together with the no-first-crossing term, all five G2 cases are recovered exactly.

## 6. ALL, denominator control and what it does NOT solve

For every actual finite candidate satisfying the stated prerequisites, coefficient summation by all-ones endpoints is precisely its labelled free-end parse count. Thus ALL says every positive run-length choice at every positive-gap word has count1.

Every nonnegative raw a-gap list has a unique compression into adjacent a-runs separated by positive gaps. The k=0 case handles the one-run core; b-only strings are handled by b. Therefore ALL for **all k and all positive-gap words**, together with actual-word binding and b/no-other-pure-b, is exactly the GP universal condition. This is a conditional characterization, not a proof that any Shor candidate satisfies it.

Denominator induction is also valid. P and A,B have one pure-chain denominator in their own variable. In R3 the prefix variable x0 is not a variable of its recursive D. W is polynomial. E_j's first branch uses the shared variable x_j once in its shorter D, while its second branch uses no x_j continuation at all. Consequently no term acquires a second independent denominator for a shared run. Every D_gamma has denominator dividing the product of the single factors(1-x_i^n). Clearing that product is invertible in formal series and makes each particular ALL a finite polynomial identity.

It does **not** make the universal collection finite in k: finite actual W support still allows products of arbitrarily many words. No finite family of checked low-k identities, nor the recursion alone, has been substituted for that quantifier.

## 7. The finite Q interface — algebra reconstructed, candidate absent

At LF281–292, choose B_* dominating every actual internal a-gap and every possible pair of touching outer delays. A gap above that bound matches no internal gap and permits every external boundary. Replacing it by infinity therefore preserves each raw-automaton transition. This caps the gap alphabet, not word length.

Conditional on the named GP automaton count interface, write accepting counts as `I A_word F`. Let `nu=(F;1)` and D_c=diag(A_c,1). If nu=Vz, D_c V=VT_c and `(I,-1)V=0`, every orbit product D_word nu lies in col(V). Its annihilation by(I,-1) gives `I A_word F−1=0`. This proves every accepting count is1, including the empty transition word.

Conversely, if those counts all equal1, take the rational span of all D_word nu. It is finite-dimensional, contains nu, is invariant under every D_c and is annihilated by(I,-1). A rational basis V gives rational coordinates z,T_c. Thus the abstract Q identities are iff for that supplied finite candidate/automaton interface. No actual M, V or Q data are present or accepted in this review.

## 8. Consolidated earlier boundaries checked in this source

The K0 data give the stated P entries and two W_1 labels directly. Its proper-prefix residual is only `aba`, with no further prefix relation, so UD is reconstructed independently of the full M0 proof. Its Kraft31/32 and the explicit missing `a b² a b a` core confirm its role as an incomplete control; the listed M0 additions are not a Shor proposal.

The restricted pure-end obstruction at LF300–350 remains correctly scoped. The actual raw collision equality holds for every beta>=1. R4's signed multiplier puts forced residues13 and14 into the coefficient22, independently of n. For R5 the minimal relation argument forces squarefree conductor dividing30; the eight displayed reductions are nonzero below the relevant minimal degrees (with eta=-zeta for30). A nonminimal relation splits into opposite pair/cube-root triangle; all difference gcds are1 except the step8 triple, which contradicts its complementary pair. Hence R5 is invertible in every cyclic quotient, forcing L=S_n/5. This reconstructs the written chain at its classical cyclotomic imports, not the old evaluated remainder table. The conclusion is only an actual pure-end escape ell>=26, not unrestricted noncompletion or automatic iteration after a seed change.

## 9. Explicit NOT_RECONSTRUCTED obligations and exclusions

1. **Original GP proof, original raw automaton construction/parent acceptance chain, and full M0 completeness construction:** NAMED IMPORTS, not re-audited from their original source files. The recursion and Q algebra are conditional on those specified interfaces. No general residue realization converse is used.
2. **An actual finite Shor M, its literal word matrices, its invariant-space witness V,z,T_c, or feasibility of ALL for every gap word:** absent and NOT_RECONSTRUCTED. The author explicitly leaves these open.
3. **A uniform obstruction eliminating every finite heterogeneous choice or larger pure-end support:** NOT_PROVED and not inferred from the representation theorem.
4. **Earlier scientific arithmetic certificates, admission/resource/exit claims, independent-model/human/formal/novelty gates:** not performed, replayed or accepted. Parent v7 and all mandatory disclosure overlays remain binding.

No source repair is requested at the explicit written/conditional scope above. The unrestricted Shor target remains open. All review files are confined to the reviewer's root; frozen author and shared sources are unchanged.
