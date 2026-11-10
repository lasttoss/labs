# Lab catalogue

Each entry is a problem I hit, the artifact that answers it, and the command that
proves it. Entries are ordered by date, because the useful signal is not the
technology — it is that the problem was actually closed.

17 entries · 3 flagship · 20 tags

## What I keep working on

Four recurring problems. Each line is a claim; the entries under it are the evidence.

**Evidence-first debugging** · 2 — I do not accept 'it might be memory' as an answer. I reproduce the failure, capture the artifact, and classify it.

- `oom-evidence` · 2026-11-06 · 6 reproducible failure modes, 10 classification outcomes, 1 leak reproduced at 99.6% of heap in MAT
- `go-log-api` · 2026-09-10 · 4-step smoke: health, batch accepted, bad event rejected with a reason, oversized batch refused with 413

**Change a legacy system without breaking it** · 1 — Before changing code nobody understands, I record its behaviour, map what depends on what, and gate the merge on both.

- `legacy-revive` · 2026-11-09 · 0 -> 20 golden tests, 89.2% line coverage with a ratchet gate, endpoint->table map, changed-file impact report

**AI as infrastructure, not magic** · 4 — If a team runs an agent, the team must be able to attribute its cost, cap it, and prove when its answer is wrong.

- `agent-harness` · 2026-11-10 · cache reuse 0 -> 13 tokens on repeat, prefix volatility detected on 6 patterns, budget stops with HTTP 429, cost per request logged
- `hubgate` · 2026-10-15 · 3 gates in fixed order (approval -> skill policy -> tool grants), 7 test files, each gate answered by a different owner
- `job-search` · 2026-10-10 · 3 deterministic filter layers at zero cost before any LLM call, 40 test files, blacklist and stale-posting rules written down
- `voicekit` · 2026-10-07 · WER on real meeting audio 5.08% (was 12.18%), fully local, no cloud, 248 test files, no cloud and no API key

**Correctness that blocks, not reports** · 7 — A number in a report changes nothing. A number that fails the build changes behaviour.

- `agent-harness` · 2026-11-10 · cache reuse 0 -> 13 tokens on repeat, prefix volatility detected on 6 patterns, budget stops with HTTP 429, cost per request logged
- `legacy-revive` · 2026-11-09 · 0 -> 20 golden tests, 89.2% line coverage with a ratchet gate, endpoint->table map, changed-file impact report
- `cicd-ai-reference` · 2026-10-30 · small app kept deliberately boring; 3 CI workflows and 16 make targets make the pipeline executable end to end, incl. qa-report and rollback
- `qa-kit` · 2026-10-25 · every release candidate emits reports/qa-<version>.md: what was verified, what could not be verified, where a human looks first
- `tech-radar` · 2026-09-28 · rubric written down and unit-tested, offline demo on recorded signals, 7 test files, Go standard library only
- `idempotent-economy` · 2026-09-20 · 10,000 operations applied twice: the second pass writes nothing; race test with 200 deliveries of one operation
- `zinx-server` · 2026-09-05 · one live session per account enforced through Redis, 11 test files, one-command smoke over the TCP protocol

## Flagship

### agent-harness  ·  2026-11-10

**Problem** — A team uses an AI agent it cannot inspect: no cost attribution, no budget, no proof a wrong answer is caught.

**Proved** — cache reuse 0 -> 13 tokens on repeat, prefix volatility detected on 6 patterns, budget stops with HTTP 429, cost per request logged

**Verify** — `cd ../agent-harness-lab && make smoke`

**Repo** — https://github.com/lasttoss/agent-harness-lab

### legacy-revive  ·  2026-11-09

**Problem** — A legacy Spring service has no tests, no maps, and nobody knows what breaks when a file changes.

**Proved** — 0 -> 20 golden tests, 89.2% line coverage with a ratchet gate, endpoint->table map, changed-file impact report

**Verify** — `cd ../legacy-revive-lab && make all`

**Repo** — https://github.com/lasttoss/legacy-revive-lab

### oom-evidence  ·  2026-11-06

**Problem** — An OOM happens every few months and nobody can prove what held the memory.

**Proved** — 6 reproducible failure modes, 10 classification outcomes, 1 leak reproduced at 99.6% of heap in MAT

**Verify** — `cd ../oom-evidence-lab && make smoke`

**Repo** — https://github.com/lasttoss/oom-evidence-lab

## Practice and specimens

### cicd-ai-reference  ·  2026-10-30

**Problem** — A pipeline is reviewed by reading YAML, so nobody can tell whether the workflow actually gates anything.

**Proved** — small app kept deliberately boring; 3 CI workflows and 16 make targets make the pipeline executable end to end, incl. qa-report and rollback

**Verify** — `cd ../cicd-ai-reference && make smoke`

**Repo** — https://github.com/lasttoss/cicd-ai-reference

### qa-kit  ·  2026-10-25

**Problem** — Testers get a URL and 'please test everything'; no one says what the machine already checked.

**Proved** — every release candidate emits reports/qa-<version>.md: what was verified, what could not be verified, where a human looks first

**Verify** — `cd ../qa-kit && make qa-report`

**Repo** — _local, not published yet_

### hubgate  ·  2026-10-15

**Problem** — An internal AI hub had no answer to: who may work, through which skill, with which tools.

**Proved** — 3 gates in fixed order (approval -> skill policy -> tool grants), 7 test files, each gate answered by a different owner

**Verify** — `cd ../hubgate && make demo`

**Repo** — _local, not published yet_

### job-search  ·  2026-10-10

**Problem** — Job scanning burns model tokens on postings that are already dead, wrong city, or excluded by hard rules.

**Proved** — 3 deterministic filter layers at zero cost before any LLM call, 40 test files, blacklist and stale-posting rules written down

**Verify** — `cd ../job-search && make test`

**Repo** — _local, not published yet_

### voicekit  ·  2026-10-07

**Problem** — Meeting notes in English are useless to me if the transcript is wrong, and cloud ASR is not allowed.

**Proved** — WER on real meeting audio 5.08% (was 12.18%), fully local, no cloud, 248 test files, no cloud and no API key

**Verify** — `see repo docs/2026-10-07-asr-transcribe-cpp-parakeet-unified.md`

**Repo** — _local, not published yet_

### tech-radar  ·  2026-09-28

**Problem** — Tech news reading is unbounded; without a written rubric it produces noise, not decisions.

**Proved** — rubric written down and unit-tested, offline demo on recorded signals, 7 test files, Go standard library only

**Verify** — `cd ../tech-radar && make demo`

**Repo** — https://github.com/lasttoss/tech-radar

### idempotent-economy  ·  2026-09-20

**Problem** — Retries duplicate side effects, so nobody can say which economy operations are safe to repeat.

**Proved** — 10,000 operations applied twice: the second pass writes nothing; race test with 200 deliveries of one operation

**Verify** — `cd ../idempotent-economy && make demo`

**Repo** — _local, not published yet_

### architecture-diagrams  ·  2026-09-15

**Problem** — Architecture lives in somebody's head and in a screenshot, so no pull request can review it.

**Proved** — 4 mermaid sources with exported PNGs, reviewable as text in a diff

**Verify** — `open ../architecture-diagrams`

**Repo** — https://github.com/lasttoss/architecture-diagrams

### go-log-api  ·  2026-09-10

**Problem** — Game servers post event batches; bad events poison the rollup and nobody can say which batch caused it.

**Proved** — 4-step smoke: health, batch accepted, bad event rejected with a reason, oversized batch refused with 413

**Verify** — `cd ../go-log-api && make up`

**Repo** — https://github.com/lasttoss/go-log-api

### zinx-server  ·  2026-09-05

**Problem** — Two devices can log into one account and both play, which breaks every server-side rule.

**Proved** — one live session per account enforced through Redis, 11 test files, one-command smoke over the TCP protocol

**Verify** — `cd ../zinx-server && make up`

**Repo** — https://github.com/lasttoss/zinx-server

### ts-nakama-game-demo  ·  2026-08-30

**Problem** — A game backend plugin is usually demonstrated by 'it compiles', not by a player completing a match.

**Proved** — device login, server-authoritative match, storage-backed inventory/shop/energy, 4 RPCs, smoke from a clean clone

**Verify** — `cd ../ts-nakama-game-demo && make up`

**Repo** — https://github.com/lasttoss/ts-nakama-game-demo

### quarkus-game-api  ·  2026-08-20

**Problem** — Client-authoritative gameplay means the client decides the outcome; the server only stores it.

**Proved** — single gRPC sendData RPC (opcode + JSON), gameplay driven by server-side config, JWT interceptor on everything but handshake, 8 test files

**Verify** — `cd ../quarkus-game-api && make up`

**Repo** — https://github.com/lasttoss/quarkus-game-api

### quarkus-auth-api  ·  2026-08-15

**Problem** — Auth is copied between services, so a token rule changes in one place and breaks in another.

**Proved** — RSA-signed JWT with register/login/renew/logout, sessions in Redis, 4 test files

**Verify** — `cd ../quarkus-auth-api && make up`

**Repo** — https://github.com/lasttoss/quarkus-auth-api

### game-center-api  ·  2026-08-10

**Problem** — Every new mobile game re-implements the same device auth, save/load, leaderboard and catalogue.

**Proved** — one REST surface serving a portfolio: device auth with JWT, save/load, leaderboards, match records, OpenAPI, 6 test files

**Verify** — `cd ../game-center-api && make up`

**Repo** — https://github.com/lasttoss/game-center-api

## All entries

| id | date | problem | tags |
|---|---|---|---|
| `agent-harness` | 2026-11-10 | A team uses an AI agent it cannot inspect: no cost attribution, no budget, no proof a w... | platform, ai-harness, cost |
| `legacy-revive` | 2026-11-09 | A legacy Spring service has no tests, no maps, and nobody knows what breaks when a file... | legacy, testing, toolkit |
| `oom-evidence` | 2026-11-06 | An OOM happens every few months and nobody can prove what held the memory. | observability, jvm, evidence |
| `cicd-ai-reference` | 2026-10-30 | A pipeline is reviewed by reading YAML, so nobody can tell whether the workflow actuall... | ci, toolkit, ai-harness |
| `qa-kit` | 2026-10-25 | Testers get a URL and 'please test everything'; no one says what the machine already ch... | testing, ci, toolkit |
| `hubgate` | 2026-10-15 | An internal AI hub had no answer to: who may work, through which skill, with which tools. | platform, ai-harness, authorization |
| `job-search` | 2026-10-10 | Job scanning burns model tokens on postings that are already dead, wrong city, or exclu... | tooling, cost, ai-harness |
| `voicekit` | 2026-10-07 | Meeting notes in English are useless to me if the transcript is wrong, and cloud ASR is... | local-ai, measurement, ai-harness |
| `tech-radar` | 2026-09-28 | Tech news reading is unbounded; without a written rubric it produces noise, not decisions. | tooling, ci, cost |
| `idempotent-economy` | 2026-09-20 | Retries duplicate side effects, so nobody can say which economy operations are safe to ... | reliability, backend |
| `architecture-diagrams` | 2026-09-15 | Architecture lives in somebody's head and in a screenshot, so no pull request can revie... | design, docs |
| `go-log-api` | 2026-09-10 | Game servers post event batches; bad events poison the rollup and nobody can say which ... | backend, observability, game |
| `zinx-server` | 2026-09-05 | Two devices can log into one account and both play, which breaks every server-side rule. | game, backend, reliability |
| `ts-nakama-game-demo` | 2026-08-30 | A game backend plugin is usually demonstrated by 'it compiles', not by a player complet... | game, backend |
| `quarkus-game-api` | 2026-08-20 | Client-authoritative gameplay means the client decides the outcome; the server only sto... | backend, game |
| `quarkus-auth-api` | 2026-08-15 | Auth is copied between services, so a token rule changes in one place and breaks in ano... | backend, security, game |
| `game-center-api` | 2026-08-10 | Every new mobile game re-implements the same device auth, save/load, leaderboard and ca... | backend, game |

## Tags

- `ai-harness` — agent-harness, cicd-ai-reference, hubgate, job-search, voicekit
- `authorization` — hubgate
- `backend` — idempotent-economy, go-log-api, zinx-server, ts-nakama-game-demo, quarkus-game-api, quarkus-auth-api, game-center-api
- `ci` — cicd-ai-reference, qa-kit, tech-radar
- `cost` — agent-harness, job-search, tech-radar
- `design` — architecture-diagrams
- `docs` — architecture-diagrams
- `evidence` — oom-evidence
- `game` — go-log-api, zinx-server, ts-nakama-game-demo, quarkus-game-api, quarkus-auth-api, game-center-api
- `jvm` — oom-evidence
- `legacy` — legacy-revive
- `local-ai` — voicekit
- `measurement` — voicekit
- `observability` — oom-evidence, go-log-api
- `platform` — agent-harness, hubgate
- `reliability` — idempotent-economy, zinx-server
- `security` — quarkus-auth-api
- `testing` — legacy-revive, qa-kit
- `tooling` — job-search, tech-radar
- `toolkit` — legacy-revive, cicd-ai-reference, qa-kit
