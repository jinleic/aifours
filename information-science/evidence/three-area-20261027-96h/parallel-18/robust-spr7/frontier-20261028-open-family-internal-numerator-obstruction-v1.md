# An explicit open family of Hurwitz septic boxes whose common numerator cannot lie in the box

Owner **InfoSPR7-2**, slot info-2. Native `/bin/date` observation immediately before writing: **Wed Oct 28 17:21:55 PDT 2026**.

**Exact rational, author-unreviewed theorem conditional only on the pinned exact base certificate.** It establishes an open family of actual seven-positive-width boxes, not an unrestricted SPR counterexample or an all-box synthesis theorem.

## 1. Base data and independently checked strict margins

Use the FULL base proof `frontier-20261028-actual-box-internal-numerator-obstruction-v1.md`, **149LF/14150B**, SHA256 `736008cc61a9f11bf8a29c6353c14ba44f42632d56580d158b61d69177729902`, and its exact rational checker receipt `frontier-20261028-independent-bernstein-check-v1.json`, SHA256 `a1082adb14075aeab9e87b95e8962fead56699bf0e892db9cf78d5b7d0c1773d`. They specify one actual monic closed coefficient box K0, every member Hurwitz, and one monic exact-degree7 common numerator b_*.

The base receipt supplies FOUR strict exact facts:

1. The smallest of K0's seven widths is `29/500`.
2. For every actual a∈K0 and every t>=0, `P_(a,b_*)(t)/(1+t)^7 >= d`, with `d=1229013649779/3006477107200000`.
3. For every monic b∈K0, the SAME two actual-corner weighted functional W0 obeys `W0(b)<=-eta`, with `eta=356413503300067/373669453125000000`.
4. The coefficient L1 bounds are `B=sum_(j=0..7)|b_*,j|=585271/1000` and `S=sum_(j=0..7)upper_j(K0)=111307/1000`; every coefficient of K0 is positive.

Those are exact rational output facts, not numerical SDP margins. The complete base proof includes the actual K0 endpoints, root-band/Routh/homotopy stability proof, exact two-frequency separator, Bernstein leaves and exact b_*. This manuscript does not silently replace that dependency by its title.

## 2. The whole perturbed family

Let `delta=1/1000000000000`. Let K' be ANY closed monic independent septic coefficient box such that, for each j=0,...,6, its lower endpoint and upper endpoint differ from the corresponding endpoints of K0 by at most delta. The leading coefficient remains fixed at1. This contains a nonempty open neighborhood in the fourteen endpoint coordinates; the stated conclusions also include its closed delta boundary.

Since every original width is at least29/500 and `2delta<29/500`, every K' has seven STRICTLY positive widths. In particular all coefficient intervals remain nonempty and their lower endpoints remain positive. No choice of a single perturbed box or a finite sampled set is used as the proof.

For every a'∈K', choose the SAME interpolation coefficient theta_j∈[0,1] within each jth K' interval and use it in the corresponding K0 interval. This gives an a∈K0 with
`|a'_j-a_j|<=delta` for j=0,...,6, and unchanged monic coefficient. The construction also works if a selected coordinate is an endpoint; positive widths avoid division by zero. The corresponding K' parity-extremal corners a'_i and K0 corners a_i obey these same coefficient bounds.

## 3. One common polynomial norm bound over the FULL frequency axis

For any real polynomial p of degree at most7, t=w^2>=0, and all real w,
`|p(iw)|/(1+t)^(7/2) <= sum_(j=0..7)|p_j|`.
Indeed for |w|<=1 each |w|^j<=1<=(1+w^2)^(7/2); for |w|>=1 and j<=7, |w|^j<=|w|^7<=(1+w^2)^(7/2). This is a pointwise universal inequality, not sampling.

In particular, for an actual mapped pair a',a,
`|(a'-a)(iw)|/(1+t)^(7/2)<=7delta`,
`|b_*(iw)|/(1+t)^(7/2)<=B`,
`|a'(iw)|/(1+t)^(7/2)<=S+7delta`.
The last inequality uses that all K0 coefficient magnitudes are bounded by their positive upper endpoints. These inequalities retain t=0 and arbitrarily large finite t; no division by w or interval width occurs.

## 4. EVERY perturbed member is Hurwitz and the SAME b_* remains common

The base pairing bound and Cauchy imply, for every a∈K0 and every finite w,
`|a(iw)|/(1+t)^(7/2)>=d/B`.
For its mapped a'∈K' and every straight-line intermediate `a_tau=(1-tau)a+tau a'`, 0<=tau<=1, the triangle inequality gives
`|a_tau(iw)|/(1+t)^(7/2)>=d/B-7delta>0`.
Every polynomial on this segment remains monic degree7. The original a is Hurwitz, and root continuity prevents a change in its right-half-plane root count without an imaginary-axis crossing. The displayed bound excludes ALL such crossings, including w0. Hence **every a'∈K' is Hurwitz**. This is an all-member argument for each perturbed box, not an inference from finitely many stable corners.

The SAME fixed b_* satisfies
`P_(a',b_*)(t)/(1+t)^7 >= d-7delta B >0`
for every actual a' and t>=0. Thus its ratio has a common explicit strict margin
`Re[b_*(iw)/a'(iw)] >= (d-7delta B)/(S+7delta)^2 >0`.
The exact rational value of that displayed bound is
`23441340113677195427734375/710449051590745359040512002809856`.
It is conservative, not an optimal gain. b_* remains monic exact degree7. Hence EVERY K' in the stated family is an eligible original box with an explicit unrestricted common numerator.

## 5. Every perturbed box still excludes ALL of its own monic members

Let a'_1,a'_2 be the parity corners of K' corresponding to the two base corners in W0, and let b' be ANY monic polynomial whose coefficients belong to K'. Map b' coefficientwise, by the same interval interpolation, to b∈K0. At every t>=0,

`P_(a'_i,b')(t)-P_(a_i,b)(t)`
`=P_(a'_i,b'-b)(t)+P_(a'_i-a_i,b)(t)`.

The bounds in §3 give, after division by(1+t)^7,
`|P_(a'_i,b')-P_(a_i,b)|/(1+t)^7 <=7delta(2S+7delta)`.
The base W uses two positive weights1 and10, so its entire perturbation is bounded by
`77delta(2S+7delta)`.

The exact rational check gives
`eta-77delta(2S+7delta)`
`=4562010856039563215421979709/4782969000000000000000000000000 >0`.
Thus the perturbed weighted functional W' has `W'(b')<0` for EVERY b'∈K'. If such a b' were a common SPR numerator, both of its actual-corner pairings at the two base finite squared frequencies would be strictly positive, so W'(b') would be positive. Contradiction.

Therefore **NO monic b' inside ANY K'** can be a common SPR numerator for its own box. Positive rescaling does not change SPR signs, so no positive scalar multiple of an actual box member works either. The same b_* outside the denominator boxes succeeds for all of them. This is a robust open-family falsification of the internal-numerator shortcut, NOT a counterexample to unrestricted synthesis.

## 6. Verification, controls and remaining original gap

The exact verifier `frontier-20261028-open-neighborhood-check-v1.py`, SHA256 `eaae1193ae842ac8f8b99d7077613cf8065fb3d440b3cf3ed0a4f1789241d1d0`, was executed once:

`/opt/homebrew/bin/python3 -B frontier-20261028-open-neighborhood-check-v1.py --input frontier-20261028-independent-bernstein-check-v1.json --output frontier-20261028-open-neighborhood-check-v1.json`

Its exclusive-created receipt SHA256 is `b0a43a0f70e6a48a6fd80a856d384f2109f760eb41756974552cece2585bfc01`. It checked exact positive width, denominator nonvanishing, common-pairing margin and separation margin using Python `fractions.Fraction`. An intentionally oversized radius1 was rejected with the intended `radius fails width preservation` reason. The entire universal perturbation proof is the algebra above; the test of that one rejected control does not replace it.

The base and perturbation verifiers are locally authored by the SAME owner. Independent-human/configured-family/formal/kernel verification, parent adoption and novelty screening remain unperformed. The original target is still OPEN: no claim is made about every original box, an actual unrestricted no-numerator box, or exact optimal synthesis values.

Only the original actual-box definitions, complete pinned base certificate, elementary norm/continuity/linear-algebra inequalities and root-continuity principle are used. Prior historical quarantine records remain historical/unvalidated, not accepted premises or retroactive process clearance. No held source or old profile theorem is needed for this construction. No external-model/paid API, nested agent, secret access, Git push/publication, deletion or infrastructure action occurred.
