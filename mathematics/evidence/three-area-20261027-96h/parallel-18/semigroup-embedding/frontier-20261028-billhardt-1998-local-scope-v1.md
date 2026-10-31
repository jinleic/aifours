# Billhardt's finite counterexample: exact public scope and unresolved local test

**NEW AUTHOR SOURCE SCOPE NOTE + EXACT FINITE CONTROL; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 19:41:01 PDT 2026**. This note neither claims that the published counterexample meets the original local-r hypothesis nor asserts that it does not. It preserves the original full problem as OPEN at the present checked scope.

## 1. Primary publication and what it actually says

Bernd Billhardt, [*On Embeddability into a Semidirect Product of a Band by a Group*](https://www.academia.edu/53871668/On_Embeddability_into_a_Semidirect_Product_of_a_Band_by_a_Group), Journal of Algebra 206 (1998), 40–50, [DOI 10.1006/jabr.1997.7390](https://doi.org/10.1006/jabr.1997.7390), gives the following. The author-hosted full text is openly rendered at the first link; the publisher's endpoint presented a human CAPTCHA here, and no CAPTCHA was bypassed.

- Theorem2.6 gives a finite E-unitary orthodox semigroup that is not embeddable in a semidirect product of ANY band by a group; the paper says that example's greatest group image is C2.
- Section3 defines the variety of left semiregular bands by `xyz = xyz x z y z`, and Theorem3.3 gives a finite E-unitary orthodox semigroup with LEFT SEMIREGULAR idempotent band that is not embeddable into ANY band-by-group semidirect product.
- Section3 defines seminormal bands by `x y z w x = x y z x z w x`. It separately STATES that every E-unitary regular semigroup with seminormal idempotent band is strictly embeddable, attributing this to M. B. Szendrei (private communication) and a more general work then in preparation. This note has NOT reconstructed that proof or located a later definitive publication of the full statement, so it is recorded as an attributed source statement, not independently adopted.

M. B. Szendrei's [2019 survey](https://arxiv.org/html/1909.05280v1) §5.1 also reports the finite nonembeddable E-unitary orthodox example with left semiregular E, and states the older positive result for globally regular E. These facts do not themselves answer whether the specific strengthened example's E is LOCALLY regular.

## 2. What the band identity does and does not imply

A seminormal band is locally regular: in any local monoid eBe, substitute its identity e for z in the seminormal identity. For arbitrary x,y,w∈eBe this yields

`x y w x = x y x w x`,

which is the regular-band identity. No converse is asserted in this note.

LEFT SEMIREGULARITY ALONE does NOT imply local regularity. The following six-element band has identity3:

```text
0 2 2 0 4 5
1 1 1 1 1 1
2 2 2 2 2 2
0 1 2 3 4 5
0 5 2 4 4 5
5 5 5 5 5 5
```

All216 associativity and all216 `xyz=xyz x z y z` substitutions hold. Yet with x=0,y=4,z=1, the regular-band sides `xyxzx` and `xyzx` are2 and5. Because3 is a two-sided identity, its local corner is the entire band, so this band is not locally regular. It also violates the seminormal identity at (x,y,z,w)=(0,4,3,1), giving5 versus2.

`frontier-20261028-left-semiregular-nonlocal-checker-v1.py`, SHA `7a811e132819b58e0dcccc62dfd4b928d0c31b21f95d0123fdabdc7b2f1bbaed`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 19:41:01 PDT 2026**, exit0 and directly checks the literal table and all stated substitutions. The bounded discovery script SHA `2ec18a8f2df9142f169363b691ea9914f2d568b4c6639daade1f50ab629ff804` found a size6 example; no size-minimality or independent verification is claimed.

This separate countermodel does NOT identify or characterize Billhardt's actual E. It proves only that the LSRB label in Theorem3.3 cannot, by itself, be used to certify the original local-r hypothesis.

## 3. Exact possible consequence and missing proof

For an orthodox S, `E(eSe)=eE(S)e`, so S is locally r-orthodox exactly when its idempotent band is locally regular. An E-unitary orthodox semigroup is weakly E-unitary, and its group quotient is pure. If a finite such published source were independently shown to have locally regular E, the following WOULD require careful review: its pure group quotient is its actual syntactic actor (a group's idempotence contexts separate group elements), and the finite actor-image restriction plus pure-CS pushforward could transfer any physical band-by-CS host to a band-by-group host. Because Billhardt's example has no band-by-group host, this would refute that particular locally regular physical-host assertion.

That is only a conditional route. The missing factual payment is an actual check or proof that the SPECIFIC published source's idempotent band is locally regular, plus independent review of the actor transfer and of the relationship between the physical host and the printed target. Neither is provided by the LSRB label or by this six-element countermodel. Conversely, no proof is presented that the published source fails local regularity. The primary paper's theorem is not an original-Q1 disposition here.

The reverse implication `locally regular band ⇒ seminormal band` has likewise NOT been proved or refuted here. Small bounded searches were inconclusive and are not evidence of a universal identity. The standing original R/L/SEP and printed-Q1/Q2 gaps remain open at this record's scope.
