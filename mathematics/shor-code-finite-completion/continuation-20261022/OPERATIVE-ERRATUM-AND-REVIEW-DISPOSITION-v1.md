# Operative Shor erratum and review disposition

Before-creation clock observed: 2026-10-22T23:10:08-0700. Read this together with `proof-REDEI-BORDER-ORDER-v1.md` (SHA256 `7ac304f71a384d9acdf4529856f618a10e6859cb526d6ae51b83a90ba981f2a4`). The actual in-harness review is `review-REDEI-BORDER-ORDER-v1.md`, SHA256 `92ba3f95ae17b8e09f4503740b0caffee5d20c1518d496c2b90490931863a123`, read WHOLE by the parent. Its two findings are accepted below; the original proof bytes are unchanged.

## F1 — status/target-B clarification, accepted

The restriction that n=1320m has m divisible by at least two distinct odd primes was already implicit in the old **conditional** predicate. Indeed n/330=4m; three distinct prime divisors of4m imply two odd prime divisors ofm. Conversely, if distinct odd primes r,s divide m, then2,r,s are three distinct prime divisors of4m, so330·2rs divides n. Overlap with primes dividing330 is allowed throughout.

Thus the manuscript gives a better-sourced derivation and an explicit structural restatement of a known-form necessary condition, **not an additional new condition beyond the old conditional statement**. Read “New source-relative order restrictions” in its final section as “This source-supported restatement of the previously conditional order restriction.” The frozen target B (an additional genuinely new necessary condition) is **UNMET by this manuscript**. It is not passed by a new citation or by removing a source-access gap. No novelty/SOTA gain is claimed.

Target A has a bounded alternate-route outcome: the unauthenticated2006 transcription is not used by the new derivation. The exact statement of Cordero2023 Lemma5.2 is a declared external theorem input. The2006 primary theorem/proof and the monograph proof remain unauthenticated/unread, respectively.

## F2 — multiplier notation, accepted

In LemmaM0, write the pushforward as

    (T_d B)(g) = sum_{d h=g} B(h)

and write ordinary convolution powers as B^{*k}. The characteristic-ell calculation is

    F*(T_ell B) = F*B^{*ell}
               = W*B^{*(ell-1)}
               = |B|^(ell-1) W
               = W.

The first equality is Frobenius in the commutative characteristic-ell group ring. The exponent ell−1 in the middle is an ordinary convolution power, not the pushforward T_(ell−1). Iteration uses T_d(T_e B)=T_(de)B and preservation of total mass. This makes the two operations unambiguous without altering the argument.

## Domain and verification boundary

The applied normalized factorization always has n≥20; no trivial group n=1 instance of R2 is claimed. Both factor-generation checks, all multiplier collisions, positive quotient arithmetic and prime-overlap handling were checked by the parent and the in-harness reviewer. The review found no mathematical defect at those explicit imported boundaries. These wording dispositions were parent-applied and were not independently re-reviewed.

All outputs remain **CANDIDATE**, not a completed historical two-family gate, formal proof or full code-completion result. Target B remains unmet; the exact missing source proof remains blocked. No code, solver, Lean, model CLI, credential/payment/config change or old-file mutation was used to dispose these findings.
