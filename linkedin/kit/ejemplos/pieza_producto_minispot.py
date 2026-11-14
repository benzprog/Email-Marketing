import os, sys
sys.path.insert(0, "/home/claude/email-marketing/linkedin/kit")
from html_kit import lamina, cabecera, render
FOTO = sys.argv[1]  # recorte de kit/productos/TZ-SPOTF-COB-3W_blanco_negro.jpg, caja (60,235,1194,800)
FD = "/usr/share/fonts/opentype/inter"
fonts = "".join(f'@font-face{{font-family:Inter;src:url("file://{FD}/Inter-{n}.otf");font-weight:{w}}}' for n, w in [("Regular",400),("Medium",500),("SemiBold",600)]) \
      + "".join(f'@font-face{{font-family:InterD;src:url("file://{FD}/InterDisplay-{n}.otf");font-weight:{w}}}' for n, w in [("Medium",500),("SemiBold",600),("Bold",700)])
CSS = fonts + """
section, section * { font-family: Inter, sans-serif; }
section.oscuro { background:#000; }
.eyebrow { top:182px; left:80px; font-size:24px; font-weight:500; color:#ffce1f; }
.tit { top:222px; left:80px; width:920px; font-family:InterD, Inter, sans-serif; font-size:68px; line-height:76px; font-weight:600; letter-spacing:-0.02em; color:#f5f5f7; }
.ft { left:0; top:400px; width:1080px; height:520px; background-size:cover; background-position:50% 50%; }
.velo { left:0; top:400px; width:1080px; height:520px; background:linear-gradient(180deg,#000 0%,rgba(0,0,0,0) 14%,rgba(0,0,0,0) 80%,#000 100%); }
.datos { top:945px; left:80px; width:920px; display:grid; grid-template-columns:1fr 1fr 1fr; column-gap:40px; }
.datos div b { display:block; font-family:InterD, Inter, sans-serif; font-size:60px; line-height:66px; font-weight:600; color:#f5f5f7; letter-spacing:-0.02em; }
.datos div span { display:block; margin-top:8px; font-size:22px; line-height:30px; color:#a1a1a6; }
.extra { top:1160px; left:80px; width:920px; font-size:22px; line-height:30px; color:#a1a1a6; }
.pie2 { top:1262px; left:80px; width:920px; display:flex; justify-content:space-between; border-top:1px solid #333336; padding-top:26px; font-size:20px; color:#a1a1a6; }
.pie2 b { font-weight:500; color:#ffce1f; }
"""
s = lamina(cabecera(None, None, True)
    + '<div class="eyebrow">Producto Tenaruz</div>'
    + '<div class="tit">Mini spot COB 3 W:<br>hueco de 28 mm.</div>'
    + f'<div class="ft" style="background-image:url(\'file://{FOTO}\')"></div><div class="velo"></div>'
    + '<div class="datos">'
    + '<div><b>28 mm</b><span>Hueco en el cielorraso<br>(aro de 38 mm)</span></div>'
    + '<div><b>250 lm</b><span>3 W · 3000 K<br>Apertura de 38°</span></div>'
    + '<div><b>220 V</b><span>220–240 V<br>Driver incluido</span></div>'
    + '</div>'
    + '<div class="extra">Clase II · IP20, para interior · 30 mm de alto · Negro (TZ-SPOTFN-COB-3W-3K) o blanco</div>'
    + '<div class="pie2"><span>Pana Iluminación</span><b>Consultanos</b></div>', True)
render([s], sys.argv[2], css_extra=CSS)
