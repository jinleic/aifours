# Ordered Olson: imported S(p), ROT-KP+, and length-sensitive reductions

Recorded at 2026-10-19T03:53:21-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIAL**, relative to the explicitly recorded classical imports. No unrestricted ordered-Olson or LS/LS+ theorem is claimed.

## Accepted statements
1. **S(p), a classical corollary, not a new result:** for every prime p>=5, every zero-sum-free sequence of p odd elements of C_(2p) has positive coefficient sum <=2p-1 relative to some generator. Equivalent to index1 for every all-odd minimal zero-sum of lengthp+1. Xia-Yuan2010 classification is imported through Peng-Sun2014; primary proof unread. SPLIT is proved in the note. [Parent source-range check](olson-Sp-import-range-parent-v1.json) resolves the even-n applicability for all these p at secondary-statement trust level.
2. **FB-p and ARC0**, at their exact candidate hypotheses, including FB-p's no-zero-sum-of-length2p condition and its exceptional complement g^(p-1)(pg).
3. **ROT-KP+:** primep>=7, an avoider of length4p-2 with an admissible normal form of terminal k=p, kappa-hat>=1, satisfying(S1) at kappa-hat, has all rotation letters in one nonzero pair. The S(p) step is no longer an open conjectural premise. The uniform corollary proves INV* for avoiders with o_F<=p and kappa(w)<=floor(2p/3), and an ordered identity2p-subword for length4p-1 words with o_F<=p and F-o_F>=2(p-1-floor(2p/3)).
4. **SLZ/EXT/PROP/RED:** for0<=kappa<=p-2, SLZ bounds a shortest long zero-sum by p+2kappa+1 under(ZP_kappa). EXT extends(S1_kappa) from Y1 to Y1y when |Y1|>=p+2kappa and its longest-zero-sum complement has length>=p+1, provided Y1y satisfies(ZP_kappa). PROP and RED have exactly the threshold/endpoint scopes in the amended source: kappa0 follows Davenport separately; they reduce LS to length p+2kappa+1, not prove LS.

## Frozen texts and mandatory overlays
- [import-Sp-XiaYuan-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/import-Sp-XiaYuan-v1.md) `d4d515cd4ff7b848d703f9337a3e9b6f12f85bd99319173207014519961381d7`; overlay [import-Sp-XiaYuan-v1-erratum-1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/import-Sp-XiaYuan-v1-erratum-1.md) `df1c5ac2dba4f088b6aa402a1e1c1e9037063230a37776d8f50b704997c87269`.
- [proof-KPS-v4.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-KPS-v4.md) `68c4e7a7ff898219bfebee028052415cdb785b4b460b87e5cd4e7a6370510170`; overlay [proof-KPS-v4-erratum-1-v2.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-KPS-v4-erratum-1-v2.md) `3ef936f19d2dc9eabadc8684ea842e19a92df2534fb582b11bb302b8375aa80b`.
- [proof-SLZ-EXT-v2.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-SLZ-EXT-v2.md) `2495300317299fda49c0fb7d4b22daa81dfcecf1aef8c161361b9c04861bd751`; overlay [proof-SLZ-EXT-v2-erratum-1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/evidence/proof-SLZ-EXT-v2-erratum-1.md) `907b3d06dd2ac93686ea4f49cf812dfd41f80f9abdefa6fd2d4398821c234daa`.

Read source and overlay together. The import overlay's estimated IRC time is not evidence and is withdrawn by this verdict; only its host-clock creation label and the separate parent source-read record are used.

## Verification
- [Codex](olson-kps-slz-codex-v1.prompt.stdout.txt) `6ce69cb0eb1a2e23b9edff9d85868e17278adfbb1dd4943e9388380cef102408`: accepts all mathematics,3minor SLZ/EXT findings.
- [Claude](olson-kps-slz-claude-v1.prompt.note.md) `c98dc2f491e739d374329d2489218a81837512e03b979714cdb57287f1bda3bd`: all correct with8requiredminor and2editorial fixes. No fatal or major findings from either.
- Parent independently re-derived FB-p gap/balance and equality corner, ARC0 interval coverage, KPS(H)/(K) including eta1, SLZ/EXT descent and unit availability, and PROP/RED. All overlays read. [Original SHgen definitions](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-SHgen-v3.md), lines39-42, confirm eta counts heavy letters of both signs, a_max=max|b|, E=sum(|b|-1). ROT-ZR and ROT-KP caller scopes remain distinct.
- [Finite import controls](olson-sp-import-parent-control-v1.json) are consistency checks only, not theorem premises. No new scientific computation is a premise of this packet.

## Remaining scope and priority
Full ordered Olson, unrestricted INV*(p), reflection half o_F>p and remaining rotation cells stay OPEN. LS, LS+ and STAB remain conjectures. SLZ3 and later LS+ partials are separate pending candidates. Mathematical verification is written and model-reviewed only, not Lean or human peer review. S(p) is classical; S1-sharp has the recorded Zeng-Yuan overlap; no novelty clearance is inferred from the bounded literature screen.
