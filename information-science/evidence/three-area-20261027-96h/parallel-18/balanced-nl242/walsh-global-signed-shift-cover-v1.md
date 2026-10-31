# info-6: every nonzero shift has both signs in the same actual Walsh support

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Actual `/bin/date` observed before this write: **2026-10-27T14:55:35-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** This is a uniform necessary phase-support obstruction conditional on an original balanced peak≤28 object, not an existence or global exclusion result. No scientific program, chosen-state/direction probe, rank selection, formal/kernel or novelty claim.

## Claim

Suppose an original balanced Boolean f exists with scaled spectrum k=W_f/4, |k|≤7, and write S={a:k(a)≠0}. For any nonzero shift b, consider unordered pairs {a,a+b} contained in S. Call a pair positive if k(a)k(a+b)>0 and negative if it is <0. Both signs occur, with the following stronger simultaneous lower bounds:

- If T:=Σ_{x:f(x)=1}x=0, then **at least 20 positive and 20 negative pairs for every b≠0**.
- If T≠0 and b·T=0, then **at least 3 of each sign for every such b≠0**.
- If T≠0 and b·T=1, then **at least 5 of each sign for every such b**.

All T and b are universally quantified; the three bullets are an exhaustive parity dichotomy, not selected test states. In particular every nonzero shift is simultaneously a difference of two nonzero coefficients of the same sign and of opposite signs.

## Proof

The definition-first caller gives k(0)=0 and

    Σ_a k(a)²=2¹⁴,      Σ_a k(a)k(a+b)=0   (b≠0).                (1)

The same balanced Boolean object also gives k(a) mod 2=a·T. If s=|S|, then for b≠0 the number m_b of unordered nonzero-support pairs obeys

    m_b=|S∩(S+b)|/2 ≥ s−256.                                     (2)

Let p_b,n_b be the positive and negative pair counts. Equation (1) gives equal total absolute product on the two signs. If every nonzero product in a case has magnitude between L and U, then

    p_b≥m_b/(1+U/L),       n_b≥m_b/(1+U/L).                      (3)

Indeed Lp_b≤Un_b and Ln_b≤Up_b. These are exact all-pair consequences, not a choice of signs.

If T=0, every nonzero k is even and has |k|≤6. Energy forces 36s≥2¹⁴, hence s≥456 and m_b≥200. Products range from 4 to 36, so (3) gives p_b,n_b≥20.

If T≠0, exactly 256 odd coefficients are nonzero. Their energy is at most 256·49; the remaining energy forces at least 107 nonzero even coefficients because each has square at most 36. Thus s≥363. If b·T=1, every nonzero pair has one odd and one even coefficient, so m_b≥107 and products have magnitudes between 2 and 42. Equation (3) gives p_b,n_b≥5. If b·T=0 and b≠0, the entire 256-point odd hyperplane is paired within itself, giving m_b≥128; products lie between 1 and 49, so (3) gives p_b,n_b≥3. ∎

## Exact consequence and remaining gap

If P={a:k(a)>0} and N={a:k(a)<0}, the claim in particular gives every b≠0 at least one representation in P+N and at least one representation using two members of P or two members of N, with the stated multiplicities. This is a phase constraint on one actual 512-frequency array, not a necessary condition on independently chosen unsigned marginals. No candidate support or b was generated or tested, and the bounds are not asserted sharp.

The proof uses only the S1 supplied definitions and the actual-object autocorrelation/parity facts derived in `prerequisite-derivation-v1.md`, SHA-256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF; all inequalities above are written consequences for the entire quantified family. The original target still needs an actual balanced peak-28 function or an obstruction covering **all** arrays. No old candidate or held guidance is an input; source/book equivalence, independent full-scope review, human, formal/kernel, executable and novelty gates remain unperformed. All S1 STOP/HOLD/ZERO, N4 UNKNOWN and aux214 STOP remain binding.
