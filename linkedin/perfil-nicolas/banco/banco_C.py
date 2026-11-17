"""Banco de infografías animadas · tanda C (piezas 09 a 12).
Ejecutar desde cualquier lado:  python3 banco_C.py [09 10 11 12]   (OUT=carpeta opcional)
Cada pieza tiene su propia composición, fondo y paleta (regla de variedad, 17/11/2026).
"""
import json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
from kit_animado import render_anim

OUT = os.environ.get("OUT", AQUI)
QUE = sys.argv[1:] or ["09", "10", "11", "12"]
KITF = os.path.join(os.path.dirname(os.path.dirname(AQUI)), "kit", "fonts")
ARCHIVO = "".join(f'@font-face{{font-family:Archivo;src:url("file://{KITF}/Archivo-{w}.ttf");font-weight:{w}}}' for w in (500, 600, 700, 800))
J = json.dumps

UTIL = """
const AR = n => Math.round(n).toLocaleString('es-AR');
const pop = (id, x) => set(id, {opacity: ease(cl(x)), transform:`scale(${.7 + .3*ease(cl(x))})`});
const sube = (id, x, d=24) => set(id, {opacity: ease(cl(x)), transform:`translateY(${(1-ease(cl(x)))*d}px)`});
"""

# =====================================================================================
# 09 · CARBÓN + NARANJA · pila de cajas que baja día a día hasta el punto de pedido
# =====================================================================================
if "09" in QUE:
    NA = "#ff7a1a"
    css = ARCHIVO + f"""
    #pz {{ padding:0 !important; background:#1c1c1e !important; color:#fff; font-family:Inter,sans-serif; }}
    .t9 {{ position:absolute; left:72px; top:64px; font:800 76px/1.0 Archivo; letter-spacing:-0.04em; }}
    .t9 em {{ font-style:normal; color:{NA}; }}
    .s9 {{ position:absolute; left:72px; top:236px; font:600 28px Inter; color:#a8a8ad; }}
    .caja {{ position:absolute; left:90px; width:300px; height:54px; border-radius:8px; background:#c98a4b;
             border:3px solid #8a5a2b; display:flex; align-items:center; justify-content:center; }}
    .caja::before {{ content:''; position:absolute; left:50%; top:0; bottom:0; width:34px; margin-left:-17px; background:#e3b07a; }}
    .caja span {{ position:relative; font:700 18px Inter; color:#4a2f14; }}
    .piso {{ position:absolute; left:70px; width:340px; top:1150px; height:6px; border-radius:3px; background:#55555a; }}
    .linea {{ position:absolute; left:60px; width:960px; height:0; border-top:5px dashed #6a4a2c; }}
    .linea b {{ position:absolute; left:360px; top:-22px; font:800 26px Inter; color:#6a4a2c; background:#1c1c1e; padding:0 10px; }}
    .panel {{ position:absolute; left:470px; right:72px; }}
    .dia {{ font:700 30px Inter; color:#a8a8ad; }}
    .stock {{ font:800 120px/1 Archivo; letter-spacing:-0.05em; }}
    .stock small {{ font:700 30px Inter; letter-spacing:0; color:#a8a8ad; margin-left:10px; }}
    .cuenta {{ position:absolute; left:470px; right:72px; top:800px; }}
    .cuenta div {{ font:700 32px/1.45 Inter; color:#e5e5ea; }}
    .cuenta div b {{ color:{NA}; }}
    .cuenta .tot {{ margin-top:10px; padding-top:12px; border-top:3px solid #3a3a3e; font:800 44px Archivo; color:#fff; }}
    .ya {{ position:absolute; left:470px; top:620px; padding:16px 26px; border-radius:16px; background:{NA}; color:#1c1c1e;
           font:800 44px Archivo; letter-spacing:-0.02em; box-shadow:0 0 0 0 rgba(255,122,26,.6); }}
    .pie9 {{ position:absolute; left:72px; right:72px; bottom:44px; display:flex; justify-content:space-between; font:700 24px Inter; color:#a8a8ad; }}
    .pie9 b {{ color:#fff; }}
    """
    N_CAJAS = 12                # cada caja = 10 unidades; arranca con 120
    BASE = 1150; ALTO = 60
    cajas = "".join(f'<div class="caja" id="cj{k}" style="top:{BASE - ALTO * (k + 1)}px"><span>10 u.</span></div>' for k in range(N_CAJAS))
    y70 = BASE - ALTO * 7 - 3
    html = (f'<style>{css}</style><div id="pz">'
            f'<div class="t9">¿Cuándo tenés que<br>volver a <em>pedir stock?</em></div>'
            f'<div class="s9">Una cuenta simple para no quedarte sin mercadería.</div>'
            f'{cajas}<div class="piso"></div>'
            f'<div class="linea" id="li" style="top:{y70}px"><b id="lb">70</b></div>'
            f'<div class="panel" style="top:400px"><div class="dia" id="dia">Día 0</div>'
            f'<div class="stock"><span id="st">120</span><small>unidades</small></div></div>'
            f'<div class="ya" id="ya">¡Pedí ahora!</div>'
            f'<div class="cuenta">'
            f'<div id="c1"><b>5</b> ventas por día</div>'
            f'<div id="c2">× <b>10</b> días que tarda el proveedor</div>'
            f'<div id="c3">+ <b>20</b> de reserva por las dudas</div>'
            f'<div class="tot" id="c4">= pedí cuando te queden 70</div></div>'
            f'<div class="pie9"><span><b>Nicolás Benítez</b></span><span>Así no te quedás sin stock mientras llega el pedido.</span></div></div>')
    js = UTIL + """
    const NA = '#ff7a1a';
    function frame(t) {
      const out = 1 - seg(t, .95, 1);
      document.querySelectorAll('#pz > *').forEach(e => e.style.opacity = out);
      // la cuenta aparece de a una línea
      sube('c1', seg(t, .04, .1)); sube('c2', seg(t, .1, .16)); sube('c3', seg(t, .16, .22));
      // pasan los días: 120 -> 70 (5 por día, 10 días)
      const d = ease(seg(t, .26, .7));
      const stock = 120 - 50 * d;
      $('st').textContent = AR(stock);
      $('dia').textContent = 'Día ' + Math.round(10 * d);
      for (let k = 0; k < 12; k++) {
        const nivel = (stock - 10 * k) / 10;          // 1 = caja entera, 0 = vacía
        set('cj'+k, {opacity: cl(nivel), transform:`translateY(${(1 - cl(nivel)) * -30}px)`});
      }
      const ya = t > .7;
      set('li', {borderTopColor: ya ? NA : '#6a4a2c', borderTopStyle: ya ? 'solid' : 'dashed'});
      set('lb', {color: ya ? NA : '#6a4a2c'});
      set('st', {color: ya ? NA : '#fff'});
      const p = seg(t, .7, .76);
      pop('ya', p);
      set('ya', {opacity: ease(p) * out, boxShadow: `0 0 0 ${ya ? 10 + Math.sin(t*60)*8 : 0}px rgba(255,122,26,.25)`});
      sube('c4', seg(t, .74, .8));
    }
    """
    render_anim(html, js, f"{OUT}/09_punto_de_pedido", segundos=8, portada_t=0.9)

# =====================================================================================
# 10 · VERDE MUY OSCURO · chat genérico con atajos de respuestas guardadas
# =====================================================================================
if "10" in QUE:
    VE = "#3ddc97"
    css = f"""
    #pz {{ padding:0 !important; background:#0a1a14 !important; color:#fff; font-family:Inter,sans-serif; }}
    .t10 {{ position:absolute; left:72px; right:72px; top:60px; font:800 70px/1.02 'Inter Display',Inter; letter-spacing:-0.04em; }}
    .t10 em {{ font-style:normal; color:{VE}; }}
    .s10 {{ position:absolute; left:72px; right:72px; top:226px; font:600 27px/1.35 Inter; color:#9fbcae; }}
    .s10 b {{ color:#fff; }}
    .tel {{ position:absolute; left:110px; right:110px; top:340px; height:680px; border-radius:40px; background:#10261d;
            border:3px solid #1f3d31; overflow:hidden; }}
    .cab {{ height:84px; background:#143126; display:flex; align-items:center; gap:16px; padding:0 26px; font:700 26px Inter; }}
    .cab i {{ width:48px; height:48px; border-radius:50%; background:#2b5546; display:block; }}
    .cab small {{ display:block; font:500 19px Inter; color:#9fbcae; }}
    .msg {{ position:absolute; max-width:700px; padding:18px 24px; border-radius:24px; font:600 31px/1.32 Inter; }}
    .cli {{ left:26px; background:#1d3a2f; border-radius:22px 22px 22px 6px; }}
    .yo {{ right:26px; background:#1f6b4d; border-radius:22px 22px 6px 22px; }}
    .inp {{ position:absolute; left:20px; right:20px; bottom:20px; height:70px; border-radius:35px; background:#1a3328; display:flex;
            align-items:center; padding:0 28px; font:700 28px Inter; color:{VE}; }}
    .inp .ph {{ color:#5f8172; font-weight:600; }}
    .cur {{ display:inline-block; width:3px; height:30px; background:{VE}; margin-left:3px; }}
    .atajos {{ position:absolute; left:72px; right:72px; top:1052px; display:flex; gap:14px; justify-content:center; }}
    .at {{ padding:12px 20px; border-radius:99px; border:2px solid #2b5546; font:800 25px Inter; color:#9fbcae; }}
    .at.on {{ background:{VE}; border-color:{VE}; color:#0a1a14; }}
    .pie10 {{ position:absolute; left:72px; right:72px; bottom:44px; display:flex; justify-content:space-between; font:700 23px Inter; color:#9fbcae; }}
    .pie10 b {{ color:#fff; }}
    """
    CASOS = [("¿Hasta qué hora atienden?", "/horarios", "Atendemos de lunes a viernes de 9 a 18 h. Estamos en [tu dirección]."),
             ("¿Cómo puedo pagar?", "/pagos", "Tarjeta de crédito o débito, transferencia y billeteras virtuales."),
             ("¿Cuánto sale el envío?", "/envios", "Enviamos a todo el país. Pasame tu código postal y te digo costo y demora."),
             ("¿Lo puedo cambiar?", "/cambios", "Sí, tenés [X] días. Escribinos con tu número de pedido y lo coordinamos.")]
    html = (f'<style>{css}</style><div id="pz">'
            f'<div class="t10">4 respuestas que tenés<br>que tener <em>guardadas</em></div>'
            f'<div class="s10">Con las <b>respuestas rápidas de WhatsApp Business</b>:<br>escribís el atajo y aparece el mensaje entero.</div>'
            f'<div class="tel"><div class="cab"><i></i><div>Cliente<small>en línea</small></div></div>'
            f'<div class="msg cli" id="q"></div><div class="msg yo" id="r"></div>'
            f'<div class="inp"><span id="tx"></span><span class="cur" id="cu"></span><span class="ph" id="ph">Mensaje</span></div></div>'
            f'<div class="atajos">' + "".join(f'<div class="at" id="at{k}">{c[1]}</div>' for k, c in enumerate(CASOS)) + '</div>'
            f'<div class="pie10"><span><b>Nicolás Benítez</b></span><span>Las armás una vez y las usás todos los días.</span></div></div>')
    js = UTIL + "const CASOS = " + J(CASOS) + """;
    function frame(t) {
      const out = 1 - seg(t, .96, 1);
      document.querySelectorAll('#pz > *').forEach(e => e.style.opacity = out);
      const W = .24, k = Math.min(3, Math.floor(t / W)), u = (t - k * W) / W;   // u: avance dentro del caso k
      const [q, atajo, resp] = CASOS[k];
      $('q').textContent = q; $('r').textContent = resp;
      sube('q', seg(u, .02, .14), 20); set('q', {top: '120px'});
      const escribe = seg(u, .16, .46);
      const enviado = u > .54;
      $('tx').textContent = enviado ? '' : typed(atajo, escribe);
      set('ph', {display: (escribe > 0 && !enviado) ? 'none' : 'inline'});
      set('cu', {opacity: (!enviado && Math.floor(t*30) % 2 === 0) ? 1 : 0});
      const r = seg(u, .54, .62);
      set('r', {top: '250px', opacity: ease(r), transform:`scale(${.85 + .15*ease(r)})`, transformOrigin:'right top'});
      for (let i = 0; i < 4; i++) $('at'+i).classList.toggle('on', i === k && u > .2);
    }
    """
    render_anim(html, js, f"{OUT}/10_respuestas_guardadas_whatsapp", segundos=8, portada_t=0.83)

# =====================================================================================
# 11 · LILA CLARO + VIOLETA · línea de tiempo horizontal con 3 sobres que viajan y se abren
# =====================================================================================
if "11" in QUE:
    VI = "#6d28d9"; TI = "#1b1530"
    css = ARCHIVO + f"""
    #pz {{ padding:0 !important; background:#ece6ff !important; color:{TI}; font-family:Inter,sans-serif; }}
    .t11 {{ position:absolute; left:72px; top:70px; font:800 80px/1.0 Archivo; letter-spacing:-0.04em; }}
    .t11 em {{ font-style:normal; color:{VI}; }}
    .s11 {{ position:absolute; left:72px; top:262px; font:600 29px Inter; color:#5d5478; }}
    .eje {{ position:absolute; left:110px; right:110px; top:560px; height:8px; border-radius:4px; background:#cfc3f5; }}
    .eje i {{ position:absolute; left:0; top:0; height:8px; border-radius:4px; background:{VI}; }}
    .hito {{ position:absolute; top:546px; width:36px; height:36px; margin-left:-18px; border-radius:50%; background:#ece6ff; border:6px solid #cfc3f5; }}
    .cuando {{ position:absolute; top:470px; width:280px; margin-left:-140px; text-align:center; font:800 25px Inter; color:{VI}; }}
    .cuando span {{ display:inline-block; padding:8px 16px; border-radius:99px; background:#fff; }}
    .sobre {{ position:absolute; top:520px; margin-left:-48px; width:96px; height:70px; z-index:4; }}
    .tarj {{ position:absolute; top:640px; width:290px; margin-left:-145px; border-radius:24px; background:#fff; padding:24px 22px 26px;
             box-shadow:0 18px 40px rgba(60,30,140,.16); }}
    .tarj .ev {{ font:700 21px Inter; color:#7c72a0; }}
    .tarj h4 {{ margin-top:6px; font:800 33px/1.05 Archivo; letter-spacing:-0.02em; }}
    .tarj .as {{ margin-top:16px; padding:14px 14px; border-radius:14px; background:#f3efff; font:600 22px/1.3 Inter; color:{TI}; }}
    .tarj .as small {{ display:block; font:800 16px Inter; letter-spacing:.1em; color:{VI}; margin-bottom:6px; }}
    .s11b {{ position:absolute; left:72px; right:72px; top:1110px; font:700 32px/1.3 Inter; text-align:center; }}
    .s11b b {{ color:{VI}; }}
    .pie11 {{ position:absolute; left:72px; right:72px; bottom:44px; display:flex; justify-content:space-between; font:700 24px Inter; color:#5d5478; }}
    .pie11 b {{ color:{TI}; }}
    """
    XS = [200, 540, 880]
    MAILS = [("Día 0", "Cuando se suscribe", "Bienvenida", "¡Bienvenido! Esto es lo que te espera"),
             ("A las pocas horas", "Cuando deja el carrito", "Carrito abandonado", "Te guardamos el carrito"),
             ("Unos días después", "Cuando ya recibió la compra", "Después de la compra", "¿Qué te pareció tu compra?")]
    sobre_svg = ('<svg viewBox="0 0 96 70" width="96" height="70"><rect x="2" y="2" width="92" height="66" rx="10" fill="#6d28d9"/>'
                 '<path id="{fid}" d="M4 6 L48 40 L92 6" fill="none" stroke="#fff" stroke-width="5" stroke-linejoin="round"/></svg>')
    html = (f'<style>{css}</style><div id="pz">'
            f'<div class="t11">3 mails que tu tienda<br>tiene que mandar <em>sola</em></div>'
            f'<div class="s11">Los armás una vez y salen solos, en el momento justo.</div>'
            f'<div class="eje"><i id="ej"></i></div>'
            + "".join(f'<div class="hito" id="h{k}" style="left:{x}px"></div>'
                      f'<div class="cuando" id="w{k}" style="left:{x}px"><span>{m[0]}</span></div>'
                      f'<div class="tarj" id="tj{k}" style="left:{x}px"><div class="ev">{m[1]}</div><h4>{m[2]}</h4>'
                      f'<div class="as"><small>ASUNTO</small>{m[3]}</div></div>'
                      for k, (x, m) in enumerate(zip(XS, MAILS)))
            + f'<div class="sobre" id="sb">{sobre_svg.format(fid="fl")}</div>'
            f'<div class="s11b">Bienvenida, carrito y reseña: <b>3 momentos en los que el cliente ya está mirando.</b></div>'
            f'<div class="pie11"><span><b>Nicolás Benítez</b></span><span>¿Ya los tenés armados?</span></div></div>')
    js = UTIL + "const XS = " + J(XS) + """;
    function frame(t) {
      const out = 1 - seg(t, .95, 1);
      document.querySelectorAll('#pz > *').forEach(e => e.style.opacity = out);
      // el sobre viaja: 0 -> hito 0 -> hito 1 -> hito 2, con una parada en cada uno
      const L = [[.04,.12], [.3,.42], [.58,.7]];         // tramos de viaje hacia cada hito
      let x = 40, abierto = false;
      for (let k = 0; k < 3; k++) {
        const [a, b] = L[k];
        if (t >= a) x = mix(k ? XS[k-1] : 40, XS[k], ease(seg(t, a, b)));
        const llego = t >= b;
        if (llego && t < (k < 2 ? L[k+1][0] : .9)) abierto = true;
        set('h'+k, {background: llego ? '#6d28d9' : '#ece6ff', borderColor: llego ? '#6d28d9' : '#cfc3f5'});
        sube('w'+k, seg(t, b - .06, b));
        sube('tj'+k, seg(t, b, b + .07), 30);
      }
      const salto = Math.abs(Math.sin(t * 50)) * (abierto ? 0 : 10);
      set('sb', {left: x + 'px', transform:`translateY(${-salto}px) rotate(${abierto ? -8 : 0}deg)`});
      $('fl').setAttribute('d', abierto ? 'M4 6 L48 -18 L92 6' : 'M4 6 L48 40 L92 6');
      $('ej').style.width = cl((x - 110) / 860) * 100 + '%';
      sube('s11b', seg(t, .8, .86));
    }
    """
    render_anim(html, js, f"{OUT}/11_tres_mails_automaticos", segundos=7, portada_t=0.9)

# =====================================================================================
# 12 · NEGRO + FRANJAS AMARILLAS · cartel de advertencia: 4 errores que se convierten en arreglos
# =====================================================================================
if "12" in QUE:
    AM = "#ffd000"; RO = "#ff3b30"; VE = "#30d158"
    franja = f"repeating-linear-gradient(-45deg, {AM} 0 34px, #0b0b0b 34px 68px)"
    css = ARCHIVO + f"""
    #pz {{ padding:0 !important; background:#0b0b0b !important; color:#fff; font-family:Inter,sans-serif; }}
    .fr {{ position:absolute; left:0; right:0; height:44px; background:{franja}; }}
    .fr.l {{ top:0; bottom:0; width:24px; height:auto; }}
    .t12 {{ position:absolute; left:72px; top:96px; font:800 92px/0.98 Archivo; letter-spacing:-0.045em; }}
    .t12 em {{ font-style:normal; color:#0b0b0b; background:{AM}; padding:0 14px; border-radius:8px; }}
    .s12 {{ position:absolute; left:72px; top:314px; font:600 29px Inter; color:#b5b5b5; }}
    .err {{ position:absolute; left:72px; right:72px; height:162px; border-radius:20px; background:#171717; overflow:hidden; border:2px solid #262626; }}
    .err .bar {{ position:absolute; left:0; top:0; bottom:0; width:12px; background:#3a3a3a; }}
    .err .ic {{ position:absolute; left:40px; top:50%; margin-top:-34px; width:68px; height:68px; border-radius:50%; display:flex;
                align-items:center; justify-content:center; font:900 36px Inter; color:#0b0b0b; background:#3a3a3a; }}
    .err .mal {{ position:absolute; left:136px; right:28px; top:50%; transform:translateY(-50%); }}
    .err .bien {{ position:absolute; left:136px; right:28px; bottom:30px; }}
    .err .k {{ font:800 19px Inter; letter-spacing:.14em; }}
    .err .x {{ margin-top:4px; font:700 30px/1.15 Inter; letter-spacing:-0.015em; }}
    .err .mal .k {{ color:{RO}; }} .err .bien .k {{ color:{VE}; }}
    .err .mal .x {{ text-decoration-color:{RO}; text-decoration-thickness:3px; }}
    .pie12 {{ position:absolute; left:72px; right:72px; bottom:72px; display:flex; justify-content:space-between; font:700 24px Inter; color:#b5b5b5; }}
    .pie12 b {{ color:#fff; }}
    """
    ERR = [("Pegar datos de clientes o contraseñas en el chat", "Borrá lo sensible o usá datos de ejemplo"),
           ("Publicar lo que escribe sin leerlo", "Leelo y corregilo antes de publicar"),
           ("Pedir sin contexto: “hacé un post”", "Contale para quién es, qué querés y cómo"),
           ("Creerle números que no le diste", "Los datos ponelos vos y chequeá cada cifra")]
    tops = [380 + 182 * k for k in range(4)]
    filas = "".join(f'<div class="err" id="e{k}" style="top:{tp}px"><div class="bar" id="eb{k}"></div><div class="ic" id="ei{k}">!</div>'
                    f'<div class="mal" id="em{k}"><div class="k">ERROR {k + 1}</div><div class="x">{a}</div></div>'
                    f'<div class="bien" id="ok{k}"><div class="x">{b}</div></div></div>'
                    for k, (tp, (a, b)) in enumerate(zip(tops, ERR)))
    html = (f'<style>{css}</style><div id="pz"><div class="fr" style="top:0"></div><div class="fr" style="bottom:0"></div>'
            f'<div class="t12"><em>4 errores</em> al usar<br>IA en tu negocio</div>'
            f'<div class="s12">Y cómo evitarlos sin dejar de usarla.</div>{filas}'
            f'<div class="pie12"><span><b>Nicolás Benítez</b></span><span>¿Cuál viste más seguido?</span></div></div>')
    js = UTIL + """
    const RO = '#ff3b30', VE = '#30d158';
    function frame(t) {
      const out = 1 - seg(t, .95, 1);
      document.querySelectorAll('#pz > *').forEach(e => e.style.opacity = out);
      for (let k = 0; k < 4; k++) {
        const a = .06 + .2 * k;                       // aparece el error k
        const ap = seg(t, a, a + .05);
        set('e'+k, {opacity: ease(ap) * out, transform:`translateX(${(1-ease(ap)) * -40}px)`});
        const tacha = t > a + .07;
        $('em'+k).querySelector('.x').style.textDecorationLine = tacha ? 'line-through' : 'none';
        const fx = seg(t, a + .11, a + .15);
        const ok = fx > 0;
        // el error queda arriba, tachado y más chico; el arreglo aparece abajo
        const e = ease(fx);
        $('em'+k).querySelector('.k').style.display = ok ? 'none' : 'block';
        set('em'+k, {top: mix(81, 30, e) + 'px', transform:`translateY(${-50 * (1-e)}%)`, opacity: 1 - .5*e,
                     fontSize: '1px'});
        $('em'+k).querySelector('.x').style.fontSize = mix(30, 23, e) + 'px';
        $('em'+k).querySelector('.x').style.color = ok ? '#8e8e93' : '#fff';
        set('ok'+k, {opacity: ease(fx), transform:`translateY(${(1-ease(fx))*20}px)`});
        const col = ok ? VE : (t >= a ? RO : '#3a3a3a');
        set('eb'+k, {background: col}); set('ei'+k, {background: col});
        $('ei'+k).textContent = ok ? '✓' : '✕';
        set('e'+k, {borderColor: ok ? 'rgba(48,209,88,.45)' : (t >= a ? 'rgba(255,59,48,.5)' : '#262626')});
      }
    }
    """
    render_anim(html, js, f"{OUT}/12_errores_ia_negocio", segundos=8, portada_t=0.92)
