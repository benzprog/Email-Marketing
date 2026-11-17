"""Banco de piezas animadas · tanda B (05 a 08). Ejecutar: python3 banco_B.py [05 06 07 08]  (OUT=carpeta opcional)

Cada pieza tiene su propia composición (regla de variedad, 17/11/2026):
05 coral + celular con 5 pedidos que suben como en un chat
06 gris claro + planilla que se transforma en gráfico de barras verde
07 beige + polaroids que caen sobre una mesa, con la regla escrita a mano (Caveat, OFL, en banco/fonts)
08 azul marino + cian + regla horizontal con el marcador que llega al envío gratis
"""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
from kit_animado import render_anim, CURSOR

OUT = os.environ.get("OUT", AQUI)
QUE = sys.argv[1:] or ["05", "06", "07", "08"]
KITF = os.path.join(os.path.dirname(os.path.dirname(AQUI)), "kit", "fonts")
ARCHIVO = "".join(f'@font-face{{font-family:Archivo;src:url("file://{KITF}/Archivo-{w}.ttf");font-weight:{w}}}' for w in (500, 600, 700, 800))
CAVEAT = f'@font-face{{font-family:Caveat;src:url("file://{AQUI}/fonts/Caveat.ttf");font-weight:400 700}}'

JS_UTIL = """
const AR = n => Math.round(n).toLocaleString('es-AR');
const pop = (id, x) => set(id, {opacity: ease(cl(x)), transform:`scale(${.7 + .3*ease(cl(x))})`});
const outBack = x => { const c1 = 1.70158, c3 = c1 + 1; return 1 + c3*Math.pow(x-1,3) + c1*Math.pow(x-1,2); };
"""


def js(code, **vals):
    """Inserta valores en el JS sin pelear con las llaves de los f-strings."""
    for k, v in vals.items():
        code = code.replace("@@" + k + "@@", str(v))
    return JS_UTIL + code


# =====================================================================================
# 05 · CORAL · un celular grande con los 5 pedidos que van subiendo
# =====================================================================================
if "05" in QUE:
    CO = "#ff5e57"; OSC = "#2a0f12"
    PEDIDOS = [
        "Con estos datos, escribí la descripción de mi producto: [pegá la ficha].",
        "Un cliente reclama porque su pedido se demoró. Escribí una respuesta amable y corta.",
        "Dame 10 asuntos para un mail de promo de fin de semana.",
        "Armé un combo de mate, termo y yerba. Dame 10 nombres para el combo.",
        "Te pego 50 reseñas. ¿Cuáles son las 3 quejas que más se repiten?",
    ]
    css = ARCHIVO + f"""
    #pz {{ padding:0 !important; background:{CO} !important; color:#fff; font-family:Inter,sans-serif; }}
    .t5 {{ position:absolute; left:70px; top:58px; font:800 92px/0.95 Archivo; letter-spacing:-0.045em; color:#fff; }}
    .t5 small {{ display:block; font:800 44px Archivo; letter-spacing:-0.02em; color:{OSC}; margin-top:12px; }}
    .rot {{ position:absolute; right:70px; top:72px; width:440px; text-align:right; font:800 25px/1.25 Inter; color:{OSC}; }}
    .rot b {{ display:inline-block; white-space:nowrap; margin-top:8px; background:{OSC}; color:#fff; padding:10px 16px; border-radius:14px; font-size:24px; }}
    .cel {{ position:absolute; left:210px; top:322px; width:660px; height:1060px; border-radius:72px; background:#141414; padding:20px;
            box-shadow:0 40px 80px rgba(80,10,10,.45); }}
    .pan {{ position:relative; width:100%; height:100%; border-radius:54px; background:#fff6f3; overflow:hidden; }}
    .cab {{ position:absolute; left:0; right:0; top:0; height:118px; background:#fff; border-bottom:2px solid #f3dcd6; z-index:2;
            display:flex; align-items:center; gap:16px; padding:30px 30px 0; }}
    .cab i {{ width:54px; height:54px; border-radius:50%; background:{CO}; color:#fff; font:800 21px Inter; font-style:normal;
              display:flex; align-items:center; justify-content:center; }}
    .cab span {{ font:800 26px Inter; color:#2a2a2a; }}
    .cab small {{ display:block; font:600 20px Inter; color:#9b8f8c; }}
    .lista {{ position:absolute; left:0; right:0; top:118px; padding:26px 26px 140px; }}
    .msg {{ margin-left:auto; width:470px; background:{CO}; color:#fff; border-radius:28px 28px 8px 28px; padding:20px 24px 22px;
            font:600 27px/1.3 Inter; position:relative; }}
    .msg .n {{ position:absolute; left:-62px; top:10px; width:46px; height:46px; border-radius:50%; background:{OSC}; color:#fff;
               font:800 22px Inter; display:flex; align-items:center; justify-content:center; }}
    .rep {{ width:300px; margin:16px 0 30px; background:#fff; border:2px solid #f0dcd6; border-radius:26px 26px 26px 8px; padding:20px 22px; }}
    .rep i {{ display:block; height:12px; border-radius:6px; background:#f1d9d3; margin-top:12px; }}
    .rep i:first-child {{ margin-top:0; }}
    .dots {{ display:flex; gap:8px; padding:6px 2px; }}
    .dots b {{ width:12px; height:12px; border-radius:50%; background:#d8b7ae; }}
    .ent {{ position:absolute; left:0; right:0; bottom:0; height:112px; background:#fff; border-top:2px solid #f3dcd6; z-index:2;
            display:flex; align-items:center; gap:14px; padding:0 26px 18px; }}
    .ent div {{ flex:1; height:62px; border-radius:31px; background:#f6efed; color:#a99c98; font:600 23px Inter; display:flex; align-items:center; padding:0 24px; }}
    .ent b {{ width:62px; height:62px; border-radius:50%; background:{CO}; color:#fff; font:900 30px Inter; display:flex; align-items:center; justify-content:center; }}
    .fir5 {{ position:absolute; left:70px; top:300px; font:800 24px Inter; color:{OSC}; writing-mode:vertical-rl; transform:rotate(180deg); }}
    """
    cuerpo = "".join(f'<div class="msg" id="m{k}"><div class="n">{k + 1}</div>{p}</div>'
                     f'<div class="rep" id="r{k}"><div class="dots" id="d{k}"><b></b><b></b><b></b></div>'
                     f'<div id="s{k}"><i style="width:92%"></i><i style="width:76%"></i><i style="width:58%"></i></div></div>'
                     for k, p in enumerate(PEDIDOS))
    html = (f'<style>{css}</style><div id="pz">'
            f'<div class="t5">5 pedidos<br>a la IA<small>para tu tienda online</small></div>'
            f'<div class="rot">Copialos tal cual.<br><b>Pegalos en ChatGPT o Claude</b></div>'
            f'<div class="cel"><div class="pan"><div class="cab"><i>IA</i><span>Asistente de IA<small>en línea</small></span></div>'
            f'<div class="lista" id="li">{cuerpo}</div>'
            f'<div class="ent"><div>Escribí acá…</div><b>↑</b></div></div></div>'
            f'<div class="fir5">Nicolás Benítez</div></div>')
    code = """
    let SC = null;
    function medir() {
      // cuánto hay que subir la lista para que el pedido k quede a la vista (con su respuesta)
      const vis = 1020 - 118 - 112;
      SC = [];
      for (let k = 0; k < 5; k++) {
        const r = $('r'+k);
        SC.push(Math.max(0, r.offsetTop + r.offsetHeight + 26 - vis));
      }
    }
    function frame(t) {
      if (!SC) medir();
      const out = 1 - seg(t, .95, 1);
      document.querySelectorAll('#pz > *').forEach(e => e.style.opacity = out);
      const P = .17, A = .06;                            // cada pedido tiene su turno de .17
      let y = 0;
      for (let k = 0; k < 5; k++) {
        const a = A + P*k;
        const m = ease(seg(t, a, a + .04));
        set('m'+k, {opacity: m, transform:`translateY(${(1-m)*30}px) scale(${.92 + .08*m})`, transformOrigin:'right bottom'});
        const r = seg(t, a + .04, a + .06);
        set('r'+k, {opacity: r});
        const listo = t > a + .1;
        set('d'+k, {display: listo ? 'none' : 'flex'});
        set('s'+k, {display: listo ? 'block' : 'none'});
        $('d'+k).querySelectorAll('b').forEach((b, i) => b.style.opacity = .35 + .65*Math.abs(Math.sin(t*50 - i*.8)));
        if (t > a) y = mix(k ? SC[k-1] : 0, SC[k], ease(seg(t, a, a + .05)));
      }
      set('li', {transform:`translateY(${-y}px)`});
    }
    """
    render_anim(html, js(code), f"{OUT}/05_pedidos_ia_tienda", segundos=8, portada_t=0.9)


# =====================================================================================
# 06 · GRIS CLARO · la planilla se levanta y se vuelve un gráfico de barras verde
# =====================================================================================
if "06" in QUE:
    VE = "#16a34a"; TI = "#14181f"
    DATOS = [("Mate", 42), ("Termo", 31), ("Bombilla", 18), ("Yerba", 55), ("Matera", 12)]
    css = ARCHIVO + f"""
    #pz {{ padding:0 !important; background:#eceef1 !important; color:{TI}; font-family:Inter,sans-serif; }}
    .t6 {{ position:absolute; left:70px; top:60px; font:800 80px/0.98 Archivo; letter-spacing:-0.04em; }}
    .t6 em {{ font-style:normal; color:{VE}; }}
    .lienzo {{ position:absolute; left:60px; right:60px; top:300px; height:640px; border-radius:30px; background:#fff;
               box-shadow:0 20px 50px rgba(20,30,40,.08); overflow:hidden; }}
    .enc {{ position:absolute; left:40px; right:40px; top:30px; height:56px; display:flex; align-items:center; justify-content:space-between;
            font:800 25px Inter; color:#6b7280; border-bottom:2px solid #e5e7eb; }}
    .pz {{ position:absolute; display:flex; align-items:center; justify-content:space-between; padding:0 22px; overflow:hidden;
           font:700 28px Inter; color:{TI}; white-space:nowrap; }}
    .val {{ position:absolute; width:140px; text-align:center; font:800 30px Inter; color:{VE}; }}
    .lab {{ position:absolute; width:150px; text-align:center; font:700 23px Inter; color:#4b5563; }}
    .base {{ position:absolute; left:40px; right:40px; top:560px; height:3px; background:#d1d5db; }}
    .q {{ position:absolute; right:40px; top:32px; max-width:560px; background:{TI}; color:#fff; border-radius:24px 24px 6px 24px; padding:16px 22px; font:600 25px/1.3 Inter; }}
    .a {{ position:absolute; left:40px; top:112px; max-width:520px; background:#dcfce7; color:#14532d; border-radius:24px 24px 24px 6px; padding:16px 22px; font:700 25px/1.3 Inter; }}
    .pasos {{ position:absolute; left:60px; right:60px; top:980px; display:flex; gap:16px; }}
    .pa {{ flex:1; border-radius:22px; background:#fff; padding:20px 18px; border:3px solid transparent; }}
    .pa b {{ display:flex; width:44px; height:44px; border-radius:50%; background:#d1d5db; color:#fff; font:800 22px Inter; align-items:center; justify-content:center; }}
    .pa p {{ margin-top:12px; font:700 24px/1.22 Inter; }}
    .pa.on {{ border-color:{VE}; }} .pa.on b {{ background:{VE}; }}
    .pie6 {{ position:absolute; left:70px; right:70px; bottom:40px; display:flex; justify-content:space-between; font:600 23px Inter; color:#6b7280; }}
    .pie6 b {{ color:{TI}; }}
    """
    # rectángulos: fila de la planilla (A) y barra del gráfico (B), en coordenadas del lienzo (960 x 640)
    FILAS = [dict(x=40, y=100 + 76 * k, w=880, h=64) for k in range(5)]
    BARRAS = []
    for k, (_, v) in enumerate(DATOS):
        h = round(v / 55 * 330)
        BARRAS.append(dict(x=58 + 172 * k, y=560 - h, w=140, h=h))
    piezas = "".join(f'<div class="pz" id="b{k}"><span id="bn{k}">{n}</span><span id="bv{k}">{v}</span></div>'
                     f'<div class="val" id="v{k}" style="left:{BARRAS[k]["x"]}px;top:{BARRAS[k]["y"] - 44}px">{v}</div>'
                     f'<div class="lab" id="l{k}" style="left:{BARRAS[k]["x"] - 5}px;top:574px">{n}</div>'
                     for k, (n, v) in enumerate(DATOS))
    pasos = [("1", "Exportá tus ventas en Excel o CSV"), ("2", "Adjuntá el archivo en ChatGPT o Claude"),
             ("3", "Preguntá en castellano"), ("4", "Pedile el gráfico")]
    html = (f'<style>{css}</style><div id="pz">'
            f'<div class="t6">Subí tu planilla<br>de ventas y <em>preguntale.</em></div>'
            f'<div class="lienzo"><div class="enc" id="enc"><span>Producto</span><span>Unidades en octubre</span></div>'
            f'<div class="base" id="base"></div>{piezas}'
            f'<div class="q" id="q">¿Qué producto vendió más en octubre?</div>'
            f'<div class="a" id="a">Yerba: 55 unidades. Después, el mate.</div></div>'
            f'<div class="pasos">' + "".join(f'<div class="pa" id="p{k}"><b>{n}</b><p>{t}</p></div>' for k, (n, t) in enumerate(pasos)) + '</div>'
            f'<div class="pie6"><span>Ejemplo con datos inventados.</span><b>Nicolás Benítez</b></div></div>')
    code = """
    const A = @@A@@, B = @@B@@;
    function frame(t) {
      const out = 1 - seg(t, .95, 1);
      document.querySelectorAll('#pz > *').forEach(e => e.style.opacity = out);
      const filas = seg(t, .02, .16);                  // aparece la planilla
      const m = ease(seg(t, .26, .5));                 // la planilla se levanta y se vuelve barras
      for (let k = 0; k < 5; k++) {
        const mk = ease(seg(t, .26 + .03*k, .44 + .03*k));
        const a = A[k], b = B[k];
        const e = $('b'+k);
        Object.assign(e.style, {left: mix(a.x, b.x, mk)+'px', top: mix(a.y, b.y, mk)+'px', width: mix(a.w, b.w, mk)+'px', height: mix(a.h, b.h, mk)+'px',
          borderRadius: mix(14, 16, mk)+'px', background: mk > .02 ? `rgba(22,163,74,${.12 + .88*mk})` : (k % 2 ? '#f7f8fa' : '#fff'),
          border: mk > .02 ? 'none' : '1px solid #eef0f3', opacity: seg(t, .02 + .025*k, .06 + .025*k)});
        set('bn'+k, {opacity: 1 - seg(t, .26, .32)}); set('bv'+k, {opacity: 1 - seg(t, .26, .32)});
        set('v'+k, {opacity: seg(t, .48 + .02*k, .52 + .02*k)});
        set('l'+k, {opacity: seg(t, .46, .52)});
      }
      set('enc', {opacity: (1 - seg(t, .24, .3)) * filas});
      set('base', {opacity: seg(t, .44, .5)});
      const q = ease(seg(t, .58, .63)); set('q', {opacity: q, transform:`translateY(${(1-q)*16}px)`});
      const a = ease(seg(t, .68, .73)); set('a', {opacity: a, transform:`translateY(${(1-a)*16}px)`});
      const hi = t > .72;
      $('b3').style.boxShadow = hi ? '0 0 0 6px #fde047' : 'none';
      // los 4 pasos se encienden en orden con la animación
      const on = t < .2 ? 0 : t < .55 ? 1 : t < .7 ? 2 : 3;
      for (let k = 0; k < 4; k++) $('p'+k).classList.toggle('on', k === on);
    }
    """
    import json
    render_anim(html, js(code, A=json.dumps(FILAS), B=json.dumps(BARRAS)), f"{OUT}/06_planilla_ventas_ia", segundos=8, portada_t=0.86)


# =====================================================================================
# 07 · BEIGE · polaroids que caen sobre la mesa, cada una con su regla escrita a mano
# =====================================================================================
if "07" in QUE:
    MA = "#3b2a1e"; TE = "#c2410c"
    css = ARCHIVO + CAVEAT + f"""
    #pz {{ padding:0 !important; color:{MA}; font-family:Inter,sans-serif;
           background:radial-gradient(900px 700px at 30% 20%, #f6ecdc 0%, #ead9bf 60%, #dfc9a8 100%) !important; }}
    .t7 {{ position:absolute; left:70px; top:56px; font:800 76px/0.98 Archivo; letter-spacing:-0.04em; }}
    .t7 span {{ font:700 96px Caveat; color:{TE}; letter-spacing:0; display:inline-block; transform:rotate(-4deg); margin-left:6px; }}
    .fir7 {{ position:absolute; right:70px; top:82px; font:600 23px Inter; color:#7a6550; }}
    .pol {{ position:absolute; width:440px; height:488px; background:#fffdf8; padding:22px 22px 0; box-shadow:0 18px 30px rgba(60,40,20,.28), 0 2px 4px rgba(60,40,20,.2); }}
    .pol .foto {{ position:relative; width:396px; height:330px; overflow:hidden; }}
    .pol p {{ font:700 44px/1.0 Caveat; color:{MA}; text-align:center; margin-top:16px; }}
    .cinta {{ position:absolute; left:160px; top:-18px; width:120px; height:38px; background:rgba(255,236,170,.75); transform:rotate(-3deg); }}
    .ok {{ position:absolute; right:18px; bottom:14px; font:700 64px Caveat; color:{TE}; }}
    """
    TAZA = ('<svg viewBox="0 0 120 110" width="{w}" height="{h}"><path d="M14 22h70v46a30 30 0 0 1-30 30h-10a30 30 0 0 1-30-30z" fill="{c}"/>'
            '<path d="M84 34h10a16 16 0 0 1 0 32h-10" fill="none" stroke="{c}" stroke-width="9"/><rect x="10" y="16" width="78" height="9" rx="4" fill="{c2}"/></svg>')
    def taza(w, c="#c2410c", c2="#9a3412"):
        return TAZA.format(w=w, h=round(w * 110 / 120), c=c, c2=c2)
    fotos = [
        # 1 · fondo liso: la taza sola sobre un fondo claro parejo
        f'<div class="foto" style="background:linear-gradient(#f4f1ec,#e9e4dc);display:flex;align-items:center;justify-content:center">{taza(190)}</div>',
        # 2 · varias vistas
        '<div class="foto" style="background:#efebe5;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:6px;padding:6px">'
        f'<div style="background:#f6f3ee;display:flex;align-items:center;justify-content:center;grid-row:span 2">{taza(150)}</div>'
        f'<div style="background:#f6f3ee;display:flex;align-items:center;justify-content:center;transform:scaleX(-1)">{taza(90)}</div>'
        '<div style="background:#f6f3ee;display:flex;align-items:center;justify-content:center;overflow:hidden">'
        '<div style="width:220px;height:220px;border-radius:50%;background:#c2410c;transform:translate(30px,40px)"></div></div></div>',
        # 3 · que se vea el tamaño: la taza al lado de un celular
        '<div class="foto" style="background:linear-gradient(#f4f1ec,#e9e4dc);display:flex;align-items:flex-end;justify-content:center;gap:22px;padding-bottom:40px">'
        f'{taza(150)}<div style="width:86px;height:176px;border-radius:16px;background:#2b2b2b;border:5px solid #111"></div></div>',
        # 4 · la misma luz en todas: tres fotos con el mismo tono
        '<div class="foto" style="background:#efebe5;display:flex;align-items:center;justify-content:center;gap:10px">'
        + "".join(f'<div style="width:118px;height:150px;background:linear-gradient(160deg,#fbf7f0,#e8e1d6);display:flex;align-items:center;justify-content:center">{taza(84, c)}</div>'
                  for c in ["#c2410c", "#2563eb", "#15803d"])
        + '<div style="position:absolute;right:16px;top:12px;font:700 44px Caveat;color:#d97706">☀</div></div>',
    ]
    textos = ["Fondo liso<br>y neutro", "Frente, costado<br>y un detalle", "Que se vea<br>el tamaño", "La misma luz<br>en todas"]
    pos = [(56, 300, -6), (584, 322, 5), (92, 818, 4), (552, 806, -5)]
    pols = "".join(f'<div class="pol" id="p{k}" style="left:{x}px;top:{y}px"><div class="cinta"></div>{fotos[k]}<p>{textos[k]}</p>'
                   f'<div class="ok" id="ok{k}">✓</div></div>' for k, (x, y, r) in enumerate(pos))
    html = (f'<style>{css}</style><div id="pz"><div class="t7">Fotos de producto<br>que venden: <span>4 reglas</span></div>'
            f'<div class="fir7">Nicolás Benítez</div>{pols}</div>')
    code = """
    const ROT = @@ROT@@;
    function frame(t) {
      const out = 1 - seg(t, .95, 1);
      document.querySelectorAll('#pz > *').forEach(e => e.style.opacity = out);
      for (let k = 0; k < 4; k++) {
        const a = .06 + .14*k;
        const c = seg(t, a, a + .1);
        const y = (1 - outBack(c)) * -900;
        const r = ROT[k] + (1 - c) * (k % 2 ? 30 : -30);
        set('p'+k, {transform:`translateY(${y}px) rotate(${r}deg)`, opacity: t < a ? 0 : 1, zIndex: 10 + k});
        set('ok'+k, {opacity: seg(t, .66 + .04*k, .69 + .04*k), transform:`scale(${.6 + .4*ease(seg(t, .66 + .04*k, .69 + .04*k))}) rotate(-8deg)`});
      }
    }
    """
    render_anim(html, js(code, ROT=[r for _, _, r in pos]), f"{OUT}/07_fotos_producto", segundos=7, portada_t=0.9)


# =====================================================================================
# 08 · AZUL MARINO + CIAN · regla horizontal: del ticket promedio al envío gratis
# =====================================================================================
if "08" in QUE:
    CI = "#22d3ee"; NA = "#0b1d3a"; AM = "#fde047"
    X0, X1, VMAX = 80, 1000, 40000            # la regla va de $0 a $40.000 entre x=80 y x=1000
    px = lambda v: X0 + (X1 - X0) * v / VMAX
    css = ARCHIVO + f"""
    #pz {{ padding:0 !important; background:linear-gradient(180deg,#0b1d3a 0%,#081428 100%) !important; color:#fff; font-family:Inter,sans-serif; }}
    .t8 {{ position:absolute; left:80px; top:64px; font:800 92px/0.96 Archivo; letter-spacing:-0.045em; }}
    .t8 em {{ font-style:normal; color:{CI}; }}
    .s8 {{ position:absolute; left:80px; top:290px; font:600 30px Inter; color:#9fb3d1; }}
    .riel {{ position:absolute; left:{X0}px; width:{X1 - X0}px; top:600px; height:34px; border-radius:17px; background:#1b3358; overflow:hidden; }}
    .riel i {{ position:absolute; left:0; top:0; height:100%; width:0; background:{CI}; border-radius:17px; }}
    .tk {{ position:absolute; top:646px; width:2px; height:16px; background:#3c5a86; }}
    .tkl {{ position:absolute; top:668px; width:120px; margin-left:-60px; text-align:center; font:600 21px Inter; color:#7f95b8; }}
    .meta {{ position:absolute; left:{px(35000) - 2}px; top:470px; width:4px; height:164px; background:{AM}; }}
    .metal {{ position:absolute; left:{px(35000) - 180}px; top:404px; width:360px; text-align:center; font:800 27px/1.2 Inter; color:{AM}; }}
    .prom {{ position:absolute; left:{px(28000) - 130}px; top:712px; width:260px; text-align:center; font:700 23px/1.25 Inter; color:#9fb3d1; }}
    .prom:before {{ content:''; position:absolute; left:128px; top:-18px; width:4px; height:14px; background:#9fb3d1; }}
    .mk {{ position:absolute; top:548px; width:150px; margin-left:-75px; text-align:center; }}
    .mk b {{ display:inline-block; padding:10px 18px; border-radius:14px; background:#fff; color:{NA}; font:800 30px Inter; }}
    .mk:after {{ content:''; display:block; width:0; height:0; margin:0 auto; border:10px solid transparent; border-top-color:#fff; }}
    .msg {{ position:absolute; left:80px; right:80px; top:820px; height:96px; border-radius:22px; display:flex; align-items:center; gap:18px; padding:0 30px;
            font:800 34px Inter; }}
    .chip {{ position:absolute; left:{px(28000) - 70}px; top:470px; padding:10px 16px; border-radius:14px; background:{CI}; color:{NA}; font:800 24px Inter; }}
    .reglas {{ position:absolute; left:80px; right:80px; top:1000px; }}
    .reglas div {{ display:flex; gap:20px; align-items:flex-start; margin-bottom:34px; font:700 36px/1.25 Inter; }}
    .reglas div b {{ flex:none; width:52px; height:52px; border-radius:50%; background:{CI}; color:{NA}; font:800 26px Inter; display:flex; align-items:center; justify-content:center; margin-top:-4px; }}
    .pie8 {{ position:absolute; left:80px; right:80px; bottom:40px; display:flex; justify-content:space-between; font:600 23px Inter; color:#7f95b8; }}
    .pie8 b {{ color:#fff; }}
    """
    ticks = "".join(f'<div class="tk" style="left:{px(v) - 1}px"></div><div class="tkl" style="left:{px(v)}px">${v // 1000}k</div>'
                    for v in range(0, 40001, 5000))
    html = (f'<style>{css}</style><div id="pz">'
            f'<div class="t8">Envío gratis,<br><em>pero desde un monto.</em></div>'
            f'<div class="s8">Así el cliente que está cerca suma un producto para llegar.</div>'
            f'<div class="meta"></div><div class="metal">Envío gratis<br>desde $35.000</div>'
            f'<div class="riel"><i id="fill"></i></div>{ticks}'
            f'<div class="prom" id="prom">Ticket promedio<br>$28.000</div>'
            f'<div class="mk" id="mk"><b id="mkv">$0</b></div>'
            f'<div class="chip" id="chip">+ 1 producto de $8.000</div>'
            f'<div class="msg" id="msg"><span id="msgt"></span></div>'
            f'<div class="reglas"><div id="g0"><b>1</b>Poné el monto un poco arriba de tu ticket promedio.</div>'
            f'<div id="g1"><b>2</b>El costo del envío tiene que entrar en tu margen.</div></div>'
            f'<div class="pie8"><span>Ejemplo con números inventados.</span><b>Nicolás Benítez</b></div></div>')
    code = """
    const X0 = @@X0@@, X1 = @@X1@@, VMAX = @@VMAX@@;
    const px = v => X0 + (X1 - X0) * v / VMAX;
    function frame(t) {
      const out = 1 - seg(t, .95, 1);
      document.querySelectorAll('#pz > *').forEach(e => e.style.opacity = out);
      // 1 · el carrito llega a $28.000 · 2 · le faltan $7.000 · 3 · suma un producto de $8.000 y pasa los $35.000
      let v = 28000 * ease(seg(t, .04, .26));
      const suma = ease(seg(t, .5, .62));
      v += 8000 * suma;
      $('fill').style.width = (px(v) - X0) + 'px';
      $('fill').style.background = v >= 35000 ? '#fde047' : '#22d3ee';
      set('mk', {left: px(v) + 'px'}); $('mkv').textContent = '$' + AR(v);
      set('prom', {opacity: seg(t, .22, .28)});
      const c = seg(t, .4, .46); const cae = ease(seg(t, .46, .54));
      set('chip', {opacity: c * (1 - seg(t, .56, .6)), transform:`translateY(${cae*90}px) scale(${1 - .3*cae})`});
      const falta = t > .3 && t < .58, listo = t >= .62;
      $('msgt').textContent = listo ? '✓ ¡Llegaste! Tu envío es gratis.' : 'Te faltan $7.000 para el envío gratis';
      set('msg', {opacity: (falta || listo) ? 1 : 0, background: listo ? '#fde047' : '#16325c', color: listo ? '#0b1d3a' : '#fff',
                  transform:`scale(${listo ? 1 + .04*Math.sin(seg(t, .62, .7)*Math.PI) : 1})`});
      set('g0', {opacity: seg(t, .7, .75), transform:`translateX(${(1-ease(seg(t, .7, .76)))*-30}px)`});
      set('g1', {opacity: seg(t, .78, .83), transform:`translateX(${(1-ease(seg(t, .78, .84)))*-30}px)`});
    }
    """
    render_anim(html, js(code, X0=X0, X1=X1, VMAX=VMAX), f"{OUT}/08_envio_gratis_monto", segundos=8, portada_t=0.9)
