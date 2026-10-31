# Shor completion: an outside-head / actual multi-b escape dichotomy

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 18:36:01 PDT 2026**.
**WRITTEN all-order necessary condition; bounded synthetic checks of its packing lemma; not a completion, universal no-go, formal proof or novelty claim.**

## 1. Exact statement

Let D be an arbitrary **finite, uniquely decipherable, factor-complete** extension of the literal Shor S, let `a^n` be its actual pure-a atom, and B its actual atoms containing exactly one b. As independently reconstructed in `frontier-20261028-six-head-border-factorization-v1.md` and the no-saturated-lines packet, `|B|=n`, `n>=26`, and the same actual D determines the one-b residue layer and b-run borders. No hypothetical separate models are combined.

For an atom `a^i b a^j` write its head and tail modulo n. Put

    A={0,3,8,11},
    I_0={i mod n : a^i b a^j in B and j==0 mod n},
    c_0=|I_0|,
    N_out=#{actual B-atoms whose head mod n is outside A}.

The old four atoms `b,a^3b,a^8b,a^11b` give `A⊆I_0` and `c_0>=4`. Atoms with tail exponent a **nonzero multiple of n** also count in `I_0`; do not silently treat every such atom as `a^i b`.

Then the following exact quantitative tradeoff holds:

    N_out >= n - 4 floor(n/c_0).                                  (1)

Consequently **every such D satisfies the following dichotomy**:

* Either `N_out >= n - 4 floor(n/5)` (in particular `N_out>=ceil(n/5)`),
* or D contains an actual atom `a^i b^k` with `k>=2` and `i mod n` outside A.

More sharply, in the second case the same border set

    P={i mod n : a^i b^k in D for some k>=1}

contributes at least `|P|-4 >= 1` **distinct head residues**, each realized by at least one such multi-b atom. This is a necessity statement, not a construction or a claim that these atoms solve the remaining consistency constraints.

## 2. Proof of the zero-column packing inequality

Let `J_h` be the set of tail residues of B-atoms with head h. For every h, `J_h + I_0` is direct modulo n. Indeed, if `j+h_1 == j'+h_2 (mod n)` for two pairs, choose actual B-atoms with first head h and tails j,j', and actual B-atoms with heads h_1,h_2 and tail residues0. Padding by actual `a^n` atoms in the interior and after the last b gives two raw-identical concatenations. Distinct pairs give distinct D-word lists, contradicting UD. Thus

    |J_h| c_0 <= n,      |J_h| <= floor(n/c_0).

Because B has exactly n atoms and distinct actual one-b atoms cannot share a residue pair under UD plus `a^n` padding, the number whose heads are in A is precisely `sum_{h in A}|J_h|`. Summing the row bound over the four literal old heads yields (1).

If `c_0>=5`, (1) implies `N_out >= n-4 floor(n/5)`. Otherwise `c_0=4` because the four old heads already occur. In this latter case the four old atoms completely occupy the zero-tail residue column: **no one-b atom with head outside A has tail divisible by n**, whether its literal tail is zero or a positive multiple of n.

## 3. Why the small-outside branch needs actual multi-b words

The independently written border proof in the cited predecessor gives the direct tiling `P+Q=Z_n`, with `A⊆P`, `Y={0,1,7,13,14}⊆Q`, and `|P|>=5`. The latter bound is explicit: if P=A, residue6 has candidate complements `6,3,-2,-5`; each collides with either old Q-element0 or1 through the A-elements, so it cannot be covered uniquely. This argument is valid for all feasible `n>=26`.

Assume the small-outside alternative `N_out < n-4 floor(n/5)`. Section2 gives `c_0=4`. For each of the at least `|P|-4` residues in `P\A`, choose its ACTUAL representative `a^i b^k` from D. If `k=1`, that actual atom is a one-b atom with tail0 and a head outside A, contradicting `c_0=4`. Therefore `k>=2`. Different chosen head residues require different actual atoms. This proves the dichotomy and its quantitative refinement.

For example, at `n=1320`, every such D either has at least264 one-b atoms with heads outside A or has an actual multi-b border atom as above. Conditional on the separate six-head/valuation assumptions `|P|=6, v_3(n)=1, v_2(n) in {2,3}`, the cited predecessor shows the two new P-residues are respectively1 and4 modulo6. In the small-outside branch, **both** must be realized by actual `a^i b^k` atoms with `k>=2`. This is an additional necessary coupling; it does not establish that this branch exists.

## 4. Bounded check and limits

Independent file `frontier-20261028-zero-column-tradeoff-check.py`, SHA256 `012855bc832923564a722ed620979f92c921855a60a2909395a10f8423dd84f2` (59 LF, 2219 bytes), implements Sardinas–Patterson and explicitly enumerates synthetic layers containing b plus `a^n`. For n=4 it tested all455 full-size layers, found134 UD, and checked the general outside-head inequality for276 choices of nonempty anchors contained in their zero-tail columns. For n=5 it tested all10626 layers, found1226 UD, and checked2568 anchor choices. It also checked each row's direct zero-column sums. A deliberately non-UD four-cell negative control violates the claimed bound and is rejected by Sardinas–Patterson. These are synthetic finite controls, **not** examples of Shor completion, checks of the border theorem, or a proof over all n.

The already known general border-factorization theorem is prior literature (Cordero, arXiv:2301.13566, Theorem1.1); the present combination and its priority have not received a novelty screen. All claims here are same-harness written mathematics, with the expressly described small integer program only checking finite controls. No human, formal/kernel, independent-family or novelty gate is claimed. The unrestricted existence/nonexistence of a finite UD factor-complete extension of S remains open.

**END OF ZERO-COLUMN / MULTI-B ESCAPE PACKET.**
