# GB necessity / genuine-bridge / adapter — review erratum r1 (x-created)

Applies the three textual MINOR fixes of Codex review `R/n8-gb-necessity-bridge-codex-v1.note.md`, SHA256
`ad9e5f04e9eedcf0f5daaf612010b3bd0fa6e86f786dbcbb3412fe8fe44113fc`. That review found no FATAL or MAJOR issue:
- GB necessity: ACCEPT;
- genuine NF bridge: ACCEPT-WITH-FIXES;
- adapter: ACCEPT-WITH-FIXES.

The target files are preserved unchanged:
- `review/GB_NF_GENUINE_BRIDGE.r1.md`, SHA256 `1a352d364a2e2c68a344735537db7e6f10861e01d520cf75dcbef7a61fbf504b`;
- `review/GB_ONE_P4_NECESSITY.r2.md`, SHA256 `b9b4a595ca50b1334419d8584edc128e852dd4f206cd21fc5a07a793a2e72365`.

Read each listed line through the replacement below. These are wording/scope corrections only. No code, flag, byte convention, formula, hash or receipt changes; the GB adapter (`5ca7c0da…e262`), the GB encoder (`4b593e55…eae0`), the 22 input identities and the GB worker receipts stay as frozen. The Claude review is still pending. This erratum is mathematical/encoding text only. It is not a GB refutation acceptance, proof certification or n=8 gate.

## E1 — bridge r1, LF15 (ROWLEX domain)
Original:
> - **ROWLEX:** the rows are sorted ascending non-strictly by Q_1's column-0 support key.

Replacement:
> **ROWLEX:** rows 2–7 are sorted ascending, non-strictly, by the Q1 column-0 support bits in coordinate order 0,…,7, coordinate 0 most significant, False < True, with no secondary key. Rows 0 and 1 are fixed.

## E2 — bridge r1, LF17 (sixteen-template coverage vs. four-template setting)
Original:
> By U and T16 (accepted, `N8_ASSEMBLY.r2.md` §§2–3), every genuine non-classical five-set reaches such a configuration for one of the sixteen templates.

Replacement:
> By accepted U and T16, every genuine non-classical five-set reaches row-0 standard form, SB2 and ROWLEX with one of the sixteen templates. For the following argument, condition on its template belonging to {P1-B1, P1-B2, P1-B3, P1-B5}.

The "Template" bullet at LF14 restricts C to these four. It is read as the conditioning hypothesis introduced by E2, not as a claim that U/T16 produce only these four.

## E3 — necessity r2, LF84 (allocator wrapper)
Original:
> The GB file is unchanged. The adapter subclasses only its clause-storage F: F.new/encode are inherited without

Replacement:
> The GB file is unchanged. `encode` is unchanged. `Sink.new` delegates allocation unchanged to the original `F.new` and adds control bookkeeping; `Sink.c` replaces clause storage with the original CLI serialization.

The rest of LF84–85 stands as written: `Sink.c` writes exactly `join(str(lits)) + ' 0\n'` into a RAM bytearray.

## Scope
With E1–E3, the review's conditional conclusion is unchanged:
- The accepted U/T16 imports remain the conditions.
- Every normalised genuine configuration yields a GB assignment.
- Every genuine configuration in a hard P1 template reaches one of its six strengthened GB inputs, so UNSAT of all six would exclude those genuine configurations.

The erratum adds no arbitrary-GB-model transformation, solver result or gate closure.
