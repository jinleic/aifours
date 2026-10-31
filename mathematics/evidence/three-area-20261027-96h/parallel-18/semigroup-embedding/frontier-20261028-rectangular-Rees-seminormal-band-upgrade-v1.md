# The rectangular-group Rees lifts use seminormal bands

**NEW AUTHOR WRITTEN TARGET-SCOPE UPGRADE with exact finite controls; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 20:05:39 PDT 2026**. This is an additive strengthening of `frontier-20261028-unrestricted-rectangular-group-rees-theorem-v1.md`, SHA `f3581fcdcc70ae810a9d2bffa4c6138843bbd2fcb0ab88302e8bdaac3561403f`: its explicit physical host bands satisfy the stronger seminormal identity. It does not prove the original question for all sources or equate the printed target to the physical product without the separately unpaid D1–D4 comparison.

## 1. Seminormality of every evaluation band

Use Billhardt's [1998 definition](https://www.academia.edu/53871668/On_Embeddability_into_a_Semidirect_Product_of_a_Band_by_a_Group) of seminormal bands:

`x y z w x = x y z x z w x`.                              (SN)

Let T=U⊔N be ANY evaluation band from the predecessor: U is left-zero, `x n=n` for every x∈T,n∈N, and `n u∈N` for n∈N,u∈U. The defining selector functions may be arbitrary.

If x∈N, both sides of (SN) end in x, so both are x. If x∈U, then `z x z=z` for every z∈T: for z∈U this follows from U's left-zero law, and for z∈N it follows because zx∈N and the final z overwrites. Replacing the middle `z x z` in the right side of (SN) by z gives its left side. Thus T is seminormal, for arbitrary index sets, label sets and selector functions.

The identity is self-dual: reversing both words and interchanging y,w gives the same identity. Hence T^op is seminormal. Rectangular bands are seminormal because `x v x=x`; products, subbands and arbitrary powers preserve identities.

## 2. Consequence for the full rectangular-base Rees family

In the predecessor's theorem, BOTH evaluation bands T_R and T_L have the stated U⊔N form. Its physical host band

`B=(T_L^op)^G × T_R^G`

is therefore seminormal, not just locally regular. Its symbolic product/injection proof is unchanged. The arbitrary noncommutative G, arbitrary rectangular band K=L×R, arbitrary matrix P with the weak-E allowed form, and regular-source assumptions remain EXACTLY as in the predecessor.

The pure onto-CS actor pushforward uses an additional rectangular band factor and transports the group action via an isomorphism. Since the added rectangle and the original B are seminormal, its target band over the actual q_τ is also seminormal. The explicit Rees-gauge product/injection calculation does not rely on the weaker identity. Thus this family has a seminormal-band physical host over its ACTUAL syntactic actor, and its canonical local-band κ_q is faithful, conditional on the named pure-CS transport being accepted.

For the original-class portion, regularity and the weak-E matrix characterization are those proved in the predecessor. No unsupported claim that every original source has a rectangular-base Rees presentation is made.

The particular nonorthodox45 source in `frontier-20261028-ambiguous-source-local-band-host-v1.md`, SHA `a96cb3eeae75bba72af2cc43ff548785c74224fb7ed3509303a0f177cfb2feba`, has physical host B0². Its five-element factor B0 is an evaluation band with U={1,3}, V={0}, W={2,4}, so that SAME explicit actual-q model is seminormal. The source cannot be described as a counterexample to the seminormal physical target merely because no globally regular-band host exists.

Seminormality itself implies local regularity: in a local monoid eBe substitute its identity e for z in (SN), yielding `xywx=xyxwx`. The converse remains unproved here; the upgrade relies on the direct selector-band argument, not on identifying those two band varieties.

## 3. Exact finite checks and named limits

`frontier-20261028-seminormal-evaluation-band-checker-v1.py`, SHA `961d3736a4563c5f429489cbec7fe94bb359e42ad28dee27080f9c108c919b43`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 20:05:39 PDT 2026**, exit0. It exhausts all16 two-by-two binary selector tables, all20736 SN substitutions and associativity checks, and every625 SN substitution in the explicit B0. As a negative control it directly detects failure of (SN) in the separate six-element left-semiregular nonlocal band from `frontier-20261028-billhardt-1998-local-scope-v1.md`.

The predecessor's `frontier-20261028-rectangular-group-rees-checker-v1.py`, SHA `482a7d7cb7286f2945ae61c1f4aab2deacc8725f3fc95a5a0e47603f0d6d737c`, separately checks its222-source nonabelian S3 host and the natural36→actual24 actor transition. Those are same-author finite checks. The arbitrary-family seminormal conclusion is the symbolic §1 proof; its actual-q extension requires the named WRITTEN pure-actor pushforward. No independent witness or scientific review, formal/kernel proof, source-priority clearance or full-original/printed-question conclusion is claimed.
