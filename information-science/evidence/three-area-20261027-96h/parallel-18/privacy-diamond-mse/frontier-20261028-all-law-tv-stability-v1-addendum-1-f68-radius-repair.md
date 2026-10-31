# Additive f68 correction: diamond radius and privacy-slack terminology

Native clock before this write: `Wed Oct 28 18:15:34 PDT 2026`. This is an additive correction to the immutable `frontier-20261028-all-law-tv-stability-v1.md`, SHA `3f6c2a61738cc92f615e375d88f6dfb10f96b553585b5c8468480a7ec9683f79`, **not** an edit of its frozen bytes or a retroactive favorable verdict.

## 1. Actual review and status

Complete review `institute/runs/three-area-2026-10-27-96h/review-waves/f68-privacy-all-law-tv-stability/review-v1.md`, SHA `901186e44e95fce0456f19ca06a411e5eb1b0f6b83cd7cc01b661d474f830b19`, 152 LF, was read through its true ending. It returns **0 FATAL / 1 MAJOR / 1 MINOR on the candidate as pinned**. M1 is a load-bearing missing citation-to-radius implication, NOT a counterexample. Its §2 supplies the exact direct repair written below; the reviewer conditionally supports the other fixed-epsilon steps at the two named imports. m1 corrects “interior law” to “strictly privacy-slack law.” Parent assessment of this additive repair remains separate; this document does not silently promote the composite to accepted or claim any successor was reviewed.

## 2. Repair M1: why the actual diamond radius is below one

The parent-v241 record says the ACTUAL optimizer core is a full diamond on and below its positive threshold, but its supplied wording does not literally identify its scalar q_* as that core's radius. The LAW642 parent gives a positive core and optimizer, but not the explicit bound `2t_*<1`. I therefore withdraw the original note's attribution of `0<gamma<1` directly to either parent and prove the needed bound from the actual diamond shape and all-law optimality.

Fix any epsilon>0, `b=e^(-epsilon)`, `m=b/(1-b)`, and D the full closed l1 unit diamond. For any a>=0 let

    u_a(x)=b^(min{j>=0:||x||_1<=a+j}),     Q_a=u_a/integral u_a.

Each is genuinely full-D private by the triangle inequality and has finite moments. Write N for a geometric random variable with P(N=j)=(1-b)b^j. The layer identity and exact diamond moments yield

    J(Q_a)= (1/3) E(a+N)^4 / E(a+N)^2.                                  (1)

At a=0, put `T2=m+2m^2`, `T3=m+6m^2+6m^3`, `T4=m+14m^2+36m^3+24m^4`. Exact differentiation and the identity

    2 T3 T2 - m T4 = m^2(1+2m)

give `J'(0)=2/[3(1+2m)]>0`. For powers 1–4, shifting the geometric index gives `E(1+N)^r=E(N^r)/b`, so the same derivative formula gives

    J'(1)=J'(0)=2/[3(1+2m)]>0.                                         (2)

Thus for sufficiently small eta>0, the actual feasible Q_(1-eta) has strictly smaller Euclidean cost than Q_1; radius a=1 cannot be the original optimum.

For any a>1, put v=a-1>0. The exact layer identity is

    u_v = b u_a + (1-b)1_(vD).                                          (3)

After normalization Q_v is a nontrivial mixture of Q_a and the uniform law on vD. That uniform's Euclidean squared cost is `v^2/3`. Q_a is a positive mixture of uniform laws on `(a+j)D`, j>=0; each has cost `(a+j)^2/3>v^2/3`. Thus `J(Q_v)<J(Q_a)`, so no diamond radius a>1 can be the original all-law optimum either.

The actual full-diamond core has some radius a>0 by its nonempty interior. Since its canonical density is Q_a and is globally optimal, the two strict competitor arguments force `0<a<1`, hence D is not contained in S. This uses only the named full-law optimum and actual diamond shape, not an identification of the v241 scalar parameter. The original rounded-side proof is unchanged: the separately stated threshold cubic is negative at 1, so above threshold m<1/4, and the strict LAW642 value bound excludes e1=(1,0) by margin >7/24. Therefore the needed D-not-subset-S caller is paid on both sides, including equality at the transition.

An exact integer-polynomial/Fraction check independently produced:

```text
2*T3*T2-m*T4 ascending m coefficients= [0, 0, 1, 2, 0, 0]
equals m^2(1+2m): True
b=1/2: J(1)= 25/3 J(99/100)= 4965453067/596010000 strictly_smaller= True
all-variable Jprime(1)=2/[3(1+2m)], sample= 2/9
```

The selected rational b is a diagnostic only; (1)–(3) and their all-m proof pay the universal correction.

## 3. Correct m1: slack, not topological interior

Where the frozen candidate calls its oscillatory reference “a general feasible interior law,” read **“a feasible strictly privacy-slack law.”** The constructed Laplace reference has density-ratio bound 2 under epsilon=log6 budget 6. No claim of interiority in the ambient weak or TV topology follows.

Indeed, for any feasible law mu, its density is absolutely continuous by the candidate's Tonelli argument. The laws `(1-delta)mu+delta delta_x` approach mu in TV and weakly as delta decreases to 0, but fail full-D privacy: the singleton {x} has mass delta while any nonzero h in D gives `{x}+h` zero mass. Thus this example cannot certify ambient topological interiority; this terminology correction does not alter its valid weak-not-TV counterexample.

## 4. Exact propagation and no automatic promotion

The repaired caller is: **LAW642 full-law optimum/canonical core + v241's actual diamond-versus-rounded shape/threshold + this addendum's elementary radius argument**. The original candidate's subsequent saturated-plateau, local-to-global L1, cost/W2 and lower-modulus conclusions, if used, must be cited together with f68's review and this addendum, not as having already been reviewed after correction. Their parent adoption, if any, is a separate actual decision.

The following already-pinned successors must carry that same corrected TV dependency where applicable; their independent portions retain their own exact author/review states:

- `frontier-20261028-density-topology-cutoff-v1.md`, SHA `bc85de66ffffb540a6f9cb40d415c90f40971820ed37e4d945217b3c0b344d08`: its ALL-sequence finite-Lp/W2 implication imports the corrected TV chain. Its core-boundary Linfinity obstruction and actual smooth exact-epsilon family depend directly on LAW642, not on the missing diamond-radius caller.
- `frontier-20261028-kl-renyi-order-cutoff-v1.md`, SHA `fbd0f94a2668ad8bb3cb86bac5977320031c3b293929b413528cb6acd5cb4e38`: its ALL near-optimizer two-sided KL and alpha<1 results import the corrected TV chain. Its explicit translated-mixture Renyi-alpha>1 counterexample is directly constructed from LAW642 and does not need TV stability.
- `frontier-20261028-staircase-erosion-tv-criterion-v1.md`, SHA `2390d99df92b2a2254cc431a8c849613d0aea478dd00421a10e4ec25dce76758`: its general iff and S=2D counterexample do NOT use the original optimum or the radius caller; only §6's application to the original optimizer imports the repaired D-not-subset-S proof.

The matching-cost-only `frontier-20261028-mean-squared-near-optimal-stability-v1.md`, SHA `d8b3a4618e57b74df934e8a162ed11c2656b7ba8f04de02360df0f8ef61e2ae8`, applies the general erosion theorem to gamma_i D with gamma_i<1 from its own named selector/equality candidates; it does NOT import the original Euclidean TV candidate and is intentionally not marked dependent on M1. It remains unreviewed at its own existing boundaries.

This addendum preserves the f68 MAJOR and MINOR as historical findings. No stronger formal/kernel/human/configured-family, novelty, source-priority, or automatic parent-adoption claim is made.
