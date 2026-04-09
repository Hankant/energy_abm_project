Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$filesDir = Join-Path $root "files"
$manifestPath = Join-Path $root "manifest.json"
$csvPath = Join-Path $root "index.csv"
$jsonPath = Join-Path $root "index.json"

New-Item -ItemType Directory -Force -Path $filesDir | Out-Null

function Get-SafeFileName {
    param(
        [string]$BaseName,
        [string]$Extension
    )

    $safe = $BaseName -replace '[<>:"/\\|?*]', " "
    $safe = $safe -replace "\s+", " "
    $safe = $safe.Trim().Trim(".")
    return "$safe$Extension"
}

function Save-TextFile {
    param(
        [string]$Path,
        [string]$Content
    )

    [System.IO.File]::WriteAllText($Path, $Content, [System.Text.Encoding]::UTF8)
}

function Get-FieldValue {
    param(
        [object]$Object,
        [string]$Name
    )

    if ($null -eq $Object) {
        return $null
    }

    $property = $Object.PSObject.Properties[$Name]
    if ($property) {
        return $property.Value
    }

    return $null
}

function Test-IsPdfFile {
    param([string]$Path)

    if (-not (Test-Path $Path)) {
        return $false
    }

    $bytes = [System.IO.File]::ReadAllBytes($Path)
    if ($bytes.Length -lt 4) {
        return $false
    }

    return ($bytes[0] -eq 0x25 -and $bytes[1] -eq 0x50 -and $bytes[2] -eq 0x44 -and $bytes[3] -eq 0x46)
}

function Try-Download {
    param(
        [string]$Url,
        [string]$Path
    )

    $headers = @{
        "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0 Safari/537.36"
        "Accept-Language" = "en-US,en;q=0.9,zh-CN;q=0.8"
    }

    try {
        Invoke-WebRequest -UseBasicParsing -Headers $headers -Uri $Url -OutFile $Path
        return $true
    }
    catch {
        return $false
    }
}

function Save-LinkStub {
    param(
        [string]$Path,
        [object]$Item
    )

    $content = @(
        "Title: $($Item.title)"
        "Year: $($Item.year)"
        "Language: $($Item.language)"
        "Type: $($Item.type)"
        "URL: $($Item.source_url)"
        ""
        "Use:"
        "$($Item.intended_use)"
    ) -join [Environment]::NewLine

    Save-TextFile -Path $Path -Content $content
}

$manifest = Get-Content -Raw -Encoding UTF8 $manifestPath | ConvertFrom-Json
$results = New-Object System.Collections.Generic.List[object]

foreach ($item in $manifest) {
    Write-Host "Collecting: $($item.title)"

    $savedFile = $null
    $status = "link_only"
    $candidatePath = $null
    $pdfUrl = Get-FieldValue -Object $item -Name "pdf_url"
    $htmlUrl = Get-FieldValue -Object $item -Name "html_url"

    if ($pdfUrl) {
        $candidatePath = Join-Path $filesDir (Get-SafeFileName -BaseName $item.title -Extension ".pdf")
        if (Try-Download -Url $pdfUrl -Path $candidatePath) {
            if (Test-IsPdfFile -Path $candidatePath) {
                $savedFile = Split-Path -Leaf $candidatePath
                $status = "pdf_saved"
            }
            else {
                Remove-Item -Force $candidatePath
            }
        }
    }

    if (-not $savedFile -and $htmlUrl) {
        $candidatePath = Join-Path $filesDir (Get-SafeFileName -BaseName $item.title -Extension ".html")
        if (Try-Download -Url $htmlUrl -Path $candidatePath) {
            $savedFile = Split-Path -Leaf $candidatePath
            $status = "html_saved"
        }
    }

    if (-not $savedFile) {
        $candidatePath = Join-Path $filesDir (Get-SafeFileName -BaseName $item.title -Extension ".txt")
        Save-LinkStub -Path $candidatePath -Item $item
        $savedFile = Split-Path -Leaf $candidatePath
        $status = "link_stub_saved"
    }

    $results.Add([PSCustomObject]@{
        title = $item.title
        year = $item.year
        language = $item.language
        type = $item.type
        source_url = $item.source_url
        intended_use = $item.intended_use
        status = $status
        saved_file = $savedFile
    })
}

$results | Export-Csv -NoTypeInformation -Encoding UTF8 -Path $csvPath
$results | ConvertTo-Json -Depth 5 | Set-Content -Encoding UTF8 $jsonPath

Write-Host ""
Write-Host "Saved to: $root"
