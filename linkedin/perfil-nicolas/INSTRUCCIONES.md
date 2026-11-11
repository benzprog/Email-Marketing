# Perfil personal de Nicolás Benítez en LinkedIn · instrucciones para la tarea semanal

Lo lee la tarea programada de cada sábado "LinkedIn Nicolás personal". Si Nicolás pide un cambio de
criterio, se actualiza acá. Es un trabajo aparte de la página de Pana (`linkedin/INSTRUCCIONES.md`).

## 1. Cuenta y modo de publicación

- **Buffer**, organización `6adb923718fd4ea5a464763e`, canal **perfil personal "Nicolas Benítez"**
  `6af3120362b70b94b0e1bde2` (tipo `profile`). Zona horaria America/Argentina/Buenos_Aires (UTC-3).
- **Los posts quedan como BORRADORES** (`saveToDraft: true`), nunca programados ni publicados: salen
  con el nombre de Nicolás y él los revisa y los programa con un clic. Pedido de Nicolás, 11/11/2026.
- Cada borrador lleva igual la fecha sugerida (`mode: customScheduled`, `dueAt`, `schedulingType:
  automatic`) para que solo tenga que aprobarlo. Si Buffer rechaza la fecha en un borrador, crearlo
  sin fecha y poner el día sugerido en el resumen.
- Plan gratis de Buffer: máximo 10 posts programados a la vez entre los dos canales. Antes de crear,
  revisar con `list_posts` (status `draft` y `scheduled`, este canal) que no queden borradores viejos
  sin usar: si hay, no duplicar el tema y avisarlo en el resumen.

## 2. Calendario

- **3 posts por semana: martes, miércoles y jueves a las 9:00** (`-03:00`) de la semana siguiente.
  Separados de la página de Pana (11:00) para que no compitan entre sí.

## 3. Tema: IA aplicada al trabajo (pedido de Nicolás, 11/11/2026)

Nicolás quiere hablar de **Claude, IA en general, novedades y IA aplicada al trabajo, con contenido de
valor**. Mezcla semanal:

1. **Martes · Novedad de la semana.** Un lanzamiento o noticia de IA de los últimos 7 a 10 días (Claude
   y Anthropic primero; también OpenAI, Google, Microsoft, Meta u otras si es lo más relevante) y **qué
   cambia para alguien que trabaja en una pyme**. Nada de "es una revolución": qué hace, para qué sirve
   y cuál es el límite.
2. **Miércoles · IA aplicada al trabajo (caso real).** Lo que Nicolás hizo de verdad con Claude en Pana,
   contado en primera persona y paso a paso. Material verificable en este repo y en su historial:
   · La página de LinkedIn de Pana se arma sola: una tarea programada de Claude investiga temas,
     verifica datos técnicos, diseña carruseles e infografías, los sube y los programa en Buffer cada sábado.
   · Medición semanal de métricas y cambios de estrategia con datos (de 10 posts por semana a 5; video
     y carruseles como formatos principales).
   · Relevamiento de precios al público en comercios online para comparar márgenes.
   · Presentación comercial en PDF y plan de expansión comercial armados con Claude.
   · Flyers, piezas para estado de WhatsApp y textos comerciales.
   · Lista semanal de prospectos con datos públicos.
   Contar el problema, cómo se resolvió, cuánto tiempo ahorra (solo si Nicolás dio el dato) y qué
   salió mal o hubo que corregir (por ejemplo: textos que se veían "mordidos" y se rehicieron con texto
   vectorial; un post que decía "sin mínimo" y se corrigió). **No inventar números, tiempos ni anécdotas.**
3. **Jueves · Contenido de valor práctico.** Algo que el lector pueda usar hoy: cómo escribir un buen
   pedido (prompt) para una tarea concreta del trabajo, cómo revisar lo que devuelve la IA, qué tareas
   conviene delegar y cuáles no, cómo cuidar datos sensibles, cómo pasar de un chat a una tarea
   automática. Con un ejemplo concreto del rubro (comercio, distribución, ventas B2B).

Cada 2 semanas, el post del miércoles o del jueves puede ser un **carrusel PDF** de 5 a 7 láminas
(`linkedin/kit/html_kit.py`) con estética neutra: sin el logo de Pana en la portada, firmado
"Nicolás Benítez" en el pie. Ejemplo de tema: "Cómo armé un equipo de marketing que trabaja los sábados".

## 4. Exactitud

- **Toda novedad se verifica en la fuente oficial** (anthropic.com/news, docs.claude.com, support.claude.com,
  blogs oficiales de cada empresa) o en medios serios, y se abre la página: un resultado de búsqueda no
  alcanza. Fecha, nombre exacto del producto y qué incluye. Si no se puede confirmar, no se publica.
- No afirmar precios, planes ni disponibilidad en Argentina sin confirmarlo en la fuente.
- El link de la fuente va en el **primer comentario** (`metadata.linkedin.firstComment`), no en el cuerpo.
- Los casos de Pana se cuentan solo con lo que consta en este repo o lo que Nicolás haya dicho.

## 5. Voz y formato

- **Primera persona, rioplatense, cercano y concreto** (vos, "probé", "me pasó"). Como alguien de una
  pyme de iluminación que usa IA todos los días, no como un gurú.
- Prohibido: "revolución", "cambia todo", "el futuro es hoy", listas de 10 herramientas, promesas.
- Primeras dos líneas = gancho (lo que se ve antes de "…ver más"). 800 a 1300 caracteres.
  Párrafos cortos, viñetas con "·", sin emojis o uno como mucho, 3 hashtags al final.
- Cierre con una pregunta concreta para que comenten.
- **Ojo con los links automáticos de Buffer** ("palabra.palabra" pegada, por ejemplo "Claude.ai" o
  "1.er"): escribir "Claude" o "claude punto ai" y "primer". Revisar `metadata.annotations` después de crear.

## 6. Qué no hacer

- No publicar ni programar: solo borradores.
- No mencionar clientes, precios, márgenes, datos de la lista mayorista ni planillas internas de Pana.
- No pegar prompts que contengan datos internos.
- No comentar, reaccionar ni escribirle a nadie desde el perfil.
- No hablar mal de otras empresas ni de otras herramientas.

## 7. Paso a paso de cada sábado

1. Leer este archivo y `linkedin/perfil-nicolas/temas.md` (no repetir temas).
2. Revisar los borradores y programados del canal en Buffer.
3. Buscar las novedades de IA de la semana y verificar la elegida en la fuente oficial.
4. Escribir los 3 textos (y el carrusel si toca), revisarlos contra las secciones 4 y 5.
5. Si hay carrusel: subir PDF y portada a `linkedin/perfil-nicolas/semana-AAAA-MM-DD/`, commit y push.
6. Crear los 3 borradores en Buffer y confirmar que no haya links automáticos falsos.
7. Anotar la semana en `temas.md` (fecha sugerida, tema, formato, id del borrador, fuente) y hacer push.
8. Mandar el aviso a Nicolás: los 3 borradores con día, tema y la primera línea de cada uno, qué
   tiene que revisar (por ejemplo una opinión que conviene que confirme) y que los programe desde Buffer.
