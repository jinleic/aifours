# RUH2 residual note: exact remaining part of R-UH after Theorems A and B, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T17:27:14-0700. Companion of proof-RUH2-v1.md (SHA256
f391b08f2df02036b4a7cfc66c1f118e7f20c6dfb8d89af2a10e121ea58df4e2) read with erratum-1-proof-RUH2-v1.md (SHA256
a3c673137ed35b81220b51f9e19997f0c31b10a32bcb5dc7b222e641f50f3f61). Everything here describes where the routes stop; it is NOT a claim that any cell is
false or that any avoider exists, and the "missing claims" are the unfinished targets of these routes, not proven-necessary
lemmas. No counterexample word is supplied.

## 1. What is proved (pointer)
Full NF antecedent throughout. Lemma L (strong windows) and Theorem A (R-UH for 3<=c<=e-1) on the SH range p>=13,
5<=e<=(p+2)/3; Theorem B (R-UH for e=5, 3<=c<=9, every prime p>=13) and Corollary B (with accepted UH-A: the whole cell
kappa=p-5 is excluded for every prime p>=13).

## 2. Exact residual of R-UH on the frozen range (p>=11 prime, (p-1)/2<=kappa<=p-5, 3<=c<=2e-1)
(R1) Non-SH range: 3e>p+2, i.e. max(5, floor((p+2)/3)+1) <= e <= (p+1)/2, every c in [3,2e-1]. Examples: p=11, e in {5,6}
     (kappa in {6,5}); p=13, e in {6,7}; p=17, e in {7,8,9}; p=19, e in {8,9,10}. In particular p=11 is entirely open here,
     including its cell kappa=p-5=6.
(R2) SH range with 6<=e<=(p+2)/3 (so p>=17) and e<=c<=2e-1. Proven structure there (proof Secs. 3-5): a super-heavy run h with
     d_h>=p+1+delta; every nonempty set avoiding h has d<=c-min(e,2m-1) (Lemma L, 1<=m<=e); E>=2 empty runs; the set Q of pure-a
     runs outside h has |Q|<=d(Q)<=c-1 and E+|Q|>=c+1; the missing set M (|M|<=c, 0 not in M) contains [e-mu,e-1]
     (mu=floor(c/2)), plus e-mu-1 when c is odd and c<=2e-3, and t(Y)+j for every set Y of empty runs and every free j in
     [max(m(Y),e-mu), m(Y)+e-1], with the (N1) rule at j=e-mu-1 for odd c. Remaining run profiles: those satisfying all of
     these with no set P in E u Q violating Lemma L.
Nothing else in the frozen range remains: c<=2 is UH-A; Theorems A and B cover the rest of the SH range at e=5 and c<=e-1.

## 3. Failed routes and exact failing inequalities (retained)
(F1) m=e window when 3e>p+2: in the proof of (MWe) the branch r<=e-2 with r>=p-2e+2-eps is no longer empty, so MW only gives
     phi>=p-1+2(p-2e+2-eps)+eps=3p-4e+3-eps, not phi>=p+kappa. The toggle path then certifies a jump of the weaker gap only;
     no super-heavy run follows.
(F2) Ordinary first passage: a high single run is forced only if Lambda-lambda>lambda, i.e. c<=p-2e+3+delta; light sets need
     A<2 Lambda, i.e. A'<kappa+1-c/2 fails to be excluded in general (two disjoint high sets need A'>=kappa+1-c/2, which is
     compatible with A'<=b-delta when c<=2e-4).
(F3) For c>=e in the SH range, Cauchy-Davenport on the sums of at most e-mu empty-run values (each with the forced interval of
     length mu+1) gives only E<=ceil(c/2) when E<=e-mu and no bound when E>e-mu; the e=5 analysis instead used explicit lists
     of the possible t-values, pairs and triples for each c.
(F4) Theorem A's mechanism (independence number of E u Q at most (c+1)/2) fails for c>=e because Lemma L at m>=(e+1)/2 only
     gives d<=c-e>=0, which allows independent sets of empty runs of any size.
(F5) The endgame for c>=e needs empty runs as separators when Q is a single block (the e=5, c=9 case used the middle of four
     consecutive empty runs); a uniform version needs the structure of the maximal-E configurations.

## 4. Smallest missing claims of these routes
(MC1) For R1: a run h whose avoiding sets are all low and satisfy a Lemma-L-type bound, without the m=e window (for example
      from the ordinary window plus an exclusion of the two-high-set branch A'>=kappa+1-c/2), or a different mechanism.
(MC2) For R2: a uniform classification, for e<=c<=2e-1, of the empty-run values t and positions allowed by the forced
      intervals in M (generalising the e=4 and e=5 lists: E<=ceil(c/2)-1, with the maximal case a block of consecutive empty
      runs of equal value), strong enough for the position argument against Lemma L.
