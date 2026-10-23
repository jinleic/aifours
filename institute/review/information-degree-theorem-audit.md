# Parent audit of the balanced nine-variable degree restriction

Source inspected: `runs/hard-2026-10-15/problems/info-p0403/attack-e1/degree-bound-proof.md`.
This is a written-proof audit only. It is not human peer review or formal verification, and it makes
no novelty claim. The Walsh-divisibility method may well be classical.

## Checked steps

1. Expanding `(-1)^(a·x)` as a product of `(1-2a_i x_i)` over the support T gives
   `W_f(a) = 512[a=0] - 2|T| + 4Σ m_i a_i - 8Σ m_ij a_i a_j + 16(...)`.
2. If f is balanced and every `m_i` is even, every coefficient is divisible by eight. The function
   `q(a)=W_f(a)/8 mod 2` has degree at most two, and balance makes `q(0)=0`. Thus `1+q` is a nonzero
   polynomial of degree at most two and vanishes at no more than 384 points, so q vanishes at least 128 times.
   Those coefficients are divisible by 16.
3. If every |W_f| were at most 28 in that case, then every |W_f| would be at most 24, and coefficients
   at the 128 forced points would be at most 16. Parseval would require `2^18`, but the possible maximum
   is `128·16² + 384·24² = 253,952`. Therefore max |W_f| ≥ 32 and NL ≤ 240.
4. Over F_2, `m_i mod 2` is the sum of `f(x)x_i` over F_2^9, equal to the coefficient of the
   full degree-nine monomial in `f·x_i`. For balanced f this is exactly the coefficient of the
   degree-eight monomial omitting `x_i`. Hence all m_i are even if and only if degree is at most
   seven, if and only if the support XOR is zero.
5. If the support XOR s is nonzero, `W_f/4 mod 2 = s·a`. On its 256 ones every coefficient is 4 mod 8,
   so every |W_f| ≤ 24 would force those magnitudes to be at most 20. Parseval would allow at most
   `256(20²+24²)=249,856`, which is impossible. Therefore every balanced nine-variable function has NL ≤ 242.
6. `x0+x1x2+x3x4+x5x6+x7x8` is balanced, has 256 Walsh magnitudes 32 and 256 zeros, and has NL 240.

## Disposition

No gap was identified. The defensible result is: the maximum nonlinearity of balanced nine-variable
Boolean functions is 240 or 242, independently of the 2026 unrefereed covering-radius claim. A balanced
242 function would have to have algebraic degree exactly eight, equivalently nonzero support XOR.
The existence question remains open in this run.
