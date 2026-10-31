# A tuple-coupling obstruction for the fixed pair-augmented primal

**Status: WRITTEN with a separately checked exact five-row Shannon identity.** This is an additive correction to `frontier-20261028-pair-augmented-lp-optimum-v1.md` (SHA-256 `eadb8a7e167e6895c191c367fbaf883cc56808a78dfcb9b870ba7439568ce1ea`). The exact optimum of the specified pair-augmented LP remains `1847/276`. The new conclusion concerns its **particular fixed primal assignment**, not the original-variable base with alternate auxiliaries/pair values.

## Exact identity

Let `X=(a,b,c,d,e,f,g,h,i,j)`, `D=d'1`, `G=g'2` and `F=f'3`. The separately checked identity is

\[
\begin{aligned}
&I(e;G\mid a,b,c,d,f,g,i,j,D,F)
+I(g;F\mid a,b,c,d,f,i,j,D,G)\\
&\quad+I(h;D\mid a,b,c,d,e,f,g,i,j,G,F)
+I(D;G\mid a,b,c,d,f,i,j,F)\\
&\quad-I(D,G;F\mid X)
=-\frac{1086281}{69000000}
\end{aligned}
\]

when evaluated on the **fixed** pair-augmented primal marginals. The four positive terms are elementary CMIs; all entropy terms involving the full triple `(D,G,F)` cancel algebraically, leaving 12 entropy coordinates from `(X,D,G)`, `(X,D,F)`, `(X,G,F)`, `(X,F)` and `X`. Consequently every Shannon-polymatroid extension of these fixed marginals must satisfy

\[
I(D,G;F\mid X)\ge \frac{1086281}{69000000}>0.
\]

In particular, these fixed marginals cannot be extended with the additional tuple equality `I(D,G;F|X)=0`. The pair-augmented LP imposed only the weaker individual equalities `I(D;F|X)=I(G;F|X)=0`, so its exact feasibility/optimality is not contradicted.

## Non-entropicity of this fixed primal

Suppose one finite joint distribution realized all fixed star and pair marginals. Its checked pair equalities give

\[
P(D,F\mid X)=P(D\mid X)P(F\mid X),\qquad
P(G,F\mid X)=P(G\mid X)P(F\mid X).
\]

Recouple to `Q=P(X)P(D,G|X)P(F|X)`. This preserves the full distributions of `(X,D,G)`, `(X,F)`, `(X,D,F)` and `(X,G,F)` because the two original pair conditionals factor; hence it preserves all 12 entropy coordinates in the identity. Under `Q`, `I(D,G;F|X)=0`, contradicting nonnegativity of the four CMIs. Thus the particular fixed pair-augmented primal is not the marginal entropy profile of any single finite joint law, even up to positive scaling.

This conditional recoupling argument does **not** here establish separation from the almost-entropic closure. It does not exclude the original 1,023-coordinate base profile with different star/pair marginals, nor does it establish a tighter upper bound for the pair LP or the full 17-variable LP. The old source/star point corrections retain their own scopes.

## Evidence

* Farkas proposer `frontier-20261028-cross-triple-farkas.py` SHA-256 `d208571a7c60af31eed44878e6e048bb82e9ea5bf3882b3aae0286c269d1160e`; ray receipt SHA-256 `a63d738fed78255bdf59c4df54f4e71d60eff2fb30aafdfa0975b97b976bc96a`. Floating dual extraction only proposed the five rows; the integer/Fraction identity is the proof evidence.
* Separate verifier `frontier-20261028-cross-triple-farkas-independent-check.py` SHA-256 `44ce4353808be67852cdf2047a03c2c478747781ede4286729d357cf1f537d3d`; receipt SHA-256 `804f5a130264ea346f7054d6b9a15f7a455a0028bf0ac19ad3ac2a579e2cd6c7`. It reconstructs all four CMIs and the tuple independence, checks signs and exact cancellation/value, binds both independently checked pair candidates and rejects five intended mutations.
* The pair-augmented exact LP binder is `frontier-20261028-pair-augmented-lp-binding-result.json` SHA-256 `f42c65d0e0c41e5df086d11ff17e347547e57bab4f3756153e62db33af5b66cc`; the nine independent pair-system checks are recorded in SHA-256 `143db08d3ce5caf8e2f764473d0eb2fe5ce4f14a760e95df33b47903a4fc4540`.

No cross-model review, proof-assistant formalization or novelty clearance was performed. Different fixed pair marginals, new copy structures, and the actual guessing-number target remain open.
