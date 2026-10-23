# gcDCQS(20⁴:0), mcDSQS(80) and χ′(79): parent Lean verification

## Result and exact scope

The accepted finite existence results now also have **parent-replayed Lean4.34.1 kernel proofs**:

- gcDCQS(20⁴:0), specifically certificateA SHA`58b51b50b5281df613c5fae0a3b0178a374554a2f062e55bd8fc25250922a0ca`, with19,400blocks and all80derived incomplete STS(79,19) designs40-coloured, exactly10classes avoiding the hole at every point.
- mcDSQS(80), SHA`49f500c5eedd9a79553e1228d0232e203a749bbda04e3a891c52778dbe9d44a3`, with20,540blocks and all80derived STS(79) designs40-coloured.
- χ′(79)=40: a data-independent lower bound over every STS on every79-element type (1027triples, at most26per class,39·26<1027), plus an explicit40-colour STS witness from the mcDSQS certificate.

This adds verification to the [existing direct verdict](gcdcqs20-parent-verdict.md), not a new construction. CertificateB remains directly verified by the earlier independent checkers; it is not part of this Lean package. **Tan–Zhou's recursive constructions and the infinite family mcDSQS(5·4ⁿ), n≥3, are not formalized.**

## Parent statement binding

The parent independently wrote [ParentAudit.lean](gcdcqs20-lean-parent-audit-v2/ParentAudit.lean), using Mathlib notions rather than trusting a development-specific target name:

- Its four groups use y.val/20=i, independently of the worker's interval filters. Kernel-checked equality identifies the two definitions.
- Its gcDCQS proposition requires a partition into the four20-point groups;4-subset blocks; exact coverage of every3-subset not wholly in a group; no group3-subset in a block; at every point, the incomplete STS with the prescribed19-point hole; and a partition of its triples into40nonempty partial parallel classes, exactly10avoiding the hole.
- χ′(79) is restated explicitly as the infimum of the numbers of classes of colourings of STS(79), not a numeral substituted into a definition. The kernel proves40 and the good-colouring parameter40−(79−19)/2=10.
- The mcDSQS proposition requires an SQS(80) and a colouring of the derived design at **every** point with exactly that minimum number of colours.

The parent module typechecks against the worker's unfolded roots. All five printed parent declarations depend only on`propext`, `Classical.choice`, `Quot.sound`.

## Observed verification

| Check | Result | Limit |
|---|---|---|
| Source/raw pins | All51worker manifest files and both raw hashes match ([rebuild receipt](gcdcqs20-lean-parent-audit-v2/parent-result.json)) | Worker package has its own retained history; parent uses copied sources |
| Fresh parent rebuild | Every required module rebuilt, including160per-point`decide +kernel`checks and the parent binding | Compiler/runtime/hardware trusted |
| Independent raw-to-Lean parse | Parent stdlib parser checks all39,940block tuples,159,760derived triple tuples,6400classes,160POINT sections and fourGROUPS lines in order, plus exact aggregate reference ordering ([script](gcdcqs20-parent-literal-binding-v1.py), [receipt](gcdcqs20-parent-literal-binding-v1.json)) | Literal binding, not a replacement design verifier |
| Binding controls | Five in-memory corruptions reject for intended BLOCKS/CLASS/GROUPS mismatch; two parent Lean statement mutations (11hole-free classes,41colours) reject with type mismatch and no olean | Worker has additional controls, not counted as parent executions |
| Generator replay | All20literal modules regenerate byte-identically from the parent-pinned raw certificates | Same generator; separate parent parser supplies independent literal comparison |
| Parent source/axiom audit | Comment-aware forbidden-token scan clean; standard axioms only for parent statements | Comments that say native_decide/ofReduceBool are not executable uses |
| **Fresh kernel replay** | `leanchecker --fresh -v ParentAudit` exits0,1014.083s, maximum RSS5,043,912,704bytes ([fresh result](gcdcqs20-lean-parent-audit-v2-fresh/parent-result.json)) | lean and leanchecker use one Lean kernel implementation, not Comparator or an independent external kernel |

The existence proof does not depend on SAT results, symmetry or a particular colouring profile; every finite condition is checked. The direct independent raw-design checkers and their controls remain the earlier correctness evidence.

## Retained failures and procedure limits

- Parent v1 stopped before builds because its line-based token scan matched doc comments explicitly saying native_decide/ofReduceBool were **not** used. v1 is retained; v2 strips Lean comments and reports comment mentions separately.
- Parent v2 completed every build, binding and negative control but its fresh-kernel invocation failed because leanchecker could not find`lean`on PATH. Only that failed step was rerun with corrected PATH, using the parent-built oleans read-only; the fresh-only receipt binds the v2 receipt and ParentAudit.olean hash.
- Worker disclosed an accidental`leanchecker --help`replay reaching14GB before SIGTERM; this breached the8GiB limit and is not accepted evidence. Successful parent fresh replay stayed below the cap.

**FRONTIER: finite proofs KERNEL-VERIFIED by parent rebuild, independently parsed raw binding, statement/axiom audit and fresh replay; NOVELTY-UNCLEAR, unchanged from the direct verdict. No claim of formalized recursion or infinite family.**

No publication, external contact, commit or push was authorized.
