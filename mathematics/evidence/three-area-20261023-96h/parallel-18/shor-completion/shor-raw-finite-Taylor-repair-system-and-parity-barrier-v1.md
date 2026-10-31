# Shor RAW completion — a finite triangular Taylor-repair system, and its parity-only barrier

Owner MathShor-2. Actual `/bin/date` before composing: **Mon Oct 26 06:18:15 PDT 2026** (earlier observation bound). WRITTEN/unreviewed; exact symbolic variables, fractions and integer products only. No scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent or new GO.

This continues the unconditional89LF repair-strip packet `shor-raw-odd-a-repair-strip-and-seed-gap-abstraction-v1.md`, SHA256 `2b40d7babf8e1334638225e1949fe250985a8332a3d8cbac9fd2014393d94cdd`. It is a change from a single negative coefficient to the WHOLE finite low-a Taylor system, retaining arbitrary codeword b-counts. The resulting parity obstruction is proved to stop short of a full contradiction; the stopping point is explicit. No actual completion or full RAW decision is claimed.

## 1. Exact finite triangular equations, without a b-count bound

Suppose M is a hypothetical finite RAW complete UD extension of the literal C. Let

    c_(d,k) = number of ACTUAL words of M with d a's and k b's.

These are nonnegative integers of FINITE support, not commutative replacements for raw UD. The finite-code Bernoulli identity is a necessary polynomial identity

    sum_(d,k) c_(d,k) z^d(1−z)^k=1.                       (MASS)

The unique pure-b word gives c_(0,1)=1 and all other c_(0,k)=0. Since ba and b are in M, any word with exactly ONE a other than ba is forbidden: enough leading/trailing b-padding would have a parse in {b,ba}* and a distinct parse using that word. Hence c_(1,1)=1 and all other c_(1,k)=0. Let a^n be the unique pure-a word. The one-b Shor words have max a-count14, and the MASS limit to the first b-layer gives |M intersect a*b a*|=n. Thus n>=16, so the pure-a word contributes nothing through a-count14. The stronger FACT divisibility is not needed.

Expanding MASS at z=0, for each N=1,...,14 the exact coefficient equation is

    sum_(d=0)^N sum_(k>=0)
       c_(d,k) (−1)^(N−d) binom(k,N−d) =0.               (T_N)

Use binom(k,j)=0 when j>k. Each sum is finite for each candidate M, even though there is NO imposed upper bound on k or maximum word length.

The unknown new words at a-count d first appear with coefficient+1 in T_d; all their higher-binomial moments enter the later equations. This is a TRIANGULAR finite collection of necessary equations in the UNBOUNDED actual-b-count data. It does not decide raw membership, interval delays or UD. A future contradiction valid for every nonnegative raw-compatible solution would exclude a completion; a formal nonnegative solution would NOT construct one.

## 2. The first two-a layer is genuinely forced at arbitrary delay

The literal seed has exactly b and ba at a-counts0 and1. In T_2, the only earlier contribution is−1 from ba, so

    sum_k c_(2,k)=1.                                     (A2)

No pure-a or one-b Shor word has exactly two a's. The UNIQUE two-a word cannot split them into two isolated single-a runs: any such raw word is C-b-boundary-completable by repeated ba and b, hence forbidden in an extension. Therefore it is

    q_2=b^alpha a² b^beta,

with alpha,beta>=1. If alpha=0, appending one b gives the two distinct parses (q_2)(ab) and(ab)(b^beta)(ab), using the seed word ab. If beta=0, left padding and two ba words give an ambiguity. The cases of no b at all are already excluded by a^n with n>=16. Thus the total b-count k_2=alpha+beta is at least2, with NO upper bound.

This agrees with, rather than replaces, the baseline start/end/isolated PR interface. It is not the invalid assertion that every small a-run needs a singleton word; start/end words can concatenate across zero gaps and must be retained.

## 3. A raw-compatible degree-five control with its exact negative defect

The following finite language is a CONTROL, not a proposed completion:

    Q = {b, ba, ab², ba²b, a³b, a³ba²}.

Every displayed word belongs to the hypothetical M if q_2=ba²b (alpha=beta=1): b,ba,a³b,a³ba² are literal seeds, and ab² is boundary-completable by ba only after padding but is NOT itself a seed. Accordingly Q is NOT asserted to be a subset of M and NOT used as an operative hypothesis. Its role is only to display why a convenient fixed delay or a selected small-code mass model cannot be silently substituted. No code/completeness claim for Q is made.

The exact actual system must keep the unknown alpha,beta and EVERY raw seed word, rather than normalize q_2 to this or any other chosen delay. This paragraph does not evaluate a numeric candidate or give it guidance/proof credit; it records the logical non-substitution boundary.

## 4. Parity-only abstraction of the full low-a repair obligation

Assume, for the purpose of a necessary obstruction, that every NEW codeword with a-count<=14 has EVEN a-count. The high-a words do not affect T_N for N<=14, and the pure-a word is beyond this range. Let the new low-a contributions be

    R(z)=sum_(d EVEN, 2<=d<=14) sum_k u_(d,k) z^d(1−z)^k,

where u_(d,k)>=0 count ACTUAL new words and retain arbitrary k. The known one-b contribution is (1−z)C_1(z), with

    C_1(z)=1+z+2z³+z⁵+2z⁷+z⁸+z⁹+2z¹¹+z¹²+2z¹³+z¹⁴.

The coefficients list the sixteen raw seed words by total a-count, with multiplicities retained. Therefore, modulo z^15,

    (1−z)C_1(z)+R(z)=1.                                 (EVEN)

Replace z by−z, subtract, and divide by2z. Every even-d new word contributes

    z^(d−1) * [ (1+z)^k − (1−z)^k ]/(2z)

on the corresponding side. The bracket is a polynomial with NONNEGATIVE coefficients: its coefficients are binom(k,j) for odd j after dividing by z. Thus parity puts sign/degree constraints on the odd coefficient equations, without any b-count cutoff.

This looks promising but does NOT by itself exclude EVEN. Each new word's arbitrary k supplies many positive binomial moments, and its occurrence at even d shifts those constraints. The Shor one-b odd part does not alone force a negative coefficient in the relevant transformed deficit: even-d words with large k contribute at the same low Taylor orders. The single NEG14 argument from the earlier repair packet, by contrast, concerns the DIFFERENT H=(G_n−Z_1)/(1−z), whose negative coefficient already proves an odd-a repair word without imposing this false even-only hypothesis.

Thus no universal parity contradiction beyond the earlier unconditional odd-a repair-strip theorem is obtained from EVEN. Neither high-b moments nor raw q_2 delays can be replaced by chosen fixed values to force one. The complete low-a Taylor system is necessary but still loses word-order and all-gap GP information.

## 5. Exact remaining original gap

A useful next representation must combine the triangular binomial-moment constraints with ACTUAL free-end parses at every internal b-gap, not merely total counts. The forced odd-a word has one of the bounded seed-hard a-run shapes of the earlier packet but has arbitrary b-delays; all other words and arities remain unrestricted. Proving every such lift triggers an incompatible finite repair cascade would close the negative direction. Supplying actual finite words with all RAW UD/factor-completeness conditions would close the positive direction. Neither is delivered here.

The source's §3 control is deliberately NONPREMISE; any normalization to it would be an invalid smaller problem. The newly proved constraints are T_N and A2 with the explicit raw endpoint form, not a completed parity obstruction. I3/I4/I5 have no role in these direct finite-code identities. H* remains FALSE/WITHDRAWN. All earlier FACT/rawPR/isolated/higher-gap/delay/STAB boundaries and the parent's LF58 qualification remain.

Own permanent v109-A exactness MAJOR/all older histories preserved. No source/shared/frozen edit, git/deletion/publication, scientific GO, formal/kernel/human/configured-family/executable/novelty acceptance or early final park. Original Shor completion **NOT_PROVED** either direction, same original cutoff/deadline.
