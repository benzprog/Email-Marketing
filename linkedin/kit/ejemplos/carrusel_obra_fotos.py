import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # fotos (t1_m.png...) en la misma carpeta que el script o ajustar H
from html_kit import lamina, cabecera, render
H = os.path.dirname(os.path.abspath(__file__)); FD = "/usr/share/fonts/opentype/inter"
NOMBRE = sys.argv[1] if len(sys.argv) > 1 else "Teatro San Martín"
fonts = "".join(f'@font-face{{font-family:Inter;src:url("file://{FD}/Inter-{n}.otf");font-weight:{w}}}' for n, w in [("Light",300),("Regular",400),("Medium",500),("SemiBold",600)]) \
      + "".join(f'@font-face{{font-family:InterD;src:url("file://{FD}/InterDisplay-{n}.otf");font-weight:{w}}}' for n, w in [("Light",300),("Medium",500),("SemiBold",600)])
CSS = fonts + """
section, section * { font-family: Inter, sans-serif; }
section.oscuro { background:#000; }
.full { left:0; top:0; width:1080px; height:1350px; background-size:cover; background-position:center; }
.ph { left:0; top:0; width:1080px; height:1010px; background-size:cover; background-position:center; }
.vt { left:0; top:0; width:1080px; height:200px; background:linear-gradient(180deg, rgba(0,0,0,.45), rgba(0,0,0,0)); }
.vb { left:0; top:0; width:1080px; height:1350px; background:linear-gradient(180deg, rgba(0,0,0,.55) 0%, rgba(0,0,0,0) 20%, rgba(0,0,0,0) 62%, rgba(0,0,0,.85) 100%); }
.n { top:96px; left:auto; right:80px; font-size:20px; color:#a1a1a6; }
.cap { top:1070px; width:920px; }
.cap .k { font-size:22px; font-weight:500; color:#ffce1f; margin-bottom:10px; }
.cap .t { font-family:InterD, Inter; font-size:44px; line-height:52px; font-weight:500; letter-spacing:-0.015em; color:#f5f5f7; }
.line { height:1px; background:#3a3a3c; width:920px; }
.eye { font-size:24px; font-weight:500; color:#ffce1f; }
.big { font-family:InterD, Inter; font-weight:300; color:#f5f5f7; letter-spacing:-0.03em; }
.small { font-size:26px; line-height:36px; color:#a1a1a6; width:920px; }
.cta { font-family:InterD, Inter; font-size:72px; line-height:80px; font-weight:500; letter-spacing:-0.025em; color:#f5f5f7; }
"""
T = 5
num = lambda i: f'<div class="n">{i}/{T}</div>'
def foto(i, img, k, t, pos="center"):
    return lamina(f'<div class="ph" style="background-image:url(\'file://{H}/{img}\');background-position:{pos}"></div><div class="vt"></div>'
        + cabecera(None, None, True) + num(i)
        + f'<div class="cap"><div class="k">{k}</div><div class="t">{t}</div></div>', True)
s1 = lamina(f'<div class="ph" style="height:640px;background-image:url(\'file://{H}/t1_m.png\');background-position:50% 40%"></div><div class="vt"></div>'
    + cabecera(None, None, True) + num(1)
    + '<div class="eye" style="top:700px">Obra de Pana Iluminación · Buenos Aires</div>'
    + f'<div class="big" style="top:745px;font-size:104px;line-height:112px">{NOMBRE}</div>'
    + '<div class="line" style="top:1010px"></div>'
    + '<div class="small" style="top:1040px">Iluminación de sala: tira LED oculta,<br>spots embutidos y mini spots en los escalones.</div>', True)
s2 = foto(2, "t3_m.png", "La sala", "Dos líneas de tira LED oculta a lo largo del revestimiento de madera.", "50% 50%")
s3 = foto(3, "t2_m.png", "El detalle", "Una línea de tira LED arriba del revestimiento y otra a mitad de la pared.", "62% 50%")
s4 = foto(4, "t4_m.png", "La pantalla", "Spots embutidos en el cielorraso negro, lejos de la pantalla.", "38% 50%")
s5 = lamina(cabecera(None, None, True) + num(5)
    + '<div class="eye" style="top:420px">Salas, halls y locales comerciales</div>'
    + '<div class="cta" style="top:470px">Mandanos tus planos.<br><span style="color:#ffce1f">Lo resolvemos con vos.</span></div>'
    + '<div class="line" style="top:760px"></div>'
    + '<div class="small" style="top:790px">WhatsApp 11 6288-3659<br>con la palabra LINKEDIN</div>'
    + '<div class="small" style="top:1200px;font-size:22px">Pana Iluminación</div>', True)
render([s1, s2, s3, s4, s5], os.path.join(H, "obra_teatro"), css_extra=CSS)
