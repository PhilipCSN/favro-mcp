#!/usr/bin/env pwsh
# Builds a standalone single-file favro-mcp.exe via PyInstaller.
# Output: dist/favro-mcp.exe

$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")

uv run --with pyinstaller pyinstaller `
    --onefile `
    --name favro-mcp `
    --paths src `
    --copy-metadata fastmcp `
    src/favro_mcp/__main__.py

if ($LASTEXITCODE -ne 0) {
    throw "PyInstaller build failed"
}

Write-Host "Built dist/favro-mcp.exe"
