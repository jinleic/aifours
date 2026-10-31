# Parent disposition — info-6-walsh-caller-and-mod4-coupling-parent

Observed clock before writing: **2026-10-27T14:59:45-0700 PDT**. Same-harness written disposition; not formal/kernel, human, configured-family, executable or novelty acceptance. Independent-model CLI review not performed.

## Inputs read completely by Main

- Author: [prerequisite-derivation-v1.md](/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/prerequisite-derivation-v1.md) SHA256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF, read raw LF1–87 including ending.
- Review w4 by InfoHinfPreview-2 (same information-science track, disjoint slot): [review](/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/stochastic-hinf-preview/review-w4-nl242-walsh-coupling-v1.md) SHA256 `7d606890133f5186c3d662d1e920383147bf18a9cf78e308cd1a8f2c0b9fdefd`, 80 LF, read raw LF1–80 including ending; 0 FATAL / 0 MAJOR / 0 MINOR.

## Parent hand checks (written)

1. With s=1-2·1_M and |M|=256: sum over M of chi_a = 256-2n_a, so W(a)=512·1_(a=0)-512+4n_a; k=W/4 is an integer with k(0)=0.
2. Converse of (4): the character transform K of k satisfies K(x)^2 = sum_b R(b)chi_b(x) = 2^14, so K(x)=±128 at every x and s=K/128 is an actual sign array with Walsh spectrum 4k.
3. (6): k(a) ≡ n_a ≡ sum over M of (a·x) ≡ a·T (mod 2), since the constant correction is a multiple of 4.
4. (9): reducing sum k^2 = 2^14 mod 16 with odd support of size 0 or 256 gives 4(E2+2O3) ≡ 0 (mod 16).

## Adopted at exact scope: WRITTEN_SUPPORTED

(a) Exact original-object caller: a balanced nine-variable Boolean function with nonlinearity >= 242 exists IFF there is an integer array k on F_2^9 with k(0)=0, |k|<=7 everywhere and sum_a k(a)k(a+b)=2^14·1_(b=0) for EVERY b. (b) Necessary conditions for EVERY balanced f: the common mod-4 moment form (5); odd support of k is empty or an affine hyperplane {a·T=1} (6); vanishing third differences mod 4 and the bilinear polarization (7)–(8); and, under the peak bound, E2+2O3 ≡ 0 (mod 4) (9).

## Not established; status

No witness, no unrestricted exclusion, no rank/weight or (24,24,2) exclusion, no numerical improvement. The filters' converse is not claimed. Novelty UNCLEAR: Walsh/Parseval, divisibility of balanced Walsh values by 4 and quadratic mod-4 structure are close to classical facts; no literature comparison was performed. Original target OPEN. All STOP/HOLD/ZERO/process findings persist; the old L>=18/L>=12 chains remain author-only.
