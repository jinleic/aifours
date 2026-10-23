# Theorem P: a Chevalley–Warning proof of ordered EGZ for a class of dihedral words

Status: written proof (lane MathOlson, 2026-10-16), mechanism checked by brute
force (`code/verify_marked.py`, `code/verify_theoremP.py`); NOT yet independently
reviewed.  This is a theorem about a CLASS OF WORDS in D_{2p}; it does not
prove ordered Olson for D_{2p} (the "many odd gaps" class remains open here).

## Setting and conventions

p is an odd prime. D_{2p} = {(v, e) : v in Z_p, e in {+1,-1}} with
(v, e)(v', e') = (v + e v', e e')  (rotations (x,+1), reflections (y,-1)).
For a word w = w_1 ... w_N and indices i_1 < ... < i_k the ordered product is
w_{i_1} w_{i_2} ... w_{i_k}.  An identity k-subword is such an index set with
product (0, +1).  Cyclic rotation of w preserves the existence of identity
k-subwords (a product U V becomes V U = U^{-1} (U V) U).

Let w contain F >= 1 reflections.  Rotate w cyclically so that it ENDS with a
reflection:
    w = X_1 f_1 X_2 f_2 ... X_F f_F,
where f_t = (y_t, -1) are the reflections and X_t (t = 1..F) is the block of
rotations strictly between f_{t-1} and f_t (X_1 = rotations before f_1); n_t =
|X_t|.  ("Gap t" = X_t; cyclically these are exactly the gaps between
consecutive reflections.)

## Theorem P

If N = |w| <= 4p - 1 and  F + sum_{t=1}^{F} floor(n_t / 2) >= 3p - 1,  then w
has an identity 2p-subword.

## Proof

**Step 1 (parametrisation).** In each gap X_t list the rotations in index order
and group them into floor(n_t/2) consecutive PAIRS pi = (i, i'); if n_t is odd
the last rotation of X_t is a SINGLETON.  Introduce Boolean parameters
  u_2, ..., u_F  (gap colours; set u_1 := 0 and u_{F+1} := u_1 = 0),
  m_pi  for each pair pi  (pair marks).
Number of parameters:  M = (F - 1) + sum_t floor(n_t/2) >= 3p - 2.

To a parameter point (u, m) assign the selection S(u, m):
* reflection f_t is selected iff u_t != u_{t+1}  (t = 1..F);
* both rotations of pair pi in gap t are selected iff m_pi XOR u_t = 1,
  otherwise neither;
* singletons are never selected.

**Step 2 (injectivity; the empty selection).** The selection determines the
parameters: going left to right, u_1 = 0 and u_{t+1} = u_t XOR [f_t selected]
determine all u_t; then m_pi = [pi selected] XOR u_t.  Hence the map
(u, m) -> S(u, m) is injective, and S(u, m) is EMPTY iff (u, m) = 0: an empty
selection selects no reflection, so all u_t = u_1 = 0, and no pair, so all
m_pi = u_t = 0.

**Step 3 (size).** |S(u,m)| = #{t : u_t != u_{t+1}} + 2 #{pi : m_pi XOR u_{t(pi)} = 1}.
The first term is the number of colour changes around the cycle 1..F, 1, hence
even.  So |S| is always EVEN, and |S| <= N <= 4p - 1.

**Step 4 (signs and the product).** Let S = S(u,m).  For an element of S lying
in gap t or equal to f_t, the number of selected reflections strictly before
it is #{s < t : u_s != u_{s+1}}, which has the parity of [u_t != u_1] = u_t.
So in the ordered product every selected rotation x in gap t is multiplied by
c_t := (-1)^{u_t}, and a selected reflection f_t contributes c_t y_t to the
rotation coordinate.  The number of selected reflections is even (Step 3), so
the product is (V, +1) with
  V = sum_{t : u_t != u_{t+1}} c_t y_t + sum_{pairs pi selected} c_{t(pi)} x_pi,
where x_pi = x_i + x_i'.  Using (c_t - c_{t+1})/2 = u_{t+1} - u_t (which is
0 when u_t = u_{t+1} and c_t when they differ) and summation by parts with
u_1 = u_{F+1} = 0,
  sum_{t=1}^{F} (u_{t+1} - u_t) y_t = sum_{t=2}^{F} u_t (y_{t-1} - y_t).
For pairs: a selected pair (m XOR u_t = 1) contributes c_t x_pi; one checks
c_t x_pi [m XOR u_t] = x_pi m - x_pi u_t for both u_t = 0, 1.  Therefore, in Z_p,
  V(u, m) = sum_{t=2}^{F} beta_t u_t + sum_pi x_pi m_pi,
  beta_t = y_{t-1} - y_t - sum_{pi in gap t} x_pi.
V is a polynomial of degree 1 in the parameters (over F_p), and S(u,m) is an
identity subword iff V(u, m) = 0 in Z_p.

**Step 5 (Chevalley–Warning on the Boolean box).** Write the size as the
integer polynomial
  Z(u, m) = sum_{t=1}^{F} (u_t + u_{t+1} - 2 u_t u_{t+1}) + 2 sum_pi (m_pi + u_{t(pi)} - 2 m_pi u_{t(pi)}),
which agrees with |S(u, m)| on {0,1}^M and has degree 2.  Over F_p put
  Q = (1 - V^{p-1}) (1 - Z^{p-1}),   deg Q <= 3(p - 1) < M.
On {0,1}^M, Q(x) = 1 if V(x) = 0 and Z(x) = 0 in F_p, and Q(x) = 0 otherwise
(Fermat).  Box lemma: for any polynomial Q over F_p of degree < M,
  sum_{x in {0,1}^M} (-1)^{|x|} Q(x) = 0.
(Proof: suffices for monomials; a monomial of degree < M omits some variable
x_j, and the involution flipping coordinate j pairs points with opposite signs
and equal values.)  Hence
  sum_{x : V(x) = 0, Z(x) = 0 mod p} (-1)^{|x|} = 0 in F_p.
The point x = 0 contributes +1, so there is a parameter point x != 0 with
V(x) = 0 and |S(x)| = Z(x) = 0 mod p.

**Step 6 (conclusion).** By Step 2, S(x) is nonempty; by Step 3 its size is
even and at most 4p - 1; being divisible by p (odd), the size is a positive
even multiple of p below 4p, i.e. exactly 2p.  By Step 4 its ordered product is
the identity.  QED.

## Remarks

1. Corollary (reflection coset): any word of 3p-1 reflections in D_{2p} has an
   identity 2p-subword (F = 3p-1, all n_t = 0).  Finite-exact computations
   (m = 3..9) show 3m-1 is also the sharp threshold for composite m.
2. Which words are covered depends only on the R/F type pattern.  Uncovered:
   F - #(odd gaps) <= 2p - 2; this contains every extremal (length 4p-2)
   dihedral avoider found in the exhaustive D10 data (alternating odd blocks).
3. The 2-part (size parity) is handled ONLY through pairing inside gaps.  A
   general "mixed modulus" Chevalley–Warning statement that would also control
   parity is false (it would give D(G) = D*(G) for G = C_2^4 + C_6).
4. Prime powers m = p^k: the same argument with congruences mod p^k would need
   Brink's restricted-variable Chevalley theorem for prime-power moduli
   (Combinatorica 31 (2011) 127-130); its exact hypotheses have NOT been read
   from the source here, so the extension is CONDITIONAL and kept separate.
