# Addendum 1 to peer-review-nl242-normalized-union-completeness-v1.md

Actual `/bin/date` before this write: `Sun Oct 25 11:25:25 PDT 2026`. This is an additive reviewer erratum. The frozen review keeps its bytes: 335 LF, SHA-256 `9005848e059a9b8298c7055f21dcaf1767c38dfed0afe086571ac7064bb3aff4`.

## The defect

Review LF142 contains a garbled false start: "Here Hq = −Hχ²... more precisely". WITHDRAW that fragment. It is not a claimed identity.

## The intended derivation

The surviving identity on the same line, Hq = −2χ, is correct:

```text
q = -(H chi)/128,  H(H chi) = 256 chi  =>  Hq = -2 chi.
```

With HB = S/2, B = q − b − 3q·1_E, C = Hb and P = H(q·1_E), this gives S = 2HB = −4χ − 2C − 6P. This matches S8:216 exactly.

## Effect on the review

None of the review's derivations, its §0 verdict (0 FATAL / 0 MAJOR / 0 MINOR at the forward scope), J_N or its named imports change. This is a presentation erratum in my own text, not a finding about S4 or S5. No source, shared or parent file was modified.
