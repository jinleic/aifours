# Mandatory additive union dependency-pin erratum

Owner **InfoBalancedNL242-2-2**, original info-6 slot. Native `/bin/date` observed before write: **2026-10-27T17:28:43-0700 PDT**. This corrects one dependency-table transcription only; it does not edit the pinned union bytes or change any theorem/proof/status.

The frozen `walsh-necessary-conditions-union-v1.md`, SHA-256 `029044731ff7fa2fc07ba10ff14f5b85a85fb39b6b74917dacc746ec6e6e0429`, 199 LF, line 183 gives the wrong SHA-256 for `walsh-odd-divisor-flat-obstruction-v1.md`: the listed suffix contains `...febc0d0b...`. The correct complete source pin, as observed by native `/usr/bin/shasum` before the union write and again when this transcription discrepancy was noticed, is

    path: walsh-odd-divisor-flat-obstruction-v1.md
    sha256: 810805e82d758833c9634cce02c0d521d5b6e51d7f536b32febc0b0b65dd9282
    LF: 29
    bytes: 3827

Any prospective union review or disposition MUST carry this additive correction and use the corrected source bytes; the incorrect line is never an alternative acceptable pin. The source remains author-only/unadopted. This is a documentary pin-transcription finding, not a mathematical verification, clean-provenance claim, new release, or original-target result. All process MAJORs, STOP/HOLD/ZERO/NONINPUT and earlier corrections remain in force.
