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
         'Dame las fórmulas para la fila 2 y <mark>explicame qué hace cada una.</mark>')),
    paso(T, 5, N, "LO QUE TE DEVUELVE", "Dos fórmulas listas para pegar",
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

# ---------- 2. De un chat a una tarea que se repite sola ----------
T = TEMAS["auto"]
N = 7
sem = ('<div class="sem"><div>Semana 1 <span class="pill">a mano</span></div><div>Semana 2 <span class="pill">a mano</span></div>'
       '<div class="ok">Semana 3 <span class="pill">se hizo sola</span></div></div>')
auto = [
    portada(T, 'Esa tarea de todas las semanas puede <span class="ac">hacerse sola.</span>',
            "Así pasé un trabajo de un chat con IA a una tarea programada.", sem),
    paso(T, 2, N, "LA DIFERENCIA", 'Un chat te ahorra minutos.<br><span class="ac">Una tarea programada te saca de encima lo repetido.</span>',
         '<div class="baj">La IA puede hacer el mismo trabajo cada semana, sin que se lo pidas de nuevo.</div>', chico=True),
    paso(T, 3, N, "MI CASO", "La página de LinkedIn de mi empresa", lista([
        ("Lee las reglas que escribí", "Tono, temas que no van, palabras que no se usan."),
        ("Busca temas y verifica los datos", ""),
        ("Diseña las piezas y las deja programadas", ""),
        ("Mide cómo les fue a las anteriores", ""),
    ]) + '<div class="baj">Todos los sábados, sola.</div>', oscuro=True, chico=True),
    paso(T, 4, N, "NO SALIÓ BIEN DE ENTRADA", "3 cosas que tuve que corregir", lista([
        ("Imágenes con el texto borroso", "Hubo que rehacerlas de otra forma."),
        ("Un dato comercial que no era cierto", "Lo corregí y quedó como regla escrita."),
        ("Frases lindas que nadie dice", "Ahora hay una lista de palabras prohibidas."),
    ]), chico=True),
    paso(T, 5, N, "LA RECETA", "Sirve para cualquier tarea de oficina", lista([
        ("Escribí las reglas una sola vez", "En un documento, no en cada chat."),
        ("Cada error que corregís va a ese documento", "Así no se repite la semana siguiente."),
        ("Revisá antes de que salga con tu nombre", "La IA hace el trabajo. El criterio es tuyo."),
    ]), oscuro=True, chico=True),
    paso(T, 6, N, "POR DÓNDE EMPEZAR", "Tareas que se prestan", lista([
        ("El reporte de todos los lunes", ""),
        ("El resumen semanal de ventas", ""),
        ("El control de pagos y vencimientos", ""),
        ("El resumen de los mails pendientes", ""),
    ]), chico=True),
    cierre(T, 7, N, '¿Qué tarea de todas las semanas te gustaría que se hiciera <span class="ac">sola?</span>'),
]
render(auto, f"{OUT}/02_de_un_chat_a_una_tarea", png=PNG)

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
         'No prometas nada de nuestro lado. <mark>Si falta información, preguntame antes de escribir.</mark>'), oscuro=True),
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
