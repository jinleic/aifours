# Prebody acknowledgment transport deviation — f827

The manifest's `direct_prebody_ack_required` required a direct acknowledgment to Main in addition to the local file. I did **not** send that direct acknowledgment before reading the packet. The actual sequence was:

1. I read the full manifest, freeze receipt, final binding, supplied metadata, actual dispatch receipt and all 22 status-only controls.
2. I wrote the exclusive local `prebody-ack-v1.md` before any mathematical packet-body access or mathematical reasoning.
3. I read all 408 LF of the single packet in ordered raw windows through its ending, then undertook mathematical reasoning and wrote `author-candidate-v1.md`.
4. Main's administrative clarification arrived afterward. I then sent Main an explicitly qualified direct acknowledgment stating that delivery was late, and wrote this note. No exact timestamp or earlier direct delivery is asserted.

The wording in candidate §7, “I wrote the direct `prebody-ack-v1.md` first,” refers only to the local file and must **not** be read as claiming that a separate direct message was sent before body access. The local-file-before-body and complete-packet-before-reasoning facts remain as stated; the separate direct-message sequencing requirement was not met. Main described this factual pattern as an ACK-transport PROCESS MINOR, not an automatic source-order mathematical hold; no self-acceptance follows. The candidate and original acknowledgment remain unchanged, and this note is additive. There was no sibling mathematical input or change in the no-child-execution rule.
