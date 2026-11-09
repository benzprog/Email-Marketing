"""Piezas de la semana del 9/11/2026 (html_kit, texto vectorial).

Uso: python3 piezas_semana_2026_11_09.py <carpeta_salida> <foto_obra.jpg>
Genera:
  01_termica_arranque  (carrusel 7 láminas)
  02_ugr_deslumbramiento (carrusel 7 láminas)
  03_apliques_tenaruz  (carrusel 7 láminas, producto)
  04_obra_hall          (una imagen, foto de obra de un cliente)
  05_codigo_ik          (una imagen)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from html_kit import lamina, cabecera, pie, puntos, render, PRODUCTOS, FOTOS, AMARILLO

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
FOTO_OBRA = sys.argv[2] if len(sys.argv) > 2 else ""

CSS = """
.sangre { left:0; top:0; width:1080px; height:1350px; background-size:cover; background-position:center; }
.velo { left:0; top:0; width:1080px; height:1350px; }
.barra { height:56px; border-radius:4px; }
.lbl { font-size:28px; font-weight:600; }
.lbl.s { font-weight:500; color:var(--suave); }
.lista { width:920px; font-size:34px; line-height:46px; font-weight:500; }
.lista p { margin-bottom:30px; padding-left:34px; position:relative; }
.lista p::before { content:""; position:absolute; left:0; top:17px; width:12px; height:12px; border-radius:50%; background:#ffce1f; }
.claro .lista p::before { background:#131313; }
.fila { width:920px; display:flex; align-items:baseline; border-top:2px solid var(--linea); padding:32px 0; }
.fila b { width:190px; font-size:56px; font-weight:800; letter-spacing:-0.02em; }
.fila span { font-size:31px; line-height:40px; font-weight:500; }
.chip { display:inline-block; width:58px; height:58px; border-radius:50%; margin:0 14px 14px 0; }
.pilla { font-size:26px; font-weight:600; padding:10px 18px; border-radius:6px; background:#ffce1f; color:#131313; }
.telefono { font-size:88px; font-weight:800; letter-spacing:-0.025em; }
.caja { border:3px solid currentColor; border-radius:6px; }
.cota { font-size:24px; font-weight:600; color:var(--suave); }
"""

def ppie(osc, cta="DESLIZÁ →", texto="Pana Iluminación"):
    return pie(osc, texto=texto, cta=cta)

def barra(top, ancho, color, left=80, alto=56):
    return f'<div class="barra" style="top:{top}px;left:{left}px;width:{ancho:.1f}px;height:{alto}px;background:{color}"></div>'

# ---------------------------------------------------------------- 1. Térmica y arranque
def termica():
    T = 7
    s = []
    s.append(lamina(cabecera(1, T, True)
        + '<div class="pre y" style="top:300px">Para instaladores y electricistas</div>'
        + '<h1 class="gigante" style="top:355px">Prendés<br>las luces<br>y salta la<br><span class="y">térmica.</span></h1>'
        + puntos(905)
        + '<p class="bajada" style="top:945px">No es un cortocircuito. Es la corriente<br>de arranque de las fuentes LED.</p>'
        + ppie(True), True))
    sc = 920 / 80
    s.append(lamina(cabecera(2, T)
        + '<div class="pre suave" style="top:240px">Al encender, cada fuente carga sus capacitores de golpe</div>'
        + '<div class="numero" style="top:300px">78 A</div>'
        + '<div class="lbl" style="top:480px;font-size:36px">durante 195 microsegundos</div>'
        + '<div class="lbl s" style="top:600px">En marcha consume 0,7 A</div>'
        + barra(645, 0.7 * sc, "#131313")
        + '<div class="lbl s" style="top:740px">En el arranque llega a 78 A</div>'
        + barra(785, 78 * sc, AMARILLO)
        + '<div class="cota" style="top:860px">Barras a escala. Ejemplo publicado por ABB: driver de 150 W.</div>'
        + '<p class="texto" style="top:960px">Más de cien veces la corriente normal, durante menos de un milisegundo.</p>'
        + ppie(False), False))
    s.append(lamina(cabecera(3, T, True)
        + '<div class="pre y" style="top:240px">Y los picos se suman</div>'
        + '<h2 style="top:290px">12 fuentes que<br>arrancan juntas:</h2>'
        + '<div class="numero y" style="top:470px">936 A</div>'
        + '<div class="lbl" style="top:650px;font-size:34px">12 × 78 A, en el mismo instante</div>'
        + '<div style="top:740px;width:920px">' + "".join('<i class="chip" style="background:#ffce1f"></i>' for _ in range(12)) + '</div>'
        + '<p class="texto suave" style="top:900px">Es una cuenta gruesa: el cable y la impedancia de la red bajan algo el pico real. Pero el orden de magnitud es ese.</p>'
        + ppie(True), True))
    sc = 920 / 170
    s.append(lamina(cabecera(4, T)
        + '<div class="pre suave" style="top:240px">La térmica tiene un disparo magnético</div>'
        + '<h2 style="top:290px">Curva B o C:<br>cambia cuánto aguanta.</h2>'
        + '<div class="lbl" style="top:520px">Curva B · entre 3 y 5 veces la nominal</div>'
        + barra(565, 48 * sc, "#d6d3cf") + barra(565, 32 * sc, "#131313", left=80 + 48 * sc)
        + '<div class="lbl s" style="top:635px">En una de 16 A: entre 48 y 80 A</div>'
        + '<div class="lbl" style="top:730px">Curva C · entre 5 y 10 veces la nominal</div>'
        + barra(775, 80 * sc, "#d6d3cf") + barra(775, 80 * sc, AMARILLO, left=80 + 80 * sc)
        + '<div class="lbl s" style="top:845px">En una de 16 A: entre 80 y 160 A</div>'
        + '<div class="cota" style="top:920px">Barras a escala, de 0 a 170 A. La parte oscura o amarilla es la franja de disparo.</div>'
        + '<p class="texto" style="top:1010px">Ante picos de microsegundos aguanta más que esos valores. Cuánto más, lo dice el fabricante: por eso hay tablas.</p>'
        + ppie(False), False))
    s.append(lamina(cabecera(5, T, True)
        + '<div class="pre y" style="top:240px">Dos ensayos publicados</div>'
        + '<div class="fila" style="top:320px;border-top:none"><b class="y">11</b><span style="width:730px">fuentes de 150 W en una térmica C de 16 A: no salta. Con 12, salta. <span class="suave">(ABB)</span></span></div>'
        + '<div class="fila" style="top:560px"><b class="y">30</b><span style="width:730px">fuentes HLP-80H en una térmica C de 16 A: no salta. Con 36, salta. <span class="suave">(Mean Well)</span></span></div>'
        + puntos(860)
        + '<p class="texto" style="top:900px;font-size:34px;line-height:46px">El límite real lo pone el arranque,<br>no la potencia en marcha.</p>'
        + ppie(True), True))
    s.append(lamina(cabecera(6, T)
        + '<div class="pre suave" style="top:240px">Qué hacer en obra</div>'
        + '<h2 style="top:290px">Antes de cablear:</h2>'
        + '<div class="lista" style="top:430px">'
          '<p>Buscá en la ficha de la fuente el pico de arranque y su duración ("inrush current").</p>'
          '<p>Usá la tabla de fuentes por térmica del fabricante. No vale entre marcas distintas.</p>'
          '<p>Repartí en más circuitos o encendé por grupos.</p>'
          '<p>Si hace falta, sumá un limitador de corriente de arranque.</p></div>'
        + '<div class="pilla" style="top:1130px">No subas el calibre de la térmica: protege al cable.</div>'
        + ppie(False), False))
    s.append(lamina(cabecera(7, T, True)
        + '<h1 class="grande" style="top:330px">La térmica<br>no está fallada.<br><span class="y">El circuito<br>está mal armado.</span></h1>'
        + puntos(850)
        + '<div class="lbl" style="top:900px;font-size:40px">Guardalo para la próxima obra.</div>'
        + '<div class="lbl s" style="top:960px;font-size:30px">Fuentes, cálculos y cotizaciones: consultanos.</div>'
        + pie(True), True))
    render(s, os.path.join(OUT, "01_termica_arranque"), css_extra=CSS)

# ---------------------------------------------------------------- 2. UGR
def ugr():
    T = 7
    s = []
    s.append(lamina(cabecera(1, T, True)
        + '<div class="pre y" style="top:300px">Oficinas, aulas y consultorios</div>'
        + '<h1 class="gigante" style="top:355px">Hay luz<br>de sobra y<br>aun así<br><span class="y">molesta.</span></h1>'
        + puntos(905)
        + '<p class="bajada" style="top:945px">Se llama deslumbramiento molesto<br>y tiene número: el UGR.</p>'
        + ppie(True), True))
    s.append(lamina(cabecera(2, T)
        + '<div class="pre suave" style="top:240px">Lo primero que hay que saber</div>'
        + '<h2 style="top:290px">El deslumbramiento<br>es de la instalación,<br>no del artefacto.</h2>'
        + puntos(600)
        + '<p class="texto" style="top:660px">Depende de cuántas luminarias hay, dónde están, qué tan brillantes se ven y desde dónde mira la persona.</p>'
        + '<p class="texto suave" style="top:860px">La misma luminaria puede cumplir en una sala y no cumplir en otra.</p>'
        + ppie(False), False))
    vals = [16, 19, 22, 25, 28]
    escala = "".join(
        f'<div style="top:{900 - (140 + i * 70)}px;left:{80 + i * 184}px;width:172px;height:{140 + i * 70}px;'
        f'background:{AMARILLO if v == 19 else "#3a3a3a"};border-radius:4px"></div>'
        f'<div style="top:910px;left:{80 + i * 184}px;font-size:56px;font-weight:800;'
        f'color:{AMARILLO if v == 19 else "#fff"}">{v}</div>' for i, v in enumerate(vals))
    s.append(lamina(cabecera(3, T, True)
        + '<div class="pre y" style="top:240px">La escala</div>'
        + '<h2 style="top:290px">Cinco escalones.<br>Más alto, más molesta.</h2>'
        + escala
        + '<p class="texto suave" style="top:1030px">Cada escalón es un cambio que se nota a simple vista. Los valores son máximos: hay que quedar por debajo.</p>'
        + ppie(True), True))
    filas = [("16", "Dibujo técnico, trabajo de precisión"),
             ("19", "Lectura, escritura, computadora, aulas"),
             ("22", "Recepción, talleres e industria"),
             ("25", "Depósitos, salas de máquinas, escaleras"),
             ("28", "Pasillos y circulaciones")]
    s.append(lamina(cabecera(4, T)
        + '<div class="pre suave" style="top:240px">Máximo recomendado por tarea</div>'
        + '<div style="top:300px">' + "".join(
            f'<div class="fila"><b>{n}</b><span>{t}</span></div>' for n, t in filas) + '</div>'
        + '<div class="cota" style="top:1150px">Referencia europea: norma EN 12464-1 (resumen de ZVEI, 2021).</div>'
        + ppie(False), False))
    s.append(lamina(cabecera(5, T, True)
        + '<div class="pre y" style="top:240px">Ojo con la ficha</div>'
        + '<h2 style="top:290px">"UGR &lt; 19" vale<br>para una sala<br>de referencia.</h2>'
        + '<div class="caja" style="top:640px;width:560px;height:280px;color:#ffce1f"></div>'
        + '<div class="cota" style="top:600px">8H</div>'
        + '<div class="cota" style="top:765px;left:660px">4H</div>'
        + '<p class="texto" style="top:960px">Planta de 4H por 8H (H: altura de la luminaria sobre los ojos), techo 70 %, paredes 50 %, piso 20 %.</p>'
        + '<p class="chico" style="top:1100px">Tu local tiene otra forma y otros colores: el número real puede cambiar.</p>'
        + ppie(True), True))
    s.append(lamina(cabecera(6, T)
        + '<div class="pre suave" style="top:240px">Qué pedir</div>'
        + '<h2 style="top:290px">Para cumplir<br>de verdad:</h2>'
        + '<div class="lista" style="top:500px">'
          '<p>La tabla UGR completa del fabricante, no solo un número.</p>'
          '<p>Un cálculo con el plano real (DIALux o Relux): el observador va sentado, con los ojos a 1,2 m.</p>'
          '<p>Revisar la posición de los puestos respecto de las luminarias.</p></div>'
        + ppie(False), False))
    s.append(lamina(cabecera(7, T, True)
        + '<h1 class="grande" style="top:330px">Más lúmenes<br>no arreglan<br><span class="y">una luz que<br>encandila.</span></h1>'
        + puntos(850)
        + '<div class="lbl" style="top:900px;font-size:40px">Guardalo para la próxima obra.</div>'
        + '<div class="lbl s" style="top:960px;font-size:30px">Proyectos de oficinas y comercios: consultanos.</div>'
        + pie(True), True))
    render(s, os.path.join(OUT, "02_ugr_deslumbramiento"), css_extra=CSS)

# ---------------------------------------------------------------- 3. Apliques Tenaruz
def apliques():
    T = 7
    s = []
    fachada = os.path.join(FOTOS, "fachada_aplique_curvo.jpg")
    pared = os.path.join(PRODUCTOS, "TZ-K2CURVN-2GU10_pared.jpg")
    velo = ("linear-gradient(180deg, rgba(10,10,10,.55) 0%, rgba(10,10,10,0) 22%, "
            "rgba(10,10,10,0) 40%, rgba(10,10,10,.92) 62%, rgba(10,10,10,.97) 100%)")
    s.append(lamina(
        f'<div class="sangre" style="background-image:url(\'file://{fachada}\');background-position:62% 20%;height:900px"></div>'
        f'<div class="velo" style="background:{velo}"></div>'
        + cabecera(1, T, True)
        + '<div class="pre y" style="top:760px">Apliques de exterior Tenaruz</div>'
        + '<h1 class="grande" style="top:810px">En una fachada<br>falla lo que <span class="y">no<br>se ve en la foto.</span></h1>'
        + ppie(True), True))
    s.append(lamina(cabecera(2, T)
        + '<div class="pre suave" style="top:240px">El problema en obra</div>'
        + '<h2 style="top:290px">Agua, sol y<br>una conexión mal<br>hecha.</h2>'
        + puntos(590)
        + '<p class="texto" style="top:650px">Un aplique de fachada pasa años a la intemperie. Lo que importa está en la ficha: protección, material, potencia máxima y cómo se conecta.</p>'
        + '<p class="texto suave" style="top:880px">Te mostramos los cuatro datos que miramos en los apliques curvo y recto de Tenaruz.</p>'
        + ppie(False), False))
    s.append(lamina(
        f'<div class="sangre" style="background-image:url(\'file://{pared}\');background-position:30% 50%;height:760px;top:0"></div>'
        + '<div class="velo" style="background:linear-gradient(180deg, rgba(10,10,10,.5) 0%, rgba(10,10,10,0) 20%)"></div>'
        + cabecera(3, T, True)
        + '<div class="pre y" style="top:810px">Dato 1 · IP65 y aluminio negro</div>'
        + '<h2 style="top:860px">Cerrado al polvo<br>y a los chorros de agua.</h2>'
        + '<p class="texto suave" style="top:1060px">Cuerpo de aluminio. IP65 es para fachada, no para sumergir.</p>'
        + ppie(True), True))
    s.append(lamina(cabecera(4, T)
        + '<div class="pre suave" style="top:240px">Dato 2 · Clase I</div>'
        + '<div class="numero" style="top:290px">Clase I</div>'
        + '<h2 style="top:480px">Lleva cable<br>a tierra.</h2>'
        + puntos(690)
        + '<p class="texto" style="top:740px">Clase I quiere decir que la protección contra descargas depende de conectar el cuerpo metálico al borne de tierra.</p>'
        + '<p class="texto" style="top:930px"><b>Error común:</b> colgarlo en una pared exterior con dos cables nada más.</p>'
        + ppie(False), False))
    sc = 740 / 50
    s.append(lamina(cabecera(5, T, True)
        + '<div class="pre y" style="top:240px">Dato 3 · Potencia máxima</div>'
        + '<div class="numero y" style="top:290px">7 W</div>'
        + '<h2 style="top:470px">por lámpara GU10.</h2>'
        + '<div class="lbl" style="top:640px">Dicroica LED GU10 de 7 W</div>'
        + barra(685, 7 * sc, AMARILLO)
        + '<div class="lbl" style="top:780px">Dicroica halógena de 50 W</div>'
        + barra(825, 50 * sc, "#ffffff")
        + '<div class="lbl" style="top:840px;left:850px;color:#ffce1f">No va</div>'
        + '<div class="cota" style="top:910px">Barras a escala.</div>'
        + '<p class="texto" style="top:990px">Se venden solos o con lámparas, como prefiera el cliente. Va una dicroica LED GU10 de hasta 7 W.</p>'
        + ppie(True), True))
    # medidas a escala: 1 mm = 3,4 px
    k = 3.4
    s.append(lamina(cabecera(6, T)
        + '<div class="pre suave" style="top:240px">Dato 4 · Medidas y modelos</div>'
        + '<h2 style="top:290px">Una o dos luces,<br>misma sección.</h2>'
        + f'<div class="caja" style="top:{1000 - 80 * k:.0f}px;left:110px;width:220px;height:{80 * k:.0f}px;background:#131313;border-color:#131313"></div>'
        + f'<div class="caja" style="top:{1000 - 150 * k:.0f}px;left:500px;width:220px;height:{150 * k:.0f}px;background:#131313;border-color:#131313"></div>'
        + '<div class="lbl" style="top:1020px;left:110px">Una luz</div>'
        + '<div class="lbl s" style="top:1060px;left:110px;font-size:24px">80 × 67 × 92 mm</div>'
        + '<div class="lbl" style="top:1020px;left:500px">Dos luces (arriba y abajo)</div>'
        + '<div class="lbl s" style="top:1060px;left:500px;font-size:24px">150 × 67 × 92 mm</div>'
        + '<div class="cota" style="top:1110px">Alto a escala. Curvo o recto · 100–240 V · bulto de 24 (una luz) y de 20 (dos luces).</div>'
        + ppie(False), False))
    s.append(lamina(cabecera(7, T, True)
        + '<h1 class="grande" style="top:300px">Pedinos<br>la lista de<br><span class="y">apliques.</span></h1>'
        + puntos(650)
        + '<div class="lbl" style="top:700px;font-size:38px">Escribinos por WhatsApp con la palabra</div>'
        + '<div class="telefono" style="top:760px">LINKEDIN</div>'
        + '<div class="telefono y" style="top:870px">11 6288-3659</div>'
        + '<div class="lbl s" style="top:1010px;font-size:28px">Venta a comercios e instaladores, por bulto cerrado.</div>'
        + pie(True, texto="Pana Iluminación · Tenaruz", cta="GUARDALO →"), True))
    render(s, os.path.join(OUT, "03_apliques_tenaruz"), css_extra=CSS)

# ---------------------------------------------------------------- 4. Obra: hall
def obra():
    velo = ("linear-gradient(180deg, rgba(10,10,10,.55) 0%, rgba(10,10,10,0) 16%, rgba(10,10,10,0) 100%)")
    s = [lamina(
        f'<div class="sangre" style="background-image:url(\'file://{FOTO_OBRA}\');height:820px;background-position:38% 50%"></div>'
        f'<div class="velo" style="height:820px;background:{velo}"></div>'
        + cabecera(None, None, True)
        + '<div class="pre y" style="top:880px">Obra de un cliente de Pana</div>'
        + '<h1 class="grande" style="top:930px;font-size:80px;line-height:90px">Se ve la luz,<br>casi no se ven las luces.</h1>'
        + puntos(1150)
        + pie(True), True)]
    render(s, os.path.join(OUT, "04_obra_hall"), css_extra=CSS)

# ---------------------------------------------------------------- 5. Código IK
def ik():
    datos = [("IK06", 1, ""), ("IK07", 2, "0,5 kg desde 40 cm"), ("IK08", 5, "1,7 kg desde 30 cm"),
             ("IK09", 10, "5 kg desde 20 cm"), ("IK10", 20, "5 kg desde 40 cm")]
    sc = 700 / 20
    filas = ""
    for i, (c, j, eq) in enumerate(datos):
        top = 600 + i * 104
        filas += (f'<div class="lbl" style="top:{top + 10}px;font-size:34px;font-weight:800">{c}</div>'
                  + barra(top, j * sc, AMARILLO if c == "IK10" else "#131313", left=220, alto=50)
                  + f'<div class="lbl" style="top:{top + 8}px;left:{220 + j * sc + 16:.0f}px">{str(j)} J</div>'
                  + (f'<div class="lbl s" style="top:{top + 62}px;left:220px;font-size:22px">{eq}</div>' if eq else ""))
    s = [lamina(cabecera(None, None, False)
        + '<div class="pre suave" style="top:240px">Código IK · norma IEC 62262</div>'
        + '<h2 style="top:290px">IP65 no dice nada<br>de un golpe.</h2>'
        + '<p class="texto" style="top:500px;font-size:28px">El IK mide la resistencia a los golpes, en joules:</p>'
        + filas
        + '<div class="cota" style="top:1125px">Barras a escala. Equivalencias del ensayo de caída. En 2021 se sumó el IK11 (50 J).</div>'
        + '<div class="pilla" style="top:1166px;font-size:22px">IP e IK son ensayos distintos: pedí los dos.</div>'
        + pie(False), False)]
    render(s, os.path.join(OUT, "05_codigo_ik"), css_extra=CSS)

if __name__ == "__main__":
    que = sys.argv[3:] or ["termica", "ugr", "apliques", "obra", "ik"]
    for q in que:
        globals()[q]()
