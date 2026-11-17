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


# ---------- ayudas comunes para las piezas siguientes ----------
JS_UTIL = """
const AR = n => Math.round(n).toLocaleString('es-AR');
const cuenta = (id, v, x, pre='', suf='') => { $(id).textContent = pre + AR(v * ease(cl(x))) + suf; };
const pop = (id, x) => set(id, {opacity: ease(cl(x)), transform:`scale(${.7 + .3*ease(cl(x))})`});
const fadeVis = out => document.querySelectorAll('.vis').forEach(v => v.style.opacity = out);
"""
def caja(idt, txt, top, left=16, right=16, fondo="#1c2230", extra=""):
    return (f'<div id="{idt}" class="burb" style="left:{left}px;right:{right}px;top:{top}px;background:{fondo};border:1px solid #303850;'
            f'font-size:20px;{extra}">{txt}</div>')

# =====================================================================================
# 03 · 4 tareas de tu tienda online que podés pasarle a la IA
# =====================================================================================
if "03" in QUE:
    DESC = "Lámpara colgante de aluminio negro, 30 cm. Ideal para cocina o comedor."
    RESP = "¡Sí! Enviamos a todo el país. Te llega en 3 a 5 días hábiles."
    chips = "".join(f'<span id="ch{k}" style="display:inline-block;margin:0 6px 8px 0;padding:6px 12px;border-radius:10px;background:#2a3142;'
                    f'font-size:19px;font-weight:700">{t}</span>' for k, t in enumerate(["Aluminio", "Negro", "30 cm", "Colgante"]))
    v1 = (f'<div style="position:absolute;left:16px;right:16px;top:16px">{chips}</div>'
          f'<div id="fl1" style="position:absolute;left:0;right:0;top:100px;text-align:center;font-size:28px;font-weight:900;color:{C[0]}">↓</div>'
          + caja("d1", "", 140, extra="min-height:76px;line-height:1.3"))
    v2 = (caja("q2", "¿Hacen envíos al interior?", 16, right=120, fondo="#2b3245", extra="border-radius:18px 18px 18px 4px")
          + caja("a2", "", 92, left=80, fondo="#163828", extra="border-color:#1f5a3c;border-radius:18px 18px 4px 18px;line-height:1.3;min-height:60px"))
    QUEJAS = [("Demora en el envío", 100), ("Talle más chico", 62), ("Embalaje roto", 34)]
    v3 = "".join(f'<div id="rv{k}" style="position:absolute;top:{14 + 6 * k}px;left:{24 + 10 * k}px;width:150px;height:44px;border-radius:10px;'
                 f'background:#232a3a;border:1px solid #39425a;font-size:16px;padding:6px 10px;color:#aab1c0">★★☆☆☆ ···</div>' for k in range(4))
    v3 += (f'<div id="ar3" class="mini" style="left:200px;top:24px;font-size:28px;color:{C[2]}">→</div>'
           f'<div class="mini" id="tq3" style="left:240px;top:28px;font-size:19px;color:#aab1c0">las que más<br>se repiten</div>')
    for k, (t, w) in enumerate(QUEJAS):
        v3 += (f'<div class="mini" style="left:16px;top:{96 + 44 * k}px;font-size:19px">{t}</div>'
               f'<div style="position:absolute;left:210px;right:16px;top:{100 + 44 * k}px;height:18px;border-radius:9px;background:#1f2533">'
               f'<div id="qj{k}" data-w="{w}" style="height:100%;width:0;border-radius:9px;background:{C[2]}"></div></div>')
    ASUNTOS = ["Tu carrito te está esperando", "Últimas 24 h de envío gratis", "Volvió lo que buscabas"]
    v4 = "".join(f'<div id="as{k}" style="position:absolute;left:16px;right:16px;top:{16 + 62 * k}px;height:52px;border-radius:12px;background:#fff;'
                 f'color:#1f2430;display:flex;align-items:center;gap:12px;padding:0 14px;font-size:20px;font-weight:700">'
                 f'<span style="flex:none">{SOBRE.format(w=28, h=21, c=C[3])}</span><span id="at{k}"></span></div>' for k in range(3))
    tarjetas = [
        tarjeta(1, "Descripciones", v1, "Pasale los datos: <b>“Escribí la descripción para mi tienda.”</b>", C[0]),
        tarjeta(2, "Preguntas de clientes", v2, "Pasale tus condiciones y pedile <b>respuestas para las de siempre</b>.", C[1]),
        tarjeta(3, "Quejas en las reseñas", v3, "Pegá tus reseñas: <b>“¿Cuáles son las 3 quejas que más se repiten?”</b>", C[2]),
        tarjeta(4, "Asuntos de mails", v4, "<b>“Dame 10 asuntos para este mail.”</b> Probá los que más te gusten.", C[3]),
    ]
    html = pieza('4 tareas de tu tienda online<br><em>que podés pasarle a la IA</em>',
                 "Pegá el pedido en ChatGPT o Claude. Son gratis.", tarjetas, "<b>Siempre revisá</b> antes de publicar.")
    js = JS_UTIL + f"""
    const DESC = {DESC!r}, RESP = {RESP!r}, AS = {ASUNTOS!r};
    function frame(t) {{
      const out = 1 - seg(t, .93, 1); fadeVis(out);
      for (let k = 0; k < 4; k++) pop('ch'+k, seg(t, .03 + .05*k, .08 + .05*k));
      set('fl1', {{opacity: seg(t, .26, .3), transform:`translateY(${{Math.sin(t*40)*3}}px)`}});
      set('d1', {{opacity: seg(t, .3, .33)}}); $('d1').textContent = typed(DESC, seg(t, .32, .7));
      pop('q2', seg(t, .04, .12));
      set('a2', {{opacity: seg(t, .22, .26)}}); $('a2').textContent = typed(RESP, seg(t, .26, .6));
      for (let k = 0; k < 4; k++) set('rv'+k, {{opacity: seg(t, .03 + .05*k, .08 + .05*k)}});
      set('ar3', {{opacity: seg(t, .26, .3)}}); set('tq3', {{opacity: seg(t, .26, .3)}});
      for (let k = 0; k < 3; k++) {{ const e = $('qj'+k); e.style.width = e.dataset.w * ease(seg(t, .32 + .08*k, .5 + .08*k)) + '%'; }}
      for (let k = 0; k < 3; k++) {{ set('as'+k, {{opacity: seg(t, .05 + .2*k, .08 + .2*k)}}); $('at'+k).textContent = typed(AS[k], seg(t, .08 + .2*k, .22 + .2*k)); }}
      set('as1', {{outline: t > .75 ? '3px solid {C[3]}' : 'none'}});
    }}
    """
    render_anim(html, js, f"{OUT}/03_ia_tareas_tienda_online", portada_t=0.86)

# =====================================================================================
# 04 · ¿Te conviene hacer un 20 % de descuento?
# =====================================================================================
if "04" in QUE:
    def precio(idp, costo_id, gan_id, top, lbl):
        return (f'<div class="mini" style="left:16px;top:{top}px;font-size:19px;color:#aab1c0">{lbl}</div>'
                f'<div id="{idp}" style="position:absolute;left:16px;top:{top + 28}px;width:381px;height:50px;border-radius:12px;overflow:hidden;display:flex">'
                f'<div id="{costo_id}" style="width:60%;background:#3a4258;display:flex;align-items:center;justify-content:center;font-size:19px;font-weight:800">Costo $6.000</div>'
                f'<div id="{gan_id}" style="flex:1;background:{C[1]};color:#0d0f14;display:flex;align-items:center;justify-content:center;font-size:19px;font-weight:800;white-space:nowrap">Ganás $4.000</div></div>')
    v1 = (precio("pr1", "co1", "ga1", 16, "Precio $10.000")
          + f'<div id="r1" style="position:absolute;left:0;right:0;bottom:16px;text-align:center;font-size:38px;font-weight:800;color:{C[0]}">Ganás $4.000</div>')
    v2 = (f'<div class="mini" style="left:16px;top:16px;font-size:19px;color:#aab1c0" id="l2">Precio $10.000</div>'
          f'<div style="position:absolute;left:16px;top:44px;width:381px;height:50px;border-radius:12px;overflow:hidden;display:flex;background:#1a1f2b">'
          f'<div style="width:228.6px;flex:none;background:#3a4258;display:flex;align-items:center;justify-content:center;font-size:19px;font-weight:800">Costo $6.000</div>'
          f'<div id="g2" style="width:152.4px;flex:none;background:{C[1]};color:#0d0f14;display:flex;align-items:center;justify-content:center;font-size:19px;font-weight:800;overflow:hidden;white-space:nowrap">Ganás $4.000</div></div>'
          f'<div id="t2" class="mini" style="left:16px;right:16px;top:110px;text-align:center;font-size:21px;color:#aab1c0">El costo no baja: <b style="color:#fff">sigue en $6.000</b></div>'
          f'<div id="r2" style="position:absolute;left:0;right:0;bottom:16px;text-align:center;font-size:38px;font-weight:800;color:{C[1]}">Ganás $2.000</div>')
    v3 = "".join(f'<div class="mini" style="left:16px;top:{22 + 64 * k}px;font-size:19px;color:#aab1c0">{l}</div>'
                 f'<div id="b3{k}" style="position:absolute;left:175px;top:{18 + 64 * k}px;height:38px;width:0;border-radius:10px;background:{c};'
                 f'color:#0d0f14;font-size:19px;font-weight:800;display:flex;align-items:center;padding-left:12px;white-space:nowrap;overflow:hidden">{v}</div>'
                 for k, (l, v, c) in enumerate([("Sin descuento", "$4.000", C[1]), ("Con 20 % off", "$2.000", C[2])]))
    v3 += f'<div id="r3" style="position:absolute;left:0;right:0;bottom:16px;text-align:center;font-size:38px;font-weight:800;color:{C[2]}">−50 % de ganancia</div>'
    bolsa = '<i style="display:inline-block;width:22px;height:27px;margin:0 3px 6px;border-radius:4px 4px 7px 7px;background:{c}"></i>'
    v4 = (f'<div class="mini" style="left:16px;top:16px;font-size:19px;color:#aab1c0">Sin descuento: 10 ventas = $40.000</div>'
          f'<div style="position:absolute;left:16px;top:44px">' + "".join(f'<span id="ba{k}">{bolsa.format(c=C[1])}</span>' for k in range(10)) + '</div>'
          f'<div class="mini" style="left:16px;top:92px;font-size:19px;color:#aab1c0">Con 20 % off: para los mismos $40.000</div>'
          f'<div style="position:absolute;left:16px;right:16px;top:120px">' + "".join(f'<span id="bb{k}">{bolsa.format(c=C[3])}</span>' for k in range(20)) + '</div>'
          f'<div id="r4" style="position:absolute;left:0;right:0;bottom:12px;text-align:center;font-size:38px;font-weight:800;color:{C[3]}">20 ventas</div>')
    tarjetas = [
        tarjeta(1, "Tu ganancia hoy", v1, "Vendés a $10.000 y te cuesta $6.000: <b>ganás $4.000</b>.", C[0]),
        tarjeta(2, "Con 20 % menos", v2, "El precio baja $2.000, pero <b>el costo sigue igual</b>.", C[1]),
        tarjeta(3, "Ganás la mitad", v3, "Un 20 % de descuento te sacó <b>la mitad de la ganancia</b>.", C[2]),
        tarjeta(4, "Vendé el doble", v4, "Para ganar lo mismo, <b>necesitás el doble de ventas</b>.", C[3]),
    ]
    html = pieza('¿Te conviene hacer<br>un <em>20 % de descuento?</em>', "Hacé esta cuenta antes de lanzar la promo.",
                 tarjetas, "<b>Tip:</b> pedile a la IA que haga esta cuenta con tus números.")
    js = JS_UTIL + """
    function frame(t) {
      const out = 1 - seg(t, .93, 1); fadeVis(out);
      // 1
      const a = ease(seg(t, .04, .25));
      set('pr1', {width: 381*a + 'px'}); pop('r1', seg(t, .3, .4));
      // 2 · la ganancia se achica a la mitad
      const g = ease(seg(t, .2, .45));
      $('l2').textContent = g > .5 ? 'Precio $8.000 (20 % off)' : 'Precio $10.000';
      set('g2', {width: (152.4 - 76.2*g) + 'px'}); $('g2').textContent = g > .5 ? '$2.000' : 'Ganás $4.000';
      set('t2', {opacity: seg(t, .46, .52)}); pop('r2', seg(t, .5, .6));
      // 3
      set('b30', {width: 216*ease(seg(t, .08, .26)) + 'px'}); set('b31', {width: 108*ease(seg(t, .3, .46)) + 'px'});
      pop('r3', seg(t, .5, .6));
      // 4
      for (let k = 0; k < 10; k++) pop('ba'+k, seg(t, .04 + .015*k, .07 + .015*k));
      for (let k = 0; k < 20; k++) pop('bb'+k, seg(t, .28 + .015*k, .31 + .015*k));
      pop('r4', seg(t, .62, .72));
    }
    """
    render_anim(html, js, f"{OUT}/04_descuento_conviene", portada_t=0.86)

# =====================================================================================
# 05 · Si te abandonan el carrito, revisá esto
# =====================================================================================
if "05" in QUE:
    v1 = ('<div style="position:absolute;left:16px;right:16px;top:16px;border-radius:14px;background:#fff;color:#1f2430;padding:12px 16px;font-size:20px;font-weight:600">'
          '<div style="display:flex;justify-content:space-between"><span>Productos</span><b>$20.000</b></div>'
          '<div id="en1" style="display:flex;justify-content:space-between;margin-top:6px;color:#c6321c"><span>Envío</span><b>$5.000</b></div>'
          '<div style="display:flex;justify-content:space-between;margin-top:6px;border-top:1px solid #e5e7eb;padding-top:6px"><span>Total</span><b id="tt1">$20.000</b></div></div>'
          f'<div id="wo1" style="position:absolute;left:0;right:0;bottom:18px;text-align:center;font-size:34px;font-weight:900;color:{C[3]}">¿¡Y esto!?</div>'
          f'<div id="ok1" style="position:absolute;left:0;right:0;bottom:22px;text-align:center;font-size:24px;font-weight:800;color:{C[1]}">Mostralo desde el principio ✓</div>')
    PAGOS = ["Tarjeta de crédito", "Tarjeta de débito", "Transferencia", "Billetera virtual", "Cuotas"]
    v2 = "".join(f'<div id="pg{k}" style="position:absolute;left:16px;right:16px;top:{12 + 42 * k}px;height:36px;border-radius:10px;background:#1c2230;'
                 f'border:1px solid #303850;display:flex;align-items:center;gap:10px;padding:0 12px;font-size:19px;font-weight:700">'
                 f'<span style="width:20px;height:20px;border-radius:50%;background:{C[1]};color:#0d0f14;font-size:14px;display:flex;align-items:center;justify-content:center">✓</span>{p}</div>'
                 for k, p in enumerate(PAGOS))
    v3 = ('<div style="position:absolute;left:16px;right:16px;top:16px;border-radius:14px;background:#fff;color:#1f2430;padding:12px 16px;font-size:19px;font-weight:600">'
          '<div id="cr3" style="border:1px solid #d1d5db;border-radius:8px;padding:8px 10px;margin-bottom:8px">Crear usuario y contraseña</div>'
          '<div id="in3" style="border-radius:8px;padding:9px 10px;text-align:center;font-weight:800;color:#fff;background:#9aa3b2">Comprar como invitado</div></div>'
          + CURSOR.format(id="cu5"))
    v4 = (f'<div id="pa4" style="position:absolute;left:0;right:0;top:30px;display:flex;justify-content:center;gap:10px"></div>'
          f'<div id="r4" style="position:absolute;left:0;right:0;bottom:16px;text-align:center;font-size:34px;font-weight:800;color:{C[3]}">De 6 pasos a 3</div>'
          f'<div id="t4" class="mini" style="left:0;right:0;top:110px;text-align:center;font-size:20px;color:#aab1c0">Datos, envío y pago. Nada más.</div>')
    tarjetas = [
        tarjeta(1, "Envío a la vista", v1, "Si el costo aparece al final, <b>la sorpresa espanta</b>.", C[0]),
        tarjeta(2, "Más formas de pago", v2, "Tarjetas, transferencia, billeteras <b>y cuotas</b>.", C[1]),
        tarjeta(3, "Compra sin cuenta", v3, "Pedir usuario frena la compra. <b>Dejá comprar como invitado</b>.", C[2]),
        tarjeta(4, "Menos pasos", v4, "Pedí solo lo necesario. <b>Cada paso de más es una excusa</b> para irse.", C[3]),
    ]
    html = pieza('Si te abandonan el carrito,<br><em>revisá estas 4 cosas</em>', "El cliente ya quería comprar. No le pongas trabas.",
                 tarjetas, "<b>¿Cuál de las 4 te falta en tu tienda?</b>")
    js = JS_UTIL + f"""
    function frame(t) {{
      const out = 1 - seg(t, .93, 1); fadeVis(out);
      // 1 · el envío aparece de golpe al final, después se corrige
      const sor = t > .2 && t < .55;
      set('en1', {{opacity: t > .2 ? 1 : 0, color: t < .55 ? '#c6321c' : '#1f2430'}});
      $('tt1').textContent = t > .2 ? '$25.000' : '$20.000';
      set('wo1', {{opacity: sor ? 1 : 0, transform:`rotate(${{sor ? Math.sin(t*90)*3 : 0}}deg)`}});
      set('ok1', {{opacity: seg(t, .58, .64)}});
      // 2
      for (let k = 0; k < 5; k++) set('pg'+k, {{opacity: seg(t, .06 + .09*k, .12 + .09*k), transform:`translateX(${{(1-ease(seg(t, .06 + .09*k, .14 + .09*k)))*-30}}px)`}});
      // 3 · tachar crear cuenta, tocar invitado
      const tach = t > .3;
      set('cr3', {{textDecoration: tach ? 'line-through' : 'none', color: tach ? '#9aa3b2' : '#1f2430'}});
      const on = t > .5; set('in3', {{background: on ? '{C[2]}' : '#9aa3b2', color: on ? '#0d0f14' : '#fff'}});
      const m = ease(seg(t, .32, .48)); set('cu5', {{left: mix(330, 300, m) + 'px', top: mix(170, 100, m) + 'px', opacity: out,
          transform:`scale(${{t > .48 && t < .52 ? .82 : 1}})`}});
      // 4 · seis pasos que se reducen a tres
      const n = t < .4 ? 6 : 3;
      $('pa4').innerHTML = Array.from({{length:n}}, (_, i) => `<span style="width:44px;height:44px;border-radius:50%;background:${{n===3?'{C[3]}':'#3a4258'}};`+
        `color:${{n===3?'#0d0f14':'#fff'}};font-size:21px;font-weight:800;display:flex;align-items:center;justify-content:center">${{i+1}}</span>`).join('');
      set('t4', {{opacity: seg(t, .44, .5)}}); pop('r4', seg(t, .5, .6));
    }}
    """
    render_anim(html, js, f"{OUT}/05_carrito_abandonado", portada_t=0.86)
