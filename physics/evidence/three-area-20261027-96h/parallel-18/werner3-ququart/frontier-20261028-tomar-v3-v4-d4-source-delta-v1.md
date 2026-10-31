# Tomar v3 → v4: original d4 certificate source delta

**PhysicsResearch96h-2 / physics-1.** Native clock before writing **Wed Oct 28 17:44:00 PDT 2026**. This records only the observed public-version and d4-source differences relevant to the existing certificate work. It does not review the entire v4 manuscript, its all-d>=9 proof, other-copy claims or Lean artifacts.

## Public version and bound bytes

The version-specific v3 registry is [Zenodo 23682914](https://zenodo.org/records/23682914). At the current observation, its public latest-version endpoint redirects to [Zenodo 23718035](https://zenodo.org/records/23718035), issued2026-10-28, relation `is_last=true` in [the primary record API](https://zenodo.org/api/records/23718035). The author calls the later record version4 in the version sequence; the locally pinned earlier paper was version3.

Downloaded actual v4 files:

- `frontier-20261028-tomar-v4-paper.pdf`, SHA256 `07acff7153eb72f9ea80446dfb936eb40a93b0dcd82cf48d04813def9b392438`; MD5 `71001306e2f8c138028b6b4b237ae7d5` matches the v4 registry.
- `frontier-20261028-tomar-v4-supplement.pdf`, SHA256 `0c20f7a0319c2a23240775386ff2c826a3abdeb100e6a349c10f471b247873c8`; MD5 `dbbec22ae2673691d521ee01e035d5bb` matches the v4 registry.
- `frontier-20261028-tomar-release-ep3-v4.tar.gz`, SHA256 `2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3`. Actual `cmp -s` against the separately downloaded v3 archive returned `EXACT_BYTES_EQUAL`; both have that SHA256 and the registry-listed size11,746,154 bytes. Thus our checked d4 certificate member and source archive are exactly the same bytes in both observed records, not merely similar filenames or an MD5 inference.

The new registry also lists a `release_ep3_checks.tar.gz` of about2.49GB. It was **not downloaded, executed or inspected**. No additional paid API, external model, publication or author contact occurred.

## Exact relevant printed scope

The v4 paper's Theorem1.2 on p2, visually read in `frontier-20261028-tomar-v4-page-02.png`, SHA256 `dcf2b10d976f152e3388a168ba3c35af646323e7ab7b64ed161dccb239c532e8`, still states q3(C)>=0 for every rank<=2 C on three finite-dimensional Hilbert spaces, with the same sum of `(-1/2)^|J|` times squared Frobenius norms of the corresponding partial traces. The original `(C^4)^tensor3` target is included. The source claim is not independently accepted just by this comparison.

The v4 p4–6 images were rendered from the pinned v4 PDF and visually read:

- p4 SHA256 `7c53ebe486437f7150f5da3feb88e230dbaf133be2c42939888f6a60f9d10495`: normalized `||C||_F²=1/2`, `A` isometry, `B=2C†A`, vectors divided by sqrt2 and **conjugated b** in `C_xy=Σ a_xr conjugate(b_yr)`; same physical moment families and normalization as the checked v3 package.
- p5 SHA256 `ab81131a7b3dae0a5f5fb1164f97e8b9660cf99348d4c1c80253bee7346112ec`: complete Gram-class lemma and actual coupled row patterns, including the conjugations lost by PDF text extraction.
- p6 SHA256 `ba458b70136affdf77ced02846e97a043c1cabb10ff91c83042cc6eaccc13312`: Stiefel contrasts, common-marginal orderings, swap objective, exact certificate identity and its conditional validity statement.

These are a **bounded relevant-section comparison**, not a claim of a complete independent review of every p4–6 dependency or the rest of v4. Our proof bridge and actual independent d4 identity/PSD remain the evidence of record.

## Sharpness qualifier and proof-route change

On v3 p2 the text following Theorem1.2 says “Moreover, the constant 1/2 cannot be increased, and equality occurs” and then describes a rank-two projector and two pairs of orthogonal unit vectors. On v4 p2 the corresponding sentence begins **“If every H_i has dimension at least two”** before the sharpness/equality construction. This is a genuine source wording/hypothesis qualification for the sharpness clause, not evidence that the q3 inequality is false. The original d4 factors all meet this explicitly added condition. This comparison does not claim a general sharpness classification outside that condition.

V3 Section4/Proposition4.1 routes small dimensions through exact fixed-dimensional certificates; its AppendixA V17 unqualified count description conflicted with the actual d3/d4 type counts. V4's main proof (§5 and its stated padding route) uses the claimed uniform d>=9 certificate to obtain lower dimensions, while fixed-dimensional certificates are presented as separate verification in the supplement. The v4 supplement §S2/TableS2 explicitly says d3 has715 multipliers (R4) and d4 has1237 (R5), agreeing with the actual unchanged archive. This corrects the relevant count description in the later source; the v3 documentary discrepancy remains historical. Our d4 proof does **not** depend on verifying the separate uniform d>=9 route.

## Limits

The two d4 certificate archives are byte-identical and the displayed relevant v4 physical definitions/claims match the checked v3 data. Actual independent d4 computations are recorded in `frontier-20261028-d4-certificate-bridge-and-independent-identity-v1.md`, `frontier-20261028-d4-certificate-verification-addendum-v1.md` and `frontier-20261028-d4-crt-certificate-identity-proof-v1.md`, plus the finite commutant witness and their pinned scripts/results. The version comparison is not itself a certificate proof or source-wide adoption.

No all-d>=9 certificate/padding computation, 2.49GB supplemental verifier package, Lean kernel run, physical distillability criterion, external/human/model-family review, novelty/priority or parent acceptance is claimed. The published preprint claim predates our local work; old quarantined outcomes remain historical/unvalidated and are not premises.
