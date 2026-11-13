# Detailed live audit and local parity script
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Continue'

$liveBase = 'https://www.enviosdosruedas.com'

# List of URLs to audit
$urlsToAudit = @(
    '/',
    '/servicios/',
    '/servicios/envios-express/',
    '/servicios/envios-lowcost/',
    '/servicios/enviosflex/',
    '/servicios/deposito-fulfillment/',
    '/servicios/empresas-cuenta-corriente/',
    '/servicios/plan-emprendedores/',
    '/servicios/envios-contrareembolso/',
    '/cotizar/',
    '/cobertura/',
    '/logistica-dosruedas/',
    '/mardelivery/',
    '/guias/envios-flex-mar-del-plata/',
    '/contacto/',
    '/nosotros/sobre-nosotros/',
    '/nosotros/preguntas-frecuentes/',
    '/nosotros/nuestras-redes/',
    '/politica-de-privacidad/',
    '/terminos-y-condiciones/'
)

Write-Host "=== AUDITING $($urlsToAudit.Count) LIVE URLS ==="

$liveResults = @()

foreach ($path in $urlsToAudit) {
    $fullUrl = "$liveBase$path"
    Write-Host "Fetching $fullUrl..."
    
    # Get headers
    $headerRaw = curl.exe -ILs --max-time 15 $fullUrl
    $statusLines = ($headerRaw | Select-String -Pattern '^HTTP/') -join ' -> '
    $lastStatus = ($headerRaw | Select-String -Pattern '^HTTP/\S+\s+(\d+)' | ForEach-Object { $_.Matches[0].Groups[1].Value }) | Select-Object -Last 1
    $finalLoc = ($headerRaw | Select-String -Pattern '^Location:\s*(.*)' | ForEach-Object { $_.Matches[0].Groups[1].Value }) | Select-Object -Last 1
    
    # Get HTML content
    $html = curl.exe -s --max-time 20 $fullUrl
    $size = $html.Length
    
    # Title
    $title = ''
    if ($html -match '(?si)<title>(.*?)</title>') {
        $title = $matches[1].Trim()
    }
    
    # Meta description
    $desc = ''
    if ($html -match '(?si)<meta\s+name=["'']description["'']\s+content=["''](.*?)["'']') {
        $desc = $matches[1].Trim()
    }
    
    # Canonical
    $canonical = ''
    if ($html -match '(?si)<link\s+rel=["'']canonical["'']\s+href=["''](.*?)["'']') {
        $canonical = $matches[1].Trim()
    }
    
    # H1
    $h1 = ''
    if ($html -match '(?si)<h1[^>]*>(.*?)</h1>') {
        $h1 = ($matches[1] -replace '<[^>]+>', ' ').Trim()
        $h1 = ($h1 -replace '\s+', ' ')
    }
    
    # WhatsApp links
    $waMatches = [regex]::Matches($html, '(?si)href=["''](https?://(?:api\.whatsapp\.com|wa\.me)/[^"'']*)["'']')
    $waLinks = @()
    foreach ($m in $waMatches) {
        $waLinks += $m.Groups[1].Value
    }
    
    # Tel links
    $telMatches = [regex]::Matches($html, '(?si)href=["''](tel:[^"'']*)["'']')
    $telLinks = @()
    foreach ($m in $telMatches) {
        $telLinks += $m.Groups[1].Value
    }
    
    # Mailto links
    $mailMatches = [regex]::Matches($html, '(?si)href=["''](mailto:[^"'']*)["'']')
    $mailLinks = @()
    foreach ($m in $mailMatches) {
        $mailLinks += $m.Groups[1].Value
    }
    
    # Forms
    $formMatches = [regex]::Matches($html, '(?si)<form([^>]*)>(.*?)</form>')
    $formsCount = $formMatches.Count
    
    # Social links
    $igMatches = [regex]::Matches($html, '(?si)href=["''](https?://(?:www\.)?instagram\.com/[^"'']*)["'']')
    $fbMatches = [regex]::Matches($html, '(?si)href=["''](https?://(?:www\.)?facebook\.com/[^"'']*)["'']')
    
    $obj = [PSCustomObject]@{
        Path = $path
        FullUrl = $fullUrl
        HttpStatus = $lastStatus
        StatusChain = $statusLines
        FinalLocation = $finalLoc
        Size = $size
        Title = $title
        H1 = $h1
        Canonical = $canonical
        Desc = $desc
        WhatsAppCount = $waLinks.Count
        WhatsAppSample = ($waLinks | Select-Object -First 1)
        TelCount = $telLinks.Count
        TelSample = ($telLinks | Select-Object -First 1)
        MailCount = $mailLinks.Count
        MailSample = ($mailLinks | Select-Object -First 1)
        FormsCount = $formsCount
        InstagramCount = $igMatches.Count
        FacebookCount = $fbMatches.Count
    }
    $liveResults += $obj
}

$liveResults | Export-Clixml -Path '.agents/teamwork/explorer_survey_live/live_audit_results.xml'

# Format summary table
$liveResults | Select-Object Path, HttpStatus, Size, Title, WhatsAppCount, FormsCount | Format-Table -AutoSize
