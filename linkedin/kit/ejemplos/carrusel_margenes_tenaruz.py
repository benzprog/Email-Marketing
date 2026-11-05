"""Ejemplo de carrusel con html_kit: '¿Cuánto ganarías vendiendo Tenaruz?' (nov. 2026).

Uso:  python3 carrusel_margenes_tenaruz.py <carpeta_salida> <lista.json> [dolar_bna_vendedor]
lista.json = {"gu10": [usd_sin_iva, iva, bulto], "mr16": [...], "fuente": [...]}, sacado de la
lista mayorista vigente. NO se sube al repo (es público): los precios mayoristas solo se publican
si Nicolás lo autoriza. Recalcula el mayorista en pesos con el dólar que se le pase.
Los precios al público son un relevamiento del 5/11/2026: actualizarlos si pasa mucho tiempo.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from html_kit import lamina, cabecera, pie, puntos, foto, render, PRODUCTOS

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
import json
LISTA = {k: tuple(v) for k, v in json.load(open(sys.argv[2])).items()}
DOLAR = float(sys.argv[3]) if len(sys.argv) > 3 else 1579  # BNA vendedor 5/11/2026
FECHA_DOLAR = "5/11/2026"
MAY = {k: round(u * DOLAR * (1 + i) / 10) * 10 for k, (u, i, b) in LISTA.items()}
MER = {
    "gu10": dict(nombre="Dicroica LED GU10", detalle="7 W, dimerizable, 220 V", lo=2900, med=4600, hi=5900,
                 foto=(os.path.join(PRODUCTOS, "TZ-GU10-7W.png"), 395, 330, 310)),
    "mr16": dict(nombre="Dicroica LED MR16", detalle="12 V, 5 W", lo=3900, med=4800, hi=6000,
                 foto=(os.path.join(PRODUCTOS, "TZ-MR16-5W_tarjeta.png"), 395, 330, 310)),
    "fuente": dict(nombre="Fuente switching", detalle="24 V, 5 A, 120 W", lo=20300, med=27400, hi=43600,
                   foto=(os.path.join(PRODUCTOS, "TZ-FSLIM24-5A.png"), 590, 380, 140)),
}
TOTAL = 6
PIE = dict(texto="Pana Iluminación · Tenaruz", cta="DESLIZÁ →")

def ars(v): return "$" + f"{v:,.0f}".replace(",", ".")
def usd(u): return f"USD {u:.2f}".replace(".", ",")
def pct(x): return f"{x * 100:.1f}".replace(".", ",").replace(",0", "") + " %"

CSS = """
.label { font-size:30px; font-weight:500; } .label.fuerte { font-weight:600; }
.label.lista { font-size:22px; left:auto; right:80px; text-align:right; }
.label.rango { font-size:24px; font-weight:400; }
.barra { height:60px; } .barra.may { background:#ffce1f; }
.oscuro .barra.pub { background:#fff; color:#131313; } .claro .barra.pub { background:#131313; color:#fff; }
.barra.pub span { position:absolute; right:16px; top:12px; font-size:28px; font-weight:700; }
.valor { font-size:28px; font-weight:700; }
.rangolinea { height:20px; border-left:3px solid var(--suave); border-right:3px solid var(--suave); }
.rangolinea::after { content:""; position:absolute; left:0; right:0; top:8.5px; border-top:3px solid var(--suave); }
.bulto { width:920px; height:86px; border-radius:8px; background:var(--tarjeta); display:flex; align-items:center; justify-content:space-between; padding:0 24px; }
.bulto span { font-size:28px; font-weight:500; color:var(--suave); } .bulto b { font-size:34px; font-weight:800; }
.tabla { width:920px; }
.fila { display:flex; justify-content:space-between; border-top:2px solid var(--linea); padding:22px 0; font-size:32px; font-weight:500; }
.fila b { font-weight:700; }
.fila.th { border-top:none; font-size:24px; font-weight:600; color:var(--suave); padding:0 0 18px; }
.tabla .fila:last-child { border-bottom:2px solid #131313; }
.telefono { font-size:88px; font-weight:800; letter-spacing:-0.025em; }
.notas { width:920px; font-size:21px; line-height:30px; color:var(--suave); } .notas b { color:#fff; font-weight:600; }
"""

def portada():
    return lamina(cabecera(1, TOTAL, True)
        + '<div class="pre y" style="top:330px">Para casas de electricidad y distribuidores</div>'
        + '<h1 class="gigante" style="top:385px">¿Cuánto<br>ganarías<br>vendiendo<br><span class="y">Tenaruz?</span></h1>'
        + puntos(910)
        + '<p class="bajada" style="top:950px">3 productos: precio mayorista contra<br>lo que se paga hoy en el mostrador.</p>'
        + pie(True, **PIE), True)

def producto(i, k):
    p = MER[k]; may = MAY[k]; u, iva, bulto = LISTA[k]
    osc = i % 2 == 1; g = p["med"] - may; sc = 920 / p["hi"]
    ruta, top, ancho, alto = p["foto"]
    return lamina(cabecera(i, TOTAL, osc)
        + f'<div class="pre {"y" if osc else "suave"}" style="top:240px">{p["detalle"]}</div>'
        + f'<h2 style="top:280px">{p["nombre"]}</h2>'
        + '<div class="label suave" style="top:432px">Ganás por unidad</div>'
        + f'<div class="numero {"y" if osc else ""}" style="top:455px">{ars(g)}</div>'
        + f'<div class="label fuerte" style="top:640px">{round(g / p["med"] * 100)} % del precio de venta</div>'
        + foto(ruta, top, ancho=ancho, alto=alto)
        + '<div class="label fuerte" style="top:740px">Precio mayorista Tenaruz (con IVA)</div>'
        + f'<div class="label suave lista" style="top:744px">Lista: {usd(u)} + IVA {pct(iva)}</div>'
        + f'<div class="barra may" style="top:784px;width:{may * sc:.1f}px"></div>'
        + f'<div class="valor" style="top:796px;left:{80 + may * sc + 16:.1f}px">{ars(may)}</div>'
        + '<div class="label fuerte" style="top:890px">Precio al público hoy (valor típico)</div>'
        + f'<div class="barra pub" style="top:934px;width:{p["med"] * sc:.1f}px"><span>{ars(p["med"])}</span></div>'
        + f'<div class="rangolinea" style="top:1000px;left:{80 + p["lo"] * sc:.1f}px;width:{(p["hi"] - p["lo"]) * sc:.1f}px"></div>'
        + f'<div class="label suave rango" style="top:1040px">En comercios online va de {ars(p["lo"])} a {ars(p["hi"])}.</div>'
        + f'<div class="bulto" style="top:1110px"><span>Bulto de {bulto} unidades:</span><b class="{"y" if osc else ""}">ganás {ars(g * bulto)}</b></div>'
        + pie(osc, **PIE), osc)

def condiciones():
    filas = "".join(f'<div class="fila"><span>{n}</span><b>{LISTA[k][2]} u.</b></div>' for n, k in
                    [("Dicroica GU10 7 W dimerizable", "gu10"), ("Dicroica MR16 12 V 5 W", "mr16"),
                     ("Fuente switching 24 V 5 A", "fuente")])
    return lamina(cabecera(5, TOTAL, False)
        + '<div class="pre suave" style="top:240px">Cómo se compra</div>'
        + '<h2 style="top:280px">Por bulto cerrado,<br>con stock disponible.</h2>'
        + puntos(490)
        + f'<div class="tabla" style="top:560px"><div class="fila th"><span>Producto</span><span>Bulto</span></div>{filas}</div>'
        + '<div class="label fuerte" style="top:960px;font-size:34px">¿Necesitás fraccionar? Consultanos.</div>'
        + '<div class="label suave" style="top:1012px;font-size:27px">Más de 80 códigos: lámparas, apliques, spots y fuentes.</div>'
        + pie(False, **PIE), False)

def cierre():
    dol = ars(DOLAR)
    return lamina(cabecera(6, TOTAL, True)
        + '<h1 class="grande" style="top:300px">Pedinos la<br><span class="y">lista mayorista</span><br>completa.</h1>'
        + puntos(705)
        + '<div class="label" style="top:745px;font-size:40px;font-weight:600">Te la mandamos por WhatsApp</div>'
        + '<div class="telefono y" style="top:800px">11 6288-3659</div>'
        + '<div class="label suave" style="top:925px;font-size:32px">o escribinos por mensaje en LinkedIn.</div>'
        + '<div class="notas" style="top:1035px"><b>Precios indicados en USD (se deberá tomar el tipo de cambio oficial vendedor BNA).<br>'
          'Los precios no incluyen IVA.</b><br>'
          f'En pesos: dólar BNA vendedor {dol} ({FECHA_DOLAR}) + IVA, para comparar con el precio al público, '
          'que ya lo incluye. Público: precio típico en comercios online relevado el 5/11/2026. '
          'Ganancia bruta, antes de gastos.</div>'
        + pie(True, texto="Pana Iluminación · Tenaruz", cta="GUARDALO →"), True)

render([portada(), producto(2, "gu10"), producto(3, "mr16"), producto(4, "fuente"), condiciones(), cierre()],
       os.path.join(OUT, "margenes_tenaruz"), css_extra=CSS)
