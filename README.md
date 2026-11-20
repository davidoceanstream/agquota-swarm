[English](README.md) | [ภาษาไทย (Thai)](README.th.md)

# AGQuota-Swarm (`/agquota-swarm`)

**A live-quota-aware multi-model Swarm Orchestrator skill for Antigravity (works across both the Antigravity Workspace App and Antigravity IDE).**

AGQuota-Swarm inspects your live remaining `%` quotas across Antigravity's model pool (`Gemini 4 Argon`, `Gemini 4 Neon`, `Gemini 4 Hydrogen`, `Claude Opus 5.5`, `Claude Sonnet 5.5`, `GPT-OSS 120B`, and more) and dispatches parallel swarm workers with disjoint file ownership, preview-first roster confirmation, and clean post-task teardown.

---

## Why AGQuota-Swarm?

- **Live Quota Balancing:** Always queries `swarm(action="models", all=True)` before spawning workers, so you never blindly drain your primary session model when other strong models have plenty of headroom.
- **Two User-Controlled Modes:**
  - **Default Mode (`/agquota-swarm <task>`):** Checks quotas, assigns disjoint scopes, launches the Swarm UI board, and delivers the synthesized result.
  - **Preview Mode (`/agquota-swarm preview first <task>`):** Shows a concise table of planned workers, models, effort levels, and remaining `%` quotas and waits for your approval before spawning.
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
