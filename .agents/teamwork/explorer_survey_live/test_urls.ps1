$urls = @(
    'https://www.enviosdosruedas.com',
    'https://www.enviosdosruedas.com/',
    'https://enviosdosruedas.com',
    'http://www.enviosdosruedas.com',
    'http://enviosdosruedas.com',
    'https://www.enviosdosruedas.com/servicios/envios-express',
    'https://www.enviosdosruedas.com/servicios/envios-lowcost',
    'https://www.enviosdosruedas.com/servicios/enviosflex',
    'https://www.enviosdosruedas.com/servicios/deposito-fulfillment',
    'https://www.enviosdosruedas.com/cotizar',
    'https://www.enviosdosruedas.com/servicios/empresas-cuenta-corriente',
    'https://www.enviosdosruedas.com/servicios/plan-emprendedores',
    'https://www.enviosdosruedas.com/servicios/envios-contrareembolso',
    'https://www.enviosdosruedas.com/cobertura',
    'https://www.enviosdosruedas.com/logistica-dosruedas',
    'https://www.enviosdosruedas.com/mardelivery',
    'https://www.enviosdosruedas.com/guias/envios-flex-mar-del-plata',
    'https://www.enviosdosruedas.com/contacto',
    'https://www.enviosdosruedas.com/nosotros/sobre-nosotros',
    'https://www.enviosdosruedas.com/nosotros/preguntas-frecuentes',
    'https://www.enviosdosruedas.com/nosotros/nuestras-redes',
    'https://www.enviosdosruedas.com/politica-de-privacidad',
    'https://www.enviosdosruedas.com/terminos-y-condiciones',
    'https://www.enviosdosruedas.com/revisar',
    'https://www.enviosdosruedas.com/admin',
    'https://www.enviosdosruedas.com/api',
    'https://www.enviosdosruedas.com/servicios/envios-flex' # testing hyphenated version too
)

foreach ($u in $urls) {
    $out = curl.exe -ILs --max-time 10 $u
    $statusLines = ($out | Select-String -Pattern '^HTTP/') -join ' -> '
    $location = ($out | Select-String -Pattern '^Location:') -join ' ; '
    Write-Output "$u | $statusLines | $location"
}
