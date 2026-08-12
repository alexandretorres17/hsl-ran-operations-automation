$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$skip = @(".git", "__pycache__", ".pytest_cache")
$files = Get-ChildItem -LiteralPath $root -Recurse -File | Where-Object {
    $relative = $_.FullName.Substring($root.Length).TrimStart('\')
    -not ($skip | Where-Object { $relative -like "$_\*" })
}

$failures = @()
foreach ($file in $files) {
    try { $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8) }
    catch { continue }

    $relative = $file.FullName.Substring($root.Length + 1)
    if ($file.Extension -in @(".hsp3", ".dsl")) {
        $failures += "${relative}: packaged artefact or project metadata"
    }
    if ($content -match '(?im)\b(?:10\.(?:\d{1,3}\.){2}\d{1,3}|192\.168\.(?:\d{1,3}\.)\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.(?:\d{1,3}\.)\d{1,3})\b') {
        $failures += "${relative}: private IPv4 address"
    }
    if ($file.Extension -eq ".hsl3") {
        $emails = [regex]::Matches($content, '(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b')
        foreach ($email in $emails) {
            if (-not $email.Value.EndsWith('.invalid', [StringComparison]::OrdinalIgnoreCase)) {
                $failures += "${relative}: non-example email address"
            }
        }
        if ($content -match '(?i)\b(?:GSM\d+[A-Z]?|UMTS\d+[A-Z]?|V\d+H\d+)\b') {
            $failures += "${relative}: real-looking network-element identifier"
        }
    }
}

if ($failures.Count) {
    $failures | ForEach-Object { Write-Error $_ }
    exit 1
}
Write-Host "Public-copy audit passed: $($files.Count) files checked."
