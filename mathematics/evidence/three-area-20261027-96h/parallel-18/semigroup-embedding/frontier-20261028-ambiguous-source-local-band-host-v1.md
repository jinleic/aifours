# The ambiguous-row source embeds in a genuinely locally regular band host

**NEW AUTHOR WRITTEN + EXACT FINITE-CHECKED CANDIDATE; unreviewed/unadopted.** Native check-start observations **Wed Oct 28 18:45:39 PDT 2026** and **18:46:01 PDT 2026**. This explicitly embeds the SAME 45-element source as `frontier-20261028-all-cs-globally-regular-band-obstruction-v1.md`, SHA `2f9f6a68a153449b61cda78305174c5b601e28fba49ec391bc1107aaba8e31af`, into a host over its ACTUAL syntactic actor, using a locally regular band that is not globally regular. Thus that source is not a counterexample to the original locally regular target. This is one finite source and its opposite, not the general original problem.

## 1. Target band and action

Let B0={0,1,2,3,4} have multiplication

```text
0 2 2 4 4
0 1 2 1 4
0 2 2 2 4
0 3 2 3 4
0 4 2 4 4
```

The additive boundary note `frontier-20261028-local-band-four-term-countermodel-v1.md`, SHA `7be9d26f0941fc37728b7305dc9451c1b3586e442e87a5c976be13f2ad8dd72f`, gives and directly checks its5 local corners: `{0}`, `{1,2,4}`, `{2}`, `{2,3,4}`, `{4}`. Each is regular; the two nontrivial corners are right-zero bands with identity.

Take `B=B0×B0` with coordinatewise multiplication. A local corner of a direct product is the product of the local corners, so B is a locally regular band. B is NOT globally regular: for `x=(1,1)`, `y=(0,1)`, `z=(3,1)`, `xyxzx=(2,1)` while `xyzx=(4,1)`. The group C2 acts on B by the involutory automorphism

`α_1(b,c)=(c,b)`.

Thus the construction lies in the original local-band target class rather than contradicting the globally-regular obstruction.

## 2. Source and coefficient table

Use A, θ, I,Λ and the original-class source S from the globally-regular obstruction, with

`P=((4,4,4),(4,1,3),(4,4,1))`,
`θ=(0,1,0,1,0):A→C2`,
`q(i,a,λ)=(i,θ(a),λ)`.

The q actor is the actual syntactic 18-element quotient, not just an onto pure auxiliary actor; its sandwich group matrix has distinct rows and columns, and the exact checker below exhausts the source context tests.

For `s=(i,a,λ)` use band coordinate C(s)∈B as follows. When a is 0,1,2 or3 the entries are independent of the source row i:

```text
             lambda 0      lambda 1      lambda 2
a=0           (2,4)         (2,0)         (2,4)
a=1           (4,4)         (0,4)         (4,4)
a=2           (4,4)         (4,0)         (4,4)
a=3           (4,2)         (0,2)         (4,2)
```

For the identity middle value a=4 put

`C(i,4,λ)=(u_i,v_λ)`, with `u_0=u_2=1`, `u_1=3`, `v_0=v_2=4`, `v_1=0`.

For every source pair `s=(i,a,λ)`, `t=(j,b,μ)`, the finite table satisfies

`C(st)=C(s) · α_(θ(a)+θ(P_(λ,j)))(C(t))`,                 (1)

with multiplication coordinatewise in B. The actor coordinate simultaneously multiplies in the completely simple Rees quotient q(S), so `j(s)=(C(s),q(s))` is a physical whole-host homomorphism. Section4 gives the exact independent-from-solver table check of every one of the45² equations.

## 3. Faithfulness, actual q and the dual L case

If j(s)=j(t), the actor supplies the same row i, column λ and θ(a). If θ(a)=0, the possibilities a=0,2,4 have distinct coordinates: for λ=0 or2 their first coordinates are respectively 2,4,u_i∈{1,3}, and for λ=1 they are again 2,4,u_i. If θ(a)=1, a=1 and3 have respective second coordinates 4 and2 for every λ. Thus the source middle values agree and j is injective. The concrete same-q R-idempotents from the global obstruction,

`e=(1,1,1)`, `f=(1,3,1)`,

have `C(e)=(0,4)` and `C(f)=(0,2)`, so this model explicitly separates the exact pair a globally regular band must collapse.

Since q is actual, mapping the canonical V-band generators to the action translates of C(s) respects (1) and all locally regular band identities. Consequently the actual canonical κ_q is injective for this source. This is a model-specific and source-specific result, not an assumed equivalence between the whole registered problem and the printed questions.

For the opposite source, reverse the band and actor multiplications; present the actor coordinates as `(λ,θ(a),i)`, and set

`C^op(s)=α_(θ(a))(C(s))`.

The standard reversed-product calculation gives a physical host in `B^op` with the same factor-swap action. Its local corners are still regular. The direct verifier below checks every opposite-source product and injection; e,f become a nontrivial same-actor L-idempotent pair, separated by `(4,0)` and `(2,0)`. Actual τ for the opposite is the original τ with left/right contexts interchanged. Hence both the R example and its L dual are explicitly paid at their exact finite scopes.

## 4. Exact finite checks, controls and provenance

`frontier-20261028-ambiguous-source-local-host-checker-v1.py`, SHA `5d6925c7e019b5dcbfcfdffc3c71809bbf9b59b711b65fcb9ad8f7a0c4535af1`, ran with `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 18:45:39 PDT 2026**, exit0:

```text
source=45 actual_actor=18 band=25 source_idempotents=24
PASS B5^2 band, all25 regular local corners, explicit global regular identity failure
PASS coordinate-swap C2 action; all2025 actor/host products and injectivity
PASS actual tau by all 46^2 contexts per source; actor pure
nontrivial same-actor R pair e,f=(1, 1, 1)(1, 3, 1) band values=(0, 4)(0, 2)
CONTROL identity action breaks source-product equations=651
```

The check reconstructs the literal25-element band, verifies every band triple, every local-corner regular-band triple, the complete involutory action, all source product and same-q injectivity comparisons, and 46² idempotence contexts per source element. Its control replaces the nontrivial swap by the identity and observes651 actual source-product failures; it is not a general no-trivial-action theorem.

`frontier-20261028-ambiguous-source-dual-local-host-checker-v1.py`, SHA `3191a2106521033b0cdc903550f66d5821d156fdc06887c58cca05a42abd0b58`, ran at **Wed Oct 28 18:46:01 PDT 2026**, exit0: all25 opposite-band corners, all45² dual products and injection pass, with the displayed L pair distinct.

The coefficients were found by bounded Z3 4.15.4 source search `frontier-20261028-countermodel-power-host-search-v1.py`, SHA `dae405a0077f00ad2bbb5ba96440a4da8bd99c1d13d4ce86e59f759dbebfa55a`; SAT and a full direct recheck were observed at18:43:42. The two literal-table verifiers above do not import Z3. All are same-author programs: no independent review, triple finite-witness certification, formal/kernel verification, novelty or lower-bound claim is made.

**Interpretation:** subject to independent review of the earlier all-CS global-regular obstruction, this one original-class source has no globally regular-band-by-CS host but does have the locally regular host explicitly displayed here. The general original full-class R/L/SEP obligation and printed questions remain open.
