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
# Desde acá, cada pieza tiene su propia composición (pedido de Nicolás, 17/11/2026: "no parezcan una
# plantilla reusada"). Fondo, paleta, tipografía y estructura cambian en cada una.
# =====================================================================================
KITF = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(AQUI))), "linkedin", "kit", "fonts")
ARCHIVO = "".join(f'@font-face{{font-family:Archivo;src:url("file://{KITF}/Archivo-{w}.ttf");font-weight:{w}}}' for w in (500, 600, 700, 800))
CARRO = ('<svg viewBox="0 0 48 40" width="{w}" height="{h}"><path d="M3 5h7l6 22h22l5-15H13" fill="none" stroke="{c}" stroke-width="4.5" '
         'stroke-linecap="round" stroke-linejoin="round"/><circle cx="19" cy="34" r="3.8" fill="{c}"/><circle cx="35" cy="34" r="3.8" fill="{c}"/></svg>')
BOLSA = ('<svg viewBox="0 0 30 36" width="{w}" height="{h}"><path d="M9 11V8a6 6 0 0 1 12 0v3" fill="none" stroke="{c}" stroke-width="3"/>'
         '<rect x="3" y="11" width="24" height="23" rx="4" fill="{c}"/></svg>')

# -------------------------------------------------------------------------------------
# 03 · CREMA + VIOLETA · lista editorial de 4 filas con "el pedido" de cada tarea
# -------------------------------------------------------------------------------------
if "03" in QUE:
    V = "#6d28d9"; TINTA = "#17131f"
    css = ARCHIVO + f"""
    #pz {{ padding:0 !important; background:#f3eee4 !important; color:{TINTA}; font-family:Inter,sans-serif; }}
    .tag {{ position:absolute; left:72px; top:62px; font:800 22px Inter; letter-spacing:.14em; color:{V}; background:#e9e0ff; padding:10px 18px; border-radius:99px; }}
    .t3 {{ position:absolute; left:72px; top:124px; font:800 86px/0.98 Archivo; letter-spacing:-0.035em; }}
    .t3 .mk {{ background:linear-gradient({V},{V}) no-repeat 0 88%/var(--m,0%) 34%; padding:0 6px; color:{TINTA}; }}
    .s3 {{ position:absolute; left:72px; top:330px; font:600 30px Inter; color:#5b5566; }}
    .s3 b {{ color:{TINTA}; }}
    .fila {{ position:absolute; left:72px; right:72px; height:196px; border-top:2px solid #ddd3c2; display:flex; align-items:center; gap:28px; }}
    .fila .num {{ font:800 92px Archivo; letter-spacing:-0.04em; color:transparent; -webkit-text-stroke:2.5px #b9add0; width:120px; flex:none; }}
    .fila.on .num {{ color:{V}; -webkit-text-stroke:0; }}
    .fila .tx {{ flex:1; }}
    .fila h4 {{ font:800 36px Archivo; letter-spacing:-0.02em; }}
    .fila .pd {{ margin-top:10px; font:600 23px/1.3 Inter; color:#5b5566; }}
    .fila.on .pd {{ color:{V}; }}
    .fila .mv {{ position:relative; width:300px; height:150px; flex:none; border-radius:20px; background:#fff; box-shadow:0 12px 30px rgba(40,20,80,.12); overflow:hidden; }}
    .pie3 {{ position:absolute; left:72px; right:72px; bottom:44px; display:flex; justify-content:space-between; align-items:center; font:700 25px Inter; }}
    .pie3 .yo {{ display:flex; align-items:center; gap:14px; }}
    .pie3 .yo i {{ width:48px; height:48px; border-radius:50%; background:{V}; color:#fff; font:800 18px Inter; font-style:normal; display:flex; align-items:center; justify-content:center; }}
    .pie3 span.r {{ color:#5b5566; font-weight:600; }}
    .chip {{ display:inline-block; margin:0 6px 6px 0; padding:5px 10px; border-radius:8px; background:#efe9ff; color:{V}; font:700 17px Inter; }}
    .bb {{ position:absolute; border-radius:14px; padding:8px 11px; font:600 17px/1.28 Inter; }}
    """
    filas = [
        ("Descripciones de producto", "“Con estos datos, escribí la descripción para mi tienda.”"),
        ("Respuestas a clientes", "“Con mis condiciones de envío, respondé esta pregunta.”"),
        ("Quejas en las reseñas", "“¿Cuáles son las 3 quejas que más se repiten?”"),
        ("Asuntos para tus mails", "“Dame 10 asuntos para este mail de promo.”"),
    ]
    mv = [
        '<div style="position:absolute;left:14px;top:12px;right:14px">' + "".join(f'<span class="chip" id="c3{k}">{t}</span>' for k, t in enumerate(["Aluminio", "Negro", "30 cm"]))
        + '</div><div id="d3" style="position:absolute;left:14px;right:14px;top:58px;font:600 17px/1.3 Inter;color:#17131f"></div>',
        '<div class="bb" id="q3" style="left:12px;top:12px;background:#efeaf5;border-radius:14px 14px 14px 4px">¿Envían al interior?</div>'
        '<div class="bb" id="a3" style="right:12px;top:62px;left:52px;background:#6d28d9;color:#fff;border-radius:14px 14px 4px 14px"></div>',
        "".join(f'<div style="position:absolute;left:14px;top:{16 + 44 * k}px;font:700 16px Inter;color:#5b5566">{t}</div>'
                f'<div style="position:absolute;left:14px;right:14px;top:{36 + 44 * k}px;height:10px;border-radius:5px;background:#efe9ff">'
                f'<div id="g3{k}" data-w="{w}" style="height:100%;width:0;border-radius:5px;background:#6d28d9"></div></div>'
                for k, (t, w) in enumerate([("Demora en el envío", 100), ("Talle más chico", 60), ("Embalaje roto", 32)])),
        "".join(f'<div id="s3{k}" style="position:absolute;left:12px;right:12px;top:{12 + 44 * k}px;height:36px;border-radius:9px;background:#f6f3fb;'
                f'display:flex;align-items:center;gap:8px;padding:0 10px;font:700 16px Inter;color:#17131f;white-space:nowrap;overflow:hidden">'
                f'<span style="flex:none">{SOBRE.format(w=20, h=15, c=V)}</span><span id="st{k}"></span></div>' for k in range(3)),
    ]
    cuerpo = "".join(f'<div class="fila" id="fi{k}" style="top:{400 + 196 * k}px"><div class="num">0{k + 1}</div>'
                     f'<div class="tx"><h4>{t}</h4><div class="pd">{p}</div></div><div class="mv">{mv[k]}</div></div>'
                     for k, (t, p) in enumerate(filas))
    html = (f'<style>{css}</style><div id="pz"><div class="tag">IA PARA TU TIENDA ONLINE</div>'
            f'<div class="t3">4 tareas que podés<br>pasarle a la IA <span class="mk" id="mk">hoy</span></div>'
            f'<div class="s3">Copiá el pedido y pegalo en <b>ChatGPT o Claude</b>. Son gratis.</div>{cuerpo}'
            f'<div class="pie3"><div class="yo"><i>NB</i>Nicolás Benítez</div><span class="r">Siempre revisá antes de publicar.</span></div></div>')
    DESC = "Lámpara colgante de aluminio negro, 30 cm. Ideal para la cocina."
    RESP = "¡Sí! Enviamos a todo el país en 3 a 5 días hábiles."
    AS = ["Tu carrito te está esperando", "Últimas 24 h de envío gratis", "Volvió lo que buscabas"]
    js = JS_UTIL + f"""
    const DESC={DESC!r}, RESP={RESP!r}, AS={AS!r};
    function frame(t) {{
      const out = 1 - seg(t, .95, 1);
      $('mk').style.setProperty('--m', 100*ease(seg(t, .02, .1)) + '%');
      const W = .2;                                     // cada fila tiene su turno
      for (let k = 0; k < 4; k++) {{
        const a = .1 + W*k, on = t >= a && t < a + W;
        $('fi'+k).classList.toggle('on', on);
        set('fi'+k, {{opacity: (t < a ? .45 : 1) * out}});
      }}
      for (let k = 0; k < 3; k++) pop('c3'+k, seg(t, .1 + .03*k, .13 + .03*k));
      $('d3').textContent = typed(DESC, seg(t, .2, .3));
      pop('q3', seg(t, .3, .34)); set('a3', {{opacity: seg(t, .36, .38)}}); $('a3').textContent = typed(RESP, seg(t, .38, .5)) || ' ';
      for (let k = 0; k < 3; k++) {{ const e = $('g3'+k); e.style.width = e.dataset.w * ease(seg(t, .52 + .04*k, .62 + .04*k)) + '%'; }}
      for (let k = 0; k < 3; k++) {{ set('s3'+k, {{opacity: seg(t, .7 + .06*k, .72 + .06*k)}}); $('st'+k).textContent = typed(AS[k], seg(t, .72 + .06*k, .76 + .06*k)); }}
    }}
    """
    render_anim(html, js, f"{OUT}/03_ia_tareas_tienda_online_v2", segundos=8, portada_t=0.9)

# -------------------------------------------------------------------------------------
# 04 · AMARILLO + NEGRO · una sola cuenta gigante (sin tarjetas)
# -------------------------------------------------------------------------------------
if "04" in QUE:
    AM = "#ffd43b"; NG = "#111111"; RJ = "#e8340c"
    css = ARCHIVO + f"""
    #pz {{ padding:0 !important; background:{AM} !important; color:{NG}; font-family:Inter,sans-serif; }}
    .big {{ position:absolute; left:62px; top:46px; font:800 196px/0.9 Archivo; letter-spacing:-0.06em; white-space:nowrap; }}
    .big .st {{ position:relative; }}
    .sub {{ position:absolute; left:70px; top:262px; font:700 40px/1.15 Inter; letter-spacing:-0.02em; }}
    .lab {{ position:absolute; font:800 28px Inter; }}
    .barra {{ position:absolute; left:70px; top:470px; height:130px; display:flex; border-radius:18px; overflow:hidden; border:4px solid {NG}; }}
    .barra div {{ height:100%; display:flex; align-items:center; justify-content:center; font:800 30px Inter; white-space:nowrap; overflow:hidden; }}
    .menos {{ position:absolute; font:800 120px Archivo; letter-spacing:-0.05em; color:{RJ}; }}
    .regla {{ position:absolute; left:70px; right:70px; top:760px; height:4px; background:{NG}; }}
    .fila4 {{ position:absolute; left:70px; right:70px; display:flex; flex-wrap:wrap; gap:8px; }}
    .cap {{ position:absolute; left:70px; font:700 26px Inter; }}
    .final {{ position:absolute; left:70px; right:70px; top:1120px; font:800 64px/1 Archivo; letter-spacing:-0.035em; }}
    .final em {{ font-style:normal; background:{NG}; color:{AM}; padding:0 14px; border-radius:10px; }}
    .pie4 {{ position:absolute; left:70px; right:70px; bottom:42px; display:flex; justify-content:space-between; font:700 24px Inter; }}
    """
    html = (f'<style>{css}</style><div id="pz">'
            f'<div class="big" id="big">¿20 % off?</div>'
            f'<div class="sub">Antes de lanzar la promo,<br>hacé esta cuenta.</div>'
            f'<div class="lab" style="left:70px;top:420px" id="pl">Precio $10.000</div>'
            f'<div class="barra" id="ba"><div id="co" style="width:546px;background:{NG};color:{AM}">Costo $6.000</div>'
            f'<div id="ga" style="width:364px;background:#fff;color:{NG}">Ganás $4.000</div></div>'
            f'<div class="lab" style="left:70px;top:620px;font-weight:600" id="cn">El costo no baja con el descuento.</div>'
            f'<div class="menos" id="me" style="left:690px;top:590px">−50 %<div style="font:800 28px Inter;letter-spacing:0;color:#111;margin-top:-6px;text-align:right">de tu ganancia</div></div>'
            f'<div class="regla"></div>'
            f'<div class="cap" style="top:790px">Para ganar $40.000:</div>'
            f'<div class="cap" style="top:850px;font-weight:600">Sin descuento · 10 ventas</div>'
            f'<div class="fila4" style="top:892px">' + "".join(f'<span id="x{k}">{BOLSA.format(w=36, h=44, c=NG)}</span>' for k in range(10)) + '</div>'
            f'<div class="cap" style="top:968px;font-weight:600">Con 20 % off · 20 ventas</div>'
            f'<div class="fila4" style="top:1010px">' + "".join(f'<span id="y{k}">{BOLSA.format(w=36, h=44, c=RJ)}</span>' for k in range(20)) + '</div>'
            f'<div class="final" id="fi">Tenés que vender <em>el doble</em>.</div>'
            f'<div class="pie4"><span>Nicolás Benítez</span><span style="font-weight:600">Ejemplo con un margen del 40 %</span></div></div>')
    js = JS_UTIL + f"""
    function frame(t) {{
      const out = 1 - seg(t, .95, 1);
      set('pz', {{opacity: 1}});
      document.querySelectorAll('#pz > *').forEach(e => e.style.opacity = out);
      const b = ease(seg(t, .03, .12)); set('big', {{transform:`translateY(${{(1-b)*-30}}px)`, opacity: b*out}});
      // la barra: precio 10.000 -> 8.000 (se achica solo la ganancia)
      const d = ease(seg(t, .2, .36));
      set('ga', {{width: (364 - 182*d) + 'px', background: d > .5 ? '{RJ}' : '#fff', color: d > .5 ? '#fff' : '{NG}'}});
      $('ga').textContent = d > .5 ? '$2.000' : 'Ganás $4.000';
      $('pl').textContent = d > .5 ? 'Precio con 20 % off: $8.000' : 'Precio $10.000';
      set('cn', {{opacity: seg(t, .36, .42) * out}});
      pop('me', seg(t, .4, .48)); set('me', {{opacity: ease(seg(t, .4, .48)) * out}});
      for (let k = 0; k < 10; k++) {{ const x = seg(t, .5 + .01*k, .53 + .01*k); set('x'+k, {{opacity: x*out, transform:`translateY(${{(1-ease(x))*-20}}px)`}}); }}
      for (let k = 0; k < 20; k++) {{ const x = seg(t, .62 + .01*k, .65 + .01*k); set('y'+k, {{opacity: x*out, transform:`translateY(${{(1-ease(x))*-20}}px)`}}); }}
      const f = ease(seg(t, .84, .9)); set('fi', {{opacity: f*out, transform:`translateY(${{(1-f)*20}}px)`}});
    }}
    """
    render_anim(html, js, f"{OUT}/04_descuento_conviene_v2", segundos=7, portada_t=0.93)

# -------------------------------------------------------------------------------------
# 05 · VIOLETA PROFUNDO + NARANJA · el recorrido del carrito, con 4 trabas que se destraban
# -------------------------------------------------------------------------------------
if "05" in QUE:
    NA = "#ff7a1a"; VE = "#2ee59d"; RO = "#ff4d6d"
    css = f"""
    #pz {{ padding:0 !important; background:linear-gradient(170deg,#24103f 0%,#120822 70%) !important; color:#fff; font-family:Inter,sans-serif; }}
    .t5 {{ position:absolute; left:72px; top:66px; font:800 74px/1.02 'Inter Display',Inter; letter-spacing:-0.04em; }}
    .t5 em {{ font-style:normal; color:{NA}; }}
    .s5 {{ position:absolute; left:72px; top:250px; font:600 28px Inter; color:#c9b8e6; }}
    .via {{ position:absolute; left:128px; top:360px; width:6px; height:800px; background:repeating-linear-gradient(#5a3d85 0 16px, transparent 16px 30px); border-radius:3px; }}
    .via i {{ position:absolute; left:0; top:0; width:6px; background:{NA}; border-radius:3px; }}
    .pt {{ position:absolute; left:112px; width:38px; height:38px; border-radius:50%; background:#2b1a48; border:4px solid #5a3d85; }}
    .tr {{ position:absolute; left:200px; right:64px; height:150px; border-radius:24px; background:rgba(255,255,255,.06); border:2px solid rgba(255,255,255,.12);
          padding:22px 28px; overflow:hidden; }}
    .tr .mal, .tr .bien {{ position:absolute; left:28px; right:28px; top:22px; }}
    .tr .k {{ font:800 20px Inter; letter-spacing:.12em; }}
    .tr .x {{ margin-top:8px; font:700 34px/1.15 Inter; letter-spacing:-0.02em; }}
    .tr .mal .k {{ color:{RO}; }} .tr .bien .k {{ color:{VE}; }}
    .tr .mal .x {{ text-decoration-thickness:4px; text-decoration-color:{RO}; }}
    .carro {{ position:absolute; left:90px; width:84px; height:70px; display:flex; align-items:center; justify-content:center;
             background:{NA}; border-radius:20px; box-shadow:0 10px 30px rgba(255,122,26,.45); z-index:3; }}
    .fin {{ position:absolute; left:200px; top:1176px; font:800 34px Inter; color:{VE}; }}
    .pie5 {{ position:absolute; left:72px; right:72px; bottom:40px; display:flex; justify-content:space-between; font:700 24px Inter; color:#c9b8e6; }}
    .pie5 b {{ color:#fff; }}
    """
    TRABAS = [("El envío aparece recién al pagar", "Mostralo desde el producto"),
              ("Un solo medio de pago", "Tarjeta, transferencia, billetera y cuotas"),
              ("Te obliga a crear una cuenta", "Dejá comprar como invitado"),
              ("Un formulario de 6 pasos", "Datos, envío y pago. Listo.")]
    tops = [370 + 190 * k for k in range(4)]
    tr = "".join(f'<div class="pt" id="pt{k}" style="top:{tp + 56}px"></div>'
                 f'<div class="tr" id="tr{k}" style="top:{tp}px"><div class="mal" id="ml{k}"><div class="k">✕ TRABA</div><div class="x">{a}</div></div>'
                 f'<div class="bien" id="bn{k}"><div class="k">✓ SOLUCIÓN</div><div class="x">{b}</div></div></div>'
                 for k, (tp, (a, b)) in enumerate(zip(tops, TRABAS)))
    html = (f'<style>{css}</style><div id="pz"><div class="t5">Llegó hasta el carrito.<br><em>¿Por qué no pagó?</em></div>'
            f'<div class="s5">4 trabas que espantan al cliente en el último paso.</div>'
            f'<div class="via"><i id="vi"></i></div>{tr}'
            f'<div class="carro" id="ca">{CARRO.format(w=52, h=44, c="#1a0b2e")}</div>'
            f'<div class="fin" id="fn">✓ Compra hecha</div>'
            f'<div class="pie5"><span><b>Nicolás Benítez</b></span><span>¿Cuál te falta revisar en tu tienda?</span></div></div>')
    js = JS_UTIL + f"""
    const TOPS = {tops!r};
    function frame(t) {{
      const out = 1 - seg(t, .95, 1);
      document.querySelectorAll('#pz > *').forEach(e => e.style.opacity = out);
      // el carrito baja por el camino y frena en cada traba (paradas de .16)
      let y = 300, prog = 0;
      for (let k = 0; k < 4; k++) {{
        const a = .06 + .2*k;                           // llega a la traba k
        const ida = ease(seg(t, a - .06, a));
        if (t >= a - .06) y = mix(k ? TOPS[k-1] + 40 : 300, TOPS[k] + 40, ida);
        const fixed = t > a + .07;
        set('ml'+k, {{opacity: t < a ? .5 : (fixed ? 0 : 1), textDecoration: t > a + .03 && !fixed ? 'line-through' : 'none'}});
        $('ml'+k).querySelector('.x').style.textDecorationLine = t > a + .03 && !fixed ? 'line-through' : 'none';
        const fb = ease(seg(t, a + .07, a + .11));
        set('bn'+k, {{opacity: fb, transform:`translateY(${{(1-fb)*24}}px)`}});
        set('tr'+k, {{borderColor: fixed ? 'rgba(46,229,157,.6)' : (t >= a ? 'rgba(255,77,109,.7)' : 'rgba(255,255,255,.12)'),
                       background: fixed ? 'rgba(46,229,157,.08)' : 'rgba(255,255,255,.06)'}});
        set('pt'+k, {{background: fixed ? '{VE}' : '#2b1a48', borderColor: fixed ? '{VE}' : '#5a3d85'}});
      }}
      const ult = ease(seg(t, .84, .9)); if (t > .84) y = mix(TOPS[3] + 40, 1150, ult);
      set('ca', {{top: y + 'px', transform:`rotate(${{Math.sin(t*120)*(t%.2 < .06 ? 4 : 0)}}deg)`}});
      $('vi').style.height = cl((y - 340) / 800) * 800 + 'px';
      set('fn', {{opacity: seg(t, .88, .92) * out}});
    }}
    """
    render_anim(html, js, f"{OUT}/05_carrito_abandonado_v2", segundos=8, portada_t=0.92)
