"""Banco de infografías animadas · tanda A (piezas 01 a 04). Ejecutar: python3 banco_A.py [01 02 03 04]  (OUT=carpeta opcional)

Cada pieza tiene su propia composición (regla de variedad, 17/11/2026). Todos los números son ejemplos.
"""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
from kit_animado import render_anim

OUT = os.environ.get("OUT", AQUI)
QUE = sys.argv[1:] or ["01", "02", "03", "04"]
KITF = os.path.join(os.path.dirname(os.path.dirname(AQUI)), "kit", "fonts")
ARCHIVO = "".join(f'@font-face{{font-family:Archivo;src:url("file://{KITF}/Archivo-{w}.ttf");font-weight:{w}}}'
                  for w in (500, 600, 700, 800))
JS_UTIL = """
const AR = n => Math.round(n).toLocaleString('es-AR');
const pop = (id, x) => set(id, {opacity: ease(cl(x)), transform:`scale(${.7 + .3*ease(cl(x))})`});
const fadeAll = out => document.querySelectorAll('#pz > *').forEach(e => e.style.opacity = out);
"""

# =====================================================================================
# 01 · Sumarle 50 % al costo no es ganar 50 % · PANTALLA DIVIDIDA blanco / negro, acento rojo
# =====================================================================================
if "01" in QUE:
    RJ = "#ff3b30"
    css = ARCHIVO + f"""
    #pz {{ padding:0 !important; background:linear-gradient(90deg,#ffffff 0 50%,#0b0b0c 50% 100%) !important; font-family:Inter,sans-serif; }}
    .dif {{ position:absolute; left:0; right:0; text-align:center; color:#fff; mix-blend-mode:difference; }}
    .t1 {{ top:64px; font:800 84px/1 Archivo; letter-spacing:-0.045em; }}
    .lado {{ position:absolute; top:300px; width:540px; text-align:center; }}
    .lado .k {{ font:800 24px Inter; letter-spacing:.16em; }}
    .lado .n {{ margin-top:6px; font:800 190px/1 Archivo; letter-spacing:-0.06em; position:relative; display:inline-block; }}
    .tacha {{ position:absolute; left:-10px; right:-10px; top:52%; height:16px; background:{RJ}; border-radius:8px; transform-origin:left center; transform:rotate(-8deg) scaleX(0); }}
    .col {{ position:absolute; width:240px; bottom:250px; display:flex; flex-direction:column-reverse; border-radius:14px; overflow:hidden; }}
    .col div {{ display:flex; flex-direction:column; align-items:center; justify-content:center; font:700 24px/1.2 Inter; text-align:center; overflow:hidden; }}
    .col div b {{ font:800 30px Inter; }}
    .cap {{ position:absolute; top:1112px; width:540px; text-align:center; font:600 25px/1.3 Inter; }}
    .cap b {{ font-weight:800; }}
    .fin {{ top:1192px; font:800 34px/1.2 Inter; letter-spacing:-0.01em; }}
    .fm {{ top:1286px; font:600 21px Inter; opacity:.8; }}
    """
    html = (f'<style>{css}</style><div id="pz">'
            f'<div class="dif t1" id="ti">Sumarle 50 % al costo<br>no es ganar 50 %</div>'
            f'<div class="lado" style="left:0;color:#0b0b0c"><div class="k" style="color:#777">LO QUE CREÉS</div>'
            f'<div class="n"><span id="nl">0 %</span><i class="tacha" id="tc"></i></div></div>'
            f'<div class="lado" style="left:540px;color:#fff"><div class="k" style="color:{RJ}">LO QUE GANÁS</div>'
            f'<div class="n" style="color:{RJ}"><span id="nr">0 %</span></div></div>'
            # columna izquierda: costo + 50 % sobre el costo
            f'<div class="col" style="left:150px"><div id="lc" style="height:0;background:#e6e6e6;color:#0b0b0c">Costo<b>$10.000</b></div>'
            f'<div id="lg" style="height:0;background:#ffd9d6;color:#b3140b">+50 % del costo<b>+$5.000</b></div></div>'
            # columna derecha: el mismo precio, visto como precio
            f'<div class="col" style="left:690px"><div id="rc" style="height:0;background:#2c2c30;color:#fff">Costo<b>$10.000</b></div>'
            f'<div id="rg" style="height:0;background:{RJ};color:#fff">Ganancia<b>$5.000</b></div></div>'
            f'<div class="cap" id="cl" style="left:0;color:#555"><b style="color:#0b0b0c">$5.000</b> sobre el costo de $10.000</div>'
            f'<div class="cap" id="cr" style="left:540px;color:#bbb"><b style="color:#fff">$5.000</b> sobre el precio de $15.000</div>'
            f'<div class="dif fin" id="fi">Para ganar el 50 % del precio, tenés que vender a $20.000.</div>'
            f'<div class="dif fm">Nicolás Benítez · números de ejemplo</div></div>')
    js = JS_UTIL + """
    const H = 30;                                   // px por cada $1.000
    function frame(t) {
      const out = 1 - seg(t, .95, 1); fadeAll(out);
      const a = ease(seg(t, .02, .1)); set('ti', {opacity: a*out, transform:`translateY(${(1-a)*-24}px)`});
      // izquierda: el costo y el 50 % que "creés"
      const lc = ease(seg(t, .1, .2)), lg = ease(seg(t, .2, .3));
      set('lc', {height: 10*H*lc + 'px'}); set('lg', {height: 5*H*lg + 'px'});
      $('nl').textContent = Math.round(50*lg) + ' %';
      set('cl', {opacity: seg(t, .28, .32)*out});
      // derecha: el mismo número mirado sobre el precio
      const rc = ease(seg(t, .34, .44)), rg = ease(seg(t, .44, .54));
      set('rc', {height: 10*H*rc + 'px'}); set('rg', {height: 5*H*rg + 'px'});
      $('nr').textContent = Math.round(33*rg) + ' %';
      set('cr', {opacity: seg(t, .52, .56)*out});
      // se tacha el 50 %
      const tc = ease(seg(t, .6, .66)); set('tc', {transform:`rotate(-8deg) scaleX(${tc})`});
      const f = ease(seg(t, .72, .8)); set('fi', {opacity: f*out, transform:`translateY(${(1-f)*16}px)`});
    }
    """
    render_anim(html, js, f"{OUT}/01_markup_vs_margen", segundos=7, portada_t=0.88)

# =====================================================================================
# 02 · Punto de equilibrio · VERDE PROFUNDO, termómetro gigante que se llena venta a venta
# =====================================================================================
if "02" in QUE:
    MENTA = "#5cf2a6"; RJ = "#ff6b5b"
    BASE, TOPE, MAXV = 1060, 170, 200            # el tubo va de y=1060 (0 ventas) a y=170 (200 ventas)
    PX = (BASE - TOPE) / MAXV                    # 4,45 px por venta
    Y150 = BASE - 150 * PX
    css = ARCHIVO + f"""
    #pz {{ padding:0 !important; background:radial-gradient(900px 900px at 80% 30%,#0f5a40 0%,#073826 60%,#052a1d 100%) !important;
          color:#fff; font-family:Inter,sans-serif; }}
    .t2 {{ position:absolute; left:70px; top:76px; font:800 76px/1 Archivo; letter-spacing:-0.045em; }}
    .t2 em {{ font-style:normal; color:{MENTA}; }}
    .bl {{ position:absolute; left:70px; width:560px; }}
    .bl .k {{ font:700 26px Inter; color:#a9d8c2; }}
    .bl .s {{ font:500 22px Inter; color:#7fb79f; margin-top:2px; }}
    .bl .v {{ font:800 76px/1.05 Archivo; letter-spacing:-0.04em; margin-top:6px; }}
    .eq {{ position:absolute; left:70px; top:830px; font:700 34px Inter; color:#cfeee0; }}
    .res {{ position:absolute; left:70px; top:878px; font:800 104px/1 Archivo; letter-spacing:-0.05em; color:{MENTA}; transform-origin:left center; }}
    .nt2 {{ position:absolute; left:70px; top:1010px; width:540px; font:600 28px/1.3 Inter; color:#cfeee0; }}
    .nota b {{ color:{MENTA}; }}
    .tubo {{ position:absolute; left:770px; top:{TOPE - 20}px; width:120px; height:{BASE - TOPE + 60}px; border-radius:60px; background:rgba(255,255,255,.08);
             border:5px solid rgba(255,255,255,.35); overflow:hidden; }}
    .liq {{ position:absolute; left:0; right:0; bottom:0; height:0; }}
    .bulbo {{ position:absolute; left:730px; top:{BASE - 10}px; width:200px; height:200px; border-radius:50%; border:5px solid rgba(255,255,255,.35);
              display:flex; flex-direction:column; align-items:center; justify-content:center; }}
    .bulbo b {{ font:800 64px/1 Archivo; letter-spacing:-0.04em; color:#06281b; }}
    .bulbo span {{ font:800 20px Inter; color:#06281b; letter-spacing:.06em; }}
    .marca {{ position:absolute; left:900px; font:600 22px Inter; color:#a9d8c2; }}
    .linea {{ position:absolute; left:680px; width:340px; top:{Y150}px; border-top:4px dashed #fff; }}
    .pe {{ position:absolute; left:300px; top:{Y150 - 40}px; width:450px; text-align:right; font:800 24px Inter; }}
    .zona {{ position:absolute; left:905px; width:160px; text-align:left; font:800 22px Inter; letter-spacing:.08em; }}
    .fm {{ position:absolute; left:70px; bottom:42px; font:600 22px Inter; color:#7fb79f; }}
    """
    marcas = "".join(f'<div class="marca" style="top:{BASE - v * PX - 14}px">{v}</div>' for v in (0, 50, 100, 200))
    html = (f'<style>{css}</style><div id="pz">'
            f'<div class="t2" id="ti">¿Cuántas ventas<br>necesitás para<br><em>no perder plata?</em></div>'
            f'<div class="bl" id="b1" style="top:400px"><div class="k">Gastos fijos del mes</div><div class="s">alquiler, sueldos, sistemas</div>'
            f'<div class="v">$600.000</div></div>'
            f'<div class="bl" id="b2" style="top:610px"><div class="k">Lo que ganás por cada venta</div><div class="v">$4.000</div></div>'
            f'<div class="eq" id="eq">$600.000 ÷ $4.000 =</div><div class="res" id="rs">150 ventas</div>'
            f'<div class="nt2" id="nt">Desde la venta 151, <b>empezás a ganar.</b></div>'
            f'<div class="tubo"><div class="liq" id="lq"></div></div>'
            f'<div class="bulbo" id="bu"><b id="cn">0</b><span>VENTAS</span></div>{marcas}'
            f'<div class="linea" id="ln"></div><div class="pe" id="pe">Punto de equilibrio: 150</div>'
            f'<div class="zona" id="zg" style="top:{TOPE + 100}px;color:{MENTA}">GANANCIA</div>'
            f'<div class="zona" id="zp" style="top:{BASE - 330}px;color:{RJ}">PÉRDIDA</div>'
            f'<div class="fm">Nicolás Benítez · números de ejemplo</div></div>')
    js = JS_UTIL + f"""
    const PX = {PX}, MENTA = '{MENTA}', RJ = '{RJ}';
    function frame(t) {{
      const out = 1 - seg(t, .95, 1); fadeAll(out);
      const a = ease(seg(t, .02, .1)); set('ti', {{opacity: a*out, transform:`translateY(${{(1-a)*-20}}px)`}});
      set('b1', {{opacity: seg(t, .08, .14)*out}}); set('b2', {{opacity: seg(t, .16, .22)*out}});
      set('eq', {{opacity: seg(t, .24, .3)*out}});
      // el líquido sube hasta 150 (rojo), frena, y sigue hasta 185 (verde)
      let v = 150 * ease(seg(t, .1, .55));
      if (t > .66) v = 150 + 35 * ease(seg(t, .66, .8));
      const gana = v > 150.5;
      set('lq', {{height: (v * PX + 30) + 'px', background: gana ? `linear-gradient(0deg, ${{RJ}} 0 ${{(150*PX+30)/(v*PX+30)*100}}%, ${{MENTA}} 0)` : RJ}});
      set('bu', {{background: gana || v >= 149.5 ? MENTA : RJ}});
      $('cn').textContent = Math.round(v);
      const pe = t > .55 && t < .66;
      set('ln', {{borderTopColor: pe ? MENTA : '#fff', opacity: seg(t, .05, .1)*out}});
      set('pe', {{opacity: seg(t, .05, .1)*out, color: pe || gana ? MENTA : '#fff', transform:`scale(${{pe ? 1.06 : 1}})`}});
      set('zp', {{opacity: seg(t, .05, .1)*out}}); set('zg', {{opacity: seg(t, .05, .1)*out}});
      const r = seg(t, .55, .63); set('rs', {{opacity: ease(r)*out, transform:`scale(${{.8 + .2*ease(r)}})`}});
      set('nt', {{opacity: seg(t, .72, .78)*out}});
    }}
    """
    render_anim(html, js, f"{OUT}/02_punto_de_equilibrio", segundos=7, portada_t=0.88)

# =====================================================================================
# 03 · ¿Cuánto te queda de una venta? · CASCADA estilo periodismo de datos, fondo blanco, azul rey
# =====================================================================================
if "03" in QUE:
    AZ = "#1d4ed8"; NAR = "#f97316"; TINTA = "#111318"
    BASEY, K = 1080, 0.034                         # $1 = 0,034 px  -> $20.000 = 680 px
    X0, SLOT, ANCHO = 170, 145, 108
    PASOS = [("Precio", 20000, 0, 20000, "$20.000"),
             ("Producto", 10000, 10000, 20000, "−$10.000"),
             ("Comisión<br>(10 %)", 8000, 8000, 10000, "−$2.000"),
             ("Envío que<br>bonificás", 5000, 5000, 8000, "−$3.000"),
             ("Publicidad", 2500, 2500, 5000, "−$2.500"),
             ("Te queda", 2500, 0, 2500, "$2.500")]
    css = ARCHIVO + f"""
    #pz {{ padding:0 !important; background:#ffffff !important; color:{TINTA}; font-family:Inter,sans-serif; }}
    .t3 {{ position:absolute; left:70px; top:70px; font:800 80px/1 Archivo; letter-spacing:-0.045em; }}
    .t3 em {{ font-style:normal; color:{AZ}; }}
    .s3 {{ position:absolute; left:72px; top:258px; font:600 26px Inter; color:#666b75; }}
    .grid {{ position:absolute; left:70px; right:70px; height:0; border-top:2px solid #e8eaee; }}
    .eje {{ position:absolute; left:70px; font:600 20px Inter; color:#9aa0aa; }}
    .base {{ position:absolute; left:70px; right:70px; top:{BASEY}px; border-top:3px solid {TINTA}; }}
    .bar {{ position:absolute; width:{ANCHO}px; border-radius:6px 6px 0 0; }}
    .val {{ position:absolute; width:{SLOT}px; text-align:center; font:800 24px Inter; white-space:nowrap; }}
    .lab {{ position:absolute; top:{BASEY + 14}px; width:{SLOT}px; text-align:center; font:700 21px/1.2 Inter; color:#4b505a; }}
    .con {{ position:absolute; height:0; border-top:2px dashed #b7bcc6; }}
    .call {{ position:absolute; left:620px; top:380px; width:390px; font:700 30px/1.25 Inter; }}
    .call b {{ color:{NAR}; font:800 64px/1 Archivo; letter-spacing:-0.04em; display:block; margin-bottom:8px; }}
    .pie {{ position:absolute; left:70px; right:70px; bottom:40px; display:flex; justify-content:space-between; font:600 21px Inter; color:#8a909a;
            border-top:2px solid #e8eaee; padding-top:16px; }}
    """
    y = lambda v: BASEY - v * K
    grid = "".join(f'<div class="grid" style="top:{y(v)}px"></div><div class="eje" style="top:{y(v) - 28}px">${v // 1000} mil</div>'
                   for v in (5000, 10000, 15000, 20000))
    barras = ""
    for i, (lab, fin, lo, hi, txt) in enumerate(PASOS):
        x = X0 + SLOT * i
        color = AZ if i == 0 else (NAR if i == 5 else "#9db4f0")
        barras += (f'<div class="bar" id="br{i}" style="left:{x + (SLOT - ANCHO) / 2}px;top:{y(hi)}px;height:0;background:{color}"></div>'
                   f'<div class="val" id="vl{i}" style="left:{x}px;top:{y(hi) - 36}px;color:{NAR if i == 5 else TINTA}">{txt}</div>'
                   f'<div class="lab" style="left:{x}px">{lab}</div>')
        if 0 < i < 5:
            barras += f'<div class="con" id="cn{i}" style="left:{x - SLOT + (SLOT + ANCHO) / 2}px;width:0;top:{y(hi)}px"></div>'
    html = (f'<style>{css}</style><div id="pz"><div class="t3" id="ti">Vendiste a $20.000.<br><em>¿Cuánto te queda?</em></div>'
            f'<div class="s3">Todo lo que se descuenta de una venta online.</div>{grid}<div class="base"></div>{barras}'
            f'<div class="call" id="ca"><b>$2.500</b>Te queda el 12,5 % de lo que cobraste.</div>'
            f'<div class="pie"><span>Números de ejemplo</span><span>Nicolás Benítez</span></div></div>')
    pasos_js = [[lo, hi] for (_, _, lo, hi, _) in PASOS]
    js = JS_UTIL + f"""
    const P = {pasos_js!r}, K = {K}, SLOT = {SLOT}, ANCHO = {ANCHO};
    function frame(t) {{
      const out = 1 - seg(t, .95, 1); fadeAll(out);
      const a = ease(seg(t, .02, .1)); set('ti', {{opacity: a*out, transform:`translateY(${{(1-a)*-20}}px)`}});
      for (let i = 0; i < 6; i++) {{
        const s = .1 + .11*i, g = ease(seg(t, s, s + .08));
        const h = (P[i][1] - P[i][0]) * K;
        set('br'+i, {{height: h*g + 'px'}});                     // la barra baja desde el nivel anterior
        set('vl'+i, {{opacity: seg(t, s + .05, s + .09)*out}});
        if (i > 0 && i < 5) set('cn'+i, {{width: (SLOT - ANCHO) * ease(seg(t, s - .03, s)) + 'px'}});
      }}
      const c = ease(seg(t, .8, .87)); set('ca', {{opacity: c*out, transform:`translateY(${{(1-c)*16}}px)`}});
    }}
    """
    render_anim(html, js, f"{OUT}/03_cuanto_te_queda", segundos=8, portada_t=0.9)

# =====================================================================================
# 04 · Un cliente que vuelve vale más · TEAL oscuro, anillo con 3 vueltas (compras) y total en el centro
# =====================================================================================
if "04" in QUE:
    import math
    AC = "#5eead4"; AM = "#ffd166"
    CX, CY, R = 540, 700, 280
    nodos = []
    for k, a in enumerate((120, 240, 360)):
        rad = math.radians(a)
        nodos.append((CX + R * math.sin(rad), CY - R * math.cos(rad)))
    css = ARCHIVO + f"""
    #pz {{ padding:0 !important; background:radial-gradient(800px 700px at 50% 52%,#0f4b4f 0%,#0a3135 60%,#072326 100%) !important;
          color:#fff; font-family:Inter,sans-serif; }}
    .t4 {{ position:absolute; left:0; right:0; top:70px; text-align:center; font:800 72px/1.02 'Inter Display',Inter; letter-spacing:-0.04em; }}
    .t4 em {{ font-style:normal; color:{AC}; }}
    .nodo {{ position:absolute; width:44px; height:44px; margin:-22px 0 0 -22px; border-radius:50%; background:#0a3135; border:6px solid #2f6669; }}
    .et {{ position:absolute; font:700 26px/1.2 Inter; color:#9fd3cd; }}
    .et b {{ display:block; font:800 32px Inter; color:#fff; }}
    .cen {{ position:absolute; left:{CX - 230}px; top:{CY - 110}px; width:460px; text-align:center; }}
    .cen .k {{ font:700 26px Inter; color:#9fd3cd; letter-spacing:.04em; }}
    .cen .v {{ font:800 112px/1.05 Archivo; letter-spacing:-0.05em; }}
    .cen .s {{ font:600 26px Inter; color:#9fd3cd; }}
    .cmp {{ position:absolute; left:70px; right:70px; top:1050px; display:flex; flex-direction:column; gap:14px; }}
    .cmp div {{ display:flex; justify-content:space-between; align-items:center; padding:18px 24px; border-radius:18px; background:rgba(255,255,255,.06);
                font:600 26px Inter; color:#cfe9e6; }}
    .cmp div b {{ font:800 30px Inter; color:#fff; white-space:nowrap; }}
    .cmp div.ok {{ background:rgba(94,234,212,.14); border:2px solid {AC}; }}
    .cmp div.ok b {{ color:{AC}; }}
    .fm {{ position:absolute; left:70px; right:70px; bottom:36px; text-align:center; font:600 21px Inter; color:#7fb2ad; }}
    """
    circ = 2 * math.pi * R
    etiquetas = [(nodos[0][0] + 44, nodos[0][1] - 20, "left"), (nodos[1][0] - 44, nodos[1][1] - 20, "right"),
                 (CX, nodos[2][1] - 118, "center")]
    et_html = ""
    for k, (x, yv, al) in enumerate(etiquetas):
        pos = (f"left:{x}px" if al == "left" else (f"right:{1080 - x}px" if al == "right" else f"left:{x - 150}px;width:300px"))
        et_html += f'<div class="et" id="et{k}" style="{pos};top:{yv}px;text-align:{al}">Compra {k + 1}<b>$30.000</b></div>'
    html = (f'<style>{css}</style><div id="pz"><div class="t4" id="ti">Un cliente que vuelve<br><em>vale más que uno nuevo</em></div>'
            f'<svg style="position:absolute;left:0;top:0" width="1080" height="1350">'
            f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="rgba(255,255,255,.1)" stroke-width="26"/>'
            f'<circle id="arc" cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="{AC}" stroke-width="26" stroke-linecap="round" '
            f'stroke-dasharray="{circ}" stroke-dashoffset="{circ}" transform="rotate(-90 {CX} {CY})"/></svg>'
            + "".join(f'<div class="nodo" id="nd{k}" style="left:{x}px;top:{yv}px"></div>' for k, (x, yv) in enumerate(nodos))
            + et_html
            + f'<div class="cen"><div class="k">EN UN AÑO</div><div class="v" id="tot">$0</div><div class="s" id="sb">Ticket de $30.000</div></div>'
            f'<div class="cmp"><div id="c1">Si compra 1 vez: $9.000 de publicidad para <b>$30.000 (30 %)</b></div>'
            f'<div class="ok" id="c3">Si compra 3 veces: los mismos $9.000 para <b>$90.000 (10 %)</b></div></div>'
            f'<div class="fm">Nicolás Benítez · números de ejemplo</div></div>')
    js = JS_UTIL + f"""
    const CIRC = {circ};
    function frame(t) {{
      const out = 1 - seg(t, .95, 1); fadeAll(out);
      const a = ease(seg(t, .02, .1)); set('ti', {{opacity: a*out, transform:`translateY(${{(1-a)*-20}}px)`}});
      let p = 0, tot = 0;
      for (let k = 0; k < 3; k++) {{
        const s = .12 + .2*k, g = ease(seg(t, s, s + .16));
        p += g / 3; tot += 30000 * g;
        const on = g >= 1;
        set('nd'+k, {{background: on ? '{AM}' : '#0a3135', borderColor: on ? '{AM}' : '#2f6669', transform:`scale(${{on && t < s + .2 ? 1.25 : 1}})`}});
        set('et'+k, {{opacity: (on ? 1 : .35) * out}});
      }}
      $('arc').setAttribute('stroke-dashoffset', CIRC * (1 - p));
      $('tot').textContent = '$' + AR(tot);
      set('tot', {{color: tot >= 89999 ? '{AM}' : '#fff'}});
      set('c1', {{opacity: seg(t, .78, .82)*out}});
      const c3 = ease(seg(t, .84, .88)); set('c3', {{opacity: c3*out, transform:`translateY(${{(1-c3)*14}}px)`}});
    }}
    """
    render_anim(html, js, f"{OUT}/04_cliente_que_vuelve", segundos=8, portada_t=0.93)
