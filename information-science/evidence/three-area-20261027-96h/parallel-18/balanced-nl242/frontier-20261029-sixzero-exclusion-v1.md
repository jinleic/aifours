# Six Walsh zeros are impossible (v1)

**UNREVIEWED AUTHOR CANDIDATE.** This is a conditional written argument with an exhaustive computational confirmation. It is not a witness, not a global NL242 theorem, not formal, and makes no novelty claim. Native clock before composing: 2026-10-29T08:32:32-0700.

## Statement

**Theorem.** Let `f:F₂⁹→{0,1}` be balanced with `max|W_f|≤28`, `k=W_f/4`, `Z={a: k(a)=0}`. Then `|Z|≠6`.

Together with the four-zero exclusion `frontier-20261029-fourzero-block-energy-exclusion-v1.md` (SHA-256 `9227c8fd…cfb`, unreviewed), every target function has `|Z|≥8`.

**Imported inputs.** These are the adopted same-harness dispositions f131/f152 and the reconstruction in f131:

- **Basic facts.** `T≠0`; `Z⊂K=T^⊥` with `0∈Z`; `|Z|` is even. If `rank B≤4`, then `|Z|≥8`.
- **(Deg)** Under the peak bound `Z=Z₈:={a∈K: k≡0 (mod 8)}`, and `1_Z` has degree at most 6 on K. Hence `⊕Z=0`.
- **(P) Coset-parity tool.** Let `L⊂K` be 5-dimensional with `rank(B|L)≤2`. Then `|A∩Z| mod 2` is constant over the eight cosets A of L in K.

  This follows from f131's `Σ_A k² ≡ 16[wt(q|A)/4+|A∩Z₈|] (mod 32)`, which is constant over cosets. When the restricted polar rank is at most 2, every `wt(q|A)` is divisible by 8.

Since `|Z|=6<8`, constant odd parity is impossible. So under (P), **every coset of every admissible L contains an even number of zeros.** By the basic facts, only `rank B∈{6,8}` remains.

## Rank 8

**Admissible L.** For nondegenerate B, `rank(B|L)=2` exactly when `D:=L^{⊥_B}` is a 3-dimensional totally isotropic subspace. The cosets of L correspond to the values of `z↦B(z,·)|_D∈D*`. Evenness therefore gives `Σ_{z∈Z} B(z,x)B(z,y) ≡ 0` for all `x,y∈D`.

**The form G.** Every isotropic pair lies in some isotropic 3-space, so the form `G(x,y)=Σ_z B(z,x)B(z,y)` vanishes whenever `B(x,y)=0`. Fix `x≠0`: `G(x,·)` vanishes on the hyperplane `x^{⊥_B}`, so `G(x,·)=c(x)B(x,·)`. Linearity in x forces c to be constant, so `G=cB`.

**G is zero.** The vectors `w_z=B(z,·)` are six distinct vectors, including 0, with sum `B(⊕Z,·)=0`. They span at most 4 dimensions, so `rank G≤4<8`, hence `c=0`.

**Contradiction.** Let W' be the full-row-rank coordinate matrix of the `w_z`, of size d×6. Then `W'W'ᵀ=0`, so the row space of W' is a self-orthogonal binary code of length 6 and `d≤3`. The six columns of W' would then be six distinct vectors of `F₂^d`, including 0, with zero sum. For `d=3`, the two omitted vectors `u≠v` force the sum to be `u+v≠0`. For `d≤2`, there are fewer than six vectors. ∎

## Rank 6

Let `R=rad B`, which is 2-dimensional, and `V=K/R`, which is 6-dimensional symplectic. Write `K=R⊕M`.

**(F1) Fibre evenness.** Take any 3-dimensional `L̄⊂V` and set `L=R+L̃`. Then `rank(B|L)=rank(B̄|L̄)≤2`, so the image multiset `Z̄` of Z in V has even weight on every coset of every 3-space. The mod-2 multiplicity function of `Z̄` is therefore orthogonal to RM(3,6), i.e. it lies in RM(2,6). Its weight is at most 6 < 16, so it is 0. **Every R-fibre contains an even number of zeros.**

**(F2) Split cosets.** For `r∈R∖0` and a 4-dimensional `L̄=U^⊥`, with U an isotropic 2-plane of V, put `L=⟨r⟩⊕L̃`. This L is admissible: `rank(B|L)=4−2=2`. Its cosets are labelled by `(ρ mod r, s mod L̄)∈F₂×F₂²`, for `a=(ρ,s)`. A zero pair `{p,p+d}` in one fibre is split between the two labels `t=0,1` exactly when `d≠r`.

**Case analysis.** By F1 the fibre counts are `(2,2,2)`, `(2,4)` or `(4,2)`; the first entry is the fibre R, which contains 0.

- **Patterns with a full fibre.** Choose `r≠d` for the single pair. That pair contributes one point to each of `(0,ȳ)` and `(1,ȳ)`. The full fibre contributes two points per label, and the other two R-fibres contribute nothing. Some label is therefore odd, contradicting evenness.
- **Three pairs with differences `d₀,d₁,d₂`.**
  - If the `d_i` take at most two values, choose r outside them. All three pairs split, so the label `(t,ȳ)` receives `#{i: ȳ_i=ȳ}` points. Three such values cannot all have even multiplicity.
  - If `{d₀,d₁,d₂}=R∖0`, take `r=d₀`. Evenness forces `ȳ₁=ȳ₂`, i.e. `s₁+s₂∈L̄`. Pick `u₁` with `B̄(u₁,s₁+s₂)=1` and any `u₂∈u₁^⊥∖⟨u₁⟩`. Then `L̄=⟨u₁,u₂⟩^⊥` avoids `s₁+s₂`, a contradiction. ∎

No assumption on whether q vanishes on R was used.

## Exhaustive confirmation (same necessary condition, all six-sets)

`frontier-20261029-sixzero-parity-exhaust.cpp` (SHA-256 `acef315f1a6f3c260f73f17aad9c5bb13fe1680150da020aa78bfde38534cd8a`, 80 LF) works as follows:
- It enumerates all 97155 five-dimensional subspaces of `F₂⁸` and keeps those with `rank(B|L)≤2`. This gives 11475 for rank 8 (the number of isotropic 3-spaces) and 16515 for rank 6 (`1395+315·3·16`).
- It tests every six-set `Z∋0` with `⊕Z=0`, 33,732,216 sets in each form.
- **0 survivors** in both forms. The rank-6 run imposes no condition on q.
- Receipts: `frontier-20261029-sixzero-parity-rank8.json` (`8d443b7305a49255d47951164fec621a2b07fb4ddd99fb6647e1870d951c68a9`) and `frontier-20261029-sixzero-parity-rank6-none.json` (`631bbed4b3c7ae51d9e91a7749e69bfc46ff664addb601b1308ed12f63dfd306`).

Normal forms suffice because condition (P) is GL(8)-equivariant in (B,Z).

Independent controls are in `frontier-20261029-sixzero-controls.py` (`9475dbeda3068ed5d74471e7f24c63a532fb3d5370d185bed412692d991ed722`, 119 LF), with result `frontier-20261029-sixzero-controls-result.json` (`7cd7617bc10f6b05ffe8d15c4faf4fbac9d2a2b5088af0074c780276fabba102`):
- **(P) on random functions.** It checks (P) in f131's raw form, `wt(q|A)/4+|A∩Z₈|` constant mod 2, on seeded random balanced Boolean functions: 240 (f,L) pairs, 0 violations.
- **Family sizes.** An independent construction reproduces both family sizes.
- **Non-vacuity.** The radical 2-plane R passes every rank-6 constraint. Each of 2000 random zero-sum six-sets is violated in both forms.

## Scope

The result is conditional on f131/f152 as adopted (same-harness), in particular on (P) and (Deg) as stated in the f131 reconstruction.

Not covered:
- `|Z|≥8` remains open.
- The four-zero exclusion is a separate, unreviewed candidate.

Not performed: independent review, human check, formal proof.
