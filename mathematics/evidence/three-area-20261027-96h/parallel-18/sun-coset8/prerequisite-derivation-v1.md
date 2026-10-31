# Sun8 definition-first prerequisite: normal-fibre capacity and uniform-quotient transfer

Actual `/bin/date` before this NEW body: **Tue Oct 27 14:52:23 PDT 2026**. Owner **MathSun8-2**, original math-6. **WRITTEN candidate**, not parent-adopted, formal/kernel, executable, independently configured-family, human or novelty-verified. No identity was machine-checked.

## 1. Released target, inputs and precise advance

The exact released literal assertion is: for EVERY group G, EVERY eight finite-index subgroups U_1,...,U_8 (possibly equal), and EVERY eight pairwise-disjoint ACTUAL LEFT cosets g_i U_i, some distinct i,j satisfy

`gcd([G:U_i],[G:U_j]) >= 8`.

There is no original-group finiteness, covering, normality, solvability, valuation or private-factor restriction. A counterconfiguration means exactly the eight stated actual cosets with all pairwise index gcd at most7.

Source: released packet S2 LF5-7, extracted by Main from selection LF5-7. The packet declares the Sun paper/book identities but NO newly reread primary text; this proof addresses the released literal assertion, not an independently certified book/source equivalence. Exact packet SHA256 `35030527e0947907a17521c58e12d8ccd0e1665330f4f4bd2eae4b557c96970a`,39LF/5643B. Controls FIRST, release, pre-body exposure ACK, then complete packet/receipt were read in that order. Pre-body ACK SHA256 `893b5fbd53dd35788246496e214606b26f335adba0e674fc63eadaafd3f0cfa5`.

**Advance:** a universal normal-subgroup coupling inequality, followed by an eight-coset exclusion whenever all eight images have the SAME nontrivial finite quotient index. This is not merely a fibre encoding: the capacity inequality rules out that entire normal-extension configuration using only the allowed k=3,4 statements and an elementary k=2 proof. It does NOT prove arbitrary normal-extension closure or Sun8 globally.

Allowed inputs actually used:
- Ordinary subgroup/index/coset facts, finite coset permutation actions, normal cores and elementary finite counting; each application is proved or specified below.
- **Zhu k=3 and k=4, at STATEMENT level only:** in any group, r actual pairwise-disjoint left cosets of finite-index subgroups, for r=3 or4, have a pair of subgroup indices with gcd at least r. These are the explicitly licensed imports, not a new proof/replay of Zhu.
- Arbitrary-group Sun7 is licensed at statement level but is NOT needed for this packet. No earlier Sun proof, review, park, checkpoint, special family, P7 candidate or quarantined guide is an input.

## 2. Elementary two-coset fact

If H,K are finite-index subgroups of any group X, put `h=[X:H]`, `k=[X:K]`, `m=[X:H∩K]`. The diagonal map from the ACTUAL left-coset set X/(H∩K) into `(X/H)×(X/K)` is injective, so m is finite and m≤hk. The index chains show both h and k divide m. If gcd(h,k)=1, then hk divides m, whence m=hk and the injection is a bijection. Every pair of actual H- and K-cosets therefore intersects. Consequently two disjoint such cosets force gcd(h,k)≥2. This argument includes infinite X and equal subgroups and assumes no normality.

This supplies the r=2 statement used below without a further import.

## 3. Exact normal-fibre identity, with its actual-object converse

Fix ANY normal subgroup N of G; neither N nor Q=G/N need be finite. Let π:G→Q and define, for each original source label i,

`H_i=U_i∩N`, `A_i=π(U_i)=NU_i/N`,
`a_i=[Q:A_i]=[G:NU_i]`, `b_i=[N:H_i]`, `n_i=[G:U_i]`.

N normal makes NU_i a subgroup. The bijection `nH_i↦nU_i` identifies the coset set N/H_i with NU_i/U_i. The index chain gives the EXACT finite positive-integer identity

`n_i=a_i b_i`.                                                   (3.1)

Let `C_i=π(g_i)A_i`, an actual quotient coset, and for q∈Q define the labelled load set `L(q)={i:q∈C_i}`. Quotient cosets may overlap or coincide: they are not asserted disjoint.

For each fixed q choose x∈G with π(x)=q. For i∈L(q), choose u_i∈U_i with π(g_i u_i)=q, and put `h_i(q)=x^(-1)g_i u_i∈N`. Then

`x^(-1)(g_i U_i∩π^(-1)(q)) = h_i(q) H_i`.                       (3.2)

To prove equality, another point in that fibre has form g_i u_i' with u_i'∈U_i and π(u_i')=π(u_i); hence u_i'=u_i h for h∈U_i∩N. Conversely every such h produces a point in the fibre. Different choices of u_i change h_i(q) only within the SAME left H_i-coset; changing x left-translates all fibre cosets together.

Thus the original eight cosets are pairwise disjoint **IFF**, for EVERY q, the ACTUAL induced N-cosets in (3.2), indexed by L(q), are pairwise disjoint. Forward implication is restriction and translation. Conversely any intersection of two original cosets has some image q and would give an intersection in that fibre. All U_i,g_i are the SAME fixed original objects throughout; this is NOT a converse permitting arbitrary independently chosen local packings to be glued into a group configuration.

Together with (3.1), an original counterconfiguration is equivalently these actual fibre-disjointness conditions plus `gcd(a_i b_i,a_j b_j)≤7` for every i≠j. This exact interface is used for the inequality below; it is not alone counted as scientific progress.

## 4. Normal-fibre capacity theorem

**Theorem 4.1 (WRITTEN, with the exact Zhu imports).** Suppose an original Sun8 counterconfiguration exists. Choose any normal N, any subset J of its eight source labels, and any INTEGER d with `2≤d≤7` such that

`gcd(a_i,a_j) >= d` for every distinct i,j∈J.                     (4.1)

Put `s=floor(7/d)`. Then BOTH of the following hold:

`|J∩L(q)| <= s` for EVERY q∈Q,                                  (4.2)
`sum_(i∈J) 1/a_i <= s`.                                         (4.3)

These are actual joint-source necessary conditions, not a source-character or numerical instance test.

**Proof of (4.2).** Any common divisor of a_i,a_j times any common divisor of b_i,b_j divides BOTH products a_i b_i,a_j b_j. Therefore (3.1) and the counterconfiguration give

`gcd(a_i,a_j) * gcd(b_i,b_j) <= gcd(n_i,n_j) <= 7`.               (4.4)

In particular on J, `gcd(b_i,b_j)≤floor(7/d)=s`. If s+1 members of J were active at one q, (3.2) would give s+1 actual disjoint finite-index N-cosets with every pair index gcd≤s. This contradicts the licensed r=s+1 assertion:
- d=2 gives s+1=4, using Zhu k=4;
- d=3 gives s+1=3, using Zhu k=3;
- 4≤d≤7 gives s+1=2, using §2.

This is the exhaustive symbolic d-range, not selected probe arithmetic. No Sun8 assertion in N is assumed. Empty J, empty loads and |J|≤s already satisfy the conclusion; no existence of a forbidden subfamily is presumed.

**Proof of (4.3), including infinite Q.** If J is empty there is nothing to prove. Otherwise let K be the intersection of the normal cores of the finitely many finite-index A_i in Q. Each core is the kernel of Q's action on its finite coset set, so K is normal of finite index and K⊂A_i for every i∈J. In the finite group X=Q/K, every C_i is the exact pullback of a coset of size `|X|/a_i`. The labelled load is constant on K-cosets and still bounded by s. Count incidences between X and the source labels:

`|X| * sum_(i∈J) 1/a_i = sum_(x∈X) |{i∈J:x∈C_i/K}| <= s|X|`.

Cancel the positive integer |X| to obtain (4.3). All labels and overlaps are retained, including repeated A_i or identical quotient cosets. This is a written all-variable finite-counting proof, not a scientific enumeration or a selected finite quotient test. □

**Limits.** Restricting d to2..7 is essential to the printed capacity formula. For d≥8 a counterconfiguration cannot have TWO labels satisfying (4.1), but a single quotient coset can of course have load1; no false floor-zero bound is asserted. For d=1, this argument would demand the very Sun8 statement in N that is still unproved. It gives NO such bound.

## 5. Uniform-quotient-index consequence: a complete normal-extension subcase

**Corollary 5.1.** For ANY group G, ANY normal N and ANY eight actual disjoint finite-index left cosets as in the ORIGINAL target, if

`[G:NU_i]=a>1` for ALL eight labels,                             (5.1)

then some pair of original indices has gcd≥8.

**Proof.** If a≥8, a divides every n_i and any distinct pair already has gcd≥8. Otherwise `2≤a≤7`. Suppose a counterconfiguration existed. Apply Theorem4.1 to all eight labels with d=a. Equation(4.3) gives

`8/a <= floor(7/a)`.

Multiplication by a yields `8≤a floor(7/a)≤7`, a contradiction. This covers the entire a>1 range, without classifying G, its subgroups or the quotient. □

The hypothesis does NOT require equal U_i, equal n_i, normal U_i, identical A_i or covering. It is equality of the quotient-image INDICES for one normal N. The exact fibre converse in §3 proves that every original configuration with this hypothesis is a valid caller. It does not assert that a suitable N exists for every original configuration.

The omitted a=1 branch is explicit: every quotient image is all Q, all eight labels occur in every fibre, and (3.1) has b_i=n_i. Sun8 in N would settle that branch, but Sun7 or Zhu3/4 does not license applying an eight-coset theorem. This is an exact remaining implication, not a claim of a counterexample or a source-separated no-go.

## 6. What changed; exact gap and continued work

Changed: we have a fresh all-variable normal-fibre capacity inequality (4.2)–(4.3) and the complete uniform-nontrivial-quotient-index exclusion (5.1), at the stated Zhu k=3,4 imports. These couple the SAME actual eight sources across N and Q. This is more than an encoding and not another SL/Sp/classical-family range or conditional bounded-simple result.

Not changed: arbitrary Sun8, a general extension/composition theorem, existence of a useful N, all heterogeneous quotient-index patterns, the a=1 branch without an N-Sun8 premise, P7 emptiness/Sun8-to-P7 bridge and any original numerical/global conclusion remain open. The inequalities are NECESSARY only, never a converse construction of actual cosets. No novelty/SOTA claim is made; Main and full-scope reviewers have not adopted this candidate.

Next admitted all-variable step: investigate a genuinely general normal-extension transfer from a PROVED/explicitly assumed Sun8 statement in N under a sharply stated quotient intersection condition, retaining actual fibre compatibility. No old least-order/P7/mixed-source proof is imported, and no selected group/control is tested. Any indispensable unpaid hypothesis will be named rather than silently assumed. This next step remains inside the same definition-first release; this file is not a research stop or final park.

## 7. Permanent boundaries

Only released definitions, current controls/intake and the named elementary and Zhu statements are inputs. Original authorship/exposure and every prior process finding persist; no blind, clean-cognition, counterfactual method-independence or configured-family claim. All old proposed sources, v233/v234 mathematical material, held/withdrawn/ZERO consumers and original STOP outside this narrow release remain NONINPUT. No old proof/review/park/checkpoint/PDF/book extraction was opened.

No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numerical/control/boundary probe, nested agent/modelCLI/paidAPI/newGO, Git/deletion/publication/contact/infrastructure mutation, timer/poll or heartbeat loop. Machine tools are metadata only. N4 UNKNOWN with historical child exit unestablished; auxiliary214 STOP; scientific HOLDv2 unchanged. New research deadline2026-10-31T21:23:27.000Z, no earlier science cutoff. This is WRITTEN prerequisite progress, not a Sun8 solution, independent primary-source equivalence check, stronger verification or round closeout.
