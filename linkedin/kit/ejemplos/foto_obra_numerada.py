"""Foto de obra con las luces numeradas. Uso: python3 foto_obra_numerada.py <salida> <foto.png>
Las posiciones de los círculos (mk) se ajustan mirando la foto."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from html_kit import lamina, cabecera, pie, render
FOTO = sys.argv[2]  # foto original de la obra (Drive)
OUT = sys.argv[1]
CSS = """
.sangre { left:0; top:0; width:1080px; height:820px; background-size:cover; background-position:38% 50%; }
.velo { left:0; top:0; width:1080px; height:820px; background:linear-gradient(180deg, rgba(10,10,10,.55) 0%, rgba(10,10,10,0) 16%); }
.mk { width:56px; height:56px; border-radius:50%; background:#ffce1f; color:#131313; font-size:30px; font-weight:800;
      display:flex; align-items:center; justify-content:center; box-shadow:0 0 0 4px rgba(19,19,19,.85); }
.lst { width:920px; display:grid; grid-template-columns:1fr 1fr; column-gap:40px; row-gap:26px; }
.lst div { display:flex; gap:16px; align-items:flex-start; font-size:30px; line-height:38px; font-weight:600; }
.lst i { flex:0 0 44px; height:44px; border-radius:50%; background:#ffce1f; color:#131313; font-style:normal; font-size:24px; font-weight:800; display:flex; align-items:center; justify-content:center; margin-top:-3px; }
"""
mk = lambda n, x, y: f'<div class="mk" style="left:{x - 28}px;top:{y - 28}px">{n}</div>'
items = ["Tira LED en buña sobre los listones", "Balizas embutidas en la escalera", "Apliques lineales verticales", "Spot embutido en el cielorraso"]
s = lamina('<div class="sangre" style="background-image:url(\'file://' + FOTO + '\')"></div><div class="velo"></div>'
    + cabecera(None, None, True)
    + mk(1, 395, 250) + mk(2, 785, 640) + mk(3, 560, 425) + mk(4, 925, 200)
    + '<div class="pre y" style="top:870px">Obra de un cliente de Pana</div>'
    + '<h2 style="top:912px;color:#fff">Un hall, 4 luces.</h2>'
    + '<div class="lst" style="top:1030px">' + "".join(f'<div><i>{i + 1}</i><span>{t}</span></div>' for i, t in enumerate(items)) + '</div>'
    + pie(True), True)
render([s], os.path.join(OUT, "04_obra_hall_v2"), css_extra=CSS)
