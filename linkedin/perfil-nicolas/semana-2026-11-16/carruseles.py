"""Carruseles de la semana del 16/11/2026 (perfil de Nicolás). Ejecutar desde esta carpeta:
    python3 carruseles.py [png]
"""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
from kit_nicolas import *

PNG = "png" in sys.argv
OUT = os.environ.get("OUT", AQUI)

# ---------- 1. Excel: pedile la fórmula a la IA ----------
T = TEMAS["excel"]
N = 7
busca = ('<div class="busca"><div class="lupa"></div><span class="tach" style="text-decoration-color:#d23c1b">'
         'fórmula excel si la fecha está vencida</span></div>')
filas = [["Fecha", "Plazo", "Vence", "Estado"],
         ["03/11", "15", "18/11", '<span class="bien">Al día</span>'],
         ["20/10", "20", "09/11", '<span class="mal">Vencida</span>'],
         ["01/11", "30", "01/12", '<span class="bien">Al día</span>']]
excel = [
    portada(T, 'Dejá de buscar fórmulas de Excel en <span class="ac">Google.</span>',
            "Pedíselas a la IA. Te muestro cómo, con un ejemplo para copiar.", busca),
    paso(T, 2, N, "TE SUENA", 'Veinte pestañas abiertas y la fórmula <span class="ac">sigue dando error.</span>',
         '<div class="baj">No hace falta saber fórmulas de memoria. Hace falta <b>saber pedirlas.</b></div>'),
    paso(T, 3, N, "EL EJEMPLO", "Una planilla de facturas", hoja("ABCD", [filas[0], ["03/11", "15", "", ""], ["20/10", "20", "", ""], ["01/11", "30", "", ""]],
         ["1fr", "1fr", "1fr", "1.2fr"], {(1, 2), (1, 3)})
         + '<div class="baj">Querés que la <b>C</b> calcule el vencimiento y la <b>D</b> avise si está vencida.</div>', oscuro=True, chico=True),
    paso(T, 4, N, "", "", chat('Tengo una planilla de <mark>Excel en español</mark>. En la <mark>columna A</mark> está la fecha de la factura y en la '
         '<mark>B</mark> los días de plazo. Quiero en la C la fecha de vencimiento y en la D que diga “Vencida” o “Al día” según la fecha de hoy. '
         'Dame las fórmulas para la fila 2 y <mark>explicame qué hace cada una.</mark>', "PEGÁ ESTO EN CLAUDE O CHATGPT")
         + '<div class="baj">Las dos tienen versión gratis: <b>claude.ai</b> y <b>chatgpt.com</b></div>'),
    paso(T, 5, N, "LO QUE TE DEVUELVE", "Dos fórmulas: copialas y pegalas en tu planilla",
         '<div class="formula"><small>En C2</small>=A2+B2</div>'
         '<div class="formula"><small>En D2</small>=SI(C2&lt;HOY();"Vencida";"Al día")</div>'
         + hoja("ABCD", filas, ["1fr", "1fr", "1fr", "1.2fr"]), oscuro=True, chico=True),
    paso(T, 6, N, "PARA QUE SALGA BIEN", "3 claves del pedido", lista([
        ("Decí el programa y el idioma", "Excel en español usa SI y HOY, no IF y TODAY."),
        ("Nombrá cada columna por su letra", "Y contale qué hay en cada una."),
        ("Probala antes de copiarla", "Tres filas en las que ya sepas el resultado."),
    ]), chico=True),
    cierre(T, 7, N, '¿Qué fórmula te costó más <span class="ac">armar?</span>', "Contala en los comentarios y la resolvemos."),
]
render(excel, f"{OUT}/01_formulas_excel_con_ia", png=PNG)

# ---------- 2. Recordatorio automático a clientes con pago atrasado ----------
T = TEMAS["auto"]
N = 7
IA = "PEGÁ ESTO EN CLAUDE O CHATGPT"
sem = ('<div class="sem"><div>Recordatorio a cliente 1 <span class="pill">a mano</span></div>'
       '<div>Recordatorio a cliente 2 <span class="pill">a mano</span></div>'
       '<div class="ok">Todos los demás <span class="pill">salen solos</span></div></div>')
auto = [
    portada(T, '¿Seguís reclamando pagos <span class="ac">mail por mail?</span>',
            "Que el recordatorio salga solo, en 5 pasos. No hace falta saber programar.", sem),
    paso(T, 2, N, "PASO 1", "Armá esta planilla en Google Sheets",
         hoja("ABCD", [["Cliente", "Mail", "Vence", "Pagó"], ["Cliente 1", "mail 1", "05/11", '<span class="mal">No</span>'],
                       ["Cliente 2", "mail 2", "10/11", '<span class="bien">Sí</span>'], ["Cliente 3", "mail 3", "12/11", '<span class="mal">No</span>']],
              ["1.3fr", "1.1fr", "1fr", "0.8fr"])
         + '<div class="baj">Los títulos en la fila 1. Un cliente por fila.</div>', chico=True),
    paso(T, 3, N, "PASO 2", "Pedile el código a la IA",
         chat('Tengo una planilla de Google. Columna A: cliente. B: mail. C: fecha de vencimiento. D: “Sí” si pagó. '
              'Haceme el <mark>código de Apps Script</mark> que mande un mail de recordatorio a los vencidos que no pagaron. '
              '<mark>Explicame dónde pegarlo, paso a paso.</mark>', IA)
         + '<div class="baj">Las dos tienen versión gratis: <b>claude.ai</b> y <b>chatgpt.com</b></div>', oscuro=True, chico=True),
    paso(T, 4, N, "PASO 3", "Pegá el código en tu planilla",
         '<div class="baj">La IA te devuelve un bloque de código. <b>Copialo entero.</b> Después, en la planilla:</div>'
         + ruta("Extensiones", "Apps Script")
         + '<div class="baj">Se abre una pestaña. <b>Borrá lo que hay, pegá el código y tocá Guardar.</b></div>', chico=True),
    paso(T, 5, N, "PASO 4", "Probalo con vos",
         lista([("En la fila 2 poné tu propio mail", "Con una fecha de ayer y “No” en Pagó."),
                ("Tocá el botón Ejecutar", "La primera vez Google te pide permiso: aceptá."),
                ("Fijate si te llegó el mail", "Si no llega, contale a la IA qué pasó.")]), oscuro=True, chico=True),
    paso(T, 6, N, "PASO 5", "Que salga solo todos los días",
         '<div class="baj">En esa misma pestaña, a la izquierda:</div>'
         + ruta("Ícono del reloj", "Añadir activador")
         + '<div class="baj">Elegí que se ejecute <b>una vez por día</b>, a la mañana, y guardá.</div>'
         '<div class="baj">Listo. Cuando alguien paga, escribí <b>“Sí”</b> y deja de recibirlo.</div>', chico=True),
    cierre(T, 7, N, '¿Qué tarea repetís <span class="ac">todas las semanas?</span>', "Contala y vemos cómo hacer que salga sola."),
]
render(auto, f"{OUT}/02_recordatorio_de_pagos_automatico", png=PNG)

# ---------- 3. El mail que no sabés cómo contestar ----------
T = TEMAS["mail"]
N = 7
vent = ('<div class="vent"><div class="barra"><i></i><i></i><i></i>&nbsp; Mensaje nuevo</div>'
        '<div class="fila">Para: <b>proveedor</b></div><div class="fila">Asunto: <b>Re: Re: Re: Entrega atrasada</b></div>'
        '<div class="txtm">Estimado,<span class="cursor"></span></div><div class="aviso">Borrador guardado hace 2 días</div></div>')
mail = [
    portada(T, 'Ese mail que no sabés cómo <span class="ac">contestar.</span>',
            "Un pedido a la IA para destrabarlo. Copialo y adaptalo.", vent),
    paso(T, 2, N, "EL ERROR DE SIEMPRE", '<span class="tach">“Respondé este mail”</span>',
         '<div class="baj">Con ese pedido la IA te devuelve algo <b>largo, genérico y que no mandarías.</b></div>'
         '<div class="baj">No sabe qué querés lograr ni qué no puede decir.</div>'),
    paso(T, 3, N, "", "", chat('Te pego un <mark>hilo de mails</mark> con un proveedor que se atrasó con una entrega. Quiero responderle para '
         '<mark>conseguir una fecha concreta sin romper la relación.</mark> Tono cordial y firme. <mark>Máximo 6 líneas.</mark> '
         'No prometas nada de nuestro lado. <mark>Si falta información, preguntame antes de escribir.</mark>', "PEGÁ ESTO EN CLAUDE O CHATGPT")
         + '<div class="baj">Debajo del pedido, <b>pegá el hilo de mails</b> copiado de tu correo.</div>', oscuro=True),
    paso(T, 4, N, "POR QUÉ FUNCIONA", "Tiene 4 partes", lista([
        ("El contexto completo", "El hilo entero, no un resumen tuyo."),
        ("Lo que querés lograr", "No solo “respondé”."),
        ("Los límites", "Largo, tono y lo que no puede prometer."),
        ("Permiso para preguntar", "Así no rellena con datos inventados."),
    ]), chico=True),
    paso(T, 5, N, "ANTES DE MANDARLO", "3 chequeos de un minuto", lista([
        ("Fechas, números y nombres", "Comparalos con el hilo original."),
        ("Sacá lo que no dirías vos", "Si suena a robot: “más corto y más directo”."),
        ("Leelo como el que lo recibe", ""),
    ]), oscuro=True, chico=True),
    paso(T, 6, N, "UN CUIDADO", 'Antes de pegar el hilo, <span class="ac">borrá los datos sensibles.</span>',
         '<div class="baj">Cuentas, precios y datos personales no hacen falta para redactar una respuesta.</div>', chico=True),
    cierre(T, 7, N, '¿Qué tipo de mail te cuesta más <span class="ac">escribir?</span>', "Contalo en los comentarios y lo armamos."),
]
render(mail, f"{OUT}/03_mail_dificil_con_ia", png=PNG)
