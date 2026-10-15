**Verdict: the necessary lemma, exact-UNSAT lower bound, and unrestricted maximum-contrast equivalence are sound. The equality-at-minimum-expansion claim needs an explicit witness size.**

1. **Pointwise lemma.** Privacy supplies a white \(N\) matching each black \(M\) on \(F\); \(N\) may depend on \(M,F\). Worst-case separation applies to every black–white pair, so your proof is valid. For \(F\subseteq Q\),
   \[
   W_Q(M)-W_F(M)=
   \sum_{\substack{T\cap Q\ne\varnothing\\T\cap F=\varnothing}}b_T.
   \]
   Thus exact integer UNSAT with \(\sum_Tb_T\le M_0-1\) and gap \(1\) excludes every strong collection scheme below \(M_0\). The query must cover all relevant \(Q,F\) and support types, unless omissions are proved harmless. SAT supplies only necessary counts.

2. **Divisibility.** Define the actual worst-case gap
   \[
   \Delta=\min_Q\left(\min_{M\in C_1}W_Q(M)-\max_{N\in C_0}W_Q(N)\right)\in\mathbb Z.
   \]
   With normalized contrast \(\alpha=\Delta/m\), attainment of \(\alpha^*=p/q\) gives \(q\Delta=pm\), hence \(q\mid m\). Consequently,
   \[
   m_{\alpha^*}\ge q\lceil L/q\rceil.
   \]
   **Exact fix:** equality requires a valid witness with expansion **exactly** \(q\lceil L/q\rceil\) and contrast \(\alpha^*\). A witness merely attaining optimal contrast at a larger expansion proves only an upper bound.

3. **Basis equivalence.** Interpret a basis as a pair whose forbidden projected-column histograms match, used with uniform column permutations. Repeat the multisets to equal cardinality \(k\), then concatenate:
   \[
   m'=km,\qquad \Delta_{\mathrm{basis}}\ge k\Delta_{\mathrm{collection}}.
   \]
   Privacy gives matching histograms; uniform permutations give identical entire forbidden-row distributions. Conversely, all permutations of a valid basis form a strong collection scheme. Therefore unrestricted maximum contrast agrees, but this construction does not establish equality of minima at fixed expansion.

4. **Expected contrast is materially different.** With \(m=1\), let \(C_0=\{00,11\}\), \(C_1=\{01,10\}\), viewing each string as one two-row column. Singleton privacy holds, expected contrast is \(1/2\), and worst-case gap is \(0\). Thus denominator \(2\) does not divide expansion \(1\). Repeating columns three times also gives expected gap \(3/2\ge1\) while violating the pointwise gap-\(1\) lemma. Neither pointwise necessity nor divisibility follows from expected separation alone.

These arguments assume nonempty collections, uniform multiset sampling, and a common expansion. Finite tables and per-instance ILP certificates do not resolve optimization over arbitrary access structures without a general theorem or a proved exhaustive reduction. They imply neither computational hardness nor novelty.