# Registro de temas · perfil personal de Nicolás Benítez

## Borradores y publicados

| Fecha sugerida | Tema | Formato | Id Buffer | Fuente | Estado |
|---|---|---|---|---|---|
| 2026-11-17 10:17 | Planillas: pedirle a la IA la fórmula de Excel (vencimiento de facturas) | Carrusel PDF, 7 láminas (01_formulas_excel_con_ia) | 6af862aae86a5789a6ac4f06 | — | Publicado (Nicolás) |
| 2026-11-17 10:52 | Ecommerce: 4 datos que tenés que mirar si vendés online (conversión, ticket promedio, carritos abandonados, costo por cliente nuevo; ejemplos con cuentas) | Infografía animada, video 6 s (02_ecommerce_4_datos) | 6af862abe86a5789a6ac4f23 | Cálculos propios de ejemplo | Programado a pedido de Nicolás |
| 2026-11-18 09:00 | IA en la tienda online: descripciones, preguntas de clientes, quejas en reseñas, asuntos de mails | Infografía animada, video 6 s (03_ia_tareas_tienda_online) | 6afc5b0a686bdd2a3c141ff2 | — | Borrador |
| 2026-11-19 09:00 | ¿Te conviene un 20 % de descuento? Con margen de 40 %, ganás la mitad y necesitás el doble de ventas | Infografía animada, video 6 s (04_descuento_conviene) | 6af862abe5a113497a860acb | Cálculo propio ($10.000, costo $6.000) | Borrador (reemplaza al carrusel del mail difícil) |
| 2026-11-20 09:00 | Carrito abandonado: envío a la vista, más formas de pago, compra sin cuenta, menos pasos | Infografía animada, video 6 s (05_carrito_abandonado) | 6afc5b0bddb326928b5df81c | Buenas prácticas generales de checkout (sin porcentajes) | Borrador |

## Casos reales de IA en Pana ya contados

(Marcar acá cuál de los casos de la sección 3 ya salió, para no repetirlo.)

- (El caso de la página de LinkedIn de Pana se armó para el 18/11 pero no salió: Nicolás prefirió un ejemplo general. Sigue disponible.) Sin contar: relevamiento de precios, presentación comercial y plan de expansión, flyers y estados de WhatsApp, lista de prospectos.

## Notas

- 2026-11-17: Nicolás eligió el formato **infografía animada** (ejemplos que mandó: "4 usos de Monte Carlo en Data Science" y "9 conceptos de probabilidad", GIF con tarjetas en grilla que se mueven) y el nicho **ecommerce + IA aplicada a negocios**. Rechazó la versión "reclamar un pago con IA" ("malísimo") y aprobó "4 datos si vendés online" ("mucho mejor"). Sin usar todavía: los carruseles 02 (recordatorio automático de pagos) y 03 (mail difícil).

- 2026-11-16: Nicolás pidió más precisión para gente que casi no usa IA: decir en qué IA, dónde se pega y qué se toca. El 02 quedó en 5 pasos numerados (Sheets, pedido en Claude o ChatGPT, Extensiones → Apps Script, Ejecutar, activador diario) y en el 01 y el 03 se agregó dónde pegar el pedido. El procedimiento del 02 no se pudo ejecutar desde la tarea: pedirle a Nicolás que lo pruebe.

- 2026-11-16 (pedido de Nicolás sobre el carrusel del miércoles): ejemplos generales que le sirvan a cualquiera (por ejemplo, un mail automático a clientes con pago atrasado) antes que el caso propio, y todo más corto: que se lea y se entienda rápido.

- 2026-11-16 (tarde): Nicolás pidió que todo sea carrusel PDF, lindo de ver, sin tecnicismos, que frene el scroll y haga interactuar. Se creó `kit_nicolas.py` y los 3 borradores pasaron a carrusel con texto corto. Portadas usadas: buscador tachado (Excel), lista de semanas (automatizar), mail a medio escribir (mails).

- 2026-11-16: Nicolás pidió enfocar el perfil en gente de oficina (Excel, Gmail, planillas, automatizar y acelerar trabajo) con ejemplos generales, buscando que los posts se compartan. Se rehicieron los 3 borradores de la semana del 16/11; los textos viejos están en `descartados/2026-11-16_borradores_viejos.md`.

- 2026-11-14: Buffer rechaza `metadata.linkedin.firstComment` en el plan gratis ("LinkedIn first comment requires a paid plan"). Los borradores se crean sin primer comentario y el link de la fuente se le pasa a Nicolás en el aviso para que lo pegue a mano como primer comentario al publicar.
- 2026-11-14: "Claude Meetings" (aparece en agregadores con fecha 10 a 12/11) no se pudo verificar en una página oficial (el acceso a claude.com y a support.claude.com estuvo bloqueado desde la tarea): no se usó.

## Ideas (foco oficina desde el 16/11/2026)

- Limpiar una planilla desordenada: espacios de más, mayúsculas, fechas como texto, duplicados (ESPACIOS, NOMPROPIO, quitar duplicados).
- BUSCARV / BUSCARX: cruzar dos planillas pidiéndole a la IA la fórmula y cómo detectar los #N/A.
- Tabla dinámica en 3 pasos: qué pedirle a la IA para que te diga cómo armarla con tus columnas.
- Resumir un hilo largo de mails en 5 líneas: decisiones, pendientes y quién tiene que hacer qué.
- De una reunión a la minuta: el pedido para pasar notas sueltas a acuerdos, responsables y fechas.
- Reporte semanal: de pegar números todos los lunes a una tarea que se repite sola.
- Qué no pegar nunca en un chat de IA (datos de clientes, cuentas, contraseñas) y qué hacer en cambio.
- Macros o Apps Script sin saber programar: pedir el código, probarlo en una copia, entender qué hace.
- Responder reclamos de clientes con un tono firme y amable (plantilla).
- Revisar un documento antes de mandarlo: errores, contradicciones, lo que falta.
- Casos reales todavía sin contar: relevamiento de precios en comercios online (sin precios ni márgenes), presentación comercial en PDF, flyers y estados de WhatsApp, lista semanal de prospectos con datos públicos, medición semanal de métricas.

## Ideas anteriores (foco IA en general, hasta el 16/11/2026)

- Cómo una tarea de Claude arma la semana de LinkedIn de una empresa (el caso de Pana, paso a paso).
- Qué le delego a la IA y qué no: verificar datos técnicos, precios y lo que sale con mi nombre.
- Errores que cometió la IA y cómo los detecté (texto "mordido", un dato de condiciones de venta).
- De 10 posts por semana a 5: lo que dicen los datos sobre frecuencia en LinkedIn.
- Cómo pedirle a la IA un relevamiento de precios de mercado y qué revisar después.
