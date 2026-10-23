**Verdict: ACCEPT-WITH-FIXES.** The exclusion of all 252 balanced fixed-half classes is mathematically sound. One clarification is needed in the packaged proof.

1. **Low severity: qualify the final certificate’s claim without a Walsh-zero assumption.** [proof.md:160](/Users/jinleic/repos/aifours/information-science/evidence/hard-continuation-20261015/proof.md:160) and [parity_certificate.py:128](/Users/jinleic/repos/aifours/information-science/evidence/hard-continuation-20261015/code/parity_certificate.py:128) claim exclusion of every odd complementary half at bound 28. However, [screen.py:122](/Users/jinleic/repos/aifours/information-science/evidence/hard-continuation-20261015/code/screen.py:122) first discards quadratic `128829881857` solely because `zero_capacity=-1`; the final parity certificate checks only `7887107311`.

   **Fix:** state that the parity contradiction needs no additional zero assumption **for the surviving quadratic**, and that the preceding stages complete the balanced-class exclusion. Alternatively, document the omitted argument for the stronger claim. I independently verified that the discarded quadratic also fails the canonical bound: inverse distance **3104 > 416**. Thus the stronger conclusion is repairable; the balanced result is unaffected.

Read-only arithmetic independently confirmed:

- The pinned input hash, all 252 original source-normal mappings, all **5,536** quadratic candidates, and **154** literal absolute-spectrum groups.
- Exclusion counts **152 / 71 / 28 / 1**, with valid half decomposition, parity, quadratic-residue, Parseval, autocorrelation, and canonical-sign reductions.
- Final certificate: **90 locked / 166 active** positions, **163 equations**, rank **147**, dimension **19**, and all **524,288** distinct parity words. The complete histogram matches: minimum cost **140**, attained six times, exceeds budget **56**.
- Original sources attain balanced **NL240** in every class.

The **31,744-class** conclusion explicitly depends on **31,492 imported exclusions**, which this audit did not reprove. The 154 groups establish neither distinct-function counts nor a full EA classification. Prior tools are credited, published even-half seeds are correctly excluded from odd-spectrum controls, and the symmetric follow-up remains NON_FIND/UNKNOWN.

No proof obligation remains for the 252 balanced-class exclusions beyond the scope clarification above. Arbitrary balanced nine-variable nonexistence remains unproved. Model review is neither peer review nor proof of novelty.

No files were changed, and no delegation was used.