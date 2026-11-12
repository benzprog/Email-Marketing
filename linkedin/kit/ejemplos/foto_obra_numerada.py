"""Foto de obra con las luces numeradas, estética limpia (Inter) con acentos amarillos de Pana.
Uso: python3 foto_obra_numerada.py <salida> <foto.png>. Ajustar posiciones (mk) y lista mirando la foto."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from html_kit import lamina, cabecera, render
FOTO = sys.argv[2]; OUT = sys.argv[1]
FD = "/usr/share/fonts/opentype/inter"
fonts = "".join(f'@font-face{{font-family:Inter;src:url("file://{FD}/Inter-{n}.otf");font-weight:{w}}}' for n, w in [("Regular",400),("Medium",500),("SemiBold",600)]) \
      + "".join(f'@font-face{{font-family:InterD;src:url("file://{FD}/InterDisplay-{n}.otf");font-weight:{w}}}' for n, w in [("Medium",500),("SemiBold",600),("Bold",700)])
CSS = fonts + """
section, section * { font-family: Inter, sans-serif; }
.sangre { left:0; top:0; width:1080px; height:840px; background-size:cover; background-position:38% 50%; }
.velo { left:0; top:0; width:1080px; height:840px; background:linear-gradient(180deg, rgba(0,0,0,.45) 0%, rgba(0,0,0,0) 18%); }
.mk { width:40px; height:40px; border-radius:50%; background:rgba(255,255,255,.92); color:#1d1d1f;
      font-size:20px; font-weight:500; display:flex; align-items:center; justify-content:center;
      box-shadow:0 2px 10px rgba(0,0,0,.35); }
.eyebrow { top:900px; font-size:24px; font-weight:500; color:#ffce1f; letter-spacing:0; }
.tit { top:940px; font-family:InterD, Inter, sans-serif; font-size:64px; line-height:72px; font-weight:600; letter-spacing:-0.02em; color:#f5f5f7; }
.lst { top:1050px; width:920px; display:grid; grid-template-columns:1fr 1fr; column-gap:48px; row-gap:22px; }
.lst div { display:flex; gap:14px; align-items:flex-start; font-size:26px; line-height:34px; font-weight:400; color:#f5f5f7; }
.lst i { flex:0 0 30px; height:30px; border-radius:50%; border:1.5px solid #a1a1a6; color:#f5f5f7; font-style:normal;
         font-size:16px; font-weight:500; display:flex; align-items:center; justify-content:center; margin-top:2px; }
.pie2 { top:1262px; width:920px; display:flex; justify-content:space-between; border-top:1px solid #333336; padding-top:26px; font-size:20px; color:#a1a1a6; }
.pie2 b { font-weight:500; color:#ffce1f; }
section.oscuro { background:#000; }
"""
mk = lambda n, x, y: f'<div class="mk" style="left:{x - 20}px;top:{y - 20}px">{n}</div>'
items = ["Tira LED oculta arriba de los listones", "Mini spots en la pared de la escalera", "Apliques lineales verticales", "Spot embutido en el cielorraso"]
s = lamina(f'<div class="sangre" style="background-image:url(\'file://{FOTO}\')"></div><div class="velo"></div>'
    + cabecera(None, None, True)
    + mk(1, 395, 255) + mk(2, 790, 650) + mk(3, 560, 430) + mk(4, 925, 205)
    + '<div class="eyebrow">Obra de un cliente de Pana</div>'
    + '<div class="tit">Un hall, 4 luces.</div>'
    + '<div class="lst">' + "".join(f'<div><i>{i + 1}</i><span>{t}</span></div>' for i, t in enumerate(items)) + '</div>'
    + '<div class="pie2"><span>Pana Iluminación</span><b>Consultanos</b></div>', True)
render([s], os.path.join(OUT, "obra_hall_apple"), css_extra=CSS)
