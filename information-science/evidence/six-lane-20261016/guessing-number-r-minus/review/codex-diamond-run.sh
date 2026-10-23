#!/bin/zsh
cd "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/guessing-number-r-minus/review"
codex exec -m "gpt-6.1-sol" -c model_reasoning_effort="max" --sandbox read-only --ephemeral --skip-git-repo-check -C "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/guessing-number-r-minus/review/codex-empty-wd" -o "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/guessing-number-r-minus/review/codex-diamond-out.md" "$(cat codex-diamond-prompt.md)" </dev/null > codex-diamond-stdout.log 2> codex-diamond-stderr.log &
CPID=$!
( sleep 3600; kill -TERM $CPID 2>/dev/null && echo "watchdog-killed=$(date '+%Y-%m-%dT%H:%M:%S%z')" >> codex-diamond-receipt.txt ) &
WPID=$!
wait $CPID; RC=$?
kill $WPID 2>/dev/null
echo "exit=$RC end=$(date '+%Y-%m-%dT%H:%M:%S%z')" >> codex-diamond-receipt.txt
