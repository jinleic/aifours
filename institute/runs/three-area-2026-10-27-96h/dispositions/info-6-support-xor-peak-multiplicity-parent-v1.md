# Parent disposition — info-6-support-xor-peak-multiplicity-parent

Observed clock before writing: **2026-10-27T15:12:12-0700 PDT**. Same-harness written disposition; not formal/kernel, human, configured-family, executable or novelty acceptance. Independent-model CLI review not performed.

## Complete parent reads and applicable chain

- Author: [walsh-support-xor-obstruction-v1.md](/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/walsh-support-xor-obstruction-v1.md), SHA256 `380655caaa06ea27e4236070ff66e070be63963960efebfabef2e730d2091fc4`, 49 LF; Main read raw LF1–25 and LF26–49 through the ending.
- Reviewer PhysicsAME46-2: [w13 review](/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/review-w13-info-6-xor-v1.md), SHA256 `fad45bbd3a2d86500f50c400ab9a5d5ae76f210dd6c186db1199fb8a6419653b`, 117 LF; Main read raw LF1–39, LF40–78 and LF79–117 through ending. Verdict 0 FATAL / 0 MAJOR / 1 MINOR. This is same-harness cross-domain supplied-proof review with disclosed prior contact, not blind or independent-model review.
- The definition-first Walsh caller and parity conditions are used at [parent disposition](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-6-walsh-caller-and-mod4-coupling-parent-v1.md) AND [mandatory coverage addendum](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-6-walsh-caller-and-mod4-coupling-parent-coverage-addendum-1.md); no historical L>=18/L>=12 chain is input.

## Mandatory correction to two author statements

Author LF33 and LF39 reverse two complementary-count directions. If q<=384, the number of nonzero Q=0 frequencies is exactly 511-q, not necessarily at most 127; if q<=192 on T-perp, it is exactly 255-q, not necessarily at most 63. The reviewer’s coupled maximizations replace both statements: 36q+16(511-q)<=36·384+16·127, respectively 36q+16(255-q)<=36·192+16·63. This is one MINOR with two sites; frozen author bytes remain unchanged. The corrected inequalities, not the incorrect individual count bounds, are mandatory inputs.

## Parent hand checks (written)

1. On every subspace K of T-perp, k is even and Q=k/2 mod 2 is quadratic with Q(0)=0. Thus 1+Q is a nonzero Boolean polynomial of degree at most two; the stated induction gives at least |K|/4 zeroes of Q.
2. For T=0, |k|<=7 implies |k|<=6. With q<=384 and k(0)=0, energy is at most 36q+16(511-q)<=15856, contradicting Parseval energy 16384.
3. For T!=0, K=T-perp has 256 points. Its energy is at most 36·192+16·63=7920. In the other 256 frequencies k is odd, and n7 entries of magnitude 7 give total energy at most 7920+25·256+24n7=14320+24n7. Parseval forces 24n7>=2064, hence n7>=86.

## Adopted at exact scope: WRITTEN_SUPPORTED

For every balanced Boolean f:F_2^9→{0,1} with every Walsh coefficient of magnitude <=28, the XOR T of its truth support is nonzero and at least 86 Walsh coefficients have magnitude exactly 28. Consequently every balanced f with T=0 has Walsh peak >=32 and nonlinearity <=240. These conclusions are necessary, not sufficient, and use the correction above.

## Not established

No balanced NL>=242 witness, no exclusion of T!=0, no unrestricted upper-bound improvement, no closure of any named rank or (24,24,2) case, no novelty/priority or source-equivalence claim. The proposition and its elementary coding-theory ancestry need literature comparison; novelty UNCLEAR. All S1/HOLD/ZERO findings persist. Formal, executable, human and independent-model acceptance not performed.
