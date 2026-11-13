# Protocolo Canva y Checklist de QA Visual

## 1. Protocolo Transaccional de Canva (`canva-edit-design`)

Cuando se edite un diseño existente de Canva (por ID o URL):
1. **Iniciar transacción:** Llamar a `start-editing-transaction` con el `design_id`. Guardar `transaction_id` y `pages`. Mostrar siempre la miniatura inicial.
2. **Verificar páginas responsivas:** Si una página tiene `is_responsive: true`, solo usar `update_title`, `replace_text`, `update_fill`, `delete_element` o `find_and_replace_text`.
3. **Ejecutar operaciones:** Agrupar los cambios en una sola llamada a `perform-editing-operations`.
   - *Limitaciones de la API:* No se puede cambiar la familia tipográfica, agregar nuevas cajas de texto, cambiar el color de fondo ni reordenar páginas. Si el usuario pide eso, avisar qué debe ajustarse manualmente en el editor de Canva.
4. **Compuerta de aprobación:** Mostrar la miniatura resultante y la lista de cambios en lenguaje simple. **Esperar confirmación explícita** antes de llamar a `commit-editing-transaction`.
5. **Cierre:** Tras `commit-editing-transaction`, entregar el enlace de edición en Canva. Si se descarta, ejecutar `cancel-editing-transaction`.

## 2. Checklist de QA antes de entregar al usuario

- [ ] **Paleta:** ¿Solo aparecen blanco `#FFFFFF`, gama azul hasta `#0950F6` y amarillo `#FFEC01` (≤15%)?
- [ ] **Sombras:** ¿Las sombras están teñidas de azul suave (`#BACEFD` / `#0950F6` baja opacidad) y no son negras ni grises?
- [ ] **Legibilidad:** Si lleva texto o se usará como fondo para texto `Anton`/`Outfit`, ¿hay suficiente espacio negativo blanco o azul limpio?
- [ ] **Datos reales:** ¿Cualquier tarifa, franja horaria o servicio mencionado coincide con `https://www.enviosdosruedas.com/`?
- [ ] **Sin artefactos IA:** ¿Sin texto deformado ni logos inventados dentro de la imagen generada?
