# A genuinely cross-member obstruction to real-rooted numerators

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** The two-member phase criterion in `frontier-20261029-cross-member-phase-root-count-criterion-v1.md` gives an exact example where the interval family itself forces nonreal numerator roots, even though no individual parity corner gives the same conclusion from that criterion at the selected two frequencies.

Use the explicit full-width box `frontier-20261028-sturm-band-strict-certificate-case-03-v1.json`, SHA-256 `477bc906fc619c38d588ff92321393eb3f0cb9ac60a45ae9696d5795fb9deb59`; its four actual parity corners are \(a_0,a_1,a_2,a_3\) in the usual \((--),(-+),(+-),(++)\) order. With continuous unwrapped phases starting at zero,
\[
\theta_{a_2}(25)-\theta_{a_0}(14)
>\pi+\frac72\log\frac{25}{14}+\frac1{1000}.
\]
The cross-member criterion at \(n=7,k=0\) therefore proves that **no** common numerator can have all seven roots real. The independent replay also proves, for **each** individual corner \(a_j\),
\[
\theta_{a_j}(25)-\theta_{a_j}(14)
<\pi+\frac72\log\frac{25}{14}-\frac1{1000}.
\]
Thus the same two-frequency, same criterion does not establish this result from any one of the four corners; the strength comes from combining two actual members. This is not a claim that no other frequencies or tests could work on one corner.

The exact checker independently verifies all **28** strict corner Hurwitz determinants and computes rigorous rational phase and logarithm intervals: Machin's identity for \(\pi\), alternating arctangent series with remainder bounds, rational Sturm root counts for unwrapped quadrants, and the positive atanh series with remainder for \(\log(25/14)\). No floating-point angle is used. The box is stable by Kharitonov's theorem. A separate independently replayed exact common numerator for this box is case 3 in `frontier-20261028-sturm-band-batch-simple-frozen-v1.json`, SHA-256 `87827043af153b0ecd5d2ac002bb1095ccd67cb9661c3076f4578e335464b509`; its full pairing and stability replay is `frontier-20261028-sturm-band-batch-independent-result-v1.json`, SHA-256 `6e5b7289eeb9c8f32800e9acb8f8530847e8ea1ce6a4c74b43ef7d0b37659987`. Thus nonreal roots are necessary but unrestricted common synthesis succeeds.

Frozen corner IDs, frequencies and exact-series settings: `frontier-20261029-cross-member-real-root-obstruction-frozen-v1.json`, SHA-256 `3c4670d112845021bb15d9eecfded656455e488650d585f70d3538483ee976ed`. Independent checker `frontier-20261029-cross-member-real-root-obstruction-independent-kernel-v1.py`, SHA-256 `b728db2b664ea15a38436e1d85c545916cc4df77de1244c6789c297b592ba505`; receipt `frontier-20261029-cross-member-real-root-obstruction-independent-result-v1.json`, SHA-256 `8f3846e70e51a0e7b444190833e8f8009d6ec49046f6ea7358b25ab255730298`. The general criterion is SHA-256 `e63f506984a2ea75aeb224eb6b4c1af10b3ff60103d354fa420c5ac7ba4d9b1d`.

The finite comparisons use exact integers and `fractions.Fraction` on one Python Eval host; the phase criterion and cited classical identities are written mathematics. No formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict, or unrestricted negative certificate is claimed.
