# f892 author erratum 1 to author-candidate-v1.md (additive; the candidate is not edited)

Self-found on rereading the complete candidate after its exclusive creation. Every item is expository or a scope precision. No statement of Theorem A or Corollary B changes.

**E1 (Section 7, five-party degree list).** Replace "A five-symbol party whose partners all have at most five symbols" with: "A five-symbol party having at least one partner party with at most five E symbols (so all its degrees are at most 5)". Its multiset is then P1, P2, P3 or P4. The extra multiset `P5=(2,2,2,2,6)` needs all three partners to have six symbols. That happens only in profile 5666, which Lemma 7 already excludes. In 4555, 4556, 5555 and 5556 every five-party has a partner with at most five symbols. So the lists used in Sections 8-9 are complete.

**E2 (Lemma 8(iii) scope).** Read "If X is a five-party" as "If X is a five-party with all degrees at most 5 (P1-P4)". This holds wherever the lemma is used (4556, 5556; and 4456 needs only (i)).

**E3 (Lemma 9, P2P2, last subcase).** The parenthetical "`rho=r2` would give r2 link-degree 3" is imprecise. The correct reason follows. If `rho=r2`, then r2's link triangle already contains `{x',x''}` through the rectangle `{x',x''}x{r1,r2}`. So `rho'=r1` and it is the same rectangle. Then `L_{x'}` is `{r1,G},{r2,G},{r1,r2}`, which is a triangle. A degree-4 link cannot contain a triangle (Lemma 4(c)). By symmetry `rho'` is not r1 and not G. If `rho!=rho'` are both new, x' would have five neighbours. Hence `rho=rho'=sigma` is new, as stated. The conclusion is unchanged.

**E4 (Lemma 10, expanded steps).**

*Case `u1=u2=u`.* By Lemma 5, u's rectangles are not doubled, because alpha_i has degree 3. So they are `{u,t1}x{alpha1,alpha2}` and `{u,t2}x{alpha1,alpha2}`. alpha_i's link triangle on `{t1,t2,u}` also contains one rectangle `{t1,t2}x{alpha_i,a_i}`. t1's link is a triangle on `N(t1)={alpha1,alpha2,beta_t1}`. It already has the edge `{alpha1,alpha2}`, so a repeated edge forces `a_1!=alpha2` and `a_2!=alpha1`. Hence `a_1=a_2=beta_t1=:beta`, and beta lies in `N(t2)`.

*Case `u1!=u2`.* `u_i` is not adjacent to alpha_j (j!=i), so `N(u_i)={alpha_i,a_i}`. Its two rectangles are not doubled (Lemma 5) and lie in alpha_i's link triangle. So they are `{u_i,t1}x{alpha_i,a_i}` and `{u_i,t2}x{alpha_i,a_i}`. Then `a_i` lies in `N(t1)∩N(t2)\{alpha_1,alpha_2}`, so `a_i=beta`.

**E5 (Lemma 9 header).** Replace "(X side, Y side; subscripts 2,3,4,5 denote degrees.)" with: "(In each item X is the first party and Y the second; parenthesised numbers are degrees.)".

**E6 (Lemma 5 naming).** "the cut DB|AC" means whichever of the two cuts separating D from A defines R, after naming the other two parties B, C accordingly. The other cut is the same argument with B and C interchanged.

Clock observed before this exclusive write: see the next administrative observation in the final return. No code, eval or scientific execution was used.
