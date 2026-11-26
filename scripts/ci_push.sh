#!/usr/bin/env bash
# Commit generated files and push them to main, retrying if main moved in the meantime.
# usage: ci_push.sh "commit message" "paths to add" ["command that regenerates the files"]
#  - with a command: every attempt starts from the latest origin/main and regenerates, so a stale checkout can never fail
#  - without one:    commits what is already in the working tree, then rebases onto the latest main before pushing
set -euo pipefail
msg="$1"; paths="$2"; gen="${3:-}"
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

if [ -z "$gen" ]; then
  git add $paths
  if git diff --cached --quiet; then echo "Nothing to commit"; exit 0; fi
  git commit -m "$msg"
  for attempt in 1 2 3 4 5; do
    if git pull --rebase origin main && git push origin HEAD:main; then exit 0; fi
    echo "Push rejected (attempt $attempt), retrying..."; git rebase --abort 2>/dev/null || true; sleep $((attempt * 7))
  done
  exit 1
fi

for attempt in 1 2 3 4 5; do
  git fetch origin main
  git reset --hard origin/main
  bash -c "$gen"
  git add $paths
  if git diff --cached --quiet; then echo "Nothing to commit"; exit 0; fi
  git commit -m "$msg"
  if git push origin HEAD:main; then exit 0; fi
  echo "Push rejected (attempt $attempt), retrying on the latest main..."; sleep $((attempt * 7))
done
exit 1
