# Additive correction 1: separate polynomial and Chevalley-operator notation

The unchanged candidate `author-independent-grade4-character-and-exact-kernel-v1.md` has SHA-256 `d4a769a2df5e9db7c3b86bc90ae946b65245b65fe314b0c3801bfe4353f54400`. It uses \(H_i=\operatorname{ad}h_i\) for Chevalley operators in §1, but then reuses \(H_j\) in §2 for the different polynomials \(H(X^j,Y^j)\). Although §5 explicitly warns about the \(j=3\) instance, §2 does not resolve the collision. This is a notation error; preserve the original and read it throughout with the following correction.

Write \(\mathscr H_j:=H(X^j,Y^j)\) for the polynomial Adams substitution and reserve \(H_i:=\operatorname{ad}h_i\) exclusively for operators. Thus the degree-four identity and its PBW explanation in §2 use
\[
 C=\tfrac14(H^4-\mathscr H_2^2),\qquad
 \text{degree-two plus degree-one contributions}=\mathscr H_2^2/4.
\]
The phrase “the \((H_1,H_2)\)-weight” in §2 means the pair of **operators** \((\operatorname{ad}h_1,\operatorname{ad}h_2)\), not the polynomial substitutions. In §5 the grade-three character identity means
\[
 \operatorname{ch}S_3=\tfrac13(H^3-\mathscr H_3),
\]
while every statement about an \(H_3\)-weight or \([E_3,F_3]=H_3\) means the **operator** \(\operatorname{ad}h_3\). All quantifiers, computations, named imports, radical exclusions and assurance limits in the original remain unchanged. This additive correction is itself an unreviewed written proposal, not parent acceptance or a scientific execution result.
