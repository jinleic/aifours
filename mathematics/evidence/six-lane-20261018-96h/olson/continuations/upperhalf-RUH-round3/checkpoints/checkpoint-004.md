# RUH3 checkpoint 004: R1 split; R1a (e<=(p-1)/2) appears to close by hand; R1b (e=(p+1)/2) open

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T18:10:55-0700. Previous checkpoint-003.md SHA256
6f58f3ffe8bbe0f5e200a645b2be66d0d78a24c71a3eeeb7d8d8c70364a8c919 (17:58:58). Frozen so far: proof-RUH3-v1.md
027ac177c9b14e76ef86d1f0c881629eb1011f1dec32c9570f48be7e0b626b31 (SH range). Hand derivation only; nothing new frozen yet.

Derived (CANDIDATE, unfrozen), nu:=p+1-2e:
- Lemma L*: for e<=(p-1)/2 every LOW set with 1<=m<=k'':=min(e,floor((p+2-e)/2)) has d<=c-min(e,2m-1) (MW count: Case A
  needs m<=floor((p+1-g)/2), worst g=e-1; Case B needs floor((p+1+g)/2)>=e+ceil(g/2), true for p>=2e+1). 2k''-1>=e.
- Super-heavy run without MWe: at m=k:=floor(e/2)+1<=k'' low sets have d<=c-e, high ones (complements) d>=Lambda+e-1, gap
  p+1+delta; toggle path at m=k (N>=2k+2) gives h with d_h>=p+1+delta; light sets and counts as before.
- Lemma E* (no h needed beyond E>=2): with interval counts <=ceil((e+1)/2) all lengths stay free and lifts additive; E<=ceil(c/2)-1
  and the refinement E+C_E<=e+eps-1 (C_E = number of empty clusters; C_E<=m(Y+)+m(Y-)).
- POS*: if m_Q>=k'' the k'' largest Q-blocks hold <=c-e runs, the rest are singletons, and m_Q-1<=C_E+|X|, |X|<=b=p-1-c give
  c+k''<=p-2+eps, contradicting c>=e+k'' and 2k''>=p+1-e (or c>=2e when k''=e); other cases as in proof-RUH3-v1 Sec. 7 with m<=k''.
- Theorem A extends (m<=floor((c+1)/2)+1<=k''). So R-UH would hold for all 5<=e<=(p-1)/2, p>=11 (SH and R1a).
- R1b: e=(p+1)/2: Case B of the count fails for odd g (parity), so Lemma L*, the m=k window and h are not available.
Next: freeze proof-RUH3-ext-v1.md (R1a + uniform version), audit, residual note for R1b, package, manifest.
