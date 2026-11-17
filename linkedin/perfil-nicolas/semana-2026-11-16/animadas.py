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
# 02 · Recordatorios de pago que salen solos
# =====================================================================================
if "02" in QUE:
    filas = [("Cliente 1", "05/11", "No"), ("Cliente 2", "10/11", "Sí"), ("Cliente 3", "12/11", "No")]
    tabla = '<div class="tabla"><div class="h">Cliente</div><div class="h">Vence</div><div class="h">Pagó</div>'
    for r, (a, b, p) in enumerate(filas):
        tabla += (f'<div id="r{r}a">{a}</div><div id="r{r}b">{b}</div>'
                  f'<div id="r{r}c" style="color:{"#d23c1b" if p == "No" else "#0f7a3d"};font-weight:800">{p}</div>')
    tabla += "</div>"
    v1 = tabla + ('<div class="mini" id="m1" style="left:16px;right:16px;bottom:18px;text-align:center;color:#ff8a8a;font-size:23px">'
                  '2 clientes sin pagar</div>')

    PEDIDO = ("Haceme el código de Apps Script que mande un recordatorio a los vencidos que no pagaron. "
              "Explicame dónde pegarlo.")
    v2 = (f'<div class="burb" id="b2" style="right:14px;top:14px;width:340px;background:#2b3245;border-radius:18px 18px 4px 18px"></div>'
          f'<div class="burb" id="c2" style="left:14px;bottom:14px;width:340px;background:#1c2230;border:1px solid #303850;'
          f'border-radius:18px 18px 18px 4px;padding:12px 14px;font-family:monospace;font-size:19px;color:{C[1]}">'
          '<div>function recordatorio() {</div><div id="l1" style="height:10px;margin:9px 0 0 18px;border-radius:5px;background:#3a4560"></div>'
          '<div id="l2" style="height:10px;margin:9px 0 0 18px;border-radius:5px;background:#3a4560"></div>'
          '<div id="l3" style="height:10px;margin:9px 0 0 18px;border-radius:5px;background:#3a4560"></div><div style="margin-top:6px">}</div></div>')

    menu = ('<div id="mn" style="position:absolute;inset:0">'
            '<div style="position:absolute;left:0;right:0;top:0;height:50px;background:#f1f3f4;display:flex;gap:22px;align-items:center;'
            'padding:0 16px;color:#3c4043;font-size:21px;font-weight:600"><span>Datos</span><span>Herramientas</span>'
            '<span id="ext" style="padding:5px 8px;border-radius:6px">Extensiones</span></div>'
            '<div id="dd" style="position:absolute;right:16px;top:52px;width:230px;background:#fff;border-radius:10px;'
            'box-shadow:0 10px 30px rgba(0,0,0,.5);color:#3c4043;font-size:21px;font-weight:600;overflow:hidden">'
            '<div style="padding:12px 16px">Complementos</div><div style="padding:12px 16px">Macros</div>'
            '<div id="as" style="padding:12px 16px">Apps Script</div></div></div>'
            '<div id="ed" style="position:absolute;inset:0;background:#1e1e1e">'
            '<div style="height:50px;background:#2d2d2d;display:flex;align-items:center;justify-content:space-between;padding:0 14px;'
            'font-size:20px;font-weight:700;color:#ddd"><span>Apps Script</span>'
            f'<span id="gu" style="padding:6px 14px;border-radius:8px;background:#3a3a3a">Guardar</span></div>'
            '<div style="padding:14px 18px;font-family:monospace;font-size:19px;color:#9cdcfe">'
            + "".join(f'<div id="p{k}" style="height:11px;margin:12px 0 0 {0 if k in (0, 5) else 22}px;width:{w}px;border-radius:6px;'
                      f'background:{C[2] if k in (0, 5) else "#4a4a4a"}"></div>' for k, w in enumerate([210, 280, 240, 300, 200, 40]))
            + '</div><div id="ok" style="position:absolute;left:0;right:0;bottom:16px;text-align:center;font-size:22px;font-weight:800;'
            f'color:{C[2]}">Guardado ✓</div></div>' + CURSOR.format(id="cu3"))

    cli = "".join(f'<div style="position:absolute;right:16px;top:{40 + 92 * k}px;width:190px;height:74px;border-radius:14px;'
                  f'background:#1c2230;border:1px solid #303850;display:flex;align-items:center;gap:12px;padding:0 14px;font-size:21px;font-weight:700">'
                  f'<span id="ck{k}" style="width:30px;height:30px;border-radius:50%;background:#2a3142;display:flex;align-items:center;'
                  f'justify-content:center;font-size:18px;color:#0d0f14">✓</span>Cliente {n}</div>' for k, n in enumerate([1, 3]))
    v4 = ('<svg style="position:absolute;left:22px;top:30px" width="170" height="170" viewBox="0 0 170 170">'
          '<circle cx="85" cy="85" r="78" fill="#1c2230" stroke="#ff4f8b" stroke-width="6"/>'
          + "".join(f'<line x1="85" y1="14" x2="85" y2="26" stroke="#7d8597" stroke-width="5" stroke-linecap="round" transform="rotate({a} 85 85)"/>'
                    for a in range(0, 360, 30))
          + '<line id="hm" x1="85" y1="85" x2="85" y2="34" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
          '<line id="hh" x1="85" y1="85" x2="85" y2="52" stroke="#ff4f8b" stroke-width="9" stroke-linecap="round"/>'
          '<circle cx="85" cy="85" r="8" fill="#fff"/></svg>'
          '<div class="mini" id="h9" style="left:22px;width:170px;top:214px;text-align:center;font-size:24px;font-weight:800">Todos los días</div>'
          + cli
          + "".join(f'<div id="sb{k}" style="position:absolute;left:0;top:0">{SOBRE.format(w=44, h=33, c=C[3])}</div>' for k in range(2)))

    tarjetas = [
        tarjeta(1, "Armá la planilla", v1, "Columnas: <b>cliente, mail, vence y pagó</b>. Uno por fila.", C[0]),
        tarjeta(2, "Pedile el código", v2, "Pegá el pedido en <b>Claude o ChatGPT</b>. Son gratis.", C[1]),
        tarjeta(3, "Pegalo en Sheets", menu, "<b>Extensiones → Apps Script</b>. Pegá el código y Guardar.", C[2]),
        tarjeta(4, "Que salga solo", v4, "<b>Reloj → Añadir activador</b> y elegí una vez por día.", C[3]),
    ]
    html = pieza('Recordatorios de pago<br><em>que salen solos</em>', "4 pasos en Google Sheets. Sin saber programar.",
                 tarjetas, "<b>Antes de activarlo:</b> probalo con tu propio mail.")
    js = f"""
    const PEDIDO = {PEDIDO!r};
    function frame(t) {{
      const out = 1 - seg(t, .94, 1);                       // fundido para cerrar el bucle
      // 1 · la planilla se llena y marca a los que no pagaron
      for (let r = 0; r < 3; r++) {{
        const a = ease(seg(t, .04 + .09*r, .12 + .09*r)) * out;
        ['a','b','c'].forEach(k => set('r'+r+k, {{opacity:a, transform:`translateX(${{(1-a)*-20}}px)`}}));
      }}
      const rojo = ease(seg(t, .42, .5)) * out;
      [0,2].forEach(r => set('r'+r+'c', {{background:`rgba(210,60,27,${{.18*rojo}})`}}));
      set('m1', {{opacity:rojo, transform:`translateY(${{(1-rojo)*12}}px)`}});
      // 2 · el pedido se escribe y vuelve el código
      const rc = ease(seg(t, .48, .58)) * out;
      set('b2', {{opacity: seg(t,.02,.06)*out*(1-.55*rc), transform:`translateY(${{-rc*120}}px)`}});
      $('b2').textContent = typed(PEDIDO, seg(t, .04, .42)) || ' ';
      set('c2', {{opacity:rc, transform:`translateY(${{(1-rc)*30}}px)`}});
      [1,2,3].forEach(k => set('l'+k, {{width: (ease(seg(t, .55+.06*k, .64+.06*k)) * [190,150,170][k-1]) + 'px'}}));
      // 3 · Extensiones -> Apps Script -> pegar -> Guardar
      const ab = seg(t, .2, .24) > 0 && t < .5;
      set('dd', {{opacity: ab ? 1 : 0, transform:`translateY(${{ab?0:-8}}px)`}});
      set('ext', {{background: t > .18 && t < .5 ? '#d3e3fd' : 'transparent'}});
      set('as', {{background: t > .38 && t < .5 ? '#d3e3fd' : '#fff'}});
      const ed = seg(t, .48, .53);
      set('mn', {{opacity:1-ed}}); set('ed', {{opacity:ed * out}});
      for (let k = 0; k < 6; k++) set('p'+k, {{opacity: seg(t, .56 + .025*k, .58 + .025*k)}});
      const gu = t > .76 && t < .82;
      set('gu', {{background: gu ? '{C[2]}' : '#3a3a3a', color: gu ? '#0d0f14' : '#ddd'}});
      set('ok', {{opacity: seg(t, .8, .84) * out}});
      let cx, cy;
      if (t < .5) {{
        const m1 = ease(seg(t, .05, .18)), m2 = ease(seg(t, .26, .37));
        cx = mix(mix(150, 330, m1), 280, m2); cy = mix(mix(180, 22, m1), 160, m2);
      }} else {{
        const m3 = ease(seg(t, .66, .76));
        cx = mix(150, 380, m3); cy = mix(200, 26, m3);
      }}
      set('cu3', {{left: cx+'px', top: cy+'px', opacity: out, transform: `scale(${{(t>.17&&t<.2)||(t>.37&&t<.4)||gu ? .82 : 1}})`}});
      // 4 · el reloj llega a la mañana y salen los mails
      const g = ease(seg(t, 0, .38));
      $('hm').setAttribute('transform', `rotate(${{g*720}} 85 85)`);
      $('hh').setAttribute('transform', `rotate(${{210 + g*60}} 85 85)`);
      set('h9', {{color: t > .38 && t < .94 ? '{C[3]}' : '#fff'}});
      [0,1].forEach(k => {{
        const f = ease(seg(t, .42 + .14*k, .6 + .14*k));
        set('sb'+k, {{opacity: f > 0 && f < 1 ? 1 : 0, transform:`translate(${{mix(80, 300, f)}}px, ${{mix(90, 60 + 92*k, f) - Math.sin(f*Math.PI)*50}}px)`}});
        set('ck'+k, {{background: f >= 1 && out > .5 ? '{C[3]}' : '#2a3142'}});
      }});
    }}
    """
    render_anim(html, js, f"{OUT}/02_recordatorio_de_pagos_animado", portada_t=0.86)
