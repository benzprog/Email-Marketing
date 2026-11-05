# LinkedIn de Pana Iluminación · instrucciones para la tarea semanal

Este archivo es la referencia completa para armar y programar cada semana los posts de la
página de LinkedIn de Pana Iluminación. Lo lee la tarea programada de Claude de cada sábado.
Si Nicolás pide un cambio de criterio, se actualiza acá.

## 1. Cuentas y herramientas

- **Buffer** (conector de Claude). Organización `6adb923718fd4ea5a464763e`, canal LinkedIn Page
  "Pana Iluminacion" `6adb9293778b240e2f9fed7a`. Zona horaria America/Argentina/Buenos_Aires (UTC-3).
- **Plan gratis de Buffer: máximo 10 posts programados a la vez.** Por eso se arma de a una semana.
- **Imágenes:** este repo público `benzprog/Email-Marketing`, carpeta `linkedin/semana-AAAA-MM-DD`
  (fecha del lunes). Buffer toma cada imagen desde
  `https://raw.githubusercontent.com/benzprog/Email-Marketing/main/linkedin/<carpeta>/<archivo>.png`.
  El conector de Google Drive NO sirve para subir imágenes (son demasiado grandes para pasarlas por el conector).
- **Kit visual:** `linkedin/kit/` (pana_style.py, logos, tipografía Archivo, piezas de ejemplo).

## 2. Calendario

- **Desde la semana del 9/11/2026: 5 posts por semana, uno por día de lunes a viernes, a las 11:00**
  (hora de Argentina, `-03:00`). Se decidió el 5/11/2026 con los datos de la sección 8:
  publicar dos veces por día en una página de empresa le resta alcance a cada post (lo recomendado
  son 3 a 5 por semana con 24 h de diferencia) y la franja de 9 a 12 es la que mejor rinde en LinkedIn.
  Historial: 9:00 y 18:00 hasta el 27/10; 8:00 y 15:30 hasta el 6/11.
- Mezcla semanal (cada semana se ajusta con la medición de la sección 8):
  · 2 o 3 **carruseles PDF** (el formato de mejor rendimiento en páginas de empresa).
  · 1 **foto real de Pana** (depósito, equipo, entregas, obras de clientes) si Nicolás mandó material;
    si no, una infografía de una sola imagen o una pieza con foto del kit.
  · 1 infografía de una imagen o un debate corto.
- Antes de cargar, revisar la cola (`list_posts` con status `scheduled`). Si quedan posts de la
  semana siguiente ya programados, completar solo los huecos y no pasar de 5.
- **Si la semana siguiente ya tiene sus 5 posts programados, no armar nada:** terminar con un
  resumen de una línea ("La semana del … ya estaba completa") y no adelantar la semana posterior.

## 3. Público, tono y lenguaje

- Público: arquitectos y estudios, instaladores y electricistas, constructoras, casas de
  electricidad y comercios, municipios (alumbrado público). Clientes finales en segundo plano.
- **Español rioplatense** (vos: "pedí", "consultanos", "fijate"). Profesional y directo, sin
  exagerar ni vender humo.
- **Términos que se usan en Argentina.** Sí: dicroica, tira LED, fuente switching, buña,
  cielorraso, dimmer para LED, titilar, parpadeo, perfil de aluminio, difusor, plafón, aplique.
  No: tecnicismos en inglés cuando hay palabra de acá ("flicker", "trailing edge", "wall washer",
  "downlight" sin explicar), ni nombres raros como "aplique bidireccional que lava hacia arriba".
  Si una métrica solo existe en inglés o con sigla (IRC, PstLM, SVM, L70), se explica en castellano.

## 4. Qué temas sí y qué temas no

- **Prohibido lo trillado**, lo que sabe todo el mundo: luz cálida/neutra/fría básica, "el LED
  ahorra energía", "cambiá tus lámparas por LED", tips genéricos de decoración.
- **Sí:** temas de nicho, técnicos y accionables, que un profesional guarde o comparta.
  Ejemplos de nivel: IRC y R9, PstLM y SVM, L70/B50, carga mínima de transformadores y dimmers,
  ángulo de apertura, código IP, cálculo de fuentes, caída de tensión en tiras.
- Mirar `linkedin/temas.md`: **no repetir** temas ya publicados y tomar ideas del banco de temas.
- Pilares para variar: educación técnica, producto (solo con datos reales), obra y proyecto,
  venta a comercios y obra (cotizaciones, compra sin mínimo para minoristas en Tenaruz).

## 5. Exactitud (lo más importante)

- Cada dato técnico tiene que ser correcto y verificable. Ante la duda, buscar en la web y usar
  fuentes serias (normas, fabricantes, organismos). Si no se puede verificar, no se publica.
- Valores normativos: aclarar de dónde salen (por ejemplo "referencia de la Unión Europea").
- **No inventar especificaciones de productos.** Datos confirmados de Pana:
  - Tenaruz: Bipin LED G9 6 W (3000/4000/6000 K); MR16 LED 12 V 5 W; dicroica GU10 dimerizable;
    Stick LED T45 E27; fuentes switching 12 V y 24 V; fuente TZ-FSLIM24-5A (entrada 175–250 V,
    salida 24 Vcc 5 A); amplificador para tiras DC 5–24 V con salida pico 12 A; estaca de aluminio GU10.
  - TREFI (lámparas LED), TBCIN (tubos LED T8), Vonderk (spots empotrables, ej. SCL210 con fuente
    incluida), MAXILED (alumbrado público, líneas Eco 3 Flex y Eco Flex Pro).
  - Contacto de Pana para cierres de venta: 11 6288-3659 (usar con moderación).
- Si un post de producto necesita datos que no están acá (potencias, lúmenes, IP, precios), **no
  se arma**: se anota en el resumen final como "datos que necesito" para que Nicolás los pase.

## 6. Formato de los textos

- **Las dos primeras líneas son el gancho**: es lo único que se ve antes de "…ver más". Tienen que
  plantear un problema concreto de obra o un dato que sorprenda ("IP65 no es sumergible").
  Nada de arranques genéricos ("Hoy queremos contarte…").
- Largo: entre 1000 y 1500 caracteres en los posts técnicos (es la franja que más interacción
  junta); debates y fotos, más cortos. Párrafos cortos. Viñetas con "·".
- **3 hashtags** al final (ya no suman alcance, pero ayudan a ordenar). Sin emojis, o como mucho uno.
- **Sin links en el cuerpo del post** (en páginas de empresa pierden entre 25 y 40 % de alcance).
  Si hace falta un link, va en el primer comentario (`metadata.linkedin.firstComment`).
- Cierre con una pregunta concreta que se pueda contestar en una línea (los comentarios en la
  primera hora son lo que más empuja el alcance) o con "Guardalo para la próxima obra" en los
  carruseles (lo guardado pesa más que un "me gusta"). "Consultanos" cuando hay producto.
- **Ojo con los links automáticos de Buffer:** cualquier "palabra.palabra" pegada (como "1.er" o
  "2.º") se convierte en link. Escribir "primer", "segundo", etc. Después de crear cada post,
  revisar que en `metadata.annotations` no aparezca ningún `type: "url"` que no sea un link real.

## 7. Diseño de las infografías

### Carruseles PDF (formato principal)

- Láminas de 1080 × 1350 armadas con `kit/pana_style.py` y exportadas con `kit/carrusel.py`
  (`exportar([láminas], "semana-AAAA-MM-DD/01_tema.pdf")`), que además guarda la portada en JPG.
- 6 a 9 láminas, **una idea por lámina** y letra grande (se leen en el celular).
  · Lámina 1: el gancho, una frase grande y una imagen o número. Tiene que dar ganas de deslizar.
  · Láminas del medio: un paso, un dato o un error por lámina. Numeradas ("2/7") en una esquina.
  · Última: resumen en una línea + "Guardalo para la próxima obra" + CONSULTANOS.
- Temas que rinden en carrusel: paso a paso de cálculo, "5 errores en obra", checklists,
  comparaciones antes/después, cómo leer una ficha técnica.
- En Buffer va como documento: `assets: [{document: {url, title, thumbnailUrl}}]` con el PDF desde
  raw.githubusercontent y la portada JPG como `thumbnailUrl`. El `title` es lo que LinkedIn muestra
  arriba del carrusel: corto y claro. Confirmar en la respuesta `metadata.type: "carousel"` y
  `mimeType: "application/pdf"` (Buffer muestra `numPages: 0` hasta publicar; es normal).
- Después de que se publique el primer carrusel, revisar con `get_post` que haya quedado `sent` y
  sin `error`. Si falló, volver a infografías de una imagen y avisarle a Nicolás.

### Infografías de una imagen

- 1080 × 1350 px. Usar `kit/pana_style.py` (paleta, Archivo, logo, helpers) y copiar el estilo de
  `kit/ejemplos/`: logo arriba a la izquierda, etiqueta en mayúsculas espaciadas arriba a la
  derecha, antetítulo, título de 64–72 px, raya amarilla, contenido, pie con "Pana Iluminación" y
  "CONSULTANOS →".
- Alternar fondo hueso y fondo negro. Amarillo solo como acento.
- Colores planos (sin degradés grandes): después se comprime a 96 colores.
- Gráficos y diagramas a escala real (si hay números, la ilustración tiene que respetarlos).
- **Revisar cada imagen mirándola** (abrir el PNG) antes de subirla: nada superpuesto, nada
  cortado, nada de cuadraditos por caracteres que la tipografía no tiene (✓ ✕ se dibujan a mano).
- Exportar: `img.quantize(colors=96, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)`
  y guardar PNG con `optimize=True` (queda en ~40 KB). Las piezas con foto van en JPEG calidad 90.

### Que no parezca hecho por IA (pedido de Nicolás)

Nicolás marcó que una pieza "se sentía muy de IA". Lo que delata eso: listas con rayitas
divisorias en todas las piezas, etiquetas en mayúsculas espaciadas por todos lados, dos columnas
iguales, demasiado texto y ninguna imagen. Para que parezca de diseño:
- Una idea por pieza y poco texto. Si hay que explicar mucho, va en el texto del post.
- Variar la composición de semana a semana: foto a sangre con frase grande, número gigante,
  diagrama protagonista, comparación lado a lado. No repetir la misma grilla en todas.
- Usar las fotos de ambientes de `kit/fotos/` cuando el tema lo permita (siempre con un velo
  oscuro para que el texto se lea). Ejemplo: `kit/ejemplos/pieza_quienes_somos.py`.
- Usar los 8 puntos del logo como recurso gráfico (con el último en amarillo) en vez de la raya.
- Etiquetas en mayúsculas espaciadas: como mucho una por pieza.

## 8. Medición: qué funciona en la página de Pana

Cada sábado, antes de elegir temas:
1. `list_posts` con status `sent`, `includeMetrics: true`, de las últimas dos semanas.
2. Anotar en `temas.md`, en la tabla de resultados, impresiones, alcance, reacciones,
   comentarios y compartidos de cada post (los de la semana anterior ya tienen datos firmes).
3. Repetir lo que funcionó: más del formato y del tipo de tema con más alcance e interacción;
   dejar de lado lo que quede abajo dos semanas seguidas. Contarlo en el resumen en una línea.

Ojo con sacar conclusiones con números chicos: con menos de 100 impresiones por post, una
diferencia de 10 o 20 es ruido. Mirar tendencias de varias semanas, no un post suelto.

Lo que dicen los estudios (resumen del 5/11/2026, ver detalle en `temas.md`):
- En páginas de empresa, los carruseles PDF tienen la mayor tasa de interacción (7 % contra 5,3 % de
  una imagen sola y 4,5 % de solo texto; Socialinsider 2026, 2,45 millones de posts de páginas).
- Las fotos con caras de personas rinden más que las piezas gráficas. El mejor post de Pana hasta
  ahora fue una foto real del depósito (91 impresiones, 2 compartidos).
- Los comentarios en la primera hora y que el equipo de Pana comparta el post desde su perfil
  personal multiplican el alcance: una página de empresa sola llega a muy poca gente.

## 9. Paso a paso de cada sábado

1. Leer este archivo y `linkedin/temas.md`. Medir la semana anterior (sección 8).
2. Revisar la cola de Buffer y calcular las 5 fechas de la semana siguiente (lunes a viernes,
   11:00).
3. Elegir los temas, investigar y verificar los datos.
4. Escribir los textos y diseñar las infografías con el kit. Revisar cada imagen.
5. Subir las imágenes al repo: `add_repo benzprog/Email-Marketing` con acceso push, clonar,
   copiar a `linkedin/semana-AAAA-MM-DD/`, commit y push a `main`.
6. Programar en Buffer con `create_post`: `mode: customScheduled`, `schedulingType: automatic`,
   `dueAt` como `AAAA-MM-DDT11:00:00-03:00`, y la imagen en `assets` con su `altText` (o el carrusel
   como `document`, ver sección 7). Confirmar en la respuesta que la imagen figura con `width: 1080`
   y `height: 1350`, o que el carrusel figura como `carousel` con `application/pdf`.
   Si la imagen no se lee, no programar ese post sin imagen: reintentar o reemplazarlo.
7. Anotar la semana en `linkedin/temas.md` (fecha, hora, tema, formato, id de Buffer) y hacer push.
8. Terminar con un resumen corto: tabla de la semana (día, hora, tema, formato), qué rindió mejor la
   semana anterior, qué se verificó, y "datos que necesito" si hubo temas de producto que quedaron
   afuera o si hacen falta fotos reales.

## 10. Qué no hacer

- No publicar nada al instante (`shareNow`) salvo que Nicolás lo pida.
- No comentar, reaccionar ni interactuar con otras cuentas: eso va contra las reglas de LinkedIn.
- No borrar ni editar posts ya publicados.
- Si algo falla (Buffer desconectado, push rechazado), no dejar la semana a medias en silencio:
  programar lo que esté completo y explicar en el resumen qué faltó y por qué.
