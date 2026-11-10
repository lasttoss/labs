# What survives: converting 14 years of failure modes into today's tools

Most of what I learned between 2011 and 2020 is not syntax. It is a catalogue of
ways systems fail, and what each failure costs. Syntax expired; the failure modes
did not. This page records the conversion one item at a time: the symptom I learned
to recognise, the tool that solves it today, the evidence that it was actually
re-solved, and the part that did not change.

The last line of each item is the only line that transfers.

---

## 1. Two devices, one account, both play

- **Symptom (then):** every server-side rule is optional once a second session can
  act on the same account.
- **Still true:** yes, in every protocol.
- **Tool today:** one live session per account enforced in Redis, JWT claims, smoke
  over the real TCP protocol.
- **Evidence:** `zinx-server` — 11 test files, one-command smoke.
- **Invariant:** authority belongs to the side that cannot be edited by the player.

## 2. Nobody dares to change a legacy service

- **Symptom (then):** the code has no tests, so every change is a bet.
- **Still true:** yes. AI makes this worse, not better: it produces plausible
  changes faster than anyone can review them.
- **Tool today:** record current behaviour as golden tests, then gate the merge on
  those recordings plus a coverage floor with a ratchet.
- **Evidence:** `legacy-revive-lab` — 0 to 20 golden tests, 89.2% line coverage,
  baseline locked at 0.892.
- **Invariant:** behaviour recorded before the change is the only definition of
  "still correct" that survives a refactor.

## 3. "It might be memory", and then a restart

- **Symptom (then):** an OOM every few months, no artifact, no answer.
- **Still true:** yes, until someone captures evidence by design.
- **Tool today:** reproducible failure cases, heap dump taken outside tmpfs,
  classification of the retention path, alert on the trend rather than the level.
- **Evidence:** `oom-evidence-lab` — 6 reproducible modes, 10 outcomes, one leak
  reproduced at 99.6% of heap.
- **Invariant:** an incident without an artifact is a rumour.

## 4. Retries that duplicate money

- **Symptom (then):** a retried request applies a side effect twice.
- **Still true:** yes, on every network that can lose an answer.
- **Tool today:** idempotency key per operation plus an outbox; the second delivery
  writes nothing.
- **Evidence:** `idempotent-economy` — 10,000 operations applied twice, second pass
  writes nothing; race test with 200 deliveries of one operation.
- **Invariant:** the client cannot be trusted to know whether its last request
  landed.

## 5. A coverage number that blocks nothing

- **Symptom (then):** the report says 71%, the review passes, the regression ships.
- **Still true:** yes. Reporting and gating are different products.
- **Tool today:** floor plus ratchet, checked in CI, failing the build.
- **Evidence:** `legacy-revive-lab` (`kit/coverage_gate.py`), `qa-kit`.
- **Invariant:** a number that cannot fail a build is decoration.

## 6. Documentation that is already wrong

- **Symptom (then):** a design document describes version 2 while the code is at 4.
- **Still true:** yes, and AI-written docs drift faster because they are cheap.
- **Tool today:** generate docs and maps from source, then fail CI when the
  regenerated output differs from what is committed.
- **Evidence:** `legacy-revive-lab` (`gen_docs.py` + `git diff --exit-code`),
  this catalogue (`gen_catalog.py` + `make check`).
- **Invariant:** anything that can be generated must never be edited by hand.

## 7. Testers receive a URL and "please test everything"

- **Symptom (then):** QA re-checks by hand what a machine already verified, and
  misses what no machine checks.
- **Still true:** yes.
- **Tool today:** a handoff report per release candidate stating what was verified,
  what could not be verified, and where a human should look first.
- **Evidence:** `qa-kit` — `reports/qa-<version>.md` emitted per candidate.
- **Invariant:** the machine states facts, the human decides.

## 8. Auth rules copied into every service

- **Symptom (then):** a token rule changes in one service and breaks in another.
- **Still true:** yes, and AI copies one more time.
- **Tool today:** an explicit contract (RSA-signed JWT, renew, logout), sessions in
  Redis, plus a gate that answers "who may work, through what, with which tools".
- **Evidence:** `quarkus-auth-api` (4 test files), `hubgate` (3 gates in fixed order).
- **Invariant:** authentication is a contract, not a snippet.

## 9. A team uses AI, nobody can say what it costs

- **Symptom (then, new):** the agent answers, the invoice grows, no one can
  attribute the spend and no gate can prove a wrong answer wrong.
- **Still true:** yes, and this is the version of "no tests" that teams are entering now.
- **Tool today:** a proxy at the tool boundary with a hard daily budget, per-request
  cost, prompt-prefix guard, redaction, and gates outside the loop.
- **Evidence:** `agent-harness-lab` — cache reuse 0 to 13 tokens on a repeat,
  volatility detected on 6 patterns, HTTP 429 when the budget is gone.
- **Invariant:** an agent that cannot be measured cannot be trusted with production.

## 10. English meetings I could not follow fast enough

- **Symptom (then):** the transcript arrives after the decision, and it is wrong.
- **Still true:** yes, until the error rate is measured instead of assumed.
- **Tool today:** local ASR, measured on real meeting audio, no cloud, no key.
- **Evidence:** `voicekit` — WER 5.08% on real meeting audio (was 12.18%).
- **Invariant:** an unmeasured tool is an opinion with a user interface.

---

## What does not convert

Naming these is part of the same discipline. These are dead, and I do not put them
on a CV as if they were alive:

1. **XML-era application-server wiring.** The problem it solved (declarative
   assembly) is solved by conventions and containers now. The skill is historical.
2. **Manual release rituals** — build on a laptop, copy by hand, verify by memory.
   The value was discipline; the practice is now a pipeline, and the pipeline does
   it better.
3. **Being the only person who knows where things are.** That was never expertise,
   it was a single point of failure. The conversion is to write the map and let it
   be checked, which is what the maps and generated docs above exist for.

## The rule I keep

> Old knowledge converts when the symptom is still real and the tool has changed.
> It does not convert by being repeated louder, and it does not convert by being
> replaced with new vocabulary.
