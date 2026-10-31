# Double-saturated Shor completions: separate even/odd tail balance at odd primes

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 18:15:15 PDT 2026**.
**All-order conditional written theorem with bounded exact checks; not an original unrestricted no-go or novelty claim.**

## 1. Branch and main conclusions

Let D be ANY finite UD factor-complete extension of the literal Shor code. Its SAME actual one-b layer B has n atoms, where a^n is its unique pure-a atom. Assume BOTH original prefix rows3 and8 attain n/4 atoms. The independently written unique-row/conservation candidates force

    n=16m, m>=2;
    J_3=J_8={0,2,4,6}+16 Z_m;
    all heads are 3,8, or congruent0 or11 mod16;
    folded head masses R_0=R_3=R_8=R_11=4m.

Let N_out count B-atoms with heads outside the four original residues, and assume additionally

    N_out < n/8.                                           (1)

**Theorem.** For EVERY odd prime p>=5 dividing n, the SAME actual suffix histogram is separately uniform across p residues within each parity: the number of even-suffix B-atoms in each residue class mod p is E/p, and the number of odd-suffix atoms in each class is O/p, where E,O are the ACTUAL total even/odd suffix counts. Equivalently its integer polynomial is divisible by BOTH Phi_p and Phi_(2p).

If 3 divides n and at least one actual new-head atom has its 16-block index NOT divisible by3, the same separate-parity conclusion also holds for p=3. If every new-head block index is divisible by3, the present argument does NOT force Phi_6.

Let P be the product of the DISTINCT odd primes >=5 dividing n (P=1 if there are none). Then E and O are multiples of 2P; in the stated p=3 subcase they are multiples of6P. For example, under this branch at n=2640, hypothesis(1) gives E,O divisible by110, and by330 if at least one new head's block index is not divisible by3. This is a conditional necessary constraint, not a claim that n=2640 or this branch is realizable.

## 2. Actual head polynomial and small perturbation

Put q=4m=n/4. Write e for the number of B-atoms with a NEW head `16h`, and o for those with a NEW head `11+16h`, 1<=h<m; repetitions of a head count with their actual atom multiplicities. Thus `N_out=e+o`.

The forced folded head balances give `r_0=q−e` and `r_11=q−o`, while the literal saturated rows have r_3=r_8=q. Therefore the actual integer head polynomial is

    R(X)=q(1+X^3+X^8+X^11) + D(X),                       (2)
    D(X)=sum_(new even atoms) (X^(16h)−1)
         +X^11 sum_(new odd atoms) (X^(16h)−1).

No two new atoms are assumed to have distinct h. The coefficient l1 norm of D is at most `2N_out`, even if terms cancel. Under(1), `q>2N_out`. Equation(2) and every later count concern ONE actual B, not a chosen marginal profile.

## 3. Force the order-2p suffix factor for every p>=5

Take ANY odd prime p>=5 dividing n and a primitive2p-th root zeta. Because 16|n and p is odd, 2p|n. Its cyclotomic polynomial is

    Phi_(2p)(X)=Phi_p(−X)=1−X+X²−...+X^(p−1),

monic of degree p−1. Every monomial X^k, reduced modulo Phi_(2p), has coefficients in `{0,±1}`: first use X^p==−1, then for the sole exponent p−1 use `X^(p−1)=X^(p−2)−...+X−1`. Therefore EVERY coefficient in the reduced D is bounded in absolute value by2N_out.

The base polynomial `A(X)=1+X^3+X^8+X^11=(1+X^3)(1+X^8)` is NONZERO at zeta. A root of `1+X^3` has order2 or6; a root of `1+X^8` has order16. None has order2p when p>=5. Thus the integral remainder of A mod Phi_(2p) has some nonzero integer coefficient. Its magnitude is at least1. Because q>2N_out, the corresponding coefficient of `qA+D` cannot vanish. Hence

    R(zeta)!=0  for every primitive 2p-th root zeta.

Actual seam conservation R(zeta)C(zeta)=0 now forces `Phi_(2p)|C`.

The prime dichotomy of `frontier-20261028-seam-fourier-tradeoff-v1.md`, SHA256 **8169a9e6a7d7823a1c21f05794bf1c9e4c9290ac70a57855a0e4f0d322e19de2**, also forces `Phi_p|C`: the alternate uniform-head branch requires at least `(p−|A mod p|)n/p >= (p−4)n/p >= n/5 > n/8` new-head atoms, contrary to(1). This bound is conservative for p=5; all p>=5 are covered.

For each b mod p let E_b/O_b count actual suffixes in that class with even/odd exponent. Vanishing at a primitive p-th root forces `E_b+O_b` constant in b. A primitive2p-th root zeta satisfies `omega=−zeta` primitive of order p; `C(zeta)=0` says `sum_b(E_b−O_b)omega^b=0`, forcing `E_b−O_b` constant by irreducibility of Phi_p. Adding/subtracting proves that E_b and O_b are separately constant. There is no joint-CRT-uniformity assumption.

## 4. Exact order-6 exception, for ANY outside count

Now suppose 3|n, and let zeta be a primitive6th root, omega=zeta². Here `A(zeta)=0`, so a small-perturbation dominance argument is NOT used. We have `zeta^16=omega²` and `zeta^11=−omega`.

Let E_1,E_2 count new even-head atoms whose 16-block index h is1,2 mod3, and O_1,O_2 count new odd-head atoms similarly. Evaluating(2) in the basis `{1,omega}` of Q(omega), the two coefficients of R(zeta) are

    −2E_1−E_2−O_1+O_2,
    −E_1+E_2+O_1+2O_2.

If both are0, the first gives `O_2=2E_1+E_2+O_1`; substituting in the second gives `3(E_1+E_2+O_1)=0`. All counts are nonnegative integers, so E_1=E_2=O_1=O_2=0. Conversely these four zeros make R(zeta)=0. Thus

    R(zeta_6)=0  IFF every actual new-head block index is0 mod3. (3)

This iff uses no N_out bound. If ANY index is not0 mod3, conservation forces `Phi_6|C`. Under(1), N_out<n/3, and the prime tradeoff forces `Phi_3|C` as well. The same sum/difference argument gives separate parity uniformity modulo3. If all block indices are0 mod3, equation(3) only says that this route cannot force the Phi_6 suffix factor; it is NOT a converse completion criterion.

## 5. Parity total consequences and example

The earlier double-saturation theorem forces the actual tail paired-class balance mod4, so E and O are even. Separate balance for each odd p>=5 makes each of E,O divisible by p; the primes are distinct, so both are divisible by2P. If the order6 subcase also applies, they are divisible by6P.

For n=2640=16*3*5*11, P=55. Thus under the ACTUAL hypotheses, E,O are multiples of110, and of330 in the nonzero-mod3-block subcase. These are simultaneous properties of the SAME suffix distribution. Marginal balances for individual primes do NOT imply uniformity modulo their product; no such inference is made.

## 6. Actual exact checks and limits

Executed:

    python3 -B frontier-20261028-double-sat-cyclotomic-check.py

A separately written exact integer checker verified the monomial-remainder coefficient bound and nonzero qA+D for bounded p=5,7,11,13,17,19 and125/343 tested three-atom block-index combinations per domain. It tested all2401 nonnegative quadruples E_1,E_2,O_1,O_2 in0..6 and found the unique zero tuple `(0,0,0,0)`. Synthetic p=5 histogram controls verified that uniformity mod p alone does NOT imply separate parity uniformity, while a separately parity-uniform histogram satisfies the Phi_(2p) condition. Those synthetic histograms are NOT Shor completions. The algebraic coefficient bound and nonnegativity proof above establish all primes/counts, not the samples.

Checker `frontier-20261028-double-sat-cyclotomic-check.py`, SHA256 **ca04a580f1b3d2f1df09735c9a3fb12b1799b6946dd611acf89c568e461294c3**,72 LF /2749 B, natively pinned Wed Oct28 18:15:15 PDT.

## 7. Exact scientific residual

The new constraints apply only if BOTH old rows saturate and the SAME actual N_out is <n/8. No argument proves that those assumptions hold, that any resulting balanced tail array is realized, or that the branch is impossible. To decide the original question one must still handle non-saturated rows and all-list/multi-b/factor-completeness couplings. No original witness, all-order no-go, novelty, formal/kernel/human or independent-model acceptance is claimed. Historical held records remain historical, not mathematical premises.

**END OF DOUBLE-SATURATION PARITY-CYCLOTOMIC CANDIDATE.**
