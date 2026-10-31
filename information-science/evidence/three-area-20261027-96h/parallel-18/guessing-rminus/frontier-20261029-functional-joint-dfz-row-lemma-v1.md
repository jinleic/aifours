# Conditional DFZ rows in the binary-plane functional coordinates

## Required source order and exclusions

Read `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md` first, SHA-256 `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9`. Its source correction is Remark 5.4, not 3.8. For primal-countermodel evidence, also read `frontier-20261029-primal-checker-subset-coverage-erratum-v1.json` before any old v1 primal-check receipt: only corrected v2 full-row replays may be used.

This is the independent joint-DFZ route frozen in `frontier-20261029-functional-dfz-separation-route-v1.json`. No f161 review/parent consumer and no paused imported-functional-gates episode is an input. In particular, no two-syndrome entropy theorem and no functional-fiber Delta gate is used.

**Status: WRITTEN, conditional on the named exactly re-derived DFZ inequalities.** This note justifies new rows; a Delta bound still requires an independently checked exact dual identity and the existing actual-component lifting premises.

## 1. Literal entropy-coordinate substitution

In a binary affine syndrome plane, choose affine coordinates S=(A,B) and its three nonzero linear functionals L0=A, L1=B, L2=A+B. Fixed affine constants in triangle parities do not affect entropy. Every pair of distinct functionals determines S and the remaining functional, and S determines all three.

For a subset U of the ten selected vertex variables Y and a subset T of {L0,L1,L2},

- if T is empty, H(Y_U,T)=H(Y_U);
- if T={Lc}, H(Y_U,T)=H(Y_U,Lc);
- if T has two or three elements, H(Y_U,T)=H(Y_U,S).

These are entropy equalities for actual laws, since the named auxiliary tuples determine each other bijectively on their supports. They are not a claim that every glued polymatroid profile is entropic.

Thus every entropy coordinate of the full thirteen-variable tuple (Y1,...,Y10,L0,L1,L2) has a literal image in the old five-branch notation: branch 0 for no auxiliary, branch 2+c for a singleton, and branch 1 for a pair or triple.

## 2. Conditional DFZ inequalities

Let (a,b,c,d,e,f,g,h,i) be an exactly re-derived DFZ coefficient tuple. For arbitrary four random-variable tuples P,Q,R,T and conditioning tuple Z, its row is

-a I(P;Q|Z) + b I(P;Q|R,Z) + c I(P;R|Q,Z)
+ d I(Q;R|P,Z) + e I(P;Q|T,Z) + f I(P;T|Q,Z)
+ g I(Q;T|P,Z) + h I(R;T|Z) + i I(R;T|P,Z) >= 0.

Validity follows by applying the unconditioned inequality to each conditional law given Z and averaging. Here P,Q,R,T,Z can be disjoint groups selected from the full thirteen variables. Expand the nine CMIs into entropy terms and apply Section 1 to each term. The resulting linear inequality on the old functional coordinates is valid for every actual binary-plane law.

## 3. Admission and arithmetic boundary

The discovery scan used only coefficient tuples marked `valid_exact` in the byte-pinned re-derivation receipts:

- `frontier-20261029-dfz-inequality-verify-result.json`, SHA-256 `12f6aa96a6ec70ee6622e4d6981d98d3e3d89ff717f061c137d8c1e52699a727`;
- `frontier-20261029-dfz-inequality-verify-base-used.json`, SHA-256 `206f4a17575c632b3185030d2c58dd9c6bc47c098a93961eb6d827afa27434e5`;
- `frontier-20261029-dfz-inequality-verify-v9b.json`, SHA-256 `614fda6760c476ff15330dc489dbb463930261808740c708cbcefb1048a574e5`.

Their source is the pinned DFZ TeX `frontier-20261029-dfz-source/src/nonShannon.tex`, SHA-256 `ab01cd4113f334715d6e80b538bfcca657d659380504be916de2bd43857e732c`. Their exact copy-lemma derivation checker is `frontier-20261029-dfz-inequality-verify.py` (SHA-256 `c2db2bad5be6e747b30abce3e9abb46f83b2b49703dc5e976cfa7ca70b44e650`).

The first solve will use only the Zhang-Yeung tuple (1,2,1,1,1,0,0,1,0); more admitted tuples remain available if needed. Each independent certificate checker must reconstruct the nine CMIs, validate disjoint masks and thirteen-variable scope, perform the coordinate substitution independently, and reject a tuple without its exact receipt.

Only an exact nonnegative-row/sign-correct identity for 3*Delta carries an exclusion claim. A negative DFZ value at a rational relaxation countermodel is merely a separator. Scientific review, formalization and novelty clearance remain unperformed.
