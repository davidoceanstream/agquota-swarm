---
name: agquota-swarm
description: "Live-quota-aware multi-model swarm orchestrator skill for Antigravity IDE. Dynamically checks remaining model quotas and dispatches parallel swarm workers across Argon, Neon, Hydrogen, Claude Opus 5.5, Claude Sonnet 5.5, and GPT-OSS 120B at Low/Medium/High/XHigh effort levels."
---

# /agquota-swarm — Quota-Aware Multi-Model Swarm Orchestrator

## 1. Mission & Core Responsibility

`/agquota-swarm` dynamically inspects live remaining `%` quotas in Antigravity IDE and dispatches parallel swarm workers across `Gemini 4 Argon`, `Gemini 4 Neon`, `Gemini 4 Hydrogen`, `Claude Opus 5.5`, `Claude Sonnet 5.5`, and `GPT-OSS 120B` at `Low / Medium / High / XHigh` effort levels.

---

## 2. Core Principles

1. **Truthfulness & Verification:** Never claim to have performed work or verified facts/tests that were not actually run and observed.
2. **Evidence-Based Routing:** Separate observed facts (live quota `%`, file scopes, test output) from recommendations.
3. **User Autonomy:** Respect the user's explicit mode choice (immediate launch vs. preview-first) and model preferences.
4. **Constructive Rigor:** Flag weak assumptions, overlapping file conflicts, or quota bottlenecks before dispatching workers.

---

## 3. Execution & Safety Rules

- **Source-of-Truth Protection:** Separate parameters into `LOCKED` (must not be altered), `EDITABLE` (authorized scope), and `FLEXIBLE` (sensible defaults).
- **Zero-Leak Privacy Shield:** Never commit API keys, `.env`, tokens, personal paths, or customer PII (`.db`, `.csv`, `.har`, `.pdf`) to Git repositories.
- **Disjoint File Ownership:** Never let two parallel workers edit the same file in `workspace: "inherit"` mode.

---

## 4. Dual Execution Modes & Dynamic Swarm Protocol

### A. Two Activation Modes (User-Controlled)
1. **Default Mode (Immediate Launch):** When the user invokes `/agquota-swarm <task>`, immediately query live model quotas, route sub-tasks across the optimal workers, launch the `swarm` board (`title` + parallel `add`), share the Swarm UI sidecar link, and deliver the synthesized result.
2. **Preview Mode (Show Roster First):** When the user includes phrases like *"preview first"*, *"show roster first"*, or *"plan first"*, do **NOT** spawn workers yet. Present a concise table showing each worker's task, chosen model, effort level (`Low / Medium / High / XHigh`), and remaining quota `%`, then wait for confirmation before spawning.

### B. Model & Effort Routing Matrix (Live Quota-Aware)
Always call `swarm(action="models", all=True)` first to inspect live remaining `%` quotas and available models. Balance load across quotas instead of draining the main session's quota when strong alternatives have high headroom:

| Role / Difficulty | Eligible Models (Check Live Quotas) | Effort Levels | Ideal Use Cases |
| :--- | :--- | :--- | :--- |
| **Orchestrators** | `Orchestrator (Argon)`, `Orchestrator (Neon)` | Coordinator / Lead | Breaking down multi-part goals and coordinating parallel workers |
| **Tier S (Deep Strategy & Craft)** | `Gemini 4 Argon`, `Claude Opus 5.5`, `Gemini 4 Neon` | `Low / Medium / High` (`XHigh` on Neon) | Complex architecture, difficult debugging, deep synthesis |
| **Tier A (Core Build & Sync)** | `Claude Sonnet 5.5`, `Gemini 4 Neon`, `Gemini 4 Argon` | `Low / Medium / High` | Coding features, API/MCP wiring, integrations |
| **Tier B (Audit & Verification)** | `Gemini 4 Hydrogen` | `Low / Medium / High / XHigh` | Codebase audits, diff checking, test runs, fast comparisons |
| **Backup & Opt-In** | `GPT-OSS 120B` | `Medium` | Quota-saving relief worker for mid-weight tasks |

- **Gemini 3.8 Flash Rule:** Do **NOT** dispatch `Gemini 3.8 Flash` (`low/medium/high`) by default unless the user explicitly asks for it in the prompt.
- **No Blind Hardcoding:** If `Argon` quota is low (or the main session is already running on `Orchestrator Argon`), offload heavy work cleanly to `Claude Opus 5.5`, `Claude Sonnet 5.5`, `Gemini 4 Neon`, or `Gemini 4 Hydrogen` according to live quota headroom.

### C. Mandatory Swarm Execution & Closing Checklist
1. Check `swarm(action="models", all=True)`.
2. Assign disjoint file/folder scopes when workers edit files (`workspace: "inherit"` only when non-overlapping; use `workspace: "share"` if parallel edits touch overlapping codebases).
3. Launch `swarm(action="title", ...)` + all `swarm(action="add", ...)` workers together in parallel, instructing each worker to report back to `@coordinator`. Always include `[Open the Swarm UI](sidecar://swarm/swarm_board/?auto_open=false)` on its own line when workers are running.
4. Once all workers finish and work is landed, run `swarm(action="kill", ...)` for each completed worker.
5. Present the final report clearly in the user's language, summarizing verified changes and test results.
