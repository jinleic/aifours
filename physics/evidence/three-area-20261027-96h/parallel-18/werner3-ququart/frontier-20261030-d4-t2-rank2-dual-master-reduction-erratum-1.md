# Erratum 1 to the rank-two dual master reduction (consolidated)

**Status: WRITTEN, additive consolidated erratum, UNREVIEWED.** Original `frontier-20261030-d4-t2-rank2-dual-master-reduction-v1.md` SHA-256 `c9003960e860eeab8a2153a94ad70843cbe2b6f50f5d2fda86c87fd89f8c90f4` is preserved byte-unchanged. Item 1 is a load-bearing MAJOR found by the parent's complete read; items 2–4 are accuracy fixes. No new mathematics beyond the corrections, no probes, no execution. Exact-rational verification of the rearrangements used `fractions.Fraction` only (no floats, no solver).

## 1. MAJOR: signs reversed in condition (2.2)

Identity (2.1) is exact and retained: `q(R)=||R||²+B−4P+2s1s2·Re C12`, with `P=s1²p1+s2²p2`. The condition `q(R)≤2||R||²` is therefore EXACTLY

**`2 s1 s2 Re C12 ≤ ||R||² − B + 4P`.**  (2.2′)

The published (2.2) had `||R||²+B−4P` — signs of both `B` and `P` reversed. All readings of the core inequality must use (2.2′); nothing downstream was frozen against (2.2). Note (2.2′) is MORE restrictive when `B>0` and less when `P>0`. Unaffected: (2.1) itself; Lemma `B≥0`; the `C12=0` paid region (proved from (2.1) directly as `q≤||R||²+B≤2||R||²`); §5's structural obstruction (it concerns bounding `C12` at all, not the bound's size).

## 2. Quantifier precision in §1

The sentence "T2 holds for a pair iff `q(R)≤2||R||²` for its maximizing R" is NOT a fixed-pair equivalence; `q(R)` is a supremum over ALL traceless source pairs and can exceed the value at the given pair. The valid statement exchanges two universal suprema. Precisely, both (T2) and (Q) are equivalent to the single joint universal

`|⟨Tr_B R,A⟩_F+⟨Tr_A R,B⟩_F|² ≤ 2(||A||_F²+||B||_F²)||R||_F²` for ALL traceless `A,B` and ALL `rank R≤2`.  (∗)

(T2)⇒(∗): instantiate (T2) at each pair with its Ky Fan optimizer. (∗)⇒(Q): fix `R`, take `A,B` traceless and parallel to `(Tr_B R)_0,(Tr_A R)_0` scaled to `||A||²+||B||²=1`, giving `q(R)≤2||R||²`. (Q)⇒(T2): for each pair and each unit rank≤2 `R`, Cauchy–Schwarz over the traceless source bounds the pairing by `√(2L)·√(q(R))≤√(2L)·√(2)||R||`, then Ky Fan.

## 3. Uniformity remark: no division by zero

For factor dimension `d<4` the per-factor scalar weight is `w_d=8d/(4−d)`, and `2/w_d−1/d=−1/4` identically. A dimension-4 factor has NO complementary block: its scalar sector is zero (equivalently its scalar weight is infinite, contributing `0` to `2/w_d`). With this zero-scalar-sector convention,

`Σ_factors (2/w_d − 1/d) = −1/2` identically for every support `(m,n)≤(4,4)`, `mn≥2`,

which is the exact statement behind the uniform q; the `m=n=4` case carries no weight at all and is proved directly in §1. Verified by exact rational arithmetic for (2,2),(2,3),(3,3),(2,4),(3,4).

## 4. The remaining core is CONDITIONAL on unreviewed antecedents

The §4 conclusion — any violation of (Q) requires rank 2, `Tr R≠0`, non-EP, `C12≠0`, both local supports ≥3 — holds only if the following named UNREVIEWED written antecedents are correct, and they are not paid or adopted:

1. Traceless rank-two dual (hollow nuclear decomposition): `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261029-d4-t2-traceless-dual-strict-chiral-consolidated-v2.md`, SHA-256 `b96fcf9f42e0762132d7b843149f424fcde28bd978439b144f3196e09e34efb5`, §2–§3.
2. EP cross-purity sublemma (`r=Tr[ρ_A(u)ρ_A(v)]+Tr[ρ_B(u)ρ_B(v)]∈[0,1]` for orthonormal `u,v`, currently asserted via the local antisymmetric-swap identity and flagged for review attention): `frontier-20261029-d4-t2-local-2x3-rank2-partial-trace-equivalence-v1.md`, SHA-256 `4bb8a5de4e53d0de78cc3df4a12b816aaf36e6a069b173f83edf9b9160f602d2`, §4.
3. Local-support-dimension-2 block identity (first queued review): `frontier-20261029-d4-t2-qubit-side-test-projectors-complete-v1.md`, SHA-256 `ce6a62889b044e898525b3478d78d227f0e3dc0686a087a396f7d3f6d8bcd02c`, §2.

Corrected core statement: IF antecedents 1–3 stand, then any (Q)-violation lies in the core, and by (2.2′) it must satisfy `2s1s2·Re C12 > ||R||²−B+4P`. No core member is asserted to exist; nothing here is paid, adopted, or kernel/human/independent-family verified.

## 5. Nonclaims

All prior nonclaims stand. This erratum corrects the master reduction only; it grants no unrestricted T2/T3/Z2/q3, no f274 `η>2L` or physical counterexample, no execution or selected parameter, and no novelty. The quarantined cross-term episode remains HELD/ZERO/NONINPUT and unused.
