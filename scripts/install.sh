#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SOURCE_SKILL="$REPO_ROOT/SKILL.md"
TARGET_DIR="${HOME}/.gemini/config/skills/virtuososwarm"
USE_SYMLINK=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      TARGET_DIR="$2"
      shift 2
      ;;
    --symlink)
      USE_SYMLINK=true
      shift
      ;;
    -h|--help)
      echo "Usage: $0 [--target <dir>] [--symlink]"
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      exit 1
      ;;
  esac
done

if [[ ! -f "$SOURCE_SKILL" ]]; then
  echo "Error: Source SKILL.md not found at $SOURCE_SKILL" >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"
TARGET_SKILL="$TARGET_DIR/SKILL.md"

if [[ "$USE_SYMLINK" == true ]]; then
  ln -sf "$SOURCE_SKILL" "$TARGET_SKILL"
  echo "Symlinked $TARGET_SKILL -> $SOURCE_SKILL"
else
  cp "$SOURCE_SKILL" "$TARGET_SKILL"
  echo "Copied $SOURCE_SKILL -> $TARGET_SKILL"
fi
