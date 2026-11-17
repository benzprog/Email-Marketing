"""Infografías animadas del perfil de Nicolás (formato pedido el 17/11/2026, estilo "4 usos de ...").

Una sola pieza de 1080 x 1350 con un título arriba y 4 tarjetas en grilla de 2 x 2. Cada tarjeta tiene un número,
un título corto, una animación chica que muestra la acción (una planilla que se llena, un chat que se escribe, un
menú que se abre) y una línea concreta abajo. La animación es un bucle de unos 6 segundos.

Cómo funciona: la pieza es HTML; una función JS `frame(t)` (t de 0 a 1) acomoda todo para ese instante.
Playwright saca una captura por cuadro y ffmpeg arma el MP4 (para Buffer/LinkedIn, que lo reproduce solo y sin
sonido) y un GIF de respaldo.

Uso:
    from kit_animado import pieza, render_anim
    html = pieza(titulo, bajada, [tarjeta1, ...4], nota, colores)
    render_anim(html, js, "semana-AAAA-MM-DD/02_tema")   # -> 02_tema.mp4, 02_tema.gif, 02_tema_portada.jpg
"""
import os, shutil, subprocess, tempfile
from playwright.sync_api import sync_playwright

COLORES = ["#4c8dff", "#2fd27a", "#ffa53d", "#ff4f8b"]  # azul, verde, naranja, rosa (uno por tarjeta)

CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
html, body { width:1080px; height:1350px; background:#0d0f14; }
body { font-family:'Inter',sans-serif; color:#fff; -webkit-font-smoothing:antialiased; }
#pz { position:relative; width:1080px; height:1350px; overflow:hidden; padding:58px 56px 0;
      background:radial-gradient(1200px 600px at 50% -10%, #1a2030 0%, #0d0f14 60%); }
.tit { font-family:'Inter Display','Inter',sans-serif; font-size:56px; line-height:1.05; font-weight:800; letter-spacing:-0.035em; text-align:center; }
.tit em { font-style:normal; color:var(--ac0); }
.baj { margin-top:12px; text-align:center; font-size:28px; font-weight:600; color:#8fd3ff; }
.grilla { margin-top:30px; display:grid; grid-template-columns:1fr 1fr; gap:26px; }
.card { position:relative; height:468px; border-radius:30px; border:3px solid var(--c); background:#141821;
        padding:26px 26px 22px; display:flex; flex-direction:column; }
.card .cab { display:flex; align-items:center; gap:16px; }
.card .n { width:46px; height:46px; flex:none; border-radius:50%; background:var(--c); color:#0d0f14; font-size:25px; font-weight:800;
           display:flex; align-items:center; justify-content:center; }
.card h3 { font-size:30px; line-height:1.08; font-weight:800; letter-spacing:-0.02em; }
.card .vis { position:relative; flex:1; margin:16px 0 14px; border-radius:18px; background:#0e1118; border:1px solid #232937; overflow:hidden; }
.card .pie { font-size:24px; line-height:1.3; font-weight:600; color:#cfd5e2; }
.card .pie b { color:var(--c); font-weight:800; }
.nota { position:absolute; left:56px; right:56px; bottom:34px; gap:24px; display:flex; justify-content:space-between; align-items:center; }
.nota span { font-size:25px; font-weight:600; color:#aab1c0; }
.nota span b { color:#fff; }
.firma { white-space:nowrap; flex:none; font-size:25px; font-weight:800; padding:12px 24px; border-radius:16px; border:3px solid var(--ac0); color:#fff; background:#141821; }
/* piezas chicas reutilizables */
.mini { position:absolute; font-size:21px; font-weight:600; }
.tabla { position:absolute; left:16px; right:16px; top:16px; display:grid; grid-template-columns:1.3fr 1fr .8fr; border-radius:12px; overflow:hidden;
         background:#fff; color:#151821; font-size:21px; font-weight:600; }
.tabla div { padding:9px 10px; border-right:1px solid #e3e6ea; border-bottom:1px solid #e3e6ea; white-space:nowrap; }
.tabla .h { background:#eef1f4; font-weight:800; }
.burb { position:absolute; border-radius:18px; padding:14px 16px; font-size:21px; line-height:1.32; font-weight:600; }
.cursor { position:absolute; width:30px; height:30px; z-index:9; }
.boton { position:absolute; border-radius:10px; padding:8px 14px; font-size:21px; font-weight:800; }
"""

CURSOR = ('<svg class="cursor" id="{id}" viewBox="0 0 24 24"><path d="M3 2l7 19 2.6-7.4L20 11z" fill="#fff" '
          'stroke="#0d0f14" stroke-width="1.6" stroke-linejoin="round"/></svg>')

JS_BASE = """
const $ = id => document.getElementById(id);
const cl = (x,a=0,b=1) => Math.max(a, Math.min(b, x));
const seg = (t,a,b) => cl((t-a)/(b-a));                 // 0..1 dentro del tramo [a,b]
const ease = x => x<.5 ? 4*x*x*x : 1-Math.pow(-2*x+2,3)/2;
const set = (id, css) => { const e=$(id); if(e) Object.assign(e.style, css); };
const mix = (a,b,x) => a+(b-a)*x;
const typed = (txt, x) => txt.slice(0, Math.round(txt.length*cl(x)));
"""


def tarjeta(i, titulo, visual, pie, color):
    return (f'<div class="card" style="--c:{color}"><div class="cab"><div class="n">{i}</div><h3>{titulo}</h3></div>'
            f'<div class="vis">{visual}</div><div class="pie">{pie}</div></div>')


def pieza(titulo, bajada, tarjetas, nota, firma="Nicolás Benítez", acento="#4c8dff"):
    return (f'<div id="pz" style="--ac0:{acento}"><div class="tit">{titulo}</div><div class="baj">{bajada}</div>'
            f'<div class="grilla">{"".join(tarjetas)}</div>'
            f'<div class="nota"><span>{nota}</span><div class="firma">{firma}</div></div></div>')


def render_anim(html, js, base, segundos=6.0, fps=15, portada_t=0.62, gif_ancho=800):
    """Genera base.mp4 (1080 x 1350, H.264, 30 fps), base.gif (respaldo) y base_portada.jpg (cuadro en portada_t)."""
    base = os.path.abspath(base)
    os.makedirs(os.path.dirname(base), exist_ok=True)
    doc = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{html}'
           f'<script>{JS_BASE}{js}</script></body></html>')
    tmp = tempfile.mkdtemp()
    hp = os.path.join(tmp, "p.html")
    open(hp, "w").write(doc)
    n = int(segundos * fps)
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        pg.goto("file://" + hp)
        pg.wait_for_timeout(500)
        el = pg.query_selector("#pz")
        for k in range(n):
            pg.evaluate(f"frame({k / n})")
            el.screenshot(path=os.path.join(tmp, f"f{k:04d}.png"))
        pg.evaluate(f"frame({portada_t})")
        el.screenshot(path=os.path.join(tmp, "portada.png"))
        b.close()
    f = os.path.join(tmp, "f%04d.png")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps), "-i", f, "-r", "30",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-preset", "slow", "-movflags", "+faststart",
                    base + ".mp4"], check=True)
    pal = os.path.join(tmp, "pal.png")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps), "-i", f, "-vf",
                    f"scale={gif_ancho}:-1:flags=lanczos,palettegen=max_colors=128", pal], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps), "-i", f, "-i", pal, "-lavfi",
                    f"scale={gif_ancho}:-1:flags=lanczos[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=4", "-loop", "0",
                    base + ".gif"], check=True)
    from PIL import Image
    Image.open(os.path.join(tmp, "portada.png")).convert("RGB").save(base + "_portada.jpg", "JPEG", quality=92)
    shutil.rmtree(tmp)
    for ext in (".mp4", ".gif"):
        print(base + ext, round(os.path.getsize(base + ext) / 1e6, 2), "MB")
    return base + ".mp4"
