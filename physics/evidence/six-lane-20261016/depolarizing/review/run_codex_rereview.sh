#!/bin/bash
# Clean configured-delegate re-review of the frozen v3 proof + code + v3 results. Captures exit code.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
P="$HERE/codex-packet-v3"
DM=/Users/jinleic/jinleic-workspace/docs/knowledge-system/DELEGATE_MODELS.json
MODEL="$(jq -r .codex.model "$DM")"; EFFORT="$(jq -r .codex.effort "$DM")"
date '+%Y-%m-%dT%H:%M:%S%z' > "$HERE/codex-rereview-v3.started"
codex exec -m "$MODEL" -c model_reasoning_effort="$EFFORT" --sandbox read-only --ephemeral --skip-git-repo-check \
  -C "$P" -o "$HERE/codex-rereview-v3.json" --output-schema "$HERE/codex-review-schema.json" \
  "$(cat "$HERE/codex-rereview-v3-prompt.txt")" </dev/null > "$HERE/codex-rereview-v3.stdout" 2> "$HERE/codex-rereview-v3.stderr"
rc=$?
{ echo "{\"exit_code\": $rc, \"finished\": \"$(date '+%Y-%m-%dT%H:%M:%S%z')\", \"requested_model\": \"$MODEL\", \"requested_effort\": \"$EFFORT\","
  echo " \"header_model\": \"$(grep -m1 '^model:' "$HERE/codex-rereview-v3.stderr" | cut -d' ' -f2-)\","
  echo " \"header_effort\": \"$(grep -m1 '^reasoning effort:' "$HERE/codex-rereview-v3.stderr" | cut -d' ' -f3-)\","
  echo " \"header_sandbox\": \"$(grep -m1 '^sandbox:' "$HERE/codex-rereview-v3.stderr" | cut -d' ' -f2-)\","
  echo " \"output_sha256\": \"$(shasum -a 256 "$HERE/codex-rereview-v3.json" 2>/dev/null | cut -d' ' -f1)\"}"; } > "$HERE/codex-rereview-v3.receipt.json"
