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

- Lunes a viernes, **2 posts por día: 9:00 y 18:00** (hora de Argentina, `-03:00`).
- 9:00: infografía (imagen 1080 × 1350). 18:00: texto de valor o debate; a veces otra infografía.
- Mezcla semanal orientativa: 5 o 6 infografías, 2 o 3 textos técnicos, 2 debates.
- Antes de cargar, revisar la cola (`list_posts` con status `scheduled`). Si quedan posts de la
  semana siguiente ya programados, completar solo los huecos y no pasar de 10.
- **Si la semana siguiente ya tiene sus 10 posts programados, no armar nada:** terminar con un
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

- Primera línea que enganche y explique el tema. Párrafos cortos. Viñetas con "·".
- 3 o 4 hashtags al final (ej. #Iluminación #Arquitectura #Instaladores #TiraLED).
- Sin emojis, o como mucho uno.
- Cierre con pregunta (debates) o con "Consultanos" cuando hay producto.
- **Ojo con los links automáticos de Buffer:** cualquier "palabra.palabra" pegada (como "1.er" o
  "2.º") se convierte en link. Escribir "primer", "segundo", etc. Después de crear cada post,
  revisar que en `metadata.annotations` no aparezca ningún `type: "url"` que no sea un link real.

## 7. Diseño de las infografías

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
  y guardar PNG con `optimize=True` (queda en ~40 KB).

## 8. Paso a paso de cada sábado

1. Leer este archivo y `linkedin/temas.md`.
2. Revisar la cola de Buffer y calcular las 10 fechas de la semana siguiente (lunes a viernes,
   9:00 y 18:00).
3. Elegir los temas, investigar y verificar los datos.
4. Escribir los textos y diseñar las infografías con el kit. Revisar cada imagen.
5. Subir las imágenes al repo: `add_repo benzprog/Email-Marketing` con acceso push, clonar,
   copiar a `linkedin/semana-AAAA-MM-DD/`, commit y push a `main`.
6. Programar en Buffer con `create_post`: `mode: customScheduled`, `schedulingType: automatic`,
   `dueAt` como `AAAA-MM-DDT09:00:00-03:00`, y la imagen en `assets` con su `altText`.
   Confirmar en la respuesta que la imagen figura con `width: 1080` y `height: 1350`.
   Si la imagen no se lee, no programar ese post sin imagen: reintentar o reemplazarlo.
7. Anotar la semana en `linkedin/temas.md` (fecha, hora, tema, formato, id de Buffer) y hacer push.
8. Terminar con un resumen corto: tabla de la semana (día, hora, tema), qué se verificó, y
   "datos que necesito" si hubo temas de producto que quedaron afuera.

## 9. Qué no hacer

- No publicar nada al instante (`shareNow`) salvo que Nicolás lo pida.
- No comentar, reaccionar ni interactuar con otras cuentas: eso va contra las reglas de LinkedIn.
- No borrar ni editar posts ya publicados.
- Si algo falla (Buffer desconectado, push rechazado), no dejar la semana a medias en silencio:
  programar lo que esté completo y explicar en el resumen qué faltó y por qué.
