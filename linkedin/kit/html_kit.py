"""Kit HTML de Pana: láminas 1080 x 1350 con texto vectorial (máxima nitidez).

Reemplaza a pana_style.py para las piezas nuevas. Cada lámina es un <section> de HTML;
Chromium (Playwright) las imprime a un PDF con el texto como texto (no como imagen), así se
ve nítido a cualquier zoom, y saca además un PNG por lámina al doble de resolución.

Uso básico:

    from html_kit import lamina, cabecera, pie, puntos, foto, render
    s1 = lamina(cabecera(1, 6, oscuro=True) + '<h1 class="gigante" style="top:385px">Hola</h1>'
                + pie(oscuro=True), oscuro=True)
    render([s1, s2, ...], "semana-AAAA-MM-DD/01_tema")
    # -> 01_tema.pdf (carrusel), 01_tema_1.png ... (2160 x 2700), 01_tema_portada.jpg

- Carrusel: subir el PDF y usar la portada JPG como miniatura en Buffer.
- Post de una imagen: usar el PNG de la lámina (2160 x 2700, mismo formato 4:5).
- Todo va posicionado en absoluto dentro de 1080 x 1350 (margen lateral 80 px), como en el kit viejo.
- Fotos de producto en kit/productos/ (recortadas, fondo transparente o tarjeta blanca).
- Requiere: python playwright (ya instalado en el entorno) y las fuentes de kit/fonts/.
"""
import os
from playwright.sync_api import sync_playwright

KIT = os.path.dirname(os.path.abspath(__file__))
PRODUCTOS = os.path.join(KIT, "productos")
FOTOS = os.path.join(KIT, "fotos")

AMARILLO = "#ffce1f"
NEGRO = "#131313"
HUESO = "#f4f3f1"


def _fuentes():
    return "".join(
        f'@font-face {{ font-family: Archivo; src: url("file://{KIT}/fonts/Archivo-{w}.ttf"); font-weight: {w}; }}\n'
        for w in (400, 500, 600, 700, 800))


CSS = _fuentes() + f"""
@page {{ size: 1080px 1350px; margin: 0; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ width:1080px; }}
body {{ font-family: Archivo, sans-serif; -webkit-font-smoothing: antialiased; text-rendering: geometricPrecision; font-kerning: normal; }}
section {{ position:relative; width:1080px; height:1350px; overflow:hidden; break-after:page; }}
section > * {{ position:absolute; left:80px; }}
.oscuro {{ background:{NEGRO}; color:#fff; --suave:#d6d3cf; --linea:#303030; --tarjeta:#2a2a2a; }}
.claro {{ background:{HUESO}; color:{NEGRO}; --suave:#5c5955; --linea:#d6d3cf; --tarjeta:#fff; }}
.y {{ color:{AMARILLO}; }} .suave {{ color:var(--suave); }}
.logo {{ top:78px; width:190px; }}
.num {{ top:96px; left:auto; right:80px; font-size:22px; font-weight:600; color:var(--suave); }}
.pre {{ font-size:30px; font-weight:500; }}
h1.gigante {{ font-size:112px; line-height:122px; font-weight:800; letter-spacing:-0.035em; }}
h1.grande {{ font-size:96px; line-height:108px; font-weight:800; letter-spacing:-0.035em; }}
h2 {{ font-size:72px; line-height:80px; font-weight:700; letter-spacing:-0.025em; }}
.numero {{ font-size:150px; line-height:170px; font-weight:800; letter-spacing:-0.035em; }}
.bajada {{ font-size:34px; line-height:44px; font-weight:500; color:var(--suave); }}
.texto {{ font-size:30px; line-height:40px; font-weight:500; width:920px; }}
.chico {{ font-size:22px; line-height:30px; color:var(--suave); width:920px; }}
.foto {{ left:auto; background-size:contain; background-repeat:no-repeat; background-position:center; }}
.tarjeta {{ width:920px; border-radius:8px; background:var(--tarjeta); padding:24px; }}
.puntos {{ display:flex; gap:14px; }}
.puntos i {{ width:12px; height:12px; border-radius:50%; }}
.oscuro .puntos i {{ background:#fff; }} .claro .puntos i {{ background:#3c3c3c; }}
.puntos i.y {{ background:{AMARILLO} !important; }}
.pie {{ top:1240px; width:920px; border-top:2px solid var(--linea); padding-top:34px; display:flex; justify-content:space-between; }}
.pie span {{ font-size:24px; font-weight:600; color:var(--suave); }}
.claro .pie span {{ color:{NEGRO}; }}
.pie b {{ font-size:22px; font-weight:600; letter-spacing:.04em; }}
.oscuro .pie b {{ color:{AMARILLO}; }}
"""


def lamina(contenido, oscuro=False):
    return f'<section class="{"oscuro" if oscuro else "claro"}">{contenido}</section>'


def cabecera(i=None, total=None, oscuro=False):
    logo = f"file://{KIT}/logo_{'blanco' if oscuro else 'negro'}.png"
    num = f'<div class="num">{i}/{total}</div>' if i else ""
    return f'<img class="logo" src="{logo}">{num}'


def pie(oscuro=False, texto="Pana Iluminación", cta="CONSULTANOS →"):
    return f'<div class="pie"><span>{texto}</span><b>{cta}</b></div>'


def puntos(top, left=80):
    return (f'<div class="puntos" style="top:{top}px;left:{left}px">'
            + "".join(f'<i class="{"y" if i == 7 else ""}"></i>' for i in range(8)) + "</div>")


def foto(ruta, top, right=80, ancho=330, alto=310):
    return (f'<div class="foto" style="top:{top}px;right:{right}px;width:{ancho}px;height:{alto}px;'
            f"background-image:url('file://{ruta}')\"></div>")


def render(laminas, base, css_extra="", png=True):
    """Genera base.pdf (vectorial), base_N.png (2160 x 2700) y base_portada.jpg."""
    os.makedirs(os.path.dirname(os.path.abspath(base)), exist_ok=True)
    html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{css_extra}</style></head><body>'
            + "".join(laminas) + "</body></html>")
    hp = base + ".html"
    open(hp, "w").write(html)
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
        pg.goto("file://" + os.path.abspath(hp))
        pg.wait_for_timeout(400)
        pg.pdf(path=base + ".pdf", width="1080px", height="1350px", print_background=True)
        secs = pg.query_selector_all("section")
        for n, s in enumerate(secs, 1):
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
