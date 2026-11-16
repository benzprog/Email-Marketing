"""Kit de carruseles del perfil personal de Nicolás Benítez (IA en el trabajo de oficina).

Láminas de 1080 x 1350 en HTML, impresas a PDF con texto vectorial (Chromium / Playwright).
Estética propia, sin marca de Pana: fondo tinta o crema, un color de acento por tema, letra muy
grande (Inter Display) y "maquetas" de lo que el lector usa todos los días (planilla, mail, chat).

Uso:
    from kit_nicolas import *
    T = TEMAS["excel"]
    laminas = [portada(T, "Título<br>grande", "Bajada", visual_html), paso(T, 2, 7, "ANTETÍTULO", "Título", cuerpo), ..., cierre(T, 7, 7, "Pregunta", "Guardalo")]
    render(laminas, "semana-AAAA-MM-DD/01_tema")   # -> .pdf y _portada.jpg (y PNG de cada lámina si png=True)

Reglas de diseño (ver INSTRUCCIONES.md, sección 5 bis):
- Una idea por lámina. Texto de cuerpo nunca menor a 30 px. Máximo ~35 palabras por lámina.
- Portada: el dolor del lector en letra gigante + una maqueta reconocible. Sin logo.
- Alternar láminas oscuras y claras. El acento solo para lo importante.
- Última lámina: pregunta para comentar + "Guardalo".
"""
import os
from playwright.sync_api import sync_playwright

TINTA = "#0d0d10"
CREMA = "#f5f1e8"

TEMAS = {
    # acento: sobre fondo oscuro · fuerte: sobre fondo claro · etiqueta: texto del rótulo
    "excel": dict(acento="#3ddc84", fuerte="#0f7a3d", etiqueta="PLANILLAS"),
    "mail": dict(acento="#ff6b4a", fuerte="#d23c1b", etiqueta="MAILS"),
    "auto": dict(acento="#a78bfa", fuerte="#6235d9", etiqueta="AUTOMATIZAR"),
    "docs": dict(acento="#ffc83d", fuerte="#a86a00", etiqueta="DOCUMENTOS"),
}

CSS = """
@page { size: 1080px 1350px; margin: 0; }
* { margin:0; padding:0; box-sizing:border-box; }
html, body { width:1080px; }
body { font-family: 'Inter', sans-serif; -webkit-font-smoothing: antialiased; text-rendering: geometricPrecision; }
section { position:relative; width:1080px; height:1350px; overflow:hidden; break-after:page;
          padding:72px 80px 150px; display:flex; flex-direction:column; }
.osc { background:%(TINTA)s; color:#fff; --suave:#a9a8b3; --linea:#2a2a31; --tarjeta:#1a1a20; --ac:var(--acento); }
.cla { background:%(CREMA)s; color:%(TINTA)s; --suave:#5d5a55; --linea:#dcd6c8; --tarjeta:#fff; --ac:var(--fuerte); }
.top { display:flex; justify-content:space-between; align-items:center; }
.rot { font-size:22px; font-weight:700; letter-spacing:.12em; color:var(--ac); display:flex; align-items:center; gap:12px; }
.rot i { width:14px; height:14px; border-radius:50%%; background:var(--ac); }
.num { font-size:22px; font-weight:600; color:var(--suave); font-variant-numeric:tabular-nums; }
.cuerpo { flex:1; display:flex; flex-direction:column; justify-content:center; gap:36px; }
.ante { font-size:26px; font-weight:700; letter-spacing:.1em; color:var(--ac); }
h1 { font-family:'Inter Display','Inter',sans-serif; font-size:116px; line-height:1.02; font-weight:800; letter-spacing:-0.04em; }
h2 { font-family:'Inter Display','Inter',sans-serif; font-size:76px; line-height:1.06; font-weight:800; letter-spacing:-0.035em; }
h2.m { font-size:64px; }
.ac { color:var(--ac); }
.baj { font-size:41px; line-height:1.3; font-weight:500; color:var(--suave); }
.txt { font-size:34px; line-height:1.35; font-weight:500; }
.txt b, .baj b { color:inherit; font-weight:700; }
.osc .baj b { color:#fff; } .cla .baj b { color:%(TINTA)s; }
.tach { text-decoration:line-through; text-decoration-thickness:5px; text-decoration-color:var(--ac); color:var(--suave); }
.pie { position:absolute; left:80px; right:80px; bottom:56px; display:flex; justify-content:space-between; align-items:center;
       border-top:2px solid var(--linea); padding-top:26px; }
.yo { display:flex; align-items:center; gap:16px; font-size:24px; font-weight:600; }
.yo i { width:46px; height:46px; border-radius:50%%; background:var(--ac); color:%(TINTA)s; font-style:normal; font-size:18px; font-weight:800;
        display:flex; align-items:center; justify-content:center; }
.cla .yo i { color:#fff; }
.sig { font-size:24px; font-weight:700; color:var(--ac); }
/* lista numerada */
.lista { display:flex; flex-direction:column; gap:26px; }
.item { display:flex; gap:26px; align-items:flex-start; background:var(--tarjeta); border-radius:22px; padding:30px 32px; }
.cla .item { box-shadow:0 2px 0 var(--linea); }
.item .n { flex:none; width:60px; height:60px; border-radius:50%%; background:var(--ac); color:%(TINTA)s; font-size:30px; font-weight:800;
           display:flex; align-items:center; justify-content:center; }
.cla .item .n { color:#fff; }
.item .t { font-size:38px; line-height:1.25; font-weight:700; }
.item .d { font-size:30px; line-height:1.3; font-weight:500; color:var(--suave); margin-top:6px; }
/* burbuja de chat: el pedido para copiar */
.chat { background:var(--tarjeta); border-radius:28px 28px 28px 6px; padding:42px 44px; font-size:38px; line-height:1.42; font-weight:500;
        border:2px solid var(--linea); }
.cla .chat { box-shadow:0 14px 40px rgba(0,0,0,.08); border:none; }
.chat mark { background:none; color:var(--ac); font-weight:700; }
.copia { align-self:flex-start; font-size:22px; font-weight:700; letter-spacing:.08em; background:var(--ac); color:%(TINTA)s; padding:10px 18px; border-radius:99px; }
.cla .copia { color:#fff; }
/* planilla */
.hoja { background:#fff; color:%(TINTA)s; border-radius:18px; overflow:hidden; border:2px solid #cfd4d1; font-size:31px; font-weight:500;
        display:grid; box-shadow:0 14px 40px rgba(0,0,0,.18); }
.hoja > div { padding:20px 16px; border-right:1px solid #dfe3e1; border-bottom:1px solid #dfe3e1; white-space:nowrap; overflow:hidden; }
.hoja .c { background:#eef1ef; color:#6b716d; font-weight:600; text-align:center; font-size:22px; padding:10px; }
.hoja .h { font-weight:700; background:#f7f9f8; }
.hoja .f { background:color-mix(in srgb, var(--fuerte) 12%%, #fff); color:var(--fuerte); font-weight:700; outline:3px solid var(--fuerte); outline-offset:-3px; }
.mal { color:#c6321c; font-weight:700; } .bien { color:#0f7a3d; font-weight:700; }
.formula { font-family:'DejaVu Sans Mono','Liberation Mono',monospace; font-size:34px; font-weight:700; background:var(--tarjeta); border-radius:16px;
           padding:24px 28px; border-left:8px solid var(--ac); }
.formula small { display:block; font-family:'Inter',sans-serif; font-size:24px; font-weight:600; color:var(--suave); margin-bottom:8px; }
/* ventana (mail, buscador) */
.vent { background:#fff; color:%(TINTA)s; border-radius:22px; overflow:hidden; box-shadow:0 20px 60px rgba(0,0,0,.35); }
.vent .barra { background:#ecebe8; padding:18px 24px; display:flex; gap:10px; align-items:center; font-size:22px; font-weight:600; color:#6d6a66; }
.vent .barra i { width:16px; height:16px; border-radius:50%%; background:#c9c6c0; }
.vent .fila { padding:18px 28px; border-bottom:1px solid #e7e4de; font-size:27px; color:#6d6a66; }
.vent .fila b { color:%(TINTA)s; font-weight:600; }
.vent .txtm { padding:28px; font-size:32px; min-height:150px; }
.cursor { display:inline-block; width:3px; height:38px; background:var(--fuerte); vertical-align:-6px; margin-left:4px; }
.aviso { padding:16px 28px; font-size:23px; font-weight:600; color:var(--fuerte); background:color-mix(in srgb, var(--fuerte) 10%%, #fff); }
.busca { background:#fff; color:#55524e; border-radius:99px; padding:28px 40px; font-size:32px; font-weight:500; display:flex; gap:20px; align-items:center;
         box-shadow:0 20px 60px rgba(0,0,0,.35); }
.busca .lupa { width:30px; height:30px; border:5px solid #8f8c87; border-radius:50%%; position:relative; flex:none; }
.busca .lupa:after { content:''; position:absolute; width:5px; height:16px; background:#8f8c87; right:-9px; bottom:-14px; transform:rotate(-45deg); border-radius:3px; }
/* semanas */
.sem { display:flex; flex-direction:column; gap:16px; }
.sem div { display:flex; justify-content:space-between; align-items:center; background:var(--tarjeta); border-radius:18px; padding:24px 30px; font-size:30px; font-weight:600; color:var(--suave); }
.sem div.ok { background:var(--ac); color:%(TINTA)s; font-weight:800; }
.pill { font-size:22px; font-weight:700; padding:8px 16px; border-radius:99px; border:2px solid var(--linea); }
.ok .pill { border-color:%(TINTA)s; }
.xl { font-family:'Inter Display','Inter',sans-serif; font-size:92px; line-height:1.04; font-weight:800; letter-spacing:-0.04em; }
""" % dict(TINTA=TINTA, CREMA=CREMA)


def _sec(T, contenido, oscuro, pie_html):
    return (f'<section class="{"osc" if oscuro else "cla"}" style="--acento:{T["acento"]};--fuerte:{T["fuerte"]}">'
            f'{contenido}{pie_html}</section>')


def _pie(sig="Deslizá →"):
    return f'<div class="pie"><div class="yo"><i>NB</i>Nicolás Benítez</div><div class="sig">{sig}</div></div>'


def _top(T, i=None, total=None):
    num = f'<div class="num">{i} / {total}</div>' if i else '<div class="num">IA en la oficina</div>'
    return f'<div class="top"><div class="rot"><i></i>{T["etiqueta"]}</div>{num}</div>'


def portada(T, titulo, bajada, visual=""):
    """Lámina 1: el dolor en letra gigante + una maqueta. Siempre oscura."""
    c = (_top(T) + f'<div class="cuerpo" style="gap:44px">{visual}<h1>{titulo}</h1>'
         f'<div class="baj">{bajada}</div></div>')
    return _sec(T, c, True, _pie())


def paso(T, i, total, ante, titulo, cuerpo="", oscuro=False, chico=False, sig="Deslizá →"):
    """Lámina interior: antetítulo + título + un bloque (lista, chat, hoja, texto)."""
    c = (_top(T, i, total) + '<div class="cuerpo">'
         + (f'<div class="ante">{ante}</div>' if ante else "")
         + (f'<h2 class="{"m" if chico else ""}">{titulo}</h2>' if titulo else "") + cuerpo + "</div>")
    return _sec(T, c, oscuro, _pie(sig))


def cierre(T, i, total, pregunta, bajada="Contalo en los comentarios."):
    c = (_top(T, i, total) + f'<div class="cuerpo"><div class="ante">TE LEO</div><div class="xl">{pregunta}</div>'
         f'<div class="baj">{bajada}</div></div>')
    return _sec(T, c, True, _pie("Guardalo ↓"))


def lista(items):
    """items: [(título, detalle)]. Tarjetas numeradas."""
    return '<div class="lista">' + "".join(
        f'<div class="item"><div class="n">{n}</div><div><div class="t">{t}</div>'
        + (f'<div class="d">{d}</div>' if d else "") + "</div></div>"
        for n, (t, d) in enumerate(items, 1)) + "</div>"


def chat(texto, rotulo="COPIÁ ESTE PEDIDO"):
    return f'<div class="copia">{rotulo}</div><div class="chat">{texto}</div>'


def hoja(columnas, filas, anchos, resaltar=()):
    """Maqueta de planilla. columnas: letras; filas: listas de celdas (la primera es el encabezado).
    resaltar: {(fila, col)} con índices desde 0 sobre filas."""
    g = "56px " + " ".join(anchos)
    h = f'<div class="hoja" style="grid-template-columns:{g}"><div class="c"></div>'
    h += "".join(f'<div class="c">{c}</div>' for c in columnas)
    for r, fila in enumerate(filas):
        h += f'<div class="c">{r + 1}</div>'
        for k, celda in enumerate(fila):
            cls = "h" if r == 0 else ("f" if (r, k) in resaltar else "")
            h += f'<div class="{cls}">{celda}</div>'
    return h + "</div>"


def render(laminas, base, png=False):
    """Genera base.pdf (vectorial) y base_portada.jpg. Con png=True, también base_N.png (2160 x 2700)."""
    os.makedirs(os.path.dirname(os.path.abspath(base)), exist_ok=True)
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(laminas)}</body></html>'
    hp = base + ".html"
    open(hp, "w").write(html)
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
        pg.goto("file://" + os.path.abspath(hp))
        pg.wait_for_timeout(400)
        # control: ninguna lámina puede desbordar
        for n, s in enumerate(pg.query_selector_all("section"), 1):
            cu = s.query_selector(".cuerpo")
            if cu and cu.evaluate("e => e.scrollHeight > e.clientHeight + 2"):
                print(f"OJO: la lámina {n} desborda")
        pg.pdf(path=base + ".pdf", width="1080px", height="1350px", print_background=True)
        for n, s in enumerate(pg.query_selector_all("section"), 1):
            if png or n == 1:
                s.screenshot(path=f"{base}_{n}.png")
        b.close()
    from PIL import Image
    Image.open(f"{base}_1.png").convert("RGB").save(base + "_portada.jpg", "JPEG", quality=90, optimize=True)
    if not png:
        os.remove(f"{base}_1.png")
    os.remove(hp)
    print(base + ".pdf", os.path.getsize(base + ".pdf"), "bytes,", len(laminas), "láminas")
    return base + ".pdf"
