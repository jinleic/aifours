# info-6: an all-frequency 2-adic moment hierarchy and a bounded Z/16 interface

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Actual `/bin/date` observed before this write: **2026-10-27T14:44:42-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** This continues the exact same S1 definition-first scope; it is not a witness, unrestricted exclusion, numerical bound, formal/kernel or novelty result. No scientific program, selected-state probe or external-model review was used.

## 1. Setup and elementary identity

Use only the S1 definition packet and the actual-object caller proved from it in `prerequisite-derivation-v1.md`, SHA-256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF. In particular V=F₂⁹, M={x:f(x)=1}, |M|=256 for a balanced object, χ_a(x)=(-1)^{a·x}, n(a)=Σ_{x∈M}1_{a·x=1}, and

    k(a)=128·1_{a=0}−128+n(a).                                  (1)

All sums below are over the **same actual M**. For arbitrary bits u_i, the exact integer identity

    1_{⊕_i u_i=1} = [1−∏_i(1−2u_i)]/2
                  = Σ_{∅≠I} (-2)^{|I|−1} ∏_{i∈I}u_i             (2)

follows by expansion. No external source, case selection or old proof body is used.

## 2. All-variable moment hierarchy

Fix any basis of V and define M_I=Σ_{x∈M}∏_{i∈I}x_i for nonempty I. For every integer r with 1≤r≤7, (1)–(2) imply simultaneously for **all** frequencies a

    k(a) ≡ Σ_{1≤|I|≤r} (-2)^{|I|−1} M_I ∏_{i∈I}a_i
           (mod 2^r).                                             (3)

The 128 correction, including its zero-frequency delta, vanishes modulo 2^r throughout this range. A coefficient attached to degree d is therefore divisible by 2^{d−1}, and its remaining residue comes from the very same M. The r=2 instance is the previous mod-4 coupling; r=4 gives the quartic mod-16 interface below.

There is also a basis-free all-increment form. With Δ_h k(a)=k(a+h)−k(a), every d≥1 satisfies the exact identity

    Δ_{h₁}⋯Δ_{h_d} k(a)
      = 128·Δ_{h₁}⋯Δ_{h_d}1_{a=0}
        +(-1)^{d+1}2^{d−1} Σ_{x∈M : h_j·x=1 for every j}χ_a(x). (4)

It follows for 1≤d≤8 that Δ_{h₁}⋯Δ_{h_d}k(a) is divisible by 2^{d−1}. In particular

    Δ_{h₁}⋯Δ_{h_{r+1}}k(a) ≡ 0 (mod 2^r),   1≤r≤7,              (5)

for every a and every ordered tuple of increments, including zero, repeated, dependent or inconsistent ones. The delta term in (4) is retained, so no exception at a=0 or a cube containing zero is hidden. Some degenerate choices make an identity tautological; no selected choice is used as evidence. ∎

## 3. A full bounded Z/16 caller

Under the original peak bound, |k(a)|≤7. Therefore q(a):=k(a) mod 16 never equals 8, and every other residue has a **unique** representative κ(q(a)) in {−7,…,7}. By (3) with r=4, every original witness has the all-frequency form

    q(a) ≡ Σ_i M_i a_i − 2Σ_{i<j}M_ij a_i a_j
            +4Σ_{i<j<l}M_ijl a_i a_j a_l
            −8Σ_{i<j<l<m}M_ijlm a_i a_j a_l a_m       (mod 16).  (6)

This is a common weighted polynomial interface, not four independent marginal choices; for a genuine witness its coefficients are moments of one M.

Conversely, an actual balanced NL≥242 object exists **if and only if** there is a q:V→Z/16 satisfying all of the following, without restricting ranks or residue types:

1. q has the weighted form (6) for some integer coefficients, q(0)=0, and q(a)≠8 for every a;
2. its unique centred lift κ(q(a)) satisfies the **full** integer shift equations (4) of `prerequisite-derivation-v1.md` for every b∈V.

For the forward direction use (3)–(6). For the converse, condition 2 produces all 512 actual Boolean inverse signs by the explicitly proved caller in the previous file; condition 1 gives the bound and zero frequency. The q-coefficients need not be presumed moment-realizable in the converse: if condition 2 holds, the recovered Boolean object supplies its own moments. Conversely, **the polynomial/avoidance conditions without the full shift equations are not claimed sufficient**. ∎

## 4. What this changes and what remains

Equations (3)–(5) are universal coupling obstructions beyond independent feasible spectral marginals: any proposed original-object array violating one is impossible, with every increment quantified. The bounded q representation preserves all 512 frequencies and the actual Boolean caller; it does not replace them by an unconstrained polynomial relaxation. No selected test, arbitrary-rank exclusion, witness or improved original bound has been obtained.

The precise missing step is to establish or refute existence of **one common** weighted q avoiding 8 whose centred lift simultaneously satisfies every shift equation; no statement that a marginally feasible q exists or fails is made. Full-scope written review, source/book equivalence, formal/kernel, executable, human and novelty gates remain separate and unperformed. S1's old proof/method/source NONINPUTs, prior exposure, HOLD, all ZERO/STOP findings, N4 UNKNOWN and aux214 STOP remain binding.
