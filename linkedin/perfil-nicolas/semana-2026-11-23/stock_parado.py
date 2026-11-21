"""Jueves 26/11/2026 · Meses de stock: cuánto tarda en venderse lo que tenés en el depósito.

Composición: RANKING de barras horizontales, fondo BORDÓ + acento LIMA (distinta del miércoles 25, cascada blanca
y azul, y del viernes 27, marrón y dorado). Todos los números son de ejemplo.
Ejecutar: python3 stock_parado.py   (genera 06_meses_de_stock.mp4 / .gif / _portada.jpg en esta carpeta)
"""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
from kit_animado import render_anim

KITF = os.path.join(os.path.dirname(os.path.dirname(AQUI)), "kit", "fonts")
ARCHIVO = "".join(f'@font-face{{font-family:Archivo;src:url("file://{KITF}/Archivo-{w}.ttf");font-weight:{w}}}'
                  for w in (500, 600, 700, 800))

BO, BO2, LI, RS, CR = "#3a0b1d", "#22050f", "#c8f53a", "#ff6b8b", "#fbe9ee"
# (producto, stock, ventas por mes)
FILAS = [("Lámpara de mesa", 30, 15), ("Aplique de pared", 24, 6), ("Colgante", 18, 3), ("Lámpara de pie", 40, 2)]
X0, PXM, TOP, PASO = 70, 38, 440, 150          # 1 mes = 38 px · 20 meses = 760 px
LIM = 6                                         # límite de ejemplo

css = ARCHIVO + f"""
#pz {{ padding:0 !important; color:{CR}; font-family:Inter,sans-serif;
       background:radial-gradient(1000px 800px at 85% 0%, #5a1430 0%, {BO} 45%, {BO2} 100%) !important; }}
.t {{ position:absolute; left:70px; top:66px; font:800 76px/1.02 Archivo; letter-spacing:-0.045em; color:#fff; }}
.t em {{ font-style:normal; color:{LI}; }}
.f {{ position:absolute; left:70px; top:262px; display:flex; gap:14px; align-items:center; font:700 28px Inter; }}
.f b {{ background:{LI}; color:{BO2}; padding:10px 18px; border-radius:14px; font:800 28px Inter; }}
.fila {{ position:absolute; left:{X0}px; width:940px; }}
.fila .nom {{ font:800 30px Inter; color:#fff; }}
.fila .cta {{ margin-left:12px; font:600 25px Inter; color:#e3b7c4; }}
.bar {{ position:absolute; left:0; top:56px; height:50px; width:0; border-radius:0 12px 12px 0; background:{LI}; }}
.num {{ position:absolute; right:0; top:60px; font:800 34px Archivo; white-space:nowrap; color:#fff; }}
.seg {{ position:absolute; left:{LIM * PXM - 2}px; top:48px; width:0; height:0; border-left:4px dashed {RS}; }}
.liml {{ position:absolute; left:{X0 + LIM * PXM - 9}px; top:{TOP - 34}px; font:800 22px Inter; color:{RS}; letter-spacing:.04em; }}
.call {{ position:absolute; left:70px; right:70px; top:1052px; border-radius:26px; background:{CR}; color:{BO2}; padding:26px 30px;
         display:flex; gap:26px; align-items:center; }}
.call .big {{ font:800 62px/1 Archivo; letter-spacing:-0.04em; color:#b0123f; white-space:nowrap; }}
.call .tx {{ font:700 27px/1.28 Inter; }}
.pie {{ position:absolute; left:70px; right:70px; bottom:36px; display:flex; justify-content:space-between; font:600 22px Inter; color:#d9a7b6; }}
.pie b {{ color:#fff; }}
"""

filas = ""
for i, (nom, st, vm) in enumerate(FILAS):
    filas += (f'<div class="fila" id="fl{i}" style="top:{TOP + PASO * i}px"><span class="nom">{nom}</span>'
              f'<span class="cta">{st} en stock ÷ {vm} por mes</span>'
              f'<div class="bar" id="br{i}"></div><div class="seg" id="sg{i}"></div><div class="num" id="nm{i}">0 meses</div></div>')

html = (f'<style>{css}</style><div id="pz">'
        f'<div class="t" id="ti">¿Cuánto tarda en venderse<br>lo que tenés <em>en el depósito?</em></div>'
        f'<div class="f" id="fo"><b>stock ÷ ventas por mes</b> = meses para venderlo</div>'
        f'<div class="liml" id="ll">↓ LÍMITE DE EJEMPLO: {LIM} MESES</div>{filas}'
        f'<div class="call" id="ca"><div class="big">$1.000.000</div>'
        f'<div class="tx">40 lámparas de pie × $25.000 de costo, quietas por 20 meses. No las repongas: combo o promo.</div></div>'
        f'<div class="pie"><span>Números de ejemplo</span><b>Nicolás Benítez</b></div></div>')

js = f"""
const F = {[[st, vm] for (_, st, vm) in FILAS]!r}, PXM = {PXM}, LIM = {LIM}, ALTO = {PASO * len(FILAS) - 10};
const LI = '{LI}', RS = '{RS}';
function frame(t) {{
  const out = 1 - seg(t, .95, 1);
  document.querySelectorAll('#pz > *').forEach(e => e.style.opacity = out);
  const a = ease(seg(t, .02, .1)); set('ti', {{opacity: a*out, transform:`translateY(${{(1-a)*-20}}px)`}});
  set('fo', {{opacity: ease(seg(t, .08, .14))*out}});
  for (let i = 0; i < 4; i++) {{
    const s = .14 + .1*i, m = F[i][0] / F[i][1];
    const g = ease(seg(t, s, s + .12)), v = m * g;
    set('fl'+i, {{opacity: seg(t, s - .03, s + .02)*out}});
    const lento = m > LIM && t > .66;
    set('br'+i, {{width: v*PXM + 'px', background: lento ? RS : LI}});
    set('nm'+i, {{color: lento ? RS : '#fff'}});
    $('nm'+i).textContent = (Math.round(v) === 1 ? '1 mes' : Math.round(v) + ' meses');
  }}
  const l = ease(seg(t, .58, .66));
  for (let i = 0; i < 4; i++) set('sg'+i, {{height: 66*l + 'px'}}); set('ll', {{opacity: seg(t, .62, .67)*out}});
  const c = ease(seg(t, .72, .8)); set('ca', {{opacity: c*out, transform:`translateY(${{(1-c)*20}}px)`}});
}}
"""

render_anim(html, js, os.path.join(AQUI, "06_meses_de_stock"), segundos=8, portada_t=0.9)
