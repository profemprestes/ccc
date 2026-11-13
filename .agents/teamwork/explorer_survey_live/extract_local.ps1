$files = Get-ChildItem -Path 'envios' -Filter '*.html'
$results = foreach ($f in $files) {
    $content = Get-Content -Path $f.FullName -Raw
    $title = if ($content -match '<title>(.*?)</title>') { $matches[1] } else { 'NO TITLE' }
    $canonical = if ($content -match '<link\s+rel=["'']canonical["'']\s+href=["''](.*?)["'']') { $matches[1] } else { 'NO CANONICAL' }
    $h1 = if ($content -match '<h1[^>]*>(.*?)</h1>') { $matches[1] -replace '<[^>]+>', '' } else { 'NO H1' }
    [PSCustomObject]@{
        File = $f.Name
        Title = $title
        Canonical = $canonical
        H1 = $h1.Trim()
    }
}
$results | Format-Table -Wrap
