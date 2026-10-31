# f46 — disjoint review of Walsh zero/support structure

Reviewer **InfoGuessingRminus-2**. Native `/bin/date` observation before this write: **Wed Oct 28 17:38:51 PDT 2026**; the eventual pin/RETURN clock is separate.

**Verdict: FATAL 0 / MAJOR 0 / MINOR 1.** The three candidate conclusions, including `4<=|Z|<=148`, are mathematically reconstructed at the exact conditional scope below. The one MINOR is an omitted explicit dependency in the written derivation of the upper endpoint; §4 reconstructs it rather than assuming it. No actual Boolean witness, unrestricted no-go, formal/human/cross-model review, current novelty or adoption is established.

## 1. Exact scope and pinned intake

For **every** balanced `f:F_2^9->{0,1}` whose Walsh transform satisfies `max_a |W_f(a)|<=28`, put `k=W_f/4`, `S={a:k(a)!=0}`, `Z=F_2^9\S`, `S4={a:|k(a)|=4}`. The candidate's exact conclusions are:

1. For every `u`, both sign counts in `k(a)(-1)^(a·u)` are even.
2. `XOR(S)=XOR(Z)=0`, `|Z|` is even and `4<=|Z|<=148`.
3. `|S4|` is even and `XOR(S4)=0`; a nonempty S4 has at least four distinct frequencies.

No selection of rank, spectrum, excluded residue branch or `(24,24,2)` alternative is made. The statement is conditional on an actual Boolean function, not the existence of one.

- Assignment `f46-nl242-walsh-zero-structure/assignment-v1.json`: read completely before the candidate.
- Candidate `frontier-20261028-walsh-zero-structure-v1.md`, SHA256 `5af3cf5e021e44211e566bce858752f6dbb1706181e001cc962a17d50d930937`, **70 LF / 7376 bytes**: read completely.
- Registered `info-6-full-walsh-definitions-v1.md`, SHA256 `af51f147a8d56e915cbd17687b9a62c859e19cba1937346a8eedd40e108497b1`, **9 LF / 1243 bytes**, and complete registered packet SHA256 `a9931cf5a12f174c232e6ad50fba993e5cd01ee9d4ab13dcfe0bd35dc69d3d37`.
- Named code/dual interface `walsh-projective-code-equivalence-v1.md` SHA256 `b68e9f6bc546872e96066625ebfb7872f92f7a78d0187e9fa1925045148dbfeb` and 15-congruence source `dual-enumerator-congruence-reduction-v1.md` SHA256 `6817ccf924a52f42fe5d860b936f79b021e6dd095efbd1b10c5a8a2facb74dad`: read completely.
- For the upper-endpoint dependency, also read the complete current `prerequisite-derivation-v1.md`, `walsh-support-xor-obstruction-v1.md`, and mandatory `walsh-support-xor-coupled-count-erratum-v1.md` SHA256 `810e3e55c52288f252b335a776a134752702df33d70d8d689fb009aac127273c`. Their mathematics is reconstructed below; the inaccurate independent-count wording in the uncorrected XOR source is not used. The additional hyperplane-energy and peak-multiplicity files were inspected for dependency context; the `>=92` claim is not needed here.

The original source packet fixes the Walsh definition and modern threshold; this review does not certify verbatim book/source equivalence. No author contact, external-model call, held-result acceptance, selected rank or candidate function was used.

## 2. MINOR 1 — make the upper-endpoint prerequisite explicit

At **candidate LF60**, the argument uses “256 odd codeword deviations” but does not itself derive why the truth-support XOR is nonzero. The named code-interface dependency does state that 256/255 split, but attributes it to an earlier `T!=0` result rather than proving it there. The candidate should explicitly name this indispensable prerequisite and its count-direction overlay, or include the short reconstruction in §4 below. In particular, §4/LF68's statement that the proof above reconstructs the needed interface and congruence is too easy to read as though the `T!=0` step were also shown in the candidate itself.

This is a **MINOR dependency/exposition omission**, not a counterexample to the stated upper bound: §4 proves the needed `T!=0` directly from the registered Boolean definitions and peak bound, and all downstream calculations then follow. The sign-parity/XOR/lower-zero and S4 claims do not need this imported count split. An additive clarification should preserve the frozen candidate bytes and the corrected coupled-count argument.

## 3. From the actual Boolean object to the congruences

Let `M={x:f(x)=1}`. Balance gives `|M|=256` and `W(0)=0`. For nonzero a, character cancellation gives

```
W(a) = -2 sum_(x in M) (-1)^(a·x) = 4(w_a-128),
w_a = |{x in M:a·x=1}|.
```

Thus all Walsh coefficients are divisible by 4, including `W(0)=0`, and `|k(a)|<=7`. Normalizing by a global output complement if necessary preserves balance and magnitudes and makes `f(0)=0`; M then contains 256 distinct nonzero columns. For each `a!=0`, `121<=w_a<=135`, so the linear map `a -> (a·x)_(x in M)` has no nonzero kernel and rank 9. The number `A_t` of nonzero frequencies with `k(a)=t` is consequently the number of nonzero codewords of weight `128+t`, and `sum_t A_t=511`.

For any j-subset J of the 256 columns, the character sum `sum_a (-1)^(a·sum_(x in J)x)` is 512 when J lies in the binary dual kernel and 0 otherwise. Summing over all J, and expanding the product over columns, proves from scratch

```
512 D_j = C(256,j) + sum_t A_t K_j(128+t),
K_j(w) = sum_i (-1)^i C(w,i) C(256-w,j-i),  0<=j<=256.
```

This is an identity for one actual common code; no separate D_j profile is postulated. The complete numerator generating polynomial is

```
P(z)=(1+z)^256 + (1-z^2)^121 B(z),
B(z)=sum_(t=-7)^7 A_t (1-z)^(7+t)(1+z)^(7-t).
```

Every coefficient of P is divisible by 512. Since `1-z^2` has constant term 1, it is a unit in `(Z/512Z)[[z]]`. Writing `q=z/(1-z)`,

```
(1+z)^256 (1-z^2)^(-121) = (1-z^2)^7 (1+2q)^128.
```

For `1<=j<=128`, `v_2(C(128,j))=7-v_2(j)`: `C(127,j-1)` is odd because `(1+x)^127` is the product of the seven binary factors `(1+x^(2^i))` over F₂, and `C(128,j)=128 C(127,j-1)/j`. Thus the `j>=3` terms of `(1+2q)^128` are multiples of 512; the j=1 and 2 coefficients are both 256 modulo 512. As `q+q^2=z/(1-z)^2` and `(1-z)^2=1-z^2` modulo 2,

```
B(z) + (1-z^2)^7 + 256z(1-z^2)^6 = 0   (coefficientwise mod 512).
```

This is a congruence of polynomials, so substituting `z=1-u` and `z=u-1` is valid; no substitution into an infinite inverse series is required.

At `u^6`, the background contributes 0 modulo 512. The first substitution gives coefficient 256 on each `A_t` for `t<0` and 0 on `t>=0`; the second does the same for `t>0`. Consequently both the negative and positive counts are even and `A_0` is odd.

At `u^7`, the first substitution yields coefficient 128 on `A_0`, 256 on `A_-4`, 0 on the other A_t, and background 128, all modulo 512. The other substitution replaces `A_-4` by `A_4`. Dividing the two congruences by 128 yields exactly

```
A_0 + 2 A_-4 + 1 = 0 (mod 4),
A_0 + 2 A_4  + 1 = 0 (mod 4).
```

The finite independent polynomial replay and its observed outputs are in §7.

## 4. Reconstructing `T!=0` and the 256/255 parity split

Let `T` be the XOR of the 256 points of M. For any frequency a, `k(a) mod 2 = a·T`: this follows from `k(a) congruent mod 4` to the number of x in M with `a·x=1`, including a=0. The exact XOR identity modulo 4, `r xor s = r+s-2rs`, shows that as a function of the nine input bits a, `k(a) mod 4` is a polynomial of degree at most 2. More explicitly, its linear coefficients are `sum_(x in M) x_i mod 4` and its quadratic coefficients are `-2 sum_(x in M) x_i x_j mod 4`.

Suppose `T=0`. Every linear coefficient is even and every k(a) is even. Hence `Q(a)=k(a)/2 mod 2` is a Boolean polynomial of degree at most 2, with `Q(0)=0`. Its complement `1+Q` is nonzero. A nonzero multilinear Boolean polynomial of degree at most d in n variables has at least `2^(n-d)` ones: induction on n using `P=P_0+x_n P_1` either doubles the previous weight if `P_1=0`, or counts at least one of the two x_n values whenever nonzero `P_1` is 1. Thus `Q=0` at at least 128 frequencies and `r=|{Q=1}|<=384`.

Parseval gives `sum_a k(a)^2=512^2/16=16384`. On `Q=1`, even k has `|k|<=6`, so its square is at most 36. On the other `511-r` **nonzero** frequencies, `Q=0` means k is divisible by 4, so its square is at most 16; at zero frequency k=0. The coupled count is essential:

```
16384 <= 36r + 16(511-r) <= 15856,
```

a contradiction. This reconstructs the needed lemma with the mandatory count correction, rather than using the uncorrected separate complement bound.

Therefore `T!=0`. The linear functional `a -> a·T` is nonzero, so exactly 256 frequencies have odd k, and exactly 256 have even k, including a=0. For a normalized object this is exactly the candidate's 256 odd and 255 nonzero even codeword deviations. No assumption about which nonzero T occurs is needed.

## 5. All translations, XORs and zero-count endpoints

For every u, the actual function `f_u(x)=f(x+u) xor f(u)` remains balanced, has `f_u(0)=0`, and satisfies the same peak bound. Changing variables in the Walsh sum gives

```
k_(f_u)(a)=(-1)^(f(u)+a·u) k_f(a).
```

Both sign counts of the normalized f_u spectrum are even by §3. Multiplying all signs by the common `(-1)^f(u)` can swap the two counts but cannot change their evenness. This proves candidate LF9 for **every** u, not only for a fixed modulation.

Let N be the negative part of S at u=0. Toggling signs at those a with `a·u=1` changes negative-count parity by `sum_(a in S) a·u`. Both parities are zero, so `u·(XOR S)=0` for every u. Nondegeneracy of the standard pairing gives `XOR S=0`. Each coordinate is 1 on 256 members of V, hence `XOR V=0` and `XOR Z=0`.

The positive and negative counts are even, so `|S|` and then `|Z|=512-|S|` are even. Balance puts 0 in Z. A 2-element set containing 0 has nonzero XOR, so the even possibilities below 4 are impossible; `|Z|>=4`.

For the other endpoint, the 256 odd k-values have squared sum at most `256*49`. The remaining 256 even positions include a=0, leaving 255 nonzero frequencies. Their squared sum is at least `16384-256*49=3840`; exactly `A_0` among them have k=0 and every other even k has square at most 36. Therefore `36(255-A_0)>=3840`, giving `A_0<=148`. Since A_0 is odd, `A_0<=147`, so `|Z|=A_0+1<=148`. This is precisely where §4's `T!=0` is required.

## 6. The `|W|=16` layer

From the two modulo-4 congruences, `A_4` and `A_-4` have the same parity. Thus `|S4|=A_4+A_-4` is even, and the parity of `A_4` is fixed by `(A_0+1)/2 mod 2`. Translation/output-complement changes signs but not zero count A_0 or the set S4. If its common sign flips, the positive and negative S4 counts still have the same parity because their total is even. Thus for every u the parity of the positive S4 count is the same. Comparing it with u=0 gives `u·(XOR S4)=0` for every u and hence `XOR S4=0`. A 2-element set of distinct frequencies has nonzero XOR, so an even nonempty S4 has at least four elements. No assumption that S4 is nonempty is made.

## 7. Independent exact calculation and limits

I wrote `frontier-review-f46-walsh-symbolic-check.py` without opening or importing the author's checker. Its SHA256 is `2bff9677969072fb803d24cc726ce2d4acfd15079dae148c351c4edbfdee50d0`; the exclusive result JSON has SHA256 `f0faccc68647e6f3d8db6b88c8e1708e133a967d361e856634d3d92000d181ca`. Executed command:

```
python3 -B frontier-review-f46-walsh-symbolic-check.py
```

Observed: **257/257** global polynomial coefficients agree modulo 512; all **15** formal A_t coefficients for both substitutions and both degrees agree with §3; H contributes `(0,128)` at `(u^6,u^7)` in both substitutions; all **128** stated binomial valuations agree; a changed background constant is rejected first at coefficient 0. Exact integer values `15856<16384` and `16384-256*49=3840` were also computed. The native output/hash clock was **Wed Oct 28 17:38:12 PDT 2026**.

These calculations verify the finite coefficient manipulations, not existence of a Boolean f or an independently checked source/novelty claim. The remaining scientific problem is an actual balanced NL>=242 function or an unrestricted exclusion. This review is same-harness written plus the stated local exact script; not formal/kernel, human, configured-family, cross-vendor, or a proof of worldwide openness.

**END OF f46 REVIEW.**
