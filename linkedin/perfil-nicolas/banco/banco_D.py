"""Banco de infografías animadas · tanda D (piezas 13 a 16). Ejecutar: python3 banco_D.py [13 14 15 16]
Cada pieza tiene su propia composición, fondo y paleta (regla de variedad, 17/11/2026)."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
from kit_animado import render_anim, CURSOR

OUT = os.environ.get("OUT", AQUI)
QUE = sys.argv[1:] or ["13", "14", "15", "16"]
KITF = os.path.join(os.path.dirname(os.path.dirname(AQUI)), "kit", "fonts")
ARCHIVO = "".join(f'@font-face{{font-family:Archivo;src:url("file://{KITF}/Archivo-{w}.ttf");font-weight:{w}}}' for w in (500, 600, 700, 800))
JS_UTIL = """
const AR = n => Math.round(n).toLocaleString('es-AR');
const pop = (id, x) => set(id, {opacity: ease(cl(x)), transform:`scale(${.7 + .3*ease(cl(x))})`});
const sube = (id, x, d=24) => set(id, {opacity: ease(cl(x)), transform:`translateY(${(1-ease(cl(x)))*d}px)`});
const todo = out => document.querySelectorAll('#pz > *').forEach(e => e.style.opacity = out);
"""
ESTRELLA = ('<svg viewBox="0 0 24 24" width="{s}" height="{s}"><defs><linearGradient id="{id}g"><stop offset="0" stop-color="{c}"/>'
            '<stop id="{id}s" offset="0" stop-color="{c}"/><stop id="{id}e" offset="0" stop-color="transparent"/></linearGradient></defs>'
            '<path d="M12 2.2l2.9 6.3 6.9.7-5.2 4.6 1.5 6.8L12 17.1l-6.1 3.5 1.5-6.8L2.2 9.2l6.9-.7z" fill="url(#{id}g)" '
            'stroke="{c}" stroke-width="1.3" stroke-linejoin="round"/></svg>')
ESTRELLA_LLENA = ('<svg viewBox="0 0 24 24" width="{s}" height="{s}"><path d="M12 2.2l2.9 6.3 6.9.7-5.2 4.6 1.5 6.8L12 17.1l-6.1 3.5 '
                  '1.5-6.8L2.2 9.2l6.9-.7z" fill="{c}"/></svg>')

# -------------------------------------------------------------------------------------
# 13 · VERDE MENTA + TINTA · la ecuación gigante del precio desde el margen
# -------------------------------------------------------------------------------------
if "13" in QUE:
    TI = "#0e1a14"; MN = "#c6f1dc"; RJ = "#d63b1f"
    css = ARCHIVO + f"""
    #pz {{ padding:0 !important; background:{MN} !important; color:{TI}; font-family:Inter,sans-serif; }}
    .lab {{ position:absolute; left:72px; top:64px; font:800 22px Inter; letter-spacing:.16em; }}
    .tt {{ position:absolute; left:72px; top:104px; font:800 100px/0.95 Archivo; letter-spacing:-0.045em; }}
    .sb {{ position:absolute; left:72px; top:222px; font:600 32px Inter; color:#2f4a3c; }}
    .eq {{ position:absolute; left:72px; top:320px; right:72px; height:430px; border:4px solid {TI}; border-radius:34px; background:#e6fbf0; }}
    .eq .t {{ position:absolute; font:800 92px Archivo; letter-spacing:-0.04em; white-space:nowrap; }}
    .fr {{ position:absolute; left:440px; top:62px; width:440px; text-align:center; }}
    .fr .n {{ font:800 92px Archivo; letter-spacing:-0.04em; }}
    .fr .b {{ height:8px; background:{TI}; border-radius:4px; margin:8px 0 10px; transform-origin:left; }}
    .fr .d {{ font:800 76px Archivo; letter-spacing:-0.04em; }}
    .res {{ background:{TI}; color:{MN}; padding:4px 22px 10px; border-radius:18px; }}
    .chk {{ position:absolute; left:72px; right:72px; top:790px; font:700 30px Inter; }}
    .chk b {{ background:{TI}; color:{MN}; padding:2px 10px; border-radius:8px; }}
    .rule {{ position:absolute; left:72px; right:72px; top:900px; height:3px; background:{TI}; opacity:.25; }}
    .err {{ position:absolute; left:72px; right:72px; top:950px; }}
    .err .k {{ font:800 24px Inter; letter-spacing:.14em; color:{RJ}; }}
    .err .m {{ position:relative; display:inline-block; margin-top:14px; font:800 86px Archivo; letter-spacing:-0.04em; color:#3b4f45; }}
    .err .m i {{ position:absolute; left:-8px; top:50%; height:9px; width:0; background:{RJ}; border-radius:5px; transform:rotate(-3deg); }}
    .err .x {{ margin-top:16px; font:700 34px/1.25 Inter; }}
    .err .x b {{ color:{RJ}; }}
    .pie {{ position:absolute; left:72px; right:72px; bottom:44px; display:flex; justify-content:space-between; font:700 24px Inter; }}
    .pie span:last-child {{ font-weight:600; color:#2f4a3c; }}
    """
    html = (f'<style>{css}</style><div id="pz">'
            '<div class="lab" id="lab">PRECIO DESDE EL MARGEN</div>'
            '<div class="tt" id="tt">¿Querés ganar 40 %?</div>'
            '<div class="sb" id="sb">No le sumes 40 % al costo. Hacé esta cuenta.</div>'
            '<div class="eq" id="eq">'
            '<div class="t" id="e1" style="left:44px;top:146px;font-size:84px">Precio =</div>'
            '<div class="fr"><div class="n" id="e2">$6.000</div><div class="b" id="e3"></div><div class="d" id="e4">1 − 0,40</div></div>'
            '<div class="t" id="e5" style="left:40px;top:304px">= <span class="res">$10.000</span></div>'
            '</div>'
            '<div class="chk" id="chk">Comprobalo: $10.000 − $6.000 = $4.000, que es el <b>40 %</b> de $10.000. ✓</div>'
            '<div class="rule" id="rule"></div>'
            '<div class="err"><div class="k" id="ek">✕ EL ERROR DE SIEMPRE</div>'
            '<div class="m" id="em">$6.000 + 40 % = $8.400<i id="ei"></i></div>'
            '<div class="x" id="ex">Así ganás $2.400 de $8.400: <b>solo el 28,6 %</b>.</div></div>'
            '<div class="pie"><span>Nicolás Benítez</span><span>Precio = costo ÷ (1 − margen)</span></div></div>')
    js = JS_UTIL + """
    function frame(t) {
      const out = 1 - seg(t, .95, 1); todo(out);
      sube('lab', seg(t, .0, .05)); sube('tt', seg(t, .02, .08)); sube('sb', seg(t, .06, .12));
      set('lab', {opacity: ease(seg(t,0,.05))*out}); set('tt', {opacity: ease(seg(t,.02,.08))*out}); set('sb', {opacity: ease(seg(t,.06,.12))*out});
      sube('e1', seg(t, .14, .19)); sube('e2', seg(t, .2, .25));
      set('e3', {transform:`scaleX(${ease(seg(t, .25, .3))})`});
      sube('e4', seg(t, .3, .35));
      pop('e5', seg(t, .4, .47));
      sube('chk', seg(t, .5, .56)); set('chk', {opacity: ease(seg(t,.5,.56))*out});
      sube('ek', seg(t, .6, .64)); sube('em', seg(t, .62, .67));
      set('ek', {opacity: ease(seg(t,.6,.64))*out}); set('em', {opacity: ease(seg(t,.62,.67))*out});
      set('ei', {width: `calc(${ease(seg(t, .7, .76))*100}% + 16px)`, opacity: t > .7 ? 1 : 0});
      sube('ex', seg(t, .78, .83)); set('ex', {opacity: ease(seg(t,.78,.83))*out});
    }
    """
    render_anim(html, js, f"{OUT}/13_precio_desde_margen", segundos=8, portada_t=0.9)

# -------------------------------------------------------------------------------------
# 14 · MARRÓN OSCURO + DORADO · 5 estrellas gigantes y 4 consejos como reseñas
# -------------------------------------------------------------------------------------
if "14" in QUE:
    GO = "#f2b632"; MA = "#24150c"; CR = "#f6ead7"
    css = f"""
    #pz {{ padding:0 !important; background:radial-gradient(900px 700px at 50% 20%, #3a2414 0%, {MA} 70%) !important; color:{CR}; font-family:Inter,sans-serif; }}
    .tt {{ position:absolute; left:0; right:0; top:62px; text-align:center; font:800 84px/1 'Inter Display',Inter; letter-spacing:-0.04em; }}
    .tt em {{ font-style:normal; color:{GO}; }}
    .st {{ position:absolute; left:0; right:0; top:262px; display:flex; justify-content:center; gap:14px; }}
    .st span {{ display:block; filter:drop-shadow(0 8px 24px rgba(242,182,50,.35)); }}
    .rv {{ position:absolute; left:72px; right:72px; height:160px; border-radius:24px; background:rgba(246,234,215,.07);
           border:2px solid rgba(242,182,50,.28); padding:22px 28px; display:flex; gap:22px; align-items:center; }}
    .rv .av {{ flex:none; width:64px; height:64px; border-radius:50%; background:{GO}; color:{MA}; font:800 30px Inter;
               display:flex; align-items:center; justify-content:center; }}
    .rv .mini {{ position:static; display:flex; gap:3px; margin-bottom:8px; }}
    .rv .q {{ font:700 32px/1.22 Inter; letter-spacing:-0.01em; }}
    .rv .q span {{ color:{GO}; }}
    .pie {{ position:absolute; left:72px; right:72px; bottom:42px; display:flex; justify-content:space-between; font:700 24px Inter; color:#cdb79a; }}
    .pie b {{ color:{CR}; }}
    """
    CONSEJOS = ["Pedila <span>unos días después</span> de que le llegó el producto.",
                "Mandale el <span>link directo</span> para opinar. Un clic, no cinco.",
                "Respondé todas, <span>también las malas</span>.",
                "Mostralas <span>en la página del producto</span>, cerca del botón de compra."]
    estrellas = "".join(f'<span id="s{k}">{ESTRELLA.format(s=150, id=f"z{k}", c=GO)}</span>' for k in range(5))
    mini = "".join(ESTRELLA_LLENA.format(s=22, c=GO) for _ in range(5))
    rv = "".join(f'<div class="rv" id="r{k}" style="top:{474 + 180 * k}px"><div class="av">{k + 1}</div>'
                 f'<div><div class="mini">{mini}</div><div class="q">{c}</div></div></div>' for k, c in enumerate(CONSEJOS))
    html = (f'<style>{css}</style><div id="pz"><div class="tt" id="tt">Las reseñas venden.<br><em>Cómo conseguir más.</em></div>'
            f'<div class="st">{estrellas}</div>{rv}'
            f'<div class="pie"><span><b>Nicolás Benítez</b></span><span>¿Le pedís reseñas a tus clientes?</span></div></div>')
    js = JS_UTIL + """
    function frame(t) {
      const out = 1 - seg(t, .95, 1); todo(out);
      sube('tt', seg(t, 0, .07)); set('tt', {opacity: ease(seg(t, 0, .07))*out});
      for (let k = 0; k < 5; k++) {
        const f = ease(seg(t, .1 + .06*k, .16 + .06*k));
        ['s','e'].forEach(p => $('z'+k+p).setAttribute('offset', f));
        set('s'+k, {transform:`scale(${1 + .12*Math.sin(Math.PI*f)})`});
      }
      for (let k = 0; k < 4; k++) { const x = seg(t, .44 + .09*k, .5 + .09*k);
        set('r'+k, {opacity: ease(x)*out, transform:`translateX(${(1-ease(x))*-60}px)`}); }
    }
    """
    render_anim(html, js, f"{OUT}/14_resenas_como_conseguir", segundos=8, portada_t=0.9)

# -------------------------------------------------------------------------------------
# 15 · GRIS APAGADO → BLANCO Y VIOLETA · antes / después con una cortina que barre
# -------------------------------------------------------------------------------------
if "15" in QUE:
    VI = "#7c3aed"; TI = "#16121f"
    LAMPARA = ('<svg viewBox="0 0 120 120" width="{s}" height="{s}"><line x1="60" y1="4" x2="60" y2="40" stroke="{c}" stroke-width="3"/>'
               '<path d="M22 84 Q60 26 98 84 Z" fill="{c}"/><rect x="18" y="82" width="84" height="7" rx="3" fill="{c}"/>'
               '<ellipse cx="60" cy="98" rx="15" ry="8" fill="{l}"/></svg>')
    css = ARCHIVO + f"""
    #pz {{ padding:0 !important; background:#ffffff !important; color:{TI}; font-family:Inter,sans-serif; }}
    .tt {{ position:absolute; left:72px; top:58px; font:800 80px/0.98 Archivo; letter-spacing:-0.04em; z-index:5; }}
    .tt em {{ font-style:normal; color:{VI}; }}
    .capa {{ position:absolute; left:0; right:0; top:250px; height:690px; }}
    #an {{ background:#d9d8dc; color:#77757d; }}
    #de {{ background:#ffffff; color:{TI}; }}
    .eti {{ position:absolute; left:72px; top:34px; font:800 24px Inter; letter-spacing:.16em; padding:8px 16px; border-radius:99px; }}
    #an .eti {{ background:#c4c2c8; color:#5d5b63; }}
    #de .eti {{ background:#efe7ff; color:{VI}; }}
    .ft {{ position:absolute; left:72px; top:96px; width:250px; height:250px; border-radius:28px; display:flex; align-items:center; justify-content:center; }}
    #an .ft {{ background:#cbc9ce; }} #de .ft {{ background:#f4efff; }}
    .an-t {{ position:absolute; left:360px; right:72px; top:120px; font:500 42px/1.3 Inter; font-style:italic; }}
    .de-h {{ position:absolute; left:360px; right:72px; top:110px; font:800 56px/1.05 Archivo; letter-spacing:-0.025em; }}
    .ch {{ position:absolute; left:72px; right:72px; top:390px; display:flex; flex-wrap:wrap; gap:14px; }}
    .ch span {{ font:700 32px Inter; padding:16px 24px; border-radius:16px; background:#f4efff; color:{VI}; border:2px solid #e2d4ff; }}
    .inc {{ position:absolute; left:72px; right:72px; font:600 36px/1.3 Inter; }}
    .inc b {{ color:{VI}; }}
    .an-x {{ position:absolute; left:72px; right:72px; top:410px; font:600 34px/1.4 Inter; color:#8d8b93; }}
    .barra {{ position:absolute; top:250px; height:690px; width:8px; margin-left:-4px; background:{VI}; z-index:4; }}
    .barra i {{ position:absolute; left:50%; top:50%; width:74px; height:74px; margin:-37px 0 0 -37px; border-radius:50%; background:{VI};
               color:#fff; font:800 28px Inter; font-style:normal; display:flex; align-items:center; justify-content:center; box-shadow:0 10px 30px rgba(124,58,237,.45); }}
    .pd {{ position:absolute; left:72px; right:72px; top:975px; border-radius:26px; background:{TI}; color:#fff; padding:26px 30px; }}
    .pd .k {{ font:800 22px Inter; letter-spacing:.16em; color:#c4a5ff; }}
    .pd .q {{ margin-top:10px; font:600 33px/1.32 Inter; }}
    .pie {{ position:absolute; left:72px; right:72px; bottom:36px; display:flex; justify-content:space-between; font:700 23px Inter; color:#55525c; }}
    """
    antes = ('<div class="capa" id="an"><div class="eti">ANTES</div>'
             f'<div class="ft">{LAMPARA.format(s=170, c="#9a98a0", l="#b8b6bc")}</div>'
             '<div class="an-t">“Lámpara negra muy linda, buena calidad, consultar.”</div>'
             '<div class="an-x">Sin medidas. Sin material. Sin envío.<br>El cliente tiene que preguntar todo… o se va.</div></div>')
    despues = ('<div class="capa" id="de"><div class="eti">DESPUÉS</div>'
               f'<div class="ft">{LAMPARA.format(s=170, c=TI, l="#ffd166")}</div>'
               '<div class="de-h">Lámpara colgante negra de aluminio</div>'
               '<div class="ch"><span id="c0">Aluminio</span><span id="c1">Ø 30 cm</span><span id="c2">Para cocina o comedor</span></div>'
               '<div class="inc" id="i0" style="top:520px"><b>Incluye:</b> florón y 1 m de cable.</div>'
               '<div class="inc" id="i1" style="top:590px"><b>Envío</b> a todo el país.</div></div>')
    html = (f'<style>{css}</style><div id="pz"><div class="tt">La misma descripción,<br><em>antes y después de la IA.</em></div>'
            f'{antes}{despues}<div class="barra" id="ba"><i>⇆</i></div>'
            '<div class="pd" id="pd"><div class="k">EL PEDIDO, PARA COPIAR</div>'
            '<div class="q">“Con estos datos, escribí una descripción clara para mi tienda, con título, 3 datos clave y qué incluye.”</div></div>'
            '<div class="pie"><span>Nicolás Benítez</span><span>Producto de ejemplo</span></div></div>')
    js = JS_UTIL + """
    function frame(t) {
      const out = 1 - seg(t, .95, 1); todo(out);
      const w = ease(seg(t, .2, .5));                 // la cortina barre de izquierda a derecha
      $('de').style.clipPath = `inset(0 ${100 - w*100}% 0 0)`;
      set('ba', {left: (w*1080) + 'px', opacity: (t > .17 && t < .56 ? 1 : 0) * out});
      for (let k = 0; k < 3; k++) pop('c'+k, seg(t, .5 + .04*k, .55 + .04*k));
      for (let k = 0; k < 2; k++) sube('i'+k, seg(t, .62 + .04*k, .67 + .04*k));
      sube('pd', seg(t, .74, .8)); set('pd', {opacity: ease(seg(t, .74, .8))*out});
    }
    """
    render_anim(html, js, f"{OUT}/15_descripcion_antes_despues", segundos=7, portada_t=0.9)

# -------------------------------------------------------------------------------------
# 16 · CELESTE + AZUL NOCHE · la balanza: publicidad contra ganancia según el margen
# -------------------------------------------------------------------------------------
if "16" in QUE:
    CE = "#cfeaf7"; TI = "#0b2233"; VE = "#13985a"; RJ = "#d9412b"; AZ = "#12507a"
    css = ARCHIVO + f"""
    #pz {{ padding:0 !important; background:{CE} !important; color:{TI}; font-family:Inter,sans-serif; }}
    .t1 {{ position:absolute; left:72px; right:72px; top:58px; font:800 54px/1.05 Archivo; letter-spacing:-0.03em; }}
    .t2 {{ position:absolute; left:72px; top:182px; font:800 118px/1 Archivo; letter-spacing:-0.05em; color:{AZ}; }}
    .ro {{ position:absolute; left:72px; right:72px; top:330px; display:flex; gap:12px; align-items:center; font:700 28px Inter; flex-wrap:nowrap; }}
    .ro span {{ background:#fff; border-radius:14px; padding:10px 16px; white-space:nowrap; }}
    .ro span.r {{ background:{TI}; color:#fff; }}
    .mg {{ position:absolute; left:0; right:0; top:420px; text-align:center; font:800 34px Inter; }}
    .mg b {{ background:{AZ}; color:#fff; padding:4px 16px; border-radius:12px; }}
    .poste {{ position:absolute; left:532px; top:560px; width:16px; height:330px; background:{TI}; border-radius:8px; }}
    .base {{ position:absolute; left:420px; top:880px; width:240px; height:22px; background:{TI}; border-radius:11px; }}
    .viga {{ position:absolute; left:190px; top:552px; width:700px; height:16px; background:{TI}; border-radius:8px; transform-origin:350px 8px; }}
    .eje {{ position:absolute; left:522px; top:542px; width:36px; height:36px; border-radius:50%; background:{AZ}; border:5px solid {TI}; }}
    .plato {{ position:absolute; width:280px; height:150px; margin-left:-140px; }}
    .plato .hilo {{ position:absolute; left:139px; top:0; width:3px; height:70px; background:{TI}; }}
    .plato .pl {{ position:absolute; left:0; top:68px; width:280px; height:82px; border-radius:0 0 140px 140px; border:4px solid {TI}; border-top-width:6px; background:#fff;
                 display:flex; flex-direction:column; align-items:center; justify-content:center; }}
    .plato .k {{ font:700 21px Inter; color:#4b6577; }}
    .plato .v {{ font:800 34px Archivo; letter-spacing:-0.02em; }}
    .res {{ position:absolute; left:0; right:0; top:938px; text-align:center; font:800 52px Archivo; letter-spacing:-0.03em; }}
    .co {{ position:absolute; left:72px; right:72px; top:1036px; border-radius:26px; background:{TI}; color:#fff; padding:24px 30px; }}
    .co .k {{ font:800 22px Inter; letter-spacing:.14em; color:#8fd0f0; }}
    .co .f {{ margin-top:8px; font:800 44px Archivo; letter-spacing:-0.02em; }}
    .co .e {{ margin-top:6px; font:600 28px Inter; color:#cfe6f2; }}
    .pie {{ position:absolute; left:72px; right:72px; bottom:34px; display:flex; justify-content:space-between; font:700 23px Inter; color:#35546a; }}
    """
    html = (f'<style>{css}</style><div id="pz">'
            '<div class="t1" id="t1">Vendiste 5 veces lo que pusiste en publicidad.</div>'
            '<div class="t2" id="t2">¿Ganaste?</div>'
            '<div class="ro" id="ro"><span>Publicidad $60.000</span>→<span>Ventas $300.000</span>=<span class="r">ROAS 5</span></div>'
            '<div class="mg" id="mg">Con un margen del <b id="mgv">40 %</b></div>'
            '<div class="poste"></div><div class="base"></div><div class="viga" id="vg"></div><div class="eje"></div>'
            '<div class="plato" id="pa"><div class="hilo"></div><div class="pl"><div class="k">Publicidad</div><div class="v">$60.000</div></div></div>'
            '<div class="plato" id="pb"><div class="hilo"></div><div class="pl" id="pbp"><div class="k">Ganancia de las ventas</div><div class="v" id="gv">$120.000</div></div></div>'
            '<div class="res" id="rs"></div>'
            '<div class="co" id="co"><div class="k">EL ROAS QUE NECESITÁS DEPENDE DE TU MARGEN</div>'
            '<div class="f">ROAS mínimo = 1 ÷ margen</div><div class="e">Con 40 % de margen: 2,5 · Con 20 %: 5</div></div>'
            '<div class="pie"><span>Nicolás Benítez</span><span>ROAS = ventas ÷ publicidad</span></div></div>')
    js = JS_UTIL + f"""
    const R = 350, CX = 540, CY = 560;
    function frame(t) {{
      const out = 1 - seg(t, .95, 1); todo(out);
      sube('t1', seg(t, 0, .06)); set('t1', {{opacity: ease(seg(t,0,.06))*out}});
      pop('t2', seg(t, .05, .11)); set('t2', {{opacity: ease(seg(t,.05,.11))*out}});
      sube('ro', seg(t, .12, .18)); set('ro', {{opacity: ease(seg(t,.12,.18))*out}});
      const fase2 = t > .58;
      $('mgv').textContent = fase2 ? '20 %' : '40 %';
      set('mg', {{opacity: (fase2 ? ease(seg(t, .58, .62)) : ease(seg(t, .2, .25))) * out}});
      // ganancia de las ventas: 40 % de 300.000 = 120.000 ; 20 % = 60.000
      const g = fase2 ? mix(120000, 60000, ease(seg(t, .6, .68))) : 120000;
      $('gv').textContent = '$' + AR(g);
      // ángulo: la ganancia pesa más que la publicidad -> el plato derecho baja
      let ang = 0;
      if (!fase2) ang = 9 * ease(seg(t, .28, .38));
      else ang = 9 * (1 - ease(seg(t, .6, .7)));
      $('vg').style.transform = `rotate(${{ang}}deg)`;
      const a = ang * Math.PI / 180;
      const ax = CX - R*Math.cos(a), ay = CY - R*Math.sin(a), bx = CX + R*Math.cos(a), by = CY + R*Math.sin(a);
      set('pa', {{left: ax + 'px', top: ay + 'px'}}); set('pb', {{left: bx + 'px', top: by + 'px'}});
      set('pbp', {{background: fase2 ? (t > .7 ? '#fde3df' : '#fff') : (t > .38 ? '#dcf5e8' : '#fff')}});
      const rs = $('rs');
      if (!fase2) {{ rs.innerHTML = '$120.000 − $60.000 = <span style="color:{VE}">te quedan $60.000</span>'; set('rs', {{opacity: ease(seg(t, .4, .46))*out}}); }}
      else {{ rs.innerHTML = '$60.000 − $60.000 = <span style="color:{RJ}">te quedan $0</span>'; set('rs', {{opacity: ease(seg(t, .7, .75))*out}}); }}
      if (t > .55 && t < .58) set('rs', {{opacity: 0}});
      sube('co', seg(t, .8, .86)); set('co', {{opacity: ease(seg(t, .8, .86))*out}});
    }}
    """
    render_anim(html, js, f"{OUT}/16_roas_ganaste", segundos=8, portada_t=0.9)
