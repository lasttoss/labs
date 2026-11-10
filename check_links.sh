#!/usr/bin/env bash
# Manual check: every published repo URL in the catalogue must answer 200.
# Not in CI on purpose (network flakiness must not fail a docs check), but run it
# before sharing the catalogue, because one dead link is worse than ten missing ones.
set -uo pipefail
cd "$(dirname "$0")"
fail=0
while read -r url; do
  code=$(curl -s -o /dev/null -w '%{http_code}' -m 12 "$url")
  printf '%s  %s\n' "$code" "$url"
  [ "$code" = "200" ] || fail=1
done < <(grep -oE 'https://github\.com/[^ "]+' catalog.yaml | sort -u)
exit "$fail"
