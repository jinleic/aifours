#!/bin/zsh
cd "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/guessing-number-r-minus/review"
codex exec -m "gpt-6.1-sol" -c model_reasoning_effort="max" --sandbox read-only --ephemeral --skip-git-repo-check -C "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/guessing-number-r-minus/review/codex-empty-wd2" -o "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/guessing-number-r-minus/review/codex-phi-out.md" "$(cat codex-phi-prompt.md)" </dev/null > codex-phi-stdout.log 2> codex-phi-stderr.log &
CPID=$!
( sleep 3600; kill -TERM $CPID 2>/dev/null && echo "watchdog-killed=$(date '+%Y-%m-%dT%H:%M:%S%z')" >> codex-phi-receipt.txt ) &
WPID=$!
wait $CPID; RC=$?
kill $WPID 2>/dev/null
echo "exit=$RC end=$(date '+%Y-%m-%dT%H:%M:%S%z')" >> codex-phi-receipt.txt
