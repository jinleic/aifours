# One tuple/single cross-branch system still leaves the exact source optimum

**Status: exact rational LP result, separately machine-checked; scientific review pending.** The pre-source erratum `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md` (SHA-256 `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9`) must be read before the f110 source LP packet. The third-cut receipt also requires `frontier-20261028-third-cross-cut-independent-label-erratum-v1.json` (SHA-256 `e6b01fe0362c99ad0a35dff4aea4a16bda7f0586a38144d1110c152913f7ed7a`) before the affected receipt.

Let `X=(a,b,c,d,e,f,g,h,i,j)`, `V=(d'1,e'1,g'2)` and `W=(f'3,g'3,h'4)`. Start with the 11/13/13 publisher LP, the two full 14-variable star Shannon blocks `X,b'0,V` and `X,b'0,W` and their already specified conditional independences, the named cut families in `frontier-20261028-threefamily-extended-optimum-v1.md`, and nine 12-variable pair blocks `X,v,w` for `v` in `V`, `w` in `W`, each with `I(v;w|X)=0`. Add the **full 13-variable Shannon block** `X,d'1,g'2,f'3`, together with

\[
I((d'1,g'2);f'3\mid X)=0.
\]

The specified finite LP still has exact optimum **`1847/276`**. It also retains this optimum after adding the following 42,850,500 explicitly enumerated `Psi` substitutions: `P` and `Q` range over the 7 nonempty subtuples of `V` and `W` respectively; `C,R,H` are nonempty pairwise disjoint original-variable blocks and `Z` is exactly their complement in `X`. The written universality proof of `Psi` is `frontier-20261028-five-variable-gluing-inequality-v1.md` (SHA-256 `ef9cb87907bd255d75f4154a11fe5471072e8959e622376bea6469ad60462df4`); its scientific review is pending. For this LP calculation the substitutions are specified linear constraints regardless of the status of that interpretation.

## Exact primal and bound

The original entropy vector and the two checked star blocks are unchanged. The new tuple system fixes their overlapping marginals `(X,d'1,g'2)` and `(X,f'3)` but reoptimizes all 3,072 remaining cross coordinates. Its two pair projections replace the old pair assignments for `(d'1,f'3)` and `(g'2,f'3)`; the other seven independently checked pair systems remain unchanged. All overlaps are therefore consistent. Its exact check covers all **159,757** elemental Shannon rows, the tuple equality, and both implied pair equalities. Three intended mutations are rejected.

The union has **40,959 nonempty entropy coordinates**. The binder pins the old star and seven pair checks, inserts the tuple coordinates, checks all nine pair equalities and the tuple equality, and checks the publisher's 1,920-row rational dual. The dual gives `h(X) <= 1847/276`, while the assembled rational primal has equality and satisfies all named constraints. The additional tuple-valued `Psi` scan depends only on the unchanged star marginals; two separately written exact integer enumerators both check all **42,850,500** substitutions, with minimum slack 0 and no violation.

The reoptimized point is **not** the earlier fixed pair primal: its pair marginals differ where necessary. The additive fixed-point obstruction in `frontier-20261028-pair-primal-nonentropic-addendum-v1.md` (SHA-256 `acea805d7e3805b87f007e887fd024386f2abb07d15526644312095fc51a4365`) remains valid and is not undone.

## Evidence pins

* Tuple candidate `frontier-20261028-cross-tuple-freepairs-candidate.json` SHA-256 `fc0e45092f735a8d17a7b7b0363b04b716e0a48c70c6a3a9f32d09855d2e76ec`; proposer `frontier-20261028-cross-tuple-freepairs.py` SHA-256 `0b21b1d2edfa1535a1d661d6042947f7a780e6c3dbd1a5cc0cb7547460bebd5c`; proposer receipt SHA-256 `f495bc1eff05252588b92e1f376a3dabdbd472ce85402ff1fc838d51c18d979e`.
* Independent tuple checker `frontier-20261028-cross-tuple-freepairs-independent.py` SHA-256 `c662be563f0c228a140a4612dadf808ce5926eaa4d17cd6fe994b7bcf87e486e`; receipt SHA-256 `ced2fff5c556165aeb2cb42b1e13291e4c08025f47dfc72002edcfb93a781c87`.
* Named LP binder `frontier-20261028-tuple-augmented-lp-binding.py` SHA-256 `7be296e2712de6d7f1a05e2233ebc0bfc6822f1c466bfef2234d952d525505f1`; receipt SHA-256 `e920d22e9e5cc35a3a7a8459f2aa11cd942e910cad3c06739cadfc31f4e4b5bd`.
* Tuple-valued `Psi` scan `frontier-20261028-psi5-cross-tuple-scan.py` SHA-256 `5f9c9c984b4915e7ac8c67eaae26c2bf262d8a6de51ac8fd3bab0b3cf26e9713`, receipt SHA-256 `1ba7883ac69a543af5396ff5c35844230dad97723f4f3eec6772bc8a45218381`; independent 6+4 enumeration `frontier-20261028-psi5-cross-tuple-independent.py` SHA-256 `3b7d6731f0d442ce410aafb8d5348bd724ed7b4eb9e0a6f99290b41d56d8b932`, receipt SHA-256 `6d29446055593884ba46d72743e9bb171fc89bc6a48da0696c6f452517381e8a`.

This is a finite LP optimum only. It is not a joint all-17-variable Shannon extension, an entropy law, an improved guessing-number bound, proof of no strict gain, or a novelty claim. No proof-assistant formalization or cross-model review was performed.
