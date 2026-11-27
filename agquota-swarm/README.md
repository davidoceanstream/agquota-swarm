[English](README.md) | [ภาษาไทย (Thai)](README.th.md)

# AGQuota-Swarm (`/agquota-swarm`)

**A live-quota-aware, model-agnostic multi-model Swarm Orchestrator skill for Antigravity (works across both the Antigravity Workspace App and Antigravity IDE).**

AGQuota-Swarm dynamically inspects the live model catalog, status tags, and remaining `%` quotas on **your own Antigravity machine** via `swarm(action="models", all=True)` and dispatches parallel swarm workers with role-based tiers, right-sized effort levels, disjoint file ownership, preview-first roster confirmation, and clean post-task teardown.

---

## Why AGQuota-Swarm?

- **Dynamic Model-Agnostic Discovery (Future-Proof):** Never hardcodes a fixed list of models as rigid rules. It reads whatever models are currently live on your machine (for example, `Gemini 4 Carbon`, `Neon`, `Hydrogen`, `Claude Opus 5.5`, `Sonnet 5.5`, `GPT-OSS 120B`, or any future release) and maps them automatically into Role Tiers (`Orchestrator`, `Tier S`, `Tier A`, `Tier B`, `Relief`).
- **Transparent Status Tags (No Forced Auto-Skip):** Models marked `Leaving Soon` or `Notice` are shown transparently with their tags rather than silently blocked—if you want to use them, you stay in full control.
- **Right-Sized Effort & Quota Awareness:** Matches `Low / Medium / High / XHigh` effort levels to real task complexity, respects `5h` vs `Weekly` quota overrides confirmed from `View Usage`, and switches workers in-place via `swarm(action="model")` if a runtime quota limit is hit—without losing conversation context.
- **Two User-Controlled Modes:**
  - **Council & Blueprint Mode (`/agquota-swarm plan first <task>` or 3+ workers):** Runs an in-context planning council (Architecture, First-Principles, and Domain/UX lenses) and presents a **Swarm Blueprint Table** showing each worker's role, Primary Skill, Execution Modifiers, MCPs, model, effort level, file scope, and live `%` quota for approval before spawning.
  - **Fast-Track Launch Mode (`/agquota-swarm <task>` for 1–2 workers or *"launch now"*):** Checks live quotas, assigns skills/MCPs in each worker's brief, launches the Swarm UI board immediately, and delivers the synthesized result.
- **Per-Worker Skill & MCP Routing (1 Primary + Max 2 Modifiers):** Assigns each worker 1 Primary Role Skill plus up to 2 Execution Modifiers and explicit MCP servers via a structured 5-line `brief` contract, while keeping interactive commands like `/learn` strictly at the coordinator level.
- **Safe Parallel Edits:** Enforces disjoint file/folder scopes (`inherit` for non-overlapping tasks, `share` or `branch` when parallel workers touch overlapping codebases).
- **Portable & Zero-Leak:** Works regardless of where you clone the repository (any drive on Windows, macOS, or Linux). Contains zero personal paths, tokens, or telemetry.

---

## Installation (Any Drive / Any OS)

Clone this repository anywhere you prefer (e.g., `C:\`, `D:\`, `~/tools/`):

```bash
git clone https://github.com/<your-org>/agquota-swarm.git
cd agquota-swarm
```

### Windows (PowerShell)

```powershell
# Preview target path without making changes
./scripts/install.ps1 -WhatIf

# Install (copies SKILL.md into %USERPROFILE%\.gemini\config\skills\agquota-swarm\)
./scripts/install.ps1

# Optional: Install as a symlink (requires Developer Mode or Admin)
./scripts/install.ps1 -Symlink

# Optional: Install to a custom skills directory
./scripts/install.ps1 -TargetDir "X:\custom\skills\agquota-swarm"
```

### macOS / Linux

```bash
chmod +x ./scripts/install.sh
./scripts/install.sh

# Optional: Symlink instead of copy
./scripts/install.sh --symlink

# Optional: Custom target directory
./scripts/install.sh --target "/custom/path/skills/agquota-swarm"
```

### Manual Installation

Simply copy `SKILL.md` into your Antigravity skills folder:
- Windows: `%USERPROFILE%\.gemini\config\skills\agquota-swarm\SKILL.md`
- macOS / Linux: `~/.gemini/config/skills/agquota-swarm/SKILL.md`

---

## Verification

Run the built-in repository and privacy-shield validator:

```bash
python tests/validate_repo.py
```

---

## License & Disclaimer

Licensed under the [MIT License](LICENSE).

*Disclaimer: AGQuota-Swarm is an independent open-source project and is not affiliated with, sponsored by, or endorsed by Google, Anthropic, or OpenAI.*
