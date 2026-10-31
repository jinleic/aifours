# The required reversed bands force opposite corner orientations

**Status: WRITTEN corollary, not parent adoption.** On any full-width, all-member-Hurwitz monic septic interval box, let a finite **actual parity-corner** atom sum have strictly negative coefficients in all eight numerator coordinates. Then the two reversed root bands required by `frontier-20261029-strict-certificate-two-reversed-bands-all-support-v1.md` (SHA-256 `b0a5a1c2c450f383a3f5c6f69a37f771641007b46e0f7ea21998fabfbaf183b8`) impose the following **time-ordered corner orientations**.

| Reversed band | An atom at an earlier selected node must use | An atom at a later selected node must use |
|---|---|---|
| \(E_q\), \(q\) odd | \(E_-\) | \(E_+\) |
| \(E_q\), \(q\) even | \(E_+\) | \(E_-\) |
| \(O_q\), \(q\) odd | \(O_-\) | \(O_+\) |
| \(O_q\), \(q\) even | \(O_+\) | \(O_-\) |

At least one even-band row and one odd-band row must occur, at disjoint frequency intervals. If several atoms share a frequency, the orientation statement requires **at least one** constituent atom of the indicated kind at that frequency; it does not assert every constituent has that kind. Atoms at zero or infinity cannot supply the required positive-frequency reversal.

## Proof

For \(t>0\), independent full-width intervals give \(E_-(t)<E_+(t)\) and \(O_-(t)<O_+(t)\). Their individual roots form the same globally separated bands. Since every parity polynomial is positive at zero and has simple alternating signs, the lower endpoint's \(q\)-th root occurs first when \(q\) is odd and last when \(q\) is even; the upper endpoint has the opposite root order.

The cited theorem supplies two increasing nodes within one band such that the averaged earlier denominator has already passed its \(q\)-th parity root and the averaged later denominator has not. Suppose the earlier node's constituent atoms all used the parity endpoint whose \(q\)-th root is **later**. That endpoint would already have passed its root, so every endpoint—and every averaged member—would have passed it before the later node, contradiction. Thus at least one earlier atom uses the earlier-root endpoint. The symmetric argument forces the later atom to use the later-root endpoint. Substituting the odd/even root ordering gives the table, separately for the two parities.

This is a necessary restriction on certificate support and its frequency ordering, not a claim that an oriented corner set suffices or that all strict certificates are impossible. The root ordering, averaging and sign arguments are written mathematics; no formal proof, cross-vendor review, novelty clearance, or original verdict is asserted.
