```markdown
# LangOne: Public Battle-Testing & GA Rollout Pack

This package includes:

1. **Cursor AI Super-Prompt** (dev bootstrapping + verification + issue hygiene)  
2. **Battle-Test Checklist** (copy/paste commands + expected behaviors)  
3. **Contributor Onboarding Pack** (CONTRIBUTING, SECURITY, CI, releases)  
4. **Public Launch Roadmap → GA** (dated phases, exit criteria)  
5. **Educator / Campus Kit** (mini-curriculum, labs, hackathon)  
6. **Ready-to-send Invites** (email + social)  
7. **Owner’s Weekly Cadence & Marketing Tracks**

---

## 1) Cursor AI “Super-Prompt” (drop into Cursor Chat)

> **Title:** LangOne Battle Test & Dev Onboarding  
> **Audience:** New contributors + maintainers  
> **Usage:** Paste as a single message. Replace all `🔧` placeholders.

```

You are a senior LangOne maintainer. Your job is to: (A) set up local dev; (B) run the full battery of checks; (C) prove each language feature with runnable samples; (D) file crisp issues with fixes/PRs.

Repo: 🔧 REPO\_URL
Primary branch: main
Targets: Windows, Linux, macOS (CLI first)

Absolute rules

* Do not guess: run, measure, log outputs.
* Prefer minimal, deterministic examples.
* Every failure → open an issue with “Steps to Reproduce”, expected vs actual, logs, and proposed fix.
* Keep changes in small PRs with green CI.
* Use semantic commits: feat:, fix:, docs:, perf:, refactor:, test:, chore:.

## Phase 0 — Environment

1. Clone, build, and run unit/integration tests.
2. Print toolchain versions (rustc, cargo, LLVM) and OS info.
3. If a version mismatch occurs, add a “/docs/DEV\_SETUP.md” note and a check in CI.

## Phase 1 — Prove Implemented Features

Create a /samples folder containing the following runnable programs, each with a matching README showing:

* Command to run
* Expected output
* What feature it demonstrates

A) Core compilation path

* hello\_world.l1 → prints “Hello, LangOne!”
* arithmetic.l1 → + − × ÷ % precedence; show compile result & run output.

B) Control flow

* control\_flow\.l1 → if/else, while, for; prints a known sequence.

C) Data structures & pattern matching

* patterns.l1 → match with bindings & guards; include a default arm test.

D) Async/await + concurrency

* async\_tasks.l1 → launch 3 tasks; await all; assert ordering insensitivity.

E) Macros (compile-time)

* log\_macro.l1 → define @log! macro that prefixes timestamps; compile to show macro expansion in build logs (if supported) or demonstrate behavior equivalently.

F) Optimizer sanity

* const\_folding.l1 → assert `2+2` optimized; compare IR before/after (emit -O0 vs -O1 if flags exist).

G) Error handling & recovery

* bad\_syntax.l1 → intentionally malformed; ensure human-friendly diagnostics with line/column & hint.

H) REPL

* record a transcript: let x=21\*2; x; fn square(n){…}; square(7) => 49

I) Stdlib smoke

* strings.l1 → substring, split, join
* math.l1 → sqrt, pow, min/max
* io.l1 → read line, echo

For each sample:

* Add `run.ps1` and `run.sh` scripts to compile/run.
* Add golden snapshots under `/samples/_golden/` and a test that diff-checks outputs.

## Phase 2 — Tooling

1. VS Code extension:

   * Confirm syntax highlighting on .l1 files.
   * Validate diagnostics appear on save (if implemented).
   * Open issues for missing IntelliSense items with a small, testable spec.

2. CLI UX:

   * `lang1 --help` and `lang1 --version` must work and be covered by CI snapshot tests.

## Phase 3 — CI & Artifacts

* Add GitHub Actions: build + test on 3 OSes; cache cargo; upload release artifacts on tags v0.\*.
* Attach artifacts: lang1(.exe), checksums, and a `QUICKSTART.md`.

## Phase 4 — Benchmarks (quick)

* Add `/bench/fib.l1` and `/bench/sieve.l1` with wall-time logs.
* Compare “interpreter vs compiled” if both paths exist; document results.

## Phase 5 — Issue Hygiene

* Any missing/unreliable behavior → open an issue with label: area\:compiler / runtime / stdlib / tooling; type\:bug|enhancement; good-first-issue where possible.
* Propose a short fix or RFC sketch where design is non-trivial.

Deliverables

* PR: /samples + scripts + tests + CI.
* Report: /reports/battle-test-YYYYMMDD.md (commands, outputs, failures, proposed fixes).

````

---

## 2) Practical Battle-Test Checklist (copy/paste)

> Assumes `lang1` is your CLI; adjust as needed.

### Bootstrap
```bash
# toolchain
cargo --version && rustc --version

# build + tests
cargo build --release
cargo test -- --nocapture

# static checks
cargo fmt -- --check
cargo clippy -- -D warnings
````

### CLI sanity

```bash
./target/release/lang1 --help
./target/release/lang1 --version
```

### Compile & run samples

```bash
# Hello + arithmetic
./lang1 build samples/hello_world.l1 -o hello && ./hello
./lang1 run   samples/arithmetic.l1

# Control flow, patterns, async/await
./lang1 run samples/control_flow.l1
./lang1 run samples/patterns.l1
./lang1 run samples/async_tasks.l1

# Macros + optimizer check
./lang1 run samples/log_macro.l1
./lang1 build samples/const_folding.l1 -O0 -o out_O0
./lang1 build samples/const_folding.l1 -O1 -o out_O1
# compare emitted IR or binary size if IR dump available
```

### REPL transcript (expected outputs after `>`)

```
lang1 repl
> let x = 21 * 2
> x
42
> fn square(n) { n*n }
> square(7)
49
```

### Stdlib

```bash
./lang1 run samples/strings.l1
./lang1 run samples/math.l1
printf "hello\n" | ./lang1 run samples/io.l1
```

### Diagnostics

```bash
./lang1 run samples/bad_syntax.l1  # expect: file:line:col + actionable hint
```

### Bench (quick pulse)

```bash
time ./lang1 run bench/fib.l1
time ./lang1 build bench/fib.l1 -o fib && time ./fib
```

---

## 3) Contributor Onboarding Pack (drop into repo)

### CONTRIBUTING.md (essentials)

* **Branch model:** `main` (protected), feature branches `feat/<slug>`, `fix/<slug>`.
* **PR rules:** small, focused; include tests; green CI; request 1 review.
* **Commits:** `feat:`, `fix:`, `docs:`, `refactor:`, `perf:`, `test:`, `chore:`.
* **Style:** `cargo fmt` + `clippy -D warnings` required.
* **Issue labels:**

  * `type:bug`, `type:enhancement`, `type:question`, `good-first-issue`
  * `area:lexer|parser|typeck|codegen|runtime|stdlib|tooling|docs`
  * `priority:P0|P1|P2`
* **RFCs:** open `/rfcs/NNNN-short-title.md` for design-affecting changes.

### SECURITY.md

* Report vulnerabilities to **[security@langone.io](mailto:security@langone.io)**.
* No PoC in public issues; 7-day triage; 30-day fix target for high severity.
* Coordinated disclosure welcomed.

### CODE\_OF\_CONDUCT.md

* Contributor Covenant v2.

### CI (GitHub Actions)

* **Matrix:** `ubuntu-latest`, `windows-latest`, `macos-latest`.
* **Steps:** checkout → toolchain cache → build → test → fmt/clippy → upload artifacts on tags.
* **Artifacts:** `lang1` binaries + checksums + `QUICKSTART.md`.

### Release & Versioning

* **SemVer pre-GA:** `v0.MINOR.PATCH`.
* **Tagging:** GitHub Release with binaries + checksums + `CHANGELOG.md`.

---

## 4) Public Launch Roadmap → GA

> **Timezone:** Asia/Karachi
> **Today:** Sep 23, 2025

### Phase A — Private Alpha *(now → Oct 15, 2025)*

**Goal:** Prove core path + REPL + basic stdlib with real users.
**Actions**

* Invite 25–50 trusted developers.
* Run the Battle-Test Checklist; file issues.
* Publish `/samples` and **Quickstart**.
* Weekly “alpha build” releases.
  **Exit criteria**
* Green CI on 3 OSes.
* 0 P0 bugs in compiler/REPL.
* Samples pass on fresh machines.

### Phase B — Public Beta *(Oct 16 → Dec 15, 2025)*

**Goal:** Widen adoption; stabilize runtime & tooling.
**Actions**

* Website **Download** + Docs **Getting Started**.
* VS Code extension on Marketplace (syntax + basic diagnostics).
* Open LangOne Discord + GitHub Discussions.
* First community livestream + mini-hackathon (1 day).
  **Exit criteria**
* ≥200 beta signups; ≥50 unique machines running (opt-in telemetry).
* Crash-free sessions ≥99% (14-day rolling).
* ≥80% issues closed within SLA (P1 ≤14 days, P2 ≤30 days).

### Phase C — Release Candidate *(Dec 16, 2025 → Jan 31, 2026)*

**Goal:** Lock language surface for v1; ship installers.
**Actions**

* Freeze breaking changes; publish **RC Language Spec**.
* Installers: winget, Homebrew, apt, Chocolatey.
* Reserve package namespace; scaffold Package Manager (read-only index).
* Security review + dependency audit.
  **Exit criteria**
* RC spec published; 2 consecutive RCs with no breaking diffs.
* Reproducible builds + signed artifacts.
* Doc coverage: 100% for CLI, language basics, stdlib.

### Phase D — **GA** *(Feb 15, 2026)*

**Goal:** General availability for production pilots.
**Actions**

* Launch blog + press note; showcase 3 reference apps:

  * CLI utility (file watcher)
  * Networked microservice (HTTP echo + JSON)
  * Data-structures demo (maps/sets + algorithms)
* Official curriculum v1.0 (see Section 5).
* Support channels: GitHub issues (community), enterprise email, Discord live help.
  **Exit criteria**
* 0 known P0/P1.
* Installers verified across 3 OSes.
* “First 30 minutes” success rate ≥95% (feedback/opt-in telemetry).
* ≥5 external contributors merged in last 60 days.

> **Optional buffer GA:** **Mar 15, 2026** (enterprise/security cushion).

### Owner’s Weekly Cadence (until GA)

* **Mon:** triage & roadmap sync (60 min)
* **Wed:** maintainers office hour (Discord, 45 min)
* **Fri:** release train / nightly summary (15 min)

### Marketing Tracks

* **DevRel:** bi-weekly blog *Building LangOne* (+ short X/LinkedIn threads).
* **Community:** monthly mini-hackathons; “good first issues” spotlight.
* **Partnerships:** cloud credits, university MoUs.

---

## 5) Educator Rollout (Campus Kit)

### Mini-Curriculum (6 weeks; 2×90-min/week)

* **W1:** Getting Started + Expressions & Types (REPL-first; 10 micro-exercises)
* **W2:** Control Flow + Functions (unit tests for fizzbuzz, primes)
* **W3:** Data Structures + Pattern Matching (tiny JSON parser)
* **W4:** Concurrency (async tasks; producer/consumer via channels/futures)
* **W5:** Algorithms Lab (sorting, searching, hash maps; measure complexity)
* **W6:** Capstone
  Pick one:

  * CLI todo app
  * HTTP echo service
  * File indexer

### Labs & Assessments

* Every lab ships with **starter + tests** (students make them pass).
* Weekly quiz (10 MCQs) auto-graded; rubric included.
* Final demo day rubric: correctness (40), code clarity (30), idiomatic LangOne (20), presentation (10).

### Campus Activation

* 90-min guest lecture deck: *Intro to LangOne & Why it Matters*.
* **LangOne Campus Ambassador** program: shirt + resume badge + early access.
* University hackathon (24h) kit:

  * Problem sets (APIs, CLI tools, data-structure challenges)
  * Judging sheet & scoring script
  * Ready-to-run Docker image of toolchain

### Teaching Materials (to prepare)

* Slides: **LangOne 101**, **Data Structures in LangOne**, **Concurrency Basics**.
* Handouts: REPL cheat-sheet, stdlib quick ref, style guide 1-pager.
* Educator guide: grading rubrics, common pitfalls, setup script for lab PCs.

---

## 6) Ready-to-Post Invites

### Email to Early Developers

```
Subject: Join the LangOne Public Beta (we need your compiler instincts)

Hey <Name>,

We’ve opened LangOne to early developers. You’ll get:
• A fast path to the compiler/runtime,
• Real say in the language surface,
• Your name in the CONTRIBUTORS list before GA.

Start here: <GitHub repo> → QUICKSTART.md
Say hi on Discord: <invite>

We’re “battle-testing” now—kick the tires, file issues, send PRs.
Thanks!
— LangOne Team
```

### Social (X/LinkedIn)

> LangOne is opening for public beta: a future-proof, AI-native language that’s friendly like Python, fast/safe like Rust, and cloud-savvy out of the box.
> Try it, file issues, shape v1 → \<repo/website>  #programming #compilers #rust #ai

---

## 7) What to Decide Now (to flip the switches)

* **Repo URL/org** to embed in the Cursor prompt.
* **Comms:** GitHub Discussions, Discord, or both.
* **License:** recommend **Apache-2.0** (open-core friendly).
* **Security contact:** e.g., `security@langone.io`.
* **Target GA date:** **Feb 15, 2026** (or backup **Mar 15, 2026**).

---

## 8) Optional: Seed Files to Generate Next

If desired, generate these immediately:

* `/samples/*` (programs + golden outputs + `run.sh` / `run.ps1`)
* `.github/workflows/ci.yml` (3-OS matrix, artifacts on tags)
* `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`
* `QUICKSTART.md` (install → run first sample in <5 minutes)
* Educator slide outlines (`/teaching/slides/*.mdx`)

```
```
