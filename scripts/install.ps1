[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$TargetDir = (Join-Path $env:USERPROFILE ".gemini\config\skills\virtuososwarm"),
    [switch]$Symlink
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$SourceSkill = Join-Path $RepoRoot "SKILL.md"
$TargetSkill = Join-Path $TargetDir "SKILL.md"

if (-not (Test-Path $SourceSkill)) {
    throw "Source SKILL.md not found at $SourceSkill"
}

if ($PSCmdlet.ShouldProcess($TargetSkill, "Install VirtuosoSwarm SKILL.md")) {
    if (-not (Test-Path $TargetDir)) {
        New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
    }

    if (Test-Path $TargetSkill) {
        Remove-Item -Path $TargetSkill -Force
    }

    if ($Symlink) {
        New-Item -ItemType SymbolicLink -Path $TargetSkill -Target $SourceSkill | Out-Null
        Write-Host "Symlinked $TargetSkill -> $SourceSkill"
    } else {
        Copy-Item -Path $SourceSkill -Destination $TargetSkill -Force
        Write-Host "Copied $SourceSkill -> $TargetSkill"
    }
}
