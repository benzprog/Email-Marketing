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

## 3. Tema: IA para el trabajo de oficina de todos los días (pedido de Nicolás, 16/11/2026)

**Público:** la mayoría de la gente que usa LinkedIn: gente de oficina que trabaja con Excel o Google
Sheets, Gmail u Outlook, Word, reportes, planillas y mails. El objetivo es que los posts **se guarden y se
compartan** (alcance y viralidad), aportando algo que el lector pueda usar ese mismo día.

**De qué se habla:** cómo integrar IA en el trabajo diario. Automatizar planillas (fórmulas, limpiar y
ordenar datos, tablas dinámicas, macros o Apps Script), redactar y ordenar mails, resumir reuniones y
documentos, armar reportes, pasar de un chat a una tarea que se repite sola, mejorar procesos chicos de una
oficina. **Ejemplos generales de oficina** (facturas, vencimientos, proveedores, reportes de ventas,
reclamos), no del rubro iluminación. Pana aparece solo como prueba real de algo que Nicolás hizo.
(Reemplaza la mezcla del 11/11/2026, que estaba centrada en novedades y en el rubro.)

Mezcla semanal:

1. **Martes · Planillas.** Un problema concreto de Excel o Sheets y cómo resolverlo con IA: el pedido exacto
   para copiar, lo que devuelve (fórmula, pasos) y cómo comprobarlo. Si la semana trae una novedad de IA
   verificada que cambie el trabajo de oficina (una función nueva de Claude, de Excel, de Gmail o de Sheets),
   puede ocupar este día con el mismo enfoque práctico: qué hace, cómo se usa y cuál es el límite.
2. **Miércoles · Lo hice yo (caso real).** Algo que Nicolás hizo de verdad con IA, contado en primera persona,
   con la lección que sirve a cualquier oficina. Material verificable en este repo y en su historial (ver la
   lista de casos en `temas.md`). No inventar números, tiempos ni anécdotas; no dar datos internos de Pana.
3. **Jueves · Plantilla para guardar.** Un pedido (prompt) listo para copiar para una tarea de oficina (un mail
   difícil, resumir un hilo o una reunión, armar un reporte, revisar un contrato o una planilla), por qué
   funciona y cómo revisar lo que devuelve. Cerrar con "Guardalo".

Cada 2 semanas, uno de los tres puede ser un **carrusel PDF** de 5 a 7 láminas (`linkedin/kit/html_kit.py`),
estética neutra, firmado "Nicolás Benítez", sin logo de Pana. Rinde para paso a paso y "5 pedidos para…".

### Para que los posts circulen (sin prometer viralidad)

- El gancho nombra un dolor de oficina que el lector reconoce en segundos ("ese mail que tenés abierto hace dos
  días", "si todavía buscás fórmulas en Google"). Nada de arranques genéricos.
- Algo concreto para copiar en el cuerpo: el pedido entre comillas, la fórmula, los pasos. Es lo que hace que
  se guarde y se comparta.
- Una sola idea por post. Ejemplo realista, con el resultado esperado.
- Cierre con una pregunta que se conteste en una línea y que invite a contar un caso propio ("¿Qué fórmula te
  costó más armar?"), o con "Guardalo".
- Recordarle a Nicolás en el aviso que contestar los comentarios en la primera hora ayuda al alcance.
- No apelar a trucos (cadenas de "comentá SI", promesas de resultados, cifras sin fuente).

### Exactitud de los tutoriales

- Toda fórmula, atajo o función se escribe como funciona de verdad en la versión en español (SI, HOY,
  BUSCARV / BUSCARX, separador ";" en la configuración regional de Argentina) y se aclara el programa.
- Si se nombra una función de un producto (Gemini en Gmail, Copilot en Excel, Claude), confirmar en la página
  oficial que existe, con ese nombre, y en qué planes. Si no se puede confirmar, contarlo sin nombrar la función.
- Siempre una línea de cuidado de datos: no pegar datos de clientes, cuentas ni precios en un chat.

## 4. Exactitud

- **Toda novedad se verifica en la fuente oficial** (anthropic.com/news, docs.claude.com, support.claude.com,
  blogs oficiales de cada empresa) o en medios serios, y se abre la página: un resultado de búsqueda no
  alcanza. Fecha, nombre exacto del producto y qué incluye. Si no se puede confirmar, no se publica.
- No afirmar precios, planes ni disponibilidad en Argentina sin confirmarlo en la fuente.
- El link de la fuente va en el **primer comentario** (`metadata.linkedin.firstComment`), no en el cuerpo.
  En el plan gratis de Buffer el primer comentario está bloqueado (14/11/2026): crear el borrador sin él y
  pasarle el link a Nicolás en el aviso para que lo pegue a mano al publicar.
- Los casos de Pana se cuentan solo con lo que consta en este repo o lo que Nicolás haya dicho.

## 5. Voz y formato

- **Rioplatense, cercano y concreto** (vos, "probá", "fijate"; primera persona en los casos reales). Como
  alguien que trabaja en una pyme y usa IA todos los días, no como un gurú.
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
3. Elegir los 3 temas de la sección 3 (dolores de oficina, sin repetir los de `temas.md`). Mirar si hay una
   novedad de IA para el trabajo de oficina y, si se usa, verificarla en la fuente oficial. Probar o revisar
   cada fórmula y cada paso antes de escribirlo.
4. Escribir los 3 textos (y el carrusel si toca), revisarlos contra las secciones 4 y 5.
5. Si hay carrusel: subir PDF y portada a `linkedin/perfil-nicolas/semana-AAAA-MM-DD/`, commit y push.
6. Crear los 3 borradores en Buffer y confirmar que no haya links automáticos falsos.
7. Anotar la semana en `temas.md` (fecha sugerida, tema, formato, id del borrador, fuente) y hacer push.
8. Mandar el aviso a Nicolás: los 3 borradores con día, tema y la primera línea de cada uno, qué
   tiene que revisar (por ejemplo una opinión que conviene que confirme) y que los programe desde Buffer.
