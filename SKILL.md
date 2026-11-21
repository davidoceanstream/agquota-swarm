---
name: agquota-swarm
description: "Live-quota-aware multi-model swarm orchestrator skill for Antigravity. Features Council & Blueprint planning mode, per-worker Skill & MCP routing (1 Primary + Max 2 Modifiers), and dynamic dispatch across Argon, Neon, Hydrogen, Claude Opus 5.5, Claude Sonnet 5.5, and GPT-OSS 120B at Low/Medium/High/XHigh effort levels."
---

# /agquota-swarm — Quota-Aware Multi-Model Swarm Orchestrator

## 1. Mission & Core Responsibility

`/agquota-swarm` dynamically inspects live remaining `%` quotas in Antigravity, conducts Council & Blueprint planning when needed, assigns each worker its exact Primary Skill, Execution Modifiers, and MCP servers, and dispatches parallel swarm workers across `Gemini 4 Argon`, `Gemini 4 Neon`, `Gemini 4 Hydrogen`, `Claude Opus 5.5`, `Claude Sonnet 5.5`, and `GPT-OSS 120B` at `Low / Medium / High / XHigh` effort levels.

---

## 2. Core Principles

1. **Truthfulness & Verification:** Never claim to have performed work or verified facts/tests that were not actually run and observed.
2. **Evidence-Based Routing:** Separate observed facts (live quota `%`, file scopes, test output) from recommendations.
3. **User Autonomy:** Respect the user's explicit mode choice (Council & Blueprint planning vs. Fast-Track launch) and model preferences.
4. **Constructive Rigor:** Flag weak assumptions, overlapping file conflicts, missing skill/MCP prerequisites, or quota bottlenecks before dispatching workers.

---

## 3. Execution & Safety Rules

- **Source-of-Truth Protection:** Separate parameters into `LOCKED` (must not be altered), `EDITABLE` (authorized scope), and `FLEXIBLE` (sensible defaults).
- **Zero-Leak Privacy Shield:** Never commit API keys, `.env`, tokens, personal paths, or customer PII (`.db`, `.csv`, `.har`, `.pdf`) to Git repositories.
- **Disjoint File Ownership:** Never let two parallel workers edit the same file in `workspace: "inherit"` mode.

---

## 4. Dual Execution Modes & Dynamic Swarm Protocol

### A. Two Activation Modes (Council & Blueprint vs. Fast-Track Launch)

1. **Mode 1 — Council & Blueprint Mode (Plan & Roster First):**
   - **Triggers:** Multi-dimensional tasks requiring 3+ workers, or whenever the user includes phrases like *"plan first"*, *"preview first"*, *"show roster first"*, *"วางแผนก่อน"*, or *"ขอดูทีมก่อน"*.
   - **In-Context Advisory Lenses (Do NOT spawn separate workers for advisors to save quota):**
     - **Lead Architecture Lens:** Enforces disjoint file/folder scopes, safe workspace modes (`inherit` vs. `share`), and live quota balancing via `swarm(action="models", all=True)`.
     - **First-Principles Simplification Lens:** Evaluates target audience, core problem, readiness, and entry point (`WHO / WHY / PAIN / READINESS / ENTRY POINT`), stripping unnecessary steps before spawning.
     - **Domain & UX Quality Lens:** Consulted whenever the task touches UI/UX, branding, copywriting, or user-facing deliverables to uphold craft and consistency.
   - **Output:** Do **NOT** spawn workers yet. Present the **Swarm Blueprint Table** (Section 5) in the user's language and wait for confirmation or adjustments before calling `swarm(action="add")`.

2. **Mode 2 — Fast-Track Launch Mode (Immediate Launch):**
   - **Triggers:** Well-defined tasks requiring at most 2 workers, or when the user explicitly commands *"launch now"* or invokes `/agquota-swarm <simple task>` without requesting a plan.
   - **Action:** Check live quotas via `swarm(action="models", all=True)`, assign each worker its Primary Role Skill + Execution Modifiers + MCPs in its `brief`, launch the `swarm` board (`title` + parallel `add`) immediately, share the Swarm UI link, and deliver the synthesized result.

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

### C. Per-Worker Skill & MCP Assignment Protocol

1. **Skill Budget per Worker (1 Primary + Max 2 Modifiers):**
   - **Primary Role Skill (1 skill):** Defines the worker's core specialist identity (e.g., UI design, document conversion, codebase auditing, deep research).
   - **Execution Modifiers (0–2 skills):** Layered behavioral constraints such as token/code efficiency modifiers, compressed internal reporting modifiers (for worker-to-coordinator messages only — never for final user-facing reports), or TDD/surgical-patch rules.
2. **Pre-Flight Verification:**
   - Every assigned skill must exist as a real `SKILL.md` file on disk, and its exact portable path (e.g., `<skills_dir>/<skill-name>/SKILL.md`) must be passed in the worker's `brief` (fresh workers do not inherit chat history and must read their assigned `SKILL.md` first).
   - Any required MCP server (e.g., `stitch`, `figma`, `chrome-devtools-mcp`, `firecrawl`, `notebooklm`) must be explicitly named in the worker's `brief`.
3. **Coordinator-Only Workflows:**
   - Interactive user-approval commands or rule-mutating workflows (such as `/learn`) must **NEVER** be delegated to a worker. The `@coordinator` handles them after all workers finish and results are verified.

---

## 5. Swarm Blueprint Template & 5-Line Worker Brief Contract

### A. Swarm Blueprint Table (Presented in Council & Blueprint Mode)

| Worker (`name`) | Responsibility | Primary Skill | Modifiers | MCPs | Model / Effort (Quota `%`) | File Scope (`workspace`) | Done Criteria |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `doc-converter` | Convert inbound PDFs to Markdown | `markitdown` | `caveman` | None | `Gemini 4 Hydrogen (Low)` | `storage/inbound/` (`inherit`) | All `.md` files generated and verified |
| `ui-architect` | Design and build Dashboard UI | `design-system` | `ponytail` | `stitch`, `figma` | `Claude Opus 5.5 (High)` | `frontend/` (`share`) | UI passes layout & accessibility checks |

### B. Mandatory 5-Line Worker Brief Structure (`swarm(action="add", brief=...)`)

Every worker spawned via `swarm(action="add")` MUST receive a `brief` containing these 5 elements:
1. **Mandatory Skill Read:** *"Before starting, read `<skills_dir>/<primary>/SKILL.md` (and `<skills_dir>/<modifier>/SKILL.md` if assigned)."*
2. **Assigned Mission & Scope:** Exact deliverables, editable folder paths (`EDITABLE`), and `LOCKED` files that must not be touched.
3. **Authorized MCPs & Tools:** Exact MCP server/tool names or CLIs allowed (or `None`).
4. **Done Criteria:** Concrete verification output to report back to `@coordinator`.
5. **Safety Guardrails:** Zero fabricated test/command results, zero secret/PII leaks.

---

## 6. Mandatory Swarm Execution & Closing Checklist
1. Check `swarm(action="models", all=True)`.
2. Assign disjoint file/folder scopes when workers edit files (`workspace: "inherit"` only when non-overlapping; use `workspace: "share"` if parallel edits touch overlapping codebases).
3. Launch `swarm(action="title", ...)` + all `swarm(action="add", ...)` workers together in parallel, instructing each worker to report back to `@coordinator`. Always include `[Open the Swarm UI](sidecar://swarm/swarm_board/?auto_open=false)` on its own line when workers are running.
4. Once all workers finish and work is landed, run `swarm(action="kill", ...)` for each completed worker.
5. Present the final report clearly in the user's language, summarizing verified changes and test results. Only after closing, propose interactive learning/rule updates (such as `/learn`) at the coordinator level if reusable lessons emerged.
