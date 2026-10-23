# Pair lemma and conditional diagonal-orbit closure (v1)

Recorded after actual `/bin/date`: 2026-10-19T18:35:08-0700. ContinueRQLS10b. Written only, single author,
unreviewed, not Lean-checked. Uses the proved Lemmas 1-2 of 01-column-reduction-v1.md,
SHA-256 56939f826eef5b26291e4447d8f21299be38f4b88b6184d465863c1ccc8afe2d.
The theorem here is CONDITIONAL on explicit finite identities/inequalities, not yet a closure verdict for family F.
Nothing is executed. The unrestricted target remains OPEN / UNKNOWN.

## 1. Pair lemma
Work in the tilde gauge of note01. Let M be Hermitian and computationally flat, with
  M_(-r,-s)=conj(M_(r,s)).
Write q(t)=M_(t+1,t) and r(t)=M_(t+2,t), and assume q(t)!=0 for every t. Define the triangle invariants
  T(t)=r(t) conj(q(t) q(t+1)).
The symmetry gives q(-t-1)=q(t), r(-t-2)=r(t), so
  (q(t))=(q0,q1,q2,q1,q0), and (T(t))=(a,b,b,a,c).
Assume (F1): Im(a conj(b))!=0.

**Lemma 3 (pair).** Suppose H=E M E^* and H'=E' conj(M) E'^* are flat (in all three bases) for diagonal unitary
E,E', and their first columns are proportional: h'(t)=lambda h(t), |lambda|=1.
Then h(-t-1)=h(t), and the five numbers 1/conj(h(t)h(t+1)) are a common complex scalar times real numbers.

Proof. None of h(t) vanishes because |h(t)|=|q(t)|. Set d_t=1/conj(h(t)h(t+1)). Triangle products are invariant
under diagonal conjugation, so the second columns of H,H' are respectively T(t)d_t and lambda^2 conj(T(t))d_t.
For a tilde-flat second column, the Fourier coefficients at +1 and -1 vanish (note01). Therefore both vectors
  v_+=(d0+d3 zeta^3, d1 zeta+d2 zeta^2, d4 zeta^4),
  v_-=(d0+d3 zeta^(-3), d1 zeta^(-1)+d2 zeta^(-2), d4 zeta^(-4))
are killed by the two rows (a,b,c), (conj(a),conj(b),conj(c)). Their kernel is one complex line, spanned by the real
vector n=(Im(b conj(c)), Im(c conj(a)), Im(a conj(b))); multiplication by a nonzero imaginary scalar gives the cross
product of those two rows. In particular n3!=0 by (F1).
Their third entries give v_-=zeta^2 v_+. The first entries then give
  (1-zeta^2)(d0-d3)=0,
and the second entries give
  (zeta^4-zeta^3)(d1-d2)=0.
Thus d0=d3 and d1=d2. Because n is real and the third entry is nonzero, the ratios of the first/third and
second/third entries of v_+ are real. But
  (1+zeta^3)/zeta^4=zeta+zeta^4, and (zeta+zeta^2)/zeta^4=zeta^2+zeta^3
are nonzero real numbers. Hence d0/d4 and d1/d4 are real; the whole vector d has one phase.
Finally d1=d2 implies h1 h2=h2 h3, so h1=h3; d0=d3 then implies h0 h1=h3 h4, so h0=h4.
This is h(-t-1)=h(t). QED.

## 2. Conditional closure theorem
In addition to (F1), assume M is flat, k!=0 in
  q(t)=k(z_t+z_t^(-1))+b0, z_t=eta zeta^t,
and (F2): q0/q2 is not real. The symmetry and support give that expression exactly by note01.

**Theorem 4.** Under these hypotheses, E M E^* is flat for a diagonal unitary E iff E=lambda Z^c,
c in Z_5, |lambda|=1.

Proof. Let h be its first column. Note01 Lemma2 classifies h, up to a scalar phase.
In its unequal real-coefficient case (B), write h(t)=mu(u z_t+v+w/z_t) with u,v,w real and u!=w.
The parity transform Pi H Pi is flat: in the physical gauge Pi permutes each of the three bases, and Pi commutes
with R. It is a diagonal conjugate of conj(M), since Pi M Pi=conj(M). Its first column is
conj(h(-t-1))=conj(mu)(u z_t+v+w/z_t), proportional to h. Lemma3 forces h(-t-1)=h(t).
The coefficients of z and z^(-1) then agree, u=w, contradiction. This eliminates ALL of case(B), without solving
its real polynomial equations.
In case(A), h is proportional either to q or to conj(q) (z+z^(-1) is real at each z_t).
If h is proportional to conj(q), pair H with H'=conj(M), whose first column is conj(q).
Lemma3 makes d0/d1 real, which here equals a real nonzero scalar times q2/q0: indeed
  d0/d1=conj(h1 h2)/conj(h0 h1)=conj(h2/h0)=q2/q0.
This contradicts (F2); a common phase in h cancels in the displayed ratio. Thus h=mu q.
For the diagonal phases of E, e_(t+1) conj(e_t)=mu at every t. Their product is one, hence mu^5=1, mu=zeta^c.
Recursion gives e_t=e_0 zeta^(ct), which is E=lambda Z^c. Conversely these diagonal conjugations preserve all
three bases up to phases/permutations, so they preserve flatness. QED.

## 3. Obligations for the actual family
For each of the four explicit M_tau, this theorem reduces the frozen closure question to:
(H0) rank2/computational flatness and flatness in X,T;
(H1) nonzero first-column entries and k!=0;
(F1) Im(T(0) conj(T(1)))!=0;
(F2) Im(q0 conj(q2))!=0.
These are exact finite symbolic statements, NOT numerical tests. Earlier unreviewed E1/E2 text may be exposed as
hypotheses for (H0), but (F1) and (F2) still need a written proof in this package before a CLOSURE delivery.
WH covariance and U/U^2 transport then give all bases and all translates. The W8 consequence additionally requires
the separately reviewed internal-F triangle theorem, not merely this conditional result.
