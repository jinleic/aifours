# A nonorthodox Q2 subclass from Dombi's straight locally inverse theorem

**Status: SOURCE-SUPPORTED WRITTEN DEDUCTION plus exact finite kernel control; unreviewed/unadopted.** This is not a new theorem attributed to us. The cited paper's abstract states the load-bearing theorem; its full text was not available at the institutional repository and has not been independently reconstructed. The result concerns a specific natural generalization of printed Fact2, not all of Q2 or Q1.

## 1. The source and the resulting subclass

Erzsébet Dombi, *Almost factorisable straight locally inverse semigroups*, Acta Scientiarum Mathematicarum 69 (2003), 569–589, institutional metadata and author abstract: <https://strathprints.strath.ac.uk/43425/>. The abstract explicitly states:

> every straight locally inverse semigroup can be obtained as a subsemigroup of an idempotent separating homomorphic image of a Pastijn product of a semilattice by a completely simple semigroup.

The full text is marked unavailable at that repository. We import the displayed assertion at precisely that scope and do not claim to have checked its proof. For the definition of straight/right-straight/left-straight, and the Pastijn product formula, see M. B. Szendrei's 2019 public survey, §5.2: <https://arxiv.org/html/1909.05280v1>. That source defines the product using a normal band N and `D=M[G;I,Λ;P]` as

`(a,(i,g,λ))(b,(j,h,μ))=(a(gP_(λ,j)·b),(i,gP_(λ,j)h,μ))`,

which is exactly the explicit physical product P(N,D) used in this run. Every semilattice is seminormal, so Dombi's theorem yields the natural generalized Q2 target: **every straight locally inverse S embeds in an idempotent-separating homomorphic image of P(B,D), with B seminormal and D completely simple.** No weak E-unitarity hypothesis is imposed. This is an imported published result, not novelty.

The straight condition cannot be dropped on the strength of this abstract. Nor does the theorem assert that S itself embeds into the Pastijn product. The image's quotient map need not split and need not preserve the original actor. Do not read it as an all-locally-inverse, all-locally-r, or general regular-semigroup theorem.

## 2. An explicit nonorthodox member and strict group-actor distinction

Let `D=M[C₂;{0,1},{0,1};P]`, with C₂ written additively in bits and `P_(λ,i)=λi`. Thus

`(i,g,λ)(j,h,μ)=(i,g+λj+h,μ)` mod 2.

D is completely simple. Each cell `D_(i,λ)={(i,g,λ):g∈C₂}` is a two-element group, with identity `e_(i,λ)=(i,iλ,λ)`; the cells form a rectangular band of subsemigroups, idempotents in a fixed row form a right-zero band, and idempotents in a fixed column form a left-zero band. Also every local monoid is a group (`e_(i,λ) D e_(i,λ)=D_(i,λ)`). Thus, by the survey's right/left-straight criterion, D is straight locally inverse.

D is not orthodox: `e=(0,0,0)` and `f=(1,1,1)` are idempotents but `ef=(0,1,1)` is not idempotent: `(ef)²=(0,0,1)`. It has the Q2 target trivially by choosing the one-element semilattice, the actor D itself, and the identity quotient. This example illustrates nonorthodox scope independently of Dombi's imported theorem; it does not test the general source claim.

The exact integer-bit checker `frontier-20261028-straight-cs-q2-control-v1.py`, SHA-256 `cabe520d7ee4fe6351a7336ddf83b727c16c1843671b9eb22804c4eed98543d3`, was executed in the Python eval kernel before Wed Oct 28 21:16:25 PDT 2026. It checked all 512 associativity triples, all 4 idempotents, all 4 cell group laws and corners, row/column zero-band laws, and the stated product/square. This finite check is not a proof of Dombi's infinite theorem.

Separately, `frontier-20261028-orthodox-q2-band-variety-characterization-v1.md`, SHA-256 `3ce438c1814af2211eb0f5927730bf27c32fe1c6c76038c5c14a7751caf7e375`, proves that any regular subsemigroup of any homomorphic image of a band-by-group product is orthodox. Thus the above D cannot be accommodated by such a group-actor image even if idempotent separation is dropped. The need for a completely simple actor here is genuine.

## 3. Union and remaining gap

Subject to independent source checking, Dombi gives the straight locally inverse subclass including nonorthodox examples. A separate conditional deduction from Hartmann's unpublished dissertation §5 would give **all orthodox locally-r** S for the same seminormal-by-CS image target (with a group actor), assuming the independently unreviewed local-regular-band/SN equality. Hence those two classes' union is a rigorously specified proposed Q2 subclass, with no weak E-unitarity hypothesis.

Neither of the sources covers every nonorthodox locally r-orthodox semigroup. The earlier author candidate `frontier-20261028-generalized-fact2-local-r-upper-bound-v1.md`, SHA `d7bab22d7c6f0ea6e6984a2c0d868aa430d0a436e54777470bb816615cd79baf`, supplies a proposed necessary local-r condition for the CS-actor target, not its sufficiency. An independent review must verify the imported Dombi theorem from full paper if available, the identification of product conventions, and the original source's exact scope. No independent review or novelty clearance has yet occurred.
