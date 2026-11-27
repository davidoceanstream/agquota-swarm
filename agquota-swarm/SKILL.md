---
name: agquota-swarm
description: "Live-quota-aware, model-agnostic multi-model Swarm Orchestrator skill for Antigravity. Dynamically discovers models and live quotas on each user's machine via swarm(action=\"models\", all=True), supports Council & Blueprint planning mode, per-worker Skill & MCP routing (1 Primary + Max 2 Modifiers), right-sized effort levels, transparent status tags without forced auto-skip, and in-place fallback switching."
---

# /agquota-swarm — Quota-Aware Multi-Model Swarm Orchestrator

## 1. Mission & Core Responsibility

`/agquota-swarm` dynamically inspects the live model catalog, status tags, effort tiers, and remaining `%` quotas available on **the user's own Antigravity machine**, conducts Council & Blueprint planning when needed, assigns each worker its exact Primary Skill, Execution Modifiers, and MCP servers, and dispatches parallel swarm workers across whichever models have headroom at right-sized effort levels (`Low / Medium / High / XHigh`).

---

## 2. Core Principles

1. **Truthfulness & Verification:** Never claim to have performed work or verified facts/tests that were not actually run and observed.
2. **Evidence-Based Routing:** Separate observed facts (live model catalog, quota `%`, status tags, file scopes, test output) from recommendations.
3. **User Autonomy First:** Always honor the user's explicit mode choice (Council & Blueprint vs. Fast-Track), preferred models, and live `View Usage` confirmations.
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
   - **Action:** Check the live machine catalog and quotas via `swarm(action="models", all=True)`, assign each worker its Primary Role Skill + Execution Modifiers + MCPs in its `brief`, launch the `swarm` board (`title` + parallel `add`) immediately, share the Swarm UI link, and deliver the synthesized result.

### B. Dynamic Model-Agnostic & Quota-Aware Routing Matrix
Always call `swarm(action="models", all=True)` first. Treat the live response from **the user's machine** as the #1 Source of Truth so newly added models work immediately and retired/removed models are never called blindly.

| Role Tier | Selection Criteria (From Live `swarm(action="models", all=True)`) | Effort Levels | Illustrative Examples *(Reference Only — Always Use Live Catalog)* |
| :--- | :--- | :--- | :--- |
| **Orchestrator / Lead** | Available orchestrator or flagship reasoning models with quota headroom | Coordinator / Lead | e.g., `Orchestrator (...)`, flagship reasoning models |
| **Tier S (Deep Strategy & Craft)** | Strongest reasoning & architecture models currently live on the user's machine | `Low / Medium / High` *(or `XHigh` if supported)* | e.g., `Gemini 4 Carbon`, `Gemini 4 Neon`, `Claude Opus 5.5` |
| **Tier A (Core Build & Integration)** | High-capability coding, API/MCP wiring, and multi-file build models currently live | `Low / Medium / High` | e.g., `Gemini 4 Carbon`, `Gemini 4 Neon`, `Claude Sonnet 5.5` |
| **Tier B (Fast Audit & Verification)** | Fast, quota-efficient models for codebase audits, diffs, test runs, and conversions | `Low / Medium / High / XHigh` | e.g., `Gemini 4 Hydrogen`, fast/flash-class models |
| **Relief / Backup** | Alternative model families with spare quota when primary families are low | Match model default | e.g., `GPT-OSS 120B (Medium)` or any live secondary pool |

- **Live Machine Catalog First (Future-Proof Rule):** Never hardcode or assume a model exists if it is missing from `swarm(action="models", all=True)`. When providers release new models or remove old ones, automatically classify the newly available models into the role tiers above based on the live list.
- **No Forced Auto-Skip on Status Tags (`Leaving Soon` / `Notice`):** Do **NOT** automatically ban or silently skip models marked `Leaving Soon`, `Notice`, or legacy (such as `Gemini 4 Argon` or `Gemini 3.8 Flash`). Show their status tag transparently in the Blueprint table and let the user choose or run them freely whenever desired.
- **Zero-Quota Protection & Balance:** Avoid automatically dispatching a model whose usable quota is `0%` (exhausted) unless the user explicitly asks to try it. Balance load across model families instead of draining the main session's pool when strong alternatives have high headroom.
- **Right-Sizing Effort Rule (Never Default All to `High`):** Match effort level to actual task complexity so workers stay fast and quota-efficient:
  - **`Low`:** Routine verification, running tests/audits, file conversions, cache/graph sync.
  - **`Medium`:** Standard feature coding, DOM/Playwright tweaks, formula/API wiring where specs are already clear.
  - **`High` / `XHigh`:** Reserve strictly for the 1–2 hardest architectural, multi-constraint layout, or deep debugging tasks.
- **User-Verified Quota Override & Two-Layer Limits (`5h` vs `Weekly`):** Antigravity tracks both short-window (`5h limit`) and `Weekly limit` quotas per model family, and `swarm(action="models")` may occasionally display a stale cached percentage after a reset. Whenever the user explicitly confirms from their live `View Usage` panel that a model family has available quota (or explicitly requests a specific model), honor the user's instruction immediately. If a worker hits an actual runtime quota error, switch it **in-place** via `swarm(action="model")` to an available model with headroom without killing its conversation.

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

| Worker (`name`) | Responsibility | Primary Skill | Modifiers | MCPs | Model / Effort (Quota `%` & Tag) | File Scope (`workspace`) | Done Criteria |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `doc-converter` | Convert inbound PDFs to Markdown | `markitdown` | `caveman` | None | `Tier B live model (Low — 99%)` | `storage/inbound/` (`inherit`) | All `.md` files generated and verified |
| `ui-architect` | Design and build Dashboard UI | `design-system` | `ponytail` | `stitch`, `figma` | `Tier S live model (High — 93%)` | `frontend/` (`share`) | UI passes layout & accessibility checks |

### B. Mandatory 5-Line Worker Brief Structure (`swarm(action="add", brief=...)`)

Every worker spawned via `swarm(action="add")` MUST receive a `brief` containing these 5 elements:
1. **Mandatory Skill Read:** *"Before starting, read `<skills_dir>/<primary>/SKILL.md` (and `<skills_dir>/<modifier>/SKILL.md` if assigned)."*
2. **Assigned Mission & Scope:** Exact deliverables, editable folder paths (`EDITABLE`), and `LOCKED` files that must not be touched.
3. **Authorized MCPs & Tools:** Exact MCP server/tool names or CLIs allowed (or `None`).
4. **Done Criteria:** Concrete verification output to report back to `@coordinator`.
5. **Safety Guardrails:** Zero fabricated test/command results, zero secret/PII leaks.

---

## 6. Mandatory Swarm Execution & Closing Checklist
1. Check `swarm(action="models", all=True)` on the user's machine and honor any explicit user model/quota overrides.
2. Assign disjoint file/folder scopes when workers edit files (`workspace: "inherit"` only when non-overlapping; use `workspace: "share"` if parallel edits touch overlapping codebases).
3. Launch `swarm(action="title", ...)` + all `swarm(action="add", ...)` workers together in parallel, instructing each worker to report back to `@coordinator`. Always include `[Open the Swarm UI](sidecar://swarm/swarm_board/?auto_open=false)` on its own line when workers are running.
4. If any worker hits a runtime quota error, switch it in-place via `swarm(action="model")` instead of killing its conversation.
5. Once all workers finish and work is landed, run `swarm(action="kill", ...)` for each completed worker.
6. Present the final report clearly in the user's language, summarizing verified changes and test results. Only after closing, propose interactive learning/rule updates (such as `/learn`) at the coordinator level if reusable lessons emerged.
