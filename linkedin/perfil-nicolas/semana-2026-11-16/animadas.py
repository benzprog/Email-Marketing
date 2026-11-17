"""Infografías animadas de la semana del 16/11/2026. Ejecutar: python3 animadas.py [02|03]  (OUT=carpeta opcional)"""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
from kit_animado import *

OUT = os.environ.get("OUT", AQUI)
QUE = sys.argv[1:] or ["02", "03"]
C = COLORES
SOBRE = ('<svg viewBox="0 0 24 18" width="{w}" height="{h}"><rect x="1" y="1" width="22" height="16" rx="3" fill="{c}"/>'
         '<path d="M2 3l10 7 10-7" fill="none" stroke="#0d0f14" stroke-width="2"/></svg>')

# =====================================================================================
# 02 · 4 datos que tenés que mirar si vendés online (pedido de Nicolás, 17/11/2026)
# =====================================================================================
if "02" in QUE:
    def num(idt, size=54, color="#fff", extra=""):
        return f'<span id="{idt}" style="font-size:{size}px;font-weight:800;letter-spacing:-0.03em;color:{color};{extra}">0</span>'

    def barra(idt, top, etiqueta, valor_id, color):
        return (f'<div class="mini" style="left:18px;top:{top}px;font-size:21px;color:#aab1c0">{etiqueta}</div>'
                f'<div class="mini" style="right:18px;top:{top}px;font-size:21px">{num(valor_id, 21)}</div>'
                f'<div style="position:absolute;left:18px;right:18px;top:{top + 30}px;height:24px;border-radius:13px;background:#1f2533">'
                f'<div id="{idt}" style="height:100%;width:0;border-radius:13px;background:{color}"></div></div>')

    # 1 · conversión: visitas contra ventas
    v1 = (barra("bv", 18, "Visitas", "nv", C[0]) + barra("bs", 84, "Ventas", "ns", C[1])
          + f'<div id="r1" style="position:absolute;left:0;right:0;bottom:12px;text-align:center">{num("p1", 38, C[0], "white-space:nowrap")}</div>')
    # 2 · ticket promedio: facturación ÷ pedidos
    bolsas = "".join(f'<i id="bo{k}" style="display:inline-block;width:20px;height:24px;margin:0 3px;border-radius:4px 4px 6px 6px;'
                     f'background:{C[1]}"></i>' for k in range(15))
    v2 = (f'<div class="mini" style="left:0;right:0;top:16px;text-align:center;font-size:21px;color:#aab1c0">Facturaste</div>'
          f'<div style="position:absolute;left:0;right:0;top:40px;text-align:center">{num("f2", 46)}</div>'
          f'<div style="position:absolute;left:0;right:0;top:110px;text-align:center;line-height:0">{bolsas}</div>'
          f'<div id="d2" class="mini" style="left:0;right:0;top:146px;text-align:center;font-size:22px;color:#aab1c0">en 15 pedidos</div>'
          f'<div id="r2" style="position:absolute;left:0;right:0;bottom:12px;text-align:center">{num("p2", 38, C[1], "white-space:nowrap")}</div>')
    # 3 · carritos abandonados: 3 de cada 4
    carro = ('<svg viewBox="0 0 48 40" width="72" height="60"><path d="M3 5h7l6 22h22l5-15H13" fill="none" stroke="{c}" stroke-width="4" '
             'stroke-linecap="round" stroke-linejoin="round"/><circle cx="19" cy="34" r="3.5" fill="{c}"/><circle cx="35" cy="34" r="3.5" fill="{c}"/></svg>')
    v3 = "".join(f'<div id="ca{k}" style="position:absolute;top:40px;left:{20 + 96 * k}px;width:80px;text-align:center">{carro.format(c="#cfd5e2")}'
                 f'<div id="mk{k}" style="font-size:30px;font-weight:900;color:{C[3] if k < 3 else C[1]}">{"✕" if k < 3 else "✓"}</div></div>'
                 for k in range(4))
    v3 += (f'<div id="d3" class="mini" style="left:0;right:0;top:146px;text-align:center;font-size:22px;color:#aab1c0">3 de cada 4 no terminan la compra</div>'
           f'<div id="r3" style="position:absolute;left:0;right:0;bottom:12px;text-align:center">{num("p3", 38, C[2], "white-space:nowrap")}</div>')
    # 4 · costo por cliente nuevo
    persona = ('<svg viewBox="0 0 20 24" width="26" height="31"><circle cx="10" cy="6" r="5" fill="{c}"/>'
               '<path d="M1 23c0-6 4-10 9-10s9 4 9 10z" fill="{c}"/></svg>')
    v4 = (f'<div class="mini" style="left:0;right:0;top:16px;text-align:center;font-size:21px;color:#aab1c0">Gastaste en publicidad</div>'
          f'<div style="position:absolute;left:0;right:0;top:40px;text-align:center">{num("f4", 46)}</div>'
          f'<div style="position:absolute;left:0;right:0;top:110px;text-align:center">'
          + "".join(f'<span id="pe{k}" style="display:inline-block;margin:0 3px">{persona.format(c=C[3])}</span>' for k in range(10))
          + '</div><div id="d4" class="mini" style="left:0;right:0;top:150px;text-align:center;font-size:22px;color:#aab1c0">y llegaron 10 clientes nuevos</div>'
          f'<div id="r4" style="position:absolute;left:0;right:0;bottom:12px;text-align:center">{num("p4", 38, C[3], "white-space:nowrap")}</div>')

    tarjetas = [
        tarjeta(1, "Tasa de conversión", v1, "Ventas ÷ visitas: <b>cuántos de los que entran compran</b>.", C[0]),
        tarjeta(2, "Ticket promedio", v2, "Facturación ÷ pedidos: <b>cuánto gasta cada uno</b>.", C[1]),
        tarjeta(3, "Carritos abandonados", v3, "Cargan el carrito y no pagan. <b>Revisá envío y medios de pago</b>.", C[2]),
        tarjeta(4, "Costo por cliente nuevo", v4, "Publicidad ÷ clientes nuevos. <b>Menos de lo que ganás por cliente</b>.", C[3]),
    ]
    html = pieza('4 datos que tenés que mirar<br><em>si vendés online</em>', "Qué son y cómo se calculan, con un ejemplo.",
                 tarjetas, "<b>¿Cuál mirás vos todas las semanas?</b>")
    js = f"""
    const AR = n => Math.round(n).toLocaleString('es-AR');
    const cuenta = (id, v, x, pre='', suf='') => {{ $(id).textContent = pre + AR(v * ease(cl(x))) + suf; }};
    const pop = (id, x) => set(id, {{opacity: ease(cl(x)), transform:`scale(${{.7 + .3*ease(cl(x))}})`}});
    function frame(t) {{
      const out = 1 - seg(t, .93, 1);
      document.querySelectorAll('.vis').forEach(v => v.style.opacity = out);
      // 1 · 1.000 visitas, 15 ventas = 1,5 %
      set('bv', {{width: 100*ease(seg(t, .04, .3)) + '%'}}); cuenta('nv', 1000, seg(t, .04, .3));
      set('bs', {{width: 1.5*ease(seg(t, .3, .45)) + '%', minWidth: t > .3 ? '26px' : '0'}}); cuenta('ns', 15, seg(t, .3, .45));
      $('p1').textContent = '= 1,5 % compra'; pop('r1', seg(t, .5, .6));
      // 2 · $450.000 ÷ 15 pedidos = $30.000 por pedido
      cuenta('f2', 450000, seg(t, .04, .3), '$');
      for (let k = 0; k < 15; k++) set('bo'+k, {{opacity: seg(t, .28 + .012*k, .3 + .012*k), transform:`translateY(${{(1-seg(t,.28+.012*k,.32+.012*k))*-14}}px)`}});
      set('d2', {{opacity: seg(t, .44, .5)}});
      $('p2').textContent = '= $30.000 por pedido'; pop('r2', seg(t, .54, .64));
      // 3 · 3 de cada 4 carritos se abandonan = 75 %
      for (let k = 0; k < 4; k++) {{
        const a = ease(seg(t, .04 + .06*k, .12 + .06*k));
        const fuera = k < 3 ? ease(seg(t, .36 + .05*k, .46 + .05*k)) : 0;
        set('ca'+k, {{opacity: a * (1 - .65*fuera), transform:`translateY(${{(1-a)*-20 + fuera*14}}px)`}});
        set('mk'+k, {{opacity: seg(t, .36 + .05*k, .42 + .05*k)}});
      }}
      set('d3', {{opacity: seg(t, .56, .62)}});
      $('p3').textContent = '= 75 % abandona'; pop('r3', seg(t, .6, .7));
      // 4 · $90.000 en publicidad, 10 clientes = $9.000 cada uno
      cuenta('f4', 90000, seg(t, .04, .3), '$');
      for (let k = 0; k < 10; k++) pop('pe'+k, seg(t, .3 + .02*k, .34 + .02*k));
      set('d4', {{opacity: seg(t, .52, .58)}});
      $('p4').textContent = '= $9.000 por cliente'; pop('r4', seg(t, .62, .72));
    }}
    """
    render_anim(html, js, f"{OUT}/02_ecommerce_4_datos", portada_t=0.85)
