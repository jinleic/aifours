# Addendum 1 to the T2 packet v2: exact block identity, trace-sign criterion, split identity

**PhysicsResearch96h-2 / physics-1. WRITTEN, source-independent, all-variable; UNREVIEWED.** This addendum is additive to `frontier-20261029-d4-t2-two-copy-obligation-packet-v2.md` (SHA256 `022049e48a2c0e3c7fa96235fc049d633ffeee5478e9be5cedac910459a23423`). That packet is unchanged.

It does not prove T2, Z2 or the original target. It makes no literature-status, novelty, review or acceptance claim, and no f153/f62/f168 scope change. No explicit operator is evaluated, and no held input or guidance is used.

## 1. Exact block identity

Let C be any operator on C⁴⊗C⁴, and fix any orthonormal basis {e_k} of site 2. Define the site-1 blocks

`C^(kl) = <e_k|C|e_l>_2`, for k,l = 1..4.

The site-2 form `K_2 = I−½|Ω_2><Ω_2|` and `<Ω_2|_2 vec C = vec(Tr_2 C)` give

`q2(C) = Σ_(k,l) q1(C^(kl)) − ½ q1(Tr_2 C)`,                         (1)

where `q1(Y)=||Y||²−½|Tr Y|²`. The sum is basis-independent, since it equals `<vec C,(K_1⊗I)vec C>`. The same identity holds with the two sites exchanged.

## 2. Trace-sign criterion

**Lemma A1.** Let C have rank ≤2. If `q1(Tr_2 C)<=0` or `q1(Tr_1 C)<=0`, then `q2(C)>=0`.

*Proof.* Each block C^(kl) is a contraction of C, so its rank is ≤2, and T1 gives `q1(C^(kl))>=0`. Then (1) gives `q2(C) >= −½q1(Tr_2 C) >= 0`. The other case follows by exchanging the sites. ∎

**Example and scope.** The condition `q1(Y)<=0` means `|Tr Y|²>=2||Y||²`, i.e. Y is close to a scalar. For instance, a range spanned by two orthogonal maximally entangled vectors gives `Tr_2 C` proportional to I. So the lemma applies to some operators in Z2. These particular examples are also covered by the spread criterion, and no new open region beyond the known criteria is claimed.

## 3. Two-plus-two split identity at one site

Let P be any rank-2 orthogonal projection on site 2, `J=2P−I`, and `C_P=(I⊗P)C`. Decompose `Ω_2` into its components inside `P⊗I` and `(I−P)⊗I`, and polarize q1. This gives

`q2(C) = q2(C_P) + q2(C_(I−P)) − ¼ q1(Tr_2 C) + ¼ q1(Tr_2[C(I⊗J)])`.      (2)

If C has rank ≤2, then C_P and C_(I−P) have rank ≤2, and their site-2 output legs lie in 2-dimensional spaces. By v2 Theorem 6 (s=1) with T1, both of the first two terms are ≥0. Hence:

**Corollary A2.** If C has rank ≤2 and there is a balanced reflection J at site 2 with `q1(Tr_2[C(I⊗J)]) >= q1(Tr_2 C)`, then `q2(C)>=0`. The same holds at site 1.

**Haar average.** Averaging J over Haar-random rank-2 P gives

`E[q1(Tr_2[C(I⊗J)])] = −(1/15) q1(Tr_2C) + (4/15) Σ_(k,l) q1(C^(kl))`.

This uses `E[P⊗P]=(7/30)I+(1/15)F` on C⁴⊗C⁴. Together with (1), the average contains no information beyond the identity (1) itself. Corollary A2 is useful only for a well-chosen J, and no general choice is proved to exist.

## 4. What this adds

- T2 holds on the explicitly described trace-sign class of Lemma A1.
- Identity (2) reduces T2 to finding a single balanced reflection J that does not decrease `q1(Tr_2[C(I⊗J)])` relative to `J=I`, whenever the ladder terms alone are insufficient.

The existence of such a J for every rank-2 C is open and is not claimed.
