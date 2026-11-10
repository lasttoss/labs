# Lab catalogue

Each entry is a problem I hit, the artifact that answers it, and the command that
proves it. Entries are ordered by date, because the useful signal is not the
technology — it is that the problem was actually closed.

5 entries · 3 flagship · 12 tags

## Flagship

### oom-evidence  ·  2026-11-06

**Problem** — An OOM happens every few months and nobody can prove what held the memory.

**Proved** — 6 reproducible failure modes, 10 classification outcomes, 1 leak reproduced at 99.6% of heap in MAT

**Verify** — `cd ../oom-evidence-lab && make smoke`

**Repo** — https://github.com/lasttoss/oom-evidence-lab

### legacy-revive  ·  2026-11-09

**Problem** — A legacy Spring service has no tests, no maps, and nobody knows what breaks when a file changes.

**Proved** — 0 -> 20 golden tests, 89.2% line coverage with a ratchet gate, endpoint->table map, changed-file impact report

**Verify** — `cd ../legacy-revive-lab && make all`

**Repo** — https://github.com/lasttoss/legacy-revive-lab

### agent-harness  ·  2026-11-10

**Problem** — A team uses an AI agent it cannot inspect: no cost attribution, no budget, no proof a wrong answer is caught.

**Proved** — cache reuse 0 -> 13 tokens on repeat, prefix volatility detected on 6 patterns, budget stops with HTTP 429, cost per request logged

**Verify** — `cd ../agent-harness-lab && make smoke`

**Repo** — _local, not published yet_

## Practice and specimens

### qa-kit  ·  2026-10-20

**Problem** — Test suites report numbers but block nothing.

**Proved** — coverage floor + ratchet, drift check on generated docs

**Verify** — `see repo README`

**Repo** — https://github.com/lasttoss/qa-kit

### idempotent-economy  ·  2026-10-28

**Problem** — Retries duplicate side effects; nobody can say which operations are safe to repeat.

**Proved** — idempotency keys + outbox pattern, duplicate-suppression test

**Verify** — `see repo README`

**Repo** — https://github.com/lasttoss/idempotent-economy

## Tags

- `ai-harness` — agent-harness
- `backend` — idempotent-economy
- `ci` — qa-kit
- `cost` — agent-harness
- `evidence` — oom-evidence
- `jvm` — oom-evidence
- `legacy` — legacy-revive
- `observability` — oom-evidence
- `platform` — agent-harness
- `reliability` — idempotent-economy
- `testing` — legacy-revive, qa-kit
- `toolkit` — legacy-revive
