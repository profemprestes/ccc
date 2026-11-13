# Scrape and compare live site vs local files

$pages = @(
    @{ Name = 'Home'; LiveUrl = 'https://www.enviosdosruedas.com/'; LocalFile = 'envios/home.html' },
    @{ Name = 'Contacto'; LiveUrl = 'https://www.enviosdosruedas.com/contacto/'; LocalFile = 'envios/contacto.html' },
    @{ Name = 'Cotizar'; LiveUrl = 'https://www.enviosdosruedas.com/cotizar/'; LocalFile = 'envios/cotizar.html' },
    @{ Name = 'Logistica DosRuedas'; LiveUrl = 'https://www.enviosdosruedas.com/logistica-dosruedas/'; LocalFile = 'envios/logistica-dosruedas.html' },
    @{ Name = 'MarDelivery'; LiveUrl = 'https://www.enviosdosruedas.com/mardelivery/'; LocalFile = 'envios/mardelivery.html' },
    @{ Name = 'Nosotros - Redes'; LiveUrl = 'https://www.enviosdosruedas.com/nosotros/nuestras-redes/'; LocalFile = 'envios/nosotrosnuestras-redes.html' },
    @{ Name = 'Nosotros - FAQ'; LiveUrl = 'https://www.enviosdosruedas.com/nosotros/preguntas-frecuentes/'; LocalFile = 'envios/nosotrospreguntas-frecuentes.html' },
    @{ Name = 'Nosotros - Sobre Nosotros'; LiveUrl = 'https://www.enviosdosruedas.com/nosotros/sobre-nosotros/'; LocalFile = 'envios/nossobresobre-nosotros.html' },
    @{ Name = 'Politica de Privacidad'; LiveUrl = 'https://www.enviosdosruedas.com/politica-de-privacidad/'; LocalFile = 'envios/politicade-privacidad.html' },
    @{ Name = 'Servicios - Deposito Fulfillment'; LiveUrl = 'https://www.enviosdosruedas.com/servicios/deposito-fulfillment/'; LocalFile = 'envios/serviciosdeposito-fulfillment.html' },
    @{ Name = 'Servicios - Empresas CC'; LiveUrl = 'https://www.enviosdosruedas.com/servicios/empresas-cuenta-corriente/'; LocalFile = 'envios/serviciosempresas-cuenta-corriente.html' },
    @{ Name = 'Servicios - Envios Express'; LiveUrl = 'https://www.enviosdosruedas.com/servicios/envios-express/'; LocalFile = 'envios/serviciosenvios-express.html' },
    @{ Name = 'Servicios - Envios LowCost'; LiveUrl = 'https://www.enviosdosruedas.com/servicios/envios-lowcost/'; LocalFile = 'envios/serviciosenvios-lowcost.html' },
    @{ Name = 'Servicios - Envios Flex'; LiveUrl = 'https://www.enviosdosruedas.com/servicios/enviosflex/'; LocalFile = 'envios/serviciosenviosflex.html' },
    @{ Name = 'Terminos y Condiciones'; LiveUrl = 'https://www.enviosdosruedas.com/terminos-y-condiciones/'; LocalFile = 'envios/terminos-y-condiciones.html' },
    @{ Name = 'Cobertura (Live Only)'; LiveUrl = 'https://www.enviosdosruedas.com/cobertura/'; LocalFile = $null },
    @{ Name = 'Guias Envios Flex (Live Only)'; LiveUrl = 'https://www.enviosdosruedas.com/guias/envios-flex-mar-del-plata/'; LocalFile = $null },
    @{ Name = 'Servicios Hub (Live Only)'; LiveUrl = 'https://www.enviosdosruedas.com/servicios/'; LocalFile = $null },
    @{ Name = 'Plan Emprendedores (Redirects)'; LiveUrl = 'https://www.enviosdosruedas.com/servicios/plan-emprendedores/'; LocalFile = $null },
    @{ Name = 'Envios Contrareembolso (Redirects)'; LiveUrl = 'https://www.enviosdosruedas.com/servicios/envios-contrareembolso/'; LocalFile = $null },
    @{ Name = 'Local Extra: html.html'; LiveUrl = $null; LocalFile = 'envios/html.html' }
)

function Extract-Meta($html) {
    $res = @{}
    if ($html -match '(?i)<title>(.*?)</title>') { $res['Title'] = $matches[1].Trim() } else { $res['Title'] = '' }
    if ($html -match '(?i)<meta\s+name=["'']description["'']\s+content=["''](.*?)["'']') { $res['Desc'] = $matches[1].Trim() } else { $res['Desc'] = '' }
    if ($html -match '(?i)<link\s+rel=["'']canonical["'']\s+href=["''](.*?)["'']') { $res['Canonical'] = $matches[1].Trim() } else { $res['Canonical'] = '' }
    if ($html -match '(?i)<h1[^>]*>(.*?)</h1>') { $res['H1'] = ($matches[1] -replace '<[^>]+>', '').Trim() } else { $res['H1'] = '' }
    return $res
}

$reportData = @()

foreach ($p in $pages) {
    Write-Host "Analyzing $($p.Name)..."
    $liveMeta = $null
    $liveSize = 0
    $liveStatus = 'N/A'
    
    if ($p.LiveUrl) {
        $headers = curl.exe -ILs --max-time 10 $p.LiveUrl
        $liveStatus = (($headers | Select-String -Pattern '^HTTP/') -join ' -> ')
        $liveHtml = curl.exe -s --max-time 15 $p.LiveUrl
        $liveSize = $liveHtml.Length
        $liveMeta = Extract-Meta $liveHtml
    }
    
    $localMeta = $null
    $localSize = 0
    if ($p.LocalFile -and (Test-Path $p.LocalFile)) {
        $localHtml = Get-Content -Path $p.LocalFile -Raw
        $localSize = $localHtml.Length
        $localMeta = Extract-Meta $localHtml
    }

    $reportData += [PSCustomObject]@{
        Page = $p.Name
        LiveUrl = $p.LiveUrl
        LiveStatus = $liveStatus
        LiveSize = $liveSize
        LiveTitle = if ($liveMeta) { $liveMeta['Title'] } else { 'N/A' }
        LiveH1 = if ($liveMeta) { $liveMeta['H1'] } else { 'N/A' }
        LocalFile = $p.LocalFile
        LocalSize = $localSize
        LocalTitle = if ($localMeta) { $localMeta['Title'] } else { 'N/A' }
        LocalH1 = if ($localMeta) { $localMeta['H1'] } else { 'N/A' }
    }
}

$reportData | Export-Clixml -Path '.agents/teamwork/explorer_survey_live/page_comparison.xml'
$reportData | Format-Table Page, LiveSize, LocalSize, LiveTitle, LocalTitle -AutoSize
